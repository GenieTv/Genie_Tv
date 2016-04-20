# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle
from imports import yt
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
from imports import extract
from imports import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
from imports import Parse , CNF_Studio_Indexer
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
from imports . tvGuide import gui
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
O00ooOO = "2.6.13"
I1iII1iiII = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
I1i1iiI1 = 'plugin.video.GenieTv'
iiIIIII1i1iI = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
o0oO0 = xbmcaddon . Addon ( id = I1i1iiI1 )
oo00 = xbmc . translatePath ( 'special://home/media' )
o00 = 'plugin.video.GenieTv'
Oo0oO0ooo = xbmcgui . DialogProgress ( )
o0oOoO00o = "[COLORgreen]GenieTv[/COLOR]"
i1 = Net ( )
oOOoo00O0O = xbmcgui . Dialog ( )
i1111 = base64 . decodestring
i11 = o0oO0 . getSetting ( 'Build' )
I11 = o0oO0 . getSetting ( 'Local' )
Oo0o0000o0o0 = o0oO0 . getSetting ( 'Remote' )
oOo0oooo00o = o0oO0 . getSetting ( 'LocalM3u' )
oO0o0o0ooO0oO = o0oO0 . getSetting ( 'User' )
oo0o0O00 = o0oO0 . getSetting ( 'Pass' )
oO = o0oO0 . getSetting ( 'AdultPass' )
i1iiIIiiI111 = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'fanart.jpg' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'icon.png' , i1iiIII111ii , '' ) )
ii11iIi1I = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
iI111I11I1I1 = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
OOooO0OOoo = xbmc . translatePath ( 'special://database' )
iIii1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
oOOoO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
O0OoO000O0OO = "GenieTv"
iiI1IiI = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
ooOoOoo0O = 'http://'
OooO0 = base64 . decodestring ( 'LnBocA==' )
II11iiii1Ii = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
OO0o = [ ]
Ooo = o0oO0 . getLocalizedString
O0o0Oo = CookieJar ( )
Oo00OOOOO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0o0Oo ) )
Oo00OOOOO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O0O = int ( sys . argv [ 1 ] )
O00o0OO = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
I11i1 = os . path . join ( O00o0OO , 'favorites' )
iIi1ii1I1 = iIii1 + '/addons.ini'
o0 = xbmc . translatePath ( 'special://home/userdata/' )
I11II1i = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIIII = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv/united' )
ooooooO0oo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( I11i1 ) == True :
 OOOO = open ( I11i1 ) . read ( )
else : OOOO = [ ]
OOO00 = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
 if 21 - 21: ii - Ii11I
def OOO0OOO00oo ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  Iii111II = 'genie tv repo not being installed '
  iiii11I ( Iii111II )
 if not os . path . exists ( IIIII ) :
  Ooo0OO0oOO ( )
  os . makedirs ( IIIII )
 ii11i1 ( )
 IIIii1II1II ( )
 i1I1iI ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( '[COLORgreen]Genie TV currently offline[/COLOR]' , iiI1IiI , 100000 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 92 - 92: oOo00oOO0O . oO0O0ooO0Oo * oOOoo0Oo
def Ooo0OO0oOO ( ) :
 o00OO00OoO ( 'Together we stand' , 'Genie is standing with all developers who work hard to create great addons for you all to enjoy for free, whatever you may think a lot of time goes in creating addons, any respect and aknowledgement should go to the rightful place.\n\n As a result of a few peoples actions the content that is and always will be freely available on Genie Tv, for now, is offline.' )
 if 60 - 60: I1IIiI1 * O00Oo000ooO0 + oO0 * Ii11I + i11iIiiIii * oO0O0ooO0Oo
 if 30 - 30: OOooOOo . oO0O0ooO0Oo - OoooooooOO
def Ii1iIiii1 ( ) :
 i1I1iI ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  i1I1iI ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  i1I1iI ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
def Oo0oOOo ( ) :
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  i1I1iI ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  oo0OooOOo0 ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 58 - 58: OoOoOO00 * Ii11I * ii11ii1ii / Ii11I
 if 75 - 75: ii
def I1III ( ) :
 i1I1iI ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  i1I1iI ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  i1I1iI ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  i1I1iI ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  i1I1iI ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
def OO0O0OoOO0 ( ) :
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  i1I1iI ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  i1I1iI ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  i1I1iI ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  i1I1iI ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  i1I1iI ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  i1I1iI ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
 if 10 - 10: OoooooooOO % iIii1I11I1II1
def O00o0O00 ( ) :
 i1I1iI ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 34 - 34: oO0
 if 15 - 15: oOo00oOO0O * oO0 * Oo % i11iIiiIii % I1IiI - Ii11I
 if 68 - 68: O00Oo000ooO0 % i1IIi . I1IIiI1 . ii11ii1ii
def o0oo0oOo ( ) :
 i1I1iI ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  i1I1iI ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  i1I1iI ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  i1I1iI ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
def o000O0o ( ) :
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  i1I1iI ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  i1I1iI ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  i1I1iI ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  i1I1iI ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
 if 42 - 42: I1IiI
 if 41 - 41: Oo . oO0 + O0 * OOooOOo % Oo * Oo
 if 19 - 19: oOOoo0Oo
def IIIii1II1II ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( 'http://architects.x10host.com/wizarddelete.txt' )
 Iiii = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( IIi1iiIi1 )
 for OO0OoO0o00 in Iiii :
  print OO0OoO0o00
  OO0OoO0o00 = ( str ( OO0OoO0o00 ) )
  if os . path . exists ( xbmc . translatePath ( OO0OoO0o00 ) ) :
   ooOO0O0ooOooO = os . path . join ( o0 , 'guisettings.xml' )
   oOOOo00O00oOo = open ( ooOO0O0ooOooO , "w+" )
   if 34 - 34: O0 + Ii11I + Oo
   oOOOo00O00oOo . write ( r'.' )
   I1 ( )
  else :
   pass
   if 10 - 10: oOo00oOO0O
def ii11i1 ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( 'http://architects.x10host.com/testdelete.txt' )
 Iiii = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIi1iiIi1 )
 for Iii111II in Iiii :
  Iii111II = ( str ( Iii111II ) )
  if os . path . exists ( xbmc . translatePath ( Iii111II ) ) :
   iiii11I ( Iii111II )
   OOooOO000 ( )
  else :
   pass
   if 97 - 97: ii11ii1ii + Ii11I / iIii1I11I1II1 / oOOoo0Oo
def iiii11I ( addon ) :
 addon = ( addon ) . replace ( 'special://home/addons/' , '' )
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 ooOO0O0ooOooO = os . path . join ( II , 'default.py' )
 oOOOo00O00oOo = open ( ooOO0O0ooOooO , "w+" )
 if 37 - 37: oOOoo0Oo - oO0 * ii % i11iIiiIii - O00Oo000ooO0
 oOOOo00O00oOo . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oOOOo00O00oOo . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oOOOo00O00oOo . write ( r'Please remove ' + addon + ' if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 83 - 83: oOo00oOO0O / OOOo0
 if 34 - 34: I1IIiI1
def I1 ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 oOo = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO00Oo , oOo in oOo :
  oOO00Oo = oOO00Oo
  Iiii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oOo ) )
  for i1iIIIi1i , iI1iIIiiii in Iiii :
   o00OO00OoO ( oOO00Oo , i1iIIIi1i , iI1iIIiiii )
   if 26 - 26: oOo00oOO0O . OoooooooOO
   if 39 - 39: oOOoo0Oo - O0 % i11iIiiIii * O00Oo000ooO0 . I1IIiI1
   if 58 - 58: Ooo00oOo00o % i11iIiiIii . oOOoo0Oo / ii
   if 84 - 84: oOOoo0Oo . ii11ii1ii / Oo - OOOo0 / OoooooooOO / OOooOOo
   if 12 - 12: OOOo0 * oOOoo0Oo % i1IIi % iIii1I11I1II1
   if 20 - 20: Ii11I % oO0O0ooO0Oo / oO0O0ooO0Oo + oO0O0ooO0Oo
   if 45 - 45: ii - I1IIiI1 - OoooooooOO - Ooo00oOo00o . OoOoOO00 / O0
   if 51 - 51: O0 + oOOoo0Oo
   if 8 - 8: ii * I1IiI - oO0O0ooO0Oo - Ooo00oOo00o * Ii11I % OOOo0
   if 48 - 48: O0
   if 11 - 11: oOo00oOO0O + OoooooooOO - Ooo00oOo00o / OOooOOo + Oo . OoOoOO00
   if 41 - 41: oO0O0ooO0Oo - O0 - O0
   if 68 - 68: Ii11I % O00Oo000ooO0
   if 88 - 88: iIii1I11I1II1 - oO0 + Ii11I
   if 40 - 40: OOOo0 * oO0O0ooO0Oo + Ii11I % oOOoo0Oo
   if 74 - 74: ii - Oo + OoooooooOO + O00Oo000ooO0 / I1IiI
   if 23 - 23: O0
def o00oO0oOo00 ( ) :
 i1I1iI ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 i1I1iI ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 i1I1iI ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 i1I1iI ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 81 - 81: Ooo00oOo00o
def IIi1 ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOO000 = 'http://imoviemax.se/?s=' + ( I1I1I ) . replace ( ' ' , '+' )
 i1Ii11i1i = OoOO000 . lower ( )
 o0oOOoo ( i1Ii11i1i )
def oOo00O0oo00o0 ( url ) :
 iiOOooooO0Oo = [ ]
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i , OO in Iiii :
  if i1iIIIi1i in iiOOooooO0Oo :
   pass
  else :
   i1I1iI ( i1iIIIi1i + ' - ' + OO + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   iiOOooooO0Oo . append ( i1iIIIi1i )
   if 25 - 25: Ooo00oOo00o
def oOo0oO ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i , OOOO0oo0 in Iiii :
  i1I1iI ( i1iIIIi1i + ' - Views:' + OOOO0oo0 , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 35 - 35: oO0O0ooO0Oo - OOOo0 % OOooOOo . OoooooooOO % oO0O0ooO0Oo
  if 47 - 47: oOOoo0Oo - oO0O0ooO0Oo . OoOoOO00 + OoooooooOO . i11iIiiIii
def o0oOOoo ( url ) :
 OOo0oO00ooO00 = [ ]
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIi1iiIi1 )
 for next in next :
  i1I1iI ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 Iiii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , i1iIIIi1i , url in Iiii :
  i1I1iI ( i1iIIIi1i , url , 10075 , oOO0O00oO0Ooo , oOO0O00oO0Ooo , '' )
  OOo0oO00ooO00 . append ( i1iIIIi1i )
  if 67 - 67: Ooo00oOo00o - Ii11I
def iI1i11iII111 ( img , name , url ) :
 img = img
 name = name
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( IIi1iiIi1 )
 for Iii1IIII11I , url in Iiii :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  OOOoo0OO = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + OOOoo0OO
  oO0o0 = ( Iii1IIII11I ) . replace ( 'play-' , 'Server ' )
  oo0OooOOo0 ( oO0o0 , OOOoo0OO , 10076 , img , img , '' )
  if 50 - 50: I1IIiI1
def Ii11iIi ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( IIi1iiIi1 )
 for O00O0Oooo0oO in Iiii :
  if '=m' in O00O0Oooo0oO :
   IIii11I1 ( O00O0Oooo0oO )
  elif 'php' in O00O0Oooo0oO :
   Ii11iIi ( url )
  else :
   IIi1iiIi1 = iii1i1iiiiIi ( O00O0Oooo0oO )
   Iiii = re . compile ( 'content="(.+?)">' ) . findall ( IIi1iiIi1 )
   for oOO0O00Oo0O0o in Iiii :
    IIii11I1 ( O00O0Oooo0oO )
    if 13 - 13: OoooooooOO
    if 33 - 33: O00Oo000ooO0 + oOOoo0Oo * ii / iIii1I11I1II1 - OOOo0
    if 54 - 54: O00Oo000ooO0 / Ii11I . ii % oOOoo0Oo
def OoO0OOOOo0O ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 OooOO = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO00Oo , I1111 in OooOO :
  print 'there ><><><><><><><><><><><><'
  oOO00Oo = oOO00Oo
  Iiii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I1111 ) )
  for i1iIIIi1i , iI1iIIiiii in Iiii :
   print 'here <><><><><><><><><><><><>'
   i1I1iI ( '[COLORred]' + oOO00Oo + '[/COLOR] - ' + i1iIIIi1i + ' - [COLORgreen]' + iI1iIIiiii + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 oOo = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO00Oo , iiIiiiiI in oOo :
  print 'there ><><><><><><><><><><><><'
  oOO00Oo = oOO00Oo
  Iiii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iiIiiiiI ) )
  for i1iIIIi1i , iI1iIIiiii in Iiii :
   print 'here <><><><><><><><><><><><>'
   i1I1iI ( '[COLORred]' + oOO00Oo + '[/COLOR] - ' + i1iIIIi1i + ' - [COLORgreen]' + iI1iIIiiii + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 62 - 62: OoooooooOO * OOOo0
   if 58 - 58: I1IiI % OOooOOo
   if 50 - 50: O00Oo000ooO0 . OOooOOo
def ooO0OO ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 oOo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOo in oOo :
  i1iIIIi1i = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oOo ) )
  for i1iIIIi1i in i1iIIIi1i :
   i1iIIIi1i = ( i1iIIIi1i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oOo ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  O000OOO = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oOo ) )
  for O000OOO in O000OOO :
   O000OOO = 'http:' + O000OOO
  oo0OooOOo0 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO , '' , '' )
  if 20 - 20: OOooOOo . OoOoOO00 % Ii11I * iIii1I11I1II1
  if 98 - 98: OOOo0 % oO0O0ooO0Oo * OoooooooOO
  if 51 - 51: iIii1I11I1II1 . I1IiI / ii + OOooOOo
  if 33 - 33: oO0 . OoOoOO00 % oOOoo0Oo + OOooOOo
def oO00O000oO0 ( url ) :
 if 79 - 79: oOo00oOO0O - OoooooooOO - ii - iIii1I11I1II1 * Ii11I
 Iii = [ ]
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for O00O0Oooo0oO , oOO0O00oO0Ooo , i1iIIIi1i , I1111i in Iiii :
  i1iIIIi1i = ( i1iIIIi1i ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  iIIii = iii1i1iiiiIi ( O00O0Oooo0oO )
  o00O0O = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iIIii )
  for ii1iii1i , Iii1I1111ii in o00O0O :
   ooOoO00 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( Iii1I1111ii ) )
   for Ii1IIiI1i in ooOoO00 :
    if i1iIIIi1i in Iii :
     pass
    else :
     oo0OooOOo0 ( i1iIIIi1i , ii1iii1i , 8043 , oOO0O00oO0Ooo , oOO0O00oO0Ooo , Ii1IIiI1i )
     OOO ( 'movies' , 'INFO' )
     Iii . append ( i1iIIIi1i )
     if 78 - 78: ii11ii1ii
     if 93 - 93: I1IIiI1 * OoooooooOO + oO0
def IiII111i1i11 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for url , i1I1i111Ii , Ii1IIiI1i , ooo , i1iIIIi1i in Iiii :
  i1I1iI ( i1iIIIi1i , url , 10065 , i1I1i111Ii , ooo , Ii1IIiI1i )
 OOO ( 'movies' , 'INFO' )
 if 27 - 27: oO0 % OOOo0
def o0oooOO00 ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOO000 = 'https://www.youtube.com/results?search_query=' + ( I1I1I ) . replace ( ' ' , '+' )
 i1Ii11i1i = OoOO000 . lower ( )
 IIi1iiIi1 = iii1i1iiiiIi ( i1Ii11i1i )
 Iiii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII in next :
  iiIiii1IIIII = 'https://www.youtube.com' + iiIiii1IIIII
  i1I1iI ( '[COLORgreen] NEXT [/COLOR]' , iiIiii1IIIII , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for oOO0O00oO0Ooo , iiIiii1IIIII , i1iIIIi1i , o00o , Iii1I1111ii in Iiii :
  OO0o . append ( i1iIIIi1i )
  OOO ( 'tvshows' , 'INFO' )
  O000OOO = 'http:' + ( oOO0O00oO0Ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + O000OOO
  iiIiii1IIIII = 'http://www.youtube.com' + iiIiii1IIIII
  oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( iiIiii1IIIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO , O000OOO , Iii1I1111ii )
 else :
  Iiii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for oOO0O00oO0Ooo , iiIiii1IIIII , i1iIIIi1i , o00o in Iiii :
   print 'im doing it'
   OOO ( 'tvshows' , 'INFO' )
   O000OOO = 'http:' + ( oOO0O00oO0Ooo ) . replace ( 'https:' , '' )
   iiIiii1IIIII = 'http://www.youtube.com' + iiIiii1IIIII
   if '&' in iiIiii1IIIII :
    print ' i got here'
    IIi1iiIi1 = iii1i1iiiiIi ( iiIiii1IIIII )
    oOo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
    for oOo in oOo :
     i1iIIIi1i = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oOo ) )
     for i1iIIIi1i in i1iIIIi1i :
      i1iIIIi1i = ( i1iIIIi1i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     iiIiii1IIIII = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oOo ) )
     for iiIiii1IIIII in iiIiii1IIIII :
      iiIiii1IIIII = 'https://www.youtube.com/w' + iiIiii1IIIII
     O000OOO = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oOo ) )
     for O000OOO in O000OOO :
      O000OOO = 'http:' + O000OOO
     oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( iiIiii1IIIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO , i1iiIII111ii , '' )
   elif i1iIIIi1i in OO0o :
    pass
   elif 'user' in iiIiii1IIIII or 'elete' in i1iIIIi1i :
    pass
   elif 'hannel' in iiIiii1IIIII :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iiIiii1IIIII
    IIi1iiIi1 = iii1i1iiiiIi ( iiIiii1IIIII )
    IIIIiiIiiI = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
    for oOO0O00oO0Ooo , iiIiii1IIIII , i1iIIIi1i in IIIIiiIiiI :
     if 'outube' in iiIiii1IIIII or 'list' in iiIiii1IIIII :
      pass
     elif 'atch' in iiIiii1IIIII :
      iiIiii1IIIII = ( iiIiii1IIIII ) . replace ( '/watch?v=' , '' )
      oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( iiIiii1IIIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOO0O00oO0Ooo , 'http:' + oOO0O00oO0Ooo , '' )
     else :
      pass
   else :
    oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( iiIiii1IIIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO , O000OOO , '' )
    if 10 - 10: I1IiI % I1IiI - I1IiI . oOOoo0Oo
def o0OoOo00o0o ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIi1iiIi1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  i1I1iI ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for oOO0O00oO0Ooo , url , i1iIIIi1i , o00o , Iii1I1111ii in Iiii :
  OO0o . append ( i1iIIIi1i )
  OOO ( 'tvshows' , 'INFO' )
  O000OOO = 'http:' + ( oOO0O00oO0Ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + O000OOO
  url = 'http://www.youtube.com' + url
  oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO , O000OOO , Iii1I1111ii )
 else :
  Iiii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for oOO0O00oO0Ooo , url , i1iIIIi1i , o00o in Iiii :
   OOO ( 'tvshows' , 'INFO' )
   O000OOO = 'http:' + ( oOO0O00oO0Ooo ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIi1iiIi1 = iii1i1iiiiIi ( url )
    oOo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
    for oOo in oOo :
     i1iIIIi1i = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oOo ) )
     for i1iIIIi1i in i1iIIIi1i :
      i1iIIIi1i = ( i1iIIIi1i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oOo ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     O000OOO = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oOo ) )
     for O000OOO in O000OOO :
      O000OOO = 'http:' + O000OOO
     oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO , i1iiIII111ii , '' )
   elif i1iIIIi1i in OO0o :
    pass
   elif 'user' in url or 'elete' in i1iIIIi1i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIi1iiIi1 = iii1i1iiiiIi ( url )
    IIIIiiIiiI = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
    for oOO0O00oO0Ooo , url , i1iIIIi1i in IIIIiiIiiI :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOO0O00oO0Ooo , 'http:' + oOO0O00oO0Ooo , '' )
     else :
      pass
   else :
    oo0OooOOo0 ( '[COLORred]' + o00o + '[/COLOR]' + '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO , O000OOO , '' )
    if 41 - 41: oO0 % Ooo00oOo00o - Oo * O00Oo000ooO0 * Oo
    if 69 - 69: Ii11I - OoooooooOO + OOooOOo - oOo00oOO0O
def iiO0oOo00o ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  o0ooooO0o0O = open ( iIi1ii1I1 )
  Iiii = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( o0ooooO0o0O ) )
  for iiIi11iI1iii , oo000 in Iiii :
   if iiIi11iI1iii == 'needs replacing' or oo000 == 'needs replacing' :
    o0000oO ( )
  i1I1iI ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelist.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 15 - 15: I1IiI % OOOo0 * oOo00oOO0O
def O0OoooO0 ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 i1iiIIiiI111 . ok ( '[COLOR=red]Reset Any Previous linked streams[/COLOR]' , 'For best results you\'ll need to clear previous linked streams' , 'Go to TVGuide tab then reset database at the bottom' , 'Then go back and guide should be all linked up and ready to go' )
 o0oO0 . openSettings ( sys . argv [ 0 ] )
 o0000oO ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 85 - 85: oOo00oOO0O
def iI1i11II1i ( ) :
 try :
  o0o0OoOo0O0OO = gui . TVGuide ( )
  o0o0OoOo0O0OO . doModal ( )
  del o0o0OoOo0O0OO
  if 36 - 36: I1IiI - O0
 except :
  import sys
  import traceback as tb
  ( o0OOOooo0OOo , iII1i11IIi1i , traceback ) = sys . exc_info ( )
  tb . print_exception ( o0OOOooo0OOo , iII1i11IIi1i , traceback )
  if 73 - 73: OOooOOo * O0 - i11iIiiIii
