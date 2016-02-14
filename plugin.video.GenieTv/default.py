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
iIii1 = "2.3.5"
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
 O0O00o0OOO0 ( '[COLORgreen]M3U STREAMS[/COLOR]' , II , 8070 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]GenieTv VOD[/COLOR]' , II , 1005 , OOooO0OOoo + 'vod.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]POPCORN BOX[/COLOR]' , II , 7061 , OOooO0OOoo + 'popcorn.png' , ii11iIi1I , '' )
 if 19 - 19: o0000oOoOoO0o + o0oO0
 O0O00o0OOO0 ( '[COLORgreen]RECENT EPISODES[/COLOR]' , II , 8081 , OOooO0OOoo + 'recent.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ANIME[/COLOR]' , II , 1001 , OOooO0OOoo + 'anime.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CLASSIC TOONS[/COLOR]' , II , 8050 , OOooO0OOoo + 'classictoons.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CHAMPION IPTV[/COLOR]' , II , 9020 , OOooO0OOoo + 'UKiptvandvod.png' , ii11iIi1I , 'UK IPTV AND HD VOD' )
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , II , 1023 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) ) , 1016 , OOooO0OOoo + 'reap.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , II , 8040 , OOooO0OOoo + 'documentary.png' , ii11iIi1I , '' )
 if 53 - 53: OoooooooOO . i1IIi
 O0O00o0OOO0 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , II , 3000 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 18 - 18: OOooOOo
 if 28 - 28: OoOO0ooOOoo0O - IIII . IIII + I1IiI - OoooooooOO + O0
 if 95 - 95: Ooo00oOo00o % OoOO . O0
 if 15 - 15: o0oO0 / o00O0oo . o00O0oo - i1IIi
 if 53 - 53: IIII + OOOo0 * OoOO
 if 61 - 61: i1IIi * OoOO0ooOOoo0O / OoooooooOO . i11iIiiIii . I1IiI
 if 60 - 60: o0000oOoOoO0o / o0000oOoOoO0o
 if 46 - 46: o00O0oo * OoOO0ooOOoo0O - Ooo00oOo00o * OoOO - O0oO
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 83 - 83: OoooooooOO
 if 31 - 31: OoOoOO00 - OoOO0ooOOoo0O . O0oO % I1IiI - O0
 if 4 - 4: OoOoOO00 / o0oO0 . oO0o0ooO0
 if 58 - 58: OoOO0ooOOoo0O * i11iIiiIii / I1IiI % O0oO - ii11ii1ii / OoOO
def ii11i1 ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , II , 1024 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 if 29 - 29: ii11ii1ii % OOOo0 + o0oO0 / OOooOOo + OoOO0ooOOoo0O * OOooOOo
def i1I1iI ( ) :
 O0O00o0OOO0 ( '[COLORgreen]Live Tv[/COLOR]' , II , 9021 , OOooO0OOoo + 'english.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]XXX[/COLOR]' , II , 9022 , OOooO0OOoo + 'xxx.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]Hd VOD[/COLOR]' , II , 9023 , OOooO0OOoo + 'vod(1).png' , ii11iIi1I , '' )
 if 93 - 93: iIii1I11I1II1 % OoOO * i1IIi
 if 16 - 16: O0 - O0oO * iIii1I11I1II1 + oO0o0ooO0
def Ii11iII1 ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , II , 9001 , OOooO0OOoo + 'MOVIESv.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , II , 9002 , OOooO0OOoo + 'TVSHOWSv.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , II , 9003 , OOooO0OOoo + 'livetv.png' , ii11iIi1I , '' )
 if 51 - 51: OoOoOO00 * Ooo00oOo00o % OOooOOo * OoOoOO00 % ii11ii1ii / o0oO0
def iIIIIii1 ( ) :
 O0O00o0OOO0 ( '[COLORgreen]RADIO[/COLOR]' , II , 1013 , OOooO0OOoo + 'radio.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC[/COLOR]' , II , 1030 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , II + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , II , 1111 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 if 58 - 58: i11iIiiIii % o0000oOoOoO0o
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 71 - 71: OoOO0ooOOoo0O + o0oO0 % i11iIiiIii + ii11ii1ii - IIII
def oO0OOoO0 ( ) :
 I111Ii111 ( 'DELETE CACHE' , 'url' , 14 , OOooO0OOoo + 'MAIN5.png' , ii11iIi1I , '' )
 I111Ii111 ( 'DELETE PACKAGES' , 'url' , 6 , OOooO0OOoo + 'MAIN4.png' , ii11iIi1I , '' )
 I111Ii111 ( 'FORCE REFRESH' , 'url' , 10 , OOooO0OOoo + 'MAIN3.png' , ii11iIi1I , 'Force Refresh All Repos' )
 if 4 - 4: OoOO
 I111Ii111 ( 'CHECK MY IP' , 'url' , 12 , OOooO0OOoo + 'MAIN2.png' , ii11iIi1I , '' )
 I111Ii111 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , OOooO0OOoo + 'MAIN1.png' , ii11iIi1I , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0O00o0OOO0 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , II , 4 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]URL FIXES[/COLOR]' , II , 20 , OOooO0OOoo + 'URLFIX.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 93 - 93: Ooo00oOo00o % OoOO . Ooo00oOo00o * O0oO % o00O0oo . OoOoOO00
 if 38 - 38: OOooOOo
def Oo0O ( ) :
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
 if 25 - 25: I1IiI . OoOoOO00 / oO0o0ooO0 . OoOO0ooOOoo0O * Ooo00oOo00o . OOOo0
 if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
