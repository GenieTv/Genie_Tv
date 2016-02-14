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
 ii11i1iIII ( '[COLORgreen]Origin[/COLOR]' , '' , 10000 , iIii1 , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]POPCORN BOX[/COLOR]' , ooOoOoo0O , 7061 , OOooO0OOoo + 'popcorn.png' , ii11iIi1I , '' )
 if 23 - 23: OOooOOo . OoOoOO00
 ii11i1iIII ( '[COLORgreen]RECENT EPISODES[/COLOR]' , ooOoOoo0O , 8081 , OOooO0OOoo + 'recent.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]ANIME[/COLOR]' , ooOoOoo0O , 1001 , OOooO0OOoo + 'anime.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]CLASSIC TOONS[/COLOR]' , ooOoOoo0O , 8050 , OOooO0OOoo + 'classictoons.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]CHAMPION IPTV[/COLOR]' , ooOoOoo0O , 9020 , OOooO0OOoo + 'UKiptvandvod.png' , ii11iIi1I , 'UK IPTV AND HD VOD' )
 ii11i1iIII ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ooOoOoo0O , 1023 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
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
 ii11i1iIII ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10001 , OOooO0OOoo + 'origin.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Football[/COLOR]' , '' , 10002 , OOooO0OOoo + 'origin.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10003 , OOooO0OOoo + 'origin.png' , ii11iIi1I , '' )
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
 ii11i1iIII ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , ooOoOoo0O , 9003 , OOooO0OOoo + 'livetv.png' , ii11iIi1I , '' )
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / OoOO0ooOOoo0O
def oo000OO00Oo ( ) :
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
 ii11i1iIII ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , iIii1 , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , iIii1 , ii11iIi1I , '' )
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
    ii11i1iIII ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 10006 , iIii1 , ii11iIi1I , '' )
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
   ii11i1iIII ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 10006 , iIii1 , ii11iIi1I , '' )
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
 ii11i1iIII ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , iIii1 , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , iIii1 , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , iIii1 , ii11iIi1I , '' )
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
def Iii1iiIi1II ( ) :
 ii11i1iIII ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , iIii1 , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , iIii1 , ii11iIi1I , '' )
 if 60 - 60: OOOo0 - OoOO * o0000oOoOoO0o % OoOoOO00
def ooo ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 III1iII1I1ii = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  ii11i1iIII ( '[COLORgreen]' + ( oOOo0 ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oo000o , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiIiIIIiiI , ii11iIi1I , '' )
  if 19 - 19: Ooo00oOo00o - Oo . OoOO / OoOO % o0oO0
def ooOii ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 OO0O0Ooo = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o0000oO )
 for OO0O0Ooo in OO0O0Ooo :
  oOoO0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( OO0O0Ooo ) )
  for Oo0 in oOoO0 :
   Oo0 = Oo0
  oo0O0o00o0O = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( OO0O0Ooo ) )
  for I11i1II , iiIiIIIiiI , time , OooiiIi1i in oo0O0o00o0O :
   I1i11111i1i11 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( OooiiIi1i )
   ii11i1iIII ( '[COLORgreen]' + Oo0 + ' - ' + I11i1II + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iiIiIIIiiI , ii11iIi1I , ( str ( I1i11111i1i11 ) ) )
   if 77 - 77: ii11ii1ii + Ooo00oOo00o / OoOO + O0 * OOooOOo
 III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if 28 - 28: o0oO0 + i11iIiiIii / o0000oOoOoO0o % I1IiI % Oo - O0
def ooo0OOO ( ) :
 if 49 - 49: i11iIiiIii % o00O0oo . I1IiI
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
 if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - OoOoOO00 * OoOO0ooOOoo0O
def iiIi1iI1iIii ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , url , oOOo0 in III1iII1I1ii :
  o00OooO0oo = oOOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  iii1 ( '[COLORgreen]' + o00OooO0oo + '[/COLOR]' , url , 10013 , iiIiIIIiiI )
  if 89 - 89: o00O0oo
def ooOoOO0OoO00o ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o0000oO )
 for IIIII1II in III1iII1I1ii :
  II1iiiiII = ( IIIII1II ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  II11iIIiiiII ( 'http:' + II1iiiiII )
  if 61 - 61: oO0o0ooO0 % OOOo0 - OOooOOo - OoOoOO00 % O0
  if 90 - 90: iIii1I11I1II1 + ii11ii1ii + o0oO0 - O0oO * IIII . ii11ii1ii
def I11iiiii1II ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 III1iII1I1ii = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 8046 , OOooO0OOoo + 'documentary.png' )
def ooOOooOo0O ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8046 , OOooO0OOoo + 'documentary.png' )
  if 40 - 40: OoOO0ooOOoo0O * OoOO0ooOOoo0O . oO0o0ooO0 % O0
def iIi11i1 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  yt . PlayVideo ( url )
  if 71 - 71: o0oO0
def Ooo0o00o0o ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 8041 , OOooO0OOoo + 'documentary.png' )
def IiIIIIIi ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 , iiIiIIIiiI in III1iII1I1ii :
  o0OoOO000ooO0 ( ( oOOo0 ) . replace ( '&#039;s' , '' ) , url , 8042 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8041 , OOooO0OOoo + 'documentary.png' )
  if 11 - 11: i1IIi % i11iIiiIii - i1IIi * I1IiI
  if 39 - 39: O0oO
def O0OoO0ooOO0o ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOo0 , iiIiIIIiiI , url , OoOo0oOooOoOO in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iiIiIIIiiI )
 for url in oOOOoo00 :
  oo00ooOoO00 ( ( url ) . replace ( '//' , 'http://' ) )
  if 96 - 96: OoOO0ooOOoo0O
def oo00ooOoO00 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  iii1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOooO0OOoo + 'documentary.png' )
  if 85 - 85: OOooOOo . I1IiI / o0oO0 . O0 % O0oO
def OO0ooo0oOO ( ) :
 o0000oO = OO ( 'http://www.stream2watch.co/live-tv' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , oOOo0 , oo000ii in III1iII1I1ii :
  o0OoOO000ooO0 ( ( oOOo0 + '[COLORgreen]' + oo000ii + '[/COLOR]' ) , oo000o , 8086 , iiIiIIIiiI )
  if 78 - 78: OoooooooOO . Ooo00oOo00o + o0oO0 - i1IIi
def ii1 ( url ) :
 o0000oO = OO ( url )
 III1iII1I1ii = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 8087 , iiIiIIIiiI )
  if 83 - 83: oO0o0ooO0 . O0 / Oo / OoOO0ooOOoo0O - OoOoOO00
def oO0oO0 ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o0000oO )
 for url , oOOo0 in III1iII1I1ii :
  i1i1IIIIi1i ( url , oOOo0 )
  if 7 - 7: iIii1I11I1II1 + oO0o0ooO0 * i11iIiiIii / OoooooooOO + oO0o0ooO0 - Oo
def i1i1IIIIi1i ( url , name ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o0000oO )
 for url in III1iII1I1ii :
  print url
  iii1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 3 - 3: i1IIi / OoOoOO00 / i11iIiiIii * i1IIi - OoOoOO00
def Ii ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 III1iII1I1ii = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , iII1111III1I , I11i1II , oo0O0o00o0O , oo000o in III1iII1I1ii :
  o0OoOO000ooO0 ( ( time + '[COLORgreen]' + oo0O0o00o0O + '[/COLOR]' + I11i1II ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , oo000o , 8061 , iiIiIIIiiI )
def ii11i ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  iii1 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , OOooO0OOoo + 'documentary.png' )
  if 100 - 100: o0oO0 % iIii1I11I1II1 * OoOoOO00 - oO0o0ooO0
def oo00O00oO000o ( ) :
 o0000oO = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 III1iII1I1ii = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oo000o , 8071 , OOooO0OOoo + 'streams.png' )
def OOo00OoO ( url ) :
 o0000oO = OO ( url )
 III1iII1I1ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000oO )
 for oOOo0 , url in III1iII1I1ii :
  iii1 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , OOooO0OOoo + 'streams.png' )
  if 10 - 10: OOooOOo / i11iIiiIii
def o00oO ( url ) :
 O00O0Ooooo00 = urllib2 . Request ( url )
 O00O0Ooooo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O000 = ''
 O0ii1ii1ii = ''
 try :
  O000 = urllib2 . urlopen ( O00O0Ooooo00 )
  O0ii1ii1ii = O000 . read ( )
  O000 . close ( )
 except : pass
 if O0ii1ii1ii != '' :
  return O0ii1ii1ii
 else :
  O0ii1ii1ii = 'Failed'
  return O0ii1ii1ii
  if 79 - 79: OoooooooOO - OOOo0
def o00O00oO00 ( ) :
 Ii1i1i1i1I1Ii = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 iiiI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 OOOoO0O = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0 = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 iiiI1I1iIIIi1 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 Iii = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1iiiiI1iI = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iiIi11iI1iii
 iIiiiii1i = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 if 40 - 40: O0 - OoooooooOO - IIII
 o0000oO = o00oO ( oo000o )
 iIiii = o00oO ( iiiI1 )
 OOO = o00oO ( OOOoO0O )
 O00OO0O0 = o00oO ( o0 )
 i1I111Ii1i11 = o00oO ( iiiI1I1iIIIi1 )
 o0O0O0o = o00oO ( I1iiiiI1iI )
 OOiI11I = oooooOoo0ooo ( iIiiiii1i )
 if 53 - 53: iIii1I11I1II1 + o00O0oo - O0oO
 if o0000oO != 'Failed' :
  III1iII1I1ii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0000oO )
  for OoO , oOOo0 in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oo000o + OoO ) , 222 , '' )
 if iIiii != 'Failed' :
  oOOOoo00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIiii )
  for OoO , oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiiI1 + OoO ) , 222 , '' )
 if OOO != 'Failed' :
  iIi1I11I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOO )
  for OoO , oOOo0 in iIi1I11I :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OOOoO0O + OoO ) , 222 , '' )
 if O00OO0O0 != 'Failed' :
  iIIiii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O00OO0O0 )
  for OoO , oOOo0 in iIIiii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0 + OoO ) , 222 , '' )
 if i1I111Ii1i11 != 'Failed' :
  O0i11i1iiI1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I111Ii1i11 )
  for OoO , iiIiIIIiiI , oOOo0 in O0i11i1iiI1i :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + '[COLORgreen] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OoO ) , 1006 , 'img' )
    if 87 - 87: o0oO0
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if o0O0O0o != 'Failed' :
  IIIii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0O0O0o )
  for OoO , iiIiIIIiiI , oOOo0 in IIIii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oo000o , 7067 , iiIiIIIiiI )
    if 83 - 83: IIII % OOooOOo % OOOo0 . iIii1I11I1II1 - IIII
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OOiI11I != 'Failed' :
  o00o = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( OOiI11I )
  for oo000o , iiIiIIIiiI , oOOo0 in o00o :
   iii1 ( oOOo0 + ' - Source 7' , oo000o , 222 , iiIiIIIiiI )
 Ii1IIiiIIi = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 88 - 88: OoooooooOO + o0000oOoOoO0o * OoOoOO00 % Oo
 if 17 - 17: IIII * OoOO0ooOOoo0O - Ooo00oOo00o / i11iIiiIii
 for O0Oo in Ii1IIiiIIi :
  oOOOOoO00OoOO = Ii1i1i1i1I1Ii + O0Oo
  oOooo0O0o = o00oO ( oOOOOoO00OoOO )
  if i1I111Ii1i11 != 'Failed' :
   Oo000 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( oOooo0O0o )
   for OoO , oOOo0 in Oo000 :
    if iiIi11iI1iii in oOOo0 . lower ( ) :
     iii1 ( ( oOOo0 + '[COLORgreen] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( Ii1i1i1i1I1Ii + O0Oo + OoO ) , 222 , '' )
     if 81 - 81: OoOO0ooOOoo0O - OoOO0ooOOoo0O % OoOoOO00 * Ooo00oOo00o
     III1ii1iII ( 'tvshows' , 'Media Info 3' )
     if 39 - 39: o0000oOoOoO0o
     if 58 - 58: i1IIi % OOooOOo
def OO000oooo0 ( ) :
 if 77 - 77: OOOo0 % O0
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 iiiI1 = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 OOOoO0O = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 o0 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iiiI1I1iIIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 Iii = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 iIiiiii1i = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 if 36 - 36: o00O0oo / OoOoOO00 / IIII / IIII + ii11ii1ii
 o0000oO = o00oO ( oo000o )
 iIiii = o00oO ( iiiI1 )
 OOO = o00oO ( OOOoO0O )
 O00OO0O0 = o00oO ( o0 )
 i1I111Ii1i11 = cloudflare . source ( iiiI1I1iIIIi1 )
 oOooo0O0o = o00oO ( Iii )
 OOiI11I = oooooOoo0ooo ( iIiiiii1i )
 if o0000oO != 'Failed' :
  III1iII1I1ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oOOo0 in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 95 - 95: IIII
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if iIiii != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiii )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiiI1 + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 51 - 51: OoOoOO00 + IIII . i1IIi . ii11ii1ii + I1IiI * OOOo0
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OOO != 'Failed' :
  iIi1I11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOO )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOOoO0O + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 72 - 72: OoOO + OoOO / OoOoOO00 . OoooooooOO % o00O0oo
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if O00OO0O0 != 'Failed' :
  iIIiii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O00OO0O0 )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0 + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 49 - 49: OoOO . Ooo00oOo00o - Oo * OoooooooOO . Oo
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if i1I111Ii1i11 != 'Failed' :
  O0i11i1iiI1i = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( i1I111Ii1i11 )
  for oo000o , iiIiIIIiiI , oOOo0 in O0i11i1iiI1i :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( oOOo0 + ' - Source - Dizi' , oo000o , 8062 , iiIiIIIiiI )
    if 2 - 2: OoooooooOO % OoOO0ooOOoo0O
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if oOooo0O0o != 'Failed' :
  Oo000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOooo0O0o )
  for oo000o , iiIiIIIiiI , oOOo0 in Oo000 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source Scooby[/COLOR]' ) , oo000o , 222 , 'img' )
    if 63 - 63: OOOo0 % iIii1I11I1II1
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OOiI11I != 'Failed' :
  o00o = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( OOiI11I )
  for oo000o , iiIiIIIiiI , oOOo0 in o00o :
   iii1 ( oOOo0 + ' - Source 7' , oo000o , 222 , iiIiIIIiiI )