def O0O0o0oOOO ( ) :
 i1I1iI ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( oOoOooOo0o0 ) :
  i1I1iI ( 'Backup Genie Favourites' , iiIiii1IIIII , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  i1I1iI ( 'Backup Ivue Config' , IIiiiiiiIi1I1 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( I1IIIii ) :
  i1I1iI ( 'Backup Kodi Favourites' , I1IIIii , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 67 - 67: I1IiI + ii11ii1ii . OOooOOo . OoOoOO00
  if 98 - 98: oOOoo0Oo
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . OOooOOo / OoOoOO00 % Oo
zip = o0oO0 . getSetting ( 'zip' )
i1i11I11 = xbmc . translatePath ( os . path . join ( zip ) )
def iiiiII1I ( ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * oOo00oOO0O % O0 + OoooooooOO
  if 25 - 25: I1IIiI1 + oO0O0ooO0Oo / oO0 . OOooOOo % O0 * Ooo00oOo00o
  if 84 - 84: oO0 % oO0O0ooO0Oo + i11iIiiIii
def II1I1Ii ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = oOoOooOo0o0
  elif 'Ivue' in name :
   url = IIiiiiiiIi1I1
  elif 'Kodi' in name :
   url = I1IIIii
  iiiiII1I ( )
  Ooo0O0oooo = open ( url ) . read ( )
  iiI = os . path . join ( i1i11I11 , description . split ( 'Your ' ) [ 1 ] )
  oOIIiIi = open ( iiI , mode = 'w' )
  oOIIiIi . write ( Ooo0O0oooo )
  oOIIiIi . close ( )
 else :
  if 'guisettings.xml' in description :
   OOoOooOoOOOoo = open ( os . path . join ( i1i11I11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iiii1iI1i = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   Iiii = re . compile ( Iiii1iI1i ) . findall ( OOoOooOoOOOoo )
   for type , I1ii1ii11i1I , o0OoOO in Iiii :
    o0OoOO = o0OoOO . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I1ii1ii11i1I , o0OoOO ) )
  else :
   iiI = os . path . join ( url )
   Ooo0O0oooo = open ( os . path . join ( i1i11I11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOIIiIi = open ( iiI , mode = 'w' )
   oOIIiIi . write ( Ooo0O0oooo )
   oOIIiIi . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 55 - 55: oO0 - oOo00oOO0O + OoOoOO00 + oOOoo0Oo % oO0O0ooO0Oo
 if 41 - 41: i1IIi - oOo00oOO0O - oO0O0ooO0Oo
 if 8 - 8: Ooo00oOo00o + O00Oo000ooO0 - OOooOOo % Oo % OOooOOo * ii
 if 9 - 9: Oo - i11iIiiIii - Ii11I * oO0O0ooO0Oo + oO0
def iIIII ( ) :
 iIIIiiI1i1i = 1
 iiiiII1I ( )
 iIII = xbmc . translatePath ( os . path . join ( i1i11I11 , 'Build Backup' , 'Full Backup' , '' ) )
 o0o0O = xbmc . translatePath ( os . path . join ( i1i11I11 , 'Build Backup' , 'my_full_backup.zip' ) )
 ooooO0oOoOOoO = xbmc . translatePath ( os . path . join ( i1i11I11 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iIII ) :
  os . makedirs ( iIII )
 I1i11i = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1i11i ) : return False , 0
 IiIi = I1i11i
 OOOOO0O00 = xbmc . translatePath ( os . path . join ( iIII , IiIi + '.zip' ) )
 IiiiIIiIiI1I1 = [ 'plugin.video.GenieTv' ]
 ooO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iiOO0O0Ooo = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oOoO0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 Oo0 = "Creating full backup of existing build"
 oo0O0o00o0O = "Creating Community Build"
 I11i1II = "Archiving..."
 OooiiIi1i = ""
 I1i11111i1i11 = "Please Wait"
 OOoOOO0 ( oooOOOOO , OOOOO0O00 , oo0O0o00o0O , I11i1II , OooiiIi1i , I1i11111i1i11 , iiOO0O0Ooo , oOoO0 )
 time . sleep ( 1 )
 I1I1i = xbmc . translatePath ( os . path . join ( iIII , IiIi + '_guisettings.zip' ) )
 I1IIIiIiIi = zipfile . ZipFile ( I1I1i , mode = 'w' )
 try :
  I1IIIiIiIi . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1IIIiIiIi . close ( )
 if iIIIiiI1i1i == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + o0o0O , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OOOOO0O00 + '[/COLOR]' )
  if 27 - 27: ii11ii1ii + I1IiI - Ii11I + O0 . oO0O0ooO0Oo
def OOoOOO0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iIi1i1iIi1iI = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iiIi1iI1iIii = len ( sourcefile )
 o00OooO0oo = [ ]
 o0o0oOoOO0O = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for i1ii1II1ii , iII111Ii , Ooo00OoOOO in os . walk ( sourcefile ) :
  for file in Ooo00OoOOO :
   o0o0oOoOO0O . append ( file )
 Oo0OO0000oooo = len ( o0o0oOoOO0O )
 for i1ii1II1ii , iII111Ii , Ooo00OoOOO in os . walk ( sourcefile ) :
  iII111Ii [ : ] = [ IIII1iII for IIII1iII in iII111Ii if IIII1iII not in exclude_dirs ]
  Ooo00OoOOO [ : ] = [ oOIIiIi for oOIIiIi in Ooo00OoOOO if oOIIiIi not in exclude_files ]
  for file in Ooo00OoOOO :
   o00OooO0oo . append ( file )
   ii1III11 = len ( o00OooO0oo ) / float ( Oo0OO0000oooo ) * 100
   Oo0oO0ooo . update ( int ( ii1III11 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1iiIIIi11 = os . path . join ( i1ii1II1ii , file )
   if not 'temp' in iII111Ii :
    if not 'plugin.program.originwizard' in iII111Ii :
     import time
     Ii1I11ii1i = '01/01/1980'
     O0iIiIIIIIii = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1iiIIIi11 ) ) )
     if O0iIiIIIIIii > Ii1I11ii1i :
      iIi1i1iIi1iI . write ( I1iiIIIi11 , I1iiIIIi11 [ iiIi1iI1iIii : ] )
 iIi1i1iIi1iI . close ( )
 Oo0oO0ooo . close ( )
 if 58 - 58: OOooOOo / I1IIiI1 . I1IiI / OoooooooOO + O00Oo000ooO0
 if 86 - 86: oOo00oOO0O * OOOo0 + oOo00oOO0O + OoOoOO00
def i1i111iI ( ) :
 i1I1iI ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 29 - 29: ii11ii1ii / i1IIi . OOOo0 - I1IiI - I1IiI - oO0O0ooO0Oo
 if 20 - 20: i1IIi % Ooo00oOo00o . OOOo0 / I1IIiI1 * i11iIiiIii * Ii11I
def OOo ( ) :
 i1I1iI ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 50 - 50: oO0
 if 72 - 72: O00Oo000ooO0
 if 90 - 90: Oo % O0 * iIii1I11I1II1 . oOOoo0Oo
 if 8 - 8: oO0 + OoOoOO00 / oOOoo0Oo / oOo00oOO0O
def ooo0O ( ) :
 i1I1iI ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  i1I1iI ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 16 - 16: I1IiI
 OOO ( 'movies' , 'MAIN' )
 if 41 - 41: i1IIi * OoOoOO00 / OoooooooOO . Ii11I
def O0iII1 ( ) :
 if 27 - 27: Ooo00oOo00o . oOo00oOO0O + I1IiI / iIii1I11I1II1 % oOOoo0Oo . oO0
 oo0OooOOo0 ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 14 - 14: ii + ii11ii1ii - oOOoo0Oo / O0 . O00Oo000ooO0
 oo0OooOOo0 ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 i1I1iI ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
 if 45 - 45: O00Oo000ooO0
 if 83 - 83: I1IiI . OoooooooOO
def iI1Ii11111iIi ( ) :
 i1I1iI ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
 if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / I1IIiI1 / i11iIiiIii
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
def ii1 ( ) :
 oo0OooOOo0 ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
 if 53 - 53: oO0O0ooO0Oo % oO0O0ooO0Oo * OOooOOo + I1IiI
def Oooo00 ( ) :
 oo0OooOOo0 ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 6 - 6: oO0O0ooO0Oo - oO0 * Ii11I . oOOoo0Oo / O0 * oO0
def II11iI111i1 ( ) :
 oo0OooOOo0 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 95 - 95: OoooooooOO - I1IIiI1 * OOOo0 + I1IiI
 if 10 - 10: OOooOOo / i11iIiiIii
 if 92 - 92: oOo00oOO0O . O00Oo000ooO0
def oOO00O0Ooooo00 ( ) :
 i1I1iI ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
 if 97 - 97: oO0 / O00Oo000ooO0 % i1IIi % ii11ii1ii
def ii111I11iI ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( i11IIIiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 5 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 69 - 69: O0
def o0ooO ( ) :
 i1I1iI ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 OOO ( 'movies' , 'MAIN' )
 if 74 - 74: O0 * ii - i11iIiiIii + O00Oo000ooO0
def IiiI1iiiiI1iI ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + iIiiiii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 40 - 40: O0 - OoooooooOO - I1IIiI1
def iIiii ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + OOOO00OO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 48 - 48: O00Oo000ooO0
def O00Oo0o000oO ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + oO0o00oOOooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 79 - 79: Ooo00oOo00o - iIii1I11I1II1 + oO0O0ooO0Oo - O00Oo000ooO0
def OoO ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 35 - 35: I1IiI + i11iIiiIii - OoOoOO00
def Ii1ii111i1 ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + i1i1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 40 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 83 - 83: ii + OoooooooOO
def I111IiiIi1 ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + o00oIi1IIiiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 5 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 88 - 88: OoooooooOO + oOo00oOO0O * OoOoOO00 % Oo
def I1I1iIi11i1II ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , O000OOO , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , iiIiii1IIIII , 2031 , O000OOO )
  if 40 - 40: OOooOOo
def OOOooo ( name , url , description ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( Oo00oo0000OO , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0oOOo0Oo = os . path . join ( ooo00Ooo , name + '.apk' )
 try :
  os . remove ( O0oOOo0Oo )
 except :
  pass
 downloader . download ( url , O0oOOo0Oo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 73 - 73: oO0O0ooO0Oo - O00Oo000ooO0
def O00oooo00o0O ( url ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0oOOo0Oo = os . path . join ( ooo00Ooo , i1iIIIi1i + '.mp4' )
 try :
  os . remove ( O0oOOo0Oo )
 except :
  pass
 downloader . download ( url , O0oOOo0Oo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 9 - 9: OOOo0 % OOOo0 % OoOoOO00
 if 30 - 30: I1IIiI1 + O00Oo000ooO0 - I1IIiI1 . I1IIiI1 - OoOoOO00 + O0
def oOO0 ( name , url , description ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0oOOo0Oo = os . path . join ( ooo00Ooo , name )
 try :
  os . remove ( O0oOOo0Oo )
 except :
  pass
 downloader . download ( url , O0oOOo0Oo , Oo0oO0ooo )
 i1IIiIii1i = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print i1IIiIii1i
 print '======================================='
 extract . all ( O0oOOo0Oo , i1IIiIii1i , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 77 - 77: O0 % ii - Ooo00oOo00o
 if 97 - 97: OoooooooOO . i11iIiiIii + OOOo0
def oOo0OoOOo0 ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 5 , i1I1i111Ii , ooo , Iii1I1111ii )
 try :
  OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iII11I1Ii1 + oO0o0o0ooO0oO + o0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
  for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
   i1I1iI ( i1iIIIi1i , url , 5 , i1I1i111Ii , ooo , Iii1I1111ii )
 except : pass
 OOO ( 'movies' , 'INFO' )
 if 59 - 59: Ii11I + i11iIiiIii
 if 88 - 88: i11iIiiIii - oO0
def O0iIi1IiII ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 43 , i1I1i111Ii , ooo , Iii1I1111ii )
 try :
  OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iII11I1Ii1 + oO0o0o0ooO0oO + o0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
  for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
   i1I1iI ( i1iIIIi1i , url , 43 , i1I1i111Ii , ooo , Iii1I1111ii )
 except : pass
 OOO ( 'movies' , 'INFO' )
 if 27 - 27: oOOoo0Oo . oOo00oOO0O . iIii1I11I1II1 . iIii1I11I1II1
 if 20 - 20: OOooOOo / i1IIi
def oOIi111 ( name , url , description ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 O0oOOo0Oo = os . path . join ( ooo00Ooo , name + '.zip' )
 try :
  os . remove ( O0oOOo0Oo )
 except :
  pass
 downloader . download ( url , O0oOOo0Oo , Oo0oO0ooo )
 oO0i1iI = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0i1iI
 print '======================================='
 extract . all ( O0oOOo0Oo , oO0i1iI , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OOooOO000 ( )
 if 10 - 10: OoOoOO00 . oOOoo0Oo
 if 32 - 32: oO0O0ooO0Oo . I1IIiI1 . OoooooooOO - Ooo00oOo00o + ii
def ooO0oO00O0o ( name , url , description ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0oOOo0Oo = os . path . join ( ooo00Ooo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0oOOo0Oo )
 except :
  pass
 downloader . download ( url , O0oOOo0Oo , Oo0oO0ooo )
 oO0i1iI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0i1iI
 print '======================================='
 extract . all ( O0oOOo0Oo , oO0i1iI , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 ooOO00oOOo000 ( )
 if 14 - 14: Ooo00oOo00o . OoOoOO00 . oOo00oOO0O / oO0O0ooO0Oo % ii11ii1ii - oO0
def o0oOoO0O ( name , url , description ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0oOOo0Oo = os . path . join ( ooo00Ooo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0oOOo0Oo )
 except :
  pass
 downloader . download ( url , O0oOOo0Oo , Oo0oO0ooo )
 oO0i1iI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0i1iI
 print '======================================='
 extract . all ( O0oOOo0Oo , oO0i1iI , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 84 - 84: O0 * OoooooooOO - I1IIiI1 * I1IIiI1
 if 8 - 8: oO0 / i1IIi . ii
def i1I1IiI ( name , url , description ) :
 oO0i1iI = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 O0oOOo0Oo = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oO0i1iI
 print '======================================='
 extract . all ( O0oOOo0Oo , oO0i1iI , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 66 - 66: Ooo00oOo00o
 if 56 - 56: O0
def ooOO00oOOo000 ( ) :
 OOo00 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OOo00 == 0 :
  return
 elif OOo00 == 1 :
  pass
 iIIIIi1iI11iI1 = i11I1II ( )
 print "Platform: " + str ( iIIIIi1iI11iI1 )
 if iIIIIi1iI11iI1 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIIIIi1iI11iI1 == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIIIIi1iI11iI1 == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif iIIIIi1iI11iI1 == 'windows' :
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
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 79 - 79: Ooo00oOo00o . oOOoo0Oo * oO0O0ooO0Oo - Ii11I + oO0
def i11I1II ( ) :
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
  if 14 - 14: i11iIiiIii - oOOoo0Oo * I1IiI
  if 51 - 51: ii11ii1ii / iIii1I11I1II1 % ii + OOooOOo * oO0 + O00Oo000ooO0
  if 77 - 77: oO0 * I1IiI
def i1i1111IiI ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( url ) :
  for file in Ooo00OoOOO :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    OOoOooOoOOOoo = open ( ( os . path . join ( i1I1I1iiII , file ) ) ) . read ( )
    O00o00O = OOoOooOoOOOoo . replace ( oooOOOOO , 'special://home/' )
    oOIIiIi = open ( ( os . path . join ( i1I1I1iiII , file ) ) , mode = 'w' )
    oOIIiIi . write ( str ( O00o00O ) )
    oOIIiIi . close ( )
 ooOO00oOOo000 ( )
 if 3 - 3: Ii11I
def IiiO0o0o ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 Iiii = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , iiIiii1IIIII in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , iiIiii1IIIII , 222 , ii11iIi1I + 'radio.png' )
  if 32 - 32: OoOoOO00 . oO0O0ooO0Oo - oOOoo0Oo * O00Oo000ooO0
def OOO00oo0ooO ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Iiii = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://www.toonjet.com/' + iiIiii1IIIII , 8051 , ii11iIi1I + 'classictoons.png' )
def iiIii1ii ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo in Iiii :
  if 'ol.gif' in oOO0O00oO0Ooo :
   pass
  elif 'link_block_' in oOO0O00oO0Ooo :
   pass
  elif '.png' in oOO0O00oO0Ooo :
   pass
  else :
   ii1IIIIiI11 ( ( oOO0O00oO0Ooo ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in o00O0O :
  ii1IIIIiI11 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def iIIIII1iiiiII ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  O0Oo00oO0O00 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 54 - 54: i1IIi
  if 22 - 22: i1IIi + oO0O0ooO0Oo
def O0o0O0OO00o ( ) :
 OOo00O ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 OOo00O ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 81 - 81: I1IIiI1 . OOooOOo / O00Oo000ooO0
def Iii111Ii ( ) :
 OOo00O ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 OOo00O ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 OOo00O ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 54 - 54: oO0O0ooO0Oo * O00Oo000ooO0 - OoooooooOO % OOOo0 + O0
def IIiiIIIi ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( II11iiii1Ii + 'books' + OooO0 )
 Iiii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1iiIi1 )
 for i1iIIIi1i , iiIiii1IIIII , OO0O0o0o0 in Iiii :
  if 'Parent' in i1iIIIi1i :
   pass
  elif '2' in OO0O0o0o0 :
   OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiIiii1IIIII , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 31 - 31: oO0O0ooO0Oo
def iIIiI1I1i ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 IIi1iiIi1 = iii1i1iiiiIi ( II11iiii1Ii + 'books' + OooO0 )
 Iiii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1iiIi1 )
 for i1iIIIi1i , iiIiii1IIIII , OO0O0o0o0 in Iiii :
  if I1I1I in i1iIIIi1i . lower ( ) :
   if '1' in OO0O0o0o0 :
    OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiIiii1IIIII , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in OO0O0o0o0 :
    OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiIiii1IIIII , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in OO0O0o0o0 :
    OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiIiii1IIIII , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 68 - 68: oOo00oOO0O % O00Oo000ooO0 + ii11ii1ii - i11iIiiIii . OOooOOo - O00Oo000ooO0
    if 31 - 31: OOOo0 * ii + OoooooooOO - oOOoo0Oo / OoooooooOO
def I111IIiii1Ii ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( II11iiii1Ii + 'books' + OooO0 )
 Iiii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1iiIi1 )
 for i1iIIIi1i , iiIiii1IIIII , OO0O0o0o0 in Iiii :
  if '1' in OO0O0o0o0 :
   OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiIiii1IIIII , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in OO0O0o0o0 :
   OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiIiii1IIIII , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in OO0O0o0o0 :
   OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiIiii1IIIII , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 13 - 13: ii . OOOo0 * ii + OOOo0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: OOOo0 + i11iIiiIii + i1IIi / oOo00oOO0O
def I11iIiI1 ( url ) :
 O00O0Oooo0oO = url
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 o00O0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in o00O0O :
  if 'mp3' in i1iIIIi1i :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) , O00O0Oooo0oO + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in i1iIIIi1i :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) , O00O0Oooo0oO + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in i1iIIIi1i :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) , O00O0Oooo0oO + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in i1iIIIi1i :
   OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O00O0Oooo0oO + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 86 - 86: OOooOOo
   if 27 - 27: O0 . OOooOOo . ii11ii1ii . ii11ii1ii + ii11ii1ii * OOooOOo
   if 100 - 100: Oo % oO0O0ooO0Oo / oOo00oOO0O
def iIII11Ii ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 O00O0Oooo0oO = url
 Iiii = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  if 'Parent' in i1iIIIi1i :
   pass
  elif '.db' in i1iIIIi1i :
   pass
  elif '.jpg' in i1iIIIi1i :
   pass
  elif '.html' in i1iIIIi1i :
   pass
  elif '.doc' in i1iIIIi1i :
   pass
  elif 'mp3' in i1iIIIi1i :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O00O0Oooo0oO + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in i1iIIIi1i :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O00O0Oooo0oO + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   OOo00O ( ( i1iIIIi1i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O00O0Oooo0oO + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 52 - 52: O00Oo000ooO0 / oO0 - oOo00oOO0O
   if 49 - 49: I1IiI / Oo . i11iIiiIii
def IIIi1i ( ) :
 OOo00O ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 OOo00O ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 OOo00O ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 71 - 71: oOOoo0Oo % OOooOOo / Ii11I / Oo
def OO0OO0OO ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 Iiii = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo in Iiii :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iiIiii1IIIII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOO0O00oO0Ooo :
   pass
  else :
   OOo00O ( oOO0O00oO0Ooo , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iiIiii1IIIII ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOO0O00oO0Ooo + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 61 - 61: OoooooooOO . ii . OoooooooOO / Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: i1IIi
 if 82 - 82: I1IiI + OoooooooOO / i11iIiiIii * ii11ii1ii . OoooooooOO
def oooo0OOo ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  if '</a>' in i1iIIIi1i :
   pass
  elif '(' in i1iIIIi1i :
   OOo00O ( ( i1iIIIi1i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 72 - 72: O0 / oO0 + OoooooooOO * oOOoo0Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: OoooooooOO % OoOoOO00 - OOOo0 % ii11ii1ii + i1IIi
def i1II ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 IIi1iiIi1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Iiii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if I1I1I in i1iIIIi1i . lower ( ) :
   if '</a>' in i1iIIIi1i :
    pass
   elif '(' in i1iIIIi1i :
    OOo00O ( ( i1iIIIi1i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiIiii1IIIII , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    i1I1iI ( ( i1iIIIi1i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiIiii1IIIII , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 15 - 15: I1IiI
    if 62 - 62: oO0O0ooO0Oo
def ooO000O ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Iiii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if '</a>' in i1iIIIi1i :
   pass
  elif '(' in i1iIIIi1i :
   OOo00O ( ( i1iIIIi1i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiIiii1IIIII , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiIiii1IIIII , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 53 - 53: OOooOOo . oOOoo0Oo / oO0O0ooO0Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: oO0O0ooO0Oo % O0 % I1IiI . i1IIi
 if 86 - 86: Ooo00oOo00o * OoooooooOO
def OooO0oOo ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( IIi1iiIi1 )
 for url in Iiii :
  O00O0Oooo0oO = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( O00O0Oooo0oO )
  if 66 - 66: Ooo00oOo00o * Oo
def II1IIIiiI11 ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for i1iIIIi1i , url in Iiii :
  if '<p align' in i1iIIIi1i :
   pass
  elif '&nbsp;' in i1iIIIi1i :
   pass
  else :
   i1I1iI ( ( i1iIIIi1i ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 86 - 86: Ooo00oOo00o % OoooooooOO % Ooo00oOo00o / OOOo0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: OoooooooOO % i11iIiiIii * iIii1I11I1II1 . Ooo00oOo00o * O0
 if 23 - 23: i11iIiiIii
def II1I11IIi ( ) :
 IIi1iiIi1 = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 Iiii = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'ongoing' in iiIiii1IIIII :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in iiIiii1IIIII :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in iiIiii1IIIII :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in iiIiii1IIIII :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in iiIiii1IIIII :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def OoOOo ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIi1iiIi1 )
 iii1 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIi1iiIi1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i , oOO0O00oO0Ooo in Iiii :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 21006 , oOO0O00oO0Ooo , oOO0O00oO0Ooo , i1iIIIi1i )
 for url , i1iIIIi1i in iii1 :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  i1I1iI ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def oOO0oo ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 II1iIi1IiIii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIi1iiIi1 )
 I111I11I111 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIi1iiIi1 )
 iiiiI11ii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in I111I11I111 :
  i1I1iI ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , i1iIIIi1i in II1iIi1IiIii :
  oo0OooOOo0 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  oo0OooOOo0 ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , '' , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def O0i1i1II1i11 ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  oo0OooOOo0 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 91 - 91: oOo00oOO0O / i1IIi * i1IIi
def Ii1 ( ) :
 ii1IIIIiI11 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 ii1IIIIiI11 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 68 - 68: oO0O0ooO0Oo - i11iIiiIii - ii + I1IiI
def OO00ooOo0OOO ( ) :
 ii1IIIIiI11 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 ii1IIIIiI11 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 40 - 40: oO0 / I1IiI % i11iIiiIii % ii11ii1ii / OOOo0
def ooOOOOo0 ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  if '?c=' in url :
   ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
def ooO00O00oOO ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , I1IIII1ii , i1iIIIi1i in Iiii :
  if 'Genre' in url :
   ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 13 - 13: OoooooooOO * ii - oO0O0ooO0Oo / Ii11I + oOo00oOO0O + I1IIiI1
def iii1III1i ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , I1IIII1ii , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1IIII1ii )
  if 17 - 17: OoOoOO00 / OoOoOO00
def o0OO0Oo ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , I1IIII1ii , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1IIII1ii )
  if 3 - 3: O00Oo000ooO0 - O0 % iIii1I11I1II1 / I1IIiI1 . OOooOOo
  if 3 - 3: O0 % OoooooooOO / Ii11I
  if 89 - 89: OoOoOO00 / ii
  if 14 - 14: Ii11I . OOOo0 * oO0 + OoOoOO00 - oO0 + Ii11I
  if 18 - 18: ii - OOooOOo - OOOo0 - OOOo0
def OOooo00 ( ) :
 if 35 - 35: O00Oo000ooO0 . I1IiI * i11iIiiIii
 i1I1iI ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 44 - 44: i11iIiiIii / Oo
def Ii1IIi ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 iiIiii1IIIII = ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 O00O0Oooo0oO = O00O0Oooo0oO = ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) ) + '?s=' + ( I1I1I ) . replace ( ' ' , '+' )
 IIi1iiIi1 = iii1i1iiiiIi ( iiIiii1IIIII )
 iIIii = cloudflare . source ( O00O0Oooo0oO )
 Iiii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIi1iiIi1 )
 o00O0O = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( iIIii )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if I1I1I in i1iIIIi1i . lower ( ) :
   if 'Dad!' in i1iIIIi1i :
    pass
   elif 'Family Guy' in i1iIIIi1i :
    pass
   elif '2 Stupid' in i1iIIIi1i :
    pass
   elif 'The Zelfs' in i1iIIIi1i :
    pass
   elif 'A Clone' in i1iIIIi1i :
    pass
   elif 'A.T.O.M' in i1iIIIi1i :
    pass
   elif 'Almost Naked' in i1iIIIi1i :
    pass
   elif 'Angry Kid' in i1iIIIi1i :
    pass
   elif 'Annoying Orange' in i1iIIIi1i :
    pass
   elif 'Aqua Teen' in i1iIIIi1i :
    pass
   elif 'Assy Mcgee' in i1iIIIi1i :
    pass
   elif 'Astroblast' in i1iIIIi1i :
    pass
   elif 'Atomic Betty' in i1iIIIi1i :
    pass
   elif 'Axe Cop' in i1iIIIi1i :
    pass
   elif 'Baby Playpen' in i1iIIIi1i :
    pass
   elif 'Beavis and Butt' in i1iIIIi1i :
    pass
   elif 'Celebrity Deathmatch' in i1iIIIi1i :
    pass
   elif 'Clerks The' in i1iIIIi1i :
    pass
   elif 'Crapston Villas' in i1iIIIi1i :
    pass
   elif 'Duckman:' in i1iIIIi1i :
    pass
   elif 'Stripperella' in i1iIIIi1i :
    pass
   elif 'Vixen' in i1iIIIi1i :
    pass
   else :
    i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 for iiIiii1IIIII , i1iIIIi1i , oOO0O00oO0Ooo in o00O0O :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 21006 , oOO0O00oO0Ooo , oOO0O00oO0Ooo , i1iIIIi1i )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 43 - 43: O00Oo000ooO0 % oOOoo0Oo
def o0O0ooOOoO ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  if 'Dad!' in i1iIIIi1i :
   pass
  elif 'Family Guy' in i1iIIIi1i :
   pass
  elif '2 Stupid' in i1iIIIi1i :
   pass
  elif 'The Zelfs' in i1iIIIi1i :
   pass
  elif 'A Clone' in i1iIIIi1i :
   pass
  elif 'A.T.O.M' in i1iIIIi1i :
   pass
  elif 'Almost Naked' in i1iIIIi1i :
   pass
  elif 'Angry Kid' in i1iIIIi1i :
   pass
  elif 'Annoying Orange' in i1iIIIi1i :
   pass
  elif 'Aqua Teen' in i1iIIIi1i :
   pass
  elif 'Assy Mcgee' in i1iIIIi1i :
   pass
  elif 'Astroblast' in i1iIIIi1i :
   pass
  elif 'Atomic Betty' in i1iIIIi1i :
   pass
  elif 'Axe Cop' in i1iIIIi1i :
   pass
  elif 'Baby Playpen' in i1iIIIi1i :
   pass
  elif 'Beavis and Butt' in i1iIIIi1i :
   pass
  elif 'Celebrity Deathmatch' in i1iIIIi1i :
   pass
  elif 'Clerks The' in i1iIIIi1i :
   pass
  elif 'Crapston Villas' in i1iIIIi1i :
   pass
  elif 'Duckman:' in i1iIIIi1i :
   pass
  elif 'Stripperella' in i1iIIIi1i :
   pass
  elif 'Vixen' in i1iIIIi1i :
   pass
  else :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: i11iIiiIii
def oo0 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 o00O0O = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( i111iIi1i1II1 )
 for oOO0O00oO0Ooo in o00O0O :
  oOO = oOO0O00oO0Ooo
 II1i11i1iIi11 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( i111iIi1i1II1 )
 for url in II1i11i1iIi11 :
  i1I1iI ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 Iiii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 10007 , oOO )
  if 83 - 83: oO0O0ooO0Oo
  if 25 - 25: oOo00oOO0O + I1IiI . OOooOOo % I1IiI * Ii11I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: i11iIiiIii - O00Oo000ooO0
def oo00ooOoo ( url , IMAGE ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , url in Iiii :
  print i1iIIIi1i + '     ' + url
  if 'easy' in url :
   iii1IIIiiiI ( url )
   if 94 - 94: O0 - oOo00oOO0O - iIii1I11I1II1 % oO0 / oO0O0ooO0Oo % oOOoo0Oo
   if 44 - 44: Oo % iIii1I11I1II1
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 90 - 90: OoOoOO00 + OoooooooOO % OoooooooOO
def iii1IIIiiiI ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( "url: '(.+?)'," ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  I11Ii ( url )
  if 16 - 16: Oo / i11iIiiIii
  if 64 - 64: i11iIiiIii / oO0O0ooO0Oo * i1IIi
  if 73 - 73: Oo - I1IiI - ii - OOOo0
def oo0o0oOo ( ) :
 if 58 - 58: OOooOOo - OoOoOO00 % ii + O00Oo000ooO0 . I1IiI / I1IIiI1
 i1I1iI ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 8 - 8: ii11ii1ii . Ooo00oOo00o * oOo00oOO0O + OoOoOO00 % i11iIiiIii
def i1i1IiIiIi1Ii ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  if 'elete' in i1iIIIi1i :
   pass
  else :
   O0Oo00oO0O00 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 222 , oOO0O00oO0Ooo )
   if 64 - 64: Ii11I + OoooooooOO * OoooooooOO
def i1I ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 IIi1iiIi1 = iii1i1iiiiIi ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iiI1I1IIi11i1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , i1II1iii1i , iIiiiI1IiI1I1 in iiI1I1IIi11i1 :
  for I1I1I in i1II1iii1i :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for iiIiii1IIIII , i1iIIIi1i in OOO0o :
    if 'tube' in iiIiii1IIIII :
     pass
    elif 'stage' in iiIiii1IIIII :
     O0Oo00oO0O00 ( '[COLORgreen]' + i1II1iii1i + '   -   ' + i1iIIIi1i + '[/COLOR]' , ( iiIiii1IIIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOO0O00oO0Ooo , )
    elif 'vee' in iiIiii1IIIII :
     pass
     if 4 - 4: Oo . i1IIi - oOOoo0Oo
def i111i11I1Ii1I ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iiI1I1IIi11i1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , i1II1iii1i , iIiiiI1IiI1I1 in iiI1I1IIi11i1 :
  OOO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for iiIiii1IIIII , i1iIIIi1i in OOO0o :
   if 'tube' in iiIiii1IIIII :
    pass
   elif 'stage' in iiIiii1IIIII :
    O0Oo00oO0O00 ( '[COLORgreen]' + i1II1iii1i + '   -   ' + i1iIIIi1i + '[/COLOR]' , ( iiIiii1IIIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOO0O00oO0Ooo )
   elif 'vee' in iiIiii1IIIII :
    pass
    if 8 - 8: oO0O0ooO0Oo
    if 35 - 35: I1IIiI1 + i1IIi * ii - oO0O0ooO0Oo . Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: OOooOOo
def Ii1I ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 ii1iii1i = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIi1iiIi1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( ii1iii1i ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in ii1iii1i :
  I11Ii ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 45 - 45: i1IIi - Oo / O0 . ii11ii1ii
  if 5 - 5: OOooOOo . iIii1I11I1II1 % iIii1I11I1II1
  if 56 - 56: OoooooooOO - oOo00oOO0O - i1IIi
  if 8 - 8: O00Oo000ooO0 / Ii11I . OOOo0 + ii11ii1ii / i11iIiiIii
  if 31 - 31: oO0 - iIii1I11I1II1 + oOOoo0Oo . Oo / I1IIiI1 % iIii1I11I1II1
  if 6 - 6: I1IIiI1 * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / i1IIi
  if 53 - 53: oOo00oOO0O + iIii1I11I1II1
def oOooo0Oo ( ) :
 if 66 - 66: Oo
 I1i1IiI1i ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 I1i1IiI1i ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 32 - 32: OoooooooOO - I1IiI - i11iIiiIii * OOooOOo / Oo + OoooooooOO
 OOO ( 'movies' , 'MAIN' )
 if 35 - 35: i1IIi - OOooOOo * oOOoo0Oo
def O0oOoo0OoO0O ( ) :
 I1i1IiI1i ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 I1i1IiI1i ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 63 - 63: OoooooooOO / oO0
 OOO ( 'movies' , 'MAIN' )
def oooO00o0 ( ) :
 if 53 - 53: oO0
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 o0oO0oo0000OO = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 45 - 45: O00Oo000ooO0 * oO0O0ooO0Oo / OoooooooOO . ii % ii11ii1ii / i1IIi
 for I1III1 in o0oO0oo0000OO :
  Iiii1ii = ooooooO0oo + I1III1 + OooO0
  IIi1iiIi1 = iii1i1iiiiIi ( Iiii1ii )
  Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1iiIi1 )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , ooo , i1iIIIi1i in Iiii :
   if I1I1I in i1iIIIi1i . lower ( ) :
    I1i111IiIiIi1 ( i1iIIIi1i , iiIiii1IIIII , 222 , i1I1i111Ii , ooo , Ii1IIiI1i )
    if 39 - 39: oOo00oOO0O - ii11ii1ii
    OOO ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 53 - 53: OOooOOo % oOOoo0Oo + oO0 . Oo - ii11ii1ii % OOooOOo
    if 64 - 64: OoOoOO00
def iIIIiIi1I1i ( ) :
 if 78 - 78: iIii1I11I1II1 % I1IiI + ii11ii1ii / i1IIi % OoOoOO00 + Ii11I
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 o0oO0oo0000OO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 91 - 91: iIii1I11I1II1 % Ooo00oOo00o . OOooOOo + oO0O0ooO0Oo + OOooOOo
 for I1III1 in o0oO0oo0000OO :
  o00OOo = ooooooO0oo + I1III1 + OooO0
  IIi1iiIi1 = iii1i1iiiiIi ( o00OOo )
  Iiii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for i1iIIIi1i , Ii1IIiI1i , iiIiii1IIIII , oOO0O00oO0Ooo , ooo , oOo0OOoooO in Iiii :
   if I1I1I in i1iIIIi1i . lower ( ) :
    I1i1IiI1i ( i1iIIIi1i , iiIiii1IIIII , oOo0OOoooO , oOO0O00oO0Ooo , ooo , Ii1IIiI1i )
    if 26 - 26: OOooOOo * I1IIiI1 . i1IIi
    OOO ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 59 - 59: O0 + i1IIi - OOooOOo
    if 62 - 62: i11iIiiIii % Ii11I . I1IIiI1 . Ii11I
def ooOo0O0O0oOO0 ( ) :
 if 10 - 10: Oo + O0
 i111iIi1i1II1 = iii1i1iiiiIi ( ooooooO0oo + 'spongemain.php' )
 Iiii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , Ii1IIiI1i , iiIiii1IIIII , oOO0O00oO0Ooo , ooo , oOo0OOoooO in Iiii :
  I1i1IiI1i ( i1iIIIi1i , iiIiii1IIIII , oOo0OOoooO , oOO0O00oO0Ooo , ooo , Ii1IIiI1i )
  OOO ( 'movies' , 'MAIN' )
def Ii1iI ( url ) :
 if 53 - 53: iIii1I11I1II1 - ii % I1IiI * O00Oo000ooO0 % oO0
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 II1Ii = ( '%s%s' % ( OOoO00ooO , url ) )
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0ooo0o0O0Oooooo )
 for url , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in Iiii :
  I1i111IiIiIi1 ( i1iIIIi1i , url , 222 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
  if 51 - 51: Ii11I . OOOo0
  OOO ( 'movies' , 'MAIN' )
  if 73 - 73: OoooooooOO . OOOo0 / O00Oo000ooO0 % oO0O0ooO0Oo
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 65 - 65: I1IIiI1 - OOOo0 - oO0O0ooO0Oo
  if 42 - 42: OoOoOO00 * OOOo0 % i1IIi - oO0O0ooO0Oo % I1IIiI1
def Ii1I1 ( url ) :
 if 58 - 58: I1IIiI1 - oOo00oOO0O % OOOo0
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , Ii1IIiI1i , url , oOO0O00oO0Ooo , ooo , oOo0OOoooO in Iiii :
  I1i1IiI1i ( i1iIIIi1i , url , oOo0OOoooO , oOO0O00oO0Ooo , ooo , Ii1IIiI1i )
  if 4 - 4: i1IIi + oO0 + i1IIi
  OOO ( 'movies' , 'MAIN' )
  if 31 - 31: oO0O0ooO0Oo
  if 78 - 78: i11iIiiIii + OOooOOo + O00Oo000ooO0 / OOooOOo % iIii1I11I1II1 % I1IIiI1
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: iIii1I11I1II1 % I1IiI % OOooOOo % O00Oo000ooO0 . ii11ii1ii % O0
def I1i111IiIiIi1 ( name , url , mode , iconimage , fanart , description ) :
 if 47 - 47: OOooOOo
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = False )
 return iiIIi
 if 25 - 25: ii
def I1i1IiI1i ( name , url , mode , iconimage , fanart , description ) :
 if 34 - 34: I1IiI . iIii1I11I1II1 % O0
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
if 43 - 43: ii11ii1ii - oOOoo0Oo
if 70 - 70: oOOoo0Oo / Ii11I % oO0 - oO0O0ooO0Oo
if 47 - 47: oOOoo0Oo
if 92 - 92: Ii11I + I1IiI % i1IIi
if 23 - 23: O00Oo000ooO0 - Ii11I + oO0O0ooO0Oo - I1IiI * I1IiI . Oo
if 47 - 47: ii % iIii1I11I1II1
if 11 - 11: OOOo0 % oO0O0ooO0Oo - Ooo00oOo00o - ii + OOooOOo
if 98 - 98: oOOoo0Oo + oO0O0ooO0Oo - Ooo00oOo00o
if 79 - 79: Ii11I / O00Oo000ooO0 . I1IiI - ii11ii1ii
if 47 - 47: OoooooooOO % O0 * oOOoo0Oo . oO0O0ooO0Oo
if 38 - 38: O0 - I1IIiI1 % O00Oo000ooO0
if 64 - 64: iIii1I11I1II1
if 15 - 15: ii11ii1ii + Ii11I / ii11ii1ii / O00Oo000ooO0
if 31 - 31: oO0 + O0 + oO0 . iIii1I11I1II1 + Oo / OOooOOo
if 6 - 6: Oo % I1IIiI1 * oOo00oOO0O / OOOo0 + Oo
def IIiI11i11 ( string ) :
 if OOO00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 14 - 14: i11iIiiIii
def o0oOOO0 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oOOO = [ ]
 try :
  if 36 - 36: ii11ii1ii - oOOoo0Oo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  IIiI11i11 ( 'Making Favorites File' )
  oOOO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OOoOooOoOOOoo = open ( I11i1 , "w" )
  OOoOooOoOOOoo . write ( json . dumps ( oOOO ) )
  OOoOooOoOOOoo . close ( )
 else :
  IIiI11i11 ( 'Appending Favorites' )
  OOoOooOoOOOoo = open ( I11i1 ) . read ( )
  III1I1 = json . loads ( OOoOooOoOOOoo )
  III1I1 . append ( ( name , url , iconimage , fanart , mode ) )
  O00o00O = open ( I11i1 , "w" )
  O00o00O . write ( json . dumps ( III1I1 ) )
  O00o00O . close ( )
  if 12 - 12: iIii1I11I1II1 % oO0 % oO0
  if 78 - 78: I1IIiI1 . I1IiI . oOo00oOO0O
def o0ooO0OOO ( ) :
 o0oo000OoOoo0 = json . loads ( open ( I11i1 ) . read ( ) )
 OoO0o = len ( o0oo000OoOoo0 )
 for iiiiIiI1i1I1 in o0oo000OoOoo0 :
  i1iIIIi1i = iiiiIiI1i1I1 [ 0 ]
  iiIiii1IIIII = iiiiIiI1i1I1 [ 1 ]
  i1I1i111Ii = iiiiIiI1i1I1 [ 2 ]
  try :
   oo0i1iIIi1II1iiI = iiiiIiI1i1I1 [ 3 ]
   if oo0i1iIIi1II1iiI == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    oo0i1iIIi1II1iiI = i1I1i111Ii
   else :
    oo0i1iIIi1II1iiI = ooo
  try : III1Ii1i1I1 = iiiiIiI1i1I1 [ 5 ]
  except : III1Ii1i1I1 = None
  try : O0O00OooO = iiiiIiI1i1I1 [ 6 ]
  except : O0O00OooO = None
  if 40 - 40: oOo00oOO0O % OoooooooOO - Ii11I + OOooOOo / Ii11I
  if iiiiIiI1i1I1 [ 4 ] == 0 :
   i1I1iI ( i1iIIIi1i , iiIiii1IIIII , '' , i1I1i111Ii , ooo , '' , 'fav' )
  else :
   i1I1iI ( i1iIIIi1i , iiIiii1IIIII , iiiiIiI1i1I1 [ 4 ] , i1I1i111Ii , ooo , '' , 'fav' )
   if 84 - 84: O0
def iiii ( name ) :
 III1I1 = json . loads ( open ( I11i1 ) . read ( ) )
 for I11I1i1iI in range ( len ( III1I1 ) ) :
  if III1I1 [ I11I1i1iI ] [ 0 ] == name :
   del III1I1 [ I11I1i1iI ]
   O00o00O = open ( I11i1 , "w" )
   O00o00O . write ( json . dumps ( III1I1 ) )
   O00o00O . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 90 - 90: I1IIiI1 * OoOoOO00 % O00Oo000ooO0 + ii
 if 93 - 93: O00Oo000ooO0 + oO0O0ooO0Oo
def o0000oO ( ) :
 i1i1 = os . path . join ( iIii1 , 'addons.ini' )
 i1IiIi1 = open ( i1i1 , "w+" )
 if 22 - 22: oOo00oOO0O * O0 . OoOoOO00 - Ooo00oOo00o
 i1IiIi1 . write ( r'# This file contains the "built-in" channels' + '\n' )
 i1IiIi1 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 i1IiIi1 . write ( r'[plugin.video.GenieTv]' + '\n' )
 i1IiIi1 . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F394.m3u8&mode=10012&name=[COLORgreen]BBC+One+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'BBC Ent MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F435.m3u8&mode=10012&name=[COLORgreen]BBC+Entertainment+MX%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F408.m3u8&mode=10012&name=[COLORgreen]Watch+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F410.m3u8&mode=10012&name=[COLORgreen]Pick+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F430.m3u8&mode=10012&name=[COLORgreen]Gold+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F411.m3u8&mode=10012&name=[COLORgreen]Yesterday+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F398.m3u8&mode=10012&name=[COLORgreen]Disney+Channel+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F397.m3u8&mode=10012&name=[COLORgreen]Disney+Junior+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F395.m3u8&mode=10012&name=[COLORgreen]Discovery+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F396.m3u8&mode=10012&name=[COLORgreen]Discovery+Science+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F428.m3u8&mode=10012&name=[COLORgreen]Animal+Planet+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F431.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F429.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F409.m3u8&mode=10012&name=[COLORgreen]MTV+Music+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'MTV Canada=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F417.m3u8&mode=10012&name=[COLORgreen]MTV+2+Ca%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F37.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F39.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F40.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F43.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F41.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F44.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F47.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F48.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Fox Movies HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F436.m3u8&mode=10012&name=[COLORgreen]Fox+Movies+HD+MX%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Film Zone MX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F437.m3u8&mode=10012&name=[COLORgreen]Film+Zone+MX+HD%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F403.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F404.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F405.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F406.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F407.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F412.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F423.m3u8&mode=10012&name=[COLORgreen]BT+Sports+1%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F413.m3u8&mode=10012&name=[COLORgreen]BT+Sports+2%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Fox Sports 1 HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F439.m3u8&mode=10012&name=[COLORgreen]Fox+Sports+1+HD+MX%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'ESPN 1 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F440.m3u8&mode=10012&name=[COLORgreen]ESPN+1+HD+ES%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'ESPN 2 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F441.m3u8&mode=10012&name=[COLORgreen]ESPN+2+HD+ES%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F427.m3u8&mode=10012&name=[COLORgreen]At+The+Races+UK%0D[/COLOR]' + '\n' )
 i1IiIi1 . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F426.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[/COLOR]' + '\n' )
 if 90 - 90: ii
 if 94 - 94: oOo00oOO0O / ii11ii1ii * O00Oo000ooO0 - I1IiI
 if 44 - 44: oO0O0ooO0Oo % i11iIiiIii - oOOoo0Oo * ii11ii1ii + Oo * Ii11I
def IiI1iI1IiiIi1 ( ) :
 if 90 - 90: O0 + oOo00oOO0O - OoooooooOO . oOo00oOO0O
 i1I1iI ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 60 - 60: OOooOOo . OOooOOo / oOOoo0Oo
def Ii ( ) :
 if 79 - 79: iIii1I11I1II1
 i111iIi1i1II1 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Iiii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i , iI1iIIiiii in Iiii :
  i1I1iI ( i1iIIIi1i + '  -  ' + ( iI1iIIiiii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiIiii1IIIII , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 81 - 81: Ii11I + iIii1I11I1II1 * O00Oo000ooO0 - iIii1I11I1II1 . Ii11I
  if 48 - 48: oOo00oOO0O . OoooooooOO . OOOo0 . I1IiI % ii11ii1ii / oOOoo0Oo
  if 11 - 11: i1IIi % Ooo00oOo00o % oOOoo0Oo
def O0Oo0 ( ) :
 if 80 - 80: OOOo0 - iIii1I11I1II1 . Ii11I + Ooo00oOo00o - O00Oo000ooO0
 i1I1iI ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 5 - 5: oOOoo0Oo
def OOiI1 ( url ) :
 OOOoo0OO = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIi1iiIi1 = cloudflare . source ( OOOoo0OO )
 Iiii = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 42 - 42: Ii11I % ii / Ooo00oOo00o - ii * i11iIiiIii
  if 19 - 19: ii * OOOo0 % i11iIiiIii
  if 24 - 24: OOooOOo
  if 10 - 10: OOooOOo % oO0O0ooO0Oo / Ii11I
def i11Ii1iIiII ( ) :
 if 81 - 81: oOo00oOO0O . OoooooooOO * I1IiI % I1IIiI1 . oOo00oOO0O
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 iiIiii1IIIII = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1I1I ) . replace ( ' ' , '+' )
 IIi1iiIi1 = cloudflare . source ( iiIiii1IIIII )
 Iiii = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  if I1I1I in i1iIIIi1i . lower ( ) :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 10022 , ii11iIi1I + 'dtv.png' )
   if 60 - 60: Ii11I / OOOo0
   if 78 - 78: oOo00oOO0O . I1IIiI1
   if 38 - 38: I1IiI + I1IIiI1
def IIi1I1i ( url ) :
 IIi1iiIi1 = cloudflare . source ( url )
 Iiii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for O00O0Oooo0oO , IioO0O , Oo00o0O0O , i1iIIIi1i in Iiii :
  o0ooO0OoOo = ( Oo00o0O0O ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0oOO00 = ( IioO0O ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ii11iiIi = 'Season ' + o0oOO00 + 'Episode ' + o0ooO0OoOo + i1iIIIi1i
  i11iI11I1I ( ii11iiIi , O00O0Oooo0oO )
  if 47 - 47: O0 * OOOo0 * Ooo00oOo00o . OoOoOO00
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 95 - 95: oO0O0ooO0Oo % I1IIiI1 . O0 % O00Oo000ooO0
  if 68 - 68: Oo . Oo - ii11ii1ii / oOo00oOO0O . oO0 / i1IIi
def i11iI11I1I ( name , url ) :
 O00O0Oooo0oO = url
 iI1i1iIi1iiII = name
 iIIii = cloudflare . source ( O00O0Oooo0oO )
 o00O0O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iIIii )
 for ii1iii1i , o0OoO0000o in o00O0O :
  O0Oo00oO0O00 ( '[COLORgreen]' + iI1i1iIi1iiII + o0OoO0000o + '[/COLOR]' , ii1iii1i , 10012 , ii11iIi1I + 'dtv.png' )
  if 90 - 90: I1IIiI1 . oO0 / iIii1I11I1II1
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: I1IIiI1 + ii - oO0 / iIii1I11I1II1 - OOOo0
 if 45 - 45: O0 / i1IIi * ii * Ooo00oOo00o
def II11I ( ) :
 if 31 - 31: oO0O0ooO0Oo
 if 18 - 18: oO0 + oO0O0ooO0Oo
 if 5 - 5: OoooooooOO + oOo00oOO0O * OoOoOO00
 if 98 - 98: Ii11I % i1IIi . OOOo0 . OoOoOO00 . ii11ii1ii / i11iIiiIii
 if 32 - 32: OOooOOo + OOOo0 . O00Oo000ooO0
 if 41 - 41: I1IiI . i11iIiiIii / oOo00oOO0O
 if 98 - 98: I1IiI % OoOoOO00
 if 95 - 95: iIii1I11I1II1 - O00Oo000ooO0 - Ii11I + O00Oo000ooO0 % ii11ii1ii . OOOo0
 if 41 - 41: O0 + ii . i1IIi - OoOoOO00 * OOooOOo . Ooo00oOo00o
 if 68 - 68: OOooOOo
 if 20 - 20: O00Oo000ooO0 - O00Oo000ooO0
 if 37 - 37: I1IIiI1
 if 37 - 37: Oo / I1IIiI1 * O0
 if 73 - 73: oOOoo0Oo * oOOoo0Oo / oO0
 if 43 - 43: ii11ii1ii . i1IIi . I1IIiI1 + O0 * oO0O0ooO0Oo * O0
 i1I1iI ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 i1I1iI ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 i1I1iI ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 41 - 41: ii11ii1ii + oO0O0ooO0Oo % OoooooooOO . ii11ii1ii + oOOoo0Oo . oOOoo0Oo
 if 31 - 31: i11iIiiIii + OoOoOO00 . oOOoo0Oo * I1IiI
def OO0ooo0 ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 oOo = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 Iiii = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( oOo ) )
 for url , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 7 - 7: ii11ii1ii - ii * Ii11I + OOooOOo . ii11ii1ii
def ooooO ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 92 - 92: OOooOOo / OOooOOo * oO0O0ooO0Oo
def iI111i11iI1 ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 o00O0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + ( i1iIIIi1i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in o00O0O :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 2 - 2: I1IiI + O00Oo000ooO0 + OoooooooOO . i1IIi
  if 19 - 19: oOOoo0Oo - OOooOOo - oO0O0ooO0Oo - I1IiI . oOOoo0Oo . O00Oo000ooO0
def i11I1I ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0ooooo00o = 'http://www.watchseries.li/search/' + I1I1I . replace ( ' ' , '%20' )
 IIi1iiIi1 = iii1i1iiiiIi ( oo0ooooo00o )
 Iiii = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'watch online' in i1iIIIi1i :
   pass
  else :
   print iiIiii1IIIII
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://www.watchseries.li' + iiIiii1IIIII , 10044 , oOO0O00oO0Ooo , '' , '' )
   if 78 - 78: iIii1I11I1II1 . OOooOOo % iIii1I11I1II1 . O0 / Ii11I
   xbmcplugin . setContent ( O0O , 'movies' )
   if 76 - 76: i1IIi * OoooooooOO * O0 + O00Oo000ooO0 * O00Oo000ooO0
def i1iIiIii ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , url , i1iIIIi1i , Oo00o0O0O , Ii1IIiI1i in Iiii :
  iI1iiI1III1i = ( i1iIIIi1i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( Oo00o0O0O ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  i1I1iI ( '[COLORgreen]' + iI1iiI1III1i + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOO0O00oO0Ooo , '' , Ii1IIiI1i )
  if 36 - 36: i1IIi / oO0 . iIii1I11I1II1
def i1IiiiiIi1I ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 o00O0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  iI1iiI1III1i = ( i1iIIIi1i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  i1I1iI ( '[COLORgreen]' + iI1iiI1III1i + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in o00O0O :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 56 - 56: OoooooooOO * O0
def oo0OoOOooO ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( IIi1iiIi1 )
 o00O0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i , oOO0O00oO0Ooo in Iiii :
  i1I1iI ( '[COLORgreen]' + ( i1iIIIi1i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOO0O00oO0Ooo , '' , '' )
 for url in o00O0O :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 60 - 60: O00Oo000ooO0
def oOO0o00o0Oo0O ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 oOo = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for IioO0O , iiI1I1IIi11i1 in oOo :
  Iiii = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( iiI1I1IIi11i1 ) )
  for url , i1iIIIi1i in Iiii :
   iI1iiI1III1i = ( IioO0O ) . replace ( '  ' , '' ) + ' ' + ( i1iIIIi1i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   i1I1iI ( '[COLORgreen]' + iI1iiI1III1i + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 o00O0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url in o00O0O :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 41 - 41: Ooo00oOo00o - OoOoOO00 + oO0O0ooO0Oo
  if 11 - 11: ii + iIii1I11I1II1
class i1ooOoo000oO ( ) :
 if 50 - 50: I1IIiI1 + OOooOOo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 96 - 96: Ooo00oOo00o
  iI1iiI1III1i = name
  self . Get_Sources ( iiIiii1IIIII , iI1iiI1III1i )
  if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
  if 87 - 87: I1IiI % iIii1I11I1II1
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  IIi1iiIi1 = iii1i1iiiiIi ( URL )
  Iiii = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for iiIiii1IIIII , i1iIIIi1i in Iiii :
   URL = 'http://www.watchseries.li/link/' + iiIiii1IIIII
   self . Get_site_link ( URL , season_name )
   if 72 - 72: Ii11I . Ii11I - ii11ii1ii
 def Get_site_link ( self , url , season_name ) :
  IIi1iiIi1 = iii1i1iiiiIi ( url )
  Iiii = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( IIi1iiIi1 )
  o00O0O = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( IIi1iiIi1 )
  II1i11i1iIi11 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( IIi1iiIi1 )
  for url in Iiii :
   self . main ( url , season_name )
  for url in o00O0O :
   self . main ( url , season_name )
  for url in II1i11i1iIi11 :
   self . main ( url , season_name )
   if 48 - 48: Oo - oO0 + Oo - OOOo0 * i11iIiiIii . oOOoo0Oo
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   I1iIIIiI = 'DACLIPS'
   if I1iIIIiI in i1ooOoo000oO . source_list :
    pass
   else :
    self . daclips ( url , season_name , I1iIIIiI )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    I1iIIIiI = 'FILEHOOT'
    if I1iIIIiI in i1ooOoo000oO . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , I1iIIIiI )
   else :
    if 'thevideo.me' in url :
     I1iIIIiI = 'THEVIDEO'
     if I1iIIIiI in i1ooOoo000oO . source_list :
      pass
     else :
      self . thevideo ( url , season_name , I1iIIIiI )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      I1iIIIiI = 'ALLMYVIDEOS'
      if I1iIIIiI in i1ooOoo000oO . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , I1iIIIiI )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       I1iIIIiI = 'VIDSPOT'
       if I1iIIIiI in i1ooOoo000oO . source_list :
        pass
       else :
        self . vidspot ( url , season_name , I1iIIIiI )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        I1iIIIiI = 'VODLOCKER'
        if I1iIIIiI in i1ooOoo000oO . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , I1iIIIiI )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 60 - 60: OOOo0 . i11iIiiIii + I1IiI / ii11ii1ii * OoOoOO00 * Ii11I
         if 59 - 59: Oo + oOOoo0Oo - Ii11I . OOooOOo + OOOo0 % ii
 def allmyvid ( self , url , season_name , source_name ) :
  IIi1iiIi1 = iii1i1iiiiIi ( url )
  Iiii = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for i111Iii , i1iIIIi1i in Iiii :
   self . Printer ( i111Iii , season_name , source_name )
   if 100 - 100: oOo00oOO0O / oOOoo0Oo . O0
 def vidspot ( self , url , season_name , source_name ) :
  IIi1iiIi1 = iii1i1iiiiIi ( url )
  Iiii = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( IIi1iiIi1 )
  for i111Iii , i1iIIIi1i in Iiii :
   self . Printer ( i111Iii , season_name , source_name )
   if 34 - 34: oOOoo0Oo
 def thevideo ( self , url , season_name , source_name ) :
  IIi1iiIi1 = iii1i1iiiiIi ( url )
  Iiii = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIi1iiIi1 )
  for i111Iii in Iiii :
   self . Printer ( i111Iii , season_name , source_name )
   if 48 - 48: Ii11I % OOOo0
 def vodlocker ( self , url , season_name , source_name ) :
  IIi1iiIi1 = iii1i1iiiiIi ( url )
  Iiii = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for i111Iii in Iiii :
   self . Printer ( i111Iii , season_name , source_name )
   if 81 - 81: i1IIi - ii + I1IiI
 def daclips ( self , url , season_name , source_name ) :
  IIi1iiIi1 = iii1i1iiiiIi ( url )
  Iiii = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( IIi1iiIi1 )
  for i111Iii in Iiii :
   self . Printer ( i111Iii , season_name , source_name )
   if 77 - 77: oOo00oOO0O . I1IIiI1
 def filehoot ( self , url , season_name , source_name ) :
  IIi1iiIi1 = iii1i1iiiiIi ( url )
  Iiii = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for i111Iii in Iiii :
   self . Printer ( i111Iii , season_name , source_name )
   if 58 - 58: oOo00oOO0O * I1IiI
 def Printer ( self , Link , season_name , source_name ) :
  if 94 - 94: oO0O0ooO0Oo - ii11ii1ii + OOooOOo - Oo
  if Link in i1ooOoo000oO . List :
   pass
  elif source_name in i1ooOoo000oO . source_list :
   pass
  else :
   O0Oo00oO0O00 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   i1ooOoo000oO . List . append ( Link )
   i1ooOoo000oO . source_list . append ( source_name )
   if 15 - 15: Ii11I
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 31 - 31: oOOoo0Oo / i1IIi . Ooo00oOo00o
   if 83 - 83: ii / iIii1I11I1II1 + i1IIi / oOOoo0Oo
   if 47 - 47: ii + OoooooooOO . OoOoOO00 . oOOoo0Oo
   if 66 - 66: oO0 * I1IiI
   if 2 - 2: ii . O00Oo000ooO0 * Oo + O0 - oOo00oOO0O * iIii1I11I1II1
def II111i1ii1iII ( ) :
 i1I1iI ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 75 - 75: iIii1I11I1II1 + OoooooooOO
def oOOO0 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 Iiii = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  i1I1iI ( '[COLORgreen]' + ( i1iIIIi1i ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiIiii1IIIII , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOO0O00oO0Ooo , i1iiIII111ii , '' )
  if 32 - 32: oO0 % O00Oo000ooO0 * Oo
def O0O000oOo0O ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 oOo = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOo in oOo :
  o0O0O0oo0oo0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( oOo ) )
  for O0Oo000OO000 in o0O0O0oo0oo0 :
   O0Oo000OO000 = O0Oo000OO000
  OOOO00OooO = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( oOo ) )
  for OOOiI1 , oOO0O00oO0Ooo , time , O00oO0o000oO in OOOO00OooO :
   IIIIiiIiiI = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( O00oO0o000oO )
   i1I1iI ( '[COLORgreen]' + O0Oo000OO000 + ' - ' + OOOiI1 + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOO0O00oO0Ooo , i1iiIII111ii , ( str ( IIIIiiIiiI ) ) )
   if 19 - 19: I1IIiI1 * O00Oo000ooO0 / ii * O00Oo000ooO0 - OoooooooOO * oOo00oOO0O
 OOO ( 'tvshows' , 'Media Info 3' )
 if 17 - 17: OoOoOO00 + Oo . O00Oo000ooO0
def I1I1i1i ( ) :
 if 87 - 87: I1IiI / I1IIiI1 . oO0 - Ii11I / Ooo00oOo00o
 i1I1iI ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 41 - 41: OoOoOO00
def II1Iiii11111 ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , url , i1iIIIi1i in Iiii :
  iiI11I1iiIiII1I = i1iIIIi1i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  O0Oo00oO0O00 ( '[COLORgreen]' + iiI11I1iiIiII1I + '[/COLOR]' , url , 10013 , oOO0O00oO0Ooo )
  if 59 - 59: O00Oo000ooO0 - I1IIiI1
def iiiii111 ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( IIi1iiIi1 )
 for ii1iii1i in Iiii :
  oO0oo0o00o0O = ( ii1iii1i ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I11Ii ( 'http:' + oO0oo0o00o0O )
  if 80 - 80: iIii1I11I1II1
  if 23 - 23: OoOoOO00
def o0oO0OO00oo0o ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i , oOO0O00oO0Ooo in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , url , 8046 , oOO0O00oO0Ooo )
 for url in o00O0O :
  ii1IIIIiI11 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def I1II1 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  I11Ii ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 53 - 53: O0 + Ii11I % i11iIiiIii * Ii11I
def o00oo0OO0 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  yt . PlayVideo ( url )
  if 60 - 60: oO0
def O000O ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 iiii1IIi1 = oooO ( i1111 ( 'aHR0cDovL2Z1bGwtZG9jdW1lbnRhcmllcy5jb20v' ) )
 Iiii = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( "<a href='([^']*)' class='.+?' title='([^']*)' style='font-size: 8pt;'>(.+?)</a>" ) . findall ( iiii1IIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , iiIiii1IIIII , 8041 , ii11iIi1I + 'documentary.png' )
 for iiIiii1IIIII , oo0o0OoOO0o0 , i1iIIIi1i in o00O0O :
  ii1IIIIiI11 ( ( i1iIIIi1i + ' [COLORred]' + oo0o0OoOO0o0 + '[/COLOR]' ) . replace ( '&#039;' , '' ) , iiIiii1IIIII , 8041 , ii11iIi1I + 'documentary.png' )
  OOO ( 'movies' , 'INFO' )
  if 14 - 14: OOooOOo % I1IIiI1 + ii11ii1ii + Ooo00oOo00o
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOoOOo0o ( url ) :
 i111iIi1i1II1 = oooO ( url )
 IiI1Iii1 = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="author">.+?<img src="([^"]*)".+?<p>(.+?)</p>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 Ooooo = re . compile ( 'class="current">.+?</span><a href="([^"]*)" class' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 Iiii = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i , oOO0O00oO0Ooo in Iiii :
  ii1IIIIiI11 ( ( i1iIIIi1i ) . replace ( '&#039;s' , '' ) , url , 8042 , oOO0O00oO0Ooo )
 for url in o00O0O :
  ii1IIIIiI11 ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
 for url , i1iIIIi1i , oOO0O00oO0Ooo , I1IIII1ii in IiI1Iii1 :
  oo0OooOOo0 ( i1iIIIi1i , url , 8042 , oOO0O00oO0Ooo , oOO0O00oO0Ooo , ( I1IIII1ii ) . replace ( '&#8211' , '' ) )
 for url in Ooooo :
  ii1IIIIiI11 ( 'NEXT' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 43 - 43: Ii11I
  if 57 - 57: O0 / OOooOOo
def IiIioO0Oo00oo ( url ) :
 i111iIi1i1II1 = oooO ( url )
 IiI1Iii1 = re . compile ( '<p><iframe src="([^"]*)"' ) . findall ( i111iIi1i1II1 )
 Iiii = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , oOO0O00oO0Ooo , url , I1IIII1ii in Iiii :
  O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , oOO0O00oO0Ooo )
 for url in o00O0O :
  OoOoooO000OO ( ( url ) . replace ( '//' , 'http://' ) )
 for url in IiI1Iii1 :
  IIii11I1 ( url )
  if 62 - 62: Ii11I + Oo % iIii1I11I1II1 / iIii1I11I1II1 . oO0 . I1IIiI1
def OoOoooO000OO ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  O0Oo00oO0O00 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 21 - 21: Ooo00oOo00o - oO0O0ooO0Oo - OOOo0 / I1IiI
def ii1oOoO0ooO0000 ( ) :
 IIi1iiIi1 = oooO ( 'http://www.stream2watch.co/live-tv' )
 Iiii = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i , OOOOO in Iiii :
  ii1IIIIiI11 ( ( i1iIIIi1i + '[COLORgreen]' + OOOOO + '[/COLOR]' ) , iiIiii1IIIII , 8086 , oOO0O00oO0Ooo )
  if 68 - 68: oOo00oOO0O + Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI
def I1iiiI ( url ) :
 IIi1iiIi1 = oooO ( url )
 Iiii = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 8087 , oOO0O00oO0Ooo )
  if 24 - 24: OOOo0 * ii
def Oo0O0000Oo00o ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  II1 ( url , i1iIIIi1i )
  if 31 - 31: i11iIiiIii . I1IIiI1
def II1 ( url , name ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url in Iiii :
  print url
  O0Oo00oO0O00 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 36 - 36: oOOoo0Oo
def oOooOO ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 Iiii = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iiIiii1IIIII , 3002 , 'http://www.solie.org/alibrary/' + oOO0O00oO0Ooo )
def Ii1I1OO0ooO0 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOO0O00oO0Ooo )
def OoOooOO0oOOo0O ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 I1II = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , i1iIIIi1i in I1II :
  ii1IIIIiI11 ( '[COLORgreen]Season- ' + i1iIIIi1i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  ii1IIIIiI11 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in o00O0O :
  ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOO0O00oO0Ooo )
def iIIi1Ii1III ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  Oooo00iii1II1iI1IIi ( url )
def Oooo00iii1II1iI1IIi ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  I11Ii ( url )
  if 41 - 41: OOOo0 - O00Oo000ooO0 % OoOoOO00 . O00Oo000ooO0 - oOo00oOO0O
def i1I111Ii ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 Iiii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiIiii1IIIII , 8061 , ii11iIi1I + 'classicmovies.png' )
def i11i1i ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( "v.src = '([^']*)';" ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  I11Ii ( url )
  if 10 - 10: oO0O0ooO0Oo - i11iIiiIii . ii11ii1ii % i1IIi
def OooOOOoOoo0O0 ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 Iiii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiIiii1IIIII , 8061 , ii11iIi1I + 'classictv.png' )
def O0OOOOo0 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( "v.src = '([^']*)';" ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  I11Ii ( url )
  if 72 - 72: OOooOOo % OOOo0 / oOOoo0Oo - O0 + oOo00oOO0O
def o0iIIIIi ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 Iiii = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iiIiii1IIIII , 8071 , ii11iIi1I + 'streams.png' )
def i1I11ii ( url ) :
 IIi1iiIi1 = oooO ( url )
 Iiii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for i1iIIIi1i , url in Iiii :
  O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def o0ooO00O0O ( url ) :
 IIi1iiIi1 = oooO ( url )
 Iiii = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , i1iIIIi1i , url in Iiii :
  url = ( ( i1111 ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . replace ( '.ts' , '.m3u8' ) , 10012 , oOO0O00oO0Ooo )
  if 41 - 41: ii11ii1ii
def i1iI1i ( ) :
 OOo00O ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 OOo00O ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 OOo00O ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 OOo00O ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 OOo00O ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 59 - 59: I1IIiI1
def oOoO0OOO00O ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 OOOOO0o0OOo = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIi1iiIi1 )
 for url in OOOOO0o0OOo :
  OOo00O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 Iiii = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i , OO in Iiii :
  OOo00O ( i1iIIIi1i + ' - No of Videos : ' + ( OO ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 40 - 40: I1IIiI1 * ii % oOo00oOO0O * ii11ii1ii
def OoOoOOoO ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 OOOOO0o0OOo = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIi1iiIi1 )
 for url in OOOOO0o0OOo :
  OOo00O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 Iiii = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , url , i1iIIIi1i , oo0o0OoOO0o0 in Iiii :
  OOo00O ( i1iIIIi1i + '--' + oo0o0OoOO0o0 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOO0O00oO0Ooo ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 19 - 19: iIii1I11I1II1 * OoooooooOO * i11iIiiIii
  if 79 - 79: I1IIiI1 % Ooo00oOo00o
def Oo0oOO ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , url , i1iIIIi1i , o00o , ooooo in Iiii :
  oo0OooOOo0 ( i1iIIIi1i + ' - Porn Quality : ' + ooooo + ' - ' + o00o , 'http://www.xvideos.com' + url , 10108 , oOO0O00oO0Ooo , oOO0O00oO0Ooo , ooooo + ' - ' + o00o )
 iIiIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIi1iiIi1 )
 for url in iIiIi :
  OOo00O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 3 - 3: Oo
def iI1ii ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 oOo = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 OOOOO0o0OOo = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIi1iiIi1 )
 for url in OOOOO0o0OOo :
  OOo00O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 Iiii = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( oOo ) )
 for url , i1iIIIi1i in Iiii :
  OOo00O ( i1iIIIi1i , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 76 - 76: oO0O0ooO0Oo + iIii1I11I1II1 + I1IiI . Ooo00oOo00o
  if 49 - 49: I1IIiI1 / oO0 / Ii11I
def IiIiIi1I11I ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiI1i1i = ( I1I1I ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 i1Ii11i1i = IiI1i1i . lower ( )
 o0OOOOOo0 = 'http://www.xvideos.com/?k=' + i1Ii11i1i
 print o0OOOOOo0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIi1iiIi1 = iii1i1iiiiIi ( o0OOOOOo0 )
 Iiii = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for oOO0O00oO0Ooo , iiIiii1IIIII , i1iIIIi1i , o00o , ooooo in Iiii :
  oo0OooOOo0 ( i1iIIIi1i + ' - Porn Quality : ' + ooooo + ' - ' + o00o , 'http://www.xvideos.com' + iiIiii1IIIII , 10108 , oOO0O00oO0Ooo , oOO0O00oO0Ooo , ooooo + ' - ' + o00o )
 iIiIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII in iIiIi :
  OOo00O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iiIiii1IIIII , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 57 - 57: iIii1I11I1II1 + iIii1I11I1II1
def oO0o0Oo ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'flv_url=(.+?)\;' ) . findall ( IIi1iiIi1 )
 for url in Iiii :
  o0OO = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  oOoO00O000 ( o0OO )
  if 54 - 54: O0 - oOOoo0Oo . Ii11I % oOOoo0Oo + oOOoo0Oo
def oOoO00O000 ( url ) :
 II1iIi1IiIii = xbmc . Player ( i1iI1Iiii1I ( ) )
 import urlresolver
 try : II1iIi1IiIii . play ( url )
 except : pass
 if 9 - 9: oOo00oOO0O / I1IiI / OoOoOO00 + O00Oo000ooO0
 if 71 - 71: oOOoo0Oo / Oo
def OOOO0Oo ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 Iiii = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + iiIiii1IIIII ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def iIiI1 ( url ) :
 IIi1iiIi1 = oooO ( url )
 Iiii = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 o00O0O = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIi1iiIi1 )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , i1iIIIi1i , oOO0O00oO0Ooo in o00O0O :
  O0Oo00oO0O00 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + oOO0O00oO0Ooo )
 for url in next :
  ii1IIIIiI11 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def I1IiII1I1i1I1 ( url ) :
 IIi1iiIi1 = oooO ( url )
 Iiii = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( IIi1iiIi1 )
 for url in Iiii :
  yt . PlayVideo ( url )
  if 28 - 28: Oo + I1IIiI1 % OoOoOO00 / Ooo00oOo00o + i11iIiiIii
def ii11Iiii ( url ) :
 II1OoooOo = urllib2 . Request ( url )
 II1OoooOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1I1IIiiii1ii = ''
 OO0ooo0o0O0Oooooo = ''
 try :
  I1I1IIiiii1ii = urllib2 . urlopen ( II1OoooOo )
  OO0ooo0o0O0Oooooo = I1I1IIiiii1ii . read ( )
  I1I1IIiiii1ii . close ( )
 except : pass
 if OO0ooo0o0O0Oooooo != '' :
  return OO0ooo0o0O0Oooooo
 else :
  OO0ooo0o0O0Oooooo = 'Failed'
  return OO0ooo0o0O0Oooooo
  if 92 - 92: ii / Ii11I . ii11ii1ii
  if 30 - 30: oO0O0ooO0Oo . ii11ii1ii / Ii11I
def i1II11IiiiI ( ) :
 IIIi = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 iiIiii1IIIII = ( i1111 ( 'aHR0cDovL2Vtb3ZpZXMucHJvLz9zPQ==' ) ) + I1I1I
 O00O0Oooo0oO = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 oOO0O00Oo0O0o = ( i1111 ( 'http://217.219.143.108/1327/' ) )
 Ii1iiI1 = ( i1111 ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 o0ooOOoO0oO0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oo00I1IiI1IIiI = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oooo = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1I1I
 o0o0oo0Ooo = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 iI1i = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 i11I = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 o0oO0o0oo0O0 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 Oo0oO0ooo . update ( 0 , "" , "Checking Hosts" )
 if 98 - 98: I1IIiI1 * iIii1I11I1II1 . oO0O0ooO0Oo * Oo / ii11ii1ii + oO0
 IIi1iiIi1 = ii11Iiii ( iiIiii1IIIII )
 Oo0oO0ooo . update ( 9 , "" , "[COLORred]Checking Source 1/10[/COLOR]" )
 iIIii = ii11Iiii ( O00O0Oooo0oO )
 Oo0oO0ooo . update ( 18 , "" , "[COLORred]Checking Source 2/10[/COLOR]" )
 iiI1ii111 = ii11Iiii ( oOO0O00Oo0O0o )
 Oo0oO0ooo . update ( 27 , "" , "[COLORred]Checking Source 3/10[/COLOR]" )
 OoOO = ii11Iiii ( Ii1iiI1 )
 Oo0oO0ooo . update ( 36 , "" , "[COLORred]Checking Source 4/10[/COLOR]" )
 IIIIIiI11Ii = ii11Iiii ( o0ooOOoO0oO0 )
 Oo0oO0ooo . update ( 45 , "" , "[COLORred]Checking Source 5/10[/COLOR]" )
 Iiii1Ii1I = ii11Iiii ( oooo )
 Oo0oO0ooo . update ( 54 , "" , "[COLORred]Checking Source 6/10[/COLOR]" )
 oooOOOOOi1iIii = ii11Iiii ( o0o0oo0Ooo )
 Oo0oO0ooo . update ( 63 , "" , "[COLORred]Checking Source 7/10[/COLOR]" )
 o0O0ooooooo00 = ii11Iiii ( iI1i )
 Oo0oO0ooo . update ( 75 , "" , "[COLORred]Checking Source 8/10[/COLOR]" )
 I1111ii11IIII = ii11Iiii ( i11I )
 Oo0oO0ooo . update ( 81 , "" , "[COLORred]Checking Source 9/10[/COLOR]" )
 IiIi1II111I = ii11Iiii ( o0oO0o0oo0O0 )
 Oo0oO0ooo . update ( 100 , "" , "[COLORred]Checking Source 10/10[/COLOR]" )
 if 80 - 80: oO0O0ooO0Oo / Ii11I
 if 21 - 21: Oo - iIii1I11I1II1 - O00Oo000ooO0
 if IIi1iiIi1 != 'Failed' :
  III1I1Iii11i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><span>.+?</span></a>' , re . DOTALL ) . findall ( IIi1iiIi1 )
  for iiIiii1IIIII , i1iIIIi1i in III1I1Iii11i :
   if I1I1I in i1iIIIi1i . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , iiIiii1IIIII , 30015 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if iIIii != 'Failed' :
  o00O0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIIii )
  for oOO00oOOo , i1iIIIi1i in o00O0O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O00O0Oooo0oO + oOO00oOOo ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if iiI1ii111 != 'Failed' :
  II1i11i1iIi11 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iiI1ii111 )
  for oOO00oOOo , i1iIIIi1i in II1i11i1iIi11 :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOO0O00Oo0O0o + oOO00oOOo ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if OoOO != 'Failed' :
  I1iiIi1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOO )
  for oOO00oOOo , i1iIIIi1i in I1iiIi1 :
   if I1I1I in i1iIIIi1i . lower ( ) :
    O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1iiI1 + oOO00oOOo ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Source 4 Links" )
 if IIIIIiI11Ii != 'Failed' :
  i1iiiIi1Iii = [ ]
  o0oO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIIIiI11Ii )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in o0oO0O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    if i1iIIIi1i in i1iiiIi1Iii :
     pass
    else :
     i1I1iI ( ( '[COLORgreen]' + i1iIIIi1i + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iiIiii1IIIII , 1016 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
     i1iiiIi1Iii . append ( i1iIIIi1i )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     OOO ( 'tvshows' , 'Media Info 3' )
 if Iiii1Ii1I != 'Failed' :
  OO0ooooO0 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Iiii1Ii1I )
  for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in OO0ooooO0 :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iiIiii1IIIII , 7067 , oOO0O00oO0Ooo )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 53 - 53: I1IiI * oOo00oOO0O - I1IIiI1 / oOo00oOO0O + OoOoOO00 % ii
    OOO ( 'tvshows' , 'Media Info 3' )
 if oooOOOOOi1iIii != 'Failed' :
  o00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oooOOOOOi1iIii )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in o00O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    oo0OooOOo0 ( ( '[COLORgreen]' + i1iIIIi1i + '- source Redemption[/COLOR]' ) , iiIiii1IIIII , 222 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 92 - 92: Oo - O00Oo000ooO0
    OOO ( 'tvshows' , 'Media Info 3' )
 if o0O0ooooooo00 != 'Failed' :
  IIi11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0O0ooooooo00 )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in IIi11 :
   if I1I1I in i1iIIIi1i . lower ( ) :
    oo0OooOOo0 ( ( '[COLORgreen]' + i1iIIIi1i + '- source Reaper[/COLOR]' ) , iiIiii1IIIII , 222 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 73 - 73: oO0 + ii11ii1ii
    OOO ( 'tvshows' , 'Media Info 3' )
 if I1111ii11IIII != 'Failed' :
  o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1111ii11IIII )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in o0o :
   if I1I1I in i1iIIIi1i . lower ( ) :
    oo0OooOOo0 ( ( '[COLORgreen]' + i1iIIIi1i + '- source Herovision[/COLOR]' ) , iiIiii1IIIII , 222 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 46 - 46: I1IiI - O0
    OOO ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: oOo00oOO0O + Oo * iIii1I11I1II1 . OOOo0 * oOo00oOO0O
 if IiIi1II111I != 'Failed' :
  ii1i11ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIi1II111I )
  for iiIiii1IIIII , i1I1i111Ii , i1iIIIi1i in ii1i11ii :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '- source Silent Hunter[/COLOR]' ) , iiIiii1IIIII , 222 , i1I1i111Ii )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 11 - 11: Oo - O0
    OOO ( 'tvshows' , 'Media Info 3' )
 OOoI111 = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 65 - 65: Oo * O0 / oO0O0ooO0Oo . O00Oo000ooO0 % Oo
 for I1III1 in OOoI111 :
  Iiii1ii = ooooooO0oo + I1III1 + OooO0
  i1Ii1i1 = iii1i1iiiiIi ( Iiii1ii )
  if i1Ii1i1 != 'Failed' :
   OoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Ii1i1 )
   for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in OoOo :
    if I1I1I in i1iIIIi1i . lower ( ) :
     oo0OooOOo0 ( '[COLORgreen]' + i1iIIIi1i + ' - Source Pandoras[/COLOR]' , iiIiii1IIIII , 222 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 33 - 33: i1IIi / O00Oo000ooO0 - i1IIi . Oo
     OOO ( 'tvshows' , 'Media Info 3' )
     if 18 - 18: Oo / O0 + oOOoo0Oo
 o0oO0oo0000OO = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 65 - 65: i1IIi . ii11ii1ii / oO0
 if 11 - 11: I1IIiI1 * oO0 / oO0 - Ii11I
 for I1III1 in o0oO0oo0000OO :
  Iiii1ii = IIIi + I1III1
  OoO0o0OOOO = ii11Iiii ( Iiii1ii )
  if IIIIIiI11Ii != 'Failed' :
   II1i = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OoO0o0OOOO )
   for oOO00oOOo , i1iIIIi1i in II1i :
    if I1I1I in i1iIIIi1i . lower ( ) :
     O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IIIi + I1III1 + oOO00oOOo ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 62 - 62: oOo00oOO0O / ii % Oo . OoooooooOO / i11iIiiIii / O00Oo000ooO0
     OOO ( 'tvshows' , 'Media Info 3' )
def OooO0O0Ooo ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  IIii11I1 ( url )
  if 85 - 85: OOooOOo / O00Oo000ooO0
  if 67 - 67: oOo00oOO0O % ii
def ii1iiIi ( ) :
 if 21 - 21: ii11ii1ii
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 iI1i = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( I1I1I ) . replace ( ' ' , '+' )
 iiIiii1IIIII = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 O00O0Oooo0oO = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 oOO0O00Oo0O0o = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 Ii1iiI1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 o0ooOOoO0oO0 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1I1I ) . replace ( ' ' , '+' )
 oo00I1IiI1IIiI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 oooo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 o0o0oo0Ooo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 84 - 84: O0 / OOOo0 % i1IIi % i1IIi / Ooo00oOo00o / ii
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0O0ooooooo00 = ii11Iiii ( iI1i )
 Oo0oO0ooo . update ( 0 , "" , "[COLORred]Checking Source 1/9[/COLOR]" )
 IIi1iiIi1 = ii11Iiii ( iiIiii1IIIII )
 Oo0oO0ooo . update ( 14 , "" , "[COLORred]Checking Source 2/9[/COLOR]" )
 iIIii = ii11Iiii ( O00O0Oooo0oO )
 Oo0oO0ooo . update ( 28 , "" , "[COLORred]Checking Source 3/9[/COLOR]" )
 iiI1ii111 = ii11Iiii ( oOO0O00Oo0O0o )
 Oo0oO0ooo . update ( 40 , "" , "[COLORred]Checking Source 4/9[/COLOR]" )
 OoOO = ii11Iiii ( Ii1iiI1 )
 Oo0oO0ooo . update ( 52 , "" , "[COLORred]Checking Source 5/9[/COLOR]" )
 IIIIIiI11Ii = cloudflare . source ( o0ooOOoO0oO0 )
 Oo0oO0ooo . update ( 64 , "" , "[COLORred]Checking Source 6/9[/COLOR]" )
 OoO0o0OOOO = ii11Iiii ( oo00I1IiI1IIiI )
 Oo0oO0ooo . update ( 76 , "" , "[COLORred]Checking Source 7/9[/COLOR]" )
 Iiii1Ii1I = ii11Iiii ( oooo )
 Oo0oO0ooo . update ( 88 , "" , "[COLORred]Checking Source 8/9[/COLOR]" )
 oooOOOOOi1iIii = ii11Iiii ( o0o0oo0Ooo )
 Oo0oO0ooo . update ( 100 , "" , "[COLORred]Checking Source 9/9[/COLOR]" )
 if 28 - 28: oO0 . OoooooooOO + OOooOOo + oO0O0ooO0Oo % oOOoo0Oo
 if oooOOOOOi1iIii != 'Failed' :
  o00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oooOOOOOi1iIii )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in o00O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    i1I1iI ( ( '[COLORgreen]' + i1iIIIi1i + '- source HeroVision[/COLOR]' ) , iiIiii1IIIII , 1016 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 80 - 80: Oo
    OOO ( 'tvshows' , 'Media Info 3' )
    if 86 - 86: ii11ii1ii * oOo00oOO0O . I1IiI / Oo + ii
 if Iiii1Ii1I != 'Failed' :
  OO0ooooO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Iiii1Ii1I )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in OO0ooooO0 :
   if I1I1I in i1iIIIi1i . lower ( ) :
    i1I1iI ( ( '[COLORgreen]' + i1iIIIi1i + '- source Reaper[/COLOR]' ) , iiIiii1IIIII , 1016 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 8 - 8: I1IiI
    OOO ( 'tvshows' , 'Media Info 3' )
    if 16 - 16: OOooOOo . oOo00oOO0O
 if o0O0ooooooo00 != 'Failed' :
  IIi11 = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( o0O0ooooooo00 )
  for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in IIi11 :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + ' CoolSeries[/COLOR]' , iiIiii1IIIII , 7052 , oOO0O00oO0Ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 50 - 50: oO0 * I1IiI + ii11ii1ii - i11iIiiIii + Oo * ii11ii1ii
    OOO ( 'tvshows' , 'Media Info 3' )
 if IIi1iiIi1 != 'Failed' :
  Iiii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1iiIi1 )
  for i1iIIIi1i in Iiii :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( '[COLORgreen]' + ( i1iIIIi1i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( iiIiii1IIIII + i1iIIIi1i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 20 - 20: O00Oo000ooO0 / OOooOOo % I1IiI
    OOO ( 'tvshows' , 'Media Info 3' )
 if iIIii != 'Failed' :
  o00O0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIii )
  for i1iIIIi1i in o00O0O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( i1iIIIi1i + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00O0Oooo0oO + i1iIIIi1i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 69 - 69: O00Oo000ooO0 - i1IIi % oOOoo0Oo . Ii11I - Ii11I
    OOO ( 'tvshows' , 'Media Info 3' )
 if iiI1ii111 != 'Failed' :
  II1i11i1iIi11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI1ii111 )
  for i1iIIIi1i in o00O0O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( i1iIIIi1i + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOO0O00Oo0O0o + i1iIIIi1i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 65 - 65: Ii11I + OoOoOO00
    OOO ( 'tvshows' , 'Media Info 3' )
 if OoOO != 'Failed' :
  I1iiIi1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OoOO )
  for i1iIIIi1i in o00O0O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( i1iIIIi1i + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1iiI1 + i1iIIIi1i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 61 - 61: i11iIiiIii * ii % Oo * O00Oo000ooO0 - OoooooooOO - Ooo00oOo00o
    OOO ( 'tvshows' , 'Media Info 3' )
 if IIIIIiI11Ii != 'Failed' :
  o0oO0O = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIIIIiI11Ii )
  for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in o0oO0O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + ' - Source - Dizi[/COLOR]' , iiIiii1IIIII , 8062 , oOO0O00oO0Ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 83 - 83: oO0 / Ii11I
    OOO ( 'tvshows' , 'Media Info 3' )
 if OoO0o0OOOO != 'Failed' :
  II1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO0o0OOOO )
  for iiIiii1IIIII , i1I1i111Ii , Ii1IIiI1i , I1IIIIiii1i , i1iIIIi1i in II1i :
   if I1I1I in i1iIIIi1i . lower ( ) :
    i1I1iI ( ( '[COLORgreen]' + i1iIIIi1i + '- Source Scooby[/COLOR]' ) , iiIiii1IIIII , 1016 , i1I1i111Ii , I1IIIIiii1i , Ii1IIiI1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 39 - 39: I1IIiI1 + oOo00oOO0O
    OOO ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: OOOo0 % oOo00oOO0O . Oo * OOOo0
 OoO0oO0oo0O = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 82 - 82: OoooooooOO . oO0O0ooO0Oo
 for I1III1 in OoO0oO0oo0O :
  Iiii1ii = ooooooO0oo + I1III1 + OooO0
  I1111ii11IIII = iii1i1iiiiIi ( Iiii1ii )
  if I1111ii11IIII != 'Failed' :
   o0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1111ii11IIII )
   for i1iIIIi1i , Ii1IIiI1i , iiIiii1IIIII , oOO0O00oO0Ooo , ooo , oOo0OOoooO in o0o :
    if I1I1I in i1iIIIi1i . lower ( ) :
     i1I1iI ( '[COLORgreen]' + i1iIIIi1i + ' - Source Pandoras[/COLOR]' , iiIiii1IIIII , oOo0OOoooO , oOO0O00oO0Ooo , ooo , Ii1IIiI1i )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 26 - 26: ii + I1IIiI1 - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
     OOO ( 'tvshows' , 'Media Info 3' )
     if 68 - 68: O0
     if 76 - 76: ii11ii1ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO000OO ( ) :
 if 43 - 43: oO0 * O00Oo000ooO0 % Ii11I
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 iiIiii1IIIII = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1iiIi1 = iii1i1iiiiIi ( iiIiii1IIIII )
 Iiii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for i1iIIIi1i , oOO0O00oO0Ooo , iiiI11 in Iiii :
  o0o00OOOO = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOO0O00oO0Ooo ) . replace ( '\\' , '' )
  if I1I1I in i1iIIIi1i . lower ( ) :
   ii1IIIIiI11 ( i1iIIIi1i , '' , 7022 , o0o00OOOO )
   if 42 - 42: oO0 * oOOoo0Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: oOOoo0Oo . Ooo00oOo00o / ii
 if 41 - 41: Ooo00oOo00o . O00Oo000ooO0 * I1IIiI1 * O00Oo000ooO0
def ooOO ( url ) :
 O0o = cloudflare . source ( url )
 Iiii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( O0o )
 for url , IioO0O , iI1iIIiiii , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( ( IioO0O ) . replace ( 'Sezon' , ' Season ' ) + ( iI1iIIiiii ) . replace ( 'Bölüm' , ' Episode ' ) + i1iIIIi1i , url , 8063 , '' )
  if 68 - 68: OoooooooOO * iIii1I11I1II1 + i1IIi - i1IIi
  if 76 - 76: Ooo00oOo00o . OoooooooOO % O00Oo000ooO0 * oO0O0ooO0Oo
  if 23 - 23: I1IIiI1 + iIii1I11I1II1
  if 14 - 14: O0 % I1IIiI1 % oO0O0ooO0Oo * ii
def o0OOO00ooo ( url ) :
 O0o = cloudflare . source ( url )
 Iiii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( O0o )
 for url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , url , 222 , '' )
  if 9 - 9: oOo00oOO0O * Oo . oO0 * i11iIiiIii - O0
  if 54 - 54: OOOo0 * Ii11I + OOooOOo % i1IIi - OOooOOo + I1IiI
  if 15 - 15: I1IiI * ii + Ii11I . oOo00oOO0O % OOOo0 - oO0
  if 13 - 13: I1IiI % I1IiI % Oo % OOOo0 * i1IIi % oOo00oOO0O
def O0i1I11I ( ) :
 if 34 - 34: oO0O0ooO0Oo * OOooOOo + Ii11I / I1IIiI1 / Oo
 O0o = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Iiii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O0o )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i , iI1iIIiiii in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i + '  -  ' + ( iI1iIIiiii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiIiii1IIIII , 8063 , oOO0O00oO0Ooo )
  if 14 - 14: oOOoo0Oo - oOo00oOO0O * OoooooooOO + Ii11I . OoOoOO00
def i1i1I11i1I ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Iiii = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i , oOO0O00oO0Ooo in Iiii :
  O0Oo00oO0O00 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 8002 , oOO0O00oO0Ooo )
