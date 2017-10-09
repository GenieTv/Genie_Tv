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
o0OoOoOO00 = "0.0.2"
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
 if Oo0oO0ooo == 'insert_password' :
  IIIII ( '[COLORorangered]It Seems Youre Not Logged In, Are You Over 18?[/COLOR]' , '' , 222 , oOOoo00O0O + 'search.png' , i1 , '' )
  IIIII ( '[COLORorangered]Yes I Am,,,, Honest[/COLOR]' , '' , 12 , i1 , i1 , '' )
  IIIII ( '[COLORorangered]No, I Am Just A Pup[/COLOR]' , '' , 100113 , i1 , i1 , '' )
  ooooooO0oo ( '[COLORsteelblue]Please Make A Selection And Flick Me To Enter[/COLOR]' , '' , 9 , i1 , i1 , '' )
 elif Oo0oO0ooo == 'dirtyfucker' :
  IIiiiiiiIi1I1 ( )
 else :
  oOOoO0 . ok ( '[COLORorangered]Genietvmedia@gmail.com[/COLOR]' , 'HOLD THE TISSUES' , 'Password Incorrect Please Reset Defaults' , '[COLORorangered]And Contact GenieTv For The Pass[/COLOR]' )
def I1IIIii ( ) :
 if Oo0oO0ooo == 'insert_password' :
  oOOoO0 . ok ( '[COLORorangered]Genietvmedia@gmail[/COLOR]' , 'You need to set the password to access this filth' , 'This is only given to dirty fuckers aged 18+' , ' @ [COLORorangered]GenieTv Media[/COLOR]' )
  o0OOO . openSettings ( sys . argv [ 0 ] )
 else :
  oOOoO0 . ok ( '[COLORorangered]Genietvmedia@gmail.com[/COLOR]' , 'HOLD THE TISSUES[CR]' , 'Seems You Are Up To No Good Without Permission[CR]' , '[COLORorangered]Contact GenieTv For The Pass[/COLOR]' )
def oOoOooOo0o0 ( ) :
 oOOoO0 . ok ( '[COLORorangered]Genietvmedia@gmail.com[/COLOR]' , 'HOLD THE TISSUES[CR]' , 'What We Recommend[CR]' , '[COLORorangered]http://us.cbeebies.com/[/COLOR]' )
def OOOO ( ) :
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 I11II1i ( )
 if 87 - 87: O0ooOooooO / i1I111II1I - oo0Oo00Oo0 - o0O0 * OoooooooOO . II
 if 75 - 75: iIii1I11I1II1 / oOOO00o % OO0o * o0O00oooo
def IIiiiiiiIi1I1 ( ) :
 if Oo0oO0ooo == 'dirtyfucker' :
  ooooooO0oo ( '[COLORorangered]Search[/COLOR]' , '' , 10107 , oOOoo00O0O + 'search.png' , i1 , '' , )
  ooooooO0oo ( '[COLORorangered]Best Videos[/COLOR]' , 'http://www.xvideos.com/best' , 10105 , oOOoo00O0O + 'best_videos.png' , i1 , '' )
  ooooooO0oo ( '[COLORorangered]Recently Uploaded[/COLOR]' , 'http://xvideos.com' , 10105 , oOOoo00O0O + 'recently_uploaded.png' , i1 , '' )
  ooooooO0oo ( '[COLORorangered]100% Verified[/COLOR]' , 'http://www.xvideos.com/verified/videos' , 10105 , oOOoo00O0O + '100_percent_verified.png' , i1 , '' )
  ooooooO0oo ( '[COLORorangered]Tags[/COLOR]' , 'http://www.xvideos.com/tags' , 10103 , oOOoo00O0O + 'tags.png' , i1 , '' )
  ooooooO0oo ( '[COLORorangered]In Your Language[/COLOR]' , 'http://www.xvideos.com/porn' , 101001 , oOOoo00O0O + 'language.png' , i1 , '' )
  ooooooO0oo ( '[COLORorangered]Adult Image Galleries[/COLOR]' , '' , 9999999 , oOOoo00O0O + 'galleries.png' , i1 , '' )
 else :
  oOOoO0 . ok ( '[COLORorangered]Genietvmedia@gmail.com[/COLOR]' , 'HOLD THE TISSUES[CR]' , 'Seems You Are Up To No Good Without Permission' , '[COLORorangered]Contact GenieTv For A Pass[/COLOR]' )
  if 9 - 9: iI
  if 33 - 33: i1I111II1I . o0O0
def O0oo0OO0oOOOo ( ) :
 i1i1i11IIi = [ '[COLORorangered]Adult Gallery[/COLOR]' , '[COLORorangered]JizBox[/COLOR]' , '[COLORorangered]Adult Channels[/COLOR]' ]
 II1III = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , i1i1i11IIi )
 if II1III == 0 :
  iI1iI1I1i1I ( )
 if II1III == 1 :
  iIi11Ii1 ( )
 if II1III == 2 :
  ARCONAI4 ( )
  if 50 - 50: II111iiii - i1I111II1I * oo / O0ooOooooO + OO0o
  if 88 - 88: IIII / O0ooOooooO + o0O0 - II111iiii / i1I111II1I - o0O00oooo
  if 15 - 15: oo + o0O00oooo - OoooooooOO / oOOO00o
def iI1iI1I1i1I ( ) :
 i1i1i11IIi = [ '[COLORorangered]YOLOselfies[/COLOR]' , '[COLORorangered]HotNudeGirls[/COLOR]' , '[COLORorangered]MyNudeBabes[/COLOR]' , '[COLORorangered]TeenNudeGirls[/COLOR]' , '[COLORorangered]ADULTmeme[/COLOR]' , '[COLORorangered]GIRLSmeme[/COLOR]' , ]
 II1III = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , i1i1i11IIi )
 if II1III == 0 :
  oo000OO00Oo ( 'http://www.yoloselfie.com/' )
 if II1III == 1 :
  O0OOO0OOoO0O ( 'http://www.hotnudegirls.net/#nudegirls' )
 if II1III == 2 :
  O00Oo000ooO0 ( 'http://www.teennudegirls.com/' )
 if II1III == 3 :
  O00Oo000ooO0 ( 'http://www.teennudegirls.com/' )
 if II1III == 4 :
  OoO0O00 ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if II1III == 5 :
  OoO0O00 ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 5 - 5: iii1I1 / OO0o . IIII - O0 / o0
