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
iIii1 = "2.3.4"
oOOoO0 = xbmc . translatePath ( 'special://database' )
O0OoO000O0OO = xbmc . translatePath ( 'special://thumbnails' ) ;
iiI1IiI = "GenieTv"
II = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
ooOoOoo0O = 'http://'
OooO0 = o0oOoO00o . getLocalizedString
II11iiii1Ii = CookieJar ( )
OO0o = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( II11iiii1Ii ) )
OO0o . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
Ooo = int ( sys . argv [ 1 ] )
if 68 - 68: o0000oOoOoO0o + OoOO0ooOOoo0O . iIii1I11I1II1 - IIII % iIii1I11I1II1 - o0oO0
def oOOO00o ( ) :
 O0O00o0OOO0 ( '[COLORgreen]WIZARD[/COLOR]' , II , 4001 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]STREAMS[/COLOR]' , II , 4002 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC[/COLOR]' , II , 4003 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 if 27 - 27: O0 % i1IIi * OoOO + i11iIiiIii + OoooooooOO * i1IIi
 O0O00o0OOO0 ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , II , 32 , OOooO0OOoo + 'builderstoolbox.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SOURCE LIST[/COLOR]' , II , 46 , OOooO0OOoo + 'sources.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MAINTENANCE[/COLOR]' , II , 3 , OOooO0OOoo + 'MAIN6.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ADDONS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , OOooO0OOoo + 'ADDONS.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]APK TOOL[/COLOR]' , II , 2 , OOooO0OOoo + 'APK.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , II , 39 , OOooO0OOoo + 'RSS.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ADDONS PACKS[/COLOR]' , II , 30 , OOooO0OOoo + 'ADDONP.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 80 - 80: i1IIi
def oOOO0o0o ( ) :
 O0O00o0OOO0 ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , II , 49 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]WIPE GENIE[/COLOR]' , II , 41 , OOooO0OOoo + 'wipegenie.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]WISHES PC[/COLOR]' , II , 1 , OOooO0OOoo + 'WISHESPC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]WISHES ANDROID[/COLOR]' , II , 44 , OOooO0OOoo + 'WISHESAN.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
def iiI1 ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SEARCH[/COLOR]' , II , 9000 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]GenieTv VOD[/COLOR]' , II , 1005 , OOooO0OOoo + 'vod.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]POPCORN BOX[/COLOR]' , II , 7061 , OOooO0OOoo + 'popcorn.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]RECENT EPISODES[/COLOR]' , II , 8081 , OOooO0OOoo + 'recent.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ANIME[/COLOR]' , II , 1001 , OOooO0OOoo + 'anime.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CLASSIC TOONS[/COLOR]' , II , 8050 , OOooO0OOoo + 'classictoons.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CHAMPION IPTV[/COLOR]' , II , 9020 , OOooO0OOoo + 'UKiptvandvod.png' , ii11iIi1I , 'UK IPTV AND HD VOD' )
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , II , 1023 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) ) , 1016 , OOooO0OOoo + 'reap.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , II , 8040 , OOooO0OOoo + 'documentary.png' , ii11iIi1I , '' )
 if 19 - 19: o0000oOoOoO0o + o0oO0
 O0O00o0OOO0 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , II , 3000 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 53 - 53: OoooooooOO . i1IIi
 if 18 - 18: OOooOOo
 if 28 - 28: OoOO0ooOOoo0O - IIII . IIII + I1IiI - OoooooooOO + O0
 if 95 - 95: Ooo00oOo00o % OoOO . O0
 if 15 - 15: o0oO0 / o00O0oo . o00O0oo - i1IIi
 if 53 - 53: IIII + OOOo0 * OoOO
 O0O00o0OOO0 ( '[COLORgreen]M3U STREAMS[/COLOR]' , II , 8070 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 if 61 - 61: i1IIi * OoOO0ooOOoo0O / OoooooooOO . i11iIiiIii . I1IiI
 if 60 - 60: o0000oOoOoO0o / o0000oOoOoO0o
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 46 - 46: o00O0oo * OoOO0ooOOoo0O - Ooo00oOo00o * OoOO - O0oO
 if 83 - 83: OoooooooOO
 if 31 - 31: OoOoOO00 - OoOO0ooOOoo0O . O0oO % I1IiI - O0
 if 4 - 4: OoOoOO00 / o0oO0 . oO0o0ooO0
def O0oo0OO0oOOOo ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , II , 1024 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 if 35 - 35: IIII % OOOo0
def o0OOoo0OO0OOO ( ) :
 O0O00o0OOO0 ( '[COLORgreen]Live Tv[/COLOR]' , II , 9021 , OOooO0OOoo + 'english.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]XXX[/COLOR]' , II , 9022 , OOooO0OOoo + 'xxx.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]Hd VOD[/COLOR]' , II , 9023 , OOooO0OOoo + 'vod(1).png' , ii11iIi1I , '' )
 if 19 - 19: OoOO % i1IIi % OOooOOo
 if 93 - 93: iIii1I11I1II1 % OoOO * i1IIi
def Ii11Ii1I ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , II , 9001 , OOooO0OOoo + 'MOVIESv.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , II , 9002 , OOooO0OOoo + 'TVSHOWSv.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , II , 9003 , OOooO0OOoo + 'livetv.png' , ii11iIi1I , '' )
 if 72 - 72: oO0o0ooO0 / i1IIi * Oo - O0oO
