# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata , socket
import xml . etree . ElementTree as ElementTree
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
IiII1IiiIiI1 = 'plugin.video.GtvV2'
iIiiiI1IiI1I1 = 'plugin.video.GtvV2'
o0OoOoOO00 = "0.0.1"
I11i = xbmc . translatePath ( 'special://home/addons/' )
O0O = base64 . decodestring
Oo = datetime . now ( )
I1ii11iIi11i = xbmcaddon . Addon ( ) . setSetting
I1IiI = xbmc . translatePath ( 'special://logpath/' )
o0OOO = xbmc . translatePath ( 'special://home/addonsbroke/' )
iIiiiI = xbmcaddon . Addon ( id = iIiiiI1IiI1I1 )
Iii1ii1II11i = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
iI111iI = 'plugin.video.GtvV2'
IiII = xbmcgui . DialogProgress ( )
iI1Ii11111iIi = "Gtv V2"
i1i1II = Net ( )
O0oo0OO0 = xbmc . translatePath ( 'special://home/' )
O0O = base64 . decodestring
I1i1iiI1 = xbmc . translatePath ( 'special://profile/' )
iiIIIII1i1iI = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
o0oO0 = os . path . join ( O0oo0OO0 , 'userdata' )
oo00 = os . path . join ( o0oO0 , 'addon_data' , IiII1IiiIiI1 )
o00 = os . path . join ( I11i , 'packages' )
Oo0oO0ooo = iIiiiI . getSetting ( 'User' )
o0oOoO00o = os . path . join ( oo00 , 'wizard.log' )
i1 = iIiiiI . getSetting ( 'Pass' )
oOOoo00O0O = iIiiiI . getSetting ( 'AdultPass' )
i1111 = ( O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsvVjIv' ) )
i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'icon.png' ) )
I11 = i1111 + ( O0O ( 'YXJ0Lw==' ) )
Oo0o0000o0o0 = i1111 + ( O0O ( 'cmVzZWwvd2l6LnhtbA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
oOo0oooo00o = i1111 + ( O0O ( 'YXBrLnR4dA==' ) )
oO0o0o0ooO0oO = ( O0O ( 'aHR0cDovL2xpdmUtcHJlbS1lbmMudWsudG86MjA1Mi8=' ) )
oo0o0O00 = 'https://genietv.co.uk'
oO = ( O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
i1iiIIiiI111 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GtvV2' )
oooOOOOO = xbmc . translatePath ( 'special://thumbnails' ) ;
i1iiIII111ii = "Reseller"
i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'fanart.jpg' ) )
ii11iIi1I = iIiiiI . getLocalizedString
iI111I11I1I1 = CookieJar ( )
OOooO0OOoo = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( iI111I11I1I1 ) )
OOooO0OOoo . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
iIii1 = int ( sys . argv [ 1 ] )
oOOoO0 = xbmc . translatePath ( iIiiiI . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
o0oO0 = xbmc . translatePath ( 'special://home/userdata/' )
O0OoO000O0OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
iiI1IiI = i1iiIIiiI111 + '/addons.ini'
II = xbmcgui . Dialog ( )
ooOoOoo0O = iIiiiI . getSetting ( 'DNS' )
if ooOoOoo0O == 'Option 1' :
 OooO0 = '.net'
if ooOoOoo0O == 'Option 2' :
 OooO0 = '.eu'
if ooOoOoo0O == 'Option 3' :
 OooO0 = '.com'
if os . path . exists ( O0OoO000O0OO ) == True :
 II11iiii1Ii = open ( O0OoO000O0OO ) . read ( )
else : II11iiii1Ii = [ ]
if 70 - 70: O00 / i1I1i1Ii11 . IIIIII11i1I - o0o0OOO0o0 % ooOOOo0oo0O0
if 71 - 71: oO00OO0oo0 . III1i1i
if 26 - 26: i1iiI11I
def iiii ( ) :
 oO0o0O0OOOoo0 ( '[COLORsteelblue]Live Lists[/COLOR]' , '' , 40099 , I11 + 'live_lists.png' , i1iIIi1 , '' )
 oO0o0O0OOOoo0 ( '[COLORsteelblue]Maintenance[/COLOR]' , '' , 5 , I11 + 'maintenance.png' , i1iIIi1 , '' )
 oO0o0O0OOOoo0 ( '[COLORsteelblue]Login[/COLOR]' , '' , 18 , I11 + 'login.png' , i1iIIi1 , '' )
 IiIiiI ( '[COLORsteelblue]Contact Us[/COLOR]' , '' , 50006 , I11 + 'contactus.png' , i1iIIi1 , '' )
def I1I ( ) :
 oO0o0O0OOOoo0 ( '[COLORsteelblue]My Account[/COLOR]' , '' , 10 , I11 + 'live_lists.png' , i1iIIi1 , '' )
 oO0o0O0OOOoo0 ( '[COLORsteelblue]Channel Lists[/COLOR]' , '' , 16 , I11 + 'live_lists.png' , i1iIIi1 , '' )
 oO0o0O0OOOoo0 ( '[COLORsteelblue]Guide Menu[/COLOR]' , '' , 211 , I11 + 'live_lists.png' , i1iIIi1 , '' )
 oO0o0O0OOOoo0 ( '[COLORsteelblue]CatchUp[/COLOR]' , '' , 90026 , I11 + 'live_lists.png' , i1iIIi1 , '' )
 if 80 - 80: i1iII11iiIii - iIii11I
 IiIiiI ( '[COLORsteelblue]Get Short Links[/COLOR]' , '' , 214 , I11 + 'live_lists.png' , i1iIIi1 , '' )
 if 69 - 69: OOOO00ooo0Ooo % OOooOooo % O00oo0OO0oOOO * i1i1i11IIi . i1i1i11IIi / IIIIII11i1I
OOOoO0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GtvV2/resources/catchup' , 'guide.xml' ) )
O0o0Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GtvV2/resources/catchup' , 'g' ) )
if 56 - 56: i1i1i11IIi . o0o0OOO0o0 * OOOO00ooo0Ooo . o0o0OOO0o0
def O00oO ( ) :
 I11i1I1I = oO0o0o0ooO0oO + "/get.php?username=" + Oo0oO0ooo + "&password=" + i1 + "&type=m3u_plus&output=ts"
 try :
  oO0Oo = urllib2 . urlopen ( I11i1I1I )
  print oO0Oo . getcode ( )
  oO0Oo . close ( )
  if 54 - 54: ooOOOo0oo0O0 - O00 + OoooooooOO
  pass
  if 70 - 70: iIii11I / i1iII11iiIii . OOOO00ooo0Ooo % i1I1i1Ii11
 except urllib2 . HTTPError , OOoOO00OOO0OO :
  print OOoOO00OOO0OO . getcode ( )
  II . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 16 - 16: O00 * III1i1i % OOooOooo
 Oo000o = oO0o0o0ooO0oO + "/xmltv.php?username=%s&password=%s" % ( Oo0oO0ooo , i1 )
 I11IiI1I11i1i ( Oo000o , O0o0Ooo + "uide.xml" )
 if 38 - 38: ooOOOo0oo0O0
 Oo0O = open ( OOOoO0O0o , 'r+' )
 input = open ( OOOoO0O0o ) . read ( ) . decode ( 'UTF-8' )
 IIi = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 Oo0O . write ( IIi )
 Oo0O . truncate ( )
 Oo0O . close ( )
 i11iIIIIIi1 ( )
 if 20 - 20: i1IIi + oO00OO0oo0 - i1i1i11IIi
def i11iIIIIIi1 ( ) :
 open = IiI11iII1 ( IIII11I1I )
 all = OOO0o ( open , '{"num' , 'direct' )
 for IiI1 in all :
  if '"tv_archive":1' in IiI1 :
   Oo0O00Oo0o0 = O00O0oOO00O00 ( IiI1 , '"epg_channel_id":"' , '"' )
   i1Oo00 = O00O0oOO00O00 ( IiI1 , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = O00O0oOO00O00 ( IiI1 , 'stream_id":"' , '"' )
   Oo0O00Oo0o0 = Oo0O00Oo0o0 . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   oO0o0O0OOOoo0 ( Oo0O00Oo0o0 , id , 90027 , i1Oo00 , i1i , Oo0O00Oo0o0 )
   if 50 - 50: OOooOooo
   if 14 - 14: i1iII11iiIii % IIIIII11i1I * i1iII11iiIii
def iII ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 oO00o0 = open ( OOOoO0O0o )
 OOoo0O = ElementTree . parse ( oO00o0 )
 Oo0ooOo0o = "apples"
 import datetime as dt
 from datetime import time
 Ii1i1 = datetime . now ( ) - timedelta ( days = 5 )
 iiIii = str ( Ii1i1 )
 Oo = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 ooo0O = OOoo0O . findall ( "programme" )
 for oOoO0o00OO0 in ooo0O :
  if name in oOoO0o00OO0 . attrib . get ( 'channel' ) :
   i1I1ii = oOoO0o00OO0 . attrib . get ( 'start' )
   oOOo0 , oo00O00oO , iIiIIIi = i1I1ii . partition ( ' +' )
   iiIii = str ( iiIii ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo = i1I1ii . partition ( '2017' )
   oo0OOo = oOoO0o00OO0 . find ( 'title' ) . text + i1I1ii
   O000OOo00oo = O000OOo00oo [ : - 6 ]
   if oOOo0 > iiIii :
    if oOOo0 < Oo :
     ooOOO00Ooo = oOOo0
     ooOOO00Ooo = ooOOO00Ooo [ : 4 ] + '/' + ooOOO00Ooo [ 4 : ]
     oOOo0 = oOOo0 [ : 4 ] + '-' + oOOo0 [ 4 : ]
     ooOOO00Ooo = ooOOO00Ooo [ : 7 ] + '/' + ooOOO00Ooo [ 7 : ]
     oOOo0 = oOOo0 [ : 7 ] + '-' + oOOo0 [ 7 : ]
     ooOOO00Ooo = ooOOO00Ooo [ : 10 ] + ' - ' + ooOOO00Ooo [ 10 : ]
     oOOo0 = oOOo0 [ : 10 ] + ':' + oOOo0 [ 10 : ]
     ooOOO00Ooo = ooOOO00Ooo [ : 15 ] + ':' + ooOOO00Ooo [ 15 : ]
     oOOo0 = oOOo0 [ : 13 ] + '-' + oOOo0 [ 13 : ]
     ooOOO00Ooo = ooOOO00Ooo [ : - 2 ]
     oOOo0 = oOOo0 [ : - 2 ]
     IiIIIi1iIi = ( oO0o0o0ooO0oO + "/streaming/timeshift.php?username=%s&password=%s&start=" + str ( oOOo0 ) + "&duration=240" + "&stream=%s" ) % ( Oo0oO0ooo , i1 , id )
     Oo0ooOo0o = IiIIIi1iIi + str ( oOOo0 ) + "&duration=240"
     ooOOO00Ooo = '[COLOR blue]%s - [/COLOR]' % ooOOO00Ooo
     oo0OOo = str ( ooOOO00Ooo ) + oOoO0o00OO0 . find ( 'title' ) . text
     ooOOoooooo = oOoO0o00OO0 . find ( 'desc' ) . text
     IiIiiI ( oo0OOo , IiIIIi1iIi , 15 , I11 + 'catchup.png' , i1iIIi1 , ooOOoooooo )
oO0o0o0ooO0oO = ( O0O ( 'aHR0cDovL2dlbmllaG9zdC5hY2Nlc3MubHk6ODA4MC8=' ) )
def II1I ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , Oo0oO0ooo ) . replace ( 'PASSWORD' , i1 )
 O0i1II1Iiii1I11 = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = i11 )
 O0i1II1Iiii1I11 . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 O0i1II1Iiii1I11 . setProperty ( 'IsPlayable' , 'true' )
 O0i1II1Iiii1I11 . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0i1II1Iiii1I11 )
