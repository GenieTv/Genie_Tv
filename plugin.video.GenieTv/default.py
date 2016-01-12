# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
import yt
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
iIii1 = "2.3.0"
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
 if 19 - 19: o0000oOoOoO0o + o0oO0
 if 53 - 53: OoooooooOO . i1IIi
 O0O00o0OOO0 ( '[COLORgreen]SEARCH[/COLOR]' , II , 9000 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]GenieTv VOD[/COLOR]' , II , 1005 , OOooO0OOoo + 'vod.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CHAMPION IPTV[/COLOR]' , II , 9020 , OOooO0OOoo + 'UKiptvandvod.png' , ii11iIi1I , 'UK IPTV AND HD VOD' )
 if 18 - 18: OOooOOo
 if 28 - 28: OoOO0ooOOoo0O - IIII . IIII + I1IiI - OoooooooOO + O0
 O0O00o0OOO0 ( '[COLORgreen]SCRAPED MOVIES VOD[/COLOR]' , II , 7018 , OOooO0OOoo + 'MOVIESv.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , II , 1023 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]THE REAPER[/COLOR]' , II , 1016 , OOooO0OOoo + 'reap.png' , ii11iIi1I , '' )
 if 95 - 95: Ooo00oOo00o % OoOO . O0
 O0O00o0OOO0 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , II , 8040 , OOooO0OOoo + 'documentary.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CLASSIC TOONS[/COLOR]' , II , 8050 , OOooO0OOoo + 'classictoons.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]M3U STREAMS[/COLOR]' , II , 8070 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 if 15 - 15: o0oO0 / o00O0oo . o00O0oo - i1IIi
 if 53 - 53: IIII + OOOo0 * OoOO
 O0O00o0OOO0 ( '[COLORgreen]ANIME --PLEASE USE PLAYER 3 WHILE WE ATTEMPT TO CORRECT THE ISSUE--[/COLOR]' , II , 1001 , OOooO0OOoo + 'anime.png' , ii11iIi1I , 'PLEASE USE PLAYER 3 WHILE WE ATTEMPT TO CORRECT THE ISSUE' )
 O0O00o0OOO0 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , II , 3000 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 61 - 61: i1IIi * OoOO0ooOOoo0O / OoooooooOO . i11iIiiIii . I1IiI
 if 60 - 60: o0000oOoOoO0o / o0000oOoOoO0o
 if 46 - 46: o00O0oo * OoOO0ooOOoo0O - Ooo00oOo00o * OoOO - O0oO
 if 83 - 83: OoooooooOO
def Iii111II ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , II , 1026 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , II , 1024 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 if 9 - 9: Ooo00oOo00o
def i11O0oo0OO0oOOOo ( ) :
 O0O00o0OOO0 ( '[COLORgreen]Live Tv[/COLOR]' , II , 9021 , OOooO0OOoo + 'english.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]XXX[/COLOR]' , II , 9022 , OOooO0OOoo + 'xxx.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]Hd VOD[/COLOR]' , II , 9023 , OOooO0OOoo + 'vod(1).png' , ii11iIi1I , '' )
 if 35 - 35: IIII % OOOo0
 if 70 - 70: oO0o0ooO0 * ii11ii1ii
def i1II1 ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , II , 9001 , OOooO0OOoo + 'MOVIESv.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , II , 9002 , OOooO0OOoo + 'TVSHOWSv.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , II , 9003 , OOooO0OOoo + 'livetv.png' , ii11iIi1I , '' )
 if 66 - 66: OoooooooOO + o00O0oo + o00O0oo - i1IIi
def O0o0Ooo ( ) :
 O0O00o0OOO0 ( '[COLORgreen]GenieTv RADIO[/COLOR]' , II , 1013 , OOooO0OOoo + 'radio.png' , ii11iIi1I , '' )
 if 56 - 56: o0oO0 . I1IiI * oO0o0ooO0 . I1IiI
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 72 - 72: oO0o0ooO0 / i1IIi * Oo - O0oO
def Oo0O0O0ooO0O ( ) :
 IIIIii ( 'DELETE CACHE' , 'url' , 14 , OOooO0OOoo + 'MAIN5.png' , ii11iIi1I , '' )
 IIIIii ( 'DELETE PACKAGES' , 'url' , 6 , OOooO0OOoo + 'MAIN4.png' , ii11iIi1I , '' )
 IIIIii ( 'FORCE REFRESH' , 'url' , 10 , OOooO0OOoo + 'MAIN3.png' , ii11iIi1I , 'Force Refresh All Repos' )
 if 70 - 70: o00O0oo / o0000oOoOoO0o . oO0o0ooO0 % Oo
 IIIIii ( 'CHECK MY IP' , 'url' , 12 , OOooO0OOoo + 'MAIN2.png' , ii11iIi1I , '' )
 IIIIii ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , OOooO0OOoo + 'MAIN1.png' , ii11iIi1I , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0O00o0OOO0 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , II , 4 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]URL FIXES[/COLOR]' , II , 20 , OOooO0OOoo + 'URLFIX.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 67 - 67: I1IiI * OOooOOo . IIII - Ooo00oOo00o * OOooOOo
 if 46 - 46: OoOO0ooOOoo0O + I1IiI . OOOo0 * OoOO % IIII
def Oo000o ( ) :
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
 if 7 - 7: o0oO0 * Ooo00oOo00o % OoOO . IIII
 if 45 - 45: i11iIiiIii * OoOoOO00 % iIii1I11I1II1 + ii11ii1ii - o00O0oo