def Oo0O0O0ooO0O ( ) :
 O0O00o0OOO0 ( '[COLORgreen]RADIO[/COLOR]' , II , 1013 , OOooO0OOoo + 'radio.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC[/COLOR]' , II , 1030 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , II + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , II , 1111 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / OoOO0ooOOoo0O
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 58 - 58: i11iIiiIii % o0000oOoOoO0o
def OO00Oo ( ) :
 O0OOO0OOoO0O ( 'DELETE CACHE' , 'url' , 14 , OOooO0OOoo + 'MAIN5.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'DELETE PACKAGES' , 'url' , 6 , OOooO0OOoo + 'MAIN4.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'FORCE REFRESH' , 'url' , 10 , OOooO0OOoo + 'MAIN3.png' , ii11iIi1I , 'Force Refresh All Repos' )
 if 70 - 70: IIII * Oo * o0000oOoOoO0o / o00O0oo
 O0OOO0OOoO0O ( 'CHECK MY IP' , 'url' , 12 , OOooO0OOoo + 'MAIN2.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , OOooO0OOoo + 'MAIN1.png' , ii11iIi1I , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0O00o0OOO0 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , II , 4 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]URL FIXES[/COLOR]' , II , 20 , OOooO0OOoo + 'URLFIX.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 88 - 88: O0
 if 64 - 64: o0000oOoOoO0o * O0 + IIII - OoOO0ooOOoo0O + i11iIiiIii * o00O0oo
def iII ( ) :
 O0O00o0OOO0 ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , OOooO0OOoo + 'repos.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]NEW[/COLOR]' , II , 22 , OOooO0OOoo + 'NEW.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]IPTV[/COLOR]' , II , 23 , OOooO0OOoo + 'IPTV.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]VIDEO[/COLOR]' , II , 24 , OOooO0OOoo + 'VIDEO.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SPORTS[/COLOR]' , II , 25 , OOooO0OOoo + 'SPORTS.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]KIDS[/COLOR]' , II , 26 , OOooO0OOoo + 'KIDS.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC[/COLOR]' , II , 27 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]PROGRAMS[/COLOR]' , II , 28 , OOooO0OOoo + 'PROGRAMS.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , OOooO0OOoo + 'XXX.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 80 - 80: IIII . OoOO
 if 25 - 25: I1IiI . OoOoOO00 / oO0o0ooO0 . OoOO0ooOOoo0O * Ooo00oOo00o . OOOo0
def Oo0oOOo ( ) :
 O0OOO0OOoO0O ( 'CHECK ADVANCED XML' , II , 8 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'MUCKYS XML' , II + '/wizard/muckys.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( '0CACHE XML' , II + '/wizard/0cache.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'MIKEY1234 XML' , II + '/wizard/mikey.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'TUXENS XML' , II + '/wizard/tuxens.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'P2P RECOMMENDED XML1' , II + '/wizard/p2p1.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'P2P RECOMMENDED XML2' , II + '/wizard/p2p2.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'DELETE XML' , II , 11 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 58 - 58: OoOoOO00 * OoOO0ooOOoo0O * ii11ii1ii / OoOO0ooOOoo0O
def oO0o0OOOO ( ) :
 O0OOO0OOoO0O ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 if 68 - 68: oO0o0ooO0 - O0oO - OOOo0 - ii11ii1ii + o0000oOoOoO0o
def iiiI1I11i1 ( ) :
 O0OOO0OOoO0O ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , II + '/wizard/customftv/ftvguide-addons.zip' , 5 , OOooO0OOoo + 'FTV4.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'FTV GUIDE FIRST RUN SETTINGS' , II + '/wizard/customftv/settings.xml' , 17 , OOooO0OOoo + 'FTV3.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , OOooO0OOoo + 'FTV1.png' , ii11iIi1I , '' )
 O0OOO0OOoO0O ( 'RESET FTV DATABASE' , 'url' , 18 , OOooO0OOoo + 'FTV2.png' , ii11iIi1I , '' )
 if 49 - 49: OOOo0 % o0oO0 . o0oO0 . o0000oOoOoO0o * o0oO0
 if 97 - 97: o00O0oo + OOooOOo . OoOO0ooOOoo0O + ii11ii1ii % oO0o0ooO0
 if 95 - 95: i1IIi
def I1ii11iI ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SKINS[/COLOR]' , II , 33 , OOooO0OOoo + 'skinp.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , II , 34 , OOooO0OOoo + 'artp.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , i1iIIi1 , 35 , OOooO0OOoo + 'GUI.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 14 - 14: I1IiI / IIII . I1IiI . o0000oOoOoO0o % Ooo00oOo00o * o0000oOoOoO0o
def iIIoO00o0 ( url ) :
 OOoo0O = Oo0ooOo0o ( Ii1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 5 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 54 - 54: O0 - IIII % OoOO0ooOOoo0O
def OOoO ( ) :
 O0O00o0OOO0 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , II , 36 , OOooO0OOoo + 'GSKIN.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]HELIX SKINS[/COLOR]' , II , 37 , OOooO0OOoo + 'HSKIN.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , i1iIIi1 , 38 , OOooO0OOoo + 'ISKIN.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 46 - 46: Ooo00oOo00o . Oo - OoooooooOO
def ooo00OOOooO ( url ) :
 OOoo0O = Oo0ooOo0o ( II + O00OOOoOoo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 77 - 77: oO0o0ooO0 % oO0o0ooO0 * OoOO - i11iIiiIii
def Oo0oO ( url ) :
 OOoo0O = Oo0ooOo0o ( II + IIiIi1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 35 - 35: o00O0oo % O0 - O0
def IiIIIi1iIi ( url ) :
 OOoo0O = Oo0ooOo0o ( II + ooOOoooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 1 - 1: Oo / OOooOOo % oO0o0ooO0 * IIII . i11iIiiIii
def III1Iiii1I11 ( url ) :
 OOoo0O = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
def o00oooO0Oo ( url ) :
 OOoo0O = Oo0ooOo0o ( II + o0O0OOO0Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 40 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 45 - 45: O0 / OOooOOo
def i1IIIII11I1IiI ( url ) :
 OOoo0O = Oo0ooOo0o ( II + i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 5 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 72 - 72: i1IIi / Ooo00oOo00o + OoooooooOO - Oo
def iI1Iii ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00OOoO00 )
 for i1Ii , ii111iI1iIi1 , ooo0O in iiIii :
  OOO ( ooo0O , i1Ii , 2031 , OOooO0OOoo + 'APK.png' )
  if 68 - 68: OoOoOO00 + o0000oOoOoO0o
def I1I1I ( name , url , description ) :
 OoOO000 = xbmc . translatePath ( os . path . join ( i1Ii11i1i , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 o0oOOoo = os . path . join ( OoOO000 , name + '.apk' )
 try :
  os . remove ( o0oOOoo )
 except :
  pass
 downloader . download ( url , o0oOOoo , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 51 - 51: Oo * i11iIiiIii
def O0oo00o0O ( url ) :
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 o0oOOoo = os . path . join ( OoOO000 , ooo0O + '.mp4' )
 try :
  os . remove ( o0oOOoo )
 except :
  pass
 downloader . download ( url , o0oOOoo , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 1 - 1: OoOoOO00
 if 84 - 84: OOooOOo % OoOoOO00 . i11iIiiIii / Ooo00oOo00o
def o0O ( name , url , description ) :
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 o0oOOoo = os . path . join ( OoOO000 , name )
 try :
  os . remove ( o0oOOoo )
 except :
  pass
 downloader . download ( url , o0oOOoo , i1111 )
 IiII = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IiII
 print '======================================='
 extract . all ( o0oOOoo , IiII , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 25 - 25: O0 - O0 * OOooOOo
 if 51 - 51: Oo - OoOO + OoOoOO00 * o00O0oo . o0000oOoOoO0o + OoOO
def OoO0o ( url ) :
 OOoo0O = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 5 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 try :
  OOoo0O = Oo0ooOo0o ( oO0o0Ooooo + oooOOOOO + OOo0oO00ooO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
  for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
   O0O00o0OOO0 ( ooo0O , url , 5 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 except : pass
 o0oo0o0O00OO ( 'movies' , 'INFO' )
 if 90 - 90: I1IiI * O0oO + OOooOOo
 if 81 - 81: OoOO . OOooOOo % O0 / OOOo0 - OoOO
def Ii1I1i ( url ) :
 OOoo0O = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 43 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 try :
  OOoo0O = Oo0ooOo0o ( oO0o0Ooooo + oooOOOOO + OOo0oO00ooO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
  for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
   O0O00o0OOO0 ( ooo0O , url , 43 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 except : pass
 o0oo0o0O00OO ( 'movies' , 'INFO' )
 if 99 - 99: OoOO . oO0o0ooO0 + o0oO0 % OoOO . i11iIiiIii % O0
 if 78 - 78: ii11ii1ii + OoOO0ooOOoo0O - O0oO
def IIIIii1I ( name , url , description ) :
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o0oOOoo = os . path . join ( OoOO000 , name + '.zip' )
 try :
  os . remove ( o0oOOoo )
 except :
  pass
 downloader . download ( url , o0oOOoo , i1111 )
 IiI1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiI1i
 print '======================================='
 extract . all ( o0oOOoo , IiI1i , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 o0Oo00 ( )
 if 32 - 32: OOooOOo . IIII * o0000oOoOoO0o
 if 93 - 93: OOooOOo % i1IIi . o00O0oo . i11iIiiIii
def oOOoo00O00o ( name , url , description ) :
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o0oOOoo = os . path . join ( OoOO000 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o0oOOoo )
 except :
  pass
 downloader . download ( url , o0oOOoo , i1111 )
 IiI1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiI1i
 print '======================================='
 extract . all ( o0oOOoo , IiI1i , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 O0O00Oo ( )
 if 97 - 97: O0 * OoooooooOO . OoooooooOO
def I111iI ( name , url , description ) :
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o0oOOoo = os . path . join ( OoOO000 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o0oOOoo )
 except :
  pass
 downloader . download ( url , o0oOOoo , i1111 )
 IiI1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiI1i
 print '======================================='
 extract . all ( o0oOOoo , IiI1i , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 56 - 56: OOOo0
 if 54 - 54: O0oO / OoOO0ooOOoo0O . OoOO % oO0o0ooO0
def OoO0OOOOo0O ( name , url , description ) :
 IiI1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 o0oOOoo = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IiI1i
 print '======================================='
 extract . all ( o0oOOoo , IiI1i , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 81 - 81: O0 / Ooo00oOo00o . i1IIi + OOOo0 - o0000oOoOoO0o
 if 74 - 74: iIii1I11I1II1 * ii11ii1ii + I1IiI / i1IIi / OoOoOO00 . Oo
def O0O00Oo ( ) :
 oooOo0OOOoo0 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oooOo0OOOoo0 == 0 :
  return
 elif oooOo0OOOoo0 == 1 :
  pass
 OOoOOO0O000 = iiIiI1i1 ( )
 print "Platform: " + str ( OOoOOO0O000 )
 if OOoOOO0O000 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIII111ii . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OOoOOO0O000 == 'linux' :
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
 elif OOoOOO0O000 == 'android' :
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
 elif OOoOOO0O000 == 'windows' :
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
  if 69 - 69: o0oO0
def iiIiI1i1 ( ) :
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
  if 40 - 40: O0oO + OoooooooOO % OOooOOo - iIii1I11I1II1 . OOOo0
  if 48 - 48: OOooOOo - OoOO / OoooooooOO
  if 100 - 100: OOOo0 / OOooOOo % OoOoOO00 % Oo % OoOO0ooOOoo0O
def O00oO000O0O ( url ) :
 i1111 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for I1i1i1iii , I1111i , iIIii in os . walk ( url ) :
  for file in iIIii :
   if file . endswith ( ".xml" ) :
    i1111 . update ( 0 , "Fixing" , file , 'Please Wait' )
    o00O0O = open ( ( os . path . join ( I1i1i1iii , file ) ) ) . read ( )
    ii1iii1i = o00O0O . replace ( i1iIIi1 , 'special://home/' )
    Iii1I1111ii = open ( ( os . path . join ( I1i1i1iii , file ) ) , mode = 'w' )
    Iii1I1111ii . write ( str ( ii1iii1i ) )
    Iii1I1111ii . close ( )
 O0O00Oo ( )
 if 72 - 72: OoOoOO00 + i1IIi + OOooOOo
def OOOIIiI1i1i ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 iiIii = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( oO00OOoO00 )
 for ooo0O , i1Ii in iiIii :
  O00Oo0 ( ooo0O , i1Ii , 222 , OOooO0OOoo + 'radio.png' )
  if 33 - 33: O0 * OOooOOo - O0oO % O0oO
def I11I ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iiIii = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , 'http://www.toonjet.com/' + i1Ii , 8051 , OOooO0OOoo + 'classictoons.png' )
def I11iIi1i1II11 ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( oO00OOoO00 )
 iiI = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( oO00OOoO00 )
 for url , i1I1i111Ii in iiIii :
  if 'ol.gif' in i1I1i111Ii :
   pass
  elif 'link_block_' in i1I1i111Ii :
   pass
  elif '.png' in i1I1i111Ii :
   pass
  else :
   OOO ( ( i1I1i111Ii ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , OOooO0OOoo + 'vod.png' )
 for url in iiI :
  OOO ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , OOooO0OOoo + 'documentary.png' )
def ooo ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oO00OOoO00 )
 for url in iiIii :
  O00Oo0 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , OOooO0OOoo + 'classictoons.png' )
  if 27 - 27: o0oO0 % OOOo0
def o0oooOO00 ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 iiIii = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O in iiIii :
  OOO ( ooo0O , i1Ii , 8046 , OOooO0OOoo + 'documentary.png' )
def iiIiii1IIIII ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( oO00OOoO00 )
 iiI = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , i1I1i111Ii , ooo0O in iiIii :
  O00Oo0 ( ( ooo0O ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , i1I1i111Ii )
 for url in iiI :
  OOO ( 'NEXT PAGE' , url , 8046 , OOooO0OOoo + 'documentary.png' )
  if 67 - 67: o00O0oo / IIII
def iiIiIIIiiI ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oO00OOoO00 )
 for url in iiIii :
  yt . PlayVideo ( url )
  if 12 - 12: O0 - OOooOOo
def oOoO00O0 ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 iiIii = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O in iiIii :
  OOO ( ooo0O , i1Ii , 8041 , OOooO0OOoo + 'documentary.png' )
def OO ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( oO00OOoO00 )
 iiI = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , ooo0O , i1I1i111Ii in iiIii :
  OOO ( ( ooo0O ) . replace ( '&#039;s' , '' ) , url , 8042 , i1I1i111Ii )
 for url in iiI :
  OOO ( 'NEXT PAGE' , url , 8041 , OOooO0OOoo + 'documentary.png' )
  if 7 - 7: O0 * i11iIiiIii * o00O0oo + o0oO0 % Ooo00oOo00o - o0oO0
  if 39 - 39: Oo * OoOO0ooOOoo0O % OoOO0ooOOoo0O - OoooooooOO + OOooOOo - o0000oOoOoO0o
def ii ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( oO00OOoO00 )
 iiI = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( oO00OOoO00 )
 for ooo0O , i1I1i111Ii , url , O0oOo00o in iiIii :
  O00Oo0 ( ( ooo0O ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , i1I1i111Ii )
 for url in iiI :
  o0ooooO0o0O ( ( url ) . replace ( '//' , 'http://' ) )
  if 24 - 24: O0 * OOooOOo
def o0ooooO0o0O ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( oO00OOoO00 )
 for url in iiIii :
  O00Oo0 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOooO0OOoo + 'documentary.png' )
  if 29 - 29: OOOo0 % OoOO0ooOOoo0O - OOOo0 / OoOO0ooOOoo0O . i1IIi
def i11III1111iIi ( ) :
 I1i111I = IiI111111IIII ( 'http://www.stream2watch.co/live-tv' )
 iiIii = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1i111I )
 for i1Ii , i1I1i111Ii , ooo0O , OooOo0oo0O0o00O in iiIii :
  OOO ( ( ooo0O + '[COLORgreen]' + OooOo0oo0O0o00O + '[/COLOR]' ) , i1Ii , 8086 , i1I1i111Ii )
  if 48 - 48: o0oO0 / O0oO . iIii1I11I1II1 * I1IiI * OoOO / i1IIi
def OOOOoOOo0O0 ( url ) :
 I1i111I = IiI111111IIII ( url )
 iiIii = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1i111I )
 for url , i1I1i111Ii , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , url , 8087 , i1I1i111Ii )
  if 92 - 92: ii11ii1ii + iIii1I11I1II1 / OoOoOO00
def OooO0OO ( url ) :
 I1i111I = Oo0ooOo0o ( url )
 iiIii = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for url , ooo0O in iiIii :
  o0OOo0o0O0O ( url , ooo0O )
  if 65 - 65: i11iIiiIii
def o0OOo0o0O0O ( url , name ) :
 I1i111I = Oo0ooOo0o ( url )
 iiIii = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1i111I )
 for url in iiIii :
  print url
  O00Oo0 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 85 - 85: o00O0oo % oO0o0ooO0 + o0000oOoOoO0o / OOooOOo . OoOO + OoOO0ooOOoo0O
def ooOoOo0 ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 iiIii = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for i1I1i111Ii , time , I11iiiiI1i , iI1i11 , OoOOoooOO0O , i1Ii in iiIii :
  OOO ( ( time + '[COLORgreen]' + OoOOoooOO0O + '[/COLOR]' + iI1i11 ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , i1Ii , 8061 , i1I1i111Ii )
def ooo00Ooo ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url in iiIii :
  O00Oo0 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , OOooO0OOoo + 'documentary.png' )
  if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * o0000oOoOoO0o % O0 + OoooooooOO
def I1i1i1 ( ) :
 I1i111I = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iiIii = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( I1i111I )
 for i1Ii , ooo0O in iiIii :
  OOO ( ( ooo0O ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + i1Ii , 8071 , OOooO0OOoo + 'streams.png' )
def OoO0O00O0oo0O ( url ) :
 I1i111I = IiI111111IIII ( url )
 iiIii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for ooo0O , url in iiIii :
  O00Oo0 ( ooo0O , ( url ) . strip ( ) , 222 , OOooO0OOoo + 'streams.png' )
  if 36 - 36: OoOO0ooOOoo0O + O0 - o00O0oo - O0 % o0000oOoOoO0o . OoOO
def oooiiI ( url ) :
 oOIIiIi = urllib2 . Request ( url )
 oOIIiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOooOoOOOoo = ''
 OOoo0O = ''
 try :
  OOoOooOoOOOoo = urllib2 . urlopen ( oOIIiIi )
  OOoo0O = OOoOooOoOOOoo . read ( )
  OOoOooOoOOOoo . close ( )
 except : pass
 if OOoo0O != '' :
  return OOoo0O
 else :
  OOoo0O = 'Failed'
  return OOoo0O
  if 25 - 25: OoooooooOO - OOOo0 . OOOo0 * OoOO
def o000oo ( ) :
 o00o0 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 II1I = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1I1I1Ii = II1I . lower ( )
 i1Ii = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 OOOOoO00o0O = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 I1I1I1IIi1III = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 II11IiiIII = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 o0OOOo = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 ii1iiIiIII1ii = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oO0o0oooO0oO = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + II1I
 IiIiII1 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( II1I ) . replace ( ' ' , '+' )
 if 21 - 21: O0 % IIII . OOOo0 / OoOoOO00 + IIII
 I1i111I = oooiiI ( i1Ii )
 OOOO0O00o = oooiiI ( OOOOoO00o0O )
 oooIIiIiI1I = oooiiI ( I1I1I1IIi1III )
 OooOoOo = oooiiI ( II11IiiIII )
 III1I1Iii1iiI = oooiiI ( o0OOOo )
 i1Iii11I1i = oooiiI ( oO0o0oooO0oO )
 Oo00o0OO0O00o = Oo0ooOo0o ( IiIiII1 )
 if 82 - 82: o0000oOoOoO0o + OoooooooOO - i1IIi . i1IIi
 if I1i111I != 'Failed' :
  iiIii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1i111I )
  for iIi1i , ooo0O in iiIii :
   if II1I in ooo0O . lower ( ) :
    O00Oo0 ( ( ooo0O + '[COLORgreen] source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1Ii + iIi1i ) , 222 , '' )
 if OOOO0O00o != 'Failed' :
  iiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOOO0O00o )
  for iIi1i , ooo0O in iiI :
   if II1I in ooo0O . lower ( ) :
    O00Oo0 ( ( ooo0O + '[COLORgreen] source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OOOOoO00o0O + iIi1i ) , 222 , '' )
 if oooIIiIiI1I != 'Failed' :
  I1i11111i1i11 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oooIIiIiI1I )
  for iIi1i , ooo0O in I1i11111i1i11 :
   if II1I in ooo0O . lower ( ) :
    O00Oo0 ( ( ooo0O + '[COLORgreen] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1I1I1IIi1III + iIi1i ) , 222 , '' )
 if OooOoOo != 'Failed' :
  OOoOOO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OooOoOo )
  for iIi1i , ooo0O in OOoOOO0 :
   if II1I in ooo0O . lower ( ) :
    O00Oo0 ( ( ooo0O + '[COLORgreen] source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II11IiiIII + iIi1i ) , 222 , '' )
 if III1I1Iii1iiI != 'Failed' :
  I1I1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( III1I1Iii1iiI )
  for iIi1i , i1I1i111Ii , ooo0O in I1I1i :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + '[COLORgreen] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iIi1i ) , 1006 , 'img' )
    if 1 - 1: o0000oOoOoO0o % OoOO0ooOOoo0O + O0 + i1IIi - Ooo00oOo00o
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if i1Iii11I1i != 'Failed' :
  iIIIII1ii1I = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1Iii11I1i )
  for iIi1i , i1I1i111Ii , ooo0O in iIIIII1ii1I :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( '[COLORgreen]' + ooo0O + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + i1Ii , 7067 , i1I1i111Ii )
    if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - OoOoOO00 * OoOO0ooOOoo0O
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if Oo00o0OO0O00o != 'Failed' :
  iiIi1iI1iIii = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( Oo00o0OO0O00o )
  for i1Ii , i1I1i111Ii , ooo0O in iiIi1iI1iIii :
   O00Oo0 ( ooo0O + ' - Source 7' , i1Ii , 222 , i1I1i111Ii )
 o00OooO0oo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 89 - 89: o00O0oo
 if 76 - 76: o0oO0
 for IIIiI11ii1I in o00OooO0oo :
  IiiiI = o00o0 + IIIiI11ii1I
  O00OoOO0oo0 = oooiiI ( IiiiI )
  if III1I1Iii1iiI != 'Failed' :
   oOO = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( O00OoOO0oo0 )
   for iIi1i , ooo0O in oOO :
    if II1I in ooo0O . lower ( ) :
     O00Oo0 ( ( ooo0O + '[COLORgreen] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o00o0 + IIIiI11ii1I + iIi1i ) , 222 , '' )
     if 53 - 53: O0oO * IIII . Oo - o00O0oo % o00O0oo * i11iIiiIii
     o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
     if 7 - 7: O0 . o00O0oo
     if 51 - 51: Ooo00oOo00o - O0 % OoOO - OoOoOO00
def I1II ( ) :
 if 64 - 64: O0 % o0000oOoOoO0o % O0 * Ooo00oOo00o . OoOO + OOOo0
 II1I = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1I1I1Ii = II1I . lower ( )
 i1Ii = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 OOOOoO00o0O = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 I1I1I1IIi1III = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 II11IiiIII = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 o0OOOo = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( II1I ) . replace ( ' ' , '+' )
 ii1iiIiIII1ii = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 IiIiII1 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( II1I ) . replace ( ' ' , '+' )
 if 75 - 75: o0000oOoOoO0o . OoooooooOO % OOooOOo * o0000oOoOoO0o % OoooooooOO
 I1i111I = oooiiI ( i1Ii )
 OOOO0O00o = oooiiI ( OOOOoO00o0O )
 oooIIiIiI1I = oooiiI ( I1I1I1IIi1III )
 OooOoOo = oooiiI ( II11IiiIII )
 III1I1Iii1iiI = cloudflare . source ( o0OOOo )
 O00OoOO0oo0 = oooiiI ( ii1iiIiIII1ii )
 Oo00o0OO0O00o = Oo0ooOo0o ( IiIiII1 )
 if I1i111I != 'Failed' :
  iiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1i111I )
  for ooo0O in iiIii :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1Ii + ooo0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 13 - 13: IIII / i11iIiiIii % OoOoOO00 % o0000oOoOoO0o . ii11ii1ii
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OOOO0O00o != 'Failed' :
  iiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOOO0O00o )
  for ooo0O in iiI :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOOOoO00o0O + ooo0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 8 - 8: I1IiI + Oo - OoOoOO00
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if oooIIiIiI1I != 'Failed' :
  I1i11111i1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooIIiIiI1I )
  for ooo0O in iiI :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1I1I1IIi1III + ooo0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 11 - 11: i1IIi % i11iIiiIii - i1IIi * I1IiI
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OooOoOo != 'Failed' :
  OOoOOO0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OooOoOo )
  for ooo0O in iiI :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( II11IiiIII + ooo0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 39 - 39: O0oO
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if III1I1Iii1iiI != 'Failed' :
  I1I1i = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( III1I1Iii1iiI )
  for i1Ii , i1I1i111Ii , ooo0O in I1I1i :
   if II1I in ooo0O . lower ( ) :
    OOO ( ooo0O + ' - Source - Dizi' , i1Ii , 8062 , i1I1i111Ii )
    if 86 - 86: o0000oOoOoO0o * OOOo0 + o0000oOoOoO0o + OoOoOO00
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if O00OoOO0oo0 != 'Failed' :
  oOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00OoOO0oo0 )
  for i1Ii , i1I1i111Ii , ooo0O in oOO :
   if II1I in ooo0O . lower ( ) :
    O00Oo0 ( ( ooo0O + '[COLORgreen] source Scooby[/COLOR]' ) , i1Ii , 222 , 'img' )
    if 8 - 8: O0oO - oO0o0ooO0 / o0oO0
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if Oo00o0OO0O00o != 'Failed' :
  iiIi1iI1iIii = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( Oo00o0OO0O00o )
  for i1Ii , i1I1i111Ii , ooo0O in iiIi1iI1iIii :
   O00Oo0 ( ooo0O + ' - Source 7' , i1Ii , 222 , i1I1i111Ii )
def oo0oOoo ( ) :
 if 57 - 57: I1IiI - ii11ii1ii
 II1I = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1I1I1Ii = II1I . lower ( )
 i1Ii = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 I1i111I = Oo0ooOo0o ( i1Ii )
 iiIii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1i111I )
 for ooo0O , i1I1i111Ii , I11i in iiIii :
  iI11 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1I1i111Ii ) . replace ( '\\' , '' )
  if II1I in ooo0O . lower ( ) :
   OOO ( ooo0O , '' , 7022 , iI11 )
   if 96 - 96: OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: OOooOOo . I1IiI / o0oO0 . O0 % O0oO
 if 90 - 90: Oo % O0 * iIii1I11I1II1 . oO0o0ooO0
def I1iii11 ( url ) :
 ooo0OiII1iii = cloudflare . source ( url )
 iiIii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( ooo0OiII1iii )
 for url , i11i1iiiII , ooOO0oO0oo00o , ooo0O in iiIii :
  OOO ( ( i11i1iiiII ) . replace ( 'Sezon' , ' Season ' ) + ( ooOO0oO0oo00o ) . replace ( 'Bölüm' , ' Episode ' ) + ooo0O , url , 8063 , '' )
  if 83 - 83: OoOO - OoOoOO00 - oO0o0ooO0
  if 3 - 3: O0oO
  if 45 - 45: O0oO
  if 83 - 83: I1IiI . OoooooooOO
def Oo0ooo ( url ) :
 ooo0OiII1iii = cloudflare . source ( url )
 iiIii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( ooo0OiII1iii )
 for url , ooo0O in iiIii :
  O00Oo0 ( ooo0O , url , 222 , '' )
  if 28 - 28: OoOO . OoOoOO00 / ii11ii1ii + OoOoOO00 . OoooooooOO . IIII
  if 53 - 53: o00O0oo % o00O0oo * OOooOOo + I1IiI
  if 92 - 92: OoooooooOO + i1IIi / o00O0oo * O0
  if 100 - 100: o0oO0 % iIii1I11I1II1 * OoOoOO00 - oO0o0ooO0
def oo00O00oO000o ( ) :
 if 71 - 71: ii11ii1ii - o0oO0 / I1IiI * I1IiI / i1IIi . i1IIi
 ooo0OiII1iii = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( ooo0OiII1iii )
 for i1Ii , i1I1i111Ii , ooo0O , ooOO0oO0oo00o in iiIii :
  OOO ( ooo0O + '  -  ' + ( ooOO0oO0oo00o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1Ii , 8063 , i1I1i111Ii )
  if 53 - 53: O0oO
def i11iiI1111 ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iiIii = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O , i1I1i111Ii in iiIii :
  O00Oo0 ( '[COLORgreen]' + ooo0O + '[/COLOR]' , i1Ii , 8002 , i1I1i111Ii )
def oOoooo000Oo00 ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for i1I1i111Ii , time , url , ooo0O , O0oOo00o in iiIii :
  O0O00o0OOO0 ( '%s %s' % ( '[COLORgreen]' + ooo0O + '[/COLOR]' , time ) , url , 1015 , i1I1i111Ii , O0oOo00o )
  if 93 - 93: ii11ii1ii / OOOo0 / iIii1I11I1II1 % O0oO % O0oO
def IiI11iI1i1i1i ( ) :
 if 89 - 89: o0000oOoOoO0o
 OOO ( 'Coronation Street' , '' , 8001 , '' )
 OOO ( 'Eastenders' , '' , 8002 , '' )
 OOO ( 'Emmerdale' , '' , 8003 , '' )
 OOO ( 'Hollyoaks' , '' , 8004 , '' )
 OOO ( 'Im a Celebrity' , '' , 8005 , '' )
 if 64 - 64: OoOoOO00 + O0 / iIii1I11I1II1 / Oo . o0oO0 % IIII
 if 50 - 50: iIii1I11I1II1 - IIII + OoOO0ooOOoo0O
 if 69 - 69: O0
 if 85 - 85: o0oO0 / O0
def iI1iIIIi1i ( ) :
 I1i111I = Oo0ooOo0o ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I1i111I )
 for i1Ii , ooo0O in iiIii :
  if 'Holly' in ooo0O :
   i1I1i111Ii = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in i1Ii :
    O00Oo0 ( ( ooo0O ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Ii . replace ( '\\/' , '/' ) , 8006 , i1I1i111Ii )
   else :
    pass
    if 89 - 89: iIii1I11I1II1
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 21 - 21: o0000oOoOoO0o % o0000oOoOoO0o
def iiI1iiIIiii ( ) :
 I1i111I = Oo0ooOo0o ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I1i111I )
 for i1Ii , ooo0O in iiIii :
  if 'East' in ooo0O :
   i1I1i111Ii = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in i1Ii :
    O00Oo0 ( ( ooo0O ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Ii . replace ( '\\/' , '/' ) , 8006 , i1I1i111Ii )
   else :
    pass
    if 30 - 30: oO0o0ooO0
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: OoOO0ooOOoo0O + OOooOOo . OoooooooOO
def ooOooo0 ( ) :
 I1i111I = Oo0ooOo0o ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I1i111I )
 for i1Ii , ooo0O in iiIii :
  if 'Emmer' in ooo0O :
   i1I1i111Ii = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in i1Ii :
    O00Oo0 ( ( ooo0O ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Ii . replace ( '\\/' , '/' ) , 8006 , i1I1i111Ii )
   else :
    pass
    if 67 - 67: OOOo0
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: ii11ii1ii - oO0o0ooO0 * OOooOOo + I1IiI * I1IiI * O0
def O000Oo0o ( ) :
 I1i111I = Oo0ooOo0o ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I1i111I )
 for i1Ii , ooo0O in iiIii :
  if 'Coro' in ooo0O :
   i1I1i111Ii = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in i1Ii :
    O00Oo0 ( ( ooo0O ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Ii . replace ( '\\/' , '/' ) , 8006 , i1I1i111Ii )
   else :
    pass
    if 99 - 99: iIii1I11I1II1 % o0oO0 + o0oO0 + oO0o0ooO0 - O0oO / O0oO
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: OOOo0 + I1IiI / IIII
def OOOoO000 ( ) :
 I1i111I = Oo0ooOo0o ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( I1i111I )
 for i1Ii , ooo0O in iiIii :
  if 'Celeb' in ooo0O :
   i1I1i111Ii = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in i1Ii :
    O00Oo0 ( ( ooo0O ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Ii . replace ( '\\/' , '/' ) , 8006 , i1I1i111Ii )
   else :
    pass
    if 57 - 57: OoOoOO00
def oOOOoo ( name , url ) :
 Ii1ii111i1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Ii1ii111i1 :
  i1i1i1I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oO00OOoO00 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( oO00OOoO00 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oO00OOoO00 = open_url ( url )
  oOoo000 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( oO00OOoO00 ) [ - 1 ]
  i1i1i1I = oOoo000 . replace ( '\\/' , '/' )
 OooOo00o = xbmcgui . ListItem ( name , '' , '' )
 OooOo00o . setPath ( i1i1i1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OooOo00o )
 if 20 - 20: i1IIi * O0oO + OoOoOO00 % OOooOOo % OoOO
 if 13 - 13: Oo
def oOOo000oOoO0 ( ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIii = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O in iiIii :
  if 'Movies' in ooo0O :
   OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , 'http://www.snagfilms.com' + i1Ii , 7061 , OOooO0OOoo + 'popcorn.png' )
def OoOo00o0OO ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oO00OOoO00 )
 iiI = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , i1I1i111Ii , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , 'http://www.snagfilms.com' + url , 7067 , i1I1i111Ii )
 for url in iiI :
  OOO ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOooO0OOoo + 'popcorn.png' )
  if 1 - 1: OOOo0 % o0oO0
  if 65 - 65: OOOo0 + I1IiI / OoOO0ooOOoo0O
def oOOoOooo0O0o ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , i1I1i111Ii , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , 'http://www.snagfilms.com' + url , 7062 , i1I1i111Ii )
  if 72 - 72: iIii1I11I1II1 / IIII % oO0o0ooO0 % OoOO0ooOOoo0O - o0000oOoOoO0o % OoOO0ooOOoo0O
  if 100 - 100: Oo + i11iIiiIii
def O0oOOO000oooo0 ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , i1I1i111Ii , ooo0O in iiIii :
  OOO ( ( '[COLORgreen]' + ooo0O + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , i1I1i111Ii )
  if 77 - 77: OOOo0 % O0
def I1iii ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url in iiIii :
  oO0o0O0Ooo0o ( 'http://www.snagfilms.com' + url )
  if 21 - 21: O0oO - OOOo0 + o0000oOoOoO0o
def oO0o0O0Ooo0o ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  O00Oo0 ( '[COLORgreen]' + ooo0O + '[/COLOR]' , url , 222 , OOooO0OOoo + 'popcorn' )
  if 78 - 78: OoooooooOO - i11iIiiIii - OoOoOO00
  if 77 - 77: I1IiI % o00O0oo
  if 9 - 9: Ooo00oOo00o - Oo * OoooooooOO . Oo
  if 2 - 2: OoooooooOO % OoOO0ooOOoo0O
def oOoOOo0oo0 ( ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iiIii = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O , i1I1i111Ii in iiIii :
  O00Oo0 ( '[COLORgreen]' + ooo0O + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( i1Ii ) ) , 222 , i1I1i111Ii )
  if 60 - 60: o0oO0 * O0oO + Oo
def IIi1i1IiIIi1i ( ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 iiIii = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( oO00OOoO00 )
 for ooo0O , i1Ii in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + i1Ii , 7051 , OOooO0OOoo + 'vod.png' )
  if 54 - 54: o0oO0
def O0iIi1IiII ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , OOooO0OOoo + 'vod.png' )
  if 27 - 27: oO0o0ooO0 . o0000oOoOoO0o . iIii1I11I1II1 . iIii1I11I1II1
def iIi1ii1ii ( url ) :
 oO00OOoO00 = Oo0ooOo0o
 iiIii = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , i1I1i111Ii , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , url , 222 , i1I1i111Ii )
  if 68 - 68: OoOO0ooOOoo0O * O0 . o0000oOoOoO0o - OoOoOO00 . o0oO0 / OoOoOO00
  if 47 - 47: OoooooooOO
  if 4 - 4: OOOo0 % o0000oOoOoO0o
  if 10 - 10: IIII . OoooooooOO - Ooo00oOo00o + IIII - O0
  if 82 - 82: o0oO0 + OoOoOO00
def II1i1i1iII1 ( ) :
 if 68 - 68: Oo + i11iIiiIii
 OOO ( 'All Channels' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Entertainment' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Movies' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Music' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'News' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Sports' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Documentary' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Kids' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Food' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Religious' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'USA Channels' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 OOO ( 'Other' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + OOOo0 / OoOO0ooOOoo0O % o00O0oo
 if 58 - 58: OoOO0ooOOoo0O * OOooOOo + O0 % OoOO0ooOOoo0O
def iI1I1iIi11 ( Cat_Name ) :
 if 87 - 87: I1IiI
 Ii = False
 oO0O = '0'
 if Cat_Name == 'All Channels' : Ii = True
 if Cat_Name == 'Entertainment' : oO0O = '1'
 if Cat_Name == 'Movies' : oO0O = '2'
 if Cat_Name == 'Music' : oO0O = '3'
 if Cat_Name == 'News' : oO0O = '4'
 if Cat_Name == 'Sports' : oO0O = '5'
 if Cat_Name == 'Documentary' : oO0O = '6'
 if Cat_Name == 'Kids' : oO0O = '7'
 if Cat_Name == 'Food' : oO0O = '8'
 if Cat_Name == 'Religious' : oO0O = '9'
 if Cat_Name == 'USA Channels' : oO0O = '10'
 if Cat_Name == 'Other' : oO0O = '11'
 if 86 - 86: I1IiI . iIii1I11I1II1 - Ooo00oOo00o
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oO00OOoO00 )
 print 'Len Match: >>>' + str ( len ( iiIii ) )
 for ooo0O , i1I1i111Ii , I11i in iiIii :
  iI11 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1I1i111Ii ) . replace ( '\\' , '' )
  if I11i == oO0O :
   OOO ( ooo0O , '' , 7022 , iI11 )
  elif Ii == True :
   OOO ( ooo0O , '' , 7022 , iI11 )
  else : pass
  if 56 - 56: O0
  xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 61 - 61: OOooOOo / OoOO0ooOOoo0O / Oo * O0
def iIII1i1i ( Search_Name ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oO00OOoO00 )
 iiIii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oO00OOoO00 )
 for i1I1i111Ii , i1Ii , OOOOoO00o0O , I1I1I1IIi1III in iiIii :
  iI11 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1I1i111Ii ) . replace ( '\\' , '' )
  O00Oo0 ( Search_Name + ': Link 1' , ( i1Ii ) . replace ( '\\' , '' ) , 222 , iI11 )
  O00Oo0 ( Search_Name + ': Link 2' , ( OOOOoO00o0O ) . replace ( '\\' , '' ) , 222 , iI11 )
  O00Oo0 ( Search_Name + ': Link 3' , ( I1I1I1IIi1III ) . replace ( '\\' , '' ) , 222 , iI11 )
  if 35 - 35: OoOoOO00 * o0000oOoOoO0o - OoooooooOO . o0000oOoOoO0o . o0000oOoOoO0o
def I1IIOO0 ( ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIii = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oO00OOoO00 )
 for ooo0O , i1Ii in iiIii :
  O00Oo0 ( ooo0O , ( i1Ii ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOooO0OOoo + 'english.png' )
def OOO0oOOo00O ( ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIii = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oO00OOoO00 )
 for ooo0O , i1Ii in iiIii :
  O00Oo0 ( ooo0O , ( i1Ii ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'xxx.png' )
def OO0oIII111i11IiI ( ) :
 oO00OOoO00 = Oo0ooOo0o ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iiIii = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oO00OOoO00 )
 for ooo0O , i1Ii in iiIii :
  O00Oo0 ( ooo0O , ( i1Ii ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'vod(1).png' )
  if 71 - 71: o0000oOoOoO0o / o0000oOoOoO0o * OoOO * OoOO / OoOoOO00
def II1I1iiIII1I1 ( url ) :
 url
 o0Ooo0o0ooo0 = xbmcgui . ListItem ( ooo0O , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0Ooo0o0ooo0 )
 return
 if 70 - 70: i11iIiiIii % oO0o0ooO0
 if 11 - 11: IIII % ii11ii1ii % o00O0oo / OoOoOO00 % O0oO - Oo
def OOooO ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  OOO ( ooo0O , url , 9031 , OOooO0OOoo + 'icon.png' )
def O00O0OO00oo ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  OOO ( ooo0O , url , 9032 , OOooO0OOoo + 'icon.png' )
def oOOO ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( oO00OOoO00 )
 for ooo0O , url in iiIii :
  if '://' in ooo0O :
   pass
   O00Oo0 ( ( ooo0O ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOooO0OOoo + 'icon.png' )
def ooo0oooo0 ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oO00OOoO00 )
 for ooo0O , url in iiIii :
  O00Oo0 ( ooo0O , url , 222 , OOooO0OOoo + 'icon.png' )
  if 62 - 62: ii11ii1ii + o00O0oo + i1IIi / OoooooooOO
  if 7 - 7: OOooOOo + i1IIi . OOOo0 / Oo
  if 22 - 22: o0oO0 - o0oO0 % OoOO0ooOOoo0O . O0oO + OoOO
def Oo00OOo00O ( ) :
 oO00OOoO00 = Oo0ooOo0o ( 'http://tvshows.cnfstudio.com/' )
 iiIii = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O in iiIii :
  OOO ( ooo0O , 'http://tvshows.cnfstudio.com/genre/' + i1Ii , 7010 , OOooO0OOoo + 'icon.png' )
  print '>>>>>>>>>>' + i1Ii
  if 81 - 81: IIII . OOooOOo / O0oO
def Iii111Ii ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oO00OOoO00 )
 O0O00oOooo0OO = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( oO00OOoO00 )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oO00OOoO00 )
 for i1I1i111Ii , url , ooo0O in iiIii :
  OOO ( ( ooo0O ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , i1I1i111Ii )
 O0O00oOooo0OO = O0O00oOooo0OO
 for url in O0O00oOooo0OO :
  OOO ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  OOO ( 'Next' , url , 7010 , '' )
  if 23 - 23: OoOO + Ooo00oOo00o
def III1I1i1 ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , ooOO0oO0oo00o , ooo0O in iiIii :
  O00Oo0 ( ( 'Season' ) + ooOO0oO0oo00o + ( '  ' ) + ooo0O , url , 7004 , OOooO0OOoo + 'icon.png' )
  if 11 - 11: O0 / Ooo00oOo00o % OoOO0ooOOoo0O + OOooOOo + iIii1I11I1II1
def I1i1111I ( url ) :
 if 95 - 95: iIii1I11I1II1 - ii11ii1ii . O0oO - OOOo0
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  OOO ( ooo0O , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOooO0OOoo + 'icon.png' )
  if 75 - 75: Ooo00oOo00o + OOooOOo - i1IIi . OoooooooOO * o00O0oo / IIII
def OOOooo0OooOoO ( name , url , img ) :
 I1i111I = Oo0ooOo0o ( url )
 oOoOOOo = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1i111I )
 ii1I = len ( oOoOOOo )
 if 85 - 85: o0000oOoOoO0o
 if 88 - 88: OOOo0 + OoooooooOO - OoOO
 if ii1I == 1 :
  for OOo in oOoOOOo :
   OOo = OOo . replace ( 'player' , 'watch' )
   oooOO0OO0O = OOo + '&fv=&sou='
   o00o = Oo0ooOo0o ( oooOO0OO0O )
   III11I = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o00o )
   for Ii1I11I in III11I :
    iiIii1I = False
    Resolve ( Ii1I11I )
    if 47 - 47: o0oO0 . o0000oOoOoO0o / OOooOOo
 elif ii1I > 1 :
  if 83 - 83: OOooOOo / OoOO0ooOOoo0O / OoOO0ooOOoo0O + OOooOOo * O0oO + OOooOOo
  for OOo in oOoOOOo :
   IIIIiii = Oo0ooOo0o ( OOo )
   oO0o = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IIIIiii )
   IIIii1iiIi = oO0o
   IIIii1iiIi = ( str ( IIIii1iiIi ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIIii1iiIi
   O00Oo0 ( 'DOUBLE LINK' , IIIii1iiIi , 424 , '' )
   if 63 - 63: ii11ii1ii
   for url in oO0o :
    OOO ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OOOOoO00o0O = Google . resolve ( url )
    except :
     pass
    try :
     i1II = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OOOOoO00o0O ) )
     for IiiI11i1I , OOo0 in i1II :
      if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
      HD_URLS . append ( IiiI11i1I )
      SD_URLS . append ( OOo0 )
    except :
     pass
 else :
  pass
  if 86 - 86: iIii1I11I1II1 + I1IiI . i11iIiiIii - o00O0oo
def ooO000O ( ) :
 if 53 - 53: OOooOOo . oO0o0ooO0 / o00O0oo
 if 39 - 39: o00O0oo % O0 % I1IiI . i1IIi
 OOO ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOooO0OOoo + 'Movies.png' )
 if 86 - 86: Ooo00oOo00o * OoooooooOO
 OOO ( 'Search Movies' , '' , 7017 , OOooO0OOoo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 71 - 71: iIii1I11I1II1 - OoOO0ooOOoo0O . OOOo0 % OoooooooOO + OoOO0ooOOoo0O
 if 26 - 26: Oo + OoOO0ooOOoo0O / Ooo00oOo00o % I1IiI % ii11ii1ii + OoOoOO00
def i11I1I1iiI ( ) :
 oO00OOoO00 = Oo0ooOo0o ( 'http://cnfstudio.com/' )
 iiIii = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O in iiIii :
  OOO ( ooo0O , 'http://cnfstudio.com/genre/' + i1Ii , 7003 , OOooO0OOoo + 'icon.png' )
  if 34 - 34: o0000oOoOoO0o % o0oO0 . O0 . iIii1I11I1II1
i1iiIII111ii = xbmcgui . Dialog ( )
if 93 - 93: i1IIi . i11iIiiIii . Oo
if 99 - 99: o0000oOoOoO0o - O0oO - OoOO % Ooo00oOo00o
def IiiIIiiiiii ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oO00OOoO00 )
 O0O00oOooo0OO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oO00OOoO00 )
 for i1I1i111Ii , url , ooo0O in iiIii :
  O00Oo0 ( ( ooo0O ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , i1I1i111Ii )
 O0O00oOooo0OO = O0O00oOooo0OO
 for url in O0O00oOooo0OO :
  OOO ( 'Next Page' , url , 7003 , '' )
  if 100 - 100: Oo + OOooOOo - O0 % OoOoOO00 . oO0o0ooO0
def ooOo0OoOooo00 ( url ) :
 if 96 - 96: ii11ii1ii % o0oO0 % o00O0oo - o0oO0 % I1IiI + ii11ii1ii
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url in iiIii :
  OOoo0O = url + '&fv=&sou='
  OOoo0O = OOoo0O . replace ( 'player' , 'watch' )
  iI = Oo0O ( OOoo0O )
  Ii11 = Oo0O ( url )
  if 8 - 8: Oo + OoOoOO00 * OoOO0ooOOoo0O * I1IiI * o0000oOoOoO0o / IIII
  if 21 - 21: OoOO / OoooooooOO
def Oo0O ( url ) :
 if 11 - 11: OoOO0ooOOoo0O % o00O0oo - i11iIiiIii - OoOO + o0oO0 + IIII
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url in iiIii :
  o0ooOo0OOOO0o ( url )
  if 98 - 98: OoOO0ooOOoo0O + i1IIi . OOOo0 - OoOoOO00 - OOooOOo
  if 24 - 24: Oo - i1IIi + o0000oOoOoO0o
def IiiIi ( ) :
 O0O00o0OOO0 ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 10 - 10: Ooo00oOo00o / Oo
def I1i ( url ) :
 iiIii = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for II11iIII1i1I , ooo0O , url in iiIii :
  O00Oo0 ( ooo0O , url , 222 , OOooO0OOoo + 'streams.png' )
  if 63 - 63: Oo + O0oO - OoOoOO00
  if 2 - 2: IIII
def oOo0O0O0 ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00OOoO00 )
 for i1Ii , ii111iI1iIi1 , ooo0O in iiIii :
  OOO ( ooo0O , i1Ii , 1007 , ii111iI1iIi1 )
def oOoo0 ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00OOoO00 )
 for url , ii111iI1iIi1 , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , url , 1006 , ii111iI1iIi1 )
  if 34 - 34: oO0o0ooO0 - OoooooooOO . OOOo0 / OoOoOO00
  if 27 - 27: Ooo00oOo00o / Oo * o0oO0 - Ooo00oOo00o
def iI11iiii1I ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00OOoO00 )
 for url , ii111iI1iIi1 , ooo0O in iiIii :
  if '.php' in url :
   OOO ( ooo0O , url , 1016 , ii111iI1iIi1 )
  else :
   O00Oo0 ( ooo0O , url , 222 , ii111iI1iIi1 )
   if 3 - 3: O0 % OoooooooOO / OoOO0ooOOoo0O
def ooOo ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00OOoO00 )
 for i1Ii , ii111iI1iIi1 , ooo0O in iiIii :
  OOO ( ooo0O , i1Ii , 1007 , ii111iI1iIi1 )