def O0oII1IIiiI1 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for oOO0O00oO0Ooo , time , url , i1iIIIi1i , I1IIII1ii in Iiii :
  i1I1iI ( '%s %s' % ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , time ) , url , 1015 , oOO0O00oO0Ooo , I1IIII1ii )
  if 96 - 96: Ii11I + Ii11I % I1IIiI1 % Ii11I
def IiiI1I ( ) :
 if 3 - 3: OoOoOO00 - oO0O0ooO0Oo % I1IiI / ii
 ii1IIIIiI11 ( 'Coronation Street' , '' , 8001 , '' )
 ii1IIIIiI11 ( 'Eastenders' , '' , 8002 , '' )
 ii1IIIIiI11 ( 'Emmerdale' , '' , 8003 , '' )
 ii1IIIIiI11 ( 'Hollyoaks' , '' , 8004 , '' )
 ii1IIIIiI11 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 44 - 44: O0 . oO0O0ooO0Oo * oOOoo0Oo / i11iIiiIii
 if 56 - 56: I1IiI % ii11ii1ii - oO0O0ooO0Oo % iIii1I11I1II1
 if 76 - 76: OoooooooOO * OoooooooOO - oOOoo0Oo - iIii1I11I1II1 . OoooooooOO / ii11ii1ii
 if 86 - 86: oO0
