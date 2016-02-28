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
O0OoO000O0OO = "2.4.3"
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
O0O = xbmc . translatePath ( o0oOoO00o . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
O00o0OO = os . path . join ( O0O , 'favorites' )
if os . path . exists ( O00o0OO ) == True :
 I11i1 = open ( O00o0OO ) . read ( )
else : I11i1 = [ ]
iIi1ii1I1 = o0oOoO00o . getSetting ( 'debug' )
if 71 - 71: O0oO . O0
def o0OO0oo0oOO ( ) :
 oo0oooooO0 ( '[COLORgreen]WIZARD[/COLOR]' , OooO0 , 4001 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]STREAMS[/COLOR]' , OooO0 , 4002 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]MUSIC[/COLOR]' , OooO0 , 4003 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 if 19 - 19: o0000oOoOoO0o + o0oO0
 oo0oooooO0 ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , OooO0 , 32 , iIii1 + 'builderstoolbox.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SOURCE LIST[/COLOR]' , OooO0 , 46 , iIii1 + 'sources.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]MAINTENANCE[/COLOR]' , OooO0 , 3 , iIii1 + 'MAIN6.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , iIii1 + 'ADDONS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]APK TOOL[/COLOR]' , OooO0 , 2 , iIii1 + 'APK.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , OooO0 , 39 , iIii1 + 'RSS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]ADDONS PACKS[/COLOR]' , OooO0 , 30 , iIii1 + 'ADDONP.png' , iI111I11I1I1 , '' )
 ooo ( 'movies' , 'MAIN' )
 if 18 - 18: OOooOOo
def I1i1I1II ( ) :
 oo0oooooO0 ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , OooO0 , 49 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]WIPE GENIE[/COLOR]' , OooO0 , 41 , iIii1 + 'wipegenie.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]WISHES PC[/COLOR]' , OooO0 , 1 , iIii1 + 'WISHESPC.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]WISHES ANDROID[/COLOR]' , OooO0 , 44 , iIii1 + 'WISHESAN.png' , iI111I11I1I1 , '' )
 ooo ( 'movies' , 'MAIN' )
def i1IiIiiI ( ) :
 oo0oooooO0 ( '[COLORgreen]FAVOURITES[/COLOR]' , OooO0 , 10057 , iIii1 + 'FAVORITES.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SEARCH[/COLOR]' , OooO0 , 9000 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]DONATORS LIST[/COLOR]' , '' , 10058 , iIii1 + 'GTVIPTV.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]POPCORN BOX[/COLOR]' , OooO0 , 7061 , iIii1 + 'popcorn.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , iIii1 + 'WATCHSERIES.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]RECENT EPISODES[/COLOR]' , OooO0 , 8081 , iIii1 + 'recent.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , OooO0 , 1023 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) ) , 1016 , iIii1 + 'reap.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]PANDORAS BOX[/COLOR]' , OooO0 , 10025 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]HEROVISION[/COLOR]' , 'http://herovision.x10host.com/vod/main.php' , 1016 , iIii1 + 'hero.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]FITNESS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iIii1 + 'FITNESS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , OooO0 , 8040 , iIii1 + 'documentary.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]ANIME[/COLOR]' , OooO0 , 1001 , iIii1 + 'anime.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]M3U STREAMS[/COLOR]' , OooO0 , 8070 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , OooO0 , 3000 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
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
 if 16 - 16: O0 - O0oO * iIii1I11I1II1 + oO0o0ooO0
 if 50 - 50: OoOoOO00 - o0oO0 * ii11ii1ii / O0oO + OOooOOo
 ooo ( 'movies' , 'MAIN' )
 if 88 - 88: o00O0oo / O0oO + oO0o0ooO0 - OoOoOO00 / o0oO0 - I1IiI
def IIIIii ( ) :
 if i1iiIII111ii == 'insert_password' :
  Oo0o0000o0o0 . ok ( '[COLOR=white]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with stream costs' , 'Donate to http://architects.x10host.com/' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
 else :
  oo0oooooO0 ( '[COLORgreen]DONATORS LIST[/COLOR]' , OooO0 + '/thelist.m3u' , 7080 , iIii1 + 'GTVIPTV.png' , iI111I11I1I1 , '' )
  if 70 - 70: o00O0oo / o0000oOoOoO0o . oO0o0ooO0 % Oo
  if 67 - 67: I1IiI * OOooOOo . IIII - Ooo00oOo00o * OOooOOo
def IIiI1I ( ) :
 oo0oooooO0 ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10001 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Dizzy TV[/COLOR]' , '' , 10018 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Football[/COLOR]' , '' , 10002 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Izle Films[/COLOR]' , '' , 10030 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10003 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 if 70 - 70: IIII * Oo * o0000oOoOoO0o / o00O0oo
 if 88 - 88: O0
def O0OoO0O00o0oO ( ) :
 oo0oooooO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , OooO0 , 1024 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 if 15 - 15: o00O0oo - O0 / OoOO * i1IIi
def oooo000 ( ) :
 oo0oooooO0 ( '[COLORgreen]Live Tv[/COLOR]' , OooO0 , 9021 , iIii1 + 'english.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]XXX[/COLOR]' , OooO0 , 9022 , iIii1 + 'xxx.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Hd VOD[/COLOR]' , OooO0 , 9023 , iIii1 + 'vod(1).png' , iI111I11I1I1 , '' )
 if 16 - 16: ii11ii1ii + Ooo00oOo00o - OoOoOO00
 if 85 - 85: I1IiI + i1IIi
def Oo0OoO00oOO0o ( ) :
 oo0oooooO0 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , OooO0 , 9001 , iIii1 + 'MOVIESv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , OooO0 , 9002 , iIii1 + 'TVSHOWSv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , iIii1 + 'ORIGINCARTOON' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , OooO0 , 9003 , iIii1 + 'livetv.png' , iI111I11I1I1 , '' )
 if 80 - 80: OoOO + OoOO0ooOOoo0O - OoOO0ooOOoo0O % oO0o0ooO0
 if 63 - 63: OOOo0 - ii11ii1ii + O0 % o0000oOoOoO0o / iIii1I11I1II1 / OOooOOo
def O0o0O00Oo0o0 ( ) :
 oo0oooooO0 ( '[COLORgreen]RADIO[/COLOR]' , OooO0 , 1013 , iIii1 + 'radio.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]MUSIC[/COLOR]' , OooO0 , 1030 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , OooO0 + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , OooO0 , 1111 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 if 87 - 87: o0oO0 * Oo % i11iIiiIii % I1IiI - OoOO0ooOOoo0O
 ooo ( 'movies' , 'MAIN' )
 if 68 - 68: O0oO % i1IIi . IIII . ii11ii1ii
def o0 ( ) :
 oo0oOo ( 'DELETE CACHE' , 'url' , 14 , iIii1 + 'MAIN5.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'DELETE PACKAGES' , 'url' , 6 , iIii1 + 'MAIN4.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'FORCE REFRESH' , 'url' , 10 , iIii1 + 'MAIN3.png' , iI111I11I1I1 , 'Force Refresh All Repos' )
 if 89 - 89: I1IiI
 oo0oOo ( 'CHECK MY IP' , 'url' , 12 , iIii1 + 'MAIN2.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iIii1 + 'MAIN1.png' , iI111I11I1I1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 oo0oooooO0 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , OooO0 , 4 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]URL FIXES[/COLOR]' , OooO0 , 20 , iIii1 + 'URLFIX.png' , iI111I11I1I1 , '' )
 ooo ( 'movies' , 'MAIN' )
 if 68 - 68: Ooo00oOo00o * OoooooooOO % O0 + Ooo00oOo00o + o0oO0
 if 4 - 4: o0oO0 + O0 * OoOO0ooOOoo0O
def OOoo0O ( ) :
 oo0oooooO0 ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iIii1 + 'repos.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]NEW[/COLOR]' , OooO0 , 22 , iIii1 + 'NEW.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]IPTV[/COLOR]' , OooO0 , 23 , iIii1 + 'IPTV.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]VIDEO[/COLOR]' , OooO0 , 24 , iIii1 + 'VIDEO.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SPORTS[/COLOR]' , OooO0 , 25 , iIii1 + 'SPORTS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]KIDS[/COLOR]' , OooO0 , 26 , iIii1 + 'KIDS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]MUSIC[/COLOR]' , OooO0 , 27 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]PROGRAMS[/COLOR]' , OooO0 , 28 , iIii1 + 'PROGRAMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , iIii1 + 'XXX.png' , iI111I11I1I1 , '' )
 ooo ( 'movies' , 'MAIN' )
 if 67 - 67: i11iIiiIii - i1IIi % ii11ii1ii . O0
 if 77 - 77: IIII / OOOo0
def I1 ( ) :
 oo0oOo ( 'CHECK ADVANCED XML' , OooO0 , 8 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'MUCKYS XML' , OooO0 + '/wizard/muckys.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oOo ( '0CACHE XML' , OooO0 + '/wizard/0cache.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'MIKEY1234 XML' , OooO0 + '/wizard/mikey.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'TUXENS XML' , OooO0 + '/wizard/tuxens.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'P2P RECOMMENDED XML1' , OooO0 + '/wizard/p2p1.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'P2P RECOMMENDED XML2' , OooO0 + '/wizard/p2p2.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'DELETE XML' , OooO0 , 11 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 ooo ( 'movies' , 'MAIN' )
 if 15 - 15: OoOoOO00
def Ii ( ) :
 oo0oOo ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 oo0oOo ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 if 79 - 79: OoooooooOO / O0
def OO0OoO0o00 ( ) :
 oo0oOo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , OooO0 + '/wizard/customftv/ftvguide-addons.zip' , 5 , iIii1 + 'FTV4.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'FTV GUIDE FIRST RUN SETTINGS' , OooO0 + '/wizard/customftv/settings.xml' , 17 , iIii1 + 'FTV3.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iIii1 + 'FTV1.png' , iI111I11I1I1 , '' )
 oo0oOo ( 'RESET FTV DATABASE' , 'url' , 18 , iIii1 + 'FTV2.png' , iI111I11I1I1 , '' )
 if 53 - 53: O0 * Ooo00oOo00o + OoOO0ooOOoo0O
 if 50 - 50: O0 . O0 - OoOO / OOOo0 - OOooOOo * I1IiI
 if 61 - 61: o0000oOoOoO0o
def O0oOoOOOoOO ( ) :
 oo0oooooO0 ( '[COLORgreen]SKINS[/COLOR]' , OooO0 , 33 , iIii1 + 'skinp.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , OooO0 , 34 , iIii1 + 'artp.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , ii11iIi1I , 35 , iIii1 + 'GUI.png' , iI111I11I1I1 , '' )
 ooo ( 'movies' , 'MAIN' )
 if 38 - 38: O0oO
def Ii1 ( url ) :
 OOooOO000 = OOoOoo ( oO0000OOo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 58 - 58: Ooo00oOo00o % i11iIiiIii . oO0o0ooO0 / OoOO
def O0o ( ) :
 oo0oooooO0 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , OooO0 , 36 , iIii1 + 'GSKIN.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]HELIX SKINS[/COLOR]' , OooO0 , 37 , iIii1 + 'HSKIN.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , ii11iIi1I , 38 , iIii1 + 'ISKIN.png' , iI111I11I1I1 , '' )
 ooo ( 'movies' , 'MAIN' )
 if 59 - 59: OOOo0 + OOOo0 + OOooOOo / iIii1I11I1II1
def O000oo ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + IIi1I11I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 63 - 63: OoooooooOO - Ooo00oOo00o . OoOoOO00 / OOooOOo . I1IiI / O0
def o0OOOO00O0Oo ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 90 - 90: OOooOOo % i1IIi / Ooo00oOo00o
def IIi ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 91 - 91: ii11ii1ii + OOOo0 . OoOO0ooOOoo0O * ii11ii1ii + OOOo0 * Oo
def O000OOOOOo ( url ) :
 OOooOO000 = OOoOoo ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * oO0o0ooO0 % i11iIiiIii * OOOo0
def oo000o ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + iiIi1IIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 40 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 84 - 84: o0oO0 * OoOoOO00 + Oo
def O0ooO0Oo00o ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + ooO0oOOooOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 38 - 38: O0oO
def Ooo00o0Oooo ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 2031 , iIii1 + 'APK.png' )
  if 5 - 5: OoooooooOO % I1IiI % OoOO % oO0o0ooO0