def I1ii ( ) :
 if 73 - 73: IIII + OOOo0 * Oo * OoooooooOO
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0000oO = oooooOoo0ooo ( oo000o )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o0000oO )
 for oOOo0 , iiIiIIIiiI , Oo0o0O in III1iII1I1ii :
  ii1iIi1II = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if iiIi11iI1iii in oOOo0 . lower ( ) :
   o0OoOO000ooO0 ( oOOo0 , '' , 7022 , ii1iIi1II )
   if 2 - 2: Oo + I1IiI - OoOO0ooOOoo0O . OOOo0 - OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: iIii1I11I1II1 - oO0o0ooO0
 if 11 - 11: iIii1I11I1II1 . OoooooooOO . OoOoOO00 / i1IIi - o0000oOoOoO0o
def ii1ii11 ( url ) :
 OoOoo0oO = cloudflare . source ( url )
 III1iII1I1ii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OoOoo0oO )
 for url , iioo0o0OoOOO , ooO0oO00O0o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( iioo0o0OoOOO ) . replace ( 'Sezon' , ' Season ' ) + ( ooO0oO00O0o ) . replace ( 'Bölüm' , ' Episode ' ) + oOOo0 , url , 8063 , '' )
  if 70 - 70: O0oO
  if 16 - 16: oO0o0ooO0 - OoooooooOO % Oo
  if 36 - 36: OoOO0ooOOoo0O
  if 84 - 84: O0oO . Ooo00oOo00o . OoOoOO00 . o0000oOoOoO0o / o00O0oo % ii11ii1ii
def OOO0oOoO0O ( url ) :
 OoOoo0oO = cloudflare . source ( url )
 III1iII1I1ii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OoOoo0oO )
 for url , oOOo0 in III1iII1I1ii :
  iii1 ( oOOo0 , url , 222 , '' )
  if 84 - 84: O0 * OoooooooOO - IIII * IIII
  if 8 - 8: o0oO0 / i1IIi . OoOO
  if 41 - 41: oO0o0ooO0 + Ooo00oOo00o
  if 86 - 86: I1IiI . iIii1I11I1II1 - Ooo00oOo00o
def oOO ( ) :
 if 31 - 31: OoOO0ooOOoo0O / Oo * i1IIi . I1IiI
 OoOoo0oO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 III1iII1I1ii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoOoo0oO )
 for oo000o , iiIiIIIiiI , oOOo0 , ooO0oO00O0o in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 + '  -  ' + ( ooO0oO00O0o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oo000o , 8063 , iiIiIIIiiI )
  if 57 - 57: OoOO0ooOOoo0O + iIii1I11I1II1 % i1IIi % OOOo0
def OO0oo ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 , iiIiIIIiiI in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 8002 , iiIiIIIiiI )
def IiIi1II11i ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , url , oOOo0 , OoOo0oOooOoOO in III1iII1I1ii :
  ii11i1iIII ( '%s %s' % ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , time ) , url , 1015 , iiIiIIIiiI , OoOo0oOooOoOO )
  if 42 - 42: ii11ii1ii * I1IiI % o0oO0 - I1IiI . i11iIiiIii - O0oO
def o0oO0oOO ( ) :
 if 89 - 89: o0oO0 + o00O0oo * o0oO0 / o0oO0
 o0OoOO000ooO0 ( 'Coronation Street' , '' , 8001 , '' )
 o0OoOO000ooO0 ( 'Eastenders' , '' , 8002 , '' )
 o0OoOO000ooO0 ( 'Emmerdale' , '' , 8003 , '' )
 o0OoOO000ooO0 ( 'Hollyoaks' , '' , 8004 , '' )
 o0OoOO000ooO0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 46 - 46: Ooo00oOo00o
 if 71 - 71: o0000oOoOoO0o / o0000oOoOoO0o * OoOO * OoOO / OoOoOO00
 if 35 - 35: OoOO0ooOOoo0O * OOooOOo * OOOo0 % Oo . I1IiI
 if 58 - 58: o0000oOoOoO0o + OoOoOO00 * oO0o0ooO0 * i11iIiiIii - iIii1I11I1II1
def oooo00o0o0o ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Holly' in oOOo0 :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 87 - 87: o0000oOoOoO0o * i1IIi - o00O0oo % OoOO0ooOOoo0O / O0oO
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 39 - 39: OOOo0 * i11iIiiIii - OoOO / IIII % O0oO % o0000oOoOoO0o
def OO00oo0o ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'East' in oOOo0 :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 18 - 18: Ooo00oOo00o + iIii1I11I1II1 - OoOoOO00 - OOOo0
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: OoooooooOO
def iIIIII1iiiiII ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Emmer' in oOOo0 :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 54 - 54: i1IIi
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: i1IIi + o00O0oo
def O0o0O0OO00o ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Coro' in oOOo0 :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 92 - 92: OOooOOo + O0oO / Oo % Ooo00oOo00o % IIII . OoooooooOO
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: o0oO0 / i11iIiiIii - OoOO0ooOOoo0O . IIII % iIii1I11I1II1 + OOooOOo
def OO00oOooo0O ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Celeb' in oOOo0 :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 58 - 58: Oo / OoOO
def iIII1I1i1i ( name , url ) :
 o0O = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if o0O :
  IIiI1I1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  Iiii1i1 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( Iiii1i1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  Iiii1i1 = open_url ( url )
  I11I1IIiiII1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( Iiii1i1 ) [ - 1 ]
  IIiI1I1 = I11I1IIiiII1 . replace ( '\\/' , '/' )
 IIIIIii1ii11 = xbmcgui . ListItem ( name , '' , '' )
 IIIIIii1ii11 . setPath ( IIiI1I1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIIIIii1ii11 )
 if 86 - 86: I1IiI * OoOoOO00 - O0 . I1IiI % iIii1I11I1II1 / OoOO0ooOOoo0O
 if 11 - 11: OOOo0 * OoOO + ii11ii1ii / ii11ii1ii
def iiii1I1 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 III1iII1I1ii = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oo000o , 7071 , OOooO0OOoo + 'popcorn.png' )
 for oo000o , oOOo0 in oOOOoo00 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oo000o , 7071 , OOooO0OOoo + 'popcorn.png' )
  if 14 - 14: I1IiI * OOOo0 + OoooooooOO - oO0o0ooO0 - IIII
def I1iii ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 III1iII1I1ii = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Movies' in oOOo0 :
   o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( oo000o ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , OOooO0OOoo + 'popcorn.png' )
def oOO0OO0O ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOooO0OOoo + 'popcorn.png' )
  if 78 - 78: o00O0oo / OoOoOO00 % I1IiI
  if 52 - 52: OoOO0ooOOoo0O - oO0o0ooO0 * OoOO
def Ii1I11I ( url ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 III1iII1I1ii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iiIiIIIiiI )
  if 36 - 36: O0 + Oo
  if 5 - 5: Oo * I1IiI
def ii1I11iIiIII1 ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiIiIIIiiI )
  if 52 - 52: OOooOOo * IIII + I1IiI
def IiiiIiiI ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  o00O ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 48 - 48: oO0o0ooO0 . i11iIiiIii
def o00O ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 222 , OOooO0OOoo + 'popcorn' )
  if 5 - 5: OoOO . ii11ii1ii . OoOoOO00 . OoooooooOO
  if 96 - 96: i11iIiiIii - OoOO0ooOOoo0O % O0 / Ooo00oOo00o
  if 100 - 100: oO0o0ooO0 / o00O0oo - OoooooooOO % OoOoOO00 - OOOo0 % I1IiI
  if 60 - 60: iIii1I11I1II1 + i1IIi
def OooOOo0 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 III1iII1I1ii = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 , iiIiIIIiiI in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( oo000o ) ) , 222 , iiIiIIIiiI )
  if 51 - 51: I1IiI
def I11IIIiIi11 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 III1iII1I1ii = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + oo000o , 7051 , OOooO0OOoo + 'vod.png' )
  if 39 - 39: o00O0oo % O0 % I1IiI . i1IIi
def oOo00OooO0oO ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , OOooO0OOoo + 'vod.png' )
  if 16 - 16: IIII / Oo + OoOO0ooOOoo0O / o00O0oo
def IIIiiI1 ( url ) :
 Iiii1i1 = oooooOoo0ooo
 III1iII1I1ii = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 222 , iiIiIIIiiI )
  if 74 - 74: o0000oOoOoO0o - OoOO0ooOOoo0O + i1IIi . OOOo0 + OoOO0ooOOoo0O - o0000oOoOoO0o
  if 17 - 17: O0 . O0oO . O0 + O0 / Oo . o0oO0
  if 62 - 62: ii11ii1ii % oO0o0ooO0 * Ooo00oOo00o - i1IIi
  if 66 - 66: i11iIiiIii / OOooOOo - OoooooooOO / i1IIi . i11iIiiIii
  if 16 - 16: Oo % ii11ii1ii + o0000oOoOoO0o - O0 . oO0o0ooO0 / O0oO
def IIi1I ( ) :
 if 27 - 27: O0 . O0oO / oO0o0ooO0
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
 if 96 - 96: ii11ii1ii % o0oO0 % o00O0oo - o0oO0 % I1IiI + ii11ii1ii
 if 3 - 3: O0