def oO0oo0O0 ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( 'http://uksoapshare.blogspot.co.uk/' )
 Iiii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'Holly' in i1iIIIi1i :
   oOO0O00oO0Ooo = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iiIiii1IIIII :
    O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiIiii1IIIII . replace ( '\\/' , '/' ) , 8006 , oOO0O00oO0Ooo )
   else :
    pass
    if 66 - 66: Ii11I - oO0 - Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 54 - 54: oOOoo0Oo . i1IIi
def i1IiIiIiiI1 ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( 'http://uksoapshare.blogspot.co.uk/' )
 Iiii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'East' in i1iIIIi1i :
   oOO0O00oO0Ooo = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iiIiii1IIIII :
    O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiIiii1IIIII . replace ( '\\/' , '/' ) , 8006 , oOO0O00oO0Ooo )
   else :
    pass
    if 41 - 41: OoOoOO00
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: O0 - oO0 % OoooooooOO % Ii11I + oOOoo0Oo
def o0O ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( 'http://uksoapshare.blogspot.co.uk/' )
 Iiii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'Emmer' in i1iIIIi1i :
   oOO0O00oO0Ooo = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iiIiii1IIIII :
    O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiIiii1IIIII . replace ( '\\/' , '/' ) , 8006 , oOO0O00oO0Ooo )
   else :
    pass
    if 3 - 3: iIii1I11I1II1 . OOooOOo . ii . Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: i1IIi * i11iIiiIii