def I11IiI1I11i1i ( url , dest ) :
 IiII = xbmcgui . DialogProgress ( )
 IiII . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 IiII . update ( 0 )
 IIII = time . time ( )
 urllib . urlretrieve ( url , dest , lambda iiIiI , o00oooO0Oo , o0O0OOO0Ooo : iiIiII1 ( iiIiI , o00oooO0Oo , o0O0OOO0Ooo , IiII , IIII ) )
def iiIiII1 ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  OOO00O0O = min ( numblocks * blocksize * 100 / filesize , 100 )
  iii = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  oOooOOOoOo = numblocks * blocksize / ( time . time ( ) - start_time )
  if oOooOOOoOo > 0 :
   i1Iii1i1I = ( filesize - numblocks * blocksize ) / oOooOOOoOo
  else :
   i1Iii1i1I = 0
  oOooOOOoOo = oOooOOOoOo / 1024
  OOoO00 = oOooOOOoOo / 1024
  IiI111111IIII = float ( filesize ) / ( 1024 * 1024 )
  i1Ii = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( iii )
  OOoOO00OOO0OO = '[COLOR white]Speed:  %.02f Mb/s ' % OOoO00 + '[/COLOR]'
  dp . update ( OOO00O0O , i1Ii , OOoOO00OOO0OO )
 except :
  OOO00O0O = 100
  dp . update ( OOO00O0O )
 if dp . iscanceled ( ) :
  II = xbmcgui . Dialog ( )
  II . ok ( "plugin.video.GtvV2" , 'The download was cancelled.' )
  if 14 - 14: OOOO00ooo0Ooo
  sys . exit ( )
  dp . close ( )
  if 11 - 11: OOooOooo * O00 . iIii1I11I1II1 % OoooooooOO + OOOO00ooo0Ooo
  if 78 - 78: IIIIII11i1I . i1iiI11I + IIIIII11i1I / i1iII11iiIii / IIIIII11i1I
def oO0O00OoOO0 ( ) :
 OoO = IiI11iII1 ( O0O ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 O00I1iI1 = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OoO )
 for Oo000o , Oo0O00Oo0o0 in O00I1iI1 :
  oO0o0O0OOOoo0 ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' , 'http://www.listenlive.eu/' + Oo000o , 51 , I11 + 'radio.png' , '' , '' )
def iiiIi1 ( url ) :
 OoO = IiI11iII1 ( url )
 O00I1iI1 = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a></td>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">(.+?)</a></td>.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( OoO )
 for Oo0O00Oo0o0 , i1I1ii11i1Iii , url , I1IiiiiI , o0O in O00I1iI1 :
  IiIiiI ( '[COLORsteelblue]' + Oo0O00Oo0o0 + ' [COLORorangered] ' + o0O + '[/COLOR]' , url , 15 , I11 + 'radio.png' , I11 + 'radio.png' , '[COLORsteelblue]' + Oo0O00Oo0o0 + '[CR]' + i1I1ii11i1Iii + '[CR]' + o0O + '[CR]' + I1IiiiiI + '[/COLOR]' )
  if 2 - 2: iIii1I11I1II1 / III1i1i + IIIIII11i1I / i1iiI11I
  if 9 - 9: ooOOOo0oo0O0 . i1i1i11IIi - i1I1i1Ii11 - III1i1i + II111iiii * i11iIiiIii
def oO00ooO0o0 ( title , message , times = 2000 , icon = i11 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def I1i1Iiiii ( ) :
 OOo0oO00ooO00 = oOO0O00oO0Ooo ( )
 oO0Oo0O0o = OOo0oO00ooO00 . replace ( I1IiI , "" )
 if os . path . exists ( OOo0oO00ooO00 ) or not OOo0oO00ooO00 == False :
  Oo0O = open ( OOo0oO00ooO00 , mode = 'r' ) ; OO = Oo0O . read ( ) ; Oo0O . close ( )
  I1iI1ii1II ( "%s - %s" % ( iI1Ii11111iIi , oO0Oo0O0o ) , OO )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def oOO0O00oO0Ooo ( ) :
 O0O0OOOOoo = False
 if os . path . exists ( os . path . join ( I1IiI , 'xbmc.log' ) ) :
  O0O0OOOOoo = os . path . join ( I1IiI , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1IiI , 'kodi.log' ) ) :
  O0O0OOOOoo = os . path . join ( I1IiI , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1IiI , 'spmc.log' ) ) :
  O0O0OOOOoo = os . path . join ( I1IiI , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1IiI , 'tvmc.log' ) ) :
  O0O0OOOOoo = os . path . join ( I1IiI , 'tvmc.log' )
 return O0O0OOOOoo
 if 74 - 74: oO00OO0oo0 + II111iiii / IIIIII11i1I
 if 100 - 100: o0o0OOO0o0 * iIii1I11I1II1
 if 86 - 86: IIIIII11i1I * i1iiI11I . OOOO00ooo0Ooo
 if 32 - 32: ooOOOo0oo0O0 . OOooOooo * i1iII11iiIii
 if 93 - 93: ooOOOo0oo0O0 % i1IIi . iIii11I . i11iIiiIii