def o0oO0OoO0 ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00OOoO00 )
 for url , ii111iI1iIi1 , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , url , 1006 , ii111iI1iIi1 )
  if 70 - 70: OoOO - OoOO
def OoOO0OOoo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 IIIi11IiIiii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 IIIi11IiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIIi11IiIiii )
 if 38 - 38: Oo - o0000oOoOoO0o . Oo
 if 38 - 38: i1IIi + o00O0oo
def Oo00O0ooOO ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00OOoO00 )
 for url , i1I1i111Ii , ooo0O in iiIii :
  OOO ( '[COLORgreen]' + ooo0O + '[/COLOR]' , url , 1006 , i1I1i111Ii )
def IiiI ( url ) :
 oO00OOoO00 = IiI111111IIII ( url )
 i11ii = url
 iiIii = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  if '.mp3' in ooo0O :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O00Oo0 ( ( ooo0O ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOooO0OOoo + 'music.png' )
  else :
   OOO ( ( ooo0O ) . replace ( '/' , '' ) , i11ii + url , 1011 , OOooO0OOoo + 'music.png' )
def i11I1 ( ) :
 oO00OOoO00 = IiI111111IIII ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iiIii = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for i1Ii , i1I1i111Ii , ooo0O in iiIii :
  OOO ( ooo0O , ( 'http://www.cyn.net/music/' + i1Ii ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + i1I1i111Ii ) . replace ( ' ' , '%20' ) )
def Ii1iIi111i1i1 ( url , img ) :
 oO00OOoO00 = IiI111111IIII ( url )
 OOOOoO00o0O = url
 img = img
 iiIii = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  O00Oo0 ( ( ooo0O ) . replace ( '.mp3' , '' ) , ( OOOOoO00o0O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 45 - 45: I1IiI . OOooOOo % I1IiI * OOOo0 % OOOo0
  if 63 - 63: O0oO
def oo00ooOoo ( ) :
 o00o0 = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 II1I = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1I1I1Ii = II1I . lower ( )
 i1Ii = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OOOOoO00o0O = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1I1I1IIi1III = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 28 - 28: o00O0oo
 I1i111I = oooiiI ( i1Ii )
 OOOO0O00o = oooiiI ( OOOOoO00o0O )
 oooIIiIiI1I = oooiiI ( I1I1I1IIi1III )
 if 1 - 1: o00O0oo
 if I1i111I != 'Failed' :
  iiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1i111I )
  for ooo0O in iiIii :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1Ii + ooo0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 48 - 48: O0 + O0 . O0oO - o0oO0
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OOOO0O00o != 'Failed' :
  iiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1i111I )
  for ooo0O in iiI :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOOOoO00o0O + ooo0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 63 - 63: OoOO
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if oooIIiIiI1I != 'Failed' :
  I1i11111i1i11 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oooIIiIiI1I )
  for ooo0O in I1i11111i1i11 :
   if II1I in ooo0O . lower ( ) :
    OOO ( ( ooo0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1I1I1IIi1III + ooo0O ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 71 - 71: i1IIi . o00O0oo * oO0o0ooO0 % OoooooooOO + OoOO0ooOOoo0O
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
    if 36 - 36: IIII
    if 49 - 49: OoOO0ooOOoo0O / OoooooooOO / OOOo0
    if 74 - 74: O0oO % ii11ii1ii
    if 7 - 7: OoOoOO00
    if 27 - 27: OoOO . OoooooooOO + i11iIiiIii
    if 86 - 86: o0000oOoOoO0o / OOooOOo - OOooOOo + ii11ii1ii + OoOO
def IIi ( ) :
 oO00OOoO00 = Oo0ooOo0o ( 'http://www.animetoon.org/cartoon' )
 iiIii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oO00OOoO00 )
 for i1Ii , ooo0O in iiIii :
  OOO ( ooo0O , i1Ii , 1002 , OOooO0OOoo + 'anime.png' )
  if 84 - 84: IIII
  if 21 - 21: ii11ii1ii . OoOO0ooOOoo0O * OOooOOo
  if 71 - 71: OoOO + O0
def o0o0oO0 ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiI = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oO00OOoO00 )
 for i1I1i111Ii in iiI :
  i1iiii11i1 = i1I1i111Ii
 I1i11111i1i11 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( oO00OOoO00 )
 for url in I1i11111i1i11 :
  OOO ( 'NEXT PAGE' , url , 1002 , i1iiii11i1 )
 iiIii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oO00OOoO00 )
 for url , ooo0O in iiIii :
  OOO ( ooo0O , url , 1003 , i1iiii11i1 )
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOo0OoO ( url , IMAGE ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oO00OOoO00 )
 for ooo0O , url in iiIii :
  print ooo0O + '     ' + url
  if 'easy' in url :
   i1iiIIi1I ( url )
  elif 'playpanda' in url :
   i1iiIIi1I ( url )
   if 36 - 36: OOOo0 * Oo
  xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1iiIIi1I ( url ) :
 oO00OOoO00 = Oo0ooOo0o ( url )
 iiIii = re . compile ( "url: '(.+?)'," ) . findall ( oO00OOoO00 )
 for url in iiIii :
  O00Oo0 ( 'STREAM' , url , 222 , OOooO0OOoo + 'anime.png' )
  if 77 - 77: OoOO % i1IIi - o00O0oo
  if 93 - 93: Ooo00oOo00o * Oo
