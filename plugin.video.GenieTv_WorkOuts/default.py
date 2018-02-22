# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
from imports import yt
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
IiII1IiiIiI1 = 'plugin.video.GenieTv_WorkOuts'
iIiiiI1IiI1I1 = 'plugin.video.GenieTv_WorkOuts'
o0OoOoOO00 = "0.0.1"
I11i = xbmc . translatePath ( 'special://home/addons/' )
O0O = base64 . decodestring
Oo = datetime . now ( )
I1ii11iIi11i = xbmc . translatePath ( 'special://logpath/' )
I1IiI = xbmc . translatePath ( 'special://home/addonsbroke/' )
o0OOO = xbmcaddon . Addon ( id = iIiiiI1IiI1I1 )
iIiiiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
Iii1ii1II11i = 'plugin.video.GenieTv_WorkOuts'
iI111iI = xbmcgui . DialogProgress ( )
IiII = "GenieTv WorkOuts"
iI1Ii11111iIi = Net ( )
i1i1II = xbmc . translatePath ( 'special://home/' )
O0O = base64 . decodestring
O0oo0OO0 = xbmc . translatePath ( 'special://profile/' )
I1i1iiI1 = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
iiIIIII1i1iI = os . path . join ( i1i1II , 'userdata' )
o0oO0 = os . path . join ( iiIIIII1i1iI , 'addon_data' , IiII1IiiIiI1 )
oo00 = os . path . join ( I11i , 'packages' )
o00 = O0O ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcy8=' )
Oo0oO0ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'icon.png' ) )
o0oOoO00o = "GenieTv"
i1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ2VuaWV0dl9hcnQvYmVuc19hcnQv' )
oOOoo00O0O = 'WEBSITE'
i1111 = ( O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
i11 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTv_WorkOuts' )
I11 = xbmc . translatePath ( 'special://thumbnails' ) ;
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'fanart.jpg' ) )
oOo0oooo00o = o0OOO . getLocalizedString
oO0o0o0ooO0oO = CookieJar ( )
oo0o0O00 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( oO0o0o0ooO0oO ) )
oo0o0O00 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
oO = int ( sys . argv [ 1 ] )
i1iiIIiiI111 = xbmc . translatePath ( o0OOO . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iiIIIII1i1iI = xbmc . translatePath ( 'special://home/userdata/' )
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
i1iiIII111ii = i11 + '/addons.ini'
i1iIIi1 = xbmcgui . Dialog ( )
ii11iIi1I = xbmcgui . Dialog ( )
if os . path . exists ( oooOOOOO ) == True :
 iI111I11I1I1 = open ( oooOOOOO ) . read ( )
else : iI111I11I1I1 = [ ]
if 55 - 55: iI1I % iiiIi - OO / i1I111I - I1I1IIiiIiI1 . iiIiIIi
if 65 - 65: iii1I1
if 84 - 84: III1I11iiii1I . IiI1i11iii1
if 96 - 96: Ii11Ii11I % I11i1I + O00o0OO
def I11i1 ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]Collections[/COLOR]' , O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsvZml0bmVzcy9tYWluLnBocA==' ) , 7084 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Search WorkOuts[/COLOR]' , o00 , 4 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]All WorkOuts[/COLOR]' , o00 , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]By Duration[/COLOR]' , '' , 1001 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]By Calorie Burn[/COLOR]' , '' , 1002 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]By Difficulty[/COLOR]' , '' , 1003 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]By Trainer[/COLOR]' , '' , 1004 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]By Body Focus[/COLOR]' , '' , 1005 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]By Training Type[/COLOR]' , '' , 1006 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]By Equipment[/COLOR]' , '' , 1007 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Mixed Filters[/COLOR]' , o00 , 2001 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
def o0 ( url ) :
 I11II1i = IIIII ( url )
 ooooooO0oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11II1i )
 for url , IIiiiiiiIi1I1 , I1IIIii , oOoOooOo0o0 , OOOO in ooooooO0oo :
  if '.php' in url :
   iIi1ii1I1 ( OOOO , url , 7084 , IIiiiiiiIi1I1 , oOoOooOo0o0 , I1IIIii )
  else :
   OOO00 ( OOOO , url , 15 , IIiiiiiiIi1I1 , oOoOooOo0o0 , I1IIIii )
def iiiiiIIii ( ) :
 O000OO0 = ii11iIi1I . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11iii1Ii = 'https://www.fitnessblender.com/search?keywords=' + O000OO0 . replace ( ' ' , '%20' )
 I11II1i = IIIII ( I11iii1Ii )
 I1IIiiIiii = re . compile ( '<img.+?src="([^"]*)".+?<a href="([^"]*)">(.+?)</a>.+?<div class="blurb">(.+?)</div>' , re . DOTALL ) . findall ( I11II1i )
 for IIiiiiiiIi1I1 , O000oo0O , OOOO , I1IIIii in I1IIiiIiii :
  iIi1ii1I1 ( '[COLORsteelblue]' + OOOO + '[/COLOR]' , 'https://www.fitnessblender.com' + O000oo0O , 7086 , IIiiiiiiIi1I1 , '' , ( I1IIIii ) . replace ( '<em>' , '' ) . replace ( '</em>' , '' ) )
  if 66 - 66: OoOo00o / IIIii1II1II % OoooooooOO + Ii11Ii11I + Ii11Ii11I - i1IIi
def O0o0Ooo ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]1 - 10 Minutes[/COLOR]' , o00 + '?minlength=1&maxlength=10' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]10 - 20 Minutes[/COLOR]' , o00 + '?minlength=10&maxlength=20' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]20 - 30 Minutes[/COLOR]' , o00 + '?minlength=20&maxlength=30' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]30 - 40 Minutes[/COLOR]' , o00 + '?minlength=30&maxlength=40' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]40 - 50 Minutes[/COLOR]' , o00 + '?minlength=40&maxlength=50' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]50 - 60 Minutes[/COLOR]' , o00 + '?minlength=50&maxlength=60' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 if 56 - 56: IIIii1II1II . i1I111I * I11i1I . i1I111I
 if 72 - 72: I11i1I / i1IIi * iiiIi - OoOo00o
