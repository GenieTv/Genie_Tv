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
o0OoOoOO00 = "0.0.7"
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
oOo0oooo00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieXXX/Change_Log_Temp' ) )
oO0o0o0ooO0oO = ( O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
oo0o0O00 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieXXX' )
oO = xbmc . translatePath ( 'special://thumbnails' ) ;
i1iiIIiiI111 = "Reseller"
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'fanart.jpg' ) )
i1iiIII111ii = o0OOO . getLocalizedString
i1iIIi1 = CookieJar ( )
ii11iIi1I = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( i1iIIi1 ) )
ii11iIi1I . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
iI111I11I1I1 = int ( sys . argv [ 1 ] )
OOooO0OOoo = xbmc . translatePath ( o0OOO . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iiIIIII1i1iI = xbmc . translatePath ( 'special://home/userdata/' )
iIii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oOOoO0 = oo0o0O00 + '/addons.ini'
O0OoO000O0OO = xbmcgui . Dialog ( )
iiI1IiI = xbmcgui . Dialog ( )
if os . path . exists ( iIii1 ) == True :
 II = open ( iIii1 ) . read ( )
else : II = [ ]
if 57 - 57: ooOoo0O
if 76 - 76: i1II1I11 / i1I / OO0o / oo % O0o0Oo
def Oo00OOOOO ( ) :
 if not os . path . exists ( oOo0oooo00o ) :
  TextBox ( 'Change Log 11/03/2018 - v0.0.7' , '[COLORsteelblue]Live Selection Added[CR],[COLORsteelblue]ChangeLog Added[CR],[COLORsteelblue]Next Button Fixed[CR],[COLORsteelblue]Sections Repaired And Updated[CR]' )
  os . makedirs ( oOo0oooo00o )
def O0OO00o0OO ( ) :
 if Oo0oO0ooo == 'insert_password' :
  I11i1 ( '[COLORorangered]It Seems Youre Not Logged In, Are You Over 18?[/COLOR]' , '' , 222 , oOOoo00O0O + 'search.png' , i1 , '' )
  I11i1 ( '[COLORorangered]Yes I Am,,,, Honest[/COLOR]' , '' , 12 , i1 , i1 , '' )
  I11i1 ( '[COLORorangered]No, I Am Just A Pup[/COLOR]' , '' , 1001133 , i1 , i1 , '' )
  iIi1ii1I1 ( '[COLORsteelblue]Please Make A Selection And Flick Me To Enter[/COLOR]' , '' , 9 , i1 , i1 , '' )
 elif Oo0oO0ooo == 'dirtyfucker' :
  o0 ( )
 else :
  O0OoO000O0OO . ok ( '[COLORorangered]http://genietv.co.uk/xxx[/COLOR]' , 'HOLD THE TISSUES' , 'Password Incorrect Please Reset Defaults' , '[COLORorangered]And Contact GenieTv For The Pass[/COLOR]' )
def I11II1i ( ) :
 if Oo0oO0ooo == 'insert_password' :
  O0OoO000O0OO . ok ( '[COLORorangered]http://genietv.co.uk/xxx[/COLOR]' , 'You need to set the password to access this filth' , 'This is only given to dirty fuckers aged 18+' , ' @ [COLORorangered]genietv.co.uk/xxx[/COLOR]' )
  o0OOO . openSettings ( sys . argv [ 0 ] )
 else :
  O0OoO000O0OO . ok ( '[COLORorangered]http://genietv.co.uk/xxx[/COLOR]' , 'HOLD THE TISSUES[CR]' , 'Seems You Are Up To No Good Without Permission[CR]' , '[COLORorangered]Contact GenieTv For The Pass[/COLOR]' )
def IIIII ( ) :
 O0OoO000O0OO . ok ( '[COLORorangered]Genietvmedia@gmail.com[/COLOR]' , 'HOLD THE TISSUES[CR]' , 'What We Recommend[CR]' , '[COLORorangered]http://us.cbeebies.com/[/COLOR]' )
def ooooooO0oo ( ) :
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 O0OO00o0OO ( )
 if 49 - 49: ooo * I1I1i / IIIii1I1 * Ii + oo0O0oOOO00oO
 if 61 - 61: iiiiiIIii * o00OO0OOO0 % i1Iii % I1I1i % o00OO0OOO0
def o0 ( ) :
 if Oo0oO0ooo == 'dirtyfucker' :
  iIi1ii1I1 ( '[COLORorangered]Search[/COLOR]' , '' , 10107 , oOOoo00O0O + 'search.png' , i1 , '' , )
  iIi1ii1I1 ( '[COLORorangered]Live Stations + VOD[/COLOR]' , '' , 300000000 , i1 , i1 , '' )
  iIi1ii1I1 ( '[COLORorangered]Best Videos[/COLOR]' , 'http://www.xvideos.com/best' , 10105 , oOOoo00O0O + 'best_videos.png' , i1 , '' )
  iIi1ii1I1 ( '[COLORorangered]Recently Uploaded[/COLOR]' , 'http://xvideos.com' , 10105 , oOOoo00O0O + 'recently_uploaded.png' , i1 , '' )
  iIi1ii1I1 ( '[COLORorangered]100% Verified[/COLOR]' , 'http://www.xvideos.com/verified/videos' , 10105 , oOOoo00O0O + '100_percent_verified.png' , i1 , '' )
  iIi1ii1I1 ( '[COLORorangered]Tags[/COLOR]' , 'http://www.xvideos.com/tags' , 10103 , oOOoo00O0O + 'tags.png' , i1 , '' )
  iIi1ii1I1 ( '[COLORorangered]In Your Language[/COLOR]' , 'http://www.xvideos.com/porn' , 101001 , oOOoo00O0O + 'language.png' , i1 , '' )
  iIi1ii1I1 ( '[COLORorangered]Adult Image Galleries[/COLOR]' , '' , 9999999 , oOOoo00O0O + 'galleries.png' , i1 , '' )
 else :
  O0OoO000O0OO . ok ( '[COLORorangered]http://genietv.co.uk/xxx[/COLOR]' , 'HOLD THE TISSUES[CR]' , 'Seems You Are Up To No Good Without Permission' , '[COLORorangered]Contact GenieTv For A Pass[/COLOR]' )
  if 51 - 51: i11iIiiIii . ooOoo0O + II111iiii
def II111ii1II1i ( ) :
 OoOo00o = o0OOoo0OO0OOO ( 'https://raw.githubusercontent.com/fluxustv/IPTV/master/xxx.m3u' )
 iI1iI1I1i1I = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OoOo00o )
 for Ii11iII1 , Oo0O0O0ooO0O , IIIIii , O0o0 , OO00Oo in iI1iI1I1i1I :
  if 'INFO' in IIIIii :
   pass
  else :
   O0OOO0OOoO0O ( ( '[COLORsteelblue]' + Ii11iII1 + O0o0 + '[COLORorangered] - ' + IIIIii + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( OO00Oo ) . strip ( ) , 222 , Oo0O0O0ooO0O , Oo0O0O0ooO0O , ( '[COLORsteelblue]' + Ii11iII1 + O0o0 + '[COLORorangered] - ' + IIIIii + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for Oo0O0O0ooO0O , IIIIii , O0o0 , OO00Oo in iIi11Ii1 :
  if 'INFO' in IIIIii :
   pass
  else :
   O0OOO0OOoO0O ( ( '[COLORsteelblue]' + O0o0 + '[COLORorangered] - ' + IIIIii + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( OO00Oo ) . strip ( ) , 222 , Oo0O0O0ooO0O , Oo0O0O0ooO0O , ( '[COLORsteelblue]' + O0o0 + '[COLORorangered] - ' + IIIIii + '[/COLOR]' ) . replace ( '_' , ' ' ) )
   if 70 - 70: iiiiiIIii * i1II1I11 * IIIii1I1 / Ii
   if 88 - 88: O0
   if 64 - 64: IIIii1I1 * O0 + iiiiiIIii - I1I1i + i11iIiiIii * Ii
def iII ( ) :
 o0ooOooo000oOO = [ '[COLORorangered]Adult Gallery[/COLOR]' , '[COLORorangered]JizBox[/COLOR]' , '[COLORorangered]Adult Channels[/COLOR]' ]
 Oo0oOOo = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , o0ooOooo000oOO )
 if Oo0oOOo == 0 :
  Oo0OoO00oOO0o ( )
 if Oo0oOOo == 1 :
  OOO00O ( )
 if Oo0oOOo == 2 :
  ARCONAI4 ( )
  if 84 - 84: ooo * i1I / IIIii1I1 - O0
  if 30 - 30: iIii1I11I1II1 / i1Iii - o00OO0OOO0 - II111iiii % oo0O0oOOO00oO
  if 49 - 49: ooOoo0O % i1Iii . i1Iii . IIIii1I1 * i1Iii
def Oo0OoO00oOO0o ( ) :
 o0ooOooo000oOO = [ '[COLORorangered]YOLOselfies[/COLOR]' , '[COLORorangered]HotNudeGirls[/COLOR]' , '[COLORorangered]MyNudeBabes[/COLOR]' , '[COLORorangered]TeenNudeGirls[/COLOR]' , '[COLORorangered]ADULTmeme[/COLOR]' , '[COLORorangered]GIRLSmeme[/COLOR]' , ]
 Oo0oOOo = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , o0ooOooo000oOO )
 if Oo0oOOo == 0 :
  O0oOO0 ( 'http://www.yoloselfie.com/' )
 if Oo0oOOo == 1 :
  O0ooo0O0oo0 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if Oo0oOOo == 2 :
  oo0oOo ( 'http://www.teennudegirls.com/' )
 if Oo0oOOo == 3 :
  oo0oOo ( 'http://www.teennudegirls.com/' )
 if Oo0oOOo == 4 :
  o000O0o ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if Oo0oOOo == 5 :
  o000O0o ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 42 - 42: OO0o
def O0oOO0 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( OoOo00o )
 for url , Ii11iII1 , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' , url , 100111 , Oo0O0O0ooO0O )
 for url in iIi11Ii1 :
  IIIi1I1IIii1II ( '[COLORorangered]NEXT[/COLOR]' , url , 100110 , Oo0O0O0ooO0O )
def O0ii1ii1ii ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  oooooOoo0ooo = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( oooooOoo0ooo )
  sys . exit ( 1 )
def o000O0o ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OoOo00o )
 for Ii11iII1 , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + Oo0O0O0ooO0O , 100113 , 'http:' + Oo0O0O0ooO0O )
 for url in iIi11Ii1 :
  IIIi1I1IIii1II ( '[COLORorangered]NEXT[/COLOR]' , 'http:' + url , 100112 , Oo0O0O0ooO0O )
