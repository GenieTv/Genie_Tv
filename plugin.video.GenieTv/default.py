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
i1iIIi1 = xbmcgui . Dialog ( )
ii11iIi1I = xbmc . translatePath ( 'special://home/' )
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'fanart.jpg' ) )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'icon.png' , iI111I11I1I1 , '' ) )
iIii1 = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
oOOoO0 = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
O0OoO000O0OO = "2.4.6"
iiI1IiI = xbmc . translatePath ( 'special://database' )
II = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
ooOoOoo0O = xbmc . translatePath ( 'special://thumbnails' ) ;
OooO0 = "GenieTv"
II11iiii1Ii = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
OO0o = 'http://'
Ooo = o0oOoO00o . getLocalizedString
O0o0Oo = CookieJar ( )
Oo00OOOOO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0o0Oo ) )
Oo00OOOOO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O0O = int ( sys . argv [ 1 ] )
O00o0OO = xbmc . translatePath ( o0oOoO00o . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
I11i1 = os . path . join ( O00o0OO , 'favorites' )
if os . path . exists ( I11i1 ) == True :
 iIi1ii1I1 = open ( I11i1 ) . read ( )
else : iIi1ii1I1 = [ ]
o0 = o0oOoO00o . getSetting ( 'debug' )
if os . path . exists ( II ) == False :
 os . makedirs ( II )
def I11II1i ( ) :
 IIIII ( '[COLORgreen]WIZARD[/COLOR]' , II11iiii1Ii , 4001 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]STREAMS[/COLOR]' , II11iiii1Ii , 4002 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]MUSIC[/COLOR]' , II11iiii1Ii , 4003 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 if 75 - 75: OoOoOO00 % OoOoOO00
 IIIII ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , II11iiii1Ii , 32 , iIii1 + 'builderstoolbox.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SOURCE LIST[/COLOR]' , II11iiii1Ii , 46 , iIii1 + 'sources.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]MAINTENANCE[/COLOR]' , II11iiii1Ii , 3 , iIii1 + 'MAIN6.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , iIii1 + 'ADDONS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]APK TOOL[/COLOR]' , II11iiii1Ii , 2 , iIii1 + 'APK.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , II11iiii1Ii , 39 , iIii1 + 'RSS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]ADDONS PACKS[/COLOR]' , II11iiii1Ii , 30 , iIii1 + 'ADDONP.png' , iI111I11I1I1 , '' )
 iI1 ( 'movies' , 'MAIN' )
 if 19 - 19: o0000oOoOoO0o + o0oO0
def ooo ( ) :
 IIIII ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , II11iiii1Ii , 49 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]WIPE GENIE[/COLOR]' , II11iiii1Ii , 41 , iIii1 + 'wipegenie.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]WISHES PC[/COLOR]' , II11iiii1Ii , 1 , iIii1 + 'WISHESPC.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]WISHES ANDROID[/COLOR]' , II11iiii1Ii , 44 , iIii1 + 'WISHESAN.png' , iI111I11I1I1 , '' )
 iI1 ( 'movies' , 'MAIN' )
def ii1I1i1I ( ) :
 IIIII ( '[COLORgreen]FAVOURITES[/COLOR]' , II11iiii1Ii , 10057 , iIii1 + 'FAVORITES.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SEARCH[/COLOR]' , II11iiii1Ii , 9000 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , iIii1 + 'GTVIPTV.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]POPCORN BOX[/COLOR]' , II11iiii1Ii , 7061 , iIii1 + 'popcorn.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , iIii1 + 'WATCHSERIES.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]RECENT EPISODES[/COLOR]' , II11iiii1Ii , 8081 , iIii1 + 'recent.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , II11iiii1Ii , 1023 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) ) , 1016 , iIii1 + 'reap.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]PANDORAS BOX[/COLOR]' , II11iiii1Ii , 10025 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]HEROVISION[/COLOR]' , 'http://herovision.x10host.com/vod/main.php' , 1016 , iIii1 + 'hero.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iIii1 + 'SILENTHUNTER.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]FITNESS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iIii1 + 'FITNESS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , II11iiii1Ii , 8040 , iIii1 + 'documentary.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]ANIME[/COLOR]' , II11iiii1Ii , 1001 , iIii1 + 'anime.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]M3U STREAMS[/COLOR]' , II11iiii1Ii , 8070 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , II11iiii1Ii , 3000 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 88 - 88: Ooo00oOo00o + O0 / I1IiI * oO0o0ooO0
 if 41 - 41: OoOO
 if 6 - 6: ii11ii1ii
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
 if 33 - 33: OOooOOo + OoOO0ooOOoo0O * Ooo00oOo00o - Oo / OoOO % o00O0oo
 if 21 - 21: Ooo00oOo00o * iIii1I11I1II1 % OoOO * i1IIi
 iI1 ( 'movies' , 'MAIN' )
 if 16 - 16: O0 - O0oO * iIii1I11I1II1 + oO0o0ooO0
def Ii11iII1 ( ) :
 if i1iiIII111ii == 'insert_password' :
  Oo0o0000o0o0 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
 else :
  IIIII ( '[COLORgreen]DONATORS LIST[/COLOR]' , II11iiii1Ii + '/thelist.m3u' , 7080 , iIii1 + 'GTVIPTV.png' , iI111I11I1I1 , '' )
  if 51 - 51: OoOoOO00 * Ooo00oOo00o % OOooOOo * OoOoOO00 % ii11ii1ii / o0oO0
  if 49 - 49: OOooOOo
def IIii1Ii1 ( ) :
 IIIII ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10001 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Dizzy TV[/COLOR]' , '' , 10018 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Football[/COLOR]' , '' , 10002 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Izle Films[/COLOR]' , '' , 10030 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10003 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 if 5 - 5: oO0o0ooO0 % OoOO0ooOOoo0O + o0oO0 % i11iIiiIii + OOooOOo
 if 60 - 60: Ooo00oOo00o * I1IiI - Ooo00oOo00o % OoooooooOO - o0oO0 + OOOo0
def O00Oo000ooO0 ( ) :
 IIIII ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , II11iiii1Ii , 1024 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 if 100 - 100: O0 + IIII - OoOO0ooOOoo0O + i11iIiiIii * o00O0oo
def iII ( ) :
 IIIII ( '[COLORgreen]Live Tv[/COLOR]' , II11iiii1Ii , 9021 , iIii1 + 'english.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]XXX[/COLOR]' , II11iiii1Ii , 9022 , iIii1 + 'xxx.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Hd VOD[/COLOR]' , II11iiii1Ii , 9023 , iIii1 + 'vod(1).png' , iI111I11I1I1 , '' )
 if 80 - 80: IIII . OoOO
 if 25 - 25: I1IiI . OoOoOO00 / oO0o0ooO0 . OoOO0ooOOoo0O * Ooo00oOo00o . OOOo0
def Oo0oOOo ( ) :
 IIIII ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , II11iiii1Ii , 9001 , iIii1 + 'MOVIESv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SEARCH SERIES[/COLOR]' , II11iiii1Ii , 9002 , iIii1 + 'TVSHOWSv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , iIii1 + 'ORIGINCARTOON' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , II11iiii1Ii , 9003 , iIii1 + 'livetv.png' , iI111I11I1I1 , '' )
 if 58 - 58: OoOoOO00 * OoOO0ooOOoo0O * ii11ii1ii / OoOO0ooOOoo0O
 if 75 - 75: OoOO
def I1III ( ) :
 IIIII ( '[COLORgreen]RADIO[/COLOR]' , II11iiii1Ii , 1013 , iIii1 + 'radio.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]MUSIC[/COLOR]' , II11iiii1Ii , 1030 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , II11iiii1Ii + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , II11iiii1Ii , 1111 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 if 63 - 63: OoOO0ooOOoo0O % OoOO * OoOO * Ooo00oOo00o / ii11ii1ii
 iI1 ( 'movies' , 'MAIN' )
 if 74 - 74: OoOoOO00
def oO0 ( ) :
 if 54 - 54: OoOoOO00 % I1IiI % o0000oOoOoO0o % iIii1I11I1II1 + iIii1I11I1II1 * o0oO0
 O00O0oOO00O00 ( 'DELETE CACHE' , 'url' , 14 , iIii1 + 'MAIN5.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'DELETE PACKAGES' , 'url' , 6 , iIii1 + 'MAIN4.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'FORCE REFRESH' , 'url' , 10 , iIii1 + 'MAIN3.png' , iI111I11I1I1 , 'Force Refresh All Repos' )
 if 11 - 11: IIII . ii11ii1ii
 O00O0oOO00O00 ( 'CHECK MY IP' , 'url' , 12 , iIii1 + 'MAIN2.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iIii1 + 'MAIN1.png' , iI111I11I1I1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 IIIII ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , II11iiii1Ii , 4 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]URL FIXES[/COLOR]' , II11iiii1Ii , 20 , iIii1 + 'URLFIX.png' , iI111I11I1I1 , '' )
 iI1 ( 'movies' , 'MAIN' )
 if 92 - 92: oO0o0ooO0 . O0oO
 if 31 - 31: O0oO . I1IiI / O0
def o000O0o ( ) :
 IIIII ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iIii1 + 'repos.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]NEW[/COLOR]' , II11iiii1Ii , 22 , iIii1 + 'NEW.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]IPTV[/COLOR]' , II11iiii1Ii , 23 , iIii1 + 'IPTV.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]VIDEO[/COLOR]' , II11iiii1Ii , 24 , iIii1 + 'VIDEO.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SPORTS[/COLOR]' , II11iiii1Ii , 25 , iIii1 + 'SPORTS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]KIDS[/COLOR]' , II11iiii1Ii , 26 , iIii1 + 'KIDS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]MUSIC[/COLOR]' , II11iiii1Ii , 27 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]PROGRAMS[/COLOR]' , II11iiii1Ii , 28 , iIii1 + 'PROGRAMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , iIii1 + 'XXX.png' , iI111I11I1I1 , '' )
 iI1 ( 'movies' , 'MAIN' )
 if 42 - 42: I1IiI
 if 41 - 41: Oo . o0oO0 + O0 * OOooOOo % Oo * Oo
def iIIIIi1iiIi1 ( ) :
 O00O0oOO00O00 ( 'CHECK ADVANCED XML' , II11iiii1Ii , 8 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'MUCKYS XML' , II11iiii1Ii + '/wizard/muckys.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( '0CACHE XML' , II11iiii1Ii + '/wizard/0cache.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'MIKEY1234 XML' , II11iiii1Ii + '/wizard/mikey.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'TUXENS XML' , II11iiii1Ii + '/wizard/tuxens.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'P2P RECOMMENDED XML1' , II11iiii1Ii + '/wizard/p2p1.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'P2P RECOMMENDED XML2' , II11iiii1Ii + '/wizard/p2p2.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'DELETE XML' , II11iiii1Ii , 11 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iI1 ( 'movies' , 'MAIN' )
 if 21 - 21: OOOo0 * iIii1I11I1II1
def oooooOoo0ooo ( ) :
 O00O0oOO00O00 ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 if 6 - 6: o0000oOoOoO0o - o00O0oo + iIii1I11I1II1 - O0oO - i11iIiiIii
def OO0oOO0O ( ) :
 O00O0oOO00O00 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , II11iiii1Ii + '/wizard/customftv/ftvguide-addons.zip' , 5 , iIii1 + 'FTV4.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'FTV GUIDE FIRST RUN SETTINGS' , II11iiii1Ii + '/wizard/customftv/settings.xml' , 17 , iIii1 + 'FTV3.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iIii1 + 'FTV1.png' , iI111I11I1I1 , '' )
 O00O0oOO00O00 ( 'RESET FTV DATABASE' , 'url' , 18 , iIii1 + 'FTV2.png' , iI111I11I1I1 , '' )
 if 91 - 91: O0
 if 61 - 61: OoOoOO00
 if 64 - 64: o0oO0 / I1IiI - O0 - o0000oOoOoO0o
def O0oOoOOOoOO ( ) :
 IIIII ( '[COLORgreen]SKINS[/COLOR]' , II11iiii1Ii , 33 , iIii1 + 'skinp.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , II11iiii1Ii , 34 , iIii1 + 'artp.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , ii11iIi1I , 35 , iIii1 + 'GUI.png' , iI111I11I1I1 , '' )
 iI1 ( 'movies' , 'MAIN' )
 if 38 - 38: O0oO
def Ii1 ( url ) :
 OOooOO000 = OOoOoo ( oO0000OOo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 58 - 58: Ooo00oOo00o % i11iIiiIii . oO0o0ooO0 / OoOO
def O0o ( ) :
 IIIII ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , II11iiii1Ii , 36 , iIii1 + 'GSKIN.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]HELIX SKINS[/COLOR]' , II11iiii1Ii , 37 , iIii1 + 'HSKIN.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , ii11iIi1I , 38 , iIii1 + 'ISKIN.png' , iI111I11I1I1 , '' )
 iI1 ( 'movies' , 'MAIN' )
 if 59 - 59: OOOo0 + OOOo0 + OOooOOo / iIii1I11I1II1
def O000oo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + IIi1I11I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 63 - 63: OoooooooOO - Ooo00oOo00o . OoOoOO00 / OOooOOo . I1IiI / O0
def o0OOOO00O0Oo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 90 - 90: OOooOOo % i1IIi / Ooo00oOo00o
def IIi ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 91 - 91: ii11ii1ii + OOOo0 . OoOO0ooOOoo0O * ii11ii1ii + OOOo0 * Oo
def O000OOOOOo ( url ) :
 OOooOO000 = OOoOoo ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * oO0o0ooO0 % i11iIiiIii * OOOo0
def oo000o ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + iiIi1IIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 40 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 84 - 84: o0oO0 * OoOoOO00 + Oo
def O0ooO0Oo00o ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + ooO0oOOooOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 38 - 38: O0oO
def Ooo00o0Oooo ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 2031 , iIii1 + 'APK.png' )
  if 5 - 5: OoooooooOO % I1IiI % OoOO % oO0o0ooO0
def Iiiii1I ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( oO0O0OO0O , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOOoOoO = os . path . join ( O0oO0 , name + '.apk' )
 try :
  os . remove ( OOOoOoO )
 except :
  pass
 downloader . download ( url , OOOoOoO , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 43 - 43: i11iIiiIii + Oo * OoOoOO00 * O0oO * O0
def o00oO0oo0OO ( url ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOOoOoO = os . path . join ( O0oO0 , oOO00Oo + '.mp4' )
 try :
  os . remove ( OOOoOoO )
 except :
  pass
 downloader . download ( url , OOOoOoO , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 57 - 57: O0oO % o00O0oo + OOooOOo - Oo
 if 65 - 65: o0000oOoOoO0o . I1IiI
def IiI1i ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOOoOoO = os . path . join ( O0oO0 , name )
 try :
  os . remove ( OOOoOoO )
 except :
  pass
 downloader . download ( url , OOOoOoO , i1111 )
 o0O = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0O
 print '======================================='
 extract . all ( OOOoOoO , o0O , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 90 - 90: OoOO0ooOOoo0O . OOOo0 * OOOo0
 if 7 - 7: IIII * O0oO % o00O0oo - OOooOOo
def i1i ( url ) :
 OOooOO000 = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 try :
  OOooOO000 = OOoOoo ( oOOoo00O00o + oooOOOOO + O0O00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
  for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
   IIIII ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 except : pass
 iI1 ( 'movies' , 'INFO' )
 if 97 - 97: O0 * OoooooooOO . OoooooooOO
 if 33 - 33: O0oO + oO0o0ooO0 * OoOO / iIii1I11I1II1 - OOOo0
def O0oOOO0ooOOO0OOO ( url ) :
 OOooOO000 = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 43 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 try :
  OOooOO000 = OOoOoo ( oOOoo00O00o + oooOOOOO + O0O00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
  for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
   IIIII ( oOO00Oo , url , 43 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 except : pass
 iI1 ( 'movies' , 'INFO' )
 if 63 - 63: I1IiI * oO0o0ooO0
 if 69 - 69: O0 . Ooo00oOo00o
def ii1111iII ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OOOoOoO = os . path . join ( O0oO0 , name + '.zip' )
 try :
  os . remove ( OOOoOoO )
 except :
  pass
 downloader . download ( url , OOOoOoO , i1111 )
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( OOOoOoO , iiiiI , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oooOo0OOOoo0 ( )
 if 51 - 51: Oo / I1IiI . OoOO0ooOOoo0O * OOooOOo + Ooo00oOo00o * IIII
 if 73 - 73: Ooo00oOo00o + OoooooooOO - O0 - o00O0oo - OoOoOO00
def O0Oo0oOOoooOOOOo ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOOoOoO = os . path . join ( O0oO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOOoOoO )
 except :
  pass
 downloader . download ( url , OOOoOoO , i1111 )
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( OOOoOoO , iiiiI , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 o0oO0O0o0O00O ( )
 if 80 - 80: i11iIiiIii % o0oO0 + o00O0oo % o0000oOoOoO0o - ii11ii1ii
def I1i1i1iii ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOOoOoO = os . path . join ( O0oO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOOoOoO )
 except :
  pass
 downloader . download ( url , OOOoOoO , i1111 )
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( OOOoOoO , iiiiI , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 16 - 16: o00O0oo + IIII * O0 % i1IIi . OOOo0
 if 67 - 67: OoooooooOO / OOOo0 * o00O0oo + o0000oOoOoO0o
def OooOo0ooo ( name , url , description ) :
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 OOOoOoO = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( OOOoOoO , iiiiI , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 71 - 71: O0oO + o00O0oo
 if 28 - 28: OoOO0ooOOoo0O
def o0oO0O0o0O00O ( ) :
 I11ii1IIiIi = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if I11ii1IIiIi == 0 :
  return
 elif I11ii1IIiIi == 1 :
  pass
 OoOOo0OOoO = ooO0O00Oo0o ( )
 print "Platform: " + str ( OoOOo0OOoO )
 if OoOOo0OOoO == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iIIi1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OoOOo0OOoO == 'linux' :
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
 elif OoOOo0OOoO == 'android' :
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
 elif OoOOo0OOoO == 'windows' :
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
  if 65 - 65: ii11ii1ii . o0000oOoOoO0o - O0oO * IIII / O0oO / o0oO0
def ooO0O00Oo0o ( ) :
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
  if 40 - 40: o0oO0 * IIII * i11iIiiIii
  if 57 - 57: o0oO0
  if 29 - 29: I1IiI - IIII * OoooooooOO + OoooooooOO . OoOoOO00 + OoooooooOO
def O0o000Oo ( url ) :
 i1111 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( url ) :
  for file in oOOOoo00 :
   if file . endswith ( ".xml" ) :
    i1111 . update ( 0 , "Fixing" , file , 'Please Wait' )
    iiIiIIIiiI = open ( ( os . path . join ( oooi1i1iI1iiiI , file ) ) ) . read ( )
    iiI1IIIi = iiIiIIIiiI . replace ( ii11iIi1I , 'special://home/' )
    II11IiIi11 = open ( ( os . path . join ( oooi1i1iI1iiiI , file ) ) , mode = 'w' )
    II11IiIi11 . write ( str ( iiI1IIIi ) )
    II11IiIi11 . close ( )
 o0oO0O0o0O00O ( )
 if 7 - 7: Ooo00oOo00o . o00O0oo % OoOO * o0oO0 + IIII + O0oO
def IIIIiII1i ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 iiIi1IIiIi = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , iIiIIi1 , 222 , iIii1 + 'radio.png' )
  if 25 - 25: O0oO / iIii1I11I1II1 % oO0o0ooO0
def IiiiiI1i1Iii ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.toonjet.com/' + iIiIIi1 , 8051 , iIii1 + 'classictoons.png' )
def oo00oO0o ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 in iiIi1IIiIi :
  if 'ol.gif' in I11iIiI1I1i11 :
   pass
  elif 'link_block_' in I11iIiI1I1i11 :
   pass
  elif '.png' in I11iIiI1I1i11 :
   pass
  else :
   I1I11i ( ( I11iIiI1I1i11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iIii1 + 'vod.png' )
 for url in iiii111II :
  I1I11i ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iIii1 + 'documentary.png' )
def OOoooO00o0oo0 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iIii1 + 'classictoons.png' )
  if 61 - 61: o00O0oo / ii11ii1ii % IIII + o0oO0 / O0oO . o0oO0
  if 12 - 12: i1IIi + i1IIi - ii11ii1ii * Oo % Oo - OoOoOO00
def o0OOOOooo ( ) :
 I1I11i ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , iIii1 + 'ORIGINCARTOON.png' )
 I1I11i ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , iIii1 + 'ORIGINCARTOON.png' )
 if 94 - 94: OoooooooOO + Oo / I1IiI * OoOO0ooOOoo0O
def o0OOo0o0O0O ( ) :
 I1I11i ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , iIii1 + 'ORIGINCARTOON.png' )
 I1I11i ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , iIii1 + 'ORIGINCARTOON.png' )
 if 65 - 65: i11iIiiIii
def O0O0o0oOOO ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  if '?c=' in url :
   I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , iIii1 + 'ORIGINCARTOON.png' )
   if 98 - 98: oO0o0ooO0
def OooooO0oOOOO ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , o0O00oOOoo , oOO00Oo in iiIi1IIiIi :
  if 'Genre' in url :
   I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , iIii1 + 'ORIGINCARTOON.png' )
   if 18 - 18: o00O0oo + IIII - O0
def o00O ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , o0O00oOOoo , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , o0O00oOOoo )
  if 5 - 5: O0oO
def O0I11Iiii1I ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , o0O00oOOoo , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , o0O00oOOoo )
  if 90 - 90: iIii1I11I1II1 % o0oO0
  if 73 - 73: O0 * oO0o0ooO0 + o00O0oo + o0oO0
  if 40 - 40: OoOoOO00 . I1IiI * O0oO + OoOO0ooOOoo0O + OoOO0ooOOoo0O
  if 9 - 9: o0000oOoOoO0o % OoooooooOO . OoOO % o0000oOoOoO0o
  if 32 - 32: i11iIiiIii
def iiiII ( ) :
 if 41 - 41: Oo
 IIIII ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 if 10 - 10: Oo / Oo / O0oO . O0oO
def OOoo ( ) :
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 OOoOoOo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if iIIiiiI in oOO00Oo . lower ( ) :
   if 'Dad!' in oOO00Oo :
    pass
   elif 'Family Guy' in oOO00Oo :
    pass
   elif '2 Stupid' in oOO00Oo :
    pass
   elif 'The Zelfs' in oOO00Oo :
    pass
   elif 'A Clone' in oOO00Oo :
    pass
   elif 'A.T.O.M' in oOO00Oo :
    pass
   elif 'Almost Naked' in oOO00Oo :
    pass
   elif 'Angry Kid' in oOO00Oo :
    pass
   elif 'Annoying Orange' in oOO00Oo :
    pass
   elif 'Aqua Teen' in oOO00Oo :
    pass
   elif 'Assy Mcgee' in oOO00Oo :
    pass
   elif 'Astroblast' in oOO00Oo :
    pass
   elif 'Atomic Betty' in oOO00Oo :
    pass
   elif 'Axe Cop' in oOO00Oo :
    pass
   elif 'Baby Playpen' in oOO00Oo :
    pass
   elif 'Beavis and Butt' in oOO00Oo :
    pass
   elif 'Celebrity Deathmatch' in oOO00Oo :
    pass
   elif 'Clerks The' in oOO00Oo :
    pass
   elif 'Crapston Villas' in oOO00Oo :
    pass
   elif 'Duckman:' in oOO00Oo :
    pass
   elif 'Stripperella' in oOO00Oo :
    pass
   elif 'Vixen' in oOO00Oo :
    pass
   else :
    IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10006 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 34 - 34: OOOo0 % oO0o0ooO0 + o0oO0 * iIii1I11I1II1
def Ii11 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Dad!' in oOO00Oo :
   pass
  elif 'Family Guy' in oOO00Oo :
   pass
  elif '2 Stupid' in oOO00Oo :
   pass
  elif 'The Zelfs' in oOO00Oo :
   pass
  elif 'A Clone' in oOO00Oo :
   pass
  elif 'A.T.O.M' in oOO00Oo :
   pass
  elif 'Almost Naked' in oOO00Oo :
   pass
  elif 'Angry Kid' in oOO00Oo :
   pass
  elif 'Annoying Orange' in oOO00Oo :
   pass
  elif 'Aqua Teen' in oOO00Oo :
   pass
  elif 'Assy Mcgee' in oOO00Oo :
   pass
  elif 'Astroblast' in oOO00Oo :
   pass
  elif 'Atomic Betty' in oOO00Oo :
   pass
  elif 'Axe Cop' in oOO00Oo :
   pass
  elif 'Baby Playpen' in oOO00Oo :
   pass
  elif 'Beavis and Butt' in oOO00Oo :
   pass
  elif 'Celebrity Deathmatch' in oOO00Oo :
   pass
  elif 'Clerks The' in oOO00Oo :
   pass
  elif 'Crapston Villas' in oOO00Oo :
   pass
  elif 'Duckman:' in oOO00Oo :
   pass
  elif 'Stripperella' in oOO00Oo :
   pass
  elif 'Vixen' in oOO00Oo :
   pass
  else :
   IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10006 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: ii11ii1ii + Oo / Oo % ii11ii1ii . ii11ii1ii
def O0O0Oo00 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiii111II = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 in iiii111II :
  oOoO00o = I11iIiI1I1i11
 oO00O0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOooooO0Oo )
 for url in oO00O0 :
  IIIII ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10007 , oOoO00o , iI111I11I1I1 , '' )
 iiIi1IIiIi = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 10007 , oOoO00o )
  if 36 - 36: OoOO - o00O0oo . Oo - i11iIiiIii - OoOO0ooOOoo0O * Oo
  if 76 - 76: i11iIiiIii + OOooOOo / ii11ii1ii - Ooo00oOo00o - o00O0oo + ii11ii1ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 51 - 51: iIii1I11I1II1 . o0oO0 + iIii1I11I1II1