def iIi1iIiii111 ( ) :
 IIIIii ( 'CHECK ADVANCED XML' , II , 8 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 IIIIii ( 'MUCKYS XML' , II + '/wizard/muckys.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 IIIIii ( '0CACHE XML' , II + '/wizard/0cache.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 IIIIii ( 'MIKEY1234 XML' , II + '/wizard/mikey.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 IIIIii ( 'TUXENS XML' , II + '/wizard/tuxens.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 IIIIii ( 'P2P RECOMMENDED XML1' , II + '/wizard/p2p1.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 IIIIii ( 'P2P RECOMMENDED XML2' , II + '/wizard/p2p2.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 IIIIii ( 'DELETE XML' , II , 11 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 16 - 16: ii11ii1ii + Ooo00oOo00o - OoOoOO00
def oOoOO0 ( ) :
 IIIIii ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 IIIIii ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 if 30 - 30: OoOoOO00 - OoOO0ooOOoo0O - i11iIiiIii % I1IiI - OoOoOO00 * o00O0oo
def oO00O0O0O ( ) :
 IIIIii ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , II + '/wizard/customftv/ftvguide-addons.zip' , 5 , OOooO0OOoo + 'FTV4.png' , ii11iIi1I , '' )
 IIIIii ( 'FTV GUIDE FIRST RUN SETTINGS' , II + '/wizard/customftv/settings.xml' , 17 , OOooO0OOoo + 'FTV3.png' , ii11iIi1I , '' )
 IIIIii ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , OOooO0OOoo + 'FTV1.png' , ii11iIi1I , '' )
 IIIIii ( 'RESET FTV DATABASE' , 'url' , 18 , OOooO0OOoo + 'FTV2.png' , ii11iIi1I , '' )
 if 31 - 31: o0000oOoOoO0o - OoOoOO00 . o0000oOoOoO0o
 if 18 - 18: OOooOOo
 if 98 - 98: oO0o0ooO0 * oO0o0ooO0 / oO0o0ooO0 + o0000oOoOoO0o
def ii111111I1iII ( ) :
 O0O00o0OOO0 ( '[COLORgreen]SKINS[/COLOR]' , II , 33 , OOooO0OOoo + 'skinp.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , II , 34 , OOooO0OOoo + 'artp.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , i1iIIi1 , 35 , OOooO0OOoo + 'GUI.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 68 - 68: oO0o0ooO0 - iIii1I11I1II1 * i11iIiiIii / ii11ii1ii * O0oO
def i1iIi1iIi1i ( url ) :
 I1I1iIiII1 = i11i1I1 ( ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 5 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 7 - 7: OoOO0ooOOoo0O + O0oO + O0
def Ii ( ) :
 O0O00o0OOO0 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , II , 36 , OOooO0OOoo + 'GSKIN.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]HELIX SKINS[/COLOR]' , II , 37 , OOooO0OOoo + 'HSKIN.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , i1iIIi1 , 38 , OOooO0OOoo + 'ISKIN.png' , ii11iIi1I , '' )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 64 - 64: o0oO0 / I1IiI - O0 - o0000oOoOoO0o
def O0oOoOOOoOO ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + ii1ii11IIIiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 67 - 67: o0000oOoOoO0o * OoOO * ii11ii1ii + OoOO0ooOOoo0O / i1IIi
def I1I111 ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + Oo00oo0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 1 - 1: Ooo00oOo00o - OoOO . o0000oOoOoO0o . Ooo00oOo00o / Oo + o0000oOoOoO0o
def OooOOOOo ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + oo0O0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 60 - 60: OOOo0
def iii1i ( url ) :
 I1I1iIiII1 = i11i1I1 ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 39 - 39: oO0o0ooO0 - O0 % i11iIiiIii * O0oO . IIII
def OOooo0O00o ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + oOOoOooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 40 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 51 - 51: o0000oOoOoO0o + oO0o0ooO0 % iIii1I11I1II1 / OoOO / OoOO0ooOOoo0O % OoooooooOO
def o0O0OOO0Ooo ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + iiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 5 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 6 - 6: IIII . OoOO * I1IiI - o00O0oo - IIII
def IiIiii1I1 ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 2031 , OOooO0OOoo + 'APK.png' )
  if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * oO0o0ooO0 % i11iIiiIii * OOOo0
def oo000o ( name , url , description ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( o0OoOO000ooO0 , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 o0o0o0oO0oOO = os . path . join ( iiIi1IIi1I , name + '.apk' )
 try :
  os . remove ( o0o0o0oO0oOO )
 except :
  pass
 downloader . download ( url , o0o0o0oO0oOO , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 3 - 3: OOooOOo
def Ii11I1 ( url ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 o0o0o0oO0oOO = os . path . join ( iiIi1IIi1I , Ii1i1 + '.mp4' )
 try :
  os . remove ( o0o0o0oO0oOO )
 except :
  pass
 downloader . download ( url , o0o0o0oO0oOO , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 14 - 14: OoOO0ooOOoo0O % iIii1I11I1II1
 if 71 - 71: O0 . oO0o0ooO0 / OOooOOo
def OooiIi1IiIiiII ( name , url , description ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 o0o0o0oO0oOO = os . path . join ( iiIi1IIi1I , name )
 try :
  os . remove ( o0o0o0oO0oOO )
 except :
  pass
 downloader . download ( url , o0o0o0oO0oOO , i1111 )
 ii1iII1II = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ii1iII1II
 print '======================================='
 extract . all ( o0o0o0oO0oOO , ii1iII1II , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 48 - 48: OoOoOO00 * o00O0oo . o0000oOoOoO0o + OoOO
 if 78 - 78: i11iIiiIii / oO0o0ooO0 - o00O0oo / OoOO0ooOOoo0O + OoOO
def oOoooo0O0Oo ( url ) :
 I1I1iIiII1 = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 5 , iiIii , ooo0O , oOoO0o00OO0 )
 try :
  I1I1iIiII1 = i11i1I1 ( o00ooO + oooOOOOO + OO0OO0O00oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
  for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
   O0O00o0OOO0 ( Ii1i1 , url , 5 , iiIii , ooo0O , oOoO0o00OO0 )
 except : pass
 o0oo0o0O00OO ( 'movies' , 'INFO' )
 if 55 - 55: OoOO0ooOOoo0O . OOOo0
 if 61 - 61: Oo % IIII . Oo
def o0oOO000oO0oo ( url ) :
 I1I1iIiII1 = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 43 , iiIii , ooo0O , oOoO0o00OO0 )
 try :
  I1I1iIiII1 = i11i1I1 ( o00ooO + oooOOOOO + OO0OO0O00oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
  for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
   O0O00o0OOO0 ( Ii1i1 , url , 43 , iiIii , ooo0O , oOoO0o00OO0 )
 except : pass
 o0oo0o0O00OO ( 'movies' , 'INFO' )
 if 78 - 78: ii11ii1ii + OoOO0ooOOoo0O - O0oO
 if 38 - 38: OOooOOo - OoOO + iIii1I11I1II1 / I1IiI % Oo
def oO0o0 ( name , url , description ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o0o0o0oO0oOO = os . path . join ( iiIi1IIi1I , name + '.zip' )
 try :
  os . remove ( o0o0o0oO0oOO )
 except :
  pass
 downloader . download ( url , o0o0o0oO0oOO , i1111 )
 iI1Ii11iIiI1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iI1Ii11iIiI1
 print '======================================='
 extract . all ( o0o0o0oO0oOO , iI1Ii11iIiI1 , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OO0Oooo0oOO0O ( )
 if 62 - 62: OOOo0
 if 100 - 100: o00O0oo - O0 % OoOO * OoOO0ooOOoo0O + OOOo0
def Oo0O0oooo ( name , url , description ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o0o0o0oO0oOO = os . path . join ( iiIi1IIi1I , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o0o0o0oO0oOO )
 except :
  pass
 downloader . download ( url , o0o0o0oO0oOO , i1111 )
 iI1Ii11iIiI1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iI1Ii11iIiI1
 print '======================================='
 extract . all ( o0o0o0oO0oOO , iI1Ii11iIiI1 , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 I111iI ( )
 if 56 - 56: OOOo0
def O0oOOO0ooOOO0OOO ( name , url , description ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o0o0o0oO0oOO = os . path . join ( iiIi1IIi1I , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o0o0o0oO0oOO )
 except :
  pass
 downloader . download ( url , o0o0o0oO0oOO , i1111 )
 iI1Ii11iIiI1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iI1Ii11iIiI1
 print '======================================='
 extract . all ( o0o0o0oO0oOO , iI1Ii11iIiI1 , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 63 - 63: I1IiI * oO0o0ooO0
 if 69 - 69: O0 . Ooo00oOo00o
def ii1111iII ( name , url , description ) :
 iI1Ii11iIiI1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 o0o0o0oO0oOO = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print iI1Ii11iIiI1
 print '======================================='
 extract . all ( o0o0o0oO0oOO , iI1Ii11iIiI1 , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 32 - 32: i1IIi / OoOoOO00 . Oo
 if 62 - 62: OoooooooOO * OOOo0
def I111iI ( ) :
 oOOOoo0O0oO = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oOOOoo0O0oO == 0 :
  return
 elif oOOOoo0O0oO == 1 :
  pass
 iIII1I111III = IIo0o0O0O00oOOo ( )
 print "Platform: " + str ( iIII1I111III )
 if iIII1I111III == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIII111ii . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIII1I111III == 'linux' :
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
 elif iIII1I111III == 'android' :
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
 elif iIII1I111III == 'windows' :
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
  if 14 - 14: I1IiI + OoOO
def IIo0o0O0O00oOOo ( ) :
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
  if 52 - 52: OoooooooOO - o0oO0
  if 74 - 74: oO0o0ooO0 + OOooOOo
  if 71 - 71: Oo % OoOO0ooOOoo0O
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
 I111iI ( )
 if 72 - 72: OoOoOO00 + i1IIi + OOooOOo
def OOO ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 Oo0ooOo0o = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( oOOO )
 for Ii1i1 , o0o in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , o0o , 222 , OOooO0OOoo + 'radio.png' )
  if 56 - 56: O0oO + I1IiI * o0oO0 / OoOO / O0 * ii11ii1ii
def O0o0o00OO0000 ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , 'http://www.toonjet.com/' + o0o , 8051 , OOooO0OOoo + 'classictoons.png' )
def I1i ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( oOOO )
 O00Oooo = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( oOOO )
 for url , i11I in Oo0ooOo0o :
  if 'ol.gif' in i11I :
   pass
  elif 'link_block_' in i11I :
   pass
  elif '.png' in i11I :
   pass
  else :
   I1111IIIIIi ( ( i11I ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , OOooO0OOoo + 'vod.png' )
 for url in O00Oooo :
  I1111IIIIIi ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , OOooO0OOoo + 'documentary.png' )
def o00Oo0oooooo ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  IIiI1i1i ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , OOooO0OOoo + 'classictoons.png' )
  if 76 - 76: o0000oOoOoO0o / OoOO0ooOOoo0O . O0 % OOOo0 . OOooOOo + IIII
def o0ooo0 ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 8041 , OOooO0OOoo + 'documentary.png' )
def oOOOoo00 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( oOOO )
 O00Oooo = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( oOOO )
 for url , Ii1i1 , i11I in Oo0ooOo0o :
  I1111IIIIIi ( ( Ii1i1 ) . replace ( '&#039;s' , '' ) , url , 8042 , i11I )
 for url in O00Oooo :
  I1111IIIIIi ( 'NEXT PAGE' , url , 8041 , OOooO0OOoo + 'documentary.png' )
  if 9 - 9: O0 % O0 - OOooOOo
  if 51 - 51: OOOo0 . iIii1I11I1II1 - ii11ii1ii / O0
def OOOoO00 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( oOOO )
 O00Oooo = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( oOOO )
 for Ii1i1 , i11I , url , IIiIi11i1i in Oo0ooOo0o :
  IIiI1i1i ( ( Ii1i1 ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , i11I )
 for url in O00Oooo :
  I1II1I11I1I ( ( url ) . replace ( '//' , 'http://' ) )
  if 54 - 54: OoooooooOO + OOooOOo - i1IIi % i11iIiiIii
def I1II1I11I1I ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  IIiI1i1i ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOooO0OOoo + 'documentary.png' )
  if 3 - 3: OOooOOo % OOooOOo
def oo00o0 ( ) :
 IiiiiI1i1Iii = iIII1 ( 'http://www.stream2watch.co/live-tv' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 for o0o , i11I , Ii1i1 , oo00oO0o in Oo0ooOo0o :
  I1111IIIIIi ( ( Ii1i1 + '[COLORgreen]' + oo00oO0o + '[/COLOR]' ) , o0o , 8086 , i11I )
  if 31 - 31: OoOO0ooOOoo0O
def i1OOO0000oO ( url ) :
 IiiiiI1i1Iii = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 for url , i11I , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , url , 8087 , i11I )
  if 15 - 15: I1IiI % OOOo0 * o0000oOoOoO0o
def O0OoooO0 ( url ) :
 IiiiiI1i1Iii = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 for url , Ii1i1 in Oo0ooOo0o :
  ooo0O0o00O ( url , Ii1i1 )
  if 48 - 48: o0oO0 / O0oO . iIii1I11I1II1 * I1IiI * OoOO / i1IIi
def ooo0O0o00O ( url , name ) :
 IiiiiI1i1Iii = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 for url in Oo0ooOo0o :
  print url
  IIiI1i1i ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 92 - 92: Oo % Oo - OOooOOo / I1IiI
def I11IIIi ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 Oo0ooOo0o = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( oOOO )
 for i11I , time , iIIiiI1II1i11 , o0o0 , IIii1111 , o0o in Oo0ooOo0o :
  I1111IIIIIi ( ( time + '[COLORgreen]' + IIii1111 + '[/COLOR]' + o0o0 ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , o0o , 8061 , i11I )
def I1iI ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  IIiI1i1i ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , OOooO0OOoo + 'documentary.png' )
  if 38 - 38: OoOO % I1IiI + ii11ii1ii . i11iIiiIii
def oo0000ooooO0o ( ) :
 IiiiiI1i1Iii = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby9pcHR2Lw==' ) )
 Oo0ooOo0o = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?"/></a></div>.+?<a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>.+?<time  itemprop="dateCreated" class="entry-date updated td-module-date" datetime=".+?" >(.+?)</time>' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 O00Oooo = re . compile ( 'href="(.+?)" class="page" title="(.+?)">.+?</a><a' ) . findall ( IiiiiI1i1Iii )
 for i11I , o0o , Ii1i1 , iI1i11 in Oo0ooOo0o :
  I1111IIIIIi ( ( iI1i11 + '-' + Ii1i1 ) . replace ( '&#038;' , '' ) , o0o , 8071 , i11I )
 for o0o , Ii1i1 in O00Oooo :
  I1111IIIIIi ( '[COLORgreen]PAGE [/COLOR]' + Ii1i1 , o0o , 8070 , i11I )
  if 66 - 66: O0 % ii11ii1ii + i11iIiiIii . I1IiI / o00O0oo + ii11ii1ii
def ooo00Ooo ( url ) :
 IiiiiI1i1Iii = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '#EXTINF:-1,(.+?)<br />\n(.+?)<br />' ) . findall ( IiiiiI1i1Iii )
 for Ii1i1 , url in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 222 , OOooO0OOoo + 'streams.png' )
  if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * o0000oOoOoO0o % O0 + OoooooooOO
def I1i1i1 ( url ) :
 OoO0O00O0oo0O = urllib2 . Request ( url )
 OoO0O00O0oo0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IiI11 = ''
 I1I1iIiII1 = ''
 try :
  I1IiI11 = urllib2 . urlopen ( OoO0O00O0oo0O )
  I1I1iIiII1 = I1IiI11 . read ( )
  I1IiI11 . close ( )
 except : pass
 if I1I1iIiII1 != '' :
  return I1I1iIiII1
 else :
  I1I1iIiII1 = 'Failed'
  return I1I1iIiII1
  if 9 - 9: o0000oOoOoO0o
def OoooO ( ) :
 iIII = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIi = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111I = iIi . lower ( )
 o0o = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 iiI = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 iIiiiII = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1iI1 = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 i11ii1ii11i = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 ooO0OoOO = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 if 55 - 55: o0oO0 - o0000oOoOoO0o + OoOoOO00 + oO0o0ooO0 % o00O0oo
 IiiiiI1i1Iii = I1i1i1 ( o0o )
 iiI11i1II = I1i1i1 ( iiI )
 OO0O0OOo0O = I1i1i1 ( iIiiiII )
 I1 = I1i1i1 ( i1iI1 )
 o0OooOOOOOO = I1i1i1 ( i11ii1ii11i )
 if 78 - 78: OOOo0 - iIii1I11I1II1 . o0oO0 + iIii1I11I1II1
 if IiiiiI1i1Iii != 'Failed' :
  Oo0ooOo0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
  for oOoOO , Ii1i1 in Oo0ooOo0o :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0o + oOoOO ) , 222 , '' )
 if iiI11i1II != 'Failed' :
  O00Oooo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iiI11i1II )
  for oOoOO , Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiI + oOoOO ) , 222 , '' )
 if OO0O0OOo0O != 'Failed' :
  Ii1i1O0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OO0O0OOo0O )
  for oOoOO , Ii1i1 in Ii1i1O0o :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIiiiII + oOoOO ) , 222 , '' )
 if I1 != 'Failed' :
  i1iIiIIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1 )
  for oOoOO , Ii1i1 in i1iIiIIi :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1iI1 + oOoOO ) , 222 , '' )
 if o0OooOOOOOO != 'Failed' :
  oO0o00oo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0OooOOOOOO )
  for oOoOO , i11I , Ii1i1 in oO0o00oo0 :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + '[COLORgreen] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOoOO ) , 1006 , 'img' )
    if 19 - 19: OoOoOO00 + IIII
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 OOOO0O00o = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 62 - 62: iIii1I11I1II1
 if 12 - 12: OoOO0ooOOoo0O / OOooOOo
 for iiI1I1 in OOOO0O00o :
  ooO = iIII + iiI1I1
  ii = I1i1i1 ( ooO )
  if o0OooOOOOOO != 'Failed' :
   OO0O0Ooo = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( ii )
   for oOoOO , Ii1i1 in OO0O0Ooo :
    if iIi in Ii1i1 . lower ( ) :
     IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iIII + iiI1I1 + oOoOO ) , 222 , '' )
     if 77 - 77: OOooOOo / OoooooooOO
     o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
     if 46 - 46: OOooOOo % iIii1I11I1II1 . oO0o0ooO0 % oO0o0ooO0 + i11iIiiIii
     if 72 - 72: iIii1I11I1II1 * o00O0oo % o0oO0 / Ooo00oOo00o
def I11i1II ( ) :
 if 72 - 72: iIii1I11I1II1 . i1IIi / Oo . OoOoOO00
 iIi = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111I = iIi . lower ( )
 o0o = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 iiI = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 iIiiiII = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 i1iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 i11ii1ii11i = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIi ) . replace ( ' ' , '+' )
 ooO0OoOO = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 if 54 - 54: OoOoOO00 % OoOoOO00
 IiiiiI1i1Iii = I1i1i1 ( o0o )
 iiI11i1II = I1i1i1 ( iiI )
 OO0O0OOo0O = I1i1i1 ( iIiiiII )
 I1 = I1i1i1 ( i1iI1 )
 o0OooOOOOOO = I1i1i1 ( i11ii1ii11i )
 ii = I1i1i1 ( ooO0OoOO )
 if IiiiiI1i1Iii != 'Failed' :
  Oo0ooOo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiiiiI1i1Iii )
  for Ii1i1 in Oo0ooOo0o :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0o + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 86 - 86: O0 % o00O0oo * o0oO0 * iIii1I11I1II1 * i1IIi * o0000oOoOoO0o
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if iiI11i1II != 'Failed' :
  O00Oooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI11i1II )
  for Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiI + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 83 - 83: I1IiI % OoOoOO00 - I1IiI + IIII - O0
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OO0O0OOo0O != 'Failed' :
  Ii1i1O0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0O0OOo0O )
  for Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiiiII + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 52 - 52: Oo * o0oO0
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  i1iIiIIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1iI1 + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 33 - 33: o00O0oo
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if o0OooOOOOOO != 'Failed' :
  oO0o00oo0 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0OooOOOOOO )
  for o0o , i11I , Ii1i1 in oO0o00oo0 :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( Ii1i1 + ' - Source - Origin' , o0o , 8062 , i11I )
    if 74 - 74: OoOO0ooOOoo0O + O0 + i1IIi - i1IIi + OoOoOO00
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if ii != 'Failed' :
  OO0O0Ooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ii )
  for o0o , i11I , Ii1i1 in OO0O0Ooo :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source Scooby[/COLOR]' ) , o0o , 222 , 'img' )
    if 83 - 83: ii11ii1ii - OOOo0 + OoOO0ooOOoo0O
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
def iIi1Ii1i1iI ( ) :
 if 16 - 16: OoOO0ooOOoo0O / Oo / OoooooooOO * OOOo0 + i1IIi % OoOO0ooOOoo0O
 iIi = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111I = iIi . lower ( )
 o0o = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IiiiiI1i1Iii = i11i1I1 ( o0o )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 for Ii1i1 , i11I , ooo0o00 in Oo0ooOo0o :
  ooOo0o00 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11I ) . replace ( '\\' , '' )
  if iIi in Ii1i1 . lower ( ) :
   I1111IIIIIi ( Ii1i1 , '' , 7022 , ooOo0o00 )
   if 14 - 14: OOooOOo . OoOO0ooOOoo0O . o0000oOoOoO0o + OoooooooOO - OoOO0ooOOoo0O + IIII
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: o00O0oo
 if 59 - 59: OOOo0 * OoOoOO00 . O0