def oo000OO00Oo ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( ooOooo000oOO )
 OOO00O = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' , url , 100111 , O0o0O00Oo0o0 )
 for url in OOO00O :
  O00O0oOO00O00 ( '[COLORorangered]NEXT[/COLOR]' , url , 100110 , O0o0O00Oo0o0 )
def i1Oo00 ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  i1i = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( i1i )
  sys . exit ( 1 )
def OoO0O00 ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( ooOooo000oOO )
 OOO00O = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for OOoOO0oo0ooO , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + O0o0O00Oo0o0 , 100113 , 'http:' + O0o0O00Oo0o0 )
 for url in OOO00O :
  O00O0oOO00O00 ( '[COLORorangered]NEXT[/COLOR]' , 'http:' + url , 100112 , O0o0O00Oo0o0 )
def O0OOO0OOoO0O ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , O0o0O00Oo0o0 )
def iiI111I1iIiI ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( ooOooo000oOO )
 OOO00O = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( '[COLORorangered]Click To Enlarge[/COLOR]' , O0o0O00Oo0o0 , 100113 , O0o0O00Oo0o0 )
def IIIi1I1IIii1II ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , O0o0O00Oo0o0 )
def O0ii1ii1ii ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( ooOooo000oOO )
 OOO00O = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( '[COLORorangered]Click To Enlarge[/COLOR]' , O0o0O00Oo0o0 , 100113 , O0o0O00Oo0o0 )
def O00Oo000ooO0 ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , O0o0O00Oo0o0 )
def oooooOoo0ooo ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( ooOooo000oOO )
 OOO00O = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  O00O0oOO00O00 ( '[COLORorangered]Click To Enlarge[/COLOR]' , O0o0O00Oo0o0 , 100113 , O0o0O00Oo0o0 )
def I1I1IiI1 ( url ) :
 i1i = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( i1i )
 sys . exit ( 1 )
 if 5 - 5: OO0o * i1I111II1I + o0O00oooo . oOOO00o + o0O00oooo
 if 91 - 91: O0
def iIi11Ii1 ( ) :
 i1i1i11IIi = [ '[COLORorangered]XXX Vids[/COLOR]' , '[COLORorangered]Perfect Girls[/COLOR]' , '[COLORorangered]Best Videos[/COLOR]' , '[COLORorangered]Genres[/COLOR]' , '[COLORorangered]Recently Uploaded[/COLOR]' , '[COLORorangered]100% Verified[/COLOR]' , '[COLORorangered]Tags[/COLOR]' , '[COLORorangered]In Your Language[/COLOR]' , '[COLORorangered]Search[/COLOR]' ]
 II1III = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , i1i1i11IIi )
 if II1III == 0 :
  oOOo0 ( 'http://watchxxxfree.com/categories' )
 if II1III == 1 :
  oo00O00oO ( 'http://www.perfectgirls.net' )
 if II1III == 2 :
  iIiIIIi ( 'http://www.xvideos.com/best' )
 if II1III == 3 :
  ooo00OOOooO ( 'http://www.xvideos.com/best' )
 if II1III == 4 :
  iIiIIIi ( 'http://www.xvideos.com/best' )
 if II1III == 5 :
  iIiIIIi ( 'http://www.xvideos.com/verified/videos' )
 if II1III == 6 :
  O00OOOoOoo0O ( 'http://www.xvideos.com/tags' )
 if II1III == 7 :
  O000OOo00oo ( 'http://www.xvideos.com/porn' )
 if II1III == 8 :
  oo0OOo ( )
  if 64 - 64: o0o0OOO0o0
  if 22 - 22: iii1I1 + IIII % oo
  if 9 - 9: OoooooooOO
  if 62 - 62: oOOO00o / iI + IIII / iI . II111iiii
  if 68 - 68: i11iIiiIii % oo + i11iIiiIii
  if 31 - 31: II111iiii . II
  if 1 - 1: iii1I1 / OO0o % o0O0 * o0 . i11iIiiIii
  if 2 - 2: oo * o0o0OOO0o0 - iIii1I11I1II1 + II . oo0Oo00Oo0 % o0O0
  if 92 - 92: o0O0
def IIiIiiIi ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO in Oo0OoO00oOO0o :
  if 'ch' in url :
   ooooooO0oo ( '[COLORorangered]' + OOoOO0oo0ooO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , i1 , i1 , '' )
def O000oo ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( ooOooo000oOO )
 IIi1I11I1II = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO in Oo0OoO00oOO0o :
  addDir2 ( ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , i1 , '' , '' )
 for OOoOO0oo0ooO , url in IIi1I11I1II :
  IIIII ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOoo00O0O + 'Next.png' , '' , '' )
def OooOoooOo ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  if 'jetload' in url :
   ii11IIII11I ( url )
def OOooo ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'file: "([^"]*)",' ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  RESOLVEtest ( url )
def oOOo0 ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for O0o0O00Oo0o0 , url , OOoOO0oo0ooO , oOooOOOoOo in Oo0OoO00oOO0o :
  if 'category' in url :
   ooooooO0oo ( '[COLORorangered]' + OOoOO0oo0ooO + '[COLORorange]   ' + oOooOOOoOo + '[/COLOR]' , url , 90006 , O0o0O00Oo0o0 , i1 , '' )