def oOoOO ( url , IMAGE ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  print oOO00Oo + '     ' + url
  if 'easy' in url :
   Ii1i1 ( url )
   if 65 - 65: o0oO0 . OoooooooOO / ii11ii1ii . i1IIi * Ooo00oOo00o
   if 19 - 19: i11iIiiIii + OoooooooOO - Oo - o0000oOoOoO0o
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 21 - 21: O0 % IIII . OOOo0 / OoOoOO00 + IIII
def Ii1i1 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "url: '(.+?)'," ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  OOOO0O00o ( url )
  if 62 - 62: iIii1I11I1II1
  if 12 - 12: OoOO0ooOOoo0O / OOooOOo
  if 42 - 42: Oo
def II1IIiiIiI ( ) :
 if 1 - 1: oO0o0ooO0
 IIIII ( '[COLORgreen]Genres[/COLOR]' , '' , 10032 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Popular Movies[/COLOR]' , '' , 10033 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Boxsets[/COLOR]' , '' , 10034 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Search[/COLOR]' , '' , 10035 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
if 97 - 97: OoOO0ooOOoo0O + oO0o0ooO0 + O0 + i11iIiiIii
if 77 - 77: OOooOOo / OoooooooOO
if 46 - 46: OOooOOo % iIii1I11I1II1 . oO0o0ooO0 % oO0o0ooO0 + i11iIiiIii
if 72 - 72: iIii1I11I1II1 * o00O0oo % o0oO0 / Ooo00oOo00o
if 35 - 35: o0oO0 + i1IIi % ii11ii1ii % o0000oOoOoO0o + OoOO
if 17 - 17: i1IIi
if 21 - 21: Oo
if 29 - 29: o0000oOoOoO0o / OoOoOO00 / o0oO0 * OoOO0ooOOoo0O
if 10 - 10: O0oO % IIII * IIII . o0000oOoOoO0o / o00O0oo % OoOO0ooOOoo0O
if 49 - 49: Ooo00oOo00o / OoOO + O0 * OOooOOo
if 28 - 28: o0oO0 + i11iIiiIii / o0000oOoOoO0o % I1IiI % Oo - O0
if 54 - 54: i1IIi + OoOoOO00
if 83 - 83: ii11ii1ii - OOOo0 + OoOO0ooOOoo0O
if 5 - 5: o00O0oo
if 46 - 46: IIII
def ii1iIi1iIiI1i ( ) :
 IIIII ( '[COLORgreen]Action[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aksiyon' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Adventure[/COLOR]' , 'http://www.izlemeyedeger.com/tur/macera' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Animation[/COLOR]' , 'http://www.izlemeyedeger.com/tur/animasyon' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Biography[/COLOR]' , 'http://www.izlemeyedeger.com/tur/biyografi' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Comedy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/komedi' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Crime[/COLOR]' , 'http://www.izlemeyedeger.com/tur/suc' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Documentary[/COLOR]' , 'http://www.izlemeyedeger.com/tur/belgesel' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Drama[/COLOR]' , 'http://www.izlemeyedeger.com/tur/dram' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Family[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aile' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Fantasy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/fantastik' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Far East[/COLOR]' , 'http://www.izlemeyedeger.com/tur/uzak-dogu' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]History[/COLOR]' , 'http://www.izlemeyedeger.com/tur/tarih' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Horror[/COLOR]' , 'http://www.izlemeyedeger.com/tur/korku' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Musical[/COLOR]' , 'http://www.izlemeyedeger.com/tur/muzikal' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Mystery[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gizem' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Romance[/COLOR]' , 'http://www.izlemeyedeger.com/tur/romantik' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Science Fiction[/COLOR]' , 'http://www.izlemeyedeger.com/tur/bilimkurgu' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Sport[/COLOR]' , 'http://www.izlemeyedeger.com/tur/spor' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Thriller[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gerilim' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]War[/COLOR]' , 'http://www.izlemeyedeger.com/tur/savas' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Western[/COLOR]' , 'http://www.izlemeyedeger.com/tur/western' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 if 40 - 40: i1IIi % OoOO0ooOOoo0O
def ooo0o00 ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , ooO , oOO00Oo in iiIi1IIiIi :
  oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) + ' ' + ( ooO ) . replace ( '  ' , '' )
  i1iIIIi1i = I11iIiI1I1i11
  url = url
  o0o00 ( oOO00Oo , i1iIIIi1i , url )
 IIioOoO00oo0O = re . compile ( '<a href="http://www.izlemeyedeger.com/tur/(.+?)?s=(.+?)&sort=&orderby=">(.+?)</a>' ) . findall ( OOoOoOo )
 for url , IiiiI , oOO00Oo in IIioOoO00oo0O :
  IIIII ( '[COLORgold] Page ' + oOO00Oo + '[/COLOR]' , 'http://www.izlemeyedeger.com/tur/' + url + '?s=' + IiiiI + '&sort=&orderby=' , 10036 , '' , iI111I11I1I1 , '' )
  if 61 - 61: OoOO0ooOOoo0O % OoOO0ooOOoo0O * OOooOOo / OOooOOo
  if 75 - 75: IIII . o0oO0
def iII111i ( ) :
 if 87 - 87: OoOO0ooOOoo0O + o0oO0 % i11iIiiIii % O0
 OOoOoOo = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbQ==' ) )
 i1OO0oOOoo = re . compile ( '<!-- popüler filmler -->(.+?)<!-- content -->' , re . DOTALL ) . findall ( OOoOoOo )
 for oOOO00o000o in i1OO0oOOoo :
  iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img width=".+?" height=".+?" src="(.+?)" alt=""/>.+?<span class="year">(.+?)</span>.+?<span class=".+?">(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( str ( i1OO0oOOoo ) )
  for iIiIIi1 , I11iIiI1I1i11 , ooO , oOO00Oo in iiIi1IIiIi :
   oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( ooO ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   i1iIIIi1i = I11iIiI1I1i11
   iIiIIi1 = iIiIIi1
   o0o00 ( oOO00Oo , i1iIIIi1i , iIiIIi1 )
   if 9 - 9: OoOO + o0000oOoOoO0o / o0000oOoOoO0o
   if 12 - 12: OoooooooOO % OOooOOo * o0000oOoOoO0o % iIii1I11I1II1 / o00O0oo
def Ii1ii1IiIII ( ) :
 OOoOoOo = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9zZXJpLWZpbG1sZXI=' ) )
 iiIi1IIiIi = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( OOoOoOo )
 for oOO00Oo , I11iIiI1I1i11 , iIiIIi1 in iiIi1IIiIi :
  if 'IMDB' in oOO00Oo :
   pass
  else :
   IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '  ' , '' ) + '[/COLOR]' , iIiIIi1 , 10037 , I11iIiI1I1i11 , iI111I11I1I1 , '' )
 IIioOoO00oo0O = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in IIioOoO00oo0O :
  IIIII ( '[COLORgold] Page ' + oOO00Oo + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + iIiIIi1 , 10039 , '' , iI111I11I1I1 , '' )
  if 57 - 57: iIii1I11I1II1 / o0000oOoOoO0o - i1IIi
def ooOOo00O00Oo ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( OOoOoOo )
 for oOO00Oo , I11iIiI1I1i11 , url in iiIi1IIiIi :
  if 'IMDB' in oOO00Oo :
   pass
  else :
   IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '  ' , '' ) + '[/COLOR]' , url , 10037 , I11iIiI1I1i11 , iI111I11I1I1 , '' )
 IIioOoO00oo0O = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( OOoOoOo )
 for url , oOO00Oo in IIioOoO00oo0O :
  IIIII ( '[COLORgold] Page ' + oOO00Oo + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + url , 10034 , '' , iI111I11I1I1 , '' )
  if 42 - 42: O0 / OOooOOo + OoooooooOO * o0oO0 % o0oO0
  if 7 - 7: oO0o0ooO0 / ii11ii1ii / i11iIiiIii
def IIIIIo0ooOoO000oO ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , ooO , oOO00Oo in iiIi1IIiIi :
  oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '&amp;' , '&' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( ooO ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  i1iIIIi1i = I11iIiI1I1i11
  url = url
  o0o00 ( oOO00Oo , i1iIIIi1i , url )
  if 85 - 85: OOooOOo . I1IiI / o0oO0 . O0 % O0oO
def o0o00 ( name , iconimage , url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<meta itemprop="embedURL" content="(.+?)" />' ) . findall ( OOoOoOo )
 for url in iiIi1IIiIi :
  OO0ooo0oOO ( name , iconimage , url )
  if 97 - 97: OOOo0 / oO0o0ooO0
def OO0ooo0oOO ( name , iconimage , url ) :
 name = name
 I11iIiI1I1i11 = iconimage
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OOoOoOo )
 for IiiiI , Oooo0 in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + name + ' - ' + Oooo0 + '[/COLOR]' , IiiiI , 10012 , I11iIiI1I1i11 )
  if 59 - 59: OoooooooOO
def i1iiiii1 ( ) :
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = 'http://www.izlemeyedeger.com/arama?q=' + iIIiiiI
 OOoOoOo = cloudflare . source ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( OOoOoOo )
 for iIiIIi1 , I11iIiI1I1i11 , ooO , oOO00Oo in iiIi1IIiIi :
  oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( ooO ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  i1iIIIi1i = I11iIiI1I1i11
  iIiIIi1 = iIiIIi1
  o0o00 ( oOO00Oo , i1iIIIi1i , iIiIIi1 )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 83 - 83: oO0o0ooO0 . O0 / Oo / OoOO0ooOOoo0O - OoOoOO00
  if 100 - 100: Ooo00oOo00o
  if 46 - 46: I1IiI / iIii1I11I1II1 % oO0o0ooO0 . iIii1I11I1II1 * oO0o0ooO0
def IIi1ii1Ii ( ) :
 if 91 - 91: i11iIiiIii / OoooooooOO + oO0o0ooO0 - i11iIiiIii + OoOO0ooOOoo0O
 IIIII ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 if 18 - 18: OoOoOO00 / IIII
def IiII ( ) :
 OOoOoOo = OOoOoo ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoOoOo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
  if 7 - 7: OoooooooOO . IIII
def O000OOO0OOo ( ) :
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 OOoOoOo = OOoOoo ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1OO0oOOoo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , i1i1I111iIi1 , iIiiiI1IiI1I1 in i1OO0oOOoo :
  for iIIiiiI in i1i1I111iIi1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oo00O00oO000o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for iIiIIi1 , oOO00Oo in oo00O00oO000o :
    if 'tube' in iIiIIi1 :
     pass
    elif 'stage' in iIiIIi1 :
     i1II1 ( '[COLORgreen]' + i1i1I111iIi1 + '   -   ' + oOO00Oo + '[/COLOR]' , ( iIiIIi1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iIiI1I1i11 , )
    elif 'vee' in iIiIIi1 :
     pass
     if 71 - 71: ii11ii1ii - o0oO0 / I1IiI * I1IiI / i1IIi . i1IIi
def ooo000ooO0000 ( ) :
 OOoOoOo = OOoOoo ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1OO0oOOoo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , i1i1I111iIi1 , iIiiiI1IiI1I1 in i1OO0oOOoo :
  oo00O00oO000o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for iIiIIi1 , oOO00Oo in oo00O00oO000o :
   if 'tube' in iIiIIi1 :
    pass
   elif 'stage' in iIiIIi1 :
    i1II1 ( '[COLORgreen]' + i1i1I111iIi1 + '   -   ' + oOO00Oo + '[/COLOR]' , ( iIiIIi1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iIiI1I1i11 )
   elif 'vee' in iIiIIi1 :
    pass
    if 97 - 97: Oo * OOOo0 . iIii1I11I1II1
    if 16 - 16: o0oO0 % OoooooooOO - OoOO0ooOOoo0O * o00O0oo * ii11ii1ii / OoooooooOO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: o0000oOoOoO0o . O0oO * o0oO0 + i11iIiiIii * OoOO
def OO0ooo0o0O0Oooooo ( url ) :
 OOoOoOo = OOoOoo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 i11IIIiI1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( OOoOoOo )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( i11IIIiI1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in i11IIIiI1I :
  OOOO0O00o ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 69 - 69: O0
  if 85 - 85: o0oO0 / O0
  if 18 - 18: OOooOOo % O0 * ii11ii1ii
  if 62 - 62: O0oO . IIII . OoooooooOO
  if 11 - 11: OoOO0ooOOoo0O / o0000oOoOoO0o
  if 73 - 73: i1IIi / i11iIiiIii
  if 58 - 58: Oo . OoOoOO00 + OoOO - i11iIiiIii / OoOoOO00 / O0
def oOOoOo ( ) :
 if 89 - 89: OoOoOO00 + i1IIi + OoOoOO00
 IiII1II11I ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , iI111I11I1I1 , '' )
 IiII1II11I ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iI111I11I1I1 , '' )
 if 54 - 54: IIII + O0 + o0000oOoOoO0o * O0oO - OoOO0ooOOoo0O % OoOO
 iI1 ( 'movies' , 'MAIN' )
 if 13 - 13: o0oO0 / oO0o0ooO0 * Ooo00oOo00o . Ooo00oOo00o * o0oO0
def O00oO ( ) :
 IiII1II11I ( 'Search Pandoras Films' , '' , 10027 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 IiII1II11I ( 'Search Pandoras TV' , '' , 10028 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 if 40 - 40: I1IiI / IIII
 iI1 ( 'movies' , 'MAIN' )
def OOOoO000 ( ) :
 if 57 - 57: OoOoOO00
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 oOOOoo = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 15 - 15: i11iIiiIii % OOOo0 * o0000oOoOoO0o / O0oO
 for oooO0o0o0O0 in oOOOoo :
  iii11111I = Base_Pand + oooO0o0o0O0 + CAT
  OOoOoOo = OOoOoo ( iii11111I )
  iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoOo )
  for iIiIIi1 , i1iIIIi1i , ii11ii11 , iI1iIIiiii , oOO00Oo in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1i1IIiiIIi1I ( oOO00Oo , iIiIIi1 , 222 , i1iIIIi1i , iI1iIIiiii , ii11ii11 )
    if 35 - 35: IIII
    iI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 75 - 75: Oo / ii11ii1ii . IIII * OoOO0ooOOoo0O - OoOoOO00
    if 41 - 41: o00O0oo
def oOOoo0o0OOOO ( ) :
 if 26 - 26: oO0o0ooO0 % iIii1I11I1II1 + OOooOOo
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 oOOOoo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 67 - 67: OoOO + OoOoOO00 - O0 . OoOO * OoOoOO00 * o0000oOoOoO0o
 for oooO0o0o0O0 in oOOOoo :
  o00OO00O0oOO = Base_Pand + oooO0o0o0O0 + CAT
  OOoOoOo = OOoOoo ( o00OO00O0oOO )
  iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoOoOo )
  for oOO00Oo , ii11ii11 , iIiIIi1 , I11iIiI1I1i11 , iI1iIIiiii , Ii1iI111 in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    IiII1II11I ( oOO00Oo , iIiIIi1 , Ii1iI111 , I11iIiI1I1i11 , iI1iIIiiii , ii11ii11 )
    if 51 - 51: IIII * O0 / OoOoOO00 . o00O0oo % OoOO0ooOOoo0O / OOOo0
    iI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 9 - 9: OOOo0 % OOOo0 % OoOoOO00
    if 30 - 30: IIII + O0oO - IIII . IIII - OoOoOO00 + O0
def oOO0 ( ) :
 if 46 - 46: o00O0oo % I1IiI
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , ii11ii11 , iIiIIi1 , I11iIiI1I1i11 , iI1iIIiiii , Ii1iI111 in iiIi1IIiIi :
  IiII1II11I ( oOO00Oo , iIiIIi1 , Ii1iI111 , I11iIiI1I1i11 , iI1iIIiiii , ii11ii11 )
  iI1 ( 'movies' , 'MAIN' )
def ooo0o0O0o ( url ) :
 if 62 - 62: o0oO0 + i11iIiiIii + Oo / i11iIiiIii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Ii = ( '%s%s' % ( oOO , url ) )
 OOooOO000 = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooOO000 )
 for url , i1iIIIi1i , ii11ii11 , Ii1II , oOO00Oo in iiIi1IIiIi :
  i1i1IIiiIIi1I ( oOO00Oo , url , 222 , i1iIIIi1i , Ii1II , ii11ii11 )
  if 89 - 89: O0oO + OoooooooOO + O0oO * i1IIi + iIii1I11I1II1 % o0000oOoOoO0o
  iI1 ( 'movies' , 'MAIN' )
  if 59 - 59: OoOO0ooOOoo0O + i11iIiiIii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 88 - 88: i11iIiiIii - o0oO0
  if 67 - 67: OoOO0ooOOoo0O . Oo + I1IiI - OoooooooOO
def OOOoO ( url ) :
 if 14 - 14: o0000oOoOoO0o . iIii1I11I1II1 . OoooooooOO . OoOoOO00 / OOooOOo
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , ii11ii11 , url , I11iIiI1I1i11 , iI1iIIiiii , Ii1iI111 in iiIi1IIiIi :
  IiII1II11I ( oOO00Oo , url , Ii1iI111 , I11iIiI1I1i11 , iI1iIIiiii , ii11ii11 )
  if 21 - 21: i11iIiiIii / i1IIi + OOOo0 * OoOO0ooOOoo0O . O0oO
  iI1 ( 'movies' , 'MAIN' )
  if 84 - 84: O0 . o0000oOoOoO0o - OoOoOO00 . o0oO0 / OoOoOO00
  if 47 - 47: OoooooooOO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: OOOo0 % o0000oOoOoO0o
def i1i1IIiiIIi1I ( name , url , mode , iconimage , fanart , description ) :
 if 10 - 10: IIII . OoooooooOO - Ooo00oOo00o + IIII - O0
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0ooO00oO = True
 i11i1iIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1iIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11i1iIiii . setProperty ( "Fanart_Image" , fanart )
 O0ooO00oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = i11i1iIiii , isFolder = False )
 return O0ooO00oO
 if 71 - 71: ii11ii1ii % o0oO0 - OOOo0 % o0000oOoOoO0o - O0