def OO0ooo0o0 ( url ) :
 oOIIiIi = urllib2 . Request ( url )
 oOIIiIi . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oOIIiIi . add_header ( 'referer' , url )
 OOoOooOoOOOoo = urllib2 . urlopen ( oOIIiIi )
 OOoo0O = OOoOooOoOOOoo . read ( )
 OOoOooOoOOOoo . close ( )
 return OOoo0O
 if 69 - 69: ii11ii1ii - O0oO
def IiI111111IIII ( url ) :
 oOIIiIi = urllib2 . Request ( url )
 oOIIiIi . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOoOooOoOOOoo = urllib2 . urlopen ( oOIIiIi )
 OOoo0O = OOoOooOoOOOoo . read ( )
 OOoOooOoOOOoo . close ( )
 return OOoo0O
 if 16 - 16: Oo
def ii1iI111 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0O0Oo0Ooo0 = ( '%s%s' % ( I11iII , url ) )
 OOoo0O = IiI111111IIII ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoo0O )
 for url , ii111iI1iIi1 , ooo0O in iiIii :
  O00Oo0 ( '%s' % ( ooo0O ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ii111iI1iIi1 )
  if 2 - 2: OOOo0 + OOooOOo . OOooOOo . O0 / o0000oOoOoO0o
def o0ooOo0OOOO0o ( url ) :
 iIiiIiiIi = xbmc . Player ( i1iiIIIi ( ) )
 import urlresolver
 try : iIiiIiiIi . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( ooo0O ) )
 iIiiIiiIi = xbmc . Player ( i1iiIIIi ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIII111ii = xbmcgui . Dialog ( )
  if i1iiIII111ii . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIII111ii . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iIiiIiiIi . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 62 - 62: O0 / OOOo0 % O0 * Ooo00oOo00o % OOOo0
  if 33 - 33: OOOo0 . OoOO * Ooo00oOo00o * iIii1I11I1II1
def i1iiIIIi ( ) :
 try :
  II11 = getSet ( "core-player" )
  if ( II11 == 'DVDPLAYER' ) : i111i1iIiiIiI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( II11 == 'MPLAYER' ) : i111i1iIiiIiI = xbmc . PLAYER_CORE_MPLAYER
  elif ( II11 == 'PAPLAYER' ) : i111i1iIiiIiI = xbmc . PLAYER_CORE_PAPLAYER
  else : i111i1iIiiIiI = xbmc . PLAYER_CORE_AUTO
 except : i111i1iIiiIiI = xbmc . PLAYER_CORE_AUTO
 return i111i1iIiiIiI
 return True
 if 26 - 26: iIii1I11I1II1 % i11iIiiIii % ii11ii1ii
def OOO ( name , url , mode , iconimage ) :
 oo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 III1i1IiI1i = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 III1i1IiI1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0O , listitem = OooOo00o , isFolder = True )
 return III1i1IiI1i
 if 32 - 32: OoooooooOO - I1IiI - i11iIiiIii * OOooOOo / Oo + OoooooooOO