def i1Iii1i1I ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( ooOooo000oOO )
 IIi1I11I1II = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( ooOooo000oOO )
 for O0o0O00Oo0o0 , url , OOoOO0oo0ooO in Oo0OoO00oOO0o :
  addDir2 ( ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , O0o0O00Oo0o0 , '' , '' )
 for url in IIi1I11I1II :
  IIIII ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOoo00O0O + 'Next.png' , '' , '' )
def OOoO00 ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  if 'jetload' in url :
   ii11IIII11I ( url )
def ii11IIII11I ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'file: "([^"]*)",' ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  RESOLVEtest ( url )
def oo00O00oO ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , oOooOOOoOo in Oo0OoO00oOO0o :
  if 'category' in url :
   ooooooO0oo ( '[COLORorangered]' + OOoOO0oo0ooO + '[COLORorange]' + oOooOOOoOo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , i1 , '' , '' )
def IiI111111IIII ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 i1Ii = url
 Oo0OoO00oOO0o = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( ooOooo000oOO )
 IIi1I11I1II = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 in Oo0OoO00oOO0o :
  addDir2 ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , O0o0O00Oo0o0 , '' , '' )
 for url in IIi1I11I1II :
  IIIII ( '[COLORred]NEXT[/COLOR]' , i1Ii + '/' + url , 90003 , oOOoo00O0O + 'Next.png' , '' , '' )