def O0ooo0O0oo0 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( OoOo00o )
 for url , Ii11iII1 , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , Oo0O0O0ooO0O )
def I1I1IiI1 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OoOo00o )
 for url , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( '[COLORorangered]Click To Enlarge[/COLOR]' , Oo0O0O0ooO0O , 100113 , Oo0O0O0ooO0O )
def III1iII1I1ii ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( OoOo00o )
 for url , Ii11iII1 , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , Oo0O0O0ooO0O )
def oOOo0 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OoOo00o )
 for url , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( '[COLORorangered]Click To Enlarge[/COLOR]' , Oo0O0O0ooO0O , 100113 , Oo0O0O0ooO0O )
def oo0oOo ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( OoOo00o )
 for url , Ii11iII1 , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , Oo0O0O0ooO0O )
def oo00O00oO ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( OoOo00o )
 for url , Oo0O0O0ooO0O in iI1iI1I1i1I :
  IIIi1I1IIii1II ( '[COLORorangered]Click To Enlarge[/COLOR]' , Oo0O0O0ooO0O , 100113 , Oo0O0O0ooO0O )
def iIiIIIi ( url ) :
 oooooOoo0ooo = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( oooooOoo0ooo )
 sys . exit ( 1 )
 if 93 - 93: oo0O0oOOO00oO
 if 10 - 10: IIIii1I1
def OOO00O ( ) :
 o0ooOooo000oOO = [ '[COLORorangered]XXX Vids[/COLOR]' , '[COLORorangered]Perfect Girls[/COLOR]' , '[COLORorangered]Best Videos[/COLOR]' , '[COLORorangered]Genres[/COLOR]' , '[COLORorangered]Recently Uploaded[/COLOR]' , '[COLORorangered]100% Verified[/COLOR]' , '[COLORorangered]Tags[/COLOR]' , '[COLORorangered]In Your Language[/COLOR]' , '[COLORorangered]Search[/COLOR]' ]
 Oo0oOOo = xbmcgui . Dialog ( ) . select ( '[COLORorangered]TOOLS[/COLOR]' , o0ooOooo000oOO )
 if Oo0oOOo == 0 :
  OOooOO000 ( 'http://watchxxxfree.com/categories' )
 if Oo0oOOo == 1 :
  OOoOoo ( 'http://www.perfectgirls.net' )
 if Oo0oOOo == 2 :
  oO0000OOo00 ( 'http://www.xvideos.com/best' )
 if Oo0oOOo == 3 :
  iiIi1IIiIi ( 'http://www.xvideos.com/best' )
 if Oo0oOOo == 4 :
  oO0000OOo00 ( 'http://www.xvideos.com/best' )
 if Oo0oOOo == 5 :
  oO0000OOo00 ( 'http://www.xvideos.com/verified/videos' )
 if Oo0oOOo == 6 :
  oOO00Oo ( 'http://www.xvideos.com/tags' )
 if Oo0oOOo == 7 :
  i1iIIIi1i ( 'http://www.xvideos.com/porn' )
 if Oo0oOOo == 8 :
  iI1iIIiiii ( )
  if 26 - 26: IIIii1I1 . OoooooooOO
  if 39 - 39: oo0O0oOOO00oO - O0 % i11iIiiIii * o00OO0OOO0 . iiiiiIIii
  if 58 - 58: i1I % i11iIiiIii . oo0O0oOOO00oO / ooo
  if 84 - 84: oo0O0oOOO00oO . O0o0Oo / i1II1I11 - ooOoo0O / OoooooooOO / oo
  if 12 - 12: ooOoo0O * oo0O0oOOO00oO % i1IIi % iIii1I11I1II1
  if 20 - 20: I1I1i % Ii / Ii + Ii
  if 45 - 45: ooo - iiiiiIIii - OoooooooOO - i1I . II111iiii / O0
  if 51 - 51: O0 + oo0O0oOOO00oO
  if 8 - 8: ooo * OO0o - Ii - i1I * I1I1i % ooOoo0O
