# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
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
iIii1 = "2.3.2"
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
 O0O00o0OOO0 ( '[COLORgreen]SCRAPED IPTV[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2lwdHYuZmlsbW92ZXIuY29tLw==' ) ) , 9030 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SEARCH[/COLOR]' , II , 9000 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]GenieTv VOD[/COLOR]' , II , 1005 , OOooO0OOoo + 'vod.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CHAMPION IPTV[/COLOR]' , II , 9020 , OOooO0OOoo + 'UKiptvandvod.png' , ii11iIi1I , 'UK IPTV AND HD VOD' )
 if 18 - 18: OOooOOo
 if 28 - 28: OoOO0ooOOoo0O - IIII . IIII + I1IiI - OoooooooOO + O0
 O0O00o0OOO0 ( '[COLORgreen]SCRAPED VOD[/COLOR]' , II , 7050 , OOooO0OOoo + 'vod.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , II , 1023 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]THE REAPER[/COLOR]' , II , 1016 , OOooO0OOoo + 'reap.png' , ii11iIi1I , '' )
 if 95 - 95: Ooo00oOo00o % OoOO . O0
 O0O00o0OOO0 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , II , 8040 , OOooO0OOoo + 'documentary.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]CLASSIC TOONS[/COLOR]' , II , 8050 , OOooO0OOoo + 'classictoons.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]M3U STREAMS[/COLOR]' , II , 8070 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 if 15 - 15: o0oO0 / o00O0oo . o00O0oo - i1IIi
 if 53 - 53: IIII + OOOo0 * OoOO
 O0O00o0OOO0 ( '[COLORgreen]ANIME[/COLOR]' , II , 1001 , OOooO0OOoo + 'anime.png' , ii11iIi1I , '' )
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
 O0O00o0OOO0 ( '[COLORgreen]RADIO[/COLOR]' , II , 1013 , OOooO0OOoo + 'radio.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC[/COLOR]' , II , 1030 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , II + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , II , 1111 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
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
 O0O0Oo00 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iIi ) . replace ( ' ' , '+' )
 if 80 - 80: OoOO + OoOO0ooOOoo0O / o0000oOoOoO0o
 IiiiiI1i1Iii = I1i1i1 ( o0o )
 oOOO00O0O0OOo = I1i1i1 ( iiI )
 OOo00O = I1i1i1 ( iIiiiII )
 OooOOOO = I1i1i1 ( i1iI1 )
 iIIIiiI1i1i = I1i1i1 ( i11ii1ii11i )
 iIIIo0o0O = i11i1I1 ( O0O0Oo00 )
 if 68 - 68: o0oO0
 if IiiiiI1i1Iii != 'Failed' :
  Oo0ooOo0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
  for iI1 , Ii1i1 in Oo0ooOo0o :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0o + iI1 ) , 222 , '' )
 if oOOO00O0O0OOo != 'Failed' :
  O00Oooo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oOOO00O0O0OOo )
  for iI1 , Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiI + iI1 ) , 222 , '' )
 if OOo00O != 'Failed' :
  iIIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOo00O )
  for iI1 , Ii1i1 in iIIi :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIiiiII + iI1 ) , 222 , '' )
 if OooOOOO != 'Failed' :
  oO0o00oo0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OooOOOO )
  for iI1 , Ii1i1 in oO0o00oo0 :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1iI1 + iI1 ) , 222 , '' )
 if iIIIiiI1i1i != 'Failed' :
  ii1IIII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIIiiI1i1i )
  for iI1 , i11I , Ii1i1 in ii1IIII :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + '[COLORgreen] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iI1 ) , 1006 , 'img' )
    if 59 - 59: OoOO * o0000oOoOoO0o % OoOoOO00
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if iIIIo0o0O != 'Failed' :
  ooo = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( iIIIo0o0O )
  for o0o , i11I , Ii1i1 in ooo :
   IIiI1i1i ( Ii1i1 + ' - Source 7' , o0o , 222 , i11I )
 IIiIiI1I = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 100 - 100: iIii1I11I1II1 + I1IiI / Oo . i11iIiiIii
 if 14 - 14: OOooOOo * OoOO0ooOOoo0O + oO0o0ooO0 + O0 + i11iIiiIii
 for oOoO0 in IIiIiI1I :
  Oo0 = iIII + oOoO0
  oo0O0o00o0O = I1i1i1 ( Oo0 )
  if iIIIiiI1i1i != 'Failed' :
   I11i1II = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( oo0O0o00o0O )
   for iI1 , Ii1i1 in I11i1II :
    if iIi in Ii1i1 . lower ( ) :
     IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iIII + oOoO0 + iI1 ) , 222 , '' )
     if 72 - 72: iIii1I11I1II1 . i1IIi / Oo . OoOoOO00
     o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
     if 54 - 54: OoOoOO00 % OoOoOO00
     if 86 - 86: O0 % o00O0oo * o0oO0 * iIii1I11I1II1 * i1IIi * o0000oOoOoO0o
def OOOoOOO0oO ( ) :
 if 28 - 28: o0oO0 + i11iIiiIii / o0000oOoOoO0o % I1IiI % Oo - O0
 iIi = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111I = iIi . lower ( )
 o0o = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 iiI = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 iIiiiII = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 i1iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 i11ii1ii11i = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIi ) . replace ( ' ' , '+' )
 ooO0OoOO = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 O0O0Oo00 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iIi ) . replace ( ' ' , '+' )
 if 54 - 54: i1IIi + OoOoOO00
 IiiiiI1i1Iii = I1i1i1 ( o0o )
 oOOO00O0O0OOo = I1i1i1 ( iiI )
 OOo00O = I1i1i1 ( iIiiiII )
 OooOOOO = I1i1i1 ( i1iI1 )
 iIIIiiI1i1i = I1i1i1 ( i11ii1ii11i )
 oo0O0o00o0O = I1i1i1 ( ooO0OoOO )
 iIIIo0o0O = i11i1I1 ( O0O0Oo00 )
 if IiiiiI1i1Iii != 'Failed' :
  Oo0ooOo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiiiiI1i1Iii )
  for Ii1i1 in Oo0ooOo0o :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0o + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 83 - 83: ii11ii1ii - OOOo0 + OoOO0ooOOoo0O
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if oOOO00O0O0OOo != 'Failed' :
  O00Oooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOOO00O0O0OOo )
  for Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiI + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 5 - 5: o00O0oo
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OOo00O != 'Failed' :
  iIIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOo00O )
  for Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiiiII + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 46 - 46: IIII
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OooOOOO != 'Failed' :
  oO0o00oo0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OooOOOO )
  for Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1iI1 + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 45 - 45: o0oO0
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if iIIIiiI1i1i != 'Failed' :
  ii1IIII = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iIIIiiI1i1i )
  for o0o , i11I , Ii1i1 in ii1IIII :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( Ii1i1 + ' - Source - Origin' , o0o , 8062 , i11I )
    if 21 - 21: OoOO . O0oO . OoOO0ooOOoo0O / Oo / O0oO
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if oo0O0o00o0O != 'Failed' :
  I11i1II = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo0O0o00o0O )
  for o0o , i11I , Ii1i1 in I11i1II :
   if iIi in Ii1i1 . lower ( ) :
    IIiI1i1i ( ( Ii1i1 + '[COLORgreen] source Scooby[/COLOR]' ) , o0o , 222 , 'img' )
    if 17 - 17: OoOO0ooOOoo0O / OoOO0ooOOoo0O / o0000oOoOoO0o
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if iIIIo0o0O != 'Failed' :
  ooo = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( iIIIo0o0O )
  for o0o , i11I , Ii1i1 in ooo :
   IIiI1i1i ( Ii1i1 + ' - Source 7' , o0o , 222 , i11I )
def ii1 ( ) :
 if 1 - 1: o0oO0 % iIii1I11I1II1 + Oo . iIii1I11I1II1 % OOOo0
 iIi = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111I = iIi . lower ( )
 o0o = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IiiiiI1i1Iii = i11i1I1 ( o0o )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 for Ii1i1 , i11I , o0o0oOoOO0O in Oo0ooOo0o :
  i1ii1II1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11I ) . replace ( '\\' , '' )
  if iIi in Ii1i1 . lower ( ) :
   I1111IIIIIi ( Ii1i1 , '' , 7022 , i1ii1II1ii )
   if 28 - 28: ii11ii1ii
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: OoOO0ooOOoo0O % OoOO0ooOOoo0O * OOooOOo / OOooOOo
 if 75 - 75: IIII . o0oO0
def iII111i ( url ) :
 IiiiiI1i1Iii = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for url , O0000o , ii , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( ( O0000o ) . replace ( 'Sezon' , ' Season ' ) + ( ii ) . replace ( 'Bölüm' , ' Episode ' ) + Ii1i1 , url , 8063 , '' )
  if 79 - 79: OOooOOo - o0000oOoOoO0o + OOooOOo . OoOO
  if 28 - 28: i1IIi - oO0o0ooO0
  if 54 - 54: oO0o0ooO0 - O0 % OoOO0ooOOoo0O
  if 73 - 73: O0 . I1IiI + OOOo0 - o0000oOoOoO0o % o0000oOoOoO0o . o0000oOoOoO0o
def I11ii1i1 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 222 , '' )
  if 78 - 78: oO0o0ooO0
  if 28 - 28: o0000oOoOoO0o
  if 58 - 58: I1IiI
  if 37 - 37: Oo - iIii1I11I1II1 / ii11ii1ii
def oo0oOOo0 ( ) :
 if 86 - 86: o0000oOoOoO0o * OOOo0 + o0000oOoOoO0o + OoOoOO00
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Oo0ooOo0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oOOO )
 for o0o , i11I , Ii1i1 , ii in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 + '  -  ' + ( ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o0o , 8063 , i11I )
  if 8 - 8: O0oO - oO0o0ooO0 / o0oO0
def oo0oOoo ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oOOO )
 for o0o , Ii1i1 , i11I in Oo0ooOo0o :
  IIiI1i1i ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , o0o , 8002 , i11I )
def oOOO0o00o ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oOOO )
 for i11I , time , url , Ii1i1 , IIiIi11i1i in Oo0ooOo0o :
  O0O00o0OOO0 ( '%s %s' % ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , time ) , url , 1015 , i11I , IIiIi11i1i )
  if 1 - 1: OOOo0 / IIII * o0oO0
def I1iIiIi11i11 ( ) :
 if 52 - 52: o0oO0 + O0 . oO0o0ooO0 . ii11ii1ii . Ooo00oOo00o
 I1111IIIIIi ( 'Coronation Street' , '' , 8001 , '' )
 I1111IIIIIi ( 'Eastenders' , '' , 8002 , '' )
 I1111IIIIIi ( 'Emmerdale' , '' , 8003 , '' )
 I1111IIIIIi ( 'Hollyoaks' , '' , 8004 , '' )
 I1111IIIIIi ( 'Im a Celebrity' , '' , 8005 , '' )
 if 97 - 97: OOOo0 / oO0o0ooO0
 if 71 - 71: OoOoOO00 / i1IIi . ii11ii1ii % OoooooooOO . I1IiI
 if 41 - 41: i1IIi * OoOoOO00 / OoooooooOO . OoOO0ooOOoo0O
 if 83 - 83: oO0o0ooO0 . O0 / Oo / OoOO0ooOOoo0O - OoOoOO00
