# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
if 64 - 64: i11iIiiIii
import re
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
import extract
import downloader
from imports import yt
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from datetime import date , datetime , timedelta
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = 'plugin.video.GenieMusic'
o0OOO = 'plugin.video.GenieMusic'
iIiiiI = "0.0.1"
Iii1ii1II11i = xbmc . translatePath ( 'special://home/addons/' )
iI111iI = base64 . decodestring
IiII = datetime . now ( )
iI1Ii11111iIi = xbmc . translatePath ( 'special://logpath/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = xbmcaddon . Addon ( id = o0OOO )
I1i1iiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
iiIIIII1i1iI = 'plugin.video.GenieMusic'
o0oO0 = xbmcgui . DialogProgress ( )
oo00 = "Genie Music"
o00 = Net ( )
Oo0oO0ooo = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieMusic' )
o0oOoO00o = xbmc . translatePath ( 'special://home/' )
iI111iI = base64 . decodestring
i1 = xbmc . translatePath ( 'special://profile/' )
oOOoo00O0O = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
i1111 = os . path . join ( o0oOoO00o , 'userdata' )
i11 = os . path . join ( i1111 , 'addon_data' , I1IiI )
I11 = os . path . join ( Iii1ii1II11i , 'packages' )
Oo0o0000o0o0 = O0oo0OO0 . getSetting ( 'Downloads' )
oOo0oooo00o = iI111iI ( 'L2dtLnBocA==' )
oO0o0o0ooO0oO = iI111iI ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L2dlbmllbXVzaWM=' )
oo0o0O00 = oO0o0o0ooO0oO + oOo0oooo00o
oO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OOO , 'icon.png' ) )
i1iiIIiiI111 = oO0o0o0ooO0oO + ( iI111iI ( 'L2FydC8=' ) )
oooOOOOO = 'Some Website'
i1iiIII111ii = os . path . join ( i11 , 'wizard.log' )
i1iIIi1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieMusic' )
ii11iIi1I = xbmc . translatePath ( 'special://thumbnails' ) ;
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OOO , 'fanart.jpg' ) )
OOooO0OOoo = O0oo0OO0 . getLocalizedString
iIii1 = CookieJar ( )
oOOoO0 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( iIii1 ) )
oOOoO0 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O0OoO000O0OO = int ( sys . argv [ 1 ] )
iiI1IiI = xbmc . translatePath ( O0oo0OO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i1111 = xbmc . translatePath ( 'special://home/userdata/' )
II = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
ooOoOoo0O = i1iIIi1 + '/addons.ini'
OooO0 = xbmcgui . Dialog ( )
II11iiii1Ii = xbmcgui . Dialog ( )
if os . path . exists ( II ) == True :
 OO0o = open ( II ) . read ( )
else : OO0o = [ ]
if 82 - 82: i1I1i1Ii11 . IIIIII11i1I - o0o0OOO0o0 % IIII % o0O0 . o0
if 9 - 9: OO0oo0oOO + I1iii - iIii1I11I1II1 / IIII - OoooooooOO
if 22 - 22: I1iii % II111iiii - iIii1I11I1II1
def iiIi ( ) :
 Oo0O0OOOoo ( '[COLORorangered]Music Library[/COLOR]' , oo0o0O00 , 210 , i1iiIIiiI111 + 'music10' , oO , '[COLORsteelblue]Music Library[/COLOR]' )
 Oo0O0OOOoo ( '[COLORorangered]Music Search[/COLOR]' , oo0o0O00 , 16 , i1iiIIiiI111 + 'music7' , oO , '[COLORsteelblue]Music Search[/COLOR]' )
 Oo0O0OOOoo ( '[COLORorangered]Music Vids[/COLOR]' , oo0o0O00 , 11 , i1iiIIiiI111 + 'music12' , oO , '[COLORsteelblue]Music Vids[/COLOR]' )
 Oo0O0OOOoo ( '[COLORorangered]DJing Music Channels[/COLOR]' , '' , 13 , i1iiIIiiI111 + 'music13' , oO , '[COLORsteelblue]DJing Music Channels[/COLOR]' )
 Oo0O0OOOoo ( '[COLORorangered]Karaoke[/COLOR]' , iI111iI ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3F1aWNrc2lsdmVyL0dlbmllL2thcmFva2Uv' ) , 212 , i1iiIIiiI111 + 'karaoke.png' , oO , '[COLORsteelblue]Karaoke[/COLOR]' )
 Oo0O0OOOoo ( '[COLORorangered]Lyrics[/COLOR]' , iI111iI ( 'aHR0cHM6Ly93d3cuYXpseXJpY3MuY29tLw==' ) , 21 , i1iiIIiiI111 + 'lyrics.png' , oO , '[COLORsteelblue]Lyrics[/COLOR]' )
 Oo0O0OOOoo ( '[COLORorangered]Radio[/COLOR]' , iI111iI ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3FzYS90aHVuZGVyc3RydWNrL3R4dC9yYWRpby50eHQ=' ) , 90037 , i1iiIIiiI111 + 'music5' , oO , '[COLORsteelblue]Radio[/COLOR]' )
 Oo0O0OOOoo ( '[COLORorangered]Maintenance[/COLOR]' , '' , 5 , i1iiIIiiI111 + 'music2' , oO , '[COLORsteelblue]Maintenance[/COLOR]' )
 if 95 - 95: OoO0O00 % i1I1i1Ii11 . O0
 if 15 - 15: I1iii / IIII . IIII - i1IIi
 if 53 - 53: o0 + I1IiiI * i1I1i1Ii11
 if 61 - 61: i1IIi * IIIIII11i1I / OoooooooOO . i11iIiiIii . OoOoOO00
 if 60 - 60: o0o0OOO0o0 / o0o0OOO0o0
def I1II1III11iii ( ) :
 Oo000 ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , i1iiIIiiI111 + 'music2' , iI111I11I1I1 , '[COLORsteelblue]Delete Packages[/COLOR]' )
 Oo000 ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , i1iiIIiiI111 + 'music2' , iI111I11I1I1 , '[COLORsteelblue]Delete Cache[/COLOR]' )
 Oo000 ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , i1iiIIiiI111 + 'music2' , iI111I11I1I1 , '[COLORsteelblue]View Log File[/COLOR]' )
 Oo000 ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , i1iiIIiiI111 + 'music2' , iI111I11I1I1 , '[COLORsteelblue]Force Refresh[/COLOR]' )
 Oo000 ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , i1iiIIiiI111 + 'music2' , iI111I11I1I1 , '[COLORsteelblue]Force Close[/COLOR]' )
 if 51 - 51: i11iIiiIii . I1IiiI + II111iiii