def ii ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( OoOo00o )
 for url , Ii11iII1 in iI1iI1I1i1I :
  if 'ch' in url :
   iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , i1 , i1 , '' )
def oOooOOOoOo ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( OoOo00o )
 i1Iii1i1I = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( OoOo00o )
 for url , Ii11iII1 in iI1iI1I1i1I :
  O0OOO0OOoO0O ( ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , i1 , '' , '' )
 for Ii11iII1 , url in i1Iii1i1I :
  I11i1 ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOoo00O0O + 'Next.png' , '' , '' )
def OOoO00 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  if 'jetload' in url :
   IiI111111IIII ( url )
def i1Ii ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'file: "([^"]*)",' ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  RESOLVEtest ( url )
def OOooOO000 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( OoOo00o )
 for Oo0O0O0ooO0O , url , Ii11iII1 , ii111iI1iIi1 in iI1iI1I1i1I :
  if 'category' in url :
   iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[COLORorange]   ' + ii111iI1iIi1 + '[/COLOR]' , url , 90006 , Oo0O0O0ooO0O , i1 , '' )
def OOO ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OoOo00o )
 i1Iii1i1I = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( OoOo00o )
 for Oo0O0O0ooO0O , url , Ii11iII1 in iI1iI1I1i1I :
  O0OOO0OOoO0O ( ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , Oo0O0O0ooO0O , '' , '' )
 for url in i1Iii1i1I :
  I11i1 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOoo00O0O + 'Next.png' , '' , '' )
def oo0OOo0 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  if 'jetload' in url :
   IiI111111IIII ( url )
def IiI111111IIII ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'file: "([^"]*)",' ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  RESOLVEtest ( url )
def OOoOoo ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( OoOo00o )
 for url , Ii11iII1 , ii111iI1iIi1 in iI1iI1I1i1I :
  if 'category' in url :
   iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[COLORorange]' + ii111iI1iIi1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , i1 , '' , '' )
def I11IiI ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 O0ooO0Oo00o = url
 iI1iI1I1i1I = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoOo00o )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( OoOo00o )
 for url , Ii11iII1 , Oo0O0O0ooO0O in iI1iI1I1i1I :
  O0OOO0OOoO0O ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , Oo0O0O0ooO0O , '' , '' )
 for url in i1Iii1i1I :
  I11i1 ( '[COLORred]NEXT[/COLOR]' , O0ooO0Oo00o + '/' + url , 90003 , oOOoo00O0O + 'Next.png' , '' , '' )
def ooO0oOOooOo0 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'get\("(.*)", function' ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  i1I1ii11i1Iii ( 'http://www.perfectgirls.net' + url )
def i1I1ii11i1Iii ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'http://(.+?)\n' ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  I1IiiiiI ( 'http://' + url )
def i1iIIIi1i ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( OoOo00o )
 for url , Ii11iII1 , ii111iI1iIi1 in iI1iI1I1i1I :
  iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[COLORgreen] - No of Videos : [COLORorange]' + ii111iI1iIi1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
def oOO00Oo ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 i1Iii1i1I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( OoOo00o )
 for url in i1Iii1i1I :
  iIi1ii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , i1 , '' , '' )
 iI1iI1I1i1I = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( OoOo00o )
 for url , Ii11iII1 , ii111iI1iIi1 in iI1iI1I1i1I :
  iIi1ii1I1 ( ( '[COLORorangered]' + Ii11iII1 + '[COLORgreen] - No of Videos : [COLORorange]' + ( ii111iI1iIi1 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
  if 80 - 80: o00OO0OOO0 . i11iIiiIii - oo
def iIiIIi1 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OoOo00o )
 for url in i1Iii1i1I :
  iIi1ii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoo00O0O + 'Next.png' , '' , '' )
 iI1iI1I1i1I = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( OoOo00o )
 for Oo0O0O0ooO0O , url , Ii11iII1 , I1IIII1i in iI1iI1I1i1I :
  iIi1ii1I1 ( Ii11iII1 + '--' + ( I1IIII1i ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( Oo0O0O0ooO0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 2 - 2: IIIii1I1 + Ii - ooOoo0O % oo . oo0O0oOOO00oO
  if 18 - 18: I1I1i + oo0O0oOOO00oO - Ii . II111iiii + i11iIiiIii
def oO0000OOo00 ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( OoOo00o )
 for Oo0O0O0ooO0O , url , Ii11iII1 , iI1Ii1iI11iiI , OO0OO0O00oO0 in iI1iI1I1i1I :
  iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[COLORgreen] - Porn Quality : [COLORorange]' + iI1Ii1iI11iiI + ' - [COLORred]' + OO0OO0O00oO0 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , Oo0O0O0ooO0O , Oo0O0O0ooO0O , iI1Ii1iI11iiI + ' - ' + OO0OO0O00oO0 )
 oOI1Ii1I1 = re . compile ( '<li><a href="([^"]*)" class="no-page next-page">Next</a></li></ul></div>' ) . findall ( OoOo00o )
 for Oo0O0O0ooO0O , url , Ii11iII1 , OO0OO0O00oO0 in iIi11Ii1 :
  iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[COLORgreen] - Porn Quality : [COLORorange]' + OO0OO0O00oO0 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , Oo0O0O0ooO0O , Oo0O0O0ooO0O , OO0OO0O00oO0 )
 oOI1Ii1I1 = re . compile ( '<li><a href="([^"]*)" class="no-page next-page">Next</a></li></ul></div>' ) . findall ( OoOo00o )
 for url in oOI1Ii1I1 :
  iIi1ii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoo00O0O + 'Next.png' , '' , '' )
  if 28 - 28: O0 * i1II1I11 - I1I1i % iIii1I11I1II1 * Ii - i11iIiiIii
def iiIi1IIiIi ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 IIII11 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( OoOo00o )
 i1Iii1i1I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( OoOo00o )
 for url in i1Iii1i1I :
  iIi1ii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoo00O0O + 'Next.png' , '' , '' )
 iI1iI1I1i1I = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( IIII11 ) )
 for url , Ii11iII1 in iI1iI1I1i1I :
  if '/c/' in url :
   iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1 , '' , '' )
   if 38 - 38: oo - ooo + iIii1I11I1II1 / OO0o % i1II1I11
   if 57 - 57: i1I / i1Iii