def oO0oO0 ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Holly' in Ii1i1 :
   i11I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 14 - 14: oO0o0ooO0
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 99 - 99: oO0o0ooO0
def IIi1ii1Ii ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'East' in Ii1i1 :
   i11I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 91 - 91: i11iIiiIii / OoooooooOO + oO0o0ooO0 - i11iIiiIii + OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: OoOoOO00 / IIII
def IiII ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Emmer' in Ii1i1 :
   i11I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 7 - 7: OoooooooOO . IIII
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 53 - 53: o00O0oo % o00O0oo * OOooOOo + I1IiI
def Oooo00 ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Coro' in Ii1i1 :
   i11I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 6 - 6: o00O0oo - o0oO0 * OoOO0ooOOoo0O . oO0o0ooO0 / O0 * o0oO0
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: Oo % oO0o0ooO0 * ii11ii1ii / OoOO0ooOOoo0O % i11iIiiIii * o0000oOoOoO0o
def Oo00OoOo ( ) :
 IiiiiI1i1Iii = i11i1I1 ( 'http://uksoapshare.blogspot.co.uk/' )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( IiiiiI1i1Iii )
 for o0o , Ii1i1 in Oo0ooOo0o :
  if 'Celeb' in Ii1i1 :
   i11I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in o0o :
    IIiI1i1i ( ( Ii1i1 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0o . replace ( '\\/' , '/' ) , 8006 , i11I )
   else :
    pass
    if 24 - 24: i11iIiiIii - O0oO
def i11iiI1111 ( name , url ) :
 oOoooo000Oo00 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if oOoooo000Oo00 :
  OOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oOOO = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( oOOO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oOOO = open_url ( url )
  o00O00oO00 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( oOOO ) [ - 1 ]
  OOoo = o00O00oO00 . replace ( '\\/' , '/' )
 Ii1i1i1i1I1Ii = xbmcgui . ListItem ( name , '' , '' )
 Ii1i1i1i1I1Ii . setPath ( OOoo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1i1i1i1I1Ii )
 if 25 - 25: OoOoOO00
 if 11 - 11: Oo
def OOOOoO0O0oo0 ( ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzL2NhdGVnb3JpZXNfYWxs' ) )
 Oo0ooOo0o = re . compile ( 'class="vb_title_center"><a href="(.+?)" class="link"><b>(.+?)</b></a></div>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , o0o , 7051 , OOooO0OOoo + 'vod.png' )
  if 30 - 30: O0 * OoooooooOO
def I1iIIIi1 ( url ) :
 oOOO = i11i1I1
 Oo0ooOo0o = re . compile ( 'href="(.+?)" class=".+?">.+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( oOOO )
 for url , i11I , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , url , 222 , i11I )
  if 17 - 17: iIii1I11I1II1 . OoooooooOO / o0000oOoOoO0o % OoOoOO00 % i1IIi / i11iIiiIii
  if 58 - 58: Oo . OoOoOO00 + OoOO - i11iIiiIii / OoOoOO00 / O0
  if 85 - 85: I1IiI + OoOO0ooOOoo0O
  if 10 - 10: IIII / Ooo00oOo00o + I1IiI / i1IIi
  if 27 - 27: o00O0oo
def oO0OO0 ( ) :
 if 82 - 82: IIII - IIII + I1IiI
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
 if 8 - 8: OOooOOo % oO0o0ooO0 * OoOO % o00O0oo . o0oO0 / o0oO0
 if 81 - 81: Ooo00oOo00o
def oO0o00oOOooO0 ( Cat_Name ) :
 if 79 - 79: Ooo00oOo00o - iIii1I11I1II1 + o00O0oo - O0oO
 OoO = False
 iIIiii = '0'
 if Cat_Name == 'All Channels' : OoO = True
 if Cat_Name == 'Entertainment' : iIIiii = '1'
 if Cat_Name == 'Movies' : iIIiii = '2'
 if Cat_Name == 'Music' : iIIiii = '3'
 if Cat_Name == 'News' : iIIiii = '4'
 if Cat_Name == 'Sports' : iIIiii = '5'
 if Cat_Name == 'Documentary' : iIIiii = '6'
 if Cat_Name == 'Kids' : iIIiii = '7'
 if Cat_Name == 'Food' : iIIiii = '8'
 if Cat_Name == 'Religious' : iIIiii = '9'
 if Cat_Name == 'USA Channels' : iIIiii = '10'
 if Cat_Name == 'Other' : iIIiii = '11'
 if 61 - 61: IIII . i1IIi / O0oO % i11iIiiIii * oO0o0ooO0
 oOOO = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oOOO )
 print 'Len Match: >>>' + str ( len ( Oo0ooOo0o ) )
 for Ii1i1 , i11I , o0o0oOoOO0O in Oo0ooOo0o :
  i1ii1II1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11I ) . replace ( '\\' , '' )
  if o0o0oOoOO0O == iIIiii :
   I1111IIIIIi ( Ii1i1 , '' , 7022 , i1ii1II1ii )
  elif OoO == True :
   I1111IIIIIi ( Ii1i1 , '' , 7022 , i1ii1II1ii )
  else : pass
  if 31 - 31: OoOO0ooOOoo0O + O0
  xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 87 - 87: o0oO0
def IIIii ( Search_Name ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOOO )
 Oo0ooOo0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOOO )
 for i11I , o0o , iiI , iIiiiII in Oo0ooOo0o :
  i1ii1II1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11I ) . replace ( '\\' , '' )
  IIiI1i1i ( Search_Name + ': Link 1' , ( o0o ) . replace ( '\\' , '' ) , 222 , i1ii1II1ii )
  IIiI1i1i ( Search_Name + ': Link 2' , ( iiI ) . replace ( '\\' , '' ) , 222 , i1ii1II1ii )
  IIiI1i1i ( Search_Name + ': Link 3' , ( iIiiiII ) . replace ( '\\' , '' ) , 222 , i1ii1II1ii )
  if 83 - 83: IIII % OOooOOo % OOOo0 . iIii1I11I1II1 - IIII
def o00o ( ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Oo0ooOo0o = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oOOO )
 for Ii1i1 , o0o in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , ( o0o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOooO0OOoo + 'english.png' )
def Ii1IIiiIIi ( ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Oo0ooOo0o = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oOOO )
 for Ii1i1 , o0o in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , ( o0o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'xxx.png' )
def Oo000oi11I1iIi ( ) :
 oOOO = i11i1I1 ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Oo0ooOo0o = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oOOO )
 for Ii1i1 , o0o in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , ( o0o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'vod(1).png' )
  if 79 - 79: O0oO . OoOO - OoOoOO00 . OOOo0 % o0oO0
def oOoO00 ( url ) :
 url
 iI1IIIii = xbmcgui . ListItem ( Ii1i1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iI1IIIii )
 return
 if 7 - 7: IIII - o0000oOoOoO0o / OoOoOO00 * o00O0oo . oO0o0ooO0 * oO0o0ooO0
 if 61 - 61: o0000oOoOoO0o % o0oO0 - Ooo00oOo00o / Oo
def Ii1iI111 ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 9031 , OOooO0OOoo + 'icon.png' )
def O0oooo00o0Oo ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 9032 , OOooO0OOoo + 'icon.png' )
def I1iii ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( oOOO )
 for Ii1i1 , url in Oo0ooOo0o :
  if '://' in Ii1i1 :
   pass
   IIiI1i1i ( ( Ii1i1 ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOooO0OOoo + 'icon.png' )
def oO0o0O0Ooo0o ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oOOO )
 for Ii1i1 , url in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 222 , OOooO0OOoo + 'icon.png' )
  if 21 - 21: O0oO - OOOo0 + o0000oOoOoO0o
  if 78 - 78: OoooooooOO - i11iIiiIii - OoOoOO00
  if 77 - 77: I1IiI % o00O0oo
def II1IiiIii ( ) :
 oOOO = i11i1I1 ( 'http://tvshows.cnfstudio.com/' )
 Oo0ooOo0o = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , 'http://tvshows.cnfstudio.com/genre/' + o0o , 7010 , OOooO0OOoo + 'icon.png' )
  print '>>>>>>>>>>' + o0o
  if 84 - 84: OoOO % i1IIi
def oOO ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oOOO )
 Ii1II = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( oOOO )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oOOO )
 for i11I , url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( ( Ii1i1 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , i11I )
 Ii1II = Ii1II
 for url in Ii1II :
  I1111IIIIIi ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  I1111IIIIIi ( 'Next' , url , 7010 , '' )
  if 89 - 89: O0oO + OoooooooOO + O0oO * i1IIi + iIii1I11I1II1 % o0000oOoOoO0o
def oOo0oO ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( oOOO )
 for url , ii , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( ( 'Season' ) + ii + ( '  ' ) + Ii1i1 , url , 7004 , OOooO0OOoo + 'icon.png' )
  if 5 - 5: OoOO0ooOOoo0O - OoOO0ooOOoo0O . Oo + I1IiI - OoOO0ooOOoo0O . OoOO
def IiIi1i1ii ( url ) :
 if 11 - 11: OoOoOO00 / OOooOOo
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOooO0OOoo + 'icon.png' )
  if 21 - 21: i11iIiiIii / i1IIi + OOOo0 * OoOO0ooOOoo0O . O0oO
def OoOoo0oO ( name , url , img ) :
 IiiiiI1i1Iii = i11i1I1 ( url )
 iioo0o0OoOOO = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IiiiiI1i1Iii )
 ooO0oO00O0o = len ( iioo0o0OoOOO )
 if 70 - 70: O0oO
 if 16 - 16: oO0o0ooO0 - OoooooooOO % Oo
 if ooO0oO00O0o == 1 :
  for i11i1iIiii in iioo0o0OoOOO :
   i11i1iIiii = i11i1iIiii . replace ( 'player' , 'watch' )
   OOO00OO0oOo = i11i1iIiii + '&fv=&sou='
   I1I1iI = i11i1I1 ( OOO00OO0oOo )
   I1iIi1iiIIiI = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( I1I1iI )
   for oOoOOoOOooOO in I1iIi1iiIIiI :
    I11I = False
    Resolve ( oOoOOoOOooOO )
    if 6 - 6: ii11ii1ii + OoOO
 elif ooO0oO00O0o > 1 :
  if 48 - 48: iIii1I11I1II1 % i1IIi % oO0o0ooO0 + o0oO0
  for i11i1iIiii in iioo0o0OoOOO :
   Iiii11iIi1 = i11i1I1 ( i11i1iIiii )
   i1iI11I1II1 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Iiii11iIi1 )
   ii11II1i = i1iI11I1II1
   ii11II1i = ( str ( ii11II1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ii11II1i
   IIiI1i1i ( 'DOUBLE LINK' , ii11II1i , 424 , '' )
   if 58 - 58: Oo . IIII - Oo - O0oO * o00O0oo
   for url in i1iI11I1II1 :
    I1111IIIIIi ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iiI = Google . resolve ( url )
    except :
     pass
    try :
     IIiI11i1111Ii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iiI ) )
     for o00O0OoOO , O00o00O in IIiI11i1111Ii :
      if 3 - 3: OoOO0ooOOoo0O
      HD_URLS . append ( o00O0OoOO )
      SD_URLS . append ( O00o00O )
    except :
     pass
 else :
  pass
  if 20 - 20: OoOoOO00 . oO0o0ooO0 / OoOoOO00 % i11iIiiIii % oO0o0ooO0