def Ii1i1i ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( 'http://uksoapshare.blogspot.co.uk/' )
 Iiii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'Coro' in i1iIIIi1i :
   oOO0O00oO0Ooo = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iiIiii1IIIII :
    O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiIiii1IIIII . replace ( '\\/' , '/' ) , 8006 , oOO0O00oO0Ooo )
   else :
    pass
    if 83 - 83: oOo00oOO0O - ii11ii1ii * ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: Oo * OOOo0
def OO0OooOo ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( 'http://uksoapshare.blogspot.co.uk/' )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'Celeb' in i1iIIIi1i :
   oOO0O00oO0Ooo = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iiIiii1IIIII :
    O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiIiii1IIIII . replace ( '\\/' , '/' ) , 8006 , oOO0O00oO0Ooo )
   else :
    pass
    if 13 - 13: O0 % oO0 % oOo00oOO0O
def Ii11IiI111 ( name , url ) :
 IIiii11ii1II1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIiii11ii1II1 :
  o0OO000O = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  i111iIi1i1II1 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( i111iIi1i1II1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  i111iIi1i1II1 = open_url ( url )
  O000o0000O = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( i111iIi1i1II1 ) [ - 1 ]
  o0OO000O = O000o0000O . replace ( '\\/' , '/' )
 i1i = xbmcgui . ListItem ( name , '' , '' )
 i1i . setPath ( o0OO000O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1i )
 if 61 - 61: Ii11I * OOooOOo * O0 / oOOoo0Oo
 if 52 - 52: Oo + iIii1I11I1II1 + i1IIi * oO0O0ooO0Oo - OoOoOO00 . OoOoOO00
def Iii1I1iI ( ) :
 iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 Iiii = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( html )
 o00O0O = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( html )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iiIiii1IIIII , 7071 , ii11iIi1I + 'popcorn.png' )
 for iiIiii1IIIII , i1iIIIi1i in o00O0O :
  ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iiIiii1IIIII , 7071 , ii11iIi1I + 'popcorn.png' )
  if 62 - 62: ii + Oo / i11iIiiIii
def ooOoOo ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Iiii = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  if 'Movies' in i1iIIIi1i :
   ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://www.snagfilms.com' + ( iiIiii1IIIII ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def iIi ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 Iiii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOO0O00oO0Ooo )
 for url in o00O0O :
  ii1IIIIiI11 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 40 - 40: OoooooooOO + oOOoo0Oo
  if 11 - 11: OoooooooOO * Ooo00oOo00o + Oo
def ooO0 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Iiii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOO0O00oO0Ooo )
  if 91 - 91: OoooooooOO
  if 48 - 48: Ooo00oOo00o / oO0O0ooO0Oo - OOOo0 % oO0O0ooO0Oo
def O0OooooO0o0O0 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOO0O00oO0Ooo )
  if 74 - 74: I1IiI / i1IIi % OoooooooOO
def o00o0o000Oo ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  Oooo00OOo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 6 - 6: ii / OOOo0 / I1IiI
def Oooo00OOo ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 51 - 51: OoOoOO00 / Oo / OOOo0 + i11iIiiIii
  if 5 - 5: oOo00oOO0O
  if 22 - 22: iIii1I11I1II1 * O00Oo000ooO0 / Oo
  if 31 - 31: i11iIiiIii
def O0O0O ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  if '(cooltvseries.com)' in i1iIIIi1i :
   O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , i1iIIIi1i in o00O0O :
  if '(cooltvseries.com)' in i1iIIIi1i :
   O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def II1io0Oo00oOO ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  I11Ii ( ( url ) . replace ( ' ' , '%20' ) )
  if 73 - 73: oOo00oOO0O / OoooooooOO . OoOoOO00 - I1IIiI1 * oO0 * I1IIiI1
  if 45 - 45: O0 * O00Oo000ooO0 + i11iIiiIii - Ii11I - iIii1I11I1II1
def I11I111i1I1 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 Iiii = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i , oOO0O00oO0Ooo in Iiii :
  O0Oo00oO0O00 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( iiIiii1IIIII ) ) , 222 , oOO0O00oO0Ooo )
  if 41 - 41: OoooooooOO / i1IIi
def OO0Ooo0Oooo ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for oOO0O00oO0Ooo , url , i1iIIIi1i in Iiii :
  if 'youtu' in url :
   O0Oo00oO0O00 ( ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + oOO0O00oO0Ooo )
 for url in next :
  ii1IIIIiI11 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 4 - 4: I1IIiI1
def oOo0OoOOOo0 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 55 - 55: ii + O0 / oOOoo0Oo % oO0 / OoooooooOO
def O00o0OO0OO0oo ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi
 Iiii = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 222 , oOO0O00oO0Ooo )
  if 59 - 59: OoooooooOO % oOo00oOO0O / O00Oo000ooO0 + OoooooooOO . OoooooooOO
  if 87 - 87: oOo00oOO0O + ii
  if 3 - 3: OoooooooOO
  if 40 - 40: O0 . O00Oo000ooO0 / iIii1I11I1II1 * OOooOOo
  if 73 - 73: Oo - oOOoo0Oo . ii % i1IIi . O0
def I1oO0oOOOooo ( ) :
 if 6 - 6: iIii1I11I1II1 - iIii1I11I1II1 % OOooOOo / iIii1I11I1II1 * O00Oo000ooO0
 ii1IIIIiI11 ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ii1IIIIiI11 ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 3 - 3: Ii11I . I1IIiI1 / Oo
 if 89 - 89: OoooooooOO . iIii1I11I1II1 . Oo * iIii1I11I1II1 - O00Oo000ooO0
def OoOO0o0o0 ( Cat_Name ) :
 if 35 - 35: O00Oo000ooO0
 O0oo0oOoO00 = False
 i1ii1iIi = '0'
 if Cat_Name == 'All Channels' : O0oo0oOoO00 = True
 if Cat_Name == 'Entertainment' : i1ii1iIi = '1'
 if Cat_Name == 'Movies' : i1ii1iIi = '2'
 if Cat_Name == 'Music' : i1ii1iIi = '3'
 if Cat_Name == 'News' : i1ii1iIi = '4'
 if Cat_Name == 'Sports' : i1ii1iIi = '5'
 if Cat_Name == 'Documentary' : i1ii1iIi = '6'
 if Cat_Name == 'Kids' : i1ii1iIi = '7'
 if Cat_Name == 'Food' : i1ii1iIi = '8'
 if Cat_Name == 'Religious' : i1ii1iIi = '9'
 if Cat_Name == 'USA Channels' : i1ii1iIi = '10'
 if Cat_Name == 'Other' : i1ii1iIi = '11'
 if 43 - 43: oO0O0ooO0Oo + oOOoo0Oo + i1IIi - I1IiI + OOooOOo
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Iiii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 print 'Len Match: >>>' + str ( len ( Iiii ) )
 for i1iIIIi1i , oOO0O00oO0Ooo , iiiI11 in Iiii :
  o0o00OOOO = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOO0O00oO0Ooo ) . replace ( '\\' , '' )
  if iiiI11 == i1ii1iIi :
   ii1IIIIiI11 ( i1iIIIi1i , '' , 7022 , o0o00OOOO )
  elif O0oo0oOoO00 == True :
   ii1IIIIiI11 ( i1iIIIi1i , '' , 7022 , o0o00OOOO )
  else : pass
  if 54 - 54: ii11ii1ii + ii11ii1ii + oOo00oOO0O % i1IIi % i11iIiiIii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 100 - 100: ii11ii1ii
def OOOoo000o0oo0 ( Search_Name ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Iiii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 Iiii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for oOO0O00oO0Ooo , iiIiii1IIIII , O00O0Oooo0oO , oOO0O00Oo0O0o in Iiii :
  o0o00OOOO = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOO0O00oO0Ooo ) . replace ( '\\' , '' )
  O0Oo00oO0O00 ( Search_Name + ': Link 1' , ( iiIiii1IIIII ) . replace ( '\\' , '' ) , 222 , o0o00OOOO )
  O0Oo00oO0O00 ( Search_Name + ': Link 2' , ( O00O0Oooo0oO ) . replace ( '\\' , '' ) , 222 , o0o00OOOO )
  O0Oo00oO0O00 ( Search_Name + ': Link 3' , ( oOO0O00Oo0O0o ) . replace ( '\\' , '' ) , 222 , o0o00OOOO )
  if 71 - 71: oO0 . oOo00oOO0O + Ii11I
def IiIiiI1ii111 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Iiii = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , iiIiii1IIIII in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , ( iiIiii1IIIII ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def i11ii1 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Iiii = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , iiIiii1IIIII in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , ( iiIiii1IIIII ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def Ii111I11 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Iiii = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , iiIiii1IIIII in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , ( iiIiii1IIIII ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 51 - 51: OoooooooOO + OOooOOo * iIii1I11I1II1 * ii / i1IIi
def I11IiI1i ( url ) :
 url
 OooO = xbmcgui . ListItem ( i1iIIIi1i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OooO )
 return
 if 85 - 85: OoOoOO00
 if 55 - 55: ii11ii1ii
def oOoo0OO0 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( i111iIi1i1II1 )
 for url , Ii1IIiI1i , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  i1I1iI ( i1iIIIi1i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOO0O00oO0Ooo , '' , ( Ii1IIiI1i ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  OOO ( 'tvshows' , 'Media Info 3' )
 for url in o00O0O :
  ii1IIIIiI11 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 5 - 5: i11iIiiIii * Oo
def i111 ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for url , Ii1IIiI1i , oOO0O00oO0Ooo in Iiii :
  oo0OooOOo0 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOO0O00oO0Ooo , '' , Ii1IIiI1i )
  OOO ( 'tvshows' , 'Media Info 3' )
 iiI1I1IIi11i1 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 for o0o0oO in iiI1I1IIi11i1 :
  IiiI1i111I1i = ( o0o0oO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  i1I1iI ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOO0O00oO0Ooo , '' , IiiI1i111I1i )
  if 97 - 97: Ii11I % OOOo0 * OOOo0 % Oo
def o0OoOooOO0o0 ( INFO ) :
 o00OO00OoO ( 'info for workout' , INFO )
 if 55 - 55: O0 % OOOo0 . OoooooooOO * Oo / OoooooooOO . oO0O0ooO0Oo
 if 26 - 26: I1IIiI1 / iIii1I11I1II1 - iIii1I11I1II1
 if 57 - 57: I1IIiI1
def IiI11I1Ii11II ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , url , 9031 , ii11iIi1I + 'icon.png' )
def oo0ooOoOOoO ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , url , 9032 , ii11iIi1I + 'icon.png' )
def Oo0000o ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , url in Iiii :
  if '://' in i1iIIIi1i :
   pass
   O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def iI1IiiiIIiiII ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , url in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , url , 222 , ii11iIi1I + 'icon.png' )
  if 94 - 94: I1IiI + I1IIiI1 . oO0
  if 69 - 69: O0 - O0
  if 41 - 41: I1IIiI1 % OOooOOo
def oo0O0oOOO0o ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 Iiii = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , 'http://www.disclose.tv/' + iiIiii1IIIII , 7010 , ii11iIi1I + 'disclose.png' )
  if 70 - 70: Oo % oO0O0ooO0Oo . ii11ii1ii
  if 8 - 8: OOOo0 - O00Oo000ooO0 * oOo00oOO0O % OoooooooOO / I1IiI
def I1I ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i , oOO0O00oO0Ooo in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , 'http://www.disclose.tv/' + url , 7011 , oOO0O00oO0Ooo )
 for url in next :
  ii1IIIIiI11 ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 53 - 53: I1IiI
  if 84 - 84: Ooo00oOo00o
def o0OOi11Ii1 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  if 'http' in url :
   O0Oo00oO0O00 ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , i1iIIIi1i in o00O0O :
  O0Oo00oO0O00 ( i1iIIIi1i , url , 222 , ii11iIi1I + 'disclose.png' )
  if 2 - 2: I1IIiI1 - ii % Ooo00oOo00o + OOooOOo + oO0O0ooO0Oo - iIii1I11I1II1
  if 18 - 18: ii11ii1ii / Oo - oOOoo0Oo
def oO000 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 81 - 81: ii
def o00oOOo ( name , url , img ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 iIIi = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIi1iiIi1 )
 i1I111iIii1i1 = len ( iIIi )
 if 80 - 80: O00Oo000ooO0 / i11iIiiIii + OoooooooOO
 if 38 - 38: ii11ii1ii % oO0 + i1IIi * OoooooooOO * ii
 if i1I111iIii1i1 == 1 :
  for OoO0o0OO in iIIi :
   OoO0o0OO = OoO0o0OO . replace ( 'player' , 'watch' )
   II11IiI1 = OoO0o0OO + '&fv=&sou='
   iIIi11i = iii1i1iiiiIi ( II11IiI1 )
   III = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( iIIi11i )
   for i111Iii in III :
    iiIi111Ii1II = False
    Resolve ( i111Iii )
    if 58 - 58: I1IiI
 elif i1I111iIii1i1 > 1 :
  if 60 - 60: OoOoOO00
  for OoO0o0OO in iIIi :
   oO0OOoo = iii1i1iiiiIi ( OoO0o0OO )
   oOo00oooOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo )
   IIIIi11iiiIi1 = oOo00oooOO
   IIIIi11iiiIi1 = ( str ( IIIIi11iiiIi1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIIIi11iiiIi1
   O0Oo00oO0O00 ( 'DOUBLE LINK' , IIIIi11iiiIi1 , 424 , '' )
   if 12 - 12: i1IIi / oOo00oOO0O
   for url in oOo00oooOO :
    ii1IIIIiI11 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     O00O0Oooo0oO = Google . resolve ( url )
    except :
     pass
    try :
     o0OOo0O = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( O00O0Oooo0oO ) )
     for oo00i1i11I1I1 , OOOOOoooO in o0OOo0O :
      if 59 - 59: ii % oO0
      HD_URLS . append ( oo00i1i11I1I1 )
      SD_URLS . append ( OOOOOoooO )
    except :
     pass
 else :
  pass
  if 36 - 36: OoooooooOO
def IiII1i ( ) :
 if 32 - 32: OOOo0
 if 47 - 47: ii11ii1ii * ii + iIii1I11I1II1 - ii / I1IIiI1
 ii1IIIIiI11 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 86 - 86: I1IIiI1
 ii1IIIIiI11 ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 43 - 43: OOOo0 / oOOoo0Oo / oO0 + iIii1I11I1II1 + OoooooooOO
 if 33 - 33: OoOoOO00 - I1IIiI1 - oO0
def oO00oOoo00o0 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( 'http://cnfstudio.com/' )
 Iiii = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , 'http://cnfstudio.com/genre/' + iiIiii1IIIII , 7003 , ii11iIi1I + 'icon.png' )
  if 41 - 41: ii / Ii11I + oOOoo0Oo + oO0
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 13 - 13: i11iIiiIii - i11iIiiIii . iIii1I11I1II1
if 33 - 33: OoooooooOO + O00Oo000ooO0 / O00Oo000ooO0 + O00Oo000ooO0 * I1IIiI1
def I1i ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 IiiiIi1111I = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( i111iIi1i1II1 )
 for oOO0O00oO0Ooo , url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOO0O00oO0Ooo )
 IiiiIi1111I = IiiiIi1111I
 for url in IiiiIi1111I :
  ii1IIIIiI11 ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 45 - 45: OOooOOo
def Oo0ooooO0O0oo ( url ) :
 if 98 - 98: i11iIiiIii
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  OO0ooo0o0O0Oooooo = url + '&fv=&sou='
  OO0ooo0o0O0Oooooo = OO0ooo0o0O0Oooooo . replace ( 'player' , 'watch' )
  IiiI = OoOoO0oO00O ( OO0ooo0o0O0Oooooo )
  ooo0OIi1iiIIi1i = OoOoO0oO00O ( url )
  if 44 - 44: OOooOOo
  if 51 - 51: OoOoOO00
def OoOoO0oO00O ( url ) :
 if 10 - 10: Ooo00oOo00o % Ooo00oOo00o / OOooOOo - I1IiI
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  IIii11I1 ( url )
  if 44 - 44: oO0 - O0 / OoOoOO00 . iIii1I11I1II1 . i1IIi
  if 63 - 63: iIii1I11I1II1 + I1IIiI1 % i1IIi / OOOo0 % OoOoOO00
def OO0 ( ) :
 i1I1iI ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 48 - 48: i1IIi * OOOo0
def iiiIIiii11I1 ( url ) :
 Iiii = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for oo0O , i1iIIIi1i , url in Iiii :
  O0Oo00oO0O00 ( i1iIIIi1i , url , 222 , ii11iIi1I + 'streams.png' )
  if 100 - 100: OoooooooOO - O0 . oOo00oOO0O / oOo00oOO0O + OoOoOO00 * I1IiI
  if 37 - 37: Oo
def O00Oo00o00O ( ) :
 i1I1iI ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 15 - 15: oOo00oOO0O / Oo * oOo00oOO0O
 if 20 - 20: oO0 - Ii11I * Ooo00oOo00o * OOooOOo * Ii11I / I1IIiI1
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
iiiIIIII11i1I = 'https://addons.tvaddons.ag/'
if 69 - 69: oO0 . Ii11I - OOOo0
def IiIiIi ( ) :
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 o0OOOOOo0 = 'https://addons.tvaddons.ag/search/?keyword=' + i1Ii11i1i
 IIi1iiIi1 = iii1i1iiiiIi ( o0OOOOOo0 )
 Iiii = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , O000OOO , i1iIIIi1i in Iiii :
  i1I1iI ( i1iIIIi1i , iiIiii1IIIII , 10054 , 'https://addons.tvaddons.ag/' + O000OOO , i1iiIII111ii , '' )
  if 36 - 36: Ii11I * oO0O0ooO0Oo
  if 16 - 16: OoOoOO00
def oooOO0OO0 ( ) :
 IIi1iiIi1 = iii1i1iiiiIi ( iiiIIIII11i1I )
 Iiii = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1iiIi1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  if 'Repositories' in i1iIIIi1i :
   pass
  elif 'Services' in i1iIIIi1i :
   pass
  elif 'International' in i1iIIIi1i :
   pass
  else :
   i1I1iI ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , iiIiii1IIIII , 10053 , 'https://addons.tvaddons.ag/' + oOO0O00oO0Ooo , i1iiIII111ii , '' )
   if 10 - 10: OOOo0 / ii11ii1ii
   if 68 - 68: Ii11I - OoooooooOO
def Addon ( url ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 IiIII = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIi1iiIi1 )
 for url in IiIII :
  i1I1iI ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 Iiii = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1iiIi1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  if 'Please' in i1iIIIi1i :
   pass
  else :
   i1I1iI ( i1iIIIi1i , url , 10054 , 'https://addons.tvaddons.ag/' + oOO0O00oO0Ooo , i1iiIII111ii , '' )
   if 38 - 38: iIii1I11I1II1 + OOOo0 + oOo00oOO0O * Ooo00oOo00o + Ooo00oOo00o + i11iIiiIii
   if 56 - 56: oO0O0ooO0Oo + OOOo0 - OOooOOo / OOooOOo . OoOoOO00 - oO0O0ooO0Oo
def i1oo ( url , name ) :
 IIi1iiIi1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<a href="(.+?)"' ) . findall ( IIi1iiIi1 )
 for url in Iiii :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   O0oOOo0Oo = os . path . join ( ooo00Ooo , name + '.zip' )
   try :
    os . remove ( O0oOOo0Oo )
   except :
    pass
   downloader . download ( url , O0oOOo0Oo , Oo0oO0ooo )
   oO0i1iI = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oO0i1iI
   print '======================================='
   extract . all ( O0oOOo0Oo , oO0i1iI , Oo0oO0ooo )
   OOooOO000 ( )
   if 83 - 83: O0 + I1IiI / O0 / oOo00oOO0O
def OOooOO000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 68 - 68: i1IIi . oOo00oOO0O . i1IIi + I1IIiI1 % OOOo0
 if 32 - 32: I1IiI . iIii1I11I1II1 % ii . O0 . I1IiI / oOOoo0Oo
def iI1 ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , O000OOO , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , iiIiii1IIIII , 1007 , O000OOO )
def O000OOOo ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for url , O000OOO , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 1006 , O000OOO )
  if 82 - 82: oOo00oOO0O / I1IiI - Ii11I / oO0
  if 50 - 50: Ii11I + Ooo00oOo00o . i11iIiiIii + ii11ii1ii + i11iIiiIii
