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
O0OoO000O0OO = "2.4.5"
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
 xbmcplugin . setContent ( O0O , 'movies' )
 if 13 - 13: o0oO0 / oO0o0ooO0 * Ooo00oOo00o . Ooo00oOo00o * o0oO0
def O00oO ( ) :
 IiII1II11I ( 'Search Pandoras Films' , '' , 10027 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 IiII1II11I ( 'Search Pandoras TV' , '' , 10028 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 if 40 - 40: I1IiI / IIII
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
    xbmcplugin . setContent ( O0O , 'movies' )
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
    xbmcplugin . setContent ( O0O , 'movies' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 9 - 9: OOOo0 % OOOo0 % OoOoOO00
    if 30 - 30: IIII + O0oO - IIII . IIII - OoOoOO00 + O0
def oOO0 ( ) :
 if 46 - 46: o00O0oo % I1IiI
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , ii11ii11 , iIiIIi1 , I11iIiI1I1i11 , iI1iIIiiii , Ii1iI111 in iiIi1IIiIi :
  IiII1II11I ( oOO00Oo , iIiIIi1 , Ii1iI111 , I11iIiI1I1i11 , iI1iIIiiii , ii11ii11 )
  if 64 - 64: i11iIiiIii - OoOoOO00
def oO0oOOO0Ooo ( url ) :
 if 38 - 38: OOOo0
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOo0OoOOo0 = ( '%s%s' % ( iII11I1Ii1 , url ) )
 OOooOO000 = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooOO000 )
 for url , i1iIIIi1i , ii11ii11 , o0o0 , oOO00Oo in iiIi1IIiIi :
  i1i1IIiiIIi1I ( oOO00Oo , url , 222 , i1iIIIi1i , o0o0 , ii11ii11 )
  if 59 - 59: OoOO0ooOOoo0O + i11iIiiIii
  iI1 ( 'tvshows' , 'Media Info 3' )
  if 88 - 88: i11iIiiIii - o0oO0
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 67 - 67: OoOO0ooOOoo0O . Oo + I1IiI - OoooooooOO
  if 70 - 70: OoOO0ooOOoo0O / OoOoOO00 - iIii1I11I1II1 - oO0o0ooO0
def Iii ( url ) :
 if 20 - 20: OOooOOo / i1IIi
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , ii11ii11 , url , I11iIiI1I1i11 , iI1iIIiiii , Ii1iI111 in iiIi1IIiIi :
  IiII1II11I ( oOO00Oo , url , Ii1iI111 , I11iIiI1I1i11 , iI1iIIiiii , ii11ii11 )
  if 71 - 71: I1IiI . i1IIi
 iI1 ( 'tvshows' , 'Media Info 3' )
 if 94 - 94: OoOO0ooOOoo0O . O0oO
 if 84 - 84: O0 . o0000oOoOoO0o - OoOoOO00 . o0oO0 / OoOoOO00
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: OoooooooOO
def i1i1IIiiIIi1I ( name , url , mode , iconimage , fanart , description ) :
 if 4 - 4: OOOo0 % o0000oOoOoO0o
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o0 = True
 iiI11I1i1i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiI11I1i1i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiI11I1i1i1iI . setProperty ( "Fanart_Image" , fanart )
 oOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = iiI11I1i1i1iI , isFolder = False )
 return oOO0o0
 if 60 - 60: OoooooooOO % Oo + OoOO0ooOOoo0O . o0oO0 * iIii1I11I1II1
def IiII1II11I ( name , url , mode , iconimage , fanart , description ) :
 if 93 - 93: Ooo00oOo00o
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o0 = True
 iiI11I1i1i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiI11I1i1i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiI11I1i1i1iI . setProperty ( "Fanart_Image" , fanart )
 oOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = iiI11I1i1i1iI , isFolder = True )
 return oOO0o0
if 5 - 5: o0000oOoOoO0o / OoOO0ooOOoo0O
if 77 - 77: o0oO0 - OOOo0 % o0000oOoOoO0o - O0
if 67 - 67: OoOO0ooOOoo0O + Oo
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
def OO000o00 ( string ) :
 if o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 46 - 46: Ooo00oOo00o
def O0000 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 ooO00O0O0 = [ ]
 try :
  if 33 - 33: Oo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  OO000o00 ( 'Making Favorites File' )
  ooO00O0O0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iiIiIIIiiI = open ( I11i1 , "w" )
  iiIiIIIiiI . write ( json . dumps ( ooO00O0O0 ) )
  iiIiIIIiiI . close ( )
 else :
  OO000o00 ( 'Appending Favorites' )
  iiIiIIIiiI = open ( I11i1 ) . read ( )
  II11i11Iii = json . loads ( iiIiIIIiiI )
  II11i11Iii . append ( ( name , url , iconimage , fanart , mode ) )
  iiI1IIIi = open ( I11i1 , "w" )
  iiI1IIIi . write ( json . dumps ( II11i11Iii ) )
  iiI1IIIi . close ( )
  if 68 - 68: OoooooooOO % OoOoOO00
  if 26 - 26: OoOoOO00 % i11iIiiIii % iIii1I11I1II1 % o0000oOoOoO0o * o0000oOoOoO0o * ii11ii1ii
def IiI1I11iIii ( ) :
 O000O0OO00oo = json . loads ( open ( I11i1 ) . read ( ) )
 oOOO = len ( O000O0OO00oo )
 for ooo0oooo0 in O000O0OO00oo :
  oOO00Oo = ooo0oooo0 [ 0 ]
  iIiIIi1 = ooo0oooo0 [ 1 ]
  i1iIIIi1i = ooo0oooo0 [ 2 ]
  try :
   OOO0ooo = ooo0oooo0 [ 3 ]
   if OOO0ooo == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    OOO0ooo = i1iIIIi1i
   else :
    OOO0ooo = iI1iIIiiii
  try : IIiiii = ooo0oooo0 [ 5 ]
  except : IIiiii = None
  try : iI111i1I1II = ooo0oooo0 [ 6 ]
  except : iI111i1I1II = None
  if 96 - 96: O0oO / Oo * OoOoOO00 - oO0o0ooO0 * Oo
  if ooo0oooo0 [ 4 ] == 0 :
   IIIII ( oOO00Oo , iIiIIi1 , '' , i1iIIIi1i , iI1iIIiiii , '' , 'fav' )
  else :
   IIIII ( oOO00Oo , iIiIIi1 , ooo0oooo0 [ 4 ] , i1iIIIi1i , iI1iIIiiii , '' , 'fav' )
   if 81 - 81: IIII . OOooOOo / O0oO
def Iii111Ii ( name ) :
 II11i11Iii = json . loads ( open ( I11i1 ) . read ( ) )
 for O0O00oOooo0OO in range ( len ( II11i11Iii ) ) :
  if II11i11Iii [ O0O00oOooo0OO ] [ 0 ] == name :
   del II11i11Iii [ O0O00oOooo0OO ]
   iiI1IIIi = open ( I11i1 , "w" )
   iiI1IIIi . write ( json . dumps ( II11i11Iii ) )
   iiI1IIIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 23 - 23: OoOO + Ooo00oOo00o
 if 2 - 2: OoOO - o00O0oo - o0000oOoOoO0o - O0oO . iIii1I11I1II1
 if 79 - 79: o00O0oo . Ooo00oOo00o
def IIiI1I1 ( ) :
 if 15 - 15: o00O0oo * Oo % ii11ii1ii * iIii1I11I1II1 - i11iIiiIii
 IIIII ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 if 60 - 60: OOOo0 * O0oO % Ooo00oOo00o + OoOO
def o0oo ( ) :
 if 80 - 80: O0oO * I1IiI * OoOoOO00 - O0 . I1IiI % OOOo0
 OOooooO0Oo = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIi1IIiIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , II1 in iiIi1IIiIi :
  IIIII ( oOO00Oo + '  -  ' + ( II1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIiIIi1 , 10023 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 32 - 32: OOOo0 - ii11ii1ii - Oo
  if 32 - 32: i1IIi . o0000oOoOoO0o / Ooo00oOo00o
  if 85 - 85: o0000oOoOoO0o
def ooOoO0 ( ) :
 if 86 - 86: OOooOOo
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
 if 27 - 27: O0 . OOooOOo . ii11ii1ii . ii11ii1ii + ii11ii1ii * OOooOOo
def oOo00oOOOOO ( url ) :
 OoOOo0O00 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 OOoOoOo = cloudflare . source ( OoOOo0O00 )
 iiIi1IIiIi = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 10022 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 49 - 49: I1IiI / Oo . i11iIiiIii
  if 21 - 21: I1IiI + i11iIiiIii + OOOo0 * OOooOOo % oO0o0ooO0 % OoOoOO00
  if 55 - 55: Oo - OoOO0ooOOoo0O
  if 84 - 84: O0oO + Oo - I1IiI * I1IiI
def OoooO0o ( ) :
 if 24 - 24: I1IiI % i1IIi + oO0o0ooO0 . i11iIiiIii . ii11ii1ii
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 OOoOoOo = cloudflare . source ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if iIIiiiI in oOO00Oo . lower ( ) :
   IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10022 , iIii1 + 'dtv.png' )
   if 17 - 17: ii11ii1ii . OoOoOO00 . o0oO0 / ii11ii1ii
   if 57 - 57: o0000oOoOoO0o
   if 67 - 67: Ooo00oOo00o . o0oO0
def oO00oOo0OOO ( url ) :
 OOoOoOo = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( OOoOoOo )
 for IiiiI , ii1 , ooOoOoOoO000OO , oOO00Oo in iiIi1IIiIi :
  ii11II11 = ( ooOoOoOoO000OO ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOo = ( ii1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOo00OooO0oO = 'Season ' + oOo + 'Episode ' + ii11II11 + oOO00Oo
  I1IIi ( oOo00OooO0oO , IiiiI )
  if 69 - 69: o00O0oo + Oo + OoOoOO00 - OOOo0 / o0000oOoOoO0o
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 74 - 74: o0000oOoOoO0o - OoOO0ooOOoo0O + i1IIi . OOOo0 + OoOO0ooOOoo0O - o0000oOoOoO0o
  if 17 - 17: O0 . O0oO . O0 + O0 / Oo . o0oO0
def I1IIi ( name , url ) :
 IiiiI = url
 OO00OOoO0o = name
 Iiiiiii1 = cloudflare . source ( IiiiI )
 iiii111II = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Iiiiiii1 )
 for i11IIIiI1I , Oooo0 in iiii111II :
  i1II1 ( '[COLORgreen]' + OO00OOoO0o + Oooo0 + '[/COLOR]' , i11IIIiI1I , 10012 , iIii1 + 'dtv.png' )
  if 78 - 78: ii11ii1ii + o0000oOoOoO0o - O0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: O0oO % OOOo0
 if 97 - 97: OoooooooOO - O0oO
def oooo00 ( ) :
 if 96 - 96: ii11ii1ii % o0oO0 % o00O0oo - o0oO0 % I1IiI + ii11ii1ii
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
 IIIII ( '[COLORgreen]Series[/COLOR]' , 'http://www.watchseries.li/series' , 10041 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 IIIII ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 IIIII ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 IIIII ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 if 31 - 31: Oo - O0 % I1IiI % OoOO
 if 45 - 45: ii11ii1ii + OoOoOO00 * i11iIiiIii
def IiIIi1I1I11Ii ( url ) :
 OOoOoOo = OOoOoo ( url )
 oOOO00o000o = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( OOoOoOo )
 iiIi1IIiIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( oOOO00o000o ) )
 for url , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 64 - 64: OoooooooOO
def oO0oooooo ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 65 - 65: IIII + Oo
def Ooo0O0 ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OOoOoOo )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 71 - 71: OoooooooOO
  if 11 - 11: IIII
def o0oooO ( ) :
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo = 'http://www.watchseries.li/search/' + iIIiiiI . replace ( ' ' , '%20' )
 OOoOoOo = OOoOoo ( ooOo )
 iiIi1IIiIi = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'watch online' in oOO00Oo :
   pass
  else :
   IIIII ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.watchseries.li' + iIiIIi1 , 10044 , I11iIiI1I1i11 , '' , '' )
   if 84 - 84: OoOO0ooOOoo0O
   xbmcplugin . setContent ( O0O , 'movies' )
   if 87 - 87: o0oO0 + OOooOOo
def i1iIIIIIIiII1 ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , url , oOO00Oo , ooOoOoOoO000OO , ii11ii11 in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( ooOoOoOoO000OO ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , I11iIiI1I1i11 , '' , ii11ii11 )
  if 45 - 45: OOOo0 / oO0o0ooO0 . oO0o0ooO0
def i1oO ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OOoOoOo )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 30 - 30: Oo . Ooo00oOo00o
def o0Oii1111i ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( OOoOoOo )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , I11iIiI1I1i11 , '' , '' )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 75 - 75: IIII + OoOoOO00 / OoOO - OoOO / OoooooooOO
  if 2 - 2: OOooOOo