def Iiiii1I ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( oO0 , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0OO0O = os . path . join ( O0oO0 , name + '.apk' )
 try :
  os . remove ( O0OO0O )
 except :
  pass
 downloader . download ( url , O0OO0O , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 81 - 81: OoOO . OOooOOo % O0 / OOOo0 - OoOO
def Ii1I1i ( url ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0OO0O = os . path . join ( O0oO0 , oOO00Oo + '.mp4' )
 try :
  os . remove ( O0OO0O )
 except :
  pass
 downloader . download ( url , O0OO0O , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 99 - 99: OoOO . oO0o0ooO0 + o0oO0 % OoOO . i11iIiiIii % O0
 if 78 - 78: ii11ii1ii + OoOO0ooOOoo0O - O0oO
def IIIIii1I ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0OO0O = os . path . join ( O0oO0 , name )
 try :
  os . remove ( O0OO0O )
 except :
  pass
 downloader . download ( url , O0OO0O , i1111 )
 IiI1i = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IiI1i
 print '======================================='
 extract . all ( O0OO0O , IiI1i , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 92 - 92: IIII . IIII + Ooo00oOo00o
 if 9 - 9: OOOo0 * O0 + IIII - o0000oOoOoO0o * O0oO
def Oooo0oOO ( url ) :
 OOooOO000 = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 try :
  OOooOO000 = OOoOoo ( Ooo00O00o + oooOOOOO + O0O00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
  for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
   oo0oooooO0 ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 except : pass
 ooo ( 'movies' , 'INFO' )
 if 97 - 97: O0 * OoooooooOO . OoooooooOO
 if 33 - 33: O0oO + oO0o0ooO0 * OoOO / iIii1I11I1II1 - OOOo0
def O0oOOO0ooOOO0OOO ( url ) :
 OOooOO000 = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 43 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 try :
  OOooOO000 = OOoOoo ( Ooo00O00o + oooOOOOO + O0O00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
  for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
   oo0oooooO0 ( oOO00Oo , url , 43 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 except : pass
 ooo ( 'movies' , 'INFO' )
 if 63 - 63: I1IiI * oO0o0ooO0
 if 69 - 69: O0 . Ooo00oOo00o
def ii1111iII ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 O0OO0O = os . path . join ( O0oO0 , name + '.zip' )
 try :
  os . remove ( O0OO0O )
 except :
  pass
 downloader . download ( url , O0OO0O , i1111 )
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( O0OO0O , iiiiI , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oooOo0OOOoo0 ( )
 if 51 - 51: Oo / I1IiI . OoOO0ooOOoo0O * OOooOOo + Ooo00oOo00o * IIII
 if 73 - 73: Ooo00oOo00o + OoooooooOO - O0 - o00O0oo - OoOoOO00
def O0Oo0oOOoooOOOOo ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0OO0O = os . path . join ( O0oO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0OO0O )
 except :
  pass
 downloader . download ( url , O0OO0O , i1111 )
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( O0OO0O , iiiiI , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 o0oO0O0o0O00O ( )
 if 80 - 80: i11iIiiIii % o0oO0 + o00O0oo % o0000oOoOoO0o - ii11ii1ii
def I1i1i1iii ( name , url , description ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0OO0O = os . path . join ( O0oO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0OO0O )
 except :
  pass
 downloader . download ( url , O0OO0O , i1111 )
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( O0OO0O , iiiiI , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 16 - 16: o00O0oo + IIII * O0 % i1IIi . OOOo0
 if 67 - 67: OoooooooOO / OOOo0 * o00O0oo + o0000oOoOoO0o
def OooOo0ooo ( name , url , description ) :
 iiiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 O0OO0O = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print iiiiI
 print '======================================='
 extract . all ( O0OO0O , iiiiI , i1111 )
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
  if 52 - 52: o0oO0 . oO0o0ooO0 + O0oO
def iiii1IIi ( ) :
 if 33 - 33: I1IiI * OoOO0ooOOoo0O - OoOoOO00
 oo0oooooO0 ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 if 83 - 83: I1IiI - o00O0oo / o0000oOoOoO0o / O0oO + OoOO - O0
def I11I1i1iIII1I ( ) :
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 OooIiIIII1i11I = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if iI in oOO00Oo . lower ( ) :
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
    oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10006 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 86 - 86: Oo . O0 - OoooooooOO . Ooo00oOo00o + o00O0oo
def OOo ( ) :
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
   oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10006 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: I1IiI * O0 . IIII * i11iIiiIii - OOOo0 * o0oO0
def OOooo0O0o0 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiii111II = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 in iiii111II :
  II1iI1I11I = I11iIiI1I1i11
 o0OO0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOooooO0Oo )
 for url in o0OO0 :
  oo0oooooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10007 , II1iI1I11I , iI111I11I1I1 , '' )
 iiIi1IIiIi = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 10007 , II1iI1I11I )
  if 44 - 44: O0 - o00O0oo - O0 % o0000oOoOoO0o . OoOO
  if 74 - 74: i11iIiiIii . OOOo0
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: OoooooooOO . Ooo00oOo00o
def oOIIiIi ( url , IMAGE ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  print oOO00Oo + '     ' + url
  if 'easy' in url :
   OOoOooOoOOOoo ( url )
   if 25 - 25: OoooooooOO - OOOo0 . OOOo0 * OoOO
   if 81 - 81: oO0o0ooO0 + IIII
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 98 - 98: OOOo0
def OOoOooOoOOOoo ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "url: '(.+?)'," ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  o00o0 ( url )
  if 50 - 50: Oo / Oo % ii11ii1ii . ii11ii1ii
  if 55 - 55: o0oO0 - o0000oOoOoO0o + OoOoOO00 + oO0o0ooO0 % o00O0oo
  if 41 - 41: i1IIi - o0000oOoOoO0o - o00O0oo
def III11I1 ( ) :
 if 36 - 36: OoOO - o00O0oo . Oo - i11iIiiIii - OoOO0ooOOoo0O * Oo
 oo0oooooO0 ( '[COLORgreen]Genres[/COLOR]' , '' , 10032 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Popular Movies[/COLOR]' , '' , 10033 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Boxsets[/COLOR]' , '' , 10034 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Search[/COLOR]' , '' , 10035 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
if 76 - 76: i11iIiiIii + OOooOOo / ii11ii1ii - Ooo00oOo00o - o00O0oo + ii11ii1ii
if 51 - 51: iIii1I11I1II1 . o0oO0 + iIii1I11I1II1
if 95 - 95: OOOo0
if 46 - 46: I1IiI + Ooo00oOo00o
if 70 - 70: oO0o0ooO0 / iIii1I11I1II1
if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / ii11ii1ii
if 96 - 96: OoooooooOO + OoOO
if 44 - 44: OoOO
if 20 - 20: o0000oOoOoO0o + o00O0oo / O0 % iIii1I11I1II1
if 88 - 88: I1IiI / OoOoOO00
if 87 - 87: ii11ii1ii - ii11ii1ii - oO0o0ooO0 + OoOO
if 82 - 82: OoOO / iIii1I11I1II1 . OOOo0 . OoOO0ooOOoo0O / OOooOOo
if 42 - 42: Oo
if 19 - 19: OoOO % ii11ii1ii * iIii1I11I1II1 + OOOo0
if 46 - 46: Oo
def i1II1I1Iii1 ( ) :
 oo0oooooO0 ( '[COLORgreen]Action[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aksiyon' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Adventure[/COLOR]' , 'http://www.izlemeyedeger.com/tur/macera' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Animation[/COLOR]' , 'http://www.izlemeyedeger.com/tur/animasyon' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Biography[/COLOR]' , 'http://www.izlemeyedeger.com/tur/biyografi' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Comedy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/komedi' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Crime[/COLOR]' , 'http://www.izlemeyedeger.com/tur/suc' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Documentary[/COLOR]' , 'http://www.izlemeyedeger.com/tur/belgesel' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Drama[/COLOR]' , 'http://www.izlemeyedeger.com/tur/dram' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Family[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aile' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Fantasy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/fantastik' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Far East[/COLOR]' , 'http://www.izlemeyedeger.com/tur/uzak-dogu' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]History[/COLOR]' , 'http://www.izlemeyedeger.com/tur/tarih' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Horror[/COLOR]' , 'http://www.izlemeyedeger.com/tur/korku' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Musical[/COLOR]' , 'http://www.izlemeyedeger.com/tur/muzikal' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Mystery[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gizem' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Romance[/COLOR]' , 'http://www.izlemeyedeger.com/tur/romantik' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Science Fiction[/COLOR]' , 'http://www.izlemeyedeger.com/tur/bilimkurgu' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Sport[/COLOR]' , 'http://www.izlemeyedeger.com/tur/spor' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Thriller[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gerilim' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]War[/COLOR]' , 'http://www.izlemeyedeger.com/tur/savas' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Western[/COLOR]' , 'http://www.izlemeyedeger.com/tur/western' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 if 30 - 30: OoooooooOO - I1IiI
def Ooo00O0o ( url ) :
 OooIiIIII1i11I = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , I11iIiI1I1i11 , Oo00o0OO0O00o , oOO00Oo in iiIi1IIiIi :
  oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) + ' ' + ( Oo00o0OO0O00o ) . replace ( '  ' , '' )
  i1iIIIi1i = I11iIiI1I1i11
  url = url
  O0Oooo ( oOO00Oo , i1iIIIi1i , url )
 iiIi1i = re . compile ( '<a href="http://www.izlemeyedeger.com/tur/(.+?)?s=(.+?)&sort=&orderby=">(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for url , I1i11111i1i11 , oOO00Oo in iiIi1i :
  oo0oooooO0 ( '[COLORgold] Page ' + oOO00Oo + '[/COLOR]' , 'http://www.izlemeyedeger.com/tur/' + url + '?s=' + I1i11111i1i11 + '&sort=&orderby=' , 10036 , '' , iI111I11I1I1 , '' )
  if 77 - 77: ii11ii1ii + Ooo00oOo00o / OoOO + O0 * OOooOOo
  if 28 - 28: o0oO0 + i11iIiiIii / o0000oOoOoO0o % I1IiI % Oo - O0
def ooo0OOO ( ) :
 if 49 - 49: i11iIiiIii % o00O0oo . I1IiI
 OooIiIIII1i11I = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbQ==' ) )
 Ii1i1iI = re . compile ( '<!-- popüler filmler -->(.+?)<!-- content -->' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for IIiI1 in Ii1i1iI :
  iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img width=".+?" height=".+?" src="(.+?)" alt=""/>.+?<span class="year">(.+?)</span>.+?<span class=".+?">(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( str ( Ii1i1iI ) )
  for iIiIIi1 , I11iIiI1I1i11 , Oo00o0OO0O00o , oOO00Oo in iiIi1IIiIi :
   oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( Oo00o0OO0O00o ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   i1iIIIi1i = I11iIiI1I1i11
   iIiIIi1 = iIiIIi1
   O0Oooo ( oOO00Oo , i1iIIIi1i , iIiIIi1 )
   if 17 - 17: OoOO0ooOOoo0O / OoOO0ooOOoo0O / o0000oOoOoO0o
   if 1 - 1: i1IIi . i11iIiiIii % OoOO0ooOOoo0O
def OooO0oo ( ) :
 OooIiIIII1i11I = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9zZXJpLWZpbG1sZXI=' ) )
 iiIi1IIiIi = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for oOO00Oo , I11iIiI1I1i11 , iIiIIi1 in iiIi1IIiIi :
  if 'IMDB' in oOO00Oo :
   pass
  else :
   oo0oooooO0 ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '  ' , '' ) + '[/COLOR]' , iIiIIi1 , 10037 , I11iIiI1I1i11 , iI111I11I1I1 , '' )
 iiIi1i = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1i :
  oo0oooooO0 ( '[COLORgold] Page ' + oOO00Oo + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + iIiIIi1 , 10039 , '' , iI111I11I1I1 , '' )
  if 89 - 89: o00O0oo
def ooOoOO0OoO00o ( url ) :
 OooIiIIII1i11I = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for oOO00Oo , I11iIiI1I1i11 , url in iiIi1IIiIi :
  if 'IMDB' in oOO00Oo :
   pass
  else :
   oo0oooooO0 ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '  ' , '' ) + '[/COLOR]' , url , 10037 , I11iIiI1I1i11 , iI111I11I1I1 , '' )
 iiIi1i = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for url , oOO00Oo in iiIi1i :
  oo0oooooO0 ( '[COLORgold] Page ' + oOO00Oo + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + url , 10034 , '' , iI111I11I1I1 , '' )
  if 11 - 11: Oo - OOOo0 * OoOoOO00 . ii11ii1ii . OoOO
  if 61 - 61: oO0o0ooO0 % OOOo0 - OOooOOo - OoOoOO00 % O0
def OoOOO00 ( url ) :
 OooIiIIII1i11I = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , I11iIiI1I1i11 , Oo00o0OO0O00o , oOO00Oo in iiIi1IIiIi :
  oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '&amp;' , '&' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( Oo00o0OO0O00o ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  i1iIIIi1i = I11iIiI1I1i11
  url = url
  O0Oooo ( oOO00Oo , i1iIIIi1i , url )
  if 94 - 94: IIII
def O0Oooo ( name , iconimage , url ) :
 OooIiIIII1i11I = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<meta itemprop="embedURL" content="(.+?)" />' ) . findall ( OooIiIIII1i11I )
 for url in iiIi1IIiIi :
  o000ooooo0 ( name , iconimage , url )
  if 51 - 51: Ooo00oOo00o - O0 % OoOO - OoOoOO00
def o000ooooo0 ( name , iconimage , url ) :
 name = name
 I11iIiI1I1i11 = iconimage
 OooIiIIII1i11I = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I1i11111i1i11 , I1II in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + name + ' - ' + I1II + '[/COLOR]' , I1i11111i1i11 , 10012 , I11iIiI1I1i11 )
  if 64 - 64: O0 % o0000oOoOoO0o % O0 * Ooo00oOo00o . OoOO + OOOo0
def O00 ( ) :
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 iIiIIi1 = 'http://www.izlemeyedeger.com/arama?q=' + iI
 OooIiIIII1i11I = cloudflare . source ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , I11iIiI1I1i11 , Oo00o0OO0O00o , oOO00Oo in iiIi1IIiIi :
  oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( Oo00o0OO0O00o ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  i1iIIIi1i = I11iIiI1I1i11
  iIiIIi1 = iIiIIi1
  O0Oooo ( oOO00Oo , i1iIIIi1i , iIiIIi1 )
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 17 - 17: o00O0oo - OoooooooOO % o00O0oo . IIII / i11iIiiIii % oO0o0ooO0
  if 28 - 28: o0000oOoOoO0o
  if 58 - 58: I1IiI
def iIiiI1iI ( ) :
 if 5 - 5: I1IiI / OoooooooOO + IIII * O0oO - Ooo00oOo00o % OOOo0
 oo0oooooO0 ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 if 42 - 42: O0 / OOooOOo + OoooooooOO * o0oO0 % o0oO0
def i1iIi ( ) :
 OooIiIIII1i11I = OOoOoo ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
  if 21 - 21: OoOO / ii11ii1ii + o00O0oo + OoooooooOO
def OoOo ( ) :
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 OooIiIIII1i11I = OOoOoo ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii1i1iI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I11iIiI1I1i11 , I1iI11iIiIi1 , iIiiiI1IiI1I1 in Ii1i1iI :
  for iI in I1iI11iIiIi1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   o0O0O0ooo0oOO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for iIiIIi1 , oOO00Oo in o0O0O0ooo0oOO :
    if 'tube' in iIiIIi1 :
     pass
    elif 'stage' in iIiIIi1 :
     i1II1 ( '[COLORgreen]' + I1iI11iIiIi1 + '   -   ' + oOO00Oo + '[/COLOR]' , ( iIiIIi1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iIiI1I1i11 , )
    elif 'vee' in iIiIIi1 :
     pass
     if 97 - 97: OOOo0 / oO0o0ooO0
def Oooo0 ( ) :
 OooIiIIII1i11I = OOoOoo ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii1i1iI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I11iIiI1I1i11 , I1iI11iIiIi1 , iIiiiI1IiI1I1 in Ii1i1iI :
  o0O0O0ooo0oOO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for iIiIIi1 , oOO00Oo in o0O0O0ooo0oOO :
   if 'tube' in iIiIIi1 :
    pass
   elif 'stage' in iIiIIi1 :
    i1II1 ( '[COLORgreen]' + I1iI11iIiIi1 + '   -   ' + oOO00Oo + '[/COLOR]' , ( iIiIIi1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iIiI1I1i11 )
   elif 'vee' in iIiIIi1 :
    pass
    if 59 - 59: OoooooooOO
    if 47 - 47: o0oO0 - OOOo0 / OoOoOO00
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: OoOO0ooOOoo0O
def O0iII1 ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIII1i = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( OooIiIIII1i11I )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIII1i ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIII1i :
  o00o0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 2 - 2: iIii1I11I1II1 * Oo % OoOO - OoOoOO00 - oO0o0ooO0
  if 3 - 3: O0oO
  if 45 - 45: O0oO
  if 83 - 83: I1IiI . OoooooooOO
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IIII / i11iIiiIii
  if 62 - 62: Ooo00oOo00o / ii11ii1ii
  if 7 - 7: OoooooooOO . IIII
def O000OOO0OOo ( ) :
 if 32 - 32: o00O0oo * O0
 O00oOo00o0o ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , iI111I11I1I1 , '' )
 O00oOo00o0o ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iI111I11I1I1 , '' )
 if 85 - 85: oO0o0ooO0 + OoooooooOO * oO0o0ooO0 - O0oO % i11iIiiIii
 xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
 if 71 - 71: ii11ii1ii - o0oO0 / I1IiI * I1IiI / i1IIi . i1IIi
def ooo000ooO0000 ( ) :
 O00oOo00o0o ( 'Search Pandoras Films' , '' , 10027 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 O00oOo00o0o ( 'Search Pandoras TV' , '' , 10028 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 if 97 - 97: Oo * OOOo0 . iIii1I11I1II1
def I1Ii1111iIi ( ) :
 if 31 - 31: o0000oOoOoO0o . O0oO * o0oO0 + i11iIiiIii * OoOO
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 OO0ooo0o0O0Oooooo = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 1 - 1: o0oO0 % I1IiI * Oo
 for o0O0oo0 in OO0ooo0o0O0Oooooo :
  iiiI1I1iIIIi1 = Base_Pand + o0O0oo0 + CAT
  OooIiIIII1i11I = OOoOoo ( iiiI1I1iIIIi1 )
  iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OooIiIIII1i11I )
  for iIiIIi1 , i1iIIIi1i , Iii , iI1iIIiiii , oOO00Oo in iiIi1IIiIi :
   if iI in oOO00Oo . lower ( ) :
    I1iiiiI1iI ( oOO00Oo , iIiIIi1 , 222 , i1iIIIi1i , iI1iIIiiii , Iii )
    if 43 - 43: OoOO - OoooooooOO
    xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
    xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 3 - 3: O0 / oO0o0ooO0
    if 31 - 31: OoOO0ooOOoo0O + OOooOOo . OoooooooOO
def ooOooo0 ( ) :
 if 67 - 67: OOOo0
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 OO0ooo0o0O0Oooooo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 55 - 55: ii11ii1ii - oO0o0ooO0 * OOooOOo + I1IiI * I1IiI * O0
 for o0O0oo0 in OO0ooo0o0O0Oooooo :
  O000Oo0o = Base_Pand + o0O0oo0 + CAT
  OooIiIIII1i11I = OOoOoo ( O000Oo0o )
  iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
  for oOO00Oo , Iii , iIiIIi1 , I11iIiI1I1i11 , iI1iIIiiii , OoO0O0O0o00 in iiIi1IIiIi :
   if iI in oOO00Oo . lower ( ) :
    O00oOo00o0o ( oOO00Oo , iIiIIi1 , OoO0O0O0o00 , I11iIiI1I1i11 , iI1iIIiiii , Iii )
    if 7 - 7: OOOo0 + I1IiI / IIII
    xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
    xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 79 - 79: Ooo00oOo00o - iIii1I11I1II1 + o00O0oo - O0oO
    if 93 - 93: OoOoOO00 . OOOo0 - Oo + I1IiI
def ooO0o ( ) :
 if 89 - 89: o0000oOoOoO0o / O0oO
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , Iii , iIiIIi1 , I11iIiI1I1i11 , iI1iIIiiii , OoO0O0O0o00 in iiIi1IIiIi :
  O00oOo00o0o ( oOO00Oo , iIiIIi1 , OoO0O0O0o00 , I11iIiI1I1i11 , iI1iIIiiii , Iii )
  if 90 - 90: oO0o0ooO0
def i1i1i1I ( url ) :
 if 83 - 83: OoOO + OoooooooOO
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I111IiiIi1 = ( '%s%s' % ( o00o , url ) )
 OOooOO000 = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooOO000 )
 for url , i1iIIIi1i , Iii , Ii1IIiiIIi , oOO00Oo in iiIi1IIiIi :
  I1iiiiI1iI ( oOO00Oo , url , 222 , i1iIIIi1i , Ii1IIiiIIi , Iii )
  if 88 - 88: OoooooooOO + o0000oOoOoO0o * OoOoOO00 % Oo
  ooo ( 'tvshows' , 'Media Info 3' )
  if 17 - 17: IIII * OoOO0ooOOoo0O - Ooo00oOo00o / i11iIiiIii
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 79 - 79: O0oO . OoOO - OoOoOO00 . OOOo0 % o0oO0
  if 65 - 65: OOOo0 + I1IiI / OoOO0ooOOoo0O
def oOO ( url ) :
 if 85 - 85: OoOO - iIii1I11I1II1 / O0
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , Iii , url , I11iIiI1I1i11 , iI1iIIiiii , OoO0O0O0o00 in iiIi1IIiIi :
  O00oOo00o0o ( oOO00Oo , url , OoO0O0O0o00 , I11iIiI1I1i11 , iI1iIIiiii , Iii )
  if 99 - 99: OoOoOO00 * IIII % iIii1I11I1II1 / o00O0oo
 ooo ( 'tvshows' , 'Media Info 3' )
 if 90 - 90: OoOO % OoOO0ooOOoo0O - OoOO0ooOOoo0O % OoOoOO00 * Ooo00oOo00o
 if 39 - 39: o0000oOoOoO0o
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: i1IIi % OOooOOo
def I1iiiiI1iI ( name , url , mode , iconimage , fanart , description ) :
 if 79 - 79: OOooOOo % oO0o0ooO0 * OoooooooOO * iIii1I11I1II1 . oO0o0ooO0 / o00O0oo
 IiI1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1I1I = True
 oO0Ooo0ooOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0Ooo0ooOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO0Ooo0ooOO0 . setProperty ( "Fanart_Image" , fanart )
 i1I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI1i1 , listitem = oO0Ooo0ooOO0 , isFolder = False )
 return i1I1I
 if 46 - 46: o00O0oo % I1IiI
def O00oOo00o0o ( name , url , mode , iconimage , fanart , description ) :
 if 64 - 64: i11iIiiIii - OoOoOO00
 IiI1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1I1I = True
 oO0Ooo0ooOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0Ooo0ooOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO0Ooo0ooOO0 . setProperty ( "Fanart_Image" , fanart )
 i1I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI1i1 , listitem = oO0Ooo0ooOO0 , isFolder = True )
 return i1I1I
if 77 - 77: I1IiI % o00O0oo
if 9 - 9: Ooo00oOo00o - Oo * OoooooooOO . Oo
if 2 - 2: OoooooooOO % OoOO0ooOOoo0O
if 63 - 63: OOOo0 % iIii1I11I1II1
if 39 - 39: oO0o0ooO0 / OoOoOO00 / ii11ii1ii % OOOo0
if 89 - 89: O0oO + OoooooooOO + O0oO * i1IIi + iIii1I11I1II1 % o0000oOoOoO0o
if 59 - 59: OoOO0ooOOoo0O + i11iIiiIii
if 88 - 88: i11iIiiIii - o0oO0
if 67 - 67: OoOO0ooOOoo0O . Oo + I1IiI - OoooooooOO
if 70 - 70: OoOO0ooOOoo0O / OoOoOO00 - iIii1I11I1II1 - oO0o0ooO0
if 11 - 11: iIii1I11I1II1 . OoooooooOO . OoOoOO00 / i1IIi - o0000oOoOoO0o
if 30 - 30: I1IiI
if 21 - 21: i11iIiiIii / O0oO % OoOO0ooOOoo0O * O0 . o0000oOoOoO0o - iIii1I11I1II1
if 26 - 26: OoOoOO00 * I1IiI
if 10 - 10: OoOoOO00 . oO0o0ooO0
def I1i ( string ) :
 if iIi1ii1I1 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 86 - 86: Oo / OoOO + O0 * oO0o0ooO0
def iiI11I1i1i1iI ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoOOo000o0 = [ ]
 try :
  if 12 - 12: OoOoOO00 . o0000oOoOoO0o / OoOO0ooOOoo0O
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( O00o0OO ) == False :
  I1i ( 'Making Favorites File' )
  OoOOo000o0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iiIiIIIiiI = open ( O00o0OO , "w" )
  iiIiIIIiiI . write ( json . dumps ( OoOOo000o0 ) )
  iiIiIIIiiI . close ( )
 else :
  I1i ( 'Appending Favorites' )
  iiIiIIIiiI = open ( O00o0OO ) . read ( )
  O00OO0oO = json . loads ( iiIiIIIiiI )
  O00OO0oO . append ( ( name , url , iconimage , fanart , mode ) )
  iiI1IIIi = open ( O00o0OO , "w" )
  iiI1IIIi . write ( json . dumps ( O00OO0oO ) )
  iiI1IIIi . close ( )
  if 25 - 25: Oo % ii11ii1ii * o0oO0
  if 6 - 6: oO0o0ooO0 . IIII * I1IiI . i1IIi
def oOOo ( ) :
 I1IiIIi = json . loads ( open ( O00o0OO ) . read ( ) )
 IiOOo00 = len ( I1IiIIi )
 for iIII in I1IiIIi :
  oOO00Oo = iIII [ 0 ]
  iIiIIi1 = iIII [ 1 ]
  i1iIIIi1i = iIII [ 2 ]
  try :
   Ii1iI11iI1 = iIII [ 3 ]
   if Ii1iI11iI1 == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    Ii1iI11iI1 = i1iIIIi1i
   else :
    Ii1iI11iI1 = iI1iIIiiii
  try : i11I1II = iIII [ 5 ]
  except : i11I1II = None
  try : OO0 = iIII [ 6 ]
  except : OO0 = None
  if 84 - 84: I1IiI % o0oO0 - I1IiI . OOooOOo
  if iIII [ 4 ] == 0 :
   oo0oooooO0 ( oOO00Oo , iIiIIi1 , '' , i1iIIIi1i , iI1iIIiiii , '' , 'fav' )
  else :
   oo0oooooO0 ( oOO00Oo , iIiIIi1 , iIII [ 4 ] , i1iIIIi1i , iI1iIIiiii , '' , 'fav' )
   if 5 - 5: I1IiI * O0oO - ii11ii1ii / iIii1I11I1II1 % OoOO + IIII
def o00o00OoO00o0 ( name ) :
 O00OO0oO = json . loads ( open ( O00o0OO ) . read ( ) )
 for OOoOoO00O0O0o in range ( len ( O00OO0oO ) ) :
  if O00OO0oO [ OOoOoO00O0O0o ] [ 0 ] == name :
   del O00OO0oO [ OOoOoO00O0O0o ]
   iiI1IIIi = open ( O00o0OO , "w" )
   iiI1IIIi . write ( json . dumps ( O00OO0oO ) )
   iiI1IIIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 12 - 12: ii11ii1ii + Ooo00oOo00o % o0000oOoOoO0o
 if 85 - 85: oO0o0ooO0 * OOooOOo
 if 3 - 3: OoOO0ooOOoo0O
def IiiO0o0o ( ) :
 if 87 - 87: o0000oOoOoO0o * i1IIi - o00O0oo % OoOO0ooOOoo0O / O0oO
 oo0oooooO0 ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 if 39 - 39: OOOo0 * i11iIiiIii - OoOO / IIII % O0oO % o0000oOoOoO0o
def OO00oo0o ( ) :
 if 18 - 18: Ooo00oOo00o + iIii1I11I1II1 - OoOoOO00 - OOOo0
 OOooooO0Oo = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIi1IIiIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , oooOOOO0oooo in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo + '  -  ' + ( oooOOOO0oooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIiIIi1 , 10023 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 51 - 51: O0 - i1IIi / OOOo0
  if 37 - 37: OOooOOo % o0oO0
  if 83 - 83: OoOO0ooOOoo0O . O0oO + OoOO - OoOO0ooOOoo0O * O0oO / O0oO
def I11I1 ( ) :
 if 45 - 45: IIII
 oo0oooooO0 ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 if 20 - 20: OoooooooOO * OOooOOo * O0 . OoOO0ooOOoo0O
def OoO000O ( url ) :
 OOoiIIiiIIIi1I = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 OooIiIIII1i11I = cloudflare . source ( OOoiIIiiIIIi1I )
 iiIi1IIiIi = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 10022 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 65 - 65: ii11ii1ii % O0 % iIii1I11I1II1 * o00O0oo
  if 31 - 31: o00O0oo
  if 44 - 44: I1IiI - iIii1I11I1II1 - Oo
  if 80 - 80: iIii1I11I1II1 * O0oO % o0000oOoOoO0o % Oo
def OooOO0o0 ( ) :
 if 91 - 91: OoOO + OoooooooOO - i1IIi
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iI ) . replace ( ' ' , '+' )
 OooIiIIII1i11I = cloudflare . source ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if iI in oOO00Oo . lower ( ) :
   oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10022 , iIii1 + 'dtv.png' )
   if 84 - 84: o00O0oo / IIII
   if 86 - 86: I1IiI * OoOoOO00 - O0 . I1IiI % iIii1I11I1II1 / OoOO0ooOOoo0O
   if 11 - 11: OOOo0 * OoOO + ii11ii1ii / ii11ii1ii
def iiii1I1 ( url ) :
 OooIiIIII1i11I = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I1i11111i1i11 , IIIiIiI11iIi , oooOO0OO0O , oOO00Oo in iiIi1IIiIi :
  o00oIII11I = ( oooOO0OO0O ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Ii1I11I = ( IIIiIiI11iIi ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iiIii1I = 'Season ' + Ii1I11I + 'Episode ' + o00oIII11I + oOO00Oo
  i1I11iIiII ( iiIii1I , I1i11111i1i11 )
  if 66 - 66: Oo - OOooOOo * IIII + I1IiI + OOooOOo - iIii1I11I1II1
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 17 - 17: OoOO
  if 22 - 22: o0000oOoOoO0o + iIii1I11I1II1
def i1I11iIiII ( name , url ) :
 I1i11111i1i11 = url
 IIIii1iiIi = name
 oooo0OOo = cloudflare . source ( I1i11111i1i11 )
 iiii111II = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( oooo0OOo )
 for IIII1i , I1II in iiii111II :
  i1II1 ( '[COLORgreen]' + IIIii1iiIi + I1II + '[/COLOR]' , IIII1i , 10012 , iIii1 + 'dtv.png' )
  if 72 - 72: O0 / o0oO0 + OoooooooOO * oO0o0ooO0
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: OoooooooOO % OoOoOO00 - OOOo0 % ii11ii1ii + i1IIi
 if 39 - 39: i1IIi
def OooOOo0 ( ) :
 if 51 - 51: I1IiI
 if 14 - 14: IIII % OoOO % Oo - i11iIiiIii
 if 53 - 53: o00O0oo % Oo
 if 59 - 59: OoOO0ooOOoo0O % iIii1I11I1II1 . i1IIi + OoOoOO00 * IIII
 if 41 - 41: o00O0oo % ii11ii1ii
 if 12 - 12: OoOO0ooOOoo0O
 if 69 - 69: OoooooooOO + OoOO0ooOOoo0O
 if 26 - 26: Oo + OoOO0ooOOoo0O / Ooo00oOo00o % I1IiI % ii11ii1ii + OoOoOO00
 if 31 - 31: o0000oOoOoO0o % OoOO0ooOOoo0O * o0000oOoOoO0o
 if 45 - 45: i1IIi . OOOo0 + OoOO0ooOOoo0O - OoooooooOO % o0oO0
 if 1 - 1: iIii1I11I1II1
 if 93 - 93: i1IIi . i11iIiiIii . Oo
 if 99 - 99: o0000oOoOoO0o - O0oO - OoOO % Ooo00oOo00o
 if 21 - 21: OoOoOO00 % ii11ii1ii . i1IIi - OoooooooOO
 oo0oooooO0 ( '[COLORgreen]Series[/COLOR]' , 'http://www.watchseries.li/series' , 10041 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 oo0oooooO0 ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 oo0oooooO0 ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 oo0oooooO0 ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 if 4 - 4: OoooooooOO . o0oO0
 if 78 - 78: ii11ii1ii + o0000oOoOoO0o - O0
def i1I1iIi1IiI ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 IIiI1 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 iiIi1IIiIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( IIiI1 ) )
 for url , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 11 - 11: OoOoOO00
def O00O00O000OOO ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for url , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 3 - 3: O0
def Ooo0Oo0oo0 ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in iiii111II :
  oo0oooooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 83 - 83: O0oO
  if 48 - 48: OoOoOO00 * OoOO0ooOOoo0O * O0oO
def i1iiiIii11 ( ) :
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOoOOO000O0 = 'http://www.watchseries.li/search/' + iI . replace ( ' ' , '%20' )
 OooIiIIII1i11I = OOoOoo ( OOoOOO000O0 )
 iiIi1IIiIi = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I11iIiI1I1i11 , iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'watch online' in oOO00Oo :
   pass
  else :
   oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.watchseries.li' + iIiIIi1 , 10044 , I11iIiI1I1i11 , '' , '' )
   if 92 - 92: ii11ii1ii / O0
   xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
   if 80 - 80: OOooOOo - OoOO0ooOOoo0O + OoooooooOO
def O0ooOoO ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I11iIiI1I1i11 , url , oOO00Oo , oooOO0OO0O , Iii in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oooOO0OO0O ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , I11iIiI1I1i11 , '' , Iii )
  if 26 - 26: I1IiI / Oo - i1IIi + o0000oOoOoO0o
def IiiIi ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in iiii111II :
  oo0oooooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 10 - 10: Ooo00oOo00o / Oo
def I1iII11iIII1i1I ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + ( oOO00Oo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , I11iIiI1I1i11 , '' , '' )
 for url in iiii111II :
  oo0oooooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 63 - 63: Oo + O0oO - OoOoOO00
  if 2 - 2: IIII
def oOo0O0O0 ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 IIiI1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for IIIiIiI11iIi , Ii1i1iI in IIiI1 :
  iiIi1IIiIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( Ii1i1iI ) )
  for url , oOO00Oo in iiIi1IIiIi :
   oo0oooooO0 ( '[COLORgreen]' + IIIiIiI11iIi + ' ' + ( oOO00Oo ) . replace ( '' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 iiii111II = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url in iiii111II :
  oo0oooooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 89 - 89: OoOO / OoooooooOO . oO0o0ooO0
  if 34 - 34: oO0o0ooO0 - OoooooooOO . OOOo0 / OoOoOO00
def II1II ( url ) :
 oo0O = [ OoiIiI1iiiI1ii ( url ) for I1iOO0Oo in xrange ( 1 ) ]
 IiIIIIIIiI = [ ]
 if 54 - 54: Oo + OOOo0 / oO0o0ooO0 . OOOo0 * I1IiI
 for iIII in xrange ( len ( oo0O ) ) :
  IIiIiiiIIIIi1 = oo0O [ iIII ]
  IiIIIIIIiI . append ( Thread ( target = OoiIiI1iiiI1ii ( url ) , args = ( IIiIiiiIIIIi1 , ) , kwargs = { } ) )
  IiIIIIIIiI [ iIII ] . start ( )
  if 39 - 39: Ooo00oOo00o / o00O0oo / O0oO
 for O00O0 in IiIIIIIIiI : O00O0 . join ( )
 if 19 - 19: OoOO - OoOoOO00
 if 63 - 63: i11iIiiIii . OOooOOo
def OoiIiI1iiiI1ii ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , oOO00Oo in iiIi1IIiIi :
  i1111 . create ( '' , '' , '' )
  OOoiIIiiIIIi1I = OOoiIIiiIIIi1I = 'http://www.watchseries.li/link/' + url
  if 'allmyvideos' in oOO00Oo :
   i11ii ( OOoiIIiiIIIi1I )
   i1111 . update ( 15 , "Please Wait" , "Getting Allmyvideos Streams" )
  elif 'vidspot' in oOO00Oo :
   i11ii ( OOoiIIiiIIIi1I )
   i1111 . update ( 30 , "Please Wait" , "Getting Vidspot Streams" )
  elif 'thevideo' in oOO00Oo :
   i11ii ( OOoiIIiiIIIi1I )
   i1111 . update ( 45 , "Please Wait" , "Getting Thevideo Streams" )
  elif 'daclips' in oOO00Oo :
   i11ii ( OOoiIIiiIIIi1I )
   i1111 . update ( 60 , "Please Wait" , "Getting Daclips Streams" )
  elif 'vodlocker' in oOO00Oo :
   i11ii ( OOoiIIiiIIIi1I )
   i1111 . update ( 80 , "Please Wait" , "Getting Vodlocker Streams" )
  elif 'filehoot' in oOO00Oo :
   i11ii ( OOoiIIiiIIIi1I )
   i1111 . update ( 100 , "Please Wait" , "Getting Filehoot Streams" )
  else :
   pass
   if 50 - 50: o00O0oo / I1IiI * o00O0oo
   if 34 - 34: O0 * O0 % OoooooooOO + oO0o0ooO0 * iIii1I11I1II1 % o00O0oo
   if 25 - 25: o0000oOoOoO0o + I1IiI . OOooOOo % I1IiI * OoOO0ooOOoo0O
def i11ii ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 o0OO0 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( OooIiIIII1i11I )
 iiii111II = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( OooIiIIII1i11I )
 iiIi1IIiIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( OooIiIIII1i11I )
 for url in o0OO0 :
  ii1IiIi11 ( url )
 for url in iiii111II :
  ii1IiIi11 ( url )
 for url in iiIi1IIiIi :
  ii1IiIi11 ( url )
  if 22 - 22: OoOO
def ii1IiIi11 ( url ) :
 if 'daclips.in' in url :
  OooIiIIII1i11I = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( OooIiIIII1i11I )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]DACLIPS[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'filehoot.com' in url :
  OooIiIIII1i11I = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OooIiIIII1i11I )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]FILEHOOT[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'thevideo.me' in url :
  OooIiIIII1i11I = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( OooIiIIII1i11I )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]THEVIDEO[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'allmyvideos.net' in url :
  OooIiIIII1i11I = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OooIiIIII1i11I )
  for url , oOO00Oo in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]ALLMYVIDEOS - ' + oOO00Oo + '[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'vidspot.net' in url :
  OooIiIIII1i11I = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( OooIiIIII1i11I )
  for url , oOO00Oo in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]VIDSPOT - ' + oOO00Oo + '[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'vodlocker' in url :
  OooIiIIII1i11I = OOoOoo ( url )
  iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OooIiIIII1i11I )
  for url in iiIi1IIiIi :
   i1II1 ( '[COLORgreen]VODLOCKER[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
if 33 - 33: iIii1I11I1II1 / o00O0oo
if 1 - 1: o00O0oo
if 48 - 48: O0 + O0 . O0oO - o0oO0
if 63 - 63: OoOO
if 71 - 71: i1IIi . o00O0oo * oO0o0ooO0 % OoooooooOO + OoOO0ooOOoo0O
if 36 - 36: IIII
if 49 - 49: OoOO0ooOOoo0O / OoooooooOO / OOOo0
if 74 - 74: O0oO % ii11ii1ii
if 7 - 7: OoOoOO00
if 27 - 27: OoOO . OoooooooOO + i11iIiiIii
if 86 - 86: o0000oOoOoO0o / OOooOOo - OOooOOo + ii11ii1ii + OoOO
if 33 - 33: OOooOOo . oO0o0ooO0 . IIII . i1IIi
if 49 - 49: ii11ii1ii
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
if 70 - 70: ii11ii1ii
if 67 - 67: OoooooooOO
if 29 - 29: O0 - i11iIiiIii - OoOoOO00 + OoOO0ooOOoo0O * IIII
if 2 - 2: i1IIi - o0oO0 + OOOo0 . OOooOOo * OOooOOo / I1IiI
def oOOO ( ) :
 oo0oooooO0 ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 if 16 - 16: OoOO + o0oO0 / OOooOOo
def O00oOoo0OoO0 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iiIi1IIiIi = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( '[COLORgreen]' + ( oOO00Oo ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIiIIi1 , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I11iIiI1I1i11 , iI111I11I1I1 , '' )
  if 62 - 62: i1IIi / o0oO0 . OOOo0 * OOooOOo
def i11i1Ii1 ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 IIiI1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for IIiI1 in IIiI1 :
  o0oO0oo0000OO = re . compile ( '(.*?)</h2>' ) . findall ( str ( IIiI1 ) )
  for I1i1ii1IiIii in o0oO0oo0000OO :
   I1i1ii1IiIii = I1i1ii1IiIii
  oOOO0O0Ooo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( IIiI1 ) )
  for IiI1i111IiIiIi1 , I11iIiI1I1i11 , time , i1II11II1 in oOOO0O0Ooo :
   II1IIIii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( i1II11II1 )
   oo0oooooO0 ( '[COLORgreen]' + I1i1ii1IiIii + ' - ' + IiI1i111IiIiIi1 + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I11iIiI1I1i11 , iI111I11I1I1 , ( str ( II1IIIii ) ) )
   if 40 - 40: I1IiI % Ooo00oOo00o
 ooo ( 'tvshows' , 'Media Info 3' )
 if 62 - 62: OOooOOo
def I1i111i ( ) :
 if 42 - 42: ii11ii1ii / i1IIi % I1IiI
 oo0oooooO0 ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iIii1 + 'fanart.jpg' , '' )
 oo0oooooO0 ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iIii1 + 'fanart.jpg' , '' )
 if 26 - 26: o00O0oo * iIii1I11I1II1 % Ooo00oOo00o . OOooOOo + Oo
def OOO00OOo0o0Oo ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  ooooOoO0O = oOO00Oo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  i1II1 ( '[COLORgreen]' + ooooOoO0O + '[/COLOR]' , url , 10013 , I11iIiI1I1i11 )
  if 1 - 1: ii11ii1ii / Ooo00oOo00o + OoOO . OOooOOo / ii11ii1ii - oO0o0ooO0
def ii111i1iI ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( OooIiIIII1i11I )
 for IIII1i in iiIi1IIiIi :
  I1I1iII1i = ( IIII1i ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o00o0 ( 'http:' + I1I1iII1i )
  if 30 - 30: O0 + ii11ii1ii + OoOoOO00
  if 14 - 14: OOooOOo / OoOO0ooOOoo0O - iIii1I11I1II1 - OoOO % o0oO0
def I1iIiI1IiIIII ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 8046 , iIii1 + 'documentary.png' )
def I1iiIi111I ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( 'NEXT PAGE' , url , 8046 , iIii1 + 'documentary.png' )
  if 34 - 34: i11iIiiIii - OoOoOO00 / OOOo0 % OOooOOo
def iI1IiiiI11 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  yt . PlayVideo ( url )
  if 80 - 80: OoOO + OOooOOo * o00O0oo + Ooo00oOo00o
def O0oOo ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 8041 , iIii1 + 'documentary.png' )
def OO0oo0O0OOO0 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo ) . replace ( '&#039;s' , '' ) , url , 8042 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( 'NEXT PAGE' , url , 8041 , iIii1 + 'documentary.png' )
  if 76 - 76: i11iIiiIii / I1IiI + I1IiI / i1IIi * OOOo0
  if 12 - 12: O0oO % i11iIiiIii + OOooOOo + O0oO / o0000oOoOoO0o
def O00O0O ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , I11iIiI1I1i11 , url , O0OOo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , I11iIiI1I1i11 )
 for url in iiii111II :
  OOo0o ( ( url ) . replace ( '//' , 'http://' ) )
  if 20 - 20: Ooo00oOo00o / iIii1I11I1II1
def OOo0o ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIii1 + 'documentary.png' )
  if 15 - 15: OoOO . OOooOOo
def ii1ii ( ) :
 OooIiIIII1i11I = OO ( 'http://www.stream2watch.co/live-tv' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , IIiI1i in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo + '[COLORgreen]' + IIiI1i + '[/COLOR]' ) , iIiIIi1 , 8086 , I11iIiI1I1i11 )
  if 6 - 6: ii11ii1ii / oO0o0ooO0 - OoOO0ooOOoo0O
def o00O00Oo00O ( url ) :
 OooIiIIII1i11I = OO ( url )
 iiIi1IIiIi = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 8087 , I11iIiI1I1i11 )
  if 46 - 46: I1IiI % i1IIi / OoOO * Oo * OoOO0ooOOoo0O
def OOoOOOo0Ooo0 ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , oOO00Oo in iiIi1IIiIi :
  o0OOOOO0O ( url , oOO00Oo )
  if 35 - 35: o00O0oo - o00O0oo + i1IIi - O0 - O0oO
def o0OOOOO0O ( url , name ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url in iiIi1IIiIi :
  print url
  i1II1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 58 - 58: I1IiI - oO0o0ooO0 - OoooooooOO
def o00ii111Iiii ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 iiIi1IIiIi = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , time , oo0oO0o0 , IiI1i111IiIiIi1 , oOOO0O0Ooo , iIiIIi1 in iiIi1IIiIi :
  I1I11i ( ( time + '[COLORgreen]' + oOOO0O0Ooo + '[/COLOR]' + IiI1i111IiIiIi1 ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , iIiIIi1 , 8061 , I11iIiI1I1i11 )
def Iii1Ii ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , iIii1 + 'documentary.png' )
  if 30 - 30: O0 - oO0o0ooO0 % Oo
def O0Oo ( ) :
 OooIiIIII1i11I = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iIiIIi1 , 8071 , iIii1 + 'streams.png' )
def iIIiI11i ( url ) :
 OooIiIIII1i11I = OO ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , iIii1 + 'streams.png' )