def iI1iIIiiii ( ) :
 Ii1I1Ii = iiI1IiI . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOoO0 = ( Ii1I1Ii ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OO0Oooo0oOO0O = OOoO0 . lower ( )
 o00O0 = 'http://www.xvideos.com/?k=' + OO0Oooo0oOO0O
 print o00O0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OoOo00o = o0OOoo0OO0OOO ( o00O0 )
 iI1iI1I1i1I = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( OoOo00o )
 for Oo0O0O0ooO0O , OO00Oo , Ii11iII1 , OO0OO0O00oO0 , oOO0O00Oo0O0o in iI1iI1I1i1I :
  iIi1ii1I1 ( '[COLORorangered]' + Ii11iII1 + '[COLORgreen] - Porn Quality : [COLORorange]' + oOO0O00Oo0O0o + ' - [COLORred]' + OO0OO0O00oO0 + '[/COLOR]' , 'http://www.xvideos.com' + OO00Oo , 10108 , Oo0O0O0ooO0O , Oo0O0O0ooO0O , oOO0O00Oo0O0o + ' - ' + OO0OO0O00oO0 )
 oOI1Ii1I1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OoOo00o )
 for OO00Oo in oOI1Ii1I1 :
  iIi1ii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OO00Oo , 10105 , oOOoo00O0O + 'Next.png' , '' , '' )
if 13 - 13: OoooooooOO
if 33 - 33: o00OO0OOO0 + oo0O0oOOO00oO * ooo / iIii1I11I1II1 - ooOoo0O
if 54 - 54: o00OO0OOO0 / I1I1i . ooo % oo0O0oOOO00oO
if 57 - 57: i11iIiiIii . O0o0Oo - Ii - ooo + OO0o
if 63 - 63: OO0o * oo0O0oOOO00oO
if 69 - 69: O0 . i1I
if 49 - 49: ooOoo0O - IIIii1I1
if 74 - 74: iIii1I11I1II1 * O0o0Oo + OO0o / i1IIi / II111iiii . i1II1I11
if 62 - 62: OoooooooOO * ooOoo0O
if 58 - 58: OO0o % oo
if 50 - 50: o00OO0OOO0 . oo
if 97 - 97: O0 + OO0o
if 89 - 89: oo + i1I * IIIii1I1 * Ii
if 37 - 37: OoooooooOO - O0 - oo
if 77 - 77: I1I1i * iIii1I11I1II1
if 98 - 98: ooOoo0O % Ii * OoooooooOO
if 51 - 51: iIii1I11I1II1 . OO0o / ooo + oo
if 33 - 33: i1Iii . II111iiii % oo0O0oOOO00oO + oo
if 71 - 71: i1II1I11 % I1I1i
if 98 - 98: IIIii1I1 % i11iIiiIii % i1Iii + Ii
if 78 - 78: O0o0Oo % ooo / oo0O0oOOO00oO - iIii1I11I1II1
if 69 - 69: o00OO0OOO0
if 11 - 11: ooOoo0O
if 16 - 16: Ii + iiiiiIIii * O0 % i1IIi . ooOoo0O
if 67 - 67: OoooooooOO / ooOoo0O * Ii + IIIii1I1
if 65 - 65: OoooooooOO - O0o0Oo / i1Iii / II111iiii / i1IIi
if 71 - 71: o00OO0OOO0 + Ii
if 28 - 28: I1I1i
if 38 - 38: i1Iii % II111iiii % IIIii1I1 / i1I + OO0o / i1IIi
if 54 - 54: iIii1I11I1II1 % O0o0Oo - I1I1i / ooo - i1I . IIIii1I1
if 11 - 11: O0o0Oo . i1I * iiiiiIIii * OoooooooOO + i1Iii
if 33 - 33: O0 * oo - o00OO0OOO0 % o00OO0OOO0
if 18 - 18: o00OO0OOO0 / i1II1I11 * o00OO0OOO0 + o00OO0OOO0 * i11iIiiIii * O0o0Oo
if 11 - 11: i1Iii / OO0o - iiiiiIIii * OoooooooOO + OoooooooOO . OO0o
if 26 - 26: Ii % O0o0Oo
def o00Oo0oooooo ( url ) :
 OoOo00o = o0OOoo0OO0OOO ( url )
 iI1iI1I1i1I = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( OoOo00o )
 iIi11Ii1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( OoOo00o )
 O0oO0 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( OoOo00o )
 for url in iI1iI1I1i1I :
  if 'http' in url :
   iII11 ( '[COLORorangered]Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , i1 )
 for url in iIi11Ii1 :
  if 'http' in url :
   iII11 ( '[COLORorangered]Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , i1 )
 for url in O0oO0 :
  if 'http' in url :
   iII11 ( '[COLORorangered]Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , i1 )
   if 32 - 32: o00OO0OOO0
def Iii1 ( url ) :
 oOOOoo00 = xbmc . Player ( iiIiIIIiiI ( ) )
 import urlresolver
 try : oOOOoo00 . play ( url )
 except : pass
 if 12 - 12: O0 - oo
def oOoO00O0 ( title , message , times = 2000 , icon = i1 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def OO ( ) :
 Ii1iI111II1I1 = oOOOOoOO0o ( )
 i1II1 = Ii1iI111II1I1 . replace ( I1ii11iIi11i , "" )
 if os . path . exists ( Ii1iI111II1I1 ) or not Ii1iI111II1I1 == False :
  i11i1 = open ( Ii1iI111II1I1 , mode = 'r' ) ; IiiiiI1i1Iii = i11i1 . read ( ) ; i11i1 . close ( )
  oo00oO0o ( "%s - %s" % ( IiII , i1II1 ) , IiiiiI1i1Iii )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def oOOOOoOO0o ( ) :
 iiii111II = False
 if os . path . exists ( os . path . join ( I1ii11iIi11i , 'xbmc.log' ) ) :
  iiii111II = os . path . join ( I1ii11iIi11i , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'kodi.log' ) ) :
  iiii111II = os . path . join ( I1ii11iIi11i , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'spmc.log' ) ) :
  iiii111II = os . path . join ( I1ii11iIi11i , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'tvmc.log' ) ) :
  iiii111II = os . path . join ( I1ii11iIi11i , 'tvmc.log' )
 return iiii111II
 if 50 - 50: I1I1i * ooOoo0O % iIii1I11I1II1 + Ii + oo0O0oOOO00oO + ooOoo0O
 if 71 - 71: O0o0Oo * O0o0Oo * i1IIi . ooo / o00OO0OOO0
 if 85 - 85: IIIii1I1
 if 20 - 20: ooo % iiiiiIIii
 if 19 - 19: O0o0Oo % iiiiiIIii + i1Iii / o00OO0OOO0 . i1Iii
def oo00oO0o ( heading , announce ) :
 class IiIi1I1 ( ) :
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
   try : i11i1 = open ( announce ) ; IiIIi1 = i11i1 . read ( )
   except : IiIIi1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiIIi1 ) )
   return
 IiIi1I1 ( )
 IiIi1I1 ( )
 if 47 - 47: i1II1I11 * O0o0Oo + iIii1I11I1II1 / o00OO0OOO0 / i1I - OoooooooOO