def IiII1II11I ( name , url , mode , iconimage , fanart , description ) :
 if 67 - 67: OoOO0ooOOoo0O + Oo
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0ooO00oO = True
 i11i1iIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1iIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11i1iIiii . setProperty ( "Fanart_Image" , fanart )
 O0ooO00oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = i11i1iIiii , isFolder = True )
 return O0ooO00oO
if 84 - 84: O0 * OoooooooOO - IIII * IIII
if 8 - 8: o0oO0 / i1IIi . OoOO
if 41 - 41: oO0o0ooO0 + Ooo00oOo00o
if 86 - 86: I1IiI . iIii1I11I1II1 - Ooo00oOo00o
if 56 - 56: O0
if 61 - 61: OOooOOo / OoOO0ooOOoo0O / Oo * O0
if 23 - 23: OoOO - OoOO0ooOOoo0O + o0000oOoOoO0o
if 12 - 12: OOOo0 / o0oO0 % OOooOOo / i11iIiiIii % OoooooooOO
if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo * o00O0oo + o0000oOoOoO0o
if 11 - 11: oO0o0ooO0 * o00O0oo - I1IiI
if 66 - 66: I1IiI . i11iIiiIii - oO0o0ooO0 * OOooOOo + OoooooooOO * ii11ii1ii
if 74 - 74: Oo
if 61 - 61: Oo - O0oO * OoOoOO00 % o0oO0 * iIii1I11I1II1 + Ooo00oOo00o
if 71 - 71: o0000oOoOoO0o / o0000oOoOoO0o * OoOO * OoOO / OoOoOO00
if 35 - 35: OoOO0ooOOoo0O * OOooOOo * OOOo0 % Oo . I1IiI
def O00o00O ( string ) :
 if o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 3 - 3: OoOO0ooOOoo0O
def Iii ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 O0o0o = [ ]
 try :
  if 87 - 87: o0000oOoOoO0o * i1IIi - o00O0oo % OoOO0ooOOoo0O / O0oO
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  O00o00O ( 'Making Favorites File' )
  O0o0o . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iiIiIIIiiI = open ( I11i1 , "w" )
  iiIiIIIiiI . write ( json . dumps ( O0o0o ) )
  iiIiIIIiiI . close ( )
 else :
  O00o00O ( 'Appending Favorites' )
  iiIiIIIiiI = open ( I11i1 ) . read ( )
  IiIiiI11111I1 = json . loads ( iiIiIIIiiI )
  IiIiiI11111I1 . append ( ( name , url , iconimage , fanart , mode ) )
  iiI1IIIi = open ( I11i1 , "w" )
  iiI1IIIi . write ( json . dumps ( IiIiiI11111I1 ) )
  iiI1IIIi . close ( )
  if 55 - 55: o0oO0 % OoooooooOO / OoooooooOO % OoooooooOO
  if 52 - 52: ii11ii1ii + ii11ii1ii . OoOoOO00
def IiiIIIII1iii ( ) :
 IIiiii = json . loads ( open ( I11i1 ) . read ( ) )
 iI111i1I1II = len ( IIiiii )
 for O00OO in IIiiii :
  oOO00Oo = O00OO [ 0 ]
  iIiIIi1 = O00OO [ 1 ]
  i1iIIIi1i = O00OO [ 2 ]
  try :
   II1Ii1iI1i1 = O00OO [ 3 ]
   if II1Ii1iI1i1 == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    II1Ii1iI1i1 = i1iIIIi1i
   else :
    II1Ii1iI1i1 = iI1iIIiiii
  try : o0OoO000O = O00OO [ 5 ]
  except : o0OoO000O = None
  try : OOo = O00OO [ 6 ]
  except : OOo = None
  if 9 - 9: o00O0oo
  if O00OO [ 4 ] == 0 :
   IIIII ( oOO00Oo , iIiIIi1 , '' , i1iIIIi1i , iI1iIIiiii , '' , 'fav' )
  else :
   IIIII ( oOO00Oo , iIiIIi1 , O00OO [ 4 ] , i1iIIIi1i , iI1iIIiiii , '' , 'fav' )
   if 56 - 56: OoOoOO00 / OoOO + i11iIiiIii + OoOO0ooOOoo0O
def O0O0o0o0o ( name ) :
 IiIiiI11111I1 = json . loads ( open ( I11i1 ) . read ( ) )
 for IIIIIiI in range ( len ( IiIiiI11111I1 ) ) :
  if IiIiiI11111I1 [ IIIIIiI ] [ 0 ] == name :
   del IiIiiI11111I1 [ IIIIIiI ]
   iiI1IIIi = open ( I11i1 , "w" )
   iiI1IIIi . write ( json . dumps ( IiIiiI11111I1 ) )
   iiI1IIIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 80 - 80: iIii1I11I1II1 * O0oO % o0000oOoOoO0o % Oo
 if 95 - 95: iIii1I11I1II1 - ii11ii1ii . O0oO - OOOo0
 if 75 - 75: Ooo00oOo00o + OOooOOo - i1IIi . OoooooooOO * o00O0oo / IIII
def OOOooo0OooOoO ( ) :
 if 91 - 91: OoOO + OOOo0
 IIIII ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 if 59 - 59: OOOo0 + i11iIiiIii + i1IIi / o0000oOoOoO0o
def I11iIiI1 ( ) :
 if 86 - 86: OOooOOo
 OOooooO0Oo = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIi1IIiIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , Ii in iiIi1IIiIi :
  IIIII ( oOO00Oo + '  -  ' + ( Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIiIIi1 , 10023 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 2 - 2: ii11ii1ii . ii11ii1ii + ii11ii1ii * OOooOOo
  if 100 - 100: Oo % o00O0oo / o0000oOoOoO0o
  if 30 - 30: Oo - OoOO0ooOOoo0O - oO0o0ooO0
def OOO ( ) :
 if 18 - 18: o0oO0 - I1IiI % i1IIi + O0 + i11iIiiIii + i1IIi
 IIIII ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 if 91 - 91: I1IiI + o0oO0 . OOOo0
def O0oOoOOO0OO ( url ) :
 O0OOOO = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 OOoOoOo = cloudflare . source ( O0OOOO )
 iiIi1IIiIi = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 10022 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 14 - 14: O0
  if 65 - 65: Oo / o0000oOoOoO0o
  if 12 - 12: o0000oOoOoO0o % I1IiI
  if 48 - 48: oO0o0ooO0 . i11iIiiIii
def IIioo0OO ( ) :
 if 2 - 2: OoOoOO00 - Ooo00oOo00o . IIII * oO0o0ooO0 / OoOO
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 OOoOoOo = cloudflare . source ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if iIIiiiI in oOO00Oo . lower ( ) :
   IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10022 , iIii1 + 'dtv.png' )
   if 80 - 80: OoOO0ooOOoo0O / o0000oOoOoO0o / I1IiI + i1IIi - Oo
   if 11 - 11: OOooOOo * Ooo00oOo00o
   if 15 - 15: I1IiI
def oOoOoO000OO ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( OOoOoOo )
 for IiiiI , ii11II11 , oOo , oOO00Oo in iiIi1IIiIi :
  oOo00OooO0oO = ( oOo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1IIi = ( ii11II11 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0OOOo = 'Season ' + I1IIi + 'Episode ' + oOo00OooO0oO + oOO00Oo
  i11I1I1iiI ( O0OOOo , IiiiI )
  if 34 - 34: o0000oOoOoO0o % o0oO0 . O0 . iIii1I11I1II1
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 93 - 93: i1IIi . i11iIiiIii . Oo
  if 99 - 99: o0000oOoOoO0o - O0oO - OoOO % Ooo00oOo00o
def i11I1I1iiI ( name , url ) :
 IiiiI = url
 IiiIIiiiiii = name
 OOOO0o = cloudflare . source ( IiiiI )
 iiii111II = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OOOO0o )
 for i11IIIiI1I , Oooo0 in iiii111II :
  i1II1 ( '[COLORgreen]' + IiiIIiiiiii + Oooo0 + '[/COLOR]' , i11IIIiI1I , 10012 , iIii1 + 'dtv.png' )
  if 10 - 10: O0oO % OOOo0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 97 - 97: OoooooooOO - O0oO
 if 58 - 58: iIii1I11I1II1 + O0
def I111I11I111 ( ) :
 if 46 - 46: i11iIiiIii - O0 . OoOO
 if 100 - 100: OOOo0 / OOooOOo * oO0o0ooO0 . O0 / OoOO0ooOOoo0O
 if 83 - 83: O0oO
 if 48 - 48: OoOoOO00 * OoOO0ooOOoo0O * O0oO
 if 50 - 50: IIII % i1IIi
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
 IIIII ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 IIIII ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 IIIII ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 if 45 - 45: ii11ii1ii + OoOoOO00 * i11iIiiIii
 if 13 - 13: OoooooooOO * OoOO - o00O0oo / OoOO0ooOOoo0O + o0000oOoOoO0o + IIII
def iii1III1i ( url ) :
 OOoOoOo = OOoOoo ( url )
 oOOO00o000o = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( OOoOoOo )
 iiIi1IIiIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( oOOO00o000o ) )
 for url , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 17 - 17: OoOoOO00 / OoOoOO00
def o0OO0Oo ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 3 - 3: O0oO - O0 % iIii1I11I1II1 / IIII . OOooOOo
def iiiiI1iiiIi ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OOoOoOo )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 84 - 84: OoOO0ooOOoo0O
  if 87 - 87: o0oO0 + OOooOOo
def i1iIIIIIIiII1 ( ) :
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iii11 = 'http://www.watchseries.li/search/' + iIIiiiI . replace ( ' ' , '%20' )
 OOoOoOo = OOoOoo ( iii11 )
 iiIi1IIiIi = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'watch online' in oOO00Oo :
   pass
  else :
   print iIiIIi1
   IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.watchseries.li' + iIiIIi1 , 10044 , I11iIiI1I1i11 , '' , '' )
   if 35 - 35: O0oO . I1IiI * i11iIiiIii
   xbmcplugin . setContent ( O0O , 'movies' )
   if 44 - 44: i11iIiiIii / Oo
def Ii1IIi ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , url , oOO00Oo , oOo , ii11ii11 in iiIi1IIiIi :
  i111i11I1ii = ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oOo ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  IIIII ( '[COLORgreen]' + i111i11I1ii + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , I11iIiI1I1i11 , '' , ii11ii11 )
  if 64 - 64: OoOO / i11iIiiIii / OOooOOo . OoooooooOO
def i1iiIIi11I ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OOoOoOo )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  i111i11I1ii = ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  IIIII ( '[COLORgreen]' + i111i11I1ii + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 80 - 80: o0oO0 * O0
def oo000o0 ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( OOoOoOo )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , I11iIiI1I1i11 , '' , '' )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 25 - 25: o0000oOoOoO0o + I1IiI . OOooOOo % I1IiI * OoOO0ooOOoo0O
def ii1IiIi11 ( url ) :
 OOoOoOo = OOoOoo ( url )
 oOOO00o000o = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for ii11II11 , i1OO0oOOoo in oOOO00o000o :
  iiIi1IIiIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( i1OO0oOOoo ) )
  for url , oOO00Oo in iiIi1IIiIi :
   i111i11I1ii = ( ii11II11 ) . replace ( '  ' , '' ) + ' ' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   IIIII ( '[COLORgreen]' + i111i11I1ii + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 22 - 22: OoOO
  if 33 - 33: iIii1I11I1II1 / o00O0oo
class iIIIiiiI11I ( ) :
 if 6 - 6: o00O0oo % i1IIi . o00O0oo * o00O0oo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 81 - 81: OoOO0ooOOoo0O / iIii1I11I1II1 + IIII
  i111i11I1ii = name
  self . Get_Sources ( iIiIIi1 , i111i11I1ii )
  if 49 - 49: OoOO0ooOOoo0O / OoooooooOO / OOOo0
  if 74 - 74: O0oO % ii11ii1ii
 def Get_Sources ( self , URL , season_name ) :
  i1111 = xbmcgui . DialogProgress ( )
  OOoOoOo = OOoOoo ( URL )
  iiIi1IIiIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( OOoOoOo )
  for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
   URL = 'http://www.watchseries.li/link/' + iIiIIi1
   self . Get_site_link ( URL , season_name )
   if 7 - 7: OoOoOO00
 def Get_site_link ( self , url , season_name ) :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( OOoOoOo )
  iiii111II = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( OOoOoOo )
  oO00O0 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( OOoOoOo )
  for url in iiIi1IIiIi :
   self . main ( url , season_name )
  for url in iiii111II :
   self . main ( url , season_name )
  for url in oO00O0 :
   self . main ( url , season_name )
   if 27 - 27: OoOO . OoooooooOO + i11iIiiIii
 def main ( self , url , season_name ) :
  i1111 . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   O0OO = 'DACLIPS'
   if O0OO in iIIIiiiI11I . source_list :
    pass
   else :
    self . daclips ( url , season_name , O0OO )
    i1111 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    O0OO = 'FILEHOOT'
    if O0OO in iIIIiiiI11I . source_list :
     pass
    else :
     i1111 . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , O0OO )
   else :
    if 'thevideo.me' in url :
     O0OO = 'THEVIDEO'
     if O0OO in iIIIiiiI11I . source_list :
      pass
     else :
      self . thevideo ( url , season_name , O0OO )
      i1111 . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      O0OO = 'ALLMYVIDEOS'
      if O0OO in iIIIiiiI11I . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , O0OO )
       i1111 . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       O0OO = 'VIDSPOT'
       if O0OO in iIIIiiiI11I . source_list :
        pass
       else :
        self . vidspot ( url , season_name , O0OO )
        i1111 . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        O0OO = 'VODLOCKER'
        if O0OO in iIIIiiiI11I . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , O0OO )
         i1111 . update ( 0 , "" , "Getting Vodlocker Links" )
         if 39 - 39: ii11ii1ii + OOOo0 - iIii1I11I1II1 - OOooOOo
         if 7 - 7: IIII . I1IiI / ii11ii1ii . OoOO0ooOOoo0O * o0000oOoOoO0o - OoOoOO00
 def allmyvid ( self , url , season_name , source_name ) :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OOoOoOo )
  for I1 , oOO00Oo in iiIi1IIiIi :
   self . Printer ( I1 , season_name , source_name )
   if 21 - 21: O0 * O0 % ii11ii1ii
 def vidspot ( self , url , season_name , source_name ) :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( OOoOoOo )
  for I1 , oOO00Oo in iiIi1IIiIi :
   self . Printer ( I1 , season_name , source_name )
   if 94 - 94: o0000oOoOoO0o + OoOoOO00 % i11iIiiIii
 def thevideo ( self , url , season_name , source_name ) :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( OOoOoOo )
  for I1 in iiIi1IIiIi :
   self . Printer ( I1 , season_name , source_name )
   if 8 - 8: o0oO0 * O0
 def vodlocker ( self , url , season_name , source_name ) :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OOoOoOo )
  for I1 in iiIi1IIiIi :
   self . Printer ( I1 , season_name , source_name )
   if 73 - 73: OOooOOo / OoOO / o0000oOoOoO0o / Ooo00oOo00o
 def daclips ( self , url , season_name , source_name ) :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( OOoOoOo )
  for I1 in iiIi1IIiIi :
   self . Printer ( I1 , season_name , source_name )
   if 11 - 11: I1IiI + IIII - OoooooooOO / Ooo00oOo00o
 def filehoot ( self , url , season_name , source_name ) :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OOoOoOo )
  for I1 in iiIi1IIiIi :
   self . Printer ( I1 , season_name , source_name )
   if 34 - 34: o0oO0
 def Printer ( self , Link , season_name , source_name ) :
  if 45 - 45: o0oO0 / Oo / o00O0oo
  if Link in iIIIiiiI11I . List :
   pass
  elif source_name in iIIIiiiI11I . source_list :
   pass
  else :
   i1II1 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , iIii1 + 'WATCHSERIES.png' )
   i1111 . update ( 100 , "" , "Got Source" )
   iIIIiiiI11I . List . append ( Link )
   iIIIiiiI11I . source_list . append ( source_name )
   if 44 - 44: ii11ii1ii - o00O0oo / OoOoOO00 * Ooo00oOo00o * Oo
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
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
def I1IiIii11I ( ) :
 IIIII ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 if 29 - 29: OOooOOo
def oo0iIiI ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iiIi1IIiIi = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIiIIi1 , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I11iIiI1I1i11 , iI111I11I1I1 , '' )
  if 81 - 81: I1IiI % o00O0oo
def oo0i1iIIi1II1iiI ( url ) :
 OOoOoOo = OOoOoo ( url )
 oOOO00o000o = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( OOoOoOo )
 for oOOO00o000o in oOOO00o000o :
  III1Ii1i1I1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( oOOO00o000o ) )
  for O0O00OooO in III1Ii1i1I1 :
   O0O00OooO = O0O00OooO
  I1IiI1iI11 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( oOOO00o000o ) )
  for iIi , I11iIiI1I1i11 , time , iiO0O0o0oO0O00 in I1IiI1iI11 :
   o0O0oO0 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iiO0O0o0oO0O00 )
   IIIII ( '[COLORgreen]' + O0O00OooO + ' - ' + iIi + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I11iIiI1I1i11 , iI111I11I1I1 , ( str ( o0O0oO0 ) ) )
   if 77 - 77: O0 . o00O0oo
 iI1 ( 'tvshows' , 'Media Info 3' )
 if 39 - 39: o0oO0 . OoOoOO00
def iIiIi1iI11iiI ( ) :
 if 26 - 26: iIii1I11I1II1 * O0oO - OoOO0ooOOoo0O
 IIIII ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iIii1 + 'fanart.jpg' , '' )
 IIIII ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iIii1 + 'fanart.jpg' , '' )
 if 27 - 27: ii11ii1ii * O0oO - Ooo00oOo00o + o00O0oo * o00O0oo
def o0OO0O0OO0oO0 ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  iIiiIi11IIi = oOO00Oo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  i1II1 ( '[COLORgreen]' + iIiiIi11IIi + '[/COLOR]' , url , 10013 , I11iIiI1I1i11 )
  if 64 - 64: OoooooooOO . ii11ii1ii % O0 + OOOo0 - OOooOOo
def ooo0oo00O00oO ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( OOoOoOo )
 for i11IIIiI1I in iiIi1IIiIi :
  oOOooooo0OoO0 = ( i11IIIiI1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOO0O00o ( 'http:' + oOOooooo0OoO0 )
  if 11 - 11: i1IIi % Ooo00oOo00o % oO0o0ooO0
  if 99 - 99: o0oO0 / iIii1I11I1II1 - o00O0oo * ii11ii1ii % OOOo0
def i1II1i ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 8046 , iIii1 + 'documentary.png' )
def I1iIiiiI1 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( 'NEXT PAGE' , url , 8046 , iIii1 + 'documentary.png' )
  if 42 - 42: OoOO0ooOOoo0O % OoOO / Ooo00oOo00o - OoOO * i11iIiiIii