def I1iI1ii1II ( title , msg ) :
 class I1iI1ii1II ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 56 - 56: oO00OO0oo0 % O0 - O00
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 100 - 100: iIii11I - O0 % III1i1i * i1iiI11I + O00
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 88 - 88: OoooooooOO - IIIIII11i1I * O0 * OoooooooOO . OoooooooOO
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 33 - 33: O00oo0OO0oOOO + OOOO00ooo0Ooo * III1i1i / iIii1I11I1II1 - O00
 O0oO = I1iI1ii1II ( "Textbox.xml" , iIiiiI . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 O0oO . doModal ( )
 del O0oO
 if 73 - 73: oO00OO0oo0 * i11iIiiIii % III1i1i . oO00OO0oo0
def OOOOo0 ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 IiiiIIiIi1 = oO0o0o0ooO0oO + 'get.php%3Fusername%3D' + Oo0oO0ooo + '%26password%3D' + i1 + '%26type%3Dm3u_plus%26output%3Dts'
 OoOOoOooooOOo = oO0o0o0ooO0oO + 'xmltv.php%3Fusername%3D' + Oo0oO0ooo + '%26password%3D' + i1
 oOo0O = oO0o0o0ooO0oO + 'enigma2.php?username=' + Oo0oO0ooo + '&password=' + i1 + '&type=get_vod_categories'
 oOo0O = IiI11iII1 ( oOo0O )
 if not oOo0O == "" :
  oo0O0 = 'https://tinyurl.com/create.php?source=indexpage&url=' + IiiiIIiIi1 + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( oo0O0 ) )
  iI = 'https://tinyurl.com/create.php?source=indexpage&url=' + OoOOoOooooOOo + '&submit=Make+TinyURL%21&alias='
  IiiiIIiIi1 = IiI11iII1 ( oo0O0 )
  OoOOoOooooOOo = IiI11iII1 ( iI )
  xbmc . log ( str ( OoOOoOooooOOo ) )
  OO0O000 = O00O0oOO00O00 ( IiiiIIiIi1 , '<div class="indent"><b>' , '</b>' )
  iiIiI1i1 = O00O0oOO00O00 ( OoOOoOooooOOo , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLORsteelblue]plugin.video.GtvV2[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % OO0O000 , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % iiIiI1i1 )
 else :
  return
def oO0O00oOOoooO ( ) :
 IiIiiI ( '[COLORsteelblue]Setup Tv Guide[/COLOR]' , '' , 212 , i11 , i1iIIi1 , '' )
 IiIiiI ( '[COLORsteelblue]Open Guide[/COLOR]' , '' , 213 , i11 , i1iIIi1 , '' )
 if 46 - 46: O00 - OoooooooOO - i1iII11iiIii * II111iiii
def I1i1I11I ( ) :
 ivuesetup . iVueInt ( )
 if 80 - 80: i11iIiiIii % i1i1i11IIi + iIii11I % i1iII11iiIii - oO00OO0oo0
def I1i1i1iii ( ) :
 I1111i ( )
 return
 if 14 - 14: i1iiI11I / ooOOOo0oo0O0
def I1111i ( ) :
 if 32 - 32: O00 * i1I1i1Ii11
 O0OooOo0o = xbmcaddon . Addon ( 'plugin.video.GtvV2' )
 iiI11ii1I1 = O0OooOo0o . getSetting ( id = 'User' )
 Ooo0OOoOoO0 = O0OooOo0o . getSetting ( id = 'Pass' )
 oOo0OOoO0 = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 IIo0Oo0oO0oOO00 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 oo00OO0000oO = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 I11i1I1I = oO0o0o0ooO0oO + "get.php?username=" + iiI11ii1I1 + "&password=" + Ooo0OOoOoO0 + "&type=m3u_plus&output=ts"
 I1II1 = oO0o0o0ooO0oO + "xmltv.php?username=" + iiI11ii1I1 + "&password=" + Ooo0OOoOoO0 + "&type=m3u_plus&output=ts"
 if 86 - 86: iIii1I11I1II1 / o0o0OOO0o0 . II111iiii
 xbmc . executeJSONRPC ( oOo0OOoO0 )
 xbmc . executeJSONRPC ( IIo0Oo0oO0oOO00 )
 xbmc . executeJSONRPC ( oo00OO0000oO )
 if 19 - 19: oO00OO0oo0 % OoooooooOO % OOooOooo * ooOOOo0oo0O0 % O0
 ooo = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 ooo . setSetting ( id = 'm3uUrl' , value = I11i1I1I )
 ooo . setSetting ( id = 'epgUrl' , value = I1II1 )
 ooo . setSetting ( id = 'm3uCache' , value = "false" )
 ooo . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def i1i1iI1iiiI ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 if 51 - 51: O00 % O00oo0OO0oOOO . III1i1i / iIii1I11I1II1 / i1iII11iiIii . III1i1i
def IIIii11 ( data ) :
 iiIiIIIiiI = len ( data ) % 4
 if 12 - 12: O0 - ooOOOo0oo0O0
 if 81 - 81: o0o0OOO0o0 - o0o0OOO0o0 . OOOO00ooo0Ooo
 if 73 - 73: i1iII11iiIii % i11iIiiIii - O00
 if 7 - 7: O0 * i11iIiiIii * iIii11I + i1i1i11IIi % IIIIII11i1I - i1i1i11IIi
 if 39 - 39: i1I1i1Ii11 * i1iiI11I % i1iiI11I - OoooooooOO + ooOOOo0oo0O0 - i1iII11iiIii
 if 23 - 23: i11iIiiIii
 if iiIiIIIiiI != 0 :
  data += b'=' * ( 4 - iiIiIIIiiI )
 return base64 . decodestring ( data )
def O00O0oOO00O00 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : II1iIi11 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : II1iIi11 = ''
 else :
  try : II1iIi11 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : II1iIi11 = ''
 return II1iIi11
 if 12 - 12: iIii11I + i11iIiiIii * iIii1I11I1II1 / oO00OO0oo0 . i1iII11iiIii
 if 5 - 5: i1IIi + OOooOooo / ooOOOo0oo0O0 . OOOO00ooo0Ooo / i1iII11iiIii
def OOO0o ( text , start_with , end_with ) :
 II1iIi11 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return II1iIi11
def IiiiIiii11 ( ) :
 OO0000o = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 OO0000o . connect ( ( '8.8.8.8' , 0 ) )
 OO0000o = OO0000o . getsockname ( ) [ 0 ]
 return OO0000o
 if 42 - 42: i1I1i1Ii11
def oo000O0OoooO ( ) :
 open = IiI11iII1 ( 'http://canyouseeme.org/' )
 O0o = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( O0o . group ( ) )
I1i11II1i = oO0o0o0ooO0oO + 'player_api.php?username=%s&password=%s' % ( Oo0oO0ooo , i1 )
IIII11I1I = oO0o0o0ooO0oO + '/panel_api.php?username=%s&password=%s' % ( Oo0oO0ooo , i1 )
o0o0OoOo0O0OO = oO0o0o0ooO0oO + 'movie/%s/%s/' % ( Oo0oO0ooo , i1 )
iIi1I11I = oO0o0o0ooO0oO + 'live/%s/%s/' % ( Oo0oO0ooo , i1 )
Iii1 = '&action=get_live_categories'
ooO = oO0o0o0ooO0oO + 'player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( Oo0oO0ooo , i1 )
o0o00OOo0 = oO0o0o0ooO0oO + 'player_api.php?username=%s&password=%s&action=get_vod_categories' % ( Oo0oO0ooo , i1 )
I1IIii1 = oO0o0o0ooO0oO + 'enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( Oo0oO0ooo , i1 )
OO0o0oOOO0O = oO0o0o0ooO0oO + 'player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( Oo0oO0ooo , i1 )
iII1i11 = oO0o0o0ooO0oO + 'enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=' % ( Oo0oO0ooo , i1 )
Ooo = oO0o0o0ooO0oO + 'enigma2.php?username=%s&password=%s&type=get_live_categories' % ( Oo0oO0ooo , i1 )
def IiIIII1i11I ( ) :
 if Oo0oO0ooo == "insert_username" :
  OOO = iII1 ( )
  OOo = IIii11Ii1i1I ( )
  I1ii11iIi11i ( 'User' , OOO )
  I1ii11iIi11i ( 'Pass' , OOo )
  xbmc . executebuiltin ( 'Container.Refresh' )
  oOo0O = oO0o0o0ooO0oO + 'enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( OOO , OOo )
  oOo0O = IiI11iII1 ( oOo0O )
  if oOo0O == "" :
   Oooo0O = "[COLORsteelblue]Incorrect Login Details[/COLOR]"
   oo00O0oO0O0 = "[COLORsteelblue]Please Re-enter[/COLOR]"
   ooo0OO0O0Oo = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , Oooo0O , oo00O0oO0O0 , ooo0OO0O0Oo )
   IiIIII1i11I ( )
  else :
   Oooo0O = "[COLORsteelblue]Login Successful[/COLOR]"
   oo00O0oO0O0 = "[COLORsteelblue]Welcome to Gtv V2[/COLOR]"
   ooo0OO0O0Oo = ( '[COLORsteelblue]%s[/COLOR]' % OOO )
   xbmcgui . Dialog ( ) . ok ( 'Gtv V2' , Oooo0O , oo00O0oO0O0 , ooo0OO0O0Oo )
   xbmc . executebuiltin ( 'Container.Refresh' )
   I1I ( )
 else :
  I1I ( )