def I11Ii11iI1 ( ) :
 if 39 - 39: OOOo0 * i11iIiiIii - OoOO / IIII % O0oO % o0000oOoOoO0o
 if 65 - 65: OoOO - o0oO0 % OoooooooOO / OoooooooOO % OoooooooOO
 I1111IIIIIi ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOooO0OOoo + 'Movies.png' )
 if 52 - 52: ii11ii1ii + ii11ii1ii . OoOoOO00
 I1111IIIIIi ( 'Search Movies' , '' , 7017 , OOooO0OOoo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 34 - 34: OoooooooOO . O0 / OoOO * I1IiI - ii11ii1ii
 if 36 - 36: i1IIi / O0 / Ooo00oOo00o - O0 - i1IIi
def ii1I11 ( ) :
 oOOO = i11i1I1 ( 'http://cnfstudio.com/' )
 Oo0ooOo0o = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , 'http://cnfstudio.com/genre/' + o0o , 7003 , OOooO0OOoo + 'icon.png' )
  if 99 - 99: OoOO0ooOOoo0O
i1iiIII111ii = xbmcgui . Dialog ( )
if 45 - 45: OoOO - OoOO0ooOOoo0O * O0oO / Oo * OoOoOO00 - O0oO
if 83 - 83: Ooo00oOo00o % IIII . OoooooooOO
def O0Oo ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oOOO )
 Ii1II = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oOOO )
 for i11I , url , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( ( Ii1i1 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , i11I )
 Ii1II = Ii1II
 for url in Ii1II :
  I1111IIIIIi ( 'Next Page' , url , 7003 , '' )
  if 7 - 7: IIII % iIii1I11I1II1 + o0000oOoOoO0o - o00O0oo * OoOO
def OOo ( url ) :
 if 9 - 9: o00O0oo
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  I1I1iIiII1 = url + '&fv=&sou='
  I1I1iIiII1 = I1I1iIiII1 . replace ( 'player' , 'watch' )
  OoOOiIII1I1i1i = o0O ( I1I1iIiII1 )
  IIiI1I1 = o0O ( url )
  if 15 - 15: o00O0oo * Oo % ii11ii1ii * iIii1I11I1II1 - i11iIiiIii
  if 60 - 60: OOOo0 * O0oO % Ooo00oOo00o + OoOO
def o0O ( url ) :
 if 52 - 52: i1IIi
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  o000 ( url )
  if 94 - 94: OOooOOo + O0 / o0000oOoOoO0o . OOOo0 + OoOO0ooOOoo0O . iIii1I11I1II1
  if 62 - 62: I1IiI / OOOo0 - ii11ii1ii - OOOo0 + i11iIiiIii + i1IIi
def I1i11II ( ) :
 O0O00o0OOO0 ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 O0O00o0OOO0 ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 31 - 31: OoOO / IIII * OOooOOo . OoOoOO00
def oooOO0OO0O ( url ) :
 Oo0ooOo0o = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for o00oIII11I , Ii1i1 , url in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 222 , OOooO0OOoo + 'streams.png' )
  if 17 - 17: OoooooooOO + OoOO0ooOOoo0O * o0000oOoOoO0o * I1IiI
  if 36 - 36: O0 + Oo
def iIIIi1i1I11i ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1007 , O0OOoO00OO0o )
def oOO0OO0OO ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , url , 1006 , O0OOoO00OO0o )
  if 87 - 87: OoOO + iIii1I11I1II1 - OoooooooOO
def IiI1 ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1027 , O0OOoO00OO0o )
  if 12 - 12: o0000oOoOoO0o % I1IiI
def i1i ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 1028 , O0OOoO00OO0o )
def IIi ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 333 , O0OOoO00OO0o )
def oo0OO ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 404 , O0OOoO00OO0o )
  if 2 - 2: OoOoOO00 - Ooo00oOo00o . IIII * oO0o0ooO0 / OoOO
def OOo0 ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1017 , O0OOoO00OO0o )
  if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
def OooOOo0 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 1018 , O0OOoO00OO0o )
def ooO000O ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 333 , O0OOoO00OO0o )
def oOIII111iiIi1 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( Ii1i1 , url , 404 , O0OOoO00OO0o )
  if 29 - 29: OoooooooOO + o00O0oo % iIii1I11I1II1 - OoOO0ooOOoo0O . OOOo0 % Oo
def I1IIi ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for o0o , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1007 , O0OOoO00OO0o )
def O0OOOo ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , url , 1006 , O0OOoO00OO0o )
  if 31 - 31: o0000oOoOoO0o % OoOO0ooOOoo0O * o0000oOoOoO0o
def IiI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I1i1iii1Ii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I1i1iii1Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1i1iii1Ii )
 if 23 - 23: i11iIiiIii
 if 39 - 39: OOooOOo - ii11ii1ii % oO0o0ooO0 * Ooo00oOo00o - OoOO0ooOOoo0O / oO0o0ooO0
def iIiiiiii1 ( url ) :
 oOOO = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOO )
 for url , i11I , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( '[COLORgreen]' + Ii1i1 + '[/COLOR]' , url , 1006 , i11I )
def oOO0oo ( url ) :
 oOOO = iIII1 ( url )
 II1iIi1IiIii = url
 Oo0ooOo0o = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  if '.mp3' in Ii1i1 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIiI1i1i ( ( Ii1i1 ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOooO0OOoo + 'music.png' )
  else :
   I1111IIIIIi ( ( Ii1i1 ) . replace ( '/' , '' ) , II1iIi1IiIii + url , 1011 , OOooO0OOoo + 'music.png' )
def I111I11I111 ( ) :
 oOOO = iIII1 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Oo0ooOo0o = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oOOO )
 for o0o , i11I , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , ( 'http://www.cyn.net/music/' + o0o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + i11I ) . replace ( ' ' , '%20' ) )
def iiiiI11ii ( url , img ) :
 oOOO = iIII1 ( url )
 iiI = url
 img = img
 Oo0ooOo0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( ( Ii1i1 ) . replace ( '.mp3' , '' ) , ( iiI + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 96 - 96: oO0o0ooO0 . O0 / oO0o0ooO0 % O0
  if 94 - 94: IIII + O0oO / OoOO0ooOOoo0O
def o00oiii11II1I ( ) :
 iIII = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iIi = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111I = iIi . lower ( )
 o0o = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iiI = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 iIiiiII = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 5 - 5: I1IiI - IIII * IIII
 IiiiiI1i1Iii = I1i1i1 ( o0o )
 oOOO00O0O0OOo = I1i1i1 ( iiI )
 OOo00O = I1i1i1 ( iIiiiII )
 if 50 - 50: OoOoOO00 * ii11ii1ii / o00O0oo . OOooOOo + Oo - OoOO0ooOOoo0O
 if IiiiiI1i1Iii != 'Failed' :
  Oo0ooOo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiiiiI1i1Iii )
  for Ii1i1 in Oo0ooOo0o :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0o + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 18 - 18: I1IiI % i11iIiiIii % ii11ii1ii / OoOO / OOooOOo / i1IIi
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if oOOO00O0O0OOo != 'Failed' :
  O00Oooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiiiiI1i1Iii )
  for Ii1i1 in O00Oooo :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiI + Ii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 48 - 48: I1IiI + o0000oOoOoO0o / IIII + OoOoOO00
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
 if OOo00O != 'Failed' :
  iIIi = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOo00O )
  for Ii1i1 in iIIi :
   if iIi in Ii1i1 . lower ( ) :
    I1111IIIIIi ( ( Ii1i1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiiiII + Ii1i1 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 18 - 18: ii11ii1ii
    o0oo0o0O00OO ( 'tvshows' , 'Media Info 3' )
    if 23 - 23: OoOoOO00
    if 24 - 24: iIii1I11I1II1 + iIii1I11I1II1 * oO0o0ooO0
    if 18 - 18: oO0o0ooO0 * o0000oOoOoO0o - o00O0oo
    if 31 - 31: Oo - O0 % I1IiI % OoOO
    if 45 - 45: ii11ii1ii + OoOoOO00 * i11iIiiIii
    if 13 - 13: OoooooooOO * OoOO - o00O0oo / OoOO0ooOOoo0O + o0000oOoOoO0o + IIII
def iii1III1i ( ) :
 oOOO = i11i1I1 ( 'http://www.animetoon.org/cartoon' )
 Oo0ooOo0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oOOO )
 for o0o , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , o0o , 1002 , OOooO0OOoo + 'anime.png' )
  if 17 - 17: OoOoOO00 / OoOoOO00
  if 65 - 65: IIII + Oo
  if 59 - 59: OoooooooOO + o0000oOoOoO0o . O0oO - O0 % iIii1I11I1II1 / O0
def OO ( url ) :
 oOOO = i11i1I1 ( url )
 O00Oooo = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oOOO )
 for i11I in O00Oooo :
  ooO0o = i11I
 iIIi = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( oOOO )
 for url in iIIi :
  I1111IIIIIi ( 'NEXT PAGE' , url , 1002 , ooO0o )
 Oo0ooOo0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oOOO )
 for url , Ii1i1 in Oo0ooOo0o :
  I1111IIIIIi ( Ii1i1 , url , 1003 , ooO0o )
 xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii1iI1iI1 ( url , IMAGE ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oOOO )
 for Ii1i1 , url in Oo0ooOo0o :
  print Ii1i1 + '     ' + url
  if 'easy' in url :
   o00oOOO ( url )
  elif 'playpanda' in url :
   o00oOOO ( url )
   if 57 - 57: OOOo0 - OOooOOo + Ooo00oOo00o % Oo
  xbmcplugin . addSortMethod ( Ooo , xbmcplugin . SORT_METHOD_TITLE ) ;
def o00oOOO ( url ) :
 oOOO = i11i1I1 ( url )
 Oo0ooOo0o = re . compile ( "url: '(.+?)'," ) . findall ( oOOO )
 for url in Oo0ooOo0o :
  IIiI1i1i ( 'STREAM' , url , 222 , OOooO0OOoo + 'anime.png' )
  if 26 - 26: oO0o0ooO0 . oO0o0ooO0
  if 35 - 35: O0oO . I1IiI * i11iIiiIii
def iiII ( url ) :
 OoO0O00O0oo0O = urllib2 . Request ( url )
 OoO0O00O0oo0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OoO0O00O0oo0O . add_header ( 'referer' , url )
 I1IiI11 = urllib2 . urlopen ( OoO0O00O0oo0O )
 I1I1iIiII1 = I1IiI11 . read ( )
 I1IiI11 . close ( )
 return I1I1iIiII1
 if 57 - 57: o0000oOoOoO0o . Oo + OoOoOO00