def Oo0OoO00oOO0o ( ) :
 I111Ii111 ( 'CHECK ADVANCED XML' , II , 8 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 I111Ii111 ( 'MUCKYS XML' , II + '/wizard/muckys.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 I111Ii111 ( '0CACHE XML' , II + '/wizard/0cache.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 I111Ii111 ( 'MIKEY1234 XML' , II + '/wizard/mikey.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 I111Ii111 ( 'TUXENS XML' , II + '/wizard/tuxens.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 I111Ii111 ( 'P2P RECOMMENDED XML1' , II + '/wizard/p2p1.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 I111Ii111 ( 'P2P RECOMMENDED XML2' , II + '/wizard/p2p2.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 I111Ii111 ( 'DELETE XML' , II , 11 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 80 - 80: OoOO + OoOO0ooOOoo0O - OoOO0ooOOoo0O % oO0o0ooO0
def OoOO0oo0o ( ) :
 I111Ii111 ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 I111Ii111 ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 if 14 - 14: OOooOOo * oO0o0ooO0 * oO0o0ooO0 / I1IiI
def Oo0o00 ( ) :
 I111Ii111 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , II + '/wizard/customftv/ftvguide-addons.zip' , 5 , OOooO0OOoo + 'FTV4.png' , ii11iIi1I , '' )
 I111Ii111 ( 'FTV GUIDE FIRST RUN SETTINGS' , II + '/wizard/customftv/settings.xml' , 17 , OOooO0OOoo + 'FTV3.png' , ii11iIi1I , '' )
 I111Ii111 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , OOooO0OOoo + 'FTV1.png' , ii11iIi1I , '' )
 I111Ii111 ( 'RESET FTV DATABASE' , 'url' , 18 , OOooO0OOoo + 'FTV2.png' , ii11iIi1I , '' )
 if 73 - 73: oO0o0ooO0 * o00O0oo + OOooOOo . OoOO0ooOOoo0O + ii11ii1ii % oO0o0ooO0
 if 95 - 95: i1IIi
 if 3 - 3: O0oO - O0 / O0oO % Ooo00oOo00o / O0oO . OOOo0
def iiI111I1iIiI ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SKINS[/COLOR]' , II , 33 , OOooO0OOoo + 'skinp.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , II , 34 , OOooO0OOoo + 'artp.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , i1iIIi1 , 35 , OOooO0OOoo + 'GUI.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 41 - 41: Oo . o0oO0 + O0 * OOooOOo % Oo * Oo
def iIIIIi1iiIi1 ( url ) :
 iii1i1iiiiIi = Iiii ( OO0OoO0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 5 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 77 - 77: oO0o0ooO0 % oO0o0ooO0 * OoOO - i11iIiiIii
def Oo0oO ( ) :
 O0O00o0OOO0 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , II , 36 , OOooO0OOoo + 'GSKIN.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]HELIX SKINS[/COLOR]' , II , 37 , OOooO0OOoo + 'HSKIN.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , i1iIIi1 , 38 , OOooO0OOoo + 'ISKIN.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 1 - 1: Ooo00oOo00o - OoOO . o0000oOoOoO0o . Ooo00oOo00o / Oo + o0000oOoOoO0o
def OooOOOOo ( url ) :
 iii1i1iiiiIi = Iiii ( II + oo0O0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 60 - 60: OOOo0
def iii1i ( url ) :
 iii1i1iiiiIi = Iiii ( II + I11i1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 87 - 87: o0000oOoOoO0o - iIii1I11I1II1 + OOOo0 . oO0o0ooO0
def Oo0oOOOoOooOo ( url ) :
 iii1i1iiiiIi = Iiii ( II + O000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 20 - 20: OoOO0ooOOoo0O % o00O0oo / o00O0oo + o00O0oo
def III1IiiI ( url ) :
 iii1i1iiiiIi = Iiii ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 31 - 31: OOooOOo . OOOo0
def ii11IIII11I ( url ) :
 iii1i1iiiiIi = Iiii ( II + OOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 40 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 90 - 90: OOooOOo % i1IIi / Ooo00oOo00o
def IIi ( url ) :
 iii1i1iiiiIi = Iiii ( II + i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 5 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 91 - 91: ii11ii1ii + OOOo0 . OoOO0ooOOoo0O * ii11ii1ii + OOOo0 * Oo
def O000OOOOOo ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , oo000o , 2031 , OOooO0OOoo + 'APK.png' )
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 91 - 91: OOooOOo . iIii1I11I1II1 / OoOO + i1IIi
def I1i ( url ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOooooO0Oo = os . path . join ( oOo00O0oo00o0 , oOOOo00O00oOo + '.mp4' )
 try :
  os . remove ( OOooooO0Oo )
 except :
  pass
 downloader . download ( url , OOooooO0Oo , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 99 - 99: o00O0oo / Oo / IIII % OOOo0
 if 13 - 13: o0000oOoOoO0o * Oo * o0oO0
def iI11iI1IiiIiI ( url ) :
 iii1i1iiiiIi = Iiii ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 5 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 try :
  iii1i1iiiiIi = Iiii ( Ii1I1i + oooOOOOO + OOI1iI1ii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
  for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
   O0O00o0OOO0 ( oOOOo00O00oOo , url , 5 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 except : pass
 o0oo0o0O00OO ( 'movies' , 'INFO' )
 if 57 - 57: O0oO % o00O0oo + OOooOOo - Oo
 if 65 - 65: o0000oOoOoO0o . I1IiI
def IiI1i ( url ) :
 iii1i1iiiiIi = Iiii ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 43 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 try :
  iii1i1iiiiIi = Iiii ( Ii1I1i + oooOOOOO + OOI1iI1ii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
  for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
   O0O00o0OOO0 ( oOOOo00O00oOo , url , 43 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 except : pass
 o0oo0o0O00OO ( 'movies' , 'INFO' )
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
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
 oO00oooOOoOo0 ( )
 if 86 - 86: iIii1I11I1II1 / I1IiI . OoOoOO00
def II1i111Ii1i ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 ooOO0O0ooOooO = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , oo000o in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , oo000o , 222 , OOooO0OOoo + 'radio.png' )
  if 96 - 96: i11iIiiIii % OoOO0ooOOoo0O
def ooO ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , 'http://www.toonjet.com/' + oo000o , 8051 , OOooO0OOoo + 'classictoons.png' )
def Ooo0oOooo0 ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI in ooOO0O0ooOooO :
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
 ooOO0O0ooOooO = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  iii1 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , OOooO0OOoo + 'classictoons.png' )
  if 47 - 47: Oo % o0000oOoOoO0o % i11iIiiIii - O0 + o0oO0
def ooO000OO0O00O ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 ooOO0O0ooOooO = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , oo000o , 8046 , OOooO0OOoo + 'documentary.png' )
def OOOoOO0o ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  iii1 ( ( oOOOo00O00oOo ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8046 , OOooO0OOoo + 'documentary.png' )
  if 1 - 1: OoOoOO00
def O0oOo00o ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  yt . PlayVideo ( url )
  if 81 - 81: IIII % i1IIi . iIii1I11I1II1
def Ii1Iii1iIi ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , oo000o , 8041 , OOooO0OOoo + 'documentary.png' )
def OO0oo ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo , iiIiIIIiiI in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( oOOOo00O00oOo ) . replace ( '&#039;s' , '' ) , url , 8042 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8041 , OOooO0OOoo + 'documentary.png' )
  if 15 - 15: OOOo0 / O0oO . O0oO * OoOO
  if 43 - 43: O0oO * o00O0oo % OOOo0
def i1I1i1 ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , iiIiIIIiiI , url , O0OoooO0 in ooOO0O0ooOooO :
  iii1 ( ( oOOOo00O00oOo ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iiIiIIIiiI )
 for url in oOOOoo00 :
  ooo0O0o00O ( ( url ) . replace ( '//' , 'http://' ) )
  if 48 - 48: o0oO0 / O0oO . iIii1I11I1II1 * I1IiI * OoOO / i1IIi
def ooo0O0o00O ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  iii1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOooO0OOoo + 'documentary.png' )
  if 92 - 92: Oo % Oo - OOooOOo / I1IiI
def I11IIIi ( ) :
 iIIiiI1II1i11 = OO ( 'http://www.stream2watch.co/live-tv' )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for oo000o , iiIiIIIiiI , oOOOo00O00oOo , o0o0 in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( oOOOo00O00oOo + '[COLORgreen]' + o0o0 + '[/COLOR]' ) , oo000o , 8086 , iiIiIIIiiI )
  if 49 - 49: OoOO - i11iIiiIii . O0oO * o00O0oo % oO0o0ooO0 + i1IIi
def oOO0OOOo ( url ) :
 iIIiiI1II1i11 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , url , 8087 , iiIiIIIiiI )
  if 56 - 56: OOooOOo
def I1 ( url ) :
 iIIiiI1II1i11 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  OooooO0oOOOO ( url , oOOOo00O00oOo )
  if 100 - 100: oO0o0ooO0 % OoOO0ooOOoo0O
def OooooO0oOOOO ( url , name ) :
 iIIiiI1II1i11 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url in ooOO0O0ooOooO :
  print url
  iii1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 86 - 86: Oo . O0 - OoooooooOO . Ooo00oOo00o + o00O0oo
def OOo ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 ooOO0O0ooOooO = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , IIii11Ii1i1I , Oooo0O , oo00O0oO0O0 , oo000o in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( time + '[COLORgreen]' + oo00O0oO0O0 + '[/COLOR]' + Oooo0O ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , oo000o , 8061 , iiIiIIIiiI )
def ooo0OO0O0Oo ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  iii1 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , OOooO0OOoo + 'documentary.png' )
  if 62 - 62: O0 % o0000oOoOoO0o . o0000oOoOoO0o - iIii1I11I1II1 / i11iIiiIii
def iiiII ( ) :
 iIIiiI1II1i11 = Iiii ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 ooOO0O0ooOooO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( iIIiiI1II1i11 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( oOOOo00O00oOo ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oo000o , 8071 , OOooO0OOoo + 'streams.png' )
def iiIiIi ( url ) :
 iIIiiI1II1i11 = OO ( url )
 ooOO0O0ooOooO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for oOOOo00O00oOo , url in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , ( url ) . strip ( ) , 404 , OOooO0OOoo + 'streams.png' )
  if 39 - 39: O0oO
def OoOooOoO ( url ) :
 iiIiii1iI1i = urllib2 . Request ( url )
 iiIiii1iI1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1ii1ii11i1I = ''
 iii1i1iiiiIi = ''
 try :
  I1ii1ii11i1I = urllib2 . urlopen ( iiIiii1iI1i )
  iii1i1iiiiIi = I1ii1ii11i1I . read ( )
  I1ii1ii11i1I . close ( )
 except : pass
 if iii1i1iiiiIi != '' :
  return iii1i1iiiiIi
 else :
  iii1i1iiiiIi = 'Failed'
  return iii1i1iiiiIi
  if 58 - 58: oO0o0ooO0 + Oo
def II1I1I1Ii ( ) :
 OOOOoO00o0O = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1I1I1IIi1III = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiiIII = I1I1I1IIi1III . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 o0OOOo = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 ii1iiIiIII1ii = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oO0o0oooO0oO = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 IiIiII1 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 Iii1iiIi1II = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO0O00oOo = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1I1I1IIi1III
 ii1II = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( I1I1I1IIi1III ) . replace ( ' ' , '+' )
 if 14 - 14: OoOO / OoOO % o0oO0
 iIIiiI1II1i11 = OoOooOoO ( oo000o )
 ooOii = OoOooOoO ( o0OOOo )
 OO0O0Ooo = OoOooOoO ( ii1iiIiIII1ii )
 oOoO0 = OoOooOoO ( oO0o0oooO0oO )
 Oo0 = OoOooOoO ( IiIiII1 )
 oo0O0o00o0O = OoOooOoO ( OO0O00oOo )
 I11i1II = Iiii ( ii1II )
 if 72 - 72: iIii1I11I1II1 . i1IIi / Oo . OoOoOO00
 if iIIiiI1II1i11 != 'Failed' :
  ooOO0O0ooOooO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
  for ooo000o000 , oOOOo00O00oOo in ooOO0O0ooOooO :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    iii1 ( ( oOOOo00O00oOo + '[COLORgreen] source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oo000o + ooo000o000 ) , 222 , '' )
 if ooOii != 'Failed' :
  oOOOoo00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( ooOii )
  for ooo000o000 , oOOOo00O00oOo in oOOOoo00 :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    iii1 ( ( oOOOo00O00oOo + '[COLORgreen] source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0OOOo + ooo000o000 ) , 222 , '' )
 if OO0O0Ooo != 'Failed' :
  O0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OO0O0Ooo )
  for ooo000o000 , oOOOo00O00oOo in O0o :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    iii1 ( ( oOOOo00O00oOo + '[COLORgreen] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ii1iiIiIII1ii + ooo000o000 ) , 222 , '' )
 if oOoO0 != 'Failed' :
  O0OOoOOO0oO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oOoO0 )
  for ooo000o000 , oOOOo00O00oOo in O0OOoOOO0oO :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    iii1 ( ( oOOOo00O00oOo + '[COLORgreen] source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oO0o0oooO0oO + ooo000o000 ) , 222 , '' )
 if Oo0 != 'Failed' :
  I1ii11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oo0 )
  for ooo000o000 , iiIiIIIiiI , oOOOo00O00oOo in I1ii11 :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + '[COLORgreen] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( ooo000o000 ) , 1006 , 'img' )
    if 74 - 74: Oo - OOooOOo . i1IIi
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if oo0O0o00o0O != 'Failed' :
  i1III = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oo0O0o00o0O )
  for ooo000o000 , iiIiIIIiiI , oOOOo00O00oOo in i1III :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOOo00O00oOo + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oo000o , 7067 , iiIiIIIiiI )
    if 49 - 49: i11iIiiIii % o00O0oo . I1IiI
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if I11i1II != 'Failed' :
  Ii1i1iI = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( I11i1II )
  for oo000o , iiIiIIIiiI , oOOOo00O00oOo in Ii1i1iI :
   iii1 ( oOOOo00O00oOo + ' - Source 7' , oo000o , 222 , iiIiIIIiiI )
 IIiI1 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 17 - 17: OoOO0ooOOoo0O / OoOO0ooOOoo0O / o0000oOoOoO0o
 if 1 - 1: i1IIi . i11iIiiIii % OoOO0ooOOoo0O
 for OooO0oo in IIiI1 :
  o0o0oOoOO0O = OOOOoO00o0O + OooO0oo
  i1ii1II1ii = OoOooOoO ( o0o0oOoOO0O )
  if Oo0 != 'Failed' :
   iII111Ii = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( i1ii1II1ii )
   for ooo000o000 , oOOOo00O00oOo in iII111Ii :
    if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
     iii1 ( ( oOOOo00O00oOo + '[COLORgreen] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OOOOoO00o0O + OooO0oo + ooo000o000 ) , 222 , '' )
     if 52 - 52: OoOoOO00 % IIII . I1IiI * iIii1I11I1II1
     o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
     if 50 - 50: o0oO0 - O0oO * IIII . ii11ii1ii
     if 37 - 37: o0oO0 % i11iIiiIii % OoOoOO00 . O0 . o00O0oo
def OO0oOOoo ( ) :
 if 52 - 52: OOooOOo % Oo
 I1I1I1IIi1III = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiiIII = I1I1I1IIi1III . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 o0OOOo = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 ii1iiIiIII1ii = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 oO0o0oooO0oO = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 IiIiII1 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1I1I1IIi1III ) . replace ( ' ' , '+' )
 Iii1iiIi1II = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 ii1II = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( I1I1I1IIi1III ) . replace ( ' ' , '+' )
 if 64 - 64: O0 % o0000oOoOoO0o % O0 * Ooo00oOo00o . OoOO + OOOo0
 iIIiiI1II1i11 = OoOooOoO ( oo000o )
 ooOii = OoOooOoO ( o0OOOo )
 OO0O0Ooo = OoOooOoO ( ii1iiIiIII1ii )
 oOoO0 = OoOooOoO ( oO0o0oooO0oO )
 Oo0 = cloudflare . source ( IiIiII1 )
 i1ii1II1ii = OoOooOoO ( Iii1iiIi1II )
 I11i1II = Iiii ( ii1II )
 if iIIiiI1II1i11 != 'Failed' :
  ooOO0O0ooOooO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiiI1II1i11 )
  for oOOOo00O00oOo in ooOO0O0ooOooO :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oOOOo00O00oOo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 75 - 75: o0000oOoOoO0o . OoooooooOO % OOooOOo * o0000oOoOoO0o % OoooooooOO
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if ooOii != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooOii )
  for oOOOo00O00oOo in oOOOoo00 :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OOOo + oOOOo00O00oOo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 13 - 13: IIII / i11iIiiIii % OoOoOO00 % o0000oOoOoO0o . ii11ii1ii
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OO0O0Ooo != 'Failed' :
  O0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0O0Ooo )
  for oOOOo00O00oOo in oOOOoo00 :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ii1iiIiIII1ii + oOOOo00O00oOo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 8 - 8: I1IiI + Oo - OoOoOO00
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if oOoO0 != 'Failed' :
  O0OOoOOO0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOoO0 )
  for oOOOo00O00oOo in oOOOoo00 :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oO0o0oooO0oO + oOOOo00O00oOo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 11 - 11: i1IIi % i11iIiiIii - i1IIi * I1IiI
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if Oo0 != 'Failed' :
  I1ii11 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( Oo0 )
  for oo000o , iiIiIIIiiI , oOOOo00O00oOo in I1ii11 :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( oOOOo00O00oOo + ' - Source - Dizi' , oo000o , 8062 , iiIiIIIiiI )
    if 39 - 39: O0oO
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if i1ii1II1ii != 'Failed' :
  iII111Ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1ii1II1ii )
  for oo000o , iiIiIIIiiI , oOOOo00O00oOo in iII111Ii :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    iii1 ( ( oOOOo00O00oOo + '[COLORgreen] source Scooby[/COLOR]' ) , oo000o , 222 , 'img' )
    if 86 - 86: o0000oOoOoO0o * OOOo0 + o0000oOoOoO0o + OoOoOO00
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if I11i1II != 'Failed' :
  Ii1i1iI = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( I11i1II )
  for oo000o , iiIiIIIiiI , oOOOo00O00oOo in Ii1i1iI :
   iii1 ( oOOOo00O00oOo + ' - Source 7' , oo000o , 222 , iiIiIIIiiI )
def i1i111iI ( ) :
 if 29 - 29: ii11ii1ii / i1IIi . OOOo0 - I1IiI - I1IiI - o00O0oo
 I1I1I1IIi1III = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiiIII = I1I1I1IIi1III . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iIIiiI1II1i11 = Iiii ( oo000o )
 ooOO0O0ooOooO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for oOOOo00O00oOo , iiIiIIIiiI , IiiIiI111iI in ooOO0O0ooOooO :
  OOoi1i11I1I1iii1 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
   o0OoOO000ooO0 ( oOOOo00O00oOo , '' , 7022 , OOoi1i11I1I1iii1 )
   if 8 - 8: o0oO0 + OoOoOO00 / oO0o0ooO0 / o0000oOoOoO0o
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: O0 / i1IIi
 if 78 - 78: OoooooooOO . Ooo00oOo00o + o0oO0 - i1IIi
def ii1 ( url ) :
 O0iII1 = cloudflare . source ( url )
 ooOO0O0ooOooO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( O0iII1 )
 for url , IIII1i , Ii1IIIIi1ii1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( IIII1i ) . replace ( 'Sezon' , ' Season ' ) + ( Ii1IIIIi1ii1I ) . replace ( 'Bölüm' , ' Episode ' ) + oOOOo00O00oOo , url , 8063 , '' )
  if 13 - 13: OOOo0 % I1IiI . ii11ii1ii / Oo % OoOO0ooOOoo0O . OoooooooOO
  if 22 - 22: IIII / i11iIiiIii
  if 62 - 62: Ooo00oOo00o / ii11ii1ii
  if 7 - 7: OoooooooOO . IIII
def O000OOO0OOo ( url ) :
 O0iII1 = cloudflare . source ( url )
 ooOO0O0ooOooO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( O0iII1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , url , 222 , '' )
  if 32 - 32: o00O0oo * O0
  if 100 - 100: o0oO0 % iIii1I11I1II1 * OoOoOO00 - oO0o0ooO0
  if 92 - 92: o0oO0
  if 22 - 22: Oo % oO0o0ooO0 * ii11ii1ii / OoOO0ooOOoo0O % i11iIiiIii * o0000oOoOoO0o
def Oo00OoOo ( ) :
 if 24 - 24: i11iIiiIii - O0oO
 O0iII1 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 ooOO0O0ooOooO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O0iII1 )
 for oo000o , iiIiIIIiiI , oOOOo00O00oOo , Ii1IIIIi1ii1I in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo + '  -  ' + ( Ii1IIIIi1ii1I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oo000o , 8063 , iiIiIIIiiI )
  if 21 - 21: o0000oOoOoO0o
def OoO00 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo , iiIiIIIiiI in ooOO0O0ooOooO :
  iii1 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , oo000o , 8002 , iiIiIIIiiI )
def OO0Ooooo000Oo ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , url , oOOOo00O00oOo , O0OoooO0 in ooOO0O0ooOooO :
  O0O00o0OOO0 ( '%s %s' % ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , time ) , url , 1015 , iiIiIIIiiI , O0OoooO0 )
  if 97 - 97: o00O0oo * ii11ii1ii / OOOo0 / iIii1I11I1II1 % o0000oOoOoO0o
def O00oO0 ( ) :
 if 97 - 97: O0oO - iIii1I11I1II1
 o0OoOO000ooO0 ( 'Coronation Street' , '' , 8001 , '' )
 o0OoOO000ooO0 ( 'Eastenders' , '' , 8002 , '' )
 o0OoOO000ooO0 ( 'Emmerdale' , '' , 8003 , '' )
 o0OoOO000ooO0 ( 'Hollyoaks' , '' , 8004 , '' )
 o0OoOO000ooO0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 75 - 75: OoooooooOO * IIII
 if 9 - 9: IIII - OoOoOO00 + O0 / iIii1I11I1II1 / i11iIiiIii
 if 39 - 39: IIII * Oo + iIii1I11I1II1 - IIII + OoOO0ooOOoo0O
 if 69 - 69: O0
def o0ooO ( ) :
 iIIiiI1II1i11 = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  if 'Holly' in oOOOo00O00oOo :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oo000o :
    iii1 ( ( oOOOo00O00oOo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 74 - 74: O0 * OoOO - i11iIiiIii + O0oO
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / o0000oOoOoO0o % OoOoOO00 % i1IIi / i11iIiiIii
def OOO ( ) :
 iIIiiI1II1i11 = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  if 'East' in oOOOo00O00oOo :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOOo00O00oOo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 30 - 30: OoooooooOO - OoooooooOO . O0 / oO0o0ooO0
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: OoOO0ooOOoo0O + OOooOOo . OoooooooOO
def ooOooo0 ( ) :
 iIIiiI1II1i11 = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  if 'Emmer' in oOOOo00O00oOo :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOOo00O00oOo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 67 - 67: OOOo0
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: ii11ii1ii - oO0o0ooO0 * OOooOOo + I1IiI * I1IiI * O0
def O000Oo0o ( ) :
 iIIiiI1II1i11 = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  if 'Coro' in oOOOo00O00oOo :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOOo00O00oOo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 99 - 99: iIii1I11I1II1 % o0oO0 + o0oO0 + oO0o0ooO0 - O0oO / O0oO
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: OOOo0 + I1IiI / IIII
def OOOoO000 ( ) :
 iIIiiI1II1i11 = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  if 'Celeb' in oOOOo00O00oOo :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOOo00O00oOo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 57 - 57: OoOoOO00
def oOOOoo ( name , url ) :
 Ii1ii111i1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Ii1ii111i1 :
  i1i1i1I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  Iiii1i1 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( Iiii1i1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  Iiii1i1 = open_url ( url )
  oOoo000 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( Iiii1i1 ) [ - 1 ]
  i1i1i1I = oOoo000 . replace ( '\\/' , '/' )
 OooOo00o = xbmcgui . ListItem ( name , '' , '' )
 OooOo00o . setPath ( i1i1i1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OooOo00o )
 if 20 - 20: i1IIi * O0oO + OoOoOO00 % OOooOOo % OoOO
 if 13 - 13: Oo
def oOOo000oOoO0 ( ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 ooOO0O0ooOooO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oo000o , 7071 , OOooO0OOoo + 'popcorn.png' )
 for oo000o , oOOOo00O00oOo in oOOOoo00 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oo000o , 7071 , OOooO0OOoo + 'popcorn.png' )
  if 86 - 86: OoOoOO00 % i11iIiiIii + o00O0oo % i11iIiiIii
def Ooo0o0OOO ( ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 ooOO0O0ooOooO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  if 'Movies' in oOOOo00O00oOo :
   o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , 'http://www.snagfilms.com' + oo000o , 7061 , OOooO0OOoo + 'popcorn.png' )
def i11IiII ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , 'http://www.snagfilms.com' + url , 7067 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOooO0OOoo + 'popcorn.png' )
  if 85 - 85: OoOO - iIii1I11I1II1 / O0
  if 99 - 99: OoOoOO00 * IIII % iIii1I11I1II1 / o00O0oo
def OOO00O0oOOo ( url ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 ooOO0O0ooOooO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , 'http://www.snagfilms.com' + url , 7062 , iiIiIIIiiI )
  if 71 - 71: o0000oOoOoO0o / OOooOOo / O0oO % OoOO0ooOOoo0O
  if 51 - 51: IIII * O0 / OoOoOO00 . o00O0oo % OoOO0ooOOoo0O / OOOo0
def ii1iii1I1I ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , iiIiIIIiiI )
  if 95 - 95: IIII
def Ooo0oo ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  IIi11IIiIii1 ( 'http://www.snagfilms.com' + url )
  if 17 - 17: o00O0oo + OoOO . Ooo00oOo00o - Oo * i11iIiiIii
def IIi11IIiIii1 ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  iii1 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , url , 222 , OOooO0OOoo + 'popcorn' )
  if 20 - 20: OOOo0 . OoooooooOO % OoOO0ooOOoo0O
  if 63 - 63: OOOo0 % iIii1I11I1II1
  if 39 - 39: oO0o0ooO0 / OoOoOO00 / ii11ii1ii % OOOo0
  if 89 - 89: O0oO + OoooooooOO + O0oO * i1IIi + iIii1I11I1II1 % o0000oOoOoO0o
