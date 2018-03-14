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
I1IiI = "3.6.9"
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
  OoOoO ( 'Change Log 14/03/2018 - v3.6.9' , '[COLORsteelblue]Free Live Tv Section Added,[CR][COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
  os . makedirs ( ooooooO0oo )
def Ii1I1i ( ) :
 OoOoO ( 'Change Log 14/03/2018 - v3.6.9' , '[COLORsteelblue]Free Live Tv Section Added,[CR][COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
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
   o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '[/COLOR]' , url , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' )
  elif 'Kodi' in O000OOO :
   pass
  elif 'Filter' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' , url , 300000004 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , '[COLORsteelblue]' + O000OOO + '' + '[COLORorangered] (By Country)[/COLOR]' )
   if 30 - 30: OoOo0o + oOoO0o00OO0 * i1IiiiI1iI % Ii % iii1i1iiiiIi
def OO0OoOO0o0o ( name , url ) :
 ooI1111i = name
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 iIIii = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 o00O0O = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 ii1iii1i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( oOOo0 )
 Iii1I1111ii = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 ooOoO00 = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for name , Ii1IIiI1i , o0O00Oo0 , iIIIiIi , url in iI111i :
  if ooI1111i in o0O00Oo0 :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( name + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , Ii1IIiI1i , Ii1IIiI1i , ( '[COLORsteelblue]' + ( name + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for Ii1IIiI1i , o0O00Oo0 , iIIIiIi , url in IIi11i1i1iI1 :
  if ooI1111i in o0O00Oo0 :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , Ii1IIiI1i , Ii1IIiI1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0O00Oo0 , iIIIiIi , url in iIIii :
  if ooI1111i in o0O00Oo0 :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0O00Oo0 , Ii1IIiI1i , iIIIiIi , url in o00O0O :
  if ooI1111i in o0O00Oo0 :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , Ii1IIiI1i , Ii1IIiI1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iIIIiIi , url in ii1iii1i :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0O00Oo0 , iIIIiIi , url in Iii1I1111ii :
  if ooI1111i in o0O00Oo0 :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iIIIiIi , url in ooOoO00 :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 33 - 33: o0o00Oo0O * ooo0O - O0Oooo0O % O0Oooo0O
def I11I ( url ) :
 url = url
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + '](_) _No Group[/COLOR]' , '[COLOR' + iiI1IiI + '](UK) United Kingdom[/COLOR]' , '[COLOR' + iiI1IiI + '](US) United States[/COLOR]' , '[COLOR' + iiI1IiI + '](AL) Albania[/COLOR]' , '[COLOR' + iiI1IiI + '](AS) American Samoa[/COLOR]' , '[COLOR' + iiI1IiI + '](AR) Argentina[/COLOR]' , '[COLOR' + iiI1IiI + '](AU) Australia[/COLOR]' , '[COLOR' + iiI1IiI + '](AZ) Azerbaijan[/COLOR]' , '[COLOR' + iiI1IiI + '](BY) Belarus[/COLOR]' , '[COLOR' + iiI1IiI + '](BE) Belgium[/COLOR]' , '[COLOR' + iiI1IiI + '](BO) Bolivia[/COLOR]' , '[COLOR' + iiI1IiI + '](BR) Brazil[/COLOR]' , '[COLOR' + iiI1IiI + '](CM) Cameroon[/COLOR]' , '[COLOR' + iiI1IiI + '](CA) Canada[/COLOR]' , '[COLOR' + iiI1IiI + '](CO) Colombia[/COLOR]' , '[COLOR' + iiI1IiI + '](CZ) Czech Republic[/COLOR]' , '[COLOR' + iiI1IiI + '](DO) Dominican Republic[/COLOR]' , '[COLOR' + iiI1IiI + '](EC) Ecuador[/COLOR]' , '[COLOR' + iiI1IiI + '](FO) Faroe Islands[/COLOR]' , '[COLOR' + iiI1IiI + '](FR) France[/COLOR]' , '[COLOR' + iiI1IiI + '](DE) Germany[/COLOR]' , '[COLOR' + iiI1IiI + '](GR) Greece[/COLOR]' , '[COLOR' + iiI1IiI + '](IS) Iceland[/COLOR]' , '[COLOR' + iiI1IiI + '](IN) India[/COLOR]' , '[COLOR' + iiI1IiI + '](ID) Indonesia[/COLOR]' , '[COLOR' + iiI1IiI + '](IR) Iran[/COLOR]' , '[COLOR' + iiI1IiI + '](IT) Italy[/COLOR]' , '[COLOR' + iiI1IiI + '](LA) Laos[/COLOR]' , '[COLOR' + iiI1IiI + '](MO) Macau[/COLOR]' , '[COLOR' + iiI1IiI + '](MX) Mexico[/COLOR]' , '[COLOR' + iiI1IiI + '](NL) Netherlands[/COLOR]' , '[COLOR' + iiI1IiI + '](NE) Niger[/COLOR]' , '[COLOR' + iiI1IiI + '](PK) Pakistan[/COLOR]' , '[COLOR' + iiI1IiI + '](PA) Panama[/COLOR]' , '[COLOR' + iiI1IiI + '](PE) Peru[/COLOR]' , '[COLOR' + iiI1IiI + '](PL) Poland[/COLOR]' , '[COLOR' + iiI1IiI + '](PT) Portugal[/COLOR]' , '[COLOR' + iiI1IiI + '](RO) Romania[/COLOR]' , '[COLOR' + iiI1IiI + '](RU) Russia[/COLOR]' , '[COLOR' + iiI1IiI + '](SL) Sierra Leone[/COLOR]' , '[COLOR' + iiI1IiI + '](EX-YU) Slovenia[/COLOR]' , '[COLOR' + iiI1IiI + '](SO) Somalia[/COLOR]' , '[COLOR' + iiI1IiI + '](SP) Spain[/COLOR]' , '[COLOR' + iiI1IiI + '](SE) Sweden[/COLOR]' , '[COLOR' + iiI1IiI + '](CH) Switzerland[/COLOR]' , '[COLOR' + iiI1IiI + '](TH) Thailand[/COLOR]' , '[COLOR' + iiI1IiI + '](TR) Turkey[/COLOR]' , '[COLOR' + iiI1IiI + '](UA) Ukraine[/COLOR]' , '[COLOR' + iiI1IiI + '](VE) Venezuela[/COLOR]' , '[COLOR' + iiI1IiI + '](WW) World Wide[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Select Country[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  O000OOO = '(_)'
 if iiI == 1 :
  O000OOO = '(UK)'
 if iiI == 2 :
  O000OOO = '(US)'
 if iiI == 3 :
  O000OOO = '(AL)'
 if iiI == 4 :
  O000OOO = '(AS)'
 if iiI == 5 :
  O000OOO = '(AR)'
 if iiI == 6 :
  O000OOO = '(AU)'
 if iiI == 7 :
  O000OOO = '(AZ)'
 if iiI == 8 :
  O000OOO = '(BY)'
 if iiI == 9 :
  O000OOO = '(BE)'
 if iiI == 10 :
  O000OOO = '(BO)'
 if iiI == 11 :
  O000OOO = '(BR)'
 if iiI == 12 :
  O000OOO = '(CM)'
 if iiI == 13 :
  O000OOO = '(CA)'
 if iiI == 14 :
  O000OOO = '(CO)'
 if iiI == 15 :
  O000OOO = '(CZ)'
 if iiI == 16 :
  O000OOO = '(DO)'
 if iiI == 17 :
  O000OOO = '(EC)'
 if iiI == 18 :
  O000OOO = '(FO)'
 if iiI == 19 :
  O000OOO = '(FR)'
 if iiI == 20 :
  O000OOO = '(DE)'
 if iiI == 21 :
  O000OOO = '(GR)'
 if iiI == 22 :
  O000OOO = '(IS)'
 if iiI == 23 :
  O000OOO = '(IN)'
 if iiI == 24 :
  O000OOO = '(ID)'
 if iiI == 25 :
  O000OOO = '(IR)'
 if iiI == 26 :
  O000OOO = '(IT)'
 if iiI == 27 :
  O000OOO = '(LA)'
 if iiI == 28 :
  O000OOO = '(MO)'
 if iiI == 29 :
  O000OOO = '(MX)'
 if iiI == 30 :
  O000OOO = '(NL)'
 if iiI == 31 :
  O000OOO = '(NE)'
 if iiI == 32 :
  O000OOO = '(PK)'
 if iiI == 33 :
  O000OOO = '(PA)'
 if iiI == 34 :
  O000OOO = '(PE)'
 if iiI == 35 :
  O000OOO = '(PL)'
 if iiI == 36 :
  O000OOO = '(PT)'
 if iiI == 37 :
  O000OOO = '(RO)'
 if iiI == 38 :
  O000OOO = '(RU)'
 if iiI == 39 :
  O000OOO = '(SL)'
 if iiI == 40 :
  O000OOO = '(EX-YU)'
 if iiI == 41 :
  O000OOO = '(SO)'
 if iiI == 42 :
  O000OOO = '(SP)'
 if iiI == 43 :
  O000OOO = '(SE)'
 if iiI == 44 :
  O000OOO = '(CH)'
 if iiI == 45 :
  O000OOO = '(TH)'
 if iiI == 46 :
  O000OOO = '(TR)'
 if iiI == 47 :
  O000OOO = '(UA)'
 if iiI == 48 :
  O000OOO = '(VE)'
 if iiI == 49 :
  O000OOO = '(WW)'
 OO0OoOO0o0o ( O000OOO , url )
 if 26 - 26: i1iIi % oOoO0o00OO0
def o00Oo0oooooo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 iIIii = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 o00O0O = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 ii1iii1i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( oOOo0 )
 Iii1I1111ii = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 ooOoO00 = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for O000OOO , Ii1IIiI1i , o0O00Oo0 , iIIIiIi , url in iI111i :
  if 'INFO' in o0O00Oo0 :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( O000OOO + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , Ii1IIiI1i , Ii1IIiI1i , ( '[COLORsteelblue]' + ( O000OOO + iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for Ii1IIiI1i , o0O00Oo0 , iIIIiIi , url in IIi11i1i1iI1 :
  if 'INFO' in o0O00Oo0 :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , Ii1IIiI1i , Ii1IIiI1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0O00Oo0 , iIIIiIi , url in iIIii :
  if 'INFO' in o0O00Oo0 :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0O00Oo0 , Ii1IIiI1i , iIIIiIi , url in o00O0O :
  if 'INFO' in o0O00Oo0 :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , Ii1IIiI1i , Ii1IIiI1i , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iIIIiIi , url in ii1iii1i :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0O00Oo0 , iIIIiIi , url in Iii1I1111ii :
  if 'INFO' in o0O00Oo0 :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0O00Oo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iIIIiIi , url in ooOoO00 :
  O0O0ooOOO ( ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , ( '[COLORsteelblue]' + ( iIIIiIi ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 76 - 76: i1IiiiI1iI / OoOo0o . o0o00Oo0O % oOo0O0Ooo . ooo0O + I11i1ii1
def o0o ( url ) :
 if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
  oo0 ( ( url ) . strip ( ) )
 else :
  try :
   oo0 ( ( url ) . strip ( ) )
  except :
   pass
  else :
   oo0 ( 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + url )
   if 61 - 61: iii1i1iiiiIi - OoOo0o - ooOoO0O00
   if 25 - 25: o0o00Oo0O * i1IiiiI1iI + oOoO0o00OO0 . ooo0O . ooo0O
def tools ( ) :
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']Change Log[/COLOR]' , '[COLOR' + iiI1IiI + ']Force Genie Update Kodi[/COLOR]' , '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  Ii1I1i ( )
 if iiI == 1 :
  Iii1I1I11iiI1 ( )
 if iiI == 2 :
  oOooO ( )
 if iiI == 3 :
  IIIIiI11I11 ( IIo0o0O0O00oOOo )
 if iiI == 4 :
  iI111I11I1I1 . ok ( oo00 , Oo0oO0ooo )
 if iiI == 5 :
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 if iiI == 6 :
  oo00o0 ( )
  if 4 - 4: i1iIi % OOOo00oo0oO * oOo
def o0O0OOOOoOO0 ( ) :
 o00oOOooOOo0o ( 'Stories' , 'http://etc.usf.edu/lit2go/books/' , 21999995 , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , '' )
 o00oOOooOOo0o ( 'Virtual FirePlaces' , 'http://www.virtual-fireplace.net/fireplaces.html' , 21999991 , 'http://www.virtual-fireplace.net/files/theme/burning-log.gif' , 'http://www.virtual-fireplace.net/files/theme/burning-log1.gif' , '' )
 o00oOOooOOo0o ( 'Nature Sounds' , 'http://www.virtual-fireplace.net/sounds.html' , 21999993 , 'http://www.virtual-fireplace.net/files/theme/sound.gif' , 'http://www.virtual-fireplace.net/files/theme/sound-bw.gif' , '' )
def iiO0oOo00o ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , O000OOO in IIIii1I :
  O0O0ooOOO ( O000OOO , url , 21999992 , 'http://www.virtual-fireplace.net/' + Ii1IIiI1i , 'http://www.virtual-fireplace.net/' + Ii1IIiI1i , O000OOO )
def o0ooooO0o0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( 'rel="canonical" href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for url in IIIii1I :
  url = ( url ) . replace ( '//www.youtube.com/embed/' , '' ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' )
  yt . PlayVideo ( url )
def iiIi11iI1iii ( url ) :
 o00oOOooOOo0o ( 'Rain And Thunder' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Water And Forests' , 'http://www.virtual-fireplace.net/water-and-forest.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Beach And Ocean' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , '' )
def oo000o0000oO ( url , iconimage ) :
 Ii1IIiI1i = iconimage
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in IIIii1I :
  O0O0ooOOO ( O000OOO , 'http:' + url , 21999992 , Ii1IIiI1i , Ii1IIiI1i , '' )
def iI1i111I1Ii ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( 'data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , O000OOO , url , i11i1ii1I in IIIii1I :
  o00oOOooOOo0o ( O000OOO , url , 21999996 , Ii1IIiI1i , Ii1IIiI1i , ( i11i1ii1I ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def o0OO0o0o00o ( url , iconimage ) :
 Ii1IIiI1i = iconimage
 i11i1ii1I = 'desc'
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , oOo0 in IIIii1I :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR] - Audio' , url , 21999997 , Ii1IIiI1i , Ii1IIiI1i , ( oOo0 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( oOo0 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR] - Text' , url , 21999998 , Ii1IIiI1i , Ii1IIiI1i , ( oOo0 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( oOo0 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def OOOoOO ( url , iconimage ) :
 Ii1IIiI1i = iconimage
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<a href="([^"]*)">Audio</a>' ) . findall ( oOOo0 )
 for url in IIIii1I :
  oo0 ( url )
def I11IIIi ( name , url , iconimage ) :
 Ii1IIiI1i = iconimage
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '</audio>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for oOo0 in IIIii1I :
  OoOoO ( ( name ) . replace ( ' - Text' , '' ) , ( oOo0 ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  if 15 - 15: oOoO0o00OO0 * oOo
  if 16 - 16: iiiiiiii1 + iii1i1iiiiIi
def O00OO ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , i11i1ii1I , I1I1 , O000OOO in IIIii1I :
  O0O0ooOOO ( O000OOO , url , 21009 , Ii1IIiI1i , I1I1 , i11i1ii1I )
  if 55 - 55: Ii . O0Oooo0O * i1iIi % oOo
def ooOOO0OOOo ( url ) :
 url = url
 oo0o0000 = oOOo0O00o ( )
 if oo0o0000 ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif oo0o0000 ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 11 - 11: iI11I1II1I1I
  if 20 - 20: IIiIiII11i % I1ii11iIi11i + oOoO0o00OO0 + oOOoOooOo
def II11iIIiiiII ( ) :
 IIo0o0O0O00oOOo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( IIo0o0O0O00oOOo , oo0O00Oooo0O0 , o0oO0 )
 I11OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11OO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
 o0O0oo0OO0O ( IIo0o0O0O00oOOo )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OO0 ( )
def o0Oooo ( ) :
 iiIoO = IIiIi ( )
 OOoOooOoOOOoo = iiIoO . replace ( ooOoOoo0O , "" )
 if os . path . exists ( iiIoO ) or not iiIoO == False :
  Iiii1iI1i = open ( iiIoO , mode = 'r' ) ; I1ii1ii11i1I = Iiii1iI1i . read ( ) ; Iiii1iI1i . close ( )
  OoOoO ( "%s - %s" % ( oo00 , OOoOooOoOOOoo ) , I1ii1ii11i1I )
 else :
  o0OoOO ( 'View Log' , 'No Log File Found!' )
def O0O0Oo00 ( log = None , count = None , all = None ) :
 if log == None :
  oOoO00o = oO00O0 ( True )
  IIi1IIIi = oO00O0 ( True , True )
  if not IIi1IIIi == False and not oOoO00o == False :
   O00Ooo = iI111I11I1I1 . select ( oOo0oooo00o , [ "View %s: %s error(s)" % ( oOoO00o . replace ( ooOoOoo0O , "" ) , O0O0Oo00 ( oOoO00o , True , True ) ) , "View %s: %s error(s)" % ( IIi1IIIi . replace ( ooOoOoo0O , "" ) , O0O0Oo00 ( IIi1IIIi , True , True ) ) ] )
   if O00Ooo == - 1 : o0OoOO ( '[COLOR %s]View Log[/COLOR]' % OOOO0OOO , '[COLOR %s]View Log Cancelled![/COLOR]' % i1i1ii ) ; return
  elif oOoO00o == False and IIi1IIIi == False :
   o0OoOO ( '[COLOR %s]View Log[/COLOR]' % OOOO0OOO , '[COLOR %s]No Log File Found![/COLOR]' % i1i1ii )
   return
  elif not oOoO00o == False : O00Ooo = 0
  elif not IIi1IIIi == False : O00Ooo = 1
  log = oOoO00o if O00Ooo == 0 else IIi1IIIi
 if log == False :
  if count == None :
   o0OoOO ( "[COLOR %s]%s[/COLOR]" % ( OOOO0OOO , oOo0oooo00o ) , "[COLOR %s]Log File not Found[/COLOR]" % i1i1ii )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   Iiii1iI1i = open ( log , mode = 'r' ) ; iII1ii1 = Iiii1iI1i . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; Iiii1iI1i . close ( )
   iI111i = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( iII1ii1 )
   if not count == None :
    if all == None :
     I1i1iiiI1 = 0
     for iIIi in iI111i :
      if o0OOO in iIIi : I1i1iiiI1 += 1
     return I1i1iiiI1
    else : return len ( iI111i )
   if len ( iI111i ) > 0 :
    I1i1iiiI1 = 0 ; I1ii1ii11i1I = ""
    for iIIi in iI111i :
     if all == None and not o0OOO in iIIi : continue
     else :
      I1i1iiiI1 += 1
      I1ii1ii11i1I += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( I1i1iiiI1 , iIIi . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( i1111 , '' ) )
    if I1i1iiiI1 > 0 :
     OoOoO ( oOo0oooo00o , I1ii1ii11i1I )
    else : o0OoOO ( oOo0oooo00o , "No Errors Found in Log" )
   else : o0OoOO ( oOo0oooo00o , "No Errors Found in Log" )
  else : o0OoOO ( oOo0oooo00o , "Log File not Found" )
def oO00O0 ( file = False , old = False , wizard = False ) :
 if wizard == True :
  if not os . path . exists ( Oo0o0000o0o0 ) : return False
  else :
   if file == True :
    return Oo0o0000o0o0
   else :
    oO0o00oo0 = open ( Oo0o0000o0o0 , 'r' )
    ii1IIII = oO0o00oo0 . read ( )
    oO0o00oo0 . close ( )
    return ii1IIII
 oO00oOooooo0 = 0
 oOoO0OOooOoO = os . listdir ( ooOoOoo0O )
 i1II1I1Iii1 = [ ]
 if 30 - 30: ii - iii1i1iiiiIi
 for iIIi in oOoO0OOooOoO :
  if old == True and iIIi . endswith ( '.old.log' ) : i1II1I1Iii1 . append ( os . path . join ( ooOoOoo0O , iIIi ) )
  elif old == False and iIIi . endswith ( '.log' ) and not iIIi . endswith ( '.old.log' ) : i1II1I1Iii1 . append ( os . path . join ( ooOoOoo0O , iIIi ) )
  if 75 - 75: iI11I1II1I1I - i1iIi . I1ii11iIi11i % Ii % i1IiiiI1iI
 if len ( i1II1I1Iii1 ) > 0 :
  i1II1I1Iii1 . sort ( key = lambda Iiii1iI1i : os . path . getmtime ( Iiii1iI1i ) )
  if file == True : return i1II1I1Iii1 [ - 1 ]
  else :
   oO0o00oo0 = open ( i1II1I1Iii1 [ - 1 ] , 'r' )
   ii1IIII = oO0o00oo0 . read ( )
   oO0o00oo0 . close ( )
   return ii1IIII
 else :
  return False
  if 55 - 55: iiiiiiii1 . IIiIiII11i % oOo * iiiiiiii1 + oOOoOooOo + i1iIi
def II11iIIiiiII ( ) :
 IIo0o0O0O00oOOo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( IIo0o0O0O00oOOo , oo0O00Oooo0O0 , o0oO0 )
 I11OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11OO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
 o0O0oo0OO0O ( IIo0o0O0O00oOOo )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OO0 ( )
def II1Iiiiii ( ) :
 ii1ii111 ( '[COLOR' + iiI1IiI + ']Todays Games[/COLOR]' , '' , 90030 , I1IIIii + 'tgames.png' , Oo00OOOOO , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport[/COLOR]' , 'http://www.replaymatches.com/' , 90037 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Replays[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , I1IIIii + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 10 - 10: O0Oooo0O % I11i1ii1 * I11i1ii1 . i1IiiiI1iI / i1iIi % OoOo0o
 if 49 - 49: oOo / OOOo00oo0oO + o0o00Oo0O * ooo0O
 if 28 - 28: oOOoOooOo + Ii / i1IiiiI1iI % iii1i1iiiiIi % I1ii11iIi11i - o0o00Oo0O
def ooo0OOO ( ) :
 iii1Ii1Ii1 = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 IIi = requests . get ( IIo0o0O0O00oOOo ) . content
 iI111i = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( IIi )
 ooO0oOo0o = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( iI111i ) )
 for IIIi1I1IIii1II , O000OOO in ooO0oOo0o :
  if not O000OOO == 'Home' :
   pass
   OOii111IiiI1 = 'http://www.replaymatches.com/' + IIIi1I1IIii1II
   if O000OOO in iii1Ii1Ii1 :
    o00oOOooOOo0o ( '[COLORred]' + O000OOO + '[/COLOR]' , OOii111IiiI1 , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
   else :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , OOii111IiiI1 , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
    if 11 - 11: iI11I1II1I1I * i1iIi
def ooOoOO0OoO00o ( url ) :
 if 11 - 11: I1ii11iIi11i - oOo0O0Ooo * IIiIiII11i . oOoO0o00OO0 . OOOo00oo0oO
 if 61 - 61: iiiiiiii1 % oOo0O0Ooo - ooo0O - IIiIiII11i % o0o00Oo0O
 if 90 - 90: iI11I1II1I1I + oOoO0o00OO0 + oOOoOooOo - O0Oooo0O * I11i1ii1 . oOoO0o00OO0
 if 37 - 37: oOOoOooOo % Ii % IIiIiII11i . o0o00Oo0O . i1iIi
 if 51 - 51: oOo - o0o00Oo0O % OOOo00oo0oO - IIiIiII11i
 if 31 - 31: iiiiiiii1 / I1ii11iIi11i - iiiiiiii1 - OoOo0o
 if 7 - 7: iiiiiiii1 % o0o00Oo0O . iii1i1iiiiIi + oOo0O0Ooo - i1IiiiI1iI
 if 75 - 75: i1IiiiI1iI
 if 71 - 71: oOOoOooOo
 if 53 - 53: ii % i1iIi . I11i1ii1 / Ii % iiiiiiii1
 oOOo0 = i11111IIIII ( url )
 iIiIIIIIii = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( oOOo0 )
 OOo0 = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iIiIIIIIii :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 900302 , Ii1IIiI1i , I1IIIii + 'tommysreplays.png' , '' )
 for ii11I1 in OOo0 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ii11I1 , 900301 , I1IIIii + 'NEXT.png' , '' , '' )
def oO0oo ( url ) :
 IIi = requests . get ( url ) . content
 iI111i = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( IIi )
 for IIIi1I1IIii1II , Ii1IIiI1i in iI111i :
  if 'Highlight' in Ii1IIiI1i :
   O000OOO = 'HighLights'
  elif '1st' in Ii1IIiI1i :
   O000OOO = '1st Half'
  elif '2nd' in Ii1IIiI1i :
   O000OOO = '2nd Half'
  else :
   O000OOO = 'Full Match'
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIIi1I1IIii1II , 1001111 , Ii1IIiI1i , I1IIIii + 'tommysreplays.png' , '' , '' )
def IIIIIo0ooOoO000oO ( ) :
 IIi = requests . get ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 iI111i = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( IIi )
 for OOo , i1i11I1I1iii1 in iI111i :
  ii1ii111 ( '[COLORred]' + OOo + '[/COLOR]' , '' , '' , I1IIIii + 'tommysreplays.png' , I1IIIii + 'tommysreplays.png' , '' , '' )
  I1iii11 = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( i1i11I1I1iii1 ) )
  for ooo0OiII1iii , i11i1iiiII in I1iii11 :
   ii1ii111 ( '[COLOR' + iiI1IiI + ']' + ooo0OiII1iii + '[/COLOR]' , '' , '' , i11i1iiiII , I1IIIii + 'tommysreplays.png' , '' , '' )
   if 68 - 68: Ii * oOo
def II1i ( url ) :
 if 2 - 2: iI11I1II1I1I * I1ii11iIi11i % OOOo00oo0oO - IIiIiII11i - iiiiiiii1
 if 3 - 3: O0Oooo0O
 if 45 - 45: O0Oooo0O
 if 83 - 83: iii1i1iiiiIi . ii
 if 58 - 58: Ii + ii % ii / I11i1ii1 / Ii
 if 62 - 62: oOo / oOoO0o00OO0
 if 7 - 7: ii . I11i1ii1
 if 53 - 53: i1iIi % i1iIi * ooo0O + iii1i1iiiiIi
 if 92 - 92: ii + ooOoO0O00 / i1iIi * o0o00Oo0O
 if 100 - 100: oOOoOooOo % iI11I1II1I1I * IIiIiII11i - iiiiiiii1
 if 92 - 92: oOOoOooOo
 if 22 - 22: I1ii11iIi11i % iiiiiiii1 * oOoO0o00OO0 / OoOo0o % Ii * i1IiiiI1iI
 if 95 - 95: ii - I11i1ii1 * oOo0O0Ooo + iii1i1iiiiIi
 if 10 - 10: ooo0O / Ii
 if 92 - 92: i1IiiiI1iI . O0Oooo0O
 if 85 - 85: oOoO0o00OO0 . O0Oooo0O
 if 78 - 78: oOOoOooOo * O0Oooo0O + iI11I1II1I1I + iI11I1II1I1I / O0Oooo0O . i1iIi
 if 97 - 97: oOOoOooOo / O0Oooo0O % ooOoO0O00 % oOoO0o00OO0
 if 18 - 18: iI11I1II1I1I % i1IiiiI1iI
 if 95 - 95: oOOoOooOo + Ii * O0Oooo0O - ooOoO0O00 * O0Oooo0O - iI11I1II1I1I
 if 75 - 75: ii * I11i1ii1
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
 OOOoO000 = liveresolver . resolve ( url )
 iIIi = xbmcgui . ListItem ( path = OOOoO000 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIi )
def oOOOO ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 IiIi1ii111i1 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiIi1ii111i1 )
def IIiIi ( ) :
 i1i1i1I = False
 if os . path . exists ( os . path . join ( ooOoOoo0O , 'xbmc.log' ) ) :
  i1i1i1I = os . path . join ( ooOoOoo0O , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'kodi.log' ) ) :
  i1i1i1I = os . path . join ( ooOoOoo0O , 'kodi.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'spmc.log' ) ) :
  i1i1i1I = os . path . join ( ooOoOoo0O , 'spmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'tvmc.log' ) ) :
  i1i1i1I = os . path . join ( ooOoOoo0O , 'tvmc.log' )
 return i1i1i1I
 if 83 - 83: OOOo00oo0oO + ii
def I111IiiIi1 ( url ) :
 if url == 'http://' : return False
 try :
  i1i = urllib2 . Request ( url )
  i1i . add_header ( 'User-Agent' , IiII )
  iiI111I1iIiI = urllib2 . urlopen ( i1i )
  iiI111I1iIiI . close ( )
 except Exception , o00o :
  return o00o
 return True
def Ii1IIiiIIi ( ) :
 if 88 - 88: ii + i1IiiiI1iI * IIiIiII11i % I1ii11iIi11i
 if 17 - 17: I11i1ii1 * OoOo0o - oOo / Ii
 if 79 - 79: O0Oooo0O . OOOo00oo0oO - IIiIiII11i . oOo0O0Ooo % oOOoOooOo
 if 65 - 65: oOo0O0Ooo + iii1i1iiiiIi / OoOo0o
 if 83 - 83: ooo0O . iiiiiiii1 - I1ii11iIi11i
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def Ooo0O ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   o0oo0000OO ( )
  if iiI == 1 :
   O0oOOo0Oo ( )
  if iiI == 2 :
   o000O000 ( ii1 )
  if iiI == 3 :
   oOoO0o0ooo ( IIo0o0O0O00oOOo )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 10060 , I1IIIii + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 49 , I1IIIii + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( O00OOOoOoo0O ) , 41 , I1IIIii + 'WipeGenie.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( O00OOOoOoo0O ) , 44 , I1IIIii + 'GenieBuilds.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 86 - 86: oOoO0o00OO0 * o0o00Oo0O * I11i1ii1
def Ooo0oo ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if 41 - 41: iii1i1iiiiIi * i1IiiiI1iI / iii1i1iiiiIi % OOOo00oo0oO
  if 18 - 18: IIiIiII11i . ii % iii1i1iiiiIi % i1iIi
  if O0oo0OO0 . getSetting ( 'Search' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( O00OOOoOoo0O ) , 9000 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'HeroVision' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie On Demand Streams[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3NoYWthL0dPRFMucGhw' ) ) , 1016 , I1IIIii + 'gods.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , I1IIIii + 'Bamf.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BOSS DOCS[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , I1IIIii + 'boss.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Supremacy[/COLOR]' , '' , 1131000 , I1IIIii + 'supremacy.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 4004 , I1IIIii + 'Movies.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( O00OOOoOoo0O ) , 4005 , I1IIIii + 'TVShows.png' , Oo00OOOOO , '' )
  if 9 - 9: oOo - I1ii11iIi11i * ii . I1ii11iIi11i
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( O00OOOoOoo0O ) , 10001 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
  if 2 - 2: ii % OoOo0o
  if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
  if 39 - 39: iiiiiiii1 / IIiIiII11i / oOoO0o00OO0 % oOo0O0Ooo
  if 89 - 89: O0Oooo0O + ii + O0Oooo0O * ooOoO0O00 + iI11I1II1I1I % i1IiiiI1iI
  if 59 - 59: OoOo0o + Ii
  if 88 - 88: Ii - oOOoOooOo
  if 67 - 67: OoOo0o . I1ii11iIi11i + iii1i1iiiiIi - ii
 else :
  if 70 - 70: OoOo0o / IIiIiII11i - iI11I1II1I1I - iiiiiiii1
  if 11 - 11: iI11I1II1I1I . ii . IIiIiII11i / ooOoO0O00 - i1IiiiI1iI
  if O0oo0OO0 . getSetting ( 'Search' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( O00OOOoOoo0O ) , 9000 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie On Demand Streams[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3NoYWthL0dPRFMucGhw' ) ) , 1016 , I1IIIii + 'gods.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , I1IIIii + 'Bamf.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Supremacy[/COLOR]' , '' , 1131000 , I1IIIii + 'supremacy.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BOSS DOCS[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , I1IIIii + 'boss.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 4004 , I1IIIii + 'Movies.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( O00OOOoOoo0O ) , 4005 , I1IIIii + 'TVShows.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( O00OOOoOoo0O ) , 10001 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']COZY CORNER[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 21999990 , I1IIIii + 'zone.png' , Oo00OOOOO , '' )
  if 30 - 30: iii1i1iiiiIi
  if 21 - 21: Ii / O0Oooo0O % OoOo0o * o0o00Oo0O . i1IiiiI1iI - iI11I1II1I1I
  if 26 - 26: IIiIiII11i * iii1i1iiiiIi
  if 10 - 10: IIiIiII11i . iiiiiiii1
  if 32 - 32: i1iIi . I11i1ii1 . ii - oOo + OOOo00oo0oO
  if 88 - 88: iiiiiiii1
  if 19 - 19: IIiIiII11i * I11i1ii1 + i1iIi
  if 65 - 65: OoOo0o . O0Oooo0O . oOo . iiiiiiii1 - OoOo0o
  if 19 - 19: Ii + iiiiiiii1 % oOOoOooOo
  if 14 - 14: oOo . IIiIiII11i . i1IiiiI1iI / i1iIi % oOoO0o00OO0 - oOOoOooOo
  if 67 - 67: i1IiiiI1iI - OoOo0o . ooOoO0O00
  if 35 - 35: iiiiiiii1 + oOOoOooOo - OOOo00oo0oO . iiiiiiii1 . I11i1ii1
  if 87 - 87: iii1i1iiiiIi
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
 iIiIi11 ( 'movies' , 'MAIN' )
def OOO0ooo ( ) :
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  IIiiii ( )
 if iiI == 1 :
  iI111i1I1II ( )
 if iiI == 2 :
  O00OOII1Ii1iI1i1 ( )
 if iiI == 3 :
  o0OoO000O ( )
 if iiI == 4 :
  OOoiIIiiIIIi1I ( )
 if iiI == 5 :
  OO0o0o0oo0O ( )
  if 40 - 40: ooo0O + I1ii11iIi11i . ooo0O % oOOoOooOo
  if 15 - 15: i1iIi * I1ii11iIi11i % oOoO0o00OO0 * iI11I1II1I1I - Ii
def Oo00OOOOoo0oo ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   O00OOooo0Ooo ( )
  if iiI == 1 :
   o0oOOoOOO ( )
  if iiI == 2 :
   iiI1i11II ( )
  if iiI == 3 :
   II11 ( o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iiI == 4 :
   I1iii ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9001 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 10200 , I1IIIii + 'rated.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , I1IIIii + 'Desi.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , I1IIIii + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , I1IIIii + 'ClassicMovies.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
def oOO0OO0O ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 78 - 78: i1iIi / IIiIiII11i % iii1i1iiiiIi
 if 52 - 52: OoOo0o - iiiiiiii1 * OOOo00oo0oO
 if 17 - 17: ii + OoOo0o * i1IiiiI1iI * iii1i1iiiiIi
 if 36 - 36: o0o00Oo0O + I1ii11iIi11i
 if 5 - 5: I1ii11iIi11i * iii1i1iiiiIi
def ii1I11iIiIII1 ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , '[COLOR' + iiI1IiI + ']THE SOURCE[/COLOR]' , '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oOO0OOOOoooO ( )
  if iiI == 1 :
   i1ii11 ( 'http://www.tvmaze.com/shows' )
  if iiI == 2 :
   ii1i ( )
  if iiI == 3 :
   IIioo0OO ( )
  if iiI == 4 :
   IiiI11i1I ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9002 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , 'http://www.tvmaze.com/shows' , 9110001 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , str ( O00OOOoOoo0O ) , 10095 , I1IIIii + 'RD.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( O00OOOoOoo0O ) , 8064 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
def OOo0iiIii1IIi ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   ii1IiIiI1 = '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]'
   if 90 - 90: ooo0O - Ii + ooOoO0O00 - i1iIi % I1ii11iIi11i
   if 59 - 59: OoOo0o % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * I11i1ii1
   if 41 - 41: i1iIi % oOoO0o00OO0
   if 12 - 12: OoOo0o
  I11iIi1i1II11 = [ ii1IiIiI1 , '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , '[COLOR' + iiI1IiI + ']PIRATE MOVIES[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   ooOo0O ( )
  if iiI == 1 :
   i1I1IIIiiI ( )
  if iiI == 2 :
   OO0O0ooOOO00 ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if iiI == 3 :
   IiIiiiiI1 ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , OO00OOoO0o , O000OOO )
 else :
  if 4 - 4: ooOoO0O00 - Ii / Ii / ii
  if 100 - 100: I1ii11iIi11i + ooo0O - o0o00Oo0O % IIiIiII11i . iiiiiiii1
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 92 - 92: IIiIiII11i * ii - O0Oooo0O
  if 58 - 58: iI11I1II1I1I + o0o00Oo0O
  if 30 - 30: oOOoOooOo % iiiiiiii1 * OoOo0o - oOoO0o00OO0 * i1iIi % oOOoOooOo
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , I1IIIii + 'bamftv.png' , Oo00OOOOO , '' )
  if 46 - 46: Ii - o0o00Oo0O . OOOo00oo0oO
  if 100 - 100: oOo0O0Ooo / ooo0O * iiiiiiii1 . o0o00Oo0O / OoOo0o
  if 83 - 83: O0Oooo0O
  if 48 - 48: IIiIiII11i * OoOo0o * O0Oooo0O
  if 50 - 50: I11i1ii1 % ooOoO0O00
  if 21 - 21: ii - iI11I1II1I1I
  if 93 - 93: OOOo00oo0oO - ooo0O % iii1i1iiiiIi . iii1i1iiiiIi - oOOoOooOo
 iIiIi11 ( 'movies' , 'MAIN' )
 if 90 - 90: oOOoOooOo + IIiIiII11i * oOoO0o00OO0 / i1iIi . ooo0O + ooo0O
def I11IoOoO ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
def OO0O0ooOOO00 ( url ) :
 IIi = i11111IIIII ( url )
 ooO0oOo0o = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( IIi )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( ooO0oOo0o ) )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( ooO0oOo0o ) )
 iIIii = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( ooO0oOo0o ) )
 for O000OOO , Ii1IIiI1i , url in iI111i :
  if '247ch' in url :
   IIII ( O000OOO , url , 10190 , Ii1IIiI1i )
  elif '.m3u' in url :
   IIII ( O000OOO , url , 1019 , Ii1IIiI1i )
  elif '.xml' in url :
   IIII ( O000OOO , url , 1018 , Ii1IIiI1i )
  else :
   iI1iiiIiii ( O000OOO , url , 222 , Ii1IIiI1i )
 for O000OOO , url , Ii1IIiI1i in IIi11i1i1iI1 :
  if '.xml' in url :
   IIII ( O000OOO , url , 1018 , Ii1IIiI1i )
  elif '.m3u' in url :
   IIII ( O000OOO , url , 1019 , Ii1IIiI1i )
  else :
   iI1iiiIiii ( O000OOO , url , 222 , Ii1IIiI1i )
 for O000OOO , url , Ii1IIiI1i in iIIii :
  iI1iiiIiii ( O000OOO , url , 8043 , Ii1IIiI1i )
def ii1i1i ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'BAMFTV.png' )
def oOO0oo ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url , Ii1IIiI1i in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , Ii1IIiI1i )
  if 13 - 13: ii * OOOo00oo0oO - i1iIi / OoOo0o + i1IiiiI1iI + I11i1ii1
def i1I1IIIiiI ( ) :
 if 39 - 39: iI11I1II1I1I - ii
 ii1ii111 ( '[COLOR' + iiI1IiI + ']All Movies[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 ii1ii111 ( '[COLOR' + iiI1IiI + ']Movies By Genre[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 ii1ii111 ( '[COLOR' + iiI1IiI + ']Movies By A - Z[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 ii1ii111 ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 9110015 , I1IIIii + 'Search.png' , Oo00OOOOO , '' , '' )
 if 81 - 81: oOoO0o00OO0 - o0o00Oo0O * ii
 if 23 - 23: IIiIiII11i / OOOo00oo0oO
 if 28 - 28: I1ii11iIi11i * oOOoOooOo - oOo
 if 19 - 19: i1IiiiI1iI
def Ooooo0OoO0 ( url ) :
 IIi = requests . get ( url ) . text
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( IIi )
 for iI1 , iIi1i , OO0Oo , i11i1iiiII , IiIIIIIIiI , OOooo00 , I1I1 in iI111i :
  if I1I1 == ' ' :
   I1I1 = Oo00OOOOO
  if i11i1iiiII == ' ' :
   i11i1iiiII = O0O
  IiIIIIIIiI = IiIIIIIIiI . replace ( '\\n' , ' ' )
  if iIi1i == 'Movie Search' :
   Ii111iIi1iIi ( iI1 , OOooo00 , 9110014 , i11i1iiiII , I1I1 , IiIIIIIIiI , '' )
  elif iIi1i == 'Menu' :
   ii1ii111 ( iI1 , OO0Oo , 9110013 , i11i1iiiII , I1I1 , IiIIIIIIiI , '' )
   if 35 - 35: O0Oooo0O . iii1i1iiiiIi * Ii
def iiII ( name , url ) :
 from imports import Scrape_Nan
 name = str ( name )
 OOooo00 = str ( url )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( name , OOooo00 , '' )
 if 57 - 57: i1IiiiI1iI . I1ii11iIi11i + IIiIiII11i
def i111i11I1ii ( ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 OOooo = iI111I11I1I1 . input ( 'Search your moive' , type = xbmcgui . INPUT_ALPHANUM )
 iii1Ii1Ii1 = [ 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ]
 for IIo0o0O0O00oOOo in iii1Ii1Ii1 :
  IIi = requests . get ( o0oOoO00o ( IIo0o0O0O00oOOo ) ) . content
  iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( IIi )
  for iI1 , iIi1i , OO0Oo , i11i1iiiII , IiIIIIIIiI , OOooo00 , I1I1 in iI111i :
   if I1I1 == ' ' :
    I1I1 = Oo00OOOOO
   if i11i1iiiII == ' ' :
    i11i1iiiII = O0O
   IiIIIIIIiI = IiIIIIIIiI . replace ( '\\n' , ' ' )
   if iIi1i == 'Movie Search' :
    if OOooo . lower ( ) in iI1 . lower ( ) :
     Ii111iIi1iIi ( iI1 , OOooo00 , 9110014 , i11i1iiiII , I1I1 , IiIIIIIIiI , '' )
def oo0oOO ( url ) :
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oOOo0 )
 for O000OOO , url , iIi1i , oo0O0oO0O0O , I1I1 , i11i1ii1I in iI111i :
  if oo0O0oO0O0O == '123' :
   oo0O0oO0O0O = I1IIIii + 'appstreams.png'
  if I1I1 == '123' :
   I1I1 = I1IIIii + 'appstreams.png'
  if 'php' in url :
   o00oOOooOOo0o ( O000OOO , url , 100010 , oo0O0oO0O0O , I1I1 , i11i1ii1I )
  elif 'playlist' in url :
   o00oOOooOOo0o ( O000OOO , url , 100007 , oo0O0oO0O0O , I1I1 , i11i1ii1I )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( O000OOO , url , 100100 , oo0O0oO0O0O , I1I1 , i11i1ii1I )
  elif not 'http' in url :
   Ii111iIi1iIi ( O000OOO , url , 100009 , oo0O0oO0O0O , I1I1 , i11i1ii1I , '' )
  else :
   Ii111iIi1iIi ( O000OOO , url , 100005 , oo0O0oO0O0O , I1I1 , i11i1ii1I , '' )
   if 69 - 69: OOOo00oo0oO / Ii
def OOo00 ( url ) :
 oOOo0 = II1i11i1iIi11 ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , i11i1ii1I , I1I1 , O000OOO in IIIii1I :
  if Ii1IIiI1i == '123' :
   Ii1IIiI1i = I1IIIii + 'appstreams.png'
  if I1I1 == '123' :
   I1I1 = Oo00OOOOO
  if 'php' in url :
   o00oOOooOOo0o ( O000OOO , url , 100004 , Ii1IIiI1i , I1I1 , i11i1ii1I )
  elif 'playlist' in url :
   o00oOOooOOo0o ( O000OOO , url , 100007 , Ii1IIiI1i , I1I1 , i11i1ii1I )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( O000OOO , url , 100100 , Ii1IIiI1i , I1I1 , i11i1ii1I )
  elif not 'http' in url :
   Ii111iIi1iIi ( O000OOO , url , 100009 , Ii1IIiI1i , I1I1 , i11i1ii1I , '' )
  else :
   Ii111iIi1iIi ( O000OOO , url , 100005 , Ii1IIiI1i , I1I1 , i11i1ii1I , '' )
   if 22 - 22: OOOo00oo0oO
def ii1ii ( url ) :
 if 79 - 79: I1ii11iIi11i - ii . o0o00Oo0O
 oOOo0 = II1i11i1iIi11 ( url )
 OOoO00oo0000O = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oOOo0 )
 for ooO0oOo0o in OOoO00oo0000O :
  oo0O0oO0O0O = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( ooO0oOo0o ) )
  for oo0O0oO0O0O in oo0O0oO0O0O :
   oo0O0oO0O0O = oo0O0oO0O0O
  O000OOO = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( ooO0oOo0o ) )
  for O000OOO in O000OOO :
   if 'elete' in O000OOO :
    pass
   elif 'rivate Vid' in O000OOO :
    pass
   else :
    O000OOO = ( O000OOO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  Ii1IIi = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( ooO0oOo0o ) )
  for Ii1IIi in Ii1IIi :
   Ii1IIi = Ii1IIi
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( ooO0oOo0o ) )
  for url in url :
   url = url
  Ii111iIi1iIi ( '[COLORred]' + str ( Ii1IIi ) + '[/COLOR] : ' + str ( O000OOO ) , str ( url ) , 100009 , str ( oo0O0oO0O0O ) , Oo00OOOOO , '' , '' )
  iIiIi11 ( 'movies' , '' )
  if 70 - 70: oOo0O0Ooo / i1IiiiI1iI
def IIiiiiIiIIii ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search Dans Scrapes' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'http://www.tvmaze.com/search?q=' + ( OOooo ) . replace ( ' ' , '+' )
 IIIiIiI = O0OO . lower ( )
 oOOo0 = i11111IIIII ( IIIiIiI )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  I1i = 'http://www.tvmaze.com' + IIo0o0O0O00oOOo . replace ( '"' , '' )
  i1II1iII = requests . get ( I1i ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( i1II1iII )
  for i11i1ii1I in iI111i :
   if not '<div>' in i11i1ii1I :
    II1io0OO00oo = i11i1ii1I . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   Ii1IIiI1i = 'http:' + Ii1IIiI1i
   O000OOO = O000OOO . replace ( '&#039;' , '' )
   if O000OOO == '' :
    i1i1IiIiIi1Ii = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( IIo0o0O0O00oOOo ) )
    for O000OOO in i1i1IiIiIi1Ii :
     O000OOO = O000OOO . replace ( '-' , ' ' )
  ii1ii111 ( O000OOO , I1i , 9110002 , Ii1IIiI1i , Oo00OOOOO , II1io0OO00oo , '' )
  if 64 - 64: OoOo0o + ii * ii
def i1ii11 ( url ) :
 IIII ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 9110004 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
 IIi = requests . get ( url ) . content
 iI111i = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( IIi )
 ii11I1 = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( IIi )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  I1i = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  if 41 - 41: oOOoOooOo . I1ii11iIi11i + oOo0O0Ooo
  i1II1iII = requests . get ( I1i ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( i1II1iII )
  for i11i1ii1I in iI111i :
   if not '<div>' in i11i1ii1I :
    II1io0OO00oo = i11i1ii1I . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   Ii1IIiI1i = 'http:' + Ii1IIiI1i
   O000OOO = O000OOO . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if O000OOO == '' :
    i1i1IiIiIi1Ii = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for O000OOO in i1i1IiIiIi1Ii :
     O000OOO = O000OOO . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  ii1ii111 ( O000OOO , I1i , 9110002 , Ii1IIiI1i , Oo00OOOOO , II1io0OO00oo , '' )
  if 100 - 100: i1iIi + oOo
 for OOo0 in ii11I1 :
  url = 'http://www.tvmaze.com' + OOo0
  ii1ii111 ( 'NEXT' , url , 9110001 , Ii1IIiI1i , Oo00OOOOO , '' , '' )
def Oo00o0OO ( url ) :
 IIi = requests . get ( url ) . content
 iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIi )
 for i11i1ii1I in iI111i :
  II1io0OO00oo = i11i1ii1I . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
 return II1io0OO00oo
def OO0ooo0o0 ( url , name , iconimage ) :
 iI1 = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 Ii1IIiI1i = iconimage
 IIi = requests . get ( url + '/episodes' ) . content
 i1II1iII = requests . get ( url ) . content
 ooO0oOo0o = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( IIi )
 iI111i = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( i1II1iII )
 for oO0ooOoO in iI111i :
  oO0ooOoO = oO0ooOoO . replace ( ' ' , '' )
 for ooO0000o00O , i1i11I1I1iii1 in ooO0oOo0o :
  if not 'special' in ooO0000o00O . lower ( ) :
   ooO0000o00O = ooO0000o00O . replace ( 'S' , '' ) . replace ( 's' , '' )
  O0Ooo = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( i1i11I1I1iii1 ) )
  for oO00oOOo0Oo , IIiIIIIii , iI in O0Ooo :
   if not 'special' in oO00oOOo0Oo . lower ( ) :
    ii1ii111 ( iI1 + ' - SEASON -' + ooO0000o00O + '- EPISODE-' + oO00oOOo0Oo + '-' + oO0ooOoO , '' , 9110003 , Ii1IIiI1i , Oo00OOOOO , '' , iI1 )
    if 5 - 5: ooo0O . iI11I1II1I1I % iI11I1II1I1I
    if 56 - 56: ii - i1IiiiI1iI - ooOoO0O00
    if 8 - 8: O0Oooo0O / OoOo0o . oOo0O0Ooo + oOoO0o00OO0 / Ii
def I1Iii1iI1 ( name , extra ) :
 if 86 - 86: o0o00Oo0O
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 from imports import Scrape_Nan
 O0o0oOooOoOo = name + '<>'
 I1iOo = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( O0o0oOooOoOo ) )
 for iI1 , IiIiIi1I1 , IiI1ii1Ii , oO0ooOoO in I1iOo :
  iI1 = iI1
  IiIiIi1I1 = IiIiIi1I1
  IiI1ii1Ii = IiI1ii1Ii
  oooOOOoOOOo0O = ''
  Scrape_Nan . scrape_episode ( iI1 , oO0ooOoO , '' , IiIiIi1I1 , IiI1ii1Ii , '' )
if 82 - 82: I11i1ii1 * Ii % IIiIiII11i - ii
if 90 - 90: I1ii11iIi11i . OOOo00oo0oO * ooOoO0O00 - ooOoO0O00
if 16 - 16: oOo0O0Ooo * ooOoO0O00 - ooo0O . I11i1ii1 % i1IiiiI1iI / ooo0O
if 14 - 14: iI11I1II1I1I * O0Oooo0O * oOoO0o00OO0 / iI11I1II1I1I * I11i1ii1 / i1IiiiI1iI
if 77 - 77: oOo + O0Oooo0O + O0Oooo0O * i1iIi / ii . i1iIi
if 62 - 62: ooOoO0O00 - ooOoO0O00
if 69 - 69: iii1i1iiiiIi % OOOo00oo0oO - i1IiiiI1iI
if 38 - 38: iI11I1II1I1I + Ii / Ii % oOo / oOOoOooOo % i1iIi
if 7 - 7: I11i1ii1 * oOo0O0Ooo + ooOoO0O00 + Ii + I1ii11iIi11i % oOo0O0Ooo
if 62 - 62: ooo0O - i1iIi * iii1i1iiiiIi - Ii % oOOoOooOo
if 52 - 52: oOoO0o00OO0 % OOOo00oo0oO - Ii
def i1III ( ) :
 ii1ii111 ( 'Featured 24/7' , '' , 9070000 , I1IIIii + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 ii1ii111 ( '24/7 Tv Thows' , '' , 9080000 , I1IIIii + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 ii1ii111 ( '24/7 Movies' , '' , 9090000 , I1IIIii + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 ii1ii111 ( '24/7 Cable' , '' , 9100000 , I1IIIii + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 ii1ii111 ( '24/7 Random Stream' , '' , 9110000 , I1IIIii + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 6 - 6: iiiiiiii1 . i1IiiiI1iI + i1iIi . O0Oooo0O
def oOoO0o ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 i111iiIIII = 'index.php#shows'
 IIi = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + i111iiIIII ) . content )
 OOO00OOo0o0Oo = IIi . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for ooooOoO0O in OOO00OOo0o0Oo :
  IIIIIIII = ooooOoO0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in IIIIIIII :
   oOoOo0oOo0O0O0o = IIIi1I1IIii1II . text
  IiiIIiIIii1iI = ooooOoO0O . findAll ( 'a' )
  for IIIi1I1IIii1II in IiiIIiIIii1iI :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Oo0O0O000 = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   II1Ii = { 'User-Agent' : random_agent ( ) }
   OOoO00ooO = requests . get ( Oo0O0O000 , headers = II1Ii ) . content
   I1IIIIiii1i = packets ( OOoO00ooO )
   if 51 - 51: OoOo0o . oOo0O0Ooo
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( I1IIIIiii1i )
   for Oo in iI111i :
    Oo = Oo . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    i11III1II1 = 'https:' + Oo + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ii111iIi1iIi ( O000OOO , i11III1II1 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 42 - 42: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 - i1iIi % I11i1ii1
    if 36 - 36: Ii / OOOo00oo0oO * oOoO0o00OO0 * oOoO0o00OO0 + i1iIi * i1IiiiI1iI
def iIiI1i ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 i111iiIIII = 'index.php#movies'
 IIi = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + i111iiIIII ) . content )
 OOO00OOo0o0Oo = IIi . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for ooooOoO0O in OOO00OOo0o0Oo :
  IIIIIIII = ooooOoO0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in IIIIIIII :
   oOoOo0oOo0O0O0o = IIIi1I1IIii1II . text
  IiiIIiIIii1iI = ooooOoO0O . findAll ( 'a' )
  for IIIi1I1IIii1II in IiiIIiIIii1iI :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Oo0O0O000 = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   II1Ii = { 'User-Agent' : random_agent ( ) }
   OOoO00ooO = requests . get ( Oo0O0O000 , headers = II1Ii ) . content
   I1IIIIiii1i = packets ( OOoO00ooO )
   if 31 - 31: i1iIi
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( I1IIIIiii1i )
   for Oo in iI111i :
    Oo = Oo . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    i11III1II1 = 'https:' + Oo + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ii111iIi1iIi ( O000OOO , i11III1II1 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 78 - 78: Ii + ooo0O + O0Oooo0O / ooo0O % iI11I1II1I1I % I11i1ii1
    if 83 - 83: iI11I1II1I1I % iii1i1iiiiIi % ooo0O % O0Oooo0O . oOoO0o00OO0 % o0o00Oo0O
def iIiIi1ii ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 i111iiIIII = 'index.php#cable'
 IIi = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + i111iiIIII ) . content )
 OOO00OOo0o0Oo = IIi . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for ooooOoO0O in OOO00OOo0o0Oo :
  IIIIIIII = ooooOoO0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in IIIIIIII :
   oOoOo0oOo0O0O0o = IIIi1I1IIii1II . text
  IiiIIiIIii1iI = ooooOoO0O . findAll ( 'a' )
  for IIIi1I1IIii1II in IiiIIiIIii1iI :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Oo0O0O000 = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   II1Ii = { 'User-Agent' : random_agent ( ) }
   OOoO00ooO = requests . get ( Oo0O0O000 , headers = II1Ii ) . content
   I1IIIIiii1i = packets ( OOoO00ooO )
   if 28 - 28: iI11I1II1I1I + iI11I1II1I1I
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( I1IIIIiii1i )
   for Oo in iI111i :
    Oo = Oo . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    i11III1II1 = 'https:' + Oo + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ii111iIi1iIi ( O000OOO , i11III1II1 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 28 - 28: OOOo00oo0oO
def ooo0oo ( ) :
 i1II1iII = 'http://arconaitv.me/stream.php?id=random'
 II1Ii = { 'User-Agent' : random_agent ( ) }
 OOoO00ooO = requests . get ( i1II1iII , headers = II1Ii ) . content
 I1IIIIiii1i = packets ( OOoO00ooO )
 if 8 - 8: oOo + iii1i1iiiiIi . iI11I1II1I1I % o0o00Oo0O
 iI111i = re . compile ( "'https:(.+?)'" ) . findall ( I1IIIIiii1i )
 for Oo in iI111i :
  Oo = Oo . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  i11III1II1 = 'https:' + Oo + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  Ii111iIi1iIi ( 'Random Pick' , i11III1II1 , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 43 - 43: oOoO0o00OO0 - iiiiiiii1
def O000O ( ) :
 IIo0o0O0O00oOOo = 'http://arconaitv.me/'
 i111iiIIII = 'index.php#shows'
 if 98 - 98: iI11I1II1I1I + O0Oooo0O % iii1i1iiiiIi + i1IiiiI1iI % iii1i1iiiiIi
 IIi = BeautifulSoup ( requests . get ( IIo0o0O0O00oOOo + i111iiIIII ) . content )
 OOO00OOo0o0Oo = IIi . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for ooooOoO0O in OOO00OOo0o0Oo :
  IIIIIIII = ooooOoO0O . findAll ( 'a' )
  for IIIi1I1IIii1II in IIIIIIII :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    Oo0O0O000 = IIo0o0O0O00oOOo + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    O000OOO = IIIi1I1IIii1II [ 'title' ]
   iI1I1I11IiII = IIIi1I1IIii1II . findAll ( 'img' )
   for iIii11iI1II in iI1I1I11IiII :
    Ii1IIiI1i = IIo0o0O0O00oOOo + iIii11iI1II [ 'src' ]
    II1Ii = { 'User-Agent' : random_agent ( ) }
    OOoO00ooO = requests . get ( Oo0O0O000 , headers = II1Ii ) . content
    I1IIIIiii1i = packets ( OOoO00ooO )
    if 42 - 42: oOOoOooOo - oOo0O0Ooo + oOoO0o00OO0 % i1iIi
    iI111i = re . compile ( "'https:(.+?)'" ) . findall ( I1IIIIiii1i )
    for Oo in iI111i :
     Oo = Oo . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     i11III1II1 = 'https:' + Oo + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     Ii111iIi1iIi ( O000OOO , i11III1II1 , 9060000 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
     if 44 - 44: ooOoO0O00 - o0o00Oo0O - oOoO0o00OO0 * oOoO0o00OO0 + iii1i1iiiiIi
def O0oo ( name , url ) :
 import urlresolver
 try :
  OOOo00 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( OOOo00 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 91 - 91: iI11I1II1I1I . ooo0O . oOoO0o00OO0 + ii
 if 69 - 69: O0Oooo0O - oOo0O0Ooo
def oOoo0OooOOo00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , i11i1ii1I , I1I1 , O000OOO in IIIii1I :
  if '.php' in url :
   o00oOOooOOo0o ( O000OOO , url , 100210 , Ii1IIiI1i , I1I1 , i11i1ii1I )
  else :
   O0O0ooOOO ( O000OOO , url , 222 , Ii1IIiI1i , I1I1 , i11i1ii1I )
   if 36 - 36: ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / ooo0O + iii1i1iiiiIi - ii
   if 39 - 39: ii * OoOo0o * o0o00Oo0O . i1IiiiI1iI . oOo + oOOoOooOo
   if 9 - 9: iii1i1iiiiIi + OOOo00oo0oO % ii + ooo0O
def ooOO0o ( iconimage , url , extra ) :
 oo0O0oO0O0O = ' '
 oO0O0oO0 = ' '
 I1I1 = ' '
 IiIiIi1I1 = ' '
 I11Ii1iI11iI1 = II1i11i1iIi11 ( url )
 oo0O0oO0O0O = re . compile ( '<img src="(.+?)">' ) . findall ( I11Ii1iI11iI1 )
 for oo0O0oO0O0O in oo0O0oO0O0O :
  oo0O0oO0O0O = oo0O0oO0O0O
 i1III1 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( I11Ii1iI11iI1 )
 for I1I1 in i1III1 :
  I1I1 = I1I1
 iI111i = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( I11Ii1iI11iI1 )
 for url , IiIiIi1I1 in iI111i :
  IiIiIi1I1 = 'S' + ( IiIiIi1I1 ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o00OO00OoO + url
  ii1ii111 ( ( IiIiIi1I1 ) . replace ( '  ' , '' ) , url , 100101 , oo0O0oO0O0O , I1I1 , oO0O0oO0 , '' )
  iIiIi11 ( 'Movies' , 'info' )
  if 43 - 43: IIiIiII11i % O0Oooo0O . i1IiiiI1iI % o0o00Oo0O - ii + o0o00Oo0O
def OooO0ooo0 ( url , name , fanart , extra , iconimage ) :
 iIiI = extra
 IiIiIi1I1 = name
 I11Ii1iI11iI1 = II1i11i1iIi11 ( url )
 oo0O0oO0O0O = iconimage
 iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( I11Ii1iI11iI1 )
 for url , name , oO00Ooo0oO in iI111i :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o00OO00OoO + url
  oO00Ooo0oO = oO00Ooo0oO
  OOOo = name + ' - [COLORred]' + oO00Ooo0oO + '[/COLOR]'
  ii1ii111 ( OOOo , url , 100102 , oo0O0oO0O0O , fanart , 'Aired : ' + oO00Ooo0oO , OOOo )
  if 74 - 74: i1iIi - ii . I1ii11iIi11i
def III1Ii1i1I1 ( name , URL , iconimage , fanart ) :
 oOOo0 = II1i11i1iIi11 ( URL )
 iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , name in iI111i :
  for iIIi in OOOO0OOoO0O0 :
   if iIIi in IIo0o0O0O00oOOo :
    URL = 'http://www.watchseriesgo.to/link/' + IIo0o0O0O00oOOo
    Ii111iIi1iIi ( name , URL , 100106 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( iI111i ) <= 0 :
  ii1ii111 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 97 - 97: O0Oooo0O . oOOoOooOo - O0Oooo0O + oOo0O0Ooo * IIiIiII11i
  if 10 - 10: i1iIi + i1IiiiI1iI % ii - oOo0O0Ooo
def o00oooOo ( url , name ) :
 iiO0O0o0oO0O00 = name
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oOOo0 )
 iIIii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oOOo0 )
 for url in iI111i :
  o0O0oO0 ( url , iiO0O0o0oO0O00 )
 for url in IIi11i1i1iI1 :
  o0O0oO0 ( url , iiO0O0o0oO0O00 )
 for url in iIIii :
  o0O0oO0 ( url , iiO0O0o0oO0O00 )
  if 77 - 77: o0o00Oo0O . i1iIi
def o0O0oO0 ( url , season_name ) :
 if 'daclips.in' in url :
  i1i1IiIi1 ( url , season_name )
 elif 'filehoot.com' in url :
  I1iiIiI1iI1I ( url , season_name )
 elif 'allmyvideos.net' in url :
  III1II111Ii1 ( url , season_name )
 elif 'vidspot.net' in url :
  o0O0OO0o ( url , season_name )
 elif 'vodlocker' in url :
  OOOoOo ( url , season_name )
 elif 'vidto' in url :
  OOoO0oo0O ( url , season_name )
  if 49 - 49: ooo0O
  if 31 - 31: oOo * Ii * i1iIi . Ii
def OOoO0oo0O ( url , season_name ) :
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for OOii111IiiI1 , O000OOO in iI111i :
  II11iI1iiI ( OOii111IiiI1 , season_name )
  if 48 - 48: i1IiiiI1iI . ii . oOo0O0Ooo . iii1i1iiiiIi % oOoO0o00OO0 / iiiiiiii1
  if 11 - 11: ooOoO0O00 % oOo % iiiiiiii1
def III1II111Ii1 ( url , season_name ) :
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for OOii111IiiI1 , O000OOO in iI111i :
  II11iI1iiI ( OOii111IiiI1 , season_name )
  if 99 - 99: oOOoOooOo / iI11I1II1I1I - i1iIi * oOoO0o00OO0 % oOo0O0Ooo
def o0O0OO0o ( url , season_name ) :
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oOOo0 )
 for OOii111IiiI1 , O000OOO in iI111i :
  II11iI1iiI ( OOii111IiiI1 , season_name )
  if 13 - 13: oOo
def OOOoOo ( url , season_name ) :
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for OOii111IiiI1 in iI111i :
  II11iI1iiI ( OOii111IiiI1 , season_name )
  if 70 - 70: O0Oooo0O + o0o00Oo0O . OOOo00oo0oO * i1iIi
def i1i1IiIi1 ( url , season_name ) :
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oOOo0 )
 for OOii111IiiI1 in iI111i :
  II11iI1iiI ( OOii111IiiI1 , season_name )
  if 2 - 2: ii . OoOo0o . I11i1ii1
def I1iiIiI1iI1I ( url , season_name ) :
 oOOo0 = II1i11i1iIi11 ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for OOii111IiiI1 in iI111i :
  II11iI1iiI ( OOii111IiiI1 , season_name )
  if 42 - 42: OoOo0o % OOOo00oo0oO / oOo - OOOo00oo0oO * Ii
def II11iI1iiI ( Link , season_name ) :
 if 'http:/' in Link :
  iI1IiiiIiI1Ii ( Link )
  if 78 - 78: ii / OoOo0o % iii1i1iiiiIi * ii
  if 68 - 68: OOOo00oo0oO
def i11i11 ( url ) :
 oOOo0 = OPEN_URL_1 ( url )
 Ii11Iii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOo0 )
 for url in Ii11Iii :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 68 - 68: oOo0O0Ooo % o0o00Oo0O
def ii1ii111 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = True )
 return oo0O0o
 if 79 - 79: ii - I11i1ii1 * I11i1ii1 . iii1i1iiiiIi
 if 100 - 100: IIiIiII11i * i1IiiiI1iI % oOo0O0Ooo / oOoO0o00OO0
def Ii111iIi1iIi ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOoo0oOO00 = [ ]
  OOoo0oOO00 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  IioO0O . addContextMenuItems ( OOoo0oOO00 )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = False )
 return oo0O0o
 if 46 - 46: Ii - i1IiiiI1iI
def oOoOo ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 71 - 71: Ii % i1iIi + oOo * I1ii11iIi11i % OOOo00oo0oO + I11i1ii1
def IiIi1 ( url ) :
 Oo00o000oOO = xbmc . Player ( ii1i1iiI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : Oo00o000oOO . play ( url ) . strip ( )
 except : pass
 if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + OoOo0o
def iI1IiiiIiI1Ii ( url ) :
 Oo00o000oOO = xbmc . Player ( )
 import urlresolver
 try : Oo00o000oOO . play ( url )
 except : pass
 if 28 - 28: oOo0O0Ooo
def II1i11i1iIi11 ( url ) :
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
  if 49 - 49: i1IiiiI1iI . ooo0O % OOOo00oo0oO / i1iIi
  if 95 - 95: o0o00Oo0O * iii1i1iiiiIi * I11i1ii1 . oOOoOooOo / iI11I1II1I1I
  if 28 - 28: I11i1ii1 + OOOo00oo0oO - oOOoOooOo / iI11I1II1I1I - oOo0O0Ooo
def iI111i1I1II ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' ]
  if 45 - 45: o0o00Oo0O / ooOoO0O00 * OOOo00oo0oO * oOo
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , I11iIi1i1II11 )
  if 35 - 35: oOoO0o00OO0 / iiiiiiii1 % oOo0O0Ooo + iI11I1II1I1I
  if 79 - 79: iii1i1iiiiIi / oOOoOooOo
  if 77 - 77: I1ii11iIi11i
  if 46 - 46: O0Oooo0O
  if iiI == 0 :
   o00OoooooooOo ( )
   if 32 - 32: ooo0O + oOo0O0Ooo . O0Oooo0O
   if 41 - 41: iii1i1iiiiIi . Ii / i1IiiiI1iI
   if 98 - 98: iii1i1iiiiIi % IIiIiII11i
   if 95 - 95: iI11I1II1I1I - O0Oooo0O - OoOo0o + O0Oooo0O % oOoO0o00OO0 . oOo0O0Ooo
 else :
  if 41 - 41: o0o00Oo0O + OOOo00oo0oO . ooOoO0O00 - IIiIiII11i * ooo0O . oOo
  if 68 - 68: ooo0O
  if 20 - 20: O0Oooo0O - O0Oooo0O
  if O0oo0OO0 . getSetting ( 'Cartoons' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , I1IIIii + 'Cartoons.png' , Oo00OOOOO , '' )
   if 37 - 37: I11i1ii1
   if 37 - 37: I1ii11iIi11i / I11i1ii1 * o0o00Oo0O
   if 73 - 73: iiiiiiii1 * iiiiiiii1 / oOOoOooOo
 iIiIi11 ( 'movies' , 'MAIN' )
def o0OoO000O ( ) :
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
 if 43 - 43: oOoO0o00OO0 . ooOoO0O00 . I11i1ii1 + o0o00Oo0O * i1iIi * o0o00Oo0O
 if 41 - 41: oOoO0o00OO0 + i1iIi % ii . oOoO0o00OO0 + iiiiiiii1 . iiiiiiii1
 if 31 - 31: Ii + IIiIiII11i . iiiiiiii1 * iii1i1iiiiIi
def I1I1i1I ( ) :
 oOOo0 = i11111IIIII ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 iI111i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oOOo0 )
 for OOooOoooOoOo in iI111i :
  OOooOoooOoOo = ( str ( OOooOoooOoOo ) )
  if os . path . exists ( xbmc . translatePath ( OOooOoooOoOo ) ) :
   OO0ooo0 = ( OOooOoooOoOo ) . replace ( 'special://home/addons/' , '' )
   OoOoO ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OO0ooo0 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iiI = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iiI == 0 :
    II1II1iI ( OOooOoooOoOo )
    OO0 ( )
   elif iiI == 1 :
    OooooO ( OOooOoooOoOo )
  else :
   pass
   if 92 - 92: ooo0O / ooo0O * i1iIi
def OooooO ( addon ) :
 OO0ooo0 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oO0 . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oO0 . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oO0 . close ( )
 if 19 - 19: i1iIi
def II1II1iI ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 O0o00oO0oOO = os . path . join ( IIIII , 'default.py' )
 iiiii1I1III1 = open ( O0o00oO0oOO , "w+" )
 if 12 - 12: iiiiiiii1 . iii1i1iiiiIi * oOo0O0Ooo
 iiiii1I1III1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 iiiii1I1III1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 iiiii1I1III1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 37 - 37: oOoO0o00OO0 * oOo0O0Ooo % Ii % ooOoO0O00 % I11i1ii1
 if 15 - 15: iI11I1II1I1I . o0o00Oo0O
 if 70 - 70: i1iIi . Ii % i1iIi . o0o00Oo0O - iI11I1II1I1I
 if 26 - 26: OoOo0o
def Oo0oOo000OoO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIii1I1i = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 I1iii11 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 iIIii = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 o00O0O = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 ii1iii1i = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url , IIII1iIIii , I1I1 , i11i1ii1I in IIii1I1i :
  if 'php' in url :
   o00oOOooOOo0o ( O000OOO , url , 90037 , IIII1iIIii , I1I1 , i11i1ii1I )
  elif O000OOO == 'Search' :
   o00oOOooOOo0o ( 'Search' , url , 90038 , IIII1iIIii , I1I1 , i11i1ii1I )
  else :
   O0O0ooOOO ( O000OOO , url , 222 , IIII1iIIii , I1I1 , i11i1ii1I )
 for O000OOO , Ii1IIiI1i , url , Iii in I1iii11 :
  o00oOOooOOo0o ( O000OOO , url , 90037 , Ii1IIiI1i , Iii , '' )
 for O000OOO , Ii1IIiI1i , url , Iii in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 90037 , Ii1IIiI1i , Iii , '' )
 for O000OOO , url , Ii1IIiI1i , Iii in IIi11i1i1iI1 :
  O0O0ooOOO ( O000OOO , url , 222 , Ii1IIiI1i , Iii , '' )
 for O000OOO , url , Ii1IIiI1i , Iii in iIIii :
  O0O0ooOOO ( O000OOO , url , 222 , Ii1IIiI1i , Iii , '' )
 for O000OOO , url , Ii1IIiI1i , Iii in o00O0O :
  O0O0ooOOO ( O000OOO , url , 222 , Ii1IIiI1i , Iii , '' )
 for O000OOO , url , Ii1IIiI1i in ii1iii1i :
  O0O0ooOOO ( O000OOO , url , 222 , Ii1IIiI1i , '' , '' )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
def OooooOo0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , Ii1IIiI1i , url , Iii in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 90037 , Ii1IIiI1i , Iii , '' )
 for O000OOO , url , Ii1IIiI1i , Iii in IIi11i1i1iI1 :
  O0O0ooOOO ( O000OOO , url , 222 , Ii1IIiI1i , Iii , '' )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
  if 45 - 45: I11i1ii1 / o0o00Oo0O / iii1i1iiiiIi * OoOo0o
def IiIIiiI ( ) :
 o0o0OO0o00o0O = [ 'serialsearch' , 'moviesearch' ]
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 if IIIiIiI == '' :
  pass
 else :
  for IIIIIIi1i in o0o0OO0o00o0O :
   iiiii11I1 = oOOoo00O0O + IIIIIIi1i + '.php'
   I11Ii1iI11iI1 = i11111IIIII ( iiiii11I1 )
   if I11Ii1iI11iI1 != 'Opened' :
    IIIii1I = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( I11Ii1iI11iI1 )
    for O000OOO , IIo0o0O0O00oOOo , IIII1iIIii , I1I1 , i11i1ii1I in IIIii1I :
     if IIIiIiI in O000OOO . lower ( ) :
      Ii1 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( oO0 ) )
      for iIIi in Ii1 :
       if iIIi == IIo0o0O0O00oOOo :
        O000OOO = '[COLORred]* [/COLOR]' + ( O000OOO ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        OOOoI1iI1IiI = open ( O0Oo000ooO00 , "a" )
        OOOoI1iI1IiI . write ( 'item="' + O000OOO + '"\n' )
        OOOoI1iI1IiI . close
      if 'php' in IIo0o0O0O00oOOo :
       o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 90037 , IIII1iIIii , I1I1 , i11i1ii1I )
      else :
       O0O0ooOOO ( O000OOO , IIo0o0O0O00oOOo , 222 , IIII1iIIii , I1I1 , i11i1ii1I )
       if 46 - 46: oOoO0o00OO0
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
   if 87 - 87: iii1i1iiiiIi % iI11I1II1I1I
def o0OO0OOO0O ( ) :
 if 36 - 36: Ii / iiiiiiii1 . i1IiiiI1iI + I11i1ii1 . o0o00Oo0O + oOo0O0Ooo
 if 36 - 36: ooOoO0O00 - oOoO0o00OO0 - O0Oooo0O
 if 7 - 7: Ii + oOo0O0Ooo
 if 47 - 47: O0Oooo0O - OoOo0o / oOOoOooOo - I1ii11iIi11i + iiiiiiii1 - iI11I1II1I1I
 if 68 - 68: i1iIi - OOOo00oo0oO + I1ii11iIi11i
 if 44 - 44: i1iIi * ooo0O * IIiIiII11i
 if 5 - 5: ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * o0o00Oo0O + iii1i1iiiiIi % ooOoO0O00
 if 80 - 80: iiiiiiii1 / ooo0O + oOo / OOOo00oo0oO
 if 46 - 46: Ii / I11i1ii1 % ooOoO0O00 - i1IiiiI1iI * iii1i1iiiiIi
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
 IIi = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 i1II1iII = requests . get ( 'http://www.djing.com/' ) . content
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( i1II1iII )
 OOO00OOo0o0Oo = IIi . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for ooooOoO0O in OOO00OOo0o0Oo :
  IIIIIIII = ooooOoO0O . findAll ( 'a' )
  for IIIi1I1IIii1II in IIIIIIII :
   if IIIi1I1IIii1II . has_attr ( 'href' ) :
    Oo0O0O000 = 'https://tvcatchup.com' + IIIi1I1IIii1II [ 'href' ]
   iI1I1I11IiII = IIIi1I1IIii1II . findAll ( 'img' )
   for iIii11iI1II in iI1I1I11IiII :
    Ii1IIiI1i = iIii11iI1II [ 'src' ]
    oo0O0o00 = iIii11iI1II [ 'alt' ]
   iI111i = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( IIIi1I1IIii1II ) )
   for I1ii1i in iI111i :
    iI1iiiIiii ( ( '[COLORgold]' + oo0O0o00 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + I1ii1i + '[/COLOR]' ) , Oo0O0O000 , 90024 , Ii1IIiI1i )
    if 22 - 22: OOOo00oo0oO * i1iIi * Ii + iiiiiiii1 * iii1i1iiiiIi * oOo
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in IIi11i1i1iI1 :
  if 'Submit' in O000OOO :
   pass
  elif '&lt;' in O000OOO :
   pass
  else :
   O0O0ooOOO ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 90025 , 'http://www.djing.com' + Ii1IIiI1i , Oo00OOOOO , '' )
   if 85 - 85: iiiiiiii1 * OoOo0o % I1ii11iIi11i - iiiiiiii1 - i1IiiiI1iI
 iIiIi11 ( 'movies' , 'MAIN' )
def iIOOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 if 32 - 32: ii
 iI111i = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( html )
 for O0000oO0o00 in iI111i :
  if not 'text' in O0000oO0o00 :
   oo000o = o0oOoO00o ( o0oOoO00o ( O0000oO0o00 ) )
   oo0 ( oo000o )
def OO00o0oOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<iframe src='([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  i1i1I1 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 46 - 46: i1IiiiI1iI . I11i1ii1 / IIiIiII11i % iI11I1II1I1I + I11i1ii1
def O0OOo ( ) :
 oOOo0 = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 i1I1Iiii1 = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for O0ooooo000 , OooOoOO0OO , I1iiIiiii1111 in i1I1Iiii1 :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O0ooooo000 + OooOoOO0OO + I1iiIiiii1111 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + IIo0o0O0O00oOOo , 10201 , I1IIIii + 'rated.png' )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'yr' in IIo0o0O0O00oOOo :
   IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + IIo0o0O0O00oOOo , 10201 , I1IIIii + 'rated.png' )
   if 29 - 29: i1iIi - oOo0O0Ooo / oOo0O0Ooo * i1iIi * I11i1ii1 . OoOo0o
def o0oOOoOOO ( ) :
 if 80 - 80: iI11I1II1I1I
 if 23 - 23: IIiIiII11i
 if 71 - 71: O0Oooo0O * I1ii11iIi11i . i1IiiiI1iI
 if 49 - 49: I11i1ii1 * o0o00Oo0O . I11i1ii1
 if 19 - 19: IIiIiII11i - I11i1ii1
 if 59 - 59: ooo0O * oOo - i1iIi . OoOo0o
 oOOo0 = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'yr' in IIo0o0O0O00oOOo :
   ii1ii111 ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + IIo0o0O0O00oOOo , 10201 , I1IIIii + 'rated.png' , '' , O000OOO , '' )
   if 89 - 89: OoOo0o
def o00oo0OO0 ( name , url , description ) :
 II1io0OO00oo = description
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
 for oO0o000OooOoo , url , name in iI111i :
  if 'id' in url :
   IIi11i = name
   ii1ii111 ( ( '[COLORred]RANK [COLORblue]' + oO0o000OooOoo + '[COLORred] - [COLORblue]' + name + '[/COLOR]' ) , name , 9110005 , I1IIIii + 'rated.png' , '' , II1io0OO00oo , IIi11i )
   if 86 - 86: i1iIi
   if 29 - 29: iI11I1II1I1I - oOo + oOo0O0Ooo % iI11I1II1I1I % OoOo0o
def O0OOO00 ( description , url ) :
 if 62 - 62: Ii + iii1i1iiiiIi + ooOoO0O00
 OOooo00 = ( str ( description ) )
 iI1 = ( str ( url ) )
 xbmc . log ( 'title:' + iI1 + '# year:' + OOooo00 , xbmc . LOGNOTICE )
 from imports import Scrape_Nan
 Scrape_Nan . scrape_movie ( iI1 , OOooo00 , '' )
 if 69 - 69: iii1i1iiiiIi
 if 63 - 63: oOo / iii1i1iiiiIi * iI11I1II1I1I . O0Oooo0O
 if 85 - 85: Ii / Ii . oOo . o0o00Oo0O
 if 67 - 67: IIiIiII11i / ooo0O . OoOo0o . ii
 if 19 - 19: I11i1ii1 . oOoO0o00OO0 / iii1i1iiiiIi
 if 68 - 68: oOOoOooOo / ii * i1IiiiI1iI / OOOo00oo0oO
 if 88 - 88: ooo0O
def iI11 ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 OO0O00O = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOooo = ( url )
 IIIiIiI = OOooo . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 I1i = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iiIiIIII1iiIIi = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1I1IiI1ii = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 O00OOoOOOO00O = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Ooo0OOO = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooooOoo0OO = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OOooo
 Oo0 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 O0000Oo00o = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 20 - 20: oOo . oOo0O0Ooo * Ii / Ii
 o00iIiiiII = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 71 - 71: iii1i1iiiiIi + iI11I1II1I1I * OOOo00oo0oO . O0Oooo0O % Ii % iI11I1II1I1I
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oOOo0 = i1Oo00 ( url )
 o0oO0 . update ( 0 , "" , "Checking Source 1/9 Links" )
 oo00O00oO = i1Oo00 ( I1i )
 o0oO0 . update ( 14 , "" , "Checking Source 2/9 Links" )
 iIiIIIi = i1Oo00 ( iiIiIIII1iiIIi )
 o0oO0 . update ( 28 , "" , "Checking Source 3/9 Links" )
 ooo00OOOooO = i1Oo00 ( i1I1IiI1ii )
 o0oO0 . update ( 40 , "" , "Checking Source 4/9 Links" )
 OooOO0oOOo0O = i1Oo00 ( O00OOoOOOO00O )
 o0oO0 . update ( 52 , "" , "Checking Source 5/9 Links" )
 I1II = i1Oo00 ( ooooOoo0OO )
 o0oO0 . update ( 64 , "" , "Checking Source 6/9 Links" )
 iIIi1Ii1III = i1Oo00 ( Oo0 )
 o0oO0 . update ( 76 , "" , "Checking Source 7/9 Links" )
 Oooo00 = i1Oo00 ( O0000Oo00o )
 o0oO0 . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 9 - 9: ii * o0o00Oo0O
 if 76 - 76: O0Oooo0O - OOOo00oo0oO . OoOo0o % ooo0O
 iIi11iiI11 = i1Oo00 ( o00iIiiiII )
 o0oO0 . update ( 100 , "" , "Checking Source 9/9 Links" )
 i1I111Ii = i1Oo00 ( Ii1I1 )
 if 31 - 31: oOo0O0Ooo
 if 73 - 73: oOOoOooOo . o0o00Oo0O / ooo0O - ii % Ii
 if 80 - 80: i1iIi / oOOoOooOo % o0o00Oo0O . I1ii11iIi11i
 if 63 - 63: OoOo0o . IIiIiII11i . i1IiiiI1iI
 if 46 - 46: oOOoOooOo % I11i1ii1 - ooo0O - I1ii11iIi11i - i1iIi / i1IiiiI1iI
 if 68 - 68: ooOoO0O00 - oOoO0o00OO0 / I1ii11iIi11i % i1IiiiI1iI . iiiiiiii1
 if 9 - 9: I11i1ii1
 if 48 - 48: ooo0O + ooo0O - I1ii11iIi11i
 if 27 - 27: oOo + iii1i1iiiiIi * oOOoOooOo
 if 83 - 83: iI11I1II1I1I
 if 72 - 72: i1IiiiI1iI
 if 87 - 87: ooOoO0O00
 if 48 - 48: I1ii11iIi11i * OOOo00oo0oO * iI11I1II1I1I + Ii - ii
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for url , O000OOO in II1iI :
   Ii1IiI1III11 = i1Oo00 ( url )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , iIIIiIi in I1IIII1i1 :
    iIIIiIi = ( iIIIiIi . replace ( '.' , ' ' ) )
    if IIIiIiI in iIIIiIi . lower ( ) :
     if '.mkv' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     elif '.mp4' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     elif '.avi' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     elif '.wav' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + oOO0 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
      if 90 - 90: I11i1ii1 - oOoO0o00OO0 % i1IiiiI1iI % iI11I1II1I1I - oOoO0o00OO0
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in IIi11i1i1iI1 :
   if OOooo in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 20 - 20: o0o00Oo0O - ii - I11i1ii1 + iI11I1II1I1I
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 94 - 94: i1iIi . ooOoO0O00
 if iIiIIIi != 'Failed' :
  iIIii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for O0OOo0o , O000OOO in iIIii :
   if OOooo in O000OOO . lower ( ) :
    IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiIiIIII1iiIIi + O0OOo0o ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Source 3 Links" )
 if ooo00OOOooO != 'Failed' :
  o00O0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in o00O0O :
   if OOooo in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 44 - 44: oOo0O0Ooo * iI11I1II1I1I / o0o00Oo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if OooOO0oOOo0O != 'Failed' :
  iiiIi = [ ]
  ii1iii1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OooOO0oOOo0O )
  for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in ii1iii1i :
   if OOooo in O000OOO . lower ( ) :
    if O000OOO in iiiIi :
     pass
    else :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , OO00OOoO0o , i1III1 , i11i1ii1I )
     iiiIi . append ( O000OOO )
     o0oO0 . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 36 , "" , "Getting Scooby Links" )
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if I1II != 'Failed' :
  ooOoO00 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( I1II )
  for url , Ii1IIiI1i , O000OOO in ooOoO00 :
   if OOooo in O000OOO . lower ( ) :
    IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , Ii1IIiI1i )
    o0oO0 . update ( 45 , "" , "Getting Snag Links" )
    if 62 - 62: o0o00Oo0O . I1ii11iIi11i
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: I1ii11iIi11i / iI11I1II1I1I % ooOoO0O00
    if 76 - 76: i1iIi + iI11I1II1I1I + iii1i1iiiiIi . oOo
    if 49 - 49: I11i1ii1 / oOOoOooOo / OoOo0o
    if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - oOOoOooOo
    if 38 - 38: ooo0O % O0Oooo0O + Ii + iiiiiiii1 + oOOoOooOo / Ii
    if 94 - 94: iiiiiiii1 - I1ii11iIi11i + OOOo00oo0oO
    if 59 - 59: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
    if 56 - 56: OOOo00oo0oO + oOOoOooOo
    if 32 - 32: IIiIiII11i + iii1i1iiiiIi % oOOoOooOo / iii1i1iiiiIi + oOoO0o00OO0
    if 2 - 2: Ii - O0Oooo0O + oOo % i1IiiiI1iI * i1iIi
    if 54 - 54: o0o00Oo0O - iiiiiiii1 . OoOo0o % iiiiiiii1 + iiiiiiii1
    if 36 - 36: OoOo0o % Ii
    if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * OOOo00oo0oO . i1IiiiI1iI / ooOoO0O00
    if 50 - 50: O0Oooo0O / ooOoO0O00 % ii
    if 83 - 83: oOoO0o00OO0 * oOoO0o00OO0 + OoOo0o
    if 57 - 57: o0o00Oo0O - o0o00Oo0O . oOoO0o00OO0 / ooo0O / i1iIi
    if 20 - 20: OoOo0o * IIiIiII11i - iii1i1iiiiIi - OOOo00oo0oO * O0Oooo0O
    if 6 - 6: oOOoOooOo + OoOo0o / I1ii11iIi11i + I11i1ii1 % IIiIiII11i / oOo
 if iIi11iiI11 != 'Failed' :
  iiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi11iiI11 )
  for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in iiIi :
   if OOooo in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Herovision Links" )
    if 74 - 74: o0o00Oo0O + ii / OOOo00oo0oO / iii1i1iiiiIi . oOoO0o00OO0 % OOOo00oo0oO
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: ooOoO0O00 . oOo0O0Ooo
    if 6 - 6: O0Oooo0O % OOOo00oo0oO % i1iIi
    if 63 - 63: o0o00Oo0O . oOo0O0Ooo . o0o00Oo0O * iI11I1II1I1I
    if 92 - 92: OOOo00oo0oO / OoOo0o . oOoO0o00OO0
    if 30 - 30: i1iIi . oOoO0o00OO0 / OoOo0o
    if 2 - 2: I11i1ii1 % oOo0O0Ooo - O0Oooo0O
    if 79 - 79: ii / oOoO0o00OO0 . o0o00Oo0O
    if 79 - 79: OOOo00oo0oO - IIiIiII11i
    if 43 - 43: ooOoO0O00 + o0o00Oo0O % oOo / i1iIi * oOo0O0Ooo
    if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + oOoO0o00OO0 . o0o00Oo0O % ooo0O
 Ooo00O0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 70 - 70: oOo0O0Ooo - oOOoOooOo - oOo - iii1i1iiiiIi . Ii % ooOoO0O00
 for IIIIIIi1i in Ooo00O0 :
  iiiii11I1 = Ii1iIiII1ii1 + IIIIIIi1i + OOOO
  Oooo00 = i1Oo00 ( iiiii11I1 )
  if Oooo00 != 'Failed' :
   II1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oooo00 )
   for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in II1iI :
    if OOooo in O000OOO . lower ( ) :
     O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
     if 1 - 1: OOOo00oo0oO / ooOoO0O00
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
     if 74 - 74: i1IiiiI1iI / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
 Ooo00O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 59 - 59: Ii . ii / i1IiiiI1iI * oOoO0o00OO0 + ii
 if 3 - 3: Ii * I1ii11iIi11i % iI11I1II1I1I % oOo0O0Ooo * iiiiiiii1 / OoOo0o
 for IIIIIIi1i in Ooo00O0 :
  iiiii11I1 = OO0O00O + IIIIIIi1i
  O00oo00oOOO0o = i1Oo00 ( iiiii11I1 )
  if O00oo00oOOO0o != 'Failed' :
   Iii1I1111ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O00oo00oOOO0o )
   for O0OOo0o , O000OOO in Iii1I1111ii :
    if OOooo in O000OOO . lower ( ) :
     iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OO0O00O + IIIIIIi1i + O0OOo0o ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 5 - 5: ooo0O / oOo0O0Ooo % i1iIi . I11i1ii1
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86: ooOoO0O00 * iii1i1iiiiIi . o0o00Oo0O - i1iIi - ooo0O - iii1i1iiiiIi
def IIioo0OO ( ) :
 IIII ( 'RUNNING' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , I1IIIii + 'running.png' )
 IIII ( 'COUNTDOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , I1IIIii + 'countdown.png' )
 IIII ( 'UNKNOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , I1IIIii + 'unknown.png' )
 IIII ( 'CANCELLED' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , I1IIIii + 'cancelled.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 47 - 47: OoOo0o + i1IiiiI1iI
def i1Iiii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , IiIiIi1I1 , o0O0O , oO00Ooo0oO , oOO in iI111i :
  IIII ( ( '[COLORblue]' + O000OOO + '[/COLOR] [COLORred]Season[/COLOR]-' + IiIiIi1I1 + ' [COLORred]Returns [/COLOR]- ' + oOO + ' ' + oO00Ooo0oO ) , O000OOO , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 59 - 59: oOo - oOo + iiiiiiii1
def iiIIII11iiii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , IiIiIi1I1 , o0O0O in iI111i :
  IIII ( ( '[COLORblue]' + O000OOO + '[/COLOR] [COLORred]Season[/COLOR]-' + IiIiIi1I1 + ' [COLORred] Status Unknown[/COLOR] ' ) , O000OOO , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 20 - 20: iiiiiiii1 / OoOo0o
def I1111ii11IIII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , IiIiIi1I1 , o0O0O , oO00Ooo0oO in iI111i :
  IIII ( ( '[COLORblue]' + O000OOO + ' [COLORred] Cancelled On[/COLOR] ' + oO00Ooo0oO ) , O000OOO , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 48 - 48: iI11I1II1I1I % ooOoO0O00 + iii1i1iiiiIi % ooo0O
def OO0oo00oOO ( url ) :
 OOooo = ( url )
 IIIiIiI = OOooo . lower ( )
 if 38 - 38: O0Oooo0O . iiiiiiii1 . oOo0O0Ooo * oOo
 if 69 - 69: ooo0O % Ii / i1iIi
 oOO0 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OOooo ) . replace ( ' ' , '+' )
 I1i = 'http://onlinemovies.tube/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 iiIiIIII1iiIIi = ( o0oOoO00o ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1I1IiI1ii = ( o0oOoO00o ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 Ooo0OOO = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 93 - 93: oOOoOooOo
 Oo0 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 O0000Oo00o = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 II11iIIii = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 57 - 57: o0o00Oo0O * oOoO0o00OO0 . Ii
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 69 - 69: o0o00Oo0O / IIiIiII11i * ooOoO0O00
 o0oO0 . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 66 - 66: o0o00Oo0O
 if 52 - 52: oOo * ii
 Ii11iiI = i1Oo00 ( oOO0 )
 o0oO0 . update ( 14 , "" , "Checking Source 3/11 Links" )
 oo00O00oO = i1Oo00 ( I1i )
 o0oO0 . update ( 28 , "" , "Checking Source 4/11 Links" )
 iIiIIIi = i1Oo00 ( iiIiIIII1iiIIi )
 o0oO0 . update ( 40 , "" , "Checking Source 5/11 Links" )
 ooo00OOOooO = i1Oo00 ( i1I1IiI1ii )
 o0oO0 . update ( 52 , "" , "Checking Source 6/11 Links" )
 O00oo00oOOO0o = i1Oo00 ( Ooo0OOO )
 o0oO0 . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 71 - 71: O0Oooo0O - ooo0O - OoOo0o
 if 28 - 28: iI11I1II1I1I
 iIIi1Ii1III = i1Oo00 ( Oo0 )
 o0oO0 . update ( 95 , "" , "Checking Source 9/11 Links" )
 Oooo00 = i1Oo00 ( O0000Oo00o )
 o0oO0 . update ( 97 , "" , "Checking Source 10/11 Links" )
 iI11II1i1I1 = i1Oo00 ( II11iIIii )
 o0oO0 . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 72 - 72: iiiiiiii1 - ii
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for url , O000OOO in II1iI :
   Ii1IiI1III11 = i1Oo00 ( url )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , iIIIiIi in I1IIII1i1 :
    if IIIiIiI in iIIIiIi . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , url + oOO0 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 25 - 25: iii1i1iiiiIi % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * OOOo00oo0oO
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iIIi1Ii1III != 'Failed' :
  I1iI1I1ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1Ii1III )
  for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in I1iI1I1ii1 :
   if IIIiIiI in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 10 , "" , "Getting Herovision Links" )
    if 33 - 33: ooo0O / o0o00Oo0O + OoOo0o
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 75 - 75: I11i1ii1 % Ii + iI11I1II1I1I
    if 92 - 92: iii1i1iiiiIi % o0o00Oo0O
    if 55 - 55: iI11I1II1I1I * iiiiiiii1
    if 85 - 85: iI11I1II1I1I . IIiIiII11i
    if 54 - 54: i1iIi . ii % I1ii11iIi11i
    if 22 - 22: OoOo0o
    if 22 - 22: iiiiiiii1 * i1IiiiI1iI - I1ii11iIi11i * o0o00Oo0O / Ii
    if 78 - 78: I1ii11iIi11i * o0o00Oo0O / oOOoOooOo + ii + OoOo0o
    if 23 - 23: iiiiiiii1 % ii / iI11I1II1I1I + oOoO0o00OO0 / ooOoO0O00 / ooo0O
    if 94 - 94: ooOoO0O00
    if 36 - 36: oOo0O0Ooo + I1ii11iIi11i
 if iI11II1i1I1 != 'Failed' :
  iIIiiiI1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI11II1i1I1 )
  for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in iIIiiiI1iI1 :
   if IIIiIiI in O000OOO . lower ( ) :
    IIII ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , OO00OOoO0o )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 30 , "" , "Getting RaizTv Links" )
    if 86 - 86: oOoO0o00OO0 * oOOoOooOo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  O0oO0o0OOOOOO = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for url , Ii1IIiI1i , O000OOO , IiI1i11IiIiii in IIi11i1i1iI1 :
   if IIIiIiI in O000OOO . lower ( ) :
    if 'season' in IiI1i11IiIiii :
     IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , Ii1IIiI1i , Ii1IIiI1i , '' )
    if 'episodes' in IiI1i11IiIiii :
     IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , Ii1IIiI1i , Ii1IIiI1i , '' )
  for url in O0oO0o0OOOOOO :
   IIII ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 4 - 4: O0Oooo0O - oOo0O0Ooo % OOOo00oo0oO / ooo0O % OOOo00oo0oO * IIiIiII11i
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if Ii11iiI != 'Failed' :
  I1iii11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( Ii11iiI )
  for url , O000OOO , Ii1IIiI1i in I1iii11 :
   if IIIiIiI in O000OOO . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( O000OOO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , Ii1IIiI1i , '' , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 45 , "" , "Getting Source iWatch Links" )
    if 3 - 3: ooOoO0O00 / O0Oooo0O - ooOoO0O00 - i1IiiiI1iI % I1ii11iIi11i - oOo0O0Ooo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: I11i1ii1
    if 7 - 7: iI11I1II1I1I - ooOoO0O00
    if 10 - 10: O0Oooo0O % o0o00Oo0O / oOo0O0Ooo % i1IiiiI1iI
    if 25 - 25: IIiIiII11i / oOo
    if 64 - 64: o0o00Oo0O % oOOoOooOo
    if 40 - 40: ooo0O + i1IiiiI1iI
    if 77 - 77: Ii % I11i1ii1 + O0Oooo0O % ii - i1IiiiI1iI
    if 26 - 26: I1ii11iIi11i + o0o00Oo0O - iI11I1II1I1I
    if 47 - 47: ii
 if iIiIIIi != 'Failed' :
  iIIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for O000OOO in iIIii :
   if IIIiIiI in O000OOO . lower ( ) :
    IIII ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iiIiIIII1iiIIi + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 2 - 2: iii1i1iiiiIi % O0Oooo0O * I1ii11iIi11i * iii1i1iiiiIi
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  o00O0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for O000OOO in o00O0O :
   if IIIiIiI in O000OOO . lower ( ) :
    IIII ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1I1IiI1ii + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 65 - 65: Ii + I1ii11iIi11i * ii - oOo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if O00oo00oOOO0o != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oo00oOOO0o )
  for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in Iii1I1111ii :
   if IIIiIiI in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 90 , "" , "Getting Scooby Links" )
    if 26 - 26: ooo0O % OoOo0o + OoOo0o % i1IiiiI1iI * Ii / iiiiiiii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 64 - 64: OOOo00oo0oO % iii1i1iiiiIi / IIiIiII11i % oOOoOooOo - iiiiiiii1
 I1II1IiI1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IIIIIIi1i in I1II1IiI1 :
  iiiii11I1 = Ii1iIiII1ii1 + IIIIIIi1i + OOOO
  iIi11iiI11 = i1Oo00 ( iiiii11I1 )
  if iIi11iiI11 != 'Failed' :
   iiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIi11iiI11 )
   for O000OOO , i11i1ii1I , url , Ii1IIiI1i , I1I1 , iIi1i in iiIi :
    if IIIiIiI in O000OOO . lower ( ) :
     o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] - Source Pandoras[/COLOR]' , url , iIi1i , Ii1IIiI1i , I1I1 , i11i1ii1I )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
     if 26 - 26: OoOo0o * I1ii11iIi11i
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
     if 31 - 31: i1IiiiI1iI * OOOo00oo0oO . i1iIi
     if 35 - 35: i1IiiiI1iI
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: oOOoOooOo / Ii % o0o00Oo0O
def O0oO0oo0O ( ) :
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']Adult Gallery[/COLOR]' , '[COLOR' + iiI1IiI + ']JizBox[/COLOR]' , '[COLOR' + iiI1IiI + ']Adult Channels[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  oooOOO0ooOoOOO ( )
 if iiI == 1 :
  o0IiIiI111IIII1 ( )
 if iiI == 2 :
  OOOoOooO000oO ( )
  if 87 - 87: iiiiiiii1 % I1ii11iIi11i
  if 62 - 62: oOo + oOOoOooOo / iiiiiiii1 * Ii
  if 37 - 37: iiiiiiii1
def oooOOO0ooOoOOO ( ) :
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']YOLOselfies[/COLOR]' , '[COLOR' + iiI1IiI + ']HotNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']MyNudeBabes[/COLOR]' , '[COLOR' + iiI1IiI + ']TeenNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']ADULTmeme[/COLOR]' , '[COLOR' + iiI1IiI + ']GIRLSmeme[/COLOR]' , ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  iIIiI1111 ( 'http://www.yoloselfie.com/' )
 if iiI == 1 :
  OooOO ( 'http://www.hotnudegirls.net/#nudegirls' )
 if iiI == 2 :
  O0o ( 'http://www.teennudegirls.com/' )
 if iiI == 3 :
  O0o ( 'http://www.teennudegirls.com/' )
 if iiI == 4 :
  OoOoOoo0OoO0 ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if iiI == 5 :
  OoOoOoo0OoO0 ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 17 - 17: i1iIi * IIiIiII11i / I11i1ii1 + iI11I1II1I1I . i1IiiiI1iI - o0o00Oo0O
def iIIiI1111 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 100111 , Ii1IIiI1i )
 for url in IIi11i1i1iI1 :
  IIII ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 100110 , Ii1IIiI1i )
def O0OOO00OOO00o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( oOOo0 )
 for url in iI111i :
  i11o00Ooo = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( i11o00Ooo )
  sys . exit ( 1 )
def OoOoOoo0OoO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , Ii1IIiI1i in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + Ii1IIiI1i , 100113 , 'http:' + Ii1IIiI1i )
 for url in IIi11i1i1iI1 :
  IIII ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http:' + url , 100112 , Ii1IIiI1i )
def OooOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , Ii1IIiI1i )
def OoO00OOoOOOo0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ii1IIiI1i in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , Ii1IIiI1i , 100113 , Ii1IIiI1i )
def oOoO00O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , Ii1IIiI1i )
def I11I1I1i1i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ii1IIiI1i in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , Ii1IIiI1i , 100113 , Ii1IIiI1i )
def O0o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , Ii1IIiI1i )
def Oo0oOO0O00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ii1IIiI1i in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , Ii1IIiI1i , 100113 , Ii1IIiI1i )
def o00OOo0o0O ( url ) :
 i11o00Ooo = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( i11o00Ooo )
 sys . exit ( 1 )
 if 14 - 14: iiiiiiii1 - i1IiiiI1iI * ii + OoOo0o . IIiIiII11i
def i1i1I11i1I ( ) :
 if 85 - 85: oOOoOooOo . o0o00Oo0O / OoOo0o * oOOoOooOo - oOo - Ii
 if 25 - 25: oOOoOooOo % I1ii11iIi11i - OoOo0o
 if 80 - 80: I11i1ii1 % IIiIiII11i - I1ii11iIi11i - iI11I1II1I1I
 if 9 - 9: ooo0O % oOoO0o00OO0 . oOoO0o00OO0
 if 28 - 28: ii % OOOo00oo0oO + oOoO0o00OO0 + o0o00Oo0O . O0Oooo0O
 if 80 - 80: Ii % oOoO0o00OO0
 if 54 - 54: ooo0O + i1IiiiI1iI - iI11I1II1I1I % oOOoOooOo % I11i1ii1
 if 19 - 19: oOoO0o00OO0 / iI11I1II1I1I % ooOoO0O00 . ii
 if 57 - 57: oOOoOooOo . I1ii11iIi11i - oOo - Ii * O0Oooo0O / ooo0O
 if 79 - 79: oOoO0o00OO0 + ooo0O % I1ii11iIi11i * ooo0O
 if 21 - 21: iiiiiiii1
 IIII ( 'SEASONS' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , I1IIIii + 'seasons.png' )
 IIII ( 'EPISODES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , I1IIIii + 'episodes.png' )
 IIII ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , I1IIIii + 'Search.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 24 - 24: iiiiiiii1 / oOOoOooOo
def ooOooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , O000OOO , ooIi111iII in iI111i :
  IIII ( ( O000OOO + ' - ' + ooIi111iII ) . replace ( '&amp;' , '&' ) , url , 90053 , I1IIIii + 'seasons.png' )
  if 83 - 83: ii + oOo * OOOo00oo0oO . o0o00Oo0O
def iiIIIi1i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  IIII ( O000OOO , url , 90054 , I1IIIii + 'episodes.png' )
  if 1 - 1: I1ii11iIi11i * O0Oooo0O . ii
def oOO00OO0o0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for Ii1IIiI1i , O000OOO , url in iI111i :
  IIII ( O000OOO , url , 90054 , Ii1IIiI1i )
 for url in next :
  IIII ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 35 - 35: ooo0O * iiiiiiii1 - iI11I1II1I1I + ooo0O . ii
def ii111iI1i1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for Ii1IIiI1i , ooIi111iII , url , O000OOO , OO000 in iI111i :
  o00oOOooOOo0o ( ooIi111iII + ' - ' + O000OOO + ' - ' + OO000 , url , 90044 , Ii1IIiI1i , Ii1IIiI1i , '' )
 for Ii1IIiI1i , O000OOO , url in IIi11i1i1iI1 :
  IIII ( O000OOO , url , 90044 , Ii1IIiI1i , Ii1IIiI1i , '' )
 for url in next :
  IIII ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 31 - 31: oOo * o0o00Oo0O / i1IiiiI1iI . ii * i1IiiiI1iI . oOoO0o00OO0
def III1II111II11 ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'http://onlinemovies.tube/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 IIIiIiI = O0OO . lower ( )
 oOOo0 = i11111IIIII ( IIIiIiI )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO , IiI1i11IiIiii in iI111i :
  if 'season' in IiI1i11IiIiii :
   IIII ( O000OOO , IIo0o0O0O00oOOo , 90054 , Ii1IIiI1i , Ii1IIiI1i , '' )
  if 'episodes' in IiI1i11IiIiii :
   IIII ( O000OOO , IIo0o0O0O00oOOo , 90044 , Ii1IIiI1i , Ii1IIiI1i , '' )
 for IIo0o0O0O00oOOo in next :
  IIII ( 'NEXT' , IIo0o0O0O00oOOo , 90053 , I1IIIii + 'Next.png' )
  if 72 - 72: ooOoO0O00 % oOOoOooOo % I11i1ii1 % OOOo00oo0oO - OOOo00oo0oO
def OOoo0O0OOOo0 ( ) :
 if 25 - 25: iI11I1II1I1I % IIiIiII11i / i1IiiiI1iI / oOoO0o00OO0
 if 22 - 22: OOOo00oo0oO * iiiiiiii1
 if 4 - 4: iii1i1iiiiIi - OOOo00oo0oO + oOo0O0Ooo
 if 36 - 36: I11i1ii1
 if 19 - 19: iii1i1iiiiIi . ooo0O . ii
 if 13 - 13: OoOo0o . I1ii11iIi11i / IIiIiII11i
 if 43 - 43: iI11I1II1I1I % oOo
 if 84 - 84: I1ii11iIi11i
 if 44 - 44: ii * Ii / I1ii11iIi11i
 if 75 - 75: ii . OoOo0o + oOo / i1iIi - oOo0O0Ooo % i1iIi
 IIII ( 'ALL MOVIES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , I1IIIii + 'allmov.png' )
 IIII ( 'GENRE' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , I1IIIii + 'Genre.png' )
 IIII ( 'BY YEAR' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , I1IIIii + 'Years.png' )
 IIII ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , I1IIIii + 'Search.png' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 89 - 89: iiiiiiii1 * iI11I1II1I1I + Ii . ii
def O0O0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , O000OOO , ooIi111iII in iI111i :
  if 'genre' in url :
   IIII ( ( O000OOO + ' - ' + ooIi111iII ) . replace ( '&amp;' , '&' ) , url , 90043 , I1IIIii + 'Genre.png' )
   if 74 - 74: iii1i1iiiiIi / ooOoO0O00 % ii
def o00o0o000Oo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if 'release' in url :
   IIII ( O000OOO , url , 90043 , I1IIIii + 'Years.png' )
   if 100 - 100: ooOoO0O00 - Ii . O0Oooo0O * oOo
def oOIIII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for Ii1IIiI1i , O000OOO , ooOOo , url , i11i1ii1I in iI111i :
  o00oOOooOOo0o ( O000OOO + ' ' + ooOOo , url , 90044 , Ii1IIiI1i , Ii1IIiI1i , i11i1ii1I )
 for Ii1IIiI1i , O000OOO , IiI1i11IiIiii , url , i1iii1IiiiI1i1 , i11i1ii1I in IIi11i1i1iI1 :
  if 'movies' in IiI1i11IiIiii :
   o00oOOooOOo0o ( O000OOO + ' - ' + i1iii1IiiiI1i1 , url , 90044 , Ii1IIiI1i , Ii1IIiI1i , i11i1ii1I )
 for url in next :
  IIII ( 'NEXT' , url , 90043 , I1IIIii + 'Next.png' )
  if 37 - 37: I1ii11iIi11i - ooOoO0O00 - I11i1ii1 + i1IiiiI1iI . iI11I1II1I1I
def Oo00oOO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  Iio0000O00oO0O ( 'http:' + url )
  if 3 - 3: iI11I1II1I1I % oOoO0o00OO0 . OoOo0o % i1IiiiI1iI
def Iio0000O00oO0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( ( O000OOO ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , I1IIIii + 'movhub.png' )
def I1i1I1Iiiii1 ( ) :
 if 88 - 88: i1IiiiI1iI + oOo0O0Ooo - i1IiiiI1iI / ii - Ii
 if 24 - 24: iI11I1II1I1I
 if 89 - 89: i1iIi / ooOoO0O00 - ooo0O % oOo0O0Ooo . I1ii11iIi11i - o0o00Oo0O
 if 71 - 71: oOo % oOo0O0Ooo - iiiiiiii1 . iiiiiiii1
 if 22 - 22: oOOoOooOo / oOOoOooOo - i1iIi % i1IiiiI1iI . OoOo0o + I11i1ii1
 if 64 - 64: ooOoO0O00 % oOoO0o00OO0 / i1iIi % ii
 if 24 - 24: O0Oooo0O + ii . I11i1ii1 / iii1i1iiiiIi / i1IiiiI1iI
 if 65 - 65: ii
 if 18 - 18: o0o00Oo0O - ooOoO0O00 . O0Oooo0O
 if 98 - 98: ooo0O
 if 73 - 73: I1ii11iIi11i - iiiiiiii1 . OOOo00oo0oO % ooOoO0O00 . o0o00Oo0O
 if 15 - 15: oOOoOooOo . iI11I1II1I1I * oOo0O0Ooo % i1IiiiI1iI
 if 21 - 21: oOo - oOo0O0Ooo . ii
 if 6 - 6: iI11I1II1I1I - iI11I1II1I1I % ooo0O / iI11I1II1I1I * O0Oooo0O
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'http://onlinemovies.tube/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 IIIiIiI = O0OO . lower ( )
 oOOo0 = i11111IIIII ( IIIiIiI )
 iI111i = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO , iIi in iI111i :
  if 'movies' in iIi :
   IIII ( iIi + '-' + O000OOO , IIo0o0O0O00oOOo , 90044 , Ii1IIiI1i )
 for IIo0o0O0O00oOOo in next :
  oOIIII ( IIo0o0O0O00oOOo )
  if 88 - 88: iiiiiiii1 * ii . iI11I1II1I1I
def iiI1i11II ( ) :
 IIII ( 'Search' , '' , 80008 , I1IIIii + 'Search.png' )
 oOOo0 = i11111IIIII ( 'http://www.join4films.com/' )
 iI111i = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( O000OOO , IIo0o0O0O00oOOo , 80006 , I1IIIii + 'Desi.png' )
def IIi111 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oOOo0 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  iI1iiiIiii ( O000OOO , url , 80007 , Ii1IIiI1i )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  IIII ( 'Next' , url , 80006 , I1IIIii + 'Next.png' )
def oO0o0o0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  url = ( url ) . replace ( ' ' , '%20' )
  oo0 ( url )
def I111ii1iI ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'http://www.join4films.com/?s=' + ( OOooo ) . replace ( ' ' , '+' ) + '&search_type=1'
 IIIiIiI = O0OO . lower ( )
 IIi111 ( IIIiIiI )
 if 33 - 33: i1iIi % o0o00Oo0O + oOoO0o00OO0
 if 96 - 96: oOOoOooOo . ii
 if 39 - 39: OoOo0o + oOo
 if 80 - 80: OoOo0o % oOo / iii1i1iiiiIi
 if 54 - 54: I1ii11iIi11i % oOo - OoOo0o - i1IiiiI1iI
 if 71 - 71: oOOoOooOo . Ii
 if 56 - 56: o0o00Oo0O * iiiiiiii1 + iiiiiiii1 * iI11I1II1I1I / oOOoOooOo * O0Oooo0O
 if 25 - 25: iI11I1II1I1I . i1IiiiI1iI * Ii + I1ii11iIi11i * i1IiiiI1iI
 if 67 - 67: iiiiiiii1
 if 88 - 88: I1ii11iIi11i
 if 8 - 8: oOoO0o00OO0
 if 82 - 82: ii
 if 75 - 75: IIiIiII11i % oOo0O0Ooo + OoOo0o % ii / I11i1ii1
 if 4 - 4: Ii - OoOo0o % oOoO0o00OO0 * O0Oooo0O % ooo0O
 if 71 - 71: oOOoOooOo . oOOoOooOo - iI11I1II1I1I
 if 22 - 22: ii / oOoO0o00OO0 % iiiiiiii1 * iii1i1iiiiIi
 if 32 - 32: ii % OOOo00oo0oO % iI11I1II1I1I / o0o00Oo0O
def Ooo0oOOoo0O ( ) :
 o00oOOooOOo0o ( 'Genre' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Most Viewed' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Box Office' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Search' , '' , 10078 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 if 57 - 57: oOo0O0Ooo . Ii * IIiIiII11i + ii + i1iIi
def OoO0o0oOOO ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'http://imoviemax.se/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 IIIiIiI = O0OO . lower ( )
 oO0I1I1i1I1I1I1 ( IIIiIiI )
def iI11IiIiiII1 ( url ) :
 I11iii1i = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oOOo0 )
 for url , O000OOO , ii1i1Iii in iI111i :
  if O000OOO in I11iii1i :
   pass
  else :
   o00oOOooOOo0o ( O000OOO + ' - ' + ii1i1Iii + ' Films' , url , 10074 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
   I11iii1i . append ( O000OOO )
   if 57 - 57: I11i1ii1
def IiI11I1Ii11II ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , oo0ooOoOOoO in iI111i :
  o00oOOooOOo0o ( O000OOO + ' - Views:' + oo0ooOoOOoO , url , 10075 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
  if 65 - 65: o0o00Oo0O + O0Oooo0O % i1iIi * oOo0O0Ooo / oOOoOooOo / iii1i1iiiiIi
  if 71 - 71: Ii / iii1i1iiiiIi . OOOo00oo0oO
def oO0I1I1i1I1I1I1 ( url ) :
 iI1IIIi11 = [ ]
 oOOo0 = i11111IIIII ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oOOo0 )
 for next in next :
  o00oOOooOOo0o ( 'NEXT PAGE' , next , 10074 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , O000OOO , url in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 10075 , Ii1IIiI1i , Ii1IIiI1i , '' )
  iI1IIIi11 . append ( O000OOO )
  if 69 - 69: o0o00Oo0O - o0o00Oo0O
def i1I1i1i1I1 ( img , name , url ) :
 img = img
 name = name
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oOOo0 )
 for iI1i1I1 , url in iI111i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iIi1Ii1111i = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iIi1Ii1111i
  i1iooO0oO0o = ( iI1i1I1 ) . replace ( 'play-' , 'Server ' )
  O0O0ooOOO ( i1iooO0oO0o , iIi1Ii1111i , 10076 , img , img , '' )
  if 22 - 22: ooo0O + I1ii11iIi11i . oOOoOooOo + oOoO0o00OO0 * iiiiiiii1 . Ii
def O0OOOOOO0ooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oOOo0 )
 for I1i in iI111i :
  if '=m' in I1i :
   II11IiI1 ( I1i )
  elif 'php' in I1i :
   O0OOOOOO0ooO ( url )
  else :
   oOOo0 = i11111IIIII ( I1i )
   iI111i = re . compile ( 'content="([^"]*)">' ) . findall ( oOOo0 )
   for iiIiIIII1iiIIi in iI111i :
    II11IiI1 ( I1i )
    if 86 - 86: iI11I1II1I1I % OOOo00oo0oO - iii1i1iiiiIi + O0Oooo0O % oOo . oOoO0o00OO0
    if 4 - 4: ooOoO0O00 + iii1i1iiiiIi
    if 39 - 39: iI11I1II1I1I + oOOoOooOo
def o00oOoo0o00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iIiiI11II11i = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for oO00Ooo0oO , o00OoO0o0 in iIiiI11II11i :
  print 'there ><><><><><><><><><><><><'
  oO00Ooo0oO = oO00Ooo0oO
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o00OoO0o0 ) )
  for O000OOO , IiI1ii1Ii in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + oO00Ooo0oO + '[/COLOR] - ' + O000OOO + ' - [COLOR' + iiI1IiI + ']' + IiI1ii1Ii + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
 ooO0oOo0o = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for oO00Ooo0oO , o0OOOoO0ooOOOo0 in ooO0oOo0o :
  print 'there ><><><><><><><><><><><><'
  oO00Ooo0oO = oO00Ooo0oO
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0OOOoO0ooOOOo0 ) )
  for O000OOO , IiI1ii1Ii in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + oO00Ooo0oO + '[/COLOR] - ' + O000OOO + ' - [COLOR' + iiI1IiI + ']' + IiI1ii1Ii + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
   if 93 - 93: I1ii11iIi11i
   if 75 - 75: iii1i1iiiiIi
   if 64 - 64: I11i1ii1 / ooo0O / ooOoO0O00
def OOo0OOOoOOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 ooO0oOo0o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
 for ooO0oOo0o in ooO0oOo0o :
  O000OOO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ooO0oOo0o ) )
  for O000OOO in O000OOO :
   O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ooO0oOo0o ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  oo0O0oO0O0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ooO0oOo0o ) )
  for oo0O0oO0O0O in oo0O0oO0O0O :
   oo0O0oO0O0O = 'http:' + oo0O0oO0O0O
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O , '' , '' )
  if 29 - 29: iii1i1iiiiIi . iiiiiiii1 + iii1i1iiiiIi + o0o00Oo0O . o0o00Oo0O * OoOo0o
  if 38 - 38: iiiiiiii1 * ii
  if 2 - 2: OOOo00oo0oO - Ii
  if 98 - 98: OOOo00oo0oO + ii - O0Oooo0O % Ii / ooo0O . ii
def II11 ( url ) :
 if 87 - 87: ooOoO0O00
 i1iI1IIi1I = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , Ii1IIiI1i , O000OOO , oo00i1i11I1I1 in iI111i :
  O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  oo00O00oO = i11111IIIII ( I1i )
  IIi11i1i1iI1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( oo00O00oO )
  for Ii11Iii , oO0O0oO0 in IIi11i1i1iI1 :
   OOOOOoooO = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oO0O0oO0 ) )
   for i11i1ii1I in OOOOOoooO :
    if O000OOO in i1iI1IIi1I :
     pass
    else :
     O0O0ooOOO ( O000OOO , Ii11Iii , 8043 , Ii1IIiI1i , Ii1IIiI1i , i11i1ii1I )
     iIiIi11 ( 'movies' , 'INFO' )
     i1iI1IIi1I . append ( O000OOO )
     if 59 - 59: OOOo00oo0oO % oOOoOooOo
     if 36 - 36: ii
def IiII1i ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi )
 for url , OO00OOoO0o , i11i1ii1I , I1I1 , O000OOO in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 10065 , OO00OOoO0o , I1I1 , i11i1ii1I )
 iIiIi11 ( 'movies' , 'INFO' )
 if 32 - 32: oOo0O0Ooo
def IIIIIiiI11i1 ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'https://www.youtube.com/results?search_query=' + ( OOooo ) . replace ( ' ' , '+' )
 IIIiIiI = O0OO . lower ( )
 oOOo0 = i11111IIIII ( IIIiIiI )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in next :
  IIo0o0O0O00oOOo = 'https://www.youtube.com' + IIo0o0O0O00oOOo
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , IIo0o0O0O00oOOo , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for Ii1IIiI1i , IIo0o0O0O00oOOo , O000OOO , Iii1I , oO0O0oO0 in iI111i :
  iiiiiIIii . append ( O000OOO )
  iIiIi11 ( 'tvshows' , 'INFO' )
  oo0O0oO0O0O = 'http:' + ( Ii1IIiI1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oo0O0oO0O0O
  IIo0o0O0O00oOOo = 'http://www.youtube.com' + IIo0o0O0O00oOOo
  O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O , oo0O0oO0O0O , oO0O0oO0 )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for Ii1IIiI1i , IIo0o0O0O00oOOo , O000OOO , Iii1I in iI111i :
   print 'im doing it'
   iIiIi11 ( 'tvshows' , 'INFO' )
   oo0O0oO0O0O = 'http:' + ( Ii1IIiI1i ) . replace ( 'https:' , '' )
   IIo0o0O0O00oOOo = 'http://www.youtube.com' + IIo0o0O0O00oOOo
   if '&' in IIo0o0O0O00oOOo :
    print ' i got here'
    oOOo0 = i11111IIIII ( IIo0o0O0O00oOOo )
    ooO0oOo0o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for ooO0oOo0o in ooO0oOo0o :
     O000OOO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ooO0oOo0o ) )
     for O000OOO in O000OOO :
      O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     IIo0o0O0O00oOOo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ooO0oOo0o ) )
     for IIo0o0O0O00oOOo in IIo0o0O0O00oOOo :
      IIo0o0O0O00oOOo = 'https://www.youtube.com/w' + IIo0o0O0O00oOOo
     oo0O0oO0O0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ooO0oOo0o ) )
     for oo0O0oO0O0O in oo0O0oO0O0O :
      oo0O0oO0O0O = 'http:' + oo0O0oO0O0O
     O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O , Oo00OOOOO , '' )
   elif O000OOO in iiiiiIIii :
    pass
   elif 'user' in IIo0o0O0O00oOOo or 'elete' in O000OOO :
    pass
   elif 'hannel' in IIo0o0O0O00oOOo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + IIo0o0O0O00oOOo
    oOOo0 = i11111IIIII ( IIo0o0O0O00oOOo )
    ooo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for Ii1IIiI1i , IIo0o0O0O00oOOo , O000OOO in ooo :
     if 'outube' in IIo0o0O0O00oOOo or 'list' in IIo0o0O0O00oOOo :
      pass
     elif 'atch' in IIo0o0O0O00oOOo :
      IIo0o0O0O00oOOo = ( IIo0o0O0O00oOOo ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + Ii1IIiI1i , 'http:' + Ii1IIiI1i , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O , oo0O0oO0O0O , '' )
    if 39 - 39: OOOo00oo0oO / oOOoOooOo * IIiIiII11i * iiiiiiii1
def IiIii11i1IIiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for url in next :
  url = 'https://www.youtube.com' + url
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for Ii1IIiI1i , url , O000OOO , Iii1I , oO0O0oO0 in iI111i :
  iiiiiIIii . append ( O000OOO )
  iIiIi11 ( 'tvshows' , 'INFO' )
  oo0O0oO0O0O = 'http:' + ( Ii1IIiI1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oo0O0oO0O0O
  url = 'http://www.youtube.com' + url
  O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O , oo0O0oO0O0O , oO0O0oO0 )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for Ii1IIiI1i , url , O000OOO , Iii1I in iI111i :
   iIiIi11 ( 'tvshows' , 'INFO' )
   oo0O0oO0O0O = 'http:' + ( Ii1IIiI1i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oOOo0 = i11111IIIII ( url )
    ooO0oOo0o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for ooO0oOo0o in ooO0oOo0o :
     O000OOO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ooO0oOo0o ) )
     for O000OOO in O000OOO :
      O000OOO = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ooO0oOo0o ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     oo0O0oO0O0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ooO0oOo0o ) )
     for oo0O0oO0O0O in oo0O0oO0O0O :
      oo0O0oO0O0O = 'http:' + oo0O0oO0O0O
     O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O , Oo00OOOOO , '' )
   elif O000OOO in iiiiiIIii :
    pass
   elif 'user' in url or 'elete' in O000OOO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oOOo0 = i11111IIIII ( url )
    ooo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for Ii1IIiI1i , url , O000OOO in ooo :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + Ii1IIiI1i , 'http:' + Ii1IIiI1i , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + Iii1I + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O , oo0O0oO0O0O , '' )
    if 40 - 40: iiiiiiii1 + iI11I1II1I1I * OOOo00oo0oO + Ii . Ii
    if 11 - 11: oOo % ii
    if 20 - 20: O0Oooo0O + O0Oooo0O * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
def OooOo ( ) :
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Setup Tv Guide[/COLOR]' , '' , 100212 , I1IIIii + 'linkchannels.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Open Guide[/COLOR]' , '' , 100213 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 if 87 - 87: oOOoOooOo * oOo + ooo0O . OoOo0o - oOOoOooOo
def Iiii ( ) :
 ivuesetup . iVueInt ( )
 if 56 - 56: i1IiiiI1iI - o0o00Oo0O / o0o00Oo0O * ooOoO0O00 . ii % iI11I1II1I1I
def I11iIiI1 ( ) :
 i1I1iiii1Ii11 ( )
 return
 if 25 - 25: Ii / iii1i1iiiiIi - O0Oooo0O / oOo . ooo0O . ooo0O
def i1I1iiii1Ii11 ( ) :
 if 6 - 6: OOOo00oo0oO . i1IiiiI1iI
 OOooOoooOoOo = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 iIIII1 = OOooOoooOoOo . getSetting ( id = 'User' )
 Oooo = OOooOoooOoOo . getSetting ( id = 'Pass' )
 iI1I = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 Iii1IiI1iI1I = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 IiiioO = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 ii11I = "http://piesustv" + Ooo + ":8000/get.php?username=" + iIIII1 + "&password=" + Oooo + "&type=m3u_plus&output=ts"
 Ooo0O00 = "http://piesustv" + Ooo + ":8000/xmltv.php?username=" + iIIII1 + "&password=" + Oooo + "&type=m3u_plus&output=ts"
 if 53 - 53: o0o00Oo0O . oOo0O0Ooo
 xbmc . executeJSONRPC ( iI1I )
 xbmc . executeJSONRPC ( Iii1IiI1iI1I )
 xbmc . executeJSONRPC ( IiiioO )
 if 74 - 74: oOOoOooOo % iii1i1iiiiIi / I1ii11iIi11i
 i1111Ii11i = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 i1111Ii11i . setSetting ( id = 'm3uUrl' , value = ii11I )
 i1111Ii11i . setSetting ( id = 'epgUrl' , value = Ooo0O00 )
 i1111Ii11i . setSetting ( id = 'm3uCache' , value = "false" )
 i1111Ii11i . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def OoOo00O0o ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 96 - 96: I11i1ii1 * I11i1ii1 % oOOoOooOo + ooo0O
if 27 - 27: I1ii11iIi11i * oOOoOooOo + Ii / oOo0O0Ooo - OOOo00oo0oO
if 44 - 44: i1iIi * oOOoOooOo / iii1i1iiiiIi
def o0Oo0ooo ( ) :
 if 60 - 60: oOo0O0Ooo
 if 44 - 44: IIiIiII11i . IIiIiII11i + OoOo0o * i1iIi
 if 16 - 16: IIiIiII11i
 if 100 - 100: o0o00Oo0O - ooOoO0O00
 if 48 - 48: OOOo00oo0oO % oOOoOooOo + o0o00Oo0O
 if 27 - 27: oOoO0o00OO0 / OoOo0o
 if 33 - 33: ii % oOoO0o00OO0 . o0o00Oo0O / oOoO0o00OO0
 if 63 - 63: I11i1ii1 + iI11I1II1I1I + oOo0O0Ooo + O0Oooo0O
 if 72 - 72: oOo + Ii + oOoO0o00OO0
 if 96 - 96: OOOo00oo0oO % ooOoO0O00 / ooo0O
 if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + iiiiiiii1
 if 88 - 88: o0o00Oo0O . OOOo00oo0oO % oOo0O0Ooo
 if OooO0 == "insert_username" :
  iii111i = iIi11ii1iI ( )
  oOiI1I = i111I1 ( )
  i1 ( 'User' , iii111i )
  i1 ( 'Pass' , oOiI1I )
  xbmc . executebuiltin ( 'Container.Refresh' )
  OOOo0Oo0O = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( iii111i , oOiI1I )
  OOOo0Oo0O = i11111IIIII ( OOOo0Oo0O )
  if OOOo0Oo0O == "" :
   i1I1I1iIIi = "[COLOR " + iiI1IiI + "]Incorrect Login Details[/COLOR]"
   IiOo00O0o0O = "[COLOR " + iiI1IiI + "]Please Re-enter[/COLOR]"
   O0OoOO = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , i1I1I1iIIi , IiOo00O0o0O , O0OoOO )
   o0Oo0ooo ( )
  else :
   i1I1I1iIIi = "[COLOR " + iiI1IiI + "]Login Successful[/COLOR]"
   IiOo00O0o0O = "[COLOR " + iiI1IiI + "]Welcome to GenieTv[/COLOR]"
   O0OoOO = ( '[COLOR ' + iiI1IiI + ']%s[/COLOR]' % iii111i )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , i1I1I1iIIi , IiOo00O0o0O , O0OoOO )
   xbmc . executebuiltin ( 'Container.Refresh' )
   o0o0oO0OOO ( )
 else :
  o0o0oO0OOO ( )
def iIi11ii1iI ( ) :
 O0Ooo0OOOo0oo = xbmc . Keyboard ( '' , 'heading' , True )
 O0Ooo0OOOo0oo . setHeading ( 'Enter Username' )
 O0Ooo0OOOo0oo . setHiddenInput ( False )
 O0Ooo0OOOo0oo . doModal ( )
 if ( O0Ooo0OOOo0oo . isConfirmed ( ) ) :
  I1111i1 = O0Ooo0OOOo0oo . getText ( )
  return I1111i1
 else :
  return False
  if 18 - 18: oOo % OOOo00oo0oO . iiiiiiii1 . i1iIi . iiiiiiii1 - O0Oooo0O
  if 33 - 33: oOOoOooOo + ii - oOo / ooOoO0O00 / ii
def i111I1 ( ) :
 O0Ooo0OOOo0oo = xbmc . Keyboard ( '' , 'heading' , True )
 O0Ooo0OOOo0oo . setHeading ( 'Enter Password' )
 O0Ooo0OOOo0oo . setHiddenInput ( False )
 O0Ooo0OOOo0oo . doModal ( )
 if ( O0Ooo0OOOo0oo . isConfirmed ( ) ) :
  I1111i1 = O0Ooo0OOOo0oo . getText ( )
  return I1111i1
 else :
  return False
def OOO0 ( ) :
 ii11I = "http://piesustv" + Ooo + ":8000//get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  IIIIii11II1I = urllib2 . urlopen ( ii11I )
  print IIIIii11II1I . getcode ( )
  IIIIii11II1I . close ( )
  if 48 - 48: oOoO0o00OO0 - o0o00Oo0O . oOo
  pass
  if 38 - 38: o0o00Oo0O
 except urllib2 . HTTPError , o00o :
  print o00o . getcode ( )
  iI111I11I1I1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + iiI1IiI + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + iiI1IiI + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def o0o0oO0OOO ( ) :
 Oo0O00O0O ( )
 if 79 - 79: ooOoO0O00 . OOOo00oo0oO
 if 34 - 34: O0Oooo0O * IIiIiII11i
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']My Account[/COLOR]' , 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii , 60004 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Guide Menu[/COLOR]' , '' , 100211 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CatchUp Tv[/COLOR]' , '' , 90026 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']VOD Lists[/COLOR]' , '' , 40000 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 71 - 71: I11i1ii1
 if 97 - 97: oOoO0o00OO0
 if 86 - 86: I1ii11iIi11i - OoOo0o . iii1i1iiiiIi . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
 if 34 - 34: ooo0O . O0Oooo0O % I11i1ii1 - o0o00Oo0O / O0Oooo0O
def Oo00OOoO0oo ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 IIi11ii11 = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii + '%26type%3Dm3u_plus%26output%3Dts'
 O0Oo00OOoO = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii
 OOOo0Oo0O = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=get_vod_categories'
 OOOo0Oo0O = i11111IIIII ( OOOo0Oo0O )
 if not OOOo0Oo0O == "" :
  OoOooO = 'https://tinyurl.com/create.php?source=indexpage&url=' + IIi11ii11 + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( OoOooO ) )
  I1I1i11iiiiI = 'https://tinyurl.com/create.php?source=indexpage&url=' + O0Oo00OOoO + '&submit=Make+TinyURL%21&alias='
  IIi11ii11 = i11111IIIII ( OoOooO )
  O0Oo00OOoO = i11111IIIII ( I1I1i11iiiiI )
  xbmc . log ( str ( O0Oo00OOoO ) )
  oOOoo = I1I1i11 ( IIi11ii11 , '<div class="indent"><b>' , '</b>' )
  oOo0Oo00O = I1I1i11 ( O0Oo00OOoO , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + iiI1IiI + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % oOOoo , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % oOo0Oo00O )
 else :
  return
def i1io0o00O ( ) :
 OOO0 ( )
 iiiI1ii ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOoooOooOOoO + '&action=get_vod_streams' , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( O0O0O0OO00oo )
 iI111i = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o00oOOooOOo0o ( ( '[COLORsteelblue]' + O000OOO + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIo0o0O0O00oOOo , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
def I11IIIIiI1 ( url ) :
 open = i11111IIIII ( o0oOOO + url )
 o00OoOooo = i1I1ii1 ( open , '<channel>' , '</channel>' )
 for iII1ii1 in o00OoOooo :
  if '<playlist_url>' in open :
   O000OOO = I1I1i11 ( iII1ii1 , '<title>' , '</title>' )
   oOO0 = I1I1i11 ( iII1ii1 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   o00oOOooOOo0o ( str ( base64 . b64decode ( O000OOO ) ) . replace ( '?' , '' ) , oOO0 , 40001 , icon , I1I1 , '' )
  else :
   if xbmcaddon . Addon ( ) . getSetting ( 'meta' ) == 'true' :
    try :
     O000OOO = I1I1i11 ( iII1ii1 , '<title>' , '</title>' )
     O000OOO = base64 . b64decode ( O000OOO )
     Iii1i = I1I1i11 ( iII1ii1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     url = I1I1i11 ( iII1ii1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     i11i1ii1I = I1I1i11 ( iII1ii1 , '<description>' , '</description>' )
     i11i1ii1I = base64 . b64decode ( i11i1ii1I )
     IiIIIIIIiI = I1I1i11 ( i11i1ii1I , 'PLOT:' , '\n' )
     ooOooo00O = I1I1i11 ( i11i1ii1I , 'CAST:' , '\n' )
     I1 = I1I1i11 ( i11i1ii1I , 'RATING:' , '\n' )
     OOooo00 = I1I1i11 ( i11i1ii1I , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
     OOooo00 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( OOooo00 )
     i1I1IIiIIi = I1I1i11 ( i11i1ii1I , 'DURATION_SECS:' , '\n' )
     iII1ii1IIII = I1I1i11 ( i11i1ii1I , 'GENRE:' , '\n' )
     Oo0o0O0OOOo0 ( str ( O000OOO ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , Iii1i , I1I1 , IiIIIIIIiI , str ( OOooo00 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( ooOooo00O ) . split ( ) , I1 , i1I1IIiIIi , iII1ii1IIII )
    except : pass
    xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   else :
    O000OOO = I1I1i11 ( iII1ii1 , '<title>' , '</title>' )
    O000OOO = base64 . b64decode ( O000OOO )
    Iii1i = I1I1i11 ( iII1ii1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    url = I1I1i11 ( iII1ii1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    i11i1ii1I = I1I1i11 ( iII1ii1 , '<description>' , '</description>' )
    O0O0ooOOO ( O000OOO , url , 222 , Iii1i , I1I1 , base64 . b64decode ( i11i1ii1I ) )
    if 4 - 4: oOOoOooOo + o0o00Oo0O . ooOoO0O00 * oOoO0o00OO0 - ooo0O
IIiIIIi1iii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
iii11III1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 61 - 61: oOoO0o00OO0 + iI11I1II1I1I % ooo0O
def ooooooO0O ( ) :
 ii11I = "http://piesustv" + Ooo + ":8000/get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  IIIIii11II1I = urllib2 . urlopen ( ii11I )
  print IIIIii11II1I . getcode ( )
  IIIIii11II1I . close ( )
  if 64 - 64: I11i1ii1 * iI11I1II1I1I . oOoO0o00OO0 / i1IiiiI1iI * iI11I1II1I1I
  pass
  if 4 - 4: oOOoOooOo % I11i1ii1 . O0Oooo0O
 except urllib2 . HTTPError , o00o :
  print o00o . getcode ( )
  iI111I11I1I1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 91 - 91: oOoO0o00OO0 + iI11I1II1I1I % I11i1ii1
 IIo0o0O0O00oOOo = "http://piesustv" + Ooo + ":8000/xmltv.php?username=%s&password=%s" % ( OooO0 , II11iiii1Ii )
 O0o0OOOO0 ( IIo0o0O0O00oOOo , iii11III1I + "uide.xml" )
 if 29 - 29: ii . O0Oooo0O % O0Oooo0O
 Iiii1iI1i = open ( IIiIIIi1iii1 , 'r+' )
 input = open ( IIiIIIi1iii1 ) . read ( ) . decode ( 'UTF-8' )
 IIIIIII1i = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 Iiii1iI1i . write ( IIIIIII1i )
 Iiii1iI1i . truncate ( )
 Iiii1iI1i . close ( )
 i1I1Iiii ( )
 if 15 - 15: oOOoOooOo % ooo0O / OOOo00oo0oO - IIiIiII11i . iI11I1II1I1I
def i1I1Iiii ( ) :
 open = i11111IIIII ( ii1111Iii11i )
 all = i1I1ii1 ( open , '{"num' , 'direct' )
 for iII1ii1 in all :
  if '"tv_archive":1' in iII1ii1 :
   O000OOO = I1I1i11 ( iII1ii1 , '"epg_channel_id":"' , '"' )
   Iii1i = I1I1i11 ( iII1ii1 , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = I1I1i11 ( iII1ii1 , 'stream_id":"' , '"' )
   O000OOO = O000OOO . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   o00oOOooOOo0o ( O000OOO , id , 90027 , Iii1i , I1I1 , O000OOO )
   if 91 - 91: i1iIi - iiiiiiii1 . ooOoO0O00 . oOoO0o00OO0 * ooo0O % iiiiiiii1
   if 30 - 30: i1IiiiI1iI
def oo000oO ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 oO0o00oo0 = open ( IIiIIIi1iii1 )
 IiIiII11i1 = ElementTree . parse ( oO0o00oo0 )
 Ii1I1iIiiI1 = "apples"
 import datetime as dt
 from datetime import time
 o00i111iiIiiIiI = datetime . now ( ) - timedelta ( days = 5 )
 oO00Ooo0oO = str ( o00i111iiIiiIiI )
 oOoOooOo0o0 = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 OOooooO = IiIiII11i1 . findall ( "programme" )
 for oOoo00 in OOooooO :
  if name in oOoo00 . attrib . get ( 'channel' ) :
   IIiIiI1I1IIiiI1 = oOoo00 . attrib . get ( 'start' )
   oooOOO0o0O0 , iiiI1IiI , Ii111IIIIii = IIiIiI1I1IIiiI1 . partition ( ' +' )
   oO00Ooo0oO = str ( oO00Ooo0oO ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   OOooo00 , O00o , oOO = IIiIiI1I1IIiiI1 . partition ( '2017' )
   Iii1iIIiii1ii = oOoo00 . find ( 'title' ) . text + IIiIiI1I1IIiiI1
   oOO = oOO [ : - 6 ]
   if oooOOO0o0O0 > oO00Ooo0oO :
    if oooOOO0o0O0 < oOoOooOo0o0 :
     Ii1iii11I = oooOOO0o0O0
     Ii1iii11I = Ii1iii11I [ : 4 ] + '/' + Ii1iii11I [ 4 : ]
     oooOOO0o0O0 = oooOOO0o0O0 [ : 4 ] + '-' + oooOOO0o0O0 [ 4 : ]
     Ii1iii11I = Ii1iii11I [ : 7 ] + '/' + Ii1iii11I [ 7 : ]
     oooOOO0o0O0 = oooOOO0o0O0 [ : 7 ] + '-' + oooOOO0o0O0 [ 7 : ]
     Ii1iii11I = Ii1iii11I [ : 10 ] + ' - ' + Ii1iii11I [ 10 : ]
     oooOOO0o0O0 = oooOOO0o0O0 [ : 10 ] + ':' + oooOOO0o0O0 [ 10 : ]
     Ii1iii11I = Ii1iii11I [ : 15 ] + ':' + Ii1iii11I [ 15 : ]
     oooOOO0o0O0 = oooOOO0o0O0 [ : 13 ] + '-' + oooOOO0o0O0 [ 13 : ]
     Ii1iii11I = Ii1iii11I [ : - 2 ]
     oooOOO0o0O0 = oooOOO0o0O0 [ : - 2 ]
     Ii11iIiiI = ( "http://piesustv" + Ooo + ":8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( oooOOO0o0O0 ) + "&duration=240" + "&stream=%s" ) % ( OooO0 , II11iiii1Ii , id )
     Ii1I1iIiiI1 = Ii11iIiiI + str ( oooOOO0o0O0 ) + "&duration=240"
     Ii1iii11I = '[COLOR blue]%s - [/COLOR]' % Ii1iii11I
     Iii1iIIiii1ii = str ( Ii1iii11I ) + oOoo00 . find ( 'title' ) . text
     i11i1ii1I = oOoo00 . find ( 'desc' ) . text
     O0O0ooOOO ( Iii1iIIiii1ii , Ii11iIiiI , 222 , I1IIIii + 'GTV.png' , Oo00OOOOO , i11i1ii1I )
def iiIIiII1IiiIIIIii ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OooO0 ) . replace ( 'PASSWORD' , II11iiii1Ii )
 IioO0O = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 IioO0O . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 IioO0O . setProperty ( 'IsPlayable' , 'true' )
 IioO0O . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IioO0O )
def O0o0OOOO0 ( url , dest ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oO0 . update ( 0 )
 oOOO = time . time ( )
 urllib . urlretrieve ( url , dest , lambda Iii1IiiII1Ii1 , iiiIIi , OOoOo0O00oo : oo0oO0oOo0O ( Iii1IiiII1Ii1 , iiiIIi , OOoOo0O00oo , o0oO0 , oOOO ) )
def oo0oO0oOo0O ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  OoOo00 = min ( numblocks * blocksize * 100 / filesize , 100 )
  OOoOoO = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  OO000o0oOoo0o = numblocks * blocksize / ( time . time ( ) - start_time )
  if OO000o0oOoo0o > 0 :
   IiiIiIIi = ( filesize - numblocks * blocksize ) / OO000o0oOoo0o
  else :
   IiiIiIIi = 0
  OO000o0oOoo0o = OO000o0oOoo0o / 1024
  O00Oo = OO000o0oOoo0o / 1024
  oOOoooo0O0 = float ( filesize ) / ( 1024 * 1024 )
  Ii111Ii11 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( OOoOoO )
  o00o = '[COLOR white]Speed:  %.02f Mb/s ' % O00Oo + '[/COLOR]'
  dp . update ( OoOo00 , Ii111Ii11 , o00o )
 except :
  OoOo00 = 100
  dp . update ( OoOo00 )
 if dp . iscanceled ( ) :
  Ii1II = xbmcgui . Dialog ( )
  Ii1II . ok ( "GenieTv" , 'The download was cancelled.' )
  if 44 - 44: ooo0O / oOoO0o00OO0 . I1ii11iIi11i + iii1i1iiiiIi
  sys . exit ( )
  dp . close ( )
  if 32 - 32: I11i1ii1 - oOOoOooOo * iiiiiiii1 * i1IiiiI1iI
def O00OOOo ( ) :
 if II11iiii1Ii == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  i1iI11Ii1i ( )
  if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . O0Oooo0O / OOOo00oo0oO
  if 4 - 4: Ii + OoOo0o
  if 26 - 26: iiiiiiii1 * O0Oooo0O * OOOo00oo0oO * iii1i1iiiiIi
  if 48 - 48: iiiiiiii1 % Ii . ii * I11i1ii1 % oOo . iiiiiiii1
  if 6 - 6: o0o00Oo0O . oOOoOooOo - OOOo00oo0oO / Ii
  if 84 - 84: i1IiiiI1iI / oOoO0o00OO0 * ooo0O * oOo * OoOo0o * o0o00Oo0O
  if 83 - 83: o0o00Oo0O % IIiIiII11i + ooo0O / ii
  if 75 - 75: IIiIiII11i . oOo0O0Ooo + OoOo0o - iii1i1iiiiIi - o0o00Oo0O . i1IiiiI1iI
def i1iI11Ii1i ( ) :
 IIIi1I1IIii1II = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( '"exp_date":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for IIo0o0O0O00oOOo in iI111i :
  dt = datetime . fromtimestamp ( float ( iI111i [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if oOoOooOo0o0 <= dt <= oOoOooOo0o0 + timedelta ( hours = 24 ) :
   iI111I11I1I1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + iiI1IiI + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + iiI1IiI + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + iiI1IiI + '] To Purchase A licence[/COLOR]' )
def I11iIi1i1I1i1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( '"username":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 iiiiii1ii1 = re . compile ( '"password":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 I1iii11 = re . compile ( '"status":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 IIi11i1i1iI1 = re . compile ( '"exp_date":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 iIIii = re . compile ( '"active_cons":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 o00O0O = re . compile ( '"created_at":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 ii1iii1i = re . compile ( '"max_connections":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 Iii1I1111ii = re . compile ( '"is_trial":"1"' ) . findall ( IIIi1I1IIii1II )
 ooOoO00 = re . compile ( '"is_trial":"0"' ) . findall ( IIIi1I1IIii1II )
 iIIII1i1 = I1I1oO00o0oOoo ( )
 oOOI1 = OOI1i ( )
 for url in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']My GTV Account Information[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in iiiiii1ii1 :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in I1iii11 :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in o00O0O :
  dt = datetime . fromtimestamp ( float ( o00O0O [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in IIi11i1i1iI1 :
  dt = datetime . fromtimestamp ( float ( IIi11i1i1iI1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if oOoOooOo0o0 <= dt <= oOoOooOo0o0 + timedelta ( hours = 24 ) :
   iI1iiiIiii ( '[COLORred]Expires Today[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in iIIii :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in ii1iii1i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in Iii1I1111ii :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] Yes' , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in ooOoO00 :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] No' , '' , '' , I1IIIii + 'MyAcc.png' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Get Short Links[/COLOR]' , '' , 100214 , I1IIIii + 'shortlinks.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local IP Address:[/COLOR] ' + iIIII1i1 , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']External IP Address:[/COLOR] ' + oOOI1 , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 47 - 47: iiiiiiii1 . iii1i1iiiiIi
 iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 58 - 58: iiiiiiii1 + I1ii11iIi11i / oOo0O0Ooo
def o000OO00OoO00 ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
 O00oIi11Iiii1iiii ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 10 - 10: iiiiiiii1 % I1ii11iIi11i
def i111111 ( data ) :
 o0oO0OOoO0OoO0 = len ( data ) % 4
 if 37 - 37: OOOo00oo0oO % O0Oooo0O % OOOo00oo0oO
 if 14 - 14: oOo / oOo0O0Ooo
 if 66 - 66: I1ii11iIi11i / Ii % oOOoOooOo
 if 43 - 43: OoOo0o
 if 84 - 84: OoOo0o . I11i1ii1 . iiiiiiii1
 if 2 - 2: I1ii11iIi11i - iii1i1iiiiIi
 if o0oO0OOoO0OoO0 != 0 :
  data += b'=' * ( 4 - o0oO0OOoO0OoO0 )
 return base64 . decodestring ( data )
def I1I1i11 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : I1iiII = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : I1iiII = ''
 else :
  try : I1iiII = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : I1iiII = ''
 return I1iiII
 if 81 - 81: iii1i1iiiiIi + ooo0O + I1ii11iIi11i
 if 79 - 79: I1ii11iIi11i - ii % O0Oooo0O + ii - i1IiiiI1iI % iii1i1iiiiIi
def i1I1ii1 ( text , start_with , end_with ) :
 I1iiII = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return I1iiII
def I1I1oO00o0oOoo ( ) :
 iII = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 iII . connect ( ( '8.8.8.8' , 0 ) )
 iII = iII . getsockname ( ) [ 0 ]
 return iII
 if 89 - 89: oOo0O0Ooo / iiiiiiii1 / ii - Ii + oOo0O0Ooo
def OOI1i ( ) :
 open = i11111IIIII ( 'http://canyouseeme.org/' )
 iIIII1i1 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( iIIII1i1 . group ( ) )
oOoooOooOOoO = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
ii1111Iii11i = 'http://piesustv' + Ooo + ':8000/panel_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
Oo0ooo = 'http://piesustv' + Ooo + ':8000/movie/%s/%s/' % ( OooO0 , II11iiii1Ii )
Oo00o00 = 'http://piesustv' + Ooo + ':8000/live/%s/%s/' % ( OooO0 , II11iiii1Ii )
OoOo0O0 = '&action=get_live_categories'
I1o0 = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OooO0 , II11iiii1Ii )
O0O0O0OO00oo = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OooO0 , II11iiii1Ii )
if 26 - 26: iiiiiiii1 * iI11I1II1I1I + IIiIiII11i / oOo0O0Ooo
o0oOOO = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OooO0 , II11iiii1Ii )
O0OOo0o0O00oOo = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OooO0 , II11iiii1Ii )
iI1ii = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OooO0 , II11iiii1Ii )
iiOOoO0oOOO = "http://piesustv" + Ooo + ":8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OooO0 , II11iiii1Ii )
if 47 - 47: OoOo0o / IIiIiII11i % I11i1ii1 . OOOo00oo0oO * oOoO0o00OO0
def iIii1iIiII1i1 ( ) :
 OOO0 ( )
 open = i11111IIIII ( iI1ii )
 o00OoOooo = i1I1ii1 ( open , '<channel>' , '</channel>' )
 for iII1ii1 in o00OoOooo :
  O000OOO = I1I1i11 ( iII1ii1 , '<title>' , '</title>' )
  O000OOO = base64 . b64decode ( O000OOO )
  oOO0 = I1I1i11 ( iII1ii1 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o00oOOooOOo0o ( '[COLORsteelblue]' + O000OOO + '[/COLOR]' , oOO0 , 60003 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
  if 56 - 56: O0Oooo0O / OOOo00oo0oO . iiiiiiii1
def iIii11II1IIiI ( url ) :
 open = i11111IIIII ( iiOOoO0oOOO + url )
 o00OoOooo = i1I1ii1 ( open , '<channel>' , '</channel>' )
 for iII1ii1 in o00OoOooo :
  O000OOO = I1I1i11 ( iII1ii1 , '<title>' , '</title>' )
  O000OOO = base64 . b64decode ( O000OOO )
  xbmc . log ( str ( O000OOO ) )
  Iii1i = I1I1i11 ( iII1ii1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  oOO0 = I1I1i11 ( iII1ii1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  i11i1ii1I = I1I1i11 ( iII1ii1 , '<description>' , '</description>' )
  i11i1ii1I = base64 . b64decode ( i11i1ii1I )
  I1iII1II1I1ii = '('
  oo0OO0O = ')'
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , oOO0 , 222 , Iii1i , I1I1 , ( '[COLOR' + iiI1IiI + ']' + i11i1ii1I + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( oo0OO0O , '[COLORsteelblue]' ) . replace ( I1iII1II1I1ii , '[COLORorangered]' ) )
  if 64 - 64: OOOo00oo0oO . oOoO0o00OO0 * O0Oooo0O % oOo0O0Ooo
def IiI11II ( url ) :
 url = url
 oOOo0 = i11111IIIII ( I1o0 + url )
 iI111i = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , type , I1i , IIII1iIIii in iI111i :
  iiIiIIII1iiIIi = ( Oo00o00 + I1i + '.m3u8' ) . strip ( )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , iiIiIIII1iiIIi , 222 , ( IIII1iIIii ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
def OO0Iii1iIiI111Ii ( url , name , img ) :
 img = img
 name = name
 url = url
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/xmltv.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oOOo0 )
 for iIIIiIi , ooO0oo0000oOo in iI111i :
  if name == iIIIiIi :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) + ooO0oo0000oOo , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def oOOoO0oO00O ( name ) :
 OOooo00oo = name
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oOOo0 )
 for name , Ii1IIiI1i , IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = ( IIo0o0O0O00oOOo ) . replace ( '.ts' , '.m3u8' )
  O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , Ii1IIiI1i , Ii1IIiI1i , '' )
 else :
  O0O0ooOOO ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 42 - 42: i1iIi * o0o00Oo0O / OOOo00oo0oO
  if 8 - 8: ooOoO0O00 + IIiIiII11i / i1iIi + oOoO0o00OO0 % i1iIi - iI11I1II1I1I
  if 29 - 29: I1ii11iIi11i + IIiIiII11i
  if 95 - 95: OOOo00oo0oO
  if 48 - 48: i1IiiiI1iI / iI11I1II1I1I % IIiIiII11i
  if 39 - 39: ooOoO0O00 . oOoO0o00OO0 / i1IiiiI1iI / i1IiiiI1iI
  if 100 - 100: ii - ii + I11i1ii1
  if 32 - 32: iii1i1iiiiIi * ooo0O / ii
  if 90 - 90: O0Oooo0O
  if 35 - 35: IIiIiII11i / i1iIi
  if 79 - 79: iii1i1iiiiIi + O0Oooo0O * iiiiiiii1 * i1iIi
  if 53 - 53: OoOo0o / I1ii11iIi11i
def o0oo0000OO ( ) :
 o00oOOooOOo0o ( 'Full Backup' , '' , 10061 , I1IIIii + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0OoO00oOO0o ) :
  o00oOOooOOo0o ( 'Backup Genie Favourites' , IIo0o0O0O00oOOo , 10062 , I1IIIii + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( ooOooo000oOO ) :
  o00oOOooOOo0o ( 'Backup Ivue Config' , ooOooo000oOO , 10062 , I1IIIii + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( Oo0oOOo ) :
  o00oOOooOOo0o ( 'Backup Kodi Favourites' , Oo0oOOo , 10062 , I1IIIii + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 10 - 10: oOoO0o00OO0 . ooo0O
  if 75 - 75: o0o00Oo0O * ooOoO0O00 - i1IiiiI1iI / OoOo0o % OoOo0o / iii1i1iiiiIi
  if 5 - 5: o0o00Oo0O - iiiiiiii1 / O0Oooo0O . ooo0O
zip = O0oo0OO0 . getSetting ( 'zip' )
iIII1iIii = xbmc . translatePath ( os . path . join ( zip ) )
def iiIII1i1 ( ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 78 - 78: OOOo00oo0oO % iii1i1iiiiIi
  if 1 - 1: iii1i1iiiiIi - ooo0O / oOOoOooOo - I11i1ii1 / ooOoO0O00
  if 28 - 28: oOo / O0Oooo0O * oOo0O0Ooo + oOOoOooOo
def iIIIIi11i ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0OoO00oOO0o
  elif 'Ivue' in name :
   url = ooOooo000oOO
  elif 'Kodi' in name :
   url = Oo0oOOo
  iiIII1i1 ( )
  oooOOoo0 = open ( url ) . read ( )
  Oo00O00o0 = os . path . join ( iIII1iIii , description . split ( 'Your ' ) [ 1 ] )
  Iiii1iI1i = open ( Oo00O00o0 , mode = 'w' )
  Iiii1iI1i . write ( oooOOoo0 )
  Iiii1iI1i . close ( )
 else :
  if 'guisettings.xml' in description :
   iII1ii1 = open ( os . path . join ( iIII1iIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I1iiII = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   iI111i = re . compile ( I1iiII ) . findall ( iII1ii1 )
   for type , IiII1 , iI1I1I in iI111i :
    iI1I1I = iI1I1I . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IiII1 , iI1I1I ) )
  else :
   Oo00O00o0 = os . path . join ( url )
   oooOOoo0 = open ( os . path . join ( iIII1iIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iiii1iI1i = open ( Oo00O00o0 , mode = 'w' )
   Iiii1iI1i . write ( oooOOoo0 )
   Iiii1iI1i . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 81 - 81: Ii % ooOoO0O00 % IIiIiII11i % oOo0O0Ooo + oOo0O0Ooo % oOoO0o00OO0
 if 20 - 20: I11i1ii1 - iI11I1II1I1I
 if 25 - 25: i1IiiiI1iI + iii1i1iiiiIi
 if 98 - 98: OoOo0o
def OoOOoOo ( ) :
 Ii1Iiiiii = 1
 iiIII1i1 ( )
 IiIii1i11i1 = xbmc . translatePath ( os . path . join ( iIII1iIii , 'Build Backup' , 'Full Backup' , '' ) )
 ooOOo00o0ooO = xbmc . translatePath ( os . path . join ( iIII1iIii , 'Build Backup' , 'my_full_backup.zip' ) )
 iIOO = xbmc . translatePath ( os . path . join ( iIII1iIii , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( IiIii1i11i1 ) :
  os . makedirs ( IiIii1i11i1 )
 I1III1I11I1 = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1III1I11I1 ) : return False , 0
 iI1 = I1III1I11I1
 oO000OoO00OoO = xbmc . translatePath ( os . path . join ( IiIii1i11i1 , iI1 + '.zip' ) )
 I1IiIi1iiI = [ 'plugin.video.GenieTv' ]
 iiII1II11i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 ooO0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OoooooOo0oOo0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 II11II = "Creating full backup of existing build"
 i1ii11III = "Creating Community Build"
 o00O = "Archiving..."
 ii1I1I1 = ""
 oo0oOOO0oOoo = "Please Wait"
 Ii1o0OOOoo0000 ( i1111 , oO000OoO00OoO , i1ii11III , o00O , ii1I1I1 , oo0oOOO0oOoo , ooO0 , OoooooOo0oOo0 )
 time . sleep ( 1 )
 IiIIii1i1i11iII = xbmc . translatePath ( os . path . join ( IiIii1i11i1 , iI1 + '_guisettings.zip' ) )
 o0II1 = zipfile . ZipFile ( IiIIii1i1i11iII , mode = 'w' )
 try :
  o0II1 . write ( xbmc . translatePath ( os . path . join ( i1111 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 o0II1 . close ( )
 if Ii1Iiiiii == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + ooOOo00o0ooO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + oO000OoO00OoO + '[/COLOR]' )
  if 86 - 86: OOOo00oo0oO . oOo0O0Ooo - O0Oooo0O + iI11I1II1I1I
def Ii1o0OOOoo0000 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0O00ooo0 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iI1iIi1 = len ( sourcefile )
 O00oOOO0 = [ ]
 Iiiiii = [ ]
 o0oO0 . create ( message_header , message1 , message2 , message3 )
 for oOOOOOoOOoo0 , oo0OOO0OOoOO , oOoO in os . walk ( sourcefile ) :
  for file in oOoO :
   Iiiiii . append ( file )
 II1i1 = len ( Iiiiii )
 for oOOOOOoOOoo0 , oo0OOO0OOoOO , oOoO in os . walk ( sourcefile ) :
  oo0OOO0OOoOO [ : ] = [ o0o0oo0OOo0O0 for o0o0oo0OOo0O0 in oo0OOO0OOoOO if o0o0oo0OOo0O0 not in exclude_dirs ]
  oOoO [ : ] = [ Iiii1iI1i for Iiii1iI1i in oOoO if Iiii1iI1i not in exclude_files ]
  for file in oOoO :
   O00oOOO0 . append ( file )
   iIIiiII11i1I1 = len ( O00oOOO0 ) / float ( II1i1 ) * 100
   o0oO0 . update ( int ( iIIiiII11i1I1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   Ii111Ii1iiIi1 = os . path . join ( oOOOOOoOOoo0 , file )
   if not 'temp' in oo0OOO0OOoOO :
    if not 'plugin.program.originwizard' in oo0OOO0OOoOO :
     import time
     OOI11i1IIi1i1 = '01/01/1980'
     I11i1iiiiIIIi = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Ii111Ii1iiIi1 ) ) )
     if I11i1iiiiIIIi > OOI11i1IIi1i1 :
      o0O00ooo0 . write ( Ii111Ii1iiIi1 , Ii111Ii1iiIi1 [ iI1iIi1 : ] )
 o0O00ooo0 . close ( )
 o0oO0 . close ( )
 if 13 - 13: o0o00Oo0O + O0Oooo0O * IIiIiII11i + I1ii11iIi11i * I11i1ii1
 if 12 - 12: I11i1ii1 - i1iIi % i1iIi
def iIII1I11II1i1 ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 if 28 - 28: oOo - iiiiiiii1
 if 99 - 99: iI11I1II1I1I
def oOOo00O ( ) :
 Oo0O00O0O ( )
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  O00OOooo0Ooo ( )
 if iiI == 1 :
  oOO0OOOOoooO ( )
 if iiI == 2 :
  o0OOO00O ( )
 if iiI == 3 :
  IIIIIiiI11i1 ( )
  if 12 - 12: OoOo0o + oOo * i1IiiiI1iI + i1iIi + I11i1ii1
  if 58 - 58: iiiiiiii1 * i1iIi - Ii % oOoO0o00OO0
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
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']RaysRavers Radio[/COLOR]' , '[COLOR' + iiI1IiI + ']ThunderStruck[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if iiI == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if iiI == 2 :
   IiiIiiiiI1III ( )
  if iiI == 3 :
   II111111 ( )
  if iiI == 4 :
   i1iI1i11iIi1 ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iiI == 5 :
   Oo0O00O ( )
  if iiI == 6 :
   OOoOOO0 ( ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iiI == 7 :
   IiI1i1i1 ( ( o0oOoO00o ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iiI == 8 :
   O0O000oOO0 ( str ( O00OOOoOoo0O ) + ( o0oOoO00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iiI == 9 :
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
OOOO0OOO = 'white'
i1i1ii = 'gold'
def oo0OoO ( ) :
 Oo0O00O0O ( )
 if oO00O0 ( True ) == False : I11iIiiI = 0
 else : I11iIiiI = O0O0Oo00 ( oO00O0 ( True ) , True , True )
 if oO00O0 ( True , True ) == False : OO000oo0o = 0
 else : OO000oo0o = O0O0Oo00 ( oO00O0 ( True , True ) , True , True )
 I11iiIiI1II11 = int ( I11iIiiI ) + int ( OO000oo0o )
 OOOoOOOo = str ( I11iiIiI1II11 ) + ' Error(s) Found' if I11iiIiI1II11 > 0 else 'None Found'
 oO0000 = ': [COLORsteelblue]Not Found[/COLOR]' if not os . path . exists ( Oo0o0000o0o0 ) else ": [COLORorangered]%s[/COLOR]" % OOO ( os . path . getsize ( Oo0o0000o0o0 ) )
 IIIIiiIi = ooooOOo ( oO )
 O0Oo0oO0OO0 = ooooOOo ( i1iiIIiiI111 )
 oo0o0 = OoO00o00 ( )
 ooOo = IIIIiiIi + O0Oo0oO0OO0 + oo0o0
 iIIII1i1 = I1I1oO00o0oOoo ( )
 oOOI1 = OOI1i ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAN UP:[COLORorangered] [B]%s[/B][/COLOR]' % OOO ( ooOo ) , 'url' , 9666 , I1IIIii + 'MAIN5.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , I1IIIii + 'KillKodi.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , I1IIIii + 'Speedtest.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG Errors:[COLORorangered] %s[/COLOR]' % ( OOOoOOOo ) , '' , 219999990 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR LOG FILES: [COLORorangered]' + oO0000 + '[/COLOR]' , '' , 219999991 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE CACHE:[COLORorangered] [B]%s[/B][/COLOR]' % OOO ( oo0o0 ) , 'url' , 14 , I1IIIii + 'DeleteCache.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE PACKAGES:[COLORorangered] [B]%s[/B][/COLOR]' % OOO ( IIIIiiIi ) , 'url' , 6 , I1IIIii + 'DeletePackages.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , 'url' , 10 , I1IIIii + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']LAST RESORT FIX EMPTY REPOS[/COLOR]' , 'url' , 9 , I1IIIii + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR THUBMNAILS:[COLORorangered] [B]%s[/B][/COLOR]' % OOO ( O0Oo0oO0OO0 ) , 'url' , 219999992 , I1IIIii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Local IP Address:[COLORorangered] ' + iIIII1i1 + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']External IP Address:[COLORorangered] ' + oOOI1 + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 93 - 93: O0Oooo0O % Ii
 if 25 - 25: oOOoOooOo % iiiiiiii1 * iiiiiiii1 + iI11I1II1I1I . ooOoO0O00
 iIiIi11 ( 'movies' , 'MAIN' )
def OO0Oo00 ( proc ) :
 xbmc . executebuiltin ( proc )
 if 28 - 28: oOo + O0Oooo0O / iii1i1iiiiIi % OOOo00oo0oO - I1ii11iIi11i
def ooOo0Ooo0 ( ) :
 OO0Oo00 ( 'Container.Refresh()' )
def IIIiIii111IIi ( ) :
 Iiii1iI1i = open ( Oo0o0000o0o0 , 'w' ) ; Iiii1iI1i . close ( ) ; o0OoOO ( "[COLOR %s]%s[/COLOR]" % ( OOOO0OOO , oOo0oooo00o ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % i1i1ii )
 ooOo0Ooo0 ( )
 if 100 - 100: ooOoO0O00 . ii % i1iIi
def oOoOo00oo ( type = None ) :
 II11IiIIiiiii = oooOOo0o0OOO ( 'Textures' )
 if not type == None : iiI = 1
 else : iiI = iI111I11I1I1 . yesno ( oOo0oooo00o , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( i1i1ii , II11IiIIiiiii ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if iiI == 1 :
  try : IiiiII ( os . join ( oooOOOOO , II11IiIIiiiii ) )
  except : OoO ( 'Failed to delete, Purging DB.' ) ; o00OoOO00 ( II11IiIIiiiii )
  oO0oOOoOo000O ( i1iiIIiiI111 )
  if 3 - 3: iii1i1iiiiIi . ooo0O % oOo / I1ii11iIi11i * O0Oooo0O
 else : OoO ( 'Clear thumbnames cancelled' )
 iIIIiI1iii ( )
 if 20 - 20: OOOo00oo0oO - ooo0O * oOo % ooOoO0O00 - iI11I1II1I1I . OoOo0o
 if 31 - 31: OOOo00oo0oO % ooOoO0O00 . ii - ooo0O + ii
def iIIIiI1iii ( ) :
 if not os . path . exists ( i1iiIIiiI111 ) : os . makedirs ( i1iiIIiiI111 )
 I1i1Ii = '0123456789abcdef'
 III1 = os . path . join ( i1iiIIiiI111 , 'Video' , 'Bookmarks' )
 for iIIi in I1i1Ii :
  I1I11 = os . path . join ( i1iiIIiiI111 , iIIi )
  if not os . path . exists ( I1I11 ) : os . makedirs ( I1I11 )
 if not os . path . exists ( III1 ) : os . makedirs ( III1 )
 if 68 - 68: Ii . o0o00Oo0O * oOo0O0Ooo * ooOoO0O00 * ii
def oooOOo0o0OOO ( DB ) :
 if DB in [ 'Addons' , 'ADSP' , 'Epg' , 'MyMusic' , 'MyVideos' , 'Textures' , 'TV' , 'ViewModes' ] :
  iI111i = glob . glob ( os . path . join ( oooOOOOO , '%s*.db' % DB ) )
  I1I1I1 = '%s(.+?).db' % DB [ 1 : ]
  i1iIIIiI = 0
  for file in iI111i :
   try : I11IiI1iII = int ( re . compile ( I1I1I1 ) . findall ( file ) [ 0 ] )
   except : I11IiI1iII = 0
   if i1iIIIiI < I11IiI1iII :
    i1iIIIiI = I11IiI1iII
  return '%s%s.db' % ( DB , i1iIIIiI )
 else : return False
 if 18 - 18: OoOo0o
def oO0oOOoOo000O ( path ) :
 OoO ( "Deleting Folder: %s" % path , xbmc . LOGNOTICE )
 try : shutil . rmtree ( path , ignore_errors = True , onerror = None )
 except : return False
 if 82 - 82: ii - oOOoOooOo * oOoO0o00OO0 * oOOoOooOo * o0o00Oo0O * iI11I1II1I1I
def o00OoOO00 ( name ) :
 if 31 - 31: oOOoOooOo . OoOo0o % oOOoOooOo
 if 33 - 33: o0o00Oo0O * i1iIi - I11i1ii1 . ii + I11i1ii1
 if 20 - 20: O0Oooo0O - iii1i1iiiiIi
 OoO ( 'Purging DB %s.' % name , xbmc . LOGNOTICE )
 if os . path . exists ( name ) :
  try :
   ooOO = database . connect ( name )
   IIiIi1I1iI1 = ooOO . cursor ( )
  except Exception , o00o :
   OoO ( "DB Connection Error: %s" % str ( o00o ) , xbmc . LOGERROR )
   return False
 else : OoO ( '%s not found.' % name , xbmc . LOGERROR ) ; return False
 IIiIi1I1iI1 . execute ( "SELECT name FROM sqlite_master WHERE type = 'table'" )
 for i1I111II11 in IIiIi1I1iI1 . fetchall ( ) :
  if i1I111II11 [ 0 ] == 'version' :
   OoO ( 'Data from table `%s` skipped.' % i1I111II11 [ 0 ] , xbmc . LOGDEBUG )
  else :
   try :
    IIiIi1I1iI1 . execute ( "DELETE FROM %s" % i1I111II11 [ 0 ] )
    ooOO . commit ( )
    OoO ( 'Data from table `%s` cleared.' % i1I111II11 [ 0 ] , xbmc . LOGDEBUG )
   except Exception , o00o : OoO ( "DB Remove Table `%s` Error: %s" % ( i1I111II11 [ 0 ] , str ( o00o ) ) , xbmc . LOGERROR )
 IIiIi1I1iI1 . close ( )
 OoO ( '%s DB Purging Complete.' % name , xbmc . LOGNOTICE )
 ooO0oo0000oOo = name . replace ( '\\' , '/' ) . split ( '/' )
 o0OoOO ( "[COLOR %s]Purge Database[/COLOR]" % OOOO0OOO , "[COLOR %s]%s Complete[/COLOR]" % ( i1i1ii , ooO0oo0000oOo [ len ( ooO0oo0000oOo ) - 1 ] ) )
 if 56 - 56: O0Oooo0O / o0o00Oo0O * OoOo0o
def IiiiII ( path ) :
 OoO ( "Deleting File: %s" % path , xbmc . LOGNOTICE )
 try : os . remove ( path )
 except : return False
 if 32 - 32: iiiiiiii1 . iI11I1II1I1I % I1ii11iIi11i . ii
 if 81 - 81: Ii * iiiiiiii1 . OOOo00oo0oO * OOOo00oo0oO . I11i1ii1
def OoO00o00 ( ) :
 Iii1i1ii1i1 = os . path . join ( oO0o0o0ooO0oO , 'addon_data' )
 iio0Oo = [
 ( os . path . join ( I11 , 'plugin.video.phstreams' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.bob' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.specto' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.genesis' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.exodus' , 'cache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'onechannelcache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'saltscache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'saltshd.lite.db' ) ) ]
 IiiiiiiI111i = [
 ( Iii1i1ii1i1 ) ,
 ( I11 ) ,
 ( os . path . join ( i1111 , 'cache' ) ) ,
 ( os . path . join ( i1111 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( Iii1i1ii1i1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Iii1i1ii1i1 , 'plugin.video.itv' , 'Images' ) ) ]
 if 19 - 19: ii * OOOo00oo0oO
 ooOo = 0
 if 60 - 60: IIiIiII11i - iiiiiiii1 + ooo0O % OoOo0o
 for iIIi in IiiiiiiI111i :
  if os . path . exists ( iIIi ) and not iIIi in [ I11 , Iii1i1ii1i1 ] :
   ooOo = ooooOOo ( iIIi , ooOo )
  else :
   for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( iIIi ) :
    for o0o0oo0OOo0O0 in oo0OOO0OOoOO :
     if 'cache' in o0o0oo0OOo0O0 . lower ( ) and not o0o0oo0OOo0O0 . lower ( ) == 'meta_cache' : ooOo = ooooOOo ( os . path . join ( oooO0O0o00o , o0o0oo0OOo0O0 ) , ooOo )
     if 75 - 75: oOoO0o00OO0
 return ooOo
def ooooOOo ( path , total = 0 ) :
 for o0oo0O0OO0 , IIiI , Ooo00O0 in os . walk ( path ) :
  for Iiii1iI1i in Ooo00O0 :
   i11I1Ii1Iiii1 = os . path . join ( o0oo0O0OO0 , Iiii1iI1i )
   total += os . path . getsize ( i11I1Ii1Iiii1 )
 return total
def OOO ( num , suffix = 'B' ) :
 for o0oooOoOoOo in [ '' , 'K' , 'M' , 'G' ] :
  if abs ( num ) < 1024.0 :
   return "%3.02f %s%s" % ( num , o0oooOoOoOo , suffix )
  num /= 1024.0
 return "%.02f %s%s" % ( num , 'G' , suffix )
 if 96 - 96: iii1i1iiiiIi / oOo % ii * oOOoOooOo
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
 if 6 - 6: oOo0O0Ooo . IIiIiII11i + O0Oooo0O / oOo % oOo0O0Ooo . ii
 if 64 - 64: iI11I1II1I1I + IIiIiII11i . iiiiiiii1 % I1ii11iIi11i * oOOoOooOo
def iiii1i1 ( ) :
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
 if 98 - 98: oOoO0o00OO0 - ii / oOo0O0Ooo . oOOoOooOo - ooOoO0O00
def O0oOOo0Oo ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , I1IIIii + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , I1IIIii + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 60 - 60: iii1i1iiiiIi % iii1i1iiiiIi
def I1I ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( O00OOOoOoo0O ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , I1IIIii + 'FTV4.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( O00OOOoOoo0O ) + '/wizard/customftv/settings.xml' , 17 , I1IIIii + 'FTV3.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , I1IIIii + 'FTV1.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'RESET FTV DATABASE' , 'url' , 18 , I1IIIii + 'FTV2.png' , Oo00OOOOO , '' )
 if 9 - 9: I11i1ii1 - IIiIiII11i * oOo
 if 78 - 78: iI11I1II1I1I / o0o00Oo0O * OOOo00oo0oO / iiiiiiii1 / iii1i1iiiiIi
 if 15 - 15: oOOoOooOo / OOOo00oo0oO
def O0Oo00o0o ( ) :
 Oo0O00O0O ( )
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  oooooO0oO0o ( )
 if iiI == 0 :
  O0ooo0Ooo ( IIo0o0O0O00oOOo )
 if iiI == 0 :
  oOOo0OOOOo0o ( IIo0o0O0O00oOOo )
  if 29 - 29: I11i1ii1 - i1IiiiI1iI . o0o00Oo0O . o0o00Oo0O
  if 16 - 16: ooOoO0O00 * oOOoOooOo % oOo + i1iIi
  if 50 - 50: OOOo00oo0oO - ii + iiiiiiii1 % oOo
 iIiIi11 ( 'movies' , 'MAIN' )
 if 12 - 12: ooOoO0O00 / oOoO0o00OO0 - iiiiiiii1 . Ii / ooOoO0O00 / ii
def O00o0 ( ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 iI111i = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1IIiI1i , O000OOO in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , Ii1IIiI1i , Ii1IIiI1i , '' )
 iIiIi11 ( 'tvshows' , 'INFO' )
 if 50 - 50: oOoO0o00OO0 % oOoO0o00OO0 . oOoO0o00OO0 / i1IiiiI1iI . oOoO0o00OO0
def IiIOOOoo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( ooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 61 - 61: oOo - Ii / i1IiiiI1iI % I11i1ii1
def oooooO0oO0o ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( O00OOOoOoo0O ) , 36 , I1IIIii + 'GothamSkins.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( O00OOOoOoo0O ) , 37 , I1IIIii + 'HelixSkins.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , i1111 , 38 , I1IIIii + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 21 - 21: iiiiiiii1 % I11i1ii1 % I1ii11iIi11i % o0o00Oo0O
def OoOoooOO00OO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OooOoOO0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 76 - 76: oOoO0o00OO0 + OoOo0o % o0o00Oo0O * Ii . o0o00Oo0O . Ii
def i11iII1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + oOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 15 - 15: oOOoOooOo * iI11I1II1I1I * OOOo00oo0oO
def O0oo0O00ooOo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + oOoOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 2 - 2: oOOoOooOo - i1IiiiI1iI * ooOoO0O00 % OoOo0o / ii * OoOo0o
def OOO000ooO0OO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 91 - 91: oOo0O0Ooo - oOo - I1ii11iIi11i - i1iIi * iI11I1II1I1I
def O0ooo0Ooo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OO0ooo0OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 40 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 69 - 69: O0Oooo0O + iI11I1II1I1I * OOOo00oo0oO + I11i1ii1 % oOOoOooOo - i1iIi
def o00OOOoO000 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o0O0OoO0oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 84 - 84: Ii / ooo0O % iI11I1II1I1I . oOOoOooOo . oOo / iiiiiiii1
def oOooO ( ) :
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  ooooo0oo0OO ( )
 if iiI == 1 :
  IIiII ( )
 if iiI == 2 :
  IIi1 ( )
  if 87 - 87: o0o00Oo0O - OOOo00oo0oO % I1ii11iIi11i
  if 98 - 98: Ii . O0Oooo0O + iii1i1iiiiIi
  if 55 - 55: i1IiiiI1iI
  if 72 - 72: i1IiiiI1iI + oOOoOooOo / oOo0O0Ooo . I11i1ii1 % oOo / Ii
def IIiII ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 iI111i = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , I1III1I1IiI in iI111i :
  IIII ( 'Android Apps' + I1III1I1IiI , 'https://www.apkfiles.com' + IIo0o0O0O00oOOo , 30035 , I1IIIii + 'apps.png' )
 for IIo0o0O0O00oOOo , I1III1I1IiI in IIi11i1i1iI1 :
  IIII ( 'Android Games' + I1III1I1IiI , 'https://www.apkfiles.com' + IIo0o0O0O00oOOo , 30035 , I1IIIii + 'GAMES.png' )
 iIiIi11 ( 'movies' , 'MAIN' )
def ooooooo0oOo0 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  if '/cat' in url :
   IIII ( ( O000OOO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def OooO00oO00o ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  if '/app' in url :
   IIII ( ( O000OOO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def IIII1iI1IiIiI ( url ) :
 IIi = i11111IIIII ( url )
 oOO0 = url
 if "page=" in str ( url ) :
  oOO0 = url . split ( '?' ) [ 0 ]
 iI111i = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( IIi )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  if 'apk' in url :
   O0O0ooOOO ( ( O000OOO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + Ii1IIiI1i )
 if len ( IIi11i1i1iI1 ) > 1 :
  IIi11i1i1iI1 = str ( IIi11i1i1iI1 [ len ( IIi11i1i1iI1 ) - 1 ] )
 O0O0ooOOO ( 'Next Page' , oOO0 + str ( IIi11i1i1iI1 ) , 30037 , I1IIIii + 'Next.png' )
def i1II1 ( name , url ) :
 IIi = II11iIII1i1I ( url )
 name = name
 iI111i = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( IIi )
 for url in iI111i :
  url = 'https://www.apkfiles.com' + url
  OoOoOoo0oOOooo0o ( name , url , 'Brackets' )
def IIi1 ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'https://www.apkfiles.com/search?q=' + ( OOooo ) . replace ( ' ' , '+' ) + '&search_type=1'
 IIIiIiI = O0OO . lower ( )
 IIII1iI1IiIiI ( IIIiIiI )
 if 6 - 6: OoOo0o . Ii - iI11I1II1I1I * I11i1ii1 * iiiiiiii1
def iiIII1i ( url ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( IiI1Ii11Iiii , 'Download' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , O000OOO + '.apk' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 44 - 44: Ii % O0Oooo0O % OOOo00oo0oO + i1IiiiI1iI * OOOo00oo0oO . i1iIi
def OoOo0Oooo0o ( url ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , O000OOO + '.mp4' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 65 - 65: iii1i1iiiiIi + O0Oooo0O % oOo0O0Ooo
 if 54 - 54: O0Oooo0O / ooo0O
def I11IIIIiII ( name , url , description ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , name )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 OoooO = xbmc . translatePath ( os . path . join ( I1i1iiI1 ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OoooO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , OoooO , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 32 - 32: oOoO0o00OO0 * oOo0O0Ooo + ooo0O % IIiIiII11i + OoOo0o + i1iIi
 if 90 - 90: i1iIi
 if 30 - 30: ooo0O + i1iIi / ii - I11i1ii1 % OOOo00oo0oO
 if 21 - 21: ii % iii1i1iiiiIi - iii1i1iiiiIi / oOoO0o00OO0 / ooo0O
 if 15 - 15: oOOoOooOo / oOOoOooOo % ii . O0Oooo0O
def ooooo0oo0OO ( ) :
 IIIi1I1IIii1II = i11111IIIII ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iI111i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , IIo0o0O0O00oOOo , IIII1iIIii , I1I1 , oOoOooO0OOOoo in iI111i :
  O0O0ooOOO ( O000OOO , IIo0o0O0O00oOOo , 80003 , IIII1iIIii , I1IIIii + 'APKToolsB.png' , oOoOooO0OOOoo )
def I1I111i ( apk , ret = None ) :
 if apk == "kodi" :
  OOooOOoO0 = "https://kodi.tv/download/"
  IIIi1I1IIii1II = i11111IIIII ( OOooOOoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iI111i = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( IIIi1I1IIii1II )
  if len ( iI111i ) == 1 :
   Ii11i = iI111i [ 0 ] [ 0 ]
   iI1 = iI111i [ 0 ] [ 1 ]
   O00 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( Ii11i , iI1 )
  if ret == 'version' : return Ii11i
  else : return O00
 elif apk == "spmc" :
  i1iiiii = 'https://github.com/koying/SPMC/releases/latest/'
  IIIi1I1IIii1II = i11111IIIII ( i1iiiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iI111i = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( IIIi1I1IIii1II )
  Ii11i = re . sub ( '<[^<]+?>' , '' , iI111i [ 0 ] ) . replace ( ' ' , '' )
  O00 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( Ii11i , Ii11i )
  if ret == 'version' : return Ii11i
  else : return O00
def OoOoOoo0oOOooo0o ( name , url , Brackets ) :
 if oOOo0O00o ( ) == 'android' :
  IIiii1I1I = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not IIiii1I1I : o0OoOO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  oo0O0OoO = name
  if IIiii1I1I :
   if not os . path . exists ( oO ) : os . makedirs ( oO )
   if not I111IiiIi1 ( url ) == True : o0OoOO ( oOo0oooo00o , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % oo0O0OoO , '' , 'Please Wait' )
   oo0O00Oooo0O0 = os . path . join ( oO , "%s.apk" % name )
   try : os . remove ( oo0O00Oooo0O0 )
   except : pass
   downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   if "Brackets" in Brackets :
    o0II1 = zipfile . ZipFile ( oo0O00Oooo0O0 )
    for file in o0II1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oO , os . path . basename ( file ) ) , 'wb' ) as Iiii1iI1i :
       OO0O0O0oo = file . split ( '/' ) [ 1 ]
       Iiii1iI1i . write ( o0II1 . read ( file ) )
       xbmc . sleep ( 500 )
       Iiii1iI1i . close ( )
       try :
        os . remove ( oo0O00Oooo0O0 )
       except :
        pass
       oo0O00Oooo0O0 = os . path . join ( oO , OO0O0O0oo )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oo0O00Oooo0O0 + '")' )
  else : o0OoOO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0OoOO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 41 - 41: ooOoO0O00 / OOOo00oo0oO
 if 47 - 47: O0Oooo0O
 if 25 - 25: iiiiiiii1 + oOo0O0Ooo + iii1i1iiiiIi + O0Oooo0O % o0o00Oo0O
 if 26 - 26: oOOoOooOo + iii1i1iiiiIi
def II111I1i1 ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( IIIi1I1IIii1II )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIo0o0O0O00oOOo = ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + IIo0o0O0O00oOOo )
  Iio0o0o ( ( O000OOO ) . replace ( '_' , ' ' ) , IIo0o0O0O00oOOo )
  if 32 - 32: o0o00Oo0O / OoOo0o . oOOoOooOo % O0Oooo0O
def Iio0o0o ( name , url ) :
 if oOOo0O00o ( ) == 'android' :
  IIiii1I1I = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not IIiii1I1I : o0OoOO ( oOo0oooo00o , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  oo0O0OoO = name
  if IIiii1I1I :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not I111IiiIi1 ( url ) == True : o0OoOO ( oOo0oooo00o , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % oo0O0OoO , '' , 'Please Wait' )
   oo0O00Oooo0O0 = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oo0O00Oooo0O0 )
   except : pass
   downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oo0O00Oooo0O0 + '")' )
  else : o0OoOO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0OoOO ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 18 - 18: I11i1ii1 * iiiiiiii1 / i1IiiiI1iI / o0o00Oo0O
 if 11 - 11: iI11I1II1I1I / i1iIi + ii % ooOoO0O00 * Ii
def OoOooooo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'INFO' )
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . i1iIi - I1ii11iIi11i . Ii
 if 47 - 47: I1ii11iIi11i % oOo - oOOoOooOo - I1ii11iIi11i * OOOo00oo0oO
def oOoO0o0ooo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 30015 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 72 - 72: ooo0O % ooo0O + iiiiiiii1 + oOoO0o00OO0 / I1ii11iIi11i
def IIIiii ( url , iconimage , fanart ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iIi1Ii1111i = url
 Ii1IIiI1i = iconimage
 fanart = fanart
 iI111i = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for I1i , O000OOO in iI111i :
  if '.mp4' in O000OOO :
   O0O0ooOOO ( 'Watch VIDEO' , url + '/' + I1i , 222 , Ii1IIiI1i , fanart , '' )
  if 'description' in O000OOO :
   O0O0ooOOO ( 'Read Description' , url + '/' + I1i , 30017 , Ii1IIiI1i , fanart , '' )
  if 'images' in O000OOO :
   o00oOOooOOo0o ( 'View Images' , url + '/' + I1i , 30018 , Ii1IIiI1i , fanart , '' )
  if 'url' in O000OOO :
   O0O0ooOOO ( 'Install Build On Android' , url + '/' + I1i , 30016 , Ii1IIiI1i , fanart , '' )
  if 'url' in O000OOO :
   O0O0ooOOO ( 'Install Build On Pc' , url + '/' + I1i , 30019 , Ii1IIiI1i , fanart , '' )
 iIiIi11 ( 'movies' , 'INFO' )
 if 44 - 44: I11i1ii1 . i1IiiiI1iI % oOo0O0Ooo - ooOoO0O00
def iIII1II ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in iI111i :
  I1iiIIIIIIII ( url )
  if 94 - 94: I1ii11iIi11i + O0Oooo0O / oOOoOooOo . i1IiiiI1iI . Ii / ooOoO0O00
def o0OOoo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in iI111i :
  oO0o00O ( url )
  if 7 - 7: I1ii11iIi11i * oOo - IIiIiII11i % O0Oooo0O . I1ii11iIi11i . I1ii11iIi11i
def iiII1iIi1ii1i ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'desc="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for I1111i1 in iI111i :
  OoOoO ( 'Description:' , I1111i1 )
  if 49 - 49: iii1i1iiiiIi
def OoO0O00 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 url = url
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for I1i , O000OOO in iI111i :
  if 'png' in O000OOO :
   O0O0ooOOO ( 'image' , '' , '' , url + '/' + I1i , url + '/' + I1i , '' )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 96 - 96: I11i1ii1 - iiiiiiii1
def I11I111i ( name , url , description ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , name + '.zip' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 I11OO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11OO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OO0 ( )
 if 82 - 82: O0Oooo0O / oOOoOooOo / oOOoOooOo
 if 6 - 6: IIiIiII11i % oOoO0o00OO0 % ooOoO0O00 * oOOoOooOo
def oO0o00O ( url ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 I11OO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11OO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
 o0O0oo0OO0O ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIIoooO0 ( )
 if 7 - 7: oOo * iiiiiiii1
def I1iiIIIIIIII ( url ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 I11OO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11OO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
 o0O0oo0OO0O ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIIoooO0 ( )
 if 16 - 16: O0Oooo0O . ooOoO0O00 . I11i1ii1
def II1iIiiiI ( name , url , description ) :
 I11OO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 oo0O00Oooo0O0 = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oO0 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print I11OO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIIoooO0 ( )
 if 9 - 9: i1iIi
def oOOo0O00o ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def iiIoO ( log ) :
 xbmc . log ( "[%s]: %s" % ( oOo0oooo00o , log ) )
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : Iiii1iI1i = open ( Oo0o0000o0o0 , 'w' ) ; Iiii1iI1i . close ( )
 with open ( Oo0o0000o0o0 , 'a' ) as Iiii1iI1i :
  Ii11I1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  Iiii1iI1i . write ( Ii11I1i . rstrip ( '\r\n' ) + '\n' )
def OoO ( msg , level = xbmc . LOGDEBUG ) :
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : Iiii1iI1i = open ( Oo0o0000o0o0 , 'w' ) ; Iiii1iI1i . close ( )
 if WIZDEBUGGING == 'false' : return False
 if DEBUGLEVEL == '0' : return False
 if DEBUGLEVEL == '1' and not level in [ xbmc . LOGNOTICE , xbmc . LOGERROR , xbmc . LOGSEVERE , xbmc . LOGFATAL ] : return False
 if DEBUGLEVEL == '2' : level = xbmc . LOGNOTICE
 try :
  if isinstance ( msg , unicode ) :
   msg = '%s' % ( msg . encode ( 'utf-8' ) )
  xbmc . log ( '%s: %s' % ( oOo0oooo00o , msg ) , level )
 except Exception as o00o :
  try : xbmc . log ( 'Logging Failure: %s' % ( o00o ) , level )
  except : pass
 if ENABLEWIZLOG == 'true' :
  iI11IIi1iiI1I = getS ( 'nextcleandate' ) if not getS ( 'nextcleandate' ) == '' else str ( TODAY )
  if CLEANWIZLOG == 'true' and iI11IIi1iiI1I <= str ( TODAY ) : checkLog ( )
  with open ( Oo0o0000o0o0 , 'a' ) as Iiii1iI1i :
   Ii11I1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , msg )
   Iiii1iI1i . write ( Ii11I1i . rstrip ( '\r\n' ) + '\n' )
def iIIoooO0 ( ) :
 iiI = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iiI == 0 : return
 elif iiI == 1 : pass
 oo0o0000 = oOOo0O00o ( )
 iiIoO ( "Platform: " + str ( oo0o0000 ) )
 os . _exit ( 1 )
 iiIoO ( "Force close failed!  Trying alternate methods." )
 if oo0o0000 == 'osx' :
  iiIoO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oo0o0000 == 'linux' :
  iiIoO ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oo0o0000 == 'android' :
  iiIoO ( "############ try android force close #################" )
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
 elif oo0o0000 == 'windows' :
  iiIoO ( "############ try windows force close #################" )
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
  iiIoO ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  iiIoO ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 83 - 83: I1ii11iIi11i / oOOoOooOo
  if 11 - 11: ooo0O - IIiIiII11i % OOOo00oo0oO . IIiIiII11i
  if 65 - 65: OOOo00oo0oO . Ii % OoOo0o * iiiiiiii1 % I1ii11iIi11i
def oOOo0OOOOo0o ( url ) :
 o0oO0 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( url ) :
  for file in oOoO :
   if file . endswith ( ".xml" ) :
    o0oO0 . update ( 0 , "Fixing" , file , 'Please Wait' )
    iII1ii1 = open ( ( os . path . join ( oooO0O0o00o , file ) ) ) . read ( )
    oO0o0ooooo = iII1ii1 . replace ( i1111 , 'special://home/' )
    Iiii1iI1i = open ( ( os . path . join ( oooO0O0o00o , file ) ) , mode = 'w' )
    Iiii1iI1i . write ( str ( oO0o0ooooo ) )
    Iiii1iI1i . close ( )
 iIIoooO0 ( )
 if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + i1iIi . OoOo0o
def IiiIiiiiI1III ( ) :
 IIII ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , I1IIIii + 'RadioNomy.png' )
 IIII ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , I1IIIii + 'RadioNomy.png' )
 IIII ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , I1IIIii + 'RadioNomy.png' )
 if 58 - 58: iI11I1II1I1I + O0Oooo0O - oOoO0o00OO0 - ooOoO0O00 * iii1i1iiiiIi
def iii1 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def iII1iii ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def o0O0o ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IIi )
 for url , O000OOO in IIi11i1i1iI1 :
  IIII ( ( '[COLOR' + iiI1IiI + ']Filter - ' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']Stream - ' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , Ii1IIiI1i )
def OO0o0o ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( IIi )
 for url in iI111i :
  oo0 ( url )
def O0O0O00OoO0O ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo
 i1II11III = 'https://www.radionomy.com/en/search/index?query=' + ( OOooo ) . replace ( ' ' , '+' )
 oOOo0 = i11111IIIII ( i1II11III )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']Stream - ' + O000OOO + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + IIo0o0O0O00oOOo , 70005 , Ii1IIiI1i )
  if 95 - 95: i1IiiiI1iI + ooo0O - Ii % oOo / OOOo00oo0oO
  if 80 - 80: O0Oooo0O * OOOo00oo0oO * ooOoO0O00
def Oo0O00O ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.listenlive.eu/' + IIo0o0O0O00oOOo , 10111113 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def i1iI1i11iIi1 ( url ) :
 IIi = II11iIII1i1I ( url )
 if 32 - 32: oOo0O0Ooo + Ii - O0Oooo0O / IIiIiII11i
 if 27 - 27: oOOoOooOo . I1ii11iIi11i + oOOoOooOo + iiiiiiii1
 iI111i = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( IIi )
 for O000OOO , III11IiI , url , IIii in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' [COLORorangered] ' + IIii + '[/COLOR]' , url , 222225 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , '[COLOR' + iiI1IiI + ']' + O000OOO + '[CR]' + III11IiI + '[CR]' + IIii + '[/COLOR]' )
  if 24 - 24: oOo0O0Ooo - ooOoO0O00 - o0o00Oo0O % O0Oooo0O - iI11I1II1I1I . i1IiiiI1iI
def II1iii1iII ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.toonjet.com/' + IIo0o0O0O00oOOo , 8051 , I1IIIii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1ii1111iIi1 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( IIi )
 for url , Ii1IIiI1i in iI111i :
  if 'ol.gif' in Ii1IIiI1i :
   pass
  elif 'link_block_' in Ii1IIiI1i :
   pass
  elif '.png' in Ii1IIiI1i :
   pass
  else :
   IIII ( ( Ii1IIiI1i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , I1IIIii + 'vod.png' )
 for url in IIi11i1i1iI1 :
  IIII ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , I1IIIii + 'Next.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oIIi111 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( IIi )
 for url in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , I1IIIii + 'classictoons.png' )
  if 63 - 63: oOOoOooOo % oOo0O0Ooo . OoOo0o - oOOoOooOo / I1ii11iIi11i % oOo0O0Ooo
  if 39 - 39: ooo0O . ooOoO0O00 % OOOo00oo0oO / i1IiiiI1iI % o0o00Oo0O
def o0O0OOooO ( ) :
 iiiI1ii ( 'Audio Books' , '' , 30011 , I1IIIii + 'AudioBooks.png' , I1IIIii + 'AudioBooks.png' , '' )
 iiiI1ii ( 'Kids Audio Books' , '' , 30006 , I1IIIii + 'KidsAudioBooks.png' , I1IIIii + 'KidsAudioBooks.png' , '' )
 if 1 - 1: O0Oooo0O * oOo - iiiiiiii1
def O0OoO0 ( ) :
 iiiI1ii ( 'All' , '' , 30001 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 iiiI1ii ( 'Popular' , '' , 30012 , I1IIIii + 'POPULARv.png' , I1IIIii + 'POPULARv.png' , '' )
 iiiI1ii ( 'Search' , '' , 30013 , I1IIIii + 'Search.png' , I1IIIii + 'Search.png' , '' )
 if 73 - 73: Ii - oOo0O0Ooo * oOo0O0Ooo
def ooo0ooOoOOoO ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for O000OOO , IIo0o0O0O00oOOo , ii1i1 in iI111i :
  if 'Parent' in O000OOO :
   pass
  elif '2' in ii1i1 :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: I11i1ii1 - o0o00Oo0O + oOo0O0Ooo / ii * iiiiiiii1 / ooOoO0O00
def II11II1i ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for O000OOO , IIo0o0O0O00oOOo , ii1i1 in iI111i :
  if OOooo in O000OOO . lower ( ) :
   if '1' in ii1i1 :
    iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '2' in ii1i1 :
    iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '3' in ii1i1 :
    iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 56 - 56: i1iIi * Ii
    if 92 - 92: IIiIiII11i - o0o00Oo0O . O0Oooo0O
def oOOOoOO ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for O000OOO , IIo0o0O0O00oOOo , ii1i1 in iI111i :
  if '1' in ii1i1 :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 3010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '2' in ii1i1 :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '3' in ii1i1 :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 80 - 80: ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: OOOo00oo0oO * ooOoO0O00 . ii % oOOoOooOo
def OoOo00oOoo0oO ( url ) :
 I1i = url
 oOOo0 = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOOo0 )
 for url , O000OOO in IIi11i1i1iI1 :
  if 'mp3' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1i + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1i + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1i + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '/' in O000OOO :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i + url , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: O0Oooo0O - ooOoO0O00 / I11i1ii1
   if 13 - 13: iii1i1iiiiIi - oOo * ii
   if 26 - 26: ii
def ooo0000oo0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 I1i = url
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
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i + url , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 58 - 58: iiiiiiii1 % iI11I1II1I1I . iI11I1II1I1I / i1IiiiI1iI
   if 79 - 79: oOo / OoOo0o - ooOoO0O00 + ooOoO0O00 - I11i1ii1 + I11i1ii1
def oOoOo000Ooooo ( ) :
 iiiI1ii ( 'A-Z' , '' , 30007 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 iiiI1ii ( 'All' , '' , 30003 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 iiiI1ii ( 'Search' , '' , 30014 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 if 18 - 18: i1iIi + iii1i1iiiiIi . ooOoO0O00 / I11i1ii1 / iiiiiiii1
def oOo0OO0 ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i in iI111i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + IIo0o0O0O00oOOo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in Ii1IIiI1i :
   pass
  else :
   iiiI1ii ( Ii1IIiI1i , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( IIo0o0O0O00oOOo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + Ii1IIiI1i + '.gif' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 56 - 56: IIiIiII11i . IIiIiII11i + I11i1ii1 . ooo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: oOOoOooOo . I11i1ii1 . IIiIiII11i
 if 25 - 25: I11i1ii1 * O0Oooo0O - OOOo00oo0oO * Ii * oOo0O0Ooo * OoOo0o
def Ooii1II11IIII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if '</a>' in O000OOO :
   pass
  elif '(' in O000OOO :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 90 - 90: I1ii11iIi11i * i1iIi
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: oOoO0o00OO0 + iI11I1II1I1I % I11i1ii1
def II1iOo0ooo0 ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if OOooo in O000OOO . lower ( ) :
   if '</a>' in O000OOO :
    pass
   elif '(' in O000OOO :
    iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   else :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 41 - 41: I11i1ii1 - o0o00Oo0O * OOOo00oo0oO * IIiIiII11i . i1IiiiI1iI - O0Oooo0O
    if 25 - 25: ii / i1IiiiI1iI % O0Oooo0O
def I1iIiIi111I ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if '</a>' in O000OOO :
   pass
  elif '(' in O000OOO :
   iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IIo0o0O0O00oOOo , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 17 - 17: oOoO0o00OO0 * ii % ooOoO0O00 % ii . iiiiiiii1
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: oOo . OOOo00oo0oO
 if 4 - 4: I1ii11iIi11i % i1iIi % oOo * iiiiiiii1 % ii
def iiooo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oOOo0 )
 for url in iI111i :
  I1i = ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I1i )
  if 42 - 42: ii % i1IiiiI1iI % I11i1ii1
def O0OoO0OOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  if '<p align' in O000OOO :
   pass
  elif '&nbsp;' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 45 - 45: oOo * oOo0O0Ooo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: iiiiiiii1 % IIiIiII11i / iii1i1iiiiIi % oOoO0o00OO0 . iI11I1II1I1I % o0o00Oo0O
 if 74 - 74: oOoO0o00OO0 * OOOo00oo0oO + iiiiiiii1 % o0o00Oo0O
def Iii1IiIiIii ( ) :
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
def OOo0ooOOOo0O0 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 iII1ii1IIII = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , Ii1IIiI1i , Ii1IIiI1i , O000OOO )
 for url , O000OOO in iII1ii1IIII :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in next :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , I1IIIii + 'Next.png' , '' , '' )
def ooI1 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 Oo00o000oOO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 i1Iii1i1II1 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oOOo0 )
 O0o00OoooO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in i1Iii1i1II1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url , O000OOO in Oo00o000oOO :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
def IiI1i1iI ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
  if 5 - 5: oOo . oOoO0o00OO0 . Ii
def iIIIII ( ) :
 oOOo0 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 iI111i = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if '9cart' in IIo0o0O0O00oOOo :
   IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 20001 , I1IIIii + 'ORIGINCARTOON.png' )
   if 57 - 57: IIiIiII11i . ooOoO0O00
def I11Ii1 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oOOo0 )
 iIIii = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if '9cart' in url :
   IIII ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url in IIi11i1i1iI1 :
  if '9cart' in url :
   IIII ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url , O000OOO in iIIii :
  if '9cart' in url :
   IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
   if 63 - 63: ooOoO0O00
def II1iII11 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 20003 , Ii1IIiI1i )
 for url , O000OOO in IIi11i1i1iI1 :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
  if 19 - 19: IIiIiII11i
def i1iIIi ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)">' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'Watch' in url :
   IIII ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , I1IIIii + 'ORIGINCARTOON.png' )
   if 63 - 63: ii * O0Oooo0O
def II1Iiiii ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 20005 , I1IIIii + 'ORIGINCARTOON.png' )
  if 70 - 70: ii / OoOo0o - oOo % ii
def iI1Iii1i11 ( url ) :
 url = cloudflare . source ( url )
 II11IiI1 ( url )
 if 30 - 30: I1ii11iIi11i + i1iIi % Ii * ooOoO0O00 + oOo0O0Ooo % OoOo0o
def IiiIIiiI1I11 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . recompile ( 'src="([^"]*)"' )
 for url in iI111i :
  II11IiI1 ( url )
  if 74 - 74: ooo0O - oOOoOooOo / oOo0O0Ooo
  if 98 - 98: o0o00Oo0O % Ii % OoOo0o
def I1i1 ( url , name ) :
 url = url ; name = name
 Ii1Ii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 Ii1Ii . clear ( )
 iIIOOoOOooO = [ ]
 i1111II1iIII = [ ]
 i1II1iII = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( i1II1iII )
 for Ii1IIiI1i in IIi11i1i1iI1 :
  I1ii11ii1iiI = Ii1IIiI1i
 iIIii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( i1II1iII )
 for oO0oo0 , IiIiI1 in iIIii :
  iIIOOoOOooO . append ( [ oO0oo0 , IiIiI1 ] )
  if len ( iIIOOoOOooO ) == len ( iIIii ) :
   for iIIi in iIIOOoOOooO :
    iiiI1 = random . randint ( 1 , len ( iIIOOoOOooO ) )
    try :
     III1Oo00OO = iIIOOoOOooO [ int ( iiiI1 ) ]
     if III1Oo00OO [ 1 ] not in i1111II1iIII :
      i1111II1iIII . append ( III1Oo00OO [ 1 ] )
      OOoO00ooO = i11111IIIII ( III1Oo00OO [ 0 ] )
      o00O0O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoO00ooO )
      for iIi111 , I11I1I in o00O0O :
       if 'easy' in I11I1I :
        i1i1ii1 = i11111IIIII ( I11I1I )
        ii1iii1i = re . compile ( 'file: "(.+?)"' ) . findall ( i1i1ii1 )
        for i1Ii in ii1iii1i :
         if 'http' in i1Ii :
          IioO0O = xbmcgui . ListItem ( III1Oo00OO [ 1 ] , iconImage = I1ii11ii1iiI , thumbnailImage = I1ii11ii1iiI )
          IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : III1Oo00OO [ 1 ] } )
          IioO0O . setProperty ( "IsPlayable" , "true" )
          Ii1Ii . add ( i1Ii , IioO0O )
          xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IioO0O )
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
   if 40 - 40: I11i1ii1 . ii . oOo0O0Ooo + o0o00Oo0O % ooOoO0O00 / I11i1ii1
def IiII1II1 ( url ) :
 Ii1Ii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 Ii1Ii . clear ( )
 Oo0ooO000Oo = [ ]
 OOOoOOooO0 = [ ]
 I1IiiI11 = [ ]
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  OOOoOOooO0 . append ( [ url , O000OOO ] )
  if len ( OOOoOOooO0 ) == len ( iI111i ) :
   for iIIi in OOOoOOooO0 :
    iIII1II11I1 = random . randint ( 1 , len ( OOOoOOooO0 ) )
    try :
     O000oOo0OO = OOOoOOooO0 [ int ( iIII1II11I1 ) ]
    except :
     pass
    if O000oOo0OO [ 1 ] not in I1IiiI11 :
     I1IiiI11 . append ( O000oOo0OO [ 1 ] )
     if int ( len ( Oo0ooO000Oo ) ) < 1 :
      Oo0ooO000Oo . append ( O000oOo0OO [ 1 ] [ 0 ] )
      I1i1 ( O000oOo0OO [ 0 ] , O000oOo0OO [ 1 ] )
     else :
      pass
    else :
     pass
  else :
   pass
   if 57 - 57: oOoO0o00OO0
def II1111i11i11 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 OoOO0o = sys . argv [ 0 ]
 OoOO0o += '?mode=' + str ( mode )
 OoOO0o += '&title=' + urllib . quote_plus ( name )
 OoOO0o += '&image=' + urllib . quote_plus ( image )
 OoOO0o += '&page=' + str ( page )
 if url != '' :
  OoOO0o += '&url=' + urllib . quote_plus ( url )
 if keyword :
  OoOO0o += '&keyword=' + urllib . quote_plus ( keyword )
 IioO0O = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  IioO0O . addContextMenuItems ( contextMenu )
 if infoLabels :
  IioO0O . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  IioO0O . setProperty ( "IsPlayable" , "true" )
 IioO0O . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = isFolder )
 if 43 - 43: o0o00Oo0O * Ii - ii - OOOo00oo0oO
def iIiiI1iIiI1I ( ) :
 OOo0ooOOO = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 IIi = i11111IIIII ( OOo0ooOOO )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  II1111i11i11 ( O000OOO , 9110012 , url = IIo0o0O0O00oOOo , image = O0O , isFolder = False )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 99 - 99: oOo - iiiiiiii1 . oOo % ooo0O % OoOo0o . o0o00Oo0O
def o00OoooooooOo ( ) :
 OOo0ooOOO = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , '' , 10004 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 ii1ii111 ( '[COLOR' + iiI1IiI + ']24/7 Select Cartoon[/COLOR]' , '' , 9110011 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' , '' )
 II1111i11i11 ( '[COLOR' + iiI1IiI + ']24/7 Random Cartoon[/COLOR]' , 9110010 , url = OOo0ooOOO , image = I1IIIii + 'Kids.png' , isFolder = False )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 if 56 - 56: OOOo00oo0oO + ooOoO0O00 * iiiiiiii1 - o0o00Oo0O
def o0OOO00O ( ) :
 OOo0ooOOO = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 oOOo0 = i11111IIIII ( OOo0ooOOO )
 if 84 - 84: iiiiiiii1 % oOo0O0Ooo / iI11I1II1I1I * i1iIi * iI11I1II1I1I + oOoO0o00OO0
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oOOo0 )
 if 78 - 78: I11i1ii1 / iiiiiiii1 * i1iIi . OoOo0o . OOOo00oo0oO - O0Oooo0O
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if OOooo in O000OOO . lower ( ) :
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
    if 39 - 39: oOOoOooOo . ooOoO0O00 + ii . iiiiiiii1 - Ii % O0Oooo0O
    if 38 - 38: OOOo00oo0oO
    if 9 - 9: i1IiiiI1iI . oOo . OOOo00oo0oO / ii
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
def iii1IiI ( url ) :
 OOo0ooOOO = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 IIi = i11111IIIII ( OOo0ooOOO )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIi )
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
 if 87 - 87: oOo0O0Ooo - o0o00Oo0O - i1IiiiI1iI * O0Oooo0O % O0Oooo0O
def Oo0o00o0oOoo0 ( url ) :
 IIi = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIi )
 for Ii1IIiI1i in IIi11i1i1iI1 :
  I1ii11ii1iiI = Ii1IIiI1i
 iIIii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( IIi )
 for url in iIIii :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10007 , I1ii11ii1iiI )
  if 36 - 36: O0Oooo0O / iii1i1iiiiIi + iii1i1iiiiIi * oOOoOooOo / OoOo0o * o0o00Oo0O
  if 17 - 17: oOo / oOOoOooOo % oOo0O0Ooo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: I1ii11iIi11i * oOo / ooo0O * oOo0O0Ooo
def OOo0iIiiI11II11 ( url , IMAGE ) :
 o0o0O00O = [ ]
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IIi )
 for O000OOO , I1i in iI111i :
  if 'panda' in I1i :
   oOOo0 = i11111IIIII ( I1i )
   IIi11i1i1iI1 = re . compile ( "url: '(.+?)'" ) . findall ( oOOo0 )
   for iiIiIIII1iiIIi in IIi11i1i1iI1 :
    if 'http' in iiIiIIII1iiIIi :
     o0o0O00O . append ( { 'source' : 'playpanda' , 'quality' : 'SD' , 'url' : iiIiIIII1iiIIi } )
  elif 'easy' in I1i :
   oo00O00oO = i11111IIIII ( I1i )
   iIIii = re . compile ( 'file: "(.+?)"' ) . findall ( oo00O00oO )
   for iiIiIIII1iiIIi in iIIii :
    if 'http' in iiIiIIII1iiIIi :
     o0o0O00O . append ( { 'source' : 'easyvideo' , 'quality' : 'SD' , 'url' : iiIiIIII1iiIIi } )
  elif 'zoo' in I1i :
   iIiIIIi = i11111IIIII ( I1i )
   o00O0O = re . compile ( 'src: "(.+?)"' ) . findall ( iIiIIIi )
   for iiIiIIII1iiIIi in o00O0O :
    if 'http' in iiIiIIII1iiIIi :
     o0o0O00O . append ( { 'source' : 'videozoo' , 'quality' : 'SD' , 'url' : iiIiIIII1iiIIi } )
 if len ( o0o0O00O ) >= 3 :
  iiI = iI111I11I1I1 . select ( 'Select Playlink' ,
 [ IIIi1I1IIii1II [ "source" ] + " - " + " (" + IIIi1I1IIii1II [ "quality" ] + ")"
 for IIIi1I1IIii1II in o0o0O00O ] )
  if iiI != - 1 :
   url = o0o0O00O [ iiI ] [ 'url' ]
   oO0o = False
   xbmc . Player ( ) . play ( url )
   if 55 - 55: i1IiiiI1iI + ooOoO0O00 - iiiiiiii1 + ooo0O * I11i1ii1
   if 85 - 85: oOo0O0Ooo % Ii
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 23 - 23: Ii * oOoO0o00OO0 % oOo % oOOoOooOo % iii1i1iiiiIi
def ooO0o0OoOo0oO ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( IIi )
 for url in iI111i :
  oo0 ( url )
  if 33 - 33: oOOoOooOo
  if 68 - 68: oOo0O0Ooo . O0Oooo0O * oOo % ii
  if 8 - 8: o0o00Oo0O * oOo0O0Ooo - iii1i1iiiiIi + oOoO0o00OO0
def IiIIiIii1ii ( ) :
 if 4 - 4: OoOo0o % oOOoOooOo - OoOo0o - ooo0O
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , I1IIIii + 'StandUp.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , I1IIIii + 'SearchComedian.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , I1IIIii + 'Others.png' , Oo00OOOOO , '' )
 if 30 - 30: I11i1ii1
def IIIiIII1 ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  if 'elete' in O000OOO :
   pass
  else :
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 222 , Ii1IIiI1i )
   if 92 - 92: I1ii11iIi11i + I11i1ii1 / I1ii11iIi11i + i1iIi / OoOo0o
def I11iI ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oOoO0O0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , oO00O0oO , i1iII1IiiIiI1 in oOoO0O0o :
  for OOooo in oO00O0oO :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   O00O00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for IIo0o0O0O00oOOo , O000OOO in O00O00 :
    if 'tube' in IIo0o0O0O00oOOo :
     pass
    elif 'stage' in IIo0o0O0O00oOOo :
     iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + oO00O0oO + '   -   ' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + Ii1IIiI1i , )
    elif 'vee' in IIo0o0O0O00oOOo :
     pass
     if 40 - 40: iii1i1iiiiIi / OoOo0o . I11i1ii1 / i1IiiiI1iI / I11i1ii1
def iIIi1Iii ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oOoO0O0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , oO00O0oO , i1iII1IiiIiI1 in oOoO0O0o :
  O00O00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for IIo0o0O0O00oOOo , O000OOO in O00O00 :
   if 'tube' in IIo0o0O0O00oOOo :
    pass
   elif 'stage' in IIo0o0O0O00oOOo :
    iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + oO00O0oO + '   -   ' + O000OOO + '[/COLOR]' , ( IIo0o0O0O00oOOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + Ii1IIiI1i )
   elif 'vee' in IIo0o0O0O00oOOo :
    pass
    if 96 - 96: iiiiiiii1 % iiiiiiii1 % O0Oooo0O / O0Oooo0O - oOoO0o00OO0
    if 11 - 11: OoOo0o / ii * i1iIi
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: O0Oooo0O / oOOoOooOo + O0Oooo0O / OoOo0o / OOOo00oo0oO + OoOo0o
def i11i11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 Ii11Iii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOo0 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( Ii11Iii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in Ii11Iii :
  i1i1I1 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 11 - 11: iI11I1II1I1I * I1ii11iIi11i % OOOo00oo0oO . oOOoOooOo - oOoO0o00OO0 * Ii
  if 33 - 33: iiiiiiii1 % ii / OOOo00oo0oO
  if 12 - 12: oOoO0o00OO0 - iI11I1II1I1I * iii1i1iiiiIi + ooo0O . i1IiiiI1iI
  if 59 - 59: iiiiiiii1 . ooOoO0O00
  if 31 - 31: oOo0O0Ooo + oOo0O0Ooo
  if 11 - 11: I11i1ii1 + iii1i1iiiiIi % ooo0O * oOo / I11i1ii1
  if 5 - 5: iiiiiiii1 / OOOo00oo0oO % oOOoOooOo . Ii % iii1i1iiiiIi + OOOo00oo0oO
def ooOo0O ( ) :
 if 95 - 95: oOoO0o00OO0
 iiIii1I1Ii ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 iiIii1I1Ii ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 14 - 14: iiiiiiii1 % oOo
 iIiIi11 ( 'movies' , 'MAIN' )
 if 6 - 6: ooo0O % i1iIi
def iiIII ( ) :
 iiIii1I1Ii ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 iiIii1I1Ii ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 75 - 75: oOo0O0Ooo - oOOoOooOo - oOo0O0Ooo % OOOo00oo0oO % ii
 iIiIi11 ( 'movies' , 'MAIN' )
def I11Iii11i1Ii ( ) :
 if 65 - 65: iI11I1II1I1I * I11i1ii1
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 Ooo00O0 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 89 - 89: I11i1ii1 % Ii . Ii + OOOo00oo0oO / oOoO0o00OO0
 for IIIIIIi1i in Ooo00O0 :
  iiiii11I1 = Ii1iIiII1ii1 + '/Movies/a.to.z/' + IIIIIIi1i + '.php'
  oOOo0 = i1Oo00 ( iiiii11I1 )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in iI111i :
   if OOooo in O000OOO . lower ( ) :
    if '.php' in IIo0o0O0O00oOOo :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 426 , OO00OOoO0o , i1III1 , i11i1ii1I )
    else :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     i1IIIo00oOOO ( O000OOO , IIo0o0O0O00oOOo , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
     if 95 - 95: Ii . ooo0O + ii % I1ii11iIi11i
     iIiIi11 ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 21 - 21: iiiiiiii1 - ooo0O / i1IiiiI1iI % o0o00Oo0O / iI11I1II1I1I / iiiiiiii1
def iIiii1Ii ( ) :
 if 17 - 17: o0o00Oo0O - i1iIi + I11i1ii1
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 Ooo00O0 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 49 - 49: I1ii11iIi11i % OOOo00oo0oO
 for IIIIIIi1i in Ooo00O0 :
  i1iII11I1I1I = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + IIIIIIi1i + '.php'
  oOOo0 = i1Oo00 ( i1iII11I1I1I )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in iI111i :
   if OOooo in O000OOO . lower ( ) :
    if '.php' in IIo0o0O0O00oOOo :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 426 , OO00OOoO0o , i1III1 , i11i1ii1I )
    else :
     O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
     i1IIIo00oOOO ( O000OOO , IIo0o0O0O00oOOo , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
     if 55 - 55: iI11I1II1I1I + iii1i1iiiiIi
     iIiIi11 ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 7 - 7: i1iIi / O0Oooo0O % oOOoOooOo - O0Oooo0O * oOo0O0Ooo
     if 18 - 18: OOOo00oo0oO - I11i1ii1 % i1IiiiI1iI * i1iIi
def OoOooO0oO ( ) :
 if 90 - 90: oOo0O0Ooo - oOo
 IIi = i11111IIIII ( Ii1iIiII1ii1 + 'spongemain.php' )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIi )
 for O000OOO , i11i1ii1I , IIo0o0O0O00oOOo , Ii1IIiI1i , I1I1 , iIi1i in iI111i :
  iiIii1I1Ii ( O000OOO , IIo0o0O0O00oOOo , iIi1i , Ii1IIiI1i , I1I1 , i11i1ii1I )
  iIiIi11 ( 'movies' , 'MAIN' )
def I1i1i1Iii1 ( url ) :
 if 78 - 78: ii % iiiiiiii1 + oOo * ii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iioOoO0oOO = ( '%s%s' % ( OOo0ooOOO , url ) )
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in iI111i :
  if '.php' in url :
   Ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for iIIi in Ii1 :
    if iIIi == url :
     O000OOO = ( '[COLORred]Watched - [/COLOR]' + O000OOO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   o00oOOooOOo0o ( O000OOO , url , 426 , OO00OOoO0o , i1III1 , i11i1ii1I )
  else :
   Ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for iIIi in Ii1 :
    if iIIi == url :
     O000OOO = ( '[COLORred]Watched - [/COLOR]' + O000OOO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   i1IIIo00oOOO ( O000OOO , url , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
   if 92 - 92: iiiiiiii1 . i1iIi
   iIiIi11 ( 'movies' , 'MAIN' )
   if 10 - 10: i1iIi + ooo0O * I11i1ii1 / oOoO0o00OO0 / OOOo00oo0oO
   xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 94 - 94: ooo0O - oOo0O0Ooo - i1IiiiI1iI / I1ii11iIi11i % ii - OOOo00oo0oO
   if 40 - 40: iiiiiiii1
def Oooo0O00Ooo ( url ) :
 if 84 - 84: ooOoO0O00
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIi )
 for O000OOO , i11i1ii1I , url , Ii1IIiI1i , I1I1 , iIi1i in iI111i :
  iiIii1I1Ii ( O000OOO , url , iIi1i , Ii1IIiI1i , I1I1 , i11i1ii1I )
  if 73 - 73: Ii * oOoO0o00OO0 . i1IiiiI1iI % oOo0O0Ooo - oOo0O0Ooo . iii1i1iiiiIi
  iIiIi11 ( 'movies' , 'MAIN' )
  if 66 - 66: OOOo00oo0oO / Ii / iii1i1iiiiIi + oOoO0o00OO0 / o0o00Oo0O
  if 97 - 97: Ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16: ooOoO0O00
def i1IIIo00oOOO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 12 - 12: iii1i1iiiiIi % OoOo0o + OOOo00oo0oO . o0o00Oo0O % iI11I1II1I1I
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOoo0oOO00 = [ ]
  OOoo0oOO00 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OOoo0oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   OOoo0oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IioO0O . addContextMenuItems ( OOoo0oOO00 )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = False )
 return oo0O0o
 if 41 - 41: ii
def iiIii1I1Ii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 13 - 13: i1IiiiI1iI + O0Oooo0O - O0Oooo0O % OOOo00oo0oO / i1IiiiI1iI
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOoo0oOO00 = [ ]
  OOoo0oOO00 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OOoo0oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   OOoo0oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IioO0O . addContextMenuItems ( OOoo0oOO00 )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = True )
 return oo0O0o
if 4 - 4: oOo0O0Ooo + OoOo0o - I11i1ii1 + iiiiiiii1
if 78 - 78: i1iIi
if 29 - 29: IIiIiII11i
if 79 - 79: iI11I1II1I1I - Ii + oOOoOooOo - IIiIiII11i . iI11I1II1I1I
if 84 - 84: I1ii11iIi11i % i1IiiiI1iI * o0o00Oo0O * i1IiiiI1iI
if 66 - 66: OoOo0o / iI11I1II1I1I - iii1i1iiiiIi % o0o00Oo0O . oOOoOooOo
if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
if 37 - 37: ooOoO0O00 * Ii
if 95 - 95: Ii % O0Oooo0O * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + oOoO0o00OO0
if 7 - 7: oOo * Ii * iI11I1II1I1I / OoOo0o / O0Oooo0O
if 35 - 35: iiiiiiii1 * OoOo0o
if 65 - 65: IIiIiII11i % ooOoO0O00
if 13 - 13: oOo * O0Oooo0O + I1ii11iIi11i - I11i1ii1
if 31 - 31: oOo
if 68 - 68: oOo + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + oOoO0o00OO0
def Ooo00OoO ( string ) :
 if O00O0oOO00O00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 77 - 77: ii
def O00Ooo00 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 ooOoii = [ ]
 try :
  if 88 - 88: IIiIiII11i - iiiiiiii1 / ii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( oo0OooOOo0 ) == False :
  Ooo00OoO ( 'Making Favorites File' )
  ooOoii . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iII1ii1 = open ( oo0OooOOo0 , "w" )
  iII1ii1 . write ( json . dumps ( ooOoii ) )
  iII1ii1 . close ( )
 else :
  Ooo00OoO ( 'Appending Favorites' )
  iII1ii1 = open ( oo0OooOOo0 ) . read ( )
  ooOOOOOo = json . loads ( iII1ii1 )
  ooOOOOOo . append ( ( name , url , iconimage , fanart , mode ) )
  oO0o0ooooo = open ( oo0OooOOo0 , "w" )
  oO0o0ooooo . write ( json . dumps ( ooOOOOOo ) )
  oO0o0ooooo . close ( )
  if 3 - 3: Ii
  if 20 - 20: ooOoO0O00 * iiiiiiii1 + oOo * oOo / I1ii11iIi11i
def oO00Oo0OO ( ) :
 if os . path . exists ( oo0OooOOo0 ) == False :
  ooOoii = [ ]
  Ooo00OoO ( 'Making Favorites File' )
  ooOoii . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  iII1ii1 = open ( oo0OooOOo0 , "w" )
  iII1ii1 . write ( json . dumps ( ooOoii ) )
  iII1ii1 . close ( )
 else :
  i11iIIiii = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
  oOOoooo0O0 = len ( i11iIIiii )
  for O0o000Oo in i11iIIiii :
   O000OOO = O0o000Oo [ 0 ]
   IIo0o0O0O00oOOo = O0o000Oo [ 1 ]
   OO00OOoO0o = O0o000Oo [ 2 ]
   try :
    ii1iII1i111II = O0o000Oo [ 3 ]
    if ii1iII1i111II == None :
     raise
   except :
    if O0oo0OO0 . getSetting ( 'use_thumb' ) == "true" :
     ii1iII1i111II = OO00OOoO0o
    else :
     ii1iII1i111II = I1I1
   try : OoO00OOoO = O0o000Oo [ 5 ]
   except : OoO00OOoO = None
   try : iiiI = O0o000Oo [ 6 ]
   except : iiiI = None
   if 27 - 27: oOo0O0Ooo / ii
   if O0o000Oo [ 4 ] == 0 :
    o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , '' , OO00OOoO0o , I1I1 , '' , 'fav' )
   else :
    o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , O0o000Oo [ 4 ] , OO00OOoO0o , I1I1 , '' , 'fav' )
    if 74 - 74: oOoO0o00OO0 % O0Oooo0O - oOo * i1IiiiI1iI . ii * oOo
def OOOooooOo0 ( name ) :
 ooOOOOOo = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
 for i111iiIIII in range ( len ( ooOOOOOo ) ) :
  if ooOOOOOo [ i111iiIIII ] [ 0 ] == name :
   del ooOOOOOo [ i111iiIIII ]
   oO0o0ooooo = open ( oo0OooOOo0 , "w" )
   oO0o0ooooo . write ( json . dumps ( ooOOOOOo ) )
   oO0o0ooooo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 63 - 63: O0Oooo0O
 if 94 - 94: ooOoO0O00 % i1iIi % oOoO0o00OO0 - i1iIi * iI11I1II1I1I + iI11I1II1I1I
def O00oIi11Iiii1iiii ( ) :
 OOO00O0000 = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 o0Oo0OOOOoo = open ( OOO00O0000 , "w+" )
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oOOo0 )
 o0Oo0OOOOoo . write ( r'[' + o0OOO + ']' + '\n' )
 for O000OOO , Ii1IIiI1i , o0O00Oo0 , IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = ( IIo0o0O0O00oOOo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  oOi1IiIiIii11I = ( O000OOO + '=plugin://' + o0OOO + '/?url=' + IIo0o0O0O00oOOo + '&mode=10012&name=' + ( O000OOO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( Ii1IIiI1i ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( Ii1IIiI1i ) . replace ( ' ' , '' ) + '+&amp;description=' )
  o0Oo0OOOOoo . write ( oOi1IiIiIii11I + '\n' )
  if 80 - 80: O0Oooo0O + i1IiiiI1iI . O0Oooo0O + OoOo0o
  if 85 - 85: Ii . i1IiiiI1iI + i1iIi / i1iIi
def i1o00Oo ( ) :
 IIi = cloudflare . source ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 iI111i = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo in iI111i :
  IIII ( '24/7' , IIo0o0O0O00oOOo , 90021 , I1IIIii + '247Streams.png' )
  if 38 - 38: O0Oooo0O
def OOoO000oO ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + '247Streams.png' , I1IIIii + '247Streams.png' , '' )
def II111111 ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + 'musicch.png' , I1IIIii + 'musicch.png' , '' )
def O00OOII1Ii1iI1i1 ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + 'NEWS.png' , I1IIIii + 'NEWS.png' , '' )
def OOOoOooO000oO ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  O0O0ooOOO ( O000OOO , ( IIo0o0O0O00oOOo ) . strip ( ) , 222 , I1IIIii + 'adult.png' , I1IIIii + 'adult.png' , '' )
def iIiIi ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 iI111i = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  O0O0ooOOO ( O000OOO , IIo0o0O0O00oOOo , 1016 , I1IIIii + 'TUTS.png' , I1IIIii + 'TUTS.png' , '' )
  if 7 - 7: oOoO0o00OO0
  if 11 - 11: oOOoOooOo
def IIIiII1iIII ( ) :
 if 62 - 62: IIiIiII11i . oOOoOooOo + oOo % oOo - o0o00Oo0O - IIiIiII11i
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 if 22 - 22: i1iIi - I1ii11iIi11i % oOoO0o00OO0 % oOOoOooOo % I11i1ii1
def o00OoOoo0 ( ) :
 if 3 - 3: O0Oooo0O
 IIi = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO , IiI1ii1Ii in iI111i :
  o00oOOooOOo0o ( O000OOO + '  -  ' + ( IiI1ii1Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IIo0o0O0O00oOOo , 10023 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
  if 28 - 28: iI11I1II1I1I . o0o00Oo0O
  if 32 - 32: ii
  if 29 - 29: oOoO0o00OO0
def iI111iiI1II ( ) :
 if 96 - 96: iii1i1iiiiIi * o0o00Oo0O - IIiIiII11i . oOOoOooOo - i1iIi
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
 if 84 - 84: OOOo00oo0oO * ooo0O * ooo0O - iiiiiiii1
def III1Ii ( url ) :
 iIi1Ii1111i = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oOOo0 = cloudflare . source ( iIi1Ii1111i )
 iI111i = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10022 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
  if 90 - 90: oOo0O0Ooo
  if 27 - 27: iI11I1II1I1I - OOOo00oo0oO
  if 73 - 73: OoOo0o . I1ii11iIi11i + I1ii11iIi11i % I1ii11iIi11i % o0o00Oo0O
  if 8 - 8: iiiiiiii1 . i1iIi - ooOoO0O00 % oOo / i1IiiiI1iI
def IIiIiOoOOo ( ) :
 if 30 - 30: I11i1ii1 + i1IiiiI1iI % oOoO0o00OO0
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 IIo0o0O0O00oOOo = ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OOooo ) . replace ( ' ' , '+' )
 oOOo0 = cloudflare . source ( IIo0o0O0O00oOOo )
 iI111i = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  if OOooo in O000OOO . lower ( ) :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 10022 , I1IIIii + 'dtv.png' )
   if 44 - 44: i1iIi . Ii / i1iIi
   if 32 - 32: i1iIi + I11i1ii1 + oOoO0o00OO0
   if 79 - 79: ooOoO0O00 / i1iIi
def o0OO0oO0oOOOoo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , IiIiIi1I1 , oO00oOOo0Oo , O000OOO in iI111i :
  OooII11II1IIii = ( oO00oOOo0Oo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0O0OO = ( IiIiIi1I1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i1iIII11i1i = 'Season ' + o0O0OO + 'Episode ' + OooII11II1IIii + O000OOO
  O0o0O0O ( i1iIII11i1i , I1i )
  if 27 - 27: iiiiiiii1
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 8 - 8: o0o00Oo0O * ooOoO0O00 - iii1i1iiiiIi % oOo0O0Ooo / oOoO0o00OO0
  if 39 - 39: oOoO0o00OO0 . OOOo00oo0oO * IIiIiII11i + oOo0O0Ooo - iI11I1II1I1I
def O0o0O0O ( name , url ) :
 I1i = url
 O0O00o0O = name
 oo00O00oO = cloudflare . source ( I1i )
 IIi11i1i1iI1 = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oo00O00oO )
 for Ii11Iii , iIii1i1i1 in IIi11i1i1iI1 :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O0O00o0O + iIii1i1i1 + '[/COLOR]' , Ii11Iii , 222 , I1IIIii + 'dtv.png' )
  if 45 - 45: i1IiiiI1iI - OoOo0o * iiiiiiii1 - oOo . i1iIi
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: OOOo00oo0oO / i1IiiiI1iI
 if 49 - 49: I11i1ii1
def ii1i ( ) :
 if 56 - 56: o0o00Oo0O / i1IiiiI1iI + OoOo0o
 if 7 - 7: I1ii11iIi11i - Ii / OOOo00oo0oO / OOOo00oo0oO . ooOoO0O00 % i1IiiiI1iI
 if 51 - 51: OOOo00oo0oO
 if 23 - 23: Ii * I11i1ii1 * i1IiiiI1iI % i1IiiiI1iI - iii1i1iiiiIi + IIiIiII11i
 if 91 - 91: ii + O0Oooo0O / IIiIiII11i * iiiiiiii1 + ooo0O / I1ii11iIi11i
 if 7 - 7: i1IiiiI1iI / Ii - i1iIi % iiiiiiii1
 if 67 - 67: iI11I1II1I1I - iii1i1iiiiIi
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , '' , 10091 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 if 51 - 51: i1IiiiI1iI * oOoO0o00OO0 % oOoO0o00OO0 + ooo0O
def Ii1iIiIiIi ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oOOo0 )
 i1I = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + Ii1IIiI1i , '' , '' )
 for url in i1I :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , I1IIIii + 'Next.png' , '' , '' )
  if 75 - 75: IIiIiII11i / iiiiiiii1 * OOOo00oo0oO
def oOo0OO00O0O ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oOOo0 )
 i1I = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  Ii1IIiI1i = 'http://watchepisodes.cc/' + Ii1IIiI1i
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 10093 , Ii1IIiI1i , Ii1IIiI1i , '' )
 for url in i1I :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , I1IIIii + 'Next.png' , '' , '' )
  if 52 - 52: oOoO0o00OO0
def o0oI1 ( url , iconimage ) :
 Ii1IIiI1i = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oOOo0 )
 for oO00oOOo0Oo , url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + oO00oOOo0Oo + ' - ' + O000OOO + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , Ii1IIiI1i , '' , '' )
  if 39 - 39: O0Oooo0O . OOOo00oo0oO - OoOo0o
def OOoooO0 ( url , iconimage ) :
 Ii1IIiI1i = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  if 'player' in O000OOO :
   pass
  elif 'vod' in O000OOO :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , Ii1IIiI1i , '' , '' )
   if 29 - 29: oOoO0o00OO0 / OOOo00oo0oO * o0o00Oo0O - Ii - oOo + i1iIi
   if 86 - 86: oOo0O0Ooo / oOoO0o00OO0 * i1iIi % Ii
   if 20 - 20: iiiiiiii1 . ii + iiiiiiii1 + oOOoOooOo * oOoO0o00OO0
   if 44 - 44: Ii
   if 69 - 69: OoOo0o * o0o00Oo0O + Ii
   if 65 - 65: o0o00Oo0O / iiiiiiii1 . ooOoO0O00 * iiiiiiii1 / iI11I1II1I1I - OOOo00oo0oO
def OOOo00OOooO ( ) :
 if 57 - 57: OOOo00oo0oO . ooo0O % oOoO0o00OO0 - ooo0O
 if 64 - 64: ooo0O
 if 69 - 69: o0o00Oo0O % iiiiiiii1 . I1ii11iIi11i + iiiiiiii1
 if 57 - 57: oOoO0o00OO0 . O0Oooo0O . I11i1ii1 . I1ii11iIi11i % OOOo00oo0oO * oOoO0o00OO0
 if 84 - 84: oOOoOooOo . oOoO0o00OO0
 if 1 - 1: I1ii11iIi11i * o0o00Oo0O . oOo0O0Ooo + oOOoOooOo / iii1i1iiiiIi + i1IiiiI1iI
 if 68 - 68: IIiIiII11i
 if 61 - 61: OoOo0o . oOoO0o00OO0 * OOOo00oo0oO / O0Oooo0O - oOo
 if 18 - 18: O0Oooo0O
 if 34 - 34: iiiiiiii1 + O0Oooo0O * i1IiiiI1iI / IIiIiII11i
 if 14 - 14: IIiIiII11i + iiiiiiii1 + i1iIi / iiiiiiii1 . iI11I1II1I1I
 if 85 - 85: i1IiiiI1iI % i1IiiiI1iI . o0o00Oo0O
 if 40 - 40: oOo * iii1i1iiiiIi * iI11I1II1I1I / iii1i1iiiiIi * ii / oOoO0o00OO0
 if 33 - 33: Ii % ooo0O . iiiiiiii1 * OoOo0o / i1IiiiI1iI
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , I1IIIii + 'latest.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , I1IIIii + 'popular.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , I1IIIii + 'Genre.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , I1IIIii + 'series.png' , I1IIIii + 'WatchSeries.png' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , I1IIIii + 'Search.png' , I1IIIii + 'WatchSeries.png' , '' )
 if 25 - 25: oOo
 if 39 - 39: i1iIi * iii1i1iiiiIi + I1ii11iIi11i . OoOo0o - o0o00Oo0O * oOoO0o00OO0
def O0o0ooo00o00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 ooO0oOo0o = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ooO0oOo0o ) )
 for url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 6 - 6: Ii / oOo . Ii / oOOoOooOo
def IiI1Iii1iIIII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 87 - 87: IIiIiII11i . i1iIi * oOo
def OOoO00o00oo ( url ) :
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
  if 5 - 5: OOOo00oo0oO - ii / iii1i1iiiiIi
  if 30 - 30: i1IiiiI1iI % ooo0O + ooOoO0O00 * ii * oOo - IIiIiII11i
def ooO0000 ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ooo00O0OooOOO = 'http://www.watchseriesgo.to/search/' + OOooo . replace ( ' ' , '%20' )
 oOOo0 = i11111IIIII ( Ooo00O0OooOOO )
 iI111i = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'watch online' in O000OOO :
   pass
  else :
   print IIo0o0O0O00oOOo
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + IIo0o0O0O00oOOo , 10044 , Ii1IIiI1i , '' , '' )
   if 28 - 28: I1ii11iIi11i
   xbmcplugin . setContent ( IIIii1II1II , 'movies' )
   if 62 - 62: I1ii11iIi11i + ii / iiiiiiii1
def O0oO0O0ooo00o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO , oO00oOOo0Oo , i11i1ii1I in iI111i :
  iiO0O0o0oO0O00 = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oO00oOOo0Oo ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + iiO0O0o0oO0O00 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , Ii1IIiI1i , '' , i11i1ii1I )
  if 2 - 2: O0Oooo0O / OoOo0o
def Ii1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  iiO0O0o0oO0O00 = ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + iiO0O0o0oO0O00 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , I1IIIii + 'Next.png' , '' , '' )
  if 24 - 24: OoOo0o * ii . o0o00Oo0O . oOo . oOo0O0Ooo
def OooO00ooo0o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , Ii1IIiI1i , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , I1IIIii + 'Next.png' , '' , '' )
  if 97 - 97: IIiIiII11i % OOOo00oo0oO - IIiIiII11i . oOOoOooOo
def I1II11IIii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oOOo0 )
 ooO0oOo0o = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 for IiIiIi1I1 , oOoO0O0o in ooO0oOo0o :
  iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oOoO0O0o ) )
  for url , O000OOO in iI111i :
   iiO0O0o0oO0O00 = ( IiIiIi1I1 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + iiO0O0o0oO0O00 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I1IIIii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 76 - 76: Ii
class I11i1IiI1 ( ) :
 if 88 - 88: OoOo0o - o0o00Oo0O % ooo0O
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 63 - 63: oOOoOooOo * OOOo00oo0oO + oOOoOooOo * i1iIi + I1ii11iIi11i / oOoO0o00OO0
  iiO0O0o0oO0O00 = name
  self . Get_Sources ( IIo0o0O0O00oOOo , iiO0O0o0oO0O00 )
  if 15 - 15: o0o00Oo0O . oOoO0o00OO0 * oOoO0o00OO0
  if 65 - 65: O0Oooo0O + o0o00Oo0O % ooo0O
 def Get_Sources ( self , URL , season_name ) :
  o0oO0 = xbmcgui . DialogProgress ( )
  oOOo0 = i11111IIIII ( URL )
  iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , O000OOO in iI111i :
   URL = 'http://www.watchseriesgo.to/link/' + IIo0o0O0O00oOOo
   self . Get_site_link ( URL , season_name )
   if 72 - 72: OoOo0o . iii1i1iiiiIi / IIiIiII11i
 def Get_site_link ( self , url , season_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oOOo0 )
  iIIii = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oOOo0 )
  for url in iI111i :
   self . main ( url , season_name )
  for url in IIi11i1i1iI1 :
   self . main ( url , season_name )
  for url in iIIii :
   self . main ( url , season_name )
   if 69 - 69: OoOo0o * IIiIiII11i - oOOoOooOo - ooOoO0O00 + Ii
 def main ( self , url , season_name ) :
  o0oO0 . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iiiiI1iiIi1i = 'DACLIPS'
   if iiiiI1iiIi1i in I11i1IiI1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , iiiiI1iiIi1i )
    o0oO0 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    iiiiI1iiIi1i = 'THEVIDEO'
    if iiiiI1iiIi1i in I11i1IiI1 . source_list :
     pass
    else :
     self . thevideo ( url , season_name , iiiiI1iiIi1i )
     o0oO0 . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     iiiiI1iiIi1i = 'ALLMYVIDEOS'
     if iiiiI1iiIi1i in I11i1IiI1 . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , iiiiI1iiIi1i )
      o0oO0 . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      iiiiI1iiIi1i = 'VIDSPOT'
      if iiiiI1iiIi1i in I11i1IiI1 . source_list :
       pass
      else :
       self . vidspot ( url , season_name , iiiiI1iiIi1i )
       o0oO0 . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       iiiiI1iiIi1i = 'VODLOCKER'
       if iiiiI1iiIi1i in I11i1IiI1 . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , iiiiI1iiIi1i )
        o0oO0 . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        iiiiI1iiIi1i = 'VIDTO'
        if iiiiI1iiIi1i in I11i1IiI1 . source_list :
         pass
        else :
         self . vidto ( url , season_name , iiiiI1iiIi1i )
         o0oO0 . update ( 0 , "" , "Getting Vidto Links" )
         if 11 - 11: o0o00Oo0O / O0Oooo0O / iI11I1II1I1I % i1iIi
       else :
        if 'youwatch' in url :
         iiiiI1iiIi1i = 'YouWatch'
         if iiiiI1iiIi1i in I11i1IiI1 . source_list :
          pass
         else :
          self . youwatch ( url , season_name , iiiiI1iiIi1i )
          o0oO0 . update ( 0 , "" , "Getting YouWatch Links" )
          if 31 - 31: i1IiiiI1iI . Ii . oOo * I1ii11iIi11i % i1iIi . ooo0O
          if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
 def allmyvid ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  for OOii111IiiI1 , O000OOO in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
   if 93 - 93: oOOoOooOo % O0Oooo0O
 def vidspot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oOOo0 )
  for OOii111IiiI1 , O000OOO in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
   if 46 - 46: oOoO0o00OO0 * iii1i1iiiiIi * I11i1ii1 * oOoO0o00OO0 . oOoO0o00OO0
 def thevideo ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{"file":"([^"]*)"' ) . findall ( oOOo0 )
  for OOii111IiiI1 in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
   if 43 - 43: oOOoOooOo . ooOoO0O00
 def vodlocker ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for OOii111IiiI1 in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
   if 68 - 68: I11i1ii1 % I1ii11iIi11i . o0o00Oo0O - iii1i1iiiiIi + oOoO0o00OO0 . Ii
 def daclips ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oOOo0 )
  for OOii111IiiI1 in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
   if 45 - 45: oOo0O0Ooo
 def filehoot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for OOii111IiiI1 in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for OOii111IiiI1 in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
  for OOii111IiiI1 in iI111i :
   self . youplay ( OOii111IiiI1 , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for OOii111IiiI1 in iI111i :
   self . Printer ( OOii111IiiI1 , season_name , source_name )
   if 17 - 17: ii - oOOoOooOo + i1iIi . ii % I1ii11iIi11i
 def Printer ( self , Link , season_name , source_name ) :
  if 92 - 92: O0Oooo0O - OoOo0o % oOo - ooo0O % ooOoO0O00
  if Link in I11i1IiI1 . List :
   pass
  elif source_name in I11i1IiI1 . source_list :
   pass
  else :
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 222 , I1IIIii + 'WATCHSERIES.png' )
   o0oO0 . update ( 100 , "" , "Got Source" )
   I11i1IiI1 . List . append ( Link )
   I11i1IiI1 . source_list . append ( source_name )
   if 38 - 38: oOoO0o00OO0 . i1IiiiI1iI / iii1i1iiiiIi % i1IiiiI1iI
   xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 10 - 10: o0o00Oo0O . oOo0O0Ooo * ooo0O / iiiiiiii1
   if 61 - 61: I1ii11iIi11i - O0Oooo0O
   if 51 - 51: iiiiiiii1 * oOOoOooOo / o0o00Oo0O / o0o00Oo0O
   if 52 - 52: ii % o0o00Oo0O
   if 56 - 56: OOOo00oo0oO - ooOoO0O00 * ii - IIiIiII11i
def IIiiii ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , I1IIIii + 'Highlights.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , I1IIIii + 'Fixtures.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , I1IIIii + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 28 - 28: ooOoO0O00 / i1IiiiI1iI . ooo0O
def iIIiiiIiiii11 ( url ) :
 iI1i1i1i1i = '20'
 iiII1i1II1iIi = [ ]
 iIIOOOO0o0Oo0 = '                                                    '
 I1iIiI1iiI = '        '
 o00oOOooOOo0o ( iIIOOOO0o0Oo0 + 'pl' + I1iIiI1iiI + 'w' + I1iIiI1iiI + 'd' + I1iIiI1iiI + 'l' + I1iIiI1iiI + 'f' + I1iIiI1iiI + 'a' + I1iIiI1iiI + 'pts' , '' , '' , '' , '' , '' )
 IIi = II1i11i1iIi11 ( url )
 iI111i = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( IIi )
 for oO000O00 , IiIIIii1iIII1 , OoOo , o0o0oo0OOo0O0 , oooo0oo , Iiii1iI1i , iII1ii1 , ii1II1 , i1I1II11I1 in iI111i :
  oo0o = OoOoo ( IiIIIii1iIII1 )
  O0oOoOooo00oo = OoOoo ( OoOo )
  OOO0OO00 = OoOoo ( o0o0oo0OOo0O0 )
  oOO00 = OoOoo ( oooo0oo )
  II1IiII1I1II = OoOoo ( Iiii1iI1i )
  oooO = OoOoo ( iII1ii1 )
  iiII1i1II1iIi . append ( oO000O00 [ 0 ] )
  II111iiI1Ii1 = len ( iiII1i1II1iIi )
  oo0oO0oO00oO = int ( len ( iIIOOOO0o0Oo0 ) - len ( oO000O00 ) - 2 )
  if len ( iiII1i1II1iIi ) >= 10 :
   oo0oO0oO00oO = oo0oO0oO00oO - 1
  if len ( iiII1i1II1iIi ) <= int ( iI1i1i1i1i ) :
   O0O0ooOOO ( str ( II111iiI1Ii1 ) + ' ' + oO000O00 + iIIOOOO0o0Oo0 [ 0 : oo0oO0oO00oO ] + IiIIIii1iIII1 + oo0o + OoOo + O0oOoOooo00oo + o0o0oo0OOo0O0 + OOO0OO00 + oooo0oo + oOO00 + Iiii1iI1i + II1IiII1I1II + iII1ii1 + oooO + ' ' + i1I1II11I1 , '' , '' , '' , '' , '' )
   if 94 - 94: oOOoOooOo * OoOo0o
   if 59 - 59: O0Oooo0O * iiiiiiii1
def OoOoo ( space ) :
 if len ( space ) > 1 :
  ii1i1Iii = len ( '        ' ) - len ( space ) + 1
  space = int ( ii1i1Iii ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 31 - 31: i1IiiiI1iI / o0o00Oo0O
def oo00oO0o000 ( ) :
 if 15 - 15: I1ii11iIi11i
 if 55 - 55: O0Oooo0O
 if 29 - 29: I1ii11iIi11i
 if 97 - 97: oOo * O0Oooo0O
 if 80 - 80: OoOo0o * OoOo0o
 if 5 - 5: ii - iiiiiiii1 - Ii
 if 53 - 53: iiiiiiii1 * oOo / oOoO0o00OO0 + oOo0O0Ooo + ii
 if 47 - 47: O0Oooo0O
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
 if 26 - 26: OoOo0o . oOo % iii1i1iiiiIi
 if 94 - 94: I11i1ii1
 if 15 - 15: i1iIi - I11i1ii1 / o0o00Oo0O
 if 28 - 28: O0Oooo0O . ooOoO0O00 / oOoO0o00OO0
 if 77 - 77: Ii / O0Oooo0O / Ii % iii1i1iiiiIi - O0Oooo0O
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iI111i = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IIo0o0O0O00oOOo , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Ii1IIiI1i , Oo00OOOOO , '' )
  if 80 - 80: O0Oooo0O % iii1i1iiiiIi . ii . IIiIiII11i % I11i1ii1
def I1i1I1i1I1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 ooO0oOo0o = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oOOo0 )
 for ooO0oOo0o in ooO0oOo0o :
  oOO = re . compile ( '(.*?)</h2>' ) . findall ( str ( ooO0oOo0o ) )
  for i1IOO in oOO :
   i1IOO = i1IOO
  ooo0OiII1iii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ooO0oOo0o ) )
  for I1I1I1 , Ii1IIiI1i , time , Oo0OO0ooO0O0O in ooo0OiII1iii :
   ooo = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( Oo0OO0ooO0O0O )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1IOO + ' - ' + I1I1I1 + ' - ' + time + '[/COLOR]' , '' , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + Ii1IIiI1i , Oo00OOOOO , ( str ( ooo ) ) )
   if 76 - 76: ooo0O / i1IiiiI1iI
 iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if 95 - 95: iii1i1iiiiIi - o0o00Oo0O % ii
def iIo0O00o00o0 ( ) :
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
 if 87 - 87: i1iIi % oOoO0o00OO0 * I1ii11iIi11i
def OOO00i111 ( url ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  Ii1i = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in O000OOO :
   pass
  else :
   Ii1i = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + Ii1i + '[/COLOR]' , url , 10013 , Ii1IIiI1i )
 for url , Ii1IIiI1i , O000OOO in IIi11i1i1iI1 :
  Ii1i = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in O000OOO :
   pass
  else :
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + Ii1i + '[/COLOR]' , url , 10013 , Ii1IIiI1i )
def i1i1I111iI ( url ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 if 20 - 20: oOo / Ii * ooo0O - oOoO0o00OO0 - IIiIiII11i / Ii
 if 17 - 17: I1ii11iIi11i - oOo0O0Ooo - I11i1ii1 - OoOo0o / OOOo00oo0oO + O0Oooo0O
 if 40 - 40: O0Oooo0O / oOo0O0Ooo - ii / O0Oooo0O
 if 48 - 48: I1ii11iIi11i . oOo . oOo0O0Ooo * iiiiiiii1 . iI11I1II1I1I
 if 66 - 66: ii * o0o00Oo0O / oOOoOooOo * i1iIi
 if 22 - 22: oOo0O0Ooo
 if 76 - 76: oOo + i1IiiiI1iI + oOo . i1IiiiI1iI % OoOo0o
 for url , Ii1IIiI1i , O000OOO in IIi11i1i1iI1 :
  Ii1i = O000OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in O000OOO :
   pass
  else :
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + Ii1i + '[/COLOR]' , url , 10013 , Ii1IIiI1i )
   if 96 - 96: I1ii11iIi11i
def iIIiiiI1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oOOo0 )
 for Ii11Iii in iI111i :
  i11i1i1i = ( Ii11Iii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  i1i1I1 ( 'http:' + i11i1i1i )
  if 83 - 83: IIiIiII11i + I11i1ii1 - ooo0O % ooo0O * ooo0O
  if 100 - 100: i1iIi . iI11I1II1I1I
  if 33 - 33: oOo0O0Ooo . iI11I1II1I1I / Ii * i1iIi
  if 18 - 18: iii1i1iiiiIi * iii1i1iiiiIi - ooo0O % oOOoOooOo % IIiIiII11i - I11i1ii1
def OOoi1Iiiiiii ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( IIi )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  iI1iiiIiii ( O000OOO , url , 8046 , Ii1IIiI1i )
 for url in IIi11i1i1iI1 :
  IIII ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , I1IIIii + 'Next.png' )
def Oo000O00o0O ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( IIi )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  i1i1I1 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 83 - 83: oOOoOooOo - OoOo0o / o0o00Oo0O
def IIio0 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( IIi )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 17 - 17: Ii
def OOoiIIiiIIIi1I ( ) :
 IIII ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , I1IIIii + 'documentary.png' )
 IIII ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , I1IIIii + 'documentary.png' )
 IIII ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , I1IIIii + 'Search.png' )
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( O000OOO , IIo0o0O0O00oOOo , 8041 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoO0oOoo ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( IIi )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( IIi )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + Ii1IIiI1i )
 for url in next :
  IIII ( 'NEXT PAGE' , url , 8041 , I1IIIii + 'Next.png' )
  if 25 - 25: i1IiiiI1iI / oOoO0o00OO0 * oOo . iiiiiiii1
  if 18 - 18: o0o00Oo0O % ooo0O + iiiiiiii1 + O0Oooo0O % I11i1ii1
def I1I111i1I1II ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIi )
 for url in iI111i :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
  else :
   IIII ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def O00oOoO0o0oO ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( IIi )
 for O000OOO , url in iI111i :
  url = ( url ) . replace ( '\/' , '/' )
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , '' )
  if 80 - 80: OOOo00oo0oO / o0o00Oo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo00oO000o0O ( name , url ) :
 IIIIi1I = 0
 name = name
 url = url
 I11iIi1i1II11 = [ '144' , '240' , '380' , '480' , '720' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  oo0 ( url )
  if 11 - 11: i1iIi / iii1i1iiiiIi - oOo + iii1i1iiiiIi
  if 51 - 51: oOOoOooOo
  if 42 - 42: ooo0O - OoOo0o / OoOo0o / iiiiiiii1 * I1ii11iIi11i . I1ii11iIi11i
  if 96 - 96: ii + oOoO0o00OO0 * o0o00Oo0O
  if 33 - 33: oOoO0o00OO0 - I11i1ii1
  if 17 - 17: OoOo0o - OOOo00oo0oO
  if 1 - 1: iI11I1II1I1I / Ii * IIiIiII11i
  if 48 - 48: oOoO0o00OO0 + o0o00Oo0O * OOOo00oo0oO + oOoO0o00OO0 + oOoO0o00OO0
def ooOOOOoO00 ( ) :
 IIi = II11iIII1i1I ( 'http://documentarylovers.com/' )
 iI111i = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  if 'genre' in IIo0o0O0O00oOOo :
   IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , IIo0o0O0O00oOOo , 80010 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO0OOO ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( IIi )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( IIi )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , Ii1IIiI1i )
 for url in next :
  IIII ( 'NEXT PAGE' , url , 80010 , I1IIIii + 'Next.png' )
  if 81 - 81: I1ii11iIi11i
def Oo0oO ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( IIi )
 for url in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
 for url in IIi11i1i1iI1 :
  O00oOoO0o0oO ( url )
  if 81 - 81: ii / oOOoOooOo * iI11I1II1I1I . I1ii11iIi11i + OOOo00oo0oO / o0o00Oo0O
def ooO0o0Oo ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO = 'http://documentarylovers.com/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 IIIiIiI = O0OO . lower ( )
 ooO0OOO ( IIIiIiI )
 if 67 - 67: iii1i1iiiiIi
def OOO0o0oo00 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  if 'films' in url :
   IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , I1IIIii + 'documentary.png' )
def o000 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( IIi )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  if 'films' in url :
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + Ii1IIiI1i )
 for url in IIi11i1i1iI1 :
  IIII ( 'NEXT' , url , 8049 , I1IIIii + 'Next.png' )
def IIIi1IiI1iII ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIi )
 for url in iI111i :
  if 'rtd' in url :
   OOOO0oo ( url )
   if 48 - 48: Ii - i1iIi . oOo
def OOOO0oo ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( IIi )
 for IIIi1I1IIii1II , file in iI111i :
  url = ( 'https://rtd.rt.com' + IIIi1I1IIii1II + file )
  oo0 ( url )
  if 89 - 89: ooOoO0O00
  if 92 - 92: iI11I1II1I1I * oOoO0o00OO0
def i1I11Iiii ( ) :
 oOOo0 = II11iIII1i1I ( 'http://www.stream2watch.co/live-tv' )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO , iIIIiIi in iI111i :
  IIII ( ( O000OOO + '[COLOR' + iiI1IiI + ']' + iIIIiIi + '[/COLOR]' ) , IIo0o0O0O00oOOo , 8086 , Ii1IIiI1i )
  if 78 - 78: O0Oooo0O
def ooOo0oO ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 8087 , Ii1IIiI1i )
  if 34 - 34: OoOo0o - oOo
def iII1iII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  iiii11i1ii1 ( url , O000OOO )
  if 90 - 90: i1IiiiI1iI
def iiii11i1ii1 ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  print url
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 40 - 40: O0Oooo0O * i1IiiiI1iI . O0Oooo0O + OOOo00oo0oO
def o0Ooo0OoO ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + IIo0o0O0O00oOOo , 3002 , 'http://www.solie.org/alibrary/' + Ii1IIiI1i )
def I1iI1i ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIi )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + Ii1IIiI1i )
def iIIiiI1II ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( IIi )
 i11i1IIi = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( IIi )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIi )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , I1IIIii + 'classicmovies.png' )
 for url , O000OOO in i11i1IIi :
  IIII ( '[COLOR' + iiI1IiI + ']Season- ' + O000OOO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'classicmovies.png' )
 for url in next :
  IIII ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'Next.png' )
 for url , Ii1IIiI1i , O000OOO in IIi11i1i1iI1 :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + Ii1IIiI1i )
def Oo0o ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIi )
 for url in iI111i :
  iiiii11i ( url )
def iiiii11i ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( IIi )
 for url in iI111i :
  oo0 ( url )
  if 65 - 65: oOo * iii1i1iiiiIi . ii - o0o00Oo0O * iii1i1iiiiIi % iii1i1iiiiIi
def I1iii ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IIo0o0O0O00oOOo , 8065 , I1IIIii + 'classicmovies.png' )
def IiiiIii ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( "v.src = '([^']*)';" ) . findall ( IIi )
 for url in iI111i :
  II11IiI1 ( url )
  if 67 - 67: iii1i1iiiiIi % ooo0O % oOoO0o00OO0 . oOo . IIiIiII11i + I11i1ii1
def IiiI11i1I ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IIo0o0O0O00oOOo , 8065 , I1IIIii + 'classictv.png' )
def IIi1Iii ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  if 'mp4' in url :
   oo0 ( url )
 for url in IIi11i1i1iI1 :
  yt . PlayVideo ( url )
  if 21 - 21: oOoO0o00OO0 - OOOo00oo0oO * oOo
def oO00oOOOO ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iI111i = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + IIo0o0O0O00oOOo , 8071 , I1IIIii + 'streams.png' )
def o0o0OOO0ooo00 ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for O000OOO , url in iI111i :
  if '(Free Access)' in O000OOO :
   url = ( url ) . strip ( )
  else :
   url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , I1IIIii + 'streams.png' )
def I11III111i1I ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , O000OOO , url in iI111i :
  url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , Ii1IIiI1i , I1I1 , '' )
  if 52 - 52: iiiiiiii1 % iI11I1II1I1I . oOoO0o00OO0 + OOOo00oo0oO % iiiiiiii1 * iiiiiiii1
def o0IiIiI111IIII1 ( ) :
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  oO0OoooO ( 'http://watchxxxfree.com/categories' )
 if iiI == 1 :
  I111iI1IIIi1I ( 'http://www.perfectgirls.net' )
 if iiI == 2 :
  I1iii1IIi1I ( 'http://www.xvideos.com/best' )
 if iiI == 3 :
  oO00O00OOOo ( 'http://www.xvideos.com/best' )
 if iiI == 4 :
  I1iii1IIi1I ( 'http://www.xvideos.com/best' )
 if iiI == 5 :
  I1iii1IIi1I ( 'http://www.xvideos.com/verified/videos' )
 if iiI == 6 :
  Oo0o0oO00 ( 'http://www.xvideos.com/tags' )
 if iiI == 7 :
  I1i1i1iiIi1 ( 'http://www.xvideos.com/porn' )
 if iiI == 8 :
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
def OO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  if 'ch' in url :
   iiiI1ii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Jizbox.png' , I1IIIii + 'Jizbox.png' , '' )
def i1i1Ii1iiII1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 IIIII11IIi = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oOOo0 )
 for url , O000OOO in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , I1IIIii + 'Jizbox.png' , '' , '' )
 for O000OOO , url in IIIII11IIi :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Next.png' , '' , '' )
def i11I1iiI1iI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   i1i11 ( url )
def OoOO0o000000 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  oo0 ( url )
def oO0OoooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO , ii1i1Iii in iI111i :
  if 'category' in url :
   iiiI1ii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORorange]   ' + ii1i1Iii + '[/COLOR]' , url , 90006 , Ii1IIiI1i , I1IIIii + 'Jizbox.png' , '' )
def O0oooOOoOOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 IIIII11IIi = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , Ii1IIiI1i , '' , '' )
 for url in IIIII11IIi :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , url , 90006 , I1IIIii + 'Next.png' , '' , '' )
def OoO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   i1i11 ( url )
def i1i11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  oo0 ( url )
def I111iI1IIIi1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , ii1i1Iii in iI111i :
  if 'category' in url :
   iiiI1ii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORorange]' + ii1i1Iii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , I1IIIii + 'Jizbox.png' , '' , '' )
def I1Ioo000oooooooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 I1i = url
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIIII11IIi = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , Ii1IIiI1i , '' , '' )
 for url in IIIII11IIi :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , I1i + '/' + url , 90003 , I1IIIii + 'Next.png' , '' , '' )
def II1IIi1ii111 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'get\("(.*)", function' ) . findall ( oOOo0 )
 for url in iI111i :
  II1 ( 'http://www.perfectgirls.net' + url )
def II1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'http://(.+?)\n' ) . findall ( oOOo0 )
 for url in iI111i :
  i1i1I1 ( 'http://' + url )
def I1i1i1iiIi1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oOOo0 )
 for url , O000OOO , ii1i1Iii in iI111i :
  iiiI1ii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgreen] - No of Videos : [COLORorange]' + ii1i1Iii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
def Oo0o0oO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIII11IIi = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in IIIII11IIi :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , I1IIIii + 'Jizbox.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oOOo0 )
 for url , O000OOO , ii1i1Iii in iI111i :
  iiiI1ii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgreen] - No of Videos : [COLORorange]' + ( ii1i1Iii + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
  if 85 - 85: iii1i1iiiiIi . o0o00Oo0O - iI11I1II1I1I - i1iIi
def o0O000Ooo ( url ) :
 oOOo0 = i11111IIIII ( url )
 IIIII11IIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in IIIII11IIi :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO , I1III1I1IiI in iI111i :
  iiiI1ii ( O000OOO + '--' + ( I1III1I1IiI ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( Ii1IIiI1i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 8 - 8: iI11I1II1I1I / IIiIiII11i / I11i1ii1
  if 65 - 65: iI11I1II1I1I + iiiiiiii1
def I1iii1IIi1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO , oo0ooOoOOoO , Iii1I in iI111i :
  iiiI1ii ( '[COLORorangered]' + O000OOO + '[COLORgreen] - Porn Quality : [COLORorange]' + oo0ooOoOOoO + ' - [COLORred]' + Iii1I + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , Ii1IIiI1i , Ii1IIiI1i , oo0ooOoOOoO + ' - ' + Iii1I )
 iI1iIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for Ii1IIiI1i , url , O000OOO , Iii1I in IIi11i1i1iI1 :
  iiiI1ii ( '[COLORorangered]' + O000OOO + '[COLORgreen] - Porn Quality : [COLORorange]' + Iii1I + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , Ii1IIiI1i , Ii1IIiI1i , Iii1I )
 iI1iIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in iI1iIi :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Next.png' , '' , '' )
  if 40 - 40: O0Oooo0O / Ii . i1iIi - I11i1ii1 / oOo
  if 14 - 14: oOOoOooOo / Ii - OOOo00oo0oO + Ii
def oO00O00OOOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 ooO0oOo0o = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 IIIII11IIi = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in IIIII11IIi :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ooO0oOo0o ) )
 for url , O000OOO in iI111i :
  if '/c/' in url :
   iiiI1ii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
   if 10 - 10: i1iIi + oOOoOooOo
   if 3 - 3: o0o00Oo0O - Ii % iii1i1iiiiIi
def OoOoo0ooO0000 ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiI1IIi = ( OOooo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IIIiIiI = iIiI1IIi . lower ( )
 i1II11III = 'http://www.xvideos.com/?k=' + IIIiIiI
 print i1II11III + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOo0 = i11111IIIII ( i1II11III )
 iI111i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , IIo0o0O0O00oOOo , O000OOO , Iii1I , I1111 in iI111i :
  iiiI1ii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgreen] - Porn Quality : [COLORorange]' + I1111 + ' - [COLORred]' + Iii1I + '[/COLOR]' , 'http://www.xvideos.com' + IIo0o0O0O00oOOo , 10108 , Ii1IIiI1i , Ii1IIiI1i , I1111 + ' - ' + Iii1I )
 iI1iIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in iI1iIi :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + IIo0o0O0O00oOOo , 10105 , I1IIIii + 'Next.png' , '' , '' )
if 100 - 100: ii
if 81 - 81: Ii + ooOoO0O00 / oOOoOooOo . i1iIi % i1iIi / O0Oooo0O
if 19 - 19: OOOo00oo0oO
if 2 - 2: oOoO0o00OO0 / iI11I1II1I1I % i1IiiiI1iI
if 94 - 94: oOo0O0Ooo - i1iIi % ii + ooOoO0O00 - ii
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
def i1iiIiiIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oOOo0 )
 iIIii = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  if 'http' in url :
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in IIi11i1i1iI1 :
  if 'http' in url :
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in iIIii :
  if 'http' in url :
   iI1iiiIiii ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
   if 9 - 9: iii1i1iiiiIi - i1IiiiI1iI . ii % oOOoOooOo
def IIIiIiIIII1i1 ( url ) :
 Oo00o000oOO = xbmc . Player ( ii1i1iiI ( ) )
 import urlresolver
 try : Oo00o000oOO . play ( url )
 except : pass
 if 90 - 90: oOo0O0Ooo % oOOoOooOo % ii / oOo . I11i1ii1 * IIiIiII11i
 if 83 - 83: OOOo00oo0oO
def i1Ii1Ii ( ) :
 if 24 - 24: iii1i1iiiiIi + ii + i1iIi * i1IiiiI1iI
 if 13 - 13: I1ii11iIi11i * ooo0O * iiiiiiii1
 if 71 - 71: OoOo0o + ii + iI11I1II1I1I
 if 99 - 99: oOo - I11i1ii1 * I11i1ii1 + OOOo00oo0oO / iiiiiiii1 + OoOo0o
 if 58 - 58: Ii + iI11I1II1I1I * ooo0O - iii1i1iiiiIi
 if 31 - 31: ooOoO0O00
 if 87 - 87: oOo0O0Ooo / i1IiiiI1iI + ii + o0o00Oo0O . i1iIi
 if 44 - 44: I1ii11iIi11i % I1ii11iIi11i
 if 58 - 58: OoOo0o * IIiIiII11i
 if 29 - 29: iI11I1II1I1I % iii1i1iiiiIi % oOoO0o00OO0 / iii1i1iiiiIi - Ii
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 8091 , I1IIIii + 'gofish.png' )
def o00OOOo0O0O0o0 ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 8092 , Ii1IIiI1i )
 for url in next :
  IIII ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
def Oo0ooo0oOo0Oo0O ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 II1ii1iI1I1i = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i in II1ii1iI1I1i :
  Ii1IIiI1i = Ii1IIiI1i
 for url , O000OOO in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 8092 , Ii1IIiI1i )
 for url in next :
  IIII ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
  if 9 - 9: ooOoO0O00 * O0Oooo0O
def i11oO0oOO000 ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( "videoId: '([^']*)'," ) . findall ( oOOo0 )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 69 - 69: o0o00Oo0O % o0o00Oo0O - iiiiiiii1 - OOOo00oo0oO
  if 83 - 83: Ii + iI11I1II1I1I
  if 21 - 21: ooo0O / Ii % O0Oooo0O
  if 56 - 56: ooo0O * iI11I1II1I1I . i1iIi + iii1i1iiiiIi % O0Oooo0O
iiI1i111I1 = '{PQ},' ; iiIi11i1I1 = '{SC},' ; o0OoO0 = '{XG},' ; I11Ii1I1I = '{JP},' ; oo00OO0o0 = '{HW},' ; o0oo0000Oo = '{RT},'
def O00OOooo0Ooo ( ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 OO0O00O = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 IIo0o0O0O00oOOo = 'http://onlinemovies.tube/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 I1i = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 iiIiIIII1iiIIi = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1I1IiI1ii = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 O00OOoOOOO00O = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Ooo0OOO = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooooOoo0OO = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OOooo
 Oo0 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 O0000Oo00o = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 93 - 93: oOOoOooOo + oOOoOooOo
 o00iIiiiII = ( o0oOoO00o ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 Ii1I1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 65 - 65: ii * i1IiiiI1iI * OOOo00oo0oO % oOoO0o00OO0 * IIiIiII11i
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 oo00O00oO = i1Oo00 ( I1i )
 o0oO0 . update ( 14 , "" , "Checking Source Technica " )
 iIIi1Ii1III = i1Oo00 ( I1i )
 o0oO0 . update ( 32 , "" , "Checking Source Pandoras Box " )
 iIiIIIi = i1Oo00 ( iiIiIIII1iiIIi )
 o0oO0 . update ( 59 , "" , "Checking Source Lazy List " )
 ooo00OOOooO = i1Oo00 ( i1I1IiI1ii )
 o0oO0 . update ( 72 , "" , "Checking Source RaizTv " )
 Oooo00 = i1Oo00 ( O0000Oo00o )
 o0oO0 . update ( 91 , "" , "Checking WebSpace " )
 i1I111Ii = i1Oo00 ( Ii1I1 )
 o0oO0 . update ( 97 , "" , "Matching Results" )
 if 86 - 86: Ii / i1IiiiI1iI * iiiiiiii1 - iiiiiiii1
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for IIo0o0O0O00oOOo , O000OOO in II1iI :
   Ii1IiI1III11 = i1Oo00 ( IIo0o0O0O00oOOo )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , iIIIiIi in I1IIII1i1 :
    iIIIiIi = ( iIIIiIi . replace ( '.' , ' ' ) )
    if IIIiIiI in iIIIiIi . lower ( ) :
     if '.mkv' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + oOO0 , 222 , '' , '' , '' )
     elif '.mp4' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + oOO0 , 222 , '' , '' , '' )
     elif '.avi' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + oOO0 , 222 , '' , '' , '' )
     elif '.wav' in oOO0 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + oOO0 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + oOO0 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting WebSpace Links" )
      if 32 - 32: I1ii11iIi11i . o0o00Oo0O
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in IIi11i1i1iI1 :
   if OOooo in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source Technica[/COLOR]' ) , IIo0o0O0O00oOOo , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 48 - 48: oOoO0o00OO0 % IIiIiII11i + i1IiiiI1iI
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: I11i1ii1 * ooo0O / oOo0O0Ooo . I11i1ii1 % IIiIiII11i
 if iIiIIIi != 'Failed' :
  iIIii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for O0OOo0o , O000OOO in iIIii :
   if OOooo in O000OOO . lower ( ) :
    IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiIiIIII1iiIIi + O0OOo0o ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Lazy List Links" )
 if ooo00OOOooO != 'Failed' :
  o00O0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in o00O0O :
   if OOooo in O000OOO . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORred] source RaizTv[/COLOR]' ) , IIo0o0O0O00oOOo , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 50 - 50: iii1i1iiiiIi * iiiiiiii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 Ooo00O0 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for IIIIIIi1i in Ooo00O0 :
  iiiii11I1 = Ii1iIiII1ii1 + '/Movies/a.to.z/' + IIIIIIi1i + '.php'
  Oooo00 = i1Oo00 ( iiiii11I1 )
  if Oooo00 != 'Failed' :
   II1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oooo00 )
   for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in II1iI :
    if OOooo in O000OOO . lower ( ) :
     if '.php' in IIo0o0O0O00oOOo :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      o00oOOooOOo0o ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 426 , OO00OOoO0o , i1III1 , i11i1ii1I )
     else :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      i1IIIo00oOOO ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
      if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / i1IiiiI1iI
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
      if 92 - 92: ooo0O
 Ooo00O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 8 - 8: iiiiiiii1 + oOoO0o00OO0 . i1iIi
 if 50 - 50: I1ii11iIi11i
 for IIIIIIi1i in Ooo00O0 :
  iiiii11I1 = OO0O00O + IIIIIIi1i
  O00oo00oOOO0o = i1Oo00 ( iiiii11I1 )
  if O00oo00oOOO0o != 'Failed' :
   Iii1I1111ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O00oo00oOOO0o )
   for O0OOo0o , O000OOO in Iii1I1111ii :
    if OOooo in O000OOO . lower ( ) :
     iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OO0O00O + IIIIIIi1i + O0OOo0o ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 16 - 16: i1iIi - iii1i1iiiiIi % I1ii11iIi11i / i1iIi . i1IiiiI1iI + oOOoOooOo
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 78 - 78: iI11I1II1I1I + oOo + Ii
def oOO0OOOOoooO ( ) :
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
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 if 6 - 6: I1ii11iIi11i % OOOo00oo0oO * oOOoOooOo - ooOoO0O00 . iii1i1iiiiIi
 if 20 - 20: I1ii11iIi11i / O0Oooo0O . I1ii11iIi11i
 oOO0 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OOooo ) . replace ( ' ' , '+' )
 I1i = 'http://onlinemovies.tube/?s=' + ( OOooo ) . replace ( ' ' , '+' )
 iiIiIIII1iiIIi = ( o0oOoO00o ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1I1IiI1ii = ( o0oOoO00o ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 Ooo0OOO = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 ooooOoo0OO = 'http://www.tvmaze.com/search?q=' + ( OOooo ) . replace ( ' ' , '+' )
 Oo0 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 O0000Oo00o = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 60 - 60: oOoO0o00OO0 - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . iii1i1iiiiIi
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 24 - 24: I11i1ii1 * oOo0O0Ooo / OoOo0o
 o0oO0 . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 51 - 51: iI11I1II1I1I / i1IiiiI1iI * oOo * i1iIi + oOoO0o00OO0 . ii
 if 75 - 75: I11i1ii1 / ii / o0o00Oo0O % OoOo0o
 Ii11iiI = i1Oo00 ( oOO0 )
 o0oO0 . update ( 14 , "" , "Checking Source 3/11 Links" )
 oo00O00oO = i1Oo00 ( I1i )
 o0oO0 . update ( 28 , "" , "Checking Source 4/11 Links" )
 iIiIIIi = i1Oo00 ( iiIiIIII1iiIIi )
 o0oO0 . update ( 40 , "" , "Checking Source 5/11 Links" )
 ooo00OOOooO = i1Oo00 ( i1I1IiI1ii )
 o0oO0 . update ( 52 , "" , "Checking Source 6/11 Links" )
 O00oo00oOOO0o = i1Oo00 ( Ooo0OOO )
 o0oO0 . update ( 76 , "" , "Checking Source 7/11 Links" )
 I1II = i1Oo00 ( ooooOoo0OO )
 o0oO0 . update ( 88 , "" , "Checking Source 8/11 Links" )
 iIIi1Ii1III = i1Oo00 ( Oo0 )
 o0oO0 . update ( 95 , "" , "Checking Source 9/11 Links" )
 Oooo00 = i1Oo00 ( O0000Oo00o )
 o0oO0 . update ( 97 , "" , "Matching Results" )
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % oOoO0o00OO0
 if 11 - 11: ooo0O * oOo
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for IIo0o0O0O00oOOo , O000OOO in II1iI :
   Ii1IiI1III11 = i1Oo00 ( IIo0o0O0O00oOOo )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , iIIIiIi in I1IIII1i1 :
    if IIIiIiI in iIIIiIi . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + iIIIiIi + '-[COLORgold] source ' + O000OOO + '[/COLOR]' ) , IIo0o0O0O00oOOo + oOO0 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 92 - 92: iii1i1iiiiIi . I1ii11iIi11i * i1IiiiI1iI
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iIIi1Ii1III != 'Failed' :
  I1iI1I1ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1Ii1III )
  for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in I1iI1I1ii1 :
   if IIIiIiI in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] source HeroVision[/COLOR]' ) , IIo0o0O0O00oOOo , 1016 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 10 , "" , "Getting Herovision Links" )
    if 86 - 86: o0o00Oo0O
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: i1iIi / O0Oooo0O / oOoO0o00OO0 % oOOoOooOo % oOo0O0Ooo
 if I1II != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( I1II )
  for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in ooOoO00 :
   I1i = 'http://www.tvmaze.com' + IIo0o0O0O00oOOo . replace ( '"' , '' )
   i1II1iII = requests . get ( I1i ) . content
   iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( i1II1iII )
   for i11i1ii1I in iI111i :
    if not '<div>' in i11i1ii1I :
     II1io0OO00oo = i11i1ii1I . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
    Ii1IIiI1i = 'http:' + Ii1IIiI1i
    O000OOO = O000OOO . replace ( '&#039;' , '' )
    if O000OOO == '' :
     i1i1IiIiIi1Ii = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( IIo0o0O0O00oOOo ) )
     for O000OOO in i1i1IiIiIi1Ii :
      O000OOO = O000OOO . replace ( '-' , ' ' )
   ii1ii111 ( O000OOO + '-[COLORgold] source Scraper[/COLOR]' , I1i , 9110002 , Ii1IIiI1i , Oo00OOOOO , II1io0OO00oo , '' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 20 , "" , "Getting Scraper Links" )
   if 55 - 55: OOOo00oo0oO + ii % ooOoO0O00
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  O0oO0o0OOOOOO = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO , IiI1i11IiIiii in IIi11i1i1iI1 :
   if IIIiIiI in O000OOO . lower ( ) :
    if 'season' in IiI1i11IiIiii :
     IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , IIo0o0O0O00oOOo , 90054 , Ii1IIiI1i , Ii1IIiI1i , '' )
    if 'episodes' in IiI1i11IiIiii :
     IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' - [COLORred]Source - Tv HUB[/COLOR]' , IIo0o0O0O00oOOo , 90044 , Ii1IIiI1i , Ii1IIiI1i , '' )
  for IIo0o0O0O00oOOo in O0oO0o0OOOOOO :
   IIII ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , IIo0o0O0O00oOOo , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 24 - 24: oOoO0o00OO0 - I1ii11iIi11i
   iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if Ii11iiI != 'Failed' :
  I1iii11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( Ii11iiI )
  for IIo0o0O0O00oOOo , O000OOO , Ii1IIiI1i in I1iii11 :
   if IIIiIiI in O000OOO . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( O000OOO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , IIo0o0O0O00oOOo , 8022 , Ii1IIiI1i , '' , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 45 , "" , "Getting Source iWatch Links" )
    if 36 - 36: oOo0O0Ooo . OoOo0o % IIiIiII11i * I11i1ii1
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if iIiIIIi != 'Failed' :
  iIIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for O000OOO in iIIii :
   if IIIiIiI in O000OOO . lower ( ) :
    IIII ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iiIiIIII1iiIIi + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 34 - 34: i1IiiiI1iI % iiiiiiii1 - oOOoOooOo - oOo0O0Ooo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  o00O0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for O000OOO in o00O0O :
   if IIIiIiI in O000OOO . lower ( ) :
    IIII ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1I1IiI1ii + O000OOO ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 44 - 44: i1iIi . ooo0O . iI11I1II1I1I + ii - oOo0O0Ooo
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if O00oo00oOOO0o != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oo00oOOO0o )
  for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in Iii1I1111ii :
   if IIIiIiI in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + O000OOO + '-[COLORgold] Source Scooby[/COLOR]' ) , IIo0o0O0O00oOOo , 1016 , OO00OOoO0o , i1III1 , i11i1ii1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 90 , "" , "Getting Scooby Links" )
    if 22 - 22: i1IiiiI1iI * oOoO0o00OO0 . ii / I1ii11iIi11i / i1iIi
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 54 - 54: O0Oooo0O % i1iIi + oOOoOooOo
 I1II1IiI1 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for IIIIIIi1i in I1II1IiI1 :
  iiiii11I1 = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + IIIIIIi1i + '.php'
  iIi11iiI11 = i1Oo00 ( iiiii11I1 )
  if iIi11iiI11 != 'Failed' :
   iiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iIi11iiI11 )
   for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in iiIi :
    if OOooo in O000OOO . lower ( ) :
     if '.php' in IIo0o0O0O00oOOo :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      o00oOOooOOo0o ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 426 , OO00OOoO0o , i1III1 , i11i1ii1I )
     else :
      O000OOO = '[COLORsteelblue]' + O000OOO + '[/COLOR]'
      i1IIIo00oOOO ( O000OOO + '-[COLORred] source Pans Box[/COLOR]' , IIo0o0O0O00oOOo , 222 , OO00OOoO0o , i1III1 , i11i1ii1I )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
      if 45 - 45: i1iIi / OOOo00oo0oO * O0Oooo0O . i1iIi
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
      if 25 - 25: oOoO0o00OO0 / oOoO0o00OO0
      if 79 - 79: I1ii11iIi11i - oOo % I1ii11iIi11i . IIiIiII11i
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0Ooo0Oooo0o ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0o0O0O00oOOo = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( OOooo ) . replace ( ' ' , '+' )
 if 22 - 22: OOOo00oo0oO / IIiIiII11i . iii1i1iiiiIi
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oO0 . update ( 0 , "" , "Checking Source Links" )
 oOOo0 = i1Oo00 ( IIo0o0O0O00oOOo )
 o0oO0 . update ( 100 , "" , "Checking Source Links" )
 if 9 - 9: Ii + oOOoOooOo . iI11I1II1I1I * iii1i1iiiiIi
 if oOOo0 != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , O000OOO in IIi11i1i1iI1 :
   if OOooo in O000OOO . lower ( ) :
    iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + IIo0o0O0O00oOOo ) , 222 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 4 - 4: O0Oooo0O + iiiiiiii1 % o0o00Oo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
OoO0oO = '{ZH},' ; ii1I1 = '{IX},' ; ooOo0OooOooo = '{LM},'
if 35 - 35: O0Oooo0O / ii / I11i1ii1 + iii1i1iiiiIi - O0Oooo0O + Ii
def ooOoo ( url ) :
 iIII1 = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iIII1 )
 for url , IiIiIi1I1 , IiI1ii1Ii , O000OOO in iI111i :
  IIII ( ( IiIiIi1I1 ) . replace ( 'Sezon' , ' Season ' ) + ( IiI1ii1Ii ) . replace ( 'Bölüm' , ' Episode ' ) + O000OOO , url , 8063 , '' )
  if 84 - 84: ii - ii / I11i1ii1
  if 29 - 29: i1iIi / o0o00Oo0O
  if 50 - 50: i1iIi + i1iIi
  if 51 - 51: oOoO0o00OO0 / ii * I11i1ii1
def o0oO ( url ) :
 iIII1 = cloudflare . source ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iIII1 )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( O000OOO , url , 222 , '' )
  if 5 - 5: ooo0O / IIiIiII11i % oOOoOooOo - oOo0O0Ooo . ooo0O
  if 34 - 34: O0Oooo0O + I1ii11iIi11i / oOo0O0Ooo / Ii - oOoO0o00OO0 % ooOoO0O00
  if 54 - 54: oOo0O0Ooo + iiiiiiii1
  if 64 - 64: iii1i1iiiiIi / ooo0O * iii1i1iiiiIi / I1ii11iIi11i + ooo0O
def I1iII1IiI11i ( ) :
 if 66 - 66: I1ii11iIi11i . OOOo00oo0oO - o0o00Oo0O . O0Oooo0O + iiiiiiii1 / Ii
 iIII1 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIII1 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO , IiI1ii1Ii in iI111i :
  IIII ( O000OOO + '  -  ' + ( IiI1ii1Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IIo0o0O0O00oOOo , 8063 , Ii1IIiI1i )
  if 52 - 52: OOOo00oo0oO % I1ii11iIi11i * IIiIiII11i
def ii1iiiIIiIII ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO , Ii1IIiI1i in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 8002 , Ii1IIiI1i )
def i1i1iiI11I ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( IIi )
 for Ii1IIiI1i , time , url , O000OOO , oOoOooO0OOOoo in iI111i :
  o00oOOooOOo0o ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , time ) , url , 1015 , Ii1IIiI1i , oOoOooO0OOOoo )
  if 78 - 78: iii1i1iiiiIi % oOo - i1iIi / OoOo0o
def ooOo000 ( ) :
 if 87 - 87: I1ii11iIi11i + oOo0O0Ooo % oOo0O0Ooo * Ii
 IIII ( 'Coronation Street' , '' , 8001 , '' )
 IIII ( 'Eastenders' , '' , 8002 , '' )
 IIII ( 'Emmerdale' , '' , 8003 , '' )
 IIII ( 'Hollyoaks' , '' , 8004 , '' )
 IIII ( 'Im a Celebrity' , '' , 8005 , '' )
 if 68 - 68: iiiiiiii1 . OoOo0o
 if 6 - 6: i1iIi - ooo0O % i1IiiiI1iI + Ii
 if 40 - 40: o0o00Oo0O . i1iIi
 if 58 - 58: Ii * iiiiiiii1 / i1iIi - OOOo00oo0oO - oOoO0o00OO0 % ooo0O
def i11Oo00 ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Holly' in O000OOO :
   Ii1IIiI1i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in IIo0o0O0O00oOOo :
    iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , Ii1IIiI1i )
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
   Ii1IIiI1i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , Ii1IIiI1i )
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
   Ii1IIiI1i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , Ii1IIiI1i )
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
   Ii1IIiI1i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , Ii1IIiI1i )
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
   Ii1IIiI1i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in IIo0o0O0O00oOOo :
    iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IIo0o0O0O00oOOo . replace ( '\\/' , '/' ) , 8006 , Ii1IIiI1i )
   else :
    pass
    if 12 - 12: I11i1ii1 * iii1i1iiiiIi / Ii + Ii
def iII11I11i ( name , url ) :
 IIIII1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIIII1 :
  i1iI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  IIi = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( IIi ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  IIi = open_url ( url )
  oOOoo00Oo = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( IIi ) [ - 1 ]
  i1iI = oOOoo00Oo . replace ( '\\/' , '/' )
 IioO0O = xbmcgui . ListItem ( name , '' , '' )
 IioO0O . setPath ( i1iI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IioO0O )
 if 19 - 19: oOo - i1IiiiI1iI % I1ii11iIi11i / Ii % IIiIiII11i * I1ii11iIi11i
 if 14 - 14: Ii % OoOo0o + ooo0O + ooo0O . oOo
def I111i1IiI1 ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iI111i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , IIo0o0O0O00oOOo , 7071 , I1IIIii + 'popcorn.png' )
 for IIo0o0O0O00oOOo , O000OOO in IIi11i1i1iI1 :
  IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , IIo0o0O0O00oOOo , 7071 , I1IIIii + 'popcorn.png' )
  if 46 - 46: IIiIiII11i - oOo % oOOoOooOo
def oOIIIiIII111iii ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Movies' in O000OOO :
   IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( IIo0o0O0O00oOOo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , I1IIIii + 'popcorn.png' )
def oOOiI ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIi )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( IIi )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , Ii1IIiI1i )
 for url in IIi11i1i1iI1 :
  IIII ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , I1IIIii + 'Next.png' )
  if 94 - 94: I11i1ii1 / oOOoOooOo + O0Oooo0O * OoOo0o
  if 16 - 16: oOOoOooOo - ooOoO0O00 - i1IiiiI1iI % I1ii11iIi11i * i1IiiiI1iI - iii1i1iiiiIi
def IiiIi11 ( url ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( IIi )
 for O000OOO , url , Ii1IIiI1i in iI111i :
  if '{{' in O000OOO :
   pass
  else :
   IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , Ii1IIiI1i )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
OoOI1I = '{UJ},' ; Ii111 = '{WE},' ; Ii11I111Ii = '{WP},' ; iIiIIiIII1I = '{PP},'
def Ii1i1IiiIiIII ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( IIi )
 for O000OOO , url , Ii1IIiI1i in iI111i :
  if '{{' in O000OOO :
   pass
  else :
   IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , Ii1IIiI1i )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0O0O000oOO0oOo0OOoOO ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  o0O00oo0Ooo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O00oo0Ooo ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( IIi )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , I1IIIii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: ii
 if 67 - 67: Ii + iii1i1iiiiIi
 if 50 - 50: oOOoOooOo . ooOoO0O00 + oOoO0o00OO0 . OoOo0o
def oO0Ooo ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  if '(cooltvseries.com)' in O000OOO :
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
 for url , O000OOO in IIi11i1i1iI1 :
  if '(cooltvseries.com)' in O000OOO :
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
def iiiiIIiiII1Iii1 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( IIi )
 for url in iI111i :
  i1i1I1 ( ( url ) . replace ( ' ' , '%20' ) )
OOo0O0O000 = '{XX},' ; o0oOOoO0o0 = '{UD},' ; oOOo0o0O0oO0o = '{YT},' ; iiIioo0O0 = '{JS},' ; oooO000oO0O = '{PF},'
if 40 - 40: OoOo0o - oOo . ii - OOOo00oo0oO / oOOoOooOo + I1ii11iIi11i
def Ooo0 ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iI111i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO , Ii1IIiI1i in iI111i :
  iI1iiiIiii ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( o0oOoO00o ( IIo0o0O0O00oOOo ) ) , 222 , Ii1IIiI1i )
  if 14 - 14: ii
def OOoOOO0 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( IIi )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( IIi )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  if 'youtu' in url :
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + Ii1IIiI1i )
 for url in next :
  IIII ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , I1IIIii + 'Next.png' )
  if 99 - 99: ooo0O * ooo0O
def Ii1II1I ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 5 - 5: OoOo0o . iiiiiiii1 . OOOo00oo0oO % I11i1ii1 * o0o00Oo0O
def Ii1II1I ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 20 - 20: I1ii11iIi11i . oOo0O0Ooo . oOo0O0Ooo / ii . ii + iI11I1II1I1I
def oO00o ( url ) :
 IIi = i11111IIIII
 iI111i = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( IIi )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 222 , Ii1IIiI1i )
  if 32 - 32: Ii + IIiIiII11i + IIiIiII11i % i1IiiiI1iI
  if 96 - 96: ooo0O
  if 90 - 90: I11i1ii1 * i1iIi . i1IiiiI1iI / oOoO0o00OO0 % i1IiiiI1iI
  if 58 - 58: iiiiiiii1 % iI11I1II1I1I * oOo
  if 25 - 25: O0Oooo0O - oOOoOooOo + I1ii11iIi11i . oOo0O0Ooo % iI11I1II1I1I
def IiIIi1I ( ) :
 if 5 - 5: Ii + i1IiiiI1iI . I11i1ii1
 IIII ( 'All Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Entertainment' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Movies' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Music' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'News' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Sports' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Documentary' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Kids' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Food' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Religious' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'USA Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 IIII ( 'Other' , '' , 7021 , I1IIIii + 'livetv.png' )
 if 9 - 9: Ii / iI11I1II1I1I - oOoO0o00OO0 * oOoO0o00OO0
 if 99 - 99: i1IiiiI1iI
def oOOOOOOooO ( Cat_Name ) :
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
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIi )
 print 'Len Match: >>>' + str ( len ( iI111i ) )
 for O000OOO , Ii1IIiI1i , I11iII in iI111i :
  II1iiIiIiiI1Ii = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( Ii1IIiI1i ) . replace ( '\\' , '' )
  if I11iII == IiiiIiiI1IIIi :
   IIII ( O000OOO , '' , 7022 , II1iiIiIiiI1Ii )
  elif Iii11Ii == True :
   IIII ( O000OOO , '' , 7022 , II1iiIiIiiI1Ii )
  else : pass
  if 50 - 50: oOo
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 35 - 35: iI11I1II1I1I . o0o00Oo0O / ooOoO0O00
def i111I ( Search_Name ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( IIi )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( IIi )
 for Ii1IIiI1i , IIo0o0O0O00oOOo , I1i , iiIiIIII1iiIIi in iI111i :
  II1iiIiIiiI1Ii = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( Ii1IIiI1i ) . replace ( '\\' , '' )
  iI1iiiIiii ( Search_Name + ': Link 1' , ( IIo0o0O0O00oOOo ) . replace ( '\\' , '' ) , 222 , II1iiIiIiiI1Ii )
  iI1iiiIiii ( Search_Name + ': Link 2' , ( I1i ) . replace ( '\\' , '' ) , 222 , II1iiIiIiiI1Ii )
  iI1iiiIiii ( Search_Name + ': Link 3' , ( iiIiIIII1iiIIi ) . replace ( '\\' , '' ) , 222 , II1iiIiIiiI1Ii )
  if 10 - 10: oOOoOooOo % o0o00Oo0O + iI11I1II1I1I % o0o00Oo0O * OOOo00oo0oO
def O000Oo ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  iI1iiiIiii ( O000OOO , ( IIo0o0O0O00oOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , I1IIIii + 'english.png' )
def IiiIi1II ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  iI1iiiIiii ( O000OOO , ( IIo0o0O0O00oOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'xxx.png' )
def IiII1IiiI ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( IIi )
 for O000OOO , IIo0o0O0O00oOOo in iI111i :
  iI1iiiIiii ( O000OOO , ( IIo0o0O0O00oOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'vod(1).png' )
  if 57 - 57: OOOo00oo0oO
def i11I ( url ) :
 url
 iIIi = xbmcgui . ListItem ( O000OOO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIi )
 return
 if 48 - 48: oOoO0o00OO0 . IIiIiII11i * I11i1ii1 . oOo0O0Ooo * i1iIi
 if 82 - 82: iii1i1iiiiIi * oOoO0o00OO0 - ii / ooOoO0O00 + ii * i1IiiiI1iI
def OoI1iIi ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']All WorkOuts[/COLOR]' , o0oOoO00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) , 7085 , I1IIIii + 'Fitness.png' , Oo00OOOOO , '' )
 if 80 - 80: ooOoO0O00 / OoOo0o / ooo0O - I11i1ii1
def Iii11 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '"id":.+?,"title":(.+?),"is_featured":1,"minutes":(.+?),"burnmin":(.+?),"burnmax":(.+?),"burnavg":(.+?),"difficulty":(.+?),"image":"([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( '"next_page_url":"([^"]*)"' ) . findall ( IIi )
 for O000OOO , time , iII1Ii1ii111 , iII11IIi1I1 , o00o0o , ooOoOo , Ii1IIiI1i , url , oO0oo0o00O0 , oO00Oo0 in iI111i :
  o00oOOooOOo0o ( ( O000OOO ) . replace ( '"' , '' ) , 'https://www.fitnessblender.com/videos/' + url , 7086 , 'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-' + Ii1IIiI1i , '' , ( 'Calorie burn:[CR]' + iII1Ii1ii111 + ' - ' + iII11IIi1I1 + ' Average = ' + o00o0o + '[CR][CR]Difficulty = ' + ooOoOo + '[CR][CR]Equipment Needed: ' + oO0oo0o00O0 + '[CR][CR]Focus: ' + oO00Oo0 ) . replace ( '"' , '' ) )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
 for url in IIi11i1i1iI1 :
  IIII ( 'NEXT' , ( 'https://www.fitnessblender.com/videos' + url ) . replace ( '\/' , '' ) , 7085 , I1IIIii + 'Next.png' )
  if 25 - 25: OoOo0o % iiiiiiii1 + iiiiiiii1
def IIiIiOOoO ( url , iconimage , description ) :
 oOOo0 = i11111IIIII ( url )
 Ii1IIiI1i = iconimage
 i11i1ii1I = description
 iI111i = re . compile ( '<div class="responsive-video">.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  O0O0ooOOO ( 'PLAY' , url , 8043 , Ii1IIiI1i , '' , i11i1ii1I )
  iIiIi11 ( 'tvshows' , 'Media Info 3' )
 oOoO0O0o = re . compile ( '<div class="article__content">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for O000OoO0OO in oOoO0O0o :
  OOo = ( O000OoO0OO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o00oOOooOOo0o ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + Ii1IIiI1i , '' , OOo )
  if 63 - 63: I11i1ii1 / oOoO0o00OO0
def o0OoooO0oo0 ( INFO ) :
 OoOoO ( 'info for workout' , INFO )
 if 59 - 59: OoOo0o - O0Oooo0O - IIiIiII11i / ooOoO0O00 * OoOo0o . ii
 if 46 - 46: I11i1ii1 * ii . ooo0O - O0Oooo0O * oOo0O0Ooo
 if 83 - 83: I1ii11iIi11i . ooo0O + iiiiiiii1 + ooo0O % iI11I1II1I1I * iii1i1iiiiIi
def OOoo00o0 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( IIi )
 for url , O000OOO in iI111i :
  IIII ( ( O000OOO ) . replace ( 'SlyNet' , '' ) , url , 9031 , I1IIIii + 'Sport.png' )
def o0OO0 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( IIi )
 for url , O000OOO in iI111i :
  IIII ( O000OOO , url , 9032 , I1IIIii + 'icon.png' )
def iI1II1i1ii ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( IIi )
 for O000OOO , url in iI111i :
  if '=' in O000OOO :
   pass
  else :
   iI1iiiIiii ( ( O000OOO ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , I1IIIii + 'icon.png' )
def OOooOOooo000OoO ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( IIi )
 for O000OOO , url in iI111i :
  if '=' in O000OOO :
   pass
  else :
   iI1iiiIiii ( O000OOO , url , 222 , I1IIIii + 'icon.png' )
   if 93 - 93: i1iIi / iii1i1iiiiIi + oOOoOooOo . oOo / o0o00Oo0O . ooo0O
   if 34 - 34: ooo0O + OoOo0o . oOo + oOo0O0Ooo + ii
   if 90 - 90: i1iIi / iii1i1iiiiIi - iI11I1II1I1I / ooOoO0O00 * O0Oooo0O - oOOoOooOo
def I111I1IiI1i1 ( url ) :
 ii1ii111 ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( IIi )
 for O000OOO , Ii1IIiI1i , url in iI111i :
  if 'music' in url :
   ii1ii111 ( O000OOO , url , 90036 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   ii1ii111 ( O000OOO , url , 90039 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
def o0oo ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( IIi )
 for O000OOO , url , Ii1IIiI1i in iI111i :
  Ii111iIi1iIi ( O000OOO , url , 100009 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
  if 62 - 62: OOOo00oo0oO . i1IiiiI1iI * OoOo0o / Ii
def OOO00OO0Ooo ( url ) :
 ii1ii111 ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 IIi = requests . get ( url ) . text
 ii11I1 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( IIi )
 ooO0oOo0o = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( IIi )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( ooO0oOo0o ) )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  i1II1iII = requests . get ( url ) . text
  iiiii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( i1II1iII )
  for ooO0OOOooo in iiiii :
   OOoO00ooO = requests . get ( ooO0OOOooo ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OOoO00ooO )
   for iII1ii1 , oO0o0ooooo , i1iII1IiiIiI1 , o0o0oo0OOo0O0 , IIIi1I1IIii1II in iI111i :
    if iII1ii1 == 'xyz' :
     IiIIiIiI1ii = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( O000OOO , IiIIiIiI1ii , 1001111 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
    else :
     IiIIiIiI1ii = 'http://' + o0o0oo0OOo0O0 + '.' + i1iII1IiiIiI1 + '.' + oO0o0ooooo + '.' + iII1ii1 + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( O000OOO , IiIIiIiI1ii , 1001111 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
 for OOo0 in ii11I1 :
  ii1ii111 ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo0 , 1000111 , '' , '' , '' , '' )
  if 10 - 10: i1iIi - IIiIiII11i / Ii * oOo0O0Ooo / o0o00Oo0O . i1IiiiI1iI
  if 67 - 67: iii1i1iiiiIi - oOOoOooOo - iI11I1II1I1I
  if 31 - 31: IIiIiII11i + ooo0O * Ii . ooo0O
def OO000IIi ( ) :
 ii1ii111 ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 98 - 98: I1ii11iIi11i % i1IiiiI1iI - i1iIi
 if 17 - 17: O0Oooo0O + iiiiiiii1 / oOo
def oOOOoO00OOooOOOoO ( url , name ) :
 ii1ii111 ( name , '' , '' , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 IIi = requests . get ( url ) . text
 ii11I1 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( IIi )
 ooO0oOo0o = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( IIi )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( ooO0oOo0o ) )
 for url , Ii1IIiI1i , name in iI111i :
  i1II1iII = requests . get ( url ) . text
  iiiii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( i1II1iII )
  for ooO0OOOooo in iiiii :
   OOoO00ooO = requests . get ( ooO0OOOooo ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OOoO00ooO )
   for iII1ii1 , oO0o0ooooo , i1iII1IiiIiI1 , o0o0oo0OOo0O0 , IIIi1I1IIii1II in iI111i :
    if iII1ii1 == 'xyz' :
     IiIIiIiI1ii = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , IiIIiIiI1ii , 1001111 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
    else :
     IiIIiIiI1ii = 'http://' + o0o0oo0OOo0O0 + '.' + i1iII1IiiIiI1 + '.' + oO0o0ooooo + '.' + iII1ii1 + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , IiIIiIiI1ii , 1001111 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
     if 60 - 60: oOo
 for OOo0 in ii11I1 :
  ii1ii111 ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo0 , 1003111 , '' , '' , '' , '' )
  if 16 - 16: i1IiiiI1iI
  if 23 - 23: ooo0O + oOOoOooOo - I11i1ii1
def Ii11I111 ( ) :
 ii1ii111 ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 63 - 63: oOoO0o00OO0 % oOOoOooOo % oOoO0o00OO0
 if 71 - 71: i1iIi
 if 43 - 43: ooo0O / oOOoOooOo
def OoOoOOoOo ( url , name ) :
 ii1ii111 ( name , '' , '' , '' , '' , '' , '' )
 ii1ii111 ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 IIi = requests . get ( url ) . text
 ii11I1 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( IIi )
 ooO0oOo0o = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( IIi )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( ooO0oOo0o ) )
 for url , Ii1IIiI1i , name in iI111i :
  i1II1iII = requests . get ( url ) . text
  iiiii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( i1II1iII )
  for ooO0OOOooo in iiiii :
   OOoO00ooO = requests . get ( ooO0OOOooo ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OOoO00ooO )
   for iII1ii1 , oO0o0ooooo , i1iII1IiiIiI1 , o0o0oo0OOo0O0 , IIIi1I1IIii1II in iI111i :
    if iII1ii1 == 'xyz' :
     IiIIiIiI1ii = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , IiIIiIiI1ii , 1001111 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
    else :
     IiIIiIiI1ii = 'http://' + o0o0oo0OOo0O0 + '.' + i1iII1IiiIiI1 + '.' + oO0o0ooooo + '.' + iII1ii1 + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , IiIIiIiI1ii , 1001111 , Ii1IIiI1i , Ii1IIiI1i , '' , '' )
     if 59 - 59: i1iIi * ii - iiiiiiii1
 for OOo0 in ii11I1 :
  ii1ii111 ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo0 , 1005111 , '' , '' , '' , '' )
def O0oo ( name , url ) :
 import urlresolver
 try :
  OOOo00 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( OOOo00 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 22 - 22: oOo - ooo0O
 if 87 - 87: I1ii11iIi11i % oOoO0o00OO0 . ii % i1iIi * OOOo00oo0oO - oOo0O0Ooo
 if 9 - 9: ii - i1iIi - I1ii11iIi11i - i1iIi - iI11I1II1I1I - iiiiiiii1
def oO00ooOoOoOO ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 iI111i = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'Daily' in O000OOO :
   IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 9008 , O0O )
def o0O0Oo0 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def iI1111i ( url ) :
 iI1iiiIiii ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 iI1iiiIiii ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 iI1iiiIiii ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IIi )
 for O000OOO , url in iI111i :
  iI1iiiIiii ( ( O000OOO ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 36 - 36: oOo % i1iIi % iiiiiiii1
def OoOO0OOOO0 ( ) :
 IIi = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if '.m3u' in IIo0o0O0O00oOOo :
   IIII ( ( O000OOO ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + IIo0o0O0O00oOOo ) , 9011 , I1IIIii + 'disclose.png' )
def OooOOo0ooO ( url ) :
 IIi = cloudflare . source ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IIi )
 for O000OOO , url in iI111i :
  iI1iiiIiii ( ( O000OOO ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 6 - 6: ii . OOOo00oo0oO / Ii / oOOoOooOo + OOOo00oo0oO . I1ii11iIi11i
def OO0o0o0oo0O ( ) :
 IIi = i11111IIIII ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 iI111i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  if 'category' in IIo0o0O0O00oOOo :
   IIII ( O000OOO , 'http://www.disclose.tv/' + IIo0o0O0O00oOOo , 7010 , I1IIIii + 'disclose.png' )
   if 94 - 94: Ii . I11i1ii1 - oOo + o0o00Oo0O
   if 89 - 89: iiiiiiii1 * OOOo00oo0oO
def I1Ii1 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( IIi )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIi )
 for url , O000OOO , Ii1IIiI1i in iI111i :
  IIII ( O000OOO , 'http://www.disclose.tv/' + url , 7011 , Ii1IIiI1i )
 for url in next :
  IIII ( 'NEXT' , url , 7010 , I1IIIii + 'Next.png' )
  if 99 - 99: I11i1ii1 + iiiiiiii1 * ooOoO0O00 . oOo0O0Ooo . ooOoO0O00
  if 50 - 50: I1ii11iIi11i * I1ii11iIi11i * ii % O0Oooo0O
def OO00iiI1II1i ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( IIi )
 iIIii = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  if 'http' in url :
   iI1iiiIiii ( 'video/flv' , url , 222 , I1IIIii + 'disclose.png' )
 for url , O000OOO in IIi11i1i1iI1 :
  iI1iiiIiii ( O000OOO , url , 222 , I1IIIii + 'disclose.png' )
 for url in iIIii :
  iI1iiiIiii ( 'YT Link' , url , 8043 , I1IIIii + 'disclose.png' )
  if 18 - 18: I11i1ii1
  if 74 - 74: oOo0O0Ooo
def O0oOooOO ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( IIi )
 for url , O000OOO in iI111i :
  IIII ( O000OOO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , I1IIIii + 'icon.png' )
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
   for OOii111IiiI1 in ii11iIIiiI1I :
    oO0o = False
    Resolve ( OOii111IiiI1 )
    if 91 - 91: oOo0O0Ooo - ii - ii
 elif iI1iII111ii1I > 1 :
  if 69 - 69: iiiiiiii1 * Ii / ooOoO0O00
  for IiIi1iIIiII1i in O0o0ooO0oO0oO :
   Oo00Oo0o000 = i11111IIIII ( IiIi1iIIiII1i )
   oOo0ooOo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oo00Oo0o000 )
   iI1i1i = oOo0ooOo
   iI1i1i = ( str ( iI1i1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iI1i1i
   iI1iiiIiii ( 'DOUBLE LINK' , iI1i1i , 424 , '' )
   if 83 - 83: o0o00Oo0O
   for url in oOo0ooOo :
    IIII ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1i = Google . resolve ( url )
    except :
     pass
    try :
     IIIii1i = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1i ) )
     for iIIiIIi1I1iiiii , iI1i1iiIiiiIiIIi in IIIii1i :
      if 87 - 87: ooOoO0O00 - o0o00Oo0O % ii * Ii % Ii
      HD_URLS . append ( iIIiIIi1I1iiiii )
      SD_URLS . append ( iI1i1iiIiiiIiIIi )
    except :
     pass
 else :
  pass
  if 19 - 19: oOOoOooOo
def i11ii1i1i ( ) :
 if 79 - 79: oOo
 if 4 - 4: i1IiiiI1iI / oOoO0o00OO0
 IIII ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , I1IIIii + 'Movies.png' )
 if 2 - 2: I11i1ii1 + i1IiiiI1iI / iI11I1II1I1I . Ii . ooOoO0O00 * oOOoOooOo
 IIII ( 'Search Movies' , '' , 7017 , I1IIIii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 14 - 14: I1ii11iIi11i . o0o00Oo0O - OOOo00oo0oO - Ii
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / oOOoOooOo
def oo0OoooOo0 ( ) :
 IIi = i11111IIIII ( 'http://cnfstudio.com/' )
 iI111i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( O000OOO , 'http://cnfstudio.com/genre/' + IIo0o0O0O00oOOo , 7003 , I1IIIii + 'icon.png' )
  if 61 - 61: IIiIiII11i . oOo - IIiIiII11i
iI111I11I1I1 = xbmcgui . Dialog ( )
if 75 - 75: I1ii11iIi11i - iii1i1iiiiIi + OOOo00oo0oO % ooOoO0O00 * OoOo0o
OOoO = '{UN},' ; oO0O = '{IG},' ; I1Ii1OOoo0Oo00 = '{PL},' ; I11I11II11I = '{LO},' ; O00oo00O = '{LP},' ; oOoI11Iii1iIII1i = '{HA},' ; ooOOO000 = '{XD},' ; i1Ii1IiIii1I = '{TA},' ; i1iIII1Ii1 = '{DP},' ; o0Oo00OoO000O = '{JT},' ; II1iii = '{JJ},' ; O0oOOOO0o = '{MM},' ; OoOOO0 = '{FQ},' ; IiIi = '{HH},'
if 96 - 96: oOo0O0Ooo
def o0OoO0iiII1 ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( IIi )
 oOooO0o000 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( IIi )
 for Ii1IIiI1i , url , O000OOO in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , Ii1IIiI1i )
 oOooO0o000 = oOooO0o000
 for url in oOooO0o000 :
  IIII ( 'Next Page' , url , 7003 , I1IIIii + 'Next.png' )
  if 50 - 50: IIiIiII11i . ooo0O
def iIII1ii1iI111IIi1 ( url ) :
 if 88 - 88: iI11I1II1I1I / i1iIi * I11i1ii1 / O0Oooo0O
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  IIIi1I1IIii1II = url + '&fv=&sou='
  IIIi1I1IIii1II = IIIi1I1IIii1II . replace ( 'player' , 'watch' )
  iii = i1i11i1 ( IIIi1I1IIii1II )
  ii1iIii1Ii1 = i1i11i1 ( url )
  if 2 - 2: O0Oooo0O
  if 67 - 67: oOOoOooOo
def i1i11i1 ( url ) :
 if 53 - 53: o0o00Oo0O . ooo0O . IIiIiII11i * iii1i1iiiiIi . OoOo0o
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( IIi )
 for url in iI111i :
  II11IiI1 ( url )
  if 78 - 78: iii1i1iiiiIi * iii1i1iiiiIi - oOo / OOOo00oo0oO
  if 24 - 24: O0Oooo0O . OOOo00oo0oO + oOOoOooOo . oOoO0o00OO0 . IIiIiII11i
def i1ii1i ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , I1IIIii + 'LocalM3U.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , I1IIIii + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 6 - 6: OoOo0o + oOo + oOo0O0Ooo / ii
def IiiiII1 ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  o0oO0OOO = open ( O0OoO000O0OO , 'r' )
  for iIIi in o0oO0OOO :
   Ooo00OO00oOO0 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIi )
   for O000OOO , IIo0o0O0O00oOOo in Ooo00OO00oOO0 :
    iI1iiiIiii ( O000OOO , IIo0o0O0O00oOOo , 222 , I1IIIii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 86 - 86: o0o00Oo0O - ii
def IIi1II ( url ) :
 if os . path . exists ( Remote ) :
  oOOo0 = II11iIII1i1I ( url )
  iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
  for O000OOO , url in iI111i :
   url = ( url ) . strip ( )
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 9 - 9: IIiIiII11i - Ii * ooo0O % oOo * Ii / i1IiiiI1iI
  if 45 - 45: Ii * iiiiiiii1 - oOoO0o00OO0 + oOOoOooOo % iiiiiiii1
def Iii1I1I11iiI1 ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + IIo0o0O0O00oOOo
 O000OOO = 'plugin.video.GenieTv'
 if 11 - 11: iI11I1II1I1I
 iiI1iiIi ( IIo0o0O0O00oOOo , O000OOO )
 if 56 - 56: iii1i1iiiiIi - I11i1ii1
def o0OOOO00O0Oo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo in iI111i :
  IIo0o0O0O00oOOo = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + IIo0o0O0O00oOOo
 O000OOO = 'repository.GenieTv'
 if 53 - 53: oOoO0o00OO0 - IIiIiII11i . Ii
 iiI1iiIi ( IIo0o0O0O00oOOo , O000OOO )
 if 76 - 76: iI11I1II1I1I - I1ii11iIi11i
 if 79 - 79: oOo0O0Ooo * I11i1ii1 . ii % O0Oooo0O * O0Oooo0O
def I1i1iI1II ( ) :
 I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , I11iIi1i1II11 )
 if iiI == 0 :
  OooO0oo ( )
 if iiI == 1 :
  OooO0o00oO ( )
  if 29 - 29: IIiIiII11i % iI11I1II1I1I * o0o00Oo0O . ooo0O
  if 56 - 56: ooOoO0O00 . oOOoOooOo + i1IiiiI1iI - Ii
  if 100 - 100: iI11I1II1I1I - ooOoO0O00 . OoOo0o
  if 73 - 73: O0Oooo0O / i1IiiiI1iI / Ii - oOoO0o00OO0 % oOOoOooOo
O0oo0OO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
i1111 = xbmc . translatePath ( 'special://home/' )
o0oO0 = xbmcgui . DialogProgress ( )
Oo0OoO00O = 'https://addons.tvaddons.ag/'
if 43 - 43: I1ii11iIi11i % OOOo00oo0oO . Ii - o0o00Oo0O
def OooO0o00oO ( ) :
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 i1II11III = 'https://addons.tvaddons.ag/search/?keyword=' + IIIiIiI
 oOOo0 = i11111IIIII ( i1II11III )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , oo0O0oO0O0O , O000OOO in iI111i :
  o00oOOooOOo0o ( O000OOO , IIo0o0O0O00oOOo , 10054 , 'https://addons.tvaddons.ag/' + oo0O0oO0O0O , Oo00OOOOO , '' )
  if 5 - 5: ooOoO0O00 + i1iIi
  if 38 - 38: oOo0O0Ooo . o0o00Oo0O + OoOo0o / oOoO0o00OO0 . iI11I1II1I1I - ooOoO0O00
def OooO0oo ( ) :
 oOOo0 = i11111IIIII ( Oo0OoO00O )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  if 'Repositories' in O000OOO :
   pass
  elif 'Services' in O000OOO :
   pass
  elif 'International' in O000OOO :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , IIo0o0O0O00oOOo , 10053 , 'https://addons.tvaddons.ag/' + Ii1IIiI1i , Oo00OOOOO , '' )
   if 3 - 3: I1ii11iIi11i + OOOo00oo0oO
   if 65 - 65: oOo0O0Ooo / iii1i1iiiiIi % oOo0O0Ooo * Ii * ii / i1IiiiI1iI
def Addon ( url ) :
 oOOo0 = i11111IIIII ( url )
 ii11I1 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  if 'Please' in O000OOO :
   pass
  else :
   O0O0ooOOO ( O000OOO , url , 10054 , 'https://addons.tvaddons.ag/' + Ii1IIiI1i , Oo00OOOOO , '' )
 for url in ii11I1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
  if 91 - 91: Ii / Ii
  if 9 - 9: i1IiiiI1iI / O0Oooo0O + iI11I1II1I1I + oOo0O0Ooo - IIiIiII11i
def O0OOoo ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oO0 = xbmcgui . DialogProgress ( )
   o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , name + '.zip' )
   try :
    os . remove ( oo0O00Oooo0O0 )
   except :
    pass
   downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
   I11OO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print I11OO
   print '======================================='
   extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
   OO0 ( )
   if 46 - 46: ooOoO0O00 % iI11I1II1I1I
def iiI1iiIi ( url , name ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , name + '.zip' )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 I11OO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11OO
 print '======================================='
 extract . all ( oo0O00Oooo0O0 , I11OO , o0oO0 )
 OO0 ( )
 if 80 - 80: ii / o0o00Oo0O / O0Oooo0O - I1ii11iIi11i . Ii
def OO0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 3 - 3: I1ii11iIi11i - OoOo0o * oOo - IIiIiII11i . ii
 if 14 - 14: oOo0O0Ooo
def I1IiiIII1ii ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi )
 for url , oo0O0oO0O0O , O000OOO in iI111i :
  IIII ( O000OOO , url , 1007 , oo0O0oO0O0O )
def iiOo00ooO0 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi )
 for url , oo0O0oO0O0O , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 1006 , oo0O0oO0O0O )
  if 5 - 5: ooOoO0O00 - iii1i1iiiiIi - OOOo00oo0oO + Ii
def oOoo0O0o ( ) :
 IIi = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , I1I1 , O000OOO in iI111i :
  II1111i11i11 ( O000OOO , 100109 , IIo0o0O0O00oOOo , image = OO00OOoO0o , isFolder = True )
  if 50 - 50: oOOoOooOo + i1IiiiI1iI / OOOo00oo0oO - I11i1ii1
def iIII1II11I1 ( url ) :
 import random
 Ii1Ii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 Ii1Ii . clear ( )
 i11ii1II1Ii = [ ]
 i1I1ii1iI1 = [ ]
 Ii1i = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for I1i , OO00OOoO0o , i11i1ii1I , I1I1 , O000OOO in iI111i :
  i11ii1II1Ii . append ( [ I1i , O000OOO ] )
  if len ( i11ii1II1Ii ) == len ( iI111i ) :
   for iIIi in i11ii1II1Ii :
    OOOOooO0Oo0oo = random . randint ( 1 , len ( i11ii1II1Ii ) )
    try :
     oOo0oooo = i11ii1II1Ii [ int ( OOOOooO0Oo0oo ) ]
    except :
     pass
    if len ( i1I1ii1iI1 ) <= 20 :
     if oOo0oooo [ 1 ] not in Ii1i :
      oo00O00oO = i11111IIIII ( oOo0oooo [ 0 ] )
      iIIii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oo00O00oO )
      for oO0oo0 , IiIiI1 in iIIii :
       ooo00OOOooO = i11111IIIII ( oO0oo0 )
       o00O0O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( ooo00OOOooO )
       for iIi111 , IIIi1I1IIii1II in o00O0O :
        if 'panda' in IIIi1I1IIii1II :
         OooOO0oOOo0O = i11111IIIII ( IIIi1I1IIii1II )
         ii1iii1i = re . compile ( "url: '(.+?)'" ) . findall ( OooOO0oOOo0O )
         for i1Ii in ii1iii1i :
          if 'http' in i1Ii :
           IioO0O = xbmcgui . ListItem ( oOo0oooo [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : oOo0oooo [ 1 ] } )
           IioO0O . setProperty ( "IsPlayable" , "true" )
           Ii1Ii . add ( i1Ii , IioO0O )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IioO0O )
           if 48 - 48: Ii * iii1i1iiiiIi - oOo0O0Ooo + iI11I1II1I1I
def II1111i11i11 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 OoOO0o = sys . argv [ 0 ]
 OoOO0o += '?mode=' + str ( mode )
 OoOO0o += '&title=' + urllib . quote_plus ( name )
 OoOO0o += '&image=' + urllib . quote_plus ( image )
 OoOO0o += '&page=' + str ( page )
 if url != '' :
  OoOO0o += '&url=' + urllib . quote_plus ( url )
 if keyword :
  OoOO0o += '&keyword=' + urllib . quote_plus ( keyword )
 IioO0O = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  IioO0O . addContextMenuItems ( contextMenu )
 if infoLabels :
  IioO0O . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  IioO0O . setProperty ( "IsPlayable" , "true" )
 IioO0O . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = isFolder )
 if 20 - 20: oOoO0o00OO0 - iI11I1II1I1I . iiiiiiii1
 if 52 - 52: oOo - O0Oooo0O
def IiIiiiiI1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi )
 for url , iconimage , i11i1ii1I , I1I1 , name in iI111i :
  if 'http' in url :
   if '.php' in url :
    Ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
    for iIIi in Ii1 :
     if iIIi == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iiIii1I1Ii ( name , url , 1016 , iconimage , I1I1 , i11i1ii1I )
   else :
    if 'youtube' in url :
     Ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for iIIi in Ii1 :
      if iIIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1IIIo00oOOO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , I1I1 , i11i1ii1I )
    else :
     Ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for iIIi in Ii1 :
      if iIIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1IIIo00oOOO ( name , url , 222 , iconimage , I1I1 , i11i1ii1I )
     iIiIi11 ( 'tvshows' , 'Media Info 3' )
  else :
   iiiII1II1i ( url , iconimage , name )
   if 25 - 25: IIiIiII11i / OoOo0o + I1ii11iIi11i - iI11I1II1I1I - iii1i1iiiiIi
 else :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi )
  for url , oo0O0oO0O0O , name in iI111i :
   if 'http' in url :
    if '.php' in url :
     IIII ( name , url , 1016 , oo0O0oO0O0O )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      iI1iiiIiii ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo0O0oO0O0O )
     else :
      Ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
      for iIIi in Ii1 :
       if iIIi == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      iI1iiiIiii ( name , url , 222 , oo0O0oO0O0O )
      iIiIi11 ( 'tvshows' , 'Media Info 3' )
   else :
    iiiII1II1i ( url , oo0O0oO0O0O , name )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 97 - 97: OoOo0o . OoOo0o / oOoO0o00OO0 + oOo0O0Ooo * ooOoO0O00
def iiiII1II1i ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oo0OOo = ( url ) . replace ( ii1I1 , 'http' ) . replace ( o0oOOoO0o0 , '.com' ) ;
 I1I1I1iI11I1 = ( oo0OOo ) . replace ( ooOo0OooOooo , 'a' ) . replace ( o0OoO0 , 'b' ) . replace ( I11Ii1I1I , 'c' ) . replace ( Ii111 , 'd' ) . replace ( I1Ii1OOoo0Oo00 , 'e' ) . replace ( o0Oo00OoO000O , 'f' ) ;
 oO0oOoOo0O0 = ( I1I1I1iI11I1 ) . replace ( OOo0O0O000 , 'g' ) . replace ( oOoI11Iii1iIII1i , 'h' ) . replace ( oOOo0o0O0oO0o , 'i' ) . replace ( oooO000oO0O , 'j' ) . replace ( oo00OO0o0 , 'k' ) . replace ( o0oo0000Oo , 'l' ) ;
 oooOoO = ( oO0oOoOo0O0 ) . replace ( Ii1iIi , 'm' ) . replace ( iIiiiI1 , 'n' ) . replace ( IiIi1I1i1iII , 'o' ) . replace ( O0o000O0O0 , 'p' ) . replace ( IiIIiI1 , 'q' ) . replace ( OoOoOoOO0ooO000 , 'r' ) ;
 ooI11 = ( oooOoO ) . replace ( OOoOo0Oo , 's' ) . replace ( Ii11I111Ii , 't' ) . replace ( oOo0o0O , 'u' ) . replace ( I1I1Ii111 , 'v' ) . replace ( o0o0o0oO0oOoo , 'w' ) . replace ( Ooi1I11i1 , 'x' ) ;
 II1iiiii = ( ooI11 ) . replace ( iI11iIiIiiiI , 'y' ) . replace ( I1oo0Oo , 'z' ) . replace ( OOoO , '.' ) . replace ( oO0O , '(' ) . replace ( I11I11II11I , ')' ) . replace ( O00oo00O , '/' ) ;
 I1OO0Oo0 = ( II1iiiii ) . replace ( OoO0oO , '1' ) . replace ( iIiIIiIII1I , '2' ) . replace ( iI1IIiI1 , '3' ) . replace ( i1Ii1IiIii1I , '4' ) . replace ( i1iIII1Ii1 , '5' ) . replace ( iiIioo0O0 , '6' ) ;
 iIIii111i1 = ( I1OO0Oo0 ) . replace ( II1iii , '7' ) . replace ( O0oOOOO0o , '8' ) . replace ( OoOOO0 , '9' ) . replace ( IiIi , '0' ) . replace ( iiI1i111I1 , ':' ) . replace ( iiIi11i1I1 , '%' ) ;
 url = ( iIIii111i1 ) . replace ( OoOI1I , '-' ) . replace ( ooOOO000 , '_' ) ;
 iI1iiiIiii ( name , url , 222 , iconimage ) ;
 if 21 - 21: ooo0O + oOoO0o00OO0
 if 43 - 43: I1ii11iIi11i . ooOoO0O00 + ooOoO0O00
def OoOOo00O ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , oo0O0oO0O0O , O000OOO in iI111i :
  IIII ( O000OOO , IIo0o0O0O00oOOo , 1007 , oo0O0oO0O0O )
def IiIIIi11 ( url ) :
 if 1 - 1: ii + ii % oOo % OOOo00oo0oO - IIiIiII11i
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi )
 for url , oo0O0oO0O0O , O000OOO in iI111i :
  IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 1006 , oo0O0oO0O0O )
  if 7 - 7: o0o00Oo0O % I11i1ii1 / I1ii11iIi11i
def i1IiOO00O0o0 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 IiIi1ii111i1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 IiIi1ii111i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiIi1ii111i1 )
 if 85 - 85: iii1i1iiiiIi % oOOoOooOo * I11i1ii1 . iI11I1II1I1I - i1IiiiI1iI . OoOo0o
 if 93 - 93: o0o00Oo0O % oOo
def O0O000oOO0 ( url ) :
 IIi = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi )
 for url , Ii1IIiI1i , O000OOO in iI111i :
  if '-dir-' in O000OOO :
   IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , Ii1IIiI1i )
  else :
   IIII ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' , url , 1006 , Ii1IIiI1i )
   if 9 - 9: iiiiiiii1
def o0O0 ( url ) :
 IIi = II11iIII1i1I ( url )
 o00OO0000 = ( 'http://afewbitsmore.com/' )
 iI111i = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( IIi )
 for url , O000OOO in iI111i :
  if '[To Parent Directory]' in O000OOO :
   O000OOO = 'HOME'
   pass
  elif 'HOME' in O000OOO :
   pass
  elif '.m3u' in O000OOO :
   IIII ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , o00OO0000 + url , 2002 , I1IIIii + 'music.png' )
  elif '.mp3' in O000OOO :
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , o00OO0000 + url , 222 , I1IIIii + 'music.png' )
  elif '.m4a' in O000OOO :
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , o00OO0000 + url , 222 , I1IIIii + 'music.png' )
  else :
   IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) , o00OO0000 + url , 1012 , I1IIIii + 'music.png' )
def OOO0O0OO ( url ) :
 oOOo0 = II11iIII1i1I ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for Ii1IIiI1i , O000OOO , url in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , I1IIIii + 'music.png' )
  if 30 - 30: I1ii11iIi11i % ii * Ii % OOOo00oo0oO
def iii11I1I1i1 ( url ) :
 IIi = II11iIII1i1I ( url )
 o00OO0000 = url
 iI111i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( IIi )
 for url , O000OOO in iI111i :
  if '.mp3' in O000OOO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , I1IIIii + 'music.png' )
  else :
   IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '/' , '' ) , o00OO0000 + url , 1011 , I1IIIii + 'music.png' )
def OOoo ( ) :
 IIi = II11iIII1i1I ( o0oOoO00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iI111i = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIi )
 for IIo0o0O0O00oOOo , Ii1IIiI1i , O000OOO in iI111i :
  IIII ( O000OOO , ( 'http://www.cyn.net/music/' + IIo0o0O0O00oOOo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + Ii1IIiI1i ) . replace ( ' ' , '%20' ) )
def oooOoo0oo00OooOO ( url , img ) :
 IIi = II11iIII1i1I ( url )
 I1i = url
 img = img
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( I1i + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 72 - 72: O0Oooo0O * I11i1ii1 - ooOoO0O00 * ooo0O / i1IiiiI1iI
def IiI1i1i1 ( url ) :
 IIi = II11iIII1i1I ( url )
 I1i = url
 iI111i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi )
 for type , url , O000OOO in iI111i :
  if '[VID]' in type :
   iI1iiiIiii ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , I1i + url , 222 , I1IIIii + 'music.png' )
  if '[DIR]' in type :
   IiI1i1i1 ( I1i + url )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: iI11I1II1I1I - iii1i1iiiiIi - IIiIiII11i . I11i1ii1 / oOo - OOOo00oo0oO
 if 86 - 86: ii / o0o00Oo0O * iii1i1iiiiIi * OoOo0o . oOo
def I1iI1iiI1Ii1 ( ) :
 OO0O00O = ( o0oOoO00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 OOooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI = OOooo . lower ( )
 IIo0o0O0O00oOOo = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 oOO0 = ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1i = ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 15 - 15: ooo0O / I11i1ii1 / oOOoOooOo * iii1i1iiiiIi
 oOOo0 = i1Oo00 ( IIo0o0O0O00oOOo )
 Ii11iiI = i1Oo00 ( oOO0 )
 oo00O00oO = i1Oo00 ( I1i )
 if 13 - 13: iiiiiiii1
 if oOOo0 != 'Failed' :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for IIo0o0O0O00oOOo , OO00OOoO0o , i11i1ii1I , i1III1 , O000OOO in iI111i :
   if OOooo in O000OOO . lower ( ) :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , IIo0o0O0O00oOOo , 1016 , OO00OOoO0o , I1I1 , i11i1ii1I )
    if 69 - 69: Ii - Ii + i1IiiiI1iI / oOo0O0Ooo % oOoO0o00OO0
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if Ii11iiI != 'Failed' :
  I1iii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Ii11iiI )
  for IIo0o0O0O00oOOo , O000OOO in I1iii11 :
   if OOooo in O000OOO . lower ( ) :
    IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + IIo0o0O0O00oOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
    if 56 - 56: iI11I1II1I1I / oOo * OoOo0o
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( oo00O00oO )
  for IIo0o0O0O00oOOo , O000OOO in IIi11i1i1iI1 :
   if OOooo in O000OOO . lower ( ) :
    IIII ( ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + IIo0o0O0O00oOOo ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
    if 73 - 73: ii % I11i1ii1 / O0Oooo0O * i1IiiiI1iI + ooOoO0O00 % Ii
    iIiIi11 ( 'tvshows' , 'Media Info 3' )
    if 91 - 91: Ii
    if 6 - 6: o0o00Oo0O - iI11I1II1I1I + O0Oooo0O . ooo0O * Ii
    if 53 - 53: OoOo0o / oOo0O0Ooo / OOOo00oo0oO * OoOo0o / ooOoO0O00 - O0Oooo0O
    if 71 - 71: o0o00Oo0O + I1ii11iIi11i % OOOo00oo0oO - ooo0O
    if 82 - 82: iI11I1II1I1I
    if 64 - 64: oOOoOooOo + oOo0O0Ooo % OoOo0o + IIiIiII11i
Ii1iIi = '{SF},' ; iIiiiI1 = '{IF},' ; IiIi1I1i1iII = '{PW},' ; iI1IIiI1 = '{AM},' ; O0o000O0O0 = '{GF},' ; IiIIiI1 = '{DD},' ; OoOoOoOO0ooO000 = '{UO},' ; OOoOo0Oo = '{LE},' ; oOo0o0O = '{ZY},' ; I1I1Ii111 = '{UE},' ; o0o0o0oO0oOoo = '{PE},' ; Ooi1I11i1 = '{JE},' ; iI11iIiIiiiI = '{TH},' ; I1oo0Oo = '{LK},'
if 46 - 46: oOo0O0Ooo
if 72 - 72: iiiiiiii1
def oOo0o0 ( ) :
 IIi = i11111IIIII ( 'http://www.iwatchseries.me/tv-list/' )
 iI111i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( O000OOO , IIo0o0O0O00oOOo , 8021 , I1IIIii + 'iwatch.png' )
  iIiIi11 ( 'movies' , 'MAIN' )
def IIiiI11iI ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( IIi )
 for url , O000OOO , iI1 in iI111i :
  IIII ( O000OOO + iI1 , url , 8022 , I1IIIii + 'iwatch.png' )
def IIi1III1II ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIi )
 for url in iI111i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  o0o0OOOO ( url )
def o0o0OOOO ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIi )
 IIi11i1i1iI1 = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIi )
 iIIii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( IIi )
 o00O0O = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  iI1iiiIiii ( 'VidSpot - ' + O000OOO , url , 222 , I1IIIii + 'iwatch.png' )
 for url in IIi11i1i1iI1 :
  iI1iiiIiii ( 'VodLocker' , url , 222 , I1IIIii + 'iwatch.png' )
 for url , O000OOO in o00O0O :
  iI1iiiIiii ( 'VidUp' + O000OOO , url , 222 , I1IIIii + 'iwatch.png' )
 for O000OOO , url in iIIii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   iI1iiiIiii ( 'TheVideo - ' + O000OOO , url , 222 , I1IIIii + 'iwatch.png' )
   if 9 - 9: i1iIi * O0Oooo0O . ii / oOo
def Ii1iIiI1iI ( ) :
 IIi = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 iI111i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( O000OOO , IIo0o0O0O00oOOo , 1021 , I1IIIii + 'anime.png' )
  if 65 - 65: oOOoOooOo % IIiIiII11i . iiiiiiii1 - iI11I1II1I1I - oOo0O0Ooo
  if 63 - 63: oOo0O0Ooo . iii1i1iiiiIi - IIiIiII11i
def o0Oo000o ( ) :
 IIi = i11111IIIII ( 'http://www.animetoon.org/cartoon' )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIi )
 for IIo0o0O0O00oOOo , O000OOO in iI111i :
  IIII ( O000OOO , IIo0o0O0O00oOOo , 1002 , I1IIIii + 'anime.png' )
  if 78 - 78: O0Oooo0O
  if 39 - 39: oOoO0o00OO0 - iI11I1II1I1I * oOOoOooOo
  if 87 - 87: o0o00Oo0O + o0o00Oo0O - oOOoOooOo . Ii - I1ii11iIi11i * Ii
def o0o0O ( url ) :
 IIi = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIi )
 for Ii1IIiI1i in IIi11i1i1iI1 :
  I1ii11ii1iiI = Ii1IIiI1i
 iIIii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( IIi )
 for url in iIIii :
  IIII ( 'NEXT PAGE' , url , 1002 , I1IIIii + 'Next.png' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi )
 for url , O000OOO in iI111i :
  IIII ( O000OOO , url , 1003 , I1ii11ii1iiI )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooooooo ( url , IMAGE ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( IIi )
 for O000OOO , url in iI111i :
  print O000OOO + '     ' + url
  if 'easy' in url :
   ooO0ooO0O ( url )
  elif 'playpanda' in url :
   ooO0ooO0O ( url )
   if 65 - 65: ii * oOo * ooOoO0O00
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO0ooO0O ( url ) :
 IIi = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( IIi )
 for url in iI111i :
  iI1iiiIiii ( 'STREAM' , url , 222 , I1IIIii + 'anime.png' )
  if 12 - 12: I11i1ii1 + oOOoOooOo . Ii - iI11I1II1I1I
  if 27 - 27: i1IiiiI1iI + iI11I1II1I1I
def OO0O00 ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i . add_header ( 'referer' , url )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 33 - 33: iiiiiiii1 % oOo0O0Ooo % oOOoOooOo * oOo + iii1i1iiiiIi % Ii
def II11iIII1i1I ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 39 - 39: I1ii11iIi11i % O0Oooo0O / oOo0O0Ooo / I1ii11iIi11i . ooo0O + ooo0O
def oo0ooo0o0OOO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iioOoO0oOO = ( '%s%s' % ( OOo0ooOOO , url ) )
 IIIi1I1IIii1II = II11iIII1i1I ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , oo0O0oO0O0O , O000OOO in iI111i :
  iI1iiiIiii ( '%s' % ( '[COLOR' + iiI1IiI + ']' + O000OOO + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oo0O0oO0O0O )
  if 17 - 17: oOo + IIiIiII11i + oOo0O0Ooo
def IIIiIIi1I1I ( url ) :
 if O0oo0OO0 . getSetting ( 'down' ) == 'true' :
  Ii1III11ii1 ( url , O000OOO )
 else :
  oo0 ( url )
def oo0 ( url ) :
 import urlresolver
 try :
  OOOo00 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OOOo00 , xbmcgui . ListItem ( O000OOO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( O000OOO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def II11IiI1 ( url ) :
 if 4 - 4: iii1i1iiiiIi / i1IiiiI1iI
 OOOoI1iI1IiI = open ( O0Oo000ooO00 , "a" )
 OOOoI1iI1IiI . write ( 'url="' + url + '"\n' )
 OOOoI1iI1IiI . close
 if 1 - 1: O0Oooo0O / i1iIi % oOoO0o00OO0
 Oo00o000oOO = xbmc . Player ( ii1i1iiI ( ) )
 import urlresolver
 try : Oo00o000oOO . play ( url )
 except : pass
 from urlresolver import common
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'LOADING' , 'Opening %s Now' % ( O000OOO ) )
 Oo00o000oOO = xbmc . Player ( ii1i1iiI ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oO0 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : Oo00o000oOO . play ( url )
  except : pass
  try : O0oo0OO0 . resolve_url ( url )
  except : pass
  o0oO0 . close ( )
def Ii1III11ii1 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  ii1i1 = '.mp4'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.mkv' in url :
  ii1i1 = '.mkv'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.mp3' in url :
  ii1i1 = '.mp3'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.avi' in url :
  ii1i1 = '.avi'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.mov' in url :
  ii1i1 = '.mov'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.mpeg' in url :
  ii1i1 = '.mpeg'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.mpg' in url :
  ii1i1 = '.mpg'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.flv' in url :
  ii1i1 = '.flv'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 elif '.wmv' in url :
  ii1i1 = '.wmv'
  I11iIi1i1II11 = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , I11iIi1i1II11 )
  if iiI == 0 :
   oo0 ( url )
  if iiI == 1 :
   oOo0oO000oOo ( url , name , ii1i1 )
 else :
  oo0 ( url )
def oOo0oO000oOo ( url , name , cat ) :
 iiii1i1iiIiI1 ( )
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( II ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 oo0O00Oooo0O0 = os . path . join ( OoOoo00Ooo00 , file )
 try :
  os . remove ( oo0O00Oooo0O0 )
 except :
  pass
 downloader . download ( url , oo0O00Oooo0O0 , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def iiii1i1iiIiI1 ( ) :
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( II ) )
 if not os . path . exists ( II ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
def i11ii ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oO0 . update ( 0 , '%s' % O000OOO )
 xbmc . sleep ( 1 )
 Oo00o000oOO = xbmc . Player ( ii1i1iiI ( ) )
 o0oO0 . update ( 100 , '%s' % O000OOO )
 xbmc . sleep ( 1 )
 Oo00o000oOO . play ( url ) . strip ( )
 o0oO0 . close ( )
 if 50 - 50: ii % i1IiiiI1iI % iI11I1II1I1I . oOoO0o00OO0 - I11i1ii1 / oOo
def i1i1I1 ( url ) :
 Oo00o000oOO = xbmc . Player ( ii1i1iiI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : Oo00o000oOO . play ( url ) . strip ( )
 except : pass
 if 19 - 19: oOoO0o00OO0 / I1ii11iIi11i * ii
def oOiIi1i1111I ( url ) :
 Oo00o000oOO = xbmc . Player ( ii1i1iiI ( ) )
 import urlresolver
 oOo0oOo0 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 Oo00o000oOO . play ( oOo0oOo0 )
 xbmc . sleep ( 1 )
 Oo00o000oOO . play ( url )
 if 14 - 14: oOo * ii
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . iii1i1iiiiIi
def ii1i1iiI ( ) :
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
def IIII ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OOoo0oOO00 = [ ]
  OOoo0oOO00 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OOoo0oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   OOoo0oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IioO0O . addContextMenuItems ( OOoo0oOO00 )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = True )
 return oo0O0o
 if 95 - 95: oOo0O0Ooo . OOOo00oo0oO
def iiiI1ii ( name , url , mode , iconimage , fanart , description ) :
 if 60 - 60: iiiiiiii1
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = True )
 return oo0O0o
 if 92 - 92: ooOoO0O00 + O0Oooo0O % ooOoO0O00 * iiiiiiii1 % ooo0O
def iI1iiiIiii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OOoo0oOO00 = [ ]
  OOoo0oOO00 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OOoo0oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   OOoo0oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IioO0O . addContextMenuItems ( OOoo0oOO00 )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = False )
 return oo0O0o
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
   try : Iiii1iI1i = open ( announce ) ; I1111i1 = Iiii1iI1i . read ( )
   except : I1111i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1111i1 ) )
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
   try : Iiii1iI1i = open ( announce ) ; I1111i1 = Iiii1iI1i . read ( )
   except : I1111i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1111i1 ) )
   return
 OoOoO ( )
 OoOoO ( )
def oo00o0 ( ) :
 i111iiiI1iiI ( I1IIIii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 23 - 23: oOoO0o00OO0 . oOoO0o00OO0 / oOo0O0Ooo . ooOoO0O00
 if 47 - 47: Ii . ooo0O . Ii + oOo0O0Ooo - oOoO0o00OO0
 if 62 - 62: ii + oOo0O0Ooo / oOOoOooOo . i1iIi . I1ii11iIi11i
 if 81 - 81: OOOo00oo0oO + I11i1ii1
 if 75 - 75: o0o00Oo0O + oOoO0o00OO0
def OO0 ( ) :
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
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 75 - 75: o0o00Oo0O - iI11I1II1I1I + iii1i1iiiiIi . Ii - ooo0O
def IIi1III11I1Ii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Oooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 80 - 80: i1IiiiI1iI + ooo0O - O0Oooo0O . oOo * OOOo00oo0oO + OoOo0o
def Oo0ooO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o000oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 61 - 61: ooo0O * o0o00Oo0O
def o0O0oO00oo0O ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1iIOo0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 4 - 4: OOOo00oo0oO / iii1i1iiiiIi . I1ii11iIi11i . ooo0O / ooOoO0O00 / OoOo0o
def OOO0i1Ii1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + O0oO0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 95 - 95: oOo + ii
def O0Oo0OOoo00Oo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iIi1IIII1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 70 - 70: oOoO0o00OO0 * iii1i1iiiiIi
def O0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + OOO0o00OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 21 - 21: O0Oooo0O + iii1i1iiiiIi + iii1i1iiiiIi . IIiIiII11i / O0Oooo0O . oOo0O0Ooo
def O0oO00o0O0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 32 - 32: oOOoOooOo / I11i1ii1
def Iii11iIII1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + II1IiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 42 , OO00OOoO0o , I1I1 , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 50 - 50: i1IiiiI1iI - I11i1ii1
def IIIIiI11I11 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + ii111II1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for O000OOO , url , OO00OOoO0o , I1I1 , oO0O0oO0 in iI111i :
  o00oOOooOOo0o ( O000OOO , url , 5 , I1IIIii + 'GenieTVRSSFeed.png' , I1IIIii + 'GenieTVRSSFeed.png' , oO0O0oO0 )
 iIiIi11 ( 'movies' , 'MAIN' )
 if 78 - 78: ii
 if 39 - 39: oOoO0o00OO0 / Ii * ooOoO0O00 * I1ii11iIi11i
 if 39 - 39: oOo * ii / ooOoO0O00 + I1ii11iIi11i
 if 57 - 57: o0o00Oo0O
 if 83 - 83: OoOo0o / i1iIi * oOo0O0Ooo % OOOo00oo0oO / iI11I1II1I1I
 if 1 - 1: i1IiiiI1iI / ii / iiiiiiii1
 if 68 - 68: ooOoO0O00 / I1ii11iIi11i / i1IiiiI1iI * I1ii11iIi11i
 if 91 - 91: oOo . iiiiiiii1
 if 82 - 82: oOoO0o00OO0 / I1ii11iIi11i
def oooO0 ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( o0 ) :
     o0O000O0000oO = 0
     o0O000O0000oO += len ( oOoO )
     if o0O000O0000oO > 0 :
      for Iiii1iI1i in oOoO :
       os . unlink ( os . path . join ( oooO0O0o00o , Iiii1iI1i ) )
  Oooo0Oo = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( Oooo0Oo )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 46 - 46: Ii - i1iIi % iI11I1II1I1I + iii1i1iiiiIi - O0Oooo0O
 if 99 - 99: oOo - oOOoOooOo + oOoO0o00OO0 + IIiIiII11i - Ii
 if 71 - 71: OOOo00oo0oO * I11i1ii1 * oOo
 if 6 - 6: O0Oooo0O - oOOoOooOo . ooo0O / oOOoOooOo % oOo * oOo0O0Ooo
 if 49 - 49: oOo0O0Ooo + o0o00Oo0O - i1IiiiI1iI
 if 43 - 43: o0o00Oo0O
 if 50 - 50: i1IiiiI1iI - ii
 if 29 - 29: OOOo00oo0oO * OOOo00oo0oO
def o0OoOO ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 44 - 44: oOOoOooOo . oOo0O0Ooo * OOOo00oo0oO * i1iIi
def IiIi11iiIi1 ( url ) :
 Iii1i1ii1i1 = os . path . join ( oO0o0o0ooO0oO , 'addon_data' )
 IiiiiiiI111i = [
 ( Iii1i1ii1i1 ) ,
 ( I11 ) ,
 ( os . path . join ( i1111 , 'cache' ) ) ,
 ( os . path . join ( i1111 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( Iii1i1ii1i1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Iii1i1ii1i1 , 'plugin.video.itv' , 'Images' ) ) ]
 if 54 - 54: oOo / oOo0O0Ooo
 i1O0OoO0O0O0oO = 0
 if 58 - 58: oOoO0o00OO0 + I1ii11iIi11i . I1ii11iIi11i / iiiiiiii1 . Ii
 for iIIi in IiiiiiiI111i :
  if os . path . exists ( iIIi ) and not iIIi in [ I11 , Iii1i1ii1i1 ] :
   for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( iIIi ) :
    o0O000O0000oO = 0
    o0O000O0000oO += len ( oOoO )
    if o0O000O0000oO > 0 :
     for Iiii1iI1i in oOoO :
      if not Iiii1iI1i in oo0o0O00 :
       try :
        os . unlink ( os . path . join ( oooO0O0o00o , Iiii1iI1i ) )
       except :
        pass
      else : iiIoO ( 'Ignore Log File: %s' % Iiii1iI1i )
     for o0o0oo0OOo0O0 in oo0OOO0OOoOO :
      try :
       shutil . rmtree ( os . path . join ( oooO0O0o00o , o0o0oo0OOo0O0 ) )
       i1O0OoO0O0O0oO += 1
       iiIoO ( "[Success] cleared %s files from %s" % ( str ( o0O000O0000oO ) , os . path . join ( iIIi , o0o0oo0OOo0O0 ) ) )
      except :
       iiIoO ( "[Failed] to wipe cache in: %s" % os . path . join ( iIIi , o0o0oo0OOo0O0 ) )
  else :
   for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( iIIi ) :
    for o0o0oo0OOo0O0 in oo0OOO0OOoOO :
     if 'cache' in o0o0oo0OOo0O0 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( oooO0O0o00o , o0o0oo0OOo0O0 ) )
       i1O0OoO0O0O0oO += 1
       iiIoO ( "[Success] wiped %s " % os . path . join ( iIIi , o0o0oo0OOo0O0 ) )
      except :
       iiIoO ( "[Failed] to wipe cache in: %s" % os . path . join ( iIIi , o0o0oo0OOo0O0 ) )
       if 8 - 8: oOoO0o00OO0 + o0o00Oo0O - OOOo00oo0oO % IIiIiII11i . O0Oooo0O
 o0OoOO ( oOo0oooo00o , 'Clear Cache: Removed %s Files' % i1O0OoO0O0O0oO )
 if 86 - 86: I11i1ii1
 if 71 - 71: i1iIi - ooOoO0O00 . oOo0O0Ooo
 if 15 - 15: ooOoO0O00 % IIiIiII11i / IIiIiII11i - oOoO0o00OO0 - i1IiiiI1iI % ooOoO0O00
 if 54 - 54: ooOoO0O00 . oOo + iiiiiiii1 + oOo * ooOoO0O00
 if 13 - 13: I1ii11iIi11i / oOo + OoOo0o
 if 90 - 90: oOo * Ii / OOOo00oo0oO
 if 91 - 91: iiiiiiii1 - iii1i1iiiiIi / I1ii11iIi11i % IIiIiII11i / IIiIiII11i / ooo0O
def IIIi1i1iIIIi ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 oOOoOoooOo0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( oOOoOoooOo0o ) :
   o0O000O0000oO = 0
   o0O000O0000oO += len ( oOoO )
   if 59 - 59: Ii - i1IiiiI1iI * I1ii11iIi11i % ooo0O + ooOoO0O00
   if 30 - 30: oOOoOooOo / iiiiiiii1
   if o0O000O0000oO > 0 :
    if 66 - 66: oOOoOooOo / I11i1ii1 * iI11I1II1I1I
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( o0O000O0000oO ) + " files found" , "Do you want to delete them?" ) :
     if 42 - 42: O0Oooo0O - Ii % IIiIiII11i * oOOoOooOo . o0o00Oo0O % i1IiiiI1iI
     for Iiii1iI1i in oOoO :
      os . unlink ( os . path . join ( oooO0O0o00o , Iiii1iI1i ) )
     for o0o0oo0OOo0O0 in oo0OOO0OOoOO :
      shutil . rmtree ( os . path . join ( oooO0O0o00o , o0o0oo0OOo0O0 ) )
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
 ooOo0Ooo0 ( )
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
def o0O0oo0OO0O ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 oOOoOoooOo0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( oOOoOoooOo0o ) :
   o0O000O0000oO = 0
   o0O000O0000oO += len ( oOoO )
   if 75 - 75: IIiIiII11i / iI11I1II1I1I / ii
   if 61 - 61: I11i1ii1 . I11i1ii1
   if o0O000O0000oO > 0 :
    if 17 - 17: iii1i1iiiiIi % I1ii11iIi11i / O0Oooo0O . i1iIi % oOo
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( o0O000O0000oO ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: oOo0O0Ooo + oOOoOooOo / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
     for Iiii1iI1i in oOoO :
      os . unlink ( os . path . join ( oooO0O0o00o , Iiii1iI1i ) )
     for o0o0oo0OOo0O0 in oo0OOO0OOoOO :
      shutil . rmtree ( os . path . join ( oooO0O0o00o , o0o0oo0OOo0O0 ) )
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
 IiIi11iiIi1 ( url )
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
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11 = os . path . join ( OoOoo00Ooo00 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 OOo0oO = os . path . join ( OoOoo00Ooo00 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOo0oO ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + oo00 + ' - ADVANCED XML###'
   OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iii11 = os . path . join ( OoOoo00Ooo00 , 'advancedsettings.xml' )
   try :
    os . remove ( iii11 )
    print '=== GenieTv - REMOVING    ' + str ( iii11 ) + '    ==='
   except :
    pass
   IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
   iII1ii1 = open ( iii11 , "w" )
   iII1ii1 . write ( IIIi1I1IIii1II )
   iII1ii1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 else :
  print '###' + oo00 + ' - ADVANCED XML###'
  OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iii11 = os . path . join ( OoOoo00Ooo00 , 'advancedsettings.xml' )
  try :
   os . remove ( iii11 )
   print '=== GenieTv - REMOVING    ' + str ( iii11 ) + '    ==='
  except :
   pass
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iII1ii1 = open ( iii11 , "w" )
  iII1ii1 . write ( IIIi1I1IIii1II )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 return
 if 84 - 84: oOo0O0Ooo % oOo0O0Ooo * i1iIi
def oo00OOooo ( url , name ) :
 print '###' + oo00 + ' - CHECK ADVANCE XML###'
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11 = os . path . join ( OoOoo00Ooo00 , 'advancedsettings.xml' )
 try :
  iII1ii1 = open ( iii11 ) . read ( )
  if 'zero' in iII1ii1 :
   name = '0CACHE'
  elif 'tuxen' in iII1ii1 :
   name = 'TUXENS'
  elif 'muckys' in iII1ii1 :
   name = 'MUCKYS'
  elif 'p2p1' in iII1ii1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iII1ii1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iII1ii1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( oo00 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 62 - 62: oOo . OoOo0o . OOOo00oo0oO + o0o00Oo0O % o0o00Oo0O
def OOoOo0Oo00 ( url ) :
 print '###' + oo00 + ' - DELETING ADVANCE XML###'
 OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iii11 = os . path . join ( OoOoo00Ooo00 , 'advancedsettings.xml' )
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
 for iIIII1i1 , Ii11iii , ooI1111i , o0OOOO in iI111i :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iIIII1i1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % ooI1111i , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % o0OOOO )
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
  OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iii11 = os . path . join ( OoOoo00Ooo00 , 'addons2.ini' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iII1ii1 = open ( iii11 , "w" )
  iII1ii1 . write ( IIIi1I1IIii1II )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New .ini File" )
 return
 if 79 - 79: O0Oooo0O - i1IiiiI1iI
def Ii1iI1I ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + oo00 + ' - CUSTOM FTV SETTINGS###'
  OoOoo00Ooo00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iii11 = os . path . join ( OoOoo00Ooo00 , 'settings.xml' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iII1ii1 = open ( iii11 , "w" )
  iII1ii1 . write ( IIIi1I1IIii1II )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iii11 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New Settings" )
 return
 if 89 - 89: oOo0O0Ooo + i1IiiiI1iI . OOOo00oo0oO . IIiIiII11i + OOOo00oo0oO / I1ii11iIi11i
 if 32 - 32: oOo % OOOo00oo0oO * oOoO0o00OO0 + i1IiiiI1iI / O0Oooo0O
def IIi1Ii ( ) :
 try :
  IIIii = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IIIii ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    i1iIiIII = os . path . join ( IIIii , "source.db" )
    os . unlink ( i1iIiIII )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "               Error Deleting Database No Database To Delete" )
 return
 if 52 - 52: Ii - o0o00Oo0O
 if 64 - 64: Ii . O0Oooo0O / o0o00Oo0O - I11i1ii1
 if 88 - 88: i1iIi / oOo - i1IiiiI1iI
 if 11 - 11: oOo / ooOoO0O00 . ii
 if 40 - 40: I11i1ii1 + iiiiiiii1 * i1IiiiI1iI + iii1i1iiiiIi
def i11111IIIII ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 5 - 5: O0Oooo0O / I11i1ii1
 if 30 - 30: OoOo0o . iiiiiiii1 % oOo + OOOo00oo0oO
 if 69 - 69: Ii + I11i1ii1 * oOOoOooOo * iiiiiiii1 % OOOo00oo0oO
 if 66 - 66: OoOo0o * I11i1ii1 + o0o00Oo0O - ii
 if 19 - 19: I1ii11iIi11i * iii1i1iiiiIi
 if 52 - 52: oOo + OOOo00oo0oO
 if 84 - 84: o0o00Oo0O % oOoO0o00OO0 % iI11I1II1I1I - iii1i1iiiiIi - I1ii11iIi11i
def o000O000 ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; Ii1Iiii1Ii = pluginmessage_yes_no ( oo00 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if Ii1Iiii1Ii :
  OOOOOOOo = xbmcaddon . Addon ( id = iiIIIII1i1iI ) . getAddonInfo ( 'path' ) ; OOOOOOOo = xbmc . translatePath ( OOOOOOOo ) ;
  ooOO0O = os . path . join ( OOOOOOOo , ".." , ".." ) ; ooOO0O = os . path . abspath ( ooOO0O ) ; pluginlog ( "freshstart.main_list xbmcPath=" + ooOO0O ) ; IIIIII1 = False
  try :
   for oooO0O0o00o , oo0OOO0OOoOO , oOoO in os . walk ( ooOO0O , topdown = True ) :
    oo0OOO0OOoOO [ : ] = [ o0o0oo0OOo0O0 for o0o0oo0OOo0O0 in oo0OOO0OOoOO if o0o0oo0OOo0O0 not in i1i1II ]
    for O000OOO in oOoO :
     try : os . remove ( os . path . join ( oooO0O0o00o , O000OOO ) )
     except :
      if O000OOO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIIIII1 = True
      pluginlog ( "Error removing " + oooO0O0o00o + " " + O000OOO )
    for O000OOO in oo0OOO0OOoOO :
     try : os . rmdir ( os . path . join ( oooO0O0o00o , O000OOO ) )
     except :
      if O000OOO not in [ "Database" , "userdata" ] : IIIIII1 = True
      pluginlog ( "Error removing " + oooO0O0o00o + " " + O000OOO )
   if not IIIIII1 : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( oo00 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( oo00 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 iIIoooO0 ( )
 if 73 - 73: OOOo00oo0oO / iii1i1iiiiIi * OoOo0o * iI11I1II1I1I / ooOoO0O00
 if 60 - 60: OoOo0o * O0Oooo0O . OOOo00oo0oO
 if 47 - 47: OOOo00oo0oO % OoOo0o / OoOo0o % iii1i1iiiiIi % O0Oooo0O / iii1i1iiiiIi
def oOOoO0ii1I1Ii11 ( ) :
 OO0OOOO = [ ]
 I1Iiiii1 = sys . argv [ 2 ]
 if len ( I1Iiiii1 ) >= 2 :
  ii1 = sys . argv [ 2 ]
  OoOo00O = ii1 . replace ( '?' , '' )
  if ( ii1 [ len ( ii1 ) - 1 ] == '/' ) :
   ii1 = ii1 [ 0 : len ( ii1 ) - 2 ]
  o0O00ooO0O0Oo = OoOo00O . split ( '&' )
  OO0OOOO = { }
  for O0o000Oo in range ( len ( o0O00ooO0O0Oo ) ) :
   ooOo0ooO0Oo = { }
   ooOo0ooO0Oo = o0O00ooO0O0Oo [ O0o000Oo ] . split ( '=' )
   if ( len ( ooOo0ooO0Oo ) ) == 2 :
    OO0OOOO [ ooOo0ooO0Oo [ 0 ] ] = ooOo0ooO0Oo [ 1 ]
    if 11 - 11: iii1i1iiiiIi * IIiIiII11i % ooo0O . ii % ooo0O
 return OO0OOOO
 if 32 - 32: O0Oooo0O
I1iI1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
IiI1Ii11Iiii = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I1iII1II1I1ii = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
IiI1I1 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
ooooo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
IIIiIi = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o000oOOoooo0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i11IiiI1iIi = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
Oooo0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o000oO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
i1iIOo0oOOo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
O0oO0o00 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iIi1IIII1iI = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OOO0o00OOo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
i1iII = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
II1IiIIi = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o0O0OoO0oOO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o0o00O000o0o = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OO0ooo0OOO = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OooOoOO0OO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oOooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oOoOOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
ii111II1Ii1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOo0ooOOO = base64 . decodestring ( 'Q1VOVA==' )
def OO00oOO0Oo ( display , mode = None , name = None , url = None , menu = None , description = oOo0oooo00o , overwrite = True , fanart = Oo00OOOOO , icon = O0O , themeit = None ) :
 OoOO0o = sys . argv [ 0 ]
 if not mode == None : OoOO0o += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OoOO0o += "&name=" + urllib . quote_plus ( name )
 if not url == None : OoOO0o += "&url=" + urllib . quote_plus ( url )
 oo0O0o = True
 if themeit : display = themeit % display
 IioO0O = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : IioO0O . addContextMenuItems ( menu , replaceItems = overwrite )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = False )
 return oo0O0o
def Oo0o0O0OOOo0 ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 IioO0O . setProperty ( 'fanart_image' , fanart )
 IioO0O . setProperty ( "IsPlayable" , "true" )
 OO00o00000oO0 = [ ]
 OO00o00000oO0 . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 OO00o00000oO0 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 IioO0O . addContextMenuItems ( OO00o00000oO0 , replaceItems = True )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = False )
 return oo0O0o
def o00oOOooOOo0o ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOoo0oOO00 = [ ]
  if showcontext == 'fav' :
   OOoo0oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   OOoo0oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IioO0O . addContextMenuItems ( OOoo0oOO00 )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = True )
 return oo0O0o
 if 40 - 40: iiiiiiii1 . oOOoOooOo % ii % OoOo0o / ii / I1ii11iIi11i
def O0O0ooOOO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OoOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0O0o = True
 IioO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IioO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IioO0O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOoo0oOO00 = [ ]
  if showcontext == 'fav' :
   OOoo0oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   OOoo0oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IioO0O . addContextMenuItems ( OOoo0oOO00 )
 oo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0o , listitem = IioO0O , isFolder = False )
 return oo0O0o
 if 93 - 93: ooo0O % iI11I1II1I1I % OOOo00oo0oO / oOo0O0Ooo
 if 98 - 98: IIiIiII11i + I1ii11iIi11i - ooOoO0O00 + iiiiiiii1 + IIiIiII11i
ii1 = oOOoO0ii1I1Ii11 ( )
IIo0o0O0O00oOOo = None
O000OOO = None
iIi1i = None
OO00OOoO0o = None
I1I1 = None
oO0O0oO0 = None
IIi11i = None
o0OOo0o00 = None
if 15 - 15: OOOo00oo0oO % iI11I1II1I1I
if 60 - 60: oOo * o0o00Oo0O / i1iIi
try :
 o0OOo0o00 = int ( ii1 [ "fav_mode" ] )
except :
 pass
 if 28 - 28: I1ii11iIi11i . Ii . o0o00Oo0O
try :
 IIo0o0O0O00oOOo = urllib . unquote_plus ( ii1 [ "url" ] )
except :
 pass
try :
 O000OOO = urllib . unquote_plus ( ii1 [ "name" ] )
except :
 pass
try :
 OO00OOoO0o = urllib . unquote_plus ( ii1 [ "iconimage" ] )
except :
 pass
try :
 iIi1i = int ( ii1 [ "mode" ] )
except :
 pass
try :
 I1I1 = urllib . unquote_plus ( ii1 [ "fanart" ] )
except :
 pass
try :
 oO0O0oO0 = urllib . unquote_plus ( ii1 [ "description" ] )
except :
 pass
 if 67 - 67: IIiIiII11i / o0o00Oo0O
 if 10 - 10: ooOoO0O00 / I1ii11iIi11i
print str ( I11II1i ) + ': ' + str ( I1IiI )
print "Mode: " + str ( iIi1i )
print "URL: " + str ( IIo0o0O0O00oOOo )
print "Name: " + str ( O000OOO )
print "IconImage: " + str ( OO00OOoO0o )
if 20 - 20: I1ii11iIi11i * O0Oooo0O / oOoO0o00OO0 . oOOoOooOo
if 67 - 67: ooo0O . I1ii11iIi11i % i1IiiiI1iI
def iIiIi11 ( content , viewType ) :
 if 38 - 38: OoOo0o - oOo . oOOoOooOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 50 - 50: ooo0O
if OO00OOoO0o == None : OO00OOoO0o = O0O
if I1I1 == None : I1I1 = Oo00OOOOO
if iIi1i == None :
 O00o0OO0 ( )
 if 85 - 85: IIiIiII11i . iiiiiiii1 - ooOoO0O00
elif iIi1i == 1 :
 OoOooooo ( IIo0o0O0O00oOOo )
 if 23 - 23: iiiiiiii1 . i1iIi - oOo / oOoO0o00OO0 / o0o00Oo0O
elif iIi1i == 44 :
 oOoO0o0ooo ( IIo0o0O0O00oOOo )
 if 4 - 4: ooOoO0O00 % I1ii11iIi11i % i1iIi * oOOoOooOo - i1IiiiI1iI
elif iIi1i == 2 :
 IIiII ( )
 if 76 - 76: iI11I1II1I1I / oOOoOooOo % oOoO0o00OO0 % OoOo0o
elif iIi1i == 3 :
 oo0OoO ( )
 if 13 - 13: I11i1ii1
elif iIi1i == 21 :
 Iii1ii1II11i ( )
 if 56 - 56: I1ii11iIi11i
elif iIi1i == 4 :
 iiii1i1 ( )
 if 55 - 55: Ii + iI11I1II1I1I / ooOoO0O00 / oOoO0o00OO0
elif iIi1i == 5 :
 oO0o00O ( IIo0o0O0O00oOOo )
 if 64 - 64: I11i1ii1 . oOo * Ii
elif iIi1i == 6 :
 IIIi1i1iIIIi ( IIo0o0O0O00oOOo )
 if 18 - 18: i1iIi % ooo0O - I1ii11iIi11i
elif iIi1i == 7 :
 ii1iII11 ( IIo0o0O0O00oOOo , O000OOO )
 if 28 - 28: I11i1ii1
elif iIi1i == 8 :
 oo00OOooo ( IIo0o0O0O00oOOo , O000OOO )
 if 93 - 93: I1ii11iIi11i % ooOoO0O00
elif iIi1i == 9 :
 FIXREPOSADDONS ( IIo0o0O0O00oOOo )
 if 51 - 51: OOOo00oo0oO % o0o00Oo0O
elif iIi1i == 10 :
 OO0 ( )
 if 41 - 41: oOo0O0Ooo * oOo0O0Ooo . O0Oooo0O
elif iIi1i == 11 :
 OOoOo0Oo00 ( IIo0o0O0O00oOOo )
 if 38 - 38: oOo0O0Ooo % Ii
elif iIi1i == 12 :
 III1I11I1i ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 17 - 17: Ii
elif iIi1i == 13 :
 oooO0 ( )
 if 81 - 81: O0Oooo0O
elif iIi1i == 14 :
 IiIi11iiIi1 ( IIo0o0O0O00oOOo )
 if 25 - 25: oOo0O0Ooo
elif iIi1i == 15 :
 I1I ( )
 if 52 - 52: oOoO0o00OO0 % ooOoO0O00 . I11i1ii1 % iii1i1iiiiIi
elif iIi1i == 16 :
 iIiIi1iI ( IIo0o0O0O00oOOo , O000OOO )
 if 50 - 50: OoOo0o * oOo0O0Ooo / ooo0O
elif iIi1i == 17 :
 Ii1iI1I ( IIo0o0O0O00oOOo , O000OOO )
 if 91 - 91: iI11I1II1I1I / OoOo0o * o0o00Oo0O . ooo0O + OOOo00oo0oO / oOoO0o00OO0
elif iIi1i == 18 :
 IIi1Ii ( )
 if 33 - 33: IIiIiII11i + i1iIi
elif iIi1i == 19 :
 iiIII1i ( IIo0o0O0O00oOOo )
 if 46 - 46: I11i1ii1 + o0o00Oo0O + ooOoO0O00 + oOOoOooOo / iiiiiiii1
elif iIi1i == 40 :
 I11IIIIiII ( O000OOO , IIo0o0O0O00oOOo , oO0O0oO0 )
 if 94 - 94: OOOo00oo0oO + iiiiiiii1 * iii1i1iiiiIi - ooOoO0O00 / ii
elif iIi1i == 42 :
 I11I111i ( O000OOO , IIo0o0O0O00oOOo , oO0O0oO0 )
 if 59 - 59: i1IiiiI1iI % i1iIi / iii1i1iiiiIi
elif iIi1i == 43 :
 I1iiIIIIIIII ( IIo0o0O0O00oOOo )
 if 99 - 99: i1iIi + IIiIiII11i / Ii - I11i1ii1 / iiiiiiii1 + iiiiiiii1
elif iIi1i == 20 :
 IiIOOOoo ( IIo0o0O0O00oOOo )
 if 55 - 55: I11i1ii1 + ii * oOoO0o00OO0 . I11i1ii1 * oOoO0o00OO0 + I11i1ii1
elif iIi1i == 22 :
 IIIIi11 ( IIo0o0O0O00oOOo )
 if 81 - 81: iI11I1II1I1I . oOOoOooOo + iii1i1iiiiIi
elif iIi1i == 23 :
 IIi1III11I1Ii ( IIo0o0O0O00oOOo )
 if 31 - 31: i1IiiiI1iI / iii1i1iiiiIi + ooo0O
elif iIi1i == 24 :
 Oo0ooO ( IIo0o0O0O00oOOo )
 if 80 - 80: I1ii11iIi11i
elif iIi1i == 25 :
 o0O0oO00oo0O ( IIo0o0O0O00oOOo )
 if 58 - 58: O0Oooo0O + OoOo0o
elif iIi1i == 26 :
 OOO0i1Ii1 ( IIo0o0O0O00oOOo )
 if 76 - 76: IIiIiII11i - ooo0O % oOo + iiiiiiii1
elif iIi1i == 27 :
 O0Oo0OOoo00Oo ( IIo0o0O0O00oOOo )
 if 38 - 38: O0Oooo0O - i1IiiiI1iI * ooOoO0O00 + iI11I1II1I1I
elif iIi1i == 28 :
 O0 ( IIo0o0O0O00oOOo )
 if 41 - 41: i1iIi . oOo + oOoO0o00OO0 + iii1i1iiiiIi
elif iIi1i == 29 :
 O0oO00o0O0 ( IIo0o0O0O00oOOo )
 if 76 - 76: iiiiiiii1 - iI11I1II1I1I
elif iIi1i == 30 :
 o00OOOoO000 ( IIo0o0O0O00oOOo )
 if 23 - 23: i1IiiiI1iI / oOo % OoOo0o
elif iIi1i == 31 :
 Iii11iIII1 ( IIo0o0O0O00oOOo )
 if 9 - 9: oOOoOooOo % oOoO0o00OO0 . ii + oOo % OoOo0o * ii
elif iIi1i == 32 :
 O0Oo00o0o ( )
 if 21 - 21: i1iIi % o0o00Oo0O
elif iIi1i == 33 :
 oooooO0oO0o ( )
 if 15 - 15: IIiIiII11i * i1iIi + I11i1ii1 % iiiiiiii1
elif iIi1i == 35 :
 oOOo0OOOOo0o ( IIo0o0O0O00oOOo )
 if 96 - 96: IIiIiII11i * O0Oooo0O / I1ii11iIi11i
elif iIi1i == 34 :
 O0ooo0Ooo ( IIo0o0O0O00oOOo )
 if 35 - 35: oOo0O0Ooo
elif iIi1i == 36 :
 OoOoooOO00OO ( IIo0o0O0O00oOOo )
 if 54 - 54: oOoO0o00OO0 % ooo0O . ooOoO0O00
elif iIi1i == 37 :
 i11iII1 ( IIo0o0O0O00oOOo )
 if 72 - 72: i1iIi
elif iIi1i == 38 :
 O0oo0O00ooOo ( IIo0o0O0O00oOOo )
 if 87 - 87: iiiiiiii1 - oOo0O0Ooo
elif iIi1i == 41 :
 o000O000 ( ii1 )
 if 54 - 54: iI11I1II1I1I + OOOo00oo0oO * ooo0O % ii . I1ii11iIi11i
elif iIi1i == 39 :
 IIIIiI11I11 ( IIo0o0O0O00oOOo )
 if 32 - 32: iiiiiiii1
elif iIi1i == 45 :
 TEXTS ( )
 if 33 - 33: oOOoOooOo + I1ii11iIi11i * iii1i1iiiiIi % oOOoOooOo * OOOo00oo0oO - oOo
elif iIi1i == 46 :
 oo00o0 ( )
 if 40 - 40: i1IiiiI1iI . ii * o0o00Oo0O / O0Oooo0O + o0o00Oo0O
elif iIi1i == 47 :
 GEVID ( )
 if 97 - 97: oOOoOooOo - oOOoOooOo * OoOo0o % iii1i1iiiiIi - iii1i1iiiiIi - O0Oooo0O
elif iIi1i == 48 :
 II1iIiiiI ( O000OOO , IIo0o0O0O00oOOo , oO0O0oO0 )
 if 52 - 52: o0o00Oo0O % iiiiiiii1
elif iIi1i == 49 :
 O0oOOo0Oo ( )
 if 81 - 81: ii % iii1i1iiiiIi % I1ii11iIi11i - oOo0O0Ooo
elif iIi1i == 22222 :
 II11IiI1 ( IIo0o0O0O00oOOo )
 if 43 - 43: ooo0O % ooo0O
elif iIi1i == 222225 :
 iI1IiiiIiI1Ii ( IIo0o0O0O00oOOo )
 if 48 - 48: o0o00Oo0O
elif iIi1i == 222 :
 IIIiIIi1I1I ( IIo0o0O0O00oOOo )
 if 5 - 5: OoOo0o / Ii . i1IiiiI1iI % OoOo0o
elif iIi1i == 2222222 :
 oo0 ( IIo0o0O0O00oOOo )
 if 1 - 1: IIiIiII11i + o0o00Oo0O * iii1i1iiiiIi / I11i1ii1 . o0o00Oo0O
elif iIi1i == 222222 :
 Ii1III11ii1 ( IIo0o0O0O00oOOo , O000OOO )
 if 87 - 87: I11i1ii1 + oOo0O0Ooo
elif iIi1i == 333 :
 oo0ooo0o0OOO ( IIo0o0O0O00oOOo )
 if 74 - 74: oOo + oOo % iiiiiiii1 / i1IiiiI1iI / o0o00Oo0O
 if 54 - 54: ooo0O / ii * oOOoOooOo . iii1i1iiiiIi - O0Oooo0O
elif iIi1i == 1020 :
 Ii1iIiI1iI ( )
 if 69 - 69: OOOo00oo0oO - oOo
elif iIi1i == 1021 :
 ANIMEEP ( )
 if 80 - 80: oOOoOooOo + iI11I1II1I1I . IIiIiII11i + oOo0O0Ooo - OOOo00oo0oO % iii1i1iiiiIi
elif iIi1i == 1022 :
 ANIMEPLAY ( IIo0o0O0O00oOOo )
 if 10 - 10: iI11I1II1I1I
elif iIi1i == 1001 :
 o0Oo000o ( )
 if 44 - 44: iii1i1iiiiIi * OOOo00oo0oO . oOoO0o00OO0 + Ii
elif iIi1i == 1005 :
 OoOOo00O ( )
 if 85 - 85: i1IiiiI1iI
elif iIi1i == 1007 :
 IiIIIi11 ( IIo0o0O0O00oOOo )
 if 36 - 36: oOOoOooOo % oOo
elif iIi1i == 1010 :
 O0O000oOO0 ( IIo0o0O0O00oOOo )
 if 1 - 1: ii - iii1i1iiiiIi
elif iIi1i == 1011 :
 iii11I1I1i1 ( IIo0o0O0O00oOOo )
 if 35 - 35: O0Oooo0O
elif iIi1i == 1012 :
 o0O0 ( IIo0o0O0O00oOOo )
 if 35 - 35: I1ii11iIi11i - iI11I1II1I1I / ooOoO0O00 + oOo - ii / Ii
elif iIi1i == 1030 :
 OOoo ( )
 if 79 - 79: oOo0O0Ooo * oOOoOooOo * oOOoOooOo
elif iIi1i == 1031 :
 oooOoo0oo00OooOO ( IIo0o0O0O00oOOo , OO00OOoO0o )
 if 92 - 92: iiiiiiii1 % oOoO0o00OO0
elif iIi1i == 1032 :
 IiI1i1i1 ( IIo0o0O0O00oOOo )
 if 16 - 16: OOOo00oo0oO
elif iIi1i == 1006 :
 Parse . ParseURL ( IIo0o0O0O00oOOo )
 if 52 - 52: ii % oOOoOooOo - O0Oooo0O * i1IiiiI1iI
elif iIi1i == 2030 :
 Parse . addonParseURL ( IIo0o0O0O00oOOo )
 if 24 - 24: i1iIi + I11i1ii1 + ii / OOOo00oo0oO / oOo0O0Ooo + I11i1ii1
elif iIi1i == 2031 :
 Parse . apkParseURL ( IIo0o0O0O00oOOo )
 if 52 - 52: oOOoOooOo
elif iIi1i == 2032 :
 Parse . ParseBOSS ( IIo0o0O0O00oOOo )
 if 38 - 38: oOo + oOo0O0Ooo % I11i1ii1
elif iIi1i == 1002 :
 o0o0O ( IIo0o0O0O00oOOo )
 if 87 - 87: OOOo00oo0oO * i1iIi - O0Oooo0O / OOOo00oo0oO
elif iIi1i == 1003 :
 ooooooo ( IIo0o0O0O00oOOo , OO00OOoO0o )
 if 65 - 65: iii1i1iiiiIi
elif iIi1i == 1004 :
 ooO0ooO0O ( IIo0o0O0O00oOOo )
 if 87 - 87: i1IiiiI1iI - Ii - OoOo0o . iii1i1iiiiIi + I11i1ii1 . oOo
elif iIi1i == 1008 :
 Ooo0 ( )
 if 70 - 70: iI11I1II1I1I % ii / oOo . o0o00Oo0O - i1IiiiI1iI % IIiIiII11i
elif iIi1i == 1009 :
 IIi1II ( IIo0o0O0O00oOOo )
 if 84 - 84: OoOo0o * ooOoO0O00 . iI11I1II1I1I * iiiiiiii1 + O0Oooo0O + IIiIiII11i
elif iIi1i == 2001 :
 IiiiII1 ( )
 if 97 - 97: i1iIi - I11i1ii1
elif iIi1i == 2002 :
 OOO0O0OO ( IIo0o0O0O00oOOo )
 if 64 - 64: OOOo00oo0oO . oOOoOooOo / oOOoOooOo - IIiIiII11i
elif iIi1i == 1013 :
 Oo0O00O ( )
elif iIi1i == 10111113 :
 i1iI1i11iIi1 ( IIo0o0O0O00oOOo )
 if 81 - 81: oOoO0o00OO0
elif iIi1i == 1014 :
 ii1iiiIIiIII ( )
 if 64 - 64: OOOo00oo0oO * oOo / OoOo0o + i1iIi % I1ii11iIi11i . I11i1ii1
elif iIi1i == 1015 :
 i1i1iiI11I ( IIo0o0O0O00oOOo )
 if 2 - 2: O0Oooo0O + i1IiiiI1iI
elif iIi1i == 1016 :
 IiIiiiiI1 ( IIo0o0O0O00oOOo , OO00OOoO0o , O000OOO )
 if 47 - 47: Ii + iI11I1II1I1I % oOoO0o00OO0 - OOOo00oo0oO % oOo
elif iIi1i == 1017 :
 i1I1IIIiiI ( )
 if 85 - 85: OOOo00oo0oO * iii1i1iiiiIi / iii1i1iiiiIi
elif iIi1i == 1018 :
 OO0O0ooOOO00 ( IIo0o0O0O00oOOo )
 if 85 - 85: OoOo0o / O0Oooo0O . ooOoO0O00 / iii1i1iiiiIi + iI11I1II1I1I
elif iIi1i == 1019 :
 ii1i1i ( IIo0o0O0O00oOOo )
elif iIi1i == 10190 :
 oOO0oo ( IIo0o0O0O00oOOo )
 if 71 - 71: oOo
elif iIi1i == 1023 :
 iIII1I11II1i1 ( )
 if 96 - 96: oOoO0o00OO0 / oOo0O0Ooo - oOoO0o00OO0 / IIiIiII11i - I11i1ii1
elif iIi1i == 1024 :
 I1IiiIII1ii ( IIo0o0O0O00oOOo )
 if 74 - 74: i1iIi * ii % OoOo0o + ii + iiiiiiii1
elif iIi1i == 1025 :
 iiOo00ooO0 ( IIo0o0O0O00oOOo )
 if 83 - 83: ooOoO0O00
elif iIi1i == 4001 :
 Ooo0O ( )
 if 2 - 2: ooOoO0O00 / OoOo0o * o0o00Oo0O
elif iIi1i == 4002 :
 Ooo0oo ( )
 if 99 - 99: ii . iii1i1iiiiIi / IIiIiII11i
elif iIi1i == 4003 :
 I1iIi1IiI1i ( )
 if 64 - 64: iiiiiiii1 / ooOoO0O00 . oOo0O0Ooo + o0o00Oo0O
elif iIi1i == 4004 :
 Oo00OOOOoo0oo ( )
 if 5 - 5: o0o00Oo0O . Ii
elif iIi1i == 4005 :
 ii1I11iIiIII1 ( )
 if 71 - 71: ooo0O + iiiiiiii1 + oOOoOooOo
elif iIi1i == 4006 :
 OOo0iiIii1IIi ( )
 if 27 - 27: ii . iiiiiiii1 * O0Oooo0O % o0o00Oo0O + ii - iiiiiiii1
elif iIi1i == 4007 :
 iI111i1I1II ( )
 if 86 - 86: ooOoO0O00
elif iIi1i == 4008 :
 o0OoO000O ( )
 if 81 - 81: iii1i1iiiiIi
elif iIi1i == 40099 : o0Oo0ooo ( )
elif iIi1i == 4009 : o0o0oO0OOO ( )
elif iIi1i == 4010 : o000OO00OoO00 ( )
elif iIi1i == 3000 :
 i1ii1i ( )
 if 52 - 52: iiiiiiii1 * I11i1ii1 % oOo0O0Ooo * i1IiiiI1iI
elif iIi1i == 3001 :
 o0Ooo0OoO ( )
 if 73 - 73: O0Oooo0O * oOOoOooOo
elif iIi1i == 3002 :
 I1iI1i ( IIo0o0O0O00oOOo )
 if 62 - 62: OoOo0o . oOo0O0Ooo * iI11I1II1I1I + oOo * oOOoOooOo / OOOo00oo0oO
elif iIi1i == 3003 :
 iIIiiI1II ( IIo0o0O0O00oOOo )
 if 14 - 14: iiiiiiii1 / oOo
elif iIi1i == 3004 :
 Oo0o ( IIo0o0O0O00oOOo )
 if 75 - 75: I11i1ii1
elif iIi1i == 404 :
 i1IiOO00O0o0 ( O000OOO , IIo0o0O0O00oOOo , OO00OOoO0o )
 if 68 - 68: I11i1ii1 - ooOoO0O00 % I11i1ii1 . oOo . Ii . ii
elif iIi1i == 405 :
 i11ii ( IIo0o0O0O00oOOo )
 if 32 - 32: iiiiiiii1 + oOo % I11i1ii1 + oOo0O0Ooo
elif iIi1i == 7030 :
 IiIIi1I ( )
 if 69 - 69: O0Oooo0O + i1IiiiI1iI - iI11I1II1I1I - IIiIiII11i . i1iIi
elif iIi1i == 7021 :
 oOOOOOOooO ( O000OOO )
 if 74 - 74: oOoO0o00OO0 % ooo0O + o0o00Oo0O - Ii - I11i1ii1 % OoOo0o
elif iIi1i == 7022 :
 i111I ( O000OOO )
 if 39 - 39: oOo - ooo0O
elif iIi1i == 7000 :
 OO00OOOO00oOO ( O000OOO , IIo0o0O0O00oOOo , img )
 if 71 - 71: iiiiiiii1 . oOo + oOOoOooOo - OoOo0o - I1ii11iIi11i
elif iIi1i == 7050 :
 OOoOOO0 ( IIo0o0O0O00oOOo )
 if 100 - 100: ii - ooo0O + O0Oooo0O . ii % Ii
elif iIi1i == 7051 :
 Ii1II1I ( IIo0o0O0O00oOOo )
 if 64 - 64: O0Oooo0O % ii / ooOoO0O00 / oOo
elif iIi1i == 70511 :
 WATCHLIST2 ( IIo0o0O0O00oOOo )
 if 2 - 2: i1IiiiI1iI % ooo0O . oOo . oOo
elif iIi1i == 7052 :
 oO0Ooo ( IIo0o0O0O00oOOo )
 if 89 - 89: oOOoOooOo - OOOo00oo0oO + IIiIiII11i + oOo - I11i1ii1
elif iIi1i == 7053 :
 iiiiIIiiII1Iii1 ( IIo0o0O0O00oOOo )
 if 27 - 27: O0Oooo0O - ooo0O + oOo
elif iIi1i == 7054 :
 CoolPlay ( IIo0o0O0O00oOOo )
 if 38 - 38: iii1i1iiiiIi + oOo . Ii + i1iIi % ooOoO0O00 % oOo0O0Ooo
elif iIi1i == 7060 :
 oOIIIiIII111iii ( )
 if 93 - 93: Ii
elif iIi1i == 7061 :
 IiiIi11 ( IIo0o0O0O00oOOo )
 if 63 - 63: iI11I1II1I1I - iI11I1II1I1I % ooo0O
elif iIi1i == 7063 :
 oOOiI ( IIo0o0O0O00oOOo )
 if 97 - 97: ooOoO0O00 % i1IiiiI1iI % iii1i1iiiiIi
elif iIi1i == 7062 :
 Ii1i1IiiIiIII ( IIo0o0O0O00oOOo )
 if 25 - 25: iii1i1iiiiIi . iI11I1II1I1I - iiiiiiii1 % IIiIiII11i . iii1i1iiiiIi
elif iIi1i == 7064 :
 NATatozcat ( )
 if 16 - 16: OoOo0o . I1ii11iIi11i . oOo0O0Ooo % o0o00Oo0O . oOoO0o00OO0 + Ii
elif iIi1i == 7067 :
 Oo0O0O000oOO0oOo0OOoOO ( IIo0o0O0O00oOOo )
 if 100 - 100: oOoO0o00OO0 - ooOoO0O00 - oOo * ooo0O + iii1i1iiiiIi
elif iIi1i == 7066 :
 NATatozA ( IIo0o0O0O00oOOo )
 if 31 - 31: ooOoO0O00
elif iIi1i == 7065 :
 o0O00oo0Ooo ( IIo0o0O0O00oOOo )
 if 21 - 21: ooo0O / o0o00Oo0O % o0o00Oo0O . ii / oOo0O0Ooo
elif iIi1i == 7070 :
 I111i1IiI1 ( )
 if 94 - 94: oOOoOooOo + oOo / oOOoOooOo - oOOoOooOo + I1ii11iIi11i + ooo0O
elif iIi1i == 7071 :
 DIZIlist ( IIo0o0O0O00oOOo )
 if 50 - 50: OOOo00oo0oO . I1ii11iIi11i
elif iIi1i == 7072 :
 DIZIpull ( IIo0o0O0O00oOOo )
 if 15 - 15: i1iIi
elif iIi1i == 7073 :
 WATCHDIZI ( IIo0o0O0O00oOOo )
 if 64 - 64: ii
elif iIi1i == 7002 :
 oo0OoooOo0 ( )
 if 25 - 25: I11i1ii1
elif iIi1i == 7003 :
 o0OoO0iiII1 ( IIo0o0O0O00oOOo )
 if 29 - 29: iii1i1iiiiIi % oOOoOooOo * ii
elif iIi1i == 7004 :
 iIII1ii1iI111IIi1 ( IIo0o0O0O00oOOo )
 if 8 - 8: Ii - O0Oooo0O / I11i1ii1
elif iIi1i == 7020 :
 i1i11i1 ( IIo0o0O0O00oOOo )
 if 17 - 17: Ii * oOo . ooo0O . ii . iii1i1iiiiIi - oOoO0o00OO0
elif iIi1i == 7001 :
 OO0o0o0oo0O ( )
 if 78 - 78: oOoO0o00OO0 - ii + o0o00Oo0O
elif iIi1i == 7010 :
 I1Ii1 ( IIo0o0O0O00oOOo )
 if 15 - 15: oOoO0o00OO0 / I11i1ii1 % oOo0O0Ooo
elif iIi1i == 7011 :
 OO00iiI1II1i ( IIo0o0O0O00oOOo )
 if 16 - 16: i1iIi
elif iIi1i == 7012 :
 O0oOooOO ( IIo0o0O0O00oOOo )
 if 26 - 26: ooo0O / i1IiiiI1iI + iii1i1iiiiIi / iii1i1iiiiIi
elif iIi1i == 7013 :
 cnfTVPlay2 ( IIo0o0O0O00oOOo )
elif iIi1i == 7014 :
 CNF_Studio_Indexer . MV_Movies ( IIo0o0O0O00oOOo )
elif iIi1i == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( IIo0o0O0O00oOOo )
elif iIi1i == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( O000OOO , IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iIi1i == 7018 :
 i11ii1i1i ( )
elif iIi1i == 7019 :
 CNF_Studio_Indexer . List_Movies ( IIo0o0O0O00oOOo )
elif iIi1i == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( IIo0o0O0O00oOOo )
elif iIi1i == 7024 :
 CNF_Studio_Indexer . Box_Office ( IIo0o0O0O00oOOo )
 if 31 - 31: O0Oooo0O
elif iIi1i == 8000 :
 ooOo000 ( )
elif iIi1i == 8001 :
 oOI1 ( )
elif iIi1i == 8002 :
 oOoo0OOoOoO0O ( )
elif iIi1i == 8003 :
 IIoo0O ( )
elif iIi1i == 8004 :
 i11Oo00 ( )
elif iIi1i == 8005 :
 oOOooOOO ( )
elif iIi1i == 8006 :
 iII11I11i ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 8030 :
 OOO000ooO0OO ( IIo0o0O0O00oOOo )
elif iIi1i == 8045 :
 OOoi1Iiiiiii ( IIo0o0O0O00oOOo )
elif iIi1i == 8046 :
 Oo000O00o0O ( IIo0o0O0O00oOOo )
elif iIi1i == 8047 :
 IIio0 ( IIo0o0O0O00oOOo )
elif iIi1i == 8048 :
 OOO0o0oo00 ( IIo0o0O0O00oOOo )
elif iIi1i == 8049 :
 o000 ( IIo0o0O0O00oOOo )
elif iIi1i == 804900 :
 IIIi1IiI1iII ( IIo0o0O0O00oOOo )
elif iIi1i == 8020 :
 oOo0o0 ( )
elif iIi1i == 8021 :
 IIiiI11iI ( IIo0o0O0O00oOOo )
elif iIi1i == 8022 :
 IIi1III1II ( IIo0o0O0O00oOOo )
elif iIi1i == 8023 :
 o0o0OOOO ( IIo0o0O0O00oOOo )
elif iIi1i == 8040 :
 OOoiIIiiIIIi1I ( )
elif iIi1i == 8041 :
 OoO0oOoo ( IIo0o0O0O00oOOo )
elif iIi1i == 8042 :
 I1I111i1I1II ( IIo0o0O0O00oOOo )
elif iIi1i == 8043 :
 yt . PlayVideo ( IIo0o0O0O00oOOo )
elif iIi1i == 8044 :
 O00oOoO0o0oO ( IIo0o0O0O00oOOo )
elif iIi1i == 8060 :
 I1iii ( )
elif iIi1i == 8061 :
 IiiiIii ( IIo0o0O0O00oOOo )
elif iIi1i == 8064 :
 IiiI11i1I ( )
elif iIi1i == 8065 :
 IIi1Iii ( IIo0o0O0O00oOOo )
elif iIi1i == 8070 :
 oO00oOOOO ( )
elif iIi1i == 8071 :
 o0o0OOO0ooo00 ( IIo0o0O0O00oOOo )
elif iIi1i == 7080 :
 I11III111i1I ( IIo0o0O0O00oOOo )
elif iIi1i == 8090 :
 i1Ii1Ii ( )
elif iIi1i == 8091 :
 o00OOOo0O0O0o0 ( IIo0o0O0O00oOOo )
elif iIi1i == 8092 :
 i11oO0oOO000 ( IIo0o0O0O00oOOo )
elif iIi1i == 8093 :
 Oo0ooo0oOo0Oo0O ( IIo0o0O0O00oOOo )
elif iIi1i == 8081 :
 I1iII1IiI11i ( )
elif iIi1i == 8062 :
 ooOoo ( IIo0o0O0O00oOOo )
elif iIi1i == 8063 :
 o0oO ( IIo0o0O0O00oOOo )
elif iIi1i == 8050 :
 II1iii1iII ( )
elif iIi1i == 8051 :
 I1ii1111iIi1 ( IIo0o0O0O00oOOo )
elif iIi1i == 8052 :
 o0oIIi111 ( IIo0o0O0O00oOOo )
elif iIi1i == 8085 :
 i1I11Iiii ( )
elif iIi1i == 8086 :
 ooOo0oO ( IIo0o0O0O00oOOo )
elif iIi1i == 8087 :
 iII1iII ( IIo0o0O0O00oOOo )
elif iIi1i == 8088 :
 iiii11i1ii1 ( IIo0o0O0O00oOOo , O000OOO )
elif iIi1i == 9000 :
 oOOo00O ( )
elif iIi1i == 1111 :
 I1iI1iiI1Ii1 ( )
elif iIi1i == 9001 :
 O00OOooo0Ooo ( )
elif iIi1i == 9002 :
 oOO0OOOOoooO ( )
elif iIi1i == 9003 :
 o0Ooo0Oooo0o ( )
elif iIi1i == 9004 :
 World1 ( )
elif iIi1i == 9005 :
 World2 ( IIo0o0O0O00oOOo )
elif iIi1i == 9006 :
 World3 ( IIo0o0O0O00oOOo )
elif iIi1i == 9007 :
 oO00ooOoOoOO ( )
elif iIi1i == 9008 :
 o0O0Oo0 ( IIo0o0O0O00oOOo )
elif iIi1i == 9009 :
 iI1111i ( IIo0o0O0O00oOOo )
elif iIi1i == 9010 :
 OoOO0OOOO0 ( )
elif iIi1i == 9011 :
 OooOOo0ooO ( IIo0o0O0O00oOOo )
elif iIi1i == 50 :
 OoOo0Oooo0o ( IIo0o0O0O00oOOo )
elif iIi1i == 9020 :
 champlist ( )
elif iIi1i == 9021 :
 O000Oo ( )
elif iIi1i == 9022 :
 IiiIi1II ( )
elif iIi1i == 9023 :
 IiII1IiiI ( )
elif iIi1i == 9024 :
 i11I ( IIo0o0O0O00oOOo )
elif iIi1i == 9030 :
 OOoo00o0 ( IIo0o0O0O00oOOo )
elif iIi1i == 9031 :
 o0OO0 ( IIo0o0O0O00oOOo )
elif iIi1i == 9032 :
 iI1II1i1ii ( IIo0o0O0O00oOOo )
elif iIi1i == 9033 :
 OOooOOooo000OoO ( IIo0o0O0O00oOOo )
elif iIi1i == 9034 :
 oOO0OO0O ( )
elif iIi1i == 7084 :
 OoI1iIi ( )
elif iIi1i == 7085 :
 Iii11 ( IIo0o0O0O00oOOo )
elif iIi1i == 7086 :
 IIiIiOOoO ( IIo0o0O0O00oOOo , OO00OOoO0o , oO0O0oO0 )
elif iIi1i == 7087 :
 o0OoooO0oo0 ( oO0O0oO0 )
elif iIi1i == 9666 :
 o0O0oo0OO0O ( IIo0o0O0O00oOOo )
elif iIi1i == 10100 : o0IiIiI111IIII1 ( )
elif iIi1i == 101001 : I1i1i1iiIi1 ( IIo0o0O0O00oOOo )
elif iIi1i == 10105 : I1iii1IIi1I ( IIo0o0O0O00oOOo )
elif iIi1i == 10106 : oO00O00OOOo ( IIo0o0O0O00oOOo )
elif iIi1i == 10104 : o0O000Ooo ( IIo0o0O0O00oOOo )
elif iIi1i == 10107 : OoOoo0ooO0000 ( )
elif iIi1i == 10103 : Oo0o0oO00 ( IIo0o0O0O00oOOo )
elif iIi1i == 10108 : i1iiIiiIi ( IIo0o0O0O00oOOo )
elif iIi1i == 10000 : Origin_Menu ( )
elif iIi1i == 10001 : o00OoooooooOo ( )
elif iIi1i == 10002 : IIiiii ( )
elif iIi1i == 10003 : IiIIiIii1ii ( )
elif iIi1i == 10004 : iii1IiI ( IIo0o0O0O00oOOo )
elif iIi1i == 10005 : o0OOO00O ( )
elif iIi1i == 10006 : Oo0o00o0oOoo0 ( IIo0o0O0O00oOOo )
elif iIi1i == 10007 : OOo0iIiiI11II11 ( IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 10008 : iIo0O00o00o0 ( )
elif iIi1i == 10009 : oo00oO0o000 ( )
elif iIi1i == 10010 : I1i1I1i1I1 ( IIo0o0O0O00oOOo )
elif iIi1i == 10011 : OOO00i111 ( IIo0o0O0O00oOOo )
elif iIi1i == 10012 : oo0 ( IIo0o0O0O00oOOo )
elif iIi1i == 10113 : GRABG ( IIo0o0O0O00oOOo , O000OOO )
elif iIi1i == 10109 : oOiIi1i1111I ( IIo0o0O0O00oOOo )
elif iIi1i == 10013 : iIIiiiI1 ( IIo0o0O0O00oOOo )
elif iIi1i == 10014 : iIIi1Iii ( )
elif iIi1i == 10015 : I11iI ( )
elif iIi1i == 10016 : i11i11 ( IIo0o0O0O00oOOo )
elif iIi1i == 10017 : IIIiIII1 ( )
elif iIi1i == 10018 : IIIiII1iIII ( )
elif iIi1i == 10019 : o00OoOoo0 ( )
elif iIi1i == 10020 : iI111iiI1II ( )
elif iIi1i == 10021 : IIiIiOoOOo ( )
elif iIi1i == 10022 : o0OO0oO0oOOOoo ( IIo0o0O0O00oOOo )
elif iIi1i == 10023 : O0o0O0O ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 10024 : III1Ii ( IIo0o0O0O00oOOo )
elif iIi1i == 10025 : ooOo0O ( )
elif iIi1i == 10026 : iiIII ( )
elif iIi1i == 10027 : I11Iii11i1Ii ( )
elif iIi1i == 10028 : iIiii1Ii ( )
elif iIi1i == 10029 : OoOooO0oO ( )
elif iIi1i == 423 : Oooo0O00Ooo ( IIo0o0O0O00oOOo )
elif iIi1i == 426 : I1i1i1Iii1 ( IIo0o0O0O00oOOo )
elif iIi1i == 10030 : Izle_Films ( )
elif iIi1i == 10031 : Latest_Izle_Movies ( )
elif iIi1i == 10032 : Izle_Genres ( )
elif iIi1i == 10033 : Izle_Pop_Movies ( )
elif iIi1i == 10034 : Izle_Boxsets ( )
elif iIi1i == 10035 : Izle_Search ( )
elif iIi1i == 10036 : Izle_Genres_Movie ( IIo0o0O0O00oOOo )
elif iIi1i == 10037 : Izle_Boxset_single ( IIo0o0O0O00oOOo )
elif iIi1i == 10038 : Izle_IFRAME ( )
elif iIi1i == 10039 : Izle_Boxsets_Next ( IIo0o0O0O00oOOo )
elif iIi1i == 10040 : OOOo00OOooO ( )
elif iIi1i == 10041 : OooO00ooo0o0 ( IIo0o0O0O00oOOo )
elif iIi1i == 10042 : O0oO0O0ooo00o0 ( IIo0o0O0O00oOOo )
elif iIi1i == 10043 : ooO0000 ( )
elif iIi1i == 10044 : I1II11IIii ( IIo0o0O0O00oOOo )
elif iIi1i == 10045 : I11i1IiI1 ( O000OOO )
elif iIi1i == 10046 : Ii1I ( IIo0o0O0O00oOOo )
elif iIi1i == 10047 : O0o0ooo00o00 ( IIo0o0O0O00oOOo )
elif iIi1i == 10048 : IiI1Iii1iIIII ( IIo0o0O0O00oOOo )
elif iIi1i == 10049 : OOoO00o00oo ( IIo0o0O0O00oOOo )
elif iIi1i == 10050 : I1i1iI1II ( )
elif iIi1i == 10051 : OooO0oo ( )
elif iIi1i == 10052 : OooO0o00oO ( )
elif iIi1i == 10053 : Addon ( IIo0o0O0O00oOOo )
elif iIi1i == 10054 : O0OOoo ( IIo0o0O0O00oOOo , O000OOO )
elif iIi1i == 10055 :
 Ooo00OoO ( "addFavorite" )
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 O00Ooo00 ( O000OOO , IIo0o0O0O00oOOo , OO00OOoO0o , I1I1 , o0OOo0o00 )
elif iIi1i == 10056 :
 Ooo00OoO ( "rmFavorite" )
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOOooooOo0 ( O000OOO )
elif iIi1i == 10057 :
 Ooo00OoO ( "getFavorites" )
 oO00Oo0OO ( )
elif iIi1i == 10058 : O00OOOo ( )
elif iIi1i == 10059 : Donators_Guide ( )
elif iIi1i == 10060 : o0oo0000OO ( )
elif iIi1i == 10061 : OoOOoOo ( )
elif iIi1i == 10062 : iIIIIi11i ( O000OOO , IIo0o0O0O00oOOo , oO0O0oO0 )
elif iIi1i == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + I11iii1Ii + ")" )
elif iIi1i == 10064 : IIIIIiiI11i1 ( )
elif iIi1i == 10065 : IiIii11i1IIiI ( IIo0o0O0O00oOOo )
elif iIi1i == 10066 : IiII1i ( IIo0o0O0O00oOOo )
elif iIi1i == 10068 : II11 ( IIo0o0O0O00oOOo )
elif iIi1i == 10069 : OOo0OOOoOOo ( IIo0o0O0O00oOOo )
elif iIi1i == 10070 : o00oOoo0o00 ( IIo0o0O0O00oOOo )
elif iIi1i == 10071 : Genie_Watch ( )
elif iIi1i == 10072 : Ooo0oOOoo0O ( )
elif iIi1i == 10073 : iI11IiIiiII1 ( IIo0o0O0O00oOOo )
elif iIi1i == 10074 : oO0I1I1i1I1I1I1 ( IIo0o0O0O00oOOo )
elif iIi1i == 10075 : i1I1i1i1I1 ( OO00OOoO0o , O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 10076 : O0OOOOOO0ooO ( IIo0o0O0O00oOOo )
elif iIi1i == 10077 : IiI11I1Ii11II ( IIo0o0O0O00oOOo )
elif iIi1i == 10078 : OoO0o0oOOO ( )
elif iIi1i == 10079 : Genie_Watch_Tv_Shows ( )
elif iIi1i == 10080 : Genie_Watch_Tv_Genre ( IIo0o0O0O00oOOo )
elif iIi1i == 10081 : Genie_Watch_TV_PlayRun ( IIo0o0O0O00oOOo )
elif iIi1i == 10082 : Genie_Watch_TV_Episodes ( IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 10083 : Genie_Watch_Tv_Recent ( IIo0o0O0O00oOOo )
elif iIi1i == 10084 : I11IoOoO ( )
elif iIi1i == 10085 : Iii1I1I11iiI1 ( )
elif iIi1i == 10086 : o0OOOO00O0Oo ( )
elif iIi1i == 20000 : iIIIII ( )
elif iIi1i == 20001 : I11Ii1 ( IIo0o0O0O00oOOo )
elif iIi1i == 20002 : II1iII11 ( IIo0o0O0O00oOOo )
elif iIi1i == 20003 : i1iIIi ( IIo0o0O0O00oOOo )
elif iIi1i == 20004 : II1Iiiii ( IIo0o0O0O00oOOo )
elif iIi1i == 20005 : iI1Iii1i11 ( IIo0o0O0O00oOOo )
elif iIi1i == 21004 : Iii1IiIiIii ( )
elif iIi1i == 21005 : OOo0ooOOOo0O0 ( IIo0o0O0O00oOOo )
elif iIi1i == 21006 : ooI1 ( IIo0o0O0O00oOOo )
elif iIi1i == 21007 : IiI1i1iI ( IIo0o0O0O00oOOo )
elif iIi1i == 21008 : O00OO ( IIo0o0O0O00oOOo )
elif iIi1i == 21009 : ooOOO0OOOo ( IIo0o0O0O00oOOo )
elif iIi1i == 30000 : o0O0OOooO ( )
elif iIi1i == 30001 : oOOOoOO ( )
elif iIi1i == 100121 : Resolve ( IIo0o0O0O00oOOo )
elif iIi1i == 30003 : I1iIiIi111I ( )
elif iIi1i == 30004 : iiooo ( IIo0o0O0O00oOOo )
elif iIi1i == 30005 : O0OoO0OOo ( IIo0o0O0O00oOOo )
elif iIi1i == 30006 : oOoOo000Ooooo ( )
elif iIi1i == 30007 : oOo0OO0 ( )
elif iIi1i == 30008 : Ooii1II11IIII ( IIo0o0O0O00oOOo )
elif iIi1i == 30009 : OoOo00oOoo0oO ( IIo0o0O0O00oOOo )
elif iIi1i == 30010 : ooo0000oo0 ( IIo0o0O0O00oOOo )
elif iIi1i == 30011 : O0OoO0 ( )
elif iIi1i == 30012 : ooo0ooOoOOoO ( )
elif iIi1i == 30013 : II11II1i ( )
elif iIi1i == 30014 : II1iOo0ooo0 ( )
elif iIi1i == 30015 : IIIiii ( IIo0o0O0O00oOOo , OO00OOoO0o , I1I1 )
elif iIi1i == 30016 : iIII1II ( IIo0o0O0O00oOOo )
elif iIi1i == 30019 : o0OOoo ( IIo0o0O0O00oOOo )
elif iIi1i == 30017 : iiII1iIi1ii1i ( IIo0o0O0O00oOOo )
elif iIi1i == 30018 : OoO0O00 ( IIo0o0O0O00oOOo )
elif iIi1i == 30030 : OOoO000oO ( )
elif iIi1i == 30031 : II111111 ( )
elif iIi1i == 30032 : O00OOII1Ii1iI1i1 ( )
elif iIi1i == 30033 : OOOoOooO000oO ( )
elif iIi1i == 30034 : iIiIi ( )
elif iIi1i == 30035 : ooooooo0oOo0 ( IIo0o0O0O00oOOo )
elif iIi1i == 30036 : OooO00oO00o ( IIo0o0O0O00oOOo )
elif iIi1i == 30037 : IIII1iI1IiIiI ( IIo0o0O0O00oOOo )
elif iIi1i == 30038 : IIi1 ( )
elif iIi1i == 30039 : oOooO ( )
elif iIi1i == 50000 : o0Oooo ( )
elif iIi1i == 50001 : O00o0 ( )
elif iIi1i == 50002 : iIIiiiIiiii11 ( IIo0o0O0O00oOOo )
elif iIi1i == 50003 : Table_Menu ( oO0O0oO0 )
elif iIi1i == 60000 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
elif iIi1i == 60001 : iIii1iIiII1i1 ( )
elif iIi1i == 60002 : oOOoO0oO00O ( O000OOO )
elif iIi1i == 60003 : iIii11II1IIiI ( IIo0o0O0O00oOOo )
elif iIi1i == 600033 : IiI11II ( IIo0o0O0O00oOOo )
elif iIi1i == 60004 : I11iIi1i1I1i1 ( IIo0o0O0O00oOOo )
elif iIi1i == 50004 : Ii1IIiiIIi ( )
elif iIi1i == 50005 : speedtest . runtest ( IIo0o0O0O00oOOo )
elif iIi1i == 70001 : IiiIiiiiI1III ( )
elif iIi1i == 70002 : iii1 ( IIo0o0O0O00oOOo )
elif iIi1i == 70003 : iII1iii ( IIo0o0O0O00oOOo )
elif iIi1i == 70004 : o0O0o ( IIo0o0O0O00oOOo )
elif iIi1i == 70005 : OO0o0o ( IIo0o0O0O00oOOo )
elif iIi1i == 70006 : O0O0O00OoO0O ( )
elif iIi1i == 50006 : O0O0OOOOoo ( oo00 , Oo0oO0ooo )
elif iIi1i == 80000 : iIIoooO0 ( )
elif iIi1i == 80001 : resolvefilmon ( IIo0o0O0O00oOOo )
elif iIi1i == 80002 : ooooo0oo0OO ( )
elif iIi1i == 80003 : OoOoOoo0oOOooo0o ( O000OOO , IIo0o0O0O00oOOo , "None" )
elif iIi1i == 80004 : i1II1 ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 80005 : iiI1i11II ( )
elif iIi1i == 80006 : IIi111 ( IIo0o0O0O00oOOo )
elif iIi1i == 80007 : oO0o0o0O ( IIo0o0O0O00oOOo )
elif iIi1i == 80008 : I111ii1iI ( )
elif iIi1i == 80009 : ooOOOOoO00 ( )
elif iIi1i == 80010 : ooO0OOO ( IIo0o0O0O00oOOo )
elif iIi1i == 80011 : Oo0oO ( IIo0o0O0O00oOOo )
elif iIi1i == 80012 : ooO0o0Oo ( )
elif iIi1i == 90000 : OOo00oO000o0O ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 90001 : tools ( )
elif iIi1i == 90002 : OOO0ooo ( )
elif iIi1i == 90003 : I1Ioo000oooooooO ( IIo0o0O0O00oOOo )
elif iIi1i == 90004 : II1IIi1ii111 ( IIo0o0O0O00oOOo )
elif iIi1i == 90005 : II1 ( IIo0o0O0O00oOOo )
elif iIi1i == 90006 : O0oooOOoOOO ( IIo0o0O0O00oOOo )
elif iIi1i == 90007 : OoO0 ( IIo0o0O0O00oOOo )
elif iIi1i == 90008 : i1i1Ii1iiII1I ( IIo0o0O0O00oOOo )
elif iIi1i == 90009 : i11I1iiI1iI ( IIo0o0O0O00oOOo )
elif iIi1i == 90010 : II1Iiiiii ( )
elif iIi1i == 90020 : i1o00Oo ( )
elif iIi1i == 90021 : hellyeah2 ( IIo0o0O0O00oOOo )
elif iIi1i == 90022 : hellyeah3 ( IIo0o0O0O00oOOo )
elif iIi1i == 90023 : o0OO0OOO0O ( )
elif iIi1i == 90024 : iIOOO ( IIo0o0O0O00oOOo )
elif iIi1i == 90025 : OO00o0oOO ( IIo0o0O0O00oOOo )
if 84 - 84: Ii * OoOo0o . iiiiiiii1 - i1iIi * ooOoO0O00 - oOoO0o00OO0
elif iIi1i == 90026 : ooooooO0O ( )
elif iIi1i == 90027 : oo000oO ( O000OOO , IIo0o0O0O00oOOo , oO0O0oO0 )
elif iIi1i == 90028 : iiIIiII1IiiIIIIii ( IIo0o0O0O00oOOo )
if 1 - 1: IIiIiII11i
elif iIi1i == 900300 : ooo0OOO ( )
elif iIi1i == 900301 : ooOoOO0OoO00o ( IIo0o0O0O00oOOo )
elif iIi1i == 900302 : oO0oo ( IIo0o0O0O00oOOo )
elif iIi1i == 90030 : IIIIIo0ooOoO000oO ( )
elif iIi1i == 90031 : Treplays ( )
elif iIi1i == 90032 : Treplays2 ( IIo0o0O0O00oOOo )
elif iIi1i == 90033 : Treplays3 ( IIo0o0O0O00oOOo )
elif iIi1i == 90034 : Treplays4 ( IIo0o0O0O00oOOo )
elif iIi1i == 90035 : II1i ( IIo0o0O0O00oOOo )
elif iIi1i == 90036 : I111I1IiI1i1 ( IIo0o0O0O00oOOo )
elif iIi1i == 90039 : o0oo ( IIo0o0O0O00oOOo )
elif iIi1i == 90037 : Oo0oOo000OoO0 ( IIo0o0O0O00oOOo )
elif iIi1i == 900377 : OooooOo0 ( IIo0o0O0O00oOOo )
elif iIi1i == 90038 : IiIIiiI ( )
if 94 - 94: oOoO0o00OO0 * iiiiiiii1 % iiiiiiii1 % i1IiiiI1iI - iiiiiiii1
elif iIi1i == 10090 : ii1i ( )
elif iIi1i == 10091 : Ii1iIiIiIi ( IIo0o0O0O00oOOo )
elif iIi1i == 10092 : oOo0OO00O0O ( IIo0o0O0O00oOOo )
elif iIi1i == 10093 : o0oI1 ( IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 10094 : OOoooO0 ( IIo0o0O0O00oOOo , OO00OOoO0o )
if 38 - 38: I11i1ii1 - oOo % i1iIi - IIiIiII11i
elif iIi1i == 10095 : IIioo0OO ( )
elif iIi1i == 10096 : i1Iiii ( IIo0o0O0O00oOOo )
elif iIi1i == 10097 : iiIIII11iiii ( IIo0o0O0O00oOOo )
elif iIi1i == 10098 : I1111ii11IIII ( IIo0o0O0O00oOOo )
elif iIi1i == 10099 : OO0oo00oOO ( IIo0o0O0O00oOOo )
if 97 - 97: o0o00Oo0O . i1iIi
elif iIi1i == 10200 : o0oOOoOOO ( )
elif iIi1i == 10201 : o00oo0OO0 ( O000OOO , IIo0o0O0O00oOOo , oO0O0oO0 )
elif iIi1i == 10202 : iI11 ( IIo0o0O0O00oOOo )
elif iIi1i == 10203 : RT4 ( IIo0o0O0O00oOOo )
if 52 - 52: I11i1ii1
elif iIi1i == 90040 : OOoo0O0OOOo0 ( )
elif iIi1i == 90041 : O0O0 ( IIo0o0O0O00oOOo )
elif iIi1i == 90042 : o00o0o000Oo ( IIo0o0O0O00oOOo )
elif iIi1i == 90043 : oOIIII ( IIo0o0O0O00oOOo )
elif iIi1i == 90044 : Oo00oOO00 ( IIo0o0O0O00oOOo )
elif iIi1i == 90045 : I1i1I1Iiiii1 ( )
elif iIi1i == 90046 : Iio0000O00oO0O ( IIo0o0O0O00oOOo )
elif iIi1i == 90050 : i1i1I11i1I ( )
elif iIi1i == 90051 : ooOooO ( IIo0o0O0O00oOOo )
elif iIi1i == 90052 : iiIIIi1i ( IIo0o0O0O00oOOo )
elif iIi1i == 90053 : oOO00OO0o0O ( IIo0o0O0O00oOOo )
elif iIi1i == 90054 : ii111iI1i1 ( IIo0o0O0O00oOOo )
elif iIi1i == 90055 : III1II111II11 ( )
if 86 - 86: O0Oooo0O / o0o00Oo0O + ii % OOOo00oo0oO
elif iIi1i == 100001 : Stand_up ( )
if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . i1IiiiI1iI . i1iIi
elif iIi1i == 100003 : i11i11 ( IIo0o0O0O00oOOo )
elif iIi1i == 100004 : OOo00 ( IIo0o0O0O00oOOo )
elif iIi1i == 100005 : Resolve ( IIo0o0O0O00oOOo )
elif iIi1i == 100008 : Search ( )
elif iIi1i == 100007 : ii1ii ( IIo0o0O0O00oOOo )
elif iIi1i == 100009 : yt . PlayVideo ( IIo0o0O0O00oOOo )
elif iIi1i == 100010 : oo0oOO ( IIo0o0O0O00oOOo )
elif iIi1i == 100100 : ooOO0o ( OO00OOoO0o , IIo0o0O0O00oOOo , IIi11i )
elif iIi1i == 100101 : OooO0ooo0 ( IIo0o0O0O00oOOo , O000OOO , I1I1 , IIi11i , OO00OOoO0o )
elif iIi1i == 100102 : III1Ii1i1I1 ( O000OOO , IIo0o0O0O00oOOo , OO00OOoO0o , I1I1 )
elif iIi1i == 100106 : o00oooOo ( IIo0o0O0O00oOOo , O000OOO )
elif iIi1i == 100107 : oOoOo ( )
elif iIi1i == 100108 : oOoo0O0o ( )
elif iIi1i == 100109 : iIII1II11I1 ( IIo0o0O0O00oOOo )
elif iIi1i == 40000 : i1io0o00O ( )
elif iIi1i == 40001 : I11IIIIiI1 ( IIo0o0O0O00oOOo )
elif iIi1i == 100110 : iIIiI1111 ( IIo0o0O0O00oOOo )
elif iIi1i == 100111 : O0OOO00OOO00o ( IIo0o0O0O00oOOo )
elif iIi1i == 100112 : OoOoOoo0OoO0 ( IIo0o0O0O00oOOo )
elif iIi1i == 100113 : o00OOo0o0O ( IIo0o0O0O00oOOo )
elif iIi1i == 100114 : OooOO ( IIo0o0O0O00oOOo )
elif iIi1i == 100115 : OoO00OOoOOOo0 ( IIo0o0O0O00oOOo )
elif iIi1i == 100117 : O0o ( IIo0o0O0O00oOOo )
elif iIi1i == 100118 : Oo0oOO0O00 ( IIo0o0O0O00oOOo )
elif iIi1i == 100120 : oOoO00O ( IIo0o0O0O00oOOo )
elif iIi1i == 1001200 : I11I1I1i1i ( IIo0o0O0O00oOOo )
elif iIi1i == 100210 : oOoo0OooOOo00 ( IIo0o0O0O00oOOo )
elif iIi1i == 100211 : OooOo ( )
elif iIi1i == 100212 : I11iIiI1 ( )
elif iIi1i == 100213 : OoOo00O0o ( )
elif iIi1i == 100214 : Oo00OOoO0oo ( )
elif iIi1i == 1000111 :
 OOO00OO0Ooo ( IIo0o0O0O00oOOo )
 if 81 - 81: IIiIiII11i + iii1i1iiiiIi % Ii / iiiiiiii1 . O0Oooo0O + IIiIiII11i
elif iIi1i == 1001111 :
 O0oo ( O000OOO , IIo0o0O0O00oOOo )
 if 48 - 48: oOo0O0Ooo . oOoO0o00OO0 * iii1i1iiiiIi % ooOoO0O00 / O0Oooo0O * IIiIiII11i
elif iIi1i == 1002111 :
 OO000IIi ( )
 if 62 - 62: ooo0O * O0Oooo0O . iI11I1II1I1I / ooOoO0O00
elif iIi1i == 1003111 :
 oOOOoO00OOooOOOoO ( IIo0o0O0O00oOOo , O000OOO )
 if 75 - 75: ii / oOOoOooOo - iiiiiiii1 . ii . iii1i1iiiiIi % ooOoO0O00
elif iIi1i == 1004111 :
 Ii11I111 ( )
 if 7 - 7: iii1i1iiiiIi . ooOoO0O00 * Ii % Ii
elif iIi1i == 1005111 :
 OoOoOOoOo ( IIo0o0O0O00oOOo , O000OOO )
elif iIi1i == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( IIo0o0O0O00oOOo , I1I1 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( O000OOO , IIo0o0O0O00oOOo , I1I1 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( O000OOO , IIo0o0O0O00oOOo , I1I1 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1105000 :
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( O000OOO , IIo0o0O0O00oOOo , OO00OOoO0o , I1I1 , o0OOo0o00 )
elif iIi1i == 1106000 :
 try :
  O000OOO = O000OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O000OOO = O000OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( O000OOO )
elif iIi1i == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( IIo0o0O0O00oOOo )
elif iIi1i == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( O000OOO )
elif iIi1i == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif iIi1i == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( IIo0o0O0O00oOOo )
elif iIi1i == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in IIo0o0O0O00oOOo :
  import urlresolver
  OOOoO000 = urlresolver . resolve ( IIo0o0O0O00oOOo )
  iIIi = xbmcgui . ListItem ( path = OOOoO000 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIi )
 elif not IIo0o0O0O00oOOo . startswith ( "plugin://plugin" ) or not any ( x in IIo0o0O0O00oOOo for x in pyramid . g_ignoreSetResolved ) :
  iIIi = xbmcgui . ListItem ( path = IIo0o0O0O00oOOo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIi )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + IIo0o0O0O00oOOo + ')' )
elif iIi1i == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( O000OOO , playlist )
elif iIi1i == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( IIo0o0O0O00oOOo , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1117000 :
 IIo0o0O0O00oOOo , oOooOiI = getRegexParsed ( regexs , IIo0o0O0O00oOOo )
 if IIo0o0O0O00oOOo :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( IIo0o0O0O00oOOo , O000OOO , OO00OOoO0o , oOooOiI )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif iIi1i == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 o0OOOOooo = youtubedl . single_YD ( IIo0o0O0O00oOOo )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( o0OOOOooo , O000OOO , OO00OOoO0o )
elif iIi1i == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( IIo0o0O0O00oOOo ) , O000OOO , OO00OOoO0o , True )
elif iIi1i == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , O000OOO , 'video' )
elif iIi1i == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( IIo0o0O0O00oOOo , O000OOO , 'video' )
elif iIi1i == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( IIo0o0O0O00oOOo , O000OOO , 'audio' )
elif iIi1i == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1126000 :
 O000OOO = O000OOO . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( IIo0o0O0O00oOOo , search_term = O000OOO [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( IIo0o0O0O00oOOo )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif iIi1i == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif iIi1i == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif iIi1i == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( O000OOO , IIo0o0O0O00oOOo , OO00OOoO0o , I1I1 )
elif iIi1i == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( IIo0o0O0O00oOOo , OO00OOoO0o , I1I1 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( O000OOO , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( IIo0o0O0O00oOOo )
elif iIi1i == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iIi1i == 9050000 : i1III ( )
elif iIi1i == 9060000 : O0oo ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 9080000 : oOoO0o ( )
elif iIi1i == 9070000 : O000O ( )
elif iIi1i == 9090000 : iIiI1i ( )
elif iIi1i == 9100000 : iIiIi1ii ( )
elif iIi1i == 9110000 : ooo0oo ( )
elif iIi1i == 9110001 : i1ii11 ( IIo0o0O0O00oOOo )
elif iIi1i == 9110002 : OO0ooo0o0 ( IIo0o0O0O00oOOo , O000OOO , OO00OOoO0o )
elif iIi1i == 9110003 : I1Iii1iI1 ( O000OOO , IIi11i )
elif iIi1i == 9110005 : O0OOO00 ( oO0O0oO0 , IIo0o0O0O00oOOo )
elif iIi1i == 9110004 : IIiiiiIiIIii ( )
elif iIi1i == 9110010 : IiII1II1 ( IIo0o0O0O00oOOo )
elif iIi1i == 9110011 : iIiiI1iIiI1I ( )
elif iIi1i == 9110012 : I1i1 ( IIo0o0O0O00oOOo , O000OOO )
elif iIi1i == 9110013 : Ooooo0OoO0 ( IIo0o0O0O00oOOo )
elif iIi1i == 9110014 : iiII ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 9110015 : i111i11I1ii ( )
elif iIi1i == 9999999 : oooOOO0ooOoOOO ( )
elif iIi1i == 19999999 : O0oO0oo0O ( )
elif iIi1i == 1999990 : O0OOo ( )
elif iIi1i == 21999990 : o0O0OOOOoOO0 ( )
elif iIi1i == 21999991 : iiO0oOo00o ( IIo0o0O0O00oOOo )
elif iIi1i == 21999992 : o0ooooO0o0O ( IIo0o0O0O00oOOo )
elif iIi1i == 21999993 : iiIi11iI1iii ( IIo0o0O0O00oOOo )
elif iIi1i == 21999994 : oo000o0000oO ( IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 21999995 : iI1i111I1Ii ( IIo0o0O0O00oOOo )
elif iIi1i == 21999996 : o0OO0o0o00o ( IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 21999997 : OOOoOO ( IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 21999998 : I11IIIi ( O000OOO , IIo0o0O0O00oOOo , OO00OOoO0o )
elif iIi1i == 219999989 : OOI1iI1ii1II ( )
elif iIi1i == 219999990 : O0O0Oo00 ( all = True )
elif iIi1i == 219999991 : IIIiIii111IIi ( )
elif iIi1i == 219999992 : oOoOo00oo ( )
elif iIi1i == 300000000 : IiI ( )
elif iIi1i == 300000001 : o00Oo0oooooo ( IIo0o0O0O00oOOo )
elif iIi1i == 300000002 : OO0O0 ( IIo0o0O0O00oOOo )
elif iIi1i == 300000003 : OO0OoOO0o0o ( O000OOO , IIo0o0O0O00oOOo )
elif iIi1i == 300000004 : I11I ( IIo0o0O0O00oOOo )
elif iIi1i == 300000005 : o0o ( IIo0o0O0O00oOOo )
if 2 - 2: iI11I1II1I1I + O0Oooo0O * iii1i1iiiiIi + i1iIi
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