def iII1i11IIi1i ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 oOOoo0000O0o0 = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + U + '%26password%3D' + Pass + '%26type%3Dm3u_plus%26output%3Dts'
 II1III = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + U + '%26password%3D' + Pass
 III1 = 'http://piesustv.net:8000/enigma2.php?username=' + U + '&password=' + Pass + '&type=get_vod_categories'
 III1 = o0OOoo0OO0OOO ( III1 )
 if not III1 == "" :
  OooooO0oOOOO = 'https://tinyurl.com/create.php?source=indexpage&url=' + oOOoo0000O0o0 + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( OooooO0oOOOO ) )
  o0O00oOOoo = 'https://tinyurl.com/create.php?source=indexpage&url=' + II1III + '&submit=Make+TinyURL%21&alias='
  oOOoo0000O0o0 = o0OOoo0OO0OOO ( OooooO0oOOOO )
  II1III = o0OOoo0OO0OOO ( o0O00oOOoo )
  xbmc . log ( str ( II1III ) )
  i1I1iIi = regex_from_to ( oOOoo0000O0o0 , '<div class="indent"><b>' , '</b>' )
  IIii11Ii1i1I = regex_from_to ( II1III , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLORorangered]WaveTv[/COLOR]' , '[COLORorangered]PLAYLIST URL: [/COLOR]%s' % i1I1iIi , '' , '[COLORorangered]EPG URL: [/COLOR]%s' % IIii11Ii1i1I )
 else :
  return
def Oooo0O ( ) :
 I11i1 ( '[COLORorangered]Setup Tv Guide[/COLOR]' , '' , 212 , oOOoo00O0O + '12.png' , oooOOOOO , '' )
 I11i1 ( '[COLORorangered]Open Guide[/COLOR]' , '' , 213 , oOOoo00O0O + '13.png' , oooOOOOO , '' )
 if 90 - 90: iIii1I11I1II1 % i1Iii
def OoO0O00O0oo0O ( ) :
 ivuesetup . iVueInt ( )
 if 36 - 36: I1I1i + O0 - Ii - O0 % IIIii1I1 . ooo
def oooiiI ( ) :
 oOIIiIi ( )
 return
 if 91 - 91: O0o0Oo * i1II1I11 / ooOoo0O . O0 + i1I + OO0o
def oOIIiIi ( ) :
 if 8 - 8: ooo / O0o0Oo
 i1iI1 = xbmcaddon . Addon ( 'plugin.video.WaveTv' )
 i11ii1ii11i = i1iI1 . getSetting ( id = 'User' )
 ooO0OoOO = i1iI1 . getSetting ( id = 'Pass' )
 O0O0Oo00 = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 oOoO00o = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 oO00O0 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 IIi1IIIi = "http://piesustv.net:8000/get.php?username=" + i11ii1ii11i + "&password=" + ooO0OoOO + "&type=m3u_plus&output=ts"
 O00Ooo = "http://piesustv.net:8000/xmltv.php?username=" + i11ii1ii11i + "&password=" + ooO0OoOO + "&type=m3u_plus&output=ts"
 if 52 - 52: O0o0Oo - i1II1I11 + O0o0Oo % oo
 xbmc . executeJSONRPC ( O0O0Oo00 )
 xbmc . executeJSONRPC ( oOoO00o )
 xbmc . executeJSONRPC ( oO00O0 )
 if 35 - 35: iIii1I11I1II1
 I1i = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 I1i . setSetting ( id = 'm3uUrl' , value = IIi1IIIi )
 I1i . setSetting ( id = 'epgUrl' , value = O00Ooo )
 I1i . setSetting ( id = 'm3uCache' , value = "false" )
 I1i . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def iIII ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 if 70 - 70: oo0O0oOOO00oO / iIii1I11I1II1
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / O0o0Oo
 if 96 - 96: OoooooooOO + ooo
def iiII1i11i ( ) :
 I11i1 ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , oOOoo00O0O + '5.png' , oooOOOOO , '' )
 I11i1 ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , oOOoo00O0O + '5.png' , oooOOOOO , '' )
 I11i1 ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , oOOoo00O0O + '5.png' , oooOOOOO , '' )
 I11i1 ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , oOOoo00O0O + '5.png' , oooOOOOO , '' )
 I11i1 ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , oOOoo00O0O + '5.png' , oooOOOOO , '' )
 if 11 - 11: ooOoo0O / II111iiii + oo * O0o0Oo - O0o0Oo - ooOoo0O
 if 85 - 85: IIIii1I1 % ooo / iIii1I11I1II1 . iIii1I11I1II1
 if 31 - 31: oo % i1I
def iI1I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def OooOoOo ( url ) :
 if url == 'http://' : return False
 try :
  III1I1Iii1iiI = urllib2 . Request ( url )
  III1I1Iii1iiI . add_header ( 'User-Agent' , iIiiiI )
  i1Iii11I1i = urllib2 . urlopen ( III1I1Iii1iiI )
  i1Iii11I1i . close ( )
 except Exception , Oo00o0OO0O00o :
  return Oo00o0OO0O00o
 return True
 if 82 - 82: IIIii1I1 + OoooooooOO - i1IIi . i1IIi
 if 6 - 6: oo / IIIii1I1 / II111iiii
 if 27 - 27: I1I1i * i1Iii . o00OO0OOO0 % iiiiiIIii * iiiiiIIii . i1IIi
def O0OOoOOO0oO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iiI1IiI = xbmcgui . Dialog ( )
 iiI1IiI . ok ( "Genie XXX" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Genie XXX[/COLOR]" )
 return
 if 28 - 28: i1Iii + i11iIiiIii / IIIii1I1 % OO0o % i1II1I11 - O0
def ooo0OOO ( url ) :
 print '###' + IiII + ' - DELETING Addons20.db ###'
 iii1Ii1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 IIi = os . path . join ( iii1Ii1Ii1 , 'Addons20.db' )
 try :
  os . remove ( IIi )
  iiI1IiI = xbmcgui . Dialog ( )
  print '=== ' + IiII + ' - DELETING    ' + str ( IIi ) + '    ==='
  iiI1IiI . ok ( IiII , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  iiI1IiI = xbmcgui . Dialog ( )
  iiI1IiI . ok ( IiII , "       No File To Remove" )
 return
 if 94 - 94: II111iiii - i1II1I11
 if 91 - 91: i1II1I11
 if 31 - 31: I1I1i / i11iIiiIii % iIii1I11I1II1 + I1I1i / i11iIiiIii
 if 70 - 70: i1I * O0 . IIIii1I1 + ooOoo0O . iiiiiIIii
 if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - i1I - IIIii1I1
def o0OOoo0OO0OOO ( url ) :
 III1I1Iii1iiI = urllib2 . Request ( url )
 III1I1Iii1iiI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Iii11I1i = urllib2 . urlopen ( III1I1Iii1iiI )
 o00oo0 = i1Iii11I1i . read ( )
 i1Iii11I1i . close ( )
 return o00oo0
def oo00oO0o ( heading , announce ) :
 class IiIi1I1 ( ) :
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
   try : i11i1 = open ( announce ) ; IiIIi1 = i11i1 . read ( )
   except : IiIIi1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiIIi1 ) )
   return
 IiIi1I1 ( )
 IiIi1I1 ( )