def Oooo0oOOO0 ( url ) :
 OooIiIIII1i11I = OO ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for I11iIiI1I1i11 , oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( ) , 222 , I11iIiI1I1i11 )
  if 61 - 61: OOooOOo / I1IiI - Oo
def I1iIIII1 ( ) :
 OooIiIIII1i11I = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy54bnh4LmNvbS8=' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a><br>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) , iIiIIi1 , 8091 , iIii1 + 'streams.png' )
def OO0I11Ii1iI11iI1 ( url ) :
 OooIiIIII1i11I = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?src="(.+?)".+?title="(.+?)">' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) , url , 8092 , I11iIiI1I1i11 )
def i1III1 ( url ) :
 OooIiIIII1i11I = OO ( url )
 iiIi1IIiIi = re . compile ( 'src=&quot;(.+?)&quot;' ) . findall ( OooIiIIII1i11I )
 for url in iiIi1IIiIi :
  Iii111IiIii ( url )
  if 100 - 100: OoOoOO00 - OOooOOo . OoOoOO00 * OoOoOO00 . IIII
def iIiI ( url ) :
 oO00Ooo0oO = urllib2 . Request ( url )
 oO00Ooo0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOOo = ''
 OOooOO000 = ''
 try :
  OOOo = urllib2 . urlopen ( oO00Ooo0oO )
  OOooOO000 = OOOo . read ( )
  OOOo . close ( )
 except : pass
 if OOooOO000 != '' :
  return OOooOO000
 else :
  OOooOO000 = 'Failed'
  return OOooOO000
  if 74 - 74: o00O0oo - OoooooooOO . Oo
