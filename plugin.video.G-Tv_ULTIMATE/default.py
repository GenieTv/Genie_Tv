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
import re
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from imports . tvGuide import gui
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 'plugin.video.G-Tv_ULTIMATE'
IiII = 'plugin.video.G-Tv_ULTIMATE'
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = xbmcaddon . Addon ( id = IiII )
I1i1iiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
IiII = 'plugin.video.G-Tv_ULTIMATE'
iiIIIII1i1iI = 'plugin.video.G-Tv_ULTIMATE'
o0oO0 = xbmcgui . DialogProgress ( )
oo00 = "G-Tv ULTIMATE"
o00 = Net ( )
Oo0oO0ooo = base64 . decodestring
o0oOoO00o = O0oo0OO0 . getSetting ( 'User' )
i1 = O0oo0OO0 . getSetting ( 'Pass' )
oOOoo00O0O = O0oo0OO0 . getSetting ( 'AdultPass' )
i1111 = xbmc . translatePath ( 'special://home/' )
i11 = ( Oo0oO0ooo ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
I11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII , 'icon.png' ) )
Oo0o0000o0o0 = i11 + 'GenieArt/NEW/'
oOo0oooo00o = "0.0.6"
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.G-Tv_ULTIMATE' )
oo0o0O00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.G-Tv_ULTIMATE/imports/tvGuide/ResetDatabase.py' ) )
oO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.G-Tv_ULTIMATE/imports/tvGuide/addon.py' ) )
i1iiIIiiI111 = xbmc . translatePath ( 'special://thumbnails' ) ;
oooOOOOO = "Xhoans"
i1iiIII111ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII , 'fanart.jpg' ) )
i1iIIi1 = base64 . decodestring ( 'LnBocA==' )
ii11iIi1I = O0oo0OO0 . getLocalizedString
iI111I11I1I1 = CookieJar ( )
OOooO0OOoo = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( iI111I11I1I1 ) )
OOooO0OOoo . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
iIii1 = int ( sys . argv [ 1 ] )
oOOoO0 = xbmc . translatePath ( O0oo0OO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
O0OoO000O0OO = xbmc . translatePath ( 'special://home/userdata/' )
iiI1IiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
II = oO0o0o0ooO0oO + '/addons.ini'
ooOoOoo0O = xbmcgui . Dialog ( )
if 76 - 76: i1II1I11 / i1I / OO0o / oo % OOooOOo
def oo0Oo00Oo0 ( ) :
 oOOO00o ( )
 O0O00o0OOO0 ( '[COLORsteelblue]PLEASE LINK CHANNELS TO GUIDE[/COLOR]' , '' , 13 , Oo0o0000o0o0 + 'linkchannels.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'Tv Guide' , '' , 11 , Oo0o0000o0o0 + 'TvGuide.png' , i1iiIII111ii , '' )
 Ii1iIIIi1ii ( 'Stream Lists' , '' , 16 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 if 80 - 80: I11i * i11iIiiIii / OO0o
 if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
def oOOO00o ( ) :
 if i1 == 'insert_password' :
  ooOoOoo0O . ok ( '[COLORsteelblue]G-Tv Ultimate Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]http://genietv.co.uk[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  III1i1i = open ( II , "r" )
  iiI1 = re . compile ( 'plugin.video.G-Tv_ULTIMATE.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( III1i1i ) )
  for i11Iiii , iI in iiI1 :
   if i11Iiii == 'replace_user' or iI == 'replace_pass' :
    ooOoOoo0O . ok ( '[COLOR=yellow]Need to set login details' , 'You need to input your login details to activate streams' , '' )
    O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
    if 28 - 28: OOooOOo - i1I . i1I + OoOoOO00 - OoooooooOO + O0
    if 95 - 95: OoO0O00 % oO0o . O0
def I1i1I ( ) :
 O0O00o0OOO0 ( 'Full List' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'PPV' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'Entertainment' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'Factual' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'Movie Channels' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'US Movie Channels TEST' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'Kids' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'Music' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'UK Sports' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'International Sports' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'News UK & International' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'German' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'Arabic' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'TV Series Latest' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'VOD Latest' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 O0O00o0OOO0 ( 'VOD Bollywood' , '' , 60003 , Oo0o0000o0o0 + 'UltimateList.png' , i1iiIII111ii , '' )
 if 80 - 80: OoOoOO00 - OoO0O00
 if 87 - 87: oO0o / I11i - i1IIi * OOooOOo / OoooooooOO . O0
def iii11I111 ( name ) :
 OOOO00ooo0Ooo = name
 OOOooOooo00O0 = Oo0OO ( Oo0oO0ooo ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 iiI1 = re . compile ( '#EXTINF:-1 tvg-name="(.+?)" tvg-logo="(.+?)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( OOOooOooo00O0 )
 for name , oOOoOo00o , o0OOoo0OO0OOO in iiI1 :
  o0OOoo0OO0OOO = ( o0OOoo0OO0OOO ) . replace ( 'replace_user' , o0oOoO00o ) . replace ( 'replace_pass' , i1 )
  O0O00o0OOO0 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OOoo0OO0OOO ) . strip ( ) , 15 , oOOoOo00o , oOOoOo00o , '' )
 else :
  O0O00o0OOO0 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 15 , '' , '' , '' )
  if 19 - 19: oO0o % i1IIi % o0oOOo0O0Ooo
def oo0OooOOo0 ( ) :
 ooOoOoo0O . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + oo0o0O00 + ")" )
 o0O ( )
 ooOoOoo0O . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 72 - 72: i1II1I11 / i1IIi * Oo0Ooo - OO0o
 if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / oo
def iIIIIii1 ( name ) :
 OOOO00ooo0Ooo = name
 OOOooOooo00O0 = Oo0OO ( 'http://piesustv.net:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=mpegts' )
 iiI1 = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( OOOooOooo00O0 )
 for name , oOOoOo00o , oo000OO00Oo , o0OOoo0OO0OOO in iiI1 :
  if OOOO00ooo0Ooo == 'Full List' :
   o0OOoo0OO0OOO = ( o0OOoo0OO0OOO ) . replace ( '.ts' , '.m3u8' )
   addDir2 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OOoo0OO0OOO ) . strip ( ) , 10012 , oOOoOo00o , oOOoOo00o , '' )
  else :
   OOOO00ooo0Ooo = ( OOOO00ooo0Ooo ) . replace ( 'World' , 'القنوات العربية' )
   if OOOO00ooo0Ooo in oo000OO00Oo :
    o0OOoo0OO0OOO = ( o0OOoo0OO0OOO ) . replace ( '.ts' , '.m3u8' )
    print o0OOoo0OO0OOO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    addDir2 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OOoo0OO0OOO ) . strip ( ) , 10012 , oOOoOo00o , oOOoOo00o , '' )
   else :
    pass