def Ooo0Oo0oo0 ( Cat_Name ) :
 if 83 - 83: O0oO
 ii111Ii11iii = False
 o00OOoOOO000O0 = '0'
 if Cat_Name == 'All Channels' : ii111Ii11iii = True
 if Cat_Name == 'Entertainment' : o00OOoOOO000O0 = '1'
 if Cat_Name == 'Movies' : o00OOoOOO000O0 = '2'
 if Cat_Name == 'Music' : o00OOoOOO000O0 = '3'
 if Cat_Name == 'News' : o00OOoOOO000O0 = '4'
 if Cat_Name == 'Sports' : o00OOoOOO000O0 = '5'
 if Cat_Name == 'Documentary' : o00OOoOOO000O0 = '6'
 if Cat_Name == 'Kids' : o00OOoOOO000O0 = '7'
 if Cat_Name == 'Food' : o00OOoOOO000O0 = '8'
 if Cat_Name == 'Religious' : o00OOoOOO000O0 = '9'
 if Cat_Name == 'USA Channels' : o00OOoOOO000O0 = '10'
 if Cat_Name == 'Other' : o00OOoOOO000O0 = '11'
 if 92 - 92: ii11ii1ii / O0
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( Iiii1i1 )
 print 'Len Match: >>>' + str ( len ( III1iII1I1ii ) )
 for oOOo0 , iiIiIIIiiI , Oo0o0O in III1iII1I1ii :
  ii1iIi1II = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if Oo0o0O == o00OOoOOO000O0 :
   o0OoOO000ooO0 ( oOOo0 , '' , 7022 , ii1iIi1II )
  elif ii111Ii11iii == True :
   o0OoOO000ooO0 ( oOOo0 , '' , 7022 , ii1iIi1II )
  else : pass
  if 80 - 80: OOooOOo - OoOO0ooOOoo0O + OoooooooOO
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 98 - 98: OoOO0ooOOoo0O + i1IIi . OOOo0 - OoOoOO00 - OOooOOo
def iIIi1I1ii ( Search_Name ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , oo000o , iiiI1 , OOOoO0O in III1iII1I1ii :
  ii1iIi1II = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  iii1 ( Search_Name + ': Link 1' , ( oo000o ) . replace ( '\\' , '' ) , 222 , ii1iIi1II )
  iii1 ( Search_Name + ': Link 2' , ( iiiI1 ) . replace ( '\\' , '' ) , 222 , ii1iIi1II )
  iii1 ( Search_Name + ': Link 3' , ( OOOoO0O ) . replace ( '\\' , '' ) , 222 , ii1iIi1II )
  if 14 - 14: O0 / i1IIi / Oo + iIii1I11I1II1
def ooO00O00oOO ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 III1iII1I1ii = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  iii1 ( oOOo0 , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOooO0OOoo + 'english.png' )
def I1 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 III1iII1I1ii = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  iii1 ( oOOo0 , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'xxx.png' )
def IIII1ii ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 III1iII1I1ii = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  iii1 ( oOOo0 , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'vod(1).png' )
  if 13 - 13: OoooooooOO * OoOO - o00O0oo / OoOO0ooOOoo0O + o0000oOoOoO0o + IIII
def iii1III1i ( url ) :
 url
 iiiIi = xbmcgui . ListItem ( oOOo0 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiIi )
 return
 if 45 - 45: ii11ii1ii + Ooo00oOo00o * i11iIiiIii / OoOO0ooOOoo0O % o0000oOoOoO0o * O0
 if 17 - 17: O0
def OOooO0o ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , url , 9031 , OOooO0OOoo + 'icon.png' )
def ii1iI1iI1 ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , url , 9032 , OOooO0OOoo + 'icon.png' )
def o00oOOO ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , url in III1iII1I1ii :
  if '://' in oOOo0 :
   pass
   iii1 ( ( oOOo0 ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOooO0OOoo + 'icon.png' )
def OoOO0OOoo ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( Iiii1i1 )
 for oOOo0 , url in III1iII1I1ii :
  iii1 ( oOOo0 , url , 222 , OOooO0OOoo + 'icon.png' )
  if 1 - 1: OOOo0 * i11iIiiIii + O0oO * i11iIiiIii + Ooo00oOo00o
  if 30 - 30: Oo . Ooo00oOo00o
  if 57 - 57: o0000oOoOoO0o . Oo + OoOoOO00
def i111i11I1ii ( ) :
 Iiii1i1 = oooooOoo0ooo ( 'http://tvshows.cnfstudio.com/' )
 III1iII1I1ii = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , 'http://tvshows.cnfstudio.com/genre/' + oo000o , 7010 , OOooO0OOoo + 'icon.png' )
  print '>>>>>>>>>>' + oo000o
  if 64 - 64: OoOO / i11iIiiIii / OOooOOo . OoooooooOO
def i1iiIIi11I ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 o0o0oOo000o0 = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( oOOo0 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , iiIiIIIiiI )
 o0o0oOo000o0 = o0o0oOo000o0
 for url in o0o0oOo000o0 :
  o0OoOO000ooO0 ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  o0OoOO000ooO0 ( 'Next' , url , 7010 , '' )
  if 25 - 25: o0000oOoOoO0o + I1IiI . OOooOOo % I1IiI * OoOO0ooOOoo0O
def ii1IiIi11 ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , ooO0oO00O0o , oOOo0 in III1iII1I1ii :
  iii1 ( ( 'Season' ) + ooO0oO00O0o + ( '  ' ) + oOOo0 , url , 7004 , OOooO0OOoo + 'icon.png' )
  if 22 - 22: OoOO
def ii1ii ( url ) :
 if 79 - 79: Oo - OoooooooOO . O0
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOooO0OOoo + 'icon.png' )
  if 62 - 62: OoOO * OoOO . o00O0oo % i1IIi . o00O0oo * o00O0oo
def o0Oo ( name , url , img ) :
 o0000oO = oooooOoo0ooo ( url )
 oo0ooO0 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o0000oO )
 IIiiiiIiIIii = len ( oo0ooO0 )
 if 86 - 86: o0000oOoOoO0o / OOooOOo - OOooOOo + ii11ii1ii + OoOO
 if 33 - 33: OOooOOo . oO0o0ooO0 . IIII . i1IIi
 if IIiiiiIiIIii == 1 :
  for i1II1iII in oo0ooO0 :
   i1II1iII = i1II1iII . replace ( 'player' , 'watch' )
   II1i = i1II1iII + '&fv=&sou='
   o0OO00oo = oooooOoo0ooo ( II1i )
   i1i1IiIiIi1Ii = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o0OO00oo )
   for oO0ooOO in i1i1IiIiIi1Ii :
    IIi1iI1 = False
    Resolve ( oO0ooOO )
    if 44 - 44: ii11ii1ii - o00O0oo / OoOoOO00 * Ooo00oOo00o * Oo
 elif IIiiiiIiIIii > 1 :
  if 73 - 73: OOooOOo - OOOo0 * i1IIi / i11iIiiIii * OoOO0ooOOoo0O % OoOoOO00
  for i1II1iII in oo0ooO0 :
   OooOoOOo0oO00 = oooooOoo0ooo ( i1II1iII )
   O00O = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OooOoOOo0oO00 )
   O0Ooo = O00O
   O0Ooo = ( str ( O0Ooo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + O0Ooo
   iii1 ( 'DOUBLE LINK' , O0Ooo , 424 , '' )
   if 78 - 78: Ooo00oOo00o % IIII * i1IIi
   for url in O00O :
    o0OoOO000ooO0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iiiI1 = Google . resolve ( url )
    except :
     pass
    try :
     O0iI = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iiiI1 ) )
     for Ii1I , IiiIiiIi in O0iI :
      if 40 - 40: OOooOOo
      HD_URLS . append ( Ii1I )
      SD_URLS . append ( IiiIiiIi )
    except :
     pass
 else :
  pass
  if 78 - 78: iIii1I11I1II1
def ooO0oo0o0 ( ) :
 if 9 - 9: OOOo0 + ii11ii1ii / OOOo0 . OoOO * o0oO0
 if 45 - 45: i11iIiiIii
 o0OoOO000ooO0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOooO0OOoo + 'Movies.png' )
 if 82 - 82: o00O0oo + IIII
 o0OoOO000ooO0 ( 'Search Movies' , '' , 7017 , OOooO0OOoo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 12 - 12: O0oO
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / OOooOOo / OoOoOO00
def I1i ( ) :
 Iiii1i1 = oooooOoo0ooo ( 'http://cnfstudio.com/' )
 III1iII1I1ii = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , 'http://cnfstudio.com/genre/' + oo000o , 7003 , OOooO0OOoo + 'icon.png' )
  if 59 - 59: OoooooooOO . o00O0oo / O0 - OoOO0ooOOoo0O
i1iiIII111ii = xbmcgui . Dialog ( )
if 1 - 1: IIII / IIII - i11iIiiIii
if 87 - 87: Oo / O0 * IIII / OOooOOo
def I1iiIII ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 o0o0oOo000o0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oOOo0 in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iiIiIIIiiI )
 o0o0oOo000o0 = o0o0oOo000o0
 for url in o0o0oOo000o0 :
  o0OoOO000ooO0 ( 'Next Page' , url , 7003 , '' )
  if 16 - 16: OoOO + o0oO0 / OOooOOo
def O00oOoo0OoO0 ( url ) :
 if 62 - 62: i1IIi / o0oO0 . OOOo0 * OOooOOo
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  O0ii1ii1ii = url + '&fv=&sou='
  O0ii1ii1ii = O0ii1ii1ii . replace ( 'player' , 'watch' )
  i11i1Ii1 = o0oO0oo0000OO ( O0ii1ii1ii )
  I1i1ii1IiIii = o0oO0oo0000OO ( url )
  if 69 - 69: I1IiI % OoOO - o0000oOoOoO0o
  if 38 - 38: iIii1I11I1II1 + i11iIiiIii / i11iIiiIii % Ooo00oOo00o / o0oO0 % o00O0oo
def o0oO0oo0000OO ( url ) :
 if 7 - 7: IIII * OOOo0 + i1IIi + i11iIiiIii + Oo % OOOo0
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  OO00OO0o0 ( url )
  if 52 - 52: ii11ii1ii % OoOO - i11iIiiIii
  if 30 - 30: oO0o0ooO0 / Ooo00oOo00o + OoOO
def I1I ( ) :
 ii11i1iIII ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 73 - 73: o00O0oo
def OOOIiIi1111ii ( url ) :
 III1iII1I1ii = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for iI1I1II1 , oOOo0 , url in III1iII1I1ii :
  iii1 ( oOOo0 , url , 222 , OOooO0OOoo + 'streams.png' )
  if 92 - 92: OoooooooOO - OoooooooOO * Ooo00oOo00o % OOOo0
  if 77 - 77: iIii1I11I1II1 - i1IIi . OoOO
def iIi1iIIIiIiI ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 1007 , iiIi1IIi1I )
def OooOo000o0o ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 42 - 42: OoOO % OoOO0ooOOoo0O
  if 60 - 60: I1IiI / O0oO - OoOoOO00 . Oo + O0
def Ii1iI ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  if '.php' in url :
   o0OoOO000ooO0 ( oOOo0 , url , 1016 , iiIi1IIi1I )
  else :
   iii1 ( oOOo0 , url , 222 , iiIi1IIi1I )
   if 53 - 53: iIii1I11I1II1 - OoOO % I1IiI * O0oO % o0oO0
def II1Ii ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 1007 , iiIi1IIi1I )
def OOoO00ooO ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 12 - 12: o0oO0 % OOOo0 + OoOO - i1IIi . o00O0oo / OOOo0
def o0IiiiI111I ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 III1I11i1iIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 III1I11i1iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , III1I11i1iIi )
 if 69 - 69: Oo * OoOoOO00 * o0oO0 . oO0o0ooO0 - ii11ii1ii
 if 39 - 39: o00O0oo * OOOo0 % Ooo00oOo00o . I1IiI
def iiii111IiIIi1 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 1006 , iiIiIIIiiI )
def Oo0000o0O0O ( url ) :
 Iiii1i1 = OO ( url )
 IIiIiIIiIi = url
 III1iII1I1ii = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  if '.mp3' in oOOo0 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iii1 ( ( oOOo0 ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOooO0OOoo + 'music.png' )
  else :
   o0OoOO000ooO0 ( ( oOOo0 ) . replace ( '/' , '' ) , IIiIiIIiIi + url , 1011 , OOooO0OOoo + 'music.png' )
def oooO ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 III1iII1I1ii = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , ( 'http://www.cyn.net/music/' + oo000o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iiIiIIIiiI ) . replace ( ' ' , '%20' ) )
def iiIIi ( url , img ) :
 Iiii1i1 = OO ( url )
 iiiI1 = url
 img = img
 III1iII1I1ii = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '.mp3' , '' ) , ( iiiI1 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 36 - 36: o0000oOoOoO0o . OoOoOO00
  if 25 - 25: OoOO
def iI1iiII11I ( ) :
 Ii1i1i1i1I1Ii = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iiiI1 = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OOOoO0O = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 32 - 32: OoOO0ooOOoo0O % o0oO0 - I1IiI % oO0o0ooO0 . O0oO
 o0000oO = o00oO ( oo000o )
 iIiii = o00oO ( iiiI1 )
 OOO = o00oO ( OOOoO0O )
 if 47 - 47: o0000oOoOoO0o % i1IIi + i1IIi
 if o0000oO != 'Failed' :
  III1iII1I1ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oOOo0 in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 87 - 87: Oo * OoOO0ooOOoo0O % IIII % I1IiI
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if iIiii != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiiI1 + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 4 - 4: I1IiI + o00O0oo / OoOO
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OOO != 'Failed' :
  iIi1I11I = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOO )
  for oOOo0 in iIi1I11I :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOOoO0O + oOOo0 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 13 - 13: oO0o0ooO0
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
    if 80 - 80: o00O0oo - OOooOOo
    if 41 - 41: OOooOOo - Oo * OOOo0
    if 82 - 82: Ooo00oOo00o % OOooOOo % OoOO0ooOOoo0O / O0
    if 94 - 94: ii11ii1ii + ii11ii1ii + OoooooooOO % o0oO0
    if 7 - 7: oO0o0ooO0
    if 78 - 78: OoOO0ooOOoo0O + oO0o0ooO0 . IIII