def ii111iI1iIi1 ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'get\("(.*)", function' ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  OOO ( 'http://www.perfectgirls.net' + url )
def OOO ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( 'http://(.+?)\n' ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  oo0OOo0 ( 'http://' + url )
def O000OOo00oo ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , oOooOOOoOo in Oo0OoO00oOO0o :
  ooooooO0oo ( '[COLORorangered]' + OOoOO0oo0ooO + '[COLORgreen] - No of Videos : [COLORorange]' + oOooOOOoOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
def O00OOOoOoo0O ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 IIi1I11I1II = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( ooOooo000oOO )
 for url in IIi1I11I1II :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , i1 , '' , '' )
 Oo0OoO00oOO0o = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( ooOooo000oOO )
 for url , OOoOO0oo0ooO , oOooOOOoOo in Oo0OoO00oOO0o :
  ooooooO0oo ( ( '[COLORorangered]' + OOoOO0oo0ooO + '[COLORgreen] - No of Videos : [COLORorange]' + ( oOooOOOoOo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
  if 47 - 47: O0ooOooooO + o0O00oooo * iii1I1 / i1I111II1I - o0O0 % iIii1I11I1II1
def IIi11i1i1iI1 ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( ooOooo000oOO )
 for url in IIi1I11I1II :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoo00O0O + 'Next.png' , '' , '' )
 Oo0OoO00oOO0o = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( ooOooo000oOO )
 for O0o0O00Oo0o0 , url , OOoOO0oo0ooO , iiiIi1 in Oo0OoO00oOO0o :
  ooooooO0oo ( OOoOO0oo0ooO + '--' + ( iiiIi1 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( O0o0O00Oo0o0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 38 - 38: O0ooOooooO
  if 84 - 84: iIii1I11I1II1 % o0O0 / iIii1I11I1II1 % o0o0OOO0o0
def iIiIIIi ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( ooOooo000oOO )
 for O0o0O00Oo0o0 , url , OOoOO0oo0ooO , ii , OOooooO0Oo in Oo0OoO00oOO0o :
  ooooooO0oo ( '[COLORorangered]' + OOoOO0oo0ooO + '[COLORgreen] - Porn Quality : [COLORorange]' + OOooooO0Oo + ' - [COLORred]' + ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , O0o0O00Oo0o0 , O0o0O00Oo0o0 , OOooooO0Oo + ' - ' + ii )
 OO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( ooOooo000oOO )
 for url in OO :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoo00O0O + 'Next.png' , '' , '' )
  if 25 - 25: iI
def ooo00OOOooO ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 oOo0oO = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( ooOooo000oOO )
 IIi1I11I1II = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( ooOooo000oOO )
 for url in IIi1I11I1II :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoo00O0O + 'Next.png' , '' , '' )
 Oo0OoO00oOO0o = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( oOo0oO ) )
 for url , OOoOO0oo0ooO in Oo0OoO00oOO0o :
  if '/c/' in url :
   ooooooO0oo ( '[COLORorangered]' + OOoOO0oo0ooO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
   if 51 - 51: iii1I1 - oo0Oo00Oo0 + II111iiii * IIII . o0o0OOO0o0 + oo0Oo00Oo0
   if 78 - 78: i11iIiiIii / o0O0 - IIII / oOOO00o + oo0Oo00Oo0
def oo0OOo ( ) :
 oOoooo0O0Oo = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00ooO = ( oOoooo0O0Oo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OO0OO0O00oO0 = o00ooO . lower ( )
 oOI1Ii1I1 = 'http://www.xvideos.com/?k=' + OO0OO0O00oO0
 print oOI1Ii1I1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 ooOooo000oOO = Oo0oOOo ( oOI1Ii1I1 )
 Oo0OoO00oOO0o = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( ooOooo000oOO )
 for O0o0O00Oo0o0 , IiII111iI1ii1 , OOoOO0oo0ooO , ii , OOooooO0Oo in Oo0OoO00oOO0o :
  ooooooO0oo ( '[COLORorangered]' + OOoOO0oo0ooO + '[COLORgreen] - Porn Quality : [COLORorange]' + OOooooO0Oo + ' - [COLORred]' + ii + '[/COLOR]' , 'http://www.xvideos.com' + IiII111iI1ii1 , 10108 , O0o0O00Oo0o0 , O0o0O00Oo0o0 , OOooooO0Oo + ' - ' + ii )
 OO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( ooOooo000oOO )
 for IiII111iI1ii1 in OO :
  ooooooO0oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + IiII111iI1ii1 , 10105 , oOOoo00O0O + 'Next.png' , '' , '' )
if 37 - 37: oo0Oo00Oo0 - O0ooOooooO % iii1I1
if 77 - 77: iii1I1 - i1IIi - o0o0OOO0o0 . o0O00oooo
if 39 - 39: II111iiii / i1I111II1I + O0ooOooooO / o0O00oooo
if 13 - 13: o0 + O0 + o0O0 % II / OO0o . o0
if 86 - 86: oo0Oo00Oo0 * OO0o % i1IIi . IIII . i11iIiiIii
if 56 - 56: oo % O0 - II
if 100 - 100: IIII - O0 % oo0Oo00Oo0 * oOOO00o + II
if 88 - 88: OoooooooOO - iI * O0 * OoooooooOO . OoooooooOO
if 33 - 33: O0ooOooooO + o0O0 * oo0Oo00Oo0 / iIii1I11I1II1 - II
if 54 - 54: O0ooOooooO / oOOO00o . oo0Oo00Oo0 % o0O0
if 57 - 57: i11iIiiIii . oo - IIII - oo0Oo00Oo0 + o0O00oooo
if 63 - 63: o0O00oooo * o0O0
if 69 - 69: O0 . iI
if 49 - 49: II - o0o0OOO0o0
if 74 - 74: iIii1I11I1II1 * oo + o0O00oooo / i1IIi / II111iiii . iii1I1
if 62 - 62: OoooooooOO * II
if 58 - 58: o0O00oooo % OO0o
if 50 - 50: O0ooOooooO . OO0o
if 97 - 97: O0 + o0O00oooo
if 89 - 89: OO0o + iI * o0o0OOO0o0 * IIII
if 37 - 37: OoooooooOO - O0 - OO0o
if 77 - 77: oOOO00o * iIii1I11I1II1
if 98 - 98: II % IIII * OoooooooOO
if 51 - 51: iIii1I11I1II1 . o0O00oooo / oo0Oo00Oo0 + OO0o
if 33 - 33: i1I111II1I . II111iiii % o0O0 + OO0o
if 71 - 71: iii1I1 % oOOO00o
if 98 - 98: o0o0OOO0o0 % i11iIiiIii % i1I111II1I + IIII
if 78 - 78: oo % oo0Oo00Oo0 / o0O0 - iIii1I11I1II1
if 69 - 69: O0ooOooooO
if 11 - 11: II
if 16 - 16: IIII + o0 * O0 % i1IIi . II
if 67 - 67: OoooooooOO / II * IIII + o0o0OOO0o0
if 65 - 65: OoooooooOO - oo / i1I111II1I / II111iiii / i1IIi
if 71 - 71: O0ooOooooO + IIII
if 28 - 28: oOOO00o
def I11ii1IIiIi ( url ) :
 ooOooo000oOO = Oo0oOOo ( url )
 Oo0OoO00oOO0o = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( ooOooo000oOO )
 OOO00O = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( ooOooo000oOO )
 OoOOo0OOoO = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( ooOooo000oOO )
 for url in Oo0OoO00oOO0o :
  if 'http' in url :
   ooO0O00Oo0o ( '[COLORorangered]Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , i1 )
 for url in OOO00O :
  if 'http' in url :
   ooO0O00Oo0o ( '[COLORorangered]Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , i1 )
 for url in OoOOo0OOoO :
  if 'http' in url :
   ooO0O00Oo0o ( '[COLORorangered]Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , i1 )
   if 65 - 65: oo . o0o0OOO0o0 - O0ooOooooO * o0 / O0ooOooooO / i1I111II1I
def i111iIi1i1II1 ( url ) :
 oooO = xbmc . Player ( i1I1i111Ii ( ) )
 import urlresolver
 try : oooO . play ( url )
 except : pass
 if 67 - 67: II . i1IIi
def i1i1iI1iiiI ( title , message , times = 2000 , icon = i1 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def Ooo0oOooo0 ( ) :
 oOOOoo00 = iiIiIIIiiI ( )
 iiI1IIIi = oOOOoo00 . replace ( I1ii11iIi11i , "" )
 if os . path . exists ( oOOOoo00 ) or not oOOOoo00 == False :
  II11IiIi11 = open ( oOOOoo00 , mode = 'r' ) ; IIOOO0O00O0OOOO = II11IiIi11 . read ( ) ; II11IiIi11 . close ( )
  I1iiii1I ( "%s - %s" % ( IiII , iiI1IIIi ) , IIOOO0O00O0OOOO )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def iiIiIIIiiI ( ) :
 OOo0 = False
 if os . path . exists ( os . path . join ( I1ii11iIi11i , 'xbmc.log' ) ) :
  OOo0 = os . path . join ( I1ii11iIi11i , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'kodi.log' ) ) :
  OOo0 = os . path . join ( I1ii11iIi11i , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'spmc.log' ) ) :
  OOo0 = os . path . join ( I1ii11iIi11i , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'tvmc.log' ) ) :
  OOo0 = os . path . join ( I1ii11iIi11i , 'tvmc.log' )
 return OOo0
 if 73 - 73: o0O0
 if 42 - 42: i11iIiiIii * iIii1I11I1II1 / oo . i11iIiiIii % o0o0OOO0o0
 if 41 - 41: o0 / O0
 if 51 - 51: o0o0OOO0o0 % II
 if 60 - 60: II / oOOO00o . II / O0ooOooooO . o0
def I1iiii1I ( heading , announce ) :
 class OO0000o ( ) :
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
   try : II11IiIi11 = open ( announce ) ; i1I1i1 = II11IiIi11 . read ( )
   except : i1I1i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i1I1i1 ) )
   return
 OO0000o ( )
 OO0000o ( )
 if 81 - 81: i1I111II1I - iIii1I11I1II1 - i1IIi / O0ooOooooO - O0 * o0o0OOO0o0
def iI1i11II1i ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 o0o0OoOo0O0OO = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + U + '%26password%3D' + Pass + '%26type%3Dm3u_plus%26output%3Dts'
 iIi1I11I = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + U + '%26password%3D' + Pass
 Iii1 = 'http://piesustv.net:8000/enigma2.php?username=' + U + '&password=' + Pass + '&type=get_vod_categories'
 Iii1 = Oo0oOOo ( Iii1 )
 if not Iii1 == "" :
  ooO = 'https://tinyurl.com/create.php?source=indexpage&url=' + o0o0OoOo0O0OO + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( ooO ) )
  o0o00OOo0 = 'https://tinyurl.com/create.php?source=indexpage&url=' + iIi1I11I + '&submit=Make+TinyURL%21&alias='
  o0o0OoOo0O0OO = Oo0oOOo ( ooO )
  iIi1I11I = Oo0oOOo ( o0o00OOo0 )
  xbmc . log ( str ( iIi1I11I ) )
  I1IIii1 = regex_from_to ( o0o0OoOo0O0OO , '<div class="indent"><b>' , '</b>' )
  OO0o0oOOO0O = regex_from_to ( iIi1I11I , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLORorangered]WaveTv[/COLOR]' , '[COLORorangered]PLAYLIST URL: [/COLOR]%s' % I1IIii1 , '' , '[COLORorangered]EPG URL: [/COLOR]%s' % OO0o0oOOO0O )
 else :
  return
def iII1i11 ( ) :
 IIIII ( '[COLORorangered]Setup Tv Guide[/COLOR]' , '' , 212 , oOOoo00O0O + '12.png' , i1iiIIiiI111 , '' )
 IIIII ( '[COLORorangered]Open Guide[/COLOR]' , '' , 213 , oOOoo00O0O + '13.png' , i1iiIIiiI111 , '' )
 if 81 - 81: O0 . OoooooooOO . o0O0 - iii1I1 / iI + oo
def o0O00oOOoo ( ) :
 ivuesetup . iVueInt ( )
 if 18 - 18: IIII + o0 - O0
def o00O ( ) :
 i1Ii1i1I11Iii ( )
 return
 if 25 - 25: o0 + IIII / i1I111II1I . OO0o % O0 * iI
def i1Ii1i1I11Iii ( ) :
 if 84 - 84: i1I111II1I % IIII + i11iIiiIii
 II1I1Ii = xbmcaddon . Addon ( 'plugin.video.WaveTv' )
 Ooo0O0oooo = II1I1Ii . getSetting ( id = 'User' )
 iiI = II1I1Ii . getSetting ( id = 'Pass' )
 oOIIiIi = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 OOoOooOoOOOoo = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 Iiii1iI1i = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 I1ii1ii11i1I = "http://piesustv.net:8000/get.php?username=" + Ooo0O0oooo + "&password=" + iiI + "&type=m3u_plus&output=ts"
 o0OoOO = "http://piesustv.net:8000/xmltv.php?username=" + Ooo0O0oooo + "&password=" + iiI + "&type=m3u_plus&output=ts"
 if 55 - 55: i1I111II1I - o0o0OOO0o0 + II111iiii + o0O0 % IIII
 xbmc . executeJSONRPC ( oOIIiIi )
 xbmc . executeJSONRPC ( OOoOooOoOOOoo )
 xbmc . executeJSONRPC ( Iiii1iI1i )
 if 41 - 41: i1IIi - o0o0OOO0o0 - IIII
 III11I1 = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 III11I1 . setSetting ( id = 'm3uUrl' , value = I1ii1ii11i1I )
 III11I1 . setSetting ( id = 'epgUrl' , value = o0OoOO )
 III11I1 . setSetting ( id = 'm3uCache' , value = "false" )
 III11I1 . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def IIi1IIIi ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 if 99 - 99: IIII + iI * II111iiii . OO0o - oo
 if 58 - 58: IIII + OO0o - II
 if 3 - 3: iI
def oooOoOOO0oo0o ( ) :
 IIIII ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 IIIII ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 IIIII ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 IIIII ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 IIIII ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / oo
 if 96 - 96: OoooooooOO + oo0Oo00Oo0
 if 44 - 44: oo0Oo00Oo0
def I1i11i ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def IiIi ( url ) :
 if url == 'http://' : return False
 try :
  OOOOO0O00 = urllib2 . Request ( url )
  OOOOO0O00 . add_header ( 'User-Agent' , iIiiiI )
  Iii = urllib2 . urlopen ( OOOOO0O00 )
  Iii . close ( )
 except Exception , iIIiIiI1I1 :
  return iIIiIiI1I1
 return True
 if 56 - 56: II . O0 + iii1I1
 if 1 - 1: o0O0
 if 97 - 97: oOOO00o + o0O0 + O0 + i11iIiiIii
def oOoO0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "Genie XXX" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Genie XXX[/COLOR]" )
 return
 if 77 - 77: iIii1I11I1II1 . o0O0 % o0O0 + i11iIiiIii
def Oo00o0OO0O00o ( url ) :
 print '###' + IiII + ' - DELETING Addons20.db ###'
 O0Oooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 iiIi1i = os . path . join ( O0Oooo , 'Addons20.db' )
 try :
  os . remove ( iiIi1i )
  O0OoO000O0OO = xbmcgui . Dialog ( )
  print '=== ' + IiII + ' - DELETING    ' + str ( iiIi1i ) + '    ==='
  O0OoO000O0OO . ok ( IiII , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( IiII , "       No File To Remove" )
 return
 if 27 - 27: oOOO00o * i1I111II1I . O0ooOooooO % o0 * o0 . i1IIi
 if 72 - 72: oOOO00o % oo + iI / oo0Oo00Oo0 + o0
 if 10 - 10: O0ooOooooO / i1I111II1I + i11iIiiIii / IIII
 if 74 - 74: oOOO00o + O0 + i1IIi - i1IIi + II111iiii
 if 83 - 83: oo - II + oOOO00o
def Oo0oOOo ( url ) :
 OOOOO0O00 = urllib2 . Request ( url )
 OOOOO0O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Iii = urllib2 . urlopen ( OOOOO0O00 )
 iIi1Ii1i1iI = Iii . read ( )
 Iii . close ( )
 return iIi1Ii1i1iI
def I1iiii1I ( heading , announce ) :
 class OO0000o ( ) :
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
   try : II11IiIi11 = open ( announce ) ; i1I1i1 = II11IiIi11 . read ( )
   except : i1I1i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i1I1i1 ) )
   return
 OO0000o ( )
 OO0000o ( )
def IIiI1 ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 i1iI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1 , I1IiiI1ii1i , O0o in os . walk ( i1iI1 ) :
   oO0OoO00o = 0
   oO0OoO00o += len ( O0o )
   if 11 - 11: iii1I1 - II * II111iiii . oo . oo0Oo00Oo0
   if 61 - 61: o0O0 % II - OO0o - II111iiii % O0
   if oO0OoO00o > 0 :
    if 90 - 90: iIii1I11I1II1 + oo + i1I111II1I - O0ooOooooO * o0 . oo
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( oO0OoO00o ) + " files found" , "Do you want to delete them?" ) :
     if 37 - 37: i1I111II1I % i11iIiiIii % II111iiii . O0 . IIII
     for II11IiIi11 in O0o :
      os . unlink ( os . path . join ( ii1 , II11IiIi11 ) )
     for OO0oOOoo in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( ii1 , OO0oOOoo ) )
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
 oOOO00o000o ( url )
 return
