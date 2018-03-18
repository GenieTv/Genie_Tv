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
I1IiI = "3.7.0"
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
  OoOoO ( 'Change Log 18/03/2018 - v3.7.0' , '[COLORsteelblue]Free Live Tv Section Added,[CR][COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
  os . makedirs ( ooooooO0oo )
def Ii1I1i ( ) :
 OoOoO ( 'Change Log 18/03/2018 - v3.7.0' , '[COLORsteelblue]Free Live Tv Section Added,[CR][COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
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
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Ultimate Live List[/COLOR]' , '' , 4009 , I1IIIii + 'GTV.png' , Oo00OOOOO , 'GenieTv Ultimate (Paid Service)' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , I1IIIii + 'tommys.png' , Oo00OOOOO , 'Tommys Sports' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Tv[/COLOR]' , '' , 300000000 , I1IIIii + 'GTV.png' , Oo00OOOOO , 'Free Live Streams - [COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
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
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Ultimate Live List[/COLOR]' , '' , 40099 , I1IIIii + 'GTV.png' , Oo00OOOOO , 'GenieTv Ultimate (Paid Service)' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , I1IIIii + 'tommys.png' , Oo00OOOOO , 'Tommys Sports' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Tv[/COLOR]' , '' , 300000000 , I1IIIii + 'GTV.png' , Oo00OOOOO , 'Free Live Streams - [COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 if O0oo0OO0 . getSetting ( 'Streams' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( O00OOOoOoo0O ) , 4002 , I1IIIii + 'Streams.png' , Oo00OOOOO , 'VOD Categories' )
 if O0oo0OO0 . getSetting ( 'Maintainance' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( O00OOOoOoo0O ) , 3 , I1IIIii + 'Maintenance.png' , Oo00OOOOO , 'MAINTENANCE' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , I1IIIii + 'tools.png' , Oo00OOOOO , 'Tools' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 87 - 87: I1ii11iIi11i . oOo0O0Ooo - IIiIiII11i + o0o00Oo0O / I1ii11iIi11i / OOOo00oo0oO
def IiI ( ) :
 O0O0ooOOO ( '[COLORwhite]Source 1 [COLORsteelblue]- [COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 oOOo0 = i11111IIIII ( 'https://github.com/fluxustv/IPTV' )
 IIIii1I = re . compile ( 'class="css-truncate css-truncate-target"><a class="js-navigation-open" title="([^"]*)" id=".+?" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 oo00O00oO = i11111IIIII ( 'http://autoiptv.net/pages/playlists/' )
 ooO0OO = re . compile ( '<span class="title">(.+?)</span>.+?<a class="no-style" href="([^"]*)"' , re . DOTALL ) . findall ( oo00O00oO )
 for O000OOO , IIo0o0O0O00oOOo in ooO0OO :
  if 'Adult' in O000OOO :
   o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' )
  elif 'Kodi' in O000OOO :
   pass
  elif 'Filter' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' , IIo0o0O0O00oOOo , 300000004 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' )
 O0O0ooOOO ( ' ' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ' ' )
 O0O0ooOOO ( '[COLORwhite]Source 2 [COLORsteelblue]- [COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 for O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  if 'READ' in O000OOO :
   pass
  elif 'list' in O000OOO :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Channel Lists[/COLOR]' , ( 'http://raw.githubusercontent.com' + IIo0o0O0O00oOOo ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']Channel ' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[/COLOR]' )
  elif 'faith' in O000OOO :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Faith Channels[/COLOR]' , ( 'http://raw.githubusercontent.com' + IIo0o0O0O00oOOo ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']Channel ' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[/COLOR]' )
  elif 'cctv' in O000OOO :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Cctv[/COLOR]' , ( 'http://raw.githubusercontent.com' + IIo0o0O0O00oOOo ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']Channel ' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[/COLOR]' )
  elif 'radio' in O000OOO :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Radio Stations[/COLOR]' , ( 'http://raw.githubusercontent.com' + IIo0o0O0O00oOOo ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']Channel ' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[/COLOR]' )
  elif 'xxx' in O000OOO :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Filth[/COLOR]' , ( 'http://raw.githubusercontent.com' + IIo0o0O0O00oOOo ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']Channel ' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[/COLOR]' )
  elif 'cinema' in O000OOO :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Cinema[COLORorangered] - VOD[/COLOR]' , ( 'http://raw.githubusercontent.com' + IIo0o0O0O00oOOo ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[COLORorangered] - VOD[/COLOR]' )
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[/COLOR]' , ( 'http://raw.githubusercontent.com' + IIo0o0O0O00oOOo ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']' + ( O000OOO ) . replace ( '.m3u' , '' ) + '[/COLOR]' )
 O0O0ooOOO ( ' ' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ' ' )
 O0O0ooOOO ( '[COLORwhite]Source 3 [COLORsteelblue]- [COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']International[/COLOR]' , 'https://raw.githubusercontent.com/teamblue65/LISTAS/master/LISTA_SSIPTV' , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']International[/COLOR]' )
 O0O0ooOOO ( ' ' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ' ' )
 O0O0ooOOO ( '[COLORwhite]Source 4 [COLORsteelblue]- [COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Big List[/COLOR]' , 'https://gitlab.com/notisj/m3u-lists/raw/master/all.m3u' , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLOR' + iiI1IiI + ']Big List[/COLOR]' )
def OO0O0 ( url ) :
 O0O0ooOOO ( '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' , '' , '' , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORorangered]They Either Work Or They Don\'t[/COLOR]' )
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<span class="title">(.+?)</span>.+?<a class="no-style" href="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in IIIii1I :
  if 'Adult' in O000OOO :
   o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '[/COLOR]' , url , 300000006 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' )
  elif 'Kodi' in O000OOO :
   pass
  elif 'Filter' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' , url , 300000004 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' )
def I11I11 ( url ) :
 if url == 'http://' : return False
 try :
  i1i = urllib2 . Request ( url )
  i1i . add_header ( 'User-Agent' , IiII )
  iiI111I1iIiI = urllib2 . urlopen ( i1i )
  iiI111I1iIiI . close ( )
 except Exception , o000O0O :
  return o000O0O
 return True
def I1i1i1iii ( name , url ) :
 if 16 - 16: i1iIi + I11i1ii1 * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
 if 67 - 67: ii / oOo0O0Ooo * i1iIi + i1IiiiI1iI
 if 65 - 65: ii - oOoO0o00OO0 / oOOoOooOo / IIiIiII11i / ooOoO0O00
 if 71 - 71: O0Oooo0O + i1iIi
 if 28 - 28: OoOo0o
 I11ii1IIiIi = name
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 OoOOo0OOoO = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 ooO0O00Oo0o = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 OOO = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( oOOo0 )
 Oo0o00OO0000 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for name , I1i , O00Oooo , iIIIiIi , url in iI111i :
  if I11ii1IIiIi in O00Oooo :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( name + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1i , I1i , ( '[COLORsteelblue]' + ( name + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for I1i , O00Oooo , iIIIiIi , url in IIi11i1i1iI1 :
  if I11ii1IIiIi in O00Oooo :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1i , I1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00Oooo , iIIIiIi , url in OoOOo0OOoO :
  if I11ii1IIiIi in O00Oooo :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00Oooo , I1i , iIIIiIi , url in ooO0O00Oo0o :
  if I11ii1IIiIi in O00Oooo :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1i , I1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iIIIiIi , url in OOO :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00Oooo , iIIIiIi , url in Oo0o00OO0000 :
  if I11ii1IIiIi in O00Oooo :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[CR]Offline[/COLOR]' ) . replace ( '_' , ' ' ) )
def i11I ( name , url ) :
 oOOo0 = i11111IIIII ( url )
 o00Oo0oooooo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for iIIIiIi , url in o00Oo0oooooo :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 76 - 76: i1IiiiI1iI / OoOo0o . o0o00Oo0O % oOo0O0Ooo . ooo0O + I11i1ii1
def o0o ( url ) :
 url = url
 oo0 = [ '[COLOR' + iiI1IiI + '](_) _No Group[/COLOR]' , '[COLOR' + iiI1IiI + '](UK) United Kingdom[/COLOR]' , '[COLOR' + iiI1IiI + '](US) United States[/COLOR]' , '[COLOR' + iiI1IiI + '](AL) Albania[/COLOR]' , '[COLOR' + iiI1IiI + '](AS) American Samoa[/COLOR]' , '[COLOR' + iiI1IiI + '](AR) Argentina[/COLOR]' , '[COLOR' + iiI1IiI + '](AU) Australia[/COLOR]' , '[COLOR' + iiI1IiI + '](AZ) Azerbaijan[/COLOR]' , '[COLOR' + iiI1IiI + '](BY) Belarus[/COLOR]' , '[COLOR' + iiI1IiI + '](BE) Belgium[/COLOR]' , '[COLOR' + iiI1IiI + '](BO) Bolivia[/COLOR]' , '[COLOR' + iiI1IiI + '](BR) Brazil[/COLOR]' , '[COLOR' + iiI1IiI + '](CM) Cameroon[/COLOR]' , '[COLOR' + iiI1IiI + '](CA) Canada[/COLOR]' , '[COLOR' + iiI1IiI + '](CO) Colombia[/COLOR]' , '[COLOR' + iiI1IiI + '](CZ) Czech Republic[/COLOR]' , '[COLOR' + iiI1IiI + '](DO) Dominican Republic[/COLOR]' , '[COLOR' + iiI1IiI + '](EC) Ecuador[/COLOR]' , '[COLOR' + iiI1IiI + '](FO) Faroe Islands[/COLOR]' , '[COLOR' + iiI1IiI + '](FR) France[/COLOR]' , '[COLOR' + iiI1IiI + '](DE) Germany[/COLOR]' , '[COLOR' + iiI1IiI + '](GR) Greece[/COLOR]' , '[COLOR' + iiI1IiI + '](IS) Iceland[/COLOR]' , '[COLOR' + iiI1IiI + '](IN) India[/COLOR]' , '[COLOR' + iiI1IiI + '](ID) Indonesia[/COLOR]' , '[COLOR' + iiI1IiI + '](IR) Iran[/COLOR]' , '[COLOR' + iiI1IiI + '](IT) Italy[/COLOR]' , '[COLOR' + iiI1IiI + '](LA) Laos[/COLOR]' , '[COLOR' + iiI1IiI + '](MO) Macau[/COLOR]' , '[COLOR' + iiI1IiI + '](MX) Mexico[/COLOR]' , '[COLOR' + iiI1IiI + '](NL) Netherlands[/COLOR]' , '[COLOR' + iiI1IiI + '](NE) Niger[/COLOR]' , '[COLOR' + iiI1IiI + '](PK) Pakistan[/COLOR]' , '[COLOR' + iiI1IiI + '](PA) Panama[/COLOR]' , '[COLOR' + iiI1IiI + '](PE) Peru[/COLOR]' , '[COLOR' + iiI1IiI + '](PL) Poland[/COLOR]' , '[COLOR' + iiI1IiI + '](PT) Portugal[/COLOR]' , '[COLOR' + iiI1IiI + '](RO) Romania[/COLOR]' , '[COLOR' + iiI1IiI + '](RU) Russia[/COLOR]' , '[COLOR' + iiI1IiI + '](SL) Sierra Leone[/COLOR]' , '[COLOR' + iiI1IiI + '](EX-YU) Slovenia[/COLOR]' , '[COLOR' + iiI1IiI + '](SO) Somalia[/COLOR]' , '[COLOR' + iiI1IiI + '](SP) Spain[/COLOR]' , '[COLOR' + iiI1IiI + '](SE) Sweden[/COLOR]' , '[COLOR' + iiI1IiI + '](CH) Switzerland[/COLOR]' , '[COLOR' + iiI1IiI + '](TH) Thailand[/COLOR]' , '[COLOR' + iiI1IiI + '](TR) Turkey[/COLOR]' , '[COLOR' + iiI1IiI + '](UA) Ukraine[/COLOR]' , '[COLOR' + iiI1IiI + '](VE) Venezuela[/COLOR]' , '[COLOR' + iiI1IiI + '](WW) World Wide[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Select Country[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  O000OOO = '(_)'
 if oOOOoo00 == 1 :
  O000OOO = '(UK)'
 if oOOOoo00 == 2 :
  O000OOO = '(US)'
 if oOOOoo00 == 3 :
  O000OOO = '(AL)'
 if oOOOoo00 == 4 :
  O000OOO = '(AS)'
 if oOOOoo00 == 5 :
  O000OOO = '(AR)'
 if oOOOoo00 == 6 :
  O000OOO = '(AU)'
 if oOOOoo00 == 7 :
  O000OOO = '(AZ)'
 if oOOOoo00 == 8 :
  O000OOO = '(BY)'
 if oOOOoo00 == 9 :
  O000OOO = '(BE)'
 if oOOOoo00 == 10 :
  O000OOO = '(BO)'
 if oOOOoo00 == 11 :
  O000OOO = '(BR)'
 if oOOOoo00 == 12 :
  O000OOO = '(CM)'
 if oOOOoo00 == 13 :
  O000OOO = '(CA)'
 if oOOOoo00 == 14 :
  O000OOO = '(CO)'
 if oOOOoo00 == 15 :
  O000OOO = '(CZ)'
 if oOOOoo00 == 16 :
  O000OOO = '(DO)'
 if oOOOoo00 == 17 :
  O000OOO = '(EC)'
 if oOOOoo00 == 18 :
  O000OOO = '(FO)'
 if oOOOoo00 == 19 :
  O000OOO = '(FR)'
 if oOOOoo00 == 20 :
  O000OOO = '(DE)'
 if oOOOoo00 == 21 :
  O000OOO = '(GR)'
 if oOOOoo00 == 22 :
  O000OOO = '(IS)'
 if oOOOoo00 == 23 :
  O000OOO = '(IN)'
 if oOOOoo00 == 24 :
  O000OOO = '(ID)'
 if oOOOoo00 == 25 :
  O000OOO = '(IR)'
 if oOOOoo00 == 26 :
  O000OOO = '(IT)'
 if oOOOoo00 == 27 :
  O000OOO = '(LA)'
 if oOOOoo00 == 28 :
  O000OOO = '(MO)'
 if oOOOoo00 == 29 :
  O000OOO = '(MX)'
 if oOOOoo00 == 30 :
  O000OOO = '(NL)'
 if oOOOoo00 == 31 :
  O000OOO = '(NE)'
 if oOOOoo00 == 32 :
  O000OOO = '(PK)'
 if oOOOoo00 == 33 :
  O000OOO = '(PA)'
 if oOOOoo00 == 34 :
  O000OOO = '(PE)'
 if oOOOoo00 == 35 :
  O000OOO = '(PL)'
 if oOOOoo00 == 36 :
  O000OOO = '(PT)'
 if oOOOoo00 == 37 :
  O000OOO = '(RO)'
 if oOOOoo00 == 38 :
  O000OOO = '(RU)'
 if oOOOoo00 == 39 :
  O000OOO = '(SL)'
 if oOOOoo00 == 40 :
  O000OOO = '(EX-YU)'
 if oOOOoo00 == 41 :
  O000OOO = '(SO)'
 if oOOOoo00 == 42 :
  O000OOO = '(SP)'
 if oOOOoo00 == 43 :
  O000OOO = '(SE)'
 if oOOOoo00 == 44 :
  O000OOO = '(CH)'
 if oOOOoo00 == 45 :
  O000OOO = '(TH)'
 if oOOOoo00 == 46 :
  O000OOO = '(TR)'
 if oOOOoo00 == 47 :
  O000OOO = '(UA)'
 if oOOOoo00 == 48 :
  O000OOO = '(VE)'
 if oOOOoo00 == 49 :
  O000OOO = '(WW)'
 I1i1i1iii ( O000OOO , url )
 if 9 - 9: o0o00Oo0O % o0o00Oo0O - ooo0O
def OoO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 OoOOo0OOoO = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 ooO0O00Oo0o = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 OOO = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( oOOo0 )
 Oo0o00OO0000 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 o00Oo0oooooo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for O000OOO , I1i , O00Oooo , iIIIiIi , url in iI111i :
  if 'INFO' in O00Oooo :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O000OOO + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1i , I1i , ( '[COLORsteelblue]' + ( O000OOO + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for I1i , O00Oooo , iIIIiIi , url in IIi11i1i1iI1 :
  if 'INFO' in O00Oooo :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1i , I1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00Oooo , iIIIiIi , url in OoOOo0OOoO :
  if 'INFO' in O00Oooo :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00Oooo , I1i , iIIIiIi , url in ooO0O00Oo0o :
  if 'INFO' in O00Oooo :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1i , I1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iIIIiIi , url in OOO :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00Oooo , iIIIiIi , url in Oo0o00OO0000 :
  if 'INFO' in O00Oooo :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + O00Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iIIIiIi , url in o00Oo0oooooo :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 12 - 12: o0o00Oo0O - ooo0O
def oOoO00O0 ( url ) :
 if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
  OOIi1iI111II1I1 ( ( url ) . strip ( ) )
 else :
  try :
   OOIi1iI111II1I1 ( ( url ) . strip ( ) )
  except :
   pass
  else :
   OOIi1iI111II1I1 ( 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + url )
   if 91 - 91: OoOo0o % OoOo0o - oOo0O0Ooo
   if 18 - 18: i1IiiiI1iI - Ii / IIiIiII11i . OoOo0o
def tools ( ) :
 oo0 = [ '[COLOR' + iiI1IiI + ']Change Log[/COLOR]' , '[COLOR' + iiI1IiI + ']Force Genie Update Kodi[/COLOR]' , '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  Ii1I1i ( )
 if oOOOoo00 == 1 :
  Iii1I1I11iiI1 ( )
 if oOOOoo00 == 2 :
  OoOo00o0O00 ( )
 if oOOOoo00 == 3 :
  iiI ( IIo0o0O0O00oOOo )
 if oOOOoo00 == 4 :
  iI111I11I1I1 . ok ( oo00 , Oo0oO0ooo )
 if oOOOoo00 == 5 :
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 if oOOOoo00 == 6 :
  oOoo0oOo00 ( )
  if 32 - 32: oOo0O0Ooo % iI11I1II1I1I / ooOoO0O00 - oOo0O0Ooo
def I1III1111iIi ( ) :
 o00oOOooOOo0o ( 'Stories' , 'http://etc.usf.edu/lit2go/books/' , 21999995 , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , '' )
 o00oOOooOOo0o ( 'Virtual FirePlaces' , 'http://www.virtual-fireplace.net/fireplaces.html' , 21999991 , 'http://www.virtual-fireplace.net/files/theme/burning-log.gif' , 'http://www.virtual-fireplace.net/files/theme/burning-log1.gif' , '' )
 o00oOOooOOo0o ( 'Nature Sounds' , 'http://www.virtual-fireplace.net/sounds.html' , 21999993 , 'http://www.virtual-fireplace.net/files/theme/sound.gif' , 'http://www.virtual-fireplace.net/files/theme/sound-bw.gif' , '' )
def I1i111I ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for url , I1i , O000OOO in IIIii1I :
  O0O0ooOOO ( O000OOO , url , 21999992 , 'http://www.virtual-fireplace.net/' + I1i , 'http://www.virtual-fireplace.net/' + I1i , O000OOO )
def OooOo0oo0O0o00O ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( 'rel="canonical" href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for url in IIIii1I :
  url = ( url ) . replace ( '//www.youtube.com/embed/' , '' ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' )
  yt . PlayVideo ( url )
def I1i11 ( url ) :
 o00oOOooOOo0o ( 'Rain And Thunder' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Water And Forests' , 'http://www.virtual-fireplace.net/water-and-forest.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Beach And Ocean' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , '' )
def IiIi1I1 ( url , iconimage ) :
 I1i = iconimage
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in IIIii1I :
  O0O0ooOOO ( O000OOO , 'http:' + url , 21999992 , I1i , I1i , '' )
def IiIIi1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( 'data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , O000OOO , url , IIIIiii1IIii in IIIii1I :
  o00oOOooOOo0o ( O000OOO , url , 21999996 , I1i , I1i , ( IIIIiii1IIii ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def II1i11I ( url , iconimage ) :
 I1i = iconimage
 IIIIiii1IIii = 'desc'
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , ii1I1IIii11 in IIIii1I :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR] - Audio' , url , 21999997 , I1i , I1i , ( ii1I1IIii11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( ii1I1IIii11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR] - Text' , url , 21999998 , I1i , I1i , ( ii1I1IIii11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( ii1I1IIii11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def O0o0oO ( url , iconimage ) :
 I1i = iconimage
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<a href="([^"]*)">Audio</a>' ) . findall ( oOOo0 )
 for url in IIIii1I :
  OOIi1iI111II1I1 ( url )
def IIIIiIiIi1 ( name , url , iconimage ) :
 I1i = iconimage
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '</audio>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for ii1I1IIii11 in IIIii1I :
  OoOoO ( ( name ) . replace ( ' - Text' , '' ) , ( ii1I1IIii11 ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  if 2 - 2: iiiiiiii1 % iI11I1II1I1I * iI11I1II1I1I . ooo0O / iiiiiiii1
  if 27 - 27: oOo + oOOoOooOo - ooOoO0O00
def O00oOOooo ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , I1i , IIIIiii1IIii , iI1iIii11Ii , O000OOO in IIIii1I :
  O0O0ooOOO ( O000OOO , url , 21009 , I1i , iI1iIii11Ii , IIIIiii1IIii )
  if 8 - 8: oOoO0o00OO0 * O0Oooo0O . oOOoOooOo / i1iIi - I1ii11iIi11i % o0o00Oo0O
def iI1i1i11I1iI ( url ) :
 url = url
 o0O0oo0OO0O = oOOo0O00o ( )
 if o0O0oo0OO0O ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif o0O0oo0OO0O ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 68 - 68: OOOo00oo0oO . i1IiiiI1iI % ii . i1IiiiI1iI
  if 64 - 64: iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + ii . oOo
def oOIIiIi ( ) :
 IIo0o0O0O00oOOo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( IIo0o0O0O00oOOo , Iiii1iI1i , o0oO0 )
 I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1ii1ii11i1I
 print '======================================='
 extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
 o0OoOO ( IIo0o0O0O00oOOo )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0O0Oo00 ( )
def oOoO00o ( ) :
 oO00O0 = IIi1IIIi ( )
 O00Ooo = oO00O0 . replace ( ooOoOoo0O , "" )
 if os . path . exists ( oO00O0 ) or not oO00O0 == False :
  OOOO0OOO = open ( oO00O0 , mode = 'r' ) ; i1i1ii = OOOO0OOO . read ( ) ; OOOO0OOO . close ( )
  OoOoO ( "%s - %s" % ( oo00 , O00Ooo ) , i1i1ii )
 else :
  iII1ii1 ( 'View Log' , 'No Log File Found!' )
def I1i1iiiI1 ( log = None , count = None , all = None ) :
 if log == None :
  iIIi = oO0o00oo0 ( True )
  ii1IIII = oO0o00oo0 ( True , True )
  if not ii1IIII == False and not iIIi == False :
   oO00oOooooo0 = iI111I11I1I1 . select ( oOo0oooo00o , [ "View %s: %s error(s)" % ( iIIi . replace ( ooOoOoo0O , "" ) , I1i1iiiI1 ( iIIi , True , True ) ) , "View %s: %s error(s)" % ( ii1IIII . replace ( ooOoOoo0O , "" ) , I1i1iiiI1 ( ii1IIII , True , True ) ) ] )
   if oO00oOooooo0 == - 1 : iII1ii1 ( '[COLOR %s]View Log[/COLOR]' % oOoO0OOooOoO , '[COLOR %s]View Log Cancelled![/COLOR]' % i1II1I1Iii1 ) ; return
  elif iIIi == False and ii1IIII == False :
   iII1ii1 ( '[COLOR %s]View Log[/COLOR]' % oOoO0OOooOoO , '[COLOR %s]No Log File Found![/COLOR]' % i1II1I1Iii1 )
   return
  elif not iIIi == False : oO00oOooooo0 = 0
  elif not ii1IIII == False : oO00oOooooo0 = 1
  log = iIIi if oO00oOooooo0 == 0 else ii1IIII
 if log == False :
  if count == None :
   iII1ii1 ( "[COLOR %s]%s[/COLOR]" % ( oOoO0OOooOoO , oOo0oooo00o ) , "[COLOR %s]Log File not Found[/COLOR]" % i1II1I1Iii1 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   OOOO0OOO = open ( log , mode = 'r' ) ; iiI11Iii = OOOO0OOO . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; OOOO0OOO . close ( )
   iI111i = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( iiI11Iii )
   if not count == None :
    if all == None :
     O0o0O0 = 0
     for Ii1II1I11i1 in iI111i :
      if o0OOO in Ii1II1I11i1 : O0o0O0 += 1
     return O0o0O0
    else : return len ( iI111i )
   if len ( iI111i ) > 0 :
    O0o0O0 = 0 ; i1i1ii = ""
    for Ii1II1I11i1 in iI111i :
     if all == None and not o0OOO in Ii1II1I11i1 : continue
     else :
      O0o0O0 += 1
      i1i1ii += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( O0o0O0 , Ii1II1I11i1 . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( i1111 , '' ) )
    if O0o0O0 > 0 :
     OoOoO ( oOo0oooo00o , i1i1ii )
    else : iII1ii1 ( oOo0oooo00o , "No Errors Found in Log" )
   else : iII1ii1 ( oOo0oooo00o , "No Errors Found in Log" )
  else : iII1ii1 ( oOo0oooo00o , "Log File not Found" )
def oO0o00oo0 ( file = False , old = False , wizard = False ) :
 if wizard == True :
  if not os . path . exists ( Oo0o0000o0o0 ) : return False
  else :
   if file == True :
    return Oo0o0000o0o0
   else :
    oOoooooOoO = open ( Oo0o0000o0o0 , 'r' )
    Ii111 = oOoooooOoO . read ( )
    oOoooooOoO . close ( )
    return Ii111
 I111i1i1111 = 0
 IIII1 = os . listdir ( ooOoOoo0O )
 I1I1i = [ ]
 if 1 - 1: i1IiiiI1iI % OoOo0o + o0o00Oo0O + ooOoO0O00 - oOo
 for Ii1II1I11i1 in IIII1 :
  if old == True and Ii1II1I11i1 . endswith ( '.old.log' ) : I1I1i . append ( os . path . join ( ooOoOoo0O , Ii1II1I11i1 ) )
  elif old == False and Ii1II1I11i1 . endswith ( '.log' ) and not Ii1II1I11i1 . endswith ( '.old.log' ) : I1I1i . append ( os . path . join ( ooOoOoo0O , Ii1II1I11i1 ) )
  if 22 - 22: oOo0O0Ooo % oOoO0o00OO0
 if len ( I1I1i ) > 0 :
  I1I1i . sort ( key = lambda OOOO0OOO : os . path . getmtime ( OOOO0OOO ) )
  if file == True : return I1I1i [ - 1 ]
  else :
   oOoooooOoO = open ( I1I1i [ - 1 ] , 'r' )
   Ii111 = oOoooooOoO . read ( )
   oOoooooOoO . close ( )
   return Ii111
 else :
  return False
  if 57 - 57: OoOo0o + o0o00Oo0O . i1iIi
def oOIIiIi ( ) :
 IIo0o0O0O00oOOo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( IIo0o0O0O00oOOo , Iiii1iI1i , o0oO0 )
 I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1ii1ii11i1I
 print '======================================='
 extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
 o0OoOO ( IIo0o0O0O00oOOo )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0O0Oo00 ( )
def iIi1i1iIi1iI ( ) :
 iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']Todays Games[/COLOR]' , '' , 90030 , I1IIIii + 'tgames.png' , Oo00OOOOO , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport[/COLOR]' , 'http://www.replaymatches.com/' , 90037 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Replays[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , I1IIIii + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 68 - 68: OoOo0o
 if 82 - 82: iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % I11i1ii1 / i1iIi . i1iIi
 if 14 - 14: ooo0O . OoOo0o . i1IiiiI1iI + ii - OoOo0o + I11i1ii1
def iII1iiiiIII ( ) :
 OOoOO0oo00Oo = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 I111i1II = requests . get ( IIo0o0O0O00oOOo ) . content
 iI111i = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( I111i1II )
 O0ooooo0OOOO0 = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( iI111i ) )
 for IIIi1I1IIii1II , O000OOO in O0ooooo0OOOO0 :
  if not O000OOO == 'Home' :
   pass
   IiiIi1III = 'http://www.replaymatches.com/' + IIIi1I1IIii1II
   if O000OOO in OOoOO0oo00Oo :
    o00oOOooOOo0o ( '[COLORred]' + O000OOO + '[/COLOR]' , IiiIi1III , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
   else :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IiiIi1III , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
    if 84 - 84: OoOo0o . iiiiiiii1 % o0o00Oo0O . iii1i1iiiiIi + OOOo00oo0oO
def Ii11i1I11i ( url ) :
 if 13 - 13: I11i1ii1 / Ii % IIiIiII11i % i1IiiiI1iI . oOoO0o00OO0
 if 8 - 8: iii1i1iiiiIi + I1ii11iIi11i - IIiIiII11i
 if 11 - 11: ooOoO0O00 % Ii - ooOoO0O00 * iii1i1iiiiIi
 if 39 - 39: O0Oooo0O
 if 86 - 86: i1IiiiI1iI * oOo0O0Ooo + i1IiiiI1iI + IIiIiII11i
 if 8 - 8: O0Oooo0O - iiiiiiii1 / oOOoOooOo
 if 96 - 96: iii1i1iiiiIi
 if 29 - 29: oOoO0o00OO0 / ooOoO0O00 . oOo0O0Ooo - iii1i1iiiiIi - iii1i1iiiiIi - i1iIi
 if 20 - 20: ooOoO0O00 % oOo . oOo0O0Ooo / I11i1ii1 * Ii * OoOo0o
 if 85 - 85: ooo0O . iii1i1iiiiIi / oOOoOooOo . o0o00Oo0O % O0Oooo0O
 oOOo0 = i11111IIIII ( url )
 OO0ooo0oOO = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( oOOo0 )
 oo000ii = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( oOOo0 )
 for url , O000OOO , I1i in OO0ooo0oOO :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 900302 , I1i , I1IIIii + 'tommysreplays.png' , '' )
 for OoOIiiiii111i1ii in oo000ii :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , OoOIiiiii111i1ii , 900301 , I1IIIii + 'NEXT.png' , '' , '' )
def i1i1iII1 ( url ) :
 I111i1II = requests . get ( url ) . content
 iI111i = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( I111i1II )
 for IIIi1I1IIii1II , I1i in iI111i :
  if 'Highlight' in I1i :
   O000OOO = 'HighLights'
  elif '1st' in I1i :
   O000OOO = '1st Half'
  elif '2nd' in I1i :
   O000OOO = '2nd Half'
  else :
   O000OOO = 'Full Match'
  iii11i1IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIIi1I1IIii1II , 1001111 , I1i , I1IIIii + 'tommysreplays.png' , '' , '' )
def Iio00 ( ) :
 I111i1II = requests . get ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 iI111i = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( I111i1II )
 for iiI1Ii1 , ii1i in iI111i :
  iiIi1iI1iIii ( '[COLORred]' + iiI1Ii1 + '[/COLOR]' , '' , '' , I1IIIii + 'tommysreplays.png' , I1IIIii + 'tommysreplays.png' , '' , '' )
  oOOoo = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( ii1i ) )
  for iII1111III1I , ii11i in oOOoo :
   iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']' + iII1111III1I + '[/COLOR]' , '' , '' , ii11i , I1IIIii + 'tommysreplays.png' , '' , '' )
   if 100 - 100: oOOoOooOo % iI11I1II1I1I * IIiIiII11i - iiiiiiii1
def oo00O00oO000o ( url ) :
 if 71 - 71: oOoO0o00OO0 - oOOoOooOo / iii1i1iiiiIi * iii1i1iiiiIi / ooOoO0O00 . ooOoO0O00
 if 53 - 53: O0Oooo0O
 if 21 - 21: i1IiiiI1iI
 if 92 - 92: Ii / O0Oooo0O - iiiiiiii1 % oOOoOooOo * O0Oooo0O + I1ii11iIi11i
 if 11 - 11: ii . O0Oooo0O
 if 80 - 80: ii - OoOo0o * i1iIi * oOoO0o00OO0 / oOo0O0Ooo / OoOo0o
 if 13 - 13: O0Oooo0O * oOOoOooOo + Ii * O0Oooo0O - oOOoOooOo
 if 23 - 23: iI11I1II1I1I * ooOoO0O00 % ii * I11i1ii1
 if 9 - 9: I11i1ii1 - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
 if 39 - 39: I11i1ii1 * I1ii11iIi11i + iI11I1II1I1I - I11i1ii1 + OoOo0o
 if 69 - 69: o0o00Oo0O
 if 85 - 85: oOOoOooOo / o0o00Oo0O
 if 18 - 18: ooo0O % o0o00Oo0O * oOoO0o00OO0
 if 62 - 62: O0Oooo0O . I11i1ii1 . ii
 if 11 - 11: OoOo0o / i1IiiiI1iI
 if 73 - 73: ooOoO0O00 / Ii
 if 58 - 58: I1ii11iIi11i . IIiIiII11i + OOOo00oo0oO - Ii / IIiIiII11i / o0o00Oo0O
 if 85 - 85: iii1i1iiiiIi + OoOo0o
 if 10 - 10: I11i1ii1 / oOo + iii1i1iiiiIi / ooOoO0O00
 if 27 - 27: i1iIi
 if 67 - 67: oOo0O0Ooo
 if 55 - 55: oOoO0o00OO0 - iiiiiiii1 * ooo0O + iii1i1iiiiIi * iii1i1iiiiIi * o0o00Oo0O
 if 91 - 91: O0Oooo0O - OoOo0o % iI11I1II1I1I - ii % oOOoOooOo
 if 98 - 98: oOo . oOo * OOOo00oo0oO * IIiIiII11i * O0Oooo0O
 if 92 - 92: I1ii11iIi11i
 if 40 - 40: iii1i1iiiiIi / I11i1ii1
 if 79 - 79: oOo - iI11I1II1I1I + i1iIi - O0Oooo0O
 if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + iii1i1iiiiIi
 if 61 - 61: IIiIiII11i
 if 15 - 15: Ii % oOo0O0Ooo * i1IiiiI1iI / O0Oooo0O
 if 90 - 90: iiiiiiii1
 if 31 - 31: OoOo0o + o0o00Oo0O
 if 87 - 87: oOOoOooOo
 if 45 - 45: oOo / ii - iiiiiiii1 / i1iIi % I11i1ii1
 if 83 - 83: oOo0O0Ooo . iI11I1II1I1I - I11i1ii1 * Ii
 if 20 - 20: ooOoO0O00 * O0Oooo0O + IIiIiII11i % ooo0O % OOOo00oo0oO
 if 13 - 13: I1ii11iIi11i
 if 60 - 60: oOoO0o00OO0 * oOo0O0Ooo
 if 17 - 17: OoOo0o % I1ii11iIi11i / oOoO0o00OO0 . I11i1ii1 * OoOo0o - IIiIiII11i
 i1i1IIii1i1 = liveresolver . resolve ( url )
 Ii1II1I11i1 = xbmcgui . ListItem ( path = i1i1IIii1i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1II1I11i1 )
def oOoO00 ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 iI1IIIii = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iI1IIIii )
def IIi1IIIi ( ) :
 I1i11ii11 = False
 if os . path . exists ( os . path . join ( ooOoOoo0O , 'xbmc.log' ) ) :
  I1i11ii11 = os . path . join ( ooOoOoo0O , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'kodi.log' ) ) :
  I1i11ii11 = os . path . join ( ooOoOoo0O , 'kodi.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'spmc.log' ) ) :
  I1i11ii11 = os . path . join ( ooOoOoo0O , 'spmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'tvmc.log' ) ) :
  I1i11ii11 = os . path . join ( ooOoOoo0O , 'tvmc.log' )
 return I1i11ii11
 if 81 - 81: OoOo0o - i1IiiiI1iI % oOOoOooOo - oOo / I1ii11iIi11i
def Ii1iI111 ( url ) :
 if url == 'http://' : return False
 try :
  i1i = urllib2 . Request ( url )
  i1i . add_header ( 'User-Agent' , IiII )
  iiI111I1iIiI = urllib2 . urlopen ( i1i )
  iiI111I1iIiI . close ( )
 except Exception , o000O0O :
  return o000O0O
 return True
def O0oooo00o0Oo ( ) :
 if 36 - 36: i1iIi / IIiIiII11i / I11i1ii1 / I11i1ii1 + oOoO0o00OO0
 if 95 - 95: I11i1ii1
 if 51 - 51: IIiIiII11i + I11i1ii1 . ooOoO0O00 . oOoO0o00OO0 + iii1i1iiiiIi * oOo0O0Ooo
 if 72 - 72: OOOo00oo0oO + OOOo00oo0oO / IIiIiII11i . ii % i1iIi
 if 49 - 49: OOOo00oo0oO . oOo - I1ii11iIi11i * ii . I1ii11iIi11i
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def ii1Ii1IiIIi ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  oo0 = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   o0OO0 ( )
  if oOOOoo00 == 1 :
   oOo00Oo0o0Oo ( )
  if oOOOoo00 == 2 :
   I1 ( I1O0 )
  if oOOOoo00 == 3 :
   iIi1IiII ( IIo0o0O0O00oOOo )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 10060 , I1IIIii + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 49 , I1IIIii + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( O00OOOoOoo0O ) , 41 , I1IIIii + 'WipeGenie.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( O00OOOoOoo0O ) , 44 , I1IIIii + 'GenieBuilds.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 27 - 27: iiiiiiii1 . i1IiiiI1iI . iI11I1II1I1I . iI11I1II1I1I
def iIi1i ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if 4 - 4: O0Oooo0O / Ii / OoOo0o
  if 91 - 91: iI11I1II1I1I % ooo0O . iI11I1II1I1I % ooOoO0O00 / IIiIiII11i * iii1i1iiiiIi
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
  if 10 - 10: IIiIiII11i . iiiiiiii1
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( O00OOOoOoo0O ) , 10001 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
  if 32 - 32: i1iIi . I11i1ii1 . ii - oOo + OOOo00oo0oO
  if 88 - 88: iiiiiiii1
  if 19 - 19: IIiIiII11i * I11i1ii1 + i1iIi
  if 65 - 65: OoOo0o . O0Oooo0O . oOo . iiiiiiii1 - OoOo0o
  if 19 - 19: Ii + iiiiiiii1 % oOOoOooOo
  if 14 - 14: oOo . IIiIiII11i . i1IiiiI1iI / i1iIi % oOoO0o00OO0 - oOOoOooOo
  if 67 - 67: i1IiiiI1iI - OoOo0o . ooOoO0O00
 else :
  if 35 - 35: iiiiiiii1 + oOOoOooOo - OOOo00oo0oO . iiiiiiii1 . I11i1ii1
  if 87 - 87: iii1i1iiiiIi
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
  if 25 - 25: ooOoO0O00 . oOo - iii1i1iiiiIi / oOo % oOo * iI11I1II1I1I
  if 50 - 50: oOo . Ii - OOOo00oo0oO . OOOo00oo0oO
  if 31 - 31: OoOo0o / I1ii11iIi11i * ooOoO0O00 . iii1i1iiiiIi
  if 57 - 57: OoOo0o + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
  if 83 - 83: ooo0O / Ii % iI11I1II1I1I . i1IiiiI1iI % OOOo00oo0oO . ii
  if 94 - 94: i1iIi + iI11I1II1I1I % oOo
  if 93 - 93: i1iIi - OoOo0o + iI11I1II1I1I * ooo0O + O0Oooo0O . iiiiiiii1
  if 49 - 49: ii * i1IiiiI1iI - I1ii11iIi11i . OOOo00oo0oO
  if 89 - 89: oOOoOooOo + i1iIi * oOOoOooOo / oOOoOooOo
  if 46 - 46: oOo
  if 71 - 71: i1IiiiI1iI / i1IiiiI1iI * OOOo00oo0oO * OOOo00oo0oO / IIiIiII11i
  if 35 - 35: OoOo0o * ooo0O * oOo0O0Ooo % I1ii11iIi11i . iii1i1iiiiIi
  if 58 - 58: i1IiiiI1iI + IIiIiII11i * iiiiiiii1 * Ii - iI11I1II1I1I
  if 68 - 68: ii % IIiIiII11i
  if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % i1IiiiI1iI * i1IiiiI1iI * oOoO0o00OO0
  if 24 - 24: IIiIiII11i % O0Oooo0O - oOOoOooOo + oOo0O0Ooo * oOoO0o00OO0
  if 2 - 2: i1iIi - I11i1ii1
  if 83 - 83: OOOo00oo0oO % ooo0O % i1iIi - IIiIiII11i * OoOo0o / ii
  if 18 - 18: oOo + iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
  if 71 - 71: ii
  if 33 - 33: O0Oooo0O
  if 62 - 62: oOoO0o00OO0 + i1iIi + ooOoO0O00 / ii
  if 7 - 7: ooo0O + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
  if 22 - 22: oOOoOooOo - oOOoOooOo % OoOo0o . O0Oooo0O + OOOo00oo0oO
  if 63 - 63: oOo0O0Ooo % O0Oooo0O * ooo0O + O0Oooo0O / I1ii11iIi11i % iiiiiiii1
  if 45 - 45: I11i1ii1
  if 20 - 20: ii * ooo0O * o0o00Oo0O . OoOo0o
  if 78 - 78: iI11I1II1I1I + i1IiiiI1iI - i1iIi * O0Oooo0O - ii % iii1i1iiiiIi
  if 34 - 34: o0o00Oo0O
  if 80 - 80: ooOoO0O00 - I1ii11iIi11i / oOo - Ii
  if 68 - 68: OOOo00oo0oO - oOoO0o00OO0 % o0o00Oo0O % O0Oooo0O
  if 11 - 11: o0o00Oo0O / oOo % OoOo0o + ooo0O + iI11I1II1I1I
  if 40 - 40: oOOoOooOo - OoOo0o . i1iIi * I1ii11iIi11i % O0Oooo0O
  if 56 - 56: Ii . ooo0O - oOo0O0Ooo * i1IiiiI1iI
 iIiIi11 ( 'movies' , 'MAIN' )
def oOOoo0 ( ) :
 oo0 = [ '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  i1111IIiii1 ( )
 if oOOOoo00 == 1 :
  iIi ( )
 if oOOOoo00 == 2 :
  OOOoO ( )
 if oOOOoo00 == 3 :
  oOooo ( )
 if oOOOoo00 == 4 :
  oo00OOoOoO00 ( )
 if oOOOoo00 == 5 :
  I1iii ( )
  if 51 - 51: oOoO0o00OO0
  if 41 - 41: oOoO0o00OO0 * oOOoOooOo - i1iIi + I1ii11iIi11i
def IiIIIII11I ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  oo0 = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   Ii1I11I ( )
  if oOOOoo00 == 1 :
   iiIii1I ( )
  if oOOOoo00 == 2 :
   i1I11iIiII ( )
  if oOOOoo00 == 3 :
   OO0OO0OO ( o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if oOOOoo00 == 4 :
   OoooO0o ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9001 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 10200 , I1IIIii + 'rated.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , I1IIIii + 'Desi.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , I1IIIii + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , I1IIIii + 'ClassicMovies.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
def IIIii1iiIi ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 63 - 63: oOoO0o00OO0
 if 6 - 6: oOOoOooOo / oOoO0o00OO0
 if 57 - 57: i1IiiiI1iI
 if 67 - 67: oOo . oOOoOooOo
 if 87 - 87: OOOo00oo0oO % i1iIi
def oo0OOOoOo ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  oo0 = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , '[COLOR' + iiI1IiI + ']THE SOURCE[/COLOR]' , '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   IIiiIIi1 ( )
  if oOOOoo00 == 1 :
   ooO000O ( 'http://www.tvmaze.com/shows' )
  if oOOOoo00 == 2 :
   oOIII111iiIi1 ( )
  if oOOOoo00 == 3 :
   Ii11Ii ( )
  if oOOOoo00 == 4 :
   IiIiIi1IIi ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9002 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , 'http://www.tvmaze.com/shows' , 9110001 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , str ( O00OOOoOoo0O ) , 10095 , I1IIIii + 'RD.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( O00OOOoOoo0O ) , 8064 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
def O0OOOo ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   i11I1I1iiI = '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]'
   if 34 - 34: i1IiiiI1iI % oOOoOooOo . o0o00Oo0O . iI11I1II1I1I
   if 93 - 93: ooOoO0O00 . Ii . I1ii11iIi11i
   if 99 - 99: i1IiiiI1iI - O0Oooo0O - OOOo00oo0oO % oOo
   if 21 - 21: IIiIiII11i % oOoO0o00OO0 . ooOoO0O00 - ii
  oo0 = [ i11I1I1iiI , '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , '[COLOR' + iiI1IiI + ']PIRATE MOVIES[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   iiOOOO0o ( )
  if oOOOoo00 == 1 :
   i1I1iIi1IiI ( )
  if oOOOoo00 == 2 :
   i1111O0O000OOOo ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if oOOOoo00 == 3 :
   i11ii1Ii1 ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , i1i1II1i11 , O000OOO )
 else :
  if 91 - 91: i1IiiiI1iI / ooOoO0O00 * ooOoO0O00
  if 25 - 25: iI11I1II1I1I . OoOo0o * OOOo00oo0oO - i1iIi
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 55 - 55: iii1i1iiiiIi
  if 63 - 63: I11i1ii1 * iii1i1iiiiIi * oOOoOooOo
  if 92 - 92: oOoO0o00OO0 / o0o00Oo0O
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , I1IIIii + 'bamftv.png' , Oo00OOOOO , '' )
  if 80 - 80: ooo0O - OoOo0o + ii
  if 98 - 98: OoOo0o + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - ooo0O
  if 24 - 24: I1ii11iIi11i - ooOoO0O00 + i1IiiiI1iI
  if 38 - 38: ii / oOoO0o00OO0 . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
  if 96 - 96: iiiiiiii1
  if 18 - 18: iiiiiiii1 * i1IiiiI1iI - i1iIi
  if 31 - 31: I1ii11iIi11i - o0o00Oo0O % iii1i1iiiiIi % OOOo00oo0oO
 iIiIi11 ( 'movies' , 'MAIN' )
 if 45 - 45: oOoO0o00OO0 + IIiIiII11i * Ii
def IiIIi1I1I11Ii ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
def i1111O0O000OOOo ( url ) :
 I111i1II = i11111IIIII ( url )
 O0ooooo0OOOO0 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I111i1II )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( O0ooooo0OOOO0 ) )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O0ooooo0OOOO0 ) )
 OoOOo0OOoO = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O0ooooo0OOOO0 ) )
 for O000OOO , I1i , url in iI111i :
  if '247ch' in url :
   o0OO ( O000OOO , url , 10190 , I1i )
  elif '.m3u' in url :
   o0OO ( O000OOO , url , 1019 , I1i )
  elif '.xml' in url :
   o0OO ( O000OOO , url , 1018 , I1i )
  else :
   Oo ( O000OOO , url , 222 , I1i )
 for O000OOO , url , I1i in IIi11i1i1iI1 :
  if '.xml' in url :
   o0OO ( O000OOO , url , 1018 , I1i )
  elif '.m3u' in url :
   o0OO ( O000OOO , url , 1019 , I1i )
  else :
   Oo ( O000OOO , url , 222 , I1i )
 for O000OOO , url , I1i in OoOOo0OOoO :
  Oo ( O000OOO , url , 8043 , I1i )
def iiIiI ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'BAMFTV.png' )
def ii1 ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url , I1i in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1i )
  if 55 - 55: I1ii11iIi11i
def i1I1iIi1IiI ( ) :
 if 77 - 77: IIiIiII11i
 iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']All Movies[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']Movies By Genre[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']Movies By A - Z[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 9110015 , I1IIIii + 'Search.png' , Oo00OOOOO , '' , '' )
 if 16 - 16: oOo0O0Ooo * IIiIiII11i / iI11I1II1I1I - iiiiiiii1
 if 3 - 3: oOo0O0Ooo * oOOoOooOo + IIiIiII11i - oOo
 if 97 - 97: oOoO0o00OO0 / OOOo00oo0oO - ooo0O - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / iiiiiiii1 . oOo0O0Ooo * iii1i1iiiiIi
def IIiIiiiIIIIi1 ( url ) :
 I111i1II = requests . get ( url ) . text
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( I111i1II )
 for iIi11 , O00O0 , iIiIiiiIi , ii11i , i1iiIIi11I , o0o0oOo000o0 , iI1iIii11Ii in iI111i :
  if iI1iIii11Ii == ' ' :
   iI1iIii11Ii = Oo00OOOOO
  if ii11i == ' ' :
   ii11i = O0O
  i1iiIIi11I = i1iiIIi11I . replace ( '\\n' , ' ' )
  if O00O0 == 'Movie Search' :
   iii11i1IIII ( iIi11 , o0o0oOo000o0 , 9110014 , ii11i , iI1iIii11Ii , i1iiIIi11I , '' )
  elif O00O0 == 'Menu' :
   iiIi1iI1iIii ( iIi11 , iIiIiiiIi , 9110013 , ii11i , iI1iIii11Ii , i1iiIIi11I , '' )
   if 25 - 25: i1IiiiI1iI + iii1i1iiiiIi . ooo0O % iii1i1iiiiIi * OoOo0o
def ii1IiIi11 ( name , url ) :
 from imports import Scrape_Nan
 name = str ( name )
 o0o0oOo000o0 = str ( url )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( name , o0o0oOo000o0 , '' )
 if 22 - 22: OOOo00oo0oO
def ii1ii ( ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 oOoooO00O = iI111I11I1I1 . input ( 'Search your moive' , type = xbmcgui . INPUT_ALPHANUM )
 OOoOO0oo00Oo = [ 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ]
 for IIo0o0O0O00oOOo in OOoOO0oo00Oo :
  I111i1II = requests . get ( o0oOoO00o ( IIo0o0O0O00oOOo ) ) . content
  iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( I111i1II )
  for iIi11 , O00O0 , iIiIiiiIi , ii11i , i1iiIIi11I , o0o0oOo000o0 , iI1iIii11Ii in iI111i :
   if iI1iIii11Ii == ' ' :
    iI1iIii11Ii = Oo00OOOOO
   if ii11i == ' ' :
    ii11i = O0O
   i1iiIIi11I = i1iiIIi11I . replace ( '\\n' , ' ' )
   if O00O0 == 'Movie Search' :
    if oOoooO00O . lower ( ) in iIi11 . lower ( ) :
     iii11i1IIII ( iIi11 , o0o0oOo000o0 , 9110014 , ii11i , iI1iIii11Ii , i1iiIIi11I , '' )
def I1ii1111Ii ( url ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oOOo0 )
 for O000OOO , url , O00O0 , iIiII , iI1iIii11Ii , IIIIiii1IIii in iI111i :
  if iIiII == '123' :
   iIiII = I1IIIii + 'appstreams.png'
  if iI1iIii11Ii == '123' :
   iI1iIii11Ii = I1IIIii + 'appstreams.png'
  if 'php' in url :
   o00oOOooOOo0o ( O000OOO , url , 100010 , iIiII , iI1iIii11Ii , IIIIiii1IIii )
  elif 'playlist' in url :
   o00oOOooOOo0o ( O000OOO , url , 100007 , iIiII , iI1iIii11Ii , IIIIiii1IIii )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( O000OOO , url , 100100 , iIiII , iI1iIii11Ii , IIIIiii1IIii )
  elif not 'http' in url :
   iii11i1IIII ( O000OOO , url , 100009 , iIiII , iI1iIii11Ii , IIIIiii1IIii , '' )
  else :
   iii11i1IIII ( O000OOO , url , 100005 , iIiII , iI1iIii11Ii , IIIIiii1IIii , '' )
   if 19 - 19: I11i1ii1
def oOOOOOOOoO ( url ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , I1i , IIIIiii1IIii , iI1iIii11Ii , O000OOO in IIIii1I :
  if I1i == '123' :
   I1i = I1IIIii + 'appstreams.png'
  if iI1iIii11Ii == '123' :
   iI1iIii11Ii = Oo00OOOOO
  if 'php' in url :
   o00oOOooOOo0o ( O000OOO , url , 100004 , I1i , iI1iIii11Ii , IIIIiii1IIii )
  elif 'playlist' in url :
   o00oOOooOOo0o ( O000OOO , url , 100007 , I1i , iI1iIii11Ii , IIIIiii1IIii )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( O000OOO , url , 100100 , I1i , iI1iIii11Ii , IIIIiii1IIii )
  elif not 'http' in url :
   iii11i1IIII ( O000OOO , url , 100009 , I1i , iI1iIii11Ii , IIIIiii1IIii , '' )
  else :
   iii11i1IIII ( O000OOO , url , 100005 , I1i , iI1iIii11Ii , IIIIiii1IIii , '' )
   if 12 - 12: iiiiiiii1 . I11i1ii1 . iii1i1iiiiIi / o0o00Oo0O
def OO0oOOo0o ( url ) :
 if 50 - 50: iiiiiiii1 . oOoO0o00OO0 . oOo * i1IiiiI1iI + IIiIiII11i % Ii
 oOOo0 = o0OiiiI1i11Ii ( url )
 i1i1IiIiIi1Ii = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oOOo0 )
 for O0ooooo0OOOO0 in i1i1IiIiIi1Ii :
  iIiII = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for iIiII in iIiII :
   iIiII = iIiII
  O000OOO = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for O000OOO in O000OOO :
   if 'elete' in O000OOO :
    pass
   elif 'rivate Vid' in O000OOO :
    pass
   else :
    O000OOO = ( O000OOO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  oO0ooOO = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for oO0ooOO in oO0ooOO :
   oO0ooOO = oO0ooOO
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for url in url :
   url = url
  iii11i1IIII ( '[COLORred]' + str ( oO0ooOO ) + '[/COLOR] : ' + str ( O000OOO ) , str ( url ) , 100009 , str ( iIiII ) , Oo00OOOOO , '' , '' )
  iIiIi11 ( 'movies' , '' )
  if 16 - 16: I1ii11iIi11i + oOOoOooOo / I1ii11iIi11i / oOo % OOOo00oo0oO % oOoO0o00OO0
def Ii1II11II1iii ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search Dans Scrapes' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'http://www.tvmaze.com/search?q=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 oOOo0 = i11111IIIII ( ooO0000o00O )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  O0Ooo = 'http://www.tvmaze.com' + IIo0o0O0O00oOOo . replace ( '"' , '' )
  oO00oOOo0Oo = requests . get ( O0Ooo ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oO00oOOo0Oo )
  for IIIIiii1IIii in iI111i :
   if not '<div>' in IIIIiii1IIii :
    IIi = IIIIiii1IIii . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   I1i = 'http:' + I1i
   O000OOO = O000OOO . replace ( '&#039;' , '' )
   if O000OOO == '' :
    IIIIii = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( IIo0o0O0O00oOOo ) )
    for O000OOO in IIIIii :
     O000OOO = O000OOO . replace ( '-' , ' ' )
  iiIi1iI1iIii ( O000OOO , O0Ooo , 9110002 , I1i , Oo00OOOOO , IIi , '' )
  if 40 - 40: o0o00Oo0O
def ooO000O ( url ) :
 o0OO ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 9110004 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
 I111i1II = requests . get ( url ) . content
 iI111i = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( I111i1II )
 OoOIiiiii111i1ii = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( I111i1II )
 for url , I1i , O000OOO in iI111i :
  O0Ooo = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  if 58 - 58: I1ii11iIi11i
  oO00oOOo0Oo = requests . get ( O0Ooo ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oO00oOOo0Oo )
  for IIIIiii1IIii in iI111i :
   if not '<div>' in IIIIiii1IIii :
    IIi = IIIIiii1IIii . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   I1i = 'http:' + I1i
   O000OOO = O000OOO . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if O000OOO == '' :
    IIIIii = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for O000OOO in IIIIii :
     O000OOO = O000OOO . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  iiIi1iI1iIii ( O000OOO , O0Ooo , 9110002 , I1i , Oo00OOOOO , IIi , '' )
  if 9 - 9: iI11I1II1I1I % oOoO0o00OO0 . OoOo0o + ii
 for oo000ii in OoOIiiiii111i1ii :
  url = 'http://www.tvmaze.com' + oo000ii
  iiIi1iI1iIii ( 'NEXT' , url , 9110001 , I1i , Oo00OOOOO , '' , '' )
def Oo0o ( url ) :
 I111i1II = requests . get ( url ) . content
 iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( I111i1II )
 for IIIIiii1IIii in iI111i :
  IIi = IIIIiii1IIii . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
 return IIi
def oOOoOoo0O0 ( url , name , iconimage ) :
 iIi11 = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 I1i = iconimage
 I111i1II = requests . get ( url + '/episodes' ) . content
 oO00oOOo0Oo = requests . get ( url ) . content
 O0ooooo0OOOO0 = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( I111i1II )
 iI111i = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( oO00oOOo0Oo )
 for i1i1ii1111i1i in iI111i :
  i1i1ii1111i1i = i1i1ii1111i1i . replace ( ' ' , '' )
 for iIiI , ii1i in O0ooooo0OOOO0 :
  if not 'special' in iIiI . lower ( ) :
   iIiI = iIiI . replace ( 'S' , '' ) . replace ( 's' , '' )
  ii1iIIiii1 = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( ii1i ) )
  for ooOo0O0o0 , o0oo0O , I1iiIII in ii1iIIiii1 :
   if not 'special' in ooOo0O0o0 . lower ( ) :
    iiIi1iI1iIii ( iIi11 + ' - SEASON -' + iIiI + '- EPISODE-' + ooOo0O0o0 + '-' + i1i1ii1111i1i , '' , 9110003 , I1i , Oo00OOOOO , '' , iIi11 )
    if 16 - 16: OOOo00oo0oO + oOOoOooOo / ooo0O
    if 82 - 82: I11i1ii1 * Ii % IIiIiII11i - ii
    if 90 - 90: I1ii11iIi11i . OOOo00oo0oO * ooOoO0O00 - ooOoO0O00
def IiIiiI11i1Ii ( name , extra ) :
 if 100 - 100: O0Oooo0O . oOo0O0Ooo * O0Oooo0O - oOo0O0Ooo . i1IiiiI1iI * i1iIi
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 from imports import Scrape_Nan
 oO000o = name + '<>'
 o0Oo = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( oO000o ) )
 for iIi11 , o0O0 , I1I1Iiii1 , i1i1ii1111i1i in o0Oo :
  iIi11 = iIi11
  o0O0 = o0O0
  I1I1Iiii1 = I1I1Iiii1
  i111i1 = ''
  Scrape_Nan . scrape_episode ( iIi11 , i1i1ii1111i1i , '' , o0O0 , I1I1Iiii1 , '' )
if 99 - 99: oOo0O0Ooo + ooOoO0O00 + Ii + I1ii11iIi11i % OOOo00oo0oO / i1IiiiI1iI
if 60 - 60: i1iIi * iii1i1iiiiIi - Ii % oOOoOooOo
if 52 - 52: oOoO0o00OO0 % OOOo00oo0oO - Ii
if 30 - 30: iiiiiiii1 / oOo + OOOo00oo0oO
if 6 - 6: iiiiiiii1 . i1IiiiI1iI + i1iIi . O0Oooo0O
if 70 - 70: oOo
if 46 - 46: i1IiiiI1iI - ooOoO0O00
if 46 - 46: O0Oooo0O % i1iIi
if 72 - 72: iI11I1II1I1I
if 45 - 45: I1ii11iIi11i - ooo0O % O0Oooo0O
if 38 - 38: O0Oooo0O % OoOo0o - ii
def oOo0OOoooO ( ) :
 iiIi1iI1iIii ( 'Featured 24/7' , '' , 9070000 , I1IIIii + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 iiIi1iI1iIii ( '24/7 Tv Thows' , '' , 9080000 , I1IIIii + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 iiIi1iI1iIii ( '24/7 Movies' , '' , 9090000 , I1IIIii + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 iiIi1iI1iIii ( '24/7 Cable' , '' , 9100000 , I1IIIii + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 iiIi1iI1iIii ( '24/7 Random Stream' , '' , 9110000 , I1IIIii + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 26 - 26: ooo0O * I11i1ii1 . ooOoO0O00
def ooOoOO ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 Ooo00o0oOo0O0O = 'index.php#shows'
 I111i1II = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + Ooo00o0oOo0O0O ) . content )
 oO0ooOOiii1iII1 = I111i1II . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for oO0O000oOo in oO0ooOOiii1iII1 :
  OoOOOO = oO0O000oOo . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in OoOOOO :
   I1iiIi111I = IIIi1I1IIii1II . text
  Iiii1iIii = oO0O000oOo . findAll ( 'a' )
  for IIIi1I1IIii1II in Iiii1iIii :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    oOoooO000O = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   III1I11i1iIi = { 'User-Agent' : random_agent ( ) }
   OO0oo0O0OOO0 = requests . get ( oOoooO000O , headers = III1I11i1iIi ) . content
   OoOOo = packets ( OO0oo0O0OOO0 )
   if 46 - 46: oOo0O0Ooo / i1iIi . O0Oooo0O % Ii + ooo0O + ii
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OoOOo )
   for O0o0000o in iI111i :
    O0o0000o = O0o0000o . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    oOo00OoOoO = 'https:' + O0o0000o + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    iii11i1IIII ( O000OOO , oOo00OoOoO , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 66 - 66: oOo0O0Ooo - I11i1ii1
    if 33 - 33: oOo0O0Ooo / oOo
def iiIIi ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 Ooo00o0oOo0O0O = 'index.php#movies'
 I111i1II = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + Ooo00o0oOo0O0O ) . content )
 oO0ooOOiii1iII1 = I111i1II . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for oO0O000oOo in oO0ooOOiii1iII1 :
  OoOOOO = oO0O000oOo . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in OoOOOO :
   I1iiIi111I = IIIi1I1IIii1II . text
  Iiii1iIii = oO0O000oOo . findAll ( 'a' )
  for IIIi1I1IIii1II in Iiii1iIii :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    oOoooO000O = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   III1I11i1iIi = { 'User-Agent' : random_agent ( ) }
   OO0oo0O0OOO0 = requests . get ( oOoooO000O , headers = III1I11i1iIi ) . content
   OoOOo = packets ( OO0oo0O0OOO0 )
   if 36 - 36: i1IiiiI1iI . IIiIiII11i
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OoOOo )
   for O0o0000o in iI111i :
    O0o0000o = O0o0000o . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    oOo00OoOoO = 'https:' + O0o0000o + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    iii11i1IIII ( O000OOO , oOo00OoOoO , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 25 - 25: OOOo00oo0oO
    if 34 - 34: iii1i1iiiiIi . iI11I1II1I1I % o0o00Oo0O
def iI11Ii111 ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 Ooo00o0oOo0O0O = 'index.php#cable'
 I111i1II = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + Ooo00o0oOo0O0O ) . content )
 oO0ooOOiii1iII1 = I111i1II . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for oO0O000oOo in oO0ooOOiii1iII1 :
  OoOOOO = oO0O000oOo . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in OoOOOO :
   I1iiIi111I = IIIi1I1IIii1II . text
  Iiii1iIii = oO0O000oOo . findAll ( 'a' )
  for IIIi1I1IIii1II in Iiii1iIii :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    oOoooO000O = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   III1I11i1iIi = { 'User-Agent' : random_agent ( ) }
   OO0oo0O0OOO0 = requests . get ( oOoooO000O , headers = III1I11i1iIi ) . content
   OoOOo = packets ( OO0oo0O0OOO0 )
   if 54 - 54: iii1i1iiiiIi % iiiiiiii1 . iii1i1iiiiIi * OoOo0o + iii1i1iiiiIi % ooOoO0O00
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OoOOo )
   for O0o0000o in iI111i :
    O0o0000o = O0o0000o . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    oOo00OoOoO = 'https:' + O0o0000o + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    iii11i1IIII ( O000OOO , oOo00OoOoO , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 23 - 23: O0Oooo0O - OoOo0o + i1iIi - iii1i1iiiiIi * iii1i1iiiiIi . I1ii11iIi11i
def iIii11iI1II ( ) :
 oO00oOOo0Oo = 'http://arconaitv.me/stream.php?id=random'
 III1I11i1iIi = { 'User-Agent' : random_agent ( ) }
 OO0oo0O0OOO0 = requests . get ( oO00oOOo0Oo , headers = III1I11i1iIi ) . content
 OoOOo = packets ( OO0oo0O0OOO0 )
 if 42 - 42: oOOoOooOo - oOo0O0Ooo + oOoO0o00OO0 % i1iIi
 iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OoOOo )
 for O0o0000o in iI111i :
  O0o0000o = O0o0000o . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  oOo00OoOoO = 'https:' + O0o0000o + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  iii11i1IIII ( 'Random Pick' , oOo00OoOoO , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 44 - 44: ooOoO0O00 - o0o00Oo0O - oOoO0o00OO0 * oOoO0o00OO0 + iii1i1iiiiIi
def O0oo ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 Ooo00o0oOo0O0O = 'index.php#shows'
 if 82 - 82: iii1i1iiiiIi + o0o00Oo0O - I11i1ii1 % OOOo00oo0oO * Ii
 I111i1II = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + Ooo00o0oOo0O0O ) . content )
 oO0ooOOiii1iII1 = I111i1II . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for oO0O000oOo in oO0ooOOiii1iII1 :
  OoOOOO = oO0O000oOo . findAll ( 'a' )
  for IIIi1I1IIii1II in OoOOOO :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    oOoooO000O = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   iIIi1iI1 = IIIi1I1IIii1II . findAll ( 'img' )
   for I1Iii1I in iIIi1iI1 :
    I1i = IIo0o0O0O00oOOo + I1Iii1I [ 'src' ]
    III1I11i1iIi = { 'User-Agent' : random_agent ( ) }
    OO0oo0O0OOO0 = requests . get ( oOoooO000O , headers = III1I11i1iIi ) . content
    OoOOo = packets ( OO0oo0O0OOO0 )
    if 13 - 13: ooo0O + o0o00Oo0O
    iI111i = re . compile ( "'https:(.+?)'" ) . findall ( OoOOo )
    for O0o0000o in iI111i :
     O0o0000o = O0o0000o . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     oOo00OoOoO = 'https:' + O0o0000o + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     iii11i1IIII ( O000OOO , oOo00OoOoO , 9060000 , I1i , I1i , '' , '' )
     if 71 - 71: I11i1ii1 + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
def OoO00o0 ( name , url ) :
 import urlresolver
 try :
  ooo0oOOO0 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( ooo0oOOO0 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 61 - 61: ooo0O / iii1i1iiiiIi - I1ii11iIi11i
 if 19 - 19: iiiiiiii1 - ooo0O / ooo0O + I1ii11iIi11i
def OoO0o0000O ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , I1i , IIIIiii1IIii , iI1iIii11Ii , O000OOO in IIIii1I :
  if '.php' in url :
   o00oOOooOOo0o ( O000OOO , url , 100210 , I1i , iI1iIii11Ii , IIIIiii1IIii )
  else :
   O0O0ooOOO ( O000OOO , url , 222 , I1i , iI1iIii11Ii , IIIIiii1IIii )
   if 8 - 8: iii1i1iiiiIi . oOOoOooOo % OOOo00oo0oO . oOo0O0Ooo % oOo0O0Ooo . i1iIi
   if 47 - 47: i1IiiiI1iI + oOOoOooOo + IIiIiII11i % Ii
   if 93 - 93: oOoO0o00OO0 % iii1i1iiiiIi . o0o00Oo0O / iiiiiiii1 * OOOo00oo0oO
def i1iii1ii ( iconimage , url , extra ) :
 iIiII = ' '
 II1 = ' '
 iI1iIii11Ii = ' '
 o0O0 = ' '
 I11Iii1 = o0OiiiI1i11Ii ( url )
 iIiII = re . compile ( '<img src="(.+?)">' ) . findall ( I11Iii1 )
 for iIiII in iIiII :
  iIiII = iIiII
 i1iIIi1II1iiI = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( I11Iii1 )
 for iI1iIii11Ii in i1iIIi1II1iiI :
  iI1iIii11Ii = iI1iIii11Ii
 iI111i = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( I11Iii1 )
 for url , o0O0 in iI111i :
  o0O0 = 'S' + ( o0O0 ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o00OO00OoO + url
  iiIi1iI1iIii ( ( o0O0 ) . replace ( '  ' , '' ) , url , 100101 , iIiII , iI1iIii11Ii , II1 , '' )
  iIiIi11 ( 'Movies' , 'info' )
  if 31 - 31: ooo0O % i1IiiiI1iI + iI11I1II1I1I + Ii * O0Oooo0O
def I1i1I1I11IiiI ( url , name , fanart , extra , iconimage ) :
 I1IiI1iI11 = extra
 o0O0 = name
 I11Iii1 = o0OiiiI1i11Ii ( url )
 iIiII = iconimage
 iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( I11Iii1 )
 for url , name , iIiii in iI111i :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o00OO00OoO + url
  iIiii = iIiii
  O0O0o0oO0O00 = name + ' - [COLORred]' + iIiii + '[/COLOR]'
  iiIi1iI1iIii ( O0O0o0oO0O00 , url , 100102 , iIiII , fanart , 'Aired : ' + iIiii , O0O0o0oO0O00 )
  if 70 - 70: O0Oooo0O + OOOo00oo0oO
def o00ooo0 ( name , URL , iconimage , fanart ) :
 oOOo0 = o0OiiiI1i11Ii ( URL )
 iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , name in iI111i :
  for Ii1II1I11i1 in OOOO0OOoO0O0 :
   if Ii1II1I11i1 in IIo0o0O0O00oOOo :
    URL = 'http://www.watchseriesgo.to/link/' + IIo0o0O0O00oOOo
    iii11i1IIII ( name , URL , 100106 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( iI111i ) <= 0 :
  iiIi1iI1iIii ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 39 - 39: oOOoOooOo . IIiIiII11i
  if 45 - 45: OOOo00oo0oO * iii1i1iiiiIi / iI11I1II1I1I
def o00ooOoO0 ( url , name ) :
 IIi11II1II111 = name
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oOOo0 )
 OoOOo0OOoO = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oOOo0 )
 for url in iI111i :
  o0OO0O0OO0oO0 ( url , IIi11II1II111 )
 for url in IIi11i1i1iI1 :
  o0OO0O0OO0oO0 ( url , IIi11II1II111 )
 for url in OoOOo0OOoO :
  o0OO0O0OO0oO0 ( url , IIi11II1II111 )
  if 9 - 9: OOOo00oo0oO % Ii / I1ii11iIi11i
def o0OO0O0OO0oO0 ( url , season_name ) :
 if 'daclips.in' in url :
  IIIiI1ii1IIi ( url , season_name )
 elif 'filehoot.com' in url :
  o0O0oo0o ( url , season_name )
 elif 'allmyvideos.net' in url :
  II11iI1iiI ( url , season_name )
 elif 'vidspot.net' in url :
  I1ii ( url , season_name )
 elif 'vodlocker' in url :
  oO0o ( url , season_name )
 elif 'vidto' in url :
  I1I1 ( url , season_name )
  if 99 - 99: oOOoOooOo / iI11I1II1I1I - i1iIi * oOoO0o00OO0 % oOo0O0Ooo
  if 13 - 13: oOo
def I1I1 ( url , season_name ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for IiiIi1III , O000OOO in iI111i :
  O0oo0O0 ( IiiIi1III , season_name )
  if 2 - 2: ii . OoOo0o . I11i1ii1
  if 42 - 42: OoOo0o % OOOo00oo0oO / oOo - OOOo00oo0oO * Ii
def II11iI1iiI ( url , season_name ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for IiiIi1III , O000OOO in iI111i :
  O0oo0O0 ( IiiIi1III , season_name )
  if 19 - 19: OOOo00oo0oO * oOo0O0Ooo % Ii
def I1ii ( url , season_name ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oOOo0 )
 for IiiIi1III , O000OOO in iI111i :
  O0oo0O0 ( IiiIi1III , season_name )
  if 24 - 24: ooo0O
def oO0o ( url , season_name ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for IiiIi1III in iI111i :
  O0oo0O0 ( IiiIi1III , season_name )
  if 10 - 10: ooo0O % i1iIi / OoOo0o
def IIIiI1ii1IIi ( url , season_name ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oOOo0 )
 for IiiIi1III in iI111i :
  O0oo0O0 ( IiiIi1III , season_name )
  if 28 - 28: OoOo0o % oOOoOooOo
def o0O0oo0o ( url , season_name ) :
 oOOo0 = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for IiiIi1III in iI111i :
  O0oo0O0 ( IiiIi1III , season_name )
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
def iiIi1iI1iIii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = True )
 return OoOo0oO0o
 if 10 - 10: i1IiiiI1iI / i1IiiiI1iI * Ii
 if 46 - 46: oOo * I1ii11iIi11i % OOOo00oo0oO + o0o00Oo0O * I11i1ii1
def iii11i1IIII ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
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
def o0OiiiI1i11Ii ( url ) :
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
def iIi ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  oo0 = [ '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' ]
  if 72 - 72: iiiiiiii1 * OoOo0o
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , oo0 )
  if 67 - 67: ooOoO0O00
  if 5 - 5: IIiIiII11i . ii
  if 57 - 57: oOo0O0Ooo
  if 35 - 35: ii - O0Oooo0O / oOo
  if oOOOoo00 == 0 :
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
def oOooo ( ) :
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
   oOOOoo00 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if oOOOoo00 == 0 :
    O00oOoOOO0ooo ( OOooOoooOoOo )
    O0O0Oo00 ( )
   elif oOOOoo00 == 1 :
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
 oOOoo = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 OoOOo0OOoO = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 ooO0O00Oo0o = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 OOO = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url , o0o0OO0o00o0O , iI1iIii11Ii , IIIIiii1IIii in oo0OoOOooO :
  if 'php' in url :
   o00oOOooOOo0o ( O000OOO , url , 90037 , o0o0OO0o00o0O , iI1iIii11Ii , IIIIiii1IIii )
  elif O000OOO == 'Search' :
   o00oOOooOOo0o ( 'Search' , url , 90038 , o0o0OO0o00o0O , iI1iIii11Ii , IIIIiii1IIii )
  else :
   O0O0ooOOO ( O000OOO , url , 222 , o0o0OO0o00o0O , iI1iIii11Ii , IIIIiii1IIii )
 for O000OOO , I1i , url , IIIIIIi1i in oOOoo :
  o00oOOooOOo0o ( O000OOO , url , 90037 , I1i , IIIIIIi1i , '' )
 for O000OOO , I1i , url , IIIIIIi1i in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 90037 , I1i , IIIIIIi1i , '' )
 for O000OOO , url , I1i , IIIIIIi1i in IIi11i1i1iI1 :
  O0O0ooOOO ( O000OOO , url , 222 , I1i , IIIIIIi1i , '' )
 for O000OOO , url , I1i , IIIIIIi1i in OoOOo0OOoO :
  O0O0ooOOO ( O000OOO , url , 222 , I1i , IIIIIIi1i , '' )
 for O000OOO , url , I1i , IIIIIIi1i in ooO0O00Oo0o :
  O0O0ooOOO ( O000OOO , url , 222 , I1i , IIIIIIi1i , '' )
 for O000OOO , url , I1i in OOO :
  O0O0ooOOO ( O000OOO , url , 222 , I1i , '' , '' )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
def iiiii11I1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , I1i , url , IIIIIIi1i in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 90037 , I1i , IIIIIIi1i , '' )
 for O000OOO , url , I1i , IIIIIIi1i in IIi11i1i1iI1 :
  O0O0ooOOO ( O000OOO , url , 222 , I1i , IIIIIIi1i , '' )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
  if 16 - 16: o0o00Oo0O . i1iIi % ooOoO0O00 % OoOo0o
def i1I1iIoOOoO ( ) :
 oOo0Oo0O0O = [ 'serialsearch' , 'moviesearch' ]
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 if ooO0000o00O == '' :
  pass
 else :
  for III1II1i in oOo0Oo0O0O :
   iI1i1IiIIIIi = oOOoo00O0O + III1II1i + '.php'
   I11Iii1 = i11111IIIII ( iI1i1IiIIIIi )
   if I11Iii1 != 'Opened' :
    IIIii1I = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( I11Iii1 )
    for O000OOO , IIo0o0O0O00oOOo , o0o0OO0o00o0O , iI1iIii11Ii , IIIIiii1IIii in IIIii1I :
     if ooO0000o00O in O000OOO . lower ( ) :
      OooOooO0O0o0 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( oO0 ) )
      for Ii1II1I11i1 in OooOooO0O0o0 :
       if Ii1II1I11i1 == IIo0o0O0O00oOOo :
        O000OOO = '[COLORred]* [/COLOR]' + ( O000OOO ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        OOO0o0 = open ( O0Oo000ooO00 , "a" )
        OOO0o0 . write ( 'item="' + O000OOO + '"\n' )
        OOO0o0 . close
      if 'php' in IIo0o0O0O00oOOo :
       o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 90037 , o0o0OO0o00o0O , iI1iIii11Ii , IIIIiii1IIii )
      else :
       O0O0ooOOO ( O000OOO , IIo0o0O0O00oOOo , 222 , o0o0OO0o00o0O , iI1iIii11Ii , IIIIiii1IIii )
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
 I111i1II = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 oO00oOOo0Oo = requests . get ( 'http://www.djing.com/' ) . content
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( oO00oOOo0Oo )
 oO0ooOOiii1iII1 = I111i1II . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for oO0O000oOo in oO0ooOOiii1iII1 :
  OoOOOO = oO0O000oOo . findAll ( 'a' )
  for IIIi1I1IIii1II in OoOOOO :
   if IIIi1I1IIii1II . has_attr ( 'href' ) :
    oOoooO000O = 'https://tvcatchup.com' + IIIi1I1IIii1II [ 'href' ]
   iIIi1iI1 = IIIi1I1IIii1II . findAll ( 'img' )
   for I1Iii1I in iIIi1iI1 :
    I1i = I1Iii1I [ 'src' ]
    O0000oO0o00 = I1Iii1I [ 'alt' ]
   iI111i = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( IIIi1I1IIii1II ) )
   for oo000o in iI111i :
    Oo ( ( '[COLORgold]' + O0000oO0o00 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + oo000o + '[/COLOR]' ) , oOoooO000O , 90024 , I1i )
    if 95 - 95: OOOo00oo0oO - oOOoOooOo * i1IiiiI1iI / oOo / IIiIiII11i + o0o00Oo0O
 for IIo0o0O0O00oOOo , I1i , O000OOO in IIi11i1i1iI1 :
  if 'Submit' in O000OOO :
   pass
  elif '&lt;' in O000OOO :
   pass
  else :
   O0O0ooOOO ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 90025 , 'http://www.djing.com' + I1i , Oo00OOOOO , '' )
   if 37 - 37: i1IiiiI1iI . O0Oooo0O + OoOo0o + i1IiiiI1iI . I11i1ii1 / i1iIi
 iIiIi11 ( 'movies' , 'MAIN' )
def i1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 if 100 - 100: oOo % oOo
 iI111i = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( html )
 for iI1I1 in iI111i :
  if not 'text' in iI1I1 :
   ii1O0ooooo000 = o0oOoO00o ( o0oOoO00o ( iI1I1 ) )
   OOIi1iI111II1I1 ( ii1O0ooooo000 )
def OooOoOO0OO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<iframe src='([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  I1iiIiiii1111 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 29 - 29: i1iIi - oOo0O0Ooo / oOo0O0Ooo * i1iIi * I11i1ii1 . OoOo0o
def ooo ( ) :
 oOOo0 = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 I11iI1I = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for Iii1iiIi1II1 , Oo000o , OO00oo in I11iI1I :
  Oo ( '[COLOR' + iiI1IiI + ']' + Iii1iiIi1II1 + Oo000o + OO00oo + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + IIo0o0O0O00oOOo , 10201 , I1IIIii + 'rated.png' )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'yr' in IIo0o0O0O00oOOo :
   o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + IIo0o0O0O00oOOo , 10201 , I1IIIii + 'rated.png' )
   if 84 - 84: oOOoOooOo + Ii - OoOo0o * oOOoOooOo
def iiIii1I ( ) :
 if 33 - 33: oOOoOooOo % ooOoO0O00 - OOOo00oo0oO . o0o00Oo0O / o0o00Oo0O
 if 96 - 96: ii + I11i1ii1 * o0o00Oo0O
 if 86 - 86: i1iIi
 if 29 - 29: iI11I1II1I1I - oOo + oOo0O0Ooo % iI11I1II1I1I % OoOo0o
 if 84 - 84: I11i1ii1 + oOoO0o00OO0 + i1iIi + iiiiiiii1
 if 62 - 62: Ii + iii1i1iiiiIi + ooOoO0O00
 oOOo0 = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'yr' in IIo0o0O0O00oOOo :
   iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + IIo0o0O0O00oOOo , 10201 , I1IIIii + 'rated.png' , '' , O000OOO , '' )
   if 69 - 69: iii1i1iiiiIi
def OO0Oo ( name , url , description ) :
 IIi = description
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
 for IIiiiiiIiIIi , url , name in iI111i :
  if 'id' in url :
   iiIiiIi1 = name
   iiIi1iI1iIii ( ( '[COLORred]RANK [COLORblue]' + IIiiiiiIiIIi + '[COLORred] - [COLORblue]' + name + '[/COLOR]' ) , name , 9110005 , I1IIIii + 'rated.png' , '' , IIi , iiIiiIi1 )
   if 30 - 30: OoOo0o + IIiIiII11i - I11i1ii1 * ii
   if 19 - 19: I11i1ii1 - ooo0O . iI11I1II1I1I . iii1i1iiiiIi / OoOo0o
def OOO0O00Oo ( description , url ) :
 if 13 - 13: iI11I1II1I1I
 o0o0oOo000o0 = ( str ( description ) )
 iIi11 = ( str ( url ) )
 xbmc . log ( 'title:' + iIi11 + '# year:' + o0o0oOo000o0 , xbmc . LOGNOTICE )
 from imports import Scrape_Nan
 Scrape_Nan . scrape_movie ( iIi11 , o0o0oOo000o0 , '' )
 if 2 - 2: ooOoO0O00 * OOOo00oo0oO - OOOo00oo0oO + ii % iii1i1iiiiIi / iii1i1iiiiIi
 if 3 - 3: ii
 if 71 - 71: I11i1ii1 + ooOoO0O00 - iiiiiiii1 - Ii . i1IiiiI1iI - oOOoOooOo
 if 85 - 85: oOoO0o00OO0 - iii1i1iiiiIi / oOoO0o00OO0 + OoOo0o - iiiiiiii1
 if 49 - 49: oOo - o0o00Oo0O / oOo * iii1i1iiiiIi + O0Oooo0O
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * OOOo00oo0oO
 if 85 - 85: IIiIiII11i . oOOoOooOo % OoOo0o % i1IiiiI1iI
def OOo00ooOoO0o ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 i1i1iiIIiiiII = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOoooO00O = ( url )
 ooO0000o00O = oOoooO00O . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 O0Ooo = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OO0ooO0 = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OoOooOO0oOOo0O = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1II = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIi1Ii1III = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOoooO00O
 Oooo00 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iii1II1iI1IIi = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 41 - 41: oOo0O0Ooo - O0Oooo0O % IIiIiII11i . O0Oooo0O - i1IiiiI1iI
 i1I111Ii = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 i11i1i = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 10 - 10: i1iIi - Ii . oOoO0o00OO0 % ooOoO0O00
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oOOo0 = i1Oo00 ( url )
 o0oO0 . update ( 0 , "" , "Checking Source 1/9 Links" )
 oo00O00oO = i1Oo00 ( O0Ooo )
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
  for url , O000OOO in i1i1 :
   o0oOoOo0 = i1Oo00 ( url )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , iIIIiIi in III1IiI1i1i :
    iIIIiIi = ( iIIIiIi . replace ( '.' , ' ' ) )
    if ooO0000o00O in iIIIiIi . lower ( ) :
     if '.mkv' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.mp4' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.avi' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.wav' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + o0OOOOOo0 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + o0OOOOOo0 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
      if 57 - 57: iI11I1II1I1I + iI11I1II1I1I
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in IIi11i1i1iI1 :
   if oOoooO00O in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 56 - 56: OOOo00oo0oO + oOOoOooOo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 32 - 32: IIiIiII11i + iii1i1iiiiIi % oOOoOooOo / iii1i1iiiiIi + oOoO0o00OO0
 if iIiIIIi != 'Failed' :
  OoOOo0OOoO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for IiI11I111 , O000OOO in OoOOo0OOoO :
   if oOoooO00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1I1 + IiI11I111 ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Source 3 Links" )
 if ooo00OOOooO != 'Failed' :
  ooO0O00Oo0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in ooO0O00Oo0o :
   if oOoooO00O in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 54 - 54: o0o00Oo0O - iiiiiiii1 . OoOo0o % iiiiiiii1 + iiiiiiii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if OooOOOoOoo0O0 != 'Failed' :
  i1iI1Iiii1I = [ ]
  OOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OooOOOoOoo0O0 )
  for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in OOO :
   if oOoooO00O in O000OOO . lower ( ) :
    if O000OOO in i1iI1Iiii1I :
     pass
    else :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
     i1iI1Iiii1I . append ( O000OOO )
     o0oO0 . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 36 , "" , "Getting Scooby Links" )
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if O0OOOOo0 != 'Failed' :
  o00Oo0oooooo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( O0OOOOo0 )
  for url , I1i , O000OOO in o00Oo0oooooo :
   if oOoooO00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , I1i )
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
  for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in IIIiI1iiiiiIi :
   if oOoooO00O in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
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
   for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in i1i1 :
    if oOoooO00O in O000OOO . lower ( ) :
     O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
     if 66 - 66: i1iIi - I1ii11iIi11i . ooOoO0O00
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
     if 75 - 75: i1iIi - i1IiiiI1iI % iii1i1iiiiIi
 Oooooooo00o00 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 80 - 80: i1iIi / OoOo0o
 if 21 - 21: I1ii11iIi11i - iI11I1II1I1I - O0Oooo0O
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = i1i1iiIIiiiII + III1II1i
  III1I1Iii11i = i1Oo00 ( iI1i1IiIIIIi )
  if III1I1Iii11i != 'Failed' :
   Oo0o00OO0000 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( III1I1Iii11i )
   for IiI11I111 , O000OOO in Oo0o00OO0000 :
    if oOoooO00O in O000OOO . lower ( ) :
     Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1i1iiIIiiiII + III1II1i + IiI11I111 ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 96 - 96: OOOo00oo0oO - OOOo00oo0oO
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: I1ii11iIi11i / ii - oOoO0o00OO0 . I11i1ii1 + iI11I1II1I1I . oOoO0o00OO0
def Ii11Ii ( ) :
 o0OO ( 'RUNNING' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , I1IIIii + 'running.png' )
 o0OO ( 'COUNTDOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , I1IIIii + 'countdown.png' )
 o0OO ( 'UNKNOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , I1IIIii + 'unknown.png' )
 o0OO ( 'CANCELLED' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , I1IIIii + 'cancelled.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 4 - 4: ii + oOOoOooOo . ooOoO0O00 / o0o00Oo0O - o0o00Oo0O
def oOooOOo00ooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , o0O0 , o0OO0oooo , iIiii , I11II1i1 in iI111i :
  o0OO ( ( '[COLORblue]' + O000OOO + '[/COLOR] [COLORred]Season[/COLOR]-' + o0O0 + ' [COLORred]Returns [/COLOR]- ' + I11II1i1 + ' ' + iIiii ) , O000OOO , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 46 - 46: IIiIiII11i % iiiiiiii1 - ooOoO0O00 / i1IiiiI1iI * iii1i1iiiiIi
def oO0o0oOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , o0O0 , o0OO0oooo in iI111i :
  o0OO ( ( '[COLORblue]' + O000OOO + '[/COLOR] [COLORred]Season[/COLOR]-' + o0O0 + ' [COLORred] Status Unknown[/COLOR] ' ) , O000OOO , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 92 - 92: ooOoO0O00 % oOOoOooOo + oOOoOooOo - iI11I1II1I1I . i1iIi
def iIIi1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , o0O0 , o0OO0oooo , iIiii in iI111i :
  o0OO ( ( '[COLORblue]' + O000OOO + ' [COLORred] Cancelled On[/COLOR] ' + iIiii ) , O000OOO , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 75 - 75: I11i1ii1 % Ii + iI11I1II1I1I
def oOoOo0o00o ( url ) :
 oOoooO00O = ( url )
 ooO0000o00O = oOoooO00O . lower ( )
 if 2 - 2: IIiIiII11i
 if 54 - 54: i1iIi . ii % I1ii11iIi11i
 o0OOOOOo0 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oOoooO00O ) . replace ( ' ' , '+' )
 O0Ooo = 'http://onlinemovies.tube/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
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
 oo00O00oO = i1Oo00 ( O0Ooo )
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
  for url , O000OOO in i1i1 :
   o0oOoOo0 = i1Oo00 ( url )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , iIIIiIi in III1IiI1i1i :
    if ooO0000o00O in iIIIiIi . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + o0OOOOOo0 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 74 - 74: o0o00Oo0O - IIiIiII11i + ooOoO0O00 . O0Oooo0O . oOoO0o00OO0
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if OOooO0Oo00 != 'Failed' :
  OoO0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooO0Oo00 )
  for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in OoO0O :
   if ooO0000o00O in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
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
  for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in Oo0OOo :
   if ooO0000o00O in O000OOO . lower ( ) :
    o0OO ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , i1i1II1i11 )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 30 , "" , "Getting RaizTv Links" )
    if 44 - 44: i1IiiiI1iI * ooo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  II11ii1I11 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for url , I1i , O000OOO , o0oO00o in IIi11i1i1iI1 :
   if ooO0000o00O in O000OOO . lower ( ) :
    if 'season' in o0oO00o :
     o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , I1i , I1i , '' )
    if 'episodes' in o0oO00o :
     o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , I1i , I1i , '' )
  for url in II11ii1I11 :
   o0OO ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 78 - 78: I1ii11iIi11i * O0Oooo0O - ii - oOo
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iiIIi1 != 'Failed' :
  oOOoo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iiIIi1 )
  for url , O000OOO , I1i in oOOoo :
   if ooO0000o00O in O000OOO . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( O000OOO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , I1i , '' , '' )
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
  OoOOo0OOoO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for O000OOO in OoOOo0OOoO :
   if ooO0000o00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Ii1I1 + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 82 - 82: I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / OoOo0o + I11i1ii1 % iI11I1II1I1I
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  ooO0O00Oo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for O000OOO in ooO0O00Oo0o :
   if ooO0000o00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OO0ooO0 + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 61 - 61: OoOo0o / I1ii11iIi11i % OoOo0o - oOo + oOOoOooOo / oOOoOooOo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if III1I1Iii11i != 'Failed' :
  Oo0o00OO0000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III1I1Iii11i )
  for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in Oo0o00OO0000 :
   if ooO0000o00O in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
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
   for O000OOO , IIIIiii1IIii , url , I1i , iI1iIii11Ii , O00O0 in IIIiI1iiiiiIi :
    if ooO0000o00O in O000OOO . lower ( ) :
     o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] - Source Pandoras[/COLOR]' , url , O00O0 , I1i , iI1iIii11Ii , IIIIiii1IIii )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
     if 68 - 68: ii * iI11I1II1I1I + ooOoO0O00 - ooOoO0O00
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
     if 76 - 76: oOo . ii % O0Oooo0O * i1iIi
     if 23 - 23: I11i1ii1 + iI11I1II1I1I
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: o0o00Oo0O % I11i1ii1 % i1iIi * OOOo00oo0oO
def o0OOO00ooo ( ) :
 oo0 = [ '[COLOR' + iiI1IiI + ']Adult Gallery[/COLOR]' , '[COLOR' + iiI1IiI + ']JizBox[/COLOR]' , '[COLOR' + iiI1IiI + ']Adult Channels[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  I1iI11IiiI11i ( )
 if oOOOoo00 == 1 :
  IIIiIIIi11I ( )
 if oOOOoo00 == 2 :
  II1O0o00 ( )
  if 48 - 48: i1IiiiI1iI + oOOoOooOo + iiiiiiii1 / i1IiiiI1iI / iiiiiiii1
  if 71 - 71: I11i1ii1
  if 18 - 18: oOOoOooOo + iiiiiiii1 - oOOoOooOo
def I1iI11IiiI11i ( ) :
 oo0 = [ '[COLOR' + iiI1IiI + ']YOLOselfies[/COLOR]' , '[COLOR' + iiI1IiI + ']HotNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']MyNudeBabes[/COLOR]' , '[COLOR' + iiI1IiI + ']TeenNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']ADULTmeme[/COLOR]' , '[COLOR' + iiI1IiI + ']GIRLSmeme[/COLOR]' , ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  o00OOo0o0O ( 'http://www.yoloselfie.com/' )
 if oOOOoo00 == 1 :
  I111Iii1 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if oOOOoo00 == 2 :
  i11i ( 'http://www.teennudegirls.com/' )
 if oOOOoo00 == 3 :
  i11i ( 'http://www.teennudegirls.com/' )
 if oOOOoo00 == 4 :
  O0o0O00o0o ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if oOOOoo00 == 5 :
  O0o0O00o0o ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 6 - 6: oOoO0o00OO0 - OOOo00oo0oO * Ii + iii1i1iiiiIi / oOOoOooOo % OoOo0o
def o00OOo0o0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 100111 , I1i )
 for url in IIi11i1i1iI1 :
  o0OO ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 100110 , I1i )
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
 for O000OOO , I1i in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + I1i , 100113 , 'http:' + I1i )
 for url in IIi11i1i1iI1 :
  o0OO ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http:' + url , 100112 , I1i )
def I111Iii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , I1i )
def ooOO0OOO00o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , I1i in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , I1i , 100113 , I1i )
def OoOoO0ooooO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , I1i )
def IIII1ii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , I1i in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , I1i , 100113 , I1i )
def i11i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , I1i )
def OOO0O0OOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , I1i in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , I1i , 100113 , I1i )
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
 o0OO ( 'SEASONS' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , I1IIIii + 'seasons.png' )
 o0OO ( 'EPISODES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , I1IIIii + 'episodes.png' )
 o0OO ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , I1IIIii + 'Search.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 56 - 56: oOOoOooOo * ooo0O + i1IiiiI1iI
def I11II11111i11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , O000OOO , OOO000Oo in iI111i :
  o0OO ( ( O000OOO + ' - ' + OOO000Oo ) . replace ( '&amp;' , '&' ) , url , 90053 , I1IIIii + 'seasons.png' )
  if 8 - 8: oOOoOooOo - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * i1iIi - iI11I1II1I1I
def i1Ii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  o0OO ( O000OOO , url , 90054 , I1IIIii + 'episodes.png' )
  if 31 - 31: iiiiiiii1 - iii1i1iiiiIi . iii1i1iiiiIi - OOOo00oo0oO + I1ii11iIi11i / Ii
def ooOoOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for I1i , O000OOO , url in iI111i :
  o0OO ( O000OOO , url , 90054 , I1i )
 for url in next :
  o0OO ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 13 - 13: OoOo0o . I1ii11iIi11i / IIiIiII11i
def iiI1iIII1ii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for I1i , OOO000Oo , url , O000OOO , i1iiIIiII1 in iI111i :
  o00oOOooOOo0o ( OOO000Oo + ' - ' + O000OOO + ' - ' + i1iiIIiII1 , url , 90044 , I1i , I1i , '' )
 for I1i , O000OOO , url in IIi11i1i1iI1 :
  o0OO ( O000OOO , url , 90044 , I1i , I1i , '' )
 for url in next :
  o0OO ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 72 - 72: I11i1ii1 % ooo0O
def OooooO ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'http://onlinemovies.tube/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 oOOo0 = i11111IIIII ( ooO0000o00O )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO , o0oO00o in iI111i :
  if 'season' in o0oO00o :
   o0OO ( O000OOO , IIo0o0O0O00oOOo , 90054 , I1i , I1i , '' )
  if 'episodes' in o0oO00o :
   o0OO ( O000OOO , IIo0o0O0O00oOOo , 90044 , I1i , I1i , '' )
 for IIo0o0O0O00oOOo in next :
  o0OO ( 'NEXT' , IIo0o0O0O00oOOo , 90053 , I1IIIii + 'Next.png' )
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
 o0OO ( 'ALL MOVIES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , I1IIIii + 'allmov.png' )
 o0OO ( 'GENRE' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , I1IIIii + 'Genre.png' )
 o0OO ( 'BY YEAR' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , I1IIIii + 'Years.png' )
 o0OO ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , I1IIIii + 'Search.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 99 - 99: Ii % ii
def o0000O00oO0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , O000OOO , OOO000Oo in iI111i :
  if 'genre' in url :
   o0OO ( ( O000OOO + ' - ' + OOO000Oo ) . replace ( '&amp;' , '&' ) , url , 90043 , I1IIIii + 'Genre.png' )
   if 3 - 3: iI11I1II1I1I % oOoO0o00OO0 . OoOo0o % i1IiiiI1iI
def I1i1I1Iiiii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if 'release' in url :
   o0OO ( O000OOO , url , 90043 , I1IIIii + 'Years.png' )
   if 88 - 88: i1IiiiI1iI + oOo0O0Ooo - i1IiiiI1iI / ii - Ii
def i11Ii1IiIIIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for I1i , O000OOO , OOOoo00o0o , url , IIIIiii1IIii in iI111i :
  o00oOOooOOo0o ( O000OOO + ' ' + OOOoo00o0o , url , 90044 , I1i , I1i , IIIIiii1IIii )
 for I1i , O000OOO , o0oO00o , url , O00o0OO0OO0oo , IIIIiii1IIii in IIi11i1i1iI1 :
  if 'movies' in o0oO00o :
   o00oOOooOOo0o ( O000OOO + ' - ' + O00o0OO0OO0oo , url , 90044 , I1i , I1i , IIIIiii1IIii )
 for url in next :
  o0OO ( 'NEXT' , url , 90043 , I1IIIii + 'Next.png' )
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
 for url , O000OOO in iI111i :
  Oo ( ( O000OOO ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , I1IIIii + 'movhub.png' )
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
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'http://onlinemovies.tube/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 oOOo0 = i11111IIIII ( ooO0000o00O )
 iI111i = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO , OoO000oo000o0 in iI111i :
  if 'movies' in OoO000oo000o0 :
   o0OO ( OoO000oo000o0 + '-' + O000OOO , IIo0o0O0O00oOOo , 90044 , I1i )
 for IIo0o0O0O00oOOo in next :
  i11Ii1IiIIIi ( IIo0o0O0O00oOOo )
  if 6 - 6: oOOoOooOo
def i1I11iIiII ( ) :
 o0OO ( 'Search' , '' , 80008 , I1IIIii + 'Search.png' )
 oOOo0 = i11111IIIII ( 'http://www.join4films.com/' )
 iI111i = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( O000OOO , IIo0o0O0O00oOOo , 80006 , I1IIIii + 'Desi.png' )
def o0Ii11iIiiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oOOo0 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , I1i , O000OOO in iI111i :
  Oo ( O000OOO , url , 80007 , I1i )
 for url , I1i , O000OOO in iI111i :
  o0OO ( 'Next' , url , 80006 , I1IIIii + 'Next.png' )
def o000 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  url = ( url ) . replace ( ' ' , '%20' )
  OOIi1iI111II1I1 ( url )
def i11ii1 ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'http://www.join4films.com/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 o0Ii11iIiiI ( ooO0000o00O )
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
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'http://imoviemax.se/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 Ooo0 ( ooO0000o00O )
def IiiiIIi ( url ) :
 I1IIIi = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oOOo0 )
 for url , O000OOO , OoOooOo00O in iI111i :
  if O000OOO in I1IIIi :
   pass
  else :
   o00oOOooOOo0o ( O000OOO + ' - ' + OoOooOo00O + ' Films' , url , 10074 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
   I1IIIi . append ( O000OOO )
   if 67 - 67: o0o00Oo0O % O0Oooo0O
def III ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , I1I in iI111i :
  o00oOOooOOo0o ( O000OOO + ' - Views:' + I1I , url , 10075 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
  if 70 - 70: i1iIi . o0o00Oo0O - OoOo0o
  if 62 - 62: O0Oooo0O * i1IiiiI1iI
def Ooo0 ( url ) :
 oOooOOoO0oO0oo0O = [ ]
 oOOo0 = i11111IIIII ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oOOo0 )
 for next in next :
  o00oOOooOOo0o ( 'NEXT PAGE' , next , 10074 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , O000OOO , url in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 10075 , I1i , I1i , '' )
  oOooOOoO0oO0oo0O . append ( O000OOO )
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
 for O0Ooo in iI111i :
  if '=m' in O0Ooo :
   O00o0o ( O0Ooo )
  elif 'php' in O0Ooo :
   OOii11Ii1IiiI1 ( url )
  else :
   oOOo0 = i11111IIIII ( O0Ooo )
   iI111i = re . compile ( 'content="([^"]*)">' ) . findall ( oOOo0 )
   for Ii1I1 in iI111i :
    O00o0o ( O0Ooo )
    if 65 - 65: oOoO0o00OO0 % OOOo00oo0oO . ii * ooo0O * oOo
    if 10 - 10: OOOo00oo0oO - iiiiiiii1 % IIiIiII11i - O0Oooo0O - ooOoO0O00
    if 10 - 10: oOoO0o00OO0 - i1IiiiI1iI . O0Oooo0O
def iiIIIi1iIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 OOo0OOOoOOo = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for iIiii , IIIooo0o0O in OOo0OOOoOOo :
  print 'there ><><><><><><><><><><><><'
  iIiii = iIiii
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIIooo0o0O ) )
  for O000OOO , I1I1Iiii1 in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + iIiii + '[/COLOR] - ' + O000OOO + ' - [COLOR' + iiI1IiI + ']' + I1I1Iiii1 + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
 O0ooooo0OOOO0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for iIiii , IiiiIIi11II in O0ooooo0OOOO0 :
  print 'there ><><><><><><><><><><><><'
  iIiii = iIiii
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiiiIIi11II ) )
  for O000OOO , I1I1Iiii1 in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + iIiii + '[/COLOR] - ' + O000OOO + ' - [COLOR' + iiI1IiI + ']' + I1I1Iiii1 + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
   if 55 - 55: i1IiiiI1iI
   if 93 - 93: Ii . ooo0O
   if 16 - 16: ooOoO0O00 . ooOoO0O00 / O0Oooo0O % iii1i1iiiiIi / oOo0O0Ooo * oOoO0o00OO0
def IIIii11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0ooooo0OOOO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
 for O0ooooo0OOOO0 in O0ooooo0OOOO0 :
  O000OOO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for O000OOO in O000OOO :
   O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iIiII = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for iIiII in iIiII :
   iIiII = 'http:' + iIiII
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII , '' , '' )
  if 29 - 29: i1iIi - i1iIi / oOOoOooOo
  if 49 - 49: i1IiiiI1iI + OOOo00oo0oO % oOo - I1ii11iIi11i - o0o00Oo0O - ii
  if 4 - 4: IIiIiII11i - OOOo00oo0oO % I1ii11iIi11i * Ii
  if 18 - 18: I1ii11iIi11i % o0o00Oo0O
def OO0OO0OO ( url ) :
 if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
 IIIIIiiI11i1 = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oOOo0 )
 for O0Ooo , I1i , O000OOO , Iii1I in iI111i :
  O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  oo00O00oO = i11111IIIII ( O0Ooo )
  IIi11i1i1iI1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( oo00O00oO )
  for I1ii1ii1I , II1 in IIi11i1i1iI1 :
   oooII111 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( II1 ) )
   for IIIIiii1IIii in oooII111 :
    if O000OOO in IIIIIiiI11i1 :
     pass
    else :
     O0O0ooOOO ( O000OOO , I1ii1ii1I , 8043 , I1i , I1i , IIIIiii1IIii )
     iIiIi11 ( 'movies' , 'INFO' )
     IIIIIiiI11i1 . append ( O000OOO )
     if 29 - 29: I11i1ii1 + Ii * o0o00Oo0O - iiiiiiii1 . IIiIiII11i % i1iIi
     if 41 - 41: OOOo00oo0oO / OoOo0o + iiiiiiii1 + oOOoOooOo
def iiiiii1Ii ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
 for url , i1i1II1i11 , IIIIiii1IIii , iI1iIii11Ii , O000OOO in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 10065 , i1i1II1i11 , iI1iIii11Ii , IIIIiii1IIii )
 iIiIi11 ( 'movies' , 'INFO' )
 if 20 - 20: O0Oooo0O + O0Oooo0O * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
def OooOo ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'https://www.youtube.com/results?search_query=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 oOOo0 = i11111IIIII ( ooO0000o00O )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in next :
  IIo0o0O0O00oOOo = 'https://www.youtube.com' + IIo0o0O0O00oOOo
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , IIo0o0O0O00oOOo , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for I1i , IIo0o0O0O00oOOo , O000OOO , O0OOoOOO0o0o , II1 in iI111i :
  iiiiiIIii . append ( O000OOO )
  iIiIi11 ( 'tvshows' , 'INFO' )
  iIiII = 'http:' + ( I1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iIiII
  IIo0o0O0O00oOOo = 'http://www.youtube.com' + IIo0o0O0O00oOOo
  O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII , iIiII , II1 )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for I1i , IIo0o0O0O00oOOo , O000OOO , O0OOoOOO0o0o in iI111i :
   print 'im doing it'
   iIiIi11 ( 'tvshows' , 'INFO' )
   iIiII = 'http:' + ( I1i ) . replace ( 'https:' , '' )
   IIo0o0O0O00oOOo = 'http://www.youtube.com' + IIo0o0O0O00oOOo
   if '&' in IIo0o0O0O00oOOo :
    print ' i got here'
    oOOo0 = i11111IIIII ( IIo0o0O0O00oOOo )
    O0ooooo0OOOO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for O0ooooo0OOOO0 in O0ooooo0OOOO0 :
     O000OOO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
     for O000OOO in O000OOO :
      O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     IIo0o0O0O00oOOo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0ooooo0OOOO0 ) )
     for IIo0o0O0O00oOOo in IIo0o0O0O00oOOo :
      IIo0o0O0O00oOOo = 'https://www.youtube.com/w' + IIo0o0O0O00oOOo
     iIiII = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
     for iIiII in iIiII :
      iIiII = 'http:' + iIiII
     O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII , Oo00OOOOO , '' )
   elif O000OOO in iiiiiIIii :
    pass
   elif 'user' in IIo0o0O0O00oOOo or 'elete' in O000OOO :
    pass
   elif 'hannel' in IIo0o0O0O00oOOo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + IIo0o0O0O00oOOo
    oOOo0 = i11111IIIII ( IIo0o0O0O00oOOo )
    iI = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for I1i , IIo0o0O0O00oOOo , O000OOO in iI :
     if 'outube' in IIo0o0O0O00oOOo or 'list' in IIo0o0O0O00oOOo :
      pass
     elif 'atch' in IIo0o0O0O00oOOo :
      IIo0o0O0O00oOOo = ( IIo0o0O0O00oOOo ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1i , 'http:' + I1i , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII , iIiII , '' )
    if 88 - 88: ooOoO0O00 % oOOoOooOo . Ii . ooOoO0O00
def ooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for url in next :
  url = 'https://www.youtube.com' + url
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for I1i , url , O000OOO , O0OOoOOO0o0o , II1 in iI111i :
  iiiiiIIii . append ( O000OOO )
  iIiIi11 ( 'tvshows' , 'INFO' )
  iIiII = 'http:' + ( I1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iIiII
  url = 'http://www.youtube.com' + url
  O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII , iIiII , II1 )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for I1i , url , O000OOO , O0OOoOOO0o0o in iI111i :
   iIiIi11 ( 'tvshows' , 'INFO' )
   iIiII = 'http:' + ( I1i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oOOo0 = i11111IIIII ( url )
    O0ooooo0OOOO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for O0ooooo0OOOO0 in O0ooooo0OOOO0 :
     O000OOO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
     for O000OOO in O000OOO :
      O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0ooooo0OOOO0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iIiII = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0ooooo0OOOO0 ) )
     for iIiII in iIiII :
      iIiII = 'http:' + iIiII
     O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII , Oo00OOOOO , '' )
   elif O000OOO in iiiiiIIii :
    pass
   elif 'user' in url or 'elete' in O000OOO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oOOo0 = i11111IIIII ( url )
    iI = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for I1i , url , O000OOO in iI :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1i , 'http:' + I1i , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + O0OOoOOO0o0o + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII , iIiII , '' )
    if 53 - 53: oOo0O0Ooo % ii + O0Oooo0O - I1ii11iIi11i / I11i1ii1 * ooo0O
    if 79 - 79: ii / oOo0O0Ooo
    if 87 - 87: I11i1ii1 . ooOoO0O00 % ii * Ii
def o0oOo ( ) :
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Setup Tv Guide[/COLOR]' , '' , 100212 , I1IIIii + 'linkchannels.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Open Guide[/COLOR]' , '' , 100213 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 if 51 - 51: IIiIiII11i . OOOo00oo0oO . oOo % IIiIiII11i
def III1I1ii ( ) :
 ivuesetup . iVueInt ( )
 if 4 - 4: iI11I1II1I1I . ooOoO0O00
def Oo00oo ( ) :
 oO0oO ( )
 return
 if 71 - 71: O0Oooo0O / oOo0O0Ooo / o0o00Oo0O
def oO0oO ( ) :
 if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / OoOo0o . oOoO0o00OO0 * oOOoOooOo
 OOooOoooOoOo = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 oo0O = OOooOoooOoOo . getSetting ( id = 'User' )
 Ooooo0O0 = OOooOoooOoOo . getSetting ( id = 'Pass' )
 oOoO000 = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 Oo00o00Oo = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 i1I1i1I111 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 oOo00OO0ooOOO = "http://piesustv" + Ooo + ":8000/get.php?username=" + oo0O + "&password=" + Ooooo0O0 + "&type=m3u_plus&output=ts"
 i1i1I1Ii1IIii = "http://piesustv" + Ooo + ":8000/xmltv.php?username=" + oo0O + "&password=" + Ooooo0O0 + "&type=m3u_plus&output=ts"
 if 80 - 80: Ii
 xbmc . executeJSONRPC ( oOoO000 )
 xbmc . executeJSONRPC ( Oo00o00Oo )
 xbmc . executeJSONRPC ( i1I1i1I111 )
 if 29 - 29: oOo0O0Ooo . OoOo0o + IIiIiII11i . I1ii11iIi11i
 I1iii1iIi = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 I1iii1iIi . setSetting ( id = 'm3uUrl' , value = oOo00OO0ooOOO )
 I1iii1iIi . setSetting ( id = 'epgUrl' , value = i1i1I1Ii1IIii )
 I1iii1iIi . setSetting ( id = 'm3uCache' , value = "false" )
 I1iii1iIi . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def i1II1i ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 27 - 27: oOoO0o00OO0 / OoOo0o
if 33 - 33: ii % oOoO0o00OO0 . o0o00Oo0O / oOoO0o00OO0
if 63 - 63: I11i1ii1 + iI11I1II1I1I + oOo0O0Ooo + O0Oooo0O
def oOOoO0O ( ) :
 if 76 - 76: ooOoO0O00 / iI11I1II1I1I - oOoO0o00OO0 - IIiIiII11i
 if 76 - 76: Ii + I11i1ii1 % iii1i1iiiiIi
 if 6 - 6: iiiiiiii1
 if 65 - 65: IIiIiII11i . oOo0O0Ooo + o0o00Oo0O
 if 75 - 75: o0o00Oo0O % iI11I1II1I1I / iii1i1iiiiIi % OoOo0o / I11i1ii1
 if 31 - 31: Ii * iii1i1iiiiIi
 if 69 - 69: Ii
 if 61 - 61: o0o00Oo0O
 if 21 - 21: oOo % iI11I1II1I1I . oOo
 if 99 - 99: ooo0O * OoOo0o % OOOo00oo0oO * OOOo00oo0oO + ii
 if 82 - 82: i1IiiiI1iI / iii1i1iiiiIi - OoOo0o / oOOoOooOo
 if 50 - 50: OoOo0o + oOo . Ii + oOoO0o00OO0 + Ii
 if OooO0 == "insert_username" :
  IIi11I1i1I1I = IiII1I ( )
  O0oO0oOO00Oo = IIIi1i ( )
  i1 ( 'User' , IIi11I1i1I1I )
  i1 ( 'Pass' , O0oO0oOO00Oo )
  xbmc . executebuiltin ( 'Container.Refresh' )
  iI1111i1i11Ii = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( IIi11I1i1I1I , O0oO0oOO00Oo )
  iI1111i1i11Ii = i11111IIIII ( iI1111i1i11Ii )
  if iI1111i1i11Ii == "" :
   oo0O00o0O0Oo = "[COLOR " + iiI1IiI + "]Incorrect Login Details[/COLOR]"
   iii11 = "[COLOR " + iiI1IiI + "]Please Re-enter[/COLOR]"
   I1i11IIIi = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , oo0O00o0O0Oo , iii11 , I1i11IIIi )
   oOOoO0O ( )
  else :
   oo0O00o0O0Oo = "[COLOR " + iiI1IiI + "]Login Successful[/COLOR]"
   iii11 = "[COLOR " + iiI1IiI + "]Welcome to GenieTv[/COLOR]"
   I1i11IIIi = ( '[COLOR ' + iiI1IiI + ']%s[/COLOR]' % IIi11I1i1I1I )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , oo0O00o0O0Oo , iii11 , I1i11IIIi )
   xbmc . executebuiltin ( 'Container.Refresh' )
   III1IIIIIiiI ( )
 else :
  III1IIIIIiiI ( )
def IiII1I ( ) :
 i1iIii = xbmc . Keyboard ( '' , 'heading' , True )
 i1iIii . setHeading ( 'Enter Username' )
 i1iIii . setHiddenInput ( False )
 i1iIii . doModal ( )
 if ( i1iIii . isConfirmed ( ) ) :
  O0o00 = i1iIii . getText ( )
  return O0o00
 else :
  return False
  if 8 - 8: O0Oooo0O * I1ii11iIi11i - OoOo0o . iI11I1II1I1I
  if 48 - 48: Ii / IIiIiII11i + i1iIi + ooo0O . O0Oooo0O % OoOo0o
def IIIi1i ( ) :
 i1iIii = xbmc . Keyboard ( '' , 'heading' , True )
 i1iIii . setHeading ( 'Enter Password' )
 i1iIii . setHiddenInput ( False )
 i1iIii . doModal ( )
 if ( i1iIii . isConfirmed ( ) ) :
  O0o00 = i1iIii . getText ( )
  return O0o00
 else :
  return False
def o0Oo00OOoO0oo ( ) :
 oOo00OO0ooOOO = "http://piesustv" + Ooo + ":8000//get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  IIi11ii11 = urllib2 . urlopen ( oOo00OO0ooOOO )
  print IIi11ii11 . getcode ( )
  IIi11ii11 . close ( )
  if 54 - 54: i1IiiiI1iI % o0o00Oo0O - OoOo0o % oOo + oOo . I11i1ii1
  pass
  if 99 - 99: oOo / ooOoO0O00 . oOoO0o00OO0
 except urllib2 . HTTPError , o000O0O :
  print o000O0O . getcode ( )
  iI111I11I1I1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + iiI1IiI + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + iiI1IiI + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def III1IIIIIiiI ( ) :
 Oo0O00O0O ( )
 if 23 - 23: i1iIi * oOOoOooOo - i1IiiiI1iI . o0o00Oo0O % iI11I1II1I1I
 if 19 - 19: oOo0O0Ooo
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']My Account[/COLOR]' , 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii , 60004 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Guide Menu[/COLOR]' , '' , 100211 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CatchUp Tv[/COLOR]' , '' , 90026 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']VOD Lists[/COLOR]' , '' , 40000 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 66 - 66: OOOo00oo0oO / iii1i1iiiiIi
 if 13 - 13: IIiIiII11i
 if 55 - 55: I1ii11iIi11i % ooOoO0O00 * i1IiiiI1iI
 if 95 - 95: OoOo0o / IIiIiII11i - ooo0O % O0Oooo0O . i1IiiiI1iI
def oo0o ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 o0o00O = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii + '%26type%3Dm3u_plus%26output%3Dts'
 iiiI1ii = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii
 iI1111i1i11Ii = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=get_vod_categories'
 iI1111i1i11Ii = i11111IIIII ( iI1111i1i11Ii )
 if not iI1111i1i11Ii == "" :
  oOoooOooOOoO = 'https://tinyurl.com/create.php?source=indexpage&url=' + o0o00O + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( oOoooOooOOoO ) )
  O0O0O0OO00oo = 'https://tinyurl.com/create.php?source=indexpage&url=' + iiiI1ii + '&submit=Make+TinyURL%21&alias='
  o0o00O = i11111IIIII ( oOoooOooOOoO )
  iiiI1ii = i11111IIIII ( O0O0O0OO00oo )
  xbmc . log ( str ( iiiI1ii ) )
  I11IIIIiI1 = o0oOOO ( o0o00O , '<div class="indent"><b>' , '</b>' )
  o00OoOooo = o0oOOO ( iiiI1ii , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + iiI1IiI + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % I11IIIIiI1 , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % o00OoOooo )
 else :
  return
def i1I1ii1 ( ) :
 o0Oo00OOoO0oo ( )
 Iii1i ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , ooOooo00O + '&action=get_vod_streams' , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( I1i1I1IIiIIi )
 iI111i = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o00oOOooOOo0o ( ( '[COLORsteelblue]' + O000OOO + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIo0o0O0O00oOOo , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
def iII1ii1IIII ( url ) :
 open = i11111IIIII ( Oo0 + url )
 o0O0OOOo0 = I1ii1i ( open , '<channel>' , '</channel>' )
 for iiI11Iii in o0O0OOOo0 :
  if '<playlist_url>' in open :
   O000OOO = o0oOOO ( iiI11Iii , '<title>' , '</title>' )
   o0OOOOOo0 = o0oOOO ( iiI11Iii , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   o00oOOooOOo0o ( str ( base64 . b64decode ( O000OOO ) ) . replace ( '?' , '' ) , o0OOOOOo0 , 40001 , icon , iI1iIii11Ii , '' )
  else :
   if xbmcaddon . Addon ( ) . getSetting ( 'meta' ) == 'true' :
    try :
     O000OOO = o0oOOO ( iiI11Iii , '<title>' , '</title>' )
     O000OOO = base64 . b64decode ( O000OOO )
     OO00OoOO = o0oOOO ( iiI11Iii , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     url = o0oOOO ( iiI11Iii , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     IIIIiii1IIii = o0oOOO ( iiI11Iii , '<description>' , '</description>' )
     IIIIiii1IIii = base64 . b64decode ( IIIIiii1IIii )
     i1iiIIi11I = o0oOOO ( IIIIiii1IIii , 'PLOT:' , '\n' )
     iiii1II1ii11 = o0oOOO ( IIIIiii1IIii , 'CAST:' , '\n' )
     i1IIIII1 = o0oOOO ( IIIIiii1IIii , 'RATING:' , '\n' )
     o0o0oOo000o0 = o0oOOO ( IIIIiii1IIii , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
     o0o0oOo000o0 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( o0o0oOo000o0 )
     IIIiiiiiI1I = o0oOOO ( IIIIiii1IIii , 'DURATION_SECS:' , '\n' )
     O0oooO00ooO0 = o0oOOO ( IIIIiii1IIii , 'GENRE:' , '\n' )
     o00OOO0o00OO ( str ( O000OOO ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , OO00OoOO , iI1iIii11Ii , i1iiIIi11I , str ( o0o0oOo000o0 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( iiii1II1ii11 ) . split ( ) , i1IIIII1 , IIIiiiiiI1I , O0oooO00ooO0 )
    except : pass
    xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   else :
    O000OOO = o0oOOO ( iiI11Iii , '<title>' , '</title>' )
    O000OOO = base64 . b64decode ( O000OOO )
    OO00OoOO = o0oOOO ( iiI11Iii , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    url = o0oOOO ( iiI11Iii , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    IIIIiii1IIii = o0oOOO ( iiI11Iii , '<description>' , '</description>' )
    O0O0ooOOO ( O000OOO , url , 222 , OO00OoOO , iI1iIii11Ii , base64 . b64decode ( IIIIiii1IIii ) )
    if 100 - 100: i1IiiiI1iI
iI1iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
I1i1IIIIIII1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 10 - 10: oOoO0o00OO0 + I11i1ii1
def Ooooo00 ( ) :
 oOo00OO0ooOOO = "http://piesustv" + Ooo + ":8000/get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  IIi11ii11 = urllib2 . urlopen ( oOo00OO0ooOOO )
  print IIi11ii11 . getcode ( )
  IIi11ii11 . close ( )
  if 99 - 99: oOoO0o00OO0 - OOOo00oo0oO
  pass
  if 10 - 10: IIiIiII11i . oOo
 except urllib2 . HTTPError , o000O0O :
  print o000O0O . getcode ( )
  iI111I11I1I1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 89 - 89: oOOoOooOo * i1iIi
 IIo0o0O0O00oOOo = "http://piesustv" + Ooo + ":8000/xmltv.php?username=%s&password=%s" % ( OooO0 , II11iiii1Ii )
 Oo0o0O0o0oo0O0O ( IIo0o0O0O00oOOo , I1i1IIIIIII1 + "uide.xml" )
 if 84 - 84: i1IiiiI1iI . iiiiiiii1
 OOOO0OOO = open ( iI1iIi , 'r+' )
 input = open ( iI1iIi ) . read ( ) . decode ( 'UTF-8' )
 i111i = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 OOOO0OOO . write ( i111i )
 OOOO0OOO . truncate ( )
 OOOO0OOO . close ( )
 i1iIiII11i1 ( )
 if 44 - 44: oOo0O0Ooo % OoOo0o * Ii * Ii - I1ii11iIi11i . O0Oooo0O
def i1iIiII11i1 ( ) :
 open = i11111IIIII ( o00i111iiIiiIiI )
 all = I1ii1i ( open , '{"num' , 'direct' )
 for iiI11Iii in all :
  if '"tv_archive":1' in iiI11Iii :
   O000OOO = o0oOOO ( iiI11Iii , '"epg_channel_id":"' , '"' )
   OO00OoOO = o0oOOO ( iiI11Iii , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = o0oOOO ( iiI11Iii , 'stream_id":"' , '"' )
   O000OOO = O000OOO . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   o00oOOooOOo0o ( O000OOO , id , 90027 , OO00OoOO , iI1iIii11Ii , O000OOO )
   if 59 - 59: OoOo0o + oOo0O0Ooo / IIiIiII11i / iii1i1iiiiIi
   if 80 - 80: iii1i1iiiiIi + iI11I1II1I1I . I11i1ii1
def ooOoOoo000O0O ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 oOoooooOoO = open ( iI1iIi )
 iI11i = ElementTree . parse ( oOoooooOoO )
 oOOO0 = "apples"
 import datetime as dt
 from datetime import time
 I1iIIi = datetime . now ( ) - timedelta ( days = 5 )
 iIiii = str ( I1iIIi )
 oOoOooOo0o0 = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 IIiIi11i111II = iI11i . findall ( "programme" )
 for ooO0 in IIiIi11i111II :
  if name in ooO0 . attrib . get ( 'channel' ) :
   Iii11ii1iIIi = ooO0 . attrib . get ( 'start' )
   iiii1Ii1iii , Oo0Oo0 , oooOooooO = Iii11ii1iIIi . partition ( ' +' )
   iIiii = str ( iIiii ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   o0o0oOo000o0 , i1IIiiIIIIi , I11II1i1 = Iii11ii1iIIi . partition ( '2017' )
   IiIIIi = ooO0 . find ( 'title' ) . text + Iii11ii1iIIi
   I11II1i1 = I11II1i1 [ : - 6 ]
   if iiii1Ii1iii > iIiii :
    if iiii1Ii1iii < oOoOooOo0o0 :
     Oo0iII = iiii1Ii1iii
     Oo0iII = Oo0iII [ : 4 ] + '/' + Oo0iII [ 4 : ]
     iiii1Ii1iii = iiii1Ii1iii [ : 4 ] + '-' + iiii1Ii1iii [ 4 : ]
     Oo0iII = Oo0iII [ : 7 ] + '/' + Oo0iII [ 7 : ]
     iiii1Ii1iii = iiii1Ii1iii [ : 7 ] + '-' + iiii1Ii1iii [ 7 : ]
     Oo0iII = Oo0iII [ : 10 ] + ' - ' + Oo0iII [ 10 : ]
     iiii1Ii1iii = iiii1Ii1iii [ : 10 ] + ':' + iiii1Ii1iii [ 10 : ]
     Oo0iII = Oo0iII [ : 15 ] + ':' + Oo0iII [ 15 : ]
     iiii1Ii1iii = iiii1Ii1iii [ : 13 ] + '-' + iiii1Ii1iii [ 13 : ]
     Oo0iII = Oo0iII [ : - 2 ]
     iiii1Ii1iii = iiii1Ii1iii [ : - 2 ]
     O0ooiIIi1 = ( "http://piesustv" + Ooo + ":8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( iiii1Ii1iii ) + "&duration=240" + "&stream=%s" ) % ( OooO0 , II11iiii1Ii , id )
     oOOO0 = O0ooiIIi1 + str ( iiii1Ii1iii ) + "&duration=240"
     Oo0iII = '[COLOR blue]%s - [/COLOR]' % Oo0iII
     IiIIIi = str ( Oo0iII ) + ooO0 . find ( 'title' ) . text
     IIIIiii1IIii = ooO0 . find ( 'desc' ) . text
     O0O0ooOOO ( IiIIIi , O0ooiIIi1 , 222 , I1IIIii + 'GTV.png' , Oo00OOOOO , IIIIiii1IIii )
def OoOo0O00 ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OooO0 ) . replace ( 'PASSWORD' , II11iiii1Ii )
 o0OoOo00ooO = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 o0OoOo00ooO . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 o0OoOo00ooO . setProperty ( 'IsPlayable' , 'true' )
 o0OoOo00ooO . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOo00ooO )
def Oo0o0O0o0oo0O0O ( url , dest ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oO0 . update ( 0 )
 iI1i1iI1iI = time . time ( )
 urllib . urlretrieve ( url , dest , lambda I1IIiIi , OOOOoOoO , OO000 : o0oOoo0o ( I1IIiIi , OOOOoOoO , OO000 , o0oO0 , iI1i1iI1iI ) )
def o0oOoo0o ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  IiiIiIIi = min ( numblocks * blocksize * 100 / filesize , 100 )
  O00Oo = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  oOOoooo0O0 = numblocks * blocksize / ( time . time ( ) - start_time )
  if oOOoooo0O0 > 0 :
   Ii111Ii11 = ( filesize - numblocks * blocksize ) / oOOoooo0O0
  else :
   Ii111Ii11 = 0
  oOOoooo0O0 = oOOoooo0O0 / 1024
  Ii1 = oOOoooo0O0 / 1024
  IIIIiII = float ( filesize ) / ( 1024 * 1024 )
  iII11 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( O00Oo )
  o000O0O = '[COLOR white]Speed:  %.02f Mb/s ' % Ii1 + '[/COLOR]'
  dp . update ( IiiIiIIi , iII11 , o000O0O )
 except :
  IiiIiIIi = 100
  dp . update ( IiiIiIIi )
 if dp . iscanceled ( ) :
  O00OO00OOOoO = xbmcgui . Dialog ( )
  O00OO00OOOoO . ok ( "GenieTv" , 'The download was cancelled.' )
  if 47 - 47: ooOoO0O00 % oOOoOooOo - I1ii11iIi11i * i1IiiiI1iI / Ii
  sys . exit ( )
  dp . close ( )
  if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . O0Oooo0O / OOOo00oo0oO
def ii1iI11 ( ) :
 if II11iiii1Ii == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  OOOO000oo0o00 ( )
  if 14 - 14: o0o00Oo0O * o0o00Oo0O - o0o00Oo0O
  if 55 - 55: OOOo00oo0oO / iiiiiiii1 . oOo0O0Ooo * O0Oooo0O % O0Oooo0O - ooo0O
  if 95 - 95: OoOo0o * iiiiiiii1 . ooo0O
  if 73 - 73: oOo
  if 28 - 28: ii - i1IiiiI1iI
  if 84 - 84: IIiIiII11i
  if 36 - 36: OoOo0o - iii1i1iiiiIi - iI11I1II1I1I
  if 10 - 10: oOoO0o00OO0 / i1iIi * ooOoO0O00 % o0o00Oo0O + i1IiiiI1iI
def OOOO000oo0o00 ( ) :
 IIIi1I1IIii1II = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( '"exp_date":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for IIo0o0O0O00oOOo in iI111i :
  dt = datetime . fromtimestamp ( float ( iI111i [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if oOoOooOo0o0 <= dt <= oOoOooOo0o0 + timedelta ( hours = 24 ) :
   iI111I11I1I1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + iiI1IiI + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + iiI1IiI + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + iiI1IiI + '] To Purchase A licence[/COLOR]' )
def I1i1ii1ii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( '"username":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 i1ii = re . compile ( '"password":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 oOOoo = re . compile ( '"status":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 IIi11i1i1iI1 = re . compile ( '"exp_date":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 OoOOo0OOoO = re . compile ( '"active_cons":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 ooO0O00Oo0o = re . compile ( '"created_at":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 OOO = re . compile ( '"max_connections":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 Oo0o00OO0000 = re . compile ( '"is_trial":"1"' ) . findall ( IIIi1I1IIii1II )
 o00Oo0oooooo = re . compile ( '"is_trial":"0"' ) . findall ( IIIi1I1IIii1II )
 oOOOOO0 = IIi1I1 ( )
 oO00o0oOoo = oOO ( )
 for url in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']My GTV Account Information[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  Oo ( '[COLOR' + iiI1IiI + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in i1ii :
  Oo ( '[COLOR' + iiI1IiI + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in oOOoo :
  Oo ( '[COLOR' + iiI1IiI + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in ooO0O00Oo0o :
  dt = datetime . fromtimestamp ( float ( ooO0O00Oo0o [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  Oo ( '[COLOR' + iiI1IiI + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in IIi11i1i1iI1 :
  dt = datetime . fromtimestamp ( float ( IIi11i1i1iI1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if oOoOooOo0o0 <= dt <= oOoOooOo0o0 + timedelta ( hours = 24 ) :
   Oo ( '[COLORred]Expires Today[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  Oo ( '[COLOR' + iiI1IiI + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in OoOOo0OOoO :
  Oo ( '[COLOR' + iiI1IiI + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in OOO :
  Oo ( '[COLOR' + iiI1IiI + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in Oo0o00OO0000 :
  Oo ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] Yes' , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in o00Oo0oooooo :
  Oo ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] No' , '' , '' , I1IIIii + 'MyAcc.png' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Get Short Links[/COLOR]' , '' , 100214 , I1IIIii + 'shortlinks.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local IP Address:[/COLOR] ' + oOOOOO0 , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']External IP Address:[/COLOR] ' + oO00o0oOoo , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 38 - 38: i1IiiiI1iI . I11i1ii1 - oOo . oOo0O0Ooo
 Oo ( '[COLOR' + iiI1IiI + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 65 - 65: O0Oooo0O
def ii1Io0oOO0 ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
 I11II11IiI11 ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 97 - 97: oOOoOooOo / iI11I1II1I1I % oOOoOooOo / oOo0O0Ooo * iiiiiiii1 % iii1i1iiiiIi
def i1iiii1 ( data ) :
 oOO0000 = len ( data ) % 4
 if 84 - 84: o0o00Oo0O % i1iIi . i1iIi . iiiiiiii1 * i1IiiiI1iI
 if 43 - 43: iii1i1iiiiIi . oOoO0o00OO0 % ooOoO0O00
 if 61 - 61: oOo0O0Ooo + OOOo00oo0oO % O0Oooo0O % iI11I1II1I1I - ii
 if 22 - 22: OoOo0o + IIiIiII11i + I1ii11iIi11i
 if 83 - 83: oOOoOooOo
 if 43 - 43: OoOo0o
 if oOO0000 != 0 :
  data += b'=' * ( 4 - oOO0000 )
 return base64 . decodestring ( data )
def o0oOOO ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : o0IiiIIII1I1i = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : o0IiiIIII1I1i = ''
 else :
  try : o0IiiIIII1I1i = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : o0IiiIIII1I1i = ''
 return o0IiiIIII1I1i
 if 26 - 26: iiiiiiii1 - I1ii11iIi11i + oOo0O0Ooo + ooo0O
 if 37 - 37: ooo0O * OoOo0o + oOo0O0Ooo . oOoO0o00OO0 * ii
def I1ii1i ( text , start_with , end_with ) :
 o0IiiIIII1I1i = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return o0IiiIIII1I1i
def IIi1I1 ( ) :
 OoooOO0 = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 OoooOO0 . connect ( ( '8.8.8.8' , 0 ) )
 OoooOO0 = OoooOO0 . getsockname ( ) [ 0 ]
 return OoooOO0
 if 69 - 69: IIiIiII11i + iiiiiiii1
def oOO ( ) :
 open = i11111IIIII ( 'http://canyouseeme.org/' )
 oOOOOO0 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( oOOOOO0 . group ( ) )
ooOooo00O = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
o00i111iiIiiIiI = 'http://piesustv' + Ooo + ':8000/panel_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
oooOOO = 'http://piesustv' + Ooo + ':8000/movie/%s/%s/' % ( OooO0 , II11iiii1Ii )
Iii1o00o0 = 'http://piesustv' + Ooo + ':8000/live/%s/%s/' % ( OooO0 , II11iiii1Ii )
OOoOo0O0 = '&action=get_live_categories'
I1o0 = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OooO0 , II11iiii1Ii )
I1i1I1IIiIIi = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OooO0 , II11iiii1Ii )
if 26 - 26: iiiiiiii1 * iI11I1II1I1I + IIiIiII11i / oOo0O0Ooo
Oo0 = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OooO0 , II11iiii1Ii )
O0OO = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OooO0 , II11iiii1Ii )
o0o0O00oOo = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OooO0 , II11iiii1Ii )
iI1ii = "http://piesustv" + Ooo + ":8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OooO0 , II11iiii1Ii )
if 2 - 2: IIiIiII11i . i1IiiiI1iI
def OoO0oOOOO ( ) :
 o0Oo00OOoO0oo ( )
 open = i11111IIIII ( o0o0O00oOo )
 o0O0OOOo0 = I1ii1i ( open , '<channel>' , '</channel>' )
 for iiI11Iii in o0O0OOOo0 :
  O000OOO = o0oOOO ( iiI11Iii , '<title>' , '</title>' )
  O000OOO = base64 . b64decode ( O000OOO )
  o0OOOOOo0 = o0oOOO ( iiI11Iii , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '[/COLOR]' , o0OOOOOo0 , 60003 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
  if 75 - 75: OoOo0o % IIiIiII11i
def IIIIi1Iii1iIi ( url ) :
 open = i11111IIIII ( iI1ii + url )
 o0O0OOOo0 = I1ii1i ( open , '<channel>' , '</channel>' )
 for iiI11Iii in o0O0OOOo0 :
  O000OOO = o0oOOO ( iiI11Iii , '<title>' , '</title>' )
  O000OOO = base64 . b64decode ( O000OOO )
  xbmc . log ( str ( O000OOO ) )
  OO00OoOO = o0oOOO ( iiI11Iii , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o0OOOOOo0 = o0oOOO ( iiI11Iii , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  IIIIiii1IIii = o0oOOO ( iiI11Iii , '<description>' , '</description>' )
  IIIIiii1IIii = base64 . b64decode ( IIIIiii1IIii )
  ii1IIi1iI1ii1 = '('
  o00iIIiIi111iI = ')'
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , o0OOOOOo0 , 222 , OO00OoOO , iI1iIii11Ii , ( '[COLOR' + iiI1IiI + ']' + IIIIiii1IIii + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( o00iIIiIi111iI , '[COLORsteelblue]' ) . replace ( ii1IIi1iI1ii1 , '[COLORorangered]' ) )
  if 40 - 40: iii1i1iiiiIi + oOo % ii * ooo0O / iii1i1iiiiIi + ii
def o0OOOoO0O ( url ) :
 url = url
 oOOo0 = i11111IIIII ( I1o0 + url )
 iI111i = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , type , O0Ooo , o0o0OO0o00o0O in iI111i :
  Ii1I1 = ( Iii1o00o0 + O0Ooo + '.m3u8' ) . strip ( )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , Ii1I1 , 222 , ( o0o0OO0o00o0O ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
def OoOOoIII11iI1i11i ( url , name , img ) :
 img = img
 name = name
 url = url
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/xmltv.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIIiIi , IIiI in iI111i :
  if name == iIIIiIi :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) + IIiI , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def OOoOo0oO0oo00 ( name ) :
 OOI1I = name
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oOOo0 )
 for name , I1i , IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = ( IIo0o0O0O00oOOo ) . replace ( '.ts' , '.m3u8' )
  O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1i , I1i , '' )
 else :
  O0O0ooOOO ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 54 - 54: iii1i1iiiiIi
  if 73 - 73: iiiiiiii1 + i1iIi
  if 37 - 37: OOOo00oo0oO - iI11I1II1I1I + IIiIiII11i . i1iIi % iI11I1II1I1I
  if 17 - 17: O0Oooo0O + ooOoO0O00 % o0o00Oo0O
  if 65 - 65: I11i1ii1
  if 50 - 50: IIiIiII11i / oOo
  if 79 - 79: oOoO0o00OO0 - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
  if 95 - 95: OOOo00oo0oO
  if 48 - 48: i1IiiiI1iI / iI11I1II1I1I % IIiIiII11i
  if 39 - 39: ooOoO0O00 . oOoO0o00OO0 / i1IiiiI1iI / i1IiiiI1iI
  if 100 - 100: ii - ii + I11i1ii1
  if 32 - 32: iii1i1iiiiIi * ooo0O / ii
def o0OO0 ( ) :
 o00oOOooOOo0o ( 'Full Backup' , '' , 10061 , I1IIIii + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0OoO00oOO0o ) :
  o00oOOooOOo0o ( 'Backup Genie Favourites' , IIo0o0O0O00oOOo , 10062 , I1IIIii + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( ooOooo000oOO ) :
  o00oOOooOOo0o ( 'Backup Ivue Config' , ooOooo000oOO , 10062 , I1IIIii + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( Oo0oOOo ) :
  o00oOOooOOo0o ( 'Backup Kodi Favourites' , Oo0oOOo , 10062 , I1IIIii + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 90 - 90: O0Oooo0O
  if 35 - 35: IIiIiII11i / i1iIi
  if 79 - 79: iii1i1iiiiIi + O0Oooo0O * iiiiiiii1 * i1iIi
zip = O0oo0OO0 . getSetting ( 'zip' )
oOOo = xbmc . translatePath ( os . path . join ( zip ) )
def iI111iIi ( ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 26 - 26: OoOo0o % OoOo0o / Ii + oOoO0o00OO0 - o0o00Oo0O
  if 20 - 20: O0Oooo0O . o0o00Oo0O - oOoO0o00OO0 / iii1i1iiiiIi - ooo0O
  if 79 - 79: ii - iI11I1II1I1I
def iiIII1i1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0OoO00oOO0o
  elif 'Ivue' in name :
   url = ooOooo000oOO
  elif 'Kodi' in name :
   url = Oo0oOOo
  iI111iIi ( )
  oOOo0OOoOO0 = open ( url ) . read ( )
  IiIi = os . path . join ( oOOo , description . split ( 'Your ' ) [ 1 ] )
  OOOO0OOO = open ( IiIi , mode = 'w' )
  OOOO0OOO . write ( oOOo0OOoOO0 )
  OOOO0OOO . close ( )
 else :
  if 'guisettings.xml' in description :
   iiI11Iii = open ( os . path . join ( oOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0IiiIIII1I1i = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   iI111i = re . compile ( o0IiiIIII1I1i ) . findall ( iiI11Iii )
   for type , IIi1IiiIi1III , IiIiIiiIIii in iI111i :
    IiIiIiiIIii = IiIiIiiIIii . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IIi1IiiIi1III , IiIiIiiIIii ) )
  else :
   IiIi = os . path . join ( url )
   oOOo0OOoOO0 = open ( os . path . join ( oOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOOO0OOO = open ( IiIi , mode = 'w' )
   OOOO0OOO . write ( oOOo0OOoOO0 )
   OOOO0OOO . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 77 - 77: OOOo00oo0oO * oOOoOooOo . OoOo0o * i1iIi % IIiIiII11i
 if 94 - 94: oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 if 75 - 75: I1ii11iIi11i + i1iIi + oOo
 if 97 - 97: oOOoOooOo % Ii % i1IiiiI1iI
def IIi1i ( ) :
 oO0oi1I1iI1 = 1
 iI111iIi ( )
 oOOoO = xbmc . translatePath ( os . path . join ( oOOo , 'Build Backup' , 'Full Backup' , '' ) )
 iii1i1Iiiiiii = xbmc . translatePath ( os . path . join ( oOOo , 'Build Backup' , 'my_full_backup.zip' ) )
 OOoo0 = xbmc . translatePath ( os . path . join ( oOOo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOOoO ) :
  os . makedirs ( oOOoO )
 Ii11I1iIIi = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not Ii11I1iIIi ) : return False , 0
 iIi11 = Ii11I1iIIi
 O0ooO = xbmc . translatePath ( os . path . join ( oOOoO , iIi11 + '.zip' ) )
 iIOO = [ 'plugin.video.GenieTv' ]
 I1III1I11I1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 oO000OoO00OoO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1IiIi1iiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iiII1II11i = "Creating full backup of existing build"
 ooO0OoooooOo0oOo0 = "Creating Community Build"
 II11II = "Archiving..."
 i1ii11 = ""
 IIIo00O = "Please Wait"
 ii1I1I1 ( i1111 , O0ooO , ooO0OoooooOo0oOo0 , II11II , i1ii11 , IIIo00O , oO000OoO00OoO , I1IiIi1iiI )
 time . sleep ( 1 )
 oo0oOOO0oOoo = xbmc . translatePath ( os . path . join ( oOOoO , iIi11 + '_guisettings.zip' ) )
 Ii1o0OOOoo0000 = zipfile . ZipFile ( oo0oOOO0oOoo , mode = 'w' )
 try :
  Ii1o0OOOoo0000 . write ( xbmc . translatePath ( os . path . join ( i1111 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 Ii1o0OOOoo0000 . close ( )
 if oO0oi1I1iI1 == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iii1i1Iiiiiii , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + O0ooO + '[/COLOR]' )
  if 19 - 19: ii . oOo0O0Ooo + O0Oooo0O - oOo0O0Ooo / oOo0O0Ooo % I11i1ii1
def ii1I1I1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 IiIIIii1i1iI = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 OoOOoO0o = len ( sourcefile )
 o0O00ooo0 = [ ]
 iI1 = [ ]
 o0oO0 . create ( message_header , message1 , message2 , message3 )
 for iIi1 , O00oOOO0 , Iiiiii in os . walk ( sourcefile ) :
  for file in Iiiiii :
   iI1 . append ( file )
 oOOOO = len ( iI1 )
 for iIi1 , O00oOOO0 , Iiiiii in os . walk ( sourcefile ) :
  O00oOOO0 [ : ] = [ OoOOoo0 for OoOOoo0 in O00oOOO0 if OoOOoo0 not in exclude_dirs ]
  Iiiiii [ : ] = [ OOOO0OOO for OOOO0OOO in Iiiiii if OOOO0OOO not in exclude_files ]
  for file in Iiiiii :
   o0O00ooo0 . append ( file )
   oo0OOO0OOoOO = len ( o0O00ooo0 ) / float ( oOOOO ) * 100
   o0oO0 . update ( int ( oo0OOO0OOoOO ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oOoO = os . path . join ( iIi1 , file )
   if not 'temp' in O00oOOO0 :
    if not 'plugin.program.originwizard' in O00oOOO0 :
     import time
     II1i1 = '01/01/1980'
     o0o0oo0OOo0O0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oOoO ) ) )
     if o0o0oo0OOo0O0 > II1i1 :
      IiIIIii1i1iI . write ( oOoO , oOoO [ OoOOoO0o : ] )
 IiIIIii1i1iI . close ( )
 o0oO0 . close ( )
 if 37 - 37: ooo0O * I1ii11iIi11i
 if 11 - 11: OOOo00oo0oO
def Oo0O0o00o00 ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 if 90 - 90: O0Oooo0O . IIiIiII11i . oOoO0o00OO0
 if 32 - 32: oOOoOooOo - oOo . iiiiiiii1 . iiiiiiii1 % ooOoO0O00 * i1iIi
def o0o0 ( ) :
 Oo0O00O0O ( )
 oo0 = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  Ii1I11I ( )
 if oOOOoo00 == 1 :
  IIiiIIi1 ( )
 if oOOOoo00 == 2 :
  I11i1iiiiIIIi ( )
 if oOOOoo00 == 3 :
  OooOo ( )
  if 13 - 13: o0o00Oo0O + O0Oooo0O * IIiIiII11i + I1ii11iIi11i * I11i1ii1
  if 12 - 12: I11i1ii1 - i1iIi % i1iIi
  if 23 - 23: oOOoOooOo
  if 61 - 61: I11i1ii1 + iiiiiiii1 - oOo * OOOo00oo0oO
  if 87 - 87: IIiIiII11i % IIiIiII11i
  if 51 - 51: oOOoOooOo * iI11I1II1I1I . iiiiiiii1
  if 25 - 25: OoOo0o - i1iIi . i1IiiiI1iI
  if 57 - 57: ooo0O + I1ii11iIi11i * oOoO0o00OO0 - oOOoOooOo % iI11I1II1I1I - i1iIi
  if 37 - 37: oOo * i1IiiiI1iI + i1iIi + oOoO0o00OO0 * ooo0O
def O00oOo0o0 ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  oo0 = [ '[COLOR' + iiI1IiI + ']RaysRavers Radio[/COLOR]' , '[COLOR' + iiI1IiI + ']ThunderStruck[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if oOOOoo00 == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if oOOOoo00 == 2 :
   Oo0O0oOoO0o0 ( )
  if oOOOoo00 == 3 :
   IiII111I ( )
  if oOOOoo00 == 4 :
   Oo0o0OoOoOo0 ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if oOOOoo00 == 5 :
   I11iiI11I1II ( )
  if oOOOoo00 == 6 :
   oO0iII1i111iI ( ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if oOOOoo00 == 7 :
   IiI1iI1 ( ( o0oOoO00o ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if oOOOoo00 == 8 :
   oOoo ( str ( O00OOOoOoo0O ) + ( o0oOoO00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if oOOOoo00 == 9 :
   i1IIII1II ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RaysRavers Radio[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , I1IIIii + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']ThunderStruck[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , I1IIIii + 'Thunder.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , I1IIIii + 'RadioNomy.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( O00OOOoOoo0O ) , 30031 , I1IIIii + 'MusicChannels.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , I1IIIii + 'UKRadio.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( O00OOOoOoo0O ) , 1013 , I1IIIii + 'WorldRadio.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CONCERTS' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , I1IIIii + 'Concerts.png' , Oo00OOOOO , '' )
   if 89 - 89: i1IiiiI1iI % iiiiiiii1 * I1ii11iIi11i / O0Oooo0O * I1ii11iIi11i / oOOoOooOo
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , I1IIIii + 'MusicVideos.png' , Oo00OOOOO , '' )
  if 14 - 14: ooOoO0O00 * iI11I1II1I1I - i1iIi * iii1i1iiiiIi - iiiiiiii1 / OOOo00oo0oO
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( O00OOOoOoo0O ) , 1111 , I1IIIii + 'MusicSearch.png' , Oo00OOOOO , '' )
  if 73 - 73: oOoO0o00OO0 - iii1i1iiiiIi * o0o00Oo0O - iii1i1iiiiIi - oOo
  if 96 - 96: oOoO0o00OO0 - o0o00Oo0O
 iIiIi11 ( 'movies' , 'MAIN' )
oOoO0OOooOoO = 'white'
i1II1I1Iii1 = 'gold'
def I1iO00O000oOO0oO ( ) :
 Oo0O00O0O ( )
 if oO0o00oo0 ( True ) == False : OO0 = 0
 else : OO0 = I1i1iiiI1 ( oO0o00oo0 ( True ) , True , True )
 if oO0o00oo0 ( True , True ) == False : i1Ii1II11 = 0
 else : i1Ii1II11 = I1i1iiiI1 ( oO0o00oo0 ( True , True ) , True , True )
 IiiIIii1I1I = int ( OO0 ) + int ( i1Ii1II11 )
 IIiIIiIi1II1IiI = str ( IiiIIii1I1I ) + ' Error(s) Found' if IiiIIii1I1I > 0 else 'None Found'
 oo0OoO = ': [COLORsteelblue]Not Found[/COLOR]' if not os . path . exists ( Oo0o0000o0o0 ) else ": [COLORorangered]%s[/COLOR]" % I11iIiiI ( os . path . getsize ( Oo0o0000o0o0 ) )
 OO000oo0o = I11iiIiI1II11 ( oO )
 OOOoOOOo = I11iiIiI1II11 ( i1iiIIiiI111 )
 oO0000 = OOOIIIIiiIi ( )
 ooooOOo = OO000oo0o + OOOoOOOo + oO0000
 oOOOOO0 = IIi1I1 ( )
 oO00o0oOoo = oOO ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAN UP:[COLORorangered] [B]%s[/B][/COLOR]' % I11iIiiI ( ooooOOo ) , 'url' , 9666 , I1IIIii + 'MAIN5.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , I1IIIii + 'KillKodi.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , I1IIIii + 'Speedtest.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG Errors:[COLORorangered] %s[/COLOR]' % ( IIiIIiIi1II1IiI ) , '' , 219999990 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR LOG FILES: [COLORorangered]' + oo0OoO + '[/COLOR]' , '' , 219999991 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE CACHE:[COLORorangered] [B]%s[/B][/COLOR]' % I11iIiiI ( oO0000 ) , 'url' , 14 , I1IIIii + 'DeleteCache.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE PACKAGES:[COLORorangered] [B]%s[/B][/COLOR]' % I11iIiiI ( OO000oo0o ) , 'url' , 6 , I1IIIii + 'DeletePackages.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , 'url' , 10 , I1IIIii + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']LAST RESORT FIX EMPTY REPOS[/COLOR]' , 'url' , 9 , I1IIIii + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR THUBMNAILS:[COLORorangered] [B]%s[/B][/COLOR]' % I11iIiiI ( OOOoOOOo ) , 'url' , 219999992 , I1IIIii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Local IP Address:[COLORorangered] ' + oOOOOO0 + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']External IP Address:[COLORorangered] ' + oO00o0oOoo + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 100 - 100: OoOo0o % Ii - oOo0O0Ooo * O0Oooo0O - ooo0O
 if 65 - 65: Ii - ii / o0o00Oo0O * I11i1ii1 % i1IiiiI1iI
 iIiIi11 ( 'movies' , 'MAIN' )
def o00o00 ( proc ) :
 xbmc . executebuiltin ( proc )
 if 72 - 72: ooOoO0O00
def I1Iii11111I1iii ( ) :
 o00o00 ( 'Container.Refresh()' )
def OO0Oo00 ( ) :
 OOOO0OOO = open ( Oo0o0000o0o0 , 'w' ) ; OOOO0OOO . close ( ) ; iII1ii1 ( "[COLOR %s]%s[/COLOR]" % ( oOoO0OOooOoO , oOo0oooo00o ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % i1II1I1Iii1 )
 I1Iii11111I1iii ( )
 if 28 - 28: oOo + O0Oooo0O / iii1i1iiiiIi % OOOo00oo0oO - I1ii11iIi11i
def ooOo0Ooo0 ( type = None ) :
 IIIiIii111IIi = oo0IiIIiIi11ii ( 'Textures' )
 if not type == None : oOOOoo00 = 1
 else : oOOOoo00 = iI111I11I1I1 . yesno ( oOo0oooo00o , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( i1II1I1Iii1 , IIIiIii111IIi ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if oOOOoo00 == 1 :
  try : II11IiIIiiiii ( os . join ( oooOOOOO , IIIiIii111IIi ) )
  except : oooOOo0o0OOO ( 'Failed to delete, Purging DB.' ) ; IiiiII ( IIIiIii111IIi )
  OoOo00OoOO00 ( i1iiIIiiI111 )
  if 62 - 62: iii1i1iiiiIi * ii * ooo0O
 else : oooOOo0o0OOO ( 'Clear thumbnames cancelled' )
 ii111Ii1i ( )
 if 46 - 46: ooOoO0O00 - iiiiiiii1 + O0Oooo0O + oOo + i1IiiiI1iI
 if 45 - 45: oOo0O0Ooo + i1IiiiI1iI + ooOoO0O00
def ii111Ii1i ( ) :
 if not os . path . exists ( i1iiIIiiI111 ) : os . makedirs ( i1iiIIiiI111 )
 i1II = '0123456789abcdef'
 OOOoooOo00O = os . path . join ( i1iiIIiiI111 , 'Video' , 'Bookmarks' )
 for Ii1II1I11i1 in i1II :
  iiIIiI1I = os . path . join ( i1iiIIiiI111 , Ii1II1I11i1 )
  if not os . path . exists ( iiIIiI1I ) : os . makedirs ( iiIIiI1I )
 if not os . path . exists ( OOOoooOo00O ) : os . makedirs ( OOOoooOo00O )
 if 67 - 67: oOoO0o00OO0 % ii
def oo0IiIIiIi11ii ( DB ) :
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
def OoOo00OoOO00 ( path ) :
 oooOOo0o0OOO ( "Deleting Folder: %s" % path , xbmc . LOGNOTICE )
 try : shutil . rmtree ( path , ignore_errors = True , onerror = None )
 except : return False
 if 29 - 29: oOoO0o00OO0
def IiiiII ( name ) :
 if 91 - 91: oOo
 if 54 - 54: oOoO0o00OO0 . oOOoOooOo + O0Oooo0O % oOOoOooOo
 if 67 - 67: oOo
 oooOOo0o0OOO ( 'Purging DB %s.' % name , xbmc . LOGNOTICE )
 if os . path . exists ( name ) :
  try :
   oOoo00 = database . connect ( name )
   O000 = oOoo00 . cursor ( )
  except Exception , o000O0O :
   oooOOo0o0OOO ( "DB Connection Error: %s" % str ( o000O0O ) , xbmc . LOGERROR )
   return False
 else : oooOOo0o0OOO ( '%s not found.' % name , xbmc . LOGERROR ) ; return False
 O000 . execute ( "SELECT name FROM sqlite_master WHERE type = 'table'" )
 for O0oooOo0000o0 in O000 . fetchall ( ) :
  if O0oooOo0000o0 [ 0 ] == 'version' :
   oooOOo0o0OOO ( 'Data from table `%s` skipped.' % O0oooOo0000o0 [ 0 ] , xbmc . LOGDEBUG )
  else :
   try :
    O000 . execute ( "DELETE FROM %s" % O0oooOo0000o0 [ 0 ] )
    oOoo00 . commit ( )
    oooOOo0o0OOO ( 'Data from table `%s` cleared.' % O0oooOo0000o0 [ 0 ] , xbmc . LOGDEBUG )
   except Exception , o000O0O : oooOOo0o0OOO ( "DB Remove Table `%s` Error: %s" % ( O0oooOo0000o0 [ 0 ] , str ( o000O0O ) ) , xbmc . LOGERROR )
 O000 . close ( )
 oooOOo0o0OOO ( '%s DB Purging Complete.' % name , xbmc . LOGNOTICE )
 IIiI = name . replace ( '\\' , '/' ) . split ( '/' )
 iII1ii1 ( "[COLOR %s]Purge Database[/COLOR]" % oOoO0OOooOoO , "[COLOR %s]%s Complete[/COLOR]" % ( i1II1I1Iii1 , IIiI [ len ( IIiI ) - 1 ] ) )
 if 95 - 95: OOOo00oo0oO
def II11IiIIiiiii ( path ) :
 oooOOo0o0OOO ( "Deleting File: %s" % path , xbmc . LOGNOTICE )
 try : os . remove ( path )
 except : return False
 if 80 - 80: I11i1ii1
 if 42 - 42: ii * IIiIiII11i
def OOOIIIIiiIi ( ) :
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
 ooooOOo = 0
 if 32 - 32: iiiiiiii1 . iI11I1II1I1I % I1ii11iIi11i . ii
 for Ii1II1I11i1 in i1I111II11 :
  if os . path . exists ( Ii1II1I11i1 ) and not Ii1II1I11i1 in [ I11 , O0oooOO ] :
   ooooOOo = I11iiIiI1II11 ( Ii1II1I11i1 , ooooOOo )
  else :
   for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( Ii1II1I11i1 ) :
    for OoOOoo0 in O00oOOO0 :
     if 'cache' in OoOOoo0 . lower ( ) and not OoOOoo0 . lower ( ) == 'meta_cache' : ooooOOo = I11iiIiI1II11 ( os . path . join ( Ooo00OoO0O00 , OoOOoo0 ) , ooooOOo )
     if 11 - 11: i1IiiiI1iI
 return ooooOOo
def I11iiIiI1II11 ( path , total = 0 ) :
 for IioooooOOo0Oo , IiiiiiiI111i , Oooooooo00o00 in os . walk ( path ) :
  for OOOO0OOO in Oooooooo00o00 :
   iiIIIIiI11II1 = os . path . join ( IioooooOOo0Oo , OOOO0OOO )
   total += os . path . getsize ( iiIIIIiI11II1 )
 return total
def I11iIiiI ( num , suffix = 'B' ) :
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
def oOo00Oo0o0Oo ( ) :
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
 oo0 = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  oooO ( )
 if oOOOoo00 == 0 :
  oo0OOoOo0 ( IIo0o0O0O00oOOo )
 if oOOOoo00 == 0 :
  oO00oO0 ( IIo0o0O0O00oOOo )
  if 80 - 80: iiiiiiii1 . o0o00Oo0O
  if 25 - 25: iiiiiiii1 / iI11I1II1I1I + oOo0O0Ooo / oOOoOooOo
  if 61 - 61: OOOo00oo0oO % oOoO0o00OO0 * i1IiiiI1iI . i1IiiiI1iI
 iIiIi11 ( 'movies' , 'MAIN' )
 if 20 - 20: i1iIi / iiiiiiii1 + IIiIiII11i . Ii . OoOo0o
def o0oOOO0 ( ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 iI111i = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for I1i , O000OOO in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , I1i , I1i , '' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 11 - 11: i1IiiiI1iI / iii1i1iiiiIi
def ii1IIi1IIIIi1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( iI1i1iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , i1i1II1i11 , iI1iIii11Ii , II1 )
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
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 85 - 85: ooOoO0O00 . ooOoO0O00
def Ii11i1I1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OOI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 59 - 59: ii * ooo0O / O0Oooo0O
def oOooOOoo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iIOoo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 21 - 21: iiiiiiii1 % I11i1ii1 % I1ii11iIi11i % o0o00Oo0O
def OoOoooOO00OO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 76 - 76: oOoO0o00OO0 + OoOo0o % o0o00Oo0O * Ii . o0o00Oo0O . Ii
def oo0OOoOo0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i11iII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 40 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 75 - 75: OoOo0o / Ii / iI11I1II1I1I
def i11iI1111ii1I ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OoOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 22 - 22: Ii + iii1i1iiiiIi + ii
def OoOo00o0O00 ( ) :
 oo0 = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  I1111ii11 ( )
 if oOOOoo00 == 1 :
  I1iI1I1111i ( )
 if oOOOoo00 == 2 :
  iII11IiIIII ( )
  if 99 - 99: OoOo0o . OoOo0o * oOOoOooOo + IIiIiII11i . iI11I1II1I1I
  if 93 - 93: ooo0O + I11i1ii1 % O0Oooo0O + oOOoOooOo
  if 15 - 15: i1IiiiI1iI - oOoO0o00OO0 * oOOoOooOo
  if 80 - 80: iiiiiiii1 + oOOoOooOo * ooo0O - IIiIiII11i - oOoO0o00OO0
def I1iI1I1111i ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 iI111i = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O0Oo0O0O0o in iI111i :
  o0OO ( 'Android Apps' + O0Oo0O0O0o , 'https://www.apkfiles.com' + IIo0o0O0O00oOOo , 30035 , I1IIIii + 'apps.png' )
 for IIo0o0O0O00oOOo , O0Oo0O0O0o in IIi11i1i1iI1 :
  o0OO ( 'Android Games' + O0Oo0O0O0o , 'https://www.apkfiles.com' + IIo0o0O0O00oOOo , 30035 , I1IIIii + 'GAMES.png' )
 iIiIi11 ( 'movies' , 'MAIN' )
def iiII11ii1Ii ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  if '/cat' in url :
   o0OO ( ( O000OOO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def iiI1Ii1iiii1i ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  if '/app' in url :
   o0OO ( ( O000OOO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def III1iIi ( url ) :
 I111i1II = i11111IIIII ( url )
 o0OOOOOo0 = url
 if "page=" in str ( url ) :
  o0OOOOOo0 = url . split ( '?' ) [ 0 ]
 iI111i = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( I111i1II )
 for url , I1i , O000OOO in iI111i :
  if 'apk' in url :
   O0O0ooOOO ( ( O000OOO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + I1i )
 if len ( IIi11i1i1iI1 ) > 1 :
  IIi11i1i1iI1 = str ( IIi11i1i1iI1 [ len ( IIi11i1i1iI1 ) - 1 ] )
 O0O0ooOOO ( 'Next Page' , o0OOOOOo0 + str ( IIi11i1i1iI1 ) , 30037 , I1IIIii + 'Next.png' )
def IIiIiii ( name , url ) :
 I111i1II = o0Ooo0O00 ( url )
 name = name
 iI111i = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I111i1II )
 for url in iI111i :
  url = 'https://www.apkfiles.com' + url
  OOo0OO ( name , url , 'Brackets' )
def iII11IiIIII ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'https://www.apkfiles.com/search?q=' + ( oOoooO00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 III1iIi ( ooO0000o00O )
 if 98 - 98: Ii . O0Oooo0O + iii1i1iiiiIi
def o00O0o0oo0 ( url ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( ooo000 , 'Download' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , O000OOO + '.apk' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 45 - 45: OoOo0o + O0Oooo0O + Ii - oOoO0o00OO0
def ooooooo0oOo0 ( url ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , O000OOO + '.mp4' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 81 - 81: Ii % oOo0O0Ooo / iiiiiiii1 % oOo / O0Oooo0O % iI11I1II1I1I
 if 14 - 14: oOoO0o00OO0 * I1ii11iIi11i + Ii % OoOo0o - OOOo00oo0oO
def iIIii ( name , url , description ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , name )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 o000oo = xbmc . translatePath ( os . path . join ( I1i1iiI1 ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o000oo
 print '======================================='
 extract . all ( Iiii1iI1i , o000oo , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 58 - 58: oOOoOooOo + IIiIiII11i + i1iIi . ii
 if 42 - 42: iI11I1II1I1I / i1IiiiI1iI . o0o00Oo0O . i1iIi
 if 12 - 12: Ii - iI11I1II1I1I * I11i1ii1 * iiiiiiii1
 if 19 - 19: o0o00Oo0O + OOOo00oo0oO + ooo0O
 if 81 - 81: iI11I1II1I1I
def I1111ii11 ( ) :
 IIIi1I1IIii1II = i11111IIIII ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iI111i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , IIo0o0O0O00oOOo , o0o0OO0o00o0O , iI1iIii11Ii , OOO00OiI in iI111i :
  O0O0ooOOO ( O000OOO , IIo0o0O0O00oOOo , 80003 , o0o0OO0o00o0O , I1IIIii + 'APKToolsB.png' , OOO00OiI )
def O0 ( apk , ret = None ) :
 if apk == "kodi" :
  o00oO00O0 = "https://kodi.tv/download/"
  IIIi1I1IIii1II = i11111IIIII ( o00oO00O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iI111i = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( IIIi1I1IIii1II )
  if len ( iI111i ) == 1 :
   I1Iii = iI111i [ 0 ] [ 0 ]
   iIi11 = iI111i [ 0 ] [ 1 ]
   IIIi1iIii1II11 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( I1Iii , iIi11 )
  if ret == 'version' : return I1Iii
  else : return IIIi1iIii1II11
 elif apk == "spmc" :
  OOOOoOOOO = 'https://github.com/koying/SPMC/releases/latest/'
  IIIi1I1IIii1II = i11111IIIII ( OOOOoOOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iI111i = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( IIIi1I1IIii1II )
  I1Iii = re . sub ( '<[^<]+?>' , '' , iI111i [ 0 ] ) . replace ( ' ' , '' )
  IIIi1iIii1II11 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( I1Iii , I1Iii )
  if ret == 'version' : return I1Iii
  else : return IIIi1iIii1II11
def OOo0OO ( name , url , Brackets ) :
 if oOOo0O00o ( ) == 'android' :
  iiIi1 = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not iiIi1 : iII1ii1 ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  Oo0OOoI1i1i1IIi1I = name
  if iiIi1 :
   if not os . path . exists ( oO ) : os . makedirs ( oO )
   if not Ii1iI111 ( url ) == True : iII1ii1 ( oOo0oooo00o , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % Oo0OOoI1i1i1IIi1I , '' , 'Please Wait' )
   Iiii1iI1i = os . path . join ( oO , "%s.apk" % name )
   try : os . remove ( Iiii1iI1i )
   except : pass
   downloader . download ( url , Iiii1iI1i , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   if "Brackets" in Brackets :
    Ii1o0OOOoo0000 = zipfile . ZipFile ( Iiii1iI1i )
    for file in Ii1o0OOOoo0000 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oO , os . path . basename ( file ) ) , 'wb' ) as OOOO0OOO :
       IIi11iIIiIiI = file . split ( '/' ) [ 1 ]
       OOOO0OOO . write ( Ii1o0OOOoo0000 . read ( file ) )
       xbmc . sleep ( 500 )
       OOOO0OOO . close ( )
       try :
        os . remove ( Iiii1iI1i )
       except :
        pass
       Iiii1iI1i = os . path . join ( oO , IIi11iIIiIiI )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Iiii1iI1i + '")' )
  else : iII1ii1 ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iII1ii1 ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 54 - 54: OOOo00oo0oO
 if 26 - 26: oOOoOooOo % ii . O0Oooo0O * oOOoOooOo + IIiIiII11i - oOoO0o00OO0
 if 20 - 20: oOo
 if 99 - 99: I1ii11iIi11i + ii . iiiiiiii1 + o0o00Oo0O
def oo000o0O ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( IIIi1I1IIii1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIo0o0O0O00oOOo = ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + IIo0o0O0O00oOOo )
  iiIiIIiI1 ( ( O000OOO ) . replace ( '_' , ' ' ) , IIo0o0O0O00oOOo )
  if 16 - 16: ooOoO0O00 / iiiiiiii1 % OOOo00oo0oO / oOOoOooOo
def iiIiIIiI1 ( name , url ) :
 if oOOo0O00o ( ) == 'android' :
  iiIi1 = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not iiIi1 : iII1ii1 ( oOo0oooo00o , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  Oo0OOoI1i1i1IIi1I = name
  if iiIi1 :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not Ii1iI111 ( url ) == True : iII1ii1 ( oOo0oooo00o , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % Oo0OOoI1i1i1IIi1I , '' , 'Please Wait' )
   Iiii1iI1i = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( Iiii1iI1i )
   except : pass
   downloader . download ( url , Iiii1iI1i , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Iiii1iI1i + '")' )
  else : iII1ii1 ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iII1ii1 ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 10 - 10: IIiIiII11i * o0o00Oo0O + ooOoO0O00 * ii + ii
 if 23 - 23: ooOoO0O00
def IIiii1I1I ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'INFO' )
 if 62 - 62: IIiIiII11i - iii1i1iiiiIi * i1iIi
 if 53 - 53: OOOo00oo0oO + iiiiiiii1
def iIi1IiII ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 30015 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 61 - 61: OOOo00oo0oO % I1ii11iIi11i % i1iIi
def iiiiII ( url , iconimage , fanart ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 I111iIIII11iI = url
 I1i = iconimage
 fanart = fanart
 iI111i = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for O0Ooo , O000OOO in iI111i :
  if '.mp4' in O000OOO :
   O0O0ooOOO ( 'Watch VIDEO' , url + '/' + O0Ooo , 222 , I1i , fanart , '' )
  if 'description' in O000OOO :
   O0O0ooOOO ( 'Read Description' , url + '/' + O0Ooo , 30017 , I1i , fanart , '' )
  if 'images' in O000OOO :
   o00oOOooOOo0o ( 'View Images' , url + '/' + O0Ooo , 30018 , I1i , fanart , '' )
  if 'url' in O000OOO :
   O0O0ooOOO ( 'Install Build On Android' , url + '/' + O0Ooo , 30016 , I1i , fanart , '' )
  if 'url' in O000OOO :
   O0O0ooOOO ( 'Install Build On Pc' , url + '/' + O0Ooo , 30019 , I1i , fanart , '' )
 iIiIi11 ( 'movies' , 'INFO' )
 if 3 - 3: OoOo0o / iiiiiiii1 + oOo0O0Ooo + iii1i1iiiiIi + O0Oooo0O % o0o00Oo0O
def i1Ii1I ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in iI111i :
  O0O0o0o0oo0O ( url )
  if 30 - 30: O0Oooo0O / oOo0O0Ooo / ooOoO0O00 - o0o00Oo0O . i1iIi - oOOoOooOo
def o00o0o0o ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in iI111i :
  IiI1 ( url )
  if 73 - 73: O0Oooo0O
def i1IiIiiiii11 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'desc="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O0o00 in iI111i :
  OoOoO ( 'Description:' , O0o00 )
  if 58 - 58: ii / iI11I1II1I1I
def IiIiI11IIII ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 url = url
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for O0Ooo , O000OOO in iI111i :
  if 'png' in O000OOO :
   O0O0ooOOO ( 'image' , '' , '' , url + '/' + O0Ooo , url + '/' + O0Ooo , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 97 - 97: OOOo00oo0oO + i1IiiiI1iI % ooo0O % ooo0O + iiiiiiii1 + ooOoO0O00
def oOOOOiI ( name , url , description ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , name + '.zip' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1ii1ii11i1I
 print '======================================='
 extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0O0Oo00 ( )
 if 64 - 64: I11i1ii1
 if 80 - 80: oOo0O0Ooo - Ii / oOo / iii1i1iiiiIi + iii1i1iiiiIi
def IiI1 ( url ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1ii1ii11i1I
 print '======================================='
 extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
 o0OoOO ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oo000oiIIIII ( )
 if 48 - 48: iii1i1iiiiIi * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def O0O0o0o0oo0O ( url ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1ii1ii11i1I
 print '======================================='
 extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
 o0OoOO ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oo000oiIIIII ( )
 if 22 - 22: oOo . iii1i1iiiiIi % IIiIiII11i - o0o00Oo0O
def oO0o00O ( name , url , description ) :
 I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 Iiii1iI1i = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oO0 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print I1ii1ii11i1I
 print '======================================='
 extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oo000oiIIIII ( )
 if 7 - 7: I1ii11iIi11i * oOo - IIiIiII11i % O0Oooo0O . I1ii11iIi11i . I1ii11iIi11i
def oOOo0O00o ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def oO00O0 ( log ) :
 xbmc . log ( "[%s]: %s" % ( oOo0oooo00o , log ) )
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : OOOO0OOO = open ( Oo0o0000o0o0 , 'w' ) ; OOOO0OOO . close ( )
 with open ( Oo0o0000o0o0 , 'a' ) as OOOO0OOO :
  iiII1iIi1ii1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOOO0OOO . write ( iiII1iIi1ii1i . rstrip ( '\r\n' ) + '\n' )
def oooOOo0o0OOO ( msg , level = xbmc . LOGDEBUG ) :
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : OOOO0OOO = open ( Oo0o0000o0o0 , 'w' ) ; OOOO0OOO . close ( )
 if WIZDEBUGGING == 'false' : return False
 if DEBUGLEVEL == '0' : return False
 if DEBUGLEVEL == '1' and not level in [ xbmc . LOGNOTICE , xbmc . LOGERROR , xbmc . LOGSEVERE , xbmc . LOGFATAL ] : return False
 if DEBUGLEVEL == '2' : level = xbmc . LOGNOTICE
 try :
  if isinstance ( msg , unicode ) :
   msg = '%s' % ( msg . encode ( 'utf-8' ) )
  xbmc . log ( '%s: %s' % ( oOo0oooo00o , msg ) , level )
 except Exception as o000O0O :
  try : xbmc . log ( 'Logging Failure: %s' % ( o000O0O ) , level )
  except : pass
 if ENABLEWIZLOG == 'true' :
  i11IiI1 = getS ( 'nextcleandate' ) if not getS ( 'nextcleandate' ) == '' else str ( TODAY )
  if CLEANWIZLOG == 'true' and i11IiI1 <= str ( TODAY ) : checkLog ( )
  with open ( Oo0o0000o0o0 , 'a' ) as OOOO0OOO :
   iiII1iIi1ii1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , msg )
   OOOO0OOO . write ( iiII1iIi1ii1i . rstrip ( '\r\n' ) + '\n' )
def oo000oiIIIII ( ) :
 oOOOoo00 = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oOOOoo00 == 0 : return
 elif oOOOoo00 == 1 : pass
 o0O0oo0OO0O = oOOo0O00o ( )
 oO00O0 ( "Platform: " + str ( o0O0oo0OO0O ) )
 os . _exit ( 1 )
 oO00O0 ( "Force close failed!  Trying alternate methods." )
 if o0O0oo0OO0O == 'osx' :
  oO00O0 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o0O0oo0OO0O == 'linux' :
  oO00O0 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o0O0oo0OO0O == 'android' :
  oO00O0 ( "############ try android force close #################" )
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
 elif o0O0oo0OO0O == 'windows' :
  oO00O0 ( "############ try windows force close #################" )
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
  oO00O0 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  oO00O0 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 62 - 62: oOOoOooOo * oOoO0o00OO0 / iiiiiiii1 * OoOo0o / OoOo0o - iiiiiiii1
  if 59 - 59: i1iIi % iiiiiiii1 / IIiIiII11i + oOo0O0Ooo * oOOoOooOo
  if 100 - 100: oOoO0o00OO0
def oO00oO0 ( url ) :
 o0oO0 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( url ) :
  for file in Iiiiii :
   if file . endswith ( ".xml" ) :
    o0oO0 . update ( 0 , "Fixing" , file , 'Please Wait' )
    iiI11Iii = open ( ( os . path . join ( Ooo00OoO0O00 , file ) ) ) . read ( )
    oO0o0OooOO0 = iiI11Iii . replace ( i1111 , 'special://home/' )
    OOOO0OOO = open ( ( os . path . join ( Ooo00OoO0O00 , file ) ) , mode = 'w' )
    OOOO0OOO . write ( str ( oO0o0OooOO0 ) )
    OOOO0OOO . close ( )
 oo000oiIIIII ( )
 if 42 - 42: ii . iii1i1iiiiIi
def Oo0O0oOoO0o0 ( ) :
 o0OO ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , I1IIIii + 'RadioNomy.png' )
 o0OO ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , I1IIIii + 'RadioNomy.png' )
 o0OO ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , I1IIIii + 'RadioNomy.png' )
 if 93 - 93: oOo0O0Ooo
def ooOo0oo0O0O ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def IIiii ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def i1Ii11I1i ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I111i1II )
 for url , O000OOO in IIi11i1i1iI1 :
  o0OO ( ( '[COLOR' + iiI1IiI + ']Filter - ' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
 for url , I1i , O000OOO in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']Stream - ' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , I1i )
def iI11IIi1iiI1I ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I111i1II )
 for url in iI111i :
  OOIi1iI111II1I1 ( url )
def oO0oO0ooOoO0 ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O
 Ii1I11IIi1 = 'https://www.radionomy.com/en/search/index?query=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 oOOo0 = i11111IIIII ( Ii1I11IIi1 )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']Stream - ' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + IIo0o0O0O00oOOo , 70005 , I1i )
  if 41 - 41: oOOoOooOo / oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . oOoO0o00OO0
  if 12 - 12: oOo
def I11iiI11I1II ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.listenlive.eu/' + IIo0o0O0O00oOOo , 10111113 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def Oo0o0OoOoOo0 ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 if 15 - 15: i1iIi
 if 69 - 69: oOo % OOOo00oo0oO . oOoO0o00OO0 * oOoO0o00OO0
 iI111i = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , oooooo0 , url , iII1iii in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' [COLORorangered] ' + iII1iii + '[/COLOR]' , url , 222225 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , '[COLOR' + iiI1IiI + ']' + O000OOO + '[CR]' + oooooo0 + '[CR]' + iII1iii + '[/COLOR]' )
  if 97 - 97: O0Oooo0O / OoOo0o - Ii
def OO0o0o ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.toonjet.com/' + IIo0o0O0O00oOOo , 8051 , I1IIIii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0O0O00OoO0O ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( I111i1II )
 for url , I1i in iI111i :
  if 'ol.gif' in I1i :
   pass
  elif 'link_block_' in I1i :
   pass
  elif '.png' in I1i :
   pass
  else :
   o0OO ( ( I1i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , I1IIIii + 'vod.png' )
 for url in IIi11i1i1iI1 :
  o0OO ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , I1IIIii + 'Next.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1II11III ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I111i1II )
 for url in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , I1IIIii + 'classictoons.png' )
  if 95 - 95: i1IiiiI1iI + ooo0O - Ii % oOo / OOOo00oo0oO
  if 80 - 80: O0Oooo0O * OOOo00oo0oO * ooOoO0O00
def IiIii1i ( ) :
 Iii1i ( 'Audio Books' , '' , 30011 , I1IIIii + 'AudioBooks.png' , I1IIIii + 'AudioBooks.png' , '' )
 Iii1i ( 'Kids Audio Books' , '' , 30006 , I1IIIii + 'KidsAudioBooks.png' , I1IIIii + 'KidsAudioBooks.png' , '' )
 if 27 - 27: oOOoOooOo . I1ii11iIi11i + oOOoOooOo + iiiiiiii1
def III11IiI ( ) :
 Iii1i ( 'All' , '' , 30001 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 Iii1i ( 'Popular' , '' , 30012 , I1IIIii + 'POPULARv.png' , I1IIIii + 'POPULARv.png' , '' )
 Iii1i ( 'Search' , '' , 30013 , I1IIIii + 'Search.png' , I1IIIii + 'Search.png' , '' )
 if 6 - 6: OoOo0o / iI11I1II1I1I / oOOoOooOo / oOo0O0Ooo - ooOoO0O00 - OoOo0o
def Iii1iI1I1iii1 ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for O000OOO , IIo0o0O0O00oOOo , Ii111ii1 in iI111i :
  if 'Parent' in O000OOO :
   pass
  elif '2' in Ii111ii1 :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + i1iIi % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def oo000O ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for O000OOO , IIo0o0O0O00oOOo , Ii111ii1 in iI111i :
  if oOoooO00O in O000OOO . lower ( ) :
   if '1' in Ii111ii1 :
    Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '2' in Ii111ii1 :
    Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '3' in Ii111ii1 :
    Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 97 - 97: ii * ooo0O + ii % i1iIi * I1ii11iIi11i
    if 35 - 35: iI11I1II1I1I % iiiiiiii1 - ooOoO0O00
def I1i1iI1I1II ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for O000OOO , IIo0o0O0O00oOOo , Ii111ii1 in iI111i :
  if '1' in Ii111ii1 :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 3010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '2' in Ii111ii1 :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '3' in Ii111ii1 :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 20 - 20: iii1i1iiiiIi
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: O0Oooo0O * oOo - iiiiiiii1
def O0OoO0 ( url ) :
 O0Ooo = url
 oOOo0 = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOOo0 )
 for url , O000OOO in IIi11i1i1iI1 :
  if 'mp3' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0Ooo + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0Ooo + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0Ooo + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '/' in O000OOO :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0Ooo + url , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 73 - 73: Ii - oOo0O0Ooo * oOo0O0Ooo
   if 83 - 83: o0o00Oo0O * oOo0O0Ooo
   if 97 - 97: IIiIiII11i
def iIiIii ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0Ooo = url
 iI111i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if 'Parent' in O000OOO :
   pass
  elif '.db' in O000OOO :
   pass
  elif '.jpg' in O000OOO :
   pass
  elif '.html' in O000OOO :
   pass
  elif '.doc' in O000OOO :
   pass
  elif 'mp3' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0Ooo + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0Ooo + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0Ooo + url , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: oOOoOooOo
   if 33 - 33: O0Oooo0O * I11i1ii1 - o0o00Oo0O + oOo0O0Ooo / I11i1ii1
def iii1II11II1 ( ) :
 Iii1i ( 'A-Z' , '' , 30007 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 Iii1i ( 'All' , '' , 30003 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 Iii1i ( 'Search' , '' , 30014 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 if 30 - 30: I11i1ii1 / Ii % oOo * OoOo0o
def i1oOOOoOO ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i in iI111i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + IIo0o0O0O00oOOo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in I1i :
   pass
  else :
   Iii1i ( I1i , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( IIo0o0O0O00oOOo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + I1i + '.gif' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 80 - 80: ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: OOOo00oo0oO * ooOoO0O00 . ii % oOOoOooOo
 if 87 - 87: Ii * IIiIiII11i - i1iIi % ii
def o0oO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if '</a>' in O000OOO :
   pass
  elif '(' in O000OOO :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: O0Oooo0O - ooOoO0O00 / I11i1ii1
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: iii1i1iiiiIi - oOo * ii
def iIi1i111ii1II11ii ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if oOoooO00O in O000OOO . lower ( ) :
   if '</a>' in O000OOO :
    pass
   elif '(' in O000OOO :
    Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   else :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 21 - 21: i1IiiiI1iI
    if 79 - 79: oOo / OoOo0o - ooOoO0O00 + ooOoO0O00 - I11i1ii1 + I11i1ii1
def oOoOo000Ooooo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if '</a>' in O000OOO :
   pass
  elif '(' in O000OOO :
   Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 18 - 18: i1iIi + iii1i1iiiiIi . ooOoO0O00 / I11i1ii1 / iiiiiiii1
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 97 - 97: oOo + iI11I1II1I1I
 if 79 - 79: oOOoOooOo + OOOo00oo0oO - IIiIiII11i . I1ii11iIi11i
def iIiIi1i1ii11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oOOo0 )
 for url in iI111i :
  O0Ooo = ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( O0Ooo )
  if 86 - 86: O0Oooo0O * oOOoOooOo - oOOoOooOo . oOo0O0Ooo
def Ooooo0o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  if '<p align' in O000OOO :
   pass
  elif '&nbsp;' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 59 - 59: oOOoOooOo % I1ii11iIi11i - OOOo00oo0oO + I11i1ii1
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: i1iIi + iii1i1iiiiIi - oOoO0o00OO0 + iI11I1II1I1I % ooOoO0O00 * I11i1ii1
 if 21 - 21: o0o00Oo0O * oOOoOooOo % oOo
def Iii1I11i1IiiI ( ) :
 oOOo0 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 iI111i = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'ongoing' in IIo0o0O0O00oOOo :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 21005 , I1IIIii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in IIo0o0O0O00oOOo :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 21005 , I1IIIii + 'CartoonShows.png' , '' , '' )
  if 'disney' in IIo0o0O0O00oOOo :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 21005 , I1IIIii + 'Disney.png' , '' , '' )
  if 'genre' in IIo0o0O0O00oOOo :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 21005 , I1IIIii + 'Genre.png' , '' , '' )
  if 'years' in IIo0o0O0O00oOOo :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 21005 , I1IIIii + 'Years.png' , '' , '' )
def OOoo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 O0oooO00ooO0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , I1i , I1i , O000OOO )
 for url , O000OOO in O0oooO00ooO0 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in next :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , I1IIIii + 'Next.png' , '' , '' )
def OO000oOoOo000 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 o0000o0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 o0O0o0ooo0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oOOo0 )
 iIo0O000O00o = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in o0O0o0ooo0 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url , O000OOO in o0000o0Oo :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
def iiooo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
  if 42 - 42: ii % i1IiiiI1iI % I11i1ii1
def O0OoO0OOo ( ) :
 oOOo0 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 iI111i = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if '9cart' in IIo0o0O0O00oOOo :
   o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 20001 , I1IIIii + 'ORIGINCARTOON.png' )
   if 45 - 45: oOo * oOo0O0Ooo
def O0oo0OoO0oo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oOOo0 )
 OoOOo0OOoO = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if '9cart' in url :
   o0OO ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url in IIi11i1i1iI1 :
  if '9cart' in url :
   o0OO ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url , O000OOO in OoOOo0OOoO :
  if '9cart' in url :
   o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
   if 74 - 74: oOoO0o00OO0 * OOOo00oo0oO + iiiiiiii1 % o0o00Oo0O
def Iii1IiIiIii ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , url , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 20003 , I1i )
 for url , O000OOO in IIi11i1i1iI1 :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
  if 55 - 55: iii1i1iiiiIi . iI11I1II1I1I * OoOo0o % iI11I1II1I1I . oOo
def I1IIiiiIi1ii11I ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)">' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'Watch' in url :
   o0OO ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , I1IIIii + 'ORIGINCARTOON.png' )
   if 9 - 9: o0o00Oo0O * i1iIi
def o0O00o00Ooo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 20005 , I1IIIii + 'ORIGINCARTOON.png' )
  if 16 - 16: OoOo0o . IIiIiII11i - i1iIi - ii
def ooOoOoOoo ( url ) :
 url = cloudflare . source ( url )
 O00o0o ( url )
 if 25 - 25: I1ii11iIi11i + ooo0O - oOo
def oooI11Ii1 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . recompile ( 'src="([^"]*)"' )
 for url in iI111i :
  O00o0o ( url )
  if 63 - 63: ooOoO0O00
  if 42 - 42: OOOo00oo0oO - Ii % OOOo00oo0oO - O0Oooo0O * o0o00Oo0O / IIiIiII11i
def i1iIIi ( url , name ) :
 url = url ; name = name
 oo0O0OO0Oooo = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oo0O0OO0Oooo . clear ( )
 IiiI11Iii = [ ]
 I1Iii1 = [ ]
 oO00oOOo0Oo = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oO00oOOo0Oo )
 for I1i in IIi11i1i1iI1 :
  Ii1II111iIi = I1i
 OoOOo0OOoO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oO00oOOo0Oo )
 for oo00ooOOoo , O000OOOo in OoOOo0OOoO :
  IiiI11Iii . append ( [ oo00ooOOoo , O000OOOo ] )
  if len ( IiiI11Iii ) == len ( OoOOo0OOoO ) :
   for Ii1II1I11i1 in IiiI11Iii :
    oO0o0o0o0o0o0 = random . randint ( 1 , len ( IiiI11Iii ) )
    try :
     Ii1Ii = IiiI11Iii [ int ( oO0o0o0o0o0o0 ) ]
     if Ii1Ii [ 1 ] not in I1Iii1 :
      I1Iii1 . append ( Ii1Ii [ 1 ] )
      OO0oo0O0OOO0 = i11111IIIII ( Ii1Ii [ 0 ] )
      ooO0O00Oo0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OO0oo0O0OOO0 )
      for iII , OOoOOooO in ooO0O00Oo0o :
       if 'easy' in OOoOOooO :
        i1111II1iIII = i11111IIIII ( OOoOOooO )
        OOO = re . compile ( 'file: "(.+?)"' ) . findall ( i1111II1iIII )
        for I1ii11ii1iiI in OOO :
         if 'http' in I1ii11ii1iiI :
          o0OoOo00ooO = xbmcgui . ListItem ( Ii1Ii [ 1 ] , iconImage = Ii1II111iIi , thumbnailImage = Ii1II111iIi )
          o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : Ii1Ii [ 1 ] } )
          o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
          oo0O0OO0Oooo . add ( I1ii11ii1iiI , o0OoOo00ooO )
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
   if 93 - 93: iii1i1iiiiIi + i1IiiiI1iI
def ii1IiIiI1iiii ( url ) :
 oo0O0OO0Oooo = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oo0O0OO0Oooo . clear ( )
 IiIiII1I1Ii = [ ]
 OOoOOOo00 = [ ]
 oO00O0OO = [ ]
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  OOoOOOo00 . append ( [ url , O000OOO ] )
  if len ( OOoOOOo00 ) == len ( iI111i ) :
   for Ii1II1I11i1 in OOoOOOo00 :
    ii1ii1iii1I = random . randint ( 1 , len ( OOoOOOo00 ) )
    try :
     ii1iiIi1iii1 = OOoOOOo00 [ int ( ii1ii1iii1I ) ]
    except :
     pass
    if ii1iiIi1iii1 [ 1 ] not in oO00O0OO :
     oO00O0OO . append ( ii1iiIi1iii1 [ 1 ] )
     if int ( len ( IiIiII1I1Ii ) ) < 1 :
      IiIiII1I1Ii . append ( ii1iiIi1iii1 [ 1 ] [ 0 ] )
      i1iIIi ( ii1iiIi1iii1 [ 0 ] , ii1iiIi1iii1 [ 1 ] )
     else :
      pass
    else :
     pass
  else :
   pass
   if 36 - 36: ii - iii1i1iiiiIi - oOo * O0Oooo0O - OOOo00oo0oO
def O0ooOOOo000OOoOO ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
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
 if 13 - 13: I1ii11iIi11i
def oO0OooO00Oo ( ) :
 oO0OO00O0 = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 I111i1II = i11111IIIII ( oO0OO00O0 )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  O0ooOOOo000OOoOO ( O000OOO , 9110012 , url = IIo0o0O0O00oOOo , image = O0O , isFolder = False )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 65 - 65: OoOo0o % I11i1ii1 % ooo0O . i1iIi . oOoO0o00OO0
def iii11i1 ( ) :
 oO0OO00O0 = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , '' , 10004 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 iiIi1iI1iIii ( '[COLOR' + iiI1IiI + ']24/7 Select Cartoon[/COLOR]' , '' , 9110011 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' , '' )
 O0ooOOOo000OOoOO ( '[COLOR' + iiI1IiI + ']24/7 Random Cartoon[/COLOR]' , 9110010 , url = oO0OO00O0 , image = I1IIIii + 'Kids.png' , isFolder = False )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 if 64 - 64: oOoO0o00OO0 . i1iIi / oOoO0o00OO0 * i1iIi
def I11i1iiiiIIIi ( ) :
 oO0OO00O0 = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 oOOo0 = i11111IIIII ( oO0OO00O0 )
 if 86 - 86: iI11I1II1I1I * iiiiiiii1 * i1iIi / oOo % oOOoOooOo - o0o00Oo0O
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oOOo0 )
 if 63 - 63: oOoO0o00OO0
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if oOoooO00O in O000OOO . lower ( ) :
   if 'Dad!' in O000OOO :
    pass
   elif 'Family Guy' in O000OOO :
    pass
   elif '2 Stupid' in O000OOO :
    pass
   elif 'The Zelfs' in O000OOO :
    pass
   elif 'A Clone' in O000OOO :
    pass
   elif 'A.T.O.M' in O000OOO :
    pass
   elif 'Almost Naked' in O000OOO :
    pass
   elif 'Angry Kid' in O000OOO :
    pass
   elif 'Annoying Orange' in O000OOO :
    pass
   elif 'Aqua Teen' in O000OOO :
    pass
   elif 'Assy Mcgee' in O000OOO :
    pass
   elif 'Astroblast' in O000OOO :
    pass
   elif 'Atomic Betty' in O000OOO :
    pass
   elif 'Axe Cop' in O000OOO :
    pass
   elif 'Baby Playpen' in O000OOO :
    pass
   elif 'Beavis and Butt' in O000OOO :
    pass
   elif 'Celebrity Deathmatch' in O000OOO :
    pass
   elif 'Clerks The' in O000OOO :
    pass
   elif 'Crapston Villas' in O000OOO :
    pass
   elif 'Duckman:' in O000OOO :
    pass
   elif 'Stripperella' in O000OOO :
    pass
   elif 'Vixen' in O000OOO :
    pass
   else :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 10006 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
    if 16 - 16: oOo + OOOo00oo0oO * ooOoO0O00 / oOoO0o00OO0
    if 100 - 100: oOo0O0Ooo - OoOo0o
    if 91 - 91: ooo0O * oOoO0o00OO0 - iiiiiiii1 . IIiIiII11i
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 1 - 1: OoOo0o + O0Oooo0O * oOoO0o00OO0
def i1I1IiIiIII ( url ) :
 oO0OO00O0 = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 I111i1II = i11111IIIII ( oO0OO00O0 )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  if 'Dad!' in O000OOO :
   pass
  elif 'Family Guy' in O000OOO :
   pass
  elif '2 Stupid' in O000OOO :
   pass
  elif 'The Zelfs' in O000OOO :
   pass
  elif 'A Clone' in O000OOO :
   pass
  elif 'A.T.O.M' in O000OOO :
   pass
  elif 'Almost Naked' in O000OOO :
   pass
  elif 'Angry Kid' in O000OOO :
   pass
  elif 'Annoying Orange' in O000OOO :
   pass
  elif 'Aqua Teen' in O000OOO :
   pass
  elif 'Assy Mcgee' in O000OOO :
   pass
  elif 'Astroblast' in O000OOO :
   pass
  elif 'Atomic Betty' in O000OOO :
   pass
  elif 'Axe Cop' in O000OOO :
   pass
  elif 'Baby Playpen' in O000OOO :
   pass
  elif 'Beavis and Butt' in O000OOO :
   pass
  elif 'Celebrity Deathmatch' in O000OOO :
   pass
  elif 'Clerks The' in O000OOO :
   pass
  elif 'Crapston Villas' in O000OOO :
   pass
  elif 'Duckman:' in O000OOO :
   pass
  elif 'Stripperella' in O000OOO :
   pass
  elif 'Vixen' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10006 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 64 - 64: oOoO0o00OO0 / o0o00Oo0O % I11i1ii1 % iiiiiiii1 % oOo0O0Ooo / O0Oooo0O
def IIiI11i111i ( url ) :
 I111i1II = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I111i1II )
 for I1i in IIi11i1i1iI1 :
  Ii1II111iIi = I1i
 OoOOo0OOoO = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I111i1II )
 for url in OoOOo0OOoO :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10007 , Ii1II111iIi )
  if 76 - 76: OoOo0o
  if 52 - 52: I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: iiiiiiii1 - iiiiiiii1
def IiIiIi ( url , IMAGE ) :
 ooOoOOiiiiIIii1I = [ ]
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( I111i1II )
 for O000OOO , O0Ooo in iI111i :
  if 'panda' in O0Ooo :
   oOOo0 = i11111IIIII ( O0Ooo )
   IIi11i1i1iI1 = re . compile ( "url: '(.+?)'" ) . findall ( oOOo0 )
   for Ii1I1 in IIi11i1i1iI1 :
    if 'http' in Ii1I1 :
     ooOoOOiiiiIIii1I . append ( { 'source' : 'playpanda' , 'quality' : 'SD' , 'url' : Ii1I1 } )
  elif 'easy' in O0Ooo :
   oo00O00oO = i11111IIIII ( O0Ooo )
   OoOOo0OOoO = re . compile ( 'file: "(.+?)"' ) . findall ( oo00O00oO )
   for Ii1I1 in OoOOo0OOoO :
    if 'http' in Ii1I1 :
     ooOoOOiiiiIIii1I . append ( { 'source' : 'easyvideo' , 'quality' : 'SD' , 'url' : Ii1I1 } )
  elif 'zoo' in O0Ooo :
   iIiIIIi = i11111IIIII ( O0Ooo )
   ooO0O00Oo0o = re . compile ( 'src: "(.+?)"' ) . findall ( iIiIIIi )
   for Ii1I1 in ooO0O00Oo0o :
    if 'http' in Ii1I1 :
     ooOoOOiiiiIIii1I . append ( { 'source' : 'videozoo' , 'quality' : 'SD' , 'url' : Ii1I1 } )
 if len ( ooOoOOiiiiIIii1I ) >= 3 :
  oOOOoo00 = iI111I11I1I1 . select ( 'Select Playlink' ,
 [ IIIi1I1IIii1II [ "source" ] + " - " + " (" + IIIi1I1IIii1II [ "quality" ] + ")"
 for IIIi1I1IIii1II in ooOoOOiiiiIIii1I ] )
  if oOOOoo00 != - 1 :
   url = ooOoOOiiiiIIii1I [ oOOOoo00 ] [ 'url' ]
   i1IIIi111111 = False
   xbmc . Player ( ) . play ( url )
   if 57 - 57: i1iIi . O0Oooo0O . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
   if 94 - 94: ooOoO0O00 * oOo * iii1i1iiiiIi
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 93 - 93: oOOoOooOo / OoOo0o * o0o00Oo0O
def iI11 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( I111i1II )
 for url in iI111i :
  OOIi1iI111II1I1 ( url )
  if 32 - 32: oOOoOooOo - ii + oOo
  if 90 - 90: oOoO0o00OO0 / ii % Ii - I11i1ii1
  if 30 - 30: iiiiiiii1
def iIOO000O ( ) :
 if 52 - 52: iiiiiiii1 . I11i1ii1 - oOoO0o00OO0 * iI11I1II1I1I % ooo0O / oOOoOooOo
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , I1IIIii + 'StandUp.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , I1IIIii + 'SearchComedian.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , I1IIIii + 'Others.png' , Oo00OOOOO , '' )
 if 18 - 18: iii1i1iiiiIi % OOOo00oo0oO % oOo / iiiiiiii1
def O0o0ooo00o0O ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  if 'elete' in O000OOO :
   pass
  else :
   Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 222 , I1i )
   if 72 - 72: oOOoOooOo % i1IiiiI1iI + oOo
def o0o0Oo ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 ooOoo00OoO00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , ooOooOOOoO0 , i1iII1IiiIiI1 in ooOoo00OoO00 :
  for oOoooO00O in ooOooOOOoO0 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiIii1iii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for IIo0o0O0O00oOOo , O000OOO in iiIii1iii :
    if 'tube' in IIo0o0O0O00oOOo :
     pass
    elif 'stage' in IIo0o0O0O00oOOo :
     Oo ( '[COLOR' + iiI1IiI + ']' + ooOooOOOoO0 + '   -   ' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1i , )
    elif 'vee' in IIo0o0O0O00oOOo :
     pass
     if 61 - 61: ooo0O - oOoO0o00OO0 * ooo0O % iI11I1II1I1I / I11i1ii1
def IIIiIII1 ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 ooOoo00OoO00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , ooOooOOOoO0 , i1iII1IiiIiI1 in ooOoo00OoO00 :
  iiIii1iii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for IIo0o0O0O00oOOo , O000OOO in iiIii1iii :
   if 'tube' in IIo0o0O0O00oOOo :
    pass
   elif 'stage' in IIo0o0O0O00oOOo :
    Oo ( '[COLOR' + iiI1IiI + ']' + ooOooOOOoO0 + '   -   ' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1i )
   elif 'vee' in IIo0o0O0O00oOOo :
    pass
    if 92 - 92: I1ii11iIi11i + I11i1ii1 / I1ii11iIi11i + i1iIi / OoOo0o
    if 3 - 3: i1iIi / o0o00Oo0O * oOOoOooOo - iii1i1iiiiIi
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: OOOo00oo0oO . ooo0O * i1IiiiI1iI
def iI1i1II ( url ) :
 oOOo0 = i11111IIIII ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1ii1ii1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOo0 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1ii1ii1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1ii1ii1I :
  I1iiIiiii1111 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 16 - 16: oOoO0o00OO0 / i1IiiiI1iI + ooo0O % Ii % OoOo0o - i1iIi
  if 37 - 37: OoOo0o * i1iIi * i1IiiiI1iI + iii1i1iiiiIi / Ii
  if 68 - 68: ii * i1IiiiI1iI
  if 86 - 86: ooo0O / iii1i1iiiiIi
  if 40 - 40: iiiiiiii1
  if 62 - 62: oOOoOooOo / OoOo0o
  if 74 - 74: iiiiiiii1 % O0Oooo0O / O0Oooo0O - iI11I1II1I1I - IIiIiII11i + OoOo0o
def iiOOOO0o ( ) :
 if 92 - 92: i1IiiiI1iI % O0Oooo0O
 I1i1i1 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 I1i1i1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 35 - 35: iI11I1II1I1I % O0Oooo0O * i1IiiiI1iI . I1ii11iIi11i
 iIiIi11 ( 'movies' , 'MAIN' )
 if 3 - 3: oOOoOooOo - oOoO0o00OO0 * oOo0O0Ooo . iii1i1iiiiIi
def OoOo ( ) :
 I1i1i1 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 I1i1i1 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 68 - 68: O0Oooo0O - iii1i1iiiiIi . Ii + ooo0O
 iIiIi11 ( 'movies' , 'MAIN' )
def Oo0oo ( ) :
 if 33 - 33: oOo0O0Ooo / i1IiiiI1iI . I1ii11iIi11i
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 Oooooooo00o00 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 89 - 89: iiiiiiii1 + ooOoO0O00 - I11i1ii1 + oOOoOooOo . IIiIiII11i
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + '/Movies/a.to.z/' + III1II1i + '.php'
  oOOo0 = i1Oo00 ( iI1i1IiIIIIi )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in iI111i :
   if oOoooO00O in O000OOO . lower ( ) :
    if '.php' in IIo0o0O0O00oOOo :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 426 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    else :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     Oo00oOOO0 ( O000OOO , IIo0o0O0O00oOOo , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
     if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
     iIiIi11 ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . iiiiiiii1 / iiiiiiii1
def i1I1I ( ) :
 if 45 - 45: iii1i1iiiiIi / oOo0O0Ooo
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 Oooooooo00o00 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 34 - 34: ooo0O % oOoO0o00OO0 + i1iIi * i1IiiiI1iI / OOOo00oo0oO
 for III1II1i in Oooooooo00o00 :
  i111Iii11i1Ii = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + III1II1i + '.php'
  oOOo0 = i1Oo00 ( i111Iii11i1Ii )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in iI111i :
   if oOoooO00O in O000OOO . lower ( ) :
    if '.php' in IIo0o0O0O00oOOo :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 426 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    else :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     Oo00oOOO0 ( O000OOO , IIo0o0O0O00oOOo , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
     if 65 - 65: iI11I1II1I1I * I11i1ii1
     iIiIi11 ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 89 - 89: I11i1ii1 % Ii . Ii + OOOo00oo0oO / oOoO0o00OO0
     if 19 - 19: oOo0O0Ooo
def OO0OO0 ( ) :
 if 100 - 100: OOOo00oo0oO + oOo
 I111i1II = i11111IIIII ( Ii1iIiII1ii1 + 'spongemain.php' )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , IIIIiii1IIii , IIo0o0O0O00oOOo , I1i , iI1iIii11Ii , O00O0 in iI111i :
  I1i1i1 ( O000OOO , IIo0o0O0O00oOOo , O00O0 , I1i , iI1iIii11Ii , IIIIiii1IIii )
  iIiIi11 ( 'movies' , 'MAIN' )
def OoOOOo0 ( url ) :
 if 53 - 53: ooo0O / i1IiiiI1iI % o0o00Oo0O / iI11I1II1I1I / iiiiiiii1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iIiii1Ii = ( '%s%s' % ( oO0OO00O0 , url ) )
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in iI111i :
  if '.php' in url :
   OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for Ii1II1I11i1 in OooOooO0O0o0 :
    if Ii1II1I11i1 == url :
     O000OOO = ( '[COLORred]Watched - [/COLOR]' + O000OOO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   o00oOOooOOo0o ( O000OOO , url , 426 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
  else :
   OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for Ii1II1I11i1 in OooOooO0O0o0 :
    if Ii1II1I11i1 == url :
     O000OOO = ( '[COLORred]Watched - [/COLOR]' + O000OOO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   Oo00oOOO0 ( O000OOO , url , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
   if 17 - 17: o0o00Oo0O - i1iIi + I11i1ii1
   iIiIi11 ( 'movies' , 'MAIN' )
   if 49 - 49: I1ii11iIi11i % OOOo00oo0oO
   xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 49 - 49: O0Oooo0O * OOOo00oo0oO / ooo0O
   if 78 - 78: I11i1ii1 + i1IiiiI1iI - ooo0O + oOo / iI11I1II1I1I
def ii111I111i ( url ) :
 if 18 - 18: OOOo00oo0oO - I11i1ii1 % i1IiiiI1iI * i1iIi
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , IIIIiii1IIii , url , I1i , iI1iIii11Ii , O00O0 in iI111i :
  I1i1i1 ( O000OOO , url , O00O0 , I1i , iI1iIii11Ii , IIIIiii1IIii )
  if 66 - 66: ooOoO0O00 - ooOoO0O00 - OoOo0o . i1IiiiI1iI
  iIiIi11 ( 'movies' , 'MAIN' )
  if 25 - 25: ooOoO0O00 * oOo0O0Ooo - iii1i1iiiiIi + OOOo00oo0oO
  if 74 - 74: iiiiiiii1 / O0Oooo0O / IIiIiII11i - iiiiiiii1 / OOOo00oo0oO % i1IiiiI1iI
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: I11i1ii1 % ii + ii
def Oo00oOOO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 7 - 7: ooOoO0O00
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
 if 91 - 91: iii1i1iiiiIi - iii1i1iiiiIi . I11i1ii1
def I1i1i1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 33 - 33: O0Oooo0O - iI11I1II1I1I / i1iIi % o0o00Oo0O
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
if 78 - 78: i1iIi
if 29 - 29: IIiIiII11i
if 79 - 79: iI11I1II1I1I - Ii + oOOoOooOo - IIiIiII11i . iI11I1II1I1I
def OO000o0O0o ( string ) :
 if O00O0oOO00O00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 67 - 67: OoOo0o . Ii + oOOoOooOo . iI11I1II1I1I
def iiIi1i ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I1i11IIiiIiI = [ ]
 try :
  if 7 - 7: oOo * Ii * iI11I1II1I1I / OoOo0o / O0Oooo0O
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( oo0OooOOo0 ) == False :
  OO000o0O0o ( 'Making Favorites File' )
  I1i11IIiiIiI . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iiI11Iii = open ( oo0OooOOo0 , "w" )
  iiI11Iii . write ( json . dumps ( I1i11IIiiIiI ) )
  iiI11Iii . close ( )
 else :
  OO000o0O0o ( 'Appending Favorites' )
  iiI11Iii = open ( oo0OooOOo0 ) . read ( )
  i11Ii1iiiI1I = json . loads ( iiI11Iii )
  i11Ii1iiiI1I . append ( ( name , url , iconimage , fanart , mode ) )
  oO0o0OooOO0 = open ( oo0OooOOo0 , "w" )
  oO0o0OooOO0 . write ( json . dumps ( i11Ii1iiiI1I ) )
  oO0o0OooOO0 . close ( )
  if 50 - 50: I1ii11iIi11i - oOo0O0Ooo * oOo . oOOoOooOo % oOo + ii
  if 25 - 25: iiiiiiii1 . oOo / iI11I1II1I1I
def OOoo00OoO0o ( ) :
 if os . path . exists ( oo0OooOOo0 ) == False :
  I1i11IIiiIiI = [ ]
  OO000o0O0o ( 'Making Favorites File' )
  I1i11IIiiIiI . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  iiI11Iii = open ( oo0OooOOo0 , "w" )
  iiI11Iii . write ( json . dumps ( I1i11IIiiIiI ) )
  iiI11Iii . close ( )
 else :
  II11Iii1 = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
  IIIIiII = len ( II11Iii1 )
  for OooOoOo in II11Iii1 :
   O000OOO = OooOoOo [ 0 ]
   IIo0o0O0O00oOOo = OooOoOo [ 1 ]
   i1i1II1i11 = OooOoOo [ 2 ]
   try :
    iIIii1i1iIiI = OooOoOo [ 3 ]
    if iIIii1i1iIiI == None :
     raise
   except :
    if O0oo0OO0 . getSetting ( 'use_thumb' ) == "true" :
     iIIii1i1iIiI = i1i1II1i11
    else :
     iIIii1i1iIiI = iI1iIii11Ii
   try : oOooooo = OooOoOo [ 5 ]
   except : oOooooo = None
   try : OO00 = OooOoOo [ 6 ]
   except : OO00 = None
   if 44 - 44: I1ii11iIi11i + iiiiiiii1
   if OooOoOo [ 4 ] == 0 :
    o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , '' , i1i1II1i11 , iI1iIii11Ii , '' , 'fav' )
   else :
    o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , OooOoOo [ 4 ] , i1i1II1i11 , iI1iIii11Ii , '' , 'fav' )
    if 8 - 8: iiiiiiii1 - iii1i1iiiiIi % oOOoOooOo . oOo
def iI11iOoo ( name ) :
 i11Ii1iiiI1I = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
 for Ooo00o0oOo0O0O in range ( len ( i11Ii1iiiI1I ) ) :
  if i11Ii1iiiI1I [ Ooo00o0oOo0O0O ] [ 0 ] == name :
   del i11Ii1iiiI1I [ Ooo00o0oOo0O0O ]
   oO0o0OooOO0 = open ( oo0OooOOo0 , "w" )
   oO0o0OooOO0 . write ( json . dumps ( i11Ii1iiiI1I ) )
   oO0o0OooOO0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 66 - 66: O0Oooo0O - i1IiiiI1iI . I11i1ii1 % OOOo00oo0oO
 if 27 - 27: ooOoO0O00
def I11II11IiI11 ( ) :
 ooOO0o000OO = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 OoO00OOoO = open ( ooOO0o000OO , "w+" )
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oOOo0 )
 OoO00OOoO . write ( r'[' + o0OOO + ']' + '\n' )
 for O000OOO , I1i , O00Oooo , IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = ( IIo0o0O0O00oOOo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iiiI = ( O000OOO + '=plugin://' + o0OOO + '/?url=' + IIo0o0O0O00oOOo + '&mode=10012&name=' + ( O000OOO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( I1i ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( I1i ) . replace ( ' ' , '' ) + '+&amp;description=' )
  OoO00OOoO . write ( iiiI + '\n' )
  if 27 - 27: oOo0O0Ooo / ii
  if 74 - 74: oOoO0o00OO0 % O0Oooo0O - oOo * i1IiiiI1iI . ii * oOo
def OOOooooOo0 ( ) :
 I111i1II = cloudflare . source ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 iI111i = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo in iI111i :
  o0OO ( '24/7' , IIo0o0O0O00oOOo , 90021 , I1IIIii + '247Streams.png' )
  if 63 - 63: O0Oooo0O
def Oo00OO00Ooo ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + '247Streams.png' , I1IIIii + '247Streams.png' , '' )
def IiII111I ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + 'musicch.png' , I1IIIii + 'musicch.png' , '' )
def OOOoO ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + 'NEWS.png' , I1IIIii + 'NEWS.png' , '' )
def II1O0o00 ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + 'adult.png' , I1IIIii + 'adult.png' , '' )
def OOO00O0000 ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 iI111i = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  O0O0ooOOO ( O000OOO , IIo0o0O0O00oOOo , 1016 , I1IIIii + 'TUTS.png' , I1IIIii + 'TUTS.png' , '' )
  if 90 - 90: i1iIi . iii1i1iiiiIi
  if 89 - 89: O0Oooo0O - oOo - ooo0O
def i1iii11 ( ) :
 if 39 - 39: oOoO0o00OO0
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 if 10 - 10: ii . OoOo0o * i1iIi - oOoO0o00OO0
def I1IOOooO0o00OOo ( ) :
 if 90 - 90: IIiIiII11i / OoOo0o * oOo0O0Ooo - I1ii11iIi11i
 I111i1II = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , I1i , O000OOO , I1I1Iiii1 in iI111i :
  o00oOOooOOo0o ( O000OOO + '  -  ' + ( I1I1Iiii1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IIo0o0O0O00oOOo , 10023 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
  if 11 - 11: I11i1ii1 - OOOo00oo0oO - OOOo00oo0oO / O0Oooo0O * IIiIiII11i % OOOo00oo0oO
  if 39 - 39: OOOo00oo0oO / Ii
  if 46 - 46: Ii . oOoO0o00OO0
def iI11IIiII1iII ( ) :
 if 51 - 51: iI11I1II1I1I * iii1i1iiiiIi / i1iIi * oOo
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
 if 58 - 58: o0o00Oo0O - ooOoO0O00 / iiiiiiii1
def OO0O0000oo ( url ) :
 I111iIIII11iI = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oOOo0 = cloudflare . source ( I111iIIII11iI )
 iI111i = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , I1i , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10022 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
  if 72 - 72: oOOoOooOo + IIiIiII11i . o0o00Oo0O - iiiiiiii1 / ii . O0Oooo0O
  if 28 - 28: iI11I1II1I1I . o0o00Oo0O
  if 32 - 32: ii
  if 29 - 29: oOoO0o00OO0
def iI111iiI1II ( ) :
 if 96 - 96: iii1i1iiiiIi * o0o00Oo0O - IIiIiII11i . oOOoOooOo - i1iIi
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 IIo0o0O0O00oOOo = ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOoooO00O ) . replace ( ' ' , '+' )
 oOOo0 = cloudflare . source ( IIo0o0O0O00oOOo )
 iI111i = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  if oOoooO00O in O000OOO . lower ( ) :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 10022 , I1IIIii + 'dtv.png' )
   if 84 - 84: OOOo00oo0oO * ooo0O * ooo0O - iiiiiiii1
   if 25 - 25: OOOo00oo0oO + O0Oooo0O + oOo0O0Ooo + o0o00Oo0O * IIiIiII11i + oOo0O0Ooo
   if 66 - 66: OOOo00oo0oO
def O0iI1Iii1i1I ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for O0Ooo , o0O0 , ooOo0O0o0 , O000OOO in iI111i :
  OoO0 = ( ooOo0O0o0 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IIiIi = ( o0O0 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OoOOoi111II = 'Season ' + IIiIi + 'Episode ' + OoO0 + O000OOO
  iii1iII1I1I ( OoOOoi111II , O0Ooo )
  if 79 - 79: ooOoO0O00 / i1iIi
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 81 - 81: iI11I1II1I1I
  if 86 - 86: I11i1ii1 % I11i1ii1 % ii
def iii1iII1I1I ( name , url ) :
 O0Ooo = url
 IIIi11 = name
 oo00O00oO = cloudflare . source ( O0Ooo )
 IIi11i1i1iI1 = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oo00O00oO )
 for I1ii1ii1I , ii11 in IIi11i1i1iI1 :
  Oo ( '[COLOR' + iiI1IiI + ']' + IIIi11 + ii11 + '[/COLOR]' , I1ii1ii1I , 222 , I1IIIii + 'dtv.png' )
  if 43 - 43: iii1i1iiiiIi % i1iIi + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: ooo0O * I1ii11iIi11i - i1iIi . oOOoOooOo
 if 2 - 2: I1ii11iIi11i - oOOoOooOo % iI11I1II1I1I
def oOIII111iiIi1 ( ) :
 if 88 - 88: O0Oooo0O - oOo
 if 79 - 79: iiiiiiii1
 if 45 - 45: IIiIiII11i + iiiiiiii1 . i1IiiiI1iI . o0o00Oo0O * ooOoO0O00 - i1iIi
 if 48 - 48: oOoO0o00OO0 + I1ii11iIi11i
 if 76 - 76: oOoO0o00OO0
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - oOoO0o00OO0 . i1iIi
 if 51 - 51: i1iIi + Ii * oOo % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , '' , 10091 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 if 20 - 20: O0Oooo0O . i1IiiiI1iI . i1iIi + i1IiiiI1iI - OoOo0o * OOOo00oo0oO
def o00ooO0 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oOOo0 )
 iIIiiI1Ii1II = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oOOo0 )
 for I1i , url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + I1i , '' , '' )
 for url in iIIiiI1Ii1II :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , I1IIIii + 'Next.png' , '' , '' )
  if 25 - 25: oOo0O0Ooo
def o0o0OoOo0 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oOOo0 )
 iIIiiI1Ii1II = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oOOo0 )
 for I1i , url , O000OOO in iI111i :
  I1i = 'http://watchepisodes.cc/' + I1i
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10093 , I1i , I1i , '' )
 for url in iIIiiI1Ii1II :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , I1IIIii + 'Next.png' , '' , '' )
  if 89 - 89: I11i1ii1
def OO0OOo00Oo ( url , iconimage ) :
 I1i = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oOOo0 )
 for ooOo0O0o0 , url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ooOo0O0o0 + ' - ' + O000OOO + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , I1i , '' , '' )
  if 26 - 26: IIiIiII11i * iiiiiiii1 + ooo0O / o0o00Oo0O + ooOoO0O00 - i1IiiiI1iI
def o000oOoOOO ( url , iconimage ) :
 I1i = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  if 'player' in O000OOO :
   pass
  elif 'vod' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , I1i , '' , '' )
   if 88 - 88: oOoO0o00OO0 % oOoO0o00OO0 + ii - OoOo0o * o0o00Oo0O
   if 100 - 100: iI11I1II1I1I - iii1i1iiiiIi
   if 28 - 28: I1ii11iIi11i . o0o00Oo0O . i1IiiiI1iI
   if 60 - 60: IIiIiII11i + O0Oooo0O / OOOo00oo0oO % ii - ooOoO0O00
   if 57 - 57: oOOoOooOo
   if 99 - 99: I1ii11iIi11i + O0Oooo0O % oOOoOooOo - ooo0O
def o0oo0oo0 ( ) :
 if 2 - 2: oOo + O0Oooo0O . OOOo00oo0oO - oOoO0o00OO0 % iiiiiiii1
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / i1iIi
 if 29 - 29: oOoO0o00OO0 / OOOo00oo0oO * o0o00Oo0O - Ii - oOo + i1iIi
 if 86 - 86: oOo0O0Ooo / oOoO0o00OO0 * i1iIi % Ii
 if 20 - 20: iiiiiiii1 . ii + iiiiiiii1 + oOOoOooOo * oOoO0o00OO0
 if 44 - 44: Ii
 if 69 - 69: OoOo0o * o0o00Oo0O + Ii
 if 65 - 65: o0o00Oo0O / iiiiiiii1 . ooOoO0O00 * iiiiiiii1 / iI11I1II1I1I - OOOo00oo0oO
 if 93 - 93: iii1i1iiiiIi % Ii - i1iIi % oOo
 if 55 - 55: ooo0O . oOoO0o00OO0
 if 63 - 63: OOOo00oo0oO
 if 79 - 79: oOoO0o00OO0 - OOOo00oo0oO - ooo0O . OoOo0o
 if 65 - 65: Ii . oOo % iiiiiiii1 + I11i1ii1 - Ii
 if 60 - 60: O0Oooo0O
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , I1IIIii + 'latest.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , I1IIIii + 'popular.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , I1IIIii + 'Genre.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , I1IIIii + 'series.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , I1IIIii + 'Search.png' , I1IIIii + 'WatchSeries.png' , '' )
 if 14 - 14: I1ii11iIi11i % OOOo00oo0oO * iiiiiiii1 - Ii / oOoO0o00OO0 * Ii
 if 95 - 95: iI11I1II1I1I + iii1i1iiiiIi . oOo0O0Ooo + iii1i1iiiiIi * i1IiiiI1iI + OoOo0o
def i1i11IiII ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0ooooo0OOOO0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O0ooooo0OOOO0 ) )
 for url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 94 - 94: iI11I1II1I1I / oOo0O0Ooo * oOoO0o00OO0
def I1i1ii1IiI1i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 78 - 78: iiiiiiii1
def I11i1i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if 'episode' in url :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , I1IIIii + 'Next.png' , '' , '' )
  if 40 - 40: oOo * iii1i1iiiiIi * iI11I1II1I1I / iii1i1iiiiIi * ii / oOoO0o00OO0
  if 33 - 33: Ii % ooo0O . iiiiiiii1 * OoOo0o / i1IiiiI1iI
def iI111II ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11iI1I1 = 'http://www.watchseriesgo.to/search/' + oOoooO00O . replace ( ' ' , '%20' )
 oOOo0 = i11111IIIII ( i11iI1I1 )
 iI111i = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'watch online' in O000OOO :
   pass
  else :
   print IIo0o0O0O00oOOo
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + IIo0o0O0O00oOOo , 10044 , I1i , '' , '' )
   if 89 - 89: iiiiiiii1
   xbmcplugin . setContent ( IIIii1II1II , 'movies' )
   if 9 - 9: I11i1ii1 . i1IiiiI1iI
def IiIiiiIii1i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , url , O000OOO , ooOo0O0o0 , IIIIiii1IIii in iI111i :
  IIi11II1II111 = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( ooOo0O0o0 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + IIi11II1II111 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1i , '' , IIIIiii1IIii )
  if 71 - 71: ooo0O . oOoO0o00OO0 % IIiIiII11i / iI11I1II1I1I % iii1i1iiiiIi - oOoO0o00OO0
def Ooo00O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  IIi11II1II111 = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + IIi11II1II111 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , I1IIIii + 'Next.png' , '' , '' )
  if 74 - 74: ooo0O % iii1i1iiiiIi . iiiiiiii1 % O0Oooo0O . o0o00Oo0O % IIiIiII11i
def iIiiIi11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I1i , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , I1IIIii + 'Next.png' , '' , '' )
  if 73 - 73: I11i1ii1 - I11i1ii1 / ii
def oOoOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oOOo0 )
 O0ooooo0OOOO0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 for o0O0 , ooOoo00OoO00 in O0ooooo0OOOO0 :
  iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( ooOoo00OoO00 ) )
  for url , O000OOO in iI111i :
   IIi11II1II111 = ( o0O0 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + IIi11II1II111 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I1IIIii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 55 - 55: I11i1ii1 * ooo0O * oOOoOooOo - ooOoO0O00 / i1iIi * OOOo00oo0oO
class ooOiiIII ( ) :
 if 37 - 37: ii / oOoO0o00OO0 % ooo0O
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 34 - 34: iii1i1iiiiIi . i1IiiiI1iI % OOOo00oo0oO - o0o00Oo0O * o0o00Oo0O
  IIi11II1II111 = name
  self . Get_Sources ( IIo0o0O0O00oOOo , IIi11II1II111 )
  if 11 - 11: o0o00Oo0O * Ii * IIiIiII11i / OoOo0o * o0o00Oo0O
  if 71 - 71: i1IiiiI1iI . I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  o0oO0 = xbmcgui . DialogProgress ( )
  oOOo0 = i11111IIIII ( URL )
  iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , O000OOO in iI111i :
   URL = 'http://www.watchseriesgo.to/link/' + IIo0o0O0O00oOOo
   self . Get_site_link ( URL , season_name )
   if 24 - 24: OoOo0o * ii . o0o00Oo0O . oOo . oOo0O0Ooo
 def Get_site_link ( self , url , season_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oOOo0 )
  OoOOo0OOoO = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oOOo0 )
  for url in iI111i :
   self . main ( url , season_name )
  for url in IIi11i1i1iI1 :
   self . main ( url , season_name )
  for url in OoOOo0OOoO :
   self . main ( url , season_name )
   if 80 - 80: o0o00Oo0O * oOo . O0Oooo0O % o0o00Oo0O
 def main ( self , url , season_name ) :
  o0oO0 . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ii11I1iIIi = 'DACLIPS'
   if ii11I1iIIi in ooOiiIII . source_list :
    pass
   else :
    self . daclips ( url , season_name , ii11I1iIIi )
    o0oO0 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    ii11I1iIIi = 'THEVIDEO'
    if ii11I1iIIi in ooOiiIII . source_list :
     pass
    else :
     self . thevideo ( url , season_name , ii11I1iIIi )
     o0oO0 . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     ii11I1iIIi = 'ALLMYVIDEOS'
     if ii11I1iIIi in ooOiiIII . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , ii11I1iIIi )
      o0oO0 . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      ii11I1iIIi = 'VIDSPOT'
      if ii11I1iIIi in ooOiiIII . source_list :
       pass
      else :
       self . vidspot ( url , season_name , ii11I1iIIi )
       o0oO0 . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       ii11I1iIIi = 'VODLOCKER'
       if ii11I1iIIi in ooOiiIII . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , ii11I1iIIi )
        o0oO0 . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        ii11I1iIIi = 'VIDTO'
        if ii11I1iIIi in ooOiiIII . source_list :
         pass
        else :
         self . vidto ( url , season_name , ii11I1iIIi )
         o0oO0 . update ( 0 , "" , "Getting Vidto Links" )
         if 29 - 29: i1iIi + iiiiiiii1 % oOoO0o00OO0 + i1IiiiI1iI * I1ii11iIi11i - Ii
       else :
        if 'youwatch' in url :
         ii11I1iIIi = 'YouWatch'
         if ii11I1iIIi in ooOiiIII . source_list :
          pass
         else :
          self . youwatch ( url , season_name , ii11I1iIIi )
          o0oO0 . update ( 0 , "" , "Getting YouWatch Links" )
          if 24 - 24: Ii . oOOoOooOo + oOOoOooOo - Ii % OoOo0o
          if 58 - 58: oOo0O0Ooo
 def allmyvid ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  for IiiIi1III , O000OOO in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
   if 94 - 94: ooo0O + i1iIi % ooo0O . O0Oooo0O - oOOoOooOo * oOo0O0Ooo
 def vidspot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oOOo0 )
  for IiiIi1III , O000OOO in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
   if 62 - 62: I1ii11iIi11i * ooOoO0O00 % oOoO0o00OO0 + I1ii11iIi11i . o0o00Oo0O . oOOoOooOo
 def thevideo ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{"file":"([^"]*)"' ) . findall ( oOOo0 )
  for IiiIi1III in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
   if 57 - 57: I1ii11iIi11i - O0Oooo0O + o0o00Oo0O % ooo0O
 def vodlocker ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for IiiIi1III in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
   if 72 - 72: OoOo0o . iii1i1iiiiIi / IIiIiII11i
 def daclips ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oOOo0 )
  for IiiIi1III in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
   if 69 - 69: OoOo0o * IIiIiII11i - oOOoOooOo - ooOoO0O00 + Ii
 def filehoot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for IiiIi1III in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for IiiIi1III in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
  for IiiIi1III in iI111i :
   self . youplay ( IiiIi1III , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for IiiIi1III in iI111i :
   self . Printer ( IiiIi1III , season_name , source_name )
   if 50 - 50: ii * ooOoO0O00 / OOOo00oo0oO
 def Printer ( self , Link , season_name , source_name ) :
  if 83 - 83: ooOoO0O00
  if Link in ooOiiIII . List :
   pass
  elif source_name in ooOiiIII . source_list :
   pass
  else :
   Oo ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 222 , I1IIIii + 'WATCHSERIES.png' )
   o0oO0 . update ( 100 , "" , "Got Source" )
   ooOiiIII . List . append ( Link )
   ooOiiIII . source_list . append ( source_name )
   if 38 - 38: ii * iI11I1II1I1I
   xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 54 - 54: ii . O0Oooo0O
   if 71 - 71: i1iIi
   if 31 - 31: i1IiiiI1iI . Ii . oOo * I1ii11iIi11i % i1iIi . ooo0O
   if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
   if 93 - 93: oOOoOooOo % O0Oooo0O
def i1111IIiii1 ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , I1IIIii + 'Highlights.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , I1IIIii + 'Fixtures.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , I1IIIii + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 46 - 46: oOoO0o00OO0 * iii1i1iiiiIi * I11i1ii1 * oOoO0o00OO0 . oOoO0o00OO0
def i1I11iIIiIIiIi ( url ) :
 ii1IiI = '20'
 o0oO00O000O = [ ]
 IiIIiIi1 = '                                                    '
 ooOoo0OoO0 = '        '
 o00oOOooOOo0o ( IiIIiIi1 + 'pl' + ooOoo0OoO0 + 'w' + ooOoo0OoO0 + 'd' + ooOoo0OoO0 + 'l' + ooOoo0OoO0 + 'f' + ooOoo0OoO0 + 'a' + ooOoo0OoO0 + 'pts' , '' , '' , '' , '' , '' )
 I111i1II = o0OiiiI1i11Ii ( url )
 iI111i = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( I111i1II )
 for oO0OO00o , oooooOOOO0oOo , iiii1Ii , OoOOoo0 , IIiiiI , OOOO0OOO , iiI11Iii , ii11iI1i1i1i1i , iiII1i1II1iIi in iI111i :
  iIIOOOO0o0Oo0 = I1iIiI1iiI ( oooooOOOO0oOo )
  oO000O00 = I1iIiI1iiI ( iiii1Ii )
  IiIIIii1iIII1 = I1iIiI1iiI ( OoOOoo0 )
  OoOooooo0oo = I1iIiI1iiI ( IIiiiI )
  ii1II1 = I1iIiI1iiI ( OOOO0OOO )
  i1I1II11I1 = I1iIiI1iiI ( iiI11Iii )
  o0oO00O000O . append ( oO0OO00o [ 0 ] )
  oo0oOoOoo = len ( o0oO00O000O )
  O0oOoOooo00oo = int ( len ( IiIIiIi1 ) - len ( oO0OO00o ) - 2 )
  if len ( o0oO00O000O ) >= 10 :
   O0oOoOooo00oo = O0oOoOooo00oo - 1
  if len ( o0oO00O000O ) <= int ( ii1IiI ) :
   O0O0ooOOO ( str ( oo0oOoOoo ) + ' ' + oO0OO00o + IiIIiIi1 [ 0 : O0oOoOooo00oo ] + oooooOOOO0oOo + iIIOOOO0o0Oo0 + iiii1Ii + oO000O00 + OoOOoo0 + IiIIIii1iIII1 + IIiiiI + OoOooooo0oo + OOOO0OOO + ii1II1 + iiI11Iii + i1I1II11I1 + ' ' + iiII1i1II1iIi , '' , '' , '' , '' , '' )
   if 84 - 84: oOo - i1IiiiI1iI + iii1i1iiiiIi + O0Oooo0O % IIiIiII11i - oOo0O0Ooo
   if 46 - 46: i1iIi * i1iIi / OOOo00oo0oO * O0Oooo0O
def I1iIiI1iiI ( space ) :
 if len ( space ) > 1 :
  OoOooOo00O = len ( '        ' ) - len ( space ) + 1
  space = int ( OoOooOo00O ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 37 - 37: iii1i1iiiiIi + I11i1ii1
def II1iiiiII ( ) :
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
 if 30 - 30: ii % OoOo0o
 if 14 - 14: iii1i1iiiiIi / oOo / Ii - iii1i1iiiiIi / ooo0O - OoOo0o
 if 81 - 81: iiiiiiii1 % i1iIi . oOOoOooOo
 if 66 - 66: oOoO0o00OO0 * i1iIi / ii * o0o00Oo0O % OoOo0o
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * i1iIi / O0Oooo0O * ii
 if 82 - 82: I1ii11iIi11i / i1iIi / i1iIi % i1iIi
 if 20 - 20: oOOoOooOo
 if 63 - 63: iI11I1II1I1I . oOo
 if 100 - 100: ooOoO0O00 * ooOoO0O00
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iI111i = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IIo0o0O0O00oOOo , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I1i , Oo00OOOOO , '' )
  if 26 - 26: OoOo0o . oOo % iii1i1iiiiIi
def ooOO0o0ooOo0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0ooooo0OOOO0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oOOo0 )
 for O0ooooo0OOOO0 in O0ooooo0OOOO0 :
  I11II1i1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( O0ooooo0OOOO0 ) )
  for i11iii11 in I11II1i1 :
   i11iii11 = i11iii11
  iII1111III1I = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O0ooooo0OOOO0 ) )
  for III1 , I1i , time , I11111i in iII1111III1I :
   iI = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I11111i )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i11iii11 + ' - ' + III1 + ' - ' + time + '[/COLOR]' , '' , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I1i , Oo00OOOOO , ( str ( iI ) ) )
   if 46 - 46: ii
 iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if 80 - 80: o0o00Oo0O * iiiiiiii1
def O0O0o ( ) :
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
 if 92 - 92: oOo0O0Ooo % iI11I1II1I1I / OOOo00oo0oO % I11i1ii1
def oOO0o0 ( url ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , url , O000OOO in iI111i :
  oooO0O0O0ooO = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in O000OOO :
   pass
  else :
   oooO0O0O0ooO = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   Oo ( '[COLOR' + iiI1IiI + ']' + oooO0O0O0ooO + '[/COLOR]' , url , 10013 , I1i )
 for url , I1i , O000OOO in IIi11i1i1iI1 :
  oooO0O0O0ooO = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in O000OOO :
   pass
  else :
   Oo ( '[COLOR' + iiI1IiI + ']' + oooO0O0O0ooO + '[/COLOR]' , url , 10013 , I1i )
def OOO0ooo ( url ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 if 9 - 9: ooo0O
 if 97 - 97: OoOo0o
 if 99 - 99: i1IiiiI1iI % O0Oooo0O . o0o00Oo0O * I11i1ii1
 if 87 - 87: i1iIi % oOoO0o00OO0 * I1ii11iIi11i
 if 59 - 59: I1ii11iIi11i / i1IiiiI1iI - iI11I1II1I1I * iI11I1II1I1I
 if 18 - 18: i1IiiiI1iI * oOoO0o00OO0 / Ii / iI11I1II1I1I * ii . OoOo0o
 if 69 - 69: I1ii11iIi11i * oOOoOooOo
 for url , I1i , O000OOO in IIi11i1i1iI1 :
  oooO0O0O0ooO = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in O000OOO :
   pass
  else :
   Oo ( '[COLOR' + iiI1IiI + ']' + oooO0O0O0ooO + '[/COLOR]' , url , 10013 , I1i )
   if 91 - 91: ooo0O . oOOoOooOo / oOo / Ii * ooo0O
def Ooooo0OO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oOOo0 )
 for I1ii1ii1I in iI111i :
  o0o0OO0OO = ( I1ii1ii1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I1iiIiiii1111 ( 'http:' + o0o0OO0OO )
  if 21 - 21: oOo0O0Ooo - ii / iii1i1iiiiIi * ii % ii + oOo
  if 89 - 89: iiiiiiii1 . OoOo0o . oOoO0o00OO0
  if 93 - 93: IIiIiII11i
  if 8 - 8: i1iIi * ii / i1iIi / oOo % iii1i1iiiiIi + i1IiiiI1iI
def i1I1iIIiIII ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO , I1i in iI111i :
  Oo ( O000OOO , url , 8046 , I1i )
 for url in IIi11i1i1iI1 :
  o0OO ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , I1IIIii + 'Next.png' )
def iI1i11i1i1i ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I111i1II )
 for url , I1i , O000OOO in iI111i :
  I1iiIiiii1111 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 83 - 83: IIiIiII11i + I11i1ii1 - ooo0O % ooo0O * ooo0O
def o0iiiii1i1 ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I111i1II )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 18 - 18: iii1i1iiiiIi * iii1i1iiiiIi - ooo0O % oOOoOooOo % IIiIiII11i - I11i1ii1
def oo00OOoOoO00 ( ) :
 o0OO ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , I1IIIii + 'documentary.png' )
 o0OO ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , I1IIIii + 'documentary.png' )
 o0OO ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , I1IIIii + 'Search.png' )
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( O000OOO , IIo0o0O0O00oOOo , 8041 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I111i1II )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I111i1II )
 for I1i , url , O000OOO in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + I1i )
 for url in next :
  o0OO ( 'NEXT PAGE' , url , 8041 , I1IIIii + 'Next.png' )
  if 30 - 30: i1IiiiI1iI - oOo
  if 15 - 15: ii
def iII1i ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I111i1II )
 for url in iI111i :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   Oo ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
  else :
   o0OO ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def OO00o0O0OO0o0 ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , url in iI111i :
  url = ( url ) . replace ( '\/' , '/' )
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , '' )
  if 10 - 10: OoOo0o
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iiii11IiI1 ( name , url ) :
 IiiIi = 0
 name = name
 url = url
 oo0 = [ '144' , '240' , '380' , '480' , '720' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  OOIi1iI111II1I1 ( url )
  if 71 - 71: ii - iiiiiiii1 + i1iIi / o0o00Oo0O % ooo0O + oOo
  if 83 - 83: I11i1ii1 * oOoO0o00OO0 / I11i1ii1 * I11i1ii1 - OoOo0o
  if 89 - 89: oOo % i1IiiiI1iI
  if 51 - 51: oOOoOooOo * i1iIi * ii % iii1i1iiiiIi
  if 25 - 25: iI11I1II1I1I * ii * i1iIi - ooOoO0O00
  if 23 - 23: ooo0O . oOOoOooOo - ii + i1IiiiI1iI
  if 73 - 73: iii1i1iiiiIi
  if 71 - 71: Ii * iii1i1iiiiIi * OoOo0o + OOOo00oo0oO + I1ii11iIi11i
def oOoOo0OOOOOO ( ) :
 I111i1II = o0Ooo0O00 ( 'http://documentarylovers.com/' )
 iI111i = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  if 'genre' in IIo0o0O0O00oOOo :
   o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , IIo0o0O0O00oOOo , 80010 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1IIiIiOoOO0OOo0Oo ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I111i1II )
 for url , O000OOO , I1i in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , I1i )
 for url in next :
  o0OO ( 'NEXT PAGE' , url , 80010 , I1IIIii + 'Next.png' )
  if 33 - 33: oOoO0o00OO0 - I11i1ii1
def i1IiIii1i ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I111i1II )
 for url in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
 for url in IIi11i1i1iI1 :
  OO00o0O0OO0o0 ( url )
  if 27 - 27: oOo % oOOoOooOo - o0o00Oo0O
def IIIIi1i ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0oOO0ooOoO = 'http://documentarylovers.com/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 ooO0000o00O = o0oOO0ooOoO . lower ( )
 I1IIiIiOoOO0OOo0Oo ( ooO0000o00O )
 if 36 - 36: oOo - ooo0O . iiiiiiii1 % iiiiiiii1
def iI1II ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  if 'films' in url :
   o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , I1IIIii + 'documentary.png' )
def OO0o0oO0 ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I111i1II )
 for I1i , url , O000OOO in iI111i :
  if 'films' in url :
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + I1i )
 for url in IIi11i1i1iI1 :
  o0OO ( 'NEXT' , url , 8049 , I1IIIii + 'Next.png' )
def o00o ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I111i1II )
 for url in iI111i :
  if 'rtd' in url :
   iiIi1io0o0OoOo ( url )
   if 49 - 49: ooOoO0O00 - iii1i1iiiiIi - i1IiiiI1iI * oOo0O0Ooo . oOOoOooOo
def iiIi1io0o0OoOo ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I111i1II )
 for IIIi1I1IIii1II , file in iI111i :
  url = ( 'https://rtd.rt.com' + IIIi1I1IIii1II + file )
  OOIi1iI111II1I1 ( url )
  if 24 - 24: oOOoOooOo
  if 79 - 79: ooOoO0O00 . i1IiiiI1iI % oOo % I11i1ii1 - OOOo00oo0oO - Ii
def oO0oOOOOOO0ooOOOoo ( ) :
 oOOo0 = o0Ooo0O00 ( 'http://www.stream2watch.co/live-tv' )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO , iIIIiIi in iI111i :
  o0OO ( ( O000OOO + '[COLOR' + iiI1IiI + ']' + iIIIiIi + '[/COLOR]' ) , IIo0o0O0O00oOOo , 8086 , I1i )
  if 76 - 76: iI11I1II1I1I * O0Oooo0O / oOo0O0Ooo
def ooOO0O00O ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , I1i , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 8087 , I1i )
  if 31 - 31: iI11I1II1I1I
def oOOOoOo0oOoo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  OoOOOO0 ( url , O000OOO )
  if 33 - 33: oOo0O0Ooo - iiiiiiii1 . ooOoO0O00 / Ii
def OoOOOO0 ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  print url
  Oo ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 84 - 84: i1IiiiI1iI / ii / I11i1ii1 % i1IiiiI1iI . OoOo0o + O0Oooo0O
def oO0OOOo0OO ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + IIo0o0O0O00oOOo , 3002 , 'http://www.solie.org/alibrary/' + I1i )
def i1IiI ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I111i1II )
 for url , I1i , O000OOO in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1i )
def I1iI1i ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I111i1II )
 iIIiiI1II = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I111i1II )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , I1IIIii + 'classicmovies.png' )
 for url , O000OOO in iIIiiI1II :
  o0OO ( '[COLOR' + iiI1IiI + ']Season- ' + O000OOO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'classicmovies.png' )
 for url in next :
  o0OO ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'Next.png' )
 for url , I1i , O000OOO in IIi11i1i1iI1 :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1i )
def i11i1IIi ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I111i1II )
 for url in iI111i :
  Oo0oiiiii11i ( url )
def Oo0oiiiii11i ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I111i1II )
 for url in iI111i :
  OOIi1iI111II1I1 ( url )
  if 65 - 65: oOo * iii1i1iiiiIi . ii - o0o00Oo0O * iii1i1iiiiIi % iii1i1iiiiIi
def OoooO0o ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IIo0o0O0O00oOOo , 8065 , I1IIIii + 'classicmovies.png' )
def IiiiIii ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( "v.src = '([^']*)';" ) . findall ( I111i1II )
 for url in iI111i :
  O00o0o ( url )
  if 67 - 67: iii1i1iiiiIi % ooo0O % oOoO0o00OO0 . oOo . IIiIiII11i + I11i1ii1
def IiIiIi1IIi ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IIo0o0O0O00oOOo , 8065 , I1IIIii + 'classictv.png' )
def IIi1Iii ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  if 'mp4' in url :
   OOIi1iI111II1I1 ( url )
 for url in IIi11i1i1iI1 :
  yt . PlayVideo ( url )
  if 21 - 21: oOoO0o00OO0 - OOOo00oo0oO * oOo
def oO00oOOOO ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iI111i = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + IIo0o0O0O00oOOo , 8071 , I1IIIii + 'streams.png' )
def o0o0OOO0ooo00 ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  if '(Free Access)' in O000OOO :
   url = ( url ) . strip ( )
  else :
   url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , I1IIIii + 'streams.png' )
def I11III111i1I ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , O000OOO , url in iI111i :
  url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , I1i , iI1iIii11Ii , '' )
  if 52 - 52: iiiiiiii1 % iI11I1II1I1I . oOoO0o00OO0 + OOOo00oo0oO % iiiiiiii1 * iiiiiiii1
def IIIiIIIi11I ( ) :
 oo0 = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  oO0OoooO ( 'http://watchxxxfree.com/categories' )
 if oOOOoo00 == 1 :
  I111iI1IIIi1I ( 'http://www.perfectgirls.net' )
 if oOOOoo00 == 2 :
  I1iii1IIi1I ( 'http://www.xvideos.com/best' )
 if oOOOoo00 == 3 :
  oO00O00OOOo ( 'http://www.xvideos.com/best' )
 if oOOOoo00 == 4 :
  I1iii1IIi1I ( 'http://www.xvideos.com/best' )
 if oOOOoo00 == 5 :
  I1iii1IIi1I ( 'http://www.xvideos.com/verified/videos' )
 if oOOOoo00 == 6 :
  Oo0o0oO00 ( 'http://www.xvideos.com/tags' )
 if oOOOoo00 == 7 :
  I1i1i1iiIi1 ( 'http://www.xvideos.com/porn' )
 if oOOOoo00 == 8 :
  OoOoo0ooO0000 ( )
  if 5 - 5: IIiIiII11i * i1IiiiI1iI
  if 21 - 21: oOo0O0Ooo
  if 70 - 70: I1ii11iIi11i + O0Oooo0O + OoOo0o . oOoO0o00OO0 - oOoO0o00OO0
  if 21 - 21: i1IiiiI1iI - OOOo00oo0oO
  if 55 - 55: iiiiiiii1 * I1ii11iIi11i + iii1i1iiiiIi * OoOo0o / iiiiiiii1 * ooOoO0O00
  if 49 - 49: I11i1ii1 + iI11I1II1I1I
  if 30 - 30: Ii % ooo0O . ooOoO0O00
  if 49 - 49: ooo0O * i1iIi + I1ii11iIi11i
  if 1 - 1: ooo0O / IIiIiII11i + i1IiiiI1iI . Ii + oOOoOooOo . iii1i1iiiiIi
def OO00i1i1Ii1iiII1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if 'ch' in url :
   Iii1i ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Jizbox.png' , I1IIIii + 'Jizbox.png' , '' )
def IIIII11IIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 i11I1iiI1iI = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , I1IIIii + 'Jizbox.png' , '' , '' )
 for O000OOO , url in i11I1iiI1iI :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Next.png' , '' , '' )
def i1i11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   OoOO0o000000 ( url )
def O0oooOOoOOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  OOIi1iI111II1I1 ( url )
def oO0OoooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , url , O000OOO , OoOooOo00O in iI111i :
  if 'category' in url :
   Iii1i ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORorange]   ' + OoOooOo00O + '[/COLOR]' , url , 90006 , I1i , I1IIIii + 'Jizbox.png' , '' )
def OoO0I1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 i11I1iiI1iI = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oOOo0 )
 for I1i , url , O000OOO in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , I1i , '' , '' )
 for url in i11I1iiI1iI :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , url , 90006 , I1IIIii + 'Next.png' , '' , '' )
def oo000oooooooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   OoOO0o000000 ( url )
def OoOO0o000000 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  OOIi1iI111II1I1 ( url )
def I111iI1IIIi1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , OoOooOo00O in iI111i :
  if 'category' in url :
   Iii1i ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORorange]' + OoOooOo00O + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , I1IIIii + 'Jizbox.png' , '' , '' )
def II1IIi1ii111 ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0Ooo = url
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 i11I1iiI1iI = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , I1i , '' , '' )
 for url in i11I1iiI1iI :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , O0Ooo + '/' + url , 90003 , I1IIIii + 'Next.png' , '' , '' )
def II1OO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'get\("(.*)", function' ) . findall ( oOOo0 )
 for url in iI111i :
  oo0OOO0O0 ( 'http://www.perfectgirls.net' + url )
def oo0OOO0O0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'http://(.+?)\n' ) . findall ( oOOo0 )
 for url in iI111i :
  I1iiIiiii1111 ( 'http://' + url )
def I1i1i1iiIi1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oOOo0 )
 for url , O000OOO , OoOooOo00O in iI111i :
  Iii1i ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgreen] - No of Videos : [COLORorange]' + OoOooOo00O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
def Oo0o0oO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 i11I1iiI1iI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in i11I1iiI1iI :
  Iii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , I1IIIii + 'Jizbox.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oOOo0 )
 for url , O000OOO , OoOooOo00O in iI111i :
  Iii1i ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgreen] - No of Videos : [COLORorange]' + ( OoOooOo00O + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
  if 99 - 99: ooOoO0O00 - o0o00Oo0O / IIiIiII11i + IIiIiII11i . I11i1ii1 / OOOo00oo0oO
def i1ii1iIiI1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 i11I1iiI1iI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in i11I1iiI1iI :
  Iii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , url , O000OOO , O0Oo0O0O0o in iI111i :
  Iii1i ( O000OOO + '--' + ( O0Oo0O0O0o ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( I1i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 17 - 17: Ii . i1iIi - I11i1ii1 / iI11I1II1I1I + ii - oOOoOooOo
  if 59 - 59: iii1i1iiiiIi
def I1iii1IIi1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , url , O000OOO , I1I , O0OOoOOO0o0o in iI111i :
  Iii1i ( '[COLORorangered]' + O000OOO + '[COLORgreen] - Porn Quality : [COLORorange]' + I1I + ' - [COLORred]' + O0OOoOOO0o0o + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , I1i , I1i , I1I + ' - ' + O0OOoOOO0o0o )
 ooOOO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for I1i , url , O000OOO , O0OOoOOO0o0o in IIi11i1i1iI1 :
  Iii1i ( '[COLORorangered]' + O000OOO + '[COLORgreen] - Porn Quality : [COLORorange]' + O0OOoOOO0o0o + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , I1i , I1i , O0OOoOOO0o0o )
 ooOOO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in ooOOO :
  Iii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Next.png' , '' , '' )
  if 62 - 62: i1iIi
  if 4 - 4: iI11I1II1I1I . I1ii11iIi11i - Ii
def oO00O00OOOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0ooooo0OOOO0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 i11I1iiI1iI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in i11I1iiI1iI :
  Iii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O0ooooo0OOOO0 ) )
 for url , O000OOO in iI111i :
  if '/c/' in url :
   Iii1i ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
   if 51 - 51: iii1i1iiiiIi - Ii / oOo0O0Ooo % i1iIi * i1iIi % oOOoOooOo
   if 12 - 12: oOOoOooOo % iii1i1iiiiIi
def OoOoo0ooO0000 ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii11o0ooOoOoO0o = ( oOoooO00O ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 ooO0000o00O = ii11o0ooOoOoO0o . lower ( )
 Ii1I11IIi1 = 'http://www.xvideos.com/?k=' + ooO0000o00O
 print Ii1I11IIi1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOo0 = i11111IIIII ( Ii1I11IIi1 )
 iI111i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , IIo0o0O0O00oOOo , O000OOO , O0OOoOOO0o0o , OOo00OoOoo in iI111i :
  Iii1i ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgreen] - Porn Quality : [COLORorange]' + OOo00OoOoo + ' - [COLORred]' + O0OOoOOO0o0o + '[/COLOR]' , 'http://www.xvideos.com' + IIo0o0O0O00oOOo , 10108 , I1i , I1i , OOo00OoOoo + ' - ' + O0OOoOOO0o0o )
 ooOOO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in ooOOO :
  Iii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + IIo0o0O0O00oOOo , 10105 , I1IIIii + 'Next.png' , '' , '' )
if 65 - 65: O0Oooo0O . o0o00Oo0O + iii1i1iiiiIi
if 82 - 82: oOOoOooOo . O0Oooo0O . I1ii11iIi11i % iI11I1II1I1I - Ii
if 11 - 11: oOOoOooOo . O0Oooo0O - iiiiiiii1 . ooo0O
if 41 - 41: OOOo00oo0oO / oOo - oOo + oOOoOooOo * OoOo0o
if 13 - 13: O0Oooo0O * IIiIiII11i - iii1i1iiiiIi
if 3 - 3: OoOo0o + oOOoOooOo * Ii . iiiiiiii1 / iI11I1II1I1I
if 44 - 44: oOo
if 74 - 74: i1iIi * ooOoO0O00 * i1IiiiI1iI - ii . oOo0O0Ooo
if 24 - 24: IIiIiII11i - Ii * ooOoO0O00 . oOOoOooOo
if 42 - 42: i1IiiiI1iI / Ii
if 7 - 7: i1IiiiI1iI
if 50 - 50: Ii . Ii * ooOoO0O00 / Ii . ooOoO0O00 - IIiIiII11i
if 72 - 72: iI11I1II1I1I / ooo0O . oOoO0o00OO0
if 78 - 78: iI11I1II1I1I . Ii % I11i1ii1 * i1iIi + iiiiiiii1 - iI11I1II1I1I
if 50 - 50: oOoO0o00OO0 % i1iIi - i1IiiiI1iI % I1ii11iIi11i - i1IiiiI1iI - oOo0O0Ooo
if 99 - 99: I11i1ii1 * iii1i1iiiiIi - ooOoO0O00 / O0Oooo0O . oOOoOooOo % ooo0O
if 69 - 69: o0o00Oo0O . iiiiiiii1
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
if 100 - 100: IIiIiII11i
if 16 - 16: i1iIi
if 96 - 96: ooo0O / O0Oooo0O % i1iIi - oOOoOooOo
if 35 - 35: OoOo0o
if 90 - 90: Ii
if 47 - 47: oOo . Ii
if 9 - 9: iii1i1iiiiIi - i1IiiiI1iI . ii % oOOoOooOo
if 13 - 13: oOo * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - iii1i1iiiiIi
def I111 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oOOo0 )
 OoOOo0OOoO = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  if 'http' in url :
   Oo ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in IIi11i1i1iI1 :
  if 'http' in url :
   Oo ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in OoOOo0OOoO :
  if 'http' in url :
   Oo ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
   if 76 - 76: oOOoOooOo % oOo0O0Ooo
def i11i1iI ( url ) :
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 import urlresolver
 try : o0000o0Oo . play ( url )
 except : pass
 if 34 - 34: iii1i1iiiiIi
 if 75 - 75: i1IiiiI1iI / iI11I1II1I1I + oOoO0o00OO0 / oOo
def i111 ( ) :
 if 13 - 13: I1ii11iIi11i * ooo0O * iiiiiiii1
 if 71 - 71: OoOo0o + ii + iI11I1II1I1I
 if 99 - 99: oOo - I11i1ii1 * I11i1ii1 + OOOo00oo0oO / iiiiiiii1 + OoOo0o
 if 58 - 58: Ii + iI11I1II1I1I * ooo0O - iii1i1iiiiIi
 if 31 - 31: ooOoO0O00
 if 87 - 87: oOo0O0Ooo / i1IiiiI1iI + ii + o0o00Oo0O . i1iIi
 if 44 - 44: I1ii11iIi11i % I1ii11iIi11i
 if 58 - 58: OoOo0o * IIiIiII11i
 if 29 - 29: iI11I1II1I1I % iii1i1iiiiIi % oOoO0o00OO0 / iii1i1iiiiIi - Ii
 if 67 - 67: OoOo0o / i1iIi
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 8091 , I1IIIii + 'gofish.png' )
def O0Oo0O0O0o0 ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , I1i in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 8092 , I1i )
 for url in next :
  o0OO ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
def Oo0ooo0oOo0Oo0O ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 II1ii1iI1I1i = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oOOo0 )
 for I1i in II1ii1iI1I1i :
  I1i = I1i
 for url , O000OOO in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 8092 , I1i )
 for url in next :
  o0OO ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
  if 9 - 9: ooOoO0O00 * O0Oooo0O
def i11oO0oOO000 ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( "videoId: '([^']*)'," ) . findall ( oOOo0 )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 69 - 69: o0o00Oo0O % o0o00Oo0O - iiiiiiii1 - OOOo00oo0oO
  if 83 - 83: Ii + iI11I1II1I1I
  if 21 - 21: ooo0O / Ii % O0Oooo0O
  if 56 - 56: ooo0O * iI11I1II1I1I . i1iIi + iii1i1iiiiIi % O0Oooo0O
iiI1i111I1 = '{PQ},' ; iiIi11i1I1 = '{SC},' ; o0OoO0 = '{XG},' ; I11Ii1I1I = '{JP},' ; oo00OO0o0 = '{HW},' ; o0oo0000Oo = '{RT},'
def Ii1I11I ( ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 i1i1iiIIiiiII = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 IIo0o0O0O00oOOo = 'http://onlinemovies.tube/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 O0Ooo = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OO0ooO0 = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OoOooOO0oOOo0O = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1II = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIi1Ii1III = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOoooO00O
 Oooo00 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iii1II1iI1IIi = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 93 - 93: oOOoOooOo + oOOoOooOo
 i1I111Ii = ( o0oOoO00o ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 i11i1i = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 65 - 65: ii * i1IiiiI1iI * OOOo00oo0oO % oOoO0o00OO0 * IIiIiII11i
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 oo00O00oO = i1Oo00 ( O0Ooo )
 o0oO0 . update ( 14 , "" , "Checking Source Technica " )
 OOooO0Oo00 = i1Oo00 ( O0Ooo )
 o0oO0 . update ( 32 , "" , "Checking Source Pandoras Box " )
 iIiIIIi = i1Oo00 ( Ii1I1 )
 o0oO0 . update ( 59 , "" , "Checking Source Lazy List " )
 ooo00OOOooO = i1Oo00 ( OO0ooO0 )
 o0oO0 . update ( 72 , "" , "Checking Source RaizTv " )
 iIIIIIIIiIII = i1Oo00 ( iii1II1iI1IIi )
 o0oO0 . update ( 91 , "" , "Checking WebSpace " )
 I1oOoO0OOO00O = i1Oo00 ( i11i1i )
 o0oO0 . update ( 97 , "" , "Matching Results" )
 if 86 - 86: Ii / i1IiiiI1iI * iiiiiiii1 - iiiiiiii1
 if iIIIIIIIiIII != 'Failed' :
  i1i1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIIIIiIII )
  for IIo0o0O0O00oOOo , O000OOO in i1i1 :
   o0oOoOo0 = i1Oo00 ( IIo0o0O0O00oOOo )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , iIIIiIi in III1IiI1i1i :
    iIIIiIi = ( iIIIiIi . replace ( '.' , ' ' ) )
    if ooO0000o00O in iIIIiIi . lower ( ) :
     if '.mkv' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.mp4' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.avi' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + o0OOOOOo0 , 222 , '' , '' , '' )
     elif '.wav' in o0OOOOOo0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + o0OOOOOo0 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + o0OOOOOo0 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting WebSpace Links" )
      if 32 - 32: I1ii11iIi11i . o0o00Oo0O
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in IIi11i1i1iI1 :
   if oOoooO00O in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source Technica[/COLOR]' ) , IIo0o0O0O00oOOo , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 48 - 48: oOoO0o00OO0 % IIiIiII11i + i1IiiiI1iI
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: I11i1ii1 * ooo0O / oOo0O0Ooo . I11i1ii1 % IIiIiII11i
 if iIiIIIi != 'Failed' :
  OoOOo0OOoO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for IiI11I111 , O000OOO in OoOOo0OOoO :
   if oOoooO00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1I1 + IiI11I111 ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Lazy List Links" )
 if ooo00OOOooO != 'Failed' :
  ooO0O00Oo0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in ooO0O00Oo0o :
   if oOoooO00O in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source RaizTv[/COLOR]' ) , IIo0o0O0O00oOOo , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 50 - 50: iii1i1iiiiIi * iiiiiiii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 Oooooooo00o00 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + '/Movies/a.to.z/' + III1II1i + '.php'
  iIIIIIIIiIII = i1Oo00 ( iI1i1IiIIIIi )
  if iIIIIIIIiIII != 'Failed' :
   i1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIIIIIiIII )
   for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in i1i1 :
    if oOoooO00O in O000OOO . lower ( ) :
     if '.php' in IIo0o0O0O00oOOo :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      o00oOOooOOo0o ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 426 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
     else :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      Oo00oOOO0 ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
      if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / i1IiiiI1iI
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
      if 92 - 92: ooo0O
 Oooooooo00o00 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 8 - 8: iiiiiiii1 + oOoO0o00OO0 . i1iIi
 if 50 - 50: I1ii11iIi11i
 for III1II1i in Oooooooo00o00 :
  iI1i1IiIIIIi = i1i1iiIIiiiII + III1II1i
  III1I1Iii11i = i1Oo00 ( iI1i1IiIIIIi )
  if III1I1Iii11i != 'Failed' :
   Oo0o00OO0000 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( III1I1Iii11i )
   for IiI11I111 , O000OOO in Oo0o00OO0000 :
    if oOoooO00O in O000OOO . lower ( ) :
     Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1i1iiIIiiiII + III1II1i + IiI11I111 ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 16 - 16: i1iIi - iii1i1iiiiIi % I1ii11iIi11i / i1iIi . i1IiiiI1iI + oOOoOooOo
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 78 - 78: iI11I1II1I1I + oOo + Ii
def IIiiIIi1 ( ) :
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
 if 51 - 51: OoOo0o - ii / ii % ii
 if 85 - 85: oOo . ooo0O . oOo0O0Ooo
 if 75 - 75: iI11I1II1I1I - i1iIi % o0o00Oo0O % I11i1ii1
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 if 6 - 6: I1ii11iIi11i % OOOo00oo0oO * oOOoOooOo - ooOoO0O00 . iii1i1iiiiIi
 if 20 - 20: I1ii11iIi11i / O0Oooo0O . I1ii11iIi11i
 o0OOOOOo0 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oOoooO00O ) . replace ( ' ' , '+' )
 O0Ooo = 'http://onlinemovies.tube/?s=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OO0ooO0 = ( o0oOoO00o ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1II = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 iIIi1Ii1III = 'http://www.tvmaze.com/search?q=' + ( oOoooO00O ) . replace ( ' ' , '+' )
 Oooo00 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iii1II1iI1IIi = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 60 - 60: oOoO0o00OO0 - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . iii1i1iiiiIi
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 24 - 24: I11i1ii1 * oOo0O0Ooo / OoOo0o
 o0oO0 . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 51 - 51: iI11I1II1I1I / i1IiiiI1iI * oOo * i1iIi + oOoO0o00OO0 . ii
 if 75 - 75: I11i1ii1 / ii / o0o00Oo0O % OoOo0o
 iiIIi1 = i1Oo00 ( o0OOOOOo0 )
 o0oO0 . update ( 14 , "" , "Checking Source 3/11 Links" )
 oo00O00oO = i1Oo00 ( O0Ooo )
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
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % oOoO0o00OO0
 if 11 - 11: ooo0O * oOo
 if iIIIIIIIiIII != 'Failed' :
  i1i1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIIIIiIII )
  for IIo0o0O0O00oOOo , O000OOO in i1i1 :
   o0oOoOo0 = i1Oo00 ( IIo0o0O0O00oOOo )
   III1IiI1i1i = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o0oOoOo0 )
   for o0OOOOOo0 , iIIIiIi in III1IiI1i1i :
    if ooO0000o00O in iIIIiIi . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + o0OOOOOo0 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 92 - 92: iii1i1iiiiIi . I1ii11iIi11i * i1IiiiI1iI
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if OOooO0Oo00 != 'Failed' :
  OoO0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOooO0Oo00 )
  for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in OoO0O :
   if ooO0000o00O in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source HeroVision[/COLOR]' ) , IIo0o0O0O00oOOo , 1016 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 10 , "" , "Getting Herovision Links" )
    if 86 - 86: o0o00Oo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: i1iIi / O0Oooo0O / oOoO0o00OO0 % oOOoOooOo % oOo0O0Ooo
 if O0OOOOo0 != 'Failed' :
  o00Oo0oooooo = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( O0OOOOo0 )
  for IIo0o0O0O00oOOo , I1i , O000OOO in o00Oo0oooooo :
   O0Ooo = 'http://www.tvmaze.com' + IIo0o0O0O00oOOo . replace ( '"' , '' )
   oO00oOOo0Oo = requests . get ( O0Ooo ) . content
   iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oO00oOOo0Oo )
   for IIIIiii1IIii in iI111i :
    if not '<div>' in IIIIiii1IIii :
     IIi = IIIIiii1IIii . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
    I1i = 'http:' + I1i
    O000OOO = O000OOO . replace ( '&#039;' , '' )
    if O000OOO == '' :
     IIIIii = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( IIo0o0O0O00oOOo ) )
     for O000OOO in IIIIii :
      O000OOO = O000OOO . replace ( '-' , ' ' )
   iiIi1iI1iIii ( O000OOO + '-[COLORgold] source Scraper[/COLOR]' , O0Ooo , 9110002 , I1i , Oo00OOOOO , IIi , '' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 20 , "" , "Getting Scraper Links" )
   if 55 - 55: OOOo00oo0oO + ii % ooOoO0O00
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  II11ii1I11 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for IIo0o0O0O00oOOo , I1i , O000OOO , o0oO00o in IIi11i1i1iI1 :
   if ooO0000o00O in O000OOO . lower ( ) :
    if 'season' in o0oO00o :
     o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , IIo0o0O0O00oOOo , 90054 , I1i , I1i , '' )
    if 'episodes' in o0oO00o :
     o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , IIo0o0O0O00oOOo , 90044 , I1i , I1i , '' )
  for IIo0o0O0O00oOOo in II11ii1I11 :
   o0OO ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , IIo0o0O0O00oOOo , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 24 - 24: oOoO0o00OO0 - I1ii11iIi11i
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iiIIi1 != 'Failed' :
  oOOoo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iiIIi1 )
  for IIo0o0O0O00oOOo , O000OOO , I1i in oOOoo :
   if ooO0000o00O in O000OOO . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( O000OOO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , IIo0o0O0O00oOOo , 8022 , I1i , '' , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 45 , "" , "Getting Source iWatch Links" )
    if 36 - 36: oOo0O0Ooo . OoOo0o % IIiIiII11i * I11i1ii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iIiIIIi != 'Failed' :
  OoOOo0OOoO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for O000OOO in OoOOo0OOoO :
   if ooO0000o00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Ii1I1 + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 34 - 34: i1IiiiI1iI % iiiiiiii1 - oOOoOooOo - oOo0O0Ooo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  ooO0O00Oo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for O000OOO in ooO0O00Oo0o :
   if ooO0000o00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OO0ooO0 + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 44 - 44: i1iIi . ooo0O . iI11I1II1I1I + ii - oOo0O0Ooo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if III1I1Iii11i != 'Failed' :
  Oo0o00OO0000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III1I1Iii11i )
  for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in Oo0o00OO0000 :
   if ooO0000o00O in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] Source Scooby[/COLOR]' ) , IIo0o0O0O00oOOo , 1016 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 90 , "" , "Getting Scooby Links" )
    if 22 - 22: i1IiiiI1iI * oOoO0o00OO0 . ii / I1ii11iIi11i / i1iIi
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 54 - 54: O0Oooo0O % i1iIi + oOOoOooOo
 O0oooOO0Oo0o = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for III1II1i in O0oooOO0Oo0o :
  iI1i1IiIIIIi = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + III1II1i + '.php'
  iiiI1iI1 = i1Oo00 ( iI1i1IiIIIIi )
  if iiiI1iI1 != 'Failed' :
   IIIiI1iiiiiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iiiI1iI1 )
   for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in IIIiI1iiiiiIi :
    if oOoooO00O in O000OOO . lower ( ) :
     if '.php' in IIo0o0O0O00oOOo :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      o00oOOooOOo0o ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 426 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
     else :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      Oo00oOOO0 ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 222 , i1i1II1i11 , i1iIIi1II1iiI , IIIIiii1IIii )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
      if 45 - 45: i1iIi / OOOo00oo0oO * O0Oooo0O . i1iIi
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
      if 25 - 25: oOoO0o00OO0 / oOoO0o00OO0
      if 79 - 79: I1ii11iIi11i - oOo % I1ii11iIi11i . IIiIiII11i
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0Ooo0Oooo0o ( ) :
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0o0O0O00oOOo = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( oOoooO00O ) . replace ( ' ' , '+' )
 if 22 - 22: OOOo00oo0oO / IIiIiII11i . iii1i1iiiiIi
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oO0 . update ( 0 , "" , "Checking Source Links" )
 oOOo0 = i1Oo00 ( IIo0o0O0O00oOOo )
 o0oO0 . update ( 100 , "" , "Checking Source Links" )
 if 9 - 9: Ii + oOOoOooOo . iI11I1II1I1I * iii1i1iiiiIi
 if oOOo0 != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , O000OOO in IIi11i1i1iI1 :
   if oOoooO00O in O000OOO . lower ( ) :
    Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + IIo0o0O0O00oOOo ) , 222 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 4 - 4: O0Oooo0O + iiiiiiii1 % o0o00Oo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
OoO0oO = '{ZH},' ; ii1I1 = '{IX},' ; ooOo0OooOooo = '{LM},'
if 35 - 35: O0Oooo0O / ii / I11i1ii1 + iii1i1iiiiIi - O0Oooo0O + Ii
def ooOoo ( url ) :
 iIII1 = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iIII1 )
 for url , o0O0 , I1I1Iiii1 , O000OOO in iI111i :
  o0OO ( ( o0O0 ) . replace ( 'Sezon' , ' Season ' ) + ( I1I1Iiii1 ) . replace ( 'Bölüm' , ' Episode ' ) + O000OOO , url , 8063 , '' )
  if 84 - 84: ii - ii / I11i1ii1
  if 29 - 29: i1iIi / o0o00Oo0O
  if 50 - 50: i1iIi + i1iIi
  if 51 - 51: oOoO0o00OO0 / ii * I11i1ii1
def o0oOII1i ( url ) :
 iIII1 = cloudflare . source ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iIII1 )
 for url , O000OOO in iI111i :
  Oo ( O000OOO , url , 222 , '' )
  if 66 - 66: oOo0O0Ooo . oOo0O0Ooo - iii1i1iiiiIi * ii * IIiIiII11i + oOo0O0Ooo
  if 59 - 59: i1iIi
  if 59 - 59: IIiIiII11i - oOo
  if 31 - 31: i1IiiiI1iI - iii1i1iiiiIi / ooo0O * iii1i1iiiiIi / I1ii11iIi11i + ooo0O
def I1iII1IiI11i ( ) :
 if 66 - 66: I1ii11iIi11i . OOOo00oo0oO - o0o00Oo0O . O0Oooo0O + iiiiiiii1 / Ii
 iIII1 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIII1 )
 for IIo0o0O0O00oOOo , I1i , O000OOO , I1I1Iiii1 in iI111i :
  o0OO ( O000OOO + '  -  ' + ( I1I1Iiii1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IIo0o0O0O00oOOo , 8063 , I1i )
  if 52 - 52: OOOo00oo0oO % I1ii11iIi11i * IIiIiII11i
def ii1iiiIIiIII ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO , I1i in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 8002 , I1i )
def i1i1iiI11I ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I111i1II )
 for I1i , time , url , O000OOO , OOO00OiI in iI111i :
  o00oOOooOOo0o ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , time ) , url , 1015 , I1i , OOO00OiI )
  if 78 - 78: iii1i1iiiiIi % oOo - i1iIi / OoOo0o
def ooOo000 ( ) :
 if 87 - 87: I1ii11iIi11i + oOo0O0Ooo % oOo0O0Ooo * Ii
 o0OO ( 'Coronation Street' , '' , 8001 , '' )
 o0OO ( 'Eastenders' , '' , 8002 , '' )
 o0OO ( 'Emmerdale' , '' , 8003 , '' )
 o0OO ( 'Hollyoaks' , '' , 8004 , '' )
 o0OO ( 'Im a Celebrity' , '' , 8005 , '' )
 if 68 - 68: iiiiiiii1 . OoOo0o
 if 6 - 6: i1iIi - ooo0O % i1IiiiI1iI + Ii
 if 40 - 40: o0o00Oo0O . i1iIi
 if 58 - 58: Ii * iiiiiiii1 / i1iIi - OOOo00oo0oO - oOoO0o00OO0 % ooo0O
def i11Oo00 ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Holly' in O000OOO :
   I1i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in IIo0o0O0O00oOOo :
    Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , I1i )
   else :
    pass
    if 54 - 54: IIiIiII11i / IIiIiII11i + i1IiiiI1iI . OoOo0o - OoOo0o
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 98 - 98: i1iIi
def oOoo0OOoOoO0O ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'East' in O000OOO :
   I1i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , I1i )
   else :
    pass
    if 1 - 1: ii - oOOoOooOo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: IIiIiII11i % iiiiiiii1 % i1iIi % iiiiiiii1 % i1IiiiI1iI . iI11I1II1I1I
def IIoo0O ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Emmer' in O000OOO :
   I1i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , I1i )
   else :
    pass
    if 87 - 87: iI11I1II1I1I * IIiIiII11i - O0Oooo0O % O0Oooo0O - OoOo0o
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: O0Oooo0O
def oOI1 ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Coro' in O000OOO :
   I1i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , I1i )
   else :
    pass
    if 21 - 21: ooo0O - oOOoOooOo * ii . ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: OoOo0o - iiiiiiii1 % oOo0O0Ooo * OoOo0o * iI11I1II1I1I . ooo0O
def oOOooOOO ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Celeb' in O000OOO :
   I1i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , I1i )
   else :
    pass
    if 12 - 12: I11i1ii1 * iii1i1iiiiIi / Ii + Ii
def iII11I11i ( name , url ) :
 IIIII1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIIII1 :
  i1iI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I111i1II = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I111i1II ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I111i1II = open_url ( url )
  oOOoo00Oo = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I111i1II ) [ - 1 ]
  i1iI = oOOoo00Oo . replace ( '\\/' , '/' )
 o0OoOo00ooO = xbmcgui . ListItem ( name , '' , '' )
 o0OoOo00ooO . setPath ( i1iI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOo00ooO )
 if 19 - 19: oOo - i1IiiiI1iI % I1ii11iIi11i / Ii % IIiIiII11i * I1ii11iIi11i
 if 14 - 14: Ii % OoOo0o + ooo0O + ooo0O . oOo
def I111i1IiI1 ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iI111i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , IIo0o0O0O00oOOo , 7071 , I1IIIii + 'popcorn.png' )
 for IIo0o0O0O00oOOo , O000OOO in IIi11i1i1iI1 :
  o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , IIo0o0O0O00oOOo , 7071 , I1IIIii + 'popcorn.png' )
  if 46 - 46: IIiIiII11i - oOo % oOOoOooOo
def oOIIIiIII111iii ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Movies' in O000OOO :
   o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( IIo0o0O0O00oOOo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , I1IIIii + 'popcorn.png' )
def oOOiI ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I111i1II )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I111i1II )
 for url , I1i , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1i )
 for url in IIi11i1i1iI1 :
  o0OO ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , I1IIIii + 'Next.png' )
  if 94 - 94: I11i1ii1 / oOOoOooOo + O0Oooo0O * OoOo0o
  if 16 - 16: oOOoOooOo - ooOoO0O00 - i1IiiiI1iI % I1ii11iIi11i * i1IiiiI1iI - iii1i1iiiiIi
def IiiIi11 ( url ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , url , I1i in iI111i :
  if '{{' in O000OOO :
   pass
  else :
   o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I1i )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
OoOI1I = '{UJ},' ; Ii111Ii11I111Ii = '{WE},' ; iIiIIiIII1I = '{WP},' ; Ii1i1IiiIiIII = '{PP},'
def Oo0O0O000 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , url , I1i in iI111i :
  if '{{' in O000OOO :
   pass
  else :
   o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1i )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOO0oOo0OOoOO ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  o0O00oo0Ooo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O00oo0Ooo ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: ii
 if 67 - 67: Ii + iii1i1iiiiIi
 if 50 - 50: oOOoOooOo . ooOoO0O00 + oOoO0o00OO0 . OoOo0o
def oO0Ooo ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  if '(cooltvseries.com)' in O000OOO :
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
 for url , O000OOO in IIi11i1i1iI1 :
  if '(cooltvseries.com)' in O000OOO :
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
def iiiiIIiiII1Iii1 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I111i1II )
 for url in iI111i :
  I1iiIiiii1111 ( ( url ) . replace ( ' ' , '%20' ) )
OOo0O0O000 = '{XX},' ; o0oOOoO0o0 = '{UD},' ; oOOo0o0O0oO0o = '{YT},' ; iiIi = '{JS},' ; oo0O0 = '{PF},'
if 55 - 55: Ii % ooOoO0O00
def I1iI1II1I1i ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iI111i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO , I1i in iI111i :
  Oo ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( o0oOoO00o ( IIo0o0O0O00oOOo ) ) , 222 , I1i )
  if 45 - 45: oOo0O0Ooo . oOo0O0Ooo - I1ii11iIi11i * OoOo0o
def oO0iII1i111iI ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( I111i1II )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I111i1II )
 for I1i , url , O000OOO in iI111i :
  if 'youtu' in url :
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + I1i )
 for url in next :
  o0OO ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , I1IIIii + 'Next.png' )
  if 71 - 71: ooOoO0O00 / i1IiiiI1iI
def i1i1O0 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 44 - 44: i1IiiiI1iI
def i1i1O0 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 61 - 61: oOoO0o00OO0 * OoOo0o . iI11I1II1I1I
def o0O00oo0oOoO ( url ) :
 I111i1II = i11111IIIII
 iI111i = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 for url , I1i , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1i )
  if 28 - 28: ii . ii + iI11I1II1I1I
  if 60 - 60: iii1i1iiiiIi / oOOoOooOo % iI11I1II1I1I
  if 32 - 32: Ii + IIiIiII11i + IIiIiII11i % i1IiiiI1iI
  if 96 - 96: ooo0O
  if 90 - 90: I11i1ii1 * i1iIi . i1IiiiI1iI / oOoO0o00OO0 % i1IiiiI1iI
def o00oOo0O0O0 ( ) :
 if 14 - 14: oOo0O0Ooo % iii1i1iiiiIi . oOoO0o00OO0
 o0OO ( 'All Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Entertainment' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Movies' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Music' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'News' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Sports' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Documentary' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Kids' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Food' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Religious' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'USA Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 o0OO ( 'Other' , '' , 7021 , I1IIIii + 'livetv.png' )
 if 45 - 45: oOo + oOo0O0Ooo
 if 82 - 82: I1ii11iIi11i . Ii + Ii
def OOoI1I ( Cat_Name ) :
 if 60 - 60: i1IiiiI1iI . iI11I1II1I1I - OOOo00oo0oO . OoOo0o + iii1i1iiiiIi % I1ii11iIi11i
 IiIiiIi1I1Iii1 = False
 Oo0ooOoo = '0'
 if Cat_Name == 'All Channels' : IiIiiIi1I1Iii1 = True
 if Cat_Name == 'Entertainment' : Oo0ooOoo = '1'
 if Cat_Name == 'Movies' : Oo0ooOoo = '2'
 if Cat_Name == 'Music' : Oo0ooOoo = '3'
 if Cat_Name == 'News' : Oo0ooOoo = '4'
 if Cat_Name == 'Sports' : Oo0ooOoo = '5'
 if Cat_Name == 'Documentary' : Oo0ooOoo = '6'
 if Cat_Name == 'Kids' : Oo0ooOoo = '7'
 if Cat_Name == 'Food' : Oo0ooOoo = '8'
 if Cat_Name == 'Religious' : Oo0ooOoo = '9'
 if Cat_Name == 'USA Channels' : Oo0ooOoo = '10'
 if Cat_Name == 'Other' : Oo0ooOoo = '11'
 if 57 - 57: oOo0O0Ooo - ooOoO0O00 + iiiiiiii1 * I1ii11iIi11i % oOo
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I111i1II )
 print 'Len Match: >>>' + str ( len ( iI111i ) )
 for O000OOO , I1i , OoOOoOo0O0 in iI111i :
  oOo0oO0 = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1i ) . replace ( '\\' , '' )
  if OoOOoOo0O0 == Oo0ooOoo :
   o0OO ( O000OOO , '' , 7022 , oOo0oO0 )
  elif IiIiiIi1I1Iii1 == True :
   o0OO ( O000OOO , '' , 7022 , oOo0oO0 )
  else : pass
  if 2 - 2: o0o00Oo0O % ooo0O
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 3 - 3: Ii / OoOo0o + OOOo00oo0oO
def iIIiii ( Search_Name ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I111i1II )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I111i1II )
 for I1i , IIo0o0O0O00oOOo , O0Ooo , Ii1I1 in iI111i :
  oOo0oO0 = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1i ) . replace ( '\\' , '' )
  Oo ( Search_Name + ': Link 1' , ( IIo0o0O0O00oOOo ) . replace ( '\\' , '' ) , 222 , oOo0oO0 )
  Oo ( Search_Name + ': Link 2' , ( O0Ooo ) . replace ( '\\' , '' ) , 222 , oOo0oO0 )
  Oo ( Search_Name + ': Link 3' , ( Ii1I1 ) . replace ( '\\' , '' ) , 222 , oOo0oO0 )
  if 25 - 25: IIiIiII11i + i1IiiiI1iI
def Oo000O ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  Oo ( O000OOO , ( IIo0o0O0O00oOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , I1IIIii + 'english.png' )
def I1iOO000Ooo ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  Oo ( O000OOO , ( IIo0o0O0O00oOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'xxx.png' )
def OoOooo0ooo0O ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I111i1II )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  Oo ( O000OOO , ( IIo0o0O0O00oOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'vod(1).png' )
  if 48 - 48: ooOoO0O00 - OOOo00oo0oO . ii - oOo - ooOoO0O00
def III1iI1ii1 ( url ) :
 url
 Ii1II1I11i1 = xbmcgui . ListItem ( O000OOO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1II1I11i1 )
 return
 if 93 - 93: iiiiiiii1 % O0Oooo0O
 if 90 - 90: oOoO0o00OO0 - ii / iii1i1iiiiIi
def I11ooOo ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']All WorkOuts[/COLOR]' , o0oOoO00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) , 7085 , I1IIIii + 'Fitness.png' , Oo00OOOOO , '' )
 if 100 - 100: OOOo00oo0oO
def IiiiIII1 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '"id":.+?,"title":(.+?),"is_featured":1,"minutes":(.+?),"burnmin":(.+?),"burnmax":(.+?),"burnavg":(.+?),"difficulty":(.+?),"image":"([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( '"next_page_url":"([^"]*)"' ) . findall ( I111i1II )
 for O000OOO , time , Iii11 , iII1Ii1ii111 , iII11IIi1I1 , o00o0o , I1i , url , ooOoOooO0oo0o00O0 , oO00Oo0 in iI111i :
  o00oOOooOOo0o ( ( O000OOO ) . replace ( '"' , '' ) , 'https://www.fitnessblender.com/videos/' + url , 7086 , 'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-' + I1i , '' , ( 'Calorie burn:[CR]' + Iii11 + ' - ' + iII1Ii1ii111 + ' Average = ' + iII11IIi1I1 + '[CR][CR]Difficulty = ' + o00o0o + '[CR][CR]Equipment Needed: ' + ooOoOooO0oo0o00O0 + '[CR][CR]Focus: ' + oO00Oo0 ) . replace ( '"' , '' ) )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
 for url in IIi11i1i1iI1 :
  o0OO ( 'NEXT' , ( 'https://www.fitnessblender.com/videos' + url ) . replace ( '\/' , '' ) , 7085 , I1IIIii + 'Next.png' )
  if 25 - 25: OoOo0o % iiiiiiii1 + iiiiiiii1
def IIiIiOOoO ( url , iconimage , description ) :
 oOOo0 = i11111IIIII ( url )
 I1i = iconimage
 IIIIiii1IIii = description
 iI111i = re . compile ( '<div class="responsive-video">.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  O0O0ooOOO ( 'PLAY' , url , 8043 , I1i , '' , IIIIiii1IIii )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
 ooOoo00OoO00 = re . compile ( '<div class="article__content">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OoO0OO in ooOoo00OoO00 :
  iiI1Ii1 = ( O000OoO0OO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o00oOOooOOo0o ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I1i , '' , iiI1Ii1 )
  if 63 - 63: I11i1ii1 / oOoO0o00OO0
def o0OoooO0oo0 ( INFO ) :
 OoOoO ( 'info for workout' , INFO )
 if 59 - 59: OoOo0o - O0Oooo0O - IIiIiII11i / ooOoO0O00 * OoOo0o . ii
 if 46 - 46: I11i1ii1 * ii . ooo0O - O0Oooo0O * oOo0O0Ooo
 if 83 - 83: I1ii11iIi11i . ooo0O + iiiiiiii1 + ooo0O % iI11I1II1I1I * iii1i1iiiiIi
def OOoo00o0 ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  o0OO ( ( O000OOO ) . replace ( 'SlyNet' , '' ) , url , 9031 , I1IIIii + 'Sport.png' )
def o0OO0iI1II1i1ii ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  o0OO ( O000OOO , url , 9032 , I1IIIii + 'icon.png' )
def OOooOOooo000OoO ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , url in iI111i :
  if '=' in O000OOO :
   pass
  else :
   Oo ( ( O000OOO ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , I1IIIii + 'icon.png' )
def O0OOo ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I111i1II )
 for O000OOO , url in iI111i :
  if '=' in O000OOO :
   pass
  else :
   Oo ( O000OOO , url , 222 , I1IIIii + 'icon.png' )
   if 97 - 97: Ii + o0o00Oo0O
   if 53 - 53: oOo % iI11I1II1I1I - OoOo0o
   if 36 - 36: oOo0O0Ooo + I11i1ii1 . I11i1ii1
def IIii1iI11 ( url ) :
 iiIi1iI1iIii ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , I1i , url in iI111i :
  if 'music' in url :
   iiIi1iI1iIii ( O000OOO , url , 90036 , I1i , I1i , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   iiIi1iI1iIii ( O000OOO , url , 90039 , I1i , I1i , '' , '' )
def I111I1IiI1i1 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( I111i1II )
 for O000OOO , url , I1i in iI111i :
  iii11i1IIII ( O000OOO , url , 100009 , I1i , I1i , '' , '' )
  if 52 - 52: i1iIi / Ii / OOOo00oo0oO
def o00o0o0O0 ( url ) :
 iiIi1iI1iIii ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 I111i1II = requests . get ( url ) . text
 OoOIiiiii111i1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I111i1II )
 O0ooooo0OOOO0 = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I111i1II )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O0ooooo0OOOO0 ) )
 for url , I1i , O000OOO in iI111i :
  oO00oOOo0Oo = requests . get ( url ) . text
  i1II1IiiiIii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( oO00oOOo0Oo )
  for i1I1 in i1II1IiiiIii :
   OO0oo0O0OOO0 = requests . get ( i1I1 ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OO0oo0O0OOO0 )
   for iiI11Iii , oO0o0OooOO0 , i1iII1IiiIiI1 , OoOOoo0 , IIIi1I1IIii1II in iI111i :
    if iiI11Iii == 'xyz' :
     IIIIiiiI11iII = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     iii11i1IIII ( O000OOO , IIIIiiiI11iII , 1001111 , I1i , I1i , '' , '' )
    else :
     IIIIiiiI11iII = 'http://' + OoOOoo0 + '.' + i1iII1IiiIiI1 + '.' + oO0o0OooOO0 + '.' + iiI11Iii + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     iii11i1IIII ( O000OOO , IIIIiiiI11iII , 1001111 , I1i , I1i , '' , '' )
 for oo000ii in OoOIiiiii111i1ii :
  iiIi1iI1iIii ( '[COLORblue][B]NEXT[/B][/COLOR]' , oo000ii , 1000111 , '' , '' , '' , '' )
  if 17 - 17: OoOo0o / Ii % o0o00Oo0O / O0Oooo0O
  if 61 - 61: IIiIiII11i / Ii * oOo0O0Ooo / o0o00Oo0O . i1IiiiI1iI
  if 67 - 67: iii1i1iiiiIi - oOOoOooOo - iI11I1II1I1I
def Ii1IiiI ( ) :
 iiIi1iI1iIii ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 73 - 73: OOOo00oo0oO / OoOo0o * IIiIiII11i % ii - ooOoO0O00 - oOOoOooOo
 if 43 - 43: ooo0O + i1iIi % oOo . O0Oooo0O + ooOoO0O00
def oOoOOO0O0O ( url , name ) :
 iiIi1iI1iIii ( name , '' , '' , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 I111i1II = requests . get ( url ) . text
 OoOIiiiii111i1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I111i1II )
 O0ooooo0OOOO0 = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I111i1II )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O0ooooo0OOOO0 ) )
 for url , I1i , name in iI111i :
  oO00oOOo0Oo = requests . get ( url ) . text
  i1II1IiiiIii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( oO00oOOo0Oo )
  for i1I1 in i1II1IiiiIii :
   OO0oo0O0OOO0 = requests . get ( i1I1 ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OO0oo0O0OOO0 )
   for iiI11Iii , oO0o0OooOO0 , i1iII1IiiIiI1 , OoOOoo0 , IIIi1I1IIii1II in iI111i :
    if iiI11Iii == 'xyz' :
     IIIIiiiI11iII = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     iii11i1IIII ( name , IIIIiiiI11iII , 1001111 , I1i , I1i , '' , '' )
    else :
     IIIIiiiI11iII = 'http://' + OoOOoo0 + '.' + i1iII1IiiIiI1 + '.' + oO0o0OooOO0 + '.' + iiI11Iii + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     iii11i1IIII ( name , IIIIiiiI11iII , 1001111 , I1i , I1i , '' , '' )
     if 90 - 90: ooo0O + iI11I1II1I1I / I1ii11iIi11i + oOo0O0Ooo + OOOo00oo0oO
 for oo000ii in OoOIiiiii111i1ii :
  iiIi1iI1iIii ( '[COLORblue][B]NEXT[/B][/COLOR]' , oo000ii , 1003111 , '' , '' , '' , '' )
  if 60 - 60: oOo
  if 16 - 16: i1IiiiI1iI
def iII11i1 ( ) :
 iiIi1iI1iIii ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 58 - 58: iiiiiiii1
 if 77 - 77: I11i1ii1 % OOOo00oo0oO % oOo
 if 68 - 68: oOOoOooOo % i1IiiiI1iI - i1iIi . oOo
def i11IIiIi ( url , name ) :
 iiIi1iI1iIii ( name , '' , '' , '' , '' , '' , '' )
 iiIi1iI1iIii ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 I111i1II = requests . get ( url ) . text
 OoOIiiiii111i1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I111i1II )
 O0ooooo0OOOO0 = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( I111i1II )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O0ooooo0OOOO0 ) )
 for url , I1i , name in iI111i :
  oO00oOOo0Oo = requests . get ( url ) . text
  i1II1IiiiIii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( oO00oOOo0Oo )
  for i1I1 in i1II1IiiiIii :
   OO0oo0O0OOO0 = requests . get ( i1I1 ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OO0oo0O0OOO0 )
   for iiI11Iii , oO0o0OooOO0 , i1iII1IiiIiI1 , OoOOoo0 , IIIi1I1IIii1II in iI111i :
    if iiI11Iii == 'xyz' :
     IIIIiiiI11iII = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     iii11i1IIII ( name , IIIIiiiI11iII , 1001111 , I1i , I1i , '' , '' )
    else :
     IIIIiiiI11iII = 'http://' + OoOOoo0 + '.' + i1iII1IiiIiI1 + '.' + oO0o0OooOO0 + '.' + iiI11Iii + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     iii11i1IIII ( name , IIIIiiiI11iII , 1001111 , I1i , I1i , '' , '' )
     if 52 - 52: iii1i1iiiiIi . oOoO0o00OO0 . I1ii11iIi11i
 for oo000ii in OoOIiiiii111i1ii :
  iiIi1iI1iIii ( '[COLORblue][B]NEXT[/B][/COLOR]' , oo000ii , 1005111 , '' , '' , '' , '' )
def OoO00o0 ( name , url ) :
 import urlresolver
 try :
  ooo0oOOO0 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( ooo0oOOO0 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 99 - 99: ii - ooOoO0O00 % ooo0O / ooo0O + I11i1ii1
 if 96 - 96: ii + OoOo0o - O0Oooo0O / OOOo00oo0oO % OOOo00oo0oO
 if 34 - 34: I11i1ii1
def o0OOO0Oo ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 iI111i = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Daily' in O000OOO :
   o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 9008 , O0O )
def O0O00oo ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def iiIIIii ( url ) :
 Oo ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 Oo ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 Oo ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I111i1II )
 for O000OOO , url in iI111i :
  Oo ( ( O000OOO ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 71 - 71: OoOo0o * iii1i1iiiiIi - i1IiiiI1iI . Ii
def i1111iII1 ( ) :
 I111i1II = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if '.m3u' in IIo0o0O0O00oOOo :
   o0OO ( ( O000OOO ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + IIo0o0O0O00oOOo ) , 9011 , I1IIIii + 'disclose.png' )
def I1I1iiI11I1 ( url ) :
 I111i1II = cloudflare . source ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I111i1II )
 for O000OOO , url in iI111i :
  Oo ( ( O000OOO ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 36 - 36: OOOo00oo0oO - i1IiiiI1iI % i1IiiiI1iI - IIiIiII11i
def I1iii ( ) :
 I111i1II = i11111IIIII ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 iI111i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'category' in IIo0o0O0O00oOOo :
   o0OO ( O000OOO , 'http://www.disclose.tv/' + IIo0o0O0O00oOOo , 7010 , I1IIIii + 'disclose.png' )
   if 5 - 5: ooOoO0O00 - oOo0O0Ooo * oOo0O0Ooo
   if 49 - 49: O0Oooo0O
def iIii ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I111i1II )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I111i1II )
 for url , O000OOO , I1i in iI111i :
  o0OO ( O000OOO , 'http://www.disclose.tv/' + url , 7011 , I1i )
 for url in next :
  o0OO ( 'NEXT' , url , 7010 , I1IIIii + 'Next.png' )
  if 41 - 41: OOOo00oo0oO . O0Oooo0O + o0o00Oo0O - OOOo00oo0oO . iii1i1iiiiIi * oOo
  if 6 - 6: oOOoOooOo / OOOo00oo0oO % ooo0O + oOOoOooOo / IIiIiII11i - O0Oooo0O
def O000ooo ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I111i1II )
 OoOOo0OOoO = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  if 'http' in url :
   Oo ( 'video/flv' , url , 222 , I1IIIii + 'disclose.png' )
 for url , O000OOO in IIi11i1i1iI1 :
  Oo ( O000OOO , url , 222 , I1IIIii + 'disclose.png' )
 for url in OoOOo0OOoO :
  Oo ( 'YT Link' , url , 8043 , I1IIIii + 'disclose.png' )
  if 32 - 32: OoOo0o + I11i1ii1
  if 36 - 36: i1IiiiI1iI + O0Oooo0O . OoOo0o % ooo0O / i1iIi * ooOoO0O00
def II1Oooo00oO0OO0o ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  o0OO ( O000OOO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , I1IIIii + 'icon.png' )
  if 47 - 47: I1ii11iIi11i / iii1i1iiiiIi
def i1IOO00OOOO00oOO ( name , url , img ) :
 oOOo0 = i11111IIIII ( url )
 O0o0ooO0oO0oO = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oOOo0 )
 iI1iII111ii1I = len ( O0o0ooO0oO0oO )
 if 97 - 97: OOOo00oo0oO - iiiiiiii1 + I11i1ii1 . iii1i1iiiiIi + iI11I1II1I1I
 if 75 - 75: oOOoOooOo + oOOoOooOo . O0Oooo0O % iiiiiiii1 / iI11I1II1I1I * iiiiiiii1
 if iI1iII111ii1I == 1 :
  for IiIi1iIIiII1i in O0o0ooO0oO0oO :
   IiIi1iIIiII1i = IiIi1iIIiII1i . replace ( 'player' , 'watch' )
   OOoOo = IiIi1iIIiII1i + '&fv=&sou='
   i1iiii11iIIiiI1I = i11111IIIII ( OOoOo )
   oOOoo0O00 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( i1iiii11iIIiiI1I )
   for IiiIi1III in oOOoo0O00 :
    i1IIIi111111 = False
    Resolve ( IiiIi1III )
    if 30 - 30: ooOoO0O00
 elif iI1iII111ii1I > 1 :
  if 86 - 86: oOo0O0Ooo % i1IiiiI1iI * o0o00Oo0O + ooOoO0O00 % O0Oooo0O
  for IiIi1iIIiII1i in O0o0ooO0oO0oO :
   OoOOo0ooOoooO = i11111IIIII ( IiIi1iIIiII1i )
   I1ioo0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OoOOo0ooOoooO )
   Iii1iiiiI = I1ioo0
   Iii1iiiiI = ( str ( Iii1iiiiI ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + Iii1iiiiI
   Oo ( 'DOUBLE LINK' , Iii1iiiiI , 424 , '' )
   if 44 - 44: ii
   for url in I1ioo0 :
    o0OO ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     O0Ooo = Google . resolve ( url )
    except :
     pass
    try :
     Oo0O0ooo = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( O0Ooo ) )
     for iIII , ooOo0OoooOo in Oo0O0ooo :
      if 65 - 65: I11i1ii1 . OoOo0o % iiiiiiii1 / o0o00Oo0O
      HD_URLS . append ( iIII )
      SD_URLS . append ( ooOo0OoooOo )
    except :
     pass
 else :
  pass
  if 95 - 95: Ii % Ii
def iIII11ii1i1i1 ( ) :
 if 3 - 3: oOo0O0Ooo . i1IiiiI1iI / oOoO0o00OO0
 if 2 - 2: I11i1ii1 + i1IiiiI1iI / iI11I1II1I1I . Ii . ooOoO0O00 * oOOoOooOo
 o0OO ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , I1IIIii + 'Movies.png' )
 if 14 - 14: I1ii11iIi11i . o0o00Oo0O - OOOo00oo0oO - Ii
 o0OO ( 'Search Movies' , '' , 7017 , I1IIIii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / oOOoOooOo
 if 80 - 80: i1IiiiI1iI
def IiiiIi ( ) :
 I111i1II = i11111IIIII ( 'http://cnfstudio.com/' )
 iI111i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( O000OOO , 'http://cnfstudio.com/genre/' + IIo0o0O0O00oOOo , 7003 , I1IIIii + 'icon.png' )
  if 81 - 81: Ii + ooo0O / IIiIiII11i + i1IiiiI1iI
iI111I11I1I1 = xbmcgui . Dialog ( )
if 73 - 73: oOo + OoOo0o + I11i1ii1 - ooOoO0O00
OoOoO0OoO = '{UN},' ; o0o0O = '{IG},' ; IIIIii1Ii11i = '{PL},' ; O0O00OO00O00O = '{LO},' ; Oo0oooOoOO000Ooo = '{LP},' ; oOO0o0OO = '{HA},' ; iI111ii11 = '{XD},' ; oOoOoo0OOOo0 = '{TA},' ; iIII1Ii1 = '{DP},' ; o0Oo00OoO000O = '{JT},' ; II1iii = '{JJ},' ; O0oOOOO0o = '{MM},' ; OoOOO0 = '{FQ},' ; IiIio0oO0O = '{HH},'
if 28 - 28: o0o00Oo0O % IIiIiII11i / iii1i1iiiiIi / OoOo0o
def O0Oo ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I111i1II )
 Ii111IiiiIi = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I111i1II )
 for I1i , url , O000OOO in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I1i )
 Ii111IiiiIi = Ii111IiiiIi
 for url in Ii111IiiiIi :
  o0OO ( 'Next Page' , url , 7003 , I1IIIii + 'Next.png' )
  if 2 - 2: oOoO0o00OO0 - OoOo0o
def o0o0o ( url ) :
 if 57 - 57: O0Oooo0O * ooo0O + oOOoOooOo . OOOo00oo0oO * iI11I1II1I1I / oOOoOooOo
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  IIIi1I1IIii1II = url + '&fv=&sou='
  IIIi1I1IIii1II = IIIi1I1IIii1II . replace ( 'player' , 'watch' )
  o0oooooooO0o = O0OI1i ( IIIi1I1IIii1II )
  i1IIi = O0OI1i ( url )
  if 91 - 91: oOOoOooOo . iiiiiiii1 - o0o00Oo0O . ooo0O . I11i1ii1
  if 30 - 30: iii1i1iiiiIi
def O0OI1i ( url ) :
 if 70 - 70: oOOoOooOo - ooo0O + IIiIiII11i + OOOo00oo0oO + ooOoO0O00
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I111i1II )
 for url in iI111i :
  O00o0o ( url )
  if 79 - 79: O0Oooo0O
  if 50 - 50: oOOoOooOo . oOoO0o00OO0 . ooOoO0O00 / ii
def IioO ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , I1IIIii + 'LocalM3U.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , I1IIIii + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 44 - 44: oOo + oOo0O0Ooo / oOo0O0Ooo / i1iIi
def iii1II1iI1III ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  Ooo00OO00oOO0 = open ( O0OoO000O0OO , 'r' )
  for Ii1II1I11i1 in Ooo00OO00oOO0 :
   oooO0OOo0 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( Ii1II1I11i1 )
   for O000OOO , IIo0o0O0O00oOOo in oooO0OOo0 :
    Oo ( O000OOO , IIo0o0O0O00oOOo , 222 , I1IIIii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 48 - 48: I11i1ii1 . IIiIiII11i - Ii * iiiiiiii1
def Ooo0O00 ( url ) :
 if os . path . exists ( Remote ) :
  oOOo0 = o0Ooo0O00 ( url )
  iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
  for O000OOO , url in iI111i :
   url = ( url ) . strip ( )
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 1 - 1: oOo % OoOo0o - iiiiiiii1 * iI11I1II1I1I
  if 14 - 14: iii1i1iiiiIi
def Iii1I1I11iiI1 ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + IIo0o0O0O00oOOo
 O000OOO = 'plugin.video.GenieTv'
 if 17 - 17: I1ii11iIi11i . ii % oOoO0o00OO0 / ii
 oO0OOOOo ( IIo0o0O0O00oOOo , O000OOO )
 if 28 - 28: i1iIi
def o0OOOO00O0Oo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + IIo0o0O0O00oOOo
 O000OOO = 'repository.GenieTv'
 if 27 - 27: I1ii11iIi11i . i1IiiiI1iI % oOo0O0Ooo * Ii
 oO0OOOOo ( IIo0o0O0O00oOOo , O000OOO )
 if 86 - 86: oOOoOooOo / O0Oooo0O * OOOo00oo0oO . O0Oooo0O - Ii
 if 93 - 93: O0Oooo0O - I1ii11iIi11i
def IIiiI1iiI ( ) :
 oo0 = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , oo0 )
 if oOOOoo00 == 0 :
  OoO0o ( )
 if oOOOoo00 == 1 :
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
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 Ii1I11IIi1 = 'https://addons.tvaddons.ag/search/?keyword=' + ooO0000o00O
 oOOo0 = i11111IIIII ( Ii1I11IIi1 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , iIiII , O000OOO in iI111i :
  o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 10054 , 'https://addons.tvaddons.ag/' + iIiII , Oo00OOOOO , '' )
  if 3 - 3: I1ii11iIi11i + OOOo00oo0oO
  if 65 - 65: oOo0O0Ooo / iii1i1iiiiIi % oOo0O0Ooo * Ii * ii / i1IiiiI1iI
def OoO0o ( ) :
 oOOo0 = i11111IIIII ( iIiiiiIi1 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  if 'Repositories' in O000OOO :
   pass
  elif 'Services' in O000OOO :
   pass
  elif 'International' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 10053 , 'https://addons.tvaddons.ag/' + I1i , Oo00OOOOO , '' )
   if 91 - 91: Ii / Ii
   if 9 - 9: i1IiiiI1iI / O0Oooo0O + iI11I1II1I1I + oOo0O0Ooo - IIiIiII11i
def Addon ( url ) :
 oOOo0 = i11111IIIII ( url )
 OoOIiiiii111i1ii = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for url , I1i , O000OOO in iI111i :
  if 'Please' in O000OOO :
   pass
  else :
   O0O0ooOOO ( O000OOO , url , 10054 , 'https://addons.tvaddons.ag/' + I1i , Oo00OOOOO , '' )
 for url in OoOIiiiii111i1ii :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
  if 96 - 96: iiiiiiii1 + I1ii11iIi11i - ii . ooOoO0O00 + ooOoO0O00 % iI11I1II1I1I
  if 80 - 80: ii / o0o00Oo0O / O0Oooo0O - I1ii11iIi11i . Ii
def II11IIiii ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oO0 = xbmcgui . DialogProgress ( )
   o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , name + '.zip' )
   try :
    os . remove ( Iiii1iI1i )
   except :
    pass
   downloader . download ( url , Iiii1iI1i , o0oO0 )
   I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print I1ii1ii11i1I
   print '======================================='
   extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
   O0O0Oo00 ( )
   if 14 - 14: oOo0O0Ooo
def oO0OOOOo ( url , name ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , name + '.zip' )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1ii1ii11i1I
 print '======================================='
 extract . all ( Iiii1iI1i , I1ii1ii11i1I , o0oO0 )
 O0O0Oo00 ( )
 if 41 - 41: O0Oooo0O % ooOoO0O00 + oOo / OOOo00oo0oO
def O0O0Oo00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 48 - 48: ooOoO0O00 . I1ii11iIi11i . ooOoO0O00 . oOoO0o00OO0 * oOo0O0Ooo - i1iIi
 if 83 - 83: ii
def IIoOOOoOoOO ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
 for url , iIiII , O000OOO in iI111i :
  o0OO ( O000OOO , url , 1007 , iIiII )
def iI1iIII1i1II ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
 for url , iIiII , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 1006 , iIiII )
  if 90 - 90: i1iIi / i1IiiiI1iI
def o0OOOo ( ) :
 I111i1II = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , iI1iIii11Ii , O000OOO in iI111i :
  O0ooOOOo000OOoOO ( O000OOO , 100109 , IIo0o0O0O00oOOo , image = i1i1II1i11 , isFolder = True )
  if 29 - 29: oOo * iI11I1II1I1I % i1iIi / OOOo00oo0oO / O0Oooo0O
def ii1ii1iii1I ( url ) :
 import random
 oo0O0OO0Oooo = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oo0O0OO0Oooo . clear ( )
 OOOOooO0Oo0oo = [ ]
 oOo0oooo = [ ]
 oooO0O0O0ooO = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for O0Ooo , i1i1II1i11 , IIIIiii1IIii , iI1iIii11Ii , O000OOO in iI111i :
  OOOOooO0Oo0oo . append ( [ O0Ooo , O000OOO ] )
  if len ( OOOOooO0Oo0oo ) == len ( iI111i ) :
   for Ii1II1I11i1 in OOOOooO0Oo0oo :
    IiIIIIiiIIIii = random . randint ( 1 , len ( OOOOooO0Oo0oo ) )
    try :
     OOO0o = OOOOooO0Oo0oo [ int ( IiIIIIiiIIIii ) ]
    except :
     pass
    if len ( oOo0oooo ) <= 20 :
     if OOO0o [ 1 ] not in oooO0O0O0ooO :
      oo00O00oO = i11111IIIII ( OOO0o [ 0 ] )
      OoOOo0OOoO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oo00O00oO )
      for oo00ooOOoo , O000OOOo in OoOOo0OOoO :
       ooo00OOOooO = i11111IIIII ( oo00ooOOoo )
       ooO0O00Oo0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( ooo00OOOooO )
       for iII , IIIi1I1IIii1II in ooO0O00Oo0o :
        if 'panda' in IIIi1I1IIii1II :
         OooOOOoOoo0O0 = i11111IIIII ( IIIi1I1IIii1II )
         OOO = re . compile ( "url: '(.+?)'" ) . findall ( OooOOOoOoo0O0 )
         for I1ii11ii1iiI in OOO :
          if 'http' in I1ii11ii1iiI :
           o0OoOo00ooO = xbmcgui . ListItem ( OOO0o [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : OOO0o [ 1 ] } )
           o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
           oo0O0OO0Oooo . add ( I1ii11ii1iiI , o0OoOo00ooO )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOo00ooO )
           if 29 - 29: oOo0O0Ooo
def O0ooOOOo000OOoOO ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
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
def i11ii1Ii1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
 for url , iconimage , IIIIiii1IIii , iI1iIii11Ii , name in iI111i :
  if 'http' in url :
   if '.php' in url :
    OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
    for Ii1II1I11i1 in OooOooO0O0o0 :
     if Ii1II1I11i1 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    I1i1i1 ( name , url , 1016 , iconimage , iI1iIii11Ii , IIIIiii1IIii )
   else :
    if 'youtube' in url :
     OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for Ii1II1I11i1 in OooOooO0O0o0 :
      if Ii1II1I11i1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Oo00oOOO0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iI1iIii11Ii , IIIIiii1IIii )
    else :
     OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for Ii1II1I11i1 in OooOooO0O0o0 :
      if Ii1II1I11i1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Oo00oOOO0 ( name , url , 222 , iconimage , iI1iIii11Ii , IIIIiii1IIii )
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
  else :
   IiIIooO00oOo0 ( url , iconimage , name )
   if 42 - 42: oOo0O0Ooo * ooo0O / o0o00Oo0O . IIiIiII11i
 else :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
  for url , iIiII , name in iI111i :
   if 'http' in url :
    if '.php' in url :
     o0OO ( name , url , 1016 , iIiII )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      Oo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIiII )
     else :
      OooOooO0O0o0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
      for Ii1II1I11i1 in OooOooO0O0o0 :
       if Ii1II1I11i1 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      Oo ( name , url , 222 , iIiII )
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
   else :
    IiIIooO00oOo0 ( url , iIiII , name )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 88 - 88: ii % IIiIiII11i + I11i1ii1 + I11i1ii1 * I1ii11iIi11i
def IiIIooO00oOo0 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ooO00O00o0O0o = ( url ) . replace ( ii1I1 , 'http' ) . replace ( o0oOOoO0o0 , '.com' ) ;
 ii1I11iiI = ( ooO00O00o0O0o ) . replace ( ooOo0OooOooo , 'a' ) . replace ( o0OoO0 , 'b' ) . replace ( I11Ii1I1I , 'c' ) . replace ( Ii111Ii11I111Ii , 'd' ) . replace ( IIIIii1Ii11i , 'e' ) . replace ( o0Oo00OoO000O , 'f' ) ;
 IIIi1 = ( ii1I11iiI ) . replace ( OOo0O0O000 , 'g' ) . replace ( oOO0o0OO , 'h' ) . replace ( oOOo0o0O0oO0o , 'i' ) . replace ( oo0O0 , 'j' ) . replace ( oo00OO0o0 , 'k' ) . replace ( o0oo0000Oo , 'l' ) ;
 iIIIiiI = ( IIIi1 ) . replace ( o0oOo0O0o0oO , 'm' ) . replace ( O00o000O0O0oO , 'n' ) . replace ( iIiI111ii , 'o' ) . replace ( IiIoOO0ooO000 , 'p' ) . replace ( ooI11 , 'q' ) . replace ( OOoOo0Oo , 'r' ) ;
 oOo0o0O = ( iIIIiiI ) . replace ( I1I1Ii111 , 's' ) . replace ( iIiIIiIII1I , 't' ) . replace ( o0o0o0oO0oOoo , 'u' ) . replace ( Ooi1I11i1 , 'v' ) . replace ( II1iiiii , 'w' ) . replace ( iI11iIiIiiiI , 'x' ) ;
 I1oo0Oo = ( oOo0o0O ) . replace ( I1OO0Oo0 , 'y' ) . replace ( iI1IIiI1 , 'z' ) . replace ( OoOoO0OoO , '.' ) . replace ( o0o0O , '(' ) . replace ( O0O00OO00O00O , ')' ) . replace ( Oo0oooOoOO000Ooo , '/' ) ;
 iIIii111i1 = ( I1oo0Oo ) . replace ( OoO0oO , '1' ) . replace ( Ii1i1IiiIiIII , '2' ) . replace ( iIIIIi , '3' ) . replace ( oOoOoo0OOOo0 , '4' ) . replace ( iIII1Ii1 , '5' ) . replace ( iiIi , '6' ) ;
 iiI1 = ( iIIii111i1 ) . replace ( II1iii , '7' ) . replace ( O0oOOOO0o , '8' ) . replace ( OoOOO0 , '9' ) . replace ( IiIio0oO0O , '0' ) . replace ( iiI1i111I1 , ':' ) . replace ( iiIi11i1I1 , '%' ) ;
 url = ( iiI1 ) . replace ( OoOI1I , '-' ) . replace ( iI111ii11 , '_' ) ;
 Oo ( name , url , 222 , iconimage ) ;
 if 51 - 51: OoOo0o + o0o00Oo0O
 if 91 - 91: Ii + ooo0O % oOo / OOOo00oo0oO - ooOoO0O00
def O0ii1IIIiiI1i ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , iIiII , O000OOO in iI111i :
  o0OO ( O000OOO , IIo0o0O0O00oOOo , 1007 , iIiII )
def Iiii1I ( url ) :
 if 20 - 20: oOoO0o00OO0 - I11i1ii1 + OOOo00oo0oO * ooOoO0O00 % iiiiiiii1 * oOOoOooOo
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
 for url , iIiII , O000OOO in iI111i :
  o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 1006 , iIiII )
  if 80 - 80: oOOoOooOo * I11i1ii1 . ooo0O
def iI1i1iIii1 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iI1IIIii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iI1IIIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iI1IIIii )
 if 72 - 72: OoOo0o / iii1i1iiiiIi
 if 89 - 89: OoOo0o + OoOo0o * iii1i1iiiiIi + iiiiiiii1 % O0Oooo0O % O0Oooo0O
def oOoo ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I111i1II )
 for url , I1i , O000OOO in iI111i :
  if '-dir-' in O000OOO :
   o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , I1i )
  else :
   o0OO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 1006 , I1i )
   if 68 - 68: I1ii11iIi11i + oOo % oOo % iii1i1iiiiIi
def II1i1iIIi1 ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 i1I1I1i1I1 = ( 'http://afewbitsmore.com/' )
 iI111i = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  if '[To Parent Directory]' in O000OOO :
   O000OOO = 'HOME'
   pass
  elif 'HOME' in O000OOO :
   pass
  elif '.m3u' in O000OOO :
   o0OO ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , i1I1I1i1I1 + url , 2002 , I1IIIii + 'music.png' )
  elif '.mp3' in O000OOO :
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , i1I1I1i1I1 + url , 222 , I1IIIii + 'music.png' )
  elif '.m4a' in O000OOO :
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , i1I1I1i1I1 + url , 222 , I1IIIii + 'music.png' )
  else :
   o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) , i1I1I1i1I1 + url , 1012 , I1IIIii + 'music.png' )
def IioooO ( url ) :
 oOOo0 = o0Ooo0O00 ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , O000OOO , url in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , I1IIIii + 'music.png' )
  if 65 - 65: O0Oooo0O
def Ii1oo ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 i1I1I1i1I1 = url
 iI111i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  if '.mp3' in O000OOO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , I1IIIii + 'music.png' )
  else :
   o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '/' , '' ) , i1I1I1i1I1 + url , 1011 , I1IIIii + 'music.png' )
def I111I11iiI ( ) :
 I111i1II = o0Ooo0O00 ( o0oOoO00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iI111i = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , I1i , O000OOO in iI111i :
  o0OO ( O000OOO , ( 'http://www.cyn.net/music/' + IIo0o0O0O00oOOo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I1i ) . replace ( ' ' , '%20' ) )
def oOoOOooo0OOO ( url , img ) :
 I111i1II = o0Ooo0O00 ( url )
 O0Ooo = url
 img = img
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( O0Ooo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 86 - 86: ii / o0o00Oo0O * iii1i1iiiiIi * OoOo0o . oOo
def IiI1iI1 ( url ) :
 I111i1II = o0Ooo0O00 ( url )
 O0Ooo = url
 iI111i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I111i1II )
 for type , url , O000OOO in iI111i :
  if '[VID]' in type :
   Oo ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , O0Ooo + url , 222 , I1IIIii + 'music.png' )
  if '[DIR]' in type :
   IiI1iI1 ( O0Ooo + url )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: ooo0O / I11i1ii1 / oOOoOooOo * iii1i1iiiiIi
 if 13 - 13: iiiiiiii1
def i1IIII1II ( ) :
 i1i1iiIIiiiII = ( o0oOoO00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oOoooO00O = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0000o00O = oOoooO00O . lower ( )
 IIo0o0O0O00oOOo = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 o0OOOOOo0 = ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 O0Ooo = ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 69 - 69: Ii - Ii + i1IiiiI1iI / oOo0O0Ooo % oOoO0o00OO0
 oOOo0 = i1Oo00 ( IIo0o0O0O00oOOo )
 iiIIi1 = i1Oo00 ( o0OOOOOo0 )
 oo00O00oO = i1Oo00 ( O0Ooo )
 if 56 - 56: iI11I1II1I1I / oOo * OoOo0o
 if oOOo0 != 'Failed' :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , i1i1II1i11 , IIIIiii1IIii , i1iIIi1II1iiI , O000OOO in iI111i :
   if oOoooO00O in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , IIo0o0O0O00oOOo , 1016 , i1i1II1i11 , iI1iIii11Ii , IIIIiii1IIii )
    if 73 - 73: ii % I11i1ii1 / O0Oooo0O * i1IiiiI1iI + ooOoO0O00 % Ii
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iiIIi1 != 'Failed' :
  oOOoo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiIIi1 )
  for IIo0o0O0O00oOOo , O000OOO in oOOoo :
   if oOoooO00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + IIo0o0O0O00oOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
    if 91 - 91: Ii
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( oo00O00oO )
  for IIo0o0O0O00oOOo , O000OOO in IIi11i1i1iI1 :
   if oOoooO00O in O000OOO . lower ( ) :
    o0OO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + IIo0o0O0O00oOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
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
 I111i1II = i11111IIIII ( 'http://www.iwatchseries.me/tv-list/' )
 iI111i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( O000OOO , IIo0o0O0O00oOOo , 8021 , I1IIIii + 'iwatch.png' )
  iIiIi11 ( 'movies' , 'MAIN' )
def IIi1III1II ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I111i1II )
 for url , O000OOO , iIi11 in iI111i :
  o0OO ( O000OOO + iIi11 , url , 8022 , I1IIIii + 'iwatch.png' )
def o0o0OOOO ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I111i1II )
 for url in iI111i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1i1iiIII1i1 ( url )
def I1i1iiIII1i1 ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I111i1II )
 IIi11i1i1iI1 = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I111i1II )
 OoOOo0OOoO = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I111i1II )
 ooO0O00Oo0o = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  Oo ( 'VidSpot - ' + O000OOO , url , 222 , I1IIIii + 'iwatch.png' )
 for url in IIi11i1i1iI1 :
  Oo ( 'VodLocker' , url , 222 , I1IIIii + 'iwatch.png' )
 for url , O000OOO in ooO0O00Oo0o :
  Oo ( 'VidUp' + O000OOO , url , 222 , I1IIIii + 'iwatch.png' )
 for O000OOO , url in OoOOo0OOoO :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   Oo ( 'TheVideo - ' + O000OOO , url , 222 , I1IIIii + 'iwatch.png' )
   if 20 - 20: I1ii11iIi11i . ii % OOOo00oo0oO - OoOo0o
def OoOooOOooO ( ) :
 I111i1II = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 iI111i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( O000OOO , IIo0o0O0O00oOOo , 1021 , I1IIIii + 'anime.png' )
  if 50 - 50: ii - oOoO0o00OO0
  if 96 - 96: O0Oooo0O / O0Oooo0O * i1iIi / iI11I1II1I1I
def oOO0o00 ( ) :
 I111i1II = i11111IIIII ( 'http://www.animetoon.org/cartoon' )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I111i1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o0OO ( O000OOO , IIo0o0O0O00oOOo , 1002 , I1IIIii + 'anime.png' )
  if 87 - 87: ooo0O . iI11I1II1I1I . oOOoOooOo
  if 53 - 53: I11i1ii1
  if 37 - 37: i1IiiiI1iI
def ii1I1IIiii ( url ) :
 I111i1II = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I111i1II )
 for I1i in IIi11i1i1iI1 :
  Ii1II111iIi = I1i
 OoOOo0OOoO = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I111i1II )
 for url in OoOOo0OOoO :
  o0OO ( 'NEXT PAGE' , url , 1002 , I1IIIii + 'Next.png' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I111i1II )
 for url , O000OOO in iI111i :
  o0OO ( O000OOO , url , 1003 , Ii1II111iIi )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1io0ooO0OO ( url , IMAGE ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I111i1II )
 for O000OOO , url in iI111i :
  print O000OOO + '     ' + url
  if 'easy' in url :
   I1IiI1i1Iii ( url )
  elif 'playpanda' in url :
   I1IiI1i1Iii ( url )
   if 27 - 27: i1IiiiI1iI + iI11I1II1I1I
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1IiI1i1Iii ( url ) :
 I111i1II = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( I111i1II )
 for url in iI111i :
  Oo ( 'STREAM' , url , 222 , I1IIIii + 'anime.png' )
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
def o0Ooo0O00 ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 30 - 30: O0Oooo0O / ooo0O + ii + iii1i1iiiiIi + oOo
def ii11IoOo0O0Oo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iIiii1Ii = ( '%s%s' % ( oO0OO00O0 , url ) )
 IIIi1I1IIii1II = o0Ooo0O00 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , iIiII , O000OOO in iI111i :
  Oo ( '%s' % ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iIiII )
  if 83 - 83: oOOoOooOo / oOo
def oO00oo0o ( url ) :
 if O0oo0OO0 . getSetting ( 'down' ) == 'true' :
  i1iIi11 ( url , O000OOO )
 else :
  OOIi1iI111II1I1 ( url )
def OOIi1iI111II1I1 ( url ) :
 import urlresolver
 try :
  ooo0oOOO0 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( ooo0oOOO0 , xbmcgui . ListItem ( O000OOO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( O000OOO ) )
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
 o0oO0 . create ( 'LOADING' , 'Opening %s Now' % ( O000OOO ) )
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
  Ii111ii1 = '.mp4'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.mkv' in url :
  Ii111ii1 = '.mkv'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.mp3' in url :
  Ii111ii1 = '.mp3'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.avi' in url :
  Ii111ii1 = '.avi'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.mov' in url :
  Ii111ii1 = '.mov'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.mpeg' in url :
  Ii111ii1 = '.mpeg'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.mpg' in url :
  Ii111ii1 = '.mpg'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.flv' in url :
  Ii111ii1 = '.flv'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 elif '.wmv' in url :
  Ii111ii1 = '.wmv'
  oo0 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  oOOOoo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , oo0 )
  if oOOOoo00 == 0 :
   OOIi1iI111II1I1 ( url )
  if oOOOoo00 == 1 :
   oooOoO0oOo00o ( url , name , Ii111ii1 )
 else :
  OOIi1iI111II1I1 ( url )
def oooOoO0oOo00o ( url , name , cat ) :
 i1i11iiIIi1I ( )
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( II ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 Iiii1iI1i = os . path . join ( OOoOooOoOOOoo , file )
 try :
  os . remove ( Iiii1iI1i )
 except :
  pass
 downloader . download ( url , Iiii1iI1i , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def i1i11iiIIi1I ( ) :
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( II ) )
 if not os . path . exists ( II ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
def iI1Ii ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oO0 . update ( 0 , '%s' % O000OOO )
 xbmc . sleep ( 1 )
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 o0oO0 . update ( 100 , '%s' % O000OOO )
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
def I1111 ( url ) :
 o0000o0Oo = xbmc . Player ( ooo0O0OOo0OoO ( ) )
 import urlresolver
 OoO0OIIi1 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 o0000o0Oo . play ( OoO0OIIi1 )
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
def o0OO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
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
def Iii1i ( name , url , mode , iconimage , fanart , description ) :
 if 60 - 60: iiiiiiii1
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOo00ooO . setProperty ( "Fanart_Image" , fanart )
 OoOo0oO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I1I1i11ii , listitem = o0OoOo00ooO , isFolder = True )
 return OoOo0oO0o
 if 92 - 92: ooOoO0O00 + O0Oooo0O % ooOoO0O00 * iiiiiiii1 % ooo0O
def Oo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
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
   try : OOOO0OOO = open ( announce ) ; O0o00 = OOOO0OOO . read ( )
   except : O0o00 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0o00 ) )
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
   try : OOOO0OOO = open ( announce ) ; O0o00 = OOOO0OOO . read ( )
   except : O0o00 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0o00 ) )
   return
 OoOoO ( )
 OoOoO ( )
def oOoo0oOo00 ( ) :
 i111iiiI1iiI ( I1IIIii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 23 - 23: oOoO0o00OO0 . oOoO0o00OO0 / oOo0O0Ooo . ooOoO0O00
 if 47 - 47: Ii . ooo0O . Ii + oOo0O0Ooo - oOoO0o00OO0
 if 62 - 62: ii + oOo0O0Ooo / oOOoOooOo . i1iIi . I1ii11iIi11i
 if 81 - 81: OOOo00oo0oO + I11i1ii1
 if 75 - 75: o0o00Oo0O + oOoO0o00OO0
def O0O0Oo00 ( ) :
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
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 75 - 75: o0o00Oo0O - iI11I1II1I1I + iii1i1iiiiIi . Ii - ooo0O
def IIi1III11I1Ii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Oooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 80 - 80: i1IiiiI1iI + ooo0O - O0Oooo0O . oOo * OOOo00oo0oO + OoOo0o
def Oo0ooO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o000oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 61 - 61: ooo0O * o0o00Oo0O
def o0O0oO00oo0O ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1iIOo0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 4 - 4: OOOo00oo0oO / iii1i1iiiiIi . I1ii11iIi11i . ooo0O / ooOoO0O00 / OoOo0o
def OOO0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 78 - 78: iiiiiiii1 . OOOo00oo0oO . oOo0O0Ooo % o0o00Oo0O * oOOoOooOo % O0Oooo0O
def ii1111I ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + IIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 56 - 56: I1ii11iIi11i . i1iIi
def oOOOO0oO0o0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o0o0O00OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 90 - 90: O0Oooo0O * oOo
def o0O0iIi ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iiII11iI11i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 92 - 92: oOo0O0Ooo / O0Oooo0O
def Iiii11i11 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1iIII1i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , i1i1II1i11 , iI1iIii11Ii , II1 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 98 - 98: OOOo00oo0oO / iI11I1II1I1I - iii1i1iiiiIi
def iiI ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + I1Ii1i111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , i1i1II1i11 , iI1iIii11Ii , II1 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , I1IIIii + 'GenieTVRSSFeed.png' , I1IIIii + 'GenieTVRSSFeed.png' , II1 )
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
    for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( o0 ) :
     I111III = 0
     I111III += len ( Iiiiii )
     if I111III > 0 :
      for OOOO0OOO in Iiiiii :
       os . unlink ( os . path . join ( Ooo00OoO0O00 , OOOO0OOO ) )
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
def iII1ii1 ( title , message , times = 2000 , icon = O0O ) :
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
 for Ii1II1I11i1 in i1I111II11 :
  if os . path . exists ( Ii1II1I11i1 ) and not Ii1II1I11i1 in [ I11 , O0oooOO ] :
   for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( Ii1II1I11i1 ) :
    I111III = 0
    I111III += len ( Iiiiii )
    if I111III > 0 :
     for OOOO0OOO in Iiiiii :
      if not OOOO0OOO in oo0o0O00 :
       try :
        os . unlink ( os . path . join ( Ooo00OoO0O00 , OOOO0OOO ) )
       except :
        pass
      else : oO00O0 ( 'Ignore Log File: %s' % OOOO0OOO )
     for OoOOoo0 in O00oOOO0 :
      try :
       shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , OoOOoo0 ) )
       I1IIiIiI += 1
       oO00O0 ( "[Success] cleared %s files from %s" % ( str ( I111III ) , os . path . join ( Ii1II1I11i1 , OoOOoo0 ) ) )
      except :
       oO00O0 ( "[Failed] to wipe cache in: %s" % os . path . join ( Ii1II1I11i1 , OoOOoo0 ) )
  else :
   for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( Ii1II1I11i1 ) :
    for OoOOoo0 in O00oOOO0 :
     if 'cache' in OoOOoo0 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , OoOOoo0 ) )
       I1IIiIiI += 1
       oO00O0 ( "[Success] wiped %s " % os . path . join ( Ii1II1I11i1 , OoOOoo0 ) )
      except :
       oO00O0 ( "[Failed] to wipe cache in: %s" % os . path . join ( Ii1II1I11i1 , OoOOoo0 ) )
       if 93 - 93: I11i1ii1 . iii1i1iiiiIi % i1iIi - ooOoO0O00 . iI11I1II1I1I / O0Oooo0O
 iII1ii1 ( oOo0oooo00o , 'Clear Cache: Removed %s Files' % I1IIiIiI )
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
  for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( oOOoOoooOo0o ) :
   I111III = 0
   I111III += len ( Iiiiii )
   if 59 - 59: Ii - i1IiiiI1iI * I1ii11iIi11i % ooo0O + ooOoO0O00
   if 30 - 30: oOOoOooOo / iiiiiiii1
   if I111III > 0 :
    if 66 - 66: oOOoOooOo / I11i1ii1 * iI11I1II1I1I
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( I111III ) + " files found" , "Do you want to delete them?" ) :
     if 42 - 42: O0Oooo0O - Ii % IIiIiII11i * oOOoOooOo . o0o00Oo0O % i1IiiiI1iI
     for OOOO0OOO in Iiiiii :
      os . unlink ( os . path . join ( Ooo00OoO0O00 , OOOO0OOO ) )
     for OoOOoo0 in O00oOOO0 :
      shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , OoOOoo0 ) )
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
 I1Iii11111I1iii ( )
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
def o0OoOO ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 oOOoOoooOo0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( oOOoOoooOo0o ) :
   I111III = 0
   I111III += len ( Iiiiii )
   if 75 - 75: IIiIiII11i / iI11I1II1I1I / ii
   if 61 - 61: I11i1ii1 . I11i1ii1
   if I111III > 0 :
    if 17 - 17: iii1i1iiiiIi % I1ii11iIi11i / O0Oooo0O . i1iIi % oOo
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( I111III ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: oOo0O0Ooo + oOOoOooOo / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
     for OOOO0OOO in Iiiiii :
      os . unlink ( os . path . join ( Ooo00OoO0O00 , OOOO0OOO ) )
     for OoOOoo0 in O00oOOO0 :
      shutil . rmtree ( os . path . join ( Ooo00OoO0O00 , OoOOoo0 ) )
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
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11OOo0oO = os . path . join ( OOoOooOoOOOoo , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 oo0o00oOo0 = os . path . join ( OOoOooOoOOOoo , 'advancedsettings.xml.bak' )
 if os . path . exists ( oo0o00oOo0 ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + oo00 + ' - ADVANCED XML###'
   OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iii11OOo0oO = os . path . join ( OOoOooOoOOOoo , 'advancedsettings.xml' )
   try :
    os . remove ( iii11OOo0oO )
    print '=== GenieTv - REMOVING    ' + str ( iii11OOo0oO ) + '    ==='
   except :
    pass
   IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
   iiI11Iii = open ( iii11OOo0oO , "w" )
   iiI11Iii . write ( IIIi1I1IIii1II )
   iiI11Iii . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iii11OOo0oO ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 else :
  print '###' + oo00 + ' - ADVANCED XML###'
  OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iii11OOo0oO = os . path . join ( OOoOooOoOOOoo , 'advancedsettings.xml' )
  try :
   os . remove ( iii11OOo0oO )
   print '=== GenieTv - REMOVING    ' + str ( iii11OOo0oO ) + '    ==='
  except :
   pass
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iiI11Iii = open ( iii11OOo0oO , "w" )
  iiI11Iii . write ( IIIi1I1IIii1II )
  iiI11Iii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11OOo0oO ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 return
 if 86 - 86: o0o00Oo0O + o0o00Oo0O / i1IiiiI1iI - iI11I1II1I1I
def iII1ii111I ( url , name ) :
 print '###' + oo00 + ' - CHECK ADVANCE XML###'
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11OOo0oO = os . path . join ( OOoOooOoOOOoo , 'advancedsettings.xml' )
 try :
  iiI11Iii = open ( iii11OOo0oO ) . read ( )
  if 'zero' in iiI11Iii :
   name = '0CACHE'
  elif 'tuxen' in iiI11Iii :
   name = 'TUXENS'
  elif 'muckys' in iiI11Iii :
   name = 'MUCKYS'
  elif 'p2p1' in iiI11Iii :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iiI11Iii :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iiI11Iii :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( oo00 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 14 - 14: i1IiiiI1iI . iI11I1II1I1I + O0Oooo0O % ii
def IIi11I ( url ) :
 print '###' + oo00 + ' - DELETING ADVANCE XML###'
 OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11OOo0oO = os . path . join ( OOoOooOoOOOoo , 'advancedsettings.xml' )
 try :
  os . remove ( iii11OOo0oO )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iii11OOo0oO ) + '    ==='
  iI111I11I1I1 . ok ( oo00 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "       No Advanced Settings To Remove" )
 return
 if 39 - 39: ooo0O
 if 64 - 64: i1IiiiI1iI % Ii % oOoO0o00OO0
 if 14 - 14: O0Oooo0O - iii1i1iiiiIi - oOoO0o00OO0 % i1IiiiI1iI + ii
 if 4 - 4: O0Oooo0O - oOo0O0Ooo / iI11I1II1I1I + oOoO0o00OO0 % iI11I1II1I1I * oOo0O0Ooo
 if 30 - 30: Ii % OoOo0o
 if 52 - 52: i1IiiiI1iI - OOOo00oo0oO . Ii - IIiIiII11i + i1iIi . iiiiiiii1
 if 27 - 27: oOo0O0Ooo + iii1i1iiiiIi + iiiiiiii1
 if 70 - 70: i1IiiiI1iI + I11i1ii1 . oOOoOooOo - oOoO0o00OO0
 if 34 - 34: ooOoO0O00 % I1ii11iIi11i . OOOo00oo0oO
 if 36 - 36: oOoO0o00OO0 / O0Oooo0O - I11i1ii1 + OoOo0o + O0Oooo0O
def OOo00 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iI111i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for oOOOOO0 , i1iIIII11I , I11ii1IIiIi , i111I in iI111i :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % oOOOOO0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I11ii1IIiIi , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % i111I )
  inc = inc + 1
  if 80 - 80: oOoO0o00OO0 % oOoO0o00OO0 * oOoO0o00OO0 / IIiIiII11i % iiiiiiii1
  if 74 - 74: oOo / oOoO0o00OO0 - oOOoOooOo * ooOoO0O00 + oOoO0o00OO0 . i1IiiiI1iI
  if 13 - 13: iiiiiiii1 + ooo0O / iiiiiiii1 - i1iIi - iiiiiiii1
  if 34 - 34: I11i1ii1 . OoOo0o + OoOo0o - ii * O0Oooo0O
  if 72 - 72: iI11I1II1I1I % ooOoO0O00 / oOo / oOo0O0Ooo - IIiIiII11i - O0Oooo0O
  if 43 - 43: ooo0O - I1ii11iIi11i - oOoO0o00OO0 / IIiIiII11i + oOo0O0Ooo / oOoO0o00OO0
  if 34 - 34: I1ii11iIi11i
  if 21 - 21: oOo0O0Ooo / oOo0O0Ooo % O0Oooo0O - iii1i1iiiiIi % iii1i1iiiiIi - IIiIiII11i
  if 97 - 97: OOOo00oo0oO
def o0Ooo0oOOooO ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + oo00 + ' - CUSTOM FTV INI###'
  OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iii11OOo0oO = os . path . join ( OOoOooOoOOOoo , 'addons2.ini' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iiI11Iii = open ( iii11OOo0oO , "w" )
  iiI11Iii . write ( IIIi1I1IIii1II )
  iiI11Iii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11OOo0oO ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New .ini File" )
 return
 if 36 - 36: i1iIi % oOo
def OOo00o0 ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + oo00 + ' - CUSTOM FTV SETTINGS###'
  OOoOooOoOOOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iii11OOo0oO = os . path . join ( OOoOooOoOOOoo , 'settings.xml' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iiI11Iii = open ( iii11OOo0oO , "w" )
  iiI11Iii . write ( IIIi1I1IIii1II )
  iiI11Iii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11OOo0oO ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New Settings" )
 return
 if 36 - 36: iiiiiiii1 / ii + i1iIi . oOo0O0Ooo
 if 48 - 48: IIiIiII11i / IIiIiII11i . i1IiiiI1iI - oOo0O0Ooo
def oOOOoO ( ) :
 try :
  iIiii1Ii1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iIiii1Ii1 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    o0OOooOooo = os . path . join ( iIiii1Ii1 , "source.db" )
    os . unlink ( o0OOooOooo )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "               Error Deleting Database No Database To Delete" )
 return
 if 40 - 40: I11i1ii1 + iiiiiiii1 * i1IiiiI1iI + iii1i1iiiiIi
 if 5 - 5: O0Oooo0O / I11i1ii1
 if 30 - 30: OoOo0o . iiiiiiii1 % oOo + OOOo00oo0oO
 if 69 - 69: Ii + I11i1ii1 * oOOoOooOo * iiiiiiii1 % OOOo00oo0oO
 if 66 - 66: OoOo0o * I11i1ii1 + o0o00Oo0O - ii
def i11111IIIII ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 19 - 19: I1ii11iIi11i * iii1i1iiiiIi
 if 52 - 52: oOo + OOOo00oo0oO
 if 84 - 84: o0o00Oo0O % oOoO0o00OO0 % iI11I1II1I1I - iii1i1iiiiIi - I1ii11iIi11i
 if 7 - 7: IIiIiII11i % OOOo00oo0oO % ooOoO0O00 . iI11I1II1I1I
 if 92 - 92: i1iIi / ooo0O % OoOo0o - iii1i1iiiiIi
 if 44 - 44: oOo0O0Ooo + iii1i1iiiiIi * I1ii11iIi11i
 if 31 - 31: i1IiiiI1iI - oOo0O0Ooo - oOo * iii1i1iiiiIi
def I1 ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; iI111iO00oooO = pluginmessage_yes_no ( oo00 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iI111iO00oooO :
  Ii1II11Ii = xbmcaddon . Addon ( id = iiIIIII1i1iI ) . getAddonInfo ( 'path' ) ; Ii1II11Ii = xbmc . translatePath ( Ii1II11Ii ) ;
  O0Oo0OOOo = os . path . join ( Ii1II11Ii , ".." , ".." ) ; O0Oo0OOOo = os . path . abspath ( O0Oo0OOOo ) ; pluginlog ( "freshstart.main_list xbmcPath=" + O0Oo0OOOo ) ; IIiI1IiIi1 = False
  try :
   for Ooo00OoO0O00 , O00oOOO0 , Iiiiii in os . walk ( O0Oo0OOOo , topdown = True ) :
    O00oOOO0 [ : ] = [ OoOOoo0 for OoOOoo0 in O00oOOO0 if OoOOoo0 not in i1i1II ]
    for O000OOO in Iiiiii :
     try : os . remove ( os . path . join ( Ooo00OoO0O00 , O000OOO ) )
     except :
      if O000OOO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIiI1IiIi1 = True
      pluginlog ( "Error removing " + Ooo00OoO0O00 + " " + O000OOO )
    for O000OOO in O00oOOO0 :
     try : os . rmdir ( os . path . join ( Ooo00OoO0O00 , O000OOO ) )
     except :
      if O000OOO not in [ "Database" , "userdata" ] : IIiI1IiIi1 = True
      pluginlog ( "Error removing " + Ooo00OoO0O00 + " " + O000OOO )
   if not IIiI1IiIi1 : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( oo00 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( oo00 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 oo000oiIIIII ( )
 if 54 - 54: Ii + i1IiiiI1iI % iiiiiiii1 % oOoO0o00OO0 + I1ii11iIi11i % ooo0O
 if 66 - 66: I11i1ii1 . O0Oooo0O - OOOo00oo0oO
 if 12 - 12: ooOoO0O00 / i1IiiiI1iI
def OoOo00O ( ) :
 o0O00ooO0O0Oo = [ ]
 ooOo0ooO0Oo = sys . argv [ 2 ]
 if len ( ooOo0ooO0Oo ) >= 2 :
  I1O0 = sys . argv [ 2 ]
  II1iiI1iIii1i = I1O0 . replace ( '?' , '' )
  if ( I1O0 [ len ( I1O0 ) - 1 ] == '/' ) :
   I1O0 = I1O0 [ 0 : len ( I1O0 ) - 2 ]
  ooO0OO0OoO0 = II1iiI1iIii1i . split ( '&' )
  o0O00ooO0O0Oo = { }
  for OooOoOo in range ( len ( ooO0OO0OoO0 ) ) :
   IIIIIi = { }
   IIIIIi = ooO0OO0OoO0 [ OooOoOo ] . split ( '=' )
   if ( len ( IIIIIi ) ) == 2 :
    o0O00ooO0O0Oo [ IIIIIi [ 0 ] ] = IIIIIi [ 1 ]
    if 54 - 54: ooOoO0O00 . iiiiiiii1
 return o0O00ooO0O0Oo
 if 83 - 83: o0o00Oo0O - OOOo00oo0oO / oOo0O0Ooo * oOo0O0Ooo + OOOo00oo0oO
Ii11I111i1i11 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
ooo000 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ii1IIi1iI1ii1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O0oOO0Oo0O0O = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iI1i1iii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
O000OO0I11 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o000oOOoooo0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OoOi1I1I1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
Oooo0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o000oO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
i1iIOo0oOOo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1Ii1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
IIii11 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0o0O00OO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiII11iI11i1I = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i1iIII1i1II = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OoOo0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
ii11IiIII = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i11iII1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
Oo000o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OOI1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iIOoo000 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1Ii1i111I = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oO0OO00O0 = base64 . decodestring ( 'Q1VOVA==' )
def ii1ii1I11Ii ( display , mode = None , name = None , url = None , menu = None , description = oOo0oooo00o , overwrite = True , fanart = Oo00OOOOO , icon = O0O , themeit = None ) :
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
def o00OOO0o00OO ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 Ii1I1I1i11ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 OoOo0oO0o = True
 o0OoOo00ooO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 o0OoOo00ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 o0OoOo00ooO . setProperty ( 'fanart_image' , fanart )
 o0OoOo00ooO . setProperty ( "IsPlayable" , "true" )
 o0oo0OoOO0Ooo = [ ]
 o0oo0OoOO0Ooo . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 o0oo0OoOO0Ooo . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 o0OoOo00ooO . addContextMenuItems ( o0oo0OoOO0Ooo , replaceItems = True )
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
 if 78 - 78: o0o00Oo0O + I1ii11iIi11i
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
 if 14 - 14: o0o00Oo0O
 if 67 - 67: IIiIiII11i / o0o00Oo0O
I1O0 = OoOo00O ( )
IIo0o0O0O00oOOo = None
O000OOO = None
O00O0 = None
i1i1II1i11 = None
iI1iIii11Ii = None
II1 = None
iiIiiIi1 = None
iiIiOo0oO0 = None
if 67 - 67: ooo0O . I1ii11iIi11i % i1IiiiI1iI
if 38 - 38: OoOo0o - oOo . oOOoOooOo
try :
 iiIiOo0oO0 = int ( I1O0 [ "fav_mode" ] )
except :
 pass
 if 50 - 50: ooo0O
try :
 IIo0o0O0O00oOOo = urllib . unquote_plus ( I1O0 [ "url" ] )
except :
 pass
try :
 O000OOO = urllib . unquote_plus ( I1O0 [ "name" ] )
except :
 pass
try :
 i1i1II1i11 = urllib . unquote_plus ( I1O0 [ "iconimage" ] )
except :
 pass
try :
 O00O0 = int ( I1O0 [ "mode" ] )
except :
 pass
try :
 iI1iIii11Ii = urllib . unquote_plus ( I1O0 [ "fanart" ] )
except :
 pass
try :
 II1 = urllib . unquote_plus ( I1O0 [ "description" ] )
except :
 pass
 if 85 - 85: IIiIiII11i . iiiiiiii1 - ooOoO0O00
 if 23 - 23: iiiiiiii1 . i1iIi - oOo / oOoO0o00OO0 / o0o00Oo0O
print str ( I11II1i ) + ': ' + str ( I1IiI )
print "Mode: " + str ( O00O0 )
print "URL: " + str ( IIo0o0O0O00oOOo )
print "Name: " + str ( O000OOO )
print "IconImage: " + str ( i1i1II1i11 )
if 4 - 4: ooOoO0O00 % I1ii11iIi11i % i1iIi * oOOoOooOo - i1IiiiI1iI
if 76 - 76: iI11I1II1I1I / oOOoOooOo % oOoO0o00OO0 % OoOo0o
def iIiIi11 ( content , viewType ) :
 if 13 - 13: I11i1ii1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 56 - 56: I1ii11iIi11i
if i1i1II1i11 == None : i1i1II1i11 = O0O
if iI1iIii11Ii == None : iI1iIii11Ii = Oo00OOOOO
if O00O0 == None :
 O00o0OO0 ( )
 if 55 - 55: Ii + iI11I1II1I1I / ooOoO0O00 / oOoO0o00OO0
elif O00O0 == 1 :
 IIiii1I1I ( IIo0o0O0O00oOOo )
 if 64 - 64: I11i1ii1 . oOo * Ii
elif O00O0 == 44 :
 iIi1IiII ( IIo0o0O0O00oOOo )
 if 18 - 18: i1iIi % ooo0O - I1ii11iIi11i
elif O00O0 == 2 :
 I1iI1I1111i ( )
 if 28 - 28: I11i1ii1
elif O00O0 == 3 :
 I1iO00O000oOO0oO ( )
 if 93 - 93: I1ii11iIi11i % ooOoO0O00
elif O00O0 == 21 :
 Iii1ii1II11i ( )
 if 51 - 51: OOOo00oo0oO % o0o00Oo0O
elif O00O0 == 4 :
 iIiii1IIi1I ( )
 if 41 - 41: oOo0O0Ooo * oOo0O0Ooo . O0Oooo0O
elif O00O0 == 5 :
 IiI1 ( IIo0o0O0O00oOOo )
 if 38 - 38: oOo0O0Ooo % Ii
elif O00O0 == 6 :
 IIIi1i1iIIIi ( IIo0o0O0O00oOOo )
 if 17 - 17: Ii
elif O00O0 == 7 :
 ii1iII11 ( IIo0o0O0O00oOOo , O000OOO )
 if 81 - 81: O0Oooo0O
elif O00O0 == 8 :
 iII1ii111I ( IIo0o0O0O00oOOo , O000OOO )
 if 25 - 25: oOo0O0Ooo
elif O00O0 == 9 :
 FIXREPOSADDONS ( IIo0o0O0O00oOOo )
 if 52 - 52: oOoO0o00OO0 % ooOoO0O00 . I11i1ii1 % iii1i1iiiiIi
elif O00O0 == 10 :
 O0O0Oo00 ( )
 if 50 - 50: OoOo0o * oOo0O0Ooo / ooo0O
elif O00O0 == 11 :
 IIi11I ( IIo0o0O0O00oOOo )
 if 91 - 91: iI11I1II1I1I / OoOo0o * o0o00Oo0O . ooo0O + OOOo00oo0oO / oOoO0o00OO0
elif O00O0 == 12 :
 OOo00 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 33 - 33: IIiIiII11i + i1iIi
elif O00O0 == 13 :
 i1Ii11I ( )
 if 46 - 46: I11i1ii1 + o0o00Oo0O + ooOoO0O00 + oOOoOooOo / iiiiiiii1
elif O00O0 == 14 :
 IiiIiiii ( IIo0o0O0O00oOOo )
 if 94 - 94: OOOo00oo0oO + iiiiiiii1 * iii1i1iiiiIi - ooOoO0O00 / ii
elif O00O0 == 15 :
 ii11I ( )
 if 59 - 59: i1IiiiI1iI % i1iIi / iii1i1iiiiIi
elif O00O0 == 16 :
 o0Ooo0oOOooO ( IIo0o0O0O00oOOo , O000OOO )
 if 99 - 99: i1iIi + IIiIiII11i / Ii - I11i1ii1 / iiiiiiii1 + iiiiiiii1
elif O00O0 == 17 :
 OOo00o0 ( IIo0o0O0O00oOOo , O000OOO )
 if 55 - 55: I11i1ii1 + ii * oOoO0o00OO0 . I11i1ii1 * oOoO0o00OO0 + I11i1ii1
elif O00O0 == 18 :
 oOOOoO ( )
 if 81 - 81: iI11I1II1I1I . oOOoOooOo + iii1i1iiiiIi
elif O00O0 == 19 :
 o00O0o0oo0 ( IIo0o0O0O00oOOo )
 if 31 - 31: i1IiiiI1iI / iii1i1iiiiIi + ooo0O
elif O00O0 == 40 :
 iIIii ( O000OOO , IIo0o0O0O00oOOo , II1 )
 if 80 - 80: I1ii11iIi11i
elif O00O0 == 42 :
 oOOOOiI ( O000OOO , IIo0o0O0O00oOOo , II1 )
 if 58 - 58: O0Oooo0O + OoOo0o
elif O00O0 == 43 :
 O0O0o0o0oo0O ( IIo0o0O0O00oOOo )
 if 76 - 76: IIiIiII11i - ooo0O % oOo + iiiiiiii1
elif O00O0 == 20 :
 ii1IIi1IIIIi1 ( IIo0o0O0O00oOOo )
 if 38 - 38: O0Oooo0O - i1IiiiI1iI * ooOoO0O00 + iI11I1II1I1I
elif O00O0 == 22 :
 IIIIi11 ( IIo0o0O0O00oOOo )
 if 41 - 41: i1iIi . oOo + oOoO0o00OO0 + iii1i1iiiiIi
elif O00O0 == 23 :
 IIi1III11I1Ii ( IIo0o0O0O00oOOo )
 if 76 - 76: iiiiiiii1 - iI11I1II1I1I
elif O00O0 == 24 :
 Oo0ooO ( IIo0o0O0O00oOOo )
 if 23 - 23: i1IiiiI1iI / oOo % OoOo0o
elif O00O0 == 25 :
 o0O0oO00oo0O ( IIo0o0O0O00oOOo )
 if 9 - 9: oOOoOooOo % oOoO0o00OO0 . ii + oOo % OoOo0o * ii
elif O00O0 == 26 :
 OOO0 ( IIo0o0O0O00oOOo )
 if 21 - 21: i1iIi % o0o00Oo0O
elif O00O0 == 27 :
 ii1111I ( IIo0o0O0O00oOOo )
 if 15 - 15: IIiIiII11i * i1iIi + I11i1ii1 % iiiiiiii1
elif O00O0 == 28 :
 oOOOO0oO0o0 ( IIo0o0O0O00oOOo )
 if 96 - 96: IIiIiII11i * O0Oooo0O / I1ii11iIi11i
elif O00O0 == 29 :
 o0O0iIi ( IIo0o0O0O00oOOo )
 if 35 - 35: oOo0O0Ooo
elif O00O0 == 30 :
 i11iI1111ii1I ( IIo0o0O0O00oOOo )
 if 54 - 54: oOoO0o00OO0 % ooo0O . ooOoO0O00
elif O00O0 == 31 :
 Iiii11i11 ( IIo0o0O0O00oOOo )
 if 72 - 72: i1iIi
elif O00O0 == 32 :
 I111I ( )
 if 87 - 87: iiiiiiii1 - oOo0O0Ooo
elif O00O0 == 33 :
 oooO ( )
 if 54 - 54: iI11I1II1I1I + OOOo00oo0oO * ooo0O % ii . I1ii11iIi11i
elif O00O0 == 35 :
 oO00oO0 ( IIo0o0O0O00oOOo )
 if 32 - 32: iiiiiiii1
elif O00O0 == 34 :
 oo0OOoOo0 ( IIo0o0O0O00oOOo )
 if 33 - 33: oOOoOooOo + I1ii11iIi11i * iii1i1iiiiIi % oOOoOooOo * OOOo00oo0oO - oOo
elif O00O0 == 36 :
 IiIIi ( IIo0o0O0O00oOOo )
 if 40 - 40: i1IiiiI1iI . ii * o0o00Oo0O / O0Oooo0O + o0o00Oo0O
elif O00O0 == 37 :
 Ii11i1I1 ( IIo0o0O0O00oOOo )
 if 97 - 97: oOOoOooOo - oOOoOooOo * OoOo0o % iii1i1iiiiIi - iii1i1iiiiIi - O0Oooo0O
elif O00O0 == 38 :
 oOooOOoo ( IIo0o0O0O00oOOo )
 if 52 - 52: o0o00Oo0O % iiiiiiii1
elif O00O0 == 41 :
 I1 ( I1O0 )
 if 81 - 81: ii % iii1i1iiiiIi % I1ii11iIi11i - oOo0O0Ooo
elif O00O0 == 39 :
 iiI ( IIo0o0O0O00oOOo )
 if 43 - 43: ooo0O % ooo0O
elif O00O0 == 45 :
 TEXTS ( )
 if 48 - 48: o0o00Oo0O
elif O00O0 == 46 :
 oOoo0oOo00 ( )
 if 5 - 5: OoOo0o / Ii . i1IiiiI1iI % OoOo0o
elif O00O0 == 47 :
 GEVID ( )
 if 1 - 1: IIiIiII11i + o0o00Oo0O * iii1i1iiiiIi / I11i1ii1 . o0o00Oo0O
elif O00O0 == 48 :
 oO0o00O ( O000OOO , IIo0o0O0O00oOOo , II1 )
 if 87 - 87: I11i1ii1 + oOo0O0Ooo
elif O00O0 == 49 :
 oOo00Oo0o0Oo ( )
 if 74 - 74: oOo + oOo % iiiiiiii1 / i1IiiiI1iI / o0o00Oo0O
elif O00O0 == 22222 :
 O00o0o ( IIo0o0O0O00oOOo )
 if 54 - 54: ooo0O / ii * oOOoOooOo . iii1i1iiiiIi - O0Oooo0O
elif O00O0 == 222225 :
 i11i11 ( IIo0o0O0O00oOOo )
 if 69 - 69: OOOo00oo0oO - oOo
elif O00O0 == 222 :
 oO00oo0o ( IIo0o0O0O00oOOo )
 if 80 - 80: oOOoOooOo + iI11I1II1I1I . IIiIiII11i + oOo0O0Ooo - OOOo00oo0oO % iii1i1iiiiIi
elif O00O0 == 2222222 :
 OOIi1iI111II1I1 ( IIo0o0O0O00oOOo )
 if 10 - 10: iI11I1II1I1I
elif O00O0 == 222222 :
 i1iIi11 ( IIo0o0O0O00oOOo , O000OOO )
 if 44 - 44: iii1i1iiiiIi * OOOo00oo0oO . oOoO0o00OO0 + Ii
elif O00O0 == 333 :
 ii11IoOo0O0Oo ( IIo0o0O0O00oOOo )
 if 85 - 85: i1IiiiI1iI
 if 36 - 36: oOOoOooOo % oOo
elif O00O0 == 1020 :
 OoOooOOooO ( )
 if 1 - 1: ii - iii1i1iiiiIi
elif O00O0 == 1021 :
 ANIMEEP ( )
 if 35 - 35: O0Oooo0O
elif O00O0 == 1022 :
 ANIMEPLAY ( IIo0o0O0O00oOOo )
 if 35 - 35: I1ii11iIi11i - iI11I1II1I1I / ooOoO0O00 + oOo - ii / Ii
elif O00O0 == 1001 :
 oOO0o00 ( )
 if 79 - 79: oOo0O0Ooo * oOOoOooOo * oOOoOooOo
elif O00O0 == 1005 :
 O0ii1IIIiiI1i ( )
 if 92 - 92: iiiiiiii1 % oOoO0o00OO0
elif O00O0 == 1007 :
 Iiii1I ( IIo0o0O0O00oOOo )
 if 16 - 16: OOOo00oo0oO
elif O00O0 == 1010 :
 oOoo ( IIo0o0O0O00oOOo )
 if 52 - 52: ii % oOOoOooOo - O0Oooo0O * i1IiiiI1iI
elif O00O0 == 1011 :
 Ii1oo ( IIo0o0O0O00oOOo )
 if 24 - 24: i1iIi + I11i1ii1 + ii / OOOo00oo0oO / oOo0O0Ooo + I11i1ii1
elif O00O0 == 1012 :
 II1i1iIIi1 ( IIo0o0O0O00oOOo )
 if 52 - 52: oOOoOooOo
elif O00O0 == 1030 :
 I111I11iiI ( )
 if 38 - 38: oOo + oOo0O0Ooo % I11i1ii1
elif O00O0 == 1031 :
 oOoOOooo0OOO ( IIo0o0O0O00oOOo , i1i1II1i11 )
 if 87 - 87: OOOo00oo0oO * i1iIi - O0Oooo0O / OOOo00oo0oO
elif O00O0 == 1032 :
 IiI1iI1 ( IIo0o0O0O00oOOo )
 if 65 - 65: iii1i1iiiiIi
elif O00O0 == 1006 :
 Parse . ParseURL ( IIo0o0O0O00oOOo )
 if 87 - 87: i1IiiiI1iI - Ii - OoOo0o . iii1i1iiiiIi + I11i1ii1 . oOo
elif O00O0 == 2030 :
 Parse . addonParseURL ( IIo0o0O0O00oOOo )
 if 70 - 70: iI11I1II1I1I % ii / oOo . o0o00Oo0O - i1IiiiI1iI % IIiIiII11i
elif O00O0 == 2031 :
 Parse . apkParseURL ( IIo0o0O0O00oOOo )
 if 84 - 84: OoOo0o * ooOoO0O00 . iI11I1II1I1I * iiiiiiii1 + O0Oooo0O + IIiIiII11i
elif O00O0 == 2032 :
 Parse . ParseBOSS ( IIo0o0O0O00oOOo )
 if 97 - 97: i1iIi - I11i1ii1
elif O00O0 == 1002 :
 ii1I1IIiii ( IIo0o0O0O00oOOo )
 if 64 - 64: OOOo00oo0oO . oOOoOooOo / oOOoOooOo - IIiIiII11i
elif O00O0 == 1003 :
 i1io0ooO0OO ( IIo0o0O0O00oOOo , i1i1II1i11 )
 if 81 - 81: oOoO0o00OO0
elif O00O0 == 1004 :
 I1IiI1i1Iii ( IIo0o0O0O00oOOo )
 if 64 - 64: OOOo00oo0oO * oOo / OoOo0o + i1iIi % I1ii11iIi11i . I11i1ii1
elif O00O0 == 1008 :
 I1iI1II1I1i ( )
 if 2 - 2: O0Oooo0O + i1IiiiI1iI
elif O00O0 == 1009 :
 Ooo0O00 ( IIo0o0O0O00oOOo )
 if 47 - 47: Ii + iI11I1II1I1I % oOoO0o00OO0 - OOOo00oo0oO % oOo
elif O00O0 == 2001 :
 iii1II1iI1III ( )
 if 85 - 85: OOOo00oo0oO * iii1i1iiiiIi / iii1i1iiiiIi
elif O00O0 == 2002 :
 IioooO ( IIo0o0O0O00oOOo )
 if 85 - 85: OoOo0o / O0Oooo0O . ooOoO0O00 / iii1i1iiiiIi + iI11I1II1I1I
elif O00O0 == 1013 :
 I11iiI11I1II ( )
elif O00O0 == 10111113 :
 Oo0o0OoOoOo0 ( IIo0o0O0O00oOOo )
 if 71 - 71: oOo
elif O00O0 == 1014 :
 ii1iiiIIiIII ( )
 if 96 - 96: oOoO0o00OO0 / oOo0O0Ooo - oOoO0o00OO0 / IIiIiII11i - I11i1ii1
elif O00O0 == 1015 :
 i1i1iiI11I ( IIo0o0O0O00oOOo )
 if 74 - 74: i1iIi * ii % OoOo0o + ii + iiiiiiii1
elif O00O0 == 1016 :
 i11ii1Ii1 ( IIo0o0O0O00oOOo , i1i1II1i11 , O000OOO )
 if 83 - 83: ooOoO0O00
elif O00O0 == 1017 :
 i1I1iIi1IiI ( )
 if 2 - 2: ooOoO0O00 / OoOo0o * o0o00Oo0O
elif O00O0 == 1018 :
 i1111O0O000OOOo ( IIo0o0O0O00oOOo )
 if 99 - 99: ii . iii1i1iiiiIi / IIiIiII11i
elif O00O0 == 1019 :
 iiIiI ( IIo0o0O0O00oOOo )
elif O00O0 == 10190 :
 ii1 ( IIo0o0O0O00oOOo )
 if 64 - 64: iiiiiiii1 / ooOoO0O00 . oOo0O0Ooo + o0o00Oo0O
elif O00O0 == 1023 :
 Oo0O0o00o00 ( )
 if 5 - 5: o0o00Oo0O . Ii
elif O00O0 == 1024 :
 IIoOOOoOoOO ( IIo0o0O0O00oOOo )
 if 71 - 71: ooo0O + iiiiiiii1 + oOOoOooOo
elif O00O0 == 1025 :
 iI1iIII1i1II ( IIo0o0O0O00oOOo )
 if 27 - 27: ii . iiiiiiii1 * O0Oooo0O % o0o00Oo0O + ii - iiiiiiii1
elif O00O0 == 4001 :
 ii1Ii1IiIIi ( )
 if 86 - 86: ooOoO0O00
elif O00O0 == 4002 :
 iIi1i ( )
 if 81 - 81: iii1i1iiiiIi
elif O00O0 == 4003 :
 O00oOo0o0 ( )
 if 52 - 52: iiiiiiii1 * I11i1ii1 % oOo0O0Ooo * i1IiiiI1iI
elif O00O0 == 4004 :
 IiIIIII11I ( )
 if 73 - 73: O0Oooo0O * oOOoOooOo
elif O00O0 == 4005 :
 oo0OOOoOo ( )
 if 62 - 62: OoOo0o . oOo0O0Ooo * iI11I1II1I1I + oOo * oOOoOooOo / OOOo00oo0oO
elif O00O0 == 4006 :
 O0OOOo ( )
 if 14 - 14: iiiiiiii1 / oOo
elif O00O0 == 4007 :
 iIi ( )
 if 75 - 75: I11i1ii1
elif O00O0 == 4008 :
 oOooo ( )
 if 68 - 68: I11i1ii1 - ooOoO0O00 % I11i1ii1 . oOo . Ii . ii
elif O00O0 == 40099 : oOOoO0O ( )
elif O00O0 == 4009 : III1IIIIIiiI ( )
elif O00O0 == 4010 : ii1Io0oOO0 ( )
elif O00O0 == 3000 :
 IioO ( )
 if 32 - 32: iiiiiiii1 + oOo % I11i1ii1 + oOo0O0Ooo
elif O00O0 == 3001 :
 oO0OOOo0OO ( )
 if 69 - 69: O0Oooo0O + i1IiiiI1iI - iI11I1II1I1I - IIiIiII11i . i1iIi
elif O00O0 == 3002 :
 i1IiI ( IIo0o0O0O00oOOo )
 if 74 - 74: oOoO0o00OO0 % ooo0O + o0o00Oo0O - Ii - I11i1ii1 % OoOo0o
elif O00O0 == 3003 :
 I1iI1i ( IIo0o0O0O00oOOo )
 if 39 - 39: oOo - ooo0O
elif O00O0 == 3004 :
 i11i1IIi ( IIo0o0O0O00oOOo )
 if 71 - 71: iiiiiiii1 . oOo + oOOoOooOo - OoOo0o - I1ii11iIi11i
elif O00O0 == 404 :
 iI1i1iIii1 ( O000OOO , IIo0o0O0O00oOOo , i1i1II1i11 )
 if 100 - 100: ii - ooo0O + O0Oooo0O . ii % Ii
elif O00O0 == 405 :
 iI1Ii ( IIo0o0O0O00oOOo )
 if 64 - 64: O0Oooo0O % ii / ooOoO0O00 / oOo
elif O00O0 == 7030 :
 o00oOo0O0O0 ( )
 if 2 - 2: i1IiiiI1iI % ooo0O . oOo . oOo
elif O00O0 == 7021 :
 OOoI1I ( O000OOO )
 if 89 - 89: oOOoOooOo - OOOo00oo0oO + IIiIiII11i + oOo - I11i1ii1
elif O00O0 == 7022 :
 iIIiii ( O000OOO )
 if 27 - 27: O0Oooo0O - ooo0O + oOo
elif O00O0 == 7000 :
 i1IOO00OOOO00oOO ( O000OOO , IIo0o0O0O00oOOo , img )
 if 38 - 38: iii1i1iiiiIi + oOo . Ii + i1iIi % ooOoO0O00 % oOo0O0Ooo
elif O00O0 == 7050 :
 oO0iII1i111iI ( IIo0o0O0O00oOOo )
 if 93 - 93: Ii
elif O00O0 == 7051 :
 i1i1O0 ( IIo0o0O0O00oOOo )
 if 63 - 63: iI11I1II1I1I - iI11I1II1I1I % ooo0O
elif O00O0 == 70511 :
 WATCHLIST2 ( IIo0o0O0O00oOOo )
 if 97 - 97: ooOoO0O00 % i1IiiiI1iI % iii1i1iiiiIi
elif O00O0 == 7052 :
 oO0Ooo ( IIo0o0O0O00oOOo )
 if 25 - 25: iii1i1iiiiIi . iI11I1II1I1I - iiiiiiii1 % IIiIiII11i . iii1i1iiiiIi
elif O00O0 == 7053 :
 iiiiIIiiII1Iii1 ( IIo0o0O0O00oOOo )
 if 16 - 16: OoOo0o . I1ii11iIi11i . oOo0O0Ooo % o0o00Oo0O . oOoO0o00OO0 + Ii
elif O00O0 == 7054 :
 CoolPlay ( IIo0o0O0O00oOOo )
 if 100 - 100: oOoO0o00OO0 - ooOoO0O00 - oOo * ooo0O + iii1i1iiiiIi
elif O00O0 == 7060 :
 oOIIIiIII111iii ( )
 if 31 - 31: ooOoO0O00
elif O00O0 == 7061 :
 IiiIi11 ( IIo0o0O0O00oOOo )
 if 21 - 21: ooo0O / o0o00Oo0O % o0o00Oo0O . ii / oOo0O0Ooo
elif O00O0 == 7063 :
 oOOiI ( IIo0o0O0O00oOOo )
 if 94 - 94: oOOoOooOo + oOo / oOOoOooOo - oOOoOooOo + I1ii11iIi11i + ooo0O
elif O00O0 == 7062 :
 Oo0O0O000 ( IIo0o0O0O00oOOo )
 if 50 - 50: OOOo00oo0oO . I1ii11iIi11i
elif O00O0 == 7064 :
 NATatozcat ( )
 if 15 - 15: i1iIi
elif O00O0 == 7067 :
 oOO0oOo0OOoOO ( IIo0o0O0O00oOOo )
 if 64 - 64: ii
elif O00O0 == 7066 :
 NATatozA ( IIo0o0O0O00oOOo )
 if 25 - 25: I11i1ii1
elif O00O0 == 7065 :
 o0O00oo0Ooo ( IIo0o0O0O00oOOo )
 if 29 - 29: iii1i1iiiiIi % oOOoOooOo * ii
elif O00O0 == 7070 :
 I111i1IiI1 ( )
 if 8 - 8: Ii - O0Oooo0O / I11i1ii1
elif O00O0 == 7071 :
 DIZIlist ( IIo0o0O0O00oOOo )
 if 17 - 17: Ii * oOo . ooo0O . ii . iii1i1iiiiIi - oOoO0o00OO0
elif O00O0 == 7072 :
 DIZIpull ( IIo0o0O0O00oOOo )
 if 78 - 78: oOoO0o00OO0 - ii + o0o00Oo0O
elif O00O0 == 7073 :
 WATCHDIZI ( IIo0o0O0O00oOOo )
 if 15 - 15: oOoO0o00OO0 / I11i1ii1 % oOo0O0Ooo
elif O00O0 == 7002 :
 IiiiIi ( )
 if 16 - 16: i1iIi
elif O00O0 == 7003 :
 O0Oo ( IIo0o0O0O00oOOo )
 if 26 - 26: ooo0O / i1IiiiI1iI + iii1i1iiiiIi / iii1i1iiiiIi
elif O00O0 == 7004 :
 o0o0o ( IIo0o0O0O00oOOo )
 if 31 - 31: O0Oooo0O
elif O00O0 == 7020 :
 O0OI1i ( IIo0o0O0O00oOOo )
 if 84 - 84: Ii * OoOo0o . iiiiiiii1 - i1iIi * ooOoO0O00 - oOoO0o00OO0
elif O00O0 == 7001 :
 I1iii ( )
 if 1 - 1: IIiIiII11i
elif O00O0 == 7010 :
 iIii ( IIo0o0O0O00oOOo )
 if 94 - 94: oOoO0o00OO0 * iiiiiiii1 % iiiiiiii1 % i1IiiiI1iI - iiiiiiii1
elif O00O0 == 7011 :
 O000ooo ( IIo0o0O0O00oOOo )
 if 38 - 38: I11i1ii1 - oOo % i1iIi - IIiIiII11i
elif O00O0 == 7012 :
 II1Oooo00oO0OO0o ( IIo0o0O0O00oOOo )
 if 97 - 97: o0o00Oo0O . i1iIi
elif O00O0 == 7013 :
 cnfTVPlay2 ( IIo0o0O0O00oOOo )
elif O00O0 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( IIo0o0O0O00oOOo )
elif O00O0 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( IIo0o0O0O00oOOo )
elif O00O0 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( O000OOO , IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif O00O0 == 7018 :
 iIII11ii1i1i1 ( )
elif O00O0 == 7019 :
 CNF_Studio_Indexer . List_Movies ( IIo0o0O0O00oOOo )
elif O00O0 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( IIo0o0O0O00oOOo )
elif O00O0 == 7024 :
 CNF_Studio_Indexer . Box_Office ( IIo0o0O0O00oOOo )
 if 52 - 52: I11i1ii1
elif O00O0 == 8000 :
 ooOo000 ( )
elif O00O0 == 8001 :
 oOI1 ( )
elif O00O0 == 8002 :
 oOoo0OOoOoO0O ( )
elif O00O0 == 8003 :
 IIoo0O ( )
elif O00O0 == 8004 :
 i11Oo00 ( )
elif O00O0 == 8005 :
 oOOooOOO ( )
elif O00O0 == 8006 :
 iII11I11i ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 8030 :
 OoOoooOO00OO ( IIo0o0O0O00oOOo )
elif O00O0 == 8045 :
 i1I1iIIiIII ( IIo0o0O0O00oOOo )
elif O00O0 == 8046 :
 iI1i11i1i1i ( IIo0o0O0O00oOOo )
elif O00O0 == 8047 :
 o0iiiii1i1 ( IIo0o0O0O00oOOo )
elif O00O0 == 8048 :
 iI1II ( IIo0o0O0O00oOOo )
elif O00O0 == 8049 :
 OO0o0oO0 ( IIo0o0O0O00oOOo )
elif O00O0 == 804900 :
 o00o ( IIo0o0O0O00oOOo )
elif O00O0 == 8020 :
 IIiiI11iI ( )
elif O00O0 == 8021 :
 IIi1III1II ( IIo0o0O0O00oOOo )
elif O00O0 == 8022 :
 o0o0OOOO ( IIo0o0O0O00oOOo )
elif O00O0 == 8023 :
 I1i1iiIII1i1 ( IIo0o0O0O00oOOo )
elif O00O0 == 8040 :
 oo00OOoOoO00 ( )
elif O00O0 == 8041 :
 OOo ( IIo0o0O0O00oOOo )
elif O00O0 == 8042 :
 iII1i ( IIo0o0O0O00oOOo )
elif O00O0 == 8043 :
 yt . PlayVideo ( IIo0o0O0O00oOOo )
elif O00O0 == 8044 :
 OO00o0O0OO0o0 ( IIo0o0O0O00oOOo )
elif O00O0 == 8060 :
 OoooO0o ( )
elif O00O0 == 8061 :
 IiiiIii ( IIo0o0O0O00oOOo )
elif O00O0 == 8064 :
 IiIiIi1IIi ( )
elif O00O0 == 8065 :
 IIi1Iii ( IIo0o0O0O00oOOo )
elif O00O0 == 8070 :
 oO00oOOOO ( )
elif O00O0 == 8071 :
 o0o0OOO0ooo00 ( IIo0o0O0O00oOOo )
elif O00O0 == 7080 :
 I11III111i1I ( IIo0o0O0O00oOOo )
elif O00O0 == 8090 :
 i111 ( )
elif O00O0 == 8091 :
 O0Oo0O0O0o0 ( IIo0o0O0O00oOOo )
elif O00O0 == 8092 :
 i11oO0oOO000 ( IIo0o0O0O00oOOo )
elif O00O0 == 8093 :
 Oo0ooo0oOo0Oo0O ( IIo0o0O0O00oOOo )
elif O00O0 == 8081 :
 I1iII1IiI11i ( )
elif O00O0 == 8062 :
 ooOoo ( IIo0o0O0O00oOOo )
elif O00O0 == 8063 :
 o0oOII1i ( IIo0o0O0O00oOOo )
elif O00O0 == 8050 :
 OO0o0o ( )
elif O00O0 == 8051 :
 O0O0O00OoO0O ( IIo0o0O0O00oOOo )
elif O00O0 == 8052 :
 i1II11III ( IIo0o0O0O00oOOo )
elif O00O0 == 8085 :
 oO0oOOOOOO0ooOOOoo ( )
elif O00O0 == 8086 :
 ooOO0O00O ( IIo0o0O0O00oOOo )
elif O00O0 == 8087 :
 oOOOoOo0oOoo ( IIo0o0O0O00oOOo )
elif O00O0 == 8088 :
 OoOOOO0 ( IIo0o0O0O00oOOo , O000OOO )
elif O00O0 == 9000 :
 o0o0 ( )
elif O00O0 == 1111 :
 i1IIII1II ( )
elif O00O0 == 9001 :
 Ii1I11I ( )
elif O00O0 == 9002 :
 IIiiIIi1 ( )
elif O00O0 == 9003 :
 o0Ooo0Oooo0o ( )
elif O00O0 == 9004 :
 World1 ( )
elif O00O0 == 9005 :
 World2 ( IIo0o0O0O00oOOo )
elif O00O0 == 9006 :
 World3 ( IIo0o0O0O00oOOo )
elif O00O0 == 9007 :
 o0OOO0Oo ( )
elif O00O0 == 9008 :
 O0O00oo ( IIo0o0O0O00oOOo )
elif O00O0 == 9009 :
 iiIIIii ( IIo0o0O0O00oOOo )
elif O00O0 == 9010 :
 i1111iII1 ( )
elif O00O0 == 9011 :
 I1I1iiI11I1 ( IIo0o0O0O00oOOo )
elif O00O0 == 50 :
 ooooooo0oOo0 ( IIo0o0O0O00oOOo )
elif O00O0 == 9020 :
 champlist ( )
elif O00O0 == 9021 :
 Oo000O ( )
elif O00O0 == 9022 :
 I1iOO000Ooo ( )
elif O00O0 == 9023 :
 OoOooo0ooo0O ( )
elif O00O0 == 9024 :
 III1iI1ii1 ( IIo0o0O0O00oOOo )
elif O00O0 == 9030 :
 OOoo00o0 ( IIo0o0O0O00oOOo )
elif O00O0 == 9031 :
 o0OO0iI1II1i1ii ( IIo0o0O0O00oOOo )
elif O00O0 == 9032 :
 OOooOOooo000OoO ( IIo0o0O0O00oOOo )
elif O00O0 == 9033 :
 O0OOo ( IIo0o0O0O00oOOo )
elif O00O0 == 9034 :
 IIIii1iiIi ( )
elif O00O0 == 7084 :
 I11ooOo ( )
elif O00O0 == 7085 :
 IiiiIII1 ( IIo0o0O0O00oOOo )
elif O00O0 == 7086 :
 IIiIiOOoO ( IIo0o0O0O00oOOo , i1i1II1i11 , II1 )
elif O00O0 == 7087 :
 o0OoooO0oo0 ( II1 )
elif O00O0 == 9666 :
 o0OoOO ( IIo0o0O0O00oOOo )
elif O00O0 == 10100 : IIIiIIIi11I ( )
elif O00O0 == 101001 : I1i1i1iiIi1 ( IIo0o0O0O00oOOo )
elif O00O0 == 10105 : I1iii1IIi1I ( IIo0o0O0O00oOOo )
elif O00O0 == 10106 : oO00O00OOOo ( IIo0o0O0O00oOOo )
elif O00O0 == 10104 : i1ii1iIiI1 ( IIo0o0O0O00oOOo )
elif O00O0 == 10107 : OoOoo0ooO0000 ( )
elif O00O0 == 10103 : Oo0o0oO00 ( IIo0o0O0O00oOOo )
elif O00O0 == 10108 : I111 ( IIo0o0O0O00oOOo )
elif O00O0 == 10000 : Origin_Menu ( )
elif O00O0 == 10001 : iii11i1 ( )
elif O00O0 == 10002 : i1111IIiii1 ( )
elif O00O0 == 10003 : iIOO000O ( )
elif O00O0 == 10004 : i1I1IiIiIII ( IIo0o0O0O00oOOo )
elif O00O0 == 10005 : I11i1iiiiIIIi ( )
elif O00O0 == 10006 : IIiI11i111i ( IIo0o0O0O00oOOo )
elif O00O0 == 10007 : IiIiIi ( IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 10008 : O0O0o ( )
elif O00O0 == 10009 : II1iiiiII ( )
elif O00O0 == 10010 : ooOO0o0ooOo0 ( IIo0o0O0O00oOOo )
elif O00O0 == 10011 : oOO0o0 ( IIo0o0O0O00oOOo )
elif O00O0 == 10012 : OOIi1iI111II1I1 ( IIo0o0O0O00oOOo )
elif O00O0 == 10113 : GRABG ( IIo0o0O0O00oOOo , O000OOO )
elif O00O0 == 10109 : I1111 ( IIo0o0O0O00oOOo )
elif O00O0 == 10013 : Ooooo0OO ( IIo0o0O0O00oOOo )
elif O00O0 == 10014 : IIIiIII1 ( )
elif O00O0 == 10015 : o0o0Oo ( )
elif O00O0 == 10016 : iI1i1II ( IIo0o0O0O00oOOo )
elif O00O0 == 10017 : O0o0ooo00o0O ( )
elif O00O0 == 10018 : i1iii11 ( )
elif O00O0 == 10019 : I1IOOooO0o00OOo ( )
elif O00O0 == 10020 : iI11IIiII1iII ( )
elif O00O0 == 10021 : iI111iiI1II ( )
elif O00O0 == 10022 : O0iI1Iii1i1I ( IIo0o0O0O00oOOo )
elif O00O0 == 10023 : iii1iII1I1I ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 10024 : OO0O0000oo ( IIo0o0O0O00oOOo )
elif O00O0 == 10025 : iiOOOO0o ( )
elif O00O0 == 10026 : OoOo ( )
elif O00O0 == 10027 : Oo0oo ( )
elif O00O0 == 10028 : i1I1I ( )
elif O00O0 == 10029 : OO0OO0 ( )
elif O00O0 == 423 : ii111I111i ( IIo0o0O0O00oOOo )
elif O00O0 == 426 : OoOOOo0 ( IIo0o0O0O00oOOo )
elif O00O0 == 10030 : Izle_Films ( )
elif O00O0 == 10031 : Latest_Izle_Movies ( )
elif O00O0 == 10032 : Izle_Genres ( )
elif O00O0 == 10033 : Izle_Pop_Movies ( )
elif O00O0 == 10034 : Izle_Boxsets ( )
elif O00O0 == 10035 : Izle_Search ( )
elif O00O0 == 10036 : Izle_Genres_Movie ( IIo0o0O0O00oOOo )
elif O00O0 == 10037 : Izle_Boxset_single ( IIo0o0O0O00oOOo )
elif O00O0 == 10038 : Izle_IFRAME ( )
elif O00O0 == 10039 : Izle_Boxsets_Next ( IIo0o0O0O00oOOo )
elif O00O0 == 10040 : o0oo0oo0 ( )
elif O00O0 == 10041 : iIiiIi11 ( IIo0o0O0O00oOOo )
elif O00O0 == 10042 : IiIiiiIii1i ( IIo0o0O0O00oOOo )
elif O00O0 == 10043 : iI111II ( )
elif O00O0 == 10044 : oOoOo ( IIo0o0O0O00oOOo )
elif O00O0 == 10045 : ooOiiIII ( O000OOO )
elif O00O0 == 10046 : Ooo00O ( IIo0o0O0O00oOOo )
elif O00O0 == 10047 : i1i11IiII ( IIo0o0O0O00oOOo )
elif O00O0 == 10048 : I1i1ii1IiI1i ( IIo0o0O0O00oOOo )
elif O00O0 == 10049 : I11i1i ( IIo0o0O0O00oOOo )
elif O00O0 == 10050 : IIiiI1iiI ( )
elif O00O0 == 10051 : OoO0o ( )
elif O00O0 == 10052 : OOoO0ooo ( )
elif O00O0 == 10053 : Addon ( IIo0o0O0O00oOOo )
elif O00O0 == 10054 : II11IIiii ( IIo0o0O0O00oOOo , O000OOO )
elif O00O0 == 10055 :
 OO000o0O0o ( "addFavorite" )
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiIi1i ( O000OOO , IIo0o0O0O00oOOo , i1i1II1i11 , iI1iIii11Ii , iiIiOo0oO0 )
elif O00O0 == 10056 :
 OO000o0O0o ( "rmFavorite" )
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 iI11iOoo ( O000OOO )
elif O00O0 == 10057 :
 OO000o0O0o ( "getFavorites" )
 OOoo00OoO0o ( )
elif O00O0 == 10058 : ii1iI11 ( )
elif O00O0 == 10059 : Donators_Guide ( )
elif O00O0 == 10060 : o0OO0 ( )
elif O00O0 == 10061 : IIi1i ( )
elif O00O0 == 10062 : iiIII1i1 ( O000OOO , IIo0o0O0O00oOOo , II1 )
elif O00O0 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + I11iii1Ii + ")" )
elif O00O0 == 10064 : OooOo ( )
elif O00O0 == 10065 : ooO ( IIo0o0O0O00oOOo )
elif O00O0 == 10066 : iiiiii1Ii ( IIo0o0O0O00oOOo )
elif O00O0 == 10068 : OO0OO0OO ( IIo0o0O0O00oOOo )
elif O00O0 == 10069 : IIIii11 ( IIo0o0O0O00oOOo )
elif O00O0 == 10070 : iiIIIi1iIi ( IIo0o0O0O00oOOo )
elif O00O0 == 10071 : Genie_Watch ( )
elif O00O0 == 10072 : OO0o0o0oo ( )
elif O00O0 == 10073 : IiiiIIi ( IIo0o0O0O00oOOo )
elif O00O0 == 10074 : Ooo0 ( IIo0o0O0O00oOOo )
elif O00O0 == 10075 : IIi1i1I11IIII ( i1i1II1i11 , O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 10076 : OOii11Ii1IiiI1 ( IIo0o0O0O00oOOo )
elif O00O0 == 10077 : III ( IIo0o0O0O00oOOo )
elif O00O0 == 10078 : iI1Ii11 ( )
elif O00O0 == 10079 : Genie_Watch_Tv_Shows ( )
elif O00O0 == 10080 : Genie_Watch_Tv_Genre ( IIo0o0O0O00oOOo )
elif O00O0 == 10081 : Genie_Watch_TV_PlayRun ( IIo0o0O0O00oOOo )
elif O00O0 == 10082 : Genie_Watch_TV_Episodes ( IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 10083 : Genie_Watch_Tv_Recent ( IIo0o0O0O00oOOo )
elif O00O0 == 10084 : IiIIi1I1I11Ii ( )
elif O00O0 == 10085 : Iii1I1I11iiI1 ( )
elif O00O0 == 10086 : o0OOOO00O0Oo ( )
elif O00O0 == 20000 : O0OoO0OOo ( )
elif O00O0 == 20001 : O0oo0OoO0oo ( IIo0o0O0O00oOOo )
elif O00O0 == 20002 : Iii1IiIiIii ( IIo0o0O0O00oOOo )
elif O00O0 == 20003 : I1IIiiiIi1ii11I ( IIo0o0O0O00oOOo )
elif O00O0 == 20004 : o0O00o00Ooo ( IIo0o0O0O00oOOo )
elif O00O0 == 20005 : ooOoOoOoo ( IIo0o0O0O00oOOo )
elif O00O0 == 21004 : Iii1I11i1IiiI ( )
elif O00O0 == 21005 : OOoo ( IIo0o0O0O00oOOo )
elif O00O0 == 21006 : OO000oOoOo000 ( IIo0o0O0O00oOOo )
elif O00O0 == 21007 : iiooo ( IIo0o0O0O00oOOo )
elif O00O0 == 21008 : O00oOOooo ( IIo0o0O0O00oOOo )
elif O00O0 == 21009 : iI1i1i11I1iI ( IIo0o0O0O00oOOo )
elif O00O0 == 30000 : IiIii1i ( )
elif O00O0 == 30001 : I1i1iI1I1II ( )
elif O00O0 == 100121 : Resolve ( IIo0o0O0O00oOOo )
elif O00O0 == 30003 : oOoOo000Ooooo ( )
elif O00O0 == 30004 : iIiIi1i1ii11 ( IIo0o0O0O00oOOo )
elif O00O0 == 30005 : Ooooo0o0 ( IIo0o0O0O00oOOo )
elif O00O0 == 30006 : iii1II11II1 ( )
elif O00O0 == 30007 : i1oOOOoOO ( )
elif O00O0 == 30008 : o0oO ( IIo0o0O0O00oOOo )
elif O00O0 == 30009 : O0OoO0 ( IIo0o0O0O00oOOo )
elif O00O0 == 30010 : iIiIii ( IIo0o0O0O00oOOo )
elif O00O0 == 30011 : III11IiI ( )
elif O00O0 == 30012 : Iii1iI1I1iii1 ( )
elif O00O0 == 30013 : oo000O ( )
elif O00O0 == 30014 : iIi1i111ii1II11ii ( )
elif O00O0 == 30015 : iiiiII ( IIo0o0O0O00oOOo , i1i1II1i11 , iI1iIii11Ii )
elif O00O0 == 30016 : i1Ii1I ( IIo0o0O0O00oOOo )
elif O00O0 == 30019 : o00o0o0o ( IIo0o0O0O00oOOo )
elif O00O0 == 30017 : i1IiIiiiii11 ( IIo0o0O0O00oOOo )
elif O00O0 == 30018 : IiIiI11IIII ( IIo0o0O0O00oOOo )
elif O00O0 == 30030 : Oo00OO00Ooo ( )
elif O00O0 == 30031 : IiII111I ( )
elif O00O0 == 30032 : OOOoO ( )
elif O00O0 == 30033 : II1O0o00 ( )
elif O00O0 == 30034 : OOO00O0000 ( )
elif O00O0 == 30035 : iiII11ii1Ii ( IIo0o0O0O00oOOo )
elif O00O0 == 30036 : iiI1Ii1iiii1i ( IIo0o0O0O00oOOo )
elif O00O0 == 30037 : III1iIi ( IIo0o0O0O00oOOo )
elif O00O0 == 30038 : iII11IiIIII ( )
elif O00O0 == 30039 : OoOo00o0O00 ( )
elif O00O0 == 50000 : oOoO00o ( )
elif O00O0 == 50001 : o0oOOO0 ( )
elif O00O0 == 50002 : i1I11iIIiIIiIi ( IIo0o0O0O00oOOo )
elif O00O0 == 50003 : Table_Menu ( II1 )
elif O00O0 == 60000 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
elif O00O0 == 60001 : OoO0oOOOO ( )
elif O00O0 == 60002 : OOoOo0oO0oo00 ( O000OOO )
elif O00O0 == 60003 : IIIIi1Iii1iIi ( IIo0o0O0O00oOOo )
elif O00O0 == 600033 : o0OOOoO0O ( IIo0o0O0O00oOOo )
elif O00O0 == 60004 : I1i1ii1ii ( IIo0o0O0O00oOOo )
elif O00O0 == 50004 : O0oooo00o0Oo ( )
elif O00O0 == 50005 : speedtest . runtest ( IIo0o0O0O00oOOo )
elif O00O0 == 70001 : Oo0O0oOoO0o0 ( )
elif O00O0 == 70002 : ooOo0oo0O0O ( IIo0o0O0O00oOOo )
elif O00O0 == 70003 : IIiii ( IIo0o0O0O00oOOo )
elif O00O0 == 70004 : i1Ii11I1i ( IIo0o0O0O00oOOo )
elif O00O0 == 70005 : iI11IIi1iiI1I ( IIo0o0O0O00oOOo )
elif O00O0 == 70006 : oO0oO0ooOoO0 ( )
elif O00O0 == 50006 : O0O0OOOOoo ( oo00 , Oo0oO0ooo )
elif O00O0 == 80000 : oo000oiIIIII ( )
elif O00O0 == 80001 : resolvefilmon ( IIo0o0O0O00oOOo )
elif O00O0 == 80002 : I1111ii11 ( )
elif O00O0 == 80003 : OOo0OO ( O000OOO , IIo0o0O0O00oOOo , "None" )
elif O00O0 == 80004 : IIiIiii ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 80005 : i1I11iIiII ( )
elif O00O0 == 80006 : o0Ii11iIiiI ( IIo0o0O0O00oOOo )
elif O00O0 == 80007 : o000 ( IIo0o0O0O00oOOo )
elif O00O0 == 80008 : i11ii1 ( )
elif O00O0 == 80009 : oOoOo0OOOOOO ( )
elif O00O0 == 80010 : I1IIiIiOoOO0OOo0Oo ( IIo0o0O0O00oOOo )
elif O00O0 == 80011 : i1IiIii1i ( IIo0o0O0O00oOOo )
elif O00O0 == 80012 : IIIIi1i ( )
elif O00O0 == 90000 : I1iiii11IiI1 ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 90001 : tools ( )
elif O00O0 == 90002 : oOOoo0 ( )
elif O00O0 == 90003 : II1IIi1ii111 ( IIo0o0O0O00oOOo )
elif O00O0 == 90004 : II1OO ( IIo0o0O0O00oOOo )
elif O00O0 == 90005 : oo0OOO0O0 ( IIo0o0O0O00oOOo )
elif O00O0 == 90006 : OoO0I1I ( IIo0o0O0O00oOOo )
elif O00O0 == 90007 : oo000oooooooO ( IIo0o0O0O00oOOo )
elif O00O0 == 90008 : IIIII11IIi ( IIo0o0O0O00oOOo )
elif O00O0 == 90009 : i1i11 ( IIo0o0O0O00oOOo )
elif O00O0 == 90010 : iIi1i1iIi1iI ( )
elif O00O0 == 90020 : OOOooooOo0 ( )
elif O00O0 == 90021 : hellyeah2 ( IIo0o0O0O00oOOo )
elif O00O0 == 90022 : hellyeah3 ( IIo0o0O0O00oOOo )
elif O00O0 == 90023 : Ii1Ii1I ( )
elif O00O0 == 90024 : i1I ( IIo0o0O0O00oOOo )
elif O00O0 == 90025 : OooOoOO0OO ( IIo0o0O0O00oOOo )
if 86 - 86: O0Oooo0O / o0o00Oo0O + ii % OOOo00oo0oO
elif O00O0 == 90026 : Ooooo00 ( )
elif O00O0 == 90027 : ooOoOoo000O0O ( O000OOO , IIo0o0O0O00oOOo , II1 )
elif O00O0 == 90028 : OoOo0O00 ( IIo0o0O0O00oOOo )
if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . i1IiiiI1iI . i1iIi
elif O00O0 == 900300 : iII1iiiiIII ( )
elif O00O0 == 900301 : Ii11i1I11i ( IIo0o0O0O00oOOo )
elif O00O0 == 900302 : i1i1iII1 ( IIo0o0O0O00oOOo )
elif O00O0 == 90030 : Iio00 ( )
elif O00O0 == 90031 : Treplays ( )
elif O00O0 == 90032 : Treplays2 ( IIo0o0O0O00oOOo )
elif O00O0 == 90033 : Treplays3 ( IIo0o0O0O00oOOo )
elif O00O0 == 90034 : Treplays4 ( IIo0o0O0O00oOOo )
elif O00O0 == 90035 : oo00O00oO000o ( IIo0o0O0O00oOOo )
elif O00O0 == 90036 : IIii1iI11 ( IIo0o0O0O00oOOo )
elif O00O0 == 90039 : I111I1IiI1i1 ( IIo0o0O0O00oOOo )
elif O00O0 == 90037 : Ooii1IIi1ii ( IIo0o0O0O00oOOo )
elif O00O0 == 900377 : iiiii11I1 ( IIo0o0O0O00oOOo )
elif O00O0 == 90038 : i1I1iIoOOoO ( )
if 81 - 81: IIiIiII11i + iii1i1iiiiIi % Ii / iiiiiiii1 . O0Oooo0O + IIiIiII11i
elif O00O0 == 10090 : oOIII111iiIi1 ( )
elif O00O0 == 10091 : o00ooO0 ( IIo0o0O0O00oOOo )
elif O00O0 == 10092 : o0o0OoOo0 ( IIo0o0O0O00oOOo )
elif O00O0 == 10093 : OO0OOo00Oo ( IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 10094 : o000oOoOOO ( IIo0o0O0O00oOOo , i1i1II1i11 )
if 48 - 48: oOo0O0Ooo . oOoO0o00OO0 * iii1i1iiiiIi % ooOoO0O00 / O0Oooo0O * IIiIiII11i
elif O00O0 == 10095 : Ii11Ii ( )
elif O00O0 == 10096 : oOooOOo00ooO ( IIo0o0O0O00oOOo )
elif O00O0 == 10097 : oO0o0oOo ( IIo0o0O0O00oOOo )
elif O00O0 == 10098 : iIIi1 ( IIo0o0O0O00oOOo )
elif O00O0 == 10099 : oOoOo0o00o ( IIo0o0O0O00oOOo )
if 62 - 62: ooo0O * O0Oooo0O . iI11I1II1I1I / ooOoO0O00
elif O00O0 == 10200 : iiIii1I ( )
elif O00O0 == 10201 : OO0Oo ( O000OOO , IIo0o0O0O00oOOo , II1 )
elif O00O0 == 10202 : OOo00ooOoO0o ( IIo0o0O0O00oOOo )
elif O00O0 == 10203 : RT4 ( IIo0o0O0O00oOOo )
if 75 - 75: ii / oOOoOooOo - iiiiiiii1 . ii . iii1i1iiiiIi % ooOoO0O00
elif O00O0 == 90040 : oO0oo ( )
elif O00O0 == 90041 : o0000O00oO0O ( IIo0o0O0O00oOOo )
elif O00O0 == 90042 : I1i1I1Iiiii1 ( IIo0o0O0O00oOOo )
elif O00O0 == 90043 : i11Ii1IiIIIi ( IIo0o0O0O00oOOo )
elif O00O0 == 90044 : o0OoooO ( IIo0o0O0O00oOOo )
elif O00O0 == 90045 : ii11i1I1i ( )
elif O00O0 == 90046 : ooOO0 ( IIo0o0O0O00oOOo )
elif O00O0 == 90050 : ooIi111iII ( )
elif O00O0 == 90051 : I11II11111i11 ( IIo0o0O0O00oOOo )
elif O00O0 == 90052 : i1Ii ( IIo0o0O0O00oOOo )
elif O00O0 == 90053 : ooOoOo ( IIo0o0O0O00oOOo )
elif O00O0 == 90054 : iiI1iIII1ii ( IIo0o0O0O00oOOo )
elif O00O0 == 90055 : OooooO ( )
if 7 - 7: iii1i1iiiiIi . ooOoO0O00 * Ii % Ii
elif O00O0 == 100001 : Stand_up ( )
if 54 - 54: oOo / oOo0O0Ooo . I1ii11iIi11i
elif O00O0 == 100003 : iI1i1II ( IIo0o0O0O00oOOo )
elif O00O0 == 100004 : oOOOOOOOoO ( IIo0o0O0O00oOOo )
elif O00O0 == 100005 : Resolve ( IIo0o0O0O00oOOo )
elif O00O0 == 100008 : Search ( )
elif O00O0 == 100007 : OO0oOOo0o ( IIo0o0O0O00oOOo )
elif O00O0 == 100009 : yt . PlayVideo ( IIo0o0O0O00oOOo )
elif O00O0 == 100010 : I1ii1111Ii ( IIo0o0O0O00oOOo )
elif O00O0 == 100100 : i1iii1ii ( i1i1II1i11 , IIo0o0O0O00oOOo , iiIiiIi1 )
elif O00O0 == 100101 : I1i1I1I11IiiI ( IIo0o0O0O00oOOo , O000OOO , iI1iIii11Ii , iiIiiIi1 , i1i1II1i11 )
elif O00O0 == 100102 : o00ooo0 ( O000OOO , IIo0o0O0O00oOOo , i1i1II1i11 , iI1iIii11Ii )
elif O00O0 == 100106 : o00ooOoO0 ( IIo0o0O0O00oOOo , O000OOO )
elif O00O0 == 100107 : oo0ooO0O0o ( )
elif O00O0 == 100108 : o0OOOo ( )
elif O00O0 == 100109 : ii1ii1iii1I ( IIo0o0O0O00oOOo )
elif O00O0 == 40000 : i1I1ii1 ( )
elif O00O0 == 40001 : iII1ii1IIII ( IIo0o0O0O00oOOo )
elif O00O0 == 100110 : o00OOo0o0O ( IIo0o0O0O00oOOo )
elif O00O0 == 100111 : II11IiIIiiI ( IIo0o0O0O00oOOo )
elif O00O0 == 100112 : O0o0O00o0o ( IIo0o0O0O00oOOo )
elif O00O0 == 100113 : Iii1 ( IIo0o0O0O00oOOo )
elif O00O0 == 100114 : I111Iii1 ( IIo0o0O0O00oOOo )
elif O00O0 == 100115 : ooOO0OOO00o ( IIo0o0O0O00oOOo )
elif O00O0 == 100117 : i11i ( IIo0o0O0O00oOOo )
elif O00O0 == 100118 : OOO0O0OOo ( IIo0o0O0O00oOOo )
elif O00O0 == 100120 : OoOoO0ooooO0 ( IIo0o0O0O00oOOo )
elif O00O0 == 1001200 : IIII1ii1 ( IIo0o0O0O00oOOo )
elif O00O0 == 100210 : OoO0o0000O ( IIo0o0O0O00oOOo )
elif O00O0 == 100211 : o0oOo ( )
elif O00O0 == 100212 : Oo00oo ( )
elif O00O0 == 100213 : i1II1i ( )
elif O00O0 == 100214 : oo0o ( )
elif O00O0 == 1000111 :
 o00o0o0O0 ( IIo0o0O0O00oOOo )
 if 39 - 39: oOo . oOOoOooOo
elif O00O0 == 1001111 :
 OoO00o0 ( O000OOO , IIo0o0O0O00oOOo )
 if 41 - 41: I1ii11iIi11i * oOoO0o00OO0 - IIiIiII11i - IIiIiII11i
elif O00O0 == 1002111 :
 Ii1IiiI ( )
 if 7 - 7: OOOo00oo0oO
elif O00O0 == 1003111 :
 oOoOOO0O0O ( IIo0o0O0O00oOOo , O000OOO )
 if 41 - 41: oOOoOooOo
elif O00O0 == 1004111 :
 iII11i1 ( )
 if 93 - 93: i1iIi + O0Oooo0O + i1iIi
elif O00O0 == 1005111 :
 i11IIiIi ( IIo0o0O0O00oOOo , O000OOO )
elif O00O0 == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( IIo0o0O0O00oOOo , iI1iIii11Ii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( O000OOO , IIo0o0O0O00oOOo , iI1iIii11Ii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( O000OOO , IIo0o0O0O00oOOo , iI1iIii11Ii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1105000 :
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( O000OOO , IIo0o0O0O00oOOo , i1i1II1i11 , iI1iIii11Ii , iiIiOo0oO0 )
elif O00O0 == 1106000 :
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( O000OOO )
elif O00O0 == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( IIo0o0O0O00oOOo )
elif O00O0 == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( O000OOO )
elif O00O0 == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif O00O0 == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( IIo0o0O0O00oOOo )
elif O00O0 == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in IIo0o0O0O00oOOo :
  import urlresolver
  i1i1IIii1i1 = urlresolver . resolve ( IIo0o0O0O00oOOo )
  Ii1II1I11i1 = xbmcgui . ListItem ( path = i1i1IIii1i1 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1II1I11i1 )
 elif not IIo0o0O0O00oOOo . startswith ( "plugin://plugin" ) or not any ( x in IIo0o0O0O00oOOo for x in pyramid . g_ignoreSetResolved ) :
  Ii1II1I11i1 = xbmcgui . ListItem ( path = IIo0o0O0O00oOOo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1II1I11i1 )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + IIo0o0O0O00oOOo + ')' )
elif O00O0 == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( O000OOO , playlist )
elif O00O0 == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( IIo0o0O0O00oOOo , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1117000 :
 IIo0o0O0O00oOOo , iiii1iIi = getRegexParsed ( regexs , IIo0o0O0O00oOOo )
 if IIo0o0O0O00oOOo :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( IIo0o0O0O00oOOo , O000OOO , i1i1II1i11 , iiii1iIi )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif O00O0 == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 o000oo0o = youtubedl . single_YD ( IIo0o0O0O00oOOo )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( o000oo0o , O000OOO , i1i1II1i11 )
elif O00O0 == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( IIo0o0O0O00oOOo ) , O000OOO , i1i1II1i11 , True )
elif O00O0 == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , O000OOO , 'video' )
elif O00O0 == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( IIo0o0O0O00oOOo , O000OOO , 'video' )
elif O00O0 == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( IIo0o0O0O00oOOo , O000OOO , 'audio' )
elif O00O0 == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1126000 :
 O000OOO = O000OOO . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( IIo0o0O0O00oOOo , search_term = O000OOO [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( IIo0o0O0O00oOOo )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif O00O0 == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif O00O0 == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif O00O0 == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( O000OOO , IIo0o0O0O00oOOo , i1i1II1i11 , iI1iIii11Ii )
elif O00O0 == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( IIo0o0O0O00oOOo , i1i1II1i11 , iI1iIii11Ii ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( O000OOO , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( IIo0o0O0O00oOOo )
elif O00O0 == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O00O0 == 9050000 : oOo0OOoooO ( )
elif O00O0 == 9060000 : OoO00o0 ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 9080000 : ooOoOO ( )
elif O00O0 == 9070000 : O0oo ( )
elif O00O0 == 9090000 : iiIIi ( )
elif O00O0 == 9100000 : iI11Ii111 ( )
elif O00O0 == 9110000 : iIii11iI1II ( )
elif O00O0 == 9110001 : ooO000O ( IIo0o0O0O00oOOo )
elif O00O0 == 9110002 : oOOoOoo0O0 ( IIo0o0O0O00oOOo , O000OOO , i1i1II1i11 )
elif O00O0 == 9110003 : IiIiiI11i1Ii ( O000OOO , iiIiiIi1 )
elif O00O0 == 9110005 : OOO0O00Oo ( II1 , IIo0o0O0O00oOOo )
elif O00O0 == 9110004 : Ii1II11II1iii ( )
elif O00O0 == 9110010 : ii1IiIiI1iiii ( IIo0o0O0O00oOOo )
elif O00O0 == 9110011 : oO0OooO00Oo ( )
elif O00O0 == 9110012 : i1iIIi ( IIo0o0O0O00oOOo , O000OOO )
elif O00O0 == 9110013 : IIiIiiiIIIIi1 ( IIo0o0O0O00oOOo )
elif O00O0 == 9110014 : ii1IiIi11 ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 9110015 : ii1ii ( )
elif O00O0 == 9999999 : I1iI11IiiI11i ( )
elif O00O0 == 19999999 : o0OOO00ooo ( )
elif O00O0 == 1999990 : ooo ( )
elif O00O0 == 21999990 : I1III1111iIi ( )
elif O00O0 == 21999991 : I1i111I ( IIo0o0O0O00oOOo )
elif O00O0 == 21999992 : OooOo0oo0O0o00O ( IIo0o0O0O00oOOo )
elif O00O0 == 21999993 : I1i11 ( IIo0o0O0O00oOOo )
elif O00O0 == 21999994 : IiIi1I1 ( IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 21999995 : IiIIi1 ( IIo0o0O0O00oOOo )
elif O00O0 == 21999996 : II1i11I ( IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 21999997 : O0o0oO ( IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 21999998 : IIIIiIiIi1 ( O000OOO , IIo0o0O0O00oOOo , i1i1II1i11 )
elif O00O0 == 219999989 : OOI1iI1ii1II ( )
elif O00O0 == 219999990 : I1i1iiiI1 ( all = True )
elif O00O0 == 219999991 : OO0Oo00 ( )
elif O00O0 == 219999992 : ooOo0Ooo0 ( )
elif O00O0 == 300000000 : IiI ( )
elif O00O0 == 300000001 : OoO ( IIo0o0O0O00oOOo )
elif O00O0 == 300000002 : OO0O0 ( IIo0o0O0O00oOOo )
elif O00O0 == 300000003 : I1i1i1iii ( O000OOO , IIo0o0O0O00oOOo )
elif O00O0 == 300000004 : o0o ( IIo0o0O0O00oOOo )
elif O00O0 == 300000005 : oOoO00O0 ( IIo0o0O0O00oOOo )
elif O00O0 == 300000006 : i11I ( O000OOO , IIo0o0O0O00oOOo )
if 30 - 30: oOo0O0Ooo % oOo - ooOoO0O00 / oOo0O0Ooo - oOo - i1IiiiI1iI
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