def i11ii ( url ) :
 OOoOoOo = OOoOoo ( url )
 oOOO00o000o = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for ii1 , i1OO0oOOoo in oOOO00o000o :
  iiIi1IIiIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( i1OO0oOOoo ) )
  for url , oOO00Oo in iiIi1IIiIi :
   IIIII ( '[COLORgreen]' + ii1 + ' ' + ( oOO00Oo ) . replace ( '' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOoOo )
 for url in iiii111II :
  IIIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 50 - 50: o00O0oo / I1IiI * o00O0oo
  if 34 - 34: O0 * O0 % OoooooooOO + oO0o0ooO0 * iIii1I11I1II1 % o00O0oo
def I1iI1I1 ( url ) :
 IiIi1 = [ oo00ooOoo ( url ) for iii1IIIiiiI in xrange ( 1 ) ]
 OoO00oo00 = [ ]
 if 76 - 76: OoooooooOO + Oo % IIII . Ooo00oOo00o + OoOoOO00
 for ooo0oooo0 in xrange ( len ( IiIi1 ) ) :
  oO0o = IiIi1 [ ooo0oooo0 ]
  OoO00oo00 . append ( Thread ( target = oo00ooOoo ( url ) , args = ( oO0o , ) , kwargs = { } ) )
  OoO00oo00 [ ooo0oooo0 ] . start ( )
  if 84 - 84: O0 - OoOoOO00 . Oo / OoOO . OoooooooOO + i11iIiiIii
 for O0OO in OoO00oo00 : O0OO . join ( )
 if 39 - 39: ii11ii1ii + OOOo0 - iIii1I11I1II1 - OOooOOo
 if 7 - 7: IIII . I1IiI / ii11ii1ii . OoOO0ooOOoo0O * o0000oOoOoO0o - OoOoOO00
def oo00ooOoo ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1111 . create ( '' , '' , '' )
  OoOOo0O00 = OoOOo0O00 = 'http://www.watchseries.li/link/' + url
  if 'allmyvideos' in oOO00Oo :
   I1ii1iI1II11ii ( OoOOo0O00 )
   i1111 . update ( 15 , "Please Wait" , "Getting Allmyvideos Streams" )
  elif 'vidspot' in oOO00Oo :
   I1ii1iI1II11ii ( OoOOo0O00 )
   i1111 . update ( 30 , "Please Wait" , "Getting Vidspot Streams" )
  elif 'thevideo' in oOO00Oo :
   I1ii1iI1II11ii ( OoOOo0O00 )
   i1111 . update ( 45 , "Please Wait" , "Getting Thevideo Streams" )
  elif 'daclips' in oOO00Oo :
   I1ii1iI1II11ii ( OoOOo0O00 )
   i1111 . update ( 60 , "Please Wait" , "Getting Daclips Streams" )
  elif 'vodlocker' in oOO00Oo :
   I1ii1iI1II11ii ( OoOOo0O00 )
   i1111 . update ( 80 , "Please Wait" , "Getting Vodlocker Streams" )
  elif 'filehoot' in oOO00Oo :
   I1ii1iI1II11ii ( OoOOo0O00 )
   i1111 . update ( 100 , "Please Wait" , "Getting Filehoot Streams" )
  else :
   pass
   if 8 - 8: o0oO0 * O0
   if 73 - 73: OOooOOo / OoOO / o0000oOoOoO0o / Ooo00oOo00o
   if 11 - 11: I1IiI + IIII - OoooooooOO / Ooo00oOo00o
def I1ii1iI1II11ii ( url ) :
 OOoOoOo = OOoOoo ( url )
 oO00O0 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( OOoOoOo )
 iiii111II = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( OOoOoOo )
 iiIi1IIiIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( OOoOoOo )
 for url in oO00O0 :
  iIIi1iI1I1IIi ( url )
 for url in iiii111II :
  iIIi1iI1I1IIi ( url )
 for url in iiIi1IIiIi :
  iIIi1iI1I1IIi ( url )
  if 77 - 77: o0oO0 / Oo + o0oO0 % OOooOOo - OOOo0 * OOOo0
def iIIi1iI1I1IIi ( url ) :
 if 'daclips.in' in url :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( OOoOoOo )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]DACLIPS[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'filehoot.com' in url :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OOoOoOo )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]FILEHOOT[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'thevideo.me' in url :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( OOoOoOo )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]THEVIDEO[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'allmyvideos.net' in url :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OOoOoOo )
  for url , oOO00Oo in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]ALLMYVIDEOS - ' + oOO00Oo + '[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'vidspot.net' in url :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( OOoOoOo )
  for url , oOO00Oo in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]VIDSPOT - ' + oOO00Oo + '[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'vodlocker' in url :
  OOoOoOo = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OOoOoOo )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]VODLOCKER[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
if 23 - 23: oO0o0ooO0 . OoOoOO00 % ii11ii1ii - OoooooooOO * Oo . iIii1I11I1II1
if 37 - 37: oO0o0ooO0 / Oo . o0000oOoOoO0o * o0000oOoOoO0o
if 80 - 80: OoOO0ooOOoo0O % ii11ii1ii
if 91 - 91: o0000oOoOoO0o / O0 - o00O0oo . OOOo0
if 82 - 82: IIII * OoOO0ooOOoo0O / OoOO
if 2 - 2: OOOo0 + OOooOOo . OOooOOo . O0 / o0000oOoOoO0o
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
def ooooOoO0O ( ) :
 IIIII ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 if 1 - 1: ii11ii1ii / Ooo00oOo00o + OoOO . OOooOOo / ii11ii1ii - oO0o0ooO0
def ii111i1iI ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iiIi1IIiIi = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  IIIII ( '[COLORgreen]' + ( oOO00Oo ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIiIIi1 , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I11iIiI1I1i11 , iI111I11I1I1 , '' )
  if 18 - 18: OoOO0ooOOoo0O - o00O0oo - I1IiI / O0oO - O0
def iiIIii ( url ) :
 OOoOoOo = OOoOoo ( url )
 oOOO00o000o = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( OOoOoOo )
 for oOOO00o000o in oOOO00o000o :
  oO0Oo0O0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( oOOO00o000o ) )
  for I1iIiI1IiIIII in oO0Oo0O0 :
   I1iIiI1IiIIII = I1iIiI1IiIIII
  I1iiIi111I = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( oOOO00o000o ) )
  for Iiii1iIii , I11iIiI1I1i11 , time , oOoooO000O in I1iiIi111I :
   III1I11i1iIi = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oOoooO000O )
   IIIII ( '[COLORgreen]' + I1iIiI1IiIIII + ' - ' + Iiii1iIii + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I11iIiI1I1i11 , iI111I11I1I1 , ( str ( III1I11i1iIi ) ) )
   if 69 - 69: Oo * OoOoOO00 * o0oO0 . oO0o0ooO0 - ii11ii1ii
 iI1 ( 'tvshows' , 'Media Info 3' )
 if 39 - 39: o00O0oo * OOOo0 % Ooo00oOo00o . I1IiI
def iiii111IiIIi1 ( ) :
 if 74 - 74: iIii1I11I1II1 % oO0o0ooO0 * OoOO0ooOOoo0O * iIii1I11I1II1
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
 if 73 - 73: OOooOOo % O0oO . OoOO0ooOOoo0O
def ooOOoOo ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  oooO = oOO00Oo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  i1II1 ( '[COLORgreen]' + oooO + '[/COLOR]' , url , 10013 , I11iIiI1I1i11 )
  if 12 - 12: OoOoOO00
def IiIii1ii ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( OOoOoOo )
 for i11IIIiI1I in iiIi1IIiIi :
  IIiI1i = ( i11IIIiI1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOO0O00o ( 'http:' + IIiI1i )
  if 6 - 6: ii11ii1ii / oO0o0ooO0 - OoOO0ooOOoo0O
  if 62 - 62: o0000oOoOoO0o % OoOO0ooOOoo0O
def OOo00OO00Oo ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 8046 , iIii1 + 'documentary.png' )
def I1I1I11Ii ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( 'NEXT PAGE' , url , 8046 , iIii1 + 'documentary.png' )
  if 48 - 48: OoooooooOO + OoOO % iIii1I11I1II1
def IiI1IIIII1I ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  yt . PlayVideo ( url )
  if 35 - 35: o00O0oo - o00O0oo + i1IIi - O0 - O0oO
def oOO0o0oo0 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 8041 , iIii1 + 'documentary.png' )
def oOo000O ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo ) . replace ( '&#039;s' , '' ) , url , 8042 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( 'NEXT PAGE' , url , 8041 , iIii1 + 'documentary.png' )
  if 1 - 1: iIii1I11I1II1
  if 54 - 54: OoooooooOO - OOOo0 % ii11ii1ii
def oO0Ooo0OooOOo ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , I11iIiI1I1i11 , url , o0O00oOOoo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , I11iIiI1I1i11 )
 for url in iiii111II :
  O00o0O ( ( url ) . replace ( '//' , 'http://' ) )
  if 32 - 32: OOooOOo + I1IiI - OoooooooOO
def O00o0O ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIii1 + 'documentary.png' )
  if 39 - 39: OoooooooOO * OoOO0ooOOoo0O * O0 . o0000oOoOoO0o . Ooo00oOo00o + o0oO0
def II1IIi ( ) :
 OOoOoOo = OO ( 'http://www.stream2watch.co/live-tv' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( OOoOoOo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , OOoOO0o in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo + '[COLORgreen]' + OOoOO0o + '[/COLOR]' ) , iIiIIi1 , 8086 , I11iIiI1I1i11 )
  if 51 - 51: Oo - ii11ii1ii * o0000oOoOoO0o
def ii1111Ii1i ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 8087 , I11iIiI1I1i11 )
  if 48 - 48: O0 * o00O0oo - O0 / o00O0oo + I1IiI
def oO00oo000O ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , oOO00Oo in iiIi1IIiIi :
  ii11 ( url , oOO00Oo )
  if 63 - 63: OOooOOo . IIII
def ii11 ( url , name ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( OOoOoOo )
 for url in iiIi1IIiIi :
  print url
  i1II1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 28 - 28: OoOoOO00
def ooOii1I11Iii1i ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 iiIi1IIiIi = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , time , IiIIi1II1ii , Iiii1iIii , I1iiIi111I , iIiIIi1 in iiIi1IIiIi :
  I1I11i ( ( time + '[COLORgreen]' + I1iiIi111I + '[/COLOR]' + Iiii1iIii ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , iIiIIi1 , 8061 , I11iIiI1I1i11 )
def i1II1Ii1i1 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , iIii1 + 'documentary.png' )
  if 45 - 45: OoOO0ooOOoo0O * O0oO . o0oO0 - O0oO + IIII
def iIIOOoO0oO00o ( ) :
 OOoOoOo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iIiIIi1 , 8071 , iIii1 + 'streams.png' )
def iiiiii1 ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoOoOo )
 for oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , iIii1 + 'streams.png' )
def OO0o0oO0O000o ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoOoOo )
 for I11iIiI1I1i11 , oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( ) , 222 , I11iIiI1I1i11 )
  if 47 - 47: O0oO - Ooo00oOo00o / o00O0oo * OoooooooOO / o00O0oo . Oo
def iiII1IiIi1iI1 ( ) :
 OOoOoOo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy54bnh4LmNvbS8=' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a><br>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 8091 , iIii1 + 'streams.png' )
def oOiiI1Ii11II1I ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?src="(.+?)".+?title="(.+?)">' , re . DOTALL ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 8092 , I11iIiI1I1i11 )
def I1Ii11II1I1 ( url ) :
 OOoOoOo = OO ( url )
 iiIi1IIiIi = re . compile ( 'src=&quot;(.+?)&quot;' ) . findall ( OOoOoOo )
 for url in iiIi1IIiIi :
  IiI1iI1IiiIi1 ( url )
  if 90 - 90: O0 + o0000oOoOoO0o - OoooooooOO . o0000oOoOoO0o
def oOII1ii1ii11I1 ( url ) :
 o0ooOO0o = urllib2 . Request ( url )
 o0ooOO0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 ooo0 = ''
 OOooOO000 = ''
 try :
  ooo0 = urllib2 . urlopen ( o0ooOO0o )
  OOooOO000 = ooo0 . read ( )
  ooo0 . close ( )
 except : pass
 if OOooOO000 != '' :
  return OOooOO000
 else :
  OOooOO000 = 'Failed'
  return OOooOO000
  if 46 - 46: oO0o0ooO0 - iIii1I11I1II1
def I1I1 ( ) :
 O0Oo0 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 IiiiI = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 OOooO0OO0 = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iI1iIiiiI1I1 = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 OOOO = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 OoI1IiiiIiI = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0Oo = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iIIiiiI
 I1Ii1iIiII = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 O0oOo00Ooo0o0 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9hcmFtYT9xPQ==' ) ) + iIIiiiI
 if 33 - 33: o0000oOoOoO0o
 OOoOoOo = oOII1ii1ii11I1 ( iIiIIi1 )
 Iiiiiii1 = oOII1ii1ii11I1 ( IiiiI )
 oOO0IIi1I1i = oOII1ii1ii11I1 ( OOooO0OO0 )
 Ii = oOII1ii1ii11I1 ( iI1iIiiiI1I1 )
 oO0O = oOII1ii1ii11I1 ( OOOO )
 Oo00o0O0O = oOII1ii1ii11I1 ( O0Oo )
 o0ooO0OoOo = OOoOoo ( I1Ii1iIiII )
 o0oOO00 = OOoOoo ( O0oOo00Ooo0o0 )
 if 46 - 46: i11iIiiIii - o0000oOoOoO0o
 if o0oOO00 != 'Failed' :
  oOoOo = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( o0oOO00 )
  for iIiIIi1 , I11iIiI1I1i11 , ooO , oOO00Oo in oOoOo :
   oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( ooO ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   i1iIIIi1i = I11iIiI1I1i11
   iIiIIi1 = iIiIIi1
   o0o00 ( oOO00Oo , i1iIIIi1i , iIiIIi1 )
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if OOoOoOo != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOoOoOo )
  for OoO00O0OOO , oOO00Oo in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIiIIi1 + OoO00O0OOO ) , 222 , '' )
 if Iiiiiii1 != 'Failed' :
  iiii111II = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Iiiiiii1 )
  for OoO00O0OOO , oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiiiI + OoO00O0OOO ) , 222 , '' )
 if oOO0IIi1I1i != 'Failed' :
  oO00O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oOO0IIi1I1i )
  for OoO00O0OOO , oOO00Oo in oO00O0 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OOooO0OO0 + OoO00O0OOO ) , 222 , '' )
 if Ii != 'Failed' :
  oooOo0O00o00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Ii )
  for OoO00O0OOO , oOO00Oo in oooOo0O00o00 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iI1iIiiiI1I1 + OoO00O0OOO ) , 222 , '' )
 if oO0O != 'Failed' :
  I1iIIIiIi1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0O )
  for OoO00O0OOO , I11iIiI1I1i11 , oOO00Oo in I1iIIIiIi1 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OoO00O0OOO , 1006 , 'img' )
    if 21 - 21: iIii1I11I1II1 / O0oO + o0oO0 - o0000oOoOoO0o / Oo / OoOoOO00
    iI1 ( 'tvshows' , 'Media Info 3' )
 if Oo00o0O0O != 'Failed' :
  oOI11 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Oo00o0O0O )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in oOI11 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iIiIIi1 , 7067 , I11iIiI1I1i11 )
    if 54 - 54: o00O0oo - O0oO
    iI1 ( 'tvshows' , 'Media Info 3' )
 if o0ooO0OoOo != 'Failed' :
  O0ii1ii1I1IIi1 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( o0ooO0OoOo )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in O0ii1ii1I1IIi1 :
   i1II1 ( '[COLORgreen]' + oOO00Oo + '- Source 7[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
 oOOOoo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 55 - 55: OOOo0
 if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
 for oooO0o0o0O0 in oOOOoo :
  iii11111I = O0Oo0 + oooO0o0o0O0
  II11I = oOII1ii1ii11I1 ( iii11111I )
  if oO0O != 'Failed' :
   iiiI11iIIi1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( II11I )
   for OoO00O0OOO , oOO00Oo in iiiI11iIIi1 :
    if iIIiiiI in oOO00Oo . lower ( ) :
     i1II1 ( ( '[COLORgreen]' + oOO00Oo + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0Oo0 + oooO0o0o0O0 + OoO00O0OOO ) , 222 , '' )
     if 72 - 72: oO0o0ooO0 * OoOO0ooOOoo0O
     iI1 ( 'tvshows' , 'Media Info 3' )
     if 67 - 67: i1IIi
     if 5 - 5: OoOoOO00 . OoooooooOO
def oOOOo ( ) :
 if 31 - 31: I1IiI + I1IiI . i11iIiiIii / o0oO0 % o0000oOoOoO0o / I1IiI
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 IiiiI = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 OOooO0OO0 = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iI1iIiiiI1I1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 OOOO = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 OoI1IiiiIiI = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 I1Ii1iIiII = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iIIiiiI ) . replace ( ' ' , '+' )
 O0oOo00Ooo0o0 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + iIIiiiI . replace ( ' ' , '%20' )
 if 29 - 29: ii11ii1ii * ii11ii1ii . Ooo00oOo00o * o0000oOoOoO0o % iIii1I11I1II1 * ii11ii1ii
 OOoOoOo = oOII1ii1ii11I1 ( iIiIIi1 )
 Iiiiiii1 = oOII1ii1ii11I1 ( IiiiI )
 oOO0IIi1I1i = oOII1ii1ii11I1 ( OOooO0OO0 )
 Ii = oOII1ii1ii11I1 ( iI1iIiiiI1I1 )
 oO0O = cloudflare . source ( OOOO )
 II11I = oOII1ii1ii11I1 ( OoI1IiiiIiI )
 o0ooO0OoOo = OOoOoo ( I1Ii1iIiII )
 o0oOO00 = OOoOoo ( O0oOo00Ooo0o0 )
 if OOoOoOo != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoOo )
  for oOO00Oo in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIIi1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 31 - 31: Ooo00oOo00o * O0 . OoOO
    iI1 ( 'tvshows' , 'Media Info 3' )
 if Iiiiiii1 != 'Failed' :
  iiii111II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiiiiii1 )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiiI + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 59 - 59: OoOoOO00 * i11iIiiIii
    iI1 ( 'tvshows' , 'Media Info 3' )
 if oOO0IIi1I1i != 'Failed' :
  oO00O0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOO0IIi1I1i )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOooO0OO0 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 54 - 54: O0 % OoooooooOO - OOOo0
    iI1 ( 'tvshows' , 'Media Info 3' )
 if Ii != 'Failed' :
  oooOo0O00o00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Ii )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI1iIiiiI1I1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 61 - 61: Oo * IIII . Oo + Oo / IIII * O0
    iI1 ( 'tvshows' , 'Media Info 3' )
 if oO0O != 'Failed' :
  I1iIIIiIi1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0O )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in I1iIIIiIi1 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( '[COLORgreen]' + oOO00Oo + ' - Source - Dizi[/COLOR]' , iIiIIi1 , 8062 , I11iIiI1I1i11 )
    if 73 - 73: oO0o0ooO0 * oO0o0ooO0 / o0oO0
    iI1 ( 'tvshows' , 'Media Info 3' )
 if II11I != 'Failed' :
  iiiI11iIIi1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11I )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiiI11iIIi1 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- Source Scooby[/COLOR]' ) , iIiIIi1 , 222 , 'img' )
    if 43 - 43: ii11ii1ii . i1IIi . IIII + O0 * o00O0oo * O0
    iI1 ( 'tvshows' , 'Media Info 3' )
 if o0ooO0OoOo != 'Failed' :
  O0ii1ii1I1IIi1 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( o0ooO0OoOo )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in O0ii1ii1I1IIi1 :
   i1II1 ( '[COLORgreen]' + oOO00Oo + ' - Source DiZzY[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
 if o0oOO00 != 'Failed' :
  oOoOo = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o0oOO00 )
  for I11iIiI1I1i11 , iIiIIi1 , oOO00Oo in oOoOo :
   if 'watch online' in oOO00Oo :
    pass
   else :
    IIIII ( '[COLORgreen]' + oOO00Oo + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + iIiIIi1 , 10044 , I11iIiI1I1i11 , '' , '' )
    if 41 - 41: ii11ii1ii + o00O0oo % OoooooooOO . ii11ii1ii + oO0o0ooO0 . oO0o0ooO0
    xbmcplugin . setContent ( O0O , 'movies' )
    if 31 - 31: i11iIiiIii + OoOoOO00 . oO0o0ooO0 * I1IiI