def oOOO00o000o ( url ) :
 iIi11i1 = os . path . join ( O0oo0OO0 , 'addon_data' )
 oO00oo0o00o0o = [
 ( iIi11i1 ) ,
 ( o0oO0 ) ,
 ( os . path . join ( i1i1II , 'cache' ) ) ,
 ( os . path . join ( i1i1II , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( o0oO0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( o0oO0 , 'plugin.video.GenieXXX' , 'Images' ) ) ,
 ( os . path . join ( iIi11i1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( iIi11i1 , 'plugin.video.GenieXXX' , 'Images' ) ) ]
 if 7 - 7: O0 - iii1I1 + oo + II111iiii + iIii1I11I1II1
 OOo0ii11I1 = 0
 if 75 - 75: iI / II111iiii % O0
 for Ii111iIi1iIi in oO00oo0o00o0o :
  if os . path . exists ( Ii111iIi1iIi ) and not Ii111iIi1iIi in [ o0oO0 , iIi11i1 ] :
   for ii1 , I1IiiI1ii1i , O0o in os . walk ( Ii111iIi1iIi ) :
    oO0OoO00o = 0
    oO0OoO00o += len ( O0o )
    if oO0OoO00o > 0 :
     for II11IiIi11 in O0o :
      if not II11IiIi11 in I1i1iiI1 :
       try :
        os . unlink ( os . path . join ( ii1 , II11IiIi11 ) )
       except :
        pass
      else : oOOOoo00 ( 'Ignore Log File: %s' % II11IiIi11 )
     for OO0oOOoo in I1IiiI1ii1i :
      try :
       shutil . rmtree ( os . path . join ( ii1 , OO0oOOoo ) )
       OOo0ii11I1 += 1
       oOOOoo00 ( "[Success] cleared %s files from %s" % ( str ( oO0OoO00o ) , os . path . join ( Ii111iIi1iIi , OO0oOOoo ) ) )
      except :
       oOOOoo00 ( "[Failed] to wipe cache in: %s" % os . path . join ( Ii111iIi1iIi , OO0oOOoo ) )
  else :
   for ii1 , I1IiiI1ii1i , O0o in os . walk ( Ii111iIi1iIi ) :
    for OO0oOOoo in I1IiiI1ii1i :
     if 'cache' in OO0oOOoo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ii1 , OO0oOOoo ) )
       OOo0ii11I1 += 1
       oOOOoo00 ( "[Success] wiped %s " % os . path . join ( Ii111iIi1iIi , OO0oOOoo ) )
      except :
       oOOOoo00 ( "[Failed] to wipe cache in: %s" % os . path . join ( Ii111iIi1iIi , OO0oOOoo ) )
       if 21 - 21: oo0Oo00Oo0 / oo + IIII + OoooooooOO
 i1i1iI1iiiI ( IiII , 'Clear Cache: Removed %s Files' % OOo0ii11I1 )
def OoOo ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 i1iI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1 , I1IiiI1ii1i , O0o in os . walk ( i1iI1 ) :
   oO0OoO00o = 0
   oO0OoO00o += len ( O0o )
   if 35 - 35: i1I111II1I * oOOO00o . o0o0OOO0o0 * OO0o . o0O00oooo / O0
   if 100 - 100: O0ooOooooO . OO0o * iii1I1 % O0 * O0
   if oO0OoO00o > 0 :
    if 14 - 14: oo . i1I111II1I + II111iiii / o0O0 / o0o0OOO0o0
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( oO0OoO00o ) + " files found" , "Do you want to delete them?" ) :
     if 74 - 74: O0 / i1IIi
     for II11IiIi11 in O0o :
      os . unlink ( os . path . join ( ii1 , II11IiIi11 ) )
     for OO0oOOoo in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( ii1 , OO0oOOoo ) )
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
 if 78 - 78: OoooooooOO . iI + i1I111II1I - i1IIi