def iI1IiiiIiI1Ii ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  yt . PlayVideo ( url )
  if 78 - 78: OoooooooOO / OoOO0ooOOoo0O % I1IiI * OoooooooOO
def ooOO00o00 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 8041 , iIii1 + 'documentary.png' )
def Ii11Iii ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo ) . replace ( '&#039;s' , '' ) , url , 8042 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( 'NEXT PAGE' , url , 8041 , iIii1 + 'documentary.png' )
  if 68 - 68: OOOo0 % O0
  if 74 - 74: i1IIi + I1IiI + iIii1I11I1II1 * I1IiI * iIii1I11I1II1 + o0000oOoOoO0o
def Oo0o ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , I11iIiI1I1i11 , url , o0O00oOOoo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , I11iIiI1I1i11 )
 for url in iiii111II :
  IiI1I1I ( ( url ) . replace ( '//' , 'http://' ) )
  if 62 - 62: IIII * O0
def IiI1I1I ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIii1 + 'documentary.png' )
  if 86 - 86: ii11ii1ii * OoOoOO00 * o0000oOoOoO0o
def oO0Oo ( ) :
 OOoOoOo = OO ( 'http://www.stream2watch.co/live-tv' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( OOoOoOo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , ooO0oOO00OoOo in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo + '[COLORgreen]' + ooO0oOO00OoOo + '[/COLOR]' ) , iIiIIi1 , 8086 , I11iIiI1I1i11 )
  if 74 - 74: OoOoOO00 . O0 - OOOo0 + IIII % i11iIiiIii % I1IiI
def O0OOO0 ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 8087 , I11iIiI1I1i11 )
  if 8 - 8: i11iIiiIii / OoOoOO00 + OOooOOo * o00O0oo % IIII . o0000oOoOoO0o
def I1iIIIiIi1 ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  IiI1 ( url , oOO00Oo )
  if 59 - 59: o0000oOoOoO0o / Oo / OoOO0ooOOoo0O / O0 / I1IiI + OOooOOo
def IiI1 ( url , name ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( OOoOoOo )
 for url in iiIi1IIiIi :
  print url
  i1II1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 13 - 13: OOooOOo % OoOO / O0oO % O0oO % O0
def o0Ii1 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 iiIi1IIiIi = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , time , IIi1IiII , iIi , I1IiI1iI11 , iIiIIi1 in iiIi1IIiIi :
  I1I11i ( ( time + '[COLORgreen]' + I1IiI1iI11 + '[/COLOR]' + iIi ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , iIiIIi1 , 8061 , I11iIiI1I1i11 )
def o0IIIIiI11I ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , iIii1 + 'documentary.png' )
  if 31 - 31: o00O0oo
def i11iIIi ( ) :
 OOoOoOo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iIiIIi1 , 8071 , iIii1 + 'streams.png' )
def O000O ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoOoOo )
 for oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , iIii1 + 'streams.png' )
def iiiIii ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( ) , 222 , I11iIiI1I1i11 )
  if 35 - 35: OoooooooOO - O0oO / Ooo00oOo00o
def iii11i1 ( ) :
 OOoOoOo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy54bnh4LmNvbS8=' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a><br>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 8091 , iIii1 + 'streams.png' )
def i1IiI1I111iIi ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?src="(.+?)".+?title="(.+?)">' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 8092 , I11iIiI1I1i11 )
def IiiIIi1 ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( 'src=&quot;(.+?)&quot;' ) . findall ( OOoOoOo )
 for url in iiIi1IIiIi :
  iI1iIiiI ( url )
  if 95 - 95: iIii1I11I1II1 + Oo * OoOoOO00 + o0oO0 + O0 * o0000oOoOoO0o
def Ii11I1iIiiI ( url ) :
 O0o0OO00 = urllib2 . Request ( url )
 O0o0OO00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iIi11i = ''
 OOooOO000 = ''
 try :
  iIi11i = urllib2 . urlopen ( O0o0OO00 )
  OOooOO000 = iIi11i . read ( )
  iIi11i . close ( )
 except : pass
 if OOooOO000 != '' :
  return OOooOO000
 else :
  OOooOO000 = 'Failed'
  return OOooOO000
  if 56 - 56: i11iIiiIii . o0oO0 / oO0o0ooO0
def III1iii1i1II ( ) :
 O0oOO0o = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 IiiiI = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 iiiiI1IiI1I1 = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iI111i11iI1 = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 III1ii = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 iI1III1iIi11 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i11I1I = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iIIiiiI
 oo0ooooo00o = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 if 78 - 78: iIii1I11I1II1 . OOooOOo % iIii1I11I1II1 . O0 / OoOO0ooOOoo0O
 OOoOoOo = Ii11I1iIiiI ( iIiIIi1 )
 OOOO0o = Ii11I1iIiiI ( IiiiI )
 Oo0oOo000OoO0 = Ii11I1iIiiI ( iiiiI1IiI1I1 )
 IIii1I1i = Ii11I1iIiiI ( iI111i11iI1 )
 IIII1iIIii = Ii11I1iIiiI ( III1ii )
 IiiOooooOo0 = Ii11I1iIiiI ( i11I1I )
 I1ii1 = OOoOoo ( oo0ooooo00o )
 if 48 - 48: o0oO0 / iIii1I11I1II1 + OoOO0ooOOoo0O + iIii1I11I1II1 . Ooo00oOo00o
 if OOoOoOo != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOoOoOo )
  for o0o0OO0o00o0O , oOO00Oo in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIiIIi1 + o0o0OO0o00o0O ) , 222 , '' )
 if OOOO0o != 'Failed' :
  iiii111II = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOOO0o )
  for o0o0OO0o00o0O , oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiiiI + o0o0OO0o00o0O ) , 222 , '' )
 if Oo0oOo000OoO0 != 'Failed' :
  oO00O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0oOo000OoO0 )
  for o0o0OO0o00o0O , oOO00Oo in oO00O0 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiiiI1IiI1I1 + o0o0OO0o00o0O ) , 222 , '' )
 if IIii1I1i != 'Failed' :
  IIIIIIi1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIii1I1i )
  for o0o0OO0o00o0O , oOO00Oo in IIIIIIi1i :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iI111i11iI1 + o0o0OO0o00o0O ) , 222 , '' )
 if IIII1iIIii != 'Failed' :
  iiiii11I1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIII1iIIii )
  for o0o0OO0o00o0O , I11iIiI1I1i11 , oOO00Oo in iiiii11I1 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , o0o0OO0o00o0O , 1006 , 'img' )
    if 16 - 16: O0 . o00O0oo % i1IIi % OoOO0ooOOoo0O
    iI1 ( 'tvshows' , 'Media Info 3' )
 if IiiOooooOo0 != 'Failed' :
  i1I1iI = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IiiOooooOo0 )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in i1I1iI :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iIiIIi1 , 7067 , I11iIiI1I1i11 )
    if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
    iI1 ( 'tvshows' , 'Media Info 3' )
 if I1ii1 != 'Failed' :
  oOo0Oo0O0O = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( I1ii1 )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in oOo0Oo0O0O :
   i1II1 ( '[COLORgreen]' + oOO00Oo + '- Source 7[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
 oOOOoo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 48 - 48: Oo - o0oO0 + Oo - OOOo0 * i11iIiiIii . oO0o0ooO0
 if 35 - 35: IIII . O0 + Oo + OoOO0ooOOoo0O + i1IIi
 for oooO0o0o0O0 in oOOOoo :
  iii11111I = O0oOO0o + oooO0o0o0O0
  OooOooO0O0o0 = Ii11I1iIiiI ( iii11111I )
  if IIII1iIIii != 'Failed' :
   OOO0o0 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OooOooO0O0o0 )
   for o0o0OO0o00o0O , oOO00Oo in OOO0o0 :
    if iIIiiiI in oOO00Oo . lower ( ) :
     i1II1 ( ( '[COLORgreen]' + oOO00Oo + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0oOO0o + oooO0o0o0O0 + o0o0OO0o00o0O ) , 222 , '' )
     if 34 - 34: OOOo0 % Oo - I1IiI + oO0o0ooO0
     iI1 ( 'tvshows' , 'Media Info 3' )
     if 79 - 79: OoOoOO00 - o0oO0 . i1IIi + O0 % O0 * OOOo0
     if 7 - 7: i1IIi + OoOO0ooOOoo0O % oO0o0ooO0 / OOooOOo + i1IIi
def I1ii11I ( ) :
 if 22 - 22: I1IiI % OOooOOo * o00O0oo - ii11ii1ii + OOooOOo - Oo
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 IiiiI = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 iiiiI1IiI1I1 = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iI111i11iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 III1ii = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 iI1III1iIi11 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 oo0ooooo00o = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 iiIi1iiI1I = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + iIIiiiI . replace ( ' ' , '%20' )
 if 26 - 26: iIii1I11I1II1 + i1IIi / I1IiI % ii11ii1ii
 OOoOoOo = Ii11I1iIiiI ( iIiIIi1 )
 OOOO0o = Ii11I1iIiiI ( IiiiI )
 Oo0oOo000OoO0 = Ii11I1iIiiI ( iiiiI1IiI1I1 )
 IIii1I1i = Ii11I1iIiiI ( iI111i11iI1 )
 IIII1iIIii = cloudflare . source ( III1ii )
 OooOooO0O0o0 = Ii11I1iIiiI ( iI1III1iIi11 )
 I1ii1 = OOoOoo ( oo0ooooo00o )
 IiiIi11Ii1iI1 = OOoOoo ( iiIi1iiI1I )
 if OOoOoOo != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoOo )
  for oOO00Oo in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIIi1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 91 - 91: OoOO0ooOOoo0O + O0oO . o0000oOoOoO0o
    iI1 ( 'tvshows' , 'Media Info 3' )
 if OOOO0o != 'Failed' :
  iiii111II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOOO0o )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiiI + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 15 - 15: o0000oOoOoO0o
    iI1 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOo000OoO0 != 'Failed' :
  oO00O0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oOo000OoO0 )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiiiI1IiI1I1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 94 - 94: O0oO % OoOoOO00 * i1IIi * iIii1I11I1II1
    iI1 ( 'tvshows' , 'Media Info 3' )
 if IIii1I1i != 'Failed' :
  IIIIIIi1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIii1I1i )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI111i11iI1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 81 - 81: Oo - o0000oOoOoO0o
    iI1 ( 'tvshows' , 'Media Info 3' )
 if IIII1iIIii != 'Failed' :
  iiiii11I1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIII1iIIii )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiiii11I1 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( '[COLORgreen]' + oOO00Oo + ' - Source - Dizi[/COLOR]' , iIiIIi1 , 8062 , I11iIiI1I1i11 )
    if 24 - 24: OoooooooOO . Ooo00oOo00o * OoOoOO00
    iI1 ( 'tvshows' , 'Media Info 3' )
 if OooOooO0O0o0 != 'Failed' :
  OOO0o0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OooOooO0O0o0 )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in OOO0o0 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- Source Scooby[/COLOR]' ) , iIiIIi1 , 222 , 'img' )
    if 59 - 59: O0oO + Ooo00oOo00o / OoOO0ooOOoo0O
    iI1 ( 'tvshows' , 'Media Info 3' )
 if I1ii1 != 'Failed' :
  oOo0Oo0O0O = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( I1ii1 )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in oOo0Oo0O0O :
   i1II1 ( '[COLORgreen]' + oOO00Oo + ' - Source DiZzY[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
 if IiiIi11Ii1iI1 != 'Failed' :
  OO00o0O0O000o = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IiiIi11Ii1iI1 )
  for I11iIiI1I1i11 , iIiIIi1 , oOO00Oo in OO00o0O0O000o :
   if 'watch online' in oOO00Oo :
    pass
   else :
    IIIII ( '[COLORgreen]' + oOO00Oo + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + iIiIIi1 , 10044 , I11iIiI1I1i11 , '' , '' )
    if 56 - 56: Oo * oO0o0ooO0
    xbmcplugin . setContent ( O0O , 'movies' )
    if 13 - 13: Oo * Oo * OoOoOO00 * oO0o0ooO0 . i1IIi / IIII
def O0Oo000OO000 ( ) :
 if 83 - 83: OOooOOo % OoOO + o0000oOoOoO0o % i11iIiiIii + O0
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOoOoOo = OOoOoo ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOoOoOo )
 for oOO00Oo , I11iIiI1I1i11 , OoOOoooO000 in iiIi1IIiIi :
  OoO0o000oOo = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  if iIIiiiI in oOO00Oo . lower ( ) :
   I1I11i ( oOO00Oo , '' , 7022 , OoO0o000oOo )
   if 88 - 88: i1IIi * O0oO * OoOO - o0oO0 * o0000oOoOoO0o / OoooooooOO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: O0 / O0oO + iIii1I11I1II1
 if 72 - 72: I1IiI * iIii1I11I1II1 % o0000oOoOoO0o
def IiIi1I1i1II ( url ) :
 iI1I1 = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI1I1 )
 for url , ii11II11 , Ii , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( ii11II11 ) . replace ( 'Sezon' , ' Season ' ) + ( Ii ) . replace ( 'Bölüm' , ' Episode ' ) + oOO00Oo , url , 8063 , '' )
  if 46 - 46: iIii1I11I1II1
  if 33 - 33: o0000oOoOoO0o % o0000oOoOoO0o % O0 / OOOo0 . i1IIi
  if 91 - 91: o0oO0 * o0000oOoOoO0o - OoOoOO00 . OOOo0 - Oo + o0oO0
  if 56 - 56: OOooOOo / IIII * OOOo0 . OOooOOo
def iiO0o0O0oo0o ( url ) :
 iI1I1 = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iI1I1 )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , '' )
  if 100 - 100: IIII . o00O0oo - iIii1I11I1II1 . i11iIiiIii / OoOoOO00
  if 71 - 71: O0oO * Oo . o0000oOoOoO0o
  if 49 - 49: IIII * O0 . IIII
  if 19 - 19: OoOoOO00 - IIII
def OOOOo000o00OO ( ) :
 if 96 - 96: O0 . OoOO0ooOOoo0O % o0oO0 + i11iIiiIii - OoOO0ooOOoo0O * o0oO0
 iI1I1 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIi1IIiIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI1I1 )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , Ii in iiIi1IIiIi :
  I1I11i ( oOO00Oo + '  -  ' + ( Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIiIIi1 , 8063 , I11iIiI1I1i11 )
  if 33 - 33: o0oO0 % i1IIi - OoOO . O0 / O0
def oo00o0 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 8002 , I11iIiI1I1i11 )
def I1IiII1iI1 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , time , url , oOO00Oo , o0O00oOOoo in iiIi1IIiIi :
  IIIII ( '%s %s' % ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , time ) , url , 1015 , I11iIiI1I1i11 , o0O00oOOoo )
  if 52 - 52: I1IiI * Ooo00oOo00o - o00O0oo
def OOoOOo0 ( ) :
 if 16 - 16: OOooOOo - Ooo00oOo00o / O0oO
 I1I11i ( 'Coronation Street' , '' , 8001 , '' )
 I1I11i ( 'Eastenders' , '' , 8002 , '' )
 I1I11i ( 'Emmerdale' , '' , 8003 , '' )
 I1I11i ( 'Hollyoaks' , '' , 8004 , '' )
 I1I11i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 48 - 48: iIii1I11I1II1
 if 91 - 91: OoOoOO00 - O0 . iIii1I11I1II1 . O0 + ii11ii1ii - OoOoOO00
 if 26 - 26: OOooOOo
 if 12 - 12: OoooooooOO / O0 + OoOoOO00 * ii11ii1ii
def Ii11ii1I1 ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Holly' in oOO00Oo :
   I11iIiI1I1i11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 11 - 11: iIii1I11I1II1 . I1IiI / IIII % o0oO0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 61 - 61: o0oO0 - OoOO0ooOOoo0O + OoOO0ooOOoo0O
def iii ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'East' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 2 - 2: i1IIi * OoOO - OoOO + OoooooooOO % I1IiI / I1IiI
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: OoooooooOO
def O0OoO0o ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Emmer' in oOO00Oo :
   I11iIiI1I1i11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 1 - 1: o0oO0 % o0000oOoOoO0o * ii11ii1ii - OoOoOO00
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: OoOO - oO0o0ooO0 % I1IiI
def Ooo0OOO ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Coro' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 94 - 94: i11iIiiIii % OoooooooOO / OOOo0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: OOOo0 * OoOO
def Oo0 ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Celeb' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 96 - 96: o0000oOoOoO0o % o00O0oo % OoOO * o0000oOoOoO0o / OoOO0ooOOoo0O
def iiI1iiii1 ( name , url ) :
 i1iiIIiiiII = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if i1iiIIiiiII :
  Ii1I1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOooooO0Oo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OOooooO0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOooooO0Oo = open_url ( url )
  OO0ooO0 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OOooooO0Oo ) [ - 1 ]
  Ii1I1 = OO0ooO0 . replace ( '\\/' , '/' )
 i11i1iIiii = xbmcgui . ListItem ( name , '' , '' )
 i11i1iIiii . setPath ( Ii1I1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11i1iIiii )
 if 95 - 95: iIii1I11I1II1 . IIII - OoooooooOO * Ooo00oOo00o / OOooOOo
 if 74 - 74: OoOO
def iII1i1IIiI1I ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iIiIIi1 , 7071 , iIii1 + 'popcorn.png' )
 for iIiIIi1 , oOO00Oo in iiii111II :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iIiIIi1 , 7071 , iIii1 + 'popcorn.png' )
  if 67 - 67: o00O0oo
def iIII11Iiii1 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIi1IIiIi = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Movies' in oOO00Oo :
   I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( iIiIIi1 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iIii1 + 'popcorn.png' )
def o0oo0 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iIii1 + 'popcorn.png' )
  if 67 - 67: O0 * o0000oOoOoO0o - OOooOOo - OoOoOO00
  if 41 - 41: OOOo0 - O0oO % OoOoOO00 . O0oO - o0000oOoOoO0o
def i1I111Ii ( url ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I11iIiI1I1i11 )
  if 31 - 31: OOOo0
  if 73 - 73: o0oO0 . O0 / OOooOOo - OoooooooOO % i11iIiiIii
def O000 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iIiI1I1i11 )
  if 12 - 12: Oo
def oOiI111I1III ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i111IiiI1Ii ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 72 - 72: O0 . I1IiI * Oo + ii11ii1ii - OOooOOo
def i111IiiI1Ii ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 222 , iIii1 + 'popcorn' )
  if 40 - 40: Ooo00oOo00o + Ooo00oOo00o
  if 94 - 94: oO0o0ooO0 * iIii1I11I1II1 . o0000oOoOoO0o
  if 13 - 13: iIii1I11I1II1 * I1IiI / O0oO % o0oO0 + OoOO
  if 41 - 41: ii11ii1ii
def i1iI1i ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( iIiIIi1 ) ) , 222 , I11iIiI1I1i11 )
  if 59 - 59: IIII
def oOoO0OOO00O ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 iiIi1IIiIi = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + iIiIIi1 , 7051 , iIii1 + 'vod.png' )
  if 73 - 73: OOooOOo % Ooo00oOo00o + IIII + OOOo0
def OoOO00 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , iIii1 + 'vod.png' )
  if 74 - 74: o0000oOoOoO0o * o00O0oo - ii11ii1ii % iIii1I11I1II1
def oOoOoO0o0 ( url ) :
 OOooooO0Oo = OOoOoo
 iiIi1IIiIi = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 222 , I11iIiI1I1i11 )
  if 18 - 18: o00O0oo
  if 25 - 25: Ooo00oOo00o * OoOO % i11iIiiIii + i11iIiiIii * Ooo00oOo00o
  if 42 - 42: OoOoOO00 / O0 . iIii1I11I1II1 / O0 / Ooo00oOo00o / OoooooooOO
  if 62 - 62: O0 . Oo
  if 33 - 33: Oo / iIii1I11I1II1 % i1IIi
def O0OooOO ( ) :
 if 49 - 49: IIII / o0oO0 / OoOO0ooOOoo0O
 I1I11i ( 'All Channels' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Entertainment' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Movies' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Music' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'News' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Sports' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Documentary' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Kids' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Food' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Religious' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'USA Channels' , '' , 7021 , iIii1 + 'livetv.png' )
 I1I11i ( 'Other' , '' , 7021 , iIii1 + 'livetv.png' )
 if 25 - 25: OOOo0 % O0 + i1IIi - o0oO0
 if 38 - 38: OOooOOo % O0oO + i11iIiiIii + oO0o0ooO0 + o0oO0 / i11iIiiIii