def O0OOO0OOoO0O ( ) :
 o0O ( )
 try :
  O00Oo000ooO0 = gui . TVGuide ( )
  O00Oo000ooO0 . doModal ( )
  del O00Oo000ooO0
  if 100 - 100: O0 + i1I - OOooOOo + i11iIiiIii * Ii1I
 except :
  import sys
  import traceback as tb
  ( iII , o0 , traceback ) = sys . exc_info ( )
  tb . print_exception ( iII , o0 , traceback )
  if 62 - 62: iIii1I11I1II1 * OoOoOO00
def Oo0OO ( url ) :
 i1OOO = urllib2 . Request ( url )
 i1OOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0oOOo = urllib2 . urlopen ( i1OOO )
 Oo0OoO00oOO0o = Oo0oOOo . read ( )
 Oo0oOOo . close ( )
 return Oo0OoO00oOO0o
 if 80 - 80: oO0o + OOooOOo - OOooOOo % i1II1I11
 if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
 if 98 - 98: i1II1I11 * i1II1I11 / i1II1I11 + I11i
def o0O ( ) :
 ii111111I1iII = os . path . join ( oO0o0o0ooO0oO , 'addons.ini' )
 O00ooo0O0 = open ( ii111111I1iII , "w+" )
 OOOooOooo00O0 = Oo0OO ( 'http://piesustv.net:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=mpegts' )
 iiI1 = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( OOOooOooo00O0 )
 O00ooo0O0 . write ( r'[' + IiiIII111iI + ']' + '\n' )
 for i1iIi1iIi1i , oOOoOo00o , oo000OO00Oo , o0OOoo0OO0OOO in iiI1 :
  o0OOoo0OO0OOO = ( o0OOoo0OO0OOO + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I1I1iIiII1 = ( i1iIi1iIi1i + '=plugin://' + IiiIII111iI + '/?url=' + o0OOoo0OO0OOO + '&mode=10012&name=' + ( i1iIi1iIi1i ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOOoOo00o ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOOoOo00o ) . replace ( ' ' , '' ) + '+&amp;description=' )
  O00ooo0O0 . write ( I1I1iIiII1 + '\n' )
  if 4 - 4: oo + O0 * OOooOOo
def OOoo0O ( url ) :
 Oo0ooOo0o = xbmc . Player ( Ii1i1 ( ) )
 import urlresolver
 try : Oo0ooOo0o . play ( url ) . strip ( )
 except : pass
 if 15 - 15: II111iiii
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
def Ii1i1 ( ) :
 try :
  OO0OoO0o00 = getSet ( "core-player" )
  if ( OO0OoO0o00 == 'DVDPLAYER' ) : ooOO0O0ooOooO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OO0OoO0o00 == 'MPLAYER' ) : ooOO0O0ooOooO = xbmc . PLAYER_CORE_MPLAYER
  elif ( OO0OoO0o00 == 'PAPLAYER' ) : ooOO0O0ooOooO = xbmc . PLAYER_CORE_PAPLAYER
  else : ooOO0O0ooOooO = xbmc . PLAYER_CORE_AUTO
 except : ooOO0O0ooOooO = xbmc . PLAYER_CORE_AUTO
 return ooOO0O0ooOooO
 return True
 if 55 - 55: o0oOOo0O0Ooo * OoOoOO00
 if 61 - 61: I11i