def ii1O0 ( ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 II1III = O0OoO000O0OO . yesno ( 'Force Close Genie XXX' , 'You are about to close Genie XXX' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if II1III == 0 : return
 elif II1III == 1 : pass
 iII1 = I1i11i ( )
 oOOOoo00 ( "Platform: " + str ( iII1 ) )
 os . _exit ( 1 )
 oOOOoo00 ( "Force close failed!  Trying alternate methods." )
 if iII1 == 'osx' :
  oOOOoo00 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iII1 == 'linux' :
  oOOOoo00 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iII1 == 'android' :
  oOOOoo00 ( "############ try android force close #################" )
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
 elif iII1 == 'windows' :
  oOOOoo00 ( "############ try windows force close #################" )
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
  oOOOoo00 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  oOOOoo00 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 27 - 27: iI . o0o0OOO0o0 + o0O00oooo / iIii1I11I1II1 % o0O0 . i1I111II1I
def oo0OOo0 ( url ) :
 import urlresolver
 try :
  IIIIi1 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( IIIIi1 , xbmcgui . ListItem ( OOoOO0oo0ooO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( OOoOO0oo0ooO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def I1i11i ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 3 - 3: O0ooOooooO
def oOOOoo00 ( log ) :
 xbmc . log ( "[%s]: %s" % ( IiII , log ) )
 if not os . path . exists ( o0oO0 ) : os . makedirs ( o0oO0 )
 if not os . path . exists ( o00 ) : II11IiIi11 = open ( o00 , 'w' ) ; II11IiIi11 . close ( )
 with open ( o00 , 'a' ) as II11IiIi11 :
  i1iiIiI1Ii1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  II11IiIi11 . write ( i1iiIiI1Ii1i . rstrip ( '\r\n' ) + '\n' )
  if 22 - 22: o0 / i11iIiiIii
def i1I1i111Ii ( ) :
 try :
  oOOoo = getSet ( "core-player" )
  if ( oOOoo == 'DVDPLAYER' ) : iII1111III1I = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oOOoo == 'MPLAYER' ) : iII1111III1I = xbmc . PLAYER_CORE_MPLAYER
  elif ( oOOoo == 'PAPLAYER' ) : iII1111III1I = xbmc . PLAYER_CORE_PAPLAYER
  else : iII1111III1I = xbmc . PLAYER_CORE_AUTO
 except : iII1111III1I = xbmc . PLAYER_CORE_AUTO
 return iII1111III1I
 return True
 if 39 - 39: i1IIi / o0
 if 78 - 78: i1I111II1I
def ooooooO0oo ( name , url , mode , iconimage , fanart , description ) :
 if 53 - 53: i1I111II1I * oOOO00o . o0O0 / O0 * i1I111II1I
 II11iI111i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00OoOo = True
 ii1ii111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ii1ii111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ii1ii111 . setProperty ( "Fanart_Image" , fanart )
 Oo00OoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11iI111i1 , listitem = ii1ii111 , isFolder = True )
 return Oo00OoOo
 if 33 - 33: oo
def IIIII ( name , url , mode , iconimage , fanart , description ) :
 if 92 - 92: o0 * iii1I1 * iii1I1 * II . iIii1I11I1II1
 II11iI111i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00OoOo = True
 ii1ii111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ii1ii111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ii1ii111 . setProperty ( "Fanart_Image" , fanart )
 Oo00OoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11iI111i1 , listitem = ii1ii111 , isFolder = False )
 return Oo00OoOo
def O00O0oOO00O00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 II11iI111i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo00OoOo = True
 ii1ii111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ii1ii111 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1Ii1111iIi = [ ]
  I1Ii1111iIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1Ii1111iIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI1IiI :
   I1Ii1111iIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ii1ii111 . addContextMenuItems ( I1Ii1111iIi )
 Oo00OoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11iI111i1 , listitem = ii1ii111 , isFolder = True )
 return Oo00OoOo
def ooO0O00Oo0o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 II11iI111i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo00OoOo = True
 ii1ii111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ii1ii111 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1Ii1111iIi = [ ]
  I1Ii1111iIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1Ii1111iIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI1IiI :
   I1Ii1111iIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ii1ii111 . addContextMenuItems ( I1Ii1111iIi )
 Oo00OoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11iI111i1 , listitem = ii1ii111 , isFolder = False )
 return Oo00OoOo
 if 31 - 31: o0o0OOO0o0 . O0ooOooooO * i1I111II1I + i11iIiiIii * oo0Oo00Oo0