def iIII1 ( url ) :
 OoO0O00O0oo0O = urllib2 . Request ( url )
 OoO0O00O0oo0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1IiI11 = urllib2 . urlopen ( OoO0O00O0oo0O )
 I1I1iIiII1 = I1IiI11 . read ( )
 I1IiI11 . close ( )
 return I1I1iIiII1
 if 43 - 43: O0oO % oO0o0ooO0
def o0O0ooOOoO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iI = ( '%s%s' % ( i11ii , url ) )
 I1I1iIiII1 = iIII1 ( url )
 Oo0ooOo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1I1iIiII1 )
 for url , O0OOoO00OO0o , Ii1i1 in Oo0ooOo0o :
  IIiI1i1i ( '%s' % ( Ii1i1 ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , O0OOoO00OO0o )
  if 50 - 50: o00O0oo / I1IiI * o00O0oo
def o000 ( url ) :
 Ii1iIi111i1i1 = xbmc . Player ( IIOO0ooOo0OoOo0 ( ) )
 import urlresolver
 try : Ii1iIi111i1i1 . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( Ii1i1 ) )
 Ii1iIi111i1i1 = xbmc . Player ( IIOO0ooOo0OoOo0 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIII111ii = xbmcgui . Dialog ( )
  if i1iiIII111ii . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIII111ii . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : Ii1iIi111i1i1 . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 87 - 87: OoOO . OOOo0
  if 17 - 17: o00O0oo . i11iIiiIii
def IIOO0ooOo0OoOo0 ( ) :
 try :
  IIIiiiI = getSet ( "core-player" )
  if ( IIIiiiI == 'DVDPLAYER' ) : OoO00oo00 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IIIiiiI == 'MPLAYER' ) : OoO00oo00 = xbmc . PLAYER_CORE_MPLAYER
  elif ( IIIiiiI == 'PAPLAYER' ) : OoO00oo00 = xbmc . PLAYER_CORE_PAPLAYER
  else : OoO00oo00 = xbmc . PLAYER_CORE_AUTO
 except : OoO00oo00 = xbmc . PLAYER_CORE_AUTO
 return OoO00oo00
 return True
 if 76 - 76: OoooooooOO + Oo % IIII . Ooo00oOo00o + OoOoOO00
def I1111IIIIIi ( name , url , mode , iconimage ) :
 oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OooooOoO = True
 Ii1i1i1i1I1Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1i1I1Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OooooOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0o , listitem = Ii1i1i1i1I1Ii , isFolder = True )
 return OooooOoO
 if 38 - 38: IIII . o00O0oo
def IIiI1i1i ( name , url , mode , iconimage ) :
 oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OooooOoO = True
 Ii1i1i1i1I1Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1i1I1Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OooooOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0o , listitem = Ii1i1i1i1I1Ii , isFolder = False )
 return OooooOoO
 if 24 - 24: OOooOOo - OOooOOo + ii11ii1ii + OOOo0 - OoOO
 if 12 - 12: oO0o0ooO0 . IIII . I1IiI / O0
 if 58 - 58: OOooOOo - OoOoOO00 % OoOO + O0oO . I1IiI / IIII
 if 8 - 8: ii11ii1ii . Ooo00oOo00o * o0000oOoOoO0o + OoOoOO00 % i11iIiiIii
 if 8 - 8: o0oO0 * O0
 if 73 - 73: OOooOOo / OoOO / o0000oOoOoO0o / Ooo00oOo00o
 if 11 - 11: I1IiI + IIII - OoooooooOO / Ooo00oOo00o
def iIIi1iI1I1IIi ( heading , announce ) :
 class O0OO0 ( ) :
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
   try : Iii1I1111ii = open ( announce ) ; O0ooo0o0 = Iii1I1111ii . read ( )
   except : O0ooo0o0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0ooo0o0 ) )
   return
 O0OO0 ( )
 if 69 - 69: ii11ii1ii - O0oO
def iiIIi1 ( ) :
 iIIi1iI1I1IIi ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 10 - 10: o0000oOoOoO0o * o00O0oo % OoooooooOO
 if 83 - 83: O0oO - OOOo0 - ii11ii1ii % O0 . o00O0oo
 if 35 - 35: IIII + i1IIi * OoOO - o00O0oo . Oo
 if 31 - 31: OOooOOo
 if 15 - 15: O0 / Oo % ii11ii1ii + OOooOOo
def OO0Oooo0oOO0O ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 23 - 23: iIii1I11I1II1 + O0
 if 58 - 58: Oo
 if 9 - 9: iIii1I11I1II1 % ii11ii1ii . OoOO0ooOOoo0O + OoooooooOO
 if 62 - 62: O0 / OOOo0 % O0 * Ooo00oOo00o % OOOo0
 if 33 - 33: OOOo0 . OoOO * Ooo00oOo00o * iIii1I11I1II1
 if 5 - 5: Oo / IIII % O0 . O0oO * IIII
 if 83 - 83: OoOO0ooOOoo0O
 if 12 - 12: i1IIi . i1IIi - OOooOOo
 if 26 - 26: iIii1I11I1II1 % i11iIiiIii % ii11ii1ii
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
def oOoOo ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + oO0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 88 - 88: I1IiI - i11iIiiIii % OOooOOo * o0000oOoOoO0o + ii11ii1ii
def OoiIIIiIi1I1i ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + OoOOoO0oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 70 - 70: o0000oOoOoO0o % iIii1I11I1II1 . Oo + Oo - OOooOOo % O0oO
def i1IIi1i1Ii1 ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 63 - 63: IIII + OOooOOo
def IIIIIIII ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 86 - 86: OoOoOO00 * i11iIiiIii * OoooooooOO + OoOO % OoOO0ooOOoo0O
def OOO0 ( url ) :
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
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 34 - 34: i11iIiiIii - OoOoOO00 / OOOo0 % OOooOOo
def iI1IiiiI11 ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + OO0OO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 75 - 75: o0000oOoOoO0o / OOooOOo / OoOO0ooOOoo0O / IIII % o0oO0 + OoOoOO00
def I1III111i ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + iiI1iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 79 - 79: Ooo00oOo00o * I1IiI . OoooooooOO - o0000oOoOoO0o * OOooOOo
def o000o0O0Oo00 ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + ooOOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 42 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 90 - 90: OoOoOO00 / OOOo0
def iii ( url ) :
 I1I1iIiII1 = i11i1I1 ( II + OOooooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0ooOo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1iIiII1 )
 for Ii1i1 , url , iiIii , ooo0O , oOoO0o00OO0 in Oo0ooOo0o :
  O0O00o0OOO0 ( Ii1i1 , url , 5 , iiIii , ooo0O , oOoO0o00OO0 )
 o0oo0o0O00OO ( 'movies' , 'MAIN' )
 if 45 - 45: I1IiI
 if 68 - 68: O0
 if 43 - 43: ii11ii1ii - oO0o0ooO0
 if 70 - 70: oO0o0ooO0 / OoOO0ooOOoo0O % o0oO0 - o00O0oo
 if 47 - 47: oO0o0ooO0
 if 92 - 92: OoOO0ooOOoo0O + I1IiI % i1IIi
 if 23 - 23: O0oO - OoOO0ooOOoo0O + o00O0oo - I1IiI * I1IiI . Oo
 if 47 - 47: OoOO % iIii1I11I1II1
 if 11 - 11: OOOo0 % o00O0oo - Ooo00oOo00o - OoOO + OOooOOo