def IIi11I1i1I1I ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for url , i1I1i111Ii , Ii1IIiI1i , ooo , i1iIIIi1i in Iiii :
  if '.php' in url :
   I1i1IiI1i ( i1iIIIi1i , url , 1016 , i1I1i111Ii , ooo , Ii1IIiI1i )
  else :
   if 'youtube' in url :
    I1i111IiIiIi1 ( i1iIIIi1i , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1I1i111Ii , ooo , Ii1IIiI1i )
   else :
    I1i111IiIiIi1 ( i1iIIIi1i , url , 222 , i1I1i111Ii , ooo , Ii1IIiI1i )
    OOO ( 'movies' , 'INFO' )
    if 35 - 35: O0 + Oo - OOOo0 % oO0O0ooO0Oo % OoOoOO00
 else :
  Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
  for url , O000OOO , i1iIIIi1i in Iiii :
   if '.php' in url :
    ii1IIIIiI11 ( i1iIIIi1i , url , 1016 , O000OOO )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     O0Oo00oO0O00 ( i1iIIIi1i , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O000OOO )
    else :
     O0Oo00oO0O00 ( i1iIIIi1i , url , 222 , O000OOO )
     OOO ( 'movies' , 'INFO' )
     if 77 - 77: O00Oo000ooO0 + ii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 38 - 38: ii11ii1ii - oO0O0ooO0Oo * OOooOOo
def iIIIi1iii1I11 ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , O000OOO , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , iiIiii1IIIII , 1007 , O000OOO )
def O0o0 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for url , O000OOO , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 1006 , O000OOO )
  if 76 - 76: ii . oOOoo0Oo . O0
def O0o0O0OooOoo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 IiII1i11III = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 IiII1i11III . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiII1i11III )
 if 8 - 8: O00Oo000ooO0 % ii
 if 50 - 50: I1IiI - ii + iIii1I11I1II1 - Ooo00oOo00o . Oo
def iiiiIii11i1 ( url ) :
 i111iIi1i1II1 = oooO ( url )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111iIi1i1II1 )
 for url , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( '[COLORgreen]' + i1iIIIi1i + '[/COLOR]' , url , 1006 , oOO0O00oO0Ooo )
def IiI11IIi1iI1i ( url ) :
 i111iIi1i1II1 = oooO ( url )
 o0OO = url
 Iiii = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  if '.mp3' in i1iIIIi1i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   ii1IIIIiI11 ( ( i1iIIIi1i ) . replace ( '/' , '' ) , o0OO + url , 1011 , ii11iIi1I + 'music.png' )
def iI1iI ( ) :
 i111iIi1i1II1 = oooO ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Iiii = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , oOO0O00oO0Ooo , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , ( 'http://www.cyn.net/music/' + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOO0O00oO0Ooo ) . replace ( ' ' , '%20' ) )
def O0oo0000o ( url , img ) :
 i111iIi1i1II1 = oooO ( url )
 O00O0Oooo0oO = url
 img = img
 Iiii = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( ( i1iIIIi1i ) . replace ( '.mp3' , '' ) , ( O00O0Oooo0oO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 99 - 99: ii - ii11ii1ii . OoOoOO00 * i11iIiiIii . Ii11I - Ooo00oOo00o
  if 31 - 31: i11iIiiIii * oO0O0ooO0Oo . OOooOOo % Ii11I * ii11ii1ii % O0
def OOoO00O ( ) :
 IIIi = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Ii11i1i = I1I1I . lower ( )
 iiIiii1IIIII = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 O00O0Oooo0oO = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oOO0O00Oo0O0o = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 20 - 20: i1IIi . i1IIi - oOo00oOO0O
 IIi1iiIi1 = ii11Iiii ( iiIiii1IIIII )
 iIIii = ii11Iiii ( O00O0Oooo0oO )
 iiI1ii111 = ii11Iiii ( oOO0O00Oo0O0o )
 if 89 - 89: oO0 - oOo00oOO0O . O0 % OoooooooOO . i11iIiiIii
 if IIi1iiIi1 != 'Failed' :
  Iiii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1iiIi1 )
  for i1iIIIi1i in Iiii :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( i1iIIIi1i + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiIiii1IIIII + i1iIIIi1i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 35 - 35: OoOoOO00 / I1IiI - O0 . OoOoOO00
    OOO ( 'tvshows' , 'Media Info 3' )
 if iIIii != 'Failed' :
  o00O0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1iiIi1 )
  for i1iIIIi1i in o00O0O :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( i1iIIIi1i + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00O0Oooo0oO + i1iIIIi1i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 55 - 55: Oo % i1IIi * oOo00oOO0O
    OOO ( 'tvshows' , 'Media Info 3' )
 if iiI1ii111 != 'Failed' :
  II1i11i1iIi11 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iiI1ii111 )
  for i1iIIIi1i in II1i11i1iIi11 :
   if I1I1I in i1iIIIi1i . lower ( ) :
    ii1IIIIiI11 ( ( i1iIIIi1i + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOO0O00Oo0O0o + i1iIIIi1i ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 95 - 95: Ii11I / OoOoOO00 - OOooOOo % O00Oo000ooO0 . oOo00oOO0O
    OOO ( 'tvshows' , 'Media Info 3' )
    if 63 - 63: iIii1I11I1II1 / oO0
    if 24 - 24: Oo / iIii1I11I1II1 % Ii11I * I1IiI - iIii1I11I1II1
    if 50 - 50: OoOoOO00
    if 39 - 39: OoOoOO00 . I1IiI - Oo * i1IIi . OoooooooOO
    if 44 - 44: OOOo0
    if 55 - 55: ii . O00Oo000ooO0 * O00Oo000ooO0
def OO0OO00ooO0 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( 'http://www.iwatchseries.me/tv-list/' )
 Iiii = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , iiIiii1IIIII , 8021 , ii11iIi1I + 'iwatch.png' )
def OOOOOoO00oo00 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i , IiIi in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i + IiIi , url , 8022 , ii11iIi1I + 'iwatch.png' )
def iIIIII11 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  ooooOOO0 ( url )
def ooooOOO0 ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 o00O0O = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( i111iIi1i1II1 )
 II1i11i1iIi11 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( 'VidSpot - ' + i1iIIIi1i , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in o00O0O :
  O0Oo00oO0O00 ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for i1iIIIi1i , url in II1i11i1iIi11 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   O0Oo00oO0O00 ( 'TheVideo - ' + i1iIIIi1i , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 49 - 49: O0 / OoOoOO00 * OOOo0 - OoooooooOO . OoOoOO00 % I1IIiI1
def IIi ( ) :
 i111iIi1i1II1 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 Iiii = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , iiIiii1IIIII , 1021 , ii11iIi1I + 'anime.png' )
  if 12 - 12: Ii11I
  if 87 - 87: oOo00oOO0O . oOo00oOO0O . OoOoOO00 / Ii11I
def oOOoOOooO0 ( ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( 'http://www.animetoon.org/cartoon' )
 Iiii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( i111iIi1i1II1 )
 for iiIiii1IIIII , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , iiIiii1IIIII , 1002 , ii11iIi1I + 'anime.png' )
  if 42 - 42: iIii1I11I1II1 * oO0O0ooO0Oo / Ooo00oOo00o + Ii11I
  if 48 - 48: OoooooooOO - O00Oo000ooO0 . i11iIiiIii * oOOoo0Oo - oO0O0ooO0Oo - OOooOOo
  if 59 - 59: oOOoo0Oo / oOo00oOO0O . Oo
def o0III11IiI ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 o00O0O = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( i111iIi1i1II1 )
 for oOO0O00oO0Ooo in o00O0O :
  oOO = oOO0O00oO0Ooo
 II1i11i1iIi11 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( i111iIi1i1II1 )
 for url in II1i11i1iIi11 :
  ii1IIIIiI11 ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 Iiii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( i111iIi1i1II1 )
 for url , i1iIIIi1i in Iiii :
  ii1IIIIiI11 ( i1iIIIi1i , url , 1003 , oOO )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0ooo ( url , IMAGE ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i111iIi1i1II1 )
 for i1iIIIi1i , url in Iiii :
  print i1iIIIi1i + '     ' + url
  if 'easy' in url :
   o0oo00O ( url )
  elif 'playpanda' in url :
   o0oo00O ( url )
   if 36 - 36: Ii11I * Ooo00oOo00o - ii11ii1ii + oOOoo0Oo
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oo00O ( url ) :
 i111iIi1i1II1 = iii1i1iiiiIi ( url )
 Iiii = re . compile ( "url: '(.+?)'," ) . findall ( i111iIi1i1II1 )
 for url in Iiii :
  O0Oo00oO0O00 ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 13 - 13: Ooo00oOo00o % iIii1I11I1II1 - OoOoOO00 / OOOo0
  if 9 - 9: ii11ii1ii * oO0O0ooO0Oo - I1IIiI1
def ooOOoO ( url ) :
 II1OoooOo = urllib2 . Request ( url )
 II1OoooOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 II1OoooOo . add_header ( 'referer' , url )
 I1I1IIiiii1ii = urllib2 . urlopen ( II1OoooOo )
 OO0ooo0o0O0Oooooo = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 return OO0ooo0o0O0Oooooo
 if 70 - 70: I1IIiI1 . O00Oo000ooO0 * Ooo00oOo00o + oOo00oOO0O - I1IIiI1 . I1IIiI1
def oooO ( url ) :
 II1OoooOo = urllib2 . Request ( url )
 II1OoooOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1I1IIiiii1ii = urllib2 . urlopen ( II1OoooOo )
 OO0ooo0o0O0Oooooo = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 return OO0ooo0o0O0Oooooo
 if 60 - 60: i11iIiiIii * Oo % Ooo00oOo00o + Ooo00oOo00o
def ooo000o ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 II1Ii = ( '%s%s' % ( OOoO00ooO , url ) )
 OO0ooo0o0O0Oooooo = oooO ( url )
 Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0ooo0o0O0Oooooo )
 for url , O000OOO , i1iIIIi1i in Iiii :
  O0Oo00oO0O00 ( '%s' % ( i1iIIIi1i ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , O000OOO )
  if 90 - 90: ii + Ooo00oOo00o + ii11ii1ii - O00Oo000ooO0
def IIii11I1 ( url ) :
 II1iIi1IiIii = xbmc . Player ( i1iI1Iiii1I ( ) )
 import urlresolver
 try : II1iIi1IiIii . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( i1iIIIi1i ) )
 II1iIi1IiIii = xbmc . Player ( i1iI1Iiii1I ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : II1iIi1IiIii . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 10 - 10: ii11ii1ii + I1IIiI1
def Ooooo00 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % i1iIIIi1i )
 xbmc . sleep ( 1 )
 II1iIi1IiIii = xbmc . Player ( i1iI1Iiii1I ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % i1iIIIi1i )
 xbmc . sleep ( 1 )
 II1iIi1IiIii . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 99 - 99: ii11ii1ii - ii
def I11Ii ( url ) :
 II1iIi1IiIii = xbmc . Player ( i1iI1Iiii1I ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : II1iIi1IiIii . play ( url ) . strip ( )
 except : pass
 if 10 - 10: OoOoOO00 . Ooo00oOo00o
 if 89 - 89: oO0 * oO0O0ooO0Oo
def i1iI1Iiii1I ( ) :
 try :
  Oo0o0O0o0oo0O0O = getSet ( "core-player" )
  if ( Oo0o0O0o0oo0O0O == 'DVDPLAYER' ) : o00i111i = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( Oo0o0O0o0oo0O0O == 'MPLAYER' ) : o00i111i = xbmc . PLAYER_CORE_MPLAYER
  elif ( Oo0o0O0o0oo0O0O == 'PAPLAYER' ) : o00i111i = xbmc . PLAYER_CORE_PAPLAYER
  else : o00i111i = xbmc . PLAYER_CORE_AUTO
 except : o00i111i = xbmc . PLAYER_CORE_AUTO
 return o00i111i
 return True
 if 36 - 36: oO0O0ooO0Oo
def ii1IIIIiI11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooOO00o0 = [ ]
  if showcontext == 'fav' :
   ooOO00o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   ooOO00o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i . addContextMenuItems ( ooOO00o0 )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
 if 44 - 44: OOOo0 % Ii11I * i11iIiiIii * i11iIiiIii - Oo . O00Oo000ooO0
def OOo00O ( name , url , mode , iconimage , fanart , description ) :
 if 68 - 68: oOOoo0Oo . oOo00oOO0O
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
 if 29 - 29: oO0 * I1IIiI1
def O0Oo00oO0O00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooOO00o0 = [ ]
  if showcontext == 'fav' :
   ooOO00o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   ooOO00o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i . addContextMenuItems ( ooOO00o0 )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = False )
 return iiIIi
 if 75 - 75: O0
 if 56 - 56: Ooo00oOo00o / OoOoOO00
 if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
 if 49 - 49: Oo + O0 + I1IIiI1 . OoOoOO00 % oO0
 if 33 - 33: I1IiI . iIii1I11I1II1 / oOo00oOO0O % oO0O0ooO0Oo
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / I1IIiI1 - O0 % oO0O0ooO0Oo
def o00OO00OoO ( heading , announce ) :
 class iII1i1 ( ) :
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
   try : oOIIiIi = open ( announce ) ; IIIii = oOIIiIi . read ( )
   except : IIIii = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IIIii ) )
   return
 iII1i1 ( )
 iII1i1 ( )
 if 63 - 63: OOOo0 - i11iIiiIii - oOOoo0Oo % oOo00oOO0O . oO0O0ooO0Oo * ii11ii1ii
def OooO0o ( ) :
 o00OO00OoO ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 81 - 81: i1IIi / O00Oo000ooO0 % i11iIiiIii . iIii1I11I1II1 * I1IiI + OoooooooOO
 if 31 - 31: i1IIi % OoOoOO00
 if 13 - 13: iIii1I11I1II1 - OoOoOO00 % O0 . oO0O0ooO0Oo % Ooo00oOo00o
 if 2 - 2: OoooooooOO - oO0O0ooO0Oo % ii / OOOo0 / OOooOOo
 if 3 - 3: OoOoOO00 / Ii11I
def OOooOO000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 48 - 48: oO0 . ii11ii1ii
 if 49 - 49: i1IIi - I1IiI . Oo + iIii1I11I1II1 - oO0 / Oo
 if 24 - 24: ii - oOOoo0Oo / oO0
 if 10 - 10: I1IiI * i1IIi
 if 15 - 15: oOo00oOO0O + i1IIi - OoOoOO00 % OOOo0
 if 34 - 34: OOOo0
 if 57 - 57: Ii11I . oO0O0ooO0Oo % OOooOOo
 if 32 - 32: oOo00oOO0O / I1IIiI1 - O0 * iIii1I11I1II1
 if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
 if 98 - 98: Ooo00oOo00o
 if 18 - 18: oOo00oOO0O + Oo - Ooo00oOo00o / O00Oo000ooO0 / Ii11I
 if 53 - 53: Ii11I + OOooOOo . ii / oOo00oOO0O
 if 52 - 52: O00Oo000ooO0 + O00Oo000ooO0
 if 73 - 73: OOooOOo . i11iIiiIii % OoooooooOO + oO0 . OoooooooOO / Ii11I
 if 54 - 54: I1IiI . OoooooooOO
 if 36 - 36: ii / OoOoOO00 * I1IIiI1 % ii11ii1ii
 if 31 - 31: OoOoOO00 + Ii11I - OoooooooOO . oOo00oOO0O
 if 28 - 28: oO0O0ooO0Oo . ii11ii1ii
 if 77 - 77: ii11ii1ii % OoOoOO00
 if 81 - 81: I1IiI % oO0O0ooO0Oo / O0 * iIii1I11I1II1 % I1IIiI1 . OOOo0
 if 90 - 90: OOooOOo
 if 44 - 44: OOooOOo / ii11ii1ii . Oo + I1IiI
 if 32 - 32: I1IIiI1 - oO0 * oOOoo0Oo * oOo00oOO0O
 if 84 - 84: oO0O0ooO0Oo + ii11ii1ii % OOOo0 + i11iIiiIii
def i1iI11Ii1i ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + Iii1Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 48 - 48: Ii11I
def I1111III111ii ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + o0oO0oOooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 99 - 99: i11iIiiIii - oOOoo0Oo
def o0O0O0O00o ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + OoOooOo00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 28 - 28: ii11ii1ii + ii11ii1ii % I1IiI
def iiI111iIi1 ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + I1i1ii1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 32 - 32: I1IIiI1 / OoooooooOO
def IIIIIIi1IIi1I11i ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + O0o0oOooOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 59 - 59: ii11ii1ii + oOo00oOO0O . ii
def oOOo0oO ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + iIIII1iII1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 98 - 98: O00Oo000ooO0 % Ooo00oOo00o - oO0 % i11iIiiIii + O00Oo000ooO0 - I1IIiI1
def O00o ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + Ii11Iiii1iiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 10 - 10: oOOoo0Oo % Oo
def i111111 ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + o0oO0OOoO0OoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 37 - 37: ii % O00Oo000ooO0 % ii
def iIIIi1i1Ii ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + Oo0o00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 42 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 32 - 32: I1IiI + oO0 + oO0O0ooO0Oo + OOOo0
def I1IIIIII1 ( url ) :
 OO0ooo0o0O0Oooooo = iii1i1iiiiIi ( iiI1IiI + O0oO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OO0ooo0o0O0Oooooo )
 for i1iIIIi1i , url , i1I1i111Ii , ooo , Iii1I1111ii in Iiii :
  i1I1iI ( i1iIIIi1i , url , 5 , i1I1i111Ii , ooo , Iii1I1111ii )
 OOO ( 'movies' , 'MAIN' )
 if 20 - 20: I1IiI % OoOoOO00 . I1IiI . I1IIiI1 + Ii11I
 if 26 - 26: oOOoo0Oo / OoooooooOO - Oo
 if 2 - 2: ii11ii1ii - Oo
 if 4 - 4: O0 / oOo00oOO0O . Ooo00oOo00o - oO0 / Ii11I
 if 25 - 25: oOo00oOO0O * I1IiI - Oo . oO0 . ii
 if 89 - 89: O0 * oOo00oOO0O * Ooo00oOo00o
 if 3 - 3: Ii11I / oOOoo0Oo * iIii1I11I1II1 + OoOoOO00 / OOooOOo / I1IIiI1
 if 25 - 25: I1IiI + Ooo00oOo00o % oO0O0ooO0Oo % Ii11I / ii
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . oO0 - OOOo0
def iii11 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( oOOoO0 ) :
     OO0oO = 0
     OO0oO += len ( Ooo00OoOOO )
     if OO0oO > 0 :
      for oOIIiIi in Ooo00OoOOO :
       os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
  i1i11ii = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( i1i11ii )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 86 - 86: ii11ii1ii - i1IIi + Oo * OOOo0 / i11iIiiIii % ii
 if 17 - 17: oO0 + oO0 . ii11ii1ii
 if 50 - 50: iIii1I11I1II1 * ii
 if 85 - 85: i1IIi
 if 100 - 100: OoooooooOO / oOo00oOO0O % Ooo00oOo00o + oO0O0ooO0Oo
 if 42 - 42: Oo / I1IIiI1 . oO0O0ooO0Oo * OOOo0
 if 54 - 54: I1IiI * oOOoo0Oo + Ooo00oOo00o
 if 93 - 93: OOooOOo / OOOo0
 if 47 - 47: Oo * Ii11I
