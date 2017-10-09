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
import extract
import downloader
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from datetime import date , datetime , timedelta
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
IiII1IiiIiI1 = 'plugin.video.GenieXXX'
iIiiiI1IiI1I1 = 'plugin.video.GenieXXX'
o0OoOoOO00 = "0.0.1"
I11i = xbmc . translatePath ( 'special://home/addons/' )
O0O = base64 . decodestring
Oo = datetime . now ( )
I1ii11iIi11i = xbmc . translatePath ( 'special://logpath/' )
I1IiI = xbmc . translatePath ( 'special://home/addonsbroke/' )
o0OOO = xbmcaddon . Addon ( id = iIiiiI1IiI1I1 )
iIiiiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
Iii1ii1II11i = 'plugin.video.GenieXXX'
iI111iI = xbmcgui . DialogProgress ( )
IiII = "Genie XXX"
iI1Ii11111iIi = Net ( )
i1i1II = xbmc . translatePath ( 'special://home/' )
O0O = base64 . decodestring
O0oo0OO0 = xbmc . translatePath ( 'special://profile/' )
I1i1iiI1 = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
iiIIIII1i1iI = os . path . join ( i1i1II , 'userdata' )
o0oO0 = os . path . join ( iiIIIII1i1iI , 'addon_data' , IiII1IiiIiI1 )
oo00 = os . path . join ( I11i , 'packages' )
o00 = os . path . join ( o0oO0 , 'wizard.log' )
Oo0oO0ooo = o0OOO . getSetting ( 'AdultPass' )
o0oOoO00o = ( O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsveHh4Lw==' ) )
i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'icon.png' ) )
oOOoo00O0O = o0oOoO00o + ( O0O ( 'YXJ0Lw==' ) )
i1111 = o0oOoO00o + ( O0O ( 'cmVzZWwvd2l6LnhtbA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
i11 = ( O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
I11 = ( O0O ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwLw==' ) )
Oo0o0000o0o0 = 'WEBSITE'
oOo0oooo00o = ( O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieXXX' )
oo0o0O00 = xbmc . translatePath ( 'special://thumbnails' ) ;
oO = "Reseller"
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'fanart.jpg' ) )
oooOOOOO = o0OOO . getLocalizedString
i1iiIII111ii = CookieJar ( )
i1iIIi1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( i1iiIII111ii ) )
i1iIIi1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
ii11iIi1I = int ( sys . argv [ 1 ] )
iI111I11I1I1 = xbmc . translatePath ( o0OOO . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iiIIIII1i1iI = xbmc . translatePath ( 'special://home/userdata/' )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
iIii1 = oO0o0o0ooO0oO + '/addons.ini'
oOOoO0 = xbmcgui . Dialog ( )
O0OoO000O0OO = xbmcgui . Dialog ( )
if os . path . exists ( OOooO0OOoo ) == True :
 iiI1IiI = open ( OOooO0OOoo ) . read ( )
else : iiI1IiI = [ ]
if 13 - 13: II . iii1I1 . iI % o0O00oooo
if 67 - 67: OO0o / oo % oo0Oo00Oo0 % oOOO00o
if 97 - 97: o0o0OOO0o0 % IIII % o0O0 . o0
def I11II1i ( ) :
 IIIII ( )
 if Oo0oO0ooo == 'wanker' :
  ooooooO0oo ( '[COLORorangered]Search[/COLOR]' , '' , 10107 , oOOoo00O0O + 'search.png' , '' , '' , )
  ooooooO0oo ( '[COLORorangered]Best Videos[/COLOR]' , 'http://www.xvideos.com/best' , 10105 , oOOoo00O0O + 'best_videos.png' , '' , '' )
  ooooooO0oo ( '[COLORorangered]Recently Uploaded[/COLOR]' , 'http://xvideos.com' , 10105 , oOOoo00O0O + 'recently_uploaded.png' , '' , '' )
  ooooooO0oo ( '[COLORorangered]100% Verified[/COLOR]' , 'http://www.xvideos.com/verified/videos' , 10105 , oOOoo00O0O + '100_percent_verified.png' , '' , '' )
  ooooooO0oo ( '[COLORorangered]Tags[/COLOR]' , 'http://www.xvideos.com/tags' , 10103 , oOOoo00O0O + 'tags.png' , '' , '' )
  ooooooO0oo ( '[COLORorangered]In Your Language[/COLOR]' , 'http://www.xvideos.com/porn' , 101001 , oOOoo00O0O + 'language.png' , '' , '' )
  ooooooO0oo ( '[COLORorangered]Adult Image Galleries[/COLOR]' , '' , 9999999 , oOOoo00O0O + 'galleries.png' , i1iiIIiiI111 , '' )
 else :
  oOOoO0 . ok ( '[COLORorangered]Genietvmedia@gmail.com[/COLOR]' , 'HOLD THE TISSUES[CR]' , 'Seems You Are Up To No Good Without Permission[CR]' , '[COLORorangered]Contact GenieTv For A Pass[/COLOR]' )
def IIIII ( ) :
 if Oo0oO0ooo == 'insert_password' :
  oOOoO0 . ok ( '[COLORorangered]Genietvmedia@gmail[/COLOR]' , 'You need to set the password to access this[CR]' , 'This is only given to dirty fuckers aged 18+' , ' @ [COLORorangered]Genie XXX Media[/COLOR]' )
  o0OOO . openSettings ( sys . argv [ 0 ] )
def IIiiiiiiIi1I1 ( ) :
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 I11II1i ( )
 if 13 - 13: OOoo0O0 + Ii + II - iIii1I11I1II1 * oo0Oo00Oo0 % IIII
 if 23 - 23: iI + Ii * oo0Oo00Oo0 / oo0Oo00Oo0
def OoOo ( ) :
 ooooooO0oo ( '[COLORorangered]Search[/COLOR]' , '' , 10107 , i1 , '' , '' , )
 ooooooO0oo ( '[COLORorangered]Best Videos[/COLOR]' , 'http://www.xvideos.com/best' , 10105 , i1 , '' , '' )
 ooooooO0oo ( '[COLORorangered]Recently Uploaded[/COLOR]' , 'http://xvideos.com' , 10105 , i1 , '' , '' )
 ooooooO0oo ( '[COLORorangered]100% Verified[/COLOR]' , 'http://www.xvideos.com/verified/videos' , 10105 , i1 , '' , '' )
 ooooooO0oo ( '[COLORorangered]Tags[/COLOR]' , 'http://www.xvideos.com/tags' , 10103 , i1 , '' , '' )
 ooooooO0oo ( '[COLORorangered]In Your Language[/COLOR]' , 'http://www.xvideos.com/porn' , 101001 , i1 , '' , '' )
 if 18 - 18: i11iIiiIii
def Ii11I ( ) :
 OOO0OOO00oo = [ '[COLORorangered]Adult Gallery[/COLOR]' , '[COLORorangered]JizBox[/COLOR]' , '[COLORorangered]Adult Channels[/COLOR]' ]
 Iii111II = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , OOO0OOO00oo )
 if Iii111II == 0 :
  iiii11I ( )
 if Iii111II == 1 :
  Ooo0OO0oOO ( )
 if Iii111II == 2 :
  ARCONAI4 ( )
  if 50 - 50: II
  if 34 - 34: II * II111iiii % o0O0 * o0O00oooo - II
  if 33 - 33: OO0o + oOOO00o * iI - iii1I1 / oo0Oo00Oo0 % IIII
def iiii11I ( ) :
 OOO0OOO00oo = [ '[COLORorangered]YOLOselfies[/COLOR]' , '[COLORorangered]HotNudeGirls[/COLOR]' , '[COLORorangered]MyNudeBabes[/COLOR]' , '[COLORorangered]TeenNudeGirls[/COLOR]' , '[COLORorangered]ADULTmeme[/COLOR]' , '[COLORorangered]GIRLSmeme[/COLOR]' , ]
 Iii111II = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , OOO0OOO00oo )
 if Iii111II == 0 :
  II1i1IiiIIi11 ( 'http://www.yoloselfie.com/' )
 if Iii111II == 1 :
  iI1Ii11iII1 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if Iii111II == 2 :
  Oo0O0O0ooO0O ( 'http://www.teennudegirls.com/' )
 if Iii111II == 3 :
  Oo0O0O0ooO0O ( 'http://www.teennudegirls.com/' )
 if Iii111II == 4 :
  IIIIii ( 'http://jokideo.com/category/funny-dirty-rude-jokes/' )
 if Iii111II == 5 :
  IIIIii ( 'http://jokideo.com/category/hot-and-sexy/' )
  if 70 - 70: IIII / o0o0OOO0o0 . o0O0 % iii1I1
def II1i1IiiIIi11 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 iI1ii1Ii = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( '[COLORorangered]' + oooo000 + '[/COLOR]' , url , 100111 , iIIIi1 )
 for url in iI1ii1Ii :
  iiII1i1 ( '[COLORorangered]NEXT[/COLOR]' , url , 100110 , iIIIi1 )
def o00oOO0o ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  OOO00O = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( OOO00O )
  sys . exit ( 1 )
def IIIIii ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 iI1ii1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for oooo000 , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( ( '[COLORorangered]' + oooo000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + iIIIi1 , 100113 , 'http:' + iIIIi1 )
 for url in iI1ii1Ii :
  iiII1i1 ( '[COLORorangered]NEXT[/COLOR]' , 'http:' + url , 100112 , iIIIi1 )
def iI1Ii11iII1 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( ( '[COLORorangered]' + oooo000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , iIIIi1 )
def OOoOO0oo0ooO ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 iI1ii1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( '[COLORorangered]Click To Enlarge[/COLOR]' , iIIIi1 , 100113 , iIIIi1 )
def O0o0O00Oo0o0 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( ( '[COLORorangered]' + oooo000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , iIIIi1 )
def O00O0oOO00O00 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 iI1ii1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( '[COLORorangered]Click To Enlarge[/COLOR]' , iIIIi1 , 100113 , iIIIi1 )
def Oo0O0O0ooO0O ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( ( '[COLORorangered]' + oooo000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , iIIIi1 )
def i1Oo00 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 iI1ii1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , iIIIi1 in I11IiI1I11i1i :
  iiII1i1 ( '[COLORorangered]Click To Enlarge[/COLOR]' , iIIIi1 , 100113 , iIIIi1 )
def i1i ( url ) :
 OOO00O = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( OOO00O )
 sys . exit ( 1 )
 if 50 - 50: o0
 if 14 - 14: o0o0OOO0o0 % iI * o0o0OOO0o0
def Ooo0OO0oOO ( ) :
 OOO0OOO00oo = [ '[COLORorangered]XXX Vids[/COLOR]' , '[COLORorangered]Perfect Girls[/COLOR]' , '[COLORorangered]Best Videos[/COLOR]' , '[COLORorangered]Genres[/COLOR]' , '[COLORorangered]Recently Uploaded[/COLOR]' , '[COLORorangered]100% Verified[/COLOR]' , '[COLORorangered]Tags[/COLOR]' , '[COLORorangered]In Your Language[/COLOR]' , '[COLORorangered]Search[/COLOR]' ]
 Iii111II = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , OOO0OOO00oo )
 if Iii111II == 0 :
  iII ( 'http://watchxxxfree.com/categories' )
 if Iii111II == 1 :
  oO00o0 ( 'http://www.perfectgirls.net' )
 if Iii111II == 2 :
  OOoo0O ( 'http://www.xvideos.com/best' )
 if Iii111II == 3 :
  Oo0ooOo0o ( 'http://www.xvideos.com/best' )
 if Iii111II == 4 :
  OOoo0O ( 'http://www.xvideos.com/best' )
 if Iii111II == 5 :
  OOoo0O ( 'http://www.xvideos.com/verified/videos' )
 if Iii111II == 6 :
  Ii1i1 ( 'http://www.xvideos.com/tags' )
 if Iii111II == 7 :
  iiIii ( 'http://www.xvideos.com/porn' )
 if Iii111II == 8 :
  ooo0O ( )
  if 75 - 75: OO0o % OO0o . OOoo0O0
  if 5 - 5: OO0o * Ii + o0O00oooo . oOOO00o + o0O00oooo
  if 91 - 91: O0
  if 61 - 61: II111iiii
  if 64 - 64: Ii / o0O00oooo - O0 - o0o0OOO0o0
  if 86 - 86: o0o0OOO0o0 % o0O00oooo / II / o0O00oooo
  if 42 - 42: iI
  if 67 - 67: OOoo0O0 . o0O0 . O0
  if 10 - 10: oo % oo - iIii1I11I1II1 / oOOO00o + IIII
def OOOOoOoo0O0O0 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 in I11IiI1I11i1i :
  if 'ch' in url :
   ooooooO0oo ( '[COLORorangered]' + oooo000 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , i1 , i1 , '' )
def OOOo00oo0oO ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 IIiIi1iI = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 in I11IiI1I11i1i :
  addDir2 ( ( '[COLORorangered]' + oooo000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , i1 , '' , '' )
 for oooo000 , url in IIiIi1iI :
  i1IiiiI1iI ( '[COLORorangered]' + oooo000 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOoo00O0O + 'Next.png' , '' , '' )
def i1iIi ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  if 'jetload' in url :
   ooOOoooooo ( url )
def II1I ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'file: "([^"]*)",' ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  RESOLVEtest ( url )
def iII ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for iIIIi1 , url , oooo000 , O0i1II1Iiii1I11 in I11IiI1I11i1i :
  if 'category' in url :
   ooooooO0oo ( '[COLORorangered]' + oooo000 + '[COLORorange]   ' + O0i1II1Iiii1I11 + '[/COLOR]' , url , 90006 , iIIIi1 , i1 , '' )
def IIIIiiIiI ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 IIiIi1iI = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( OOoOO00OOO0OO )
 for iIIIi1 , url , oooo000 in I11IiI1I11i1i :
  addDir2 ( ( '[COLORorangered]' + oooo000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , iIIIi1 , '' , '' )
 for url in IIiIi1iI :
  i1IiiiI1iI ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOoo00O0O + 'Next.png' , '' , '' )
def o00oooO0Oo ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  if 'jetload' in url :
   ooOOoooooo ( url )
def ooOOoooooo ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'file: "([^"]*)",' ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  RESOLVEtest ( url )
def oO00o0 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , O0i1II1Iiii1I11 in I11IiI1I11i1i :
  if 'category' in url :
   ooooooO0oo ( '[COLORorangered]' + oooo000 + '[COLORorange]' + O0i1II1Iiii1I11 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , i1 , '' , '' )
def o0O0OOO0Ooo ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 iiIiI = url
 I11IiI1I11i1i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 IIiIi1iI = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , iIIIi1 in I11IiI1I11i1i :
  addDir2 ( '[COLORorangered]' + oooo000 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , iIIIi1 , '' , '' )
 for url in IIiIi1iI :
  i1IiiiI1iI ( '[COLORred]NEXT[/COLOR]' , iiIiI + '/' + url , 90003 , oOOoo00O0O + 'Next.png' , '' , '' )
def I1 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'get\("(.*)", function' ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  OOO00O0O ( 'http://www.perfectgirls.net' + url )
def OOO00O0O ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( 'http://(.+?)\n' ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  iii ( 'http://' + url )
def iiIii ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , O0i1II1Iiii1I11 in I11IiI1I11i1i :
  ooooooO0oo ( '[COLORorangered]' + oooo000 + '[COLORgreen] - No of Videos : [COLORorange]' + O0i1II1Iiii1I11 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
def Ii1i1 ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 IIiIi1iI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( OOoOO00OOO0OO )
 for url in IIiIi1iI :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , i1 , '' , '' )
 I11IiI1I11i1i = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( OOoOO00OOO0OO )
 for url , oooo000 , O0i1II1Iiii1I11 in I11IiI1I11i1i :
  ooooooO0oo ( ( '[COLORorangered]' + oooo000 + '[COLORgreen] - No of Videos : [COLORorange]' + ( O0i1II1Iiii1I11 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
  if 90 - 90: OO0o % i1IIi / iI
def IIi ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 IIiIi1iI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OOoOO00OOO0OO )
 for url in IIiIi1iI :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoo00O0O + 'Next.png' , '' , '' )
 I11IiI1I11i1i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for iIIIi1 , url , oooo000 , i1Iii1i1I in I11IiI1I11i1i :
  ooooooO0oo ( oooo000 + '--' + ( i1Iii1i1I ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iIIIi1 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 91 - 91: oo + II . oOOO00o * oo + II * iii1I1
  if 80 - 80: o0O0 % oOOO00o % oo0Oo00Oo0 - iii1I1 + iii1I1
def OOoo0O ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for iIIIi1 , url , oooo000 , iIiii1i111iI1 , i11oO0oOo0 in I11IiI1I11i1i :
  ooooooO0oo ( '[COLORorangered]' + oooo000 + '[COLORgreen] - Porn Quality : [COLORorange]' + i11oO0oOo0 + ' - [COLORred]' + iIiii1i111iI1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iIIIi1 , iIIIi1 , i11oO0oOo0 + ' - ' + iIiii1i111iI1 )
 I1I1I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OOoOO00OOO0OO )
 for url in I1I1I :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoo00O0O + 'Next.png' , '' , '' )
  if 95 - 95: II111iiii + OO0o + o0O0 * iIii1I11I1II1 % oo0Oo00Oo0 / o0
def Oo0ooOo0o ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 o0o0o0oO0oOO = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 IIiIi1iI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( OOoOO00OOO0OO )
 for url in IIiIi1iI :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoo00O0O + 'Next.png' , '' , '' )
 I11IiI1I11i1i = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( o0o0o0oO0oOO ) )
 for url , oooo000 in I11IiI1I11i1i :
  if '/c/' in url :
   ooooooO0oo ( '[COLORorangered]' + oooo000 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
   if 3 - 3: OO0o
   if 24 - 24: i11iIiiIii + o0O0 * IIII - II111iiii . oOOO00o % iIii1I11I1II1
def ooo0O ( ) :
 ooI1IiiiiI = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0O = ( ooI1IiiiiI ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IiIIii1iII1II = o0O . lower ( )
 Iii1I1I11iiI1 = 'http://www.xvideos.com/?k=' + IiIIii1iII1II
 print Iii1I1I11iiI1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OOoOO00OOO0OO = iI1I111Ii111i ( Iii1I1I11iiI1 )
 I11IiI1I11i1i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( OOoOO00OOO0OO )
 for iIIIi1 , I1I1i1I , oooo000 , iIiii1i111iI1 , i11oO0oOo0 in I11IiI1I11i1i :
  ooooooO0oo ( '[COLORorangered]' + oooo000 + '[COLORgreen] - Porn Quality : [COLORorange]' + i11oO0oOo0 + ' - [COLORred]' + iIiii1i111iI1 + '[/COLOR]' , 'http://www.xvideos.com' + I1I1i1I , 10108 , iIIIi1 , iIIIi1 , i11oO0oOo0 + ' - ' + iIiii1i111iI1 )
 I1I1I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OOoOO00OOO0OO )
 for I1I1i1I in I1I1I :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + I1I1i1I , 10105 , oOOoo00O0O + 'Next.png' , '' , '' )
if 30 - 30: OoooooooOO
if 5 - 5: Ii - II111iiii - OoooooooOO % IIII + II * iIii1I11I1II1
if 37 - 37: o0 % Ii + o0O00oooo + OO0o * o0o0OOO0o0 % O0
if 61 - 61: II - oOOO00o . oo0Oo00Oo0 / oOOO00o + iii1I1
if 5 - 5: Ii + Ii / O0 * iii1I1 - oOOO00o % Ii
if 15 - 15: i11iIiiIii % IIII . iii1I1 + oo
if 61 - 61: iii1I1 * oo % iii1I1 - i1IIi - iIii1I11I1II1
if 74 - 74: oo + II111iiii / iI
if 100 - 100: o0O00oooo * iIii1I11I1II1
if 86 - 86: iI * oOOO00o . o0O0
if 32 - 32: OO0o . o0 * o0o0OOO0o0
if 93 - 93: OO0o % i1IIi . IIII . i11iIiiIii
if 56 - 56: oo % O0 - II
if 100 - 100: IIII - O0 % oo0Oo00Oo0 * oOOO00o + II
if 88 - 88: OoooooooOO - iI * O0 * OoooooooOO . OoooooooOO
if 33 - 33: OOoo0O0 + o0O0 * oo0Oo00Oo0 / iIii1I11I1II1 - II
if 54 - 54: OOoo0O0 / oOOO00o . oo0Oo00Oo0 % o0O0
if 57 - 57: i11iIiiIii . oo - IIII - oo0Oo00Oo0 + o0O00oooo
if 63 - 63: o0O00oooo * o0O0
if 69 - 69: O0 . iI
if 49 - 49: II - o0o0OOO0o0
if 74 - 74: iIii1I11I1II1 * oo + o0O00oooo / i1IIi / II111iiii . iii1I1
if 62 - 62: OoooooooOO * II
if 58 - 58: o0O00oooo % OO0o
if 50 - 50: OOoo0O0 . OO0o
if 97 - 97: O0 + o0O00oooo
if 89 - 89: OO0o + iI * o0o0OOO0o0 * IIII
if 37 - 37: OoooooooOO - O0 - OO0o
if 77 - 77: oOOO00o * iIii1I11I1II1
if 98 - 98: II % IIII * OoooooooOO
if 51 - 51: iIii1I11I1II1 . o0O00oooo / oo0Oo00Oo0 + OO0o
if 33 - 33: Ii . II111iiii % o0O0 + OO0o
if 71 - 71: iii1I1 % oOOO00o
if 98 - 98: o0o0OOO0o0 % i11iIiiIii % Ii + IIII
if 78 - 78: oo % oo0Oo00Oo0 / o0O0 - iIii1I11I1II1
def ooooo0O0000oo ( url ) :
 OOoOO00OOO0OO = iI1I111Ii111i ( url )
 I11IiI1I11i1i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( OOoOO00OOO0OO )
 iI1ii1Ii = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( OOoOO00OOO0OO )
 iIii1II11 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( OOoOO00OOO0OO )
 for url in I11IiI1I11i1i :
  if 'http' in url :
   OooOo0ooo ( '[COLORorangered]Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , i1 )
 for url in iI1ii1Ii :
  if 'http' in url :
   OooOo0ooo ( '[COLORorangered]Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , i1 )
 for url in iIii1II11 :
  if 'http' in url :
   OooOo0ooo ( '[COLORorangered]Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , i1 )
   if 71 - 71: OOoo0O0 + IIII
def iI1111ii1I ( url ) :
 iiI11iI = xbmc . Player ( oOOoO0o0oO ( ) )
 import urlresolver
 try : iiI11iI . play ( url )
 except : pass
 if 93 - 93: o0 * OoooooooOO + Ii
def IiII111i1i11 ( title , message , times = 2000 , icon = i1 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def i111iIi1i1II1 ( ) :
 oooO = i1I1i111Ii ( )
 ooo = oooO . replace ( I1ii11iIi11i , "" )
 if os . path . exists ( oooO ) or not oooO == False :
  i1i1iI1iiiI = open ( oooO , mode = 'r' ) ; Ooo0oOooo0 = i1i1iI1iiiI . read ( ) ; i1i1iI1iiiI . close ( )
  oOOOoo00 ( "%s - %s" % ( IiII , ooo ) , Ooo0oOooo0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def i1I1i111Ii ( ) :
 iiIiIIIiiI = False
 if os . path . exists ( os . path . join ( I1ii11iIi11i , 'xbmc.log' ) ) :
  iiIiIIIiiI = os . path . join ( I1ii11iIi11i , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'kodi.log' ) ) :
  iiIiIIIiiI = os . path . join ( I1ii11iIi11i , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'spmc.log' ) ) :
  iiIiIIIiiI = os . path . join ( I1ii11iIi11i , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'tvmc.log' ) ) :
  iiIiIIIiiI = os . path . join ( I1ii11iIi11i , 'tvmc.log' )
 return iiIiIIIiiI
 if 12 - 12: O0 - OO0o
 if 81 - 81: o0O00oooo - o0O00oooo . o0O0
 if 73 - 73: o0o0OOO0o0 % i11iIiiIii - II
 if 7 - 7: O0 * i11iIiiIii * IIII + Ii % iI - Ii
 if 39 - 39: iii1I1 * oOOO00o % oOOO00o - OoooooooOO + OO0o - o0o0OOO0o0
def oOOOoo00 ( heading , announce ) :
 class ii ( ) :
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
   try : i1i1iI1iiiI = open ( announce ) ; O0oOo00o = i1i1iI1iiiI . read ( )
   except : O0oOo00o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0oOo00o ) )
   return
 ii ( )
 ii ( )
 if 81 - 81: o0 % i1IIi . iIii1I11I1II1
def Ii1Iii1iIi ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 OO0oo = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + U + '%26password%3D' + Pass + '%26type%3Dm3u_plus%26output%3Dts'
 Iii1 = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + U + '%26password%3D' + Pass
 OOO0000oO = 'http://piesustv.net:8000/enigma2.php?username=' + U + '&password=' + Pass + '&type=get_vod_categories'
 OOO0000oO = iI1I111Ii111i ( OOO0000oO )
 if not OOO0000oO == "" :
  iI1i111I1Ii = 'https://tinyurl.com/create.php?source=indexpage&url=' + OO0oo + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( iI1i111I1Ii ) )
  i11i1ii1I = 'https://tinyurl.com/create.php?source=indexpage&url=' + Iii1 + '&submit=Make+TinyURL%21&alias='
  OO0oo = iI1I111Ii111i ( iI1i111I1Ii )
  Iii1 = iI1I111Ii111i ( i11i1ii1I )
  xbmc . log ( str ( Iii1 ) )
  o0OO0o0o00o = regex_from_to ( OO0oo , '<div class="indent"><b>' , '</b>' )
  oOo0 = regex_from_to ( Iii1 , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLORorangered]WaveTv[/COLOR]' , '[COLORorangered]PLAYLIST URL: [/COLOR]%s' % o0OO0o0o00o , '' , '[COLORorangered]EPG URL: [/COLOR]%s' % oOo0 )
 else :
  return
def OOOoOO ( ) :
 i1IiiiI1iI ( '[COLORorangered]Setup Tv Guide[/COLOR]' , '' , 212 , oOOoo00O0O + '12.png' , i1iiIIiiI111 , '' )
 i1IiiiI1iI ( '[COLORorangered]Open Guide[/COLOR]' , '' , 213 , oOOoo00O0O + '13.png' , i1iiIIiiI111 , '' )
 if 10 - 10: o0O0 + iii1I1 * oo + iIii1I11I1II1 / OOoo0O0 / oo
def iI1II ( ) :
 ivuesetup . iVueInt ( )
 if 69 - 69: Ii % oo0Oo00Oo0
def ii1I1IIii11 ( ) :
 O0o0oO ( )
 return
 if 38 - 38: oo0Oo00Oo0 % o0O00oooo + oo . i11iIiiIii
def O0o0oO ( ) :
 if 53 - 53: i11iIiiIii * o0O0
 OooooO0oOOOO = xbmcaddon . Addon ( 'plugin.video.WaveTv' )
 o0O00oOOoo = OooooO0oOOOO . getSetting ( id = 'User' )
 i1I1iIi = OooooO0oOOOO . getSetting ( id = 'Pass' )
 IIii11Ii1i1I = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 Oooo0O = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 oo00O0oO0O0 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 ooo0OO0O0Oo = "http://piesustv.net:8000/get.php?username=" + o0O00oOOoo + "&password=" + i1I1iIi + "&type=m3u_plus&output=ts"
 Ooo0O0oooo = "http://piesustv.net:8000/xmltv.php?username=" + o0O00oOOoo + "&password=" + i1I1iIi + "&type=m3u_plus&output=ts"
 if 36 - 36: OoooooooOO . iI
 xbmc . executeJSONRPC ( IIii11Ii1i1I )
 xbmc . executeJSONRPC ( Oooo0O )
 xbmc . executeJSONRPC ( oo00O0oO0O0 )
 if 56 - 56: iii1I1 . oo . II
 ii111I = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 ii111I . setSetting ( id = 'm3uUrl' , value = ooo0OO0O0Oo )
 ii111I . setSetting ( id = 'epgUrl' , value = Ooo0O0oooo )
 ii111I . setSetting ( id = 'm3uCache' , value = "false" )
 ii111I . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def iiI ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 if 7 - 7: o0O00oooo + II111iiii . i1IIi
 if 63 - 63: iIii1I11I1II1 / OOoo0O0 / oo0Oo00Oo0 / o0O0
 if 33 - 33: o0 % iIii1I11I1II1 * II
def o00o0 ( ) :
 i1IiiiI1iI ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 i1IiiiI1iI ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 i1IiiiI1iI ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 i1IiiiI1iI ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 i1IiiiI1iI ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 if 50 - 50: iii1I1 / iii1I1 % oo . oo
 if 55 - 55: Ii - o0o0OOO0o0 + II111iiii + o0O0 % IIII
 if 41 - 41: i1IIi - o0o0OOO0o0 - IIII
def III11I1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def IIi1IIIi ( url ) :
 if url == 'http://' : return False
 try :
  O00Ooo = urllib2 . Request ( url )
  O00Ooo . add_header ( 'User-Agent' , iIiiiI )
  OOOO0OOO = urllib2 . urlopen ( O00Ooo )
  OOOO0OOO . close ( )
 except Exception , i1i1ii :
  return i1i1ii
 return True
 if 46 - 46: o0O00oooo + iI
 if 70 - 70: o0O0 / iIii1I11I1II1
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / oo
def ooOOoO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "Genie XXX" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Genie XXX[/COLOR]" )
 return
 if 20 - 20: o0o0OOO0o0 + IIII / O0 % iIii1I11I1II1
def oOo0O ( url ) :
 print '###' + IiII + ' - DELETING Addons20.db ###'
 OOO0O00oO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 iiiOoOoO0O = os . path . join ( OOO0O00oO , 'Addons20.db' )
 try :
  os . remove ( iiiOoOoO0O )
  O0OoO000O0OO = xbmcgui . Dialog ( )
  print '=== ' + IiII + ' - DELETING    ' + str ( iiiOoOoO0O ) + '    ==='
  O0OoO000O0OO . ok ( IiII , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( IiII , "       No File To Remove" )
 return
 if 100 - 100: iIii1I11I1II1 + o0O00oooo / iii1I1 . i11iIiiIii
 if 14 - 14: OO0o * oOOO00o + o0O0 + O0 + i11iIiiIii
 if 77 - 77: OO0o / OoooooooOO
 if 46 - 46: OO0o % iIii1I11I1II1 . o0O0 % o0O0 + i11iIiiIii
 if 72 - 72: iIii1I11I1II1 * IIII % Ii / iI
def iI1I111Ii111i ( url ) :
 O00Ooo = urllib2 . Request ( url )
 O00Ooo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOOO0OOO = urllib2 . urlopen ( O00Ooo )
 I11i1II = OOOO0OOO . read ( )
 OOOO0OOO . close ( )
 return I11i1II
def oOOOoo00 ( heading , announce ) :
 class ii ( ) :
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
   try : i1i1iI1iiiI = open ( announce ) ; O0oOo00o = i1i1iI1iiiI . read ( )
   except : O0oOo00o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0oOo00o ) )
   return
 ii ( )
 ii ( )
def Ooo ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 iiIi1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i11111i1i11 , OOoOOO0 , I1I1i in os . walk ( iiIi1i ) :
   I1IIIiIiIi = 0
   I1IIIiIiIi += len ( I1I1i )
   if 27 - 27: oo + o0O00oooo - oOOO00o + O0 . IIII
   if 46 - 46: o0
   if I1IIIiIiIi > 0 :
    if 45 - 45: Ii
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( I1IIIiIiIi ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: oo0Oo00Oo0 . OOoo0O0 . oOOO00o / iii1I1 / OOoo0O0
     for i1i1iI1iiiI in I1I1i :
      os . unlink ( os . path . join ( I1i11111i1i11 , i1i1iI1iiiI ) )
     for i1iI1 in OOoOOO0 :
      shutil . rmtree ( os . path . join ( I1i11111i1i11 , i1iI1 ) )
     O0OoO000O0OO = xbmcgui . Dialog ( )
     O0OoO000O0OO . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    O0OoO000O0OO = xbmcgui . Dialog ( )
    O0OoO000O0OO . ok ( IiII , "       No Packages to DELETE" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( IiII , "Error Deleting Packages please visit The Support Group, Genie XXX on facebook" )
 ii1 ( url )
 return
def ii1 ( url ) :
 I1IiiI1ii1i = os . path . join ( O0oo0OO0 , 'addon_data' )
 O0o = [
 ( I1IiiI1ii1i ) ,
 ( o0oO0 ) ,
 ( os . path . join ( i1i1II , 'cache' ) ) ,
 ( os . path . join ( i1i1II , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( o0oO0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( o0oO0 , 'plugin.video.GenieXXX' , 'Images' ) ) ,
 ( os . path . join ( I1IiiI1ii1i , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1IiiI1ii1i , 'plugin.video.GenieXXX' , 'Images' ) ) ]
 if 54 - 54: oOOO00o
 IiI11ii1I = 0
 if 39 - 39: iIii1I11I1II1 / O0 / oo0Oo00Oo0 - IIII - o0O0 % oOOO00o
 for I1ii11Ii in O0o :
  if os . path . exists ( I1ii11Ii ) and not I1ii11Ii in [ o0oO0 , I1IiiI1ii1i ] :
   for I1i11111i1i11 , OOoOOO0 , I1I1i in os . walk ( I1ii11Ii ) :
    I1IIIiIiIi = 0
    I1IIIiIiIi += len ( I1I1i )
    if I1IIIiIiIi > 0 :
     for i1i1iI1iiiI in I1I1i :
      if not i1i1iI1iiiI in I1i1iiI1 :
       try :
        os . unlink ( os . path . join ( I1i11111i1i11 , i1i1iI1iiiI ) )
       except :
        pass
      else : oooO ( 'Ignore Log File: %s' % i1i1iI1iiiI )
     for i1iI1 in OOoOOO0 :
      try :
       shutil . rmtree ( os . path . join ( I1i11111i1i11 , i1iI1 ) )
       IiI11ii1I += 1
       oooO ( "[Success] cleared %s files from %s" % ( str ( I1IIIiIiIi ) , os . path . join ( I1ii11Ii , i1iI1 ) ) )
      except :
       oooO ( "[Failed] to wipe cache in: %s" % os . path . join ( I1ii11Ii , i1iI1 ) )
  else :
   for I1i11111i1i11 , OOoOOO0 , I1I1i in os . walk ( I1ii11Ii ) :
    for i1iI1 in OOoOOO0 :
     if 'cache' in i1iI1 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( I1i11111i1i11 , i1iI1 ) )
       IiI11ii1I += 1
       oooO ( "[Success] wiped %s " % os . path . join ( I1ii11Ii , i1iI1 ) )
      except :
       oooO ( "[Failed] to wipe cache in: %s" % os . path . join ( I1ii11Ii , i1iI1 ) )
       if 50 - 50: Ii - OOoo0O0 * o0 . oo
 IiII111i1i11 ( IiII , 'Clear Cache: Removed %s Files' % IiI11ii1I )
def I11iiiii1II ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 iiIi1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i11111i1i11 , OOoOOO0 , I1I1i in os . walk ( iiIi1i ) :
   I1IIIiIiIi = 0
   I1IIIiIiIi += len ( I1I1i )
   if 51 - 51: O0 % oo0Oo00Oo0 - II111iiii
   if 31 - 31: o0O0 / iii1I1 - o0O0 - oOOO00o
   if I1IIIiIiIi > 0 :
    if 7 - 7: o0O0 % O0 . o0O00oooo + II - o0o0OOO0o0
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( I1IIIiIiIi ) + " files found" , "Do you want to delete them?" ) :
     if 75 - 75: o0o0OOO0o0
     for i1i1iI1iiiI in I1I1i :
      os . unlink ( os . path . join ( I1i11111i1i11 , i1i1iI1iiiI ) )
     for i1iI1 in OOoOOO0 :
      shutil . rmtree ( os . path . join ( I1i11111i1i11 , i1iI1 ) )
     O0OoO000O0OO = xbmcgui . Dialog ( )
     O0OoO000O0OO . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    O0OoO000O0OO = xbmcgui . Dialog ( )
    O0OoO000O0OO . ok ( IiII , "       No Packages to DELETE" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( IiII , "Error Deleting Packages" )
 return
 if 71 - 71: Ii
def Ooo0o00o0o ( ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 Iii111II = O0OoO000O0OO . yesno ( 'Force Close Genie XXX' , 'You are about to close Genie XXX' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if Iii111II == 0 : return
 elif Iii111II == 1 : pass
 IiIIIIIi = III11I1 ( )
 oooO ( "Platform: " + str ( IiIIIIIi ) )
 os . _exit ( 1 )
 oooO ( "Force close failed!  Trying alternate methods." )
 if IiIIIIIi == 'osx' :
  oooO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IiIIIIIi == 'linux' :
  oooO ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IiIIIIIi == 'android' :
  oooO ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.Genie XXX' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.Genie XXX' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.Genie XXX());' )
  except : pass
  O0OoO000O0OO . ok ( IiII , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif IiIIIIIi == 'windows' :
  oooO ( "############ try windows force close #################" )
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
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  oooO ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  oooO ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 11 - 11: i1IIi % i11iIiiIii - i1IIi * o0O00oooo
def iii ( url ) :
 import urlresolver
 try :
  i1I11IiI1iiII = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( i1I11IiI1iiII , xbmcgui . ListItem ( oooo000 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( oooo000 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def III11I1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 91 - 91: Ii % Ii
def oooO ( log ) :
 xbmc . log ( "[%s]: %s" % ( IiII , log ) )
 if not os . path . exists ( o0oO0 ) : os . makedirs ( o0oO0 )
 if not os . path . exists ( o00 ) : i1i1iI1iiiI = open ( o00 , 'w' ) ; i1i1iI1iiiI . close ( )
 with open ( o00 , 'a' ) as i1i1iI1iiiI :
  i1iIiIIIII = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  i1i1iI1iiiI . write ( i1iIiIIIII . rstrip ( '\r\n' ) + '\n' )
  if 78 - 78: IIII * i1IIi
def oOOoO0o0oO ( ) :
 try :
  iI11 = getSet ( "core-player" )
  if ( iI11 == 'DVDPLAYER' ) : o00oOoOo0 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iI11 == 'MPLAYER' ) : o00oOoOo0 = xbmc . PLAYER_CORE_MPLAYER
  elif ( iI11 == 'PAPLAYER' ) : o00oOoOo0 = xbmc . PLAYER_CORE_PAPLAYER
  else : o00oOoOo0 = xbmc . PLAYER_CORE_AUTO
 except : o00oOoOo0 = xbmc . PLAYER_CORE_AUTO
 return o00oOoOo0
 return True
 if 72 - 72: OOoo0O0
 if 90 - 90: iii1I1 % O0 * iIii1I11I1II1 . o0O0
def ooooooO0oo ( name , url , mode , iconimage , fanart , description ) :
 if 8 - 8: Ii + II111iiii / o0O0 / o0o0OOO0o0
 ooo0OiII1iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iiiII = True
 ooOO0oO0oo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO0oO0oo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO0oO0oo00o . setProperty ( "Fanart_Image" , fanart )
 i11i1iiiII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0OiII1iii , listitem = ooOO0oO0oo00o , isFolder = True )
 return i11i1iiiII
 if 83 - 83: oo0Oo00Oo0 - II111iiii - o0O0
def i1IiiiI1iI ( name , url , mode , iconimage , fanart , description ) :
 if 3 - 3: OOoo0O0
 ooo0OiII1iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iiiII = True
 ooOO0oO0oo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO0oO0oo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO0oO0oo00o . setProperty ( "Fanart_Image" , fanart )
 i11i1iiiII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0OiII1iii , listitem = ooOO0oO0oo00o , isFolder = False )
 return i11i1iiiII
def iiII1i1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 ooo0OiII1iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i11i1iiiII = True
 ooOO0oO0oo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO0oO0oo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1iiIiI1Ii1i = [ ]
  i1iiIiI1Ii1i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   i1iiIiI1Ii1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI1IiI :
   i1iiIiI1Ii1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOO0oO0oo00o . addContextMenuItems ( i1iiIiI1Ii1i )
 i11i1iiiII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0OiII1iii , listitem = ooOO0oO0oo00o , isFolder = True )
 return i11i1iiiII
def OooOo0ooo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 ooo0OiII1iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i11i1iiiII = True
 ooOO0oO0oo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO0oO0oo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1iiIiI1Ii1i = [ ]
  i1iiIiI1Ii1i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   i1iiIiI1Ii1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI1IiI :
   i1iiIiI1Ii1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOO0oO0oo00o . addContextMenuItems ( i1iiIiI1Ii1i )
 i11i1iiiII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0OiII1iii , listitem = ooOO0oO0oo00o , isFolder = False )
 return i11i1iiiII
 if 22 - 22: o0 / i11iIiiIii
def oOOoo ( ) :
 iII1111III1I = [ ]
 ii11i = sys . argv [ 2 ]
 if len ( ii11i ) >= 2 :
  O00oOo00o0o = sys . argv [ 2 ]
  O00oO0 = O00oOo00o0o . replace ( '?' , '' )
  if ( O00oOo00o0o [ len ( O00oOo00o0o ) - 1 ] == '/' ) :
   O00oOo00o0o = O00oOo00o0o [ 0 : len ( O00oOo00o0o ) - 2 ]
  O0Oo00OoOo = O00oO0 . split ( '&' )
  iII1111III1I = { }
  for ii1ii111 in range ( len ( O0Oo00OoOo ) ) :
   i11111I1I = { }
   i11111I1I = O0Oo00OoOo [ ii1ii111 ] . split ( '=' )
   if ( len ( i11111I1I ) ) == 2 :
    iII1111III1I [ i11111I1I [ 0 ] ] = i11111I1I [ 1 ]
    if 11 - 11: OoooooooOO . OOoo0O0
 return iII1111III1I
 if 80 - 80: OoooooooOO - oOOO00o * IIII * oo / II / oOOO00o
 if 13 - 13: OOoo0O0 * Ii + i11iIiiIii * OOoo0O0 - Ii
O00oOo00o0o = oOOoo ( )
I1I1i1I = None
oooo000 = None
Ii1i1i1i1I1Ii = None
iiiI1 = None
OOOoO0O = None
o0iiiI1I1iIIIi1 = None
Iii = None
if 19 - 19: o0o0OOO0o0 % II111iiii / i11iIiiIii / o0O0 - OoooooooOO
if 37 - 37: oOOO00o / OoooooooOO - i11iIiiIii
try :
 Iii = int ( O00oOo00o0o [ "fav_mode" ] )
except :
 pass
 if 18 - 18: o0O0 . II
try :
 I1I1i1I = urllib . unquote_plus ( O00oOo00o0o [ "url" ] )
except :
 pass
try :
 oooo000 = urllib . unquote_plus ( O00oOo00o0o [ "name" ] )
except :
 pass
try :
 iiiI1 = urllib . unquote_plus ( O00oOo00o0o [ "iconimage" ] )
except :
 pass
try :
 Ii1i1i1i1I1Ii = int ( O00oOo00o0o [ "mode" ] )
except :
 pass
try :
 OOOoO0O = urllib . unquote_plus ( O00oOo00o0o [ "fanart" ] )
except :
 pass
try :
 o0iiiI1I1iIIIi1 = urllib . unquote_plus ( O00oOo00o0o [ "description" ] )
except :
 pass
 if 40 - 40: O0 - OoooooooOO - o0
 if 37 - 37: o0O00oooo / II111iiii / O0
print str ( oO ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( Ii1i1i1i1I1Ii )
print "URL: " + str ( I1I1i1I )
print "Name: " + str ( oooo000 )
print "IconImage: " + str ( iiiI1 )
if 76 - 76: II . Ii - oo - o0O0 * iI
if 54 - 54: o0 + O0 + o0o0OOO0o0 * OOoo0O0 - oOOO00o % oo0Oo00Oo0
def I111 ( content , viewType ) :
 if 13 - 13: iI * oo0Oo00Oo0 * o0O0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OOO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OOO . getSetting ( viewType ) )
  if 26 - 26: O0 * iii1I1 + II111iiii / o0 + oo0Oo00Oo0 % OO0o
  if 42 - 42: oo . OOoo0O0 % OOoo0O0
if Ii1i1i1i1I1Ii == None : I11II1i ( )
elif Ii1i1i1i1I1Ii == 1 : Genres ( )
elif Ii1i1i1i1I1Ii == 2 : Lists ( I1I1i1I , iiiI1 )
elif Ii1i1i1i1I1Ii == 3 : all_mov ( )
elif Ii1i1i1i1I1Ii == 4 : Search ( )
elif Ii1i1i1i1I1Ii == 5 : o00o0 ( )
elif Ii1i1i1i1I1Ii == 6 : I11iiiii1II ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 7 : ii1 ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 8 : Ooo0o00o0o ( )
elif Ii1i1i1i1I1Ii == 9 : OoOo ( )
elif Ii1i1i1i1I1Ii == 10 : MyAccDetails ( )
elif Ii1i1i1i1I1Ii == 11 : TvGuide ( )
elif Ii1i1i1i1I1Ii == 12 : IIIII ( )
elif Ii1i1i1i1I1Ii == 13 : ReCreate_Addon_ini ( )
elif Ii1i1i1i1I1Ii == 14 : Get_Ultimate_playlinks_data ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 144 : Get_List_playlinks ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 15 : iii ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 222 : iii ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 16 : Streams_Menu ( )
elif Ii1i1i1i1I1Ii == 17 : Live_Events ( oooo000 )
elif Ii1i1i1i1I1Ii == 18 : o0OOO . openSettings ( sys . argv [ 0 ] )
elif Ii1i1i1i1I1Ii == 19 : WIZ ( )
elif Ii1i1i1i1I1Ii == 20 : WIZARD ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 30 : CatchUp ( )
elif Ii1i1i1i1I1Ii == 31 : CatchUpPlay ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 40 : VOD_Menu ( )
elif Ii1i1i1i1I1Ii == 41 : Get_VOD_playlinks ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 21 : show_inf ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 22 : get_info ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 50 : RADIO ( )
elif Ii1i1i1i1I1Ii == 51 : RADIO2 ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 50000 : i111iIi1i1II1 ( )
elif Ii1i1i1i1I1Ii == 50001 : ooOOoO ( )
elif Ii1i1i1i1I1Ii == 50002 : oOo0O ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 60001 : apkmasterMenu ( )
elif Ii1i1i1i1I1Ii == 60002 : apkInstaller ( oooo000 , I1I1i1I )
elif Ii1i1i1i1I1Ii == 211 : OOOoOO ( )
elif Ii1i1i1i1I1Ii == 212 : ii1I1IIii11 ( )
elif Ii1i1i1i1I1Ii == 213 : iiI ( )
elif Ii1i1i1i1I1Ii == 214 : Ii1Iii1iIi ( )
elif Ii1i1i1i1I1Ii == 10100 : Ooo0OO0oOO ( )
elif Ii1i1i1i1I1Ii == 101001 : iiIii ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 10105 : OOoo0O ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 10106 : Oo0ooOo0o ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 10104 : IIi ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 10107 : ooo0O ( )
elif Ii1i1i1i1I1Ii == 10103 : Ii1i1 ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 10108 : ooooo0O0000oo ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 9999999 : iiii11I ( )
elif Ii1i1i1i1I1Ii == 19999999 : Ii11I ( )
elif Ii1i1i1i1I1Ii == 100110 : II1i1IiiIIi11 ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 100111 : o00oOO0o ( I1I1i1I )
elif Ii1i1i1i1I1Ii == 100112 : IIIIii ( I1I1i1I )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