def o0O0O0 ( ) :
 try :
  if os . path . exists ( O0OoO000O0OO ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I1i1i1iii , I1111i , iIIii in os . walk ( O0OoO000O0OO ) :
     oo0OOOOO0 = 0
     oo0OOOOO0 += len ( iIIii )
     if oo0OOOOO0 > 0 :
      for Iii1I1111ii in iIIii :
       os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
  IiOOOo00 = os . path . join ( oOOoO0 , "Textures13.db" )
  os . unlink ( IiOOOo00 )
  i1iiIII111ii . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 91 - 91: iIii1I11I1II1 . OOooOOo . ii11ii1ii + OoooooooOO
 if 69 - 69: O0oO - OOOo0
 if 95 - 95: OOOo0 * i11iIiiIii . o0oO0
 if 41 - 41: OoOoOO00
 if 37 - 37: o0000oOoOoO0o . Oo % IIII * i1IIi
 if 71 - 71: Oo / OOooOOo + OoOO0ooOOoo0O
 if 48 - 48: O0oO + oO0o0ooO0
 if 16 - 16: iIii1I11I1II1 % i11iIiiIii . I1IiI % o0oO0 + OoOO . Ooo00oOo00o
 if 46 - 46: Ooo00oOo00o - OOooOOo / I1IiI - OoooooooOO + OoOO
def OOOO ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 I1iI1i11 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( I1iI1i11 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( I1iI1i11 ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 99 - 99: O0 + O0 * o0000oOoOoO0o + O0 * OoOO
   if 80 - 80: OOOo0 . o00O0oo
   if oo0OOOOO0 > 0 :
    if 47 - 47: o0000oOoOoO0o + o0oO0 + OoOoOO00 % i11iIiiIii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete KODI Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: ii11ii1ii % I1IiI . O0 / oO0o0ooO0 * OoOO
     for Iii1I1111ii in iIIii :
      try :
       os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
      except :
       pass
     for i1iii1ii in I1111i :
      try :
       shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      except :
       pass
       if 18 - 18: Ooo00oOo00o . OoOoOO00 % I1IiI % o00O0oo
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oo0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 16 - 16: o00O0oo * Ooo00oOo00o / OoOO
  for I1i1i1iii , I1111i , iIIii in os . walk ( oo0 ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 22 - 22: OoOO + iIii1I11I1II1 % Oo / o0000oOoOoO0o / o00O0oo
   if oo0OOOOO0 > 0 :
    if 54 - 54: I1IiI % IIII . i11iIiiIii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( oo0OOOOO0 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 93 - 93: o0oO0 % i11iIiiIii % O0oO
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 64 - 64: O0oO + OOOo0 * O0 / Oo - o0000oOoOoO0o % o0000oOoOoO0o
   else :
    pass
  o0oO00 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 2 - 2: iIii1I11I1II1
  for I1i1i1iii , I1111i , iIIii in os . walk ( o0oO00 ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 45 - 45: OoooooooOO / i11iIiiIii
   if oo0OOOOO0 > 0 :
    if 10 - 10: oO0o0ooO0 - OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - ii11ii1ii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( oo0OOOOO0 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 97 - 97: OoOoOO00 % O0oO + O0oO - Ooo00oOo00o / o00O0oo * OOOo0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 17 - 17: o00O0oo
   else :
    pass
    if 39 - 39: o0oO0 . OoOoOO00
    if 45 - 45: OoOO * I1IiI / iIii1I11I1II1
    if 77 - 77: O0oO - o0000oOoOoO0o
    if 11 - 11: ii11ii1ii
 iiI1Ii11II1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( iiI1Ii11II1I ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( iiI1Ii11II1I ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 44 - 44: o00O0oo % i11iIiiIii - oO0o0ooO0 * ii11ii1ii + Oo * OoOO0ooOOoo0O
   if 41 - 41: O0 * o0oO0 - I1IiI . o00O0oo
   if oo0OOOOO0 > 0 :
    if 65 - 65: Oo . OoooooooOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete WTF Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: Oo - OoOO . iIii1I11I1II1 % o0000oOoOoO0o / I1IiI - O0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 55 - 55: oO0o0ooO0 - Ooo00oOo00o
   else :
    pass
    if 100 - 100: O0
    if 79 - 79: iIii1I11I1II1
 O00oO0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( O00oO0o ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( O00oO0o ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 15 - 15: O0oO + o0000oOoOoO0o . OoooooooOO . i11iIiiIii
   if 31 - 31: OoooooooOO + oO0o0ooO0 - I1IiI . i1IIi % oO0o0ooO0
   if oo0OOOOO0 > 0 :
    if 43 - 43: OoOO0ooOOoo0O * o0oO0 / iIii1I11I1II1 - o00O0oo * o00O0oo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete 4oD Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 60 - 60: iIii1I11I1II1 . OoOO0ooOOoo0O + ii11ii1ii
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 44 - 44: O0 . OoOO * i11iIiiIii % i11iIiiIii + O0 / OoOO0ooOOoo0O
   else :
    pass
    if 89 - 89: o00O0oo % i1IIi % OoOO
    if 53 - 53: OoOO * OoooooooOO . I1IiI
 OOoooOoO0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( OOoooOoO0Oo ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( OOoooOoO0Oo ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 78 - 78: OoooooooOO / OoOO0ooOOoo0O % I1IiI * OoooooooOO
   if 68 - 68: OoOO
   if oo0OOOOO0 > 0 :
    if 29 - 29: oO0o0ooO0 + i11iIiiIii % o0000oOoOoO0o
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete BBC iPlayer Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: I1IiI % iIii1I11I1II1
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 90 - 90: OOOo0 - OoOO0ooOOoo0O / o00O0oo / O0 / o0000oOoOoO0o
   else :
    pass
    if 87 - 87: I1IiI / IIII + iIii1I11I1II1
    if 93 - 93: iIii1I11I1II1 + OoOO % o0oO0
    if 21 - 21: OoOO0ooOOoo0O
 iIiI1I1IIi11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( iIiI1I1IIi11 ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( iIiI1I1IIi11 ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 9 - 9: o0oO0 + oO0o0ooO0 - o0000oOoOoO0o / i1IIi % ii11ii1ii / IIII
   if 60 - 60: ii11ii1ii
   if oo0OOOOO0 > 0 :
    if 1 - 1: I1IiI . i11iIiiIii % I1IiI - oO0o0ooO0 % i1IIi + ii11ii1ii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Simple Downloader Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 2 - 2: iIii1I11I1II1 * OoOO / I1IiI . o0000oOoOoO0o / IIII
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 75 - 75: I1IiI
   else :
    pass
    if 78 - 78: o00O0oo + I1IiI + IIII - IIII . i11iIiiIii / Ooo00oOo00o
    if 27 - 27: o00O0oo - O0 % o0000oOoOoO0o * O0oO . IIII % iIii1I11I1II1
 IiIi1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IiIi1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( IiIi1i ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 99 - 99: I1IiI . O0oO
   if 59 - 59: o0000oOoOoO0o / Oo / OoOO0ooOOoo0O / O0 / I1IiI + OOooOOo
   if oo0OOOOO0 > 0 :
    if 13 - 13: OOooOOo % OoOO / O0oO % O0oO % O0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ITV Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: IIII . o0oO0 / iIii1I11I1II1
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 28 - 28: IIII + OoOO - o0oO0 / iIii1I11I1II1 - OOOo0
   else :
    pass
    if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
    if 35 - 35: ii11ii1ii / oO0o0ooO0 % OOOo0 + iIii1I11I1II1
 oO00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( IiIi1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( oO00o ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 36 - 36: O0oO . OoOoOO00 % o0oO0
   if 84 - 84: OoooooooOO - i11iIiiIii / iIii1I11I1II1 / OoooooooOO / ii11ii1ii
   if oo0OOOOO0 > 0 :
    if 4 - 4: Oo + OOooOOo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Movies4me Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: Ooo00oOo00o * I1IiI
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 15 - 15: i11iIiiIii / o0oO0 % OOOo0
   else :
    pass
    if 71 - 71: O0oO / ii11ii1ii * iIii1I11I1II1
    if 57 - 57: OoOO0ooOOoo0O + O0oO % ii11ii1ii . Ooo00oOo00o / Ooo00oOo00o * O0
 Ii1iiII1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( IiIi1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( Ii1iiII1i ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 52 - 52: OoOO / O0oO
   if 91 - 91: IIII . Oo + OoOoOO00
   if oo0OOOOO0 > 0 :
    if 36 - 36: O0 * Ooo00oOo00o % oO0o0ooO0 * oO0o0ooO0 / Ooo00oOo00o * IIII
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Phoenix Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: i1IIi . IIII + O0 * o0oO0
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 76 - 76: Ooo00oOo00o
   else :
    pass
    if 92 - 92: o0000oOoOoO0o - iIii1I11I1II1 % OoooooooOO
    if 39 - 39: oO0o0ooO0 . OOOo0 * I1IiI - i11iIiiIii
 i1II1II1iii1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( IiIi1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i1II1II1iii1i ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 75 - 75: IIII - I1IiI - iIii1I11I1II1 % OOooOOo
   if 58 - 58: O0 . IIII / OoooooooOO . Ooo00oOo00o / Oo * OoOoOO00
   if oo0OOOOO0 > 0 :
    if 53 - 53: o00O0oo - O0 / OOooOOo % oO0o0ooO0 * OOOo0 % OoOO0ooOOoo0O
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Music Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 69 - 69: ii11ii1ii
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 83 - 83: OOooOOo
   else :
    pass
    if 38 - 38: O0oO + OoooooooOO . i1IIi
    if 19 - 19: oO0o0ooO0 - OOooOOo - o00O0oo - I1IiI . oO0o0ooO0 . O0oO
 i11I1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( IiIi1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i11I1I ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 71 - 71: oO0o0ooO0
   if 23 - 23: i1IIi . iIii1I11I1II1 . OoOO0ooOOoo0O . O0 % o00O0oo % i11iIiiIii
   if oo0OOOOO0 > 0 :
    if 11 - 11: O0 - OoOoOO00 . OoOO0ooOOoo0O . o00O0oo % O0oO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete SuperCartoons Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: Oo / oO0o0ooO0 . O0oO * OoooooooOO + o0000oOoOoO0o - i1IIi
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 58 - 58: ii11ii1ii
   else :
    pass
    if 2 - 2: OoOoOO00 / O0oO
    if 54 - 54: i1IIi . o0000oOoOoO0o - ii11ii1ii + o0oO0 + Oo / Oo
 i1ii1IiiiiIi1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( IiIi1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( i1ii1IiiiiIi1I ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 56 - 56: OoooooooOO * O0
   if 85 - 85: OoooooooOO % I1IiI * iIii1I11I1II1
   if oo0OOOOO0 > 0 :
    if 44 - 44: iIii1I11I1II1 . ii11ii1ii + O0oO . o0oO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete TVonline Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: ii11ii1ii + iIii1I11I1II1 * o0000oOoOoO0o * o0000oOoOoO0o / OoOoOO00 - o00O0oo
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 65 - 65: OoOO + I1IiI + OoOoOO00
   else :
    pass
    if 77 - 77: OoOoOO00
    if 50 - 50: O0 . O0 . o0oO0 % Oo
 ooo000oOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( IiIi1i ) == True :
  for I1i1i1iii , I1111i , iIIii in os . walk ( ooo000oOO ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 27 - 27: OOooOOo * i11iIiiIii * Ooo00oOo00o
   if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
   if oo0OOOOO0 > 0 :
    if 87 - 87: I1IiI % iIii1I11I1II1
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 72 - 72: OoOO0ooOOoo0O . OoOO0ooOOoo0O - ii11ii1ii
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
      if 48 - 48: Oo - o0oO0 + Oo - OOOo0 * i11iIiiIii . oO0o0ooO0
   else :
    pass
    if 35 - 35: IIII . O0 + Oo + OoOO0ooOOoo0O + i1IIi
    if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
    if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
 O0O = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 try :
  if i1iiIII111ii . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   OOOOO0 = os . path . join ( O0O , "cache.db" )
   os . unlink ( OOOOO0 )
   if 79 - 79: OoOoOO00 - o0oO0 . i1IIi + O0 % O0 * OOOo0
 except :
  pass
  if 7 - 7: i1IIi + OoOO0ooOOoo0O % oO0o0ooO0 / OOooOOo + i1IIi
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 41 - 41: o00O0oo + i11iIiiIii / IIII % ii11ii1ii
 if 22 - 22: I1IiI % OOooOOo * o00O0oo - ii11ii1ii + OOooOOo - Oo
 if 15 - 15: OoOO0ooOOoo0O
 if 31 - 31: oO0o0ooO0 / i1IIi . Ooo00oOo00o
 if 83 - 83: OoOO / iIii1I11I1II1 + i1IIi / oO0o0ooO0
 if 47 - 47: OoOO + OoooooooOO . OoOoOO00 . oO0o0ooO0
 if 66 - 66: o0oO0 * I1IiI
 if 2 - 2: OoOO . O0oO * Oo + O0 - o0000oOoOoO0o * iIii1I11I1II1
 if 12 - 12: OOooOOo * O0oO % OoOoOO00 * i1IIi * iIii1I11I1II1
def oO0oOoo0O ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 II1iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i1i1iii , I1111i , iIIii in os . walk ( II1iI11 ) :
   oo0OOOOO0 = 0
   oo0OOOOO0 += len ( iIIii )
   if 88 - 88: o0000oOoOoO0o + i11iIiiIii % OoOO * OoOO0ooOOoo0O * OoOO0ooOOoo0O * o00O0oo
   if 24 - 24: o0oO0 / oO0o0ooO0 + IIII . IIII
   if oo0OOOOO0 > 0 :
    if 39 - 39: o0oO0 + O0 / i1IIi % IIII / OoOO * IIII
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Package Cache Files" , str ( oo0OOOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 77 - 77: IIII . O0oO % I1IiI
     for Iii1I1111ii in iIIii :
      os . unlink ( os . path . join ( I1i1i1iii , Iii1I1111ii ) )
     for i1iii1ii in I1111i :
      shutil . rmtree ( os . path . join ( I1i1i1iii , i1iii1ii ) )
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
 if 42 - 42: IIII % oO0o0ooO0 % OOooOOo % OoOO + o0000oOoOoO0o % I1IiI
 if 3 - 3: OoOO
 if 64 - 64: Ooo00oOo00o . OOOo0 - OoooooooOO . o0oO0 - oO0o0ooO0
 if 77 - 77: o00O0oo % I1IiI / OoOoOO00 % oO0o0ooO0 % OoooooooOO % Ooo00oOo00o
 if 19 - 19: IIII * O0oO / OoOO * O0oO - OoooooooOO * o0000oOoOoO0o
 if 17 - 17: OoOoOO00 + Oo . O0oO
 if 12 - 12: O0oO + OoOO0ooOOoo0O + o0000oOoOoO0o . IIII / o00O0oo
 if 29 - 29: IIII . o0oO0 - OoOoOO00
 if 68 - 68: iIii1I11I1II1 + OoOoOO00 / OoOO
def oOooo00000 ( url , name ) :
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iiI11I1iiIiII1I = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 o00ooOoo = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml.bak' )
 if os . path . exists ( o00ooOoo ) == False :
  if i1iiIII111ii . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iiI11I1iiIiII1I = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
   try :
    os . remove ( iiI11I1iiIiII1I )
    print '=== GenieTv - REMOVING    ' + str ( iiI11I1iiIiII1I ) + '    ==='
   except :
    pass
   I1I1iIiII1 = I11 . http_GET ( url ) . content
   o00O0O = open ( iiI11I1iiIiII1I , "w" )
   o00O0O . write ( I1I1iIiII1 )
   o00O0O . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iiI11I1iiIiII1I ) + '    ==='
   i1iiIII111ii = xbmcgui . Dialog ( )
   i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iiI11I1iiIiII1I = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
  try :
   os . remove ( iiI11I1iiIiII1I )
   print '=== GenieTv - REMOVING    ' + str ( iiI11I1iiIiII1I ) + '    ==='
  except :
   pass
  I1I1iIiII1 = I11 . http_GET ( url ) . content
  o00O0O = open ( iiI11I1iiIiII1I , "w" )
  o00O0O . write ( I1I1iIiII1 )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iiI11I1iiIiII1I ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 5 - 5: IIII
def Oo0O0oo0o00o0 ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iiI11I1iiIiII1I = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
 try :
  o00O0O = open ( iiI11I1iiIiII1I ) . read ( )
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
 if 66 - 66: iIii1I11I1II1 . i11iIiiIii / o0000oOoOoO0o / o0oO0 + O0oO
def iII11ii1ii ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iiI11I1iiIiII1I = os . path . join ( iiIi1IIi1I , 'advancedsettings.xml' )
 try :
  os . remove ( iiI11I1iiIiII1I )
  i1iiIII111ii = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iiI11I1iiIiII1I ) + '    ==='
  i1iiIII111ii . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 51 - 51: ii11ii1ii * ii11ii1ii
 if 98 - 98: Ooo00oOo00o - o00O0oo . IIII % i11iIiiIii
 if 69 - 69: ii11ii1ii + oO0o0ooO0 * O0 . OoOO0ooOOoo0O % I1IiI
 if 96 - 96: o0oO0 . o0oO0 - o0000oOoOoO0o / o0000oOoOoO0o
 if 96 - 96: i11iIiiIii / OOOo0 - O0 . o0oO0
 if 39 - 39: o0oO0 / O0 * IIII
 if 17 - 17: o00O0oo / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % OoOO0ooOOoo0O
 if 14 - 14: OOooOOo % IIII + ii11ii1ii + Ooo00oOo00o
 if 76 - 76: Ooo00oOo00o - i11iIiiIii + I1IiI + OoOO0ooOOoo0O / OoooooooOO
 if 50 - 50: OoOoOO00 - O0oO + iIii1I11I1II1 + iIii1I11I1II1
def OoooooOo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Oo0ooOo0o = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for OooOo , oOo0 , I1Ii11i , I1iIiiiI1 in Oo0ooOo0o :
  if inc < 2 : i1iiIII111ii = xbmcgui . Dialog ( ) ; i1iiIII111ii . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OooOo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I1Ii11i , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1iIiiiI1 )
  inc = inc + 1
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  iiI11I1iiIiII1I = os . path . join ( iiIi1IIi1I , 'addons2.ini' )
  I1I1iIiII1 = I11 . http_GET ( url ) . content
  o00O0O = open ( iiI11I1iiIiII1I , "w" )
  o00O0O . write ( I1I1iIiII1 )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iiI11I1iiIiII1I ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 21 - 21: i11iIiiIii
def o00iIiiiII ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  iiIi1IIi1I = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  iiI11I1iiIiII1I = os . path . join ( iiIi1IIi1I , 'settings.xml' )
  I1I1iIiII1 = I11 . http_GET ( url ) . content
  o00O0O = open ( iiI11I1iiIiII1I , "w" )
  o00O0O . write ( I1I1iIiII1 )
  o00O0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iiI11I1iiIiII1I ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 5 - 5: OoooooooOO / OOooOOo % o0000oOoOoO0o % Ooo00oOo00o * oO0o0ooO0 + iIii1I11I1II1
 if 11 - 11: O0oO % i11iIiiIii % OoOO . IIII
def oOO0o ( ) :
 try :
  o0OI1II = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( o0OI1II ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iIIi1Ii1III = os . path . join ( o0OI1II , "source.db" )
    os . unlink ( iIIi1Ii1III )
  i1iiIII111ii . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 86 - 86: i11iIiiIii + i11iIiiIii . O0oO % OOOo0 . o0oO0
 if 17 - 17: o00O0oo
 if 67 - 67: O0 * o0000oOoOoO0o - OOooOOo - OoOoOO00
 if 41 - 41: OOOo0 - O0oO % OoOoOO00 . O0oO - o0000oOoOoO0o
 if 45 - 45: o00O0oo - OoOO0ooOOoo0O
def i11i1I1 ( url ) :
 OoO0O00O0oo0O = urllib2 . Request ( url )
 OoO0O00O0oo0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IiI11 = urllib2 . urlopen ( OoO0O00O0oo0O )
 I1I1iIiII1 = I1IiI11 . read ( )
 I1IiI11 . close ( )
 return I1I1iIiII1
 if 70 - 70: Ooo00oOo00o % OOOo0 / OOOo0 . o0000oOoOoO0o % o0oO0 . OoOoOO00
 if 10 - 10: o00O0oo - i11iIiiIii . ii11ii1ii % i1IIi
 if 78 - 78: iIii1I11I1II1 * Oo . Oo - OoOO0ooOOoo0O . iIii1I11I1II1
 if 30 - 30: o0oO0 + o0oO0 % IIII - OOooOOo - ii11ii1ii
 if 36 - 36: o0000oOoOoO0o % OoOO0ooOOoo0O
 if 72 - 72: OOOo0 / oO0o0ooO0 - O0 + o0000oOoOoO0o
 if 83 - 83: O0
def oOOOOOo ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i1I11ii = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i1I11ii :
  o0ooO00O0O = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; o0ooO00O0O = xbmc . translatePath ( o0ooO00O0O ) ;
  iiiI1iI1 = os . path . join ( o0ooO00O0O , ".." , ".." ) ; iiiI1iI1 = os . path . abspath ( iiiI1iI1 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iiiI1iI1 ) ; I1 = False
  try :
   for I1i1i1iii , I1111i , iIIii in os . walk ( iiiI1iI1 , topdown = True ) :
    I1111i [ : ] = [ i1iii1ii for i1iii1ii in I1111i if i1iii1ii not in Oo0oO0ooo ]
    for Ii1i1 in iIIii :
     try : os . remove ( os . path . join ( I1i1i1iii , Ii1i1 ) )
     except :
      if Ii1i1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : I1 = True
      plugintools . log ( "Error removing " + I1i1i1iii + " " + Ii1i1 )
    for Ii1i1 in I1111i :
     try : os . rmdir ( os . path . join ( I1i1i1iii , Ii1i1 ) )
     except :
      if Ii1i1 not in [ "Database" , "userdata" ] : I1 = True
      plugintools . log ( "Error removing " + I1i1i1iii + " " + Ii1i1 )
   if not I1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 I111iI ( )
 if 89 - 89: I1IiI % iIii1I11I1II1
 if 35 - 35: ii11ii1ii + O0oO - I1IiI % OoOO % OOooOOo % I1IiI
 if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
def i111I11I ( ) :
 OoOoOOoO = [ ]
 ii1ii1i11I1I = sys . argv [ 2 ]
 if len ( ii1ii1i11I1I ) >= 2 :
  iiII1iiiiiii = sys . argv [ 2 ]
  iiIiii = iiII1iiiiiii . replace ( '?' , '' )
  if ( iiII1iiiiiii [ len ( iiII1iiiiiii ) - 1 ] == '/' ) :
   iiII1iiiiiii = iiII1iiiiiii [ 0 : len ( iiII1iiiiiii ) - 2 ]
  iiI1ii = iiIiii . split ( '&' )
  OoOoOOoO = { }
  for O0OooOO in range ( len ( iiI1ii ) ) :
   i1i1 = { }
   i1i1 = iiI1ii [ O0OooOO ] . split ( '=' )
   if ( len ( i1i1 ) ) == 2 :
    OoOoOOoO [ i1i1 [ 0 ] ] = i1i1 [ 1 ]
    if 68 - 68: o00O0oo - OOOo0
 return OoOoOOoO
 if 41 - 41: OoOO
o00ooO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
o0OoOO000ooO0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OO0OO0O00oO0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I11II1 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
ii1I = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
i1i1i1I = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
oO0OO = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OOOOOo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
OoOOoO0oOo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Iii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oOo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iIiIIi = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I1iiIi111I = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OO0OO0O = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiI1iii = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
ooOOoOo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iiIiI = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
OOooO = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oOOoOooOo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ii1ii11IIIiiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
Oo00oo0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oo0O0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OOooooOO = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
i11ii = base64 . decodestring ( 'Q1VOVA==' )
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description ) :
 oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OooooOoO = True
 Ii1i1i1i1I1Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1i1I1Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1i1I1Ii . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  OooooOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0o , listitem = Ii1i1i1i1I1Ii , isFolder = False )
 else :
  OooooOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0o , listitem = Ii1i1i1i1I1Ii , isFolder = True )
 return OooooOoO
def IIIIii ( name , url , mode , iconimage , fanart , description ) :
 oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OooooOoO = True
 Ii1i1i1i1I1Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1i1I1Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1i1I1Ii . setProperty ( "Fanart_Image" , fanart )
 OooooOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0o , listitem = Ii1i1i1i1I1Ii , isFolder = False )
 return OooooOoO
 if 28 - 28: o0oO0 - OoOO0ooOOoo0O / OOOo0
 if 27 - 27: i1IIi + OOOo0 * ii11ii1ii + OoOO0ooOOoo0O . OoOO
iiII1iiiiiii = i111I11I ( )
o0o = None
Ii1i1 = None
i1I111I1Iii1 = None
iiIii = None
ooo0O = None
oOoO0o00OO0 = None
if 68 - 68: oO0o0ooO0 + Oo % o00O0oo / i11iIiiIii % I1IiI
if 94 - 94: i11iIiiIii / O0oO / Oo
try :
 o0o = urllib . unquote_plus ( iiII1iiiiiii [ "url" ] )
except :
 pass
try :
 Ii1i1 = urllib . unquote_plus ( iiII1iiiiiii [ "name" ] )
except :
 pass
try :
 iiIii = urllib . unquote_plus ( iiII1iiiiiii [ "iconimage" ] )
except :
 pass
try :
 i1I111I1Iii1 = int ( iiII1iiiiiii [ "mode" ] )
except :
 pass
try :
 ooo0O = urllib . unquote_plus ( iiII1iiiiiii [ "fanart" ] )
except :
 pass
try :
 oOoO0o00OO0 = urllib . unquote_plus ( iiII1iiiiiii [ "description" ] )
except :
 pass
 if 9 - 9: o0000oOoOoO0o / I1IiI / OoOoOO00 + O0oO
 if 71 - 71: oO0o0ooO0 / Oo
print str ( iiI1IiI ) + ': ' + str ( iIii1 )
print "Mode: " + str ( i1I111I1Iii1 )
print "URL: " + str ( o0o )
print "Name: " + str ( Ii1i1 )
print "IconImage: " + str ( iiIii )
if 87 - 87: ii11ii1ii + ii11ii1ii - ii11ii1ii % O0
if 13 - 13: OoOoOO00
def o0oo0o0O00OO ( content , viewType ) :
 if 57 - 57: o00O0oo - OoooooooOO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 68 - 68: OOooOOo % ii11ii1ii / O0oO + O0oO - O0oO . Ooo00oOo00o
  if 100 - 100: I1IiI % Oo
if i1I111I1Iii1 == None :
 oOOO00o ( )
 if 76 - 76: OoOoOO00 / Ooo00oOo00o + OoooooooOO . ii11ii1ii . o0000oOoOoO0o . o0oO0
elif i1I111I1Iii1 == 1 :
 oOoooo0O0Oo ( o0o )
 if 43 - 43: i1IIi
elif i1I111I1Iii1 == 44 :
 o0oOO000oO0oo ( o0o )
 if 17 - 17: O0 - I1IiI
elif i1I111I1Iii1 == 2 :
 IiIiii1I1 ( )
 if 81 - 81: OOOo0 - iIii1I11I1II1 / OOOo0 / O0
elif i1I111I1Iii1 == 3 :
 Oo0O0O0ooO0O ( )
 if 34 - 34: o00O0oo * o00O0oo - ii11ii1ii - O0 . i11iIiiIii
elif i1I111I1Iii1 == 21 :
 Oo000o ( )
 if 32 - 32: iIii1I11I1II1 . Ooo00oOo00o * OoOO / OoOO0ooOOoo0O . OoOoOO00 - Oo
elif i1I111I1Iii1 == 4 :
 iIi1iIiii111 ( )
 if 10 - 10: ii11ii1ii / i11iIiiIii - o00O0oo + OoOO * OOOo0
elif i1I111I1Iii1 == 5 :
 Oo0O0oooo ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 94 - 94: OOOo0 + iIii1I11I1II1 / O0 - OoooooooOO % ii11ii1ii
elif i1I111I1Iii1 == 6 :
 oO0oOoo0O ( o0o )
 if 64 - 64: o0000oOoOoO0o + Ooo00oOo00o
elif i1I111I1Iii1 == 7 :
 oOooo00000 ( o0o , Ii1i1 )
 if 25 - 25: OOOo0 . o0oO0 + OOOo0 % o00O0oo * iIii1I11I1II1
elif i1I111I1Iii1 == 8 :
 Oo0O0oo0o00o0 ( o0o , Ii1i1 )
 if 31 - 31: i11iIiiIii + OoOO0ooOOoo0O - O0
elif i1I111I1Iii1 == 9 :
 FIXREPOSADDONS ( o0o )
 if 51 - 51: Ooo00oOo00o * i1IIi / o00O0oo * OoOO0ooOOoo0O + o0oO0 % ii11ii1ii
elif i1I111I1Iii1 == 10 :
 OO0Oooo0oOO0O ( )
 if 34 - 34: OoOO * OoooooooOO + o00O0oo + i11iIiiIii
elif i1I111I1Iii1 == 11 :
 iII11ii1ii ( o0o )
 if 22 - 22: i1IIi
elif i1I111I1Iii1 == 12 :
 OoooooOo ( )
 if 24 - 24: o0000oOoOoO0o / OOOo0 * i1IIi % OoooooooOO
elif i1I111I1Iii1 == 13 :
 o0O0O0 ( )
 if 99 - 99: i11iIiiIii . OoOoOO00 . OoooooooOO
elif i1I111I1Iii1 == 14 :
 OOOO ( o0o )
 if 59 - 59: i11iIiiIii . OoooooooOO / o0000oOoOoO0o * ii11ii1ii + OoooooooOO
elif i1I111I1Iii1 == 15 :
 oO00O0O0O ( )
 if 3 - 3: i11iIiiIii * Oo % iIii1I11I1II1 % OOOo0 * oO0o0ooO0 / OoOO0ooOOoo0O
elif i1I111I1Iii1 == 16 :
 OOo00ooOoO0o ( o0o , Ii1i1 )
 if 95 - 95: IIII * O0 * O0oO . OoooooooOO % Oo + ii11ii1ii
elif i1I111I1Iii1 == 17 :
 o00iIiiiII ( o0o , Ii1i1 )
 if 98 - 98: OoOO . OoooooooOO
elif i1I111I1Iii1 == 18 :
 oOO0o ( )
 if 54 - 54: O0 / IIII % o0oO0 * i1IIi * O0
elif i1I111I1Iii1 == 19 :
 oo000o ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 48 - 48: OOooOOo . OoOO % I1IiI - I1IiI
elif i1I111I1Iii1 == 40 :
 OooiIi1IiIiiII ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 33 - 33: o0000oOoOoO0o % OoOoOO00 + Ooo00oOo00o
elif i1I111I1Iii1 == 42 :
 oO0o0 ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 93 - 93: i1IIi . IIII / OOOo0 + IIII
elif i1I111I1Iii1 == 43 :
 O0oOOO0ooOOO0OOO ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 58 - 58: ii11ii1ii + O0 . Oo + I1IiI - Ooo00oOo00o - I1IiI
elif i1I111I1Iii1 == 20 :
 i1iIi1iIi1i ( o0o )
 if 41 - 41: Oo / i1IIi / Oo - oO0o0ooO0 . OOooOOo
elif i1I111I1Iii1 == 22 :
 oOoOo ( o0o )
 if 65 - 65: O0 * i11iIiiIii . OoooooooOO / OOOo0 / oO0o0ooO0
elif i1I111I1Iii1 == 23 :
 OoiIIIiIi1I1i ( o0o )
 if 69 - 69: o0oO0 % o0oO0
elif i1I111I1Iii1 == 24 :
 i1IIi1i1Ii1 ( o0o )
 if 76 - 76: i11iIiiIii * oO0o0ooO0 / Ooo00oOo00o % ii11ii1ii + OoOO0ooOOoo0O
elif i1I111I1Iii1 == 25 :
 IIIIIIII ( o0o )
 if 48 - 48: iIii1I11I1II1 % i1IIi + I1IiI % OOooOOo
elif i1I111I1Iii1 == 26 :
 OOO0 ( o0o )
 if 79 - 79: I1IiI % OOOo0 % o00O0oo / i1IIi % Ooo00oOo00o
elif i1I111I1Iii1 == 27 :
 I1iIiI1IiIIII ( o0o )
 if 56 - 56: iIii1I11I1II1 - i11iIiiIii * oO0o0ooO0
elif i1I111I1Iii1 == 28 :
 iI1IiiiI11 ( o0o )
 if 84 - 84: OoOO0ooOOoo0O + o00O0oo + OOooOOo
elif i1I111I1Iii1 == 29 :
 I1III111i ( o0o )
 if 33 - 33: o00O0oo
elif i1I111I1Iii1 == 30 :
 o0O0OOO0Ooo ( o0o )
 if 93 - 93: o0oO0
elif i1I111I1Iii1 == 31 :
 o000o0O0Oo00 ( o0o )
 if 34 - 34: OoOO - o0oO0 * Oo / OOooOOo
elif i1I111I1Iii1 == 32 :
 ii111111I1iII ( )
 if 19 - 19: ii11ii1ii
elif i1I111I1Iii1 == 33 :
 Ii ( )
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
elif i1I111I1Iii1 == 35 :
 O00oO000O0O ( o0o )
 if 66 - 66: O0
elif i1I111I1Iii1 == 34 :
 OOooo0O00o ( o0o )
 if 52 - 52: Ooo00oOo00o * OoooooooOO
elif i1I111I1Iii1 == 36 :
 O0oOoOOOoOO ( o0o )
 if 12 - 12: O0 + IIII * i1IIi . Ooo00oOo00o
elif i1I111I1Iii1 == 37 :
 I1I111 ( o0o )
 if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
elif i1I111I1Iii1 == 38 :
 OooOOOOo ( o0o )
 if 28 - 28: iIii1I11I1II1
elif i1I111I1Iii1 == 41 :
 oOOOOOo ( iiII1iiiiiii )
 if 7 - 7: OOooOOo % IIII * I1IiI
elif i1I111I1Iii1 == 39 :
 iii ( o0o )
 if 58 - 58: IIII / o0000oOoOoO0o + OoOoOO00 % oO0o0ooO0 - OoooooooOO
elif i1I111I1Iii1 == 45 :
 TEXTS ( )
 if 25 - 25: I1IiI % OoooooooOO * Oo - i1IIi * OoOoOO00 * OoOO
elif i1I111I1Iii1 == 46 :
 iiIIi1 ( )
 if 30 - 30: o0000oOoOoO0o % I1IiI / ii11ii1ii * O0 * o00O0oo . OOOo0
elif i1I111I1Iii1 == 47 :
 GEVID ( )
 if 46 - 46: I1IiI - O0
elif i1I111I1Iii1 == 48 :
 ii1111iII ( Ii1i1 , o0o , oOoO0o00OO0 )
 if 70 - 70: o0000oOoOoO0o + Oo * iIii1I11I1II1 . OOOo0 * o0000oOoOoO0o
elif i1I111I1Iii1 == 49 :
 oOoOO0 ( )
 if 49 - 49: OOooOOo
elif i1I111I1Iii1 == 222 :
 o000 ( o0o )
 if 25 - 25: oO0o0ooO0 . OoooooooOO * iIii1I11I1II1 . OOooOOo / O0 + o00O0oo
elif i1I111I1Iii1 == 333 :
 o0O0ooOOoO ( o0o )
 if 68 - 68: Oo
 if 22 - 22: OoOO0ooOOoo0O
elif i1I111I1Iii1 == 1001 :
 iii1III1i ( )
 if 22 - 22: oO0o0ooO0 * o0000oOoOoO0o - Oo * O0 / i11iIiiIii
elif i1I111I1Iii1 == 1005 :
 I1IIi ( )
 if 78 - 78: Oo * O0 / o0oO0 + OoooooooOO + OoOO0ooOOoo0O
elif i1I111I1Iii1 == 1007 :
 O0OOOo ( o0o )
 if 23 - 23: oO0o0ooO0 % OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
elif i1I111I1Iii1 == 1010 :
 iIiiiiii1 ( o0o )
 if 94 - 94: i1IIi
elif i1I111I1Iii1 == 1011 :
 oOO0oo ( o0o )
 if 36 - 36: OOOo0 + Oo
elif i1I111I1Iii1 == 1030 :
 I111I11I111 ( )
 if 46 - 46: oO0o0ooO0
elif i1I111I1Iii1 == 1031 :
 iiiiI11ii ( o0o , iiIii )
 if 65 - 65: i1IIi . ii11ii1ii / o0oO0
elif i1I111I1Iii1 == 1006 :
 Parse . ParseURL ( o0o )
 if 11 - 11: IIII * o0oO0 / o0oO0 - OoOO0ooOOoo0O
elif i1I111I1Iii1 == 2030 :
 Parse . addonParseURL ( o0o )
 if 68 - 68: OOOo0 % IIII - IIII / OOOo0 + ii11ii1ii - Oo
elif i1I111I1Iii1 == 2031 :
 Parse . apkParseURL ( o0o )
 if 65 - 65: o0oO0 - i1IIi
elif i1I111I1Iii1 == 1002 :
 OO ( o0o )
 if 62 - 62: o0000oOoOoO0o / OoOO % Oo . OoooooooOO / i11iIiiIii / O0oO
elif i1I111I1Iii1 == 1003 :
 ii1iI1iI1 ( o0o , iiIii )
 if 60 - 60: OOOo0 % OoOO / OOooOOo % OoOO * i11iIiiIii / oO0o0ooO0
elif i1I111I1Iii1 == 1004 :
 o00oOOO ( o0o )
 if 34 - 34: O0oO - OoOO0ooOOoo0O
elif i1I111I1Iii1 == 1008 :
 M3UCATS ( )
 if 25 - 25: OoOO % OOOo0 + i11iIiiIii + O0 * OoooooooOO
elif i1I111I1Iii1 == 1009 :
 M3UPLAY ( o0o )
 if 64 - 64: i1IIi
elif i1I111I1Iii1 == 2001 :
 oooOO0OO0O ( o0o )
 if 10 - 10: O0oO % O0 / OOOo0 % o0000oOoOoO0o
elif i1I111I1Iii1 == 1013 :
 OOO ( )
 if 25 - 25: OoOoOO00 / Ooo00oOo00o
elif i1I111I1Iii1 == 1014 :
 oo0oOoo ( )
 if 64 - 64: O0 % o0oO0
elif i1I111I1Iii1 == 1015 :
 oOOO0o00o ( o0o )
 if 40 - 40: OOooOOo + o0000oOoOoO0o
elif i1I111I1Iii1 == 1016 :
 OOo0 ( )
 if 77 - 77: i11iIiiIii % IIII + O0oO % OoooooooOO - o0000oOoOoO0o
elif i1I111I1Iii1 == 1017 :
 OooOOo0 ( o0o )
 if 26 - 26: Oo + O0 - iIii1I11I1II1
elif i1I111I1Iii1 == 1018 :
 ooO000O ( o0o )
 if 47 - 47: OoooooooOO
elif i1I111I1Iii1 == 1019 :
 oOIII111iiIi1 ( o0o )
 if 2 - 2: I1IiI % O0oO * Oo * I1IiI
elif i1I111I1Iii1 == 1023 :
 Iii111II ( )
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
elif i1I111I1Iii1 == 1024 :
 iIIIi1i1I11i ( )
 if 26 - 26: OOooOOo % OoOO0ooOOoo0O + OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / oO0o0ooO0
elif i1I111I1Iii1 == 1025 :
 oOO0OO0OO ( o0o )
 if 64 - 64: OoOO % I1IiI / OoOoOO00 % o0oO0 - oO0o0ooO0
elif i1I111I1Iii1 == 1026 :
 IiI1 ( )
 if 2 - 2: O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
elif i1I111I1Iii1 == 1027 :
 i1i ( o0o )
 if 26 - 26: OoOO0ooOOoo0O * Oo
elif i1I111I1Iii1 == 1028 :
 IIi ( o0o )
 if 31 - 31: o0000oOoOoO0o * OoOO . o00O0oo
elif i1I111I1Iii1 == 1029 :
 oo0OO ( o0o )
 if 35 - 35: o0000oOoOoO0o
elif i1I111I1Iii1 == 4001 :
 oOOO0o0o ( )
 if 94 - 94: o0oO0 / i11iIiiIii % O0
elif i1I111I1Iii1 == 4002 :
 iiI1 ( )
 if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
elif i1I111I1Iii1 == 4003 :
 O0o0Ooo ( )
 if 95 - 95: OoooooooOO % OoooooooOO . o00O0oo
elif i1I111I1Iii1 == 3000 :
 I1i11II ( )
 if 26 - 26: OoOO + IIII - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
elif i1I111I1Iii1 == 404 :
 IiI ( Ii1i1 , o0o , iiIii )
 if 68 - 68: O0
elif i1I111I1Iii1 == 7030 :
 oO0OO0 ( )
 if 76 - 76: ii11ii1ii
elif i1I111I1Iii1 == 7021 :
 oO0o00oOOooO0 ( Ii1i1 )
 if 99 - 99: OOooOOo
elif i1I111I1Iii1 == 7022 :
 IIIii ( Ii1i1 )
 if 1 - 1: o00O0oo * I1IiI * Ooo00oOo00o + Oo
elif i1I111I1Iii1 == 7000 :
 OoOoo0oO ( Ii1i1 , o0o , img )
 if 90 - 90: O0oO % Oo - Oo . iIii1I11I1II1 / OoOO0ooOOoo0O + o0000oOoOoO0o
elif i1I111I1Iii1 == 7050 :
 OOOOoO0O0oo0 ( )
 if 89 - 89: OoOO
elif i1I111I1Iii1 == 7001 :
 I1iIIIi1 ( o0o )
 if 87 - 87: oO0o0ooO0 % Oo
elif i1I111I1Iii1 == 7002 :
 ii1I11 ( )
 if 62 - 62: Ooo00oOo00o + o0oO0 / oO0o0ooO0 * i11iIiiIii
elif i1I111I1Iii1 == 7003 :
 O0Oo ( o0o )
 if 37 - 37: oO0o0ooO0
elif i1I111I1Iii1 == 7004 :
 OOo ( o0o )
 if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
elif i1I111I1Iii1 == 7020 :
 o0O ( o0o )
 if 94 - 94: IIII * o0000oOoOoO0o * OoooooooOO / OOooOOo . IIII - OOooOOo
elif i1I111I1Iii1 == 7001 :
 II1IiiIii ( )
 if 13 - 13: OoOO0ooOOoo0O / IIII - Ooo00oOo00o / OoOO0ooOOoo0O . i1IIi
elif i1I111I1Iii1 == 7010 :
 oOO ( o0o )
 if 22 - 22: O0 - o0000oOoOoO0o + O0oO . o00O0oo * i1IIi
elif i1I111I1Iii1 == 7011 :
 oOo0oO ( o0o )
 if 26 - 26: iIii1I11I1II1 * OOooOOo . o0000oOoOoO0o
elif i1I111I1Iii1 == 7012 :
 IiIi1i1ii ( o0o )
 if 10 - 10: O0oO * OoOO % Oo - o0000oOoOoO0o % Oo
elif i1I111I1Iii1 == 7013 :
 cnfTVPlay2 ( o0o )
elif i1I111I1Iii1 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( o0o )
elif i1I111I1Iii1 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( o0o )
elif i1I111I1Iii1 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Ii1i1 , o0o , iiIii )
elif i1I111I1Iii1 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif i1I111I1Iii1 == 7018 :
 I11Ii11iI1 ( )
elif i1I111I1Iii1 == 7019 :
 CNF_Studio_Indexer . List_Movies ( o0o )
elif i1I111I1Iii1 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( o0o )
elif i1I111I1Iii1 == 7024 :
 CNF_Studio_Indexer . Box_Office ( o0o )
 if 65 - 65: oO0o0ooO0 * iIii1I11I1II1 / O0 . o0000oOoOoO0o
elif i1I111I1Iii1 == 8000 :
 I1iIiIi11i11 ( )
elif i1I111I1Iii1 == 8001 :
 Oooo00 ( )
elif i1I111I1Iii1 == 8002 :
 IIi1ii1Ii ( )
elif i1I111I1Iii1 == 8003 :
 IiII ( )
elif i1I111I1Iii1 == 8004 :
 oO0oO0 ( )
elif i1I111I1Iii1 == 8005 :
 Oo00OoOo ( )
elif i1I111I1Iii1 == 8006 :
 i11iiI1111 ( Ii1i1 , o0o )
elif i1I111I1Iii1 == 8030 :
 iii1i ( o0o )
elif i1I111I1Iii1 == 8040 :
 o0ooo0 ( )
elif i1I111I1Iii1 == 8041 :
 oOOOoo00 ( o0o )
elif i1I111I1Iii1 == 8042 :
 OOOoO00 ( o0o )
elif i1I111I1Iii1 == 8043 :
 yt . PlayVideo ( o0o )
elif i1I111I1Iii1 == 8044 :
 I1II1I11I1I ( o0o )
elif i1I111I1Iii1 == 8060 :
 I11IIIi ( )
elif i1I111I1Iii1 == 8061 :
 I1iI ( o0o )
elif i1I111I1Iii1 == 8070 :
 oo0000ooooO0o ( )
elif i1I111I1Iii1 == 8071 :
 ooo00Ooo ( o0o )
elif i1I111I1Iii1 == 8081 :
 oo0oOOo0 ( )
elif i1I111I1Iii1 == 8062 :
 iII111i ( o0o )
elif i1I111I1Iii1 == 8063 :
 I11ii1i1 ( o0o )
elif i1I111I1Iii1 == 8050 :
 O0o0o00OO0000 ( )
elif i1I111I1Iii1 == 8051 :
 I1i ( o0o )
elif i1I111I1Iii1 == 8052 :
 o00Oo0oooooo ( o0o )
elif i1I111I1Iii1 == 8085 :
 oo00o0 ( )
elif i1I111I1Iii1 == 8086 :
 i1OOO0000oO ( o0o )
elif i1I111I1Iii1 == 8087 :
 O0OoooO0 ( o0o )
elif i1I111I1Iii1 == 8088 :
 ooo0O0o00O ( o0o , Ii1i1 )
elif i1I111I1Iii1 == 9000 :
 i1II1 ( )
elif i1I111I1Iii1 == 1111 :
 o00oiii11II1I ( )
elif i1I111I1Iii1 == 9001 :
 OoooO ( )
elif i1I111I1Iii1 == 9002 :
 OOOoOOO0oO ( )
elif i1I111I1Iii1 == 9003 :
 ii1 ( )
elif i1I111I1Iii1 == 50 :
 Ii11I1 ( o0o )
elif i1I111I1Iii1 == 9020 :
 i11O0oo0OO0oOOOo ( )
elif i1I111I1Iii1 == 9021 :
 o00o ( )
elif i1I111I1Iii1 == 9022 :
 Ii1IIiiIIi ( )
elif i1I111I1Iii1 == 9023 :
 Oo000oi11I1iIi ( )
elif i1I111I1Iii1 == 9024 :
 oOoO00 ( o0o )
elif i1I111I1Iii1 == 9030 :
 Ii1iI111 ( o0o )
elif i1I111I1Iii1 == 9031 :
 O0oooo00o0Oo ( o0o )
elif i1I111I1Iii1 == 9032 :
 I1iii ( o0o )
elif i1I111I1Iii1 == 9033 :
 oO0o0O0Ooo0o ( o0o )
 if 94 - 94: Oo . o0oO0 * i11iIiiIii - OOooOOo . oO0o0ooO0
 if 98 - 98: OoOO0ooOOoo0O + o00O0oo
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
