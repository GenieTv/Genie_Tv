# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata , socket , random
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle
from imports import yt
import xml . etree . ElementTree as ElementTree
import httplib
import liveresolver
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
from imports . jsunpack import unpack as packets
from imports . common import random_agent
from imports import Parse , CNF_Studio_Indexer , speedtest , uservar , tools
try :
 import StorageServer
except :
 import storageserverdummy as StorageServer
oo000 = StorageServer . StorageServer ( "plugin.video.GenieTv" , 24 )
try :
 import json
except :
 import simplejson as json
from threading import Thread
from datetime import date , datetime , timedelta
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from imports . tvGuide import gui
import webbrowser
import SimpleDownloader
if 9 - 9: Ii . o0o00Oo0O - iI11I1II1I1I
if 71 - 71: ii
iIIii1IIi = ''
def o0OO00 ( i , t1 , t2 = [ ] ) :
 oo = iIIii1IIi
 for i1iII1IiiIiI1 in t1 :
  oo += chr ( i1iII1IiiIiI1 )
  i += 1
  if i > 1 :
   oo = oo [ : - 1 ]
   i = 0
 for i1iII1IiiIiI1 in t2 :
  oo += chr ( i1iII1IiiIiI1 )
  i += 1
  if i > 1 :
   oo = oo [ : - 1 ]
   i = 0
 return oo
 if 40 - 40: ooOoO0O00 * IIiIiII11i
 if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
I1IiI = "3.7.3"
o0OOO = 'plugin.video.GenieTv'
iIiiiI = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
Iii1ii1II11i = xbmc . translatePath ( 'special://home/addons/' )
iI111iI = xbmc . translatePath ( 'special://home/addonsbroke/' )
IiII = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
iI1Ii11111iIi = 'plugin.video.GenieTv'
i1i1II = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
O0oo0OO0 = xbmcaddon . Addon ( id = iI1Ii11111iIi )
I1i1iiI1 = xbmc . translatePath ( 'special://home/media' )
iiIIIII1i1iI = 'plugin.video.GenieTv'
o0oO0 = xbmcgui . DialogProgress ( )
oo00 = '[COLORsteelblue]GenieTv[/COLOR]'
o00 = base64 . b64decode ( 'aHR0cDovL2dlbmlldHYuY28udWsvc3BlZWR0ZXN0LnR4dA==' )
Oo0oO0ooo = uservar . CONTACT
o0oOoO00o = base64 . decodestring
i1 = xbmcaddon . Addon ( ) . setSetting
oOOoo00O0O = ( o0oOoO00o ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIv' ) )
i1111 = xbmc . translatePath ( 'special://home/' )
i11 = os . path . join ( i1111 , 'userdata' )
I11 = os . path . join ( i11 , 'addon_data' , o0OOO )
Oo0o0000o0o0 = os . path . join ( I11 , 'wizard.log' )
oOo0oooo00o = uservar . ADDONTITLE
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://profile/' )
oo0o0O00 = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
Iii1ii1II11i = os . path . join ( i1111 , 'addons' )
oO = os . path . join ( Iii1ii1II11i , 'packages' )
i1iiIIiiI111 = os . path . join ( i11 , 'Thumbnails' )
oooOOOOO = os . path . join ( i11 , 'Database' )
i1iiIII111ii = os . path . join ( Iii1ii1II11i , 'HUB' )
i1iIIi1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
ii11iIi1I = Net ( )
iI111I11I1I1 = xbmcgui . Dialog ( )
OOooO0OOoo = O0oo0OO0 . getSetting ( 'Build' )
iIii1 = O0oo0OO0 . getSetting ( 'Local' )
oOOoO0 = O0oo0OO0 . getSetting ( 'Remote' )
O0OoO000O0OO = O0oo0OO0 . getSetting ( 'LocalM3u' )
iiI1IiI = O0oo0OO0 . getSetting ( 'TEXTCOL' )
II = O0oo0OO0 . getSetting ( 'Downloads' )
ooOoOoo0O = xbmc . translatePath ( 'special://logpath/' )
OooO0 = O0oo0OO0 . getSetting ( 'User' )
II11iiii1Ii = O0oo0OO0 . getSetting ( 'Pass' )
OO0o = O0oo0OO0 . getSetting ( 'DNS' )
if OO0o == 'Option 1' :
 Ooo = '.net'
if OO0o == 'Option 2' :
 Ooo = '.eu'
if OO0o == 'Option 3' :
 Ooo = '.com'
O0o0Oo = O0oo0OO0 . getSetting ( 'AdultPass' )
iI111I11I1I1 = xbmcgui . Dialog ( )
i1111 = xbmc . translatePath ( 'special://home/' )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iI1Ii11111iIi , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iI1Ii11111iIi , 'icon.png' ) )
O00o0OO = ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
I11i1 = xbmc . translatePath ( 'special://database' )
iIi1ii1I1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
o0 = xbmc . translatePath ( 'special://thumbnails' ) ;
I11II1i = "GenieTv"
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
IIiiiiiiIi1I1 = 'http://'
I1IIIii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ2VuaWV0dl9hcnQvYmVuc19hcnQv' )
oOoOooOo0o0 = datetime . now ( )
OOOO = base64 . decodestring ( 'LnBocA==' )
OOO00 = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
iiiiiIIii = [ ]
O000OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
I11iii1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
I1IIiiIiii = O0oo0OO0 . getLocalizedString
O000oo0O = CookieJar ( )
OOOOi11i1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O000oo0O ) )
OOOOi11i1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
IIIii1II1II = int ( sys . argv [ 1 ] )
i1I1iI = xbmc . translatePath ( O0oo0OO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
oo0OooOOo0 = os . path . join ( iIi1ii1I1 , 'favorites' )
o0O = iIi1ii1I1 + '/addons.ini'
i11 = xbmc . translatePath ( 'special://home/userdata/' )
O00oO = xbmc . translatePath ( 'special://home/userdatabroke/' )
I11i1I1I = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
oO0Oo = xbmc . translatePath ( 'special://home/userdata/addon_data' )
oOOoo0Oo = oO0Oo + 'GenieTvWatched'
o00OO00OoO = ( o0oOoO00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
OOOO0OOoO0O0 = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
O0Oo000ooO00 = oOOoo0Oo + 'watched.txt'
if not os . path . exists ( oOOoo0Oo ) :
 os . makedirs ( oOOoo0Oo )
O0Oo000ooO00 = oOOoo0Oo + 'watched.txt'
if not os . path . exists ( O0Oo000ooO00 ) :
 open ( O0Oo000ooO00 , 'w+' )
oO0 = open ( O0Oo000ooO00 ) . read ( )
Ii1iIiII1ii1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
ooOooo000oOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
Oo0oOOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
Oo0OoO00oOO0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
OOO00O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
OOoOO0oo0ooO = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( oo0OooOOo0 ) == True :
 O0o0O00Oo0o0 = open ( oo0OooOOo0 ) . read ( )
else : O0o0O00Oo0o0 = [ ]
O00O0oOO00O00 = O0oo0OO0 . getSetting ( 'debug' )
if os . path . exists ( iIi1ii1I1 ) == False :
 os . makedirs ( iIi1ii1I1 )
def i1Oo00 ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI111I1iIiI = ''
 IIIi1I1IIii1II = ''
 try :
  iiI111I1iIiI = urllib2 . urlopen ( i1i )
  IIIi1I1IIii1II = iiI111I1iIiI . read ( )
  iiI111I1iIiI . close ( )
 except : pass
 if IIIi1I1IIii1II != '' :
  return IIIi1I1IIii1II
 else :
  IIIi1I1IIii1II = 'Failed'
  return IIIi1I1IIii1II
  if 65 - 65: oOo . iii1i1iiiiIi % ooo0O . oOoO0o00OO0
i1I1ii = [ ]
oOOo0 = i1Oo00 ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if oOOo0 != 'Failed' :
 i1I1ii . append ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not oOOo0 != 'Failed' :
 oo00O00oO = i1Oo00 ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if oo00O00oO != 'Failed' :
  i1I1ii . append ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not oo00O00oO != 'Failed' :
  iIiIIIi = i1Oo00 ( o0oOoO00o ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if iIiIIIi != 'Failed' :
   i1I1ii . append ( o0oOoO00o ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not iIiIIIi != 'Failed' :
   ooo00OOOooO = i1Oo00 ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if ooo00OOOooO != 'Failed' :
    i1I1ii . append ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
O00OOOoOoo0O = ( str ( i1I1ii ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
if 77 - 77: OOOo00oo0oO % OoOo0o . i1IiiiI1iI + i1iIi
if 68 - 68: iiiiiiii1 % I11i1ii1 / O0Oooo0O
if 84 - 84: oOOoOooOo . O0Oooo0O - i1IiiiI1iI + iiiiiiii1 % iI11I1II1I1I / ii
def Oo0O00O0O ( ) :
 if not os . path . exists ( iIiiiI ) :
  iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  OOooOoooOoOo = 'genie tv repo not being installed '
  o0OOOO00O0Oo ( )
 else :
  iioOooOOOoOo ( )
  if 41 - 41: i1iIi - o0o00Oo0O - o0o00Oo0O
def iioOooOOOoOo ( ) :
 if 68 - 68: OoOo0o % O0Oooo0O
 ooO00OO0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 iIiii1i111iI1 = open ( OOO00O ) . read ( )
 i11oO0oOo0 = open ( OOoOO0oo0ooO ) . read ( )
 if 45 - 45: iiiiiiii1 / iiiiiiii1 + O0Oooo0O + oOOoOooOo
 iI111i = re . compile ( 'version="([^"]*)" provider' ) . findall ( iIiii1i111iI1 )
 IIi11i1i1iI1 = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( i11oO0oOo0 )
 iiiIi1 = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( ooO00OO0 )
 i1I1ii11i1Iii = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( ooO00OO0 )
 for I1IiiiiI in iI111i :
  o0OIiII = I1IiiiiI
  for ii1iII1II in iiiIi1 :
   if not ii1iII1II == o0OIiII :
    o0oO0 . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oO0 . close
    Iii1I1I11iiI1 ( )
   if ii1iII1II == o0OIiII :
    I1I1i1I
 for ii1I in IIi11i1i1iI1 :
  O0oO0 = ii1I
  for oO0O0OO0O in i1I1ii11i1Iii :
   if not oO0O0OO0O == O0oO0 :
    o0oO0 . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oO0 . close
    o0OOOO00O0Oo ( )
   if oO0O0OO0O == O0oO0 :
    xbmc . sleep ( 100 )
    I1I1i1I
def OO ( ) :
 if not os . path . exists ( ooooooO0oo ) :
  OoOoO ( 'Change Log 24/04/2018 - v3.7.3' , '[COLORsteelblue]Free Live Tv Section Updated,[CR][COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
  os . makedirs ( ooooooO0oo )
def Ii1I1i ( ) :
 OoOoO ( 'Change Log 24/04/2018 - v3.7.3' , '[COLORsteelblue]Free Live Tv Section Updated,[CR][COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
def OOI1iI1ii1II ( ) :
 OoOoO ( Ooo , Ooo )
def OoOoO ( title , msg ) :
 class O0O0OOOOoo ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 74 - 74: oOoO0o00OO0 + IIiIiII11i / oOo
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 100 - 100: iii1i1iiiiIi * iI11I1II1I1I
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 86 - 86: oOo * OoOo0o . iiiiiiii1
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 32 - 32: ooo0O . I11i1ii1 * i1IiiiI1iI
 OOooo0oOO0O = O0O0OOOOoo ( "Textbox.xml" , O0oo0OO0 . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 OOooo0oOO0O . doModal ( )
 del OOooo0oOO0O
 if 62 - 62: oOo0O0Ooo
def O00o0OO0 ( ) :
 Oo0O00O0O ( )
 OO ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  IIi1I1iiiii ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Ultimate Live List[/COLOR]' , '' , 4009 , I1IIIii + 'GTV.png' , Oo00OOOOO , '[COLOR' + iiI1IiI + ']GenieTv Ultimate [COLORorangered][CR](Paid Service)[/COLOR]' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , I1IIIii + 'tommys.png' , Oo00OOOOO , 'Tommys Sports' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Free Live Tv[/COLOR]' , '' , 300000008 , I1IIIii + 'GTV.png' , Oo00OOOOO , 'Free Live Streams - [COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
  if O0oo0OO0 . getSetting ( 'Streams' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( O00OOOoOoo0O ) , 4002 , I1IIIii + 'Streams.png' , Oo00OOOOO , 'VOD Categories' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , I1IIIii + 'tools.png' , Oo00OOOOO , '' )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , I1IIIii + 'settings.png' , Oo00OOOOO , '' )
  if oOOo0O00o ( ) == 'android' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , str ( O00OOOoOoo0O ) , 30039 , I1IIIii + 'APKpng' , Oo00OOOOO , 'APK TOOL Install GenieTv Apps Direct To Your Box' )
  if O0oo0OO0 . getSetting ( 'Maintainance' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( O00OOOoOoo0O ) , 3 , I1IIIii + 'Maintenance.png' , Oo00OOOOO , 'MAINTENANCE' )
 iIiIi11 ( 'movies' , 'MAIN' )
def IIi1I1iiiii ( ) :
 Oo0O00O0O ( )
 OO ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Ultimate Live List[/COLOR]' , '' , 40099 , I1IIIii + 'GTV.png' , Oo00OOOOO , '[COLOR' + iiI1IiI + ']GenieTv Ultimate [COLORorangered][CR](Paid Service)[/COLOR]' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , I1IIIii + 'tommys.png' , Oo00OOOOO , 'Tommys Sports' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Free Live Tv[/COLOR]' , '' , 300000008 , I1IIIii + 'GTV.png' , Oo00OOOOO , 'Free Live Streams - [COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 if O0oo0OO0 . getSetting ( 'Streams' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( O00OOOoOoo0O ) , 4002 , I1IIIii + 'Streams.png' , Oo00OOOOO , 'VOD Categories' )
 if O0oo0OO0 . getSetting ( 'Maintainance' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( O00OOOoOoo0O ) , 3 , I1IIIii + 'Maintenance.png' , Oo00OOOOO , 'MAINTENANCE' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , I1IIIii + 'tools.png' , Oo00OOOOO , 'Tools' )
 iIiIi11 ( 'movies' , 'MAIN' )
def OOO ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if 32 - 32: ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
  if 62 - 62: ii * oOo0O0Ooo
  if O0oo0OO0 . getSetting ( 'Search' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( O00OOOoOoo0O ) , 9000 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'HeroVision' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie On Demand Streams[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zaGFrYS9HT0RTLnBocA==' ) ) , 1016 , I1IIIii + 'gods.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , I1IIIii + 'Bamf.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BOSS DOCS[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , I1IIIii + 'boss.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Supremacy[/COLOR]' , '' , 1131000 , I1IIIii + 'supremacy.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 4004 , I1IIIii + 'Movies.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( O00OOOoOoo0O ) , 4005 , I1IIIii + 'TVShows.png' , Oo00OOOOO , '' )
  if 58 - 58: iii1i1iiiiIi % ooo0O
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( O00OOOoOoo0O ) , 10001 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
  if 50 - 50: O0Oooo0O . ooo0O
  if 97 - 97: o0o00Oo0O + iii1i1iiiiIi
  if 89 - 89: ooo0O + oOo * i1IiiiI1iI * i1iIi
  if 37 - 37: ii - o0o00Oo0O - ooo0O
  if 77 - 77: OoOo0o * iI11I1II1I1I
  if 98 - 98: oOo0O0Ooo % i1iIi * ii
  if 51 - 51: iI11I1II1I1I . iii1i1iiiiIi / OOOo00oo0oO + ooo0O
 else :
  if 33 - 33: oOOoOooOo . IIiIiII11i % iiiiiiii1 + ooo0O
  if 71 - 71: I1ii11iIi11i % OoOo0o
  if O0oo0OO0 . getSetting ( 'Search' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( O00OOOoOoo0O ) , 9000 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie On Demand Streams[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zaGFrYS9HT0RTLnBocA==' ) ) , 1016 , I1IIIii + 'gods.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , I1IIIii + 'Bamf.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Supremacy[/COLOR]' , '' , 1131000 , I1IIIii + 'supremacy.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BOSS DOCS[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , I1IIIii + 'boss.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 4004 , I1IIIii + 'Movies.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( O00OOOoOoo0O ) , 4005 , I1IIIii + 'TVShows.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( O00OOOoOoo0O ) , 10001 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']COZY CORNER[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 21999990 , I1IIIii + 'zone.png' , Oo00OOOOO , '' )
  if 98 - 98: i1IiiiI1iI % Ii % oOOoOooOo + i1iIi
  if 78 - 78: oOoO0o00OO0 % OOOo00oo0oO / iiiiiiii1 - iI11I1II1I1I
  if 69 - 69: O0Oooo0O
  if 11 - 11: oOo0O0Ooo
  if 16 - 16: i1iIi + I11i1ii1 * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
  if 67 - 67: ii / oOo0O0Ooo * i1iIi + i1IiiiI1iI
  if 65 - 65: ii - oOoO0o00OO0 / oOOoOooOo / IIiIiII11i / ooOoO0O00
  if 71 - 71: O0Oooo0O + i1iIi
  if 28 - 28: OoOo0o
  if 38 - 38: oOOoOooOo % IIiIiII11i % i1IiiiI1iI / oOo + iii1i1iiiiIi / ooOoO0O00
  if 54 - 54: iI11I1II1I1I % oOoO0o00OO0 - OoOo0o / OOOo00oo0oO - oOo . i1IiiiI1iI
  if 11 - 11: oOoO0o00OO0 . oOo * I11i1ii1 * ii + oOOoOooOo
  if 33 - 33: o0o00Oo0O * ooo0O - O0Oooo0O % O0Oooo0O
  if 18 - 18: O0Oooo0O / I1ii11iIi11i * O0Oooo0O + O0Oooo0O * Ii * oOoO0o00OO0
  if 11 - 11: oOOoOooOo / iii1i1iiiiIi - I11i1ii1 * ii + ii . iii1i1iiiiIi
  if 26 - 26: i1iIi % oOoO0o00OO0
  if 76 - 76: I11i1ii1 * iiiiiiii1
  if 52 - 52: OoOo0o
  if 19 - 19: oOo0O0Ooo
  if 25 - 25: i1iIi / oOOoOooOo
  if 31 - 31: OoOo0o . o0o00Oo0O % oOo0O0Ooo . ooo0O + I11i1ii1
  if 71 - 71: O0Oooo0O . IIiIiII11i
  if 62 - 62: ii . i1IiiiI1iI
  if 61 - 61: iii1i1iiiiIi - OoOo0o - ooOoO0O00
  if 25 - 25: o0o00Oo0O * i1IiiiI1iI + oOoO0o00OO0 . ooo0O . ooo0O
  if 58 - 58: oOo0O0Ooo
  if 53 - 53: ooOoO0O00
  if 59 - 59: ooo0O
  if 81 - 81: iii1i1iiiiIi - iii1i1iiiiIi . iiiiiiii1
  if 73 - 73: i1IiiiI1iI % Ii - oOo0O0Ooo
  if 7 - 7: o0o00Oo0O * Ii * i1iIi + oOOoOooOo % oOo - oOOoOooOo
  if 39 - 39: I1ii11iIi11i * OoOo0o % OoOo0o - ii + ooo0O - i1IiiiI1iI
  if 23 - 23: Ii
  if 30 - 30: ooo0O - ooOoO0O00 % IIiIiII11i + i1IiiiI1iI * iI11I1II1I1I
 iIiIi11 ( 'movies' , 'MAIN' )
def o0ooooO0o0O ( ) :
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  iI1i111I1Ii ( )
 if oo000o0000oO == 1 :
  i11i1ii1I ( )
 if oo000o0000oO == 2 :
  o0OO0o0o00o ( )
 if oo000o0000oO == 3 :
  oOo0 ( )
 if oo000o0000oO == 4 :
  OOOoOO ( )
 if oo000o0000oO == 5 :
  I11IIIi ( )
  if 15 - 15: oOoO0o00OO0 * oOo
  if 16 - 16: iiiiiiii1 + iii1i1iiiiIi
def O00OO ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   I1I1 ( )
  if oo000o0000oO == 1 :
   Oo ( )
  if oo000o0000oO == 2 :
   O0O0o0oOOO ( )
  if oo000o0000oO == 3 :
   OOoOoOo ( o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if oo000o0000oO == 4 :
   o000ooooO0o ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9001 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 10200 , I1IIIii + 'rated.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , I1IIIii + 'Desi.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , I1IIIii + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , I1IIIii + 'ClassicMovies.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
def iI1i11 ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 66 - 66: o0o00Oo0O % oOoO0o00OO0 + Ii . iii1i1iiiiIi / i1iIi + oOoO0o00OO0
 if 86 - 86: ooo0O
 if 5 - 5: I11i1ii1 * iii1i1iiiiIi
 if 5 - 5: O0Oooo0O
 if 90 - 90: O0Oooo0O . oOOoOooOo / i1iIi - i1IiiiI1iI
def ii1 ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , '[COLOR' + iiI1IiI + ']THE SOURCE[/COLOR]' , '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   I1i11 ( )
  if oo000o0000oO == 1 :
   OOo0O0oo0OO0O ( 'http://www.tvmaze.com/shows' )
  if oo000o0000oO == 2 :
   OO0 ( )
  if oo000o0000oO == 3 :
   o0Oooo ( )
  if oo000o0000oO == 4 :
   iiI ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9002 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , 'http://www.tvmaze.com/shows' , 9110001 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , str ( O00OOOoOoo0O ) , 10095 , I1IIIii + 'RD.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( O00OOOoOoo0O ) , 8064 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
def oOIIiIi ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   OOoOooOoOOOoo = '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]'
   if 25 - 25: ii - oOo0O0Ooo . oOo0O0Ooo * OOOo00oo0oO
   if 81 - 81: iiiiiiii1 + I11i1ii1
   if 98 - 98: oOo0O0Ooo
   if 95 - 95: oOOoOooOo / oOOoOooOo
  iiIi11iI1iii = [ OOoOooOoOOOoo , '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , '[COLOR' + iiI1IiI + ']PIRATE MOVIES[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   IIiI1Ii ( )
  if oo000o0000oO == 1 :
   O0O0O0Oo ( )
  if oo000o0000oO == 2 :
   OOOOoO00o0O ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if oo000o0000oO == 3 :
   I1I1I1IIi1III ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , II11IiiIII , o0OOOo )
 else :
  if 11 - 11: iI11I1II1I1I * iI11I1II1I1I * oOo0O0Ooo
  if 46 - 46: iii1i1iiiiIi + oOo
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 70 - 70: iiiiiiii1 / iI11I1II1I1I
  if 85 - 85: ii % ooOoO0O00 * ii / oOoO0o00OO0
  if 96 - 96: ii + OOOo00oo0oO
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , I1IIIii + 'bamftv.png' , Oo00OOOOO , '' )
  if 44 - 44: OOOo00oo0oO
  if 20 - 20: i1IiiiI1iI + i1iIi / o0o00Oo0O % iI11I1II1I1I
  if 88 - 88: iii1i1iiiiIi / IIiIiII11i
  if 87 - 87: oOoO0o00OO0 - oOoO0o00OO0 - iiiiiiii1 + OOOo00oo0oO
  if 82 - 82: OOOo00oo0oO / iI11I1II1I1I . oOo0O0Ooo . OoOo0o / ooo0O
  if 42 - 42: I1ii11iIi11i
  if 19 - 19: OOOo00oo0oO % oOoO0o00OO0 * iI11I1II1I1I + oOo0O0Ooo
 iIiIi11 ( 'movies' , 'MAIN' )
 if 46 - 46: I1ii11iIi11i
def i1II1I1Iii1 ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
def OOOOoO00o0O ( url ) :
 iiI11Iii = i11111IIIII ( url )
 O0o0O0 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( iiI11Iii )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( O0o0O0 ) )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O0o0O0 ) )
 Ii1II1I11i1 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O0o0O0 ) )
 for o0OOOo , oOoooooOoO , url in iI111i :
  if '247ch' in url :
   Ii111 ( o0OOOo , url , 10190 , oOoooooOoO )
  elif '.m3u' in url :
   Ii111 ( o0OOOo , url , 1019 , oOoooooOoO )
  elif '.xml' in url :
   Ii111 ( o0OOOo , url , 1018 , oOoooooOoO )
  else :
   I111i1i1111 ( o0OOOo , url , 222 , oOoooooOoO )
 for o0OOOo , url , oOoooooOoO in IIi11i1i1iI1 :
  if '.xml' in url :
   Ii111 ( o0OOOo , url , 1018 , oOoooooOoO )
  elif '.m3u' in url :
   Ii111 ( o0OOOo , url , 1019 , oOoooooOoO )
  else :
   I111i1i1111 ( o0OOOo , url , 222 , oOoooooOoO )
 for o0OOOo , url , oOoooooOoO in Ii1II1I11i1 :
  I111i1i1111 ( o0OOOo , url , 8043 , oOoooooOoO )
def IIII1 ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 222 , I1IIIii + 'BAMFTV.png' )
def I1IIIiIiIi ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url , oOoooooOoO in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 222 , oOoooooOoO )
  if 27 - 27: oOoO0o00OO0 + iii1i1iiiiIi - OoOo0o + o0o00Oo0O . i1iIi
def O0O0O0Oo ( ) :
 if 46 - 46: I11i1ii1
 ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']All Movies[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']Movies By Genre[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']Movies By A - Z[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 9110015 , I1IIIii + 'Search.png' , Oo00OOOOO , '' , '' )
 if 40 - 40: ooOoO0O00 % OoOo0o
 if 71 - 71: iii1i1iiiiIi
 if 14 - 14: Ii % OoOo0o
 if 82 - 82: iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % I11i1ii1 / i1iIi . i1iIi
def IIi ( ) :
 O0O0ooOOO ( '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 o00oOOooOOo0o ( '[COLORwhite]Source 1 [COLORsteelblue]AutoIptv[COLORorangered]  (By Country)[/COLOR]' , '' , 300000002 , 'http://autoiptv.net/images/TitleWhite.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 o00oOOooOOo0o ( '[COLORwhite]Source 2 [COLORsteelblue]FluxUstv[/COLOR]' , '' , 300000000 , 'https://3.bp.blogspot.com/-IItJ_Ki4rQE/Wszm5CN0suI/AAAAAAAADA0/eGnav96WIjM19v4X82KPEv6T4xlg5JmBACK4BGAYYCw/s1600/FluxusSkinny2.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 o00oOOooOOo0o ( '[COLORwhite]Source 3 [COLORsteelblue]Lodge Tv[/COLOR]' , '' , 300000009 , 'http://4.bp.blogspot.com/-mizXavKU9L8/WrCjl_J67_I/AAAAAAAAC3U/cl5tHXhVfg4Ro84d21ehdiDiKoRQX2TtQCK4BGAYYCw/s1600/LodgeTV_Logo-Header_Long.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 o00oOOooOOo0o ( '[COLORwhite]Source 4 [COLOR' + iiI1IiI + ']International[/COLOR]' , 'https://raw.githubusercontent.com/teamblue65/LISTAS/master/LISTA_SSIPTV' , 300000001 , 'https://icq-chat.com/wp-content/themes/theme49644/images/chatroomimages/international.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']International[/COLOR]' )
 o00oOOooOOo0o ( '[COLORwhite]Source 5 [COLOR' + iiI1IiI + ']Big List[/COLOR]' , 'https://gitlab.com/notisj/m3u-lists/raw/master/all.m3u' , 300000001 , 'http://webiconspng.com/wp-content/uploads/2017/01/List-Amazing-PNG-Icon.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']Big List[/COLOR]' )
def oOoO00oo0O ( ) :
 O0O0ooOOO ( '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 oOOo0 = i11111IIIII ( 'http://lodgetv.blogspot.co.uk/p/remote-playlists.html' )
 IiiiI = re . compile ( '<a href="([^"]*)"><img alt=.+?src="([^"]*)" title="([^"]*)" width="200"' , re . DOTALL ) . findall ( oOOo0 )
 for O00OoOO0oo0 , oOoooooOoO , o0OOOo in IiiiI :
  oOoooooOoO = oOoooooOoO
  o0OOOo = o0OOOo
  oOO = i11111IIIII ( O00OoOO0oo0 )
  O0o0OO0000ooo = re . compile ( '<a href="([^"]*)"><b>' , re . DOTALL ) . findall ( oOO )
  for iIIII1iIIii in O0o0OO0000ooo :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 300000001 , oOoooooOoO , oOoooooOoO , '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' )
def oOOO00o000o ( ) :
 O0O0ooOOO ( '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 oOOo0 = i11111IIIII ( 'https://fluxustv.blogspot.com.by/p/m3u-list.html' )
 IiiiI = re . compile ( 'center;">\n<a href="([^"]*)".+?src="([^"]*)" title="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for iIi11i1 , oOoooooOoO , o0OOOo in IiiiI :
  oOoooooOoO = oOoooooOoO
  o0OOOo = o0OOOo
  oO00oo0o00o0o = i11111IIIII ( iIi11i1 )
  IiIIIIIi = re . compile ( '<a href="([^"]*)"><b>' , re . DOTALL ) . findall ( oO00oo0o00o0o )
  for iIIII1iIIii in IiIIIIIi :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 300000001 , oOoooooOoO , oOoooooOoO , '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' )
def IiIi1iIIi1 ( ) :
 O0O0ooOOO ( '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 oo00O00oO = i11111IIIII ( 'http://autoiptv.net/pages/playlists/' )
 O0OoO0ooOO0o = re . compile ( '<h1>(.+?)</h1>.+?<a class="nostyle" href="([^"]*)"' , re . DOTALL ) . findall ( oo00O00oO )
 for o0OOOo , iIIII1iIIii in O0OoO0ooOO0o :
  if 'Adult' in o0OOOo :
   o00oOOooOOo0o ( '[COLORsteelblue]' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + o0OOOo + '[/COLOR]' )
  elif '24/7' in o0OOOo :
   o00oOOooOOo0o ( '[COLORsteelblue]' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + o0OOOo + '[/COLOR]' )
  elif 'Kodi' in o0OOOo :
   pass
  elif 'XML' in o0OOOo :
   pass
  elif 'Filter' in o0OOOo :
   pass
  else :
   o00oOOooOOo0o ( '[COLORsteelblue]' + o0OOOo + '' + '[COLORorangered] (By Country)[/COLOR]' , iIIII1iIIii , 300000004 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + o0OOOo + '' + '[COLORorangered] (By Country)[/COLOR]' )
def OoOo0oOooOoOO ( ) :
 oo00ooOoO00 = i11111IIIII ( 'http://autoiptv.net/pages/statistics/' )
 o00oOoOo0 = re . compile ( "'title': '(.+?)'" , re . DOTALL ) . findall ( oo00ooOoO00 )
 for o0O0O0ooo0oOO in o00oOoOo0 :
  O0O0ooOOO ( '[COLORsteelblue]' + o0O0O0ooo0oOO + '[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + o0O0O0ooo0oOO + '[/COLOR]' )
def oo000ii ( url ) :
 if url == 'http://' : return False
 try :
  i1i = urllib2 . Request ( url )
  i1i . add_header ( 'User-Agent' , IiII )
  iiI111I1iIiI = urllib2 . urlopen ( i1i )
  iiI111I1iIiI . close ( )
 except Exception , OoO :
  return OoO
 return True
def Iiiiii111i1ii ( name , url ) :
 if 25 - 25: OoOo0o - oOOoOooOo / Ii
 if 41 - 41: ooOoO0O00 % iiiiiiii1 + iI11I1II1I1I
 if 2 - 2: iI11I1II1I1I * I1ii11iIi11i % OOOo00oo0oO - IIiIiII11i - iiiiiiii1
 if 3 - 3: O0Oooo0O
 if 45 - 45: O0Oooo0O
 oOIIi1iiii1iI = name
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 Ii1II1I11i1 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 iIiiii = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 O0000OOO0 = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( oOOo0 )
 ooo0 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for name , oOoooooOoO , oO000oOo00o0o , O00oO0 , url in iI111i :
  if oOIIi1iiii1iI in oO000oOo00o0o :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( name + O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oOoooooOoO , oOoooooOoO , ( '[COLORsteelblue]' + ( name + O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oOoooooOoO , oO000oOo00o0o , O00oO0 , url in IIi11i1i1iI1 :
  if oOIIi1iiii1iI in oO000oOo00o0o :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oOoooooOoO , oOoooooOoO , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO000oOo00o0o , O00oO0 , url in Ii1II1I11i1 :
  if oOIIi1iiii1iI in oO000oOo00o0o :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO000oOo00o0o , oOoooooOoO , O00oO0 , url in iIiiii :
  if oOIIi1iiii1iI in oO000oOo00o0o :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oOoooooOoO , oOoooooOoO , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00oO0 , url in O0000OOO0 :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO000oOo00o0o , O00oO0 , url in ooo0 :
  if oOIIi1iiii1iI in oO000oOo00o0o :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
def O0 ( name , url ) :
 oOOo0 = i11111IIIII ( url )
 Oo00OoOo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for O00oO0 , url in Oo00OoOo :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( ',' , ' ' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 24 - 24: Ii - O0Oooo0O
def i11iiI1111 ( url ) :
 url = url
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + '](_) _No Group[/COLOR]' , '[COLOR' + iiI1IiI + '](UK) United Kingdom[/COLOR]' , '[COLOR' + iiI1IiI + '](US) United States[/COLOR]' , '[COLOR' + iiI1IiI + '](AL) Albania[/COLOR]' , '[COLOR' + iiI1IiI + '](AS) American Samoa[/COLOR]' , '[COLOR' + iiI1IiI + '](AR) Argentina[/COLOR]' , '[COLOR' + iiI1IiI + '](AU) Australia[/COLOR]' , '[COLOR' + iiI1IiI + '](AZ) Azerbaijan[/COLOR]' , '[COLOR' + iiI1IiI + '](BY) Belarus[/COLOR]' , '[COLOR' + iiI1IiI + '](BE) Belgium[/COLOR]' , '[COLOR' + iiI1IiI + '](BO) Bolivia[/COLOR]' , '[COLOR' + iiI1IiI + '](BR) Brazil[/COLOR]' , '[COLOR' + iiI1IiI + '](CM) Cameroon[/COLOR]' , '[COLOR' + iiI1IiI + '](CA) Canada[/COLOR]' , '[COLOR' + iiI1IiI + '](CO) Colombia[/COLOR]' , '[COLOR' + iiI1IiI + '](CZ) Czech Republic[/COLOR]' , '[COLOR' + iiI1IiI + '](DO) Dominican Republic[/COLOR]' , '[COLOR' + iiI1IiI + '](EC) Ecuador[/COLOR]' , '[COLOR' + iiI1IiI + '](FO) Faroe Islands[/COLOR]' , '[COLOR' + iiI1IiI + '](FR) France[/COLOR]' , '[COLOR' + iiI1IiI + '](DE) Germany[/COLOR]' , '[COLOR' + iiI1IiI + '](GR) Greece[/COLOR]' , '[COLOR' + iiI1IiI + '](IS) Iceland[/COLOR]' , '[COLOR' + iiI1IiI + '](IN) India[/COLOR]' , '[COLOR' + iiI1IiI + '](ID) Indonesia[/COLOR]' , '[COLOR' + iiI1IiI + '](IR) Iran[/COLOR]' , '[COLOR' + iiI1IiI + '](IT) Italy[/COLOR]' , '[COLOR' + iiI1IiI + '](LA) Laos[/COLOR]' , '[COLOR' + iiI1IiI + '](MO) Macau[/COLOR]' , '[COLOR' + iiI1IiI + '](MX) Mexico[/COLOR]' , '[COLOR' + iiI1IiI + '](NL) Netherlands[/COLOR]' , '[COLOR' + iiI1IiI + '](NE) Niger[/COLOR]' , '[COLOR' + iiI1IiI + '](PK) Pakistan[/COLOR]' , '[COLOR' + iiI1IiI + '](PA) Panama[/COLOR]' , '[COLOR' + iiI1IiI + '](PE) Peru[/COLOR]' , '[COLOR' + iiI1IiI + '](PL) Poland[/COLOR]' , '[COLOR' + iiI1IiI + '](PT) Portugal[/COLOR]' , '[COLOR' + iiI1IiI + '](RO) Romania[/COLOR]' , '[COLOR' + iiI1IiI + '](RU) Russia[/COLOR]' , '[COLOR' + iiI1IiI + '](SL) Sierra Leone[/COLOR]' , '[COLOR' + iiI1IiI + '](EX-YU) Slovenia[/COLOR]' , '[COLOR' + iiI1IiI + '](SO) Somalia[/COLOR]' , '[COLOR' + iiI1IiI + '](SP) Spain[/COLOR]' , '[COLOR' + iiI1IiI + '](SE) Sweden[/COLOR]' , '[COLOR' + iiI1IiI + '](CH) Switzerland[/COLOR]' , '[COLOR' + iiI1IiI + '](TH) Thailand[/COLOR]' , '[COLOR' + iiI1IiI + '](TR) Turkey[/COLOR]' , '[COLOR' + iiI1IiI + '](UA) Ukraine[/COLOR]' , '[COLOR' + iiI1IiI + '](VE) Venezuela[/COLOR]' , '[COLOR' + iiI1IiI + '](WW) World Wide[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Select Country[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  o0OOOo = '(_)'
 if oo000o0000oO == 1 :
  o0OOOo = '(UK)'
 if oo000o0000oO == 2 :
  o0OOOo = '(US)'
 if oo000o0000oO == 3 :
  o0OOOo = '(AL)'
 if oo000o0000oO == 4 :
  o0OOOo = '(AS)'
 if oo000o0000oO == 5 :
  o0OOOo = '(AR)'
 if oo000o0000oO == 6 :
  o0OOOo = '(AU)'
 if oo000o0000oO == 7 :
  o0OOOo = '(AZ)'
 if oo000o0000oO == 8 :
  o0OOOo = '(BY)'
 if oo000o0000oO == 9 :
  o0OOOo = '(BE)'
 if oo000o0000oO == 10 :
  o0OOOo = '(BO)'
 if oo000o0000oO == 11 :
  o0OOOo = '(BR)'
 if oo000o0000oO == 12 :
  o0OOOo = '(CM)'
 if oo000o0000oO == 13 :
  o0OOOo = '(CA)'
 if oo000o0000oO == 14 :
  o0OOOo = '(CO)'
 if oo000o0000oO == 15 :
  o0OOOo = '(CZ)'
 if oo000o0000oO == 16 :
  o0OOOo = '(DO)'
 if oo000o0000oO == 17 :
  o0OOOo = '(EC)'
 if oo000o0000oO == 18 :
  o0OOOo = '(FO)'
 if oo000o0000oO == 19 :
  o0OOOo = '(FR)'
 if oo000o0000oO == 20 :
  o0OOOo = '(DE)'
 if oo000o0000oO == 21 :
  o0OOOo = '(GR)'
 if oo000o0000oO == 22 :
  o0OOOo = '(IS)'
 if oo000o0000oO == 23 :
  o0OOOo = '(IN)'
 if oo000o0000oO == 24 :
  o0OOOo = '(ID)'
 if oo000o0000oO == 25 :
  o0OOOo = '(IR)'
 if oo000o0000oO == 26 :
  o0OOOo = '(IT)'
 if oo000o0000oO == 27 :
  o0OOOo = '(LA)'
 if oo000o0000oO == 28 :
  o0OOOo = '(MO)'
 if oo000o0000oO == 29 :
  o0OOOo = '(MX)'
 if oo000o0000oO == 30 :
  o0OOOo = '(NL)'
 if oo000o0000oO == 31 :
  o0OOOo = '(NE)'
 if oo000o0000oO == 32 :
  o0OOOo = '(PK)'
 if oo000o0000oO == 33 :
  o0OOOo = '(PA)'
 if oo000o0000oO == 34 :
  o0OOOo = '(PE)'
 if oo000o0000oO == 35 :
  o0OOOo = '(PL)'
 if oo000o0000oO == 36 :
  o0OOOo = '(PT)'
 if oo000o0000oO == 37 :
  o0OOOo = '(RO)'
 if oo000o0000oO == 38 :
  o0OOOo = '(RU)'
 if oo000o0000oO == 39 :
  o0OOOo = '(SL)'
 if oo000o0000oO == 40 :
  o0OOOo = '(EX-YU)'
 if oo000o0000oO == 41 :
  o0OOOo = '(SO)'
 if oo000o0000oO == 42 :
  o0OOOo = '(SP)'
 if oo000o0000oO == 43 :
  o0OOOo = '(SE)'
 if oo000o0000oO == 44 :
  o0OOOo = '(CH)'
 if oo000o0000oO == 45 :
  o0OOOo = '(TH)'
 if oo000o0000oO == 46 :
  o0OOOo = '(TR)'
 if oo000o0000oO == 47 :
  o0OOOo = '(UA)'
 if oo000o0000oO == 48 :
  o0OOOo = '(VE)'
 if oo000o0000oO == 49 :
  o0OOOo = '(WW)'
 Iiiiii111i1ii ( o0OOOo , url )
 if 97 - 97: I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
def I1Ii1111iIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 Ii1II1I11i1 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 iIiiii = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 O0000OOO0 = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( oOOo0 )
 ooo0 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 Oo00OoOo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for o0OOOo , oOoooooOoO , oO000oOo00o0o , O00oO0 , url in iI111i :
  if 'INFO' in oO000oOo00o0o :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( o0OOOo + O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oOoooooOoO , oOoooooOoO , ( '[COLORsteelblue]' + ( o0OOOo + O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oOoooooOoO , oO000oOo00o0o , O00oO0 , url in IIi11i1i1iI1 :
  if 'INFO' in oO000oOo00o0o :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oOoooooOoO , oOoooooOoO , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO000oOo00o0o , O00oO0 , url in Ii1II1I11i1 :
  if 'INFO' in oO000oOo00o0o :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO000oOo00o0o , oOoooooOoO , O00oO0 , url in iIiiii :
  if 'INFO' in oO000oOo00o0o :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oOoooooOoO , oOoooooOoO , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00oO0 , url in O0000OOO0 :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO000oOo00o0o , O00oO0 , url in ooo0 :
  if 'INFO' in oO000oOo00o0o :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00oO0 , url in Oo00OoOo :
  if 'Fluxus' in O00oO0 :
   pass
  elif '.swf' in url :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( ',' , ' ' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( O00oO0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
   if 31 - 31: i1IiiiI1iI . O0Oooo0O * oOOoOooOo + Ii * OOOo00oo0oO
def OO0ooo0o0O0Oooooo ( url ) :
 if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
  i11IIIiI1I ( ( url ) . strip ( ) )
 else :
  try :
   i11IIIiI1I ( ( url ) . strip ( ) )
  except :
   pass
  else :
   i11IIIiI1I ( 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + url )
   if 69 - 69: o0o00Oo0O
   if 85 - 85: oOOoOooOo / o0o00Oo0O
def tools ( ) :
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']Change Log[/COLOR]' , '[COLOR' + iiI1IiI + ']Force Genie Update Kodi[/COLOR]' , '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  Ii1I1i ( )
 if oo000o0000oO == 1 :
  Iii1I1I11iiI1 ( )
 if oo000o0000oO == 2 :
  iI1iIIIi1i ( )
 if oo000o0000oO == 3 :
  ooo ( iIIII1iIIii )
 if oo000o0000oO == 4 :
  iI111I11I1I1 . ok ( oo00 , Oo0oO0ooo )
 if oo000o0000oO == 5 :
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 if oo000o0000oO == 6 :
  OooooO0oOO ( )
  if 30 - 30: ii - ii . o0o00Oo0O / iiiiiiii1
def iIiIi1I ( ) :
 o00oOOooOOo0o ( 'Stories' , 'http://etc.usf.edu/lit2go/books/' , 21999995 , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , '' )
 o00oOOooOOo0o ( 'Virtual FirePlaces' , 'http://www.virtual-fireplace.net/fireplaces.html' , 21999991 , 'http://www.virtual-fireplace.net/files/theme/burning-log.gif' , 'http://www.virtual-fireplace.net/files/theme/burning-log1.gif' , '' )
 o00oOOooOOo0o ( 'Nature Sounds' , 'http://www.virtual-fireplace.net/sounds.html' , 21999993 , 'http://www.virtual-fireplace.net/files/theme/sound.gif' , 'http://www.virtual-fireplace.net/files/theme/sound-bw.gif' , '' )
def iiii11i ( url ) :
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( '<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for url , oOoooooOoO , o0OOOo in IiiiI :
  O0O0ooOOO ( o0OOOo , url , 21999992 , 'http://www.virtual-fireplace.net/' + oOoooooOoO , 'http://www.virtual-fireplace.net/' + oOoooooOoO , o0OOOo )
def III11II1I1Ii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( 'rel="canonical" href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for url in IiiiI :
  url = ( url ) . replace ( '//www.youtube.com/embed/' , '' ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' )
  yt . PlayVideo ( url )
def O00Oo0o000oO ( url ) :
 o00oOOooOOo0o ( 'Rain And Thunder' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Water And Forests' , 'http://www.virtual-fireplace.net/water-and-forest.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Beach And Ocean' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , '' )
def oO0o00oOOooO0 ( url , iconimage ) :
 oOoooooOoO = iconimage
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( '<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url in IiiiI :
  O0O0ooOOO ( o0OOOo , 'http:' + url , 21999992 , oOoooooOoO , oOoooooOoO , '' )
def OOOoO000 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( 'data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , o0OOOo , url , oOOOO in IiiiI :
  o00oOOooOOo0o ( o0OOOo , url , 21999996 , oOoooooOoO , oOoooooOoO , ( oOOOO ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def IiIi1ii111i1 ( url , iconimage ) :
 oOoooooOoO = iconimage
 oOOOO = 'desc'
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( '<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , i1i1i1I in IiiiI :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR] - Audio' , url , 21999997 , oOoooooOoO , oOoooooOoO , ( i1i1i1I ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( i1i1i1I ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR] - Text' , url , 21999998 , oOoooooOoO , oOoooooOoO , ( i1i1i1I ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( i1i1i1I ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def oOoo000 ( url , iconimage ) :
 oOoooooOoO = iconimage
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( '<a href="([^"]*)">Audio</a>' ) . findall ( oOOo0 )
 for url in IiiiI :
  i11IIIiI1I ( url )
def OooOo00o ( name , url , iconimage ) :
 oOoooooOoO = iconimage
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( '</audio>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for i1i1i1I in IiiiI :
  OoOoO ( ( name ) . replace ( ' - Text' , '' ) , ( i1i1i1I ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  if 20 - 20: ooOoO0O00 * O0Oooo0O + IIiIiII11i % ooo0O % OOOo00oo0oO
  if 13 - 13: I1ii11iIi11i
def oOOo000oOoO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , oOoooooOoO , oOOOO , OoOo00o0OO , o0OOOo in IiiiI :
  O0O0ooOOO ( o0OOOo , url , 21009 , oOoooooOoO , OoOo00o0OO , oOOOO )
  if 1 - 1: oOo0O0Ooo % oOOoOooOo
def oOoO00 ( url ) :
 url = url
 iI1IIIii = oOOo0O00o ( )
 if iI1IIIii ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif iI1IIIii ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 7 - 7: I11i1ii1 - i1IiiiI1iI / IIiIiII11i * i1iIi . iiiiiiii1 * iiiiiiii1
  if 61 - 61: i1IiiiI1iI % oOOoOooOo - oOo / I1ii11iIi11i
def Ii1iI111 ( ) :
 iIIII1iIIii = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 I1iii = os . path . join ( O0oooo00o0Oo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( iIIII1iIIii , I1iii , o0oO0 )
 oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0o0O0Ooo0o
 print '======================================='
 extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
 i1Ii11II ( iIIII1iIIii )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IioO0oOOO0Ooo ( )
def i1i1I ( ) :
 IiIIi1 = iII11I1Ii1 ( )
 o0o0 = IiIIi1 . replace ( ooOoOoo0O , "" )
 if os . path . exists ( IiIIi1 ) or not IiIIi1 == False :
  oOo0oO = open ( IiIIi1 , mode = 'r' ) ; IIi1IIIIi = oOo0oO . read ( ) ; oOo0oO . close ( )
  OoOoO ( "%s - %s" % ( oo00 , o0o0 ) , IIi1IIIIi )
 else :
  OOOoO ( 'View Log' , 'No Log File Found!' )
def I1i ( log = None , count = None , all = None ) :
 if log == None :
  iiiI = IiIi1 ( True )
  i111iiI1ii = IiIi1 ( True , True )
  if not i111iiI1ii == False and not iiiI == False :
   IIiii = iI111I11I1I1 . select ( oOo0oooo00o , [ "View %s: %s error(s)" % ( iiiI . replace ( ooOoOoo0O , "" ) , I1i ( iiiI , True , True ) ) , "View %s: %s error(s)" % ( i111iiI1ii . replace ( ooOoOoo0O , "" ) , I1i ( i111iiI1ii , True , True ) ) ] )
   if IIiii == - 1 : OOOoO ( '[COLOR %s]View Log[/COLOR]' % I1i1i , '[COLOR %s]View Log Cancelled![/COLOR]' % OOOOooO0oO00O0o ) ; return
  elif iiiI == False and i111iiI1ii == False :
   OOOoO ( '[COLOR %s]View Log[/COLOR]' % I1i1i , '[COLOR %s]No Log File Found![/COLOR]' % OOOOooO0oO00O0o )
   return
  elif not iiiI == False : IIiii = 0
  elif not i111iiI1ii == False : IIiii = 1
  log = iiiI if IIiii == 0 else i111iiI1ii
 if log == False :
  if count == None :
   OOOoO ( "[COLOR %s]%s[/COLOR]" % ( I1i1i , oOo0oooo00o ) , "[COLOR %s]Log File not Found[/COLOR]" % OOOOooO0oO00O0o )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   oOo0oO = open ( log , mode = 'r' ) ; ooOO00oOOo000 = oOo0oO . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; oOo0oO . close ( )
   iI111i = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( ooOO00oOOo000 )
   if not count == None :
    if all == None :
     IIii11II11II1 = 0
     for II1I in iI111i :
      if o0OOO in II1I : IIii11II11II1 += 1
     return IIii11II11II1
    else : return len ( iI111i )
   if len ( iI111i ) > 0 :
    IIii11II11II1 = 0 ; IIi1IIIIi = ""
    for II1I in iI111i :
     if all == None and not o0OOO in II1I : continue
     else :
      IIii11II11II1 += 1
      IIi1IIIIi += "[COLORorangered]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( IIii11II11II1 , II1I . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( i1111 , '' ) )
    if IIii11II11II1 > 0 :
     OoOoO ( oOo0oooo00o , IIi1IIIIi )
    else : OOOoO ( oOo0oooo00o , "No Errors Found in Log" )
   else : OOOoO ( oOo0oooo00o , "No Errors Found in Log" )
  else : OOOoO ( oOo0oooo00o , "Log File not Found" )
def IiIi1 ( file = False , old = False , wizard = False ) :
 if wizard == True :
  if not os . path . exists ( Oo0o0000o0o0 ) : return False
  else :
   if file == True :
    return Oo0o0000o0o0
   else :
    OoOo000oOo0oo = open ( Oo0o0000o0o0 , 'r' )
    oO0O = OoOo000oOo0oo . read ( )
    OoOo000oOo0oo . close ( )
    return oO0O
 oOOiiiIIiIi = 0
 OooOOO = os . listdir ( ooOoOoo0O )
 Ii1iI11iI1 = [ ]
 if 5 - 5: iI11I1II1I1I
 for II1I in OooOOO :
  if old == True and II1I . endswith ( '.old.log' ) : Ii1iI11iI1 . append ( os . path . join ( ooOoOoo0O , II1I ) )
  elif old == False and II1I . endswith ( '.log' ) and not II1I . endswith ( '.old.log' ) : Ii1iI11iI1 . append ( os . path . join ( ooOoOoo0O , II1I ) )
  if 72 - 72: OOOo00oo0oO . O0Oooo0O / iii1i1iiiiIi + i1IiiiI1iI % iI11I1II1I1I
 if len ( Ii1iI11iI1 ) > 0 :
  Ii1iI11iI1 . sort ( key = lambda oOo0oO : os . path . getmtime ( oOo0oO ) )
  if file == True : return Ii1iI11iI1 [ - 1 ]
  else :
   OoOo000oOo0oo = open ( Ii1iI11iI1 [ - 1 ] , 'r' )
   oO0O = OoOo000oOo0oo . read ( )
   OoOo000oOo0oo . close ( )
   return oO0O
 else :
  return False
  if 42 - 42: oOoO0o00OO0 * iii1i1iiiiIi % oOOoOooOo - iii1i1iiiiIi . Ii - O0Oooo0O
def Ii1iI111 ( ) :
 iIIII1iIIii = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 I1iii = os . path . join ( O0oooo00o0Oo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( iIIII1iIIii , I1iii , o0oO0 )
 oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0o0O0Ooo0o
 print '======================================='
 extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
 i1Ii11II ( iIIII1iIIii )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IioO0oOOO0Ooo ( )
def o0oO0oOO ( ) :
 ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']Todays Games[/COLOR]' , '' , 90030 , I1IIIii + 'tgames.png' , Oo00OOOOO , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport[/COLOR]' , 'http://www.replaymatches.com/' , 90037 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Replays[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , I1IIIii + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 89 - 89: oOOoOooOo + i1iIi * oOOoOooOo / oOOoOooOo
 if 46 - 46: oOo
 if 71 - 71: i1IiiiI1iI / i1IiiiI1iI * OOOo00oo0oO * OOOo00oo0oO / IIiIiII11i
def II1I1iiIII1I1 ( ) :
 o0Ooo0o0ooo0 = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 iiI11Iii = requests . get ( iIIII1iIIii ) . content
 iI111i = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( iiI11Iii )
 O0o0O0 = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( iI111i ) )
 for IIIi1I1IIii1II , o0OOOo in O0o0O0 :
  if not o0OOOo == 'Home' :
   pass
   oo0o0000Oo0 = 'http://www.replaymatches.com/' + IIIi1I1IIii1II
   if o0OOOo in o0Ooo0o0ooo0 :
    o00oOOooOOo0o ( '[COLORred]' + o0OOOo + '[/COLOR]' , oo0o0000Oo0 , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
   else :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , oo0o0000Oo0 , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
    if 80 - 80: O0Oooo0O - I1ii11iIi11i
def OOooO ( url ) :
 if 79 - 79: O0Oooo0O % OOOo00oo0oO % ooo0O % i1iIi - IIiIiII11i * ii
 if 69 - 69: ooo0O / I1ii11iIi11i
 if 43 - 43: oOoO0o00OO0 . oOo0O0Ooo / ii % ii
 if 33 - 33: O0Oooo0O
 if 62 - 62: oOoO0o00OO0 + i1iIi + ooOoO0O00 / ii
 if 7 - 7: ooo0O + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
 if 22 - 22: oOOoOooOo - oOOoOooOo % OoOo0o . O0Oooo0O + OOOo00oo0oO
 if 63 - 63: oOo0O0Ooo % O0Oooo0O * ooo0O + O0Oooo0O / I1ii11iIi11i % iiiiiiii1
 if 45 - 45: I11i1ii1
 if 20 - 20: ii * ooo0O * o0o00Oo0O . OoOo0o
 oOOo0 = i11111IIIII ( url )
 OoO000O = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( oOOo0 )
 OOo = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in OoO000O :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 900302 , oOoooooOoO , I1IIIii + 'tommysreplays.png' , '' )
 for iIIiiIIIi1I in OOo :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , iIIiiIIIi1I , 900301 , I1IIIii + 'NEXT.png' , '' , '' )
def OO0o0o0oo0O ( url ) :
 iiI11Iii = requests . get ( url ) . content
 iI111i = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( iiI11Iii )
 for IIIi1I1IIii1II , oOoooooOoO in iI111i :
  if 'Highlight' in oOoooooOoO :
   o0OOOo = 'HighLights'
  elif '1st' in oOoooooOoO :
   o0OOOo = '1st Half'
  elif '2nd' in oOoooooOoO :
   o0OOOo = '2nd Half'
  else :
   o0OOOo = 'Full Match'
  IIiI1I1 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , IIIi1I1IIii1II , 1001111 , oOoooooOoO , I1IIIii + 'tommysreplays.png' , '' , '' )
def I11I1IIiiII1 ( ) :
 iiI11Iii = requests . get ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 iI111i = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( iiI11Iii )
 for IIIIIii1ii11 , OOOooo0OooOoO in iI111i :
  ii1iIi1iIiI1i ( '[COLORred]' + IIIIIii1ii11 + '[/COLOR]' , '' , '' , I1IIIii + 'tommysreplays.png' , I1IIIii + 'tommysreplays.png' , '' , '' )
  oOoOOOo = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( OOOooo0OooOoO ) )
  for ii1Io0OOoOoO00 , I1iiioOO0OO0O in oOoOOOo :
   ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']' + ii1Io0OOoOoO00 + '[/COLOR]' , '' , '' , I1iiioOO0OO0O , I1IIIii + 'tommysreplays.png' , '' , '' )
   if 78 - 78: i1iIi / IIiIiII11i % iii1i1iiiiIi
def oO00OoOO ( url ) :
 if 18 - 18: oOOoOooOo - iii1i1iiiiIi % ooOoO0O00 + o0o00Oo0O + Ii + ooOoO0O00
 if 91 - 91: iii1i1iiiiIi + oOOoOooOo . oOo0O0Ooo
 if 71 - 71: iiiiiiii1 % ooo0O / OoOo0o / I1ii11iIi11i
 if 66 - 66: I1ii11iIi11i - ooo0O * I11i1ii1 + iii1i1iiiiIi + ooo0O - iI11I1II1I1I
 if 17 - 17: OOOo00oo0oO
 if 22 - 22: i1IiiiI1iI + iI11I1II1I1I
 if 24 - 24: iii1i1iiiiIi % ooOoO0O00 + iiiiiiii1 . Ii . oOoO0o00OO0
 if 17 - 17: oOoO0o00OO0 . IIiIiII11i . oOOoOooOo / oOoO0o00OO0
 if 57 - 57: i1IiiiI1iI
 if 67 - 67: oOo . oOOoOooOo
 if 87 - 87: OOOo00oo0oO % i1iIi
 if 83 - 83: IIiIiII11i - i1IiiiI1iI
 if 35 - 35: ooOoO0O00 - iI11I1II1I1I + ooOoO0O00
 if 86 - 86: iI11I1II1I1I + iii1i1iiiiIi . Ii - i1iIi
 if 51 - 51: iii1i1iiiiIi
 if 14 - 14: I11i1ii1 % OOOo00oo0oO % I1ii11iIi11i - Ii
 if 53 - 53: i1iIi % I1ii11iIi11i
 if 59 - 59: OoOo0o % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * I11i1ii1
 if 41 - 41: i1iIi % oOoO0o00OO0
 if 12 - 12: OoOo0o
 if 69 - 69: ii + OoOo0o
 if 26 - 26: I1ii11iIi11i + OoOo0o / oOo % iii1i1iiiiIi % oOoO0o00OO0 + IIiIiII11i
 if 31 - 31: i1IiiiI1iI % OoOo0o * i1IiiiI1iI
 if 45 - 45: ooOoO0O00 . oOo0O0Ooo + OoOo0o - ii % oOOoOooOo
 if 1 - 1: iI11I1II1I1I
 if 93 - 93: ooOoO0O00 . Ii . I1ii11iIi11i
 if 99 - 99: i1IiiiI1iI - O0Oooo0O - OOOo00oo0oO % oOo
 if 21 - 21: IIiIiII11i % oOoO0o00OO0 . ooOoO0O00 - ii
 if 4 - 4: ii . oOOoOooOo
 if 78 - 78: oOoO0o00OO0 + i1IiiiI1iI - o0o00Oo0O
 if 10 - 10: O0Oooo0O % oOo0O0Ooo
 if 97 - 97: ii - O0Oooo0O
 if 58 - 58: iI11I1II1I1I + o0o00Oo0O
 if 30 - 30: oOOoOooOo % iiiiiiii1 * OoOo0o - oOoO0o00OO0 * i1iIi % oOOoOooOo
 if 46 - 46: Ii - o0o00Oo0O . OOOo00oo0oO
 if 100 - 100: oOo0O0Ooo / ooo0O * iiiiiiii1 . o0o00Oo0O / OoOo0o
 if 83 - 83: O0Oooo0O
 if 48 - 48: IIiIiII11i * OoOo0o * O0Oooo0O
 if 50 - 50: I11i1ii1 % ooOoO0O00
 iii11II1I = liveresolver . resolve ( url )
 II1I = xbmcgui . ListItem ( path = iii11II1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II1I )
def iI111I11i ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 I1 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1 )
def iII11I1Ii1 ( ) :
 II1i11I1 = False
 if os . path . exists ( os . path . join ( ooOoOoo0O , 'xbmc.log' ) ) :
  II1i11I1 = os . path . join ( ooOoOoo0O , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'kodi.log' ) ) :
  II1i11I1 = os . path . join ( ooOoOoo0O , 'kodi.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'spmc.log' ) ) :
  II1i11I1 = os . path . join ( ooOoOoo0O , 'spmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'tvmc.log' ) ) :
  II1i11I1 = os . path . join ( ooOoOoo0O , 'tvmc.log' )
 return II1i11I1
 if 2 - 2: oOo0O0Ooo - OOOo00oo0oO
def IIII ( url ) :
 if url == 'http://' : return False
 try :
  i1i = urllib2 . Request ( url )
  i1i . add_header ( 'User-Agent' , IiII )
  iiI111I1iIiI = urllib2 . urlopen ( i1i )
  iiI111I1iIiI . close ( )
 except Exception , OoO :
  return OoO
 return True
def iI1iiiIiii ( ) :
 if 24 - 24: iI11I1II1I1I + iI11I1II1I1I * iiiiiiii1
 if 18 - 18: iiiiiiii1 * i1IiiiI1iI - i1iIi
 if 31 - 31: I1ii11iIi11i - o0o00Oo0O % iii1i1iiiiIi % OOOo00oo0oO
 if 45 - 45: oOoO0o00OO0 + IIiIiII11i * Ii
 if 13 - 13: ii * OOOo00oo0oO - i1iIi / OoOo0o + i1IiiiI1iI + I11i1ii1
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def iii1III1i ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   iiiIi ( )
  if oo000o0000oO == 1 :
   II1Iii ( )
  if oo000o0000oO == 2 :
   O0oooo0OoO0oo ( IiiiIi1iI1iI )
  if oo000o0000oO == 3 :
   OO00o ( iIIII1iIIii )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 10060 , I1IIIii + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 49 , I1IIIii + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( O00OOOoOoo0O ) , 41 , I1IIIii + 'WipeGenie.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( O00OOOoOoo0O ) , 44 , I1IIIii + 'GenieBuilds.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 60 - 60: oOoO0o00OO0 - OOOo00oo0oO - oOo0O0Ooo / ooo0O
 if 81 - 81: IIiIiII11i + Ii / iiiiiiii1
def oo00OoO ( url ) :
 iiI11Iii = requests . get ( url ) . text
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( iiI11Iii )
 for iI , Ii1IIi , i111i11I1ii , I1iiioOO0OO0O , OOooo , oo0 , OoOo00o0OO in iI111i :
  if OoOo00o0OO == ' ' :
   OoOo00o0OO = Oo00OOOOO
  if I1iiioOO0OO0O == ' ' :
   I1iiioOO0OO0O = O0O
  OOooo = OOooo . replace ( '\\n' , ' ' )
  if Ii1IIi == 'Movie Search' :
   IIiI1I1 ( iI , oo0 , 9110014 , I1iiioOO0OO0O , OoOo00o0OO , OOooo , '' )
  elif Ii1IIi == 'Menu' :
   ii1iIi1iIiI1i ( iI , i111i11I1ii , 9110013 , I1iiioOO0OO0O , OoOo00o0OO , OOooo , '' )
   if 73 - 73: iii1i1iiiiIi . oOo0O0Ooo
def II1i11i1iIi11 ( name , url ) :
 from imports import Scrape_Nan
 name = str ( name )
 oo0 = str ( url )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( name , oo0 , '' )
 if 83 - 83: i1iIi
def I1iI1I1 ( ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search your moive' , type = xbmcgui . INPUT_ALPHANUM )
 o0Ooo0o0ooo0 = [ 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ]
 for iIIII1iIIii in o0Ooo0o0ooo0 :
  iiI11Iii = requests . get ( o0oOoO00o ( iIIII1iIIii ) ) . content
  iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( iiI11Iii )
  for iI , Ii1IIi , i111i11I1ii , I1iiioOO0OO0O , OOooo , oo0 , OoOo00o0OO in iI111i :
   if OoOo00o0OO == ' ' :
    OoOo00o0OO = Oo00OOOOO
   if I1iiioOO0OO0O == ' ' :
    I1iiioOO0OO0O = O0O
   OOooo = OOooo . replace ( '\\n' , ' ' )
   if Ii1IIi == 'Movie Search' :
    if IiIi1oo00ooOoo . lower ( ) in iI . lower ( ) :
     IIiI1I1 ( iI , oo0 , 9110014 , I1iiioOO0OO0O , OoOo00o0OO , OOooo , '' )
def iii1IIIiiiI ( url ) :
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oOOo0 )
 for o0OOOo , url , Ii1IIi , Oo0Oo0O , OoOo00o0OO , oOOOO in iI111i :
  if Oo0Oo0O == '123' :
   Oo0Oo0O = I1IIIii + 'appstreams.png'
  if OoOo00o0OO == '123' :
   OoOo00o0OO = I1IIIii + 'appstreams.png'
  if 'php' in url :
   o00oOOooOOo0o ( o0OOOo , url , 100010 , Oo0Oo0O , OoOo00o0OO , oOOOO )
  elif 'playlist' in url :
   o00oOOooOOo0o ( o0OOOo , url , 100007 , Oo0Oo0O , OoOo00o0OO , oOOOO )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( o0OOOo , url , 100100 , Oo0Oo0O , OoOo00o0OO , oOOOO )
  elif not 'http' in url :
   IIiI1I1 ( o0OOOo , url , 100009 , Oo0Oo0O , OoOo00o0OO , oOOOO , '' )
  else :
   IIiI1I1 ( o0OOOo , url , 100005 , Oo0Oo0O , OoOo00o0OO , oOOOO , '' )
   if 44 - 44: ii % ii
def I11Ii ( url ) :
 oOOo0 = OoO00oo00 ( url )
 IiiiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , oOoooooOoO , oOOOO , OoOo00o0OO , o0OOOo in IiiiI :
  if oOoooooOoO == '123' :
   oOoooooOoO = I1IIIii + 'appstreams.png'
  if OoOo00o0OO == '123' :
   OoOo00o0OO = Oo00OOOOO
  if 'php' in url :
   o00oOOooOOo0o ( o0OOOo , url , 100004 , oOoooooOoO , OoOo00o0OO , oOOOO )
  elif 'playlist' in url :
   o00oOOooOOo0o ( o0OOOo , url , 100007 , oOoooooOoO , OoOo00o0OO , oOOOO )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( o0OOOo , url , 100100 , oOoooooOoO , OoOo00o0OO , oOOOO )
  elif not 'http' in url :
   IIiI1I1 ( o0OOOo , url , 100009 , oOoooooOoO , OoOo00o0OO , oOOOO , '' )
  else :
   IIiI1I1 ( o0OOOo , url , 100005 , oOoooooOoO , OoOo00o0OO , oOOOO , '' )
   if 16 - 16: I1ii11iIi11i / Ii
def oo00IIIIIIIiI ( url ) :
 if 12 - 12: iiiiiiii1 . I11i1ii1 . iii1i1iiiiIi / o0o00Oo0O
 oOOo0 = OoO00oo00 ( url )
 OO0oOOo0o = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oOOo0 )
 for O0o0O0 in OO0oOOo0o :
  Oo0Oo0O = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O0o0O0 ) )
  for Oo0Oo0O in Oo0Oo0O :
   Oo0Oo0O = Oo0Oo0O
  o0OOOo = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O0o0O0 ) )
  for o0OOOo in o0OOOo :
   if 'elete' in o0OOOo :
    pass
   elif 'rivate Vid' in o0OOOo :
    pass
   else :
    o0OOOo = ( o0OOOo ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  I1III11iiii11i1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O0o0O0 ) )
  for I1III11iiii11i1 in I1III11iiii11i1 :
   I1III11iiii11i1 = I1III11iiii11i1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O0o0O0 ) )
  for url in url :
   url = url
  IIiI1I1 ( '[COLORred]' + str ( I1III11iiii11i1 ) + '[/COLOR] : ' + str ( o0OOOo ) , str ( url ) , 100009 , str ( Oo0Oo0O ) , Oo00OOOOO , '' , '' )
  iIiIi11 ( 'movies' , '' )
  if 54 - 54: ooOoO0O00 - OOOo00oo0oO
def IiIIII ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search Dans Scrapes' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'http://www.tvmaze.com/search?q=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oo0oO0 = oOOo . lower ( )
 oOOo0 = i11111IIIII ( oo0oO0 )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  IIi11i1II = 'http://www.tvmaze.com' + iIIII1iIIii . replace ( '"' , '' )
  OO0ooo0o0 = requests . get ( IIi11i1II ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OO0ooo0o0 )
  for oOOOO in iI111i :
   if not '<div>' in oOOOO :
    oO0ooOoO = oOOOO . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   oOoooooOoO = 'http:' + oOoooooOoO
   o0OOOo = o0OOOo . replace ( '&#039;' , '' )
   if o0OOOo == '' :
    ooO0000o00O = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( iIIII1iIIii ) )
    for o0OOOo in ooO0000o00O :
     o0OOOo = o0OOOo . replace ( '-' , ' ' )
  ii1iIi1iIiI1i ( o0OOOo , IIi11i1II , 9110002 , oOoooooOoO , Oo00OOOOO , oO0ooOoO , '' )
  if 91 - 91: i1IiiiI1iI / o0o00Oo0O - i1iIi . oOo0O0Ooo
def OOo0O0oo0OO0O ( url ) :
 Ii111 ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 9110004 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
 iiI11Iii = requests . get ( url ) . content
 iI111i = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( iiI11Iii )
 iIIiiIIIi1I = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( iiI11Iii )
 for url , oOoooooOoO , o0OOOo in iI111i :
  IIi11i1II = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  if 82 - 82: I11i1ii1 * OoOo0o / OOOo00oo0oO
  OO0ooo0o0 = requests . get ( IIi11i1II ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OO0ooo0o0 )
  for oOOOO in iI111i :
   if not '<div>' in oOOOO :
    oO0ooOoO = oOOOO . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   oOoooooOoO = 'http:' + oOoooooOoO
   o0OOOo = o0OOOo . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if o0OOOo == '' :
    ooO0000o00O = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for o0OOOo in ooO0000o00O :
     o0OOOo = o0OOOo . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  ii1iIi1iIiI1i ( o0OOOo , IIi11i1II , 9110002 , oOoooooOoO , Oo00OOOOO , oO0ooOoO , '' )
  if 2 - 2: oOo0O0Ooo + ooo0O . ooo0O . o0o00Oo0O / i1IiiiI1iI
 for OOo in iIIiiIIIi1I :
  url = 'http://www.tvmaze.com' + OOo
  ii1iIi1iIiI1i ( 'NEXT' , url , 9110001 , oOoooooOoO , Oo00OOOOO , '' , '' )
def iIiiIiiIi ( url ) :
 iiI11Iii = requests . get ( url ) . content
 iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiI11Iii )
 for oOOOO in iI111i :
  oO0ooOoO = oOOOO . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
 return oO0ooOoO
def i1iiIIIi ( url , name , iconimage ) :
 iI = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 oOoooooOoO = iconimage
 iiI11Iii = requests . get ( url + '/episodes' ) . content
 OO0ooo0o0 = requests . get ( url ) . content
 O0o0O0 = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( iiI11Iii )
 iI111i = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( OO0ooo0o0 )
 for Oo0o in iI111i :
  Oo0o = Oo0o . replace ( ' ' , '' )
 for oOOoOoo0O0 , OOOooo0OooOoO in O0o0O0 :
  if not 'special' in oOOoOoo0O0 . lower ( ) :
   oOOoOoo0O0 = oOOoOoo0O0 . replace ( 'S' , '' ) . replace ( 's' , '' )
  i1i1ii1111i1i = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( OOOooo0OooOoO ) )
  for iIiI , ii1iIIiii1 , ooOo0O0o0 in i1i1ii1111i1i :
   if not 'special' in iIiI . lower ( ) :
    ii1iIi1iIiI1i ( iI + ' - SEASON -' + oOOoOoo0O0 + '- EPISODE-' + iIiI + '-' + Oo0o , '' , 9110003 , oOoooooOoO , Oo00OOOOO , '' , iI )
    if 65 - 65: oOOoOooOo + o0o00Oo0O
    if 32 - 32: ii - iii1i1iiiiIi - Ii * ooo0O / I1ii11iIi11i + ii
    if 35 - 35: ooOoO0O00 - ooo0O * iiiiiiii1
def O0oOoo0OoO0O ( name , extra ) :
 if 63 - 63: ii / oOOoOooOo
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 from imports import Scrape_Nan
 oooO00o0 = name + '<>'
 o0o00oO0oo000 = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( oooO00o0 ) )
 for iI , oO000o , o0Oo , Oo0o in o0o00oO0oo000 :
  iI = iI
  oO000o = oO000o
  o0Oo = o0Oo
  o0O0 = ''
  Scrape_Nan . scrape_episode ( iI , Oo0o , '' , oO000o , o0Oo , '' )
if 48 - 48: i1IiiiI1iI - I11i1ii1 + iI11I1II1I1I + ii
if 4 - 4: IIiIiII11i . i1IiiiI1iI + i1iIi * O0Oooo0O . oOOoOooOo
if 87 - 87: iii1i1iiiiIi / oOo / Ii
if 74 - 74: OOOo00oo0oO / oOoO0o00OO0 % ooo0O
if 88 - 88: iii1i1iiiiIi - Ii % ooo0O * i1IiiiI1iI + oOoO0o00OO0
if 52 - 52: IIiIiII11i . oOo0O0Ooo + iii1i1iiiiIi % oOo
if 62 - 62: ooo0O
if 15 - 15: i1IiiiI1iI + i1iIi . OoOo0o * oOo . iii1i1iiiiIi
if 18 - 18: ooOoO0O00 % IIiIiII11i + O0Oooo0O % i1iIi
if 72 - 72: iI11I1II1I1I
if 45 - 45: I1ii11iIi11i - ooo0O % O0Oooo0O
def i1IIi1i1Ii1 ( ) :
 ii1iIi1iIiI1i ( 'Featured 24/7' , '' , 9070000 , I1IIIii + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 ii1iIi1iIiI1i ( '24/7 Tv Thows' , '' , 9080000 , I1IIIii + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 ii1iIi1iIiI1i ( '24/7 Movies' , '' , 9090000 , I1IIIii + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 ii1iIi1iIiI1i ( '24/7 Cable' , '' , 9100000 , I1IIIii + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 ii1iIi1iIiI1i ( '24/7 Random Stream' , '' , 9110000 , I1IIIii + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 45 - 45: iI11I1II1I1I . OOOo00oo0oO / iii1i1iiiiIi / I11i1ii1
def ooOOOoOoOOO0 ( ) :
 iIIII1iIIii = 'http://arconaitv.me/'
 ii111i1iI = 'index.php#shows'
 iiI11Iii = BeautifulSoup ( requests . get ( iIIII1iIIii + ii111i1iI ) . content )
 I1I1iII1i = iiI11Iii . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for iiIIii in I1I1iII1i :
  oO0Oo0O0 = iiIIii . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in oO0Oo0O0 :
   I1iIiI1IiIIII = IIIi1I1IIii1II . text
  I1iiIi111I = iiIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in I1iiIi111I :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Iiii1iIii = iIIII1iIIii + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    o0OOOo = IIIi1I1IIii1II [ 'title' ]
   oOoooO000O = { 'User-Agent' : random_agent ( ) }
   III1I11i1iIi = requests . get ( Iiii1iIii , headers = oOoooO000O ) . content
   OO0oo0O0OOO0 = packets ( III1I11i1iIi )
   if 76 - 76: Ii / iii1i1iiiiIi + iii1i1iiiiIi / ooOoO0O00 * oOo0O0Ooo
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OO0oo0O0OOO0 )
   for I1IiIIi11I1 in iI111i :
    I1IiIIi11I1 = I1IiIIi11I1 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    I11i1I1Ii11 = 'https:' + I1IiIIi11I1 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    IIiI1I1 ( o0OOOo , I11i1I1Ii11 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 60 - 60: iii1i1iiiiIi
    if 5 - 5: oOo0O0Ooo - oOo0O0Ooo - oOo0O0Ooo * ii
def iiiiiII ( ) :
 iIIII1iIIii = 'http://arconaitv.me/'
 ii111i1iI = 'index.php#movies'
 iiI11Iii = BeautifulSoup ( requests . get ( iIIII1iIIii + ii111i1iI ) . content )
 I1I1iII1i = iiI11Iii . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for iiIIii in I1I1iII1i :
  oO0Oo0O0 = iiIIii . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in oO0Oo0O0 :
   I1iIiI1IiIIII = IIIi1I1IIii1II . text
  I1iiIi111I = iiIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in I1iiIi111I :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Iiii1iIii = iIIII1iIIii + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    o0OOOo = IIIi1I1IIii1II [ 'title' ]
   oOoooO000O = { 'User-Agent' : random_agent ( ) }
   III1I11i1iIi = requests . get ( Iiii1iIii , headers = oOoooO000O ) . content
   OO0oo0O0OOO0 = packets ( III1I11i1iIi )
   if 21 - 21: iI11I1II1I1I / IIiIiII11i % ooOoO0O00
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OO0oo0O0OOO0 )
   for I1IiIIi11I1 in iI111i :
    I1IiIIi11I1 = I1IiIIi11I1 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    I11i1I1Ii11 = 'https:' + I1IiIIi11I1 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    IIiI1I1 ( o0OOOo , I11i1I1Ii11 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 8 - 8: oOo + iii1i1iiiiIi . iI11I1II1I1I % o0o00Oo0O
    if 43 - 43: oOoO0o00OO0 - iiiiiiii1
def O000O ( ) :
 iIIII1iIIii = 'http://arconaitv.me/'
 ii111i1iI = 'index.php#cable'
 iiI11Iii = BeautifulSoup ( requests . get ( iIIII1iIIii + ii111i1iI ) . content )
 I1I1iII1i = iiI11Iii . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for iiIIii in I1I1iII1i :
  oO0Oo0O0 = iiIIii . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in oO0Oo0O0 :
   I1iIiI1IiIIII = IIIi1I1IIii1II . text
  I1iiIi111I = iiIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in I1iiIi111I :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Iiii1iIii = iIIII1iIIii + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    o0OOOo = IIIi1I1IIii1II [ 'title' ]
   oOoooO000O = { 'User-Agent' : random_agent ( ) }
   III1I11i1iIi = requests . get ( Iiii1iIii , headers = oOoooO000O ) . content
   OO0oo0O0OOO0 = packets ( III1I11i1iIi )
   if 98 - 98: iI11I1II1I1I + O0Oooo0O % iii1i1iiiiIi + i1IiiiI1iI % iii1i1iiiiIi
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OO0oo0O0OOO0 )
   for I1IiIIi11I1 in iI111i :
    I1IiIIi11I1 = I1IiIIi11I1 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    I11i1I1Ii11 = 'https:' + I1IiIIi11I1 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    IIiI1I1 ( o0OOOo , I11i1I1Ii11 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 24 - 24: OOOo00oo0oO * O0Oooo0O
def I11IiIIIi ( ) :
 OO0ooo0o0 = 'http://arconaitv.me/stream.php?id=random'
 oOoooO000O = { 'User-Agent' : random_agent ( ) }
 III1I11i1iIi = requests . get ( OO0ooo0o0 , headers = oOoooO000O ) . content
 OO0oo0O0OOO0 = packets ( III1I11i1iIi )
 if 77 - 77: iI11I1II1I1I . i1iIi % OOOo00oo0oO / i1iIi
 iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OO0oo0O0OOO0 )
 for I1IiIIi11I1 in iI111i :
  I1IiIIi11I1 = I1IiIIi11I1 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  I11i1I1Ii11 = 'https:' + I1IiIIi11I1 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  IIiI1I1 ( 'Random Pick' , I11i1I1Ii11 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 54 - 54: OOOo00oo0oO + oOOoOooOo - I1ii11iIi11i
def I1I1IiIi1 ( ) :
 iIIII1iIIii = 'http://arconaitv.me/'
 ii111i1iI = 'index.php#shows'
 if 58 - 58: iii1i1iiiiIi - iiiiiiii1 - ii
 iiI11Iii = BeautifulSoup ( requests . get ( iIIII1iIIii + ii111i1iI ) . content )
 I1I1iII1i = iiI11Iii . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for iiIIii in I1I1iII1i :
  oO0Oo0O0 = iiIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in oO0Oo0O0 :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Iiii1iIii = iIIII1iIIii + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    o0OOOo = IIIi1I1IIii1II [ 'title' ]
   o00ii111Iiii = IIIi1I1IIii1II . findAll ( 'img' )
   for oo0oO0o0 in o00ii111Iiii :
    oOoooooOoO = iIIII1iIIii + oo0oO0o0 [ 'src' ]
    oOoooO000O = { 'User-Agent' : random_agent ( ) }
    III1I11i1iIi = requests . get ( Iiii1iIii , headers = oOoooO000O ) . content
    OO0oo0O0OOO0 = packets ( III1I11i1iIi )
    if 44 - 44: o0o00Oo0O + oOOoOooOo . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - i1IiiiI1iI
    iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OO0oo0O0OOO0 )
    for I1IiIIi11I1 in iI111i :
     I1IiIIi11I1 = I1IiIIi11I1 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     I11i1I1Ii11 = 'https:' + I1IiIIi11I1 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     IIiI1I1 ( o0OOOo , I11i1I1Ii11 , 9060000 , oOoooooOoO , oOoooooOoO , '' , '' )
     if 83 - 83: I11i1ii1 * i1IiiiI1iI / I1ii11iIi11i
def iIIIiI ( name , url ) :
 import urlresolver
 try :
  O00 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( O00 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 14 - 14: Ii
 if 73 - 73: oOOoOooOo + OOOo00oo0oO . oOo
def IIiIIIIiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 IiiiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , oOoooooOoO , oOOOO , OoOo00o0OO , o0OOOo in IiiiI :
  if '.php' in url :
   o00oOOooOOo0o ( o0OOOo , url , 100210 , oOoooooOoO , OoOo00o0OO , oOOOO )
  else :
   O0O0ooOOO ( o0OOOo , url , 222 , oOoooooOoO , OoOo00o0OO , oOOOO )
   if 58 - 58: ooo0O / ooo0O + oOOoOooOo + i1IiiiI1iI - iii1i1iiiiIi . OoOo0o
   if 15 - 15: oOOoOooOo * iii1i1iiiiIi % I11i1ii1 . iii1i1iiiiIi . i1IiiiI1iI
   if 97 - 97: OOOo00oo0oO
def oOoO0O00oo ( iconimage , url , extra ) :
 Oo0Oo0O = ' '
 OOoOoo00Oo = ' '
 OoOo00o0OO = ' '
 oO000o = ' '
 Iiii1iiiIiI1 = OoO00oo00 ( url )
 Oo0Oo0O = re . compile ( '<img src="(.+?)">' ) . findall ( Iiii1iiiIiI1 )
 for Oo0Oo0O in Oo0Oo0O :
  Oo0Oo0O = Oo0Oo0O
 I11Iii1 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( Iiii1iiiIiI1 )
 for OoOo00o0OO in I11Iii1 :
  OoOo00o0OO = OoOo00o0OO
 iI111i = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( Iiii1iiiIiI1 )
 for url , oO000o in iI111i :
  oO000o = 'S' + ( oO000o ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o00OO00OoO + url
  ii1iIi1iIiI1i ( ( oO000o ) . replace ( '  ' , '' ) , url , 100101 , Oo0Oo0O , OoOo00o0OO , OOoOoo00Oo , '' )
  iIiIi11 ( 'Movies' , 'info' )
  if 16 - 16: i1iIi * oOo / OOOo00oo0oO
def II1iiI ( url , name , fanart , extra , iconimage ) :
 III1Ii1i1I1 = extra
 oO000o = name
 Iiii1iiiIiI1 = OoO00oo00 ( url )
 Oo0Oo0O = iconimage
 iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( Iiii1iiiIiI1 )
 for url , name , O0O00OooO in iI111i :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o00OO00OoO + url
  O0O00OooO = O0O00OooO
  I1IiI1iI11 = name + ' - [COLORred]' + O0O00OooO + '[/COLOR]'
  ii1iIi1iIiI1i ( I1IiI1iI11 , url , 100102 , Oo0Oo0O , fanart , 'Aired : ' + O0O00OooO , I1IiI1iI11 )
  if 2 - 2: iI11I1II1I1I
def iiii1 ( name , URL , iconimage , fanart ) :
 oOOo0 = OoO00oo00 ( URL )
 iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , name in iI111i :
  for II1I in OOOO0OOoO0O0 :
   if II1I in iIIII1iIIii :
    URL = 'http://www.watchseriesgo.to/link/' + iIIII1iIIii
    IIiI1I1 ( name , URL , 100106 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( iI111i ) <= 0 :
  ii1iIi1iIiI1i ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 66 - 66: OOOo00oo0oO * iI11I1II1I1I % iI11I1II1I1I * I11i1ii1 - oOOoOooOo - I11i1ii1
  if 70 - 70: O0Oooo0O + OOOo00oo0oO
def o00ooo0 ( url , name ) :
 i1i1IiIi1 = name
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oOOo0 )
 Ii1II1I11i1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oOOo0 )
 for url in iI111i :
  I1iiIiI1iI1I ( url , i1i1IiIi1 )
 for url in IIi11i1i1iI1 :
  I1iiIiI1iI1I ( url , i1i1IiIi1 )
 for url in Ii1II1I11i1 :
  I1iiIiI1iI1I ( url , i1i1IiIi1 )
  if 27 - 27: oOoO0o00OO0 * O0Oooo0O - oOo + i1iIi * i1iIi
def I1iiIiI1iI1I ( url , season_name ) :
 if 'daclips.in' in url :
  o0OO0O0OO0oO0 ( url , season_name )
 elif 'filehoot.com' in url :
  iIiiIi11IIi ( url , season_name )
 elif 'allmyvideos.net' in url :
  Oo0 ( url , season_name )
 elif 'vidspot.net' in url :
  oOII1ii1ii11I1 ( url , season_name )
 elif 'vodlocker' in url :
  o0ooOO0o ( url , season_name )
 elif 'vidto' in url :
  ooo0i1iI1i1I1 ( url , season_name )
  if 99 - 99: oOOoOooOo / iI11I1II1I1I - i1iIi * oOoO0o00OO0 % oOo0O0Ooo
  if 13 - 13: oOo
def ooo0i1iI1i1I1 ( url , season_name ) :
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for oo0o0000Oo0 , o0OOOo in iI111i :
  O0oo0O0 ( oo0o0000Oo0 , season_name )
  if 2 - 2: ii . OoOo0o . I11i1ii1
  if 42 - 42: OoOo0o % OOOo00oo0oO / oOo - OOOo00oo0oO * Ii
def Oo0 ( url , season_name ) :
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for oo0o0000Oo0 , o0OOOo in iI111i :
  O0oo0O0 ( oo0o0000Oo0 , season_name )
  if 19 - 19: OOOo00oo0oO * oOo0O0Ooo % Ii
def oOII1ii1ii11I1 ( url , season_name ) :
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oOOo0 )
 for oo0o0000Oo0 , o0OOOo in iI111i :
  O0oo0O0 ( oo0o0000Oo0 , season_name )
  if 24 - 24: ooo0O
def o0ooOO0o ( url , season_name ) :
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for oo0o0000Oo0 in iI111i :
  O0oo0O0 ( oo0o0000Oo0 , season_name )
  if 10 - 10: ooo0O % i1iIi / OoOo0o
def o0OO0O0OO0oO0 ( url , season_name ) :
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oOOo0 )
 for oo0o0000Oo0 in iI111i :
  O0oo0O0 ( oo0o0000Oo0 , season_name )
  if 28 - 28: OoOo0o % oOOoOooOo
def iIiiIi11IIi ( url , season_name ) :
 oOOo0 = OoO00oo00 ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for oo0o0000Oo0 in iI111i :
  O0oo0O0 ( oo0o0000Oo0 , season_name )
  if 48 - 48: Ii % OOOo00oo0oO
def O0oo0O0 ( Link , season_name ) :
 if 'http:/' in Link :
  i11i11 ( Link )
  if 18 - 18: iI11I1II1I1I + i1IiiiI1iI * oOo0O0Ooo - OoOo0o / oOo0O0Ooo
  if 78 - 78: i1IiiiI1iI . I11i1ii1
def iI1i1II ( url ) :
 oOOo0 = OPEN_URL_1 ( url )
 I1ii1ii1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOo0 )
 for url in I1ii1ii1I :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 18 - 18: OOOo00oo0oO * OOOo00oo0oO % OOOo00oo0oO
def ii1iIi1iIiI1i ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = True )
 return OoOo0oO0o
 if 10 - 10: i1IiiiI1iI / i1IiiiI1iI * Ii
 if 46 - 46: oOo * I1ii11iIi11i % OOOo00oo0oO + o0o00Oo0O * I11i1ii1
def IIiI1I1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1I11i = [ ]
  ii1I11i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  o0OoOo00ooO . addContextMenuItems ( ii1I11i )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = False )
 return OoOo0oO0o
 if 89 - 89: O0Oooo0O . I11i1ii1 % I1ii11iIi11i . I1ii11iIi11i - ii
def oo0ooO0O0o ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 75 - 75: IIiIiII11i + OoOo0o
def iIIi11 ( url ) :
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : o0000o0Oo . play ( url ) . strip ( )
 except : pass
 if 45 - 45: o0o00Oo0O / ooOoO0O00 * OOOo00oo0oO * oOo
def i11i11 ( url ) :
 o0000o0Oo = xbmc . Player ( )
 import urlresolver
 try : o0000o0Oo . play ( url )
 except : pass
 if 35 - 35: oOoO0o00OO0 / iiiiiiii1 % oOo0O0Ooo + iI11I1II1I1I
def OoO00oo00 ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI111I1iIiI = ''
 IIIi1I1IIii1II = ''
 try :
  iiI111I1iIiI = urllib2 . urlopen ( i1i )
  IIIi1I1IIii1II = iiI111I1iIiI . read ( )
  iiI111I1iIiI . close ( )
 except : pass
 if IIIi1I1IIii1II != '' :
  return IIIi1I1IIii1II
 else :
  IIIi1I1IIii1II = 'Opened'
  return IIIi1I1IIii1II
  if 79 - 79: iii1i1iiiiIi / oOOoOooOo
  if 77 - 77: I1ii11iIi11i
  if 46 - 46: O0Oooo0O
def i11i1ii1I ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' ]
  if 72 - 72: iiiiiiii1 * OoOo0o
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , iiIi11iI1iii )
  if 67 - 67: ooOoO0O00
  if 5 - 5: IIiIiII11i . ii
  if 57 - 57: oOo0O0Ooo
  if 35 - 35: ii - O0Oooo0O / oOo
  if oo000o0000oO == 0 :
   iii11i1 ( )
   if 48 - 48: oOOoOooOo * oOoO0o00OO0
   if 15 - 15: oOo * i1IiiiI1iI % iI11I1II1I1I * oOoO0o00OO0
   if 31 - 31: oOo * o0o00Oo0O . OOOo00oo0oO
   if 59 - 59: IIiIiII11i * Ii
 else :
  if 54 - 54: o0o00Oo0O % ii - oOo0O0Ooo
  if 61 - 61: I1ii11iIi11i * I11i1ii1 . I1ii11iIi11i + I1ii11iIi11i / I11i1ii1 * o0o00Oo0O
  if 73 - 73: iiiiiiii1 * iiiiiiii1 / oOOoOooOo
  if O0oo0OO0 . getSetting ( 'Cartoons' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , I1IIIii + 'Cartoons.png' , Oo00OOOOO , '' )
   if 43 - 43: oOoO0o00OO0 . ooOoO0O00 . I11i1ii1 + o0o00Oo0O * i1iIi * o0o00Oo0O
   if 41 - 41: oOoO0o00OO0 + i1iIi % ii . oOoO0o00OO0 + iiiiiiii1 . iiiiiiii1
   if 31 - 31: Ii + IIiIiII11i . iiiiiiii1 * iii1i1iiiiIi
 iIiIi11 ( 'movies' , 'MAIN' )
def oOo0 ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Football' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , I1IIIii + 'Football.png' , Oo00OOOOO , '' )
 if O0oo0OO0 . getSetting ( 'Fitness' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']FITNESS[/COLOR]' , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , I1IIIii + 'Fitness.png' , Oo00OOOOO , '' )
 if O0oo0OO0 . getSetting ( 'Go Fishing' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Go Fishing[/COLOR]' , str ( O00OOOoOoo0O ) , 8090 , I1IIIii + 'GoFishing.png' , Oo00OOOOO , '' )
 if O0oo0OO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']GenieTv Kitchen[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , I1IIIii + 'GenieTVKitchen.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 66 - 66: iii1i1iiiiIi + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * oOoO0o00OO0 % oOoO0o00OO0
 if 87 - 87: OoOo0o + ooo0O . iiiiiiii1 - ii
 if 6 - 6: iI11I1II1I1I * ii
def I1I1i1I ( ) :
 oOOo0 = i11111IIIII ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 iI111i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oOOo0 )
 for OOooOoooOoOo in iI111i :
  OOooOoooOoOo = ( str ( OOooOoooOoOo ) )
  if os . path . exists ( xbmc . translatePath ( OOooOoooOoOo ) ) :
   iIiI1I1ii1I1 = ( OOooOoooOoOo ) . replace ( 'special://home/addons/' , '' )
   OoOoO ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iIiI1I1ii1I1 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   oo000o0000oO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if oo000o0000oO == 0 :
    O00oOoOOO0ooo ( OOooOoooOoOo )
    IioO0oOOO0Ooo ( )
   elif oo000o0000oO == 1 :
    I1III1iIi ( OOooOoooOoOo )
  else :
   pass
   if 82 - 82: oOo0O0Ooo + iiiiiiii1 + oOoO0o00OO0 * oOo0O0Ooo % Ii % iiiiiiii1
def I1III1iIi ( addon ) :
 iIiI1I1ii1I1 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oO0 . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oO0 . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oO0 . close ( )
 if 23 - 23: ooOoO0O00 . iI11I1II1I1I . OoOo0o . o0o00Oo0O % i1iIi % Ii
def O00oOoOOO0ooo ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 Iiiii111 = os . path . join ( IIIII , 'default.py' )
 ooOo000OoO0o = open ( Iiiii111 , "w+" )
 if 58 - 58: oOoO0o00OO0
 ooOo000OoO0o . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 ooOo000OoO0o . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 ooOo000OoO0o . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 2 - 2: IIiIiII11i / O0Oooo0O
 if 54 - 54: ooOoO0O00 . i1IiiiI1iI - oOoO0o00OO0 + oOOoOooOo + I1ii11iIi11i / I1ii11iIi11i
 if 22 - 22: oOOoOooOo . iI11I1II1I1I
 if 12 - 12: i1iIi
def Ooii1IIi1ii ( url ) :
 oOOo0 = i11111IIIII ( url )
 oo0OoOOooO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 oOoOOOo = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 Ii1II1I11i1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 iIiiii = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 O0000OOO0 = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url , o0o0OO0o00o0O , OoOo00o0OO , oOOOO in oo0OoOOooO :
  if 'php' in url :
   o00oOOooOOo0o ( o0OOOo , url , 90037 , o0o0OO0o00o0O , OoOo00o0OO , oOOOO )
  elif o0OOOo == 'Search' :
   o00oOOooOOo0o ( 'Search' , url , 90038 , o0o0OO0o00o0O , OoOo00o0OO , oOOOO )
  else :
   O0O0ooOOO ( o0OOOo , url , 222 , o0o0OO0o00o0O , OoOo00o0OO , oOOOO )
 for o0OOOo , oOoooooOoO , url , IIIIIIi1i in oOoOOOo :
  o00oOOooOOo0o ( o0OOOo , url , 90037 , oOoooooOoO , IIIIIIi1i , '' )
 for o0OOOo , oOoooooOoO , url , IIIIIIi1i in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 90037 , oOoooooOoO , IIIIIIi1i , '' )
 for o0OOOo , url , oOoooooOoO , IIIIIIi1i in IIi11i1i1iI1 :
  O0O0ooOOO ( o0OOOo , url , 222 , oOoooooOoO , IIIIIIi1i , '' )
 for o0OOOo , url , oOoooooOoO , IIIIIIi1i in Ii1II1I11i1 :
  O0O0ooOOO ( o0OOOo , url , 222 , oOoooooOoO , IIIIIIi1i , '' )
 for o0OOOo , url , oOoooooOoO , IIIIIIi1i in iIiiii :
  O0O0ooOOO ( o0OOOo , url , 222 , oOoooooOoO , IIIIIIi1i , '' )
 for o0OOOo , url , oOoooooOoO in O0000OOO0 :
  O0O0ooOOO ( o0OOOo , url , 222 , oOoooooOoO , '' , '' )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
def iiiii11I1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , oOoooooOoO , url , IIIIIIi1i in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 90037 , oOoooooOoO , IIIIIIi1i , '' )
 for o0OOOo , url , oOoooooOoO , IIIIIIi1i in IIi11i1i1iI1 :
  O0O0ooOOO ( o0OOOo , url , 222 , oOoooooOoO , IIIIIIi1i , '' )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
  if 16 - 16: o0o00Oo0O . i1iIi % ooOoO0O00 % OoOo0o
def i1I1iIoOOoO ( ) :
 oOo0Oo0O0O = [ 'serialsearch' , 'moviesearch' ]
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 if oo0oO0 == '' :
  pass
 else :
  for III1II1i in oOo0Oo0O0O :
   iI1i1IiIIIIi = oOOoo00O0O + III1II1i + '.php'
   Iiii1iiiIiI1 = i11111IIIII ( iI1i1IiIIIIi )
   if Iiii1iiiIiI1 != 'Opened' :
    IiiiI = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( Iiii1iiiIiI1 )
    for o0OOOo , iIIII1iIIii , o0o0OO0o00o0O , OoOo00o0OO , oOOOO in IiiiI :
     if oo0oO0 in o0OOOo . lower ( ) :
      OooOooO0O0o0 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( oO0 ) )
      for II1I in OooOooO0O0o0 :
       if II1I == iIIII1iIIii :
        o0OOOo = '[COLORred]* [/COLOR]' + ( o0OOOo ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        OOO0o0 = open ( O0Oo000ooO00 , "a" )
        OOO0o0 . write ( 'item="' + o0OOOo + '"\n' )
        OOO0o0 . close
      if 'php' in iIIII1iIIii :
       o00oOOooOOo0o ( o0OOOo , iIIII1iIIii , 90037 , o0o0OO0o00o0O , OoOo00o0OO , oOOOO )
      else :
       O0O0ooOOO ( o0OOOo , iIIII1iIIii , 222 , o0o0OO0o00o0O , OoOo00o0OO , oOOOO )
       if 34 - 34: oOo0O0Ooo % I1ii11iIi11i - iii1i1iiiiIi + iiiiiiii1
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
   if 79 - 79: IIiIiII11i - oOOoOooOo . ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * oOo0O0Ooo
def Ii1Ii1I ( ) :
 if 54 - 54: OOOo00oo0oO + iii1i1iiiiIi
 if 77 - 77: i1IiiiI1iI . I11i1ii1
 if 58 - 58: i1IiiiI1iI * iii1i1iiiiIi
 if 94 - 94: i1iIi - oOoO0o00OO0 + ooo0O - I1ii11iIi11i
 if 15 - 15: OoOo0o
 if 31 - 31: iiiiiiii1 / ooOoO0O00 . oOo
 if 83 - 83: OOOo00oo0oO / iI11I1II1I1I + ooOoO0O00 / iiiiiiii1
 if 47 - 47: OOOo00oo0oO + ii . IIiIiII11i . iiiiiiii1
 if 66 - 66: oOOoOooOo * iii1i1iiiiIi
 if 2 - 2: OOOo00oo0oO . O0Oooo0O * I1ii11iIi11i + o0o00Oo0O - i1IiiiI1iI * iI11I1II1I1I
 if 12 - 12: ooo0O * O0Oooo0O % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
 if 81 - 81: I1ii11iIi11i - i1IiiiI1iI
 if 24 - 24: ii . oOo * IIiIiII11i
 if 59 - 59: O0Oooo0O + oOo / OoOo0o
 if 97 - 97: I1ii11iIi11i * iiiiiiii1 % oOOoOooOo . iiiiiiii1 - O0Oooo0O - OoOo0o
 if 79 - 79: oOo0O0Ooo - oOOoOooOo
 if 37 - 37: I11i1ii1 . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
 if 83 - 83: I11i1ii1 / O0Oooo0O
 if 64 - 64: oOo % I11i1ii1 . O0Oooo0O % oOo + i1IiiiI1iI * I11i1ii1
 if 83 - 83: ooo0O % OOOo00oo0oO + i1IiiiI1iI % Ii + o0o00Oo0O
 if 65 - 65: iI11I1II1I1I % OOOo00oo0oO + o0o00Oo0O / ii
 iiI11Iii = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 OO0ooo0o0 = requests . get ( 'http://www.djing.com/' ) . content
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( OO0ooo0o0 )
 I1I1iII1i = iiI11Iii . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for iiIIii in I1I1iII1i :
  oO0Oo0O0 = iiIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in oO0Oo0O0 :
   if IIIi1I1IIii1II . has_attr ( 'href' ) :
    Iiii1iIii = 'https://tvcatchup.com' + IIIi1I1IIii1II [ 'href' ]
   o00ii111Iiii = IIIi1I1IIii1II . findAll ( 'img' )
   for oo0oO0o0 in o00ii111Iiii :
    oOoooooOoO = oo0oO0o0 [ 'src' ]
    O0000oO0o00 = oo0oO0o0 [ 'alt' ]
   iI111i = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( IIIi1I1IIii1II ) )
   for oo000o in iI111i :
    I111i1i1111 ( ( '[COLORgold]' + O0000oO0o00 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + oo000o + '[/COLOR]' ) , Iiii1iIii , 90024 , oOoooooOoO )
    if 95 - 95: OOOo00oo0oO - oOOoOooOo * i1IiiiI1iI / oOo / IIiIiII11i + o0o00Oo0O
 for iIIII1iIIii , oOoooooOoO , o0OOOo in IIi11i1i1iI1 :
  if 'Submit' in o0OOOo :
   pass
  elif '&lt;' in o0OOOo :
   pass
  else :
   O0O0ooOOO ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 90025 , 'http://www.djing.com' + oOoooooOoO , Oo00OOOOO , '' )
   if 37 - 37: i1IiiiI1iI . O0Oooo0O + OoOo0o + i1IiiiI1iI . I11i1ii1 / i1iIi
 iIiIi11 ( 'movies' , 'MAIN' )
def i1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 if 100 - 100: oOo % oOo
 iI111i = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( html )
 for iI1I1 in iI111i :
  if not 'text' in iI1I1 :
   ii1O0ooooo000 = o0oOoO00o ( o0oOoO00o ( iI1I1 ) )
   i11IIIiI1I ( ii1O0ooooo000 )
def OooOoOO0OO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<iframe src='([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  I1iiIiiii1111 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 29 - 29: i1iIi - oOo0O0Ooo / oOo0O0Ooo * i1iIi * I11i1ii1 . OoOo0o
def oooI11iI1I ( ) :
 oOOo0 = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 Iii1iiIi1II1 = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for Oo000o , OO00oo , O0Oo0O0 in Iii1iiIi1II1 :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + Oo000o + OO00oo + O0Oo0O0 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + iIIII1iIIii , 10201 , I1IIIii + 'rated.png' )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'yr' in iIIII1iIIii :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + iIIII1iIIii , 10201 , I1IIIii + 'rated.png' )
   if 33 - 33: oOOoOooOo % ooOoO0O00 - OOOo00oo0oO . o0o00Oo0O / o0o00Oo0O
def Oo ( ) :
 if 96 - 96: ii + I11i1ii1 * o0o00Oo0O
 if 86 - 86: i1iIi
 if 29 - 29: iI11I1II1I1I - oOo + oOo0O0Ooo % iI11I1II1I1I % OoOo0o
 if 84 - 84: I11i1ii1 + oOoO0o00OO0 + i1iIi + iiiiiiii1
 if 62 - 62: Ii + iii1i1iiiiIi + ooOoO0O00
 if 69 - 69: iii1i1iiiiIi
 oOOo0 = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'yr' in iIIII1iIIii :
   ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + iIIII1iIIii , 10201 , I1IIIii + 'rated.png' , '' , o0OOOo , '' )
   if 63 - 63: oOo / iii1i1iiiiIi * iI11I1II1I1I . O0Oooo0O
def Ooooo ( name , url , description ) :
 oO0ooOoO = description
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
 for iIiiiIiIi , url , name in iI111i :
  if 'id' in url :
   i1I1Ii11i = name
   ii1iIi1iIiI1i ( ( '[COLORred]RANK [COLORblue]' + iIiiiIiIi + '[COLORred] - [COLORblue]' + name + '[/COLOR]' ) , name , 9110005 , I1IIIii + 'rated.png' , '' , oO0ooOoO , i1I1Ii11i )
   if 19 - 19: I11i1ii1 - ooo0O . iI11I1II1I1I . iii1i1iiiiIi / OoOo0o
   if 87 - 87: iii1i1iiiiIi - oOOoOooOo - OoOo0o + I1ii11iIi11i % iI11I1II1I1I / Ii
def i1iIIII1iiIIi ( description , url ) :
 if 17 - 17: i1IiiiI1iI
 oo0 = ( str ( description ) )
 iI = ( str ( url ) )
 xbmc . log ( 'title:' + iI + '# year:' + oo0 , xbmc . LOGNOTICE )
 from imports import Scrape_Nan
 Scrape_Nan . scrape_movie ( iI , oo0 , '' )
 if 97 - 97: oOoO0o00OO0 * oOoO0o00OO0 / iiiiiiii1
 if 6 - 6: OOOo00oo0oO
 if 72 - 72: i1IiiiI1iI * oOoO0o00OO0 - iii1i1iiiiIi / oOoO0o00OO0 + OoOo0o - iiiiiiii1
 if 49 - 49: oOo - o0o00Oo0O / oOo * iii1i1iiiiIi + O0Oooo0O
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * OOOo00oo0oO
 if 85 - 85: IIiIiII11i . oOOoOooOo % OoOo0o % i1IiiiI1iI
 if 80 - 80: OOOo00oo0oO * i1IiiiI1iI / iI11I1II1I1I % OOOo00oo0oO / iI11I1II1I1I
def Iiii1 ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 i1iiIIiiiII = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiIi1oo00ooOoo = ( url )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 IIi11i1II = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OO0ooO0 = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OoOooOO0oOOo0O = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1II = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIi1Ii1III = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IiIi1oo00ooOoo
 Oooo00 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iii1II1iI1IIi = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 41 - 41: oOo0O0Ooo - O0Oooo0O % IIiIiII11i . O0Oooo0O - i1IiiiI1iI
 i1I111Ii = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 i11i1i = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 10 - 10: i1iIi - Ii . oOoO0o00OO0 % ooOoO0O00
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oOOo0 = i1Oo00 ( url )
 o0oO0 . update ( 0 , "" , "Checking Source 1/9 Links" )
 oo00O00oO = i1Oo00 ( IIi11i1II )
 o0oO0 . update ( 14 , "" , "Checking Source 2/9 Links" )
 iIiIIIi = i1Oo00 ( Ii1I1 )
 o0oO0 . update ( 28 , "" , "Checking Source 3/9 Links" )
 ooo00OOOooO = i1Oo00 ( OO0ooO0 )
 o0oO0 . update ( 40 , "" , "Checking Source 4/9 Links" )
 OooOOOoOoo0O0 = i1Oo00 ( OoOooOO0oOOo0O )
 o0oO0 . update ( 52 , "" , "Checking Source 5/9 Links" )
 O0OOOOo0 = i1Oo00 ( iIIi1Ii1III )
 o0oO0 . update ( 64 , "" , "Checking Source 6/9 Links" )
 OOooO0Oo00 = i1Oo00 ( Oooo00 )
 o0oO0 . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIIIIIIIiIII = i1Oo00 ( iii1II1iI1IIi )
 o0oO0 . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 94 - 94: iiiiiiii1 * iI11I1II1I1I . i1IiiiI1iI
 if 13 - 13: iI11I1II1I1I * iii1i1iiiiIi / O0Oooo0O % oOOoOooOo + OOOo00oo0oO
 iiiI1iI1 = i1Oo00 ( i1I111Ii )
 o0oO0 . update ( 100 , "" , "Checking Source 9/9 Links" )
 I1oOoO0OOO00O = i1Oo00 ( i11i1i )
 if 73 - 73: ooo0O % oOo + I11i1ii1 + oOo0O0Ooo
 if 80 - 80: ooOoO0O00 + ooo0O + I11i1ii1 * i1IiiiI1iI
 if 65 - 65: oOoO0o00OO0 % i1IiiiI1iI % iI11I1II1I1I - ii - oOoO0o00OO0 - o0o00Oo0O
 if 58 - 58: I11i1ii1 + iI11I1II1I1I
 if 94 - 94: i1iIi . ooOoO0O00
 if 71 - 71: iiiiiiii1 + oOo - I11i1ii1 . oOo . I11i1ii1 + oOo0O0Ooo
 if 26 - 26: o0o00Oo0O
 if 17 - 17: IIiIiII11i
 if 9 - 9: ii + OOOo00oo0oO
 if 33 - 33: o0o00Oo0O
 if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
 if 83 - 83: ooOoO0O00
 if 76 - 76: i1iIi + iI11I1II1I1I + iii1i1iiiiIi . oOo
 if iIIIIIIIiIII != 'Failed' :
  i1i1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIIIIiIII )
  for url , o0OOOo in i1i1 :
   o0oOoOo0 = i1Oo00 ( url )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , O00oO0 in III1IiI1i1i :
    O00oO0 = ( O00oO0 . replace ( '.' , ' ' ) )
    if oo0oO0 in O00oO0 . lower ( ) :
     if '.mkv' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.mp4' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.avi' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.wav' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , url + o0OOOOOo0 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
      if 57 - 57: iI11I1II1I1I + iI11I1II1I1I
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in IIi11i1i1iI1 :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 56 - 56: OOOo00oo0oO + oOOoOooOo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 32 - 32: IIiIiII11i + iii1i1iiiiIi % oOOoOooOo / iii1i1iiiiIi + oOoO0o00OO0
 if iIiIIIi != 'Failed' :
  Ii1II1I11i1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for IiI11I111 , o0OOOo in Ii1II1I11i1 :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1I1 + IiI11I111 ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Source 3 Links" )
 if ooo00OOOooO != 'Failed' :
  iIiiii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in iIiiii :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 54 - 54: o0o00Oo0O - iiiiiiii1 . OoOo0o % iiiiiiii1 + iiiiiiii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if OooOOOoOoo0O0 != 'Failed' :
  i1iI1Iiii1I = [ ]
  O0000OOO0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OooOOOoOoo0O0 )
  for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in O0000OOO0 :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    if o0OOOo in i1iI1Iiii1I :
     pass
    else :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , II11IiiIII , I11Iii1 , oOOOO )
     i1iI1Iiii1I . append ( o0OOOo )
     o0oO0 . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 36 , "" , "Getting Scooby Links" )
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if O0OOOOo0 != 'Failed' :
  Oo00OoOo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( O0OOOOo0 )
  for url , oOoooooOoO , o0OOOo in Oo00OoOo :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , oOoooooOoO )
    o0oO0 . update ( 45 , "" , "Getting Snag Links" )
    if 9 - 9: i1IiiiI1iI / iii1i1iiiiIi / IIiIiII11i + O0Oooo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 71 - 71: iiiiiiii1 / I1ii11iIi11i
    if 87 - 87: oOoO0o00OO0 + oOoO0o00OO0 - oOoO0o00OO0 % o0o00Oo0O
    if 13 - 13: IIiIiII11i
    if 57 - 57: i1iIi - ii
    if 68 - 68: ooo0O % oOoO0o00OO0 / O0Oooo0O + O0Oooo0O - O0Oooo0O . oOo
    if 100 - 100: iii1i1iiiiIi % I1ii11iIi11i
    if 76 - 76: IIiIiII11i / oOo + ii . oOoO0o00OO0 . i1IiiiI1iI . oOOoOooOo
    if 43 - 43: ooOoO0O00
    if 17 - 17: o0o00Oo0O - iii1i1iiiiIi
    if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
    if 34 - 34: i1iIi * i1iIi - oOoO0o00OO0 - o0o00Oo0O . Ii
    if 32 - 32: iI11I1II1I1I . oOo * OOOo00oo0oO / OoOo0o . IIiIiII11i - I1ii11iIi11i
    if 10 - 10: oOoO0o00OO0 / Ii - i1iIi + OOOo00oo0oO * oOo0O0Ooo
    if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % oOoO0o00OO0
    if 64 - 64: i1IiiiI1iI + oOo
    if 25 - 25: oOo0O0Ooo . oOOoOooOo + oOo0O0Ooo % i1iIi * iI11I1II1I1I
    if 31 - 31: Ii + OoOo0o - o0o00Oo0O
    if 51 - 51: oOo * ooOoO0O00 / i1iIi * OoOo0o + oOOoOooOo % oOoO0o00OO0
 if iiiI1iI1 != 'Failed' :
  IIIiI1iiiiiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiI1iI1 )
  for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in IIIiI1iiiiiIi :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Herovision Links" )
    if 74 - 74: i1IiiiI1iI / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: Ii . ii / i1IiiiI1iI * oOoO0o00OO0 + ii
    if 3 - 3: Ii * I1ii11iIi11i % iI11I1II1I1I % oOo0O0Ooo * iiiiiiii1 / OoOo0o
    if 95 - 95: I11i1ii1 * o0o00Oo0O * O0Oooo0O . ii % I1ii11iIi11i + oOoO0o00OO0
    if 98 - 98: OOOo00oo0oO . ii
    if 54 - 54: o0o00Oo0O / I11i1ii1 % oOOoOooOo * ooOoO0O00 * o0o00Oo0O
    if 48 - 48: ooo0O . OOOo00oo0oO % iii1i1iiiiIi - iii1i1iiiiIi
    if 33 - 33: i1IiiiI1iI % IIiIiII11i + oOo
    if 93 - 93: ooOoO0O00 . I11i1ii1 / oOo0O0Ooo + I11i1ii1
    if 58 - 58: oOoO0o00OO0 + o0o00Oo0O . I1ii11iIi11i + iii1i1iiiiIi - oOo - iii1i1iiiiIi
    if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - iiiiiiii1 . ooo0O
 Oooooooo00o00 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 100 - 100: O0Oooo0O % IIiIiII11i . i1iIi % oOo + oOoO0o00OO0
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + III1II1i + OOOO
  iIIIIIIIiIII = i1Oo00 ( iI1i1IiIIIIi )
  if iIIIIIIIiIII != 'Failed' :
   i1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIIIIIiIII )
   for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in i1i1 :
    if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
     O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , II11IiiIII , I11Iii1 , oOOOO )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
     if 66 - 66: i1iIi - I1ii11iIi11i . ooOoO0O00
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
     if 75 - 75: i1iIi - i1IiiiI1iI % iii1i1iiiiIi
 Oooooooo00o00 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 80 - 80: i1iIi / OoOo0o
 if 21 - 21: I1ii11iIi11i - iI11I1II1I1I - O0Oooo0O
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = i1iiIIiiiII + III1II1i
  III1I1Iii11i = i1Oo00 ( iI1i1IiIIIIi )
  if III1I1Iii11i != 'Failed' :
   ooo0 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( III1I1Iii11i )
   for IiI11I111 , o0OOOo in ooo0 :
    if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
     I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1iiIIiiiII + III1II1i + IiI11I111 ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 96 - 96: OOOo00oo0oO - OOOo00oo0oO
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: I1ii11iIi11i / ii - oOoO0o00OO0 . I11i1ii1 + iI11I1II1I1I . oOoO0o00OO0
def o0Oooo ( ) :
 Ii111 ( 'RUNNING' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , I1IIIii + 'running.png' )
 Ii111 ( 'COUNTDOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , I1IIIii + 'countdown.png' )
 Ii111 ( 'UNKNOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , I1IIIii + 'unknown.png' )
 Ii111 ( 'CANCELLED' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , I1IIIii + 'cancelled.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 4 - 4: ii + oOOoOooOo . ooOoO0O00 / o0o00Oo0O - o0o00Oo0O
def oOooOOo00ooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , oO000o , o0OO0oooo , O0O00OooO , I11II1i1 in iI111i :
  Ii111 ( ( '[COLORblue]' + o0OOOo + '[/COLOR] [COLORred]Season[/COLOR]-' + oO000o + ' [COLORred]Returns [/COLOR]- ' + I11II1i1 + ' ' + O0O00OooO ) , o0OOOo , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 46 - 46: IIiIiII11i % iiiiiiii1 - ooOoO0O00 / i1IiiiI1iI * iii1i1iiiiIi
def oO0o0oOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , oO000o , o0OO0oooo in iI111i :
  Ii111 ( ( '[COLORblue]' + o0OOOo + '[/COLOR] [COLORred]Season[/COLOR]-' + oO000o + ' [COLORred] Status Unknown[/COLOR] ' ) , o0OOOo , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 92 - 92: ooOoO0O00 % oOOoOooOo + oOOoOooOo - iI11I1II1I1I . i1iIi
def iIIi1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , oO000o , o0OO0oooo , O0O00OooO in iI111i :
  Ii111 ( ( '[COLORblue]' + o0OOOo + ' [COLORred] Cancelled On[/COLOR] ' + O0O00OooO ) , o0OOOo , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 75 - 75: I11i1ii1 % Ii + iI11I1II1I1I
def oOoOo0o00o ( url ) :
 IiIi1oo00ooOoo = ( url )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 if 2 - 2: IIiIiII11i
 if 54 - 54: i1iIi . ii % I1ii11iIi11i
 o0OOOOOo0 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 IIi11i1II = 'http://onlinemovies.tube/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OO0ooO0 = ( o0oOoO00o ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1II = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 22 - 22: OoOo0o
 Oooo00 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iii1II1iI1IIi = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 I1I11Iiii111 = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 38 - 38: oOo . oOOoOooOo
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 34 - 34: ooOoO0O00 % I11i1ii1
 o0oO0 . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 80 - 80: ii / iI11I1II1I1I + oOoO0o00OO0 / ooOoO0O00 / ooo0O
 if 94 - 94: ooOoO0O00
 iiIIi1 = i1Oo00 ( o0OOOOOo0 )
 o0oO0 . update ( 14 , "" , "Checking Source 3/11 Links" )
 oo00O00oO = i1Oo00 ( IIi11i1II )
 o0oO0 . update ( 28 , "" , "Checking Source 4/11 Links" )
 iIiIIIi = i1Oo00 ( Ii1I1 )
 o0oO0 . update ( 40 , "" , "Checking Source 5/11 Links" )
 ooo00OOOooO = i1Oo00 ( OO0ooO0 )
 o0oO0 . update ( 52 , "" , "Checking Source 6/11 Links" )
 III1I1Iii11i = i1Oo00 ( I1II )
 o0oO0 . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 65 - 65: ooOoO0O00 . oOoO0o00OO0 / oOOoOooOo
 if 11 - 11: I11i1ii1 * oOOoOooOo / oOOoOooOo - OoOo0o
 OOooO0Oo00 = i1Oo00 ( Oooo00 )
 o0oO0 . update ( 95 , "" , "Checking Source 9/11 Links" )
 iIIIIIIIiIII = i1Oo00 ( iii1II1iI1IIi )
 o0oO0 . update ( 97 , "" , "Checking Source 10/11 Links" )
 OoO0o0OOOO = i1Oo00 ( I1I11Iiii111 )
 o0oO0 . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 39 - 39: oOoO0o00OO0 / ooOoO0O00 * I11i1ii1 - oOo0O0Ooo
 if iIIIIIIIiIII != 'Failed' :
  i1i1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIIIIiIII )
  for url , o0OOOo in i1i1 :
   o0oOoOo0 = i1Oo00 ( url )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , O00oO0 in III1IiI1i1i :
    if oo0oO0 in O00oO0 . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , url + o0OOOOOo0 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 74 - 74: o0o00Oo0O - IIiIiII11i + ooOoO0O00 . O0Oooo0O . oOoO0o00OO0
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if OOooO0Oo00 != 'Failed' :
  OoO0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooO0Oo00 )
  for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in OoO0O :
   if oo0oO0 in o0OOOo . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 10 , "" , "Getting Herovision Links" )
    if 98 - 98: Ii / oOo0O0Ooo * ooo0O / O0Oooo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 67 - 67: i1IiiiI1iI % OOOo00oo0oO
    if 39 - 39: Ii + I11i1ii1
    if 7 - 7: iI11I1II1I1I - ooOoO0O00
    if 10 - 10: O0Oooo0O % o0o00Oo0O / oOo0O0Ooo % i1IiiiI1iI
    if 25 - 25: IIiIiII11i / oOo
    if 64 - 64: o0o00Oo0O % oOOoOooOo
    if 40 - 40: ooo0O + i1IiiiI1iI
    if 77 - 77: Ii % I11i1ii1 + O0Oooo0O % ii - i1IiiiI1iI
    if 26 - 26: I1ii11iIi11i + o0o00Oo0O - iI11I1II1I1I
    if 47 - 47: ii
    if 2 - 2: iii1i1iiiiIi % O0Oooo0O * I1ii11iIi11i * iii1i1iiiiIi
 if OoO0o0OOOO != 'Failed' :
  Oo0OOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO0o0OOOO )
  for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in Oo0OOo :
   if oo0oO0 in o0OOOo . lower ( ) :
    Ii111 ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , II11IiiIII )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 30 , "" , "Getting RaizTv Links" )
    if 44 - 44: i1IiiiI1iI * ooo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  II11ii1I11 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for url , oOoooooOoO , o0OOOo , o0oO00o in IIi11i1i1iI1 :
   if oo0oO0 in o0OOOo . lower ( ) :
    if 'season' in o0oO00o :
     Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , oOoooooOoO , oOoooooOoO , '' )
    if 'episodes' in o0oO00o :
     Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , oOoooooOoO , oOoooooOoO , '' )
  for url in II11ii1I11 :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 78 - 78: I1ii11iIi11i * O0Oooo0O - ii - oOo
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iiIIi1 != 'Failed' :
  oOoOOOo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iiIIi1 )
  for url , o0OOOo , oOoooooOoO in oOoOOOo :
   if oo0oO0 in o0OOOo . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( o0OOOo ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , oOoooooOoO , '' , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 45 , "" , "Getting Source iWatch Links" )
    if 83 - 83: oOOoOooOo / OoOo0o
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 39 - 39: I11i1ii1 + i1IiiiI1iI
    if 9 - 9: oOo0O0Ooo % i1IiiiI1iI . I1ii11iIi11i * oOo0O0Ooo
    if 99 - 99: o0o00Oo0O . ooo0O % i1IiiiI1iI - I1ii11iIi11i / i1IiiiI1iI
    if 20 - 20: iii1i1iiiiIi * iiiiiiii1
    if 19 - 19: ii
    if 76 - 76: oOo * OOOo00oo0oO
    if 63 - 63: IIiIiII11i . IIiIiII11i + oOoO0o00OO0 + OoOo0o + o0o00Oo0O . i1iIi
    if 1 - 1: o0o00Oo0O * Ii - oOOoOooOo - i1iIi
    if 94 - 94: oOo + I11i1ii1 + oOOoOooOo
 if iIiIIIi != 'Failed' :
  Ii1II1I11i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for o0OOOo in Ii1II1I11i1 :
   if oo0oO0 in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Ii1I1 + o0OOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 82 - 82: I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / OoOo0o + I11i1ii1 % iI11I1II1I1I
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  iIiiii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for o0OOOo in iIiiii :
   if oo0oO0 in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OO0ooO0 + o0OOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 61 - 61: OoOo0o / I1ii11iIi11i % OoOo0o - oOo + oOOoOooOo / oOOoOooOo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if III1I1Iii11i != 'Failed' :
  ooo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III1I1Iii11i )
  for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in ooo0 :
   if oo0oO0 in o0OOOo . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 90 , "" , "Getting Scooby Links" )
    if 82 - 82: I1ii11iIi11i
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 5 - 5: oOo / oOo - o0o00Oo0O - O0Oooo0O + O0Oooo0O
 O0oooOO0Oo0o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for III1II1i in O0oooOO0Oo0o :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + III1II1i + OOOO
  iiiI1iI1 = i1Oo00 ( iI1i1IiIIIIi )
  if iiiI1iI1 != 'Failed' :
   IIIiI1iiiiiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiiI1iI1 )
   for o0OOOo , oOOOO , url , oOoooooOoO , OoOo00o0OO , Ii1IIi in IIIiI1iiiiiIi :
    if oo0oO0 in o0OOOo . lower ( ) :
     o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgold] - Source Pandoras[/COLOR]' , url , Ii1IIi , oOoooooOoO , OoOo00o0OO , oOOOO )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
     if 68 - 68: ii * iI11I1II1I1I + ooOoO0O00 - ooOoO0O00
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
     if 76 - 76: oOo . ii % O0Oooo0O * i1iIi
     if 23 - 23: I11i1ii1 + iI11I1II1I1I
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: o0o00Oo0O % I11i1ii1 % i1iIi * OOOo00oo0oO
def o0OOO00ooo ( ) :
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']Adult Gallery[/COLOR]' , '[COLOR' + iiI1IiI + ']JizBox[/COLOR]' , '[COLOR' + iiI1IiI + ']Adult Channels[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  I1iI11IiiI11i ( )
 if oo000o0000oO == 1 :
  IIIiIIIi11I ( )
 if oo000o0000oO == 2 :
  II1 ( )
  if 71 - 71: oOOoOooOo / oOOoOooOo . iii1i1iiiiIi % iiiiiiii1
  if 50 - 50: oOOoOooOo + iiiiiiii1 / i1IiiiI1iI / i1IiiiI1iI % o0o00Oo0O
  if 87 - 87: I1ii11iIi11i + oOOoOooOo
def I1iI11IiiI11i ( ) :
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']YOLOselfies[/COLOR]' , '[COLOR' + iiI1IiI + ']HotNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']MyNudeBabes[/COLOR]' , '[COLOR' + iiI1IiI + ']TeenNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']ADULTmeme[/COLOR]' , '[COLOR' + iiI1IiI + ']GIRLSmeme[/COLOR]' , ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  OOO000OOo0o0O ( 'http://www.yoloselfie.com/' )
 if oo000o0000oO == 1 :
  I111Iii1 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if oo000o0000oO == 2 :
  i11i ( 'http://www.teennudegirls.com/' )
 if oo000o0000oO == 3 :
  i11i ( 'http://www.teennudegirls.com/' )
 if oo000o0000oO == 4 :
  O0o0O00o0o ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if oo000o0000oO == 5 :
  O0o0O00o0o ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 6 - 6: oOoO0o00OO0 - OOOo00oo0oO * Ii + iii1i1iiiiIi / oOOoOooOo % OoOo0o
def OOO000OOo0o0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 100111 , oOoooooOoO )
 for url in IIi11i1i1iI1 :
  Ii111 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 100110 , oOoooooOoO )
def II11IiIIiiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( oOOo0 )
 for url in iI111i :
  OOo0oOOOOoo0 = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( OOo0oOOOOoo0 )
  sys . exit ( 1 )
def O0o0O00o0o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , oOoooooOoO in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + oOoooooOoO , 100113 , 'http:' + oOoooooOoO )
 for url in IIi11i1i1iI1 :
  Ii111 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http:' + url , 100112 , oOoooooOoO )
def I111Iii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , oOoooooOoO )
def ooOO0OOO00o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , oOoooooOoO in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , oOoooooOoO , 100113 , oOoooooOoO )
def OoOoO0ooooO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , oOoooooOoO )
def IIII1ii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , oOoooooOoO in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , oOoooooOoO , 100113 , oOoooooOoO )
def i11i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , oOoooooOoO )
def OOO0O0OOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , oOoooooOoO in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , oOoooooOoO , 100113 , oOoooooOoO )
def Iii1 ( url ) :
 OOo0oOOOOoo0 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( OOo0oOOOOoo0 )
 sys . exit ( 1 )
 if 96 - 96: I1ii11iIi11i / OOOo00oo0oO . IIiIiII11i . I1ii11iIi11i
def ooIi111iII ( ) :
 if 83 - 83: ii + oOo * OOOo00oo0oO . o0o00Oo0O
 if 13 - 13: ooo0O
 if 7 - 7: oOo0O0Ooo + I11i1ii1 / Ii / I1ii11iIi11i
 if 97 - 97: O0Oooo0O . i1IiiiI1iI / oOo0O0Ooo
 if 83 - 83: i1IiiiI1iI - oOoO0o00OO0 * OOOo00oo0oO
 if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
 if 75 - 75: oOoO0o00OO0 - iii1i1iiiiIi * Ii . ii - I1ii11iIi11i . i1IiiiI1iI
 if 6 - 6: i1IiiiI1iI * OOOo00oo0oO / ii % i1iIi * ooo0O
 if 28 - 28: I11i1ii1 * oOo0O0Ooo % I11i1ii1
 if 95 - 95: o0o00Oo0O / i1IiiiI1iI . O0Oooo0O
 if 17 - 17: i1IiiiI1iI
 Ii111 ( 'SEASONS' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , I1IIIii + 'seasons.png' )
 Ii111 ( 'EPISODES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , I1IIIii + 'episodes.png' )
 Ii111 ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , I1IIIii + 'Search.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 56 - 56: oOOoOooOo * ooo0O + i1IiiiI1iI
def I11II11111i11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , o0OOOo , OOO000Oo in iI111i :
  Ii111 ( ( o0OOOo + ' - ' + OOO000Oo ) . replace ( '&amp;' , '&' ) , url , 90053 , I1IIIii + 'seasons.png' )
  if 8 - 8: oOOoOooOo - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * i1iIi - iI11I1II1I1I
def i1Ii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  Ii111 ( o0OOOo , url , 90054 , I1IIIii + 'episodes.png' )
  if 31 - 31: iiiiiiii1 - iii1i1iiiiIi . iii1i1iiiiIi - OOOo00oo0oO + I1ii11iIi11i / Ii
def ooOoOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for oOoooooOoO , o0OOOo , url in iI111i :
  Ii111 ( o0OOOo , url , 90054 , oOoooooOoO )
 for url in next :
  Ii111 ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 13 - 13: OoOo0o . I1ii11iIi11i / IIiIiII11i
def iiI1iIII1ii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for oOoooooOoO , OOO000Oo , url , o0OOOo , i1iiIIiII1 in iI111i :
  o00oOOooOOo0o ( OOO000Oo + ' - ' + o0OOOo + ' - ' + i1iiIIiII1 , url , 90044 , oOoooooOoO , oOoooooOoO , '' )
 for oOoooooOoO , o0OOOo , url in IIi11i1i1iI1 :
  Ii111 ( o0OOOo , url , 90044 , oOoooooOoO , oOoooooOoO , '' )
 for url in next :
  Ii111 ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 72 - 72: I11i1ii1 % ooo0O
def OooooO ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'http://onlinemovies.tube/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oo0oO0 = oOOo . lower ( )
 oOOo0 = i11111IIIII ( oo0oO0 )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo , o0oO00o in iI111i :
  if 'season' in o0oO00o :
   Ii111 ( o0OOOo , iIIII1iIIii , 90054 , oOoooooOoO , oOoooooOoO , '' )
  if 'episodes' in o0oO00o :
   Ii111 ( o0OOOo , iIIII1iIIii , 90044 , oOoooooOoO , oOoooooOoO , '' )
 for iIIII1iIIii in next :
  Ii111 ( 'NEXT' , iIIII1iIIii , 90053 , I1IIIii + 'Next.png' )
  if 77 - 77: oOo0O0Ooo % oOOoOooOo
def oO0oo ( ) :
 if 52 - 52: I11i1ii1 % oOOoOooOo
 if 25 - 25: i1IiiiI1iI / i1IiiiI1iI % ii - oOoO0o00OO0 * OOOo00oo0oO
 if 23 - 23: Ii
 if 100 - 100: OOOo00oo0oO + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - iii1i1iiiiIi + ooo0O
 if 65 - 65: IIiIiII11i / I1ii11iIi11i
 if 42 - 42: Ii . o0o00Oo0O
 if 75 - 75: O0Oooo0O + iI11I1II1I1I
 if 19 - 19: oOo0O0Ooo + Ii . I11i1ii1 - i1IiiiI1iI / i1iIi + ooo0O
 if 38 - 38: I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I % oOoO0o00OO0
 if 92 - 92: i1IiiiI1iI / o0o00Oo0O * oOo0O0Ooo - i1IiiiI1iI
 Ii111 ( 'ALL MOVIES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , I1IIIii + 'allmov.png' )
 Ii111 ( 'GENRE' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , I1IIIii + 'Genre.png' )
 Ii111 ( 'BY YEAR' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , I1IIIii + 'Years.png' )
 Ii111 ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , I1IIIii + 'Search.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 99 - 99: Ii % ii
def o0000O00oO0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , o0OOOo , OOO000Oo in iI111i :
  if 'genre' in url :
   Ii111 ( ( o0OOOo + ' - ' + OOO000Oo ) . replace ( '&amp;' , '&' ) , url , 90043 , I1IIIii + 'Genre.png' )
   if 3 - 3: iI11I1II1I1I % oOoO0o00OO0 . OoOo0o % i1IiiiI1iI
def I1i1I1Iiiii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  if 'release' in url :
   Ii111 ( o0OOOo , url , 90043 , I1IIIii + 'Years.png' )
   if 88 - 88: i1IiiiI1iI + oOo0O0Ooo - i1IiiiI1iI / ii - Ii
def i11Ii1IiIIIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for oOoooooOoO , o0OOOo , OOOoo00o0o , url , oOOOO in iI111i :
  o00oOOooOOo0o ( o0OOOo + ' ' + OOOoo00o0o , url , 90044 , oOoooooOoO , oOoooooOoO , oOOOO )
 for oOoooooOoO , o0OOOo , o0oO00o , url , O00o0OO0OO0oo , oOOOO in IIi11i1i1iI1 :
  if 'movies' in o0oO00o :
   o00oOOooOOo0o ( o0OOOo + ' - ' + O00o0OO0OO0oo , url , 90044 , oOoooooOoO , oOoooooOoO , oOOOO )
 for url in next :
  Ii111 ( 'NEXT' , url , 90043 , I1IIIii + 'Next.png' )
  if 59 - 59: ii % i1IiiiI1iI / O0Oooo0O + ii . ii
def o0OoooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  ooOO0 ( 'http:' + url )
  if 81 - 81: Ii + i1iIi % Ii - ooOoO0O00
def ooOO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( ( o0OOOo ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , I1IIIii + 'movhub.png' )
def ii11i1I1i ( ) :
 if 49 - 49: ii + ii / OoOo0o . OOOo00oo0oO
 if 13 - 13: IIiIiII11i . iiiiiiii1 - O0Oooo0O . oOo . iI11I1II1I1I
 if 66 - 66: I1ii11iIi11i * I11i1ii1
 if 83 - 83: ii
 if 12 - 12: oOOoOooOo
 if 36 - 36: O0Oooo0O . I11i1ii1 * ii - ooo0O
 if 60 - 60: OoOo0o . iiiiiiii1 / iI11I1II1I1I + OoOo0o * O0Oooo0O
 if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - i1IiiiI1iI + i1iIi
 if 48 - 48: oOoO0o00OO0
 if 96 - 96: oOOoOooOo . ii
 if 39 - 39: OoOo0o + oOo
 if 80 - 80: OoOo0o % oOo / iii1i1iiiiIi
 if 54 - 54: I1ii11iIi11i % oOo - OoOo0o - i1IiiiI1iI
 if 71 - 71: oOOoOooOo . Ii
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'http://onlinemovies.tube/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oo0oO0 = oOOo . lower ( )
 oOOo0 = i11111IIIII ( oo0oO0 )
 iI111i = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo , OoO000oo000o0 in iI111i :
  if 'movies' in OoO000oo000o0 :
   Ii111 ( OoO000oo000o0 + '-' + o0OOOo , iIIII1iIIii , 90044 , oOoooooOoO )
 for iIIII1iIIii in next :
  i11Ii1IiIIIi ( iIIII1iIIii )
  if 6 - 6: oOOoOooOo
def O0O0o0oOOO ( ) :
 Ii111 ( 'Search' , '' , 80008 , I1IIIii + 'Search.png' )
 oOOo0 = i11111IIIII ( 'http://www.join4films.com/' )
 iI111i = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( o0OOOo , iIIII1iIIii , 80006 , I1IIIii + 'Desi.png' )
def o0Ii11iIiiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oOOo0 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , oOoooooOoO , o0OOOo in iI111i :
  I111i1i1111 ( o0OOOo , url , 80007 , oOoooooOoO )
 for url , oOoooooOoO , o0OOOo in iI111i :
  Ii111 ( 'Next' , url , 80006 , I1IIIii + 'Next.png' )
def o000 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  url = ( url ) . replace ( ' ' , '%20' )
  i11IIIiI1I ( url )
def i11ii1 ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'http://www.join4films.com/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' ) + '&search_type=1'
 oo0oO0 = oOOo . lower ( )
 o0Ii11iIiiI ( oo0oO0 )
 if 4 - 4: Ii - OoOo0o % oOoO0o00OO0 * O0Oooo0O % ooo0O
 if 71 - 71: oOOoOooOo . oOOoOooOo - iI11I1II1I1I
 if 22 - 22: ii / oOoO0o00OO0 % iiiiiiii1 * iii1i1iiiiIi
 if 32 - 32: ii % OOOo00oo0oO % iI11I1II1I1I / o0o00Oo0O
 if 61 - 61: IIiIiII11i . o0o00Oo0O - i1iIi - oOoO0o00OO0 / Ii - IIiIiII11i
 if 98 - 98: i1iIi - oOo0O0Ooo . Ii * I1ii11iIi11i
 if 29 - 29: i1iIi / oOOoOooOo % i1IiiiI1iI
 if 10 - 10: iI11I1II1I1I % ii % oOoO0o00OO0
 if 39 - 39: IIiIiII11i * iii1i1iiiiIi . o0o00Oo0O * i1IiiiI1iI
 if 89 - 89: i1iIi - oOOoOooOo . i1IiiiI1iI - O0Oooo0O - oOo0O0Ooo
 if 79 - 79: I11i1ii1 + I11i1ii1 + i1iIi
 if 39 - 39: o0o00Oo0O - ii
 if 63 - 63: iI11I1II1I1I % ooo0O * oOOoOooOo
 if 79 - 79: o0o00Oo0O
 if 32 - 32: IIiIiII11i . o0o00Oo0O + i1iIi / iii1i1iiiiIi / I11i1ii1 / OoOo0o
 if 15 - 15: oOoO0o00OO0
 if 4 - 4: I11i1ii1 + iI11I1II1I1I * iiiiiiii1 + I1ii11iIi11i * ooo0O % IIiIiII11i
def OO0o0o0oo ( ) :
 o00oOOooOOo0o ( 'Genre' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Most Viewed' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Box Office' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Search' , '' , 10078 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 if 40 - 40: I1ii11iIi11i
def iI1Ii11 ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'http://imoviemax.se/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oo0oO0 = oOOo . lower ( )
 Ooo0 ( oo0oO0 )
def IiiiIIi ( url ) :
 I1IIIi = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oOOo0 )
 for url , o0OOOo , OoOooOo00O in iI111i :
  if o0OOOo in I1IIIi :
   pass
  else :
   o00oOOooOOo0o ( o0OOOo + ' - ' + OoOooOo00O + ' Films' , url , 10074 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
   I1IIIi . append ( o0OOOo )
   if 67 - 67: o0o00Oo0O % O0Oooo0O
def III ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , I1I in iI111i :
  o00oOOooOOo0o ( o0OOOo + ' - Views:' + I1I , url , 10075 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
  if 70 - 70: i1iIi . o0o00Oo0O - OoOo0o
  if 62 - 62: O0Oooo0O * i1IiiiI1iI
def Ooo0 ( url ) :
 oOooOOoO0oO0oo0O = [ ]
 oOOo0 = i11111IIIII ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oOOo0 )
 for next in next :
  o00oOOooOOo0o ( 'NEXT PAGE' , next , 10074 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , o0OOOo , url in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 10075 , oOoooooOoO , oOoooooOoO , '' )
  oOooOOoO0oO0oo0O . append ( o0OOOo )
  if 55 - 55: I1ii11iIi11i
def IIi1i1I11IIII ( img , name , url ) :
 img = img
 name = name
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oOOo0 )
 for OooOoOOO00O , url in iI111i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I111iIIII11iI = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I111iIIII11iI
  oOoOO = ( OooOoOOO00O ) . replace ( 'play-' , 'Server ' )
  O0O0ooOOO ( oOoOO , I111iIIII11iI , 10076 , img , img , '' )
  if 20 - 20: oOOoOooOo . oOo * iiiiiiii1
def OOii11Ii1IiiI1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oOOo0 )
 for IIi11i1II in iI111i :
  if '=m' in IIi11i1II :
   O00o0o ( IIi11i1II )
  elif 'php' in IIi11i1II :
   OOii11Ii1IiiI1 ( url )
  else :
   oOOo0 = i11111IIIII ( IIi11i1II )
   iI111i = re . compile ( 'content="([^"]*)">' ) . findall ( oOOo0 )
   for Ii1I1 in iI111i :
    O00o0o ( IIi11i1II )
    if 65 - 65: oOoO0o00OO0 % OOOo00oo0oO . ii * ooo0O * oOo
    if 10 - 10: OOOo00oo0oO - iiiiiiii1 % IIiIiII11i - O0Oooo0O - ooOoO0O00
    if 10 - 10: oOoO0o00OO0 - i1IiiiI1iI . O0Oooo0O
def iiIIIi1iIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 OOo0OOOoOOo = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for O0O00OooO , IIIooo0o0O in OOo0OOOoOOo :
  print 'there ><><><><><><><><><><><><'
  O0O00OooO = O0O00OooO
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIIooo0o0O ) )
  for o0OOOo , o0Oo in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + O0O00OooO + '[/COLOR] - ' + o0OOOo + ' - [COLOR' + iiI1IiI + ']' + o0Oo + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
 O0o0O0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for O0O00OooO , IiiiIIi11II in O0o0O0 :
  print 'there ><><><><><><><><><><><><'
  O0O00OooO = O0O00OooO
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiiiIIi11II ) )
  for o0OOOo , o0Oo in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + O0O00OooO + '[/COLOR] - ' + o0OOOo + ' - [COLOR' + iiI1IiI + ']' + o0Oo + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
   if 55 - 55: i1IiiiI1iI
   if 93 - 93: Ii . ooo0O
   if 16 - 16: ooOoO0O00 . ooOoO0O00 / O0Oooo0O % iii1i1iiiiIi / oOo0O0Ooo * oOoO0o00OO0
def IIIii11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0o0O0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
 for O0o0O0 in O0o0O0 :
  o0OOOo = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0o0O0 ) )
  for o0OOOo in o0OOOo :
   o0OOOo = ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0o0O0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  Oo0Oo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0o0O0 ) )
  for Oo0Oo0O in Oo0Oo0O :
   Oo0Oo0O = 'http:' + Oo0Oo0O
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O , '' , '' )
  if 29 - 29: i1iIi - i1iIi / oOOoOooOo
  if 49 - 49: i1IiiiI1iI + OOOo00oo0oO % oOo - I1ii11iIi11i - o0o00Oo0O - ii
  if 4 - 4: IIiIiII11i - OOOo00oo0oO % I1ii11iIi11i * Ii
  if 18 - 18: I1ii11iIi11i % o0o00Oo0O
def OOoOoOo ( url ) :
 if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
 IIIIIiiI11i1 = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oOOo0 )
 for IIi11i1II , oOoooooOoO , o0OOOo , Iii1I in iI111i :
  o0OOOo = ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  oo00O00oO = i11111IIIII ( IIi11i1II )
  IIi11i1i1iI1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( oo00O00oO )
  for I1ii1ii1I , OOoOoo00Oo in IIi11i1i1iI1 :
   oooII111 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OOoOoo00Oo ) )
   for oOOOO in oooII111 :
    if o0OOOo in IIIIIiiI11i1 :
     pass
    else :
     O0O0ooOOO ( o0OOOo , I1ii1ii1I , 8043 , oOoooooOoO , oOoooooOoO , oOOOO )
     iIiIi11 ( 'movies' , 'INFO' )
     IIIIIiiI11i1 . append ( o0OOOo )
     if 29 - 29: I11i1ii1 + Ii * o0o00Oo0O - iiiiiiii1 . IIiIiII11i % i1iIi
     if 41 - 41: OOOo00oo0oO / OoOo0o + iiiiiiii1 + oOOoOooOo
def iiiiii1Ii ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
 for url , II11IiiIII , oOOOO , OoOo00o0OO , o0OOOo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 10065 , II11IiiIII , OoOo00o0OO , oOOOO )
 iIiIi11 ( 'movies' , 'INFO' )
 if 20 - 20: O0Oooo0O + O0Oooo0O * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
def OooOo ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'https://www.youtube.com/results?search_query=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oo0oO0 = oOOo . lower ( )
 oOOo0 = i11111IIIII ( oo0oO0 )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for iIIII1iIIii in next :
  iIIII1iIIii = 'https://www.youtube.com' + iIIII1iIIii
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , iIIII1iIIii , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for oOoooooOoO , iIIII1iIIii , o0OOOo , O0OOoOOO0o0o , OOoOoo00Oo in iI111i :
  iiiiiIIii . append ( o0OOOo )
  iIiIi11 ( 'tvshows' , 'INFO' )
  Oo0Oo0O = 'http:' + ( oOoooooOoO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + Oo0Oo0O
  iIIII1iIIii = 'http://www.youtube.com' + iIIII1iIIii
  O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( iIIII1iIIii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O , Oo0Oo0O , OOoOoo00Oo )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for oOoooooOoO , iIIII1iIIii , o0OOOo , O0OOoOOO0o0o in iI111i :
   print 'im doing it'
   iIiIi11 ( 'tvshows' , 'INFO' )
   Oo0Oo0O = 'http:' + ( oOoooooOoO ) . replace ( 'https:' , '' )
   iIIII1iIIii = 'http://www.youtube.com' + iIIII1iIIii
   if '&' in iIIII1iIIii :
    print ' i got here'
    oOOo0 = i11111IIIII ( iIIII1iIIii )
    O0o0O0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for O0o0O0 in O0o0O0 :
     o0OOOo = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0o0O0 ) )
     for o0OOOo in o0OOOo :
      o0OOOo = ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iIIII1iIIii = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0o0O0 ) )
     for iIIII1iIIii in iIIII1iIIii :
      iIIII1iIIii = 'https://www.youtube.com/w' + iIIII1iIIii
     Oo0Oo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0o0O0 ) )
     for Oo0Oo0O in Oo0Oo0O :
      Oo0Oo0O = 'http:' + Oo0Oo0O
     O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( iIIII1iIIii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O , Oo00OOOOO , '' )
   elif o0OOOo in iiiiiIIii :
    pass
   elif 'user' in iIIII1iIIii or 'elete' in o0OOOo :
    pass
   elif 'hannel' in iIIII1iIIii :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iIIII1iIIii
    oOOo0 = i11111IIIII ( iIIII1iIIii )
    iIOoo0ooo0oo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for oOoooooOoO , iIIII1iIIii , o0OOOo in iIOoo0ooo0oo :
     if 'outube' in iIIII1iIIii or 'list' in iIIII1iIIii :
      pass
     elif 'atch' in iIIII1iIIii :
      iIIII1iIIii = ( iIIII1iIIii ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( iIIII1iIIii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOoooooOoO , 'http:' + oOoooooOoO , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( iIIII1iIIii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O , Oo0Oo0O , '' )
    if 21 - 21: I11i1ii1 - oOo0O0Ooo % ii + ooo0O
def o00O0o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for url in next :
  url = 'https://www.youtube.com' + url
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for oOoooooOoO , url , o0OOOo , O0OOoOOO0o0o , OOoOoo00Oo in iI111i :
  iiiiiIIii . append ( o0OOOo )
  iIiIi11 ( 'tvshows' , 'INFO' )
  Oo0Oo0O = 'http:' + ( oOoooooOoO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + Oo0Oo0O
  url = 'http://www.youtube.com' + url
  O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O , Oo0Oo0O , OOoOoo00Oo )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for oOoooooOoO , url , o0OOOo , O0OOoOOO0o0o in iI111i :
   iIiIi11 ( 'tvshows' , 'INFO' )
   Oo0Oo0O = 'http:' + ( oOoooooOoO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oOOo0 = i11111IIIII ( url )
    O0o0O0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for O0o0O0 in O0o0O0 :
     o0OOOo = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0o0O0 ) )
     for o0OOOo in o0OOOo :
      o0OOOo = ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0o0O0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     Oo0Oo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0o0O0 ) )
     for Oo0Oo0O in Oo0Oo0O :
      Oo0Oo0O = 'http:' + Oo0Oo0O
     O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O , Oo00OOOOO , '' )
   elif o0OOOo in iiiiiIIii :
    pass
   elif 'user' in url or 'elete' in o0OOOo :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oOOo0 = i11111IIIII ( url )
    iIOoo0ooo0oo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for oOoooooOoO , url , o0OOOo in iIOoo0ooo0oo :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOoooooOoO , 'http:' + oOoooooOoO , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O , Oo0Oo0O , '' )
    if 28 - 28: oOo0O0Ooo
    if 87 - 87: I11i1ii1 . ooOoO0O00 % ii * Ii
    if 67 - 67: O0Oooo0O / oOo . ii
def OoIIiIIIII1I ( ) :
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Setup Tv Guide[/COLOR]' , '' , 100212 , I1IIIii + 'linkchannels.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Open Guide[/COLOR]' , '' , 100213 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 if 96 - 96: Ii . IIiIiII11i
def iI1I ( ) :
 ivuesetup . iVueInt ( )
 if 11 - 11: IIiIiII11i * i1iIi / IIiIiII11i + i1IiiiI1iI - o0o00Oo0O
def Oo0oooo ( ) :
 oOii11I ( )
 return
 if 97 - 97: ooOoO0O00 + iiiiiiii1 . oOOoOooOo - iiiiiiii1
def oOii11I ( ) :
 if 53 - 53: o0o00Oo0O . oOo0O0Ooo
 OOooOoooOoOo = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 o0oOOoO000 = OOooOoooOoOo . getSetting ( id = 'User' )
 Oo00o00Oo = OOooOoooOoOo . getSetting ( id = 'Pass' )
 i1I1i1I111 = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 oOo00OO0ooOOO = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 i1i1I1Ii1IIii = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 oooOOoo = "http://piesustv" + Ooo + ":8000/get.php?username=" + o0oOOoO000 + "&password=" + Oo00o00Oo + "&type=m3u_plus&output=ts"
 iI1iii1iIiiI = "http://piesustv" + Ooo + ":8000/xmltv.php?username=" + o0oOOoO000 + "&password=" + Oo00o00Oo + "&type=m3u_plus&output=ts"
 if 36 - 36: oOo - o0o00Oo0O * oOo0O0Ooo / oOoO0o00OO0 / OoOo0o
 xbmc . executeJSONRPC ( i1I1i1I111 )
 xbmc . executeJSONRPC ( oOo00OO0ooOOO )
 xbmc . executeJSONRPC ( i1i1I1Ii1IIii )
 if 33 - 33: ii % oOoO0o00OO0 . o0o00Oo0O / oOoO0o00OO0
 O0OoOo = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 O0OoOo . setSetting ( id = 'm3uUrl' , value = oooOOoo )
 O0OoOo . setSetting ( id = 'epgUrl' , value = iI1iii1iIiiI )
 O0OoOo . setSetting ( id = 'm3uCache' , value = "false" )
 O0OoOo . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def OOOOoO0 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 43 - 43: oOo0O0Ooo - ooo0O / ooo0O . IIiIiII11i - i1iIi
if 40 - 40: iiiiiiii1 . iii1i1iiiiIi * o0o00Oo0O
if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + i1IiiiI1iI . OoOo0o
def oo0O ( ) :
 if 23 - 23: oOo0O0Ooo * oOOoOooOo / iii1i1iiiiIi . iI11I1II1I1I % Ii
 if 61 - 61: o0o00Oo0O
 if 21 - 21: oOo % iI11I1II1I1I . oOo
 if 99 - 99: ooo0O * OoOo0o % OOOo00oo0oO * OOOo00oo0oO + ii
 if 82 - 82: i1IiiiI1iI / iii1i1iiiiIi - OoOo0o / oOOoOooOo
 if 50 - 50: OoOo0o + oOo . Ii + oOoO0o00OO0 + Ii
 if 31 - 31: OOOo00oo0oO * O0Oooo0O . iii1i1iiiiIi * i1IiiiI1iI
 if 28 - 28: I11i1ii1 + oOo0O0Ooo - I1ii11iIi11i % OoOo0o . i1IiiiI1iI + oOo0O0Ooo
 if 72 - 72: i1iIi / I1ii11iIi11i / OOOo00oo0oO * iii1i1iiiiIi + OoOo0o
 if 58 - 58: ooo0O % oOo0O0Ooo . oOo0O0Ooo * oOo - I11i1ii1 . ii
 if 10 - 10: O0Oooo0O
 if 48 - 48: iiiiiiii1 * ooOoO0O00 % ii * i1iIi * oOo
 if OooO0 == "insert_username" :
  I1iO0o0O0OooOoo = IiII1i11III ( )
  i1II1IIIII = iIii1ii ( )
  i1 ( 'User' , I1iO0o0O0OooOoo )
  i1 ( 'Pass' , i1II1IIIII )
  xbmc . executebuiltin ( 'Container.Refresh' )
  Ii11i = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( I1iO0o0O0OooOoo , i1II1IIIII )
  Ii11i = i11111IIIII ( Ii11i )
  if Ii11i == "" :
   o0oO00OOo0oO = "[COLOR " + iiI1IiI + "]Incorrect Login Details[/COLOR]"
   oOiiI11I1ii11 = "[COLOR " + iiI1IiI + "]Please Re-enter[/COLOR]"
   O0OoO0oooOO = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , o0oO00OOo0oO , oOiiI11I1ii11 , O0OoO0oooOO )
   oo0O ( )
  else :
   o0oO00OOo0oO = "[COLOR " + iiI1IiI + "]Login Successful[/COLOR]"
   oOiiI11I1ii11 = "[COLOR " + iiI1IiI + "]Welcome to GenieTv[/COLOR]"
   O0OoO0oooOO = ( '[COLOR ' + iiI1IiI + ']%s[/COLOR]' % I1iO0o0O0OooOoo )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , o0oO00OOo0oO , oOiiI11I1ii11 , O0OoO0oooOO )
   xbmc . executebuiltin ( 'Container.Refresh' )
   i1ii11I111Ii ( )
 else :
  i1ii11I111Ii ( )
def IiII1i11III ( ) :
 OOoO00O = xbmc . Keyboard ( '' , 'heading' , True )
 OOoO00O . setHeading ( 'Enter Username' )
 OOoO00O . setHiddenInput ( False )
 OOoO00O . doModal ( )
 if ( OOoO00O . isConfirmed ( ) ) :
  iio00O0o00oo = OOoO00O . getText ( )
  return iio00O0o00oo
 else :
  return False
  if 19 - 19: oOo0O0Ooo
  if 66 - 66: OOOo00oo0oO / iii1i1iiiiIi
def iIii1ii ( ) :
 OOoO00O = xbmc . Keyboard ( '' , 'heading' , True )
 OOoO00O . setHeading ( 'Enter Password' )
 OOoO00O . setHiddenInput ( False )
 OOoO00O . doModal ( )
 if ( OOoO00O . isConfirmed ( ) ) :
  iio00O0o00oo = OOoO00O . getText ( )
  return iio00O0o00oo
 else :
  return False
def iII1I ( ) :
 oooOOoo = "http://piesustv" + Ooo + ":8000//get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  o00oOOo0Oo = urllib2 . urlopen ( oooOOoo )
  print o00oOOo0Oo . getcode ( )
  o00oOOo0Oo . close ( )
  if 91 - 91: IIiIiII11i - iI11I1II1I1I / ooOoO0O00 * ooOoO0O00 % I1ii11iIi11i
  pass
  if 82 - 82: oOOoOooOo
 except urllib2 . HTTPError , OoO :
  print OoO . getcode ( )
  iI111I11I1I1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + iiI1IiI + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + iiI1IiI + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def i1ii11I111Ii ( ) :
 Oo0O00O0O ( )
 if 70 - 70: iI11I1II1I1I + Ii + I1ii11iIi11i / iiiiiiii1
 if 9 - 9: iii1i1iiiiIi - I11i1ii1
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']My Account[/COLOR]' , 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii , 60004 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Guide Menu[/COLOR]' , '' , 100211 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CatchUp Tv[/COLOR]' , '' , 90026 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']VOD Lists[/COLOR]' , '' , 40000 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 39 - 39: ooOoO0O00
 if 19 - 19: oOo0O0Ooo . oOo0O0Ooo - Ii
 if 61 - 61: O0Oooo0O * oOoO0o00OO0 % oOo0O0Ooo % oOo % i1IiiiI1iI + i1IiiiI1iI
 if 6 - 6: I1ii11iIi11i
def O0OOOOoO00oo ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 OoOiII11IiIi = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii + '%26type%3Dm3u_plus%26output%3Dts'
 iII1I1i = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii
 Ii11i = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=get_vod_categories'
 Ii11i = i11111IIIII ( Ii11i )
 if not Ii11i == "" :
  IIiiiooOoOooo00Oo = 'https://tinyurl.com/create.php?source=indexpage&url=' + OoOiII11IiIi + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( IIiiiooOoOooo00Oo ) )
  ooo00O0OOo = 'https://tinyurl.com/create.php?source=indexpage&url=' + iII1I1i + '&submit=Make+TinyURL%21&alias='
  OoOiII11IiIi = i11111IIIII ( IIiiiooOoOooo00Oo )
  iII1I1i = i11111IIIII ( ooo00O0OOo )
  xbmc . log ( str ( iII1I1i ) )
  IiI1 = Iii1IIII1Iii ( OoOiII11IiIi , '<div class="indent"><b>' , '</b>' )
  OOOOOOo0o0O0o = Iii1IIII1Iii ( iII1I1i , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + iiI1IiI + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % IiI1 , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % OOOOOOo0o0O0o )
 else :
  return
def IIIIIIiIIIi1iii1 ( ) :
 iII1I ( )
 iii11III1I ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , oO0oO0O + '&action=get_vod_streams' , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( ooooO )
 iI111i = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  o00oOOooOOo0o ( ( '[COLORsteelblue]' + o0OOOo + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , iIIII1iIIii , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
def O000oooO0 ( url ) :
 open = i11111IIIII ( oOO00 + url )
 oO0o00 = Oo0OOOO0oOoo0 ( open , '<channel>' , '</channel>' )
 for ooOO00oOOo000 in oO0o00 :
  if '<playlist_url>' in open :
   o0OOOo = Iii1IIII1Iii ( ooOO00oOOo000 , '<title>' , '</title>' )
   o0OOOOOo0 = Iii1IIII1Iii ( ooOO00oOOo000 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   o00oOOooOOo0o ( str ( base64 . b64decode ( o0OOOo ) ) . replace ( '?' , '' ) , o0OOOOOo0 , 40001 , icon , OoOo00o0OO , '' )
  else :
   if xbmcaddon . Addon ( ) . getSetting ( 'meta' ) == 'true' :
    try :
     o0OOOo = Iii1IIII1Iii ( ooOO00oOOo000 , '<title>' , '</title>' )
     o0OOOo = base64 . b64decode ( o0OOOo )
     O0OIIII1i = Iii1IIII1Iii ( ooOO00oOOo000 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     url = Iii1IIII1Iii ( ooOO00oOOo000 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     oOOOO = Iii1IIII1Iii ( ooOO00oOOo000 , '<description>' , '</description>' )
     oOOOO = base64 . b64decode ( oOOOO )
     OOooo = Iii1IIII1Iii ( oOOOO , 'PLOT:' , '\n' )
     i1I1Iiii = Iii1IIII1Iii ( oOOOO , 'CAST:' , '\n' )
     I1iIIIiiii = Iii1IIII1Iii ( oOOOO , 'RATING:' , '\n' )
     oo0 = Iii1IIII1Iii ( oOOOO , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
     oo0 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( oo0 )
     I1111 = Iii1IIII1Iii ( oOOOO , 'DURATION_SECS:' , '\n' )
     o00o = Iii1IIII1Iii ( oOOOO , 'GENRE:' , '\n' )
     O0o0oo0O ( str ( o0OOOo ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , O0OIIII1i , OoOo00o0OO , OOooo , str ( oo0 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( i1I1Iiii ) . split ( ) , I1iIIIiiii , I1111 , o00o )
    except : pass
    xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   else :
    o0OOOo = Iii1IIII1Iii ( ooOO00oOOo000 , '<title>' , '</title>' )
    o0OOOo = base64 . b64decode ( o0OOOo )
    O0OIIII1i = Iii1IIII1Iii ( ooOO00oOOo000 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    url = Iii1IIII1Iii ( ooOO00oOOo000 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    oOOOO = Iii1IIII1Iii ( ooOO00oOOo000 , '<description>' , '</description>' )
    O0O0ooOOO ( o0OOOo , url , 222 , O0OIIII1i , OoOo00o0OO , base64 . b64decode ( oOOOO ) )
    if 74 - 74: IIiIiII11i % i1IiiiI1iI . oOo * oOo
I1iIi11iIiII1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
oO00o0O0oOooO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 95 - 95: ii / i1IiiiI1iI % ii / oOOoOooOo * I11i1ii1
def oOiiIIIII ( ) :
 oooOOoo = "http://piesustv" + Ooo + ":8000/get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  o00oOOo0Oo = urllib2 . urlopen ( oooOOoo )
  print o00oOOo0Oo . getcode ( )
  o00oOOo0Oo . close ( )
  if 19 - 19: IIiIiII11i / iii1i1iiiiIi
  pass
  if 80 - 80: iii1i1iiiiIi + iI11I1II1I1I . I11i1ii1
 except urllib2 . HTTPError , OoO :
  print OoO . getcode ( )
  iI111I11I1I1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 76 - 76: oOo0O0Ooo * OoOo0o
 iIIII1iIIii = "http://piesustv" + Ooo + ":8000/xmltv.php?username=%s&password=%s" % ( OooO0 , II11iiii1Ii )
 ii111 ( iIIII1iIIii , oO00o0O0oOooO + "uide.xml" )
 if 49 - 49: oOo + IIiIiII11i / I11i1ii1 - o0o00Oo0O % i1iIi
 oOo0oO = open ( I1iIi11iIiII1 , 'r+' )
 input = open ( I1iIi11iIiII1 ) . read ( ) . decode ( 'UTF-8' )
 iII1i1 = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 oOo0oO . write ( iII1i1 )
 oOo0oO . truncate ( )
 oOo0oO . close ( )
 IIIii ( )
 if 63 - 63: oOo0O0Ooo - Ii - iiiiiiii1 % i1IiiiI1iI . i1iIi * oOoO0o00OO0
def IIIii ( ) :
 open = i11111IIIII ( OooO0o )
 all = Oo0OOOO0oOoo0 ( open , '{"num' , 'direct' )
 for ooOO00oOOo000 in all :
  if '"tv_archive":1' in ooOO00oOOo000 :
   o0OOOo = Iii1IIII1Iii ( ooOO00oOOo000 , '"epg_channel_id":"' , '"' )
   O0OIIII1i = Iii1IIII1Iii ( ooOO00oOOo000 , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = Iii1IIII1Iii ( ooOO00oOOo000 , 'stream_id":"' , '"' )
   o0OOOo = o0OOOo . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   o00oOOooOOo0o ( o0OOOo , id , 90027 , O0OIIII1i , OoOo00o0OO , o0OOOo )
   if 81 - 81: ooOoO0O00 / O0Oooo0O % Ii . iI11I1II1I1I * iii1i1iiiiIi + ii
   if 31 - 31: ooOoO0O00 % IIiIiII11i
def Ii1iii11I ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 OoOo000oOo0oo = open ( I1iIi11iIiII1 )
 Ii11iIiiI = ElementTree . parse ( OoOo000oOo0oo )
 iiII = "apples"
 import datetime as dt
 from datetime import time
 iII1IiiIIIIii = datetime . now ( ) - timedelta ( days = 5 )
 O0O00OooO = str ( iII1IiiIIIIii )
 oOoOooOo0o0 = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 oOOO = Ii11iIiiI . findall ( "programme" )
 for Iii1IiiII1Ii1 in oOOO :
  if name in Iii1IiiII1Ii1 . attrib . get ( 'channel' ) :
   iiiIIi = Iii1IiiII1Ii1 . attrib . get ( 'start' )
   OOoOo0O00oo , oo0oO0oOo0O , OoOo00 = iiiIIi . partition ( ' +' )
   O0O00OooO = str ( O0O00OooO ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   oo0 , OOoOoO , I11II1i1 = iiiIIi . partition ( '2017' )
   OO000 = Iii1IiiII1Ii1 . find ( 'title' ) . text + iiiIIi
   I11II1i1 = I11II1i1 [ : - 6 ]
   if OOoOo0O00oo > O0O00OooO :
    if OOoOo0O00oo < oOoOooOo0o0 :
     o0oOoo0o = OOoOo0O00oo
     o0oOoo0o = o0oOoo0o [ : 4 ] + '/' + o0oOoo0o [ 4 : ]
     OOoOo0O00oo = OOoOo0O00oo [ : 4 ] + '-' + OOoOo0O00oo [ 4 : ]
     o0oOoo0o = o0oOoo0o [ : 7 ] + '/' + o0oOoo0o [ 7 : ]
     OOoOo0O00oo = OOoOo0O00oo [ : 7 ] + '-' + OOoOo0O00oo [ 7 : ]
     o0oOoo0o = o0oOoo0o [ : 10 ] + ' - ' + o0oOoo0o [ 10 : ]
     OOoOo0O00oo = OOoOo0O00oo [ : 10 ] + ':' + OOoOo0O00oo [ 10 : ]
     o0oOoo0o = o0oOoo0o [ : 15 ] + ':' + o0oOoo0o [ 15 : ]
     OOoOo0O00oo = OOoOo0O00oo [ : 13 ] + '-' + OOoOo0O00oo [ 13 : ]
     o0oOoo0o = o0oOoo0o [ : - 2 ]
     OOoOo0O00oo = OOoOo0O00oo [ : - 2 ]
     IiiIiIIi = ( "http://piesustv" + Ooo + ":8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( OOoOo0O00oo ) + "&duration=240" + "&stream=%s" ) % ( OooO0 , II11iiii1Ii , id )
     iiII = IiiIiIIi + str ( OOoOo0O00oo ) + "&duration=240"
     o0oOoo0o = '[COLOR blue]%s - [/COLOR]' % o0oOoo0o
     OO000 = str ( o0oOoo0o ) + Iii1IiiII1Ii1 . find ( 'title' ) . text
     oOOOO = Iii1IiiII1Ii1 . find ( 'desc' ) . text
     O0O0ooOOO ( OO000 , IiiIiIIi , 222 , I1IIIii + 'GTV.png' , Oo00OOOOO , oOOOO )
def O00Oo ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OooO0 ) . replace ( 'PASSWORD' , II11iiii1Ii )
 o0OoOo00ooO = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 o0OoOo00ooO . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 o0OoOo00ooO . setProperty ( 'IsPlayable' , 'true' )
 o0OoOo00ooO . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOo00ooO )
def ii111 ( url , dest ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oO0 . update ( 0 )
 oOOoo = time . time ( )
 urllib . urlretrieve ( url , dest , lambda oo0O0 , Ii111Ii11 , Ii1 : IIIIiII ( oo0O0 , Ii111Ii11 , Ii1 , o0oO0 , oOOoo ) )
def IIIIiII ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  iII11 = min ( numblocks * blocksize * 100 / filesize , 100 )
  O00OO00OOOoO = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  IiI11Ii1iI = numblocks * blocksize / ( time . time ( ) - start_time )
  if IiI11Ii1iI > 0 :
   ooOo0 = ( filesize - numblocks * blocksize ) / IiI11Ii1iI
  else :
   ooOo0 = 0
  IiI11Ii1iI = IiI11Ii1iI / 1024
  oOo0o = IiI11Ii1iI / 1024
  O000OOO000o = float ( filesize ) / ( 1024 * 1024 )
  I11iiIiiI1iIi11 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( O00OO00OOOoO )
  OoO = '[COLOR white]Speed:  %.02f Mb/s ' % oOo0o + '[/COLOR]'
  dp . update ( iII11 , I11iiIiiI1iIi11 , OoO )
 except :
  iII11 = 100
  dp . update ( iII11 )
 if dp . iscanceled ( ) :
  II1I1I11i1I1 = xbmcgui . Dialog ( )
  II1I1I11i1I1 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 9 - 9: ii / ii - i1IiiiI1iI
  sys . exit ( )
  dp . close ( )
  if 84 - 84: IIiIiII11i
def i1IIii1i ( ) :
 if II11iiii1Ii == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  O0oOo0o0O0o ( )
  if 76 - 76: o0o00Oo0O
  if 71 - 71: oOo0O0Ooo . ooOoO0O00
  if 19 - 19: IIiIiII11i / IIiIiII11i % oOoO0o00OO0 + OOOo00oo0oO + OOOo00oo0oO + iiiiiiii1
  if 4 - 4: ooo0O + i1IiiiI1iI / iiiiiiii1 + ooOoO0O00 % ooo0O % iiiiiiii1
  if 80 - 80: i1iIi
  if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
  if 59 - 59: oOoO0o00OO0 + i1IiiiI1iI . OOOo00oo0oO
  if 87 - 87: oOo
def O0oOo0o0O0o ( ) :
 IIIi1I1IIii1II = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( '"exp_date":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for iIIII1iIIii in iI111i :
  dt = datetime . fromtimestamp ( float ( iI111i [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if oOoOooOo0o0 <= dt <= oOoOooOo0o0 + timedelta ( hours = 24 ) :
   iI111I11I1I1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + iiI1IiI + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + iiI1IiI + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + iiI1IiI + '] To Purchase A licence[/COLOR]' )
def I1ii1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( '"username":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 II1iII1 = re . compile ( '"password":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 oOoOOOo = re . compile ( '"status":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 IIi11i1i1iI1 = re . compile ( '"exp_date":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 Ii1II1I11i1 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 iIiiii = re . compile ( '"created_at":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 O0000OOO0 = re . compile ( '"max_connections":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 ooo0 = re . compile ( '"is_trial":"1"' ) . findall ( IIIi1I1IIii1II )
 Oo00OoOo = re . compile ( '"is_trial":"0"' ) . findall ( IIIi1I1IIii1II )
 I11II11IiI11 = O00o ( )
 Ii11Iiii1iiii = i1IIII1111 ( )
 for url in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']My GTV Account Information[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in II1iII1 :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in oOoOOOo :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in iIiiii :
  dt = datetime . fromtimestamp ( float ( iIiiii [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in IIi11i1i1iI1 :
  dt = datetime . fromtimestamp ( float ( IIi11i1i1iI1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if oOoOooOo0o0 <= dt <= oOoOooOo0o0 + timedelta ( hours = 24 ) :
   I111i1i1111 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in Ii1II1I11i1 :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in O0000OOO0 :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in ooo0 :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] Yes' , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in Oo00OoOo :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] No' , '' , '' , I1IIIii + 'MyAcc.png' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Get Short Links[/COLOR]' , '' , 100214 , I1IIIii + 'shortlinks.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local IP Address:[/COLOR] ' + I11II11IiI11 , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']External IP Address:[/COLOR] ' + Ii11Iiii1iiii , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 84 - 84: o0o00Oo0O % i1iIi . i1iIi . iiiiiiii1 * i1IiiiI1iI
 I111i1i1111 ( '[COLOR' + iiI1IiI + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 43 - 43: iii1i1iiiiIi . oOoO0o00OO0 % ooOoO0O00
def OO0O00 ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
 ooOO ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 66 - 66: I1ii11iIi11i / Ii % oOOoOooOo
def i1Ii1i11ii ( data ) :
 oO0O0oo = len ( data ) % 4
 if 64 - 64: iii1i1iiiiIi % iii1i1iiiiIi + ooo0O + I1ii11iIi11i
 if 79 - 79: I1ii11iIi11i - ii % O0Oooo0O + ii - i1IiiiI1iI % iii1i1iiiiIi
 if 5 - 5: iii1i1iiiiIi . I1ii11iIi11i
 if 89 - 89: oOo0O0Ooo / iiiiiiii1 / ii - Ii + oOo0O0Ooo
 if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . i1IiiiI1iI
 if 64 - 64: oOOoOooOo / ooOoO0O00 % iiiiiiii1
 if oO0O0oo != 0 :
  data += b'=' * ( 4 - oO0O0oo )
 return base64 . decodestring ( data )
def Iii1IIII1Iii ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : OOoOo0O0 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : OOoOo0O0 = ''
 else :
  try : OOoOo0O0 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : OOoOo0O0 = ''
 return OOoOo0O0
 if 39 - 39: O0Oooo0O . oOo % oOOoOooOo . OoOo0o / iiiiiiii1 * oOo
 if 12 - 12: oOo0O0Ooo / ooo0O
def Oo0OOOO0oOoo0 ( text , start_with , end_with ) :
 OOoOo0O0 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return OOoOo0O0
def O00o ( ) :
 oOO0O00o0O0 = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 oOO0O00o0O0 . connect ( ( '8.8.8.8' , 0 ) )
 oOO0O00o0O0 = oOO0O00o0O0 . getsockname ( ) [ 0 ]
 return oOO0O00o0O0
 if 68 - 68: Ii + oOo
def i1IIII1111 ( ) :
 open = i11111IIIII ( 'http://canyouseeme.org/' )
 I11II11IiI11 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( I11II11IiI11 . group ( ) )
oO0oO0O = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
OooO0o = 'http://piesustv' + Ooo + ':8000/panel_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
i1iiiiii1 = 'http://piesustv' + Ooo + ':8000/movie/%s/%s/' % ( OooO0 , II11iiii1Ii )
OoO0oOOOO = 'http://piesustv' + Ooo + ':8000/live/%s/%s/' % ( OooO0 , II11iiii1Ii )
o0oo00OOOo = '&action=get_live_categories'
oo0oO = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OooO0 , II11iiii1Ii )
ooooO = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OooO0 , II11iiii1Ii )
if 17 - 17: oOOoOooOo + oOOoOooOo . oOoO0o00OO0
oOO00 = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OooO0 , II11iiii1Ii )
iiI1ii1Iii11I = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OooO0 , II11iiii1Ii )
IIiIi11 = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OooO0 , II11iiii1Ii )
oO0OO0O0 = "http://piesustv" + Ooo + ":8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OooO0 , II11iiii1Ii )
if 18 - 18: oOo0O0Ooo - iii1i1iiiiIi
def II1III ( ) :
 iII1I ( )
 open = i11111IIIII ( IIiIi11 )
 oO0o00 = Oo0OOOO0oOoo0 ( open , '<channel>' , '</channel>' )
 for ooOO00oOOo000 in oO0o00 :
  o0OOOo = Iii1IIII1Iii ( ooOO00oOOo000 , '<title>' , '</title>' )
  o0OOOo = base64 . b64decode ( o0OOOo )
  o0OOOOOo0 = Iii1IIII1Iii ( ooOO00oOOo000 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o00oOOooOOo0o ( '[COLORsteelblue]' + o0OOOo + '[/COLOR]' , o0OOOOOo0 , 60003 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
  if 14 - 14: oOoO0o00OO0 * O0Oooo0O % ooOoO0O00 / oOoO0o00OO0
def i11II1 ( url ) :
 open = i11111IIIII ( oO0OO0O0 + url )
 oO0o00 = Oo0OOOO0oOoo0 ( open , '<channel>' , '</channel>' )
 for ooOO00oOOo000 in oO0o00 :
  o0OOOo = Iii1IIII1Iii ( ooOO00oOOo000 , '<title>' , '</title>' )
  o0OOOo = base64 . b64decode ( o0OOOo )
  xbmc . log ( str ( o0OOOo ) )
  O0OIIII1i = Iii1IIII1Iii ( ooOO00oOOo000 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o0OOOOOo0 = Iii1IIII1Iii ( ooOO00oOOo000 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  oOOOO = Iii1IIII1Iii ( ooOO00oOOo000 , '<description>' , '</description>' )
  oOOOO = base64 . b64decode ( oOOOO )
  o0o00o = '('
  IIiI = ')'
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , o0OOOOOo0 , 222 , O0OIIII1i , OoOo00o0OO , ( '[COLOR' + iiI1IiI + ']' + oOOOO + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( IIiI , '[COLORsteelblue]' ) . replace ( o0o00o , '[COLORorangered]' ) )
  if 99 - 99: ooo0O * OOOo00oo0oO . O0Oooo0O / iii1i1iiiiIi . oOOoOooOo
def i111iIi1i1 ( url ) :
 url = url
 oOOo0 = i11111IIIII ( oo0oO + url )
 iI111i = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , type , IIi11i1II , o0o0OO0o00o0O in iI111i :
  Ii1I1 = ( OoO0oOOOO + IIi11i1II + '.m3u8' ) . strip ( )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , Ii1I1 , 222 , ( o0o0OO0o00o0O ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
def OOo00O0O ( url , name , img ) :
 img = img
 name = name
 url = url
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/xmltv.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oOOo0 )
 for O00oO0 , oooOoO in iI111i :
  if name == O00oO0 :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) + oooOoO , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def IiiIi1IiiiI ( name ) :
 OO0oooOO = name
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oOOo0 )
 for name , oOoooooOoO , iIIII1iIIii in iI111i :
  iIIII1iIIii = ( iIIII1iIIii ) . replace ( '.ts' , '.m3u8' )
  O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iIIII1iIIii ) . strip ( ) , 222 , oOoooooOoO , oOoooooOoO , '' )
 else :
  O0O0ooOOO ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 30 - 30: OOOo00oo0oO . oOo + i1IiiiI1iI / iI11I1II1I1I % I1ii11iIi11i / OOOo00oo0oO
  if 3 - 3: oOoO0o00OO0 / IIiIiII11i
  if 73 - 73: oOo * ii - ii + oOo0O0Ooo * I1ii11iIi11i
  if 87 - 87: ooo0O / I11i1ii1 / Ii
  if 95 - 95: ooOoO0O00 / i1iIi / i1iIi
  if 65 - 65: O0Oooo0O + iiiiiiii1 * iiiiiiii1
  if 79 - 79: ooOoO0O00 / I1ii11iIi11i - oOo0O0Ooo . o0o00Oo0O
  if 56 - 56: I11i1ii1 % o0o00Oo0O * ooOoO0O00 - IIiIiII11i
  if 74 - 74: ooOoO0O00 - iii1i1iiiiIi % OOOo00oo0oO . o0o00Oo0O - ii
  if 84 - 84: O0Oooo0O
  if 53 - 53: ooOoO0O00
  if 59 - 59: ooo0O + oOo0O0Ooo % ii - iI11I1II1I1I
def iiiIi ( ) :
 o00oOOooOOo0o ( 'Full Backup' , '' , 10061 , I1IIIii + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0OoO00oOO0o ) :
  o00oOOooOOo0o ( 'Backup Genie Favourites' , iIIII1iIIii , 10062 , I1IIIii + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( ooOooo000oOO ) :
  o00oOOooOOo0o ( 'Backup Ivue Config' , ooOooo000oOO , 10062 , I1IIIii + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( Oo0oOOo ) :
  o00oOOooOOo0o ( 'Backup Kodi Favourites' , Oo0oOOo , 10062 , I1IIIii + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 9 - 9: ooOoO0O00 - iii1i1iiiiIi
  if 57 - 57: iI11I1II1I1I * i1iIi * iiiiiiii1 / OOOo00oo0oO
  if 46 - 46: i1iIi
zip = O0oo0OO0 . getSetting ( 'zip' )
oOO0 = xbmc . translatePath ( os . path . join ( zip ) )
def IiIi ( ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 45 - 45: iii1i1iiiiIi * oOOoOooOo / ii + oOo . O0Oooo0O / oOo
  if 64 - 64: i1iIi / ooOoO0O00 % oOo0O0Ooo - ooo0O
  if 11 - 11: oOoO0o00OO0 - ii
def I1Ii11I11i1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0OoO00oOO0o
  elif 'Ivue' in name :
   url = ooOooo000oOO
  elif 'Kodi' in name :
   url = Oo0oOOo
  IiIi ( )
  IiII1 = open ( url ) . read ( )
  iI1I1I = os . path . join ( oOO0 , description . split ( 'Your ' ) [ 1 ] )
  oOo0oO = open ( iI1I1I , mode = 'w' )
  oOo0oO . write ( IiII1 )
  oOo0oO . close ( )
 else :
  if 'guisettings.xml' in description :
   ooOO00oOOo000 = open ( os . path . join ( oOO0 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoOo0O0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   iI111i = re . compile ( OOoOo0O0 ) . findall ( ooOO00oOOo000 )
   for type , Oo0o0oOo0oO , i1iiiI1I in iI111i :
    i1iiiI1I = i1iiiI1I . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , Oo0o0oOo0oO , i1iiiI1I ) )
  else :
   iI1I1I = os . path . join ( url )
   IiII1 = open ( os . path . join ( oOO0 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOo0oO = open ( iI1I1I , mode = 'w' )
   oOo0oO . write ( IiII1 )
   oOo0oO . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 98 - 98: OoOo0o
 if 69 - 69: IIiIiII11i + I1ii11iIi11i - OOOo00oo0oO . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
 if 75 - 75: oOo % ii
 if 16 - 16: o0o00Oo0O / ooOoO0O00
def OOoo0 ( ) :
 Ii11I1iIIi = 1
 IiIi ( )
 O0ooO = xbmc . translatePath ( os . path . join ( oOO0 , 'Build Backup' , 'Full Backup' , '' ) )
 iIOO = xbmc . translatePath ( os . path . join ( oOO0 , 'Build Backup' , 'my_full_backup.zip' ) )
 I1III1I11I1 = xbmc . translatePath ( os . path . join ( oOO0 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( O0ooO ) :
  os . makedirs ( O0ooO )
 oO000OoO00OoO = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oO000OoO00OoO ) : return False , 0
 iI = oO000OoO00OoO
 I1IiIi1iiI = xbmc . translatePath ( os . path . join ( O0ooO , iI + '.zip' ) )
 iiII1II11i = [ 'plugin.video.GenieTv' ]
 ooO0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 OoooooOo0oOo0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 II11II = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 i1ii11 = "Creating full backup of existing build"
 IIIo00O = "Creating Community Build"
 ii1I1I1 = "Archiving..."
 oo0oOOO0oOoo = ""
 Ii1o0OOOoo0000 = "Please Wait"
 IiI ( i1111 , I1IiIi1iiI , IIIo00O , ii1I1I1 , oo0oOOO0oOoo , Ii1o0OOOoo0000 , OoooooOo0oOo0 , II11II )
 time . sleep ( 1 )
 Iii1i1i11iII = xbmc . translatePath ( os . path . join ( O0ooO , iI + '_guisettings.zip' ) )
 o0II1 = zipfile . ZipFile ( Iii1i1i11iII , mode = 'w' )
 try :
  o0II1 . write ( xbmc . translatePath ( os . path . join ( i1111 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 o0II1 . close ( )
 if Ii11I1iIIi == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iIOO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + I1IiIi1iiI + '[/COLOR]' )
  if 86 - 86: OOOo00oo0oO . oOo0O0Ooo - O0Oooo0O + iI11I1II1I1I
def IiI ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0O00ooo0 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iI1 = len ( sourcefile )
 iIi1 = [ ]
 O00oOOO0 = [ ]
 o0oO0 . create ( message_header , message1 , message2 , message3 )
 for Iiiiii , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( sourcefile ) :
  for file in oo0OOO0OOoOO :
   O00oOOO0 . append ( file )
 oOoO = len ( O00oOOO0 )
 for Iiiiii , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( sourcefile ) :
  oOOOOOoOOoo0 [ : ] = [ II1i1 for II1i1 in oOOOOOoOOoo0 if II1i1 not in exclude_dirs ]
  oo0OOO0OOoOO [ : ] = [ oOo0oO for oOo0oO in oo0OOO0OOoOO if oOo0oO not in exclude_files ]
  for file in oo0OOO0OOoOO :
   iIi1 . append ( file )
   o0o0oo0OOo0O0 = len ( iIi1 ) / float ( oOoO ) * 100
   o0oO0 . update ( int ( o0o0oo0OOo0O0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iIIiiII11i1I1 = os . path . join ( Iiiiii , file )
   if not 'temp' in oOOOOOoOOoo0 :
    if not 'plugin.program.originwizard' in oOOOOOoOOoo0 :
     import time
     Ii111Ii1iiIi1 = '01/01/1980'
     OOI11i1IIi1i1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iIIiiII11i1I1 ) ) )
     if OOI11i1IIi1i1 > Ii111Ii1iiIi1 :
      o0O00ooo0 . write ( iIIiiII11i1I1 , iIIiiII11i1I1 [ iI1 : ] )
 o0O00ooo0 . close ( )
 o0oO0 . close ( )
 if 28 - 28: i1IiiiI1iI . ii * OoOo0o + Ii % oOo0O0Ooo . iI11I1II1I1I
 if 63 - 63: IIiIiII11i - i1IiiiI1iI . iii1i1iiiiIi
def IIi1I1iII111 ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 if 76 - 76: oOOoOooOo . OOOo00oo0oO
 if 60 - 60: OoOo0o * oOOoOooOo * oOo
def O0ooOIii1iIIIi11I1 ( ) :
 Oo0O00O0O ( )
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  I1I1 ( )
 if oo000o0000oO == 1 :
  I1i11 ( )
 if oo000o0000oO == 2 :
  IIII11Ii1I11I ( )
 if oo000o0000oO == 3 :
  OooOo ( )
  if 40 - 40: i1iIi + oOoO0o00OO0 * O0Oooo0O - OOOo00oo0oO % i1iIi
  if 67 - 67: oOoO0o00OO0
  if 3 - 3: O0Oooo0O . i1IiiiI1iI % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oOo
  if 5 - 5: IIiIiII11i * ooOoO0O00 % i1iIi
  if 55 - 55: oOo0O0Ooo + iiiiiiii1
  if 85 - 85: OOOo00oo0oO + iiiiiiii1 % iiiiiiii1 / i1IiiiI1iI . oOo0O0Ooo - iii1i1iiiiIi
  if 19 - 19: i1IiiiI1iI / iiiiiiii1 + I11i1ii1
  if 76 - 76: iI11I1II1I1I / O0Oooo0O - oOoO0o00OO0 % ooo0O % OoOo0o + ii
  if 10 - 10: oOo * i1IiiiI1iI / I1ii11iIi11i - O0Oooo0O
def I1iIi1IiI1i ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']RaysRavers Radio[/COLOR]' , '[COLOR' + iiI1IiI + ']ThunderStruck[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if oo000o0000oO == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if oo000o0000oO == 2 :
   IiiIiiiiI1III ( )
  if oo000o0000oO == 3 :
   II111111 ( )
  if oo000o0000oO == 4 :
   i1iI1i11iIi1 ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if oo000o0000oO == 5 :
   Oo0O00O ( )
  if oo000o0000oO == 6 :
   OOoOOO0 ( ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if oo000o0000oO == 7 :
   IiI1i1i1 ( ( o0oOoO00o ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if oo000o0000oO == 8 :
   O0O000oOO0 ( str ( O00OOOoOoo0O ) + ( o0oOoO00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if oo000o0000oO == 9 :
   I1iI1iiI1Ii1 ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RaysRavers Radio[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , I1IIIii + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']ThunderStruck[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , I1IIIii + 'Thunder.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , I1IIIii + 'RadioNomy.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( O00OOOoOoo0O ) , 30031 , I1IIIii + 'MusicChannels.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , I1IIIii + 'UKRadio.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( O00OOOoOoo0O ) , 1013 , I1IIIii + 'WorldRadio.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CONCERTS' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , I1IIIii + 'Concerts.png' , Oo00OOOOO , '' )
   if 62 - 62: i1IiiiI1iI % OOOo00oo0oO / ii % ii
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , I1IIIii + 'MusicVideos.png' , Oo00OOOOO , '' )
  if 65 - 65: o0o00Oo0O . oOoO0o00OO0 * O0Oooo0O
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( O00OOOoOoo0O ) , 1111 , I1IIIii + 'MusicSearch.png' , Oo00OOOOO , '' )
  if 39 - 39: iI11I1II1I1I % o0o00Oo0O + I1ii11iIi11i
  if 71 - 71: ii + ooOoO0O00 + OOOo00oo0oO * i1iIi + Ii - OOOo00oo0oO
 iIiIi11 ( 'movies' , 'MAIN' )
I1i1i = 'white'
OOOOooO0oO00O0o = 'gold'
def oo0OoO ( ) :
 Oo0O00O0O ( )
 if IiIi1 ( True ) == False : I11iIiiI = 0
 else : I11iIiiI = I1i ( IiIi1 ( True ) , True , True )
 if IiIi1 ( True , True ) == False : OO000oo0o = 0
 else : OO000oo0o = I1i ( IiIi1 ( True , True ) , True , True )
 I11iiIiI1II11 = int ( I11iIiiI ) + int ( OO000oo0o )
 OOOoOOOo = str ( I11iiIiI1II11 ) + ' Error(s) Found' if I11iiIiI1II11 > 0 else 'None Found'
 oO0000 = ': [COLORsteelblue]Not Found[/COLOR]' if not os . path . exists ( Oo0o0000o0o0 ) else ": [COLORorangered]%s[/COLOR]" % OOOIIIIiiIi ( os . path . getsize ( Oo0o0000o0o0 ) )
 ooooOOo = O0Oo0oO0OO0 ( oO )
 oo0o0 = O0Oo0oO0OO0 ( i1iiIIiiI111 )
 OoO00o00 = ooOo ( )
 o0oo00000O = ooooOOo + oo0o0 + OoO00o00
 I11II11IiI11 = O00o ( )
 Ii11Iiii1iiii = i1IIII1111 ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAN UP:[COLORorangered] [B]%s[/B][/COLOR]' % OOOIIIIiiIi ( o0oo00000O ) , 'url' , 9666 , I1IIIii + 'MAIN5.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , I1IIIii + 'KillKodi.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , I1IIIii + 'Speedtest.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG Errors:[COLORorangered] %s[/COLOR]' % ( OOOoOOOo ) , '' , 219999990 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR LOG FILES: [COLORorangered]' + oO0000 + '[/COLOR]' , '' , 219999991 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE CACHE:[COLORorangered] [B]%s[/B][/COLOR]' % OOOIIIIiiIi ( OoO00o00 ) , 'url' , 14 , I1IIIii + 'DeleteCache.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE PACKAGES:[COLORorangered] [B]%s[/B][/COLOR]' % OOOIIIIiiIi ( ooooOOo ) , 'url' , 6 , I1IIIii + 'DeletePackages.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , 'url' , 10 , I1IIIii + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']LAST RESORT FIX EMPTY REPOS[/COLOR]' , 'url' , 9 , I1IIIii + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR THUBMNAILS:[COLORorangered] [B]%s[/B][/COLOR]' % OOOIIIIiiIi ( oo0o0 ) , 'url' , 219999992 , I1IIIii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Local IP Address:[COLORorangered] ' + I11II11IiI11 + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']External IP Address:[COLORorangered] ' + Ii11Iiii1iiii + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 84 - 84: iI11I1II1I1I
 if 25 - 25: oOo * I11i1ii1 - ooOoO0O00 - i1IiiiI1iI * IIiIiII11i
 iIiIi11 ( 'movies' , 'MAIN' )
def oo00OO ( proc ) :
 xbmc . executebuiltin ( proc )
 if 63 - 63: oOo % ooOoO0O00 - OOOo00oo0oO
def Iii1i11 ( ) :
 oo00OO ( 'Container.Refresh()' )
def IIii1 ( ) :
 oOo0oO = open ( Oo0o0000o0o0 , 'w' ) ; oOo0oO . close ( ) ; OOOoO ( "[COLOR %s]%s[/COLOR]" % ( I1i1i , oOo0oooo00o ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % OOOOooO0oO00O0o )
 Iii1i11 ( )
 if 89 - 89: iii1i1iiiiIi - oOOoOooOo . iI11I1II1I1I + iiiiiiii1 / i1iIi / iiiiiiii1
def IiIi11i ( type = None ) :
 i1I11IiI = iiiiI ( 'Textures' )
 if not type == None : oo000o0000oO = 1
 else : oo000o0000oO = iI111I11I1I1 . yesno ( oOo0oooo00o , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( OOOOooO0oO00O0o , i1I11IiI ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if oo000o0000oO == 1 :
  try : IiO0o ( os . join ( oooOOOOO , i1I11IiI ) )
  except : oOo0Oooo ( 'Failed to delete, Purging DB.' ) ; I1iiIIiI11I ( i1I11IiI )
  I11II1I ( i1iiIIiiI111 )
  if 92 - 92: ooo0O
 else : oOo0Oooo ( 'Clear thumbnames cancelled' )
 ii111Ii1i ( )
 if 46 - 46: ooOoO0O00 - iiiiiiii1 + O0Oooo0O + oOo + i1IiiiI1iI
 if 45 - 45: oOo0O0Ooo + i1IiiiI1iI + ooOoO0O00
def ii111Ii1i ( ) :
 if not os . path . exists ( i1iiIIiiI111 ) : os . makedirs ( i1iiIIiiI111 )
 i1II = '0123456789abcdef'
 OOOoooOo00O = os . path . join ( i1iiIIiiI111 , 'Video' , 'Bookmarks' )
 for II1I in i1II :
  iiIIiI1I = os . path . join ( i1iiIIiiI111 , II1I )
  if not os . path . exists ( iiIIiI1I ) : os . makedirs ( iiIIiI1I )
 if not os . path . exists ( OOOoooOo00O ) : os . makedirs ( OOOoooOo00O )
 if 67 - 67: oOoO0o00OO0 % ii
def iiiiI ( DB ) :
 if DB in [ 'Addons' , 'ADSP' , 'Epg' , 'MyMusic' , 'MyVideos' , 'Textures' , 'TV' , 'ViewModes' ] :
  iI111i = glob . glob ( os . path . join ( oooOOOOO , '%s*.db' % DB ) )
  III1 = '%s(.+?).db' % DB [ 1 : ]
  I1I11 = 0
  for file in iI111i :
   try : Oo0I1iii = int ( re . compile ( III1 ) . findall ( file ) [ 0 ] )
   except : Oo0I1iii = 0
   if I1I11 < Oo0I1iii :
    I1I11 = Oo0I1iii
  return '%s%s.db' % ( DB , I1I11 )
 else : return False
 if 85 - 85: oOoO0o00OO0 * iii1i1iiiiIi % i1IiiiI1iI
def I11II1I ( path ) :
 oOo0Oooo ( "Deleting Folder: %s" % path , xbmc . LOGNOTICE )
 try : shutil . rmtree ( path , ignore_errors = True , onerror = None )
 except : return False
 if 29 - 29: oOoO0o00OO0
def I1iiIIiI11I ( name ) :
 if 91 - 91: oOo
 if 54 - 54: oOoO0o00OO0 . oOOoOooOo + O0Oooo0O % oOOoOooOo
 if 67 - 67: oOo
 oOo0Oooo ( 'Purging DB %s.' % name , xbmc . LOGNOTICE )
 if os . path . exists ( name ) :
  try :
   oOoo00 = database . connect ( name )
   O000 = oOoo00 . cursor ( )
  except Exception , OoO :
   oOo0Oooo ( "DB Connection Error: %s" % str ( OoO ) , xbmc . LOGERROR )
   return False
 else : oOo0Oooo ( '%s not found.' % name , xbmc . LOGERROR ) ; return False
 O000 . execute ( "SELECT name FROM sqlite_master WHERE type = 'table'" )
 for O0oooOo0000o0 in O000 . fetchall ( ) :
  if O0oooOo0000o0 [ 0 ] == 'version' :
   oOo0Oooo ( 'Data from table `%s` skipped.' % O0oooOo0000o0 [ 0 ] , xbmc . LOGDEBUG )
  else :
   try :
    O000 . execute ( "DELETE FROM %s" % O0oooOo0000o0 [ 0 ] )
    oOoo00 . commit ( )
    oOo0Oooo ( 'Data from table `%s` cleared.' % O0oooOo0000o0 [ 0 ] , xbmc . LOGDEBUG )
   except Exception , OoO : oOo0Oooo ( "DB Remove Table `%s` Error: %s" % ( O0oooOo0000o0 [ 0 ] , str ( OoO ) ) , xbmc . LOGERROR )
 O000 . close ( )
 oOo0Oooo ( '%s DB Purging Complete.' % name , xbmc . LOGNOTICE )
 oooOoO = name . replace ( '\\' , '/' ) . split ( '/' )
 OOOoO ( "[COLOR %s]Purge Database[/COLOR]" % I1i1i , "[COLOR %s]%s Complete[/COLOR]" % ( OOOOooO0oO00O0o , oooOoO [ len ( oooOoO ) - 1 ] ) )
 if 95 - 95: OOOo00oo0oO
def IiO0o ( path ) :
 oOo0Oooo ( "Deleting File: %s" % path , xbmc . LOGNOTICE )
 try : os . remove ( path )
 except : return False
 if 80 - 80: I11i1ii1
 if 42 - 42: ii * IIiIiII11i
def ooOo ( ) :
 O0oooOO = os . path . join ( oO0o0o0ooO0oO , 'addon_data' )
 IIiIi1I1iI1 = [
 ( os . path . join ( I11 , 'plugin.video.phstreams' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.bob' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.specto' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.genesis' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.exodus' , 'cache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'onechannelcache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'saltscache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'saltshd.lite.db' ) ) ]
 i1I111II11 = [
 ( O0oooOO ) ,
 ( I11 ) ,
 ( os . path . join ( i1111 , 'cache' ) ) ,
 ( os . path . join ( i1111 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( O0oooOO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( O0oooOO , 'plugin.video.itv' , 'Images' ) ) ]
 if 56 - 56: O0Oooo0O / o0o00Oo0O * OoOo0o
 o0oo00000O = 0
 if 32 - 32: iiiiiiii1 . iI11I1II1I1I % I1ii11iIi11i . ii
 for II1I in i1I111II11 :
  if os . path . exists ( II1I ) and not II1I in [ I11 , O0oooOO ] :
   o0oo00000O = O0Oo0oO0OO0 ( II1I , o0oo00000O )
  else :
   for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( II1I ) :
    for II1i1 in oOOOOOoOOoo0 :
     if 'cache' in II1i1 . lower ( ) and not II1i1 . lower ( ) == 'meta_cache' : o0oo00000O = O0Oo0oO0OO0 ( os . path . join ( Ooo00OoO0O00 , II1i1 ) , o0oo00000O )
     if 11 - 11: i1IiiiI1iI
 return o0oo00000O
def O0Oo0oO0OO0 ( path , total = 0 ) :
 for IioooooOOo0Oo , IiiiiiiI111i , Oooooooo00o00 in os . walk ( path ) :
  for oOo0oO in Oooooooo00o00 :
   iiIIIIiI11II1 = os . path . join ( IioooooOOo0Oo , oOo0oO )
   total += os . path . getsize ( iiIIIIiI11II1 )
 return total
def OOOIIIIiiIi ( num , suffix = 'B' ) :
 for IiI1i11i1iI in [ '' , 'K' , 'M' , 'G' ] :
  if abs ( num ) < 1024.0 :
   return "%3.02f %s%s" % ( num , IiI1i11i1iI , suffix )
  num /= 1024.0
 return "%.02f %s%s" % ( num , 'G' , suffix )
 if 92 - 92: OoOo0o % IIiIiII11i . iiiiiiii1
def Iii1ii1II11i ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']REPOS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , I1IIIii + 'repos.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEW[/COLOR]' , str ( O00OOOoOoo0O ) , 22 , I1IIIii + 'NEW.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']IPTV[/COLOR]' , str ( O00OOOoOoo0O ) , 23 , I1IIIii + 'IPTV.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']VIDEO[/COLOR]' , str ( O00OOOoOoo0O ) , 24 , I1IIIii + 'VIDEO.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SPORTS[/COLOR]' , str ( O00OOOoOoo0O ) , 25 , I1IIIii + 'SPORTS.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( O00OOOoOoo0O ) , 26 , I1IIIii + 'KIDS.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( O00OOOoOoo0O ) , 27 , I1IIIii + 'MUSIC.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PROGRAMS[/COLOR]' , str ( O00OOOoOoo0O ) , 28 , I1IIIii + 'PROGRAMS.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']XXX[/COLOR]' , 'URL' , 29 , I1IIIii + 'XXX.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 46 - 46: iii1i1iiiiIi + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
 if 47 - 47: iiiiiiii1 * iii1i1iiiiIi * I11i1ii1
def iIiii1IIi1I ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( 'CHECK ADVANCED XML' , str ( O00OOOoOoo0O ) , 8 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'MUCKYS XML' , str ( O00OOOoOoo0O ) + '/wizard/muckys.xml' , 7 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '0CACHE XML' , str ( O00OOOoOoo0O ) + '/wizard/0cache.xml' , 7 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'MIKEY1234 XML' , str ( O00OOOoOoo0O ) + '/wizard/mikey.xml' , 7 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'TUXENS XML' , str ( O00OOOoOoo0O ) + '/wizard/tuxens.xml' , 7 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'P2P RECOMMENDED XML1' , str ( O00OOOoOoo0O ) + '/wizard/p2p1.xml' , 7 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'P2P RECOMMENDED XML2' , str ( O00OOOoOoo0O ) + '/wizard/p2p2.xml' , 7 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'DELETE XML' , str ( O00OOOoOoo0O ) , 11 , I1IIIii + 'XML.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 18 - 18: o0o00Oo0O / iI11I1II1I1I + Ii + I1ii11iIi11i
def II1Iii ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , I1IIIii + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , I1IIIii + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 31 - 31: ooOoO0O00 - i1IiiiI1iI + O0Oooo0O + oOOoOooOo . oOOoOooOo . o0o00Oo0O
def ii11I ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( O00OOOoOoo0O ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , I1IIIii + 'FTV4.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( O00OOOoOoo0O ) + '/wizard/customftv/settings.xml' , 17 , I1IIIii + 'FTV3.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , I1IIIii + 'FTV1.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'RESET FTV DATABASE' , 'url' , 18 , I1IIIii + 'FTV2.png' , Oo00OOOOO , '' )
 if 2 - 2: OOOo00oo0oO . OoOo0o
 if 43 - 43: iI11I1II1I1I
 if 29 - 29: I11i1ii1 % oOOoOooOo + oOo . ooOoO0O00 + oOo0O0Ooo
def I111I ( ) :
 Oo0O00O0O ( )
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  oooO ( )
 if oo000o0000oO == 0 :
  oo0OOoOo0 ( iIIII1iIIii )
 if oo000o0000oO == 0 :
  oO00oO0 ( iIIII1iIIii )
  if 80 - 80: iiiiiiii1 . o0o00Oo0O
  if 25 - 25: iiiiiiii1 / iI11I1II1I1I + oOo0O0Ooo / oOOoOooOo
  if 61 - 61: OOOo00oo0oO % oOoO0o00OO0 * i1IiiiI1iI . i1IiiiI1iI
 iIiIi11 ( 'movies' , 'MAIN' )
 if 20 - 20: i1iIi / iiiiiiii1 + IIiIiII11i . Ii . OoOo0o
def o0oOOO0 ( ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 iI111i = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOoooooOoO , o0OOOo in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOoooooOoO , oOoooooOoO , '' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 11 - 11: i1IiiiI1iI / iii1i1iiiiIi
def ii1IIi1IIIIi1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( iI1i1iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 5 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 16 - 16: ooOoO0O00 * oOOoOooOo % oOo + i1iIi
def oooO ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( O00OOOoOoo0O ) , 36 , I1IIIii + 'GothamSkins.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( O00OOOoOoo0O ) , 37 , I1IIIii + 'HelixSkins.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , i1111 , 38 , I1IIIii + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 50 - 50: OOOo00oo0oO - ii + iiiiiiii1 % oOo
def IiIIi ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 85 - 85: ooOoO0O00 . ooOoO0O00
def Ii11i1I1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OOI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 59 - 59: ii * ooo0O / O0Oooo0O
def oOooOOoo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iIOoo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 21 - 21: iiiiiiii1 % I11i1ii1 % I1ii11iIi11i % o0o00Oo0O
def OoOoooOO00OO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 76 - 76: oOoO0o00OO0 + OoOo0o % o0o00Oo0O * Ii . o0o00Oo0O . Ii
def oo0OOoOo0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i11iII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 40 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 75 - 75: OoOo0o / Ii / iI11I1II1I1I
def i11iI1111ii1I ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OoOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 5 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 22 - 22: Ii + iii1i1iiiiIi + ii
def iI1iIIIi1i ( ) :
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  I1111ii11 ( )
 if oo000o0000oO == 1 :
  I1iI1I1111i ( )
 if oo000o0000oO == 2 :
  iII11IiIIII ( )
  if 99 - 99: OoOo0o . OoOo0o * oOOoOooOo + IIiIiII11i . iI11I1II1I1I
  if 93 - 93: ooo0O + I11i1ii1 % O0Oooo0O + oOOoOooOo
  if 15 - 15: i1IiiiI1iI - oOoO0o00OO0 * oOOoOooOo
  if 80 - 80: iiiiiiii1 + oOOoOooOo * ooo0O - IIiIiII11i - oOoO0o00OO0
def I1iI1I1111i ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 iI111i = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0O0O0ooo0oOO in iI111i :
  Ii111 ( 'Android Apps' + o0O0O0ooo0oOO , 'https://www.apkfiles.com' + iIIII1iIIii , 30035 , I1IIIii + 'apps.png' )
 for iIIII1iIIii , o0O0O0ooo0oOO in IIi11i1i1iI1 :
  Ii111 ( 'Android Games' + o0O0O0ooo0oOO , 'https://www.apkfiles.com' + iIIII1iIIii , 30035 , I1IIIii + 'GAMES.png' )
 iIiIi11 ( 'movies' , 'MAIN' )
def O0Oo0O0O0o ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  if '/cat' in url :
   Ii111 ( ( o0OOOo ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def iiII11ii1Ii ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  if '/app' in url :
   Ii111 ( ( o0OOOo ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def iiI1Ii1iiii1i ( url ) :
 iiI11Iii = i11111IIIII ( url )
 o0OOOOOo0 = url
 if "page=" in str ( url ) :
  o0OOOOOo0 = url . split ( '?' ) [ 0 ]
 iI111i = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iiI11Iii )
 for url , oOoooooOoO , o0OOOo in iI111i :
  if 'apk' in url :
   O0O0ooOOO ( ( o0OOOo ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOoooooOoO )
 if len ( IIi11i1i1iI1 ) > 1 :
  IIi11i1i1iI1 = str ( IIi11i1i1iI1 [ len ( IIi11i1i1iI1 ) - 1 ] )
 O0O0ooOOO ( 'Next Page' , o0OOOOOo0 + str ( IIi11i1i1iI1 ) , 30037 , I1IIIii + 'Next.png' )
def III1iIi ( name , url ) :
 iiI11Iii = I1I1i ( url )
 name = name
 iI111i = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iiI11Iii )
 for url in iI111i :
  url = 'https://www.apkfiles.com' + url
  IIiIiii ( name , url , 'Brackets' )
def iII11IiIIII ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'https://www.apkfiles.com/search?q=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' ) + '&search_type=1'
 oo0oO0 = oOOo . lower ( )
 iiI1Ii1iiii1i ( oo0oO0 )
 if 71 - 71: ooo0O + OoOo0o . I1ii11iIi11i - iii1i1iiiiIi * Ii . iii1i1iiiiIi
def oo000O0o ( url ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( o00oO , 'Download' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I1iii = os . path . join ( O0oooo00o0Oo , o0OOOo + '.apk' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 2 - 2: I11i1ii1
def OOO0O0O ( url ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I1iii = os . path . join ( O0oooo00o0Oo , o0OOOo + '.mp4' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 5 - 5: iii1i1iiiiIi % IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 if 11 - 11: iiiiiiii1
def i1OooO00oO00o ( name , url , description ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I1iii = os . path . join ( O0oooo00o0Oo , name )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 IIII1iI1IiIiI = xbmc . translatePath ( os . path . join ( I1i1iiI1 ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIII1iI1IiIiI
 print '======================================='
 extract . all ( I1iii , IIII1iI1IiIiI , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 43 - 43: IIiIiII11i
 if 95 - 95: O0Oooo0O + I11i1ii1 * iI11I1II1I1I
 if 17 - 17: oOo - I1ii11iIi11i * o0o00Oo0O / i1iIi
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . i1IiiiI1iI
 if 2 - 2: i1iIi
def I1111ii11 ( ) :
 IIIi1I1IIii1II = i11111IIIII ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iI111i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , iIIII1iIIii , o0o0OO0o00o0O , OoOo00o0OO , Ii1i111iI in iI111i :
  O0O0ooOOO ( o0OOOo , iIIII1iIIii , 80003 , o0o0OO0o00o0O , I1IIIii + 'APKToolsB.png' , Ii1i111iI )
def iII1ii ( apk , ret = None ) :
 if apk == "kodi" :
  OOO00OiI = "https://kodi.tv/download/"
  IIIi1I1IIii1II = i11111IIIII ( OOO00OiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iI111i = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( IIIi1I1IIii1II )
  if len ( iI111i ) == 1 :
   O0o00oO00O0 = iI111i [ 0 ] [ 0 ]
   iI = iI111i [ 0 ] [ 1 ]
   I1Iii = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( O0o00oO00O0 , iI )
  if ret == 'version' : return O0o00oO00O0
  else : return I1Iii
 elif apk == "spmc" :
  IIIi1iIii1II11 = 'https://github.com/koying/SPMC/releases/latest/'
  IIIi1I1IIii1II = i11111IIIII ( IIIi1iIii1II11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iI111i = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( IIIi1I1IIii1II )
  O0o00oO00O0 = re . sub ( '<[^<]+?>' , '' , iI111i [ 0 ] ) . replace ( ' ' , '' )
  I1Iii = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( O0o00oO00O0 , O0o00oO00O0 )
  if ret == 'version' : return O0o00oO00O0
  else : return I1Iii
def IIiIiii ( name , url , Brackets ) :
 if oOOo0O00o ( ) == 'android' :
  OOOOoOOOO = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not OOOOoOOOO : OOOoO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iiIi1 = name
  if OOOOoOOOO :
   if not os . path . exists ( oO ) : os . makedirs ( oO )
   if not IIII ( url ) == True : OOOoO ( oOo0oooo00o , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % iiIi1 , '' , 'Please Wait' )
   I1iii = os . path . join ( oO , "%s.apk" % name )
   try : os . remove ( I1iii )
   except : pass
   downloader . download ( url , I1iii , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   if "Brackets" in Brackets :
    o0II1 = zipfile . ZipFile ( I1iii )
    for file in o0II1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oO , os . path . basename ( file ) ) , 'wb' ) as oOo0oO :
       Oo0OOoI1i1i1IIi1I = file . split ( '/' ) [ 1 ]
       oOo0oO . write ( o0II1 . read ( file ) )
       xbmc . sleep ( 500 )
       oOo0oO . close ( )
       try :
        os . remove ( I1iii )
       except :
        pass
       I1iii = os . path . join ( oO , Oo0OOoI1i1i1IIi1I )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I1iii + '")' )
  else : OOOoO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : OOOoO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 18 - 18: OOOo00oo0oO * i1iIi / ii % iii1i1iiiiIi - ooOoO0O00
 if 49 - 49: ooo0O - iI11I1II1I1I
 if 61 - 61: iiiiiiii1 * oOOoOooOo
 if 1 - 1: O0Oooo0O * iii1i1iiiiIi
def OOooOOOooO0o ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( IIIi1I1IIii1II )
 for iIIII1iIIii , o0OOOo in iI111i :
  iIIII1iIIii = ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + iIIII1iIIii )
  oo000o0O ( ( o0OOOo ) . replace ( '_' , ' ' ) , iIIII1iIIii )
  if 1 - 1: IIiIiII11i - ooOoO0O00 + OOOo00oo0oO
def oo000o0O ( name , url ) :
 if oOOo0O00o ( ) == 'android' :
  OOOOoOOOO = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not OOOOoOOOO : OOOoO ( oOo0oooo00o , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iiIi1 = name
  if OOOOoOOOO :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not IIII ( url ) == True : OOOoO ( oOo0oooo00o , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % iiIi1 , '' , 'Please Wait' )
   I1iii = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( I1iii )
   except : pass
   downloader . download ( url , I1iii , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I1iii + '")' )
  else : OOOoO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : OOOoO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 58 - 58: iiiiiiii1 - ii
 if 56 - 56: iiiiiiii1 / iiiiiiii1
def Ii11iIi1iIiii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 5 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'INFO' )
 if 11 - 11: oOoO0o00OO0 / oOoO0o00OO0
 if 39 - 39: o0o00Oo0O . i1IiiiI1iI
def OO00o ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 30015 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 45 - 45: OOOo00oo0oO + ooo0O + I11i1ii1 / i1iIi + ooo0O
def i1II1I1I1 ( url , iconimage , fanart ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 I111iIIII11iI = url
 oOoooooOoO = iconimage
 fanart = fanart
 iI111i = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for IIi11i1II , o0OOOo in iI111i :
  if '.mp4' in o0OOOo :
   O0O0ooOOO ( 'Watch VIDEO' , url + '/' + IIi11i1II , 222 , oOoooooOoO , fanart , '' )
  if 'description' in o0OOOo :
   O0O0ooOOO ( 'Read Description' , url + '/' + IIi11i1II , 30017 , oOoooooOoO , fanart , '' )
  if 'images' in o0OOOo :
   o00oOOooOOo0o ( 'View Images' , url + '/' + IIi11i1II , 30018 , oOoooooOoO , fanart , '' )
  if 'url' in o0OOOo :
   O0O0ooOOO ( 'Install Build On Android' , url + '/' + IIi11i1II , 30016 , oOoooooOoO , fanart , '' )
  if 'url' in o0OOOo :
   O0O0ooOOO ( 'Install Build On Pc' , url + '/' + IIi11i1II , 30019 , oOoooooOoO , fanart , '' )
 iIiIi11 ( 'movies' , 'INFO' )
 if 21 - 21: ooOoO0O00 + IIiIiII11i
def Ii1i1I1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in iI111i :
  iI11ii ( url )
  if 23 - 23: iii1i1iiiiIi * I11i1ii1 / OOOo00oo0oO
def O0O0o0o0oo0O ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in iI111i :
  I1iiI ( url )
  if 24 - 24: o0o00Oo0O
def O0oO00o0o0oo0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'desc="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for iio00O0o00oo in iI111i :
  OoOoO ( 'Description:' , iio00O0o00oo )
  if 18 - 18: iii1i1iiiiIi
def O0o ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 url = url
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for IIi11i1II , o0OOOo in iI111i :
  if 'png' in o0OOOo :
   O0O0ooOOO ( 'image' , '' , '' , url + '/' + IIi11i1II , url + '/' + IIi11i1II , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 1 - 1: ooo0O % ooo0O . iI11I1II1I1I . ii . I11i1ii1 . iiiiiiii1
def oooo ( name , url , description ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I1iii = os . path . join ( O0oooo00o0Oo , name + '.zip' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0o0O0Ooo0o
 print '======================================='
 extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IioO0oOOO0Ooo ( )
 if 65 - 65: I1ii11iIi11i . iii1i1iiiiIi . OoOo0o % ooo0O + oOo
 if 53 - 53: I1ii11iIi11i * i1IiiiI1iI - i1iIi % oOo - iii1i1iiiiIi - iiiiiiii1
def I1iiI ( url ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1iii = os . path . join ( O0oooo00o0Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0o0O0Ooo0o
 print '======================================='
 extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
 i1Ii11II ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIIIIiI ( )
 if 64 - 64: I11i1ii1
def iI11ii ( url ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1iii = os . path . join ( O0oooo00o0Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0o0O0Ooo0o
 print '======================================='
 extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
 i1Ii11II ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIIIIiI ( )
 if 80 - 80: oOo0O0Ooo - Ii / oOo / iii1i1iiiiIi + iii1i1iiiiIi
def oo000oiIIIII ( name , url , description ) :
 oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 I1iii = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oO0 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oO0o0O0Ooo0o
 print '======================================='
 extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIIIIiI ( )
 if 48 - 48: iii1i1iiiiIi * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def oOOo0O00o ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def IiIIi1 ( log ) :
 xbmc . log ( "[%s]: %s" % ( oOo0oooo00o , log ) )
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : oOo0oO = open ( Oo0o0000o0o0 , 'w' ) ; oOo0oO . close ( )
 with open ( Oo0o0000o0o0 , 'a' ) as oOo0oO :
  IIoooOoOO0o = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oOo0oO . write ( IIoooOoOO0o . rstrip ( '\r\n' ) + '\n' )
def oOo0Oooo ( msg , level = xbmc . LOGDEBUG ) :
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : oOo0oO = open ( Oo0o0000o0o0 , 'w' ) ; oOo0oO . close ( )
 if WIZDEBUGGING == 'false' : return False
 if DEBUGLEVEL == '0' : return False
 if DEBUGLEVEL == '1' and not level in [ xbmc . LOGNOTICE , xbmc . LOGERROR , xbmc . LOGSEVERE , xbmc . LOGFATAL ] : return False
 if DEBUGLEVEL == '2' : level = xbmc . LOGNOTICE
 try :
  if isinstance ( msg , unicode ) :
   msg = '%s' % ( msg . encode ( 'utf-8' ) )
  xbmc . log ( '%s: %s' % ( oOo0oooo00o , msg ) , level )
 except Exception as OoO :
  try : xbmc . log ( 'Logging Failure: %s' % ( OoO ) , level )
  except : pass
 if ENABLEWIZLOG == 'true' :
  Oo00OOO0 = getS ( 'nextcleandate' ) if not getS ( 'nextcleandate' ) == '' else str ( TODAY )
  if CLEANWIZLOG == 'true' and Oo00OOO0 <= str ( TODAY ) : checkLog ( )
  with open ( Oo0o0000o0o0 , 'a' ) as oOo0oO :
   IIoooOoOO0o = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , msg )
   oOo0oO . write ( IIoooOoOO0o . rstrip ( '\r\n' ) + '\n' )
def IiIIIIiI ( ) :
 oo000o0000oO = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oo000o0000oO == 0 : return
 elif oo000o0000oO == 1 : pass
 iI1IIIii = oOOo0O00o ( )
 IiIIi1 ( "Platform: " + str ( iI1IIIii ) )
 os . _exit ( 1 )
 IiIIi1 ( "Force close failed!  Trying alternate methods." )
 if iI1IIIii == 'osx' :
  IiIIi1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iI1IIIii == 'linux' :
  IiIIi1 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iI1IIIii == 'android' :
  IiIIi1 ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.itvmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.itvmc' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.itvmc());' )
  except : pass
  iI111I11I1I1 . ok ( oOo0oooo00o , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif iI1IIIii == 'windows' :
  IiIIi1 ( "############ try windows force close #################" )
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
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  IiIIi1 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  IiIIi1 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 27 - 27: O0Oooo0O
  if 10 - 10: Ii + oOOoOooOo / ii
  if 57 - 57: ii % IIiIiII11i - O0Oooo0O
def oO00oO0 ( url ) :
 o0oO0 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( url ) :
  for file in oo0OOO0OOoOO :
   if file . endswith ( ".xml" ) :
    o0oO0 . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooOO00oOOo000 = open ( ( os . path . join ( Ooo00OoO0O00 , file ) ) ) . read ( )
    iiIiI11IiI1I = ooOO00oOOo000 . replace ( i1111 , 'special://home/' )
    oOo0oO = open ( ( os . path . join ( Ooo00OoO0O00 , file ) ) , mode = 'w' )
    oOo0oO . write ( str ( iiIiI11IiI1I ) )
    oOo0oO . close ( )
 IiIIIIiI ( )
 if 98 - 98: IIiIiII11i * I11i1ii1 - oOo0O0Ooo % ooo0O - iiiiiiii1 % oOoO0o00OO0
def IiiIiiiiI1III ( ) :
 Ii111 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , I1IIIii + 'RadioNomy.png' )
 Ii111 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , I1IIIii + 'RadioNomy.png' )
 Ii111 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , I1IIIii + 'RadioNomy.png' )
 if 69 - 69: ooOoO0O00 % oOo % O0Oooo0O / oOOoOooOo / oOOoOooOo
def Ii1I1i1IiiI ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def IiiiI1i ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def I1iIi1i ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in IIi11i1i1iI1 :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + o0OOOo + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
 for url , oOoooooOoO , o0OOOo in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + o0OOOo + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOoooooOoO )
def I1II1iI ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iiI11Iii )
 for url in iI111i :
  i11IIIiI1I ( url )
def iIii1Ii11I1i ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo
 iI11IIi1iiI1I = 'https://www.radionomy.com/en/search/index?query=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oOOo0 = i11111IIIII ( iI11IIi1iiI1I )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + o0OOOo + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + iIIII1iIIii , 70005 , oOoooooOoO )
  if 83 - 83: I1ii11iIi11i / oOOoOooOo
  if 11 - 11: ooo0O - IIiIiII11i % OOOo00oo0oO . IIiIiII11i
def Oo0O00O ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.listenlive.eu/' + iIIII1iIIii , 10111113 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def i1iI1i11iIi1 ( url ) :
 iiI11Iii = I1I1i ( url )
 if 65 - 65: OOOo00oo0oO . Ii % OoOo0o * iiiiiiii1 % I1ii11iIi11i
 if 51 - 51: oOo % iiiiiiii1
 iI111i = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , Iiiii , url , IiIi1I1IiI1II1 in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' [COLORorangered] ' + IiIi1I1IiI1II1 + '[/COLOR]' , url , 222225 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , '[COLOR' + iiI1IiI + ']' + o0OOOo + '[CR]' + Iiiii + '[CR]' + IiIi1I1IiI1II1 + '[/COLOR]' )
  if 21 - 21: ii . o0o00Oo0O / Ii
def oOOOoo0 ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.toonjet.com/' + iIIII1iIIii , 8051 , I1IIIii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1i11II1i1i ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( iiI11Iii )
 for url , oOoooooOoO in iI111i :
  if 'ol.gif' in oOoooooOoO :
   pass
  elif 'link_block_' in oOoooooOoO :
   pass
  elif '.png' in oOoooooOoO :
   pass
  else :
   Ii111 ( ( oOoooooOoO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , I1IIIii + 'vod.png' )
 for url in IIi11i1i1iI1 :
  Ii111 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , I1IIIii + 'Next.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0O0O00OoO0O ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iiI11Iii )
 for url in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , I1IIIii + 'classictoons.png' )
  if 22 - 22: i1IiiiI1iI - ooo0O
  if 54 - 54: OOOo00oo0oO * oOo - iiiiiiii1 * i1IiiiI1iI + ooo0O - i1iIi
def iI1I11 ( ) :
 iii11III1I ( 'Audio Books' , '' , 30011 , I1IIIii + 'AudioBooks.png' , I1IIIii + 'AudioBooks.png' , '' )
 iii11III1I ( 'Kids Audio Books' , '' , 30006 , I1IIIii + 'KidsAudioBooks.png' , I1IIIii + 'KidsAudioBooks.png' , '' )
 if 92 - 92: oOo0O0Ooo / oOo - OoOo0o / Ii
def IiIi1i11i1II ( ) :
 iii11III1I ( 'All' , '' , 30001 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 iii11III1I ( 'Popular' , '' , 30012 , I1IIIii + 'POPULARv.png' , I1IIIii + 'POPULARv.png' , '' )
 iii11III1I ( 'Search' , '' , 30013 , I1IIIii + 'Search.png' , I1IIIii + 'Search.png' , '' )
 if 51 - 51: OOOo00oo0oO % OOOo00oo0oO / oOOoOooOo . OoOo0o / iI11I1II1I1I / ooOoO0O00
def OOo0o ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for o0OOOo , iIIII1iIIii , Ooo0O0ooo0o in iI111i :
  if 'Parent' in o0OOOo :
   pass
  elif '2' in Ooo0O0ooo0o :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIIII1iIIii , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 55 - 55: oOOoOooOo . I11i1ii1 * ooOoO0O00 . i1iIi
def OoOo00Oo0oo0O ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for o0OOOo , iIIII1iIIii , Ooo0O0ooo0o in iI111i :
  if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
   if '1' in Ooo0O0ooo0o :
    iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIIII1iIIii , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '2' in Ooo0O0ooo0o :
    iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIIII1iIIii , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '3' in Ooo0O0ooo0o :
    iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIIII1iIIii , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 39 - 39: i1IiiiI1iI * O0Oooo0O
    if 63 - 63: oOOoOooOo % oOo0O0Ooo . OoOo0o - oOOoOooOo / I1ii11iIi11i % oOo0O0Ooo
def II1i11i1iI1I ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for o0OOOo , iIIII1iIIii , Ooo0O0ooo0o in iI111i :
  if '1' in Ooo0O0ooo0o :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIIII1iIIii , 3010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '2' in Ooo0O0ooo0o :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIIII1iIIii , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '3' in Ooo0O0ooo0o :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIIII1iIIii , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 78 - 78: ii - iii1i1iiiiIi . Ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: OOOo00oo0oO * iiiiiiii1 + I11i1ii1 * iiiiiiii1 . oOoO0o00OO0 - iI11I1II1I1I
def i1IIi1ii1i1ii ( url ) :
 IIi11i1II = url
 oOOo0 = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOOo0 )
 for url , o0OOOo in IIi11i1i1iI1 :
  if 'mp3' in o0OOOo :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IIi11i1II + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in o0OOOo :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IIi11i1II + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in o0OOOo :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IIi11i1II + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '/' in o0OOOo :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIi11i1II + url , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 97 - 97: IIiIiII11i
   if 38 - 38: oOo0O0Ooo
   if 42 - 42: ooo0O
def ii1i1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIi11i1II = url
 iI111i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  if 'Parent' in o0OOOo :
   pass
  elif '.db' in o0OOOo :
   pass
  elif '.jpg' in o0OOOo :
   pass
  elif '.html' in o0OOOo :
   pass
  elif '.doc' in o0OOOo :
   pass
  elif 'mp3' in o0OOOo :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIi11i1II + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in o0OOOo :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIi11i1II + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIi11i1II + url , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: I11i1ii1 - o0o00Oo0O + oOo0O0Ooo / ii * iiiiiiii1 / ooOoO0O00
   if 28 - 28: ooo0O - iiiiiiii1 * oOoO0o00OO0 - IIiIiII11i % IIiIiII11i - I11i1ii1
def oOOooo0OoOOOO ( ) :
 iii11III1I ( 'A-Z' , '' , 30007 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 iii11III1I ( 'All' , '' , 30003 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 iii11III1I ( 'Search' , '' , 30014 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 if 27 - 27: i1iIi - ii . oOoO0o00OO0 - I11i1ii1
def o0o0OoOo00oOoo0oO ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO in iI111i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iIIII1iIIii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOoooooOoO :
   pass
  else :
   iii11III1I ( oOoooooOoO , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iIIII1iIIii ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOoooooOoO + '.gif' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: O0Oooo0O - ooOoO0O00 / I11i1ii1
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: iii1i1iiiiIi - oOo * ii
 if 26 - 26: ii
def ooo0000oo0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  if '</a>' in o0OOOo :
   pass
  elif '(' in o0OOOo :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 58 - 58: iiiiiiii1 % iI11I1II1I1I . iI11I1II1I1I / i1IiiiI1iI
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: oOo / OoOo0o - ooOoO0O00 + ooOoO0O00 - I11i1ii1 + I11i1ii1
def oOoOo000Ooooo ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
   if '</a>' in o0OOOo :
    pass
   elif '(' in o0OOOo :
    iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIIII1iIIii , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   else :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIIII1iIIii , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 18 - 18: i1iIi + iii1i1iiiiIi . ooOoO0O00 / I11i1ii1 / iiiiiiii1
    if 97 - 97: oOo + iI11I1II1I1I
def O0OOoo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if '</a>' in o0OOOo :
   pass
  elif '(' in o0OOOo :
   iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIIII1iIIii , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIIII1iIIii , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 38 - 38: I11i1ii1 . ooo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: oOOoOooOo . I11i1ii1 . IIiIiII11i
 if 25 - 25: I11i1ii1 * O0Oooo0O - OOOo00oo0oO * Ii * oOo0O0Ooo * OoOo0o
def Ooii1II11IIII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oOOo0 )
 for url in iI111i :
  IIi11i1II = ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( IIi11i1II )
  if 90 - 90: I1ii11iIi11i * i1iIi
def oO0o0o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url in iI111i :
  if '<p align' in o0OOOo :
   pass
  elif '&nbsp;' in o0OOOo :
   pass
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 21 - 21: o0o00Oo0O * oOOoOooOo % oOo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: o0o00Oo0O / O0Oooo0O / oOOoOooOo + I11i1ii1 - I11i1ii1
 if 10 - 10: o0o00Oo0O - oOoO0o00OO0 / O0Oooo0O % iii1i1iiiiIi / ii / i1iIi
def O000oOo ( ) :
 oOOo0 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 iI111i = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'ongoing' in iIIII1iIIii :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 21005 , I1IIIii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in iIIII1iIIii :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 21005 , I1IIIii + 'CartoonShows.png' , '' , '' )
  if 'disney' in iIIII1iIIii :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 21005 , I1IIIii + 'Disney.png' , '' , '' )
  if 'genre' in iIIII1iIIii :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 21005 , I1IIIii + 'Genre.png' , '' , '' )
  if 'years' in iIIII1iIIii :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 21005 , I1IIIii + 'Years.png' , '' , '' )
def o00Oo00O0o ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 o00o = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOoooooOoO , oOoooooOoO , o0OOOo )
 for url , o0OOOo in o00o :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in next :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , I1IIIii + 'Next.png' , '' , '' )
def ooooOOoO000O0 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 o0000o0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 oooo0O = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oOOo0 )
 iII11OO0OoO0OOoOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in oooo0O :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url , o0OOOo in o0000o0Oo :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
def oO000 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
  if 20 - 20: iii1i1iiiiIi % o0o00Oo0O
def Oo0OOO00oo0 ( ) :
 oOOo0 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 iI111i = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if '9cart' in iIIII1iIIii :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 20001 , I1IIIii + 'ORIGINCARTOON.png' )
   if 80 - 80: I11i1ii1 . ooo0O
def IIiIiI1i11iiII ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oOOo0 )
 Ii1II1I11i1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if '9cart' in url :
   Ii111 ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url in IIi11i1i1iI1 :
  if '9cart' in url :
   Ii111 ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url , o0OOOo in Ii1II1I11i1 :
  if '9cart' in url :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
   if 64 - 64: i1iIi
def IIiiiIi1ii11I ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 20003 , oOoooooOoO )
 for url , o0OOOo in IIi11i1i1iI1 :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
  if 9 - 9: o0o00Oo0O * i1iIi
def o0O00o00Ooo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)">' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'Watch' in url :
   Ii111 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , I1IIIii + 'ORIGINCARTOON.png' )
   if 16 - 16: OoOo0o . IIiIiII11i - i1iIi - ii
def ooOoOoOoo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 20005 , I1IIIii + 'ORIGINCARTOON.png' )
  if 25 - 25: I1ii11iIi11i + ooo0O - oOo
def oooI11Ii1 ( url ) :
 url = cloudflare . source ( url )
 O00o0o ( url )
 if 63 - 63: ooOoO0O00
def II1iII11 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . recompile ( 'src="([^"]*)"' )
 for url in iI111i :
  O00o0o ( url )
  if 19 - 19: IIiIiII11i
  if 5 - 5: I1ii11iIi11i
def oOoOo0o0 ( url , name ) :
 url = url ; name = name
 II1Iiiii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 II1Iiiii . clear ( )
 OoO00 = [ ]
 iI1IOo0o = [ ]
 OO0ooo0o0 = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0ooo0o0 )
 for oOoooooOoO in IIi11i1i1iI1 :
  O0OO0 = oOoooooOoO
 Ii1II1I11i1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OO0ooo0o0 )
 for OOI1i11i , iiiI1I in Ii1II1I11i1 :
  OoO00 . append ( [ OOI1i11i , iiiI1I ] )
  if len ( OoO00 ) == len ( Ii1II1I11i1 ) :
   for II1I in OoO00 :
    OOOOo0o0O0 = random . randint ( 1 , len ( OoO00 ) )
    try :
     I1I1i1 = OoO00 [ int ( OOOOo0o0O0 ) ]
     if I1I1i1 [ 1 ] not in iI1IOo0o :
      iI1IOo0o . append ( I1I1i1 [ 1 ] )
      III1I11i1iIi = i11111IIIII ( I1I1i1 [ 0 ] )
      iIiiii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( III1I11i1iIi )
      for Ii1Ii , iII in iIiiii :
       if 'easy' in iII :
        OOoOOooO = i11111IIIII ( iII )
        O0000OOO0 = re . compile ( 'file: "(.+?)"' ) . findall ( OOoOOooO )
        for i1111II1iIII in O0000OOO0 :
         if 'http' in i1111II1iIII :
          o0OoOo00ooO = xbmcgui . ListItem ( I1I1i1 [ 1 ] , iconImage = O0OO0 , thumbnailImage = O0OO0 )
          o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : I1I1i1 [ 1 ] } )
          o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
          II1Iiiii . add ( i1111II1iIII , o0OoOo00ooO )
          xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOo00ooO )
         else :
          pass
       else :
        pass
     else :
      pass
    except :
     pass
  else :
   pass
   if 41 - 41: I11i1ii1 * ii . oOOoOooOo % Ii
def IiIoO0oo0 ( url ) :
 II1Iiiii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 II1Iiiii . clear ( )
 IiIiI1 = [ ]
 iiiI1 = [ ]
 III1Oo00OO = [ ]
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  iiiI1 . append ( [ url , o0OOOo ] )
  if len ( iiiI1 ) == len ( iI111i ) :
   for II1I in iiiI1 :
    iIi111 = random . randint ( 1 , len ( iiiI1 ) )
    try :
     I11I1I = iiiI1 [ int ( iIi111 ) ]
    except :
     pass
    if I11I1I [ 1 ] not in III1Oo00OO :
     III1Oo00OO . append ( I11I1I [ 1 ] )
     if int ( len ( IiIiI1 ) ) < 1 :
      IiIiI1 . append ( I11I1I [ 1 ] [ 0 ] )
      oOoOo0o0 ( I11I1I [ 0 ] , I11I1I [ 1 ] )
     else :
      pass
    else :
     pass
  else :
   pass
   if 50 - 50: i1iIi + OoOo0o . iI11I1II1I1I
def IiIiI1i1ii ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 Ii1I1I1i11ii = sys . argv [ 0 ]
 Ii1I1I1i11ii += '?mode=' + str ( mode )
 Ii1I1I1i11ii += '&title=' + urllib . quote_plus ( name )
 Ii1I1I1i11ii += '&image=' + urllib . quote_plus ( image )
 Ii1I1I1i11ii += '&page=' + str ( page )
 if url != '' :
  Ii1I1I1i11ii += '&url=' + urllib . quote_plus ( url )
 if keyword :
  Ii1I1I1i11ii += '&keyword=' + urllib . quote_plus ( keyword )
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  o0OoOo00ooO . addContextMenuItems ( contextMenu )
 if infoLabels :
  o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
 o0OoOo00ooO . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = isFolder )
 if 46 - 46: o0o00Oo0O % ii
def I1IiII ( ) :
 o0O00o0o = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 iiI11Iii = i11111IIIII ( o0O00o0o )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  IiIiI1i1ii ( o0OOOo , 9110012 , url = iIIII1iIIii , image = O0O , isFolder = False )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 31 - 31: oOOoOooOo % oOo0O0Ooo % I11i1ii1 / O0Oooo0O
def iii11i1 ( ) :
 o0O00o0o = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , '' , 10004 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 ii1iIi1iIiI1i ( '[COLOR' + iiI1IiI + ']24/7 Select Cartoon[/COLOR]' , '' , 9110011 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' , '' )
 IiIiI1i1ii ( '[COLOR' + iiI1IiI + ']24/7 Random Cartoon[/COLOR]' , 9110010 , url = o0O00o0o , image = I1IIIii + 'Kids.png' , isFolder = False )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 if 74 - 74: ooOoO0O00 + OOOo00oo0oO - iI11I1II1I1I . I1ii11iIi11i
def IIII11Ii1I11I ( ) :
 o0O00o0o = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 oOOo0 = i11111IIIII ( o0O00o0o )
 if 70 - 70: iiiiiiii1
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oOOo0 )
 if 51 - 51: o0o00Oo0O - oOoO0o00OO0 / i1IiiiI1iI * IIiIiII11i + oOo % oOoO0o00OO0
 for iIIII1iIIii , o0OOOo in iI111i :
  if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
   if 'Dad!' in o0OOOo :
    pass
   elif 'Family Guy' in o0OOOo :
    pass
   elif '2 Stupid' in o0OOOo :
    pass
   elif 'The Zelfs' in o0OOOo :
    pass
   elif 'A Clone' in o0OOOo :
    pass
   elif 'A.T.O.M' in o0OOOo :
    pass
   elif 'Almost Naked' in o0OOOo :
    pass
   elif 'Angry Kid' in o0OOOo :
    pass
   elif 'Annoying Orange' in o0OOOo :
    pass
   elif 'Aqua Teen' in o0OOOo :
    pass
   elif 'Assy Mcgee' in o0OOOo :
    pass
   elif 'Astroblast' in o0OOOo :
    pass
   elif 'Atomic Betty' in o0OOOo :
    pass
   elif 'Axe Cop' in o0OOOo :
    pass
   elif 'Baby Playpen' in o0OOOo :
    pass
   elif 'Beavis and Butt' in o0OOOo :
    pass
   elif 'Celebrity Deathmatch' in o0OOOo :
    pass
   elif 'Clerks The' in o0OOOo :
    pass
   elif 'Crapston Villas' in o0OOOo :
    pass
   elif 'Duckman:' in o0OOOo :
    pass
   elif 'Stripperella' in o0OOOo :
    pass
   elif 'Vixen' in o0OOOo :
    pass
   else :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 10006 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
    if 58 - 58: OOOo00oo0oO + I11i1ii1 % iiiiiiii1 - i1iIi - OoOo0o % i1iIi
    if 86 - 86: ooo0O
    if 15 - 15: OOOo00oo0oO - iI11I1II1I1I - IIiIiII11i - I11i1ii1 % oOoO0o00OO0
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 80 - 80: I11i1ii1 * iiiiiiii1 . ooOoO0O00 % i1iIi % oOoO0o00OO0 + oOOoOooOo
def IIII1IiiI ( url ) :
 o0O00o0o = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 iiI11Iii = i11111IIIII ( o0O00o0o )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  if 'Dad!' in o0OOOo :
   pass
  elif 'Family Guy' in o0OOOo :
   pass
  elif '2 Stupid' in o0OOOo :
   pass
  elif 'The Zelfs' in o0OOOo :
   pass
  elif 'A Clone' in o0OOOo :
   pass
  elif 'A.T.O.M' in o0OOOo :
   pass
  elif 'Almost Naked' in o0OOOo :
   pass
  elif 'Angry Kid' in o0OOOo :
   pass
  elif 'Annoying Orange' in o0OOOo :
   pass
  elif 'Aqua Teen' in o0OOOo :
   pass
  elif 'Assy Mcgee' in o0OOOo :
   pass
  elif 'Astroblast' in o0OOOo :
   pass
  elif 'Atomic Betty' in o0OOOo :
   pass
  elif 'Axe Cop' in o0OOOo :
   pass
  elif 'Baby Playpen' in o0OOOo :
   pass
  elif 'Beavis and Butt' in o0OOOo :
   pass
  elif 'Celebrity Deathmatch' in o0OOOo :
   pass
  elif 'Clerks The' in o0OOOo :
   pass
  elif 'Crapston Villas' in o0OOOo :
   pass
  elif 'Duckman:' in o0OOOo :
   pass
  elif 'Stripperella' in o0OOOo :
   pass
  elif 'Vixen' in o0OOOo :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 10006 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: oOo0O0Ooo - OoOo0o
def OOOOo0ooOOO0 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iiI11Iii )
 for oOoooooOoO in IIi11i1i1iI1 :
  O0OO0 = oOoooooOoO
 Ii1II1I11i1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iiI11Iii )
 for url in Ii1II1I11i1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 10007 , O0OO0 )
  if 91 - 91: Ii + i1iIi % i1iIi + ooo0O
  if 15 - 15: oOoO0o00OO0 . oOo0O0Ooo - O0Oooo0O - ooOoO0O00
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: iiiiiiii1 . i1iIi * oOo0O0Ooo % O0Oooo0O + iI11I1II1I1I
def OoO00o ( url , IMAGE ) :
 Oo0o0OO0O0o = [ ]
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iiI11Iii )
 for o0OOOo , IIi11i1II in iI111i :
  if 'panda' in IIi11i1II :
   oOOo0 = i11111IIIII ( IIi11i1II )
   IIi11i1i1iI1 = re . compile ( "url: '(.+?)'" ) . findall ( oOOo0 )
   for Ii1I1 in IIi11i1i1iI1 :
    if 'http' in Ii1I1 :
     Oo0o0OO0O0o . append ( { 'source' : 'playpanda' , 'quality' : 'SD' , 'url' : Ii1I1 } )
  elif 'easy' in IIi11i1II :
   oo00O00oO = i11111IIIII ( IIi11i1II )
   Ii1II1I11i1 = re . compile ( 'file: "(.+?)"' ) . findall ( oo00O00oO )
   for Ii1I1 in Ii1II1I11i1 :
    if 'http' in Ii1I1 :
     Oo0o0OO0O0o . append ( { 'source' : 'easyvideo' , 'quality' : 'SD' , 'url' : Ii1I1 } )
  elif 'zoo' in IIi11i1II :
   iIiIIIi = i11111IIIII ( IIi11i1II )
   iIiiii = re . compile ( 'src: "(.+?)"' ) . findall ( iIiIIIi )
   for Ii1I1 in iIiiii :
    if 'http' in Ii1I1 :
     Oo0o0OO0O0o . append ( { 'source' : 'videozoo' , 'quality' : 'SD' , 'url' : Ii1I1 } )
 if len ( Oo0o0OO0O0o ) >= 3 :
  oo000o0000oO = iI111I11I1I1 . select ( 'Select Playlink' ,
 [ IIIi1I1IIii1II [ "source" ] + " - " + " (" + IIIi1I1IIii1II [ "quality" ] + ")"
 for IIIi1I1IIii1II in Oo0o0OO0O0o ] )
  if oo000o0000oO != - 1 :
   url = Oo0o0OO0O0o [ oo000o0000oO ] [ 'url' ]
   oooOO0 = False
   xbmc . Player ( ) . play ( url )
   if 38 - 38: OOOo00oo0oO
   if 9 - 9: i1IiiiI1iI . oOo . OOOo00oo0oO / ii
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
def iii1IiI ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( iiI11Iii )
 for url in iI111i :
  i11IIIiI1I ( url )
  if 87 - 87: oOo0O0Ooo - o0o00Oo0O - i1IiiiI1iI * O0Oooo0O % O0Oooo0O
  if 99 - 99: o0o00Oo0O * Ii % OoOo0o * IIiIiII11i
  if 98 - 98: o0o00Oo0O + iI11I1II1I1I
def oo0OO0Oo000oo ( ) :
 if 38 - 38: iiiiiiii1 + oOOoOooOo
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , I1IIIii + 'StandUp.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , I1IIIii + 'SearchComedian.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , I1IIIii + 'Others.png' , Oo00OOOOO , '' )
 if 32 - 32: oOOoOooOo - ii + oOo
def OO0oO ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  if 'elete' in o0OOOo :
   pass
  else :
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 222 , oOoooooOoO )
   if 5 - 5: Ii / oOo % o0o00Oo0O / OoOo0o + I1ii11iIi11i % ooo0O
def OOO0o0O00O ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , O0OoO00 , i1iII1IiiIiI1 in oO0o :
  for IiIi1oo00ooOoo in O0OoO00 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   Oo0ooo00o0O0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iIIII1iIIii , o0OOOo in Oo0ooo00o0O0 :
    if 'tube' in iIIII1iIIii :
     pass
    elif 'stage' in iIIII1iIIii :
     I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + O0OoO00 + '   -   ' + o0OOOo + '[/COLOR]' , ( iIIII1iIIii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOoooooOoO , )
    elif 'vee' in iIIII1iIIii :
     pass
     if 43 - 43: iii1i1iiiiIi * oOo % ooOoO0O00 * i1iIi + iI11I1II1I1I
def oOIIii ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , O0OoO00 , i1iII1IiiIiI1 in oO0o :
  Oo0ooo00o0O0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iIIII1iIIii , o0OOOo in Oo0ooo00o0O0 :
   if 'tube' in iIIII1iIIii :
    pass
   elif 'stage' in iIIII1iIIii :
    I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + O0OoO00 + '   -   ' + o0OOOo + '[/COLOR]' , ( iIIII1iIIii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOoooooOoO )
   elif 'vee' in iIIII1iIIii :
    pass
    if 100 - 100: Ii - oOOoOooOo + OoOo0o * ii + o0o00Oo0O
    if 66 - 66: oOoO0o00OO0 . I1ii11iIi11i / oOoO0o00OO0 + oOoO0o00OO0 . IIiIiII11i % oOo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: Ii - ii
def iI1i1II ( url ) :
 oOOo0 = i11111IIIII ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1ii1ii1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOo0 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1ii1ii1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1ii1ii1I :
  I1iiIiiii1111 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 90 - 90: oOo0O0Ooo
  if 4 - 4: OoOo0o % oOOoOooOo - OoOo0o - ooo0O
  if 30 - 30: I11i1ii1
  if 34 - 34: OOOo00oo0oO - IIiIiII11i - ooo0O + iiiiiiii1 + O0Oooo0O
  if 70 - 70: ii + oOo * I1ii11iIi11i
  if 20 - 20: Ii - IIiIiII11i - oOOoOooOo % OOOo00oo0oO . oOOoOooOo
  if 50 - 50: iI11I1II1I1I + O0Oooo0O - i1IiiiI1iI - ii
def IIiI1Ii ( ) :
 if 84 - 84: iii1i1iiiiIi - i1IiiiI1iI
 OoO00O00O0 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 OoO00O00O0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 76 - 76: oOo0O0Ooo % Ii + OoOo0o
 iIiIi11 ( 'movies' , 'MAIN' )
 if 17 - 17: i1IiiiI1iI / IIiIiII11i * ooo0O / I1ii11iIi11i + iiiiiiii1 . OOOo00oo0oO
def i11111i1I1IiI ( ) :
 OoO00O00O0 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 OoO00O00O0 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 27 - 27: ii * i1IiiiI1iI % ii * I1ii11iIi11i * oOOoOooOo
 iIiIi11 ( 'movies' , 'MAIN' )
def I1IIo0o0OoOO00Oo ( ) :
 if 33 - 33: iiiiiiii1 % ii / OOOo00oo0oO
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 Oooooooo00o00 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 12 - 12: oOoO0o00OO0 - iI11I1II1I1I * iii1i1iiiiIi + ooo0O . i1IiiiI1iI
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + '/Movies/a.to.z/' + III1II1i + '.php'
  oOOo0 = i1Oo00 ( iI1i1IiIIIIi )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in iI111i :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    if '.php' in iIIII1iIIii :
     o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
     o00oOOooOOo0o ( o0OOOo , iIIII1iIIii , 426 , II11IiiIII , I11Iii1 , oOOOO )
    else :
     o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
     o0iIiii ( o0OOOo , iIIII1iIIii , 222 , II11IiiIII , I11Iii1 , oOOOO )
     if 73 - 73: iiiiiiii1 * iiiiiiii1 + ooo0O
     iIiIi11 ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 24 - 24: Ii * IIiIiII11i * iiiiiiii1
def O00iI1iIIi ( ) :
 if 74 - 74: iii1i1iiiiIi
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 Oooooooo00o00 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 28 - 28: iiiiiiii1
 for III1II1i in Oooooooo00o00 :
  Oooo00i1I1I = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + III1II1i + '.php'
  oOOo0 = i1Oo00 ( Oooo00i1I1I )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
  for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in iI111i :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    if '.php' in iIIII1iIIii :
     o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
     o00oOOooOOo0o ( o0OOOo , iIIII1iIIii , 426 , II11IiiIII , I11Iii1 , oOOOO )
    else :
     o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
     o0iIiii ( o0OOOo , iIIII1iIIii , 222 , II11IiiIII , I11Iii1 , oOOOO )
     if 45 - 45: iii1i1iiiiIi / oOo0O0Ooo
     iIiIi11 ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 34 - 34: ooo0O % oOoO0o00OO0 + i1iIi * i1IiiiI1iI / OOOo00oo0oO
     if 18 - 18: oOOoOooOo
def OOoo00o0OoO ( ) :
 if 24 - 24: I11i1ii1 . iiiiiiii1 * I11i1ii1 % Ii . Ii + ooOoO0O00
 iiI11Iii = i11111IIIII ( Ii1iIiII1ii1 + 'spongemain.php' )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , oOOOO , iIIII1iIIii , oOoooooOoO , OoOo00o0OO , Ii1IIi in iI111i :
  OoO00O00O0 ( o0OOOo , iIIII1iIIii , Ii1IIi , oOoooooOoO , OoOo00o0OO , oOOOO )
  iIiIi11 ( 'movies' , 'MAIN' )
def Ooo0o0OO00oOO ( url ) :
 if 45 - 45: iI11I1II1I1I - I1ii11iIi11i . i1IiiiI1iI - I1ii11iIi11i / oOOoOooOo / ooo0O
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o00oooo0 = ( '%s%s' % ( o0O00o0o , url ) )
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in iI111i :
  if '.php' in url :
   OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for II1I in OooOooO0O0o0 :
    if II1I == url :
     o0OOOo = ( '[COLORred]Watched - [/COLOR]' + o0OOOo ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   o00oOOooOOo0o ( o0OOOo , url , 426 , II11IiiIII , I11Iii1 , oOOOO )
  else :
   OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for II1I in OooOooO0O0o0 :
    if II1I == url :
     o0OOOo = ( '[COLORred]Watched - [/COLOR]' + o0OOOo ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   o0iIiii ( o0OOOo , url , 222 , II11IiiIII , I11Iii1 , oOOOO )
   if 1 - 1: I1ii11iIi11i . Ii
   iIiIi11 ( 'movies' , 'MAIN' )
   if 9 - 9: ii / i1IiiiI1iI
   xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 47 - 47: ii
   if 48 - 48: iii1i1iiiiIi . I11i1ii1 % oOo0O0Ooo + i1IiiiI1iI
def II11iII ( url ) :
 if 78 - 78: I11i1ii1 + i1IiiiI1iI - ooo0O + oOo / iI11I1II1I1I
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , oOOOO , url , oOoooooOoO , OoOo00o0OO , Ii1IIi in iI111i :
  OoO00O00O0 ( o0OOOo , url , Ii1IIi , oOoooooOoO , OoOo00o0OO , oOOOO )
  if 47 - 47: OoOo0o
  iIiIi11 ( 'movies' , 'MAIN' )
  if 20 - 20: O0Oooo0O % oOOoOooOo - O0Oooo0O * ii / oOoO0o00OO0
  if 57 - 57: I11i1ii1 % i1IiiiI1iI * OoOo0o % oOoO0o00OO0
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: ooOoO0O00 - ii
def o0iIiii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 66 - 66: oOoO0o00OO0 / ooOoO0O00 * oOo0O0Ooo - iii1i1iiiiIi + OOOo00oo0oO
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1I11i = [ ]
  ii1I11i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   ii1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOo00ooO . addContextMenuItems ( ii1I11i )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = False )
 return OoOo0oO0o
 if 74 - 74: iiiiiiii1 / O0Oooo0O / IIiIiII11i - iiiiiiii1 / OOOo00oo0oO % i1IiiiI1iI
def OoO00O00O0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 19 - 19: I11i1ii1 % ii + ii
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1I11i = [ ]
  ii1I11i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   ii1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOo00ooO . addContextMenuItems ( ii1I11i )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = True )
 return OoOo0oO0o
if 7 - 7: ooOoO0O00
if 91 - 91: iii1i1iiiiIi - iii1i1iiiiIi . I11i1ii1
if 33 - 33: O0Oooo0O - iI11I1II1I1I / i1iIi % o0o00Oo0O
if 80 - 80: I11i1ii1 % ii - I11i1ii1
if 27 - 27: O0Oooo0O - ooo0O * oOoO0o00OO0 - oOo0O0Ooo
if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - iiiiiiii1 . i1iIi
if 100 - 100: IIiIiII11i / O0Oooo0O / iiiiiiii1 - oOoO0o00OO0 * iI11I1II1I1I
if 7 - 7: ooOoO0O00 . I11i1ii1 % Ii * oOoO0o00OO0 . i1IiiiI1iI % oOoO0o00OO0
if 35 - 35: oOo0O0Ooo
if 48 - 48: ii % ii - oOo . iii1i1iiiiIi
if 22 - 22: oOOoOooOo . Ii . ii . ooOoO0O00
if 12 - 12: iii1i1iiiiIi % OoOo0o + OOOo00oo0oO . o0o00Oo0O % iI11I1II1I1I
if 41 - 41: ii
if 13 - 13: i1IiiiI1iI + O0Oooo0O - O0Oooo0O % OOOo00oo0oO / i1IiiiI1iI
if 4 - 4: oOo0O0Ooo + OoOo0o - I11i1ii1 + iiiiiiii1
def oooo00OoOoO ( string ) :
 if O00O0oOO00O00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 99 - 99: IIiIiII11i
def I1I111i1I ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oOo0Ooo0oo = [ ]
 try :
  if 43 - 43: I1ii11iIi11i / O0Oooo0O / ooOoO0O00
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( oo0OooOOo0 ) == False :
  oooo00OoOoO ( 'Making Favorites File' )
  oOo0Ooo0oo . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ooOO00oOOo000 = open ( oo0OooOOo0 , "w" )
  ooOO00oOOo000 . write ( json . dumps ( oOo0Ooo0oo ) )
  ooOO00oOOo000 . close ( )
 else :
  oooo00OoOoO ( 'Appending Favorites' )
  ooOO00oOOo000 = open ( oo0OooOOo0 ) . read ( )
  I1i11IIiiIiI = json . loads ( ooOO00oOOo000 )
  I1i11IIiiIiI . append ( ( name , url , iconimage , fanart , mode ) )
  iiIiI11IiI1I = open ( oo0OooOOo0 , "w" )
  iiIiI11IiI1I . write ( json . dumps ( I1i11IIiiIiI ) )
  iiIiI11IiI1I . close ( )
  if 7 - 7: oOo * Ii * iI11I1II1I1I / OoOo0o / O0Oooo0O
  if 35 - 35: iiiiiiii1 * OoOo0o
def ooooO0OO0O ( ) :
 if os . path . exists ( oo0OooOOo0 ) == False :
  oOo0Ooo0oo = [ ]
  oooo00OoOoO ( 'Making Favorites File' )
  oOo0Ooo0oo . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  ooOO00oOOo000 = open ( oo0OooOOo0 , "w" )
  ooOO00oOOo000 . write ( json . dumps ( oOo0Ooo0oo ) )
  ooOO00oOOo000 . close ( )
 else :
  IiI11 = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
  O000OOO000o = len ( IiI11 )
  for iiIi in IiI11 :
   o0OOOo = iiIi [ 0 ]
   iIIII1iIIii = iiIi [ 1 ]
   II11IiiIII = iiIi [ 2 ]
   try :
    ooO00Oo = iiIi [ 3 ]
    if ooO00Oo == None :
     raise
   except :
    if O0oo0OO0 . getSetting ( 'use_thumb' ) == "true" :
     ooO00Oo = II11IiiIII
    else :
     ooO00Oo = OoOo00o0OO
   try : IIiI1iiIII1 = iiIi [ 5 ]
   except : IIiI1iiIII1 = None
   try : oo0OooOoOo = iiIi [ 6 ]
   except : oo0OooOoOo = None
   if 8 - 8: I11i1ii1
   if iiIi [ 4 ] == 0 :
    o00oOOooOOo0o ( o0OOOo , iIIII1iIIii , '' , II11IiiIII , OoOo00o0OO , '' , 'fav' )
   else :
    o00oOOooOOo0o ( o0OOOo , iIIII1iIIii , iiIi [ 4 ] , II11IiiIII , OoOo00o0OO , '' , 'fav' )
    if 37 - 37: oOo0O0Ooo / ii % Ii % oOoO0o00OO0
def IIIIiiii ( name ) :
 I1i11IIiiIiI = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
 for ii111i1iI in range ( len ( I1i11IIiiIiI ) ) :
  if I1i11IIiiIiI [ ii111i1iI ] [ 0 ] == name :
   del I1i11IIiiIiI [ ii111i1iI ]
   iiIiI11IiI1I = open ( oo0OooOOo0 , "w" )
   iiIiI11IiI1I . write ( json . dumps ( I1i11IIiiIiI ) )
   iiIiI11IiI1I . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 20 - 20: ooOoO0O00 * iiiiiiii1 + oOo * oOo / I1ii11iIi11i
 if 83 - 83: oOoO0o00OO0
def ooOO ( ) :
 OOo0OOooO0 = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 oOoooOOO0 = open ( OOo0OOooO0 , "w+" )
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oOOo0 )
 oOoooOOO0 . write ( r'[' + o0OOO + ']' + '\n' )
 for o0OOOo , oOoooooOoO , oO000oOo00o0o , iIIII1iIIii in iI111i :
  iIIII1iIIii = ( iIIII1iIIii + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I1Iiii1i1iI = ( o0OOOo + '=plugin://' + o0OOO + '/?url=' + iIIII1iIIii + '&mode=10012&name=' + ( o0OOOo ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOoooooOoO ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOoooooOoO ) . replace ( ' ' , '' ) + '+&amp;description=' )
  oOoooOOO0 . write ( I1Iiii1i1iI + '\n' )
  if 51 - 51: iiiiiiii1 / O0Oooo0O % OOOo00oo0oO + OOOo00oo0oO * OOOo00oo0oO
  if 20 - 20: iiiiiiii1 % oOoO0o00OO0 + oOo / I1ii11iIi11i
def iiIii ( ) :
 iiI11Iii = cloudflare . source ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 iI111i = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii in iI111i :
  Ii111 ( '24/7' , iIIII1iIIii , 90021 , I1IIIii + '247Streams.png' )
  if 18 - 18: i1IiiiI1iI / oOOoOooOo
def O00Oo00o ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  O0O0ooOOO ( o0OOOo , ( iIIII1iIIii ) . strip ( ) , 222 , I1IIIii + '247Streams.png' , I1IIIii + '247Streams.png' , '' )
def II111111 ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  O0O0ooOOO ( o0OOOo , ( iIIII1iIIii ) . strip ( ) , 222 , I1IIIii + 'musicch.png' , I1IIIii + 'musicch.png' , '' )
def o0OO0o0o00o ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  O0O0ooOOO ( o0OOOo , ( iIIII1iIIii ) . strip ( ) , 222 , I1IIIii + 'NEWS.png' , I1IIIii + 'NEWS.png' , '' )
def II1 ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  O0O0ooOOO ( o0OOOo , ( iIIII1iIIii ) . strip ( ) , 222 , I1IIIii + 'adult.png' , I1IIIii + 'adult.png' , '' )
def IiII1Iiii ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 iI111i = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  O0O0ooOOO ( o0OOOo , iIIII1iIIii , 1016 , I1IIIii + 'TUTS.png' , I1IIIii + 'TUTS.png' , '' )
  if 16 - 16: iiiiiiii1 . o0o00Oo0O - O0Oooo0O * O0Oooo0O
  if 80 - 80: i1iIi % oOoO0o00OO0
def OOoo000OO00 ( ) :
 if 51 - 51: oOOoOooOo * I11i1ii1 * iI11I1II1I1I / iii1i1iiiiIi % I11i1ii1
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 if 36 - 36: oOoO0o00OO0 * ooo0O + Ii + ii
def oOi1IiIiIii11I ( ) :
 if 80 - 80: O0Oooo0O + i1IiiiI1iI . O0Oooo0O + OoOo0o
 iiI11Iii = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , oOoooooOoO , o0OOOo , o0Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo + '  -  ' + ( o0Oo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIIII1iIIii , 10023 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
  if 85 - 85: Ii . i1IiiiI1iI + i1iIi / i1iIi
  if 43 - 43: I11i1ii1 . ii - IIiIiII11i
  if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + oOoO0o00OO0 * OoOo0o * OOOo00oo0oO
def I11iIIiiIiIi ( ) :
 if 7 - 7: oOoO0o00OO0
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Action[/COLOR]' , 'Aksiyon' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Adventure[/COLOR]' , 'Macera' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Animation[/COLOR]' , 'Animasyon' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Anime[/COLOR]' , 'Anime' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Biography[/COLOR]' , 'Biyografi' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Comedy[/COLOR]' , 'Komedi' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Drama[/COLOR]' , 'Dram' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Family[/COLOR]' , 'Aile' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']History[/COLOR]' , 'Tarih' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Horror[/COLOR]' , 'Korku' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Mystery[/COLOR]' , 'Gizem' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Romance[/COLOR]' , 'Romantik' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Sport[/COLOR]' , 'Spor' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Western[/COLOR]' , 'Tarih' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 if 11 - 11: oOOoOooOo
def IIIiII1iIII ( url ) :
 I111iIIII11iI = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oOOo0 = cloudflare . source ( I111iIIII11iI )
 iI111i = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , oOoooooOoO , o0OOOo in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 10022 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
  if 62 - 62: IIiIiII11i . oOOoOooOo + oOo % oOo - o0o00Oo0O - IIiIiII11i
  if 22 - 22: i1iIi - I1ii11iIi11i % oOoO0o00OO0 % oOOoOooOo % I11i1ii1
  if 72 - 72: ooOoO0O00
  if 72 - 72: oOOoOooOo + IIiIiII11i . o0o00Oo0O - iiiiiiii1 / ii . O0Oooo0O
def iii ( ) :
 if 32 - 32: ii
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 iIIII1iIIii = ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oOOo0 = cloudflare . source ( iIIII1iIIii )
 iI111i = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 10022 , I1IIIii + 'dtv.png' )
   if 29 - 29: oOoO0o00OO0
   if 41 - 41: i1iIi
   if 49 - 49: i1iIi % IIiIiII11i . i1iIi - ooo0O - i1IiiiI1iI * I11i1ii1
def Iii ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for IIi11i1II , oO000o , iIiI , o0OOOo in iI111i :
  O0O0O0OOO0o = ( iIiI ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oO0Oo0oOo = ( oO000o ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  II1oOO0O0Ooo0 = 'Season ' + oO0Oo0oOo + 'Episode ' + O0O0O0OOO0o + o0OOOo
  I11iiI1i ( II1oOO0O0Ooo0 , IIi11i1II )
  if 52 - 52: o0o00Oo0O + iii1i1iiiiIi
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 5 - 5: oOo0O0Ooo - ooo0O . ii - IIiIiII11i
  if 38 - 38: i1iIi * oOoO0o00OO0 % oOo
def I11iiI1i ( name , url ) :
 IIi11i1II = url
 iii1iII1I1I = name
 oo00O00oO = cloudflare . source ( IIi11i1II )
 IIi11i1i1iI1 = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oo00O00oO )
 for I1ii1ii1I , oo00o in IIi11i1i1iI1 :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + iii1iII1I1I + oo00o + '[/COLOR]' , I1ii1ii1I , 222 , I1IIIii + 'dtv.png' )
  if 14 - 14: i1iIi + i1iIi * ii * i1IiiiI1iI + I1ii11iIi11i . oOo0O0Ooo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: OoOo0o . OoOo0o
 if 17 - 17: IIiIiII11i / oOOoOooOo
def OO0 ( ) :
 if 80 - 80: OoOo0o * oOo + i1iIi
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
 if 98 - 98: ooo0O * I1ii11iIi11i - i1iIi . oOOoOooOo
 if 2 - 2: I1ii11iIi11i - oOOoOooOo % iI11I1II1I1I
 if 88 - 88: O0Oooo0O - oOo
 if 79 - 79: iiiiiiii1
 if 45 - 45: IIiIiII11i + iiiiiiii1 . i1IiiiI1iI . o0o00Oo0O * ooOoO0O00 - i1iIi
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , '' , 10091 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 if 48 - 48: oOoO0o00OO0 + I1ii11iIi11i
def o0OOoOoo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oOOo0 )
 O0O00o0O = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + oOoooooOoO , '' , '' )
 for url in O0O00o0O :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , I1IIIii + 'Next.png' , '' , '' )
  if 31 - 31: oOo0O0Ooo - ii . I11i1ii1
def I1IO00O0oO00o ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oOOo0 )
 O0O00o0O = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo in iI111i :
  oOoooooOoO = 'http://watchepisodes.cc/' + oOoooooOoO
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 10093 , oOoooooOoO , oOoooooOoO , '' )
 for url in O0O00o0O :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , I1IIIii + 'Next.png' , '' , '' )
  if 30 - 30: iii1i1iiiiIi % I11i1ii1 . I1ii11iIi11i - ii
def iIi1IIiiiI ( url , iconimage ) :
 oOoooooOoO = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oOOo0 )
 for iIiI , url , o0OOOo in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + iIiI + ' - ' + o0OOOo + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , oOoooooOoO , '' , '' )
  if 4 - 4: ooOoO0O00 % ooo0O % OOOo00oo0oO . ooOoO0O00
def O0OO0OOo00Oo ( url , iconimage ) :
 oOoooooOoO = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url in iI111i :
  if 'player' in o0OOOo :
   pass
  elif 'vod' in o0OOOo :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , oOoooooOoO , '' , '' )
   if 26 - 26: IIiIiII11i * iiiiiiii1 + ooo0O / o0o00Oo0O + ooOoO0O00 - i1IiiiI1iI
   if 56 - 56: OoOo0o
   if 76 - 76: ooOoO0O00 % iI11I1II1I1I - ooo0O + I11i1ii1 - i1IiiiI1iI
   if 81 - 81: oOoO0o00OO0 + ii - OoOo0o * o0o00Oo0O
   if 100 - 100: iI11I1II1I1I - iii1i1iiiiIi
   if 28 - 28: I1ii11iIi11i . o0o00Oo0O . i1IiiiI1iI
def Ooo00O ( ) :
 if 60 - 60: ooOoO0O00
 if 57 - 57: oOOoOooOo
 if 99 - 99: I1ii11iIi11i + O0Oooo0O % oOOoOooOo - ooo0O
 if 52 - 52: oOoO0o00OO0
 if 93 - 93: iiiiiiii1 . Ii
 if 24 - 24: OoOo0o . oOo + O0Oooo0O . OOOo00oo0oO - oOoO0o00OO0 % iiiiiiii1
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / i1iIi
 if 29 - 29: oOoO0o00OO0 / OOOo00oo0oO * o0o00Oo0O - Ii - oOo + i1iIi
 if 86 - 86: oOo0O0Ooo / oOoO0o00OO0 * i1iIi % Ii
 if 20 - 20: iiiiiiii1 . ii + iiiiiiii1 + oOOoOooOo * oOoO0o00OO0
 if 44 - 44: Ii
 if 69 - 69: OoOo0o * o0o00Oo0O + Ii
 if 65 - 65: o0o00Oo0O / iiiiiiii1 . ooOoO0O00 * iiiiiiii1 / iI11I1II1I1I - OOOo00oo0oO
 if 93 - 93: iii1i1iiiiIi % Ii - i1iIi % oOo
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , I1IIIii + 'latest.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , I1IIIii + 'popular.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , I1IIIii + 'Genre.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , I1IIIii + 'series.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , I1IIIii + 'Search.png' , I1IIIii + 'WatchSeries.png' , '' )
 if 55 - 55: ooo0O . oOoO0o00OO0
 if 63 - 63: OOOo00oo0oO
def OOOOoO0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0o0O0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O0o0O0 ) )
 for url , o0OOOo in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 79 - 79: Ii
def o0O0oO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 13 - 13: I11i1ii1 . I1ii11iIi11i % OOOo00oo0oO * iiiiiiii1 - Ii / oOOoOooOo
def o0OooOOo0OO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  if 'episode' in url :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , I1IIIii + 'Next.png' , '' , '' )
  if 14 - 14: i1iIi - o0o00Oo0O
  if 68 - 68: IIiIiII11i - oOoO0o00OO0 - oOo * iI11I1II1I1I / oOo0O0Ooo * oOoO0o00OO0
def I1i1ii1IiI1i ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0O00o0oO00 = 'http://www.watchseriesgo.to/search/' + IiIi1oo00ooOoo . replace ( ' ' , '%20' )
 oOOo0 = i11111IIIII ( oo0O00o0oO00 )
 iI111i = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , iIIII1iIIii , o0OOOo in iI111i :
  if 'watch online' in o0OOOo :
   pass
  else :
   print iIIII1iIIii
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.watchseriesgo.to' + iIIII1iIIii , 10044 , oOoooooOoO , '' , '' )
   if 42 - 42: ooOoO0O00 + iiiiiiii1 . ii + oOoO0o00OO0 . i1IiiiI1iI / i1iIi
   xbmcplugin . setContent ( IIIii1II1II , 'movies' )
   if 1 - 1: ooo0O
def O00oi111II ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo , iIiI , oOOOO in iI111i :
  i1i1IiIi1 = ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iIiI ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1i1IiIi1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOoooooOoO , '' , oOOOO )
  if 6 - 6: OoOo0o - o0o00Oo0O * oOoO0o00OO0
def O0o0ooo00o00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  i1i1IiIi1 = ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1i1IiIi1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , I1IIIii + 'Next.png' , '' , '' )
  if 6 - 6: Ii / oOo . Ii / oOOoOooOo
def IiI1Iii1iIIII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOoooooOoO , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , I1IIIii + 'Next.png' , '' , '' )
  if 87 - 87: IIiIiII11i . i1iIi * oOo
def OOoO00o00oo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oOOo0 )
 O0o0O0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 for oO000o , oO0o in O0o0O0 :
  iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oO0o ) )
  for url , o0OOOo in iI111i :
   i1i1IiIi1 = ( oO000o ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1i1IiIi1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I1IIIii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 5 - 5: OOOo00oo0oO - ii / iii1i1iiiiIi
class I1II1i1iIIi ( ) :
 if 55 - 55: oOo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 20 - 20: oOOoOooOo * O0Oooo0O * ooo0O - oOOoOooOo
  i1i1IiIi1 = name
  self . Get_Sources ( iIIII1iIIii , i1i1IiIi1 )
  if 32 - 32: i1iIi * OOOo00oo0oO
  if 85 - 85: Ii . oOo + oOo
 def Get_Sources ( self , URL , season_name ) :
  o0oO0 = xbmcgui . DialogProgress ( )
  oOOo0 = i11111IIIII ( URL )
  iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  for iIIII1iIIii , o0OOOo in iI111i :
   URL = 'http://www.watchseriesgo.to/link/' + iIIII1iIIii
   self . Get_site_link ( URL , season_name )
   if 28 - 28: I1ii11iIi11i
 def Get_site_link ( self , url , season_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oOOo0 )
  Ii1II1I11i1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oOOo0 )
  for url in iI111i :
   self . main ( url , season_name )
  for url in IIi11i1i1iI1 :
   self . main ( url , season_name )
  for url in Ii1II1I11i1 :
   self . main ( url , season_name )
   if 62 - 62: I1ii11iIi11i + ii / iiiiiiii1
 def main ( self , url , season_name ) :
  o0oO0 . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   O0oO0O0ooo00o0 = 'DACLIPS'
   if O0oO0O0ooo00o0 in I1II1i1iIIi . source_list :
    pass
   else :
    self . daclips ( url , season_name , O0oO0O0ooo00o0 )
    o0oO0 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    O0oO0O0ooo00o0 = 'THEVIDEO'
    if O0oO0O0ooo00o0 in I1II1i1iIIi . source_list :
     pass
    else :
     self . thevideo ( url , season_name , O0oO0O0ooo00o0 )
     o0oO0 . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     O0oO0O0ooo00o0 = 'ALLMYVIDEOS'
     if O0oO0O0ooo00o0 in I1II1i1iIIi . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , O0oO0O0ooo00o0 )
      o0oO0 . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      O0oO0O0ooo00o0 = 'VIDSPOT'
      if O0oO0O0ooo00o0 in I1II1i1iIIi . source_list :
       pass
      else :
       self . vidspot ( url , season_name , O0oO0O0ooo00o0 )
       o0oO0 . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       O0oO0O0ooo00o0 = 'VODLOCKER'
       if O0oO0O0ooo00o0 in I1II1i1iIIi . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , O0oO0O0ooo00o0 )
        o0oO0 . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        O0oO0O0ooo00o0 = 'VIDTO'
        if O0oO0O0ooo00o0 in I1II1i1iIIi . source_list :
         pass
        else :
         self . vidto ( url , season_name , O0oO0O0ooo00o0 )
         o0oO0 . update ( 0 , "" , "Getting Vidto Links" )
         if 2 - 2: O0Oooo0O / OoOo0o
       else :
        if 'youwatch' in url :
         O0oO0O0ooo00o0 = 'YouWatch'
         if O0oO0O0ooo00o0 in I1II1i1iIIi . source_list :
          pass
         else :
          self . youwatch ( url , season_name , O0oO0O0ooo00o0 )
          o0oO0 . update ( 0 , "" , "Getting YouWatch Links" )
          if 6 - 6: Ii / I1ii11iIi11i % iiiiiiii1 / OoOo0o * o0o00Oo0O
          if 18 - 18: o0o00Oo0O
 def allmyvid ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  for oo0o0000Oo0 , o0OOOo in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
   if 14 - 14: i1iIi / I11i1ii1 - o0o00Oo0O
 def vidspot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oOOo0 )
  for oo0o0000Oo0 , o0OOOo in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
   if 16 - 16: O0Oooo0O % iI11I1II1I1I . ooOoO0O00
 def thevideo ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{"file":"([^"]*)"' ) . findall ( oOOo0 )
  for oo0o0000Oo0 in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
   if 72 - 72: oOOoOooOo * OoOo0o
 def vodlocker ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for oo0o0000Oo0 in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
   if 69 - 69: OOOo00oo0oO - Ii
 def daclips ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oOOo0 )
  for oo0o0000Oo0 in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
   if 29 - 29: i1iIi + iiiiiiii1 % oOoO0o00OO0 + i1IiiiI1iI * I1ii11iIi11i - Ii
 def filehoot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for oo0o0000Oo0 in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for oo0o0000Oo0 in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
  for oo0o0000Oo0 in iI111i :
   self . youplay ( oo0o0000Oo0 , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for oo0o0000Oo0 in iI111i :
   self . Printer ( oo0o0000Oo0 , season_name , source_name )
   if 24 - 24: Ii . oOOoOooOo + oOOoOooOo - Ii % OoOo0o
 def Printer ( self , Link , season_name , source_name ) :
  if 58 - 58: oOo0O0Ooo
  if Link in I1II1i1iIIi . List :
   pass
  elif source_name in I1II1i1iIIi . source_list :
   pass
  else :
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 222 , I1IIIii + 'WATCHSERIES.png' )
   o0oO0 . update ( 100 , "" , "Got Source" )
   I1II1i1iIIi . List . append ( Link )
   I1II1i1iIIi . source_list . append ( source_name )
   if 94 - 94: ooo0O + i1iIi % ooo0O . O0Oooo0O - oOOoOooOo * oOo0O0Ooo
   xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 62 - 62: I1ii11iIi11i * ooOoO0O00 % oOoO0o00OO0 + I1ii11iIi11i . o0o00Oo0O . oOOoOooOo
   if 57 - 57: I1ii11iIi11i - O0Oooo0O + o0o00Oo0O % ooo0O
   if 72 - 72: OoOo0o . iii1i1iiiiIi / IIiIiII11i
   if 69 - 69: OoOo0o * IIiIiII11i - oOOoOooOo - ooOoO0O00 + Ii
   if 50 - 50: ii * ooOoO0O00 / OOOo00oo0oO
def iI1i111I1Ii ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , I1IIIii + 'Highlights.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , I1IIIii + 'Fixtures.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , I1IIIii + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 83 - 83: ooOoO0O00
def iiiIiii11i1i ( url ) :
 ooo0O0Oo0O = '20'
 Oo0oi1i = [ ]
 OO00O0O00oOOO = '                                                    '
 ii1111iIIiIIi = '        '
 o00oOOooOOo0o ( OO00O0O00oOOO + 'pl' + ii1111iIIiIIi + 'w' + ii1111iIIiIIi + 'd' + ii1111iIIiIIi + 'l' + ii1111iIIiIIi + 'f' + ii1111iIIiIIi + 'a' + ii1111iIIiIIi + 'pts' , '' , '' , '' , '' , '' )
 iiI11Iii = OoO00oo00 ( url )
 iI111i = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( iiI11Iii )
 for ooOo0Oo , I11i1I111II1IiI , oo00O0oOo , II1i1 , IiI1Ii , oOo0oO , ooOO00oOOo000 , oOO00o0oooOo0 , iIII1iIi in iI111i :
  iiii1Ii = IIiiiI ( I11i1I111II1IiI )
  ii11 = IIiiiI ( oo00O0oOo )
  iI1i1i1i1i = IIiiiI ( II1i1 )
  iiII1i1II1iIi = IIiiiI ( IiI1Ii )
  iIIOOOO0o0Oo0 = IIiiiI ( oOo0oO )
  I1iIiI1iiI = IIiiiI ( ooOO00oOOo000 )
  Oo0oi1i . append ( ooOo0Oo [ 0 ] )
  oO000O00 = len ( Oo0oi1i )
  IiIIIii1iIII1 = int ( len ( OO00O0O00oOOO ) - len ( ooOo0Oo ) - 2 )
  if len ( Oo0oi1i ) >= 10 :
   IiIIIii1iIII1 = IiIIIii1iIII1 - 1
  if len ( Oo0oi1i ) <= int ( ooo0O0Oo0O ) :
   O0O0ooOOO ( str ( oO000O00 ) + ' ' + ooOo0Oo + OO00O0O00oOOO [ 0 : IiIIIii1iIII1 ] + I11i1I111II1IiI + iiii1Ii + oo00O0oOo + ii11 + II1i1 + iI1i1i1i1i + IiI1Ii + iiII1i1II1iIi + oOo0oO + iIIOOOO0o0Oo0 + ooOO00oOOo000 + I1iIiI1iiI + ' ' + iIII1iIi , '' , '' , '' , '' , '' )
   if 69 - 69: ooOoO0O00 / Ii + I1ii11iIi11i - iii1i1iiiiIi
   if 13 - 13: I11i1ii1 . iI11I1II1I1I
def IIiiiI ( space ) :
 if len ( space ) > 1 :
  OoOooOo00O = len ( '        ' ) - len ( space ) + 1
  space = int ( OoOooOo00O ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 30 - 30: ooOoO0O00
def iII1ii11I1I ( ) :
 if 50 - 50: OOOo00oo0oO * O0Oooo0O % ooOoO0O00 . iiiiiiii1 / OOOo00oo0oO . OoOo0o
 if 27 - 27: ooOoO0O00 + iI11I1II1I1I
 if 97 - 97: oOOoOooOo * I1ii11iIi11i / ooo0O . IIiIiII11i / iiiiiiii1 / iiiiiiii1
 if 25 - 25: iiiiiiii1
 if 85 - 85: I1ii11iIi11i + I1ii11iIi11i % i1IiiiI1iI + O0Oooo0O
 if 57 - 57: iii1i1iiiiIi / oOoO0o00OO0
 if 90 - 90: i1iIi / OOOo00oo0oO * I1ii11iIi11i * I1ii11iIi11i / iii1i1iiiiIi
 if 86 - 86: oOoO0o00OO0 * oOOoOooOo - o0o00Oo0O
 if 21 - 21: oOo0O0Ooo . I1ii11iIi11i
 if 54 - 54: O0Oooo0O - O0Oooo0O * o0o00Oo0O / i1iIi + oOo0O0Ooo - O0Oooo0O
 if 58 - 58: ii * ooOoO0O00 * iii1i1iiiiIi
 if 99 - 99: I1ii11iIi11i
 if 72 - 72: I1ii11iIi11i / IIiIiII11i * oOOoOooOo * oOoO0o00OO0 - I11i1ii1 / O0Oooo0O
 if 82 - 82: oOo0O0Ooo / i1IiiiI1iI
 if 6 - 6: i1iIi / oOOoOooOo / Ii % ooo0O
 if 69 - 69: O0Oooo0O
 if 83 - 83: iI11I1II1I1I . ooo0O + O0Oooo0O . ii / oOOoOooOo + IIiIiII11i
 if 90 - 90: i1iIi * iiiiiiii1 / OoOo0o
 if 68 - 68: iii1i1iiiiIi
 if 65 - 65: OOOo00oo0oO
 if 82 - 82: ooo0O
 if 80 - 80: ooOoO0O00 % iii1i1iiiiIi + oOo - ii / iI11I1II1I1I + O0Oooo0O
 if 65 - 65: i1iIi
 if 71 - 71: O0Oooo0O % O0Oooo0O . OOOo00oo0oO + Ii - Ii
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / O0Oooo0O - Ii . oOOoOooOo / OoOo0o
 if 13 - 13: ooo0O % o0o00Oo0O - O0Oooo0O * ii / I1ii11iIi11i - ii
 if 78 - 78: OOOo00oo0oO % ii
 if 73 - 73: oOo0O0Ooo % oOOoOooOo % I11i1ii1 + ooOoO0O00 - ii / OOOo00oo0oO
 if 78 - 78: ii % OOOo00oo0oO - Ii
 if 37 - 37: I11i1ii1 % i1iIi % ooOoO0O00
 if 23 - 23: oOOoOooOo - o0o00Oo0O + Ii
 if 98 - 98: ii
 if 61 - 61: ooo0O . I11i1ii1 . o0o00Oo0O + ii + o0o00Oo0O
 if 65 - 65: ooOoO0O00 * OoOo0o * ii - I11i1ii1 . iiiiiiii1 - oOo
 if 71 - 71: i1iIi * iii1i1iiiiIi
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % O0Oooo0O * ooo0O
 if 64 - 64: oOOoOooOo / oOOoOooOo + oOoO0o00OO0 * OoOo0o % OoOo0o
 if 87 - 87: oOo * I1ii11iIi11i
 if 83 - 83: ooOoO0O00 * O0Oooo0O - I11i1ii1 / i1iIi
 if 48 - 48: OOOo00oo0oO . IIiIiII11i - iii1i1iiiiIi % ooOoO0O00 . iii1i1iiiiIi
 if 32 - 32: i1iIi * oOo0O0Ooo - OoOo0o . I1ii11iIi11i / o0o00Oo0O + i1iIi
 if 67 - 67: iii1i1iiiiIi % I1ii11iIi11i
 if 7 - 7: Ii % oOoO0o00OO0 / O0Oooo0O % I1ii11iIi11i - oOo
 if 73 - 73: oOoO0o00OO0
 if 92 - 92: Ii + o0o00Oo0O * i1IiiiI1iI
 if 60 - 60: ooo0O / I1ii11iIi11i
 if 19 - 19: iI11I1II1I1I . oOo / ii
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % O0Oooo0O / oOoO0o00OO0
 if 76 - 76: oOo * OOOo00oo0oO - oOo
 if 57 - 57: ii / iii1i1iiiiIi + OOOo00oo0oO . i1iIi
 if 14 - 14: Ii % OoOo0o * ooo0O * iii1i1iiiiIi
 if 55 - 55: O0Oooo0O * OoOo0o * O0Oooo0O
 if 70 - 70: o0o00Oo0O . i1iIi
 if 33 - 33: OoOo0o * i1iIi
 if 64 - 64: Ii . iI11I1II1I1I
 if 7 - 7: iii1i1iiiiIi % oOOoOooOo + iii1i1iiiiIi - iii1i1iiiiIi * Ii % oOo
 if 57 - 57: OoOo0o / oOo + oOoO0o00OO0
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % OoOo0o + I11i1ii1 . oOo . I1ii11iIi11i
 if 70 - 70: i1IiiiI1iI . oOoO0o00OO0 * OOOo00oo0oO
 if 97 - 97: OOOo00oo0oO . iI11I1II1I1I - OoOo0o
 if 23 - 23: oOoO0o00OO0 % i1IiiiI1iI
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
 if 99 - 99: O0Oooo0O - oOoO0o00OO0 - oOo0O0Ooo - O0Oooo0O + oOo + IIiIiII11i
 if 34 - 34: O0Oooo0O * i1IiiiI1iI
 if 31 - 31: I11i1ii1 . OOOo00oo0oO
 if 40 - 40: i1iIi - i1IiiiI1iI / IIiIiII11i * ooOoO0O00 + I11i1ii1 * IIiIiII11i
 if 53 - 53: oOoO0o00OO0 - Ii . oOo / iii1i1iiiiIi - O0Oooo0O
 if 99 - 99: i1iIi - I11i1ii1 - ooOoO0O00 / Ii . I11i1ii1
 if 58 - 58: OoOo0o
 if 12 - 12: oOo0O0Ooo . ooo0O * ii
 if 64 - 64: iii1i1iiiiIi + I11i1ii1 - ooOoO0O00 . IIiIiII11i . oOo
 if 31 - 31: OOOo00oo0oO . iiiiiiii1 - i1IiiiI1iI . iI11I1II1I1I + i1IiiiI1iI . iii1i1iiiiIi
 if 86 - 86: oOoO0o00OO0 - oOoO0o00OO0 / iiiiiiii1 - oOoO0o00OO0 * iiiiiiii1 + O0Oooo0O
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - I11i1ii1
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iI111i = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIIII1iIIii , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOoooooOoO , Oo00OOOOO , '' )
  if 30 - 30: ii % OoOo0o
def IIiIoOOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0o0O0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oOOo0 )
 for O0o0O0 in O0o0O0 :
  I11II1i1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( O0o0O0 ) )
  for O00o00 in I11II1i1 :
   O00o00 = O00o00
  ii1Io0OOoOoO00 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O0o0O0 ) )
  for III1 , oOoooooOoO , time , OOo00o0oOO0o in ii1Io0OOoOoO00 :
   iIOoo0ooo0oo = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( OOo00o0oOO0o )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O00o00 + ' - ' + III1 + ' - ' + time + '[/COLOR]' , '' , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOoooooOoO , Oo00OOOOO , ( str ( iIOoo0ooo0oo ) ) )
   if 27 - 27: iiiiiiii1 / ooOoO0O00 . iiiiiiii1 % ii * OOOo00oo0oO % IIiIiII11i
 iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if 40 - 40: i1IiiiI1iI % i1iIi
def o0OiI1 ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , I1IIIii + 'fanart.jpg' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , I1IIIii + 'fanart.jpg' , '' )
 if 22 - 22: ooOoO0O00 / iii1i1iiiiIi / OoOo0o . oOo % O0Oooo0O + Ii
def oO0o0oo ( url ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo in iI111i :
  iiiI11iii11iI = o0OOOo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0OOOo :
   pass
  else :
   iiiI11iii11iI = o0OOOo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + iiiI11iii11iI + '[/COLOR]' , url , 10013 , oOoooooOoO )
 for url , oOoooooOoO , o0OOOo in IIi11i1i1iI1 :
  iiiI11iii11iI = o0OOOo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0OOOo :
   pass
  else :
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + iiiI11iii11iI + '[/COLOR]' , url , 10013 , oOoooooOoO )
def I111iIii1i1 ( url ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 if 6 - 6: O0Oooo0O % I11i1ii1 / i1iIi + O0Oooo0O . OOOo00oo0oO
 if 70 - 70: iI11I1II1I1I / i1iIi
 if 61 - 61: o0o00Oo0O * ooo0O + O0Oooo0O - OoOo0o . oOo0O0Ooo - I11i1ii1
 if 7 - 7: oOoO0o00OO0
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % ooo0O / i1IiiiI1iI
 if 95 - 95: iii1i1iiiiIi - o0o00Oo0O % ii
 if 13 - 13: Ii
 for url , oOoooooOoO , o0OOOo in IIi11i1i1iI1 :
  iiiI11iii11iI = o0OOOo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0OOOo :
   pass
  else :
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + iiiI11iii11iI + '[/COLOR]' , url , 10013 , oOoooooOoO )
   if 54 - 54: OoOo0o . oOoO0o00OO0 * i1IiiiI1iI % O0Oooo0O . o0o00Oo0O * I11i1ii1
def o00OOOOoOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oOOo0 )
 for I1ii1ii1I in iI111i :
  OooOoOoo0ooo0 = ( I1ii1ii1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I1iiIiiii1111 ( 'http:' + OooOoOoo0ooo0 )
  if 69 - 69: I1ii11iIi11i * oOOoOooOo
  if 91 - 91: ooo0O . oOOoOooOo / oOo / Ii * ooo0O
  if 52 - 52: oOo0O0Ooo - Ii / I11i1ii1 . OOOo00oo0oO
  if 38 - 38: OOOo00oo0oO + ii * iii1i1iiiiIi % OOOo00oo0oO
def oo0Oooo0O ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo , oOoooooOoO in iI111i :
  I111i1i1111 ( o0OOOo , url , 8046 , oOoooooOoO )
 for url in IIi11i1i1iI1 :
  Ii111 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , I1IIIii + 'Next.png' )
def ooO0Oo ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iiI11Iii )
 for url , oOoooooOoO , o0OOOo in iI111i :
  I1iiIiiii1111 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 81 - 81: OoOo0o
def OooOooo00OOO0o ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iiI11Iii )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 41 - 41: OoOo0o % Ii * oOo0O0Ooo + ooo0O / OOOo00oo0oO
def OOOoOO ( ) :
 Ii111 ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , I1IIIii + 'documentary.png' )
 Ii111 ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , I1IIIii + 'documentary.png' )
 Ii111 ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , I1IIIii + 'Search.png' )
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( o0OOOo , iIIII1iIIii , 8041 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO0i11i1i1i ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iiI11Iii )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iiI11Iii )
 for oOoooooOoO , url , o0OOOo in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOoooooOoO )
 for url in next :
  Ii111 ( 'NEXT PAGE' , url , 8041 , I1IIIii + 'Next.png' )
  if 83 - 83: IIiIiII11i + I11i1ii1 - ooo0O % ooo0O * ooo0O
  if 100 - 100: i1iIi . iI11I1II1I1I
def Iiii1i11III1I1 ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iiI11Iii )
 for url in iI111i :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
  else :
   Ii111 ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def O000o ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , url in iI111i :
  url = ( url ) . replace ( '\/' , '/' )
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 222 , '' )
  if 44 - 44: IIiIiII11i
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIiiiiiiII ( name , url ) :
 o00O00o0O0 = 0
 name = name
 url = url
 iiIi11iI1iii = [ '144' , '240' , '380' , '480' , '720' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  i11IIIiI1I ( url )
  if 41 - 41: IIiIiII11i * o0o00Oo0O % OoOo0o . iI11I1II1I1I
  if 55 - 55: I11i1ii1
  if 43 - 43: OoOo0o
  if 17 - 17: Ii
  if 94 - 94: ii - I11i1ii1 + OOOo00oo0oO . ii / ooOoO0O00
  if 53 - 53: O0Oooo0O % oOoO0o00OO0
  if 17 - 17: ii % i1iIi % o0o00Oo0O
  if 46 - 46: iiiiiiii1 + O0Oooo0O % ii * oOoO0o00OO0
def O000o0O0 ( ) :
 iiI11Iii = I1I1i ( 'http://documentarylovers.com/' )
 iI111i = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  if 'genre' in iIIII1iIIii :
   Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , iIIII1iIIii , 80010 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0000oOoO0o0 ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iiI11Iii )
 for url , o0OOOo , oOoooooOoO in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOoooooOoO )
 for url in next :
  Ii111 ( 'NEXT PAGE' , url , 80010 , I1IIIii + 'Next.png' )
  if 19 - 19: ooOoO0O00 % OOOo00oo0oO / ooo0O . ooo0O
def o00oI1i1IIIIIII ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iiI11Iii )
 for url in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
 for url in IIi11i1i1iI1 :
  O000o ( url )
  if 1 - 1: iI11I1II1I1I - IIiIiII11i - OOOo00oo0oO % oOo + iii1i1iiiiIi + ooo0O
def I1IIiIi ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo = 'http://documentarylovers.com/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 oo0oO0 = oOOo . lower ( )
 O0000oOoO0o0 ( oo0oO0 )
 if 68 - 68: ii % I1ii11iIi11i + I1ii11iIi11i * ii + oOoO0o00OO0 * o0o00Oo0O
def iI1iiI1Ii ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  if 'films' in url :
   Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , I1IIIii + 'documentary.png' )
def i1iiII1iIIIIII ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iiI11Iii )
 for oOoooooOoO , url , o0OOOo in iI111i :
  if 'films' in url :
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOoooooOoO )
 for url in IIi11i1i1iI1 :
  Ii111 ( 'NEXT' , url , 8049 , I1IIIii + 'Next.png' )
def IIIIII11iIiI1III ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iiI11Iii )
 for url in iI111i :
  if 'rtd' in url :
   o0Ooo0 ( url )
   if 17 - 17: I11i1ii1 % ii / oOOoOooOo * ii
def o0Ooo0 ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iiI11Iii )
 for IIIi1I1IIii1II , file in iI111i :
  url = ( 'https://rtd.rt.com' + IIIi1I1IIii1II + file )
  i11IIIiI1I ( url )
  if 14 - 14: IIiIiII11i + o0o00Oo0O - iiiiiiii1
  if 18 - 18: ooo0O / Ii % oOoO0o00OO0 * ii
def o0OoOO0 ( ) :
 oOOo0 = I1I1i ( 'http://www.stream2watch.co/live-tv' )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo , O00oO0 in iI111i :
  Ii111 ( ( o0OOOo + '[COLOR' + iiI1IiI + ']' + O00oO0 + '[/COLOR]' ) , iIIII1iIIii , 8086 , oOoooooOoO )
  if 75 - 75: oOo0O0Ooo
def o00o000 ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , oOoooooOoO , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 8087 , oOoooooOoO )
  if 41 - 41: oOoO0o00OO0 * Ii - I1ii11iIi11i * IIiIiII11i
def OOO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  oOO0ooOO ( url , o0OOOo )
  if 65 - 65: iI11I1II1I1I
def oOO0ooOO ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  print url
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 76 - 76: iI11I1II1I1I * O0Oooo0O / oOo0O0Ooo
def ooOO0O00O ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iIIII1iIIii , 3002 , 'http://www.solie.org/alibrary/' + oOoooooOoO )
def i1iOOoOo0o ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iiI11Iii )
 for url , oOoooooOoO , o0OOOo in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOoooooOoO )
def oOOOiII1iII ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iiI11Iii )
 iiii11i1ii1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iiI11Iii )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , I1IIIii + 'classicmovies.png' )
 for url , o0OOOo in iiii11i1ii1 :
  Ii111 ( '[COLOR' + iiI1IiI + ']Season- ' + o0OOOo + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'classicmovies.png' )
 for url in next :
  Ii111 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'Next.png' )
 for url , oOoooooOoO , o0OOOo in IIi11i1i1iI1 :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOoooooOoO )
def oOO00o0O0O ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iiI11Iii )
 for url in iI111i :
  o0Ooo0OoO ( url )
def o0Ooo0OoO ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iiI11Iii )
 for url in iI111i :
  i11IIIiI1I ( url )
  if 31 - 31: i1IiiiI1iI + oOo / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
def o000ooooO0o ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iIIII1iIIii , 8065 , I1IIIii + 'classicmovies.png' )
def iiiiIiI1IIiI ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( "v.src = '([^']*)';" ) . findall ( iiI11Iii )
 for url in iI111i :
  O00o0o ( url )
  if 53 - 53: iI11I1II1I1I % iii1i1iiiiIi % oOo0O0Ooo + oOoO0o00OO0 % ii
def iiI ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iIIII1iIIii , 8065 , I1IIIii + 'classictv.png' )
def IIIIii11 ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  if 'mp4' in url :
   i11IIIiI1I ( url )
 for url in IIi11i1i1iI1 :
  yt . PlayVideo ( url )
  if 24 - 24: oOOoOooOo * Ii + ooo0O + ii
def oOOo0OoooOo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iI111i = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iIIII1iIIii , 8071 , I1IIIii + 'streams.png' )
def I1I1IiIiIIi1I ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for o0OOOo , url in iI111i :
  if '(Free Access)' in o0OOOo :
   url = ( url ) . strip ( )
  else :
   url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , I1IIIii + 'streams.png' )
def oo0Ooo ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , o0OOOo , url in iI111i :
  url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , oOoooooOoO , OoOo00o0OO , '' )
  if 21 - 21: oOoO0o00OO0 - OOOo00oo0oO * oOo
def IIIiIIIi11I ( ) :
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  oO00oOOOO ( 'http://watchxxxfree.com/categories' )
 if oo000o0000oO == 1 :
  o0o0OOO0ooo00 ( 'http://www.perfectgirls.net' )
 if oo000o0000oO == 2 :
  I11III111i1I ( 'http://www.xvideos.com/best' )
 if oo000o0000oO == 3 :
  O0ooOO0O00 ( 'http://www.xvideos.com/best' )
 if oo000o0000oO == 4 :
  I11III111i1I ( 'http://www.xvideos.com/best' )
 if oo000o0000oO == 5 :
  I11III111i1I ( 'http://www.xvideos.com/verified/videos' )
 if oo000o0000oO == 6 :
  OOO0O ( 'http://www.xvideos.com/tags' )
 if oo000o0000oO == 7 :
  iIi11 ( 'http://www.xvideos.com/porn' )
 if oo000o0000oO == 8 :
  OoO0OOOo0Oo ( )
  if 51 - 51: iI11I1II1I1I * ooOoO0O00 . iii1i1iiiiIi * IIiIiII11i - O0Oooo0O
  if 58 - 58: i1iIi . I11i1ii1 - oOoO0o00OO0 * iiiiiiii1 * oOoO0o00OO0 + I1ii11iIi11i
  if 15 - 15: oOoO0o00OO0 * i1iIi / iiiiiiii1 . ooo0O / i1iIi % iii1i1iiiiIi
  if 75 - 75: ii % Ii % iI11I1II1I1I % oOoO0o00OO0 / Ii
  if 96 - 96: oOOoOooOo * OOOo00oo0oO / iI11I1II1I1I / i1IiiiI1iI
  if 5 - 5: ooo0O
  if 83 - 83: i1IiiiI1iI * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
  if 35 - 35: iii1i1iiiiIi % oOo + o0o00Oo0O * ooo0O % oOoO0o00OO0
  if 57 - 57: OOOo00oo0oO / i1IiiiI1iI
def O00OO0OoO00oO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  if 'ch' in url :
   iii11III1I ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Jizbox.png' , I1IIIii + 'Jizbox.png' , '' )
def iiiI1iiIiII1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 oOo0oOOoo0O = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oOOo0 )
 for url , o0OOOo in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , I1IIIii + 'Jizbox.png' , '' , '' )
 for o0OOOo , url in oOo0oOOoo0O :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Next.png' , '' , '' )
def iI1IiI11Ii11i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   O0oi1IiI1I ( url )
def O00OOoOo0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  i11IIIiI1I ( url )
def oO00oOOOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo , OoOooOo00O in iI111i :
  if 'category' in url :
   iii11III1I ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORorange]   ' + OoOooOo00O + '[/COLOR]' , url , 90006 , oOoooooOoO , I1IIIii + 'Jizbox.png' , '' )
def O0ooO0oOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 oOo0oOOoo0O = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , oOoooooOoO , '' , '' )
 for url in oOo0oOOoo0O :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , url , 90006 , I1IIIii + 'Next.png' , '' , '' )
def ii111I1iII1i1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   O0oi1IiI1I ( url )
def O0oi1IiI1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  i11IIIiI1I ( url )
def o0o0OOO0ooo00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , OoOooOo00O in iI111i :
  if 'category' in url :
   iii11III1I ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORorange]' + OoOooOo00O + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , I1IIIii + 'Jizbox.png' , '' , '' )
def O000000oooOOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIi11i1II = url
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 oOo0oOOoo0O = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oOoooooOoO , '' , '' )
 for url in oOo0oOOoo0O :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , IIi11i1II + '/' + url , 90003 , I1IIIii + 'Next.png' , '' , '' )
def I11iiI1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'get\("(.*)", function' ) . findall ( oOOo0 )
 for url in iI111i :
  I1Ioo000oooooooO ( 'http://www.perfectgirls.net' + url )
def I1Ioo000oooooooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'http://(.+?)\n' ) . findall ( oOOo0 )
 for url in iI111i :
  I1iiIiiii1111 ( 'http://' + url )
def iIi11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oOOo0 )
 for url , o0OOOo , OoOooOo00O in iI111i :
  iii11III1I ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgreen] - No of Videos : [COLORorange]' + OoOooOo00O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
def OOO0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 oOo0oOOoo0O = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in oOo0oOOoo0O :
  iii11III1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , I1IIIii + 'Jizbox.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oOOo0 )
 for url , o0OOOo , OoOooOo00O in iI111i :
  iii11III1I ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgreen] - No of Videos : [COLORorange]' + ( OoOooOo00O + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
  if 18 - 18: OOOo00oo0oO * I1ii11iIi11i % Ii + o0o00Oo0O % OoOo0o . OoOo0o
def ooO00OoO ( url ) :
 oOOo0 = i11111IIIII ( url )
 oOo0oOOoo0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in oOo0oOOoo0O :
  iii11III1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo , o0O0O0ooo0oOO in iI111i :
  iii11III1I ( o0OOOo + '--' + ( o0O0O0ooo0oOO ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOoooooOoO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 62 - 62: OOOo00oo0oO
  if 15 - 15: iii1i1iiiiIi - i1IiiiI1iI - i1IiiiI1iI + I11i1ii1 * oOoO0o00OO0
def I11III111i1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo , I1I , O0OOoOOO0o0o in iI111i :
  iii11III1I ( '[COLORorangered]' + o0OOOo + '[COLORgreen] - Porn Quality : [COLORorange]' + I1I + ' - [COLORred]' + O0OOoOOO0o0o + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOoooooOoO , oOoooooOoO , I1I + ' - ' + O0OOoOOO0o0o )
 iIii1Ii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for oOoooooOoO , url , o0OOOo , O0OOoOOO0o0o in IIi11i1i1iI1 :
  iii11III1I ( '[COLORorangered]' + o0OOOo + '[COLORgreen] - Porn Quality : [COLORorange]' + O0OOoOOO0o0o + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOoooooOoO , oOoooooOoO , O0OOoOOO0o0o )
 iIii1Ii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in iIii1Ii :
  iii11III1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Next.png' , '' , '' )
  if 42 - 42: iiiiiiii1
  if 6 - 6: oOo + OoOo0o
def O0ooOO0O00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0o0O0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 oOo0oOOoo0O = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in oOo0oOOoo0O :
  iii11III1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O0o0O0 ) )
 for url , o0OOOo in iI111i :
  if '/c/' in url :
   iii11III1I ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
   if 22 - 22: I1ii11iIi11i . ii % O0Oooo0O
   if 16 - 16: oOoO0o00OO0
def OoO0OOOo0Oo ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOoOo0OoOOoo = ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 oo0oO0 = oOoOo0OoOOoo . lower ( )
 iI11IIi1iiI1I = 'http://www.xvideos.com/?k=' + oo0oO0
 print iI11IIi1iiI1I + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOo0 = i11111IIIII ( iI11IIi1iiI1I )
 iI111i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , iIIII1iIIii , o0OOOo , O0OOoOOO0o0o , i1iIIi1iIii in iI111i :
  iii11III1I ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgreen] - Porn Quality : [COLORorange]' + i1iIIi1iIii + ' - [COLORred]' + O0OOoOOO0o0o + '[/COLOR]' , 'http://www.xvideos.com' + iIIII1iIIii , 10108 , oOoooooOoO , oOoooooOoO , i1iIIi1iIii + ' - ' + O0OOoOOO0o0o )
 iIii1Ii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for iIIII1iIIii in iIii1Ii :
  iii11III1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iIIII1iIIii , 10105 , I1IIIii + 'Next.png' , '' , '' )
if 55 - 55: ooo0O . OoOo0o * iii1i1iiiiIi
if 19 - 19: iiiiiiii1
if 32 - 32: i1IiiiI1iI % oOOoOooOo % ii . oOOoOooOo % Ii + IIiIiII11i
if 25 - 25: oOOoOooOo
if 83 - 83: i1iIi / ii * OOOo00oo0oO . oOo0O0Ooo . ooOoO0O00
if 59 - 59: i1IiiiI1iI . i1IiiiI1iI * oOo0O0Ooo - i1iIi % iii1i1iiiiIi
if 19 - 19: ii / I1ii11iIi11i - O0Oooo0O . iii1i1iiiiIi
if 8 - 8: i1IiiiI1iI % oOOoOooOo . iI11I1II1I1I
if 95 - 95: ooo0O + Ii . oOoO0o00OO0 . oOOoOooOo . ooo0O
if 93 - 93: iiiiiiii1
if 55 - 55: IIiIiII11i % ooo0O - oOo
if 48 - 48: oOOoOooOo * iI11I1II1I1I % iii1i1iiiiIi
if 100 - 100: IIiIiII11i - Ii + oOo % oOOoOooOo - iI11I1II1I1I * Ii
if 30 - 30: oOo . oOo . i1iIi % i1iIi * ooOoO0O00 * OOOo00oo0oO
if 74 - 74: ii
if 33 - 33: ooo0O - IIiIiII11i
if 95 - 95: ii
if 23 - 23: IIiIiII11i + i1IiiiI1iI / o0o00Oo0O . i1IiiiI1iI . O0Oooo0O + iI11I1II1I1I
if 2 - 2: ooOoO0O00 . o0o00Oo0O / ooo0O . IIiIiII11i / oOo % ooOoO0O00
if 12 - 12: ooo0O
if 58 - 58: iI11I1II1I1I * i1iIi . oOOoOooOo . I1ii11iIi11i * i1iIi
if 63 - 63: iii1i1iiiiIi . i1IiiiI1iI * ooo0O - i1IiiiI1iI % i1IiiiI1iI
if 62 - 62: i1IiiiI1iI - oOOoOooOo / oOOoOooOo
if 95 - 95: iii1i1iiiiIi - ooOoO0O00 / O0Oooo0O . oOOoOooOo % OoOo0o - ooOoO0O00
if 12 - 12: iiiiiiii1
if 96 - 96: o0o00Oo0O
if 89 - 89: oOoO0o00OO0 - I1ii11iIi11i
if 26 - 26: oOOoOooOo % oOOoOooOo / IIiIiII11i / iiiiiiii1
if 2 - 2: ooOoO0O00 / Ii + oOo0O0Ooo
if 95 - 95: oOoO0o00OO0 / I11i1ii1 % iI11I1II1I1I + o0o00Oo0O
if 6 - 6: I11i1ii1
if 73 - 73: ooo0O % ooo0O . OoOo0o * oOoO0o00OO0 - i1iIi
if 97 - 97: I11i1ii1
if 15 - 15: o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . O0Oooo0O
if 64 - 64: oOOoOooOo / ooOoO0O00
def ooo00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oOOo0 )
 Ii1II1I11i1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  if 'http' in url :
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in IIi11i1i1iI1 :
  if 'http' in url :
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in Ii1II1I11i1 :
  if 'http' in url :
   I111i1i1111 ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
   if 56 - 56: OoOo0o - O0Oooo0O
def OOoO0ooOooOoo ( url ) :
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 import urlresolver
 try : o0000o0Oo . play ( url )
 except : pass
 if 57 - 57: Ii + i1IiiiI1iI % oOOoOooOo / iI11I1II1I1I
 if 74 - 74: I1ii11iIi11i + OoOo0o . ooo0O / iii1i1iiiiIi + i1iIi + ooOoO0O00
def O0o00oooO00o ( ) :
 if 83 - 83: OOOo00oo0oO
 if 34 - 34: iii1i1iiiiIi
 if 75 - 75: i1IiiiI1iI / iI11I1II1I1I + oOoO0o00OO0 / oOo
 if 50 - 50: O0Oooo0O / i1IiiiI1iI % iI11I1II1I1I
 if 46 - 46: oOOoOooOo + iiiiiiii1 - I1ii11iIi11i % OoOo0o + ii + iI11I1II1I1I
 if 99 - 99: oOo - I11i1ii1 * I11i1ii1 + OOOo00oo0oO / iiiiiiii1 + OoOo0o
 if 58 - 58: Ii + iI11I1II1I1I * ooo0O - iii1i1iiiiIi
 if 31 - 31: ooOoO0O00
 if 87 - 87: oOo0O0Ooo / i1IiiiI1iI + ii + o0o00Oo0O . i1iIi
 if 44 - 44: I1ii11iIi11i % I1ii11iIi11i
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 8091 , I1IIIii + 'gofish.png' )
def oOoo00o0OoOOO ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 for url , o0OOOo , oOoooooOoO in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 8092 , oOoooooOoO )
 for url in next :
  Ii111 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
def Ii11 ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 O0Oo0O0O0o0 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO in O0Oo0O0O0o0 :
  oOoooooOoO = oOoooooOoO
 for url , o0OOOo in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 8092 , oOoooooOoO )
 for url in next :
  Ii111 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
  if 82 - 82: ii / oOo0O0Ooo * IIiIiII11i - ii % iI11I1II1I1I * oOo
def Ii1Ii11I ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( "videoId: '([^']*)'," ) . findall ( oOOo0 )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 99 - 99: OoOo0o . iI11I1II1I1I
  if 45 - 45: O0Oooo0O - o0o00Oo0O . O0Oooo0O / O0Oooo0O / iii1i1iiiiIi
  if 12 - 12: OoOo0o
  if 75 - 75: OoOo0o + i1iIi + OOOo00oo0oO . I1ii11iIi11i
O0O0oOoO0O0oO = '{PQ},' ; iIiIoO00OooO00O0o = '{SC},' ; II1I1I1iIiiIi = '{XG},' ; i1i1I11II1Ii = '{JP},' ; O0o00 = '{HW},' ; Ii1I1I = '{RT},'
def I1I1 ( ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 i1iiIIiiiII = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 iIIII1iIIii = 'http://onlinemovies.tube/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 IIi11i1II = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OO0ooO0 = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OoOooOO0oOOo0O = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1II = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIi1Ii1III = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IiIi1oo00ooOoo
 Oooo00 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iii1II1iI1IIi = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 85 - 85: Ii - iiiiiiii1
 i1I111Ii = ( o0oOoO00o ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 i11i1i = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 69 - 69: OoOo0o + iiiiiiii1 / O0Oooo0O
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 oo00O00oO = i1Oo00 ( IIi11i1II )
 o0oO0 . update ( 14 , "" , "Checking Source Technica " )
 OOooO0Oo00 = i1Oo00 ( IIi11i1II )
 o0oO0 . update ( 32 , "" , "Checking Source Pandoras Box " )
 iIiIIIi = i1Oo00 ( Ii1I1 )
 o0oO0 . update ( 59 , "" , "Checking Source Lazy List " )
 ooo00OOOooO = i1Oo00 ( OO0ooO0 )
 o0oO0 . update ( 72 , "" , "Checking Source RaizTv " )
 iIIIIIIIiIII = i1Oo00 ( iii1II1iI1IIi )
 o0oO0 . update ( 91 , "" , "Checking WebSpace " )
 I1oOoO0OOO00O = i1Oo00 ( i11i1i )
 o0oO0 . update ( 97 , "" , "Matching Results" )
 if 37 - 37: iI11I1II1I1I * i1IiiiI1iI / I11i1ii1 * I1ii11iIi11i % Ii
 if iIIIIIIIiIII != 'Failed' :
  i1i1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIIIIiIII )
  for iIIII1iIIii , o0OOOo in i1i1 :
   o0oOoOo0 = i1Oo00 ( iIIII1iIIii )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , O00oO0 in III1IiI1i1i :
    O00oO0 = ( O00oO0 . replace ( '.' , ' ' ) )
    if oo0oO0 in O00oO0 . lower ( ) :
     if '.mkv' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , iIIII1iIIii + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.mp4' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , iIIII1iIIii + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.avi' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , iIIII1iIIii + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.wav' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , iIIII1iIIii + o0OOOOOo0 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , iIIII1iIIii + o0OOOOOo0 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting WebSpace Links" )
      if 93 - 93: oOOoOooOo + oOOoOooOo
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in IIi11i1i1iI1 :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORred] source Technica[/COLOR]' ) , iIIII1iIIii , 222 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 65 - 65: ii * i1IiiiI1iI * OOOo00oo0oO % oOoO0o00OO0 * IIiIiII11i
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 86 - 86: Ii / i1IiiiI1iI * iiiiiiii1 - iiiiiiii1
 if iIiIIIi != 'Failed' :
  Ii1II1I11i1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for IiI11I111 , o0OOOo in Ii1II1I11i1 :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1I1 + IiI11I111 ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Lazy List Links" )
 if ooo00OOOooO != 'Failed' :
  iIiiii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in iIiiii :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORred] source RaizTv[/COLOR]' ) , iIIII1iIIii , 222 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 32 - 32: I1ii11iIi11i . o0o00Oo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 Oooooooo00o00 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + '/Movies/a.to.z/' + III1II1i + '.php'
  iIIIIIIIiIII = i1Oo00 ( iI1i1IiIIIIi )
  if iIIIIIIIiIII != 'Failed' :
   i1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIIIIIiIII )
   for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in i1i1 :
    if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
     if '.php' in iIIII1iIIii :
      o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
      o00oOOooOOo0o ( o0OOOo + '-[COLORred] source Pans Box[/COLOR]' , iIIII1iIIii , 426 , II11IiiIII , I11Iii1 , oOOOO )
     else :
      o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
      o0iIiii ( o0OOOo + '-[COLORred] source Pans Box[/COLOR]' , iIIII1iIIii , 222 , II11IiiIII , I11Iii1 , oOOOO )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
      if 48 - 48: oOoO0o00OO0 % IIiIiII11i + i1IiiiI1iI
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
      if 25 - 25: I11i1ii1 * ooo0O / oOo0O0Ooo . I11i1ii1 % IIiIiII11i
 Oooooooo00o00 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 50 - 50: iii1i1iiiiIi * iiiiiiii1
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / i1IiiiI1iI
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = i1iiIIiiiII + III1II1i
  III1I1Iii11i = i1Oo00 ( iI1i1IiIIIIi )
  if III1I1Iii11i != 'Failed' :
   ooo0 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( III1I1Iii11i )
   for IiI11I111 , o0OOOo in ooo0 :
    if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
     I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1iiIIiiiII + III1II1i + IiI11I111 ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 92 - 92: ooo0O
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 8 - 8: iiiiiiii1 + oOoO0o00OO0 . i1iIi
def I1i11 ( ) :
 if 50 - 50: I1ii11iIi11i
 if 16 - 16: i1iIi - iii1i1iiiiIi % I1ii11iIi11i / i1iIi . i1IiiiI1iI + oOOoOooOo
 if 78 - 78: iI11I1II1I1I + oOo + Ii
 if 21 - 21: I1ii11iIi11i + i1iIi % oOOoOooOo + iii1i1iiiiIi % i1IiiiI1iI
 if 22 - 22: ooOoO0O00 / ii . oOo
 if 83 - 83: oOo0O0Ooo - ii + oOoO0o00OO0 . i1iIi / ooo0O + oOOoOooOo
 if 90 - 90: oOo0O0Ooo - Ii
 if 42 - 42: OoOo0o . I1ii11iIi11i
 if 21 - 21: iiiiiiii1 . oOo0O0Ooo / i1IiiiI1iI
 if 97 - 97: iI11I1II1I1I + ooOoO0O00 - ooo0O
 if 73 - 73: oOo - Ii % O0Oooo0O / I1ii11iIi11i - ii % OoOo0o
 if 79 - 79: oOo0O0Ooo / ooo0O . i1iIi * oOoO0o00OO0 + i1IiiiI1iI
 if 96 - 96: oOo * IIiIiII11i
 if 1 - 1: oOo0O0Ooo - iii1i1iiiiIi
 if 74 - 74: iii1i1iiiiIi * IIiIiII11i + o0o00Oo0O + i1IiiiI1iI
 if 3 - 3: iI11I1II1I1I - ooOoO0O00 / iiiiiiii1 + ooOoO0O00 + o0o00Oo0O
 if 18 - 18: iI11I1II1I1I . iiiiiiii1 % OoOo0o % OOOo00oo0oO + iI11I1II1I1I * ii
 if 78 - 78: I11i1ii1
 if 38 - 38: oOo * oOoO0o00OO0
 if 4 - 4: oOo . oOoO0o00OO0
 if 21 - 21: Ii / oOo / oOoO0o00OO0 * o0o00Oo0O - IIiIiII11i * OoOo0o
 if 27 - 27: ooo0O . iii1i1iiiiIi * i1iIi * iiiiiiii1 * o0o00Oo0O
 if 93 - 93: I11i1ii1 % O0Oooo0O % IIiIiII11i
 if 20 - 20: ii * O0Oooo0O
 if 38 - 38: iiiiiiii1 . ii
 if 28 - 28: O0Oooo0O * ooOoO0O00 . oOoO0o00OO0
 if 75 - 75: o0o00Oo0O / OOOo00oo0oO * oOOoOooOo - OoOo0o / ooOoO0O00
 if 61 - 61: i1IiiiI1iI
 if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
 if 35 - 35: oOOoOooOo
 if 57 - 57: oOo . I1ii11iIi11i + oOo0O0Ooo
 if 18 - 18: oOo0O0Ooo - oOoO0o00OO0 * i1IiiiI1iI / Ii - ooo0O % ooo0O
 if 31 - 31: i1IiiiI1iI
 if 100 - 100: Ii * Ii . iI11I1II1I1I % iiiiiiii1 * oOoO0o00OO0
 if 17 - 17: i1iIi * I11i1ii1 * Ii / oOoO0o00OO0 / Ii
 if 23 - 23: ii + Ii / I1ii11iIi11i / iiiiiiii1 . iiiiiiii1 * oOo0O0Ooo
 if 98 - 98: I11i1ii1
 if 23 - 23: i1IiiiI1iI / ooOoO0O00 * oOo
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 if 51 - 51: OoOo0o - ii / ii % ii
 if 85 - 85: oOo . ooo0O . oOo0O0Ooo
 o0OOOOOo0 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 IIi11i1II = 'http://onlinemovies.tube/?s=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OO0ooO0 = ( o0oOoO00o ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1II = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 iIIi1Ii1III = 'http://www.tvmaze.com/search?q=' + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 Oooo00 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iii1II1iI1IIi = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 75 - 75: iI11I1II1I1I - i1iIi % o0o00Oo0O % I11i1ii1
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 6 - 6: I1ii11iIi11i % OOOo00oo0oO * oOOoOooOo - ooOoO0O00 . iii1i1iiiiIi
 o0oO0 . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 20 - 20: I1ii11iIi11i / O0Oooo0O . I1ii11iIi11i
 if 60 - 60: oOoO0o00OO0 - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . iii1i1iiiiIi
 iiIIi1 = i1Oo00 ( o0OOOOOo0 )
 o0oO0 . update ( 14 , "" , "Checking Source 3/11 Links" )
 oo00O00oO = i1Oo00 ( IIi11i1II )
 o0oO0 . update ( 28 , "" , "Checking Source 4/11 Links" )
 iIiIIIi = i1Oo00 ( Ii1I1 )
 o0oO0 . update ( 40 , "" , "Checking Source 5/11 Links" )
 ooo00OOOooO = i1Oo00 ( OO0ooO0 )
 o0oO0 . update ( 52 , "" , "Checking Source 6/11 Links" )
 III1I1Iii11i = i1Oo00 ( I1II )
 o0oO0 . update ( 76 , "" , "Checking Source 7/11 Links" )
 O0OOOOo0 = i1Oo00 ( iIIi1Ii1III )
 o0oO0 . update ( 88 , "" , "Checking Source 8/11 Links" )
 OOooO0Oo00 = i1Oo00 ( Oooo00 )
 o0oO0 . update ( 95 , "" , "Checking Source 9/11 Links" )
 iIIIIIIIiIII = i1Oo00 ( iii1II1iI1IIi )
 o0oO0 . update ( 97 , "" , "Matching Results" )
 if 24 - 24: I11i1ii1 * oOo0O0Ooo / OoOo0o
 if 51 - 51: iI11I1II1I1I / i1IiiiI1iI * oOo * i1iIi + oOoO0o00OO0 . ii
 if iIIIIIIIiIII != 'Failed' :
  i1i1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIIIIiIII )
  for iIIII1iIIii , o0OOOo in i1i1 :
   o0oOoOo0 = i1Oo00 ( iIIII1iIIii )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , O00oO0 in III1IiI1i1i :
    if oo0oO0 in O00oO0 . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + O00oO0 + '-[COLORgold] source ' + o0OOOo + '[/COLOR]' ) , iIIII1iIIii + o0OOOOOo0 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 75 - 75: I11i1ii1 / ii / o0o00Oo0O % OoOo0o
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if OOooO0Oo00 != 'Failed' :
  OoO0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooO0Oo00 )
  for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in OoO0O :
   if oo0oO0 in o0OOOo . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] source HeroVision[/COLOR]' ) , iIIII1iIIii , 1016 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 10 , "" , "Getting Herovision Links" )
    if 87 - 87: IIiIiII11i / iI11I1II1I1I % oOoO0o00OO0
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 11 - 11: ooo0O * oOo
 if O0OOOOo0 != 'Failed' :
  Oo00OoOo = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( O0OOOOo0 )
  for iIIII1iIIii , oOoooooOoO , o0OOOo in Oo00OoOo :
   IIi11i1II = 'http://www.tvmaze.com' + iIIII1iIIii . replace ( '"' , '' )
   OO0ooo0o0 = requests . get ( IIi11i1II ) . content
   iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OO0ooo0o0 )
   for oOOOO in iI111i :
    if not '<div>' in oOOOO :
     oO0ooOoO = oOOOO . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
    oOoooooOoO = 'http:' + oOoooooOoO
    o0OOOo = o0OOOo . replace ( '&#039;' , '' )
    if o0OOOo == '' :
     ooO0000o00O = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( iIIII1iIIii ) )
     for o0OOOo in ooO0000o00O :
      o0OOOo = o0OOOo . replace ( '-' , ' ' )
   ii1iIi1iIiI1i ( o0OOOo + '-[COLORgold] source Scraper[/COLOR]' , IIi11i1II , 9110002 , oOoooooOoO , Oo00OOOOO , oO0ooOoO , '' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 20 , "" , "Getting Scraper Links" )
   if 92 - 92: iii1i1iiiiIi . I1ii11iIi11i * i1IiiiI1iI
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  II11ii1I11 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for iIIII1iIIii , oOoooooOoO , o0OOOo , o0oO00o in IIi11i1i1iI1 :
   if oo0oO0 in o0OOOo . lower ( ) :
    if 'season' in o0oO00o :
     Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' - [COLORred]Source - Tv HUB[/COLOR]' , iIIII1iIIii , 90054 , oOoooooOoO , oOoooooOoO , '' )
    if 'episodes' in o0oO00o :
     Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' - [COLORred]Source - Tv HUB[/COLOR]' , iIIII1iIIii , 90044 , oOoooooOoO , oOoooooOoO , '' )
  for iIIII1iIIii in II11ii1I11 :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , iIIII1iIIii , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 86 - 86: o0o00Oo0O
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iiIIi1 != 'Failed' :
  oOoOOOo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iiIIi1 )
  for iIIII1iIIii , o0OOOo , oOoooooOoO in oOoOOOo :
   if oo0oO0 in o0OOOo . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( o0OOOo ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , iIIII1iIIii , 8022 , oOoooooOoO , '' , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 45 , "" , "Getting Source iWatch Links" )
    if 55 - 55: i1iIi / O0Oooo0O / oOoO0o00OO0 % oOOoOooOo % oOo0O0Ooo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iIiIIIi != 'Failed' :
  Ii1II1I11i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for o0OOOo in Ii1II1I11i1 :
   if oo0oO0 in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Ii1I1 + o0OOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 55 - 55: OOOo00oo0oO + ii % ooOoO0O00
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  iIiiii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for o0OOOo in iIiiii :
   if oo0oO0 in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OO0ooO0 + o0OOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 24 - 24: oOoO0o00OO0 - I1ii11iIi11i
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if III1I1Iii11i != 'Failed' :
  ooo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III1I1Iii11i )
  for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in ooo0 :
   if oo0oO0 in o0OOOo . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + o0OOOo + '-[COLORgold] Source Scooby[/COLOR]' ) , iIIII1iIIii , 1016 , II11IiiIII , I11Iii1 , oOOOO )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 90 , "" , "Getting Scooby Links" )
    if 36 - 36: oOo0O0Ooo . OoOo0o % IIiIiII11i * I11i1ii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: i1IiiiI1iI % iiiiiiii1 - oOOoOooOo - oOo0O0Ooo
 O0oooOO0Oo0o = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for III1II1i in O0oooOO0Oo0o :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + III1II1i + '.php'
  iiiI1iI1 = i1Oo00 ( iI1i1IiIIIIi )
  if iiiI1iI1 != 'Failed' :
   IIIiI1iiiiiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iiiI1iI1 )
   for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in IIIiI1iiiiiIi :
    if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
     if '.php' in iIIII1iIIii :
      o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
      o00oOOooOOo0o ( o0OOOo + '-[COLORred] source Pans Box[/COLOR]' , iIIII1iIIii , 426 , II11IiiIII , I11Iii1 , oOOOO )
     else :
      o0OOOo = '[COLORsteelblue]' + o0OOOo + '[/COLOR]'
      o0iIiii ( o0OOOo + '-[COLORred] source Pans Box[/COLOR]' , iIIII1iIIii , 222 , II11IiiIII , I11Iii1 , oOOOO )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
      if 44 - 44: i1iIi . ooo0O . iI11I1II1I1I + ii - oOo0O0Ooo
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
      if 22 - 22: i1IiiiI1iI * oOoO0o00OO0 . ii / I1ii11iIi11i / i1iIi
      if 54 - 54: O0Oooo0O % i1iIi + oOOoOooOo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11I ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1iIIii = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( IiIi1oo00ooOoo ) . replace ( ' ' , '+' )
 if 10 - 10: ooOoO0O00 % IIiIiII11i / oOoO0o00OO0 - OOOo00oo0oO % I1ii11iIi11i - iiiiiiii1
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oO0 . update ( 0 , "" , "Checking Source Links" )
 oOOo0 = i1Oo00 ( iIIII1iIIii )
 o0oO0 . update ( 100 , "" , "Checking Source Links" )
 if 45 - 45: I1ii11iIi11i
 if oOOo0 != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
  for iIIII1iIIii , o0OOOo in IIi11i1i1iI1 :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + iIIII1iIIii ) , 222 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 27 - 27: iiiiiiii1 + I1ii11iIi11i * o0o00Oo0O / OOOo00oo0oO * Ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
iiiIiIiiIi = '{ZH},' ; ooOOo = '{IX},' ; i11i11IiI1iIi = '{LM},'
if 18 - 18: iiiiiiii1 . OoOo0o
def O0oO ( url ) :
 IiiIiiiI1 = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IiiIiiiI1 )
 for url , oO000o , o0Oo , o0OOOo in iI111i :
  Ii111 ( ( oO000o ) . replace ( 'Sezon' , ' Season ' ) + ( o0Oo ) . replace ( 'Bölüm' , ' Episode ' ) + o0OOOo , url , 8063 , '' )
  if 29 - 29: ii / I11i1ii1 + iii1i1iiiiIi - O0Oooo0O + I11i1ii1 . ooOoO0O00
  if 26 - 26: Ii - IIiIiII11i
  if 43 - 43: oOo0O0Ooo
  if 35 - 35: oOOoOooOo + iii1i1iiiiIi * ii - IIiIiII11i
def Iii1i ( url ) :
 IiiIiiiI1 = cloudflare . source ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( IiiIiiiI1 )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( o0OOOo , url , 222 , '' )
  if 50 - 50: i1iIi + i1iIi
  if 51 - 51: oOoO0o00OO0 / ii * I11i1ii1
  if 78 - 78: iiiiiiii1 / oOoO0o00OO0 . Ii
  if 69 - 69: i1IiiiI1iI - IIiIiII11i
def OOoO0oOooOo0Oo ( ) :
 if 54 - 54: oOo0O0Ooo + iiiiiiii1
 IiiIiiiI1 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IiiIiiiI1 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo , o0Oo in iI111i :
  Ii111 ( o0OOOo + '  -  ' + ( o0Oo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIIII1iIIii , 8063 , oOoooooOoO )
  if 64 - 64: iii1i1iiiiIi / ooo0O * iii1i1iiiiIi / I1ii11iIi11i + ooo0O
def I1iII1IiI11i ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo , oOoooooOoO in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 8002 , oOoooooOoO )
def OOOoOooOO0O0OooO0 ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iiI11Iii )
 for oOoooooOoO , time , url , o0OOOo , Ii1i111iI in iI111i :
  o00oOOooOOo0o ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , time ) , url , 1015 , oOoooooOoO , Ii1i111iI )
  if 4 - 4: ooOoO0O00 / oOo / ooOoO0O00 - OOOo00oo0oO + Ii - oOo
def O0oi1I1I1IIIi11 ( ) :
 if 81 - 81: iii1i1iiiiIi
 Ii111 ( 'Coronation Street' , '' , 8001 , '' )
 Ii111 ( 'Eastenders' , '' , 8002 , '' )
 Ii111 ( 'Emmerdale' , '' , 8003 , '' )
 Ii111 ( 'Hollyoaks' , '' , 8004 , '' )
 Ii111 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 21 - 21: iiiiiiii1 / OoOo0o % I11i1ii1
 if 51 - 51: i1IiiiI1iI + oOOoOooOo / oOo0O0Ooo
 if 3 - 3: iI11I1II1I1I / OoOo0o % OOOo00oo0oO . i1iIi - i1iIi
 if 55 - 55: Ii % ii + o0o00Oo0O
def I11ii1I1 ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'Holly' in o0OOOo :
   oOoooooOoO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iIIII1iIIii :
    I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIIII1iIIii . replace ( '\\/' , '/' ) , 8006 , oOoooooOoO )
   else :
    pass
    if 51 - 51: oOoO0o00OO0 % ii - ii . i1IiiiI1iI
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 97 - 97: ooOoO0O00 % i1IiiiI1iI . ooo0O * oOo0O0Ooo % IIiIiII11i
def i1O0o00o0Oo ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'East' in o0OOOo :
   oOoooooOoO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iIIII1iIIii :
    I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIIII1iIIii . replace ( '\\/' , '/' ) , 8006 , oOoooooOoO )
   else :
    pass
    if 29 - 29: oOo - I1ii11iIi11i . OOOo00oo0oO / oOo % Ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: oOOoOooOo . O0Oooo0O / IIiIiII11i % i1iIi
def O00o0oO0oO0 ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'Emmer' in o0OOOo :
   oOoooooOoO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iIIII1iIIii :
    I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIIII1iIIii . replace ( '\\/' , '/' ) , 8006 , oOoooooOoO )
   else :
    pass
    if 28 - 28: I11i1ii1 . ooo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: iI11I1II1I1I * IIiIiII11i - O0Oooo0O % O0Oooo0O - OoOo0o
def i1iiIiIi1iIII ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'Coro' in o0OOOo :
   oOoooooOoO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iIIII1iIIii :
    I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIIII1iIIii . replace ( '\\/' , '/' ) , 8006 , oOoooooOoO )
   else :
    pass
    if 90 - 90: ii . ii . oOoO0o00OO0 * i1iIi - iiiiiiii1 % oOo0O0Ooo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: iI11I1II1I1I . oOoO0o00OO0 - oOoO0o00OO0 + OOOo00oo0oO
def iIII1 ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOo0 )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'Celeb' in o0OOOo :
   oOoooooOoO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iIIII1iIIii :
    I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIIII1iIIii . replace ( '\\/' , '/' ) , 8006 , oOoooooOoO )
   else :
    pass
    if 86 - 86: I1ii11iIi11i + Ii
def iII1I11ii1III ( name , url ) :
 IIii1iIIiII = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIii1iIIiII :
  i11i1II = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iiI11Iii = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iiI11Iii ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iiI11Iii = open_url ( url )
  OO0ooo00oO = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iiI11Iii ) [ - 1 ]
  i11i1II = OO0ooo00oO . replace ( '\\/' , '/' )
 o0OoOo00ooO = xbmcgui . ListItem ( name , '' , '' )
 o0OoOo00ooO . setPath ( i11i1II )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOo00ooO )
 if 70 - 70: o0o00Oo0O - oOo - I1ii11iIi11i
 if 95 - 95: I11i1ii1 * IIiIiII11i % ooo0O * I1ii11iIi11i . i1IiiiI1iI
def ii1I11ii ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iI111i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iIIII1iIIii , 7071 , I1IIIii + 'popcorn.png' )
 for iIIII1iIIii , o0OOOo in IIi11i1i1iI1 :
  Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iIIII1iIIii , 7071 , I1IIIii + 'popcorn.png' )
  if 41 - 41: oOOoOooOo % oOoO0o00OO0 + iI11I1II1I1I
def O000ooo ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'Movies' in o0OOOo :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.snagfilms.com' + ( iIIII1iIIii ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , I1IIIii + 'popcorn.png' )
def oOOiI ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iiI11Iii )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iiI11Iii )
 for url , oOoooooOoO , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOoooooOoO )
 for url in IIi11i1i1iI1 :
  Ii111 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , I1IIIii + 'Next.png' )
  if 94 - 94: I11i1ii1 / oOOoOooOo + O0Oooo0O * OoOo0o
  if 16 - 16: oOOoOooOo - ooOoO0O00 - i1IiiiI1iI % I1ii11iIi11i * i1IiiiI1iI - iii1i1iiiiIi
def IiiIi11 ( url ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , url , oOoooooOoO in iI111i :
  if '{{' in o0OOOo :
   pass
  else :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOoooooOoO )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
OoOI1I = '{UJ},' ; Ii111Ii11I111Ii = '{WE},' ; iIiIIiIII1I = '{WP},' ; Ii1i1IiiIiIII = '{PP},'
def Oo0O0O000 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , url , oOoooooOoO in iI111i :
  if '{{' in o0OOOo :
   pass
  else :
   Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOoooooOoO )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOO0oOo0OOoOO ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  o0O00oo0Ooo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O00oo0Ooo ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 222 , I1IIIii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: ii
 if 67 - 67: Ii + iii1i1iiiiIi
 if 50 - 50: oOOoOooOo . ooOoO0O00 + oOoO0o00OO0 . OoOo0o
def oO0Ooo ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  if '(cooltvseries.com)' in o0OOOo :
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
 for url , o0OOOo in IIi11i1i1iI1 :
  if '(cooltvseries.com)' in o0OOOo :
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
def iiiiIIiiII1Iii1 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iiI11Iii )
 for url in iI111i :
  I1iiIiiii1111 ( ( url ) . replace ( ' ' , '%20' ) )
OOo0O0O000 = '{XX},' ; o0oOOoO0o0 = '{UD},' ; oOOo0o0O0oO0o = '{YT},' ; iiIioo0O0 = '{JS},' ; oooO000oO0O = '{PF},'
if 40 - 40: OoOo0o - oOo . ii - OOOo00oo0oO / oOOoOooOo + I1ii11iIi11i
def Ooo0i1i1 ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iI111i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo , oOoooooOoO in iI111i :
  I111i1i1111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( o0oOoO00o ( iIIII1iIIii ) ) , 222 , oOoooooOoO )
  if 51 - 51: i1iIi . Ii + OOOo00oo0oO % iii1i1iiiiIi
def OOoOOO0 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( iiI11Iii )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iiI11Iii )
 for oOoooooOoO , url , o0OOOo in iI111i :
  if 'youtu' in url :
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOoooooOoO )
 for url in next :
  Ii111 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , I1IIIii + 'Next.png' )
  if 97 - 97: OoOo0o . OoOo0o . iiiiiiii1 . iiiiiiii1
def Ooo0oOoOoOoo ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 40 - 40: oOoO0o00OO0 . oOo
def Ooo0oOoOoOoo ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 30 - 30: oOOoOooOo % oOo0O0Ooo . OOOo00oo0oO
def ii1i11i ( url ) :
 iiI11Iii = i11111IIIII
 iI111i = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 for url , oOoooooOoO , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 222 , oOoooooOoO )
  if 54 - 54: O0Oooo0O % o0o00Oo0O * IIiIiII11i % iiiiiiii1 % i1IiiiI1iI - oOoO0o00OO0
  if 43 - 43: oOOoOooOo % oOo . i1IiiiI1iI / O0Oooo0O - I1ii11iIi11i
  if 98 - 98: I1ii11iIi11i
  if 74 - 74: iii1i1iiiiIi . oOoO0o00OO0
  if 45 - 45: oOo + oOo0O0Ooo
def oOi1 ( ) :
 if 89 - 89: OOOo00oo0oO
 Ii111 ( 'All Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Entertainment' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Movies' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Music' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'News' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Sports' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Documentary' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Kids' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Food' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Religious' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'USA Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 Ii111 ( 'Other' , '' , 7021 , I1IIIii + 'livetv.png' )
 if 27 - 27: ooo0O
 if 13 - 13: oOoO0o00OO0 - o0o00Oo0O * OOOo00oo0oO % iI11I1II1I1I . oOo0O0Ooo - OoOo0o
def oOOooO ( Cat_Name ) :
 if 19 - 19: i1IiiiI1iI . iI11I1II1I1I + oOOoOooOo
 Iii11Ii = False
 IiiiIiiI1IIIi = '0'
 if Cat_Name == 'All Channels' : Iii11Ii = True
 if Cat_Name == 'Entertainment' : IiiiIiiI1IIIi = '1'
 if Cat_Name == 'Movies' : IiiiIiiI1IIIi = '2'
 if Cat_Name == 'Music' : IiiiIiiI1IIIi = '3'
 if Cat_Name == 'News' : IiiiIiiI1IIIi = '4'
 if Cat_Name == 'Sports' : IiiiIiiI1IIIi = '5'
 if Cat_Name == 'Documentary' : IiiiIiiI1IIIi = '6'
 if Cat_Name == 'Kids' : IiiiIiiI1IIIi = '7'
 if Cat_Name == 'Food' : IiiiIiiI1IIIi = '8'
 if Cat_Name == 'Religious' : IiiiIiiI1IIIi = '9'
 if Cat_Name == 'USA Channels' : IiiiIiiI1IIIi = '10'
 if Cat_Name == 'Other' : IiiiIiiI1IIIi = '11'
 if 89 - 89: I1ii11iIi11i % I11i1ii1 + OoOo0o - iii1i1iiiiIi . oOo0O0Ooo + oOo
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iiI11Iii )
 print 'Len Match: >>>' + str ( len ( iI111i ) )
 for o0OOOo , oOoooooOoO , I11iII in iI111i :
  II1iiIiIiiI1Ii = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOoooooOoO ) . replace ( '\\' , '' )
  if I11iII == IiiiIiiI1IIIi :
   Ii111 ( o0OOOo , '' , 7022 , II1iiIiIiiI1Ii )
  elif Iii11Ii == True :
   Ii111 ( o0OOOo , '' , 7022 , II1iiIiIiiI1Ii )
  else : pass
  if 50 - 50: oOo
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 35 - 35: iI11I1II1I1I . o0o00Oo0O / ooOoO0O00
def i111I ( Search_Name ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iiI11Iii )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iiI11Iii )
 for oOoooooOoO , iIIII1iIIii , IIi11i1II , Ii1I1 in iI111i :
  II1iiIiIiiI1Ii = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOoooooOoO ) . replace ( '\\' , '' )
  I111i1i1111 ( Search_Name + ': Link 1' , ( iIIII1iIIii ) . replace ( '\\' , '' ) , 222 , II1iiIiIiiI1Ii )
  I111i1i1111 ( Search_Name + ': Link 2' , ( IIi11i1II ) . replace ( '\\' , '' ) , 222 , II1iiIiIiiI1Ii )
  I111i1i1111 ( Search_Name + ': Link 3' , ( Ii1I1 ) . replace ( '\\' , '' ) , 222 , II1iiIiIiiI1Ii )
  if 10 - 10: oOOoOooOo % o0o00Oo0O + iI11I1II1I1I % o0o00Oo0O * OOOo00oo0oO
def O000Oo ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  I111i1i1111 ( o0OOOo , ( iIIII1iIIii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , I1IIIii + 'english.png' )
def IiiIi1II ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  I111i1i1111 ( o0OOOo , ( iIIII1iIIii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'xxx.png' )
def IiII1IiiI ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iiI11Iii )
 for o0OOOo , iIIII1iIIii in iI111i :
  I111i1i1111 ( o0OOOo , ( iIIII1iIIii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'vod(1).png' )
  if 57 - 57: OOOo00oo0oO
def i11I ( url ) :
 url
 II1I = xbmcgui . ListItem ( o0OOOo , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II1I )
 return
 if 48 - 48: oOoO0o00OO0 . IIiIiII11i * I11i1ii1 . oOo0O0Ooo * i1iIi
 if 82 - 82: iii1i1iiiiIi * oOoO0o00OO0 - ii / ooOoO0O00 + ii * i1IiiiI1iI
def OoI1iIi ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']All WorkOuts[/COLOR]' , o0oOoO00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) , 7085 , I1IIIii + 'Fitness.png' , Oo00OOOOO , '' )
 if 80 - 80: ooOoO0O00 / OoOo0o / ooo0O - I11i1ii1
def Iii11 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '"id":.+?,"title":(.+?),"is_featured":1,"minutes":(.+?),"burnmin":(.+?),"burnmax":(.+?),"burnavg":(.+?),"difficulty":(.+?),"image":"([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( '"next_page_url":"([^"]*)"' ) . findall ( iiI11Iii )
 for o0OOOo , time , iII1Ii1ii111 , iII11IIi1I1 , o00o0o , ooOoOooO0oo0o00O0 , oOoooooOoO , url , oO00Oo0 , iII11I1iIiI in iI111i :
  o00oOOooOOo0o ( ( o0OOOo ) . replace ( '"' , '' ) , 'https://www.fitnessblender.com/videos/' + url , 7086 , 'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-' + oOoooooOoO , '' , ( 'Calorie burn:[CR]' + iII1Ii1ii111 + ' - ' + iII11IIi1I1 + ' Average = ' + o00o0o + '[CR][CR]Difficulty = ' + ooOoOooO0oo0o00O0 + '[CR][CR]Equipment Needed: ' + oO00Oo0 + '[CR][CR]Focus: ' + iII11I1iIiI ) . replace ( '"' , '' ) )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
 for url in IIi11i1i1iI1 :
  Ii111 ( 'NEXT' , ( 'https://www.fitnessblender.com/videos' + url ) . replace ( '\/' , '' ) , 7085 , I1IIIii + 'Next.png' )
  if 27 - 27: ooOoO0O00 - ooOoO0O00 - i1iIi - OoOo0o
def O0OoO0OOOo ( url , iconimage , description ) :
 oOOo0 = i11111IIIII ( url )
 oOoooooOoO = iconimage
 oOOOO = description
 iI111i = re . compile ( '<div class="responsive-video">.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  O0O0ooOOO ( 'PLAY' , url , 8043 , oOoooooOoO , '' , oOOOO )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
 oO0o = re . compile ( '<div class="article__content">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i11Iiii in oO0o :
  IIIIIii1ii11 = ( I1i11Iiii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o00oOOooOOo0o ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOoooooOoO , '' , IIIIIii1ii11 )
  if 60 - 60: iI11I1II1I1I . oOoO0o00OO0 % ooo0O * OoOo0o - oOo0O0Ooo * IIiIiII11i
def o0i11iiII11i ( INFO ) :
 OoOoO ( 'info for workout' , INFO )
 if 83 - 83: I1ii11iIi11i . ooo0O + iiiiiiii1 + ooo0O % iI11I1II1I1I * iii1i1iiiiIi
 if 65 - 65: OoOo0o . IIiIiII11i * Ii + OoOo0o
 if 99 - 99: oOoO0o00OO0 % I1ii11iIi11i
def II1ii1I1 ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  Ii111 ( ( o0OOOo ) . replace ( 'SlyNet' , '' ) , url , 9031 , I1IIIii + 'Sport.png' )
def Oo0ooO0oOo0 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  Ii111 ( o0OOOo , url , 9032 , I1IIIii + 'icon.png' )
def IIiii11 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , url in iI111i :
  if '=' in o0OOOo :
   pass
  else :
   I111i1i1111 ( ( o0OOOo ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , I1IIIii + 'icon.png' )
def oO00o ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iiI11Iii )
 for o0OOOo , url in iI111i :
  if '=' in o0OOOo :
   pass
  else :
   I111i1i1111 ( o0OOOo , url , 222 , I1IIIii + 'icon.png' )
   if 76 - 76: o0o00Oo0O + IIiIiII11i * oOo
   if 1 - 1: ooo0O
   if 34 - 34: ooo0O + OoOo0o . oOo + oOo0O0Ooo + ii
def O0OOo ( url ) :
 ii1iIi1iIiI1i ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , oOoooooOoO , url in iI111i :
  if 'music' in url :
   ii1iIi1iIiI1i ( o0OOOo , url , 90036 , oOoooooOoO , oOoooooOoO , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   ii1iIi1iIiI1i ( o0OOOo , url , 90039 , oOoooooOoO , oOoooooOoO , '' , '' )
def II11 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( iiI11Iii )
 for o0OOOo , url , oOoooooOoO in iI111i :
  IIiI1I1 ( o0OOOo , url , 100009 , oOoooooOoO , oOoooooOoO , '' , '' )
  if 2 - 2: iiiiiiii1 * i1IiiiI1iI * oOOoOooOo + Ii + OOOo00oo0oO
def oOOo0ooOOoO0 ( url ) :
 ii1iIi1iIiI1i ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 iiI11Iii = requests . get ( url ) . text
 iIIiiIIIi1I = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( iiI11Iii )
 O0o0O0 = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( iiI11Iii )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O0o0O0 ) )
 for url , oOoooooOoO , o0OOOo in iI111i :
  OO0ooo0o0 = requests . get ( url ) . text
  oo0O0OO00O = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( OO0ooo0o0 )
  for IiiiIi in oo0O0OO00O :
   III1I11i1iIi = requests . get ( IiiiIi ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( III1I11i1iIi )
   for ooOO00oOOo000 , iiIiI11IiI1I , i1iII1IiiIiI1 , II1i1 , IIIi1I1IIii1II in iI111i :
    if ooOO00oOOo000 == 'xyz' :
     iiooO0OOOooo = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     IIiI1I1 ( o0OOOo , iiooO0OOOooo , 1001111 , oOoooooOoO , oOoooooOoO , '' , '' )
    else :
     iiooO0OOOooo = 'http://' + II1i1 + '.' + i1iII1IiiIiI1 + '.' + iiIiI11IiI1I + '.' + ooOO00oOOo000 + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     IIiI1I1 ( o0OOOo , iiooO0OOOooo , 1001111 , oOoooooOoO , oOoooooOoO , '' , '' )
 for OOo in iIIiiIIIi1I :
  ii1iIi1iIiI1i ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo , 1000111 , '' , '' , '' , '' )
  if 34 - 34: Ii % oOo - OOOo00oo0oO / OoOo0o / iiiiiiii1
  if 5 - 5: O0Oooo0O . OOOo00oo0oO
  if 77 - 77: iiiiiiii1 / Ii
def iiOOOO0oo ( ) :
 ii1iIi1iIiI1i ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 52 - 52: O0Oooo0O / ii - Ii
 if 53 - 53: oOo0O0Ooo * I11i1ii1 - iiiiiiii1 % oOoO0o00OO0 / ii
def oO0OO00oOO0o0 ( url , name ) :
 ii1iIi1iIiI1i ( name , '' , '' , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 iiI11Iii = requests . get ( url ) . text
 iIIiiIIIi1I = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( iiI11Iii )
 O0o0O0 = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( iiI11Iii )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O0o0O0 ) )
 for url , oOoooooOoO , name in iI111i :
  OO0ooo0o0 = requests . get ( url ) . text
  oo0O0OO00O = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( OO0ooo0o0 )
  for IiiiIi in oo0O0OO00O :
   III1I11i1iIi = requests . get ( IiiiIi ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( III1I11i1iIi )
   for ooOO00oOOo000 , iiIiI11IiI1I , i1iII1IiiIiI1 , II1i1 , IIIi1I1IIii1II in iI111i :
    if ooOO00oOOo000 == 'xyz' :
     iiooO0OOOooo = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     IIiI1I1 ( name , iiooO0OOOooo , 1001111 , oOoooooOoO , oOoooooOoO , '' , '' )
    else :
     iiooO0OOOooo = 'http://' + II1i1 + '.' + i1iII1IiiIiI1 + '.' + iiIiI11IiI1I + '.' + ooOO00oOOo000 + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     IIiI1I1 ( name , iiooO0OOOooo , 1001111 , oOoooooOoO , oOoooooOoO , '' , '' )
     if 45 - 45: ii + OoOo0o - OoOo0o - oOOoOooOo + ooo0O
 for OOo in iIIiiIIIi1I :
  ii1iIi1iIiI1i ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo , 1003111 , '' , '' , '' , '' )
  if 90 - 90: ooo0O + iI11I1II1I1I / I1ii11iIi11i + oOo0O0Ooo + OOOo00oo0oO
  if 60 - 60: oOo
def iiIIII11i1 ( ) :
 ii1iIi1iIiI1i ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 58 - 58: iiiiiiii1
 if 77 - 77: I11i1ii1 % OOOo00oo0oO % oOo
 if 68 - 68: oOOoOooOo % i1IiiiI1iI - i1iIi . oOo
def i11IIiIi ( url , name ) :
 ii1iIi1iIiI1i ( name , '' , '' , '' , '' , '' , '' )
 ii1iIi1iIiI1i ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 iiI11Iii = requests . get ( url ) . text
 iIIiiIIIi1I = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( iiI11Iii )
 O0o0O0 = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( iiI11Iii )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O0o0O0 ) )
 for url , oOoooooOoO , name in iI111i :
  OO0ooo0o0 = requests . get ( url ) . text
  oo0O0OO00O = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( OO0ooo0o0 )
  for IiiiIi in oo0O0OO00O :
   III1I11i1iIi = requests . get ( IiiiIi ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( III1I11i1iIi )
   for ooOO00oOOo000 , iiIiI11IiI1I , i1iII1IiiIiI1 , II1i1 , IIIi1I1IIii1II in iI111i :
    if ooOO00oOOo000 == 'xyz' :
     iiooO0OOOooo = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     IIiI1I1 ( name , iiooO0OOOooo , 1001111 , oOoooooOoO , oOoooooOoO , '' , '' )
    else :
     iiooO0OOOooo = 'http://' + II1i1 + '.' + i1iII1IiiIiI1 + '.' + iiIiI11IiI1I + '.' + ooOO00oOOo000 + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     IIiI1I1 ( name , iiooO0OOOooo , 1001111 , oOoooooOoO , oOoooooOoO , '' , '' )
     if 52 - 52: iii1i1iiiiIi . oOoO0o00OO0 . I1ii11iIi11i
 for OOo in iIIiiIIIi1I :
  ii1iIi1iIiI1i ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo , 1005111 , '' , '' , '' , '' )
def iIIIiI ( name , url ) :
 import urlresolver
 try :
  O00 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( O00 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 99 - 99: ii - ooOoO0O00 % ooo0O / ooo0O + I11i1ii1
 if 96 - 96: ii + OoOo0o - O0Oooo0O / OOOo00oo0oO % OOOo00oo0oO
 if 34 - 34: I11i1ii1
def o0OOO0Oo ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 iI111i = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'Daily' in o0OOOo :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 9008 , O0O )
def O0O00oo ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def iiIIIii ( url ) :
 I111i1i1111 ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 I111i1i1111 ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 I111i1i1111 ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iiI11Iii )
 for o0OOOo , url in iI111i :
  I111i1i1111 ( ( o0OOOo ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 71 - 71: OoOo0o * iii1i1iiiiIi - i1IiiiI1iI . Ii
def i1111iII1 ( ) :
 iiI11Iii = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  if '.m3u' in iIIII1iIIii :
   Ii111 ( ( o0OOOo ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + iIIII1iIIii ) , 9011 , I1IIIii + 'disclose.png' )
def I1I1iiI11I1 ( url ) :
 iiI11Iii = cloudflare . source ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iiI11Iii )
 for o0OOOo , url in iI111i :
  I111i1i1111 ( ( o0OOOo ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 36 - 36: OOOo00oo0oO - i1IiiiI1iI % i1IiiiI1iI - IIiIiII11i
def I11IIIi ( ) :
 iiI11Iii = i11111IIIII ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 iI111i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  if 'category' in iIIII1iIIii :
   Ii111 ( o0OOOo , 'http://www.disclose.tv/' + iIIII1iIIii , 7010 , I1IIIii + 'disclose.png' )
   if 5 - 5: ooOoO0O00 - oOo0O0Ooo * oOo0O0Ooo
   if 49 - 49: O0Oooo0O
def iIii ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iiI11Iii )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iiI11Iii )
 for url , o0OOOo , oOoooooOoO in iI111i :
  Ii111 ( o0OOOo , 'http://www.disclose.tv/' + url , 7011 , oOoooooOoO )
 for url in next :
  Ii111 ( 'NEXT' , url , 7010 , I1IIIii + 'Next.png' )
  if 41 - 41: OOOo00oo0oO . O0Oooo0O + o0o00Oo0O - OOOo00oo0oO . iii1i1iiiiIi * oOo
  if 6 - 6: oOOoOooOo / OOOo00oo0oO % ooo0O + oOOoOooOo / IIiIiII11i - O0Oooo0O
def O000oooiI1I1I1 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iiI11Iii )
 Ii1II1I11i1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  if 'http' in url :
   I111i1i1111 ( 'video/flv' , url , 222 , I1IIIii + 'disclose.png' )
 for url , o0OOOo in IIi11i1i1iI1 :
  I111i1i1111 ( o0OOOo , url , 222 , I1IIIii + 'disclose.png' )
 for url in Ii1II1I11i1 :
  I111i1i1111 ( 'YT Link' , url , 8043 , I1IIIii + 'disclose.png' )
  if 17 - 17: OoOo0o % ooo0O / i1iIi * Ii / o0o00Oo0O - oOoO0o00OO0
  if 93 - 93: oOOoOooOo - ii / I11i1ii1 . i1IiiiI1iI
def iII1iIiiII ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  Ii111 ( o0OOOo , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , I1IIIii + 'icon.png' )
  if 26 - 26: i1IiiiI1iI . oOoO0o00OO0
def OO00OOOO00oOO ( name , url , img ) :
 oOOo0 = i11111IIIII ( url )
 O0o0ooO0oO0oO = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oOOo0 )
 iI1iII111ii1I = len ( O0o0ooO0oO0oO )
 if 97 - 97: OOOo00oo0oO - iiiiiiii1 + I11i1ii1 . iii1i1iiiiIi + iI11I1II1I1I
 if 75 - 75: oOOoOooOo + oOOoOooOo . O0Oooo0O % iiiiiiii1 / iI11I1II1I1I * iiiiiiii1
 if iI1iII111ii1I == 1 :
  for IiIi1iIIiII1i in O0o0ooO0oO0oO :
   IiIi1iIIiII1i = IiIi1iIIiII1i . replace ( 'player' , 'watch' )
   OOoOo = IiIi1iIIiII1i + '&fv=&sou='
   i1ii = i11111IIIII ( OOoOo )
   ii11iIIiiI1I = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( i1ii )
   for oo0o0000Oo0 in ii11iIIiiI1I :
    oooOO0 = False
    Resolve ( oo0o0000Oo0 )
    if 91 - 91: oOo0O0Ooo - ii - ii
 elif iI1iII111ii1I > 1 :
  if 69 - 69: iiiiiiii1 * Ii / ooOoO0O00
  for IiIi1iIIiII1i in O0o0ooO0oO0oO :
   Oo00Oo0o000 = i11111IIIII ( IiIi1iIIiII1i )
   oOo0ooOo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oo00Oo0o000 )
   iI1i1i = oOo0ooOo
   iI1i1i = ( str ( iI1i1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iI1i1i
   I111i1i1111 ( 'DOUBLE LINK' , iI1i1i , 424 , '' )
   if 83 - 83: o0o00Oo0O
   for url in oOo0ooOo :
    Ii111 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IIi11i1II = Google . resolve ( url )
    except :
     pass
    try :
     IIIii1i = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IIi11i1II ) )
     for iIIi , IIi1I1iiiiiiI1i1i in IIIii1i :
      if 46 - 46: OoOo0o
      HD_URLS . append ( iIIi )
      SD_URLS . append ( IIi1I1iiiiiiI1i1i )
    except :
     pass
 else :
  pass
  if 64 - 64: oOo0O0Ooo / iii1i1iiiiIi
def Ii11Ii1i1 ( ) :
 if 18 - 18: Ii . o0o00Oo0O / oOo * OOOo00oo0oO + O0Oooo0O
 if 91 - 91: oOo0O0Ooo
 Ii111 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , I1IIIii + 'Movies.png' )
 if 84 - 84: o0o00Oo0O % i1iIi
 Ii111 ( 'Search Movies' , '' , 7017 , I1IIIii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 3 - 3: oOo0O0Ooo . i1IiiiI1iI / oOoO0o00OO0
 if 2 - 2: I11i1ii1 + i1IiiiI1iI / iI11I1II1I1I . Ii . ooOoO0O00 * oOOoOooOo
def IIoOoo0oooo ( ) :
 iiI11Iii = i11111IIIII ( 'http://cnfstudio.com/' )
 iI111i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( o0OOOo , 'http://cnfstudio.com/genre/' + iIIII1iIIii , 7003 , I1IIIii + 'icon.png' )
  if 23 - 23: I1ii11iIi11i / oOOoOooOo
iI111I11I1I1 = xbmcgui . Dialog ( )
if 80 - 80: i1IiiiI1iI
IiiiIiOooOOo0 = '{UN},' ; OOO0O0 = '{IG},' ; IIiIiI1I = '{PL},' ; iIi1i1Ii11III = '{LO},' ; iIi11i1111I = '{LP},' ; OO00O0 = '{HA},' ; O0oo00O0ooOo = '{XD},' ; I11Iii1iIII1i = '{TA},' ; ooOOO000 = '{DP},' ; i1Ii1IiIii1I = '{JT},' ; i1iIII1Ii1 = '{JJ},' ; o0Oo00OoO000O = '{MM},' ; II1iii = '{FQ},' ; O0oOOOO0o = '{HH},'
if 65 - 65: IIiIiII11i + OOOo00oo0oO + OoOo0o + I11i1ii1 + ooOoO0O00
def I1iiI1IiI1iii ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iiI11Iii )
 i1Ii1IiiI = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iiI11Iii )
 for oOoooooOoO , url , o0OOOo in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOoooooOoO )
 i1Ii1IiiI = i1Ii1IiiI
 for url in i1Ii1IiiI :
  Ii111 ( 'Next Page' , url , 7003 , I1IIIii + 'Next.png' )
  if 80 - 80: oOOoOooOo % I11i1ii1
def iioo ( url ) :
 if 66 - 66: i1iIi - oOo0O0Ooo . ii * O0Oooo0O
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  IIIi1I1IIii1II = url + '&fv=&sou='
  IIIi1I1IIii1II = IIIi1I1IIii1II . replace ( 'player' , 'watch' )
  I11IIi11Iii1 = o0oooooooO0o ( IIIi1I1IIii1II )
  O0OI1i = o0oooooooO0o ( url )
  if 50 - 50: i1IiiiI1iI . oOoO0o00OO0
  if 31 - 31: iI11I1II1I1I . OoOo0o * oOOoOooOo . iiiiiiii1 - o0o00Oo0O . iI11I1II1I1I
def o0oooooooO0o ( url ) :
 if 54 - 54: iI11I1II1I1I / OoOo0o + OOOo00oo0oO % iii1i1iiiiIi * iii1i1iiiiIi - IIiIiII11i
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iiI11Iii )
 for url in iI111i :
  O00o0o ( url )
  if 43 - 43: i1iIi / O0Oooo0O . OOOo00oo0oO + iI11I1II1I1I
  if 99 - 99: oOoO0o00OO0
def iI1iiiIIIIIiIii1 ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , I1IIIii + 'LocalM3U.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , I1IIIii + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 50 - 50: iI11I1II1I1I . I1ii11iIi11i
def III1iI1III1I1 ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  i1II11iII11iI = open ( O0OoO000O0OO , 'r' )
  for II1I in i1II11iII11iI :
   i1IIi1 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( II1I )
   for o0OOOo , iIIII1iIIii in i1IIi1 :
    I111i1i1111 ( o0OOOo , iIIII1iIIii , 222 , I1IIIii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 48 - 48: I11i1ii1 . IIiIiII11i - Ii * iiiiiiii1
def Ooo0O00 ( url ) :
 if os . path . exists ( Remote ) :
  oOOo0 = I1I1i ( url )
  iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
  for o0OOOo , url in iI111i :
   url = ( url ) . strip ( )
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 1 - 1: oOo % OoOo0o - iiiiiiii1 * iI11I1II1I1I
  if 14 - 14: iii1i1iiiiIi
def Iii1I1I11iiI1 ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for iIIII1iIIii in iI111i :
  iIIII1iIIii = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iIIII1iIIii
 o0OOOo = 'plugin.video.GenieTv'
 if 17 - 17: I1ii11iIi11i . ii % oOoO0o00OO0 / ii
 oO0OOOOo ( iIIII1iIIii , o0OOOo )
 if 28 - 28: i1iIi
def o0OOOO00O0Oo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for iIIII1iIIii in iI111i :
  iIIII1iIIii = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iIIII1iIIii
 o0OOOo = 'repository.GenieTv'
 if 27 - 27: I1ii11iIi11i . i1IiiiI1iI % oOo0O0Ooo * Ii
 oO0OOOOo ( iIIII1iIIii , o0OOOo )
 if 86 - 86: oOOoOooOo / O0Oooo0O * OOOo00oo0oO . O0Oooo0O - Ii
 if 93 - 93: O0Oooo0O - I1ii11iIi11i
def IIiiI1iiI ( ) :
 iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , iiIi11iI1iii )
 if oo000o0000oO == 0 :
  OoO0o ( )
 if oo000o0000oO == 1 :
  OOoO0ooo ( )
  if 51 - 51: Ii - oOo0O0Ooo / oOoO0o00OO0 * i1IiiiI1iI
  if 3 - 3: oOoO0o00OO0 + iI11I1II1I1I . OoOo0o / i1IiiiI1iI % O0Oooo0O / ooOoO0O00
  if 73 - 73: iiiiiiii1 . oOOoOooOo - i1iIi * oOoO0o00OO0
  if 31 - 31: IIiIiII11i - i1IiiiI1iI - OOOo00oo0oO * OOOo00oo0oO + OoOo0o
O0oo0OO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
i1111 = xbmc . translatePath ( 'special://home/' )
o0oO0 = xbmcgui . DialogProgress ( )
iIiiiiIi1 = 'https://addons.tvaddons.ag/'
if 38 - 38: oOo0O0Ooo . o0o00Oo0O + OoOo0o / oOoO0o00OO0 . iI11I1II1I1I - ooOoO0O00
def OOoO0ooo ( ) :
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 iI11IIi1iiI1I = 'https://addons.tvaddons.ag/search/?keyword=' + oo0oO0
 oOOo0 = i11111IIIII ( iI11IIi1iiI1I )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for iIIII1iIIii , Oo0Oo0O , o0OOOo in iI111i :
  o00oOOooOOo0o ( o0OOOo , iIIII1iIIii , 10054 , 'https://addons.tvaddons.ag/' + Oo0Oo0O , Oo00OOOOO , '' )
  if 3 - 3: I1ii11iIi11i + OOOo00oo0oO
  if 65 - 65: oOo0O0Ooo / iii1i1iiiiIi % oOo0O0Ooo * Ii * ii / i1IiiiI1iI
def OoO0o ( ) :
 oOOo0 = i11111IIIII ( iIiiiiIi1 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  if 'Repositories' in o0OOOo :
   pass
  elif 'Services' in o0OOOo :
   pass
  elif 'International' in o0OOOo :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , iIIII1iIIii , 10053 , 'https://addons.tvaddons.ag/' + oOoooooOoO , Oo00OOOOO , '' )
   if 91 - 91: Ii / Ii
   if 9 - 9: i1IiiiI1iI / O0Oooo0O + iI11I1II1I1I + oOo0O0Ooo - IIiIiII11i
def Addon ( url ) :
 oOOo0 = i11111IIIII ( url )
 iIIiiIIIi1I = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for url , oOoooooOoO , o0OOOo in iI111i :
  if 'Please' in o0OOOo :
   pass
  else :
   O0O0ooOOO ( o0OOOo , url , 10054 , 'https://addons.tvaddons.ag/' + oOoooooOoO , Oo00OOOOO , '' )
 for url in iIIiiIIIi1I :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
  if 96 - 96: iiiiiiii1 + I1ii11iIi11i - ii . ooOoO0O00 + ooOoO0O00 % iI11I1II1I1I
  if 80 - 80: ii / o0o00Oo0O / O0Oooo0O - I1ii11iIi11i . Ii
def II11IIiii ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oO0 = xbmcgui . DialogProgress ( )
   o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   I1iii = os . path . join ( O0oooo00o0Oo , name + '.zip' )
   try :
    os . remove ( I1iii )
   except :
    pass
   downloader . download ( url , I1iii , o0oO0 )
   oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oO0o0O0Ooo0o
   print '======================================='
   extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
   IioO0oOOO0Ooo ( )
   if 14 - 14: oOo0O0Ooo
def oO0OOOOo ( url , name ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I1iii = os . path . join ( O0oooo00o0Oo , name + '.zip' )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 oO0o0O0Ooo0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0o0O0Ooo0o
 print '======================================='
 extract . all ( I1iii , oO0o0O0Ooo0o , o0oO0 )
 IioO0oOOO0Ooo ( )
 if 41 - 41: O0Oooo0O % ooOoO0O00 + oOo / OOOo00oo0oO
def IioO0oOOO0Ooo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 48 - 48: ooOoO0O00 . I1ii11iIi11i . ooOoO0O00 . oOoO0o00OO0 * oOo0O0Ooo - i1iIi
 if 83 - 83: ii
def IIoOOOoOoOO ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
 for url , Oo0Oo0O , o0OOOo in iI111i :
  Ii111 ( o0OOOo , url , 1007 , Oo0Oo0O )
def iI1iIII1i1II ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
 for url , Oo0Oo0O , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 1006 , Oo0Oo0O )
  if 90 - 90: i1iIi / i1IiiiI1iI
def o0OO ( ) :
 iiI11Iii = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , II11IiiIII , oOOOO , OoOo00o0OO , o0OOOo in iI111i :
  IiIiI1i1ii ( o0OOOo , 100109 , iIIII1iIIii , image = II11IiiIII , isFolder = True )
  if 92 - 92: oOo0O0Ooo . i1IiiiI1iI / oOo * i1iIi
def iIi111 ( url ) :
 import random
 II1Iiiii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 II1Iiiii . clear ( )
 iiI1111IIIi = [ ]
 iIi1ii1iIIi1 = [ ]
 iiiI11iii11iI = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for IIi11i1II , II11IiiIII , oOOOO , OoOo00o0OO , o0OOOo in iI111i :
  iiI1111IIIi . append ( [ IIi11i1II , o0OOOo ] )
  if len ( iiI1111IIIi ) == len ( iI111i ) :
   for II1I in iiI1111IIIi :
    iiIiIIIIiiIIIii = random . randint ( 1 , len ( iiI1111IIIi ) )
    try :
     OOO0o = iiI1111IIIi [ int ( iiIiIIIIiiIIIii ) ]
    except :
     pass
    if len ( iIi1ii1iIIi1 ) <= 20 :
     if OOO0o [ 1 ] not in iiiI11iii11iI :
      oo00O00oO = i11111IIIII ( OOO0o [ 0 ] )
      Ii1II1I11i1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oo00O00oO )
      for OOI1i11i , iiiI1I in Ii1II1I11i1 :
       ooo00OOOooO = i11111IIIII ( OOI1i11i )
       iIiiii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( ooo00OOOooO )
       for Ii1Ii , IIIi1I1IIii1II in iIiiii :
        if 'panda' in IIIi1I1IIii1II :
         OooOOOoOoo0O0 = i11111IIIII ( IIIi1I1IIii1II )
         O0000OOO0 = re . compile ( "url: '(.+?)'" ) . findall ( OooOOOoOoo0O0 )
         for i1111II1iIII in O0000OOO0 :
          if 'http' in i1111II1iIII :
           o0OoOo00ooO = xbmcgui . ListItem ( OOO0o [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : OOO0o [ 1 ] } )
           o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
           II1Iiiii . add ( i1111II1iIII , o0OoOo00ooO )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOo00ooO )
           if 29 - 29: oOo0O0Ooo
def IiIiI1i1ii ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 Ii1I1I1i11ii = sys . argv [ 0 ]
 Ii1I1I1i11ii += '?mode=' + str ( mode )
 Ii1I1I1i11ii += '&title=' + urllib . quote_plus ( name )
 Ii1I1I1i11ii += '&image=' + urllib . quote_plus ( image )
 Ii1I1I1i11ii += '&page=' + str ( page )
 if url != '' :
  Ii1I1I1i11ii += '&url=' + urllib . quote_plus ( url )
 if keyword :
  Ii1I1I1i11ii += '&keyword=' + urllib . quote_plus ( keyword )
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  o0OoOo00ooO . addContextMenuItems ( contextMenu )
 if infoLabels :
  o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
 o0OoOo00ooO . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = isFolder )
 if 3 - 3: i1IiiiI1iI
 if 46 - 46: oOoO0o00OO0 * O0Oooo0O - iI11I1II1I1I
def I1I1I1IIi1III ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
 for url , iconimage , oOOOO , OoOo00o0OO , name in iI111i :
  if 'http' in url :
   if '.php' in url :
    OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
    for II1I in OooOooO0O0o0 :
     if II1I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OoO00O00O0 ( name , url , 1016 , iconimage , OoOo00o0OO , oOOOO )
   else :
    if 'youtube' in url :
     OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for II1I in OooOooO0O0o0 :
      if II1I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0iIiii ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , OoOo00o0OO , oOOOO )
    else :
     OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for II1I in OooOooO0O0o0 :
      if II1I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0iIiii ( name , url , 222 , iconimage , OoOo00o0OO , oOOOO )
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
  else :
   IiIIooO00oOo0 ( url , iconimage , name )
   if 42 - 42: oOo0O0Ooo * ooo0O / o0o00Oo0O . IIiIiII11i
 else :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
  for url , Oo0Oo0O , name in iI111i :
   if 'http' in url :
    if '.php' in url :
     Ii111 ( name , url , 1016 , Oo0Oo0O )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      I111i1i1111 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0Oo0O )
     else :
      OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
      for II1I in OooOooO0O0o0 :
       if II1I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      I111i1i1111 ( name , url , 222 , Oo0Oo0O )
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
   else :
    IiIIooO00oOo0 ( url , Oo0Oo0O , name )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 88 - 88: ii % IIiIiII11i + I11i1ii1 + I11i1ii1 * I1ii11iIi11i
def IiIIooO00oOo0 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ooO00O00o0O0o = ( url ) . replace ( ooOOo , 'http' ) . replace ( o0oOOoO0o0 , '.com' ) ;
 ii1I11iiI = ( ooO00O00o0O0o ) . replace ( i11i11IiI1iIi , 'a' ) . replace ( II1I1I1iIiiIi , 'b' ) . replace ( i1i1I11II1Ii , 'c' ) . replace ( Ii111Ii11I111Ii , 'd' ) . replace ( IIiIiI1I , 'e' ) . replace ( i1Ii1IiIii1I , 'f' ) ;
 IIIi1 = ( ii1I11iiI ) . replace ( OOo0O0O000 , 'g' ) . replace ( OO00O0 , 'h' ) . replace ( oOOo0o0O0oO0o , 'i' ) . replace ( oooO000oO0O , 'j' ) . replace ( O0o00 , 'k' ) . replace ( Ii1I1I , 'l' ) ;
 iIIIiiI = ( IIIi1 ) . replace ( o0oOo0O0o0oO , 'm' ) . replace ( O00o000O0O0oO , 'n' ) . replace ( iIiI111ii , 'o' ) . replace ( IiIoOO0ooO000 , 'p' ) . replace ( ooI11 , 'q' ) . replace ( OOoOo0Oo , 'r' ) ;
 oOo0o0O = ( iIIIiiI ) . replace ( I1I1Ii111 , 's' ) . replace ( iIiIIiIII1I , 't' ) . replace ( o0o0o0oO0oOoo , 'u' ) . replace ( Ooi1I11i1 , 'v' ) . replace ( II1iiiii , 'w' ) . replace ( iI11iIiIiiiI , 'x' ) ;
 I1oo0Oo = ( oOo0o0O ) . replace ( I1OO0Oo0 , 'y' ) . replace ( iI1IIiI1 , 'z' ) . replace ( IiiiIiOooOOo0 , '.' ) . replace ( OOO0O0 , '(' ) . replace ( iIi1i1Ii11III , ')' ) . replace ( iIi11i1111I , '/' ) ;
 iIIii111i1 = ( I1oo0Oo ) . replace ( iiiIiIiiIi , '1' ) . replace ( Ii1i1IiiIiIII , '2' ) . replace ( iIIIIi , '3' ) . replace ( I11Iii1iIII1i , '4' ) . replace ( ooOOO000 , '5' ) . replace ( iiIioo0O0 , '6' ) ;
 iiI1 = ( iIIii111i1 ) . replace ( i1iIII1Ii1 , '7' ) . replace ( o0Oo00OoO000O , '8' ) . replace ( II1iii , '9' ) . replace ( O0oOOOO0o , '0' ) . replace ( O0O0oOoO0O0oO , ':' ) . replace ( iIiIoO00OooO00O0o , '%' ) ;
 url = ( iiI1 ) . replace ( OoOI1I , '-' ) . replace ( O0oo00O0ooOo , '_' ) ;
 I111i1i1111 ( name , url , 222 , iconimage ) ;
 if 51 - 51: OoOo0o + o0o00Oo0O
 if 91 - 91: Ii + ooo0O % oOo / OOOo00oo0oO - ooOoO0O00
def O0ii1IIIiiI1i ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , Oo0Oo0O , o0OOOo in iI111i :
  Ii111 ( o0OOOo , iIIII1iIIii , 1007 , Oo0Oo0O )
def Iiii1I ( url ) :
 if 20 - 20: oOoO0o00OO0 - I11i1ii1 + OOOo00oo0oO * ooOoO0O00 % iiiiiiii1 * oOOoOooOo
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
 for url , Oo0Oo0O , o0OOOo in iI111i :
  Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 1006 , Oo0Oo0O )
  if 80 - 80: oOOoOooOo * I11i1ii1 . ooo0O
def iI1i1iIii1 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1 )
 if 72 - 72: OoOo0o / iii1i1iiiiIi
 if 89 - 89: OoOo0o + OoOo0o * iii1i1iiiiIi + iiiiiiii1 % O0Oooo0O % O0Oooo0O
def O0O000oOO0 ( url ) :
 iiI11Iii = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI11Iii )
 for url , oOoooooOoO , o0OOOo in iI111i :
  if '-dir-' in o0OOOo :
   Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOoooooOoO )
  else :
   Ii111 ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' , url , 1006 , oOoooooOoO )
   if 68 - 68: I1ii11iIi11i + oOo % oOo % iii1i1iiiiIi
def II1i1iIIi1 ( url ) :
 iiI11Iii = I1I1i ( url )
 i1I1I1i1I1 = ( 'http://afewbitsmore.com/' )
 iI111i = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  if '[To Parent Directory]' in o0OOOo :
   o0OOOo = 'HOME'
   pass
  elif 'HOME' in o0OOOo :
   pass
  elif '.m3u' in o0OOOo :
   Ii111 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , i1I1I1i1I1 + url , 2002 , I1IIIii + 'music.png' )
  elif '.mp3' in o0OOOo :
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , i1I1I1i1I1 + url , 222 , I1IIIii + 'music.png' )
  elif '.m4a' in o0OOOo :
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , i1I1I1i1I1 + url , 222 , I1IIIii + 'music.png' )
  else :
   Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) , i1I1I1i1I1 + url , 1012 , I1IIIii + 'music.png' )
def IioooO ( url ) :
 oOOo0 = I1I1i ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for oOoooooOoO , o0OOOo , url in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , I1IIIii + 'music.png' )
  if 65 - 65: O0Oooo0O
def Ii1oo ( url ) :
 iiI11Iii = I1I1i ( url )
 i1I1I1i1I1 = url
 iI111i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  if '.mp3' in o0OOOo :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , I1IIIii + 'music.png' )
  else :
   Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '/' , '' ) , i1I1I1i1I1 + url , 1011 , I1IIIii + 'music.png' )
def I111I11iiI ( ) :
 iiI11Iii = I1I1i ( o0oOoO00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iI111i = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iiI11Iii )
 for iIIII1iIIii , oOoooooOoO , o0OOOo in iI111i :
  Ii111 ( o0OOOo , ( 'http://www.cyn.net/music/' + iIIII1iIIii ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOoooooOoO ) . replace ( ' ' , '%20' ) )
def oOoOOooo0OOO ( url , img ) :
 iiI11Iii = I1I1i ( url )
 IIi11i1II = url
 img = img
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( IIi11i1II + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 86 - 86: ii / o0o00Oo0O * iii1i1iiiiIi * OoOo0o . oOo
def IiI1i1i1 ( url ) :
 iiI11Iii = I1I1i ( url )
 IIi11i1II = url
 iI111i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iiI11Iii )
 for type , url , o0OOOo in iI111i :
  if '[VID]' in type :
   I111i1i1111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , IIi11i1II + url , 222 , I1IIIii + 'music.png' )
  if '[DIR]' in type :
   IiI1i1i1 ( IIi11i1II + url )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: ooo0O / I11i1ii1 / oOOoOooOo * iii1i1iiiiIi
 if 13 - 13: iiiiiiii1
def I1iI1iiI1Ii1 ( ) :
 i1iiIIiiiII = ( o0oOoO00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IiIi1oo00ooOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO0 = IiIi1oo00ooOoo . lower ( )
 iIIII1iIIii = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 o0OOOOOo0 = ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IIi11i1II = ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 69 - 69: Ii - Ii + i1IiiiI1iI / oOo0O0Ooo % oOoO0o00OO0
 oOOo0 = i1Oo00 ( iIIII1iIIii )
 iiIIi1 = i1Oo00 ( o0OOOOOo0 )
 oo00O00oO = i1Oo00 ( IIi11i1II )
 if 56 - 56: iI11I1II1I1I / oOo * OoOo0o
 if oOOo0 != 'Failed' :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for iIIII1iIIii , II11IiiIII , oOOOO , I11Iii1 , o0OOOo in iI111i :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , iIIII1iIIii , 1016 , II11IiiIII , OoOo00o0OO , oOOOO )
    if 73 - 73: ii % I11i1ii1 / O0Oooo0O * i1IiiiI1iI + ooOoO0O00 % Ii
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iiIIi1 != 'Failed' :
  oOoOOOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiIIi1 )
  for iIIII1iIIii , o0OOOo in oOoOOOo :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + iIIII1iIIii ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
    if 91 - 91: Ii
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( oo00O00oO )
  for iIIII1iIIii , o0OOOo in IIi11i1i1iI1 :
   if IiIi1oo00ooOoo in o0OOOo . lower ( ) :
    Ii111 ( ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + iIIII1iIIii ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
    if 6 - 6: o0o00Oo0O - iI11I1II1I1I + O0Oooo0O . ooo0O * Ii
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: OoOo0o / oOo0O0Ooo / OOOo00oo0oO * OoOo0o / ooOoO0O00 - O0Oooo0O
    if 71 - 71: o0o00Oo0O + I1ii11iIi11i % OOOo00oo0oO - ooo0O
    if 82 - 82: iI11I1II1I1I
    if 64 - 64: oOOoOooOo + oOo0O0Ooo % OoOo0o + IIiIiII11i
    if 46 - 46: oOo0O0Ooo
    if 72 - 72: iiiiiiii1
o0oOo0O0o0oO = '{SF},' ; O00o000O0O0oO = '{IF},' ; iIiI111ii = '{PW},' ; iIIIIi = '{AM},' ; IiIoOO0ooO000 = '{GF},' ; ooI11 = '{DD},' ; OOoOo0Oo = '{UO},' ; I1I1Ii111 = '{LE},' ; o0o0o0oO0oOoo = '{ZY},' ; Ooi1I11i1 = '{UE},' ; II1iiiii = '{PE},' ; iI11iIiIiiiI = '{JE},' ; I1OO0Oo0 = '{TH},' ; iI1IIiI1 = '{LK},'
if 100 - 100: oOo0O0Ooo
if 55 - 55: ooOoO0O00 % I11i1ii1
def IIiiI11iI ( ) :
 iiI11Iii = i11111IIIII ( 'http://www.iwatchseries.me/tv-list/' )
 iI111i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( o0OOOo , iIIII1iIIii , 8021 , I1IIIii + 'iwatch.png' )
  iIiIi11 ( 'movies' , 'MAIN' )
def IIi1III1II ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iiI11Iii )
 for url , o0OOOo , iI in iI111i :
  Ii111 ( o0OOOo + iI , url , 8022 , I1IIIii + 'iwatch.png' )
def o0o0OOOO ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iiI11Iii )
 for url in iI111i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1i1iiIII1i1 ( url )
def I1i1iiIII1i1 ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iiI11Iii )
 IIi11i1i1iI1 = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iiI11Iii )
 Ii1II1I11i1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iiI11Iii )
 iIiiii = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  I111i1i1111 ( 'VidSpot - ' + o0OOOo , url , 222 , I1IIIii + 'iwatch.png' )
 for url in IIi11i1i1iI1 :
  I111i1i1111 ( 'VodLocker' , url , 222 , I1IIIii + 'iwatch.png' )
 for url , o0OOOo in iIiiii :
  I111i1i1111 ( 'VidUp' + o0OOOo , url , 222 , I1IIIii + 'iwatch.png' )
 for o0OOOo , url in Ii1II1I11i1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   I111i1i1111 ( 'TheVideo - ' + o0OOOo , url , 222 , I1IIIii + 'iwatch.png' )
   if 20 - 20: I1ii11iIi11i . ii % OOOo00oo0oO - OoOo0o
def OoOooOOooO ( ) :
 iiI11Iii = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 iI111i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( o0OOOo , iIIII1iIIii , 1021 , I1IIIii + 'anime.png' )
  if 50 - 50: ii - oOoO0o00OO0
  if 96 - 96: O0Oooo0O / O0Oooo0O * i1iIi / iI11I1II1I1I
def oOO0o00 ( ) :
 iiI11Iii = i11111IIIII ( 'http://www.animetoon.org/cartoon' )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iiI11Iii )
 for iIIII1iIIii , o0OOOo in iI111i :
  Ii111 ( o0OOOo , iIIII1iIIii , 1002 , I1IIIii + 'anime.png' )
  if 87 - 87: ooo0O . iI11I1II1I1I . oOOoOooOo
  if 53 - 53: I11i1ii1
  if 37 - 37: i1IiiiI1iI
def ii1I1IIiii ( url ) :
 iiI11Iii = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iiI11Iii )
 for oOoooooOoO in IIi11i1i1iI1 :
  O0OO0 = oOoooooOoO
 Ii1II1I11i1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iiI11Iii )
 for url in Ii1II1I11i1 :
  Ii111 ( 'NEXT PAGE' , url , 1002 , I1IIIii + 'Next.png' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI11Iii )
 for url , o0OOOo in iI111i :
  Ii111 ( o0OOOo , url , 1003 , O0OO0 )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1io0ooO0OO ( url , IMAGE ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iiI11Iii )
 for o0OOOo , url in iI111i :
  print o0OOOo + '     ' + url
  if 'easy' in url :
   I1IiI1i1Iii ( url )
  elif 'playpanda' in url :
   I1IiI1i1Iii ( url )
   if 27 - 27: i1IiiiI1iI + iI11I1II1I1I
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1IiI1i1Iii ( url ) :
 iiI11Iii = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( iiI11Iii )
 for url in iI111i :
  I111i1i1111 ( 'STREAM' , url , 222 , I1IIIii + 'anime.png' )
  if 71 - 71: iii1i1iiiiIi + OOOo00oo0oO % OoOo0o * oOo0O0Ooo
  if 89 - 89: i1iIi % O0Oooo0O / I1ii11iIi11i * i1iIi + iii1i1iiiiIi
def i1Ii1iiiIIII ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i . add_header ( 'referer' , url )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 83 - 83: ii * IIiIiII11i % ii
def I1I1i ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 30 - 30: O0Oooo0O / ooo0O + ii + iii1i1iiiiIi + oOo
def ii11IoOo0O0Oo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o00oooo0 = ( '%s%s' % ( o0O00o0o , url ) )
 IIIi1I1IIii1II = I1I1i ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , Oo0Oo0O , o0OOOo in iI111i :
  I111i1i1111 ( '%s' % ( '[COLOR' + iiI1IiI + ']' + o0OOOo + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , Oo0Oo0O )
  if 83 - 83: oOOoOooOo / oOo
def oO00oo0o ( url ) :
 if O0oo0OO0 . getSetting ( 'down' ) == 'true' :
  i1iIi11 ( url , o0OOOo )
 else :
  i11IIIiI1I ( url )
def i11IIIiI1I ( url ) :
 import urlresolver
 try :
  O00 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( O00 , xbmcgui . ListItem ( o0OOOo ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( o0OOOo ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def O00o0o ( url ) :
 if 76 - 76: oOo % iii1i1iiiiIi * oOOoOooOo . oOo0O0Ooo
 OOO0o0 = open ( O0Oo000ooO00 , "a" )
 OOO0o0 . write ( 'url="' + url + '"\n' )
 OOO0o0 . close
 if 64 - 64: oOOoOooOo % oOoO0o00OO0 . oOo . oOOoOooOo + Ii . iI11I1II1I1I
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 import urlresolver
 try : o0000o0Oo . play ( url )
 except : pass
 from urlresolver import common
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'LOADING' , 'Opening %s Now' % ( o0OOOo ) )
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oO0 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : o0000o0Oo . play ( url )
  except : pass
  try : O0oo0OO0 . resolve_url ( url )
  except : pass
  o0oO0 . close ( )
def i1iIi11 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  Ooo0O0ooo0o = '.mp4'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.mkv' in url :
  Ooo0O0ooo0o = '.mkv'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.mp3' in url :
  Ooo0O0ooo0o = '.mp3'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.avi' in url :
  Ooo0O0ooo0o = '.avi'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.mov' in url :
  Ooo0O0ooo0o = '.mov'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.mpeg' in url :
  Ooo0O0ooo0o = '.mpeg'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.mpg' in url :
  Ooo0O0ooo0o = '.mpg'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.flv' in url :
  Ooo0O0ooo0o = '.flv'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 elif '.wmv' in url :
  Ooo0O0ooo0o = '.wmv'
  iiIi11iI1iii = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oo000o0000oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , iiIi11iI1iii )
  if oo000o0000oO == 0 :
   i11IIIiI1I ( url )
  if oo000o0000oO == 1 :
   oooOoO0oOo00o ( url , name , Ooo0O0ooo0o )
 else :
  i11IIIiI1I ( url )
def oooOoO0oOo00o ( url , name , cat ) :
 i1i11iiIIi1I ( )
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( II ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 I1iii = os . path . join ( O0oooo00o0Oo , file )
 try :
  os . remove ( I1iii )
 except :
  pass
 downloader . download ( url , I1iii , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def i1i11iiIIi1I ( ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( II ) )
 if not os . path . exists ( II ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
def iI1Ii ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oO0 . update ( 0 , '%s' % o0OOOo )
 xbmc . sleep ( 1 )
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 o0oO0 . update ( 100 , '%s' % o0OOOo )
 xbmc . sleep ( 1 )
 o0000o0Oo . play ( url ) . strip ( )
 o0oO0 . close ( )
 if 67 - 67: o0o00Oo0O
def I1iiIiiii1111 ( url ) :
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : o0000o0Oo . play ( url ) . strip ( )
 except : pass
 if 37 - 37: i1IiiiI1iI / I1ii11iIi11i
def I1111OoO0O ( url ) :
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 import urlresolver
 IIi1 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 o0000o0Oo . play ( IIi1 )
 xbmc . sleep ( 1 )
 o0000o0Oo . play ( url )
 if 14 - 14: oOo * ii
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . iii1i1iiiiIi
def ooo0O0OOo0OoO ( ) :
 try :
  O00oo0ooo0O = getSet ( "core-player" )
  if ( O00oo0ooo0O == 'DVDPLAYER' ) : iiIi1i1iI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O00oo0ooo0O == 'MPLAYER' ) : iiIi1i1iI = xbmc . PLAYER_CORE_MPLAYER
  elif ( O00oo0ooo0O == 'PAPLAYER' ) : iiIi1i1iI = xbmc . PLAYER_CORE_PAPLAYER
  else : iiIi1i1iI = xbmc . PLAYER_CORE_AUTO
 except : iiIi1i1iI = xbmc . PLAYER_CORE_AUTO
 return iiIi1i1iI
 return True
 if 34 - 34: i1IiiiI1iI
def Ii111 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1I11i = [ ]
  ii1I11i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   ii1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOo00ooO . addContextMenuItems ( ii1I11i )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = True )
 return OoOo0oO0o
 if 95 - 95: oOo0O0Ooo . OOOo00oo0oO
def iii11III1I ( name , url , mode , iconimage , fanart , description ) :
 if 60 - 60: iiiiiiii1
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = True )
 return OoOo0oO0o
 if 92 - 92: ooOoO0O00 + O0Oooo0O % ooOoO0O00 * iiiiiiii1 % ooo0O
def I111i1i1111 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1I11i = [ ]
  ii1I11i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   ii1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOo00ooO . addContextMenuItems ( ii1I11i )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = False )
 return OoOo0oO0o
 if 56 - 56: oOo0O0Ooo / OoOo0o * o0o00Oo0O - iiiiiiii1 + I1ii11iIi11i + I11i1ii1
 if 15 - 15: iI11I1II1I1I % IIiIiII11i
 if 48 - 48: iii1i1iiiiIi + o0o00Oo0O - IIiIiII11i % IIiIiII11i . IIiIiII11i
 if 90 - 90: OOOo00oo0oO % I11i1ii1 / O0Oooo0O + o0o00Oo0O
 if 4 - 4: oOOoOooOo . iI11I1II1I1I + oOo0O0Ooo - oOo
 if 69 - 69: OoOo0o
def i111iiiI1iiI ( url , heading , announce ) :
 class OoOoO ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   self . image = xbmcgui . ControlImage ( 800 , 600 , 1200 , 450 , url , aspectRatio = 2 )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . addControl ( self . image )
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : oOo0oO = open ( announce ) ; iio00O0o00oo = oOo0oO . read ( )
   except : iio00O0o00oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iio00O0o00oo ) )
   return
 OoOoO ( )
 OoOoO ( )
def O0O0OOOOoo ( heading , announce ) :
 class OoOoO ( ) :
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
   try : oOo0oO = open ( announce ) ; iio00O0o00oo = oOo0oO . read ( )
   except : iio00O0o00oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iio00O0o00oo ) )
   return
 OoOoO ( )
 OoOoO ( )
def OooooO0oOO ( ) :
 i111iiiI1iiI ( I1IIIii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 23 - 23: oOoO0o00OO0 . oOoO0o00OO0 / oOo0O0Ooo . ooOoO0O00
 if 47 - 47: Ii . ooo0O . Ii + oOo0O0Ooo - oOoO0o00OO0
 if 62 - 62: ii + oOo0O0Ooo / oOOoOooOo . i1iIi . I1ii11iIi11i
 if 81 - 81: OOOo00oo0oO + I11i1ii1
 if 75 - 75: o0o00Oo0O + oOoO0o00OO0
def IioO0oOOO0Ooo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 51 - 51: ooOoO0O00 + IIiIiII11i % OOOo00oo0oO
 if 72 - 72: OoOo0o + OoOo0o
 if 30 - 30: i1IiiiI1iI
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / i1iIi
 if 11 - 11: iI11I1II1I1I + oOo0O0Ooo
 if 15 - 15: ooo0O
 if 55 - 55: Ii / ii - i1IiiiI1iI
 if 89 - 89: i1IiiiI1iI - ooOoO0O00 - ooOoO0O00 * OoOo0o - o0o00Oo0O
 if 94 - 94: I1ii11iIi11i / i1IiiiI1iI . oOoO0o00OO0
 if 31 - 31: Ii + iI11I1II1I1I . IIiIiII11i
 if 72 - 72: O0Oooo0O * oOo + I1ii11iIi11i / i1iIi % OoOo0o
 if 84 - 84: iii1i1iiiiIi / ooo0O
 if 9 - 9: i1iIi
 if 76 - 76: oOo0O0Ooo % I1ii11iIi11i / iI11I1II1I1I - I1ii11iIi11i
 if 34 - 34: iii1i1iiiiIi - ooOoO0O00 + OoOo0o + i1iIi . ooo0O
 if 42 - 42: oOo
 if 59 - 59: oOo . O0Oooo0O % oOo
 if 22 - 22: I1ii11iIi11i
 if 21 - 21: ooo0O
 if 86 - 86: oOOoOooOo / iI11I1II1I1I . OoOo0o
 if 93 - 93: I1ii11iIi11i / IIiIiII11i . I1ii11iIi11i + ooOoO0O00 + ooOoO0O00
 if 30 - 30: iii1i1iiiiIi . OoOo0o % OoOo0o / IIiIiII11i + ooOoO0O00
 if 61 - 61: ooOoO0O00 % IIiIiII11i * IIiIiII11i . ooo0O / oOoO0o00OO0 - O0Oooo0O
 if 93 - 93: i1iIi - ooOoO0O00
def IIIIi11 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o000oOOoooo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 75 - 75: o0o00Oo0O - iI11I1II1I1I + iii1i1iiiiIi . Ii - ooo0O
def IIi1III11I1Ii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Oooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 80 - 80: i1IiiiI1iI + ooo0O - O0Oooo0O . oOo * OOOo00oo0oO + OoOo0o
def Oo0ooO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o000oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 61 - 61: ooo0O * o0o00Oo0O
def o0O0oO00oo0O ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 81 - 81: iI11I1II1I1I + o0o00Oo0O * ooo0O - Ii / iiiiiiii1
def IIiIii1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OOO0i1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 78 - 78: iiiiiiii1 . OOOo00oo0oO . oOo0O0Ooo % o0o00Oo0O * oOOoOooOo % O0Oooo0O
def ii1111I ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + IIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 56 - 56: I1ii11iIi11i . i1iIi
def oOOOO0oO0o0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o0o0O00OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 90 - 90: O0Oooo0O * oOo
def o0O0iIi ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iiII11iI11i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 92 - 92: oOo0O0Ooo / O0Oooo0O
def Iiii11i11 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1iIII1i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 42 , II11IiiIII , OoOo00o0OO , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 98 - 98: OOOo00oo0oO / iI11I1II1I1I - iii1i1iiiiIi
def ooo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + I1Ii1i111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for o0OOOo , url , II11IiiIII , OoOo00o0OO , OOoOoo00Oo in iI111i :
  o00oOOooOOo0o ( o0OOOo , url , 5 , I1IIIii + 'GenieTVRSSFeed.png' , I1IIIii + 'GenieTVRSSFeed.png' , OOoOoo00Oo )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 51 - 51: o0o00Oo0O + i1iIi * ii . OOOo00oo0oO + ii
 if 58 - 58: oOOoOooOo . I1ii11iIi11i / oOoO0o00OO0 + oOo * ii / oOo0O0Ooo
 if 24 - 24: o0o00Oo0O - iiiiiiii1 . i1iIi
 if 20 - 20: i1iIi * oOo0O0Ooo % OOOo00oo0oO / Ii . oOo
 if 18 - 18: ii / OoOo0o % ooOoO0O00 - ooOoO0O00 / I1ii11iIi11i
 if 94 - 94: O0Oooo0O + Ii / iiiiiiii1 + ii % ooOoO0O00
 if 57 - 57: iI11I1II1I1I - Ii / IIiIiII11i
 if 35 - 35: oOo0O0Ooo - I11i1ii1 * O0Oooo0O - oOOoOooOo % OOOo00oo0oO
 if 88 - 88: I11i1ii1 * oOo / I11i1ii1 * oOo0O0Ooo + o0o00Oo0O / I11i1ii1
def i1Ii11I ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( o0 ) :
     I111III = 0
     I111III += len ( oo0OOO0OOoOO )
     if I111III > 0 :
      for oOo0oO in oo0OOO0OOoOO :
       os . unlink ( os . path . join ( Ooo00OoO0O00 , oOo0oO ) )
  oOoo0O0O0 = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( oOoo0O0O0 )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 87 - 87: iiiiiiii1 . O0Oooo0O - o0o00Oo0O
 if 97 - 97: i1iIi - oOOoOooOo
 if 94 - 94: iii1i1iiiiIi + oOo + oOo0O0Ooo
 if 66 - 66: i1IiiiI1iI
 if 43 - 43: o0o00Oo0O
 if 50 - 50: i1IiiiI1iI - ii
 if 29 - 29: OOOo00oo0oO * OOOo00oo0oO
 if 44 - 44: oOOoOooOo . oOo0O0Ooo * OOOo00oo0oO * i1iIi
def OOOoO ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 41 - 41: ooOoO0O00 % Ii + i1IiiiI1iI % ii / oOoO0o00OO0
def IiiIiiii ( url ) :
 O0oooOO = os . path . join ( oO0o0o0ooO0oO , 'addon_data' )
 i1I111II11 = [
 ( O0oooOO ) ,
 ( I11 ) ,
 ( os . path . join ( i1111 , 'cache' ) ) ,
 ( os . path . join ( i1111 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( O0oooOO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( O0oooOO , 'plugin.video.itv' , 'Images' ) ) ]
 if 87 - 87: I11i1ii1 - oOo * I1ii11iIi11i / ooo0O % OOOo00oo0oO % i1iIi
 I1IIiIiI = 0
 if 2 - 2: o0o00Oo0O . oOo % OOOo00oo0oO - iiiiiiii1 . Ii - IIiIiII11i
 for II1I in i1I111II11 :
  if os . path . exists ( II1I ) and not II1I in [ I11 , O0oooOO ] :
   for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( II1I ) :
    I111III = 0
    I111III += len ( oo0OOO0OOoOO )
    if I111III > 0 :
     for oOo0oO in oo0OOO0OOoOO :
      if not oOo0oO in oo0o0O00 :
       try :
        os . unlink ( os . path . join ( Ooo00OoO0O00 , oOo0oO ) )
       except :
        pass
      else : IiIIi1 ( 'Ignore Log File: %s' % oOo0oO )
     for II1i1 in oOOOOOoOOoo0 :
      try :
       shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , II1i1 ) )
       I1IIiIiI += 1
       IiIIi1 ( "[Success] cleared %s files from %s" % ( str ( I111III ) , os . path . join ( II1I , II1i1 ) ) )
      except :
       IiIIi1 ( "[Failed] to wipe cache in: %s" % os . path . join ( II1I , II1i1 ) )
  else :
   for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( II1I ) :
    for II1i1 in oOOOOOoOOoo0 :
     if 'cache' in II1i1 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , II1i1 ) )
       I1IIiIiI += 1
       IiIIi1 ( "[Success] wiped %s " % os . path . join ( II1I , II1i1 ) )
      except :
       IiIIi1 ( "[Failed] to wipe cache in: %s" % os . path . join ( II1I , II1i1 ) )
       if 93 - 93: I11i1ii1 . iii1i1iiiiIi % i1iIi - ooOoO0O00 . iI11I1II1I1I / O0Oooo0O
 OOOoO ( oOo0oooo00o , 'Clear Cache: Removed %s Files' % I1IIiIiI )
 if 75 - 75: IIiIiII11i / OOOo00oo0oO
 if 26 - 26: i1IiiiI1iI - ooOoO0O00 % OoOo0o - ii
 if 23 - 23: iii1i1iiiiIi + O0Oooo0O * oOo
 if 22 - 22: oOo
 if 28 - 28: oOo + I11i1ii1 % I1ii11iIi11i
 if 95 - 95: Ii / O0Oooo0O - O0Oooo0O
 if 61 - 61: iii1i1iiiiIi / I1ii11iIi11i % IIiIiII11i / IIiIiII11i / ooo0O
def IIIi1i1iIIIi ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 oOOoOoooOo0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( oOOoOoooOo0o ) :
   I111III = 0
   I111III += len ( oo0OOO0OOoOO )
   if 59 - 59: Ii - i1IiiiI1iI * I1ii11iIi11i % ooo0O + ooOoO0O00
   if 30 - 30: oOOoOooOo / iiiiiiii1
   if I111III > 0 :
    if 66 - 66: oOOoOooOo / I11i1ii1 * iI11I1II1I1I
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( I111III ) + " files found" , "Do you want to delete them?" ) :
     if 42 - 42: O0Oooo0O - Ii % IIiIiII11i * oOOoOooOo . o0o00Oo0O % i1IiiiI1iI
     for oOo0oO in oo0OOO0OOoOO :
      os . unlink ( os . path . join ( Ooo00OoO0O00 , oOo0oO ) )
     for II1i1 in oOOOOOoOOoo0 :
      shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , II1i1 ) )
     iI111I11I1I1 = xbmcgui . Dialog ( )
     iI111I11I1I1 . ok ( oo00 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iI111I11I1I1 = xbmcgui . Dialog ( )
    iI111I11I1I1 . ok ( oo00 , "       No Packages to DELETE" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 Iii1i11 ( )
 return
 if 82 - 82: I1ii11iIi11i % o0o00Oo0O + oOoO0o00OO0 % oOoO0o00OO0
 if 74 - 74: o0o00Oo0O * I11i1ii1 . i1IiiiI1iI - O0Oooo0O + o0o00Oo0O + i1IiiiI1iI
 if 48 - 48: OOOo00oo0oO . ooo0O - OoOo0o
 if 29 - 29: I1ii11iIi11i - i1iIi - I1ii11iIi11i
 if 89 - 89: I1ii11iIi11i . oOo . oOoO0o00OO0 * OOOo00oo0oO . o0o00Oo0O
 if 72 - 72: Ii % i1IiiiI1iI / O0Oooo0O + oOo0O0Ooo * iiiiiiii1
 if 69 - 69: O0Oooo0O + o0o00Oo0O . I11i1ii1 . ooo0O
 if 38 - 38: I11i1ii1 / ooOoO0O00
 if 60 - 60: iii1i1iiiiIi
def i1Ii11II ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 oOOoOoooOo0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( oOOoOoooOo0o ) :
   I111III = 0
   I111III += len ( oo0OOO0OOoOO )
   if 75 - 75: IIiIiII11i / iI11I1II1I1I / ii
   if 61 - 61: I11i1ii1 . I11i1ii1
   if I111III > 0 :
    if 17 - 17: iii1i1iiiiIi % I1ii11iIi11i / O0Oooo0O . i1iIi % oOo
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( I111III ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: oOo0O0Ooo + oOOoOooOo / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
     for oOo0oO in oo0OOO0OOoOO :
      os . unlink ( os . path . join ( Ooo00OoO0O00 , oOo0oO ) )
     for II1i1 in oOOOOOoOOoo0 :
      shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , II1i1 ) )
     iI111I11I1I1 = xbmcgui . Dialog ( )
     iI111I11I1I1 . ok ( oo00 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iI111I11I1I1 = xbmcgui . Dialog ( )
    iI111I11I1I1 . ok ( oo00 , "       No Packages to DELETE" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 IiiIiiii ( url )
 return
 if 95 - 95: iiiiiiii1 / oOOoOooOo + O0Oooo0O
 if 78 - 78: iI11I1II1I1I / oOo0O0Ooo - I11i1ii1
 if 81 - 81: oOoO0o00OO0
 if 31 - 31: o0o00Oo0O % oOOoOooOo / oOo0O0Ooo * iiiiiiii1 % iI11I1II1I1I * iii1i1iiiiIi
 if 76 - 76: O0Oooo0O - o0o00Oo0O
 if 23 - 23: o0o00Oo0O * i1iIi * oOOoOooOo % oOOoOooOo
 if 7 - 7: IIiIiII11i + i1IiiiI1iI
 if 99 - 99: iI11I1II1I1I * OOOo00oo0oO
 if 37 - 37: oOOoOooOo * iiiiiiii1 * i1IiiiI1iI
 if 11 - 11: oOo0O0Ooo
def ii1iII11 ( url , name ) :
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11 = os . path . join ( O0oooo00o0Oo , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 OOo0oO = os . path . join ( O0oooo00o0Oo , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOo0oO ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + oo00 + ' - ADVANCED XML###'
   O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iii11 = os . path . join ( O0oooo00o0Oo , 'advancedsettings.xml' )
   try :
    os . remove ( iii11 )
    print '=== GenieTv - REMOVING    ' + str ( iii11 ) + '    ==='
   except :
    pass
   IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
   ooOO00oOOo000 = open ( iii11 , "w" )
   ooOO00oOOo000 . write ( IIIi1I1IIii1II )
   ooOO00oOOo000 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 else :
  print '###' + oo00 + ' - ADVANCED XML###'
  O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iii11 = os . path . join ( O0oooo00o0Oo , 'advancedsettings.xml' )
  try :
   os . remove ( iii11 )
   print '=== GenieTv - REMOVING    ' + str ( iii11 ) + '    ==='
  except :
   pass
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  ooOO00oOOo000 = open ( iii11 , "w" )
  ooOO00oOOo000 . write ( IIIi1I1IIii1II )
  ooOO00oOOo000 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 return
 if 84 - 84: oOo0O0Ooo % oOo0O0Ooo * i1iIi
def oo00OOooo ( url , name ) :
 print '###' + oo00 + ' - CHECK ADVANCE XML###'
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11 = os . path . join ( O0oooo00o0Oo , 'advancedsettings.xml' )
 try :
  ooOO00oOOo000 = open ( iii11 ) . read ( )
  if 'zero' in ooOO00oOOo000 :
   name = '0CACHE'
  elif 'tuxen' in ooOO00oOOo000 :
   name = 'TUXENS'
  elif 'muckys' in ooOO00oOOo000 :
   name = 'MUCKYS'
  elif 'p2p1' in ooOO00oOOo000 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ooOO00oOOo000 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ooOO00oOOo000 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( oo00 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 62 - 62: oOo . OoOo0o . OOOo00oo0oO + o0o00Oo0O % o0o00Oo0O
def OOoOo0Oo00 ( url ) :
 print '###' + oo00 + ' - DELETING ADVANCE XML###'
 O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11 = os . path . join ( O0oooo00o0Oo , 'advancedsettings.xml' )
 try :
  os . remove ( iii11 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iii11 ) + '    ==='
  iI111I11I1I1 . ok ( oo00 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "       No Advanced Settings To Remove" )
 return
 if 16 - 16: iiiiiiii1
 if 36 - 36: i1iIi / oOoO0o00OO0 * iI11I1II1I1I + ooo0O
 if 64 - 64: i1IiiiI1iI % Ii % oOoO0o00OO0
 if 14 - 14: O0Oooo0O - iii1i1iiiiIi - oOoO0o00OO0 % i1IiiiI1iI + ii
 if 4 - 4: O0Oooo0O - oOo0O0Ooo / iI11I1II1I1I + oOoO0o00OO0 % iI11I1II1I1I * oOo0O0Ooo
 if 30 - 30: Ii % OoOo0o
 if 52 - 52: i1IiiiI1iI - OOOo00oo0oO . Ii - IIiIiII11i + i1iIi . iiiiiiii1
 if 27 - 27: oOo0O0Ooo + iii1i1iiiiIi + iiiiiiii1
 if 70 - 70: i1IiiiI1iI + I11i1ii1 . oOOoOooOo - oOoO0o00OO0
 if 34 - 34: ooOoO0O00 % I1ii11iIi11i . OOOo00oo0oO
def III1I11I1i ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iI111i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for I11II11IiI11 , Ii11iii , oOIIi1iiii1iI , o0OOOO in iI111i :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % I11II11IiI11 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oOIIi1iiii1iI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % o0OOOO )
  inc = inc + 1
  if 89 - 89: ooOoO0O00 - oOo0O0Ooo . i1IiiiI1iI % ooo0O * i1iIi
  if 77 - 77: oOOoOooOo - oOo0O0Ooo - i1iIi - iiiiiiii1 / i1IiiiI1iI
  if 96 - 96: oOoO0o00OO0 + oOoO0o00OO0
  if 89 - 89: ooOoO0O00 + oOoO0o00OO0 . iI11I1II1I1I % iii1i1iiiiIi % IIiIiII11i % ooo0O
  if 52 - 52: i1iIi - oOo0O0Ooo * iI11I1II1I1I % I1ii11iIi11i * OoOo0o
  if 67 - 67: ii * i1IiiiI1iI * i1iIi * iI11I1II1I1I
  if 22 - 22: oOo / ooo0O
  if 35 - 35: O0Oooo0O / O0Oooo0O + ooo0O - OOOo00oo0oO
  if 40 - 40: iii1i1iiiiIi - IIiIiII11i
def iIiIi1iI ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + oo00 + ' - CUSTOM FTV INI###'
  O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iii11 = os . path . join ( O0oooo00o0Oo , 'addons2.ini' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  ooOO00oOOo000 = open ( iii11 , "w" )
  ooOO00oOOo000 . write ( IIIi1I1IIii1II )
  ooOO00oOOo000 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New .ini File" )
 return
 if 79 - 79: O0Oooo0O - i1IiiiI1iI
def Ii1iI1I ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + oo00 + ' - CUSTOM FTV SETTINGS###'
  O0oooo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iii11 = os . path . join ( O0oooo00o0Oo , 'settings.xml' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  ooOO00oOOo000 = open ( iii11 , "w" )
  ooOO00oOOo000 . write ( IIIi1I1IIii1II )
  ooOO00oOOo000 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New Settings" )
 return
 if 89 - 89: oOo0O0Ooo + i1IiiiI1iI . OOOo00oo0oO . IIiIiII11i + OOOo00oo0oO / I1ii11iIi11i
 if 32 - 32: oOo % OOOo00oo0oO * oOoO0o00OO0 + i1IiiiI1iI / O0Oooo0O
def IIi1Ii ( ) :
 try :
  IIIiii1iIiIII = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IIIiii1iIiIII ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    oooOOooo0 = os . path . join ( IIIiii1iIiIII , "source.db" )
    os . unlink ( oooOOooo0 )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "               Error Deleting Database No Database To Delete" )
 return
 if 56 - 56: I11i1ii1
 if 88 - 88: i1iIi / oOo - i1IiiiI1iI
 if 11 - 11: oOo / ooOoO0O00 . ii
 if 40 - 40: I11i1ii1 + iiiiiiii1 * i1IiiiI1iI + iii1i1iiiiIi
 if 5 - 5: O0Oooo0O / I11i1ii1
def i11111IIIII ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 30 - 30: OoOo0o . iiiiiiii1 % oOo + OOOo00oo0oO
 if 69 - 69: Ii + I11i1ii1 * oOOoOooOo * iiiiiiii1 % OOOo00oo0oO
 if 66 - 66: OoOo0o * I11i1ii1 + o0o00Oo0O - ii
 if 19 - 19: I1ii11iIi11i * iii1i1iiiiIi
 if 52 - 52: oOo + OOOo00oo0oO
 if 84 - 84: o0o00Oo0O % oOoO0o00OO0 % iI11I1II1I1I - iii1i1iiiiIi - I1ii11iIi11i
 if 7 - 7: IIiIiII11i % OOOo00oo0oO % ooOoO0O00 . iI11I1II1I1I
def O0oooo0OoO0oo ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; O00O = pluginmessage_yes_no ( oo00 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O00O :
  OOOOo0O = xbmcaddon . Addon ( id = iiIIIII1i1iI ) . getAddonInfo ( 'path' ) ; OOOOo0O = xbmc . translatePath ( OOOOo0O ) ;
  iI1Ii1III = os . path . join ( OOOOo0O , ".." , ".." ) ; iI1Ii1III = os . path . abspath ( iI1Ii1III ) ; pluginlog ( "freshstart.main_list xbmcPath=" + iI1Ii1III ) ; i111iI1I = False
  try :
   for Ooo00OoO0O00 , oOOOOOoOOoo0 , oo0OOO0OOoOO in os . walk ( iI1Ii1III , topdown = True ) :
    oOOOOOoOOoo0 [ : ] = [ II1i1 for II1i1 in oOOOOOoOOoo0 if II1i1 not in i1i1II ]
    for o0OOOo in oo0OOO0OOoOO :
     try : os . remove ( os . path . join ( Ooo00OoO0O00 , o0OOOo ) )
     except :
      if o0OOOo not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : i111iI1I = True
      pluginlog ( "Error removing " + Ooo00OoO0O00 + " " + o0OOOo )
    for o0OOOo in oOOOOOoOOoo0 :
     try : os . rmdir ( os . path . join ( Ooo00OoO0O00 , o0OOOo ) )
     except :
      if o0OOOo not in [ "Database" , "userdata" ] : i111iI1I = True
      pluginlog ( "Error removing " + Ooo00OoO0O00 + " " + o0OOOo )
   if not i111iI1I : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( oo00 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( oo00 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 IiIIIIiI ( )
 if 95 - 95: iI11I1II1I1I / oOoO0o00OO0 / oOOoOooOo + iI11I1II1I1I - O0Oooo0O
 if 65 - 65: i1iIi * IIiIiII11i - OoOo0o
 if 82 - 82: iii1i1iiiiIi % O0Oooo0O / ooo0O + oOo
def i1IiI1IiI ( ) :
 I1Ii1111 = [ ]
 IIIIIi1I1Ii = sys . argv [ 2 ]
 if len ( IIIIIi1I1Ii ) >= 2 :
  IiiiIi1iI1iI = sys . argv [ 2 ]
  i11Iii11I1i = IiiiIi1iI1iI . replace ( '?' , '' )
  if ( IiiiIi1iI1iI [ len ( IiiiIi1iI1iI ) - 1 ] == '/' ) :
   IiiiIi1iI1iI = IiiiIi1iI1iI [ 0 : len ( IiiiIi1iI1iI ) - 2 ]
  O00ooO0 = i11Iii11I1i . split ( '&' )
  I1Ii1111 = { }
  for iiIi in range ( len ( O00ooO0 ) ) :
   Oo0O0oOo = { }
   Oo0O0oOo = O00ooO0 [ iiIi ] . split ( '=' )
   if ( len ( Oo0O0oOo ) ) == 2 :
    I1Ii1111 [ Oo0O0oOo [ 0 ] ] = Oo0O0oOo [ 1 ]
    if 83 - 83: o0o00Oo0O
 return I1Ii1111
 if 35 - 35: Ii - i1IiiiI1iI . iii1i1iiiiIi * IIiIiII11i % Ii
OOoo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
o00oO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
o0o00o = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oO0oO0OO0O = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iI1i1iii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iI1IIIIIiIiii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o000oOOoooo0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OOooO0oOoOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
Oooo0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o000oO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
i1iI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OOO0i1Ii1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
IIii11 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0o0O00OO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiII11iI11i1I = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i1iIII1i1II = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OoOo0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
O00O0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i11iII1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OO00oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OOI1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iIOoo000 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1Ii1i111I = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
o0O00o0o = base64 . decodestring ( 'Q1VOVA==' )
def O0o00O0oOO0Oo0O0O ( display , mode = None , name = None , url = None , menu = None , description = oOo0oooo00o , overwrite = True , fanart = Oo00OOOOO , icon = O0O , themeit = None ) :
 Ii1I1I1i11ii = sys . argv [ 0 ]
 if not mode == None : Ii1I1I1i11ii += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Ii1I1I1i11ii += "&name=" + urllib . quote_plus ( name )
 if not url == None : Ii1I1I1i11ii += "&url=" + urllib . quote_plus ( url )
 OoOo0oO0o = True
 if themeit : display = themeit % display
 o0OoOo00ooO = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : o0OoOo00ooO . addContextMenuItems ( menu , replaceItems = overwrite )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = False )
 return OoOo0oO0o
def O0o0oo0O ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 o0OoOo00ooO . setProperty ( 'fanart_image' , fanart )
 o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
 O000OO0I11 = [ ]
 O000OO0I11 . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 O000OO0I11 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 o0OoOo00ooO . addContextMenuItems ( O000OO0I11 , replaceItems = True )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = False )
 return OoOo0oO0o
def o00oOOooOOo0o ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1I11i = [ ]
  if showcontext == 'fav' :
   ii1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   ii1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0OoOo00ooO . addContextMenuItems ( ii1I11i )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = True )
 return OoOo0oO0o
 if 96 - 96: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i . oOoO0o00OO0 * i1iIi
def O0O0ooOOO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1I11i = [ ]
  if showcontext == 'fav' :
   ii1I11i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   ii1I11i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0OoOo00ooO . addContextMenuItems ( ii1I11i )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = False )
 return OoOo0oO0o
 if 55 - 55: oOo0O0Ooo . oOo0O0Ooo - i1iIi * IIiIiII11i + OOOo00oo0oO
 if 38 - 38: I1ii11iIi11i / IIiIiII11i % O0Oooo0O
IiiiIi1iI1iI = i1IiI1IiI ( )
iIIII1iIIii = None
o0OOOo = None
Ii1IIi = None
II11IiiIII = None
OoOo00o0OO = None
OOoOoo00Oo = None
i1I1Ii11i = None
iI11Ii1i11i = None
if 21 - 21: iI11I1II1I1I - oOo - oOo * o0o00Oo0O / i1iIi
if 28 - 28: I1ii11iIi11i . Ii . o0o00Oo0O
try :
 iI11Ii1i11i = int ( IiiiIi1iI1iI [ "fav_mode" ] )
except :
 pass
 if 67 - 67: IIiIiII11i / o0o00Oo0O
try :
 iIIII1iIIii = urllib . unquote_plus ( IiiiIi1iI1iI [ "url" ] )
except :
 pass
try :
 o0OOOo = urllib . unquote_plus ( IiiiIi1iI1iI [ "name" ] )
except :
 pass
try :
 II11IiiIII = urllib . unquote_plus ( IiiiIi1iI1iI [ "iconimage" ] )
except :
 pass
try :
 Ii1IIi = int ( IiiiIi1iI1iI [ "mode" ] )
except :
 pass
try :
 OoOo00o0OO = urllib . unquote_plus ( IiiiIi1iI1iI [ "fanart" ] )
except :
 pass
try :
 OOoOoo00Oo = urllib . unquote_plus ( IiiiIi1iI1iI [ "description" ] )
except :
 pass
 if 10 - 10: ooOoO0O00 / I1ii11iIi11i
 if 20 - 20: I1ii11iIi11i * O0Oooo0O / oOoO0o00OO0 . oOOoOooOo
print str ( I11II1i ) + ': ' + str ( I1IiI )
print "Mode: " + str ( Ii1IIi )
print "URL: " + str ( iIIII1iIIii )
print "Name: " + str ( o0OOOo )
print "IconImage: " + str ( II11IiiIII )
if 67 - 67: ooo0O . I1ii11iIi11i % i1IiiiI1iI
if 38 - 38: OoOo0o - oOo . oOOoOooOo
def iIiIi11 ( content , viewType ) :
 if 50 - 50: ooo0O
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 85 - 85: IIiIiII11i . iiiiiiii1 - ooOoO0O00
if II11IiiIII == None : II11IiiIII = O0O
if OoOo00o0OO == None : OoOo00o0OO = Oo00OOOOO
if Ii1IIi == None :
 O00o0OO0 ( )
 if 23 - 23: iiiiiiii1 . i1iIi - oOo / oOoO0o00OO0 / o0o00Oo0O
elif Ii1IIi == 1 :
 Ii11iIi1iIiii ( iIIII1iIIii )
 if 4 - 4: ooOoO0O00 % I1ii11iIi11i % i1iIi * oOOoOooOo - i1IiiiI1iI
elif Ii1IIi == 44 :
 OO00o ( iIIII1iIIii )
 if 76 - 76: iI11I1II1I1I / oOOoOooOo % oOoO0o00OO0 % OoOo0o
elif Ii1IIi == 2 :
 I1iI1I1111i ( )
 if 13 - 13: I11i1ii1
elif Ii1IIi == 3 :
 oo0OoO ( )
 if 56 - 56: I1ii11iIi11i
elif Ii1IIi == 21 :
 Iii1ii1II11i ( )
 if 55 - 55: Ii + iI11I1II1I1I / ooOoO0O00 / oOoO0o00OO0
elif Ii1IIi == 4 :
 iIiii1IIi1I ( )
 if 64 - 64: I11i1ii1 . oOo * Ii
elif Ii1IIi == 5 :
 I1iiI ( iIIII1iIIii )
 if 18 - 18: i1iIi % ooo0O - I1ii11iIi11i
elif Ii1IIi == 6 :
 IIIi1i1iIIIi ( iIIII1iIIii )
 if 28 - 28: I11i1ii1
elif Ii1IIi == 7 :
 ii1iII11 ( iIIII1iIIii , o0OOOo )
 if 93 - 93: I1ii11iIi11i % ooOoO0O00
elif Ii1IIi == 8 :
 oo00OOooo ( iIIII1iIIii , o0OOOo )
 if 51 - 51: OOOo00oo0oO % o0o00Oo0O
elif Ii1IIi == 9 :
 FIXREPOSADDONS ( iIIII1iIIii )
 if 41 - 41: oOo0O0Ooo * oOo0O0Ooo . O0Oooo0O
elif Ii1IIi == 10 :
 IioO0oOOO0Ooo ( )
 if 38 - 38: oOo0O0Ooo % Ii
elif Ii1IIi == 11 :
 OOoOo0Oo00 ( iIIII1iIIii )
 if 17 - 17: Ii
elif Ii1IIi == 12 :
 III1I11I1i ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 81 - 81: O0Oooo0O
elif Ii1IIi == 13 :
 i1Ii11I ( )
 if 25 - 25: oOo0O0Ooo
elif Ii1IIi == 14 :
 IiiIiiii ( iIIII1iIIii )
 if 52 - 52: oOoO0o00OO0 % ooOoO0O00 . I11i1ii1 % iii1i1iiiiIi
elif Ii1IIi == 15 :
 ii11I ( )
 if 50 - 50: OoOo0o * oOo0O0Ooo / ooo0O
elif Ii1IIi == 16 :
 iIiIi1iI ( iIIII1iIIii , o0OOOo )
 if 91 - 91: iI11I1II1I1I / OoOo0o * o0o00Oo0O . ooo0O + OOOo00oo0oO / oOoO0o00OO0
elif Ii1IIi == 17 :
 Ii1iI1I ( iIIII1iIIii , o0OOOo )
 if 33 - 33: IIiIiII11i + i1iIi
elif Ii1IIi == 18 :
 IIi1Ii ( )
 if 46 - 46: I11i1ii1 + o0o00Oo0O + ooOoO0O00 + oOOoOooOo / iiiiiiii1
elif Ii1IIi == 19 :
 oo000O0o ( iIIII1iIIii )
 if 94 - 94: OOOo00oo0oO + iiiiiiii1 * iii1i1iiiiIi - ooOoO0O00 / ii
elif Ii1IIi == 40 :
 i1OooO00oO00o ( o0OOOo , iIIII1iIIii , OOoOoo00Oo )
 if 59 - 59: i1IiiiI1iI % i1iIi / iii1i1iiiiIi
elif Ii1IIi == 42 :
 oooo ( o0OOOo , iIIII1iIIii , OOoOoo00Oo )
 if 99 - 99: i1iIi + IIiIiII11i / Ii - I11i1ii1 / iiiiiiii1 + iiiiiiii1
elif Ii1IIi == 43 :
 iI11ii ( iIIII1iIIii )
 if 55 - 55: I11i1ii1 + ii * oOoO0o00OO0 . I11i1ii1 * oOoO0o00OO0 + I11i1ii1
elif Ii1IIi == 20 :
 ii1IIi1IIIIi1 ( iIIII1iIIii )
 if 81 - 81: iI11I1II1I1I . oOOoOooOo + iii1i1iiiiIi
elif Ii1IIi == 22 :
 IIIIi11 ( iIIII1iIIii )
 if 31 - 31: i1IiiiI1iI / iii1i1iiiiIi + ooo0O
elif Ii1IIi == 23 :
 IIi1III11I1Ii ( iIIII1iIIii )
 if 80 - 80: I1ii11iIi11i
elif Ii1IIi == 24 :
 Oo0ooO ( iIIII1iIIii )
 if 58 - 58: O0Oooo0O + OoOo0o
elif Ii1IIi == 25 :
 o0O0oO00oo0O ( iIIII1iIIii )
 if 76 - 76: IIiIiII11i - ooo0O % oOo + iiiiiiii1
elif Ii1IIi == 26 :
 IIiIii1 ( iIIII1iIIii )
 if 38 - 38: O0Oooo0O - i1IiiiI1iI * ooOoO0O00 + iI11I1II1I1I
elif Ii1IIi == 27 :
 ii1111I ( iIIII1iIIii )
 if 41 - 41: i1iIi . oOo + oOoO0o00OO0 + iii1i1iiiiIi
elif Ii1IIi == 28 :
 oOOOO0oO0o0 ( iIIII1iIIii )
 if 76 - 76: iiiiiiii1 - iI11I1II1I1I
elif Ii1IIi == 29 :
 o0O0iIi ( iIIII1iIIii )
 if 23 - 23: i1IiiiI1iI / oOo % OoOo0o
elif Ii1IIi == 30 :
 i11iI1111ii1I ( iIIII1iIIii )
 if 9 - 9: oOOoOooOo % oOoO0o00OO0 . ii + oOo % OoOo0o * ii
elif Ii1IIi == 31 :
 Iiii11i11 ( iIIII1iIIii )
 if 21 - 21: i1iIi % o0o00Oo0O
elif Ii1IIi == 32 :
 I111I ( )
 if 15 - 15: IIiIiII11i * i1iIi + I11i1ii1 % iiiiiiii1
elif Ii1IIi == 33 :
 oooO ( )
 if 96 - 96: IIiIiII11i * O0Oooo0O / I1ii11iIi11i
elif Ii1IIi == 35 :
 oO00oO0 ( iIIII1iIIii )
 if 35 - 35: oOo0O0Ooo
elif Ii1IIi == 34 :
 oo0OOoOo0 ( iIIII1iIIii )
 if 54 - 54: oOoO0o00OO0 % ooo0O . ooOoO0O00
elif Ii1IIi == 36 :
 IiIIi ( iIIII1iIIii )
 if 72 - 72: i1iIi
elif Ii1IIi == 37 :
 Ii11i1I1 ( iIIII1iIIii )
 if 87 - 87: iiiiiiii1 - oOo0O0Ooo
elif Ii1IIi == 38 :
 oOooOOoo ( iIIII1iIIii )
 if 54 - 54: iI11I1II1I1I + OOOo00oo0oO * ooo0O % ii . I1ii11iIi11i
elif Ii1IIi == 41 :
 O0oooo0OoO0oo ( IiiiIi1iI1iI )
 if 32 - 32: iiiiiiii1
elif Ii1IIi == 39 :
 ooo ( iIIII1iIIii )
 if 33 - 33: oOOoOooOo + I1ii11iIi11i * iii1i1iiiiIi % oOOoOooOo * OOOo00oo0oO - oOo
elif Ii1IIi == 45 :
 TEXTS ( )
 if 40 - 40: i1IiiiI1iI . ii * o0o00Oo0O / O0Oooo0O + o0o00Oo0O
elif Ii1IIi == 46 :
 OooooO0oOO ( )
 if 97 - 97: oOOoOooOo - oOOoOooOo * OoOo0o % iii1i1iiiiIi - iii1i1iiiiIi - O0Oooo0O
elif Ii1IIi == 47 :
 GEVID ( )
 if 52 - 52: o0o00Oo0O % iiiiiiii1
elif Ii1IIi == 48 :
 oo000oiIIIII ( o0OOOo , iIIII1iIIii , OOoOoo00Oo )
 if 81 - 81: ii % iii1i1iiiiIi % I1ii11iIi11i - oOo0O0Ooo
elif Ii1IIi == 49 :
 II1Iii ( )
 if 43 - 43: ooo0O % ooo0O
elif Ii1IIi == 22222 :
 O00o0o ( iIIII1iIIii )
 if 48 - 48: o0o00Oo0O
elif Ii1IIi == 222225 :
 i11i11 ( iIIII1iIIii )
 if 5 - 5: OoOo0o / Ii . i1IiiiI1iI % OoOo0o
elif Ii1IIi == 222 :
 oO00oo0o ( iIIII1iIIii )
 if 1 - 1: IIiIiII11i + o0o00Oo0O * iii1i1iiiiIi / I11i1ii1 . o0o00Oo0O
elif Ii1IIi == 2222222 :
 i11IIIiI1I ( iIIII1iIIii )
 if 87 - 87: I11i1ii1 + oOo0O0Ooo
elif Ii1IIi == 222222 :
 i1iIi11 ( iIIII1iIIii , o0OOOo )
 if 74 - 74: oOo + oOo % iiiiiiii1 / i1IiiiI1iI / o0o00Oo0O
elif Ii1IIi == 333 :
 ii11IoOo0O0Oo ( iIIII1iIIii )
 if 54 - 54: ooo0O / ii * oOOoOooOo . iii1i1iiiiIi - O0Oooo0O
 if 69 - 69: OOOo00oo0oO - oOo
elif Ii1IIi == 1020 :
 OoOooOOooO ( )
 if 80 - 80: oOOoOooOo + iI11I1II1I1I . IIiIiII11i + oOo0O0Ooo - OOOo00oo0oO % iii1i1iiiiIi
elif Ii1IIi == 1021 :
 ANIMEEP ( )
 if 10 - 10: iI11I1II1I1I
elif Ii1IIi == 1022 :
 ANIMEPLAY ( iIIII1iIIii )
 if 44 - 44: iii1i1iiiiIi * OOOo00oo0oO . oOoO0o00OO0 + Ii
elif Ii1IIi == 1001 :
 oOO0o00 ( )
 if 85 - 85: i1IiiiI1iI
elif Ii1IIi == 1005 :
 O0ii1IIIiiI1i ( )
 if 36 - 36: oOOoOooOo % oOo
elif Ii1IIi == 1007 :
 Iiii1I ( iIIII1iIIii )
 if 1 - 1: ii - iii1i1iiiiIi
elif Ii1IIi == 1010 :
 O0O000oOO0 ( iIIII1iIIii )
 if 35 - 35: O0Oooo0O
elif Ii1IIi == 1011 :
 Ii1oo ( iIIII1iIIii )
 if 35 - 35: I1ii11iIi11i - iI11I1II1I1I / ooOoO0O00 + oOo - ii / Ii
elif Ii1IIi == 1012 :
 II1i1iIIi1 ( iIIII1iIIii )
 if 79 - 79: oOo0O0Ooo * oOOoOooOo * oOOoOooOo
elif Ii1IIi == 1030 :
 I111I11iiI ( )
 if 92 - 92: iiiiiiii1 % oOoO0o00OO0
elif Ii1IIi == 1031 :
 oOoOOooo0OOO ( iIIII1iIIii , II11IiiIII )
 if 16 - 16: OOOo00oo0oO
elif Ii1IIi == 1032 :
 IiI1i1i1 ( iIIII1iIIii )
 if 52 - 52: ii % oOOoOooOo - O0Oooo0O * i1IiiiI1iI
elif Ii1IIi == 1006 :
 Parse . ParseURL ( iIIII1iIIii )
 if 24 - 24: i1iIi + I11i1ii1 + ii / OOOo00oo0oO / oOo0O0Ooo + I11i1ii1
elif Ii1IIi == 2030 :
 Parse . addonParseURL ( iIIII1iIIii )
 if 52 - 52: oOOoOooOo
elif Ii1IIi == 2031 :
 Parse . apkParseURL ( iIIII1iIIii )
 if 38 - 38: oOo + oOo0O0Ooo % I11i1ii1
elif Ii1IIi == 2032 :
 Parse . ParseBOSS ( iIIII1iIIii )
 if 87 - 87: OOOo00oo0oO * i1iIi - O0Oooo0O / OOOo00oo0oO
elif Ii1IIi == 1002 :
 ii1I1IIiii ( iIIII1iIIii )
 if 65 - 65: iii1i1iiiiIi
elif Ii1IIi == 1003 :
 i1io0ooO0OO ( iIIII1iIIii , II11IiiIII )
 if 87 - 87: i1IiiiI1iI - Ii - OoOo0o . iii1i1iiiiIi + I11i1ii1 . oOo
elif Ii1IIi == 1004 :
 I1IiI1i1Iii ( iIIII1iIIii )
 if 70 - 70: iI11I1II1I1I % ii / oOo . o0o00Oo0O - i1IiiiI1iI % IIiIiII11i
elif Ii1IIi == 1008 :
 Ooo0i1i1 ( )
 if 84 - 84: OoOo0o * ooOoO0O00 . iI11I1II1I1I * iiiiiiii1 + O0Oooo0O + IIiIiII11i
elif Ii1IIi == 1009 :
 Ooo0O00 ( iIIII1iIIii )
 if 97 - 97: i1iIi - I11i1ii1
elif Ii1IIi == 2001 :
 III1iI1III1I1 ( )
 if 64 - 64: OOOo00oo0oO . oOOoOooOo / oOOoOooOo - IIiIiII11i
elif Ii1IIi == 2002 :
 IioooO ( iIIII1iIIii )
 if 81 - 81: oOoO0o00OO0
elif Ii1IIi == 1013 :
 Oo0O00O ( )
elif Ii1IIi == 10111113 :
 i1iI1i11iIi1 ( iIIII1iIIii )
 if 64 - 64: OOOo00oo0oO * oOo / OoOo0o + i1iIi % I1ii11iIi11i . I11i1ii1
elif Ii1IIi == 1014 :
 I1iII1IiI11i ( )
 if 2 - 2: O0Oooo0O + i1IiiiI1iI
elif Ii1IIi == 1015 :
 OOOoOooOO0O0OooO0 ( iIIII1iIIii )
 if 47 - 47: Ii + iI11I1II1I1I % oOoO0o00OO0 - OOOo00oo0oO % oOo
elif Ii1IIi == 1016 :
 I1I1I1IIi1III ( iIIII1iIIii , II11IiiIII , o0OOOo )
 if 85 - 85: OOOo00oo0oO * iii1i1iiiiIi / iii1i1iiiiIi
elif Ii1IIi == 1017 :
 O0O0O0Oo ( )
 if 85 - 85: OoOo0o / O0Oooo0O . ooOoO0O00 / iii1i1iiiiIi + iI11I1II1I1I
elif Ii1IIi == 1018 :
 OOOOoO00o0O ( iIIII1iIIii )
 if 71 - 71: oOo
elif Ii1IIi == 1019 :
 IIII1 ( iIIII1iIIii )
elif Ii1IIi == 10190 :
 I1IIIiIiIi ( iIIII1iIIii )
 if 96 - 96: oOoO0o00OO0 / oOo0O0Ooo - oOoO0o00OO0 / IIiIiII11i - I11i1ii1
elif Ii1IIi == 1023 :
 IIi1I1iII111 ( )
 if 74 - 74: i1iIi * ii % OoOo0o + ii + iiiiiiii1
elif Ii1IIi == 1024 :
 IIoOOOoOoOO ( iIIII1iIIii )
 if 83 - 83: ooOoO0O00
elif Ii1IIi == 1025 :
 iI1iIII1i1II ( iIIII1iIIii )
 if 2 - 2: ooOoO0O00 / OoOo0o * o0o00Oo0O
elif Ii1IIi == 4001 :
 iii1III1i ( )
 if 99 - 99: ii . iii1i1iiiiIi / IIiIiII11i
elif Ii1IIi == 4002 :
 OOO ( )
 if 64 - 64: iiiiiiii1 / ooOoO0O00 . oOo0O0Ooo + o0o00Oo0O
elif Ii1IIi == 4003 :
 I1iIi1IiI1i ( )
 if 5 - 5: o0o00Oo0O . Ii
elif Ii1IIi == 4004 :
 O00OO ( )
 if 71 - 71: ooo0O + iiiiiiii1 + oOOoOooOo
elif Ii1IIi == 4005 :
 ii1 ( )
 if 27 - 27: ii . iiiiiiii1 * O0Oooo0O % o0o00Oo0O + ii - iiiiiiii1
elif Ii1IIi == 4006 :
 oOIIiIi ( )
 if 86 - 86: ooOoO0O00
elif Ii1IIi == 4007 :
 i11i1ii1I ( )
 if 81 - 81: iii1i1iiiiIi
elif Ii1IIi == 4008 :
 oOo0 ( )
 if 52 - 52: iiiiiiii1 * I11i1ii1 % oOo0O0Ooo * i1IiiiI1iI
elif Ii1IIi == 40099 : oo0O ( )
elif Ii1IIi == 4009 : i1ii11I111Ii ( )
elif Ii1IIi == 4010 : OO0O00 ( )
elif Ii1IIi == 3000 :
 iI1iiiIIIIIiIii1 ( )
 if 73 - 73: O0Oooo0O * oOOoOooOo
elif Ii1IIi == 3001 :
 ooOO0O00O ( )
 if 62 - 62: OoOo0o . oOo0O0Ooo * iI11I1II1I1I + oOo * oOOoOooOo / OOOo00oo0oO
elif Ii1IIi == 3002 :
 i1iOOoOo0o ( iIIII1iIIii )
 if 14 - 14: iiiiiiii1 / oOo
elif Ii1IIi == 3003 :
 oOOOiII1iII ( iIIII1iIIii )
 if 75 - 75: I11i1ii1
elif Ii1IIi == 3004 :
 oOO00o0O0O ( iIIII1iIIii )
 if 68 - 68: I11i1ii1 - ooOoO0O00 % I11i1ii1 . oOo . Ii . ii
elif Ii1IIi == 404 :
 iI1i1iIii1 ( o0OOOo , iIIII1iIIii , II11IiiIII )
 if 32 - 32: iiiiiiii1 + oOo % I11i1ii1 + oOo0O0Ooo
elif Ii1IIi == 405 :
 iI1Ii ( iIIII1iIIii )
 if 69 - 69: O0Oooo0O + i1IiiiI1iI - iI11I1II1I1I - IIiIiII11i . i1iIi
elif Ii1IIi == 7030 :
 oOi1 ( )
 if 74 - 74: oOoO0o00OO0 % ooo0O + o0o00Oo0O - Ii - I11i1ii1 % OoOo0o
elif Ii1IIi == 7021 :
 oOOooO ( o0OOOo )
 if 39 - 39: oOo - ooo0O
elif Ii1IIi == 7022 :
 i111I ( o0OOOo )
 if 71 - 71: iiiiiiii1 . oOo + oOOoOooOo - OoOo0o - I1ii11iIi11i
elif Ii1IIi == 7000 :
 OO00OOOO00oOO ( o0OOOo , iIIII1iIIii , img )
 if 100 - 100: ii - ooo0O + O0Oooo0O . ii % Ii
elif Ii1IIi == 7050 :
 OOoOOO0 ( iIIII1iIIii )
 if 64 - 64: O0Oooo0O % ii / ooOoO0O00 / oOo
elif Ii1IIi == 7051 :
 Ooo0oOoOoOoo ( iIIII1iIIii )
 if 2 - 2: i1IiiiI1iI % ooo0O . oOo . oOo
elif Ii1IIi == 70511 :
 WATCHLIST2 ( iIIII1iIIii )
 if 89 - 89: oOOoOooOo - OOOo00oo0oO + IIiIiII11i + oOo - I11i1ii1
elif Ii1IIi == 7052 :
 oO0Ooo ( iIIII1iIIii )
 if 27 - 27: O0Oooo0O - ooo0O + oOo
elif Ii1IIi == 7053 :
 iiiiIIiiII1Iii1 ( iIIII1iIIii )
 if 38 - 38: iii1i1iiiiIi + oOo . Ii + i1iIi % ooOoO0O00 % oOo0O0Ooo
elif Ii1IIi == 7054 :
 CoolPlay ( iIIII1iIIii )
 if 93 - 93: Ii
elif Ii1IIi == 7060 :
 O000ooo ( )
 if 63 - 63: iI11I1II1I1I - iI11I1II1I1I % ooo0O
elif Ii1IIi == 7061 :
 IiiIi11 ( iIIII1iIIii )
 if 97 - 97: ooOoO0O00 % i1IiiiI1iI % iii1i1iiiiIi
elif Ii1IIi == 7063 :
 oOOiI ( iIIII1iIIii )
 if 25 - 25: iii1i1iiiiIi . iI11I1II1I1I - iiiiiiii1 % IIiIiII11i . iii1i1iiiiIi
elif Ii1IIi == 7062 :
 Oo0O0O000 ( iIIII1iIIii )
 if 16 - 16: OoOo0o . I1ii11iIi11i . oOo0O0Ooo % o0o00Oo0O . oOoO0o00OO0 + Ii
elif Ii1IIi == 7064 :
 NATatozcat ( )
 if 100 - 100: oOoO0o00OO0 - ooOoO0O00 - oOo * ooo0O + iii1i1iiiiIi
elif Ii1IIi == 7067 :
 oOO0oOo0OOoOO ( iIIII1iIIii )
 if 31 - 31: ooOoO0O00
elif Ii1IIi == 7066 :
 NATatozA ( iIIII1iIIii )
 if 21 - 21: ooo0O / o0o00Oo0O % o0o00Oo0O . ii / oOo0O0Ooo
elif Ii1IIi == 7065 :
 o0O00oo0Ooo ( iIIII1iIIii )
 if 94 - 94: oOOoOooOo + oOo / oOOoOooOo - oOOoOooOo + I1ii11iIi11i + ooo0O
elif Ii1IIi == 7070 :
 ii1I11ii ( )
 if 50 - 50: OOOo00oo0oO . I1ii11iIi11i
elif Ii1IIi == 7071 :
 DIZIlist ( iIIII1iIIii )
 if 15 - 15: i1iIi
elif Ii1IIi == 7072 :
 DIZIpull ( iIIII1iIIii )
 if 64 - 64: ii
elif Ii1IIi == 7073 :
 WATCHDIZI ( iIIII1iIIii )
 if 25 - 25: I11i1ii1
elif Ii1IIi == 7002 :
 IIoOoo0oooo ( )
 if 29 - 29: iii1i1iiiiIi % oOOoOooOo * ii
elif Ii1IIi == 7003 :
 I1iiI1IiI1iii ( iIIII1iIIii )
 if 8 - 8: Ii - O0Oooo0O / I11i1ii1
elif Ii1IIi == 7004 :
 iioo ( iIIII1iIIii )
 if 17 - 17: Ii * oOo . ooo0O . ii . iii1i1iiiiIi - oOoO0o00OO0
elif Ii1IIi == 7020 :
 o0oooooooO0o ( iIIII1iIIii )
 if 78 - 78: oOoO0o00OO0 - ii + o0o00Oo0O
elif Ii1IIi == 7001 :
 I11IIIi ( )
 if 15 - 15: oOoO0o00OO0 / I11i1ii1 % oOo0O0Ooo
elif Ii1IIi == 7010 :
 iIii ( iIIII1iIIii )
 if 16 - 16: i1iIi
elif Ii1IIi == 7011 :
 O000oooiI1I1I1 ( iIIII1iIIii )
 if 26 - 26: ooo0O / i1IiiiI1iI + iii1i1iiiiIi / iii1i1iiiiIi
elif Ii1IIi == 7012 :
 iII1iIiiII ( iIIII1iIIii )
 if 31 - 31: O0Oooo0O
elif Ii1IIi == 7013 :
 cnfTVPlay2 ( iIIII1iIIii )
elif Ii1IIi == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iIIII1iIIii )
elif Ii1IIi == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iIIII1iIIii )
elif Ii1IIi == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( o0OOOo , iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ii1IIi == 7018 :
 Ii11Ii1i1 ( )
elif Ii1IIi == 7019 :
 CNF_Studio_Indexer . List_Movies ( iIIII1iIIii )
elif Ii1IIi == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iIIII1iIIii )
elif Ii1IIi == 7024 :
 CNF_Studio_Indexer . Box_Office ( iIIII1iIIii )
 if 84 - 84: Ii * OoOo0o . iiiiiiii1 - i1iIi * ooOoO0O00 - oOoO0o00OO0
elif Ii1IIi == 8000 :
 O0oi1I1I1IIIi11 ( )
elif Ii1IIi == 8001 :
 i1iiIiIi1iIII ( )
elif Ii1IIi == 8002 :
 i1O0o00o0Oo ( )
elif Ii1IIi == 8003 :
 O00o0oO0oO0 ( )
elif Ii1IIi == 8004 :
 I11ii1I1 ( )
elif Ii1IIi == 8005 :
 iIII1 ( )
elif Ii1IIi == 8006 :
 iII1I11ii1III ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 8030 :
 OoOoooOO00OO ( iIIII1iIIii )
elif Ii1IIi == 8045 :
 oo0Oooo0O ( iIIII1iIIii )
elif Ii1IIi == 8046 :
 ooO0Oo ( iIIII1iIIii )
elif Ii1IIi == 8047 :
 OooOooo00OOO0o ( iIIII1iIIii )
elif Ii1IIi == 8048 :
 iI1iiI1Ii ( iIIII1iIIii )
elif Ii1IIi == 8049 :
 i1iiII1iIIIIII ( iIIII1iIIii )
elif Ii1IIi == 804900 :
 IIIIII11iIiI1III ( iIIII1iIIii )
elif Ii1IIi == 8020 :
 IIiiI11iI ( )
elif Ii1IIi == 8021 :
 IIi1III1II ( iIIII1iIIii )
elif Ii1IIi == 8022 :
 o0o0OOOO ( iIIII1iIIii )
elif Ii1IIi == 8023 :
 I1i1iiIII1i1 ( iIIII1iIIii )
elif Ii1IIi == 8040 :
 OOOoOO ( )
elif Ii1IIi == 8041 :
 ooO0i11i1i1i ( iIIII1iIIii )
elif Ii1IIi == 8042 :
 Iiii1i11III1I1 ( iIIII1iIIii )
elif Ii1IIi == 8043 :
 yt . PlayVideo ( iIIII1iIIii )
elif Ii1IIi == 8044 :
 O000o ( iIIII1iIIii )
elif Ii1IIi == 8060 :
 o000ooooO0o ( )
elif Ii1IIi == 8061 :
 iiiiIiI1IIiI ( iIIII1iIIii )
elif Ii1IIi == 8064 :
 iiI ( )
elif Ii1IIi == 8065 :
 IIIIii11 ( iIIII1iIIii )
elif Ii1IIi == 8070 :
 oOOo0OoooOo ( )
elif Ii1IIi == 8071 :
 I1I1IiIiIIi1I ( iIIII1iIIii )
elif Ii1IIi == 7080 :
 oo0Ooo ( iIIII1iIIii )
elif Ii1IIi == 8090 :
 O0o00oooO00o ( )
elif Ii1IIi == 8091 :
 oOoo00o0OoOOO ( iIIII1iIIii )
elif Ii1IIi == 8092 :
 Ii1Ii11I ( iIIII1iIIii )
elif Ii1IIi == 8093 :
 Ii11 ( iIIII1iIIii )
elif Ii1IIi == 8081 :
 OOoO0oOooOo0Oo ( )
elif Ii1IIi == 8062 :
 O0oO ( iIIII1iIIii )
elif Ii1IIi == 8063 :
 Iii1i ( iIIII1iIIii )
elif Ii1IIi == 8050 :
 oOOOoo0 ( )
elif Ii1IIi == 8051 :
 iI1i11II1i1i ( iIIII1iIIii )
elif Ii1IIi == 8052 :
 O0O0O00OoO0O ( iIIII1iIIii )
elif Ii1IIi == 8085 :
 o0OoOO0 ( )
elif Ii1IIi == 8086 :
 o00o000 ( iIIII1iIIii )
elif Ii1IIi == 8087 :
 OOO0 ( iIIII1iIIii )
elif Ii1IIi == 8088 :
 oOO0ooOO ( iIIII1iIIii , o0OOOo )
elif Ii1IIi == 9000 :
 O0ooOIii1iIIIi11I1 ( )
elif Ii1IIi == 1111 :
 I1iI1iiI1Ii1 ( )
elif Ii1IIi == 9001 :
 I1I1 ( )
elif Ii1IIi == 9002 :
 I1i11 ( )
elif Ii1IIi == 9003 :
 I11I ( )
elif Ii1IIi == 9004 :
 World1 ( )
elif Ii1IIi == 9005 :
 World2 ( iIIII1iIIii )
elif Ii1IIi == 9006 :
 World3 ( iIIII1iIIii )
elif Ii1IIi == 9007 :
 o0OOO0Oo ( )
elif Ii1IIi == 9008 :
 O0O00oo ( iIIII1iIIii )
elif Ii1IIi == 9009 :
 iiIIIii ( iIIII1iIIii )
elif Ii1IIi == 9010 :
 i1111iII1 ( )
elif Ii1IIi == 9011 :
 I1I1iiI11I1 ( iIIII1iIIii )
elif Ii1IIi == 50 :
 OOO0O0O ( iIIII1iIIii )
elif Ii1IIi == 9020 :
 champlist ( )
elif Ii1IIi == 9021 :
 O000Oo ( )
elif Ii1IIi == 9022 :
 IiiIi1II ( )
elif Ii1IIi == 9023 :
 IiII1IiiI ( )
elif Ii1IIi == 9024 :
 i11I ( iIIII1iIIii )
elif Ii1IIi == 9030 :
 II1ii1I1 ( iIIII1iIIii )
elif Ii1IIi == 9031 :
 Oo0ooO0oOo0 ( iIIII1iIIii )
elif Ii1IIi == 9032 :
 IIiii11 ( iIIII1iIIii )
elif Ii1IIi == 9033 :
 oO00o ( iIIII1iIIii )
elif Ii1IIi == 9034 :
 iI1i11 ( )
elif Ii1IIi == 7084 :
 OoI1iIi ( )
elif Ii1IIi == 7085 :
 Iii11 ( iIIII1iIIii )
elif Ii1IIi == 7086 :
 O0OoO0OOOo ( iIIII1iIIii , II11IiiIII , OOoOoo00Oo )
elif Ii1IIi == 7087 :
 o0i11iiII11i ( OOoOoo00Oo )
elif Ii1IIi == 9666 :
 i1Ii11II ( iIIII1iIIii )
elif Ii1IIi == 10100 : IIIiIIIi11I ( )
elif Ii1IIi == 101001 : iIi11 ( iIIII1iIIii )
elif Ii1IIi == 10105 : I11III111i1I ( iIIII1iIIii )
elif Ii1IIi == 10106 : O0ooOO0O00 ( iIIII1iIIii )
elif Ii1IIi == 10104 : ooO00OoO ( iIIII1iIIii )
elif Ii1IIi == 10107 : OoO0OOOo0Oo ( )
elif Ii1IIi == 10103 : OOO0O ( iIIII1iIIii )
elif Ii1IIi == 10108 : ooo00 ( iIIII1iIIii )
elif Ii1IIi == 10000 : Origin_Menu ( )
elif Ii1IIi == 10001 : iii11i1 ( )
elif Ii1IIi == 10002 : iI1i111I1Ii ( )
elif Ii1IIi == 10003 : oo0OO0Oo000oo ( )
elif Ii1IIi == 10004 : IIII1IiiI ( iIIII1iIIii )
elif Ii1IIi == 10005 : IIII11Ii1I11I ( )
elif Ii1IIi == 10006 : OOOOo0ooOOO0 ( iIIII1iIIii )
elif Ii1IIi == 10007 : OoO00o ( iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 10008 : o0OiI1 ( )
elif Ii1IIi == 10009 : iII1ii11I1I ( )
elif Ii1IIi == 10010 : IIiIoOOO ( iIIII1iIIii )
elif Ii1IIi == 10011 : oO0o0oo ( iIIII1iIIii )
elif Ii1IIi == 10012 : i11IIIiI1I ( iIIII1iIIii )
elif Ii1IIi == 10113 : GRABG ( iIIII1iIIii , o0OOOo )
elif Ii1IIi == 10109 : I1111OoO0O ( iIIII1iIIii )
elif Ii1IIi == 10013 : o00OOOOoOO ( iIIII1iIIii )
elif Ii1IIi == 10014 : oOIIii ( )
elif Ii1IIi == 10015 : OOO0o0O00O ( )
elif Ii1IIi == 10016 : iI1i1II ( iIIII1iIIii )
elif Ii1IIi == 10017 : OO0oO ( )
elif Ii1IIi == 10018 : OOoo000OO00 ( )
elif Ii1IIi == 10019 : oOi1IiIiIii11I ( )
elif Ii1IIi == 10020 : I11iIIiiIiIi ( )
elif Ii1IIi == 10021 : iii ( )
elif Ii1IIi == 10022 : Iii ( iIIII1iIIii )
elif Ii1IIi == 10023 : I11iiI1i ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 10024 : IIIiII1iIII ( iIIII1iIIii )
elif Ii1IIi == 10025 : IIiI1Ii ( )
elif Ii1IIi == 10026 : i11111i1I1IiI ( )
elif Ii1IIi == 10027 : I1IIo0o0OoOO00Oo ( )
elif Ii1IIi == 10028 : O00iI1iIIi ( )
elif Ii1IIi == 10029 : OOoo00o0OoO ( )
elif Ii1IIi == 423 : II11iII ( iIIII1iIIii )
elif Ii1IIi == 426 : Ooo0o0OO00oOO ( iIIII1iIIii )
elif Ii1IIi == 10030 : Izle_Films ( )
elif Ii1IIi == 10031 : Latest_Izle_Movies ( )
elif Ii1IIi == 10032 : Izle_Genres ( )
elif Ii1IIi == 10033 : Izle_Pop_Movies ( )
elif Ii1IIi == 10034 : Izle_Boxsets ( )
elif Ii1IIi == 10035 : Izle_Search ( )
elif Ii1IIi == 10036 : Izle_Genres_Movie ( iIIII1iIIii )
elif Ii1IIi == 10037 : Izle_Boxset_single ( iIIII1iIIii )
elif Ii1IIi == 10038 : Izle_IFRAME ( )
elif Ii1IIi == 10039 : Izle_Boxsets_Next ( iIIII1iIIii )
elif Ii1IIi == 10040 : Ooo00O ( )
elif Ii1IIi == 10041 : IiI1Iii1iIIII ( iIIII1iIIii )
elif Ii1IIi == 10042 : O00oi111II ( iIIII1iIIii )
elif Ii1IIi == 10043 : I1i1ii1IiI1i ( )
elif Ii1IIi == 10044 : OOoO00o00oo ( iIIII1iIIii )
elif Ii1IIi == 10045 : I1II1i1iIIi ( o0OOOo )
elif Ii1IIi == 10046 : O0o0ooo00o00 ( iIIII1iIIii )
elif Ii1IIi == 10047 : OOOOoO0O ( iIIII1iIIii )
elif Ii1IIi == 10048 : o0O0oO ( iIIII1iIIii )
elif Ii1IIi == 10049 : o0OooOOo0OO00 ( iIIII1iIIii )
elif Ii1IIi == 10050 : IIiiI1iiI ( )
elif Ii1IIi == 10051 : OoO0o ( )
elif Ii1IIi == 10052 : OOoO0ooo ( )
elif Ii1IIi == 10053 : Addon ( iIIII1iIIii )
elif Ii1IIi == 10054 : II11IIiii ( iIIII1iIIii , o0OOOo )
elif Ii1IIi == 10055 :
 oooo00OoOoO ( "addFavorite" )
 try :
  o0OOOo = o0OOOo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0OOOo = o0OOOo . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1I111i1I ( o0OOOo , iIIII1iIIii , II11IiiIII , OoOo00o0OO , iI11Ii1i11i )
elif Ii1IIi == 10056 :
 oooo00OoOoO ( "rmFavorite" )
 try :
  o0OOOo = o0OOOo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0OOOo = o0OOOo . split ( '  - ' ) [ 0 ]
 except :
  pass
 IIIIiiii ( o0OOOo )
elif Ii1IIi == 10057 :
 oooo00OoOoO ( "getFavorites" )
 ooooO0OO0O ( )
elif Ii1IIi == 10058 : i1IIii1i ( )
elif Ii1IIi == 10059 : Donators_Guide ( )
elif Ii1IIi == 10060 : iiiIi ( )
elif Ii1IIi == 10061 : OOoo0 ( )
elif Ii1IIi == 10062 : I1Ii11I11i1 ( o0OOOo , iIIII1iIIii , OOoOoo00Oo )
elif Ii1IIi == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + I11iii1Ii + ")" )
elif Ii1IIi == 10064 : OooOo ( )
elif Ii1IIi == 10065 : o00O0o ( iIIII1iIIii )
elif Ii1IIi == 10066 : iiiiii1Ii ( iIIII1iIIii )
elif Ii1IIi == 10068 : OOoOoOo ( iIIII1iIIii )
elif Ii1IIi == 10069 : IIIii11 ( iIIII1iIIii )
elif Ii1IIi == 10070 : iiIIIi1iIi ( iIIII1iIIii )
elif Ii1IIi == 10071 : Genie_Watch ( )
elif Ii1IIi == 10072 : OO0o0o0oo ( )
elif Ii1IIi == 10073 : IiiiIIi ( iIIII1iIIii )
elif Ii1IIi == 10074 : Ooo0 ( iIIII1iIIii )
elif Ii1IIi == 10075 : IIi1i1I11IIII ( II11IiiIII , o0OOOo , iIIII1iIIii )
elif Ii1IIi == 10076 : OOii11Ii1IiiI1 ( iIIII1iIIii )
elif Ii1IIi == 10077 : III ( iIIII1iIIii )
elif Ii1IIi == 10078 : iI1Ii11 ( )
elif Ii1IIi == 10079 : Genie_Watch_Tv_Shows ( )
elif Ii1IIi == 10080 : Genie_Watch_Tv_Genre ( iIIII1iIIii )
elif Ii1IIi == 10081 : Genie_Watch_TV_PlayRun ( iIIII1iIIii )
elif Ii1IIi == 10082 : Genie_Watch_TV_Episodes ( iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 10083 : Genie_Watch_Tv_Recent ( iIIII1iIIii )
elif Ii1IIi == 10084 : i1II1I1Iii1 ( )
elif Ii1IIi == 10085 : Iii1I1I11iiI1 ( )
elif Ii1IIi == 10086 : o0OOOO00O0Oo ( )
elif Ii1IIi == 20000 : Oo0OOO00oo0 ( )
elif Ii1IIi == 20001 : IIiIiI1i11iiII ( iIIII1iIIii )
elif Ii1IIi == 20002 : IIiiiIi1ii11I ( iIIII1iIIii )
elif Ii1IIi == 20003 : o0O00o00Ooo ( iIIII1iIIii )
elif Ii1IIi == 20004 : ooOoOoOoo ( iIIII1iIIii )
elif Ii1IIi == 20005 : oooI11Ii1 ( iIIII1iIIii )
elif Ii1IIi == 21004 : O000oOo ( )
elif Ii1IIi == 21005 : o00Oo00O0o ( iIIII1iIIii )
elif Ii1IIi == 21006 : ooooOOoO000O0 ( iIIII1iIIii )
elif Ii1IIi == 21007 : oO000 ( iIIII1iIIii )
elif Ii1IIi == 21008 : oOOo000oOoO0 ( iIIII1iIIii )
elif Ii1IIi == 21009 : oOoO00 ( iIIII1iIIii )
elif Ii1IIi == 30000 : iI1I11 ( )
elif Ii1IIi == 30001 : II1i11i1iI1I ( )
elif Ii1IIi == 100121 : Resolve ( iIIII1iIIii )
elif Ii1IIi == 30003 : O0OOoo ( )
elif Ii1IIi == 30004 : Ooii1II11IIII ( iIIII1iIIii )
elif Ii1IIi == 30005 : oO0o0o0 ( iIIII1iIIii )
elif Ii1IIi == 30006 : oOOooo0OoOOOO ( )
elif Ii1IIi == 30007 : o0o0OoOo00oOoo0oO ( )
elif Ii1IIi == 30008 : ooo0000oo0 ( iIIII1iIIii )
elif Ii1IIi == 30009 : i1IIi1ii1i1ii ( iIIII1iIIii )
elif Ii1IIi == 30010 : ii1i1 ( iIIII1iIIii )
elif Ii1IIi == 30011 : IiIi1i11i1II ( )
elif Ii1IIi == 30012 : OOo0o ( )
elif Ii1IIi == 30013 : OoOo00Oo0oo0O ( )
elif Ii1IIi == 30014 : oOoOo000Ooooo ( )
elif Ii1IIi == 30015 : i1II1I1I1 ( iIIII1iIIii , II11IiiIII , OoOo00o0OO )
elif Ii1IIi == 30016 : Ii1i1I1 ( iIIII1iIIii )
elif Ii1IIi == 30019 : O0O0o0o0oo0O ( iIIII1iIIii )
elif Ii1IIi == 30017 : O0oO00o0o0oo0 ( iIIII1iIIii )
elif Ii1IIi == 30018 : O0o ( iIIII1iIIii )
elif Ii1IIi == 30030 : O00Oo00o ( )
elif Ii1IIi == 30031 : II111111 ( )
elif Ii1IIi == 30032 : o0OO0o0o00o ( )
elif Ii1IIi == 30033 : II1 ( )
elif Ii1IIi == 30034 : IiII1Iiii ( )
elif Ii1IIi == 30035 : O0Oo0O0O0o ( iIIII1iIIii )
elif Ii1IIi == 30036 : iiII11ii1Ii ( iIIII1iIIii )
elif Ii1IIi == 30037 : iiI1Ii1iiii1i ( iIIII1iIIii )
elif Ii1IIi == 30038 : iII11IiIIII ( )
elif Ii1IIi == 30039 : iI1iIIIi1i ( )
elif Ii1IIi == 50000 : i1i1I ( )
elif Ii1IIi == 50001 : o0oOOO0 ( )
elif Ii1IIi == 50002 : iiiIiii11i1i ( iIIII1iIIii )
elif Ii1IIi == 50003 : Table_Menu ( OOoOoo00Oo )
elif Ii1IIi == 60000 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
elif Ii1IIi == 60001 : II1III ( )
elif Ii1IIi == 60002 : IiiIi1IiiiI ( o0OOOo )
elif Ii1IIi == 60003 : i11II1 ( iIIII1iIIii )
elif Ii1IIi == 600033 : i111iIi1i1 ( iIIII1iIIii )
elif Ii1IIi == 60004 : I1ii1 ( iIIII1iIIii )
elif Ii1IIi == 50004 : iI1iiiIiii ( )
elif Ii1IIi == 50005 : speedtest . runtest ( iIIII1iIIii )
elif Ii1IIi == 70001 : IiiIiiiiI1III ( )
elif Ii1IIi == 70002 : Ii1I1i1IiiI ( iIIII1iIIii )
elif Ii1IIi == 70003 : IiiiI1i ( iIIII1iIIii )
elif Ii1IIi == 70004 : I1iIi1i ( iIIII1iIIii )
elif Ii1IIi == 70005 : I1II1iI ( iIIII1iIIii )
elif Ii1IIi == 70006 : iIii1Ii11I1i ( )
elif Ii1IIi == 50006 : O0O0OOOOoo ( oo00 , Oo0oO0ooo )
elif Ii1IIi == 80000 : IiIIIIiI ( )
elif Ii1IIi == 80001 : resolvefilmon ( iIIII1iIIii )
elif Ii1IIi == 80002 : I1111ii11 ( )
elif Ii1IIi == 80003 : IIiIiii ( o0OOOo , iIIII1iIIii , "None" )
elif Ii1IIi == 80004 : III1iIi ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 80005 : O0O0o0oOOO ( )
elif Ii1IIi == 80006 : o0Ii11iIiiI ( iIIII1iIIii )
elif Ii1IIi == 80007 : o000 ( iIIII1iIIii )
elif Ii1IIi == 80008 : i11ii1 ( )
elif Ii1IIi == 80009 : O000o0O0 ( )
elif Ii1IIi == 80010 : O0000oOoO0o0 ( iIIII1iIIii )
elif Ii1IIi == 80011 : o00oI1i1IIIIIII ( iIIII1iIIii )
elif Ii1IIi == 80012 : I1IIiIi ( )
elif Ii1IIi == 90000 : IIiiiiiiII ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 90001 : tools ( )
elif Ii1IIi == 90002 : o0ooooO0o0O ( )
elif Ii1IIi == 90003 : O000000oooOOo ( iIIII1iIIii )
elif Ii1IIi == 90004 : I11iiI1 ( iIIII1iIIii )
elif Ii1IIi == 90005 : I1Ioo000oooooooO ( iIIII1iIIii )
elif Ii1IIi == 90006 : O0ooO0oOO ( iIIII1iIIii )
elif Ii1IIi == 90007 : ii111I1iII1i1 ( iIIII1iIIii )
elif Ii1IIi == 90008 : iiiI1iiIiII1 ( iIIII1iIIii )
elif Ii1IIi == 90009 : iI1IiI11Ii11i ( iIIII1iIIii )
elif Ii1IIi == 90010 : o0oO0oOO ( )
elif Ii1IIi == 90020 : iiIii ( )
elif Ii1IIi == 90021 : hellyeah2 ( iIIII1iIIii )
elif Ii1IIi == 90022 : hellyeah3 ( iIIII1iIIii )
elif Ii1IIi == 90023 : Ii1Ii1I ( )
elif Ii1IIi == 90024 : i1I ( iIIII1iIIii )
elif Ii1IIi == 90025 : OooOoOO0OO ( iIIII1iIIii )
if 1 - 1: IIiIiII11i
elif Ii1IIi == 90026 : oOiiIIIII ( )
elif Ii1IIi == 90027 : Ii1iii11I ( o0OOOo , iIIII1iIIii , OOoOoo00Oo )
elif Ii1IIi == 90028 : O00Oo ( iIIII1iIIii )
if 94 - 94: oOoO0o00OO0 * iiiiiiii1 % iiiiiiii1 % i1IiiiI1iI - iiiiiiii1
elif Ii1IIi == 900300 : II1I1iiIII1I1 ( )
elif Ii1IIi == 900301 : OOooO ( iIIII1iIIii )
elif Ii1IIi == 900302 : OO0o0o0oo0O ( iIIII1iIIii )
elif Ii1IIi == 90030 : I11I1IIiiII1 ( )
elif Ii1IIi == 90031 : Treplays ( )
elif Ii1IIi == 90032 : Treplays2 ( iIIII1iIIii )
elif Ii1IIi == 90033 : Treplays3 ( iIIII1iIIii )
elif Ii1IIi == 90034 : Treplays4 ( iIIII1iIIii )
elif Ii1IIi == 90035 : oO00OoOO ( iIIII1iIIii )
elif Ii1IIi == 90036 : O0OOo ( iIIII1iIIii )
elif Ii1IIi == 90039 : II11 ( iIIII1iIIii )
elif Ii1IIi == 90037 : Ooii1IIi1ii ( iIIII1iIIii )
elif Ii1IIi == 900377 : iiiii11I1 ( iIIII1iIIii )
elif Ii1IIi == 90038 : i1I1iIoOOoO ( )
if 38 - 38: I11i1ii1 - oOo % i1iIi - IIiIiII11i
elif Ii1IIi == 10090 : OO0 ( )
elif Ii1IIi == 10091 : o0OOoOoo ( iIIII1iIIii )
elif Ii1IIi == 10092 : I1IO00O0oO00o ( iIIII1iIIii )
elif Ii1IIi == 10093 : iIi1IIiiiI ( iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 10094 : O0OO0OOo00Oo ( iIIII1iIIii , II11IiiIII )
if 97 - 97: o0o00Oo0O . i1iIi
elif Ii1IIi == 10095 : o0Oooo ( )
elif Ii1IIi == 10096 : oOooOOo00ooO ( iIIII1iIIii )
elif Ii1IIi == 10097 : oO0o0oOo ( iIIII1iIIii )
elif Ii1IIi == 10098 : iIIi1 ( iIIII1iIIii )
elif Ii1IIi == 10099 : oOoOo0o00o ( iIIII1iIIii )
if 52 - 52: I11i1ii1
elif Ii1IIi == 10200 : Oo ( )
elif Ii1IIi == 10201 : Ooooo ( o0OOOo , iIIII1iIIii , OOoOoo00Oo )
elif Ii1IIi == 10202 : Iiii1 ( iIIII1iIIii )
elif Ii1IIi == 10203 : RT4 ( iIIII1iIIii )
if 86 - 86: O0Oooo0O / o0o00Oo0O + ii % OOOo00oo0oO
elif Ii1IIi == 90040 : oO0oo ( )
elif Ii1IIi == 90041 : o0000O00oO0O ( iIIII1iIIii )
elif Ii1IIi == 90042 : I1i1I1Iiiii1 ( iIIII1iIIii )
elif Ii1IIi == 90043 : i11Ii1IiIIIi ( iIIII1iIIii )
elif Ii1IIi == 90044 : o0OoooO ( iIIII1iIIii )
elif Ii1IIi == 90045 : ii11i1I1i ( )
elif Ii1IIi == 90046 : ooOO0 ( iIIII1iIIii )
elif Ii1IIi == 90050 : ooIi111iII ( )
elif Ii1IIi == 90051 : I11II11111i11 ( iIIII1iIIii )
elif Ii1IIi == 90052 : i1Ii ( iIIII1iIIii )
elif Ii1IIi == 90053 : ooOoOo ( iIIII1iIIii )
elif Ii1IIi == 90054 : iiI1iIII1ii ( iIIII1iIIii )
elif Ii1IIi == 90055 : OooooO ( )
if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . i1IiiiI1iI . i1iIi
elif Ii1IIi == 100001 : Stand_up ( )
if 81 - 81: IIiIiII11i + iii1i1iiiiIi % Ii / iiiiiiii1 . O0Oooo0O + IIiIiII11i
elif Ii1IIi == 100003 : iI1i1II ( iIIII1iIIii )
elif Ii1IIi == 100004 : I11Ii ( iIIII1iIIii )
elif Ii1IIi == 100005 : Resolve ( iIIII1iIIii )
elif Ii1IIi == 100008 : Search ( )
elif Ii1IIi == 100007 : oo00IIIIIIIiI ( iIIII1iIIii )
elif Ii1IIi == 100009 : yt . PlayVideo ( iIIII1iIIii )
elif Ii1IIi == 100010 : iii1IIIiiiI ( iIIII1iIIii )
elif Ii1IIi == 100100 : oOoO0O00oo ( II11IiiIII , iIIII1iIIii , i1I1Ii11i )
elif Ii1IIi == 100101 : II1iiI ( iIIII1iIIii , o0OOOo , OoOo00o0OO , i1I1Ii11i , II11IiiIII )
elif Ii1IIi == 100102 : iiii1 ( o0OOOo , iIIII1iIIii , II11IiiIII , OoOo00o0OO )
elif Ii1IIi == 100106 : o00ooo0 ( iIIII1iIIii , o0OOOo )
elif Ii1IIi == 100107 : oo0ooO0O0o ( )
elif Ii1IIi == 100108 : o0OO ( )
elif Ii1IIi == 100109 : iIi111 ( iIIII1iIIii )
elif Ii1IIi == 40000 : IIIIIIiIIIi1iii1 ( )
elif Ii1IIi == 40001 : O000oooO0 ( iIIII1iIIii )
elif Ii1IIi == 100110 : OOO000OOo0o0O ( iIIII1iIIii )
elif Ii1IIi == 100111 : II11IiIIiiI ( iIIII1iIIii )
elif Ii1IIi == 100112 : O0o0O00o0o ( iIIII1iIIii )
elif Ii1IIi == 100113 : Iii1 ( iIIII1iIIii )
elif Ii1IIi == 100114 : I111Iii1 ( iIIII1iIIii )
elif Ii1IIi == 100115 : ooOO0OOO00o ( iIIII1iIIii )
elif Ii1IIi == 100117 : i11i ( iIIII1iIIii )
elif Ii1IIi == 100118 : OOO0O0OOo ( iIIII1iIIii )
elif Ii1IIi == 100120 : OoOoO0ooooO0 ( iIIII1iIIii )
elif Ii1IIi == 1001200 : IIII1ii1 ( iIIII1iIIii )
elif Ii1IIi == 100210 : IIiIIIIiI ( iIIII1iIIii )
elif Ii1IIi == 100211 : OoIIiIIIII1I ( )
elif Ii1IIi == 100212 : Oo0oooo ( )
elif Ii1IIi == 100213 : OOOOoO0 ( )
elif Ii1IIi == 100214 : O0OOOOoO00oo ( )
elif Ii1IIi == 1000111 :
 oOOo0ooOOoO0 ( iIIII1iIIii )
 if 48 - 48: oOo0O0Ooo . oOoO0o00OO0 * iii1i1iiiiIi % ooOoO0O00 / O0Oooo0O * IIiIiII11i
elif Ii1IIi == 1001111 :
 iIIIiI ( o0OOOo , iIIII1iIIii )
 if 62 - 62: ooo0O * O0Oooo0O . iI11I1II1I1I / ooOoO0O00
elif Ii1IIi == 1002111 :
 iiOOOO0oo ( )
 if 75 - 75: ii / oOOoOooOo - iiiiiiii1 . ii . iii1i1iiiiIi % ooOoO0O00
elif Ii1IIi == 1003111 :
 oO0OO00oOO0o0 ( iIIII1iIIii , o0OOOo )
 if 7 - 7: iii1i1iiiiIi . ooOoO0O00 * Ii % Ii
elif Ii1IIi == 1004111 :
 iiIIII11i1 ( )
 if 54 - 54: oOo / oOo0O0Ooo . I1ii11iIi11i
elif Ii1IIi == 1005111 :
 i11IIiIi ( iIIII1iIIii , o0OOOo )
elif Ii1IIi == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( iIIII1iIIii , OoOo00o0OO ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( o0OOOo , iIIII1iIIii , OoOo00o0OO ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( o0OOOo , iIIII1iIIii , OoOo00o0OO ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1105000 :
 try :
  o0OOOo = o0OOOo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0OOOo = o0OOOo . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( o0OOOo , iIIII1iIIii , II11IiiIII , OoOo00o0OO , iI11Ii1i11i )
elif Ii1IIi == 1106000 :
 try :
  o0OOOo = o0OOOo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0OOOo = o0OOOo . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( o0OOOo )
elif Ii1IIi == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( iIIII1iIIii )
elif Ii1IIi == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( o0OOOo )
elif Ii1IIi == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif Ii1IIi == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( iIIII1iIIii )
elif Ii1IIi == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in iIIII1iIIii :
  import urlresolver
  iii11II1I = urlresolver . resolve ( iIIII1iIIii )
  II1I = xbmcgui . ListItem ( path = iii11II1I )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II1I )
 elif not iIIII1iIIii . startswith ( "plugin://plugin" ) or not any ( x in iIIII1iIIii for x in pyramid . g_ignoreSetResolved ) :
  II1I = xbmcgui . ListItem ( path = iIIII1iIIii )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II1I )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + iIIII1iIIii + ')' )
elif Ii1IIi == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( o0OOOo , playlist )
elif Ii1IIi == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( iIIII1iIIii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( iIIII1iIIii , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1117000 :
 iIIII1iIIii , iIo0OOOOooo = getRegexParsed ( regexs , iIIII1iIIii )
 if iIIII1iIIii :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( iIIII1iIIii , o0OOOo , II11IiiIII , iIo0OOOOooo )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif Ii1IIi == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 Ii11II = youtubedl . single_YD ( iIIII1iIIii )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( Ii11II , o0OOOo , II11IiiIII )
elif Ii1IIi == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( iIIII1iIIii ) , o0OOOo , II11IiiIII , True )
elif Ii1IIi == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , o0OOOo , 'video' )
elif Ii1IIi == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( iIIII1iIIii , o0OOOo , 'video' )
elif Ii1IIi == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( iIIII1iIIii , o0OOOo , 'audio' )
elif Ii1IIi == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( iIIII1iIIii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1126000 :
 o0OOOo = o0OOOo . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( iIIII1iIIii , search_term = o0OOOo [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( iIIII1iIIii )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif Ii1IIi == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif Ii1IIi == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif Ii1IIi == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( o0OOOo , iIIII1iIIii , II11IiiIII , OoOo00o0OO )
elif Ii1IIi == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( iIIII1iIIii , II11IiiIII , OoOo00o0OO ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( iIIII1iIIii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( o0OOOo , iIIII1iIIii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( iIIII1iIIii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( iIIII1iIIii )
elif Ii1IIi == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( iIIII1iIIii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( iIIII1iIIii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif Ii1IIi == 9050000 : i1IIi1i1Ii1 ( )
elif Ii1IIi == 9060000 : iIIIiI ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 9080000 : ooOOOoOoOOO0 ( )
elif Ii1IIi == 9070000 : I1I1IiIi1 ( )
elif Ii1IIi == 9090000 : iiiiiII ( )
elif Ii1IIi == 9100000 : O000O ( )
elif Ii1IIi == 9110000 : I11IiIIIi ( )
elif Ii1IIi == 9110001 : OOo0O0oo0OO0O ( iIIII1iIIii )
elif Ii1IIi == 9110002 : i1iiIIIi ( iIIII1iIIii , o0OOOo , II11IiiIII )
elif Ii1IIi == 9110003 : O0oOoo0OoO0O ( o0OOOo , i1I1Ii11i )
elif Ii1IIi == 9110005 : i1iIIII1iiIIi ( OOoOoo00Oo , iIIII1iIIii )
elif Ii1IIi == 9110004 : IiIIII ( )
elif Ii1IIi == 9110010 : IiIoO0oo0 ( iIIII1iIIii )
elif Ii1IIi == 9110011 : I1IiII ( )
elif Ii1IIi == 9110012 : oOoOo0o0 ( iIIII1iIIii , o0OOOo )
elif Ii1IIi == 9110013 : oo00OoO ( iIIII1iIIii )
elif Ii1IIi == 9110014 : II1i11i1iIi11 ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 9110015 : I1iI1I1 ( )
elif Ii1IIi == 9999999 : I1iI11IiiI11i ( )
elif Ii1IIi == 19999999 : o0OOO00ooo ( )
elif Ii1IIi == 1999990 : oooI11iI1I ( )
elif Ii1IIi == 21999990 : iIiIi1I ( )
elif Ii1IIi == 21999991 : iiii11i ( iIIII1iIIii )
elif Ii1IIi == 21999992 : III11II1I1Ii1 ( iIIII1iIIii )
elif Ii1IIi == 21999993 : O00Oo0o000oO ( iIIII1iIIii )
elif Ii1IIi == 21999994 : oO0o00oOOooO0 ( iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 21999995 : OOOoO000 ( iIIII1iIIii )
elif Ii1IIi == 21999996 : IiIi1ii111i1 ( iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 21999997 : oOoo000 ( iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 21999998 : OooOo00o ( o0OOOo , iIIII1iIIii , II11IiiIII )
elif Ii1IIi == 219999989 : OOI1iI1ii1II ( )
elif Ii1IIi == 219999990 : I1i ( all = True )
elif Ii1IIi == 219999991 : IIii1 ( )
elif Ii1IIi == 219999992 : IiIi11i ( )
elif Ii1IIi == 300000000 : oOOO00o000o ( )
elif Ii1IIi == 300000001 : I1Ii1111iIi ( iIIII1iIIii )
elif Ii1IIi == 300000002 : IiIi1iIIi1 ( )
elif Ii1IIi == 300000003 : Iiiiii111i1ii ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 300000004 : i11iiI1111 ( iIIII1iIIii )
elif Ii1IIi == 300000005 : OO0ooo0o0O0Oooooo ( iIIII1iIIii )
elif Ii1IIi == 300000006 : O0 ( o0OOOo , iIIII1iIIii )
elif Ii1IIi == 300000007 : OoOo0oOooOoOO ( )
elif Ii1IIi == 300000008 : IIi ( )
elif Ii1IIi == 300000009 : oOoO00oo0O ( )
if 76 - 76: i1iIi * iii1i1iiiiIi / oOoO0o00OO0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