def Ii1iIIIi1ii ( name , url , mode , iconimage , fanart , description ) :
 if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
 iIIi1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1IIIiiII1 = True
 OOOOoOoo0O0O0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOoOoo0O0O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOoOoo0O0O0 . setProperty ( "Fanart_Image" , fanart )
 i1IIIiiII1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIi1i1 , listitem = OOOOoOoo0O0O0 , isFolder = True )
 return i1IIIiiII1
 if 85 - 85: oO0o % i11iIiiIii - i1II1I11 * OoooooooOO / I1IiiI % I1IiiI
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description ) :
 if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
 iIIi1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1IIIiiII1 = True
 OOOOoOoo0O0O0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOoOoo0O0O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOoOoo0O0O0 . setProperty ( "Fanart_Image" , fanart )
 i1IIIiiII1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIi1i1 , listitem = OOOOoOoo0O0O0 , isFolder = False )
 return i1IIIiiII1
 if 78 - 78: O0 . oO0o . II111iiii % OOooOOo
def i1iIi ( ) :
 ooOOoooooo = [ ]
 II1I = sys . argv [ 2 ]
 if len ( II1I ) >= 2 :
  O0i1II1Iiii1I11 = sys . argv [ 2 ]
  IIII = O0i1II1Iiii1I11 . replace ( '?' , '' )
  if ( O0i1II1Iiii1I11 [ len ( O0i1II1Iiii1I11 ) - 1 ] == '/' ) :
   O0i1II1Iiii1I11 = O0i1II1Iiii1I11 [ 0 : len ( O0i1II1Iiii1I11 ) - 2 ]
  iiIiI = IIII . split ( '&' )
  ooOOoooooo = { }
  for o00oooO0Oo in range ( len ( iiIiI ) ) :
   o0O0OOO0Ooo = { }
   o0O0OOO0Ooo = iiIiI [ o00oooO0Oo ] . split ( '=' )
   if ( len ( o0O0OOO0Ooo ) ) == 2 :
    ooOOoooooo [ o0O0OOO0Ooo [ 0 ] ] = o0O0OOO0Ooo [ 1 ]
    if 45 - 45: O0 / o0oOOo0O0Ooo
 return ooOOoooooo
 if 32 - 32: i1II1I11 . i1I . i1I
 if 62 - 62: I1ii11iIi11i + i1I % i1II1I11 + OOooOOo
O0i1II1Iiii1I11 = i1iIi ( )
o0OOoo0OO0OOO = None
i1iIi1iIi1i = None
iii = None
oOooOOOoOo = None
i1Iii1i1I = None
OOoO00 = None
IiI111111IIII = None
if 37 - 37: OO0o / OoOoOO00
if 23 - 23: O0
try :
 IiI111111IIII = int ( O0i1II1Iiii1I11 [ "fav_mode" ] )
except :
 pass
 if 85 - 85: Ii1I
try :
 o0OOoo0OO0OOO = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "url" ] )
except :
 pass
try :
 i1iIi1iIi1i = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "name" ] )
except :
 pass
try :
 oOooOOOoOo = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "iconimage" ] )
except :
 pass
try :
 iii = int ( O0i1II1Iiii1I11 [ "mode" ] )
except :
 pass
try :
 i1Iii1i1I = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "fanart" ] )
except :
 pass
try :
 OOoO00 = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "description" ] )
except :
 pass
 if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
 if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + i1II1I11 / OoOoOO00
print str ( oooOOOOO ) + ': ' + str ( oOo0oooo00o )
print "Mode: " + str ( iii )
print "URL: " + str ( o0OOoo0OO0OOO )
print "Name: " + str ( i1iIi1iIi1i )
print "IconImage: " + str ( oOooOOOoOo )
if 84 - 84: oo * II111iiii + Oo0Ooo
if 53 - 53: i1II1I11 % II111iiii . i1I - iIii1I11I1II1 - i1I * II111iiii
def ooO0oOOooOo0 ( content , viewType ) :
 if 38 - 38: OO0o
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 84 - 84: iIii1I11I1II1 % i1II1I11 / iIii1I11I1II1 % I11i
  if 45 - 45: O0
if iii == None : oo0Oo00Oo0 ( )
elif iii == 11 : xbmc . executebuiltin ( "XBMC.RunScript(" + oO + ")" )
elif iii == 12 : oOOO00o ( )
elif iii == 13 : oo0OooOOo0 ( )
elif iii == 14 : iIIIIii1 ( i1iIi1iIi1i )
elif iii == 15 : OOoo0O ( o0OOoo0OO0OOO )
elif iii == 16 : I1i1I ( )
elif iii == 17 : iii11I111 ( i1iIi1iIi1i )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