def Oo0O0O0ooO0O ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]0 - 100 Calories[/COLOR]' , o00 + '?minburn=10&maxburn=100' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]100 - 200 Calories[/COLOR]' , o00 + '?minburn=100&maxburn=200' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]200 - 300 Calories[/COLOR]' , o00 + '?minburn=200&maxburn=300' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]300 - 400 Calories[/COLOR]' , o00 + '?minburn=300&maxburn=400' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]400 - 500 Calories[/COLOR]' , o00 + '?minburn=400&maxburn=500' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]500 - 1000 Calories[/COLOR]' , o00 + '?minburn=500&maxburn=1000' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 if 15 - 15: iiIiIIi + i1I111I - OoooooooOO / III1I11iiii1I
 if 58 - 58: i11iIiiIii % IiI1i11iii1
def OO00Oo ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]All WorkOuts[/COLOR]' , o00 + '?difficulty%5B%5D=1' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]All WorkOuts[/COLOR]' , o00 + '?difficulty%5B%5D=2' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]All WorkOuts[/COLOR]' , o00 + '?difficulty%5B%5D=3' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]All WorkOuts[/COLOR]' , o00 + '?difficulty%5B%5D=4' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]All WorkOuts[/COLOR]' , o00 + '?difficulty%5B%5D=5' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 if 51 - 51: O00o0OO * I1I1IIiiIiI1 + IiI1i11iii1 + OO
 if 66 - 66: i1I111I
def oO000Oo000 ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]Male[/COLOR]' , o00 + '?trainer%5B%5D=Male' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Female[/COLOR]' , o00 + '?trainer%5B%5D=Female' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Both[/COLOR]' , o00 + '?trainer%5B%5D=Both' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 if 4 - 4: iii1I1
 if 93 - 93: OO % iii1I1 . OO * OoOo00o % Ii11Ii11I . II111iiii
def iI1ii1Ii ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]Upper Body[/COLOR]' , o00 + '?focus%5B%5D=1' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Core[/COLOR]' , o00 + '?focus%5B%5D=2' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Lower Body[/COLOR]' , o00 + '?focus%5B%5D=3' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Total Workout[/COLOR]' , o00 + '?focus%5B%5D=4' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 if 92 - 92: i1I111I
 if 26 - 26: I11i1I . OoOo00o
def oOOOOo0 ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]HIIT[/COLOR]' , o00 + '?trainingtype%5B%5D=8' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Strength Training[/COLOR]' , o00 + '?trainingtype%5B%5D=13' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Pilates[/COLOR]' , o00 + '?trainingtype%5B%5D=11' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Cardiovascular[/COLOR]' , o00 + '?trainingtype%5B%5D=7' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Yoga / Flexibility[/COLOR]' , o00 + '?trainingtype%5B%5D=16' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Low Impact[/COLOR]' , o00 + '?trainingtype%5B%5D=10' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Warm Up / Cool Down[/COLOR]' , o00 + '?trainingtype%5B%5D=15' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Kettle Ball[/COLOR]' , o00 + '?trainingtype%5B%5D=9' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Toning[/COLOR]' , o00 + '?trainingtype%5B%5D=14' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 if 20 - 20: i1IIi + iiIiIIi - IIIii1II1II
 if 30 - 30: II111iiii - III1I11iiii1I - i11iIiiIii % i1I111I - II111iiii * Ii11Ii11I
def oO00O0O0O ( ) :
 iIi1ii1I1 ( '[COLORsteelblue]No Equipment[/COLOR]' , o00 + '?equipment%5B%5D=26' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]DumbBell[/COLOR]' , o00 + '?equipment%5B%5D=20' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Mat[/COLOR]' , o00 + '?equipment%5B%5D=24' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Bench[/COLOR]' , o00 + '?equipment%5B%5D=19' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Excercise Belt[/COLOR]' , o00 + '?equipment%5B%5D=21' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Jump Rope[/COLOR]' , o00 + '?equipment%5B%5D=22' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Kettlebell[/COLOR]' , o00 + '?equipment%5B%5D=23' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Medicine Ball[/COLOR]' , o00 + '?equipment%5B%5D=25' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 iIi1ii1I1 ( '[COLORsteelblue]Physio-Ball[/COLOR]' , o00 + '?equipment%5B%5D=27' , 7085 , i1 + 'Fitness.png' , Oo0o0000o0o0 , '' )
 if 31 - 31: IiI1i11iii1 - II111iiii . IiI1i11iii1
 if 18 - 18: I1I1IIiiIiI1
 if 98 - 98: I11i1I * I11i1I / I11i1I + IiI1i11iii1
def ii111111I1iII ( url ) :
 url = url
 O00ooo0O0 = [ '[COLORsteelblue]Any Duration[/COLOR]' , '[COLORsteelblue]0 - 10 Minutes[/COLOR]' , '[COLORsteelblue]10 - 20 Minutes[/COLOR]' , '[COLORsteelblue]20 - 30 Minutes[/COLOR]' , '[COLORsteelblue]30 - 40 Minutes[/COLOR]' , '[COLORsteelblue]40 - 50 Minutes[/COLOR]' , '[COLORsteelblue]50 - 60 Minutes[/COLOR]' ]
 i1iIi1iIi1i = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Duration[/COLOR]' , O00ooo0O0 )
 if i1iIi1iIi1i == 0 :
  I1I1iIiII1 ( url + '' )
 if i1iIi1iIi1i == 1 :
  I1I1iIiII1 ( url + '?minlength=1&maxlength=10' )
 if i1iIi1iIi1i == 2 :
  I1I1iIiII1 ( url + '?minlength=10&maxlength=20' )
 if i1iIi1iIi1i == 3 :
  I1I1iIiII1 ( url + '?minlength=20&maxlength=30' )
 if i1iIi1iIi1i == 4 :
  I1I1iIiII1 ( url + '?minlength=30&maxlength=40' )
 if i1iIi1iIi1i == 5 :
  I1I1iIiII1 ( url + '?minlength=40&maxlength=50' )
 if i1iIi1iIi1i == 5 :
  I1I1iIiII1 ( url + '?minlength=50&maxlength=60' )
  if 4 - 4: IIIii1II1II + O0 * III1I11iiii1I