def oOo0oO ( ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 ooOO0O0ooOooO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo , iiIiIIIiiI in ooOO0O0ooOooO :
  iii1 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( oo000o ) ) , 222 , iiIiIIIiiI )
  if 5 - 5: OoOO0ooOOoo0O - OoOO0ooOOoo0O . Oo + I1IiI - OoOO0ooOOoo0O . OoOO
def IiIi1i1ii ( ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 ooOO0O0ooOooO = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , oo000o in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + oo000o , 7051 , OOooO0OOoo + 'vod.png' )
  if 11 - 11: OoOoOO00 / OOooOOo
def IiIi1 ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , OOooO0OOoo + 'vod.png' )
  if 34 - 34: OoOO0ooOOoo0O
def OooO0ooo0o ( url ) :
 Iiii1i1 = Iiii
 ooOO0O0ooOooO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , url , 222 , iiIiIIIiiI )
  if 47 - 47: OoooooooOO
  if 4 - 4: OOOo0 % o0000oOoOoO0o
  if 10 - 10: IIII . OoooooooOO - Ooo00oOo00o + IIII - O0
  if 82 - 82: o0oO0 + OoOoOO00
  if 39 - 39: OoOO % iIii1I11I1II1 % O0 % OoooooooOO * ii11ii1ii + oO0o0ooO0
def oOo000 ( ) :
 if 14 - 14: Ooo00oOo00o . OoOoOO00 . o0000oOoOoO0o / o00O0oo % ii11ii1ii - o0oO0
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
 if 67 - 67: o0000oOoOoO0o - OoOO0ooOOoo0O . i1IIi
 if 35 - 35: oO0o0ooO0 + o0oO0 - OoOO . oO0o0ooO0 . IIII
def oo0ooOO ( Cat_Name ) :
 if 24 - 24: Ooo00oOo00o % Ooo00oOo00o * iIii1I11I1II1
 III = False
 iIiIi11Ii = '0'
 if Cat_Name == 'All Channels' : III = True
 if Cat_Name == 'Entertainment' : iIiIi11Ii = '1'
 if Cat_Name == 'Movies' : iIiIi11Ii = '2'
 if Cat_Name == 'Music' : iIiIi11Ii = '3'
 if Cat_Name == 'News' : iIiIi11Ii = '4'
 if Cat_Name == 'Sports' : iIiIi11Ii = '5'
 if Cat_Name == 'Documentary' : iIiIi11Ii = '6'
 if Cat_Name == 'Kids' : iIiIi11Ii = '7'
 if Cat_Name == 'Food' : iIiIi11Ii = '8'
 if Cat_Name == 'Religious' : iIiIi11Ii = '9'
 if Cat_Name == 'USA Channels' : iIiIi11Ii = '10'
 if Cat_Name == 'Other' : iIiIi11Ii = '11'
 if 23 - 23: OoOO - OoOO0ooOOoo0O + o0000oOoOoO0o
 Iiii1i1 = Iiii ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 ooOO0O0ooOooO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( Iiii1i1 )
 print 'Len Match: >>>' + str ( len ( ooOO0O0ooOooO ) )
 for oOOOo00O00oOo , iiIiIIIiiI , IiiIiI111iI in ooOO0O0ooOooO :
  OOoi1i11I1I1iii1 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if IiiIiI111iI == iIiIi11Ii :
   o0OoOO000ooO0 ( oOOOo00O00oOo , '' , 7022 , OOoi1i11I1I1iii1 )
  elif III == True :
   o0OoOO000ooO0 ( oOOOo00O00oOo , '' , 7022 , OOoi1i11I1I1iii1 )
  else : pass
  if 12 - 12: OOOo0 / o0oO0 % OOooOOo / i11iIiiIii % OoooooooOO
  xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo * o00O0oo + o0000oOoOoO0o
def i1I1II1iIIi11 ( Search_Name ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 ooOO0O0ooOooO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 ooOO0O0ooOooO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , oo000o , o0OOOo , ii1iiIiIII1ii in ooOO0O0ooOooO :
  OOoi1i11I1I1iii1 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  iii1 ( Search_Name + ': Link 1' , ( oo000o ) . replace ( '\\' , '' ) , 222 , OOoi1i11I1I1iii1 )
  iii1 ( Search_Name + ': Link 2' , ( o0OOOo ) . replace ( '\\' , '' ) , 222 , OOoi1i11I1I1iii1 )
  iii1 ( Search_Name + ': Link 3' , ( ii1iiIiIII1ii ) . replace ( '\\' , '' ) , 222 , OOoi1i11I1I1iii1 )
  if 49 - 49: OoooooooOO * o0000oOoOoO0o - Oo . OoOO
def O000o0 ( ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 ooOO0O0ooOooO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , oo000o in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOooO0OOoo + 'english.png' )
def oO0 ( ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 ooOO0O0ooOooO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , oo000o in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'xxx.png' )
def o000OoOoO0 ( ) :
 Iiii1i1 = Iiii ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 ooOO0O0ooOooO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , oo000o in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'vod(1).png' )
  if 99 - 99: OOooOOo * OOOo0 % Oo . I1IiI
def O00o00O ( url ) :
 url
 ii1iii11i1 = xbmcgui . ListItem ( oOOOo00O00oOo , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1iii11i1 )
 return
 if 4 - 4: IIII . IIII % ii11ii1ii % o00O0oo / o00O0oo
 if 29 - 29: Oo * o0oO0 * ii11ii1ii / i11iIiiIii
def I1111I1II11 ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , url , 9031 , OOooO0OOoo + 'icon.png' )
def iiiIIIIiIi ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , url , 9032 , OOooO0OOoo + 'icon.png' )
def Iii ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , url in ooOO0O0ooOooO :
  if '://' in oOOOo00O00oOo :
   pass
   iii1 ( ( oOOOo00O00oOo ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOooO0OOoo + 'icon.png' )
def IIIII1iii ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , url in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , url , 222 , OOooO0OOoo + 'icon.png' )
  if 7 - 7: OOooOOo + i1IIi . OOOo0 / Oo
  if 22 - 22: o0oO0 - o0oO0 % OoOO0ooOOoo0O . O0oO + OoOO
  if 63 - 63: OOOo0 % O0oO * OOooOOo + O0oO / Oo % oO0o0ooO0
def iiI1i1Iii111 ( ) :
 Iiii1i1 = Iiii ( 'http://tvshows.cnfstudio.com/' )
 ooOO0O0ooOooO = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , 'http://tvshows.cnfstudio.com/genre/' + oo000o , 7010 , OOooO0OOoo + 'icon.png' )
  print '>>>>>>>>>>' + oo000o
  if 43 - 43: OOooOOo
def OO00oOooo0O ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOo = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( ( oOOOo00O00oOo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , iiIiIIIiiI )
 oOOOo = oOOOo
 for url in oOOOo :
  o0OoOO000ooO0 ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  o0OoOO000ooO0 ( 'Next' , url , 7010 , '' )
  if 68 - 68: OoOO - ii11ii1ii % O0 % O0oO
def Ii1II ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , Ii1IIIIi1ii1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  iii1 ( ( 'Season' ) + Ii1IIIIi1ii1I + ( '  ' ) + oOOOo00O00oOo , url , 7004 , OOooO0OOoo + 'icon.png' )
  if 67 - 67: iIii1I11I1II1 - o00O0oo + OOooOOo
def o000O0OOoo ( url ) :
 if 60 - 60: OOOo0 * O0oO % Ooo00oOo00o + OoOO
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOooO0OOoo + 'icon.png' )
  if 52 - 52: i1IIi