def O000OoOO0 ( url ) :
 IiiiiI1i1Iii = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for url , i1IiIII111i1 , o000ooooo0 , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( ( i1IiIII111i1 ) . replace ( 'Sezon' , ' Season ' ) + ( o000ooooo0 ) . replace ( 'Bölüm' , ' Episode ' ) + Ii1i1 , url , 8063 , '' )
  if 51 - 51: Ooo00oOo00o - O0 % OoOO - OoOoOO00
  if 31 - 31: oO0o0ooO0 / Oo - oO0o0ooO0 - OoOO0ooOOoo0O
  if 7 - 7: oO0o0ooO0 % O0 . I1IiI + OOOo0 - o0000oOoOoO0o
  if 75 - 75: o0000oOoOoO0o
def oO00oo0o00o0o ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 222 , '' )
  if 7 - 7: O0 - Oo + ii11ii1ii + OoOoOO00 + iIii1I11I1II1
  if 58 - 58: OOooOOo / IIII . I1IiI / OoooooooOO + O0oO
  if 86 - 86: o0000oOoOoO0o * OOOo0 + o0000oOoOoO0o + OoOoOO00
  if 8 - 8: O0oO - oO0o0ooO0 / o0oO0
def oo0oOoo ( ) :
 if 57 - 57: I1IiI - ii11ii1ii
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Oo0ooOo0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oOOO )
 for o0o , i11I , Ii1i1 , o000ooooo0 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 + '  -  ' + ( o000ooooo0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o0o , 8063 , i11I )
  if 50 - 50: O0oO / i1IIi % Ooo00oOo00o . OOOo0 / oO0o0ooO0
def OO ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oOOO )
 for o0o , Ii1i1 , i11I in Oo0ooOo0o :
  IIiI1i1i ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , o0o , 8002 , i11I )
def OOo ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oOOO )
 for i11I , time , url , Ii1i1 , IIiIi11i1i in Oo0ooOo0o :
  O0O00o0OOO0 ( '%s %s' % ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , time ) , url , 1015 , i11I , IIiIi11i1i )
  if 50 - 50: o0oO0
def o0O0O0ooo0oOO ( ) :
 if 97 - 97: OOOo0 / oO0o0ooO0
 I1111IIIIIi ( 'Coronation Street' , '' , 8001 , '' )
 I1111IIIIIi ( 'Eastenders' , '' , 8002 , '' )
 I1111IIIIIi ( 'Emmerdale' , '' , 8003 , '' )
 I1111IIIIIi ( 'Hollyoaks' , '' , 8004 , '' )
 I1111IIIIIi ( 'Im a Celebrity' , '' , 8005 , '' )
 if 71 - 71: OoOoOO00 / i1IIi . ii11ii1ii % OoooooooOO . I1IiI
 if 41 - 41: i1IIi * OoOoOO00 / OoooooooOO . OoOO0ooOOoo0O
 if 83 - 83: oO0o0ooO0 . O0 / Oo / OoOO0ooOOoo0O - OoOoOO00
 if 100 - 100: Ooo00oOo00o
def II1i ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Holly' in Ii1i1 :
   i11I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 2 - 2: iIii1I11I1II1 * Oo % OoOO - OoOoOO00 - oO0o0ooO0
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 3 - 3: O0oO
def i1iiIiI1Ii1i ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'East' in Ii1i1 :
   i11I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 22 - 22: IIII / i11iIiiIii
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
def ii1 ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Emmer' in Ii1i1 :
   i11I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 53 - 53: o00O0oo % o00O0oo * OOooOOo + I1IiI
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: OoooooooOO + i1IIi / o00O0oo * O0
def O00oOo00o0o ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Coro' in Ii1i1 :
   i11I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 85 - 85: oO0o0ooO0 + OoooooooOO * oO0o0ooO0 - O0oO % i11iIiiIii
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: ii11ii1ii - o0oO0 / I1IiI * I1IiI / i1IIi . i1IIi
def ooo000ooO0000 ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Celeb' in Ii1i1 :
   i11I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 97 - 97: Oo * OOOo0 . iIii1I11I1II1
def I1Ii1111iIi ( name , url ) :
 I11o0oO00oO0o0o0 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if I11o0oO00oO0o0o0 :
  I1I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oOOO = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( oOOO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oOOO = open_url ( url )
  ooooo = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( oOOO ) [ - 1 ]
  I1I = ooooo . replace ( '\\/' , '/' )
 i11IIIiI1I = xbmcgui . ListItem ( name , '' , '' )
 i11IIIiI1I . setPath ( I1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11IIIiI1I )
 if 69 - 69: O0
 if 85 - 85: o0oO0 / O0
 if 18 - 18: OOooOOo % O0 * ii11ii1ii
 if 62 - 62: O0oO . IIII . OoooooooOO
def i111 ( ) :
 if 27 - 27: i11iIiiIii / ii11ii1ii
 I1111IIIIIi ( 'All Channels' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Entertainment' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Movies' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Music' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'News' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Sports' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Documentary' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Kids' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Food' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Religious' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'USA Channels' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 I1111IIIIIi ( 'Other' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 if 84 - 84: Oo
 if 43 - 43: OoOO - OoooooooOO
def ii1iI ( Cat_Name ) :
 if 49 - 49: OOooOOo . IIII / Ooo00oOo00o + OoOoOO00
 ii11i = False
 III11II1I1Ii1 = '0'
 if Cat_Name == 'All Channels' : ii11i = True
 if Cat_Name == 'Entertainment' : III11II1I1Ii1 = '1'
 if Cat_Name == 'Movies' : III11II1I1Ii1 = '2'
 if Cat_Name == 'Music' : III11II1I1Ii1 = '3'
 if Cat_Name == 'News' : III11II1I1Ii1 = '4'
 if Cat_Name == 'Sports' : III11II1I1Ii1 = '5'
 if Cat_Name == 'Documentary' : III11II1I1Ii1 = '6'
 if Cat_Name == 'Kids' : III11II1I1Ii1 = '7'
 if Cat_Name == 'Food' : III11II1I1Ii1 = '8'
 if Cat_Name == 'Religious' : III11II1I1Ii1 = '9'
 if Cat_Name == 'USA Channels' : III11II1I1Ii1 = '10'
 if Cat_Name == 'Other' : III11II1I1Ii1 = '11'
 if 72 - 72: oO0o0ooO0 * OoOO % o00O0oo . OoooooooOO
 oOOO = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oOOO )
 print 'Len Match: >>>' + str ( len ( Oo0ooOo0o ) )
 for Ii1i1 , i11I , ooo0o00 in Oo0ooOo0o :
  ooOo0o00 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11I ) . replace ( '\\' , '' )
  if ooo0o00 == III11II1I1Ii1 :
   I1111IIIIIi ( Ii1i1 , '' , 7022 , ooOo0o00 )
  elif ii11i == True :
   I1111IIIIIi ( Ii1i1 , '' , 7022 , ooOo0o00 )
  else : pass
  if 99 - 99: iIii1I11I1II1 % o0oO0 + o0oO0 + oO0o0ooO0 - O0oO / O0oO
  xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 7 - 7: OOOo0 + I1IiI / IIII
def OOOoO000 ( Search_Name ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOOO )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOOO )
 for i11I , o0o , iiI , iIiiiII in Oo0ooOo0o :
  ooOo0o00 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11I ) . replace ( '\\' , '' )
  IIiI1i1i ( Search_Name + ': Link 1' , ( o0o ) . replace ( '\\' , '' ) , 222 , ooOo0o00 )
  IIiI1i1i ( Search_Name + ': Link 2' , ( iiI ) . replace ( '\\' , '' ) , 222 , ooOo0o00 )
  IIiI1i1i ( Search_Name + ': Link 3' , ( iIiiiII ) . replace ( '\\' , '' ) , 222 , ooOo0o00 )
  if 57 - 57: OoOoOO00
def oOOOoo ( ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Oo0ooOo0o = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oOOO )
 for Ii1i1 , o0o in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , ( o0o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'english.png' )
def Ii1ii111i1 ( ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Oo0ooOo0o = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oOOO )
 for Ii1i1 , o0o in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , ( o0o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'xxx.png' )
def i1i1i1I ( ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Oo0ooOo0o = re . compile ( '#EXTINF:-3group-title="HD MOVIES ON DEMAND",(.+)\s*(.+)\s*' ) . findall ( oOOO )
 for Ii1i1 , o0o in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , ( o0o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'vod(1).png' )
  if 83 - 83: OoOO + OoooooooOO
def I111IiiIi1 ( url ) :
 url
 o00o = xbmcgui . ListItem ( Ii1i1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o00o )
 return
 if 46 - 46: OoOoOO00 % OOooOOo % iIii1I11I1II1 - Oo . OoooooooOO - IIII
 if 59 - 59: IIII . OoOO0ooOOoo0O % OoOoOO00
def i11I1iIi ( ) :
 oOOO = i11i1I1 ( 'http://tvshows.cnfstudio.com/' )
 Oo0ooOo0o = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , 'http://tvshows.cnfstudio.com/genre/' + o0o , 7010 , OOooO0OOoo + 'icon.png' )
  print '>>>>>>>>>>' + o0o
  if 79 - 79: O0oO . OoOO - OoOoOO00 . OOOo0 % o0oO0
def oOoO00 ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oOOO )
 iI1IIIii = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( oOOO )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oOOO )
 for i11I , url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( ( Ii1i1 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , i11I )
 iI1IIIii = iI1IIIii
 for url in iI1IIIii :
  I1111IIIIIi ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  I1111IIIIIi ( 'Next' , url , 7010 , '' )
  if 7 - 7: IIII - o0000oOoOoO0o / OoOoOO00 * o00O0oo . oO0o0ooO0 * oO0o0ooO0
def O0O0oOOo0O ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( oOOO )
 for url , o000ooooo0 , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( ( 'Season' ) + o000ooooo0 + ( '  ' ) + Ii1i1 , url , 7004 , OOooO0OOoo + 'icon.png' )
  if 19 - 19: OOooOOo / O0oO % OOooOOo % oO0o0ooO0 * IIII
def ii1oOoO0o0ooo ( url ) :
 if 86 - 86: ii11ii1ii * O0 * IIII
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOooO0OOoo + 'icon.png' )
  if 51 - 51: OoOoOO00 + IIII . i1IIi . ii11ii1ii + I1IiI * OOOo0
def OOoOoo0 ( name , url , img ) :
 IiiiiI1i1Iii = i11i1I1 ( url )
 I1iIII1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 iIii = len ( I1iIII1 )
 if 84 - 84: OoOO % i1IIi
 if 70 - 70: Oo . OoooooooOO - oO0o0ooO0
 if iIii == 1 :
  for iII11I1Ii1 in I1iIII1 :
   iII11I1Ii1 = iII11I1Ii1 . replace ( 'player' , 'watch' )
   o0o0oOo0oO = iII11I1Ii1 + '&fv=&sou='
   IIi1IIIIi = i11i1I1 ( o0o0oOo0oO )
   OOOoO = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( IIi1IIIIi )
   for I1iiiiI in OOOoO :
    IiIi1 = False
    Resolve ( I1iiiiI )
    if 34 - 34: OoOO0ooOOoo0O
 elif iIii > 1 :
  if 91 - 91: iIii1I11I1II1 % OOooOOo . iIii1I11I1II1 % i1IIi / OoOoOO00 * I1IiI
  for iII11I1Ii1 in I1iIII1 :
   iioo0o0OoOOO = i11i1I1 ( iII11I1Ii1 )
   ooO0oO00O0o = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iioo0o0OoOOO )
   ooOO00oOOo000 = ooO0oO00O0o
   ooOO00oOOo000 = ( str ( ooOO00oOOo000 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ooOO00oOOo000
   IIiI1i1i ( 'DOUBLE LINK' , ooOO00oOOo000 , 424 , '' )
   if 14 - 14: Ooo00oOo00o . OoOoOO00 . o0000oOoOoO0o / o00O0oo % ii11ii1ii - o0oO0
   for url in ooO0oO00O0o :
    I1111IIIIIi ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iiI = Google . resolve ( url )
    except :
     pass
    try :
     o0oOoO0O = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iiI ) )
     for OoOo000oOo0oo , oO0O in o0oOoO0O :
      if 86 - 86: I1IiI . iIii1I11I1II1 - Ooo00oOo00o
      HD_URLS . append ( OoOo000oOo0oo )
      SD_URLS . append ( oO0O )
    except :
     pass
 else :
  pass
  if 56 - 56: O0