def OO0ooo0 ( ) :
 if 7 - 7: ii11ii1ii - OoOO * OoOO0ooOOoo0O + OOooOOo . ii11ii1ii
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOoOoOo = OOoOoo ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOoOoOo )
 for oOO00Oo , I11iIiI1I1i11 , ooooO in iiIi1IIiIi :
  oO0O0 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  if iIIiiiI in oOO00Oo . lower ( ) :
   I1I11i ( oOO00Oo , '' , 7022 , oO0O0 )
   if 19 - 19: o00O0oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: OoOO0ooOOoo0O % OoOO0ooOOoo0O / O0 % oO0o0ooO0 - OOooOOo . Oo
 if 49 - 49: iIii1I11I1II1 * i1IIi . OoooooooOO
def OOOO0oOo00O ( url ) :
 i1I1I1i1i1i = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( i1I1I1i1i1i )
 for url , ii1 , II1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( ii1 ) . replace ( 'Sezon' , ' Season ' ) + ( II1 ) . replace ( 'Bölüm' , ' Episode ' ) + oOO00Oo , url , 8063 , '' )
  if 23 - 23: iIii1I11I1II1
  if 8 - 8: O0 % o00O0oo % iIii1I11I1II1 . OOooOOo % O0
  if 12 - 12: OoOO0ooOOoo0O . o00O0oo
  if 79 - 79: O0oO / Oo / oO0o0ooO0 . O0oO * OoooooooOO + OOooOOo
def ooOoooo0 ( url ) :
 i1I1I1i1i1i = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i1I1I1i1i1i )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , '' )
  if 54 - 54: i1IIi . o0000oOoOoO0o - ii11ii1ii + o0oO0 + Oo / Oo
  if 22 - 22: o0oO0 . iIii1I11I1II1
  if 12 - 12: o00O0oo
  if 71 - 71: OOOo0 . OoOoOO00 . OOOo0 - o0oO0
def I1ii1 ( ) :
 if 48 - 48: o0oO0 / iIii1I11I1II1 + OoOO0ooOOoo0O + iIii1I11I1II1 . Ooo00oOo00o
 i1I1I1i1i1i = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIi1IIiIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1I1I1i1i1i )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , II1 in iiIi1IIiIi :
  I1I11i ( oOO00Oo + '  -  ' + ( II1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIiIIi1 , 8063 , I11iIiI1I1i11 )
  if 60 - 60: O0oO
def oOO0o00o0Oo0O ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 8002 , I11iIiI1I1i11 )
def iIIi1iiII ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , time , url , oOO00Oo , o0O00oOOoo in iiIi1IIiIi :
  IIIII ( '%s %s' % ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , time ) , url , 1015 , I11iIiI1I1i11 , o0O00oOOoo )
  if 14 - 14: O0
def II1iIii111iII ( ) :
 if 27 - 27: OOooOOo * i11iIiiIii * Ooo00oOo00o
 I1I11i ( 'Coronation Street' , '' , 8001 , '' )
 I1I11i ( 'Eastenders' , '' , 8002 , '' )
 I1I11i ( 'Emmerdale' , '' , 8003 , '' )
 I1I11i ( 'Hollyoaks' , '' , 8004 , '' )
 I1I11i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
 if 87 - 87: I1IiI % iIii1I11I1II1
 if 72 - 72: OoOO0ooOOoo0O . OoOO0ooOOoo0O - ii11ii1ii
 if 48 - 48: Oo - o0oO0 + Oo - OOOo0 * i11iIiiIii . oO0o0ooO0
def I1iIIIiI ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Holly' in oOO00Oo :
   I11iIiI1I1i11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 60 - 60: OOOo0 . i11iIiiIii + I1IiI / ii11ii1ii * OoOoOO00 * OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 59 - 59: Oo + oO0o0ooO0 - OoOO0ooOOoo0O . OOooOOo + OOOo0 % OoOO
def i111Iii ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'East' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 100 - 100: o0000oOoOoO0o / oO0o0ooO0 . O0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: oO0o0ooO0
def iIi1IIiIII1 ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Emmer' in oOO00Oo :
   I11iIiI1I1i11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 19 - 19: o0000oOoOoO0o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: o0oO0 / I1IiI % OOooOOo * OoOO
def oOOOoo0o ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Coro' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 44 - 44: O0 % i1IIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: OoOoOO00 - Ooo00oOo00o - OoooooooOO . oO0o0ooO0 / I1IiI
def ooooo0Oo0 ( ) :
 OOoOoOo = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( OOoOoOo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Celeb' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 97 - 97: IIII . OoOO . IIII
def oOo00o ( name , url ) :
 II111i1ii1iII = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if II111i1ii1iII :
  ooo0OoO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOooooO0Oo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OOooooO0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOooooO0Oo = open_url ( url )
  iiI1111I11i1I = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OOooooO0Oo ) [ - 1 ]
  ooo0OoO = iiI1111I11i1I . replace ( '\\/' , '/' )
 iiI11I1i1i1iI = xbmcgui . ListItem ( name , '' , '' )
 iiI11I1i1i1iI . setPath ( ooo0OoO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiI11I1i1i1iI )
 if 85 - 85: OoOO0ooOOoo0O * i1IIi % OOOo0 - o0oO0
 if 37 - 37: IIII . Oo * Oo * OoOoOO00 * O0
def o00OOo000O ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iIiIIi1 , 7071 , iIii1 + 'popcorn.png' )
 for iIiIIi1 , oOO00Oo in iiii111II :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iIiIIi1 , 7071 , iIii1 + 'popcorn.png' )
  if 42 - 42: IIII % oO0o0ooO0 % OOooOOo % OoOO + o0000oOoOoO0o % I1IiI
def iI1iIIiii ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIi1IIiIi = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Movies' in oOO00Oo :
   I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( iIiIIi1 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iIii1 + 'popcorn.png' )
def O0000oO0o00 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iIii1 + 'popcorn.png' )
  if 80 - 80: OoooooooOO + IIII
  if 95 - 95: O0oO / OoOO * O0oO - OoooooooOO * OoooooooOO % Ooo00oOo00o
def iI1I1I1i1i ( url ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I11iIiI1I1i11 )
  if 87 - 87: I1IiI / IIII . o0oO0 - OoOO0ooOOoo0O / Ooo00oOo00o
  if 41 - 41: OoOoOO00
def II1Iiii11111 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iIiI1I1i11 )
  if 26 - 26: O0
def i111I1iiIiII ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  OoO00ooO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 15 - 15: i11iIiiIii
def OoO00ooO ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 222 , iIii1 + 'popcorn' )
  if 13 - 13: o0000oOoOoO0o * OoOoOO00 * OoOO * OoOoOO00 % IIII / OOOo0
  if 100 - 100: IIII . o00O0oo - iIii1I11I1II1 . i11iIiiIii / OoOoOO00
  if 71 - 71: O0oO * Oo . o0000oOoOoO0o
  if 49 - 49: IIII * O0 . IIII
def ii1II1II ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( iIiIIi1 ) ) , 222 , I11iIiI1I1i11 )
  if 42 - 42: o00O0oo
def O0o00oo0OO0 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 iiIi1IIiIi = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + iIiIIi1 , 7051 , iIii1 + 'vod.png' )
  if 60 - 60: o0oO0
def O000O ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , iIii1 + 'vod.png' )
  if 22 - 22: OoOO
def i1i11i ( url ) :
 OOooooO0Oo = OOoOoo
 iiIi1IIiIi = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 222 , I11iIiI1I1i11 )
  if 86 - 86: o00O0oo
  if 29 - 29: iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % iIii1I11I1II1 % OoOO0ooOOoo0O
  if 84 - 84: IIII + ii11ii1ii + o00O0oo + oO0o0ooO0
  if 62 - 62: i11iIiiIii + I1IiI + i1IIi
  if 69 - 69: I1IiI
def OO0Oo ( ) :
 if 13 - 13: OOooOOo * i11iIiiIii / i11iIiiIii . Ooo00oOo00o . OoOO0ooOOoo0O . ii11ii1ii
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
 if 26 - 26: OOooOOo . iIii1I11I1II1
 if 67 - 67: Oo / O0
def oO0Oo00oo ( Cat_Name ) :
 if 75 - 75: iIii1I11I1II1 * i11iIiiIii - OoooooooOO . I1IiI
 OOOO0O00Ooooo = False
 IiIIII1iiIIi = '0'
 if Cat_Name == 'All Channels' : OOOO0O00Ooooo = True
 if Cat_Name == 'Entertainment' : IiIIII1iiIIi = '1'
 if Cat_Name == 'Movies' : IiIIII1iiIIi = '2'
 if Cat_Name == 'Music' : IiIIII1iiIIi = '3'
 if Cat_Name == 'News' : IiIIII1iiIIi = '4'
 if Cat_Name == 'Sports' : IiIIII1iiIIi = '5'
 if Cat_Name == 'Documentary' : IiIIII1iiIIi = '6'
 if Cat_Name == 'Kids' : IiIIII1iiIIi = '7'
 if Cat_Name == 'Food' : IiIIII1iiIIi = '8'
 if Cat_Name == 'Religious' : IiIIII1iiIIi = '9'
 if Cat_Name == 'USA Channels' : IiIIII1iiIIi = '10'
 if Cat_Name == 'Other' : IiIIII1iiIIi = '11'
 if 17 - 17: o0000oOoOoO0o
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 print 'Len Match: >>>' + str ( len ( iiIi1IIiIi ) )
 for oOO00Oo , I11iIiI1I1i11 , ooooO in iiIi1IIiIi :
  oO0O0 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  if ooooO == IiIIII1iiIIi :
   I1I11i ( oOO00Oo , '' , 7022 , oO0O0 )
  elif OOOO0O00Ooooo == True :
   I1I11i ( oOO00Oo , '' , 7022 , oO0O0 )
  else : pass
  if 97 - 97: ii11ii1ii * ii11ii1ii / oO0o0ooO0
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 6 - 6: OoOO
def O0OOoOOOO00O ( Search_Name ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , iIiIIi1 , IiiiI , OOooO0OO0 in iiIi1IIiIi :
  oO0O0 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  i1II1 ( Search_Name + ': Link 1' , ( iIiIIi1 ) . replace ( '\\' , '' ) , 222 , oO0O0 )
  i1II1 ( Search_Name + ': Link 2' , ( IiiiI ) . replace ( '\\' , '' ) , 222 , oO0O0 )
  i1II1 ( Search_Name + ': Link 3' , ( OOooO0OO0 ) . replace ( '\\' , '' ) , 222 , oO0O0 )
  if 72 - 72: OOOo0 + IIII . I1IiI + I1IiI
def ooooOoo0OO ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iIii1 + 'english.png' )
def Oo0 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'xxx.png' )
def O0000Oo00o ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'vod(1).png' )
  if 20 - 20: Ooo00oOo00o . OOOo0 * i11iIiiIii / i11iIiiIii
def o00iIiiiII ( url ) :
 url
 Ii1I1 = xbmcgui . ListItem ( oOO00Oo , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1I1 )
 return
 if 71 - 71: I1IiI + iIii1I11I1II1 * OoOO . O0oO % i11iIiiIii % iIii1I11I1II1
 if 63 - 63: OoooooooOO * Ooo00oOo00o / o0000oOoOoO0o - OoOO . iIii1I11I1II1 + oO0o0ooO0
def ii1IIiI1IIi ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOooooO0Oo )
 for url , ii11ii11 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  IIIII ( oOO00Oo , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , ( ii11ii11 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iI1 ( 'tvshows' , 'Media Info 3' )
 for url in iiii111II :
  I1I11i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iIii1 + 'FITNESS.png' )
  if 76 - 76: oO0o0ooO0 / Ooo00oOo00o + I1IiI
def Oooo00 ( url ) :
 OOoOoOo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( OOoOoOo )
 for url , ii11ii11 , I11iIiI1I1i11 in iiIi1IIiIi :
  O00O0oOO00O00 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , ii11ii11 )
  iI1 ( 'tvshows' , 'Media Info 3' )
 i1OO0oOOoo = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( OOoOoOo )
 for iii1II1iI1IIi in i1OO0oOOoo :
  Ii11iiI1 = ( iii1II1iI1IIi ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  IIIII ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , Ii11iiI1 )
  if 71 - 71: OOooOOo / OoOO0ooOOoo0O % OoOO0ooOOoo0O
def OoooO0 ( INFO ) :
 oooOO0oo0Oo00 ( 'info for workout' , INFO )
 if 99 - 99: O0
 if 38 - 38: i11iIiiIii + iIii1I11I1II1 - o0000oOoOoO0o / I1IiI
 if 99 - 99: ii11ii1ii * OoOO * ii11ii1ii - OoOoOO00 + o00O0oo
def OOooO0Oo00 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 9031 , iIii1 + 'icon.png' )
def iIIIIIIIiIII ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 9032 , iIii1 + 'icon.png' )
def o0oo0o00ooO00 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  if '://' in oOO00Oo :
   pass
   i1II1 ( ( oOO00Oo ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , iIii1 + 'icon.png' )
def IIiIiiI1i ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , iIii1 + 'icon.png' )
  if 49 - 49: ii11ii1ii . IIII . i1IIi * I1IiI % iIii1I11I1II1
  if 35 - 35: ii11ii1ii + O0oO - I1IiI % OoOO % OOooOOo % I1IiI
  if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