def oOoO0O00o ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 IiI11II = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( IiI11II ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( IiI11II ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 87 - 87: Oo . OoooooooOO * O00Oo000ooO0 * OoOoOO00 / i1IIi * I1IiI
   if 25 - 25: oO0O0ooO0Oo * OOooOOo * ii . OOOo0
   if OO0oO > 0 :
    if 93 - 93: I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 97 - 97: i11iIiiIii
     for oOIIiIi in Ooo00OoOOO :
      try :
       os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
      except :
       pass
     for IIII1iII in iII111Ii :
      try :
       shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      except :
       pass
       if 68 - 68: I1IIiI1 * Ooo00oOo00o . oOo00oOO0O / oO0O0ooO0Oo . OOooOOo - i11iIiiIii
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  II11IOOooo00oo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 42 - 42: oO0O0ooO0Oo * O0 / ii
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( II11IOOooo00oo ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 8 - 8: i1IIi + OoOoOO00 / oO0O0ooO0Oo + ii11ii1ii % oO0O0ooO0Oo - iIii1I11I1II1
   if OO0oO > 0 :
    if 29 - 29: Oo + OoOoOO00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OO0oO ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 95 - 95: ii
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 48 - 48: oOo00oOO0O / iIii1I11I1II1 % OoOoOO00
   else :
    pass
  IiI111I = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 62 - 62: OoooooooOO + I1IIiI1
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( IiI111I ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 32 - 32: I1IiI * OOooOOo / OoooooooOO
   if OO0oO > 0 :
    if 90 - 90: O00Oo000ooO0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OO0oO ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 35 - 35: OoOoOO00 / oO0O0ooO0Oo
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 79 - 79: I1IiI + O00Oo000ooO0 * oOOoo0Oo * oO0O0ooO0Oo
   else :
    pass
    if 53 - 53: Ii11I / Oo
    if 10 - 10: ii11ii1ii . OOooOOo
    if 75 - 75: O0 * i1IIi - oOo00oOO0O / Ii11I % Ii11I / I1IiI
    if 5 - 5: O0 - oOOoo0Oo / O00Oo000ooO0 . OOooOOo
 iIII1iIii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( iIII1iIii ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( iIII1iIii ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 9 - 9: i1IIi - I1IiI
   if 57 - 57: iIii1I11I1II1 * oO0O0ooO0Oo * oOOoo0Oo / ii
   if OO0oO > 0 :
    if 46 - 46: oO0O0ooO0Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 61 - 61: OOooOOo / oO0 - OoOoOO00
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 87 - 87: ii11ii1ii / OOOo0
   else :
    pass
    if 45 - 45: I1IiI * oO0 / OoooooooOO + Ooo00oOo00o . O00Oo000ooO0 / Ooo00oOo00o
    if 64 - 64: oO0O0ooO0Oo / i1IIi % OOOo0 - OOooOOo
 iIii111Ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( iIii111Ii ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( iIii111Ii ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 96 - 96: oO0O0ooO0Oo - OoOoOO00 % I1IiI * OOOo0 * OOOo0 . Oo
   if 75 - 75: Oo + oO0O0ooO0Oo + Ooo00oOo00o
   if OO0oO > 0 :
    if 97 - 97: oO0 % i11iIiiIii % oOo00oOO0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: Oo / oO0O0ooO0Oo / ii11ii1ii / i1IIi / OOooOOo
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 86 - 86: i1IIi
   else :
    pass
    if 33 - 33: I1IiI % i11iIiiIii * Ii11I
    if 69 - 69: OoOoOO00 + Oo - ii . Oo / iIii1I11I1II1 * iIii1I11I1II1
 oOooooooO0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( oOooooooO0o ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( oOooooooO0o ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 54 - 54: oO0O0ooO0Oo . O0
   if 79 - 79: I1IIiI1 / Ooo00oOo00o * OoooooooOO * I1IiI + OOOo0
   if OO0oO > 0 :
    if 68 - 68: oOo00oOO0O / iIii1I11I1II1 . Oo + i11iIiiIii + OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 92 - 92: Ooo00oOo00o . OOooOOo . oO0O0ooO0Oo % I1IiI
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 58 - 58: ii11ii1ii % oO0O0ooO0Oo * oO0O0ooO0Oo - oOOoo0Oo
   else :
    pass
    if 9 - 9: oO0 - oO0O0ooO0Oo % OoOoOO00 + I1IIiI1 + Ii11I % O0
    if 65 - 65: Ii11I - Ooo00oOo00o % i11iIiiIii
    if 58 - 58: oOOoo0Oo
 iii1iII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( iii1iII ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( iii1iII ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 77 - 77: I1IIiI1 + OoooooooOO * i1IIi % OoooooooOO
   if 3 - 3: oO0O0ooO0Oo * oO0 - OOOo0 / i1IIi
   if OO0oO > 0 :
    if 21 - 21: OoOoOO00 + O00Oo000ooO0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 22 - 22: I1IIiI1 . oOOoo0Oo + Oo
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 45 - 45: Oo % Oo + Oo / O0 % OoooooooOO
   else :
    pass
    if 92 - 92: oO0O0ooO0Oo . I1IiI . oOo00oOO0O - OoooooooOO / oO0
    if 80 - 80: iIii1I11I1II1 / i11iIiiIii + oOOoo0Oo
 I11I1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( I11I1i ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( I11I1i ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 100 - 100: ii
   if 39 - 39: OoOoOO00 * OOOo0 - iIii1I11I1II1
   if OO0oO > 0 :
    if 25 - 25: OoooooooOO . oO0O0ooO0Oo % oOOoo0Oo . I1IIiI1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 67 - 67: OoooooooOO + O00Oo000ooO0 / oO0
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 75 - 75: I1IIiI1 / OoooooooOO . OOOo0 + O00Oo000ooO0 - OoOoOO00
   else :
    pass
    if 33 - 33: I1IIiI1 / I1IIiI1 . i11iIiiIii * ii11ii1ii + OOooOOo
    if 16 - 16: I1IIiI1
 II1OOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( I11I1i ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( II1OOO ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 32 - 32: iIii1I11I1II1 * Oo - ii
   if 72 - 72: I1IIiI1 % i1IIi / iIii1I11I1II1
   if OO0oO > 0 :
    if 95 - 95: O0 . Ooo00oOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: i1IIi
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 19 - 19: oO0 / OOooOOo % I1IIiI1 - oO0O0ooO0Oo
   else :
    pass
    if 14 - 14: ii11ii1ii - i11iIiiIii * O00Oo000ooO0
    if 39 - 39: OoooooooOO
 i1iIII1IIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( I11I1i ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( i1iIII1IIi ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 63 - 63: OoOoOO00 . O00Oo000ooO0 % I1IIiI1 + OoOoOO00
   if 81 - 81: Ii11I - OOOo0 % OOooOOo
   if OO0oO > 0 :
    if 7 - 7: oO0 - i1IIi . I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 12 - 12: I1IIiI1 / Ooo00oOo00o / O0 * I1IIiI1
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 51 - 51: oO0 * oOOoo0Oo / i1IIi
   else :
    pass
    if 2 - 2: ii + I1IIiI1 . oOOoo0Oo - i1IIi + O00Oo000ooO0
    if 54 - 54: OoooooooOO . ii - oOOoo0Oo
 oO0o00o000Oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( I11I1i ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( oO0o00o000Oo0 ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 1 - 1: OOOo0 - O00Oo000ooO0
   if 62 - 62: Ooo00oOo00o . oOOoo0Oo . oOOoo0Oo % i1IIi * ii % Oo
   if OO0oO > 0 :
    if 20 - 20: oO0 . I1IIiI1 / oOo00oOO0O . OoooooooOO * Ii11I + oO0O0ooO0Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 2 - 2: OOOo0
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 11 - 11: Ii11I + iIii1I11I1II1 / I1IiI % O0
   else :
    pass
    if 98 - 98: OoOoOO00 + Oo * iIii1I11I1II1 * ii11ii1ii + Ii11I * oO0O0ooO0Oo
    if 76 - 76: oO0 . ii
 oO00OO0o0ooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( I11I1i ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( oO00OO0o0ooO ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 42 - 42: O0 * oOOoo0Oo . I1IiI / Ii11I - oO0O0ooO0Oo . oOo00oOO0O
   if 57 - 57: OOooOOo + Oo * ii11ii1ii - oO0 % iIii1I11I1II1 - oO0O0ooO0Oo
   if OO0oO > 0 :
    if 37 - 37: Ooo00oOo00o * oOo00oOO0O + oO0O0ooO0Oo + ii11ii1ii * OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: oO0O0ooO0Oo - i11iIiiIii % i11iIiiIii - O0 * O00Oo000ooO0
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
   else :
    pass
    if 100 - 100: i1IIi % oO0O0ooO0Oo
    if 55 - 55: OOOo0 + oOOoo0Oo
 OO00o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( I11I1i ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( OO00o0 ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 11 - 11: OOOo0 - OoooooooOO + OoOoOO00 + Oo % oOOoo0Oo
   if 90 - 90: OOOo0 * ii11ii1ii . oOo00oOO0O * oO0O0ooO0Oo - OOooOOo
   if OO0oO > 0 :
    if 40 - 40: O0 / I1IIiI1 - OoOoOO00 + OOooOOo % Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: oO0
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 82 - 82: ii11ii1ii / oO0 . i11iIiiIii + Ii11I - I1IiI / oOOoo0Oo
   else :
    pass
    if 99 - 99: ii / i1IIi
    if 2 - 2: ii . oOOoo0Oo
 II1II111 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( I11I1i ) == True :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( II1II111 ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 71 - 71: OoOoOO00 % O00Oo000ooO0 + OOOo0 * oO0 + I1IIiI1 . oO0
   if 25 - 25: oO0 . OOooOOo % OOOo0 + oOOoo0Oo
   if OO0oO > 0 :
    if 61 - 61: ii % oO0 - ii11ii1ii + ii . I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 44 - 44: ii11ii1ii / O0 - I1IIiI1 + Ii11I . oOo00oOO0O . ii11ii1ii
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
      if 95 - 95: I1IiI % O00Oo000ooO0 % i1IIi * OOooOOo + Ii11I
   else :
    pass
    if 34 - 34: O00Oo000ooO0 * OOooOOo . OOOo0 % i11iIiiIii
    if 61 - 61: iIii1I11I1II1 + ii * oOo00oOO0O - i1IIi % ii
    if 76 - 76: ii / I1IiI
 iI1II1iIiI11I = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   i1IIOO = os . path . join ( iI1II1iIiI11I , "cache.db" )
   os . unlink ( i1IIOO )
   if 99 - 99: Oo
 except :
  pass
  if 17 - 17: i11iIiiIii - i11iIiiIii + ii11ii1ii * oO0 * ii / OoooooooOO
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 22 - 22: O00Oo000ooO0 * ii11ii1ii - I1IIiI1
 if 71 - 71: iIii1I11I1II1 / i11iIiiIii % OOooOOo . O00Oo000ooO0 * OOOo0 % OoOoOO00
 if 35 - 35: O00Oo000ooO0 - I1IiI
 if 61 - 61: O00Oo000ooO0 * OOooOOo * Ooo00oOo00o + ii11ii1ii . Oo + i1IIi
 if 82 - 82: Oo + O00Oo000ooO0
 if 93 - 93: oOo00oOO0O * O0 * Ii11I - OOooOOo / ii11ii1ii
 if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
 if 95 - 95: O0 + iIii1I11I1II1 . ii11ii1ii
 if 61 - 61: oO0O0ooO0Oo * oO0O0ooO0Oo
def O0III1Iiii1i11 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 OO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( OO00 ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 10 - 10: oOo00oOO0O * i1IIi . ii / O00Oo000ooO0 . Ii11I / O00Oo000ooO0
   if 1 - 1: oOOoo0Oo % oO0
   if OO0oO > 0 :
    if 99 - 99: oOOoo0Oo + iIii1I11I1II1 . Ii11I / Ooo00oOo00o * ii11ii1ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: I1IIiI1 / OoOoOO00 % Ooo00oOo00o % Ooo00oOo00o
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 28 - 28: I1IiI % ii - Ii11I + Ii11I + ii / iIii1I11I1II1
 if 91 - 91: OOOo0 / OoOoOO00 * Ii11I
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % oO0O0ooO0Oo
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
 if 60 - 60: O00Oo000ooO0
 if 77 - 77: OOOo0 / ii11ii1ii
 if 95 - 95: O00Oo000ooO0 * i1IIi + ii
 if 40 - 40: OoOoOO00
def iII1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 OO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( OO00 ) :
   OO0oO = 0
   OO0oO += len ( Ooo00OoOOO )
   if 7 - 7: ii11ii1ii - iIii1I11I1II1
   if 97 - 97: Ii11I
   if OO0oO > 0 :
    if 41 - 41: OoooooooOO - Oo * iIii1I11I1II1 . i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OO0oO ) + " files found" , "Do you want to delete them?" ) :
     if 39 - 39: oO0O0ooO0Oo % i1IIi . ii11ii1ii - O0
     for oOIIiIi in Ooo00OoOOO :
      os . unlink ( os . path . join ( i1I1I1iiII , oOIIiIi ) )
     for IIII1iII in iII111Ii :
      shutil . rmtree ( os . path . join ( i1I1I1iiII , IIII1iII ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 oOoO0O00o ( url )
 if 65 - 65: ii * ii / oOo00oOO0O + ii % oO0 + I1IiI
 if 92 - 92: OOooOOo
 if 37 - 37: ii
 if 18 - 18: I1IIiI1 * i11iIiiIii + iIii1I11I1II1 % oOo00oOO0O + i1IIi - Ooo00oOo00o
 if 85 - 85: Ooo00oOo00o * oOo00oOO0O + Ooo00oOo00o
 if 39 - 39: Oo / i1IIi % i1IIi
 if 20 - 20: Ii11I * ii
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . Ii11I
 if 31 - 31: ii % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
def I1i1Ii ( url , name ) :
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 III1 = os . path . join ( ooo00Ooo , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 I1I11 = os . path . join ( ooo00Ooo , 'advancedsettings.xml.bak' )
 if os . path . exists ( I1I11 ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   III1 = os . path . join ( ooo00Ooo , 'advancedsettings.xml' )
   try :
    os . remove ( III1 )
    print '=== GenieTv - REMOVING    ' + str ( III1 ) + '    ==='
   except :
    pass
   OO0ooo0o0O0Oooooo = i1 . http_GET ( url ) . content
   OOoOooOoOOOoo = open ( III1 , "w" )
   OOoOooOoOOOoo . write ( OO0ooo0o0O0Oooooo )
   OOoOooOoOOOoo . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( III1 ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  III1 = os . path . join ( ooo00Ooo , 'advancedsettings.xml' )
  try :
   os . remove ( III1 )
   print '=== GenieTv - REMOVING    ' + str ( III1 ) + '    ==='
  except :
   pass
  OO0ooo0o0O0Oooooo = i1 . http_GET ( url ) . content
  OOoOooOoOOOoo = open ( III1 , "w" )
  OOoOooOoOOOoo . write ( OO0ooo0o0O0Oooooo )
  OOoOooOoOOOoo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( III1 ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 68 - 68: i11iIiiIii . O0 * OOOo0 * i1IIi * OoooooooOO
def I1I1I1 ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 III1 = os . path . join ( ooo00Ooo , 'advancedsettings.xml' )
 try :
  OOoOooOoOOOoo = open ( III1 ) . read ( )
  if 'zero' in OOoOooOoOOOoo :
   name = '0CACHE'
  elif 'tuxen' in OOoOooOoOOOoo :
   name = 'TUXENS'
  elif 'muckys' in OOoOooOoOOOoo :
   name = 'MUCKYS'
  elif 'p2p1' in OOoOooOoOOOoo :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OOoOooOoOOOoo :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OOoOooOoOOOoo :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 29 - 29: ii11ii1ii
def oOOoOO ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 III1 = os . path . join ( ooo00Ooo , 'advancedsettings.xml' )
 try :
  os . remove ( III1 )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( III1 ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 99 - 99: oO0 * iIii1I11I1II1 - oO0O0ooO0Oo + Oo . Oo
 if 18 - 18: Ii11I
 if 82 - 82: OoooooooOO - oO0 * ii11ii1ii * oO0 * O0 * iIii1I11I1II1
 if 31 - 31: oO0 . Ii11I % oO0
 if 33 - 33: O0 * oO0O0ooO0Oo - I1IIiI1 . OoooooooOO + I1IIiI1
 if 20 - 20: O00Oo000ooO0 - I1IiI
 if 91 - 91: i1IIi
 if 31 - 31: i11iIiiIii + oO0O0ooO0Oo % I1IiI
 if 9 - 9: oO0 . oOo00oOO0O - Oo . O00Oo000ooO0
 if 39 - 39: Ii11I
def o00OO00OOo0 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Iiii = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for ooOo00ooO , I1ii11IiI1I , Oo0Ii , oooooOOo0Oo in Iiii :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ooOo00ooO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % Oo0Ii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % oooooOOo0Oo )
  inc = inc + 1
  if 29 - 29: O0 * i11iIiiIii / OoooooooOO / OOooOOo . oO0
  if 70 - 70: OoooooooOO . oO0 / ii . ii - OOooOOo
  if 29 - 29: oOo00oOO0O % Ii11I - oO0
  if 26 - 26: O0 . oOo00oOO0O + oOOoo0Oo - oO0O0ooO0Oo . oOo00oOO0O
  if 2 - 2: ii11ii1ii . Oo * Ii11I % OoOoOO00 . oOOoo0Oo
  if 46 - 46: I1IiI + OOOo0 % OoooooooOO * i11iIiiIii - Oo
  if 47 - 47: oOOoo0Oo * I1IiI * I1IIiI1
  if 46 - 46: oO0O0ooO0Oo
  if 42 - 42: iIii1I11I1II1
def IIi1IiIii ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  III1 = os . path . join ( ooo00Ooo , 'addons2.ini' )
  OO0ooo0o0O0Oooooo = i1 . http_GET ( url ) . content
  OOoOooOoOOOoo = open ( III1 , "w" )
  OOoOooOoOOOoo . write ( OO0ooo0o0O0Oooooo )
  OOoOooOoOOOoo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( III1 ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 40 - 40: OOOo0
def i1IiI ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  ooo00Ooo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  III1 = os . path . join ( ooo00Ooo , 'settings.xml' )
  OO0ooo0o0O0Oooooo = i1 . http_GET ( url ) . content
  OOoOooOoOOOoo = open ( III1 , "w" )
  OOoOooOoOOOoo . write ( OO0ooo0o0O0Oooooo )
  OOoOooOoOOOoo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( III1 ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 73 - 73: OoooooooOO * O0 * oO0
 if 7 - 7: OoOoOO00 + i1IIi
def OoooO0 ( ) :
 try :
  ii1O0oOOo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( ii1O0oOOo ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    ii111IIiiiiI = os . path . join ( ii1O0oOOo , "source.db" )
    os . unlink ( ii111IIiiiiI )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 98 - 98: i1IIi - oOOoo0Oo
 if 49 - 49: OOooOOo . oO0O0ooO0Oo . ii
 if 9 - 9: I1IIiI1 - OoOoOO00 * Ooo00oOo00o
 if 78 - 78: iIii1I11I1II1 / O0 * ii / oOOoo0Oo / I1IiI
 if 15 - 15: oO0 / ii
def iii1i1iiiiIi ( url ) :
 II1OoooOo = urllib2 . Request ( url )
 II1OoooOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1I1IIiiii1ii = urllib2 . urlopen ( II1OoooOo )
 OO0ooo0o0O0Oooooo = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 return OO0ooo0o0O0Oooooo
 if 54 - 54: oO0 - iIii1I11I1II1 - oOo00oOO0O % oO0O0ooO0Oo / OoOoOO00
 if 80 - 80: i11iIiiIii % iIii1I11I1II1 / i11iIiiIii
 if 66 - 66: I1IiI . iIii1I11I1II1 * ii11ii1ii - oO0O0ooO0Oo - iIii1I11I1II1
 if 28 - 28: I1IiI % OoooooooOO
 if 13 - 13: I1IIiI1 . Oo - oOo00oOO0O / ii - Oo - OOOo0
 if 84 - 84: OoOoOO00
 if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
def O00O ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; IIIIIi1 = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if IIIIIi1 :
  o0oIi1iiiii = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; o0oIi1iiiii = xbmc . translatePath ( o0oIi1iiiii ) ;
  O00o0 = os . path . join ( o0oIi1iiiii , ".." , ".." ) ; O00o0 = os . path . abspath ( O00o0 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + O00o0 ) ; IIiIiIi1II = False
  try :
   for i1I1I1iiII , iII111Ii , Ooo00OoOOO in os . walk ( O00o0 , topdown = True ) :
    iII111Ii [ : ] = [ IIII1iII for IIII1iII in iII111Ii if IIII1iII not in iiIIIII1i1iI ]
    for i1iIIIi1i in Ooo00OoOOO :
     try : os . remove ( os . path . join ( i1I1I1iiII , i1iIIIi1i ) )
     except :
      if i1iIIIi1i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIiIiIi1II = True
      plugintools . log ( "Error removing " + i1I1I1iiII + " " + i1iIIIi1i )
    for i1iIIIi1i in iII111Ii :
     try : os . rmdir ( os . path . join ( i1I1I1iiII , i1iIIIi1i ) )
     except :
      if i1iIIIi1i not in [ "Database" , "userdata" ] : IIiIiIi1II = True
      plugintools . log ( "Error removing " + i1I1I1iiII + " " + i1iIIIi1i )
   if not IIiIiIi1II : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 ooOO00oOOo000 ( )
 if 90 - 90: i1IIi
 if 54 - 54: OoOoOO00 % OOooOOo - i1IIi . OOOo0 - OoOoOO00 / iIii1I11I1II1
 if 29 - 29: ii
def Ooo000 ( ) :
 I1111IiII1 = [ ]
 IiiII = sys . argv [ 2 ]
 if len ( IiiII ) >= 2 :
  OO00OO0 = sys . argv [ 2 ]
  Ooii = OO00OO0 . replace ( '?' , '' )
  if ( OO00OO0 [ len ( OO00OO0 ) - 1 ] == '/' ) :
   OO00OO0 = OO00OO0 [ 0 : len ( OO00OO0 ) - 2 ]
  i11iII1 = Ooii . split ( '&' )
  I1111IiII1 = { }
  for iiiiIiI1i1I1 in range ( len ( i11iII1 ) ) :
   oOooo = { }
   oOooo = i11iII1 [ iiiiIiI1i1I1 ] . split ( '=' )
   if ( len ( oOooo ) ) == 2 :
    I1111IiII1 [ oOooo [ 0 ] ] = oOooo [ 1 ]
    if 15 - 15: oO0 * iIii1I11I1II1 * ii
 return I1111IiII1
 if 96 - 96: O00Oo000ooO0 * iIii1I11I1II1 / I1IiI % Ii11I * OoOoOO00
iII11I1Ii1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
Oo00oo0000OO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
o0o0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I1iiIIii = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i11IIIiI1I = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
O000oo00o000o = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
Iii1Iii = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
O0000ooO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
o0oO0oOooO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OoOooOo00o = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1i1ii1ii = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
O0o0oOooOoo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iIIII1iII1i = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
Ii11Iiii1iiii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o0oO0OOoO0OoO0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
Oo0o00o = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o00oIi1IIiiIIi = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
O00OoO = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i1i1i1I = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
iIiiiii1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OOOO00OO0O0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oO0o00oOOooO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
O0oO0O = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOoO00ooO = base64 . decodestring ( 'Q1VOVA==' )
def i1I1iI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOO00o0 = [ ]
  if showcontext == 'fav' :
   ooOO00o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   ooOO00o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1i . addContextMenuItems ( ooOO00o0 )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
 if 41 - 41: oO0 + iIii1I11I1II1 % I1IIiI1 % Ii11I
def oo0OooOOo0 ( name , url , mode , iconimage , fanart , description ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = False )
 return iiIIi
 if 41 - 41: OoOoOO00 . O00Oo000ooO0 . I1IiI - Ii11I - OOOo0 * O00Oo000ooO0
 if 99 - 99: OOOo0
OO00OO0 = Ooo000 ( )
iiIiii1IIIII = None
i1iIIIi1i = None
oOo0OOoooO = None
i1I1i111Ii = None
ooo = None
Iii1I1111ii = None
OO000O000OOO = None
if 26 - 26: oOo00oOO0O * oO0O0ooO0Oo % OOOo0 + oOOoo0Oo
if 38 - 38: oOOoo0Oo - Oo / oO0O0ooO0Oo + ii . oOOoo0Oo + I1IIiI1
try :
 OO000O000OOO = int ( OO00OO0 [ "fav_mode" ] )
except :
 pass
 if 19 - 19: oO0O0ooO0Oo
try :
 iiIiii1IIIII = urllib . unquote_plus ( OO00OO0 [ "url" ] )
except :
 pass
try :
 i1iIIIi1i = urllib . unquote_plus ( OO00OO0 [ "name" ] )
except :
 pass
try :
 i1I1i111Ii = urllib . unquote_plus ( OO00OO0 [ "iconimage" ] )
except :
 pass
try :
 oOo0OOoooO = int ( OO00OO0 [ "mode" ] )
except :
 pass
try :
 ooo = urllib . unquote_plus ( OO00OO0 [ "fanart" ] )
except :
 pass
try :
 Iii1I1111ii = urllib . unquote_plus ( OO00OO0 [ "description" ] )
except :
 pass
 if 51 - 51: iIii1I11I1II1
 if 8 - 8: Ooo00oOo00o / OOooOOo % oOOoo0Oo . i11iIiiIii . OoooooooOO . oO0O0ooO0Oo
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( oOo0OOoooO )
print "URL: " + str ( iiIiii1IIIII )
print "Name: " + str ( i1iIIIi1i )
print "IconImage: " + str ( i1I1i111Ii )
if 8 - 8: Ooo00oOo00o * Oo
if 41 - 41: Oo / Ooo00oOo00o / I1IiI - i11iIiiIii - I1IiI
def OOO ( content , viewType ) :
 if 4 - 4: oOo00oOO0O . I1IIiI1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 39 - 39: Ii11I . Oo - I1IiI * i11iIiiIii
  if 4 - 4: I1IiI * O0 - oOo00oOO0O
if oOo0OOoooO == None :
 OOO0OOO00oo ( )
 if 72 - 72: oOo00oOO0O + oO0 / OOOo0 . I1IIiI1 % Ooo00oOo00o / i11iIiiIii
elif oOo0OOoooO == 1 :
 oOo0OoOOo0 ( iiIiii1IIIII )
 if 13 - 13: O00Oo000ooO0 % OOooOOo + Ii11I + O00Oo000ooO0 + i11iIiiIii - ii11ii1ii
elif oOo0OOoooO == 44 :
 O0iIi1IiII ( iiIiii1IIIII )
 if 70 - 70: OoOoOO00 * OoOoOO00 . OOOo0
elif oOo0OOoooO == 2 :
 I1I1iIi11i1II ( )
 if 11 - 11: oOOoo0Oo
elif oOo0OOoooO == 3 :
 O0iII1 ( )
 if 20 - 20: oO0O0ooO0Oo . O00Oo000ooO0 % oO0O0ooO0Oo
elif oOo0OOoooO == 21 :
 iI1Ii11111iIi ( )
 if 5 - 5: Ii11I + oOOoo0Oo
elif oOo0OOoooO == 4 :
 ii1 ( )
 if 23 - 23: O00Oo000ooO0 % iIii1I11I1II1 . oOo00oOO0O
elif oOo0OOoooO == 5 :
 ooO0oO00O0o ( i1iIIIi1i , iiIiii1IIIII , Iii1I1111ii )
 if 95 - 95: Oo + i11iIiiIii % Ii11I - ii
elif oOo0OOoooO == 6 :
 O0III1Iiii1i11 ( iiIiii1IIIII )
 if 11 - 11: ii11ii1ii / O0 + OoOoOO00
elif oOo0OOoooO == 7 :
 I1i1Ii ( iiIiii1IIIII , i1iIIIi1i )
 if 95 - 95: O00Oo000ooO0 + I1IIiI1 * iIii1I11I1II1
elif oOo0OOoooO == 8 :
 I1I1I1 ( iiIiii1IIIII , i1iIIIi1i )
 if 17 - 17: Ooo00oOo00o - Oo * O0 / oO0O0ooO0Oo
elif oOo0OOoooO == 9 :
 FIXREPOSADDONS ( iiIiii1IIIII )
 if 19 - 19: i1IIi - iIii1I11I1II1 . oOo00oOO0O
elif oOo0OOoooO == 10 :
 OOooOO000 ( )
 if 2 - 2: oO0O0ooO0Oo
elif oOo0OOoooO == 11 :
 oOOoOO ( iiIiii1IIIII )
 if 12 - 12: i11iIiiIii - iIii1I11I1II1 * I1IIiI1 * oOOoo0Oo
elif oOo0OOoooO == 12 :
 o00OO00OOo0 ( )
 if 19 - 19: O0 + ii + OOooOOo
elif oOo0OOoooO == 13 :
 iii11 ( )
 if 81 - 81: iIii1I11I1II1
elif oOo0OOoooO == 14 :
 oOoO0O00o ( iiIiii1IIIII )
 if 51 - 51: OOooOOo . ii11ii1ii * oO0O0ooO0Oo / Oo * OoOoOO00 / O0
elif oOo0OOoooO == 15 :
 II11iI111i1 ( )
 if 44 - 44: i11iIiiIii % O00Oo000ooO0 % ii + oOo00oOO0O * ii . oO0O0ooO0Oo
elif oOo0OOoooO == 16 :
 IIi1IiIii ( iiIiii1IIIII , i1iIIIi1i )
 if 89 - 89: OoooooooOO % OoOoOO00 - Ooo00oOo00o % i11iIiiIii
elif oOo0OOoooO == 17 :
 i1IiI ( iiIiii1IIIII , i1iIIIi1i )
 if 7 - 7: I1IIiI1
elif oOo0OOoooO == 18 :
 OoooO0 ( )
 if 15 - 15: Oo + oOOoo0Oo + OOOo0 * OOooOOo
elif oOo0OOoooO == 19 :
 OOOooo ( i1iIIIi1i , iiIiii1IIIII , Iii1I1111ii )
 if 33 - 33: OOooOOo * Oo
elif oOo0OOoooO == 40 :
 oOO0 ( i1iIIIi1i , iiIiii1IIIII , Iii1I1111ii )
 if 88 - 88: O00Oo000ooO0 % Ii11I - I1IiI - I1IiI . OOOo0
elif oOo0OOoooO == 42 :
 oOIi111 ( i1iIIIi1i , iiIiii1IIIII , Iii1I1111ii )
 if 52 - 52: OoOoOO00 / OoOoOO00 / OOOo0 - O00Oo000ooO0
elif oOo0OOoooO == 43 :
 o0oOoO0O ( i1iIIIi1i , iiIiii1IIIII , Iii1I1111ii )
 if 91 - 91: OOOo0 + OOooOOo % OoOoOO00 + Ooo00oOo00o
elif oOo0OOoooO == 20 :
 ii111I11iI ( iiIiii1IIIII )
 if 66 - 66: iIii1I11I1II1 * OoOoOO00 % Oo % OOOo0 - oO0O0ooO0Oo
elif oOo0OOoooO == 22 :
 i1iI11Ii1i ( iiIiii1IIIII )
 if 59 - 59: I1IIiI1 % ii
elif oOo0OOoooO == 23 :
 I1111III111ii ( iiIiii1IIIII )
 if 21 - 21: OoooooooOO % I1IiI - I1IiI / ii11ii1ii / OOooOOo
elif oOo0OOoooO == 24 :
 o0O0O0O00o ( iiIiii1IIIII )
 if 15 - 15: oO0 / oO0 % OoooooooOO . O00Oo000ooO0
elif oOo0OOoooO == 25 :
 iiI111iIi1 ( iiIiii1IIIII )
 if 93 - 93: ii11ii1ii * ii11ii1ii / OoooooooOO
elif oOo0OOoooO == 26 :
 IIIIIIi1IIi1I11i ( iiIiii1IIIII )
 if 6 - 6: ii11ii1ii * Oo + iIii1I11I1II1
elif oOo0OOoooO == 27 :
 oOOo0oO ( iiIiii1IIIII )
 if 19 - 19: O0 % OoOoOO00 * OOooOOo
elif oOo0OOoooO == 28 :
 O00o ( iiIiii1IIIII )
 if 27 - 27: Ii11I * I1IIiI1 / i11iIiiIii - ii + OoOoOO00
elif oOo0OOoooO == 29 :
 i111111 ( iiIiii1IIIII )
 if 43 - 43: ii11ii1ii - OoOoOO00
elif oOo0OOoooO == 30 :
 I111IiiIi1 ( iiIiii1IIIII )
 if 56 - 56: ii11ii1ii . i1IIi / oOOoo0Oo % ii / O0 * oOo00oOO0O
elif oOo0OOoooO == 31 :
 iIIIi1i1Ii ( iiIiii1IIIII )
 if 98 - 98: O0 + oOOoo0Oo
elif oOo0OOoooO == 32 :
 oOO00O0Ooooo00 ( )
 if 23 - 23: OoooooooOO . iIii1I11I1II1 / i1IIi
elif oOo0OOoooO == 33 :
 o0ooO ( )
 if 31 - 31: Oo - iIii1I11I1II1 / oOo00oOO0O . Ooo00oOo00o
elif oOo0OOoooO == 35 :
 i1i1111IiI ( iiIiii1IIIII )
 if 74 - 74: Oo - OoOoOO00 - I1IIiI1
elif oOo0OOoooO == 34 :
 Ii1ii111i1 ( iiIiii1IIIII )
 if 50 - 50: OOOo0 - ii + ii * oOo00oOO0O + ii
elif oOo0OOoooO == 36 :
 IiiI1iiiiI1iI ( iiIiii1IIIII )
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
elif oOo0OOoooO == 37 :
 iIiii ( iiIiii1IIIII )
 if 30 - 30: I1IiI - i11iIiiIii
elif oOo0OOoooO == 38 :
 O00Oo0o000oO ( iiIiii1IIIII )
 if 94 - 94: I1IiI % oOOoo0Oo
elif oOo0OOoooO == 41 :
 O00O ( OO00OO0 )
 if 39 - 39: I1IiI + O00Oo000ooO0 % O0
elif oOo0OOoooO == 39 :
 I1IIIIII1 ( iiIiii1IIIII )
 if 26 - 26: oO0 + I1IiI
elif oOo0OOoooO == 45 :
 TEXTS ( )
 if 17 - 17: ii11ii1ii - oOOoo0Oo % Oo * O0 % O0 * Ii11I
elif oOo0OOoooO == 46 :
 OooO0o ( )
 if 6 - 6: O00Oo000ooO0
elif oOo0OOoooO == 47 :
 GEVID ( )
 if 46 - 46: OoOoOO00 * O00Oo000ooO0
elif oOo0OOoooO == 48 :
 i1I1IiI ( i1iIIIi1i , iiIiii1IIIII , Iii1I1111ii )
 if 23 - 23: i1IIi - O0
elif oOo0OOoooO == 49 :
 Oooo00 ( )
 if 6 - 6: oO0 % OoooooooOO * O00Oo000ooO0 - I1IIiI1
elif oOo0OOoooO == 222 :
 IIii11I1 ( iiIiii1IIIII )
 if 24 - 24: oOo00oOO0O / iIii1I11I1II1 . OoooooooOO % I1IiI . oO0O0ooO0Oo
elif oOo0OOoooO == 333 :
 ooo000o ( iiIiii1IIIII )
 if 73 - 73: O00Oo000ooO0
 if 25 - 25: I1IIiI1
elif oOo0OOoooO == 1020 :
 IIi ( )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif oOo0OOoooO == 1021 :
 ANIMEEP ( )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . oO0O0ooO0Oo - Oo . i11iIiiIii
elif oOo0OOoooO == 1022 :
 ANIMEPLAY ( iiIiii1IIIII )
 if 47 - 47: Oo % Ooo00oOo00o - oO0 - Oo * ii
elif oOo0OOoooO == 1001 :
 oOOoOOooO0 ( )
 if 72 - 72: OOooOOo % OOooOOo + oOOoo0Oo + ii11ii1ii / Oo
elif oOo0OOoooO == 1005 :
 iIIIi1iii1I11 ( )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif oOo0OOoooO == 1007 :
 O0o0 ( iiIiii1IIIII )
 if 64 - 64: I1IIiI1
elif oOo0OOoooO == 1010 :
 iiiiIii11i1 ( iiIiii1IIIII )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif oOo0OOoooO == 1011 :
 IiI11IIi1iI1i ( iiIiii1IIIII )
 if 89 - 89: O0 + I1IIiI1 * O00Oo000ooO0
elif oOo0OOoooO == 1030 :
 iI1iI ( )
 if 30 - 30: I1IiI
elif oOo0OOoooO == 1031 :
 O0oo0000o ( iiIiii1IIIII , i1I1i111Ii )
 if 39 - 39: ii11ii1ii + OOooOOo + O00Oo000ooO0 + I1IIiI1
elif oOo0OOoooO == 1006 :
 Parse . ParseURL ( iiIiii1IIIII )
 if 48 - 48: O00Oo000ooO0 / oO0 . iIii1I11I1II1
elif oOo0OOoooO == 2030 :
 Parse . addonParseURL ( iiIiii1IIIII )
 if 72 - 72: i1IIi . OOooOOo
elif oOo0OOoooO == 2031 :
 Parse . apkParseURL ( iiIiii1IIIII )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif oOo0OOoooO == 1002 :
 o0III11IiI ( iiIiii1IIIII )
 if 52 - 52: Ooo00oOo00o
elif oOo0OOoooO == 1003 :
 o0ooo ( iiIiii1IIIII , i1I1i111Ii )
 if 49 - 49: oO0O0ooO0Oo . ii11ii1ii % oO0 . Oo * Ii11I
elif oOo0OOoooO == 1004 :
 o0oo00O ( iiIiii1IIIII )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . oO0
elif oOo0OOoooO == 1008 :
 I11I111i1I1 ( )
 if 20 - 20: oOOoo0Oo + OOooOOo . O00Oo000ooO0 / i11iIiiIii
elif oOo0OOoooO == 1009 :
 M3UPLAY ( iiIiii1IIIII )
 if 7 - 7: I1IiI / I1IiI . O00Oo000ooO0 * O0 + I1IIiI1 + ii
elif oOo0OOoooO == 2001 :
 iiiIIiii11I1 ( iiIiii1IIIII )
 if 98 - 98: OoOoOO00 * I1IIiI1 - OOOo0 % OOooOOo - oOOoo0Oo % ii11ii1ii
elif oOo0OOoooO == 1013 :
 IiiO0o0o ( )
 if 69 - 69: i1IIi % Ooo00oOo00o % O00Oo000ooO0 / oO0 / oO0
elif oOo0OOoooO == 1014 :
 i1i1I11i1I ( )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * oO0
elif oOo0OOoooO == 1015 :
 O0oII1IIiiI1 ( iiIiii1IIIII )
 if 47 - 47: O0
elif oOo0OOoooO == 1016 :
 IIi11I1i1I1I ( iiIiii1IIIII )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif oOo0OOoooO == 1023 :
 i1i111iI ( )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif oOo0OOoooO == 1024 :
 iI1 ( )
 if 88 - 88: ii11ii1ii * oOOoo0Oo + OoOoOO00
elif oOo0OOoooO == 1025 :
 O000OOOo ( iiIiii1IIIII )
 if 62 - 62: OoooooooOO
elif oOo0OOoooO == 4001 :
 MenWish ( )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif oOo0OOoooO == 4003 :
 ooo0O ( )
 if 50 - 50: oO0
elif oOo0OOoooO == 4004 :
 Ii1iIiii1 ( )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * Ii11I
elif oOo0OOoooO == 4005 :
 I1III ( )
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif oOo0OOoooO == 4006 :
 OO0O0OoOO0 ( )
 if 59 - 59: oOOoo0Oo - OoooooooOO / oO0 + ii11ii1ii . OOooOOo - oOOoo0Oo
elif oOo0OOoooO == 4007 :
 o0oo0oOo ( )
 if 29 - 29: ii
elif oOo0OOoooO == 4008 :
 o000O0o ( )
 if 26 - 26: O0 % Ii11I - I1IIiI1 . Ii11I
elif oOo0OOoooO == 4009 : Oo0oOOo ( )
elif oOo0OOoooO == 4010 : O0OoooO0 ( )
elif oOo0OOoooO == 3000 :
 OO0 ( )
 if 70 - 70: OOooOOo + oOo00oOO0O / oOOoo0Oo + oO0 / OOOo0
elif oOo0OOoooO == 3001 :
 oOooOO ( )
 if 33 - 33: OoooooooOO . O0
elif oOo0OOoooO == 3002 :
 Ii1I1OO0ooO0 ( iiIiii1IIIII )
 if 59 - 59: iIii1I11I1II1
elif oOo0OOoooO == 3003 :
 OoOooOO0oOOo0O ( iiIiii1IIIII )
 if 45 - 45: O0
elif oOo0OOoooO == 3004 :
 iIIi1Ii1III ( iiIiii1IIIII )
 if 78 - 78: oOo00oOO0O - iIii1I11I1II1 + O00Oo000ooO0 - ii11ii1ii - O00Oo000ooO0
elif oOo0OOoooO == 404 :
 O0o0O0OooOoo ( i1iIIIi1i , iiIiii1IIIII , i1I1i111Ii )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif oOo0OOoooO == 405 :
 Ooooo00 ( iiIiii1IIIII )
 if 86 - 86: I1IiI / Ii11I
elif oOo0OOoooO == 7030 :
 I1oO0oOOOooo ( )
 if 40 - 40: iIii1I11I1II1 / oO0 / OOOo0 + ii11ii1ii * Ii11I
elif oOo0OOoooO == 7021 :
 OoOO0o0o0 ( i1iIIIi1i )
 if 1 - 1: Ooo00oOo00o * oO0 + I1IIiI1 . ii / oO0
elif oOo0OOoooO == 7022 :
 OOOoo000o0oo0 ( i1iIIIi1i )
 if 91 - 91: oO0O0ooO0Oo + oOo00oOO0O - Oo % I1IiI . oOOoo0Oo
elif oOo0OOoooO == 7000 :
 o00oOOo ( i1iIIIi1i , iiIiii1IIIII , img )
 if 51 - 51: Ii11I / oOo00oOO0O
elif oOo0OOoooO == 7050 :
 OO0Ooo0Oooo ( iiIiii1IIIII )
 if 51 - 51: oO0 * ii - O00Oo000ooO0 + oOOoo0Oo
elif oOo0OOoooO == 7051 :
 oOo0OoOOOo0 ( iiIiii1IIIII )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / oO0O0ooO0Oo - I1IiI
elif oOo0OOoooO == 7052 :
 O0O0O ( iiIiii1IIIII )
 if 88 - 88: ii * OOOo0 / Ooo00oOo00o - Ii11I / i1IIi . O00Oo000ooO0
elif oOo0OOoooO == 7053 :
 II1io0Oo00oOO ( iiIiii1IIIII )
 if 26 - 26: i11iIiiIii - oO0
elif oOo0OOoooO == 7054 :
 CoolPlay ( iiIiii1IIIII )
 if 45 - 45: oO0 + OoOoOO00 % oOOoo0Oo
elif oOo0OOoooO == 7060 :
 ooOoOo ( )
 if 55 - 55: oO0 - ii % OOOo0
elif oOo0OOoooO == 7061 :
 ooO0 ( iiIiii1IIIII )
 if 61 - 61: oO0
elif oOo0OOoooO == 7063 :
 iIi ( iiIiii1IIIII )
 if 22 - 22: iIii1I11I1II1 / oO0 / OOOo0 - OOooOOo
elif oOo0OOoooO == 7062 :
 O0OooooO0o0O0 ( iiIiii1IIIII )
 if 21 - 21: ii . i11iIiiIii * oOo00oOO0O . Ii11I / Ii11I
elif oOo0OOoooO == 7064 :
 NATatozcat ( )
 if 42 - 42: OoooooooOO / O00Oo000ooO0 . OOooOOo / O0 - I1IIiI1 * I1IIiI1
elif oOo0OOoooO == 7067 :
 o00o0o000Oo ( iiIiii1IIIII )
 if 1 - 1: oO0O0ooO0Oo % O00Oo000ooO0
elif oOo0OOoooO == 7066 :
 NATatozA ( iiIiii1IIIII )
 if 97 - 97: I1IiI
elif oOo0OOoooO == 7065 :
 Oooo00OOo ( iiIiii1IIIII )
 if 13 - 13: I1IiI % Ii11I . O0 / Oo % Oo
elif oOo0OOoooO == 7070 :
 Iii1I1iI ( )
 if 19 - 19: O00Oo000ooO0 % oO0 - oO0 % OOOo0 . Ii11I - OoooooooOO
elif oOo0OOoooO == 7071 :
 DIZIlist ( iiIiii1IIIII )
 if 100 - 100: OOOo0 + oO0O0ooO0Oo + OOooOOo . i1IIi % OoooooooOO
elif oOo0OOoooO == 7072 :
 DIZIpull ( iiIiii1IIIII )
 if 64 - 64: O0 % i1IIi * O00Oo000ooO0 - oO0O0ooO0Oo + Oo
elif oOo0OOoooO == 7073 :
 WATCHDIZI ( iiIiii1IIIII )
 if 65 - 65: I1IiI . i11iIiiIii
elif oOo0OOoooO == 7002 :
 oO00oOoo00o0 ( )
 if 36 - 36: ii * oOOoo0Oo + I1IIiI1 * oOOoo0Oo . ii11ii1ii - iIii1I11I1II1
elif oOo0OOoooO == 7003 :
 I1i ( iiIiii1IIIII )
 if 14 - 14: oOo00oOO0O * ii + i11iIiiIii
elif oOo0OOoooO == 7004 :
 Oo0ooooO0O0oo ( iiIiii1IIIII )
 if 84 - 84: oOOoo0Oo / OoOoOO00
elif oOo0OOoooO == 7020 :
 OoOoO0oO00O ( iiIiii1IIIII )
 if 86 - 86: OOOo0
elif oOo0OOoooO == 7001 :
 oo0O0oOOO0o ( )
 if 97 - 97: OoOoOO00
elif oOo0OOoooO == 7010 :
 I1I ( iiIiii1IIIII )
 if 38 - 38: OOOo0
elif oOo0OOoooO == 7011 :
 o0OOi11Ii1 ( iiIiii1IIIII )
 if 42 - 42: OOooOOo
elif oOo0OOoooO == 7012 :
 oO000 ( iiIiii1IIIII )
 if 8 - 8: i11iIiiIii / oO0
elif oOo0OOoooO == 7013 :
 cnfTVPlay2 ( iiIiii1IIIII )
elif oOo0OOoooO == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iiIiii1IIIII )
elif oOo0OOoooO == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iiIiii1IIIII )
elif oOo0OOoooO == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( i1iIIIi1i , iiIiii1IIIII , i1I1i111Ii )
elif oOo0OOoooO == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oOo0OOoooO == 7018 :
 IiII1i ( )
elif oOo0OOoooO == 7019 :
 CNF_Studio_Indexer . List_Movies ( iiIiii1IIIII )
elif oOo0OOoooO == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iiIiii1IIIII )
elif oOo0OOoooO == 7024 :
 CNF_Studio_Indexer . Box_Office ( iiIiii1IIIII )
 if 33 - 33: O00Oo000ooO0 * I1IIiI1 - O0 + OOOo0 / I1IIiI1
elif oOo0OOoooO == 8000 :
 IiiI1I ( )
elif oOo0OOoooO == 8001 :
 Ii1i1i ( )
elif oOo0OOoooO == 8002 :
 i1IiIiIiiI1 ( )
elif oOo0OOoooO == 8003 :
 o0O ( )
elif oOo0OOoooO == 8004 :
 oO0oo0O0 ( )
elif oOo0OOoooO == 8005 :
 OO0OooOo ( )
elif oOo0OOoooO == 8006 :
 Ii11IiI111 ( i1iIIIi1i , iiIiii1IIIII )
elif oOo0OOoooO == 8030 :
 OoO ( iiIiii1IIIII )
elif oOo0OOoooO == 8045 :
 o0oO0OO00oo0o ( iiIiii1IIIII )
elif oOo0OOoooO == 8046 :
 I1II1 ( iiIiii1IIIII )
elif oOo0OOoooO == 8047 :
 o00oo0OO0 ( iiIiii1IIIII )
elif oOo0OOoooO == 8020 :
 OO0OO00ooO0 ( )
elif oOo0OOoooO == 8021 :
 OOOOOoO00oo00 ( iiIiii1IIIII )
elif oOo0OOoooO == 8022 :
 iIIIII11 ( iiIiii1IIIII )
elif oOo0OOoooO == 8023 :
 ooooOOO0 ( iiIiii1IIIII )
elif oOo0OOoooO == 8040 :
 O000O ( )
elif oOo0OOoooO == 8041 :
 OOOoOOo0o ( iiIiii1IIIII )
elif oOo0OOoooO == 8042 :
 IiIioO0Oo00oo ( iiIiii1IIIII )
elif oOo0OOoooO == 8043 :
 yt . PlayVideo ( iiIiii1IIIII )
elif oOo0OOoooO == 8044 :
 OoOoooO000OO ( iiIiii1IIIII )
elif oOo0OOoooO == 8060 :
 i1I111Ii ( )
elif oOo0OOoooO == 8061 :
 i11i1i ( iiIiii1IIIII )
elif oOo0OOoooO == 8064 :
 OooOOOoOoo0O0 ( )
elif oOo0OOoooO == 8065 :
 O0OOOOo0 ( iiIiii1IIIII )
elif oOo0OOoooO == 8070 :
 o0iIIIIi ( )
elif oOo0OOoooO == 8071 :
 i1I11ii ( iiIiii1IIIII )
elif oOo0OOoooO == 7080 :
 o0ooO00O0O ( iiIiii1IIIII )
elif oOo0OOoooO == 8090 :
 OOOO0Oo ( )
elif oOo0OOoooO == 8091 :
 iIiI1 ( iiIiii1IIIII )
elif oOo0OOoooO == 8092 :
 I1IiII1I1i1I1 ( iiIiii1IIIII )
elif oOo0OOoooO == 8081 :
 O0i1I11I ( )
elif oOo0OOoooO == 8062 :
 ooOO ( iiIiii1IIIII )
elif oOo0OOoooO == 8063 :
 o0OOO00ooo ( iiIiii1IIIII )
elif oOo0OOoooO == 8050 :
 OOO00oo0ooO ( )
elif oOo0OOoooO == 8051 :
 iiIii1ii ( iiIiii1IIIII )
elif oOo0OOoooO == 8052 :
 iIIIII1iiiiII ( iiIiii1IIIII )
elif oOo0OOoooO == 8085 :
 ii1oOoO0ooO0000 ( )
elif oOo0OOoooO == 8086 :
 I1iiiI ( iiIiii1IIIII )
elif oOo0OOoooO == 8087 :
 Oo0O0000Oo00o ( iiIiii1IIIII )
elif oOo0OOoooO == 8088 :
 II1 ( iiIiii1IIIII , i1iIIIi1i )
elif oOo0OOoooO == 9000 :
 OOo ( )
elif oOo0OOoooO == 1111 :
 OOoO00O ( )
elif oOo0OOoooO == 9001 :
 i1II11IiiiI ( )
elif oOo0OOoooO == 9002 :
 ii1iiIi ( )
elif oOo0OOoooO == 9003 :
 ooO000OO ( )
elif oOo0OOoooO == 50 :
 O00oooo00o0O ( iiIiii1IIIII )
elif oOo0OOoooO == 9020 :
 champlist ( )
elif oOo0OOoooO == 9021 :
 IiIiiI1ii111 ( )
elif oOo0OOoooO == 9022 :
 i11ii1 ( )
elif oOo0OOoooO == 9023 :
 Ii111I11 ( )
elif oOo0OOoooO == 9024 :
 I11IiI1i ( iiIiii1IIIII )
elif oOo0OOoooO == 9030 :
 IiI11I1Ii11II ( iiIiii1IIIII )
elif oOo0OOoooO == 9031 :
 oo0ooOoOOoO ( iiIiii1IIIII )
elif oOo0OOoooO == 9032 :
 Oo0000o ( iiIiii1IIIII )
elif oOo0OOoooO == 9033 :
 iI1IiiiIIiiII ( iiIiii1IIIII )
elif oOo0OOoooO == 7085 :
 oOoo0OO0 ( iiIiii1IIIII )
elif oOo0OOoooO == 7086 :
 i111 ( iiIiii1IIIII )
elif oOo0OOoooO == 7087 :
 o0OoOooOO0o0 ( Iii1I1111ii )
elif oOo0OOoooO == 9666 :
 iII1 ( iiIiii1IIIII )
elif oOo0OOoooO == 10100 : i1iI1i ( )
elif oOo0OOoooO == 10105 : Oo0oOO ( iiIiii1IIIII )
elif oOo0OOoooO == 10106 : iI1ii ( iiIiii1IIIII )
elif oOo0OOoooO == 10104 : OoOoOOoO ( iiIiii1IIIII )
elif oOo0OOoooO == 10107 : IiIiIi1I11I ( )
elif oOo0OOoooO == 10103 : oOoO0OOO00O ( iiIiii1IIIII )
elif oOo0OOoooO == 10108 : oO0o0Oo ( iiIiii1IIIII )
elif oOo0OOoooO == 10107 : IiIiIi1I11I ( )
elif oOo0OOoooO == 10000 : Origin_Menu ( )
elif oOo0OOoooO == 10001 : OOooo00 ( )
elif oOo0OOoooO == 10002 : II111i1ii1iII ( )
elif oOo0OOoooO == 10003 : oo0o0oOo ( )
elif oOo0OOoooO == 10004 : o0O0ooOOoO ( iiIiii1IIIII )
elif oOo0OOoooO == 10005 : Ii1IIi ( )
elif oOo0OOoooO == 10006 : oo0 ( iiIiii1IIIII )
elif oOo0OOoooO == 10007 : oo00ooOoo ( iiIiii1IIIII , i1I1i111Ii )
elif oOo0OOoooO == 10008 : I1I1i1i ( )
elif oOo0OOoooO == 10009 : oOOO0 ( )
elif oOo0OOoooO == 10010 : O0O000oOo0O ( iiIiii1IIIII )
elif oOo0OOoooO == 10011 : II1Iiii11111 ( iiIiii1IIIII )
elif oOo0OOoooO == 10012 : I11Ii ( iiIiii1IIIII )
elif oOo0OOoooO == 10013 : iiiii111 ( iiIiii1IIIII )
elif oOo0OOoooO == 10014 : i111i11I1Ii1I ( )
elif oOo0OOoooO == 10015 : i1I ( )
elif oOo0OOoooO == 10016 : Ii1I ( iiIiii1IIIII )
elif oOo0OOoooO == 10017 : i1i1IiIiIi1Ii ( )
elif oOo0OOoooO == 10018 : IiI1iI1IiiIi1 ( )
elif oOo0OOoooO == 10019 : Ii ( )
elif oOo0OOoooO == 10020 : O0Oo0 ( )
elif oOo0OOoooO == 10021 : i11Ii1iIiII ( )
elif oOo0OOoooO == 10022 : IIi1I1i ( iiIiii1IIIII )
elif oOo0OOoooO == 10023 : i11iI11I1I ( i1iIIIi1i , iiIiii1IIIII )
elif oOo0OOoooO == 10024 : OOiI1 ( iiIiii1IIIII )
elif oOo0OOoooO == 10025 : oOooo0Oo ( )
elif oOo0OOoooO == 10026 : O0oOoo0OoO0O ( )
elif oOo0OOoooO == 10027 : oooO00o0 ( )
elif oOo0OOoooO == 10028 : iIIIiIi1I1i ( )
elif oOo0OOoooO == 10029 : ooOo0O0O0oOO0 ( )
elif oOo0OOoooO == 423 : Ii1I1 ( iiIiii1IIIII )
elif oOo0OOoooO == 426 : Ii1iI ( iiIiii1IIIII )
elif oOo0OOoooO == 10030 : Izle_Films ( )
elif oOo0OOoooO == 10031 : Latest_Izle_Movies ( )
elif oOo0OOoooO == 10032 : Izle_Genres ( )
elif oOo0OOoooO == 10033 : Izle_Pop_Movies ( )
elif oOo0OOoooO == 10034 : Izle_Boxsets ( )
elif oOo0OOoooO == 10035 : Izle_Search ( )
elif oOo0OOoooO == 10036 : Izle_Genres_Movie ( iiIiii1IIIII )
elif oOo0OOoooO == 10037 : Izle_Boxset_single ( iiIiii1IIIII )
elif oOo0OOoooO == 10038 : Izle_IFRAME ( )
elif oOo0OOoooO == 10039 : Izle_Boxsets_Next ( iiIiii1IIIII )
elif oOo0OOoooO == 10040 : II11I ( )
elif oOo0OOoooO == 10041 : oo0OoOOooO ( iiIiii1IIIII )
elif oOo0OOoooO == 10042 : i1iIiIii ( iiIiii1IIIII )
elif oOo0OOoooO == 10043 : i11I1I ( )
elif oOo0OOoooO == 10044 : oOO0o00o0Oo0O ( iiIiii1IIIII )
elif oOo0OOoooO == 10045 : i1ooOoo000oO ( i1iIIIi1i )
elif oOo0OOoooO == 10046 : i1IiiiiIi1I ( iiIiii1IIIII )
elif oOo0OOoooO == 10047 : OO0ooo0 ( iiIiii1IIIII )
elif oOo0OOoooO == 10048 : ooooO ( iiIiii1IIIII )
elif oOo0OOoooO == 10049 : iI111i11iI1 ( iiIiii1IIIII )
elif oOo0OOoooO == 10050 : O00Oo00o00O ( )
elif oOo0OOoooO == 10051 : oooOO0OO0 ( )
elif oOo0OOoooO == 10052 : IiIiIi ( )
elif oOo0OOoooO == 10053 : Addon ( iiIiii1IIIII )
elif oOo0OOoooO == 10054 : i1oo ( iiIiii1IIIII , i1iIIIi1i )
elif oOo0OOoooO == 10055 :
 IIiI11i11 ( "addFavorite" )
 try :
  i1iIIIi1i = i1iIIIi1i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1iIIIi1i = i1iIIIi1i . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0oOOO0 ( i1iIIIi1i , iiIiii1IIIII , i1I1i111Ii , ooo , OO000O000OOO )
elif oOo0OOoooO == 10056 :
 IIiI11i11 ( "rmFavorite" )
 try :
  i1iIIIi1i = i1iIIIi1i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1iIIIi1i = i1iIIIi1i . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiii ( i1iIIIi1i )
elif oOo0OOoooO == 10057 :
 IIiI11i11 ( "getFavorites" )
 o0ooO0OOO ( )
elif oOo0OOoooO == 10058 : iiO0oOo00o ( )
elif oOo0OOoooO == 10059 : Donators_Guide ( )
elif oOo0OOoooO == 10060 : O0O0o0oOOO ( )
elif oOo0OOoooO == 10061 : iIIII ( )
elif oOo0OOoooO == 10062 : II1I1Ii ( i1iIIIi1i , iiIiii1IIIII , Iii1I1111ii )
elif oOo0OOoooO == 10063 : iI1i11II1i ( )
elif oOo0OOoooO == 10064 : o0oooOO00 ( )
elif oOo0OOoooO == 10065 : o0OoOo00o0o ( iiIiii1IIIII )
elif oOo0OOoooO == 10066 : IiII111i1i11 ( iiIiii1IIIII )
elif oOo0OOoooO == 10068 : oO00O000oO0 ( iiIiii1IIIII )
elif oOo0OOoooO == 10069 : ooO0OO ( iiIiii1IIIII )
elif oOo0OOoooO == 10070 : OoO0OOOOo0O ( iiIiii1IIIII )
elif oOo0OOoooO == 10071 : Genie_Watch ( )
elif oOo0OOoooO == 10072 : o00oO0oOo00 ( )
elif oOo0OOoooO == 10073 : oOo00O0oo00o0 ( iiIiii1IIIII )
elif oOo0OOoooO == 10074 : o0oOOoo ( iiIiii1IIIII )
elif oOo0OOoooO == 10075 : iI1i11iII111 ( i1I1i111Ii , i1iIIIi1i , iiIiii1IIIII )
elif oOo0OOoooO == 10076 : Ii11iIi ( iiIiii1IIIII )
elif oOo0OOoooO == 10077 : oOo0oO ( iiIiii1IIIII )
elif oOo0OOoooO == 10078 : IIi1 ( )
elif oOo0OOoooO == 10079 : Genie_Watch_Tv_Shows ( )
elif oOo0OOoooO == 10080 : Genie_Watch_Tv_Genre ( iiIiii1IIIII )
elif oOo0OOoooO == 10081 : Genie_Watch_TV_PlayRun ( iiIiii1IIIII )
elif oOo0OOoooO == 10082 : Genie_Watch_TV_Episodes ( iiIiii1IIIII , i1I1i111Ii )
elif oOo0OOoooO == 10083 : Genie_Watch_Tv_Recent ( iiIiii1IIIII )
elif oOo0OOoooO == 10084 : O00o0O00 ( )
elif oOo0OOoooO == 20000 : Ii1 ( )
elif oOo0OOoooO == 20001 : OO00ooOo0OOO ( )
elif oOo0OOoooO == 20002 : ooOOOOo0 ( iiIiii1IIIII )
elif oOo0OOoooO == 20003 : ooO00O00oOO ( iiIiii1IIIII )
elif oOo0OOoooO == 20004 : iii1III1i ( iiIiii1IIIII )
elif oOo0OOoooO == 21004 : II1I11IIi ( )
elif oOo0OOoooO == 21005 : OoOOo ( iiIiii1IIIII )
elif oOo0OOoooO == 21006 : oOO0oo ( iiIiii1IIIII )
elif oOo0OOoooO == 21007 : O0i1i1II1i11 ( iiIiii1IIIII )
elif oOo0OOoooO == 30000 : O0o0O0OO00o ( )
elif oOo0OOoooO == 30001 : I111IIiii1Ii ( )
elif oOo0OOoooO == 10012 : Resolve ( iiIiii1IIIII )
elif oOo0OOoooO == 30003 : ooO000O ( )
elif oOo0OOoooO == 30004 : OooO0oOo ( iiIiii1IIIII )
elif oOo0OOoooO == 30005 : II1IIIiiI11 ( iiIiii1IIIII )
elif oOo0OOoooO == 30006 : IIIi1i ( )
elif oOo0OOoooO == 30007 : OO0OO0OO ( )
elif oOo0OOoooO == 30008 : oooo0OOo ( iiIiii1IIIII )
elif oOo0OOoooO == 30009 : I11iIiI1 ( iiIiii1IIIII )
elif oOo0OOoooO == 30010 : iIII11Ii ( iiIiii1IIIII )
elif oOo0OOoooO == 30011 : Iii111Ii ( )
elif oOo0OOoooO == 30012 : IIiiIIIi ( )
elif oOo0OOoooO == 30013 : iIIiI1I1i ( )
elif oOo0OOoooO == 30014 : i1II ( )
elif oOo0OOoooO == 30015 : OooO0O0Ooo ( iiIiii1IIIII )
elif oOo0OOoooO == 100000 : Ooo0OO0oOO ( )
if 19 - 19: i1IIi % OoOoOO00
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
