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
iIiiiI = "0.0.2"
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
oO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieMusic/Change_Log_Temp' ) )
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OOO , 'icon.png' ) )
oooOOOOO = oO0o0o0ooO0oO + ( iI111iI ( 'L2FydC8=' ) )
i1iiIII111ii = 'Some Website'
i1iIIi1 = os . path . join ( i11 , 'wizard.log' )
ii11iIi1I = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieMusic' )
iI111I11I1I1 = xbmc . translatePath ( 'special://thumbnails' ) ;
OOooO0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OOO , 'fanart.jpg' ) )
iIii1 = O0oo0OO0 . getLocalizedString
oOOoO0 = CookieJar ( )
O0OoO000O0OO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( oOOoO0 ) )
O0OoO000O0OO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
iiI1IiI = int ( sys . argv [ 1 ] )
II = xbmc . translatePath ( O0oo0OO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i1111 = xbmc . translatePath ( 'special://home/userdata/' )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
OooO0 = ii11iIi1I + '/addons.ini'
II11iiii1Ii = xbmcgui . Dialog ( )
OO0o = xbmcgui . Dialog ( )
if os . path . exists ( ooOoOoo0O ) == True :
 Ooo = open ( ooOoOoo0O ) . read ( )
else : Ooo = [ ]
if 68 - 68: oOo00Oo00O + I11i1I + o0o0OOO0o0 % IIII % o0O0 . o0
if 9 - 9: OO0oo0oOO + I1iii - iIii1I11I1II1 / IIII - OoooooooOO
def i1IiiiiiiI ( ) :
 if not os . path . exists ( oO ) :
  I1i1I1II ( 'Change Log 06/03/2018 - v0.0.2' , '[COLORsteelblue]Genie Music Release 5/3/2018 v0.0.2:[CR]The Latest Addition To The GenieTv Repo.[CR][CR]Extensive Music Library,[CR]Music Videos,[CR]Music Channels By DJing,[CR]Karaoke,[CR]Song Lyrics Archive,[CR]Live Radio,[CR]Searches For Album, Song, Karoke Tracks And Lyrics.[CR][CR][CR][CR]To Make Requests For Content Please Visit[CR]http://genietv.co.uk/geniemusic/[/COLOR]' )
  os . makedirs ( oO )
def i1IiIiiI ( ) :
 I1i1I1II ( 'Change Log 06/03/2018 - v0.0.2' , '[COLORsteelblue]Genie Music Release 5/3/2018 v0.0.2:[CR]The Latest Addition To The GenieTv Repo.[CR][CR]Extensive Music Library,[CR]Music Videos,[CR]Music Channels By DJing,[CR]Karaoke,[CR]Song Lyrics Archive,[CR]Live Radio,[CR]Searches For Album, Song, Karoke Tracks And Lyrics.[CR][CR][CR][CR]To Make Requests For Content Please Visit[CR]http://genietv.co.uk/geniemusic/[/COLOR]' )
 if 31 - 31: IIII . IIII - o0oOOo0O0Ooo / OoO0O00 + I1iii * I1IiiI
def O0ooOooooO ( ) :
 i1IiiiiiiI ( )
 o00O ( '[COLORorangered]Music Library[/COLOR]' , oo0o0O00 , 210 , oooOOOOO + 'music10' , i1iiIIiiI111 , '[COLORsteelblue]Music Library[/COLOR]' )
 o00O ( '[COLORorangered]Music Search[/COLOR]' , oo0o0O00 , 16 , oooOOOOO + 'music7' , i1iiIIiiI111 , '[COLORsteelblue]Music Search[/COLOR]' )
 o00O ( '[COLORorangered]Music Vids[/COLOR]' , oo0o0O00 , 11 , oooOOOOO + 'music12' , i1iiIIiiI111 , '[COLORsteelblue]Music Vids[/COLOR]' )
 o00O ( '[COLORorangered]DJing Music Channels[/COLOR]' , '' , 13 , oooOOOOO + 'music13' , i1iiIIiiI111 , '[COLORsteelblue]DJing Music Channels[/COLOR]' )
 o00O ( '[COLORorangered]Karaoke[/COLOR]' , iI111iI ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3F1aWNrc2lsdmVyL0dlbmllL2thcmFva2Uv' ) , 212 , oooOOOOO + 'karaoke.png' , i1iiIIiiI111 , '[COLORsteelblue]Karaoke[/COLOR]' )
 o00O ( '[COLORorangered]Lyrics[/COLOR]' , iI111iI ( 'aHR0cHM6Ly93d3cuYXpseXJpY3MuY29tLw==' ) , 21 , oooOOOOO + 'lyrics.png' , i1iiIIiiI111 , '[COLORsteelblue]Lyrics[/COLOR]' )
 o00O ( '[COLORorangered]Radio[/COLOR]' , iI111iI ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3FzYS90aHVuZGVyc3RydWNrL3R4dC9yYWRpby50eHQ=' ) , 90037 , oooOOOOO + 'music5' , i1iiIIiiI111 , '[COLORsteelblue]Radio[/COLOR]' )
 o00O ( '[COLORorangered]Maintenance[/COLOR]' , '' , 5 , oooOOOOO + 'music2' , i1iiIIiiI111 , '[COLORsteelblue]Maintenance[/COLOR]' )
 OOO0OOO00oo ( '[COLORorangered]Change Log[/COLOR]' , '' , 25 , i1iiIIiiI111 , i1iiIIiiI111 , '[COLORsteelblue]Change Log[/COLOR]' )
 if 31 - 31: II111iiii - I11i1I . OO0oo0oOO % OoOoOO00 - O0
 if 4 - 4: II111iiii / I1iii . o0O0
 if 58 - 58: I11i1I * i11iIiiIii / OoOoOO00 % OO0oo0oOO - I1ii11iIi11i / oOo00Oo00O
 if 50 - 50: I1IiiI
 if 34 - 34: I1IiiI * II111iiii % o0O0 * OoOoOO00 - I1IiiI
def II1III ( ) :
 OOO0OOO00oo ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , oooOOOOO + 'music2' , OOooO0OOoo , '[COLORsteelblue]Delete Packages[/COLOR]' )
 OOO0OOO00oo ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , oooOOOOO + 'music2' , OOooO0OOoo , '[COLORsteelblue]Delete Cache[/COLOR]' )
 OOO0OOO00oo ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , oooOOOOO + 'music2' , OOooO0OOoo , '[COLORsteelblue]View Log File[/COLOR]' )
 OOO0OOO00oo ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , oooOOOOO + 'music2' , OOooO0OOoo , '[COLORsteelblue]Force Refresh[/COLOR]' )
 OOO0OOO00oo ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , oooOOOOO + 'music2' , OOooO0OOoo , '[COLORsteelblue]Force Close[/COLOR]' )
 if 19 - 19: oOo00Oo00O % i1IIi % o0oOOo0O0Ooo