def i111I11I ( ) :
 OOooooO0Oo = OOoOoo ( 'http://tvshows.cnfstudio.com/' )
 iiIi1IIiIi = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , 'http://tvshows.cnfstudio.com/genre/' + iIiIIi1 , 7010 , iIii1 + 'icon.png' )
  print '>>>>>>>>>>' + iIiIIi1
  if 80 - 80: iIii1I11I1II1 - OoooooooOO - ii11ii1ii - ii11ii1ii . OoooooooOO
def I1i ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOooooO0Oo )
 I11I = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , I11iIiI1I1i11 )
 I11I = I11I
 for url in I11I :
  I1I11i ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  I1I11i ( 'Next' , url , 7010 , '' )
  if 81 - 81: i11iIiiIii + i11iIiiIii * Ooo00oOo00o + IIII
def iii ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , II1 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( 'Season' ) + II1 + ( '  ' ) + oOO00Oo , url , 7004 , iIii1 + 'icon.png' )
  if 15 - 15: OOOo0 . Ooo00oOo00o
def IiiIi ( url ) :
 if 42 - 42: oO0o0ooO0 + iIii1I11I1II1
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iIii1 + 'icon.png' )
  if 21 - 21: I1IiI - Oo % O0 . Ooo00oOo00o + I1IiI
def ii11iI1iIiIi ( name , url , img ) :
 OOoOoOo = OOoOoo ( url )
 o0OO0OoO0o0o0 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( OOoOoOo )
 IIIIIIi1IiIi = len ( o0OO0OoO0o0o0 )
 if 14 - 14: Ooo00oOo00o / o0oO0 - OoOO0ooOOoo0O / OOOo0
 if 27 - 27: i1IIi + OOOo0 * ii11ii1ii + OoOO0ooOOoo0O . OoOO
 if IIIIIIi1IiIi == 1 :
  for i1I111I1Iii1 in o0OO0OoO0o0o0 :
   i1I111I1Iii1 = i1I111I1Iii1 . replace ( 'player' , 'watch' )
   O00Oo0 = i1I111I1Iii1 + '&fv=&sou='
   o0Oooo0 = OOoOoo ( O00Oo0 )
   ii1iIIi11 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o0Oooo0 )
   for iI1IIIII1Ii in ii1iIIi11 :
    iIiI1 = False
    Resolve ( iI1IIIII1Ii )
    if 20 - 20: OoOO0ooOOoo0O * OoOoOO00 - I1IiI - OoOO * O0oO
 elif IIIIIIi1IiIi > 1 :
  if 6 - 6: o0oO0 + OoOO0ooOOoo0O / Oo + IIII % OoOoOO00 / Ooo00oOo00o
  for i1I111I1Iii1 in o0OO0OoO0o0o0 :
   iiIi = OOoOoo ( i1I111I1Iii1 )
   OooooOo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iiIi )
   IIIiiiIiI = OooooOo
   IIIiiiIiI = ( str ( IIIiiiIiI ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIIiiiIiI
   i1II1 ( 'DOUBLE LINK' , IIIiiiIiI , 424 , '' )
   if 80 - 80: OoOO % OoOO % O0 - i11iIiiIii . oO0o0ooO0 / O0
   for url in OooooOo :
    I1I11i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IiiiI = Google . resolve ( url )
    except :
     pass
    try :
     IiIi1Ii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IiiiI ) )
     for iiIIiI11II1 , oooOo in IiIi1Ii :
      if 79 - 79: OoOO - OoOoOO00
      HD_URLS . append ( iiIIiI11II1 )
      SD_URLS . append ( oooOo )
    except :
     pass
 else :
  pass
  if 43 - 43: i1IIi + O0 % Ooo00oOo00o / o00O0oo * OOOo0
def OoO ( ) :
 if 37 - 37: ii11ii1ii
 if 68 - 68: OOooOOo
 I1I11i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iIii1 + 'Movies.png' )
 if 84 - 84: OoooooooOO + O0oO / OOOo0 % OoOO0ooOOoo0O % ii11ii1ii * OOOo0
 I1I11i ( 'Search Movies' , '' , 7017 , iIii1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 58 - 58: Ooo00oOo00o - I1IiI . i11iIiiIii % i11iIiiIii / i1IIi / OoOO
 if 24 - 24: OOOo0 * i1IIi % o0oO0 / O0 + i11iIiiIii
def iI1i ( ) :
 OOooooO0Oo = OOoOoo ( 'http://cnfstudio.com/' )
 iiIi1IIiIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , 'http://cnfstudio.com/genre/' + iIiIIi1 , 7003 , iIii1 + 'icon.png' )
  if 3 - 3: IIII / o0000oOoOoO0o
i1iIIi1 = xbmcgui . Dialog ( )
if 34 - 34: i11iIiiIii / O0oO * OoOO0ooOOoo0O . Oo
if 79 - 79: O0oO
def iI11111ii11 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOooooO0Oo )
 I11I = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I11iIiI1I1i11 )
 I11I = I11I
 for url in I11I :
  I1I11i ( 'Next Page' , url , 7003 , '' )
  if 20 - 20: ii11ii1ii + i1IIi * i11iIiiIii
def o0oo0000 ( url ) :
 if 89 - 89: I1IiI . OoOO0ooOOoo0O
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  OOooOO000 = url + '&fv=&sou='
  OOooOO000 = OOooOO000 . replace ( 'player' , 'watch' )
  IIIIIiI11Ii = Iiii1Ii1I ( OOooOO000 )
  oooOOOOOi1iIii = Iiii1Ii1I ( url )
  if 65 - 65: oO0o0ooO0 . OoOO - o00O0oo
  if 93 - 93: O0
def Iiii1Ii1I ( url ) :
 if 4 - 4: OOOo0 / OOOo0
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  IiI1iI1IiiIi1 ( url )
  if 82 - 82: o0000oOoOoO0o / o0oO0 * o0000oOoOoO0o % i11iIiiIii * OoOoOO00
  if 83 - 83: Ooo00oOo00o + OoOO0ooOOoo0O - OOooOOo + iIii1I11I1II1 % Oo
def II111I1 ( ) :
 IIIII ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 32 - 32: OoOO0ooOOoo0O % i1IIi
def IIi1i1 ( url ) :
 iiIi1IIiIi = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for o0O0Ooo , oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , iIii1 + 'streams.png' )
  if 79 - 79: o0oO0 . OoOO / OoOO - o0oO0 * Oo / OOooOOo
  if 19 - 19: ii11ii1ii
def IiI ( ) :
 IIIII ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 IIIII ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 4 - 4: OoooooooOO + o0oO0 . i1IIi / O0 - O0
 if 52 - 52: Ooo00oOo00o * OoooooooOO
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
ii11iIi1I = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
Ii11iiI = 'https://addons.tvaddons.ag/'
if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
def iiI ( ) :
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 O0OO0o0O00oO = 'https://addons.tvaddons.ag/search/?keyword=' + oo0
 OOoOoOo = OOoOoo ( O0OO0o0O00oO )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOoOo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  IIIII ( oOO00Oo , iIiIIi1 , 10054 , 'https://addons.tvaddons.ag/' + I1IIII1i , iI111I11I1I1 , '' )
  if 81 - 81: IIII / o0000oOoOoO0o
  if 46 - 46: ii11ii1ii / O0oO + IIII / OoOO / O0oO / OoOO0ooOOoo0O
def o0O0oo0 ( ) :
 OOoOoOo = OOoOoo ( Ii11iiI )
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
   if 33 - 33: OOooOOo / O0 + OoOO0ooOOoo0O
   if 75 - 75: IIII % i11iIiiIii + iIii1I11I1II1
def Addon ( url ) :
 OOoOoOo = OOoOoo ( url )
 oOoOo0o00o = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OOoOoOo )
 for url in oOoOo0o00o :
  IIIII ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOoOo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if 'Please' in oOO00Oo :
   pass
  else :
   IIIII ( oOO00Oo , url , 10054 , 'https://addons.tvaddons.ag/' + I11iIiI1I1i11 , iI111I11I1I1 , '' )
   if 2 - 2: OoOoOO00
   if 54 - 54: o00O0oo . OoooooooOO % Oo
def ii111I11Ii ( url , name ) :
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
   if 6 - 6: o00O0oo
def oooOo0OOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 77 - 77: i1IIi + Ooo00oOo00o . OOOo0 * OoOO0ooOOoo0O / IIII / o00O0oo
 if 84 - 84: Ooo00oOo00o / iIii1I11I1II1
def IiI1 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1007 , I1IIII1i )
def iiIiII ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I1IIII1i )
  if 7 - 7: Oo - i1IIi . ii11ii1ii / iIii1I11I1II1 * OOooOOo
  if 100 - 100: o0oO0 / o0oO0 - OoOO0ooOOoo0O % OoOO0ooOOoo0O * OoOO / IIII
def IIIIIIi ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  if '.php' in url :
   I1I11i ( oOO00Oo , url , 1016 , I1IIII1i )
  else :
   i1II1 ( oOO00Oo , url , 222 , I1IIII1i )
   if 59 - 59: OoOO / OOOo0 * o00O0oo % O0 - OoOoOO00 + OoooooooOO
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 21 - 21: O0oO
def OooO0O0Ooo ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1007 , I1IIII1i )
def oO0OIIIiIi1iiI ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I1IIII1i )
  if 15 - 15: ii11ii1ii . oO0o0ooO0
def o0Iiii ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I1i1I = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1i1I )
 if 17 - 17: o0000oOoOoO0o - oO0o0ooO0 % o00O0oo
 if 2 - 2: o00O0oo * ii11ii1ii * OoooooooOO
def oOOOooO ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I11iIiI1I1i11 )
def iI ( url ) :
 OOooooO0Oo = OO ( url )
 o00OOOOOo0OOo = url
 iiIi1IIiIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  if '.mp3' in oOO00Oo :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1II1 ( ( oOO00Oo ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iIii1 + 'music.png' )
  else :
   I1I11i ( ( oOO00Oo ) . replace ( '/' , '' ) , o00OOOOOo0OOo + url , 1011 , iIii1 + 'music.png' )
def i1II11I11ii1 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , ( 'http://www.cyn.net/music/' + iIiIIi1 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I11iIiI1I1i11 ) . replace ( ' ' , '%20' ) )
def OOoO0oO00o ( url , img ) :
 OOooooO0Oo = OO ( url )
 IiiiI = url
 img = img
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '.mp3' , '' ) , ( IiiiI + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 78 - 78: Oo * O0oO - OoooooooOO - Ooo00oOo00o
  if 83 - 83: o0oO0 / OoOO0ooOOoo0O
def i11iI1 ( ) :
 O0Oo0 = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iIIiiiI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0 = iIIiiiI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IiiiI = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OOooO0OO0 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 35 - 35: o0000oOoOoO0o
 OOoOoOo = oOII1ii1ii11I1 ( iIiIIi1 )
 Iiiiiii1 = oOII1ii1ii11I1 ( IiiiI )
 oOO0IIi1I1i = oOII1ii1ii11I1 ( OOooO0OO0 )
 if 94 - 94: o0oO0 / i11iIiiIii % O0
 if OOoOoOo != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoOo )
  for oOO00Oo in iiIi1IIiIi :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIIi1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
    iI1 ( 'tvshows' , 'Media Info 3' )
 if Iiiiiii1 != 'Failed' :
  iiii111II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoOo )
  for oOO00Oo in iiii111II :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiiI + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 95 - 95: OoooooooOO % OoooooooOO . o00O0oo
    iI1 ( 'tvshows' , 'Media Info 3' )
 if oOO0IIi1I1i != 'Failed' :
  oO00O0 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oOO0IIi1I1i )
  for oOO00Oo in oO00O0 :
   if iIIiiiI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOooO0OO0 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 26 - 26: OoOO + IIII - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
    iI1 ( 'tvshows' , 'Media Info 3' )
    if 68 - 68: O0
    if 76 - 76: ii11ii1ii
    if 99 - 99: OOooOOo
    if 1 - 1: o00O0oo * I1IiI * Ooo00oOo00o + Oo
    if 90 - 90: O0oO % Oo - Oo . iIii1I11I1II1 / OoOO0ooOOoo0O + o0000oOoOoO0o
    if 89 - 89: OoOO
def o0OOOOOo00 ( ) :
 OOooooO0Oo = OOoOoo ( 'http://www.animetoon.org/cartoon' )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1002 , iIii1 + 'anime.png' )
  if 82 - 82: Oo
  if 5 - 5: Ooo00oOo00o / Ooo00oOo00o - O0 - O0oO + O0oO
  if 99 - 99: o0000oOoOoO0o * OoooooooOO / OOooOOo . IIII - iIii1I11I1II1 - o00O0oo
def I1iIiIii ( url ) :
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
def OO0 ( url , IMAGE ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  print oOO00Oo + '     ' + url
  if 'easy' in url :
   I1iiI1iiI1i1 ( url )
  elif 'playpanda' in url :
   I1iiI1iiI1i1 ( url )
   if 88 - 88: OoOO % Oo - o0000oOoOoO0o % OoOO + IIII - oO0o0ooO0
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iiI1iiI1i1 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "url: '(.+?)'," ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( 'STREAM' , url , 222 , iIii1 + 'anime.png' )
  if 23 - 23: O0
  if 9 - 9: o0000oOoOoO0o * Oo . o0oO0 * i11iIiiIii - O0
def OoO00OOoOOOo0 ( url ) :
 o0ooOO0o = urllib2 . Request ( url )
 o0ooOO0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0ooOO0o . add_header ( 'referer' , url )
 ooo0 = urllib2 . urlopen ( o0ooOO0o )
 OOooOO000 = ooo0 . read ( )
 ooo0 . close ( )
 return OOooOO000
 if 84 - 84: OoOO + OoOO0ooOOoo0O . oO0o0ooO0
def OO ( url ) :
 o0ooOO0o = urllib2 . Request ( url )
 o0ooOO0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 ooo0 = urllib2 . urlopen ( o0ooOO0o )
 OOooOO000 = ooo0 . read ( )
 ooo0 . close ( )
 return OOooOO000
 if 71 - 71: o0oO0 / o0oO0 . I1IiI % oO0o0ooO0
def I1i1i1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOo0OoOOo0 = ( '%s%s' % ( iII11I1Ii1 , url ) )
 OOooOO000 = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooOO000 )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '%s' % ( oOO00Oo ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I1IIII1i )
  if 82 - 82: IIII . I1IiI / o0oO0 + oO0o0ooO0 - o0oO0
def IiI1iI1IiiIi1 ( url ) :
 o00OOo0o0O = xbmc . Player ( I111Iii1 ( ) )
 import urlresolver
 try : o00OOo0o0O . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( oOO00Oo ) )
 o00OOo0o0O = xbmc . Player ( I111Iii1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iIIi1 = xbmcgui . Dialog ( )
  if i1iIIi1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iIIi1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : o00OOo0o0O . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 30 - 30: i1IIi
def OOOO0O00o ( url ) :
 o00OOo0o0O = xbmc . Player ( I111Iii1 ( ) )
 import urlresolver
 try : o00OOo0o0O . play ( url )
 except : pass
 if 75 - 75: o0000oOoOoO0o . OoOO0ooOOoo0O - iIii1I11I1II1 * Ooo00oOo00o * oO0o0ooO0
 if 93 - 93: o0oO0
def I111Iii1 ( ) :
 try :
  iII1IIiiI11II = getSet ( "core-player" )
  if ( iII1IIiiI11II == 'DVDPLAYER' ) : O00OoOOoo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iII1IIiiI11II == 'MPLAYER' ) : O00OoOOoo = xbmc . PLAYER_CORE_MPLAYER
  elif ( iII1IIiiI11II == 'PAPLAYER' ) : O00OoOOoo = xbmc . PLAYER_CORE_PAPLAYER
  else : O00OoOOoo = xbmc . PLAYER_CORE_AUTO
 except : O00OoOOoo = xbmc . PLAYER_CORE_AUTO
 return O00OoOOoo
 return True
 if 49 - 49: i11iIiiIii - ii11ii1ii - o0000oOoOoO0o / OoooooooOO % I1IiI