def o000 ( name , url , img ) :
 iIIiiI1II1i11 = Iiii ( url )
 OOooo0O = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 iiI1iIIiI = len ( OOooo0O )
 if 57 - 57: Ooo00oOo00o / i1IIi . i1IIi
 if 74 - 74: iIii1I11I1II1 * IIII % I1IiI
 if iiI1iIIiI == 1 :
  for iiI11iIi in OOooo0O :
   iiI11iIi = iiI11iIi . replace ( 'player' , 'watch' )
   oooOO0OO0O = iiI11iIi + '&fv=&sou='
   o00o = Iiii ( oooOO0OO0O )
   III11I = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o00o )
   for Ii1I11I in III11I :
    iiIii1I = False
    Resolve ( Ii1I11I )
    if 47 - 47: o0oO0 . o0000oOoOoO0o / OOooOOo
 elif iiI1iIIiI > 1 :
  if 83 - 83: OOooOOo / OoOO0ooOOoo0O / OoOO0ooOOoo0O + OOooOOo * O0oO + OOooOOo
  for iiI11iIi in OOooo0O :
   IIIIiii = Iiii ( iiI11iIi )
   oO0o = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IIIIiii )
   IIIii1iiIi = oO0o
   IIIii1iiIi = ( str ( IIIii1iiIi ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIIii1iiIi
   iii1 ( 'DOUBLE LINK' , IIIii1iiIi , 424 , '' )
   if 63 - 63: ii11ii1ii
   for url in oO0o :
    o0OoOO000ooO0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     o0OOOo = Google . resolve ( url )
    except :
     pass
    try :
     i1II = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( o0OOOo ) )
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
 o0OoOO000ooO0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOooO0OOoo + 'Movies.png' )
 if 86 - 86: Ooo00oOo00o * OoooooooOO
 o0OoOO000ooO0 ( 'Search Movies' , '' , 7017 , OOooO0OOoo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 71 - 71: iIii1I11I1II1 - OoOO0ooOOoo0O . OOOo0 % OoooooooOO + OoOO0ooOOoo0O
 if 26 - 26: Oo + OoOO0ooOOoo0O / Ooo00oOo00o % I1IiI % ii11ii1ii + OoOoOO00
def i11I1I1iiI ( ) :
 Iiii1i1 = Iiii ( 'http://cnfstudio.com/' )
 ooOO0O0ooOooO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , 'http://cnfstudio.com/genre/' + oo000o , 7003 , OOooO0OOoo + 'icon.png' )
  if 34 - 34: o0000oOoOoO0o % o0oO0 . O0 . iIii1I11I1II1
i1iiIII111ii = xbmcgui . Dialog ( )
if 93 - 93: i1IIi . i11iIiiIii . Oo
if 99 - 99: o0000oOoOoO0o - O0oO - OoOO % Ooo00oOo00o
def IiiIIiiiiii ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOo = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oOOOo00O00oOo in ooOO0O0ooOooO :
  iii1 ( ( oOOOo00O00oOo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iiIiIIIiiI )
 oOOOo = oOOOo
 for url in oOOOo :
  o0OoOO000ooO0 ( 'Next Page' , url , 7003 , '' )
  if 100 - 100: Oo + OOooOOo - O0 % OoOoOO00 . oO0o0ooO0
def ooOo0OoOooo00 ( url ) :
 if 96 - 96: ii11ii1ii % o0oO0 % o00O0oo - o0oO0 % I1IiI + ii11ii1ii
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  iii1i1iiiiIi = url + '&fv=&sou='
  iii1i1iiiiIi = iii1i1iiiiIi . replace ( 'player' , 'watch' )
  iI = Oo0OIi11 ( iii1i1iiiiIi )
  II1i111 = Oo0OIi11 ( url )
  if 50 - 50: IIII % i1IIi
  if 21 - 21: OoooooooOO - iIii1I11I1II1
def Oo0OIi11 ( url ) :
 if 93 - 93: OoOO - OOooOOo % I1IiI . I1IiI - o0oO0
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  O00ooOo ( url )
  if 80 - 80: OOooOOo - OoOO0ooOOoo0O + OoooooooOO
  if 98 - 98: OoOO0ooOOoo0O + i1IIi . OOOo0 - OoOoOO00 - OOooOOo
def iIIi1I1ii ( ) :
 O0O00o0OOO0 ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 14 - 14: O0 / i1IIi / Oo + iIii1I11I1II1
def ooO00O00oOO ( url ) :
 ooOO0O0ooOooO = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for I1IIII1ii , oOOOo00O00oOo , url in ooOO0O0ooOooO :
  iii1 ( oOOOo00O00oOo , url , 222 , OOooO0OOoo + 'streams.png' )
  if 13 - 13: OoooooooOO * OoOO - o00O0oo / OoOO0ooOOoo0O + o0000oOoOoO0o + IIII
  if 39 - 39: iIii1I11I1II1 - OoooooooOO
def oO0oooooo ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , oo000o , 1007 , iiIi1IIi1I )
def o0OO0Oo ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 3 - 3: O0oO - O0 % iIii1I11I1II1 / IIII . OOooOOo
  if 3 - 3: O0 % OoooooooOO / OoOO0ooOOoo0O
def ooOo ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  if '.php' in url :
   o0OoOO000ooO0 ( oOOOo00O00oOo , url , 1016 , iiIi1IIi1I )
  else :
   iii1 ( oOOOo00O00oOo , url , 222 , iiIi1IIi1I )
   if 84 - 84: OoOO0ooOOoo0O
def o0OoO00 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , oo000o , 1007 , iiIi1IIi1I )
def IIIIIiII1 ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 45 - 45: OOOo0 / oO0o0ooO0 . oO0o0ooO0
def i1oO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iIIi1IIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iIIi1IIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIi1IIi )
 if 43 - 43: O0oO % oO0o0ooO0
 if 69 - 69: oO0o0ooO0 % Ooo00oOo00o
def oOOoO ( url ) :
 Iiii1i1 = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOOo00O00oOo + '[/COLOR]' , url , 1006 , iiIiIIIiiI )
def iIi11ii ( url ) :
 Iiii1i1 = OO ( url )
 i11I1 = url
 ooOO0O0ooOooO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  if '.mp3' in oOOOo00O00oOo :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iii1 ( ( oOOOo00O00oOo ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOooO0OOoo + 'music.png' )
  else :
   o0OoOO000ooO0 ( ( oOOOo00O00oOo ) . replace ( '/' , '' ) , i11I1 + url , 1011 , OOooO0OOoo + 'music.png' )
def Ii1iIi111i1i1 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 ooOO0O0ooOooO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , ( 'http://www.cyn.net/music/' + oo000o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iiIiIIIiiI ) . replace ( ' ' , '%20' ) )
def IIOO0ooOo0OoOo0 ( url , img ) :
 Iiii1i1 = OO ( url )
 o0OOOo = url
 img = img
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  iii1 ( ( oOOOo00O00oOo ) . replace ( '.mp3' , '' ) , ( o0OOOo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 87 - 87: OoOO . OOOo0
  if 17 - 17: o00O0oo . i11iIiiIii
def IIIiiiI ( ) :
 OOOOoO00o0O = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1I1I1IIi1III = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiiIII = I1I1I1IIi1III . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 o0OOOo = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 ii1iiIiIII1ii = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 94 - 94: O0 - o0000oOoOoO0o - iIii1I11I1II1 % o0oO0 / o00O0oo % oO0o0ooO0
 iIIiiI1II1i11 = OoOooOoO ( oo000o )
 ooOii = OoOooOoO ( o0OOOo )
 OO0O0Ooo = OoOooOoO ( ii1iiIiIII1ii )
 if 44 - 44: Oo % iIii1I11I1II1
 if iIIiiI1II1i11 != 'Failed' :
  ooOO0O0ooOooO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiiI1II1i11 )
  for oOOOo00O00oOo in ooOO0O0ooOooO :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oOOOo00O00oOo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 90 - 90: OoOoOO00 + OoooooooOO % OoooooooOO
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if ooOii != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiiI1II1i11 )
  for oOOOo00O00oOo in oOOOoo00 :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OOOo + oOOOo00O00oOo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 35 - 35: oO0o0ooO0 / ii11ii1ii * OoooooooOO . OoOoOO00 / Oo
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OO0O0Ooo != 'Failed' :
  O0o = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OO0O0Ooo )
  for oOOOo00O00oOo in O0o :
   if I1I1I1IIi1III in oOOOo00O00oOo . lower ( ) :
    o0OoOO000ooO0 ( ( oOOOo00O00oOo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ii1iiIiIII1ii + oOOOo00O00oOo ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 1 - 1: OoooooooOO + IIII . i1IIi % o0000oOoOoO0o
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: OOooOOo + ii11ii1ii + OOOo0 - OoOO
    if 12 - 12: oO0o0ooO0 . IIII . I1IiI / O0
    if 58 - 58: OOooOOo - OoOoOO00 % OoOO + O0oO . I1IiI / IIII
    if 8 - 8: ii11ii1ii . Ooo00oOo00o * o0000oOoOoO0o + OoOoOO00 % i11iIiiIii
    if 8 - 8: o0oO0 * O0
    if 73 - 73: OOooOOo / OoOO / o0000oOoOoO0o / Ooo00oOo00o
def III1ii ( ) :
 Iiii1i1 = Iiii ( 'http://www.animetoon.org/cartoon' )
 ooOO0O0ooOooO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Iiii1i1 )
 for oo000o , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , oo000o , 1002 , OOooO0OOoo + 'anime.png' )
  if 41 - 41: o0oO0 . Oo + OOOo0
  if 100 - 100: o00O0oo + Ooo00oOo00o
  if 73 - 73: i1IIi - O0oO % o0oO0 / Ooo00oOo00o
def III1iii1i11iI ( url ) :
 Iiii1i1 = Iiii ( url )
 oOOOoo00 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Iiii1i1 )
 for iiIiIIIiiI in oOOOoo00 :
  OoO = iiIiIIIiiI
 O0o = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( Iiii1i1 )
 for url in O0o :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 1002 , OoO )
 ooOO0O0ooOooO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oOOOo00O00oOo in ooOO0O0ooOooO :
  o0OoOO000ooO0 ( oOOOo00O00oOo , url , 1003 , OoO )
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii1iI111 ( url , IMAGE ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Iiii1i1 )
 for oOOOo00O00oOo , url in ooOO0O0ooOooO :
  print oOOOo00O00oOo + '     ' + url
  if 'easy' in url :
   o0O0Oo0Ooo0 ( url )
  elif 'playpanda' in url :
   o0O0Oo0Ooo0 ( url )
   if 35 - 35: IIII + i1IIi * OoOO - o00O0oo . Oo
  xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O0Oo0Ooo0 ( url ) :
 Iiii1i1 = Iiii ( url )
 ooOO0O0ooOooO = re . compile ( "url: '(.+?)'," ) . findall ( Iiii1i1 )
 for url in ooOO0O0ooOooO :
  iii1 ( 'STREAM' , url , 222 , OOooO0OOoo + 'anime.png' )
  if 31 - 31: OOooOOo
  if 15 - 15: O0 / Oo % ii11ii1ii + OOooOOo
def iiiIiI ( url ) :
 iiIiii1iI1i = urllib2 . Request ( url )
 iiIiii1iI1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iiIiii1iI1i . add_header ( 'referer' , url )
 I1ii1ii11i1I = urllib2 . urlopen ( iiIiii1iI1i )
 iii1i1iiiiIi = I1ii1ii11i1I . read ( )
 I1ii1ii11i1I . close ( )
 return iii1i1iiiiIi
 if 9 - 9: iIii1I11I1II1 % ii11ii1ii . OoOO0ooOOoo0O + OoooooooOO
def OO ( url ) :
 iiIiii1iI1i = urllib2 . Request ( url )
 iiIiii1iI1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1ii1ii11i1I = urllib2 . urlopen ( iiIiii1iI1i )
 iii1i1iiiiIi = I1ii1ii11i1I . read ( )
 I1ii1ii11i1I . close ( )
 return iii1i1iiiiIi
 if 62 - 62: O0 / OOOo0 % O0 * Ooo00oOo00o % OOOo0
def Ii ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoo0oO00oo00 = ( '%s%s' % ( O0ii , url ) )
 iii1i1iiiiIi = OO ( url )
 ooOO0O0ooOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iii1i1iiiiIi )
 for url , iiIi1IIi1I , oOOOo00O00oOo in ooOO0O0ooOooO :
  iii1 ( '%s' % ( oOOOo00O00oOo ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiIi1IIi1I )
  if 54 - 54: OoOoOO00 - I1IiI
def O00ooOo ( url ) :
 ooOOooo0Oo = xbmc . Player ( oo0O0o ( ) )
 import urlresolver
 try : ooOOooo0Oo . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( oOOOo00O00oOo ) )
 ooOOooo0Oo = xbmc . Player ( oo0O0o ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIII111ii = xbmcgui . Dialog ( )
  if i1iiIII111ii . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIII111ii . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : ooOOooo0Oo . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 87 - 87: Oo / O0 * IIII / OOooOOo
  if 19 - 19: O0oO + i1IIi . OOOo0 - Oo
def oo0O0o ( ) :
 try :
  iIi1I1 = getSet ( "core-player" )
  if ( iIi1I1 == 'DVDPLAYER' ) : O0oOoo0OoO0O = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIi1I1 == 'MPLAYER' ) : O0oOoo0OoO0O = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIi1I1 == 'PAPLAYER' ) : O0oOoo0OoO0O = xbmc . PLAYER_CORE_PAPLAYER
  else : O0oOoo0OoO0O = xbmc . PLAYER_CORE_AUTO
 except : O0oOoo0OoO0O = xbmc . PLAYER_CORE_AUTO
 return O0oOoo0OoO0O
 return True
 if 63 - 63: OoooooooOO / o0oO0