def O00Oo0 ( name , url , mode , iconimage ) :
 oo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 III1i1IiI1i = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 III1i1IiI1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0O , listitem = OooOo00o , isFolder = False )
 return III1i1IiI1i
 if 35 - 35: i1IIi - OOooOOo * oO0o0ooO0
 if 63 - 63: oO0o0ooO0 * ii11ii1ii . OoooooooOO / OoOO0ooOOoo0O * Oo . o0oO0
 if 62 - 62: i1IIi / o0oO0 . OOOo0 * OOooOOo
 if 21 - 21: OOooOOo
 if 81 - 81: o0000oOoOoO0o / iIii1I11I1II1 - o0oO0 * O0oO . OOOo0 * ii11ii1ii
 if 95 - 95: OOOo0
 if 88 - 88: IIII % Ooo00oOo00o + O0oO + O0oO * OoOoOO00
def o0Oo ( heading , announce ) :
 class o0O0 ( ) :
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
   try : Iii1I1111ii = open ( announce ) ; I1I1Iiii1 = Iii1I1111ii . read ( )
   except : I1I1Iiii1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1I1Iiii1 ) )
   return
 o0O0 ( )
 if 2 - 2: o0000oOoOoO0o + o0oO0
def o00OoOoOo0OoO ( ) :
 o0Oo ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 75 - 75: IIII - OOooOOo % oO0o0ooO0 + i11iIiiIii
 if 100 - 100: o0000oOoOoO0o + OOooOOo - i11iIiiIii - OoOoOO00
 if 40 - 40: I1IiI % Ooo00oOo00o
 if 62 - 62: OOooOOo
 if 15 - 15: o0000oOoOoO0o + o00O0oo . OoOO0ooOOoo0O * Ooo00oOo00o . I1IiI