def OOo00 ( ) :
 if 37 - 37: i1IIi
 if 46 - 46: I1IiI - o0000oOoOoO0o - o00O0oo . i1IIi
 I1111IIIIIi ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOooO0OOoo + 'Movies.png' )
 if 35 - 35: OoOoOO00 * o0000oOoOoO0o - OoooooooOO . o0000oOoOoO0o . o0000oOoOoO0o
 I1111IIIIIi ( 'Search Movies' , '' , 7017 , OOooO0OOoo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 11 - 11: O0oO / I1IiI + o0000oOoOoO0o % iIii1I11I1II1
 if 42 - 42: ii11ii1ii * I1IiI % o0oO0 - I1IiI . i11iIiiIii - O0oO
def o0oO0oOO ( ) :
 oOOO = i11i1I1 ( 'http://cnfstudio.com/' )
 Oo0ooOo0o = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , 'http://cnfstudio.com/genre/' + o0o , 7003 , OOooO0OOoo + 'icon.png' )
  if 89 - 89: o0oO0 + o00O0oo * o0oO0 / o0oO0
i1iiIII111ii = xbmcgui . Dialog ( )
if 46 - 46: Ooo00oOo00o
if 71 - 71: o0000oOoOoO0o / o0000oOoOoO0o * OoOO * OoOO / OoOoOO00
def II1I1iiIII1I1 ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oOOO )
 iI1IIIii = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oOOO )
 for i11I , url , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( ( Ii1i1 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , i11I )
 iI1IIIii = iI1IIIii
 for url in iI1IIIii :
  I1111IIIIIi ( 'Next Page' , url , 7003 , '' )
  if 85 - 85: oO0o0ooO0 * OOooOOo
def ii1iii11i1 ( url ) :
 if 4 - 4: IIII . IIII % ii11ii1ii % o00O0oo / o00O0oo
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  I1I1iIiII1 = url + '&fv=&sou='
  I1I1iIiII1 = I1I1iIiII1 . replace ( 'player' , 'watch' )
  II11iIiiI1111 = OOO00oo0ooO ( I1I1iIiII1 )
  iiIii1ii = OOO00oo0ooO ( url )
  if 33 - 33: O0oO
  if 62 - 62: ii11ii1ii + o00O0oo + i1IIi / OoooooooOO
def OOO00oo0ooO ( url ) :
 if 7 - 7: OOooOOo + i1IIi . OOOo0 / Oo
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  I111i1I1 ( url )
  if 62 - 62: OoOO0ooOOoo0O * O0oO / Oo * OOooOOo
  if 29 - 29: Oo % Ooo00oOo00o % IIII . OOooOOo / OoooooooOO * o0oO0
def o0 ( ) :
 O0O00o0OOO0 ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 78 - 78: iIii1I11I1II1 + o0000oOoOoO0o - o00O0oo * O0oO - OoooooooOO % I1IiI
def i1OoOO ( url ) :
 Oo0ooOo0o = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for iIII1I1i1i , Ii1i1 , url in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 222 , OOooO0OOoo + 'streams.png' )
  if 79 - 79: o00O0oo . Ooo00oOo00o
  if 40 - 40: OOooOOo + Oo . OOooOOo % o0oO0
def I11I1IIiiII1 ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1007 , O0OOoO00OO0o )
def IIIIIii1ii11 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , url , 1006 , O0OOoO00OO0o )
  if 86 - 86: I1IiI * OoOoOO00 - O0 . I1IiI % iIii1I11I1II1 / OoOO0ooOOoo0O
def IiIIiIIIiIii ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1027 , O0OOoO00OO0o )
  if 23 - 23: oO0o0ooO0 + o0000oOoOoO0o . I1IiI * OOOo0 + ii11ii1ii
def I1iIi1iiiIiI ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 1028 , O0OOoO00OO0o )
def III1I1Ii11iI ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 333 , O0OOoO00OO0o )
def oO00OoOO ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 404 , O0OOoO00OO0o )
  if 18 - 18: o0oO0 - I1IiI % i1IIi + O0 + i11iIiiIii + i1IIi
def oOo0o0O ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1017 , O0OOoO00OO0o )
  if 83 - 83: OOooOOo / OoOO0ooOOoo0O / OoOO0ooOOoo0O + OOooOOo * O0oO + OOooOOo
def IIIIiii ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 1018 , O0OOoO00OO0o )
def oO0o ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 333 , O0OOoO00OO0o )
def IIIii1iiIi ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 404 , O0OOoO00OO0o )
  if 63 - 63: ii11ii1ii
def i1II ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1007 , O0OOoO00OO0o )
def IiiI11i1I ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , url , 1006 , O0OOoO00OO0o )
  if 80 - 80: OoOO0ooOOoo0O / o0000oOoOoO0o / I1IiI + i1IIi - Oo
def iIIiiIIi1IiI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I11IIIiIi11 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I11IIIiIi11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11IIIiIi11 )
 if 39 - 39: o00O0oo % O0 % I1IiI . i1IIi
 if 86 - 86: Ooo00oOo00o * OoooooooOO
def OooO0oOo ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL2ZyZWVtdXNpY2FyY2hpdmUub3JnLw==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" style="background-color:.+?">(.+?)</a>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , o0o , 1011 , OOooO0OOoo + 'streams.png' )
def oOOo00O0OOOo ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<span class="ptxt-artist">\n.+?<b>\n.+?<a href=".+?">(.+?)</a>\n.+?</b>\n.+?</span>\n.+?<span class="ptxt-track"><a href=".+?"><b>"(.+?)"</b></a></span>\n.+?<span class="playicn">\n.+?<a href="(.+?)" class="icn-arrow" title="Download"></a>' , re . DOTALL ) . findall ( oOOO )
 O00Oooo = re . compile ( '.+?<a href="(.+?)">NEXT' ) . findall ( oOOO )
 for i11I1I1iiI , Ii1i1 , url in Oo0ooOo0o :
  IIiI1i1i ( '%s %s' % ( '[COLORgold]' + i11I1I1iiI + '[/COLOR]' , '[COLORgreen]' + Ii1i1 + '[/COLOR]' ) , url , 222 , OOooO0OOoo + 'streams.png' )
 O00Oooo = O00Oooo
 for iiI in O00Oooo :
  I1111IIIIIi ( '[COLORgold]NEXT[/COLOR] [COLORgreen]PAGE[/COLOR]' , iiI , 1011 , OOooO0OOoo + 'streams.png' )
def I1i1iii1Ii ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<div class="full-poster">.+?<img src="(.+?)".+?title=.+?alt="Watch(.+?)Online" />.+?<div class="clear"></div>(.+?)..+?</div>.+?<iframe.+?scrolling="no" frameborder="0" src="(.+?)" allowFullScreen></iframe>' , re . DOTALL ) . findall ( oOOO )
 for O0OOoO00OO0o , Ii1i1 , iI , url in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 222 , 'http://www.movietubenow.biz%s' % O0OOoO00OO0o , '' , iI )
  if 99 - 99: o0000oOoOoO0o - O0oO - OoOO % Ooo00oOo00o
  if 21 - 21: OoOoOO00 % ii11ii1ii . i1IIi - OoooooooOO
  if 4 - 4: OoooooooOO . o0oO0
  if 78 - 78: ii11ii1ii + o0000oOoOoO0o - O0
  if 10 - 10: O0oO % OOOo0
def oo0OoOooo ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 Oo0ooOo0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1002 , OOooO0OOoo + 'vod.png' )
  if 95 - 95: IIII * ii11ii1ii % o0oO0 % o00O0oo - o00O0oo
def oOoooO0 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 1003 , OOooO0OOoo + 'vod.png' )
  if 68 - 68: o0oO0 / OOooOOo
def Ii11 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oOOO )
 for Ii1i1 , url in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 1004 , OOooO0OOoo + 'vod.png' )
  if 8 - 8: Oo + OoOoOO00 * OoOO0ooOOoo0O * I1IiI * o0000oOoOoO0o / IIII
def iIiiOO0OoOOO0 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( "url: '(.+?)'," ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  IIiI1i1i ( 'STREAM' , url , 222 , OOooO0OOoo + 'vod.png' )
  if 90 - 90: o0oO0 + OoOoOO00 * ii11ii1ii / o00O0oo . OOooOOo + OOooOOo
  if 40 - 40: o0oO0 / I1IiI % i11iIiiIii % ii11ii1ii / OOOo0
def ooOOOOo0 ( url ) :
 OoO0O00O0oo0O = urllib2 . Request ( url )
 OoO0O00O0oo0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OoO0O00O0oo0O . add_header ( 'referer' , url )
 I1IiI11 = urllib2 . urlopen ( OoO0O00O0oo0O )
 I1I1iIiII1 = I1IiI11 . read ( )
 I1IiI11 . close ( )
 return I1I1iIiII1
 if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
def iIII1 ( url ) :
 OoO0O00O0oo0O = urllib2 . Request ( url )
 OoO0O00O0oo0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1IiI11 = urllib2 . urlopen ( OoO0O00O0oo0O )
 I1I1iIiII1 = I1IiI11 . read ( )
 I1IiI11 . close ( )
 return I1I1iIiII1
 if 96 - 96: oO0o0ooO0
def i1I11iIII1i1I ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOO0oo = ( '%s%s' % ( IiIIi1I1I11Ii , url ) )
 I1I1iIiII1 = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1I1iIiII1 )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( '%s' % ( Ii1i1 ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , O0OOoO00OO0o )
  if 64 - 64: OoooooooOO
def I111i1I1 ( url ) :
 oO0oooooo = xbmc . Player ( o0OO0Oo ( ) )
 import urlresolver
 try : oO0oooooo . play ( url )
 except : pass
 if 3 - 3: O0oO - O0 % iIii1I11I1II1 / IIII . OOooOOo
 if 3 - 3: O0 % OoooooooOO / OoOO0ooOOoo0O
def o0OO0Oo ( ) :
 try :
  ooOo = getSet ( "core-player" )
  if ( ooOo == 'DVDPLAYER' ) : o0oO0OoO0 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ooOo == 'MPLAYER' ) : o0oO0OoO0 = xbmc . PLAYER_CORE_MPLAYER
  elif ( ooOo == 'PAPLAYER' ) : o0oO0OoO0 = xbmc . PLAYER_CORE_PAPLAYER
  else : o0oO0OoO0 = xbmc . PLAYER_CORE_AUTO
 except : o0oO0OoO0 = xbmc . PLAYER_CORE_AUTO
 return o0oO0OoO0
 return True
 if 70 - 70: OoOO - OoOO
def I1111IIIIIi ( name , url , mode , iconimage ) :
 OoOO0OOoo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIIi11IiIiii = True
 i11IIIiI1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11IIIiI1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 IIIi11IiIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0OOoo , listitem = i11IIIiI1I , isFolder = True )
 return IIIi11IiIiii
 if 38 - 38: Oo - o0000oOoOoO0o . Oo
def IIiI1i1i ( name , url , mode , iconimage ) :
 OoOO0OOoo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIIi11IiIiii = True
 i11IIIiI1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11IIIiI1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 IIIi11IiIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0OOoo , listitem = i11IIIiI1I , isFolder = False )
 return IIIi11IiIiii
 if 38 - 38: i1IIi + o00O0oo
 if 91 - 91: OoOoOO00 % oO0o0ooO0 % IIII + OoOoOO00 / OoOO
 if 62 - 62: OoooooooOO - i11iIiiIii
 if 5 - 5: iIii1I11I1II1 / o0000oOoOoO0o / i1IIi % OoooooooOO
 if 50 - 50: o00O0oo / I1IiI * o00O0oo
 if 34 - 34: O0 * O0 % OoooooooOO + oO0o0ooO0 * iIii1I11I1II1 % o00O0oo
 if 25 - 25: o0000oOoOoO0o + I1IiI . OOooOOo % I1IiI * OoOO0ooOOoo0O
def ii1IiIi11 ( heading , announce ) :
 class iiiii1ii1 ( ) :
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
   try : Iii1I1111ii = open ( announce ) ; IiiiI1 = Iii1I1111ii . read ( )
   except : IiiiI1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiiiI1 ) )
   return
 iiiii1ii1 ( )
 if 100 - 100: OoOO . o00O0oo % i1IIi . o0oO0