def II111ii1II1i ( url , description ) :
 Oo0O0OOOoo ( '[COLORsteelblue]Search Lyrics[/COLOR]' , 'http:' + url , 20 , i1iiIIiiI111 + 'lyrics.png' , OoOo00o , '[COLORsteelblue]Search Lyrics[/COLOR]' )
 o0OOoo0OO0OOO = ( '[COLORorangered]' + description + '[/COLOR]' )
 iI1iI1I1i1I = iIi11Ii1 ( url )
 Ii11iII1 = re . compile ( '<a class="btn btn-menu" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for url , Oo0O0O0ooO0O in Ii11iII1 :
  Oo0O0OOOoo ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' , 'http:' + url , 22 , i1iiIIiiI111 + Oo0O0O0ooO0O + '.png' , OoOo00o , o0OOoo0OO0OOO + '[CR][CR]' + Oo0O0O0ooO0O )
def IIIIii ( url , description ) :
 Oo0O0OOOoo ( '[COLORsteelblue]Search Lyrics[/COLOR]' , 'http:' + url , 20 , i1iiIIiiI111 + 'lyrics.png' , OoOo00o , '[COLORsteelblue]Search Lyrics[/COLOR]' )
 o0OOoo0OO0OOO = ( '[COLORorangered]' + description + '[/COLOR]' )
 iI1iI1I1i1I = iIi11Ii1 ( url )
 Ii11iII1 = re . compile ( '<a href="([^"]*)">(.+?)</a><br>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for url , Oo0O0O0ooO0O in Ii11iII1 :
  Oo0O0OOOoo ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' , 'https://www.azlyrics.com/' + url , 23 , i1iiIIiiI111 + 'lyrics.png' , OoOo00o , o0OOoo0OO0OOO + '[CR][CR]' + Oo0O0O0ooO0O )
def O0o0 ( url , description ) :
 Oo0O0OOOoo ( '[COLORsteelblue]Search Lyrics[/COLOR]' , 'http:' + url , 20 , i1iiIIiiI111 + 'lyrics.png' , OoOo00o , '[COLORsteelblue]Search Lyrics[/COLOR]' )
 o0OOoo0OO0OOO = ( '[COLORorangered]' + description + '[/COLOR]' )
 iI1iI1I1i1I = iIi11Ii1 ( url )
 OO00Oo = re . compile ( '<!-- start of song list -->(.+?)<!-- end of song list -->' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 O0OOO0OOoO0O = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a><br>' , re . DOTALL ) . findall ( str ( OO00Oo ) )
 for url , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  O00Oo000ooO0 = '\''
  Oo000 ( ( '[COLORsteelblue]' + ( Oo0O0O0ooO0O ) . replace ( O00Oo000ooO0 , '' ) . replace ( '/' , '' ) + '[/COLOR]' ) , ( url ) . replace ( '../' , 'https://www.azlyrics.com/' ) , 24 , i1iiIIiiI111 + 'lyrics.png' , OoOo00o , o0OOoo0OO0OOO + '[CR][CR]' + ( '[COLORsteelblue]' + ( Oo0O0O0ooO0O ) . replace ( O00Oo000ooO0 , '' ) . replace ( '/' , '' ) + '[/COLOR]' ) )
def OoO0O00IIiII ( url , description ) :
 o0OOoo0OO0OOO = ( '[COLORorangered]' + description + '[/COLOR]' )
 iI1iI1I1i1I = iIi11Ii1 ( url )
 OO00Oo = re . compile ( '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->(.+?)</div>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for II111ii1II1i in OO00Oo :
  II111ii1II1i = ( '[COLORsteelblue]' + II111ii1II1i + '[/COLOR]' ) . replace ( '<br>' , '' ) . replace ( '<i>' , '[CR]' ) . replace ( '</i>' , '[CR]' )
  o0ooOooo000oOO ( o0OOoo0OO0OOO , II111ii1II1i )
def Oo0oOOo ( ) :
 Oo0OoO00oOO0o = II11iiii1Ii . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = 'https://search.azlyrics.com/search.php?q=' + ( Oo0OoO00oOO0o ) . replace ( ' ' , '+' ) + '&w=songs&p=1'
 iI1iI1I1i1I = iIi11Ii1 ( OOO00O )
 O0OOO0OOoO0O = re . compile ( '<tr><td class="text-left visitedlyr">.+?<a href="([^"]*)" target="_blank"><b>(.+?)</b></a>  by <b>(.+?)</b><br>.+?<small>(.+?)</td></tr>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for OOoOO0oo0ooO , O0o0O00Oo0o0 , O00O0oOO00O00 , o0OOoo0OO0OOO in O0OOO0OOoO0O :
  Oo000 ( '[COLORsteelblue]' + O0o0O00Oo0o0 + ' - ' + O00O0oOO00O00 + '[/COLOR]' , OOoOO0oo0ooO , 24 , i1iiIIiiI111 + 'lyrics.png' , OoOo00o , '[COLORsteelblue]' + O0o0O00Oo0o0 + ' - ' + O00O0oOO00O00 + '[/COLOR]' + '[CR][CR]' + ( '[COLORorangered]' + ( o0OOoo0OO0OOO ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) + '[/COLOR]' ) )
  if 11 - 11: o0 . I1ii11iIi11i
  xbmcplugin . setContent ( O0OoO000O0OO , 'movies' )
  if 92 - 92: o0O0 . OO0oo0oOO
def i1i ( url ) :
 iI1iI1I1i1I = iIi11Ii1 ( url )
 Ii11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for url , iiI111I1iIiI , o0OOoo0OO0OOO , OoOo00o , Oo0O0O0ooO0O in Ii11iII1 :
  if '.php' in url :
   Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 211 , iiI111I1iIiI , OoOo00o , o0OOoo0OO0OOO )
  else :
   Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 212 , iiI111I1iIiI , OoOo00o , o0OOoo0OO0OOO )
def IIIi1I1IIii1II ( url ) :
 iI1iI1I1i1I = iIi11Ii1 ( url )
 Ii11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for url , iiI111I1iIiI , o0OOoo0OO0OOO , OoOo00o , Oo0O0O0ooO0O in Ii11iII1 :
  if '.php' in url :
   Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 211 , iiI111I1iIiI , OoOo00o , o0OOoo0OO0OOO )
  else :
   Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 212 , iiI111I1iIiI , OoOo00o , o0OOoo0OO0OOO )
def O0ii1ii1ii ( url , description ) :
 o0OOoo0OO0OOO = description
 oooooOoo0ooo = oOOoO0 . open ( url ) . read ( )
 if 6 - 6: o0o0OOO0o0 - IIII + iIii1I11I1II1 - OO0oo0oOO - i11iIiiIii
 try :
  OO0oOO0O = re . findall ( r'<a .*?>(.*?)</a>' , oooooOoo0ooo )
  oOiIi1IIIi1 = re . findall ( r'<a.*?href="(.*?)">' , oooooOoo0ooo )
  if 86 - 86: o0o0OOO0o0 % OoOoOO00 / I1IiiI / OoOoOO00
  for iIIi1i1 in oOiIi1IIIi1 :
   if '.db' in iIIi1i1 :
    pass
   elif 'cover/' in iIIi1i1 :
    pass
   elif '.cue' in iIIi1i1 :
    pass
   elif '.log' in iIIi1i1 :
    pass
   elif '.accurip' in iIIi1i1 :
    pass
   elif '.gif' in iIIi1i1 :
    pass
   elif '.srt' in iIIi1i1 :
    pass
   elif '..' in iIIi1i1 :
    pass
   elif '.txt' in iIIi1i1 :
    pass
   elif '.nfo' in iIIi1i1 :
    pass
   elif '.jpg' in iIIi1i1 :
    pass
   elif '1-Irani/' in iIIi1i1 :
    pass
   elif 'index.php' in iIIi1i1 :
    pass
   elif '.png' in iIIi1i1 :
    pass
   elif '?C=M&O=D' in iIIi1i1 :
    pass
   elif '?C=M&O=A' in iIIi1i1 :
    pass
   elif '?C=N&O=D' in iIIi1i1 :
    pass
   elif '?C=N&O=A' in iIIi1i1 :
    pass
   elif '?C=S&O=A' in iIIi1i1 :
    pass
   elif '?C=S&O=D' in iIIi1i1 :
    pass
   elif '?C=N;O=D' in iIIi1i1 :
    pass
   elif '?C=M;O=A' in iIIi1i1 :
    pass
   elif '?C=S;O=A' in iIIi1i1 :
    pass
   elif '?C=D;O=A' in iIIi1i1 :
    pass
   elif 'Torrent' in iIIi1i1 :
    pass
   elif 'exe' in iIIi1i1 :
    pass
   elif 'public' in iIIi1i1 :
    pass
   elif '?C=D;O=A' in iIIi1i1 :
    pass
   elif 'pub' in iIIi1i1 :
    pass
   elif 'install' in iIIi1i1 :
    pass
   elif '?C=D;O=A' in iIIi1i1 :
    pass
   elif '?C=D;O=A' in iIIi1i1 :
    pass
   elif '.m3u' in iIIi1i1 :
    pass
   elif '?C=D;O=A' in iIIi1i1 :
    pass
   elif 'mpeg' in iIIi1i1 :
    pass
   elif '.doc' in iIIi1i1 :
    pass
   elif '.html' in iIIi1i1 :
    pass
   elif 'boss' in iIIi1i1 :
    pass
   elif 'quicksilver' in iIIi1i1 :
    pass
   else :
    iiI111I1iIiI = ( iIIi1i1 ) . replace ( '/' , '' )
    Oo0O0O0ooO0O = iIIi1i1
    if 'txt' in Oo0O0O0ooO0O :
     pass
    if '.avi' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( 'avi' , '' )
    if '.' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( '.' , ' ' )
    if '_' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( '_' , ' ' )
    if '%20' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( '%20' , ' ' )
    if '/' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( '/' , '' )
    if 'mkv' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( 'mkv' , '' )
    if 'mp4' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( 'mp4' , '' )
    if 'Tehmovies' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( 'Tehmovies' , '' )
    if 'flac' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( 'flac' , '' )
    if '&amp;' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( '&amp;' , '&' )
    if 'mp3' in Oo0O0O0ooO0O :
     Oo0O0O0ooO0O = Oo0O0O0ooO0O . replace ( 'mp3' , '' )
     if 10 - 10: o0o0OOO0o0
     if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / IIIIII11i1I + IIII
    if '.mkv' in iIIi1i1 or '.MP3' in iIIi1i1 or '.wma' in iIIi1i1 or '.m4a' in iIIi1i1 or '.m4a' in iIIi1i1 or '.m4B' in iIIi1i1 or '.m4a' in iIIi1i1 or '.m4v' in iIIi1i1 or '.mp3' in iIIi1i1 or '.mp4' in iIIi1i1 or '.avi' in iIIi1i1 or '.flv' in iIIi1i1 or '.mpeg' in iIIi1i1 or '.3gp' in iIIi1i1 or '.divx' in iIIi1i1 or '.flac' in iIIi1i1 or '.strm' in iIIi1i1 :
     Oo000 ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' , url + iIIi1i1 , 15 , url + 'cunt.png' , url + 'cunt.png' , Oo0O0O0ooO0O + '[CR][CR]' + o0OOoo0OO0OOO )
     if 87 - 87: i1I1i1Ii11 * I1ii11iIi11i + IIIIII11i1I / iIii1I11I1II1 / o0O0
    else :
     Oo0O0OOOoo ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' , url + iIIi1i1 , 212 , url + iiI111I1iIiI + '.png' , url + iiI111I1iIiI + '.png' , Oo0O0O0ooO0O + '[CR][CR]' + o0OOoo0OO0OOO )
     if 37 - 37: o0O0 - I1iii * i1I1i1Ii11 % i11iIiiIii - OO0oo0oOO
     if 83 - 83: o0o0OOO0o0 / I1IiiI
     if 34 - 34: o0
     if 57 - 57: i1I1i1Ii11 . o0o0OOO0o0 . i1IIi
 except Exception , i11Iii :
  print str ( i11Iii )
 xbmcplugin . addSortMethod ( O0OoO000O0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIIIi1iIi ( ) :
 ooOOoooooo = xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 ) )
 if not os . path . exists ( Oo0o0000o0o0 ) :
  II11iiii1Ii . ok ( '[COLOR=white]Genie Music[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
def II1I ( url ) :
 if O0oo0OO0 . getSetting ( 'down' ) == 'true' :
  O0i1II1Iiii1I11 ( url , Oo0O0O0ooO0O )
 else :
  IIIIiiIiI ( url )
def O0i1II1Iiii1I11 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  o00oooO0Oo = '.mp4'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.flac' in url :
  o00oooO0Oo = '.flac'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.strm' in url :
  o00oooO0Oo = '.strm'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.M4v' in url :
  o00oooO0Oo = '.M4v'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.MP3' in url :
  o00oooO0Oo = '.MP3'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.wma' in url :
  o00oooO0Oo = '.wma'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.m4B' in url :
  o00oooO0Oo = '.m4B'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.m4a' in url :
  o00oooO0Oo = '.m4a'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.mkv' in url :
  o00oooO0Oo = '.mkv'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.mp3' in url :
  o00oooO0Oo = '.mp3'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.avi' in url :
  o00oooO0Oo = '.avi'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.mov' in url :
  o00oooO0Oo = '.mov'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.mpeg' in url :
  o00oooO0Oo = '.mpeg'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.mpg' in url :
  o00oooO0Oo = '.mpg'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.flv' in url :
  o00oooO0Oo = '.flv'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 elif '.wmv' in url :
  o00oooO0Oo = '.wmv'
  o0O0OOO0Ooo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + o00oooO0Oo + '[/COLOR]' , o0O0OOO0Ooo )
  if iiIiI == 0 :
   IIIIiiIiI ( url )
  if iiIiI == 1 :
   I1 ( url , name , o00oooO0Oo )
 else :
  IIIIiiIiI ( url )