def oooooOOO000Oo ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 Ooo00OoOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Oo0OO0000oooo , IIII1iII , ii1III11 in os . walk ( Ooo00OoOOO ) :
   I1iiIIIi11 = 0
   I1iiIIIi11 += len ( ii1III11 )
   if 12 - 12: OoooooooOO % oo * IIIii1I1 % iIii1I11I1II1 / Ii
   if 27 - 27: i11iIiiIii % II111iiii % IIIii1I1 . O0 - i1II1I11 + OO0o
   if I1iiIIIi11 > 0 :
    if 57 - 57: iIii1I11I1II1 / IIIii1I1 - i1IIi
    iiI1IiI = xbmcgui . Dialog ( )
    if iiI1IiI . yesno ( "Delete Package Cache Files" , str ( I1iiIIIi11 ) + " files found" , "Do you want to delete them?" ) :
     if 51 - 51: iiiiiIIii
     for i11i1 in ii1III11 :
      os . unlink ( os . path . join ( Oo0OO0000oooo , i11i1 ) )
     for ii11I1 in IIII1iII :
      shutil . rmtree ( os . path . join ( Oo0OO0000oooo , ii11I1 ) )
     iiI1IiI = xbmcgui . Dialog ( )
     iiI1IiI . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    iiI1IiI = xbmcgui . Dialog ( )
    iiI1IiI . ok ( IiII , "       No Packages to DELETE" )
 except :
  iiI1IiI = xbmcgui . Dialog ( )
  iiI1IiI . ok ( IiII , "Error Deleting Packages please visit The Support Group, Genie XXX on facebook" )
 oO0oo ( url )
 return
def oO0oo ( url ) :
 Ii111iIi1iIi = os . path . join ( O0oo0OO0 , 'addon_data' )
 IIIIIo0ooOoO000oO = [
 ( Ii111iIi1iIi ) ,
 ( o0oO0 ) ,
 ( os . path . join ( i1i1II , 'cache' ) ) ,
 ( os . path . join ( i1i1II , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( o0oO0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( o0oO0 , 'plugin.video.GenieXXX' , 'Images' ) ) ,
 ( os . path . join ( Ii111iIi1iIi , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Ii111iIi1iIi , 'plugin.video.GenieXXX' , 'Images' ) ) ]
 if 85 - 85: oo . OO0o / i1Iii . O0 % o00OO0OOO0
 OO0ooo0oOO = 0
 if 97 - 97: ooOoo0O / oo0O0oOOO00oO
 for Oooo0 in IIIIIo0ooOoO000oO :
  if os . path . exists ( Oooo0 ) and not Oooo0 in [ o0oO0 , Ii111iIi1iIi ] :
   for Oo0OO0000oooo , IIII1iII , ii1III11 in os . walk ( Oooo0 ) :
    I1iiIIIi11 = 0
    I1iiIIIi11 += len ( ii1III11 )
    if I1iiIIIi11 > 0 :
     for i11i1 in ii1III11 :
      if not i11i1 in I1i1iiI1 :
       try :
        os . unlink ( os . path . join ( Oo0OO0000oooo , i11i1 ) )
       except :
        pass
      else : Ii1iI111II1I1 ( 'Ignore Log File: %s' % i11i1 )
     for ii11I1 in IIII1iII :
      try :
       shutil . rmtree ( os . path . join ( Oo0OO0000oooo , ii11I1 ) )
       OO0ooo0oOO += 1
       Ii1iI111II1I1 ( "[Success] cleared %s files from %s" % ( str ( I1iiIIIi11 ) , os . path . join ( Oooo0 , ii11I1 ) ) )
      except :
       Ii1iI111II1I1 ( "[Failed] to wipe cache in: %s" % os . path . join ( Oooo0 , ii11I1 ) )
  else :
   for Oo0OO0000oooo , IIII1iII , ii1III11 in os . walk ( Oooo0 ) :
    for ii11I1 in IIII1iII :
     if 'cache' in ii11I1 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Oo0OO0000oooo , ii11I1 ) )
       OO0ooo0oOO += 1
       Ii1iI111II1I1 ( "[Success] wiped %s " % os . path . join ( Oooo0 , ii11I1 ) )
      except :
       Ii1iI111II1I1 ( "[Failed] to wipe cache in: %s" % os . path . join ( Oooo0 , ii11I1 ) )
       if 59 - 59: OoooooooOO
 oOoO00O0 ( IiII , 'Clear Cache: Removed %s Files' % OO0ooo0oOO )