def I1I1iIiII1 ( url ) :
 url = url
 O00ooo0O0 = [ '[COLORsteelblue]Any Count[/COLOR]' , '[COLORsteelblue]0 - 100 Calories[/COLOR]' , '[COLORsteelblue]100 - 200 Calories[/COLOR]' , '[COLORsteelblue]200 - 300 Calories[/COLOR]' , '[COLORsteelblue]300 - 400 Calories[/COLOR]' , '[COLORsteelblue]400 - 500 Calories[/COLOR]' , '[COLORsteelblue]500+ Calories[/COLOR]' ]
 i1iIi1iIi1i = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Calorie Burn[/COLOR]' , O00ooo0O0 )
 if i1iIi1iIi1i == 0 :
  OOoo0O ( url + '' )
 if i1iIi1iIi1i == 1 :
  OOoo0O ( url + '&minburn=10&maxburn=100' )
 if i1iIi1iIi1i == 2 :
  OOoo0O ( url + '&minburn=100&maxburn=200' )
 if OOoo0O == 3 :
  I1I1iIiII1 ( url + '&minburn=20&maxburn=300' )
 if OOoo0O == 4 :
  OOoo0O ( url + '&minburn=30&maxburn=400' )
 if i1iIi1iIi1i == 5 :
  OOoo0O ( url + '&minburn=40&maxburn=500' )
 if i1iIi1iIi1i == 5 :
  OOoo0O ( url + '&minburn=500' )
  if 67 - 67: i11iIiiIii - i1IIi % iiIiIIi . O0
def OOoo0O ( url ) :
 url = url
 O00ooo0O0 = [ '[COLORsteelblue]Any Duration[/COLOR]' , '[COLORsteelblue]Level 1[/COLOR]' , '[COLORsteelblue]Level 2[/COLOR]' , '[COLORsteelblue]Level 3[/COLOR]' , '[COLORsteelblue]Level 4[/COLOR]' , '[COLORsteelblue]Level 5[/COLOR]' ]
 i1iIi1iIi1i = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Difficulty[/COLOR]' , O00ooo0O0 )
 if i1iIi1iIi1i == 0 :
  o0oo ( url + '' )
 if i1iIi1iIi1i == 1 :
  o0oo ( url + '&difficulty%5B%5D=1' )
 if i1iIi1iIi1i == 2 :
  o0oo ( url + '&difficulty%5B%5D=2' )
 if i1iIi1iIi1i == 3 :
  o0oo ( url + '&difficulty%5B%5D=3' )
 if i1iIi1iIi1i == 4 :
  o0oo ( url + '&difficulty%5B%5D=4' )
 if i1iIi1iIi1i == 5 :
  o0oo ( url + '&difficulty%5B%5D=5' )
  if 91 - 91: O00o0OO
def o0oo ( url ) :
 url = url
 O00ooo0O0 = [ '[COLORsteelblue]Any Duration[/COLOR]' , '[COLORsteelblue]Upper Body[/COLOR]' , '[COLORsteelblue]Core[/COLOR]' , '[COLORsteelblue]Lower Body[/COLOR]' , '[COLORsteelblue]Total Body[/COLOR]' ]
 i1iIi1iIi1i = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Focus[/COLOR]' , O00ooo0O0 )
 if i1iIi1iIi1i == 0 :
  iiIii ( url + '' )
 if i1iIi1iIi1i == 1 :
  iiIii ( url + '&focus%5B%5D=1' )
 if i1iIi1iIi1i == 2 :
  iiIii ( url + '&focus%5B%5D=2' )
 if i1iIi1iIi1i == 3 :
  iiIii ( url + '&focus%5B%5D=3' )
 if i1iIi1iIi1i == 4 :
  iiIii ( url + '&focus%5B%5D=4' )
  if 79 - 79: OoooooooOO / O0
def iiIii ( url ) :
 url = url
 O00ooo0O0 = [ '[COLORsteelblue]Any Trainer[/COLOR]' , '[COLORsteelblue]Male[/COLOR]' , '[COLORsteelblue]Female[/COLOR]' , '[COLORsteelblue]Both[/COLOR]' ]
 i1iIi1iIi1i = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Trainer[/COLOR]' , O00ooo0O0 )
 if i1iIi1iIi1i == 0 :
  OO0OoO0o00 ( url + '' )
 if i1iIi1iIi1i == 1 :
  OO0OoO0o00 ( url + '&trainer%5B%5D=Male' )
 if i1iIi1iIi1i == 2 :
  OO0OoO0o00 ( url + '&trainer%5B%5D=Female' )
 if i1iIi1iIi1i == 3 :
  OO0OoO0o00 ( url + '&trainer%5B%5D=Both' )
  if 53 - 53: O0 * OO + III1I11iiii1I
def OO0OoO0o00 ( url ) :
 url = url
 O00ooo0O0 = [ '[COLORsteelblue]Any Type[/COLOR]' , '[COLORsteelblue]HIIT[/COLOR]' , '[COLORsteelblue]Strength Training[/COLOR]' , '[COLORsteelblue]Pilates[/COLOR]' , '[COLORsteelblue]Cardiovascular[/COLOR]' , '[COLORsteelblue]Yoga / Flexibility[/COLOR]' , '[COLORsteelblue]Low Impact[/COLOR]' , '[COLORsteelblue]Warm Up / Cool Down[/COLOR]' , '[COLORsteelblue]Kettle Ball[/COLOR]' , '[COLORsteelblue]Toning[/COLOR]' ]
 i1iIi1iIi1i = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Training Type[/COLOR]' , O00ooo0O0 )
 if i1iIi1iIi1i == 0 :
  Ii ( url + '' )
 if i1iIi1iIi1i == 1 :
  Ii ( url + '&trainingtype%5B%5D=8' )
 if i1iIi1iIi1i == 2 :
  Ii ( url + '&trainingtype%5B%5D=13' )
 if i1iIi1iIi1i == 3 :
  Ii ( url + '&trainingtype%5B%5D=11' )
 if i1iIi1iIi1i == 4 :
  Ii ( url + '&trainingtype%5B%5D=7' )
 if i1iIi1iIi1i == 5 :
  Ii ( url + '&trainingtype%5B%5D=16' )
 if i1iIi1iIi1i == 6 :
  Ii ( url + '&trainingtype%5B%5D=10' )
 if i1iIi1iIi1i == 7 :
  Ii ( url + '&trainingtype%5B%5D=15' )
 if i1iIi1iIi1i == 8 :
  Ii ( url + '&trainingtype%5B%5D=9' )
 if i1iIi1iIi1i == 9 :
  Ii ( url + '&trainingtype%5B%5D=14' )
  if 61 - 61: II111iiii