def o0OOOOOo0 ( Cat_Name ) :
 if 57 - 57: iIii1I11I1II1 + iIii1I11I1II1
 oO0o0Oo = False
 o0OO = '0'
 if Cat_Name == 'All Channels' : oO0o0Oo = True
 if Cat_Name == 'Entertainment' : o0OO = '1'
 if Cat_Name == 'Movies' : o0OO = '2'
 if Cat_Name == 'Music' : o0OO = '3'
 if Cat_Name == 'News' : o0OO = '4'
 if Cat_Name == 'Sports' : o0OO = '5'
 if Cat_Name == 'Documentary' : o0OO = '6'
 if Cat_Name == 'Kids' : o0OO = '7'
 if Cat_Name == 'Food' : o0OO = '8'
 if Cat_Name == 'Religious' : o0OO = '9'
 if Cat_Name == 'USA Channels' : o0OO = '10'
 if Cat_Name == 'Other' : o0OO = '11'
 if 60 - 60: OoOO0ooOOoo0O
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 print 'Len Match: >>>' + str ( len ( iiIi1IIiIi ) )
 for oOO00Oo , I11iIiI1I1i11 , OoOOoooO000 in iiIi1IIiIi :
  OoO0o000oOo = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  if OoOOoooO000 == o0OO :
   I1I11i ( oOO00Oo , '' , 7022 , OoO0o000oOo )
  elif oO0o0Oo == True :
   I1I11i ( oOO00Oo , '' , 7022 , OoO0o000oOo )
  else : pass
  if 65 - 65: I1IiI
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 91 - 91: IIII + o00O0oo % o00O0oo - O0 - i11iIiiIii
def OO00Oo00oO ( Search_Name ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , iIiIIi1 , IiiiI , iiiiI1IiI1I1 in iiIi1IIiIi :
  OoO0o000oOo = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  i1II1 ( Search_Name + ': Link 1' , ( iIiIIi1 ) . replace ( '\\' , '' ) , 222 , OoO0o000oOo )
  i1II1 ( Search_Name + ': Link 2' , ( IiiiI ) . replace ( '\\' , '' ) , 222 , OoO0o000oOo )
  i1II1 ( Search_Name + ': Link 3' , ( iiiiI1IiI1I1 ) . replace ( '\\' , '' ) , 222 , OoO0o000oOo )
  if 94 - 94: i11iIiiIii / O0oO / Oo
def I1iII ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iIii1 + 'english.png' )
def Iii1I1IIII ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'xxx.png' )
def OooooOoO ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'vod(1).png' )
  if 79 - 79: o0oO0 % OoOO0ooOOoo0O
def oO0O0o0O ( url ) :
 url
 oOO00ooOOo = xbmcgui . ListItem ( oOO00Oo , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO00ooOOo )
 return
 if 20 - 20: ii11ii1ii
 if 3 - 3: Ooo00oOo00o * i1IIi . OOOo0 . O0 - I1IiI
def OOoooOoO0 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOooooO0Oo )
 for url , ii11ii11 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  IIIII ( oOO00Oo , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , ( ii11ii11 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iI1 ( 'tvshows' , 'Media Info 3' )
 for url in iiii111II :
  I1I11i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iIii1 + 'FITNESS.png' )
  if 95 - 95: o00O0oo - ii11ii1ii - O0 . OOOo0 . oO0o0ooO0
def iIiIi1IiIi1iI ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , ii11ii11 , I11iIiI1I1i11 in iiIi1IIiIi :
  O00O0oOO00O00 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , ii11ii11 )
  iI1 ( 'tvshows' , 'Media Info 3' )
 i1OO0oOOoo = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( OOoOoOo )
 for o00OO0 in i1OO0oOOoo :
  oooOo = ( o00OO0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  IIIII ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , oooOo )
  if 79 - 79: OoOO - OoOoOO00
def Ii1iiI1 ( INFO ) :
 o0ooOOoO0oO0 ( 'info for workout' , INFO )
 if 86 - 86: i1IIi / o00O0oo * OOOo0
 if 67 - 67: ii11ii1ii * ii11ii1ii / OoOO * OoooooooOO + I1IiI
 if 79 - 79: i1IIi
def iIi1 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 9031 , iIii1 + 'icon.png' )
def ooo0Oooooo ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 9032 , iIii1 + 'icon.png' )
def Ooi1IIii11i1I1 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  if '://' in oOO00Oo :
   pass
   i1II1 ( ( oOO00Oo ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , iIii1 + 'icon.png' )
def Ii1I1O0oo00oOOO0o ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , iIii1 + 'icon.png' )
  if 5 - 5: OOooOOo / OOOo0 % o00O0oo . IIII
  if 86 - 86: i1IIi * I1IiI . O0 - o00O0oo - OOooOOo - I1IiI
  if 47 - 47: OoOO0ooOOoo0O + o0000oOoOoO0o
def i1Iiii ( ) :
 OOooooO0Oo = OOoOoo ( 'http://tvshows.cnfstudio.com/' )
 iiIi1IIiIi = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , 'http://tvshows.cnfstudio.com/genre/' + iIiIIi1 , 7010 , iIii1 + 'icon.png' )
  print '>>>>>>>>>>' + iIiIIi1
  if 87 - 87: IIII / O0oO - Oo
def oOOoOOO0oOoo ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOooooO0Oo )
 o0O0ooooooo00 = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , I11iIiI1I1i11 )
 o0O0ooooooo00 = o0O0ooooooo00
 for url in o0O0ooooooo00 :
  I1I11i ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  I1I11i ( 'Next' , url , 7010 , '' )
  if 28 - 28: o0oO0 * o0000oOoOoO0o % i11iIiiIii * oO0o0ooO0 / o00O0oo
def iIII1iIi ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , Ii , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( 'Season' ) + Ii + ( '  ' ) + oOO00Oo , url , 7004 , iIii1 + 'icon.png' )
  if 75 - 75: o00O0oo - o0000oOoOoO0o % I1IiI
def o00o ( url ) :
 if 45 - 45: ii11ii1ii + O0oO . oO0o0ooO0 . oO0o0ooO0
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iIii1 + 'icon.png' )
  if 34 - 34: Ooo00oOo00o % OOooOOo % OOOo0
def Ii1iIII11iIIi ( name , url , img ) :
 OOoOoOo = OOoOoo ( url )
 I1iiIi1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( OOoOoOo )
 i1iiiIi1Iii = len ( I1iiIi1 )
 if 54 - 54: o0oO0 . iIii1I11I1II1 * i1IIi
 if 44 - 44: OoOO + ii11ii1ii * OoOO0ooOOoo0O - i11iIiiIii / iIii1I11I1II1
 if i1iiiIi1Iii == 1 :
  for iI11II1i1I1 in I1iiIi1 :
   iI11II1i1I1 = iI11II1i1I1 . replace ( 'player' , 'watch' )
   o0oo00O0o = iI11II1i1I1 + '&fv=&sou='
   oo0oOo000oO0O = OOoOoo ( o0oo00O0o )
   o0o = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( oo0oOo000oO0O )
   for I1 in o0o :
    iIi11I11 = False
    Resolve ( I1 )
    if 40 - 40: iIii1I11I1II1
 elif i1iiiIi1Iii > 1 :
  if 92 - 92: I1IiI % O0
  for iI11II1i1I1 in I1iiIi1 :
   oo00ooooOOo00 = OOoOoo ( iI11II1i1I1 )
   ii1i = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oo00ooooOOo00 )
   OO00Oooo000 = ii1i
   OO00Oooo000 = ( str ( OO00Oooo000 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OO00Oooo000
   i1II1 ( 'DOUBLE LINK' , OO00Oooo000 , 424 , '' )
   if 38 - 38: Ooo00oOo00o . o0oO0
   for url in ii1i :
    I1I11i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IiiiI = Google . resolve ( url )
    except :
     pass
    try :
     ii111iiIii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IiiiI ) )
     for oO0o , iIiI in ii111iiIii :
      if 46 - 46: oO0o0ooO0
      HD_URLS . append ( oO0o )
      SD_URLS . append ( iIiI )
    except :
     pass
 else :
  pass
  if 65 - 65: i1IIi . ii11ii1ii / o0oO0
def I1i1I11111iI1 ( ) :
 if 32 - 32: OOOo0 + ii11ii1ii - OoOO + ii11ii1ii / i1IIi * OoOO
 if 90 - 90: o00O0oo % OoOO
 I1I11i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iIii1 + 'Movies.png' )
 if 6 - 6: OoooooooOO / i11iIiiIii / O0oO
 I1I11i ( 'Search Movies' , '' , 7017 , iIii1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 60 - 60: OOOo0 % OoOO / OOooOOo % OoOO * i11iIiiIii / oO0o0ooO0
 if 34 - 34: O0oO - OoOO0ooOOoo0O
def IIIiIi1iiI ( ) :
 OOooooO0Oo = OOoOoo ( 'http://cnfstudio.com/' )
 iiIi1IIiIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , 'http://cnfstudio.com/genre/' + iIiIIi1 , 7003 , iIii1 + 'icon.png' )
  if 15 - 15: ii11ii1ii . oO0o0ooO0
i1iIIi1 = xbmcgui . Dialog ( )
if 94 - 94: o0000oOoOoO0o . OOOo0
if 73 - 73: i1IIi / OoOoOO00
def I1i1I ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOooooO0Oo )
 o0O0ooooooo00 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I11iIiI1I1i11 )
 o0O0ooooooo00 = o0O0ooooooo00
 for url in o0O0ooooooo00 :
  I1I11i ( 'Next Page' , url , 7003 , '' )
  if 17 - 17: o0000oOoOoO0o - oO0o0ooO0 % o00O0oo
def i11Ii1iIIIIi ( url ) :
 if 14 - 14: OoooooooOO . OOooOOo . o0000oOoOoO0o
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  OOooOO000 = url + '&fv=&sou='
  OOooOO000 = OOooOO000 . replace ( 'player' , 'watch' )
  I1IIIIIi1IIiI = III11I11ii ( OOooOO000 )
  O0OoO0oO00 = III11I11ii ( url )
  if 2 - 2: O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
  if 26 - 26: OoOO0ooOOoo0O * Oo
def III11I11ii ( url ) :
 if 31 - 31: o0000oOoOoO0o * OoOO . o00O0oo
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  iI1iIiiI ( url )
  if 35 - 35: o0000oOoOoO0o
  if 94 - 94: o0oO0 / i11iIiiIii % O0
def O0oO0oo0O ( ) :
 IIIII ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 82 - 82: OoooooooOO . o00O0oo
def III1iiiII1ii ( url ) :
 iiIi1IIiIi = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for o0oOoO00 , oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , iIii1 + 'streams.png' )
  if 94 - 94: Ooo00oOo00o + IIII + o0oO0
  if 82 - 82: Oo - Oo . iIii1I11I1II1 / OoOO0ooOOoo0O + IIII % iIii1I11I1II1
def O00OOoo000o ( ) :
 IIIII ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 37 - 37: oO0o0ooO0
 if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
ii11iIi1I = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
O000oooOO0Oo0 = 'https://addons.tvaddons.ag/'
if 31 - 31: IIII - Ooo00oOo00o / OoOO0ooOOoo0O . i1IIi / o00O0oo
def o0o000o ( ) :
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iiiI1i1111II = 'https://addons.tvaddons.ag/search/?keyword=' + oo0
 OOoOoOo = OOoOoo ( iiiI1i1111II )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOoOo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  IIIII ( oOO00Oo , iIiIIi1 , 10054 , 'https://addons.tvaddons.ag/' + I1IIII1i , iI111I11I1I1 , '' )
  if 38 - 38: Oo % ii11ii1ii - oO0o0ooO0 * iIii1I11I1II1 / O0
  if 9 - 9: o0000oOoOoO0o * Oo . o0oO0 * i11iIiiIii - O0
def OoO00OOoOOOo0 ( ) :
 OOoOoOo = OOoOoo ( O000oooOO0Oo0 )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOoOo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if 'Repositories' in oOO00Oo :
   pass
  elif 'Services' in oOO00Oo :
   pass
  elif 'International' in oOO00Oo :
   pass
  else :
   IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10053 , 'https://addons.tvaddons.ag/' + I11iIiI1I1i11 , iI111I11I1I1 , '' )
   if 84 - 84: OoOO + OoOO0ooOOoo0O . oO0o0ooO0
   if 71 - 71: o0oO0 / o0oO0 . I1IiI % oO0o0ooO0
def Addon ( url ) :
 OOoOoOo = OOoOoo ( url )
 I1i1i1 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OOoOoOo )
 for url in I1i1i1 :
  IIIII ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if 'Please' in oOO00Oo :
   pass
  else :
   IIIII ( oOO00Oo , url , 10054 , 'https://addons.tvaddons.ag/' + I11iIiI1I1i11 , iI111I11I1I1 , '' )
   if 82 - 82: IIII . I1IiI / o0oO0 + oO0o0ooO0 - o0oO0
   if 55 - 55: o0oO0 % Oo % OOooOOo
def I1IiO00Ooo0ooo0 ( url , name ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)"' ) . findall ( OOoOoOo )
 for url in iiIi1IIiIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   i1111 = xbmcgui . DialogProgress ( )
   i1111 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   OOOoOoO = os . path . join ( O0oO0 , name + '.zip' )
   try :
    os . remove ( OOOoOoO )
   except :
    pass
   downloader . download ( url , OOOoOoO , i1111 )
   iiiiI = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print iiiiI
   print '======================================='
   extract . all ( OOOoOoO , iiiiI , i1111 )
   oooOo0OOOoo0 ( )
   if 74 - 74: o0000oOoOoO0o
def oooOo0OOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 58 - 58: iIii1I11I1II1 * Ooo00oOo00o * O0oO * o0oO0 . OoooooooOO
 if 6 - 6: ii11ii1ii - OoOO * i11iIiiIii + I1IiI / o0oO0 % OoOO0ooOOoo0O
def II11IiIIiiI ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1007 , I1IIII1i )
def OOo0oOOOOoo0 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I1IIII1i )
  if 80 - 80: i11iIiiIii % ii11ii1ii
  if 54 - 54: OOooOOo + o0000oOoOoO0o - iIii1I11I1II1 % o0oO0 % IIII
def II1i ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , i1iIIIi1i , ii11ii11 , iI1iIIiiii , oOO00Oo in iiIi1IIiIi :
  if '.php' in url :
   i1i1IIiiIIi1I ( oOO00Oo , url , 1016 , i1iIIIi1i , iI1iIIiiii , ii11ii11 )
   iI1 ( 'tvshows' , 'Media Info 3' )
  else :
   i1i1IIiiIIi1I ( oOO00Oo , url , 222 , i1iIIIi1i , iI1iIIiiii , ii11ii11 )
   iI1 ( 'tvshows' , 'Media Info 3' )
   if 13 - 13: ii11ii1ii . IIII
 else :
  iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
  for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
   if '.php' in url :
    I1I11i ( oOO00Oo , url , 1016 , I1IIII1i )
   else :
    i1II1 ( oOO00Oo , url , 222 , I1IIII1i )
    if 4 - 4: Oo - Ooo00oOo00o - i11iIiiIii * O0oO / o00O0oo - OoOO0ooOOoo0O
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 45 - 45: OOooOOo % Oo * i1IIi - O0
def oo00ooOooO ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1007 , I1IIII1i )
def ooIi111iII ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I1IIII1i )
  if 83 - 83: OoooooooOO + Ooo00oOo00o * OoOO . O0
def iiIIIi1i ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iIi1i1i1II11I = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iIi1i1i1II11I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIi1i1i1II11I )
 if 61 - 61: O0oO / OOOo0 + o0oO0 % ii11ii1ii - I1IiI * iIii1I11I1II1
 if 1 - 1: iIii1I11I1II1 . o0000oOoOoO0o + o0000oOoOoO0o . o0oO0
def o0o00OoO0 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I11iIiI1I1i11 )
def O00Oo ( url ) :
 OOooooO0Oo = OO ( url )
 i1ii1II11I = url
 iiIi1IIiIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  if '.mp3' in oOO00Oo :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1II1 ( ( oOO00Oo ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iIii1 + 'music.png' )
  else :
   I1I11i ( ( oOO00Oo ) . replace ( '/' , '' ) , i1ii1II11I + url , 1011 , iIii1 + 'music.png' )
def OO000OO ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , ( 'http://www.cyn.net/music/' + iIiIIi1 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I11iIiI1I1i11 ) . replace ( ' ' , '%20' ) )
def O00o0000OO ( url , img ) :
 OOooooO0Oo = OO ( url )
 IiiiI = url
 img = img
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '.mp3' , '' ) , ( IiiiI + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 61 - 61: IIII % i1IIi - oO0o0ooO0 . o0oO0 - Oo + Oo
  if 12 - 12: OOooOOo / iIii1I11I1II1 % OoOoOO00 / o0000oOoOoO0o / i1IIi - OOOo0
def OoOOOOOoOo0 ( ) :
 O0oOO0o = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IiiiI = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 iiiiI1IiI1I1 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 19 - 19: I1IiI . OOooOOo . OoooooooOO
 OOoOoOo = Ii11I1iIiiI ( iIiIIi1 )
 OOOO0o = Ii11I1iIiiI ( IiiiI )
 Oo0oOo000OoO0 = Ii11I1iIiiI ( iiiiI1IiI1I1 )
 if 13 - 13: OoOO0ooOOoo0O . Oo / OoOoOO00
 if OOoOoOo != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoOo )
  for oOO00Oo in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIIi1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 43 - 43: iIii1I11I1II1 % Ooo00oOo00o
    iI1 ( 'tvshows' , 'Media Info 3' )
 if OOOO0o != 'Failed' :
  iiii111II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoOo )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiiI + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 84 - 84: Oo
    iI1 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOo000OoO0 != 'Failed' :
  oO00O0 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Oo0oOo000OoO0 )
  for oOO00Oo in oO00O0 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiiiI1IiI1I1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 44 - 44: OoooooooOO * i11iIiiIii / Oo
    iI1 ( 'tvshows' , 'Media Info 3' )
    if 75 - 75: OoooooooOO . OoOO0ooOOoo0O + Ooo00oOo00o / o00O0oo - OOOo0 % o00O0oo
    if 89 - 89: oO0o0ooO0 * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
    if 51 - 51: OoOO0ooOOoo0O / o0oO0 + Ooo00oOo00o % I1IiI / o00O0oo
    if 25 - 25: OOooOOo
    if 25 - 25: o0oO0 * oO0o0ooO0 / o0000oOoOoO0o / o0000oOoOoO0o % OOooOOo
    if 19 - 19: OoOO - iIii1I11I1II1 / o0oO0 . Ooo00oOo00o * O0 - O0
def iiIIIIiii ( ) :
 OOooooO0Oo = OOoOoo ( 'http://www.animetoon.org/cartoon' )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1002 , iIii1 + 'anime.png' )
  if 36 - 36: i11iIiiIii / O0 . o0000oOoOoO0o
  if 22 - 22: iIii1I11I1II1 * O0oO / Oo
  if 31 - 31: i11iIiiIii
def O0O0O ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiii111II = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 in iiii111II :
  oOoO00o = I11iIiI1I1i11
 oO00O0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOooooO0Oo )
 for url in oO00O0 :
  I1I11i ( 'NEXT PAGE' , url , 1002 , oOoO00o )
 iiIi1IIiIi = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 1003 , oOoO00o )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1io0Oo00oOO ( url , IMAGE ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  print oOO00Oo + '     ' + url
  if 'easy' in url :
   O0oo ( url )
  elif 'playpanda' in url :
   O0oo ( url )
   if 56 - 56: IIII * O0oO
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0oo ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "url: '(.+?)'," ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( 'STREAM' , url , 222 , iIii1 + 'anime.png' )
  if 98 - 98: o0000oOoOoO0o + O0 * O0oO + i11iIiiIii - OoOO0ooOOoo0O - iIii1I11I1II1
  if 5 - 5: OoOO0ooOOoo0O % Oo % IIII % o0oO0
def I1Iiii ( url ) :
 O0o0OO00 = urllib2 . Request ( url )
 O0o0OO00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o0OO00 . add_header ( 'referer' , url )
 iIi11i = urllib2 . urlopen ( O0o0OO00 )
 OOooOO000 = iIi11i . read ( )
 iIi11i . close ( )
 return OOooOO000
 if 22 - 22: o00O0oo * o0000oOoOoO0o + OOOo0 - o0000oOoOoO0o / ii11ii1ii
def OO ( url ) :
 O0o0OO00 = urllib2 . Request ( url )
 O0o0OO00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iIi11i = urllib2 . urlopen ( O0o0OO00 )
 OOooOO000 = iIi11i . read ( )
 iIi11i . close ( )
 return OOooOO000
 if 18 - 18: i1IIi
def i1i1Ii1IiIII ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Ii = ( '%s%s' % ( oOO , url ) )
 OOooOO000 = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooOO000 )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '%s' % ( oOO00Oo ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I1IIII1i )
  if 9 - 9: o0000oOoOoO0o - OoOO + O0 / oO0o0ooO0 % i1IIi