def i1iiiii1 ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 Ooo00OoOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Oo0OO0000oooo , IIII1iII , ii1III11 in os . walk ( Ooo00OoOOO ) :
   I1iiIIIi11 = 0
   I1iiIIIi11 += len ( ii1III11 )
   if 83 - 83: oo0O0oOOO00oO . O0 / i1II1I11 / I1I1i - II111iiii
   if 100 - 100: i1I
   if I1iiIIIi11 > 0 :
    if 46 - 46: OO0o / iIii1I11I1II1 % oo0O0oOOO00oO . iIii1I11I1II1 * oo0O0oOOO00oO
    iiI1IiI = xbmcgui . Dialog ( )
    if iiI1IiI . yesno ( "Delete Package Cache Files" , str ( I1iiIIIi11 ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: O0o0Oo - oo0O0oOOO00oO / O0 . o00OO0OOO0
     for i11i1 in ii1III11 :
      os . unlink ( os . path . join ( Oo0OO0000oooo , i11i1 ) )
     for ii11I1 in IIII1iII :
      shutil . rmtree ( os . path . join ( Oo0OO0000oooo , ii11I1 ) )
     iiI1IiI = xbmcgui . Dialog ( )
     iiI1IiI . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    iiI1IiI = xbmcgui . Dialog ( )
    iiI1IiI . ok ( IiII , "       No Packages to DELETE" )
 except :
  iiI1IiI = xbmcgui . Dialog ( )
  iiI1IiI . ok ( IiII , "Error Deleting Packages" )
 return
 if 45 - 45: o00OO0OOO0
def oOIIi1iiii1iI ( ) :
 iiI1IiI = xbmcgui . Dialog ( )
 Oo0oOOo = iiI1IiI . yesno ( 'Force Close Genie XXX' , 'You are about to close Genie XXX' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if Oo0oOOo == 0 : return
 elif Oo0oOOo == 1 : pass
 iIiiii = iI1I ( )
 Ii1iI111II1I1 ( "Platform: " + str ( iIiiii ) )
 os . _exit ( 1 )
 Ii1iI111II1I1 ( "Force close failed!  Trying alternate methods." )
 if iIiiii == 'osx' :
  Ii1iI111II1I1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iiI1IiI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIiiii == 'linux' :
  Ii1iI111II1I1 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iiI1IiI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIiiii == 'android' :
  Ii1iI111II1I1 ( "############ try android force close #################" )
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
  iiI1IiI . ok ( IiII , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif iIiiii == 'windows' :
  Ii1iI111II1I1 ( "############ try windows force close #################" )
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
  iiI1IiI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  Ii1iI111II1I1 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  Ii1iI111II1I1 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iiI1IiI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 89 - 89: oo0O0oOOO00oO - i1Iii % i1II1I11 % oo
def I1IiiiiI ( url ) :
 import urlresolver
 try :
  IIiii11i = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( IIiii11i , xbmcgui . ListItem ( Ii11iII1 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( Ii11iII1 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def iI1I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 100 - 100: i1Iii % iIii1I11I1II1 * II111iiii - oo0O0oOOO00oO
def Ii1iI111II1I1 ( log ) :
 xbmc . log ( "[%s]: %s" % ( IiII , log ) )
 if not os . path . exists ( o0oO0 ) : os . makedirs ( o0oO0 )
 if not os . path . exists ( o00 ) : i11i1 = open ( o00 , 'w' ) ; i11i1 . close ( )
 with open ( o00 , 'a' ) as i11i1 :
  oo00O00oO000o = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  i11i1 . write ( oo00O00oO000o . rstrip ( '\r\n' ) + '\n' )
  if 71 - 71: O0o0Oo - i1Iii / OO0o * OO0o / i1IIi . i1IIi
def iiIiIIIiiI ( ) :
 try :
  ooo000ooO0000 = getSet ( "core-player" )
  if ( ooo000ooO0000 == 'DVDPLAYER' ) : oOoooo000Oo00 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ooo000ooO0000 == 'MPLAYER' ) : oOoooo000Oo00 = xbmc . PLAYER_CORE_MPLAYER
  elif ( ooo000ooO0000 == 'PAPLAYER' ) : oOoooo000Oo00 = xbmc . PLAYER_CORE_PAPLAYER
  else : oOoooo000Oo00 = xbmc . PLAYER_CORE_AUTO
 except : oOoooo000Oo00 = xbmc . PLAYER_CORE_AUTO
 return oOoooo000Oo00
 return True
 if 93 - 93: O0o0Oo / ooOoo0O / iIii1I11I1II1 % o00OO0OOO0 % o00OO0OOO0
 if 40 - 40: i11iIiiIii * o00OO0OOO0 - i1IIi * o00OO0OOO0 - IIIii1I1 . i1IIi
def iIi1ii1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 99 - 99: O0 * IIIii1I1
 Ooooooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1IIIiI1I1ii1 = True
 iiiI1I1iIIIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiI1I1iIIIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiI1I1iIIIi1 . setProperty ( "Fanart_Image" , fanart )
 I1IIIiI1I1ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooooo , listitem = iiiI1I1iIIIi1 , isFolder = True )
 return I1IIIiI1I1ii1
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / IIIii1I1 % II111iiii % i1IIi / i11iIiiIii
def I11i1 ( name , url , mode , iconimage , fanart , description ) :
 if 58 - 58: i1II1I11 . II111iiii + ooo - i11iIiiIii / II111iiii / O0
 Ooooooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1IIIiI1I1ii1 = True
 iiiI1I1iIIIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiI1I1iIIIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiI1I1iIIIi1 . setProperty ( "Fanart_Image" , fanart )
 I1IIIiI1I1ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooooo , listitem = iiiI1I1iIIIi1 , isFolder = False )
 return I1IIIiI1I1ii1
def O0OOO0OOoO0O ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ooooooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1IIIiI1I1ii1 = True
 iiiI1I1iIIIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiI1I1iIIIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiI1I1iIIIi1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oOOoOo = [ ]
  if showcontext == 'fav' :
   oOOoOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in II :
   oOOoOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiiI1I1iIIIi1 . addContextMenuItems ( oOOoOo )
 I1IIIiI1I1ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooooo , listitem = iiiI1I1iIIIi1 , isFolder = False )
 return I1IIIiI1I1ii1
def IIIi1I1IIii1II ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooooooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1IIIiI1I1ii1 = True
 iiiI1I1iIIIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiI1I1iIIIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oOOoOo = [ ]
  oOOoOo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oOOoOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in II :
   oOOoOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiiI1I1iIIIi1 . addContextMenuItems ( oOOoOo )
 I1IIIiI1I1ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooooo , listitem = iiiI1I1iIIIi1 , isFolder = True )
 return I1IIIiI1I1ii1
def iII11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooooooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1IIIiI1I1ii1 = True
 iiiI1I1iIIIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiI1I1iIIIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oOOoOo = [ ]
  oOOoOo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oOOoOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in II :
   oOOoOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiiI1I1iIIIi1 . addContextMenuItems ( oOOoOo )
 I1IIIiI1I1ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooooo , listitem = iiiI1I1iIIIi1 , isFolder = False )
 return I1IIIiI1I1ii1
 if 89 - 89: II111iiii + i1IIi + II111iiii
def IiII1II11I ( ) :
 O0Oo00O = [ ]
 OOo0o000oO = sys . argv [ 2 ]
 if len ( OOo0o000oO ) >= 2 :
  oO0o00oOOooO0 = sys . argv [ 2 ]
  OOOoO000 = oO0o00oOOooO0 . replace ( '?' , '' )
  if ( oO0o00oOOooO0 [ len ( oO0o00oOOooO0 ) - 1 ] == '/' ) :
   oO0o00oOOooO0 = oO0o00oOOooO0 [ 0 : len ( oO0o00oOOooO0 ) - 2 ]
  oOOOO = OOOoO000 . split ( '&' )
  O0Oo00O = { }
  for IiIi1ii111i1 in range ( len ( oOOOO ) ) :
   i1i1i1I = { }
   i1i1i1I = oOOOO [ IiIi1ii111i1 ] . split ( '=' )
   if ( len ( i1i1i1I ) ) == 2 :
    O0Oo00O [ i1i1i1I [ 0 ] ] = i1i1i1I [ 1 ]
    if 83 - 83: ooo + OoooooooOO
 return O0Oo00O
 if 22 - 22: Ii % oo0O0oOOO00oO * OoooooooOO - oo / iIii1I11I1II1
 if 86 - 86: OoooooooOO . oo0O0oOOO00oO % OO0o / IIIii1I1 * oo0O0oOOO00oO / oo
oO0o00oOOooO0 = IiII1II11I ( )
OO00Oo = None
Ii11iII1 = None
oOoOOo000oOoO0 = None
OoOo00o0OO = None
ii1IIIIiI11 = None
iI1IIIii = None
I1i11ii11 = None
if 81 - 81: I1I1i - IIIii1I1 % i1Iii - i1I / i1II1I11
if 4 - 4: OoooooooOO - i1IIi % Ii - I1I1i * oo
try :
 I1i11ii11 = int ( oO0o00oOOooO0 [ "fav_mode" ] )
except :
 pass
 if 85 - 85: OoooooooOO * iIii1I11I1II1 . oo0O0oOOO00oO / OoooooooOO % ooOoo0O % O0
try :
 OO00Oo = urllib . unquote_plus ( oO0o00oOOooO0 [ "url" ] )
except :
 pass
try :
 Ii11iII1 = urllib . unquote_plus ( oO0o00oOOooO0 [ "name" ] )
except :
 pass
try :
 OoOo00o0OO = urllib . unquote_plus ( oO0o00oOOooO0 [ "iconimage" ] )
except :
 pass
try :
 oOoOOo000oOoO0 = int ( oO0o00oOOooO0 [ "mode" ] )
except :
 pass
try :
 ii1IIIIiI11 = urllib . unquote_plus ( oO0o00oOOooO0 [ "fanart" ] )
except :
 pass
try :
 iI1IIIii = urllib . unquote_plus ( oO0o00oOOooO0 [ "description" ] )
except :
 pass
 if 36 - 36: Ii / II111iiii / iiiiiIIii / iiiiiIIii + O0o0Oo
 if 95 - 95: iiiiiIIii
print str ( i1iiIIiiI111 ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( oOoOOo000oOoO0 )
print "URL: " + str ( OO00Oo )
print "Name: " + str ( Ii11iII1 )
print "IconImage: " + str ( OoOo00o0OO )
if 51 - 51: II111iiii + iiiiiIIii . i1IIi . O0o0Oo + OO0o * ooOoo0O
if 72 - 72: ooo + ooo / II111iiii . OoooooooOO % Ii
def III ( content , viewType ) :
 if 41 - 41: i11iIiiIii + i1II1I11 / ooOoo0O . OoooooooOO % ooo % i1IIi
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OOO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OOO . getSetting ( viewType ) )
  if 70 - 70: i1II1I11 . OoooooooOO - oo0O0oOOO00oO
  if 30 - 30: O0o0Oo % ooOoo0O
if oOoOOo000oOoO0 == None : O0OO00o0OO ( )
elif oOoOOo000oOoO0 == 1 : Genres ( )
elif oOoOOo000oOoO0 == 2 : Lists ( OO00Oo , OoOo00o0OO )
elif oOoOOo000oOoO0 == 3 : all_mov ( )
elif oOoOOo000oOoO0 == 4 : Search ( )
elif oOoOOo000oOoO0 == 5 : iiII1i11i ( )
elif oOoOOo000oOoO0 == 6 : i1iiiii1 ( OO00Oo )
elif oOoOOo000oOoO0 == 7 : oO0oo ( OO00Oo )
elif oOoOOo000oOoO0 == 8 : oOIIi1iiii1iI ( )
elif oOoOOo000oOoO0 == 9 : o0 ( )
elif oOoOOo000oOoO0 == 10 : MyAccDetails ( )
elif oOoOOo000oOoO0 == 11 : TvGuide ( )
elif oOoOOo000oOoO0 == 12 : I11II1i ( )
elif oOoOOo000oOoO0 == 13 : ReCreate_Addon_ini ( )
elif oOoOOo000oOoO0 == 14 : Get_Ultimate_playlinks_data ( OO00Oo )
elif oOoOOo000oOoO0 == 144 : Get_List_playlinks ( OO00Oo )
elif oOoOOo000oOoO0 == 15 : I1IiiiiI ( OO00Oo )
elif oOoOOo000oOoO0 == 222 : I1IiiiiI ( OO00Oo )
elif oOoOOo000oOoO0 == 16 : Streams_Menu ( )
elif oOoOOo000oOoO0 == 17 : Live_Events ( Ii11iII1 )
elif oOoOOo000oOoO0 == 18 : o0OOO . openSettings ( sys . argv [ 0 ] )
elif oOoOOo000oOoO0 == 19 : WIZ ( )
elif oOoOOo000oOoO0 == 20 : WIZARD ( OO00Oo )
elif oOoOOo000oOoO0 == 30 : CatchUp ( )
elif oOoOOo000oOoO0 == 31 : CatchUpPlay ( OO00Oo )
elif oOoOOo000oOoO0 == 40 : VOD_Menu ( )
elif oOoOOo000oOoO0 == 41 : Get_VOD_playlinks ( OO00Oo )
elif oOoOOo000oOoO0 == 21 : show_inf ( OO00Oo )
elif oOoOOo000oOoO0 == 22 : get_info ( OO00Oo )
elif oOoOOo000oOoO0 == 50 : RADIO ( )
elif oOoOOo000oOoO0 == 51 : RADIO2 ( OO00Oo )
elif oOoOOo000oOoO0 == 50000 : OO ( )
elif oOoOOo000oOoO0 == 50001 : O0OOoOOO0oO ( )
elif oOoOOo000oOoO0 == 50002 : ooo0OOO ( OO00Oo )
elif oOoOOo000oOoO0 == 60001 : apkmasterMenu ( )
elif oOoOOo000oOoO0 == 60002 : apkInstaller ( Ii11iII1 , OO00Oo )
elif oOoOOo000oOoO0 == 211 : Oooo0O ( )
elif oOoOOo000oOoO0 == 212 : oooiiI ( )
elif oOoOOo000oOoO0 == 213 : iIII ( )
elif oOoOOo000oOoO0 == 214 : iII1i11IIi1i ( )
elif oOoOOo000oOoO0 == 10100 : OOO00O ( )
elif oOoOOo000oOoO0 == 101001 : i1iIIIi1i ( OO00Oo )
elif oOoOOo000oOoO0 == 10105 : oO0000OOo00 ( OO00Oo )
elif oOoOOo000oOoO0 == 10106 : iiIi1IIiIi ( OO00Oo )
elif oOoOOo000oOoO0 == 10104 : iIiIIi1 ( OO00Oo )
elif oOoOOo000oOoO0 == 10107 : iI1iIIiiii ( )
elif oOoOOo000oOoO0 == 10103 : oOO00Oo ( OO00Oo )
elif oOoOOo000oOoO0 == 10108 : o00Oo0oooooo ( OO00Oo )
elif oOoOOo000oOoO0 == 9999999 : Oo0OoO00oOO0o ( )
elif oOoOOo000oOoO0 == 19999999 : iII ( )
elif oOoOOo000oOoO0 == 100110 : O0oOO0 ( OO00Oo )
elif oOoOOo000oOoO0 == 100111 : O0ii1ii1ii ( OO00Oo )
elif oOoOOo000oOoO0 == 100112 : o000O0o ( OO00Oo )
elif oOoOOo000oOoO0 == 100113 : iIiIIIi ( OO00Oo )
elif oOoOOo000oOoO0 == 100114 : O0ooo0O0oo0 ( OO00Oo )
elif oOoOOo000oOoO0 == 100115 : I1I1IiI1 ( OO00Oo )
elif oOoOOo000oOoO0 == 100117 : oo0oOo ( OO00Oo )
elif oOoOOo000oOoO0 == 100118 : oo00O00oO ( OO00Oo )
elif oOoOOo000oOoO0 == 100120 : III1iII1I1ii ( OO00Oo )
elif oOoOOo000oOoO0 == 1001200 : oOOo0 ( OO00Oo )
elif oOoOOo000oOoO0 == 1001133 : IIIII ( )
elif oOoOOo000oOoO0 == 300000000 : II111ii1II1i ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