def III1Ii1i1I1 ( ) :
 O0O00OooO = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 I1i11111i1i11 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 I1IiI1iI11 = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iIi = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 iiO0O0o0oO0O00 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 o0O0oO0 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oo0 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iI
 i1i1IiIi1 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iI ) . replace ( ' ' , '+' )
 I1iiIiI1iI1I = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9hcmFtYT9xPQ==' ) ) + iI
 if 27 - 27: ii11ii1ii * O0oO - Ooo00oOo00o + o00O0oo * o00O0oo
 OooIiIIII1i11I = iIiI ( iIiIIi1 )
 oooo0OOo = iIiI ( I1i11111i1i11 )
 o0OO0O0OO0oO0 = iIiI ( I1IiI1iI11 )
 iIiiIi11IIi = iIiI ( iIi )
 Oo0 = iIiI ( iiO0O0o0oO0O00 )
 oOII1ii1ii11I1 = iIiI ( oo0 )
 o0ooOO0o = OOoOoo ( i1i1IiIi1 )
 ooo0 = OOoOoo ( I1iiIiI1iI1I )
 if 46 - 46: oO0o0ooO0 - iIii1I11I1II1
 if ooo0 != 'Failed' :
  I1I1 = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( ooo0 )
  for iIiIIi1 , I11iIiI1I1i11 , Oo00o0OO0O00o , oOO00Oo in I1I1 :
   oOO00Oo = ( oOO00Oo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( Oo00o0OO0O00o ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   i1iIIIi1i = I11iIiI1I1i11
   iIiIIi1 = iIiIIi1
   O0Oooo ( oOO00Oo , i1iIIIi1i , iIiIIi1 )
   xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if OooIiIIII1i11I != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OooIiIIII1i11I )
  for O0Oo0 , oOO00Oo in iiIi1IIiIi :
   if iI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIiIIi1 + O0Oo0 ) , 222 , '' )
 if oooo0OOo != 'Failed' :
  iiii111II = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oooo0OOo )
  for O0Oo0 , oOO00Oo in iiii111II :
   if iI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1i11111i1i11 + O0Oo0 ) , 222 , '' )
 if o0OO0O0OO0oO0 != 'Failed' :
  o0OO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0OO0O0OO0oO0 )
  for O0Oo0 , oOO00Oo in o0OO0 :
   if iI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1IiI1iI11 + O0Oo0 ) , 222 , '' )
 if iIiiIi11IIi != 'Failed' :
  OOooO0OO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIiiIi11IIi )
  for O0Oo0 , oOO00Oo in OOooO0OO0 :
   if iI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIi + O0Oo0 ) , 222 , '' )
 if Oo0 != 'Failed' :
  iI1iIiiiI1I1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oo0 )
  for O0Oo0 , I11iIiI1I1i11 , oOO00Oo in iI1iIiiiI1I1 :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , O0Oo0 , 1006 , 'img' )
    if 78 - 78: OoOO / Ooo00oOo00o - OoOO * OoooooooOO . I1IiI
    ooo ( 'tvshows' , 'Media Info 3' )
 if oOII1ii1ii11I1 != 'Failed' :
  OOoooOoO0Oo = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oOII1ii1ii11I1 )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in OOoooOoO0Oo :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iIiIIi1 , 7067 , I11iIiI1I1i11 )
    if 78 - 78: OoooooooOO / OoOO0ooOOoo0O % I1IiI * OoooooooOO
    ooo ( 'tvshows' , 'Media Info 3' )
 if o0ooOO0o != 'Failed' :
  ooOO00o00 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( o0ooOO0o )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in ooOO00o00 :
   i1II1 ( '[COLORgreen]' + oOO00Oo + '- Source 7[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
 OO0ooo0o0O0Oooooo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 18 - 18: iIii1I11I1II1 + o0000oOoOoO0o * OOOo0 - OoOO0ooOOoo0O / OOOo0
 if 78 - 78: o0000oOoOoO0o . IIII
 for o0O0oo0 in OO0ooo0o0O0Oooooo :
  iiiI1I1iIIIi1 = O0O00OooO + o0O0oo0
  iI1i1II = iIiI ( iiiI1I1iIIIi1 )
  if Oo0 != 'Failed' :
   I1ii1ii1I = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( iI1i1II )
   for O0Oo0 , oOO00Oo in I1ii1ii1I :
    if iI in oOO00Oo . lower ( ) :
     i1II1 ( ( '[COLORgreen]' + oOO00Oo + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0O00OooO + o0O0oo0 + O0Oo0 ) , 222 , '' )
     if 18 - 18: OoOO * OoOO % OoOO
     ooo ( 'tvshows' , 'Media Info 3' )
     if 17 - 17: O0 * I1IiI * ii11ii1ii * OoOoOO00 * o0000oOoOoO0o % i1IIi
     if 33 - 33: ii11ii1ii * ii11ii1ii . o0oO0 . i11iIiiIii
def IIIIiIi11iiIi ( ) :
 if 48 - 48: IIII % o0000oOoOoO0o
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 I1i11111i1i11 = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 I1IiI1iI11 = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iIi = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iiO0O0o0oO0O00 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iI ) . replace ( ' ' , '+' )
 o0O0oO0 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 i1i1IiIi1 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iI ) . replace ( ' ' , '+' )
 I1iiIiI1iI1I = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + iI . replace ( ' ' , '%20' )
 if 3 - 3: IIII % o00O0oo + Oo
 OooIiIIII1i11I = iIiI ( iIiIIi1 )
 oooo0OOo = iIiI ( I1i11111i1i11 )
 o0OO0O0OO0oO0 = iIiI ( I1IiI1iI11 )
 iIiiIi11IIi = iIiI ( iIi )
 Oo0 = cloudflare . source ( iiO0O0o0oO0O00 )
 iI1i1II = iIiI ( o0O0oO0 )
 o0ooOO0o = OOoOoo ( i1i1IiIi1 )
 ooo0 = OOoOoo ( I1iiIiI1iI1I )
 if OooIiIIII1i11I != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OooIiIIII1i11I )
  for oOO00Oo in iiIi1IIiIi :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIIi1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 47 - 47: O0 * OOOo0 * Ooo00oOo00o . OoOoOO00
    ooo ( 'tvshows' , 'Media Info 3' )
 if oooo0OOo != 'Failed' :
  iiii111II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooo0OOo )
  for oOO00Oo in iiii111II :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i11111i1i11 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 95 - 95: o00O0oo % IIII . O0 % O0oO
    ooo ( 'tvshows' , 'Media Info 3' )
 if o0OO0O0OO0oO0 != 'Failed' :
  o0OO0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0OO0O0OO0oO0 )
  for oOO00Oo in iiii111II :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1IiI1iI11 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 68 - 68: Oo . Oo - ii11ii1ii / o0000oOoOoO0o . o0oO0 / i1IIi
    ooo ( 'tvshows' , 'Media Info 3' )
 if iIiiIi11IIi != 'Failed' :
  OOooO0OO0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiiIi11IIi )
  for oOO00Oo in iiii111II :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( '[COLORgreen]' + oOO00Oo + ' source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIi + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 12 - 12: ii11ii1ii * i1IIi * o0000oOoOoO0o
    ooo ( 'tvshows' , 'Media Info 3' )
 if Oo0 != 'Failed' :
  iI1iIiiiI1I1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( Oo0 )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iI1iIiiiI1I1 :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( '[COLORgreen]' + oOO00Oo + ' - Source - Dizi[/COLOR]' , iIiIIi1 , 8062 , I11iIiI1I1i11 )
    if 23 - 23: OoOO0ooOOoo0O / O0 / OOOo0
    ooo ( 'tvshows' , 'Media Info 3' )
 if iI1i1II != 'Failed' :
  I1ii1ii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i1II )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in I1ii1ii1I :
   if iI in oOO00Oo . lower ( ) :
    i1II1 ( ( '[COLORgreen]' + oOO00Oo + '- Source Scooby[/COLOR]' ) , iIiIIi1 , 222 , 'img' )
    if 49 - 49: o0000oOoOoO0o . OOooOOo % OoOO / o00O0oo
    ooo ( 'tvshows' , 'Media Info 3' )
 if o0ooOO0o != 'Failed' :
  ooOO00o00 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( o0ooOO0o )
  for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in ooOO00o00 :
   i1II1 ( '[COLORgreen]' + oOO00Oo + ' - Source DiZzY[/COLOR]' , iIiIIi1 , 222 , I11iIiI1I1i11 )
 if ooo0 != 'Failed' :
  I1I1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( ooo0 )
  for I11iIiI1I1i11 , iIiIIi1 , oOO00Oo in I1I1 :
   if 'watch online' in oOO00Oo :
    pass
   else :
    oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + iIiIIi1 , 10044 , I11iIiI1I1i11 , '' , '' )
    if 95 - 95: O0 * I1IiI * IIII . o0oO0 / iIii1I11I1II1
    xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
    if 28 - 28: IIII + OoOO - o0oO0 / iIii1I11I1II1 - OOOo0
def Ii1i1 ( ) :
 if 65 - 65: OoOO + ii11ii1ii / OoOO0ooOOoo0O
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OooIiIIII1i11I = OOoOoo ( iIiIIi1 )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for oOO00Oo , I11iIiI1I1i11 , oo0oo in iiIi1IIiIi :
  IiIIi11i111 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  if iI in oOO00Oo . lower ( ) :
   I1I11i ( oOO00Oo , '' , 7022 , IiIIi11i111 )
   if 67 - 67: i1IIi
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: OoOoOO00 . OoooooooOO
 if 57 - 57: OOOo0
def iii1IIiI ( url ) :
 i1i1Ii11Ii = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( i1i1Ii11Ii )
 for url , IIIiIiI11iIi , oooOOOO0oooo , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( IIIiIiI11iIi ) . replace ( 'Sezon' , ' Season ' ) + ( oooOOOO0oooo ) . replace ( 'Bölüm' , ' Episode ' ) + oOO00Oo , url , 8063 , '' )
  if 57 - 57: OoOO0ooOOoo0O + O0oO % ii11ii1ii . Ooo00oOo00o / Ooo00oOo00o * O0
  if 6 - 6: i1IIi - OoOoOO00 * OOooOOo . Ooo00oOo00o
  if 68 - 68: OOooOOo
  if 20 - 20: O0oO - O0oO
def iIIiI11i1I11 ( url ) :
 i1i1Ii11Ii = cloudflare . source ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i1i1Ii11Ii )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , '' )
  if 29 - 29: Ooo00oOo00o * iIii1I11I1II1 * O0 - I1IiI / IIII
  if 99 - 99: o0oO0
  if 76 - 76: Ooo00oOo00o
  if 92 - 92: o0000oOoOoO0o - iIii1I11I1II1 % OoooooooOO
def I1oOooo00O ( ) :
 if 66 - 66: I1IiI + i1IIi % OoOoOO00 . O0 * ii11ii1ii % ii11ii1ii
 i1i1Ii11Ii = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIi1IIiIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1i1Ii11Ii )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo , oooOOOO0oooo in iiIi1IIiIi :
  I1I11i ( oOO00Oo + '  -  ' + ( oooOOOO0oooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIiIIi1 , 8063 , I11iIiI1I1i11 )
  if 87 - 87: OoOO0ooOOoo0O + OOooOOo . oO0o0ooO0 - OoooooooOO
def iiiiI1IiI1I1 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 8002 , I11iIiI1I1i11 )
def iI111i11iI1 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , time , url , oOO00Oo , O0OOo in iiIi1IIiIi :
  oo0oooooO0 ( '%s %s' % ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , time ) , url , 1015 , I11iIiI1I1i11 , O0OOo )
  if 2 - 2: I1IiI + O0oO + OoooooooOO . i1IIi
def I1III1iIi ( ) :
 if 82 - 82: OOOo0 + oO0o0ooO0 + ii11ii1ii * OOOo0 % i11iIiiIii % oO0o0ooO0
 I1I11i ( 'Coronation Street' , '' , 8001 , '' )
 I1I11i ( 'Eastenders' , '' , 8002 , '' )
 I1I11i ( 'Emmerdale' , '' , 8003 , '' )
 I1I11i ( 'Hollyoaks' , '' , 8004 , '' )
 I1I11i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 23 - 23: i1IIi . iIii1I11I1II1 . OoOO0ooOOoo0O . O0 % o00O0oo % i11iIiiIii
 if 11 - 11: O0 - OoOoOO00 . OoOO0ooOOoo0O . o00O0oo % O0oO
 if 21 - 21: Oo / oO0o0ooO0 . O0oO * OoooooooOO + o0000oOoOoO0o - i1IIi
 if 58 - 58: ii11ii1ii
def ii1I ( ) :
 OooIiIIII1i11I = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Holly' in oOO00Oo :
   I11iIiI1I1i11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 98 - 98: i1IIi
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 51 - 51: ii11ii1ii + o0oO0 + Oo / i1IIi + i1IIi
def IiiOooooOo0 ( ) :
 OooIiIIII1i11I = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'East' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 45 - 45: IIII / O0 / I1IiI * OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: iIii1I11I1II1 + OoOO0ooOOoo0O + iIii1I11I1II1 . ii11ii1ii + O0oO . o0oO0
def II1i11 ( ) :
 OooIiIIII1i11I = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Emmer' in oOO00Oo :
   I11iIiI1I1i11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 28 - 28: OoOoOO00 - OoOO % I1IiI + Ooo00oOo00o - I1IiI
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: OoOoOO00 . OoOO + O0 . O0 . OoOO0ooOOoo0O
def ooOoo000oO ( ) :
 OooIiIIII1i11I = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Coro' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 50 - 50: IIII + OOooOOo
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: Ooo00oOo00o
def oOOoO ( ) :
 OooIiIIII1i11I = OOoOoo ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Celeb' in oOO00Oo :
   I11iIiI1I1i11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iIiIIi1 :
    i1II1 ( ( oOO00Oo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIiIIi1 . replace ( '\\/' , '/' ) , 8006 , I11iIiI1I1i11 )
   else :
    pass
    if 87 - 87: I1IiI % iIii1I11I1II1
def o0O ( name , url ) :
 O0OOO0O = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if O0OOO0O :
  Iii1I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOooooO0Oo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OOooooO0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOooooO0Oo = open_url ( url )
  oOoOOOOoOO0o = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OOooooO0Oo ) [ - 1 ]
  Iii1I = oOoOOOOoOO0o . replace ( '\\/' , '/' )
 oO0Ooo0ooOO0 = xbmcgui . ListItem ( name , '' , '' )
 oO0Ooo0ooOO0 . setPath ( Iii1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oO0Ooo0ooOO0 )
 if 31 - 31: OOOo0 . IIII + ii11ii1ii
 if 91 - 91: ii11ii1ii % o0oO0
def i1i1II1I ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iiIi1IIiIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iIiIIi1 , 7071 , iIii1 + 'popcorn.png' )
 for iIiIIi1 , oOO00Oo in iiii111II :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iIiIIi1 , 7071 , iIii1 + 'popcorn.png' )
  if 62 - 62: I1IiI + o00O0oo * oO0o0ooO0
def o0ii1iIi1Ii1 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIi1IIiIi = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  if 'Movies' in oOO00Oo :
   I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( iIiIIi1 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iIii1 + 'popcorn.png' )
def oOOoOOO0oo0 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iIiI1I1i11 )
 for url in iiii111II :
  I1I11i ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iIii1 + 'popcorn.png' )
  if 87 - 87: o0oO0 / I1IiI % OOooOOo * OoOO
  if 77 - 77: OoOO - Oo - iIii1I11I1II1
def IIi1i ( url ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIi1IIiIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I11iIiI1I1i11 )
  if 21 - 21: OoOO % OoOO / Ooo00oOo00o
  if 12 - 12: oO0o0ooO0 / I1IiI
def ooooo0Oo0 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iIiI1I1i11 )
  if 97 - 97: IIII . OoOO . IIII
def oOo00o ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  II111i1ii1iII ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 75 - 75: iIii1I11I1II1 + OoooooooOO
def II111i1ii1iII ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 222 , iIii1 + 'popcorn' )
  if 97 - 97: ii11ii1ii / Oo + O0oO
  if 32 - 32: o0oO0 % O0oO * Oo
  if 72 - 72: o0oO0 . oO0o0ooO0 - O0oO - o00O0oo % i1IIi
  if 56 - 56: Oo * oO0o0ooO0
def II1I1ii1ii11 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo , I11iIiI1I1i11 in iiIi1IIiIi :
  i1II1 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( iIiIIi1 ) ) , 222 , I11iIiI1I1i11 )
  if 64 - 64: Ooo00oOo00o % IIII . O0oO % Ooo00oOo00o + o0000oOoOoO0o * IIII
def OOOO00OooO ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 iiIi1IIiIi = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + iIiIIi1 , 7051 , iIii1 + 'vod.png' )
  if 64 - 64: Ooo00oOo00o . OOOo0 - OoooooooOO . o0oO0 - oO0o0ooO0
def O0oO0o000o ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , iIii1 + 'vod.png' )
  if 42 - 42: O0oO * IIII
def III11i1iIIiiI ( url ) :
 OOooooO0Oo = OOoOoo
 iiIi1IIiIi = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 222 , I11iIiI1I1i11 )
  if 95 - 95: o0000oOoOoO0o
  if 44 - 44: OoOO0ooOOoo0O + o0000oOoOoO0o . IIII / OoOoOO00 % iIii1I11I1II1 + IIII
  if 61 - 61: OoOO0ooOOoo0O / Ooo00oOo00o + OoOoOO00 . OoOO / Oo * OoOO0ooOOoo0O
  if 46 - 46: iIii1I11I1II1
  if 33 - 33: o0000oOoOoO0o % o0000oOoOoO0o % O0 / OOOo0 . i1IIi
def O0O0ooOoOO0OO ( ) :
 if 27 - 27: IIII * OOOo0 . iIii1I11I1II1 - iIii1I11I1II1
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
 if 5 - 5: IIII
 if 84 - 84: OoOoOO00 * OoOO * OoOoOO00 % IIII / OOOo0
def O0OoooI11iI1I ( Cat_Name ) :
 if 50 - 50: iIii1I11I1II1 * IIII . OoooooooOO / OoOoOO00 - ii11ii1ii * ii11ii1ii
 OOo000o0 = False
 o00oo0OO0 = '0'
 if Cat_Name == 'All Channels' : OOo000o0 = True
 if Cat_Name == 'Entertainment' : o00oo0OO0 = '1'
 if Cat_Name == 'Movies' : o00oo0OO0 = '2'
 if Cat_Name == 'Music' : o00oo0OO0 = '3'
 if Cat_Name == 'News' : o00oo0OO0 = '4'
 if Cat_Name == 'Sports' : o00oo0OO0 = '5'
 if Cat_Name == 'Documentary' : o00oo0OO0 = '6'
 if Cat_Name == 'Kids' : o00oo0OO0 = '7'
 if Cat_Name == 'Food' : o00oo0OO0 = '8'
 if Cat_Name == 'Religious' : o00oo0OO0 = '9'
 if Cat_Name == 'USA Channels' : o00oo0OO0 = '10'
 if Cat_Name == 'Other' : o00oo0OO0 = '11'
 if 60 - 60: o0oO0
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 print 'Len Match: >>>' + str ( len ( iiIi1IIiIi ) )
 for oOO00Oo , I11iIiI1I1i11 , oo0oo in iiIi1IIiIi :
  IiIIi11i111 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  if oo0oo == o00oo0OO0 :
   I1I11i ( oOO00Oo , '' , 7022 , IiIIi11i111 )
  elif OOo000o0 == True :
   I1I11i ( oOO00Oo , '' , 7022 , IiIIi11i111 )
  else : pass
  if 66 - 66: o0000oOoOoO0o / o0oO0 % i1IIi - OoOO . O0 / O0
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 96 - 96: OoooooooOO + IIII * O0
def oo0OoOO0o0o ( Search_Name ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiIi1IIiIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , iIiIIi1 , I1i11111i1i11 , I1IiI1iI11 in iiIi1IIiIi :
  IiIIi11i111 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iIiI1I1i11 ) . replace ( '\\' , '' )
  i1II1 ( Search_Name + ': Link 1' , ( iIiIIi1 ) . replace ( '\\' , '' ) , 222 , IiIIi11i111 )
  i1II1 ( Search_Name + ': Link 2' , ( I1i11111i1i11 ) . replace ( '\\' , '' ) , 222 , IiIIi11i111 )
  i1II1 ( Search_Name + ': Link 3' , ( I1IiI1iI11 ) . replace ( '\\' , '' ) , 222 , IiIIi11i111 )
  if 67 - 67: I1IiI - I1IiI * Ooo00oOo00o - oO0o0ooO0 % OoOO
def iIiiIIIiI1Ii ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iIii1 + 'english.png' )
def IIiiiiiIiIIi ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'xxx.png' )
def iiIiiIi1 ( ) :
 OOooooO0Oo = OOoOoo ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iiIi1IIiIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , iIiIIi1 in iiIi1IIiIi :
  i1II1 ( oOO00Oo , ( iIiIIi1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'vod(1).png' )
  if 30 - 30: OoOO0ooOOoo0O + OoOoOO00 - IIII * OoooooooOO
def I1iIiiiI1 ( url ) :
 url
 OOO0O00Oo = xbmcgui . ListItem ( oOO00Oo , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOO0O00Oo )
 return
 if 13 - 13: iIii1I11I1II1
 if 2 - 2: i1IIi * OoOO - OoOO + OoooooooOO % I1IiI / I1IiI
def i11IiI1iiI11 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 iiii111II = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOooooO0Oo )
 for url , Iii , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , ( Iii ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  ooo ( 'tvshows' , 'Media Info 3' )
 for url in iiii111II :
  I1I11i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iIii1 + 'FITNESS.png' )
  if 85 - 85: ii11ii1ii - I1IiI / ii11ii1ii + OoOO0ooOOoo0O - oO0o0ooO0