def iI1iIiiI ( url ) :
 oO000o0OO0OO0 = xbmc . Player ( i11ii1I1 ( ) )
 import urlresolver
 try : oO000o0OO0OO0 . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( oOO00Oo ) )
 oO000o0OO0OO0 = xbmc . Player ( i11ii1I1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iIIi1 = xbmcgui . Dialog ( )
  if i1iIIi1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iIIi1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oO000o0OO0OO0 . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 10 - 10: IIII / OoooooooOO
def OOOO0O00o ( url ) :
 oO000o0OO0OO0 = xbmc . Player ( i11ii1I1 ( ) )
 import urlresolver
 try : oO000o0OO0OO0 . play ( url )
 except : pass
 if 50 - 50: i11iIiiIii - OoooooooOO . OoOO + O0 . i1IIi
 if 91 - 91: OOooOOo . oO0o0ooO0 % Oo - oO0o0ooO0 . OoOO % i11iIiiIii
def i11ii1I1 ( ) :
 try :
  iIiO0O = getSet ( "core-player" )
  if ( iIiO0O == 'DVDPLAYER' ) : oOOoooo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIiO0O == 'MPLAYER' ) : oOOoooo = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIiO0O == 'PAPLAYER' ) : oOOoooo = xbmc . PLAYER_CORE_PAPLAYER
  else : oOOoooo = xbmc . PLAYER_CORE_AUTO
 except : oOOoooo = xbmc . PLAYER_CORE_AUTO
 return oOOoooo
 return True
 if 70 - 70: oO0o0ooO0 . OoOoOO00 . oO0o0ooO0 - iIii1I11I1II1
def I1I11i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0ooO00oO = True
 i11i1iIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1iIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooOo0O0 = [ ]
  if showcontext == 'fav' :
   ooOo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iIi1ii1I1 :
   ooOo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i11i1iIiii . addContextMenuItems ( ooOo0O0 )
 O0ooO00oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = i11i1iIiii , isFolder = True )
 return O0ooO00oO
 if 83 - 83: OoooooooOO
def i1II1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0ooO00oO = True
 i11i1iIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1iIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooOo0O0 = [ ]
  if showcontext == 'fav' :
   ooOo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iIi1ii1I1 :
   ooOo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i11i1iIiii . addContextMenuItems ( ooOo0O0 )
 O0ooO00oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = i11i1iIiii , isFolder = False )
 return O0ooO00oO
 if 12 - 12: o0oO0
 if 36 - 36: O0oO . IIII * OoooooooOO - OOooOOo
 if 60 - 60: OoOO0ooOOoo0O . oO0o0ooO0 / iIii1I11I1II1 + OoOO0ooOOoo0O * O0oO
 if 82 - 82: i11iIiiIii . iIii1I11I1II1 * OOOo0 - o0000oOoOoO0o + o00O0oo
 if 48 - 48: ii11ii1ii
 if 96 - 96: o0oO0 . OoooooooOO
def o0ooOOoO0oO0 ( heading , announce ) :
 class i1I1I1I ( ) :
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
   try : II11IiIi11 = open ( announce ) ; iII1III = II11IiIi11 . read ( )
   except : iII1III = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iII1III ) )
   return
 i1I1I1I ( )
 if 58 - 58: o0000oOoOoO0o % i11iIiiIii / i11iIiiIii * o0oO0 - O0oO
def i11ii111i1ii ( ) :
 o0ooOOoO0oO0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 97 - 97: i11iIiiIii + Oo * OoOO0ooOOoo0O % oO0o0ooO0 . IIII
 if 4 - 4: O0 . oO0o0ooO0 - iIii1I11I1II1
 if 19 - 19: OoOO0ooOOoo0O % Ooo00oOo00o / o00O0oo + OoOoOO00 % OoooooooOO
 if 89 - 89: o00O0oo
 if 51 - 51: oO0o0ooO0
def oooOo0OOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 68 - 68: oO0o0ooO0 - OOooOOo * Ooo00oOo00o % o0oO0 . o0oO0 - iIii1I11I1II1
 if 22 - 22: OoooooooOO / ii11ii1ii % oO0o0ooO0 * I1IiI
 if 32 - 32: OoooooooOO % OoOO % iIii1I11I1II1 / O0
 if 61 - 61: OoOoOO00 . O0 - o00O0oo - ii11ii1ii / i11iIiiIii - OoOoOO00
 if 98 - 98: o00O0oo - OOOo0 . i11iIiiIii * Oo
 if 29 - 29: o00O0oo / o0oO0 % o0000oOoOoO0o
 if 10 - 10: iIii1I11I1II1 % OoooooooOO % ii11ii1ii
 if 39 - 39: OoOoOO00 * I1IiI . O0 * o0000oOoOoO0o
 if 89 - 89: o00O0oo - o0oO0 . o0000oOoOoO0o - O0oO - OOOo0
 if 79 - 79: IIII + IIII + o00O0oo
 if 39 - 39: O0 - OoooooooOO
 if 63 - 63: iIii1I11I1II1 % OOooOOo * o0oO0
 if 79 - 79: O0
 if 32 - 32: OoOoOO00 . O0 + o00O0oo / I1IiI / IIII / OoOO0ooOOoo0O
 if 15 - 15: ii11ii1ii
 if 4 - 4: IIII + iIii1I11I1II1 * oO0o0ooO0 + Oo * OOooOOo % OoOoOO00
 if 88 - 88: OoOO - i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
 if 40 - 40: Oo
 if 47 - 47: I1IiI
 if 65 - 65: O0 + O0oO % o00O0oo * OOOo0 / o0oO0 / I1IiI
 if 71 - 71: i11iIiiIii / I1IiI . OoOO
 if 33 - 33: OoOO
 if 39 - 39: Ooo00oOo00o + O0 + o0oO0 * OoOoOO00 % O0 - O0
 if 41 - 41: IIII % OOooOOo
def oo0O0oOOO0o ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + oOo0Oo0Oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 94 - 94: OOOo0 % I1IiI . IIII . o0oO0 . Ooo00oOo00o
def o0oO0oo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + ooOO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 82 - 82: IIII
def OOOOOOO0oo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + iII11IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 86 - 86: iIii1I11I1II1 % OoOO - I1IiI + O0oO % Ooo00oOo00o . ii11ii1ii
def iiIIiIi ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + O000oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 23 - 23: OoOoOO00 * oO0o0ooO0
def o0Oo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + i1II11i1iI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 81 - 81: OoOO . OoooooooOO * OOooOOo * Ooo00oOo00o
def II11IiI1 ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + iIIi11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 39 - 39: I1IiI . Oo - IIII / OOooOOo / i1IIi
def OOo0OOOoOOo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + III ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 84 - 84: i11iIiiIii + o0oO0 . O0
def o00oo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + Ii11IIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 93 - 93: i11iIiiIii . OOooOOo
def IiiIiI1IIi1IIIii ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + OOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 80 - 80: IIII + o0000oOoOoO0o + OoOO % Ooo00oOo00o - Oo - OoOO
def iI ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + oO0Oooo0OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 38 - 38: OOOo0 . OOOo0 . o00O0oo + ii11ii1ii * Oo
 if 61 - 61: OoOoOO00 . IIII - O0 * IIII
 if 43 - 43: OOOo0 / oO0o0ooO0 / o0oO0 + iIii1I11I1II1 + OoooooooOO
 if 33 - 33: OoOoOO00 - IIII - o0oO0
 if 92 - 92: Ooo00oOo00o * IIII
 if 92 - 92: OoOO
 if 7 - 7: oO0o0ooO0
 if 73 - 73: Ooo00oOo00o % ii11ii1ii
 if 32 - 32: OoOO0ooOOoo0O + oO0o0ooO0 + iIii1I11I1II1 * Oo