def o0Oo00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
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
def OoOOo00 ( url ) :
 OOoo0O = Oo0ooOo0o ( II + O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 94 - 94: o0000oOoOoO0o . o0000oOoOoO0o + i11iIiiIii - OoOO0ooOOoo0O * ii11ii1ii
def iIoo0ooooO ( url ) :
 OOoo0O = Oo0ooOo0o ( II + iiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 36 - 36: o0000oOoOoO0o . OoOoOO00
def iIIiI1iiI ( url ) :
 OOoo0O = Oo0ooOo0o ( II + I11Ii111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 98 - 98: iIii1I11I1II1 + O0oO % I1IiI + o0000oOoOoO0o % I1IiI
def iI1I1I11IiII ( url ) :
 OOoo0O = Oo0ooOo0o ( II + iIii11iI1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 42 - 42: o0oO0 - OOOo0 + ii11ii1ii % o00O0oo
def IiIi1III ( url ) :
 OOoo0O = Oo0ooOo0o ( II + Ii1ii11IIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 82 - 82: OoOO * iIii1I11I1II1 . OOooOOo . ii11ii1ii + OoOO0ooOOoo0O / OOOo0
def O0O0O ( url ) :
 OOoo0O = Oo0ooOo0o ( II + iIiiIIi11I11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 71 - 71: Oo / OOooOOo + OoOO0ooOOoo0O
def i11i11 ( url ) :
 OOoo0O = Oo0ooOo0o ( II + i1iiIII1IIiIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 19 - 19: oO0o0ooO0 - OOooOOo / OOooOOo + Oo
def OoO0o0000O ( url ) :
 OOoo0O = Oo0ooOo0o ( II + II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 97 - 97: OoOO
def oOoO0O00oo ( url ) :
 OOoo0O = Oo0ooOo0o ( II + OOoOoo00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 42 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 9 - 9: OoOoOO00 * OoOoOO00 . i11iIiiIii * iIii1I11I1II1
def II1I11Iii1 ( url ) :
 OOoo0O = Oo0ooOo0o ( II + i1iIIi1II1iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOoo0O )
 for ooo0O , url , oOoO0o00OO0 , i1I1ii , oOOo0 in iiIii :
  O0O00o0OOO0 ( ooo0O , url , 5 , oOoO0o00OO0 , i1I1ii , oOOo0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 31 - 31: OOooOOo % o0000oOoOoO0o + iIii1I11I1II1 + i11iIiiIii * O0oO
 if 45 - 45: OoOO0ooOOoo0O * O0oO . o0oO0 - O0oO + IIII
 if 34 - 34: OoOO0ooOOoo0O . Oo
 if 78 - 78: ii11ii1ii % OOOo0 / OoooooooOO % OoOO0ooOOoo0O - oO0o0ooO0
 if 2 - 2: iIii1I11I1II1
 if 45 - 45: OoooooooOO / i11iIiiIii
 if 10 - 10: oO0o0ooO0 - OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - ii11ii1ii
 if 97 - 97: OoOoOO00 % O0oO + O0oO - Ooo00oOo00o / o00O0oo * OOOo0
 if 17 - 17: o00O0oo
def i1i1IiIi1 ( ) :
 try :
  if os . path . exists ( O0OoO000O0OO ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I1i1i1iii , I1111i , iIIii in os . walk ( O0OoO000O0OO ) :
     I1iiIiI1iI1I = 0
     I1iiIiI1iI1I += len ( iIIii )
     if I1iiIiI1iI1I > 0 :
      for Iii1I1111ii in iIIii :
       os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
  III1II111Ii1 = os . path . join ( oOOoO0 , "Textures13.db" )
  os . unlink ( III1II111Ii1 )
  i1iiIII111ii . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 82 - 82: O0oO - OoOO0ooOOoo0O + Ooo00oOo00o
 if 64 - 64: OOooOOo . O0 * o00O0oo + OoooooooOO - Oo . OoooooooOO
 if 70 - 70: Oo - OoOO . iIii1I11I1II1 % o0000oOoOoO0o / I1IiI - O0
 if 55 - 55: oO0o0ooO0 - Ooo00oOo00o
 if 100 - 100: O0
 if 79 - 79: iIii1I11I1II1
 if 81 - 81: OoOO0ooOOoo0O + iIii1I11I1II1 * O0oO - iIii1I11I1II1 . OoOO0ooOOoo0O
 if 48 - 48: o0000oOoOoO0o . OoooooooOO . OOOo0 . I1IiI % ii11ii1ii / oO0o0ooO0
 if 11 - 11: i1IIi % Ooo00oOo00o % oO0o0ooO0
def O0Oo0 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 OOooO0OO0 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( OOooO0OO0 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( OOooO0OO0 ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 5 - 5: oO0o0ooO0
   if 62 - 62: I1IiI . OoooooooOO . OoOO0ooOOoo0O . Ooo00oOo00o * oO0o0ooO0
   if I1iiIiI1iI1I > 0 :
    if 78 - 78: OoOO / Ooo00oOo00o - OoOO * OoooooooOO . I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete KODI Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 96 - 96: OOOo0 % i1IIi . OOooOOo . O0
     for Iii1I1111ii in iIIii :
      try :
       os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
      except :
       pass
     for Ii1Iii11 in I1111i :
      try :
       shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      except :
       pass
       if 97 - 97: OoOO0ooOOoo0O / OoOO . OoOoOO00
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  i1i11i1Ii11 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 60 - 60: OoOO0ooOOoo0O / OOOo0
  for I1i1i1iii , I1111i , iIIii in os . walk ( i1i11i1Ii11 ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 78 - 78: o0000oOoOoO0o . IIII
   if I1iiIiI1iI1I > 0 :
    if 38 - 38: I1IiI + IIII
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( I1iiIiI1iI1I ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 15 - 15: Oo + o0000oOoOoO0o . o0oO0 - iIii1I11I1II1 / O0 % iIii1I11I1II1
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 86 - 86: OOOo0 / OoOO * o00O0oo
   else :
    pass
  O00o = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 86 - 86: ii11ii1ii * OoOoOO00 * o0000oOoOoO0o
  for I1i1i1iii , I1111i , iIIii in os . walk ( O00o ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 74 - 74: ii11ii1ii / IIII
   if I1iiIiI1iI1I > 0 :
    if 60 - 60: ii11ii1ii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( I1iiIiI1iI1I ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 1 - 1: I1IiI . i11iIiiIii % I1IiI - oO0o0ooO0 % i1IIi + ii11ii1ii
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 2 - 2: iIii1I11I1II1 * OoOO / I1IiI . o0000oOoOoO0o / IIII
   else :
    pass
    if 75 - 75: I1IiI
    if 78 - 78: o00O0oo + I1IiI + IIII - IIII . i11iIiiIii / Ooo00oOo00o
    if 27 - 27: o00O0oo - O0 % o0000oOoOoO0o * O0oO . IIII % iIii1I11I1II1
    if 37 - 37: OoooooooOO + O0 - i1IIi % o0oO0
 i1I1i1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( i1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i1I1i1i ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 36 - 36: OoOoOO00 % O0
   if 35 - 35: iIii1I11I1II1 - OoOO0ooOOoo0O % OOooOOo
   if I1iiIiI1iI1I > 0 :
    if 30 - 30: O0oO % O0oO % IIII . I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete WTF Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 9 - 9: o0oO0 / OoOoOO00 . I1IiI % OOooOOo * OoOoOO00 - o0oO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 55 - 55: OOOo0
   else :
    pass
    if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
    if 35 - 35: ii11ii1ii / oO0o0ooO0 % OOOo0 + iIii1I11I1II1
 oO00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( oO00o ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( oO00o ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 36 - 36: O0oO . OoOoOO00 % o0oO0
   if 84 - 84: OoooooooOO - i11iIiiIii / iIii1I11I1II1 / OoooooooOO / ii11ii1ii
   if I1iiIiI1iI1I > 0 :
    if 4 - 4: Oo + OOooOOo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete 4oD Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: Ooo00oOo00o * I1IiI
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 15 - 15: i11iIiiIii / o0oO0 % OOOo0
   else :
    pass
    if 71 - 71: O0oO / ii11ii1ii * iIii1I11I1II1
    if 57 - 57: OoOO0ooOOoo0O + O0oO % ii11ii1ii . Ooo00oOo00o / Ooo00oOo00o * O0
 Ii1iiII1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( Ii1iiII1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( Ii1iiII1i ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 52 - 52: OoOO / O0oO
   if 91 - 91: IIII . Oo + OoOoOO00
   if I1iiIiI1iI1I > 0 :
    if 36 - 36: O0 * Ooo00oOo00o % oO0o0ooO0 * oO0o0ooO0 / Ooo00oOo00o * IIII
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete BBC iPlayer Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: i1IIi . IIII + O0 * o0oO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 76 - 76: Ooo00oOo00o
   else :
    pass
    if 92 - 92: o0000oOoOoO0o - iIii1I11I1II1 % OoooooooOO
    if 39 - 39: oO0o0ooO0 . OOOo0 * I1IiI - i11iIiiIii
    if 1 - 1: oO0o0ooO0 * I1IiI
 OO0ooo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( OO0ooo0 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( OO0ooo0 ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 7 - 7: ii11ii1ii - OoOO * OoOO0ooOOoo0O + OOooOOo . ii11ii1ii
   if 85 - 85: O0
   if I1iiIiI1iI1I > 0 :
    if 32 - 32: OoooooooOO . Ooo00oOo00o / Oo * OOooOOo / OOooOOo * o00O0oo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Simple Downloader Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: o00O0oo
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 55 - 55: OoOO0ooOOoo0O % OoOO0ooOOoo0O / O0 % oO0o0ooO0 - OOooOOo . Oo
   else :
    pass
    if 49 - 49: iIii1I11I1II1 * i1IIi . OoooooooOO
    if 90 - 90: OOooOOo % ii11ii1ii - iIii1I11I1II1 % I1IiI
 IIiI11I1I1i1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IIiI11I1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( IIiI11I1I1i1i ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 86 - 86: i1IIi
   if 13 - 13: O0
   if I1iiIiI1iI1I > 0 :
    if 70 - 70: o00O0oo . i11iIiiIii % o00O0oo . O0 - iIii1I11I1II1
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ITV Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 26 - 26: OoOO0ooOOoo0O
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 76 - 76: i1IIi * OoooooooOO * O0 + O0oO * O0oO
   else :
    pass
    if 35 - 35: OOooOOo
    if 73 - 73: O0 - ii11ii1ii
 ii1IoO0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( IIiI11I1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( ii1IoO0O ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 59 - 59: OoooooooOO * Oo + i1IIi
   if 23 - 23: o0oO0
   if I1iiIiI1iI1I > 0 :
    if 13 - 13: iIii1I11I1II1
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Movies4me Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 77 - 77: i11iIiiIii - iIii1I11I1II1 / OoOO / o0oO0 / Ooo00oOo00o
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 56 - 56: OoooooooOO * O0
   else :
    pass
    if 85 - 85: OoooooooOO % I1IiI * iIii1I11I1II1
    if 44 - 44: iIii1I11I1II1 . ii11ii1ii + O0oO . o0oO0
 II1i11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( IIiI11I1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( II1i11 ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 28 - 28: OoOoOO00 - OoOO % I1IiI + Ooo00oOo00o - I1IiI
   if 28 - 28: OoOoOO00 . OoOO + O0 . O0 . OoOO0ooOOoo0O
   if I1iiIiI1iI1I > 0 :
    if 98 - 98: OoooooooOO % O0 - O0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Phoenix Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 76 - 76: i1IIi % I1IiI - OOOo0 / OOooOOo * o0oO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 4 - 4: Oo * Oo / I1IiI
   else :
    pass
    if 4 - 4: OOOo0 * I1IiI % o0000oOoOoO0o . I1IiI
    if 11 - 11: OoOO0ooOOoo0O - I1IiI - OOooOOo * I1IiI + o0oO0
 oooo0O0o0OoOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( IIiI11I1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( oooo0O0o0OoOO ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 36 - 36: OoOO / O0oO - OOOo0 . OOOo0
   if 2 - 2: IIII + ii11ii1ii
   if I1iiIiI1iI1I > 0 :
    if 91 - 91: ii11ii1ii % o0oO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Music Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: oO0o0ooO0 - OoOO0ooOOoo0O . OOOo0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 51 - 51: OoOO + Ooo00oOo00o + oO0o0ooO0 + oO0o0ooO0 % OOooOOo
   else :
    pass
    if 29 - 29: o0oO0
    if 41 - 41: O0 % oO0o0ooO0
 i1iIi1IIiIII1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( IIiI11I1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i1iIi1IIiIII1 ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 19 - 19: o0000oOoOoO0o
   if 87 - 87: o0oO0 / I1IiI % OOooOOo * OoOO
   if I1iiIiI1iI1I > 0 :
    if 77 - 77: OoOO - Oo - iIii1I11I1II1
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete SuperCartoons Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 16 - 16: Ooo00oOo00o / oO0o0ooO0 / i1IIi . oO0o0ooO0 + OoOO
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 26 - 26: iIii1I11I1II1 + i1IIi / I1IiI % ii11ii1ii
   else :
    pass
    if 44 - 44: OoooooooOO . OoOoOO00 . OoOO0ooOOoo0O % OoooooooOO
    if 86 - 86: i11iIiiIii + O0 * IIII - Ooo00oOo00o * OoOO0ooOOoo0O + O0
 Oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( IIiI11I1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( Oo0 ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 94 - 94: O0oO % OoOoOO00 * i1IIi * iIii1I11I1II1
   if 81 - 81: Oo - o0000oOoOoO0o
   if I1iiIiI1iI1I > 0 :
    if 24 - 24: OoooooooOO . Ooo00oOo00o * OoOoOO00
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete TVonline Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 59 - 59: O0oO + Ooo00oOo00o / OoOO0ooOOoo0O
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 97 - 97: Oo * oO0o0ooO0 % o0oO0 . oO0o0ooO0 - O0oO - OoOO0ooOOoo0O
   else :
    pass
    if 79 - 79: OOOo0 - o0oO0
    if 37 - 37: IIII . Oo * Oo * OoOoOO00 * O0
 o00O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( IIiI11I1I1i1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( o00O ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 88 - 88: i11iIiiIii + oO0o0ooO0 * I1IiI * oO0o0ooO0 + o0000oOoOoO0o
   if 88 - 88: OoOO0ooOOoo0O % Oo - oO0o0ooO0 - I1IiI % i11iIiiIii
   if I1iiIiI1iI1I > 0 :
    if 6 - 6: o00O0oo - Ooo00oOo00o . OOOo0 - O0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 16 - 16: oO0o0ooO0 * oO0o0ooO0 % o00O0oo % OOOo0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
      if 48 - 48: OoOO0ooOOoo0O / o00O0oo % Ooo00oOo00o / IIII / O0oO
   else :
    pass
    if 89 - 89: O0oO * OoOO
    if 63 - 63: OoooooooOO * OoooooooOO % Ooo00oOo00o + O0 / O0oO + iIii1I11I1II1
    if 72 - 72: I1IiI * iIii1I11I1II1 % o0000oOoOoO0o
 IiIi1I1i1II = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 try :
  if i1iiIII111ii . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   iI1I1 = os . path . join ( IiIi1I1i1II , "cache.db" )
   os . unlink ( iI1I1 )
   if 46 - 46: iIii1I11I1II1
 except :
  pass
  if 33 - 33: o0000oOoOoO0o % o0000oOoOoO0o % O0 / OOOo0 . i1IIi
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 91 - 91: o0oO0 * o0000oOoOoO0o - OoOoOO00 . OOOo0 - Oo + o0oO0
 if 56 - 56: OOooOOo / IIII * OOOo0 . OOooOOo
 if 15 - 15: i11iIiiIii
 if 13 - 13: o0000oOoOoO0o * OoOoOO00 * OoOO * OoOoOO00 % IIII / OOOo0
 if 100 - 100: IIII . o00O0oo - iIii1I11I1II1 . i11iIiiIii / OoOoOO00
 if 71 - 71: O0oO * Oo . o0000oOoOoO0o
 if 49 - 49: IIII * O0 . IIII
 if 19 - 19: OoOoOO00 - IIII
 if 59 - 59: OOooOOo * Ooo00oOo00o - o00O0oo . OoOO0ooOOoo0O
def o0OO00oo0O ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 Ii1I1i111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i1i1iii , I1111i , iIIii in os . walk ( Ii1I1i111 ) :
   I1iiIiI1iI1I = 0
   I1iiIiI1iI1I += len ( iIIii )
   if 57 - 57: OoOO . OOOo0
   if 6 - 6: o0oO0
   if I1iiIiI1iI1I > 0 :
    if 39 - 39: o0oO0 / O0 * IIII
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Package Cache Files" , str ( I1iiIiI1iI1I ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: o00O0oo / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % OoOO0ooOOoo0O
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for Ii1Iii11 in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , Ii1Iii11 ) )
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
 if 14 - 14: OOooOOo % IIII + ii11ii1ii + Ooo00oOo00o
 if 76 - 76: Ooo00oOo00o - i11iIiiIii + I1IiI + OoOO0ooOOoo0O / OoooooooOO
 if 50 - 50: OoOoOO00 - O0oO + iIii1I11I1II1 + iIii1I11I1II1
 if 91 - 91: OoOoOO00 - O0 . iIii1I11I1II1 . O0 + ii11ii1ii - OoOoOO00
 if 26 - 26: OOooOOo
 if 12 - 12: OoooooooOO / O0 + OoOoOO00 * ii11ii1ii
 if 46 - 46: OoOoOO00 - IIII * OoooooooOO / OoOO % IIII
 if 11 - 11: iIii1I11I1II1 . I1IiI / IIII % o0oO0
 if 61 - 61: o0oO0 - OoOO0ooOOoo0O + OoOO0ooOOoo0O
def iii ( url , name ) :
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiIIII1iiIIi = os . path . join ( OoOO000 , 'advancedsettings.xml' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1I1IiI1ii = os . path . join ( OoOO000 , 'advancedsettings.xml.bak' )
 if os . path . exists ( i1I1IiI1ii ) == False :
  if i1iiIII111ii . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   IiIIII1iiIIi = os . path . join ( OoOO000 , 'advancedsettings.xml' )
   try :
    os . remove ( IiIIII1iiIIi )
    print '=== GenieTv - REMOVING    ' + str ( IiIIII1iiIIi ) + '    ==='
   except :
    pass
   OOoo0O = I11 . http_GET ( url ) . content
   o00O0O = open ( IiIIII1iiIIi , "w" )
   o00O0O . write ( OOoo0O )
   o00O0O . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( IiIIII1iiIIi ) + '    ==='
   i1iiIII111ii = xbmcgui . Dialog ( )
   i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  IiIIII1iiIIi = os . path . join ( OoOO000 , 'advancedsettings.xml' )
  try :
   os . remove ( IiIIII1iiIIi )
   print '=== GenieTv - REMOVING    ' + str ( IiIIII1iiIIi ) + '    ==='
  except :
   pass
  OOoo0O = I11 . http_GET ( url ) . content
  o00O0O = open ( IiIIII1iiIIi , "w" )
  o00O0O . write ( OOoo0O )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiIIII1iiIIi ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 64 - 64: oO0o0ooO0 * ii11ii1ii % OoOoOO00 - I1IiI + ii11ii1ii
def OO0OOoo0OOO ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiIIII1iiIIi = os . path . join ( OoOO000 , 'advancedsettings.xml' )
 try :
  o00O0O = open ( IiIIII1iiIIi ) . read ( )
  if 'zero' in o00O0O :
   name = '0CACHE'
  elif 'tuxen' in o00O0O :
   name = 'TUXENS'
  elif 'muckys' in o00O0O :
   name = 'MUCKYS'
  elif 'p2p1' in o00O0O :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in o00O0O :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in o00O0O :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 94 - 94: i11iIiiIii % OoooooooOO / OOOo0
def iII1Iii11111 ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 OoOO000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiIIII1iiIIi = os . path . join ( OoOO000 , 'advancedsettings.xml' )
 try :
  os . remove ( IiIIII1iiIIi )
  i1iiIII111ii = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( IiIIII1iiIIi ) + '    ==='
  i1iiIII111ii . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 80 - 80: OoOO * o0000oOoOoO0o / iIii1I11I1II1 % OoOO / iIii1I11I1II1
 if 42 - 42: i1IIi / i11iIiiIii . Oo * oO0o0ooO0 . i11iIiiIii * O0
 if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + IIII
 if 27 - 27: OoOO0ooOOoo0O
 if 52 - 52: O0oO % I1IiI + iIii1I11I1II1 * OoOO . o00O0oo
 if 95 - 95: iIii1I11I1II1 . IIII - OoooooooOO * Ooo00oOo00o / OOooOOo
 if 74 - 74: OoOO
 if 34 - 34: oO0o0ooO0
 if 44 - 44: i1IIi % OOOo0 % OOooOOo
 if 9 - 9: Oo % OoooooooOO - o00O0oo
def iIII11Iiii1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iiIii = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for o0oo0 , OoO0OOoO0Oo0 , oO00O , II111IiiiI1 in iiIii :
  if inc < 2 : i1iiIII111ii = xbmcgui . Dialog ( ) ; i1iiIII111ii . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % o0oo0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oO00O , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % II111IiiiI1 )
  inc = inc + 1
  if 75 - 75: o0oO0
  if 29 - 29: ii11ii1ii
  if 53 - 53: i11iIiiIii . ii11ii1ii % o00O0oo / o0oO0 % iIii1I11I1II1
  if 6 - 6: Oo - OoOO0ooOOoo0O . iIii1I11I1II1
  if 30 - 30: o0oO0 + o0oO0 % IIII - OOooOOo - ii11ii1ii
  if 36 - 36: o0000oOoOoO0o % OoOO0ooOOoo0O
  if 72 - 72: OOOo0 / oO0o0ooO0 - O0 + o0000oOoOoO0o
  if 83 - 83: O0
  if 89 - 89: Oo + ii11ii1ii - OOooOOo
def iII1I11 ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  OoOO000 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  IiIIII1iiIIi = os . path . join ( OoOO000 , 'addons2.ini' )
  OOoo0O = I11 . http_GET ( url ) . content
  o00O0O = open ( IiIIII1iiIIi , "w" )
  o00O0O . write ( OOoo0O )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiIIII1iiIIi ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 15 - 15: o0000oOoOoO0o
def IiiI11I1IIiI ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  OoOO000 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  IiIIII1iiIIi = os . path . join ( OoOO000 , 'settings.xml' )
  OOoo0O = I11 . http_GET ( url ) . content
  o00O0O = open ( IiIIII1iiIIi , "w" )
  o00O0O . write ( OOoo0O )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiIIII1iiIIi ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 5 - 5: Oo
 if 100 - 100: o00O0oo + iIii1I11I1II1
def o0o0OoO0OOO0 ( ) :
 try :
  oO0OOOO0o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( oO0OOOO0o0 ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    oOO0 = os . path . join ( oO0OOOO0o0 , "source.db" )
    os . unlink ( oOO0 )
  i1iiIII111ii . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 90 - 90: IIII - ii11ii1ii % o0000oOoOoO0o % iIii1I11I1II1 - ii11ii1ii
 if 20 - 20: O0 - OoooooooOO - IIII + iIii1I11I1II1
 if 94 - 94: o00O0oo . i1IIi
 if 71 - 71: oO0o0ooO0 + Ooo00oOo00o - IIII . Ooo00oOo00o . IIII + OOOo0
 if 26 - 26: O0
def Oo0ooOo0o ( url ) :
 oOIIiIi = urllib2 . Request ( url )
 oOIIiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOooOoOOOoo = urllib2 . urlopen ( oOIIiIi )
 OOoo0O = OOoOooOoOOOoo . read ( )
 OOoOooOoOOOoo . close ( )
 return OOoo0O
 if 17 - 17: OoOoOO00
 if 9 - 9: OoooooooOO + OoOO
 if 33 - 33: O0
 if 39 - 39: OOOo0 + Oo
 if 83 - 83: i1IIi
 if 76 - 76: o00O0oo + iIii1I11I1II1 + I1IiI . Ooo00oOo00o
 if 49 - 49: IIII / o0oO0 / OoOO0ooOOoo0O
def IiIiIi1I11I ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; IiI1i1i = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if IiI1i1i :
  o0OOOOOo0 = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; o0OOOOOo0 = xbmc . translatePath ( o0OOOOOo0 ) ;
  oooOoO = os . path . join ( o0OOOOOo0 , ".." , ".." ) ; oooOoO = os . path . abspath ( oooOoO ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oooOoO ) ; O0Oo0iIIIi1IiI11I1 = False
  try :
   for I1i1i1iii , I1111i , iIIii in os . walk ( oooOoO , topdown = True ) :
    I1111i [ : ] = [ Ii1Iii11 for Ii1Iii11 in I1111i if Ii1Iii11 not in Oo0oO0ooo ]
    for ooo0O in iIIii :
     try : os . remove ( os . path . join ( I1i1i1iii , ooo0O ) )
     except :
      if ooo0O not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0Oo0iIIIi1IiI11I1 = True
      plugintools . log ( "Error removing " + I1i1i1iii + " " + ooo0O )
    for ooo0O in I1111i :
     try : os . rmdir ( os . path . join ( I1i1i1iii , ooo0O ) )
     except :
      if ooo0O not in [ "Database" , "userdata" ] : O0Oo0iIIIi1IiI11I1 = True
      plugintools . log ( "Error removing " + I1i1i1iii + " " + ooo0O )
   if not O0Oo0iIIIi1IiI11I1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 O0O00Oo ( )
 if 71 - 71: o00O0oo - O0 - oO0o0ooO0 . OoOO0ooOOoo0O % Oo
 if 82 - 82: OoooooooOO + OoOO0ooOOoo0O % I1IiI . Ooo00oOo00o * i1IIi
 if 2 - 2: Oo * O0
def ooOOo00oo0 ( ) :
 IIIII1Ii = [ ]
 iIiI1 = sys . argv [ 2 ]
 if len ( iIiI1 ) >= 2 :
  I1IiII1I1i1I1 = sys . argv [ 2 ]
  II11iiI = I1IiII1I1i1I1 . replace ( '?' , '' )
  if ( I1IiII1I1i1I1 [ len ( I1IiII1I1i1I1 ) - 1 ] == '/' ) :
   I1IiII1I1i1I1 = I1IiII1I1i1I1 [ 0 : len ( I1IiII1I1i1I1 ) - 2 ]
  iiIi = II11iiI . split ( '&' )
  IIIII1Ii = { }
  for OooooOo in range ( len ( iiIi ) ) :
   IIIiiiIiI = { }
   IIIiiiIiI = iiIi [ OooooOo ] . split ( '=' )
   if ( len ( IIIiiiIiI ) ) == 2 :
    IIIII1Ii [ IIIiiiIiI [ 0 ] ] = IIIiiiIiI [ 1 ]
    if 80 - 80: OoOO % OoOO % O0 - i11iIiiIii . oO0o0ooO0 / O0
 return IIIII1Ii
 if 13 - 13: OOOo0 + O0 - ii11ii1ii % Oo / o00O0oo . i1IIi
oO0o0Ooooo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
i1Ii11i1i = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OOo0oO00ooO00 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOOO00OoooO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
Ii1i1 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
IIIi = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
O00 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Ii1iiI1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
iiIIi = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
I11Ii111I = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iIii11iI1II = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Ii1ii11IIIi = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iIiiIIi11I11i = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
i1iiIII1IIiIIII = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
II1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OOoOoo00Oo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o0ooOOoO0oO0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o0O0OOO0Ooo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O00OOOoOoo0O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
IIiIi1iI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
ooOOoooooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
i1iIIi1II1iiI = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
I11iII = base64 . decodestring ( 'Q1VOVA==' )
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description ) :
 oo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 III1i1IiI1i = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  III1i1IiI1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0O , listitem = OooOo00o , isFolder = False )
 else :
  III1i1IiI1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0O , listitem = OooOo00o , isFolder = True )
 return III1i1IiI1i
def O0OOO0OOoO0O ( name , url , mode , iconimage , fanart , description ) :
 oo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 III1i1IiI1i = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 III1i1IiI1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0O , listitem = OooOo00o , isFolder = False )
 return III1i1IiI1i
 if 86 - 86: i1IIi / o00O0oo * OOOo0
 if 67 - 67: ii11ii1ii * ii11ii1ii / OoOO * OoooooooOO + I1IiI
I1IiII1I1i1I1 = ooOOo00oo0 ( )
i1Ii = None
ooo0O = None
oooo = None
oOoO0o00OO0 = None
i1I1ii = None
oOOo0 = None
if 63 - 63: o0oO0 % OOOo0
if 75 - 75: o0oO0 / Oo
try :
 i1Ii = urllib . unquote_plus ( I1IiII1I1i1I1 [ "url" ] )
except :
 pass
try :
 ooo0O = urllib . unquote_plus ( I1IiII1I1i1I1 [ "name" ] )
except :
 pass
try :
 oOoO0o00OO0 = urllib . unquote_plus ( I1IiII1I1i1I1 [ "iconimage" ] )
except :
 pass
try :
 oooo = int ( I1IiII1I1i1I1 [ "mode" ] )
except :
 pass
try :
 i1I1ii = urllib . unquote_plus ( I1IiII1I1i1I1 [ "fanart" ] )
except :
 pass
try :
 oOOo0 = urllib . unquote_plus ( I1IiII1I1i1I1 [ "description" ] )
except :
 pass
 if 8 - 8: iIii1I11I1II1
 if 30 - 30: o00O0oo - i11iIiiIii
print str ( iiI1IiI ) + ': ' + str ( iIii1 )
print "Mode: " + str ( oooo )
print "URL: " + str ( i1Ii )
print "Name: " + str ( ooo0O )
print "IconImage: " + str ( oOoO0o00OO0 )
if 3 - 3: IIII / o0000oOoOoO0o
if 34 - 34: i11iIiiIii / O0oO * OoOO0ooOOoo0O . Oo
def o0oo0o0O00OO ( content , viewType ) :
 if 79 - 79: O0oO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 31 - 31: OoOO0ooOOoo0O % O0oO
  if 98 - 98: IIII * iIii1I11I1II1 . o00O0oo * Oo / ii11ii1ii + o0oO0
if oooo == None :
 oOOO00o ( )
 if 25 - 25: OoOO
elif oooo == 1 :
 OoO0o ( i1Ii )
 if 19 - 19: OOOo0 % o00O0oo . IIII * o0oO0
elif oooo == 44 :
 Ii1I1i ( i1Ii )
 if 89 - 89: I1IiI . OoOO0ooOOoo0O
elif oooo == 2 :
 iI1Iii ( )
 if 7 - 7: OoOO % I1IiI - OOOo0 + Oo
elif oooo == 3 :
 OO00Oo ( )
 if 70 - 70: OoOoOO00 + O0oO + i11iIiiIii - i1IIi / IIII
elif oooo == 21 :
 iII ( )
 if 40 - 40: ii11ii1ii * O0oO
elif oooo == 4 :
 Oo0oOOo ( )
 if 38 - 38: O0 . Oo + I1IiI - OoOO
elif oooo == 5 :
 oOOoo00O00o ( ooo0O , i1Ii , oOOo0 )
 if 43 - 43: oO0o0ooO0 + Oo / OoooooooOO
elif oooo == 6 :
 o0OO00oo0O ( i1Ii )
 if 24 - 24: O0 + OOooOOo * o00O0oo - O0oO
elif oooo == 7 :
 iii ( i1Ii , ooo0O )
 if 10 - 10: i11iIiiIii
elif oooo == 8 :
 OO0OOoo0OOO ( i1Ii , ooo0O )
 if 21 - 21: OOOo0 / oO0o0ooO0
elif oooo == 9 :
 FIXREPOSADDONS ( i1Ii )
 if 69 - 69: o0oO0 % o0oO0
elif oooo == 10 :
 o0Oo00 ( )
 if 76 - 76: i11iIiiIii * oO0o0ooO0 / Ooo00oOo00o % ii11ii1ii + OoOO0ooOOoo0O
elif oooo == 11 :
 iII1Iii11111 ( i1Ii )
 if 48 - 48: iIii1I11I1II1 % i1IIi + I1IiI % OOooOOo
elif oooo == 12 :
 iIII11Iiii1 ( )
 if 79 - 79: I1IiI % OOOo0 % o00O0oo / i1IIi % Ooo00oOo00o
elif oooo == 13 :
 i1i1IiIi1 ( )
 if 56 - 56: iIii1I11I1II1 - i11iIiiIii * oO0o0ooO0
elif oooo == 14 :
 O0Oo0 ( i1Ii )
 if 84 - 84: OoOO0ooOOoo0O + o00O0oo + OOooOOo
elif oooo == 15 :
 iiiI1I11i1 ( )
 if 33 - 33: o00O0oo
elif oooo == 16 :
 iII1I11 ( i1Ii , ooo0O )
 if 93 - 93: o0oO0
elif oooo == 17 :
 IiiI11I1IIiI ( i1Ii , ooo0O )
 if 34 - 34: OoOO - o0oO0 * Oo / OOooOOo
elif oooo == 18 :
 o0o0OoO0OOO0 ( )
 if 19 - 19: ii11ii1ii
elif oooo == 19 :
 I1I1I ( ooo0O , i1Ii , oOOo0 )
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
elif oooo == 40 :
 o0O ( ooo0O , i1Ii , oOOo0 )
 if 66 - 66: O0
elif oooo == 42 :
 IIIIii1I ( ooo0O , i1Ii , oOOo0 )
 if 52 - 52: Ooo00oOo00o * OoooooooOO
elif oooo == 43 :
 I111iI ( ooo0O , i1Ii , oOOo0 )
 if 12 - 12: O0 + IIII * i1IIi . Ooo00oOo00o
elif oooo == 20 :
 iIIoO00o0 ( i1Ii )
 if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
elif oooo == 22 :
 OoOOo00 ( i1Ii )
 if 28 - 28: iIii1I11I1II1
elif oooo == 23 :
 iIoo0ooooO ( i1Ii )
 if 7 - 7: OOooOOo % IIII * I1IiI
elif oooo == 24 :
 iIIiI1iiI ( i1Ii )
 if 58 - 58: IIII / o0000oOoOoO0o + OoOoOO00 % oO0o0ooO0 - OoooooooOO
elif oooo == 25 :
 iI1I1I11IiII ( i1Ii )
 if 25 - 25: I1IiI % OoooooooOO * Oo - i1IIi * OoOoOO00 * OoOO
elif oooo == 26 :
 IiIi1III ( i1Ii )
 if 30 - 30: o0000oOoOoO0o % I1IiI / ii11ii1ii * O0 * o00O0oo . OOOo0
elif oooo == 27 :
 O0O0O ( i1Ii )
 if 46 - 46: I1IiI - O0
elif oooo == 28 :
 i11i11 ( i1Ii )
 if 70 - 70: o0000oOoOoO0o + Oo * iIii1I11I1II1 . OOOo0 * o0000oOoOoO0o
elif oooo == 29 :
 OoO0o0000O ( i1Ii )
 if 49 - 49: OOooOOo
elif oooo == 30 :
 i1IIIII11I1IiI ( i1Ii )
 if 25 - 25: oO0o0ooO0 . OoooooooOO * iIii1I11I1II1 . OOooOOo / O0 + o00O0oo
elif oooo == 31 :
 oOoO0O00oo ( i1Ii )
 if 68 - 68: Oo
elif oooo == 32 :
 I1ii11iI ( )
 if 22 - 22: OoOO0ooOOoo0O
elif oooo == 33 :
 OOoO ( )
 if 22 - 22: oO0o0ooO0 * o0000oOoOoO0o - Oo * O0 / i11iIiiIii
elif oooo == 35 :
 O00oO000O0O ( i1Ii )
 if 78 - 78: Oo * O0 / o0oO0 + OoooooooOO + OoOO0ooOOoo0O
elif oooo == 34 :
 o00oooO0Oo ( i1Ii )
 if 23 - 23: oO0o0ooO0 % OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
elif oooo == 36 :
 ooo00OOOooO ( i1Ii )
 if 94 - 94: i1IIi
elif oooo == 37 :
 Oo0oO ( i1Ii )
 if 36 - 36: OOOo0 + Oo
elif oooo == 38 :
 IiIIIi1iIi ( i1Ii )
 if 46 - 46: oO0o0ooO0
elif oooo == 41 :
 IiIiIi1I11I ( I1IiII1I1i1I1 )
 if 65 - 65: i1IIi . ii11ii1ii / o0oO0
elif oooo == 39 :
 II1I11Iii1 ( i1Ii )
 if 11 - 11: IIII * o0oO0 / o0oO0 - OoOO0ooOOoo0O
elif oooo == 45 :
 TEXTS ( )
 if 68 - 68: OOOo0 % IIII - IIII / OOOo0 + ii11ii1ii - Oo
elif oooo == 46 :
 o00OoOoOo0OoO ( )
 if 65 - 65: o0oO0 - i1IIi
elif oooo == 47 :
 GEVID ( )
 if 62 - 62: o0000oOoOoO0o / OoOO % Oo . OoooooooOO / i11iIiiIii / O0oO
elif oooo == 48 :
 OoO0OOOOo0O ( ooo0O , i1Ii , oOOo0 )
 if 60 - 60: OOOo0 % OoOO / OOooOOo % OoOO * i11iIiiIii / oO0o0ooO0
elif oooo == 49 :
 oO0o0OOOO ( )
 if 34 - 34: O0oO - OoOO0ooOOoo0O
elif oooo == 222 :
 o0ooOo0OOOO0o ( i1Ii )
 if 25 - 25: OoOO % OOOo0 + i11iIiiIii + O0 * OoooooooOO
elif oooo == 333 :
 ii1iI111 ( i1Ii )
 if 64 - 64: i1IIi
 if 10 - 10: O0oO % O0 / OOOo0 % o0000oOoOoO0o
elif oooo == 1001 :
 IIi ( )
 if 25 - 25: OoOoOO00 / Ooo00oOo00o
elif oooo == 1005 :
 ooOo ( )
 if 64 - 64: O0 % o0oO0
elif oooo == 1007 :
 o0oO0OoO0 ( i1Ii )
 if 40 - 40: OOooOOo + o0000oOoOoO0o
elif oooo == 1010 :
 Oo00O0ooOO ( i1Ii )
 if 77 - 77: i11iIiiIii % IIII + O0oO % OoooooooOO - o0000oOoOoO0o
elif oooo == 1011 :
 IiiI ( i1Ii )
 if 26 - 26: Oo + O0 - iIii1I11I1II1
elif oooo == 1030 :
 i11I1 ( )
 if 47 - 47: OoooooooOO
elif oooo == 1031 :
 Ii1iIi111i1i1 ( i1Ii , oOoO0o00OO0 )
 if 2 - 2: I1IiI % O0oO * Oo * I1IiI
elif oooo == 1006 :
 Parse . ParseURL ( i1Ii )
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
elif oooo == 2030 :
 Parse . addonParseURL ( i1Ii )
 if 26 - 26: OOooOOo % OoOO0ooOOoo0O + OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / oO0o0ooO0
elif oooo == 2031 :
 Parse . apkParseURL ( i1Ii )
 if 64 - 64: OoOO % I1IiI / OoOoOO00 % o0oO0 - oO0o0ooO0
elif oooo == 1002 :
 o0o0oO0 ( i1Ii )
 if 2 - 2: O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
elif oooo == 1003 :
 ooOo0OoO ( i1Ii , oOoO0o00OO0 )
 if 26 - 26: OoOO0ooOOoo0O * Oo
elif oooo == 1004 :
 i1iiIIi1I ( i1Ii )
 if 31 - 31: o0000oOoOoO0o * OoOO . o00O0oo
elif oooo == 1008 :
 oOoOOo0oo0 ( )
 if 35 - 35: o0000oOoOoO0o
elif oooo == 1009 :
 M3UPLAY ( i1Ii )
 if 94 - 94: o0oO0 / i11iIiiIii % O0
elif oooo == 2001 :
 I1i ( i1Ii )
 if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
elif oooo == 1013 :
 OOOIIiI1i1i ( )
 if 95 - 95: OoooooooOO % OoooooooOO . o00O0oo
elif oooo == 1014 :
 i11iiI1111 ( )
 if 26 - 26: OoOO + IIII - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
elif oooo == 1015 :
 oOoooo000Oo00 ( i1Ii )
 if 68 - 68: O0
elif oooo == 1016 :
 iI11iiii1I ( i1Ii )
 if 76 - 76: ii11ii1ii
elif oooo == 1023 :
 O0oo0OO0oOOOo ( )
 if 99 - 99: OOooOOo
elif oooo == 1024 :
 oOo0O0O0 ( )
 if 1 - 1: o00O0oo * I1IiI * Ooo00oOo00o + Oo
elif oooo == 1025 :
 oOoo0 ( i1Ii )
 if 90 - 90: O0oO % Oo - Oo . iIii1I11I1II1 / OoOO0ooOOoo0O + o0000oOoOoO0o
elif oooo == 4001 :
 oOOO0o0o ( )
 if 89 - 89: OoOO
elif oooo == 4002 :
 iiI1 ( )
 if 87 - 87: oO0o0ooO0 % Oo
elif oooo == 4003 :
 Oo0O0O0ooO0O ( )
 if 62 - 62: Ooo00oOo00o + o0oO0 / oO0o0ooO0 * i11iIiiIii
elif oooo == 3000 :
 IiiIi ( )
 if 37 - 37: oO0o0ooO0
elif oooo == 404 :
 OoOO0OOoo ( ooo0O , i1Ii , oOoO0o00OO0 )
 if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
elif oooo == 7030 :
 II1i1i1iII1 ( )
 if 94 - 94: IIII * o0000oOoOoO0o * OoooooooOO / OOooOOo . IIII - OOooOOo
elif oooo == 7021 :
 iI1I1iIi11 ( ooo0O )
 if 13 - 13: OoOO0ooOOoo0O / IIII - Ooo00oOo00o / OoOO0ooOOoo0O . i1IIi
elif oooo == 7022 :
 iIII1i1i ( ooo0O )
 if 22 - 22: O0 - o0000oOoOoO0o + O0oO . o00O0oo * i1IIi
elif oooo == 7000 :
 OOOooo0OooOoO ( ooo0O , i1Ii , img )
 if 26 - 26: iIii1I11I1II1 * OOooOOo . o0000oOoOoO0o
elif oooo == 7050 :
 IIi1i1IiIIi1i ( )
 if 10 - 10: O0oO * OoOO % Oo - o0000oOoOoO0o % Oo
elif oooo == 7051 :
 O0iIi1IiII ( i1Ii )
 if 65 - 65: oO0o0ooO0 * iIii1I11I1II1 / O0 . o0000oOoOoO0o
elif oooo == 7060 :
 oOOo000oOoO0 ( )
 if 94 - 94: Oo . o0oO0 * i11iIiiIii - OOooOOo . oO0o0ooO0
elif oooo == 7061 :
 oOOoOooo0O0o ( i1Ii )
 if 98 - 98: OoOO0ooOOoo0O + o00O0oo
elif oooo == 7063 :
 OoOo00o0OO ( i1Ii )
 if 52 - 52: Oo / I1IiI - O0oO . oO0o0ooO0
elif oooo == 7062 :
 O0oOOO000oooo0 ( i1Ii )
 if 50 - 50: iIii1I11I1II1 - oO0o0ooO0 - o0000oOoOoO0o
elif oooo == 7064 :
 NATatozcat ( )
 if 60 - 60: iIii1I11I1II1 * o0oO0
elif oooo == 7067 :
 I1iii ( i1Ii )
 if 71 - 71: I1IiI % Oo % o0oO0
elif oooo == 7066 :
 NATatozA ( i1Ii )
 if 34 - 34: o0000oOoOoO0o / o0000oOoOoO0o % IIII . I1IiI / Oo
elif oooo == 7065 :
 oO0o0O0Ooo0o ( i1Ii )
 if 99 - 99: o0oO0 * OOOo0 - o0oO0 % o00O0oo
elif oooo == 7002 :
 i11I1I1iiI ( )
 if 40 - 40: OoOO0ooOOoo0O / IIII / iIii1I11I1II1 + o00O0oo
elif oooo == 7003 :
 IiiIIiiiiii ( i1Ii )
 if 59 - 59: o0000oOoOoO0o * OoooooooOO + OoOO0ooOOoo0O . iIii1I11I1II1 / i1IIi
elif oooo == 7004 :
 ooOo0OoOooo00 ( i1Ii )
 if 75 - 75: o0000oOoOoO0o . OoOO0ooOOoo0O - iIii1I11I1II1 * Ooo00oOo00o * oO0o0ooO0
elif oooo == 7020 :
 Oo0O ( i1Ii )
 if 93 - 93: o0oO0
elif oooo == 7001 :
 Oo00OOo00O ( )
 if 18 - 18: o0oO0
elif oooo == 7010 :
 Iii111Ii ( i1Ii )
 if 66 - 66: OoOO * i11iIiiIii + I1IiI / OoOO0ooOOoo0O
elif oooo == 7011 :
 III1I1i1 ( i1Ii )
 if 96 - 96: OoOO0ooOOoo0O + OoOO0ooOOoo0O % IIII % OoOO0ooOOoo0O
elif oooo == 7012 :
 I1i1111I ( i1Ii )
 if 28 - 28: iIii1I11I1II1 + I1IiI . OOooOOo % i11iIiiIii
elif oooo == 7013 :
 cnfTVPlay2 ( i1Ii )
elif oooo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( i1Ii )
elif oooo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( i1Ii )
elif oooo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( ooo0O , i1Ii , oOoO0o00OO0 )
elif oooo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oooo == 7018 :
 ooO000O ( )
elif oooo == 7019 :
 CNF_Studio_Indexer . List_Movies ( i1Ii )
elif oooo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( i1Ii )
elif oooo == 7024 :
 CNF_Studio_Indexer . Box_Office ( i1Ii )
 if 58 - 58: o0000oOoOoO0o / OoooooooOO % OoOO + Ooo00oOo00o
elif oooo == 8000 :
 IiI11iI1i1i1i ( )
elif oooo == 8001 :
 O000Oo0o ( )
elif oooo == 8002 :
 iiI1iiIIiii ( )
elif oooo == 8003 :
 ooOooo0 ( )
elif oooo == 8004 :
 iI1iIIIi1i ( )
elif oooo == 8005 :
 OOOoO000 ( )
elif oooo == 8006 :
 oOOOoo ( ooo0O , i1Ii )
elif oooo == 8030 :
 III1Iiii1I11 ( i1Ii )
elif oooo == 8045 :
 o0oooOO00 ( )
elif oooo == 8046 :
 iiIiii1IIIII ( i1Ii )
elif oooo == 8047 :
 iiIiIIIiiI ( i1Ii )
elif oooo == 8040 :
 oOoO00O0 ( )
elif oooo == 8041 :
 OO ( i1Ii )
elif oooo == 8042 :
 ii ( i1Ii )
elif oooo == 8043 :
 yt . PlayVideo ( i1Ii )
elif oooo == 8044 :
 o0ooooO0o0O ( i1Ii )
elif oooo == 8060 :
 ooOoOo0 ( )
elif oooo == 8061 :
 ooo00Ooo ( i1Ii )
elif oooo == 8070 :
 I1i1i1 ( )
elif oooo == 8071 :
 OoO0O00O0oo0O ( i1Ii )
elif oooo == 8081 :
 oo00O00oO000o ( )
elif oooo == 8062 :
 I1iii11 ( i1Ii )
elif oooo == 8063 :
 Oo0ooo ( i1Ii )
elif oooo == 8050 :
 I11I ( )
elif oooo == 8051 :
 I11iIi1i1II11 ( i1Ii )
elif oooo == 8052 :
 ooo ( i1Ii )
elif oooo == 8085 :
 i11III1111iIi ( )
elif oooo == 8086 :
 OOOOoOOo0O0 ( i1Ii )
elif oooo == 8087 :
 OooO0OO ( i1Ii )
elif oooo == 8088 :
 o0OOo0o0O0O ( i1Ii , ooo0O )
elif oooo == 9000 :
 Ii11Ii1I ( )
elif oooo == 1111 :
 oo00ooOoo ( )
elif oooo == 9001 :
 o000oo ( )
elif oooo == 9002 :
 I1II ( )
elif oooo == 9003 :
 oo0oOoo ( )
elif oooo == 50 :
 O0oo00o0O ( i1Ii )
elif oooo == 9020 :
 o0OOoo0OO0OOO ( )
elif oooo == 9021 :
 I1IIOO0 ( )
elif oooo == 9022 :
 OOO0oOOo00O ( )
elif oooo == 9023 :
 OO0oIII111i11IiI ( )
elif oooo == 9024 :
 II1I1iiIII1I1 ( i1Ii )
elif oooo == 9030 :
 OOooO ( i1Ii )
elif oooo == 9031 :
 O00O0OO00oo ( i1Ii )
elif oooo == 9032 :
 oOOO ( i1Ii )
elif oooo == 9033 :
 ooo0oooo0 ( i1Ii )
 if 58 - 58: O0
 if 91 - 91: oO0o0ooO0 / ii11ii1ii . oO0o0ooO0 - OOooOOo + ii11ii1ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