def IIii1III ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , Iii , I11iIiI1I1i11 in iiIi1IIiIi :
  oo0oOo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , Iii )
  ooo ( 'tvshows' , 'Media Info 3' )
 Ii1i1iI = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for ooooOoo0OO in Ii1i1iI :
  Oo0O0000Oo00o = ( ooooOoo0OO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  oo0oooooO0 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I11iIiI1I1i11 , '' , Oo0O0000Oo00o )
  if 20 - 20: Ooo00oOo00o . OOOo0 * i11iIiiIii / i11iIiiIii
def o00iIiiiII ( INFO ) :
 Ii1I1 ( 'info for workout' , INFO )
 if 71 - 71: I1IiI + iIii1I11I1II1 * OoOO . O0oO % i11iIiiIii % iIii1I11I1II1
 if 63 - 63: OoooooooOO * Ooo00oOo00o / o0000oOoOoO0o - OoOO . iIii1I11I1II1 + oO0o0ooO0
 if 44 - 44: i1IIi % OOOo0 % OOooOOo
def iIIi1Ii1III ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 9031 , iIii1 + 'icon.png' )
def Oooo00 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 9032 , iIii1 + 'icon.png' )
def iii1II1iI1IIi ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  if '://' in oOO00Oo :
   pass
   i1II1 ( ( oOO00Oo ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , iIii1 + 'icon.png' )
def Ii11iiI1 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , iIii1 + 'icon.png' )
  if 71 - 71: OOooOOo / OoOO0ooOOoo0O % OoOO0ooOOoo0O
  if 89 - 89: OoooooooOO + i11iIiiIii / o0000oOoOoO0o + iIii1I11I1II1 % o0oO0
  if 29 - 29: ii11ii1ii
def Oo0o00ooOOOoOo ( ) :
 OOooooO0Oo = OOoOoo ( 'http://tvshows.cnfstudio.com/' )
 iiIi1IIiIi = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , 'http://tvshows.cnfstudio.com/genre/' + iIiIIi1 , 7010 , iIii1 + 'icon.png' )
  print '>>>>>>>>>>' + iIiIIi1
  if 30 - 30: o0oO0 + o0oO0 % IIII - OOooOOo - ii11ii1ii
def i111IiiI1Ii ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOooooO0Oo )
 OooOOOOOo = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( ( oOO00Oo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , I11iIiI1I1i11 )
 OooOOOOOo = OooOOOOOo
 for url in OooOOOOOo :
  I1I11i ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  I1I11i ( 'Next' , url , 7010 , '' )
  if 50 - 50: O0oO + o0oO0 + oO0o0ooO0
def ii11iiI11I ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oooOOOO0oooo , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( 'Season' ) + oooOOOO0oooo + ( '  ' ) + oOO00Oo , url , 7004 , iIii1 + 'icon.png' )
  if 96 - 96: iIii1I11I1II1 + i11iIiiIii - Oo . o0oO0
def iiIi11i1IiI ( url ) :
 if 88 - 88: ii11ii1ii - o00O0oo * I1IiI
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iIii1 + 'icon.png' )
  if 73 - 73: OOooOOo % Ooo00oOo00o + IIII + OOOo0
def OoOO00 ( name , url , img ) :
 OooIiIIII1i11I = OOoOoo ( url )
 O0O00OoOoOOo = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( OooIiIIII1i11I )
 o0o0oo0 = len ( O0O00OoOoOOo )
 if 25 - 25: Ooo00oOo00o * OoOO % i11iIiiIii + i11iIiiIii * Ooo00oOo00o
 if 42 - 42: OoOoOO00 / O0 . iIii1I11I1II1 / O0 / Ooo00oOo00o / OoooooooOO
 if o0o0oo0 == 1 :
  for ooiiI1ii in O0O00OoOoOOo :
   ooiiI1ii = ooiiI1ii . replace ( 'player' , 'watch' )
   O0OooOO = ooiiI1ii + '&fv=&sou='
   i1i1 = OOoOoo ( O0OooOO )
   o0oOoOo0 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( i1i1 )
   for III1IiI1i1i in o0oOoOo0 :
    o0OOOOOo0 = False
    Resolve ( III1IiI1i1i )
    if 57 - 57: iIii1I11I1II1 + iIii1I11I1II1
 elif o0o0oo0 > 1 :
  if 56 - 56: OoOO + o0oO0
  for ooiiI1ii in O0O00OoOoOOo :
   Ii1Ii1 = OOoOoo ( ooiiI1ii )
   ii1IiI11I = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Ii1Ii1 )
   OO0Ooo000O0 = ii1IiI11I
   OO0Ooo000O0 = ( str ( OO0Ooo000O0 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OO0Ooo000O0
   i1II1 ( 'DOUBLE LINK' , OO0Ooo000O0 , 424 , '' )
   if 83 - 83: o00O0oo / i11iIiiIii % I1IiI
   for url in ii1IiI11I :
    I1I11i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1i11111i1i11 = Google . resolve ( url )
    except :
     pass
    try :
     ooo0ii1iIIi11 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1i11111i1i11 ) )
     for iI1IIIII1Ii , iIiI1 in ooo0ii1iIIi11 :
      if 20 - 20: OoOO0ooOOoo0O * OoOoOO00 - I1IiI - OoOO * O0oO
      HD_URLS . append ( iI1IIIII1Ii )
      SD_URLS . append ( iIiI1 )
    except :
     pass
 else :
  pass
  if 6 - 6: o0oO0 + OoOO0ooOOoo0O / Oo + IIII % OoOoOO00 / Ooo00oOo00o
def iiIi ( ) :
 if 74 - 74: O0 + OoooooooOO / OoOO / I1IiI . ii11ii1ii % OoOO
 if 34 - 34: i1IIi . OOOo0
 I1I11i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iIii1 + 'Movies.png' )
 if 6 - 6: O0oO % OoOO % o00O0oo
 I1I11i ( 'Search Movies' , '' , 7017 , iIii1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 63 - 63: O0 . OOOo0 . O0 * iIii1I11I1II1
 if 92 - 92: OoOO / OoOO0ooOOoo0O . ii11ii1ii
def i1i ( ) :
 OOooooO0Oo = OOoOoo ( 'http://cnfstudio.com/' )
 iiIi1IIiIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , 'http://cnfstudio.com/genre/' + iIiIIi1 , 7003 , iIii1 + 'icon.png' )
  if 60 - 60: Oo . IIII % OOOo0 - O0oO
i1iIIi1 = xbmcgui . Dialog ( )
if 79 - 79: OoooooooOO / ii11ii1ii . O0
if 79 - 79: OoOO - OoOoOO00
def Ii1iiI1 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOooooO0Oo )
 OooOOOOOo = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 , url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I11iIiI1I1i11 )
 OooOOOOOo = OooOOOOOo
 for url in OooOOOOOo :
  I1I11i ( 'Next Page' , url , 7003 , '' )
  if 76 - 76: o00O0oo * iIii1I11I1II1
def iiI1iI ( url ) :
 if 84 - 84: OoooooooOO + O0oO / OOOo0 % OoOO0ooOOoo0O % ii11ii1ii * OOOo0
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  OOooOO000 = url + '&fv=&sou='
  OOooOO000 = OOooOO000 . replace ( 'player' , 'watch' )
  OOoO0oooo = I11i ( OOooOO000 )
  o0Oo = I11i ( url )
  if 4 - 4: OoOoOO00
  if 20 - 20: i11iIiiIii % OoooooooOO . IIII / o0000oOoOoO0o
def I11i ( url ) :
 if 34 - 34: i11iIiiIii / O0oO * OoOO0ooOOoo0O . Oo
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  Iii111IiIii ( url )
  if 79 - 79: O0oO
  if 31 - 31: OoOO0ooOOoo0O % O0oO
def O0oo00oOOO0o ( ) :
 oo0oooooO0 ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 5 - 5: OOooOOo / OOOo0 % o00O0oo . IIII
def OooOOoO0OOOO ( url ) :
 iiIi1IIiIi = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for i1IiI1Iiii , oOO00Oo , url in iiIi1IIiIi :
  i1II1 ( oOO00Oo , url , 222 , iIii1 + 'streams.png' )
  if 87 - 87: IIII / O0oO - Oo
  if 56 - 56: O0
def iIIIII1iI ( ) :
 oo0oooooO0 ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 oo0oooooO0 ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 18 - 18: Oo - O0
 if 85 - 85: o00O0oo - O0 * i11iIiiIii . i1IIi
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
ii11iIi1I = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
i11i1 = 'https://addons.tvaddons.ag/'
if 100 - 100: o0000oOoOoO0o % i11iIiiIii * oO0o0ooO0 / Ooo00oOo00o % ii11ii1ii + OoOO0ooOOoo0O
def IiIi1II111I ( ) :
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 o00oIIi1i1 = 'https://addons.tvaddons.ag/search/?keyword=' + I1i11
 OooIiIIII1i11I = OOoOoo ( o00oIIi1i1 )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , iIiIIi1 , 10054 , 'https://addons.tvaddons.ag/' + I1IIII1i , iI111I11I1I1 , '' )
  if 84 - 84: OoOO0ooOOoo0O + o00O0oo + OOooOOo
  if 33 - 33: o00O0oo
def ooOOO00oOOooO ( ) :
 OooIiIIII1i11I = OOoOoo ( i11i1 )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OooIiIIII1i11I )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if 'Repositories' in oOO00Oo :
   pass
  elif 'Services' in oOO00Oo :
   pass
  elif 'International' in oOO00Oo :
   pass
  else :
   oo0oooooO0 ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , iIiIIi1 , 10053 , 'https://addons.tvaddons.ag/' + I11iIiI1I1i11 , iI111I11I1I1 , '' )
   if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
   if 66 - 66: O0
def Addon ( url ) :
 OooIiIIII1i11I = OOoOoo ( url )
 oOooOOo00ooO = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OooIiIIII1i11I )
 for url in oOooOOo00ooO :
  oo0oooooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10053 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 iiIi1IIiIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OooIiIIII1i11I )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  if 'Please' in oOO00Oo :
   pass
  else :
   oo0oooooO0 ( oOO00Oo , url , 10054 , 'https://addons.tvaddons.ag/' + I11iIiI1I1i11 , iI111I11I1I1 , '' )
   if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
   if 28 - 28: iIii1I11I1II1
def iI11II1i1I1 ( url , name ) :
 OooIiIIII1i11I = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)"' ) . findall ( OooIiIIII1i11I )
 for url in iiIi1IIiIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   i1111 = xbmcgui . DialogProgress ( )
   i1111 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   O0OO0O = os . path . join ( O0oO0 , name + '.zip' )
   try :
    os . remove ( O0OO0O )
   except :
    pass
   downloader . download ( url , O0OO0O , i1111 )
   iiiiI = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print iiiiI
   print '======================================='
   extract . all ( O0OO0O , iiiiI , i1111 )
   oooOo0OOOoo0 ( )
   if 72 - 72: oO0o0ooO0 - OoooooooOO
def oooOo0OOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 25 - 25: I1IiI % OoooooooOO * Oo - i1IIi * OoOoOO00 * OoOO
 if 30 - 30: o0000oOoOoO0o % I1IiI / ii11ii1ii * O0 * o00O0oo . OOOo0
def iIi11I11 ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1007 , I1IIII1i )
def i1ioO ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I1IIII1i )
  if 25 - 25: oO0o0ooO0 . OoooooooOO * iIii1I11I1II1 . OOooOOo / O0 + o00O0oo
  if 68 - 68: Oo
def ii111I11Ii ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  if '.php' in url :
   I1I11i ( oOO00Oo , url , 1016 , I1IIII1i )
  else :
   i1II1 ( oOO00Oo , url , 222 , I1IIII1i )
   if 6 - 6: o00O0oo
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: i1IIi + Ooo00oOo00o . OOOo0 * OoOO0ooOOoo0O / IIII / o00O0oo
def oOoo ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1007 , I1IIII1i )
def oO0o ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I1IIII1i )
  if 22 - 22: Ooo00oOo00o / Oo / I1IiI
def IIiiiI1iI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0O0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0 )
 if 70 - 70: OoOO0ooOOoo0O * OoOO / OOOo0 * I1IiI * OOOo0
 if 61 - 61: OoOO + ii11ii1ii / i1IIi * OoOO
def o0OoOoooo0 ( url ) :
 OOooooO0Oo = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooooO0Oo )
 for url , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( '[COLORgreen]' + oOO00Oo + '[/COLOR]' , url , 1006 , I11iIiI1I1i11 )
def OooO0O0Ooo ( url ) :
 OOooooO0Oo = OO ( url )
 oO0O = url
 iiIi1IIiIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  if '.mp3' in oOO00Oo :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1II1 ( ( oOO00Oo ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iIii1 + 'music.png' )
  else :
   I1I11i ( ( oOO00Oo ) . replace ( '/' , '' ) , oO0O + url , 1011 , iIii1 + 'music.png' )
def IIIiIi1iiI ( ) :
 OOooooO0Oo = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for iIiIIi1 , I11iIiI1I1i11 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , ( 'http://www.cyn.net/music/' + iIiIIi1 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I11iIiI1I1i11 ) . replace ( ' ' , '%20' ) )
def iI1 ( url , img ) :
 OOooooO0Oo = OO ( url )
 I1i11111i1i11 = url
 img = img
 iiIi1IIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  i1II1 ( ( oOO00Oo ) . replace ( '.mp3' , '' ) , ( I1i11111i1i11 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 94 - 94: o0000oOoOoO0o . OOOo0
  if 73 - 73: i1IIi / OoOoOO00
def I1i1I ( ) :
 O0O00OooO = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iI = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = iI . lower ( )
 iIiIIi1 = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1i11111i1i11 = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1IiI1iI11 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 17 - 17: o0000oOoOoO0o - oO0o0ooO0 % o00O0oo
 OooIiIIII1i11I = iIiI ( iIiIIi1 )
 oooo0OOo = iIiI ( I1i11111i1i11 )
 o0OO0O0OO0oO0 = iIiI ( I1IiI1iI11 )
 if 2 - 2: o00O0oo * ii11ii1ii * OoooooooOO
 if OooIiIIII1i11I != 'Failed' :
  iiIi1IIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OooIiIIII1i11I )
  for oOO00Oo in iiIi1IIiIi :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIIi1 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 73 - 73: I1IiI + Oo
    ooo ( 'tvshows' , 'Media Info 3' )
 if oooo0OOo != 'Failed' :
  iiii111II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OooIiIIII1i11I )
  for oOO00Oo in iiii111II :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i11111i1i11 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 61 - 61: iIii1I11I1II1
    ooo ( 'tvshows' , 'Media Info 3' )
 if o0OO0O0OO0oO0 != 'Failed' :
  o0OO0 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( o0OO0O0OO0oO0 )
  for oOO00Oo in o0OO0 :
   if iI in oOO00Oo . lower ( ) :
    I1I11i ( ( oOO00Oo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1IiI1iI11 + oOO00Oo ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 47 - 47: OoooooooOO
    ooo ( 'tvshows' , 'Media Info 3' )
    if 2 - 2: I1IiI % O0oO * Oo * I1IiI
    if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
    if 26 - 26: OOooOOo % OoOO0ooOOoo0O + OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / oO0o0ooO0
    if 64 - 64: OoOO % I1IiI / OoOoOO00 % o0oO0 - oO0o0ooO0
    if 2 - 2: O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
    if 26 - 26: OoOO0ooOOoo0O * Oo
def i1iI1Ii11Ii1 ( ) :
 OOooooO0Oo = OOoOoo ( 'http://www.animetoon.org/cartoon' )
 iiIi1IIiIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOooooO0Oo )
 for iIiIIi1 , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , iIiIIi1 , 1002 , iIii1 + 'anime.png' )
  if 82 - 82: O0
  if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
  if 95 - 95: OoooooooOO % OoooooooOO . o00O0oo
def III1ii ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiii111II = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOooooO0Oo )
 for I11iIiI1I1i11 in iiii111II :
  II1iI1I11I = I11iIiI1I1i11
 o0OO0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOooooO0Oo )
 for url in o0OO0 :
  I1I11i ( 'NEXT PAGE' , url , 1002 , II1iI1I11I )
 iiIi1IIiIi = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOooooO0Oo )
 for url , oOO00Oo in iiIi1IIiIi :
  I1I11i ( oOO00Oo , url , 1003 , II1iI1I11I )
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII1ii ( url , IMAGE ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOooooO0Oo )
 for oOO00Oo , url in iiIi1IIiIi :
  print oOO00Oo + '     ' + url
  if 'easy' in url :
   o0oOoO00 ( url )
  elif 'playpanda' in url :
   o0oOoO00 ( url )
   if 94 - 94: Ooo00oOo00o + IIII + o0oO0
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oOoO00 ( url ) :
 OOooooO0Oo = OOoOoo ( url )
 iiIi1IIiIi = re . compile ( "url: '(.+?)'," ) . findall ( OOooooO0Oo )
 for url in iiIi1IIiIi :
  i1II1 ( 'STREAM' , url , 222 , iIii1 + 'anime.png' )
  if 82 - 82: Oo - Oo . iIii1I11I1II1 / OoOO0ooOOoo0O + IIII % iIii1I11I1II1
  if 61 - 61: OoOO0ooOOoo0O / Oo % OoOO0ooOOoo0O - Ooo00oOo00o + o0oO0 / o0oO0
def oo0oOO ( url ) :
 oO00Ooo0oO = urllib2 . Request ( url )
 oO00Ooo0oO . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oO00Ooo0oO . add_header ( 'referer' , url )
 OOOo = urllib2 . urlopen ( oO00Ooo0oO )
 OOooOO000 = OOOo . read ( )
 OOOo . close ( )
 return OOooOO000
 if 41 - 41: Ooo00oOo00o . O0oO * IIII * O0oO
def OO ( url ) :
 oO00Ooo0oO = urllib2 . Request ( url )
 oO00Ooo0oO . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOOo = urllib2 . urlopen ( oO00Ooo0oO )
 OOooOO000 = OOOo . read ( )
 OOOo . close ( )
 return OOooOO000
 if 74 - 74: iIii1I11I1II1 / OOooOOo
def Oo0o0O0o ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I111IiiIi1 = ( '%s%s' % ( o00o , url ) )
 OOooOO000 = OO ( url )
 iiIi1IIiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOooOO000 )
 for url , I1IIII1i , oOO00Oo in iiIi1IIiIi :
  i1II1 ( '%s' % ( oOO00Oo ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I1IIII1i )
  if 45 - 45: OoOO0ooOOoo0O
def Iii111IiIii ( url ) :
 iIiI1i111ii = xbmc . Player ( IiI ( ) )
 import urlresolver
 try : iIiI1i111ii . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( oOO00Oo ) )
 iIiI1i111ii = xbmc . Player ( IiI ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iIIi1 = xbmcgui . Dialog ( )
  if i1iIIi1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iIIi1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iIiI1i111ii . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 73 - 73: OoOO0ooOOoo0O
def o00o0 ( url ) :
 iIiI1i111ii = xbmc . Player ( IiI ( ) )
 import urlresolver
 try : iIiI1i111ii . play ( url )
 except : pass
 if 88 - 88: OoOO % Oo - o0000oOoOoO0o % OoOO + IIII - oO0o0ooO0
 if 23 - 23: O0
def IiI ( ) :
 try :
  I1iI11IiiI11i = getSet ( "core-player" )
  if ( I1iI11IiiI11i == 'DVDPLAYER' ) : IIIiIIIi11I = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( I1iI11IiiI11i == 'MPLAYER' ) : IIIiIIIi11I = xbmc . PLAYER_CORE_MPLAYER
  elif ( I1iI11IiiI11i == 'PAPLAYER' ) : IIIiIIIi11I = xbmc . PLAYER_CORE_PAPLAYER
  else : IIIiIIIi11I = xbmc . PLAYER_CORE_AUTO
 except : IIIiIIIi11I = xbmc . PLAYER_CORE_AUTO
 return IIIiIIIi11I
 return True
 if 46 - 46: OoOO0ooOOoo0O . o0000oOoOoO0o % OOOo0 - o0oO0
def I1I11i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IiI1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1I1I = True
 oO0Ooo0ooOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0Ooo0ooOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II1I1I1i1i = [ ]
  if showcontext == 'fav' :
   II1I1I1i1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in I11i1 :
   II1I1I1i1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oO0Ooo0ooOO0 . addContextMenuItems ( II1I1I1i1i )
 i1I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI1i1 , listitem = oO0Ooo0ooOO0 , isFolder = True )
 return i1I1I
 if 74 - 74: O0 % OoooooooOO * Oo + OoOO0ooOOoo0O * oO0o0ooO0