def I1I11i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO0o0 = True
 iiI11I1i1i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiI11I1i1i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooo00o0o = [ ]
  if showcontext == 'fav' :
   ooo00o0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iIi1ii1I1 :
   ooo00o0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiI11I1i1i1iI . addContextMenuItems ( ooo00o0o )
 oOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = iiI11I1i1i1iI , isFolder = True )
 return oOO0o0
 if 56 - 56: I1IiI % ii11ii1ii - o00O0oo % iIii1I11I1II1
def i1II1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO0o0 = True
 iiI11I1i1i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiI11I1i1i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooo00o0o = [ ]
  if showcontext == 'fav' :
   ooo00o0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iIi1ii1I1 :
   ooo00o0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiI11I1i1i1iI . addContextMenuItems ( ooo00o0o )
 oOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = iiI11I1i1i1iI , isFolder = False )
 return oOO0o0
 if 76 - 76: OoooooooOO * OoooooooOO - oO0o0ooO0 - iIii1I11I1II1 . OoooooooOO / ii11ii1ii
 if 86 - 86: o0oO0
 if 51 - 51: Ooo00oOo00o - i11iIiiIii * OOOo0
 if 95 - 95: OoOO0ooOOoo0O % ii11ii1ii + OOooOOo % o0oO0
 if 36 - 36: O0 / i1IIi % OoOoOO00 / oO0o0ooO0
 if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
def oooOO0oo0Oo00 ( heading , announce ) :
 class ooIi111iII ( ) :
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
   try : II11IiIi11 = open ( announce ) ; Oo0OoOo = II11IiIi11 . read ( )
   except : Oo0OoOo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Oo0OoOo ) )
   return
 ooIi111iII ( )
 if 13 - 13: OOooOOo
def IIi1ii ( ) :
 oooOO0oo0Oo00 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 38 - 38: iIii1I11I1II1 + OoooooooOO * OOOo0 % I1IiI % o0000oOoOoO0o - IIII
 if 56 - 56: OoooooooOO * Oo * o0000oOoOoO0o + o0oO0
 if 54 - 54: I1IiI * i11iIiiIii . OoooooooOO - iIii1I11I1II1
 if 38 - 38: o0000oOoOoO0o . o0000oOoOoO0o * OoOO / OoooooooOO % o0oO0
 if 80 - 80: Ooo00oOo00o / IIII * OOOo0 % IIII
def oooOo0OOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 95 - 95: O0 / o0000oOoOoO0o . O0oO
 if 17 - 17: o0000oOoOoO0o
 if 56 - 56: o0oO0 * OOooOOo + o0000oOoOoO0o
 if 48 - 48: IIII * Ooo00oOo00o % O0oO - o0000oOoOoO0o
 if 72 - 72: i1IIi % o0oO0 % IIII % OoOO - OoOO
 if 97 - 97: OOooOOo * O0 / OOooOOo * Ooo00oOo00o * Oo
 if 38 - 38: O0oO
 if 25 - 25: iIii1I11I1II1 % OoOoOO00 / o0000oOoOoO0o / ii11ii1ii
 if 22 - 22: OoOO * oO0o0ooO0
 if 4 - 4: I1IiI - OoOO + OOOo0
 if 36 - 36: IIII
 if 19 - 19: I1IiI . OOooOOo . OoooooooOO
 if 13 - 13: OoOO0ooOOoo0O . Oo / OoOoOO00
 if 43 - 43: iIii1I11I1II1 % Ooo00oOo00o
 if 84 - 84: Oo
 if 44 - 44: OoooooooOO * i11iIiiIii / Oo
 if 75 - 75: OoooooooOO . OoOO0ooOOoo0O + Ooo00oOo00o / o00O0oo - OOOo0 % o00O0oo
 if 89 - 89: oO0o0ooO0 * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
 if 51 - 51: OoOO0ooOOoo0O / o0oO0 + Ooo00oOo00o % I1IiI / o00O0oo
 if 25 - 25: OOooOOo
 if 25 - 25: o0oO0 * oO0o0ooO0 / o0000oOoOoO0o / o0000oOoOoO0o % OOooOOo
 if 19 - 19: OoOO - iIii1I11I1II1 / o0oO0 . Ooo00oOo00o * O0 - O0
 if 41 - 41: i1IIi - OOOo0
 if 48 - 48: OOOo0 - OoOoOO00 / Ooo00oOo00o + OOOo0