def oo0OooOOo0 ( url , description ) :
 o00O ( '[COLORsteelblue]Search Lyrics[/COLOR]' , 'http:' + url , 20 , oooOOOOO + 'lyrics.png' , o0O , '[COLORsteelblue]Search Lyrics[/COLOR]' )
 O00oO = ( '[COLORorangered]' + description + '[/COLOR]' )
 I11i1I1I = oO0Oo ( url )
 oOOoo0Oo = re . compile ( '<a class="btn btn-menu" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11i1I1I )
 for url , o00OO00OoO in oOOoo0Oo :
  o00O ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' , 'http:' + url , 22 , oooOOOOO + o00OO00OoO + '.png' , o0O , O00oO + '[CR][CR]' + o00OO00OoO )
def OOOO0OOoO0O0 ( url , description ) :
 o00O ( '[COLORsteelblue]Search Lyrics[/COLOR]' , 'http:' + url , 20 , oooOOOOO + 'lyrics.png' , o0O , '[COLORsteelblue]Search Lyrics[/COLOR]' )
 O00oO = ( '[COLORorangered]' + description + '[/COLOR]' )
 I11i1I1I = oO0Oo ( url )
 oOOoo0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a><br>' , re . DOTALL ) . findall ( I11i1I1I )
 for url , o00OO00OoO in oOOoo0Oo :
  o00O ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' , 'https://www.azlyrics.com/' + url , 23 , oooOOOOO + 'lyrics.png' , o0O , O00oO + '[CR][CR]' + o00OO00OoO )
def O0Oo000ooO00 ( url , description ) :
 o00O ( '[COLORsteelblue]Search Lyrics[/COLOR]' , 'http:' + url , 20 , oooOOOOO + 'lyrics.png' , o0O , '[COLORsteelblue]Search Lyrics[/COLOR]' )
 O00oO = ( '[COLORorangered]' + description + '[/COLOR]' )
 I11i1I1I = oO0Oo ( url )
 oO0 = re . compile ( '<!-- start of song list -->(.+?)<!-- end of song list -->' , re . DOTALL ) . findall ( I11i1I1I )
 Ii1iIiII1ii1 = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a><br>' , re . DOTALL ) . findall ( str ( oO0 ) )
 for url , o00OO00OoO in Ii1iIiII1ii1 :
  ooOooo000oOO = '\''
  OOO0OOO00oo ( ( '[COLORsteelblue]' + ( o00OO00OoO ) . replace ( ooOooo000oOO , '' ) . replace ( '/' , '' ) + '[/COLOR]' ) , ( url ) . replace ( '../' , 'https://www.azlyrics.com/' ) , 24 , oooOOOOO + 'lyrics.png' , o0O , O00oO + '[CR][CR]' + ( '[COLORsteelblue]' + ( o00OO00OoO ) . replace ( ooOooo000oOO , '' ) . replace ( '/' , '' ) + '[/COLOR]' ) )
def Oo0oOOo ( url , description ) :
 O00oO = ( '[COLORorangered]' + description + '[/COLOR]' )
 I11i1I1I = oO0Oo ( url )
 oO0 = re . compile ( '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->(.+?)</div>' , re . DOTALL ) . findall ( I11i1I1I )
 for oo0OooOOo0 in oO0 :
  oo0OooOOo0 = ( '[COLORsteelblue]' + oo0OooOOo0 + '[/COLOR]' ) . replace ( '<br>' , '' ) . replace ( '<i>' , '[CR]' ) . replace ( '</i>' , '[CR]' )
  I1i1I1II ( O00oO , oo0OooOOo0 )
def Oo0OoO00oOO0o ( ) :
 OOO00O = OO0o . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOoOO0oo0ooO = 'https://search.azlyrics.com/search.php?q=' + ( OOO00O ) . replace ( ' ' , '+' ) + '&w=songs&p=1'
 I11i1I1I = oO0Oo ( OOoOO0oo0ooO )
 Ii1iIiII1ii1 = re . compile ( '<tr><td class="text-left visitedlyr">.+?<a href="([^"]*)" target="_blank"><b>(.+?)</b></a>  by <b>(.+?)</b><br>.+?<small>(.+?)</td></tr>' , re . DOTALL ) . findall ( I11i1I1I )
 for O0o0O00Oo0o0 , O00O0oOO00O00 , i1Oo00 , O00oO in Ii1iIiII1ii1 :
  OOO0OOO00oo ( '[COLORsteelblue]' + O00O0oOO00O00 + ' - ' + i1Oo00 + '[/COLOR]' , O0o0O00Oo0o0 , 24 , oooOOOOO + 'lyrics.png' , o0O , '[COLORsteelblue]' + O00O0oOO00O00 + ' - ' + i1Oo00 + '[/COLOR]' + '[CR][CR]' + ( '[COLORorangered]' + ( O00oO ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) + '[/COLOR]' ) )
  if 31 - 31: OO0oo0oOO . OoOoOO00 / O0
  xbmcplugin . setContent ( iiI1IiI , 'movies' )
  if 89 - 89: OoOoOO00
def OO0oOoOO0oOO0 ( url ) :
 I11i1I1I = oO0Oo ( url )
 oOOoo0Oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I11i1I1I )
 for url , oO0OOoo0OO , O00oO , o0O , o00OO00OoO in oOOoo0Oo :
  if '.php' in url :
   o00O ( o00OO00OoO , url , 211 , oO0OOoo0OO , o0O , O00oO )
  else :
   o00O ( o00OO00OoO , url , 212 , oO0OOoo0OO , o0O , O00oO )
def O0ii1ii1ii ( url ) :
 I11i1I1I = oO0Oo ( url )
 oOOoo0Oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I11i1I1I )
 for url , oO0OOoo0OO , O00oO , o0O , o00OO00OoO in oOOoo0Oo :
  if '.php' in url :
   o00O ( o00OO00OoO , url , 211 , oO0OOoo0OO , o0O , O00oO )
  else :
   o00O ( o00OO00OoO , url , 212 , oO0OOoo0OO , o0O , O00oO )