def i1II1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IiI1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1I1I = True
 oO0Ooo0ooOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0Ooo0ooOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II1I1I1i1i = [ ]
  if showcontext == 'fav' :
   II1I1I1i1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in I11i1 :
   II1I1I1i1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oO0Ooo0ooOO0 . addContextMenuItems ( II1I1I1i1i )
 i1I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI1i1 , listitem = oO0Ooo0ooOO0 , isFolder = False )
 return i1I1I
 if 100 - 100: OoOO0ooOOoo0O + o00O0oo * OOooOOo + OoOoOO00
 if 70 - 70: Oo * iIii1I11I1II1
 if 76 - 76: oO0o0ooO0 % I1IiI % iIii1I11I1II1 . OoOO0ooOOoo0O
 if 30 - 30: i1IIi
 if 75 - 75: o0000oOoOoO0o . OoOO0ooOOoo0O - iIii1I11I1II1 * Ooo00oOo00o * oO0o0ooO0
 if 93 - 93: o0oO0
def Ii1I1 ( heading , announce ) :
 class iII1IIiiI11II ( ) :
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
   try : II11IiIi11 = open ( announce ) ; O00OoOOoo = II11IiIi11 . read ( )
   except : O00OoOOoo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O00OoOOoo ) )
   return
 iII1IIiiI11II ( )
 if 49 - 49: i11iIiiIii - ii11ii1ii - o0000oOoOoO0o / OoooooooOO % I1IiI
def ooo00o0o ( ) :
 Ii1I1 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 56 - 56: I1IiI % ii11ii1ii - o00O0oo % iIii1I11I1II1
 if 76 - 76: OoooooooOO * OoooooooOO - oO0o0ooO0 - iIii1I11I1II1 . OoooooooOO / ii11ii1ii
 if 86 - 86: o0oO0
 if 51 - 51: Ooo00oOo00o - i11iIiiIii * OOOo0
 if 95 - 95: OoOO0ooOOoo0O % ii11ii1ii + OOooOOo % o0oO0
def oooOo0OOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 36 - 36: O0 / i1IIi % OoOoOO00 / oO0o0ooO0
 if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
 if 91 - 91: OoOoOO00 . OoOO0ooOOoo0O + OOooOOo
 if 8 - 8: OoOO0ooOOoo0O * Oo / oO0o0ooO0 - Ooo00oOo00o - OoooooooOO
 if 100 - 100: OoOO . iIii1I11I1II1 . iIii1I11I1II1
 if 55 - 55: OoOO
 if 37 - 37: IIII / i11iIiiIii / Oo
 if 97 - 97: O0oO . o0000oOoOoO0o / OOOo0
 if 83 - 83: o0000oOoOoO0o - ii11ii1ii * OoOO
 if 90 - 90: Oo * OOOo0
 if 75 - 75: ii11ii1ii - I1IiI * i11iIiiIii . OoooooooOO - Oo . o0000oOoOoO0o
 if 6 - 6: o0000oOoOoO0o * OoOO / OoooooooOO % o00O0oo * OOooOOo
 if 28 - 28: IIII * OOOo0 % IIII
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
def iIioOo ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + ooOo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 44 - 44: Oo . Oo + OoooooooOO * i11iIiiIii / o0000oOoOoO0o + O0oO
def iIiII11 ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + II11IiiiiI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 68 - 68: o0000oOoOoO0o * OoOoOO00 + I1IiI
def oOo ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + Oo0o000Oo0OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 14 - 14: o0oO0
def oooOoOoOO ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + OooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 32 - 32: i11iIiiIii
def II1i ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + IiiiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 34 - 34: o00O0oo + Oo - i1IIi - IIII + iIii1I11I1II1
def o0Oo00oOO ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + O0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 56 - 56: IIII * O0oO
def O00oO0O ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + IiiI111I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 98 - 98: o00O0oo
def Iiiii1 ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + O0Ooo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 18 - 18: i1IIi
def i1i1Ii1IiIII ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + I1IIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 42 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 22 - 22: o0oO0 / o0oO0 - o00O0oo % o0000oOoOoO0o . OoOO0ooOOoo0O + IIII
def OooO00oo0O0 ( url ) :
 OOooOO000 = OOoOoo ( OooO0 + i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIi1IIiIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOooOO000 )
 for oOO00Oo , url , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 in iiIi1IIiIi :
  oo0oooooO0 ( oOO00Oo , url , 5 , i1iIIIi1i , iI1iIIiiii , i1iI11i1ii11 )
 ooo ( 'movies' , 'MAIN' )
 if 73 - 73: OoooooooOO . Oo / O0 - O0
 if 25 - 25: iIii1I11I1II1 * o0000oOoOoO0o - OoOO % i11iIiiIii + o00O0oo % OoOO
 if 5 - 5: iIii1I11I1II1 . OoOO
 if 2 - 2: iIii1I11I1II1 * OOOo0 % i1IIi % ii11ii1ii + OoooooooOO + OOOo0
 if 16 - 16: OoOO0ooOOoo0O
 if 63 - 63: oO0o0ooO0
 if 11 - 11: oO0o0ooO0 - iIii1I11I1II1
 if 92 - 92: Ooo00oOo00o
 if 15 - 15: IIII / IIII + iIii1I11I1II1 % OoooooooOO