def OoIIi1iI ( ) :
 Iiii1i1 = oooooOoo0ooo ( 'http://www.animetoon.org/cartoon' )
 III1iII1I1ii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 1002 , OOooO0OOoo + 'anime.png' )
  if 92 - 92: Ooo00oOo00o * o0oO0
  if 35 - 35: i11iIiiIii
  if 99 - 99: OoOoOO00 . OOooOOo + O0
def O00o0O ( url ) :
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
def iIIIiI ( url , IMAGE ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Iiii1i1 )
 for oOOo0 , url in III1iII1I1ii :
  print oOOo0 + '     ' + url
  if 'easy' in url :
   O00 ( url )
  elif 'playpanda' in url :
   O00 ( url )
   if 14 - 14: i11iIiiIii
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00 ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( "url: '(.+?)'," ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  iii1 ( 'STREAM' , url , 222 , OOooO0OOoo + 'anime.png' )
  if 73 - 73: o0oO0 + OoOO . Ooo00oOo00o
  if 46 - 46: Ooo00oOo00o - OOooOOo / I1IiI - OoooooooOO + OoOO
def OOOO ( url ) :
 O00O0Ooooo00 = urllib2 . Request ( url )
 O00O0Ooooo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0Ooooo00 . add_header ( 'referer' , url )
 O000 = urllib2 . urlopen ( O00O0Ooooo00 )
 O0ii1ii1ii = O000 . read ( )
 O000 . close ( )
 return O0ii1ii1ii
 if 37 - 37: o0000oOoOoO0o - I1IiI . iIii1I11I1II1 % o0oO0 % o00O0oo * I1IiI
def OO ( url ) :
 O00O0Ooooo00 = urllib2 . Request ( url )
 O00O0Ooooo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O000 = urllib2 . urlopen ( O00O0Ooooo00 )
 O0ii1ii1ii = O000 . read ( )
 O000 . close ( )
 return O0ii1ii1ii
 if 8 - 8: I1IiI . o0oO0 % OoOO . OOOo0 % OOOo0 . o00O0oo
def I1I11ii ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoOoo00Oo = ( '%s%s' % ( Iiii1iiiIiI1 , url ) )
 O0ii1ii1ii = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0ii1ii1ii )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  iii1 ( '%s' % ( oOOo0 ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiIi1IIi1I )
  if 27 - 27: o00O0oo + OOOo0 * iIii1I11I1II1 . OoooooooOO * I1IiI
def OO00OO0o0 ( url ) :
 OOOo = xbmc . Player ( o0ooOo00O ( ) )
 import urlresolver
 try : OOOo . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( oOOo0 ) )
 OOOo = xbmc . Player ( o0ooOo00O ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIII111ii = xbmcgui . Dialog ( )
  if i1iiIII111ii . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIII111ii . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : OOOo . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 38 - 38: iIii1I11I1II1 + i11iIiiIii * Ooo00oOo00o * o0oO0 % OoOO0ooOOoo0O
def II11iIIiiiII ( url ) :
 OOOo = xbmc . Player ( o0ooOo00O ( ) )
 import urlresolver
 try : OOOo . play ( url )
 except : pass
 if 5 - 5: o0oO0 - O0oO + OOOo0 * O0 / Oo - o00O0oo
 if 75 - 75: OoooooooOO - OoOO0ooOOoo0O + OOooOOo / oO0o0ooO0 % i11iIiiIii
def o0ooOo00O ( ) :
 try :
  iiiiii1 = getSet ( "core-player" )
  if ( iiiiii1 == 'DVDPLAYER' ) : OO0o0oO0O000o = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iiiiii1 == 'MPLAYER' ) : OO0o0oO0O000o = xbmc . PLAYER_CORE_MPLAYER
  elif ( iiiiii1 == 'PAPLAYER' ) : OO0o0oO0O000o = xbmc . PLAYER_CORE_PAPLAYER
  else : OO0o0oO0O000o = xbmc . PLAYER_CORE_AUTO
 except : OO0o0oO0O000o = xbmc . PLAYER_CORE_AUTO
 return OO0o0oO0O000o
 return True
 if 47 - 47: O0oO - Ooo00oOo00o / o00O0oo * OoooooooOO / o00O0oo . Oo
def o0OoOO000ooO0 ( name , url , mode , iconimage ) :
 iiII1IiIi1iI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOiiI1Ii11II1I = True
 IIIIIii1ii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIIii1ii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOiiI1Ii11II1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiII1IiIi1iI1 , listitem = IIIIIii1ii11 , isFolder = True )
 return oOiiI1Ii11II1I
 if 44 - 44: o00O0oo % i11iIiiIii - oO0o0ooO0 * ii11ii1ii + Oo * OoOO0ooOOoo0O
def iii1 ( name , url , mode , iconimage ) :
 iiII1IiIi1iI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOiiI1Ii11II1I = True
 IIIIIii1ii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIIii1ii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOiiI1Ii11II1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiII1IiIi1iI1 , listitem = IIIIIii1ii11 , isFolder = False )
 return oOiiI1Ii11II1I
 if 41 - 41: O0 * o0oO0 - I1IiI . o00O0oo
 if 65 - 65: Oo . OoooooooOO
 if 70 - 70: Oo - OoOO . iIii1I11I1II1 % o0000oOoOoO0o / I1IiI - O0
 if 55 - 55: oO0o0ooO0 - Ooo00oOo00o
 if 100 - 100: O0
 if 79 - 79: iIii1I11I1II1
 if 81 - 81: OoOO0ooOOoo0O + iIii1I11I1II1 * O0oO - iIii1I11I1II1 . OoOO0ooOOoo0O
def I1iioO0o ( heading , announce ) :
 class I1I1 ( ) :
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
   try : I1II1 = open ( announce ) ; O0Oo0 = I1II1 . read ( )
   except : O0Oo0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0Oo0 ) )
   return
 I1I1 ( )
 if 80 - 80: OOOo0 - iIii1I11I1II1 . OoOO0ooOOoo0O + Ooo00oOo00o - O0oO
def iI1iIiiiI1I1 ( ) :
 I1iioO0o ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 78 - 78: OoOO / Ooo00oOo00o - OoOO * OoooooooOO . I1IiI
 if 96 - 96: OOOo0 % i1IIi . OOooOOo . O0
 if 37 - 37: i1IIi - OoOO0ooOOoo0O % OoooooooOO / OoOO0ooOOoo0O % o0oO0
 if 48 - 48: i11iIiiIii % OoOO
 if 29 - 29: oO0o0ooO0 + i11iIiiIii % o0000oOoOoO0o
def o00oOOooOOo0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 93 - 93: I1IiI % iIii1I11I1II1
 if 90 - 90: OOOo0 - OoOO0ooOOoo0O / o00O0oo / O0 / o0000oOoOoO0o
 if 87 - 87: I1IiI / IIII + iIii1I11I1II1
 if 93 - 93: iIii1I11I1II1 + OoOO % o0oO0
 if 21 - 21: OoOO0ooOOoo0O
 if 6 - 6: IIII
 if 46 - 46: IIII + OoOO
 if 79 - 79: OoooooooOO - IIII * IIII . I1IiI
 if 100 - 100: OoOoOO00 * o0000oOoOoO0o % OOOo0 / ii11ii1ii
 if 90 - 90: ii11ii1ii . o0oO0 . I1IiI . o00O0oo
 if 4 - 4: o00O0oo + I1IiI % ii11ii1ii / i11iIiiIii
 if 74 - 74: OoOoOO00 . O0 - OOOo0 + IIII % i11iIiiIii % I1IiI
 if 78 - 78: o00O0oo + I1IiI + IIII - IIII . i11iIiiIii / Ooo00oOo00o
 if 27 - 27: o00O0oo - O0 % o0000oOoOoO0o * O0oO . IIII % iIii1I11I1II1
 if 37 - 37: OoooooooOO + O0 - i1IIi % o0oO0
 if 24 - 24: I1IiI
 if 94 - 94: i1IIi * i1IIi % OoOoOO00 + OoOO0ooOOoo0O
 if 28 - 28: OOOo0
 if 49 - 49: o0000oOoOoO0o . OOooOOo % OoOO / o00O0oo
 if 95 - 95: O0 * I1IiI * IIII . o0oO0 / iIii1I11I1II1
 if 28 - 28: IIII + OoOO - o0oO0 / iIii1I11I1II1 - OOOo0
 if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
 if 35 - 35: ii11ii1ii / oO0o0ooO0 % OOOo0 + iIii1I11I1II1
 if 79 - 79: I1IiI / o0oO0
def oOo00o ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + OOoooooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 4 - 4: Oo + OOooOOo
def iIIiIii11i1Ii ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + OoO0O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 14 - 14: Ooo00oOo00o / Ooo00oOo00o * O0 . OoOO
def oooOO0oOooO00 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + iIIiI11i1I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 29 - 29: Ooo00oOo00o * iIii1I11I1II1 * O0 - I1IiI / IIII
def o0oO0OO00ooOO ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + IiIIiii11II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 42 - 42: i1IIi % OoOoOO00 . o0oO0
def II1II1iI ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + OooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 92 - 92: OOooOOo / OOooOOo * o00O0oo
def iI111i11iI1 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + III1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 23 - 23: OoOO * oO0o0ooO0
def O0oOo00O ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + i1I1I1i1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 23 - 23: iIii1I11I1II1
def Ii11ii1Iiii ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + I11i1iIi111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 35 - 35: OOooOOo
def ooOoooo0 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + OoOoO0oOOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 99 - 99: iIii1I11I1II1
def IIiiiiIi1I ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + ooo0O0o0OoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 5 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 9 - 9: Ooo00oOo00o
 if 60 - 60: O0oO
 if 98 - 98: o0oO0
 if 34 - 34: iIii1I11I1II1 * o0000oOoOoO0o * o0000oOoOoO0o / ii11ii1ii
 if 28 - 28: Ooo00oOo00o - OoOO + I1IiI + o00O0oo / iIii1I11I1II1
 if 26 - 26: iIii1I11I1II1 - O0 . O0
 if 68 - 68: OoOO0ooOOoo0O + OoOO . O0 . o00O0oo % i1IIi % OoOO0ooOOoo0O
 if 50 - 50: IIII + OOooOOo
 if 96 - 96: Ooo00oOo00o
def oOOoO ( ) :
 try :
  if os . path . exists ( iiI1IiI ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iiI1IiI ) :
     oOo0Oo0O0O = 0
     oOo0Oo0O0O += len ( oOo0OOoO0 )
     if oOo0Oo0O0O > 0 :
      for I1II1 in oOo0OOoO0 :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
  III1II1i = os . path . join ( O0OoO000O0OO , "Textures13.db" )
  os . unlink ( III1II1i )
  i1iiIII111ii . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 3 - 3: oO0o0ooO0
 if 35 - 35: IIII . O0 + Oo + OoOO0ooOOoo0O + i1IIi
 if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
 if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
 if 58 - 58: OoOO0ooOOoo0O . OOooOOo + OOOo0 % Oo - Ooo00oOo00o
 if 50 - 50: oO0o0ooO0 % OoOoOO00 - o0oO0 . i1IIi + O0 % oO0o0ooO0
 if 10 - 10: oO0o0ooO0 . i1IIi + o00O0oo
 if 66 - 66: Ooo00oOo00o % OOooOOo
 if 21 - 21: I1IiI - OoooooooOO % i11iIiiIii