def OOo0Oo0OOo0 ( ) :
 ii1IiIi11 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 19 - 19: o0000oOoOoO0o + OoOoOO00
 if 84 - 84: O0 - OoOoOO00 . Oo / OoOO . OoooooooOO + i11iIiiIii
 if 86 - 86: o0000oOoOoO0o / OOooOOo - OOooOOo + ii11ii1ii + OoOO
 if 33 - 33: OOooOOo . oO0o0ooO0 . IIII . i1IIi
 if 49 - 49: ii11ii1ii
def OO0Oooo0oOO0O ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 84 - 84: o0000oOoOoO0o - Oo / O0 - O0oO
 if 21 - 21: O0 * O0 % ii11ii1ii
 if 94 - 94: o0000oOoOoO0o + OoOoOO00 % i11iIiiIii
 if 8 - 8: o0oO0 * O0
 if 73 - 73: OOooOOo / OoOO / o0000oOoOoO0o / Ooo00oOo00o
 if 11 - 11: I1IiI + IIII - OoooooooOO / Ooo00oOo00o
 if 34 - 34: o0oO0
 if 45 - 45: o0oO0 / Oo / o00O0oo
 if 44 - 44: ii11ii1ii - o00O0oo / OoOoOO00 * Ooo00oOo00o * Oo
 if 73 - 73: OOooOOo - OOOo0 * i1IIi / i11iIiiIii * OoOO0ooOOoo0O % OoOoOO00
 if 56 - 56: OoooooooOO * Oo . Oo . ii11ii1ii
 if 24 - 24: Oo . o0000oOoOoO0o * o00O0oo % oO0o0ooO0 / OoOO0ooOOoo0O
 if 58 - 58: OOOo0 - ii11ii1ii % O0 . OOOo0 % Ooo00oOo00o % IIII
 if 87 - 87: OoOO - i11iIiiIii
 if 78 - 78: i11iIiiIii / iIii1I11I1II1 - OOooOOo
 if 23 - 23: o0000oOoOoO0o
 if 40 - 40: OOooOOo - OoOoOO00 / Oo
 if 14 - 14: ii11ii1ii
 if 5 - 5: OOooOOo . iIii1I11I1II1 % iIii1I11I1II1
 if 56 - 56: OoooooooOO - o0000oOoOoO0o - i1IIi
 if 8 - 8: O0oO / OoOO0ooOOoo0O . OOOo0 + ii11ii1ii / i11iIiiIii
 if 31 - 31: o0oO0 - iIii1I11I1II1 + oO0o0ooO0 . Oo / IIII % iIii1I11I1II1
 if 6 - 6: IIII * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / i1IIi
 if 53 - 53: o0000oOoOoO0o + iIii1I11I1II1
def oOooo0Oo ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + oo0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 87 - 87: Oo / O0 * IIII / OOooOOo
def I1iiIII ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + iIi1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 63 - 63: oO0o0ooO0 * ii11ii1ii . OoooooooOO / OoOO0ooOOoo0O * Oo . o0oO0
def Ooo0 ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + oooO00o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 53 - 53: o0oO0
def o0oO0oo0000OO ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + I1i1ii1IiIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 69 - 69: I1IiI % OoOO - o0000oOoOoO0o
def Iiii1ii ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + I1i111IiIiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 39 - 39: o0000oOoOoO0o - ii11ii1ii
def OOO0o0OO0OO ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + oOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 43 - 43: OOooOOo . oO0o0ooO0 . o0000oOoOoO0o + iIii1I11I1II1
def OoOOoO0oOo ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + O0ooOOOO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 38 - 38: O0oO % OoOO0ooOOoo0O - OoooooooOO
def oOo0OOoooO ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + iIi1iIIIiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 62 - 62: i11iIiiIii % OoOO0ooOOoo0O . IIII . OoOO0ooOOoo0O
def ooOo0O0O0oOO0 ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + iIiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 14 - 14: OOooOOo / OoOO0ooOOoo0O - iIii1I11I1II1 - OoOO % o0oO0
def I1iIiI1IiIIII ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + I1iiIi111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 5 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 34 - 34: i11iIiiIii - OoOoOO00 / OOOo0 % OOooOOo
 if 33 - 33: OoOO0ooOOoo0O
 if 35 - 35: i11iIiiIii - OOOo0 / OoOO0ooOOoo0O + o00O0oo * OoOO
 if 49 - 49: OOooOOo * o00O0oo + o0000oOoOoO0o + oO0o0ooO0
 if 30 - 30: OOooOOo / OoOO0ooOOoo0O / IIII % o0oO0 + OoOoOO00
 if 4 - 4: oO0o0ooO0 - Oo - IIII - o0000oOoOoO0o % i11iIiiIii / Ooo00oOo00o
 if 50 - 50: o0oO0 + i1IIi
 if 31 - 31: o00O0oo
 if 78 - 78: i11iIiiIii + OOooOOo + O0oO / OOooOOo % iIii1I11I1II1 % IIII