def iIIi111IiII1i ( ) :
 try :
  if os . path . exists ( II ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( II ) :
     oOo0O000oo0 = 0
     oOo0O000oo0 += len ( oOOOoo00 )
     if oOo0O000oo0 > 0 :
      for II11IiIi11 in oOOOoo00 :
       os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
  II11I = os . path . join ( iiI1IiI , "Textures13.db" )
  os . unlink ( II11I )
  i1iIIi1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 7 - 7: OoOoOO00 * o0oO0 . Oo / OOOo0
 if 43 - 43: o00O0oo + oO0o0ooO0 + i1IIi - I1IiI + OOooOOo
 if 54 - 54: ii11ii1ii + ii11ii1ii + o0000oOoOoO0o % i1IIi % i11iIiiIii
 if 100 - 100: ii11ii1ii
 if 96 - 96: OOOo0 . IIII * OoOoOO00 % IIII . O0oO * i1IIi
 if 83 - 83: iIii1I11I1II1
 if 97 - 97: i11iIiiIii + Oo * OoOO0ooOOoo0O % oO0o0ooO0 . IIII
 if 4 - 4: O0 . oO0o0ooO0 - iIii1I11I1II1
 if 19 - 19: OoOO0ooOOoo0O % Ooo00oOo00o / o00O0oo + OoOoOO00 % OoooooooOO
def oOo000O00O0 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 iI1iiIii1I11I = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( iI1iiIii1I11I ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iI1iiIii1I11I ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 32 - 32: OoooooooOO % OoOO % iIii1I11I1II1 / O0
   if 61 - 61: OoOoOO00 . O0 - o00O0oo - ii11ii1ii / i11iIiiIii - OoOoOO00
   if oOo0O000oo0 > 0 :
    if 98 - 98: o00O0oo - OOOo0 . i11iIiiIii * Oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete KODI Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 29 - 29: o00O0oo / o0oO0 % o0000oOoOoO0o
     for II11IiIi11 in oOOOoo00 :
      try :
       os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
      except :
       pass
     for ii1iIII1ii in Ooo0oOooo0 :
      try :
       shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      except :
       pass
       if 47 - 47: o0000oOoOoO0o . oO0o0ooO0 * o00O0oo - o0oO0 . o0000oOoOoO0o - OoOO0ooOOoo0O
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oOO0O00OoOo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 16 - 16: oO0o0ooO0 + IIII . o0oO0 - o00O0oo
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( oOO0O00OoOo ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 9 - 9: OOOo0
   if oOo0O000oo0 > 0 :
    if 94 - 94: OoOoOO00
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( oOo0O000oo0 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 37 - 37: OoooooooOO
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 78 - 78: OoOoOO00 + IIII
   else :
    pass
  oOoo0oO00O0Oo00 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 63 - 63: i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( oOoo0oO00O0Oo00 ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 40 - 40: Oo
   if oOo0O000oo0 > 0 :
    if 47 - 47: I1IiI
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( oOo0O000oo0 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 65 - 65: O0 + O0oO % o00O0oo * OOOo0 / o0oO0 / I1IiI
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 71 - 71: i11iIiiIii / I1IiI . OoOO
   else :
    pass
    if 33 - 33: OoOO
    if 39 - 39: Ooo00oOo00o + O0 + o0oO0 * OoOoOO00 % O0 - O0
    if 41 - 41: IIII % OOooOOo
    if 67 - 67: O0 % O0oO
 III = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( III ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( III ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 48 - 48: OoOO0ooOOoo0O . OoOO0ooOOoo0O + i11iIiiIii + ii11ii1ii % O0
   if 67 - 67: o0oO0 / o0000oOoOoO0o * OOOo0 % OoooooooOO
   if oOo0O000oo0 > 0 :
    if 46 - 46: IIII
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete WTF Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 12 - 12: OOooOOo + I1IiI . iIii1I11I1II1 % o0oO0 + i1IIi . o0oO0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 43 - 43: Oo . o0oO0 + ii11ii1ii * i11iIiiIii
   else :
    pass
    if 82 - 82: IIII
    if 51 - 51: OoOO % Ooo00oOo00o + OOooOOo + o00O0oo - OoooooooOO . Ooo00oOo00o
 II11IiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( II11IiI1 ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( II11IiI1 ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 86 - 86: iIii1I11I1II1 % OoOO - I1IiI + O0oO % Ooo00oOo00o . ii11ii1ii
   if 4 - 4: i1IIi + I1IiI
   if oOo0O000oo0 > 0 :
    if 39 - 39: iIii1I11I1II1 + o0oO0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete 4oD Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 92 - 92: o0000oOoOoO0o % i11iIiiIii % Oo
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 23 - 23: OoOoOO00 * oO0o0ooO0
   else :
    pass
    if 80 - 80: O0oO / i11iIiiIii + OoooooooOO
    if 38 - 38: ii11ii1ii % o0oO0 + i1IIi * OoooooooOO * OoOO
 OoO0o0OO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( OoO0o0OO ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( OoO0o0OO ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 10 - 10: OoOO - oO0o0ooO0 % OoOoOO00 - O0oO - i1IIi
   if 10 - 10: ii11ii1ii - o0000oOoOoO0o . O0oO
   if oOo0O000oo0 > 0 :
    if 8 - 8: iIii1I11I1II1 % OoOO + Oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete BBC iPlayer Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 24 - 24: OOooOOo / o00O0oo / o00O0oo % OoOoOO00 - OoOO * OoOO
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 58 - 58: I1IiI
   else :
    pass
    if 60 - 60: OoOoOO00
    if 90 - 90: I1IiI
    if 37 - 37: I1IiI + O0 . O0 * Oo % O0oO / oO0o0ooO0
 iIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( iIIi ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iIIi ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 98 - 98: OoOO + OoooooooOO - O0oO % i11iIiiIii / OOooOOo . OoooooooOO
   if 87 - 87: i1IIi
   if oOo0O000oo0 > 0 :
    if 33 - 33: O0oO % OoOoOO00
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Simple Downloader Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: ii11ii1ii + o0000oOoOoO0o / OOooOOo + OoooooooOO + OoOO0ooOOoo0O / IIII
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 29 - 29: o00O0oo - o00O0oo / o0oO0
   else :
    pass
    if 49 - 49: o0000oOoOoO0o + OoOO % Ooo00oOo00o - Oo - O0 - OoooooooOO
    if 4 - 4: OoOoOO00 - OoOO % Oo * i11iIiiIii
 iIiII1iiiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iIiII1iiiiI ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iIiII1iiiiI ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 80 - 80: Oo - OOooOOo - OoOoOO00 . IIII - O0 * IIII
   if 43 - 43: OOOo0 / oO0o0ooO0 / o0oO0 + iIii1I11I1II1 + OoooooooOO
   if oOo0O000oo0 > 0 :
    if 33 - 33: OoOoOO00 - IIII - o0oO0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ITV Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 92 - 92: Ooo00oOo00o * IIII
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 92 - 92: OoOO
   else :
    pass
    if 7 - 7: oO0o0ooO0
    if 73 - 73: Ooo00oOo00o % ii11ii1ii
 I1I11iIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iIiII1iiiiI ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( I1I11iIi ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 2 - 2: OOOo0
   if 69 - 69: OoooooooOO / Oo * O0oO
   if oOo0O000oo0 > 0 :
    if 99 - 99: OoOoOO00 * iIii1I11I1II1 % O0 * OoOO / OoOoOO00 % OoooooooOO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Movies4me Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: IIII . IIII % o0oO0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 42 - 42: OOooOOo . OoOO0ooOOoo0O - o0oO0
   else :
    pass
    if 33 - 33: OoOoOO00 / O0 / IIII - o0000oOoOoO0o - i1IIi
    if 8 - 8: i11iIiiIii . oO0o0ooO0 / iIii1I11I1II1 / ii11ii1ii / IIII - o00O0oo
 iI1i1I1iiii1Ii11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iIiII1iiiiI ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iI1i1I1iiii1Ii11 ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 25 - 25: i11iIiiIii / I1IiI - O0oO / Ooo00oOo00o . OOooOOo . OOooOOo
   if 6 - 6: OoOO . o0000oOoOoO0o
   if oOo0O000oo0 > 0 :
    if 43 - 43: ii11ii1ii + OOooOOo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Phoenix Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 50 - 50: OoOO % i1IIi * O0
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 4 - 4: iIii1I11I1II1 . i1IIi
   else :
    pass
    if 63 - 63: iIii1I11I1II1 + IIII % i1IIi / OOOo0 % OoOoOO00
    if 60 - 60: OOooOOo . I1IiI % O0oO / OOOo0 / O0
 IiIii11I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iIiII1iiiiI ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( IiIii11I ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 97 - 97: i1IIi + oO0o0ooO0 . o0oO0 - oO0o0ooO0
   if 53 - 53: O0 . OOOo0
   if oOo0O000oo0 > 0 :
    if 74 - 74: o0oO0 % I1IiI / Oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Music Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 2 - 2: IIII % IIII % O0oO
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 60 - 60: OoOO0ooOOoo0O
   else :
    pass
    if 73 - 73: o0oO0
    if 86 - 86: I1IiI . o0000oOoOoO0o / Oo * o0000oOoOoO0o
 I1111I1Ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iIiII1iiiiI ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( I1111I1Ii ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 68 - 68: Ooo00oOo00o + OOOo0 * OOooOOo . OoOO + I1IiI + o0oO0
   if 80 - 80: I1IiI * OoOO0ooOOoo0O
   if oOo0O000oo0 > 0 :
    if 47 - 47: o0oO0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete SuperCartoons Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 63 - 63: OoOoOO00 / i11iIiiIii % OoOoOO00 . ii11ii1ii
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 6 - 6: OoOO0ooOOoo0O + i11iIiiIii
   else :
    pass
    if 26 - 26: IIII / o00O0oo - OoooooooOO
    if 9 - 9: OoooooooOO * ii11ii1ii
 iI1II1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iIiII1iiiiI ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iI1II1i ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 27 - 27: ii11ii1ii / OoOO0ooOOoo0O
   if 33 - 33: OoooooooOO % ii11ii1ii . O0 / ii11ii1ii
   if oOo0O000oo0 > 0 :
    if 63 - 63: IIII + iIii1I11I1II1 + OOOo0 + O0oO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete TVonline Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 72 - 72: Ooo00oOo00o + i11iIiiIii + ii11ii1ii
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 96 - 96: OoOO % i1IIi / OOooOOo
   else :
    pass
    if 13 - 13: OoOoOO00 - Oo % i11iIiiIii + oO0o0ooO0
    if 88 - 88: O0 . OoOO % OOOo0
 iii111i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iIiII1iiiiI ) == True :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( iii111i ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 21 - 21: o0000oOoOoO0o
   if 50 - 50: IIII % OOOo0
   if oOo0O000oo0 > 0 :
    if 32 - 32: I1IiI . iIii1I11I1II1 % OoOO . O0 . I1IiI / oO0o0ooO0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 45 - 45: iIii1I11I1II1
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
      if 41 - 41: oO0o0ooO0 % oO0o0ooO0 - IIII % Ooo00oOo00o - OoooooooOO - oO0o0ooO0
   else :
    pass
    if 66 - 66: OOooOOo % I1IiI
    if 30 - 30: I1IiI * Oo % iIii1I11I1II1 % Ooo00oOo00o + i11iIiiIii
    if 46 - 46: OOOo0 . IIII - i11iIiiIii - O0oO
 oo0O0OO0Oo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iIIi1 = xbmcgui . Dialog ( )
 try :
  if i1iIIi1 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   oO00o0oO0O = os . path . join ( oo0O0OO0Oo , "cache.db" )
   os . unlink ( oO00o0oO0O )
   if 38 - 38: ii11ii1ii - o00O0oo * OOooOOo
 except :
  pass
  if 13 - 13: OOOo0 * OoOO
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 41 - 41: IIII
 if 16 - 16: iIii1I11I1II1
 if 94 - 94: o0oO0 % o0000oOoOoO0o % i1IIi
 if 90 - 90: o00O0oo * Ooo00oOo00o
 if 7 - 7: oO0o0ooO0 . o00O0oo . oO0o0ooO0 - O0oO
 if 33 - 33: o0oO0 + OoooooooOO - Ooo00oOo00o / i1IIi / OoooooooOO
 if 82 - 82: ii11ii1ii / OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
 if 55 - 55: OoooooooOO
 if 73 - 73: I1IiI - ii11ii1ii % Oo + ii11ii1ii - O0 . Ooo00oOo00o
def i1iIii ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 O0o00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( O0o00 ) :
   oOo0O000oo0 = 0
   oOo0O000oo0 += len ( oOOOoo00 )
   if 8 - 8: O0oO * Oo - OoOO0ooOOoo0O . iIii1I11I1II1
   if 48 - 48: i11iIiiIii / OoOoOO00 + o00O0oo + OOooOOo . O0oO % OoOO0ooOOoo0O
   if oOo0O000oo0 > 0 :
    if 88 - 88: O0oO . O0oO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Package Cache Files" , str ( oOo0O000oo0 ) + " files found" , "Do you want to delete them?" ) :
     if 71 - 71: o0oO0 . ii11ii1ii * O0 - O0oO - OoOoOO00
     for II11IiIi11 in oOOOoo00 :
      os . unlink ( os . path . join ( oooi1i1iI1iiiI , II11IiIi11 ) )
     for ii1iIII1ii in Ooo0oOooo0 :
      shutil . rmtree ( os . path . join ( oooi1i1iI1iiiI , ii1iIII1ii ) )
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
 if 5 - 5: OOooOOo
 if 66 - 66: oO0o0ooO0 / i11iIiiIii * O0
 if 78 - 78: IIII - o0000oOoOoO0o % O0 - OoOO0ooOOoo0O % Ooo00oOo00o
 if 43 - 43: Ooo00oOo00o
 if 90 - 90: OoooooooOO + O0 + ii11ii1ii / o0000oOoOoO0o / o00O0oo * ii11ii1ii
 if 100 - 100: o0000oOoOoO0o
 if 82 - 82: iIii1I11I1II1
 if 19 - 19: OOOo0
 if 66 - 66: OoOO / I1IiI
def iII1I ( url , name ) :
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00oOOo0Oo = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 i1iIIi1 = xbmcgui . Dialog ( )
 Oooo0o0oO = os . path . join ( O0oO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( Oooo0o0oO ) == False :
  if i1iIIi1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o00oOOo0Oo = os . path . join ( O0oO0 , 'advancedsettings.xml' )
   try :
    os . remove ( o00oOOo0Oo )
    print '=== GenieTv - REMOVING    ' + str ( o00oOOo0Oo ) + '    ==='
   except :
    pass
   OOooOO000 = I11 . http_GET ( url ) . content
   iiIiIIIiiI = open ( o00oOOo0Oo , "w" )
   iiIiIIIiiI . write ( OOooOO000 )
   iiIiIIIiiI . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o00oOOo0Oo ) + '    ==='
   i1iIIi1 = xbmcgui . Dialog ( )
   i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o00oOOo0Oo = os . path . join ( O0oO0 , 'advancedsettings.xml' )
  try :
   os . remove ( o00oOOo0Oo )
   print '=== GenieTv - REMOVING    ' + str ( o00oOOo0Oo ) + '    ==='
  except :
   pass
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( o00oOOo0Oo , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00oOOo0Oo ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 82 - 82: o0oO0
def OoOooO0 ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00oOOo0Oo = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 try :
  iiIiIIIiiI = open ( o00oOOo0Oo ) . read ( )
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
 if 9 - 9: I1IiI - IIII
def iiIiIiI111 ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 O0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00oOOo0Oo = os . path . join ( O0oO0 , 'advancedsettings.xml' )
 try :
  os . remove ( o00oOOo0Oo )
  i1iIIi1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o00oOOo0Oo ) + '    ==='
  i1iIIi1 . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 82 - 82: OOOo0 % Ooo00oOo00o % o0000oOoOoO0o + o0000oOoOoO0o
 if 6 - 6: Oo
 if 73 - 73: O0oO * ii11ii1ii + OOooOOo - Oo . o0000oOoOoO0o
 if 93 - 93: i11iIiiIii
 if 80 - 80: i1IIi . OOOo0 - OoOO + OoOO0ooOOoo0O + oO0o0ooO0 % OoOO
 if 13 - 13: OoOoOO00 / I1IiI / I1IiI + o0oO0
 if 49 - 49: O0 / OoOoOO00 * OOOo0 - OoooooooOO . OoOoOO00 % IIII
 if 13 - 13: OoOO . iIii1I11I1II1 . OoOO0ooOOoo0O . IIII
 if 58 - 58: o0000oOoOoO0o
 if 7 - 7: OoOoOO00 / IIII % o0000oOoOoO0o + OOOo0 - O0
def IiI1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iiIi1IIiIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for Iii1IIII1Iii , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 , iii11III1I in iiIi1IIiIi :
  if inc < 2 : i1iIIi1 = xbmcgui . Dialog ( ) ; i1iIIi1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % Iii1IIII1Iii , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IIIIIIiIIIi1iii1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iii11III1I )
  inc = inc + 1
  if 61 - 61: ii11ii1ii + iIii1I11I1II1 % OOooOOo
  if 78 - 78: iIii1I11I1II1 - OoOoOO00 / OOOo0
  if 9 - 9: ii11ii1ii * o00O0oo - IIII
  if 88 - 88: iIii1I11I1II1
  if 27 - 27: o0000oOoOoO0o * i11iIiiIii . OoOO0ooOOoo0O + o0oO0
  if 14 - 14: O0oO * Ooo00oOo00o + o0000oOoOoO0o - IIII . ii11ii1ii * OoOO
  if 100 - 100: o0000oOoOoO0o
  if 36 - 36: Ooo00oOo00o + OoOoOO00 * I1IiI
  if 14 - 14: O0oO % O0oO
def IIIIIII1i ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  o00oOOo0Oo = os . path . join ( O0oO0 , 'addons2.ini' )
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( o00oOOo0Oo , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00oOOo0Oo ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 30 - 30: IIII - oO0o0ooO0 - Ooo00oOo00o
def ii11 ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  O0oO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  o00oOOo0Oo = os . path . join ( O0oO0 , 'settings.xml' )
  OOooOO000 = I11 . http_GET ( url ) . content
  iiIiIIIiiI = open ( o00oOOo0Oo , "w" )
  iiIiIIIiiI . write ( OOooOO000 )
  iiIiIIIiiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00oOOo0Oo ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 99 - 99: ii11ii1ii - OoOO
 if 10 - 10: OoOoOO00 . Ooo00oOo00o
def o000Ooo00o00O ( ) :
 try :
  ooo0O0O0oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( ooo0O0O0oo0 ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    oo000oO = os . path . join ( ooo0O0O0oo0 , "source.db" )
    os . unlink ( oo000oO )
  i1iIIi1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 8 - 8: OOOo0 % OoOoOO00 - OOooOOo - o0000oOoOoO0o % OOOo0
 if 93 - 93: o00O0oo * oO0o0ooO0 / OoOO0ooOOoo0O
 if 88 - 88: OoOO
 if 1 - 1: Oo
 if 95 - 95: OoooooooOO / o0000oOoOoO0o % OoooooooOO / o0oO0 * IIII
def OOoOoo ( url ) :
 oO00Ooo0oO = urllib2 . Request ( url )
 oO00Ooo0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOOo = urllib2 . urlopen ( oO00Ooo0oO )
 OOooOO000 = OOOo . read ( )
 OOOo . close ( )
 return OOooOO000
 if 75 - 75: O0
 if 56 - 56: Ooo00oOo00o / OoOoOO00
 if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
 if 49 - 49: Oo + O0 + IIII . OoOoOO00 % o0oO0
 if 33 - 33: I1IiI . iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / IIII - O0 % o00O0oo
 if 27 - 27: Ooo00oOo00o + Oo
def oO0oOOooO0 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; oo00o000O = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oo00o000O :
  OooO0o = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; OooO0o = xbmc . translatePath ( OooO0o ) ;
  Oo00o = os . path . join ( OooO0o , ".." , ".." ) ; Oo00o = os . path . abspath ( Oo00o ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + Oo00o ) ; IIIi1ii = False
  try :
   for oooi1i1iI1iiiI , Ooo0oOooo0 , oOOOoo00 in os . walk ( Oo00o , topdown = True ) :
    Ooo0oOooo0 [ : ] = [ ii1iIII1ii for ii1iIII1ii in Ooo0oOooo0 if ii1iIII1ii not in Oo0oO0ooo ]
    for oOO00Oo in oOOOoo00 :
     try : os . remove ( os . path . join ( oooi1i1iI1iiiI , oOO00Oo ) )
     except :
      if oOO00Oo not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIIi1ii = True
      plugintools . log ( "Error removing " + oooi1i1iI1iiiI + " " + oOO00Oo )
    for oOO00Oo in Ooo0oOooo0 :
     try : os . rmdir ( os . path . join ( oooi1i1iI1iiiI , oOO00Oo ) )
     except :
      if oOO00Oo not in [ "Database" , "userdata" ] : IIIi1ii = True
      plugintools . log ( "Error removing " + oooi1i1iI1iiiI + " " + oOO00Oo )
   if not IIIi1ii : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0oO0O0o0O00O ( )
 if 13 - 13: iIii1I11I1II1 - OoOoOO00 % O0 . o00O0oo % Ooo00oOo00o
 if 2 - 2: OoooooooOO - o00O0oo % OoOO / OOOo0 / OOooOOo
 if 3 - 3: OoOoOO00 / OoOO0ooOOoo0O
def i1I ( ) :
 IiiIIIIi = [ ]
 IiIIIi = sys . argv [ 2 ]
 if len ( IiIIIi ) >= 2 :
  Oo0iII = sys . argv [ 2 ]
  O0ooiIIi1 = Oo0iII . replace ( '?' , '' )
  if ( Oo0iII [ len ( Oo0iII ) - 1 ] == '/' ) :
   Oo0iII = Oo0iII [ 0 : len ( Oo0iII ) - 2 ]
  OoOo0O00 = O0ooiIIi1 . split ( '&' )
  IiiIIIIi = { }
  for iIII in range ( len ( OoOo0O00 ) ) :
   iI1i1iI1iI = { }
   iI1i1iI1iI = OoOo0O00 [ iIII ] . split ( '=' )
   if ( len ( iI1i1iI1iI ) ) == 2 :
    IiiIIIIi [ iI1i1iI1iI [ 0 ] ] = iI1i1iI1iI [ 1 ]
    if 18 - 18: o0000oOoOoO0o + Oo - Ooo00oOo00o / O0oO / OoOO0ooOOoo0O
 return IiiIIIIi
 if 53 - 53: OoOO0ooOOoo0O + OOooOOo . OoOO / o0000oOoOoO0o
Ooo00O00o = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
oO0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O0O00Oo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
o0000oO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oO0000OOo00 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
ooo0oo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
ooOo0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OoOoO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
II11IiiiiI1i = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Oo0o000Oo0OOo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OooOO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
IiiiI1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
O0oo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IiiI111I11 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
O0Ooo0O = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
I1IIii11 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooO0oOOooOo0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o0o00OoOO = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iiIi1IIi1I = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
IIi1I11I1II = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
i1iI = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
o00o = base64 . decodestring ( 'Q1VOVA==' )
def oo0oooooO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 IiI1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1I1I = True
 oO0Ooo0ooOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0Ooo0ooOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO0Ooo0ooOO0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II1I1I1i1i = [ ]
  if showcontext == 'fav' :
   II1I1I1i1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in I11i1 :
   II1I1I1i1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oO0Ooo0ooOO0 . addContextMenuItems ( II1I1I1i1i )
 i1I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI1i1 , listitem = oO0Ooo0ooOO0 , isFolder = True )
 return i1I1I
 if 26 - 26: O0 - o0000oOoOoO0o . OoOoOO00 / iIii1I11I1II1
def oo0oOo ( name , url , mode , iconimage , fanart , description ) :
 IiI1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1I1I = True
 oO0Ooo0ooOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0Ooo0ooOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO0Ooo0ooOO0 . setProperty ( "Fanart_Image" , fanart )
 i1I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI1i1 , listitem = oO0Ooo0ooOO0 , isFolder = False )
 return i1I1I
 if 80 - 80: OOOo0 % ii11ii1ii % oO0o0ooO0 / IIII
 if 67 - 67: o00O0oo / O0 * oO0o0ooO0
Oo0iII = i1I ( )
iIiIIi1 = None
oOO00Oo = None
OoO0O0O0o00 = None
i1iIIIi1i = None
iI1iIIiiii = None
i1iI11i1ii11 = None
ii1iIIIiIiII = None
if 39 - 39: OOooOOo / IIII - oO0o0ooO0
if 96 - 96: o0000oOoOoO0o * ii11ii1ii * o00O0oo + ii11ii1ii % OOOo0 + i11iIiiIii
try :
 ii1iIIIiIiII = int ( Oo0iII [ "fav_mode" ] )
except :
 pass
 if 37 - 37: o0000oOoOoO0o % ii11ii1ii / o0oO0
try :
 iIiIIi1 = urllib . unquote_plus ( Oo0iII [ "url" ] )
except :
 pass
try :
 oOO00Oo = urllib . unquote_plus ( Oo0iII [ "name" ] )
except :
 pass
try :
 i1iIIIi1i = urllib . unquote_plus ( Oo0iII [ "iconimage" ] )
except :
 pass
try :
 OoO0O0O0o00 = int ( Oo0iII [ "mode" ] )
except :
 pass
try :
 iI1iIIiiii = urllib . unquote_plus ( Oo0iII [ "fanart" ] )
except :
 pass
try :
 i1iI11i1ii11 = urllib . unquote_plus ( Oo0iII [ "description" ] )
except :
 pass
 if 94 - 94: o0000oOoOoO0o / Ooo00oOo00o . OOooOOo
 if 1 - 1: Oo . OoOoOO00
print str ( ooOoOoo0O ) + ': ' + str ( O0OoO000O0OO )
print "Mode: " + str ( OoO0O0O0o00 )
print "URL: " + str ( iIiIIi1 )
print "Name: " + str ( oOO00Oo )
print "IconImage: " + str ( i1iIIIi1i )
if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % OoOO
if 98 - 98: O0oO * OoOO * I1IiI + o00O0oo * oO0o0ooO0
def ooo ( content , viewType ) :
 if 4 - 4: IIII
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 16 - 16: iIii1I11I1II1 * oO0o0ooO0 + OoOO . O0 . OOooOOo
  if 99 - 99: i11iIiiIii - oO0o0ooO0
if OoO0O0O0o00 == None :
 o0OO0oo0oOO ( )
 if 85 - 85: O0oO % ii11ii1ii
elif OoO0O0O0o00 == 1 :
 Oooo0oOO ( iIiIIi1 )
 if 95 - 95: Ooo00oOo00o * OoOO0ooOOoo0O * oO0o0ooO0 . OOooOOo
elif OoO0O0O0o00 == 44 :
 O0oOOO0ooOOO0OOO ( iIiIIi1 )
 if 73 - 73: Ooo00oOo00o
elif OoO0O0O0o00 == 2 :
 Ooo00o0Oooo ( )
 if 28 - 28: OoooooooOO - o0000oOoOoO0o
elif OoO0O0O0o00 == 3 :
 o0 ( )
 if 84 - 84: OoOoOO00
elif OoO0O0O0o00 == 21 :
 OOoo0O ( )
 if 36 - 36: OoOO0ooOOoo0O - I1IiI - iIii1I11I1II1
elif OoO0O0O0o00 == 4 :
 I1 ( )
 if 10 - 10: ii11ii1ii / o00O0oo * i1IIi % O0 + o0000oOoOoO0o
elif OoO0O0O0o00 == 5 :
 O0Oo0oOOoooOOOOo ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 25 - 25: O0oO - o00O0oo / O0 . OoooooooOO % OOOo0 . i1IIi
elif OoO0O0O0o00 == 6 :
 i1iIii ( iIiIIi1 )
 if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + OoOO + OoOO + oO0o0ooO0
elif OoO0O0O0o00 == 7 :
 iII1I ( iIiIIi1 , oOO00Oo )
 if 4 - 4: OOooOOo + o0000oOoOoO0o / oO0o0ooO0 + i1IIi % OOooOOo % oO0o0ooO0
elif OoO0O0O0o00 == 8 :
 OoOooO0 ( iIiIIi1 , oOO00Oo )
 if 80 - 80: o00O0oo
elif OoO0O0O0o00 == 9 :
 FIXREPOSADDONS ( iIiIIi1 )
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
elif OoO0O0O0o00 == 10 :
 oooOo0OOOoo0 ( )
 if 59 - 59: ii11ii1ii + o0000oOoOoO0o . OoOO
elif OoO0O0O0o00 == 11 :
 iiIiIiI111 ( iIiIIi1 )
 if 87 - 87: Ooo00oOo00o
elif OoO0O0O0o00 == 12 :
 IiI1 ( )
 if 34 - 34: O0oO . I1IiI / i11iIiiIii / oO0o0ooO0
elif OoO0O0O0o00 == 13 :
 iIIi111IiII1i ( )
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + OoOO0ooOOoo0O
elif OoO0O0O0o00 == 14 :
 oOo000O00O0 ( iIiIIi1 )
 if 31 - 31: o00O0oo * OOooOOo * o00O0oo + Ooo00oOo00o * OOooOOo . O0oO
elif OoO0O0O0o00 == 15 :
 OO0OoO0o00 ( )
 if 89 - 89: OoooooooOO * o00O0oo * OOOo0 . o0oO0 * o00O0oo / oO0o0ooO0
elif OoO0O0O0o00 == 16 :
 IIIIIII1i ( iIiIIi1 , oOO00Oo )
 if 46 - 46: i11iIiiIii
elif OoO0O0O0o00 == 17 :
 ii11 ( iIiIIi1 , oOO00Oo )
 if 15 - 15: O0 / i1IIi / i1IIi . oO0o0ooO0 % I1IiI + OOOo0
elif OoO0O0O0o00 == 18 :
 o000Ooo00o00O ( )
 if 48 - 48: O0oO % oO0o0ooO0 % o00O0oo % iIii1I11I1II1 . o00O0oo
elif OoO0O0O0o00 == 19 :
 Iiiii1I ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 14 - 14: oO0o0ooO0 * Ooo00oOo00o % O0 + o0000oOoOoO0o + ii11ii1ii
elif OoO0O0O0o00 == 40 :
 IIIIii1I ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 23 - 23: Oo % oO0o0ooO0 + o00O0oo - O0oO
elif OoO0O0O0o00 == 42 :
 ii1111iII ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 65 - 65: OoooooooOO
elif OoO0O0O0o00 == 43 :
 I1i1i1iii ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 22 - 22: OoOO0ooOOoo0O + OoOoOO00 + Oo
elif OoO0O0O0o00 == 20 :
 Ii1 ( iIiIIi1 )
 if 83 - 83: o0oO0
elif OoO0O0O0o00 == 22 :
 iIioOo ( iIiIIi1 )
 if 43 - 43: OoOO0ooOOoo0O
elif OoO0O0O0o00 == 23 :
 iIiII11 ( iIiIIi1 )
 if 84 - 84: OoOO0ooOOoo0O . IIII . oO0o0ooO0
elif OoO0O0O0o00 == 24 :
 oOo ( iIiIIi1 )
 if 2 - 2: Oo - I1IiI
elif OoO0O0O0o00 == 25 :
 oooOoOoOO ( iIiIIi1 )
 if 49 - 49: o00O0oo + OoOoOO00 / OoOO - I1IiI % I1IiI + OOOo0
elif OoO0O0O0o00 == 26 :
 II1i ( iIiIIi1 )
 if 54 - 54: o0oO0 % Oo - OoOO0ooOOoo0O
elif OoO0O0O0o00 == 27 :
 o0Oo00oOO ( iIiIIi1 )
 if 16 - 16: ii11ii1ii * oO0o0ooO0 / o0000oOoOoO0o
elif OoO0O0O0o00 == 28 :
 O00oO0O ( iIiIIi1 )
 if 46 - 46: OoOoOO00
elif OoO0O0O0o00 == 29 :
 Iiiii1 ( iIiIIi1 )
 if 13 - 13: IIII + OoOoOO00 % OOOo0
elif OoO0O0O0o00 == 30 :
 O0ooO0Oo00o ( iIiIIi1 )
 if 30 - 30: OoooooooOO - i11iIiiIii + OoOO / Oo - i11iIiiIii
elif OoO0O0O0o00 == 31 :
 i1i1Ii1IiIII ( iIiIIi1 )
 if 74 - 74: O0 . o0000oOoOoO0o
elif OoO0O0O0o00 == 32 :
 O0oOoOOOoOO ( )
 if 64 - 64: o0oO0 / i1IIi % oO0o0ooO0
elif OoO0O0O0o00 == 33 :
 O0o ( )
 if 84 - 84: I1IiI - Oo . o0oO0 . IIII - Oo
elif OoO0O0O0o00 == 35 :
 O0o000Oo ( iIiIIi1 )
 if 99 - 99: O0oO
elif OoO0O0O0o00 == 34 :
 oo000o ( iIiIIi1 )
 if 75 - 75: o0oO0 . OoOO0ooOOoo0O / IIII
elif OoO0O0O0o00 == 36 :
 O000oo ( iIiIIi1 )
 if 84 - 84: OoooooooOO . OOOo0 / OOooOOo
elif OoO0O0O0o00 == 37 :
 o0OOOO00O0Oo ( iIiIIi1 )
 if 86 - 86: Oo % I1IiI
elif OoO0O0O0o00 == 38 :
 IIi ( iIiIIi1 )
 if 77 - 77: o00O0oo % OoOO0ooOOoo0O / OoOO
elif OoO0O0O0o00 == 41 :
 oO0oOOooO0 ( Oo0iII )
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . o0oO0 - OOOo0
elif OoO0O0O0o00 == 39 :
 OooO00oo0O0 ( iIiIIi1 )
 if 23 - 23: OOOo0
elif OoO0O0O0o00 == 45 :
 TEXTS ( )
 if 7 - 7: oO0o0ooO0 % ii11ii1ii
elif OoO0O0O0o00 == 46 :
 ooo00o0o ( )
 if 64 - 64: O0oO + i11iIiiIii
elif OoO0O0O0o00 == 47 :
 GEVID ( )
 if 35 - 35: I1IiI + i1IIi % OoOO0ooOOoo0O
elif OoO0O0O0o00 == 48 :
 OooOo0ooo ( oOO00Oo , iIiIIi1 , i1iI11i1ii11 )
 if 68 - 68: IIII . o0oO0
elif OoO0O0O0o00 == 49 :
 Ii ( )
 if 64 - 64: i1IIi + Oo * OOOo0 / OoOO0ooOOoo0O
elif OoO0O0O0o00 == 222 :
 Iii111IiIii ( iIiIIi1 )
 if 3 - 3: Oo / o0oO0 + o0oO0 . ii11ii1ii
elif OoO0O0O0o00 == 333 :
 Oo0o0O0o ( iIiIIi1 )
 if 50 - 50: iIii1I11I1II1 * OoOO
 if 85 - 85: i1IIi
elif OoO0O0O0o00 == 1001 :
 i1iI1Ii11Ii1 ( )
 if 100 - 100: OoooooooOO / o0000oOoOoO0o % Ooo00oOo00o + o00O0oo
elif OoO0O0O0o00 == 1005 :
 oOoo ( )
 if 42 - 42: Oo / IIII . o00O0oo * OOOo0
elif OoO0O0O0o00 == 1007 :
 oO0o ( iIiIIi1 )
 if 54 - 54: I1IiI * oO0o0ooO0 + Ooo00oOo00o
elif OoO0O0O0o00 == 1010 :
 o0OoOoooo0 ( iIiIIi1 )
 if 93 - 93: OOooOOo / OOOo0
elif OoO0O0O0o00 == 1011 :
 OooO0O0Ooo ( iIiIIi1 )
 if 47 - 47: Oo * OoOO0ooOOoo0O
elif OoO0O0O0o00 == 1030 :
 IIIiIi1iiI ( )
 if 98 - 98: OoOO - OoOO . o0oO0
elif OoO0O0O0o00 == 1031 :
 iI1 ( iIiIIi1 , i1iIIIi1i )
 if 60 - 60: OOOo0 * ii11ii1ii / O0 + o0000oOoOoO0o + IIII
elif OoO0O0O0o00 == 1006 :
 Parse . ParseURL ( iIiIIi1 )
 if 66 - 66: IIII * Oo . OoooooooOO * O0oO
elif OoO0O0O0o00 == 2030 :
 Parse . addonParseURL ( iIiIIi1 )
 if 93 - 93: IIII / i1IIi
elif OoO0O0O0o00 == 2031 :
 Parse . apkParseURL ( iIiIIi1 )
 if 47 - 47: o0oO0 - o00O0oo
elif OoO0O0O0o00 == 1002 :
 III1ii ( iIiIIi1 )
 if 98 - 98: OoOO . O0oO / I1IiI . o0oO0
elif OoO0O0O0o00 == 1003 :
 iII1ii ( iIiIIi1 , i1iIIIi1i )
 if 1 - 1: OoOO0ooOOoo0O
elif OoO0O0O0o00 == 1004 :
 o0oOoO00 ( iIiIIi1 )
 if 87 - 87: O0 * OoOoOO00 + iIii1I11I1II1 % OoOO % i11iIiiIii - I1IiI
elif OoO0O0O0o00 == 1008 :
 II1I1ii1ii11 ( )
 if 73 - 73: oO0o0ooO0 + o00O0oo
elif OoO0O0O0o00 == 1009 :
 M3UPLAY ( iIiIIi1 )
 if 37 - 37: OoOO - iIii1I11I1II1 + OoOoOO00 . o00O0oo % iIii1I11I1II1
elif OoO0O0O0o00 == 2001 :
 OooOOoO0OOOO ( iIiIIi1 )
 if 17 - 17: O0oO + i1IIi % O0
elif OoO0O0O0o00 == 1013 :
 IIIIiII1i ( )
 if 65 - 65: IIII
elif OoO0O0O0o00 == 1014 :
 iiiiI1IiI1I1 ( )
 if 50 - 50: OoOoOO00 / Ooo00oOo00o
elif OoO0O0O0o00 == 1015 :
 iI111i11iI1 ( iIiIIi1 )
 if 79 - 79: ii11ii1ii - iIii1I11I1II1 % i1IIi / Oo + OoOoOO00
elif OoO0O0O0o00 == 1016 :
 ii111I11Ii ( iIiIIi1 )
 if 95 - 95: OoOO
elif OoO0O0O0o00 == 1023 :
 O0OoO0O00o0oO ( )
 if 48 - 48: o0000oOoOoO0o / iIii1I11I1II1 % OoOoOO00
elif OoO0O0O0o00 == 1024 :
 iIi11I11 ( )
 if 39 - 39: i1IIi . ii11ii1ii / o0000oOoOoO0o / o0000oOoOoO0o
elif OoO0O0O0o00 == 1025 :
 i1ioO ( iIiIIi1 )
 if 100 - 100: OoooooooOO - OoooooooOO + IIII
elif OoO0O0O0o00 == 4001 :
 I1i1I1II ( )
 if 32 - 32: I1IiI * OOooOOo / OoooooooOO
elif OoO0O0O0o00 == 4002 :
 i1IiIiiI ( )
 if 90 - 90: O0oO
elif OoO0O0O0o00 == 4003 :
 O0o0O00Oo0o0 ( )
 if 35 - 35: OoOoOO00 / o00O0oo
elif OoO0O0O0o00 == 3000 :
 O0oo00oOOO0o ( )
 if 79 - 79: I1IiI + O0oO * oO0o0ooO0 * o00O0oo
elif OoO0O0O0o00 == 404 :
 IIiiiI1iI ( oOO00Oo , iIiIIi1 , i1iIIIi1i )
 if 53 - 53: OoOO0ooOOoo0O / Oo
elif OoO0O0O0o00 == 7030 :
 O0O0ooOoOO0OO ( )
 if 10 - 10: ii11ii1ii . OOooOOo
elif OoO0O0O0o00 == 7021 :
 O0OoooI11iI1I ( oOO00Oo )
 if 75 - 75: O0 * i1IIi - o0000oOoOoO0o / OoOO0ooOOoo0O % OoOO0ooOOoo0O / I1IiI
elif OoO0O0O0o00 == 7022 :
 oo0OoOO0o0o ( oOO00Oo )
 if 5 - 5: O0 - oO0o0ooO0 / O0oO . OOooOOo
elif OoO0O0O0o00 == 7000 :
 OoOO00 ( oOO00Oo , iIiIIi1 , img )
 if 7 - 7: ii11ii1ii - I1IiI
elif OoO0O0O0o00 == 7050 :
 OOOO00OooO ( )
 if 54 - 54: OoOO / iIii1I11I1II1 / OoooooooOO . i1IIi - I1IiI
elif OoO0O0O0o00 == 7051 :
 O0oO0o000o ( iIiIIi1 )
 if 57 - 57: iIii1I11I1II1 * o00O0oo * oO0o0ooO0 / OoOO
elif OoO0O0O0o00 == 7060 :
 o0ii1iIi1Ii1 ( )
 if 46 - 46: o00O0oo
elif OoO0O0O0o00 == 7061 :
 IIi1i ( iIiIIi1 )
 if 61 - 61: OOooOOo / o0oO0 - OoOoOO00
elif OoO0O0O0o00 == 7063 :
 oOOoOOO0oo0 ( iIiIIi1 )
 if 87 - 87: ii11ii1ii / OOOo0
elif OoO0O0O0o00 == 7062 :
 ooooo0Oo0 ( iIiIIi1 )
 if 45 - 45: I1IiI * o0oO0 / OoooooooOO + Ooo00oOo00o . O0oO / Ooo00oOo00o
elif OoO0O0O0o00 == 7064 :
 NATatozcat ( )
 if 64 - 64: o00O0oo / i1IIi % OOOo0 - OOooOOo
elif OoO0O0O0o00 == 7067 :
 oOo00o ( iIiIIi1 )
 if 11 - 11: ii11ii1ii - OoooooooOO
elif OoO0O0O0o00 == 7066 :
 NATatozA ( iIiIIi1 )
 if 16 - 16: IIII % OoooooooOO - o0oO0 * o00O0oo - o00O0oo
elif OoO0O0O0o00 == 7065 :
 II111i1ii1iII ( iIiIIi1 )
 if 27 - 27: IIII + iIii1I11I1II1 / Oo + Ooo00oOo00o % Oo + Ooo00oOo00o
elif OoO0O0O0o00 == 7070 :
 i1i1II1I ( )
 if 77 - 77: Oo * o0oO0 % o00O0oo
elif OoO0O0O0o00 == 7071 :
 DIZIlist ( iIiIIi1 )
 if 2 - 2: o0000oOoOoO0o / Oo / o00O0oo / ii11ii1ii / OoooooooOO
elif OoO0O0O0o00 == 7072 :
 DIZIpull ( iIiIIi1 )
 if 22 - 22: iIii1I11I1II1 * OOOo0 / o0000oOoOoO0o + I1IiI
elif OoO0O0O0o00 == 7073 :
 WATCHDIZI ( iIiIIi1 )
 if 98 - 98: OoOO0ooOOoo0O
elif OoO0O0O0o00 == 7002 :
 i1i ( )
 if 69 - 69: OoOoOO00 + Oo - OoOO . Oo / iIii1I11I1II1 * iIii1I11I1II1
elif OoO0O0O0o00 == 7003 :
 Ii1iiI1 ( iIiIIi1 )
 if 75 - 75: Ooo00oOo00o % OoooooooOO
elif OoO0O0O0o00 == 7004 :
 iiI1iI ( iIiIIi1 )
 if 16 - 16: O0 / i1IIi
elif OoO0O0O0o00 == 7020 :
 I11i ( iIiIIi1 )
 if 58 - 58: OOooOOo / i11iIiiIii / O0 % o0000oOoOoO0o % OOOo0
elif OoO0O0O0o00 == 7001 :
 Oo0o00ooOOOoOo ( )
 if 86 - 86: IIII + I1IiI / OOOo0 + o0000oOoOoO0o % o0000oOoOoO0o / i11iIiiIii
elif OoO0O0O0o00 == 7010 :
 i111IiiI1Ii ( iIiIIi1 )
 if 12 - 12: I1IiI + OOooOOo . O0oO
elif OoO0O0O0o00 == 7011 :
 ii11iiI11I ( iIiIIi1 )
 if 52 - 52: Ooo00oOo00o
elif OoO0O0O0o00 == 7012 :
 iiIi11i1IiI ( iIiIIi1 )
 if 4 - 4: o00O0oo % ii11ii1ii + o0000oOoOoO0o - ii11ii1ii
elif OoO0O0O0o00 == 7013 :
 cnfTVPlay2 ( iIiIIi1 )
elif OoO0O0O0o00 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iIiIIi1 )
elif OoO0O0O0o00 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iIiIIi1 )
elif OoO0O0O0o00 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oOO00Oo , iIiIIi1 , i1iIIIi1i )
elif OoO0O0O0o00 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OoO0O0O0o00 == 7018 :
 iiIi ( )
elif OoO0O0O0o00 == 7019 :
 CNF_Studio_Indexer . List_Movies ( iIiIIi1 )
elif OoO0O0O0o00 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iIiIIi1 )
elif OoO0O0O0o00 == 7024 :
 CNF_Studio_Indexer . Box_Office ( iIiIIi1 )
 if 98 - 98: o00O0oo - O0 * OoOO * o00O0oo * o00O0oo
elif OoO0O0O0o00 == 8000 :
 I1III1iIi ( )
elif OoO0O0O0o00 == 8001 :
 ooOoo000oO ( )
elif OoO0O0O0o00 == 8002 :
 IiiOooooOo0 ( )
elif OoO0O0O0o00 == 8003 :
 II1i11 ( )
elif OoO0O0O0o00 == 8004 :
 ii1I ( )
elif OoO0O0O0o00 == 8005 :
 oOOoO ( )
elif OoO0O0O0o00 == 8006 :
 o0O ( oOO00Oo , iIiIIi1 )
elif OoO0O0O0o00 == 8030 :
 O000OOOOOo ( iIiIIi1 )
elif OoO0O0O0o00 == 8045 :
 I1iIiI1IiIIII ( )
elif OoO0O0O0o00 == 8046 :
 I1iiIi111I ( iIiIIi1 )
elif OoO0O0O0o00 == 8047 :
 iI1IiiiI11 ( iIiIIi1 )
elif OoO0O0O0o00 == 8040 :
 O0oOo ( )
elif OoO0O0O0o00 == 8041 :
 OO0oo0O0OOO0 ( iIiIIi1 )
elif OoO0O0O0o00 == 8042 :
 O00O0O ( iIiIIi1 )
elif OoO0O0O0o00 == 8043 :
 yt . PlayVideo ( iIiIIi1 )
elif OoO0O0O0o00 == 8044 :
 OOo0o ( iIiIIi1 )
elif OoO0O0O0o00 == 8060 :
 o00ii111Iiii ( )
elif OoO0O0O0o00 == 8061 :
 Iii1Ii ( iIiIIi1 )
elif OoO0O0O0o00 == 8070 :
 O0Oo ( )
elif OoO0O0O0o00 == 8071 :
 iIIiI11i ( iIiIIi1 )
elif OoO0O0O0o00 == 7080 :
 Oooo0oOOO0 ( iIiIIi1 )
elif OoO0O0O0o00 == 8090 :
 I1iIIII1 ( )
elif OoO0O0O0o00 == 8091 :
 OO0I11Ii1iI11iI1 ( iIiIIi1 )
elif OoO0O0O0o00 == 8092 :
 i1III1 ( iIiIIi1 )
elif OoO0O0O0o00 == 8081 :
 I1oOooo00O ( )
elif OoO0O0O0o00 == 8062 :
 iii1IIiI ( iIiIIi1 )
elif OoO0O0O0o00 == 8063 :
 iIIiI11i1I11 ( iIiIIi1 )
elif OoO0O0O0o00 == 8050 :
 IiiiiI1i1Iii ( )
elif OoO0O0O0o00 == 8051 :
 oo00oO0o ( iIiIIi1 )
elif OoO0O0O0o00 == 8052 :
 OOoooO00o0oo0 ( iIiIIi1 )
elif OoO0O0O0o00 == 8085 :
 ii1ii ( )
elif OoO0O0O0o00 == 8086 :
 o00O00Oo00O ( iIiIIi1 )
elif OoO0O0O0o00 == 8087 :
 OOoOOOo0Ooo0 ( iIiIIi1 )
elif OoO0O0O0o00 == 8088 :
 o0OOOOO0O ( iIiIIi1 , oOO00Oo )
elif OoO0O0O0o00 == 9000 :
 Oo0OoO00oOO0o ( )
elif OoO0O0O0o00 == 1111 :
 I1i1I ( )
elif OoO0O0O0o00 == 9001 :
 III1Ii1i1I1 ( )
elif OoO0O0O0o00 == 9002 :
 IIIIiIi11iiIi ( )
elif OoO0O0O0o00 == 9003 :
 Ii1i1 ( )
elif OoO0O0O0o00 == 50 :
 Ii1I1i ( iIiIIi1 )
elif OoO0O0O0o00 == 9020 :
 oooo000 ( )
elif OoO0O0O0o00 == 9021 :
 iIiiIIIiI1Ii ( )
elif OoO0O0O0o00 == 9022 :
 IIiiiiiIiIIi ( )
elif OoO0O0O0o00 == 9023 :
 iiIiiIi1 ( )
elif OoO0O0O0o00 == 9024 :
 I1iIiiiI1 ( iIiIIi1 )
elif OoO0O0O0o00 == 9030 :
 iIIi1Ii1III ( iIiIIi1 )
elif OoO0O0O0o00 == 9031 :
 Oooo00 ( iIiIIi1 )
elif OoO0O0O0o00 == 9032 :
 iii1II1iI1IIi ( iIiIIi1 )
elif OoO0O0O0o00 == 9033 :
 Ii11iiI1 ( iIiIIi1 )
elif OoO0O0O0o00 == 7085 :
 i11IiI1iiI11 ( iIiIIi1 )
elif OoO0O0O0o00 == 7086 :
 IIii1III ( iIiIIi1 )
elif OoO0O0O0o00 == 7087 :
 o00iIiiiII ( i1iI11i1ii11 )
elif OoO0O0O0o00 == 10000 : IIiI1I ( )
elif OoO0O0O0o00 == 10001 : iiii1IIi ( )
elif OoO0O0O0o00 == 10002 : oOOO ( )
elif OoO0O0O0o00 == 10003 : iIiiI1iI ( )
elif OoO0O0O0o00 == 10004 : OOo ( )
elif OoO0O0O0o00 == 10005 : I11I1i1iIII1I ( )
elif OoO0O0O0o00 == 10006 : OOooo0O0o0 ( iIiIIi1 )
elif OoO0O0O0o00 == 10007 : oOIIiIi ( iIiIIi1 , i1iIIIi1i )
elif OoO0O0O0o00 == 10008 : I1i111i ( )
elif OoO0O0O0o00 == 10009 : O00oOoo0OoO0 ( )
elif OoO0O0O0o00 == 10010 : i11i1Ii1 ( iIiIIi1 )
elif OoO0O0O0o00 == 10011 : OOO00OOo0o0Oo ( iIiIIi1 )
elif OoO0O0O0o00 == 10012 : o00o0 ( iIiIIi1 )
elif OoO0O0O0o00 == 10013 : ii111i1iI ( iIiIIi1 )
elif OoO0O0O0o00 == 10014 : Oooo0 ( )
elif OoO0O0O0o00 == 10015 : OoOo ( )
elif OoO0O0O0o00 == 10016 : O0iII1 ( iIiIIi1 )
elif OoO0O0O0o00 == 10017 : i1iIi ( )
elif OoO0O0O0o00 == 10018 : IiiO0o0o ( )
elif OoO0O0O0o00 == 10019 : OO00oo0o ( )
elif OoO0O0O0o00 == 10020 : I11I1 ( )
elif OoO0O0O0o00 == 10021 : OooOO0o0 ( )
elif OoO0O0O0o00 == 10022 : iiii1I1 ( iIiIIi1 )
elif OoO0O0O0o00 == 10023 : i1I11iIiII ( oOO00Oo , iIiIIi1 )
elif OoO0O0O0o00 == 10024 : OoO000O ( iIiIIi1 )
elif OoO0O0O0o00 == 10025 : O000OOO0OOo ( )
elif OoO0O0O0o00 == 10026 : ooo000ooO0000 ( )
elif OoO0O0O0o00 == 10027 : I1Ii1111iIi ( )
elif OoO0O0O0o00 == 10028 : ooOooo0 ( )
elif OoO0O0O0o00 == 10029 : ooO0o ( )
elif OoO0O0O0o00 == 423 : oOO ( iIiIIi1 )
elif OoO0O0O0o00 == 426 : i1i1i1I ( iIiIIi1 )
elif OoO0O0O0o00 == 10030 : III11I1 ( )
elif OoO0O0O0o00 == 10031 : Latest_Izle_Movies ( )
elif OoO0O0O0o00 == 10032 : i1II1I1Iii1 ( )
elif OoO0O0O0o00 == 10033 : ooo0OOO ( )
elif OoO0O0O0o00 == 10034 : OooO0oo ( )
elif OoO0O0O0o00 == 10035 : O00 ( )
elif OoO0O0O0o00 == 10036 : Ooo00O0o ( iIiIIi1 )
elif OoO0O0O0o00 == 10037 : OoOOO00 ( iIiIIi1 )
elif OoO0O0O0o00 == 10038 : O0Oooo ( )
elif OoO0O0O0o00 == 10039 : ooOoOO0OoO00o ( iIiIIi1 )
elif OoO0O0O0o00 == 10040 : OooOOo0 ( )
elif OoO0O0O0o00 == 10041 : I1iII11iIII1i1I ( iIiIIi1 )
elif OoO0O0O0o00 == 10042 : O0ooOoO ( iIiIIi1 )
elif OoO0O0O0o00 == 10043 : i1iiiIii11 ( )
elif OoO0O0O0o00 == 10044 : oOo0O0O0 ( iIiIIi1 )
elif OoO0O0O0o00 == 10045 : II1II ( iIiIIi1 )
elif OoO0O0O0o00 == 10046 : IiiIi ( iIiIIi1 )
elif OoO0O0O0o00 == 10047 : i1I1iIi1IiI ( iIiIIi1 )
elif OoO0O0O0o00 == 10048 : O00O00O000OOO ( iIiIIi1 )
elif OoO0O0O0o00 == 10049 : Ooo0Oo0oo0 ( iIiIIi1 )
elif OoO0O0O0o00 == 10050 : iIIIII1iI ( )
elif OoO0O0O0o00 == 10051 : ooOOO00oOOooO ( )
elif OoO0O0O0o00 == 10052 : IiIi1II111I ( )
elif OoO0O0O0o00 == 10053 : Addon ( iIiIIi1 )
elif OoO0O0O0o00 == 10054 : iI11II1i1I1 ( iIiIIi1 , oOO00Oo )
elif OoO0O0O0o00 == 10055 :
 I1i ( "addFavorite" )
 try :
  oOO00Oo = oOO00Oo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOO00Oo = oOO00Oo . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiI11I1i1i1iI ( oOO00Oo , iIiIIi1 , i1iIIIi1i , iI1iIIiiii , ii1iIIIiIiII )
elif OoO0O0O0o00 == 10056 :
 I1i ( "rmFavorite" )
 try :
  oOO00Oo = oOO00Oo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOO00Oo = oOO00Oo . split ( '  - ' ) [ 0 ]
 except :
  pass
 o00o00OoO00o0 ( oOO00Oo )
elif OoO0O0O0o00 == 10057 :
 I1i ( "getFavorites" )
 oOOo ( )
elif OoO0O0O0o00 == 10058 : IIIIii ( )
if 44 - 44: IIII + o0000oOoOoO0o
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