def ooiIii1I1111 ( ) :
 try :
  if os . path . exists ( ooOoOoo0O ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( ooOoOoo0O ) :
     I1i = 0
     I1i += len ( oOOOoo00 )
     if I1i > 0 :
      for II11IiIi11 in oOOOoo00 :
       os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
  IiiiIi1111I = os . path . join ( iiI1IiI , "Textures13.db" )
  os . unlink ( IiiiIi1111I )
  i1iIIi1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 45 - 45: OOooOOo
 if 58 - 58: OOOo0 * i1IIi % OoOoOO00 / O0
 if 56 - 56: o0000oOoOoO0o - O0 / O0 * i1IIi . OoooooooOO % iIii1I11I1II1
 if 21 - 21: IIII - OOOo0 % OoooooooOO + OOooOOo
 if 92 - 92: o0oO0 + IIII
 if 52 - 52: OoOoOO00 / OOOo0 . OoOO * IIII . o0000oOoOoO0o
 if 25 - 25: i11iIiiIii / I1IiI - O0oO / Ooo00oOo00o . OOooOOo . OOooOOo
 if 6 - 6: OoOO . o0000oOoOoO0o
 if 43 - 43: ii11ii1ii + OOooOOo
def iI1iiiiiii ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 Oo00oo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( Oo00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( Oo00oo ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 79 - 79: ii11ii1ii / O0 % OOooOOo
   if 71 - 71: O0oO / OOOo0 / O0
   if I1i > 0 :
    if 19 - 19: i11iIiiIii . OOOo0 + OoOoOO00 / OoOO0ooOOoo0O . ii11ii1ii * o0oO0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete KODI Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 59 - 59: iIii1I11I1II1 / ii11ii1ii % o0oO0
     for II11IiIi11 in oOOOoo00 :
      try :
       os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
      except :
       pass
     for Oooo in Ooo0oOooo0 :
      try :
       shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      except :
       pass
       if 74 - 74: o0oO0 % I1IiI / Oo
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  i1111Ii11i = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 98 - 98: iIii1I11I1II1 - i1IIi + o0oO0 % o0000oOoOoO0o + o0oO0 / OoOO
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( i1111Ii11i ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 97 - 97: IIII % o0oO0 + OoOoOO00 - IIII % Ooo00oOo00o + o0oO0
   if I1i > 0 :
    if 31 - 31: OOooOOo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( I1i ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 35 - 35: I1IiI + o00O0oo * o0oO0 / I1IiI
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 69 - 69: o0oO0 . OoOO0ooOOoo0O - OOOo0
   else :
    pass
  IiIi = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 44 - 44: OoOoOO00 . OoOoOO00 + OoOO0ooOOoo0O * o00O0oo
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( IiIi ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 16 - 16: OoOoOO00
   if I1i > 0 :
    if 100 - 100: O0 - i1IIi
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( I1i ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 48 - 48: OoOO % o0oO0 + O0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 27 - 27: ii11ii1ii / OoOO0ooOOoo0O
   else :
    pass
    if 33 - 33: OoooooooOO % ii11ii1ii . O0 / ii11ii1ii
    if 63 - 63: IIII + iIii1I11I1II1 + OOOo0 + O0oO
    if 72 - 72: Ooo00oOo00o + i11iIiiIii + ii11ii1ii
    if 96 - 96: OoOO % i1IIi / OOooOOo
 Ii1IIi11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( Ii1IIi11 ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( Ii1IIi11 ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 47 - 47: O0
   if 83 - 83: O0 + I1IiI / O0 / o0000oOoOoO0o
   if I1i > 0 :
    if 68 - 68: i1IIi . o0000oOoOoO0o . i1IIi + IIII % OOOo0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete WTF Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: I1IiI . iIii1I11I1II1 % OoOO . O0 . I1IiI / oO0o0ooO0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 45 - 45: iIii1I11I1II1
   else :
    pass
    if 41 - 41: oO0o0ooO0 % oO0o0ooO0 - IIII % Ooo00oOo00o - OoooooooOO - oO0o0ooO0
    if 66 - 66: OOooOOo % I1IiI
 II1I1iIIiIIii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( II1I1iIIiIIii ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( II1I1iIIiIIii ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 65 - 65: i11iIiiIii - o0oO0 * o0000oOoOoO0o + o0oO0 / IIII + OOooOOo
   if 35 - 35: O0 + Oo - OOOo0 % o00O0oo % OoOoOO00
   if I1i > 0 :
    if 77 - 77: O0oO + OoOO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete 4oD Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: ii11ii1ii - o00O0oo * OOooOOo
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 13 - 13: OOOo0 * OoOO
   else :
    pass
    if 41 - 41: IIII
    if 16 - 16: iIii1I11I1II1
 o000o0o00Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( o000o0o00Oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( o000o0o00Oo ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 62 - 62: oO0o0ooO0
   if 8 - 8: oO0o0ooO0 - OOOo0 * Oo % ii11ii1ii * OoooooooOO
   if I1i > 0 :
    if 26 - 26: i1IIi / oO0o0ooO0 . oO0o0ooO0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete BBC iPlayer Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 20 - 20: OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 55 - 55: OoooooooOO
   else :
    pass
    if 73 - 73: I1IiI - ii11ii1ii % Oo + ii11ii1ii - O0 . Ooo00oOo00o
    if 38 - 38: O0
    if 79 - 79: i1IIi . OoOO
 i1i1i11iI11II = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( i1i1i11iI11II ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( i1i1i11iI11II ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / o00O0oo
   if 14 - 14: O0oO % IIII - O0 / O0oO
   if I1i > 0 :
    if 91 - 91: i11iIiiIii % O0oO * OoOO - ii11ii1ii . O0oO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Simple Downloader Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: i11iIiiIii
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 51 - 51: OOOo0 + o0oO0 * O0 . o00O0oo
   else :
    pass
    if 82 - 82: OoOO0ooOOoo0O * ii11ii1ii % o00O0oo . OoOO0ooOOoo0O
    if 43 - 43: Ooo00oOo00o . o0oO0 * Oo
 iio00O0o00oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iio00O0o00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iio00O0o00oo ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 19 - 19: OOOo0
   if 66 - 66: OoOO / I1IiI
   if I1i > 0 :
    if 13 - 13: OoOoOO00
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ITV Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 55 - 55: Oo % i1IIi * o0000oOoOoO0o
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 95 - 95: OoOO0ooOOoo0O / OoOoOO00 - OOooOOo % O0oO . o0000oOoOoO0o
   else :
    pass
    if 63 - 63: iIii1I11I1II1 / o0oO0
    if 24 - 24: Oo / iIii1I11I1II1 % OoOO0ooOOoo0O * I1IiI - iIii1I11I1II1
 iI1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iio00O0o00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iI1ii ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 61 - 61: Oo * i1IIi . OoooooooOO
   if 44 - 44: OOOo0
   if I1i > 0 :
    if 55 - 55: OoOO . O0oO * O0oO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Movies4me Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 82 - 82: OOOo0 % Ooo00oOo00o % o0000oOoOoO0o + o0000oOoOoO0o
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 6 - 6: Oo
   else :
    pass
    if 73 - 73: O0oO * ii11ii1ii + OOooOOo - Oo . o0000oOoOoO0o
    if 93 - 93: i11iIiiIii
 OoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iio00O0o00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( OoO ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 34 - 34: Oo - o00O0oo - oO0o0ooO0
   if 61 - 61: ii11ii1ii
   if I1i > 0 :
    if 33 - 33: I1IiI / Ooo00oOo00o
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Phoenix Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: oO0o0ooO0 + O0 / OoOoOO00 * OOOo0 - OoooooooOO . o00O0oo
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 28 - 28: OoOO . OoOO . iIii1I11I1II1 . OoOO0ooOOoo0O . ii11ii1ii * i11iIiiIii
   else :
    pass
    if 72 - 72: o0000oOoOoO0o
    if 26 - 26: IIII % Oo
 OoOOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iio00O0o00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( OoOOoo ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 38 - 38: OoOO + iIii1I11I1II1 * o00O0oo / Ooo00oOo00o + OoOO0ooOOoo0O
   if 48 - 48: OoooooooOO - O0oO . i11iIiiIii * oO0o0ooO0 - o00O0oo - OOooOOo
   if I1i > 0 :
    if 59 - 59: oO0o0ooO0 / o0000oOoOoO0o . Oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Music Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 100 - 100: O0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 94 - 94: ii11ii1ii - OOooOOo
   else :
    pass
    if 42 - 42: OOooOOo * I1IiI . Ooo00oOo00o - oO0o0ooO0 / OoOoOO00
    if 25 - 25: Oo % I1IiI
 o00OIIIIII1iI1II = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iio00O0o00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( o00OIIIIII1iI1II ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 14 - 14: OOOo0 / O0
   if 43 - 43: OoOO - IIII % i11iIiiIii * OoOoOO00 . O0oO - o0000oOoOoO0o
   if I1i > 0 :
    if 13 - 13: Ooo00oOo00o
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete SuperCartoons Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: IIII . O0oO * Ooo00oOo00o + o0000oOoOoO0o - IIII . IIII
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 60 - 60: i11iIiiIii * Oo % Ooo00oOo00o + Ooo00oOo00o
   else :
    pass
    if 84 - 84: iIii1I11I1II1 + OoooooooOO
    if 77 - 77: O0 * ii11ii1ii * OoOO + Ooo00oOo00o + ii11ii1ii - O0oO
 iI1I1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iio00O0o00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iI1I1I ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 33 - 33: iIii1I11I1II1 / oO0o0ooO0
   if 74 - 74: OOooOOo / OoOO - OoOoOO00 . OoOoOO00 . IIII + OoOoOO00
   if I1i > 0 :
    if 92 - 92: O0oO % iIii1I11I1II1 - oO0o0ooO0 / i11iIiiIii % o0oO0 * OOooOOo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete TVonline Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 80 - 80: oO0o0ooO0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 3 - 3: ii11ii1ii * o0000oOoOoO0o
   else :
    pass
    if 53 - 53: iIii1I11I1II1 / oO0o0ooO0 % Ooo00oOo00o + IIII / o0oO0
    if 74 - 74: Oo
 IiIiII11i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iio00O0o00oo ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( IiIiII11i1 ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 44 - 44: OOOo0 % OoOO0ooOOoo0O * i11iIiiIii * i11iIiiIii - Oo . O0oO
   if 68 - 68: oO0o0ooO0 . o0000oOoOoO0o
   if I1i > 0 :
    if 29 - 29: o0oO0 * IIII
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 75 - 75: O0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
      if 56 - 56: Ooo00oOo00o / OoOoOO00
   else :
    pass
    if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
    if 49 - 49: Oo + O0 + IIII . OoOoOO00 % o0oO0
    if 33 - 33: I1IiI . iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
 IIiiI11 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iIIi1 = xbmcgui . Dialog ( )
 try :
  if i1iIIi1 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   IiIII = os . path . join ( IIiiI11 , "cache.db" )
   os . unlink ( IiIII )
   if 92 - 92: OOOo0 % oO0o0ooO0
 except :
  pass
  if 31 - 31: OoooooooOO - OoOO / O0oO
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 62 - 62: i11iIiiIii - o0000oOoOoO0o
 if 81 - 81: o0000oOoOoO0o
 if 92 - 92: OoOO0ooOOoo0O - Oo - OoooooooOO / IIII - i1IIi
 if 81 - 81: i1IIi / O0oO % i11iIiiIii . iIii1I11I1II1 * I1IiI + OoooooooOO
 if 31 - 31: i1IIi % OoOoOO00
 if 13 - 13: iIii1I11I1II1 - OoOoOO00 % O0 . o00O0oo % Ooo00oOo00o
 if 2 - 2: OoooooooOO - o00O0oo % OoOO / OOOo0 / OOooOOo
 if 3 - 3: OoOoOO00 / OoOO0ooOOoo0O
 if 48 - 48: o0oO0 . ii11ii1ii
def IiiIIIIi ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 IiIIIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( IiIIIi ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 81 - 81: OoooooooOO . I1IiI * iIii1I11I1II1 / I1IiI - ii11ii1ii % i1IIi
   if 77 - 77: OOOo0 / OoooooooOO
   if I1i > 0 :
    if 33 - 33: i11iIiiIii + o00O0oo % OOooOOo % OOOo0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Package Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 66 - 66: OOooOOo % IIII
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
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
 if 100 - 100: iIii1I11I1II1
 if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
 if 98 - 98: Ooo00oOo00o
 if 18 - 18: o0000oOoOoO0o + Oo - Ooo00oOo00o / O0oO / OoOO0ooOOoo0O
 if 53 - 53: OoOO0ooOOoo0O + OOooOOo . OoOO / o0000oOoOoO0o
 if 52 - 52: O0oO + O0oO
 if 73 - 73: OOooOOo . i11iIiiIii % OoooooooOO + o0oO0 . OoooooooOO / OoOO0ooOOoo0O
 if 54 - 54: I1IiI . OoooooooOO
 if 36 - 36: OoOO / OoOoOO00 * IIII % ii11ii1ii
def IiIIii ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 IiIIIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( IiIIIi ) :
   I1i = 0
   I1i += len ( oOOOoo00 )
   if 74 - 74: iIii1I11I1II1 / o00O0oo
   if 59 - 59: o00O0oo / OoOoOO00 - IIII % I1IiI % OoooooooOO
   if I1i > 0 :
    if 79 - 79: oO0o0ooO0 . OoooooooOO . OOOo0 * O0 * Ooo00oOo00o - OoOO0ooOOoo0O
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Package Cache Files" , str ( I1i ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: ii11ii1ii . Oo + OOOo0 + OOooOOo
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for Oooo in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , Oooo ) )
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
 iI1iiiiiii ( url )
 if 54 - 54: o0oO0 * oO0o0ooO0 * oO0o0ooO0 % I1IiI - OoOO0ooOOoo0O % ii11ii1ii
 if 44 - 44: Oo . OoOO0ooOOoo0O + o0000oOoOoO0o
 if 22 - 22: O0oO * OoooooooOO + i11iIiiIii % Ooo00oOo00o
 if 53 - 53: OOOo0
 if 10 - 10: O0oO / i11iIiiIii - OoOoOO00
 if 48 - 48: OoOO0ooOOoo0O
 if 26 - 26: oO0o0ooO0 * O0oO * OoOO * I1IiI
 if 48 - 48: oO0o0ooO0 % i11iIiiIii . OoooooooOO * IIII % Ooo00oOo00o . oO0o0ooO0
 if 6 - 6: O0 . o0oO0 - OoOO / i11iIiiIii
def O00O0 ( url , name ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O00o0O = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 i1iIIi1 = xbmcgui . Dialog ( )
 oooOo00 = os . path . join ( O0oO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oooOo00 ) == False :
  if i1iIIi1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   O00o0O = os . path . join ( O0oO0 , 'advancedsettings.xml' )
   try :
    os . remove ( O00o0O )
    print '=== GenieTv - REMOVING    ' + str ( O00o0O ) + '    ==='
   except :
    pass
   OOooOO000 = I11 . http_GET ( url ) . content
   iiIiIIIiiI = open ( O00o0O , "w" )
   iiIiIIIiiI . write ( OOooOO000 )
   iiIiIIIiiI . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( O00o0O ) + '    ==='
   i1iIIi1 = xbmcgui . Dialog ( )
   i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  O00o0O = os . path . join ( O0oO0 , 'advancedsettings.xml' )
  try :
   os . remove ( O00o0O )
   print '=== GenieTv - REMOVING    ' + str ( O00o0O ) + '    ==='
  except :
   pass
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( O00o0O , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O00o0O ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 1 - 1: OOOo0 + ii11ii1ii
def Ooo0oO0 ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O00o0O = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 try :
  iiIiIIIiiI = open ( O00o0O ) . read ( )
  if 'zero' in iiIiIIIiiI :
   name = '0CACHE'
  elif 'tuxen' in iiIiIIIiiI :
   name = 'TUXENS'
  elif 'muckys' in iiIiIIIiiI :
   name = 'MUCKYS'
  elif 'p2p1' in iiIiIIIiiI :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iiIiIIIiiI :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iiIiIIIiiI :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 77 - 77: Oo / o0000oOoOoO0o . oO0o0ooO0 / O0oO - OoooooooOO
def o0iii1i ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O00o0O = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 try :
  os . remove ( O00o0O )
  i1iIIi1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( O00o0O ) + '    ==='
  i1iIIi1 . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 30 - 30: I1IiI / OOOo0 - Ooo00oOo00o - oO0o0ooO0 - i11iIiiIii
 if 84 - 84: i1IIi - OOOo0 % oO0o0ooO0
 if 80 - 80: OOooOOo % oO0o0ooO0
 if 80 - 80: o00O0oo
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 if 59 - 59: ii11ii1ii + o0000oOoOoO0o . OoOO
 if 87 - 87: Ooo00oOo00o
 if 34 - 34: O0oO . I1IiI / i11iIiiIii / oO0o0ooO0
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + OoOO0ooOOoo0O
 if 31 - 31: o00O0oo * OOooOOo * o00O0oo + Ooo00oOo00o * OOooOOo . O0oO
def Oo00oo00o00Oo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iiIi1IIiIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for iiiiiii11III , I11111ii1i , O0OOoO0OoO0 , iI11IiiiIII in iiIi1IIiIi :
  if inc < 2 : i1iIIi1 = xbmcgui . Dialog ( ) ; i1iIIi1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iiiiiii11III , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % O0OOoO0OoO0 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iI11IiiiIII )
  inc = inc + 1
  if 43 - 43: oO0o0ooO0 + i11iIiiIii
  if 96 - 96: OoOO0ooOOoo0O . I1IiI * O0
  if 69 - 69: IIII
  if 81 - 81: OOOo0
  if 58 - 58: I1IiI + Ooo00oOo00o * o00O0oo
  if 31 - 31: OoOO - oO0o0ooO0
  if 46 - 46: OOOo0 + Oo - o00O0oo
  if 99 - 99: OoOO0ooOOoo0O + OOOo0 . ii11ii1ii * OoooooooOO
  if 82 - 82: i11iIiiIii + iIii1I11I1II1 / Oo + OoOO0ooOOoo0O * OoOoOO00
def iIiIiiIIIi1 ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  O00o0O = os . path . join ( O0oO0 , 'addons2.ini' )
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( O00o0O , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O00o0O ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 25 - 25: O0
def Oo00o00 ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  O00o0O = os . path . join ( O0oO0 , 'settings.xml' )
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( O00o0O , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O00o0O ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 74 - 74: O0 + iIii1I11I1II1 + OoOO * IIII
 if 39 - 39: O0oO . Ooo00oOo00o % o0oO0 . OoOO0ooOOoo0O / oO0o0ooO0 * Ooo00oOo00o
def iiI1i ( ) :
 try :
  o0O00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( o0O00o0 ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OoOoOooO0o = os . path . join ( o0O00o0 , "source.db" )
    os . unlink ( OoOoOooO0o )
  i1iIIi1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 23 - 23: OOOo0
 if 7 - 7: oO0o0ooO0 % ii11ii1ii
 if 64 - 64: O0oO + i11iIiiIii
 if 35 - 35: I1IiI + i1IIi % OoOO0ooOOoo0O
 if 68 - 68: IIII . o0oO0
def OOoOoo ( url ) :
 O0o0OO00 = urllib2 . Request ( url )
 O0o0OO00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iIi11i = urllib2 . urlopen ( O0o0OO00 )
 OOooOO000 = iIi11i . read ( )
 iIi11i . close ( )
 return OOooOO000
 if 64 - 64: i1IIi + Oo * OOOo0 / OoOO0ooOOoo0O
 if 3 - 3: Oo / o0oO0 + o0oO0 . ii11ii1ii
 if 50 - 50: iIii1I11I1II1 * OoOO
 if 85 - 85: i1IIi
 if 100 - 100: OoooooooOO / o0000oOoOoO0o % Ooo00oOo00o + o00O0oo
 if 42 - 42: Oo / IIII . o00O0oo * OOOo0
 if 54 - 54: I1IiI * oO0o0ooO0 + Ooo00oOo00o
def oOOOo ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; o0OOOoO0O = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if o0OOOoO0O :
  OoOOo = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; OoOOo = xbmc . translatePath ( OoOOo ) ;
  III11iI1i11i = os . path . join ( OoOOo , ".." , ".." ) ; III11iI1i11i = os . path . abspath ( III11iI1i11i ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + III11iI1i11i ) ; IIiI = False
  try :
   for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( III11iI1i11i , topdown = True ) :
    Ooo0oOooo0 [ : ] = [ Oooo for Oooo in Ooo0oOooo0 if Oooo not in Oo0oO0ooo ]
    for oOO00Oo in oOOOoo00 :
     try : os . remove ( os . path . join ( oooi1i1iI1iiiI , oOO00Oo ) )
     except :
      if oOO00Oo not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIiI = True
      plugintools . log ( "Error removing " + oooi1i1iI1iiiI + " " + oOO00Oo )
    for oOO00Oo in Ooo0oOooo0 :
     try : os . rmdir ( os . path . join ( oooi1i1iI1iiiI , oOO00Oo ) )
     except :
      if oOO00Oo not in [ "Database" , "userdata" ] : IIiI = True
      plugintools . log ( "Error removing " + oooi1i1iI1iiiI + " " + oOO00Oo )
   if not IIiI : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0oO0O0o0O00O ( )
 if 99 - 99: OOooOOo * OoOO . O0oO / I1IiI . o0oO0
 if 1 - 1: OoOO0ooOOoo0O
 if 87 - 87: O0 * OoOoOO00 + iIii1I11I1II1 % OoOO % i11iIiiIii - I1IiI
def o00O0O ( ) :
 oooOoO = [ ]
 IiiIi1IiiiI = sys . argv [ 2 ]
 if len ( IiiIi1IiiiI ) >= 2 :
  OO0oooOO = sys . argv [ 2 ]
  IIIi1iiIIiiiI = OO0oooOO . replace ( '?' , '' )
  if ( OO0oooOO [ len ( OO0oooOO ) - 1 ] == '/' ) :
   OO0oooOO = OO0oooOO [ 0 : len ( OO0oooOO ) - 2 ]
  I1IIiIi1iI = IIIi1iiIIiiiI . split ( '&' )
  oooOoO = { }
  for O00OO in range ( len ( I1IIiIi1iI ) ) :
   oOo0 = { }
   oOo0 = I1IIiIi1iI [ O00OO ] . split ( '=' )
   if ( len ( oOo0 ) ) == 2 :
    oooOoO [ oOo0 [ 0 ] ] = oOo0 [ 1 ]
    if 2 - 2: OOOo0 + OoOoOO00 / o00O0oo % Oo - O0oO + O0oO
 return oooOoO
 if 84 - 84: OOooOOo % i1IIi / Oo - OOOo0 . ii11ii1ii . OOooOOo
oOOoo00O00o = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
oO0O0OO0O = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O0O00Oo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OoOoo00Oo0OoO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oO0000OOo00 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
o0o0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
oOo0Oo0Oo0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oOOO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
ooOO00Oo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
iII11IiI1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
O000oO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1II11i1iI1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iIIi11i = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
III = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
Ii11IIIi1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OOO0o = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooO0oOOooOo0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
OOooo = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iiIi1IIi1I = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
IIi1I11I1II = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oO0Oooo0OoO = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oOO = base64 . decodestring ( 'Q1VOVA==' )
def IIIII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0ooO00oO = True
 i11i1iIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1iIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11i1iIiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOo0O0 = [ ]
  if showcontext == 'fav' :
   ooOo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iIi1ii1I1 :
   ooOo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i11i1iIiii . addContextMenuItems ( ooOo0O0 )
 O0ooO00oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = i11i1iIiii , isFolder = True )
 return O0ooO00oO
 if 20 - 20: I1IiI / ii11ii1ii - iIii1I11I1II1 * IIII
def O00O0oOO00O00 ( name , url , mode , iconimage , fanart , description ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0ooO00oO = True
 i11i1iIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1iIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11i1iIiii . setProperty ( "Fanart_Image" , fanart )
 O0ooO00oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = i11i1iIiii , isFolder = False )
 return O0ooO00oO
 if 78 - 78: OoOO % I1IiI
 if 1 - 1: I1IiI - OOooOOo / o0oO0 - IIII / i1IIi
OO0oooOO = o00O0O ( )
iIiIIi1 = None
oOO00Oo = None
Ii1iI111 = None
i1iIIIi1i = None
iI1iIIiiii = None
i1iI11i1ii11 = None
II11I = None
if 32 - 32: OoooooooOO + Ooo00oOo00o . O0oO / OoOO + OoooooooOO - o00O0oo
if 77 - 77: OOOo0 - OOooOOo
try :
 II11I = int ( OO0oooOO [ "fav_mode" ] )
except :
 pass
 if 11 - 11: ii11ii1ii - OoooooooOO
try :
 iIiIIi1 = urllib . unquote_plus ( OO0oooOO [ "url" ] )
except :
 pass
try :
 oOO00Oo = urllib . unquote_plus ( OO0oooOO [ "name" ] )
except :
 pass
try :
 i1iIIIi1i = urllib . unquote_plus ( OO0oooOO [ "iconimage" ] )
except :
 pass
try :
 Ii1iI111 = int ( OO0oooOO [ "mode" ] )
except :
 pass
try :
 iI1iIIiiii = urllib . unquote_plus ( OO0oooOO [ "fanart" ] )
except :
 pass
try :
 i1iI11i1ii11 = urllib . unquote_plus ( OO0oooOO [ "description" ] )
except :
 pass
 if 16 - 16: IIII % OoooooooOO - o0oO0 * o00O0oo - o00O0oo
 if 27 - 27: IIII + iIii1I11I1II1 / Oo + Ooo00oOo00o % Oo + Ooo00oOo00o
print str ( OooO0 ) + ': ' + str ( O0OoO000O0OO )
print "Mode: " + str ( Ii1iI111 )
print "URL: " + str ( iIiIIi1 )
print "Name: " + str ( oOO00Oo )
print "IconImage: " + str ( i1iIIIi1i )
if 77 - 77: Oo * o0oO0 % o00O0oo
if 2 - 2: o0000oOoOoO0o / Oo / o00O0oo / ii11ii1ii / OoooooooOO
def iI1 ( content , viewType ) :
 if 22 - 22: iIii1I11I1II1 * OOOo0 / o0000oOoOoO0o + I1IiI
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 98 - 98: OoOO0ooOOoo0O
  if 69 - 69: OoOoOO00 + Oo - OoOO . Oo / iIii1I11I1II1 * iIii1I11I1II1
if Ii1iI111 == None :
 I11II1i ( )
 if 75 - 75: Ooo00oOo00o % OoooooooOO
elif Ii1iI111 == 1 :
 i1i ( iIiIIi1 )
 if 16 - 16: O0 / i1IIi
elif Ii1iI111 == 44 :
 O0oOOO0ooOOO0OOO ( iIiIIi1 )
 if 58 - 58: OOooOOo / i11iIiiIii / O0 % o0000oOoOoO0o % OOOo0
elif Ii1iI111 == 2 :
 Ooo00o0Oooo ( )
 if 86 - 86: IIII + I1IiI / OOOo0 + o0000oOoOoO0o % o0000oOoOoO0o / i11iIiiIii
elif Ii1iI111 == 3 :
 oO0 ( )
 if 12 - 12: I1IiI + OOooOOo . O0oO
elif Ii1iI111 == 21 :
 o000O0o ( )
 if 52 - 52: Ooo00oOo00o
elif Ii1iI111 == 4 :
 iIIIIi1iiIi1 ( )
 if 4 - 4: o00O0oo % ii11ii1ii + o0000oOoOoO0o - ii11ii1ii
elif Ii1iI111 == 5 :
 O0Oo0oOOoooOOOOo ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 98 - 98: o00O0oo - O0 * OoOO * o00O0oo * o00O0oo
elif Ii1iI111 == 6 :
 IiiIIIIi ( iIiIIi1 )
 if 44 - 44: IIII + o0000oOoOoO0o
elif Ii1iI111 == 7 :
 O00O0 ( iIiIIi1 , oOO00Oo )
 if 66 - 66: OoOO
elif Ii1iI111 == 8 :
 Ooo0oO0 ( iIiIIi1 , oOO00Oo )
 if 34 - 34: oO0o0ooO0 % i11iIiiIii + i11iIiiIii - oO0o0ooO0
elif Ii1iI111 == 9 :
 FIXREPOSADDONS ( iIiIIi1 )
 if 2 - 2: OoOoOO00 + i1IIi
elif Ii1iI111 == 10 :
 oooOo0OOOoo0 ( )
 if 68 - 68: OoOO0ooOOoo0O + o00O0oo
elif Ii1iI111 == 11 :
 o0iii1i ( iIiIIi1 )
 if 58 - 58: IIII * o00O0oo . i1IIi
elif Ii1iI111 == 12 :
 Oo00oo00o00Oo ( )
 if 19 - 19: OoOO
elif Ii1iI111 == 13 :
 ooiIii1I1111 ( )
 if 85 - 85: o0oO0 - OOOo0 / i1IIi / Ooo00oOo00o / OoOoOO00
elif Ii1iI111 == 14 :
 iI1iiiiiii ( iIiIIi1 )
 if 94 - 94: iIii1I11I1II1 + IIII
elif Ii1iI111 == 15 :
 OO0oOO0O ( )
 if 44 - 44: Ooo00oOo00o + o0000oOoOoO0o % Ooo00oOo00o + i1IIi + oO0o0ooO0 + O0
elif Ii1iI111 == 16 :
 iIiIiiIIIi1 ( iIiIIi1 , oOO00Oo )
 if 18 - 18: iIii1I11I1II1 % iIii1I11I1II1 % OoOO + OOOo0 % o0oO0 / o00O0oo
elif Ii1iI111 == 17 :
 Oo00o00 ( iIiIIi1 , oOO00Oo )
 if 36 - 36: I1IiI . i11iIiiIii
elif Ii1iI111 == 18 :
 iiI1i ( )
 if 81 - 81: Oo * oO0o0ooO0 * Ooo00oOo00o
elif Ii1iI111 == 19 :
 Iiiii1I ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 85 - 85: O0 * OoOO
elif Ii1iI111 == 40 :
 IiI1i ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 39 - 39: OoOoOO00 * OOOo0 - iIii1I11I1II1
elif Ii1iI111 == 42 :
 ii1111iII ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 25 - 25: OoooooooOO . o00O0oo % oO0o0ooO0 . IIII
elif Ii1iI111 == 43 :
 I1i1i1iii ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 67 - 67: OoooooooOO + O0oO / o0oO0
elif Ii1iI111 == 20 :
 Ii1 ( iIiIIi1 )
 if 75 - 75: IIII / OoooooooOO . OOOo0 + O0oO - OoOoOO00
elif Ii1iI111 == 22 :
 oo0O0oOOO0o ( iIiIIi1 )
 if 33 - 33: IIII / IIII . i11iIiiIii * ii11ii1ii + OOooOOo
elif Ii1iI111 == 23 :
 o0oO0oo ( iIiIIi1 )
 if 16 - 16: IIII
elif Ii1iI111 == 24 :
 OOOOOOO0oo ( iIiIIi1 )
 if 10 - 10: I1IiI . IIII * iIii1I11I1II1 - OoOO - I1IiI / O0oO
elif Ii1iI111 == 25 :
 iiIIiIi ( iIiIIi1 )
 if 13 - 13: OoOO + I1IiI % IIII % OoooooooOO
elif Ii1iI111 == 26 :
 o0Oo ( iIiIIi1 )
 if 22 - 22: O0oO
elif Ii1iI111 == 27 :
 II11IiI1 ( iIiIIi1 )
 if 23 - 23: O0
elif Ii1iI111 == 28 :
 OOo0OOOoOOo ( iIiIIi1 )
 if 41 - 41: i1IIi . OoOO0ooOOoo0O / o0oO0 / OOooOOo % IIII - o00O0oo
elif Ii1iI111 == 29 :
 o00oo ( iIiIIi1 )
 if 14 - 14: ii11ii1ii - i11iIiiIii * O0oO
elif Ii1iI111 == 30 :
 O0ooO0Oo00o ( iIiIIi1 )
 if 39 - 39: OoooooooOO
elif Ii1iI111 == 31 :
 IiiIiI1IIi1IIIii ( iIiIIi1 )
 if 19 - 19: i11iIiiIii
elif Ii1iI111 == 32 :
 O0oOoOOOoOO ( )
 if 80 - 80: OOOo0
elif Ii1iI111 == 33 :
 O0o ( )
 if 58 - 58: OoOO + ii11ii1ii % I1IiI
elif Ii1iI111 == 35 :
 O0o000Oo ( iIiIIi1 )
 if 22 - 22: iIii1I11I1II1 - o00O0oo / OOOo0 * IIII
elif Ii1iI111 == 34 :
 oo000o ( iIiIIi1 )
 if 26 - 26: OOooOOo + OoOO0ooOOoo0O - OOooOOo + Oo . OoOO
elif Ii1iI111 == 36 :
 O000oo ( iIiIIi1 )
 if 97 - 97: i1IIi
elif Ii1iI111 == 37 :
 o0OOOO00O0Oo ( iIiIIi1 )
 if 46 - 46: ii11ii1ii
elif Ii1iI111 == 38 :
 IIi ( iIiIIi1 )
 if 30 - 30: Ooo00oOo00o / O0 * OOooOOo * O0oO + OoooooooOO * oO0o0ooO0
elif Ii1iI111 == 41 :
 oOOOo ( OO0oooOO )
 if 23 - 23: o0000oOoOoO0o
elif Ii1iI111 == 39 :
 iI ( iIiIIi1 )
 if 36 - 36: IIII . oO0o0ooO0 - i1IIi + O0oO
elif Ii1iI111 == 45 :
 TEXTS ( )
 if 54 - 54: OoooooooOO . OoOO - oO0o0ooO0
elif Ii1iI111 == 46 :
 i11ii111i1ii ( )
 if 76 - 76: O0oO
elif Ii1iI111 == 47 :
 GEVID ( )
 if 61 - 61: o0oO0 / OoOoOO00 * o0oO0 * I1IiI * O0oO . i11iIiiIii
elif Ii1iI111 == 48 :
 OooOo0ooo ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 26 - 26: O0oO / o0oO0 - Ooo00oOo00o . iIii1I11I1II1
elif Ii1iI111 == 49 :
 oooooOoo0ooo ( )
 if 83 - 83: o0oO0 % o00O0oo / Oo - oO0o0ooO0 / O0
elif Ii1iI111 == 222 :
 iI1iIiiI ( iIiIIi1 )
 if 97 - 97: iIii1I11I1II1 * o0000oOoOoO0o
elif Ii1iI111 == 333 :
 i1i1Ii1IiIII ( iIiIIi1 )
 if 95 - 95: Ooo00oOo00o
 if 68 - 68: iIii1I11I1II1 . iIii1I11I1II1 / I1IiI - OoOoOO00 - iIii1I11I1II1
elif Ii1iI111 == 1001 :
 iiIIIIiii ( )
 if 75 - 75: o0oO0 . OOOo0 * OoOoOO00
elif Ii1iI111 == 1005 :
 oo00ooOooO ( )
 if 99 - 99: iIii1I11I1II1 * ii11ii1ii + IIII
elif Ii1iI111 == 1007 :
 ooIi111iII ( iIiIIi1 )
 if 70 - 70: i1IIi % o0oO0 . ii11ii1ii - IIII + OoOO0ooOOoo0O
elif Ii1iI111 == 1010 :
 o0o00OoO0 ( iIiIIi1 )
 if 84 - 84: OoOO + OoOoOO00 * OoOoOO00 % OOooOOo / oO0o0ooO0 + o0oO0
elif Ii1iI111 == 1011 :
 O00Oo ( iIiIIi1 )
 if 9 - 9: oO0o0ooO0
elif Ii1iI111 == 1030 :
 OO000OO ( )
 if 25 - 25: OoOO0ooOOoo0O - o00O0oo . o0000oOoOoO0o
elif Ii1iI111 == 1031 :
 O00o0000OO ( iIiIIi1 , i1iIIIi1i )
 if 57 - 57: OOooOOo + Oo * ii11ii1ii - o0oO0 % iIii1I11I1II1 - o00O0oo
elif Ii1iI111 == 1006 :
 Parse . ParseURL ( iIiIIi1 )
 if 37 - 37: Ooo00oOo00o * o0000oOoOoO0o + o00O0oo + ii11ii1ii * OOooOOo
elif Ii1iI111 == 2030 :
 Parse . addonParseURL ( iIiIIi1 )
 if 95 - 95: o00O0oo - i11iIiiIii % i11iIiiIii - O0 * O0oO
elif Ii1iI111 == 2031 :
 Parse . apkParseURL ( iIiIIi1 )
 if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
elif Ii1iI111 == 1002 :
 O0O0O ( iIiIIi1 )
 if 100 - 100: i1IIi % o00O0oo
elif Ii1iI111 == 1003 :
 II1io0Oo00oOO ( iIiIIi1 , i1iIIIi1i )
 if 55 - 55: OOOo0 + oO0o0ooO0
elif Ii1iI111 == 1004 :
 O0oo ( iIiIIi1 )
 if 85 - 85: OoOO + oO0o0ooO0 % oO0o0ooO0 / o0000oOoOoO0o . OOOo0 - I1IiI
elif Ii1iI111 == 1008 :
 i1iI1i ( )
 if 19 - 19: o0000oOoOoO0o / oO0o0ooO0 + IIII
elif Ii1iI111 == 1009 :
 M3UPLAY ( iIiIIi1 )
 if 76 - 76: iIii1I11I1II1 / O0oO - ii11ii1ii % OOooOOo % OoOO0ooOOoo0O + OoooooooOO
elif Ii1iI111 == 2001 :
 III1iiiII1ii ( iIiIIi1 )
 if 10 - 10: Ooo00oOo00o * o0000oOoOoO0o / Oo - O0oO
elif Ii1iI111 == 1013 :
 IIIIiII1i ( )
 if 11 - 11: IIII % ii11ii1ii / o0oO0 . i11iIiiIii + OoOO0ooOOoo0O - OoOoOO00
elif Ii1iI111 == 1014 :
 oo00o0 ( )
 if 50 - 50: i1IIi * OoOO / i11iIiiIii / i11iIiiIii / OoOO
elif Ii1iI111 == 1015 :
 I1IiII1iI1 ( iIiIIi1 )
 if 84 - 84: ii11ii1ii - oO0o0ooO0 + ii11ii1ii
elif Ii1iI111 == 1016 :
 II1i ( iIiIIi1 )
 if 63 - 63: o0000oOoOoO0o * o0oO0 % OoOoOO00 % O0oO + OOOo0 * Oo
elif Ii1iI111 == 1023 :
 O00Oo000ooO0 ( )
 if 96 - 96: IIII
elif Ii1iI111 == 1024 :
 II11IiIIiiI ( )
 if 99 - 99: iIii1I11I1II1 - o0oO0
elif Ii1iI111 == 1025 :
 OOo0oOOOOoo0 ( iIiIIi1 )
 if 79 - 79: OOOo0 + OoOO % o0000oOoOoO0o % OoOO
elif Ii1iI111 == 4001 :
 ooo ( )
 if 56 - 56: ii11ii1ii + OoOO . Ooo00oOo00o + OoooooooOO * ii11ii1ii - O0
elif Ii1iI111 == 4002 :
 ii1I1i1I ( )
 if 35 - 35: OoOO0ooOOoo0O . o0000oOoOoO0o . O0oO - o0000oOoOoO0o % o0000oOoOoO0o + O0oO
elif Ii1iI111 == 4003 :
 I1III ( )
 if 99 - 99: OOooOOo + OoOO0ooOOoo0O
elif Ii1iI111 == 3000 :
 O0oO0oo0O ( )
 if 34 - 34: O0oO * OOooOOo . OOOo0 % i11iIiiIii
elif Ii1iI111 == 404 :
 iiIIIi1i ( oOO00Oo , iIiIIi1 , i1iIIIi1i )
 if 61 - 61: iIii1I11I1II1 + OoOO * o0000oOoOoO0o - i1IIi % OoOO
elif Ii1iI111 == 7030 :
 O0OooOO ( )
 if 76 - 76: OoOO / I1IiI
elif Ii1iI111 == 7021 :
 o0OOOOOo0 ( oOO00Oo )
 if 12 - 12: O0oO
elif Ii1iI111 == 7022 :
 OO00Oo00oO ( oOO00Oo )
 if 58 - 58: Ooo00oOo00o + iIii1I11I1II1 % O0 + o0000oOoOoO0o + I1IiI * OoooooooOO
elif Ii1iI111 == 7000 :
 Ii1iIII11iIIi ( oOO00Oo , iIiIIi1 , img )
 if 41 - 41: OoOO * OOOo0
elif Ii1iI111 == 7050 :
 oOoO0OOO00O ( )
 if 76 - 76: OoOO . O0 * OoooooooOO + o0oO0
elif Ii1iI111 == 7051 :
 OoOO00 ( iIiIIi1 )
 if 53 - 53: Oo
elif Ii1iI111 == 7060 :
 iIII11Iiii1 ( )
 if 3 - 3: IIII - OoooooooOO * OoooooooOO - OOOo0 / O0oO * ii11ii1ii
elif Ii1iI111 == 7061 :
 i1I111Ii ( iIiIIi1 )
 if 58 - 58: IIII % iIii1I11I1II1 / i11iIiiIii % OOooOOo . O0oO * oO0o0ooO0
elif Ii1iI111 == 7063 :
 o0oo0 ( iIiIIi1 )
 if 32 - 32: OoooooooOO + OOooOOo
elif Ii1iI111 == 7062 :
 O000 ( iIiIIi1 )
 if 91 - 91: o0oO0 - O0oO * O0oO
elif Ii1iI111 == 7064 :
 NATatozcat ( )
 if 55 - 55: iIii1I11I1II1 + OOOo0 - Oo
elif Ii1iI111 == 7067 :
 oOiI111I1III ( iIiIIi1 )
 if 24 - 24: Ooo00oOo00o / O0oO + oO0o0ooO0 * o0000oOoOoO0o * oO0o0ooO0
elif Ii1iI111 == 7066 :
 NATatozA ( iIiIIi1 )
 if 10 - 10: OOOo0 - ii11ii1ii - Oo - OOooOOo
elif Ii1iI111 == 7065 :
 i111IiiI1Ii ( iIiIIi1 )
 if 21 - 21: OoooooooOO + O0oO
elif Ii1iI111 == 7070 :
 iII1i1IIiI1I ( )
 if 43 - 43: i11iIiiIii . ii11ii1ii . OoOO
elif Ii1iI111 == 7071 :
 DIZIlist ( iIiIIi1 )
 if 31 - 31: o00O0oo % OOooOOo % O0oO . ii11ii1ii / OOooOOo * OoOO
elif Ii1iI111 == 7072 :
 DIZIpull ( iIiIIi1 )
 if 74 - 74: OOOo0 . o0oO0 / oO0o0ooO0 . IIII
elif Ii1iI111 == 7073 :
 WATCHDIZI ( iIiIIi1 )
 if 74 - 74: Oo / O0oO % O0oO . IIII
elif Ii1iI111 == 7002 :
 IIIiIi1iiI ( )
 if 72 - 72: i1IIi
elif Ii1iI111 == 7003 :
 I1i1I ( iIiIIi1 )
 if 21 - 21: O0oO . OoOO0ooOOoo0O / i11iIiiIii * i1IIi
elif Ii1iI111 == 7004 :
 i11Ii1iIIIIi ( iIiIIi1 )
 if 82 - 82: o0oO0 * Oo % i11iIiiIii * i1IIi . OoOO0ooOOoo0O
elif Ii1iI111 == 7020 :
 III11I11ii ( iIiIIi1 )
 if 89 - 89: IIII - i1IIi - IIII
elif Ii1iI111 == 7001 :
 i1Iiii ( )
 if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
elif Ii1iI111 == 7010 :
 oOOoOOO0oOoo ( iIiIIi1 )
 if 28 - 28: I1IiI % OoOO - OoOO0ooOOoo0O + OoOO0ooOOoo0O + OoOO / iIii1I11I1II1
elif Ii1iI111 == 7011 :
 iIII1iIi ( iIiIIi1 )
 if 91 - 91: OOOo0 / OoOoOO00 * OoOO0ooOOoo0O
elif Ii1iI111 == 7012 :
 o00o ( iIiIIi1 )
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
elif Ii1iI111 == 7013 :
 cnfTVPlay2 ( iIiIIi1 )
elif Ii1iI111 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iIiIIi1 )
elif Ii1iI111 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iIiIIi1 )
elif Ii1iI111 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oOO00Oo , iIiIIi1 , i1iIIIi1i )
elif Ii1iI111 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ii1iI111 == 7018 :
 I1i1I11111iI1 ( )
elif Ii1iI111 == 7019 :
 CNF_Studio_Indexer . List_Movies ( iIiIIi1 )
elif Ii1iI111 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iIiIIi1 )
elif Ii1iI111 == 7024 :
 CNF_Studio_Indexer . Box_Office ( iIiIIi1 )
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % o00O0oo
elif Ii1iI111 == 8000 :
 OOoOOo0 ( )
elif Ii1iI111 == 8001 :
 Ooo0OOO ( )
elif Ii1iI111 == 8002 :
 iii ( )
elif Ii1iI111 == 8003 :
 O0OoO0o ( )
elif Ii1iI111 == 8004 :
 Ii11ii1I1 ( )
elif Ii1iI111 == 8005 :
 Oo0 ( )
elif Ii1iI111 == 8006 :
 iiI1iiii1 ( oOO00Oo , iIiIIi1 )
elif Ii1iI111 == 8030 :
 O000OOOOOo ( iIiIIi1 )
elif Ii1iI111 == 8045 :
 i1II1i ( )
elif Ii1iI111 == 8046 :
 I1iIiiiI1 ( iIiIIi1 )
elif Ii1iI111 == 8047 :
 iI1IiiiIiI1Ii ( iIiIIi1 )
elif Ii1iI111 == 8040 :
 ooOO00o00 ( )
elif Ii1iI111 == 8041 :
 Ii11Iii ( iIiIIi1 )
elif Ii1iI111 == 8042 :
 Oo0o ( iIiIIi1 )
elif Ii1iI111 == 8043 :
 yt . PlayVideo ( iIiIIi1 )
elif Ii1iI111 == 8044 :
 IiI1I1I ( iIiIIi1 )
elif Ii1iI111 == 8060 :
 o0Ii1 ( )
elif Ii1iI111 == 8061 :
 o0IIIIiI11I ( iIiIIi1 )
elif Ii1iI111 == 8070 :
 i11iIIi ( )
elif Ii1iI111 == 8071 :
 O000O ( iIiIIi1 )
elif Ii1iI111 == 7080 :
 iiiIii ( iIiIIi1 )
elif Ii1iI111 == 8090 :
 iii11i1 ( )
elif Ii1iI111 == 8091 :
 i1IiI1I111iIi ( iIiIIi1 )
elif Ii1iI111 == 8092 :
 IiiIIi1 ( iIiIIi1 )
elif Ii1iI111 == 8081 :
 OOOOo000o00OO ( )
elif Ii1iI111 == 8062 :
 IiIi1I1i1II ( iIiIIi1 )
elif Ii1iI111 == 8063 :
 iiO0o0O0oo0o ( iIiIIi1 )
elif Ii1iI111 == 8050 :
 IiiiiI1i1Iii ( )
elif Ii1iI111 == 8051 :
 oo00oO0o ( iIiIIi1 )
elif Ii1iI111 == 8052 :
 OOoooO00o0oo0 ( iIiIIi1 )
elif Ii1iI111 == 8085 :
 oO0Oo ( )
elif Ii1iI111 == 8086 :
 O0OOO0 ( iIiIIi1 )
elif Ii1iI111 == 8087 :
 I1iIIIiIi1 ( iIiIIi1 )
elif Ii1iI111 == 8088 :
 IiI1 ( iIiIIi1 , oOO00Oo )
elif Ii1iI111 == 9000 :
 Oo0oOOo ( )
elif Ii1iI111 == 1111 :
 OoOOOOOoOo0 ( )
elif Ii1iI111 == 9001 :
 III1iii1i1II ( )
elif Ii1iI111 == 9002 :
 I1ii11I ( )
elif Ii1iI111 == 9003 :
 O0Oo000OO000 ( )
elif Ii1iI111 == 50 :
 o00oO0oo0OO ( iIiIIi1 )
elif Ii1iI111 == 9020 :
 iII ( )
elif Ii1iI111 == 9021 :
 I1iII ( )
elif Ii1iI111 == 9022 :
 Iii1I1IIII ( )
elif Ii1iI111 == 9023 :
 OooooOoO ( )
elif Ii1iI111 == 9024 :
 oO0O0o0O ( iIiIIi1 )
elif Ii1iI111 == 9030 :
 iIi1 ( iIiIIi1 )
elif Ii1iI111 == 9031 :
 ooo0Oooooo ( iIiIIi1 )
elif Ii1iI111 == 9032 :
 Ooi1IIii11i1I1 ( iIiIIi1 )
elif Ii1iI111 == 9033 :
 Ii1I1O0oo00oOOO0o ( iIiIIi1 )
elif Ii1iI111 == 7085 :
 OOoooOoO0 ( iIiIIi1 )
elif Ii1iI111 == 7086 :
 iIiIi1IiIi1iI ( iIiIIi1 )
elif Ii1iI111 == 7087 :
 Ii1iiI1 ( i1iI11i1ii11 )
elif Ii1iI111 == 9666 :
 IiIIii ( iIiIIi1 )
elif Ii1iI111 == 10000 : IIii1Ii1 ( )
elif Ii1iI111 == 10001 : iiiII ( )
elif Ii1iI111 == 10002 : I1IiIii11I ( )
elif Ii1iI111 == 10003 : IIi1ii1Ii ( )
elif Ii1iI111 == 10004 : Ii11 ( )
elif Ii1iI111 == 10005 : OOoo ( )
elif Ii1iI111 == 10006 : O0O0Oo00 ( iIiIIi1 )
elif Ii1iI111 == 10007 : oOoOO ( iIiIIi1 , i1iIIIi1i )
elif Ii1iI111 == 10008 : iIiIi1iI11iiI ( )
elif Ii1iI111 == 10009 : oo0iIiI ( )
elif Ii1iI111 == 10010 : oo0i1iIIi1II1iiI ( iIiIIi1 )
elif Ii1iI111 == 10011 : o0OO0O0OO0oO0 ( iIiIIi1 )
elif Ii1iI111 == 10012 : OOOO0O00o ( iIiIIi1 )
elif Ii1iI111 == 10013 : ooo0oo00O00oO ( iIiIIi1 )
elif Ii1iI111 == 10014 : ooo000ooO0000 ( )
elif Ii1iI111 == 10015 : O000OOO0OOo ( )
elif Ii1iI111 == 10016 : OO0ooo0o0O0Oooooo ( iIiIIi1 )
elif Ii1iI111 == 10017 : IiII ( )
elif Ii1iI111 == 10018 : OOOooo0OooOoO ( )
elif Ii1iI111 == 10019 : I11iIiI1 ( )
elif Ii1iI111 == 10020 : OOO ( )
elif Ii1iI111 == 10021 : IIioo0OO ( )
elif Ii1iI111 == 10022 : oOoOoO000OO ( iIiIIi1 )
elif Ii1iI111 == 10023 : i11I1I1iiI ( oOO00Oo , iIiIIi1 )
elif Ii1iI111 == 10024 : O0oOoOOO0OO ( iIiIIi1 )
elif Ii1iI111 == 10025 : oOOoOo ( )
elif Ii1iI111 == 10026 : O00oO ( )
elif Ii1iI111 == 10027 : OOOoO000 ( )
elif Ii1iI111 == 10028 : oOOoo0o0OOOO ( )
elif Ii1iI111 == 10029 : oOO0 ( )
elif Ii1iI111 == 423 : OOOoO ( iIiIIi1 )
elif Ii1iI111 == 426 : ooo0o0O0o ( iIiIIi1 )
elif Ii1iI111 == 10030 : II1IIiiIiI ( )
elif Ii1iI111 == 10031 : Latest_Izle_Movies ( )
elif Ii1iI111 == 10032 : ii1iIi1iIiI1i ( )
elif Ii1iI111 == 10033 : iII111i ( )
elif Ii1iI111 == 10034 : Ii1ii1IiIII ( )
elif Ii1iI111 == 10035 : i1iiiii1 ( )
elif Ii1iI111 == 10036 : ooo0o00 ( iIiIIi1 )
elif Ii1iI111 == 10037 : IIIIIo0ooOoO000oO ( iIiIIi1 )
elif Ii1iI111 == 10038 : o0o00 ( )
elif Ii1iI111 == 10039 : ooOOo00O00Oo ( iIiIIi1 )
elif Ii1iI111 == 10040 : I111I11I111 ( )
elif Ii1iI111 == 10041 : oo000o0 ( iIiIIi1 )
elif Ii1iI111 == 10042 : Ii1IIi ( iIiIIi1 )
elif Ii1iI111 == 10043 : i1iIIIIIIiII1 ( )
elif Ii1iI111 == 10044 : ii1IiIi11 ( iIiIIi1 )
elif Ii1iI111 == 10045 : iIIIiiiI11I ( oOO00Oo )
elif Ii1iI111 == 10046 : i1iiIIi11I ( iIiIIi1 )
elif Ii1iI111 == 10047 : iii1III1i ( iIiIIi1 )
elif Ii1iI111 == 10048 : o0OO0Oo ( iIiIIi1 )
elif Ii1iI111 == 10049 : iiiiI1iiiIi ( iIiIIi1 )
elif Ii1iI111 == 10050 : O00OOoo000o ( )
elif Ii1iI111 == 10051 : OoO00OOoOOOo0 ( )
elif Ii1iI111 == 10052 : o0o000o ( )
elif Ii1iI111 == 10053 : Addon ( iIiIIi1 )
elif Ii1iI111 == 10054 : I1IiO00Ooo0ooo0 ( iIiIIi1 , oOO00Oo )
elif Ii1iI111 == 10055 :
 O00o00O ( "addFavorite" )
 try :
  oOO00Oo = oOO00Oo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOO00Oo = oOO00Oo . split ( '  - ' ) [ 0 ]
 except :
  pass
 Iii ( oOO00Oo , iIiIIi1 , i1iIIIi1i , iI1iIIiiii , II11I )
elif Ii1iI111 == 10056 :
 O00o00O ( "rmFavorite" )
 try :
  oOO00Oo = oOO00Oo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOO00Oo = oOO00Oo . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0O0o0o0o ( oOO00Oo )
elif Ii1iI111 == 10057 :
 O00o00O ( "getFavorites" )
 IiiIIIII1iii ( )
elif Ii1iI111 == 10058 : Ii11iII1 ( )
elif Ii1iI111 == 20000 : o0OOOOooo ( )
elif Ii1iI111 == 20001 : o0OOo0o0O0O ( )
elif Ii1iI111 == 20002 : O0O0o0oOOO ( iIiIIi1 )
elif Ii1iI111 == 20003 : OooooO0oOOOO ( iIiIIi1 )
elif Ii1iI111 == 20004 : o00O ( iIiIIi1 )
if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