def OO0ooo0o0O0Oooooo ( ) :
 i11IIIiI1I = [ ]
 o0iiiI1I1iIIIi1 = sys . argv [ 2 ]
 if len ( o0iiiI1I1iIIIi1 ) >= 2 :
  IiiI1iiiiI1iI = sys . argv [ 2 ]
  iIiiiii1i = IiiI1iiiiI1iI . replace ( '?' , '' )
  if ( IiiI1iiiiI1iI [ len ( IiiI1iiiiI1iI ) - 1 ] == '/' ) :
   IiiI1iiiiI1iI = IiiI1iiiiI1iI [ 0 : len ( IiiI1iiiiI1iI ) - 2 ]
  iiIi1IIiI = iIiiiii1i . split ( '&' )
  i11IIIiI1I = { }
  for i1oO0OO0 in range ( len ( iiIi1IIiI ) ) :
   o0O0Oo00 = { }
   o0O0Oo00 = iiIi1IIiI [ i1oO0OO0 ] . split ( '=' )
   if ( len ( o0O0Oo00 ) ) == 2 :
    i11IIIiI1I [ o0O0Oo00 [ 0 ] ] = o0O0Oo00 [ 1 ]
    if 51 - 51: oOOO00o % iIii1I11I1II1 - OoooooooOO % i1I111II1I * iIii1I11I1II1 % iI
 return i11IIIiI1I
 if 99 - 99: oo0Oo00Oo0 * II111iiii * O0ooOooooO
 if 92 - 92: iii1I1