def i1iii1IiiiI1i1 ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + IIIiI1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 13 - 13: OoOO0ooOOoo0O * o0000oOoOoO0o / O0 * OOooOOo
def Ii1iiIi11111I ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + OOOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 80 - 80: Oo % IIII % OoooooooOO * Oo % o00O0oo
def iii1 ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + O0Ooo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 18 - 18: i1IIi
def i1i1Ii1IiIII ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + I1IIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 22 - 22: o0oO0 / o0oO0 - o00O0oo % o0000oOoOoO0o . OoOO0ooOOoo0O + IIII
def OooO00oo0O0 ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 73 - 73: OoooooooOO . Oo / O0 - O0
def IiI11IIi11Iii ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + ii11i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 49 - 49: OoooooooOO + OoooooooOO / OoOO0ooOOoo0O . OoOO
def IiIooOoOo0O00oo ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + iIIi111IiII1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 67 - 67: OOOo0 % iIii1I11I1II1
def O00oo0oOoO00O ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + Iii1iIiI1I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 66 - 66: I1IiI + OOooOOo
def OOOO00 ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + o0I1iI111ii111i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 83 - 83: iIii1I11I1II1
def Oo0O0O ( url ) :
 OOooOO000 = OOoOoo ( II11iiii1Ii + IiIiiI1ii111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  IIIII ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 iI1 ( 'movies' , 'MAIN' )
 if 30 - 30: o00O0oo + OoOoOO00 % OoooooooOO
 if 89 - 89: o00O0oo
 if 51 - 51: oO0o0ooO0
 if 68 - 68: oO0o0ooO0 - OOooOOo * Ooo00oOo00o % o0oO0 . o0oO0 - iIii1I11I1II1
 if 22 - 22: OoooooooOO / ii11ii1ii % oO0o0ooO0 * I1IiI
 if 32 - 32: OoooooooOO % OoOO % iIii1I11I1II1 / O0
 if 61 - 61: OoOoOO00 . O0 - o00O0oo - ii11ii1ii / i11iIiiIii - OoOoOO00
 if 98 - 98: o00O0oo - OOOo0 . i11iIiiIii * Oo
 if 29 - 29: o00O0oo / o0oO0 % o0000oOoOoO0o
def ii1iIII1ii ( ) :
 try :
  if os . path . exists ( ooOoOoo0O ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( ooOoOoo0O ) :
     I11Oo0O0O0O0OO = 0
     I11Oo0O0O0O0OO += len ( oOOOoo00 )
     if I11Oo0O0O0O0OO > 0 :
      for II11IiIi11 in oOOOoo00 :
       os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
  o0OoOooOO0o0 = os . path . join ( iiI1IiI , "Textures13.db" )
  os . unlink ( o0OoOooOO0o0 )
  i1iIIi1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 55 - 55: O0 % OOOo0 . OoooooooOO * Oo / OoooooooOO . o00O0oo
 if 26 - 26: IIII / iIii1I11I1II1 - iIii1I11I1II1
 if 57 - 57: IIII
 if 41 - 41: iIii1I11I1II1 * oO0o0ooO0 + Oo * OOooOOo % IIII / OoOO0ooOOoo0O
 if 63 - 63: i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
 if 40 - 40: Oo
 if 47 - 47: I1IiI
 if 65 - 65: O0 + O0oO % o00O0oo * OOOo0 / o0oO0 / I1IiI
 if 71 - 71: i11iIiiIii / I1IiI . OoOO
def iI1IIIi11 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 oooOo00O0 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( oooOo00O0 ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( oooOo00O0 ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 26 - 26: O0oO . o00O0oo + OOOo0 . I1IiI + OoOO0ooOOoo0O
   if 17 - 17: OoOO0ooOOoo0O + i11iIiiIii + ii11ii1ii % OoOO0ooOOoo0O . OoOO
   if I11Oo0O0O0O0OO > 0 :
    if 33 - 33: o0000oOoOoO0o * OOOo0 % I1IiI . IIII . o0oO0 . Ooo00oOo00o
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete KODI Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: I1IiI
     for II11IiIi11 in oOOOoo00 :
      try :
       os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
      except :
       pass
     for o0oo0OO in Ooo0oOooo0 :
      try :
       shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      except :
       pass
       if 17 - 17: o0oO0 + ii11ii1ii * i11iIiiIii
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oO00OOOOOO0o = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 18 - 18: ii11ii1ii / Oo - oO0o0ooO0
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( oO00OOOOOO0o ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 69 - 69: OoOO / IIII * o0oO0
   if I11Oo0O0O0O0OO > 0 :
    if 81 - 81: OoOO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 62 - 62: o00O0oo + O0 * Ooo00oOo00o
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 59 - 59: OoOoOO00
   else :
    pass
  iIiIi11 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 42 - 42: o0000oOoOoO0o % Oo . OoOoOO00 / OoOoOO00 * oO0o0ooO0
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iIiIi11 ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 80 - 80: O0oO / i11iIiiIii + OoooooooOO
   if I11Oo0O0O0O0OO > 0 :
    if 38 - 38: ii11ii1ii % o0oO0 + i1IIi * OoooooooOO * OoOO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 83 - 83: iIii1I11I1II1 - o0oO0 - O0oO / Ooo00oOo00o - O0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 81 - 81: o00O0oo - OoOO * ii11ii1ii / O0oO
   else :
    pass
    if 21 - 21: Ooo00oOo00o
    if 63 - 63: o0000oOoOoO0o . O0 * o0000oOoOoO0o + iIii1I11I1II1
    if 46 - 46: i1IIi + OoOoOO00 * i1IIi - o00O0oo
    if 79 - 79: OoOoOO00 - OoOO * ii11ii1ii - I1IiI . ii11ii1ii
 iiII1IIii1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( iiII1IIii1i1 ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iiII1IIii1i1 ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 38 - 38: oO0o0ooO0 * OoooooooOO
   if 2 - 2: OoOO - i11iIiiIii
   if I11Oo0O0O0O0OO > 0 :
    if 98 - 98: OoOO + OoooooooOO - O0oO % i11iIiiIii / OOooOOo . OoooooooOO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete WTF Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: i1IIi
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 33 - 33: O0oO % OoOoOO00
   else :
    pass
    if 49 - 49: ii11ii1ii + o0000oOoOoO0o / OOooOOo + OoooooooOO + OoOO0ooOOoo0O / IIII
    if 29 - 29: o00O0oo - o00O0oo / o0oO0
 I11IIII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( I11IIII ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( I11IIII ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 38 - 38: OoooooooOO . OOooOOo . OoOoOO00 - oO0o0ooO0
   if 65 - 65: i11iIiiIii + OOOo0 / Oo % OoOO0ooOOoo0O . o00O0oo + iIii1I11I1II1
   if I11Oo0O0O0O0OO > 0 :
    if 32 - 32: OOOo0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete 4oD Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: ii11ii1ii * OoOO + iIii1I11I1II1 - OoOO / IIII
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 86 - 86: IIII
   else :
    pass
    if 43 - 43: OOOo0 / oO0o0ooO0 / o0oO0 + iIii1I11I1II1 + OoooooooOO
    if 33 - 33: OoOoOO00 - IIII - o0oO0
 oO00oOoo00o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( oO00oOoo00o0 ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( oO00oOoo00o0 ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 41 - 41: OoOO / OoOO0ooOOoo0O + oO0o0ooO0 + o0oO0
   if 13 - 13: i11iIiiIii - i11iIiiIii . iIii1I11I1II1
   if I11Oo0O0O0O0OO > 0 :
    if 33 - 33: OoooooooOO + O0oO / O0oO + O0oO * IIII
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete BBC iPlayer Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 26 - 26: O0oO . OOOo0 . oO0o0ooO0 - OoooooooOO / iIii1I11I1II1
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 47 - 47: IIII
   else :
    pass
    if 76 - 76: Ooo00oOo00o * iIii1I11I1II1 + ii11ii1ii - o0oO0 - o0000oOoOoO0o / i1IIi
    if 27 - 27: ii11ii1ii . IIII
    if 66 - 66: O0 / O0 * i1IIi . OoooooooOO % iIii1I11I1II1
 I11iIiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( I11iIiI1 ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( I11iIiI1 ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 22 - 22: IIII * o00O0oo - OoooooooOO
   if 28 - 28: OOOo0
   if I11Oo0O0O0O0OO > 0 :
    if 87 - 87: IIII . i1IIi % OoooooooOO * i11iIiiIii
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Simple Downloader Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 67 - 67: O0oO / Ooo00oOo00o . OoooooooOO
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 51 - 51: OoOoOO00 . OoOO . Ooo00oOo00o % OoOoOO00
   else :
    pass
    if 41 - 41: I1IiI - OoOO0ooOOoo0O + o0oO0 - i1IIi
    if 6 - 6: OoOoOO00
 iI1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iI1I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iI1I ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 11 - 11: OoOoOO00 * o00O0oo / OoOoOO00 + o0000oOoOoO0o - O0
   if 51 - 51: OOOo0 + i1IIi * O0 / IIII / iIii1I11I1II1
   if I11Oo0O0O0O0OO > 0 :
    if 2 - 2: OoooooooOO + O0 / OoOO0ooOOoo0O
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ITV Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 86 - 86: ii11ii1ii * i1IIi + oO0o0ooO0 . ii11ii1ii
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 100 - 100: OoooooooOO - O0 . o0000oOoOoO0o / o0000oOoOoO0o + OoOoOO00 * I1IiI
   else :
    pass
    if 37 - 37: Oo
    if 72 - 72: IIII % ii11ii1ii * OoOO0ooOOoo0O . i11iIiiIii % IIII * OoOO0ooOOoo0O
 i11I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iI1I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( i11I ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 75 - 75: OoOO * o0oO0
   if 88 - 88: Ooo00oOo00o * OOooOOo * OoOO0ooOOoo0O / Oo * Ooo00oOo00o
   if I11Oo0O0O0O0OO > 0 :
    if 100 - 100: OOooOOo . OOOo0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Movies4me Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 62 - 62: o0oO0 + OoOoOO00 % o0oO0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 50 - 50: OoooooooOO + OoOO * OOOo0 - o00O0oo / i11iIiiIii
   else :
    pass
    if 5 - 5: O0 - OOOo0
    if 44 - 44: OoOoOO00 . OoOoOO00 + OoOO0ooOOoo0O * o00O0oo
 i1iIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iI1I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( i1iIi ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 22 - 22: oO0o0ooO0 + Ooo00oOo00o - o0oO0
   if 10 - 10: OOOo0 / ii11ii1ii
   if I11Oo0O0O0O0OO > 0 :
    if 68 - 68: OoOO0ooOOoo0O - OoooooooOO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Phoenix Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: O0 / OoOO - Oo - IIII
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 44 - 44: Ooo00oOo00o
   else :
    pass
    if 32 - 32: I1IiI % Ooo00oOo00o + i11iIiiIii + o0oO0 - o00O0oo + OoOO
    if 31 - 31: iIii1I11I1II1 - OOooOOo
 oOOo00Ooo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iI1I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( oOOo00Ooo0O ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 34 - 34: OoOoOO00
   if 49 - 49: o0000oOoOoO0o . OoOO0ooOOoo0O
   if I11Oo0O0O0O0OO > 0 :
    if 74 - 74: i1IIi
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Music Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 15 - 15: i1IIi + IIII % OOOo0 / i11iIiiIii * I1IiI
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 69 - 69: i11iIiiIii
   else :
    pass
    if 61 - 61: O0
    if 21 - 21: Ooo00oOo00o % iIii1I11I1II1 . Ooo00oOo00o
 OO000OOOo0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iI1I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( OO000OOOo0Oo ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 75 - 75: OoOoOO00 + o0oO0 % OoOO0ooOOoo0O + Oo
   if 70 - 70: Ooo00oOo00o
   if I11Oo0O0O0O0OO > 0 :
    if 43 - 43: I1IiI
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete SuperCartoons Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 57 - 57: OOOo0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 65 - 65: i11iIiiIii - o0oO0 * o0000oOoOoO0o + o0oO0 / IIII + OOooOOo
   else :
    pass
    if 35 - 35: O0 + Oo - OOOo0 % o00O0oo % OoOoOO00
    if 77 - 77: O0oO + OoOO
 iI11Iii1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iI1I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iI11Iii1I ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 62 - 62: IIII . O0 . iIii1I11I1II1
   if 94 - 94: o0oO0 % o0000oOoOoO0o % i1IIi
   if I11Oo0O0O0O0OO > 0 :
    if 90 - 90: o00O0oo * Ooo00oOo00o
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete TVonline Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: oO0o0ooO0 . o00O0oo . oO0o0ooO0 - O0oO
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 33 - 33: o0oO0 + OoooooooOO - Ooo00oOo00o / i1IIi / OoooooooOO
   else :
    pass
    if 82 - 82: ii11ii1ii / OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
    if 55 - 55: OoooooooOO
 OO0OOOOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iI1I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( OO0OOOOOo ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 7 - 7: O0 + o00O0oo . OoOoOO00
   if 12 - 12: OOOo0 - i1IIi
   if I11Oo0O0O0O0OO > 0 :
    if 95 - 95: o0000oOoOoO0o / IIII . O0 * IIII - OOooOOo * Oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / o00O0oo
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
      if 14 - 14: O0oO % IIII - O0 / O0oO
   else :
    pass
    if 91 - 91: i11iIiiIii % O0oO * OoOO - ii11ii1ii . O0oO
    if 28 - 28: i11iIiiIii
    if 51 - 51: OOOo0 + o0oO0 * O0 . o00O0oo
 O00Oo00OOoO0 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iIIi1 = xbmcgui . Dialog ( )
 try :
  if i1iIIi1 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   oOoo = os . path . join ( O00Oo00OOoO0 , "cache.db" )
   os . unlink ( oOoo )
   if 59 - 59: IIII % o00O0oo
 except :
  pass
  if 57 - 57: o0000oOoOoO0o . O0 % OoooooooOO . OOOo0 . i1IIi - OoOoOO00
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 61 - 61: O0 . OOooOOo / I1IiI
 if 74 - 74: i1IIi * O0oO % o00O0oo
 if 30 - 30: OoOoOO00 - OOooOOo % O0oO . o0000oOoOoO0o
 if 63 - 63: iIii1I11I1II1 / o0oO0
 if 24 - 24: Oo / iIii1I11I1II1 % OoOO0ooOOoo0O * I1IiI - iIii1I11I1II1
 if 50 - 50: OoOoOO00
 if 39 - 39: OoOoOO00 . I1IiI - Oo * i1IIi . OoooooooOO
 if 44 - 44: OOOo0
 if 55 - 55: OoOO . O0oO * O0oO
def OO0OO00ooO0 ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 OOOOOoO00oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( OOOOOoO00oo00 ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 9 - 9: OOOo0 - Oo
   if 62 - 62: o00O0oo - OoOO % iIii1I11I1II1
   if I11Oo0O0O0O0OO > 0 :
    if 57 - 57: OoooooooOO / I1IiI
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Package Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 44 - 44: I1IiI * i1IIi * O0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
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
 if 94 - 94: OOOo0 - O0
 if 18 - 18: IIII / OoOO . OoOO . iIii1I11I1II1 . i11iIiiIii
 if 69 - 69: i11iIiiIii - O0 % OoOoOO00 % OoOO0ooOOoo0O / Oo * o0000oOoOoO0o
 if 61 - 61: Ooo00oOo00o . i1IIi - OOOo0
 if 38 - 38: OoOO + iIii1I11I1II1 * o00O0oo / Ooo00oOo00o + OoOO0ooOOoo0O
 if 48 - 48: OoooooooOO - O0oO . i11iIiiIii * oO0o0ooO0 - o00O0oo - OOooOOo
 if 59 - 59: oO0o0ooO0 / o0000oOoOoO0o . Oo
 if 100 - 100: O0
 if 94 - 94: ii11ii1ii - OOooOOo
def IIiIIIi1iii1 ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 OOOOOoO00oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( OOOOOoO00oo00 ) :
   I11Oo0O0O0O0OO = 0
   I11Oo0O0O0O0OO += len ( oOOOoo00 )
   if 37 - 37: iIii1I11I1II1 % o0000oOoOoO0o / IIII
   if 37 - 37: O0oO - OoOO - Ooo00oOo00o
   if I11Oo0O0O0O0OO > 0 :
    if 42 - 42: iIii1I11I1II1 % o00O0oo - ii11ii1ii + iIii1I11I1II1
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Package Cache Files" , str ( I11Oo0O0O0O0OO ) + " files found" , "Do you want to delete them?" ) :
     if 27 - 27: O0 / Ooo00oOo00o
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for o0oo0OO in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , o0oo0OO ) )
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
 iI1IIIi11 ( url )
 if 99 - 99: o00O0oo - IIII * iIii1I11I1II1 . OoOoOO00
 if 56 - 56: iIii1I11I1II1 % Ooo00oOo00o . o0oO0 % IIII . O0oO * Oo
 if 41 - 41: iIii1I11I1II1 % IIII * OoOO - o0oO0
 if 5 - 5: Ooo00oOo00o + Ooo00oOo00o + OoOoOO00 * iIii1I11I1II1 + OoooooooOO
 if 77 - 77: O0 * ii11ii1ii * OoOO + Ooo00oOo00o + ii11ii1ii - O0oO
 if 10 - 10: ii11ii1ii + IIII
 if 58 - 58: OOOo0 + OoooooooOO / oO0o0ooO0 . o0oO0 % OOooOOo / ii11ii1ii
 if 62 - 62: OoOoOO00
 if 12 - 12: IIII + OoOoOO00
def O0Ooo00o00O ( url , name ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooo0O0O0oo0 = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 i1iIIi1 = xbmcgui . Dialog ( )
 oo000oO = os . path . join ( O0oO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oo000oO ) == False :
  if i1iIIi1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   ooo0O0O0oo0 = os . path . join ( O0oO0 , 'advancedsettings.xml' )
   try :
    os . remove ( ooo0O0O0oo0 )
    print '=== GenieTv - REMOVING    ' + str ( ooo0O0O0oo0 ) + '    ==='
   except :
    pass
   OOooOO000 = I11 . http_GET ( url ) . content
   iiIiIIIiiI = open ( ooo0O0O0oo0 , "w" )
   iiIiIIIiiI . write ( OOooOO000 )
   iiIiIIIiiI . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( ooo0O0O0oo0 ) + '    ==='
   i1iIIi1 = xbmcgui . Dialog ( )
   i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  ooo0O0O0oo0 = os . path . join ( O0oO0 , 'advancedsettings.xml' )
  try :
   os . remove ( ooo0O0O0oo0 )
   print '=== GenieTv - REMOVING    ' + str ( ooo0O0O0oo0 ) + '    ==='
  except :
   pass
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( ooo0O0O0oo0 , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooo0O0O0oo0 ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 8 - 8: OOOo0 % OoOoOO00 - OOooOOo - o0000oOoOoO0o % OOOo0
def o0o0O0oOooO00 ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooo0O0O0oo0 = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 try :
  iiIiIIIiiI = open ( ooo0O0O0oo0 ) . read ( )
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
 if 27 - 27: oO0o0ooO0
def o000 ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooo0O0O0oo0 = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 try :
  os . remove ( ooo0O0O0oo0 )
  i1iIIi1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( ooo0O0O0oo0 ) + '    ==='
  i1iIIi1 . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 75 - 75: O0
 if 56 - 56: Ooo00oOo00o / OoOoOO00
 if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
 if 49 - 49: Oo + O0 + IIII . OoOoOO00 % o0oO0
 if 33 - 33: I1IiI . iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / IIII - O0 % o00O0oo
 if 27 - 27: Ooo00oOo00o + Oo
 if 92 - 92: OOOo0 % oO0o0ooO0
 if 31 - 31: OoooooooOO - OoOO / O0oO
 if 62 - 62: i11iIiiIii - o0000oOoOoO0o
def o00OOOOooO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iiIi1IIiIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for o0oo00oo0oO , ii1ii , Ii1iii11I , Ii11iIiiI in iiIi1IIiIi :
  if inc < 2 : i1iIIi1 = xbmcgui . Dialog ( ) ; i1iIIi1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % o0oo00oo0oO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % Ii1iii11I , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % Ii11iIiiI )
  inc = inc + 1
  if 3 - 3: OoOoOO00 / OoOO0ooOOoo0O
  if 48 - 48: o0oO0 . ii11ii1ii
  if 49 - 49: i1IIi - I1IiI . Oo + iIii1I11I1II1 - o0oO0 / Oo
  if 24 - 24: OoOO - oO0o0ooO0 / o0oO0
  if 10 - 10: I1IiI * i1IIi
  if 15 - 15: o0000oOoOoO0o + i1IIi - OoOoOO00 % OOOo0
  if 34 - 34: OOOo0
  if 57 - 57: OoOO0ooOOoo0O . o00O0oo % OOooOOo
  if 32 - 32: o0000oOoOoO0o / IIII - O0 * iIii1I11I1II1
def oo0oO0oOo0O ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  ooo0O0O0oo0 = os . path . join ( O0oO0 , 'addons2.ini' )
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( ooo0O0O0oo0 , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooo0O0O0oo0 ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 75 - 75: OoOoOO00 + OoOoOO00 + OoOO0ooOOoo0O * OOooOOo
def ooOoO0OoO ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  ooo0O0O0oo0 = os . path . join ( O0oO0 , 'settings.xml' )
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( ooo0O0O0oo0 , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooo0O0O0oo0 ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 94 - 94: IIII % OOooOOo . i11iIiiIii % OoooooooOO + o0oO0 . OOOo0
 if 19 - 19: OOOo0 - I1IiI . Oo . i1IIi - OoOO
def o0OoOOoOOoo ( ) :
 try :
  oo0O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( oo0O0 ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Ii111Ii11 = os . path . join ( oo0O0 , "source.db" )
    os . unlink ( Ii111Ii11 )
  i1iIIi1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 10 - 10: OoooooooOO . OOOo0 * O0 * Ooo00oOo00o - OoOO0ooOOoo0O
 if 33 - 33: ii11ii1ii . Oo + OOOo0 + OOooOOo
 if 54 - 54: o0oO0 * oO0o0ooO0 * oO0o0ooO0 % I1IiI - OoOO0ooOOoo0O % ii11ii1ii
 if 44 - 44: Oo . OoOO0ooOOoo0O + o0000oOoOoO0o
 if 22 - 22: O0oO * OoooooooOO + i11iIiiIii % Ooo00oOo00o
def OOoOoo ( url ) :
 o0ooOO0o = urllib2 . Request ( url )
 o0ooOO0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 ooo0 = urllib2 . urlopen ( o0ooOO0o )
 OOooOO000 = ooo0 . read ( )
 ooo0 . close ( )
 return OOooOO000
 if 53 - 53: OOOo0
 if 10 - 10: O0oO / i11iIiiIii - OoOoOO00
 if 48 - 48: OoOO0ooOOoo0O
 if 26 - 26: oO0o0ooO0 * O0oO * OoOO * I1IiI
 if 48 - 48: oO0o0ooO0 % i11iIiiIii . OoooooooOO * IIII % Ooo00oOo00o . oO0o0ooO0
 if 6 - 6: O0 . o0oO0 - OoOO / i11iIiiIii
 if 84 - 84: o0000oOoOoO0o / ii11ii1ii * OOooOOo * Ooo00oOo00o * OoOO0ooOOoo0O * O0
def OoOooOo00o ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iI1IIi = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iI1IIi :
  II11 = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; II11 = xbmc . translatePath ( II11 ) ;
  oo0o0O = os . path . join ( II11 , ".." , ".." ) ; oo0o0O = os . path . abspath ( oo0o0O ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oo0o0O ) ; ooo0ooooo0o = False
  try :
   for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( oo0o0O , topdown = True ) :
    Ooo0oOooo0 [ : ] = [ o0oo0OO for o0oo0OO in Ooo0oOooo0 if o0oo0OO not in Oo0oO0ooo ]
    for oOO00Oo in oOOOoo00 :
     try : os . remove ( os . path . join ( oooi1i1iI1iiiI , oOO00Oo ) )
     except :
      if oOO00Oo not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : ooo0ooooo0o = True
      plugintools . log ( "Error removing " + oooi1i1iI1iiiI + " " + oOO00Oo )
    for oOO00Oo in Ooo0oOooo0 :
     try : os . rmdir ( os . path . join ( oooi1i1iI1iiiI , oOO00Oo ) )
     except :
      if oOO00Oo not in [ "Database" , "userdata" ] : ooo0ooooo0o = True
      plugintools . log ( "Error removing " + oooi1i1iI1iiiI + " " + oOO00Oo )
   if not ooo0ooooo0o : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0oO0O0o0O00O ( )
 if 30 - 30: I1IiI / OOOo0 - Ooo00oOo00o - oO0o0ooO0 - i11iIiiIii
 if 84 - 84: i1IIi - OOOo0 % oO0o0ooO0
 if 80 - 80: OOooOOo % oO0o0ooO0
def ooOooOooOOO ( ) :
 oO0oOOOo0o = [ ]
 i1II1iII1 = sys . argv [ 2 ]
 if len ( i1II1iII1 ) >= 2 :
  I11II11IiI11 = sys . argv [ 2 ]
  O00o = I11II11IiI11 . replace ( '?' , '' )
  if ( I11II11IiI11 [ len ( I11II11IiI11 ) - 1 ] == '/' ) :
   I11II11IiI11 = I11II11IiI11 [ 0 : len ( I11II11IiI11 ) - 2 ]
  Ii11Iiii1iiii = O00o . split ( '&' )
  oO0oOOOo0o = { }
  for ooo0oooo0 in range ( len ( Ii11Iiii1iiii ) ) :
   i1IIII1111 = { }
   i1IIII1111 = Ii11Iiii1iiii [ ooo0oooo0 ] . split ( '=' )
   if ( len ( i1IIII1111 ) ) == 2 :
    oO0oOOOo0o [ i1IIII1111 [ 0 ] ] = i1IIII1111 [ 1 ]
    if 84 - 84: O0 % o00O0oo . o00O0oo . oO0o0ooO0 * o0000oOoOoO0o
 return oO0oOOOo0o
 if 43 - 43: I1IiI . ii11ii1ii % i1IIi
oOOoo00O00o = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
oO0O0OO0O = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O0O00Oo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OO0O00 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oO0000OOo00 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
ooOO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
IIIiI1i1 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oO0o0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
OOOOoO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
O0Ooo0O = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1IIii11 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1iI = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
ii11i1I1i = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iIIi111IiII1i = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
Iii1iIiI1I1I1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0I1iI111ii111i = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooO0oOOooOo0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
i1Ii1i11ii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iiIi1IIi1I = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
IIi1I11I1II = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiIiiI1ii111 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iII11I1Ii1 = base64 . decodestring ( 'Q1VOVA==' )
def IIIII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o0 = True
 iiI11I1i1i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiI11I1i1i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiI11I1i1i1iI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooo00o0o = [ ]
  if showcontext == 'fav' :
   ooo00o0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iIi1ii1I1 :
   ooo00o0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiI11I1i1i1iI . addContextMenuItems ( ooo00o0o )
 oOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = iiI11I1i1i1iI , isFolder = True )
 return oOO0o0
 if 58 - 58: I1IiI + Ooo00oOo00o * o00O0oo
def O00O0oOO00O00 ( name , url , mode , iconimage , fanart , description ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o0 = True
 iiI11I1i1i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiI11I1i1i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiI11I1i1i1iI . setProperty ( "Fanart_Image" , fanart )
 oOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = iiI11I1i1i1iI , isFolder = False )
 return oOO0o0
 if 31 - 31: OoOO - oO0o0ooO0
 if 46 - 46: OOOo0 + Oo - o00O0oo
I11II11IiI11 = ooOooOooOOO ( )
iIiIIi1 = None
oOO00Oo = None
Ii1iI111 = None
i1iIIIi1i = None
iI1iIIiiii = None
i1iI11i1ii11 = None
O0oO0O = None
if 20 - 20: I1IiI % OoOoOO00 . I1IiI . IIII + OoOO0ooOOoo0O
if 26 - 26: oO0o0ooO0 / OoooooooOO - Oo
try :
 O0oO0O = int ( I11II11IiI11 [ "fav_mode" ] )
except :
 pass
 if 2 - 2: ii11ii1ii - Oo
try :
 iIiIIi1 = urllib . unquote_plus ( I11II11IiI11 [ "url" ] )
except :
 pass
try :
 oOO00Oo = urllib . unquote_plus ( I11II11IiI11 [ "name" ] )
except :
 pass
try :
 i1iIIIi1i = urllib . unquote_plus ( I11II11IiI11 [ "iconimage" ] )
except :
 pass
try :
 Ii1iI111 = int ( I11II11IiI11 [ "mode" ] )
except :
 pass
try :
 iI1iIIiiii = urllib . unquote_plus ( I11II11IiI11 [ "fanart" ] )
except :
 pass
try :
 i1iI11i1ii11 = urllib . unquote_plus ( I11II11IiI11 [ "description" ] )
except :
 pass
 if 4 - 4: O0 / o0000oOoOoO0o . Ooo00oOo00o - o0oO0 / OoOO0ooOOoo0O
 if 25 - 25: o0000oOoOoO0o * I1IiI - Oo . o0oO0 . OoOO
print str ( OooO0 ) + ': ' + str ( O0OoO000O0OO )
print "Mode: " + str ( Ii1iI111 )
print "URL: " + str ( iIiIIi1 )
print "Name: " + str ( oOO00Oo )
print "IconImage: " + str ( i1iIIIi1i )
if 89 - 89: O0 * o0000oOoOoO0o * Ooo00oOo00o
if 3 - 3: OoOO0ooOOoo0O / oO0o0ooO0 * iIii1I11I1II1 + OoOoOO00 / OOooOOo / IIII
def iI1 ( content , viewType ) :
 if 25 - 25: I1IiI + Ooo00oOo00o % o00O0oo % OoOO0ooOOoo0O / OoOO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . o0oO0 - OOOo0
  if 23 - 23: OOOo0
if Ii1iI111 == None :
 I11II1i ( )
 if 7 - 7: oO0o0ooO0 % ii11ii1ii
elif Ii1iI111 == 1 :
 i1i ( iIiIIi1 )
 if 64 - 64: O0oO + i11iIiiIii
elif Ii1iI111 == 44 :
 O0oOOO0ooOOO0OOO ( iIiIIi1 )
 if 35 - 35: I1IiI + i1IIi % OoOO0ooOOoo0O
elif Ii1iI111 == 2 :
 Ooo00o0Oooo ( )
 if 68 - 68: IIII . o0oO0
elif Ii1iI111 == 3 :
 oO0 ( )
 if 64 - 64: i1IIi + Oo * OOOo0 / OoOO0ooOOoo0O
elif Ii1iI111 == 21 :
 o000O0o ( )
 if 3 - 3: Oo / o0oO0 + o0oO0 . ii11ii1ii
elif Ii1iI111 == 4 :
 iIIIIi1iiIi1 ( )
 if 50 - 50: iIii1I11I1II1 * OoOO
elif Ii1iI111 == 5 :
 O0Oo0oOOoooOOOOo ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 85 - 85: i1IIi
elif Ii1iI111 == 6 :
 OO0OO00ooO0 ( iIiIIi1 )
 if 100 - 100: OoooooooOO / o0000oOoOoO0o % Ooo00oOo00o + o00O0oo
elif Ii1iI111 == 7 :
 O0Ooo00o00O ( iIiIIi1 , oOO00Oo )
 if 42 - 42: Oo / IIII . o00O0oo * OOOo0
elif Ii1iI111 == 8 :
 o0o0O0oOooO00 ( iIiIIi1 , oOO00Oo )
 if 54 - 54: I1IiI * oO0o0ooO0 + Ooo00oOo00o
elif Ii1iI111 == 9 :
 FIXREPOSADDONS ( iIiIIi1 )
 if 93 - 93: OOooOOo / OOOo0
elif Ii1iI111 == 10 :
 oooOo0OOOoo0 ( )
 if 47 - 47: Oo * OoOO0ooOOoo0O
elif Ii1iI111 == 11 :
 o000 ( iIiIIi1 )
 if 98 - 98: OoOO - OoOO . o0oO0
elif Ii1iI111 == 12 :
 o00OOOOooO ( )
 if 60 - 60: OOOo0 * ii11ii1ii / O0 + o0000oOoOoO0o + IIII
elif Ii1iI111 == 13 :
 ii1iIII1ii ( )
 if 66 - 66: IIII * Oo . OoooooooOO * O0oO
elif Ii1iI111 == 14 :
 iI1IIIi11 ( iIiIIi1 )
 if 93 - 93: IIII / i1IIi
elif Ii1iI111 == 15 :
 OO0oOO0O ( )
 if 47 - 47: o0oO0 - o00O0oo
elif Ii1iI111 == 16 :
 oo0oO0oOo0O ( iIiIIi1 , oOO00Oo )
 if 98 - 98: OoOO . O0oO / I1IiI . o0oO0
elif Ii1iI111 == 17 :
 ooOoO0OoO ( iIiIIi1 , oOO00Oo )
 if 1 - 1: OoOO0ooOOoo0O
elif Ii1iI111 == 18 :
 o0OoOOoOOoo ( )
 if 87 - 87: O0 * OoOoOO00 + iIii1I11I1II1 % OoOO % i11iIiiIii - I1IiI
elif Ii1iI111 == 19 :
 Iiiii1I ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 73 - 73: oO0o0ooO0 + o00O0oo
elif Ii1iI111 == 40 :
 IiI1i ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 37 - 37: OoOO - iIii1I11I1II1 + OoOoOO00 . o00O0oo % iIii1I11I1II1
elif Ii1iI111 == 42 :
 ii1111iII ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 17 - 17: O0oO + i1IIi % O0
elif Ii1iI111 == 43 :
 I1i1i1iii ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 65 - 65: IIII
elif Ii1iI111 == 20 :
 Ii1 ( iIiIIi1 )
 if 50 - 50: OoOoOO00 / Ooo00oOo00o
elif Ii1iI111 == 22 :
 i1iii1IiiiI1i1 ( iIiIIi1 )
 if 79 - 79: ii11ii1ii - iIii1I11I1II1 % i1IIi / Oo + OoOoOO00
elif Ii1iI111 == 23 :
 Ii1iiIi11111I ( iIiIIi1 )
 if 95 - 95: OoOO
elif Ii1iI111 == 24 :
 iii1 ( iIiIIi1 )
 if 48 - 48: o0000oOoOoO0o / iIii1I11I1II1 % OoOoOO00
elif Ii1iI111 == 25 :
 i1i1Ii1IiIII ( iIiIIi1 )
 if 39 - 39: i1IIi . ii11ii1ii / o0000oOoOoO0o / o0000oOoOoO0o
elif Ii1iI111 == 26 :
 OooO00oo0O0 ( iIiIIi1 )
 if 100 - 100: OoooooooOO - OoooooooOO + IIII
elif Ii1iI111 == 27 :
 IiI11IIi11Iii ( iIiIIi1 )
 if 32 - 32: I1IiI * OOooOOo / OoooooooOO
elif Ii1iI111 == 28 :
 IiIooOoOo0O00oo ( iIiIIi1 )
 if 90 - 90: O0oO
elif Ii1iI111 == 29 :
 O00oo0oOoO00O ( iIiIIi1 )
 if 35 - 35: OoOoOO00 / o00O0oo
elif Ii1iI111 == 30 :
 O0ooO0Oo00o ( iIiIIi1 )
 if 79 - 79: I1IiI + O0oO * oO0o0ooO0 * o00O0oo
elif Ii1iI111 == 31 :
 OOOO00 ( iIiIIi1 )
 if 53 - 53: OoOO0ooOOoo0O / Oo
elif Ii1iI111 == 32 :
 O0oOoOOOoOO ( )
 if 10 - 10: ii11ii1ii . OOooOOo
elif Ii1iI111 == 33 :
 O0o ( )
 if 75 - 75: O0 * i1IIi - o0000oOoOoO0o / OoOO0ooOOoo0O % OoOO0ooOOoo0O / I1IiI
elif Ii1iI111 == 35 :
 O0o000Oo ( iIiIIi1 )
 if 5 - 5: O0 - oO0o0ooO0 / O0oO . OOooOOo
elif Ii1iI111 == 34 :
 oo000o ( iIiIIi1 )
 if 7 - 7: ii11ii1ii - I1IiI
elif Ii1iI111 == 36 :
 O000oo ( iIiIIi1 )
 if 54 - 54: OoOO / iIii1I11I1II1 / OoooooooOO . i1IIi - I1IiI
elif Ii1iI111 == 37 :
 o0OOOO00O0Oo ( iIiIIi1 )
 if 57 - 57: iIii1I11I1II1 * o00O0oo * oO0o0ooO0 / OoOO
elif Ii1iI111 == 38 :
 IIi ( iIiIIi1 )
 if 46 - 46: o00O0oo
elif Ii1iI111 == 41 :
 OoOooOo00o ( I11II11IiI11 )
 if 61 - 61: OOooOOo / o0oO0 - OoOoOO00
elif Ii1iI111 == 39 :
 Oo0O0O ( iIiIIi1 )
 if 87 - 87: ii11ii1ii / OOOo0
elif Ii1iI111 == 45 :
 TEXTS ( )
 if 45 - 45: I1IiI * o0oO0 / OoooooooOO + Ooo00oOo00o . O0oO / Ooo00oOo00o
elif Ii1iI111 == 46 :
 IIi1ii ( )
 if 64 - 64: o00O0oo / i1IIi % OOOo0 - OOooOOo
elif Ii1iI111 == 47 :
 GEVID ( )
 if 11 - 11: ii11ii1ii - OoooooooOO
elif Ii1iI111 == 48 :
 OooOo0ooo ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 16 - 16: IIII % OoooooooOO - o0oO0 * o00O0oo - o00O0oo
elif Ii1iI111 == 49 :
 oooooOoo0ooo ( )
 if 27 - 27: IIII + iIii1I11I1II1 / Oo + Ooo00oOo00o % Oo + Ooo00oOo00o
elif Ii1iI111 == 222 :
 IiI1iI1IiiIi1 ( iIiIIi1 )
 if 77 - 77: Oo * o0oO0 % o00O0oo
elif Ii1iI111 == 333 :
 I1i1i1 ( iIiIIi1 )
 if 2 - 2: o0000oOoOoO0o / Oo / o00O0oo / ii11ii1ii / OoooooooOO
 if 22 - 22: iIii1I11I1II1 * OOOo0 / o0000oOoOoO0o + I1IiI
elif Ii1iI111 == 1001 :
 o0OOOOOo00 ( )
 if 98 - 98: OoOO0ooOOoo0O
elif Ii1iI111 == 1005 :
 OooO0O0Ooo ( )
 if 69 - 69: OoOoOO00 + Oo - OoOO . Oo / iIii1I11I1II1 * iIii1I11I1II1
elif Ii1iI111 == 1007 :
 oO0OIIIiIi1iiI ( iIiIIi1 )
 if 75 - 75: Ooo00oOo00o % OoooooooOO
elif Ii1iI111 == 1010 :
 oOOOooO ( iIiIIi1 )
 if 16 - 16: O0 / i1IIi
elif Ii1iI111 == 1011 :
 iI ( iIiIIi1 )
 if 58 - 58: OOooOOo / i11iIiiIii / O0 % o0000oOoOoO0o % OOOo0
elif Ii1iI111 == 1030 :
 i1II11I11ii1 ( )
 if 86 - 86: IIII + I1IiI / OOOo0 + o0000oOoOoO0o % o0000oOoOoO0o / i11iIiiIii
elif Ii1iI111 == 1031 :
 OOoO0oO00o ( iIiIIi1 , i1iIIIi1i )
 if 12 - 12: I1IiI + OOooOOo . O0oO
elif Ii1iI111 == 1006 :
 Parse . ParseURL ( iIiIIi1 )
 if 52 - 52: Ooo00oOo00o
elif Ii1iI111 == 2030 :
 Parse . addonParseURL ( iIiIIi1 )
 if 4 - 4: o00O0oo % ii11ii1ii + o0000oOoOoO0o - ii11ii1ii
elif Ii1iI111 == 2031 :
 Parse . apkParseURL ( iIiIIi1 )
 if 98 - 98: o00O0oo - O0 * OoOO * o00O0oo * o00O0oo
elif Ii1iI111 == 1002 :
 I1iIiIii ( iIiIIi1 )
 if 44 - 44: IIII + o0000oOoOoO0o
elif Ii1iI111 == 1003 :
 OO0 ( iIiIIi1 , i1iIIIi1i )
 if 66 - 66: OoOO
elif Ii1iI111 == 1004 :
 I1iiI1iiI1i1 ( iIiIIi1 )
 if 34 - 34: oO0o0ooO0 % i11iIiiIii + i11iIiiIii - oO0o0ooO0
elif Ii1iI111 == 1008 :
 ii1II1II ( )
 if 2 - 2: OoOoOO00 + i1IIi
elif Ii1iI111 == 1009 :
 M3UPLAY ( iIiIIi1 )
 if 68 - 68: OoOO0ooOOoo0O + o00O0oo
elif Ii1iI111 == 2001 :
 IIi1i1 ( iIiIIi1 )
 if 58 - 58: IIII * o00O0oo . i1IIi
elif Ii1iI111 == 1013 :
 IIIIiII1i ( )
 if 19 - 19: OoOO
elif Ii1iI111 == 1014 :
 oOO0o00o0Oo0O ( )
 if 85 - 85: o0oO0 - OOOo0 / i1IIi / Ooo00oOo00o / OoOoOO00
elif Ii1iI111 == 1015 :
 iIIi1iiII ( iIiIIi1 )
 if 94 - 94: iIii1I11I1II1 + IIII
elif Ii1iI111 == 1016 :
 IIIIIIi ( iIiIIi1 )
 if 44 - 44: Ooo00oOo00o + o0000oOoOoO0o % Ooo00oOo00o + i1IIi + oO0o0ooO0 + O0
elif Ii1iI111 == 1023 :
 O00Oo000ooO0 ( )
 if 18 - 18: iIii1I11I1II1 % iIii1I11I1II1 % OoOO + OOOo0 % o0oO0 / o00O0oo
elif Ii1iI111 == 1024 :
 IiI1 ( )
 if 36 - 36: I1IiI . i11iIiiIii
elif Ii1iI111 == 1025 :
 iiIiII ( iIiIIi1 )
 if 81 - 81: Oo * oO0o0ooO0 * Ooo00oOo00o
elif Ii1iI111 == 4001 :
 ooo ( )
 if 85 - 85: O0 * OoOO
elif Ii1iI111 == 4002 :
 ii1I1i1I ( )
 if 39 - 39: OoOoOO00 * OOOo0 - iIii1I11I1II1
elif Ii1iI111 == 4003 :
 I1III ( )
 if 25 - 25: OoooooooOO . o00O0oo % oO0o0ooO0 . IIII
elif Ii1iI111 == 3000 :
 II111I1 ( )
 if 67 - 67: OoooooooOO + O0oO / o0oO0
elif Ii1iI111 == 404 :
 o0Iiii ( oOO00Oo , iIiIIi1 , i1iIIIi1i )
 if 75 - 75: IIII / OoooooooOO . OOOo0 + O0oO - OoOoOO00
elif Ii1iI111 == 7030 :
 OO0Oo ( )
 if 33 - 33: IIII / IIII . i11iIiiIii * ii11ii1ii + OOooOOo
elif Ii1iI111 == 7021 :
 oO0Oo00oo ( oOO00Oo )
 if 16 - 16: IIII
elif Ii1iI111 == 7022 :
 O0OOoOOOO00O ( oOO00Oo )
 if 10 - 10: I1IiI . IIII * iIii1I11I1II1 - OoOO - I1IiI / O0oO
elif Ii1iI111 == 7000 :
 ii11iI1iIiIi ( oOO00Oo , iIiIIi1 , img )
 if 13 - 13: OoOO + I1IiI % IIII % OoooooooOO
elif Ii1iI111 == 7050 :
 O0o00oo0OO0 ( )
 if 22 - 22: O0oO
elif Ii1iI111 == 7051 :
 O000O ( iIiIIi1 )
 if 23 - 23: O0
elif Ii1iI111 == 7060 :
 iI1iIIiii ( )
 if 41 - 41: i1IIi . OoOO0ooOOoo0O / o0oO0 / OOooOOo % IIII - o00O0oo
elif Ii1iI111 == 7061 :
 iI1I1I1i1i ( iIiIIi1 )
 if 14 - 14: ii11ii1ii - i11iIiiIii * O0oO
elif Ii1iI111 == 7063 :
 O0000oO0o00 ( iIiIIi1 )
 if 39 - 39: OoooooooOO
elif Ii1iI111 == 7062 :
 II1Iiii11111 ( iIiIIi1 )
 if 19 - 19: i11iIiiIii
elif Ii1iI111 == 7064 :
 NATatozcat ( )
 if 80 - 80: OOOo0
elif Ii1iI111 == 7067 :
 i111I1iiIiII ( iIiIIi1 )
 if 58 - 58: OoOO + ii11ii1ii % I1IiI
elif Ii1iI111 == 7066 :
 NATatozA ( iIiIIi1 )
 if 22 - 22: iIii1I11I1II1 - o00O0oo / OOOo0 * IIII
elif Ii1iI111 == 7065 :
 OoO00ooO ( iIiIIi1 )
 if 26 - 26: OOooOOo + OoOO0ooOOoo0O - OOooOOo + Oo . OoOO
elif Ii1iI111 == 7070 :
 o00OOo000O ( )
 if 97 - 97: i1IIi
elif Ii1iI111 == 7071 :
 DIZIlist ( iIiIIi1 )
 if 46 - 46: ii11ii1ii
elif Ii1iI111 == 7072 :
 DIZIpull ( iIiIIi1 )
 if 30 - 30: Ooo00oOo00o / O0 * OOooOOo * O0oO + OoooooooOO * oO0o0ooO0
elif Ii1iI111 == 7073 :
 WATCHDIZI ( iIiIIi1 )
 if 23 - 23: o0000oOoOoO0o
elif Ii1iI111 == 7002 :
 iI1i ( )
 if 36 - 36: IIII . oO0o0ooO0 - i1IIi + O0oO
elif Ii1iI111 == 7003 :
 iI11111ii11 ( iIiIIi1 )
 if 54 - 54: OoooooooOO . OoOO - oO0o0ooO0
elif Ii1iI111 == 7004 :
 o0oo0000 ( iIiIIi1 )
 if 76 - 76: O0oO
elif Ii1iI111 == 7020 :
 Iiii1Ii1I ( iIiIIi1 )
 if 61 - 61: o0oO0 / OoOoOO00 * o0oO0 * I1IiI * O0oO . i11iIiiIii
elif Ii1iI111 == 7001 :
 i111I11I ( )
 if 26 - 26: O0oO / o0oO0 - Ooo00oOo00o . iIii1I11I1II1
elif Ii1iI111 == 7010 :
 I1i ( iIiIIi1 )
 if 83 - 83: o0oO0 % o00O0oo / Oo - oO0o0ooO0 / O0
elif Ii1iI111 == 7011 :
 iii ( iIiIIi1 )
 if 97 - 97: iIii1I11I1II1 * o0000oOoOoO0o
elif Ii1iI111 == 7012 :
 IiiIi ( iIiIIi1 )
 if 95 - 95: Ooo00oOo00o
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
 OoO ( )
elif Ii1iI111 == 7019 :
 CNF_Studio_Indexer . List_Movies ( iIiIIi1 )
elif Ii1iI111 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iIiIIi1 )
elif Ii1iI111 == 7024 :
 CNF_Studio_Indexer . Box_Office ( iIiIIi1 )
 if 68 - 68: iIii1I11I1II1 . iIii1I11I1II1 / I1IiI - OoOoOO00 - iIii1I11I1II1
elif Ii1iI111 == 8000 :
 II1iIii111iII ( )
elif Ii1iI111 == 8001 :
 oOOOoo0o ( )
elif Ii1iI111 == 8002 :
 i111Iii ( )
elif Ii1iI111 == 8003 :
 iIi1IIiIII1 ( )
elif Ii1iI111 == 8004 :
 I1iIIIiI ( )
elif Ii1iI111 == 8005 :
 ooooo0Oo0 ( )
elif Ii1iI111 == 8006 :
 oOo00o ( oOO00Oo , iIiIIi1 )
elif Ii1iI111 == 8030 :
 O000OOOOOo ( iIiIIi1 )
elif Ii1iI111 == 8045 :
 OOo00OO00Oo ( )
elif Ii1iI111 == 8046 :
 I1I1I11Ii ( iIiIIi1 )
elif Ii1iI111 == 8047 :
 IiI1IIIII1I ( iIiIIi1 )
elif Ii1iI111 == 8040 :
 oOO0o0oo0 ( )
elif Ii1iI111 == 8041 :
 oOo000O ( iIiIIi1 )
elif Ii1iI111 == 8042 :
 oO0Ooo0OooOOo ( iIiIIi1 )
elif Ii1iI111 == 8043 :
 yt . PlayVideo ( iIiIIi1 )
elif Ii1iI111 == 8044 :
 O00o0O ( iIiIIi1 )
elif Ii1iI111 == 8060 :
 ooOii1I11Iii1i ( )
elif Ii1iI111 == 8061 :
 i1II1Ii1i1 ( iIiIIi1 )
elif Ii1iI111 == 8070 :
 iIIOOoO0oO00o ( )
elif Ii1iI111 == 8071 :
 iiiiii1 ( iIiIIi1 )
elif Ii1iI111 == 7080 :
 OO0o0oO0O000o ( iIiIIi1 )
elif Ii1iI111 == 8090 :
 iiII1IiIi1iI1 ( )
elif Ii1iI111 == 8091 :
 oOiiI1Ii11II1I ( iIiIIi1 )
elif Ii1iI111 == 8092 :
 I1Ii11II1I1 ( iIiIIi1 )
elif Ii1iI111 == 8081 :
 I1ii1 ( )
elif Ii1iI111 == 8062 :
 OOOO0oOo00O ( iIiIIi1 )
elif Ii1iI111 == 8063 :
 ooOoooo0 ( iIiIIi1 )
elif Ii1iI111 == 8050 :
 IiiiiI1i1Iii ( )
elif Ii1iI111 == 8051 :
 oo00oO0o ( iIiIIi1 )
elif Ii1iI111 == 8052 :
 OOoooO00o0oo0 ( iIiIIi1 )
elif Ii1iI111 == 8085 :
 II1IIi ( )
elif Ii1iI111 == 8086 :
 ii1111Ii1i ( iIiIIi1 )
elif Ii1iI111 == 8087 :
 oO00oo000O ( iIiIIi1 )
elif Ii1iI111 == 8088 :
 ii11 ( iIiIIi1 , oOO00Oo )
elif Ii1iI111 == 9000 :
 Oo0oOOo ( )
elif Ii1iI111 == 1111 :
 i11iI1 ( )
elif Ii1iI111 == 9001 :
 I1I1 ( )
elif Ii1iI111 == 9002 :
 oOOOo ( )
elif Ii1iI111 == 9003 :
 OO0ooo0 ( )
elif Ii1iI111 == 50 :
 o00oO0oo0OO ( iIiIIi1 )
elif Ii1iI111 == 9020 :
 iII ( )
elif Ii1iI111 == 9021 :
 ooooOoo0OO ( )
elif Ii1iI111 == 9022 :
 Oo0 ( )
elif Ii1iI111 == 9023 :
 O0000Oo00o ( )
elif Ii1iI111 == 9024 :
 o00iIiiiII ( iIiIIi1 )
elif Ii1iI111 == 9030 :
 OOooO0Oo00 ( iIiIIi1 )
elif Ii1iI111 == 9031 :
 iIIIIIIIiIII ( iIiIIi1 )
elif Ii1iI111 == 9032 :
 o0oo0o00ooO00 ( iIiIIi1 )
elif Ii1iI111 == 9033 :
 IIiIiiI1i ( iIiIIi1 )
elif Ii1iI111 == 7085 :
 ii1IIiI1IIi ( iIiIIi1 )
elif Ii1iI111 == 7086 :
 Oooo00 ( iIiIIi1 )
elif Ii1iI111 == 7087 :
 OoooO0 ( i1iI11i1ii11 )
elif Ii1iI111 == 9666 :
 IIiIIIi1iii1 ( iIiIIi1 )
elif Ii1iI111 == 10000 : IIii1Ii1 ( )
elif Ii1iI111 == 10001 : iiiII ( )
elif Ii1iI111 == 10002 : ooooOoO0O ( )
elif Ii1iI111 == 10003 : IIi1ii1Ii ( )
elif Ii1iI111 == 10004 : Ii11 ( )
elif Ii1iI111 == 10005 : OOoo ( )
elif Ii1iI111 == 10006 : O0O0Oo00 ( iIiIIi1 )
elif Ii1iI111 == 10007 : oOoOO ( iIiIIi1 , i1iIIIi1i )
elif Ii1iI111 == 10008 : iiii111IiIIi1 ( )
elif Ii1iI111 == 10009 : ii111i1iI ( )
elif Ii1iI111 == 10010 : iiIIii ( iIiIIi1 )
elif Ii1iI111 == 10011 : ooOOoOo ( iIiIIi1 )
elif Ii1iI111 == 10012 : OOOO0O00o ( iIiIIi1 )
elif Ii1iI111 == 10013 : IiIii1ii ( iIiIIi1 )
elif Ii1iI111 == 10014 : ooo000ooO0000 ( )
elif Ii1iI111 == 10015 : O000OOO0OOo ( )
elif Ii1iI111 == 10016 : OO0ooo0o0O0Oooooo ( iIiIIi1 )
elif Ii1iI111 == 10017 : IiII ( )
elif Ii1iI111 == 10018 : IIiI1I1 ( )
elif Ii1iI111 == 10019 : o0oo ( )
elif Ii1iI111 == 10020 : ooOoO0 ( )
elif Ii1iI111 == 10021 : OoooO0o ( )
elif Ii1iI111 == 10022 : oO00oOo0OOO ( iIiIIi1 )
elif Ii1iI111 == 10023 : I1IIi ( oOO00Oo , iIiIIi1 )
elif Ii1iI111 == 10024 : oOo00oOOOOO ( iIiIIi1 )
elif Ii1iI111 == 10025 : oOOoOo ( )
elif Ii1iI111 == 10026 : O00oO ( )
elif Ii1iI111 == 10027 : OOOoO000 ( )
elif Ii1iI111 == 10028 : oOOoo0o0OOOO ( )
elif Ii1iI111 == 10029 : oOO0 ( )
elif Ii1iI111 == 423 : Iii ( iIiIIi1 )
elif Ii1iI111 == 426 : oO0oOOO0Ooo ( iIiIIi1 )
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
elif Ii1iI111 == 10040 : oooo00 ( )
elif Ii1iI111 == 10041 : o0Oii1111i ( iIiIIi1 )
elif Ii1iI111 == 10042 : i1iIIIIIIiII1 ( iIiIIi1 )
elif Ii1iI111 == 10043 : o0oooO ( )
elif Ii1iI111 == 10044 : i11ii ( iIiIIi1 )
elif Ii1iI111 == 10045 : I1iI1I1 ( iIiIIi1 )
elif Ii1iI111 == 10046 : i1oO ( iIiIIi1 )
elif Ii1iI111 == 10047 : IiIIi1I1I11Ii ( iIiIIi1 )
elif Ii1iI111 == 10048 : oO0oooooo ( iIiIIi1 )
elif Ii1iI111 == 10049 : Ooo0O0 ( iIiIIi1 )
elif Ii1iI111 == 10050 : IiI ( )
elif Ii1iI111 == 10051 : o0O0oo0 ( )
elif Ii1iI111 == 10052 : iiI ( )
elif Ii1iI111 == 10053 : Addon ( iIiIIi1 )
elif Ii1iI111 == 10054 : ii111I11Ii ( iIiIIi1 , oOO00Oo )
elif Ii1iI111 == 10055 :
 OO000o00 ( "addFavorite" )
 try :
  oOO00Oo = oOO00Oo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOO00Oo = oOO00Oo . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0000 ( oOO00Oo , iIiIIi1 , i1iIIIi1i , iI1iIIiiii , O0oO0O )
elif Ii1iI111 == 10056 :
 OO000o00 ( "rmFavorite" )
 try :
  oOO00Oo = oOO00Oo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOO00Oo = oOO00Oo . split ( '  - ' ) [ 0 ]
 except :
  pass
 Iii111Ii ( oOO00Oo )
elif Ii1iI111 == 10057 :
 OO000o00 ( "getFavorites" )
 IiI1I11iIii ( )
elif Ii1iI111 == 10058 : Ii11iII1 ( )
elif Ii1iI111 == 20000 : o0OOOOooo ( )
elif Ii1iI111 == 20001 : o0OOo0o0O0O ( )
elif Ii1iI111 == 20002 : O0O0o0oOOO ( iIiIIi1 )
elif Ii1iI111 == 20003 : OooooO0oOOOO ( iIiIIi1 )
elif Ii1iI111 == 20004 : o00O ( iIiIIi1 )
if 75 - 75: o0oO0 . OOOo0 * OoOoOO00
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
