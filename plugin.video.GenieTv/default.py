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
O00ooOO = "2.6.22"
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
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  i1I1iI ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  oo0OooOOo0 ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 oo0OooOOo0 ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 91 - 91: Ooo00oOo00o . ii11ii1ii + Ooo00oOo00o - oOOoo0Oo / OoooooooOO
 if 39 - 39: ii11ii1ii / oO0 - OoOoOO00
 if 98 - 98: ii11ii1ii / oOo00oOO0O % ii . I1IiI
 if 91 - 91: ii % Oo
 if 64 - 64: oOo00oOO0O % oOOoo0Oo - O00Oo000ooO0 - ii
def IIIii1II1II ( ) :
 i1ii1iiI = O0o0O00Oo0o0 ( 'http://architects.x10host.com/wizarddelete.txt' )
 O00O0oOO00O00 = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( i1ii1iiI )
 for i1Oo00 in O00O0oOO00O00 :
  print i1Oo00
  i1Oo00 = ( str ( i1Oo00 ) )
  if os . path . exists ( xbmc . translatePath ( i1Oo00 ) ) :
   i1i = os . path . join ( o0 , 'guisettings.xml' )
   iiI111I1iIiI = open ( i1i , "w+" )
   if 41 - 41: Oo . oO0 + O0 * OOooOOo % Oo * Oo
   iiI111I1iIiI . write ( r'.' )
   iIIIIi1iiIi1 ( )
  else :
   pass
   if 21 - 21: OOOo0 * iIii1I11I1II1
def ii11i1 ( ) :
 i1ii1iiI = O0o0O00Oo0o0 ( 'http://architects.x10host.com/testdelete.txt' )
 O00O0oOO00O00 = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( i1ii1iiI )
 for Iii111II in O00O0oOO00O00 :
  Iii111II = ( str ( Iii111II ) )
  if os . path . exists ( xbmc . translatePath ( Iii111II ) ) :
   iiii11I ( Iii111II )
   UPDATEREPO ( )
  else :
   pass
   if 91 - 91: I1IIiI1
def iiii11I ( addon ) :
 addon = ( addon ) . replace ( 'special://home/addons/' , '' )
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 i1i = os . path . join ( II , 'default.py' )
 iiI111I1iIiI = open ( i1i , "w+" )
 if 15 - 15: OoOoOO00
 iiI111I1iIiI . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 iiI111I1iIiI . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 iiI111I1iIiI . write ( r'Please remove ' + addon + ' if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 if 75 - 75: I1IiI % OOooOOo % OOooOOo . O00Oo000ooO0
def iIIIIi1iiIi1 ( ) :
 i1ii1iiI = O0o0O00Oo0o0 ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 III1iII1I1ii = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( i1ii1iiI )
 for oOOo0 , III1iII1I1ii in III1iII1I1ii :
  oOOo0 = oOOo0
  O00O0oOO00O00 = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( III1iII1I1ii ) )
  for oo00O00oO , iIiIIIi in O00O0oOO00O00 :
   o00OO00OoO ( oOOo0 , oo00O00oO , iIiIIIi )
   if 93 - 93: oOOoo0Oo
   if 10 - 10: oOo00oOO0O
def OOooOO000 ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  OOoOoo = open ( iIi1ii1I1 )
  O00O0oOO00O00 = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OOoOoo ) )
  for oO0000OOo00 , iiIi1IIiIi in O00O0oOO00O00 :
   if oO0000OOo00 == 'needs replacing' or iiIi1IIiIi == 'needs replacing' :
    oOO00Oo ( )
  i1I1iI ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelist.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 6 - 6: ii
def oOOo0oOo0 ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 i1iiIIiiI111 . ok ( '[COLOR=red]Reset Any Previous linked streams[/COLOR]' , 'For best results you\'ll need to clear previous linked streams' , 'Go to TVGuide tab then reset database at the bottom' , 'Then go back and guide should be all linked up and ready to go' )
 o0oO0 . openSettings ( sys . argv [ 0 ] )
 oOO00Oo ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 49 - 49: Oo . i11iIiiIii - i1IIi / OoOoOO00 . OOOo0
def II1I ( ) :
 try :
  O0i1II1Iiii1I11 = gui . TVGuide ( )
  O0i1II1Iiii1I11 . doModal ( )
  del O0i1II1Iiii1I11
  if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
 except :
  import sys
  import traceback as tb
  ( o00oooO0Oo , o0O0OOO0Ooo , traceback ) = sys . exc_info ( )
  tb . print_exception ( o00oooO0Oo , o0O0OOO0Ooo , traceback )
  if 45 - 45: O0 / OOooOOo
  if 32 - 32: oOOoo0Oo . I1IIiI1 . I1IIiI1
  if 62 - 62: ii11ii1ii + I1IIiI1 % oOOoo0Oo + Ii11I