def Oo00O0OO ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 oOOOoo0o = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( oOOOoo0o ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( oOOOoo0o ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 44 - 44: O0 % i1IIi
   if 42 - 42: OoOoOO00 - Ooo00oOo00o - OoooooooOO . oO0o0ooO0 / I1IiI
   if oOo0Oo0O0O > 0 :
    if 56 - 56: i11iIiiIii - iIii1I11I1II1 . OoOoOO00
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete KODI Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 81 - 81: IIII / I1IiI * IIII . O0
     for I1II1 in oOo0OOoO0 :
      try :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
      except :
       pass
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      try :
       shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      except :
       pass
       if 83 - 83: OoOoOO00 * i1IIi * oO0o0ooO0 . ii11ii1ii / o0000oOoOoO0o + i1IIi
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  i1Ii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 59 - 59: O0oO + Ooo00oOo00o / OoOO0ooOOoo0O
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( i1Ii ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 97 - 97: Oo * oO0o0ooO0 % o0oO0 . oO0o0ooO0 - O0oO - OoOO0ooOOoo0O
   if oOo0Oo0O0O > 0 :
    if 79 - 79: OOOo0 - o0oO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( oOo0Oo0O0O ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 37 - 37: IIII . Oo * Oo * OoOoOO00 * O0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 83 - 83: IIII / O0oO
   else :
    pass
  OOo000OO000 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 83 - 83: OOooOOo % OoOO + o0000oOoOoO0o % i11iIiiIii + O0
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OOo000OO000 ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 65 - 65: iIii1I11I1II1 % OoOO + O0 / OoooooooOO
   if oOo0Oo0O0O > 0 :
    if 52 - 52: o00O0oo % OoOO0ooOOoo0O * OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / oO0o0ooO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( oOo0Oo0O0O ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 80 - 80: OoooooooOO + IIII
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 95 - 95: O0oO / OoOO * O0oO - OoooooooOO * OoooooooOO % Ooo00oOo00o
   else :
    pass
    if 43 - 43: Oo . O0oO
    if 12 - 12: O0oO + OoOO0ooOOoo0O + o0000oOoOoO0o . IIII / o00O0oo
    if 29 - 29: IIII . o0oO0 - OoOoOO00
    if 68 - 68: iIii1I11I1II1 + OoOoOO00 / OoOO
 oOooo00000 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( oOooo00000 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( oOooo00000 ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 26 - 26: O0
   if 34 - 34: o0oO0 * O0oO
   if oOo0Oo0O0O > 0 :
    if 97 - 97: i11iIiiIii % OoOO / Oo / Oo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete WTF Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 97 - 97: OoOoOO00 - O0oO - iIii1I11I1II1 * OOOo0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 54 - 54: iIii1I11I1II1
   else :
    pass
    if 5 - 5: IIII
    if 84 - 84: OoOoOO00 * OoOO * OoOoOO00 % IIII / OOOo0
 O0Oooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( O0Oooo ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O0Oooo ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 27 - 27: o0oO0 + i11iIiiIii * o0000oOoOoO0o + I1IiI + oO0o0ooO0
   if 87 - 87: O0
   if oOo0Oo0O0O > 0 :
    if 87 - 87: OOooOOo / OoOoOO00
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete 4oD Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: o0oO0 - ii11ii1ii - O0 + o00O0oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 68 - 68: OoOO0ooOOoo0O . Oo % o0oO0 - OoooooooOO * oO0o0ooO0 . OoOO0ooOOoo0O
   else :
    pass
    if 46 - 46: i11iIiiIii - OoOO0ooOOoo0O * OOOo0 * o0000oOoOoO0o % ii11ii1ii * i1IIi
    if 5 - 5: O0 / o0oO0 . Oo + OoooooooOO
 O0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( O0o ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O0o ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 78 - 78: OoOO0ooOOoo0O % iIii1I11I1II1
   if 50 - 50: OOOo0 % iIii1I11I1II1 % OoOO0ooOOoo0O
   if oOo0Oo0O0O > 0 :
    if 84 - 84: IIII + ii11ii1ii + o00O0oo + oO0o0ooO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete BBC iPlayer Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 62 - 62: i11iIiiIii + I1IiI + i1IIi
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 69 - 69: I1IiI
   else :
    pass
    if 63 - 63: Ooo00oOo00o / I1IiI * iIii1I11I1II1 . O0oO
    if 85 - 85: i11iIiiIii / i11iIiiIii . Ooo00oOo00o . O0
    if 67 - 67: OoOoOO00 / OOooOOo . OoOO0ooOOoo0O . OoooooooOO
 i1I1Ii11i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( i1I1Ii11i ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( i1I1Ii11i ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 19 - 19: IIII - OOooOOo . iIii1I11I1II1 . I1IiI / OoOO0ooOOoo0O
   if 87 - 87: I1IiI - o0oO0 - OoOO0ooOOoo0O + Oo % iIii1I11I1II1 / i11iIiiIii
   if oOo0Oo0O0O > 0 :
    if 12 - 12: o0oO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Simple Downloader Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 86 - 86: OoOO - Ooo00oOo00o
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 63 - 63: OOOo0 / I1IiI + OoooooooOO . o0000oOoOoO0o . o0oO0
   else :
    pass
    if 48 - 48: i1IIi - oO0o0ooO0 - i11iIiiIii . o0000oOoOoO0o - oO0o0ooO0 * o0000oOoOoO0o
    if 60 - 60: I1IiI / ii11ii1ii + OoOO0ooOOoo0O - oO0o0ooO0
 IIii1III = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IIii1III ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( IIii1III ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 94 - 94: i11iIiiIii % OoooooooOO / OOOo0
   if 24 - 24: OOOo0 * OoOO
   if oOo0Oo0O0O > 0 :
    if 85 - 85: OoOoOO00 . o0oO0 % OoOO0ooOOoo0O % o0000oOoOoO0o
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ITV Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 80 - 80: OoOO * o0000oOoOoO0o / iIii1I11I1II1 % OoOO / iIii1I11I1II1
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 42 - 42: i1IIi / i11iIiiIii . Oo * oO0o0ooO0 . i11iIiiIii * O0
   else :
    pass
    if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + IIII
    if 27 - 27: OoOO0ooOOoo0O
 O0OO0ooO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( IIii1III ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O0OO0ooO00 ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 83 - 83: iIii1I11I1II1
   if 63 - 63: OoooooooOO * Ooo00oOo00o / o0000oOoOoO0o - OoOO . iIii1I11I1II1 + oO0o0ooO0
   if oOo0Oo0O0O > 0 :
    if 44 - 44: i1IIi % OOOo0 % OOooOOo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Movies4me Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 9 - 9: Oo % OoooooooOO - o00O0oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 43 - 43: Ooo00oOo00o % Ooo00oOo00o
   else :
    pass
    if 46 - 46: Oo % iIii1I11I1II1 . oO0o0ooO0 . O0 * o0oO0 / OoooooooOO
    if 7 - 7: OoOO - O0 * o0000oOoOoO0o - OOooOOo - OoOoOO00
 Ii11iiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( IIii1III ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( Ii11iiI1 ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 71 - 71: OOooOOo / OoOO0ooOOoo0O % OoOO0ooOOoo0O
   if 89 - 89: OoooooooOO + i11iIiiIii / o0000oOoOoO0o + iIii1I11I1II1 % o0oO0
   if oOo0Oo0O0O > 0 :
    if 29 - 29: ii11ii1ii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Phoenix Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: i11iIiiIii . ii11ii1ii % o00O0oo / o0oO0 % iIii1I11I1II1
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 6 - 6: Oo - OoOO0ooOOoo0O . iIii1I11I1II1
   else :
    pass
    if 30 - 30: o0oO0 + o0oO0 % IIII - OOooOOo - ii11ii1ii
    if 36 - 36: o0000oOoOoO0o % OoOO0ooOOoo0O
 OoO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( IIii1III ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OoO0 ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 37 - 37: o0000oOoOoO0o
   if 83 - 83: O0
   if oOo0Oo0O0O > 0 :
    if 89 - 89: Oo + ii11ii1ii - OOooOOo
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Music Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 40 - 40: Ooo00oOo00o + Ooo00oOo00o
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 94 - 94: oO0o0ooO0 * iIii1I11I1II1 . o0000oOoOoO0o
   else :
    pass
    if 13 - 13: iIii1I11I1II1 * I1IiI / O0oO % o0oO0 + OoOO
    if 41 - 41: ii11ii1ii
 i1iI1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( IIii1III ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( i1iI1i ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 59 - 59: IIII
   if 89 - 89: I1IiI % iIii1I11I1II1
   if oOo0Oo0O0O > 0 :
    if 35 - 35: ii11ii1ii + O0oO - I1IiI % OoOO % OOooOOo % I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete SuperCartoons Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 24 - 24: o0oO0 - o0000oOoOoO0o * OoOO
   else :
    pass
    if 87 - 87: o00O0oo - ii11ii1ii % ii11ii1ii . OoOO / ii11ii1ii
    if 6 - 6: I1IiI / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
 o0O0OOo0oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( IIii1III ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( o0O0OOo0oO ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 42 - 42: OoOoOO00 / O0 . iIii1I11I1II1 / O0 / Ooo00oOo00o / OoooooooOO
   if 62 - 62: O0 . Oo
   if oOo0Oo0O0O > 0 :
    if 33 - 33: Oo / iIii1I11I1II1 % i1IIi
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete TVonline Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 76 - 76: o00O0oo + iIii1I11I1II1 + I1IiI . Ooo00oOo00o
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 49 - 49: IIII / o0oO0 / OoOO0ooOOoo0O
   else :
    pass
    if 25 - 25: OOOo0 % O0 + i1IIi - o0oO0
    if 38 - 38: OOooOOo % O0oO + i11iIiiIii + oO0o0ooO0 + o0oO0 / i11iIiiIii
 o0OOOOOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( IIii1III ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( o0OOOOOo0 ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 57 - 57: iIii1I11I1II1 + iIii1I11I1II1
   if 56 - 56: OoOO + o0oO0
   if oOo0Oo0O0O > 0 :
    if 32 - 32: OoOoOO00 + I1IiI % o0oO0 / I1IiI + ii11ii1ii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 2 - 2: i11iIiiIii - O0oO + Ooo00oOo00o % o0000oOoOoO0o * o00O0oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
      if 54 - 54: O0 - oO0o0ooO0 . OoOO0ooOOoo0O % oO0o0ooO0 + oO0o0ooO0
   else :
    pass
    if 36 - 36: OoOO0ooOOoo0O % i11iIiiIii
    if 47 - 47: i1IIi + OoOoOO00 . Oo * OoOO . o0000oOoOoO0o / i1IIi
    if 50 - 50: O0oO / i1IIi % OoooooooOO
 oOOOOO0Ooooo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 try :
  if i1iiIII111ii . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   o0o000Oo = os . path . join ( oOOOOO0Ooooo , "cache.db" )
   os . unlink ( o0o000Oo )
   if 57 - 57: OoOO * O0 * O0oO
 except :
  pass
  if 44 - 44: OoOO0ooOOoo0O / Oo + IIII % OoOoOO00 / Ooo00oOo00o + i11iIiiIii
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 20 - 20: ii11ii1ii
 if 3 - 3: Ooo00oOo00o * i1IIi . OOOo0 . O0 - I1IiI
 if 81 - 81: OOOo0 - iIii1I11I1II1 / OOOo0 / O0
 if 34 - 34: o00O0oo * o00O0oo - ii11ii1ii - O0 . i11iIiiIii
 if 32 - 32: iIii1I11I1II1 . Ooo00oOo00o * OoOO / OoOO0ooOOoo0O . OoOoOO00 - Oo
 if 10 - 10: ii11ii1ii / i11iIiiIii - o00O0oo + OoOO * OOOo0
 if 94 - 94: OOOo0 + iIii1I11I1II1 / O0 - OoooooooOO % ii11ii1ii
 if 64 - 64: o0000oOoOoO0o + Ooo00oOo00o
 if 25 - 25: OOOo0 . o0oO0 + OOOo0 % o00O0oo * iIii1I11I1II1
def iiI1iI ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 Ooo00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( Ooo00O0 ) :
   oOo0Oo0O0O = 0
   oOo0Oo0O0O += len ( oOo0OOoO0 )
   if 70 - 70: OOOo0 - o0oO0 - Ooo00oOo00o - I1IiI . i11iIiiIii % i1IIi
   if 1 - 1: OoOO / i1IIi
   if oOo0Oo0O0O > 0 :
    if 74 - 74: o0000oOoOoO0o / OoooooooOO / Oo * i11iIiiIii . OoOoOO00 . OoooooooOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Package Cache Files" , str ( oOo0Oo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 59 - 59: i11iIiiIii . OoooooooOO / o0000oOoOoO0o * ii11ii1ii + OoooooooOO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for OOOOo00oo00O in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , OOOOo00oo00O ) )
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
 if 3 - 3: i11iIiiIii * Oo % iIii1I11I1II1 % OOOo0 * oO0o0ooO0 / OoOO0ooOOoo0O
 if 95 - 95: IIII * O0 * O0oO . OoooooooOO % Oo + ii11ii1ii
 if 98 - 98: OoOO . OoooooooOO
 if 54 - 54: O0 / IIII % o0oO0 * i1IIi * O0
 if 48 - 48: OOooOOo . OoOO % I1IiI - I1IiI
 if 33 - 33: o0000oOoOoO0o % OoOoOO00 + Ooo00oOo00o
 if 93 - 93: i1IIi . IIII / OOOo0 + IIII
 if 58 - 58: ii11ii1ii + O0 . Oo + I1IiI - Ooo00oOo00o - I1IiI
 if 41 - 41: Oo / i1IIi / Oo - oO0o0ooO0 . OOooOOo
def Oooooooo00o00 ( url , name ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O0oo00OOOO = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 IiIi1II111I = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( IiIi1II111I ) == False :
  if i1iiIII111ii . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   O0oo00OOOO = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
   try :
    os . remove ( O0oo00OOOO )
    print '=== GenieTv - REMOVING    ' + str ( O0oo00OOOO ) + '    ==='
   except :
    pass
   O0ii1ii1ii = I11 . http_GET ( url ) . content
   IIo0Oo0oO0oOO00 = open ( O0oo00OOOO , "w" )
   IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
   IIo0Oo0oO0oOO00 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( O0oo00OOOO ) + '    ==='
   i1iiIII111ii = xbmcgui . Dialog ( )
   i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  O0oo00OOOO = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
  try :
   os . remove ( O0oo00OOOO )
   print '=== GenieTv - REMOVING    ' + str ( O0oo00OOOO ) + '    ==='
  except :
   pass
  O0ii1ii1ii = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( O0oo00OOOO , "w" )
  IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O0oo00OOOO ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 80 - 80: o00O0oo / OoOO0ooOOoo0O
def iIIi1i11 ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O0oo00OOOO = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  IIo0Oo0oO0oOO00 = open ( O0oo00OOOO ) . read ( )
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
 if 34 - 34: Ooo00oOo00o % OOooOOo % OOOo0
def Ii1iIII11iIIi ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O0oo00OOOO = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  os . remove ( O0oo00OOOO )
  i1iiIII111ii = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( O0oo00OOOO ) + '    ==='
  i1iiIII111ii . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 11 - 11: IIII + iIii1I11I1II1 . i11iIiiIii - OoOO0ooOOoo0O
 if 49 - 49: o0oO0 . OoOoOO00
 if 24 - 24: O0 . OoooooooOO - Ooo00oOo00o * OoooooooOO
 if 12 - 12: O0 + IIII * i1IIi . Ooo00oOo00o
 if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
 if 28 - 28: iIii1I11I1II1
 if 7 - 7: OOooOOo % IIII * I1IiI
 if 58 - 58: IIII / o0000oOoOoO0o + OoOoOO00 % oO0o0ooO0 - OoooooooOO
 if 25 - 25: I1IiI % OoooooooOO * Oo - i1IIi * OoOoOO00 * OoOO
 if 30 - 30: o0000oOoOoO0o % I1IiI / ii11ii1ii * O0 * o00O0oo . OOOo0
def iIi11I11 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 III1iII1I1ii = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for i1i , oOI11 , iiI , i1iIii1i111 in III1iII1I1ii :
  if inc < 2 : i1iiIII111ii = xbmcgui . Dialog ( ) ; i1iiIII111ii . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1i , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iiI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % i1iIii1i111 )
  inc = inc + 1
  if 65 - 65: Oo * O0 / o00O0oo . O0oO % Oo
  if 24 - 24: Ooo00oOo00o
  if 99 - 99: OoOO0ooOOoo0O / IIII / o00O0oo
  if 84 - 84: Ooo00oOo00o / iIii1I11I1II1
  if 33 - 33: i1IIi / O0oO - i1IIi . Oo
  if 18 - 18: Oo / O0 + oO0o0ooO0
  if 65 - 65: i1IIi . ii11ii1ii / o0oO0
  if 11 - 11: IIII * o0oO0 / o0oO0 - OoOO0ooOOoo0O
  if 68 - 68: OOOo0 % IIII - IIII / OOOo0 + ii11ii1ii - Oo
def o0oO0o00O ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  O0oo00OOOO = os . path . join ( oOo00O0oo00o0 , 'addons2.ini' )
  O0ii1ii1ii = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( O0oo00OOOO , "w" )
  IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O0oo00OOOO ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 6 - 6: OoooooooOO / i11iIiiIii / O0oO
def OooO0O0Ooo ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  O0oo00OOOO = os . path . join ( oOo00O0oo00o0 , 'settings.xml' )
  O0ii1ii1ii = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( O0oo00OOOO , "w" )
  IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O0oo00OOOO ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 85 - 85: OOooOOo / O0oO
 if 67 - 67: o0000oOoOoO0o % OoOO
def ii1iiIi ( ) :
 try :
  i11ii1i1i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( i11ii1i1i ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iIIi1 = os . path . join ( i11ii1i1i , "source.db" )
    os . unlink ( iIIi1 )
  i1iiIII111ii . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 9 - 9: OoooooooOO + OOooOOo + o00O0oo % o00O0oo % Oo . IIII
 if 76 - 76: OoooooooOO - OoOoOO00 % I1IiI + OoOO + iIii1I11I1II1 . I1IiI
 if 16 - 16: OOooOOo . o0000oOoOoO0o
 if 50 - 50: o0oO0 * I1IiI + ii11ii1ii - i11iIiiIii + Oo * ii11ii1ii
 if 20 - 20: O0oO / OOooOOo % I1IiI
def oooooOoo0ooo ( url ) :
 O00O0Ooooo00 = urllib2 . Request ( url )
 O00O0Ooooo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O000 = urllib2 . urlopen ( O00O0Ooooo00 )
 O0ii1ii1ii = O000 . read ( )
 O000 . close ( )
 return O0ii1ii1ii
 if 69 - 69: O0oO - i1IIi % oO0o0ooO0 . OoOO0ooOOoo0O - OoOO0ooOOoo0O
 if 65 - 65: OoOO0ooOOoo0O + OoOoOO00
 if 61 - 61: i11iIiiIii * OoOO % Oo * O0oO - OoooooooOO - Ooo00oOo00o
 if 83 - 83: o0oO0 / OoOO0ooOOoo0O
 if 39 - 39: IIII + o0000oOoOoO0o
 if 9 - 9: OOOo0 % o0000oOoOoO0o . Oo * OOOo0
 if 99 - 99: O0 . OOooOOo % o0000oOoOoO0o - Oo / o0000oOoOoO0o
def iI1iii1i1III1 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iiIII1 = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iiIII1 :
  iiI1iIiI111 = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; iiI1iIiI111 = xbmc . translatePath ( iiI1iIiI111 ) ;
  iI1111I = os . path . join ( iiI1iIiI111 , ".." , ".." ) ; iI1111I = os . path . abspath ( iI1111I ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iI1111I ) ; iiiI11 = False
  try :
   for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iI1111I , topdown = True ) :
    Ooo0OOoOoO0 [ : ] = [ OOOOo00oo00O for OOOOo00oo00O in Ooo0OOoOoO0 if OOOOo00oo00O not in Oo0oO0ooo ]
    for oOOo0 in oOo0OOoO0 :
     try : os . remove ( os . path . join ( iiI11ii1I1 , oOOo0 ) )
     except :
      if oOOo0 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iiiI11 = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oOOo0 )
    for oOOo0 in Ooo0OOoOoO0 :
     try : os . rmdir ( os . path . join ( iiI11ii1I1 , oOOo0 ) )
     except :
      if oOOo0 not in [ "Database" , "userdata" ] : iiiI11 = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oOOo0 )
   if not iiiI11 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OoOOoOooooOOo ( )
 if 89 - 89: OoOO
 if 87 - 87: oO0o0ooO0 % Oo
 if 62 - 62: Ooo00oOo00o + o0oO0 / oO0o0ooO0 * i11iIiiIii
def iiIIIIiI111 ( ) :
 OoooOO0Oo0 = [ ]
 I1iIiIii = sys . argv [ 2 ]
 if len ( I1iIiIii ) >= 2 :
  OO0 = sys . argv [ 2 ]
  I1iiI1iiI1i1 = OO0 . replace ( '?' , '' )
  if ( OO0 [ len ( OO0 ) - 1 ] == '/' ) :
   OO0 = OO0 [ 0 : len ( OO0 ) - 2 ]
  OOOO00OOO00 = I1iiI1iiI1i1 . split ( '&' )
  OoooOO0Oo0 = { }
  for ii1OO0 in range ( len ( OOOO00OOO00 ) ) :
   OoOoO00OOoOOOo0 = { }
   OoOoO00OOoOOOo0 = OOOO00OOO00 [ ii1OO0 ] . split ( '=' )
   if ( len ( OoOoO00OOoOOOo0 ) ) == 2 :
    OoooOO0Oo0 [ OoOoO00OOoOOOo0 [ 0 ] ] = OoOoO00OOoOOOo0 [ 1 ]
    if 84 - 84: OoOO + OoOO0ooOOoo0O . oO0o0ooO0
 return OoooOO0Oo0
 if 71 - 71: o0oO0 / o0oO0 . I1IiI % oO0o0ooO0
I1iI1ii1II = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
iiOOooooO0Oo = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O0O0OOOOoo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I1i1i1O0 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1I1IiI1 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
i1I11I = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
OOoooooooO = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
I1IIi1i1Ii1I1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
OoO0O000 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
iIIiI11i1I11 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
IiIIiii11II1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OooooO = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
III1ii = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
i1I1I1i1i1i = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
I11i1iIi111 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OoOoO0oOOooo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ooo0ooo = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
ii = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oOO00Oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
IIooooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
IIIIiiIiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
ooo0O0o0OoOO = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
Iiii1iiiIiI1 = base64 . decodestring ( 'Q1VOVA==' )
def ii11i1iIII ( name , url , mode , iconimage , fanart , description ) :
 iiII1IiIi1iI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOiiI1Ii11II1I = True
 IIIIIii1ii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIIii1ii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIIIIii1ii11 . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  oOiiI1Ii11II1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiII1IiIi1iI1 , listitem = IIIIIii1ii11 , isFolder = False )
 else :
  oOiiI1Ii11II1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiII1IiIi1iI1 , listitem = IIIIIii1ii11 , isFolder = True )
 return oOiiI1Ii11II1I
def i111IiI1I ( name , url , mode , iconimage , fanart , description ) :
 iiII1IiIi1iI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOiiI1Ii11II1I = True
 IIIIIii1ii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIIii1ii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIIIIii1ii11 . setProperty ( "Fanart_Image" , fanart )
 oOiiI1Ii11II1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiII1IiIi1iI1 , listitem = IIIIIii1ii11 , isFolder = False )
 return oOiiI1Ii11II1I
 if 75 - 75: o0000oOoOoO0o . OoOO0ooOOoo0O - iIii1I11I1II1 * Ooo00oOo00o * oO0o0ooO0
 if 93 - 93: o0oO0
OO0 = iiIIIIiI111 ( )
oo000o = None
oOOo0 = None
iII1IIiiI11II = None
oo00O00oO = None
iIiIIIi = None
ooo00OOOooO = None
if 70 - 70: o00O0oo - OoOO0ooOOoo0O * OoOO0ooOOoo0O / iIii1I11I1II1 + O0
if 49 - 49: i11iIiiIii - ii11ii1ii - o0000oOoOoO0o / OoooooooOO % I1IiI
try :
 oo000o = urllib . unquote_plus ( OO0 [ "url" ] )
except :
 pass
try :
 oOOo0 = urllib . unquote_plus ( OO0 [ "name" ] )
except :
 pass
try :
 oo00O00oO = urllib . unquote_plus ( OO0 [ "iconimage" ] )
except :
 pass
try :
 iII1IIiiI11II = int ( OO0 [ "mode" ] )
except :
 pass
try :
 iIiIIIi = urllib . unquote_plus ( OO0 [ "fanart" ] )
except :
 pass
try :
 ooo00OOOooO = urllib . unquote_plus ( OO0 [ "description" ] )
except :
 pass
 if 65 - 65: O0 - O0oO . o00O0oo
 if 19 - 19: ii11ii1ii . oO0o0ooO0 - OOooOOo + o0000oOoOoO0o - o00O0oo
print str ( II ) + ': ' + str ( oOOoO0 )
print "Mode: " + str ( iII1IIiiI11II )
print "URL: " + str ( oo000o )
print "Name: " + str ( oOOo0 )
print "IconImage: " + str ( oo00O00oO )
if 13 - 13: IIII * ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % iIii1I11I1II1
if 21 - 21: ii11ii1ii
def III1ii1iII ( content , viewType ) :
 if 86 - 86: o0oO0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 51 - 51: Ooo00oOo00o - i11iIiiIii * OOOo0
  if 95 - 95: OoOO0ooOOoo0O % ii11ii1ii + OOooOOo % o0oO0
if iII1IIiiI11II == None :
 I11I11i1I ( )
 if 36 - 36: O0 / i1IIi % OoOoOO00 / oO0o0ooO0
elif iII1IIiiI11II == 1 :
 I11iI ( oo000o )
 if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
elif iII1IIiiI11II == 44 :
 oOo00oOoO000 ( oo000o )
 if 91 - 91: OoOoOO00 . OoOO0ooOOoo0O + OOooOOo
elif iII1IIiiI11II == 2 :
 O000OOOOOo ( )
 if 8 - 8: OoOO0ooOOoo0O * Oo / oO0o0ooO0 - Ooo00oOo00o - OoooooooOO
elif iII1IIiiI11II == 3 :
 oO000Oo000 ( )
 if 100 - 100: OoOO . iIii1I11I1II1 . iIii1I11I1II1
elif iII1IIiiI11II == 21 :
 oOOOOo0 ( )
 if 55 - 55: OoOO
elif iII1IIiiI11II == 4 :
 oO00O0O0O ( )
 if 37 - 37: IIII / i11iIiiIii / Oo
elif iII1IIiiI11II == 5 :
 IiiiIIiIi1 ( oOOo0 , oo000o , ooo00OOOooO )
 if 97 - 97: O0oO . o0000oOoOoO0o / OOOo0
elif iII1IIiiI11II == 6 :
 iiI1iI ( oo000o )
 if 83 - 83: o0000oOoOoO0o - ii11ii1ii * OoOO
elif iII1IIiiI11II == 7 :
 Oooooooo00o00 ( oo000o , oOOo0 )
 if 90 - 90: Oo * OOOo0
elif iII1IIiiI11II == 8 :
 iIIi1i11 ( oo000o , oOOo0 )
 if 75 - 75: ii11ii1ii - I1IiI * i11iIiiIii . OoooooooOO - Oo . o0000oOoOoO0o
elif iII1IIiiI11II == 9 :
 FIXREPOSADDONS ( oo000o )
 if 6 - 6: o0000oOoOoO0o * OoOO / OoooooooOO % o00O0oo * OOooOOo
elif iII1IIiiI11II == 10 :
 o00oOOooOOo0o ( )
 if 28 - 28: IIII * OOOo0 % IIII
elif iII1IIiiI11II == 11 :
 Ii1iIII11iIIi ( oo000o )
 if 95 - 95: O0 / o0000oOoOoO0o . O0oO
elif iII1IIiiI11II == 12 :
 iIi11I11 ( )
 if 17 - 17: o0000oOoOoO0o
elif iII1IIiiI11II == 13 :
 oOOoO ( )
 if 56 - 56: o0oO0 * OOooOOo + o0000oOoOoO0o
elif iII1IIiiI11II == 14 :
 Oo00O0OO ( oo000o )
 if 48 - 48: IIII * Ooo00oOo00o % O0oO - o0000oOoOoO0o
elif iII1IIiiI11II == 15 :
 ooOO00O00oo ( )
 if 72 - 72: i1IIi % o0oO0 % IIII % OoOO - OoOO
elif iII1IIiiI11II == 16 :
 o0oO0o00O ( oo000o , oOOo0 )
 if 97 - 97: OOooOOo * O0 / OOooOOo * Ooo00oOo00o * Oo
elif iII1IIiiI11II == 17 :
 OooO0O0Ooo ( oo000o , oOOo0 )
 if 38 - 38: O0oO
elif iII1IIiiI11II == 18 :
 ii1iiIi ( )
 if 25 - 25: iIii1I11I1II1 % OoOoOO00 / o0000oOoOoO0o / ii11ii1ii
elif iII1IIiiI11II == 19 :
 oo0oO0oOOoo ( oOOo0 , oo000o , ooo00OOOooO )
 if 22 - 22: OoOO * oO0o0ooO0
elif iII1IIiiI11II == 40 :
 OOo0oO00ooO00 ( oOOo0 , oo000o , ooo00OOOooO )
 if 4 - 4: I1IiI - OoOO + OOOo0
elif iII1IIiiI11II == 42 :
 O00o0OO0 ( oOOo0 , oo000o , ooo00OOOooO )
 if 36 - 36: IIII
elif iII1IIiiI11II == 43 :
 oOOOoo0O0oO ( oOOo0 , oo000o , ooo00OOOooO )
 if 19 - 19: I1IiI . OOooOOo . OoooooooOO
elif iII1IIiiI11II == 20 :
 Ii1I1IIii1II ( oo000o )
 if 13 - 13: OoOO0ooOOoo0O . Oo / OoOoOO00
elif iII1IIiiI11II == 22 :
 oOo00o ( oo000o )
 if 43 - 43: iIii1I11I1II1 % Ooo00oOo00o
elif iII1IIiiI11II == 23 :
 iIIiIii11i1Ii ( oo000o )
 if 84 - 84: Oo
elif iII1IIiiI11II == 24 :
 oooOO0oOooO00 ( oo000o )
 if 44 - 44: OoooooooOO * i11iIiiIii / Oo
elif iII1IIiiI11II == 25 :
 o0oO0OO00ooOO ( oo000o )
 if 75 - 75: OoooooooOO . OoOO0ooOOoo0O + Ooo00oOo00o / o00O0oo - OOOo0 % o00O0oo
elif iII1IIiiI11II == 26 :
 II1II1iI ( oo000o )
 if 89 - 89: oO0o0ooO0 * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
elif iII1IIiiI11II == 27 :
 iI111i11iI1 ( oo000o )
 if 51 - 51: OoOO0ooOOoo0O / o0oO0 + Ooo00oOo00o % I1IiI / o00O0oo
elif iII1IIiiI11II == 28 :
 O0oOo00O ( oo000o )
 if 25 - 25: OOooOOo
elif iII1IIiiI11II == 29 :
 Ii11ii1Iiii ( oo000o )
 if 25 - 25: o0oO0 * oO0o0ooO0 / o0000oOoOoO0o / o0000oOoOoO0o % OOooOOo
elif iII1IIiiI11II == 30 :
 IIi ( oo000o )
 if 19 - 19: OoOO - iIii1I11I1II1 / o0oO0 . Ooo00oOo00o * O0 - O0
elif iII1IIiiI11II == 31 :
 ooOoooo0 ( oo000o )
 if 41 - 41: i1IIi - OOOo0
elif iII1IIiiI11II == 32 :
 iII ( )
 if 48 - 48: OOOo0 - OoOoOO00 / Ooo00oOo00o + OOOo0
elif iII1IIiiI11II == 33 :
 I1I111 ( )
 if 5 - 5: O0
elif iII1IIiiI11II == 35 :
 O0OooOo0o ( oo000o )
 if 75 - 75: O0oO + iIii1I11I1II1
elif iII1IIiiI11II == 34 :
 o0OOOO00O0Oo ( oo000o )
 if 19 - 19: OOOo0 + i11iIiiIii . IIII - o0000oOoOoO0o / o00O0oo + OOooOOo
elif iII1IIiiI11II == 36 :
 i1oOo ( oo000o )
 if 38 - 38: Oo / iIii1I11I1II1 * iIii1I11I1II1 % ii11ii1ii
elif iII1IIiiI11II == 37 :
 oOOo0oOo0 ( oo000o )
 if 92 - 92: o0000oOoOoO0o / O0 * OOOo0 - o0000oOoOoO0o
elif iII1IIiiI11II == 38 :
 III1Iiii1I11 ( oo000o )
 if 99 - 99: i11iIiiIii % OoooooooOO
elif iII1IIiiI11II == 41 :
 iI1iii1i1III1 ( OO0 )
 if 56 - 56: IIII * O0oO
elif iII1IIiiI11II == 39 :
 IIiiiiIi1I ( oo000o )
 if 98 - 98: o0000oOoOoO0o + O0 * O0oO + i11iIiiIii - OoOO0ooOOoo0O - iIii1I11I1II1
elif iII1IIiiI11II == 45 :
 TEXTS ( )
 if 5 - 5: OoOO0ooOOoo0O % Oo % IIII % o0oO0
elif iII1IIiiI11II == 46 :
 iI1iIiiiI1I1 ( )
 if 17 - 17: o00O0oo + OoOoOO00 + OoooooooOO / OoOO0ooOOoo0O / IIII
elif iII1IIiiI11II == 47 :
 GEVID ( )
 if 80 - 80: OOooOOo % i1IIi / o0000oOoOoO0o
elif iII1IIiiI11II == 48 :
 O0O ( oOOo0 , oo000o , ooo00OOOooO )
 if 56 - 56: i1IIi . i11iIiiIii
elif iII1IIiiI11II == 49 :
 i1I11i1I ( )
 if 15 - 15: OoOoOO00 * OoOO % oO0o0ooO0 / i11iIiiIii - OoOO + Oo
elif iII1IIiiI11II == 222 :
 OO00OO0o0 ( oo000o )
 if 9 - 9: o0000oOoOoO0o - OoOO + O0 / oO0o0ooO0 % i1IIi
elif iII1IIiiI11II == 333 :
 I1I11ii ( oo000o )
 if 97 - 97: OOooOOo * o0oO0
 if 78 - 78: o0000oOoOoO0o . OoOO0ooOOoo0O + OoOO * oO0o0ooO0 - i1IIi
elif iII1IIiiI11II == 1001 :
 OoIIi1iI ( )
 if 27 - 27: o00O0oo % i1IIi . Oo % O0oO
elif iII1IIiiI11II == 1005 :
 II1Ii ( )
 if 10 - 10: IIII / OoooooooOO
elif iII1IIiiI11II == 1007 :
 OOoO00ooO ( oo000o )
 if 50 - 50: i11iIiiIii - OoooooooOO . OoOO + O0 . i1IIi
elif iII1IIiiI11II == 1010 :
 iiii111IiIIi1 ( oo000o )
 if 91 - 91: OOooOOo . oO0o0ooO0 % Oo - oO0o0ooO0 . OoOO % i11iIiiIii
elif iII1IIiiI11II == 1011 :
 Oo0000o0O0O ( oo000o )
 if 25 - 25: iIii1I11I1II1
elif iII1IIiiI11II == 1030 :
 oooO ( )
 if 63 - 63: o0oO0
elif iII1IIiiI11II == 1031 :
 iiIIi ( oo000o , oo00O00oO )
 if 96 - 96: o0000oOoOoO0o
elif iII1IIiiI11II == 1006 :
 Parse . ParseURL ( oo000o )
 if 34 - 34: I1IiI / Ooo00oOo00o - OOOo0 . O0 . OoOO0ooOOoo0O
elif iII1IIiiI11II == 2030 :
 Parse . addonParseURL ( oo000o )
 if 63 - 63: oO0o0ooO0
elif iII1IIiiI11II == 2031 :
 Parse . apkParseURL ( oo000o )
 if 11 - 11: oO0o0ooO0 - iIii1I11I1II1
elif iII1IIiiI11II == 1002 :
 O00o0O ( oo000o )
 if 92 - 92: Ooo00oOo00o
elif iII1IIiiI11II == 1003 :
 iIIIiI ( oo000o , oo00O00oO )
 if 15 - 15: IIII / IIII + iIii1I11I1II1 % OoooooooOO
elif iII1IIiiI11II == 1004 :
 O00 ( oo000o )
 if 12 - 12: o0oO0
elif iII1IIiiI11II == 1008 :
 OooOOo0 ( )
 if 36 - 36: O0oO . IIII * OoooooooOO - OOooOOo
elif iII1IIiiI11II == 1009 :
 M3UPLAY ( oo000o )
 if 60 - 60: OoOO0ooOOoo0O . oO0o0ooO0 / iIii1I11I1II1 + OoOO0ooOOoo0O * O0oO
elif iII1IIiiI11II == 2001 :
 OOOIiIi1111ii ( oo000o )
 if 82 - 82: i11iIiiIii . iIii1I11I1II1 * OOOo0 - o0000oOoOoO0o + o00O0oo
elif iII1IIiiI11II == 1013 :
 II1i111Ii1i ( )
 if 48 - 48: ii11ii1ii
elif iII1IIiiI11II == 1014 :
 OO0oo ( )
 if 96 - 96: o0oO0 . OoooooooOO
elif iII1IIiiI11II == 1015 :
 IiIi1II11i ( oo000o )
 if 39 - 39: OoOO0ooOOoo0O + Ooo00oOo00o
elif iII1IIiiI11II == 1016 :
 Ii1iI ( oo000o )
 if 80 - 80: OoOO0ooOOoo0O % Ooo00oOo00o / I1IiI
elif iII1IIiiI11II == 1023 :
 i1II1 ( )
 if 54 - 54: Oo % Ooo00oOo00o - OoOO0ooOOoo0O - o0000oOoOoO0o
elif iII1IIiiI11II == 1024 :
 iIi1iIIIiIiI ( )
 if 71 - 71: o0oO0 . i11iIiiIii
elif iII1IIiiI11II == 1025 :
 OooOo000o0o ( oo000o )
 if 56 - 56: O0 * oO0o0ooO0 + oO0o0ooO0 * iIii1I11I1II1 / o0oO0 * O0oO
elif iII1IIiiI11II == 4001 :
 iI1 ( )
 if 25 - 25: iIii1I11I1II1 . o0000oOoOoO0o * i11iIiiIii + Oo * o0000oOoOoO0o
elif iII1IIiiI11II == 4002 :
 i11Iiii ( )
 if 67 - 67: oO0o0ooO0
elif iII1IIiiI11II == 4003 :
 oo000OO00Oo ( )
 if 88 - 88: Oo
elif iII1IIiiI11II == 3000 :
 I1I ( )
 if 8 - 8: ii11ii1ii
elif iII1IIiiI11II == 404 :
 o0IiiiI111I ( oOOo0 , oo000o , oo00O00oO )
 if 82 - 82: OoooooooOO
elif iII1IIiiI11II == 7030 :
 IIi1I ( )
 if 75 - 75: OoOoOO00 % OOOo0 + OoOO0ooOOoo0O % OoooooooOO / IIII
elif iII1IIiiI11II == 7021 :
 Ooo0Oo0oo0 ( oOOo0 )
 if 4 - 4: i11iIiiIii - OoOO0ooOOoo0O % ii11ii1ii * O0oO % OOooOOo
elif iII1IIiiI11II == 7022 :
 iIIi1I1ii ( oOOo0 )
 if 71 - 71: o0oO0 . o0oO0 - iIii1I11I1II1
elif iII1IIiiI11II == 7000 :
 o0Oo ( oOOo0 , oo000o , img )
 if 22 - 22: OoooooooOO / ii11ii1ii % oO0o0ooO0 * I1IiI
elif iII1IIiiI11II == 7050 :
 I11IIIiIi11 ( )
 if 32 - 32: OoooooooOO % OoOO % iIii1I11I1II1 / O0
elif iII1IIiiI11II == 7051 :
 oOo00OooO0oO ( oo000o )
 if 61 - 61: OoOoOO00 . O0 - o00O0oo - ii11ii1ii / i11iIiiIii - OoOoOO00
elif iII1IIiiI11II == 7060 :
 I1iii ( )
 if 98 - 98: o00O0oo - OOOo0 . i11iIiiIii * Oo
elif iII1IIiiI11II == 7061 :
 Ii1I11I ( oo000o )
 if 29 - 29: o00O0oo / o0oO0 % o0000oOoOoO0o
elif iII1IIiiI11II == 7063 :
 oOO0OO0O ( oo000o )
 if 10 - 10: iIii1I11I1II1 % OoooooooOO % ii11ii1ii
elif iII1IIiiI11II == 7062 :
 ii1I11iIiIII1 ( oo000o )
 if 39 - 39: OoOoOO00 * I1IiI . O0 * o0000oOoOoO0o
elif iII1IIiiI11II == 7064 :
 NATatozcat ( )
 if 89 - 89: o00O0oo - o0oO0 . o0000oOoOoO0o - O0oO - OOOo0
elif iII1IIiiI11II == 7067 :
 IiiiIiiI ( oo000o )
 if 79 - 79: IIII + IIII + o00O0oo
elif iII1IIiiI11II == 7066 :
 NATatozA ( oo000o )
 if 39 - 39: O0 - OoooooooOO
elif iII1IIiiI11II == 7065 :
 o00O ( oo000o )
 if 63 - 63: iIii1I11I1II1 % OOooOOo * o0oO0
elif iII1IIiiI11II == 7070 :
 iiii1I1 ( )
 if 79 - 79: O0
elif iII1IIiiI11II == 7071 :
 DIZIlist ( oo000o )
 if 32 - 32: OoOoOO00 . O0 + o00O0oo / I1IiI / IIII / OoOO0ooOOoo0O
elif iII1IIiiI11II == 7072 :
 DIZIpull ( oo000o )
 if 15 - 15: ii11ii1ii
elif iII1IIiiI11II == 7073 :
 WATCHDIZI ( oo000o )
 if 4 - 4: IIII + iIii1I11I1II1 * oO0o0ooO0 + Oo * OOooOOo % OoOoOO00
elif iII1IIiiI11II == 7002 :
 I1i ( )
 if 88 - 88: OoOO - i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
elif iII1IIiiI11II == 7003 :
 I1iiIII ( oo000o )
 if 40 - 40: Oo
elif iII1IIiiI11II == 7004 :
 O00oOoo0OoO0 ( oo000o )
 if 47 - 47: I1IiI
elif iII1IIiiI11II == 7020 :
 o0oO0oo0000OO ( oo000o )
 if 65 - 65: O0 + O0oO % o00O0oo * OOOo0 / o0oO0 / I1IiI
elif iII1IIiiI11II == 7001 :
 i111i11I1ii ( )
 if 71 - 71: i11iIiiIii / I1IiI . OoOO
elif iII1IIiiI11II == 7010 :
 i1iiIIi11I ( oo000o )
 if 33 - 33: OoOO
elif iII1IIiiI11II == 7011 :
 ii1IiIi11 ( oo000o )
 if 39 - 39: Ooo00oOo00o + O0 + o0oO0 * OoOoOO00 % O0 - O0
elif iII1IIiiI11II == 7012 :
 ii1ii ( oo000o )
 if 41 - 41: IIII % OOooOOo
elif iII1IIiiI11II == 7013 :
 cnfTVPlay2 ( oo000o )
elif iII1IIiiI11II == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oo000o )
elif iII1IIiiI11II == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oo000o )
elif iII1IIiiI11II == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oOOo0 , oo000o , oo00O00oO )
elif iII1IIiiI11II == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iII1IIiiI11II == 7018 :
 ooO0oo0o0 ( )
elif iII1IIiiI11II == 7019 :
 CNF_Studio_Indexer . List_Movies ( oo000o )
elif iII1IIiiI11II == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oo000o )
elif iII1IIiiI11II == 7024 :
 CNF_Studio_Indexer . Box_Office ( oo000o )
 if 67 - 67: O0 % O0oO
elif iII1IIiiI11II == 8000 :
 o0oO0oOO ( )
elif iII1IIiiI11II == 8001 :
 O0o0O0OO00o ( )
elif iII1IIiiI11II == 8002 :
 OO00oo0o ( )
elif iII1IIiiI11II == 8003 :
 iIIIII1iiiiII ( )
elif iII1IIiiI11II == 8004 :
 oooo00o0o0o ( )
elif iII1IIiiI11II == 8005 :
 OO00oOooo0O ( )
elif iII1IIiiI11II == 8006 :
 iIII1I1i1i ( oOOo0 , oo000o )
elif iII1IIiiI11II == 8030 :
 IIi1I11I1II ( oo000o )
elif iII1IIiiI11II == 8045 :
 I11iiiii1II ( )
elif iII1IIiiI11II == 8046 :
 ooOOooOo0O ( oo000o )
elif iII1IIiiI11II == 8047 :
 iIi11i1 ( oo000o )
elif iII1IIiiI11II == 8040 :
 Ooo0o00o0o ( )
elif iII1IIiiI11II == 8041 :
 IiIIIIIi ( oo000o )
elif iII1IIiiI11II == 8042 :
 O0OoO0ooOO0o ( oo000o )
elif iII1IIiiI11II == 8043 :
 yt . PlayVideo ( oo000o )
elif iII1IIiiI11II == 8044 :
 oo00ooOoO00 ( oo000o )
elif iII1IIiiI11II == 8060 :
 Ii ( )
elif iII1IIiiI11II == 8061 :
 ii11i ( oo000o )
elif iII1IIiiI11II == 8070 :
 oo00O00oO000o ( )
elif iII1IIiiI11II == 8071 :
 OOo00OoO ( oo000o )
elif iII1IIiiI11II == 8081 :
 oOO ( )
elif iII1IIiiI11II == 8062 :
 ii1ii11 ( oo000o )
elif iII1IIiiI11II == 8063 :
 OOO0oOoO0O ( oo000o )
elif iII1IIiiI11II == 8050 :
 ooO ( )
elif iII1IIiiI11II == 8051 :
 Ooo0oOooo0 ( oo000o )
elif iII1IIiiI11II == 8052 :
 iiI1IIIi ( oo000o )
elif iII1IIiiI11II == 8085 :
 OO0ooo0oOO ( )
elif iII1IIiiI11II == 8086 :
 ii1 ( oo000o )
elif iII1IIiiI11II == 8087 :
 oO0oO0 ( oo000o )
elif iII1IIiiI11II == 8088 :
 i1i1IIIIi1i ( oo000o , oOOo0 )
elif iII1IIiiI11II == 9000 :
 Oo0O0O0ooO0O ( )
elif iII1IIiiI11II == 1111 :
 iI1iiII11I ( )
elif iII1IIiiI11II == 9001 :
 o00O00oO00 ( )
elif iII1IIiiI11II == 9002 :
 OO000oooo0 ( )
elif iII1IIiiI11II == 9003 :
 I1ii ( )
elif iII1IIiiI11II == 50 :
 iI1I11iiI1i ( oo000o )
elif iII1IIiiI11II == 9020 :
 O0o0Ooo ( )
elif iII1IIiiI11II == 9021 :
 ooO00O00oOO ( )
elif iII1IIiiI11II == 9022 :
 I1 ( )
elif iII1IIiiI11II == 9023 :
 IIII1ii ( )
elif iII1IIiiI11II == 9024 :
 iii1III1i ( oo000o )
elif iII1IIiiI11II == 9030 :
 OOooO0o ( oo000o )
elif iII1IIiiI11II == 9031 :
 ii1iI1iI1 ( oo000o )
elif iII1IIiiI11II == 9032 :
 o00oOOO ( oo000o )
elif iII1IIiiI11II == 9033 :
 OoOO0OOoo ( oo000o )
elif iII1IIiiI11II == 10000 : O0oo0OO0oOOOo ( )
elif iII1IIiiI11II == 10001 : o0O0OOOOoOO0 ( )
elif iII1IIiiI11II == 10002 : Iii1iiIi1II ( )
elif iII1IIiiI11II == 10003 : I1i1i1 ( )
elif iII1IIiiI11II == 10004 : O0OoooO0 ( )
elif iII1IIiiI11II == 10005 : o0ooooO0o0O ( )
elif iII1IIiiI11II == 10006 : iI1i11II1i ( oo000o )
elif iII1IIiiI11II == 10007 : I11I1i1iIII1I ( oo000o , oo00O00oO )
elif iII1IIiiI11II == 10008 : ooo0OOO ( )
elif iII1IIiiI11II == 10009 : ooo ( )
elif iII1IIiiI11II == 10010 : ooOii ( oo000o )
elif iII1IIiiI11II == 10011 : iiIi1iI1iIii ( oo000o )
elif iII1IIiiI11II == 10012 : II11iIIiiiII ( oo000o )
elif iII1IIiiI11II == 10013 : ooOoOO0OoO00o ( oo000o )
elif iII1IIiiI11II == 10014 : II1I1I1Ii ( )
elif iII1IIiiI11II == 10015 : oOIIiIi ( )
elif iII1IIiiI11II == 10016 : oo00O00Oo ( oo000o )
elif iII1IIiiI11II == 10017 : I1ii1I1iiii ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