IiiI1iiiiI1iI = OO0ooo0o0O0Oooooo ( )
IiII111iI1ii1 = None
OOoOO0oo0ooO = None
iI11I = None
ooO000 = None
oOOOO = None
Ii = None
Ii1ii111i1 = None
if 31 - 31: oOOO00o + O0
if 87 - 87: i1I111II1I
try :
 Ii1ii111i1 = int ( IiiI1iiiiI1iI [ "fav_mode" ] )
except :
 pass
 if 45 - 45: iI / OoooooooOO - o0O0 / IIII % o0
try :
 IiII111iI1ii1 = urllib . unquote_plus ( IiiI1iiiiI1iI [ "url" ] )
except :
 pass
try :
 OOoOO0oo0ooO = urllib . unquote_plus ( IiiI1iiiiI1iI [ "name" ] )
except :
 pass
try :
 ooO000 = urllib . unquote_plus ( IiiI1iiiiI1iI [ "iconimage" ] )
except :
 pass
try :
 iI11I = int ( IiiI1iiiiI1iI [ "mode" ] )
except :
 pass
try :
 oOOOO = urllib . unquote_plus ( IiiI1iiiiI1iI [ "fanart" ] )
except :
 pass
try :
 Ii = urllib . unquote_plus ( IiiI1iiiiI1iI [ "description" ] )
except :
 pass
 if 83 - 83: II . iIii1I11I1II1 - o0 * i11iIiiIii
 if 20 - 20: i1IIi * O0ooOooooO + II111iiii % OO0o % oo0Oo00Oo0
print str ( oO ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( iI11I )
print "URL: " + str ( IiII111iI1ii1 )
print "Name: " + str ( OOoOO0oo0ooO )
print "IconImage: " + str ( ooO000 )
if 13 - 13: iii1I1
if 60 - 60: oo * II
def I1iIiI11I1 ( content , viewType ) :
 if 27 - 27: IIII . i11iIiiIii % O0ooOooooO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OOO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OOO . getSetting ( viewType ) )
  if 65 - 65: II111iiii . II % oo0Oo00Oo0 * iI
  if 38 - 38: o0O00oooo / o0O0 % iii1I1
if iI11I == None : I11II1i ( )
elif iI11I == 1 : Genres ( )
elif iI11I == 2 : Lists ( IiII111iI1ii1 , ooO000 )
elif iI11I == 3 : all_mov ( )
elif iI11I == 4 : Search ( )
elif iI11I == 5 : oooOoOOO0oo0o ( )
elif iI11I == 6 : OoOo ( IiII111iI1ii1 )
elif iI11I == 7 : oOOO00o000o ( IiII111iI1ii1 )
elif iI11I == 8 : ii1O0 ( )
elif iI11I == 9 : IIiiiiiiIi1I1 ( )
elif iI11I == 10 : MyAccDetails ( )
elif iI11I == 11 : TvGuide ( )
elif iI11I == 12 : I1IIIii ( )
elif iI11I == 13 : ReCreate_Addon_ini ( )
elif iI11I == 14 : Get_Ultimate_playlinks_data ( IiII111iI1ii1 )
elif iI11I == 144 : Get_List_playlinks ( IiII111iI1ii1 )
elif iI11I == 15 : oo0OOo0 ( IiII111iI1ii1 )
elif iI11I == 222 : oo0OOo0 ( IiII111iI1ii1 )
elif iI11I == 16 : Streams_Menu ( )
elif iI11I == 17 : Live_Events ( OOoOO0oo0ooO )
elif iI11I == 18 : o0OOO . openSettings ( sys . argv [ 0 ] )
elif iI11I == 19 : WIZ ( )
elif iI11I == 20 : WIZARD ( IiII111iI1ii1 )
elif iI11I == 30 : CatchUp ( )
elif iI11I == 31 : CatchUpPlay ( IiII111iI1ii1 )
elif iI11I == 40 : VOD_Menu ( )
elif iI11I == 41 : Get_VOD_playlinks ( IiII111iI1ii1 )
elif iI11I == 21 : show_inf ( IiII111iI1ii1 )
elif iI11I == 22 : get_info ( IiII111iI1ii1 )
elif iI11I == 50 : RADIO ( )
elif iI11I == 51 : RADIO2 ( IiII111iI1ii1 )
elif iI11I == 50000 : Ooo0oOooo0 ( )
elif iI11I == 50001 : oOoO0 ( )
elif iI11I == 50002 : Oo00o0OO0O00o ( IiII111iI1ii1 )
elif iI11I == 60001 : apkmasterMenu ( )
elif iI11I == 60002 : apkInstaller ( OOoOO0oo0ooO , IiII111iI1ii1 )
elif iI11I == 211 : iII1i11 ( )
elif iI11I == 212 : o00O ( )
elif iI11I == 213 : IIi1IIIi ( )
elif iI11I == 214 : iI1i11II1i ( )
elif iI11I == 10100 : iIi11Ii1 ( )
elif iI11I == 101001 : O000OOo00oo ( IiII111iI1ii1 )
elif iI11I == 10105 : iIiIIIi ( IiII111iI1ii1 )
elif iI11I == 10106 : ooo00OOOooO ( IiII111iI1ii1 )
elif iI11I == 10104 : IIi11i1i1iI1 ( IiII111iI1ii1 )
elif iI11I == 10107 : oo0OOo ( )
elif iI11I == 10103 : O00OOOoOoo0O ( IiII111iI1ii1 )
elif iI11I == 10108 : I11ii1IIiIi ( IiII111iI1ii1 )
elif iI11I == 9999999 : iI1iI1I1i1I ( )
elif iI11I == 19999999 : O0oo0OO0oOOOo ( )
elif iI11I == 100110 : oo000OO00Oo ( IiII111iI1ii1 )
elif iI11I == 100111 : i1Oo00 ( IiII111iI1ii1 )
elif iI11I == 100112 : OoO0O00 ( IiII111iI1ii1 )
elif iI11I == 100113 : oOoOooOo0o0 ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