def Oo0O0Oo00O ( ) :
 try :
  if os . path . exists ( O0OoO000O0OO ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I1i1i1iii , I1111i , iIIii in os . walk ( O0OoO000O0OO ) :
     iIoo0ooooO = 0
     iIoo0ooooO += len ( iIIii )
     if iIoo0ooooO > 0 :
      for Iii1I1111ii in iIIii :
       os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
  iiIIi = os . path . join ( oOOoO0 , "Textures13.db" )
  os . unlink ( iiIIi )
  i1iiIII111ii . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 36 - 36: o0000oOoOoO0o . OoOoOO00
 if 25 - 25: OoOO
 if 34 - 34: I1IiI . iIii1I11I1II1 % O0
 if 43 - 43: ii11ii1ii - oO0o0ooO0
 if 70 - 70: oO0o0ooO0 / OoOO0ooOOoo0O % o0oO0 - o00O0oo
 if 47 - 47: oO0o0ooO0
 if 92 - 92: OoOO0ooOOoo0O + I1IiI % i1IIi
 if 23 - 23: O0oO - OoOO0ooOOoo0O + o00O0oo - I1IiI * I1IiI . Oo
 if 47 - 47: OoOO % iIii1I11I1II1
def IiI1IIIII1I ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 I1I1IiIi1 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( I1I1IiIi1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( I1I1IiIi1 ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 58 - 58: I1IiI - oO0o0ooO0 - OoooooooOO
   if 96 - 96: iIii1I11I1II1
   if iIoo0ooooO > 0 :
    if 82 - 82: I1IiI + O0 - IIII % OoOO * i11iIiiIii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete KODI Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 15 - 15: OOooOOo
     for Iii1I1111ii in iIIii :
      try :
       os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
      except :
       pass
     for I1iIoO0Ooo0OooOOo in I1111i :
      try :
       shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      except :
       pass
       if 71 - 71: IIII + i1IIi * Oo % Oo / Oo
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  OoO00o0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 68 - 68: O0
  for I1i1i1iii , I1111i , iIIii in os . walk ( OoO00o0 ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 2 - 2: Ooo00oOo00o + O0 * Ooo00oOo00o - o00O0oo + OoOO
   if iIoo0ooooO > 0 :
    if 43 - 43: ii11ii1ii - I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( iIoo0ooooO ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 36 - 36: ii11ii1ii - oO0o0ooO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 24 - 24: OOooOOo + o0oO0 + o0000oOoOoO0o - iIii1I11I1II1
   else :
    pass
  I11Oo0oO00 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 8 - 8: OOOo0 % OOOo0 . I1IiI % OOooOOo
  for I1i1i1iii , I1111i , iIIii in os . walk ( I11Oo0oO00 ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 47 - 47: o0oO0 + OoOoOO00 % O0oO . o0000oOoOoO0o % ii11ii1ii
   if iIoo0ooooO > 0 :
    if 7 - 7: O0 / oO0o0ooO0 * OoOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( iIoo0ooooO ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 29 - 29: OOooOOo
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 86 - 86: OoOoOO00 . IIII
   else :
    pass
    if 2 - 2: OoooooooOO
    if 60 - 60: Ooo00oOo00o
    if 81 - 81: I1IiI % o00O0oo
    if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
 OOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( OOOo ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( OOOo ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 74 - 74: o00O0oo - OoooooooOO . Oo
   if 31 - 31: OOooOOo % o0000oOoOoO0o + iIii1I11I1II1 + i11iIiiIii * O0oO
   if iIoo0ooooO > 0 :
    if 45 - 45: OoOO0ooOOoo0O * O0oO . o0oO0 - O0oO + IIII
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete WTF Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 34 - 34: OoOO0ooOOoo0O . Oo
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 78 - 78: ii11ii1ii % OOOo0 / OoooooooOO % OoOO0ooOOoo0O - oO0o0ooO0
   else :
    pass
    if 2 - 2: iIii1I11I1II1
    if 45 - 45: OoooooooOO / i11iIiiIii
 I11I1i1iI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( I11I1i1iI ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( I11I1i1iI ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 90 - 90: IIII * OoOoOO00 % O0oO + OoOO
   if 93 - 93: O0oO + o00O0oo
   if iIoo0ooooO > 0 :
    if 33 - 33: O0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete 4oD Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 78 - 78: O0 / OoOoOO00 * Ooo00oOo00o
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % O0oO - iIii1I11I1II1 % O0
   else :
    pass
    if 58 - 58: IIII + iIii1I11I1II1
    if 65 - 65: OoOoOO00 - O0oO % OOooOOo - I1IiI * oO0o0ooO0 + o00O0oo
 O0o0O0OO0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( O0o0O0OO0o ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( O0o0O0OO0o ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 54 - 54: I1IiI . OoOO % i11iIiiIii / OoooooooOO + IIII % OoOO
   if 36 - 36: OoOO
   if iIoo0ooooO > 0 :
    if 74 - 74: OoooooooOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete BBC iPlayer Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 72 - 72: O0 + OOOo0 - oO0o0ooO0 - Ooo00oOo00o
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 100 - 100: O0
   else :
    pass
    if 79 - 79: iIii1I11I1II1
    if 81 - 81: OoOO0ooOOoo0O + iIii1I11I1II1 * O0oO - iIii1I11I1II1 . OoOO0ooOOoo0O
    if 48 - 48: o0000oOoOoO0o . OoooooooOO . OOOo0 . I1IiI % ii11ii1ii / oO0o0ooO0
 ii1I111i1Ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( ii1I111i1Ii ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( ii1I111i1Ii ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 84 - 84: ii11ii1ii % iIii1I11I1II1 + Ooo00oOo00o . ii11ii1ii % Ooo00oOo00o
   if 93 - 93: O0
   if iIoo0ooooO > 0 :
    if 85 - 85: i11iIiiIii % i11iIiiIii + O0 / OoOO0ooOOoo0O
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Simple Downloader Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: o00O0oo % i1IIi % OoOO
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 53 - 53: OoOO * OoooooooOO . I1IiI
   else :
    pass
    if 96 - 96: OOOo0 % i1IIi . OOooOOo . O0
    if 37 - 37: i1IIi - OoOO0ooOOoo0O % OoooooooOO / OoOO0ooOOoo0O % o0oO0
 iiIiII11i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iiIiII11i1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( iiIiII11i1 ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 93 - 93: I1IiI % iIii1I11I1II1
   if 90 - 90: OOOo0 - OoOO0ooOOoo0O / o00O0oo / O0 / o0000oOoOoO0o
   if iIoo0ooooO > 0 :
    if 87 - 87: I1IiI / IIII + iIii1I11I1II1
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ITV Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: iIii1I11I1II1 + OoOO % o0oO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 21 - 21: OoOO0ooOOoo0O
   else :
    pass
    if 6 - 6: IIII
    if 46 - 46: IIII + OoOO
 Oo00o0O0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iiIiII11i1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( Oo00o0O0O ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 84 - 84: o0000oOoOoO0o % i1IIi
   if 33 - 33: ii11ii1ii * ii11ii1ii . o0oO0 . i11iIiiIii
   if iIoo0ooooO > 0 :
    if 48 - 48: OOooOOo . o00O0oo + I1IiI % ii11ii1ii / i11iIiiIii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Movies4me Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 74 - 74: OoOoOO00 . O0 - OOOo0 + IIII % i11iIiiIii % I1IiI
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 78 - 78: o00O0oo + I1IiI + IIII - IIII . i11iIiiIii / Ooo00oOo00o
   else :
    pass
    if 27 - 27: o00O0oo - O0 % o0000oOoOoO0o * O0oO . IIII % iIii1I11I1II1
    if 37 - 37: OoooooooOO + O0 - i1IIi % o0oO0
 i1I1i1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iiIiII11i1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i1I1i1i ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 36 - 36: OoOoOO00 % O0
   if 35 - 35: iIii1I11I1II1 - OoOO0ooOOoo0O % OOooOOo
   if iIoo0ooooO > 0 :
    if 30 - 30: O0oO % O0oO % IIII . I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Phoenix Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 9 - 9: o0oO0 / OoOoOO00 . I1IiI % OOooOOo * OoOoOO00 - o0oO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 55 - 55: OOOo0
   else :
    pass
    if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
    if 35 - 35: ii11ii1ii / oO0o0ooO0 % OOOo0 + iIii1I11I1II1
 oO00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iiIiII11i1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( oO00o ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 36 - 36: O0oO . OoOoOO00 % o0oO0
   if 84 - 84: OoooooooOO - i11iIiiIii / iIii1I11I1II1 / OoooooooOO / ii11ii1ii
   if iIoo0ooooO > 0 :
    if 4 - 4: Oo + OOooOOo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Music Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: Ooo00oOo00o * I1IiI
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 15 - 15: i11iIiiIii / o0oO0 % OOOo0
   else :
    pass
    if 71 - 71: O0oO / ii11ii1ii * iIii1I11I1II1
    if 57 - 57: OoOO0ooOOoo0O + O0oO % ii11ii1ii . Ooo00oOo00o / Ooo00oOo00o * O0
 Ii1iiII1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iiIiII11i1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( Ii1iiII1i ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 52 - 52: OoOO / O0oO
   if 91 - 91: IIII . Oo + OoOoOO00
   if iIoo0ooooO > 0 :
    if 36 - 36: O0 * Ooo00oOo00o % oO0o0ooO0 * oO0o0ooO0 / Ooo00oOo00o * IIII
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete SuperCartoons Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: i1IIi . IIII + O0 * o0oO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 76 - 76: Ooo00oOo00o
   else :
    pass
    if 92 - 92: o0000oOoOoO0o - iIii1I11I1II1 % OoooooooOO
    if 39 - 39: oO0o0ooO0 . OOOo0 * I1IiI - i11iIiiIii
 i1II1II1iii1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iiIiII11i1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i1II1II1iii1i ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 75 - 75: IIII - I1IiI - iIii1I11I1II1 % OOooOOo
   if 58 - 58: O0 . IIII / OoooooooOO . Ooo00oOo00o / Oo * OoOoOO00
   if iIoo0ooooO > 0 :
    if 53 - 53: o00O0oo - O0 / OOooOOo % oO0o0ooO0 * OOOo0 % OoOO0ooOOoo0O
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete TVonline Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 69 - 69: ii11ii1ii
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 83 - 83: OOooOOo
   else :
    pass
    if 38 - 38: O0oO + OoooooooOO . i1IIi
    if 19 - 19: oO0o0ooO0 - OOooOOo - o00O0oo - I1IiI . oO0o0ooO0 . O0oO
 i11I1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iiIiII11i1 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i11I1I ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 71 - 71: oO0o0ooO0
   if 23 - 23: i1IIi . iIii1I11I1II1 . OoOO0ooOOoo0O . O0 % o00O0oo % i11iIiiIii
   if iIoo0ooooO > 0 :
    if 11 - 11: O0 - OoOoOO00 . OoOO0ooOOoo0O . o00O0oo % O0oO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: Oo / oO0o0ooO0 . O0oO * OoooooooOO + o0000oOoOoO0o - i1IIi
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
      if 58 - 58: ii11ii1ii
   else :
    pass
    if 2 - 2: OoOoOO00 / O0oO
    if 54 - 54: i1IIi . o0000oOoOoO0o - ii11ii1ii + o0oO0 + Oo / Oo
    if 22 - 22: o0oO0 . iIii1I11I1II1
 i1IiiiiIi1I = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 try :
  if i1iiIII111ii . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   ooo0O0o0OoOO = os . path . join ( i1IiiiiIi1I , "cache.db" )
   os . unlink ( ooo0O0o0OoOO )
   if 9 - 9: Ooo00oOo00o
 except :
  pass
  if 60 - 60: O0oO
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 98 - 98: o0oO0
 if 34 - 34: iIii1I11I1II1 * o0000oOoOoO0o * o0000oOoOoO0o / ii11ii1ii
 if 28 - 28: Ooo00oOo00o - OoOO + I1IiI + o00O0oo / iIii1I11I1II1
 if 26 - 26: iIii1I11I1II1 - O0 . O0
 if 68 - 68: OoOO0ooOOoo0O + OoOO . O0 . o00O0oo % i1IIi % OoOO0ooOOoo0O
 if 50 - 50: IIII + OOooOOo
 if 96 - 96: Ooo00oOo00o
 if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
 if 87 - 87: I1IiI % iIii1I11I1II1
def o0O ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 O0OOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i1i1iii , I1111i , iIIii in os . walk ( O0OOO0O ) :
   iIoo0ooooO = 0
   iIoo0ooooO += len ( iIIii )
   if 36 - 36: i11iIiiIii / oO0o0ooO0 . o0000oOoOoO0o + IIII . O0 + OOOo0
   if 36 - 36: i1IIi - ii11ii1ii - O0oO
   if iIoo0ooooO > 0 :
    if 7 - 7: i11iIiiIii + OOOo0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Package Cache Files" , str ( iIoo0ooooO ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: O0oO - OoOO0ooOOoo0O / o0oO0 - Oo + oO0o0ooO0 - iIii1I11I1II1
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for I1iIoO0Ooo0OooOOo in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , I1iIoO0Ooo0OooOOo ) )
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
 if 68 - 68: o00O0oo - OoOO + Oo
 if 44 - 44: o00O0oo * OOooOOo * OoOoOO00
 if 5 - 5: i1IIi + O0 % O0 * O0 + I1IiI % i1IIi
 if 80 - 80: oO0o0ooO0 / OOooOOo + Ooo00oOo00o / OoOO
 if 46 - 46: i11iIiiIii / IIII % i1IIi - o0000oOoOoO0o * I1IiI
 if 94 - 94: o00O0oo - ii11ii1ii + OOooOOo - Oo
 if 15 - 15: OoOO0ooOOoo0O
 if 31 - 31: oO0o0ooO0 / i1IIi . Ooo00oOo00o
 if 83 - 83: OoOO / iIii1I11I1II1 + i1IIi / oO0o0ooO0
def IIiiii1 ( url , name ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oo0oO00OOO = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 Iii11I111i = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml.bak' )
 if os . path . exists ( Iii11I111i ) == False :
  if i1iiIII111ii . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0Oo0oO00OOO = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
   try :
    os . remove ( o0Oo0oO00OOO )
    print '=== GenieTv - REMOVING    ' + str ( o0Oo0oO00OOO ) + '    ==='
   except :
    pass
   I1I1iIiII1 = I11 . http_GET ( url ) . content
   o00O0O = open ( o0Oo0oO00OOO , "w" )
   o00O0O . write ( I1I1iIiII1 )
   o00O0O . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0oO00OOO ) + '    ==='
   i1iiIII111ii = xbmcgui . Dialog ( )
   i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0Oo0oO00OOO = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
  try :
   os . remove ( o0Oo0oO00OOO )
   print '=== GenieTv - REMOVING    ' + str ( o0Oo0oO00OOO ) + '    ==='
  except :
   pass
  I1I1iIiII1 = I11 . http_GET ( url ) . content
  o00O0O = open ( o0Oo0oO00OOO , "w" )
  o00O0O . write ( I1I1iIiII1 )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0oO00OOO ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 89 - 89: oO0o0ooO0 . OOOo0
def ooOoo0OoOO ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oo0oO00OOO = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
 try :
  o00O0O = open ( o0Oo0oO00OOO ) . read ( )
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
 if 38 - 38: Ooo00oOo00o / o0oO0 % O0oO * o0000oOoOoO0o + i11iIiiIii % o0oO0
def O000oOo0O ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oo0oO00OOO = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
 try :
  os . remove ( o0Oo0oO00OOO )
  i1iiIII111ii = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0Oo0oO00OOO ) + '    ==='
  i1iiIII111ii . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 82 - 82: IIII
 if 86 - 86: Oo * OoOoOO00 * O0
 if 83 - 83: IIII / O0oO
 if 64 - 64: Ooo00oOo00o % IIII . O0oO % Ooo00oOo00o + o0000oOoOoO0o * IIII
 if 83 - 83: OOooOOo % OoOO + o0000oOoOoO0o % i11iIiiIii + O0
 if 65 - 65: iIii1I11I1II1 % OoOO + O0 / OoooooooOO
 if 52 - 52: o00O0oo % OoOO0ooOOoo0O * OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / oO0o0ooO0
 if 80 - 80: OoooooooOO + IIII
 if 95 - 95: O0oO / OoOO * O0oO - OoooooooOO * OoooooooOO % Ooo00oOo00o
 if 43 - 43: Oo . O0oO
def I1I1i1i ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Oo0ooOo0o = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for OOo0O , oOOoooO0O0 , ii1O0ooooo000 , OooOoOO0OO in Oo0ooOo0o :
  if inc < 2 : i1iiIII111ii = xbmcgui . Dialog ( ) ; i1iiIII111ii . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOo0O , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % ii1O0ooooo000 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OooOoOO0OO )
  inc = inc + 1
  if 27 - 27: IIII * OOOo0 . iIii1I11I1II1 - iIii1I11I1II1
  if 5 - 5: IIII
  if 84 - 84: OoOoOO00 * OoOO * OoOoOO00 % IIII / OOOo0
  if 100 - 100: IIII . o00O0oo - iIii1I11I1II1 . i11iIiiIii / OoOoOO00
  if 71 - 71: O0oO * Oo . o0000oOoOoO0o
  if 49 - 49: IIII * O0 . IIII
  if 19 - 19: OoOoOO00 - IIII
  if 59 - 59: OOooOOo * Ooo00oOo00o - o00O0oo . OoOO0ooOOoo0O
  if 89 - 89: OoOO0ooOOoo0O
def o00oo0OO0 ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  o0Oo0oO00OOO = os . path . join ( iiIi1IIi1I , 'addons2.ini' )
  I1I1iIiII1 = I11 . http_GET ( url ) . content
  o00O0O = open ( o0Oo0oO00OOO , "w" )
  o00O0O . write ( I1I1iIiII1 )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0oO00OOO ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 60 - 60: o0oO0
def O000O ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  o0Oo0oO00OOO = os . path . join ( iiIi1IIi1I , 'settings.xml' )
  I1I1iIiII1 = I11 . http_GET ( url ) . content
  o00O0O = open ( o0Oo0oO00OOO , "w" )
  o00O0O . write ( I1I1iIiII1 )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0oO00OOO ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 22 - 22: OoOO
 if 33 - 33: O0
def oo00o0I1IiI ( ) :
 try :
  I1iI1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( I1iI1 ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    oOOO00OOOoOO = os . path . join ( I1iI1 , "source.db" )
    os . unlink ( oOOO00OOOoOO )
  i1iiIII111ii . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 23 - 23: I1IiI . OOooOOo - Ooo00oOo00o / I1IiI * iIii1I11I1II1
 if 13 - 13: OOooOOo * i11iIiiIii / i11iIiiIii . Ooo00oOo00o . OoOO0ooOOoo0O . ii11ii1ii
 if 26 - 26: OOooOOo . iIii1I11I1II1
 if 67 - 67: Oo / O0
 if 88 - 88: I1IiI - OoOO0ooOOoo0O
def i11i1I1 ( url ) :
 OoO0O00O0oo0O = urllib2 . Request ( url )
 OoO0O00O0oo0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IiI11 = urllib2 . urlopen ( OoO0O00O0oo0O )
 I1I1iIiII1 = I1IiI11 . read ( )
 I1IiI11 . close ( )
 return I1I1iIiII1
 if 63 - 63: IIII * OoooooooOO
 if 19 - 19: IIII - OOooOOo . iIii1I11I1II1 . I1IiI / OoOO0ooOOoo0O
 if 87 - 87: I1IiI - o0oO0 - OoOO0ooOOoo0O + Oo % iIii1I11I1II1 / i11iIiiIii
 if 12 - 12: o0oO0
 if 86 - 86: OoOO - Ooo00oOo00o
 if 63 - 63: OOOo0 / I1IiI + OoooooooOO . o0000oOoOoO0o . o0oO0
 if 48 - 48: i1IIi - oO0o0ooO0 - i11iIiiIii . o0000oOoOoO0o - oO0o0ooO0 * o0000oOoOoO0o
def OOOOO ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; O0OOoo0 = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O0OOoo0 :
  i1I1iii = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; i1I1iii = xbmc . translatePath ( i1I1iii ) ;
  i1IIOo0 = os . path . join ( i1I1iii , ".." , ".." ) ; i1IIOo0 = os . path . abspath ( i1IIOo0 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + i1IIOo0 ) ; O0000Oo00o = False
  try :
   for I1i1i1iii , I1111i , iIIii in os . walk ( i1IIOo0 , topdown = True ) :
    I1111i [ : ] = [ I1iIoO0Ooo0OooOOo for I1iIoO0Ooo0OooOOo in I1111i if I1iIoO0Ooo0OooOOo not in Oo0oO0ooo ]
    for Ii1i1 in iIIii :
     try : os . remove ( os . path . join ( I1i1i1iii , Ii1i1 ) )
     except :
      if Ii1i1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0000Oo00o = True
      plugintools . log ( "Error removing " + I1i1i1iii + " " + Ii1i1 )
    for Ii1i1 in I1111i :
     try : os . rmdir ( os . path . join ( I1i1i1iii , Ii1i1 ) )
     except :
      if Ii1i1 not in [ "Database" , "userdata" ] : O0000Oo00o = True
      plugintools . log ( "Error removing " + I1i1i1iii + " " + Ii1i1 )
   if not O0000Oo00o : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 I111iI ( )
 if 20 - 20: Ooo00oOo00o . OOOo0 * i11iIiiIii / i11iIiiIii
 if 89 - 89: oO0o0ooO0 . i11iIiiIii * O0
 if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + IIII
def iI111II1ii ( ) :
 O0ooO00ooOO0o = [ ]
 o0OI1II = sys . argv [ 2 ]
 if len ( o0OI1II ) >= 2 :
  iIIi1Ii1III = sys . argv [ 2 ]
  Oooo00 = iIIi1Ii1III . replace ( '?' , '' )
  if ( iIIi1Ii1III [ len ( iIIi1Ii1III ) - 1 ] == '/' ) :
   iIIi1Ii1III = iIIi1Ii1III [ 0 : len ( iIIi1Ii1III ) - 2 ]
  iii1II1iI1IIi = Oooo00 . split ( '&' )
  O0ooO00ooOO0o = { }
  for Ii11iiI1 in range ( len ( iii1II1iI1IIi ) ) :
   oO0OOOoooO00o0o = { }
   oO0OOOoooO00o0o = iii1II1iI1IIi [ Ii11iiI1 ] . split ( '=' )
   if ( len ( oO0OOOoooO00o0o ) ) == 2 :
    O0ooO00ooOO0o [ oO0OOOoooO00o0o [ 0 ] ] = oO0OOOoooO00o0o [ 1 ]
    if 10 - 10: o00O0oo - i11iIiiIii . ii11ii1ii % i1IIi
 return O0ooO00ooOO0o
 if 78 - 78: iIii1I11I1II1 * Oo . Oo - OoOO0ooOOoo0O . iIii1I11I1II1
o00ooO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
o0OoOO000ooO0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OO0OO0O00oO0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I111I1I = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
ii1I = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
Oo0000 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
oo0O0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oO0Oo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
iIi1I1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oooO00o0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1i1ii1IiIii = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
I1i111IiIiIi1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oOo0O = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O0ooOOOO0O0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iIi1iIIIiIiI = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iIiIIi = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iiIiI = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
OooOOOOOo = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oOOoOooOo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ii1ii11IIIiiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
Oo00oo0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oo0O0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1iiIi111I = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
IiIIi1I1I11Ii = base64 . decodestring ( 'Q1VOVA==' )
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description ) :
 OoOO0OOoo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIi11IiIiii = True
 i11IIIiI1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11IIIiI1I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11IIIiI1I . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  IIIi11IiIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0OOoo , listitem = i11IIIiI1I , isFolder = False )
 else :
  IIIi11IiIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0OOoo , listitem = i11IIIiI1I , isFolder = True )
 return IIIi11IiIiii
def IIIIii ( name , url , mode , iconimage , fanart , description ) :
 OoOO0OOoo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIi11IiIiii = True
 i11IIIiI1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11IIIiI1I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11IIIiI1I . setProperty ( "Fanart_Image" , fanart )
 IIIi11IiIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0OOoo , listitem = i11IIIiI1I , isFolder = False )
 return IIIi11IiIiii
 if 50 - 50: O0oO + o0oO0 + oO0o0ooO0
 if 15 - 15: o0000oOoOoO0o
iIIi1Ii1III = iI111II1ii ( )
o0o = None
Ii1i1 = None
IiiI11I1IIiI = None
iiIii = None
ooo0O = None
oOoO0o00OO0 = None
if 5 - 5: Oo
if 100 - 100: o00O0oo + iIii1I11I1II1
try :
 o0o = urllib . unquote_plus ( iIIi1Ii1III [ "url" ] )
except :
 pass
try :
 Ii1i1 = urllib . unquote_plus ( iIIi1Ii1III [ "name" ] )
except :
 pass
try :
 iiIii = urllib . unquote_plus ( iIIi1Ii1III [ "iconimage" ] )
except :
 pass
try :
 IiiI11I1IIiI = int ( iIIi1Ii1III [ "mode" ] )
except :
 pass
try :
 ooo0O = urllib . unquote_plus ( iIIi1Ii1III [ "fanart" ] )
except :
 pass
try :
 oOoO0o00OO0 = urllib . unquote_plus ( iIIi1Ii1III [ "description" ] )
except :
 pass
 if 59 - 59: IIII
 if 89 - 89: I1IiI % iIii1I11I1II1
print str ( iiI1IiI ) + ': ' + str ( iIii1 )
print "Mode: " + str ( IiiI11I1IIiI )
print "URL: " + str ( o0o )
print "Name: " + str ( Ii1i1 )
print "IconImage: " + str ( iiIii )
if 35 - 35: ii11ii1ii + O0oO - I1IiI % OoOO % OOooOOo % I1IiI
if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
def o0oo0o0O00OO ( content , viewType ) :
 if 24 - 24: o0oO0 - o0000oOoOoO0o * OoOO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 87 - 87: o00O0oo - ii11ii1ii % ii11ii1ii . OoOO / ii11ii1ii
  if 6 - 6: I1IiI / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
if IiiI11I1IIiI == None :
 oOOO00o ( )
 if 79 - 79: IIII % Ooo00oOo00o
elif IiiI11I1IIiI == 1 :
 oOoooo0O0Oo ( o0o )
 if 81 - 81: i11iIiiIii + i11iIiiIii * Ooo00oOo00o + IIII
elif IiiI11I1IIiI == 44 :
 o0oOO000oO0oo ( o0o )
 if 32 - 32: O0 . OoooooooOO
elif IiiI11I1IIiI == 2 :
 IiIiii1I1 ( )
 if 15 - 15: OOOo0 . Ooo00oOo00o
elif IiiI11I1IIiI == 3 :
 Oo0O0O0ooO0O ( )
 if 17 - 17: i11iIiiIii / Oo . Ooo00oOo00o / OOOo0
elif IiiI11I1IIiI == 21 :
 Oo000o ( )
 if 38 - 38: i1IIi . ii11ii1ii % o00O0oo + iIii1I11I1II1 + O0
elif IiiI11I1IIiI == 4 :
 iIi1iIiii111 ( )
 if 47 - 47: Ooo00oOo00o + IIII / OoOoOO00
elif IiiI11I1IIiI == 5 :
 Oo0O0oooo ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 97 - 97: ii11ii1ii / OOOo0 % O0 + i1IIi - o0oO0
elif IiiI11I1IIiI == 6 :
 o0O ( o0o )
 if 38 - 38: OOooOOo % O0oO + i11iIiiIii + oO0o0ooO0 + o0oO0 / i11iIiiIii
elif IiiI11I1IIiI == 7 :
 IIiiii1 ( o0o , Ii1i1 )
 if 94 - 94: oO0o0ooO0 - Oo + OoOO
elif IiiI11I1IIiI == 8 :
 ooOoo0OoOO ( o0o , Ii1i1 )
 if 59 - 59: o0000oOoOoO0o . OOOo0 - iIii1I11I1II1 + iIii1I11I1II1
elif IiiI11I1IIiI == 9 :
 FIXREPOSADDONS ( o0o )
 if 56 - 56: OoOO + o0oO0
elif IiiI11I1IIiI == 10 :
 OO0Oooo0oOO0O ( )
 if 32 - 32: OoOoOO00 + I1IiI % o0oO0 / I1IiI + ii11ii1ii
elif IiiI11I1IIiI == 11 :
 O000oOo0O ( o0o )
 if 2 - 2: i11iIiiIii - O0oO + Ooo00oOo00o % o0000oOoOoO0o * o00O0oo
elif IiiI11I1IIiI == 12 :
 I1I1i1i ( )
 if 54 - 54: O0 - oO0o0ooO0 . OoOO0ooOOoo0O % oO0o0ooO0 + oO0o0ooO0
elif IiiI11I1IIiI == 13 :
 Oo0O0Oo00O ( )
 if 36 - 36: OoOO0ooOOoo0O % i11iIiiIii
elif IiiI11I1IIiI == 14 :
 IiI1IIIII1I ( o0o )
 if 47 - 47: i1IIi + OoOoOO00 . Oo * OoOO . o0000oOoOoO0o / i1IIi
elif IiiI11I1IIiI == 15 :
 oO00O0O0O ( )
 if 50 - 50: O0oO / i1IIi % OoooooooOO
elif IiiI11I1IIiI == 16 :
 o00oo0OO0 ( o0o , Ii1i1 )
 if 83 - 83: ii11ii1ii * ii11ii1ii + OoOO0ooOOoo0O
elif IiiI11I1IIiI == 17 :
 O000O ( o0o , Ii1i1 )
 if 57 - 57: O0 - O0 . ii11ii1ii / OOooOOo / o00O0oo
elif IiiI11I1IIiI == 18 :
 oo00o0I1IiI ( )
 if 20 - 20: OoOO0ooOOoo0O * OoOoOO00 - I1IiI - OoOO * O0oO
elif IiiI11I1IIiI == 19 :
 oo000o ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 6 - 6: o0oO0 + OoOO0ooOOoo0O / Oo + IIII % OoOoOO00 / Ooo00oOo00o
elif IiiI11I1IIiI == 40 :
 OooiIi1IiIiiII ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 45 - 45: OoooooooOO
elif IiiI11I1IIiI == 42 :
 oO0o0 ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 9 - 9: o0000oOoOoO0o . Ooo00oOo00o * i1IIi . OoooooooOO
elif IiiI11I1IIiI == 43 :
 O0oOOO0ooOOO0OOO ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 32 - 32: I1IiI . ii11ii1ii % OOOo0 - OoOoOO00
elif IiiI11I1IIiI == 20 :
 i1iIi1iIi1i ( o0o )
 if 11 - 11: O0 + OOOo0
elif IiiI11I1IIiI == 22 :
 oOooo0Oo ( o0o )
 if 80 - 80: OoOO % OoOO % O0 - i11iIiiIii . oO0o0ooO0 / O0
elif IiiI11I1IIiI == 23 :
 I1iiIII ( o0o )
 if 13 - 13: OOOo0 + O0 - ii11ii1ii % Oo / o00O0oo . i1IIi
elif IiiI11I1IIiI == 24 :
 Ooo0 ( o0o )
 if 60 - 60: Oo . IIII % OOOo0 - O0oO
elif IiiI11I1IIiI == 25 :
 o0oO0oo0000OO ( o0o )
 if 79 - 79: OoooooooOO / ii11ii1ii . O0
elif IiiI11I1IIiI == 26 :
 Iiii1ii ( o0o )
 if 79 - 79: OoOO - OoOoOO00
elif IiiI11I1IIiI == 27 :
 OOO0o0OO0OO ( o0o )
 if 43 - 43: i1IIi + O0 % Ooo00oOo00o / o00O0oo * OOOo0
elif IiiI11I1IIiI == 28 :
 OoOOoO0oOo ( o0o )
 if 89 - 89: OOOo0 . Oo + ii11ii1ii . O0 % OOooOOo
elif IiiI11I1IIiI == 29 :
 oOo0OOoooO ( o0o )
 if 84 - 84: OoooooooOO + O0oO / OOOo0 % OoOO0ooOOoo0O % ii11ii1ii * OOOo0
elif IiiI11I1IIiI == 30 :
 o0O0OOO0Ooo ( o0o )
 if 58 - 58: Ooo00oOo00o - I1IiI . i11iIiiIii % i11iIiiIii / i1IIi / OoOO
elif IiiI11I1IIiI == 31 :
 ooOo0O0O0oOO0 ( o0o )
 if 24 - 24: OOOo0 * i1IIi % o0oO0 / O0 + i11iIiiIii
elif IiiI11I1IIiI == 32 :
 ii111111I1iII ( )
 if 12 - 12: ii11ii1ii / o00O0oo
elif IiiI11I1IIiI == 33 :
 Ii ( )
 if 5 - 5: OoooooooOO
elif IiiI11I1IIiI == 35 :
 O00oO000O0O ( o0o )
 if 18 - 18: OOOo0 % OoooooooOO - oO0o0ooO0 . i11iIiiIii * Oo % o00O0oo
elif IiiI11I1IIiI == 34 :
 OOooo0O00o ( o0o )
 if 12 - 12: i1IIi / OoOO0ooOOoo0O % o0oO0 * IIII * O0 * iIii1I11I1II1
elif IiiI11I1IIiI == 36 :
 O0oOoOOOoOO ( o0o )
 if 93 - 93: Oo / ii11ii1ii + i1IIi * OoOO . OoooooooOO
elif IiiI11I1IIiI == 37 :
 I1I111 ( o0o )
 if 54 - 54: O0 / IIII % o0oO0 * i1IIi * O0
elif IiiI11I1IIiI == 38 :
 OooOOOOo ( o0o )
 if 48 - 48: OOooOOo . OoOO % I1IiI - I1IiI
elif IiiI11I1IIiI == 41 :
 OOOOO ( iIIi1Ii1III )
 if 33 - 33: o0000oOoOoO0o % OoOoOO00 + Ooo00oOo00o
elif IiiI11I1IIiI == 39 :
 I1iIiI1IiIIII ( o0o )
 if 93 - 93: i1IIi . IIII / OOOo0 + IIII
elif IiiI11I1IIiI == 45 :
 TEXTS ( )
 if 58 - 58: ii11ii1ii + O0 . Oo + I1IiI - Ooo00oOo00o - I1IiI
elif IiiI11I1IIiI == 46 :
 OOo0Oo0OOo0 ( )
 if 41 - 41: Oo / i1IIi / Oo - oO0o0ooO0 . OOooOOo
elif IiiI11I1IIiI == 47 :
 GEVID ( )
 if 65 - 65: O0 * i11iIiiIii . OoooooooOO / OOOo0 / oO0o0ooO0
elif IiiI11I1IIiI == 48 :
 ii1111iII ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 69 - 69: o0oO0 % o0oO0
elif IiiI11I1IIiI == 49 :
 oOoOO0 ( )
 if 76 - 76: i11iIiiIii * oO0o0ooO0 / Ooo00oOo00o % ii11ii1ii + OoOO0ooOOoo0O
elif IiiI11I1IIiI == 222 :
 I111i1I1 ( o0o )
 if 48 - 48: iIii1I11I1II1 % i1IIi + I1IiI % OOooOOo
elif IiiI11I1IIiI == 333 :
 i1I11iIII1i1I ( o0o )
 if 79 - 79: I1IiI % OOOo0 % o00O0oo / i1IIi % Ooo00oOo00o
 if 56 - 56: iIii1I11I1II1 - i11iIiiIii * oO0o0ooO0
elif IiiI11I1IIiI == 1001 :
 oo0OoOooo ( )
 if 84 - 84: OoOO0ooOOoo0O + o00O0oo + OOooOOo
elif IiiI11I1IIiI == 1005 :
 i1II ( )
 if 33 - 33: o00O0oo
elif IiiI11I1IIiI == 1007 :
 IiiI11i1I ( o0o )
 if 93 - 93: o0oO0
elif IiiI11I1IIiI == 1010 :
 OooO0oOo ( )
 if 34 - 34: OoOO - o0oO0 * Oo / OOooOOo
elif IiiI11I1IIiI == 1011 :
 oOOo00O0OOOo ( o0o )
 if 19 - 19: ii11ii1ii
elif IiiI11I1IIiI == 1012 :
 I1i1iii1Ii ( o0o )
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
elif IiiI11I1IIiI == 1006 :
 Parse . ParseURL ( o0o )
 if 66 - 66: O0
elif IiiI11I1IIiI == 2030 :
 Parse . addonParseURL ( o0o )
 if 52 - 52: Ooo00oOo00o * OoooooooOO
elif IiiI11I1IIiI == 2031 :
 Parse . apkParseURL ( o0o )
 if 12 - 12: O0 + IIII * i1IIi . Ooo00oOo00o
elif IiiI11I1IIiI == 1002 :
 oOoooO0 ( o0o )
 if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
elif IiiI11I1IIiI == 1003 :
 Ii11 ( o0o )
 if 28 - 28: iIii1I11I1II1
elif IiiI11I1IIiI == 1004 :
 iIiiOO0OoOOO0 ( o0o )
 if 7 - 7: OOooOOo % IIII * I1IiI
elif IiiI11I1IIiI == 1008 :
 M3UCATS ( )
 if 58 - 58: IIII / o0000oOoOoO0o + OoOoOO00 % oO0o0ooO0 - OoooooooOO
elif IiiI11I1IIiI == 1009 :
 M3UPLAY ( o0o )
 if 25 - 25: I1IiI % OoooooooOO * Oo - i1IIi * OoOoOO00 * OoOO
elif IiiI11I1IIiI == 2001 :
 i1OoOO ( o0o )
 if 30 - 30: o0000oOoOoO0o % I1IiI / ii11ii1ii * O0 * o00O0oo . OOOo0
elif IiiI11I1IIiI == 1013 :
 OOO ( )
 if 46 - 46: I1IiI - O0
elif IiiI11I1IIiI == 1014 :
 OO ( )
 if 70 - 70: o0000oOoOoO0o + Oo * iIii1I11I1II1 . OOOo0 * o0000oOoOoO0o
elif IiiI11I1IIiI == 1015 :
 OOo ( o0o )
 if 49 - 49: OOooOOo
elif IiiI11I1IIiI == 1016 :
 oOo0o0O ( )
 if 25 - 25: oO0o0ooO0 . OoooooooOO * iIii1I11I1II1 . OOooOOo / O0 + o00O0oo
elif IiiI11I1IIiI == 1017 :
 IIIIiii ( o0o )
 if 68 - 68: Oo
elif IiiI11I1IIiI == 1018 :
 oO0o ( o0o )
 if 22 - 22: OoOO0ooOOoo0O
elif IiiI11I1IIiI == 1019 :
 IIIii1iiIi ( o0o )
 if 22 - 22: oO0o0ooO0 * o0000oOoOoO0o - Oo * O0 / i11iIiiIii
elif IiiI11I1IIiI == 1023 :
 Iii111II ( )
 if 78 - 78: Oo * O0 / o0oO0 + OoooooooOO + OoOO0ooOOoo0O
elif IiiI11I1IIiI == 1024 :
 I11I1IIiiII1 ( )
 if 23 - 23: oO0o0ooO0 % OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
elif IiiI11I1IIiI == 1025 :
 IIIIIii1ii11 ( o0o )
 if 94 - 94: i1IIi
elif IiiI11I1IIiI == 1026 :
 IiIIiIIIiIii ( )
 if 36 - 36: OOOo0 + Oo
elif IiiI11I1IIiI == 1027 :
 I1iIi1iiiIiI ( o0o )
 if 46 - 46: oO0o0ooO0
elif IiiI11I1IIiI == 1028 :
 III1I1Ii11iI ( o0o )
 if 65 - 65: i1IIi . ii11ii1ii / o0oO0
elif IiiI11I1IIiI == 1029 :
 oO00OoOO ( o0o )
 if 11 - 11: IIII * o0oO0 / o0oO0 - OoOO0ooOOoo0O
elif IiiI11I1IIiI == 4001 :
 oOOO0o0o ( )
 if 68 - 68: OOOo0 % IIII - IIII / OOOo0 + ii11ii1ii - Oo
elif IiiI11I1IIiI == 4002 :
 iiI1 ( )
 if 65 - 65: o0oO0 - i1IIi
elif IiiI11I1IIiI == 4003 :
 O0o0Ooo ( )
 if 62 - 62: o0000oOoOoO0o / OoOO % Oo . OoooooooOO / i11iIiiIii / O0oO
elif IiiI11I1IIiI == 3000 :
 o0 ( )
 if 60 - 60: OOOo0 % OoOO / OOooOOo % OoOO * i11iIiiIii / oO0o0ooO0
elif IiiI11I1IIiI == 404 :
 iIIiiIIi1IiI ( Ii1i1 , o0o , iiIii )
 if 34 - 34: O0oO - OoOO0ooOOoo0O
elif IiiI11I1IIiI == 7030 :
 i111 ( )
 if 25 - 25: OoOO % OOOo0 + i11iIiiIii + O0 * OoooooooOO
elif IiiI11I1IIiI == 7021 :
 ii1iI ( Ii1i1 )
 if 64 - 64: i1IIi
elif IiiI11I1IIiI == 7022 :
 OOOoO000 ( Ii1i1 )
 if 10 - 10: O0oO % O0 / OOOo0 % o0000oOoOoO0o
elif IiiI11I1IIiI == 7000 :
 OOoOoo0 ( Ii1i1 , o0o , img )
 if 25 - 25: OoOoOO00 / Ooo00oOo00o
elif IiiI11I1IIiI == 7002 :
 o0oO0oOO ( )
 if 64 - 64: O0 % o0oO0
elif IiiI11I1IIiI == 7003 :
 II1I1iiIII1I1 ( o0o )
 if 40 - 40: OOooOOo + o0000oOoOoO0o
elif IiiI11I1IIiI == 7004 :
 ii1iii11i1 ( o0o )
 if 77 - 77: i11iIiiIii % IIII + O0oO % OoooooooOO - o0000oOoOoO0o
elif IiiI11I1IIiI == 7020 :
 OOO00oo0ooO ( o0o )
 if 26 - 26: Oo + O0 - iIii1I11I1II1
elif IiiI11I1IIiI == 7001 :
 i11I1iIi ( )
 if 47 - 47: OoooooooOO
elif IiiI11I1IIiI == 7010 :
 oOoO00 ( o0o )
 if 2 - 2: I1IiI % O0oO * Oo * I1IiI
elif IiiI11I1IIiI == 7011 :
 O0O0oOOo0O ( o0o )
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
elif IiiI11I1IIiI == 7012 :
 ii1oOoO0o0ooo ( o0o )
 if 26 - 26: OOooOOo % OoOO0ooOOoo0O + OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / oO0o0ooO0
elif IiiI11I1IIiI == 7013 :
 cnfTVPlay2 ( o0o )
elif IiiI11I1IIiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( o0o )
elif IiiI11I1IIiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( o0o )
elif IiiI11I1IIiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Ii1i1 , o0o , iiIii )
elif IiiI11I1IIiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IiiI11I1IIiI == 7018 :
 OOo00 ( )
elif IiiI11I1IIiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( o0o )
elif IiiI11I1IIiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( o0o )
elif IiiI11I1IIiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( o0o )
 if 64 - 64: OoOO % I1IiI / OoOoOO00 % o0oO0 - oO0o0ooO0
elif IiiI11I1IIiI == 8000 :
 o0O0O0ooo0oOO ( )
elif IiiI11I1IIiI == 8001 :
 O00oOo00o0o ( )
elif IiiI11I1IIiI == 8002 :
 i1iiIiI1Ii1i ( )
elif IiiI11I1IIiI == 8003 :
 ii1 ( )
elif IiiI11I1IIiI == 8004 :
 II1i ( )
elif IiiI11I1IIiI == 8005 :
 ooo000ooO0000 ( )
elif IiiI11I1IIiI == 8006 :
 I1Ii1111iIi ( Ii1i1 , o0o )
elif IiiI11I1IIiI == 8030 :
 iii1i ( o0o )
elif IiiI11I1IIiI == 8040 :
 o0ooo0 ( )
elif IiiI11I1IIiI == 8041 :
 oOOOoo00 ( o0o )
elif IiiI11I1IIiI == 8042 :
 OOOoO00 ( o0o )
elif IiiI11I1IIiI == 8043 :
 yt . PlayVideo ( o0o )
elif IiiI11I1IIiI == 8044 :
 I1II1I11I1I ( o0o )
elif IiiI11I1IIiI == 8060 :
 I11IIIi ( )
elif IiiI11I1IIiI == 8061 :
 I1iI ( o0o )
elif IiiI11I1IIiI == 8070 :
 oo0000ooooO0o ( )
elif IiiI11I1IIiI == 8071 :
 ooo00Ooo ( o0o )
elif IiiI11I1IIiI == 8081 :
 oo0oOoo ( )
elif IiiI11I1IIiI == 8062 :
 O000OoOO0 ( o0o )
elif IiiI11I1IIiI == 8063 :
 oO00oo0o00o0o ( o0o )
elif IiiI11I1IIiI == 8050 :
 O0o0o00OO0000 ( )
elif IiiI11I1IIiI == 8051 :
 I1i ( o0o )
elif IiiI11I1IIiI == 8052 :
 o00Oo0oooooo ( o0o )
elif IiiI11I1IIiI == 8085 :
 oo00o0 ( )
elif IiiI11I1IIiI == 8086 :
 i1OOO0000oO ( o0o )
elif IiiI11I1IIiI == 8087 :
 O0OoooO0 ( o0o )
elif IiiI11I1IIiI == 8088 :
 ooo0O0o00O ( o0o , Ii1i1 )
elif IiiI11I1IIiI == 9000 :
 i1II1 ( )
elif IiiI11I1IIiI == 9001 :
 OoooO ( )
elif IiiI11I1IIiI == 9002 :
 I11i1II ( )
elif IiiI11I1IIiI == 9003 :
 iIi1Ii1i1iI ( )
elif IiiI11I1IIiI == 50 :
 Ii11I1 ( o0o )
elif IiiI11I1IIiI == 9020 :
 i11O0oo0OO0oOOOo ( )
elif IiiI11I1IIiI == 9021 :
 oOOOoo ( )
elif IiiI11I1IIiI == 9022 :
 Ii1ii111i1 ( )
elif IiiI11I1IIiI == 9023 :
 i1i1i1I ( )
elif IiiI11I1IIiI == 9024 :
 I111IiiIi1 ( o0o )
 if 2 - 2: O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
 if 26 - 26: OoOO0ooOOoo0O * Oo
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