def iII1 ( ) :
 Ooo0O0oooo = xbmc . Keyboard ( '' , 'heading' , True )
 Ooo0O0oooo . setHeading ( 'Enter Username' )
 Ooo0O0oooo . setHiddenInput ( False )
 Ooo0O0oooo . doModal ( )
 if ( Ooo0O0oooo . isConfirmed ( ) ) :
  iiI = Ooo0O0oooo . getText ( )
  return iiI
 else :
  return False
  if 56 - 56: i1I1i1Ii11 . oO00OO0oo0 . O00
  if 39 - 39: O0 + O00oo0OO0oOOO
def IIii11Ii1i1I ( ) :
 Ooo0O0oooo = xbmc . Keyboard ( '' , 'heading' , True )
 Ooo0O0oooo . setHeading ( 'Enter Password' )
 Ooo0O0oooo . setHiddenInput ( False )
 Ooo0O0oooo . doModal ( )
 if ( Ooo0O0oooo . isConfirmed ( ) ) :
  iiI = Ooo0O0oooo . getText ( )
  return iiI
 else :
  return False
def OoOooOoO ( ) :
 I11i1I1I = oO0o0o0ooO0oO + "/get.php?username=" + Oo0oO0ooo + "&password=" + i1 + "&type=m3u_plus&output=ts"
 try :
  oO0Oo = urllib2 . urlopen ( I11i1I1I )
  print oO0Oo . getcode ( )
  oO0Oo . close ( )
  if 43 - 43: II111iiii . III1i1i / oO00OO0oo0
  pass
  if 20 - 20: O00
 except urllib2 . HTTPError , OOoOO00OOO0OO :
  print OOoOO00OOO0OO . getcode ( )
  Dialog . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLORsteelblue]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLORsteelblue]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def o0oO000oo ( ) :
 OoOooOoO ( )
 open = IiI11iII1 ( Ooo )
 o00o0 = OOO0o ( open , '<channel>' , '</channel>' )
 for IiI1 in o00o0 :
  Oo0O00Oo0o0 = O00O0oOO00O00 ( IiI1 , '<title>' , '</title>' )
  Oo0O00Oo0o0 = base64 . b64decode ( Oo0O00Oo0o0 )
  II1III1I1I1Ii = O00O0oOO00O00 ( IiI1 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  oO0o0O0OOOoo0 ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' , II1III1I1I1Ii , 14 , I11 + 'live_lists.png' , i1iIIi1 , '' )
def OOOOoO00o0O ( url ) :
 open = IiI11iII1 ( iII1i11 + url )
 o00o0 = OOO0o ( open , '<channel>' , '</channel>' )
 for IiI1 in o00o0 :
  Oo0O00Oo0o0 = O00O0oOO00O00 ( IiI1 , '<title>' , '</title>' )
  Oo0O00Oo0o0 = base64 . b64decode ( Oo0O00Oo0o0 )
  xbmc . log ( str ( Oo0O00Oo0o0 ) )
  i1Oo00 = O00O0oOO00O00 ( IiI1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  II1III1I1I1Ii = O00O0oOO00O00 ( IiI1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  ooOOoooooo = O00O0oOO00O00 ( IiI1 , '<description>' , '</description>' )
  ooOOoooooo = base64 . b64decode ( ooOOoooooo )
  I1I1I1IIi1III = '('
  II11IiiIII = ')'
  IiIiiI ( ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , II1III1I1I1Ii , 15 , i1Oo00 , i1i , ( '[COLORsteelblue]' + ooOOoooooo + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( II11IiiIII , '[COLORsteelblue]' ) . replace ( I1I1I1IIi1III , '[COLORorangered]' ) )
  if 58 - 58: iIii11I + ooOOOo0oo0O0 - O00
def i1i1ii ( url ) :
 url = url
 iII1ii1 = IiI11iII1 ( ooO + url )
 O00I1iI1 = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( iII1ii1 )
 for Oo0O00Oo0o0 , type , I1i1iiiI1 , iIIi in O00I1iI1 :
  oO0o00oo0 = ( iIi1I11I + I1i1iiiI1 + '.m3u8' ) . strip ( )
  IiIiiI ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' , oO0o00oo0 , 15 , ( iIIi ) . replace ( '\/' , '/' ) + 'jpg' , i1iIIi1 , type )
  ii1IIII ( 'tvshows' , 'Media Info 3' )
  if 59 - 59: III1i1i * i1iII11iiIii % II111iiii
  if 62 - 62: iIii1I11I1II1
def i1II ( ) :
 oO0o0O0OOOoo0 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , I1i11II1i + '&action=get_vod_streams' , 41 , I11 + 'live_lists.png' , i1iIIi1 , '' )
 iII1ii1 = IiI11iII1 ( o0o00OOo0 )
 O00I1iI1 = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( iII1ii1 )
 for Oo000o , Oo0O00Oo0o0 in O00I1iI1 :
  oO0o0O0OOOoo0 ( ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , Oo000o , 41 , I11 + 'live_lists.png' , i1iIIi1 , '' )
def iI1I ( url ) :
 open = IiI11iII1 ( I1IIii1 + url )
 o00o0 = OOO0o ( open , '<channel>' , '</channel>' )
 for IiI1 in o00o0 :
  if '<playlist_url>' in open :
   Oo0O00Oo0o0 = O00O0oOO00O00 ( IiI1 , '<title>' , '</title>' )
   II1III1I1I1Ii = O00O0oOO00O00 ( IiI1 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   IiIiiI ( str ( base64 . b64decode ( Oo0O00Oo0o0 ) ) . replace ( '?' , '' ) , II1III1I1I1Ii , 41 , icon , i1i , '' )
  else :
   if xbmcaddon . Addon ( ) . getSetting ( 'meta' ) == 'true' :
    try :
     Oo0O00Oo0o0 = O00O0oOO00O00 ( IiI1 , '<title>' , '</title>' )
     Oo0O00Oo0o0 = base64 . b64decode ( Oo0O00Oo0o0 )
     i1Oo00 = O00O0oOO00O00 ( IiI1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     url = O00O0oOO00O00 ( IiI1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     ooOOoooooo = O00O0oOO00O00 ( IiI1 , '<description>' , '</description>' )
     ooOOoooooo = base64 . b64decode ( ooOOoooooo )
     OooOoOo = O00O0oOO00O00 ( ooOOoooooo , 'PLOT:' , '\n' )
     III1I1Iii1iiI = O00O0oOO00O00 ( ooOOoooooo , 'CAST:' , '\n' )
     i1Iii11I1i = O00O0oOO00O00 ( ooOOoooooo , 'RATING:' , '\n' )
     ooo00OOOooO = O00O0oOO00O00 ( ooOOoooooo , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
     ooo00OOOooO = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( ooo00OOOooO )
     Oo00o0OO0O00o = O00O0oOO00O00 ( ooOOoooooo , 'DURATION_SECS:' , '\n' )
     O0Oooo = O00O0oOO00O00 ( ooOOoooooo , 'GENRE:' , '\n' )
     iiIi1i ( str ( Oo0O00Oo0o0 ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 15 , i1Oo00 , i1i , OooOoOo , str ( ooo00OOOooO ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( III1I1Iii1iiI ) . split ( ) , i1Iii11I1i , Oo00o0OO0O00o , O0Oooo )
    except : pass
    xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   else :
    Oo0O00Oo0o0 = O00O0oOO00O00 ( IiI1 , '<title>' , '</title>' )
    Oo0O00Oo0o0 = base64 . b64decode ( Oo0O00Oo0o0 )
    i1Oo00 = O00O0oOO00O00 ( IiI1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    url = O00O0oOO00O00 ( IiI1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    ooOOoooooo = O00O0oOO00O00 ( IiI1 , '<description>' , '</description>' )
    IiIiiI ( Oo0O00Oo0o0 , url , 15 , i1Oo00 , i1i , base64 . b64decode ( ooOOoooooo ) )
I1i11111i1i11 = 'Thank you for choosing Gtv V2.\r\n\r\nContact us @\r\n\r\n Website: https://genietv.co.uk/ \r\n\r\n Facebook: https://www.facebook.com/groups/GenieTv/ \r\n\r\n Email: genietvmedia@gmail.com'
if 77 - 77: oO00OO0oo0 + IIIIII11i1I / III1i1i + O0 * ooOOOo0oo0O0
def I1ii11 ( ) :
 oOoOoOoo0 = IiI11iII1 ( I1i11II1i )
 O00I1iI1 = re . compile ( '"username":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 III1ii1I = re . compile ( '"password":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 Ii1i1iI = re . compile ( '"status":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 IIiI1 = re . compile ( '"exp_date":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 i1iI1 = re . compile ( '"active_cons":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 ii1 = re . compile ( '"created_at":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 I1IiiI1ii1i = re . compile ( '"max_connections":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 O0ooO0OoO00o = re . compile ( '"is_trial":"1"' ) . findall ( oOoOoOoo0 )
 II1iiiiII = re . compile ( '"is_trial":"0"' ) . findall ( oOoOoOoo0 )
 O0OoOO0oo0 = re . compile ( '"timezone":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 oOO = re . compile ( '"time_now":"([^"]*)"' ) . findall ( oOoOoOoo0 )
 O0o = IiiiIiii11 ( )
 O0o0OO0000ooo = oo000O0OoooO ( )
 for Oo000o in O00I1iI1 :
  IiIiiI ( '[COLORsteelblue]My Account Information[/COLOR]' , '' , '' , I11 + 'live_lists.png' , i1i , '' )
  IiIiiI ( '[COLORsteelblue]Username:[/COLOR]  %s' % ( Oo000o ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in III1ii1I :
  IiIiiI ( '[COLORsteelblue]Password:[/COLOR]  %s' % ( Oo000o ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in Ii1i1iI :
  IiIiiI ( '[COLORsteelblue]Status:[/COLOR]  %s' % ( Oo000o ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in ii1 :
  dt = datetime . fromtimestamp ( float ( ii1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  IiIiiI ( '[COLORsteelblue]Created:[/COLOR]  %s' % ( dt ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in IIiI1 :
  dt = datetime . fromtimestamp ( float ( IIiI1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if Oo <= dt <= Oo + timedelta ( hours = 24 ) :
   IiIiiI ( '[COLORred]Expires Today[/COLOR]' , '' , '' , I11 + 'live_lists.png' , i1i , '' )
  IiIiiI ( '[COLORsteelblue]Expires:[/COLOR]  %s' % ( dt ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in i1iI1 :
  IiIiiI ( '[COLORsteelblue]Active Connection:[/COLOR]  %s' % ( Oo000o ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in I1IiiI1ii1i :
  IiIiiI ( '[COLORsteelblue]Max Connection:[/COLOR]  %s' % ( Oo000o ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in O0ooO0OoO00o :
  IiIiiI ( '[COLORsteelblue]Trial:[/COLOR] Yes' , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in II1iiiiII :
  IiIiiI ( '[COLORsteelblue]Trial:[/COLOR] No' , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in O0OoOO0oo0 :
  IiIiiI ( '[COLORsteelblue]Timezone:[/COLOR] %s' % ( Oo000o ) . replace ( '\/' , '/' ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 for Oo000o in oOO :
  IiIiiI ( '[COLORsteelblue]Time Now:[/COLOR] %s' % ( Oo000o ) , '' , '' , I11 + 'live_lists.png' , i1i , '' )
 IiIiiI ( '[COLORsteelblue]Sign up[/COLOR]' , '' , 50006 , I11 + 'live_lists.png' , i1i , '' )
def iIIII1iIIii ( ) :
 oOoOoOoo0 = IiI11iII1 ( oO0o0o0ooO0oO + 'panel_api.php?username=' + Oo0oO0ooo + '&password=' + i1 )
 O00I1iI1 = re . compile ( '"exp_date":"(.+?)"' ) . findall ( oOoOoOoo0 )
 for Oo000o in O00I1iI1 :
  dt = datetime . fromtimestamp ( float ( O00I1iI1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if Oo <= dt <= Oo + timedelta ( hours = 24 ) :
   II . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLORsteelblue]If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLORsteelblue]Please Visit [COLORred]' + oo0o0O00 + '[COLORsteelblue] To Purchase A licence[/COLOR]' )
   if 52 - 52: ooOOOo0oo0O0 % i1I1i1Ii11
def Oo000ooOOO ( ) :
 iII1ii1 = IiI11iII1 ( I1i11II1i + '&action=get_simple_data_table&stream_id=1309' )
 O00I1iI1 = re . compile ( '"id":"([^"]*)","epg_id":"([^"]*)","title":"([^"]*)","lang":"([^"]*)","start":"([^"]*)","end":"([^"]*)","description":"([^"]*)","channel_id":"([^"]*)"' , re . DOTALL ) . findall ( iII1ii1 )
 for id , OoOOoOooooOOo , Ii11i1I11i , I11i1 , IiIIII1i11I , iIiIIIIIii , ooOOoooooo , OOo0 in O00I1iI1 :
  IiIiiI ( '[COLORsteelblue]' + OOo0 + ' - ' + O0O ( Ii11i1I11i ) + ' - ' + I11i1 + '[/COLOR]' , id , 31 , I11 + 'catchup.png' , i1iIIi1 , IiIIII1i11I + '[CR]' + iIiIIIIIii + '[CR]' + O0O ( ooOOoooooo ) )
def ii11I1 ( url ) :
 url = o0o0OoOo0O0OO + id + '.mp4'
 oO0oo ( url )
def Ii111iIi1iIi ( url ) :
 iII1ii1 = IiI11iII1 ( url )
 O00I1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iII1ii1 )
 for url , IIIII , ooOOoooooo , o0ooOoO000oO , Oo0O00Oo0o0 in O00I1iI1 :
  if 'php' in url :
   oO0o0O0OOOoo0 ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' , url , 21 , I11 + '2.png' , I11 + '2.png' , ooOOoooooo )
  else :
   IiIiiI ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' , url , 15 , IIIII , o0ooOoO000oO , ooOOoooooo )
   xbmcplugin . addSortMethod ( iIii1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOoi1i11I1I1iii1 ( url ) :
 iII1ii1 = IiI11iII1 ( url )
 O00I1iI1 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iII1ii1 )
 for IIIII , Oo0O00Oo0o0 , url in O00I1iI1 :
  url = ( ( O0O ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + Oo0oO0ooo + '/' + i1 + url ) . strip ( )
  IiIiiI ( ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(ULTIMATE ONLY)' , ' ' ) , url , 15 , IIIII , i1i , '' )
  if 8 - 8: i1i1i11IIi + II111iiii / OOOO00ooo0Ooo / i1iII11iiIii
  if 74 - 74: O0 / i1IIi
def OoOIiiiii111i1ii ( ) :
 IiIiiI ( '[COLORsteelblue]Delete Packages[/COLOR]' , '' , 6 , I11 + 'maintenance.png' , i1iIIi1 , '' )
 IiIiiI ( '[COLORsteelblue]Delete Cache[/COLOR]' , '' , 7 , I11 + 'maintenance.png' , i1iIIi1 , '' )
 IiIiiI ( '[COLORsteelblue]View Log File[/COLOR]' , '' , 50000 , I11 + 'maintenance.png' , i1iIIi1 , '' )
 IiIiiI ( '[COLORsteelblue]Force Refresh[/COLOR]' , '' , 50001 , I11 + 'maintenance.png' , i1iIIi1 , '' )
 IiIiiI ( '[COLORsteelblue]Force Close[/COLOR]' , '' , 8 , I11 + 'maintenance.png' , i1iIIi1 , '' )
 if 25 - 25: i1iiI11I - i1i1i11IIi / i11iIiiIii
 if 41 - 41: i1IIi % OOOO00ooo0Ooo + iIii1I11I1II1
 if 2 - 2: iIii1I11I1II1 * i1I1i1Ii11 % III1i1i - II111iiii - OOOO00ooo0Ooo
def iIi11iiIiI1I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def Iiii ( url ) :
 if url == 'http://' : return False
 try :
  oooOOoooo = urllib2 . Request ( url )
  oooOOoooo . add_header ( 'User-Agent' , Iii1ii1II11i )
  O0000OOO0 = urllib2 . urlopen ( oooOOoooo )
  O0000OOO0 . close ( )
 except Exception , OOoOO00OOO0OO :
  return OOoOO00OOO0OO
 return True
def ooo0 ( ) :
 oOoOoOoo0 = IiI11iII1 ( oOo0oooo00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O00I1iI1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOoOoOoo0 )
 for Oo0O00Oo0o0 , Oo000o , iIIi , i1i , oO000oOo00o0o in O00I1iI1 :
  IiIiiI ( Oo0O00Oo0o0 , Oo000o , 60002 , iIIi , I11 + 'apks.png' , oO000oOo00o0o )
  if 85 - 85: OOOO00ooo0Ooo + OoooooooOO * OOOO00ooo0Ooo - O00oo0OO0oOOO % i11iIiiIii
def OOo00OoO ( name , url ) :
 if iIi11iiIiI1I ( ) == 'android' :
  iIi1 = II . yesno ( iI1Ii11111iIi , "Would you like to download and install:" , "%s" % name )
  if not iIi1 : oO00ooO0o0 ( iI1Ii11111iIi , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  i11iiI1111 = name
  if iIi1 :
   if not os . path . exists ( o00 ) : os . makedirs ( o00 )
   if not Iiii ( url ) == True : oO00ooO0o0 ( iI1Ii11111iIi , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   IiII . create ( iI1Ii11111iIi , 'Downloading %s' % i11iiI1111 , '' , 'Please Wait' )
   oOoooo000Oo00 = os . path . join ( o00 , "%s.apk" % name )
   try : os . remove ( oOoooo000Oo00 )
   except : pass
   downloader . download ( url , oOoooo000Oo00 , IiII )
   xbmc . sleep ( 500 )
   IiII . close ( )
   II . ok ( iI1Ii11111iIi , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOoooo000Oo00 + '")' )
  else : oO00ooO0o0 ( iI1Ii11111iIi , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oO00ooO0o0 ( iI1Ii11111iIi , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 93 - 93: oO00OO0oo0 / O00 / iIii1I11I1II1 % O00oo0OO0oOOO % O00oo0OO0oOOO
 if 40 - 40: i11iIiiIii * O00oo0OO0oOOO - i1IIi * O00oo0OO0oOOO - i1iII11iiIii . i1IIi
 if 99 - 99: O0 * i1iII11iiIii
def Ooooooo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
 I1IIIiI1I1ii1 . ok ( "plugin.video.GtvV2" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By plugin.video.GtvV2[/COLOR]" )
 return
 if 30 - 30: O0 * OoooooooOO
def I1iIIIi1 ( url ) :
 print '###' + iI1Ii11111iIi + ' - DELETING Addons20.db ###'
 Iii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 I1iiiiI1iI = os . path . join ( Iii , 'Addons20.db' )
 try :
  os . remove ( I1iiiiI1iI )
  I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
  print '=== ' + iI1Ii11111iIi + ' - DELETING    ' + str ( I1iiiiI1iI ) + '    ==='
  I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
  I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "       No File To Remove" )
 return
 if 43 - 43: III1i1i - OoooooooOO
 if 3 - 3: O0 / OOOO00ooo0Ooo
 if 31 - 31: i1iiI11I + ooOOOo0oo0O0 . OoooooooOO
 if 89 - 89: II111iiii + i1IIi + II111iiii
def IiII1II11I ( ) :
 if i1 == 'insert_password' :
  II . ok ( '[COLORsteelblue]plugin.video.GtvV2 Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]' + oo0o0O00 + '[/COLOR]' )
  iIiiiI . openSettings ( sys . argv [ 0 ] )
 else :
  iIIII1iIIii ( )
  if 54 - 54: OOooOooo + O0 + i1iII11iiIii * O00oo0OO0oOOO - i1iiI11I % III1i1i
def IiI11iII1 ( url ) :
 oooOOoooo = urllib2 . Request ( url )
 oooOOoooo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0000OOO0 = urllib2 . urlopen ( oooOOoooo )
 oOoOoOoo0 = O0000OOO0 . read ( )
 O0000OOO0 . close ( )
 return oOoOoOoo0
def I111 ( ) :
 Oo000o = oO
 iI1I1i11iIIii = II . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIIIiI111I = iI1I1i11iIIii . lower ( )
 iII1ii1 = IiI11iII1 ( Oo000o )
 iIIIIIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iII1ii1 )
 for Oo000o , IIIII , ooOOoooooo , o0ooOoO000oO , Oo0O00Oo0o0 in iIIIIIii :
  if IIIIIiI111I in Oo0O00Oo0o0 . lower ( ) :
   IiIiiI ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' , Oo000o , 15 , IIIII , o0ooOoO000oO , ooOOoooooo )
   IiII . create ( '[COLORsteelblue]' + iI1Ii11111iIi + '[/COLOR]' , "Checking Library" , '' , 'Please Wait' )
   IiII . update ( 53 , "" , "Getting Movie Links" )
   if 15 - 15: i11iIiiIii % O00 * i1iII11iiIii / O00oo0OO0oOOO
  ii1IIII ( 'tvshows' , 'Media Info 3' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 90 - 90: OOOO00ooo0Ooo
  if 31 - 31: i1iiI11I + O0
def oO0oOOoo00000 ( ) :
 oOoOoOoo0 = IiI11iII1 ( Oo0o0000o0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00I1iI1 = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( oOoOoOoo0 )
 for Oo0O00Oo0o0 , Oo000o , oOo00 , i1i , i1iI11i1IIi in O00I1iI1 :
  IiIiiI ( '[COLORsteelblue]' + Oo0O00Oo0o0 + '[/COLOR]' , Oo000o , 20 , oOo00 , i1i , i1iI11i1IIi )
 ii1IIII ( 'movies' , 'MAIN' )
def ii1IIi111 ( url ) :
 Iii = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 IiII = xbmcgui . DialogProgress ( )
 IiII . create ( "plugin.video.GtvV2" , "Downloading Files" , '' , 'Please Wait' )
 oOoooo000Oo00 = os . path . join ( Iii , 'plugin.video.GtvV2' + '.zip' )
 try :
  os . remove ( oOoooo000Oo00 )
 except :
  pass
 downloader . download ( url , oOoooo000Oo00 , IiII )
 iI1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 IiII . update ( 0 , "" , "plugin.video.GtvV2 Is Now Installing Files Please Wait" )
 print '======================================='
 print iI1
 print '======================================='
 extract . all ( oOoooo000Oo00 , iI1 , IiII )
 OoOo00o0OO ( url )
 I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
 I1IIIiI1I1ii1 . ok ( "plugin.video.GtvV2" , "Press ok to force close plugin.video.GtvV2, If unsuccessful Please press home button got to settings/apps and force close plugin.video.GtvV2 and clear cache. " , "[COLOR yellow]Brought To You By plugin.video.GtvV2[/COLOR]" )
 ii1IIIIiI11 ( )
def OoOo00o0OO ( url ) :
 print '###' + iI1Ii11111iIi + ' - DELETING PACKAGES###'
 iI1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i11ii11 , OO00O0oOO , Ii1iI111 in os . walk ( iI1IIIii ) :
   O0oooo00o0Oo = 0
   O0oooo00o0Oo += len ( Ii1iI111 )
   if 36 - 36: iIii11I / II111iiii / OOooOooo / OOooOooo + oO00OO0oo0
   if 95 - 95: OOooOooo
   if O0oooo00o0Oo > 0 :
    if 51 - 51: II111iiii + OOooOooo . i1IIi . oO00OO0oo0 + o0o0OOO0o0 * O00
    I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
    if I1IIIiI1I1ii1 . yesno ( "Delete Package Cache Files" , str ( O0oooo00o0Oo ) + " files found" , "Do you want to delete them?" ) :
     if 72 - 72: III1i1i + III1i1i / II111iiii . OoooooooOO % iIii11I
     for Oo0O in Ii1iI111 :
      os . unlink ( os . path . join ( I1i11ii11 , Oo0O ) )
     for III in OO00O0oOO :
      shutil . rmtree ( os . path . join ( I1i11ii11 , III ) )
     I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
     I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "       Deleting Packages all done" )
    else :
     pass
   else :
    I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
    I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "       No Packages to DELETE" )
 except :
  I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
  I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "Error Deleting Packages please visit The Support Group, plugin.video.GtvV2 on facebook" )
 IiiIii ( url )
 return
def IiiIii ( url ) :
 oOo0OoOOo0 = os . path . join ( I1i1iiI1 , 'addon_data' )
 iII11I1Ii1 = [
 ( oOo0OoOOo0 ) ,
 ( oo00 ) ,
 ( os . path . join ( O0oo0OO0 , 'cache' ) ) ,
 ( os . path . join ( O0oo0OO0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo00 , 'plugin.video.GtvV2' , 'Images' ) ) ,
 ( os . path . join ( oOo0OoOOo0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0OoOOo0 , 'plugin.video.GtvV2' , 'Images' ) ) ]
 if 92 - 92: i1iII11iiIii / i1iII11iiIii . oO00OO0oo0
 ii1iIi1II = 0
 if 2 - 2: i1I1i1Ii11 + o0o0OOO0o0 - i1iiI11I . O00 - i1iiI11I
 for oo0o0oooo in iII11I1Ii1 :
  if os . path . exists ( oo0o0oooo ) and not oo0o0oooo in [ oo00 , oOo0OoOOo0 ] :
   for I1i11ii11 , OO00O0oOO , Ii1iI111 in os . walk ( oo0o0oooo ) :
    O0oooo00o0Oo = 0
    O0oooo00o0Oo += len ( Ii1iI111 )
    if O0oooo00o0Oo > 0 :
     for Oo0O in Ii1iI111 :
      if not Oo0O in iiIIIII1i1iI :
       try :
        os . unlink ( os . path . join ( I1i11ii11 , Oo0O ) )
       except :
        pass
      else : OOo0oO00ooO00 ( 'Ignore Log File: %s' % Oo0O )
     for III in OO00O0oOO :
      try :
       shutil . rmtree ( os . path . join ( I1i11ii11 , III ) )
       ii1iIi1II += 1
       OOo0oO00ooO00 ( "[Success] cleared %s files from %s" % ( str ( O0oooo00o0Oo ) , os . path . join ( oo0o0oooo , III ) ) )
      except :
       OOo0oO00ooO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( oo0o0oooo , III ) )
  else :
   for I1i11ii11 , OO00O0oOO , Ii1iI111 in os . walk ( oo0o0oooo ) :
    for III in OO00O0oOO :
     if 'cache' in III . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( I1i11ii11 , III ) )
       ii1iIi1II += 1
       OOo0oO00ooO00 ( "[Success] wiped %s " % os . path . join ( oo0o0oooo , III ) )
      except :
       OOo0oO00ooO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( oo0o0oooo , III ) )
       if 20 - 20: i1IIi - i1iII11iiIii
 oO00ooO0o0 ( iI1Ii11111iIi , 'Clear Cache: Removed %s Files' % ii1iIi1II )
def ii1ii11 ( url ) :
 print '###' + iI1Ii11111iIi + ' - DELETING PACKAGES###'
 iI1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i11ii11 , OO00O0oOO , Ii1iI111 in os . walk ( iI1IIIii ) :
   O0oooo00o0Oo = 0
   O0oooo00o0Oo += len ( Ii1iI111 )
   if 84 - 84: O0 . i1iII11iiIii - II111iiii . i1i1i11IIi / II111iiii
   if 47 - 47: OoooooooOO
   if O0oooo00o0Oo > 0 :
    if 4 - 4: O00 % i1iII11iiIii
    I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
    if I1IIIiI1I1ii1 . yesno ( "Delete Package Cache Files" , str ( O0oooo00o0Oo ) + " files found" , "Do you want to delete them?" ) :
     if 10 - 10: OOooOooo . OoooooooOO - IIIIII11i1I + OOooOooo - O0
     for Oo0O in Ii1iI111 :
      os . unlink ( os . path . join ( I1i11ii11 , Oo0O ) )
     for III in OO00O0oOO :
      shutil . rmtree ( os . path . join ( I1i11ii11 , III ) )
     I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
     I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "       Deleting Packages all done" )
    else :
     pass
   else :
    I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
    I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "       No Packages to DELETE" )
 except :
  I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
  I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "Error Deleting Packages" )
 return
 if 82 - 82: i1i1i11IIi + II111iiii
def ii1IIIIiI11 ( ) :
 I1IIIiI1I1ii1 = xbmcgui . Dialog ( )
 II1i1i1iII1 = I1IIIiI1I1ii1 . yesno ( 'Force Close plugin.video.GtvV2' , 'You are about to close plugin.video.GtvV2' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if II1i1i1iII1 == 0 : return
 elif II1i1i1iII1 == 1 : pass
 oOo000 = iIi11iiIiI1I ( )
 OOo0oO00ooO00 ( "Platform: " + str ( oOo000 ) )
 os . _exit ( 1 )
 OOo0oO00ooO00 ( "Force close failed!  Trying alternate methods." )
 if oOo000 == 'osx' :
  OOo0oO00ooO00 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  I1IIIiI1I1ii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oOo000 == 'linux' :
  OOo0oO00ooO00 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  I1IIIiI1I1ii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oOo000 == 'android' :
  OOo0oO00ooO00 ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.plugin.video.GtvV2' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.plugin.video.GtvV2' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.plugin.video.GtvV2());' )
  except : pass
  I1IIIiI1I1ii1 . ok ( iI1Ii11111iIi , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif oOo000 == 'windows' :
  OOo0oO00ooO00 ( "############ try windows force close #################" )
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
  I1IIIiI1I1ii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  OOo0oO00ooO00 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  OOo0oO00ooO00 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  I1IIIiI1I1ii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 14 - 14: IIIIII11i1I . II111iiii . i1iII11iiIii / iIii11I % oO00OO0oo0 - i1i1i11IIi
def oO0oo ( url ) :
 import urlresolver
 try :
  o0oOoO0O = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( o0oOoO0O , xbmcgui . ListItem ( Oo0O00Oo0o0 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( Oo0O00Oo0o0 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "Gtv V2" , "unplayable stream" )
   sys . exit ( )
def iIi11iiIiI1I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 84 - 84: O0 * OoooooooOO - OOooOooo * OOooOooo
def OOo0oO00ooO00 ( log ) :
 xbmc . log ( "[%s]: %s" % ( iI1Ii11111iIi , log ) )
 if not os . path . exists ( oo00 ) : os . makedirs ( oo00 )
 if not os . path . exists ( o0oOoO00o ) : Oo0O = open ( o0oOoO00o , 'w' ) ; Oo0O . close ( )
 with open ( o0oOoO00o , 'a' ) as Oo0O :
  i1ii = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  Oo0O . write ( i1ii . rstrip ( '\r\n' ) + '\n' )
  if 65 - 65: o0o0OOO0o0 / IIIIII11i1I % OOooOooo
def iIiIIii ( ) :
 try :
  OOo00 = getSet ( "core-player" )
  if ( OOo00 == 'DVDPLAYER' ) : iIII = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OOo00 == 'MPLAYER' ) : iIII = xbmc . PLAYER_CORE_MPLAYER
  elif ( OOo00 == 'PAPLAYER' ) : iIII = xbmc . PLAYER_CORE_PAPLAYER
  else : iIII = xbmc . PLAYER_CORE_AUTO
 except : iIII = xbmc . PLAYER_CORE_AUTO
 return iIII
 return True
def Ii1iI11iI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i11I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO0 = True
 O0i1II1Iiii1I11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0i1II1Iiii1I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0i1II1Iiii1I11 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOO0oOOo00O = [ ]
  if showcontext == 'fav' :
   OOO0oOOo00O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in II11iiii1Ii :
   OOO0oOOo00O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  O0i1II1Iiii1I11 . addContextMenuItems ( OOO0oOOo00O )
 OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11I1II , listitem = O0i1II1Iiii1I11 , isFolder = False )
 return OO0
 if 51 - 51: oO00OO0oo0 / iIii1I11I1II1 % III1i1i + ooOOOo0oo0O0 * i1i1i11IIi + O00oo0OO0oOOO
def iiIi1i ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 i11I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 OO0 = True
 O0i1II1Iiii1I11 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0i1II1Iiii1I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 O0i1II1Iiii1I11 . setProperty ( 'fanart_image' , fanart )
 O0i1II1Iiii1I11 . setProperty ( "IsPlayable" , "true" )
 o0OoO00o0000O = [ ]
 o0OoO00o0000O . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 o0OoO00o0000O . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 O0i1II1Iiii1I11 . addContextMenuItems ( o0OoO00o0000O , replaceItems = True )
 OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11I1II , listitem = O0i1II1Iiii1I11 , isFolder = False )
 return OO0
def oO0o0O0OOOoo0 ( name , url , mode , iconimage , fanart , description ) :
 if 21 - 21: O00 / i1i1i11IIi % i1i1i11IIi - ooOOOo0oo0O0
 i11I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO0 = True
 O0i1II1Iiii1I11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0i1II1Iiii1I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0i1II1Iiii1I11 . setProperty ( "Fanart_Image" , fanart )
 OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11I1II , listitem = O0i1II1Iiii1I11 , isFolder = True )
 return OO0
 if 70 - 70: i1I1i1Ii11 . o0o0OOO0o0
def IiIiiI ( name , url , mode , iconimage , fanart , description ) :
 if 58 - 58: i1iII11iiIii + II111iiii * OOOO00ooo0Ooo * i11iIiiIii - iIii1I11I1II1
 i11I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO0 = True
 O0i1II1Iiii1I11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0i1II1Iiii1I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0i1II1Iiii1I11 . setProperty ( "Fanart_Image" , fanart )
 OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11I1II , listitem = O0i1II1Iiii1I11 , isFolder = False )
 return OO0
 if 68 - 68: OoooooooOO % II111iiii
def Ii1i1i1111 ( ) :
 o0oO0O00oOo = [ ]
 I1111I1II11 = sys . argv [ 2 ]
 if len ( I1111I1II11 ) >= 2 :
  iiiIIIIiIi = sys . argv [ 2 ]
  IiiIIIII1iii = iiiIIIIiIi . replace ( '?' , '' )
  if ( iiiIIIIiIi [ len ( iiiIIIIiIi ) - 1 ] == '/' ) :
   iiiIIIIiIi = iiiIIIIiIi [ 0 : len ( iiiIIIIiIi ) - 2 ]
  IIiiii = IiiIIIII1iii . split ( '&' )
  o0oO0O00oOo = { }
  for iI111i1I1II in range ( len ( IIiiii ) ) :
   O00OO = { }
   O00OO = IIiiii [ iI111i1I1II ] . split ( '=' )
   if ( len ( O00OO ) ) == 2 :
    o0oO0O00oOo [ O00OO [ 0 ] ] = O00OO [ 1 ]
    if 29 - 29: i1I1i1Ii11 % IIIIII11i1I % OOooOooo . ooOOOo0oo0O0 / OoooooooOO * i1i1i11IIi
 return o0oO0O00oOo
 if 54 - 54: O0
 if 68 - 68: IIIIII11i1I * ooOOOo0oo0O0 . i1i1i11IIi % III1i1i % O00oo0OO0oOOO
iiiIIIIiIi = Ii1i1i1111 ( )
Oo000o = None
Oo0O00Oo0o0 = None
oooo0OO = None
oOo00 = None
i1i = None
i1iI11i1IIi = None
iIIi1I = None
if 65 - 65: oO00OO0oo0 % O0 % iIii1I11I1II1 * iIii11I
if 31 - 31: iIii11I
try :
 iIIi1I = int ( iiiIIIIiIi [ "fav_mode" ] )
except :
 pass
 if 44 - 44: o0o0OOO0o0 - iIii1I11I1II1 - i1I1i1Ii11
try :
 Oo000o = urllib . unquote_plus ( iiiIIIIiIi [ "url" ] )
except :
 pass
try :
 Oo0O00Oo0o0 = urllib . unquote_plus ( iiiIIIIiIi [ "name" ] )
except :
 pass
try :
 oOo00 = urllib . unquote_plus ( iiiIIIIiIi [ "iconimage" ] )
except :
 pass
try :
 oooo0OO = int ( iiiIIIIiIi [ "mode" ] )
except :
 pass
try :
 i1i = urllib . unquote_plus ( iiiIIIIiIi [ "fanart" ] )
except :
 pass
try :
 i1iI11i1IIi = urllib . unquote_plus ( iiiIIIIiIi [ "description" ] )
except :
 pass
 if 80 - 80: iIii1I11I1II1 * O00oo0OO0oOOO % i1iII11iiIii % i1I1i1Ii11
 if 95 - 95: iIii1I11I1II1 - oO00OO0oo0 . O00oo0OO0oOOO - O00
print str ( i1iiIII111ii ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( oooo0OO )
print "URL: " + str ( Oo000o )
print "Name: " + str ( Oo0O00Oo0o0 )
print "IconImage: " + str ( oOo00 )
if 75 - 75: IIIIII11i1I + ooOOOo0oo0O0 - i1IIi . OoooooooOO * iIii11I / OOooOooo
if 86 - 86: o0o0OOO0o0 * II111iiii - O0 . o0o0OOO0o0 % iIii1I11I1II1 / i1iiI11I
def ii1IIII ( content , viewType ) :
 if 11 - 11: O00 * III1i1i + oO00OO0oo0 / oO00OO0oo0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if iIiiiI . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iIiiiI . getSetting ( viewType ) )
  if 37 - 37: i11iIiiIii + i1IIi
  if 23 - 23: OOOO00ooo0Ooo + i1iII11iiIii . o0o0OOO0o0 * O00 + oO00OO0oo0
if oooo0OO == None : iiii ( )
elif oooo0OO == 1 : Genres ( )
elif oooo0OO == 2 : Lists ( Oo000o , oOo00 )
elif oooo0OO == 3 : all_mov ( )
elif oooo0OO == 4 : I111 ( )
elif oooo0OO == 5 : OoOIiiiii111i1ii ( )
elif oooo0OO == 6 : ii1ii11 ( Oo000o )
elif oooo0OO == 7 : IiiIii ( Oo000o )
elif oooo0OO == 8 : ii1IIIIiI11 ( )
elif oooo0OO == 9 : I1I ( )
elif oooo0OO == 10 : I1ii11 ( )
elif oooo0OO == 11 : TvGuide ( )
elif oooo0OO == 12 : IiII1II11I ( )
elif oooo0OO == 13 : ReCreate_Addon_ini ( )
elif oooo0OO == 14 : OOOOoO00o0O ( Oo000o )
elif oooo0OO == 144 : i1i1ii ( Oo000o )
elif oooo0OO == 15 : oO0oo ( Oo000o )
elif oooo0OO == 16 : o0oO000oo ( )
elif oooo0OO == 17 : Live_Events ( Oo0O00Oo0o0 )
elif oooo0OO == 18 : iIiiiI . openSettings ( sys . argv [ 0 ] )
elif oooo0OO == 19 : oO0oOOoo00000 ( )
elif oooo0OO == 20 : ii1IIi111 ( Oo000o )
elif oooo0OO == 30 : Oo000ooOOO ( )
elif oooo0OO == 31 : ii11I1 ( Oo000o )
elif oooo0OO == 40 : i1II ( )
elif oooo0OO == 41 : iI1I ( Oo000o )
elif oooo0OO == 21 : Ii111iIi1iIi ( Oo000o )
elif oooo0OO == 22 : OOoi1i11I1I1iii1 ( Oo000o )
elif oooo0OO == 50 : oO0O00OoOO0 ( )
elif oooo0OO == 51 : iiiIi1 ( Oo000o )
elif oooo0OO == 50000 : I1i1Iiiii ( )
elif oooo0OO == 50001 : Ooooooo ( )
elif oooo0OO == 50002 : I1iIIIi1 ( Oo000o )
elif oooo0OO == 50006 : I1iI1ii1II ( iI1Ii11111iIi , I1i11111i1i11 )
elif oooo0OO == 60001 : ooo0 ( )
elif oooo0OO == 60002 : OOo00OoO ( Oo0O00Oo0o0 , Oo000o )
elif oooo0OO == 211 : oO0O00oOOoooO ( )
elif oooo0OO == 212 : I1i1i1iii ( )
elif oooo0OO == 213 : i1i1iI1iiiI ( )
elif oooo0OO == 214 : OOOOo0 ( )
elif oooo0OO == 90026 : O00oO ( )
elif oooo0OO == 90027 : iII ( Oo0O00Oo0o0 , Oo000o , i1iI11i1IIi )
elif oooo0OO == 90028 : II1I ( Oo000o )
elif oooo0OO == 40099 : IiIIII1i11I ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