def I1 ( url , name , cat ) :
 IiIIIi1iIi ( )
 ooOOoooooo = xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Item Is Downloading" , "And Will Be Available In Just A Moment" , '' , 'http://GenieTv.co.uk' )
 OOO00O0O = os . path . join ( ooOOoooooo , file )
 try :
  os . remove ( OOO00O0O )
 except :
  pass
 downloader . download ( url , OOO00O0O , o0oO0 )
 II11iiii1Ii = xbmcgui . Dialog ( )
 II11iiii1Ii . ok ( "Genie Music" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 33 - 33: O0 . o0 . I1IiiI
def OoOO ( ) :
 o0O0OOO0Ooo = [ '[COLORsteelblue]Songs[/COLOR]' , '[COLORsteelblue]Albums[/COLOR]' , '[COLORsteelblue]Music Videos[/COLOR]' , '[COLORsteelblue]Lyrics[/COLOR]' ]
 iiIiI = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]CATEGORIES[/COLOR]' , o0O0OOO0Ooo )
 if iiIiI == 0 :
  ooOOO0 ( oO0o0o0ooO0oO + '/songs.php' )
 if iiIiI == 1 :
  ooOOO0 ( oO0o0o0ooO0oO + '/albums.php' )
 if iiIiI == 2 :
  o0o ( oO0o0o0ooO0oO + '/gmv.php' )
 if iiIiI == 3 :
  Oo0oOOo ( )
  if 73 - 73: o0 * I1ii11iIi11i + I1IiiI . I1iii