def Ii ( url ) :
 url = url
 O00ooo0O0 = [ '[COLORsteelblue]Any Equipment[/COLOR]' , '[COLORsteelblue]No Equipment[/COLOR]' , '[COLORsteelblue]DumbBell[/COLOR]' , '[COLORsteelblue]Mat[/COLOR]' , '[COLORsteelblue]Bench[/COLOR]' , '[COLORsteelblue]Excercise Band[/COLOR]' , '[COLORsteelblue]Jump Rope[/COLOR]' , '[COLORsteelblue]Kettlebell[/COLOR]' , '[COLORsteelblue]Medicine Ball[/COLOR]' , '[COLORsteelblue]Physio Belt[/COLOR]' ]
 i1iIi1iIi1i = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Equipment[/COLOR]' , O00ooo0O0 )
 if i1iIi1iIi1i == 0 :
  O0OOO ( url + '' )
 if i1iIi1iIi1i == 1 :
  O0OOO ( url + '&equipment%5B%5D=26' )
 if i1iIi1iIi1i == 2 :
  O0OOO ( url + '&equipment%5B%5D=20' )
 if i1iIi1iIi1i == 3 :
  O0OOO ( url + '&equipment%5B%5D=24' )
 if i1iIi1iIi1i == 4 :
  O0OOO ( url + '&equipment%5B%5D=19' )
 if i1iIi1iIi1i == 5 :
  O0OOO ( url + '&equipment%5B%5D=21' )
 if i1iIi1iIi1i == 6 :
  O0OOO ( url + '&equipment%5B%5D=22' )
 if i1iIi1iIi1i == 7 :
  O0OOO ( url + '&equipment%5B%5D=23' )
 if i1iIi1iIi1i == 8 :
  O0OOO ( url + '&equipment%5B%5D=25' )
 if i1iIi1iIi1i == 9 :
  O0OOO ( url + '&equipment%5B%5D=27' )
  if 10 - 10: III1I11iiii1I * IiI1i11iii1 % i1I111I / iI1I / i1I111I
  if 42 - 42: OO
  if 67 - 67: OoOo00o . I11i1I . O0
def O0OOO ( url ) :
 IIIIiiII111 = IIIII ( url )
 I1IIiiIiii = re . compile ( '"id":.+?,"title":(.+?),"is_featured":1,"minutes":(.+?),"burnmin":(.+?),"burnmax":(.+?),"burnavg":(.+?),"difficulty":(.+?),"image":"([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"' , re . DOTALL ) . findall ( IIIIiiII111 )
 OOoOoo = re . compile ( '"next_page_url":"([^"]*)"' ) . findall ( IIIIiiII111 )
 for OOOO , time , oO0000OOo00 , iiIi1IIiIi , oOO00Oo , i1iIIIi1i , IIiiiiiiIi1I1 , url , iI1iIIiiii , i1iI11i1ii11 in I1IIiiIiii :
  iIi1ii1I1 ( ( OOOO ) . replace ( '"' , '' ) , 'https://www.fitnessblender.com/videos/' + url , 7086 , 'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-' + IIiiiiiiIi1I1 , '' , ( 'Calorie burn:[CR]' + oO0000OOo00 + ' - ' + iiIi1IIiIi + ' Average = ' + oOO00Oo + '[CR][CR]Difficulty = ' + i1iIIIi1i + '[CR][CR]Equipment Needed: ' + iI1iIIiiii + '[CR][CR]Focus: ' + i1iI11i1ii11 ) . replace ( '"' , '' ) )
  OOooo0O00o ( 'tvshows' , 'Media Info 3' )
 for url in OOoOoo :
  oOOoOooOo ( 'NEXT' , ( o00 + url ) . replace ( '\/' , '' ) , 7085 , i1 + 'Next.png' )
  if 51 - 51: IiI1i11iii1 + I11i1I % iIii1I11I1II1 / iii1I1 / III1I11iiii1I % OoooooooOO