def oooooOoo0ooo ( url , description ) :
 O00oO = description
 I1I1IiI1 = O0OoO000O0OO . open ( url ) . read ( )
 if 5 - 5: o0oOOo0O0Ooo * I1iii + OoOoOO00 . I11i1I + OoOoOO00
 try :
  oOiIi1IIIi1 = re . findall ( r'<a .*?>(.*?)</a>' , I1I1IiI1 )
  O0oOoOOOoOO = re . findall ( r'<a.*?href="(.*?)">' , I1I1IiI1 )
  if 38 - 38: OO0oo0oOO
  for Ii1 in O0oOoOOOoOO :
   if '.db' in Ii1 :
    pass
   elif 'cover/' in Ii1 :
    pass
   elif '.cue' in Ii1 :
    pass
   elif '.log' in Ii1 :
    pass
   elif '.accurip' in Ii1 :
    pass
   elif '.gif' in Ii1 :
    pass
   elif '.srt' in Ii1 :
    pass
   elif '..' in Ii1 :
    pass
   elif '.txt' in Ii1 :
    pass
   elif '.nfo' in Ii1 :
    pass
   elif '.jpg' in Ii1 :
    pass
   elif '1-Irani/' in Ii1 :
    pass
   elif 'index.php' in Ii1 :
    pass
   elif '.png' in Ii1 :
    pass
   elif '?C=M&O=D' in Ii1 :
    pass
   elif '?C=M&O=A' in Ii1 :
    pass
   elif '?C=N&O=D' in Ii1 :
    pass
   elif '?C=N&O=A' in Ii1 :
    pass
   elif '?C=S&O=A' in Ii1 :
    pass
   elif '?C=S&O=D' in Ii1 :
    pass
   elif '?C=N;O=D' in Ii1 :
    pass
   elif '?C=M;O=A' in Ii1 :
    pass
   elif '?C=S;O=A' in Ii1 :
    pass
   elif '?C=D;O=A' in Ii1 :
    pass
   elif 'Torrent' in Ii1 :
    pass
   elif 'exe' in Ii1 :
    pass
   elif 'public' in Ii1 :
    pass
   elif '?C=D;O=A' in Ii1 :
    pass
   elif 'pub' in Ii1 :
    pass
   elif 'install' in Ii1 :
    pass
   elif '?C=D;O=A' in Ii1 :
    pass
   elif '?C=D;O=A' in Ii1 :
    pass
   elif '.m3u' in Ii1 :
    pass
   elif '?C=D;O=A' in Ii1 :
    pass
   elif 'mpeg' in Ii1 :
    pass
   elif '.doc' in Ii1 :
    pass
   elif '.html' in Ii1 :
    pass
   elif 'boss' in Ii1 :
    pass
   elif 'quicksilver' in Ii1 :
    pass
   else :
    oO0OOoo0OO = ( Ii1 ) . replace ( '/' , '' )
    o00OO00OoO = Ii1
    if 'txt' in o00OO00OoO :
     pass
    if '.avi' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( 'avi' , '' )
    if '.' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( '.' , ' ' )
    if '_' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( '_' , ' ' )
    if '%20' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( '%20' , ' ' )
    if '/' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( '/' , '' )
    if 'mkv' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( 'mkv' , '' )
    if 'mp4' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( 'mp4' , '' )
    if 'Tehmovies' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( 'Tehmovies' , '' )
    if 'flac' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( 'flac' , '' )
    if '&amp;' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( '&amp;' , '&' )
    if 'mp3' in o00OO00OoO :
     o00OO00OoO = o00OO00OoO . replace ( 'mp3' , '' )
     if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / I11i1I + IIII
     if 87 - 87: oOo00Oo00O * I1ii11iIi11i + I11i1I / iIii1I11I1II1 / o0O0
    if '.mkv' in Ii1 or '.MP3' in Ii1 or '.wma' in Ii1 or '.m4a' in Ii1 or '.m4a' in Ii1 or '.m4B' in Ii1 or '.m4a' in Ii1 or '.m4v' in Ii1 or '.mp3' in Ii1 or '.mp4' in Ii1 or '.avi' in Ii1 or '.flv' in Ii1 or '.mpeg' in Ii1 or '.3gp' in Ii1 or '.divx' in Ii1 or '.flac' in Ii1 or '.strm' in Ii1 :
     OOO0OOO00oo ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' , url + Ii1 , 15 , url + 'cunt.png' , url + 'cunt.png' , o00OO00OoO + '[CR][CR]' + O00oO )
     if 37 - 37: o0O0 - I1iii * oOo00Oo00O % i11iIiiIii - OO0oo0oOO
    else :
     o00O ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' , url + Ii1 , 212 , url + oO0OOoo0OO + '.png' , url + oO0OOoo0OO + '.png' , o00OO00OoO + '[CR][CR]' + O00oO )
     if 83 - 83: o0o0OOO0o0 / I1IiiI
     if 34 - 34: o0
     if 57 - 57: oOo00Oo00O . o0o0OOO0o0 . i1IIi
     if 42 - 42: o0o0OOO0o0 + I1ii11iIi11i % O0
 except Exception , i1iIIIi1i :
  print str ( i1iIIIi1i )
 xbmcplugin . addSortMethod ( iiI1IiI , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1iIIiiii ( ) :
 i1iI11i1ii11 = xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 ) )
 if not os . path . exists ( Oo0o0000o0o0 ) :
  OO0o . ok ( '[COLOR=white]Genie Music[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
def OOooo0O00o ( url ) :
 if O0oo0OO0 . getSetting ( 'down' ) == 'true' :
  oOOoOooOo ( url , o00OO00OoO )
 else :
  O000oo ( url )
def oOOoOooOo ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  IIi1I11I1II = '.mp4'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.flac' in url :
  IIi1I11I1II = '.flac'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.strm' in url :
  IIi1I11I1II = '.strm'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.M4v' in url :
  IIi1I11I1II = '.M4v'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.MP3' in url :
  IIi1I11I1II = '.MP3'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.wma' in url :
  IIi1I11I1II = '.wma'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.m4B' in url :
  IIi1I11I1II = '.m4B'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.m4a' in url :
  IIi1I11I1II = '.m4a'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.mkv' in url :
  IIi1I11I1II = '.mkv'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.mp3' in url :
  IIi1I11I1II = '.mp3'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.avi' in url :
  IIi1I11I1II = '.avi'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.mov' in url :
  IIi1I11I1II = '.mov'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.mpeg' in url :
  IIi1I11I1II = '.mpeg'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.mpg' in url :
  IIi1I11I1II = '.mpg'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.flv' in url :
  IIi1I11I1II = '.flv'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 elif '.wmv' in url :
  IIi1I11I1II = '.wmv'
  OooOoooOo = [ '[COLORsteelblue]PLAY[/COLOR]' , '[COLORsteelblue]DOWNLOAD[/COLOR]' ]
  ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Play/Download - ' + IIi1I11I1II + '[/COLOR]' , OooOoooOo )
  if ii11IIII11I == 0 :
   O000oo ( url )
  if ii11IIII11I == 1 :
   OOooo ( url , name , IIi1I11I1II )
 else :
  O000oo ( url )
def OOooo ( url , name , cat ) :
 iI1iIIiiii ( )
 i1iI11i1ii11 = xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Item Is Downloading" , "And Will Be Available In Just A Moment" , '' , 'http://GenieTv.co.uk' )
 oOooOOOoOo = os . path . join ( i1iI11i1ii11 , file )
 try :
  os . remove ( oOooOOOoOo )
 except :
  pass
 downloader . download ( url , oOooOOOoOo , o0oO0 )
 OO0o = xbmcgui . Dialog ( )
 OO0o . ok ( "Genie Music" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 41 - 41: IIII - O0 - O0
def oO00OOoO00 ( ) :
 OooOoooOo = [ '[COLORsteelblue]Songs[/COLOR]' , '[COLORsteelblue]Albums[/COLOR]' , '[COLORsteelblue]Music Videos[/COLOR]' , '[COLORsteelblue]Lyrics[/COLOR]' ]
 ii11IIII11I = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]CATEGORIES[/COLOR]' , OooOoooOo )
 if ii11IIII11I == 0 :
  IiI111111IIII ( oO0o0o0ooO0oO + '/songs.php' )
 if ii11IIII11I == 1 :
  IiI111111IIII ( oO0o0o0ooO0oO + '/albums.php' )
 if ii11IIII11I == 2 :
  i1Ii ( oO0o0o0ooO0oO + '/gmv.php' )
 if ii11IIII11I == 3 :
  Oo0OoO00oOO0o ( )
  if 14 - 14: o0O0
def IiI111111IIII ( url ) :
 OOO00O = OO0o . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iI1iIi111i = OOO00O . lower ( )
 I11i1I1I = oO0Oo ( url )
 o0oO0 . create ( "[COLORsteelblue]Genie Music[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
 Ii1iIiII1ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I11i1I1I )
 for url , oO0OOoo0OO , O00oO , iiIi1IIi1I , o00OO00OoO in Ii1iIiII1ii1 :
  if I1iI1iIi111i in o00OO00OoO . lower ( ) :
   o0oO0 . update ( 20 , "" , "Watch Close" )
   o00OO00OoO = ( o00OO00OoO . replace ( '%20' , ' ' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
   o0oO0 . update ( 40 , "" , "Matching Up" )
   if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
    o0oO0 . update ( 60 , "" , "Adding A Few Songs There" )
    OOO0OOO00oo ( ( '[COLORsteelblue]' + ( o00OO00OoO ) . replace ( '/' , '' ) + '[/COLOR]' ) , url , 15 , oO0OOoo0OO , o0O , ( '[COLORsteelblue]' + ( o00OO00OoO ) . replace ( '/' , '' ) + '[CR][CR]Song[/COLOR]' ) )
   else :
    o0oO0 . update ( 80 , "" , "Oooooh An Album" )
    o00O ( ( '[COLORsteelblue]' + ( o00OO00OoO ) . replace ( '/' , '' ) + '[/COLOR]' ) , url , 212 , oO0OOoo0OO , o0O , ( '[COLORsteelblue]' + ( o00OO00OoO ) . replace ( '/' , '' ) + '[CR][CR]Folder[/COLOR]' ) )
    o0oO0 . update ( 100 , "" , "Get In" )
    if 84 - 84: I1iii * II111iiii + Oo0Ooo
    O0ooO0Oo00o ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( iiI1IiI , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: iIii1I11I1II1 * OoO0O00
def oOooOo0 ( ) :
 i1I1ii11i1Iii = ( oO0o0o0ooO0oO ) . replace ( '/geniemusic' , '/quicksilver/Other/Music' )
 I1IiiiiI = oO0Oo ( oO0o0o0ooO0oO + '/gmv.php' )
 I11i1I1I = oO0Oo ( i1I1ii11i1Iii )
 o0OIiII = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' , re . DOTALL ) . findall ( I1IiiiiI )
 Ii1iIiII1ii1 = re . compile ( '<a.*?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11i1I1I )
 for O0o0O00Oo0o0 , o00OO00OoO in o0OIiII :
  ii1iII1II = oO0Oo ( O0o0O00Oo0o0 )
  Iii1I1I11iiI1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' , re . DOTALL ) . findall ( ii1iII1II )
  for I1I1i1I , i1Oo00 in Iii1I1I11iiI1 :
   i1Oo00 = ( i1Oo00 . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
   if '.png' in I1I1i1I or '.jpg' in I1I1i1I or '=' in I1I1i1I or 'quicksilver' in I1I1i1I or '&' in I1I1i1I or '.jpeg' in I1I1i1I or "'" in I1I1i1I :
    pass
   elif '.mkv' in I1I1i1I or '.MP3' in I1I1i1I or '.m4a' in I1I1i1I or '.m4B' in I1I1i1I or '.m4a' in I1I1i1I or '.m4v' in I1I1i1I or '.mp3' in I1I1i1I or '.mp4' in I1I1i1I or '.avi' in I1I1i1I or '.flv' in I1I1i1I or '.mpeg' in I1I1i1I or '.3gp' in I1I1i1I or '.divx' in I1I1i1I or '.flac' in I1I1i1I or '.strm' in I1I1i1I :
    ii1I ( ( '[COLORsteelblue]' + i1Oo00 + ' -[COLORgold] source ' + o00OO00OoO + '[/COLOR]' ) , O0o0O00Oo0o0 + I1I1i1I , 15 , oooOOOOO + 'music12' , i1iiIIiiI111 , '[COLORsteelblue]' + i1Oo00 + ' - [COLORgold]Source Home[/COLOR]' )
    o0oO0 . create ( "[COLORsteelblue]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 50 , "" , "Getting Video Links" )
 for O0o0O00Oo0o0 , o00OO00OoO in Ii1iIiII1ii1 :
  o00OO00OoO = ( o00OO00OoO . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
  if '.png' in O0o0O00Oo0o0 or '=' in O0o0O00Oo0o0 or '.jpg' in O0o0O00Oo0o0 or '=' in O0o0O00Oo0o0 or 'quicksilver' in O0o0O00Oo0o0 or '&' in O0o0O00Oo0o0 or '.jpeg' in O0o0O00Oo0o0 or "'" in O0o0O00Oo0o0 :
   pass
  elif '.mkv' in O0o0O00Oo0o0 or '.MP3' in O0o0O00Oo0o0 or '.m4a' in O0o0O00Oo0o0 or '.m4B' in O0o0O00Oo0o0 or '.m4a' in O0o0O00Oo0o0 or '.m4v' in O0o0O00Oo0o0 or '.mp3' in O0o0O00Oo0o0 or '.mp4' in O0o0O00Oo0o0 or '.avi' in O0o0O00Oo0o0 or '.flv' in O0o0O00Oo0o0 or '.mpeg' in O0o0O00Oo0o0 or '.3gp' in O0o0O00Oo0o0 or '.divx' in O0o0O00Oo0o0 or '.flac' in O0o0O00Oo0o0 or '.strm' in O0o0O00Oo0o0 :
   ii1I ( ( '[COLORsteelblue]' + o00OO00OoO + ' -[COLORgold] source Home2[/COLOR]' ) , i1I1ii11i1Iii + O0o0O00Oo0o0 , 15 , oooOOOOO + 'music12' , i1iiIIiiI111 , '[COLORsteelblue]' + o00OO00OoO + ' - [COLORgold]Source Home[/COLOR]' )
   o0oO0 . create ( "[COLORsteelblue]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 50 , "" , "Getting Video Links" )
  else :
   o00O ( '[COLORsteelblue]' + o00OO00OoO + ' - [COLORgold]Source Home[/COLOR]' , i1I1ii11i1Iii + '/' + O0o0O00Oo0o0 , 212 , oooOOOOO + 'music12' , i1iiIIiiI111 , '[COLORsteelblue]' + o00OO00OoO + ' - [COLORgold]Source Home[/COLOR]' )
   if 99 - 99: IIII / Oo0Ooo / o0 % I1IiiI
   O0ooO0Oo00o ( 'tvshows' , 'Media Info 3' )
   xbmcplugin . addSortMethod ( iiI1IiI , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1Ii ( url ) :
 OOO00O = OO0o . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iI1iIi111i = OOO00O . lower ( )
 I1IiiiiI = oO0Oo ( url )
 o0OIiII = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' , re . DOTALL ) . findall ( I1IiiiiI )
 for url , o00OO00OoO in o0OIiII :
  ii1iII1II = oO0Oo ( url )
  Iii1I1I11iiI1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' , re . DOTALL ) . findall ( ii1iII1II )
  for I1I1i1I , i1Oo00 in Iii1I1I11iiI1 :
   if I1iI1iIi111i in i1Oo00 . lower ( ) :
    i1Oo00 = ( i1Oo00 . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) . replace ( '.mkv' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4B' , '' ) . replace ( '.m4a' , '' ) . replace ( '.m4v' , '' ) . replace ( '.mp3' , '' ) . replace ( '.mp4' , '' ) . replace ( '.avi' , '' ) . replace ( '.flv' , '' ) . replace ( '.mpeg' , '' ) . replace ( '.3gp' , '' ) . replace ( '.divx' , '' ) . replace ( '.flac' , '' ) . replace ( '.strm' , '' ) . replace ( '.' , ' ' ) )
    if '.png' in I1I1i1I or '.jpg' in I1I1i1I or '=' in I1I1i1I or 'quicksilver' in I1I1i1I or '&' in I1I1i1I or '.jpeg' in I1I1i1I or "'" in I1I1i1I :
     pass
    elif '.mkv' in I1I1i1I or '.MP3' in I1I1i1I or '.m4a' in I1I1i1I or '.m4B' in I1I1i1I or '.m4a' in I1I1i1I or '.m4v' in I1I1i1I or '.mp3' in I1I1i1I or '.mp4' in I1I1i1I or '.avi' in I1I1i1I or '.flv' in I1I1i1I or '.mpeg' in I1I1i1I or '.3gp' in I1I1i1I or '.divx' in I1I1i1I or '.flac' in I1I1i1I or '.strm' in I1I1i1I :
     ii1I ( ( '[COLORsteelblue]' + i1Oo00 + ' -[COLORgold] source ' + o00OO00OoO + '[/COLOR]' ) , url + I1I1i1I , 15 , oooOOOOO + 'music12' , i1iiIIiiI111 , '' )
     o0oO0 . create ( "[COLORsteelblue]Genie Music[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 50 , "" , "Getting Video Links" )
     if 13 - 13: o0o0OOO0o0 * Oo0Ooo * I1iii
     O0ooO0Oo00o ( 'tvshows' , 'Media Info 3' )
  xbmcplugin . addSortMethod ( iiI1IiI , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 50 - 50: o0oOOo0O0Ooo * o0o0OOO0o0 % O0
def OooOoOO0 ( ) :
 iI1i11iII111 = requests . get ( 'http://www.djing.com/' ) . content
 Iii1IIII11I = re . compile ( '<img class="thumb" src="([^"]*)" alt=.+?<source src="([^"]*)"></video><h3>(.+?)</h3><p>(.+?)/p>' , re . DOTALL ) . findall ( iI1i11iII111 )
 for oO0OOoo0OO , O0o0O00Oo0o0 , o00OO00OoO , O00oO in Iii1IIII11I :
  oO0OOoo0OO = ( 'http://www.djing.com' + oO0OOoo0OO )
  o00OO00OoO = ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' ) . replace ( '[Subscribers only]' , '' )
  O00oO = ( '[COLORorangered]' + O00oO + '[/COLOR]' ) . replace ( '<' , '' )
  if 'Submit' in o00OO00OoO :
   pass
  elif '&lt;' in o00OO00OoO :
   pass
  else :
   ii1I ( o00OO00OoO , O0o0O00Oo0o0 , 15 , oO0OOoo0OO , oO0OOoo0OO , o00OO00OoO + '[CR][CR]' + O00oO )
   if 77 - 77: Oo0Ooo - i1IIi - o0o0OOO0o0 . OoOoOO00
 O0ooO0Oo00o ( 'movies' , 'MAIN' )
 if 39 - 39: II111iiii / I1iii + OO0oo0oOO / OoOoOO00
 if 13 - 13: o0 + O0 + o0O0 % I1IiiI / o0oOOo0O0Ooo . o0
def OO0Oooo0oOO0O ( url ) :
 I11i1I1I = oO0Oo ( url )
 Ii1iIiII1ii1 = re . compile ( '<title>(.+?)</title>.+?<sportsdevil>(.+?)' , re . DOTALL ) . findall ( I11i1I1I )
 for o00OO00OoO , url in Ii1iIiII1ii1 :
  o00O0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
  ii1I ( o00OO00OoO , o00O0 , 15 , i1iiIIiiI111 , '' , '' )
  O0ooO0Oo00o ( 'tvshows' , 'Media Info 3' )
  if 83 - 83: I1iii
def oO00Oo0O0o ( url ) :
 I11i1I1I = oO0Oo ( url )
 Ii1iIiII1ii1 = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 ii1 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 Iii1IIII11I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 I1iIIiiIIi1i = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 O0O0ooOOO = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 oOOo0O00o = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( I11i1I1I )
 iIiIi11 = re . compile ( '<name>(.+?)</name>.+?<externallink>(.+?)</externallink>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 OOO = re . compile ( '<title>(.+?)</title>.+?<sportsdevil>(.+?)' , re . DOTALL ) . findall ( I11i1I1I )
 for o00OO00OoO , oO0OOoo0OO , url , iiiiI in ii1 :
  o00O ( o00OO00OoO , url , 90037 , oO0OOoo0OO , iiiiI , o00OO00OoO )
 for o00OO00OoO , oO0OOoo0OO , url , iiiiI in Ii1iIiII1ii1 :
  o00O ( o00OO00OoO , url , 90037 , oO0OOoo0OO , iiiiI , o00OO00OoO )
 for o00OO00OoO , url , oO0OOoo0OO , iiiiI in Iii1IIII11I :
  ii1I ( o00OO00OoO , url , 15 , oO0OOoo0OO , iiiiI , o00OO00OoO )
 for o00OO00OoO , url , oO0OOoo0OO , iiiiI in I1iIIiiIIi1i :
  ii1I ( o00OO00OoO , url , 15 , oO0OOoo0OO , iiiiI , o00OO00OoO )
 for o00OO00OoO , url , oO0OOoo0OO , iiiiI in O0O0ooOOO :
  ii1I ( o00OO00OoO , url , 15 , oO0OOoo0OO , iiiiI , o00OO00OoO )
 for o00OO00OoO , url , oO0OOoo0OO in oOOo0O00o :
  ii1I ( o00OO00OoO , url , 15 , oO0OOoo0OO , oO0OOoo0OO , o00OO00OoO )
 for o00OO00OoO , url , oO0OOoo0OO , o0O in iIiIi11 :
  o00O ( o00OO00OoO , url , 90037 , oO0OOoo0OO , oO0OOoo0OO , o00OO00OoO )
 for o00OO00OoO , url , oO0OOoo0OO , o0O in iIiIi11 :
  ii1I ( o00OO00OoO , url , 15 , oO0OOoo0OO , oO0OOoo0OO , o00OO00OoO )
  O0ooO0Oo00o ( 'tvshows' , 'Media Info 3' )
def oooOo0OOOoo0 ( url ) :
 I11i1I1I = oO0Oo ( url )
 Ii1iIiII1ii1 = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 Iii1IIII11I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I11i1I1I )
 for o00OO00OoO , oO0OOoo0OO , url , iiiiI in Ii1iIiII1ii1 :
  o00O ( o00OO00OoO , url , 90037 , oO0OOoo0OO , iiiiI , o00OO00OoO )
 for o00OO00OoO , url , oO0OOoo0OO , iiiiI in Iii1IIII11I :
  ii1I ( o00OO00OoO , url , 15 , oO0OOoo0OO , iiiiI , o00OO00OoO )
  O0ooO0Oo00o ( 'tvshows' , 'Media Info 3' )
  if 51 - 51: Oo0Ooo / OoOoOO00 . I11i1I * o0oOOo0O0Ooo + OoO0O00 * o0
  if 73 - 73: OoO0O00 + OoooooooOO - O0 - IIII - II111iiii
def O0O ( name , url , mode , iconimage , description = "" , isFolder = True , background = None ) :
 o0oOOoooOOOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 if 62 - 62: I1iii
 o0O0o0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 o0O0o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 if background :
  o0O0o0 . setProperty ( 'fanart_image' , background )
 if mode == 1 or mode == 2 :
  o0O0o0 . addContextMenuItems ( items = [ ( '{0}' . format ( iIii1 ( 10008 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=22)' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) ) ) ] )
 elif mode == 404 :
  o0O0o0 . setProperty ( 'IsPlayable' , 'true' )
  o0O0o0 . addContextMenuItems ( items = [ ( '{0}' . format ( iIii1 ( 10009 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
 elif mode == 556 :
  o0O0o0 . setProperty ( 'IsPlayable' , 'true' )
  o0O0o0 . addContextMenuItems ( items = [ ( '{0}' . format ( iIii1 ( 10010 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
  if 37 - 37: I1ii11iIi11i * o0o0OOO0o0 % i11iIiiIii % I1iii + IIII
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOoooOOOOo , listitem = o0O0o0 , isFolder = isFolder )
 if 78 - 78: I1ii11iIi11i % oOo00Oo00O / o0O0 - iIii1I11I1II1
def ooooo0O0000oo ( handle , url , listitem , isFolder ) :
 if 21 - 21: o0oOOo0O0Ooo - I1IiiI
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 18 - 18: Oo0Ooo + o0o0OOO0o0 % I11i1I - OoooooooOO - I1ii11iIi11i / i1IIi
def oo0oO ( url ) :
 Oo0O0 = oO0Oo ( url )
 Ii1iIiII1ii1 = re . compile ( '<img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+?rel=".+? >(.+?)</a>&#32' , re . DOTALL ) . findall ( Oo0O0 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( Oo0O0 )
 for oO0OOoo0OO , url , o00OO00OoO in Ii1iIiII1ii1 :
  if 'share' in url :
   Ooo0OOoOoO0 ( ( '[COLORorangered]' + o00OO00OoO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 70511 , 'http:' + oO0OOoo0OO )
  elif 'watch?v=' in url :
   Ooo0OOoOoO0 ( ( '[COLORpurple]' + o00OO00OoO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oO0OOoo0OO )
  elif 'youtu' in url :
   Ooo0OOoOoO0 ( ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) , 7052 , 'http:' + oO0OOoo0OO )
 for url in next :
  oOo0OOoO0 ( '[COLORsteelblue]NEXT[/COLOR]' , url , 7050 , oooOOOOO + 'Next.png' )
  if 11 - 11: I1ii11iIi11i . OoO0O00 * o0 * OoooooooOO + I1iii
def IiII111i1i11 ( url ) :
 Oo0O0 = oO0Oo ( url )
 Ii1iIiII1ii1 = re . compile ( '"shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( Oo0O0 )
 for url in Ii1iIiII1ii1 :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
def i111iIi1i1II1 ( url ) :
 Oo0O0 = oO0Oo ( url )
 Iii1IIII11I = re . compile ( '"shortUrl":"([^"]*)"' , re . DOTALL ) . findall ( Oo0O0 )
 for url in Iii1IIII11I :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 86 - 86: iIii1I11I1II1 / OoOoOO00 . II111iiii
  if 19 - 19: I1ii11iIi11i % OoooooooOO % o0 * o0oOOo0O0Ooo % O0
def ooo ( ) :
 oOo0OOoO0 ( ( '[COLORsteelblue]GENRE[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oooOOOOO + 'RadioNomy.png' )
 oOo0OOoO0 ( ( '[COLORsteelblue]SORT BY[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oooOOOOO + 'RadioNomy.png' )
 oOo0OOoO0 ( ( '[COLORsteelblue]SEARCH[/COLOR]' ) , '' , 70006 , oooOOOOO + 'RadioNomy.png' )
 if 27 - 27: I1iii % I1IiiI
def o0oooOO00 ( url ) :
 Oo0O0 = OPEN_CAT ( url )
 Ii1iIiII1ii1 = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( Oo0O0 )
 for url , o00OO00OoO in Ii1iIiII1ii1 :
  oOo0OOoO0 ( ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oooOOOOO + 'RadioNomy.png' )
def iiIiii1IIIII ( url ) :
 Oo0O0 = OPEN_CAT ( url )
 Ii1iIiII1ii1 = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( Oo0O0 )
 for url , o00OO00OoO in Ii1iIiII1ii1 :
  oOo0OOoO0 ( ( '[COLORsteelblue]' + o00OO00OoO + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oooOOOOO + 'RadioNomy.png' )
def o00o ( url ) :
 Oo0O0 = OPEN_CAT ( url )
 Ii1iIiII1ii1 = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( Oo0O0 )
 Iii1IIII11I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( Oo0O0 )
 for url , o00OO00OoO in Iii1IIII11I :
  oOo0OOoO0 ( ( '[COLORsteelblue]Filter - ' + o00OO00OoO + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oooOOOOO + 'RadioNomy.png' )
 for url , oO0OOoo0OO , o00OO00OoO in Ii1iIiII1ii1 :
  Ooo0OOoOoO0 ( ( '[COLORsteelblue]Stream - ' + o00OO00OoO + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oO0OOoo0OO )
def IIIIiiIiiI ( url ) :
 Oo0O0 = OPEN_CAT ( url )
 Ii1iIiII1ii1 = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( Oo0O0 )
 for url in Ii1iIiII1ii1 :
  RESOLVEtest ( url )
def IIIIiI11I11 ( ) :
 OOO00O = OO0o . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iI1iIi111i = OOO00O
 oo00o0 = 'https://www.radionomy.com/en/search/index?query=' + ( OOO00O ) . replace ( ' ' , '+' )
 I11i1I1I = oO0Oo ( oo00o0 )
 Ii1iIiII1ii1 = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I11i1I1I )
 for O0o0O00Oo0o0 , oO0OOoo0OO , o00OO00OoO in Ii1iIiII1ii1 :
  Ooo0OOoOoO0 ( ( '[COLORsteelblue]Stream - ' + o00OO00OoO + '[/COLOR]' ) , ( iI111iI ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + O0o0O00Oo0o0 , 70005 , oO0OOoo0OO )
  if 4 - 4: IIII % oOo00Oo00O * OoO0O00
  if 100 - 100: OO0oo0oOO * I11i1I + I11i1I
  if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
  if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
  if 83 - 83: II111iiii + OO0oo0oOO
def oO00ooooO0o ( title , message , times = 2000 , icon = i1iiIIiiI111 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def oo0o ( ) :
 o0oO0oooOoo = I1III1111iIi ( )
 I1i111I = o0oO0oooOoo . replace ( iI1Ii11111iIi , "" )
 if os . path . exists ( o0oO0oooOoo ) or not o0oO0oooOoo == False :
  OooOo0oo0O0o00O = open ( o0oO0oooOoo , mode = 'r' ) ; I1i11 = OooOo0oo0O0o00O . read ( ) ; OooOo0oo0O0o00O . close ( )
  I1i1I1II ( "%s - %s" % ( oo00 , I1i111I ) , I1i11 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def I1III1111iIi ( ) :
 IiIi1I1 = False
 if os . path . exists ( os . path . join ( iI1Ii11111iIi , 'xbmc.log' ) ) :
  IiIi1I1 = os . path . join ( iI1Ii11111iIi , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( iI1Ii11111iIi , 'kodi.log' ) ) :
  IiIi1I1 = os . path . join ( iI1Ii11111iIi , 'kodi.log' )
 elif os . path . exists ( os . path . join ( iI1Ii11111iIi , 'spmc.log' ) ) :
  IiIi1I1 = os . path . join ( iI1Ii11111iIi , 'spmc.log' )
 elif os . path . exists ( os . path . join ( iI1Ii11111iIi , 'tvmc.log' ) ) :
  IiIi1I1 = os . path . join ( iI1Ii11111iIi , 'tvmc.log' )
 return IiIi1I1
 if 39 - 39: II111iiii + OoOoOO00 - I1iii . OoOoOO00
 if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
 if 38 - 38: I11i1I + II111iiii % I1iii % OoOoOO00 - IIII / OoooooooOO
 if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
 if 85 - 85: IIII % o0O0 + o0o0OOO0o0 / o0oOOo0O0Ooo . oOo00Oo00O + I11i1I
def I1i1I1II ( title , msg ) :
 class ooOoOo0 ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 2 - 2: o0O0 % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / o0O0
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 27 - 27: OoO0O00 + I1iii - i1IIi
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 69 - 69: o0 - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 79 - 79: O0 * i11iIiiIii - o0 / o0
 i1O0 = ooOoOo0 ( "Textbox.xml" , O0oo0OO0 . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 i1O0 . doModal ( )
 del i1O0
 if 32 - 32: IIII - Oo0Ooo % OoooooooOO . o0O0 / o0 + I1IiiI
 if 76 - 76: I1iii
 if 73 - 73: O0 * o0O0 + IIII + I1iii
def Ii ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def o0O0Oo ( url ) :
 if url == 'http://' : return False
 try :
  Ooo0O0oooo = urllib2 . Request ( url )
  Ooo0O0oooo . add_header ( 'User-Agent' , I1i1iiI1 )
  I1I1IiI1 = urllib2 . urlopen ( Ooo0O0oooo )
  I1I1IiI1 . close ( )
 except Exception , i1iIIIi1i :
  return i1iIIIi1i
 return True
 if 36 - 36: OoooooooOO . OoO0O00
 if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
 if 39 - 39: O0 + OO0oo0oOO
def OoOooOoO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OO0o = xbmcgui . Dialog ( )
 OO0o . ok ( "Genie Music" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Genie Music[/COLOR]" )
 return
 if 43 - 43: II111iiii . oOo00Oo00O / I1ii11iIi11i
def i1iI1 ( url ) :
 print '###' + oo00 + ' - DELETING Addons20.db ###'
 i1iI11i1ii11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 i11ii1ii11i = os . path . join ( i1iI11i1ii11 , 'Addons20.db' )
 try :
  os . remove ( i11ii1ii11i )
  OO0o = xbmcgui . Dialog ( )
  print '=== ' + oo00 + ' - DELETING    ' + str ( i11ii1ii11i ) + '    ==='
  OO0o . ok ( oo00 , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  OO0o = xbmcgui . Dialog ( )
  OO0o . ok ( oo00 , "       No File To Remove" )
 return
 if 70 - 70: i1IIi - o0O0 + Oo0Ooo
 if 12 - 12: o0oOOo0O0Ooo - I1ii11iIi11i % OoOoOO00 * o0o0OOO0o0
 if 44 - 44: o0O0 % IIII
 if 41 - 41: i1IIi - o0o0OOO0o0 - IIII
 if 8 - 8: OoO0O00 + OO0oo0oOO - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oOo00Oo00O
def oO0Oo ( url ) :
 Ooo0O0oooo = urllib2 . Request ( url )
 Ooo0O0oooo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1I1IiI1 = urllib2 . urlopen ( Ooo0O0oooo )
 Ii1 = I1I1IiI1 . read ( )
 I1I1IiI1 . close ( )
 return Ii1
def ooOoOo0 ( heading , announce ) :
 class I1i1I1II ( ) :
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
   try : OooOo0oo0O0o00O = open ( announce ) ; IIIi11I11 = OooOo0oo0O0o00O . read ( )
   except : IIIi11I11 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IIIi11I11 ) )
   return
 I1i1I1II ( )
 I1i1I1II ( )
def iIIII ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 iIIIiiI1i1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIII , o0o0O , ooooO0oOoOOoO in os . walk ( iIIIiiI1i1i ) :
   I1i11i = 0
   I1i11i += len ( ooooO0oOoOOoO )
   if 11 - 11: I1IiiI / II111iiii + o0oOOo0O0Ooo * I1ii11iIi11i - I1ii11iIi11i - I1IiiI
   if 85 - 85: o0o0OOO0o0 % oOo00Oo00O / iIii1I11I1II1 . iIii1I11I1II1
   if I1i11i > 0 :
    if 31 - 31: o0oOOo0O0Ooo % OoO0O00
    OO0o = xbmcgui . Dialog ( )
    if OO0o . yesno ( "Delete Package Cache Files" , str ( I1i11i ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: oOo00Oo00O / oOo00Oo00O % I1iii
     for OooOo0oo0O0o00O in ooooO0oOoOOoO :
      os . unlink ( os . path . join ( iIII , OooOo0oo0O0o00O ) )
     for ooO in o0o0O :
      shutil . rmtree ( os . path . join ( iIII , ooO ) )
     OO0o = xbmcgui . Dialog ( )
     OO0o . ok ( oo00 , "       Deleting Packages all done" )
    else :
     pass
   else :
    OO0o = xbmcgui . Dialog ( )
    OO0o . ok ( oo00 , "       No Packages to DELETE" )
 except :
  OO0o = xbmcgui . Dialog ( )
  OO0o . ok ( oo00 , "Error Deleting Packages please visit The Support Group, Genie Music on facebook" )
 ii ( url )
 return
def ii ( url ) :
 OO0O0Ooo = os . path . join ( i1 , 'addon_data' )
 oOoO0 = [
 ( OO0O0Ooo ) ,
 ( i11 ) ,
 ( os . path . join ( o0oOoO00o , 'cache' ) ) ,
 ( os . path . join ( o0oOoO00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( i11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( i11 , 'plugin.video.GenieMusic' , 'Images' ) ) ,
 ( os . path . join ( OO0O0Ooo , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OO0O0Ooo , 'plugin.video.GenieMusic' , 'Images' ) ) ]
 if 77 - 77: iIii1I11I1II1 . o0O0 % o0O0 + i11iIiiIii
 Oo00o0OO0O00o = 0
 if 82 - 82: o0o0OOO0o0 + OoooooooOO - i1IIi . i1IIi
 for iIi1i in oOoO0 :
  if os . path . exists ( iIi1i ) and not iIi1i in [ i11 , OO0O0Ooo ] :
   for iIII , o0o0O , ooooO0oOoOOoO in os . walk ( iIi1i ) :
    I1i11i = 0
    I1i11i += len ( ooooO0oOoOOoO )
    if I1i11i > 0 :
     for OooOo0oo0O0o00O in ooooO0oOoOOoO :
      if not OooOo0oo0O0o00O in oOOoo00O0O :
       try :
        os . unlink ( os . path . join ( iIII , OooOo0oo0O0o00O ) )
       except :
        pass
      else : o0oO0oooOoo ( 'Ignore Log File: %s' % OooOo0oo0O0o00O )
     for ooO in o0o0O :
      try :
       shutil . rmtree ( os . path . join ( iIII , ooO ) )
       Oo00o0OO0O00o += 1
       o0oO0oooOoo ( "[Success] cleared %s files from %s" % ( str ( I1i11i ) , os . path . join ( iIi1i , ooO ) ) )
      except :
       o0oO0oooOoo ( "[Failed] to wipe cache in: %s" % os . path . join ( iIi1i , ooO ) )
  else :
   for iIII , o0o0O , ooooO0oOoOOoO in os . walk ( iIi1i ) :
    for ooO in o0o0O :
     if 'cache' in ooO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iIII , ooO ) )
       Oo00o0OO0O00o += 1
       o0oO0oooOoo ( "[Success] wiped %s " % os . path . join ( iIi1i , ooO ) )
      except :
       o0oO0oooOoo ( "[Failed] to wipe cache in: %s" % os . path . join ( iIi1i , ooO ) )
       if 27 - 27: I11i1I * I1iii . OO0oo0oOO % o0 * o0 . i1IIi
 oO00ooooO0o ( oo00 , 'Clear Cache: Removed %s Files' % Oo00o0OO0O00o )
def O0OOoOOO0oO ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 iIIIiiI1i1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIII , o0o0O , ooooO0oOoOOoO in os . walk ( iIIIiiI1i1i ) :
   I1i11i = 0
   I1i11i += len ( ooooO0oOoOOoO )
   if 28 - 28: I1iii + i11iIiiIii / o0o0OOO0o0 % OoOoOO00 % Oo0Ooo - O0
   if 54 - 54: i1IIi + II111iiii
   if I1i11i > 0 :
    if 83 - 83: I1ii11iIi11i - I1IiiI + I11i1I
    OO0o = xbmcgui . Dialog ( )
    if OO0o . yesno ( "Delete Package Cache Files" , str ( I1i11i ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: IIII
     for OooOo0oo0O0o00O in ooooO0oOoOOoO :
      os . unlink ( os . path . join ( iIII , OooOo0oo0O0o00O ) )
     for ooO in o0o0O :
      shutil . rmtree ( os . path . join ( iIII , ooO ) )
     OO0o = xbmcgui . Dialog ( )
     OO0o . ok ( oo00 , "       Deleting Packages all done" )
    else :
     pass
   else :
    OO0o = xbmcgui . Dialog ( )
    OO0o . ok ( oo00 , "       No Packages to DELETE" )
 except :
  OO0o = xbmcgui . Dialog ( )
  OO0o . ok ( oo00 , "Error Deleting Packages" )
 return
 if 46 - 46: o0
def ii1iIi1iIiI1i ( ) :
 OO0o = xbmcgui . Dialog ( )
 ii11IIII11I = OO0o . yesno ( 'Force Close Genie Music' , 'You are about to close Genie Music' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if ii11IIII11I == 0 : return
 elif ii11IIII11I == 1 : pass
 iiI1iIii1i = Ii ( )
 o0oO0oooOoo ( "Platform: " + str ( iiI1iIii1i ) )
 os . _exit ( 1 )
 o0oO0oooOoo ( "Force close failed!  Trying alternate methods." )
 if iiI1iIii1i == 'osx' :
  o0oO0oooOoo ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OO0o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iiI1iIii1i == 'linux' :
  o0oO0oooOoo ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  OO0o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iiI1iIii1i == 'android' :
  o0oO0oooOoo ( "############ try android force close #################" )
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
  OO0o . ok ( oo00 , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif iiI1iIii1i == 'windows' :
  o0oO0oooOoo ( "############ try windows force close #################" )
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
  OO0o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  o0oO0oooOoo ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  o0oO0oooOoo ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  OO0o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 70 - 70: OoO0O00 * O0 . o0o0OOO0o0 + I1IiiI . o0
def O000oo ( url ) :
 import urlresolver
 try :
  Ii1iIiII1Ii = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( Ii1iIiII1Ii , xbmcgui . ListItem ( o00OO00OoO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( o00OO00OoO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def Ii ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 42 - 42: O0 * IIII . Oo0Ooo - I1IiiI * iIii1I11I1II1
def o0oO0oooOoo ( log ) :
 xbmc . log ( "[%s]: %s" % ( oo00 , log ) )
 if not os . path . exists ( i11 ) : os . makedirs ( i11 )
 if not os . path . exists ( i1iIIi1 ) : OooOo0oo0O0o00O = open ( i1iIIi1 , 'w' ) ; OooOo0oo0O0o00O . close ( )
 with open ( i1iIIi1 , 'a' ) as OooOo0oo0O0o00O :
  iII111Ii = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OooOo0oo0O0o00O . write ( iII111Ii . rstrip ( '\r\n' ) + '\n' )
  if 52 - 52: II111iiii % o0 . OoOoOO00 * iIii1I11I1II1
def I111i1II ( ) :
 try :
  O0ooooo0OOOO0 = getSet ( "core-player" )
  if ( O0ooooo0OOOO0 == 'DVDPLAYER' ) : IiiIi1III = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0ooooo0OOOO0 == 'MPLAYER' ) : IiiIi1III = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0ooooo0OOOO0 == 'PAPLAYER' ) : IiiIi1III = xbmc . PLAYER_CORE_PAPLAYER
  else : IiiIi1III = xbmc . PLAYER_CORE_AUTO
 except : IiiIi1III = xbmc . PLAYER_CORE_AUTO
 return IiiIi1III
 return True
 if 84 - 84: I11i1I . o0O0 % O0 . OoOoOO00 + oOo00Oo00O
 if 31 - 31: iIii1I11I1II1 % o0o0OOO0o0 % I1iii . IIII - o0o0OOO0o0
def o00O ( name , url , mode , iconimage , fanart , description ) :
 if 17 - 17: IIII
 o0oOOoooOOOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1ii1IiIII = True
 o0O0o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0o0 . setProperty ( "Fanart_Image" , fanart )
 Ii1ii1IiIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOoooOOOOo , listitem = o0O0o0 , isFolder = True )
 return Ii1ii1IiIII
 if 57 - 57: iIii1I11I1II1 / o0o0OOO0o0 - i1IIi
def OOO0OOO00oo ( name , url , mode , iconimage , fanart , description ) :
 if 51 - 51: o0
 o0oOOoooOOOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1ii1IiIII = True
 o0O0o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0o0 . setProperty ( "Fanart_Image" , fanart )
 Ii1ii1IiIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOoooOOOOo , listitem = o0O0o0 , isFolder = False )
 return Ii1ii1IiIII
def ii1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0oOOoooOOOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1ii1IiIII = True
 o0O0o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0o0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii11I1 = [ ]
  if showcontext == 'fav' :
   ii11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Ooo :
   ii11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0O0o0 . addContextMenuItems ( ii11I1 )
 Ii1ii1IiIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOoooOOOOo , listitem = o0O0o0 , isFolder = False )
 return Ii1ii1IiIII
 if 75 - 75: OoO0O00 / II111iiii % O0
def oOo0OOoO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oOOoooOOOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1ii1IiIII = True
 o0O0o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii11I1 = [ ]
  ii11I1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Ooo :
   ii11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0O0o0 . addContextMenuItems ( ii11I1 )
 Ii1ii1IiIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOoooOOOOo , listitem = o0O0o0 , isFolder = True )
 return Ii1ii1IiIII
def Ooo0OOoOoO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oOOoooOOOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1ii1IiIII = True
 o0O0o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii11I1 = [ ]
  ii11I1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Ooo :
   ii11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0O0o0 . addContextMenuItems ( ii11I1 )
 Ii1ii1IiIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOoooOOOOo , listitem = o0O0o0 , isFolder = False )
 return Ii1ii1IiIII
 if 38 - 38: OoooooooOO * I1iii % O0 * OoOoOO00
def IIiiI ( ) :
 III1i11 = [ ]
 iiI111 = sys . argv [ 2 ]
 if len ( iiI111 ) >= 2 :
  I1iIiIi11i11 = sys . argv [ 2 ]
  O0ooo0 = I1iIiIi11i11 . replace ( '?' , '' )
  if ( I1iIiIi11i11 [ len ( I1iIiIi11i11 ) - 1 ] == '/' ) :
   I1iIiIi11i11 = I1iIiIi11i11 [ 0 : len ( I1iIiIi11i11 ) - 2 ]
  I1iii11 = O0ooo0 . split ( '&' )
  III1i11 = { }
  for ooo0O in range ( len ( I1iii11 ) ) :
   iII1iii = { }
   iII1iii = I1iii11 [ ooo0O ] . split ( '=' )
   if ( len ( iII1iii ) ) == 2 :
    III1i11 [ iII1iii [ 0 ] ] = iII1iii [ 1 ]
    if 12 - 12: I11i1I
 return III1i11
 if 83 - 83: o0O0 . O0 / Oo0Ooo / I11i1I - II111iiii
 if 100 - 100: OoO0O00
I1iIiIi11i11 = IIiiI ( )
O0o0O00Oo0o0 = None
o00OO00OoO = None
II1i = None
Ii1IIIIi1ii1I = None
o0O = None
IiiIiI1Ii1i = None
i1iIi = None
if 30 - 30: O0 - iIii1I11I1II1 / OoooooooOO
if 89 - 89: o0O0 - I1iii % Oo0Ooo % o0oOOo0O0Ooo
try :
 i1iIi = int ( I1iIiIi11i11 [ "fav_mode" ] )
except :
 pass
 if 49 - 49: Oo0Ooo - I1IiiI / o0 / O0 % o0oOOo0O0Ooo * IIII
try :
 O0o0O00Oo0o0 = urllib . unquote_plus ( I1iIiIi11i11 [ "url" ] )
except :
 pass
try :
 o00OO00OoO = urllib . unquote_plus ( I1iIiIi11i11 [ "name" ] )
except :
 pass
try :
 Ii1IIIIi1ii1I = urllib . unquote_plus ( I1iIiIi11i11 [ "iconimage" ] )
except :
 pass
try :
 II1i = int ( I1iIiIi11i11 [ "mode" ] )
except :
 pass
try :
 o0O = urllib . unquote_plus ( I1iIiIi11i11 [ "fanart" ] )
except :
 pass
try :
 IiiIiI1Ii1i = urllib . unquote_plus ( I1iIiIi11i11 [ "description" ] )
except :
 pass
 if 100 - 100: I11i1I . o0O0 / O0 * i1IIi * IIII * Oo0Ooo
 if 84 - 84: I1ii11iIi11i / I11i1I % i11iIiiIii * OO0oo0oOO % I1ii11iIi11i - OoooooooOO
print str ( Oo0oO0ooo ) + ': ' + str ( iIiiiI )
print "Mode: " + str ( II1i )
print "URL: " + str ( O0o0O00Oo0o0 )
print "Name: " + str ( o00OO00OoO )
print "IconImage: " + str ( Ii1IIIIi1ii1I )
if 99 - 99: I1IiiI + O0 + i1IIi / i11iIiiIii - i1IIi * iIii1I11I1II1
if 72 - 72: I1IiiI * I1ii11iIi11i . IIII * o0 * Oo0Ooo * OO0oo0oOO
def O0ooO0Oo00o ( content , viewType ) :
 if 40 - 40: I1IiiI
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 14 - 14: OO0oo0oOO
  if 80 - 80: OoooooooOO - I11i1I * IIII * I1ii11iIi11i / I1IiiI / I11i1I
if II1i == None : O0ooOooooO ( )
elif II1i == 1000 : OO0Oooo0oOO0O ( O0o0O00Oo0o0 )
elif II1i == 1 : Genres ( )
elif II1i == 2 : Lists ( O0o0O00Oo0o0 , Ii1IIIIi1ii1I )
elif II1i == 3 : all_mov ( )
elif II1i == 5 : II1III ( )
elif II1i == 6 : O0OOoOOO0oO ( O0o0O00Oo0o0 )
elif II1i == 7 : ii ( O0o0O00Oo0o0 )
elif II1i == 8 : ii1iIi1iIiI1i ( )
elif II1i == 9 : IiI111111IIII ( O0o0O00Oo0o0 )
elif II1i == 10 : Search2 ( )
elif II1i == 11 : oOooOo0 ( )
elif II1i == 12 : i1Ii ( O0o0O00Oo0o0 )
elif II1i == 13 : OooOoOO0 ( )
elif II1i == 14 : DJing2 ( O0o0O00Oo0o0 )
elif II1i == 15 : OOooo0O00o ( O0o0O00Oo0o0 )
if 13 - 13: OO0oo0oOO * I1iii + i11iIiiIii * OO0oo0oOO - I1iii
elif II1i == 16 : oO00OOoO00 ( )
elif II1i == 222 : O000oo ( O0o0O00Oo0o0 )
elif II1i == 18 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
elif II1i == 20 : Oo0OoO00oOO0o ( )
elif II1i == 21 : oo0OooOOo0 ( O0o0O00Oo0o0 , IiiIiI1Ii1i )
elif II1i == 22 : OOOO0OOoO0O0 ( O0o0O00Oo0o0 , IiiIiI1Ii1i )
elif II1i == 23 : O0Oo000ooO00 ( O0o0O00Oo0o0 , IiiIiI1Ii1i )
elif II1i == 24 : Oo0oOOo ( O0o0O00Oo0o0 , IiiIiI1Ii1i )
elif II1i == 25 : i1IiIiiI ( )
elif II1i == 50000 : oo0o ( )
elif II1i == 50001 : OoOooOoO ( )
elif II1i == 50002 : i1iI1 ( O0o0O00Oo0o0 )
elif II1i == 210 : OO0oOoOO0oOO0 ( O0o0O00Oo0o0 )
elif II1i == 212 : oooooOoo0ooo ( O0o0O00Oo0o0 , IiiIiI1Ii1i )
elif II1i == 211 : O0ii1ii1ii ( O0o0O00Oo0o0 )
elif II1i == 8043 : yt . PlayVideo ( O0o0O00Oo0o0 )
elif II1i == 7050 : oo0oO ( O0o0O00Oo0o0 )
elif II1i == 7051 : IiII111i1i11 ( O0o0O00Oo0o0 )
elif II1i == 7052 : yt . PlayVideo ( O0o0O00Oo0o0 )
elif II1i == 70511 : i111iIi1i1II1 ( O0o0O00Oo0o0 )
elif II1i == 70001 : ooo ( )
elif II1i == 70002 : o0oooOO00 ( O0o0O00Oo0o0 )
elif II1i == 70003 : iiIiii1IIIII ( O0o0O00Oo0o0 )
elif II1i == 70004 : o00o ( O0o0O00Oo0o0 )
elif II1i == 70005 : IIIIiiIiiI ( O0o0O00Oo0o0 )
elif II1i == 70006 : IIIIiI11I11 ( )
elif II1i == 90037 : oO00Oo0O0o ( O0o0O00Oo0o0 )
elif II1i == 900377 : oooOo0OOOoo0 ( O0o0O00Oo0o0 )
if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * o0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
