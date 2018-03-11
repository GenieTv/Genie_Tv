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
I1IiI = "3.6.8"
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
  OoOoO ( 'Change Log 11/03/2018 - v3.6.6' , '[COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
  os . makedirs ( ooooooO0oo )
def Ii1I1i ( ) :
 OoOoO ( 'Change Log 11/03/2018 - v3.6.6' , '[COLORsteelblue]Pandoras Box Returns,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
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
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , I1IIIii + 'tommys.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'Streams' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( O00OOOoOoo0O ) , 4002 , I1IIIii + 'Streams.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , I1IIIii + 'tools.png' , Oo00OOOOO , '' )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , I1IIIii + 'settings.png' , Oo00OOOOO , '' )
  if oOOo0O00o ( ) == 'android' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , str ( O00OOOoOoo0O ) , 30039 , I1IIIii + 'APKpng' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'Maintainance' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( O00OOOoOoo0O ) , 3 , I1IIIii + 'Maintenance.png' , Oo00OOOOO , '' )
   if 8 - 8: oOo
   if 49 - 49: oOo0O0Ooo - i1IiiiI1iI
   if 74 - 74: iI11I1II1I1I * oOoO0o00OO0 + iii1i1iiiiIi / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
   if 62 - 62: ii * oOo0O0Ooo
   if 58 - 58: iii1i1iiiiIi % ooo0O
   if 50 - 50: O0Oooo0O . ooo0O
   if 97 - 97: o0o00Oo0O + iii1i1iiiiIi
   if 89 - 89: ooo0O + oOo * i1IiiiI1iI * i1iIi
   if 37 - 37: ii - o0o00Oo0O - ooo0O
   if 77 - 77: OoOo0o * iI11I1II1I1I
   if 98 - 98: oOo0O0Ooo % i1iIi * ii
   if 51 - 51: iI11I1II1I1I . iii1i1iiiiIi / OOOo00oo0oO + ooo0O
   if 33 - 33: oOOoOooOo . IIiIiII11i % iiiiiiii1 + ooo0O
   if 71 - 71: I1ii11iIi11i % OoOo0o
 O00oO000O0O ( 'movies' , 'MAIN' )
def IIi1I1iiiii ( ) :
 if 18 - 18: iiiiiiii1 - OoOo0o . O0Oooo0O . iI11I1II1I1I
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 40099 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , I1IIIii + 'tommys.png' , Oo00OOOOO , '' )
 if O0oo0OO0 . getSetting ( 'Streams' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( O00OOOoOoo0O ) , 4002 , I1IIIii + 'Streams.png' , Oo00OOOOO , '' )
 if O0oo0OO0 . getSetting ( 'Maintainance' ) == 'true' :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( O00OOOoOoo0O ) , 3 , I1IIIii + 'Maintenance.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , I1IIIii + 'png' , Oo00OOOOO , '' )
 if 2 - 2: OoOo0o . oOo
 if 78 - 78: i1IiiiI1iI * iI11I1II1I1I . oOo0O0Ooo / ooo0O - ii / O0Oooo0O
 if 35 - 35: i1IiiiI1iI % OoOo0o - OOOo00oo0oO
 if 20 - 20: ooOoO0O00 - oOOoOooOo
 if 30 - 30: i1IiiiI1iI / oOo0O0Ooo
 if 35 - 35: IIiIiII11i % OoOo0o . oOOoOooOo + oOOoOooOo % IIiIiII11i % IIiIiII11i
 if 72 - 72: IIiIiII11i + ooOoO0O00 + ooo0O
 if 94 - 94: OOOo00oo0oO . ooOoO0O00 - ooo0O % o0o00Oo0O - oOo
 if 72 - 72: i1iIi
 if 1 - 1: oOo * I11i1ii1 * ii + oOOoOooOo
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 33 - 33: o0o00Oo0O * ooo0O - O0Oooo0O % O0Oooo0O
def I11I ( ) :
 oOOo0 = i11111IIIII ( 'https://github.com/fluxustv/IPTV' )
 I11iIi1i1II11 = re . compile ( 'class="css-truncate css-truncate-target"><a href="([^"]*)" class="js-navigation-open" id=".+?" title="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii , ooo in I11iIi1i1II11 :
  if 'READ' in i1I1i111Ii :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( i1I1i111Ii ) . replace ( '.m3u' , '' ) + '[/COLOR]' , ( 'http://raw.githubusercontent.com' + iiI ) . replace ( '/blob' , '' ) , 300000001 , I1IIIii + 'GTV.png' , I1IIIii + 'GTV.png' , 'FluxUstv' )
def i1i1iI1iiiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( oOOo0 )
 for i1I1i111Ii , Ooo0oOooo0 , oOOOoo00 , ooo , url in iI111i :
  if 'INFO' in oOOOoo00 :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + i1I1i111Ii + ooo + '[COLORorangered] - ' + oOOOoo00 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , Ooo0oOooo0 , Ooo0oOooo0 , ( '[COLORsteelblue]' + i1I1i111Ii + ooo + '[COLORorangered] - ' + oOOOoo00 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for Ooo0oOooo0 , oOOOoo00 , ooo , url in IIi11i1i1iI1 :
  if 'INFO' in oOOOoo00 :
   pass
  else :
   O0O0ooOOO ( ( '[COLORsteelblue]' + ooo + '[COLORorangered] - ' + oOOOoo00 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , Ooo0oOooo0 , Ooo0oOooo0 , ( '[COLORsteelblue]' + ooo + '[COLORorangered] - ' + oOOOoo00 + '[/COLOR]' ) . replace ( '_' , ' ' ) )
   if 9 - 9: o0o00Oo0O % o0o00Oo0O - ooo0O
def tools ( ) :
 OoO = [ '[COLOR' + iiI1IiI + ']Change Log[/COLOR]' , '[COLOR' + iiI1IiI + ']Force Genie Update Kodi[/COLOR]' , '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  Ii1I1i ( )
 if iiI1IIIi == 1 :
  Iii1I1I11iiI1 ( )
 if iiI1IIIi == 2 :
  II11IiIi11 ( )
 if iiI1IIIi == 3 :
  IIOOO0O00O0OOOO ( iiI )
 if iiI1IIIi == 4 :
  iI111I11I1I1 . ok ( oo00 , Oo0oO0ooo )
 if iiI1IIIi == 5 :
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 if iiI1IIIi == 6 :
  I1iiii1I ( )
  if 54 - 54: oOo0O0Ooo / O0Oooo0O / iI11I1II1I1I % oOo % i1iIi
def oooO ( ) :
 o00oOOooOOo0o ( 'Stories' , 'http://etc.usf.edu/lit2go/books/' , 21999995 , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , '' )
 o00oOOooOOo0o ( 'Virtual FirePlaces' , 'http://www.virtual-fireplace.net/fireplaces.html' , 21999991 , 'http://www.virtual-fireplace.net/files/theme/burning-log.gif' , 'http://www.virtual-fireplace.net/files/theme/burning-log1.gif' , '' )
 o00oOOooOOo0o ( 'Nature Sounds' , 'http://www.virtual-fireplace.net/sounds.html' , 21999993 , 'http://www.virtual-fireplace.net/files/theme/sound.gif' , 'http://www.virtual-fireplace.net/files/theme/sound-bw.gif' , '' )
def oOoo0oOo00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( '<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , i1I1i111Ii in I11iIi1i1II11 :
  O0O0ooOOO ( i1I1i111Ii , url , 21999992 , 'http://www.virtual-fireplace.net/' + Ooo0oOooo0 , 'http://www.virtual-fireplace.net/' + Ooo0oOooo0 , i1I1i111Ii )
def IiiiIiii11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( 'rel="canonical" href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for url in I11iIi1i1II11 :
  url = ( url ) . replace ( '//www.youtube.com/embed/' , '' ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' )
  yt . PlayVideo ( url )
def OO0000o ( url ) :
 o00oOOooOOo0o ( 'Rain And Thunder' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Water And Forests' , 'http://www.virtual-fireplace.net/water-and-forest.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , '' )
 o00oOOooOOo0o ( 'Beach And Ocean' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , '' )
def i1I1i1 ( url , iconimage ) :
 Ooo0oOooo0 = iconimage
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( '<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url in I11iIi1i1II11 :
  O0O0ooOOO ( i1I1i111Ii , 'http:' + url , 21999992 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
def O0OoooO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( 'data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , i1I1i111Ii , url , ooo0O0o00O in I11iIi1i1II11 :
  o00oOOooOOo0o ( i1I1i111Ii , url , 21999996 , Ooo0oOooo0 , Ooo0oOooo0 , ( ooo0O0o00O ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def I1i11 ( url , iconimage ) :
 Ooo0oOooo0 = iconimage
 ooo0O0o00O = 'desc'
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( '<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , IiIi1I1 in I11iIi1i1II11 :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR] - Audio' , url , 21999997 , Ooo0oOooo0 , Ooo0oOooo0 , ( IiIi1I1 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( IiIi1I1 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR] - Text' , url , 21999998 , Ooo0oOooo0 , Ooo0oOooo0 , ( IiIi1I1 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( IiIi1I1 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def IiIIi1 ( url , iconimage ) :
 Ooo0oOooo0 = iconimage
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( '<a href="([^"]*)">Audio</a>' ) . findall ( oOOo0 )
 for url in I11iIi1i1II11 :
  IIIIiii1IIii ( url )
def II1i11I ( name , url , iconimage ) :
 Ooo0oOooo0 = iconimage
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( '</audio>(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for IiIi1I1 in I11iIi1i1II11 :
  OoOoO ( ( name ) . replace ( ' - Text' , '' ) , ( IiIi1I1 ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  if 50 - 50: ii % i1IiiiI1iI
  if 49 - 49: OOOo00oo0oO - Ii . O0Oooo0O * i1iIi % iiiiiiii1 + ooOoO0O00
def oOO0OOOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , ooo0O0o00O , oo0o0000 , i1I1i111Ii in I11iIi1i1II11 :
  O0O0ooOOO ( i1I1i111Ii , url , 21009 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
  if 11 - 11: iI11I1II1I1I
def IiIIII1i11I ( url ) :
 url = url
 OOO = oOOo0O00o ( )
 if OOO ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif OOO ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 6 - 6: ii
  if 50 - 50: oOoO0o00OO0 % o0o00Oo0O * ooo0O
def i1Iii11Ii1i1 ( ) :
 iiI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( iiI , II1iI1I11I , o0oO0 )
 o0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
 IiI11ii1I ( iiI )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oooiiI ( )
def oOIIiIi ( ) :
 OOoOooOoOOOoo = Iiii1iI1i ( )
 I1ii1ii11i1I = OOoOooOoOOOoo . replace ( ooOoOoo0O , "" )
 if os . path . exists ( OOoOooOoOOOoo ) or not OOoOooOoOOOoo == False :
  o0OoOO = open ( OOoOooOoOOOoo , mode = 'r' ) ; O0O0Oo00 = o0OoOO . read ( ) ; o0OoOO . close ( )
  OoOoO ( "%s - %s" % ( oo00 , I1ii1ii11i1I ) , O0O0Oo00 )
 else :
  oOoO00o ( 'View Log' , 'No Log File Found!' )
def oO00O0 ( log = None , count = None , all = None ) :
 if log == None :
  IIi1IIIi = O00Ooo ( True )
  OOOO0OOO = O00Ooo ( True , True )
  if not OOOO0OOO == False and not IIi1IIIi == False :
   i1i1ii = iI111I11I1I1 . select ( oOo0oooo00o , [ "View %s: %s error(s)" % ( IIi1IIIi . replace ( ooOoOoo0O , "" ) , oO00O0 ( IIi1IIIi , True , True ) ) , "View %s: %s error(s)" % ( OOOO0OOO . replace ( ooOoOoo0O , "" ) , oO00O0 ( OOOO0OOO , True , True ) ) ] )
   if i1i1ii == - 1 : oOoO00o ( '[COLOR %s]View Log[/COLOR]' % iII1ii1 , '[COLOR %s]View Log Cancelled![/COLOR]' % I1i1iiiI1 ) ; return
  elif IIi1IIIi == False and OOOO0OOO == False :
   oOoO00o ( '[COLOR %s]View Log[/COLOR]' % iII1ii1 , '[COLOR %s]No Log File Found![/COLOR]' % I1i1iiiI1 )
   return
  elif not IIi1IIIi == False : i1i1ii = 0
  elif not OOOO0OOO == False : i1i1ii = 1
  log = IIi1IIIi if i1i1ii == 0 else OOOO0OOO
 if log == False :
  if count == None :
   oOoO00o ( "[COLOR %s]%s[/COLOR]" % ( iII1ii1 , oOo0oooo00o ) , "[COLOR %s]Log File not Found[/COLOR]" % I1i1iiiI1 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   o0OoOO = open ( log , mode = 'r' ) ; iIIi = o0OoOO . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; o0OoOO . close ( )
   iI111i = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( iIIi )
   if not count == None :
    if all == None :
     oO0o00oo0 = 0
     for ii1IIII in iI111i :
      if o0OOO in ii1IIII : oO0o00oo0 += 1
     return oO0o00oo0
    else : return len ( iI111i )
   if len ( iI111i ) > 0 :
    oO0o00oo0 = 0 ; O0O0Oo00 = ""
    for ii1IIII in iI111i :
     if all == None and not o0OOO in ii1IIII : continue
     else :
      oO0o00oo0 += 1
      O0O0Oo00 += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( oO0o00oo0 , ii1IIII . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( i1111 , '' ) )
    if oO0o00oo0 > 0 :
     OoOoO ( oOo0oooo00o , O0O0Oo00 )
    else : oOoO00o ( oOo0oooo00o , "No Errors Found in Log" )
   else : oOoO00o ( oOo0oooo00o , "No Errors Found in Log" )
  else : oOoO00o ( oOo0oooo00o , "Log File not Found" )
def O00Ooo ( file = False , old = False , wizard = False ) :
 if wizard == True :
  if not os . path . exists ( Oo0o0000o0o0 ) : return False
  else :
   if file == True :
    return Oo0o0000o0o0
   else :
    oO00oOooooo0 = open ( Oo0o0000o0o0 , 'r' )
    oOoO0OOooOoO = oO00oOooooo0 . read ( )
    oO00oOooooo0 . close ( )
    return oOoO0OOooOoO
 i1II1I1Iii1 = 0
 iiI11Iii = os . listdir ( ooOoOoo0O )
 O0o0O0 = [ ]
 if 11 - 11: IIiIiII11i % oOo * iiiiiiii1 + oOOoOooOo + i1iIi
 for ii1IIII in iiI11Iii :
  if old == True and ii1IIII . endswith ( '.old.log' ) : O0o0O0 . append ( os . path . join ( ooOoOoo0O , ii1IIII ) )
  elif old == False and ii1IIII . endswith ( '.log' ) and not ii1IIII . endswith ( '.old.log' ) : O0o0O0 . append ( os . path . join ( ooOoOoo0O , ii1IIII ) )
  if 24 - 24: I1ii11iIi11i - OOOo00oo0oO % iI11I1II1I1I . ooOoO0O00 / o0o00Oo0O
 if len ( O0o0O0 ) > 0 :
  O0o0O0 . sort ( key = lambda o0OoOO : os . path . getmtime ( o0OoOO ) )
  if file == True : return O0o0O0 [ - 1 ]
  else :
   oO00oOooooo0 = open ( O0o0O0 [ - 1 ] , 'r' )
   oOoO0OOooOoO = oO00oOooooo0 . read ( )
   oO00oOooooo0 . close ( )
   return oOoO0OOooOoO
 else :
  return False
  if 36 - 36: oOo0O0Ooo - i1IiiiI1iI
def i1Iii11Ii1i1 ( ) :
 iiI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( iiI , II1iI1I11I , o0oO0 )
 o0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
 IiI11ii1I ( iiI )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oooiiI ( )
def i11i11111i1i ( ) :
 O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']Todays Games[/COLOR]' , '' , 90030 , I1IIIii + 'tgames.png' , Oo00OOOOO , '' , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Tommys Replays[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , I1IIIii + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 28 - 28: oOOoOooOo + Ii / i1IiiiI1iI % iii1i1iiiiIi % I1ii11iIi11i - o0o00Oo0O
 if 54 - 54: ooOoO0O00 + IIiIiII11i
 if 83 - 83: oOoO0o00OO0 - oOo0O0Ooo + OoOo0o
def iIi1Ii1i1iI ( ) :
 IIiI1 = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 i1iI1 = requests . get ( iiI ) . content
 iI111i = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( i1iI1 )
 ii1 = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( iI111i ) )
 for IIIi1I1IIii1II , i1I1i111Ii in ii1 :
  if not i1I1i111Ii == 'Home' :
   pass
   I1IiiI1ii1i = 'http://www.replaymatches.com/' + IIIi1I1IIii1II
   if i1I1i111Ii in IIiI1 :
    o00oOOooOOo0o ( '[COLORred]' + i1I1i111Ii + '[/COLOR]' , I1IiiI1ii1i , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
   else :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , I1IiiI1ii1i , 900301 , I1IIIii + 'tommysreplays.png' , '' , '' )
    if 78 - 78: oOOoOooOo . ooo0O . OoOo0o . i1IiiiI1iI + OOOo00oo0oO
def i1ii1II1ii ( url ) :
 if 28 - 28: oOoO0o00OO0
 if 61 - 61: OoOo0o % OoOo0o * ooo0O / ooo0O
 if 75 - 75: I11i1ii1 . oOOoOooOo
 if 50 - 50: iii1i1iiiiIi
 if 60 - 60: oOOoOooOo * iI11I1II1I1I * oOoO0o00OO0 * I1ii11iIi11i
 if 69 - 69: i1iIi * o0o00Oo0O . Ii / i1iIi . ooo0O
 if 63 - 63: i1IiiiI1iI + ooo0O . IIiIiII11i - oOo0O0Ooo
 if 52 - 52: ooo0O % I1ii11iIi11i
 if 64 - 64: o0o00Oo0O % i1IiiiI1iI % o0o00Oo0O * oOo . OOOo00oo0oO + oOo0O0Ooo
 if 75 - 75: i1IiiiI1iI . ii % ooo0O * i1IiiiI1iI % ii
 oOOo0 = i11111IIIII ( url )
 I11i1iIiIIIIIii = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( oOOo0 )
 OOo0 = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in I11i1iIiIIIIIii :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 900302 , Ooo0oOooo0 , I1IIIii + 'tommysreplays.png' , '' )
 for ii11I1 in OOo0 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ii11I1 , 900301 , I1IIIii + 'NEXT.png' , '' , '' )
def oO0oo ( url ) :
 i1iI1 = requests . get ( url ) . content
 iI111i = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( i1iI1 )
 for IIIi1I1IIii1II , Ooo0oOooo0 in iI111i :
  if 'Highlight' in Ooo0oOooo0 :
   i1I1i111Ii = 'HighLights'
  elif '1st' in Ooo0oOooo0 :
   i1I1i111Ii = '1st Half'
  elif '2nd' in Ooo0oOooo0 :
   i1I1i111Ii = '2nd Half'
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , IIIi1I1IIii1II , 1001111 , Ooo0oOooo0 , I1IIIii + 'tommysreplays.png' , '' , '' )
def IIIIIo0ooOoO000oO ( ) :
 i1iI1 = requests . get ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 iI111i = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( i1iI1 )
 for OOo , i1i11I1I1iii1 in iI111i :
  O0OOoOOO0oO ( '[COLORred]' + OOo + '[/COLOR]' , '' , '' , I1IIIii + 'tommysreplays.png' , I1IIIii + 'tommysreplays.png' , '' , '' )
  I1iii11 = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( i1i11I1I1iii1 ) )
  for ooo0OiII1iii , i11i1iiiII in I1iii11 :
   O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']' + ooo0OiII1iii + '[/COLOR]' , '' , '' , i11i1iiiII , I1IIIii + 'tommysreplays.png' , '' , '' )
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
 ii1IIII = xbmcgui . ListItem ( path = OOOoO000 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1IIII )
def oOOOO ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 IiIi1ii111i1 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiIi1ii111i1 )
def Iiii1iI1i ( ) :
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
  OoO = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   o0oo0000OO ( )
  if iiI1IIIi == 1 :
   O0oOOo0Oo ( )
  if iiI1IIIi == 2 :
   o000O000 ( ii1oOoO0o0ooo )
  if iiI1IIIi == 3 :
   oO0o0O0Ooo0o ( iiI )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 10060 , I1IIIii + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( O00OOOoOoo0O ) , 49 , I1IIIii + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( O00OOOoOoo0O ) , 41 , I1IIIii + 'WipeGenie.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( O00OOOoOoo0O ) , 44 , I1IIIii + 'GenieBuilds.png' , Oo00OOOOO , '' )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 21 - 21: O0Oooo0O - oOo0O0Ooo + i1IiiiI1iI
def ooOoo0o0O ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if 77 - 77: OOOo00oo0oO
  if 64 - 64: I1ii11iIi11i * ii . I1ii11iIi11i
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
  if 2 - 2: ii % OoOo0o
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( O00OOOoOoo0O ) , 10001 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
  if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
  if 39 - 39: iiiiiiii1 / IIiIiII11i / oOoO0o00OO0 % oOo0O0Ooo
  if 89 - 89: O0Oooo0O + ii + O0Oooo0O * ooOoO0O00 + iI11I1II1I1I % i1IiiiI1iI
  if 59 - 59: OoOo0o + Ii
  if 88 - 88: Ii - oOOoOooOo
  if 67 - 67: OoOo0o . I1ii11iIi11i + iii1i1iiiiIi - ii
  if 70 - 70: OoOo0o / IIiIiII11i - iI11I1II1I1I - iiiiiiii1
 else :
  if 11 - 11: iI11I1II1I1I . ii . IIiIiII11i / ooOoO0O00 - i1IiiiI1iI
  if 30 - 30: iii1i1iiiiIi
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
  if 62 - 62: oOoO0o00OO0 + i1iIi + ooOoO0O00 / ii
 O00oO000O0O ( 'movies' , 'MAIN' )
def IIiiii ( ) :
 OoO = [ '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  iI111i1I1II ( )
 if iiI1IIIi == 1 :
  O00OO ( )
 if iiI1IIIi == 2 :
  II1Ii1iI1i1 ( )
 if iiI1IIIi == 3 :
  o0OoO000O ( )
 if iiI1IIIi == 4 :
  OOoiIIiiIIIi1I ( )
 if iiI1IIIi == 5 :
  OO0o0o0oo0O ( )
  if 40 - 40: ooo0O + I1ii11iIi11i . ooo0O % oOOoOooOo
  if 15 - 15: i1iIi * I1ii11iIi11i % oOoO0o00OO0 * iI11I1II1I1I - Ii
def Oo00OOOOoo0oo ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  OoO = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   O00OOooo0Ooo ( )
  if iiI1IIIi == 1 :
   o0oOOoOOO ( )
  if iiI1IIIi == 2 :
   iiI1i11II ( )
  if iiI1IIIi == 3 :
   II11 ( o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iiI1IIIi == 4 :
   I1iii ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9001 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TOP RATED MOVIES[/COLOR]' , str ( O00OOOoOoo0O ) , 10200 , I1IIIii + 'rated.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , I1IIIii + 'Desi.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , I1IIIii + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , I1IIIii + 'ClassicMovies.png' , Oo00OOOOO , '' )
 O00oO000O0O ( 'movies' , 'MAIN' )
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
  OoO = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , '[COLOR' + iiI1IiI + ']THE SOURCE[/COLOR]' , '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   oOO0OOOOoooO ( )
  if iiI1IIIi == 1 :
   i1ii11 ( 'http://www.tvmaze.com/shows' )
  if iiI1IIIi == 2 :
   ii1i ( )
  if iiI1IIIi == 3 :
   IIi ( )
  if iiI1IIIi == 4 :
   oo0OO ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( O00OOOoOoo0O ) , 9002 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Dans Scrapes[/COLOR]' , 'http://www.tvmaze.com/shows' , 9110001 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RETURN DATES[/COLOR]' , str ( O00OOOoOoo0O ) , 10095 , I1IIIii + 'RD.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( O00OOOoOoo0O ) , 8064 , I1IIIii + 'ClassicTV.png' , Oo00OOOOO , '' )
 O00oO000O0O ( 'movies' , 'MAIN' )
def IiiI11i1I ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   OOo0iiIii1IIi = '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]'
   if 10 - 10: Ii - ooo0O % iI11I1II1I1I
   if 49 - 49: OOOo00oo0oO
   if 83 - 83: OOOo00oo0oO % I1ii11iIi11i - ooo0O . iiiiiiii1 / I1ii11iIi11i % oOoO0o00OO0
   if 75 - 75: o0o00Oo0O % iii1i1iiiiIi . I11i1ii1 / I11i1ii1 / oOo
  OoO = [ OOo0iiIii1IIi , '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , '[COLOR' + iiI1IiI + ']PIRATE MOVIES[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIiiI1iIiIi ( )
  if iiI1IIIi == 1 :
   oo00O0 ( )
  if iiI1IIIi == 2 :
   iiiI111I ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if iiI1IIIi == 3 :
   oooOOO00o0 ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , i1I , i1I1i111Ii )
 else :
  if 7 - 7: Ii . I1ii11iIi11i
  if 99 - 99: i1IiiiI1iI - O0Oooo0O - OOOo00oo0oO % oOo
  if O0oo0OO0 . getSetting ( 'Pandoras Box' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Murrays Mints[/COLOR]' , str ( O00OOOoOoo0O ) , 10025 , I1IIIii + 'PandorasBox.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']TECHNICA STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , I1IIIii + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 21 - 21: IIiIiII11i % oOoO0o00OO0 . ooOoO0O00 - ii
  if 4 - 4: ii . oOOoOooOo
  if 78 - 78: oOoO0o00OO0 + i1IiiiI1iI - o0o00Oo0O
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']BAMF TV[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , I1IIIii + 'bamftv.png' , Oo00OOOOO , '' )
  if 10 - 10: O0Oooo0O % oOo0O0Ooo
  if 97 - 97: ii - O0Oooo0O
  if 58 - 58: iI11I1II1I1I + o0o00Oo0O
  if 30 - 30: oOOoOooOo % iiiiiiii1 * OoOo0o - oOoO0o00OO0 * i1iIi % oOOoOooOo
  if 46 - 46: Ii - o0o00Oo0O . OOOo00oo0oO
  if 100 - 100: oOo0O0Ooo / ooo0O * iiiiiiii1 . o0o00Oo0O / OoOo0o
  if 83 - 83: O0Oooo0O
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 48 - 48: IIiIiII11i * OoOo0o * O0Oooo0O
def i1iiiIii11 ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , I1IIIii + 'SilentHunter.png' , Oo00OOOOO , '' )
def iiiI111I ( url ) :
 i1iI1 = i11111IIIII ( url )
 ii1 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( i1iI1 )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( ii1 ) )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( ii1 ) )
 OOoOOO000O0 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( ii1 ) )
 for i1I1i111Ii , Ooo0oOooo0 , url in iI111i :
  if '247ch' in url :
   oOo0 ( i1I1i111Ii , url , 10190 , Ooo0oOooo0 )
  elif '.m3u' in url :
   oOo0 ( i1I1i111Ii , url , 1019 , Ooo0oOooo0 )
  elif '.xml' in url :
   oOo0 ( i1I1i111Ii , url , 1018 , Ooo0oOooo0 )
  else :
   II1i11I1 ( i1I1i111Ii , url , 222 , Ooo0oOooo0 )
 for i1I1i111Ii , url , Ooo0oOooo0 in IIi11i1i1iI1 :
  if '.xml' in url :
   oOo0 ( i1I1i111Ii , url , 1018 , Ooo0oOooo0 )
  elif '.m3u' in url :
   oOo0 ( i1I1i111Ii , url , 1019 , Ooo0oOooo0 )
  else :
   II1i11I1 ( i1I1i111Ii , url , 222 , Ooo0oOooo0 )
 for i1I1i111Ii , url , Ooo0oOooo0 in OOoOOO000O0 :
  II1i11I1 ( i1I1i111Ii , url , 8043 , Ooo0oOooo0 )
def iiIiIiII ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 222 , I1IIIii + 'BAMFTV.png' )
def iIi ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url , Ooo0oOooo0 in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 222 , Ooo0oOooo0 )
  if 10 - 10: oOo / I1ii11iIi11i
def oo00O0 ( ) :
 if 15 - 15: iiiiiiii1 . iii1i1iiiiIi / iiiiiiii1 * i1IiiiI1iI - oOo0O0Ooo % oOoO0o00OO0
 O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']All Movies[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']Movies By Genre[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']Movies By A - Z[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ) ) , 9110013 , I1IIIii + 'scraped.png' , Oo00OOOOO , '' , '' )
 O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 9110015 , I1IIIii + 'Search.png' , Oo00OOOOO , '' , '' )
 if 57 - 57: o0o00Oo0O % iii1i1iiiiIi % OOOo00oo0oO
 if 45 - 45: oOoO0o00OO0 + IIiIiII11i * Ii
 if 13 - 13: ii * OOOo00oo0oO - i1iIi / OoOo0o + i1IiiiI1iI + I11i1ii1
 if 39 - 39: iI11I1II1I1I - ii
def oO0oooooo ( url ) :
 i1iI1 = requests . get ( url ) . text
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( i1iI1 )
 for o0OO0Oo , I11iiii1I , iiiiI1iiiIi , i11i1iiiII , o0oO0OoO0 , oOOOOOoOO , oo0o0000 in iI111i :
  if oo0o0000 == ' ' :
   oo0o0000 = Oo00OOOOO
  if i11i1iiiII == ' ' :
   i11i1iiiII = O0O
  o0oO0OoO0 = o0oO0OoO0 . replace ( '\\n' , ' ' )
  if I11iiii1I == 'Movie Search' :
   Ii111iIi1iIi ( o0OO0Oo , oOOOOOoOO , 9110014 , i11i1iiiII , oo0o0000 , o0oO0OoO0 , '' )
  elif I11iiii1I == 'Menu' :
   O0OOoOOO0oO ( o0OO0Oo , iiiiI1iiiIi , 9110013 , i11i1iiiII , oo0o0000 , o0oO0OoO0 , '' )
   if 81 - 81: IIiIiII11i + Ii / iiiiiiii1
def oo00OoO ( name , url ) :
 from imports import Scrape_Nan
 name = str ( name )
 oOOOOOoOO = str ( url )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( name , oOOOOOoOO , '' )
 if 30 - 30: I1ii11iIi11i . oOo
def o0Oii1111i ( ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 O0ooOO = iI111I11I1I1 . input ( 'Search your moive' , type = xbmcgui . INPUT_ALPHANUM )
 IIiI1 = [ 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ]
 for iiI in IIiI1 :
  i1iI1 = requests . get ( o0oOoO00o ( iiI ) ) . content
  iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( i1iI1 )
  for o0OO0Oo , I11iiii1I , iiiiI1iiiIi , i11i1iiiII , o0oO0OoO0 , oOOOOOoOO , oo0o0000 in iI111i :
   if oo0o0000 == ' ' :
    oo0o0000 = Oo00OOOOO
   if i11i1iiiII == ' ' :
    i11i1iiiII = O0O
   o0oO0OoO0 = o0oO0OoO0 . replace ( '\\n' , ' ' )
   if I11iiii1I == 'Movie Search' :
    if O0ooOO . lower ( ) in o0OO0Oo . lower ( ) :
     Ii111iIi1iIi ( o0OO0Oo , oOOOOOoOO , 9110014 , i11i1iiiII , oo0o0000 , o0oO0OoO0 , '' )
def IiiI ( url ) :
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oOOo0 )
 for i1I1i111Ii , url , I11iiii1I , i11I1 , oo0o0000 , ooo0O0o00O in iI111i :
  if i11I1 == '123' :
   i11I1 = I1IIIii + 'appstreams.png'
  if oo0o0000 == '123' :
   oo0o0000 = I1IIIii + 'appstreams.png'
  if 'php' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 100010 , i11I1 , oo0o0000 , ooo0O0o00O )
  elif 'playlist' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 100007 , i11I1 , oo0o0000 , ooo0O0o00O )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 100100 , i11I1 , oo0o0000 , ooo0O0o00O )
  elif not 'http' in url :
   Ii111iIi1iIi ( i1I1i111Ii , url , 100009 , i11I1 , oo0o0000 , ooo0O0o00O , '' )
  else :
   Ii111iIi1iIi ( i1I1i111Ii , url , 100005 , i11I1 , oo0o0000 , ooo0O0o00O , '' )
   if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + iiiiiiii1 * iI11I1II1I1I % i1iIi
def I1iI1I1 ( url ) :
 oOOo0 = i11ii ( url )
 I11iIi1i1II11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , ooo0O0o00O , oo0o0000 , i1I1i111Ii in I11iIi1i1II11 :
  if Ooo0oOooo0 == '123' :
   Ooo0oOooo0 = I1IIIii + 'appstreams.png'
  if oo0o0000 == '123' :
   oo0o0000 = Oo00OOOOO
  if 'php' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 100004 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
  elif 'playlist' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 100007 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
  elif 'watchseries' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 100100 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
  elif not 'http' in url :
   Ii111iIi1iIi ( i1I1i111Ii , url , 100009 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O , '' )
  else :
   Ii111iIi1iIi ( i1I1i111Ii , url , 100005 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O , '' )
   if 48 - 48: oOo0O0Ooo / Ii - ooo0O * OOOo00oo0oO / ii
def OoOo ( url ) :
 if 17 - 17: i1iIi . Ii
 oOOo0 = i11ii ( url )
 IIIiiiI = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oOOo0 )
 for ii1 in IIIiiiI :
  i11I1 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( ii1 ) )
  for i11I1 in i11I1 :
   i11I1 = i11I1
  i1I1i111Ii = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( ii1 ) )
  for i1I1i111Ii in i1I1i111Ii :
   if 'elete' in i1I1i111Ii :
    pass
   elif 'rivate Vid' in i1I1i111Ii :
    pass
   else :
    i1I1i111Ii = ( i1I1i111Ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  OoO00oo00 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( ii1 ) )
  for OoO00oo00 in OoO00oo00 :
   OoO00oo00 = OoO00oo00
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( ii1 ) )
  for url in url :
   url = url
  Ii111iIi1iIi ( '[COLORred]' + str ( OoO00oo00 ) + '[/COLOR] : ' + str ( i1I1i111Ii ) , str ( url ) , 100009 , str ( i11I1 ) , Oo00OOOOO , '' , '' )
  O00oO000O0O ( 'movies' , '' )
  if 76 - 76: ii + I1ii11iIi11i % I11i1ii1 . oOo + IIiIiII11i
def oO0o ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search Dans Scrapes' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'http://www.tvmaze.com/search?q=' + ( O0ooOO ) . replace ( ' ' , '+' )
 i1oOOOOOOOoO = OooooOoO . lower ( )
 oOOo0 = i11111IIIII ( i1oOOOOOOOoO )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  I1 = 'http://www.tvmaze.com' + iiI . replace ( '"' , '' )
  IIiI = requests . get ( I1 ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiI )
  for ooo0O0o00O in iI111i :
   if not '<div>' in ooo0O0o00O :
    O0oOOo0o = ooo0O0o00O . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   Ooo0oOooo0 = 'http:' + Ooo0oOooo0
   i1I1i111Ii = i1I1i111Ii . replace ( '&#039;' , '' )
   if i1I1i111Ii == '' :
    I1III11iiii11i1 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( iiI ) )
    for i1I1i111Ii in I1III11iiii11i1 :
     i1I1i111Ii = i1I1i111Ii . replace ( '-' , ' ' )
  O0OOoOOO0oO ( i1I1i111Ii , I1 , 9110002 , Ooo0oOooo0 , Oo00OOOOO , O0oOOo0o , '' )
  if 54 - 54: ooOoO0O00 - OOOo00oo0oO
def i1ii11 ( url ) :
 oOo0 ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 9110004 , I1IIIii + 'Search.png' , Oo00OOOOO , '' )
 i1iI1 = requests . get ( url ) . content
 iI111i = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( i1iI1 )
 ii11I1 = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  I1 = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  if 18 - 18: iI11I1II1I1I + I1ii11iIi11i - OoOo0o + ii * ii
  IIiI = requests . get ( I1 ) . content
  iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiI )
  for ooo0O0o00O in iI111i :
   if not '<div>' in ooo0O0o00O :
    O0oOOo0o = ooo0O0o00O . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   Ooo0oOooo0 = 'http:' + Ooo0oOooo0
   i1I1i111Ii = i1I1i111Ii . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if i1I1i111Ii == '' :
    I1III11iiii11i1 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for i1I1i111Ii in I1III11iiii11i1 :
     i1I1i111Ii = i1I1i111Ii . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  O0OOoOOO0oO ( i1I1i111Ii , I1 , 9110002 , Ooo0oOooo0 , Oo00OOOOO , O0oOOo0o , '' )
  if 41 - 41: oOOoOooOo . I1ii11iIi11i + oOo0O0Ooo
 for OOo0 in ii11I1 :
  url = 'http://www.tvmaze.com' + OOo0
  O0OOoOOO0oO ( 'NEXT' , url , 9110001 , Ooo0oOooo0 , Oo00OOOOO , '' , '' )
def o0O0OO ( url ) :
 i1iI1 = requests . get ( url ) . content
 iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( i1iI1 )
 for ooo0O0o00O in iI111i :
  O0oOOo0o = ooo0O0o00O . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
 return O0oOOo0o
def Ii1II11II1iii ( url , name , iconimage ) :
 o0OO0Oo = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 Ooo0oOooo0 = iconimage
 i1iI1 = requests . get ( url + '/episodes' ) . content
 IIiI = requests . get ( url ) . content
 ii1 = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( i1iI1 )
 iI111i = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( IIiI )
 for o0oOO0ooOoO in iI111i :
  o0oOO0ooOoO = o0oOO0ooOoO . replace ( ' ' , '' )
 for ooO0000o00O , i1i11I1I1iii1 in ii1 :
  if not 'special' in ooO0000o00O . lower ( ) :
   ooO0000o00O = ooO0000o00O . replace ( 'S' , '' ) . replace ( 's' , '' )
  O0Ooo = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( i1i11I1I1iii1 ) )
  for oO00oOOo0Oo , IIiIIIIii , iI in O0Ooo :
   if not 'special' in oO00oOOo0Oo . lower ( ) :
    O0OOoOOO0oO ( o0OO0Oo + ' - SEASON -' + ooO0000o00O + '- EPISODE-' + oO00oOOo0Oo + '-' + o0oOO0ooOoO , '' , 9110003 , Ooo0oOooo0 , Oo00OOOOO , '' , o0OO0Oo )
    if 5 - 5: ooo0O . iI11I1II1I1I % iI11I1II1I1I
    if 56 - 56: ii - i1IiiiI1iI - ooOoO0O00
    if 8 - 8: O0Oooo0O / OoOo0o . oOo0O0Ooo + oOoO0o00OO0 / Ii
def I1Iii1iI1 ( name , extra ) :
 if 86 - 86: o0o00Oo0O
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Checking for stream' )
 from imports import Scrape_Nan
 O0o0oOooOoOo = name + '<>'
 I1i = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( O0o0oOooOoOo ) )
 for o0OO0Oo , Oo , IiIiIi1I1 , o0oOO0ooOoO in I1i :
  o0OO0Oo = o0OO0Oo
  Oo = Oo
  IiIiIi1I1 = IiIiIi1I1
  IiI1ii1Ii = ''
  Scrape_Nan . scrape_episode ( o0OO0Oo , o0oOO0ooOoO , '' , Oo , IiIiIi1I1 , '' )
if 51 - 51: Ii * ooo0O / oOo0O0Ooo
if 40 - 40: oOo0O0Ooo
if 36 - 36: oOOoOooOo / iiiiiiii1 - I11i1ii1 - I11i1ii1
if 82 - 82: oOoO0o00OO0
if 29 - 29: I11i1ii1
if 66 - 66: I1ii11iIi11i
if 97 - 97: ooOoO0O00 - ii / O0Oooo0O * oOo0O0Ooo
if 55 - 55: ooo0O . iiiiiiii1
if 87 - 87: ooo0O % iI11I1II1I1I
if 100 - 100: O0Oooo0O . oOo0O0Ooo * O0Oooo0O - oOo0O0Ooo . i1IiiiI1iI * i1iIi
if 89 - 89: oOo + I11i1ii1 * O0Oooo0O
def Ii1 ( ) :
 O0OOoOOO0oO ( 'Featured 24/7' , '' , 9070000 , I1IIIii + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 O0OOoOOO0oO ( '24/7 Tv Thows' , '' , 9080000 , I1IIIii + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 O0OOoOOO0oO ( '24/7 Movies' , '' , 9090000 , I1IIIii + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 O0OOoOOO0oO ( '24/7 Cable' , '' , 9100000 , I1IIIii + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 O0OOoOOO0oO ( '24/7 Random Stream' , '' , 9110000 , I1IIIii + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 62 - 62: ooOoO0O00 - ooOoO0O00
def oOOO0O0Ooo ( ) :
 iiI = 'http://arconaitv.me/'
 IiI1i111IiIiIi1 = 'index.php#shows'
 i1iI1 = BeautifulSoup ( requests . get ( iiI + IiI1i111IiIiIi1 ) . content )
 i1II11II1 = i1iI1 . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for II1IIIii in i1II11II1 :
  iIIIiIi1I1i = II1IIIii . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in iIIIiIi1I1i :
   OoOOoO0oOo = IIIi1I1IIii1II . text
  O0ooOOOO0O0 = II1IIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in O0ooOOOO0O0 :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    i1IIi1i1Ii1 = iiI + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    i1I1i111Ii = IIIi1I1IIii1II [ 'title' ]
   Iii = { 'User-Agent' : random_agent ( ) }
   o0Oo0oO = requests . get ( i1IIi1i1Ii1 , headers = Iii ) . content
   iIII1iiIi11 = packets ( o0Oo0oO )
   if 84 - 84: Ii * oOo
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
   for I1I1iII1i in iI111i :
    I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ii111iIi1iIi ( i1I1i111Ii , iiIIii , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 70 - 70: ooo0O - OoOo0o
    if 62 - 62: i1IiiiI1iI
def O000oOo ( ) :
 iiI = 'http://arconaitv.me/'
 IiI1i111IiIiIi1 = 'index.php#movies'
 i1iI1 = BeautifulSoup ( requests . get ( iiI + IiI1i111IiIiIi1 ) . content )
 i1II11II1 = i1iI1 . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for II1IIIii in i1II11II1 :
  iIIIiIi1I1i = II1IIIii . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in iIIIiIi1I1i :
   OoOOoO0oOo = IIIi1I1IIii1II . text
  O0ooOOOO0O0 = II1IIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in O0ooOOOO0O0 :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    i1IIi1i1Ii1 = iiI + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    i1I1i111Ii = IIIi1I1IIii1II [ 'title' ]
   Iii = { 'User-Agent' : random_agent ( ) }
   o0Oo0oO = requests . get ( i1IIi1i1Ii1 , headers = Iii ) . content
   iIII1iiIi11 = packets ( o0Oo0oO )
   if 53 - 53: iI11I1II1I1I + ooo0O - iii1i1iiiiIi - OOOo00oo0oO / oOOoOooOo % Ii
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
   for I1I1iII1i in iI111i :
    I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ii111iIi1iIi ( i1I1i111Ii , iiIIii , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 3 - 3: iiiiiiii1 . oOOoOooOo % oOo0O0Ooo + oOoO0o00OO0
    if 64 - 64: ooOoO0O00
def IIii1 ( ) :
 iiI = 'http://arconaitv.me/'
 IiI1i111IiIiIi1 = 'index.php#cable'
 i1iI1 = BeautifulSoup ( requests . get ( iiI + IiI1i111IiIiIi1 ) . content )
 i1II11II1 = i1iI1 . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for II1IIIii in i1II11II1 :
  iIIIiIi1I1i = II1IIIii . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for IIIi1I1IIii1II in iIIIiIi1I1i :
   OoOOoO0oOo = IIIi1I1IIii1II . text
  O0ooOOOO0O0 = II1IIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in O0ooOOOO0O0 :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    i1IIi1i1Ii1 = iiI + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    i1I1i111Ii = IIIi1I1IIii1II [ 'title' ]
   Iii = { 'User-Agent' : random_agent ( ) }
   o0Oo0oO = requests . get ( i1IIi1i1Ii1 , headers = Iii ) . content
   iIII1iiIi11 = packets ( o0Oo0oO )
   if 35 - 35: Ii - oOo0O0Ooo / OoOo0o + i1iIi * OOOo00oo0oO
   iI111i = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
   for I1I1iII1i in iI111i :
    I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ii111iIi1iIi ( i1I1i111Ii , iiIIii , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 49 - 49: ooo0O * i1iIi + i1IiiiI1iI + iiiiiiii1
def IIi11 ( ) :
 IIiI = 'http://arconaitv.me/stream.php?id=random'
 Iii = { 'User-Agent' : random_agent ( ) }
 o0Oo0oO = requests . get ( IIiI , headers = Iii ) . content
 iIII1iiIi11 = packets ( o0Oo0oO )
 if 89 - 89: IIiIiII11i * oOOoOooOo . OOOo00oo0oO
 iI111i = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
 for I1I1iII1i in iI111i :
  I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  Ii111iIi1iIi ( 'Random Pick' , iiIIii , 9060000 , I1IIIii + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 85 - 85: oOoO0o00OO0 + i1iIi * oOo0O0Ooo % Ii
def iI1i ( ) :
 iiI = 'http://arconaitv.me/'
 IiI1i111IiIiIi1 = 'index.php#shows'
 if 31 - 31: i1iIi
 i1iI1 = BeautifulSoup ( requests . get ( iiI + IiI1i111IiIiIi1 ) . content )
 i1II11II1 = i1iI1 . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for II1IIIii in i1II11II1 :
  iIIIiIi1I1i = II1IIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in iIIIiIi1I1i :
   if IIIi1I1IIii1II . has_key ( 'href' ) :
    i1IIi1i1Ii1 = iiI + IIIi1I1IIii1II [ 'href' ]
   if IIIi1I1IIii1II . has_key ( 'title' ) :
    i1I1i111Ii = IIIi1I1IIii1II [ 'title' ]
   OoOOo00 = IIIi1I1IIii1II . findAll ( 'img' )
   for O00 in OoOOo00 :
    Ooo0oOooo0 = iiI + O00 [ 'src' ]
    Iii = { 'User-Agent' : random_agent ( ) }
    o0Oo0oO = requests . get ( i1IIi1i1Ii1 , headers = Iii ) . content
    iIII1iiIi11 = packets ( o0Oo0oO )
    if 94 - 94: i1IiiiI1iI . i1IiiiI1iI + Ii - OoOo0o * oOoO0o00OO0
    iI111i = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
    for I1I1iII1i in iI111i :
     I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     Ii111iIi1iIi ( i1I1i111Ii , iiIIii , 9060000 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
     if 9 - 9: ooo0O . oOo0O0Ooo - oOoO0o00OO0
def IiiiI ( name , url ) :
 import urlresolver
 try :
  iiIIi = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiIIi , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 36 - 36: i1IiiiI1iI . IIiIiII11i
 if 25 - 25: OOOo00oo0oO
def iI1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 I11iIi1i1II11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , ooo0O0o00O , oo0o0000 , i1I1i111Ii in I11iIi1i1II11 :
  if '.php' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 100210 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
  else :
   O0O0ooOOO ( i1I1i111Ii , url , 222 , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
   if 11 - 11: oOo
   if 18 - 18: iiiiiiii1 - OOOo00oo0oO % iiiiiiii1 / i1IiiiI1iI
   if 68 - 68: i1iIi * iI11I1II1I1I + O0Oooo0O % iii1i1iiiiIi
def IIii1I1I1I ( iconimage , url , extra ) :
 i11I1 = ' '
 OoOOOo0 = ' '
 oo0o0000 = ' '
 Oo = ' '
 o00IIIIII1II1I = i11ii ( url )
 i11I1 = re . compile ( '<img src="(.+?)">' ) . findall ( o00IIIIII1II1I )
 for i11I1 in i11I1 :
  i11I1 = i11I1
 oOoOo0OOOOO = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( o00IIIIII1II1I )
 for oo0o0000 in oOoOo0OOOOO :
  oo0o0000 = oo0o0000
 iI111i = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( o00IIIIII1II1I )
 for url , Oo in iI111i :
  Oo = 'S' + ( Oo ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o00OO00OoO + url
  O0OOoOOO0oO ( ( Oo ) . replace ( '  ' , '' ) , url , 100101 , i11I1 , oo0o0000 , OoOOOo0 , '' )
  O00oO000O0O ( 'Movies' , 'info' )
  if 83 - 83: o0o00Oo0O * iI11I1II1I1I
def OOOo00 ( url , name , fanart , extra , iconimage ) :
 OoIIi1iI = extra
 Oo = name
 o00IIIIII1II1I = i11ii ( url )
 i11I1 = iconimage
 iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( o00IIIIII1II1I )
 for url , name , oO0Ooo0OooOOo in iI111i :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o00OO00OoO + url
  oO0Ooo0OooOOo = oO0Ooo0OooOOo
  O00o0O = name + ' - [COLORred]' + oO0Ooo0OooOOo + '[/COLOR]'
  O0OOoOOO0oO ( O00o0O , url , 100102 , i11I1 , fanart , 'Aired : ' + oO0Ooo0OooOOo , O00o0O )
  if 32 - 32: ooo0O + iii1i1iiiiIi - ii
def Ii11iii1II1i ( name , URL , iconimage , fanart ) :
 oOOo0 = i11ii ( URL )
 iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , name in iI111i :
  for ii1IIII in OOOO0OOoO0O0 :
   if ii1IIII in iiI :
    URL = 'http://www.watchseriesgo.to/link/' + iiI
    Ii111iIi1iIi ( name , URL , 100106 , I1IIIii + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( iI111i ) <= 0 :
  O0OOoOOO0oO ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 65 - 65: i1iIi + oOo - ii
  if 51 - 51: I1ii11iIi11i + OOOo00oo0oO / iiiiiiii1 - ooOoO0O00
def oO0O0oO0 ( url , name ) :
 I11Ii1iI11iI1 = name
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oOOo0 )
 OOoOOO000O0 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oOOo0 )
 for url in iI111i :
  i1III1 ( url , I11Ii1iI11iI1 )
 for url in IIi11i1i1iI1 :
  i1III1 ( url , I11Ii1iI11iI1 )
 for url in OOoOOO000O0 :
  i1III1 ( url , I11Ii1iI11iI1 )
  if 43 - 43: IIiIiII11i % O0Oooo0O . i1IiiiI1iI % o0o00Oo0O - ii + o0o00Oo0O
def i1III1 ( url , season_name ) :
 if 'daclips.in' in url :
  OooO0ooo0 ( url , season_name )
 elif 'filehoot.com' in url :
  iIiI ( url , season_name )
 elif 'allmyvideos.net' in url :
  oO00Ooo0oO ( url , season_name )
 elif 'vidspot.net' in url :
  OOOo ( url , season_name )
 elif 'vodlocker' in url :
  o0ooOo00O ( url , season_name )
 elif 'vidto' in url :
  Ii1i1I1 ( url , season_name )
  if 97 - 97: O0Oooo0O . oOOoOooOo - O0Oooo0O + oOo0O0Ooo * IIiIiII11i
  if 10 - 10: i1iIi + i1IiiiI1iI % ii - oOo0O0Ooo
def Ii1i1I1 ( url , season_name ) :
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for I1IiiI1ii1i , i1I1i111Ii in iI111i :
  o00oooOo ( I1IiiI1ii1i , season_name )
  if 29 - 29: o0o00Oo0O . O0Oooo0O
  if 66 - 66: OOOo00oo0oO * iI11I1II1I1I % iI11I1II1I1I * I11i1ii1 - oOOoOooOo - I11i1ii1
def oO00Ooo0oO ( url , season_name ) :
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOo0 )
 for I1IiiI1ii1i , i1I1i111Ii in iI111i :
  o00oooOo ( I1IiiI1ii1i , season_name )
  if 70 - 70: O0Oooo0O + OOOo00oo0oO
def OOOo ( url , season_name ) :
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oOOo0 )
 for I1IiiI1ii1i , i1I1i111Ii in iI111i :
  o00oooOo ( I1IiiI1ii1i , season_name )
  if 93 - 93: O0Oooo0O + i1iIi
def o0ooOo00O ( url , season_name ) :
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for I1IiiI1ii1i in iI111i :
  o00oooOo ( I1IiiI1ii1i , season_name )
  if 33 - 33: o0o00Oo0O
def OooO0ooo0 ( url , season_name ) :
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oOOo0 )
 for I1IiiI1ii1i in iI111i :
  o00oooOo ( I1IiiI1ii1i , season_name )
  if 78 - 78: o0o00Oo0O / IIiIiII11i * oOo
def iIiI ( url , season_name ) :
 oOOo0 = i11ii ( url )
 iI111i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOo0 )
 for I1IiiI1ii1i in iI111i :
  o00oooOo ( I1IiiI1ii1i , season_name )
  if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % O0Oooo0O - iI11I1II1I1I % o0o00Oo0O
def o00oooOo ( Link , season_name ) :
 if 'http:/' in Link :
  o0oO0Oo ( Link )
  if 71 - 71: ooo0O - iii1i1iiiiIi * iiiiiiii1 + i1iIi % Ii - oOOoOooOo
  if 82 - 82: O0Oooo0O - OoOo0o + oOo
def OO0 ( url ) :
 oOOo0 = OPEN_URL_1 ( url )
 iIiiIi11IIi = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOo0 )
 for url in iIiiIi11IIi :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 64 - 64: ii . oOoO0o00OO0 % o0o00Oo0O + oOo0O0Ooo - ooo0O
def O0OOoOOO0oO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = True )
 return oOO
 if 11 - 11: ooOoO0O00 % oOo % iiiiiiii1
 if 99 - 99: oOOoOooOo / iI11I1II1I1I - i1iIi * oOoO0o00OO0 % oOo0O0Ooo
def Ii111iIi1iIi ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1II1i = [ ]
  i1II1i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  ooooo0OoO0 . addContextMenuItems ( i1II1i )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = False )
 return oOO
 if 10 - 10: i1iIi - iii1i1iiiiIi . ii . OoOo0o . oOo * iiiiiiii1
def OOOOOo ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 50 - 50: i1iIi - Ii + iI11I1II1I1I / o0o00Oo0O - i1iIi + ooo0O
def Iii111Ii1 ( url ) :
 III11 = xbmc . Player ( Ii1Ii11Iii1i1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : III11 . play ( url ) . strip ( )
 except : pass
 if 33 - 33: i1IiiiI1iI
def o0oO0Oo ( url ) :
 III11 = xbmc . Player ( )
 import urlresolver
 try : III11 . play ( url )
 except : pass
 if 87 - 87: iii1i1iiiiIi / I11i1ii1 + iI11I1II1I1I
def i11ii ( url ) :
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
  if 93 - 93: iI11I1II1I1I + OOOo00oo0oO % oOOoOooOo
  if 21 - 21: OoOo0o
  if 6 - 6: I11i1ii1
def O00OO ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  OoO = [ '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' ]
  if 46 - 46: I11i1ii1 + OOOo00oo0oO
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , OoO )
  if 79 - 79: ii - I11i1ii1 * I11i1ii1 . iii1i1iiiiIi
  if 100 - 100: IIiIiII11i * i1IiiiI1iI % oOo0O0Ooo / oOoO0o00OO0
  if 90 - 90: oOoO0o00OO0 . oOOoOooOo . iii1i1iiiiIi . i1iIi
  if 4 - 4: i1iIi + iii1i1iiiiIi % oOoO0o00OO0 / Ii
  if iiI1IIIi == 0 :
   OoOi111i ( )
   if 46 - 46: oOo * I1ii11iIi11i % OOOo00oo0oO + o0o00Oo0O * I11i1ii1
   if 34 - 34: oOo
   if 27 - 27: i1iIi - o0o00Oo0O % i1IiiiI1iI * O0Oooo0O . I11i1ii1 % iI11I1II1I1I
   if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % oOOoOooOo
 else :
  if 24 - 24: iii1i1iiiiIi
  if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + OoOo0o
  if 28 - 28: oOo0O0Ooo
  if O0oo0OO0 . getSetting ( 'Cartoons' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , I1IIIii + 'Cartoons.png' , Oo00OOOOO , '' )
   if 49 - 49: i1IiiiI1iI . ooo0O % OOOo00oo0oO / i1iIi
   if 95 - 95: o0o00Oo0O * iii1i1iiiiIi * I11i1ii1 . oOOoOooOo / iI11I1II1I1I
   if 28 - 28: I11i1ii1 + OOOo00oo0oO - oOOoOooOo / iI11I1II1I1I - oOo0O0Ooo
 O00oO000O0O ( 'movies' , 'MAIN' )
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
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 45 - 45: o0o00Oo0O / ooOoO0O00 * OOOo00oo0oO * oOo
 if 35 - 35: oOoO0o00OO0 / iiiiiiii1 % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: iii1i1iiiiIi / oOOoOooOo
def I1I1i1I ( ) :
 oOOo0 = i11111IIIII ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 iI111i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oOOo0 )
 for OOooOoooOoOo in iI111i :
  OOooOoooOoOo = ( str ( OOooOoooOoOo ) )
  if os . path . exists ( xbmc . translatePath ( OOooOoooOoOo ) ) :
   oOo00o = ( OOooOoooOoOo ) . replace ( 'special://home/addons/' , '' )
   OoOoO ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oOo00o + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iiI1IIIi = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iiI1IIIi == 0 :
    OOoooooooO ( OOooOoooOoOo )
    oooiiI ( )
   elif iiI1IIIi == 1 :
    iIIii1 ( OOooOoooOoOo )
  else :
   pass
   if 41 - 41: iii1i1iiiiIi . Ii / i1IiiiI1iI
def iIIii1 ( addon ) :
 oOo00o = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oO0 . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oO0 . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oO0 . close ( )
 if 98 - 98: iii1i1iiiiIi % IIiIiII11i
def OOoooooooO ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OoO0O000 = os . path . join ( IIIII , 'default.py' )
 II1Ii = open ( OoO0O000 , "w+" )
 if 6 - 6: ooOoO0O00 - IIiIiII11i * ooo0O . oOo
 II1Ii . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 II1Ii . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 II1Ii . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 68 - 68: ooo0O
 if 20 - 20: O0Oooo0O - O0Oooo0O
 if 37 - 37: I11i1ii1
 if 37 - 37: I1ii11iIi11i / I11i1ii1 * o0o00Oo0O
def o0o00O0oOooO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 o0oO0OO00ooOO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 I1iii11 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 OOoOOO000O0 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IiIIiii11II1 = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oOOo0 )
 iiii1i1II1 = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url , ooOO0ooo0o , oo0o0000 , ooo0O0o00O in o0oO0OO00ooOO :
  if 'php' in url :
   o00oOOooOOo0o ( i1I1i111Ii , url , 90037 , ooOO0ooo0o , oo0o0000 , ooo0O0o00O )
  elif i1I1i111Ii == 'Search' :
   o00oOOooOOo0o ( 'Search' , url , 90038 , ooOO0ooo0o , oo0o0000 , ooo0O0o00O )
  else :
   O0O0ooOOO ( i1I1i111Ii , url , 222 , ooOO0ooo0o , oo0o0000 , ooo0O0o00O )
 for i1I1i111Ii , Ooo0oOooo0 , url , i1IiI1I in I1iii11 :
  o00oOOooOOo0o ( i1I1i111Ii , url , 90037 , Ooo0oOooo0 , i1IiI1I , '' )
 for i1I1i111Ii , Ooo0oOooo0 , url , i1IiI1I in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 90037 , Ooo0oOooo0 , i1IiI1I , '' )
 for i1I1i111Ii , url , Ooo0oOooo0 , i1IiI1I in IIi11i1i1iI1 :
  O0O0ooOOO ( i1I1i111Ii , url , 222 , Ooo0oOooo0 , i1IiI1I , '' )
 for i1I1i111Ii , url , Ooo0oOooo0 , i1IiI1I in OOoOOO000O0 :
  O0O0ooOOO ( i1I1i111Ii , url , 222 , Ooo0oOooo0 , i1IiI1I , '' )
 for i1I1i111Ii , url , Ooo0oOooo0 , i1IiI1I in IiIIiii11II1 :
  O0O0ooOOO ( i1I1i111Ii , url , 222 , Ooo0oOooo0 , i1IiI1I , '' )
 for i1I1i111Ii , url , Ooo0oOooo0 in iiii1i1II1 :
  O0O0ooOOO ( i1I1i111Ii , url , 222 , Ooo0oOooo0 , '' , '' )
  O00oO000O0O ( 'tvshows' , 'Media Info 3' )
def o0OOo00oO0oOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , Ooo0oOooo0 , url , i1IiI1I in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 90037 , Ooo0oOooo0 , i1IiI1I , '' )
 for i1I1i111Ii , url , Ooo0oOooo0 , i1IiI1I in IIi11i1i1iI1 :
  O0O0ooOOO ( i1I1i111Ii , url , 222 , Ooo0oOooo0 , i1IiI1I , '' )
  O00oO000O0O ( 'tvshows' , 'Media Info 3' )
  if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
def OOOO0oOo00O ( ) :
 i1I1I1i1i1i = [ 'serialsearch' , 'moviesearch' ]
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 if i1oOOOOOOOoO == '' :
  pass
 else :
  for ii1o0oo0Ooooo0 in i1I1I1i1i1i :
   Oo0oOo000OoO0 = oOOoo00O0O + ii1o0oo0Ooooo0 + '.php'
   o00IIIIII1II1I = i11111IIIII ( Oo0oOo000OoO0 )
   if o00IIIIII1II1I != 'Opened' :
    I11iIi1i1II11 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( o00IIIIII1II1I )
    for i1I1i111Ii , iiI , ooOO0ooo0o , oo0o0000 , ooo0O0o00O in I11iIi1i1II11 :
     if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
      IIii1I1i = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( oO0 ) )
      for ii1IIII in IIii1I1i :
       if ii1IIII == iiI :
        i1I1i111Ii = '[COLORred]* [/COLOR]' + ( i1I1i111Ii ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        IIII1iIIii = open ( O0Oo000ooO00 , "a" )
        IIII1iIIii . write ( 'item="' + i1I1i111Ii + '"\n' )
        IIII1iIIii . close
      if 'php' in iiI :
       o00oOOooOOo0o ( i1I1i111Ii , iiI , 90037 , ooOO0ooo0o , oo0o0000 , ooo0O0o00O )
      else :
       O0O0ooOOO ( i1I1i111Ii , iiI , 222 , ooOO0ooo0o , oo0o0000 , ooo0O0o00O )
       if 12 - 12: iI11I1II1I1I . i1iIi . oOoO0o00OO0 % oOo0O0Ooo . IIiIiII11i . OOOo00oo0oO
   O00oO000O0O ( 'tvshows' , 'Media Info 3' )
   if 32 - 32: oOoO0o00OO0 + I11i1ii1 / o0o00Oo0O / iii1i1iiiiIi * ii % oOOoOooOo
def iIiiIIi ( ) :
 if 93 - 93: oOOoOooOo . oOoO0o00OO0 + iI11I1II1I1I * i1IiiiI1iI * i1IiiiI1iI / oOoO0o00OO0
 if 28 - 28: oOo - OOOo00oo0oO + iii1i1iiiiIi + i1iIi / iI11I1II1I1I
 if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
 if 68 - 68: OoOo0o + OOOo00oo0oO . o0o00Oo0O . i1iIi % ooOoO0O00 % OoOo0o
 if 50 - 50: I11i1ii1 + ooo0O
 if 96 - 96: oOo
 if 92 - 92: I1ii11iIi11i / Ii + oOoO0o00OO0
 if 87 - 87: iii1i1iiiiIi % iI11I1II1I1I
 if 72 - 72: OoOo0o . OoOo0o - oOoO0o00OO0
 if 48 - 48: I1ii11iIi11i - oOOoOooOo + I1ii11iIi11i - oOo0O0Ooo * Ii . iiiiiiii1
 if 35 - 35: I11i1ii1 . o0o00Oo0O + I1ii11iIi11i + OoOo0o + ooOoO0O00
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . iii1i1iiiiIi
 if 87 - 87: IIiIiII11i * oOoO0o00OO0 % I1ii11iIi11i * I1ii11iIi11i
 if 58 - 58: OoOo0o . ooo0O + oOo0O0Ooo % I1ii11iIi11i - oOo
 if 50 - 50: iiiiiiii1 % IIiIiII11i - oOOoOooOo . ooOoO0O00 + o0o00Oo0O % iiiiiiii1
 if 10 - 10: iiiiiiii1 . ooOoO0O00 + i1iIi
 if 66 - 66: oOo % ooo0O
 if 21 - 21: iii1i1iiiiIi - ii % Ii
 if 71 - 71: ooOoO0O00 - i1IiiiI1iI * O0Oooo0O + OOOo00oo0oO - oOo % oOoO0o00OO0
 if 63 - 63: iI11I1II1I1I + OoOo0o . oOo / oOo0O0Ooo
 if 84 - 84: ooOoO0O00
 i1iI1 = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 IIiI = requests . get ( 'http://www.djing.com/' ) . content
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( IIiI )
 i1II11II1 = i1iI1 . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for II1IIIii in i1II11II1 :
  iIIIiIi1I1i = II1IIIii . findAll ( 'a' )
  for IIIi1I1IIii1II in iIIIiIi1I1i :
   if IIIi1I1IIii1II . has_attr ( 'href' ) :
    i1IIi1i1Ii1 = 'https://tvcatchup.com' + IIIi1I1IIii1II [ 'href' ]
   OoOOo00 = IIIi1I1IIii1II . findAll ( 'img' )
   for O00 in OoOOo00 :
    Ooo0oOooo0 = O00 [ 'src' ]
    IiIIiii1I = O00 [ 'alt' ]
   iI111i = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( IIIi1I1IIii1II ) )
   for ooooo0Oo0 in iI111i :
    II1i11I1 ( ( '[COLORgold]' + IiIIiii1I + '[/COLOR][COLORwhite] - [COLORsteelblue]' + ooooo0Oo0 + '[/COLOR]' ) , i1IIi1i1Ii1 , 90024 , Ooo0oOooo0 )
    if 97 - 97: I11i1ii1 . OOOo00oo0oO . I11i1ii1
 for iiI , Ooo0oOooo0 , i1I1i111Ii in IIi11i1i1iI1 :
  if 'Submit' in i1I1i111Ii :
   pass
  elif '&lt;' in i1I1i111Ii :
   pass
  else :
   O0O0ooOOO ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + i1I1i111Ii + '[/COLOR]' , iiI , 90025 , 'http://www.djing.com' + Ooo0oOooo0 , Oo00OOOOO , '' )
   if 91 - 91: OoOo0o + O0Oooo0O . i1IiiiI1iI
 O00oO000O0O ( 'movies' , 'MAIN' )
def i1I111i1ii ( url ) :
 oOOo0 = i11111IIIII ( url )
 if 81 - 81: I1ii11iIi11i - i1IiiiI1iI
 iI111i = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( html )
 for ii1iII1iI111 in iI111i :
  if not 'text' in ii1iII1iI111 :
   o0o0O0O000 = o0oOoO00o ( o0oOoO00o ( ii1iII1iI111 ) )
   IIIIiii1IIii ( o0o0O0O000 )
def I1I1i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<iframe src='([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  O0O0oo ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 83 - 83: I11i1ii1 / O0Oooo0O
def OOo000OO000 ( ) :
 oOOo0 = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 OOOO00OooO = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for OOOiI1 , O00oO0o000oO , I1i11II11i1iI in OOOO00OooO :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + OOOiI1 + O00oO0o000oO + I1i11II11i1iI + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + iiI , 10201 , I1IIIii + 'rated.png' )
 for iiI , i1I1i111Ii in iI111i :
  if 'yr' in iiI :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + iiI , 10201 , I1IIIii + 'rated.png' )
   if 43 - 43: I1ii11iIi11i . O0Oooo0O
def o0oOOoOOO ( ) :
 if 12 - 12: O0Oooo0O + OoOo0o + i1IiiiI1iI . I11i1ii1 / i1iIi
 if 29 - 29: I11i1ii1 . oOOoOooOo - IIiIiII11i
 if 68 - 68: iI11I1II1I1I + IIiIiII11i / OOOo00oo0oO
 if 91 - 91: iii1i1iiiiIi % iI11I1II1I1I . oOo0O0Ooo
 if 70 - 70: i1IiiiI1iI % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / O0Oooo0O
 if 100 - 100: oOoO0o00OO0 * Ii % OOOo00oo0oO / I1ii11iIi11i / oOOoOooOo + oOoO0o00OO0
 oOOo0 = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if 'yr' in iiI :
   O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + iiI , 10201 , I1IIIii + 'rated.png' , '' , i1I1i111Ii , '' )
   if 59 - 59: O0Oooo0O - I11i1ii1
def iiiii111 ( name , url , description ) :
 O0oOOo0o = description
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
 for oO0oo0o00o0O , url , name in iI111i :
  if 'id' in url :
   oooI11iI1I = name
   O0OOoOOO0oO ( ( '[COLORred]RANK [COLORblue]' + oO0oo0o00o0O + '[COLORred] - [COLORblue]' + name + '[/COLOR]' ) , name , 9110005 , I1IIIii + 'rated.png' , '' , O0oOOo0o , oooI11iI1I )
   if 50 - 50: iI11I1II1I1I * I11i1ii1 . ii / IIiIiII11i - oOoO0o00OO0 * oOoO0o00OO0
   if 98 - 98: oOo - i1iIi . I11i1ii1 % Ii
def OO00oo ( description , url ) :
 if 84 - 84: oOOoOooOo + Ii - OoOo0o * oOOoOooOo
 oOOOOOoOO = ( str ( description ) )
 o0OO0Oo = ( str ( url ) )
 xbmc . log ( 'title:' + o0OO0Oo + '# year:' + oOOOOOoOO , xbmc . LOGNOTICE )
 from imports import Scrape_Nan
 Scrape_Nan . scrape_movie ( o0OO0Oo , oOOOOOoOO , '' )
 if 33 - 33: oOOoOooOo % ooOoO0O00 - OOOo00oo0oO . o0o00Oo0O / o0o00Oo0O
 if 96 - 96: ii + I11i1ii1 * o0o00Oo0O
 if 86 - 86: i1iIi
 if 29 - 29: iI11I1II1I1I - oOo + oOo0O0Ooo % iI11I1II1I1I % OoOo0o
 if 84 - 84: I11i1ii1 + oOoO0o00OO0 + i1iIi + iiiiiiii1
 if 62 - 62: Ii + iii1i1iiiiIi + ooOoO0O00
 if 69 - 69: iii1i1iiiiIi
def OO0Oo ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 IIiiiiiIiIIi = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0ooOO = ( url )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 I1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iiIiiIi1 = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 I1Ii11i = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 I1iIiiiI1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OOO0O00Oo = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ii1oOOO0ooOO = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + O0ooOO
 i11IiI1iiI11 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OOoOOOO00 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 49 - 49: oOo - o0o00Oo0O / oOo * iii1i1iiiiIi + O0Oooo0O
 Iiii1I = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ooo000000 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 80 - 80: IIiIiII11i - OoOo0o % ii . iI11I1II1I1I - oOOoOooOo + oOo0O0Ooo
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oOOo0 = i1Oo00 ( url )
 o0oO0 . update ( 0 , "" , "Checking Source 1/9 Links" )
 oo00O00oO = i1Oo00 ( I1 )
 o0oO0 . update ( 14 , "" , "Checking Source 2/9 Links" )
 iIiIIIi = i1Oo00 ( iiIiiIi1 )
 o0oO0 . update ( 28 , "" , "Checking Source 3/9 Links" )
 ooo00OOOooO = i1Oo00 ( I1Ii11i )
 o0oO0 . update ( 40 , "" , "Checking Source 4/9 Links" )
 i1i1iiIIiiiII = i1Oo00 ( I1iIiiiI1 )
 o0oO0 . update ( 52 , "" , "Checking Source 5/9 Links" )
 Ii1I1 = i1Oo00 ( ii1oOOO0ooOO )
 o0oO0 . update ( 64 , "" , "Checking Source 6/9 Links" )
 OO0ooO0 = i1Oo00 ( i11IiI1iiI11 )
 o0oO0 . update ( 76 , "" , "Checking Source 7/9 Links" )
 OoOooOO0oOOo0O = i1Oo00 ( OOoOOOO00 )
 o0oO0 . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 42 - 42: iiiiiiii1 / ooo0O + I1ii11iIi11i . I1ii11iIi11i % OoOo0o
 if 16 - 16: ooOoO0O00 + oOo % iii1i1iiiiIi + i1iIi * I1ii11iIi11i
 i1o0oo0 = i1Oo00 ( Iiii1I )
 o0oO0 . update ( 100 , "" , "Checking Source 9/9 Links" )
 OoO0OOoO0Oo0 = i1Oo00 ( Ooo000000 )
 if 91 - 91: IIiIiII11i
 if 53 - 53: oOo % ooo0O / OoOo0o % I11i1ii1 % oOo % ii
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
 if OoOooOO0oOOo0O != 'Failed' :
  oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOooOO0oOOo0O )
  for url , i1I1i111Ii in oO00 :
   IIiIiiI1i = i1Oo00 ( url )
   IIiO0Oo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIiIiiI1i )
   for III11I1 , ooo in IIiO0Oo :
    ooo = ( ooo . replace ( '.' , ' ' ) )
    if i1oOOOOOOOoO in ooo . lower ( ) :
     if '.mkv' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , url + III11I1 , 222 , '' , '' , '' )
     elif '.mp4' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , url + III11I1 , 222 , '' , '' , '' )
     elif '.avi' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , url + III11I1 , 222 , '' , '' , '' )
     elif '.wav' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']*' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , url + III11I1 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , url + III11I1 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
      if 61 - 61: iii1i1iiiiIi - oOo + oOo0O0Ooo * OoOo0o % oOo
      O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in IIi11i1i1iI1 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 24 - 24: oOOoOooOo - i1IiiiI1iI * OOOo00oo0oO
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 87 - 87: i1iIi - oOoO0o00OO0 % oOoO0o00OO0 . OOOo00oo0oO / oOoO0o00OO0
 if iIiIIIi != 'Failed' :
  OOoOOO000O0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for II1io0 , i1I1i111Ii in OOoOOO000O0 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiIiiIi1 + II1io0 ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Source 3 Links" )
 if ooo00OOOooO != 'Failed' :
  IiIIiii11II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in IiIIiii11II1 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 25 - 25: oOo * OOOo00oo0oO % Ii + Ii * oOo
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if i1i1iiIIiiiII != 'Failed' :
  Iiiii = [ ]
  iiii1i1II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i1iiIIiiiII )
  for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in iiii1i1II1 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    if i1I1i111Ii in Iiiii :
     pass
    else :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , i1I , oOoOo0OOOOO , ooo0O0o00O )
     Iiiii . append ( i1I1i111Ii )
     o0oO0 . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 36 , "" , "Getting Scooby Links" )
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if Ii1I1 != 'Failed' :
  iiIIiiIi = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Ii1I1 )
  for url , Ooo0oOooo0 , i1I1i111Ii in iiIIiiIi :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , Ooo0oOooo0 )
    o0oO0 . update ( 45 , "" , "Getting Snag Links" )
    if 42 - 42: iiiiiiii1 + iI11I1II1I1I
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: iii1i1iiiiIi - I1ii11iIi11i % o0o00Oo0O . oOo + iii1i1iiiiIi
    if 41 - 41: IIiIiII11i * oOOoOooOo
    if 68 - 68: i1iIi - oOo0O0Ooo
    if 41 - 41: OOOo00oo0oO
    if 21 - 21: oOOoOooOo + ooo0O % O0Oooo0O + Ii + iiiiiiii1 + IIiIiII11i
    if 98 - 98: O0Oooo0O
    if 49 - 49: I1ii11iIi11i * OOOo00oo0oO + ooo0O - Ii
    if 74 - 74: I1ii11iIi11i / iI11I1II1I1I . IIiIiII11i - oOo
    if 62 - 62: OoOo0o / IIiIiII11i + iii1i1iiiiIi % oOOoOooOo / iii1i1iiiiIi + oOoO0o00OO0
    if 2 - 2: Ii - O0Oooo0O + oOo % i1IiiiI1iI * i1iIi
    if 54 - 54: o0o00Oo0O - iiiiiiii1 . OoOo0o % iiiiiiii1 + iiiiiiii1
    if 36 - 36: OoOo0o % Ii
    if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * OOOo00oo0oO . i1IiiiI1iI / ooOoO0O00
    if 50 - 50: O0Oooo0O / ooOoO0O00 % ii
    if 83 - 83: oOoO0o00OO0 * oOoO0o00OO0 + OoOo0o
    if 57 - 57: o0o00Oo0O - o0o00Oo0O . oOoO0o00OO0 / ooo0O / i1iIi
    if 20 - 20: OoOo0o * IIiIiII11i - iii1i1iiiiIi - OOOo00oo0oO * O0Oooo0O
    if 6 - 6: oOOoOooOo + OoOo0o / I1ii11iIi11i + I11i1ii1 % IIiIiII11i / oOo
 if i1o0oo0 != 'Failed' :
  iiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1o0oo0 )
  for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in iiIi :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Herovision Links" )
    if 74 - 74: o0o00Oo0O + ii / OOOo00oo0oO / iii1i1iiiiIi . oOoO0o00OO0 % OOOo00oo0oO
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
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
 for ii1o0oo0Ooooo0 in Ooo00O0 :
  Oo0oOo000OoO0 = Ii1iIiII1ii1 + ii1o0oo0Ooooo0 + OOOO
  OoOooOO0oOOo0O = i1Oo00 ( Oo0oOo000OoO0 )
  if OoOooOO0oOOo0O != 'Failed' :
   oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOooOO0oOOo0O )
   for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in oO00 :
    if O0ooOO in i1I1i111Ii . lower ( ) :
     O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
     if 1 - 1: OOOo00oo0oO / ooOoO0O00
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
     if 74 - 74: i1IiiiI1iI / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
 Ooo00O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 59 - 59: Ii . ii / i1IiiiI1iI * oOoO0o00OO0 + ii
 if 3 - 3: Ii * I1ii11iIi11i % iI11I1II1I1I % oOo0O0Ooo * iiiiiiii1 / OoOo0o
 for ii1o0oo0Ooooo0 in Ooo00O0 :
  Oo0oOo000OoO0 = IIiiiiiIiIIi + ii1o0oo0Ooooo0
  O00oo00oOOO0o = i1Oo00 ( Oo0oOo000OoO0 )
  if O00oo00oOOO0o != 'Failed' :
   II1iI111iiIIiI1I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O00oo00oOOO0o )
   for II1io0 , i1I1i111Ii in II1iI111iiIIiI1I :
    if O0ooOO in i1I1i111Ii . lower ( ) :
     II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IIiiiiiIiIIi + ii1o0oo0Ooooo0 + II1io0 ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 51 - 51: oOo0O0Ooo + OoOo0o + i1IiiiI1iI
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: O0Oooo0O + oOoO0o00OO0
def IIi ( ) :
 oOo0 ( 'RUNNING' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , I1IIIii + 'running.png' )
 oOo0 ( 'COUNTDOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , I1IIIii + 'countdown.png' )
 oOo0 ( 'UNKNOWN' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , I1IIIii + 'unknown.png' )
 oOo0 ( 'CANCELLED' , o0oOoO00o ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , I1IIIii + 'cancelled.png' )
 O00oO000O0O ( 'tvshows' , 'INFO' )
 if 4 - 4: I11i1ii1 / I1ii11iIi11i
def I1IIiiII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , Oo , oOOO0oOoo , oO0Ooo0OooOOo , o0O0ooooooo00 in iI111i :
  oOo0 ( ( '[COLORblue]' + i1I1i111Ii + '[/COLOR] [COLORred]Season[/COLOR]-' + Oo + ' [COLORred]Returns [/COLOR]- ' + o0O0ooooooo00 + ' ' + oO0Ooo0OooOOo ) , i1I1i111Ii , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 28 - 28: oOOoOooOo * i1IiiiI1iI % Ii * iiiiiiii1 / i1iIi
def iIII1iIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , Oo , oOOO0oOoo in iI111i :
  oOo0 ( ( '[COLORblue]' + i1I1i111Ii + '[/COLOR] [COLORred]Season[/COLOR]-' + Oo + ' [COLORred] Status Unknown[/COLOR] ' ) , i1I1i111Ii , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 75 - 75: i1iIi - i1IiiiI1iI % iii1i1iiiiIi
def o00oIIi1i1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , Oo , oOOO0oOoo , oO0Ooo0OooOOo in iI111i :
  oOo0 ( ( '[COLORblue]' + i1I1i111Ii + ' [COLORred] Cancelled On[/COLOR] ' + oO0Ooo0OooOOo ) , i1I1i111Ii , 10099 , I1IIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 84 - 84: OoOo0o + i1iIi + ooo0O
def i1i1iIII11i ( url ) :
 O0ooOO = ( url )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 if 40 - 40: iI11I1II1I1I / iii1i1iiiiIi - o0o00Oo0O * iI11I1II1I1I
 if 56 - 56: OoOo0o
 III11I1 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( O0ooOO ) . replace ( ' ' , '+' )
 I1 = 'http://onlinemovies.tube/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 iiIiiIi1 = ( o0oOoO00o ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 I1Ii11i = ( o0oOoO00o ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 OOO0O00Oo = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 49 - 49: oOOoOooOo . IIiIiII11i
 i11IiI1iiI11 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 OOoOOOO00 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 IioOooOOo00ooO = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 71 - 71: O0Oooo0O - ooo0O - OoOo0o
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 28 - 28: iI11I1II1I1I
 o0oO0 . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 7 - 7: ooo0O % I11i1ii1 * iii1i1iiiiIi
 if 58 - 58: I11i1ii1 / i1IiiiI1iI + IIiIiII11i % iiiiiiii1 - ii
 II1iII1i1i = i1Oo00 ( III11I1 )
 o0oO0 . update ( 14 , "" , "Checking Source 3/11 Links" )
 oo00O00oO = i1Oo00 ( I1 )
 o0oO0 . update ( 28 , "" , "Checking Source 4/11 Links" )
 iIiIIIi = i1Oo00 ( iiIiiIi1 )
 o0oO0 . update ( 40 , "" , "Checking Source 5/11 Links" )
 ooo00OOOooO = i1Oo00 ( I1Ii11i )
 o0oO0 . update ( 52 , "" , "Checking Source 6/11 Links" )
 O00oo00oOOO0o = i1Oo00 ( OOO0O00Oo )
 o0oO0 . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 63 - 63: OoOo0o * i1IiiiI1iI
 if 22 - 22: oOoO0o00OO0 * o0o00Oo0O * iI11I1II1I1I
 OO0ooO0 = i1Oo00 ( i11IiI1iiI11 )
 o0oO0 . update ( 95 , "" , "Checking Source 9/11 Links" )
 OoOooOO0oOOo0O = i1Oo00 ( OOoOOOO00 )
 o0oO0 . update ( 97 , "" , "Checking Source 10/11 Links" )
 ooOOo00 = i1Oo00 ( IioOooOOo00ooO )
 o0oO0 . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 39 - 39: I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * iii1i1iiiiIi % o0o00Oo0O
 if OoOooOO0oOOo0O != 'Failed' :
  oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOooOO0oOOo0O )
  for url , i1I1i111Ii in oO00 :
   IIiIiiI1i = i1Oo00 ( url )
   IIiO0Oo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIiIiiI1i )
   for III11I1 , ooo in IIiO0Oo :
    if i1oOOOOOOOoO in ooo . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , url + III11I1 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 55 - 55: iI11I1II1I1I * iiiiiiii1
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if OO0ooO0 != 'Failed' :
  ooIi11iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0ooO0 )
  for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in ooIi11iI :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 10 , "" , "Getting Herovision Links" )
    if 22 - 22: OoOo0o
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 22 - 22: iiiiiiii1 * i1IiiiI1iI - I1ii11iIi11i * o0o00Oo0O / Ii
    if 78 - 78: I1ii11iIi11i * o0o00Oo0O / oOOoOooOo + ii + OoOo0o
    if 23 - 23: iiiiiiii1 % ii / iI11I1II1I1I + oOoO0o00OO0 / ooOoO0O00 / ooo0O
    if 94 - 94: ooOoO0O00
    if 36 - 36: oOo0O0Ooo + I1ii11iIi11i
    if 46 - 46: iiiiiiii1
    if 65 - 65: ooOoO0O00 . oOoO0o00OO0 / oOOoOooOo
    if 11 - 11: I11i1ii1 * oOOoOooOo / oOOoOooOo - OoOo0o
    if 68 - 68: oOo0O0Ooo % I11i1ii1 - I11i1ii1 / oOo0O0Ooo + oOoO0o00OO0 - I1ii11iIi11i
    if 65 - 65: oOOoOooOo - ooOoO0O00
    if 62 - 62: i1IiiiI1iI / OOOo00oo0oO % I1ii11iIi11i . ii / Ii / O0Oooo0O
 if ooOOo00 != 'Failed' :
  OooO0O0Ooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOOo00 )
  for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in OooO0O0Ooo :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    oOo0 ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , i1I )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 30 , "" , "Getting RaizTv Links" )
    if 85 - 85: ooo0O / O0Oooo0O
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  o0OOoOo0oo = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for url , Ooo0oOooo0 , i1I1i111Ii , ooO0 in IIi11i1i1iI1 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    if 'season' in ooO0 :
     oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
    if 'episodes' in ooO0 :
     oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
  for url in o0OOoOo0oo :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 94 - 94: i1IiiiI1iI . oOo0O0Ooo
   O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if II1iII1i1i != 'Failed' :
  I1iii11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( II1iII1i1i )
  for url , i1I1i111Ii , Ooo0oOooo0 in I1iii11 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( i1I1i111Ii ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , Ooo0oOooo0 , '' , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 45 , "" , "Getting Source iWatch Links" )
    if 73 - 73: ooOoO0O00 / IIiIiII11i
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: i1iIi / oOOoOooOo . ii + oOo
    if 51 - 51: iiiiiiii1 % Ii % I11i1ii1 + O0Oooo0O % oOoO0o00OO0
    if 16 - 16: iii1i1iiiiIi / I1ii11iIi11i + o0o00Oo0O - iii1i1iiiiIi . ii
    if 19 - 19: ooo0O
    if 73 - 73: O0Oooo0O * I1ii11iIi11i * iii1i1iiiiIi
    if 65 - 65: Ii + I1ii11iIi11i * ii - oOo
    if 26 - 26: ooo0O % OoOo0o + OoOo0o % i1IiiiI1iI * Ii / iiiiiiii1
    if 64 - 64: OOOo00oo0oO % iii1i1iiiiIi / IIiIiII11i % oOOoOooOo - iiiiiiii1
    if 2 - 2: O0Oooo0O - oOoO0o00OO0 + ooo0O * oOo / iiiiiiii1
 if iIiIIIi != 'Failed' :
  OOoOOO000O0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for i1I1i111Ii in OOoOOO000O0 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iiIiiIi1 + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 26 - 26: OoOo0o * I1ii11iIi11i
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  IiIIiii11II1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for i1I1i111Ii in IiIIiii11II1 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( I1Ii11i + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 31 - 31: i1IiiiI1iI * OOOo00oo0oO . i1iIi
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if O00oo00oOOO0o != 'Failed' :
  II1iI111iiIIiI1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oo00oOOO0o )
  for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in II1iI111iiIIiI1I :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 90 , "" , "Getting Scooby Links" )
    if 35 - 35: i1IiiiI1iI
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 94 - 94: oOOoOooOo / Ii % o0o00Oo0O
 O0oO0oo0O = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for ii1o0oo0Ooooo0 in O0oO0oo0O :
  Oo0oOo000OoO0 = Ii1iIiII1ii1 + ii1o0oo0Ooooo0 + OOOO
  i1o0oo0 = i1Oo00 ( Oo0oOo000OoO0 )
  if i1o0oo0 != 'Failed' :
   iiIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1o0oo0 )
   for i1I1i111Ii , ooo0O0o00O , url , Ooo0oOooo0 , oo0o0000 , I11iiii1I in iiIi :
    if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
     o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgold] - Source Pandoras[/COLOR]' , url , I11iiii1I , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
     if 82 - 82: ii . i1iIi
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
     if 26 - 26: OOOo00oo0oO + I11i1ii1 - IIiIiII11i . IIiIiII11i + oOoO0o00OO0 + iii1i1iiiiIi
     if 68 - 68: o0o00Oo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 76 - 76: oOoO0o00OO0
def ooO000OO ( ) :
 OoO = [ '[COLOR' + iiI1IiI + ']Adult Gallery[/COLOR]' , '[COLOR' + iiI1IiI + ']JizBox[/COLOR]' , '[COLOR' + iiI1IiI + ']Adult Channels[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  i111IIiIiiI1 ( )
 if iiI1IIIi == 1 :
  OO0IIIIIIi111i ( )
 if iiI1IIIi == 2 :
  iiIIIIiI111 ( )
  if 86 - 86: IIiIiII11i % iI11I1II1I1I / oOoO0o00OO0 - ooo0O * i1iIi . oOo0O0Ooo
  if 68 - 68: ii * iI11I1II1I1I + ooOoO0O00 - ooOoO0O00
  if 76 - 76: oOo . ii % O0Oooo0O * i1iIi
def i111IIiIiiI1 ( ) :
 OoO = [ '[COLOR' + iiI1IiI + ']YOLOselfies[/COLOR]' , '[COLOR' + iiI1IiI + ']HotNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']MyNudeBabes[/COLOR]' , '[COLOR' + iiI1IiI + ']TeenNudeGirls[/COLOR]' , '[COLOR' + iiI1IiI + ']ADULTmeme[/COLOR]' , '[COLOR' + iiI1IiI + ']GIRLSmeme[/COLOR]' , ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  i1iiI1i ( 'http://www.yoloselfie.com/' )
 if iiI1IIIi == 1 :
  O0OOO00OOO00o ( 'http://www.hotnudegirls.net/#nudegirls' )
 if iiI1IIIi == 2 :
  i11o00Ooo ( 'http://www.teennudegirls.com/' )
 if iiI1IIIi == 3 :
  i11o00Ooo ( 'http://www.teennudegirls.com/' )
 if iiI1IIIi == 4 :
  OoO00OOoOOOo0 ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if iiI1IIIi == 5 :
  OoO00OOoOOOo0 ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 84 - 84: OOOo00oo0oO + OoOo0o . iiiiiiii1
def i1iiI1i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 100111 , Ooo0oOooo0 )
 for url in IIi11i1i1iI1 :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 100110 , Ooo0oOooo0 )
def O0o00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( oOOo0 )
 for url in iI111i :
  I1I1i1i = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( I1I1i1i )
  sys . exit ( 1 )
def OoO00OOoOOOo0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , Ooo0oOooo0 in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + Ooo0oOooo0 , 100113 , 'http:' + Ooo0oOooo0 )
 for url in IIi11i1i1iI1 :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http:' + url , 100112 , Ooo0oOooo0 )
def O0OOO00OOO00o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , Ooo0oOooo0 )
def Oo0oOO0O00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , Ooo0oOooo0 , 100113 , Ooo0oOooo0 )
def o00OOo0o0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , Ooo0oOooo0 )
def I111Iii1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , Ooo0oOooo0 , 100113 , Ooo0oOooo0 )
def i11o00Ooo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , Ooo0oOooo0 )
def i11i ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']Click To Enlarge[/COLOR]' , Ooo0oOooo0 , 100113 , Ooo0oOooo0 )
def O0o0O00o0o ( url ) :
 I1I1i1i = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( I1I1i1i )
 sys . exit ( 1 )
 if 6 - 6: oOoO0o00OO0 - OOOo00oo0oO * Ii + iii1i1iiiiIi / oOOoOooOo % OoOo0o
def II11IiIIiiI ( ) :
 if 67 - 67: oOoO0o00OO0 . IIiIiII11i - i1iIi % ii
 if 49 - 49: oOoO0o00OO0 + o0o00Oo0O . i1iIi * ii
 if 82 - 82: oOoO0o00OO0
 if 54 - 54: ooo0O + i1IiiiI1iI - iI11I1II1I1I % oOOoOooOo % I11i1ii1
 if 19 - 19: oOoO0o00OO0 / iI11I1II1I1I % ooOoO0O00 . ii
 if 57 - 57: oOOoOooOo . I1ii11iIi11i - oOo - Ii * O0Oooo0O / ooo0O
 if 79 - 79: oOoO0o00OO0 + ooo0O % I1ii11iIi11i * ooo0O
 if 21 - 21: iiiiiiii1
 if 24 - 24: iiiiiiii1 / oOOoOooOo
 if 61 - 61: iI11I1II1I1I + OOOo00oo0oO
 if 8 - 8: O0Oooo0O + oOo
 oOo0 ( 'SEASONS' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , I1IIIii + 'seasons.png' )
 oOo0 ( 'EPISODES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , I1IIIii + 'episodes.png' )
 oOo0 ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , I1IIIii + 'Search.png' )
 O00oO000O0O ( 'tvshows' , 'INFO' )
 if 9 - 9: OoOo0o + ooo0O
def I1iII1IIi1IiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii , iIioo0ooO in iI111i :
  oOo0 ( ( i1I1i111Ii + ' - ' + iIioo0ooO ) . replace ( '&amp;' , '&' ) , url , 90053 , I1IIIii + 'seasons.png' )
  if 97 - 97: O0Oooo0O . i1IiiiI1iI / oOo0O0Ooo
def o00OO0o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , url , 90054 , I1IIIii + 'episodes.png' )
  if 39 - 39: oOOoOooOo % oOoO0o00OO0 - iiiiiiii1
def iIi1i111 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for Ooo0oOooo0 , i1I1i111Ii , url in iI111i :
  oOo0 ( i1I1i111Ii , url , 90054 , Ooo0oOooo0 )
 for url in next :
  oOo0 ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 25 - 25: ii % i1iIi * IIiIiII11i - oOo
def Oo00Oooo00o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for Ooo0oOooo0 , iIioo0ooO , url , i1I1i111Ii , II11II1I in iI111i :
  o00oOOooOOo0o ( iIioo0ooO + ' - ' + i1I1i111Ii + ' - ' + II11II1I , url , 90044 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
 for Ooo0oOooo0 , i1I1i111Ii , url in IIi11i1i1iI1 :
  oOo0 ( i1I1i111Ii , url , 90044 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
 for url in next :
  oOo0 ( 'NEXT' , url , 90053 , I1IIIii + 'Next.png' )
  if 52 - 52: OoOo0o * OOOo00oo0oO + i1IiiiI1iI * i1IiiiI1iI % ooOoO0O00 % i1IiiiI1iI
def OOOO000Ooo0O ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'http://onlinemovies.tube/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 i1oOOOOOOOoO = OooooOoO . lower ( )
 oOOo0 = i11111IIIII ( i1oOOOOOOOoO )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii , ooO0 in iI111i :
  if 'season' in ooO0 :
   oOo0 ( i1I1i111Ii , iiI , 90054 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
  if 'episodes' in ooO0 :
   oOo0 ( i1I1i111Ii , iiI , 90044 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
 for iiI in next :
  oOo0 ( 'NEXT' , iiI , 90053 , I1IIIii + 'Next.png' )
  if 96 - 96: I1ii11iIi11i + O0Oooo0O . ooOoO0O00
def OooIii1I1iI ( ) :
 if 62 - 62: OOOo00oo0oO + I1ii11iIi11i / Ii
 if 90 - 90: iI11I1II1I1I + iii1i1iiiiIi
 if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
 if 30 - 30: iiiiiiii1 / oOo . iiiiiiii1
 if 17 - 17: I1ii11iIi11i + ii * ii
 if 5 - 5: O0Oooo0O % ii . iii1i1iiiiIi
 if 67 - 67: oOoO0o00OO0 + i1iIi
 if 72 - 72: I11i1ii1 % ooo0O
 if 93 - 93: iI11I1II1I1I + Ii . ooo0O . ooOoO0O00 % oOo0O0Ooo % oOOoOooOo
 if 74 - 74: iii1i1iiiiIi / ooOoO0O00 % ii
 oOo0 ( 'ALL MOVIES' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , I1IIIii + 'allmov.png' )
 oOo0 ( 'GENRE' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , I1IIIii + 'Genre.png' )
 oOo0 ( 'BY YEAR' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , I1IIIii + 'Years.png' )
 oOo0 ( 'SEARCH' , o0oOoO00o ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , I1IIIii + 'Search.png' )
 O00oO000O0O ( 'tvshows' , 'INFO' )
 if 52 - 52: I11i1ii1 % oOOoOooOo
def I111 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii , iIioo0ooO in iI111i :
  if 'genre' in url :
   oOo0 ( ( i1I1i111Ii + ' - ' + iIioo0ooO ) . replace ( '&amp;' , '&' ) , url , 90043 , I1IIIii + 'Genre.png' )
   if 51 - 51: oOoO0o00OO0 * OOOo00oo0oO
def i1oooOoOoOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  if 'release' in url :
   oOo0 ( i1I1i111Ii , url , 90043 , I1IIIii + 'Years.png' )
   if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
def iiI1ii1Iii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oOOo0 )
 for Ooo0oOooo0 , i1I1i111Ii , Ii1I1IIIiI1i , url , ooo0O0o00O in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii + ' ' + Ii1I1IIIiI1i , url , 90044 , Ooo0oOooo0 , Ooo0oOooo0 , ooo0O0o00O )
 for Ooo0oOooo0 , i1I1i111Ii , ooO0 , url , o0Oo00oOO , ooo0O0o00O in IIi11i1i1iI1 :
  if 'movies' in ooO0 :
   o00oOOooOOo0o ( i1I1i111Ii + ' - ' + o0Oo00oOO , url , 90044 , Ooo0oOooo0 , Ooo0oOooo0 , ooo0O0o00O )
 for url in next :
  oOo0 ( 'NEXT' , url , 90043 , I1IIIii + 'Next.png' )
  if 73 - 73: i1IiiiI1iI / ii . IIiIiII11i - I11i1ii1 * oOOoOooOo * I11i1ii1
def IiI1IiI1iiI1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  O000o0 ( 'http:' + url )
  if 39 - 39: IIiIiII11i + ii / OoOo0o / i1iIi * iii1i1iiiiIi
def O000o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( ( i1I1i111Ii ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , I1IIIii + 'movhub.png' )
def Oo0Oo ( ) :
 if 5 - 5: iI11I1II1I1I . I11i1ii1
 if 93 - 93: OOOo00oo0oO % ooOoO0O00
 if 83 - 83: oOo0O0Ooo . I1ii11iIi11i - i1IiiiI1iI . ooo0O
 if 73 - 73: oOo0O0Ooo - iiiiiiii1 . iiiiiiii1
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
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'http://onlinemovies.tube/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 i1oOOOOOOOoO = OooooOoO . lower ( )
 oOOo0 = i11111IIIII ( i1oOOOOOOOoO )
 iI111i = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii , iIio0oooo0OOo00 in iI111i :
  if 'movies' in iIio0oooo0OOo00 :
   oOo0 ( iIio0oooo0OOo00 + '-' + i1I1i111Ii , iiI , 90044 , Ooo0oOooo0 )
 for iiI in next :
  iiI1ii1Iii ( iiI )
  if 90 - 90: ooo0O / OoOo0o - OoOo0o . oOo0O0Ooo
def iiI1i11II ( ) :
 oOo0 ( 'Search' , '' , 80008 , I1IIIii + 'Search.png' )
 oOOo0 = i11111IIIII ( 'http://www.join4films.com/' )
 iI111i = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , iiI , 80006 , I1IIIii + 'Desi.png' )
def o0OOoo0oOoO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oOOo0 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  II1i11I1 ( i1I1i111Ii , url , 80007 , Ooo0oOooo0 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  oOo0 ( 'Next' , url , 80006 , I1IIIii + 'Next.png' )
def i1ii1iIi ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  url = ( url ) . replace ( ' ' , '%20' )
  IIIIiii1IIii ( url )
def I1I1Ii ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'http://www.join4films.com/?s=' + ( O0ooOO ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1oOOOOOOOoO = OooooOoO . lower ( )
 o0OOoo0oOoO00 ( i1oOOOOOOOoO )
 if 42 - 42: ooo0O - I1ii11iIi11i % oOoO0o00OO0
 if 43 - 43: i1IiiiI1iI % ooOoO0O00 % oOOoOooOo . Ii
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
 if 61 - 61: IIiIiII11i . o0o00Oo0O - i1iIi - oOoO0o00OO0 / Ii - IIiIiII11i
 if 98 - 98: i1iIi - oOo0O0Ooo . Ii * I1ii11iIi11i
 if 29 - 29: i1iIi / oOOoOooOo % i1IiiiI1iI
 if 10 - 10: iI11I1II1I1I % ii % oOoO0o00OO0
def IiiI1i111I1i ( ) :
 o00oOOooOOo0o ( 'Genre' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Most Viewed' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Box Office' , o0oOoO00o ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( 'Search' , '' , 10078 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
 if 97 - 97: OoOo0o % oOo0O0Ooo * oOo0O0Ooo % I1ii11iIi11i
def o0OoOooOO0o0 ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'http://imoviemax.se/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 i1oOOOOOOOoO = OooooOoO . lower ( )
 Oooo0ooOoo0 ( i1oOOOOOOOoO )
def i1Iii ( url ) :
 oO00oO00O0Oo = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii , OO0o0o0oo in iI111i :
  if i1I1i111Ii in oO00oO00O0Oo :
   pass
  else :
   o00oOOooOOo0o ( i1I1i111Ii + ' - ' + OO0o0o0oo + ' Films' , url , 10074 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
   oO00oO00O0Oo . append ( i1I1i111Ii )
   if 40 - 40: I1ii11iIi11i
def iI1Ii11 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii + ' - Views:' + Ooo0 , url , 10075 , I1IIIii + 'genievision.png' , Oo00OOOOO , '' )
  if 49 - 49: IIiIiII11i + ii . OOOo00oo0oO + Ii / OOOo00oo0oO
  if 39 - 39: oOo + o0o00Oo0O + oOOoOooOo * IIiIiII11i % o0o00Oo0O - o0o00Oo0O
def Oooo0ooOoo0 ( url ) :
 i1I1i1i1I1 = [ ]
 oOOo0 = i11111IIIII ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oOOo0 )
 for next in next :
  o00oOOooOOo0o ( 'NEXT PAGE' , next , 10074 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , i1I1i111Ii , url in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 10075 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
  i1I1i1i1I1 . append ( i1I1i111Ii )
  if 17 - 17: iii1i1iiiiIi + ii % OoOo0o
def Ii1Ii1 ( img , name , url ) :
 img = img
 name = name
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oOOo0 )
 for o000ooOo0o0OO , url in iI111i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iiI1ii1IIiI = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iiI1ii1IIiI
  IIi1i1I11IIII = ( o000ooOo0o0OO ) . replace ( 'play-' , 'Server ' )
  O0O0ooOOO ( IIi1i1I11IIII , iiI1ii1IIiI , 10076 , img , img , '' )
  if 55 - 55: iI11I1II1I1I % oOo / oOoO0o00OO0 / ooo0O
def IIiI1111iI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oOOo0 )
 for I1 in iI111i :
  if '=m' in I1 :
   o00oOOo ( I1 )
  elif 'php' in I1 :
   IIiI1111iI ( url )
  else :
   oOOo0 = i11111IIIII ( I1 )
   iI111i = re . compile ( 'content="([^"]*)">' ) . findall ( oOOo0 )
   for iiIiiIi1 in iI111i :
    o00oOOo ( I1 )
    if 29 - 29: iii1i1iiiiIi / ii + iii1i1iiiiIi
    if 13 - 13: oOo * i1IiiiI1iI % Ii % ooOoO0O00 + I11i1ii1 / IIiIiII11i
    if 84 - 84: ooOoO0O00 + oOo * ii . iiiiiiii1 + iiiiiiii1
def o0o0oO00OoO0o ( url ) :
 oOOo0 = i11111IIIII ( url )
 Oo0OO00 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for oO0Ooo0OooOOo , o0ooOOOo in Oo0OO00 :
  print 'there ><><><><><><><><><><><><'
  oO0Ooo0OooOOo = oO0Ooo0OooOOo
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0ooOOOo ) )
  for i1I1i111Ii , IiIiIi1I1 in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + oO0Ooo0OooOOo + '[/COLOR] - ' + i1I1i111Ii + ' - [COLOR' + iiI1IiI + ']' + IiIiIi1I1 + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
 ii1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for oO0Ooo0OooOOo , OOoOOo0oO in ii1 :
  print 'there ><><><><><><><><><><><><'
  oO0Ooo0OooOOo = oO0Ooo0OooOOo
  iI111i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOoOOo0oO ) )
  for i1I1i111Ii , IiIiIi1I1 in iI111i :
   print 'here <><><><><><><><><><><><>'
   o00oOOooOOo0o ( '[COLORred]' + oO0Ooo0OooOOo + '[/COLOR] - ' + i1I1i111Ii + ' - [COLOR' + iiI1IiI + ']' + IiIiIi1I1 + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , I1IIIii + 'loader.png' , Oo00OOOOO , '' )
   if 25 - 25: i1iIi % IIiIiII11i - OOOo00oo0oO * oOoO0o00OO0 - iI11I1II1I1I
   if 46 - 46: IIiIiII11i . o0o00Oo0O * I1ii11iIi11i + iiiiiiii1
   if 40 - 40: o0o00Oo0O . o0o00Oo0O * OoOo0o
def i1iiiIIi11II ( url ) :
 oOOo0 = i11111IIIII ( url )
 ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
 for ii1 in ii1 :
  i1I1i111Ii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii1 ) )
  for i1I1i111Ii in i1I1i111Ii :
   i1I1i111Ii = ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  i11I1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii1 ) )
  for i11I1 in i11I1 :
   i11I1 = 'http:' + i11I1
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 , '' , '' )
  if 55 - 55: i1IiiiI1iI
  if 93 - 93: Ii . ooo0O
  if 16 - 16: ooOoO0O00 . ooOoO0O00 / O0Oooo0O % iii1i1iiiiIi / oOo0O0Ooo * oOoO0o00OO0
  if 30 - 30: ooo0O + ii + OoOo0o / IIiIiII11i * I1ii11iIi11i
def II11 ( url ) :
 if 59 - 59: i1iIi / iii1i1iiiiIi * oOo * iiiiiiii1 % OOOo00oo0oO
 oOOoooOO = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oOOo0 )
 for I1 , Ooo0oOooo0 , i1I1i111Ii , I1Iiii1Ii in iI111i :
  i1I1i111Ii = ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  oo00O00oO = i11111IIIII ( I1 )
  IIi11i1i1iI1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( oo00O00oO )
  for iIiiIi11IIi , OoOOOo0 in IIi11i1i1iI1 :
   oooooO00OOO = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OoOOOo0 ) )
   for ooo0O0o00O in oooooO00OOO :
    if i1I1i111Ii in oOOoooOO :
     pass
    else :
     O0O0ooOOO ( i1I1i111Ii , iIiiIi11IIi , 8043 , Ooo0oOooo0 , Ooo0oOooo0 , ooo0O0o00O )
     O00oO000O0O ( 'movies' , 'INFO' )
     oOOoooOO . append ( i1I1i111Ii )
     if 53 - 53: IIiIiII11i
     if 61 - 61: o0o00Oo0O * oOo * oOo0O0Ooo % ii / iii1i1iiiiIi % oOOoOooOo
def iiII ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
 for url , i1I , ooo0O0o00O , oo0o0000 , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 10065 , i1I , oo0o0000 , ooo0O0o00O )
 O00oO000O0O ( 'movies' , 'INFO' )
 if 29 - 29: oOOoOooOo * IIiIiII11i * oOo * I11i1ii1
def ooo00o0OO ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'https://www.youtube.com/results?search_query=' + ( O0ooOO ) . replace ( ' ' , '+' )
 i1oOOOOOOOoO = OooooOoO . lower ( )
 oOOo0 = i11111IIIII ( i1oOOOOOOOoO )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for iiI in next :
  iiI = 'https://www.youtube.com' + iiI
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , iiI , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for Ooo0oOooo0 , iiI , i1I1i111Ii , I1I11i , OoOOOo0 in iI111i :
  iiiiiIIii . append ( i1I1i111Ii )
  O00oO000O0O ( 'tvshows' , 'INFO' )
  i11I1 = 'http:' + ( Ooo0oOooo0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i11I1
  iiI = 'http://www.youtube.com' + iiI
  O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( iiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 , i11I1 , OoOOOo0 )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for Ooo0oOooo0 , iiI , i1I1i111Ii , I1I11i in iI111i :
   print 'im doing it'
   O00oO000O0O ( 'tvshows' , 'INFO' )
   i11I1 = 'http:' + ( Ooo0oOooo0 ) . replace ( 'https:' , '' )
   iiI = 'http://www.youtube.com' + iiI
   if '&' in iiI :
    print ' i got here'
    oOOo0 = i11111IIIII ( iiI )
    ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for ii1 in ii1 :
     i1I1i111Ii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii1 ) )
     for i1I1i111Ii in i1I1i111Ii :
      i1I1i111Ii = ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iiI = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1 ) )
     for iiI in iiI :
      iiI = 'https://www.youtube.com/w' + iiI
     i11I1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii1 ) )
     for i11I1 in i11I1 :
      i11I1 = 'http:' + i11I1
     O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( iiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 , Oo00OOOOO , '' )
   elif i1I1i111Ii in iiiiiIIii :
    pass
   elif 'user' in iiI or 'elete' in i1I1i111Ii :
    pass
   elif 'hannel' in iiI :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iiI
    oOOo0 = i11111IIIII ( iiI )
    Iii1Iii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for Ooo0oOooo0 , iiI , i1I1i111Ii in Iii1Iii :
     if 'outube' in iiI or 'list' in iiI :
      pass
     elif 'atch' in iiI :
      iiI = ( iiI ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( iiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + Ooo0oOooo0 , 'http:' + Ooo0oOooo0 , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( iiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 , i11I1 , '' )
    if 91 - 91: oOOoOooOo * I11i1ii1 * IIiIiII11i
def oooO0oooOo000 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOo0 )
 for url in next :
  url = 'https://www.youtube.com' + url
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 for Ooo0oOooo0 , url , i1I1i111Ii , I1I11i , OoOOOo0 in iI111i :
  iiiiiIIii . append ( i1I1i111Ii )
  O00oO000O0O ( 'tvshows' , 'INFO' )
  i11I1 = 'http:' + ( Ooo0oOooo0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i11I1
  url = 'http://www.youtube.com' + url
  O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 , i11I1 , OoOOOo0 )
 else :
  iI111i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
  for Ooo0oOooo0 , url , i1I1i111Ii , I1I11i in iI111i :
   O00oO000O0O ( 'tvshows' , 'INFO' )
   i11I1 = 'http:' + ( Ooo0oOooo0 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oOOo0 = i11111IIIII ( url )
    ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOo0 )
    for ii1 in ii1 :
     i1I1i111Ii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii1 ) )
     for i1I1i111Ii in i1I1i111Ii :
      i1I1i111Ii = ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     i11I1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii1 ) )
     for i11I1 in i11I1 :
      i11I1 = 'http:' + i11I1
     O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 , Oo00OOOOO , '' )
   elif i1I1i111Ii in iiiiiIIii :
    pass
   elif 'user' in url or 'elete' in i1I1i111Ii :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oOOo0 = i11111IIIII ( url )
    Iii1Iii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
    for Ooo0oOooo0 , url , i1I1i111Ii in Iii1Iii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + Ooo0oOooo0 , 'http:' + Ooo0oOooo0 , '' )
     else :
      pass
   else :
    O0O0ooOOO ( '[COLORred]' + I1I11i + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 , i11I1 , '' )
    if 97 - 97: iI11I1II1I1I + oOoO0o00OO0 - OoOo0o
    if 98 - 98: ooOoO0O00 % IIiIiII11i
    if 30 - 30: oOoO0o00OO0
def Ooo0ooo0oo ( ) :
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Setup Tv Guide[/COLOR]' , '' , 100212 , I1IIIii + 'linkchannels.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Open Guide[/COLOR]' , '' , 100213 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 if 21 - 21: I11i1ii1 - oOo0O0Ooo % ii + ooo0O
def o00O0o ( ) :
 ivuesetup . iVueInt ( )
 if 28 - 28: oOo0O0Ooo
def O00IiII ( ) :
 IIiOo ( )
 return
 if 10 - 10: oOo % oOo / ooo0O - iii1i1iiiiIi
def IIiOo ( ) :
 if 44 - 44: oOOoOooOo - o0o00Oo0O / IIiIiII11i . iI11I1II1I1I . ooOoO0O00
 OOooOoooOoOo = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 Oo00oo = OOooOoooOoOo . getSetting ( id = 'User' )
 oO0oO = OOooOoooOoOo . getSetting ( id = 'Pass' )
 o0ooo = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 IiI = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 ii11I = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 Ooo0O00 = "http://piesustv" + Ooo + ":8000/get.php?username=" + Oo00oo + "&password=" + oO0oO + "&type=m3u_plus&output=ts"
 oooo0oOOoO000 = "http://piesustv" + Ooo + ":8000/xmltv.php?username=" + Oo00oo + "&password=" + oO0oO + "&type=m3u_plus&output=ts"
 if 86 - 86: iI11I1II1I1I - i1IiiiI1iI % oOOoOooOo . OoOo0o * iii1i1iiiiIi . ooOoO0O00
 xbmc . executeJSONRPC ( o0ooo )
 xbmc . executeJSONRPC ( IiI )
 xbmc . executeJSONRPC ( ii11I )
 if 75 - 75: i1IiiiI1iI + oOOoOooOo / oOOoOooOo - OoOo0o * oOo * oOOoOooOo
 o0OO0ooOOO = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 o0OO0ooOOO . setSetting ( id = 'm3uUrl' , value = Ooo0O00 )
 o0OO0ooOOO . setSetting ( id = 'epgUrl' , value = oooo0oOOoO000 )
 o0OO0ooOOO . setSetting ( id = 'm3uCache' , value = "false" )
 o0OO0ooOOO . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def i1i1I1Ii1IIii ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 80 - 80: Ii
if 29 - 29: oOo0O0Ooo . OoOo0o + IIiIiII11i . I1ii11iIi11i
if 29 - 29: i1iIi - o0o00Oo0O . oOOoOooOo / oOoO0o00OO0 / ooOoO0O00 . iii1i1iiiiIi
def II1iiiiI1 ( ) :
 if 33 - 33: ii % oOoO0o00OO0 . o0o00Oo0O / oOoO0o00OO0
 if 63 - 63: I11i1ii1 + iI11I1II1I1I + oOo0O0Ooo + O0Oooo0O
 if 72 - 72: oOo + Ii + oOoO0o00OO0
 if 96 - 96: OOOo00oo0oO % ooOoO0O00 / ooo0O
 if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + iiiiiiii1
 if 88 - 88: o0o00Oo0O . OOOo00oo0oO % oOo0O0Ooo
 if 10 - 10: oOo0O0Ooo + o0o00Oo0O
 if 75 - 75: o0o00Oo0O % iI11I1II1I1I / iii1i1iiiiIi % OoOo0o / I11i1ii1
 if 31 - 31: Ii * iii1i1iiiiIi
 if 69 - 69: Ii
 if 61 - 61: o0o00Oo0O
 if 21 - 21: oOo % iI11I1II1I1I . oOo
 if OooO0 == "insert_username" :
  OO000OOOo0Oo = Oo00O0O ( )
  oOoOOoo = Oo00O0o0O ( )
  i1 ( 'User' , OO000OOOo0Oo )
  i1 ( 'Pass' , oOoOOoo )
  xbmc . executebuiltin ( 'Container.Refresh' )
  O0OoOO = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( OO000OOOo0Oo , oOoOOoo )
  O0OoOO = i11111IIIII ( O0OoOO )
  if O0OoOO == "" :
   o0o0oO0OOO = "[COLOR " + iiI1IiI + "]Incorrect Login Details[/COLOR]"
   O0Ooo0OOOo0oo = "[COLOR " + iiI1IiI + "]Please Re-enter[/COLOR]"
   I1111i1 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , o0o0oO0OOO , O0Ooo0OOOo0oo , I1111i1 )
   II1iiiiI1 ( )
  else :
   o0o0oO0OOO = "[COLOR " + iiI1IiI + "]Login Successful[/COLOR]"
   O0Ooo0OOOo0oo = "[COLOR " + iiI1IiI + "]Welcome to GenieTv[/COLOR]"
   I1111i1 = ( '[COLOR ' + iiI1IiI + ']%s[/COLOR]' % OO000OOOo0Oo )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , o0o0oO0OOO , O0Ooo0OOOo0oo , I1111i1 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   IIiIi1i1I11 ( )
 else :
  IIiIi1i1I11 ( )
def Oo00O0O ( ) :
 I1IiiI = xbmc . Keyboard ( '' , 'heading' , True )
 I1IiiI . setHeading ( 'Enter Username' )
 I1IiiI . setHiddenInput ( False )
 I1IiiI . doModal ( )
 if ( I1IiiI . isConfirmed ( ) ) :
  i11I1i11IIIi = I1IiiI . getText ( )
  return i11I1i11IIIi
 else :
  return False
  if 19 - 19: OOOo00oo0oO * iiiiiiii1 + iii1i1iiiiIi - OOOo00oo0oO + oOoO0o00OO0
  if 14 - 14: oOo
def Oo00O0o0O ( ) :
 I1IiiI = xbmc . Keyboard ( '' , 'heading' , True )
 I1IiiI . setHeading ( 'Enter Password' )
 I1IiiI . setHiddenInput ( False )
 I1IiiI . doModal ( )
 if ( I1IiiI . isConfirmed ( ) ) :
  i11I1i11IIIi = I1IiiI . getText ( )
  return i11I1i11IIIi
 else :
  return False
def i1iIii ( ) :
 Ooo0O00 = "http://piesustv" + Ooo + ":8000//get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  O0o00I1IIi1iI1iiI = urllib2 . urlopen ( Ooo0O00 )
  print O0o00I1IIi1iI1iiI . getcode ( )
  O0o00I1IIi1iI1iiI . close ( )
  if 27 - 27: iI11I1II1I1I % i1IiiiI1iI - O0Oooo0O
  pass
  if 67 - 67: o0o00Oo0O / O0Oooo0O * i1iIi % oOOoOooOo . oOoO0o00OO0 * OOOo00oo0oO
 except urllib2 . HTTPError , o00o :
  print o00o . getcode ( )
  iI111I11I1I1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + iiI1IiI + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + iiI1IiI + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def IIiIi1i1I11 ( ) :
 Oo0O00O0O ( )
 if 9 - 9: IIiIiII11i * Ii . OoOo0o - oOo
 if 31 - 31: Ii * i1iIi . ooo0O % OoOo0o * oOoO0o00OO0 % o0o00Oo0O
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']My Account[/COLOR]' , 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii , 60004 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Guide Menu[/COLOR]' , '' , 100211 , I1IIIii + 'TvGuide.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CatchUp Tv[/COLOR]' , '' , 90026 , I1IIIii + 'Sport.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']VOD Lists[/COLOR]' , '' , 40000 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 77 - 77: oOo + oOo . oOOoOooOo * ii + oOo
 if 6 - 6: ooOoO0O00 - i1IiiiI1iI
 if 89 - 89: oOOoOooOo - i1IiiiI1iI . o0o00Oo0O % ii . Ii
 if 35 - 35: IIiIiII11i / iii1i1iiiiIi - o0o00Oo0O . IIiIiII11i
def oO0o000oOO ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 Ii11Iiii = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii + '%26type%3Dm3u_plus%26output%3Dts'
 ooO0o00OOo = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OooO0 + '%26password%3D' + II11iiii1Ii
 O0OoOO = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=get_vod_categories'
 O0OoOO = i11111IIIII ( O0OoOO )
 if not O0OoOO == "" :
  iI1ii = 'https://tinyurl.com/create.php?source=indexpage&url=' + Ii11Iiii + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( iI1ii ) )
  oOoooOooOOoO = 'https://tinyurl.com/create.php?source=indexpage&url=' + ooO0o00OOo + '&submit=Make+TinyURL%21&alias='
  Ii11Iiii = i11111IIIII ( iI1ii )
  ooO0o00OOo = i11111IIIII ( oOoooOooOOoO )
  xbmc . log ( str ( ooO0o00OOo ) )
  O0O0O0OO00oo = I11IIIIiI1 ( Ii11Iiii , '<div class="indent"><b>' , '</b>' )
  o0oOOO = I11IIIIiI1 ( ooO0o00OOo , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + iiI1IiI + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % O0O0O0OO00oo , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % o0oOOO )
 else :
  return
def o00OoOooo ( ) :
 i1iIii ( )
 i1I1ii1 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , Iii1i + '&action=get_vod_streams' , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
 oOOo0 = i11111IIIII ( ooOooo00O )
 iI111i = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( ( '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , iiI , 40001 , I1IIIii + 'Vod_Lists.png' , Oo00OOOOO , '' )
def I1i1I1IIiIIi ( url ) :
 open = i11111IIIII ( iII1ii1IIII + url )
 Oo0 = o0O0OOOo0 ( open , '<channel>' , '</channel>' )
 for iIIi in Oo0 :
  if '<playlist_url>' in open :
   i1I1i111Ii = I11IIIIiI1 ( iIIi , '<title>' , '</title>' )
   III11I1 = I11IIIIiI1 ( iIIi , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   o00oOOooOOo0o ( str ( base64 . b64decode ( i1I1i111Ii ) ) . replace ( '?' , '' ) , III11I1 , 40001 , icon , oo0o0000 , '' )
  else :
   if xbmcaddon . Addon ( ) . getSetting ( 'meta' ) == 'true' :
    try :
     i1I1i111Ii = I11IIIIiI1 ( iIIi , '<title>' , '</title>' )
     i1I1i111Ii = base64 . b64decode ( i1I1i111Ii )
     I1ii1i = I11IIIIiI1 ( iIIi , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     url = I11IIIIiI1 ( iIIi , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     ooo0O0o00O = I11IIIIiI1 ( iIIi , '<description>' , '</description>' )
     ooo0O0o00O = base64 . b64decode ( ooo0O0o00O )
     o0oO0OoO0 = I11IIIIiI1 ( ooo0O0o00O , 'PLOT:' , '\n' )
     OO00OoOO = I11IIIIiI1 ( ooo0O0o00O , 'CAST:' , '\n' )
     iiii1II1ii11 = I11IIIIiI1 ( ooo0O0o00O , 'RATING:' , '\n' )
     oOOOOOoOO = I11IIIIiI1 ( ooo0O0o00O , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
     oOOOOOoOO = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( oOOOOOoOO )
     i1IIIII1 = I11IIIIiI1 ( ooo0O0o00O , 'DURATION_SECS:' , '\n' )
     IIIiiiiiI1I = I11IIIIiI1 ( ooo0O0o00O , 'GENRE:' , '\n' )
     O0oooO00ooO0 ( str ( i1I1i111Ii ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , I1ii1i , oo0o0000 , o0oO0OoO0 , str ( oOOOOOoOO ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( OO00OoOO ) . split ( ) , iiii1II1ii11 , i1IIIII1 , IIIiiiiiI1I )
    except : pass
    xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   else :
    i1I1i111Ii = I11IIIIiI1 ( iIIi , '<title>' , '</title>' )
    i1I1i111Ii = base64 . b64decode ( i1I1i111Ii )
    I1ii1i = I11IIIIiI1 ( iIIi , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    url = I11IIIIiI1 ( iIIi , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    ooo0O0o00O = I11IIIIiI1 ( iIIi , '<description>' , '</description>' )
    O0O0ooOOO ( i1I1i111Ii , url , 222 , I1ii1i , oo0o0000 , base64 . b64decode ( ooo0O0o00O ) )
    if 99 - 99: I11i1ii1
OOO0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
O0o0OOOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 29 - 29: ii . O0Oooo0O % O0Oooo0O
def IIIIIII1i ( ) :
 Ooo0O00 = "http://piesustv" + Ooo + ":8000/get.php?username=" + OooO0 + "&password=" + II11iiii1Ii + "&type=m3u_plus&output=ts"
 try :
  O0o00I1IIi1iI1iiI = urllib2 . urlopen ( Ooo0O00 )
  print O0o00I1IIi1iI1iiI . getcode ( )
  O0o00I1IIi1iI1iiI . close ( )
  if 30 - 30: I11i1ii1 - iiiiiiii1 - oOo
  pass
  if 33 - 33: iI11I1II1I1I / iiiiiiii1
 except urllib2 . HTTPError , o00o :
  print o00o . getcode ( )
  iI111I11I1I1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 74 - 74: ooo0O / OOOo00oo0oO - IIiIiII11i . IIiIiII11i . I11i1ii1 + IIiIiII11i
 iiI = "http://piesustv" + Ooo + ":8000/xmltv.php?username=%s&password=%s" % ( OooO0 , II11iiii1Ii )
 O0Ooo00o00O ( iiI , O0o0OOOO0 + "uide.xml" )
 if 80 - 80: iiiiiiii1
 o0OoOO = open ( OOO0o0 , 'r+' )
 input = open ( OOO0o0 ) . read ( ) . decode ( 'UTF-8' )
 iI1I1ii11IIi1 = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 o0OoOO . write ( iI1I1ii11IIi1 )
 o0OoOO . truncate ( )
 o0OoOO . close ( )
 OOoOOoOO ( )
 if 78 - 78: O0Oooo0O / O0Oooo0O + oOo0O0Ooo % OoOo0o * I11i1ii1
def OOoOOoOO ( ) :
 open = i11111IIIII ( IiIii11ii111 )
 all = o0O0OOOo0 ( open , '{"num' , 'direct' )
 for iIIi in all :
  if '"tv_archive":1' in iIIi :
   i1I1i111Ii = I11IIIIiI1 ( iIIi , '"epg_channel_id":"' , '"' )
   I1ii1i = I11IIIIiI1 ( iIIi , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = I11IIIIiI1 ( iIIi , 'stream_id":"' , '"' )
   i1I1i111Ii = i1I1i111Ii . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   o00oOOooOOo0o ( i1I1i111Ii , id , 90027 , I1ii1i , oo0o0000 , i1I1i111Ii )
   if 75 - 75: o0o00Oo0O
   if 56 - 56: oOo / IIiIiII11i
def IIIiiiiI1 ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 oO00oOooooo0 = open ( OOO0o0 )
 iii11i1 = ElementTree . parse ( oO00oOooooo0 )
 IIiI1I1IIiiI1 = "apples"
 import datetime as dt
 from datetime import time
 oooOOO0o0O0 = datetime . now ( ) - timedelta ( days = 5 )
 oO0Ooo0OooOOo = str ( oooOOO0o0O0 )
 oOoOooOo0o0 = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 iiiI1IiI = iii11i1 . findall ( "programme" )
 for Ii111IIIIii in iiiI1IiI :
  if name in Ii111IIIIii . attrib . get ( 'channel' ) :
   O00o = Ii111IIIIii . attrib . get ( 'start' )
   Iii1iIIiii1ii , Ii1iii11I , Ii11iIiiI = O00o . partition ( ' +' )
   oO0Ooo0OooOOo = str ( oO0Ooo0OooOOo ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   oOOOOOoOO , iiIIiII1IiiIIIIii , o0O0ooooooo00 = O00o . partition ( '2017' )
   oOOO = Ii111IIIIii . find ( 'title' ) . text + O00o
   o0O0ooooooo00 = o0O0ooooooo00 [ : - 6 ]
   if Iii1iIIiii1ii > oO0Ooo0OooOOo :
    if Iii1iIIiii1ii < oOoOooOo0o0 :
     Iii1IiiII1Ii1 = Iii1iIIiii1ii
     Iii1IiiII1Ii1 = Iii1IiiII1Ii1 [ : 4 ] + '/' + Iii1IiiII1Ii1 [ 4 : ]
     Iii1iIIiii1ii = Iii1iIIiii1ii [ : 4 ] + '-' + Iii1iIIiii1ii [ 4 : ]
     Iii1IiiII1Ii1 = Iii1IiiII1Ii1 [ : 7 ] + '/' + Iii1IiiII1Ii1 [ 7 : ]
     Iii1iIIiii1ii = Iii1iIIiii1ii [ : 7 ] + '-' + Iii1iIIiii1ii [ 7 : ]
     Iii1IiiII1Ii1 = Iii1IiiII1Ii1 [ : 10 ] + ' - ' + Iii1IiiII1Ii1 [ 10 : ]
     Iii1iIIiii1ii = Iii1iIIiii1ii [ : 10 ] + ':' + Iii1iIIiii1ii [ 10 : ]
     Iii1IiiII1Ii1 = Iii1IiiII1Ii1 [ : 15 ] + ':' + Iii1IiiII1Ii1 [ 15 : ]
     Iii1iIIiii1ii = Iii1iIIiii1ii [ : 13 ] + '-' + Iii1iIIiii1ii [ 13 : ]
     Iii1IiiII1Ii1 = Iii1IiiII1Ii1 [ : - 2 ]
     Iii1iIIiii1ii = Iii1iIIiii1ii [ : - 2 ]
     iiiIIi = ( "http://piesustv" + Ooo + ":8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( Iii1iIIiii1ii ) + "&duration=240" + "&stream=%s" ) % ( OooO0 , II11iiii1Ii , id )
     IIiI1I1IIiiI1 = iiiIIi + str ( Iii1iIIiii1ii ) + "&duration=240"
     Iii1IiiII1Ii1 = '[COLOR blue]%s - [/COLOR]' % Iii1IiiII1Ii1
     oOOO = str ( Iii1IiiII1Ii1 ) + Ii111IIIIii . find ( 'title' ) . text
     ooo0O0o00O = Ii111IIIIii . find ( 'desc' ) . text
     O0O0ooOOO ( oOOO , iiiIIi , 222 , I1IIIii + 'GTV.png' , Oo00OOOOO , ooo0O0o00O )
def OOoOo0O00oo ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OooO0 ) . replace ( 'PASSWORD' , II11iiii1Ii )
 ooooo0OoO0 = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 ooooo0OoO0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 ooooo0OoO0 . setProperty ( 'IsPlayable' , 'true' )
 ooooo0OoO0 . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooooo0OoO0 )
def O0Ooo00o00O ( url , dest ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oO0 . update ( 0 )
 oo0oO0oOo0O = time . time ( )
 urllib . urlretrieve ( url , dest , lambda OoOo00 , OOoOoO , OO000 : o0oOoo0o ( OoOo00 , OOoOoO , OO000 , o0oO0 , oo0oO0oOo0O ) )
def o0oOoo0o ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  IiiIiIIi = min ( numblocks * blocksize * 100 / filesize , 100 )
  O00Oo = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  oOOoo = numblocks * blocksize / ( time . time ( ) - start_time )
  if oOOoo > 0 :
   oo0O0 = ( filesize - numblocks * blocksize ) / oOOoo
  else :
   oo0O0 = 0
  oOOoo = oOOoo / 1024
  Ii111Ii11 = oOOoo / 1024
  Ii1II = float ( filesize ) / ( 1024 * 1024 )
  IIiII = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( O00Oo )
  o00o = '[COLOR white]Speed:  %.02f Mb/s ' % Ii111Ii11 + '[/COLOR]'
  dp . update ( IiiIiIIi , IIiII , o00o )
 except :
  IiiIiIIi = 100
  dp . update ( IiiIiIIi )
 if dp . iscanceled ( ) :
  iII11 = xbmcgui . Dialog ( )
  iII11 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 96 - 96: i1IiiiI1iI * oOoO0o00OO0 * i1iIi + oOoO0o00OO0 % oOo0O0Ooo + Ii
  sys . exit ( )
  dp . close ( )
  if 37 - 37: i1IiiiI1iI % oOoO0o00OO0 / oOOoOooOo
def o0oO ( ) :
 if II11iiii1Ii == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  ooOo0 ( )
  if 61 - 61: IIiIiII11i
  if 48 - 48: OoOo0o
  if 26 - 26: iiiiiiii1 * O0Oooo0O * OOOo00oo0oO * iii1i1iiiiIi
  if 48 - 48: iiiiiiii1 % Ii . ii * I11i1ii1 % oOo . iiiiiiii1
  if 6 - 6: o0o00Oo0O . oOOoOooOo - OOOo00oo0oO / Ii
  if 84 - 84: i1IiiiI1iI / oOoO0o00OO0 * ooo0O * oOo * OoOo0o * o0o00Oo0O
  if 83 - 83: o0o00Oo0O % IIiIiII11i + ooo0O / ii
  if 75 - 75: IIiIiII11i . oOo0O0Ooo + OoOo0o - iii1i1iiiiIi - o0o00Oo0O . i1IiiiI1iI
def ooOo0 ( ) :
 IIIi1I1IIii1II = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/panel_api.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( '"exp_date":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for iiI in iI111i :
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
 OOoOOO000O0 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 IiIIiii11II1 = re . compile ( '"created_at":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 iiii1i1II1 = re . compile ( '"max_connections":"(.+?)"' ) . findall ( IIIi1I1IIii1II )
 II1iI111iiIIiI1I = re . compile ( '"is_trial":"1"' ) . findall ( IIIi1I1IIii1II )
 iiIIiiIi = re . compile ( '"is_trial":"0"' ) . findall ( IIIi1I1IIii1II )
 iIIII1i1 = I1I1 ( )
 oO00o0oOoo = oOOI1 ( )
 for url in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']My GTV Account Information[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in iiiiii1ii1 :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in I1iii11 :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in IiIIiii11II1 :
  dt = datetime . fromtimestamp ( float ( IiIIiii11II1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in IIi11i1i1iI1 :
  dt = datetime . fromtimestamp ( float ( IIi11i1i1iI1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if oOoOooOo0o0 <= dt <= oOoOooOo0o0 + timedelta ( hours = 24 ) :
   II1i11I1 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , I1IIIii + 'MyAcc.png' )
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in OOoOOO000O0 :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in iiii1i1II1 :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in II1iI111iiIIiI1I :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] Yes' , '' , '' , I1IIIii + 'MyAcc.png' )
 for url in iiIIiiIi :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']Trial:[/COLOR] No' , '' , '' , I1IIIii + 'MyAcc.png' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Get Short Links[/COLOR]' , '' , 100214 , I1IIIii + 'shortlinks.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local IP Address:[/COLOR] ' + iIIII1i1 , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']External IP Address:[/COLOR] ' + oO00o0oOoo , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 63 - 63: oOo . OOOo00oo0oO + O0Oooo0O . iii1i1iiiiIi / Ii / iiiiiiii1
 II1i11I1 ( '[COLOR' + iiI1IiI + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + OoOo0o
def I11II11IiI11 ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
 O00oIi11Iiii1iiii ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 10 - 10: iiiiiiii1 % I1ii11iIi11i
def i111111 ( data ) :
 o0o = len ( data ) % 4
 if 78 - 78: i1IiiiI1iI % I1ii11iIi11i + iii1i1iiiiIi . oOoO0o00OO0 % OOOo00oo0oO / i1iIi
 if 37 - 37: OOOo00oo0oO % O0Oooo0O % OOOo00oo0oO
 if 14 - 14: oOo / oOo0O0Ooo
 if 66 - 66: I1ii11iIi11i / Ii % oOOoOooOo
 if 43 - 43: OoOo0o
 if 84 - 84: OoOo0o . I11i1ii1 . iiiiiiii1
 if o0o != 0 :
  data += b'=' * ( 4 - o0o )
 return base64 . decodestring ( data )
def I11IIIIiI1 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : iIII1I1i = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : iIII1I1i = ''
 else :
  try : iIII1I1i = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : iIII1I1i = ''
 return iIII1I1i
 if 26 - 26: iiiiiiii1 - I1ii11iIi11i + oOo0O0Ooo + ooo0O
 if 37 - 37: ooo0O * OoOo0o + oOo0O0Ooo . oOoO0o00OO0 * ii
def o0O0OOOo0 ( text , start_with , end_with ) :
 iIII1I1i = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return iIII1I1i
def I1I1 ( ) :
 OoooOO0 = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 OoooOO0 . connect ( ( '8.8.8.8' , 0 ) )
 OoooOO0 = OoooOO0 . getsockname ( ) [ 0 ]
 return OoooOO0
 if 69 - 69: IIiIiII11i + iiiiiiii1
def oOOI1 ( ) :
 open = i11111IIIII ( 'http://canyouseeme.org/' )
 iIIII1i1 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( iIIII1i1 . group ( ) )
Iii1i = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
IiIii11ii111 = 'http://piesustv' + Ooo + ':8000/panel_api.php?username=%s&password=%s' % ( OooO0 , II11iiii1Ii )
oooOOO = 'http://piesustv' + Ooo + ':8000/movie/%s/%s/' % ( OooO0 , II11iiii1Ii )
Iii1 = 'http://piesustv' + Ooo + ':8000/live/%s/%s/' % ( OooO0 , II11iiii1Ii )
o00o0 = '&action=get_live_categories'
OOoOo0O0 = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OooO0 , II11iiii1Ii )
ooOooo00O = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OooO0 , II11iiii1Ii )
if 39 - 39: O0Oooo0O . oOo % oOOoOooOo . OoOo0o / iiiiiiii1 * oOo
iII1ii1IIII = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OooO0 , II11iiii1Ii )
iiI1i = 'http://piesustv' + Ooo + ':8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OooO0 , II11iiii1Ii )
o0O00o0 = 'http://piesustv' + Ooo + ':8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OooO0 , II11iiii1Ii )
OoOoOooO0o = "http://piesustv" + Ooo + ":8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OooO0 , II11iiii1Ii )
if 23 - 23: oOo0O0Ooo
def i1IIiI1iII ( ) :
 i1iIii ( )
 open = i11111IIIII ( o0O00o0 )
 Oo0 = o0O0OOOo0 ( open , '<channel>' , '</channel>' )
 for iIIi in Oo0 :
  i1I1i111Ii = I11IIIIiI1 ( iIIi , '<title>' , '</title>' )
  i1I1i111Ii = base64 . b64decode ( i1I1i111Ii )
  III11I1 = I11IIIIiI1 ( iIIi , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o00oOOooOOo0o ( '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]' , III11I1 , 60003 , I1IIIii + 'GTV.png' , Oo00OOOOO , '' )
  if 45 - 45: ooOoO0O00 % OoOo0o % IIiIiII11i
def IIIIi1Iii1iIi ( url ) :
 open = i11111IIIII ( OoOoOooO0o + url )
 Oo0 = o0O0OOOo0 ( open , '<channel>' , '</channel>' )
 for iIIi in Oo0 :
  i1I1i111Ii = I11IIIIiI1 ( iIIi , '<title>' , '</title>' )
  i1I1i111Ii = base64 . b64decode ( i1I1i111Ii )
  xbmc . log ( str ( i1I1i111Ii ) )
  I1ii1i = I11IIIIiI1 ( iIIi , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  III11I1 = I11IIIIiI1 ( iIIi , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  ooo0O0o00O = I11IIIIiI1 ( iIIi , '<description>' , '</description>' )
  ooo0O0o00O = base64 . b64decode ( ooo0O0o00O )
  ii1IIi1iI1ii1 = '('
  o00iIIiIi111iI = ')'
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , III11I1 , 222 , I1ii1i , oo0o0000 , ( '[COLOR' + iiI1IiI + ']' + ooo0O0o00O + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( o00iIIiIi111iI , '[COLORsteelblue]' ) . replace ( ii1IIi1iI1ii1 , '[COLORorangered]' ) )
  if 40 - 40: iii1i1iiiiIi + oOo % ii * ooo0O / iii1i1iiiiIi + ii
def o0OOOoO0O ( url ) :
 url = url
 oOOo0 = i11111IIIII ( OOoOo0O0 + url )
 iI111i = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , type , I1 , ooOO0ooo0o in iI111i :
  iiIiiIi1 = ( Iii1 + I1 + '.m3u8' ) . strip ( )
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiIiiIi1 , 222 , ( ooOO0ooo0o ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  O00oO000O0O ( 'tvshows' , 'Media Info 3' )
def OoOOo ( url , name , img ) :
 img = img
 name = name
 url = url
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/xmltv.php?username=' + OooO0 + '&password=' + II11iiii1Ii )
 iI111i = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oOOo0 )
 for ooo , III11iI1i11i in iI111i :
  if name == ooo :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) + III11iI1i11i , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def IIiIOOoOo0oO0oo00 ( name ) :
 OOI1I = name
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oOOo0 )
 for name , Ooo0oOooo0 , iiI in iI111i :
  iiI = ( iiI ) . replace ( '.ts' , '.m3u8' )
  O0O0ooOOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiI ) . strip ( ) , 222 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
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
def o0oo0000OO ( ) :
 o00oOOooOOo0o ( 'Full Backup' , '' , 10061 , I1IIIii + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0OoO00oOO0o ) :
  o00oOOooOOo0o ( 'Backup Genie Favourites' , iiI , 10062 , I1IIIii + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
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
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
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
  o0OoOO = open ( IiIi , mode = 'w' )
  o0OoOO . write ( oOOo0OOoOO0 )
  o0OoOO . close ( )
 else :
  if 'guisettings.xml' in description :
   iIIi = open ( os . path . join ( oOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iIII1I1i = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   iI111i = re . compile ( iIII1I1i ) . findall ( iIIi )
   for type , IIi1IiiIi1III , IiIiIiiIIii in iI111i :
    IiIiIiiIIii = IiIiIiiIIii . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IIi1IiiIi1III , IiIiIiiIIii ) )
  else :
   IiIi = os . path . join ( url )
   oOOo0OOoOO0 = open ( os . path . join ( oOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0OoOO = open ( IiIi , mode = 'w' )
   o0OoOO . write ( oOOo0OOoOO0 )
   o0OoOO . close ( )
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
 o0OO0Oo = Ii11I1iIIi
 O0ooO = xbmc . translatePath ( os . path . join ( oOOoO , o0OO0Oo + '.zip' ) )
 iIOO = [ 'plugin.video.GenieTv' ]
 I1III1I11I1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 oO000OoO00OoO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1IiIi1iiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iiII1II11i = "Creating full backup of existing build"
 ooO0OoooooOo0oOo0 = "Creating Community Build"
 II11II = "Archiving..."
 i1ii11III = ""
 o00O = "Please Wait"
 ii1I1I1 ( i1111 , O0ooO , ooO0OoooooOo0oOo0 , II11II , i1ii11III , o00O , oO000OoO00OoO , I1IiIi1iiI )
 time . sleep ( 1 )
 oo0oOOO0oOoo = xbmc . translatePath ( os . path . join ( oOOoO , o0OO0Oo + '_guisettings.zip' ) )
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
 iI1iIi1 = [ ]
 o0oO0 . create ( message_header , message1 , message2 , message3 )
 for O00oOOO0 , Iiiiii , oOOOOOoOOoo0 in os . walk ( sourcefile ) :
  for file in oOOOOOoOOoo0 :
   iI1iIi1 . append ( file )
 oo0OOO0OOoOO = len ( iI1iIi1 )
 for O00oOOO0 , Iiiiii , oOOOOOoOOoo0 in os . walk ( sourcefile ) :
  Iiiiii [ : ] = [ oOoO for oOoO in Iiiiii if oOoO not in exclude_dirs ]
  oOOOOOoOOoo0 [ : ] = [ o0OoOO for o0OoOO in oOOOOOoOOoo0 if o0OoOO not in exclude_files ]
  for file in oOOOOOoOOoo0 :
   o0O00ooo0 . append ( file )
   II1i1 = len ( o0O00ooo0 ) / float ( oo0OOO0OOoOO ) * 100
   o0oO0 . update ( int ( II1i1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o0o0oo0OOo0O0 = os . path . join ( O00oOOO0 , file )
   if not 'temp' in Iiiiii :
    if not 'plugin.program.originwizard' in Iiiiii :
     import time
     iIIiiII11i1I1 = '01/01/1980'
     Ii111Ii1iiIi1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0o0oo0OOo0O0 ) ) )
     if Ii111Ii1iiIi1 > iIIiiII11i1I1 :
      IiIIIii1i1iI . write ( o0o0oo0OOo0O0 , o0o0oo0OOo0O0 [ OoOOoO0o : ] )
 IiIIIii1i1iI . close ( )
 o0oO0 . close ( )
 if 62 - 62: oOo . iiiiiiii1 . iiiiiiii1 % ooOoO0O00 * OOOo00oo0oO % I1ii11iIi11i
 if 20 - 20: oOOoOooOo . I11i1ii1 / i1IiiiI1iI . ii * OoOo0o + i1iIi
def iiIII ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , I1IIIii + 'scoob.png' , Oo00OOOOO , '' )
 if 30 - 30: i1IiiiI1iI
 if 46 - 46: oOOoOooOo
def o0O0o ( ) :
 Oo0O00O0O ( )
 OoO = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  O00OOooo0Ooo ( )
 if iiI1IIIi == 1 :
  oOO0OOOOoooO ( )
 if iiI1IIIi == 2 :
  I111ii1III1I ( )
 if iiI1IIIi == 3 :
  ooo00o0OO ( )
  if 84 - 84: OOOo00oo0oO + IIiIiII11i * IIiIiII11i % ooo0O / iiiiiiii1 + oOOoOooOo
  if 9 - 9: iiiiiiii1
  if 25 - 25: OoOo0o - i1iIi . i1IiiiI1iI
  if 57 - 57: ooo0O + I1ii11iIi11i * oOoO0o00OO0 - oOOoOooOo % iI11I1II1I1I - i1iIi
  if 37 - 37: oOo * i1IiiiI1iI + i1iIi + oOoO0o00OO0 * ooo0O
  if 95 - 95: i1iIi - Ii % Ii - o0o00Oo0O * O0Oooo0O
  if 81 - 81: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + iii1i1iiiiIi
  if 100 - 100: ooOoO0O00 % i1iIi
  if 55 - 55: oOo0O0Ooo + iiiiiiii1
def OO00o0 ( ) :
 Oo0O00O0O ( )
 if O0oo0OO0 . getSetting ( 'Simplify' ) == 'true' :
  OoO = [ '[COLOR' + iiI1IiI + ']RaysRavers Radio[/COLOR]' , '[COLOR' + iiI1IiI + ']ThunderStruck[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if iiI1IIIi == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if iiI1IIIi == 2 :
   IiIiIi1I1OooO00O0OO0oo ( )
  if iiI1IIIi == 3 :
   Oo0OO0 ( )
  if iiI1IIIi == 4 :
   I1iIi1IiI1i ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iiI1IIIi == 5 :
   IiiIiiiiI1III ( )
  if iiI1IIIi == 6 :
   II111111 ( ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iiI1IIIi == 7 :
   i1iI1i11iIi1 ( ( o0oOoO00o ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iiI1IIIi == 8 :
   Oo0O00O ( str ( O00OOOoOoo0O ) + ( o0oOoO00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iiI1IIIi == 9 :
   OOoOOO0 ( )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RaysRavers Radio[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , I1IIIii + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']ThunderStruck[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , I1IIIii + 'Thunder.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , I1IIIii + 'RadioNomy.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( O00OOOoOoo0O ) , 30031 , I1IIIii + 'MusicChannels.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , I1IIIii + 'UKRadio.png' , Oo00OOOOO , '' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( O00OOOoOoo0O ) , 1013 , I1IIIii + 'WorldRadio.png' , Oo00OOOOO , '' )
  if O0oo0OO0 . getSetting ( 'CONCERTS' ) == 'true' :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , I1IIIii + 'Concerts.png' , Oo00OOOOO , '' )
   if 18 - 18: o0o00Oo0O - I11i1ii1 + OoOo0o . o0o00Oo0O
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( o0oOoO00o ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , I1IIIii + 'MusicVideos.png' , Oo00OOOOO , '' )
  if 72 - 72: i1IiiiI1iI * iii1i1iiiiIi % O0Oooo0O % oOOoOooOo
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( O00OOOoOoo0O ) , 1111 , I1IIIii + 'MusicSearch.png' , Oo00OOOOO , '' )
  if 22 - 22: OoOo0o - oOoO0o00OO0 / I11i1ii1
  if 95 - 95: ooo0O
 O00oO000O0O ( 'movies' , 'MAIN' )
iII1ii1 = 'white'
I1i1iiiI1 = 'gold'
def oOo0O ( ) :
 Oo0O00O0O ( )
 if O00Ooo ( True ) == False : OoO0ooOOoo = 0
 else : OoO0ooOOoo = oO00O0 ( O00Ooo ( True ) , True , True )
 if O00Ooo ( True , True ) == False : OOO0oOoO00OoO = 0
 else : OOO0oOoO00OoO = oO00O0 ( O00Ooo ( True , True ) , True , True )
 II1IiI1iI = int ( OoO0ooOOoo ) + int ( OOO0oOoO00OoO )
 IiIi1I11 = str ( II1IiI1iI ) + ' Error(s) Found' if II1IiI1iI > 0 else 'None Found'
 IiI1 = ': [COLORsteelblue]Not Found[/COLOR]' if not os . path . exists ( Oo0o0000o0o0 ) else ": [COLORorangered]%s[/COLOR]" % O000oo0o ( os . path . getsize ( Oo0o0000o0o0 ) )
 I11iiIiI1II11 = OOOoOOOo ( oO )
 oO0000 = OOOoOOOo ( i1iiIIiiI111 )
 OOOIIIIiiIi = ooooOOo ( )
 O0Oo0oO0OO0 = I11iiIiI1II11 + oO0000 + OOOIIIIiiIi
 iIIII1i1 = I1I1 ( )
 oO00o0oOoo = oOOI1 ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAN UP:[COLORorangered] [B]%s[/B][/COLOR]' % O000oo0o ( O0Oo0oO0OO0 ) , 'url' , 9666 , I1IIIii + 'MAIN5.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , I1IIIii + 'KillKodi.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , I1IIIii + 'Speedtest.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG Errors:[COLORorangered] %s[/COLOR]' % ( IiIi1I11 ) , '' , 219999990 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR LOG FILES: [COLORorangered]' + IiI1 + '[/COLOR]' , '' , 219999991 , I1IIIii + 'View-Log-File.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE CACHE:[COLORorangered] [B]%s[/B][/COLOR]' % O000oo0o ( OOOIIIIiiIi ) , 'url' , 14 , I1IIIii + 'DeleteCache.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']DELETE PACKAGES:[COLORorangered] [B]%s[/B][/COLOR]' % O000oo0o ( I11iiIiI1II11 ) , 'url' , 6 , I1IIIii + 'DeletePackages.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , 'url' , 10 , I1IIIii + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']LAST RESORT FIX EMPTY REPOS[/COLOR]' , 'url' , 9 , I1IIIii + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']CLEAR THUBMNAILS:[COLORorangered] [B]%s[/B][/COLOR]' % O000oo0o ( oO0000 ) , 'url' , 219999992 , I1IIIii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']Local IP Address:[COLORorangered] ' + iIIII1i1 + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']External IP Address:[COLORorangered] ' + oO00o0oOoo + '[/COLOR] ' , '' , '' , I1IIIii + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 54 - 54: oOo0O0Ooo
 if 19 - 19: iiiiiiii1 . i1IiiiI1iI * ii - OoOo0o + o0o00Oo0O * O0Oooo0O
 O00oO000O0O ( 'movies' , 'MAIN' )
def OoI1 ( proc ) :
 xbmc . executebuiltin ( proc )
 if 21 - 21: Ii * iiiiiiii1 / oOOoOooOo % iiiiiiii1 * I1ii11iIi11i
def oo0 ( ) :
 OoI1 ( 'Container.Refresh()' )
def o0Oo00o0 ( ) :
 o0OoOO = open ( Oo0o0000o0o0 , 'w' ) ; o0OoOO . close ( ) ; oOoO00o ( "[COLOR %s]%s[/COLOR]" % ( iII1ii1 , oOo0oooo00o ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % I1i1iiiI1 )
 oo0 ( )
 if 42 - 42: O0Oooo0O / iii1i1iiiiIi % OOOo00oo0oO
def oOOoOo0Ooo ( type = None ) :
 o0OOoOoo00 = Oo0Ooo0 ( 'Textures' )
 if not type == None : iiI1IIIi = 1
 else : iiI1IIIi = iI111I11I1I1 . yesno ( oOo0oooo00o , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( I1i1iiiI1 , o0OOoOoo00 ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if iiI1IIIi == 1 :
  try : IiIIiIi11ii ( os . join ( oooOOOOO , o0OOoOoo00 ) )
  except : II11IiIIiiiii ( 'Failed to delete, Purging DB.' ) ; oooOOo0o0OOO ( o0OOoOoo00 )
  IiiiII ( i1iiIIiiI111 )
  if 82 - 82: ooOoO0O00 . oOoO0o00OO0 - OOOo00oo0oO . O0Oooo0O * OOOo00oo0oO
 else : II11IiIIiiiii ( 'Clear thumbnames cancelled' )
 I11II1I ( )
 if 92 - 92: ooo0O
 if 37 - 37: OOOo00oo0oO
def I11II1I ( ) :
 if not os . path . exists ( i1iiIIiiI111 ) : os . makedirs ( i1iiIIiiI111 )
 I1Ii1iI1IiI1I = '0123456789abcdef'
 o0OOOoO = os . path . join ( i1iiIIiiI111 , 'Video' , 'Bookmarks' )
 for ii1IIII in I1Ii1iI1IiI1I :
  ooo0 = os . path . join ( i1iiIIiiI111 , ii1IIII )
  if not os . path . exists ( ooo0 ) : os . makedirs ( ooo0 )
 if not os . path . exists ( o0OOOoO ) : os . makedirs ( o0OOOoO )
 if 66 - 66: ooo0O * oOo % ooOoO0O00 - iI11I1II1I1I
def Oo0Ooo0 ( DB ) :
 if DB in [ 'Addons' , 'ADSP' , 'Epg' , 'MyMusic' , 'MyVideos' , 'Textures' , 'TV' , 'ViewModes' ] :
  iI111i = glob . glob ( os . path . join ( oooOOOOO , '%s*.db' % DB ) )
  I11Ii = '%s(.+?).db' % DB [ 1 : ]
  III = 0
  for file in iI111i :
   try : iI1i1IiI1i = int ( re . compile ( I11Ii ) . findall ( file ) [ 0 ] )
   except : iI1i1IiI1i = 0
   if III < iI1i1IiI1i :
    III = iI1i1IiI1i
  return '%s%s.db' % ( DB , III )
 else : return False
 if 42 - 42: iI11I1II1I1I * oOo0O0Ooo * O0Oooo0O
def IiiiII ( path ) :
 II11IiIIiiiii ( "Deleting Folder: %s" % path , xbmc . LOGNOTICE )
 try : shutil . rmtree ( path , ignore_errors = True , onerror = None )
 except : return False
 if 62 - 62: OoOo0o * o0o00Oo0O % I11i1ii1 . I11i1ii1 . oOo0O0Ooo
def oooOOo0o0OOO ( name ) :
 if 91 - 91: ooOoO0O00 . iiiiiiii1
 if 37 - 37: iiiiiiii1 - i1IiiiI1iI + iI11I1II1I1I / O0Oooo0O - oOo . ooo0O
 if 62 - 62: oOoO0o00OO0
 II11IiIIiiiii ( 'Purging DB %s.' % name , xbmc . LOGNOTICE )
 if os . path . exists ( name ) :
  try :
   I11IiI1iII = database . connect ( name )
   i11Ii111I1 = I11IiI1iII . cursor ( )
  except Exception , o00o :
   II11IiIIiiiii ( "DB Connection Error: %s" % str ( o00o ) , xbmc . LOGERROR )
   return False
 else : II11IiIIiiiii ( '%s not found.' % name , xbmc . LOGERROR ) ; return False
 i11Ii111I1 . execute ( "SELECT name FROM sqlite_master WHERE type = 'table'" )
 for Ooi11 in i11Ii111I1 . fetchall ( ) :
  if Ooi11 [ 0 ] == 'version' :
   II11IiIIiiiii ( 'Data from table `%s` skipped.' % Ooi11 [ 0 ] , xbmc . LOGDEBUG )
  else :
   try :
    i11Ii111I1 . execute ( "DELETE FROM %s" % Ooi11 [ 0 ] )
    I11IiI1iII . commit ( )
    II11IiIIiiiii ( 'Data from table `%s` cleared.' % Ooi11 [ 0 ] , xbmc . LOGDEBUG )
   except Exception , o00o : II11IiIIiiiii ( "DB Remove Table `%s` Error: %s" % ( Ooi11 [ 0 ] , str ( o00o ) ) , xbmc . LOGERROR )
 i11Ii111I1 . close ( )
 II11IiIIiiiii ( '%s DB Purging Complete.' % name , xbmc . LOGNOTICE )
 III11iI1i11i = name . replace ( '\\' , '/' ) . split ( '/' )
 oOoO00o ( "[COLOR %s]Purge Database[/COLOR]" % iII1ii1 , "[COLOR %s]%s Complete[/COLOR]" % ( I1i1iiiI1 , III11iI1i11i [ len ( III11iI1i11i ) - 1 ] ) )
 if 67 - 67: i1IiiiI1iI / o0o00Oo0O * i1iIi - I11i1ii1 . ii + I11i1ii1
def IiIIiIi11ii ( path ) :
 II11IiIIiiiii ( "Deleting File: %s" % path , xbmc . LOGNOTICE )
 try : os . remove ( path )
 except : return False
 if 20 - 20: O0Oooo0O - iii1i1iiiiIi
 if 91 - 91: ooOoO0O00
def ooooOOo ( ) :
 ii11IiI = os . path . join ( oO0o0o0ooO0oO , 'addon_data' )
 I1iI1Ii11 = [
 ( os . path . join ( I11 , 'plugin.video.phstreams' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.bob' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.specto' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.genesis' , 'cache.db' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.exodus' , 'cache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'onechannelcache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'saltscache.db' ) ) ,
 ( os . path . join ( oooOOOOO , 'saltshd.lite.db' ) ) ]
 I1II11IIi11i = [
 ( ii11IiI ) ,
 ( I11 ) ,
 ( os . path . join ( i1111 , 'cache' ) ) ,
 ( os . path . join ( i1111 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( ii11IiI , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( ii11IiI , 'plugin.video.itv' , 'Images' ) ) ]
 if 67 - 67: iI11I1II1I1I - iiiiiiii1
 O0Oo0oO0OO0 = 0
 if 81 - 81: o0o00Oo0O
 for ii1IIII in I1II11IIi11i :
  if os . path . exists ( ii1IIII ) and not ii1IIII in [ I11 , ii11IiI ] :
   O0Oo0oO0OO0 = OOOoOOOo ( ii1IIII , O0Oo0oO0OO0 )
  else :
   for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( ii1IIII ) :
    for oOoO in Iiiiii :
     if 'cache' in oOoO . lower ( ) and not oOoO . lower ( ) == 'meta_cache' : O0Oo0oO0OO0 = OOOoOOOo ( os . path . join ( i11ii11IiI1 , oOoO ) , O0Oo0oO0OO0 )
     if 47 - 47: iI11I1II1I1I % i1IiiiI1iI . i1IiiiI1iI / o0o00Oo0O . Ii * i1iIi
 return O0Oo0oO0OO0
def OOOoOOOo ( path , total = 0 ) :
 for iio0Oo , IiiiiiiI111i , Ooo00O0 in os . walk ( path ) :
  for o0OoOO in Ooo00O0 :
   iiIIIIiI11II1 = os . path . join ( iio0Oo , o0OoOO )
   total += os . path . getsize ( iiIIIIiI11II1 )
 return total
def O000oo0o ( num , suffix = 'B' ) :
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
 O00oO000O0O ( 'movies' , 'MAIN' )
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
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 18 - 18: o0o00Oo0O / iI11I1II1I1I + Ii + I1ii11iIi11i
def O0oOOo0Oo ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , I1IIIii + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , I1IIIii + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 31 - 31: ooOoO0O00 - i1IiiiI1iI + O0Oooo0O + oOOoOooOo . oOOoOooOo . o0o00Oo0O
def ii11IiI1 ( ) :
 Oo0O00O0O ( )
 O0O0ooOOO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( O00OOOoOoo0O ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , I1IIIii + 'FTV4.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( O00OOOoOoo0O ) + '/wizard/customftv/settings.xml' , 17 , I1IIIii + 'FTV3.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , I1IIIii + 'FTV1.png' , Oo00OOOOO , '' )
 O0O0ooOOO ( 'RESET FTV DATABASE' , 'url' , 18 , I1IIIii + 'FTV2.png' , Oo00OOOOO , '' )
 if 43 - 43: iI11I1II1I1I
 if 29 - 29: I11i1ii1 % oOOoOooOo + oOo . ooOoO0O00 + oOo0O0Ooo
 if 24 - 24: O0Oooo0O / i1iIi * oOoO0o00OO0 - ii / oOo0O0Ooo . OOOo00oo0oO
def oo0OOoOo0 ( ) :
 Oo0O00O0O ( )
 OoO = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  oO00oO0 ( )
 if iiI1IIIi == 0 :
  o0oI1Iii ( iiI )
 if iiI1IIIi == 0 :
  II1I1Ii11 ( iiI )
  if 20 - 20: i1iIi / iiiiiiii1 + IIiIiII11i . Ii . OoOo0o
  if 77 - 77: iii1i1iiiiIi
  if 91 - 91: OOOo00oo0oO
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 56 - 56: iI11I1II1I1I % IIiIiII11i / iii1i1iiiiIi % ii
def I1I ( ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 iI111i = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ooo0oOooo0 , i1I1i111Ii in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , Ooo0oOooo0 , Ooo0oOooo0 , '' )
 O00oO000O0O ( 'tvshows' , 'INFO' )
 if 37 - 37: oOoO0o00OO0 % OOOo00oo0oO
def o0ooO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 5 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 14 - 14: o0o00Oo0O
def oO00oO0 ( ) :
 Oo0O00O0O ( )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( O00OOOoOoo0O ) , 36 , I1IIIii + 'GothamSkins.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( O00OOOoOoo0O ) , 37 , I1IIIii + 'HelixSkins.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , i1111 , 38 , I1IIIii + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 16 - 16: ooOoO0O00 * oOOoOooOo % oOo + i1iIi
def IIIi11Ii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + O00oO0o000oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 92 - 92: OOOo00oo0oO / oOoO0o00OO0
def Iiii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Ii11i1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 70 - 70: oOoO0o00OO0 . oOoO0o00OO0 / i1IiiiI1iI . oOoO0o00OO0
def IiIOOOoo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + ooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 61 - 61: oOo - Ii / i1IiiiI1iI % I11i1ii1
def I1111IiII1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 26 - 26: ooOoO0O00 / oOo0O0Ooo / i1IiiiI1iI + i1IiiiI1iI
def o0oI1Iii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + i1II111iiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 40 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 6 - 6: IIiIiII11i
def i1iII11IiI ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iiIOoO0000oo0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 5 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 70 - 70: oOoO0o00OO0 . o0o00Oo0O
def II11IiIi11 ( ) :
 OoO = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  oOoOOo ( )
 if iiI1IIIi == 1 :
  I1111ii11 ( )
 if iiI1IIIi == 2 :
  I1iI1I1111i ( )
  if 9 - 9: ooo0O % O0Oooo0O + i1IiiiI1iI
  if 55 - 55: oOo - oOoO0o00OO0
  if 38 - 38: iI11I1II1I1I % I11i1ii1 % oOo % o0o00Oo0O * iI11I1II1I1I / O0Oooo0O
  if 65 - 65: OoOo0o - oOo0O0Ooo * O0Oooo0O
def I1111ii11 ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 iI111i = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( i1iI1 )
 for iiI , oO00O0O000OO in iI111i :
  oOo0 ( 'Android Apps' + oO00O0O000OO , 'https://www.apkfiles.com' + iiI , 30035 , I1IIIii + 'apps.png' )
 for iiI , oO00O0O000OO in IIi11i1i1iI1 :
  oOo0 ( 'Android Games' + oO00O0O000OO , 'https://www.apkfiles.com' + iiI , 30035 , I1IIIii + 'GAMES.png' )
 O00oO000O0O ( 'movies' , 'MAIN' )
def o0000Oo0 ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  if '/cat' in url :
   oOo0 ( ( i1I1i111Ii ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def I1iII1iI ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  if '/app' in url :
   oOo0 ( ( i1I1i111Ii ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , I1IIIii + 'APK.png' )
def Iii1Iiii1iI1 ( url ) :
 i1iI1 = i11111IIIII ( url )
 III11I1 = url
 if "page=" in str ( url ) :
  III11I1 = url . split ( '?' ) [ 0 ]
 iI111i = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  if 'apk' in url :
   O0O0ooOOO ( ( i1I1i111Ii ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + Ooo0oOooo0 )
 if len ( IIi11i1i1iI1 ) > 1 :
  IIi11i1i1iI1 = str ( IIi11i1i1iI1 [ len ( IIi11i1i1iI1 ) - 1 ] )
 O0O0ooOOO ( 'Next Page' , III11I1 + str ( IIi11i1i1iI1 ) , 30037 , I1IIIii + 'Next.png' )
def ooooo0oo0OO ( name , url ) :
 i1iI1 = i1I1 ( url )
 name = name
 iI111i = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( i1iI1 )
 for url in iI111i :
  url = 'https://www.apkfiles.com' + url
  IIiIIII ( name , url , 'Brackets' )
def I1iI1I1111i ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'https://www.apkfiles.com/search?q=' + ( O0ooOO ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1oOOOOOOOoO = OooooOoO . lower ( )
 Iii1Iiii1iI1 ( i1oOOOOOOOoO )
 if 4 - 4: i1IiiiI1iI . I11i1ii1
def I1IIiiI1II ( url ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( I1I1i1ii11 , 'Download' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , i1I1i111Ii + '.apk' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 22 - 22: iI11I1II1I1I . i1iIi * O0Oooo0O
def I1I1IiI ( url ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , i1I1i111Ii + '.mp4' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 if 11 - 11: iiiiiiii1
def i1OooO00oO00o ( name , url , description ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , name )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 IIII1iI1IiIiI = xbmc . translatePath ( os . path . join ( I1i1iiI1 ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIII1iI1IiIiI
 print '======================================='
 extract . all ( II1iI1I11I , IIII1iI1IiIiI , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 43 - 43: IIiIiII11i
 if 95 - 95: O0Oooo0O + I11i1ii1 * iI11I1II1I1I
 if 17 - 17: oOo - I1ii11iIi11i * o0o00Oo0O / i1iIi
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . i1IiiiI1iI
 if 2 - 2: i1iIi
def oOoOOo ( ) :
 IIIi1I1IIii1II = i11111IIIII ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iI111i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , iiI , ooOO0ooo0o , oo0o0000 , Ii1i111iI in iI111i :
  O0O0ooOOO ( i1I1i111Ii , iiI , 80003 , ooOO0ooo0o , I1IIIii + 'APKToolsB.png' , Ii1i111iI )
def iII1ii ( apk , ret = None ) :
 if apk == "kodi" :
  OOO00OiI = "https://kodi.tv/download/"
  IIIi1I1IIii1II = i11111IIIII ( OOO00OiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iI111i = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( IIIi1I1IIii1II )
  if len ( iI111i ) == 1 :
   O0o00oO00O0 = iI111i [ 0 ] [ 0 ]
   o0OO0Oo = iI111i [ 0 ] [ 1 ]
   I1Iii = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( O0o00oO00O0 , o0OO0Oo )
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
def IIiIIII ( name , url , Brackets ) :
 if oOOo0O00o ( ) == 'android' :
  OOOOoOOOO = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not OOOOoOOOO : oOoO00o ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iiIi1 = name
  if OOOOoOOOO :
   if not os . path . exists ( oO ) : os . makedirs ( oO )
   if not I111IiiIi1 ( url ) == True : oOoO00o ( oOo0oooo00o , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % iiIi1 , '' , 'Please Wait' )
   II1iI1I11I = os . path . join ( oO , "%s.apk" % name )
   try : os . remove ( II1iI1I11I )
   except : pass
   downloader . download ( url , II1iI1I11I , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   if "Brackets" in Brackets :
    Ii1o0OOOoo0000 = zipfile . ZipFile ( II1iI1I11I )
    for file in Ii1o0OOOoo0000 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oO , os . path . basename ( file ) ) , 'wb' ) as o0OoOO :
       Oo0OOo = file . split ( '/' ) [ 1 ]
       o0OoOO . write ( Ii1o0OOOoo0000 . read ( file ) )
       xbmc . sleep ( 500 )
       o0OoOO . close ( )
       try :
        os . remove ( II1iI1I11I )
       except :
        pass
       II1iI1I11I = os . path . join ( oO , Oo0OOo )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + II1iI1I11I + '")' )
  else : oOoO00o ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oOoO00o ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 43 - 43: I11i1ii1 % i1iIi . OoOo0o / I1ii11iIi11i
 if 55 - 55: oOoO0o00OO0 % ii
 if 73 - 73: ooOoO0O00 - iiiiiiii1 % OOOo00oo0oO / ooOoO0O00 + IIiIiII11i + oOoO0o00OO0
 if 54 - 54: OOOo00oo0oO
def I1ii11I1IiI ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 IIIi1I1IIii1II = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( IIIi1I1IIii1II )
 for iiI , i1I1i111Ii in iI111i :
  iiI = ( ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + iiI )
  i1IIIii ( ( i1I1i111Ii ) . replace ( '_' , ' ' ) , iiI )
  if 37 - 37: iiiiiiii1 . ooo0O / i1iIi / OoOo0o * ooOoO0O00
def i1IIIii ( name , url ) :
 if oOOo0O00o ( ) == 'android' :
  OOOOoOOOO = iI111I11I1I1 . yesno ( oOo0oooo00o , "Would you like to download and install:" , "%s" % name )
  if not OOOOoOOOO : oOoO00o ( oOo0oooo00o , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iiIi1 = name
  if OOOOoOOOO :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not I111IiiIi1 ( url ) == True : oOoO00o ( oOo0oooo00o , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oO0 . create ( oOo0oooo00o , 'Downloading %s' % iiIi1 , '' , 'Please Wait' )
   II1iI1I11I = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( II1iI1I11I )
   except : pass
   downloader . download ( url , II1iI1I11I , o0oO0 )
   xbmc . sleep ( 500 )
   o0oO0 . close ( )
   iI111I11I1I1 . ok ( oOo0oooo00o , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + II1iI1I11I + '")' )
  else : oOoO00o ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oOoO00o ( oOo0oooo00o , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + OOOo00oo0oO
 if 58 - 58: iiiiiiii1 - ii
def o00oO00 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 5 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'INFO' )
 if 27 - 27: iiiiiiii1 . iii1i1iiiiIi / ii
 if 18 - 18: ooOoO0O00 . oOo0O0Ooo
def oO0o0O0Ooo0o ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( O00OOOoOoo0O + ( o0oOoO00o ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 30015 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 58 - 58: ooOoO0O00 + o0o00Oo0O . oOo % i1IiiiI1iI
def IIi1I1 ( url , iconimage , fanart ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iiI1ii1IIiI = url
 Ooo0oOooo0 = iconimage
 fanart = fanart
 iI111i = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for I1 , i1I1i111Ii in iI111i :
  if '.mp4' in i1I1i111Ii :
   O0O0ooOOO ( 'Watch VIDEO' , url + '/' + I1 , 222 , Ooo0oOooo0 , fanart , '' )
  if 'description' in i1I1i111Ii :
   O0O0ooOOO ( 'Read Description' , url + '/' + I1 , 30017 , Ooo0oOooo0 , fanart , '' )
  if 'images' in i1I1i111Ii :
   o00oOOooOOo0o ( 'View Images' , url + '/' + I1 , 30018 , Ooo0oOooo0 , fanart , '' )
  if 'url' in i1I1i111Ii :
   O0O0ooOOO ( 'Install Build On Android' , url + '/' + I1 , 30016 , Ooo0oOooo0 , fanart , '' )
  if 'url' in i1I1i111Ii :
   O0O0ooOOO ( 'Install Build On Pc' , url + '/' + I1 , 30019 , Ooo0oOooo0 , fanart , '' )
 O00oO000O0O ( 'movies' , 'INFO' )
 if 53 - 53: OOOo00oo0oO + iiiiiiii1
def oO0O0ooOoo ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( 'url="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in iI111i :
  Ii1i1I1iI11ii ( url )
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
 for i11I1i11IIIi in iI111i :
  OoOoO ( 'Description:' , i11I1i11IIIi )
  if 18 - 18: iii1i1iiiiIi
def O0o ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( url )
 url = url
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for I1 , i1I1i111Ii in iI111i :
  if 'png' in i1I1i111Ii :
   O0O0ooOOO ( 'image' , '' , '' , url + '/' + I1 , url + '/' + I1 , '' )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 1 - 1: ooo0O % ooo0O . iI11I1II1I1I . ii . I11i1ii1 . iiiiiiii1
def oooo ( name , url , description ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , name + '.zip' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 o0OO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oooiiI ( )
 if 65 - 65: I1ii11iIi11i . iii1i1iiiiIi . OoOo0o % ooo0O + oOo
 if 53 - 53: I1ii11iIi11i * i1IiiiI1iI - i1iIi % oOo - iii1i1iiiiIi - iiiiiiii1
def I1iiI ( url ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 o0OO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
 IiI11ii1I ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIIII ( )
 if 32 - 32: oOo . OOOo00oo0oO
def Ii1i1I1iI11ii ( url ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 o0OO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
 IiI11ii1I ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIIII ( )
 if 15 - 15: i1IiiiI1iI % oOo0O0Ooo - Ii / oOo / iii1i1iiiiIi + iii1i1iiiiIi
def oo000o ( name , url , description ) :
 o0OO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 II1iI1I11I = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oO0 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIIII ( )
 if 6 - 6: OoOo0o + oOoO0o00OO0 + I1ii11iIi11i
def oOOo0O00o ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def OOoOooOoOOOoo ( log ) :
 xbmc . log ( "[%s]: %s" % ( oOo0oooo00o , log ) )
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : o0OoOO = open ( Oo0o0000o0o0 , 'w' ) ; o0OoOO . close ( )
 with open ( Oo0o0000o0o0 , 'a' ) as o0OoOO :
  o0OOo0o0o0ooo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  o0OoOO . write ( o0OOo0o0o0ooo . rstrip ( '\r\n' ) + '\n' )
def II11IiIIiiiii ( msg , level = xbmc . LOGDEBUG ) :
 if not os . path . exists ( I11 ) : os . makedirs ( I11 )
 if not os . path . exists ( Oo0o0000o0o0 ) : o0OoOO = open ( Oo0o0000o0o0 , 'w' ) ; o0OoOO . close ( )
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
  o0OOoo = getS ( 'nextcleandate' ) if not getS ( 'nextcleandate' ) == '' else str ( TODAY )
  if CLEANWIZLOG == 'true' and o0OOoo <= str ( TODAY ) : checkLog ( )
  with open ( Oo0o0000o0o0 , 'a' ) as o0OoOO :
   o0OOo0o0o0ooo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , msg )
   o0OoOO . write ( o0OOo0o0o0ooo . rstrip ( '\r\n' ) + '\n' )
def IiIIII ( ) :
 iiI1IIIi = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iiI1IIIi == 0 : return
 elif iiI1IIIi == 1 : pass
 OOO = oOOo0O00o ( )
 OOoOooOoOOOoo ( "Platform: " + str ( OOO ) )
 os . _exit ( 1 )
 OOoOooOoOOOoo ( "Force close failed!  Trying alternate methods." )
 if OOO == 'osx' :
  OOoOooOoOOOoo ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OOO == 'linux' :
  OOoOooOoOOOoo ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OOO == 'android' :
  OOoOooOoOOOoo ( "############ try android force close #################" )
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
 elif OOO == 'windows' :
  OOoOooOoOOOoo ( "############ try windows force close #################" )
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
  OOoOooOoOOOoo ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  OOoOooOoOOOoo ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 52 - 52: oOo
  if 49 - 49: i1iIi . oOoO0o00OO0 % oOOoOooOo . I1ii11iIi11i * OoOo0o
  if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . oOOoOooOo
def II1I1Ii11 ( url ) :
 o0oO0 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( url ) :
  for file in oOOOOOoOOoo0 :
   if file . endswith ( ".xml" ) :
    o0oO0 . update ( 0 , "Fixing" , file , 'Please Wait' )
    iIIi = open ( ( os . path . join ( i11ii11IiI1 , file ) ) ) . read ( )
    I1iIi1i = iIIi . replace ( i1111 , 'special://home/' )
    o0OoOO = open ( ( os . path . join ( i11ii11IiI1 , file ) ) , mode = 'w' )
    o0OoOO . write ( str ( I1iIi1i ) )
    o0OoOO . close ( )
 IiIIII ( )
 if 7 - 7: iii1i1iiiiIi / iii1i1iiiiIi . O0Oooo0O * o0o00Oo0O + I11i1ii1 + OOOo00oo0oO
def IiIiIi1I1OooO00O0OO0oo ( ) :
 oOo0 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , I1IIIii + 'RadioNomy.png' )
 oOo0 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , I1IIIii + 'RadioNomy.png' )
 oOo0 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , I1IIIii + 'RadioNomy.png' )
 if 98 - 98: IIiIiII11i * I11i1ii1 - oOo0O0Ooo % ooo0O - iiiiiiii1 % oOoO0o00OO0
def Oo0Oo0o00oO ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def oO0o0OooOO0 ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
def iiIiooOo0oo0O0O ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in IIi11i1i1iI1 :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + i1I1i111Ii + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , I1IIIii + 'RadioNomy.png' )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + i1I1i111Ii + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , Ooo0oOooo0 )
def IIiii ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( i1iI1 )
 for url in iI111i :
  IIIIiii1IIii ( url )
def i1Ii11I1i ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO
 iI11IIi1iiI1I = 'https://www.radionomy.com/en/search/index?query=' + ( O0ooOO ) . replace ( ' ' , '+' )
 oOOo0 = i11111IIIII ( iI11IIi1iiI1I )
 iI111i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + i1I1i111Ii + '[/COLOR]' ) , ( o0oOoO00o ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + iiI , 70005 , Ooo0oOooo0 )
  if 83 - 83: I1ii11iIi11i / oOOoOooOo
  if 11 - 11: ooo0O - IIiIiII11i % OOOo00oo0oO . IIiIiII11i
def IiiIiiiiI1III ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.listenlive.eu/' + iiI , 10111113 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def I1iIi1IiI1i ( url ) :
 i1iI1 = i1I1 ( url )
 if 65 - 65: OOOo00oo0oO . Ii % OoOo0o * iiiiiiii1 % I1ii11iIi11i
 if 51 - 51: oOo % iiiiiiii1
 iI111i = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , IiiiiIiI , url , i1I1IiI1II1 in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' [COLORorangered] ' + i1I1IiI1II1 + '[/COLOR]' , url , 222225 , I1IIIii + 'WorldRadio.png' , I1IIIii + 'WorldRadio.png' , '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[CR]' + IiiiiIiI + '[CR]' + i1I1IiI1II1 + '[/COLOR]' )
  if 21 - 21: ii . o0o00Oo0O / Ii
def oOOOoo0 ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.toonjet.com/' + iiI , 8051 , I1IIIii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1i11II1i1i ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 in iI111i :
  if 'ol.gif' in Ooo0oOooo0 :
   pass
  elif 'link_block_' in Ooo0oOooo0 :
   pass
  elif '.png' in Ooo0oOooo0 :
   pass
  else :
   oOo0 ( ( Ooo0oOooo0 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , I1IIIii + 'vod.png' )
 for url in IIi11i1i1iI1 :
  oOo0 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , I1IIIii + 'Next.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0O0O00OoO0O ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( i1iI1 )
 for url in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , I1IIIii + 'classictoons.png' )
  if 22 - 22: i1IiiiI1iI - ooo0O
  if 54 - 54: OOOo00oo0oO * oOo - iiiiiiii1 * i1IiiiI1iI + ooo0O - i1iIi
def iI1I11 ( ) :
 i1I1ii1 ( 'Audio Books' , '' , 30011 , I1IIIii + 'AudioBooks.png' , I1IIIii + 'AudioBooks.png' , '' )
 i1I1ii1 ( 'Kids Audio Books' , '' , 30006 , I1IIIii + 'KidsAudioBooks.png' , I1IIIii + 'KidsAudioBooks.png' , '' )
 if 92 - 92: oOo0O0Ooo / oOo - OoOo0o / Ii
def IiIi1 ( ) :
 i1I1ii1 ( 'All' , '' , 30001 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 i1I1ii1 ( 'Popular' , '' , 30012 , I1IIIii + 'POPULARv.png' , I1IIIii + 'POPULARv.png' , '' )
 i1I1ii1 ( 'Search' , '' , 30013 , I1IIIii + 'Search.png' , I1IIIii + 'Search.png' , '' )
 if 45 - 45: oOOoOooOo + IIiIiII11i % iiiiiiii1
def o00OoOo0 ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for i1I1i111Ii , iiI , Iii1I in iI111i :
  if 'Parent' in i1I1i111Ii :
   pass
  elif '2' in Iii1I :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiI , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 33 - 33: OoOo0o / OOOo00oo0oO . Ii * iI11I1II1I1I
def o0O0ooo0o ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for i1I1i111Ii , iiI , Iii1I in iI111i :
  if O0ooOO in i1I1i111Ii . lower ( ) :
   if '1' in Iii1I :
    i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiI , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '2' in Iii1I :
    i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiI , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   elif '3' in Iii1I :
    i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiI , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 55 - 55: oOOoOooOo . I11i1ii1 * ooOoO0O00 . i1iIi
    if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + i1iIi % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def oo000O ( ) :
 oOOo0 = i11111IIIII ( OOO00 + 'books' + OOOO )
 iI111i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOo0 )
 for i1I1i111Ii , iiI , Iii1I in iI111i :
  if '1' in Iii1I :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiI , 3010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '2' in Iii1I :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiI , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '3' in Iii1I :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiI , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 97 - 97: ii * ooo0O + ii % i1iIi * I1ii11iIi11i
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 35 - 35: iI11I1II1I1I % iiiiiiii1 - ooOoO0O00
def I1i1iI1I1II ( url ) :
 I1 = url
 oOOo0 = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii in IIi11i1i1iI1 :
  if 'mp3' in i1I1i111Ii :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1 + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in i1I1i111Ii :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1 + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in i1I1i111Ii :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1 + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif '/' in i1I1i111Ii :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 30009 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 20 - 20: iii1i1iiiiIi
   if 1 - 1: O0Oooo0O * oOo - iiiiiiii1
   if 97 - 97: iiiiiiii1 . oOoO0o00OO0 - iI11I1II1I1I . oOOoOooOo + oOo0O0Ooo % OOOo00oo0oO
def Ii1i1 ( url ) :
 oOOo0 = i11111IIIII ( url )
 I1 = url
 iI111i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  if 'Parent' in i1I1i111Ii :
   pass
  elif '.db' in i1I1i111Ii :
   pass
  elif '.jpg' in i1I1i111Ii :
   pass
  elif '.html' in i1I1i111Ii :
   pass
  elif '.doc' in i1I1i111Ii :
   pass
  elif 'mp3' in i1I1i111Ii :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in i1I1i111Ii :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 30010 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 6 - 6: iI11I1II1I1I * IIiIiII11i
   if 38 - 38: oOo0O0Ooo
def iiiii1i1 ( ) :
 i1I1ii1 ( 'A-Z' , '' , 30007 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 i1I1ii1 ( 'All' , '' , 30003 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 i1I1ii1 ( 'Search' , '' , 30014 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
 if 87 - 87: I11i1ii1 - o0o00Oo0O + oOo0O0Ooo / ii * iiiiiiii1 / ooOoO0O00
def II11II1i ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 in iI111i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iiI + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in Ooo0oOooo0 :
   pass
  else :
   i1I1ii1 ( Ooo0oOooo0 , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iiI ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + Ooo0oOooo0 + '.gif' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 56 - 56: i1iIi * Ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: IIiIiII11i - o0o00Oo0O . O0Oooo0O
 if 59 - 59: iii1i1iiiiIi
def iiII1iiI ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  if '</a>' in i1I1i111Ii :
   pass
  elif '(' in i1I1i111Ii :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: Ii - i1IiiiI1iI / oOOoOooOo / ooo0O * Ii * ooo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: ii % o0o00Oo0O - OoOo0o / ooo0O / oOo0O0Ooo
def Iii1iIII1Iii ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if O0ooOO in i1I1i111Ii . lower ( ) :
   if '</a>' in i1I1i111Ii :
    pass
   elif '(' in i1I1i111Ii :
    i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiI , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   else :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiI , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
    if 13 - 13: iI11I1II1I1I - OoOo0o
    if 14 - 14: oOOoOooOo
def Ooo0OO00oo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI111i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if '</a>' in i1I1i111Ii :
   pass
  elif '(' in i1I1i111Ii :
   i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiI , 30005 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiI , 30004 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 21 - 21: i1IiiiI1iI
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: oOo / OoOo0o - ooOoO0O00 + ooOoO0O00 - I11i1ii1 + I11i1ii1
 if 67 - 67: oOo * oOo / ii
def OOooooo0O0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oOOo0 )
 for url in iI111i :
  I1 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I1 )
  if 7 - 7: ooOoO0O00 / I11i1ii1 / iiiiiiii1
def oOo0OO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url in iI111i :
  if '<p align' in i1I1i111Ii :
   pass
  elif '&nbsp;' in i1I1i111Ii :
   pass
  else :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , o0oOoO00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , I1IIIii + 'KodibleAudioBooks.png' , I1IIIii + 'KodibleAudioBooks.png' , '' )
   if 56 - 56: IIiIiII11i . IIiIiII11i + I11i1ii1 . ooo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: oOOoOooOo . I11i1ii1 . IIiIiII11i
 if 25 - 25: I11i1ii1 * O0Oooo0O - OOOo00oo0oO * Ii * oOo0O0Ooo * OoOo0o
def Ooii1II11IIII ( ) :
 oOOo0 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 iI111i = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if 'ongoing' in iiI :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 21005 , I1IIIii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in iiI :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 21005 , I1IIIii + 'CartoonShows.png' , '' , '' )
  if 'disney' in iiI :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 21005 , I1IIIii + 'Disney.png' , '' , '' )
  if 'genre' in iiI :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 21005 , I1IIIii + 'Genre.png' , '' , '' )
  if 'years' in iiI :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 21005 , I1IIIii + 'Years.png' , '' , '' )
def oO0OOOO0o0o0 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIIiiiiiI1I = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , Ooo0oOooo0 , Ooo0oOooo0 , i1I1i111Ii )
 for url , i1I1i111Ii in IIIiiiiiI1I :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in next :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , I1IIIii + 'Next.png' , '' , '' )
def ii11Ii1iii1I1 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 III11 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 Oo0OooO00oOo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oOOo0 )
 I1I111iIiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url in Oo0OooO00oOo :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 for url , i1I1i111Ii in III11 :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
 else :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , I1IIIii + 'watchcartoons.png' , '' , '' )
def I1Ii11I1i1iii ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 222 , I1IIIii + 'watchcartoons.png' , '' , '' )
  if 83 - 83: o0o00Oo0O / oOo
def o0O000O00o ( ) :
 oOOo0 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 iI111i = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if '9cart' in iiI :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 20001 , I1IIIii + 'ORIGINCARTOON.png' )
   if 38 - 38: ii . iiiiiiii1
def iiII11 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oOOo0 )
 OOoOOO000O0 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if '9cart' in url :
   oOo0 ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url in IIi11i1i1iI1 :
  if '9cart' in url :
   oOo0 ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
 for url , i1I1i111Ii in OOoOOO000O0 :
  if '9cart' in url :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
   if 89 - 89: oOoO0o00OO0 * oOoO0o00OO0 * iii1i1iiiiIi / iiiiiiii1
def OOo0i111ii1Ii ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 20003 , Ooo0oOooo0 )
 for url , i1I1i111Ii in IIi11i1i1iI1 :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , I1IIIii + 'ORIGINCARTOON.png' )
  if 59 - 59: o0o00Oo0O . ooo0O % oOoO0o00OO0 * OOOo00oo0oO + i1IiiiI1iI
def o00oIiIiIiiI ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a href="([^"]*)">' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'Watch' in url :
   oOo0 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , I1IIIii + 'ORIGINCARTOON.png' )
   if 83 - 83: iii1i1iiiiIi
def o0ooOOOo0O0 ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 20005 , I1IIIii + 'ORIGINCARTOON.png' )
  if 100 - 100: Ii . OoOo0o . Ii
def o00Oo ( url ) :
 url = cloudflare . source ( url )
 o00oOOo ( url )
 if 20 - 20: i1iIi . I1ii11iIi11i - i1IiiiI1iI % i1IiiiI1iI - oOo0O0Ooo * OoOo0o
def OooOo ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . recompile ( 'src="([^"]*)"' )
 for url in iI111i :
  o00oOOo ( url )
  if 67 - 67: ooo0O / ii % IIiIiII11i % OOOo00oo0oO
  if 5 - 5: oOo . oOoO0o00OO0 . Ii
def iIIIII ( url , name ) :
 url = url ; name = name
 oooI11Ii1 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oooI11Ii1 . clear ( )
 oO0O = [ ]
 OOOoooooO0oOOoO = [ ]
 IIiI = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIiI )
 for Ooo0oOooo0 in IIi11i1i1iI1 :
  I1I1oOoooo0OooO = Ooo0oOooo0
 OOoOOO000O0 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IIiI )
 for OooO0O , Oo0o in OOoOOO000O0 :
  oO0O . append ( [ OooO0O , Oo0o ] )
  if len ( oO0O ) == len ( OOoOOO000O0 ) :
   for ii1IIII in oO0O :
    O0OO0 = random . randint ( 1 , len ( oO0O ) )
    try :
     OOI1i11i = oO0O [ int ( O0OO0 ) ]
     if OOI1i11i [ 1 ] not in OOOoooooO0oOOoO :
      OOOoooooO0oOOoO . append ( OOI1i11i [ 1 ] )
      o0Oo0oO = i11111IIIII ( OOI1i11i [ 0 ] )
      IiIIiii11II1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( o0Oo0oO )
      for iiiI1I , OOOOo0o0O0 in IiIIiii11II1 :
       if 'easy' in OOOOo0o0O0 :
        I1I1i1 = i11111IIIII ( OOOOo0o0O0 )
        iiii1i1II1 = re . compile ( 'file: "(.+?)"' ) . findall ( I1I1i1 )
        for Ii1Ii in iiii1i1II1 :
         if 'http' in Ii1Ii :
          ooooo0OoO0 = xbmcgui . ListItem ( OOI1i11i [ 1 ] , iconImage = I1I1oOoooo0OooO , thumbnailImage = I1I1oOoooo0OooO )
          ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : OOI1i11i [ 1 ] } )
          ooooo0OoO0 . setProperty ( "IsPlayable" , "true" )
          oooI11Ii1 . add ( Ii1Ii , ooooo0OoO0 )
          xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooooo0OoO0 )
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
   if 15 - 15: o0o00Oo0O
def O0OOoOOooO ( url ) :
 oooI11Ii1 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oooI11Ii1 . clear ( )
 i1111II1iIII = [ ]
 I1ii11ii1iiI = [ ]
 oO0oo0 = [ ]
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  I1ii11ii1iiI . append ( [ url , i1I1i111Ii ] )
  if len ( I1ii11ii1iiI ) == len ( iI111i ) :
   for ii1IIII in I1ii11ii1iiI :
    IiIiI1 = random . randint ( 1 , len ( I1ii11ii1iiI ) )
    try :
     iiiI1 = I1ii11ii1iiI [ int ( IiIiI1 ) ]
    except :
     pass
    if iiiI1 [ 1 ] not in oO0oo0 :
     oO0oo0 . append ( iiiI1 [ 1 ] )
     if int ( len ( i1111II1iIII ) ) < 1 :
      i1111II1iIII . append ( iiiI1 [ 1 ] [ 0 ] )
      iIIIII ( iiiI1 [ 0 ] , iiiI1 [ 1 ] )
     else :
      pass
    else :
     pass
  else :
   pass
   if 29 - 29: I1ii11iIi11i / iiiiiiii1 + i1iIi - oOo
def IIIiIIIi111iI ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 ooo0oo00O00oO = sys . argv [ 0 ]
 ooo0oo00O00oO += '?mode=' + str ( mode )
 ooo0oo00O00oO += '&title=' + urllib . quote_plus ( name )
 ooo0oo00O00oO += '&image=' + urllib . quote_plus ( image )
 ooo0oo00O00oO += '&page=' + str ( page )
 if url != '' :
  ooo0oo00O00oO += '&url=' + urllib . quote_plus ( url )
 if keyword :
  ooo0oo00O00oO += '&keyword=' + urllib . quote_plus ( keyword )
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  ooooo0OoO0 . addContextMenuItems ( contextMenu )
 if infoLabels :
  ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  ooooo0OoO0 . setProperty ( "IsPlayable" , "true" )
 ooooo0OoO0 . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = isFolder )
 if 41 - 41: OOOo00oo0oO % oOo0O0Ooo % I1ii11iIi11i + i1iIi + Ii
def o0oiIiI1i1iiIi1i ( ) :
 iI1IiII1II1I = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 i1iI1 = i11111IIIII ( iI1IiII1II1I )
 iI111i = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  IIIiIIIi111iI ( i1I1i111Ii , 9110012 , url = iiI , image = O0O , isFolder = False )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 99 - 99: oOOoOooOo / oOo0O0Ooo . i1iIi - i1iIi * oOo0O0Ooo
def OoOi111i ( ) :
 iI1IiII1II1I = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , '' , 10004 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 O0OOoOOO0oO ( '[COLOR' + iiI1IiI + ']24/7 Select Cartoon[/COLOR]' , '' , 9110011 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' , '' )
 IIIiIIIi111iI ( '[COLOR' + iiI1IiI + ']24/7 Random Cartoon[/COLOR]' , 9110010 , url = iI1IiII1II1I , image = I1IIIii + 'Kids.png' , isFolder = False )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 if 24 - 24: i1IiiiI1iI * oOo - OOOo00oo0oO / iI11I1II1I1I - I1ii11iIi11i . OoOo0o
def I111ii1III1I ( ) :
 iI1IiII1II1I = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 oOOo0 = i11111IIIII ( iI1IiII1II1I )
 if 2 - 2: oOOoOooOo - o0o00Oo0O - oOoO0o00OO0 / i1IiiiI1iI * iii1i1iiiiIi
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oOOo0 )
 if 26 - 26: oOoO0o00OO0 + O0Oooo0O - OOOo00oo0oO + I11i1ii1 % OoOo0o
 for iiI , i1I1i111Ii in iI111i :
  if O0ooOO in i1I1i111Ii . lower ( ) :
   if 'Dad!' in i1I1i111Ii :
    pass
   elif 'Family Guy' in i1I1i111Ii :
    pass
   elif '2 Stupid' in i1I1i111Ii :
    pass
   elif 'The Zelfs' in i1I1i111Ii :
    pass
   elif 'A Clone' in i1I1i111Ii :
    pass
   elif 'A.T.O.M' in i1I1i111Ii :
    pass
   elif 'Almost Naked' in i1I1i111Ii :
    pass
   elif 'Angry Kid' in i1I1i111Ii :
    pass
   elif 'Annoying Orange' in i1I1i111Ii :
    pass
   elif 'Aqua Teen' in i1I1i111Ii :
    pass
   elif 'Assy Mcgee' in i1I1i111Ii :
    pass
   elif 'Astroblast' in i1I1i111Ii :
    pass
   elif 'Atomic Betty' in i1I1i111Ii :
    pass
   elif 'Axe Cop' in i1I1i111Ii :
    pass
   elif 'Baby Playpen' in i1I1i111Ii :
    pass
   elif 'Beavis and Butt' in i1I1i111Ii :
    pass
   elif 'Celebrity Deathmatch' in i1I1i111Ii :
    pass
   elif 'Clerks The' in i1I1i111Ii :
    pass
   elif 'Crapston Villas' in i1I1i111Ii :
    pass
   elif 'Duckman:' in i1I1i111Ii :
    pass
   elif 'Stripperella' in i1I1i111Ii :
    pass
   elif 'Vixen' in i1I1i111Ii :
    pass
   else :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 10006 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
    if 84 - 84: i1IiiiI1iI % i1iIi % o0o00Oo0O * ooo0O
    if 15 - 15: OOOo00oo0oO - iI11I1II1I1I - IIiIiII11i - I11i1ii1 % oOoO0o00OO0
    if 80 - 80: I11i1ii1 * iiiiiiii1 . ooOoO0O00 % i1iIi % oOoO0o00OO0 + oOOoOooOo
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 6 - 6: oOoO0o00OO0 . OOOo00oo0oO . oOo + I11i1ii1
def oO0oo0O0OOOo0 ( url ) :
 iI1IiII1II1I = o0oOoO00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 i1iI1 = i11111IIIII ( iI1IiII1II1I )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  if 'Dad!' in i1I1i111Ii :
   pass
  elif 'Family Guy' in i1I1i111Ii :
   pass
  elif '2 Stupid' in i1I1i111Ii :
   pass
  elif 'The Zelfs' in i1I1i111Ii :
   pass
  elif 'A Clone' in i1I1i111Ii :
   pass
  elif 'A.T.O.M' in i1I1i111Ii :
   pass
  elif 'Almost Naked' in i1I1i111Ii :
   pass
  elif 'Angry Kid' in i1I1i111Ii :
   pass
  elif 'Annoying Orange' in i1I1i111Ii :
   pass
  elif 'Aqua Teen' in i1I1i111Ii :
   pass
  elif 'Assy Mcgee' in i1I1i111Ii :
   pass
  elif 'Astroblast' in i1I1i111Ii :
   pass
  elif 'Atomic Betty' in i1I1i111Ii :
   pass
  elif 'Axe Cop' in i1I1i111Ii :
   pass
  elif 'Baby Playpen' in i1I1i111Ii :
   pass
  elif 'Beavis and Butt' in i1I1i111Ii :
   pass
  elif 'Celebrity Deathmatch' in i1I1i111Ii :
   pass
  elif 'Clerks The' in i1I1i111Ii :
   pass
  elif 'Crapston Villas' in i1I1i111Ii :
   pass
  elif 'Duckman:' in i1I1i111Ii :
   pass
  elif 'Stripperella' in i1I1i111Ii :
   pass
  elif 'Vixen' in i1I1i111Ii :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 10006 , I1IIIii + 'Kids.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: oOo0O0Ooo
def I1IIi11I1IiIi ( url ) :
 i1iI1 = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( i1iI1 )
 for Ooo0oOooo0 in IIi11i1i1iI1 :
  I1I1oOoooo0OooO = Ooo0oOooo0
 OOoOOO000O0 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( i1iI1 )
 for url in OOoOOO000O0 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 10007 , I1I1oOoooo0OooO )
  if 56 - 56: OOOo00oo0oO + ooOoO0O00 * iiiiiiii1 - o0o00Oo0O
  if 84 - 84: iiiiiiii1 % oOo0O0Ooo / iI11I1II1I1I * i1iIi * iI11I1II1I1I + oOoO0o00OO0
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 78 - 78: I11i1ii1 / iiiiiiii1 * i1iIi . OoOo0o . OOOo00oo0oO - O0Oooo0O
def I1IiI11 ( url , IMAGE ) :
 IiIiIi = [ ]
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i1iI1 )
 for i1I1i111Ii , I1 in iI111i :
  if 'panda' in I1 :
   oOOo0 = i11111IIIII ( I1 )
   IIi11i1i1iI1 = re . compile ( "url: '(.+?)'" ) . findall ( oOOo0 )
   for iiIiiIi1 in IIi11i1i1iI1 :
    if 'http' in iiIiiIi1 :
     IiIiIi . append ( { 'source' : 'playpanda' , 'quality' : 'SD' , 'url' : iiIiiIi1 } )
  elif 'easy' in I1 :
   oo00O00oO = i11111IIIII ( I1 )
   OOoOOO000O0 = re . compile ( 'file: "(.+?)"' ) . findall ( oo00O00oO )
   for iiIiiIi1 in OOoOOO000O0 :
    if 'http' in iiIiiIi1 :
     IiIiIi . append ( { 'source' : 'easyvideo' , 'quality' : 'SD' , 'url' : iiIiiIi1 } )
  elif 'zoo' in I1 :
   iIiIIIi = i11111IIIII ( I1 )
   IiIIiii11II1 = re . compile ( 'src: "(.+?)"' ) . findall ( iIiIIIi )
   for iiIiiIi1 in IiIIiii11II1 :
    if 'http' in iiIiiIi1 :
     IiIiIi . append ( { 'source' : 'videozoo' , 'quality' : 'SD' , 'url' : iiIiiIi1 } )
 if len ( IiIiIi ) >= 3 :
  iiI1IIIi = iI111I11I1I1 . select ( 'Select Playlink' ,
 [ IIIi1I1IIii1II [ "source" ] + " - " + " (" + IIIi1I1IIii1II [ "quality" ] + ")"
 for IIIi1I1IIii1II in IiIiIi ] )
  if iiI1IIIi != - 1 :
   url = IiIiIi [ iiI1IIIi ] [ 'url' ]
   ooOoOO = False
   xbmc . Player ( ) . play ( url )
   if 42 - 42: i1IiiiI1iI
   if 23 - 23: iii1i1iiiiIi . oOo
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 29 - 29: i1IiiiI1iI
def i11III ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( i1iI1 )
 for url in iI111i :
  IIIIiii1IIii ( url )
  if 10 - 10: iiiiiiii1 % O0Oooo0O * oOoO0o00OO0 * o0o00Oo0O * Ii % O0Oooo0O
  if 68 - 68: ii * iii1i1iiiiIi
  if 9 - 9: O0Oooo0O
def I1II ( ) :
 if 93 - 93: oOOoOooOo / OoOo0o * o0o00Oo0O
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , I1IIIii + 'StandUp.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , I1IIIii + 'SearchComedian.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , I1IIIii + 'Others.png' , Oo00OOOOO , '' )
 if 17 - 17: oOo / oOOoOooOo % oOo0O0Ooo
def IIiI1IiI1iIi1 ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  if 'elete' in i1I1i111Ii :
   pass
  else :
   II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 222 , Ooo0oOooo0 )
   if 30 - 30: iiiiiiii1
def iIOO000O ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0OO0ooO0oO0O0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , o00O00o , i1iII1IiiIiI1 in O0OO0ooO0oO0O0 :
  for O0ooOO in o00O00o :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   ooO0O00O0O0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iiI , i1I1i111Ii in ooO0O00O0O0 :
    if 'tube' in iiI :
     pass
    elif 'stage' in iiI :
     II1i11I1 ( '[COLOR' + iiI1IiI + ']' + o00O00o + '   -   ' + i1I1i111Ii + '[/COLOR]' , ( iiI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + Ooo0oOooo0 , )
    elif 'vee' in iiI :
     pass
     if 24 - 24: iI11I1II1I1I % I1ii11iIi11i % Ii
def ooOoo00OoO00 ( ) :
 oOOo0 = i11111IIIII ( ( o0oOoO00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0OO0ooO0oO0O0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , o00O00o , i1iII1IiiIiI1 in O0OO0ooO0oO0O0 :
  ooO0O00O0O0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iiI , i1I1i111Ii in ooO0O00O0O0 :
   if 'tube' in iiI :
    pass
   elif 'stage' in iiI :
    II1i11I1 ( '[COLOR' + iiI1IiI + ']' + o00O00o + '   -   ' + i1I1i111Ii + '[/COLOR]' , ( iiI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + Ooo0oOooo0 )
   elif 'vee' in iiI :
    pass
    if 69 - 69: o0o00Oo0O . O0Oooo0O - o0o00Oo0O
    if 58 - 58: iii1i1iiiiIi + oOoO0o00OO0
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: IIiIiII11i % OOOo00oo0oO + ooo0O / Ii
def OO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iIiiIi11IIi = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOo0 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( iIiiIi11IIi ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in iIiiIi11IIi :
  O0O0oo ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 16 - 16: oOo0O0Ooo . OOOo00oo0oO . OoOo0o % oOOoOooOo - OoOo0o - ooo0O
  if 30 - 30: I11i1ii1
  if 34 - 34: OOOo00oo0oO - IIiIiII11i - ooo0O + iiiiiiii1 + O0Oooo0O
  if 70 - 70: ii + oOo * I1ii11iIi11i
  if 20 - 20: Ii - IIiIiII11i - oOOoOooOo % OOOo00oo0oO . oOOoOooOo
  if 50 - 50: iI11I1II1I1I + O0Oooo0O - i1IiiiI1iI - ii
  if 84 - 84: iii1i1iiiiIi - i1IiiiI1iI
def IIiiI1iIiIi ( ) :
 if 80 - 80: Ii % OoOo0o - I1ii11iIi11i % OoOo0o
 O0O0oOo0o0o0 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 O0O0oOo0o0o0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 86 - 86: ooo0O / iii1i1iiiiIi
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 40 - 40: iiiiiiii1
def o000 ( ) :
 O0O0oOo0o0o0 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 O0O0oOo0o0o0 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 85 - 85: ooOoO0O00 % ooo0O * oOoO0o00OO0 * oOo . IIiIiII11i
 O00oO000O0O ( 'movies' , 'MAIN' )
def O000 ( ) :
 if 18 - 18: oOOoOooOo + O0Oooo0O / OoOo0o / OOOo00oo0oO + iI11I1II1I1I % I11i1ii1
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 Ooo00O0 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 94 - 94: i1IiiiI1iI
 for ii1o0oo0Ooooo0 in Ooo00O0 :
  Oo0oOo000OoO0 = Ii1iIiII1ii1 + '/Movies/a.to.z/' + ii1o0oo0Ooooo0 + '.php'
  oOOo0 = i1Oo00 ( Oo0oOo000OoO0 )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in iI111i :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    if '.php' in iiI :
     i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
     o00oOOooOOo0o ( i1I1i111Ii , iiI , 426 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    else :
     i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
     iI11IiiI1 ( i1I1i111Ii , iiI , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
     if 83 - 83: OOOo00oo0oO / iI11I1II1I1I
     O00oO000O0O ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 68 - 68: O0Oooo0O - iii1i1iiiiIi . Ii + ooo0O
def Oo0oo ( ) :
 if 33 - 33: oOo0O0Ooo / i1IiiiI1iI . I1ii11iIi11i
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 Ooo00O0 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 if 89 - 89: iiiiiiii1 + ooOoO0O00 - I11i1ii1 + oOOoOooOo . IIiIiII11i
 for ii1o0oo0Ooooo0 in Ooo00O0 :
  Oo00oOOO0 = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + ii1o0oo0Ooooo0 + '.php'
  oOOo0 = i1Oo00 ( Oo00oOOO0 )
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
  for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in iI111i :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    if '.php' in iiI :
     i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
     o00oOOooOOo0o ( i1I1i111Ii , iiI , 426 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    else :
     i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
     iI11IiiI1 ( i1I1i111Ii , iiI , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
     if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
     O00oO000O0O ( 'movies' , 'MAIN' )
     xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
     if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . iiiiiiii1 / iiiiiiii1
     if 43 - 43: oOo0O0Ooo
def OOOooOOO00O ( ) :
 if 34 - 34: i1iIi * i1IiiiI1iI / ii - iI11I1II1I1I
 i1iI1 = i11111IIIII ( Ii1iIiII1ii1 + 'spongemain.php' )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , ooo0O0o00O , iiI , Ooo0oOooo0 , oo0o0000 , I11iiii1I in iI111i :
  O0O0oOo0o0o0 ( i1I1i111Ii , iiI , I11iiii1I , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
  O00oO000O0O ( 'movies' , 'MAIN' )
def O0Ooo00o0OoOo ( url ) :
 if 96 - 96: I11i1ii1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 O0ooOooOOoo = ( '%s%s' % ( iI1IiII1II1I , url ) )
 IIIi1I1IIii1II = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in iI111i :
  if '.php' in url :
   IIii1I1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for ii1IIII in IIii1I1i :
    if ii1IIII == url :
     i1I1i111Ii = ( '[COLORred]Watched - [/COLOR]' + i1I1i111Ii ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   o00oOOooOOo0o ( i1I1i111Ii , url , 426 , i1I , oOoOo0OOOOO , ooo0O0o00O )
  else :
   IIii1I1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
   for ii1IIII in IIii1I1i :
    if ii1IIII == url :
     i1I1i111Ii = ( '[COLORred]Watched - [/COLOR]' + i1I1i111Ii ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
   iI11IiiI1 ( i1I1i111Ii , url , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
   if 31 - 31: I1ii11iIi11i - oOOoOooOo - iii1i1iiiiIi + oOOoOooOo * oOo / OOOo00oo0oO
   O00oO000O0O ( 'movies' , 'MAIN' )
   if 45 - 45: iI11I1II1I1I - I1ii11iIi11i . i1IiiiI1iI - I1ii11iIi11i / oOOoOooOo / ooo0O
   xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 81 - 81: iiiiiiii1 - i1IiiiI1iI
   if 20 - 20: ooOoO0O00
def Iiiii1I ( url ) :
 if 3 - 3: iii1i1iiiiIi
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , ooo0O0o00O , url , Ooo0oOooo0 , oo0o0000 , I11iiii1I in iI111i :
  O0O0oOo0o0o0 ( i1I1i111Ii , url , I11iiii1I , Ooo0oOooo0 , oo0o0000 , ooo0O0o00O )
  if 52 - 52: iii1i1iiiiIi
  O00oO000O0O ( 'movies' , 'MAIN' )
  if 79 - 79: oOo0O0Ooo + I1ii11iIi11i % iii1i1iiiiIi - I11i1ii1 + oOo0O0Ooo * OOOo00oo0oO
  if 52 - 52: iii1i1iiiiIi % oOoO0o00OO0 * I1ii11iIi11i % ii - oOo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: OoOo0o . i1iIi / i1IiiiI1iI
def iI11IiiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 93 - 93: oOOoOooOo * oOo0O0Ooo * oOoO0o00OO0 / oOoO0o00OO0
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1II1i = [ ]
  i1II1i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   i1II1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   i1II1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooooo0OoO0 . addContextMenuItems ( i1II1i )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = False )
 return oOO
 if 62 - 62: oOOoOooOo * i1iIi % oOoO0o00OO0 - ooOoO0O00 - oOoO0o00OO0
def O0O0oOo0o0o0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 24 - 24: OoOo0o
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1II1i = [ ]
  i1II1i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   i1II1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   i1II1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooooo0OoO0 . addContextMenuItems ( i1II1i )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = True )
 return oOO
if 71 - 71: I11i1ii1 - ooOoO0O00
if 56 - 56: iii1i1iiiiIi + OOOo00oo0oO
if 74 - 74: iiiiiiii1 / O0Oooo0O / IIiIiII11i - iiiiiiii1 / OOOo00oo0oO % i1IiiiI1iI
if 19 - 19: I11i1ii1 % ii + ii
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
def IIIIiI1iiI ( string ) :
 if O00O0oOO00O00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 13 - 13: i1IiiiI1iI . oOo
def O00oO0oOOOOOO ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 Oo0ooo00OoO = [ ]
 try :
  if 1 - 1: ii * iI11I1II1I1I / oOoO0o00OO0 * i1IiiiI1iI
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( oo0OooOOo0 ) == False :
  IIIIiI1iiI ( 'Making Favorites File' )
  Oo0ooo00OoO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iIIi = open ( oo0OooOOo0 , "w" )
  iIIi . write ( json . dumps ( Oo0ooo00OoO ) )
  iIIi . close ( )
 else :
  IIIIiI1iiI ( 'Appending Favorites' )
  iIIi = open ( oo0OooOOo0 ) . read ( )
  I1i1I1i1Ii = json . loads ( iIIi )
  I1i1I1i1Ii . append ( ( name , url , iconimage , fanart , mode ) )
  I1iIi1i = open ( oo0OooOOo0 , "w" )
  I1iIi1i . write ( json . dumps ( I1i1I1i1Ii ) )
  I1iIi1i . close ( )
  if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
  if 43 - 43: I1ii11iIi11i / O0Oooo0O / ooOoO0O00
def I1i11IIiiIiI ( ) :
 if os . path . exists ( oo0OooOOo0 ) == False :
  Oo0ooo00OoO = [ ]
  IIIIiI1iiI ( 'Making Favorites File' )
  Oo0ooo00OoO . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  iIIi = open ( oo0OooOOo0 , "w" )
  iIIi . write ( json . dumps ( Oo0ooo00OoO ) )
  iIIi . close ( )
 else :
  II1iiiiI1Ii11 = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
  Ii1II = len ( II1iiiiI1Ii11 )
  for O0oo in II1iiiiI1Ii11 :
   i1I1i111Ii = O0oo [ 0 ]
   iiI = O0oo [ 1 ]
   i1I = O0oo [ 2 ]
   try :
    III1II1iiI11 = O0oo [ 3 ]
    if III1II1iiI11 == None :
     raise
   except :
    if O0oo0OO0 . getSetting ( 'use_thumb' ) == "true" :
     III1II1iiI11 = i1I
    else :
     III1II1iiI11 = oo0o0000
   try : iiIiooO00Oo = O0oo [ 5 ]
   except : iiIiooO00Oo = None
   try : IIiI1iiIII1 = O0oo [ 6 ]
   except : IIiI1iiIII1 = None
   if 68 - 68: Ii . oOOoOooOo % i1IiiiI1iI
   if O0oo [ 4 ] == 0 :
    o00oOOooOOo0o ( i1I1i111Ii , iiI , '' , i1I , oo0o0000 , '' , 'fav' )
   else :
    o00oOOooOOo0o ( i1I1i111Ii , iiI , O0oo [ 4 ] , i1I , oo0o0000 , '' , 'fav' )
    if 47 - 47: iii1i1iiiiIi . ooOoO0O00
def iiooo0o0oO ( name ) :
 I1i1I1i1Ii = json . loads ( open ( oo0OooOOo0 ) . read ( ) )
 for IiI1i111IiIiIi1 in range ( len ( I1i1I1i1Ii ) ) :
  if I1i1I1i1Ii [ IiI1i111IiIiIi1 ] [ 0 ] == name :
   del I1i1I1i1Ii [ IiI1i111IiIiIi1 ]
   I1iIi1i = open ( oo0OooOOo0 , "w" )
   I1iIi1i . write ( json . dumps ( I1i1I1i1Ii ) )
   I1iIi1i . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 19 - 19: I1ii11iIi11i - oOo + Ii / iI11I1II1I1I
 if 1 - 1: I11i1ii1 % ooOoO0O00
def O00oIi11Iiii1iiii ( ) :
 IIiII1iII11Ii = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 oooO00o = open ( IIiII1iII11Ii , "w+" )
 oOOo0 = i11111IIIII ( 'http://piesustv' + Ooo + ':8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 iI111i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oOOo0 )
 oooO00o . write ( r'[' + o0OOO + ']' + '\n' )
 for i1I1i111Ii , Ooo0oOooo0 , oOOOoo00 , iiI in iI111i :
  iiI = ( iiI + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  OooO0o000Oo = ( i1I1i111Ii + '=plugin://' + o0OOO + '/?url=' + iiI + '&mode=10012&name=' + ( i1I1i111Ii ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( Ooo0oOooo0 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( Ooo0oOooo0 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  oooO00o . write ( OooO0o000Oo + '\n' )
  if 1 - 1: o0o00Oo0O * i1iIi
  if 5 - 5: iiiiiiii1 - iiiiiiii1 / O0Oooo0O % I1ii11iIi11i
def OOoO00OOo ( ) :
 i1iI1 = cloudflare . source ( o0oOoO00o ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 iI111i = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( i1iI1 )
 for iiI in iI111i :
  oOo0 ( '24/7' , iiI , 90021 , I1IIIii + '247Streams.png' )
  if 42 - 42: ooOoO0O00 . Ii / iii1i1iiiiIi
def iii1 ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  O0O0ooOOO ( i1I1i111Ii , ( iiI ) . strip ( ) , 222 , I1IIIii + '247Streams.png' , I1IIIii + '247Streams.png' , '' )
def Oo0OO0 ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  O0O0ooOOO ( i1I1i111Ii , ( iiI ) . strip ( ) , 222 , I1IIIii + 'musicch.png' , I1IIIii + 'musicch.png' , '' )
def II1Ii1iI1i1 ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  O0O0ooOOO ( i1I1i111Ii , ( iiI ) . strip ( ) , 222 , I1IIIii + 'NEWS.png' , I1IIIii + 'NEWS.png' , '' )
def iiIIIIiI111 ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  O0O0ooOOO ( i1I1i111Ii , ( iiI ) . strip ( ) , 222 , I1IIIii + 'adult.png' , I1IIIii + 'adult.png' , '' )
def OO00Oo00o ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 iI111i = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  O0O0ooOOO ( i1I1i111Ii , iiI , 1016 , I1IIIii + 'TUTS.png' , I1IIIii + 'TUTS.png' , '' )
  if 44 - 44: Ii - ooo0O + ooo0O % o0o00Oo0O / ii . OoOo0o
  if 3 - 3: o0o00Oo0O - O0Oooo0O * i1iIi * OoOo0o / i1iIi
def O0Ooo000OO00 ( ) :
 if 51 - 51: oOOoOooOo * I11i1ii1 * iI11I1II1I1I / iii1i1iiiiIi % I11i1ii1
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
 if 36 - 36: oOoO0o00OO0 * ooo0O + Ii + ii
def oOi1IiIiIii11I ( ) :
 if 80 - 80: O0Oooo0O + i1IiiiI1iI . O0Oooo0O + OoOo0o
 i1iI1 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii , IiIiIi1I1 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii + '  -  ' + ( IiIiIi1I1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiI , 10023 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
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
 iiI1ii1IIiI = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oOOo0 = cloudflare . source ( iiI1ii1IIiI )
 iI111i = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 10022 , I1IIIii + 'dtv.png' , Oo00OOOOO , '' )
  if 62 - 62: IIiIiII11i . oOOoOooOo + oOo % oOo - o0o00Oo0O - IIiIiII11i
  if 22 - 22: i1iIi - I1ii11iIi11i % oOoO0o00OO0 % oOOoOooOo % I11i1ii1
  if 72 - 72: ooOoO0O00
  if 72 - 72: oOOoOooOo + IIiIiII11i . o0o00Oo0O - iiiiiiii1 / ii . O0Oooo0O
def iii ( ) :
 if 32 - 32: ii
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 iiI = ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( O0ooOO ) . replace ( ' ' , '+' )
 oOOo0 = cloudflare . source ( iiI )
 iI111i = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  if O0ooOO in i1I1i111Ii . lower ( ) :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 10022 , I1IIIii + 'dtv.png' )
   if 29 - 29: oOoO0o00OO0
   if 41 - 41: i1iIi
   if 49 - 49: i1iIi % IIiIiII11i . i1iIi - ooo0O - i1IiiiI1iI * I11i1ii1
def IiiO0O0O0OOO0o ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for I1 , Oo , oO00oOOo0Oo , i1I1i111Ii in iI111i :
  oO0Oo0oOo = ( oO00oOOo0Oo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  II1 = ( Oo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOO0O0Ooo0 = 'Season ' + II1 + 'Episode ' + oO0Oo0oOo + i1I1i111Ii
  I11iiI1i ( oOO0O0Ooo0 , I1 )
  if 52 - 52: o0o00Oo0O + iii1i1iiiiIi
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 5 - 5: oOo0O0Ooo - ooo0O . ii - IIiIiII11i
  if 38 - 38: i1iIi * oOoO0o00OO0 % oOo
def I11iiI1i ( name , url ) :
 I1 = url
 iii1iII1I1I = name
 oo00O00oO = cloudflare . source ( I1 )
 IIi11i1i1iI1 = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oo00O00oO )
 for iIiiIi11IIi , oo00o in IIi11i1i1iI1 :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + iii1iII1I1I + oo00o + '[/COLOR]' , iIiiIi11IIi , 222 , I1IIIii + 'dtv.png' )
  if 14 - 14: i1iIi + i1iIi * ii * i1IiiiI1iI + I1ii11iIi11i . oOo0O0Ooo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: OoOo0o . OoOo0o
 if 17 - 17: IIiIiII11i / oOOoOooOo
def ii1i ( ) :
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
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + Ooo0oOooo0 , '' , '' )
 for url in O0O00o0O :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , I1IIIii + 'Next.png' , '' , '' )
  if 31 - 31: oOo0O0Ooo - ii . I11i1ii1
def I1IO00O0oO00o ( url ) :
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oOOo0 )
 O0O00o0O = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  Ooo0oOooo0 = 'http://watchepisodes.cc/' + Ooo0oOooo0
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 10093 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
 for url in O0O00o0O :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , I1IIIii + 'Next.png' , '' , '' )
  if 30 - 30: iii1i1iiiiIi % I11i1ii1 . I1ii11iIi11i - ii
def iIi1IIiiiI ( url , iconimage ) :
 Ooo0oOooo0 = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oOOo0 )
 for oO00oOOo0Oo , url , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + oO00oOOo0Oo + ' - ' + i1I1i111Ii + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , Ooo0oOooo0 , '' , '' )
  if 4 - 4: ooOoO0O00 % ooo0O % OOOo00oo0oO . ooOoO0O00
def O0OO0OOo00Oo ( url , iconimage ) :
 Ooo0oOooo0 = iconimage
 oOOo0 = cloudflare . source ( url )
 iI111i = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url in iI111i :
  if 'player' in i1I1i111Ii :
   pass
  elif 'vod' in i1I1i111Ii :
   o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , Ooo0oOooo0 , '' , '' )
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
 ii1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ii1 ) )
 for url , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 79 - 79: Ii
def o0O0oO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  if 13 - 13: I11i1ii1 . I1ii11iIi11i % OOOo00oo0oO * iiiiiiii1 - Ii / oOOoOooOo
def o0OooOOo0OO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  if 'episode' in url :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , I1IIIii + 'Next.png' , '' , '' )
  if 14 - 14: i1iIi - o0o00Oo0O
  if 68 - 68: IIiIiII11i - oOoO0o00OO0 - oOo * iI11I1II1I1I / oOo0O0Ooo * oOoO0o00OO0
def I1i1ii1IiI1i ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0O00o0oO00 = 'http://www.watchseriesgo.to/search/' + O0ooOO . replace ( ' ' , '%20' )
 oOOo0 = i11111IIIII ( oo0O00o0oO00 )
 iI111i = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , iiI , i1I1i111Ii in iI111i :
  if 'watch online' in i1I1i111Ii :
   pass
  else :
   print iiI
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.watchseriesgo.to' + iiI , 10044 , Ooo0oOooo0 , '' , '' )
   if 42 - 42: ooOoO0O00 + iiiiiiii1 . ii + oOoO0o00OO0 . i1IiiiI1iI / i1iIi
   xbmcplugin . setContent ( IIIii1II1II , 'movies' )
   if 1 - 1: ooo0O
def O00oi111II ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii , oO00oOOo0Oo , ooo0O0o00O in iI111i :
  I11Ii1iI11iI1 = ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oO00oOOo0Oo ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + I11Ii1iI11iI1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , Ooo0oOooo0 , '' , ooo0O0o00O )
  if 6 - 6: OoOo0o - o0o00Oo0O * oOoO0o00OO0
def O0o0ooo00o00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  I11Ii1iI11iI1 = ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + I11Ii1iI11iI1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , I1IIIii + 'Next.png' , '' , '' )
  if 6 - 6: Ii / oOo . Ii / oOOoOooOo
def IiI1Iii1iIIII ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , Ooo0oOooo0 , '' , '' )
 for url in IIi11i1i1iI1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , I1IIIii + 'Next.png' , '' , '' )
  if 87 - 87: IIiIiII11i . i1iIi * oOo
def OOoO00o00oo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oOOo0 )
 ii1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oOOo0 )
 for Oo , O0OO0ooO0oO0O0 in ii1 :
  iI111i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O0OO0ooO0oO0O0 ) )
  for url , i1I1i111Ii in iI111i :
   I11Ii1iI11iI1 = ( Oo ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + I11Ii1iI11iI1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
 IIi11i1i1iI1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url in iI111i :
  o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , I1IIIii + 'WATCHSERIES.png' , '' , '' )
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
  I11Ii1iI11iI1 = name
  self . Get_Sources ( iiI , I11Ii1iI11iI1 )
  if 32 - 32: i1iIi * OOOo00oo0oO
  if 85 - 85: Ii . oOo + oOo
 def Get_Sources ( self , URL , season_name ) :
  o0oO0 = xbmcgui . DialogProgress ( )
  oOOo0 = i11111IIIII ( URL )
  iI111i = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  for iiI , i1I1i111Ii in iI111i :
   URL = 'http://www.watchseriesgo.to/link/' + iiI
   self . Get_site_link ( URL , season_name )
   if 28 - 28: I1ii11iIi11i
 def Get_site_link ( self , url , season_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
  IIi11i1i1iI1 = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oOOo0 )
  OOoOOO000O0 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oOOo0 )
  for url in iI111i :
   self . main ( url , season_name )
  for url in IIi11i1i1iI1 :
   self . main ( url , season_name )
  for url in OOoOOO000O0 :
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
  for I1IiiI1ii1i , i1I1i111Ii in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
   if 14 - 14: i1iIi / I11i1ii1 - o0o00Oo0O
 def vidspot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oOOo0 )
  for I1IiiI1ii1i , i1I1i111Ii in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
   if 16 - 16: O0Oooo0O % iI11I1II1I1I . ooOoO0O00
 def thevideo ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{"file":"([^"]*)"' ) . findall ( oOOo0 )
  for I1IiiI1ii1i in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
   if 72 - 72: oOOoOooOo * OoOo0o
 def vodlocker ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for I1IiiI1ii1i in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
   if 69 - 69: OOOo00oo0oO - Ii
 def daclips ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oOOo0 )
  for I1IiiI1ii1i in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
   if 29 - 29: i1iIi + iiiiiiii1 % oOoO0o00OO0 + i1IiiiI1iI * I1ii11iIi11i - Ii
 def filehoot ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for I1IiiI1ii1i in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for I1IiiI1ii1i in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOo0 )
  for I1IiiI1ii1i in iI111i :
   self . youplay ( I1IiiI1ii1i , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oOOo0 = i11111IIIII ( url )
  iI111i = re . compile ( 'file: "([^"]*)"' ) . findall ( oOOo0 )
  for I1IiiI1ii1i in iI111i :
   self . Printer ( I1IiiI1ii1i , season_name , source_name )
   if 24 - 24: Ii . oOOoOooOo + oOOoOooOo - Ii % OoOo0o
 def Printer ( self , Link , season_name , source_name ) :
  if 58 - 58: oOo0O0Ooo
  if Link in I1II1i1iIIi . List :
   pass
  elif source_name in I1II1i1iIIi . source_list :
   pass
  else :
   II1i11I1 ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 222 , I1IIIii + 'WATCHSERIES.png' )
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
def iI111i1I1II ( ) :
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
 i1iI1 = i11ii ( url )
 iI111i = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( i1iI1 )
 for ooOo0Oo , I11i1I111II1IiI , oo00O0oOo , oOoO , IiI1Ii , o0OoOO , iIIi , oOO00o0oooOo0 , iIII1iIiiiii1Ii in iI111i :
  IIiiiI = ii11 ( I11i1I111II1IiI )
  iI1i1i1i1i = ii11 ( oo00O0oOo )
  iiII1i1II1iIi = ii11 ( oOoO )
  iII = ii11 ( IiI1Ii )
  OOOO0o0Oo0 = ii11 ( o0OoOO )
  I1iIiI1iiI = ii11 ( iIIi )
  Oo0oi1i . append ( ooOo0Oo [ 0 ] )
  oO000O00 = len ( Oo0oi1i )
  IiIIIii1iIII1 = int ( len ( OO00O0O00oOOO ) - len ( ooOo0Oo ) - 2 )
  if len ( Oo0oi1i ) >= 10 :
   IiIIIii1iIII1 = IiIIIii1iIII1 - 1
  if len ( Oo0oi1i ) <= int ( ooo0O0Oo0O ) :
   O0O0ooOOO ( str ( oO000O00 ) + ' ' + ooOo0Oo + OO00O0O00oOOO [ 0 : IiIIIii1iIII1 ] + I11i1I111II1IiI + IIiiiI + oo00O0oOo + iI1i1i1i1i + oOoO + iiII1i1II1iIi + IiI1Ii + iII + o0OoOO + OOOO0o0Oo0 + iIIi + I1iIiI1iiI + ' ' + iIII1iIiiiii1Ii , '' , '' , '' , '' , '' )
   if 69 - 69: ooOoO0O00 / Ii + I1ii11iIi11i - iii1i1iiiiIi
   if 13 - 13: I11i1ii1 . iI11I1II1I1I
def ii11 ( space ) :
 if len ( space ) > 1 :
  OO0o0o0oo = len ( '        ' ) - len ( space ) + 1
  space = int ( OO0o0o0oo ) * ' '
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
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iI111i = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiI , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Ooo0oOooo0 , Oo00OOOOO , '' )
  if 30 - 30: ii % OoOo0o
def IIiIoOOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 ii1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oOOo0 )
 for ii1 in ii1 :
  o0O0ooooooo00 = re . compile ( '(.*?)</h2>' ) . findall ( str ( ii1 ) )
  for O00o00 in o0O0ooooooo00 :
   O00o00 = O00o00
  ooo0OiII1iii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ii1 ) )
  for I11Ii , Ooo0oOooo0 , time , OOo00o0oOO0o in ooo0OiII1iii :
   Iii1Iii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( OOo00o0oOO0o )
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + O00o00 + ' - ' + I11Ii + ' - ' + time + '[/COLOR]' , '' , 10010 , o0oOoO00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + Ooo0oOooo0 , Oo00OOOOO , ( str ( Iii1Iii ) ) )
   if 27 - 27: iiiiiiii1 / ooOoO0O00 . iiiiiiii1 % ii * OOOo00oo0oO % IIiIiII11i
 O00oO000O0O ( 'tvshows' , 'Media Info 3' )
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
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  iiiI11iii11iI = i1I1i111Ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in i1I1i111Ii :
   pass
  else :
   iiiI11iii11iI = i1I1i111Ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   II1i11I1 ( '[COLOR' + iiI1IiI + ']' + iiiI11iii11iI + '[/COLOR]' , url , 10013 , Ooo0oOooo0 )
 for url , Ooo0oOooo0 , i1I1i111Ii in IIi11i1i1iI1 :
  iiiI11iii11iI = i1I1i111Ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in i1I1i111Ii :
   pass
  else :
   II1i11I1 ( '[COLOR' + iiI1IiI + ']' + iiiI11iii11iI + '[/COLOR]' , url , 10013 , Ooo0oOooo0 )
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
 for url , Ooo0oOooo0 , i1I1i111Ii in IIi11i1i1iI1 :
  iiiI11iii11iI = i1I1i111Ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in i1I1i111Ii :
   pass
  else :
   II1i11I1 ( '[COLOR' + iiI1IiI + ']' + iiiI11iii11iI + '[/COLOR]' , url , 10013 , Ooo0oOooo0 )
   if 54 - 54: OoOo0o . oOoO0o00OO0 * i1IiiiI1iI % O0Oooo0O . o0o00Oo0O * I11i1ii1
def o00OOOOoOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oOOo0 )
 for iIiiIi11IIi in iI111i :
  OooOoOoo0ooo0 = ( iIiiIi11IIi ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  O0O0oo ( 'http:' + OooOoOoo0ooo0 )
  if 69 - 69: I1ii11iIi11i * oOOoOooOo
  if 91 - 91: ooo0O . oOOoOooOo / oOo / Ii * ooo0O
  if 52 - 52: oOo0O0Ooo - Ii / I11i1ii1 . OOOo00oo0oO
  if 38 - 38: OOOo00oo0oO + ii * iii1i1iiiiIi % OOOo00oo0oO
def oo0Oooo0O ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  II1i11I1 ( i1I1i111Ii , url , 8046 , Ooo0oOooo0 )
 for url in IIi11i1i1iI1 :
  oOo0 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , I1IIIii + 'Next.png' )
def ooO0Oo ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  O0O0oo ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 81 - 81: OoOo0o
def OooOooo00OOO0o ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( i1iI1 )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 41 - 41: OoOo0o % Ii * oOo0O0Ooo + ooo0O / OOOo00oo0oO
def OOoiIIiiIIIi1I ( ) :
 oOo0 ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , I1IIIii + 'documentary.png' )
 oOo0 ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , I1IIIii + 'documentary.png' )
 oOo0 ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , I1IIIii + 'Search.png' )
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , iiI , 8041 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO0i11i1i1i ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( i1iI1 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( i1iI1 )
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + Ooo0oOooo0 )
 for url in next :
  oOo0 ( 'NEXT PAGE' , url , 8041 , I1IIIii + 'Next.png' )
  if 83 - 83: IIiIiII11i + I11i1ii1 - ooo0O % ooo0O * ooo0O
  if 100 - 100: i1iIi . iI11I1II1I1I
def Iiii1i11III1I1 ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( i1iI1 )
 for url in iI111i :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   II1i11I1 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
  else :
   oOo0 ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def O000o ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , url in iI111i :
  url = ( url ) . replace ( '\/' , '/' )
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 222 , '' )
  if 44 - 44: IIiIiII11i
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIiiiiiiII ( name , url ) :
 o00O00o0O0 = 0
 name = name
 url = url
 OoO = [ '144' , '240' , '380' , '480' , '720' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  IIIIiii1IIii ( url )
  if 41 - 41: IIiIiII11i * o0o00Oo0O % OoOo0o . iI11I1II1I1I
  if 55 - 55: I11i1ii1
  if 43 - 43: OoOo0o
  if 17 - 17: Ii
  if 94 - 94: ii - I11i1ii1 + OOOo00oo0oO . ii / ooOoO0O00
  if 53 - 53: O0Oooo0O % oOoO0o00OO0
  if 17 - 17: ii % i1iIi % o0o00Oo0O
  if 46 - 46: iiiiiiii1 + O0Oooo0O % ii * oOoO0o00OO0
def O000o0O0 ( ) :
 i1iI1 = i1I1 ( 'http://documentarylovers.com/' )
 iI111i = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  if 'genre' in iiI :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , iiI , 80010 , I1IIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0000oOoO0o0 ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( i1iI1 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , Ooo0oOooo0 )
 for url in next :
  oOo0 ( 'NEXT PAGE' , url , 80010 , I1IIIii + 'Next.png' )
  if 19 - 19: ooOoO0O00 % OOOo00oo0oO / ooo0O . ooo0O
def o00oI1i1IIIIIII ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( i1iI1 )
 for url in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , I1IIIii + 'documentary.png' )
 for url in IIi11i1i1iI1 :
  O000o ( url )
  if 1 - 1: iI11I1II1I1I - IIiIiII11i - OOOo00oo0oO % oOo + iii1i1iiiiIi + ooo0O
def I1IIiIi ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = 'http://documentarylovers.com/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 i1oOOOOOOOoO = OooooOoO . lower ( )
 O0000oOoO0o0 ( i1oOOOOOOOoO )
 if 68 - 68: ii % I1ii11iIi11i + I1ii11iIi11i * ii + oOoO0o00OO0 * o0o00Oo0O
def iI1iiI1Ii ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  if 'films' in url :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , I1IIIii + 'documentary.png' )
def i1iiII1iIIIIII ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( i1iI1 )
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  if 'films' in url :
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + Ooo0oOooo0 )
 for url in IIi11i1i1iI1 :
  oOo0 ( 'NEXT' , url , 8049 , I1IIIii + 'Next.png' )
def IIIIII11iIiI1III ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( i1iI1 )
 for url in iI111i :
  if 'rtd' in url :
   o0Ooo0 ( url )
   if 17 - 17: I11i1ii1 % ii / oOOoOooOo * ii
def o0Ooo0 ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( i1iI1 )
 for IIIi1I1IIii1II , file in iI111i :
  url = ( 'https://rtd.rt.com' + IIIi1I1IIii1II + file )
  IIIIiii1IIii ( url )
  if 14 - 14: IIiIiII11i + o0o00Oo0O - iiiiiiii1
  if 18 - 18: ooo0O / Ii % oOoO0o00OO0 * ii
def o0OoOO0 ( ) :
 oOOo0 = i1I1 ( 'http://www.stream2watch.co/live-tv' )
 iI111i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii , ooo in iI111i :
  oOo0 ( ( i1I1i111Ii + '[COLOR' + iiI1IiI + ']' + ooo + '[/COLOR]' ) , iiI , 8086 , Ooo0oOooo0 )
  if 75 - 75: oOo0O0Ooo
def o00o000 ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 8087 , Ooo0oOooo0 )
  if 41 - 41: oOoO0o00OO0 * Ii - I1ii11iIi11i * IIiIiII11i
def OOO0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  oOO0ooOO ( url , i1I1i111Ii )
  if 65 - 65: iI11I1II1I1I
def oOO0ooOO ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  print url
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 76 - 76: iI11I1II1I1I * O0Oooo0O / oOo0O0Ooo
def ooOO0O00O ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iiI , 3002 , 'http://www.solie.org/alibrary/' + Ooo0oOooo0 )
def i1iOOoOo0o ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + Ooo0oOooo0 )
def oOOOiII1iII ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( i1iI1 )
 iiii11i1ii1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( i1iI1 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , I1IIIii + 'classicmovies.png' )
 for url , i1I1i111Ii in iiii11i1ii1 :
  oOo0 ( '[COLOR' + iiI1IiI + ']Season- ' + i1I1i111Ii + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'classicmovies.png' )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , I1IIIii + 'Next.png' )
 for url , Ooo0oOooo0 , i1I1i111Ii in IIi11i1i1iI1 :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + Ooo0oOooo0 )
def oOO00o0O0O ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( i1iI1 )
 for url in iI111i :
  o0Ooo0OoO ( url )
def o0Ooo0OoO ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( i1iI1 )
 for url in iI111i :
  IIIIiii1IIii ( url )
  if 31 - 31: i1IiiiI1iI + oOo / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
def I1iii ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiI , 8065 , I1IIIii + 'classicmovies.png' )
def iiiiIiI1IIiI ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( "v.src = '([^']*)';" ) . findall ( i1iI1 )
 for url in iI111i :
  o00oOOo ( url )
  if 53 - 53: iI11I1II1I1I % iii1i1iiiiIi % oOo0O0Ooo + oOoO0o00OO0 % ii
def oo0OO ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 iI111i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiI , 8065 , I1IIIii + 'classictv.png' )
def IIII ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  if 'mp4' in url :
   IIIIiii1IIii ( url )
 for url in IIi11i1i1iI1 :
  yt . PlayVideo ( url )
  if 23 - 23: ooOoO0O00
def IiI11IiIIi ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iI111i = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iiI , 8071 , I1IIIii + 'streams.png' )
def oOOo0OoooOo ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for i1I1i111Ii , url in iI111i :
  if '(Free Access)' in i1I1i111Ii :
   url = ( url ) . strip ( )
  else :
   url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , I1IIIii + 'streams.png' )
def I1I1IiIiIIi1I ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , i1I1i111Ii , url in iI111i :
  url = ( ( o0oOoO00o ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , Ooo0oOooo0 , oo0o0000 , '' )
  if 74 - 74: ii + oOoO0o00OO0 % o0o00Oo0O
def OO0IIIIIIi111i ( ) :
 OoO = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  iII1II ( 'http://watchxxxfree.com/categories' )
 if iiI1IIIi == 1 :
  oO00oOOOO ( 'http://www.perfectgirls.net' )
 if iiI1IIIi == 2 :
  o0o0OOO0ooo00 ( 'http://www.xvideos.com/best' )
 if iiI1IIIi == 3 :
  I11III111i1I ( 'http://www.xvideos.com/best' )
 if iiI1IIIi == 4 :
  o0o0OOO0ooo00 ( 'http://www.xvideos.com/best' )
 if iiI1IIIi == 5 :
  o0o0OOO0ooo00 ( 'http://www.xvideos.com/verified/videos' )
 if iiI1IIIi == 6 :
  O0ooOO0O00 ( 'http://www.xvideos.com/tags' )
 if iiI1IIIi == 7 :
  OOO0O ( 'http://www.xvideos.com/porn' )
 if iiI1IIIi == 8 :
  iIi11 ( )
  if 82 - 82: ooOoO0O00 % I11i1ii1 + I1ii11iIi11i - o0o00Oo0O - i1IiiiI1iI
  if 64 - 64: i1iIi - iiiiiiii1
  if 12 - 12: ooOoO0O00
  if 99 - 99: IIiIiII11i - oOoO0o00OO0 * I11i1ii1
  if 3 - 3: I11i1ii1 - oOoO0o00OO0 * iiiiiiii1 * oOoO0o00OO0 + I1ii11iIi11i
  if 15 - 15: oOoO0o00OO0 * i1iIi / iiiiiiii1 . ooo0O / i1iIi % iii1i1iiiiIi
  if 75 - 75: ii % Ii % iI11I1II1I1I % oOoO0o00OO0 / Ii
  if 96 - 96: oOOoOooOo * OOOo00oo0oO / iI11I1II1I1I / i1IiiiI1iI
  if 5 - 5: ooo0O
def O0oo0o0ooO00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  if 'ch' in url :
   i1I1ii1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Jizbox.png' , I1IIIii + 'Jizbox.png' , '' )
def i1i1IIoO0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oOOo0 )
 O0OO0OoO00oOo = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oOOo0 )
 for url , i1I1i111Ii in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , I1IIIii + 'Jizbox.png' , '' , '' )
 for i1I1i111Ii , url in O0OO0OoO00oOo :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , I1IIIii + 'Next.png' , '' , '' )
def IiIoOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   iII1Ii1iIIii ( url )
def oooOoO00Oo00o0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  IIIIiii1IIii ( url )
def iII1II ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii , OO0o0o0oo in iI111i :
  if 'category' in url :
   i1I1ii1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORorange]   ' + OO0o0o0oo + '[/COLOR]' , url , 90006 , Ooo0oOooo0 , I1IIIii + 'Jizbox.png' , '' )
def IiiIiI1IIII11II ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 O0OO0OoO00oOo = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , Ooo0oOooo0 , '' , '' )
 for url in O0OO0OoO00oOo :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , url , 90006 , I1IIIii + 'Next.png' , '' , '' )
def i111I ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  if 'jetload' in url :
   iII1Ii1iIIii ( url )
def iII1Ii1iIIii ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",' ) . findall ( oOOo0 )
 for url in iI111i :
  IIIIiii1IIii ( url )
def oO00oOOOO ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , OO0o0o0oo in iI111i :
  if 'category' in url :
   i1I1ii1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORorange]' + OO0o0o0oo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , I1IIIii + 'Jizbox.png' , '' , '' )
def oO0ooo0o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 I1 = url
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 O0OO0OoO00oOo = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  O0O0ooOOO ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , Ooo0oOooo0 , '' , '' )
 for url in O0OO0OoO00oOo :
  o00oOOooOOo0o ( '[COLORred]NEXT[/COLOR]' , I1 + '/' + url , 90003 , I1IIIii + 'Next.png' , '' , '' )
def O0oOO0o0 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'get\("(.*)", function' ) . findall ( oOOo0 )
 for url in iI111i :
  O000000oooOOo ( 'http://www.perfectgirls.net' + url )
def O000000oooOOo ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'http://(.+?)\n' ) . findall ( oOOo0 )
 for url in iI111i :
  O0O0oo ( 'http://' + url )
def OOO0O ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii , OO0o0o0oo in iI111i :
  i1I1ii1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgreen] - No of Videos : [COLORorange]' + OO0o0o0oo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
def O0ooOO0O00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0OO0OoO00oOo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in O0OO0OoO00oOo :
  i1I1ii1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , I1IIIii + 'Jizbox.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oOOo0 )
 for url , i1I1i111Ii , OO0o0o0oo in iI111i :
  i1I1ii1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgreen] - No of Videos : [COLORorange]' + ( OO0o0o0oo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
  if 50 - 50: i1IiiiI1iI + ooOoO0O00 * oOo / i1iIi
def I1Ioo000oooooooO ( url ) :
 oOOo0 = i11111IIIII ( url )
 O0OO0OoO00oOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in O0OO0OoO00oOo :
  i1I1ii1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii , oO00O0O000OO in iI111i :
  i1I1ii1 ( i1I1i111Ii + '--' + ( oO00O0O000OO ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( Ooo0oOooo0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 18 - 18: OOOo00oo0oO * I1ii11iIi11i % Ii + o0o00Oo0O % OoOo0o . OoOo0o
  if 84 - 84: ii - I1ii11iIi11i
def o0o0OOO0ooo00 ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii , Ooo0 , I1I11i in iI111i :
  i1I1ii1 ( '[COLORorangered]' + i1I1i111Ii + '[COLORgreen] - Porn Quality : [COLORorange]' + Ooo0 + ' - [COLORred]' + I1I11i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , Ooo0oOooo0 , Ooo0oOooo0 , Ooo0 + ' - ' + I1I11i )
 OoOOoOo0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for Ooo0oOooo0 , url , i1I1i111Ii , I1I11i in IIi11i1i1iI1 :
  i1I1ii1 ( '[COLORorangered]' + i1I1i111Ii + '[COLORgreen] - Porn Quality : [COLORorange]' + I1I11i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , Ooo0oOooo0 , Ooo0oOooo0 , I1I11i )
 OoOOoOo0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for url in OoOOoOo0O :
  i1I1ii1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Next.png' , '' , '' )
  if 47 - 47: iii1i1iiiiIi % oOOoOooOo % oOoO0o00OO0 * ooOoO0O00
  if 18 - 18: iii1i1iiiiIi
def I11III111i1I ( url ) :
 oOOo0 = i11111IIIII ( url )
 ii1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 O0OO0OoO00oOo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oOOo0 )
 for url in O0OO0OoO00oOo :
  i1I1ii1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , I1IIIii + 'Next.png' , '' , '' )
 iI111i = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ii1 ) )
 for url , i1I1i111Ii in iI111i :
  if '/c/' in url :
   i1I1ii1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , I1IIIii + 'Jizbox.png' , '' , '' )
   if 30 - 30: IIiIiII11i
   if 27 - 27: ooOoO0O00 - iI11I1II1I1I + o0o00Oo0O % I1ii11iIi11i / OoOo0o + ooOoO0O00
def iIi11 ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1iiO0Oo = ( O0ooOO ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 i1oOOOOOOOoO = i1i1iiO0Oo . lower ( )
 iI11IIi1iiI1I = 'http://www.xvideos.com/?k=' + i1oOOOOOOOoO
 print iI11IIi1iiI1I + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOo0 = i11111IIIII ( iI11IIi1iiI1I )
 iI111i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , iiI , i1I1i111Ii , I1I11i , oOoOOoooO00oO in iI111i :
  i1I1ii1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgreen] - Porn Quality : [COLORorange]' + oOoOOoooO00oO + ' - [COLORred]' + I1I11i + '[/COLOR]' , 'http://www.xvideos.com' + iiI , 10108 , Ooo0oOooo0 , Ooo0oOooo0 , oOoOOoooO00oO + ' - ' + I1I11i )
 OoOOoOo0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOo0 )
 for iiI in OoOOoOo0O :
  i1I1ii1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iiI , 10105 , I1IIIii + 'Next.png' , '' , '' )
if 62 - 62: i1iIi
if 4 - 4: iI11I1II1I1I . I1ii11iIi11i - Ii
if 51 - 51: iii1i1iiiiIi - Ii / oOo0O0Ooo % i1iIi * i1iIi % oOOoOooOo
if 12 - 12: oOOoOooOo % iii1i1iiiiIi
if 1 - 1: o0o00Oo0O / oOOoOooOo
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
def o0o0o ( url ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oOOo0 )
 IIi11i1i1iI1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oOOo0 )
 OOoOOO000O0 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oOOo0 )
 for url in iI111i :
  if 'http' in url :
   II1i11I1 ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in IIi11i1i1iI1 :
  if 'http' in url :
   II1i11I1 ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
 for url in OOoOOO000O0 :
  if 'http' in url :
   II1i11I1 ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , I1IIIii + 'Jizbox.png' )
   if 30 - 30: o0o00Oo0O
def OoO00O00 ( url ) :
 III11 = xbmc . Player ( Ii1Ii11Iii1i1 ( ) )
 import urlresolver
 try : III11 . play ( url )
 except : pass
 if 35 - 35: OoOo0o
 if 90 - 90: Ii
def iIiIIi11i1 ( ) :
 if 13 - 13: oOo * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - iii1i1iiiiIi
 if 43 - 43: iiiiiiii1 / O0Oooo0O * oOo0O0Ooo % oOOoOooOo % oOo0O0Ooo
 if 18 - 18: oOo
 if 99 - 99: iiiiiiii1 / OOOo00oo0oO . Ii / i1IiiiI1iI + ooOoO0O00 - i1IiiiI1iI
 if 50 - 50: ooOoO0O00
 if 56 - 56: oOo + O0Oooo0O / i1iIi
 if 75 - 75: iii1i1iiiiIi
 if 96 - 96: ooo0O * i1IiiiI1iI * I1ii11iIi11i
 if 36 - 36: ii + oOOoOooOo . OOOo00oo0oO * oOOoOooOo + I11i1ii1
 if 45 - 45: OOOo00oo0oO / iiiiiiii1 + oOoO0o00OO0 - I1ii11iIi11i - oOOoOooOo . iI11I1II1I1I
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 8091 , I1IIIii + 'gofish.png' )
def Oooo00o ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 8092 , Ooo0oOooo0 )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
def iIiii1Ii1I ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oOOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oOOo0 )
 I1Ii = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 in I1Ii :
  Ooo0oOooo0 = Ooo0oOooo0
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 8092 , Ooo0oOooo0 )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , I1IIIii + 'Next.png' )
  if 29 - 29: iI11I1II1I1I % iii1i1iiiiIi % oOoO0o00OO0 / iii1i1iiiiIi - Ii
def o00OOOo0O0O0o0 ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( "videoId: '([^']*)'," ) . findall ( oOOo0 )
 for url in iI111i :
  yt . PlayVideo ( url )
  if 82 - 82: ii / oOo0O0Ooo * IIiIiII11i - ii % iI11I1II1I1I * oOo
  if 32 - 32: Ii - iii1i1iiiiIi * i1IiiiI1iI . I1ii11iIi11i * oOOoOooOo
  if 21 - 21: OoOo0o
  if 11 - 11: OOOo00oo0oO % Ii * o0o00Oo0O
I1IiIIIII1iII1 = '{PQ},' ; OO0oOoO0O0 = '{SC},' ; iiiI1i = '{XG},' ; O0OooO00O0 = '{JP},' ; iiI1i111I1 = '{HW},' ; iiIi11i1I1 = '{RT},'
def O00OOooo0Ooo ( ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 IIiiiiiIiIIi = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 iiI = 'http://onlinemovies.tube/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 I1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 iiIiiIi1 = ( o0oOoO00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 I1Ii11i = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 I1iIiiiI1 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OOO0O00Oo = ( o0oOoO00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ii1oOOO0ooOO = ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + O0ooOO
 i11IiI1iiI11 = ( o0oOoO00o ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OOoOOOO00 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 72 - 72: I11i1ii1 + Ii - OoOo0o
 Iiii1I = ( o0oOoO00o ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 Ooo000000 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 67 - 67: iI11I1II1I1I % I11i1ii1
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 oo00O00oO = i1Oo00 ( I1 )
 o0oO0 . update ( 14 , "" , "Checking Source Technica " )
 OO0ooO0 = i1Oo00 ( I1 )
 o0oO0 . update ( 32 , "" , "Checking Source Pandoras Box " )
 iIiIIIi = i1Oo00 ( iiIiiIi1 )
 o0oO0 . update ( 59 , "" , "Checking Source Lazy List " )
 ooo00OOOooO = i1Oo00 ( I1Ii11i )
 o0oO0 . update ( 72 , "" , "Checking Source RaizTv " )
 OoOooOO0oOOo0O = i1Oo00 ( OOoOOOO00 )
 o0oO0 . update ( 91 , "" , "Checking WebSpace " )
 OoO0OOoO0Oo0 = i1Oo00 ( Ooo000000 )
 o0oO0 . update ( 97 , "" , "Matching Results" )
 if 97 - 97: iiiiiiii1
 if OoOooOO0oOOo0O != 'Failed' :
  oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOooOO0oOOo0O )
  for iiI , i1I1i111Ii in oO00 :
   IIiIiiI1i = i1Oo00 ( iiI )
   IIiO0Oo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIiIiiI1i )
   for III11I1 , ooo in IIiO0Oo :
    ooo = ( ooo . replace ( '.' , ' ' ) )
    if i1oOOOOOOOoO in ooo . lower ( ) :
     if '.mkv' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , iiI + III11I1 , 222 , '' , '' , '' )
     elif '.mp4' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , iiI + III11I1 , 222 , '' , '' , '' )
     elif '.avi' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , iiI + III11I1 , 222 , '' , '' , '' )
     elif '.wav' in III11I1 :
      O0O0ooOOO ( ( '[COLOR' + iiI1IiI + ']' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , iiI + III11I1 , 222 , '' , '' , '' )
     else :
      o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , iiI + III11I1 , 1006 , '' , '' , '' )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 05 , "" , "Getting WebSpace Links" )
      if 40 - 40: oOOoOooOo
      O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00O00oO )
  for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in IIi11i1i1iI1 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORred] source Technica[/COLOR]' ) , iiI , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting Technica Links" )
    if 61 - 61: iiiiiiii1 - OoOo0o / iiiiiiii1 . I1ii11iIi11i % oOo
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: O0Oooo0O * I1ii11iIi11i
 if iIiIIIi != 'Failed' :
  OOoOOO000O0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIiIIIi )
  for II1io0 , i1I1i111Ii in OOoOOO000O0 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiIiiIi1 + II1io0 ) , 1006 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 18 , "" , "Getting Lazy List Links" )
 if ooo00OOOooO != 'Failed' :
  IiIIiii11II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo00OOOooO )
  for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in IiIIiii11II1 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    O0O0ooOOO ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORred] source RaizTv[/COLOR]' ) , iiI , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 53 , "" , "Getting RaizTv Links" )
    if 75 - 75: oOo0O0Ooo . iiiiiiii1 % iiiiiiii1 * Ii + ooOoO0O00 * I1ii11iIi11i
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 Ooo00O0 = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for ii1o0oo0Ooooo0 in Ooo00O0 :
  Oo0oOo000OoO0 = Ii1iIiII1ii1 + '/Movies/a.to.z/' + ii1o0oo0Ooooo0 + '.php'
  OoOooOO0oOOo0O = i1Oo00 ( Oo0oOo000OoO0 )
  if OoOooOO0oOOo0O != 'Failed' :
   oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOooOO0oOOo0O )
   for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in oO00 :
    if O0ooOO in i1I1i111Ii . lower ( ) :
     if '.php' in iiI :
      i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
      o00oOOooOOo0o ( i1I1i111Ii + '-[COLORred] source Pans Box[/COLOR]' , iiI , 426 , i1I , oOoOo0OOOOO , ooo0O0o00O )
     else :
      i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
      iI11IiiI1 ( i1I1i111Ii + '-[COLORred] source Pans Box[/COLOR]' , iiI , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 89 , "" , "Getting Pandoras Links" )
      if 98 - 98: i1iIi - ii * i1IiiiI1iI * OOOo00oo0oO % oOoO0o00OO0 * IIiIiII11i
      O00oO000O0O ( 'tvshows' , 'Media Info 3' )
      if 86 - 86: Ii / i1IiiiI1iI * iiiiiiii1 - iiiiiiii1
 Ooo00O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 32 - 32: I1ii11iIi11i . o0o00Oo0O
 if 48 - 48: oOoO0o00OO0 % IIiIiII11i + i1IiiiI1iI
 for ii1o0oo0Ooooo0 in Ooo00O0 :
  Oo0oOo000OoO0 = IIiiiiiIiIIi + ii1o0oo0Ooooo0
  O00oo00oOOO0o = i1Oo00 ( Oo0oOo000OoO0 )
  if O00oo00oOOO0o != 'Failed' :
   II1iI111iiIIiI1I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O00oo00oOOO0o )
   for II1io0 , i1I1i111Ii in II1iI111iiIIiI1I :
    if O0ooOO in i1I1i111Ii . lower ( ) :
     II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IIiiiiiIiIIi + ii1o0oo0Ooooo0 + II1io0 ) , 222 , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 100 , "" , "Getting Source 5 Links" )
     if 25 - 25: I11i1ii1 * ooo0O / oOo0O0Ooo . I11i1ii1 % IIiIiII11i
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: iii1i1iiiiIi * iiiiiiii1
def oOO0OOOOoooO ( ) :
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / i1IiiiI1iI
 if 92 - 92: ooo0O
 if 8 - 8: iiiiiiii1 + oOoO0o00OO0 . i1iIi
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
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 if 23 - 23: ii + Ii / I1ii11iIi11i / iiiiiiii1 . iiiiiiii1 * oOo0O0Ooo
 if 98 - 98: I11i1ii1
 III11I1 = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( O0ooOO ) . replace ( ' ' , '+' )
 I1 = 'http://onlinemovies.tube/?s=' + ( O0ooOO ) . replace ( ' ' , '+' )
 iiIiiIi1 = ( o0oOoO00o ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 I1Ii11i = ( o0oOoO00o ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 OOO0O00Oo = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 ii1oOOO0ooOO = 'http://www.tvmaze.com/search?q=' + ( O0ooOO ) . replace ( ' ' , '+' )
 i11IiI1iiI11 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 OOoOOOO00 = ( o0oOoO00o ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 23 - 23: i1IiiiI1iI / ooOoO0O00 * oOo
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 51 - 51: OoOo0o - ii / ii % ii
 o0oO0 . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 85 - 85: oOo . ooo0O . oOo0O0Ooo
 if 75 - 75: iI11I1II1I1I - i1iIi % o0o00Oo0O % I11i1ii1
 II1iII1i1i = i1Oo00 ( III11I1 )
 o0oO0 . update ( 14 , "" , "Checking Source 3/11 Links" )
 oo00O00oO = i1Oo00 ( I1 )
 o0oO0 . update ( 28 , "" , "Checking Source 4/11 Links" )
 iIiIIIi = i1Oo00 ( iiIiiIi1 )
 o0oO0 . update ( 40 , "" , "Checking Source 5/11 Links" )
 ooo00OOOooO = i1Oo00 ( I1Ii11i )
 o0oO0 . update ( 52 , "" , "Checking Source 6/11 Links" )
 O00oo00oOOO0o = i1Oo00 ( OOO0O00Oo )
 o0oO0 . update ( 76 , "" , "Checking Source 7/11 Links" )
 Ii1I1 = i1Oo00 ( ii1oOOO0ooOO )
 o0oO0 . update ( 88 , "" , "Checking Source 8/11 Links" )
 OO0ooO0 = i1Oo00 ( i11IiI1iiI11 )
 o0oO0 . update ( 95 , "" , "Checking Source 9/11 Links" )
 OoOooOO0oOOo0O = i1Oo00 ( OOoOOOO00 )
 o0oO0 . update ( 97 , "" , "Matching Results" )
 if 6 - 6: I1ii11iIi11i % OOOo00oo0oO * oOOoOooOo - ooOoO0O00 . iii1i1iiiiIi
 if 20 - 20: I1ii11iIi11i / O0Oooo0O . I1ii11iIi11i
 if OoOooOO0oOOo0O != 'Failed' :
  oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOooOO0oOOo0O )
  for iiI , i1I1i111Ii in oO00 :
   IIiIiiI1i = i1Oo00 ( iiI )
   IIiO0Oo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIiIiiI1i )
   for III11I1 , ooo in IIiO0Oo :
    if i1oOOOOOOOoO in ooo . lower ( ) :
     o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']*' + ooo + '-[COLORgold] source ' + i1I1i111Ii + '[/COLOR]' ) , iiI + III11I1 , 1006 , '' , '' , '' )
     o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oO0 . update ( 05 , "" , "Getting INDEXER Links" )
     if 60 - 60: oOoO0o00OO0 - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . iii1i1iiiiIi
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if OO0ooO0 != 'Failed' :
  ooIi11iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0ooO0 )
  for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in ooIi11iI :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] source HeroVision[/COLOR]' ) , iiI , 1016 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 10 , "" , "Getting Herovision Links" )
    if 24 - 24: I11i1ii1 * oOo0O0Ooo / OoOo0o
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 51 - 51: iI11I1II1I1I / i1IiiiI1iI * oOo * i1iIi + oOoO0o00OO0 . ii
 if Ii1I1 != 'Failed' :
  iiIIiiIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( Ii1I1 )
  for iiI , Ooo0oOooo0 , i1I1i111Ii in iiIIiiIi :
   I1 = 'http://www.tvmaze.com' + iiI . replace ( '"' , '' )
   IIiI = requests . get ( I1 ) . content
   iI111i = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiI )
   for ooo0O0o00O in iI111i :
    if not '<div>' in ooo0O0o00O :
     O0oOOo0o = ooo0O0o00O . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
    Ooo0oOooo0 = 'http:' + Ooo0oOooo0
    i1I1i111Ii = i1I1i111Ii . replace ( '&#039;' , '' )
    if i1I1i111Ii == '' :
     I1III11iiii11i1 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( iiI ) )
     for i1I1i111Ii in I1III11iiii11i1 :
      i1I1i111Ii = i1I1i111Ii . replace ( '-' , ' ' )
   O0OOoOOO0oO ( i1I1i111Ii + '-[COLORgold] source Scraper[/COLOR]' , I1 , 9110002 , Ooo0oOooo0 , Oo00OOOOO , O0oOOo0o , '' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 20 , "" , "Getting Scraper Links" )
   if 75 - 75: I11i1ii1 / ii / o0o00Oo0O % OoOo0o
   O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oo00O00oO )
  o0OOoOo0oo = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oo00O00oO )
  for iiI , Ooo0oOooo0 , i1I1i111Ii , ooO0 in IIi11i1i1iI1 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    if 'season' in ooO0 :
     oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , iiI , 90054 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
    if 'episodes' in ooO0 :
     oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , iiI , 90044 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
  for iiI in o0OOoOo0oo :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , iiI , 90053 , I1IIIii + 'Next.png' )
   o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oO0 . update ( 40 , "" , "Getting Tv HUB Links" )
   if 87 - 87: IIiIiII11i / iI11I1II1I1I % oOoO0o00OO0
   O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if II1iII1i1i != 'Failed' :
  I1iii11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( II1iII1i1i )
  for iiI , i1I1i111Ii , Ooo0oOooo0 in I1iii11 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + ( i1I1i111Ii ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , iiI , 8022 , Ooo0oOooo0 , '' , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 45 , "" , "Getting Source iWatch Links" )
    if 11 - 11: ooo0O * oOo
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if iIiIIIi != 'Failed' :
  OOoOOO000O0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIiIIIi )
  for i1I1i111Ii in OOoOOO000O0 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iiIiiIi1 + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 60 , "" , "Getting Source 3 Links" )
    if 92 - 92: iii1i1iiiiIi . I1ii11iIi11i * i1IiiiI1iI
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if ooo00OOOooO != 'Failed' :
  IiIIiii11II1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooo00OOOooO )
  for i1I1i111Ii in IiIIiii11II1 :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( I1Ii11i + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'TVShows.png' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 70 , "" , "Getting Source 4 Links" )
    if 86 - 86: o0o00Oo0O
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if O00oo00oOOO0o != 'Failed' :
  II1iI111iiIIiI1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oo00oOOO0o )
  for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in II1iI111iiIIiI1I :
   if i1oOOOOOOOoO in i1I1i111Ii . lower ( ) :
    o00oOOooOOo0o ( ( '[COLORred]*[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '-[COLORgold] Source Scooby[/COLOR]' ) , iiI , 1016 , i1I , oOoOo0OOOOO , ooo0O0o00O )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 90 , "" , "Getting Scooby Links" )
    if 55 - 55: i1iIi / O0Oooo0O / oOoO0o00OO0 % oOOoOooOo % oOo0O0Ooo
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: OOOo00oo0oO + ii % ooOoO0O00
 O0oO0oo0O = [ '#' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
 for ii1o0oo0Ooooo0 in O0oO0oo0O :
  Oo0oOo000OoO0 = Ii1iIiII1ii1 + 'TV/Index/A-Z/' + ii1o0oo0Ooooo0 + '.php'
  i1o0oo0 = i1Oo00 ( Oo0oOo000OoO0 )
  if i1o0oo0 != 'Failed' :
   iiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( i1o0oo0 )
   for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in iiIi :
    if O0ooOO in i1I1i111Ii . lower ( ) :
     if '.php' in iiI :
      i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
      o00oOOooOOo0o ( i1I1i111Ii + '-[COLORred] source Pans Box[/COLOR]' , iiI , 426 , i1I , oOoOo0OOOOO , ooo0O0o00O )
     else :
      i1I1i111Ii = '[COLORsteelblue]' + i1I1i111Ii + '[/COLOR]'
      iI11IiiI1 ( i1I1i111Ii + '-[COLORred] source Pans Box[/COLOR]' , iiI , 222 , i1I , oOoOo0OOOOO , ooo0O0o00O )
      o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oO0 . update ( 100 , "" , "Getting Pandoras Links" )
      if 24 - 24: oOoO0o00OO0 - I1ii11iIi11i
      O00oO000O0O ( 'tvshows' , 'Media Info 3' )
      if 36 - 36: oOo0O0Ooo . OoOo0o % IIiIiII11i * I11i1ii1
      if 34 - 34: i1IiiiI1iI % iiiiiiii1 - oOOoOooOo - oOo0O0Ooo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1ioOo ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI = ( o0oOoO00o ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( O0ooOO ) . replace ( ' ' , '+' )
 if 31 - 31: I11i1ii1 % i1IiiiI1iI
 o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oO0 . update ( 0 , "" , "Checking Source Links" )
 oOOo0 = i1Oo00 ( iiI )
 o0oO0 . update ( 100 , "" , "Checking Source Links" )
 if 9 - 9: ii / I1ii11iIi11i / ooo0O % I1ii11iIi11i
 if oOOo0 != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oOOo0 )
  for iiI , i1I1i111Ii in IIi11i1i1iI1 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + iiI ) , 222 , '' )
    o0oO0 . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oO0 . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 80 - 80: i1iIi + oOo * ii - I11i1ii1 % o0o00Oo0O - O0Oooo0O
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
ooOO0 = '{ZH},' ; O0OoOo = '{IX},' ; o0Ooo0Oooo0o = '{LM},'
if 22 - 22: OOOo00oo0oO / IIiIiII11i . iii1i1iiiiIi
def Iii11i ( url ) :
 iI111iOoO0oO = cloudflare . source ( url )
 iI111i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI111iOoO0oO )
 for url , Oo , IiIiIi1I1 , i1I1i111Ii in iI111i :
  oOo0 ( ( Oo ) . replace ( 'Sezon' , ' Season ' ) + ( IiIiIi1I1 ) . replace ( 'Bölüm' , ' Episode ' ) + i1I1i111Ii , url , 8063 , '' )
  if 23 - 23: o0o00Oo0O / iiiiiiii1
  if 66 - 66: ooOoO0O00 % ii * Ii + OOOo00oo0oO * o0o00Oo0O / oOo
  if 14 - 14: oOo0O0Ooo . I11i1ii1
  if 29 - 29: ii / I11i1ii1 + iii1i1iiiiIi - O0Oooo0O + I11i1ii1 . ooOoO0O00
def iiiIiiIII ( url ) :
 iI111iOoO0oO = cloudflare . source ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iI111iOoO0oO )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( i1I1i111Ii , url , 222 , '' )
  if 100 - 100: OOOo00oo0oO + IIiIiII11i / I11i1ii1 / ooOoO0O00 / i1iIi / o0o00Oo0O
  if 50 - 50: i1iIi + i1iIi
  if 51 - 51: oOoO0o00OO0 / ii * I11i1ii1
  if 78 - 78: iiiiiiii1 / oOoO0o00OO0 . Ii
def o0oO0oOO ( ) :
 if 34 - 34: O0Oooo0O + I1ii11iIi11i / oOo0O0Ooo / Ii - oOoO0o00OO0 % ooOoO0O00
 iI111iOoO0oO = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI111i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI111iOoO0oO )
 for iiI , Ooo0oOooo0 , i1I1i111Ii , IiIiIi1I1 in iI111i :
  oOo0 ( i1I1i111Ii + '  -  ' + ( IiIiIi1I1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiI , 8063 , Ooo0oOooo0 )
  if 54 - 54: oOo0O0Ooo + iiiiiiii1
def OO0OoiIII11 ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iI111i = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 8002 , Ooo0oOooo0 )
def i1IiI11 ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( i1iI1 )
 for Ooo0oOooo0 , time , url , i1I1i111Ii , Ii1i111iI in iI111i :
  o00oOOooOOo0o ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , time ) , url , 1015 , Ooo0oOooo0 , Ii1i111iI )
  if 7 - 7: o0o00Oo0O * ooo0O + Ii - o0o00Oo0O
def I1iI ( ) :
 if 34 - 34: iiiiiiii1 - IIiIiII11i + oOo / Ii * I11i1ii1
 oOo0 ( 'Coronation Street' , '' , 8001 , '' )
 oOo0 ( 'Eastenders' , '' , 8002 , '' )
 oOo0 ( 'Emmerdale' , '' , 8003 , '' )
 oOo0 ( 'Hollyoaks' , '' , 8004 , '' )
 oOo0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 23 - 23: oOo / ooo0O
 if 22 - 22: OoOo0o - oOo . i1IiiiI1iI
 if 89 - 89: O0Oooo0O
 if 19 - 19: I11i1ii1 + O0Oooo0O
def O0OOOo000 ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if 'Holly' in i1I1i111Ii :
   Ooo0oOooo0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iiI :
    II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiI . replace ( '\\/' , '/' ) , 8006 , Ooo0oOooo0 )
   else :
    pass
    if 5 - 5: oOo / iiiiiiii1 / OoOo0o
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 70 - 70: iii1i1iiiiIi - i1IiiiI1iI + oOOoOooOo / Ii / oOo0O0Ooo % iI11I1II1I1I
def OOOOO0oOooo0O ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if 'East' in i1I1i111Ii :
   Ooo0oOooo0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iiI :
    II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiI . replace ( '\\/' , '/' ) , 8006 , Ooo0oOooo0 )
   else :
    pass
    if 97 - 97: ii . oOoO0o00OO0 % ooo0O % OoOo0o - ooo0O - ii
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: i1IiiiI1iI
def Ooo00O0ooOo ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if 'Emmer' in i1I1i111Ii :
   Ooo0oOooo0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iiI :
    II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiI . replace ( '\\/' , '/' ) , 8006 , Ooo0oOooo0 )
   else :
    pass
    if 4 - 4: OoOo0o - oOOoOooOo - i1iIi . oOo0O0Ooo * oOOoOooOo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: IIiIiII11i
def OoOoO0O ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if 'Coro' in i1I1i111Ii :
   Ooo0oOooo0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iiI :
    II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiI . replace ( '\\/' , '/' ) , 8006 , Ooo0oOooo0 )
   else :
    pass
    if 1 - 1: ii - oOOoOooOo
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: IIiIiII11i % iiiiiiii1 % i1iIi % iiiiiiii1 % i1IiiiI1iI . iI11I1II1I1I
def IIoo0O ( ) :
 oOOo0 = i11111IIIII ( 'http://uksoapshare.blogspot.co.uk/' )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOo0 )
 for iiI , i1I1i111Ii in iI111i :
  if 'Celeb' in i1I1i111Ii :
   Ooo0oOooo0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iiI :
    II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiI . replace ( '\\/' , '/' ) , 8006 , Ooo0oOooo0 )
   else :
    pass
    if 87 - 87: iI11I1II1I1I * IIiIiII11i - O0Oooo0O % O0Oooo0O - OoOo0o
def i1iiIiIi1iIII ( name , url ) :
 OoiII111i1IiiII = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OoiII111i1IiiII :
  IIiiIIIiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  i1iI1 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( i1iI1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  i1iI1 = open_url ( url )
  OOOoiI = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( i1iI1 ) [ - 1 ]
  IIiiIIIiI = OOOoiI . replace ( '\\/' , '/' )
 ooooo0OoO0 = xbmcgui . ListItem ( name , '' , '' )
 ooooo0OoO0 . setPath ( IIiiIIIiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooooo0OoO0 )
 if 46 - 46: oOOoOooOo % OoOo0o + IIiIiII11i * ooOoO0O00
 if 81 - 81: OOOo00oo0oO - ooo0O + iiiiiiii1
def i1iI ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iI111i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iiI , 7071 , I1IIIii + 'popcorn.png' )
 for iiI , i1I1i111Ii in IIi11i1i1iI1 :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iiI , 7071 , I1IIIii + 'popcorn.png' )
  if 66 - 66: I1ii11iIi11i - oOo
def i1Iii1II11iI1 ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  if 'Movies' in i1I1i111Ii :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( iiI ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , I1IIIii + 'popcorn.png' )
def IIi11iIIiIII111 ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i1iI1 )
 iI111i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , Ooo0oOooo0 )
 for url in IIi11i1i1iI1 :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , I1IIIii + 'Next.png' )
  if 88 - 88: I11i1ii1 / iI11I1II1I1I - i1IiiiI1iI + iii1i1iiiiIi + ooo0O
  if 28 - 28: oOOoOooOo + ooOoO0O00 * oOo . i1iIi + oOOoOooOo
def IIII1iiiIIiIIiI ( url ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , url , Ooo0oOooo0 in iI111i :
  if '{{' in i1I1i111Ii :
   pass
  else :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , Ooo0oOooo0 )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
iIi1I111Ii1I1 = '{UJ},' ; o00OO0Oo0Oo = '{WE},' ; I1OooOo0o0Oo0 = '{WP},' ; i11iI1i11I111 = '{PP},'
def oo0iIiIII1Ii ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , url , Ooo0oOooo0 in iI111i :
  if '{{' in i1I1i111Ii :
   pass
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , Ooo0oOooo0 )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0oOo ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  iIII1Ii1 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIII1Ii1 ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 222 , I1IIIii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: oOOoOooOo - O0Oooo0O % Ii * I1ii11iIi11i * I11i1ii1 - o0o00Oo0O
 if 66 - 66: oOo * oOo
 if 11 - 11: oOOoOooOo - i1iIi . OOOo00oo0oO * i1iIi
def o0Oo ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  if '(cooltvseries.com)' in i1I1i111Ii :
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
 for url , i1I1i111Ii in IIi11i1i1iI1 :
  if '(cooltvseries.com)' in i1I1i111Ii :
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , I1IIIii + 'CoolSeries.png' )
def iiooOOOo ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( i1iI1 )
 for url in iI111i :
  O0O0oo ( ( url ) . replace ( ' ' , '%20' ) )
ooOO = '{XX},' ; oO0Ooo = '{UD},' ; iiiiIIiiII1Iii1 = '{YT},' ; OOo0O0O000 = '{JS},' ; o0oOOoO0o0 = '{PF},'
if 56 - 56: oOo0O0Ooo . i1IiiiI1iI % iiiiiiii1
def I1I1iOO ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iI111i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  II1i11I1 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( o0oOoO00o ( iiI ) ) , 222 , Ooo0oOooo0 )
  if 48 - 48: Ii
def II111111 ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( i1iI1 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( i1iI1 )
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  if 'youtu' in url :
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + Ooo0oOooo0 )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , I1IIIii + 'Next.png' )
  if 25 - 25: oOo0O0Ooo . iI11I1II1I1I * Ii / OOOo00oo0oO % i1iIi
def oooO000oO0O ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 40 - 40: OoOo0o - oOo . ii - OOOo00oo0oO / oOOoOooOo + I1ii11iIi11i
def oooO000oO0O ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 70 - 70: ooOoO0O00 / i1IiiiI1iI / o0o00Oo0O . oOOoOooOo / IIiIiII11i
def Oo0Oo0OO ( url ) :
 i1iI1 = i11111IIIII
 iI111i = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 222 , Ooo0oOooo0 )
  if 97 - 97: OoOo0o . OoOo0o . iiiiiiii1 . iiiiiiii1
  if 63 - 63: o0o00Oo0O * I11i1ii1 / I1ii11iIi11i . oOo0O0Ooo . oOo0O0Ooo / Ii
  if 17 - 17: iI11I1II1I1I / oOo - IIiIiII11i
  if 46 - 46: iI11I1II1I1I * OOOo00oo0oO / Ii + IIiIiII11i + i1IiiiI1iI
  if 30 - 30: o0o00Oo0O * I11i1ii1 - O0Oooo0O % o0o00Oo0O * i1iIi
def II1II111iIi ( ) :
 if 71 - 71: I1ii11iIi11i * iI11I1II1I1I * i1IiiiI1iI + oOo0O0Ooo
 oOo0 ( 'All Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Entertainment' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Movies' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Music' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'News' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Sports' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Documentary' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Kids' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Food' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Religious' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'USA Channels' , '' , 7021 , I1IIIii + 'livetv.png' )
 oOo0 ( 'Other' , '' , 7021 , I1IIIii + 'livetv.png' )
 if 13 - 13: oOo - I1ii11iIi11i / oOo
 if 34 - 34: Ii + oOo + Ii . I11i1ii1 % o0o00Oo0O
def oOII1i1IiiI ( Cat_Name ) :
 if 34 - 34: iii1i1iiiiIi % iii1i1iiiiIi + ooOoO0O00 - OOOo00oo0oO . ii
 iIi1I1Iii1 = False
 Oo0ooOoo = '0'
 if Cat_Name == 'All Channels' : iIi1I1Iii1 = True
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
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( i1iI1 )
 print 'Len Match: >>>' + str ( len ( iI111i ) )
 for i1I1i111Ii , Ooo0oOooo0 , OoOOoOo0O0 in iI111i :
  oOo0oO0 = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( Ooo0oOooo0 ) . replace ( '\\' , '' )
  if OoOOoOo0O0 == Oo0ooOoo :
   oOo0 ( i1I1i111Ii , '' , 7022 , oOo0oO0 )
  elif iIi1I1Iii1 == True :
   oOo0 ( i1I1i111Ii , '' , 7022 , oOo0oO0 )
  else : pass
  if 2 - 2: o0o00Oo0O % ooo0O
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 3 - 3: Ii / OoOo0o + OOOo00oo0oO
def iIIiii ( Search_Name ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( i1iI1 )
 iI111i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( i1iI1 )
 for Ooo0oOooo0 , iiI , I1 , iiIiiIi1 in iI111i :
  oOo0oO0 = o0oOoO00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( Ooo0oOooo0 ) . replace ( '\\' , '' )
  II1i11I1 ( Search_Name + ': Link 1' , ( iiI ) . replace ( '\\' , '' ) , 222 , oOo0oO0 )
  II1i11I1 ( Search_Name + ': Link 2' , ( I1 ) . replace ( '\\' , '' ) , 222 , oOo0oO0 )
  II1i11I1 ( Search_Name + ': Link 3' , ( iiIiiIi1 ) . replace ( '\\' , '' ) , 222 , oOo0oO0 )
  if 25 - 25: IIiIiII11i + i1IiiiI1iI
def Oo000O ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  II1i11I1 ( i1I1i111Ii , ( iiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , I1IIIii + 'english.png' )
def I1iOO000Ooo ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  II1i11I1 ( i1I1i111Ii , ( iiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'xxx.png' )
def OoOooo0ooo0O ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iI111i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( i1iI1 )
 for i1I1i111Ii , iiI in iI111i :
  II1i11I1 ( i1I1i111Ii , ( iiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , I1IIIii + 'vod(1).png' )
  if 48 - 48: ooOoO0O00 - OOOo00oo0oO . ii - oOo - ooOoO0O00
def III1iI1ii1 ( url ) :
 url
 ii1IIII = xbmcgui . ListItem ( i1I1i111Ii , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1IIII )
 return
 if 93 - 93: iiiiiiii1 % O0Oooo0O
 if 90 - 90: oOoO0o00OO0 - ii / iii1i1iiiiIi
def I11ooOo ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']All WorkOuts[/COLOR]' , o0oOoO00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) , 7085 , I1IIIii + 'Fitness.png' , Oo00OOOOO , '' )
 if 100 - 100: OOOo00oo0oO
def IiiiIII1 ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '"id":.+?,"title":(.+?),"is_featured":1,"minutes":(.+?),"burnmin":(.+?),"burnmax":(.+?),"burnavg":(.+?),"difficulty":(.+?),"image":"([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( '"next_page_url":"([^"]*)"' ) . findall ( i1iI1 )
 for i1I1i111Ii , time , Iii11 , iII1Ii1ii111 , iII11IIi1I1 , o00o0o , Ooo0oOooo0 , url , ooOoOo , oO0oo0o00O0 in iI111i :
  o00oOOooOOo0o ( ( i1I1i111Ii ) . replace ( '"' , '' ) , 'https://www.fitnessblender.com/videos/' + url , 7086 , 'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-' + Ooo0oOooo0 , '' , ( 'Calorie burn:[CR]' + Iii11 + ' - ' + iII1Ii1ii111 + ' Average = ' + iII11IIi1I1 + '[CR][CR]Difficulty = ' + o00o0o + '[CR][CR]Equipment Needed: ' + ooOoOo + '[CR][CR]Focus: ' + oO0oo0o00O0 ) . replace ( '"' , '' ) )
  O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 for url in IIi11i1i1iI1 :
  oOo0 ( 'NEXT' , ( 'https://www.fitnessblender.com/videos' + url ) . replace ( '\/' , '' ) , 7085 , I1IIIii + 'Next.png' )
  if 51 - 51: I1ii11iIi11i + iiiiiiii1 * oOo
def II1I ( url , iconimage , description ) :
 oOOo0 = i11111IIIII ( url )
 Ooo0oOooo0 = iconimage
 ooo0O0o00O = description
 iI111i = re . compile ( '<div class="responsive-video">.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp' , re . DOTALL ) . findall ( oOOo0 )
 for url in iI111i :
  O0O0ooOOO ( 'PLAY' , url , 8043 , Ooo0oOooo0 , '' , ooo0O0o00O )
  O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 O0OO0ooO0oO0O0 = re . compile ( '<div class="article__content">(.+?)</div>' , re . DOTALL ) . findall ( oOOo0 )
 for II1iIiIiIIi in O0OO0ooO0oO0O0 :
  OOo = ( II1iIiIiIIi ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o00oOOooOOo0o ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + Ooo0oOooo0 , '' , OOo )
  if 53 - 53: i1iIi - OoOo0o
def O0OoO0OOOo ( INFO ) :
 OoOoO ( 'info for workout' , INFO )
 if 32 - 32: iiiiiiii1 - iiiiiiii1 / oOo % iI11I1II1I1I / oOoO0o00OO0 / I11i1ii1
 if 11 - 11: i1IiiiI1iI
 if 59 - 59: OoOo0o - O0Oooo0O - IIiIiII11i / ooOoO0O00 * OoOo0o . ii
def I1iiII11i11iI ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  oOo0 ( ( i1I1i111Ii ) . replace ( 'SlyNet' , '' ) , url , 9031 , I1IIIii + 'Sport.png' )
def I11I1iI ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , url , 9032 , I1IIIii + 'icon.png' )
def OOoo00o0 ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , url in iI111i :
  if '=' in i1I1i111Ii :
   pass
  else :
   II1i11I1 ( ( i1I1i111Ii ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , I1IIIii + 'icon.png' )
def o0OO0iI1II1i1ii ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( i1iI1 )
 for i1I1i111Ii , url in iI111i :
  if '=' in i1I1i111Ii :
   pass
  else :
   II1i11I1 ( i1I1i111Ii , url , 222 , I1IIIii + 'icon.png' )
   if 63 - 63: I1ii11iIi11i . iiiiiiii1 . I11i1ii1 . I1ii11iIi11i + o0o00Oo0O . oOo0O0Ooo
   if 91 - 91: oOo % iii1i1iiiiIi / O0Oooo0O * i1iIi / I1ii11iIi11i
   if 50 - 50: oOOoOooOo
def iioOOo0OOOoo0 ( url ) :
 O0OOoOOO0oO ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , Ooo0oOooo0 , url in iI111i :
  if 'music' in url :
   O0OOoOOO0oO ( i1I1i111Ii , url , 90036 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   O0OOoOOO0oO ( i1I1i111Ii , url , 90039 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
def oOOoo0oO00o ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( i1iI1 )
 for i1I1i111Ii , url , Ooo0oOooo0 in iI111i :
  Ii111iIi1iIi ( i1I1i111Ii , url , 100009 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
  if 78 - 78: I11i1ii1 % iii1i1iiiiIi % oOo * OOOo00oo0oO . IIiIiII11i % O0Oooo0O
def o0oo ( url ) :
 O0OOoOOO0oO ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 i1iI1 = requests . get ( url ) . text
 ii11I1 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( i1iI1 )
 ii1 = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( i1iI1 )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( ii1 ) )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  IIiI = requests . get ( url ) . text
  OOO0o0OO00OO0 = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( IIiI )
  for iiIii in OOO0o0OO00OO0 :
   o0Oo0oO = requests . get ( iiIii ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( o0Oo0oO )
   for iIIi , I1iIi1i , i1iII1IiiIiI1 , oOoO , IIIi1I1IIii1II in iI111i :
    if iIIi == 'xyz' :
     i1I1IIIIiiiI11iII = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( i1I1i111Ii , i1I1IIIIiiiI11iII , 1001111 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
    else :
     i1I1IIIIiiiI11iII = 'http://' + oOoO + '.' + i1iII1IiiIiI1 + '.' + I1iIi1i + '.' + iIIi + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( i1I1i111Ii , i1I1IIIIiiiI11iII , 1001111 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
 for OOo0 in ii11I1 :
  O0OOoOOO0oO ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo0 , 1000111 , '' , '' , '' , '' )
  if 17 - 17: OoOo0o / Ii % o0o00Oo0O / O0Oooo0O
  if 61 - 61: IIiIiII11i / Ii * oOo0O0Ooo / o0o00Oo0O . i1IiiiI1iI
  if 67 - 67: iii1i1iiiiIi - oOOoOooOo - iI11I1II1I1I
def Ii1IiiI ( ) :
 O0OOoOOO0oO ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 73 - 73: OOOo00oo0oO / OoOo0o * IIiIiII11i % ii - ooOoO0O00 - oOOoOooOo
 if 43 - 43: ooo0O + i1iIi % oOo . O0Oooo0O + ooOoO0O00
def oOoOOO0O0O ( url , name ) :
 O0OOoOOO0oO ( name , '' , '' , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 i1iI1 = requests . get ( url ) . text
 ii11I1 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( i1iI1 )
 ii1 = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( i1iI1 )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( ii1 ) )
 for url , Ooo0oOooo0 , name in iI111i :
  IIiI = requests . get ( url ) . text
  OOO0o0OO00OO0 = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( IIiI )
  for iiIii in OOO0o0OO00OO0 :
   o0Oo0oO = requests . get ( iiIii ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( o0Oo0oO )
   for iIIi , I1iIi1i , i1iII1IiiIiI1 , oOoO , IIIi1I1IIii1II in iI111i :
    if iIIi == 'xyz' :
     i1I1IIIIiiiI11iII = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , i1I1IIIIiiiI11iII , 1001111 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
    else :
     i1I1IIIIiiiI11iII = 'http://' + oOoO + '.' + i1iII1IiiIiI1 + '.' + I1iIi1i + '.' + iIIi + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , i1I1IIIIiiiI11iII , 1001111 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
     if 90 - 90: ooo0O + iI11I1II1I1I / I1ii11iIi11i + oOo0O0Ooo + OOOo00oo0oO
 for OOo0 in ii11I1 :
  O0OOoOOO0oO ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo0 , 1003111 , '' , '' , '' , '' )
  if 60 - 60: oOo
  if 16 - 16: i1IiiiI1iI
def iII11i1 ( ) :
 O0OOoOOO0oO ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 58 - 58: iiiiiiii1
 if 77 - 77: I11i1ii1 % OOOo00oo0oO % oOo
 if 68 - 68: oOOoOooOo % i1IiiiI1iI - i1iIi . oOo
def i11IIiIi ( url , name ) :
 O0OOoOOO0oO ( name , '' , '' , '' , '' , '' , '' )
 O0OOoOOO0oO ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 i1iI1 = requests . get ( url ) . text
 ii11I1 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( i1iI1 )
 ii1 = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( i1iI1 )
 iI111i = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( ii1 ) )
 for url , Ooo0oOooo0 , name in iI111i :
  IIiI = requests . get ( url ) . text
  OOO0o0OO00OO0 = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( IIiI )
  for iiIii in OOO0o0OO00OO0 :
   o0Oo0oO = requests . get ( iiIii ) . text
   iI111i = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( o0Oo0oO )
   for iIIi , I1iIi1i , i1iII1IiiIiI1 , oOoO , IIIi1I1IIii1II in iI111i :
    if iIIi == 'xyz' :
     i1I1IIIIiiiI11iII = 'http://xyz.streamjunkie.tv/hls/' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , i1I1IIIIiiiI11iII , 1001111 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
    else :
     i1I1IIIIiiiI11iII = 'http://' + oOoO + '.' + i1iII1IiiIiI1 + '.' + I1iIi1i + '.' + iIIi + '/hls/,' + IIIi1I1IIii1II + ',.urlset/master.m3u8'
     Ii111iIi1iIi ( name , i1I1IIIIiiiI11iII , 1001111 , Ooo0oOooo0 , Ooo0oOooo0 , '' , '' )
     if 52 - 52: iii1i1iiiiIi . oOoO0o00OO0 . I1ii11iIi11i
 for OOo0 in ii11I1 :
  O0OOoOOO0oO ( '[COLORblue][B]NEXT[/B][/COLOR]' , OOo0 , 1005111 , '' , '' , '' , '' )
def IiiiI ( name , url ) :
 import urlresolver
 try :
  iiIIi = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiIIi , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 99 - 99: ii - ooOoO0O00 % ooo0O / ooo0O + I11i1ii1
 if 96 - 96: ii + OoOo0o - O0Oooo0O / OOOo00oo0oO % OOOo00oo0oO
 if 34 - 34: I11i1ii1
def o0OOO0Oo ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 iI111i = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  if 'Daily' in i1I1i111Ii :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 9008 , O0O )
def O0O00oo ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def iiIIIii ( url ) :
 II1i11I1 ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 II1i11I1 ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 II1i11I1 ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i1iI1 )
 for i1I1i111Ii , url in iI111i :
  II1i11I1 ( ( i1I1i111Ii ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 71 - 71: OoOo0o * iii1i1iiiiIi - i1IiiiI1iI . Ii
def i1111iII1 ( ) :
 i1iI1 = cloudflare . source ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  if '.m3u' in iiI :
   oOo0 ( ( i1I1i111Ii ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( o0oOoO00o ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + iiI ) , 9011 , I1IIIii + 'disclose.png' )
def I1I1iiI11I1 ( url ) :
 i1iI1 = cloudflare . source ( url )
 iI111i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i1iI1 )
 for i1I1i111Ii , url in iI111i :
  II1i11I1 ( ( i1I1i111Ii ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 36 - 36: OOOo00oo0oO - i1IiiiI1iI % i1IiiiI1iI - IIiIiII11i
def OO0o0o0oo0O ( ) :
 i1iI1 = i11111IIIII ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 iI111i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  if 'category' in iiI :
   oOo0 ( i1I1i111Ii , 'http://www.disclose.tv/' + iiI , 7010 , I1IIIii + 'disclose.png' )
   if 5 - 5: ooOoO0O00 - oOo0O0Ooo * oOo0O0Ooo
   if 49 - 49: O0Oooo0O
def iIii ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( i1iI1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( i1iI1 )
 for url , i1I1i111Ii , Ooo0oOooo0 in iI111i :
  oOo0 ( i1I1i111Ii , 'http://www.disclose.tv/' + url , 7011 , Ooo0oOooo0 )
 for url in next :
  oOo0 ( 'NEXT' , url , 7010 , I1IIIii + 'Next.png' )
  if 41 - 41: OOOo00oo0oO . O0Oooo0O + o0o00Oo0O - OOOo00oo0oO . iii1i1iiiiIi * oOo
  if 6 - 6: oOOoOooOo / OOOo00oo0oO % ooo0O + oOOoOooOo / IIiIiII11i - O0Oooo0O
def O000ooo ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( i1iI1 )
 OOoOOO000O0 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  if 'http' in url :
   II1i11I1 ( 'video/flv' , url , 222 , I1IIIii + 'disclose.png' )
 for url , i1I1i111Ii in IIi11i1i1iI1 :
  II1i11I1 ( i1I1i111Ii , url , 222 , I1IIIii + 'disclose.png' )
 for url in OOoOOO000O0 :
  II1i11I1 ( 'YT Link' , url , 8043 , I1IIIii + 'disclose.png' )
  if 32 - 32: OoOo0o + I11i1ii1
  if 36 - 36: i1IiiiI1iI + O0Oooo0O . OoOo0o % ooo0O / i1iIi * ooOoO0O00
def II1Oooo00oO0OO0o ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , I1IIIii + 'icon.png' )
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
   i1ii = i11111IIIII ( OOoOo )
   ii11iIIiiI1I = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( i1ii )
   for I1IiiI1ii1i in ii11iIIiiI1I :
    ooOoOO = False
    Resolve ( I1IiiI1ii1i )
    if 91 - 91: oOo0O0Ooo - ii - ii
 elif iI1iII111ii1I > 1 :
  if 69 - 69: iiiiiiii1 * Ii / ooOoO0O00
  for IiIi1iIIiII1i in O0o0ooO0oO0oO :
   Oo00Oo0o000 = i11111IIIII ( IiIi1iIIiII1i )
   oOo0ooOo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oo00Oo0o000 )
   iI1i1i = oOo0ooOo
   iI1i1i = ( str ( iI1i1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iI1i1i
   II1i11I1 ( 'DOUBLE LINK' , iI1i1i , 424 , '' )
   if 83 - 83: o0o00Oo0O
   for url in oOo0ooOo :
    oOo0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1 = Google . resolve ( url )
    except :
     pass
    try :
     IIIii1i = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1 ) )
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
 oOo0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , I1IIIii + 'Movies.png' )
 if 2 - 2: I11i1ii1 + i1IiiiI1iI / iI11I1II1I1I . Ii . ooOoO0O00 * oOOoOooOo
 oOo0 ( 'Search Movies' , '' , 7017 , I1IIIii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 14 - 14: I1ii11iIi11i . o0o00Oo0O - OOOo00oo0oO - Ii
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / oOOoOooOo
def oo0OoooOo0 ( ) :
 i1iI1 = i11111IIIII ( 'http://cnfstudio.com/' )
 iI111i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , 'http://cnfstudio.com/genre/' + iiI , 7003 , I1IIIii + 'icon.png' )
  if 61 - 61: IIiIiII11i . oOo - IIiIiII11i
iI111I11I1I1 = xbmcgui . Dialog ( )
if 75 - 75: I1ii11iIi11i - iii1i1iiiiIi + OOOo00oo0oO % ooOoO0O00 * OoOo0o
OOoO = '{UN},' ; oO0OI1Ii1 = '{IG},' ; OOoo0Oo00 = '{PL},' ; I11I11II11I = '{LO},' ; O00oo00O = '{LP},' ; oOoI11Iii1iIII1i = '{HA},' ; ooOOO000 = '{XD},' ; i1Ii1IiIii1I = '{TA},' ; i1iIII1Ii1 = '{DP},' ; o0Oo00OoO000O = '{JT},' ; II1iii = '{JJ},' ; O0oOOOO0o = '{MM},' ; OoOOO0 = '{FQ},' ; IiIio0oO0O = '{HH},'
if 28 - 28: o0o00Oo0O % IIiIiII11i / iii1i1iiiiIi / OoOo0o
def O0Oo ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( i1iI1 )
 Ii111IiiiIi = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( i1iI1 )
 for Ooo0oOooo0 , url , i1I1i111Ii in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , Ooo0oOooo0 )
 Ii111IiiiIi = Ii111IiiiIi
 for url in Ii111IiiiIi :
  oOo0 ( 'Next Page' , url , 7003 , I1IIIii + 'Next.png' )
  if 2 - 2: oOoO0o00OO0 - OoOo0o
def o0o0oO0OOo00Ooo00 ( url ) :
 if 26 - 26: oOo0O0Ooo * ii / oOo0O0Ooo . o0o00Oo0O . oOOoOooOo + o0o00Oo0O
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  IIIi1I1IIii1II = url + '&fv=&sou='
  IIIi1I1IIii1II = IIIi1I1IIii1II . replace ( 'player' , 'watch' )
  O0OI1i = i1IIi ( IIIi1I1IIii1II )
  O0OooOoO00 = i1IIi ( url )
  if 61 - 61: ooo0O + IIiIiII11i + OOOo00oo0oO + i1iIi / O0Oooo0O . iii1i1iiiiIi
  if 62 - 62: oOOoOooOo
def i1IIi ( url ) :
 if 13 - 13: ooOoO0O00 / oOo0O0Ooo . o0o00Oo0O * ooOoO0O00
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( i1iI1 )
 for url in iI111i :
  o00oOOo ( url )
  if 93 - 93: oOoO0o00OO0 . oOo
  if 67 - 67: IIiIiII11i + ii + oOo0O0Ooo
def oooOO ( ) :
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , I1IIIii + 'LocalM3U.png' , Oo00OOOOO , '' )
 o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , I1IIIii + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 81 - 81: ooo0O + IIiIiII11i % O0Oooo0O - OOOo00oo0oO + oOOoOooOo - oOoO0o00OO0
def o00i1iII11iIiiI1 ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  i1IIiO0o0O = open ( O0OoO000O0OO , 'r' )
  for ii1IIII in i1IIiO0o0O :
   oo0O = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ii1IIII )
   for i1I1i111Ii , iiI in oo0O :
    II1i11I1 ( i1I1i111Ii , iiI , 222 , I1IIIii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 81 - 81: OOOo00oo0oO . oOo % OoOo0o - iiiiiiii1 * iI11I1II1I1I . iI11I1II1I1I
def iiI1iiIi ( url ) :
 if os . path . exists ( Remote ) :
  oOOo0 = i1I1 ( url )
  iI111i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
  for i1I1i111Ii , url in iI111i :
   url = ( url ) . strip ( )
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 56 - 56: iii1i1iiiiIi - I11i1ii1
  if 53 - 53: oOoO0o00OO0 - IIiIiII11i . Ii
def Iii1I1I11iiI1 ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for iiI in iI111i :
  iiI = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iiI
 i1I1i111Ii = 'plugin.video.GenieTv'
 if 76 - 76: iI11I1II1I1I - I1ii11iIi11i
 OOo00o000oOO0 ( iiI , i1I1i111Ii )
 if 1 - 1: OOOo00oo0oO / I1ii11iIi11i * oOOoOooOo + iii1i1iiiiIi - iI11I1II1I1I / ooo0O
def o0OOOO00O0Oo ( ) :
 oOOo0 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 iI111i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOo0 )
 for iiI in iI111i :
  iiI = o0oOoO00o ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iiI
 i1I1i111Ii = 'repository.GenieTv'
 if 86 - 86: oOo0O0Ooo
 OOo00o000oOO0 ( iiI , i1I1i111Ii )
 if 63 - 63: oOo0O0Ooo % OOOo00oo0oO / iI11I1II1I1I * i1iIi % OoOo0o . IIiIiII11i
 if 56 - 56: I11i1ii1 / Ii . ooo0O . OOOo00oo0oO - Ii
def iI1i1IIiiiI11 ( ) :
 OoO = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OoO )
 if iiI1IIIi == 0 :
  I1IiO00Oo0OoO00OO ( )
 if iiI1IIIi == 1 :
  OoOOoo ( )
  if 5 - 5: ooOoO0O00 + i1iIi
  if 38 - 38: oOo0O0Ooo . o0o00Oo0O + OoOo0o / oOoO0o00OO0 . iI11I1II1I1I - ooOoO0O00
  if 3 - 3: I1ii11iIi11i + OOOo00oo0oO
  if 65 - 65: oOo0O0Ooo / iii1i1iiiiIi % oOo0O0Ooo * Ii * ii / i1IiiiI1iI
O0oo0OO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
i1111 = xbmc . translatePath ( 'special://home/' )
o0oO0 = xbmcgui . DialogProgress ( )
oooo0 = 'https://addons.tvaddons.ag/'
if 31 - 31: O0Oooo0O + iI11I1II1I1I + oOo0O0Ooo - oOOoOooOo / O0Oooo0O
def OoOOoo ( ) :
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 iI11IIi1iiI1I = 'https://addons.tvaddons.ag/search/?keyword=' + i1oOOOOOOOoO
 oOOo0 = i11111IIIII ( iI11IIi1iiI1I )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for iiI , i11I1 , i1I1i111Ii in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , iiI , 10054 , 'https://addons.tvaddons.ag/' + i11I1 , Oo00OOOOO , '' )
  if 39 - 39: I1ii11iIi11i - ii . ooOoO0O00 + ooOoO0O00 % i1iIi . OoOo0o
  if 30 - 30: o0o00Oo0O / OOOo00oo0oO
def I1IiO00Oo0OoO00OO ( ) :
 oOOo0 = i11111IIIII ( oooo0 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  if 'Repositories' in i1I1i111Ii :
   pass
  elif 'Services' in i1I1i111Ii :
   pass
  elif 'International' in i1I1i111Ii :
   pass
  else :
   o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , iiI , 10053 , 'https://addons.tvaddons.ag/' + Ooo0oOooo0 , Oo00OOOOO , '' )
   if 93 - 93: I1ii11iIi11i
   if 5 - 5: iiiiiiii1
def Addon ( url ) :
 oOOo0 = i11111IIIII ( url )
 ii11I1 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oOOo0 )
 iI111i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOo0 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  if 'Please' in i1I1i111Ii :
   pass
  else :
   O0O0ooOOO ( i1I1i111Ii , url , 10054 , 'https://addons.tvaddons.ag/' + Ooo0oOooo0 , Oo00OOOOO , '' )
 for url in ii11I1 :
  o00oOOooOOo0o ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , I1IIIii + 'Next.png' , Oo00OOOOO , '' )
  if 61 - 61: OoOo0o * oOo - o0o00Oo0O
  if 30 - 30: iI11I1II1I1I
def iI11Ii ( url , name ) :
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)"' ) . findall ( oOOo0 )
 for url in iI111i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oO0 = xbmcgui . DialogProgress ( )
   o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   II1iI1I11I = os . path . join ( OOooo0O0o0 , name + '.zip' )
   try :
    os . remove ( II1iI1I11I )
   except :
    pass
   downloader . download ( url , II1iI1I11I , o0oO0 )
   o0OO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print o0OO0
   print '======================================='
   extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
   oooiiI ( )
   if 18 - 18: iii1i1iiiiIi - Ii * ooOoO0O00
def OOo00o000oOO0 ( url , name ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , name + '.zip' )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 o0OO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oO0 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( II1iI1I11I , o0OO0 , o0oO0 )
 oooiiI ( )
 if 13 - 13: ooOoO0O00 . oOoO0o00OO0 * ooo0O
def oooiiI ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 31 - 31: Ii % oOo . Ii % OOOo00oo0oO - ooOoO0O00
 if 62 - 62: OOOo00oo0oO + OOOo00oo0oO . ii
def oo0IIII1 ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
 for url , i11I1 , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , url , 1007 , i11I1 )
def II1ii111 ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
 for url , i11I1 , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 1006 , i11I1 )
  if 14 - 14: OoOo0o * iii1i1iiiiIi
def OoII1ii1iI1111 ( ) :
 i1iI1 = i11111IIIII ( o0oOoO00o ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , i1I , ooo0O0o00O , oo0o0000 , i1I1i111Ii in iI111i :
  IIIiIIIi111iI ( i1I1i111Ii , 100109 , iiI , image = i1I , isFolder = True )
  if 43 - 43: o0o00Oo0O + iii1i1iiiiIi / I11i1ii1
def IiIiI1 ( url ) :
 import random
 oooI11Ii1 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oooI11Ii1 . clear ( )
 iii1iIIi1ii = [ ]
 iI1iIII = [ ]
 iiiI11iii11iI = [ ]
 oOOo0 = i11111IIIII ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOo0 )
 for I1 , i1I , ooo0O0o00O , oo0o0000 , i1I1i111Ii in iI111i :
  iii1iIIi1ii . append ( [ I1 , i1I1i111Ii ] )
  if len ( iii1iIIi1ii ) == len ( iI111i ) :
   for ii1IIII in iii1iIIi1ii :
    iIII = random . randint ( 1 , len ( iii1iIIi1ii ) )
    try :
     iIiII1iiiii = iii1iIIi1ii [ int ( iIII ) ]
    except :
     pass
    if len ( iI1iIII ) <= 20 :
     if iIiII1iiiii [ 1 ] not in iiiI11iii11iI :
      oo00O00oO = i11111IIIII ( iIiII1iiiii [ 0 ] )
      OOoOOO000O0 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oo00O00oO )
      for OooO0O , Oo0o in OOoOOO000O0 :
       ooo00OOOooO = i11111IIIII ( OooO0O )
       IiIIiii11II1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( ooo00OOOooO )
       for iiiI1I , IIIi1I1IIii1II in IiIIiii11II1 :
        if 'panda' in IIIi1I1IIii1II :
         i1i1iiIIiiiII = i11111IIIII ( IIIi1I1IIii1II )
         iiii1i1II1 = re . compile ( "url: '(.+?)'" ) . findall ( i1i1iiIIiiiII )
         for Ii1Ii in iiii1i1II1 :
          if 'http' in Ii1Ii :
           ooooo0OoO0 = xbmcgui . ListItem ( iIiII1iiiii [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : iIiII1iiiii [ 1 ] } )
           ooooo0OoO0 . setProperty ( "IsPlayable" , "true" )
           oooI11Ii1 . add ( Ii1Ii , ooooo0OoO0 )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooooo0OoO0 )
           if 3 - 3: oOo0O0Ooo + oOoO0o00OO0 * O0Oooo0O - ooOoO0O00 . OoOo0o
def IIIiIIIi111iI ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 ooo0oo00O00oO = sys . argv [ 0 ]
 ooo0oo00O00oO += '?mode=' + str ( mode )
 ooo0oo00O00oO += '&title=' + urllib . quote_plus ( name )
 ooo0oo00O00oO += '&image=' + urllib . quote_plus ( image )
 ooo0oo00O00oO += '&page=' + str ( page )
 if url != '' :
  ooo0oo00O00oO += '&url=' + urllib . quote_plus ( url )
 if keyword :
  ooo0oo00O00oO += '&keyword=' + urllib . quote_plus ( keyword )
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  ooooo0OoO0 . addContextMenuItems ( contextMenu )
 if infoLabels :
  ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  ooooo0OoO0 . setProperty ( "IsPlayable" , "true" )
 ooooo0OoO0 . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = isFolder )
 if 21 - 21: OoOo0o + ooo0O
 if 39 - 39: iii1i1iiiiIi . i1IiiiI1iI * OoOo0o . ooOoO0O00
def oooOOO00o0 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
 for url , iconimage , ooo0O0o00O , oo0o0000 , name in iI111i :
  if 'http' in url :
   if '.php' in url :
    IIii1I1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
    for ii1IIII in IIii1I1i :
     if ii1IIII == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    O0O0oOo0o0o0 ( name , url , 1016 , iconimage , oo0o0000 , ooo0O0o00O )
   else :
    if 'youtube' in url :
     IIii1I1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for ii1IIII in IIii1I1i :
      if ii1IIII == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iI11IiiI1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oo0o0000 , ooo0O0o00O )
    else :
     IIii1I1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
     for ii1IIII in IIii1I1i :
      if ii1IIII == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iI11IiiI1 ( name , url , 222 , iconimage , oo0o0000 , ooo0O0o00O )
     O00oO000O0O ( 'tvshows' , 'Media Info 3' )
  else :
   o0OoOooo ( url , iconimage , name )
   if 88 - 88: ii % IIiIiII11i + I11i1ii1 + I11i1ii1 * I1ii11iIi11i
 else :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
  for url , i11I1 , name in iI111i :
   if 'http' in url :
    if '.php' in url :
     oOo0 ( name , url , 1016 , i11I1 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      II1i11I1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11I1 )
     else :
      IIii1I1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0 ) )
      for ii1IIII in IIii1I1i :
       if ii1IIII == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      II1i11I1 ( name , url , 222 , i11I1 )
      O00oO000O0O ( 'tvshows' , 'Media Info 3' )
   else :
    o0OoOooo ( url , i11I1 , name )
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 81 - 81: oOo0O0Ooo * oOOoOooOo + O0Oooo0O
def o0OoOooo ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 Ii1I1iIiIi = ( url ) . replace ( O0OoOo , 'http' ) . replace ( oO0Ooo , '.com' ) ;
 O0oOooOoOo = ( Ii1I1iIiIi ) . replace ( o0Ooo0Oooo0o , 'a' ) . replace ( iiiI1i , 'b' ) . replace ( O0OooO00O0 , 'c' ) . replace ( o00OO0Oo0Oo , 'd' ) . replace ( OOoo0Oo00 , 'e' ) . replace ( o0Oo00OoO000O , 'f' ) ;
 o0oiIIIiii = ( O0oOooOoOo ) . replace ( ooOO , 'g' ) . replace ( oOoI11Iii1iIII1i , 'h' ) . replace ( iiiiIIiiII1Iii1 , 'i' ) . replace ( o0oOOoO0o0 , 'j' ) . replace ( iiI1i111I1 , 'k' ) . replace ( iiIi11i1I1 , 'l' ) ;
 I11iI = ( o0oiIIIiii ) . replace ( I1i1iII11 , 'm' ) . replace ( O0O0O0oOO , 'n' ) . replace ( IiI111ii , 'o' ) . replace ( IiIoOO0ooO000 , 'p' ) . replace ( ooI11 , 'q' ) . replace ( OOoOo0Oo , 'r' ) ;
 oOo0o0O = ( I11iI ) . replace ( I1I1Ii111 , 's' ) . replace ( I1OooOo0o0Oo0 , 't' ) . replace ( o0o0o0oO0oOoo , 'u' ) . replace ( Ooi1I11i1 , 'v' ) . replace ( II1iiiii , 'w' ) . replace ( iI11iIiIiiiI , 'x' ) ;
 I1oo0Oo = ( oOo0o0O ) . replace ( I1OO0Oo0 , 'y' ) . replace ( iI1IIiI1 , 'z' ) . replace ( OOoO , '.' ) . replace ( oO0OI1Ii1 , '(' ) . replace ( I11I11II11I , ')' ) . replace ( O00oo00O , '/' ) ;
 iIIii111i1 = ( I1oo0Oo ) . replace ( ooOO0 , '1' ) . replace ( i11iI1i11I111 , '2' ) . replace ( iIIIIi , '3' ) . replace ( i1Ii1IiIii1I , '4' ) . replace ( i1iIII1Ii1 , '5' ) . replace ( OOo0O0O000 , '6' ) ;
 iiI1 = ( iIIii111i1 ) . replace ( II1iii , '7' ) . replace ( O0oOOOO0o , '8' ) . replace ( OoOOO0 , '9' ) . replace ( IiIio0oO0O , '0' ) . replace ( I1IiIIIII1iII1 , ':' ) . replace ( OO0oOoO0O0 , '%' ) ;
 url = ( iiI1 ) . replace ( iIi1I111Ii1I1 , '-' ) . replace ( ooOOO000 , '_' ) ;
 II1i11I1 ( name , url , 222 , iconimage ) ;
 if 51 - 51: OoOo0o + o0o00Oo0O
 if 91 - 91: Ii + ooo0O % oOo / OOOo00oo0oO - ooOoO0O00
def O0ii1IIIiiI1i ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
 for iiI , i11I1 , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , iiI , 1007 , i11I1 )
def Iiii1IIII11I1i ( url ) :
 if 87 - 87: i1iIi * O0Oooo0O + iI11I1II1I1I * ooo0O * iI11I1II1I1I . i1IiiiI1iI
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
 for url , i11I1 , i1I1i111Ii in iI111i :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 1006 , i11I1 )
  if 66 - 66: i1iIi / oOo . o0o00Oo0O . i1IiiiI1iI % ii / OoOo0o
def III11II111111 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 IiIi1ii111i1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 IiIi1ii111i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiIi1ii111i1 )
 if 59 - 59: i1IiiiI1iI + i1iIi + oOo
 if 46 - 46: i1IiiiI1iI - I1ii11iIi11i
def Oo0O00O ( url ) :
 i1iI1 = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1iI1 )
 for url , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  if '-dir-' in i1I1i111Ii :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , Ooo0oOooo0 )
  else :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' , url , 1006 , Ooo0oOooo0 )
   if 86 - 86: Ii % OOOo00oo0oO
def iii11I1I1i1 ( url ) :
 i1iI1 = i1I1 ( url )
 OOoo = ( 'http://afewbitsmore.com/' )
 iI111i = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  if '[To Parent Directory]' in i1I1i111Ii :
   i1I1i111Ii = 'HOME'
   pass
  elif 'HOME' in i1I1i111Ii :
   pass
  elif '.m3u' in i1I1i111Ii :
   oOo0 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , OOoo + url , 2002 , I1IIIii + 'music.png' )
  elif '.mp3' in i1I1i111Ii :
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OOoo + url , 222 , I1IIIii + 'music.png' )
  elif '.m4a' in i1I1i111Ii :
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OOoo + url , 222 , I1IIIii + 'music.png' )
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) , OOoo + url , 1012 , I1IIIii + 'music.png' )
def oooOoo0oo00OooOO ( url ) :
 oOOo0 = i1I1 ( url )
 iI111i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOo0 )
 for Ooo0oOooo0 , i1I1i111Ii , url in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , I1IIIii + 'music.png' )
  if 72 - 72: O0Oooo0O * I11i1ii1 - ooOoO0O00 * ooo0O / i1IiiiI1iI
def IiIIiii1II1ii1i1IiIIi ( url ) :
 i1iI1 = i1I1 ( url )
 OOoo = url
 iI111i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  if '.mp3' in i1I1i111Ii :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , I1IIIii + 'music.png' )
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '/' , '' ) , OOoo + url , 1011 , I1IIIii + 'music.png' )
def oo000Ooo ( ) :
 i1iI1 = i1I1 ( o0oOoO00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iI111i = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( i1iI1 )
 for iiI , Ooo0oOooo0 , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , ( 'http://www.cyn.net/music/' + iiI ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + Ooo0oOooo0 ) . replace ( ' ' , '%20' ) )
def OOoOoo00oO ( url , img ) :
 i1iI1 = i1I1 ( url )
 I1 = url
 img = img
 iI111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( I1 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 56 - 56: iI11I1II1I1I / oOo * OoOo0o
def i1iI1i11iIi1 ( url ) :
 i1iI1 = i1I1 ( url )
 I1 = url
 iI111i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 )
 for type , url , i1I1i111Ii in iI111i :
  if '[VID]' in type :
   II1i11I1 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , I1 + url , 222 , I1IIIii + 'music.png' )
  if '[DIR]' in type :
   i1iI1i11iIi1 ( I1 + url )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: ii % I11i1ii1 / O0Oooo0O * i1IiiiI1iI + ooOoO0O00 % Ii
 if 91 - 91: Ii
def OOoOOO0 ( ) :
 IIiiiiiIiIIi = ( o0oOoO00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 O0ooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1oOOOOOOOoO = O0ooOO . lower ( )
 iiI = ( o0oOoO00o ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 III11I1 = ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1 = ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + O0Oooo0O . ooo0O * Ii
 oOOo0 = i1Oo00 ( iiI )
 II1iII1i1i = i1Oo00 ( III11I1 )
 oo00O00oO = i1Oo00 ( I1 )
 if 53 - 53: OoOo0o / oOo0O0Ooo / OOOo00oo0oO * OoOo0o / ooOoO0O00 - O0Oooo0O
 if oOOo0 != 'Failed' :
  iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo0 )
  for iiI , i1I , ooo0O0o00O , oOoOo0OOOOO , i1I1i111Ii in iI111i :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    o00oOOooOOo0o ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , iiI , 1016 , i1I , oo0o0000 , ooo0O0o00O )
    if 71 - 71: o0o00Oo0O + I1ii11iIi11i % OOOo00oo0oO - ooo0O
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if II1iII1i1i != 'Failed' :
  I1iii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II1iII1i1i )
  for iiI , i1I1i111Ii in I1iii11 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + iiI ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
    if 82 - 82: iI11I1II1I1I
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
 if oo00O00oO != 'Failed' :
  IIi11i1i1iI1 = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( oo00O00oO )
  for iiI , i1I1i111Ii in IIi11i1i1iI1 :
   if O0ooOO in i1I1i111Ii . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( o0oOoO00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + iiI ) . replace ( ' ' , '%20' ) , 1006 , I1IIIii + 'Music.png' )
    if 64 - 64: oOOoOooOo + oOo0O0Ooo % OoOo0o + IIiIiII11i
    O00oO000O0O ( 'tvshows' , 'Media Info 3' )
    if 46 - 46: oOo0O0Ooo
    if 72 - 72: iiiiiiii1
    if 100 - 100: oOo0O0Ooo
    if 55 - 55: ooOoO0O00 % I11i1ii1
    if 44 - 44: OOOo00oo0oO - iI11I1II1I1I / oOOoOooOo - iI11I1II1I1I % ooOoO0O00 + oOOoOooOo
    if 74 - 74: i1IiiiI1iI . iii1i1iiiiIi + iii1i1iiiiIi
I1i1iII11 = '{SF},' ; O0O0O0oOO = '{IF},' ; IiI111ii = '{PW},' ; iIIIIi = '{AM},' ; IiIoOO0ooO000 = '{GF},' ; ooI11 = '{DD},' ; OOoOo0Oo = '{UO},' ; I1I1Ii111 = '{LE},' ; o0o0o0oO0oOoo = '{ZY},' ; Ooi1I11i1 = '{UE},' ; II1iiiii = '{PE},' ; iI11iIiIiiiI = '{JE},' ; I1OO0Oo0 = '{TH},' ; iI1IIiI1 = '{LK},'
if 87 - 87: I11i1ii1 + ooo0O . ooOoO0O00 % O0Oooo0O
if 44 - 44: I1ii11iIi11i - OoOo0o . i1iIi * ii
def oOOO0 ( ) :
 i1iI1 = i11111IIIII ( 'http://www.iwatchseries.me/tv-list/' )
 iI111i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , iiI , 8021 , I1IIIii + 'iwatch.png' )
  O00oO000O0O ( 'movies' , 'MAIN' )
def II1I111iiI1I ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii , o0OO0Oo in iI111i :
  oOo0 ( i1I1i111Ii + o0OO0Oo , url , 8022 , I1IIIii + 'iwatch.png' )
def iIiiIIiIi ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( i1iI1 )
 for url in iI111i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  Oo000o0o ( url )
def Oo000o0o ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( i1iI1 )
 IIi11i1i1iI1 = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( i1iI1 )
 OOoOOO000O0 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( i1iI1 )
 IiIIiii11II1 = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  II1i11I1 ( 'VidSpot - ' + i1I1i111Ii , url , 222 , I1IIIii + 'iwatch.png' )
 for url in IIi11i1i1iI1 :
  II1i11I1 ( 'VodLocker' , url , 222 , I1IIIii + 'iwatch.png' )
 for url , i1I1i111Ii in IiIIiii11II1 :
  II1i11I1 ( 'VidUp' + i1I1i111Ii , url , 222 , I1IIIii + 'iwatch.png' )
 for i1I1i111Ii , url in OOoOOO000O0 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   II1i11I1 ( 'TheVideo - ' + i1I1i111Ii , url , 222 , I1IIIii + 'iwatch.png' )
   if 95 - 95: oOoO0o00OO0 + oOOoOooOo - iI11I1II1I1I
def OOoOoo0Oo0Oo ( ) :
 i1iI1 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 iI111i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , iiI , 1021 , I1IIIii + 'anime.png' )
  if 72 - 72: i1IiiiI1iI / ii
  if 95 - 95: oOo0O0Ooo * Ii + Ii / iI11I1II1I1I
def iiIiI1iiI1 ( ) :
 i1iI1 = i11111IIIII ( 'http://www.animetoon.org/cartoon' )
 iI111i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( i1iI1 )
 for iiI , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , iiI , 1002 , I1IIIii + 'anime.png' )
  if 41 - 41: oOOoOooOo + I11i1ii1 . ooOoO0O00 + iI11I1II1I1I
  if 57 - 57: Ii * OOOo00oo0oO * Ii
  if 14 - 14: I1ii11iIi11i / i1IiiiI1iI
def III1I11i ( url ) :
 i1iI1 = i11111IIIII ( url )
 IIi11i1i1iI1 = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( i1iI1 )
 for Ooo0oOooo0 in IIi11i1i1iI1 :
  I1I1oOoooo0OooO = Ooo0oOooo0
 OOoOOO000O0 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( i1iI1 )
 for url in OOoOOO000O0 :
  oOo0 ( 'NEXT PAGE' , url , 1002 , I1IIIii + 'Next.png' )
 iI111i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( i1iI1 )
 for url , i1I1i111Ii in iI111i :
  oOo0 ( i1I1i111Ii , url , 1003 , I1I1oOoooo0OooO )
 xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0o00OO0OoO ( url , IMAGE ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( i1iI1 )
 for i1I1i111Ii , url in iI111i :
  print i1I1i111Ii + '     ' + url
  if 'easy' in url :
   Oo0ooo ( url )
  elif 'playpanda' in url :
   Oo0ooo ( url )
   if 39 - 39: ooo0O - I1ii11iIi11i % I11i1ii1
  xbmcplugin . addSortMethod ( IIIii1II1II , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0ooo ( url ) :
 i1iI1 = i11111IIIII ( url )
 iI111i = re . compile ( "url: '(.+?)'," ) . findall ( i1iI1 )
 for url in iI111i :
  II1i11I1 ( 'STREAM' , url , 222 , I1IIIii + 'anime.png' )
  if 20 - 20: ii / i1IiiiI1iI / O0Oooo0O / ooo0O + oOo
  if 17 - 17: oOo + IIiIiII11i + oOo0O0Ooo
def IIIiIIi1I1I ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i . add_header ( 'referer' , url )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 22 - 22: ooOoO0O00 / oOo * oOo0O0Ooo - I1ii11iIi11i - i1iIi
def i1I1 ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 80 - 80: oOOoOooOo . Ii
def i1iIi11 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 O0ooOooOOoo = ( '%s%s' % ( iI1IiII1II1I , url ) )
 IIIi1I1IIii1II = i1I1 ( url )
 iI111i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for url , i11I1 , i1I1i111Ii in iI111i :
  II1i11I1 ( '%s' % ( '[COLOR' + iiI1IiI + ']' + i1I1i111Ii + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , i11I1 )
  if 76 - 76: oOo % iii1i1iiiiIi * oOOoOooOo . oOo0O0Ooo
def O0oOoOO0oo ( url ) :
 if O0oo0OO0 . getSetting ( 'down' ) == 'true' :
  I1iiI1iIi1 ( url , i1I1i111Ii )
 else :
  IIIIiii1IIii ( url )
def IIIIiii1IIii ( url ) :
 import urlresolver
 try :
  iiIIi = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( iiIIi , xbmcgui . ListItem ( i1I1i111Ii ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( i1I1i111Ii ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def o00oOOo ( url ) :
 if 68 - 68: iii1i1iiiiIi / I11i1ii1
 IIII1iIIii = open ( O0Oo000ooO00 , "a" )
 IIII1iIIii . write ( 'url="' + url + '"\n' )
 IIII1iIIii . close
 if 76 - 76: i1IiiiI1iI % iI11I1II1I1I
 III11 = xbmc . Player ( Ii1Ii11Iii1i1 ( ) )
 import urlresolver
 try : III11 . play ( url )
 except : pass
 from urlresolver import common
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'LOADING' , 'Opening %s Now' % ( i1I1i111Ii ) )
 III11 = xbmc . Player ( Ii1Ii11Iii1i1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oO0 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : III11 . play ( url )
  except : pass
  try : O0oo0OO0 . resolve_url ( url )
  except : pass
  o0oO0 . close ( )
def I1iiI1iIi1 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  Iii1I = '.mp4'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.mkv' in url :
  Iii1I = '.mkv'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.mp3' in url :
  Iii1I = '.mp3'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.avi' in url :
  Iii1I = '.avi'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.mov' in url :
  Iii1I = '.mov'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.mpeg' in url :
  Iii1I = '.mpeg'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.mpg' in url :
  Iii1I = '.mpg'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.flv' in url :
  Iii1I = '.flv'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 elif '.wmv' in url :
  Iii1I = '.wmv'
  OoO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  iiI1IIIi = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OoO )
  if iiI1IIIi == 0 :
   IIIIiii1IIii ( url )
  if iiI1IIIi == 1 :
   Ii1IiIiI ( url , name , Iii1I )
 else :
  IIIIiii1IIii ( url )
def Ii1IiIiI ( url , name , cat ) :
 o0ooi1Ii ( )
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( II ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 II1iI1I11I = os . path . join ( OOooo0O0o0 , file )
 try :
  os . remove ( II1iI1I11I )
 except :
  pass
 downloader . download ( url , II1iI1I11I , o0oO0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def o0ooi1Ii ( ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( II ) )
 if not os . path . exists ( II ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
def o000OOooO0O ( url ) :
 o0oO0 = xbmcgui . DialogProgress ( )
 o0oO0 . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oO0 . update ( 0 , '%s' % i1I1i111Ii )
 xbmc . sleep ( 1 )
 III11 = xbmc . Player ( Ii1Ii11Iii1i1 ( ) )
 o0oO0 . update ( 100 , '%s' % i1I1i111Ii )
 xbmc . sleep ( 1 )
 III11 . play ( url ) . strip ( )
 o0oO0 . close ( )
 if 36 - 36: iii1i1iiiiIi / i1iIi . ii . oOo * ii
def O0O0oo ( url ) :
 III11 = xbmc . Player ( Ii1Ii11Iii1i1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : III11 . play ( url ) . strip ( )
 except : pass
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . iii1i1iiiiIi
def O00oo0ooo0O ( url ) :
 III11 = xbmc . Player ( Ii1Ii11Iii1i1 ( ) )
 import urlresolver
 iiIi1i1iI = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 III11 . play ( iiIi1i1iI )
 xbmc . sleep ( 1 )
 III11 . play ( url )
 if 34 - 34: i1IiiiI1iI
 if 95 - 95: oOo0O0Ooo . OOOo00oo0oO
def Ii1Ii11Iii1i1 ( ) :
 try :
  o00Oo000o00 = getSet ( "core-player" )
  if ( o00Oo000o00 == 'DVDPLAYER' ) : OoO0OOoO0OO0o = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o00Oo000o00 == 'MPLAYER' ) : OoO0OOoO0OO0o = xbmc . PLAYER_CORE_MPLAYER
  elif ( o00Oo000o00 == 'PAPLAYER' ) : OoO0OOoO0OO0o = xbmc . PLAYER_CORE_PAPLAYER
  else : OoO0OOoO0OO0o = xbmc . PLAYER_CORE_AUTO
 except : OoO0OOoO0OO0o = xbmc . PLAYER_CORE_AUTO
 return OoO0OOoO0OO0o
 return True
 if 18 - 18: IIiIiII11i . i1iIi + iii1i1iiiiIi + o0o00Oo0O - i1IiiiI1iI
def oOo0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1II1i = [ ]
  i1II1i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   i1II1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   i1II1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooooo0OoO0 . addContextMenuItems ( i1II1i )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = True )
 return oOO
 if 30 - 30: IIiIiII11i
def i1I1ii1 ( name , url , mode , iconimage , fanart , description ) :
 if 26 - 26: i1IiiiI1iI - ooOoO0O00 - I1ii11iIi11i * o0o00Oo0O * OoOo0o . ii
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = True )
 return oOO
 if 99 - 99: OOOo00oo0oO . oOo / OoOo0o
def II1i11I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1II1i = [ ]
  i1II1i . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   i1II1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   i1II1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooooo0OoO0 . addContextMenuItems ( i1II1i )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = False )
 return oOO
 if 12 - 12: iI11I1II1I1I + oOOoOooOo * O0Oooo0O % ii / iI11I1II1I1I
 if 43 - 43: o0o00Oo0O . ooOoO0O00 - ii - ooOoO0O00 - oOoO0o00OO0
 if 8 - 8: iii1i1iiiiIi / i1iIi
 if 12 - 12: iI11I1II1I1I
 if 52 - 52: OOOo00oo0oO . oOoO0o00OO0 + OOOo00oo0oO
 if 73 - 73: IIiIiII11i / Ii / oOOoOooOo
def I1iII1 ( url , heading , announce ) :
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
   try : o0OoOO = open ( announce ) ; i11I1i11IIIi = o0OoOO . read ( )
   except : i11I1i11IIIi = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i11I1i11IIIi ) )
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
   try : o0OoOO = open ( announce ) ; i11I1i11IIIi = o0OoOO . read ( )
   except : i11I1i11IIIi = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i11I1i11IIIi ) )
   return
 OoOoO ( )
 OoOoO ( )
def I1iiii1I ( ) :
 I1iII1 ( I1IIIii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 75 - 75: o0o00Oo0O + oOoO0o00OO0
 if 51 - 51: ooOoO0O00 + IIiIiII11i % OOOo00oo0oO
 if 72 - 72: OoOo0o + OoOo0o
 if 30 - 30: i1IiiiI1iI
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / i1iIi
def oooiiI ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
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
 if 3 - 3: OOOo00oo0oO + oOo - iiiiiiii1 / i1iIi
 if 58 - 58: i1iIi * i1IiiiI1iI
 if 95 - 95: OOOo00oo0oO
 if 49 - 49: oOo0O0Ooo
def ii11IiIiiIIi ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o0Oo0OOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 73 - 73: iii1i1iiiiIi % OOOo00oo0oO / o0o00Oo0O - ii
def oo0O0OOo0 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + oO000Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 100 - 100: oOoO0o00OO0 . oOOoOooOo
def i11iIIi1Ii1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + II1iI11ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 50 - 50: ii + ii % I1ii11iIi11i
def Oo0oOOoIIiIi ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iii111iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 59 - 59: iii1i1iiiiIi . i1IiiiI1iI / ii - i1iIi * I11i1ii1
def IIoo000oOOo000 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + o0Ii11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 32 - 32: I1ii11iIi11i
def O0iI1iI1i1I ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Ii1I11II1i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 42 - 42: ooOoO0O00 . iii1i1iiiiIi * iii1i1iiiiIi * iii1i1iiiiIi
def iii1I11iI11i1 ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Iii1Iiii11i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 16 - 16: i1iIi % Ii
def o0o0OO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + oOOoOI1Ii1i111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 51 - 51: o0o00Oo0O + i1iIi * ii . OOOo00oo0oO + ii
def O0iI1Iii ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + iIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 42 , i1I , oo0o0000 , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 20 - 20: i1iIi * oOo0O0Ooo % OOOo00oo0oO / Ii . oOo
def IIOOO0O00O0OOOO ( url ) :
 IIIi1I1IIii1II = i11111IIIII ( str ( O00OOOoOoo0O ) + Ii11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI111i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for i1I1i111Ii , url , i1I , oo0o0000 , OoOOOo0 in iI111i :
  o00oOOooOOo0o ( i1I1i111Ii , url , 5 , I1IIIii + 'GenieTVRSSFeed.png' , I1IIIii + 'GenieTVRSSFeed.png' , OoOOOo0 )
 O00oO000O0O ( 'movies' , 'MAIN' )
 if 24 - 24: I1ii11iIi11i / O0Oooo0O
 if 74 - 74: IIiIiII11i * oOo . iiiiiiii1
 if 82 - 82: oOoO0o00OO0 / I1ii11iIi11i
 if 63 - 63: oOo0O0Ooo
 if 3 - 3: iiiiiiii1 + oOoO0o00OO0
 if 35 - 35: OOOo00oo0oO * iiiiiiii1 * OOOo00oo0oO * O0Oooo0O * I11i1ii1 * ooOoO0O00
 if 43 - 43: oOo * oOo0O0Ooo / I11i1ii1 . Ii + iiiiiiii1 + ooo0O
 if 1 - 1: oOo0O0Ooo % ooo0O . O0Oooo0O + i1IiiiI1iI * OOOo00oo0oO
 if 41 - 41: oOo * OOOo00oo0oO - IIiIiII11i
def I1I11Ii ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( o0 ) :
     Oo0oO000OOOO = 0
     Oo0oO000OOOO += len ( oOOOOOoOOoo0 )
     if Oo0oO000OOOO > 0 :
      for o0OoOO in oOOOOOoOOoo0 :
       os . unlink ( os . path . join ( i11ii11IiI1 , o0OoOO ) )
  ii1IiiIiI = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( ii1IiiIiI )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 73 - 73: ooOoO0O00 / oOOoOooOo
 if 62 - 62: ooo0O + oOOoOooOo . oOo0O0Ooo * O0Oooo0O
 if 65 - 65: i1IiiiI1iI + ooOoO0O00 % Ii + i1IiiiI1iI % IIiIiII11i
 if 18 - 18: iiiiiiii1 . ii - oOo / oOo0O0Ooo
 if 4 - 4: o0o00Oo0O
 if 87 - 87: I11i1ii1 - oOo * I1ii11iIi11i / ooo0O % OOOo00oo0oO % i1iIi
 if 25 - 25: i1iIi - oOoO0o00OO0 + I1ii11iIi11i . oOo0O0Ooo
 if 36 - 36: iiiiiiii1
def oOoO00o ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 3 - 3: i1iIi
def Ii1Iii11i ( url ) :
 ii11IiI = os . path . join ( oO0o0o0ooO0oO , 'addon_data' )
 I1II11IIi11i = [
 ( ii11IiI ) ,
 ( I11 ) ,
 ( os . path . join ( i1111 , 'cache' ) ) ,
 ( os . path . join ( i1111 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I11 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( ii11IiI , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( ii11IiI , 'plugin.video.itv' , 'Images' ) ) ]
 if 87 - 87: ooo0O + Ii % oOo0O0Ooo / O0Oooo0O . i1IiiiI1iI
 iIiII = 0
 if 75 - 75: ooo0O / ii % oOo / iii1i1iiiiIi + iiiiiiii1
 for ii1IIII in I1II11IIi11i :
  if os . path . exists ( ii1IIII ) and not ii1IIII in [ I11 , ii11IiI ] :
   for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( ii1IIII ) :
    Oo0oO000OOOO = 0
    Oo0oO000OOOO += len ( oOOOOOoOOoo0 )
    if Oo0oO000OOOO > 0 :
     for o0OoOO in oOOOOOoOOoo0 :
      if not o0OoOO in oo0o0O00 :
       try :
        os . unlink ( os . path . join ( i11ii11IiI1 , o0OoOO ) )
       except :
        pass
      else : OOoOooOoOOOoo ( 'Ignore Log File: %s' % o0OoOO )
     for oOoO in Iiiiii :
      try :
       shutil . rmtree ( os . path . join ( i11ii11IiI1 , oOoO ) )
       iIiII += 1
       OOoOooOoOOOoo ( "[Success] cleared %s files from %s" % ( str ( Oo0oO000OOOO ) , os . path . join ( ii1IIII , oOoO ) ) )
      except :
       OOoOooOoOOOoo ( "[Failed] to wipe cache in: %s" % os . path . join ( ii1IIII , oOoO ) )
  else :
   for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( ii1IIII ) :
    for oOoO in Iiiiii :
     if 'cache' in oOoO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( i11ii11IiI1 , oOoO ) )
       iIiII += 1
       OOoOooOoOOOoo ( "[Success] wiped %s " % os . path . join ( ii1IIII , oOoO ) )
      except :
       OOoOooOoOOOoo ( "[Failed] to wipe cache in: %s" % os . path . join ( ii1IIII , oOoO ) )
       if 91 - 91: iI11I1II1I1I / IIiIiII11i + I1ii11iIi11i
 oOoO00o ( oOo0oooo00o , 'Clear Cache: Removed %s Files' % iIiII )
 if 47 - 47: I11i1ii1 % O0Oooo0O + oOo
 if 32 - 32: OOOo00oo0oO
 if 91 - 91: iiiiiiii1 - iii1i1iiiiIi / I1ii11iIi11i % IIiIiII11i / IIiIiII11i / ooo0O
 if 34 - 34: oOo * IIiIiII11i + Ii % i1iIi
 if 25 - 25: iii1i1iiiiIi + I11i1ii1 . Ii
 if 87 - 87: oOo0O0Ooo + ii + o0o00Oo0O
 if 32 - 32: i1iIi / oOoO0o00OO0 . i1iIi
def o00OOOoooo00 ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 o000iI11i1ii11i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( o000iI11i1ii11i11 ) :
   Oo0oO000OOOO = 0
   Oo0oO000OOOO += len ( oOOOOOoOOoo0 )
   if 59 - 59: oOo + OoOo0o . oOoO0o00OO0 - iiiiiiii1 % oOOoOooOo
   if 9 - 9: I11i1ii1
   if Oo0oO000OOOO > 0 :
    if 51 - 51: O0Oooo0O + o0o00Oo0O + iii1i1iiiiIi % o0o00Oo0O + OOOo00oo0oO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( Oo0oO000OOOO ) + " files found" , "Do you want to delete them?" ) :
     if 65 - 65: IIiIiII11i % oOoO0o00OO0 + OoOo0o + i1iIi
     for o0OoOO in oOOOOOoOOoo0 :
      os . unlink ( os . path . join ( i11ii11IiI1 , o0OoOO ) )
     for oOoO in Iiiiii :
      shutil . rmtree ( os . path . join ( i11ii11IiI1 , oOoO ) )
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
 oo0 ( )
 return
 if 39 - 39: Ii % iI11I1II1I1I + oOOoOooOo + Ii - o0o00Oo0O - i1IiiiI1iI
 if 71 - 71: ii . iii1i1iiiiIi % I11i1ii1 * iiiiiiii1 / OoOo0o
 if 63 - 63: o0o00Oo0O * o0o00Oo0O . I11i1ii1
 if 54 - 54: oOo0O0Ooo / ooOoO0O00 * oOoO0o00OO0
 if 10 - 10: oOo0O0Ooo % IIiIiII11i / oOo0O0Ooo
 if 13 - 13: IIiIiII11i - Ii
 if 90 - 90: i1IiiiI1iI . iii1i1iiiiIi % I1ii11iIi11i / O0Oooo0O . i1iIi % oOo
 if 32 - 32: oOo0O0Ooo + oOOoOooOo / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
 if 95 - 95: iiiiiiii1 / oOOoOooOo + O0Oooo0O
def IiI11ii1I ( url ) :
 print '###' + oo00 + ' - DELETING PACKAGES###'
 o000iI11i1ii11i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( o000iI11i1ii11i11 ) :
   Oo0oO000OOOO = 0
   Oo0oO000OOOO += len ( oOOOOOoOOoo0 )
   if 78 - 78: iI11I1II1I1I / oOo0O0Ooo - I11i1ii1
   if 81 - 81: oOoO0o00OO0
   if Oo0oO000OOOO > 0 :
    if 31 - 31: o0o00Oo0O % oOOoOooOo / oOo0O0Ooo * iiiiiiii1 % iI11I1II1I1I * iii1i1iiiiIi
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( Oo0oO000OOOO ) + " files found" , "Do you want to delete them?" ) :
     if 76 - 76: O0Oooo0O - o0o00Oo0O
     for o0OoOO in oOOOOOoOOoo0 :
      os . unlink ( os . path . join ( i11ii11IiI1 , o0OoOO ) )
     for oOoO in Iiiiii :
      shutil . rmtree ( os . path . join ( i11ii11IiI1 , oOoO ) )
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
 Ii1Iii11i ( url )
 return
 if 23 - 23: o0o00Oo0O * i1iIi * oOOoOooOo % oOOoOooOo
 if 7 - 7: IIiIiII11i + i1IiiiI1iI
 if 99 - 99: iI11I1II1I1I * OOOo00oo0oO
 if 37 - 37: oOOoOooOo * iiiiiiii1 * i1IiiiI1iI
 if 11 - 11: oOo0O0Ooo
 if 48 - 48: o0o00Oo0O . i1IiiiI1iI
 if 9 - 9: OOOo00oo0oO / I1ii11iIi11i
 if 85 - 85: Ii / oOo0O0Ooo . oOo . i1IiiiI1iI . OOOo00oo0oO * I11i1ii1
 if 41 - 41: i1iIi / oOo / oOo * i1IiiiI1iI
 if 31 - 31: i1iIi / ii % iI11I1II1I1I - I11i1ii1 * oOo0O0Ooo - o0o00Oo0O
def i1iIi1II1 ( url , name ) :
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i11IiIi1Ii1 = os . path . join ( OOooo0O0o0 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 o0Oo0OOoOOO000 = os . path . join ( OOooo0O0o0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( o0Oo0OOoOOO000 ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + oo00 + ' - ADVANCED XML###'
   OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   i11IiIi1Ii1 = os . path . join ( OOooo0O0o0 , 'advancedsettings.xml' )
   try :
    os . remove ( i11IiIi1Ii1 )
    print '=== GenieTv - REMOVING    ' + str ( i11IiIi1Ii1 ) + '    ==='
   except :
    pass
   IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
   iIIi = open ( i11IiIi1Ii1 , "w" )
   iIIi . write ( IIIi1I1IIii1II )
   iIIi . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( i11IiIi1Ii1 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 else :
  print '###' + oo00 + ' - ADVANCED XML###'
  OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  i11IiIi1Ii1 = os . path . join ( OOooo0O0o0 , 'advancedsettings.xml' )
  try :
   os . remove ( i11IiIi1Ii1 )
   print '=== GenieTv - REMOVING    ' + str ( i11IiIi1Ii1 ) + '    ==='
  except :
   pass
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iIIi = open ( i11IiIi1Ii1 , "w" )
  iIIi . write ( IIIi1I1IIii1II )
  iIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i11IiIi1Ii1 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "       Done Adding new Advanced XML" )
 return
 if 2 - 2: i1iIi . O0Oooo0O - iii1i1iiiiIi - i1iIi
def ooo0O0oOOo ( url , name ) :
 print '###' + oo00 + ' - CHECK ADVANCE XML###'
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i11IiIi1Ii1 = os . path . join ( OOooo0O0o0 , 'advancedsettings.xml' )
 try :
  iIIi = open ( i11IiIi1Ii1 ) . read ( )
  if 'zero' in iIIi :
   name = '0CACHE'
  elif 'tuxen' in iIIi :
   name = 'TUXENS'
  elif 'muckys' in iIIi :
   name = 'MUCKYS'
  elif 'p2p1' in iIIi :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iIIi :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iIIi :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( oo00 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 81 - 81: iI11I1II1I1I * IIiIiII11i + i1IiiiI1iI / Ii
def OO0oOOoOoo00o ( url ) :
 print '###' + oo00 + ' - DELETING ADVANCE XML###'
 OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i11IiIi1Ii1 = os . path . join ( OOooo0O0o0 , 'advancedsettings.xml' )
 try :
  os . remove ( i11IiIi1Ii1 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( i11IiIi1Ii1 ) + '    ==='
  iI111I11I1I1 . ok ( oo00 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "       No Advanced Settings To Remove" )
 return
 if 42 - 42: iii1i1iiiiIi / iiiiiiii1 + OoOo0o
 if 61 - 61: Ii % OOOo00oo0oO * oOOoOooOo
 if 59 - 59: OoOo0o + ooOoO0O00
 if 10 - 10: I1ii11iIi11i - ooOoO0O00 % oOoO0o00OO0
 if 54 - 54: I11i1ii1 + OoOo0o + OOOo00oo0oO * o0o00Oo0O % oOOoOooOo + oOo
 if 13 - 13: Ii * o0o00Oo0O . ii % O0Oooo0O + oOoO0o00OO0 + OoOo0o
 if 45 - 45: OOOo00oo0oO % Ii / i1iIi / I11i1ii1 % i1iIi - i1iIi
 if 73 - 73: oOoO0o00OO0 * oOoO0o00OO0 / IIiIiII11i % iiiiiiii1
 if 74 - 74: oOo / oOoO0o00OO0 - oOOoOooOo * ooOoO0O00 + oOoO0o00OO0 . i1IiiiI1iI
 if 13 - 13: iiiiiiii1 + ooo0O / iiiiiiii1 - i1iIi - iiiiiiii1
def I1IO0o0000oo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iI111i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for iIIII1i1 , iIIIi1I , OOOoOOoo , IiIi1i in iI111i :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iIIII1i1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % OOOoOOoo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % IiIi1i )
  inc = inc + 1
  if 35 - 35: OOOo00oo0oO / i1IiiiI1iI * ooo0O + IIiIiII11i + oOOoOooOo
  if 7 - 7: I1ii11iIi11i * O0Oooo0O * oOo0O0Ooo + iI11I1II1I1I
  if 75 - 75: OOOo00oo0oO
  if 50 - 50: OOOo00oo0oO / I1ii11iIi11i
  if 32 - 32: oOo % OOOo00oo0oO * oOoO0o00OO0 + i1IiiiI1iI / O0Oooo0O
  if 5 - 5: ooo0O + iiiiiiii1 / ii + i1iIi . iii1i1iiiiIi / OOOo00oo0oO
  if 18 - 18: IIiIiII11i . ooo0O
  if 75 - 75: ii - I1ii11iIi11i
  if 56 - 56: IIiIiII11i - Ii - OOOo00oo0oO . ooo0O
def i1Ii ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + oo00 + ' - CUSTOM FTV INI###'
  OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  i11IiIi1Ii1 = os . path . join ( OOooo0O0o0 , 'addons2.ini' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iIIi = open ( i11IiIi1Ii1 , "w" )
  iIIi . write ( IIIi1I1IIii1II )
  iIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i11IiIi1Ii1 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New .ini File" )
 return
 if 86 - 86: ooOoO0O00 + ooo0O % i1IiiiI1iI + oOo0O0Ooo . oOo / Ii
def iII111 ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + oo00 + ' - CUSTOM FTV SETTINGS###'
  OOooo0O0o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  i11IiIi1Ii1 = os . path . join ( OOooo0O0o0 , 'settings.xml' )
  IIIi1I1IIii1II = ii11iIi1I . http_GET ( url ) . content
  iIIi = open ( i11IiIi1Ii1 , "w" )
  iIIi . write ( IIIi1I1IIii1II )
  iIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i11IiIi1Ii1 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "                               Done Adding New Settings" )
 return
 if 41 - 41: Ii + ooOoO0O00 / I11i1ii1 * oOoO0o00OO0 / iI11I1II1I1I
 if 70 - 70: oOo0O0Ooo % OOOo00oo0oO + iiiiiiii1 % Ii + oOOoOooOo
def O00OOO00O0Ooo ( ) :
 try :
  iIIIiIII111i1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iIIIiIII111i1 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OOOi1i1Iiii = os . path . join ( iIIIiIII111i1 , "source.db" )
    os . unlink ( OOOi1i1Iiii )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( oo00 , "               Error Deleting Database No Database To Delete" )
 return
 if 92 - 92: i1iIi / ooo0O % OoOo0o - iii1i1iiiiIi
 if 44 - 44: oOo0O0Ooo + iii1i1iiiiIi * I1ii11iIi11i
 if 31 - 31: i1IiiiI1iI - oOo0O0Ooo - oOo * iii1i1iiiiIi
 if 50 - 50: oOoO0o00OO0 + i1IiiiI1iI * iiiiiiii1
 if 27 - 27: iii1i1iiiiIi * OoOo0o * iI11I1II1I1I / ooOoO0O00
def i11111IIIII ( url ) :
 i1i = urllib2 . Request ( url )
 i1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI111I1iIiI = urllib2 . urlopen ( i1i )
 IIIi1I1IIii1II = iiI111I1iIiI . read ( )
 iiI111I1iIiI . close ( )
 return IIIi1I1IIii1II
 if 60 - 60: OoOo0o * O0Oooo0O . OOOo00oo0oO
 if 47 - 47: OOOo00oo0oO % OoOo0o / OoOo0o % iii1i1iiiiIi % O0Oooo0O / iii1i1iiiiIi
 if 51 - 51: oOo0O0Ooo . i1IiiiI1iI - iii1i1iiiiIi
 if 10 - 10: I1ii11iIi11i * OoOo0o / I11i1ii1 . ooo0O
 if 97 - 97: i1iIi . i1iIi % iiiiiiii1
 if 49 - 49: I1ii11iIi11i % OoOo0o - ii + I11i1ii1
 if 54 - 54: iI11I1II1I1I - ii / i1IiiiI1iI / OOOo00oo0oO % oOo0O0Ooo + iii1i1iiiiIi
def o000O000 ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; II1i11I11iiI1 = pluginmessage_yes_no ( oo00 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if II1i11I11iiI1 :
  Oo0O0oOo = xbmcaddon . Addon ( id = iiIIIII1i1iI ) . getAddonInfo ( 'path' ) ; Oo0O0oOo = xbmc . translatePath ( Oo0O0oOo ) ;
  oOOoO0ooO0o = os . path . join ( Oo0O0oOo , ".." , ".." ) ; oOOoO0ooO0o = os . path . abspath ( oOOoO0ooO0o ) ; pluginlog ( "freshstart.main_list xbmcPath=" + oOOoO0ooO0o ) ; o0oooO0OO0OoO0 = False
  try :
   for i11ii11IiI1 , Iiiiii , oOOOOOoOOoo0 in os . walk ( oOOoO0ooO0o , topdown = True ) :
    Iiiiii [ : ] = [ oOoO for oOoO in Iiiiii if oOoO not in i1i1II ]
    for i1I1i111Ii in oOOOOOoOOoo0 :
     try : os . remove ( os . path . join ( i11ii11IiI1 , i1I1i111Ii ) )
     except :
      if i1I1i111Ii not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : o0oooO0OO0OoO0 = True
      pluginlog ( "Error removing " + i11ii11IiI1 + " " + i1I1i111Ii )
    for i1I1i111Ii in Iiiiii :
     try : os . rmdir ( os . path . join ( i11ii11IiI1 , i1I1i111Ii ) )
     except :
      if i1I1i111Ii not in [ "Database" , "userdata" ] : o0oooO0OO0OoO0 = True
      pluginlog ( "Error removing " + i11ii11IiI1 + " " + i1I1i111Ii )
   if not o0oooO0OO0OoO0 : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( oo00 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( oo00 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( oo00 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 IiIIII ( )
 if 37 - 37: ooo0O + iii1i1iiiiIi + iI11I1II1I1I + IIiIiII11i - o0o00Oo0O
 if 22 - 22: i1iIi % o0o00Oo0O - OOOo00oo0oO / oOo0O0Ooo * iii1i1iiiiIi
 if 31 - 31: I11i1ii1 + oOo0O0Ooo * i1IiiiI1iI % oOo
def Oo0o000O00oOO ( ) :
 O0Oo0o00000oO0O0 = [ ]
 I11iiIiiI1 = sys . argv [ 2 ]
 if len ( I11iiIiiI1 ) >= 2 :
  ii1oOoO0o0ooo = sys . argv [ 2 ]
  O0ooOo00 = ii1oOoO0o0ooo . replace ( '?' , '' )
  if ( ii1oOoO0o0ooo [ len ( ii1oOoO0o0ooo ) - 1 ] == '/' ) :
   ii1oOoO0o0ooo = ii1oOoO0o0ooo [ 0 : len ( ii1oOoO0o0ooo ) - 2 ]
  iIIiI1i1i = O0ooOo00 . split ( '&' )
  O0Oo0o00000oO0O0 = { }
  for O0oo in range ( len ( iIIiI1i1i ) ) :
   I11Ii1i1 = { }
   I11Ii1i1 = iIIiI1i1i [ O0oo ] . split ( '=' )
   if ( len ( I11Ii1i1 ) ) == 2 :
    O0Oo0o00000oO0O0 [ I11Ii1i1 [ 0 ] ] = I11Ii1i1 [ 1 ]
    if 69 - 69: ooOoO0O00
 return O0Oo0o00000oO0O0
 if 83 - 83: oOoO0o00OO0 . oOOoOooOo + oOo0O0Ooo + o0o00Oo0O
ooOoooO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
I1I1i1ii11 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ii1IIi1iI1ii1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
iiiii = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
O0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iI1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o0Oo0OOO0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
IIOoO0O0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
oO000Oo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
II1iI11ii1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iii111iI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
o0Ii11I = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Ii1I11II1i11 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
Iii1Iiii11i11 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oOOoOI1Ii1i111I = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iIii11 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iiIOoO0000oo0O0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
IiI1IiI1Ii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i1II111iiii = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O00oO0o000oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
Ii11i1I1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
ooooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Ii11I = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iI1IiII1II1I = base64 . decodestring ( 'Q1VOVA==' )
def Iii1i1I1iIi ( display , mode = None , name = None , url = None , menu = None , description = oOo0oooo00o , overwrite = True , fanart = Oo00OOOOO , icon = O0O , themeit = None ) :
 ooo0oo00O00oO = sys . argv [ 0 ]
 if not mode == None : ooo0oo00O00oO += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : ooo0oo00O00oO += "&name=" + urllib . quote_plus ( name )
 if not url == None : ooo0oo00O00oO += "&url=" + urllib . quote_plus ( url )
 oOO = True
 if themeit : display = themeit % display
 ooooo0OoO0 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : ooooo0OoO0 . addContextMenuItems ( menu , replaceItems = overwrite )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = False )
 return oOO
def O0oooO00ooO0 ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 ooooo0OoO0 . setProperty ( 'fanart_image' , fanart )
 ooooo0OoO0 . setProperty ( "IsPlayable" , "true" )
 o0oO00O000Oo = [ ]
 o0oO00O000Oo . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 o0oO00O000Oo . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 ooooo0OoO0 . addContextMenuItems ( o0oO00O000Oo , replaceItems = True )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = False )
 return oOO
def o00oOOooOOo0o ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1II1i = [ ]
  if showcontext == 'fav' :
   i1II1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   i1II1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooooo0OoO0 . addContextMenuItems ( i1II1i )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = True )
 return oOO
 if 14 - 14: i1IiiiI1iI * OoOo0o - o0o00Oo0O . oOoO0o00OO0 * o0o00Oo0O
def O0O0ooOOO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 ooo0oo00O00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO = True
 ooooo0OoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooo0OoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooo0OoO0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1II1i = [ ]
  if showcontext == 'fav' :
   i1II1i . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0o0O00Oo0o0 :
   i1II1i . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooooo0OoO0 . addContextMenuItems ( i1II1i )
 oOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooo0oo00O00oO , listitem = ooooo0OoO0 , isFolder = False )
 return oOO
 if 40 - 40: iii1i1iiiiIi - IIiIiII11i . oOo0O0Ooo . ooOoO0O00
 if 60 - 60: iI11I1II1I1I + oOOoOooOo * Ii + ii
ii1oOoO0o0ooo = Oo0o000O00oOO ( )
iiI = None
i1I1i111Ii = None
I11iiii1I = None
i1I = None
oo0o0000 = None
OoOOOo0 = None
oooI11iI1I = None
IIIIii11i1I = None
if 24 - 24: OoOo0o / o0o00Oo0O - oOo + I11i1ii1
if 33 - 33: oOo0O0Ooo
try :
 IIIIii11i1I = int ( ii1oOoO0o0ooo [ "fav_mode" ] )
except :
 pass
 if 92 - 92: OoOo0o / Ii + ii
try :
 iiI = urllib . unquote_plus ( ii1oOoO0o0ooo [ "url" ] )
except :
 pass
try :
 i1I1i111Ii = urllib . unquote_plus ( ii1oOoO0o0ooo [ "name" ] )
except :
 pass
try :
 i1I = urllib . unquote_plus ( ii1oOoO0o0ooo [ "iconimage" ] )
except :
 pass
try :
 I11iiii1I = int ( ii1oOoO0o0ooo [ "mode" ] )
except :
 pass
try :
 oo0o0000 = urllib . unquote_plus ( ii1oOoO0o0ooo [ "fanart" ] )
except :
 pass
try :
 OoOOOo0 = urllib . unquote_plus ( ii1oOoO0o0ooo [ "description" ] )
except :
 pass
 if 9 - 9: iiiiiiii1
 if 9 - 9: o0o00Oo0O / ooo0O / i1IiiiI1iI - Ii - iiiiiiii1 / I11i1ii1
print str ( I11II1i ) + ': ' + str ( I1IiI )
print "Mode: " + str ( I11iiii1I )
print "URL: " + str ( iiI )
print "Name: " + str ( i1I1i111Ii )
print "IconImage: " + str ( i1I )
if 46 - 46: I11i1ii1 + ii % oOo0O0Ooo
if 51 - 51: oOo0O0Ooo * O0Oooo0O . Ii % I1ii11iIi11i . ooOoO0O00 - OOOo00oo0oO
def O00oO000O0O ( content , viewType ) :
 if 56 - 56: I1ii11iIi11i / IIiIiII11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 76 - 76: iii1i1iiiiIi % oOo * o0o00Oo0O
if i1I == None : i1I = O0O
if oo0o0000 == None : oo0o0000 = Oo00OOOOO
if I11iiii1I == None :
 O00o0OO0 ( )
 if 39 - 39: oOOoOooOo / iiiiiiii1
elif I11iiii1I == 1 :
 o00oO00 ( iiI )
 if 94 - 94: OOOo00oo0oO + iiiiiiii1 * iii1i1iiiiIi - ooOoO0O00 / ii
elif I11iiii1I == 44 :
 oO0o0O0Ooo0o ( iiI )
 if 59 - 59: i1IiiiI1iI % i1iIi / iii1i1iiiiIi
elif I11iiii1I == 2 :
 I1111ii11 ( )
 if 99 - 99: i1iIi + IIiIiII11i / Ii - I11i1ii1 / iiiiiiii1 + iiiiiiii1
elif I11iiii1I == 3 :
 oOo0O ( )
 if 55 - 55: I11i1ii1 + ii * oOoO0o00OO0 . I11i1ii1 * oOoO0o00OO0 + I11i1ii1
elif I11iiii1I == 21 :
 Iii1ii1II11i ( )
 if 81 - 81: iI11I1II1I1I . oOOoOooOo + iii1i1iiiiIi
elif I11iiii1I == 4 :
 iIiii1IIi1I ( )
 if 31 - 31: i1IiiiI1iI / iii1i1iiiiIi + ooo0O
elif I11iiii1I == 5 :
 I1iiI ( iiI )
 if 80 - 80: I1ii11iIi11i
elif I11iiii1I == 6 :
 o00OOOoooo00 ( iiI )
 if 58 - 58: O0Oooo0O + OoOo0o
elif I11iiii1I == 7 :
 i1iIi1II1 ( iiI , i1I1i111Ii )
 if 76 - 76: IIiIiII11i - ooo0O % oOo + iiiiiiii1
elif I11iiii1I == 8 :
 ooo0O0oOOo ( iiI , i1I1i111Ii )
 if 38 - 38: O0Oooo0O - i1IiiiI1iI * ooOoO0O00 + iI11I1II1I1I
elif I11iiii1I == 9 :
 FIXREPOSADDONS ( iiI )
 if 41 - 41: i1iIi . oOo + oOoO0o00OO0 + iii1i1iiiiIi
elif I11iiii1I == 10 :
 oooiiI ( )
 if 76 - 76: iiiiiiii1 - iI11I1II1I1I
elif I11iiii1I == 11 :
 OO0oOOoOoo00o ( iiI )
 if 23 - 23: i1IiiiI1iI / oOo % OoOo0o
elif I11iiii1I == 12 :
 I1IO0o0000oo ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 9 - 9: oOOoOooOo % oOoO0o00OO0 . ii + oOo % OoOo0o * ii
elif I11iiii1I == 13 :
 I1I11Ii ( )
 if 21 - 21: i1iIi % o0o00Oo0O
elif I11iiii1I == 14 :
 Ii1Iii11i ( iiI )
 if 15 - 15: IIiIiII11i * i1iIi + I11i1ii1 % iiiiiiii1
elif I11iiii1I == 15 :
 ii11IiI1 ( )
 if 96 - 96: IIiIiII11i * O0Oooo0O / I1ii11iIi11i
elif I11iiii1I == 16 :
 i1Ii ( iiI , i1I1i111Ii )
 if 35 - 35: oOo0O0Ooo
elif I11iiii1I == 17 :
 iII111 ( iiI , i1I1i111Ii )
 if 54 - 54: oOoO0o00OO0 % ooo0O . ooOoO0O00
elif I11iiii1I == 18 :
 O00OOO00O0Ooo ( )
 if 72 - 72: i1iIi
elif I11iiii1I == 19 :
 I1IIiiI1II ( iiI )
 if 87 - 87: iiiiiiii1 - oOo0O0Ooo
elif I11iiii1I == 40 :
 i1OooO00oO00o ( i1I1i111Ii , iiI , OoOOOo0 )
 if 54 - 54: iI11I1II1I1I + OOOo00oo0oO * ooo0O % ii . I1ii11iIi11i
elif I11iiii1I == 42 :
 oooo ( i1I1i111Ii , iiI , OoOOOo0 )
 if 32 - 32: iiiiiiii1
elif I11iiii1I == 43 :
 Ii1i1I1iI11ii ( iiI )
 if 33 - 33: oOOoOooOo + I1ii11iIi11i * iii1i1iiiiIi % oOOoOooOo * OOOo00oo0oO - oOo
elif I11iiii1I == 20 :
 o0ooO ( iiI )
 if 40 - 40: i1IiiiI1iI . ii * o0o00Oo0O / O0Oooo0O + o0o00Oo0O
elif I11iiii1I == 22 :
 ii11IiIiiIIi ( iiI )
 if 97 - 97: oOOoOooOo - oOOoOooOo * OoOo0o % iii1i1iiiiIi - iii1i1iiiiIi - O0Oooo0O
elif I11iiii1I == 23 :
 oo0O0OOo0 ( iiI )
 if 52 - 52: o0o00Oo0O % iiiiiiii1
elif I11iiii1I == 24 :
 i11iIIi1Ii1 ( iiI )
 if 81 - 81: ii % iii1i1iiiiIi % I1ii11iIi11i - oOo0O0Ooo
elif I11iiii1I == 25 :
 Oo0oOOoIIiIi ( iiI )
 if 43 - 43: ooo0O % ooo0O
elif I11iiii1I == 26 :
 IIoo000oOOo000 ( iiI )
 if 48 - 48: o0o00Oo0O
elif I11iiii1I == 27 :
 O0iI1iI1i1I ( iiI )
 if 5 - 5: OoOo0o / Ii . i1IiiiI1iI % OoOo0o
elif I11iiii1I == 28 :
 iii1I11iI11i1 ( iiI )
 if 1 - 1: IIiIiII11i + o0o00Oo0O * iii1i1iiiiIi / I11i1ii1 . o0o00Oo0O
elif I11iiii1I == 29 :
 o0o0OO ( iiI )
 if 87 - 87: I11i1ii1 + oOo0O0Ooo
elif I11iiii1I == 30 :
 i1iII11IiI ( iiI )
 if 74 - 74: oOo + oOo % iiiiiiii1 / i1IiiiI1iI / o0o00Oo0O
elif I11iiii1I == 31 :
 O0iI1Iii ( iiI )
 if 54 - 54: ooo0O / ii * oOOoOooOo . iii1i1iiiiIi - O0Oooo0O
elif I11iiii1I == 32 :
 oo0OOoOo0 ( )
 if 69 - 69: OOOo00oo0oO - oOo
elif I11iiii1I == 33 :
 oO00oO0 ( )
 if 80 - 80: oOOoOooOo + iI11I1II1I1I . IIiIiII11i + oOo0O0Ooo - OOOo00oo0oO % iii1i1iiiiIi
elif I11iiii1I == 35 :
 II1I1Ii11 ( iiI )
 if 10 - 10: iI11I1II1I1I
elif I11iiii1I == 34 :
 o0oI1Iii ( iiI )
 if 44 - 44: iii1i1iiiiIi * OOOo00oo0oO . oOoO0o00OO0 + Ii
elif I11iiii1I == 36 :
 IIIi11Ii ( iiI )
 if 85 - 85: i1IiiiI1iI
elif I11iiii1I == 37 :
 Iiii ( iiI )
 if 36 - 36: oOOoOooOo % oOo
elif I11iiii1I == 38 :
 IiIOOOoo ( iiI )
 if 1 - 1: ii - iii1i1iiiiIi
elif I11iiii1I == 41 :
 o000O000 ( ii1oOoO0o0ooo )
 if 35 - 35: O0Oooo0O
elif I11iiii1I == 39 :
 IIOOO0O00O0OOOO ( iiI )
 if 35 - 35: I1ii11iIi11i - iI11I1II1I1I / ooOoO0O00 + oOo - ii / Ii
elif I11iiii1I == 45 :
 TEXTS ( )
 if 79 - 79: oOo0O0Ooo * oOOoOooOo * oOOoOooOo
elif I11iiii1I == 46 :
 I1iiii1I ( )
 if 92 - 92: iiiiiiii1 % oOoO0o00OO0
elif I11iiii1I == 47 :
 GEVID ( )
 if 16 - 16: OOOo00oo0oO
elif I11iiii1I == 48 :
 oo000o ( i1I1i111Ii , iiI , OoOOOo0 )
 if 52 - 52: ii % oOOoOooOo - O0Oooo0O * i1IiiiI1iI
elif I11iiii1I == 49 :
 O0oOOo0Oo ( )
 if 24 - 24: i1iIi + I11i1ii1 + ii / OOOo00oo0oO / oOo0O0Ooo + I11i1ii1
elif I11iiii1I == 22222 :
 o00oOOo ( iiI )
 if 52 - 52: oOOoOooOo
elif I11iiii1I == 222225 :
 o0oO0Oo ( iiI )
 if 38 - 38: oOo + oOo0O0Ooo % I11i1ii1
elif I11iiii1I == 222 :
 O0oOoOO0oo ( iiI )
 if 87 - 87: OOOo00oo0oO * i1iIi - O0Oooo0O / OOOo00oo0oO
elif I11iiii1I == 2222222 :
 IIIIiii1IIii ( iiI )
 if 65 - 65: iii1i1iiiiIi
elif I11iiii1I == 222222 :
 I1iiI1iIi1 ( iiI , i1I1i111Ii )
 if 87 - 87: i1IiiiI1iI - Ii - OoOo0o . iii1i1iiiiIi + I11i1ii1 . oOo
elif I11iiii1I == 333 :
 i1iIi11 ( iiI )
 if 70 - 70: iI11I1II1I1I % ii / oOo . o0o00Oo0O - i1IiiiI1iI % IIiIiII11i
 if 84 - 84: OoOo0o * ooOoO0O00 . iI11I1II1I1I * iiiiiiii1 + O0Oooo0O + IIiIiII11i
elif I11iiii1I == 1020 :
 OOoOoo0Oo0Oo ( )
 if 97 - 97: i1iIi - I11i1ii1
elif I11iiii1I == 1021 :
 ANIMEEP ( )
 if 64 - 64: OOOo00oo0oO . oOOoOooOo / oOOoOooOo - IIiIiII11i
elif I11iiii1I == 1022 :
 ANIMEPLAY ( iiI )
 if 81 - 81: oOoO0o00OO0
elif I11iiii1I == 1001 :
 iiIiI1iiI1 ( )
 if 64 - 64: OOOo00oo0oO * oOo / OoOo0o + i1iIi % I1ii11iIi11i . I11i1ii1
elif I11iiii1I == 1005 :
 O0ii1IIIiiI1i ( )
 if 2 - 2: O0Oooo0O + i1IiiiI1iI
elif I11iiii1I == 1007 :
 Iiii1IIII11I1i ( iiI )
 if 47 - 47: Ii + iI11I1II1I1I % oOoO0o00OO0 - OOOo00oo0oO % oOo
elif I11iiii1I == 1010 :
 Oo0O00O ( iiI )
 if 85 - 85: OOOo00oo0oO * iii1i1iiiiIi / iii1i1iiiiIi
elif I11iiii1I == 1011 :
 IiIIiii1II1ii1i1IiIIi ( iiI )
 if 85 - 85: OoOo0o / O0Oooo0O . ooOoO0O00 / iii1i1iiiiIi + iI11I1II1I1I
elif I11iiii1I == 1012 :
 iii11I1I1i1 ( iiI )
 if 71 - 71: oOo
elif I11iiii1I == 1030 :
 oo000Ooo ( )
 if 96 - 96: oOoO0o00OO0 / oOo0O0Ooo - oOoO0o00OO0 / IIiIiII11i - I11i1ii1
elif I11iiii1I == 1031 :
 OOoOoo00oO ( iiI , i1I )
 if 74 - 74: i1iIi * ii % OoOo0o + ii + iiiiiiii1
elif I11iiii1I == 1032 :
 i1iI1i11iIi1 ( iiI )
 if 83 - 83: ooOoO0O00
elif I11iiii1I == 1006 :
 Parse . ParseURL ( iiI )
 if 2 - 2: ooOoO0O00 / OoOo0o * o0o00Oo0O
elif I11iiii1I == 2030 :
 Parse . addonParseURL ( iiI )
 if 99 - 99: ii . iii1i1iiiiIi / IIiIiII11i
elif I11iiii1I == 2031 :
 Parse . apkParseURL ( iiI )
 if 64 - 64: iiiiiiii1 / ooOoO0O00 . oOo0O0Ooo + o0o00Oo0O
elif I11iiii1I == 2032 :
 Parse . ParseBOSS ( iiI )
 if 5 - 5: o0o00Oo0O . Ii
elif I11iiii1I == 1002 :
 III1I11i ( iiI )
 if 71 - 71: ooo0O + iiiiiiii1 + oOOoOooOo
elif I11iiii1I == 1003 :
 O0o00OO0OoO ( iiI , i1I )
 if 27 - 27: ii . iiiiiiii1 * O0Oooo0O % o0o00Oo0O + ii - iiiiiiii1
elif I11iiii1I == 1004 :
 Oo0ooo ( iiI )
 if 86 - 86: ooOoO0O00
elif I11iiii1I == 1008 :
 I1I1iOO ( )
 if 81 - 81: iii1i1iiiiIi
elif I11iiii1I == 1009 :
 iiI1iiIi ( iiI )
 if 52 - 52: iiiiiiii1 * I11i1ii1 % oOo0O0Ooo * i1IiiiI1iI
elif I11iiii1I == 2001 :
 o00i1iII11iIiiI1 ( )
 if 73 - 73: O0Oooo0O * oOOoOooOo
elif I11iiii1I == 2002 :
 oooOoo0oo00OooOO ( iiI )
 if 62 - 62: OoOo0o . oOo0O0Ooo * iI11I1II1I1I + oOo * oOOoOooOo / OOOo00oo0oO
elif I11iiii1I == 1013 :
 IiiIiiiiI1III ( )
elif I11iiii1I == 10111113 :
 I1iIi1IiI1i ( iiI )
 if 14 - 14: iiiiiiii1 / oOo
elif I11iiii1I == 1014 :
 OO0OoiIII11 ( )
 if 75 - 75: I11i1ii1
elif I11iiii1I == 1015 :
 i1IiI11 ( iiI )
 if 68 - 68: I11i1ii1 - ooOoO0O00 % I11i1ii1 . oOo . Ii . ii
elif I11iiii1I == 1016 :
 oooOOO00o0 ( iiI , i1I , i1I1i111Ii )
 if 32 - 32: iiiiiiii1 + oOo % I11i1ii1 + oOo0O0Ooo
elif I11iiii1I == 1017 :
 oo00O0 ( )
 if 69 - 69: O0Oooo0O + i1IiiiI1iI - iI11I1II1I1I - IIiIiII11i . i1iIi
elif I11iiii1I == 1018 :
 iiiI111I ( iiI )
 if 74 - 74: oOoO0o00OO0 % ooo0O + o0o00Oo0O - Ii - I11i1ii1 % OoOo0o
elif I11iiii1I == 1019 :
 iiIiIiII ( iiI )
elif I11iiii1I == 10190 :
 iIi ( iiI )
 if 39 - 39: oOo - ooo0O
elif I11iiii1I == 1023 :
 iiIII ( )
 if 71 - 71: iiiiiiii1 . oOo + oOOoOooOo - OoOo0o - I1ii11iIi11i
elif I11iiii1I == 1024 :
 oo0IIII1 ( iiI )
 if 100 - 100: ii - ooo0O + O0Oooo0O . ii % Ii
elif I11iiii1I == 1025 :
 II1ii111 ( iiI )
 if 64 - 64: O0Oooo0O % ii / ooOoO0O00 / oOo
elif I11iiii1I == 4001 :
 Ooo0O ( )
 if 2 - 2: i1IiiiI1iI % ooo0O . oOo . oOo
elif I11iiii1I == 4002 :
 ooOoo0o0O ( )
 if 89 - 89: oOOoOooOo - OOOo00oo0oO + IIiIiII11i + oOo - I11i1ii1
elif I11iiii1I == 4003 :
 OO00o0 ( )
 if 27 - 27: O0Oooo0O - ooo0O + oOo
elif I11iiii1I == 4004 :
 Oo00OOOOoo0oo ( )
 if 38 - 38: iii1i1iiiiIi + oOo . Ii + i1iIi % ooOoO0O00 % oOo0O0Ooo
elif I11iiii1I == 4005 :
 ii1I11iIiIII1 ( )
 if 93 - 93: Ii
elif I11iiii1I == 4006 :
 IiiI11i1I ( )
 if 63 - 63: iI11I1II1I1I - iI11I1II1I1I % ooo0O
elif I11iiii1I == 4007 :
 O00OO ( )
 if 97 - 97: ooOoO0O00 % i1IiiiI1iI % iii1i1iiiiIi
elif I11iiii1I == 4008 :
 o0OoO000O ( )
 if 25 - 25: iii1i1iiiiIi . iI11I1II1I1I - iiiiiiii1 % IIiIiII11i . iii1i1iiiiIi
elif I11iiii1I == 40099 : II1iiiiI1 ( )
elif I11iiii1I == 4009 : IIiIi1i1I11 ( )
elif I11iiii1I == 4010 : I11II11IiI11 ( )
elif I11iiii1I == 3000 :
 oooOO ( )
 if 16 - 16: OoOo0o . I1ii11iIi11i . oOo0O0Ooo % o0o00Oo0O . oOoO0o00OO0 + Ii
elif I11iiii1I == 3001 :
 ooOO0O00O ( )
 if 100 - 100: oOoO0o00OO0 - ooOoO0O00 - oOo * ooo0O + iii1i1iiiiIi
elif I11iiii1I == 3002 :
 i1iOOoOo0o ( iiI )
 if 31 - 31: ooOoO0O00
elif I11iiii1I == 3003 :
 oOOOiII1iII ( iiI )
 if 21 - 21: ooo0O / o0o00Oo0O % o0o00Oo0O . ii / oOo0O0Ooo
elif I11iiii1I == 3004 :
 oOO00o0O0O ( iiI )
 if 94 - 94: oOOoOooOo + oOo / oOOoOooOo - oOOoOooOo + I1ii11iIi11i + ooo0O
elif I11iiii1I == 404 :
 III11II111111 ( i1I1i111Ii , iiI , i1I )
 if 50 - 50: OOOo00oo0oO . I1ii11iIi11i
elif I11iiii1I == 405 :
 o000OOooO0O ( iiI )
 if 15 - 15: i1iIi
elif I11iiii1I == 7030 :
 II1II111iIi ( )
 if 64 - 64: ii
elif I11iiii1I == 7021 :
 oOII1i1IiiI ( i1I1i111Ii )
 if 25 - 25: I11i1ii1
elif I11iiii1I == 7022 :
 iIIiii ( i1I1i111Ii )
 if 29 - 29: iii1i1iiiiIi % oOOoOooOo * ii
elif I11iiii1I == 7000 :
 i1IOO00OOOO00oOO ( i1I1i111Ii , iiI , img )
 if 8 - 8: Ii - O0Oooo0O / I11i1ii1
elif I11iiii1I == 7050 :
 II111111 ( iiI )
 if 17 - 17: Ii * oOo . ooo0O . ii . iii1i1iiiiIi - oOoO0o00OO0
elif I11iiii1I == 7051 :
 oooO000oO0O ( iiI )
 if 78 - 78: oOoO0o00OO0 - ii + o0o00Oo0O
elif I11iiii1I == 70511 :
 WATCHLIST2 ( iiI )
 if 15 - 15: oOoO0o00OO0 / I11i1ii1 % oOo0O0Ooo
elif I11iiii1I == 7052 :
 o0Oo ( iiI )
 if 16 - 16: i1iIi
elif I11iiii1I == 7053 :
 iiooOOOo ( iiI )
 if 26 - 26: ooo0O / i1IiiiI1iI + iii1i1iiiiIi / iii1i1iiiiIi
elif I11iiii1I == 7054 :
 CoolPlay ( iiI )
 if 31 - 31: O0Oooo0O
elif I11iiii1I == 7060 :
 i1Iii1II11iI1 ( )
 if 84 - 84: Ii * OoOo0o . iiiiiiii1 - i1iIi * ooOoO0O00 - oOoO0o00OO0
elif I11iiii1I == 7061 :
 IIII1iiiIIiIIiI ( iiI )
 if 1 - 1: IIiIiII11i
elif I11iiii1I == 7063 :
 IIi11iIIiIII111 ( iiI )
 if 94 - 94: oOoO0o00OO0 * iiiiiiii1 % iiiiiiii1 % i1IiiiI1iI - iiiiiiii1
elif I11iiii1I == 7062 :
 oo0iIiIII1Ii ( iiI )
 if 38 - 38: I11i1ii1 - oOo % i1iIi - IIiIiII11i
elif I11iiii1I == 7064 :
 NATatozcat ( )
 if 97 - 97: o0o00Oo0O . i1iIi
elif I11iiii1I == 7067 :
 O0oOo ( iiI )
 if 52 - 52: I11i1ii1
elif I11iiii1I == 7066 :
 NATatozA ( iiI )
 if 86 - 86: O0Oooo0O / o0o00Oo0O + ii % OOOo00oo0oO
elif I11iiii1I == 7065 :
 iIII1Ii1 ( iiI )
 if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . i1IiiiI1iI . i1iIi
elif I11iiii1I == 7070 :
 i1iI ( )
 if 81 - 81: IIiIiII11i + iii1i1iiiiIi % Ii / iiiiiiii1 . O0Oooo0O + IIiIiII11i
elif I11iiii1I == 7071 :
 DIZIlist ( iiI )
 if 48 - 48: oOo0O0Ooo . oOoO0o00OO0 * iii1i1iiiiIi % ooOoO0O00 / O0Oooo0O * IIiIiII11i
elif I11iiii1I == 7072 :
 DIZIpull ( iiI )
 if 62 - 62: ooo0O * O0Oooo0O . iI11I1II1I1I / ooOoO0O00
elif I11iiii1I == 7073 :
 WATCHDIZI ( iiI )
 if 75 - 75: ii / oOOoOooOo - iiiiiiii1 . ii . iii1i1iiiiIi % ooOoO0O00
elif I11iiii1I == 7002 :
 oo0OoooOo0 ( )
 if 7 - 7: iii1i1iiiiIi . ooOoO0O00 * Ii % Ii
elif I11iiii1I == 7003 :
 O0Oo ( iiI )
 if 54 - 54: oOo / oOo0O0Ooo . I1ii11iIi11i
elif I11iiii1I == 7004 :
 o0o0oO0OOo00Ooo00 ( iiI )
 if 39 - 39: oOo . oOOoOooOo
elif I11iiii1I == 7020 :
 i1IIi ( iiI )
 if 41 - 41: I1ii11iIi11i * oOoO0o00OO0 - IIiIiII11i - IIiIiII11i
elif I11iiii1I == 7001 :
 OO0o0o0oo0O ( )
 if 7 - 7: OOOo00oo0oO
elif I11iiii1I == 7010 :
 iIii ( iiI )
 if 41 - 41: oOOoOooOo
elif I11iiii1I == 7011 :
 O000ooo ( iiI )
 if 93 - 93: i1iIi + O0Oooo0O + i1iIi
elif I11iiii1I == 7012 :
 II1Oooo00oO0OO0o ( iiI )
 if 23 - 23: oOo0O0Ooo - ooOoO0O00 / oOOoOooOo
elif I11iiii1I == 7013 :
 cnfTVPlay2 ( iiI )
elif I11iiii1I == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iiI )
elif I11iiii1I == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iiI )
elif I11iiii1I == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( i1I1i111Ii , iiI , i1I )
elif I11iiii1I == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif I11iiii1I == 7018 :
 i11ii1i1i ( )
elif I11iiii1I == 7019 :
 CNF_Studio_Indexer . List_Movies ( iiI )
elif I11iiii1I == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iiI )
elif I11iiii1I == 7024 :
 CNF_Studio_Indexer . Box_Office ( iiI )
 if 4 - 4: I11i1ii1 . oOoO0o00OO0 + iiiiiiii1 % oOOoOooOo
elif I11iiii1I == 8000 :
 I1iI ( )
elif I11iiii1I == 8001 :
 OoOoO0O ( )
elif I11iiii1I == 8002 :
 OOOOO0oOooo0O ( )
elif I11iiii1I == 8003 :
 Ooo00O0ooOo ( )
elif I11iiii1I == 8004 :
 O0OOOo000 ( )
elif I11iiii1I == 8005 :
 IIoo0O ( )
elif I11iiii1I == 8006 :
 i1iiIiIi1iIII ( i1I1i111Ii , iiI )
elif I11iiii1I == 8030 :
 I1111IiII1 ( iiI )
elif I11iiii1I == 8045 :
 oo0Oooo0O ( iiI )
elif I11iiii1I == 8046 :
 ooO0Oo ( iiI )
elif I11iiii1I == 8047 :
 OooOooo00OOO0o ( iiI )
elif I11iiii1I == 8048 :
 iI1iiI1Ii ( iiI )
elif I11iiii1I == 8049 :
 i1iiII1iIIIIII ( iiI )
elif I11iiii1I == 804900 :
 IIIIII11iIiI1III ( iiI )
elif I11iiii1I == 8020 :
 oOOO0 ( )
elif I11iiii1I == 8021 :
 II1I111iiI1I ( iiI )
elif I11iiii1I == 8022 :
 iIiiIIiIi ( iiI )
elif I11iiii1I == 8023 :
 Oo000o0o ( iiI )
elif I11iiii1I == 8040 :
 OOoiIIiiIIIi1I ( )
elif I11iiii1I == 8041 :
 ooO0i11i1i1i ( iiI )
elif I11iiii1I == 8042 :
 Iiii1i11III1I1 ( iiI )
elif I11iiii1I == 8043 :
 yt . PlayVideo ( iiI )
elif I11iiii1I == 8044 :
 O000o ( iiI )
elif I11iiii1I == 8060 :
 I1iii ( )
elif I11iiii1I == 8061 :
 iiiiIiI1IIiI ( iiI )
elif I11iiii1I == 8064 :
 oo0OO ( )
elif I11iiii1I == 8065 :
 IIII ( iiI )
elif I11iiii1I == 8070 :
 IiI11IiIIi ( )
elif I11iiii1I == 8071 :
 oOOo0OoooOo ( iiI )
elif I11iiii1I == 7080 :
 I1I1IiIiIIi1I ( iiI )
elif I11iiii1I == 8090 :
 iIiIIi11i1 ( )
elif I11iiii1I == 8091 :
 Oooo00o ( iiI )
elif I11iiii1I == 8092 :
 o00OOOo0O0O0o0 ( iiI )
elif I11iiii1I == 8093 :
 iIiii1Ii1I ( iiI )
elif I11iiii1I == 8081 :
 o0oO0oOO ( )
elif I11iiii1I == 8062 :
 Iii11i ( iiI )
elif I11iiii1I == 8063 :
 iiiIiiIII ( iiI )
elif I11iiii1I == 8050 :
 oOOOoo0 ( )
elif I11iiii1I == 8051 :
 iI1i11II1i1i ( iiI )
elif I11iiii1I == 8052 :
 O0O0O00OoO0O ( iiI )
elif I11iiii1I == 8085 :
 o0OoOO0 ( )
elif I11iiii1I == 8086 :
 o00o000 ( iiI )
elif I11iiii1I == 8087 :
 OOO0 ( iiI )
elif I11iiii1I == 8088 :
 oOO0ooOO ( iiI , i1I1i111Ii )
elif I11iiii1I == 9000 :
 o0O0o ( )
elif I11iiii1I == 1111 :
 OOoOOO0 ( )
elif I11iiii1I == 9001 :
 O00OOooo0Ooo ( )
elif I11iiii1I == 9002 :
 oOO0OOOOoooO ( )
elif I11iiii1I == 9003 :
 I1ioOo ( )
elif I11iiii1I == 9004 :
 World1 ( )
elif I11iiii1I == 9005 :
 World2 ( iiI )
elif I11iiii1I == 9006 :
 World3 ( iiI )
elif I11iiii1I == 9007 :
 o0OOO0Oo ( )
elif I11iiii1I == 9008 :
 O0O00oo ( iiI )
elif I11iiii1I == 9009 :
 iiIIIii ( iiI )
elif I11iiii1I == 9010 :
 i1111iII1 ( )
elif I11iiii1I == 9011 :
 I1I1iiI11I1 ( iiI )
elif I11iiii1I == 50 :
 I1I1IiI ( iiI )
elif I11iiii1I == 9020 :
 champlist ( )
elif I11iiii1I == 9021 :
 Oo000O ( )
elif I11iiii1I == 9022 :
 I1iOO000Ooo ( )
elif I11iiii1I == 9023 :
 OoOooo0ooo0O ( )
elif I11iiii1I == 9024 :
 III1iI1ii1 ( iiI )
elif I11iiii1I == 9030 :
 I1iiII11i11iI ( iiI )
elif I11iiii1I == 9031 :
 I11I1iI ( iiI )
elif I11iiii1I == 9032 :
 OOoo00o0 ( iiI )
elif I11iiii1I == 9033 :
 o0OO0iI1II1i1ii ( iiI )
elif I11iiii1I == 9034 :
 oOO0OO0O ( )
elif I11iiii1I == 7084 :
 I11ooOo ( )
elif I11iiii1I == 7085 :
 IiiiIII1 ( iiI )
elif I11iiii1I == 7086 :
 II1I ( iiI , i1I , OoOOOo0 )
elif I11iiii1I == 7087 :
 O0OoO0OOOo ( OoOOOo0 )
elif I11iiii1I == 9666 :
 IiI11ii1I ( iiI )
elif I11iiii1I == 10100 : OO0IIIIIIi111i ( )
elif I11iiii1I == 101001 : OOO0O ( iiI )
elif I11iiii1I == 10105 : o0o0OOO0ooo00 ( iiI )
elif I11iiii1I == 10106 : I11III111i1I ( iiI )
elif I11iiii1I == 10104 : I1Ioo000oooooooO ( iiI )
elif I11iiii1I == 10107 : iIi11 ( )
elif I11iiii1I == 10103 : O0ooOO0O00 ( iiI )
elif I11iiii1I == 10108 : o0o0o ( iiI )
elif I11iiii1I == 10000 : Origin_Menu ( )
elif I11iiii1I == 10001 : OoOi111i ( )
elif I11iiii1I == 10002 : iI111i1I1II ( )
elif I11iiii1I == 10003 : I1II ( )
elif I11iiii1I == 10004 : oO0oo0O0OOOo0 ( iiI )
elif I11iiii1I == 10005 : I111ii1III1I ( )
elif I11iiii1I == 10006 : I1IIi11I1IiIi ( iiI )
elif I11iiii1I == 10007 : I1IiI11 ( iiI , i1I )
elif I11iiii1I == 10008 : o0OiI1 ( )
elif I11iiii1I == 10009 : iII1ii11I1I ( )
elif I11iiii1I == 10010 : IIiIoOOO ( iiI )
elif I11iiii1I == 10011 : oO0o0oo ( iiI )
elif I11iiii1I == 10012 : IIIIiii1IIii ( iiI )
elif I11iiii1I == 10113 : GRABG ( iiI , i1I1i111Ii )
elif I11iiii1I == 10109 : O00oo0ooo0O ( iiI )
elif I11iiii1I == 10013 : o00OOOOoOO ( iiI )
elif I11iiii1I == 10014 : ooOoo00OoO00 ( )
elif I11iiii1I == 10015 : iIOO000O ( )
elif I11iiii1I == 10016 : OO0 ( iiI )
elif I11iiii1I == 10017 : IIiI1IiI1iIi1 ( )
elif I11iiii1I == 10018 : O0Ooo000OO00 ( )
elif I11iiii1I == 10019 : oOi1IiIiIii11I ( )
elif I11iiii1I == 10020 : I11iIIiiIiIi ( )
elif I11iiii1I == 10021 : iii ( )
elif I11iiii1I == 10022 : IiiO0O0O0OOO0o ( iiI )
elif I11iiii1I == 10023 : I11iiI1i ( i1I1i111Ii , iiI )
elif I11iiii1I == 10024 : IIIiII1iIII ( iiI )
elif I11iiii1I == 10025 : IIiiI1iIiIi ( )
elif I11iiii1I == 10026 : o000 ( )
elif I11iiii1I == 10027 : O000 ( )
elif I11iiii1I == 10028 : Oo0oo ( )
elif I11iiii1I == 10029 : OOOooOOO00O ( )
elif I11iiii1I == 423 : Iiiii1I ( iiI )
elif I11iiii1I == 426 : O0Ooo00o0OoOo ( iiI )
elif I11iiii1I == 10030 : Izle_Films ( )
elif I11iiii1I == 10031 : Latest_Izle_Movies ( )
elif I11iiii1I == 10032 : Izle_Genres ( )
elif I11iiii1I == 10033 : Izle_Pop_Movies ( )
elif I11iiii1I == 10034 : Izle_Boxsets ( )
elif I11iiii1I == 10035 : Izle_Search ( )
elif I11iiii1I == 10036 : Izle_Genres_Movie ( iiI )
elif I11iiii1I == 10037 : Izle_Boxset_single ( iiI )
elif I11iiii1I == 10038 : Izle_IFRAME ( )
elif I11iiii1I == 10039 : Izle_Boxsets_Next ( iiI )
elif I11iiii1I == 10040 : Ooo00O ( )
elif I11iiii1I == 10041 : IiI1Iii1iIIII ( iiI )
elif I11iiii1I == 10042 : O00oi111II ( iiI )
elif I11iiii1I == 10043 : I1i1ii1IiI1i ( )
elif I11iiii1I == 10044 : OOoO00o00oo ( iiI )
elif I11iiii1I == 10045 : I1II1i1iIIi ( i1I1i111Ii )
elif I11iiii1I == 10046 : O0o0ooo00o00 ( iiI )
elif I11iiii1I == 10047 : OOOOoO0O ( iiI )
elif I11iiii1I == 10048 : o0O0oO ( iiI )
elif I11iiii1I == 10049 : o0OooOOo0OO00 ( iiI )
elif I11iiii1I == 10050 : iI1i1IIiiiI11 ( )
elif I11iiii1I == 10051 : I1IiO00Oo0OoO00OO ( )
elif I11iiii1I == 10052 : OoOOoo ( )
elif I11iiii1I == 10053 : Addon ( iiI )
elif I11iiii1I == 10054 : iI11Ii ( iiI , i1I1i111Ii )
elif I11iiii1I == 10055 :
 IIIIiI1iiI ( "addFavorite" )
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 O00oO0oOOOOOO ( i1I1i111Ii , iiI , i1I , oo0o0000 , IIIIii11i1I )
elif I11iiii1I == 10056 :
 IIIIiI1iiI ( "rmFavorite" )
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiooo0o0oO ( i1I1i111Ii )
elif I11iiii1I == 10057 :
 IIIIiI1iiI ( "getFavorites" )
 I1i11IIiiIiI ( )
elif I11iiii1I == 10058 : o0oO ( )
elif I11iiii1I == 10059 : Donators_Guide ( )
elif I11iiii1I == 10060 : o0oo0000OO ( )
elif I11iiii1I == 10061 : IIi1i ( )
elif I11iiii1I == 10062 : iiIII1i1 ( i1I1i111Ii , iiI , OoOOOo0 )
elif I11iiii1I == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + I11iii1Ii + ")" )
elif I11iiii1I == 10064 : ooo00o0OO ( )
elif I11iiii1I == 10065 : oooO0oooOo000 ( iiI )
elif I11iiii1I == 10066 : iiII ( iiI )
elif I11iiii1I == 10068 : II11 ( iiI )
elif I11iiii1I == 10069 : i1iiiIIi11II ( iiI )
elif I11iiii1I == 10070 : o0o0oO00OoO0o ( iiI )
elif I11iiii1I == 10071 : Genie_Watch ( )
elif I11iiii1I == 10072 : IiiI1i111I1i ( )
elif I11iiii1I == 10073 : i1Iii ( iiI )
elif I11iiii1I == 10074 : Oooo0ooOoo0 ( iiI )
elif I11iiii1I == 10075 : Ii1Ii1 ( i1I , i1I1i111Ii , iiI )
elif I11iiii1I == 10076 : IIiI1111iI ( iiI )
elif I11iiii1I == 10077 : iI1Ii11 ( iiI )
elif I11iiii1I == 10078 : o0OoOooOO0o0 ( )
elif I11iiii1I == 10079 : Genie_Watch_Tv_Shows ( )
elif I11iiii1I == 10080 : Genie_Watch_Tv_Genre ( iiI )
elif I11iiii1I == 10081 : Genie_Watch_TV_PlayRun ( iiI )
elif I11iiii1I == 10082 : Genie_Watch_TV_Episodes ( iiI , i1I )
elif I11iiii1I == 10083 : Genie_Watch_Tv_Recent ( iiI )
elif I11iiii1I == 10084 : i1iiiIii11 ( )
elif I11iiii1I == 10085 : Iii1I1I11iiI1 ( )
elif I11iiii1I == 10086 : o0OOOO00O0Oo ( )
elif I11iiii1I == 20000 : o0O000O00o ( )
elif I11iiii1I == 20001 : iiII11 ( iiI )
elif I11iiii1I == 20002 : OOo0i111ii1Ii ( iiI )
elif I11iiii1I == 20003 : o00oIiIiIiiI ( iiI )
elif I11iiii1I == 20004 : o0ooOOOo0O0 ( iiI )
elif I11iiii1I == 20005 : o00Oo ( iiI )
elif I11iiii1I == 21004 : Ooii1II11IIII ( )
elif I11iiii1I == 21005 : oO0OOOO0o0o0 ( iiI )
elif I11iiii1I == 21006 : ii11Ii1iii1I1 ( iiI )
elif I11iiii1I == 21007 : I1Ii11I1i1iii ( iiI )
elif I11iiii1I == 21008 : oOO0OOOo ( iiI )
elif I11iiii1I == 21009 : IiIIII1i11I ( iiI )
elif I11iiii1I == 30000 : iI1I11 ( )
elif I11iiii1I == 30001 : oo000O ( )
elif I11iiii1I == 100121 : Resolve ( iiI )
elif I11iiii1I == 30003 : Ooo0OO00oo ( )
elif I11iiii1I == 30004 : OOooooo0O0 ( iiI )
elif I11iiii1I == 30005 : oOo0OO0 ( iiI )
elif I11iiii1I == 30006 : iiiii1i1 ( )
elif I11iiii1I == 30007 : II11II1i ( )
elif I11iiii1I == 30008 : iiII1iiI ( iiI )
elif I11iiii1I == 30009 : I1i1iI1I1II ( iiI )
elif I11iiii1I == 30010 : Ii1i1 ( iiI )
elif I11iiii1I == 30011 : IiIi1 ( )
elif I11iiii1I == 30012 : o00OoOo0 ( )
elif I11iiii1I == 30013 : o0O0ooo0o ( )
elif I11iiii1I == 30014 : Iii1iIII1Iii ( )
elif I11iiii1I == 30015 : IIi1I1 ( iiI , i1I , oo0o0000 )
elif I11iiii1I == 30016 : oO0O0ooOoo ( iiI )
elif I11iiii1I == 30019 : O0O0o0o0oo0O ( iiI )
elif I11iiii1I == 30017 : O0oO00o0o0oo0 ( iiI )
elif I11iiii1I == 30018 : O0o ( iiI )
elif I11iiii1I == 30030 : iii1 ( )
elif I11iiii1I == 30031 : Oo0OO0 ( )
elif I11iiii1I == 30032 : II1Ii1iI1i1 ( )
elif I11iiii1I == 30033 : iiIIIIiI111 ( )
elif I11iiii1I == 30034 : OO00Oo00o ( )
elif I11iiii1I == 30035 : o0000Oo0 ( iiI )
elif I11iiii1I == 30036 : I1iII1iI ( iiI )
elif I11iiii1I == 30037 : Iii1Iiii1iI1 ( iiI )
elif I11iiii1I == 30038 : I1iI1I1111i ( )
elif I11iiii1I == 30039 : II11IiIi11 ( )
elif I11iiii1I == 50000 : oOIIiIi ( )
elif I11iiii1I == 50001 : I1I ( )
elif I11iiii1I == 50002 : iiiIiii11i1i ( iiI )
elif I11iiii1I == 50003 : Table_Menu ( OoOOOo0 )
elif I11iiii1I == 60000 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
elif I11iiii1I == 60001 : i1IIiI1iII ( )
elif I11iiii1I == 60002 : IIiIOOoOo0oO0oo00 ( i1I1i111Ii )
elif I11iiii1I == 60003 : IIIIi1Iii1iIi ( iiI )
elif I11iiii1I == 600033 : o0OOOoO0O ( iiI )
elif I11iiii1I == 60004 : I11iIi1i1I1i1 ( iiI )
elif I11iiii1I == 50004 : Ii1IIiiIIi ( )
elif I11iiii1I == 50005 : speedtest . runtest ( iiI )
elif I11iiii1I == 70001 : IiIiIi1I1OooO00O0OO0oo ( )
elif I11iiii1I == 70002 : Oo0Oo0o00oO ( iiI )
elif I11iiii1I == 70003 : oO0o0OooOO0 ( iiI )
elif I11iiii1I == 70004 : iiIiooOo0oo0O0O ( iiI )
elif I11iiii1I == 70005 : IIiii ( iiI )
elif I11iiii1I == 70006 : i1Ii11I1i ( )
elif I11iiii1I == 50006 : O0O0OOOOoo ( oo00 , Oo0oO0ooo )
elif I11iiii1I == 80000 : IiIIII ( )
elif I11iiii1I == 80001 : resolvefilmon ( iiI )
elif I11iiii1I == 80002 : oOoOOo ( )
elif I11iiii1I == 80003 : IIiIIII ( i1I1i111Ii , iiI , "None" )
elif I11iiii1I == 80004 : ooooo0oo0OO ( i1I1i111Ii , iiI )
elif I11iiii1I == 80005 : iiI1i11II ( )
elif I11iiii1I == 80006 : o0OOoo0oOoO00 ( iiI )
elif I11iiii1I == 80007 : i1ii1iIi ( iiI )
elif I11iiii1I == 80008 : I1I1Ii ( )
elif I11iiii1I == 80009 : O000o0O0 ( )
elif I11iiii1I == 80010 : O0000oOoO0o0 ( iiI )
elif I11iiii1I == 80011 : o00oI1i1IIIIIII ( iiI )
elif I11iiii1I == 80012 : I1IIiIi ( )
elif I11iiii1I == 90000 : IIiiiiiiII ( i1I1i111Ii , iiI )
elif I11iiii1I == 90001 : tools ( )
elif I11iiii1I == 90002 : IIiiii ( )
elif I11iiii1I == 90003 : oO0ooo0o0 ( iiI )
elif I11iiii1I == 90004 : O0oOO0o0 ( iiI )
elif I11iiii1I == 90005 : O000000oooOOo ( iiI )
elif I11iiii1I == 90006 : IiiIiI1IIII11II ( iiI )
elif I11iiii1I == 90007 : i111I ( iiI )
elif I11iiii1I == 90008 : i1i1IIoO0O ( iiI )
elif I11iiii1I == 90009 : IiIoOo ( iiI )
elif I11iiii1I == 90010 : i11i11111i1i ( )
elif I11iiii1I == 90020 : OOoO00OOo ( )
elif I11iiii1I == 90021 : hellyeah2 ( iiI )
elif I11iiii1I == 90022 : hellyeah3 ( iiI )
elif I11iiii1I == 90023 : iIiiIIi ( )
elif I11iiii1I == 90024 : i1I111i1ii ( iiI )
elif I11iiii1I == 90025 : I1I1i ( iiI )
if 28 - 28: O0Oooo0O
elif I11iiii1I == 90026 : IIIIIII1i ( )
elif I11iiii1I == 90027 : IIIiiiiI1 ( i1I1i111Ii , iiI , OoOOOo0 )
elif I11iiii1I == 90028 : OOoOo0O00oo ( iiI )
if 27 - 27: iiiiiiii1 * oOo0O0Ooo
elif I11iiii1I == 900300 : iIi1Ii1i1iI ( )
elif I11iiii1I == 900301 : i1ii1II1ii ( iiI )
elif I11iiii1I == 900302 : oO0oo ( iiI )
elif I11iiii1I == 90030 : IIIIIo0ooOoO000oO ( )
elif I11iiii1I == 90031 : Treplays ( )
elif I11iiii1I == 90032 : Treplays2 ( iiI )
elif I11iiii1I == 90033 : Treplays3 ( iiI )
elif I11iiii1I == 90034 : Treplays4 ( iiI )
elif I11iiii1I == 90035 : II1i ( iiI )
elif I11iiii1I == 90036 : iioOOo0OOOoo0 ( iiI )
elif I11iiii1I == 90039 : oOOoo0oO00o ( iiI )
elif I11iiii1I == 90037 : o0o00O0oOooO0 ( iiI )
elif I11iiii1I == 900377 : o0OOo00oO0oOO ( iiI )
elif I11iiii1I == 90038 : OOOO0oOo00O ( )
if 60 - 60: ooOoO0O00 / oOo0O0Ooo - oOoO0o00OO0
elif I11iiii1I == 10090 : ii1i ( )
elif I11iiii1I == 10091 : o0OOoOoo ( iiI )
elif I11iiii1I == 10092 : I1IO00O0oO00o ( iiI )
elif I11iiii1I == 10093 : iIi1IIiiiI ( iiI , i1I )
elif I11iiii1I == 10094 : O0OO0OOo00Oo ( iiI , i1I )
if 41 - 41: O0Oooo0O + oOOoOooOo / OoOo0o + i1IiiiI1iI % I1ii11iIi11i
elif I11iiii1I == 10095 : IIi ( )
elif I11iiii1I == 10096 : I1IIiiII ( iiI )
elif I11iiii1I == 10097 : iIII1iIi ( iiI )
elif I11iiii1I == 10098 : o00oIIi1i1 ( iiI )
elif I11iiii1I == 10099 : i1i1iIII11i ( iiI )
if 91 - 91: oOo0O0Ooo % oOoO0o00OO0 % OOOo00oo0oO / ooOoO0O00 * iI11I1II1I1I + i1IiiiI1iI
elif I11iiii1I == 10200 : o0oOOoOOO ( )
elif I11iiii1I == 10201 : iiiii111 ( i1I1i111Ii , iiI , OoOOOo0 )
elif I11iiii1I == 10202 : OO0Oo ( iiI )
elif I11iiii1I == 10203 : RT4 ( iiI )
if 48 - 48: oOOoOooOo / oOoO0o00OO0 / oOo / IIiIiII11i * iii1i1iiiiIi
elif I11iiii1I == 90040 : OooIii1I1iI ( )
elif I11iiii1I == 90041 : I111 ( iiI )
elif I11iiii1I == 90042 : i1oooOoOoOO ( iiI )
elif I11iiii1I == 90043 : iiI1ii1Iii ( iiI )
elif I11iiii1I == 90044 : IiI1IiI1iiI1 ( iiI )
elif I11iiii1I == 90045 : Oo0Oo ( )
elif I11iiii1I == 90046 : O000o0 ( iiI )
elif I11iiii1I == 90050 : II11IiIIiiI ( )
elif I11iiii1I == 90051 : I1iII1IIi1IiI ( iiI )
elif I11iiii1I == 90052 : o00OO0o0 ( iiI )
elif I11iiii1I == 90053 : iIi1i111 ( iiI )
elif I11iiii1I == 90054 : Oo00Oooo00o ( iiI )
elif I11iiii1I == 90055 : OOOO000Ooo0O ( )
if 73 - 73: i1IiiiI1iI / oOo0O0Ooo - I11i1ii1 - ooOoO0O00 * I11i1ii1 - OoOo0o
elif I11iiii1I == 100001 : Stand_up ( )
if 39 - 39: i1IiiiI1iI . oOOoOooOo * IIiIiII11i
elif I11iiii1I == 100003 : OO0 ( iiI )
elif I11iiii1I == 100004 : I1iI1I1 ( iiI )
elif I11iiii1I == 100005 : Resolve ( iiI )
elif I11iiii1I == 100008 : Search ( )
elif I11iiii1I == 100007 : OoOo ( iiI )
elif I11iiii1I == 100009 : yt . PlayVideo ( iiI )
elif I11iiii1I == 100010 : IiiI ( iiI )
elif I11iiii1I == 100100 : IIii1I1I1I ( i1I , iiI , oooI11iI1I )
elif I11iiii1I == 100101 : OOOo00 ( iiI , i1I1i111Ii , oo0o0000 , oooI11iI1I , i1I )
elif I11iiii1I == 100102 : Ii11iii1II1i ( i1I1i111Ii , iiI , i1I , oo0o0000 )
elif I11iiii1I == 100106 : oO0O0oO0 ( iiI , i1I1i111Ii )
elif I11iiii1I == 100107 : OOOOOo ( )
elif I11iiii1I == 100108 : OoII1ii1iI1111 ( )
elif I11iiii1I == 100109 : IiIiI1 ( iiI )
elif I11iiii1I == 40000 : o00OoOooo ( )
elif I11iiii1I == 40001 : I1i1I1IIiIIi ( iiI )
elif I11iiii1I == 100110 : i1iiI1i ( iiI )
elif I11iiii1I == 100111 : O0o00 ( iiI )
elif I11iiii1I == 100112 : OoO00OOoOOOo0 ( iiI )
elif I11iiii1I == 100113 : O0o0O00o0o ( iiI )
elif I11iiii1I == 100114 : O0OOO00OOO00o ( iiI )
elif I11iiii1I == 100115 : Oo0oOO0O00 ( iiI )
elif I11iiii1I == 100117 : i11o00Ooo ( iiI )
elif I11iiii1I == 100118 : i11i ( iiI )
elif I11iiii1I == 100120 : o00OOo0o0O ( iiI )
elif I11iiii1I == 1001200 : I111Iii1 ( iiI )
elif I11iiii1I == 100210 : iI1 ( iiI )
elif I11iiii1I == 100211 : Ooo0ooo0oo ( )
elif I11iiii1I == 100212 : O00IiII ( )
elif I11iiii1I == 100213 : i1i1I1Ii1IIii ( )
elif I11iiii1I == 100214 : oO0o000oOO ( )
elif I11iiii1I == 1000111 :
 o0oo ( iiI )
 if 21 - 21: i1iIi
elif I11iiii1I == 1001111 :
 IiiiI ( i1I1i111Ii , iiI )
 if 92 - 92: oOo * oOoO0o00OO0 + iI11I1II1I1I
elif I11iiii1I == 1002111 :
 Ii1IiiI ( )
 if 88 - 88: iI11I1II1I1I + iI11I1II1I1I * Ii . oOoO0o00OO0 % OOOo00oo0oO
elif I11iiii1I == 1003111 :
 oOoOOO0O0O ( iiI , i1I1i111Ii )
 if 94 - 94: oOo0O0Ooo / oOoO0o00OO0 / OoOo0o
elif I11iiii1I == 1004111 :
 iII11i1 ( )
 if 45 - 45: IIiIiII11i
elif I11iiii1I == 1005111 :
 i11IIiIi ( iiI , i1I1i111Ii )
elif I11iiii1I == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( iiI , oo0o0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( i1I1i111Ii , iiI , oo0o0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( i1I1i111Ii , iiI , oo0o0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1105000 :
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( i1I1i111Ii , iiI , i1I , oo0o0000 , IIIIii11i1I )
elif I11iiii1I == 1106000 :
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( i1I1i111Ii )
elif I11iiii1I == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( iiI )
elif I11iiii1I == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( i1I1i111Ii )
elif I11iiii1I == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( i1I1i111Ii , iiI )
elif I11iiii1I == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif I11iiii1I == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( iiI )
elif I11iiii1I == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in iiI :
  import urlresolver
  OOOoO000 = urlresolver . resolve ( iiI )
  ii1IIII = xbmcgui . ListItem ( path = OOOoO000 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1IIII )
 elif not iiI . startswith ( "plugin://plugin" ) or not any ( x in iiI for x in pyramid . g_ignoreSetResolved ) :
  ii1IIII = xbmcgui . ListItem ( path = iiI )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1IIII )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + iiI + ')' )
elif I11iiii1I == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( i1I1i111Ii , playlist )
elif I11iiii1I == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( iiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( iiI , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1117000 :
 iiI , Oo0OoO = getRegexParsed ( regexs , iiI )
 if iiI :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( iiI , i1I1i111Ii , i1I , Oo0OoO )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif I11iiii1I == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 IIIOoO = youtubedl . single_YD ( iiI )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( IIIOoO , i1I1i111Ii , i1I )
elif I11iiii1I == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( iiI ) , i1I1i111Ii , i1I , True )
elif I11iiii1I == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , i1I1i111Ii , 'video' )
elif I11iiii1I == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( iiI , i1I1i111Ii , 'video' )
elif I11iiii1I == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( iiI , i1I1i111Ii , 'audio' )
elif I11iiii1I == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( iiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1126000 :
 i1I1i111Ii = i1I1i111Ii . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( iiI , search_term = i1I1i111Ii [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( iiI )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif I11iiii1I == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif I11iiii1I == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif I11iiii1I == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( i1I1i111Ii , iiI , i1I , oo0o0000 )
elif I11iiii1I == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( iiI , i1I , oo0o0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( iiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( i1I1i111Ii , iiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( iiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( iiI )
elif I11iiii1I == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( iiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( iiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I11iiii1I == 9050000 : Ii1 ( )
elif I11iiii1I == 9060000 : IiiiI ( i1I1i111Ii , iiI )
elif I11iiii1I == 9080000 : oOOO0O0Ooo ( )
elif I11iiii1I == 9070000 : iI1i ( )
elif I11iiii1I == 9090000 : O000oOo ( )
elif I11iiii1I == 9100000 : IIii1 ( )
elif I11iiii1I == 9110000 : IIi11 ( )
elif I11iiii1I == 9110001 : i1ii11 ( iiI )
elif I11iiii1I == 9110002 : Ii1II11II1iii ( iiI , i1I1i111Ii , i1I )
elif I11iiii1I == 9110003 : I1Iii1iI1 ( i1I1i111Ii , oooI11iI1I )
elif I11iiii1I == 9110005 : OO00oo ( OoOOOo0 , iiI )
elif I11iiii1I == 9110004 : oO0o ( )
elif I11iiii1I == 9110010 : O0OOoOOooO ( iiI )
elif I11iiii1I == 9110011 : o0oiIiI1i1iiIi1i ( )
elif I11iiii1I == 9110012 : iIIIII ( iiI , i1I1i111Ii )
elif I11iiii1I == 9110013 : oO0oooooo ( iiI )
elif I11iiii1I == 9110014 : oo00OoO ( i1I1i111Ii , iiI )
elif I11iiii1I == 9110015 : o0Oii1111i ( )
elif I11iiii1I == 9999999 : i111IIiIiiI1 ( )
elif I11iiii1I == 19999999 : ooO000OO ( )
elif I11iiii1I == 1999990 : OOo000OO000 ( )
elif I11iiii1I == 21999990 : oooO ( )
elif I11iiii1I == 21999991 : oOoo0oOo00 ( iiI )
elif I11iiii1I == 21999992 : IiiiIiii11 ( iiI )
elif I11iiii1I == 21999993 : OO0000o ( iiI )
elif I11iiii1I == 21999994 : i1I1i1 ( iiI , i1I )
elif I11iiii1I == 21999995 : O0OoooO0 ( iiI )
elif I11iiii1I == 21999996 : I1i11 ( iiI , i1I )
elif I11iiii1I == 21999997 : IiIIi1 ( iiI , i1I )
elif I11iiii1I == 21999998 : II1i11I ( i1I1i111Ii , iiI , i1I )
elif I11iiii1I == 219999989 : OOI1iI1ii1II ( )
elif I11iiii1I == 219999990 : oO00O0 ( all = True )
elif I11iiii1I == 219999991 : o0Oo00o0 ( )
elif I11iiii1I == 219999992 : oOOoOo0Ooo ( )
elif I11iiii1I == 300000000 : I11I ( )
elif I11iiii1I == 300000001 : i1i1iI1iiiI ( iiI )
if 86 - 86: Ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