def oOO00Oo ( ) :
 iii = os . path . join ( iIii1 , 'addons.ini' )
 oOooOOOoOo = open ( iii , "w+" )
 if 41 - 41: oO0O0ooO0Oo - O0 - O0
 oOooOOOoOo . write ( r'# This file contains the "built-in" channels' + '\n' )
 oOooOOOoOo . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 oOooOOOoOo . write ( r'[plugin.video.GenieTv]' + '\n' )
 oOooOOOoOo . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F394.m3u8&mode=10012&name=[COLORgreen]BBC+One+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'BBC Ent MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F435.m3u8&mode=10012&name=[COLORgreen]BBC+Entertainment+MX%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F408.m3u8&mode=10012&name=[COLORgreen]Watch+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F410.m3u8&mode=10012&name=[COLORgreen]Pick+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F430.m3u8&mode=10012&name=[COLORgreen]Gold+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F411.m3u8&mode=10012&name=[COLORgreen]Yesterday+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F398.m3u8&mode=10012&name=[COLORgreen]Disney+Channel+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F397.m3u8&mode=10012&name=[COLORgreen]Disney+Junior+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F395.m3u8&mode=10012&name=[COLORgreen]Discovery+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F396.m3u8&mode=10012&name=[COLORgreen]Discovery+Science+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F428.m3u8&mode=10012&name=[COLORgreen]Animal+Planet+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F431.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F429.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F409.m3u8&mode=10012&name=[COLORgreen]MTV+Music+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'MTV Canada=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F417.m3u8&mode=10012&name=[COLORgreen]MTV+2+Ca%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F37.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F39.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F40.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F43.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F41.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F44.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F47.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F48.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Fox Movies HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F436.m3u8&mode=10012&name=[COLORgreen]Fox+Movies+HD+MX%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Film Zone MX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F437.m3u8&mode=10012&name=[COLORgreen]Film+Zone+MX+HD%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F403.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F404.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F405.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F406.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F407.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F412.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F423.m3u8&mode=10012&name=[COLORgreen]BT+Sports+1%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F413.m3u8&mode=10012&name=[COLORgreen]BT+Sports+2%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Fox Sports 1 HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F439.m3u8&mode=10012&name=[COLORgreen]Fox+Sports+1+HD+MX%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'ESPN 1 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F440.m3u8&mode=10012&name=[COLORgreen]ESPN+1+HD+ES%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'ESPN 2 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F441.m3u8&mode=10012&name=[COLORgreen]ESPN+2+HD+ES%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F427.m3u8&mode=10012&name=[COLORgreen]At+The+Races+UK%0D[/COLOR]' + '\n' )
 oOooOOOoOo . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F426.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[/COLOR]' + '\n' )
 if 68 - 68: Ii11I % O00Oo000ooO0
def i1I1iI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 ooO00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11111IIIII = True
 iIiii1i111iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIiii1i111iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIiii1i111iI1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i11oO0oOo0 = [ ]
  if showcontext == 'fav' :
   i11oO0oOo0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   i11oO0oOo0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iIiii1i111iI1 . addContextMenuItems ( i11oO0oOo0 )
 i11111IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO00OO0 , listitem = iIiii1i111iI1 , isFolder = True )
 return i11111IIIII
 if 45 - 45: oOOoo0Oo / oOOoo0Oo + O00Oo000ooO0 + oO0
def oo0OooOOo0 ( name , url , mode , iconimage , fanart , description ) :
 ooO00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11111IIIII = True
 iIiii1i111iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIiii1i111iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIiii1i111iI1 . setProperty ( "Fanart_Image" , fanart )
 i11111IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO00OO0 , listitem = iIiii1i111iI1 , isFolder = False )
 return i11111IIIII
 if 47 - 47: OOooOOo + oO0
def OoO ( ) :
 O00 = [ ]
 I1iI1 = sys . argv [ 2 ]
 if len ( I1iI1 ) >= 2 :
  iiiIi1 = sys . argv [ 2 ]
  i1I1ii11i1Iii = iiiIi1 . replace ( '?' , '' )
  if ( iiiIi1 [ len ( iiiIi1 ) - 1 ] == '/' ) :
   iiiIi1 = iiiIi1 [ 0 : len ( iiiIi1 ) - 2 ]
  I1IiiiiI = i1I1ii11i1Iii . split ( '&' )
  O00 = { }
  for o0O in range ( len ( I1IiiiiI ) ) :
   IiII = { }
   IiII = I1IiiiiI [ o0O ] . split ( '=' )
   if ( len ( IiII ) ) == 2 :
    O00 [ IiII [ 0 ] ] = IiII [ 1 ]
    if 25 - 25: O0 - O0 * OOooOOo
 return O00
 if 51 - 51: Oo - ii + OoOoOO00 * oO0O0ooO0Oo . oOo00oOO0O + ii
iiiIi1 = OoO ( )
OoO0o = None
oo00O00oO = None
oO0o0Ooooo = None
OOo0oO00ooO00 = None
oOO0O00oO0Ooo = None
oO0Oo0O0o = None
OO = None
if 37 - 37: oO0 % ii . i11iIiiIii % oO0O0ooO0Oo . Oo
if 39 - 39: Ii11I - Oo * ii11ii1ii % OOooOOo
try :
 OO = int ( iiiIi1 [ "fav_mode" ] )