def o0OoOO000ooO0 ( name , url , mode , iconimage ) :
 oooO00o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o0o00oO0oo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o0o00oO0oo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO00o0 , listitem = OooOo00o , isFolder = True )
 return o0o00oO0oo000
 if 89 - 89: Ooo00oOo00o + IIII * O0oO
def iii1 ( name , url , mode , iconimage ) :
 oooO00o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o0o00oO0oo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o0o00oO0oo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO00o0 , listitem = OooOo00o , isFolder = False )
 return o0o00oO0oo000
 if 28 - 28: OoooooooOO . OoOO % ii11ii1ii / i1IIi / OoOO0ooOOoo0O
 if 36 - 36: OOooOOo + o0000oOoOoO0o - IIII + iIii1I11I1II1 + OoooooooOO
 if 4 - 4: OoOoOO00 . o0000oOoOoO0o + o00O0oo * O0oO . o0oO0
 if 87 - 87: I1IiI / Ooo00oOo00o / i11iIiiIii
 if 74 - 74: OoOO / ii11ii1ii % OOooOOo
 if 88 - 88: I1IiI - i11iIiiIii % OOooOOo * o0000oOoOoO0o + ii11ii1ii
 if 52 - 52: OoOoOO00 . OOOo0 + I1IiI % Ooo00oOo00o
def oo0O0o00 ( heading , announce ) :
 class oOoO0o ( ) :
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
   try : I1II1 = open ( announce ) ; i111iiIIII = I1II1 . read ( )
   except : i111iiIIII = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i111iiIIII ) )
   return
 oOoO0o ( )
 if 80 - 80: Oo * o00O0oo + ii11ii1ii * OoOO0ooOOoo0O
def I1Ii ( ) :
 oo0O0o00 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 77 - 77: iIii1I11I1II1 - i1IIi . OoOO
 if 26 - 26: OOooOOo * IIII . i1IIi
 if 59 - 59: O0 + i1IIi - OOooOOo
 if 62 - 62: i11iIiiIii % OoOO0ooOOoo0O . IIII . OoOO0ooOOoo0O
 if 84 - 84: i11iIiiIii * Ooo00oOo00o