def o0O0OOO0Ooo ( url , iconimage , description ) :
 I11II1i = IIIII ( url )
 IIiiiiiiIi1I1 = iconimage
 I1IIIii = description
 I1IIiiIiii = re . compile ( '<div class="responsive-video">.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp' , re . DOTALL ) . findall ( I11II1i )
 for url in I1IIiiIiii :
  iiIiI ( 'PLAY' , url , 8043 , IIiiiiiiIi1I1 , '' , I1IIIii )
  OOooo0O00o ( 'tvshows' , 'Media Info 3' )
 I1 = re . compile ( '<div class="article__content">(.+?)</div>' , re . DOTALL ) . findall ( I11II1i )
 OOO00O0O = re . compile ( '<div class="article_body article__content">(.+?)</div>' , re . DOTALL ) . findall ( I11II1i )
 for iii in I1 :
  oOooOOOoOo = ( iii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  OOO00 ( 'INFO' , '' , 7087 , o00 + IIiiiiiiIi1I1 , '' , oOooOOOoOo )
 for iii in OOO00O0O :
  oOooOOOoOo = ( iii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  OOO00 ( 'INFO' , '' , 7087 , o00 + IIiiiiiiIi1I1 , '' , oOooOOOoOo )
  if 41 - 41: Ii11Ii11I - O0 - O0
def oO00OOoO00 ( INFO ) :
 IiI111111IIII ( 'info for workout' , INFO )
 if 37 - 37: OoOo00o / i1I111I
def IiI111111IIII ( title , msg ) :
 class i1I1iI1iIi111i ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 44 - 44: i1IIi % II111iiii + IiI1i11iii1
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 45 - 45: I11i1I / I11i1I + OoOo00o + IIIii1II1II
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 47 - 47: I1I1IIiiIiI1 + IIIii1II1II
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 82 - 82: II111iiii . O00o0OO - iIii1I11I1II1 - O00o0OO * II111iiii
 ooO0oOOooOo0 = i1I1iI1iIi111i ( "Textbox.xml" , o0OOO . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 ooO0oOOooOo0 . doModal ( )
 del ooO0oOOooOo0
 if 38 - 38: OoOo00o
 if 84 - 84: iIii1I11I1II1 % I11i1I / iIii1I11I1II1 % IiI1i11iii1
def ii ( title , message , times = 2000 , icon = Oo0oO0ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def OOooooO0Oo ( ) :
 OOiIiIIi1 = I1IIII1i ( )
 I1I11i = OOiIiIIi1 . replace ( I1ii11iIi11i , "" )
 if os . path . exists ( OOiIiIIi1 ) or not OOiIiIIi1 == False :
  Ii1I1I1i1Ii = open ( OOiIiIIi1 , mode = 'r' ) ; i1Oo0oO00o = Ii1I1I1i1Ii . read ( ) ; Ii1I1I1i1Ii . close ( )
  i1I1iI1iIi111i ( "%s - %s" % ( IiII , I1I11i ) , i1Oo0oO00o )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def I1IIII1i ( ) :
 i11I1II1I11i = False
 if os . path . exists ( os . path . join ( I1ii11iIi11i , 'xbmc.log' ) ) :
  i11I1II1I11i = os . path . join ( I1ii11iIi11i , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'kodi.log' ) ) :
  i11I1II1I11i = os . path . join ( I1ii11iIi11i , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'spmc.log' ) ) :
  i11I1II1I11i = os . path . join ( I1ii11iIi11i , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'tvmc.log' ) ) :
  i11I1II1I11i = os . path . join ( I1ii11iIi11i , 'tvmc.log' )
 return i11I1II1I11i
 if 61 - 61: iI1I - III1I11iiii1I . iii1I1 / III1I11iiii1I + iiiIi
 if 5 - 5: IIIii1II1II + IIIii1II1II / O0 * iiiIi - III1I11iiii1I % IIIii1II1II
 if 15 - 15: i11iIiiIii % Ii11Ii11I . iiiIi + iiIiIIi
 if 61 - 61: iiiIi * iiIiIIi % iiiIi - i1IIi - iIii1I11I1II1
 if 74 - 74: iiIiIIi + II111iiii / OO
def i1I1iI1iIi111i ( heading , announce ) :
 class IiI111111IIII ( ) :
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
   try : Ii1I1I1i1Ii = open ( announce ) ; oOo0O0Oo00oO = Ii1I1I1i1Ii . read ( )
   except : oOo0O0Oo00oO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOo0O0Oo00oO ) )
   return
 IiI111111IIII ( )
 IiI111111IIII ( )
 if 7 - 7: O00o0OO * OoOo00o % Ii11Ii11I - I1I1IIiiIiI1
def i1i ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 oOOoo00O00o = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + U + '%26password%3D' + Pass + '%26type%3Dm3u_plus%26output%3Dts'
 O0O00Oo = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + U + '%26password%3D' + Pass
 oooooo0O000o = 'http://piesustv.net:8000/enigma2.php?username=' + U + '&password=' + Pass + '&type=get_vod_categories'
 oooooo0O000o = IIIII ( oooooo0O000o )
 if not oooooo0O000o == "" :
  OoO = 'https://tinyurl.com/create.php?source=indexpage&url=' + oOOoo00O00o + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( OoO ) )
  ooO0O0O0ooOOO = 'https://tinyurl.com/create.php?source=indexpage&url=' + O0O00Oo + '&submit=Make+TinyURL%21&alias='
  oOOoo00O00o = IIIII ( OoO )
  O0O00Oo = IIIII ( ooO0O0O0ooOOO )
  xbmc . log ( str ( O0O00Oo ) )
  oOOo0O00o = regex_from_to ( oOOoo00O00o , '<div class="indent"><b>' , '</b>' )
  iIiIi11 = regex_from_to ( O0O00Oo , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLORorangered]WaveTv[/COLOR]' , '[COLORorangered]PLAYLIST URL: [/COLOR]%s' % oOOo0O00o , '' , '[COLORorangered]EPG URL: [/COLOR]%s' % iIiIi11 )
 else :
  return
def OOO ( ) :
 OOO00 ( '[COLORorangered]Setup Tv Guide[/COLOR]' , '' , 212 , i1 + '12.png' , Oo0o0000o0o0 , '' )
 OOO00 ( '[COLORorangered]Open Guide[/COLOR]' , '' , 213 , i1 + '13.png' , Oo0o0000o0o0 , '' )
 if 32 - 32: i1IIi / II111iiii . iiiIi
def oooOo0OOOoo0 ( ) :
 ivuesetup . iVueInt ( )
 if 51 - 51: iiiIi / i1I111I . III1I11iiii1I * I1I1IIiiIiI1 + OO * O00o0OO
def OOOoOo ( ) :
 O00o0 ( )
 return
 if 40 - 40: OoOo00o + OoooooooOO % I1I1IIiiIiI1 - iIii1I11I1II1 . iI1I
def O00o0 ( ) :
 if 48 - 48: I1I1IIiiIiI1 - iii1I1 / OoooooooOO
 OO0O0 = xbmcaddon . Addon ( 'plugin.video.WaveTv' )
 I11I11 = OO0O0 . getSetting ( id = 'User' )
 o000O0O = OO0O0 . getSetting ( id = 'Pass' )
 I1i1i1iii = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 I1111i = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 iIIii = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 o00O0O = "http://piesustv.net:8000/get.php?username=" + I11I11 + "&password=" + o000O0O + "&type=m3u_plus&output=ts"
 ii1iii1i = "http://piesustv.net:8000/xmltv.php?username=" + I11I11 + "&password=" + o000O0O + "&type=m3u_plus&output=ts"
 if 35 - 35: II111iiii % III1I11iiii1I . IIIii1II1II + IIIii1II1II % II111iiii % II111iiii
 xbmc . executeJSONRPC ( I1i1i1iii )
 xbmc . executeJSONRPC ( I1111i )
 xbmc . executeJSONRPC ( iIIii )
 if 72 - 72: II111iiii + i1IIi + I1I1IIiiIiI1
 OOOIIiI1i1i = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 OOOIIiI1i1i . setSetting ( id = 'm3uUrl' , value = o00O0O )
 OOOIIiI1i1i . setSetting ( id = 'epgUrl' , value = ii1iii1i )
 OOOIIiI1i1i . setSetting ( id = 'm3uCache' , value = "false" )
 OOOIIiI1i1i . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def O00Oo0 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 if 33 - 33: O0 * I1I1IIiiIiI1 - OoOo00o % OoOo00o
 if 18 - 18: OoOo00o / iiiIi * OoOo00o + OoOo00o * i11iIiiIii * iiIiIIi
 if 11 - 11: IIIii1II1II / i1I111I - O00o0OO * OoooooooOO + OoooooooOO . i1I111I