except :
 pass
 if 40 - 40: iIii1I11I1II1 / I1IiI % ii11ii1ii + OoOoOO00
try :
 OoO0o = urllib . unquote_plus ( iiiIi1 [ "url" ] )
except :
 pass
try :
 oo00O00oO = urllib . unquote_plus ( iiiIi1 [ "name" ] )
except :
 pass
try :
 OOo0oO00ooO00 = urllib . unquote_plus ( iiiIi1 [ "iconimage" ] )
except :
 pass
try :
 oO0o0Ooooo = int ( iiiIi1 [ "mode" ] )
except :
 pass
try :
 oOO0O00oO0Ooo = urllib . unquote_plus ( iiiIi1 [ "fanart" ] )
except :
 pass
try :
 oO0Oo0O0o = urllib . unquote_plus ( iiiIi1 [ "description" ] )
except :
 pass
 if 27 - 27: OoOoOO00 * I1IiI * iIii1I11I1II1
 if 86 - 86: Ooo00oOo00o * Ii11I . oOOoo0Oo
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( oO0o0Ooooo )
print "URL: " + str ( OoO0o )
print "Name: " + str ( oo00O00oO )
print "IconImage: " + str ( OOo0oO00ooO00 )
if 32 - 32: OOooOOo . I1IIiI1 * oOo00oOO0O
def o00OO00OoO ( heading , announce ) :
 class OOooo0oOO0O ( ) :
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
   try : o00O0 = open ( announce ) ; oOO0O00Oo0O0o = o00O0 . read ( )
   except : oOO0O00Oo0O0o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOO0O00Oo0O0o ) )
   return
 OOooo0oOO0O ( )
 OOooo0oOO0O ( )
 if 13 - 13: OoooooooOO
def O0o0O00Oo0o0 ( url ) :
 I111iI = urllib2 . Request ( url )
 I111iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oOOo0II1I1iiIII = urllib2 . urlopen ( I111iI )
 oOOo0O00o = oOOo0II1I1iiIII . read ( )
 oOOo0II1I1iiIII . close ( )
 return oOOo0O00o
 if 8 - 8: Ooo00oOo00o
def ii1111iII ( url ) :
 i1ii1iiI = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( i1ii1iiI )
 for iiiiI , oo00O00oO , url in O00O0oOO00O00 :
  url = ( ( i1111 ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  oo0OooOOo0 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . replace ( '.ts' , '.m3u8' ) , 10012 , iiiiI , '' , '' )
  if 62 - 62: OoooooooOO * OOOo0
def oOOOoo0O0oO ( url ) :
 iIII1I111III = xbmc . Player ( IIo0o0O0O00oOOo ( ) )
 import urlresolver
 try : iIII1I111III . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( oo00O00oO ) )
 iIII1I111III = xbmc . Player ( IIo0o0O0O00oOOo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iIII1I111III . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 14 - 14: I1IiI + ii
def oo00oO0O0 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % oo00O00oO )
 xbmc . sleep ( 1 )
 iIII1I111III = xbmc . Player ( IIo0o0O0O00oOOo ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % oo00O00oO )
 xbmc . sleep ( 1 )
 iIII1I111III . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 30 - 30: Ii11I + ii11ii1ii * oOo00oOO0O % i11iIiiIii % I1IiI
def OO0OoOO0o0o ( url ) :
 iIII1I111III = xbmc . Player ( IIo0o0O0O00oOOo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIII1I111III . play ( url ) . strip ( )
 except : pass
 if 95 - 95: i11iIiiIii
def IIo0o0O0O00oOOo ( ) :
 try :
  iI1111iiii = getSet ( "core-player" )
  if ( iI1111iiii == 'DVDPLAYER' ) : Oo0OO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iI1111iiii == 'MPLAYER' ) : Oo0OO = xbmc . PLAYER_CORE_MPLAYER
  elif ( iI1111iiii == 'PAPLAYER' ) : Oo0OO = xbmc . PLAYER_CORE_PAPLAYER
  else : Oo0OO = xbmc . PLAYER_CORE_AUTO
 except : Oo0OO = xbmc . PLAYER_CORE_AUTO
 return Oo0OO
 return True
 if 78 - 78: Ii11I - OoooooooOO - ii11ii1ii / oO0 / OoOoOO00
if oO0o0Ooooo == None : OOO0OOO00oo ( )
elif oO0o0Ooooo == 7080 : ii1111iII ( OoO0o )
elif oO0o0Ooooo == 4009 : Ii1iIiii1 ( )
elif oO0o0Ooooo == 4010 : oOOo0oOo0 ( )
elif oO0o0Ooooo == 10063 : II1I ( )
elif oO0o0Ooooo == 10058 : OOooOO000 ( )
elif oO0o0Ooooo == 10059 : Donators_Guide ( )
elif oO0o0Ooooo == 10012 : OO0OoOO0o0o ( OoO0o )
elif oO0o0Ooooo == 100000 : Ooo0OO0oOO ( )
if 29 - 29: OOOo0 % OOOo0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