def O0O00Oo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
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
def O000O ( url ) :
 iii1i1iiiiIi = Iiii ( II + Oo00OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 72 - 72: i1IIi / OoOO * O0oO
def I11IiIIIi ( url ) :
 iii1i1iiiiIi = Iiii ( II + Oo0o0OOOOO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 35 - 35: o00O0oo - o00O0oo + i1IIi - O0 - O0oO
def oOO0o0oo0 ( url ) :
 iii1i1iiiiIi = Iiii ( II + oOo000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 1 - 1: iIii1I11I1II1
def oo0oO0o0 ( url ) :
 iii1i1iiiiIi = Iiii ( II + Iii1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 30 - 30: O0 - oO0o0ooO0 % Oo
def O0Oo ( url ) :
 iii1i1iiiiIi = Iiii ( II + iIIiI11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 100 - 100: O0 . o0000oOoOoO0o . Ooo00oOo00o + O0 * OoOO
def iIIiIIIIiII ( url ) :
 iii1i1iiiiIi = Iiii ( II + oOOO0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 49 - 49: o0000oOoOoO0o . o0oO0 * I1IiI % IIII . O0
def IiI1iiI1III1I ( url ) :
 iii1i1iiiiIi = Iiii ( II + Oo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 57 - 57: I1IiI
def i1IiiI1iii1ii ( url ) :
 iii1i1iiiiIi = Iiii ( II + II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 27 - 27: o00O0oo + OOOo0 * iIii1I11I1II1 . OoooooooOO * I1IiI
def OOOo ( url ) :
 iii1i1iiiiIi = Iiii ( II + o0ooOo00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 42 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 38 - 38: iIii1I11I1II1 + i11iIiiIii * Ooo00oOo00o * o0oO0 % OoOO0ooOOoo0O
def I1I11IiiI ( url ) :
 iii1i1iiiiIi = Iiii ( II + I1IiI1iI11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOO0O0ooOooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1i1iiiiIi )
 for oOOOo00O00oOo , url , iiIIIi , ooo00OOOooO , O00OOOoOoo0O in ooOO0O0ooOooO :
  O0O00o0OOO0 ( oOOOo00O00oOo , url , 5 , iiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 2 - 2: iIii1I11I1II1
 if 45 - 45: OoooooooOO / i11iIiiIii
 if 10 - 10: oO0o0ooO0 - OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - ii11ii1ii
 if 97 - 97: OoOoOO00 % O0oO + O0oO - Ooo00oOo00o / o00O0oo * OOOo0
 if 17 - 17: o00O0oo
 if 39 - 39: o0oO0 . OoOoOO00
 if 45 - 45: OoOO * I1IiI / iIii1I11I1II1
 if 77 - 77: O0oO - o0000oOoOoO0o
 if 11 - 11: ii11ii1ii
def iiI1Ii11II1I ( ) :
 try :
  if os . path . exists ( O0OoO000O0OO ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O0OoO000O0OO ) :
     I1Ii11II1I1 = 0
     I1Ii11II1I1 += len ( oOo0OOoO0 )
     if I1Ii11II1I1 > 0 :
      for I1II1 in oOo0OOoO0 :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
  IiI1iI1IiiIi1 = os . path . join ( oOOoO0 , "Textures13.db" )
  os . unlink ( IiI1iI1IiiIi1 )
  i1iiIII111ii . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 90 - 90: O0 + o0000oOoOoO0o - OoooooooOO . o0000oOoOoO0o
 if 60 - 60: OOooOOo . OOooOOo / oO0o0ooO0
 if 45 - 45: O0 . i11iIiiIii % oO0o0ooO0 . I1IiI % IIII % iIii1I11I1II1
 if 58 - 58: iIii1I11I1II1 . I1IiI - i11iIiiIii * iIii1I11I1II1 % i11iIiiIii / OOOo0
 if 80 - 80: ii11ii1ii / iIii1I11I1II1 % I1IiI
 if 80 - 80: Ooo00oOo00o % oO0o0ooO0
 if 99 - 99: o0oO0 / iIii1I11I1II1 - o00O0oo * ii11ii1ii % OOOo0
 if 13 - 13: Ooo00oOo00o
 if 70 - 70: O0oO + O0 . OoOO * o00O0oo
def iiII111iIII1Ii ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 iI1IiiiIiI1Ii = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( iI1IiiiIiI1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iI1IiiiIiI1Ii ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 78 - 78: OoooooooOO / OoOO0ooOOoo0O % I1IiI * OoooooooOO
   if 68 - 68: OoOO
   if I1Ii11II1I1 > 0 :
    if 29 - 29: oO0o0ooO0 + i11iIiiIii % o0000oOoOoO0o
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete KODI Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: I1IiI % iIii1I11I1II1
     for I1II1 in oOo0OOoO0 :
      try :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
      except :
       pass
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      try :
       shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      except :
       pass
       if 87 - 87: I1IiI / IIII + iIii1I11I1II1
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oo0O0oIi = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 86 - 86: OOOo0 / OoOO * o00O0oo
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( oo0O0oIi ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 64 - 64: o0oO0 / O0 * I1IiI * o0oO0
   if I1Ii11II1I1 > 0 :
    if 60 - 60: o0000oOoOoO0o / i1IIi % ii11ii1ii / ii11ii1ii * ii11ii1ii . i11iIiiIii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( I1Ii11II1I1 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 99 - 99: I1IiI
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 77 - 77: OOooOOo
   else :
    pass
  IIiIi11iiIi = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 48 - 48: IIII % o0000oOoOoO0o
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( IIiIi11iiIi ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 3 - 3: IIII % o00O0oo + Oo
   if I1Ii11II1I1 > 0 :
    if 47 - 47: O0 * OOOo0 * Ooo00oOo00o . OoOoOO00
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( I1Ii11II1I1 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 95 - 95: o00O0oo % IIII . O0 % O0oO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 68 - 68: Oo . Oo - ii11ii1ii / o0000oOoOoO0o . o0oO0 / i1IIi
   else :
    pass
    if 12 - 12: ii11ii1ii * i1IIi * o0000oOoOoO0o
    if 23 - 23: OoOO0ooOOoo0O / O0 / OOOo0
    if 49 - 49: o0000oOoOoO0o . OOooOOo % OoOO / o00O0oo
    if 95 - 95: O0 * I1IiI * IIII . o0oO0 / iIii1I11I1II1
 I1IIi1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( I1IIi1I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( I1IIi1I ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 14 - 14: OoOO + O0 / IIII
   if 24 - 24: Ooo00oOo00o - OoOO + ii11ii1ii / oO0o0ooO0 % OOOo0 + iIii1I11I1II1
   if I1Ii11II1I1 > 0 :
    if 79 - 79: I1IiI / o0oO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete WTF Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 77 - 77: Oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 46 - 46: O0oO
   else :
    pass
    if 72 - 72: oO0o0ooO0 * OoOO0ooOOoo0O
    if 67 - 67: i1IIi
 iii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( iii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iii ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 57 - 57: OOOo0
   if 35 - 35: OoooooooOO - O0oO / Ooo00oOo00o
   if I1Ii11II1I1 > 0 :
    if 50 - 50: I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete 4oD Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: o0000oOoOoO0o
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 98 - 98: I1IiI % OoOoOO00
   else :
    pass
    if 95 - 95: iIii1I11I1II1 - O0oO - OoOO0ooOOoo0O + O0oO % ii11ii1ii . OOOo0
    if 41 - 41: O0 + OoOO . i1IIi - OoOoOO00 * OOooOOo . Ooo00oOo00o
 oooO00Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( oooO00Oo ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( oooO00Oo ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 86 - 86: OoOoOO00 + o0oO0 + IIII
   if 9 - 9: o0oO0 + OoOoOO00 % o0oO0 % IIII + iIii1I11I1II1
   if I1Ii11II1I1 > 0 :
    if 59 - 59: i1IIi
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete BBC iPlayer Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 48 - 48: O0 * o00O0oo * Ooo00oOo00o . Ooo00oOo00o * o0000oOoOoO0o - o00O0oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 14 - 14: ii11ii1ii + i11iIiiIii
   else :
    pass
    if 83 - 83: ii11ii1ii / i11iIiiIii + OoOoOO00 . oO0o0ooO0 * OoOO0ooOOoo0O + IIII
    if 42 - 42: i1IIi % OoOoOO00 . o0oO0
    if 7 - 7: ii11ii1ii - OoOO * OoOO0ooOOoo0O + OOooOOo . ii11ii1ii
 ooooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( ooooO ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( ooooO ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 92 - 92: OOooOOo / OOooOOo * o00O0oo
   if 19 - 19: o00O0oo
   if I1Ii11II1I1 > 0 :
    if 55 - 55: OoOO0ooOOoo0O % OoOO0ooOOoo0O / O0 % oO0o0ooO0 - OOooOOo . Oo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Simple Downloader Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: iIii1I11I1II1 * i1IIi . OoooooooOO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 90 - 90: OOooOOo % ii11ii1ii - iIii1I11I1II1 % I1IiI
   else :
    pass
    if 8 - 8: I1IiI * Oo / IIII % o00O0oo - OOOo0
    if 71 - 71: oO0o0ooO0
 Iiii1i11ii1Ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( Iiii1i11ii1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( Iiii1i11ii1Ii ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 12 - 12: OoOO0ooOOoo0O . o00O0oo
   if 79 - 79: O0oO / Oo / oO0o0ooO0 . O0oO * OoooooooOO + OOooOOo
   if I1Ii11II1I1 > 0 :
    if 73 - 73: O0 - ii11ii1ii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ITV Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 2 - 2: OoOoOO00 / O0oO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 54 - 54: i1IIi . o0000oOoOoO0o - ii11ii1ii + o0oO0 + Oo / Oo
   else :
    pass
    if 22 - 22: o0oO0 . iIii1I11I1II1
    if 12 - 12: o00O0oo
 Ooii1IIi1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( Iiii1i11ii1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( Ooii1IIi1ii ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 85 - 85: OoooooooOO % I1IiI * iIii1I11I1II1
   if 44 - 44: iIii1I11I1II1 . ii11ii1ii + O0oO . o0oO0
   if I1Ii11II1I1 > 0 :
    if 7 - 7: ii11ii1ii + iIii1I11I1II1 * o0000oOoOoO0o * o0000oOoOoO0o / OoOoOO00 - o00O0oo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Movies4me Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 65 - 65: OoOO + I1IiI + OoOoOO00
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 77 - 77: OoOoOO00
   else :
    pass
    if 50 - 50: O0 . O0 . o0oO0 % Oo
    if 68 - 68: OoOO
 i11iIIiI1I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( Iiii1i11ii1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( i11iIIiI1I1 ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 4 - 4: Oo * Oo / I1IiI
   if 4 - 4: OOOo0 * I1IiI % o0000oOoOoO0o . I1IiI
   if I1Ii11II1I1 > 0 :
    if 11 - 11: OoOO0ooOOoo0O - I1IiI - OOooOOo * I1IiI + o0oO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Phoenix Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 62 - 62: OOOo0 * i11iIiiIii . oO0o0ooO0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 35 - 35: IIII . O0 + Oo + OoOO0ooOOoo0O + i1IIi
   else :
    pass
    if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
    if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
 O0OOOOOO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( Iiii1i11ii1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O0OOOOOO0 ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 79 - 79: OoOoOO00 - o0oO0 . i1IIi + O0 % O0 * OOOo0
   if 7 - 7: i1IIi + OoOO0ooOOoo0O % oO0o0ooO0 / OOooOOo + i1IIi
   if I1Ii11II1I1 > 0 :
    if 41 - 41: o00O0oo + i11iIiiIii / IIII % ii11ii1ii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Music Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 22 - 22: I1IiI % OOooOOo * o00O0oo - ii11ii1ii + OOooOOo - Oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 15 - 15: OoOO0ooOOoo0O
   else :
    pass
    if 31 - 31: oO0o0ooO0 / i1IIi . Ooo00oOo00o
    if 83 - 83: OoOO / iIii1I11I1II1 + i1IIi / oO0o0ooO0
 IIiiii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( Iiii1i11ii1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( IIiiii1 ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 66 - 66: o0oO0 * I1IiI
   if 2 - 2: OoOO . O0oO * Oo + O0 - o0000oOoOoO0o * iIii1I11I1II1
   if I1Ii11II1I1 > 0 :
    if 12 - 12: OOooOOo * O0oO % OoOoOO00 * i1IIi * iIii1I11I1II1
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete SuperCartoons Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 81 - 81: Oo - o0000oOoOoO0o
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 24 - 24: OoooooooOO . Ooo00oOo00o * OoOoOO00
   else :
    pass
    if 59 - 59: O0oO + Ooo00oOo00o / OoOO0ooOOoo0O
    if 97 - 97: Oo * oO0o0ooO0 % o0oO0 . oO0o0ooO0 - O0oO - OoOO0ooOOoo0O
 oo0O0o00I1ii1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( Iiii1i11ii1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( oo0O0o00I1ii1i ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 22 - 22: OoOO * o00O0oo * i11iIiiIii + oO0o0ooO0 * I1IiI * Ooo00oOo00o
   if 85 - 85: oO0o0ooO0 * OoOO0ooOOoo0O % Oo - oO0o0ooO0 - o0000oOoOoO0o
   if I1Ii11II1I1 > 0 :
    if 46 - 46: O0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete TVonline Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 65 - 65: iIii1I11I1II1 % OoOO + O0 / OoooooooOO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 52 - 52: o00O0oo % OoOO0ooOOoo0O * OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / oO0o0ooO0
   else :
    pass
    if 80 - 80: OoooooooOO + IIII
    if 95 - 95: O0oO / OoOO * O0oO - OoooooooOO * OoooooooOO % Ooo00oOo00o
 iI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( Iiii1i11ii1Ii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iI1 ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 12 - 12: O0oO + OoOO0ooOOoo0O + o0000oOoOoO0o . IIII / o00O0oo
   if 29 - 29: IIII . o0oO0 - OoOoOO00
   if I1Ii11II1I1 > 0 :
    if 68 - 68: iIii1I11I1II1 + OoOoOO00 / OoOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: I1IiI % iIii1I11I1II1 . OOOo0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
      if 70 - 70: o0000oOoOoO0o % OoOoOO00 % O0 . i1IIi / O0oO
   else :
    pass
    if 100 - 100: ii11ii1ii * i11iIiiIii % OoOO / Oo / o0oO0 + ii11ii1ii
    if 59 - 59: O0oO - IIII
    if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
 i111i1I1ii1i = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 try :
  if i1iiIII111ii . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   O0Oooo = os . path . join ( i111i1I1ii1i , "cache.db" )
   os . unlink ( O0Oooo )
   if 27 - 27: o0oO0 + i11iIiiIii * o0000oOoOoO0o + I1IiI + oO0o0ooO0
 except :
  pass
  if 87 - 87: O0
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 87 - 87: OOooOOo / OoOoOO00
 if 90 - 90: o0oO0 - ii11ii1ii - O0 + o00O0oo
 if 68 - 68: OoOO0ooOOoo0O . Oo % o0oO0 - OoooooooOO * oO0o0ooO0 . OoOO0ooOOoo0O
 if 46 - 46: i11iIiiIii - OoOO0ooOOoo0O * OOOo0 * o0000oOoOoO0o % ii11ii1ii * i1IIi
 if 5 - 5: O0 / o0oO0 . Oo + OoooooooOO
 if 97 - 97: IIII . o00O0oo . o00O0oo / iIii1I11I1II1 - Ooo00oOo00o + oO0o0ooO0
 if 32 - 32: OoOO0ooOOoo0O . OOooOOo % IIII + ii11ii1ii + Ooo00oOo00o
 if 76 - 76: Ooo00oOo00o - i11iIiiIii + I1IiI + OoOO0ooOOoo0O / OoooooooOO
 if 50 - 50: OoOoOO00 - O0oO + iIii1I11I1II1 + iIii1I11I1II1
def OoooooOo ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 OooOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OooOo ) :
   I1Ii11II1I1 = 0
   I1Ii11II1I1 += len ( oOo0OOoO0 )
   if 67 - 67: Oo / O0
   if 88 - 88: I1IiI - OoOO0ooOOoo0O
   if I1Ii11II1I1 > 0 :
    if 63 - 63: IIII * OoooooooOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Package Cache Files" , str ( I1Ii11II1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: IIII - OOooOOo . iIii1I11I1II1 . I1IiI / OoOO0ooOOoo0O
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for Ooo0o0oo0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , Ooo0o0oo0 ) )
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
 if 87 - 87: I1IiI - o0oO0 - OoOO0ooOOoo0O + Oo % iIii1I11I1II1 / i11iIiiIii
 if 12 - 12: o0oO0
 if 86 - 86: OoOO - Ooo00oOo00o
 if 63 - 63: OOOo0 / I1IiI + OoooooooOO . o0000oOoOoO0o . o0oO0
 if 48 - 48: i1IIi - oO0o0ooO0 - i11iIiiIii . o0000oOoOoO0o - oO0o0ooO0 * o0000oOoOoO0o
 if 60 - 60: I1IiI / ii11ii1ii + OoOO0ooOOoo0O - oO0o0ooO0
 if 49 - 49: Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI + O0oO
 if 35 - 35: OoOoOO00 . OOOo0 / i1IIi / OOOo0 * OoOO
 if 85 - 85: OoOoOO00 . o0oO0 % OoOO0ooOOoo0O % o0000oOoOoO0o
def OOo00ooOoO0o ( url , name ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i1i1iiIIiiiII = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 Ii1I1 = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( Ii1I1 ) == False :
  if i1iiIII111ii . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   i1i1iiIIiiiII = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
   try :
    os . remove ( i1i1iiIIiiiII )
    print '=== GenieTv - REMOVING    ' + str ( i1i1iiIIiiiII ) + '    ==='
   except :
    pass
   iii1i1iiiiIi = I11 . http_GET ( url ) . content
   IIo0Oo0oO0oOO00 = open ( i1i1iiIIiiiII , "w" )
   IIo0Oo0oO0oOO00 . write ( iii1i1iiiiIi )
   IIo0Oo0oO0oOO00 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( i1i1iiIIiiiII ) + '    ==='
   i1iiIII111ii = xbmcgui . Dialog ( )
   i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  i1i1iiIIiiiII = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
  try :
   os . remove ( i1i1iiIIiiiII )
   print '=== GenieTv - REMOVING    ' + str ( i1i1iiIIiiiII ) + '    ==='
  except :
   pass
  iii1i1iiiiIi = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( i1i1iiIIiiiII , "w" )
  IIo0Oo0oO0oOO00 . write ( iii1i1iiiiIi )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i1i1iiIIiiiII ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 71 - 71: I1IiI + iIii1I11I1II1 * OoOO . O0oO % i11iIiiIii % iIii1I11I1II1
def OooOO0oOOo0O ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i1i1iiIIiiiII = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  IIo0Oo0oO0oOO00 = open ( i1i1iiIIiiiII ) . read ( )
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
 if 42 - 42: oO0o0ooO0 / OOooOOo + Oo . Oo % OoOO0ooOOoo0O
def Ii1III1 ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i1i1iiIIiiiII = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  os . remove ( i1i1iiIIiiiII )
  i1iiIII111ii = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( i1i1iiIIiiiII ) + '    ==='
  i1iiIII111ii . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 80 - 80: iIii1I11I1II1 . oO0o0ooO0 . O0oO
 if 9 - 9: OoooooooOO * O0
 if 76 - 76: O0oO - OoOO . OoOO0ooOOoo0O % OOooOOo
 if 30 - 30: ii11ii1ii % o0000oOoOoO0o / O0oO
 if 1 - 1: O0oO - o0000oOoOoO0o
 if 45 - 45: o00O0oo - OoOO0ooOOoo0O
 if 70 - 70: Ooo00oOo00o % OOOo0 / OOOo0 . o0000oOoOoO0o % o0oO0 . OoOoOO00
 if 10 - 10: o00O0oo - i11iIiiIii . ii11ii1ii % i1IIi
 if 78 - 78: iIii1I11I1II1 * Oo . Oo - OoOO0ooOOoo0O . iIii1I11I1II1
 if 30 - 30: o0oO0 + o0oO0 % IIII - OOooOOo - ii11ii1ii
def i111IiiI1Ii ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 ooOO0O0ooOooO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for OooOOOOOo , i1I11ii , o0ooO00O0O , iiiI1iI1 in ooOO0O0ooOooO :
  if inc < 2 : i1iiIII111ii = xbmcgui . Dialog ( ) ; i1iiIII111ii . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OooOOOOOo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % o0ooO00O0O , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iiiI1iI1 )
  inc = inc + 1
  if 15 - 15: IIII . i1IIi * I1IiI % iIii1I11I1II1
  if 35 - 35: ii11ii1ii + O0oO - I1IiI % OoOO % OOooOOo % I1IiI
  if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
  if 24 - 24: o0oO0 - o0000oOoOoO0o * OoOO
  if 87 - 87: o00O0oo - ii11ii1ii % ii11ii1ii . OoOO / ii11ii1ii
  if 6 - 6: I1IiI / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
  if 79 - 79: IIII % Ooo00oOo00o
  if 81 - 81: i11iIiiIii + i11iIiiIii * Ooo00oOo00o + IIII
  if 32 - 32: O0 . OoooooooOO
def iiI ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  i1i1iiIIiiiII = os . path . join ( oOo00O0oo00o0 , 'addons2.ini' )
  iii1i1iiiiIi = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( i1i1iiIIiiiII , "w" )
  IIo0Oo0oO0oOO00 . write ( iii1i1iiiiIi )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i1i1iiIIiiiII ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 17 - 17: i11iIiiIii / Oo . Ooo00oOo00o / OOOo0
def Ii1 ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  i1i1iiIIiiiII = os . path . join ( oOo00O0oo00o0 , 'settings.xml' )
  iii1i1iiiiIi = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( i1i1iiIIiiiII , "w" )
  IIo0Oo0oO0oOO00 . write ( iii1i1iiiiIi )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i1i1iiIIiiiII ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 59 - 59: Oo % O0 . I1IiI
 if 41 - 41: i1IIi + OoOoOO00 * o0oO0
def o0oOoOo0 ( ) :
 try :
  III1IiI1i1i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( III1IiI1i1i ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    o0OOOOOo0 = os . path . join ( III1IiI1i1i , "source.db" )
    os . unlink ( o0OOOOOo0 )
  i1iiIII111ii . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 57 - 57: iIii1I11I1II1 + iIii1I11I1II1
 if 56 - 56: OoOO + o0oO0
 if 32 - 32: OoOoOO00 + I1IiI % o0oO0 / I1IiI + ii11ii1ii
 if 2 - 2: i11iIiiIii - O0oO + Ooo00oOo00o % o0000oOoOoO0o * o00O0oo
 if 54 - 54: O0 - oO0o0ooO0 . OoOO0ooOOoo0O % oO0o0ooO0 + oO0o0ooO0
def Iiii ( url ) :
 iiIiii1iI1i = urllib2 . Request ( url )
 iiIiii1iI1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1ii1ii11i1I = urllib2 . urlopen ( iiIiii1iI1i )
 iii1i1iiiiIi = I1ii1ii11i1I . read ( )
 I1ii1ii11i1I . close ( )
 return iii1i1iiiiIi
 if 36 - 36: OoOO0ooOOoo0O % i11iIiiIii
 if 47 - 47: i1IIi + OoOoOO00 . Oo * OoOO . o0000oOoOoO0o / i1IIi
 if 50 - 50: O0oO / i1IIi % OoooooooOO
 if 83 - 83: ii11ii1ii * ii11ii1ii + OoOO0ooOOoo0O
 if 57 - 57: O0 - O0 . ii11ii1ii / OOooOOo / o00O0oo
 if 20 - 20: OoOO0ooOOoo0O * OoOoOO00 - I1IiI - OoOO * O0oO
 if 6 - 6: o0oO0 + OoOO0ooOOoo0O / Oo + IIII % OoOoOO00 / Ooo00oOo00o
def iiIi ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OooooOo = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OooooOo :
  IIIiiiIiI = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; IIIiiiIiI = xbmc . translatePath ( IIIiiiIiI ) ;
  OO0OOoooo0o = os . path . join ( IIIiiiIiI , ".." , ".." ) ; OO0OOoooo0o = os . path . abspath ( OO0OOoooo0o ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OO0OOoooo0o ) ; IiIi1Ii = False
  try :
   for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OO0OOoooo0o , topdown = True ) :
    Ooo0OOoOoO0 [ : ] = [ Ooo0o0oo0 for Ooo0o0oo0 in Ooo0OOoOoO0 if Ooo0o0oo0 not in Oo0oO0ooo ]
    for oOOOo00O00oOo in oOo0OOoO0 :
     try : os . remove ( os . path . join ( iiI11ii1I1 , oOOOo00O00oOo ) )
     except :
      if oOOOo00O00oOo not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiIi1Ii = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oOOOo00O00oOo )
    for oOOOo00O00oOo in Ooo0OOoOoO0 :
     try : os . rmdir ( os . path . join ( iiI11ii1I1 , oOOOo00O00oOo ) )
     except :
      if oOOOo00O00oOo not in [ "Database" , "userdata" ] : IiIi1Ii = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oOOOo00O00oOo )
   if not IiIi1Ii : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oO00oooOOoOo0 ( )
 if 39 - 39: o00O0oo
 if 24 - 24: i11iIiiIii - o00O0oo + OoOO * OOOo0
 if 94 - 94: OOOo0 + iIii1I11I1II1 / O0 - OoooooooOO % ii11ii1ii
def o0Oo0oo ( ) :
 Ii11iiIIiI1 = [ ]
 I1Iii11I111I = sys . argv [ 2 ]
 if len ( I1Iii11I111I ) >= 2 :
  IIIiI1iiiiiIi = sys . argv [ 2 ]
  O0oo0 = IIIiI1iiiiiIi . replace ( '?' , '' )
  if ( IIIiI1iiiiiIi [ len ( IIIiI1iiiiiIi ) - 1 ] == '/' ) :
   IIIiI1iiiiiIi = IIIiI1iiiiiIi [ 0 : len ( IIIiI1iiiiiIi ) - 2 ]
  iii1iiii11I = O0oo0 . split ( '&' )
  Ii11iiIIiI1 = { }
  for o0 in range ( len ( iii1iiii11I ) ) :
   oO0o0oo0O0 = { }
   oO0o0oo0O0 = iii1iiii11I [ o0 ] . split ( '=' )
   if ( len ( oO0o0oo0O0 ) ) == 2 :
    Ii11iiIIiI1 [ oO0o0oo0O0 [ 0 ] ] = oO0o0oo0O0 [ 1 ]
    if 98 - 98: IIII * iIii1I11I1II1 . o00O0oo * Oo / ii11ii1ii + o0oO0
 return Ii11iiIIiI1
 if 25 - 25: OoOO
Ii1I1i = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
ii = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OOI1iI1ii1II = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
Iii11111iiI = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
OO0OoO0o00 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
o0OOOOoO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
Oo00OO0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OoO0Ooo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
Oo0o0OOOOO0O = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oOo000O = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
Iii1Ii = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iIIiI11i = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oOOO0O0o = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
Oo000 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
II1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0ooOo00O = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ii1I1I = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOooo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oo0O0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
I11i1ii1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
O000oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1IiI1iI11 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
O0ii = base64 . decodestring ( 'Q1VOVA==' )
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description ) :
 oooO00o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0o00oO0oo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  o0o00oO0oo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO00o0 , listitem = OooOo00o , isFolder = False )
 else :
  o0o00oO0oo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO00o0 , listitem = OooOo00o , isFolder = True )
 return o0o00oO0oo000
def I111Ii111 ( name , url , mode , iconimage , fanart , description ) :
 oooO00o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0o00oO0oo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 o0o00oO0oo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO00o0 , listitem = OooOo00o , isFolder = False )
 return o0o00oO0oo000
 if 56 - 56: O0
 if 45 - 45: I1IiI - Ooo00oOo00o - I1IiI
IIIiI1iiiiiIi = o0Oo0oo ( )
oo000o = None
oOOOo00O00oOo = None
IIiiI = None
iiIIIi = None
ooo00OOOooO = None
O00OOOoOoo0O = None
if 36 - 36: oO0o0ooO0
if 52 - 52: O0oO % O0 . i1IIi . OoooooooOO
try :
 oo000o = urllib . unquote_plus ( IIIiI1iiiiiIi [ "url" ] )
except :
 pass
try :
 oOOOo00O00oOo = urllib . unquote_plus ( IIIiI1iiiiiIi [ "name" ] )
except :
 pass
try :
 iiIIIi = urllib . unquote_plus ( IIIiI1iiiiiIi [ "iconimage" ] )
except :
 pass
try :
 IIiiI = int ( IIIiI1iiiiiIi [ "mode" ] )
except :
 pass
try :
 ooo00OOOooO = urllib . unquote_plus ( IIIiI1iiiiiIi [ "fanart" ] )
except :
 pass
try :
 O00OOOoOoo0O = urllib . unquote_plus ( IIIiI1iiiiiIi [ "description" ] )
except :
 pass
 if 33 - 33: OoOO0ooOOoo0O % OoOoOO00
 if 71 - 71: o00O0oo * O0oO % OoOoOO00 . o00O0oo % Ooo00oOo00o + ii11ii1ii
print str ( iiI1IiI ) + ': ' + str ( iIii1 )
print "Mode: " + str ( IIiiI )
print "URL: " + str ( oo000o )
print "Name: " + str ( oOOOo00O00oOo )
print "IconImage: " + str ( iiIIIi )
if 66 - 66: o00O0oo - Oo . i1IIi
if 75 - 75: o00O0oo - o0000oOoOoO0o % I1IiI
def o0oo0o0O00OO ( content , viewType ) :
 if 80 - 80: o00O0oo / OoOO0ooOOoo0O
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 21 - 21: Oo - iIii1I11I1II1 - O0oO
  if 1 - 1: OOOo0 * OoOO0ooOOoo0O + o00O0oo + OOOo0 - i11iIiiIii
if IIiiI == None :
 oOOO00o ( )
 if 79 - 79: o0oO0 . OoOO / OoOO - o0oO0 * Oo / OOooOOo
elif IIiiI == 1 :
 iI11iI1IiiIiI ( oo000o )
 if 19 - 19: ii11ii1ii
elif IIiiI == 44 :
 IiI1i ( oo000o )
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
elif IIiiI == 2 :
 O000OOOOOo ( )
 if 66 - 66: O0
elif IIiiI == 3 :
 oO0OOoO0 ( )
 if 52 - 52: Ooo00oOo00o * OoooooooOO
elif IIiiI == 21 :
 Oo0O ( )
 if 12 - 12: O0 + IIII * i1IIi . Ooo00oOo00o
elif IIiiI == 4 :
 Oo0OoO00oOO0o ( )
 if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
elif IIiiI == 5 :
 O0oOOO0ooOOO0OOO ( oOOOo00O00oOo , oo000o , O00OOOoOoo0O )
 if 28 - 28: iIii1I11I1II1
elif IIiiI == 6 :
 OoooooOo ( oo000o )
 if 7 - 7: OOooOOo % IIII * I1IiI
elif IIiiI == 7 :
 OOo00ooOoO0o ( oo000o , oOOOo00O00oOo )
 if 58 - 58: IIII / o0000oOoOoO0o + OoOoOO00 % oO0o0ooO0 - OoooooooOO
elif IIiiI == 8 :
 OooOO0oOOo0O ( oo000o , oOOOo00O00oOo )
 if 25 - 25: I1IiI % OoooooooOO * Oo - i1IIi * OoOoOO00 * OoOO
elif IIiiI == 9 :
 FIXREPOSADDONS ( oo000o )
 if 30 - 30: o0000oOoOoO0o % I1IiI / ii11ii1ii * O0 * o00O0oo . OOOo0
elif IIiiI == 10 :
 O0O00Oo ( )
 if 46 - 46: I1IiI - O0
elif IIiiI == 11 :
 Ii1III1 ( oo000o )
 if 70 - 70: o0000oOoOoO0o + Oo * iIii1I11I1II1 . OOOo0 * o0000oOoOoO0o
elif IIiiI == 12 :
 i111IiiI1Ii ( )
 if 49 - 49: OOooOOo
elif IIiiI == 13 :
 iiI1Ii11II1I ( )
 if 25 - 25: oO0o0ooO0 . OoooooooOO * iIii1I11I1II1 . OOooOOo / O0 + o00O0oo
elif IIiiI == 14 :
 iiII111iIII1Ii ( oo000o )
 if 68 - 68: Oo
elif IIiiI == 15 :
 Oo0o00 ( )
 if 22 - 22: OoOO0ooOOoo0O
elif IIiiI == 16 :
 iiI ( oo000o , oOOOo00O00oOo )
 if 22 - 22: oO0o0ooO0 * o0000oOoOoO0o - Oo * O0 / i11iIiiIii
elif IIiiI == 17 :
 Ii1 ( oo000o , oOOOo00O00oOo )
 if 78 - 78: Oo * O0 / o0oO0 + OoooooooOO + OoOO0ooOOoo0O
elif IIiiI == 18 :
 o0oOoOo0 ( )
 if 23 - 23: oO0o0ooO0 % OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
elif IIiiI == 19 :
 oo0oO0oOOoo ( oOOOo00O00oOo , oo000o , O00OOOoOoo0O )
 if 94 - 94: i1IIi
elif IIiiI == 40 :
 I1I1i1I ( oOOOo00O00oOo , oo000o , O00OOOoOoo0O )
 if 36 - 36: OOOo0 + Oo
elif IIiiI == 42 :
 Oooo0oOO ( oOOOo00O00oOo , oo000o , O00OOOoOoo0O )
 if 46 - 46: oO0o0ooO0
elif IIiiI == 43 :
 oooOo0OOOoo0 ( oOOOo00O00oOo , oo000o , O00OOOoOoo0O )
 if 65 - 65: i1IIi . ii11ii1ii / o0oO0
elif IIiiI == 20 :
 iIIIIi1iiIi1 ( oo000o )
 if 11 - 11: IIII * o0oO0 / o0oO0 - OoOO0ooOOoo0O
elif IIiiI == 22 :
 O000O ( oo000o )
 if 68 - 68: OOOo0 % IIII - IIII / OOOo0 + ii11ii1ii - Oo
elif IIiiI == 23 :
 I11IiIIIi ( oo000o )
 if 65 - 65: o0oO0 - i1IIi
elif IIiiI == 24 :
 oOO0o0oo0 ( oo000o )
 if 62 - 62: o0000oOoOoO0o / OoOO % Oo . OoooooooOO / i11iIiiIii / O0oO
elif IIiiI == 25 :
 oo0oO0o0 ( oo000o )
 if 60 - 60: OOOo0 % OoOO / OOooOOo % OoOO * i11iIiiIii / oO0o0ooO0
elif IIiiI == 26 :
 O0Oo ( oo000o )
 if 34 - 34: O0oO - OoOO0ooOOoo0O
elif IIiiI == 27 :
 iIIiIIIIiII ( oo000o )
 if 25 - 25: OoOO % OOOo0 + i11iIiiIii + O0 * OoooooooOO
elif IIiiI == 28 :
 IiI1iiI1III1I ( oo000o )
 if 64 - 64: i1IIi
elif IIiiI == 29 :
 i1IiiI1iii1ii ( oo000o )
 if 10 - 10: O0oO % O0 / OOOo0 % o0000oOoOoO0o
elif IIiiI == 30 :
 IIi ( oo000o )
 if 25 - 25: OoOoOO00 / Ooo00oOo00o
elif IIiiI == 31 :
 OOOo ( oo000o )
 if 64 - 64: O0 % o0oO0
elif IIiiI == 32 :
 iiI111I1iIiI ( )
 if 40 - 40: OOooOOo + o0000oOoOoO0o
elif IIiiI == 33 :
 Oo0oO ( )
 if 77 - 77: i11iIiiIii % IIII + O0oO % OoooooooOO - o0000oOoOoO0o
elif IIiiI == 35 :
 O0OooOo0o ( oo000o )
 if 26 - 26: Oo + O0 - iIii1I11I1II1
elif IIiiI == 34 :
 ii11IIII11I ( oo000o )
 if 47 - 47: OoooooooOO
elif IIiiI == 36 :
 OooOOOOo ( oo000o )
 if 2 - 2: I1IiI % O0oO * Oo * I1IiI
elif IIiiI == 37 :
 iii1i ( oo000o )
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
elif IIiiI == 38 :
 Oo0oOOOoOooOo ( oo000o )
 if 26 - 26: OOooOOo % OoOO0ooOOoo0O + OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / oO0o0ooO0
elif IIiiI == 41 :
 iiIi ( IIIiI1iiiiiIi )
 if 64 - 64: OoOO % I1IiI / OoOoOO00 % o0oO0 - oO0o0ooO0
elif IIiiI == 39 :
 I1I11IiiI ( oo000o )
 if 2 - 2: O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
elif IIiiI == 45 :
 TEXTS ( )
 if 26 - 26: OoOO0ooOOoo0O * Oo
elif IIiiI == 46 :
 I1Ii ( )
 if 31 - 31: o0000oOoOoO0o * OoOO . o00O0oo
elif IIiiI == 47 :
 GEVID ( )
 if 35 - 35: o0000oOoOoO0o
elif IIiiI == 48 :
 O0O ( oOOOo00O00oOo , oo000o , O00OOOoOoo0O )
 if 94 - 94: o0oO0 / i11iIiiIii % O0
elif IIiiI == 49 :
 OoOO0oo0o ( )
 if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
elif IIiiI == 222 :
 O00ooOo ( oo000o )
 if 95 - 95: OoooooooOO % OoooooooOO . o00O0oo
elif IIiiI == 333 :
 Ii ( oo000o )
 if 26 - 26: OoOO + IIII - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
 if 68 - 68: O0
elif IIiiI == 1001 :
 III1ii ( )
 if 76 - 76: ii11ii1ii
elif IIiiI == 1005 :
 o0OoO00 ( )
 if 99 - 99: OOooOOo
elif IIiiI == 1007 :
 IIIIIiII1 ( oo000o )
 if 1 - 1: o00O0oo * I1IiI * Ooo00oOo00o + Oo
elif IIiiI == 1010 :
 oOOoO ( oo000o )
 if 90 - 90: O0oO % Oo - Oo . iIii1I11I1II1 / OoOO0ooOOoo0O + o0000oOoOoO0o
elif IIiiI == 1011 :
 iIi11ii ( oo000o )
 if 89 - 89: OoOO
elif IIiiI == 1030 :
 Ii1iIi111i1i1 ( )
 if 87 - 87: oO0o0ooO0 % Oo
elif IIiiI == 1031 :
 IIOO0ooOo0OoOo0 ( oo000o , iiIIIi )
 if 62 - 62: Ooo00oOo00o + o0oO0 / oO0o0ooO0 * i11iIiiIii
elif IIiiI == 1006 :
 Parse . ParseURL ( oo000o )
 if 37 - 37: oO0o0ooO0
elif IIiiI == 2030 :
 Parse . addonParseURL ( oo000o )
 if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
elif IIiiI == 2031 :
 Parse . apkParseURL ( oo000o )
 if 94 - 94: IIII * o0000oOoOoO0o * OoooooooOO / OOooOOo . IIII - OOooOOo
elif IIiiI == 1002 :
 III1iii1i11iI ( oo000o )
 if 13 - 13: OoOO0ooOOoo0O / IIII - Ooo00oOo00o / OoOO0ooOOoo0O . i1IIi
elif IIiiI == 1003 :
 ii1iI111 ( oo000o , iiIIIi )
 if 22 - 22: O0 - o0000oOoOoO0o + O0oO . o00O0oo * i1IIi
elif IIiiI == 1004 :
 o0O0Oo0Ooo0 ( oo000o )
 if 26 - 26: iIii1I11I1II1 * OOooOOo . o0000oOoOoO0o
elif IIiiI == 1008 :
 oOo0oO ( )
 if 10 - 10: O0oO * OoOO % Oo - o0000oOoOoO0o % Oo
elif IIiiI == 1009 :
 M3UPLAY ( oo000o )
 if 65 - 65: oO0o0ooO0 * iIii1I11I1II1 / O0 . o0000oOoOoO0o
elif IIiiI == 2001 :
 ooO00O00oOO ( oo000o )
 if 94 - 94: Oo . o0oO0 * i11iIiiIii - OOooOOo . oO0o0ooO0
elif IIiiI == 1013 :
 II1i111Ii1i ( )
 if 98 - 98: OoOO0ooOOoo0O + o00O0oo
elif IIiiI == 1014 :
 OoO00 ( )
 if 52 - 52: Oo / I1IiI - O0oO . oO0o0ooO0
elif IIiiI == 1015 :
 OO0Ooooo000Oo ( oo000o )
 if 50 - 50: iIii1I11I1II1 - oO0o0ooO0 - o0000oOoOoO0o
elif IIiiI == 1016 :
 ooOo ( oo000o )
 if 60 - 60: iIii1I11I1II1 * o0oO0
elif IIiiI == 1023 :
 ii11i1 ( )
 if 71 - 71: I1IiI % Oo % o0oO0
elif IIiiI == 1024 :
 oO0oooooo ( )
 if 34 - 34: o0000oOoOoO0o / o0000oOoOoO0o % IIII . I1IiI / Oo
elif IIiiI == 1025 :
 o0OO0Oo ( oo000o )
 if 99 - 99: o0oO0 * OOOo0 - o0oO0 % o00O0oo
elif IIiiI == 4001 :
 oOOO0o0o ( )
 if 40 - 40: OoOO0ooOOoo0O / IIII / iIii1I11I1II1 + o00O0oo
elif IIiiI == 4002 :
 iiI1 ( )
 if 59 - 59: o0000oOoOoO0o * OoooooooOO + OoOO0ooOOoo0O . iIii1I11I1II1 / i1IIi
elif IIiiI == 4003 :
 iIIIIii1 ( )
 if 75 - 75: o0000oOoOoO0o . OoOO0ooOOoo0O - iIii1I11I1II1 * Ooo00oOo00o * oO0o0ooO0
elif IIiiI == 3000 :
 iIIi1I1ii ( )
 if 93 - 93: o0oO0
elif IIiiI == 404 :
 i1oO ( oOOOo00O00oOo , oo000o , iiIIIi )
 if 18 - 18: o0oO0
elif IIiiI == 7030 :
 oOo000 ( )
 if 66 - 66: OoOO * i11iIiiIii + I1IiI / OoOO0ooOOoo0O
elif IIiiI == 7021 :
 oo0ooOO ( oOOOo00O00oOo )
 if 96 - 96: OoOO0ooOOoo0O + OoOO0ooOOoo0O % IIII % OoOO0ooOOoo0O
elif IIiiI == 7022 :
 i1I1II1iIIi11 ( oOOOo00O00oOo )
 if 28 - 28: iIii1I11I1II1 + I1IiI . OOooOOo % i11iIiiIii
elif IIiiI == 7000 :
 o000 ( oOOOo00O00oOo , oo000o , img )
 if 58 - 58: o0000oOoOoO0o / OoooooooOO % OoOO + Ooo00oOo00o
elif IIiiI == 7050 :
 IiIi1i1ii ( )
 if 58 - 58: O0
elif IIiiI == 7051 :
 IiIi1 ( oo000o )
 if 91 - 91: oO0o0ooO0 / ii11ii1ii . oO0o0ooO0 - OOooOOo + ii11ii1ii
elif IIiiI == 7060 :
 Ooo0o0OOO ( )
 if 72 - 72: o00O0oo . IIII * ii11ii1ii / ii11ii1ii / oO0o0ooO0
elif IIiiI == 7061 :
 OOO00O0oOOo ( oo000o )
 if 13 - 13: i1IIi
elif IIiiI == 7063 :
 i11IiII ( oo000o )
 if 17 - 17: i11iIiiIii * OOooOOo * OOooOOo + Ooo00oOo00o
elif IIiiI == 7062 :
 ii1iii1I1I ( oo000o )
 if 95 - 95: OOOo0
elif IIiiI == 7064 :
 NATatozcat ( )
 if 95 - 95: OoOO0ooOOoo0O % ii11ii1ii + OOooOOo % o0oO0
elif IIiiI == 7067 :
 Ooo0oo ( oo000o )
 if 36 - 36: O0 / i1IIi % OoOoOO00 / oO0o0ooO0
elif IIiiI == 7066 :
 NATatozA ( oo000o )
 if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
elif IIiiI == 7065 :
 IIi11IIiIii1 ( oo000o )
 if 91 - 91: OoOoOO00 . OoOO0ooOOoo0O + OOooOOo
elif IIiiI == 7070 :
 oOOo000oOoO0 ( )
 if 8 - 8: OoOO0ooOOoo0O * Oo / oO0o0ooO0 - Ooo00oOo00o - OoooooooOO
elif IIiiI == 7071 :
 DIZIlist ( oo000o )
 if 100 - 100: OoOO . iIii1I11I1II1 . iIii1I11I1II1
elif IIiiI == 7072 :
 DIZIpull ( oo000o )
 if 55 - 55: OoOO
elif IIiiI == 7073 :
 WATCHDIZI ( oo000o )
 if 37 - 37: IIII / i11iIiiIii / Oo
elif IIiiI == 7002 :
 i11I1I1iiI ( )
 if 97 - 97: O0oO . o0000oOoOoO0o / OOOo0
elif IIiiI == 7003 :
 IiiIIiiiiii ( oo000o )
 if 83 - 83: o0000oOoOoO0o - ii11ii1ii * OoOO
elif IIiiI == 7004 :
 ooOo0OoOooo00 ( oo000o )
 if 90 - 90: Oo * OOOo0
elif IIiiI == 7020 :
 Oo0OIi11 ( oo000o )
 if 75 - 75: ii11ii1ii - I1IiI * i11iIiiIii . OoooooooOO - Oo . o0000oOoOoO0o
elif IIiiI == 7001 :
 iiI1i1Iii111 ( )
 if 6 - 6: o0000oOoOoO0o * OoOO / OoooooooOO % o00O0oo * OOooOOo
elif IIiiI == 7010 :
 OO00oOooo0O ( oo000o )
 if 28 - 28: IIII * OOOo0 % IIII
elif IIiiI == 7011 :
 Ii1II ( oo000o )
 if 95 - 95: O0 / o0000oOoOoO0o . O0oO
elif IIiiI == 7012 :
 o000O0OOoo ( oo000o )
 if 17 - 17: o0000oOoOoO0o
elif IIiiI == 7013 :
 cnfTVPlay2 ( oo000o )
elif IIiiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oo000o )
elif IIiiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oo000o )
elif IIiiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oOOOo00O00oOo , oo000o , iiIIIi )
elif IIiiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IIiiI == 7018 :
 ooO000O ( )
elif IIiiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( oo000o )
elif IIiiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oo000o )
elif IIiiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( oo000o )
 if 56 - 56: o0oO0 * OOooOOo + o0000oOoOoO0o
elif IIiiI == 8000 :
 O00oO0 ( )
elif IIiiI == 8001 :
 O000Oo0o ( )
elif IIiiI == 8002 :
 OOO ( )
elif IIiiI == 8003 :
 ooOooo0 ( )
elif IIiiI == 8004 :
 o0ooO ( )
elif IIiiI == 8005 :
 OOOoO000 ( )
elif IIiiI == 8006 :
 oOOOoo ( oOOOo00O00oOo , oo000o )
elif IIiiI == 8030 :
 III1IiiI ( oo000o )
elif IIiiI == 8045 :
 ooO000OO0O00O ( )
elif IIiiI == 8046 :
 OOOoOO0o ( oo000o )
elif IIiiI == 8047 :
 O0oOo00o ( oo000o )
elif IIiiI == 8040 :
 Ii1Iii1iIi ( )
elif IIiiI == 8041 :
 OO0oo ( oo000o )
elif IIiiI == 8042 :
 i1I1i1 ( oo000o )
elif IIiiI == 8043 :
 yt . PlayVideo ( oo000o )
elif IIiiI == 8044 :
 ooo0O0o00O ( oo000o )
elif IIiiI == 8060 :
 OOo ( )
elif IIiiI == 8061 :
 ooo0OO0O0Oo ( oo000o )
elif IIiiI == 8070 :
 iiiII ( )
elif IIiiI == 8071 :
 iiIiIi ( oo000o )
elif IIiiI == 8081 :
 Oo00OoOo ( )
elif IIiiI == 8062 :
 ii1 ( oo000o )
elif IIiiI == 8063 :
 O000OOO0OOo ( oo000o )
elif IIiiI == 8050 :
 ooO ( )
elif IIiiI == 8051 :
 Ooo0oOooo0 ( oo000o )
elif IIiiI == 8052 :
 iiI1IIIi ( oo000o )
elif IIiiI == 8085 :
 I11IIIi ( )
elif IIiiI == 8086 :
 oOO0OOOo ( oo000o )
elif IIiiI == 8087 :
 I1 ( oo000o )
elif IIiiI == 8088 :
 OooooO0oOOOO ( oo000o , oOOOo00O00oOo )
elif IIiiI == 9000 :
 Ii11iII1 ( )
elif IIiiI == 1111 :
 IIIiiiI ( )
elif IIiiI == 9001 :
 II1I1I1Ii ( )
elif IIiiI == 9002 :
 OO0oOOoo ( )
elif IIiiI == 9003 :
 i1i111iI ( )
elif IIiiI == 50 :
 I1i ( oo000o )
elif IIiiI == 9020 :
 i1I1iI ( )
elif IIiiI == 9021 :
 O000o0 ( )
elif IIiiI == 9022 :
 oO0 ( )
elif IIiiI == 9023 :
 o000OoOoO0 ( )
elif IIiiI == 9024 :
 O00o00O ( oo000o )
elif IIiiI == 9030 :
 I1111I1II11 ( oo000o )
elif IIiiI == 9031 :
 iiiIIIIiIi ( oo000o )
elif IIiiI == 9032 :
 Iii ( oo000o )
elif IIiiI == 9033 :
 IIIII1iii ( oo000o )
 if 48 - 48: IIII * Ooo00oOo00o % O0oO - o0000oOoOoO0o
 if 72 - 72: i1IIi % o0oO0 % IIII % OoOO - OoOO
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