def i1I1i111Ii ( ) :
 OOO00 ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 OOO00 ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 OOO00 ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 OOO00 ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 OOO00 ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 if 67 - 67: iI1I . i1IIi
 if 27 - 27: IIIii1II1II % iI1I
 if 73 - 73: III1I11iiii1I
def ooO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def Ooo0oOooo0 ( url ) :
 if url == 'http://' : return False
 try :
  oOOOoo00 = urllib2 . Request ( url )
  oOOOoo00 . add_header ( 'User-Agent' , iIiiiI )
  iiIiIIIiiI = urllib2 . urlopen ( oOOOoo00 )
  iiIiIIIiiI . close ( )
 except Exception , iiI1IIIi :
  return iiI1IIIi
 return True
 if 47 - 47: iiiIi % IiI1i11iii1 % i11iIiiIii - O0 + IIIii1II1II
 if 94 - 94: OoOo00o
 if 4 - 4: Ii11Ii11I % iii1I1 * OO
def o0O0OOOOoOO0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv WorkOuts" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By GenieTv WorkOuts[/COLOR]" )
 return
 if 23 - 23: i11iIiiIii
def II1iIi11 ( url ) :
 print '###' + IiII + ' - DELETING Addons20.db ###'
 I11iiii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 O0i1iI = os . path . join ( I11iiii , 'Addons20.db' )
 try :
  os . remove ( O0i1iI )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== ' + IiII + ' - DELETING    ' + str ( O0i1iI ) + '    ==='
  ii11iIi1I . ok ( IiII , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "       No File To Remove" )
 return
 if 29 - 29: iI1I % III1I11iiii1I - iI1I / III1I11iiii1I . i1IIi
 if 31 - 31: OoOo00o
 if 88 - 88: OO - IIIii1II1II + III1I11iiii1I * iI1I % iIii1I11I1II1 + iiiIi
 if 76 - 76: iI1I * I11i1I % OoOo00o
 if 57 - 57: iIii1I11I1II1 - i1IIi / OoOo00o - O0 * OoooooooOO % II111iiii
def IIIII ( url ) :
 oOOOoo00 = urllib2 . Request ( url )
 oOOOoo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiIiIIIiiI = urllib2 . urlopen ( oOOOoo00 )
 Oo00OO0o0o00 = iiIiIIIiiI . read ( )
 iiIiIIIiiI . close ( )
 return Oo00OO0o0o00
def i1I1iI1iIi111i ( heading , announce ) :
 class IiI111111IIII ( ) :
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
   try : Ii1I1I1i1Ii = open ( announce ) ; oOo0O0Oo00oO = Ii1I1I1i1Ii . read ( )
   except : oOo0O0Oo00oO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOo0O0Oo00oO ) )
   return
 IiI111111IIII ( )
 IiI111111IIII ( )
def IiIi1I1 ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 IiIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IIIIiii1IIii , II1i11I , ii1I1IIii11 in os . walk ( IiIIi1 ) :
   O0o0oO = 0
   O0o0oO += len ( ii1I1IIii11 )
   if 38 - 38: iii1I1 % i1I111I + iiIiIIi . i11iIiiIii
   if 53 - 53: i11iIiiIii * I11i1I
   if O0o0oO > 0 :
    if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . I1I1IIiiIiI1 / II111iiii % iiiIi
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( O0o0oO ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: IIIii1II1II - III1I11iiii1I / I11i1I
     for Ii1I1I1i1Ii in ii1I1IIii11 :
      os . unlink ( os . path . join ( IIIIiii1IIii , Ii1I1I1i1Ii ) )
     for OoOOoooOO0O in II1i11I :
      shutil . rmtree ( os . path . join ( IIIIiii1IIii , OoOOoooOO0O ) )
     ii11iIi1I = xbmcgui . Dialog ( )
     ii11iIi1I . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    ii11iIi1I = xbmcgui . Dialog ( )
    ii11iIi1I . ok ( IiII , "       No Packages to DELETE" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "Error Deleting Packages please visit The Support Group, GenieTv WorkOuts on facebook" )
 ooo00Ooo ( url )
 return
def ooo00Ooo ( url ) :
 Oo0o0O00 = os . path . join ( O0oo0OO0 , 'addon_data' )
 ii1 = [
 ( Oo0o0O00 ) ,
 ( o0oO0 ) ,
 ( os . path . join ( i1i1II , 'cache' ) ) ,
 ( os . path . join ( i1i1II , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( o0oO0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( o0oO0 , 'plugin.video.GenieTv_WorkOuts' , 'Images' ) ) ,
 ( os . path . join ( Oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Oo0o0O00 , 'plugin.video.GenieTv_WorkOuts' , 'Images' ) ) ]
 if 39 - 39: Ii11Ii11I / IIIii1II1II . I1I1IIiiIiI1 % O0 * I11i1I + iI1I
 O0oo0O = 0
 if 36 - 36: III1I11iiii1I + O0 - Ii11Ii11I - O0 % IiI1i11iii1 . iii1I1
 for ooo in ii1 :
  if os . path . exists ( ooo ) and not ooo in [ o0oO0 , Oo0o0O00 ] :
   for IIIIiii1IIii , II1i11I , ii1I1IIii11 in os . walk ( ooo ) :
    O0o0oO = 0
    O0o0oO += len ( ii1I1IIii11 )
    if O0o0oO > 0 :
     for Ii1I1I1i1Ii in ii1I1IIii11 :
      if not Ii1I1I1i1Ii in I1i1iiI1 :
       try :
        os . unlink ( os . path . join ( IIIIiii1IIii , Ii1I1I1i1Ii ) )
       except :
        pass
      else : OOiIiIIi1 ( 'Ignore Log File: %s' % Ii1I1I1i1Ii )
     for OoOOoooOO0O in II1i11I :
      try :
       shutil . rmtree ( os . path . join ( IIIIiii1IIii , OoOOoooOO0O ) )
       O0oo0O += 1
       OOiIiIIi1 ( "[Success] cleared %s files from %s" % ( str ( O0o0oO ) , os . path . join ( ooo , OoOOoooOO0O ) ) )
      except :
       OOiIiIIi1 ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo , OoOOoooOO0O ) )
  else :
   for IIIIiii1IIii , II1i11I , ii1I1IIii11 in os . walk ( ooo ) :
    for OoOOoooOO0O in II1i11I :
     if 'cache' in OoOOoooOO0O . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( IIIIiii1IIii , OoOOoooOO0O ) )
       O0oo0O += 1
       OOiIiIIi1 ( "[Success] wiped %s " % os . path . join ( ooo , OoOOoooOO0O ) )
      except :
       OOiIiIIi1 ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo , OoOOoooOO0O ) )
       if 36 - 36: OoooooooOO . OO
 ii ( IiII , 'Clear Cache: Removed %s Files' % O0oo0O )