def ooOOO0 ( url ) :
 Oo0OoO00oOO0o = II11iiii1Ii . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oO00000 = Oo0OoO00oOO0o . lower ( )
 iI1iI1I1i1I = iIi11Ii1 ( url )
 o0oO0 . create ( "[COLORsteelblue]Genie Music[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
 O0OOO0OOoO0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for url , iiI111I1iIiI , o0OOoo0OO0OOO , OOOOoo0Oo , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  if o0oO00000 in Oo0O0O0ooO0O . lower ( ) :
   o0oO0 . update ( 20 , "" , "Watch Close" )
   Oo0O0O0ooO0O = ( Oo0O0O0ooO0O . replace ( '%20' , ' ' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
   o0oO0 . update ( 40 , "" , "Matching Up" )
   if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
    o0oO0 . update ( 60 , "" , "Adding A Few Songs There" )
    Oo000 ( ( '[COLORsteelblue]' + ( Oo0O0O0ooO0O ) . replace ( '/' , '' ) + '[/COLOR]' ) , url , 15 , iiI111I1iIiI , OoOo00o , ( '[COLORsteelblue]' + ( Oo0O0O0ooO0O ) . replace ( '/' , '' ) + '[CR][CR]Song[/COLOR]' ) )
   else :
    o0oO0 . update ( 80 , "" , "Oooooh An Album" )
    Oo0O0OOOoo ( ( '[COLORsteelblue]' + ( Oo0O0O0ooO0O ) . replace ( '/' , '' ) + '[/COLOR]' ) , url , 212 , iiI111I1iIiI , OoOo00o , ( '[COLORsteelblue]' + ( Oo0O0O0ooO0O ) . replace ( '/' , '' ) + '[CR][CR]Folder[/COLOR]' ) )
    o0oO0 . update ( 100 , "" , "Get In" )
    if 14 - 14: o0O0
    I1iI1iIi111i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O0OoO000O0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
if 44 - 44: i1IIi % II111iiii + o0o0OOO0o0
if 45 - 45: o0O0 / o0O0 + OO0oo0oOO + I1iii
def iI111i ( ) :
 if 26 - 26: I1ii11iIi11i * o0O0 . II111iiii * IIII
 if 28 - 28: OoO0O00 . i1IIi * I1IiiI + O0 . i1IIi - I1iii
 if 38 - 38: OO0oo0oOO
 if 84 - 84: iIii1I11I1II1 % o0O0 / iIii1I11I1II1 % o0o0OOO0o0
 if 45 - 45: O0
 if 26 - 26: o0o0OOO0o0 - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
 if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / i1I1i1Ii11 + i1IIi
 if 42 - 42: I1iii . o0oOOo0O0Ooo . I1iii - I1ii11iIi11i
 if 40 - 40: I1iii - i11iIiiIii / IIII
 if 35 - 35: IIII - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % IIII
 if 47 - 47: o0O0 - IIII . II111iiii + OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * IIII / Oo0Ooo / IIII
 if 87 - 87: Oo0Ooo . o0
 if 75 - 75: I1iii + OoOoOO00 + o0oOOo0O0Ooo * o0o0OOO0o0 % i1I1i1Ii11 . o0O0
 if 55 - 55: IIIIII11i1I . I1IiiI
 if 61 - 61: Oo0Ooo % o0 . Oo0Ooo
 if 100 - 100: OO0oo0oOO * O0
 if 64 - 64: IIIIII11i1I % iIii1I11I1II1 * i1I1i1Ii11
 if 79 - 79: O0
 if 78 - 78: I1ii11iIi11i + IIIIII11i1I - OO0oo0oOO
 if 38 - 38: o0oOOo0O0Ooo - i1I1i1Ii11 + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 if 57 - 57: OoO0O00 / I1iii
 if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * IIIIII11i1I . I1IiiI * I1IiiI
 if 7 - 7: o0 * OO0oo0oOO % IIII - o0oOOo0O0Ooo
 if 13 - 13: IIII . i11iIiiIii
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 if 100 - 100: IIII - O0 % i1I1i1Ii11 * IIIIII11i1I + I1IiiI
 if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 if 33 - 33: OO0oo0oOO + o0O0 * i1I1i1Ii11 / iIii1I11I1II1 - I1IiiI
 if 54 - 54: OO0oo0oOO / IIIIII11i1I . i1I1i1Ii11 % o0O0
 Oo = ( oO0o0o0ooO0oO ) . replace ( '/geniemusic' , '/quicksilver/Other/Music' )
 O0OOOOo0O = iIi11Ii1 ( oO0o0o0ooO0oO + '/gmv.php' )
 iI1iI1I1i1I = iIi11Ii1 ( Oo )
 OooOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' , re . DOTALL ) . findall ( O0OOOOo0O )
 O0OOO0OOoO0O = re . compile ( '<a.*?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for OOoOO0oo0ooO , Oo0O0O0ooO0O in OooOO :
  I1111 = iIi11Ii1 ( OOoOO0oo0ooO )
  iiIiiiiI = re . compile ( '<a href="([^"]*)">(.*?)</a>' , re . DOTALL ) . findall ( I1111 )
  for oooOo0OOOoo0 , O00O0oOO00O00 in iiIiiiiI :
   O00O0oOO00O00 = ( O00O0oOO00O00 . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
   if '.png' in oooOo0OOOoo0 or '.jpg' in oooOo0OOOoo0 or '=' in oooOo0OOOoo0 or 'quicksilver' in oooOo0OOOoo0 or '&' in oooOo0OOOoo0 or '.jpeg' in oooOo0OOOoo0 or "'" in oooOo0OOOoo0 :
    pass
   elif '.mkv' in oooOo0OOOoo0 or '.MP3' in oooOo0OOOoo0 or '.m4a' in oooOo0OOOoo0 or '.m4B' in oooOo0OOOoo0 or '.m4a' in oooOo0OOOoo0 or '.m4v' in oooOo0OOOoo0 or '.mp3' in oooOo0OOOoo0 or '.mp4' in oooOo0OOOoo0 or '.avi' in oooOo0OOOoo0 or '.flv' in oooOo0OOOoo0 or '.mpeg' in oooOo0OOOoo0 or '.3gp' in oooOo0OOOoo0 or '.divx' in oooOo0OOOoo0 or '.flac' in oooOo0OOOoo0 or '.strm' in oooOo0OOOoo0 :
    OOoO ( ( '[COLORsteelblue]' + O00O0oOO00O00 + ' -[COLORgold] source ' + Oo0O0O0ooO0O + '[/COLOR]' ) , OOoOO0oo0ooO + oooOo0OOOoo0 , 15 , i1iiIIiiI111 + 'music12' , oO , '[COLORsteelblue]' + O00O0oOO00O00 + ' - [COLORgold]Source Home[/COLOR]' )
    o0oO0 . create ( "[COLORsteelblue]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 50 , "" , "Getting Video Links" )
 for OOoOO0oo0ooO , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  Oo0O0O0ooO0O = ( Oo0O0O0ooO0O . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
  if '.png' in OOoOO0oo0ooO or '=' in OOoOO0oo0ooO or '.jpg' in OOoOO0oo0ooO or '=' in OOoOO0oo0ooO or 'quicksilver' in OOoOO0oo0ooO or '&' in OOoOO0oo0ooO or '.jpeg' in OOoOO0oo0ooO or "'" in OOoOO0oo0ooO :
   pass
  elif '.mkv' in OOoOO0oo0ooO or '.MP3' in OOoOO0oo0ooO or '.m4a' in OOoOO0oo0ooO or '.m4B' in OOoOO0oo0ooO or '.m4a' in OOoOO0oo0ooO or '.m4v' in OOoOO0oo0ooO or '.mp3' in OOoOO0oo0ooO or '.mp4' in OOoOO0oo0ooO or '.avi' in OOoOO0oo0ooO or '.flv' in OOoOO0oo0ooO or '.mpeg' in OOoOO0oo0ooO or '.3gp' in OOoOO0oo0ooO or '.divx' in OOoOO0oo0ooO or '.flac' in OOoOO0oo0ooO or '.strm' in OOoOO0oo0ooO :
   OOoO ( ( '[COLORsteelblue]' + Oo0O0O0ooO0O + ' -[COLORgold] source Home2[/COLOR]' ) , Oo + OOoOO0oo0ooO , 15 , i1iiIIiiI111 + 'music12' , oO , '[COLORsteelblue]' + Oo0O0O0ooO0O + ' - [COLORgold]Source Home[/COLOR]' )
   o0oO0 . create ( "[COLORsteelblue]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 50 , "" , "Getting Video Links" )
  else :
   Oo0O0OOOoo ( '[COLORsteelblue]' + Oo0O0O0ooO0O + ' - [COLORgold]Source Home[/COLOR]' , Oo + '/' + OOoOO0oo0ooO , 212 , i1iiIIiiI111 + 'music12' , oO , '[COLORsteelblue]' + Oo0O0O0ooO0O + ' - [COLORgold]Source Home[/COLOR]' )
   if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * o0o0OOO0o0 * IIII
   I1iI1iIi111i ( 'tvshows' , 'Media Info 3' )
   xbmcplugin . addSortMethod ( O0OoO000O0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o ( url ) :
 Oo0OoO00oOO0o = II11iiii1Ii . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oO00000 = Oo0OoO00oOO0o . lower ( )
 O0OOOOo0O = iIi11Ii1 ( url )
 OooOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' , re . DOTALL ) . findall ( O0OOOOo0O )
 for url , Oo0O0O0ooO0O in OooOO :
  I1111 = iIi11Ii1 ( url )
  iiIiiiiI = re . compile ( '<a href="([^"]*)">(.*?)</a>' , re . DOTALL ) . findall ( I1111 )
  for oooOo0OOOoo0 , O00O0oOO00O00 in iiIiiiiI :
   if o0oO00000 in O00O0oOO00O00 . lower ( ) :
    O00O0oOO00O00 = ( O00O0oOO00O00 . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
    if '.png' in oooOo0OOOoo0 or '.jpg' in oooOo0OOOoo0 or '=' in oooOo0OOOoo0 or 'quicksilver' in oooOo0OOOoo0 or '&' in oooOo0OOOoo0 or '.jpeg' in oooOo0OOOoo0 or "'" in oooOo0OOOoo0 :
     pass
    elif '.mkv' in oooOo0OOOoo0 or '.MP3' in oooOo0OOOoo0 or '.m4a' in oooOo0OOOoo0 or '.m4B' in oooOo0OOOoo0 or '.m4a' in oooOo0OOOoo0 or '.m4v' in oooOo0OOOoo0 or '.mp3' in oooOo0OOOoo0 or '.mp4' in oooOo0OOOoo0 or '.avi' in oooOo0OOOoo0 or '.flv' in oooOo0OOOoo0 or '.mpeg' in oooOo0OOOoo0 or '.3gp' in oooOo0OOOoo0 or '.divx' in oooOo0OOOoo0 or '.flac' in oooOo0OOOoo0 or '.strm' in oooOo0OOOoo0 :
     OOoO ( ( '[COLORsteelblue]' + O00O0oOO00O00 + ' -[COLORgold] source ' + Oo0O0O0ooO0O + '[/COLOR]' ) , url + oooOo0OOOoo0 , 15 , i1iiIIiiI111 + 'music12' , oO , '' )
     o0oO0 . create ( "[COLORsteelblue]Genie Music[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 50 , "" , "Getting Video Links" )
     if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
     I1iI1iIi111i ( 'tvshows' , 'Media Info 3' )
  xbmcplugin . addSortMethod ( O0OoO000O0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: IIIIII11i1I * iIii1I11I1II1
def oO00oOOoooO ( ) :
 IiIi11iI = requests . get ( 'http://www.djing.com/' ) . content
 Oo0O00O000 = re . compile ( '<img class="thumb" src="([^"]*)" alt=.+?<source src="([^"]*)"></video><h3>(.+?)</h3><p>(.+?)/p>' , re . DOTALL ) . findall ( IiIi11iI )
 for iiI111I1iIiI , OOoOO0oo0ooO , Oo0O0O0ooO0O , o0OOoo0OO0OOO in Oo0O00O000 :
  iiI111I1iIiI = ( 'http://www.djing.com' + iiI111I1iIiI )
  Oo0O0O0ooO0O = ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' ) . replace ( '[Subscribers only]' , '' )
  o0OOoo0OO0OOO = ( '[COLORorangered]' + o0OOoo0OO0OOO + '[/COLOR]' ) . replace ( '<' , '' )
  if 'Submit' in Oo0O0O0ooO0O :
   pass
  elif '&lt;' in Oo0O0O0ooO0O :
   pass
  else :
   OOoO ( Oo0O0O0ooO0O , OOoOO0oo0ooO , 15 , iiI111I1iIiI , iiI111I1iIiI , Oo0O0O0ooO0O + '[CR][CR]' + o0OOoo0OO0OOO )
   if 3 - 3: IIII * I1ii11iIi11i % o0o0OOO0o0
 I1iI1iIi111i ( 'movies' , 'MAIN' )
 if 59 - 59: i1I1i1Ii11 - o0O0
 if 15 - 15: OO0oo0oOO . i11iIiiIii . OoooooooOO / OoO0O00 % IIII
def OooooOOoo0 ( url ) :
 iI1iI1I1i1I = iIi11Ii1 ( url )
 O0OOO0OOoO0O = re . compile ( '<title>(.+?)</title>.+?<sportsdevil>(.+?)' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for Oo0O0O0ooO0O , url in O0OOO0OOoO0O :
  i1I1IiiIi1i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
  OOoO ( Oo0O0O0ooO0O , i1I1IiiIi1i , 15 , oO , '' , '' )
  I1iI1iIi111i ( 'tvshows' , 'Media Info 3' )
  if 29 - 29: I1IiiI % I1IiiI
def Oo0O0 ( url ) :
 iI1iI1I1i1I = iIi11Ii1 ( url )
 O0OOO0OOoO0O = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 Ooo0OOoOoO0 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 Oo0O00O000 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 oOo0OOoO0 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 IIo0Oo0oO0oOO00 = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 oo00OO0000oO = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 I1II1 = re . compile ( '<name>(.+?)</name>.+?<externallink>(.+?)</externallink>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 oooO = re . compile ( '<title>(.+?)</title>.+?<sportsdevil>(.+?)' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for Oo0O0O0ooO0O , iiI111I1iIiI , url , i1I1i111Ii in Ooo0OOoOoO0 :
  Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 90037 , iiI111I1iIiI , i1I1i111Ii , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , iiI111I1iIiI , url , i1I1i111Ii in O0OOO0OOoO0O :
  Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 90037 , iiI111I1iIiI , i1I1i111Ii , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , url , iiI111I1iIiI , i1I1i111Ii in Oo0O00O000 :
  OOoO ( Oo0O0O0ooO0O , url , 15 , iiI111I1iIiI , i1I1i111Ii , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , url , iiI111I1iIiI , i1I1i111Ii in oOo0OOoO0 :
  OOoO ( Oo0O0O0ooO0O , url , 15 , iiI111I1iIiI , i1I1i111Ii , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , url , iiI111I1iIiI , i1I1i111Ii in IIo0Oo0oO0oOO00 :
  OOoO ( Oo0O0O0ooO0O , url , 15 , iiI111I1iIiI , i1I1i111Ii , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , url , iiI111I1iIiI in oo00OO0000oO :
  OOoO ( Oo0O0O0ooO0O , url , 15 , iiI111I1iIiI , iiI111I1iIiI , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , url , iiI111I1iIiI , OoOo00o in I1II1 :
  Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 90037 , iiI111I1iIiI , iiI111I1iIiI , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , url , iiI111I1iIiI , OoOo00o in I1II1 :
  OOoO ( Oo0O0O0ooO0O , url , 15 , iiI111I1iIiI , iiI111I1iIiI , Oo0O0O0ooO0O )
  I1iI1iIi111i ( 'tvshows' , 'Media Info 3' )
def ooo ( url ) :
 iI1iI1I1i1I = iIi11Ii1 ( url )
 O0OOO0OOoO0O = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 Oo0O00O000 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for Oo0O0O0ooO0O , iiI111I1iIiI , url , i1I1i111Ii in O0OOO0OOoO0O :
  Oo0O0OOOoo ( Oo0O0O0ooO0O , url , 90037 , iiI111I1iIiI , i1I1i111Ii , Oo0O0O0ooO0O )
 for Oo0O0O0ooO0O , url , iiI111I1iIiI , i1I1i111Ii in Oo0O00O000 :
  OOoO ( Oo0O0O0ooO0O , url , 15 , iiI111I1iIiI , i1I1i111Ii , Oo0O0O0ooO0O )
  I1iI1iIi111i ( 'tvshows' , 'Media Info 3' )
  if 27 - 27: I1iii % I1IiiI
  if 73 - 73: IIIIII11i1I
def ooO ( name , url , mode , iconimage , description = "" , isFolder = True , background = None ) :
 Ooo0oOooo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 if 61 - 61: OoOoOO00 - IIIIII11i1I - i1IIi
 IiI1iIiIIIii = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 IiI1iIiIIIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 if background :
  IiI1iIiIIIii . setProperty ( 'fanart_image' , background )
 if mode == 1 or mode == 2 :
  IiI1iIiIIIii . addContextMenuItems ( items = [ ( '{0}' . format ( OOooO0OOoo ( 10008 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=22)' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) ) ) ] )
 elif mode == 404 :
  IiI1iIiIIIii . setProperty ( 'IsPlayable' , 'true' )
  IiI1iIiIIIii . addContextMenuItems ( items = [ ( '{0}' . format ( OOooO0OOoo ( 10009 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
 elif mode == 556 :
  IiI1iIiIIIii . setProperty ( 'IsPlayable' , 'true' )
  IiI1iIiIIIii . addContextMenuItems ( items = [ ( '{0}' . format ( OOooO0OOoo ( 10010 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
  if 53 - 53: i1IIi
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0oOooo0 , listitem = IiI1iIiIIIii , isFolder = isFolder )
 if 59 - 59: o0oOOo0O0Ooo
def oOoO00O0 ( handle , url , listitem , isFolder ) :
 if 75 - 75: I1IiiI . I1iii . O0 * OO0oo0oOO
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 4 - 4: IIII % i1I1i1Ii11 * OoO0O00
def o0O0OOOOoOO0 ( url ) :
 ii = iIi11Ii1 ( url )
 O0OOO0OOoO0O = re . compile ( '<img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+?rel=".+? >(.+?)</a>&#32' , re . DOTALL ) . findall ( ii )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( ii )
 for iiI111I1iIiI , url , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  if 'share' in url :
   O0oOo00o ( ( '[COLORorangered]' + Oo0O0O0ooO0O + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 70511 , 'http:' + iiI111I1iIiI )
  elif 'watch?v=' in url :
   O0oOo00o ( ( '[COLORpurple]' + Oo0O0O0ooO0O + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iiI111I1iIiI )
  elif 'youtu' in url :
   O0oOo00o ( ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) , 7052 , 'http:' + iiI111I1iIiI )
 for url in next :
  o0ooooO0o0O ( '[COLORsteelblue]NEXT[/COLOR]' , url , 7050 , i1iiIIiiI111 + 'Next.png' )
  if 24 - 24: O0 * o0oOOo0O0Ooo
def IiI1iiiIii ( url ) :
 ii = iIi11Ii1 ( url )
 O0OOO0OOoO0O = re . compile ( '"shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( ii )
 for url in O0OOO0OOoO0O :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
def I1III1111iIi ( url ) :
 ii = iIi11Ii1 ( url )
 Oo0O00O000 = re . compile ( '"shortUrl":"([^"]*)"' , re . DOTALL ) . findall ( ii )
 for url in Oo0O00O000 :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 38 - 38: o0O0 + o0o0OOO0o0 / OO0oo0oOO % I1iii - I1ii11iIi11i
  if 14 - 14: i1I1i1Ii11 / OO0oo0oOO
def ooo0O0o00O ( ) :
 o0ooooO0o0O ( ( '[COLORsteelblue]GENRE[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , i1iiIIiiI111 + 'RadioNomy.png' )
 o0ooooO0o0O ( ( '[COLORsteelblue]SORT BY[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , i1iiIIiiI111 + 'RadioNomy.png' )
 o0ooooO0o0O ( ( '[COLORsteelblue]SEARCH[/COLOR]' ) , '' , 70006 , i1iiIIiiI111 + 'RadioNomy.png' )
 if 48 - 48: I1iii / OO0oo0oOO . iIii1I11I1II1 * OoOoOO00 * i1I1i1Ii11 / i1IIi
def OOOOoOOo0O0 ( url ) :
 ii = OPEN_CAT ( url )
 O0OOO0OOoO0O = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( ii )
 for url , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  o0ooooO0o0O ( ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i1iiIIiiI111 + 'RadioNomy.png' )
def oOooo0 ( url ) :
 ii = OPEN_CAT ( url )
 O0OOO0OOoO0O = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( ii )
 for url , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  o0ooooO0o0O ( ( '[COLORsteelblue]' + Oo0O0O0ooO0O + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i1iiIIiiI111 + 'RadioNomy.png' )
def ooOo0o00OOo0 ( url ) :
 ii = OPEN_CAT ( url )
 O0OOO0OOoO0O = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( ii )
 Oo0O00O000 = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( ii )
 for url , Oo0O0O0ooO0O in Oo0O00O000 :
  o0ooooO0o0O ( ( '[COLORsteelblue]Filter - ' + Oo0O0O0ooO0O + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i1iiIIiiI111 + 'RadioNomy.png' )
 for url , iiI111I1iIiI , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  O0oOo00o ( ( '[COLORsteelblue]Stream - ' + Oo0O0O0ooO0O + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iiI111I1iIiI )
def I1IIii1 ( url ) :
 ii = OPEN_CAT ( url )
 O0OOO0OOoO0O = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( ii )
 for url in O0OOO0OOoO0O :
  RESOLVEtest ( url )
def OO0o0oOOO0O ( ) :
 Oo0OoO00oOO0o = II11iiii1Ii . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oO00000 = Oo0OoO00oOO0o
 iI = 'https://www.radionomy.com/en/search/index?query=' + ( Oo0OoO00oOO0o ) . replace ( ' ' , '+' )
 iI1iI1I1i1I = iIi11Ii1 ( iI )
 O0OOO0OOoO0O = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iI1iI1I1i1I )
 for OOoOO0oo0ooO , iiI111I1iIiI , Oo0O0O0ooO0O in O0OOO0OOoO0O :
  O0oOo00o ( ( '[COLORsteelblue]Stream - ' + Oo0O0O0ooO0O + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + OOoOO0oo0ooO , 70005 , iiI111I1iIiI )
  if 2 - 2: I1iii / o0O0 . o0O0 % OO0oo0oOO
  if 11 - 11: iIii1I11I1II1
  if 20 - 20: II111iiii % Oo0Ooo + I1ii11iIi11i + I1iii
  if 23 - 23: IIIIII11i1I * IIII * Oo0Ooo . O0 - i11iIiiIii
  if 18 - 18: IIII + o0 - O0
def o00O ( title , message , times = 2000 , icon = oO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def i1Ii1i1I11Iii ( ) :
 I1i1i1 = OoO0O00O0oo0O ( )
 I1IiI11 = I1i1i1 . replace ( iI1Ii11111iIi , "" )
 if os . path . exists ( I1i1i1 ) or not I1i1i1 == False :
  iI1iiiiIii = open ( I1i1i1 , mode = 'r' ) ; iIiIiIiI = iI1iiiiIii . read ( ) ; iI1iiiiIii . close ( )
  o0ooOooo000oOO ( "%s - %s" % ( oo00 , I1IiI11 ) , iIiIiIiI )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OoO0O00O0oo0O ( ) :
 i11OOoo = False
 if os . path . exists ( os . path . join ( iI1Ii11111iIi , 'xbmc.log' ) ) :
  i11OOoo = os . path . join ( iI1Ii11111iIi , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( iI1Ii11111iIi , 'kodi.log' ) ) :
  i11OOoo = os . path . join ( iI1Ii11111iIi , 'kodi.log' )
 elif os . path . exists ( os . path . join ( iI1Ii11111iIi , 'spmc.log' ) ) :
  i11OOoo = os . path . join ( iI1Ii11111iIi , 'spmc.log' )
 elif os . path . exists ( os . path . join ( iI1Ii11111iIi , 'tvmc.log' ) ) :
  i11OOoo = os . path . join ( iI1Ii11111iIi , 'tvmc.log' )
 return i11OOoo
 if 50 - 50: OoO0O00
 if 43 - 43: II111iiii . i1I1i1Ii11 / I1ii11iIi11i
 if 20 - 20: I1IiiI
 if 95 - 95: o0O0 - I1IiiI
 if 34 - 34: I1iii * I1IiiI . i1IIi * I1iii / I1iii
def o0ooOooo000oOO ( title , msg ) :
 class IIiI1Ii ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 57 - 57: IIIIII11i1I - I1iii - o0o0OOO0o0 + OoO0O00
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 30 - 30: IIII % OoOoOO00 + i1IIi - o0o0OOO0o0 - IIII
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 8 - 8: OoO0O00 + OO0oo0oOO - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * i1I1i1Ii11
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 9 - 9: Oo0Ooo - i11iIiiIii - IIIIII11i1I * IIII + I1iii
 iIIII = IIiI1Ii ( "Textbox.xml" , O0oo0OO0 . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 iIIII . doModal ( )
 del iIIII
 if 45 - 45: I1ii11iIi11i % I1IiiI - i11iIiiIii
 if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * I1IiiI
 if 46 - 46: OoOoOO00 + OoO0O00
def o0o0O ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def ooooO0oOoOOoO ( url ) :
 if url == 'http://' : return False
 try :
  I1i11i = urllib2 . Request ( url )
  I1i11i . add_header ( 'User-Agent' , I1i1iiI1 )
  oooooOoo0ooo = urllib2 . urlopen ( I1i11i )
  oooooOoo0ooo . close ( )
 except Exception , i11Iii :
  return i11Iii
 return True
 if 11 - 11: I1IiiI / II111iiii + o0oOOo0O0Ooo * I1ii11iIi11i - I1ii11iIi11i - I1IiiI
 if 85 - 85: o0o0OOO0o0 % i1I1i1Ii11 / iIii1I11I1II1 . iIii1I11I1II1
 if 31 - 31: o0oOOo0O0Ooo % OoO0O00
def iI1I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 II11iiii1Ii = xbmcgui . Dialog ( )
 II11iiii1Ii . ok ( "Genie Music" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Genie Music[/COLOR]" )
 return
 if 100 - 100: iIii1I11I1II1 + OoOoOO00 / Oo0Ooo . i11iIiiIii
def III1I1Iii1iiI ( url ) :
 print '###' + oo00 + ' - DELETING Addons20.db ###'
 ooOOoooooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 i1Iii11I1i = os . path . join ( ooOOoooooo , 'Addons20.db' )
 try :
  os . remove ( i1Iii11I1i )
  II11iiii1Ii = xbmcgui . Dialog ( )
  print '=== ' + oo00 + ' - DELETING    ' + str ( i1Iii11I1i ) + '    ==='
  II11iiii1Ii . ok ( oo00 , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  II11iiii1Ii = xbmcgui . Dialog ( )
  II11iiii1Ii . ok ( oo00 , "       No File To Remove" )
 return
 if 72 - 72: iIii1I11I1II1 * IIII % I1iii / OoO0O00
 if 35 - 35: I1iii + i1IIi % I1ii11iIi11i % o0o0OOO0o0 + i1I1i1Ii11
 if 17 - 17: i1IIi
 if 21 - 21: Oo0Ooo
 if 29 - 29: o0o0OOO0o0 / II111iiii / I1iii * IIIIII11i1I
def iIi11Ii1 ( url ) :
 I1i11i = urllib2 . Request ( url )
 I1i11i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oooooOoo0ooo = urllib2 . urlopen ( I1i11i )
 iIIi1i1 = oooooOoo0ooo . read ( )
 oooooOoo0ooo . close ( )
 return iIIi1i1
def IIiI1Ii ( heading , announce ) :
 class o0ooOooo000oOO ( ) :
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
   try : iI1iiiiIii = open ( announce ) ; I111i1i1111 = iI1iiiiIii . read ( )
   except : I111i1i1111 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I111i1i1111 ) )
   return
 o0ooOooo000oOO ( )
 o0ooOooo000oOO ( )
def IIII1 ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 I1I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1IIIiIiIi , IIIII1 , iIi1Ii1i1iI in os . walk ( I1I1i ) :
   IIiI1 = 0
   IIiI1 += len ( iIi1Ii1i1iI )
   if 17 - 17: IIIIII11i1I / IIIIII11i1I / o0o0OOO0o0
   if 1 - 1: i1IIi . i11iIiiIii % IIIIII11i1I
   if IIiI1 > 0 :
    if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % o0 / IIII . IIII
    II11iiii1Ii = xbmcgui . Dialog ( )
    if II11iiii1Ii . yesno ( "Delete Package Cache Files" , str ( IIiI1 ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: o0oOOo0O0Ooo . IIIIII11i1I . o0o0OOO0o0 + OoooooooOO - IIIIII11i1I + o0
     for iI1iiiiIii in iIi1Ii1i1iI :
      os . unlink ( os . path . join ( I1IIIiIiIi , iI1iiiiIii ) )
     for iII1iiiiIII in IIIII1 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , iII1iiiiIII ) )
     II11iiii1Ii = xbmcgui . Dialog ( )
     II11iiii1Ii . ok ( oo00 , "       Deleting Packages all done" )
    else :
     pass
   else :
    II11iiii1Ii = xbmcgui . Dialog ( )
    II11iiii1Ii . ok ( oo00 , "       No Packages to DELETE" )
 except :
  II11iiii1Ii = xbmcgui . Dialog ( )
  II11iiii1Ii . ok ( oo00 , "Error Deleting Packages please visit The Support Group, Genie Music on facebook" )
 OOoOO0oo00Oo ( url )
 return
def OOoOO0oo00Oo ( url ) :
 I111i1II = os . path . join ( i1 , 'addon_data' )
 O0ooooo0OOOO0 = [
 ( I111i1II ) ,
 ( i11 ) ,
 ( os . path . join ( o0oOoO00o , 'cache' ) ) ,
 ( os . path . join ( o0oOoO00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( i11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( i11 , 'plugin.video.GenieMusic' , 'Images' ) ) ,
 ( os . path . join ( I111i1II , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I111i1II , 'plugin.video.GenieMusic' , 'Images' ) ) ]
 if 9 - 9: II111iiii - o0oOOo0O0Ooo / o0O0 / o0oOOo0O0Ooo
 I1i111iiIIIi = 0
 if 75 - 75: o0o0OOO0o0 . OoooooooOO % o0oOOo0O0Ooo * o0o0OOO0o0 % OoooooooOO
 for I11i1 in O0ooooo0OOOO0 :
  if os . path . exists ( I11i1 ) and not I11i1 in [ i11 , I111i1II ] :
   for I1IIIiIiIi , IIIII1 , iIi1Ii1i1iI in os . walk ( I11i1 ) :
    IIiI1 = 0
    IIiI1 += len ( iIi1Ii1i1iI )
    if IIiI1 > 0 :
     for iI1iiiiIii in iIi1Ii1i1iI :
      if not iI1iiiiIii in oOOoo00O0O :
       try :
        os . unlink ( os . path . join ( I1IIIiIiIi , iI1iiiiIii ) )
       except :
        pass
      else : I1i1i1 ( 'Ignore Log File: %s' % iI1iiiiIii )
     for iII1iiiiIII in IIIII1 :
      try :
       shutil . rmtree ( os . path . join ( I1IIIiIiIi , iII1iiiiIII ) )
       I1i111iiIIIi += 1
       I1i1i1 ( "[Success] cleared %s files from %s" % ( str ( IIiI1 ) , os . path . join ( I11i1 , iII1iiiiIII ) ) )
      except :
       I1i1i1 ( "[Failed] to wipe cache in: %s" % os . path . join ( I11i1 , iII1iiiiIII ) )
  else :
   for I1IIIiIiIi , IIIII1 , iIi1Ii1i1iI in os . walk ( I11i1 ) :
    for iII1iiiiIII in IIIII1 :
     if 'cache' in iII1iiiiIII . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( I1IIIiIiIi , iII1iiiiIII ) )
       I1i111iiIIIi += 1
       I1i1i1 ( "[Success] wiped %s " % os . path . join ( I11i1 , iII1iiiiIII ) )
      except :
       I1i1i1 ( "[Failed] to wipe cache in: %s" % os . path . join ( I11i1 , iII1iiiiIII ) )
       if 28 - 28: o0o0OOO0o0
 o00O ( oo00 , 'Clear Cache: Removed %s Files' % I1i111iiIIIi )
def oOOOOoo ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 I1I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1IIIiIiIi , IIIII1 , iIi1Ii1i1iI in os . walk ( I1I1i ) :
   IIiI1 = 0
   IIiI1 += len ( iIi1Ii1i1iI )
   if 58 - 58: o0oOOo0O0Ooo / o0 . OoOoOO00 / OoooooooOO + OO0oo0oOO
   if 86 - 86: o0o0OOO0o0 * I1IiiI + o0o0OOO0o0 + II111iiii
   if IIiI1 > 0 :
    if 8 - 8: OO0oo0oOO - o0O0 / I1iii
    II11iiii1Ii = xbmcgui . Dialog ( )
    if II11iiii1Ii . yesno ( "Delete Package Cache Files" , str ( IIiI1 ) + " files found" , "Do you want to delete them?" ) :
     if 96 - 96: OoOoOO00
     for iI1iiiiIii in iIi1Ii1i1iI :
      os . unlink ( os . path . join ( I1IIIiIiIi , iI1iiiiIii ) )
     for iII1iiiiIII in IIIII1 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , iII1iiiiIII ) )
     II11iiii1Ii = xbmcgui . Dialog ( )
     II11iiii1Ii . ok ( oo00 , "       Deleting Packages all done" )
    else :
     pass
   else :
    II11iiii1Ii = xbmcgui . Dialog ( )
    II11iiii1Ii . ok ( oo00 , "       No Packages to DELETE" )
 except :
  II11iiii1Ii = xbmcgui . Dialog ( )
  II11iiii1Ii . ok ( oo00 , "Error Deleting Packages" )
 return
 if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - IIII
def IiiIiI111iI ( ) :
 II11iiii1Ii = xbmcgui . Dialog ( )
 iiIiI = II11iiii1Ii . yesno ( 'Force Close Genie Music' , 'You are about to close Genie Music' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iiIiI == 0 : return
 elif iiIiI == 1 : pass
 OOo = o0o0O ( )
 I1i1i1 ( "Platform: " + str ( OOo ) )
 os . _exit ( 1 )
 I1i1i1 ( "Force close failed!  Trying alternate methods." )
 if OOo == 'osx' :
  I1i1i1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  II11iiii1Ii . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OOo == 'linux' :
  I1i1i1 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  II11iiii1Ii . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OOo == 'android' :
  I1i1i1 ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.Genie Music' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.Genie Music' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.Genie Music());' )
  except : pass
  II11iiii1Ii . ok ( oo00 , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif OOo == 'windows' :
  I1i1i1 ( "############ try windows force close #################" )
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
  II11iiii1Ii . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  I1i1i1 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  I1i1i1 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  II11iiii1Ii . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 50 - 50: I1iii
def IIIIiiIiI ( url ) :
 import urlresolver
 try :
  o0O0O0ooo0oOO = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( o0O0O0ooo0oOO , xbmcgui . ListItem ( Oo0O0O0ooO0O ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( Oo0O0O0ooO0O ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def o0o0O ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 97 - 97: I1IiiI / o0O0
def I1i1i1 ( log ) :
 xbmc . log ( "[%s]: %s" % ( oo00 , log ) )
 if not os . path . exists ( i11 ) : os . makedirs ( i11 )
 if not os . path . exists ( i1iiIII111ii ) : iI1iiiiIii = open ( i1iiIII111ii , 'w' ) ; iI1iiiiIii . close ( )
 with open ( i1iiIII111ii , 'a' ) as iI1iiiiIii :
  Oooo0 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  iI1iiiiIii . write ( Oooo0 . rstrip ( '\r\n' ) + '\n' )
  if 59 - 59: OoooooooOO
def i1iiiii1 ( ) :
 try :
  O0iII1 = getSet ( "core-player" )
  if ( O0iII1 == 'DVDPLAYER' ) : IIII1i = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0iII1 == 'MPLAYER' ) : IIII1i = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0iII1 == 'PAPLAYER' ) : IIII1i = xbmc . PLAYER_CORE_PAPLAYER
  else : IIII1i = xbmc . PLAYER_CORE_AUTO
 except : IIII1i = xbmc . PLAYER_CORE_AUTO
 return IIII1i
 return True
 if 2 - 2: iIii1I11I1II1 * Oo0Ooo % i1I1i1Ii11 - II111iiii - o0O0
 if 3 - 3: OO0oo0oOO
def Oo0O0OOOoo ( name , url , mode , iconimage , fanart , description ) :
 if 45 - 45: OO0oo0oOO
 Ooo0oOooo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOIIi1iiii1iI = True
 IiI1iIiIIIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iIiIIIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iIiIIIii . setProperty ( "Fanart_Image" , fanart )
 oOIIi1iiii1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0oOooo0 , listitem = IiI1iIiIIIii , isFolder = True )
 return oOIIi1iiii1iI
 if 25 - 25: I1ii11iIi11i + O0
def Oo000 ( name , url , mode , iconimage , fanart , description ) :
 if 28 - 28: OoooooooOO
 Ooo0oOooo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOIIi1iiii1iI = True
 IiI1iIiIIIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iIiIIIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iIiIIIii . setProperty ( "Fanart_Image" , fanart )
 oOIIi1iiii1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0oOooo0 , listitem = IiI1iIiIIIii , isFolder = False )
 return oOIIi1iiii1iI
def OOoO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ooo0oOooo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOIIi1iiii1iI = True
 IiI1iIiIIIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iIiIIIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iIiIIIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0000OOO0 = [ ]
  if showcontext == 'fav' :
   O0000OOO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OO0o :
   O0000OOO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IiI1iIiIIIii . addContextMenuItems ( O0000OOO0 )
 oOIIi1iiii1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0oOooo0 , listitem = IiI1iIiIIIii , isFolder = False )
 return oOIIi1iiii1iI
 if 51 - 51: I1IiiI / o0 / IIII
def o0ooooO0o0O ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooo0oOooo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOIIi1iiii1iI = True
 IiI1iIiIIIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iIiIIIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0000OOO0 = [ ]
  O0000OOO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0000OOO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OO0o :
   O0000OOO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiI1iIiIIIii . addContextMenuItems ( O0000OOO0 )
 oOIIi1iiii1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0oOooo0 , listitem = IiI1iIiIIIii , isFolder = True )
 return oOIIi1iiii1iI
def O0oOo00o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooo0oOooo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOIIi1iiii1iI = True
 IiI1iIiIIIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iIiIIIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0000OOO0 = [ ]
  O0000OOO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0000OOO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OO0o :
   O0000OOO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiI1iIiIIIii . addContextMenuItems ( O0000OOO0 )
 oOIIi1iiii1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0oOooo0 , listitem = IiI1iIiIIIii , isFolder = False )
 return oOIIi1iiii1iI
 if 6 - 6: IIII - I1iii * IIIIII11i1I . o0O0 / O0 * I1iii
def II11iI111i1 ( ) :
 Oo00OoOo = [ ]
 ii1ii111 = sys . argv [ 2 ]
 if len ( ii1ii111 ) >= 2 :
  i11111I1I = sys . argv [ 2 ]
  ii1 = i11111I1I . replace ( '?' , '' )
  if ( i11111I1I [ len ( i11111I1I ) - 1 ] == '/' ) :
   i11111I1I = i11111I1I [ 0 : len ( i11111I1I ) - 2 ]
  Oo0000oOo = ii1 . split ( '&' )
  Oo00OoOo = { }
  for I11o0oO00oO0o0o0 in range ( len ( Oo0000oOo ) ) :
   I1I = { }
   I1I = Oo0000oOo [ I11o0oO00oO0o0o0 ] . split ( '=' )
   if ( len ( I1I ) ) == 2 :
    Oo00OoOo [ I1I [ 0 ] ] = I1I [ 1 ]
    if 89 - 89: i1IIi / II111iiii . iIii1I11I1II1
 return Oo00OoOo
 if 1 - 1: I1iii % OoOoOO00 * Oo0Ooo
 if 55 - 55: OoOoOO00
i11111I1I = II11iI111i1 ( )
OOoOO0oo0ooO = None
Oo0O0O0ooO0O = None
Ooo0oo0ooO = None
OoOOOo0o0ooo = None
OoOo00o = None
I1iiiiI1iI = None
iIiiiii1i = None
if 40 - 40: O0 - OoooooooOO - o0
if 37 - 37: OoOoOO00 / II111iiii / O0
try :
 iIiiiii1i = int ( i11111I1I [ "fav_mode" ] )
except :
 pass
 if 76 - 76: I1IiiI . I1iii - I1ii11iIi11i - o0O0 * OoO0O00
try :
 OOoOO0oo0ooO = urllib . unquote_plus ( i11111I1I [ "url" ] )
except :
 pass
try :
 Oo0O0O0ooO0O = urllib . unquote_plus ( i11111I1I [ "name" ] )
except :
 pass
try :
 OoOOOo0o0ooo = urllib . unquote_plus ( i11111I1I [ "iconimage" ] )
except :
 pass
try :
 Ooo0oo0ooO = int ( i11111I1I [ "mode" ] )
except :
 pass
try :
 OoOo00o = urllib . unquote_plus ( i11111I1I [ "fanart" ] )
except :
 pass
try :
 I1iiiiI1iI = urllib . unquote_plus ( i11111I1I [ "description" ] )
except :
 pass
 if 54 - 54: o0 + O0 + o0o0OOO0o0 * OO0oo0oOO - IIIIII11i1I % i1I1i1Ii11
 if 13 - 13: I1iii / o0O0 * OoO0O00 . OoO0O00 * I1iii
print str ( Oo0oO0ooo ) + ': ' + str ( iIiiiI )
print "Mode: " + str ( Ooo0oo0ooO )
print "URL: " + str ( OOoOO0oo0ooO )
print "Name: " + str ( Oo0O0O0ooO0O )
print "IconImage: " + str ( OoOOOo0o0ooo )
if 63 - 63: OO0oo0oOO / O0 * Oo0Ooo + II111iiii / o0 + IIII
if 63 - 63: OoO0O00 + I1ii11iIi11i . OO0oo0oOO % OO0oo0oOO
def I1iI1iIi111i ( content , viewType ) :
 if 57 - 57: II111iiii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 54 - 54: Oo0Ooo + i1I1i1Ii11 + i11iIiiIii
  if 28 - 28: i1I1i1Ii11
if Ooo0oo0ooO == None : iiIi ( )
elif Ooo0oo0ooO == 1000 : OooooOOoo0 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 1 : Genres ( )
elif Ooo0oo0ooO == 2 : Lists ( OOoOO0oo0ooO , OoOOOo0o0ooo )
elif Ooo0oo0ooO == 3 : all_mov ( )
elif Ooo0oo0ooO == 5 : I1II1III11iii ( )
elif Ooo0oo0ooO == 6 : oOOOOoo ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 7 : OOoOO0oo00Oo ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 8 : IiiIiI111iI ( )
elif Ooo0oo0ooO == 9 : ooOOO0 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 10 : Search2 ( )
elif Ooo0oo0ooO == 11 : iI111i ( )
elif Ooo0oo0ooO == 12 : o0o ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 13 : oO00oOOoooO ( )
elif Ooo0oo0ooO == 14 : DJing2 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 15 : II1I ( OOoOO0oo0ooO )
if 70 - 70: o0
elif Ooo0oo0ooO == 16 : OoOO ( )
elif Ooo0oo0ooO == 222 : IIIIiiIiI ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 18 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
elif Ooo0oo0ooO == 20 : Oo0oOOo ( )
elif Ooo0oo0ooO == 21 : II111ii1II1i ( OOoOO0oo0ooO , I1iiiiI1iI )
elif Ooo0oo0ooO == 22 : IIIIii ( OOoOO0oo0ooO , I1iiiiI1iI )
elif Ooo0oo0ooO == 23 : O0o0 ( OOoOO0oo0ooO , I1iiiiI1iI )
elif Ooo0oo0ooO == 24 : OoO0O00IIiII ( OOoOO0oo0ooO , I1iiiiI1iI )
elif Ooo0oo0ooO == 50000 : i1Ii1i1I11Iii ( )
elif Ooo0oo0ooO == 50001 : iI1I ( )
elif Ooo0oo0ooO == 50002 : III1I1Iii1iiI ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 210 : i1i ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 212 : O0ii1ii1ii ( OOoOO0oo0ooO , I1iiiiI1iI )
elif Ooo0oo0ooO == 211 : IIIi1I1IIii1II ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 8043 : yt . PlayVideo ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 7050 : o0O0OOOOoOO0 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 7051 : IiI1iiiIii ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 7052 : yt . PlayVideo ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 70511 : I1III1111iIi ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 70001 : ooo0O0o00O ( )
elif Ooo0oo0ooO == 70002 : OOOOoOOo0O0 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 70003 : oOooo0 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 70004 : ooOo0o00OOo0 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 70005 : I1IIii1 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 70006 : OO0o0oOOO0O ( )
elif Ooo0oo0ooO == 90037 : Oo0O0 ( OOoOO0oo0ooO )
elif Ooo0oo0ooO == 900377 : ooo ( OOoOO0oo0ooO )
if 34 - 34: OO0oo0oOO % o0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