def oOIIiIi ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 IiIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IIIIiii1IIii , II1i11I , ii1I1IIii11 in os . walk ( IiIIi1 ) :
   O0o0oO = 0
   O0o0oO += len ( ii1I1IIii11 )
   if 91 - 91: iiIiIIi * iiiIi / iI1I . O0 + OO + i1I111I
   if 8 - 8: iii1I1 / iiIiIIi
   if O0o0oO > 0 :
    if 20 - 20: iI1I
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( O0o0oO ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: I11i1I - iI1I
     for Ii1I1I1i1Ii in ii1I1IIii11 :
      os . unlink ( os . path . join ( IIIIiii1IIii , Ii1I1I1i1Ii ) )
     for OoOOoooOO0O in II1i11I :
      shutil . rmtree ( os . path . join ( IIIIiii1IIii , OoOOoooOO0O ) )
     ii11iIi1I = xbmcgui . Dialog ( )
     ii11iIi1I . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    ii11iIi1I = xbmcgui . Dialog ( )
    ii11iIi1I . ok ( IiII , "       No Packages to DELETE" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "Error Deleting Packages" )
 return
 if 34 - 34: IIIii1II1II * iI1I . i1IIi * IIIii1II1II / IIIii1II1II
def IIiI1Ii ( ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 i1iIi1iIi1i = ii11iIi1I . yesno ( 'Force Close GenieTv WorkOuts' , 'You are about to close GenieTv WorkOuts' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if i1iIi1iIi1i == 0 : return
 elif i1iIi1iIi1i == 1 : pass
 O0O0O0Oo = ooO ( )
 OOiIiIIi1 ( "Platform: " + str ( O0O0O0Oo ) )
 os . _exit ( 1 )
 OOiIiIIi1 ( "Force close failed!  Trying alternate methods." )
 if O0O0O0Oo == 'osx' :
  OOiIiIIi1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0O0O0Oo == 'linux' :
  OOiIiIIi1 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0O0O0Oo == 'android' :
  OOiIiIIi1 ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.GenieTv WorkOuts' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.GenieTv WorkOuts' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.GenieTv WorkOuts());' )
  except : pass
  ii11iIi1I . ok ( IiII , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif O0O0O0Oo == 'windows' :
  OOiIiIIi1 ( "############ try windows force close #################" )
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
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  OOiIiIIi1 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  OOiIiIIi1 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 70 - 70: OO % iii1I1 + III1I11iiii1I / Ii11Ii11I % O0
def oO00O0 ( url ) :
 import urlresolver
 try :
  IIi1IIIi = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( IIi1IIIi , xbmcgui . ListItem ( OOOO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( OOOO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def ooO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 99 - 99: Ii11Ii11I + OO * II111iiii . I1I1IIiiIiI1 - iiIiIIi
def OOiIiIIi1 ( log ) :
 xbmc . log ( "[%s]: %s" % ( IiII , log ) )
 if not os . path . exists ( o0oO0 ) : os . makedirs ( o0oO0 )
 if not os . path . exists ( WIZLOG ) : Ii1I1I1i1Ii = open ( WIZLOG , 'w' ) ; Ii1I1I1i1Ii . close ( )
 with open ( WIZLOG , 'a' ) as Ii1I1I1i1Ii :
  o0OOOo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  Ii1I1I1i1Ii . write ( o0OOOo . rstrip ( '\r\n' ) + '\n' )
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * iI1I
def iII1ii1 ( ) :
 try :
  I1i1iiiI1 = getSet ( "core-player" )
  if ( I1i1iiiI1 == 'DVDPLAYER' ) : iIIi = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( I1i1iiiI1 == 'MPLAYER' ) : iIIi = xbmc . PLAYER_CORE_MPLAYER
  elif ( I1i1iiiI1 == 'PAPLAYER' ) : iIIi = xbmc . PLAYER_CORE_PAPLAYER
  else : iIIi = xbmc . PLAYER_CORE_AUTO
 except : iIIi = xbmc . PLAYER_CORE_AUTO
 return iIIi
 return True
 if 62 - 62: iiiIi - IiI1i11iii1
 if 21 - 21: O0 % O00o0OO . iI1I / II111iiii + O00o0OO
def iIi1ii1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 53 - 53: iii1I1 - iI1I - iii1I1 * I11i1I
 oooooo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1IOooOoOo = True
 III1I1Iii1iiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 III1I1Iii1iiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 III1I1Iii1iiI . setProperty ( "Fanart_Image" , fanart )
 iI1IOooOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooooo0OO , listitem = III1I1Iii1iiI , isFolder = True )
 return iI1IOooOoOo
 if 17 - 17: Ii11Ii11I % iIii1I11I1II1 - iIii1I11I1II1
def OOO00 ( name , url , mode , iconimage , fanart , description ) :
 if 78 - 78: I11i1I + IiI1i11iii1 . IIIii1II1II - I11i1I . Ii11Ii11I
 oooooo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1IOooOoOo = True
 III1I1Iii1iiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 III1I1Iii1iiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 III1I1Iii1iiI . setProperty ( "Fanart_Image" , fanart )
 iI1IOooOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooooo0OO , listitem = III1I1Iii1iiI , isFolder = False )
 return iI1IOooOoOo
def iiIiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oooooo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1IOooOoOo = True
 III1I1Iii1iiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 III1I1Iii1iiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 III1I1Iii1iiI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II1I11i = [ ]
  if showcontext == 'fav' :
   II1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   II1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  III1I1Iii1iiI . addContextMenuItems ( II1I11i )
 iI1IOooOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooooo0OO , listitem = III1I1Iii1iiI , isFolder = False )
 return iI1IOooOoOo
def oOOoOooOo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oooooo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iI1IOooOoOo = True
 III1I1Iii1iiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 III1I1Iii1iiI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II1I11i = [ ]
  II1I11i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   II1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  III1I1Iii1iiI . addContextMenuItems ( II1I11i )
 iI1IOooOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooooo0OO , listitem = III1I1Iii1iiI , isFolder = True )
 return iI1IOooOoOo
def O0Oooo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oooooo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iI1IOooOoOo = True
 III1I1Iii1iiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 III1I1Iii1iiI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II1I11i = [ ]
  II1I11i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   II1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  III1I1Iii1iiI . addContextMenuItems ( II1I11i )
 iI1IOooOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooooo0OO , listitem = III1I1Iii1iiI , isFolder = False )
 return iI1IOooOoOo
 if 21 - 21: iiiIi
def I1ii1 ( ) :
 O00 = [ ]
 Oo0o0000OOoO = sys . argv [ 2 ]
 if len ( Oo0o0000OOoO ) >= 2 :
  IiIi1I1ii111 = sys . argv [ 2 ]
  IiIiIi = IiIi1I1ii111 . replace ( '?' , '' )
  if ( IiIi1I1ii111 [ len ( IiIi1I1ii111 ) - 1 ] == '/' ) :
   IiIi1I1ii111 = IiIi1I1ii111 [ 0 : len ( IiIi1I1ii111 ) - 2 ]
  IIIII1 = IiIiIi . split ( '&' )
  O00 = { }
  for iIi1Ii1i1iI in range ( len ( IIIII1 ) ) :
   IIiI1 = { }
   IIiI1 = IIIII1 [ iIi1Ii1i1iI ] . split ( '=' )
   if ( len ( IIiI1 ) ) == 2 :
    O00 [ IIiI1 [ 0 ] ] = IIiI1 [ 1 ]
    if 17 - 17: III1I11iiii1I / III1I11iiii1I / IiI1i11iii1
 return O00
 if 1 - 1: i1IIi . i11iIiiIii % III1I11iiii1I
 if 82 - 82: iIii1I11I1II1 + iiiIi . iIii1I11I1II1 % O00o0OO / Ii11Ii11I . Ii11Ii11I
IiIi1I1ii111 = I1ii1 ( )
O000oo0O = None
OOOO = None
IIi = None
oOoO00oo0O = None
oOoOooOo0o0 = None
IiiiI = None
O00OoOO0oo0 = None
if 96 - 96: i1I111I . I1I1IIiiIiI1 - IIIii1II1II
if 99 - 99: O00o0OO . iiiIi - Ii11Ii11I % Ii11Ii11I * O0 . II111iiii
try :
 O00OoOO0oo0 = int ( IiIi1I1ii111 [ "fav_mode" ] )
except :
 pass
 if 4 - 4: Ii11Ii11I
try :
 O000oo0O = urllib . unquote_plus ( IiIi1I1ii111 [ "url" ] )
except :
 pass
try :
 OOOO = urllib . unquote_plus ( IiIi1I1ii111 [ "name" ] )
except :
 pass
try :
 oOoO00oo0O = urllib . unquote_plus ( IiIi1I1ii111 [ "iconimage" ] )
except :
 pass
try :
 IIi = int ( IiIi1I1ii111 [ "mode" ] )
except :
 pass
try :
 oOoOooOo0o0 = urllib . unquote_plus ( IiIi1I1ii111 [ "fanart" ] )
except :
 pass
try :
 IiiiI = urllib . unquote_plus ( IiIi1I1ii111 [ "description" ] )
except :
 pass
 if 51 - 51: OO - O0 % iii1I1 - II111iiii
 if 31 - 31: I11i1I / iiiIi - I11i1I - III1I11iiii1I
print str ( o0oOoO00o ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( IIi )
print "URL: " + str ( O000oo0O )
print "Name: " + str ( OOOO )
print "IconImage: " + str ( oOoO00oo0O )
if 7 - 7: I11i1I % O0 . i1I111I + iI1I - IiI1i11iii1
if 75 - 75: IiI1i11iii1
def OOooo0O00o ( content , viewType ) :
 if 71 - 71: IIIii1II1II
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OOO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OOO . getSetting ( viewType ) )
  if 53 - 53: OoooooooOO % Ii11Ii11I . O00o0OO / i11iIiiIii % I11i1I
  if 28 - 28: IiI1i11iii1
if IIi == None : I11i1 ( )
elif IIi == 7084 :
 o0 ( O000oo0O )
elif IIi == 7085 :
 O0OOO ( O000oo0O )
elif IIi == 7086 :
 o0O0OOO0Ooo ( O000oo0O , oOoO00oo0O , IiiiI )
elif IIi == 7087 :
 oO00OOoO00 ( IiiiI )
elif IIi == 8043 :
 yt . PlayVideo ( O000oo0O )
elif IIi == 1001 : O0o0Ooo ( )
elif IIi == 1002 : Oo0O0O0ooO0O ( )
elif IIi == 1003 : OO00Oo ( )
elif IIi == 1004 : oO000Oo000 ( )
elif IIi == 1005 : iI1ii1Ii ( )
elif IIi == 1006 : oOOOOo0 ( )
elif IIi == 1007 : oO00O0O0O ( )
elif IIi == 2001 : ii111111I1iII ( O000oo0O )
elif IIi == 4 : iiiiiIIii ( )
elif IIi == 5 : i1I1i111Ii ( )
elif IIi == 6 : oOIIiIi ( O000oo0O )
elif IIi == 7 : ooo00Ooo ( O000oo0O )
elif IIi == 8 : IIiI1Ii ( )
elif IIi == 15 : oO00O0 ( O000oo0O )
elif IIi == 18 : o0OOO . openSettings ( sys . argv [ 0 ] )
elif IIi == 50000 : OOooooO0Oo ( )
elif IIi == 50001 : o0O0OOOOoOO0 ( )
elif IIi == 50002 : II1iIi11 ( O000oo0O )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
