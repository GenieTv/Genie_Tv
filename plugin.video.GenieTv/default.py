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
 if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = "3.6.4"
IiII = 'plugin.video.GenieTv'
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
i1i1II = xbmc . translatePath ( 'special://home/addons/' )
O0oo0OO0 = xbmc . translatePath ( 'special://home/addonsbroke/' )
I1i1iiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
iiIIIII1i1iI = 'plugin.video.GenieTv'
o0oO0 = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
oo00 = xbmcaddon . Addon ( id = iiIIIII1i1iI )
o00 = xbmc . translatePath ( 'special://home/media' )
Oo0oO0ooo = 'plugin.video.GenieTv'
o0oOoO00o = xbmcgui . DialogProgress ( )
i1 = '[COLORsteelblue]GenieTv[/COLOR]'
oOOoo00O0O = base64 . b64decode ( 'aHR0cDovL2dlbmlldHYuY28udWsvc3BlZWR0ZXN0LnR4dA==' )
i1111 = uservar . CONTACT
i11 = base64 . decodestring
I11 = xbmcaddon . Addon ( ) . setSetting
Oo0o0000o0o0 = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIv' ) )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
oO0o0o0ooO0oO = os . path . join ( oOo0oooo00o , 'userdata' )
oo0o0O00 = os . path . join ( oO0o0o0ooO0oO , 'addon_data' , IiII )
oO = os . path . join ( oo0o0O00 , 'wizard.log' )
i1iiIIiiI111 = uservar . ADDONTITLE
oooOOOOO = xbmc . translatePath ( 'special://profile/' )
i1iiIII111ii = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
i1i1II = os . path . join ( oOo0oooo00o , 'addons' )
i1iIIi1 = os . path . join ( i1i1II , 'packages' )
ii11iIi1I = os . path . join ( oO0o0o0ooO0oO , 'Thumbnails' )
iI111I11I1I1 = os . path . join ( oO0o0o0ooO0oO , 'Database' )
OOooO0OOoo = os . path . join ( i1i1II , 'HUB' )
iIii1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
oOOoO0 = Net ( )
O0OoO000O0OO = xbmcgui . Dialog ( )
iiI1IiI = oo00 . getSetting ( 'Build' )
II = oo00 . getSetting ( 'Local' )
ooOoOoo0O = oo00 . getSetting ( 'Remote' )
OooO0 = oo00 . getSetting ( 'LocalM3u' )
II11iiii1Ii = oo00 . getSetting ( 'TEXTCOL' )
OO0o = oo00 . getSetting ( 'Downloads' )
Ooo = xbmc . translatePath ( 'special://logpath/' )
O0o0Oo = oo00 . getSetting ( 'User' )
Oo00OOOOO = oo00 . getSetting ( 'Pass' )
O0O = oo00 . getSetting ( 'DNS' )
if O0O == 'Option 1' :
 O00o0OO = '.net'
if O0O == 'Option 2' :
 O00o0OO = '.eu'
if O0O == 'Option 3' :
 O00o0OO = '.com'
I11i1 = oo00 . getSetting ( 'AdultPass' )
O0OoO000O0OO = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
iIi1ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
I11II1i = ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
IIIII = xbmc . translatePath ( 'special://database' )
ooooooO0oo = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
IIiiiiiiIi1I1 = xbmc . translatePath ( 'special://thumbnails' ) ;
I1IIIii = "GenieTv"
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
OOO00 = 'http://'
iiiiiIIii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ2VuaWV0dl9hcnQvYmVuc19hcnQv' )
O000OO0 = datetime . now ( )
I11iii1Ii = base64 . decodestring ( 'LnBocA==' )
I1IIiiIiii = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
O000oo0O = [ ]
OOOOi11i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
IIIii1II1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
i1I1iI = oo00 . getLocalizedString
oo0OooOOo0 = CookieJar ( )
o0O = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( oo0OooOOo0 ) )
o0O . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O00oO = int ( sys . argv [ 1 ] )
I11i1I1I = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
oO0Oo = os . path . join ( ooooooO0oo , 'favorites' )
oOOoo0Oo = ooooooO0oo + '/addons.ini'
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/' )
o00OO00OoO = xbmc . translatePath ( 'special://home/userdatabroke/' )
OOOO0OOoO0O0 = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
O0Oo000ooO00 = xbmc . translatePath ( 'special://home/userdata/addon_data' )
oO0 = O0Oo000ooO00 + 'GenieTvWatched'
Ii1iIiII1ii1 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
ooOooo000oOO = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
Oo0oOOo = oO0 + 'watched.txt'
if not os . path . exists ( oO0 ) :
 os . makedirs ( oO0 )
Oo0oOOo = oO0 + 'watched.txt'
if not os . path . exists ( Oo0oOOo ) :
 open ( Oo0oOOo , 'w+' )
Oo0OoO00oOO0o = open ( Oo0oOOo ) . read ( )
OOO00O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlNvbGQv' ) )
OOoOO0oo0ooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
O0o0O00Oo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
O00O0oOO00O00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
i1Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
i1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( oO0Oo ) == True :
 iiI111I1iIiI = open ( oO0Oo ) . read ( )
else : iiI111I1iIiI = [ ]
IIIi1I1IIii1II = oo00 . getSetting ( 'debug' )
if os . path . exists ( ooooooO0oo ) == False :
 os . makedirs ( ooooooO0oo )
def O0 ( url ) :
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oooooOoo0ooo = ''
 I1I1IiI1 = ''
 try :
  oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
  I1I1IiI1 = oooooOoo0ooo . read ( )
  oooooOoo0ooo . close ( )
 except : pass
 if I1I1IiI1 != '' :
  return I1I1IiI1
 else :
  I1I1IiI1 = 'Failed'
  return I1I1IiI1
  if 5 - 5: ooOO0O0ooOooO * IIIi11I1 - iIII % Ii1i1i . IIIIiiII111
OOoOoo = [ ]
oO0000OOo00 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if oO0000OOo00 != 'Failed' :
 OOoOoo . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not oO0000OOo00 != 'Failed' :
 iiIi1IIiIi = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if iiIi1IIiIi != 'Failed' :
  OOoOoo . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not iiIi1IIiIi != 'Failed' :
  oOO00Oo = O0 ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if oOO00Oo != 'Failed' :
   OOoOoo . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not oOO00Oo != 'Failed' :
   i1iIIIi1i = O0 ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if i1iIIIi1i != 'Failed' :
    OOoOoo . append ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
iI1iIIiiii = ( str ( OOoOoo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
if 26 - 26: o0O00o . o0O0Oooo0O
if 84 - 84: oOOoOooOo . o0O0Oooo0O - iIII + IIIIiiII111 % iI11I1II1I1I / ii
if 61 - 61: ii - OOooOOo % Ii1i1i % o0O0Oooo0O + Ii1I
def OOooOoooOoOo ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  O0OoO000O0OO . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  o0OOOO00O0Oo = 'genie tv repo not being installed '
  iioOooOOOoOo ( )
 else :
  i1Iii1i1I ( )
  if 91 - 91: Ii1I + oOo0O0Ooo . IIIi11I1 * Ii1I + oOo0O0Ooo * I1ii11iIi11i
def i1Iii1i1I ( ) :
 if 80 - 80: IIIIiiII111 % IIIi11I1 % ooOO0O0ooOooO - I1ii11iIi11i + I1ii11iIi11i
 iIiii1i111iI1 = i11oO0oOo0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 I1I1I = open ( i1Oo00 ) . read ( )
 OoOO000 = open ( i1i ) . read ( )
 if 14 - 14: o0O00o - Ii1I
 Ii1i1iI1iIIi = re . compile ( 'version="([^"]*)" provider' ) . findall ( I1I1I )
 I1Ii = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( OoOO000 )
 O0oo00o0O = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( iIiii1i111iI1 )
 i1I1I = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( iIiii1i111iI1 )
 for iiI1I in Ii1i1iI1iIIi :
  IiIiiIIiI = iiI1I
  for ooOO0OOOO0oo0 in O0oo00o0O :
   if not ooOO0OOOO0oo0 == IiIiiIIiI :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    I11iiI1i1 ( )
   if ooOO0OOOO0oo0 == IiIiiIIiI :
    I1i1Iiiii
 for OOo0oO00ooO00 in I1Ii :
  oOO0O00oO0Ooo = OOo0oO00ooO00
  for oO0Oo0O0o in i1I1I :
   if not oO0Oo0O0o == oOO0O00oO0Ooo :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    iioOooOOOoOo ( )
   if oO0Oo0O0o == oOO0O00oO0Ooo :
    xbmc . sleep ( 100 )
    I1i1Iiiii
def OO ( ) :
 if not os . path . exists ( OOOO ) :
  I1iI1ii1II ( 'Change Log 21/02/2018 - v3.6.4' , '[COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
  os . makedirs ( OOOO )
def O0O0OOOOoo ( ) :
 I1iI1ii1II ( 'Change Log 21/02/2018 - v3.6.4' , '[COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]' )
def oOooO0 ( ) :
 I1iI1ii1II ( O00o0OO , O00o0OO )
def I1iI1ii1II ( title , msg ) :
 class Ii1I1Ii ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 69 - 69: oOo0O0Ooo / I11i . o0O00o * o0O0Oooo0O % Ii1i1i - I11i
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 13 - 13: Ii1i1i . Ii
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 56 - 56: Ii1I % o0o00Oo0O - oOo0O0Ooo
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 100 - 100: Ii1i1i - o0o00Oo0O % ooOO0O0ooOooO * IIIi11I1 + oOo0O0Ooo
 Oo0O0oooo = Ii1I1Ii ( "Textbox.xml" , oo00 . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 Oo0O0oooo . doModal ( )
 del Oo0O0oooo
 if 33 - 33: o0O0Oooo0O + IIIIiiII111 * ooOO0O0ooOooO / iI11I1II1I1I - oOo0O0Ooo
def O0oO ( ) :
 OOooOoooOoOo ( )
 OO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OO0ooOOO0OOO ( )
 else :
  if 63 - 63: OOooOOo * IIIIiiII111
  if 69 - 69: o0o00Oo0O . oO0o
  if 49 - 49: oOo0O0Ooo - iIII
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']G-Tv Live List[/COLOR]' , '' , 4009 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Tommys Sports[/COLOR]' , '' , 90010 , iiiiiIIii + 'tommys.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']STREAMS[/COLOR]' , str ( iI1iIIiiii ) , 4002 , iiiiiIIii + 'Streams.png' , iIi1ii1I1 , '' )
   if 87 - 87: oOo0O0Ooo
  if oo00 . getSetting ( 'Music' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Music[/COLOR]' , str ( iI1iIIiiii ) , 4003 , iiiiiIIii + 'Music.png' , iIi1ii1I1 , '' )
  if I11i1 == '5knuckleshuffle' :
   OoOOoOooooOOo ( '[COLORorangered]Adult Content[/COLOR]' , '' , 19999999 , iiiiiIIii + 'AG.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , '' , 90001 , iiiiiIIii + 'tools.png' , iIi1ii1I1 , '' )
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , iiiiiIIii + 'settings.png' , iIi1ii1I1 , '' )
  if iIII1I111III ( ) == 'android' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']APK TOOL[/COLOR]' , str ( iI1iIIiiii ) , 30039 , iiiiiIIii + 'APKpng' , iIi1ii1I1 , '' )
   if 20 - 20: I11i . IIiIiII11i % IIIi11I1 * iI11I1II1I1I
   if 98 - 98: oOo0O0Ooo % Ii1i1i * ii
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MAINTENANCE[/COLOR]' , str ( iI1iIIiiii ) , 3 , iiiiiIIii + 'Maintenance.png' , iIi1ii1I1 , '' )
   if 51 - 51: iI11I1II1I1I . OOooOOo / ooOO0O0ooOooO + I11i
   if 33 - 33: oOOoOooOo . IIiIiII11i % IIIIiiII111 + I11i
   if 71 - 71: I1ii11iIi11i % IIIi11I1
   if 98 - 98: iIII % Ii % oOOoOooOo + Ii1i1i
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def OO0ooOOO0OOO ( ) :
 if 11 - 11: oOo0O0Ooo
 if 16 - 16: Ii1i1i + o0O00o * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
 if 67 - 67: ii / oOo0O0Ooo * Ii1i1i + iIII
 if 65 - 65: ii - Ii1I / oOOoOooOo / IIiIiII11i / ooOoO0O00
 if 71 - 71: o0O0Oooo0O + Ii1i1i
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Tommys Sports[/COLOR]' , '' , 90010 , iiiiiIIii + 'tommys.png' , iIi1ii1I1 , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']STREAMS[/COLOR]' , str ( iI1iIIiiii ) , 4002 , iiiiiIIii + 'Streams.png' , iIi1ii1I1 , '' )
  if 28 - 28: IIIi11I1
 if oo00 . getSetting ( 'Music' ) == 'true' :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Music[/COLOR]' , str ( iI1iIIiiii ) , 4003 , iiiiiIIii + 'Music.png' , iIi1ii1I1 , '' )
 if I11i1 == '5knuckleshuffle' :
  OoOOoOooooOOo ( '[COLORorangered]Adult Content[/COLOR]' , '' , 19999999 , iiiiiIIii + 'AG.png' , iIi1ii1I1 , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MAINTENANCE[/COLOR]' , str ( iI1iIIiiii ) , 3 , iiiiiIIii + 'Maintenance.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , '' , 90001 , iiiiiIIii + 'png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def tools ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']Change Log[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Force Genie Update Kodi[/COLOR]' , '[COLOR' + II11iiii1Ii + ']APK TOOL[/COLOR]' , '[COLOR' + II11iiii1Ii + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CONTACT US[/COLOR]' , '[COLOR' + II11iiii1Ii + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SOURCE LIST[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  O0O0OOOOoo ( )
 if OoOOo0OOoO == 1 :
  I11iiI1i1 ( )
 if OoOOo0OOoO == 2 :
  ooO0O00Oo0o ( )
 if OoOOo0OOoO == 3 :
  OOO ( Oo0o00OO0000 )
 if OoOOo0OOoO == 4 :
  O0OoO000O0OO . ok ( i1 , i1111 )
 if OoOOo0OOoO == 5 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if OoOOo0OOoO == 6 :
  I1i ( )
  if 99 - 99: o0O0Oooo0O + OOooOOo * iI11I1II1I1I / ii
def i11I ( ) :
 OoOOoOooooOOo ( 'Stories' , 'http://etc.usf.edu/lit2go/books/' , 21999995 , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , '' )
 OoOOoOooooOOo ( 'Virtual FirePlaces' , 'http://www.virtual-fireplace.net/fireplaces.html' , 21999991 , 'http://www.virtual-fireplace.net/files/theme/burning-log.gif' , 'http://www.virtual-fireplace.net/files/theme/burning-log1.gif' , '' )
 OoOOoOooooOOo ( 'Nature Sounds' , 'http://www.virtual-fireplace.net/sounds.html' , 21999993 , 'http://www.virtual-fireplace.net/files/theme/sound.gif' , 'http://www.virtual-fireplace.net/files/theme/sound-bw.gif' , '' )
def o00Oo0oooooo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in O0oO0 :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 21999992 , 'http://www.virtual-fireplace.net/' + iII11 , 'http://www.virtual-fireplace.net/' + iII11 , iiIiii1IIIII )
def o00o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( 'rel="canonical" href="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in O0oO0 :
  url = ( url ) . replace ( '//www.youtube.com/embed/' , '' ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' )
  yt . PlayVideo ( url )
def IIIIiiIiiI ( url ) :
 OoOOoOooooOOo ( 'Rain And Thunder' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , '' )
 OoOOoOooooOOo ( 'Water And Forests' , 'http://www.virtual-fireplace.net/water-and-forest.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , '' )
 OoOOoOooooOOo ( 'Beach And Ocean' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , '' )
def IIIIiI11I11 ( url , iconimage ) :
 iII11 = iconimage
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in O0oO0 :
  oOOOoo0O0oO ( iiIiii1IIIII , 'http:' + url , 21999992 , iII11 , iII11 , '' )
def oo00o0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( 'data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url , i11II1I11I1 in O0oO0 :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 21999996 , iII11 , iII11 , ( i11II1I11I1 ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def OOoOO0ooo ( url , iconimage ) :
 iII11 = iconimage
 i11II1I11I1 = 'desc'
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , II1iIi11 in O0oO0 :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR] - Audio' , url , 21999997 , iII11 , iII11 , ( II1iIi11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( II1iIi11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR] - Text' , url , 21999998 , iII11 , iII11 , ( II1iIi11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) , ( II1iIi11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def I11iiii ( url , iconimage ) :
 iII11 = iconimage
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '<a href="([^"]*)">Audio</a>' ) . findall ( oO0000OOo00 )
 for url in O0oO0 :
  O0i1iI ( url )
def IiI1iiiIii ( name , url , iconimage ) :
 iII11 = iconimage
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '</audio>(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for II1iIi11 in O0oO0 :
  I1iI1ii1II ( ( name ) . replace ( ' - Text' , '' ) , ( II1iIi11 ) . replace ( '&ldquo;' , '"' ) . replace ( '&rdquo;' , '"' ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  if 7 - 7: o0O0Oooo0O * oO0o - oOOoOooOo + IIIi11I1 * oOo0O0Ooo % oO0o
  if 15 - 15: OOooOOo % oOo0O0Ooo * iIII
def O0OoooO0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
 for url , iII11 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in O0oO0 :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 21009 , iII11 , ooo0O0o00O , i11II1I11I1 )
  if 48 - 48: oOOoOooOo / o0O0Oooo0O . iI11I1II1I1I * OOooOOo * ooOO0O0ooOooO / ooOoO0O00
def OOOOoOOo0O0 ( url ) :
 url = url
 oOooo0 = iIII1I111III ( )
 if oOooo0 ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif oOooo0 ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 58 - 58: oOo0O0Ooo . IIIIiiII111 + OOooOOo
  if 66 - 66: IIIIiiII111 / ooOO0O0ooOooO * ii + ii % iIII
def IIii1111 ( ) :
 Oo0o00OO0000 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 IIIIiIiIi1 = os . path . join ( I1iI , 'GuideSkins' + '.zip' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( Oo0o00OO0000 , IIIIiIiIi1 , o0oOoO00o )
 I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11iiiiI1i
 print '======================================='
 extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
 iI1i11 ( Oo0o00OO0000 )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOOoooOO0O ( )
def ooo00Ooo ( ) :
 Oo0o0O00 = ii1 ( )
 I1i11 = Oo0o0O00 . replace ( Ooo , "" )
 if os . path . exists ( Oo0o0O00 ) or not Oo0o0O00 == False :
  OOo0O0oo0OO0O = open ( Oo0o0O00 , mode = 'r' ) ; OO0 = OOo0O0oo0OO0O . read ( ) ; OOo0O0oo0OO0O . close ( )
  I1iI1ii1II ( "%s - %s" % ( i1 , I1i11 ) , OO0 )
 else :
  o0Oooo ( 'View Log' , 'No Log File Found!' )
def iiI ( log = None , count = None , all = None ) :
 if log == None :
  oOIIiIi = OOoOooOoOOOoo ( True )
  Iiii1iI1i = OOoOooOoOOOoo ( True , True )
  if not Iiii1iI1i == False and not oOIIiIi == False :
   I1ii1ii11i1I = O0OoO000O0OO . select ( i1iiIIiiI111 , [ "View %s: %s error(s)" % ( oOIIiIi . replace ( Ooo , "" ) , iiI ( oOIIiIi , True , True ) ) , "View %s: %s error(s)" % ( Iiii1iI1i . replace ( Ooo , "" ) , iiI ( Iiii1iI1i , True , True ) ) ] )
   if I1ii1ii11i1I == - 1 : o0Oooo ( '[COLOR %s]View Log[/COLOR]' % o0OoOO , '[COLOR %s]View Log Cancelled![/COLOR]' % O0O0Oo00 ) ; return
  elif oOIIiIi == False and Iiii1iI1i == False :
   o0Oooo ( '[COLOR %s]View Log[/COLOR]' % o0OoOO , '[COLOR %s]No Log File Found![/COLOR]' % O0O0Oo00 )
   return
  elif not oOIIiIi == False : I1ii1ii11i1I = 0
  elif not Iiii1iI1i == False : I1ii1ii11i1I = 1
  log = oOIIiIi if I1ii1ii11i1I == 0 else Iiii1iI1i
 if log == False :
  if count == None :
   o0Oooo ( "[COLOR %s]%s[/COLOR]" % ( o0OoOO , i1iiIIiiI111 ) , "[COLOR %s]Log File not Found[/COLOR]" % O0O0Oo00 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   OOo0O0oo0OO0O = open ( log , mode = 'r' ) ; oOoO00o = OOo0O0oo0OO0O . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; OOo0O0oo0OO0O . close ( )
   Ii1i1iI1iIIi = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( oOoO00o )
   if not count == None :
    if all == None :
     oO00O0 = 0
     for IIi1IIIi in Ii1i1iI1iIIi :
      if IiII in IIi1IIIi : oO00O0 += 1
     return oO00O0
    else : return len ( Ii1i1iI1iIIi )
   if len ( Ii1i1iI1iIIi ) > 0 :
    oO00O0 = 0 ; OO0 = ""
    for IIi1IIIi in Ii1i1iI1iIIi :
     if all == None and not IiII in IIi1IIIi : continue
     else :
      oO00O0 += 1
      OO0 += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( oO00O0 , IIi1IIIi . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( oOo0oooo00o , '' ) )
    if oO00O0 > 0 :
     I1iI1ii1II ( i1iiIIiiI111 , OO0 )
    else : o0Oooo ( i1iiIIiiI111 , "No Errors Found in Log" )
   else : o0Oooo ( i1iiIIiiI111 , "No Errors Found in Log" )
  else : o0Oooo ( i1iiIIiiI111 , "Log File not Found" )
def OOoOooOoOOOoo ( file = False , old = False , wizard = False ) :
 if wizard == True :
  if not os . path . exists ( oO ) : return False
  else :
   if file == True :
    return oO
   else :
    O00Ooo = open ( oO , 'r' )
    OOOO0OOO = O00Ooo . read ( )
    O00Ooo . close ( )
    return OOOO0OOO
 i1i1ii = 0
 iII1ii1 = os . listdir ( Ooo )
 I1i1iiiI1 = [ ]
 if 24 - 24: ooOO0O0ooOooO / Ii + ooOO0O0ooOooO
 for IIi1IIIi in iII1ii1 :
  if old == True and IIi1IIIi . endswith ( '.old.log' ) : I1i1iiiI1 . append ( os . path . join ( Ooo , IIi1IIIi ) )
  elif old == False and IIi1IIIi . endswith ( '.log' ) and not IIi1IIIi . endswith ( '.old.log' ) : I1i1iiiI1 . append ( os . path . join ( Ooo , IIi1IIIi ) )
  if 20 - 20: iIII + Ii1i1i / o0o00Oo0O % iI11I1II1I1I
 if len ( I1i1iiiI1 ) > 0 :
  I1i1iiiI1 . sort ( key = lambda OOo0O0oo0OO0O : os . path . getmtime ( OOo0O0oo0OO0O ) )
  if file == True : return I1i1iiiI1 [ - 1 ]
  else :
   O00Ooo = open ( I1i1iiiI1 [ - 1 ] , 'r' )
   OOOO0OOO = O00Ooo . read ( )
   O00Ooo . close ( )
   return OOOO0OOO
 else :
  return False
  if 88 - 88: OOooOOo / IIiIiII11i
def IIii1111 ( ) :
 Oo0o00OO0000 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 IIIIiIiIi1 = os . path . join ( I1iI , 'GuideSkins' + '.zip' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( Oo0o00OO0000 , IIIIiIiIi1 , o0oOoO00o )
 I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11iiiiI1i
 print '======================================='
 extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
 iI1i11 ( Oo0o00OO0000 )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOOoooOO0O ( )
def OOOOO0O00 ( ) :
 Iii ( '[COLOR' + II11iiii1Ii + ']Todays Games[/COLOR]' , '' , 90030 , iiiiiIIii + 'tgames.png' , iIi1ii1I1 , '' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Tommys Replays[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , iiiiiIIii + 'tommysreplays.png' , iIi1ii1I1 , '' )
 if 31 - 31: I11i % oO0o
 if 14 - 14: ooOO0O0ooOooO / ooOO0O0ooOooO % oOOoOooOo
 if 56 - 56: oOo0O0Ooo . o0o00Oo0O + I1ii11iIi11i
def i1II1I1Iii1 ( ) :
 iiI11Iii = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 O0o0O0 = requests . get ( Oo0o00OO0000 ) . content
 Ii1i1iI1iIIi = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( O0o0O0 )
 Ii1II1I11i1 = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( Ii1i1iI1iIIi ) )
 for I1I1IiI1 , iiIiii1IIIII in Ii1II1I11i1 :
  if not iiIiii1IIIII == 'Home' :
   pass
   oOoooooOoO = 'http://www.replaymatches.com/' + I1I1IiI1
   if iiIiii1IIIII in iiI11Iii :
    OoOOoOooooOOo ( '[COLORred]' + iiIiii1IIIII + '[/COLOR]' , oOoooooOoO , 900301 , iiiiiIIii + 'tommysreplays.png' , '' , '' )
   else :
    OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , oOoooooOoO , 900301 , iiiiiIIii + 'tommysreplays.png' , '' , '' )
    if 33 - 33: IIiIiII11i / oOOoOooOo * o0o00Oo0O % Ii1i1i * o0O0Oooo0O
def O0o ( url ) :
 if 72 - 72: IIIi11I1 % Ii1I + oO0o / ooOO0O0ooOooO + o0O00o
 if 10 - 10: o0O0Oooo0O / oOOoOooOo + Ii / Ii1i1i
 if 74 - 74: IIIi11I1 + o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
 if 83 - 83: Ii1I - oOo0O0Ooo + IIIi11I1
 if 5 - 5: Ii1i1i
 if 46 - 46: o0O00o
 if 45 - 45: oOOoOooOo
 if 21 - 21: ooOO0O0ooOooO . o0O0Oooo0O . IIIi11I1 / I1ii11iIi11i / o0O0Oooo0O
 if 17 - 17: IIIi11I1 / IIIi11I1 / iIII
 if 1 - 1: ooOoO0O00 . Ii % IIIi11I1
 oO0000OOo00 = i11oO0oOo0 ( url )
 OooO0oo = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( oO0000OOo00 )
 o0o0oOoOO0O = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in OooO0oo :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 900302 , iII11 , iiiiiIIii + 'tommysreplays.png' , '' )
 for i1ii1II1ii in o0o0oOoOO0O :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NEXT PAGE[/COLOR]' , i1ii1II1ii , 900301 , iiiiiIIii + 'NEXT.png' , '' , '' )
def iII111Ii ( url ) :
 O0o0O0 = requests . get ( url ) . content
 Ii1i1iI1iIIi = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( O0o0O0 )
 for I1I1IiI1 , iII11 in Ii1i1iI1iIIi :
  if 'Highlight' in iII11 :
   iiIiii1IIIII = 'HighLights'
  elif '1st' in iII11 :
   iiIiii1IIIII = '1st Half'
  elif '2nd' in iII11 :
   iiIiii1IIIII = '2nd Half'
  Ooo00OoOOO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , I1I1IiI1 , 1001111 , iII11 , iiiiiIIii + 'tommysreplays.png' , '' , '' )
def Oo0OO0000oooo ( ) :
 O0o0O0 = requests . get ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 Ii1i1iI1iIIi = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( O0o0O0 )
 for IIII1iII , ii1III11 in Ii1i1iI1iIIi :
  Iii ( '[COLORred]' + IIII1iII + '[/COLOR]' , '' , '' , iiiiiIIii + 'tommysreplays.png' , iiiiiIIii + 'tommysreplays.png' , '' , '' )
  I1iiIIIi11 = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( ii1III11 ) )
  for Ii1I11ii1i , O0iIiIIIIIii in I1iiIIIi11 :
   Iii ( '[COLOR' + II11iiii1Ii + ']' + Ii1I11ii1i + '[/COLOR]' , '' , '' , O0iIiIIIIIii , iiiiiIIii + 'tommysreplays.png' , '' , '' )
   if 58 - 58: I11i / o0O00o . OOooOOo / ii + o0O0Oooo0O
def O0OoO0ooOO0o ( url ) :
 if 81 - 81: o0o00Oo0O * IIiIiII11i + oOo0O0Ooo * Ii - Ii1I / oOo0O0Ooo
 if 63 - 63: OOooOOo - ii % o0O0Oooo0O
 if 77 - 77: oO0o . ooOoO0O00
 if 35 - 35: oOOoOooOo * IIIi11I1 . iIII * I11i . OOooOOo / o0o00Oo0O
 if 100 - 100: o0O0Oooo0O . I11i * I1ii11iIi11i % o0o00Oo0O * o0o00Oo0O
 if 14 - 14: Ii1I . oOOoOooOo + IIiIiII11i / IIIIiiII111 / iIII
 if 74 - 74: o0o00Oo0O / ooOoO0O00
 if 78 - 78: ii . oO0o + oOOoOooOo - ooOoO0O00
 if 31 - 31: ii . IIIi11I1
 if 83 - 83: IIIIiiII111 . o0o00Oo0O / I1ii11iIi11i / IIIi11I1 - IIiIiII11i
 if 100 - 100: oO0o
 if 46 - 46: OOooOOo / iI11I1II1I1I % IIIIiiII111 . iI11I1II1I1I * IIIIiiII111
 if 38 - 38: Ii1I - IIIIiiII111 / o0o00Oo0O . o0O0Oooo0O
 if 45 - 45: o0O0Oooo0O
 if 83 - 83: OOooOOo . ii
 if 58 - 58: Ii + ii % ii / o0O00o / Ii
 if 62 - 62: oO0o / Ii1I
 if 7 - 7: ii . o0O00o
 if 53 - 53: Ii1i1i % Ii1i1i * I11i + OOooOOo
 if 92 - 92: ii + ooOoO0O00 / Ii1i1i * o0o00Oo0O
 if 100 - 100: oOOoOooOo % iI11I1II1I1I * IIiIiII11i - IIIIiiII111
 if 92 - 92: oOOoOooOo
 if 22 - 22: I1ii11iIi11i % IIIIiiII111 * Ii1I / IIIi11I1 % Ii * iIII
 if 95 - 95: ii - o0O00o * oOo0O0Ooo + OOooOOo
 if 10 - 10: I11i / Ii
 if 92 - 92: iIII . o0O0Oooo0O
 if 85 - 85: Ii1I . o0O0Oooo0O
 if 78 - 78: oOOoOooOo * o0O0Oooo0O + iI11I1II1I1I + iI11I1II1I1I / o0O0Oooo0O . Ii1i1i
 if 97 - 97: oOOoOooOo / o0O0Oooo0O % ooOoO0O00 % Ii1I
 if 18 - 18: iI11I1II1I1I % iIII
 if 95 - 95: oOOoOooOo + Ii * o0O0Oooo0O - ooOoO0O00 * o0O0Oooo0O - iI11I1II1I1I
 if 75 - 75: ii * o0O00o
 if 9 - 9: o0O00o - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
 if 39 - 39: o0O00o * I1ii11iIi11i + iI11I1II1I1I - o0O00o + IIIi11I1
 if 69 - 69: o0o00Oo0O
 if 85 - 85: oOOoOooOo / o0o00Oo0O
 if 18 - 18: I11i % o0o00Oo0O * Ii1I
 if 62 - 62: o0O0Oooo0O . o0O00o . ii
 if 11 - 11: IIIi11I1 / iIII
 oooO0 = liveresolver . resolve ( url )
 IIi1IIIi = xbmcgui . ListItem ( path = oooO0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIi1IIIi )
def iiIIiii ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 iiIIIiIi1IIi = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIi1IIi )
def ii1 ( ) :
 ii11i = False
 if os . path . exists ( os . path . join ( Ooo , 'xbmc.log' ) ) :
  ii11i = os . path . join ( Ooo , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( Ooo , 'kodi.log' ) ) :
  ii11i = os . path . join ( Ooo , 'kodi.log' )
 elif os . path . exists ( os . path . join ( Ooo , 'spmc.log' ) ) :
  ii11i = os . path . join ( Ooo , 'spmc.log' )
 elif os . path . exists ( os . path . join ( Ooo , 'tvmc.log' ) ) :
  ii11i = os . path . join ( Ooo , 'tvmc.log' )
 return ii11i
 if 35 - 35: Ii1I * IIIIiiII111 - oO0o % I11i
def oOo00O000Oo0 ( url ) :
 if url == 'http://' : return False
 try :
  ii1ii1ii = urllib2 . Request ( url )
  ii1ii1ii . add_header ( 'User-Agent' , I1i1iiI1 )
  oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
  oooooOoo0ooo . close ( )
 except Exception , I1iI1I1I1i11i :
  return I1iI1I1I1i11i
 return True
def iiI11 ( ) :
 if 63 - 63: oO0o + Ii1I . o0O0Oooo0O % o0O0Oooo0O
 if 57 - 57: IIiIiII11i
 if 54 - 54: I1ii11iIi11i + ooOO0O0ooOooO + Ii
 if 28 - 28: ooOO0O0ooOooO
 if 70 - 70: o0O00o
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def i11i1iiI1i ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II11iiii1Ii + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II11iiii1Ii + ']WIPE GENIE[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Genie BUILDS[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Wizard[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   oO0oOOoo00000 ( )
  if OoOOo0OOoO == 1 :
   oOo00 ( )
  if OoOOo0OOoO == 2 :
   i1iI11i1IIi ( ii1IIi111 )
  if OoOOo0OOoO == 3 :
   iI1 ( Oo0o00OO0000 )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']BACKUP MY BUILD[/COLOR]' , str ( iI1iIIiiii ) , 10060 , iiiiiIIii + 'BackupMyBuild.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']RESTORE MY BUILD[/COLOR]' , str ( iI1iIIiiii ) , 49 , iiiiiIIii + 'RestoreMyBuild.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']WIPE GENIE[/COLOR]' , str ( iI1iIIiiii ) , 41 , iiiiiIIii + 'WipeGenie.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Genie BUILDS[/COLOR]' , str ( iI1iIIiiii ) , 44 , iiiiiIIii + 'GenieBuilds.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 86 - 86: IIiIiII11i % Ii + Ii1i1i % Ii
def Ooo0o0OOO ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if 35 - 35: IIIi11I1 + IIIIiiII111
  if 40 - 40: I11i
  if oo00 . getSetting ( 'Search' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH[/COLOR]' , str ( iI1iIIiiii ) , 9000 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']APPRENTICE[/COLOR]' , '' , 1017 , iiiiiIIii + 'appstreams.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiiiiIIii + 'Technica-Streams.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Genie On Demand Streams[/COLOR]' , ( i11 ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3NoYWthL0dPRFMucGhw' ) ) , 1016 , iiiiiIIii + 'gods.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , iiiiiIIii + 'Bamf.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiiiiIIii + 'boss.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Supremacy[/COLOR]' , '' , 1131000 , iiiiiIIii + 'supremacy.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MOVIES[/COLOR]' , str ( iI1iIIiiii ) , 4004 , iiiiiIIii + 'Movies.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TV SHOWS[/COLOR]' , str ( iI1iIIiiii ) , 4005 , iiiiiIIii + 'TVShows.png' , iIi1ii1I1 , '' )
  if 67 - 67: ooOO0O0ooOooO + IIiIiII11i - o0o00Oo0O . ooOO0O0ooOooO * IIiIiII11i * iIII
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']KIDS[/COLOR]' , str ( iI1iIIiiii ) , 4007 , iiiiiIIii + 'Kids.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FREEVIEW[/COLOR]' , str ( iI1iIIiiii ) , 90023 , iiiiiIIii + 'freeview.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiiiiIIii + 'zone.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']STREAM CATEGORIES[/COLOR]' , str ( iI1iIIiiii ) , 90002 , iiiiiIIii + 'cats.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'Fitness' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FITNESS[/COLOR]' , '' , 7084 , iiiiiIIii + 'Fitness.png' , iIi1ii1I1 , '' )
   if 90 - 90: Ii1i1i . o0O00o
   if 81 - 81: IIIi11I1 - iIII % oOOoOooOo - oO0o / I1ii11iIi11i
   if 4 - 4: ii - ooOoO0O00 % Ii1i1i - IIIi11I1 * I11i
 else :
  if 85 - 85: ii * iI11I1II1I1I . IIIIiiII111 / ii % oOo0O0Ooo % o0o00Oo0O
  if 36 - 36: Ii1i1i / IIiIiII11i / o0O00o / o0O00o + Ii1I
  if oo00 . getSetting ( 'Search' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH[/COLOR]' , str ( iI1iIIiiii ) , 9000 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiiiiIIii + 'Technica-Streams.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Genie On Demand Streams[/COLOR]' , ( i11 ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3NoYWthL0dPRFMucGhw' ) ) , 1016 , iiiiiIIii + 'gods.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , iiiiiIIii + 'Bamf.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Supremacy[/COLOR]' , '' , 1131000 , iiiiiIIii + 'supremacy.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiiiiIIii + 'boss.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']APPRENTICE[/COLOR]' , '' , 1017 , iiiiiIIii + 'appstreams.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MOVIES[/COLOR]' , str ( iI1iIIiiii ) , 4004 , iiiiiIIii + 'Movies.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TV SHOWS[/COLOR]' , str ( iI1iIIiiii ) , 4005 , iiiiiIIii + 'TVShows.png' , iIi1ii1I1 , '' )
  if 95 - 95: o0O00o
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']KIDS[/COLOR]' , str ( iI1iIIiiii ) , 4007 , iiiiiIIii + 'Kids.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']COZY CORNER[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 21999990 , iiiiiIIii + 'zone.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiiiiIIii + 'zone.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FREEVIEW[/COLOR]' , str ( iI1iIIiiii ) , 90023 , iiiiiIIii + 'freeview.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FOOTBALL[/COLOR]' , '' , 10002 , iiiiiIIii + 'Football.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'Fitness' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FITNESS[/COLOR]' , '' , 7084 , iiiiiIIii + 'Fitness.png' , iIi1ii1I1 , '' )
   if 51 - 51: IIiIiII11i + o0O00o . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
   if 72 - 72: ooOO0O0ooOooO + ooOO0O0ooOooO / IIiIiII11i . ii % Ii1i1i
   if 49 - 49: ooOO0O0ooOooO . oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
   if 2 - 2: ii % IIIi11I1
   if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
   if 39 - 39: IIIIiiII111 / IIiIiII11i / Ii1I % oOo0O0Ooo
   if 89 - 89: o0O0Oooo0O + ii + o0O0Oooo0O * ooOoO0O00 + iI11I1II1I1I % iIII
   if 59 - 59: IIIi11I1 + Ii
   if 88 - 88: Ii - oOOoOooOo
   if 67 - 67: IIIi11I1 . I1ii11iIi11i + OOooOOo - ii
   if 70 - 70: IIIi11I1 / IIiIiII11i - iI11I1II1I1I - IIIIiiII111
   if 11 - 11: iI11I1II1I1I . ii . IIiIiII11i / ooOoO0O00 - iIII
   if 30 - 30: OOooOOo
   if 21 - 21: Ii / o0O0Oooo0O % IIIi11I1 * o0o00Oo0O . iIII - iI11I1II1I1I
   if 26 - 26: IIiIiII11i * OOooOOo
   if 10 - 10: IIiIiII11i . IIIIiiII111
   if 32 - 32: Ii1i1i . o0O00o . ii - oO0o + ooOO0O0ooOooO
   if 88 - 88: IIIIiiII111
   if 19 - 19: IIiIiII11i * o0O00o + Ii1i1i
   if 65 - 65: IIIi11I1 . o0O0Oooo0O . oO0o . IIIIiiII111 - IIIi11I1
   if 19 - 19: Ii + IIIIiiII111 % oOOoOooOo
   if 14 - 14: oO0o . IIiIiII11i . iIII / Ii1i1i % Ii1I - oOOoOooOo
   if 67 - 67: iIII - IIIi11I1 . ooOoO0O00
   if 35 - 35: IIIIiiII111 + oOOoOooOo - ooOO0O0ooOooO . IIIIiiII111 . o0O00o
   if 87 - 87: OOooOOo
   if 25 - 25: ooOoO0O00 . oO0o - OOooOOo / oO0o % oO0o * iI11I1II1I1I
   if 50 - 50: oO0o . Ii - ooOO0O0ooOooO . ooOO0O0ooOooO
   if 31 - 31: IIIi11I1 / I1ii11iIi11i * ooOoO0O00 . OOooOOo
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def OO0o0oO ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']FOOTBALL[/COLOR]' , '[COLOR' + II11iiii1Ii + ']KIDS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']NEWS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']HOBBIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DISCLOSE TV[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']CATEGORIES[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  OO0oo ( )
 if OoOOo0OOoO == 1 :
  IiIi1II11i ( )
 if OoOOo0OOoO == 2 :
  II1II1iIIi11 ( )
 if OoOOo0OOoO == 3 :
  IiI1iII1II111 ( )
 if OoOOo0OOoO == 4 :
  IIiI11i1111Ii ( )
 if OoOOo0OOoO == 5 :
  o00O0O ( )
  if 70 - 70: I1ii11iIi11i . OOooOOo
  if 58 - 58: iIII + IIiIiII11i * IIIIiiII111 * Ii - iI11I1II1I1I
def oooo00o0o0o ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']POPCORN BOX[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DESI FLIX[/COLOR]' , '[COLOR' + II11iiii1Ii + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CLASSIC MOVIES[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']MOVIES[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0Oo00oO0O00 ( )
  if OoOOo0OOoO == 1 :
   IiO000O0OO00oo ( )
  if OoOOo0OOoO == 2 :
   oOOO ( Oo0o00OO0000 )
  if OoOOo0OOoO == 3 :
   ooo0oooo0 ( )
  if OoOOo0OOoO == 4 :
   OOO0ooo ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if OoOOo0OOoO == 5 :
   IIiiii ( )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH MOVIES[/COLOR]' , str ( iI1iIIiiii ) , 9001 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TOP RATED MOVIES[/COLOR]' , str ( iI1iIIiiii ) , 10200 , iiiiiIIii + 'rated.png' , iIi1ii1I1 , '' )
  if 37 - 37: I11i % oOOoOooOo
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']POPCORN BOX[/COLOR]' , str ( iI1iIIiiii ) , 7061 , iiiiiIIii + 'PopcornBox.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Desi Flix[/COLOR]' , '' , 80005 , iiiiiIIii + 'Desi.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiiiiIIii + 'FilmTrailers.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiiiiIIii + 'ClassicMovies.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def O0II11i11II ( ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']DAILY LISTS[/COLOR]' , '' , 9007 , o0 , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , o0 , iIi1ii1I1 , '' )
 if 29 - 29: I1ii11iIi11i % oO0o % o0O00o . I11i / ii * oOOoOooOo
 if 54 - 54: o0o00Oo0O
 if 68 - 68: oO0o * I11i . oOOoOooOo % ooOO0O0ooOooO % o0O0Oooo0O
 if 75 - 75: OOooOOo
 if 34 - 34: o0o00Oo0O
def OooOOOo0 ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Dans Scrapes[/COLOR]' , '[COLOR' + II11iiii1Ii + ']THE SOURCE[/COLOR]' , '[COLOR' + II11iiii1Ii + ']WATCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']RETURN DATES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CLASSIC TV[/COLOR]' , '[COLOR' + II11iiii1Ii + ']TV SHOW TRAILERS[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TV SHOWS[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0O0o0o0o ( )
  if OoOOo0OOoO == 1 :
   IIIIIiI ( 'http://www.tvmaze.com/shows' )
  if OoOOo0OOoO == 2 :
   Oo0000O0OOooO ( )
  if OoOOo0OOoO == 3 :
   O00OO ( )
  if OoOOo0OOoO == 4 :
   Oo0 ( )
  if OoOOo0OOoO == 5 :
   i1111IIiii1 ( )
  if OoOOo0OOoO == 6 :
   iIi ( )
  if OoOOo0OOoO == 7 :
   OOOoO ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH SERIES[/COLOR]' , str ( iI1iIIiiii ) , 9002 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
  if 57 - 57: oO0o / ooOoO0O00 . ooOoO0O00
  if 74 - 74: iI11I1II1I1I * o0O00o % OOooOOo
  if 36 - 36: ii - ooOO0O0ooOooO
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Dans Scrapes[/COLOR]' , 'http://www.tvmaze.com/shows' , 9110001 , iiiiiIIii + 'ClassicTV.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiiiiIIii + 'iWatchSeries.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']RETURN DATES[/COLOR]' , str ( iI1iIIiiii ) , 10095 , iiiiiIIii + 'RD.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CLASSIC TV[/COLOR]' , str ( iI1iIIiiii ) , 8064 , iiiiiIIii + 'ClassicTV.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiiiiIIii + 'TVShowTrailers.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def OOo ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   oooOO0OO0O = '[COLOR' + II11iiii1Ii + ']Murrays Mints[/COLOR]'
   if 78 - 78: Ii1i1i / IIiIiII11i % OOooOOo
   if 52 - 52: IIIi11I1 - IIIIiiII111 * ooOO0O0ooOooO
   if 17 - 17: ii + IIIi11I1 * iIII * OOooOOo
   if 36 - 36: o0o00Oo0O + I1ii11iIi11i
  I11ii1IIiIi = [ oooOO0OO0O , '[COLOR' + II11iiii1Ii + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']BAMF TV[/COLOR]' , '[COLOR' + II11iiii1Ii + ']PIRATE MOVIES[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']StreamTeam[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   iIIIi1i1I11i ( )
  if OoOOo0OOoO == 1 :
   oOO0OO0OO ( )
  if OoOOo0OOoO == 2 :
   oOOoooO ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if OoOOo0OOoO == 3 :
   i1ii11 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , ii1i , iiIiii1IIIII )
 else :
  if 5 - 5: ooOO0O0ooOooO . Ii1I . IIiIiII11i . ii
  if 96 - 96: Ii - IIIi11I1 % o0o00Oo0O / oO0o
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Murrays Mints[/COLOR]' , str ( iI1iIIiiii ) , 10025 , iiiiiIIii + 'PandorasBox.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiiiiIIii + 'Technica-Streams.png' , iIi1ii1I1 , '' )
  if 100 - 100: IIIIiiII111 / Ii1i1i - ii % IIiIiII11i - oOo0O0Ooo % OOooOOo
  if 60 - 60: iI11I1II1I1I + ooOoO0O00
  if 86 - 86: iI11I1II1I1I + OOooOOo . Ii - Ii1i1i
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiiiiIIii + 'bamftv.png' , iIi1ii1I1 , '' )
  if 51 - 51: OOooOOo
  if 14 - 14: o0O00o % ooOO0O0ooOooO % I1ii11iIi11i - Ii
  if 53 - 53: Ii1i1i % I1ii11iIi11i
  if 59 - 59: IIIi11I1 % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * o0O00o
  if 41 - 41: Ii1i1i % Ii1I
  if 12 - 12: IIIi11I1
  if 69 - 69: ii + IIIi11I1
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 26 - 26: I1ii11iIi11i + IIIi11I1 / oO0o % OOooOOo % Ii1I + IIiIiII11i
def i11I1I1iiI ( ) :
 OOooOoooOoOo ( )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
def oOOoooO ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 I1Ii = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 I1i1iii1Ii = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for iiIiii1IIIII , iII11 , url in Ii1i1iI1iIIi :
  if '247ch' in url :
   iI ( iiIiii1IIIII , url , 10190 , iII11 )
  elif '.m3u' in url :
   iI ( iiIiii1IIIII , url , 1019 , iII11 )
  elif '.xml' in url :
   iI ( iiIiii1IIIII , url , 1018 , iII11 )
  else :
   O0O00OOo ( iiIiii1IIIII , url , 222 , iII11 )
 for iiIiii1IIIII , url , iII11 in I1Ii :
  if '.xml' in url :
   iI ( iiIiii1IIIII , url , 1018 , iII11 )
  elif '.m3u' in url :
   iI ( iiIiii1IIIII , url , 1019 , iII11 )
  else :
   O0O00OOo ( iiIiii1IIIII , url , 222 , iII11 )
 for iiIiii1IIIII , url , iII11 in I1i1iii1Ii :
  O0O00OOo ( iiIiii1IIIII , url , 8043 , iII11 )
def OoOOo ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'BAMFTV.png' )
def oOO0oo ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iII11 )
  if 29 - 29: oOo0O0Ooo * IIiIiII11i * ii - Ii1I * IIiIiII11i
def oOO0OO0OO ( ) :
 if 41 - 41: o0o00Oo0O
 Iii ( '[COLOR' + II11iiii1Ii + ']All Movies[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' ) ) , 9110013 , iiiiiIIii + 'scraped.png' , iIi1ii1I1 , '' , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']Movies By Genre[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' ) ) , 9110013 , iiiiiIIii + 'scraped.png' , iIi1ii1I1 , '' , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']Movies By A - Z[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ) ) , 9110013 , iiiiiIIii + 'scraped.png' , iIi1ii1I1 , '' , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']Search[/COLOR]' , '' , 9110015 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' , '' )
 if 30 - 30: oOOoOooOo % IIIIiiII111 * IIIi11I1 - Ii1I * Ii1i1i % oOOoOooOo
 if 46 - 46: Ii - o0o00Oo0O . ooOO0O0ooOooO
 if 100 - 100: oOo0O0Ooo / I11i * IIIIiiII111 . o0o00Oo0O / IIIi11I1
 if 83 - 83: o0O0Oooo0O
def ii111Ii11iii ( url ) :
 O0o0O0 = requests . get ( url ) . text
 Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for o00OOoOOO000O0 , oOo0 , II1i11I1 , O0iIiIIIIIii , iiIiIiII , i1I1 , ooo0O0o00O in Ii1i1iI1iIIi :
  if ooo0O0o00O == ' ' :
   ooo0O0o00O = iIi1ii1I1
  if O0iIiIIIIIii == ' ' :
   O0iIiIIIIIii = o0
  iiIiIiII = iiIiIiII . replace ( '\\n' , ' ' )
  if oOo0 == 'Movie Search' :
   Ooo00OoOOO ( o00OOoOOO000O0 , i1I1 , 9110014 , O0iIiIIIIIii , ooo0O0o00O , iiIiIiII , '' )
  elif oOo0 == 'Menu' :
   Iii ( o00OOoOOO000O0 , II1i11I1 , 9110013 , O0iIiIIIIIii , ooo0O0o00O , iiIiIiII , '' )
   if 28 - 28: Ii1I . ooOoO0O00
def iIIi ( name , url ) :
 from imports import Scrape_Nan
 name = str ( name )
 i1I1 = str ( url )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( name , i1I1 , '' )
 if 96 - 96: IIIIiiII111
def i1I11iIII1i1I ( ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search your moive' , type = xbmcgui . INPUT_ALPHANUM )
 iiI11Iii = [ 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ]
 for Oo0o00OO0000 in iiI11Iii :
  O0o0O0 = requests . get ( i11 ( Oo0o00OO0000 ) ) . content
  Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
  for o00OOoOOO000O0 , oOo0 , II1i11I1 , O0iIiIIIIIii , iiIiIiII , i1I1 , ooo0O0o00O in Ii1i1iI1iIIi :
   if ooo0O0o00O == ' ' :
    ooo0O0o00O = iIi1ii1I1
   if O0iIiIIIIIii == ' ' :
    O0iIiIIIIIii = o0
   iiIiIiII = iiIiIiII . replace ( '\\n' , ' ' )
   if oOo0 == 'Movie Search' :
    if oOO0ooIiIIi1I1I11Ii . lower ( ) in o00OOoOOO000O0 . lower ( ) :
     Ooo00OoOOO ( o00OOoOOO000O0 , i1I1 , 9110014 , O0iIiIIIIIii , ooo0O0o00O , iiIiIiII , '' )
def o0OO ( url ) :
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url , oOo0 , iiIiI , ooo0O0o00O , i11II1I11I1 in Ii1i1iI1iIIi :
  if iiIiI == '123' :
   iiIiI = iiiiiIIii + 'appstreams.png'
  if ooo0O0o00O == '123' :
   ooo0O0o00O = iiiiiIIii + 'appstreams.png'
  if 'php' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100010 , iiIiI , ooo0O0o00O , i11II1I11I1 )
  elif 'playlist' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100007 , iiIiI , ooo0O0o00O , i11II1I11I1 )
  elif 'watchseries' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100100 , iiIiI , ooo0O0o00O , i11II1I11I1 )
  elif not 'http' in url :
   Ooo00OoOOO ( iiIiii1IIIII , url , 100009 , iiIiI , ooo0O0o00O , i11II1I11I1 , '' )
  else :
   Ooo00OoOOO ( iiIiii1IIIII , url , 100005 , iiIiI , ooo0O0o00O , i11II1I11I1 , '' )
   if 87 - 87: oOOoOooOo - ii + Ii
def O0oooo0OoO0oo ( url ) :
 oO0000OOo00 = Oo ( url )
 O0oO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
 for url , iII11 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in O0oO0 :
  if iII11 == '123' :
   iII11 = iiiiiIIii + 'appstreams.png'
  if ooo0O0o00O == '123' :
   ooo0O0o00O = iIi1ii1I1
  if 'php' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100004 , iII11 , ooo0O0o00O , i11II1I11I1 )
  elif 'playlist' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100007 , iII11 , ooo0O0o00O , i11II1I11I1 )
  elif 'watchseries' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100100 , iII11 , ooo0O0o00O , i11II1I11I1 )
  elif not 'http' in url :
   Ooo00OoOOO ( iiIiii1IIIII , url , 100009 , iII11 , ooo0O0o00O , i11II1I11I1 , '' )
  else :
   Ooo00OoOOO ( iiIiii1IIIII , url , 100005 , iII11 , ooo0O0o00O , i11II1I11I1 , '' )
   if 16 - 16: oOo0O0Ooo * IIiIiII11i / iI11I1II1I1I - IIIIiiII111
def IiI1IiI11iII ( url ) :
 if 64 - 64: ooOO0O0ooOooO - oOo0O0Ooo / IIIIiiII111 - oO0o
 oO0000OOo00 = Oo ( url )
 ii11I = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Ii1II1I11i1 in ii11I :
  iiIiI = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iiIiI in iiIiI :
   iiIiI = iiIiI
  iiIiii1IIIII = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iiIiii1IIIII in iiIiii1IIIII :
   if 'elete' in iiIiii1IIIII :
    pass
   elif 'rivate Vid' in iiIiii1IIIII :
    pass
   else :
    iiIiii1IIIII = ( iiIiii1IIIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  i1IiIiiiIIIIi = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( Ii1II1I11i1 ) )
  for i1IiIiiiIIIIi in i1IiIiiiIIIIi :
   i1IiIiiiIIIIi = i1IiIiiiIIIIi
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for url in url :
   url = url
  Ooo00OoOOO ( '[COLORred]' + str ( i1IiIiiiIIIIi ) + '[/COLOR] : ' + str ( iiIiii1IIIII ) , str ( url ) , 100009 , str ( iiIiI ) , iIi1ii1I1 , '' , '' )
  OOoOO0o0o0 ( 'movies' , '' )
  if 74 - 74: IIiIiII11i + ooOoO0O00 + Ii1i1i
def Oo00O0ooOO ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search Dans Scrapes' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'http://www.tvmaze.com/search?q=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11ii = IiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( i11ii )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  i11I1 = 'http://www.tvmaze.com' + Oo0o00OO0000 . replace ( '"' , '' )
  Ii1iIi111i1i1 = requests . get ( i11I1 ) . content
  Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
  for i11II1I11I1 in Ii1i1iI1iIIi :
   if not '<div>' in i11II1I11I1 :
    IIOO0ooOo0OoOo0 = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   iII11 = 'http:' + iII11
   iiIiii1IIIII = iiIiii1IIIII . replace ( '&#039;' , '' )
   if iiIiii1IIIII == '' :
    oOo = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( Oo0o00OO0000 ) )
    for iiIiii1IIIII in oOo :
     iiIiii1IIIII = iiIiii1IIIII . replace ( '-' , ' ' )
  Iii ( iiIiii1IIIII , i11I1 , 9110002 , iII11 , iIi1ii1I1 , IIOO0ooOo0OoOo0 , '' )
  if 17 - 17: Ii1i1i . Ii
def IIIIIiI ( url ) :
 iI ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 9110004 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
 O0o0O0 = requests . get ( url ) . content
 Ii1i1iI1iIIi = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( O0o0O0 )
 i1ii1II1ii = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  i11I1 = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . o0O0Oooo0O - oOOoOooOo
  Ii1iIi111i1i1 = requests . get ( i11I1 ) . content
  Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
  for i11II1I11I1 in Ii1i1iI1iIIi :
   if not '<div>' in i11II1I11I1 :
    IIOO0ooOo0OoOo0 = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   iII11 = 'http:' + iII11
   iiIiii1IIIII = iiIiii1IIIII . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if iiIiii1IIIII == '' :
    oOo = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for iiIiii1IIIII in oOo :
     iiIiii1IIIII = iiIiii1IIIII . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  Iii ( iiIiii1IIIII , i11I1 , 9110002 , iII11 , iIi1ii1I1 , IIOO0ooOo0OoOo0 , '' )
  if 63 - 63: ooOO0O0ooOooO
 for o0o0oOoOO0O in i1ii1II1ii :
  url = 'http://www.tvmaze.com' + o0o0oOoOO0O
  Iii ( 'NEXT' , url , 9110001 , iII11 , iIi1ii1I1 , '' , '' )
def Oo0OOo0Oo0OOo0 ( url ) :
 O0o0O0 = requests . get ( url ) . content
 Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( O0o0O0 )
 for i11II1I11I1 in Ii1i1iI1iIIi :
  IIOO0ooOo0OoOo0 = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
 return IIOO0ooOo0OoOo0
def i1i11I ( url , name , iconimage ) :
 o00OOoOOO000O0 = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 iII11 = iconimage
 O0o0O0 = requests . get ( url + '/episodes' ) . content
 Ii1iIi111i1i1 = requests . get ( url ) . content
 Ii1II1I11i1 = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
 for iiIiIi1 in Ii1i1iI1iIIi :
  iiIiIi1 = iiIiIi1 . replace ( ' ' , '' )
 for oOOOOOOOoO , ii1III11 in Ii1II1I11i1 :
  if not 'special' in oOOOOOOOoO . lower ( ) :
   oOOOOOOOoO = oOOOOOOOoO . replace ( 'S' , '' ) . replace ( 's' , '' )
  I1 = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( ii1III11 ) )
  for IIiI , O0oOOo0o , I1III11iiii11i1 in I1 :
   if not 'special' in IIiI . lower ( ) :
    Iii ( o00OOoOOO000O0 + ' - SEASON -' + oOOOOOOOoO + '- EPISODE-' + IIiI + '-' + iiIiIi1 , '' , 9110003 , iII11 , iIi1ii1I1 , '' , o00OOoOOO000O0 )
    if 54 - 54: ooOoO0O00 - ooOO0O0ooOooO
    if 18 - 18: iI11I1II1I1I + I1ii11iIi11i - IIIi11I1 + ii * ii
    if 41 - 41: oOOoOooOo . I1ii11iIi11i + oOo0O0Ooo
def o0O0OO ( name , extra ) :
 if 22 - 22: IIiIiII11i * oO0o * iIII + Ii1I * I11i
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Checking for stream' )
 from imports import Scrape_Nan
 oo0o0 = name + '<>'
 oO0ooOoO = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( oo0o0 ) )
 for o00OOoOOO000O0 , ooO0000o00O , O0Ooo , iiIiIi1 in oO0ooOoO :
  o00OOoOOO000O0 = o00OOoOOO000O0
  ooO0000o00O = ooO0000o00O
  O0Ooo = O0Ooo
  oO00oOOo0Oo = ''
  Scrape_Nan . scrape_episode ( o00OOoOOO000O0 , iiIiIi1 , '' , ooO0000o00O , O0Ooo , '' )
if 5 - 5: I11i . o0o00Oo0O / I1ii11iIi11i % oO0o
if 60 - 60: IIiIiII11i / iI11I1II1I1I + Ii1I . Ii
if 40 - 40: I11i
if 78 - 78: iI11I1II1I1I
if 56 - 56: ii - iIII - ooOoO0O00
if 8 - 8: o0O0Oooo0O / IIIi11I1 . oOo0O0Ooo + Ii1I / Ii
if 31 - 31: oOOoOooOo - iI11I1II1I1I + IIIIiiII111 . I1ii11iIi11i / o0O00o % iI11I1II1I1I
if 6 - 6: o0O00o * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
if 53 - 53: iIII + iI11I1II1I1I
if 70 - 70: Ii1I
if 67 - 67: ii
def IiIiIi1I1 ( ) :
 Iii ( 'Featured 24/7' , '' , 9070000 , iiiiiIIii + 'arconai/feat.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Tv Thows' , '' , 9080000 , iiiiiIIii + 'arconai/247shows.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Movies' , '' , 9090000 , iiiiiIIii + 'arconai/247movies.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Cable' , '' , 9100000 , iiiiiIIii + 'arconai/247cable.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Random Stream' , '' , 9110000 , iiiiiIIii + 'arconai/random.png' , iIi1ii1I1 , '' , '' )
 if 2 - 2: ooOoO0O00 - oOOoOooOo + oOo0O0Ooo . I11i * I11i / OOooOOo
def oOOOiIi1I1 ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 O0oOoo0OoO0O = 'index.php#shows'
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + O0oOoo0OoO0O ) . content )
 oo00IiI1 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for oOo00o00oO in oo00IiI1 :
  o0000 = oOo00o00oO . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I1I1IiI1 in o0000 :
   i111i1i = I1I1IiI1 . text
  IiIii1I1I = oOo00o00oO . findAll ( 'a' )
  for I1I1IiI1 in IiIii1I1I :
   if I1I1IiI1 . has_key ( 'href' ) :
    OO0Oooo0oo = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   I1i111IiIiIi1 = { 'User-Agent' : random_agent ( ) }
   i1II11II1 = requests . get ( OO0Oooo0oo , headers = I1i111IiIiIi1 ) . content
   II1IIIii = packets ( i1II11II1 )
   if 40 - 40: OOooOOo % oO0o
   Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( II1IIIii )
   for oo0O0o00 in Ii1i1iI1iIIi :
    oo0O0o00 = oo0O0o00 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    oOoO0o = 'https:' + oo0O0o00 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ooo00OoOOO ( iiIiii1IIIII , oOoO0o , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
    if 46 - 46: o0O0Oooo0O % Ii1i1i
    if 72 - 72: iI11I1II1I1I
def iI1I1II1 ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 O0oOoo0OoO0O = 'index.php#movies'
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + O0oOoo0OoO0O ) . content )
 oo00IiI1 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for oOo00o00oO in oo00IiI1 :
  o0000 = oOo00o00oO . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I1I1IiI1 in o0000 :
   i111i1i = I1I1IiI1 . text
  IiIii1I1I = oOo00o00oO . findAll ( 'a' )
  for I1I1IiI1 in IiIii1I1I :
   if I1I1IiI1 . has_key ( 'href' ) :
    OO0Oooo0oo = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   I1i111IiIiIi1 = { 'User-Agent' : random_agent ( ) }
   i1II11II1 = requests . get ( OO0Oooo0oo , headers = I1i111IiIiIi1 ) . content
   II1IIIii = packets ( i1II11II1 )
   if 92 - 92: ii - ii * oO0o % oOo0O0Ooo
   Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( II1IIIii )
   for oo0O0o00 in Ii1i1iI1iIIi :
    oo0O0o00 = oo0O0o00 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    oOoO0o = 'https:' + oo0O0o00 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ooo00OoOOO ( iiIiii1IIIII , oOoO0o , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
    if 77 - 77: iI11I1II1I1I - ooOoO0O00 . ooOO0O0ooOooO
    if 26 - 26: I11i * o0O00o . ooOoO0O00
def ooOoOO ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 O0oOoo0OoO0O = 'index.php#cable'
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + O0oOoo0OoO0O ) . content )
 oo00IiI1 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for oOo00o00oO in oo00IiI1 :
  o0000 = oOo00o00oO . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I1I1IiI1 in o0000 :
   i111i1i = I1I1IiI1 . text
  IiIii1I1I = oOo00o00oO . findAll ( 'a' )
  for I1I1IiI1 in IiIii1I1I :
   if I1I1IiI1 . has_key ( 'href' ) :
    OO0Oooo0oo = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   I1i111IiIiIi1 = { 'User-Agent' : random_agent ( ) }
   i1II11II1 = requests . get ( OO0Oooo0oo , headers = I1i111IiIiIi1 ) . content
   II1IIIii = packets ( i1II11II1 )
   if 56 - 56: iI11I1II1I1I . Ii - IIIi11I1 * IIiIiII11i * o0O0Oooo0O
   Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( II1IIIii )
   for oo0O0o00 in Ii1i1iI1iIIi :
    oo0O0o00 = oo0O0o00 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    oOoO0o = 'https:' + oo0O0o00 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ooo00OoOOO ( iiIiii1IIIII , oOoO0o , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
    if 5 - 5: IIIi11I1 / IIIi11I1 - Ii1I
def oO0ooOO ( ) :
 Ii1iIi111i1i1 = 'http://arconaitv.me/stream.php?id=random'
 I1i111IiIiIi1 = { 'User-Agent' : random_agent ( ) }
 i1II11II1 = requests . get ( Ii1iIi111i1i1 , headers = I1i111IiIiIi1 ) . content
 II1IIIii = packets ( i1II11II1 )
 if 7 - 7: IIiIiII11i - IIIi11I1 . IIiIiII11i
 Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( II1IIIii )
 for oo0O0o00 in Ii1i1iI1iIIi :
  oo0O0o00 = oo0O0o00 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  oOoO0o = 'https:' + oo0O0o00 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  Ooo00OoOOO ( 'Random Pick' , oOoO0o , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
  if 53 - 53: ooOO0O0ooOooO % iIII . oOOoOooOo - OOooOOo
def OoOoO0OoOOOOo ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 O0oOoo0OoO0O = 'index.php#shows'
 if 61 - 61: Ii * ooOO0O0ooOooO . IIIIiiII111 . oOOoOooOo % oO0o
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + O0oOoo0OoO0O ) . content )
 oo00IiI1 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for oOo00o00oO in oo00IiI1 :
  o0000 = oOo00o00oO . findAll ( 'a' )
  for I1I1IiI1 in o0000 :
   if I1I1IiI1 . has_key ( 'href' ) :
    OO0Oooo0oo = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   Iiii1iIii = I1I1IiI1 . findAll ( 'img' )
   for oOoooO000O in Iiii1iIii :
    iII11 = Oo0o00OO0000 + oOoooO000O [ 'src' ]
    I1i111IiIiIi1 = { 'User-Agent' : random_agent ( ) }
    i1II11II1 = requests . get ( OO0Oooo0oo , headers = I1i111IiIiIi1 ) . content
    II1IIIii = packets ( i1II11II1 )
    if 49 - 49: I11i * Ii1i1i + iIII + IIIIiiII111
    Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( II1IIIii )
    for oo0O0o00 in Ii1i1iI1iIIi :
     oo0O0o00 = oo0O0o00 . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     oOoO0o = 'https:' + oo0O0o00 + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     Ooo00OoOOO ( iiIiii1IIIII , oOoO0o , 9060000 , iII11 , iII11 , '' , '' )
     if 30 - 30: I11i / IIIi11I1 / o0O00o % oOOoOooOo + IIiIiII11i
def I1III111i ( name , url ) :
 import urlresolver
 try :
  iiI1iii = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiI1iii , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 79 - 79: oO0o * OOooOOo . ii - iIII * I11i
 if 78 - 78: o0O00o
def Oo0O0Oo00O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
 for url , iII11 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in O0oO0 :
  if '.php' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100210 , iII11 , ooo0O0o00O , i11II1I11I1 )
  else :
   oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , ooo0O0o00O , i11II1I11I1 )
   if 9 - 9: I11i . oOo0O0Ooo - Ii1I
   if 32 - 32: ii / oOo0O0Ooo / iI11I1II1I1I + IIiIiII11i . ooOO0O0ooOooO . I11i
   if 21 - 21: iI11I1II1I1I / IIiIiII11i % ooOoO0O00
def IIiI1i ( iconimage , url , extra ) :
 iiIiI = ' '
 iII1 = ' '
 ooo0O0o00O = ' '
 ooO0000o00O = ' '
 O000O = Oo ( url )
 iiIiI = re . compile ( '<img src="(.+?)">' ) . findall ( O000O )
 for iiIiI in iiIiI :
  iiIiI = iiIiI
 Oo00OO0 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( O000O )
 for ooo0O0o00O in Oo00OO0 :
  ooo0O0o00O = ooo0O0o00O
 Ii1i1iI1iIIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( O000O )
 for url , ooO0000o00O in Ii1i1iI1iIIi :
  ooO0000o00O = 'S' + ( ooO0000o00O ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = Ii1iIiII1ii1 + url
  Iii ( ( ooO0000o00O ) . replace ( '  ' , '' ) , url , 100101 , iiIiI , ooo0O0o00O , iII1 , '' )
  OOoOO0o0o0 ( 'Movies' , 'info' )
  if 72 - 72: ooOoO0O00 / ooOO0O0ooOooO * o0O0Oooo0O
def I11IiIIIi ( url , name , fanart , extra , iconimage ) :
 Oo0o0OOOOO0O = extra
 ooO0000o00O = name
 O000O = Oo ( url )
 iiIiI = iconimage
 Ii1i1iI1iIIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( O000O )
 for url , name , I1I1IiIi1 in Ii1i1iI1iIIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = Ii1iIiII1ii1 + url
  I1I1IiIi1 = I1I1IiIi1
  oOO0o0oo0 = name + ' - [COLORred]' + I1I1IiIi1 + '[/COLOR]'
  Iii ( oOO0o0oo0 , url , 100102 , iiIiI , fanart , 'Aired : ' + I1I1IiIi1 , oOO0o0oo0 )
  if 78 - 78: IIIi11I1 + IIIIiiII111 . o0O00o
def OoIIi1iI ( name , URL , iconimage , fanart ) :
 oO0000OOo00 = Oo ( URL )
 Ii1i1iI1iIIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , name in Ii1i1iI1iIIi :
  for IIi1IIIi in ooOooo000oOO :
   if IIi1IIIi in Oo0o00OO0000 :
    URL = 'http://www.watchseriesgo.to/link/' + Oo0o00OO0000
    Ooo00OoOOO ( name , URL , 100106 , iiiiiIIii + 'appstreams.png' , iIi1ii1I1 , '' , '' )
 if len ( Ii1i1iI1iIIi ) <= 0 :
  Iii ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 92 - 92: oO0o * oOOoOooOo
  if 35 - 35: Ii
def ooO ( url , name ) :
 o0O00o0OoO = name
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0000OOo00 )
 I1i1iii1Ii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  IIiI11i11 ( url , o0O00o0OoO )
 for url in I1Ii :
  IIiI11i11 ( url , o0O00o0OoO )
 for url in I1i1iii1Ii :
  IIiI11i11 ( url , o0O00o0OoO )
  if 14 - 14: Ii
def IIiI11i11 ( url , season_name ) :
 if 'daclips.in' in url :
  o0oOOO0 ( url , season_name )
 elif 'filehoot.com' in url :
  oOOOiI1iIIII1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  OO0I11Ii1iI11iI1 ( url , season_name )
 elif 'vidspot.net' in url :
  i1III1 ( url , season_name )
 elif 'vodlocker' in url :
  Iii111IiIii ( url , season_name )
 elif 'vidto' in url :
  OooO0ooo0 ( url , season_name )
  if 2 - 2: ii
  if 60 - 60: oO0o
def OooO0ooo0 ( url , season_name ) :
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
  oO00Ooo0oO ( oOoooooOoO , season_name )
  if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % Ii1i1i - iI11I1II1I1I
  if 17 - 17: iIII / I11i % I1ii11iIi11i
def OO0I11Ii1iI11iI1 ( url , season_name ) :
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
  oO00Ooo0oO ( oOoooooOoO , season_name )
  if 71 - 71: o0O00o . o0O0Oooo0O . oO0o
def i1III1 ( url , season_name ) :
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0000OOo00 )
 for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
  oO00Ooo0oO ( oOoooooOoO , season_name )
  if 68 - 68: Ii % ooOO0O0ooOooO * oO0o * o0O00o * IIiIiII11i + o0o00Oo0O
def Iii111IiIii ( url , season_name ) :
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO in Ii1i1iI1iIIi :
  oO00Ooo0oO ( oOoooooOoO , season_name )
  if 66 - 66: iIII % Ii1I % ii
def o0oOOO0 ( url , season_name ) :
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0000OOo00 )
 for oOoooooOoO in Ii1i1iI1iIIi :
  oO00Ooo0oO ( oOoooooOoO , season_name )
  if 34 - 34: I11i / IIIIiiII111 % o0o00Oo0O . oO0o . ooOoO0O00
def oOOOiI1iIIII1 ( url , season_name ) :
 oO0000OOo00 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO in Ii1i1iI1iIIi :
  oO00Ooo0oO ( oOoooooOoO , season_name )
  if 29 - 29: o0o00Oo0O . o0O0Oooo0O
def oO00Ooo0oO ( Link , season_name ) :
 if 'http:/' in Link :
  OO0o0oO0O000o ( Link )
  if 47 - 47: o0O0Oooo0O - oO0o / Ii1i1i * ii / Ii1i1i . I1ii11iIi11i
  if 34 - 34: oOOoOooOo
def i1IiIi1 ( url ) :
 oO0000OOo00 = OPEN_URL_1 ( url )
 I1iiIiI1iI1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0000OOo00 )
 for url in I1iiIiI1iI1I :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 27 - 27: Ii1I * o0O0Oooo0O - oO0o + Ii1i1i * Ii1i1i
def Iii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = True )
 return iIiiIi11IIi
 if 31 - 31: oO0o * Ii * Ii1i1i . Ii
 if 12 - 12: OOooOOo % o0O00o % Ii1I . Ii * iI11I1II1I1I
def Ooo00OoOOO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oo0oooo0OoO0o = [ ]
  oo0oooo0OoO0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  Oo0oO . addContextMenuItems ( oo0oooo0OoO0o )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = False )
 return iIiiIi11IIi
 if 50 - 50: IIIIiiII111 / IIIIiiII111 + IIIi11I1 * oOOoOooOo / Ii1I
def I1IIiiI1II1 ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 5 - 5: IIIIiiII111
def OOiI1 ( url ) :
 I1iIII1IiiI = xbmc . Player ( OOoooOoO0Oo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1iIII1IiiI . play ( url ) . strip ( )
 except : pass
 if 78 - 78: ii / IIIi11I1 % OOooOOo * ii
def OO0o0oO0O000o ( url ) :
 I1iIII1IiiI = xbmc . Player ( )
 import urlresolver
 try : I1iIII1IiiI . play ( url )
 except : pass
 if 68 - 68: ooOO0O0ooOooO
def Oo ( url ) :
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oooooOoo0ooo = ''
 I1I1IiI1 = ''
 try :
  oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
  I1I1IiI1 = oooooOoo0ooo . read ( )
  oooooOoo0ooo . close ( )
 except : pass
 if I1I1IiI1 != '' :
  return I1I1IiI1
 else :
  I1I1IiI1 = 'Opened'
  return I1I1IiI1
  if 29 - 29: IIIIiiII111 + Ii % iIII
  if 93 - 93: OOooOOo % iI11I1II1I1I
  if 90 - 90: oOo0O0Ooo - IIIi11I1 / Ii1i1i / o0o00Oo0O / iIII
def IiIi1II11i ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']CARTOONS[/COLOR]' ]
  if 87 - 87: OOooOOo / o0O00o + iI11I1II1I1I
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Kids[/COLOR]' , I11ii1IIiIi )
  if 93 - 93: iI11I1II1I1I + ooOO0O0ooOooO % oOOoOooOo
  if 21 - 21: IIIi11I1
  if 6 - 6: o0O00o
  if 46 - 46: o0O00o + ooOO0O0ooOooO
  if OoOOo0OOoO == 0 :
   Oo00o0O0O ( )
   if 84 - 84: iIII % ooOoO0O00
   if 33 - 33: Ii1I * Ii1I . oOOoOooOo . Ii
   if 48 - 48: I11i . Ii1i1i + OOooOOo % Ii1I / Ii
   if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + o0O00o % Ii % OOooOOo
 else :
  if 78 - 78: Ii1i1i + OOooOOo + o0O00o - o0O00o . Ii / oO0o
  if 27 - 27: Ii1i1i - o0o00Oo0O % iIII * o0O0Oooo0O . o0O00o % iI11I1II1I1I
  if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % oOOoOooOo
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CARTOONS[/COLOR]' , '' , 10001 , iiiiiIIii + 'Cartoons.png' , iIi1ii1I1 , '' )
   if 24 - 24: OOooOOo
   if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + IIIi11I1
   if 28 - 28: oOo0O0Ooo
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def IiI1iII1II111 ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FOOTBALL[/COLOR]' , '' , 10002 , iiiiiIIii + 'Football.png' , iIi1ii1I1 , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iiiiiIIii + 'Fitness.png' , iIi1ii1I1 , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Go Fishing[/COLOR]' , str ( iI1iIIiiii ) , 8090 , iiiiiIIii + 'GoFishing.png' , iIi1ii1I1 , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , iiiiiIIii + 'GenieTVKitchen.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 49 - 49: iIII . I11i % ooOO0O0ooOooO / Ii1i1i
 if 95 - 95: o0o00Oo0O * OOooOOo * o0O00o . oOOoOooOo / iI11I1II1I1I
 if 28 - 28: o0O00o + ooOO0O0ooOooO - oOOoOooOo / iI11I1II1I1I - oOo0O0Ooo
def I1i1Iiiii ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 Ii1i1iI1iIIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0000OOo00 )
 for o0OOOO00O0Oo in Ii1i1iI1iIIi :
  o0OOOO00O0Oo = ( str ( o0OOOO00O0Oo ) )
  if os . path . exists ( xbmc . translatePath ( o0OOOO00O0Oo ) ) :
   Ii1i1 = ( o0OOOO00O0Oo ) . replace ( 'special://home/addons/' , '' )
   I1iI1ii1II ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + Ii1i1 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   OoOOo0OOoO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if OoOOo0OOoO == 0 :
    oOoO00 ( o0OOOO00O0Oo )
    OoOOoooOO0O ( )
   elif OoOOo0OOoO == 1 :
    i1ii1iIIi11i111I ( o0OOOO00O0Oo )
  else :
   pass
   if 16 - 16: oOo0O0Ooo . iI11I1II1I1I
def i1ii1iIIi11i111I ( addon ) :
 Ii1i1 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 27 - 27: Ii - oOo0O0Ooo
def oOoO00 ( addon ) :
 O0OoO000O0OO . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 iii1IIiI = os . path . join ( oOoOooOo0o0 , 'default.py' )
 i1i1Ii11Ii = open ( iii1IIiI , "w+" )
 if 57 - 57: IIIi11I1 + o0O0Oooo0O % Ii1I . oO0o / oO0o * o0o00Oo0O
 i1i1Ii11Ii . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 i1i1Ii11Ii . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 i1i1Ii11Ii . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 6 - 6: ooOoO0O00 - IIiIiII11i * I11i . oO0o
 if 68 - 68: I11i
 if 20 - 20: o0O0Oooo0O - o0O0Oooo0O
 if 37 - 37: o0O00o
def iI11i ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 o0o00O0oOooO0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1i1iI1iIIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1iiIIIi11 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1i1iii1Ii = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 o0oO0OO00ooOO = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 IiIIiii11II1 = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url , iiii1i1II1 , ooo0O0o00O , i11II1I11I1 in o0o00O0oOooO0 :
  if 'php' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iiii1i1II1 , ooo0O0o00O , i11II1I11I1 )
  elif iiIiii1IIIII == 'Search' :
   OoOOoOooooOOo ( 'Search' , url , 90038 , iiii1i1II1 , ooo0O0o00O , i11II1I11I1 )
  else :
   oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iiii1i1II1 , ooo0O0o00O , i11II1I11I1 )
 for iiIiii1IIIII , iII11 , url , ooOO0ooo0o in I1iiIIIi11 :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iII11 , ooOO0ooo0o , '' )
 for iiIiii1IIIII , iII11 , url , ooOO0ooo0o in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iII11 , ooOO0ooo0o , '' )
 for iiIiii1IIIII , url , iII11 , ooOO0ooo0o in I1Ii :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , ooOO0ooo0o , '' )
 for iiIiii1IIIII , url , iII11 , ooOO0ooo0o in I1i1iii1Ii :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , ooOO0ooo0o , '' )
 for iiIiii1IIIII , url , iII11 , ooOO0ooo0o in o0oO0OO00ooOO :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , ooOO0ooo0o , '' )
 for iiIiii1IIIII , url , iII11 in IiIIiii11II1 :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , '' , '' )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
def i1IiI1I ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , iII11 , url , ooOO0ooo0o in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iII11 , ooOO0ooo0o , '' )
 for iiIiii1IIIII , url , iII11 , ooOO0ooo0o in I1Ii :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , ooOO0ooo0o , '' )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
  if 77 - 77: Ii1i1i . I11i
def Oo00oO0oOO ( ) :
 iiiii1I1III1 = [ 'serialsearch' , 'moviesearch' ]
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 if i11ii == '' :
  pass
 else :
  for i1oO00O in iiiii1I1III1 :
   oo0o0ooooo = Oo0o0000o0o0 + i1oO00O + '.php'
   O000O = i11oO0oOo0 ( oo0o0ooooo )
   if O000O != 'Opened' :
    O0oO0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( O000O )
    for iiIiii1IIIII , Oo0o00OO0000 , iiii1i1II1 , ooo0O0o00O , i11II1I11I1 in O0oO0 :
     if i11ii in iiIiii1IIIII . lower ( ) :
      O0o0O = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
      for IIi1IIIi in O0o0O :
       if IIi1IIIi == Oo0o00OO0000 :
        iiIiii1IIIII = '[COLORred]* [/COLOR]' + ( iiIiii1IIIII ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        ii111 = open ( Oo0oOOo , "a" )
        ii111 . write ( 'item="' + iiIiii1IIIII + '"\n' )
        ii111 . close
      if 'php' in Oo0o00OO0000 :
       OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , 90037 , iiii1i1II1 , ooo0O0o00O , i11II1I11I1 )
      else :
       oOOOoo0O0oO ( iiIiii1IIIII , Oo0o00OO0000 , 222 , iiii1i1II1 , ooo0O0o00O , i11II1I11I1 )
       if 93 - 93: ii * I1ii11iIi11i
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
   if 10 - 10: o0O0Oooo0O * ii + iIII - Ii1I / Ii1I . Ii
def i1I1i ( ) :
 if 22 - 22: I1ii11iIi11i % oO0o - ii * I1ii11iIi11i
 if 38 - 38: iI11I1II1I1I / oOOoOooOo
 if 13 - 13: iI11I1II1I1I
 if 77 - 77: Ii - iI11I1II1I1I / ooOO0O0ooOooO / oOOoOooOo / oO0o
 if 56 - 56: ii * o0o00Oo0O
 if 85 - 85: ii % OOooOOo * iI11I1II1I1I
 if 44 - 44: iI11I1II1I1I . Ii1I + o0O0Oooo0O . oOOoOooOo
 if 7 - 7: Ii1I + iI11I1II1I1I * iIII * iIII / IIiIiII11i - Ii1i1i
 if 65 - 65: ooOO0O0ooOooO + OOooOOo + IIiIiII11i
 if 77 - 77: IIiIiII11i
 if 50 - 50: o0o00Oo0O . o0o00Oo0O . oOOoOooOo % I1ii11iIi11i
 if 68 - 68: ooOO0O0ooOooO
 if 10 - 10: Ii1i1i
 if 77 - 77: IIIi11I1 / IIiIiII11i + o0O00o + oOOoOooOo - Ii
 if 44 - 44: oOo0O0Ooo + OOooOOo + Ii1I . oOo0O0Ooo * OOooOOo % iI11I1II1I1I
 if 72 - 72: IIIi11I1 . IIIi11I1 - Ii1I
 if 48 - 48: I1ii11iIi11i - oOOoOooOo + I1ii11iIi11i - oOo0O0Ooo * Ii . IIIIiiII111
 if 35 - 35: o0O00o . o0o00Oo0O + I1ii11iIi11i + IIIi11I1 + ooOoO0O00
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
 if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
 if 58 - 58: IIIi11I1 . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
 O0o0O0 = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 Ii1iIi111i1i1 = requests . get ( 'http://www.djing.com/' ) . content
 I1Ii = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
 oo00IiI1 = O0o0O0 . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for oOo00o00oO in oo00IiI1 :
  o0000 = oOo00o00oO . findAll ( 'a' )
  for I1I1IiI1 in o0000 :
   if I1I1IiI1 . has_attr ( 'href' ) :
    OO0Oooo0oo = 'https://tvcatchup.com' + I1I1IiI1 [ 'href' ]
   Iiii1iIii = I1I1IiI1 . findAll ( 'img' )
   for oOoooO000O in Iiii1iIii :
    iII11 = oOoooO000O [ 'src' ]
    I1Iii1Ii1i1 = oOoooO000O [ 'alt' ]
   Ii1i1iI1iIIi = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( I1I1IiI1 ) )
   for i1iIi1IIiIII1 in Ii1i1iI1iIIi :
    O0O00OOo ( ( '[COLORgold]' + I1Iii1Ii1i1 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + i1iIi1IIiIII1 + '[/COLOR]' ) , OO0Oooo0oo , 90024 , iII11 )
    if 19 - 19: iIII
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in I1Ii :
  if 'Submit' in iiIiii1IIIII :
   pass
  elif '&lt;' in iiIiii1IIIII :
   pass
  else :
   oOOOoo0O0oO ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 90025 , 'http://www.djing.com' + iII11 , iIi1ii1I1 , '' )
   if 87 - 87: oOOoOooOo / OOooOOo % I11i * ooOO0O0ooOooO
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def oOOOoo0o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 if 44 - 44: o0o00Oo0O % ooOoO0O00
 Ii1i1iI1iIIi = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( html )
 for IiIIiii1I in Ii1i1iI1iIIi :
  if not 'text' in IiIIiii1I :
   ooooo0Oo0 = i11 ( i11 ( IiIIiii1I ) )
   O0i1iI ( ooooo0Oo0 )
def o0I1IIIi11ii11 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O0o0oo0oOO0oO ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 15 - 15: oO0o * IIiIiII11i
def o0oO00 ( ) :
 oO0000OOo00 = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 O00o0O = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for O00oOo0O0o00O , ooo0oo00O00Oo , OOO000000OOO0 in O00o0O :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + O00oOo0O0o00O + ooo0oo00O00Oo + OOO000000OOO0 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + Oo0o00OO0000 , 10201 , iiiiiIIii + 'rated.png' )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'yr' in Oo0o00OO0000 :
   iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + Oo0o00OO0000 , 10201 , iiiiiIIii + 'rated.png' )
   if 74 - 74: o0o00Oo0O . ooOO0O0ooOooO - Ii1i1i
def IiO000O0OO00oo ( ) :
 if 14 - 14: oOo0O0Ooo - ii . I11i
 if 97 - 97: IIIIiiII111 % Ii1i1i % OOooOOo / IIiIiII11i % IIIi11I1
 if 83 - 83: oO0o / o0O00o / o0O00o * o0O0Oooo0O / o0O0Oooo0O
 if 65 - 65: oOOoOooOo * iIII / oO0o / oO0o
 if 27 - 27: I1ii11iIi11i
 if 95 - 95: iIII
 oO0000OOo00 = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'yr' in Oo0o00OO0000 :
   Iii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + Oo0o00OO0000 , 10201 , iiiiiIIii + 'rated.png' , '' , iiIiii1IIIII , '' )
   if 44 - 44: IIIi11I1 + iIII . o0O00o / IIiIiII11i % iI11I1II1I1I + o0O00o
def O0OOo ( name , url , description ) :
 IIOO0ooOo0OoOo0 = description
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0000OOo00 )
 for i1I1Iiii1 , url , name in Ii1i1iI1iIIi :
  if 'id' in url :
   O0ooooo000 = name
   Iii ( ( '[COLORred]RANK [COLORblue]' + i1I1Iiii1 + '[COLORred] - [COLORblue]' + name + '[/COLOR]' ) , name , 9110005 , iiiiiIIii + 'rated.png' , '' , IIOO0ooOo0OoOo0 , O0ooooo000 )
   if 97 - 97: Ii % ooOO0O0ooOooO / I1ii11iIi11i / I1ii11iIi11i
   if 97 - 97: IIiIiII11i - o0O0Oooo0O - iI11I1II1I1I * oOo0O0Ooo
def ooo ( description , url ) :
 if 88 - 88: o0O0Oooo0O % o0O00o / Ii1i1i - oOo0O0Ooo / oOo0O0Ooo * oOOoOooOo
 i1I1 = ( str ( description ) )
 o00OOoOOO000O0 = ( str ( url ) )
 xbmc . log ( 'title:' + o00OOoOOO000O0 + '# year:' + i1I1 , xbmc . LOGNOTICE )
 from imports import Scrape_Nan
 Scrape_Nan . scrape_movie ( o00OOoOOO000O0 , i1I1 , '' )
 if 77 - 77: o0O00o
 if 66 - 66: iI11I1II1I1I . Ii / iIII / oOOoOooOo + o0O0Oooo0O
 if 5 - 5: OOooOOo % IIIIiiII111 + o0O00o
 if 13 - 13: o0O00o
 if 19 - 19: IIiIiII11i - o0O00o
 if 59 - 59: I11i * oO0o - Ii1i1i . IIIi11I1
 if 89 - 89: IIIi11I1
def o00oo0OO0 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oO0o000OooOoo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOO0ooIiIIi1I1I11Ii = ( url )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 IIi11i = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oo0OoOO0o0o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OO0OOO00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 ooOOo0o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiI1Iii1 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOO0ooIiIIi1I1I11Ii
 Ooooo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIiiiIiIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 19 - 19: o0O00o . Ii1I / OOooOOo
 O00oo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 OoOoooO000OO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 62 - 62: IIIi11I1 + I1ii11iIi11i % iI11I1II1I1I / iI11I1II1I1I . oOOoOooOo . o0O00o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0000OOo00 = O0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 iiIi1IIiIi = O0 ( i11I1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 oOO00Oo = O0 ( IIi11i )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 i1iIIIi1i = O0 ( oo0OoOO0o0o )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 III1iiIIi = O0 ( OO0OOO00 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1I1IiI1ii = O0 ( IiI1Iii1 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O00OOoOOOO00O = O0 ( Ooooo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 Ooo0OOO = O0 ( iIiiiIiIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 94 - 94: Ii % ii / oOo0O0Ooo
 if 24 - 24: oOo0O0Ooo * ooOO0O0ooOooO
 Oo0O0000Oo00o = O0 ( O00oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 II1 = O0 ( OoOoooO000OO )
 if 31 - 31: Ii . o0O00o
 if 36 - 36: IIIIiiII111
 if 90 - 90: o0o00Oo0O
 if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + o0O00o
 if 27 - 27: IIIi11I1
 if 52 - 52: o0O0Oooo0O % OOooOOo + iI11I1II1I1I * ooOO0O0ooOooO . Ii1i1i
 if 95 - 95: iI11I1II1I1I . o0O00o - ii * oO0o / I11i
 if 74 - 74: ooOO0O0ooOooO
 if 34 - 34: IIIIiiII111
 if 44 - 44: ooOoO0O00 % oOo0O0Ooo % I11i
 if 9 - 9: I1ii11iIi11i % ii - Ii1i1i
 if 43 - 43: oO0o % oO0o
 if 46 - 46: I1ii11iIi11i % iI11I1II1I1I . IIIIiiII111 . o0o00Oo0O * oOOoOooOo / ii
 if Ooo0OOO != 'Failed' :
  II1iI1IIi = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Ooo0OOO )
  for url , iiIiii1IIIII in II1iI1IIi :
   Ii11iiI1 = O0 ( url )
   oO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii11iiI1 )
   for OOoooO00o0o , I1ii1Ii1 in oO0O :
    I1ii1Ii1 = ( I1ii1Ii1 . replace ( '.' , ' ' ) )
    if i11ii in I1ii1Ii1 . lower ( ) :
     if '.mkv' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + OOoooO00o0o , 222 , '' , '' , '' )
     elif '.mp4' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + OOoooO00o0o , 222 , '' , '' , '' )
     elif '.avi' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + OOoooO00o0o , 222 , '' , '' , '' )
     elif '.wav' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + OOoooO00o0o , 222 , '' , '' , '' )
     else :
      OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']*' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + OOoooO00o0o , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 73 - 73: o0o00Oo0O . ooOO0O0ooOooO + Ii + iI11I1II1I1I - iIII / OOooOOo
      OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiIi1IIiIi )
  for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in I1Ii :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 99 - 99: Ii1I * ooOO0O0ooOooO * Ii1I - IIiIiII11i + Ii1i1i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 72 - 72: I11i % oOo0O0Ooo / IIIIiiII111 - o0o00Oo0O + iIII
 if oOO00Oo != 'Failed' :
  I1i1iii1Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOO00Oo )
  for o0iIIIIi , iiIiii1IIIII in I1i1iii1Ii :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIi11i + o0iIIIIi ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if i1iIIIi1i != 'Failed' :
  o0oO0OO00ooOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIIi1i )
  for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in o0oO0OO00ooOO :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 50 - 50: o0O0Oooo0O + oOOoOooOo + IIIIiiII111
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if III1iiIIi != 'Failed' :
  ii11iiI11I = [ ]
  IiIIiii11II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III1iiIIi )
  for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in IiIIiii11II1 :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    if iiIiii1IIIII in ii11iiI11I :
     pass
    else :
     OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , ii1i , Oo00OO0 , i11II1I11I1 )
     ii11iiI11I . append ( iiIiii1IIIII )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if i1I1IiI1ii != 'Failed' :
  OoOooO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1I1IiI1ii )
  for url , iII11 , iiIiii1IIIII in OoOooO :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , iII11 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 100 - 100: Ii1i1i + iI11I1II1I1I
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: o0O00o
    if 89 - 89: OOooOOo % iI11I1II1I1I
    if 35 - 35: Ii1I + o0O0Oooo0O - OOooOOo % ooOO0O0ooOooO % I11i % OOooOOo
    if 45 - 45: oOo0O0Ooo * IIIi11I1 % oO0o
    if 24 - 24: oOOoOooOo - iIII * ooOO0O0ooOooO
    if 87 - 87: Ii1i1i - Ii1I % Ii1I . ooOO0O0ooOooO / Ii1I
    if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
    if 79 - 79: o0O00o % oO0o
    if 81 - 81: Ii + Ii * oO0o + o0O00o
    if 32 - 32: o0o00Oo0O . ii
    if 15 - 15: oOo0O0Ooo . oO0o
    if 17 - 17: Ii / I1ii11iIi11i . oO0o / oOo0O0Ooo
    if 38 - 38: ooOoO0O00 . Ii1I % Ii1i1i + iI11I1II1I1I + o0o00Oo0O
    if 47 - 47: oO0o + o0O00o / IIiIiII11i
    if 97 - 97: Ii1I / oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - oOOoOooOo
    if 38 - 38: I11i % o0O0Oooo0O + Ii + IIIIiiII111 + oOOoOooOo / Ii
    if 94 - 94: IIIIiiII111 - I1ii11iIi11i + ooOO0O0ooOooO
    if 59 - 59: iIII . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
 if Oo0O0000Oo00o != 'Failed' :
  oO0o0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0O0000Oo00o )
  for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in oO0o0Oo :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 76 - 76: oOOoOooOo / OOooOOo + Ii1I
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 2 - 2: Ii - o0O0Oooo0O + oO0o % iIII * Ii1i1i
    if 54 - 54: o0o00Oo0O - IIIIiiII111 . IIIi11I1 % IIIIiiII111 + IIIIiiII111
    if 36 - 36: IIIi11I1 % Ii
    if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * ooOO0O0ooOooO . iIII / ooOoO0O00
    if 50 - 50: o0O0Oooo0O / ooOoO0O00 % ii
    if 83 - 83: Ii1I * Ii1I + IIIi11I1
    if 57 - 57: o0o00Oo0O - o0o00Oo0O . Ii1I / I11i / Ii1i1i
    if 20 - 20: IIIi11I1 * IIiIiII11i - OOooOOo - ooOO0O0ooOooO * o0O0Oooo0O
    if 6 - 6: oOOoOooOo + IIIi11I1 / I1ii11iIi11i + o0O00o % IIiIiII11i / oO0o
    if 45 - 45: ii
 I1oo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 17 - 17: o0o00Oo0O - OOooOOo
 for i1oO00O in I1oo :
  oo0o0ooooo = OOO00O + i1oO00O + I11iii1Ii
  Ooo0OOO = O0 ( oo0o0ooooo )
  if Ooo0OOO != 'Failed' :
   II1iI1IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ooo0OOO )
   for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in II1iI1IIi :
    if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
     oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 34 - 34: Ii1i1i * Ii1i1i - Ii1I - o0o00Oo0O . Ii
 I1oo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 32 - 32: iI11I1II1I1I . oO0o * ooOO0O0ooOooO / IIIi11I1 . IIiIiII11i - I1ii11iIi11i
 if 10 - 10: Ii1I / Ii - Ii1i1i + ooOO0O0ooOooO * oOo0O0Ooo
 for i1oO00O in I1oo :
  oo0o0ooooo = oO0o000OooOoo + i1oO00O
  OoooOo0 = O0 ( oo0o0ooooo )
  if OoooOo0 != 'Failed' :
   IiI1Ii1ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( OoooOo0 )
   for o0iIIIIi , iiIiii1IIIII in IiI1Ii1ii :
    if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
     O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oO0o000OooOoo + i1oO00O + o0iIIIIi ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 44 - 44: oOo0O0Ooo % Ii1i1i * oOo0O0Ooo . I1ii11iIi11i + Ii1I . IIIi11I1
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 6 - 6: o0O00o * ii + o0O0Oooo0O / Ii1i1i
def i1111IIiii1 ( ) :
 iI ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiiiiIIii + 'running.png' )
 iI ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiiiiIIii + 'countdown.png' )
 iI ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiiiiIIii + 'unknown.png' )
 iI ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiiiiIIii + 'cancelled.png' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 35 - 35: oOOoOooOo % oOo0O0Ooo - oOOoOooOo - oO0o - ii
def IiiIi1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , ooO0000o00O , ooo0Oooooo , I1I1IiIi1 , Ooi1IIii11i1I1 in Ii1i1iI1iIIi :
  iI ( ( '[COLORblue]' + iiIiii1IIIII + '[/COLOR] [COLORred]Season[/COLOR]-' + ooO0000o00O + ' [COLORred]Returns [/COLOR]- ' + Ooi1IIii11i1I1 + ' ' + I1I1IiIi1 ) , iiIiii1IIIII , 10099 , iiiiiIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 12 - 12: ooOoO0O00 / IIIi11I1 % oOOoOooOo * o0O00o * o0o00Oo0O * iI11I1II1I1I
def OOOOoO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , ooO0000o00O , ooo0Oooooo in Ii1i1iI1iIIi :
  iI ( ( '[COLORblue]' + iiIiii1IIIII + '[/COLOR] [COLORred]Season[/COLOR]-' + ooO0000o00O + ' [COLORred] Status Unknown[/COLOR] ' ) , iiIiii1IIIII , 10099 , iiiiiIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 19 - 19: oOo0O0Ooo % Ii1i1i . o0O00o * oOOoOooOo
def oOo0OOOOoO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , ooO0000o00O , ooo0Oooooo , I1I1IiIi1 in Ii1i1iI1iIIi :
  iI ( ( '[COLORblue]' + iiIiii1IIIII + ' [COLORred] Cancelled On[/COLOR] ' + I1I1IiIi1 ) , iiIiii1IIIII , 10099 , iiiiiIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 70 - 70: IIiIiII11i + o0O0Oooo0O + Ii - ooOoO0O00 / o0O00o
def iI1IIiiIIIII ( url ) :
 oOO0ooIiIIi1I1I11Ii = ( url )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 if 43 - 43: IIIIiiII111 + I1ii11iIi11i / ii
 if 24 - 24: o0o00Oo0O + I11i * Ii1i1i - o0O0Oooo0O
 OOoooO00o0o = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11I1 = 'http://onlinemovies.tube/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 IIi11i = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 oo0OoOO0o0o = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 ooOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 10 - 10: Ii
 Ooooo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iIiiiIiIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 ii11iO000oo00OOOOO = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 52 - 52: I1ii11iIi11i . iIII / I11i + Ii1i1i % iIII
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 47 - 47: ii / IIIi11I1 % oO0o / I1ii11iIi11i - Ii1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 13 - 13: IIIIiiII111 . oOo0O0Ooo * IIIi11I1 + Ii1i1i + oOo0O0Ooo - Ii
 if 79 - 79: oOOoOooOo . ooOO0O0ooOooO / ooOO0O0ooOooO - oOOoOooOo * I1ii11iIi11i / I11i
 iI1iiIi1 = O0 ( OOoooO00o0o )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 iiIi1IIiIi = O0 ( i11I1 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 oOO00Oo = O0 ( IIi11i )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 i1iIIIi1i = O0 ( oo0OoOO0o0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 OoooOo0 = O0 ( ooOOo0o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 49 - 49: oOOoOooOo . IIiIiII11i
 if 24 - 24: o0o00Oo0O . ii - oO0o * ii
 O00OOoOOOO00O = O0 ( Ooooo )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 Ooo0OOO = O0 ( iIiiiIiIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 Ii11iiI = O0 ( ii11iO000oo00OOOOO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 71 - 71: o0O0Oooo0O - I11i - IIIi11I1
 if Ooo0OOO != 'Failed' :
  II1iI1IIi = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Ooo0OOO )
  for url , iiIiii1IIIII in II1iI1IIi :
   Ii11iiI1 = O0 ( url )
   oO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii11iiI1 )
   for OOoooO00o0o , I1ii1Ii1 in oO0O :
    if i11ii in I1ii1Ii1 . lower ( ) :
     OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']*' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + OOoooO00o0o , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 28 - 28: iI11I1II1I1I
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if O00OOoOOOO00O != 'Failed' :
  iI11II1i1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00OOoOOOO00O )
  for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in iI11II1i1I1 :
   if i11ii in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 72 - 72: IIIIiiII111 - ii
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * ooOO0O0ooOooO
    if 30 - 30: iIII % OOooOOo / Ii1I * o0o00Oo0O * Ii1i1i . oOo0O0Ooo
    if 46 - 46: OOooOOo - o0o00Oo0O
    if 70 - 70: iIII + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * iIII
    if 49 - 49: I11i
    if 25 - 25: IIIIiiII111 . ii * iI11I1II1I1I . I11i / o0o00Oo0O + Ii1i1i
    if 68 - 68: I1ii11iIi11i
    if 22 - 22: IIIi11I1
    if 22 - 22: IIIIiiII111 * iIII - I1ii11iIi11i * o0o00Oo0O / Ii
    if 78 - 78: I1ii11iIi11i * o0o00Oo0O / oOOoOooOo + ii + IIIi11I1
    if 23 - 23: IIIIiiII111 % ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
 if Ii11iiI != 'Failed' :
  oOoO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii11iiI )
  for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in oOoO :
   if i11ii in iiIiii1IIIII . lower ( ) :
    iI ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , ii1i )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 32 - 32: o0o00Oo0O + ooOO0O0ooOooO % I1ii11iIi11i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  iI1iI = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  for url , iII11 , iiIiii1IIIII , O0O0 in I1Ii :
   if i11ii in iiIiii1IIIII . lower ( ) :
    if 'season' in O0O0 :
     iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , iII11 , iII11 , '' )
    if 'episodes' in O0O0 :
     iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , iII11 , iII11 , '' )
  for url in iI1iI :
   iI ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiiiiIIii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 70 - 70: IIIi11I1 * ooOO0O0ooOooO / oOo0O0Ooo * OOooOOo * oOo0O0Ooo
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iI1iiIi1 != 'Failed' :
  I1iiIIIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iI1iiIi1 )
  for url , iiIiii1IIIII , iII11 in I1iiIIIi11 :
   if i11ii in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( iiIiii1IIIII ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , iII11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 61 - 61: ooOO0O0ooOooO + Ii1I / ooOoO0O00 * ooOO0O0ooOooO
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 90 - 90: Ii1i1i % ooOO0O0ooOooO
    if 6 - 6: ii / Ii / o0O0Oooo0O
    if 60 - 60: oOo0O0Ooo % ooOO0O0ooOooO / I11i % ooOO0O0ooOooO * Ii / IIIIiiII111
    if 34 - 34: o0O0Oooo0O - IIIi11I1
    if 25 - 25: ooOO0O0ooOooO % oOo0O0Ooo + Ii + o0o00Oo0O * ii
    if 64 - 64: ooOoO0O00
    if 10 - 10: o0O0Oooo0O % o0o00Oo0O / oOo0O0Ooo % iIII
    if 25 - 25: IIiIiII11i / oO0o
    if 64 - 64: o0o00Oo0O % oOOoOooOo
 if oOO00Oo != 'Failed' :
  I1i1iii1Ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOO00Oo )
  for iiIiii1IIIII in I1i1iii1Ii :
   if i11ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( IIi11i + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 40 - 40: I11i + iIII
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if i1iIIIi1i != 'Failed' :
  o0oO0OO00ooOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1iIIIi1i )
  for iiIiii1IIIII in o0oO0OO00ooOO :
   if i11ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( oo0OoOO0o0o + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 77 - 77: Ii % o0O00o + o0O0Oooo0O % ii - iIII
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if OoooOo0 != 'Failed' :
  IiI1Ii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoooOo0 )
  for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in IiI1Ii1ii :
   if i11ii in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 26 - 26: I1ii11iIi11i + o0o00Oo0O - iI11I1II1I1I
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 47 - 47: ii
 II111IIIII = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for i1oO00O in II111IIIII :
  oo0o0ooooo = OOO00O + i1oO00O + I11iii1Ii
  Oo0O0000Oo00o = O0 ( oo0o0ooooo )
  if Oo0O0000Oo00o != 'Failed' :
   oO0o0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oo0O0000Oo00o )
   for iiIiii1IIIII , i11II1I11I1 , url , iII11 , ooo0O0o00O , oOo0 in oO0o0Oo :
    if i11ii in iiIiii1IIIII . lower ( ) :
     OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , url , oOo0 , iII11 , ooo0O0o00O , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 4 - 4: Ii1I + oO0o / o0O0Oooo0O / I11i % IIIi11I1 + IIIi11I1
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 66 - 66: ooOoO0O00 % IIIIiiII111 . IIIi11I1 - ooOO0O0ooOooO % OOooOOo / IIIi11I1
     if 26 - 26: IIIIiiII111 * Ii1i1i . o0O0Oooo0O - I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: ii - IIIIiiII111 + oOo0O0Ooo / IIIi11I1 * oOo0O0Ooo + oO0o
def OO0i1Ii11ii1I ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']Adult Gallery[/COLOR]' , '[COLOR' + II11iiii1Ii + ']JizBox[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Adult Channels[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  OO0oI1iii1i ( )
 if OoOOo0OOoO == 1 :
  oO0ooOoOO ( )
 if OoOOo0OOoO == 2 :
  Ii1 ( )
  if 1 - 1: o0o00Oo0O * Ii - oOOoOooOo - Ii1i1i
  if 94 - 94: oO0o + o0O00o + oOOoOooOo
  if 82 - 82: I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / IIIi11I1 + o0O00o % iI11I1II1I1I
def OO0oI1iii1i ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']YOLOselfies[/COLOR]' , '[COLOR' + II11iiii1Ii + ']HotNudeGirls[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MyNudeBabes[/COLOR]' , '[COLOR' + II11iiii1Ii + ']TeenNudeGirls[/COLOR]' , '[COLOR' + II11iiii1Ii + ']ADULTmeme[/COLOR]' , '[COLOR' + II11iiii1Ii + ']GIRLSmeme[/COLOR]' , ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  O00OOoo000o ( 'http://www.yoloselfie.com/' )
 if OoOOo0OOoO == 1 :
  iiIIIIiI111 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if OoOOo0OOoO == 2 :
  OoooOO0Oo0 ( 'http://www.teennudegirls.com/' )
 if OoOOo0OOoO == 3 :
  OoooOO0Oo0 ( 'http://www.teennudegirls.com/' )
 if OoOOo0OOoO == 4 :
  I1iIiIii ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if OoOOo0OOoO == 5 :
  I1iIiIii ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 76 - 76: oO0o . ii % o0O0Oooo0O * Ii1i1i
def O00OOoo000o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 100111 , iII11 )
 for url in I1Ii :
  iI ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 100110 , iII11 )
def i1iiI1i ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O0OOO00OOO00o = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( O0OOO00OOO00o )
  sys . exit ( 1 )
def I1iIiIii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + iII11 , 100113 , 'http:' + iII11 )
 for url in I1Ii :
  iI ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , 'http:' + url , 100112 , iII11 )
def iiIIIIiI111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , iII11 )
def i11o00Ooo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']Click To Enlarge[/COLOR]' , iII11 , 100113 , iII11 )
def OoO00OOoOOOo0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , iII11 )
def oOoO00O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']Click To Enlarge[/COLOR]' , iII11 , 100113 , iII11 )
def OoooOO0Oo0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , iII11 )
def I11I1I1i1i ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']Click To Enlarge[/COLOR]' , iII11 , 100113 , iII11 )
def Oo0oOO0O00 ( url ) :
 O0OOO00OOO00o = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( O0OOO00OOO00o )
 sys . exit ( 1 )
 if 55 - 55: oOOoOooOo % I1ii11iIi11i % I11i
def I1IiO00Ooo0ooo0 ( ) :
 if 74 - 74: iIII
 if 58 - 58: iI11I1II1I1I * oO0o * o0O0Oooo0O * oOOoOooOo . ii
 if 6 - 6: Ii1I - ooOO0O0ooOooO * Ii + OOooOOo / oOOoOooOo % IIIi11I1
 if 38 - 38: IIIi11I1 % o0O00o % IIiIiII11i - I1ii11iIi11i - iI11I1II1I1I
 if 9 - 9: I11i % Ii1I . Ii1I
 if 28 - 28: ii % ooOO0O0ooOooO + Ii1I + o0o00Oo0O . o0O0Oooo0O
 if 80 - 80: Ii % Ii1I
 if 54 - 54: I11i + iIII - iI11I1II1I1I % oOOoOooOo % o0O00o
 if 19 - 19: Ii1I / iI11I1II1I1I % ooOoO0O00 . ii
 if 57 - 57: oOOoOooOo . I1ii11iIi11i - oO0o - Ii * o0O0Oooo0O / I11i
 if 79 - 79: Ii1I + I11i % I1ii11iIi11i * I11i
 iI ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiiiiIIii + 'seasons.png' )
 iI ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiiiiIIii + 'episodes.png' )
 iI ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiiiiIIii + 'Search.png' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 21 - 21: IIIIiiII111
def i11Ii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iiiI1IiiI in Ii1i1iI1iIIi :
  iI ( ( iiIiii1IIIII + ' - ' + iiiI1IiiI ) . replace ( '&amp;' , '&' ) , url , 90053 , iiiiiIIii + 'seasons.png' )
  if 70 - 70: iIII . IIIi11I1 * I1ii11iIi11i / IIIi11I1
def Oo0OoOo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , url , 90054 , iiiiiIIii + 'episodes.png' )
  if 13 - 13: I11i
def IIi1ii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , url , 90054 , iII11 )
 for url in next :
  iI ( 'NEXT' , url , 90053 , iiiiiIIii + 'Next.png' )
  if 38 - 38: iI11I1II1I1I + ii * oOo0O0Ooo % OOooOOo % iIII - o0O00o
def Oo0OO00OO0Oo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0000OOo00 )
 for iII11 , iiiI1IiiI , url , iiIiii1IIIII , IiI in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiiI1IiiI + ' - ' + iiIiii1IIIII + ' - ' + IiI , url , 90044 , iII11 , iII11 , '' )
 for iII11 , iiIiii1IIIII , url in I1Ii :
  iI ( iiIiii1IIIII , url , 90044 , iII11 , iII11 , '' )
 for url in next :
  iI ( 'NEXT' , url , 90053 , iiiiiIIii + 'Next.png' )
  if 74 - 74: iIII
def OO0oOoO000o0 ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'http://onlinemovies.tube/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11ii = IiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( i11ii )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , O0O0 in Ii1i1iI1iIIi :
  if 'season' in O0O0 :
   iI ( iiIiii1IIIII , Oo0o00OO0000 , 90054 , iII11 , iII11 , '' )
  if 'episodes' in O0O0 :
   iI ( iiIiii1IIIII , Oo0o00OO0000 , 90044 , iII11 , iII11 , '' )
 for Oo0o00OO0000 in next :
  iI ( 'NEXT' , Oo0o00OO0000 , 90053 , iiiiiIIii + 'Next.png' )
  if 95 - 95: o0o00Oo0O / iIII . o0O0Oooo0O
def iII11II1II ( ) :
 if 100 - 100: oO0o % o0O0Oooo0O - iIII % iIII % iIII / oOOoOooOo
 if 83 - 83: ooOO0O0ooOooO - oOOoOooOo - o0O00o % ooOoO0O00 - IIIIiiII111 . I11i
 if 96 - 96: I1ii11iIi11i + o0O0Oooo0O . ooOoO0O00
 if 54 - 54: IIiIiII11i . ooOoO0O00 / Ii1I % oOo0O0Ooo / o0O0Oooo0O
 if 65 - 65: OOooOOo . OOooOOo - ooOO0O0ooOooO + I1ii11iIi11i / Ii
 if 90 - 90: iI11I1II1I1I + OOooOOo
 if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
 if 30 - 30: IIIIiiII111 / oO0o . IIIIiiII111
 if 17 - 17: I1ii11iIi11i + ii * ii
 if 5 - 5: o0O0Oooo0O % ii . OOooOOo
 iI ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiiiiIIii + 'allmov.png' )
 iI ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiiiiIIii + 'Genre.png' )
 iI ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiiiiIIii + 'Years.png' )
 iI ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiiiiIIii + 'Search.png' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 67 - 67: Ii1I + Ii1i1i
def o0O00OooooO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iiiI1IiiI in Ii1i1iI1iIIi :
  if 'genre' in url :
   iI ( ( iiIiii1IIIII + ' - ' + iiiI1IiiI ) . replace ( '&amp;' , '&' ) , url , 90043 , iiiiiIIii + 'Genre.png' )
   if 77 - 77: oOo0O0Ooo % oOOoOooOo
def oO0oo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'release' in url :
   iI ( iiIiii1IIIII , url , 90043 , iiiiiIIii + 'Years.png' )
   if 52 - 52: o0O00o % oOOoOooOo
def I111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , oOOooo00OOooO , url , i11II1I11I1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII + ' ' + oOOooo00OOooO , url , 90044 , iII11 , iII11 , i11II1I11I1 )
 for iII11 , iiIiii1IIIII , O0O0 , url , IIII , i11II1I11I1 in I1Ii :
  if 'movies' in O0O0 :
   OoOOoOooooOOo ( iiIiii1IIIII + ' - ' + IIII , url , 90044 , iII11 , iII11 , i11II1I11I1 )
 for url in next :
  iI ( 'NEXT' , url , 90043 , iiiiiIIii + 'Next.png' )
  if 65 - 65: IIiIiII11i / I1ii11iIi11i
def iiII1i ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  IiiiI1 ( 'http:' + url )
  if 34 - 34: Ii1i1i + I1ii11iIi11i - ooOoO0O00 - o0O00o + iI11I1II1I1I
def IiiiI1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( iiIiii1IIIII ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiiiiIIii + 'movhub.png' )
def o0Oo00oOO ( ) :
 if 73 - 73: iIII / ii . IIiIiII11i - o0O00o * oOOoOooOo * o0O00o
 if 45 - 45: o0o00Oo0O * o0O0Oooo0O + Ii - IIIi11I1 - iI11I1II1I1I
 if 5 - 5: IIIi11I1 % I1ii11iIi11i % o0O00o % oOOoOooOo
 if 17 - 17: Ii1i1i + IIiIiII11i + ii / IIIi11I1 / o0O00o
 if 80 - 80: I11i % ooOoO0O00 / iIII
 if 56 - 56: ooOoO0O00 . Ii
 if 15 - 15: IIiIiII11i * ooOO0O0ooOooO % IIIIiiII111 / Ii - ooOO0O0ooOooO + I1ii11iIi11i
 if 9 - 9: iIII - ooOO0O0ooOooO + o0o00Oo0O / IIIIiiII111 % ooOoO0O00
 if 97 - 97: I11i * oOOoOooOo
 if 78 - 78: iIII . IIIi11I1 + ooOO0O0ooOooO * IIIIiiII111 - ooOoO0O00
 if 27 - 27: Ii1i1i % ooOoO0O00 . I1ii11iIi11i % o0O0Oooo0O
 if 10 - 10: o0O00o / ii
 if 50 - 50: Ii - ii . ooOO0O0ooOooO + o0o00Oo0O . ooOoO0O00
 if 91 - 91: I11i . IIIIiiII111 % I1ii11iIi11i - IIIIiiII111 . ooOO0O0ooOooO % Ii
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'http://onlinemovies.tube/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11ii = IiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( i11ii )
 Ii1i1iI1iIIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , iIiO0O in Ii1i1iI1iIIi :
  if 'movies' in iIiO0O :
   iI ( iIiO0O + '-' + iiIiii1IIIII , Oo0o00OO0000 , 90044 , iII11 )
 for Oo0o00OO0000 in next :
  I111 ( Oo0o00OO0000 )
  if 71 - 71: Ii1I + oO0o
def ooo0oooo0 ( ) :
 iI ( 'Search' , '' , 80008 , iiiiiIIii + 'Search.png' )
 oO0000OOo00 = i11oO0oOo0 ( 'http://www.join4films.com/' )
 Ii1i1iI1iIIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , Oo0o00OO0000 , 80006 , iiiiiIIii + 'Desi.png' )
def ii1oooO0o0oOoO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0000OOo00 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( iiIiii1IIIII , url , 80007 , iII11 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( 'Next' , url , 80006 , iiiiiIIii + 'Next.png' )
def I11iii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  url = ( url ) . replace ( ' ' , '%20' )
  O0i1iI ( url )
def IIi111 ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'http://www.join4films.com/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' ) + '&search_type=1'
 i11ii = IiiI . lower ( )
 ii1oooO0o0oOoO ( i11ii )
 if 61 - 61: Ii1I - IIIi11I1
 if 16 - 16: IIIIiiII111 / iI11I1II1I1I + IIIi11I1 * IIIIiiII111 * iIII
 if 8 - 8: o0O0Oooo0O
 if 15 - 15: I1ii11iIi11i / Ii1i1i % o0o00Oo0O + Ii1I
 if 96 - 96: oOOoOooOo . ii
 if 39 - 39: IIIi11I1 + oO0o
 if 80 - 80: IIIi11I1 % oO0o / OOooOOo
 if 54 - 54: I1ii11iIi11i % oO0o - IIIi11I1 - iIII
 if 71 - 71: oOOoOooOo . Ii
 if 56 - 56: o0o00Oo0O * IIIIiiII111 + IIIIiiII111 * iI11I1II1I1I / oOOoOooOo * o0O0Oooo0O
 if 25 - 25: iI11I1II1I1I . iIII * Ii + I1ii11iIi11i * iIII
 if 67 - 67: IIIIiiII111
 if 88 - 88: I1ii11iIi11i
 if 8 - 8: Ii1I
 if 82 - 82: ii
 if 75 - 75: IIiIiII11i % oOo0O0Ooo + IIIi11I1 % ii / o0O00o
 if 4 - 4: Ii - IIIi11I1 % Ii1I * o0O0Oooo0O % I11i
def o0OoOoo ( ) :
 OoOOoOooooOOo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( 'Search' , '' , 10078 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 if 75 - 75: IIIIiiII111 * oOo0O0Ooo + IIIIiiII111 - ii
def OooO ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'http://imoviemax.se/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11ii = IiiI . lower ( )
 oOoO0 ( i11ii )
def Iii1II1ii ( url ) :
 ooOo00 = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , OO0III in Ii1i1iI1iIIi :
  if iiIiii1IIIII in ooOo00 :
   pass
  else :
   OoOOoOooooOOo ( iiIiii1IIIII + ' - ' + OO0III + ' Films' , url , 10074 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
   ooOo00 . append ( iiIiii1IIIII )
   if 59 - 59: ii / o0O00o + iIII . IIIIiiII111 * Ii1i1i - ii
def OO0O0OO0O0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , oOoo in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII + ' - Views:' + oOoo , url , 10075 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
  if 63 - 63: iI11I1II1I1I % I11i * oOOoOooOo
  if 79 - 79: o0o00Oo0O
def oOoO0 ( url ) :
 IiIiiIi1IiiIi1 = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0000OOo00 )
 for next in next :
  OoOOoOooooOOo ( 'NEXT PAGE' , next , 10074 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 Ii1i1iI1iIIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 10075 , iII11 , iII11 , '' )
  IiIiiIi1IiiIi1 . append ( iiIiii1IIIII )
  if 41 - 41: iI11I1II1I1I * IIIIiiII111 + I1ii11iIi11i * I11i % o0O00o / IIIi11I1
def Oo0o0ooOoO ( img , name , url ) :
 img = img
 name = name
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0000OOo00 )
 for iI1Ii11 , url in Ii1i1iI1iIIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  Ooo0 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + Ooo0
  IiiiIIi = ( iI1Ii11 ) . replace ( 'play-' , 'Server ' )
  oOOOoo0O0oO ( IiiiIIi , Ooo0 , 10076 , img , img , '' )
  if 4 - 4: o0O0Oooo0O + oO0o + o0o00Oo0O + o0O00o
def OOooO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0000OOo00 )
 for i11I1 in Ii1i1iI1iIIi :
  if '=m' in i11I1 :
   II1i1i1I1iII ( i11I1 )
  elif 'php' in i11I1 :
   OOooO ( url )
  else :
   oO0000OOo00 = i11oO0oOo0 ( i11I1 )
   Ii1i1iI1iIIi = re . compile ( 'content="([^"]*)">' ) . findall ( oO0000OOo00 )
   for IIi11i in Ii1i1iI1iIIi :
    II1i1i1I1iII ( i11I1 )
    if 48 - 48: IIIi11I1 . IIIi11I1 + Ii + Ii1I % o0o00Oo0O
    if 67 - 67: oOOoOooOo / iIII * oOo0O0Ooo % ii
    if 46 - 46: o0O00o
def IIiI1iIi1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 III = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for I1I1IiIi1 , Oo0o0O00oOOO0o in III :
  print 'there ><><><><><><><><><><><><'
  I1I1IiIi1 = I1I1IiIi1
  Ii1i1iI1iIIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo0o0O00oOOO0o ) )
  for iiIiii1IIIII , O0Ooo in Ii1i1iI1iIIi :
   print 'here <><><><><><><><><><><><>'
   OoOOoOooooOOo ( '[COLORred]' + I1I1IiIi1 + '[/COLOR] - ' + iiIiii1IIIII + ' - [COLOR' + II11iiii1Ii + ']' + O0Ooo + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiiiiIIii + 'loader.png' , iIi1ii1I1 , '' )
 Ii1II1I11i1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for I1I1IiIi1 , iIIIOoO0000 in Ii1II1I11i1 :
  print 'there ><><><><><><><><><><><><'
  I1I1IiIi1 = I1I1IiIi1
  Ii1i1iI1iIIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iIIIOoO0000 ) )
  for iiIiii1IIIII , O0Ooo in Ii1i1iI1iIIi :
   print 'here <><><><><><><><><><><><>'
   OoOOoOooooOOo ( '[COLORred]' + I1I1IiIi1 + '[/COLOR] - ' + iiIiii1IIIII + ' - [COLOR' + II11iiii1Ii + ']' + O0Ooo + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiiiiIIii + 'loader.png' , iIi1ii1I1 , '' )
   if 11 - 11: oO0o - Ii1i1i + o0o00Oo0O * oO0o
   if 59 - 59: IIiIiII11i
   if 43 - 43: I1ii11iIi11i + ii
def OOOoO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Ii1II1I11i1 in Ii1II1I11i1 :
  iiIiii1IIIII = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iiIiii1IIIII in iiIiii1IIIII :
   iiIiii1IIIII = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Ii1II1I11i1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iiIiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iiIiI in iiIiI :
   iiIiI = 'http:' + iiIiI
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI , '' , '' )
  if 47 - 47: oOOoOooOo
  if 92 - 92: iIII % Ii % I1ii11iIi11i
  if 23 - 23: IIiIiII11i * IIIIiiII111
  if 80 - 80: o0O0Oooo0O / Ii + ii
def OOO0ooo ( url ) :
 if 38 - 38: Ii1I % oOOoOooOo + ooOoO0O00 * ii * ooOO0O0ooOooO
 OoO0o0OO = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for i11I1 , iII11 , iiIiii1IIIII , II11IiI1 in Ii1i1iI1iIIi :
  iiIiii1IIIII = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iiIi1IIiIi = i11oO0oOo0 ( i11I1 )
  I1Ii = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iiIi1IIiIi )
  for I1iiIiI1iI1I , iII1 in I1Ii :
   iIIi11i = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iII1 ) )
   for i11II1I11I1 in iIIi11i :
    if iiIiii1IIIII in OoO0o0OO :
     pass
    else :
     oOOOoo0O0oO ( iiIiii1IIIII , I1iiIiI1iI1I , 8043 , iII11 , iII11 , i11II1I11I1 )
     OOoOO0o0o0 ( 'movies' , 'INFO' )
     OoO0o0OO . append ( iiIiii1IIIII )
     if 39 - 39: OOooOOo . I1ii11iIi11i - o0O00o / I11i / ooOoO0O00
     if 79 - 79: IIIi11I1 % o0O0Oooo0O / ooOO0O0ooOooO - iI11I1II1I1I - OOooOOo
def o0oOO ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , ii1i , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 10065 , ii1i , ooo0O0o00O , i11II1I11I1 )
 OOoOO0o0o0 ( 'movies' , 'INFO' )
 if 84 - 84: Ii + oOOoOooOo . o0o00Oo0O
def o00oo ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'https://www.youtube.com/results?search_query=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11ii = IiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( i11ii )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 in next :
  Oo0o00OO0000 = 'https://www.youtube.com' + Oo0o00OO0000
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + '] NEXT [/COLOR]' , Oo0o00OO0000 , 10065 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 for iII11 , Oo0o00OO0000 , iiIiii1IIIII , Ii11IIIi1 , iII1 in Ii1i1iI1iIIi :
  O000oo0O . append ( iiIiii1IIIII )
  OOoOO0o0o0 ( 'tvshows' , 'INFO' )
  iiIiI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiIiI
  Oo0o00OO0000 = 'http://www.youtube.com' + Oo0o00OO0000
  oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI , iiIiI , iII1 )
 else :
  Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iII11 , Oo0o00OO0000 , iiIiii1IIIII , Ii11IIIi1 in Ii1i1iI1iIIi :
   print 'im doing it'
   OOoOO0o0o0 ( 'tvshows' , 'INFO' )
   iiIiI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
   Oo0o00OO0000 = 'http://www.youtube.com' + Oo0o00OO0000
   if '&' in Oo0o00OO0000 :
    print ' i got here'
    oO0000OOo00 = i11oO0oOo0 ( Oo0o00OO0000 )
    Ii1II1I11i1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0000OOo00 )
    for Ii1II1I11i1 in Ii1II1I11i1 :
     iiIiii1IIIII = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
     for iiIiii1IIIII in iiIiii1IIIII :
      iiIiii1IIIII = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     Oo0o00OO0000 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Ii1II1I11i1 ) )
     for Oo0o00OO0000 in Oo0o00OO0000 :
      Oo0o00OO0000 = 'https://www.youtube.com/w' + Oo0o00OO0000
     iiIiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
     for iiIiI in iiIiI :
      iiIiI = 'http:' + iiIiI
     oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI , iIi1ii1I1 , '' )
   elif iiIiii1IIIII in O000oo0O :
    pass
   elif 'user' in Oo0o00OO0000 or 'elete' in iiIiii1IIIII :
    pass
   elif 'hannel' in Oo0o00OO0000 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Oo0o00OO0000
    oO0000OOo00 = i11oO0oOo0 ( Oo0o00OO0000 )
    ooooooo00oO0OO = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
    for iII11 , Oo0o00OO0000 , iiIiii1IIIII in ooooooo00oO0OO :
     if 'outube' in Oo0o00OO0000 or 'list' in Oo0o00OO0000 :
      pass
     elif 'atch' in Oo0o00OO0000 :
      Oo0o00OO0000 = ( Oo0o00OO0000 ) . replace ( '/watch?v=' , '' )
      oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iII11 , 'http:' + iII11 , '' )
     else :
      pass
   else :
    oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI , iiIiI , '' )
    if 30 - 30: I11i + ii + IIIi11I1 / IIiIiII11i * I1ii11iIi11i
def O00O0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0000OOo00 )
 for url in next :
  url = 'https://www.youtube.com' + url
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + '] NEXT [/COLOR]' , url , 10065 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 for iII11 , url , iiIiii1IIIII , Ii11IIIi1 , iII1 in Ii1i1iI1iIIi :
  O000oo0O . append ( iiIiii1IIIII )
  OOoOO0o0o0 ( 'tvshows' , 'INFO' )
  iiIiI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiIiI
  url = 'http://www.youtube.com' + url
  oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI , iiIiI , iII1 )
 else :
  Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iII11 , url , iiIiii1IIIII , Ii11IIIi1 in Ii1i1iI1iIIi :
   OOoOO0o0o0 ( 'tvshows' , 'INFO' )
   iiIiI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0000OOo00 = i11oO0oOo0 ( url )
    Ii1II1I11i1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0000OOo00 )
    for Ii1II1I11i1 in Ii1II1I11i1 :
     iiIiii1IIIII = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
     for iiIiii1IIIII in iiIiii1IIIII :
      iiIiii1IIIII = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Ii1II1I11i1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iiIiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
     for iiIiI in iiIiI :
      iiIiI = 'http:' + iiIiI
     oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI , iIi1ii1I1 , '' )
   elif iiIiii1IIIII in O000oo0O :
    pass
   elif 'user' in url or 'elete' in iiIiii1IIIII :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0000OOo00 = i11oO0oOo0 ( url )
    ooooooo00oO0OO = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
    for iII11 , url , iiIiii1IIIII in ooooooo00oO0OO :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iII11 , 'http:' + iII11 , '' )
     else :
      pass
   else :
    oOOOoo0O0oO ( '[COLORred]' + Ii11IIIi1 + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI , iiIiI , '' )
    if 43 - 43: ooOO0O0ooOooO % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
    if 4 - 4: IIiIiII11i - ooOO0O0ooOooO % I1ii11iIi11i * Ii
    if 18 - 18: I1ii11iIi11i % o0o00Oo0O
def oooooO00OOO ( ) :
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiiiiIIii + 'linkchannels.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Open Guide[/COLOR]' , '' , 100213 , iiiiiIIii + 'TvGuide.png' , iIi1ii1I1 , '' )
 if 53 - 53: IIiIiII11i
def Oo0O0ooo0O0O ( ) :
 ivuesetup . iVueInt ( )
 if 13 - 13: I1ii11iIi11i / Ii1I
def I11i1I11iIii ( ) :
 O0OOooO00oOOooo ( )
 return
 if 11 - 11: oO0o % ii
def O0OOooO00oOOooo ( ) :
 if 20 - 20: o0O0Oooo0O + o0O0Oooo0O * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
 o0OOOO00O0Oo = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 OooOo = o0OOOO00O0Oo . getSetting ( id = 'User' )
 O0OOoOOO0o0o = o0OOOO00O0Oo . getSetting ( id = 'Pass' )
 iIOoo0ooo0oo = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 I11iIiI1 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 i1I1iiii1Ii11 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 IiIIIIi = "http://piesustv" + O00o0OO + ":8000/get.php?username=" + OooOo + "&password=" + O0OOoOOO0o0o + "&type=m3u_plus&output=ts"
 OoIIiIIIII1I = "http://piesustv" + O00o0OO + ":8000/xmltv.php?username=" + OooOo + "&password=" + O0OOoOOO0o0o + "&type=m3u_plus&output=ts"
 if 96 - 96: Ii . IIiIiII11i
 xbmc . executeJSONRPC ( iIOoo0ooo0oo )
 xbmc . executeJSONRPC ( I11iIiI1 )
 xbmc . executeJSONRPC ( i1I1iiii1Ii11 )
 if 7 - 7: ooOoO0O00
 Oo00oo = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 Oo00oo . setSetting ( id = 'm3uUrl' , value = IiIIIIi )
 Oo00oo . setSetting ( id = 'epgUrl' , value = OoIIiIIIII1I )
 Oo00oo . setSetting ( id = 'm3uCache' , value = "false" )
 Oo00oo . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def oO0oO ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 71 - 71: o0O0Oooo0O / oOo0O0Ooo / o0o00Oo0O
if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / IIIi11I1 . Ii1I * oOOoOooOo
if 59 - 59: iI11I1II1I1I / Ii1I % oOOoOooOo
def Oooo ( ) :
 if 74 - 74: oOOoOooOo % OOooOOo / I1ii11iIi11i
 if 2 - 2: o0O00o % o0O00o % o0O0Oooo0O
 if 60 - 60: IIIi11I1
 if 73 - 73: oOOoOooOo
 if 86 - 86: OOooOOo . iIII / I1ii11iIi11i * iIII
 if 20 - 20: oOOoOooOo - IIIi11I1 * oO0o * I11i * IIIi11I1 / o0O00o
 if 40 - 40: oOo0O0Ooo * I11i . oOo0O0Ooo
 if 62 - 62: oOOoOooOo + IIiIiII11i % oOOoOooOo
 if 50 - 50: ii + ooOO0O0ooOooO * oOo0O0Ooo - Ii1i1i / Ii
 if 5 - 5: o0o00Oo0O - oOo0O0Ooo
 if 44 - 44: IIiIiII11i . IIiIiII11i + IIIi11I1 * Ii1i1i
 if 16 - 16: IIiIiII11i
 if O0o0Oo == "insert_username" :
  oooOO0OO0 = iiI1i ( )
  OoOo = III1IiIi1 ( )
  I11 ( 'User' , oooOO0OO0 )
  I11 ( 'Pass' , OoOo )
  xbmc . executebuiltin ( 'Container.Refresh' )
  oOOoO0O = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( oooOO0OO0 , OoOo )
  oOOoO0O = i11oO0oOo0 ( oOOoO0O )
  if oOOoO0O == "" :
   OoOoO = "[COLOR " + II11iiii1Ii + "]Incorrect Login Details[/COLOR]"
   oOOo00Ooo0O = "[COLOR " + II11iiii1Ii + "]Please Re-enter[/COLOR]"
   iIii1Oo = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , OoOoO , oOOo00Ooo0O , iIii1Oo )
   Oooo ( )
  else :
   OoOoO = "[COLOR " + II11iiii1Ii + "]Login Successful[/COLOR]"
   oOOo00Ooo0O = "[COLOR " + II11iiii1Ii + "]Welcome to GenieTv[/COLOR]"
   iIii1Oo = ( '[COLOR ' + II11iiii1Ii + ']%s[/COLOR]' % oooOO0OO0 )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , OoOoO , oOOo00Ooo0O , iIii1Oo )
   xbmc . executebuiltin ( 'Container.Refresh' )
   Ii11ii1 ( )
 else :
  Ii11ii1 ( )
def iiI1i ( ) :
 iiiIiiiI1I = xbmc . Keyboard ( '' , 'heading' , True )
 iiiIiiiI1I . setHeading ( 'Enter Username' )
 iiiIiiiI1I . setHiddenInput ( False )
 iiiIiiiI1I . doModal ( )
 if ( iiiIiiiI1I . isConfirmed ( ) ) :
  i111I1 = iiiIiiiI1I . getText ( )
  return i111I1
 else :
  return False
  if 69 - 69: oO0o - ii - IIIi11I1 % iIII / OOooOOo - IIiIiII11i
  if 67 - 67: IIIi11I1 + IIIi11I1 + oO0o . Ii + Ii1I + Ii
def III1IiIi1 ( ) :
 iiiIiiiI1I = xbmc . Keyboard ( '' , 'heading' , True )
 iiiIiiiI1I . setHeading ( 'Enter Password' )
 iiiIiiiI1I . setHiddenInput ( False )
 iiiIiiiI1I . doModal ( )
 if ( iiiIiiiI1I . isConfirmed ( ) ) :
  i111I1 = iiiIiiiI1I . getText ( )
  return i111I1
 else :
  return False
def IIi11I1i1I1I ( ) :
 IiIIIIi = "http://piesustv" + O00o0OO + ":8000//get.php?username=" + O0o0Oo + "&password=" + Oo00OOOOO + "&type=m3u_plus&output=ts"
 try :
  IiII1I = urllib2 . urlopen ( IiIIIIi )
  print IiII1I . getcode ( )
  IiII1I . close ( )
  if 72 - 72: Ii1i1i / I1ii11iIi11i / ooOO0O0ooOooO * OOooOOo + IIIi11I1
  pass
  if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - o0O00o . ii
 except urllib2 . HTTPError , I1iI1I1I1i11i :
  print I1iI1I1I1i11i . getcode ( )
  O0OoO000O0OO . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + II11iiii1Ii + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + II11iiii1Ii + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def Ii11ii1 ( ) :
 OOooOoooOoOo ( )
 if 10 - 10: o0O0Oooo0O
 if 48 - 48: IIIIiiII111 * ooOoO0O00 % ii * Ii1i1i * oO0o
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']My Account[/COLOR]' , 'http://piesustv' + O00o0OO + ':8000/panel_api.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO , 60004 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Guide Menu[/COLOR]' , '' , 100211 , iiiiiIIii + 'TvGuide.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']VOD Lists[/COLOR]' , '' , 40000 , iiiiiIIii + 'Vod_Lists.png' , iIi1ii1I1 , '' )
 if 7 - 7: IIIIiiII111 . Ii1i1i . IIIIiiII111 - o0O0Oooo0O
 if 33 - 33: oOOoOooOo + ii - oO0o / ooOoO0O00 / ii
 if 82 - 82: Ii1I / IIIi11I1 - IIIIiiII111 / I1ii11iIi11i * oO0o
 if 55 - 55: ii
def OO0OOOOOo ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 iii1ii = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + O0o0Oo + '%26password%3D' + Oo00OOOOO + '%26type%3Dm3u_plus%26output%3Dts'
 Ii11i = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + O0o0Oo + '%26password%3D' + Oo00OOOOO
 oOOoO0O = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO + '&type=get_vod_categories'
 oOOoO0O = i11oO0oOo0 ( oOOoO0O )
 if not oOOoO0O == "" :
  o0oO00OOo0oO = 'https://tinyurl.com/create.php?source=indexpage&url=' + iii1ii + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( o0oO00OOo0oO ) )
  oOiiI11I1ii11 = 'https://tinyurl.com/create.php?source=indexpage&url=' + Ii11i + '&submit=Make+TinyURL%21&alias='
  iii1ii = i11oO0oOo0 ( o0oO00OOo0oO )
  Ii11i = i11oO0oOo0 ( oOiiI11I1ii11 )
  xbmc . log ( str ( Ii11i ) )
  O0OoO0oooOO = i1ii11I111Ii ( iii1ii , '<div class="indent"><b>' , '</b>' )
  OOoO00O = i1ii11I111Ii ( Ii11i , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + II11iiii1Ii + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % O0OoO0oooOO , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % OOoO00O )
 else :
  return
def iio00O0o00oo ( ) :
 IIi11I1i1I1I ( )
 iIiiII ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , iII1I + '&action=get_vod_streams' , 40001 , iiiiiIIii + 'Vod_Lists.png' , iIi1ii1I1 , '' )
 oO0000OOo00 = i11oO0oOo0 ( o00oOOo0Oo )
 Ii1i1iI1iIIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLORsteelblue]' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , Oo0o00OO0000 , 40001 , iiiiiIIii + 'Vod_Lists.png' , iIi1ii1I1 , '' )
def Oooo0o0oO ( url ) :
 open = i11oO0oOo0 ( o0OOoOooO0ooO + url )
 IiiiIi = IiI111 ( open , '<channel>' , '</channel>' )
 for oOoO00o in IiiiIi :
  if '<playlist_url>' in open :
   iiIiii1IIIII = i1ii11I111Ii ( oOoO00o , '<title>' , '</title>' )
   OOoooO00o0o = i1ii11I111Ii ( oOoO00o , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   OoOOoOooooOOo ( str ( base64 . b64decode ( iiIiii1IIIII ) ) . replace ( '?' , '' ) , OOoooO00o0o , 40001 , icon , ooo0O0o00O , '' )
  else :
   if xbmcaddon . Addon ( ) . getSetting ( 'meta' ) == 'true' :
    try :
     iiIiii1IIIII = i1ii11I111Ii ( oOoO00o , '<title>' , '</title>' )
     iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
     OO0OO00ooO0 = i1ii11I111Ii ( oOoO00o , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     url = i1ii11I111Ii ( oOoO00o , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     i11II1I11I1 = i1ii11I111Ii ( oOoO00o , '<description>' , '</description>' )
     i11II1I11I1 = base64 . b64decode ( i11II1I11I1 )
     iiIiIiII = i1ii11I111Ii ( i11II1I11I1 , 'PLOT:' , '\n' )
     OOOOOoO00oo00 = i1ii11I111Ii ( i11II1I11I1 , 'CAST:' , '\n' )
     iIIIII11 = i1ii11I111Ii ( i11II1I11I1 , 'RATING:' , '\n' )
     i1I1 = i1ii11I111Ii ( i11II1I11I1 , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
     i1I1 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( i1I1 )
     ooooOOO0 = i1ii11I111Ii ( i11II1I11I1 , 'DURATION_SECS:' , '\n' )
     Ii1i = i1ii11I111Ii ( i11II1I11I1 , 'GENRE:' , '\n' )
     ooooOoOooo00Oo ( str ( iiIiii1IIIII ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , OO0OO00ooO0 , ooo0O0o00O , iiIiIiII , str ( i1I1 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( OOOOOoO00oo00 ) . split ( ) , iIIIII11 , ooooOOO0 , Ii1i )
    except : pass
    xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   else :
    iiIiii1IIIII = i1ii11I111Ii ( oOoO00o , '<title>' , '</title>' )
    iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
    OO0OO00ooO0 = i1ii11I111Ii ( oOoO00o , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    url = i1ii11I111Ii ( oOoO00o , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    i11II1I11I1 = i1ii11I111Ii ( oOoO00o , '<description>' , '</description>' )
    oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , OO0OO00ooO0 , ooo0O0o00O , base64 . b64decode ( i11II1I11I1 ) )
    if 72 - 72: iIII
i1I1IIiIIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
iII1ii1IIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 98 - 98: Ii . o0O0Oooo0O * ooOO0O0ooOooO . IIIIiiII111
def OOOo0o0O ( ) :
 IiIIIIi = "http://piesustv" + O00o0OO + ":8000/get.php?username=" + O0o0Oo + "&password=" + Oo00OOOOO + "&type=m3u_plus&output=ts"
 try :
  IiII1I = urllib2 . urlopen ( IiIIIIi )
  print IiII1I . getcode ( )
  IiII1I . close ( )
  if 100 - 100: o0o00Oo0O
  pass
  if 94 - 94: Ii1I - I11i
 except urllib2 . HTTPError , I1iI1I1I1i11i :
  print I1iI1I1I1i11i . getcode ( )
  O0OoO000O0OO . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 42 - 42: I11i * OOooOOo . oO0o - IIIIiiII111 / IIiIiII11i
 Oo0o00OO0000 = "http://piesustv" + O00o0OO + ":8000/xmltv.php?username=%s&password=%s" % ( O0o0Oo , Oo00OOOOO )
 iII1ii11III ( Oo0o00OO0000 , iII1ii1IIII + "uide.xml" )
 if 92 - 92: oO0o - Ii1I + iI11I1II1I1I % I11i
 OOo0O0oo0OO0O = open ( i1I1IIiIIi , 'r+' )
 input = open ( i1I1IIiIIi ) . read ( ) . decode ( 'UTF-8' )
 ooooooO0O = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 OOo0O0oo0OO0O . write ( ooooooO0O )
 OOo0O0oo0OO0O . truncate ( )
 OOo0O0oo0OO0O . close ( )
 O0oooO00ooO0 ( )
 if 99 - 99: o0O00o
def O0oooO00ooO0 ( ) :
 open = i11oO0oOo0 ( OOO0o0 )
 all = IiI111 ( open , '{"num' , 'direct' )
 for oOoO00o in all :
  if '"tv_archive":1' in oOoO00o :
   iiIiii1IIIII = i1ii11I111Ii ( oOoO00o , '"epg_channel_id":"' , '"' )
   OO0OO00ooO0 = i1ii11I111Ii ( oOoO00o , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = i1ii11I111Ii ( oOoO00o , 'stream_id":"' , '"' )
   iiIiii1IIIII = iiIiii1IIIII . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   OoOOoOooooOOo ( iiIiii1IIIII , id , 90027 , OO0OO00ooO0 , ooo0O0o00O , iiIiii1IIIII )
   if 90 - 90: oOOoOooOo - iIII . oO0o + oO0o
   if 45 - 45: OOooOOo / ii . o0O0Oooo0O % o0o00Oo0O * Ii1I * I1ii11iIi11i
def oOO0ooO ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 O00Ooo = open ( i1I1IIiIIi )
 O0Ooooo0 = ElementTree . parse ( O00Ooo )
 OOOOiiI = "apples"
 import datetime as dt
 from datetime import time
 o000Ooo00o00O = datetime . now ( ) - timedelta ( days = 5 )
 I1I1IiIi1 = str ( o000Ooo00o00O )
 O000OO0 = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 ooo0O0O0oo0 = O0Ooooo0 . findall ( "programme" )
 for oo000oO in ooo0O0O0oo0 :
  if name in oo000oO . attrib . get ( 'channel' ) :
   IiIiII11i1 = oo000oO . attrib . get ( 'start' )
   Ii1I1iIiiI1 , o00i111iiIiiIiI , OOooooO = IiIiII11i1 . partition ( ' +' )
   I1I1IiIi1 = str ( I1I1IiIi1 ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   i1I1 , oOoo00 , Ooi1IIii11i1I1 = IiIiII11i1 . partition ( '2017' )
   IIiIi = oo000oO . find ( 'title' ) . text + IiIiII11i1
   Ooi1IIii11i1I1 = Ooi1IIii11i1I1 [ : - 6 ]
   if Ii1I1iIiiI1 > I1I1IiIi1 :
    if Ii1I1iIiiI1 < O000OO0 :
     I1I1IIiiI1 = Ii1I1iIiiI1
     I1I1IIiiI1 = I1I1IIiiI1 [ : 4 ] + '/' + I1I1IIiiI1 [ 4 : ]
     Ii1I1iIiiI1 = Ii1I1iIiiI1 [ : 4 ] + '-' + Ii1I1iIiiI1 [ 4 : ]
     I1I1IIiiI1 = I1I1IIiiI1 [ : 7 ] + '/' + I1I1IIiiI1 [ 7 : ]
     Ii1I1iIiiI1 = Ii1I1iIiiI1 [ : 7 ] + '-' + Ii1I1iIiiI1 [ 7 : ]
     I1I1IIiiI1 = I1I1IIiiI1 [ : 10 ] + ' - ' + I1I1IIiiI1 [ 10 : ]
     Ii1I1iIiiI1 = Ii1I1iIiiI1 [ : 10 ] + ':' + Ii1I1iIiiI1 [ 10 : ]
     I1I1IIiiI1 = I1I1IIiiI1 [ : 15 ] + ':' + I1I1IIiiI1 [ 15 : ]
     Ii1I1iIiiI1 = Ii1I1iIiiI1 [ : 13 ] + '-' + Ii1I1iIiiI1 [ 13 : ]
     I1I1IIiiI1 = I1I1IIiiI1 [ : - 2 ]
     Ii1I1iIiiI1 = Ii1I1iIiiI1 [ : - 2 ]
     oooOOO0o0O0 = ( "http://piesustv" + O00o0OO + ":8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( Ii1I1iIiiI1 ) + "&duration=240" + "&stream=%s" ) % ( O0o0Oo , Oo00OOOOO , id )
     OOOOiiI = oooOOO0o0O0 + str ( Ii1I1iIiiI1 ) + "&duration=240"
     I1I1IIiiI1 = '[COLOR blue]%s - [/COLOR]' % I1I1IIiiI1
     IIiIi = str ( I1I1IIiiI1 ) + oo000oO . find ( 'title' ) . text
     i11II1I11I1 = oo000oO . find ( 'desc' ) . text
     oOOOoo0O0oO ( IIiIi , oooOOO0o0O0 , 222 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , i11II1I11I1 )
def iiiI1IiI ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , O0o0Oo ) . replace ( 'PASSWORD' , Oo00OOOOO )
 Oo0oO = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = o0 )
 Oo0oO . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 Oo0oO . setProperty ( 'IsPlayable' , 'true' )
 Oo0oO . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0oO )
def iII1ii11III ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 Ii111IIIIii = time . time ( )
 urllib . urlretrieve ( url , dest , lambda O00o , Iii1iIIiii1ii , Ii1iii11I : Ii11iIiiI ( O00o , Iii1iIIiii1ii , Ii1iii11I , o0oOoO00o , Ii111IIIIii ) )
def Ii11iIiiI ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  iiII = min ( numblocks * blocksize * 100 / filesize , 100 )
  iII1IiiIIIIii = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  oOOOIii1IiiII1Ii1 = numblocks * blocksize / ( time . time ( ) - start_time )
  if oOOOIii1IiiII1Ii1 > 0 :
   iiiIIi = ( filesize - numblocks * blocksize ) / oOOOIii1IiiII1Ii1
  else :
   iiiIIi = 0
  oOOOIii1IiiII1Ii1 = oOOOIii1IiiII1Ii1 / 1024
  OOoOo0O00oo = oOOOIii1IiiII1Ii1 / 1024
  oo0oO0oOo0O = float ( filesize ) / ( 1024 * 1024 )
  OoOo00 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( iII1IiiIIIIii )
  I1iI1I1I1i11i = '[COLOR white]Speed:  %.02f Mb/s ' % OOoOo0O00oo + '[/COLOR]'
  dp . update ( iiII , OoOo00 , I1iI1I1I1i11i )
 except :
  iiII = 100
  dp . update ( iiII )
 if dp . iscanceled ( ) :
  OOoOoO = xbmcgui . Dialog ( )
  OOoOoO . ok ( "GenieTv" , 'The download was cancelled.' )
  if 72 - 72: OOooOOo / o0O0Oooo0O * o0O00o % iI11I1II1I1I
  sys . exit ( )
  dp . close ( )
  if 53 - 53: oO0o . o0o00Oo0O . oOo0O0Ooo * IIIi11I1 / I11i
def iiIIiI1 ( ) :
 if Oo00OOOOO == 'insert_password' :
  O0OoO000O0OO . ok ( '[COLOR' + II11iiii1Ii + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II11iiii1Ii + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  IIiIIiIIii1i ( )
  if 27 - 27: Ii1i1i
  if 59 - 59: Ii1i1i / IIiIiII11i - o0O00o % OOooOOo % ii
  if 79 - 79: IIIIiiII111 . ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIIi11I1
  if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
  if 54 - 54: oOOoOooOo * IIIIiiII111 * IIIIiiII111 % OOooOOo - IIIi11I1 % Ii1I
  if 44 - 44: I1ii11iIi11i . IIIi11I1 + iIII
  if 22 - 22: o0O0Oooo0O * ii + Ii % oO0o
  if 53 - 53: oOo0O0Ooo
def IIiIIiIIii1i ( ) :
 I1I1IiI1 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/panel_api.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO )
 Ii1i1iI1iIIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( I1I1IiI1 )
 for Oo0o00OO0000 in Ii1i1iI1iIIi :
  dt = datetime . fromtimestamp ( float ( Ii1i1iI1iIIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if O000OO0 <= dt <= O000OO0 + timedelta ( hours = 24 ) :
   O0OoO000O0OO . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II11iiii1Ii + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II11iiii1Ii + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II11iiii1Ii + '] To Purchase A licence[/COLOR]' )
def i1Iii ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '"username":"(.+?)"' ) . findall ( I1I1IiI1 )
 iiI11111II = re . compile ( '"password":"(.+?)"' ) . findall ( I1I1IiI1 )
 I1iiIIIi11 = re . compile ( '"status":"(.+?)"' ) . findall ( I1I1IiI1 )
 I1Ii = re . compile ( '"exp_date":"(.+?)"' ) . findall ( I1I1IiI1 )
 I1i1iii1Ii = re . compile ( '"active_cons":"(.+?)"' ) . findall ( I1I1IiI1 )
 o0oO0OO00ooOO = re . compile ( '"created_at":"(.+?)"' ) . findall ( I1I1IiI1 )
 IiIIiii11II1 = re . compile ( '"max_connections":"(.+?)"' ) . findall ( I1I1IiI1 )
 IiI1Ii1ii = re . compile ( '"is_trial":"1"' ) . findall ( I1I1IiI1 )
 OoOooO = re . compile ( '"is_trial":"0"' ) . findall ( I1I1IiI1 )
 I1ii1i11iI1 = IiOOo0 ( )
 o0O0O0O00o = OoOooOo00o ( )
 for url in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']My GTV Account Information[/COLOR]' , '' , '' , iiiiiIIii + 'MyAcc.png' )
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in iiI11111II :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in I1iiIIIi11 :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in o0oO0OO00ooOO :
  dt = datetime . fromtimestamp ( float ( o0oO0OO00ooOO [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in I1Ii :
  dt = datetime . fromtimestamp ( float ( I1Ii [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if O000OO0 <= dt <= O000OO0 + timedelta ( hours = 24 ) :
   O0O00OOo ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiiiiIIii + 'MyAcc.png' )
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in I1i1iii1Ii :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in IiIIiii11II1 :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in IiI1Ii1ii :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Trial:[/COLOR] Yes' , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in OoOooO :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Trial:[/COLOR] No' , '' , '' , iiiiiIIii + 'MyAcc.png' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Get Short Links[/COLOR]' , '' , 100214 , iiiiiIIii + 'shortlinks.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Local IP Address:[/COLOR] ' + I1ii1i11iI1 , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']External IP Address:[/COLOR] ' + o0O0O0O00o , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 if 28 - 28: Ii1I + Ii1I % OOooOOo
 O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 12 - 12: iIII
def I11iIi1i1I1i1 ( ) :
 O0OoO000O0OO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOOOi11i1 + ")" )
 iiiiii1ii1 ( )
 O0OoO000O0OO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 27 - 27: oOo0O0Ooo - oO0o - ooOO0O0ooOooO
def oOOo0O00o0O0 ( data ) :
 ooOooOooOOO = len ( data ) % 4
 if 59 - 59: iIII
 if 63 - 63: oO0o . ooOO0O0ooOooO + o0O0Oooo0O . OOooOOo / Ii / IIIIiiII111
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + IIIi11I1
 if 31 - 31: Ii1i1i * I11i * Ii1i1i + oO0o * I11i . o0O0Oooo0O
 if 89 - 89: ii * Ii1i1i * oOo0O0Ooo . oOOoOooOo * Ii1i1i / IIIIiiII111
 if 46 - 46: Ii
 if ooOooOooOOO != 0 :
  data += b'=' * ( 4 - ooOooOooOOO )
 return base64 . decodestring ( data )
def i1ii11I111Ii ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : Iiiii = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : Iiiii = ''
 else :
  try : Iiiii = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : Iiiii = ''
 return Iiiii
 if 25 - 25: I1ii11iIi11i * oOo0O0Ooo + IIIi11I1 + o0O0Oooo0O % IIIi11I1
 if 84 - 84: o0o00Oo0O % Ii1i1i . Ii1i1i . IIIIiiII111 * iIII
def IiI111 ( text , start_with , end_with ) :
 Iiiii = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return Iiiii
def IiOOo0 ( ) :
 iIOO0O = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 iIOO0O . connect ( ( '8.8.8.8' , 0 ) )
 iIOO0O = iIOO0O . getsockname ( ) [ 0 ]
 return iIOO0O
 if 34 - 34: Ii1i1i - ooOO0O0ooOooO * ii . oO0o / oOo0O0Ooo
def OoOooOo00o ( ) :
 open = i11oO0oOo0 ( 'http://canyouseeme.org/' )
 I1ii1i11iI1 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( I1ii1i11iI1 . group ( ) )
iII1I = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s' % ( O0o0Oo , Oo00OOOOO )
OOO0o0 = 'http://piesustv' + O00o0OO + ':8000/panel_api.php?username=%s&password=%s' % ( O0o0Oo , Oo00OOOOO )
oO0o0 = 'http://piesustv' + O00o0OO + ':8000/movie/%s/%s/' % ( O0o0Oo , Oo00OOOOO )
i1Ii1i11ii = 'http://piesustv' + O00o0OO + ':8000/live/%s/%s/' % ( O0o0Oo , Oo00OOOOO )
oO0O0oo = '&action=get_live_categories'
OOOOOOO00OO = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( O0o0Oo , Oo00OOOOO )
o00oOOo0Oo = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( O0o0Oo , Oo00OOOOO )
if 68 - 68: oOo0O0Ooo
o0OOoOooO0ooO = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( O0o0Oo , Oo00OOOOO )
O00O = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( O0o0Oo , Oo00OOOOO )
iII = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( O0o0Oo , Oo00OOOOO )
OOo0O = "http://piesustv" + O00o0OO + ":8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( O0o0Oo , Oo00OOOOO )
if 18 - 18: oOo0O0Ooo . Ii1I - I1ii11iIi11i
def Iii1 ( ) :
 IIi11I1i1I1I ( )
 open = i11oO0oOo0 ( iII )
 IiiiIi = IiI111 ( open , '<channel>' , '</channel>' )
 for oOoO00o in IiiiIi :
  iiIiii1IIIII = i1ii11I111Ii ( oOoO00o , '<title>' , '</title>' )
  iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
  OOoooO00o0o = i1ii11I111Ii ( oOoO00o , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OoOOoOooooOOo ( '[COLORsteelblue]' + iiIiii1IIIII + '[/COLOR]' , OOoooO00o0o , 60003 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , '' )
  if 64 - 64: oOOoOooOo / ooOoO0O00 % IIIIiiII111
def OOoOo0O0 ( url ) :
 open = i11oO0oOo0 ( OOo0O + url )
 IiiiIi = IiI111 ( open , '<channel>' , '</channel>' )
 for oOoO00o in IiiiIi :
  iiIiii1IIIII = i1ii11I111Ii ( oOoO00o , '<title>' , '</title>' )
  iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
  xbmc . log ( str ( iiIiii1IIIII ) )
  OO0OO00ooO0 = i1ii11I111Ii ( oOoO00o , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OOoooO00o0o = i1ii11I111Ii ( oOoO00o , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  i11II1I11I1 = i1ii11I111Ii ( oOoO00o , '<description>' , '</description>' )
  i11II1I11I1 = base64 . b64decode ( i11II1I11I1 )
  I1o0 = '('
  I1IiiiiI1i1I = ')'
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , OOoooO00o0o , 222 , OO0OO00ooO0 , ooo0O0o00O , ( '[COLOR' + II11iiii1Ii + ']' + i11II1I11I1 + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( I1IiiiiI1i1I , '[COLORsteelblue]' ) . replace ( I1o0 , '[COLORorangered]' ) )
  if 48 - 48: iIII + IIiIiII11i % ooOO0O0ooOooO % IIIi11I1 * IIiIiII11i
def iiiI1i ( url ) :
 url = url
 oO0000OOo00 = i11oO0oOo0 ( OOOOOOO00OO + url )
 Ii1i1iI1iIIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , type , i11I1 , iiii1i1II1 in Ii1i1iI1iIIi :
  IIi11i = ( i1Ii1i11ii + i11I1 + '.m3u8' ) . strip ( )
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , IIi11i , 222 , ( iiii1i1II1 ) . replace ( '\/' , '/' ) + 'jpg' , iIi1ii1I1 , type )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
def iii11 ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0000OOo00 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/xmltv.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO )
 Ii1i1iI1iIIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for I1ii1Ii1 , OO0oO in Ii1i1iI1iIIi :
  if name == I1ii1Ii1 :
   oOOOoo0O0oO ( ( '' + name + '' ) . replace ( '_' , ' ' ) + OO0oO , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   oOOOoo0O0oO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def i1i11ii ( name ) :
 OOOo0Ooo0 = name
 oO0000OOo00 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/get.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO + '&type=m3u_plus&output=mpegts' )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0000OOo00 )
 for name , iII11 , Oo0o00OO0000 in Ii1i1iI1iIIi :
  Oo0o00OO0000 = ( Oo0o00OO0000 ) . replace ( '.ts' , '.m3u8' )
  oOOOoo0O0oO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Oo0o00OO0000 ) . strip ( ) , 222 , iII11 , iII11 , '' )
 else :
  oOOOoo0O0oO ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 3 - 3: I1ii11iIi11i / oOOoOooOo + oOOoOooOo . Ii1I
  if 50 - 50: iI11I1II1I1I * ooOO0O0ooOooO
  if 85 - 85: ooOoO0O00
  if 100 - 100: ii / iIII % oO0o + Ii1i1i
  if 42 - 42: I1ii11iIi11i / o0O00o . Ii1i1i * oOo0O0Ooo
  if 54 - 54: OOooOOo * IIIIiiII111 + oO0o
  if 93 - 93: I11i / oOo0O0Ooo
  if 47 - 47: I1ii11iIi11i * IIIi11I1
  if 98 - 98: ooOO0O0ooOooO - ooOO0O0ooOooO . oOOoOooOo
  if 60 - 60: oOo0O0Ooo * Ii1I / o0o00Oo0O + iIII + o0O00o
  if 66 - 66: o0O00o * I1ii11iIi11i . ii * o0O0Oooo0O
  if 93 - 93: o0O00o / ooOoO0O00
def oO0oOOoo00000 ( ) :
 OoOOoOooooOOo ( 'Full Backup' , '' , 10061 , iiiiiIIii + 'FullBackUp.png' , iIi1ii1I1 , 'Back Up Your Full System' )
 if os . path . exists ( O00O0oOO00O00 ) :
  OoOOoOooooOOo ( 'Backup Genie Favourites' , Oo0o00OO0000 , 10062 , iiiiiIIii + 'BackupGenieFavourites.png' , iIi1ii1I1 , 'Back Up Your favourites' )
 if os . path . exists ( OOoOO0oo0ooO ) :
  OoOOoOooooOOo ( 'Backup Ivue Config' , OOoOO0oo0ooO , 10062 , iiiiiIIii + 'BackUpIvueConfig.png' , iIi1ii1I1 , 'Back Up Your master.db' )
 if os . path . exists ( O0o0O00Oo0o0 ) :
  OoOOoOooooOOo ( 'Backup Kodi Favourites' , O0o0O00Oo0o0 , 10062 , iiiiiIIii + 'BackKodiFavourites.png' , iIi1ii1I1 , 'Back Up Your favourites.xml' )
  if 47 - 47: oOOoOooOo - Ii1i1i
  if 98 - 98: ooOO0O0ooOooO . o0O0Oooo0O / OOooOOo . oOOoOooOo
  if 1 - 1: IIIi11I1
zip = oo00 . getSetting ( 'zip' )
OoOo0o0OOoO0 = xbmc . translatePath ( os . path . join ( zip ) )
def i1I1IIIiii1 ( ) :
 I1iI = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  O0OoO000O0OO . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 76 - 76: ii
  if 42 - 42: Ii1i1i * o0o00Oo0O / ooOO0O0ooOooO
  if 8 - 8: ooOoO0O00 + IIiIiII11i / Ii1i1i + Ii1I % Ii1i1i - iI11I1II1I1I
def iIi1iI ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = O00O0oOO00O00
  elif 'Ivue' in name :
   url = OOoOO0oo0ooO
  elif 'Kodi' in name :
   url = O0o0O00Oo0o0
  i1I1IIIiii1 ( )
  i11iiIi = open ( url ) . read ( )
  I111I = os . path . join ( OoOo0o0OOoO0 , description . split ( 'Your ' ) [ 1 ] )
  OOo0O0oo0OO0O = open ( I111I , mode = 'w' )
  OOo0O0oo0OO0O . write ( i11iiIi )
  OOo0O0oo0OO0O . close ( )
 else :
  if 'guisettings.xml' in description :
   oOoO00o = open ( os . path . join ( OoOo0o0OOoO0 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iiiii = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   Ii1i1iI1iIIi = re . compile ( Iiiii ) . findall ( oOoO00o )
   for type , oo0oO0 , ii1i1Iii in Ii1i1iI1iIIi :
    ii1i1Iii = ii1i1Iii . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oo0oO0 , ii1i1Iii ) )
  else :
   I111I = os . path . join ( url )
   i11iiIi = open ( os . path . join ( OoOo0o0OOoO0 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOo0O0oo0OO0O = open ( I111I , mode = 'w' )
   OOo0O0oo0OO0O . write ( i11iiIi )
   OOo0O0oo0OO0O . close ( )
 O0OoO000O0OO . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 28 - 28: ooOO0O0ooOooO % OOooOOo + o0O0Oooo0O * IIIIiiII111 * Ii1i1i
 if 53 - 53: IIIi11I1 / I1ii11iIi11i
 if 10 - 10: Ii1I . I11i
 if 75 - 75: o0o00Oo0O * ooOoO0O00 - iIII / IIIi11I1 % IIIi11I1 / OOooOOo
def Iii1i1Ii ( ) :
 III1iIii = 1
 i1I1IIIiii1 ( )
 iiIII1i1 = xbmc . translatePath ( os . path . join ( OoOo0o0OOoO0 , 'Build Backup' , 'Full Backup' , '' ) )
 oOOo0OOoOO0 = xbmc . translatePath ( os . path . join ( OoOo0o0OOoO0 , 'Build Backup' , 'my_full_backup.zip' ) )
 IiIi = xbmc . translatePath ( os . path . join ( OoOo0o0OOoO0 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iiIII1i1 ) :
  os . makedirs ( iiIII1i1 )
 IIi1IiiIi1III = O0OoO000O0OO . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not IIi1IiiIi1III ) : return False , 0
 o00OOoOOO000O0 = IIi1IiiIi1III
 IiIiIiiIIii = xbmc . translatePath ( os . path . join ( iiIII1i1 , o00OOoOOO000O0 + '.zip' ) )
 OOo00O00o0O0 = [ 'plugin.video.GenieTv' ]
 iI1III = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 I1I111 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1iIIIiiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 ooO0 = "Creating full backup of existing build"
 IIOoOOoOo = "Creating Community Build"
 Ii1Iiiiii = "Archiving..."
 IiIii1i11i1 = ""
 ooOOo00o0ooO = "Please Wait"
 iIOO ( oOo0oooo00o , IiIiIiiIIii , IIOoOOoOo , Ii1Iiiiii , IiIii1i11i1 , ooOOo00o0ooO , I1I111 , I1iIIIiiI )
 time . sleep ( 1 )
 I1III1I11I1 = xbmc . translatePath ( os . path . join ( iiIII1i1 , o00OOoOOO000O0 + '_guisettings.zip' ) )
 oO000OoO00OoO = zipfile . ZipFile ( I1III1I11I1 , mode = 'w' )
 try :
  oO000OoO00OoO . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oO000OoO00OoO . close ( )
 if III1iIii == 0 :
  O0OoO000O0OO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  O0OoO000O0OO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  O0OoO000O0OO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oOOo0OOoOO0 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IiIiIiiIIii + '[/COLOR]' )
  if 34 - 34: IIIIiiII111 % Ii + Ii - IIIIiiII111
def iIOO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iii1iII = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 O00o0o = len ( sourcefile )
 i11I1iiii = [ ]
 i1iIi = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for oOO00OOOoO0o , Ii1iII1ii1 , ooOo0 in os . walk ( sourcefile ) :
  for file in ooOo0 :
   i1iIi . append ( file )
 I11I1i = len ( i1iIi )
 for oOO00OOOoO0o , Ii1iII1ii1 , ooOo0 in os . walk ( sourcefile ) :
  Ii1iII1ii1 [ : ] = [ oOO0oOooo for oOO0oOooo in Ii1iII1ii1 if oOO0oOooo not in exclude_dirs ]
  ooOo0 [ : ] = [ OOo0O0oo0OO0O for OOo0O0oo0OO0O in ooOo0 if OOo0O0oo0OO0O not in exclude_files ]
  for file in ooOo0 :
   i11I1iiii . append ( file )
   o00IIIIii1111i1 = len ( i11I1iiii ) / float ( I11I1i ) * 100
   o0oOoO00o . update ( int ( o00IIIIii1111i1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iiI1ii1 = os . path . join ( oOO00OOOoO0o , file )
   if not 'temp' in Ii1iII1ii1 :
    if not 'plugin.program.originwizard' in Ii1iII1ii1 :
     import time
     I1oOOoo0 = '01/01/1980'
     II1OOO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iiI1ii1 ) ) )
     if II1OOO > I1oOOoo0 :
      iii1iII . write ( iiI1ii1 , iiI1ii1 [ O00o0o : ] )
 iii1iII . close ( )
 o0oOoO00o . close ( )
 if 32 - 32: iI11I1II1I1I * I1ii11iIi11i - ooOO0O0ooOooO
 if 72 - 72: o0O00o % ooOoO0O00 / iI11I1II1I1I
def ooIii ( ) :
 OOooOoooOoOo ( )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiiiiIIii + 'scoob.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiiiiIIii + 'scoob.png' , iIi1ii1I1 , '' )
 if 66 - 66: IIIi11I1 * I11i
 if 58 - 58: iI11I1II1I1I % IIIi11I1 + o0O0Oooo0O - o0O0Oooo0O . Ii + ii
def i1iIII1IIi ( ) :
 OOooOoooOoOo ( )
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SEARCH YOUTUBE[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Search Genie[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  O0Oo00oO0O00 ( )
 if OoOOo0OOoO == 1 :
  O0O0o0o0o ( )
 if OoOOo0OOoO == 2 :
  Oo0oo0OOO0OOoOO ( )
 if OoOOo0OOoO == 3 :
  o00oo ( )
  if 97 - 97: ooOoO0O00
  if 46 - 46: Ii1I
  if 30 - 30: oO0o / o0o00Oo0O * I11i * o0O0Oooo0O + ii * IIIIiiII111
  if 23 - 23: iIII
  if 36 - 36: o0O00o . IIIIiiII111 - ooOoO0O00 + o0O0Oooo0O
  if 54 - 54: ii . ooOO0O0ooOooO - IIIIiiII111
  if 76 - 76: o0O0Oooo0O
  if 61 - 61: oOOoOooOo / IIiIiII11i * oOOoOooOo * OOooOOo * o0O0Oooo0O . Ii
  if 26 - 26: o0O0Oooo0O / oOOoOooOo - oO0o . iI11I1II1I1I
def O0o0OOo0o0o ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']RaysRavers Radio[/COLOR]' , '[COLOR' + II11iiii1Ii + ']ThunderStruck[/COLOR]' , '[COLOR' + II11iiii1Ii + ']RadioNomy[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']UK RADIO[/COLOR]' , '[COLOR' + II11iiii1Ii + ']WORLD RADIO[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CONCERTS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC SEARCH[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Music[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if OoOOo0OOoO == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if OoOOo0OOoO == 2 :
   o0oO00oooo ( )
  if OoOOo0OOoO == 3 :
   ooo0Oo00O ( )
  if OoOOo0OOoO == 4 :
   I1iII1 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if OoOOo0OOoO == 5 :
   Ooo0OOO0O00 ( )
  if OoOOo0OOoO == 6 :
   Ii1iiII11ii1 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if OoOOo0OOoO == 7 :
   iIi11I1II ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if OoOOo0OOoO == 8 :
   oO00Oo0O0 ( str ( iI1iIIiiii ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if OoOOo0OOoO == 9 :
   o0O00O ( )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']RaysRavers Radio[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , iiiiiIIii + 'Rays-Ravers.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']ThunderStruck[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , iiiiiIIii + 'Thunder.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']RadioNomy[/COLOR]' , '' , 70001 , iiiiiIIii + 'RadioNomy.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MUSIC CHANNELS[/COLOR]' , str ( iI1iIIiiii ) , 30031 , iiiiiIIii + 'MusicChannels.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiiiiIIii + 'UKRadio.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']WORLD RADIO[/COLOR]' , str ( iI1iIIiiii ) , 1013 , iiiiiIIii + 'WorldRadio.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiiiiIIii + 'Concerts.png' , iIi1ii1I1 , '' )
   if 53 - 53: ooOO0O0ooOooO % IIIi11I1 % Ii1I . o0O0Oooo0O . o0O0Oooo0O . IIIIiiII111
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiiiiIIii + 'MusicVideos.png' , iIi1ii1I1 , '' )
  if 73 - 73: IIIIiiII111 / oOOoOooOo + oO0o / OOooOOo . IIiIiII11i * Ii1i1i
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MUSIC SEARCH[/COLOR]' , str ( iI1iIIiiii ) , 1111 , iiiiiIIii + 'MusicSearch.png' , iIi1ii1I1 , '' )
  if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + IIIIiiII111 % oOo0O0Ooo * ooOO0O0ooOooO
  if 74 - 74: IIIIiiII111 / iIII . oOo0O0Ooo - ii + IIiIiII11i + iIII
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
o0OoOO = 'white'
O0O0Oo00 = 'gold'
def I11iiI11I1II ( ) :
 OOooOoooOoOo ( )
 if OOoOooOoOOOoo ( True ) == False : oO0iII1i111iI = 0
 else : oO0iII1i111iI = iiI ( OOoOooOoOOOoo ( True ) , True , True )
 if OOoOooOoOOOoo ( True , True ) == False : IiI1iI1 = 0
 else : IiI1iI1 = iiI ( OOoOooOoOOOoo ( True , True ) , True , True )
 oOooi1IIII1II = int ( oO0iII1i111iI ) + int ( IiI1iI1 )
 O000oO00oO = str ( oOooi1IIII1II ) + ' Error(s) Found' if oOooi1IIII1II > 0 else 'None Found'
 o0oOo00OOo0O = ': [COLORsteelblue]Not Found[/COLOR]' if not os . path . exists ( oO ) else ": [COLORorangered]%s[/COLOR]" % OO0OOoOOO ( os . path . getsize ( oO ) )
 oOoO0o0o = O00O000oOO0oO ( i1iIIi1 )
 OO0i1Ii1II11 = O00O000oOO0oO ( ii11iIi1I )
 IiiIIii1I1I = IIi ( )
 IIiIi1II1IiI = oOoO0o0o + OO0i1Ii1II11 + IiiIIii1I1I
 I1ii1i11iI1 = IiOOo0 ( )
 o0O0O0O00o = OoOooOo00o ( )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']CLEAN UP:[COLORorangered] [B]%s[/B][/COLOR]' % OO0OOoOOO ( IIiIi1II1IiI ) , 'url' , 9666 , iiiiiIIii + 'MAIN5.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']KILL KODI[/COLOR]' , '' , 80000 , iiiiiIIii + 'KillKodi.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']SPEEDTEST[/COLOR]' , '' , 50004 , iiiiiIIii + 'Speedtest.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']VIEW LOG Errors:[COLORorangered] %s[/COLOR]' % ( O000oO00oO ) , '' , 219999990 , iiiiiIIii + 'View-Log-File.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , iiiiiIIii + 'View-Log-File.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']CLEAR LOG FILES: [COLORorangered]' + o0oOo00OOo0O + '[/COLOR]' , '' , 219999991 , iiiiiIIii + 'View-Log-File.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']DELETE CACHE:[COLORorangered] [B]%s[/B][/COLOR]' % OO0OOoOOO ( IiiIIii1I1I ) , 'url' , 14 , iiiiiIIii + 'DeleteCache.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']DELETE PACKAGES:[COLORorangered] [B]%s[/B][/COLOR]' % OO0OOoOOO ( oOoO0o0o ) , 'url' , 6 , iiiiiIIii + 'DeletePackages.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']FORCE REFRESH[/COLOR]' , 'url' , 10 , iiiiiIIii + 'ForceRefresh.png' , iIi1ii1I1 , 'Force Refresh All Repos' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']LAST RESORT FIX EMPTY REPOS[/COLOR]' , 'url' , 9 , iiiiiIIii + '1.jpg' , iIi1ii1I1 , 'Fix Corrupt Database' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']CLEAR THUBMNAILS:[COLORorangered] [B]%s[/B][/COLOR]' % OO0OOoOOO ( OO0i1Ii1II11 ) , 'url' , 219999992 , iiiiiIIii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , iIi1ii1I1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Local IP Address:[COLORorangered] ' + I1ii1i11iI1 + '[/COLOR] ' , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']External IP Address:[COLORorangered] ' + o0O0O0O00o + '[/COLOR] ' , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 if 99 - 99: I1ii11iIi11i
 if 17 - 17: Ii - Ii + Ii1I * oOOoOooOo * ooOO0O0ooOooO / ii
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def i1II111ii1ii ( proc ) :
 xbmc . executebuiltin ( proc )
 if 54 - 54: IIIIiiII111 * IIiIiII11i / ii + o0O0Oooo0O - ooOO0O0ooOooO + oOOoOooOo
def OOOOoOOOo0oOO ( ) :
 i1II111ii1ii ( 'Container.Refresh()' )
def O000oOOoOOO ( ) :
 OOo0O0oo0OO0O = open ( oO , 'w' ) ; OOo0O0oo0OO0O . close ( ) ; o0Oooo ( "[COLOR %s]%s[/COLOR]" % ( o0OoOO , i1iiIIiiI111 ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % O0O0Oo00 )
 OOOOoOOOo0oOO ( )
 if 40 - 40: oOo0O0Ooo / ii + oO0o * oO0o
def iIII11Ii1iI1II ( type = None ) :
 OoI1 = OoO00o00 ( 'Textures' )
 if not type == None : OoOOo0OOoO = 1
 else : OoOOo0OOoO = O0OoO000O0OO . yesno ( i1iiIIiiI111 , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( O0O0Oo00 , OoI1 ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if OoOOo0OOoO == 1 :
  try : ooOo ( os . join ( iI111I11I1I1 , OoI1 ) )
  except : o0oo00000O ( 'Failed to delete, Purging DB.' ) ; oo0 ( OoI1 )
  o0Oo00o0 ( ii11iIi1I )
  if 42 - 42: o0O0Oooo0O / OOooOOo % ooOO0O0ooOooO
 else : o0oo00000O ( 'Clear thumbnames cancelled' )
 oOOoOo0Ooo ( )
 if 95 - 95: o0O0Oooo0O % I1ii11iIi11i
 if 54 - 54: iI11I1II1I1I - iI11I1II1I1I
def oOOoOo0Ooo ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 OOOo0Ooo0o00o = '0123456789abcdef'
 oOoOooO = os . path . join ( ii11iIi1I , 'Video' , 'Bookmarks' )
 for IIi1IIIi in OOOo0Ooo0o00o :
  o0OoOOoooooOO = os . path . join ( ii11iIi1I , IIi1IIIi )
  if not os . path . exists ( o0OoOOoooooOO ) : os . makedirs ( o0OoOOoooooOO )
 if not os . path . exists ( oOoOooO ) : os . makedirs ( oOoOooO )
 if 88 - 88: ooOoO0O00
def OoO00o00 ( DB ) :
 if DB in [ 'Addons' , 'ADSP' , 'Epg' , 'MyMusic' , 'MyVideos' , 'Textures' , 'TV' , 'ViewModes' ] :
  Ii1i1iI1iIIi = glob . glob ( os . path . join ( iI111I11I1I1 , '%s*.db' % DB ) )
  O0ooOo0Oooo = '%s(.+?).db' % DB [ 1 : ]
  I1iiIIiI11I = 0
  for file in Ii1i1iI1iIIi :
   try : I11II1I = int ( re . compile ( O0ooOo0Oooo ) . findall ( file ) [ 0 ] )
   except : I11II1I = 0
   if I1iiIIiI11I < I11II1I :
    I1iiIIiI11I = I11II1I
  return '%s%s.db' % ( DB , I1iiIIiI11I )
 else : return False
 if 92 - 92: I11i
def o0Oo00o0 ( path ) :
 o0oo00000O ( "Deleting Folder: %s" % path , xbmc . LOGNOTICE )
 try : shutil . rmtree ( path , ignore_errors = True , onerror = None )
 except : return False
 if 37 - 37: ooOO0O0ooOooO
def oo0 ( name ) :
 if 18 - 18: o0O00o * Ii + iI11I1II1I1I % iIII + ooOoO0O00 - oO0o
 if 85 - 85: oO0o * iIII + oO0o
 if 39 - 39: I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
 o0oo00000O ( 'Purging DB %s.' % name , xbmc . LOGNOTICE )
 if os . path . exists ( name ) :
  try :
   iII1I1IIiiiI = database . connect ( name )
   IIiiIiIIiI1 = iII1I1IIiiiI . cursor ( )
  except Exception , I1iI1I1I1i11i :
   o0oo00000O ( "DB Connection Error: %s" % str ( I1iI1I1I1i11i ) , xbmc . LOGERROR )
   return False
 else : o0oo00000O ( '%s not found.' % name , xbmc . LOGERROR ) ; return False
 IIiiIiIIiI1 . execute ( "SELECT name FROM sqlite_master WHERE type = 'table'" )
 for I1IiI in IIiiIiIIiI1 . fetchall ( ) :
  if I1IiI [ 0 ] == 'version' :
   o0oo00000O ( 'Data from table `%s` skipped.' % I1IiI [ 0 ] , xbmc . LOGDEBUG )
  else :
   try :
    IIiiIiIIiI1 . execute ( "DELETE FROM %s" % I1IiI [ 0 ] )
    iII1I1IIiiiI . commit ( )
    o0oo00000O ( 'Data from table `%s` cleared.' % I1IiI [ 0 ] , xbmc . LOGDEBUG )
   except Exception , I1iI1I1I1i11i : o0oo00000O ( "DB Remove Table `%s` Error: %s" % ( I1IiI [ 0 ] , str ( I1iI1I1I1i11i ) ) , xbmc . LOGERROR )
 IIiiIiIIiI1 . close ( )
 o0oo00000O ( '%s DB Purging Complete.' % name , xbmc . LOGNOTICE )
 OO0oO = name . replace ( '\\' , '/' ) . split ( '/' )
 o0Oooo ( "[COLOR %s]Purge Database[/COLOR]" % o0OoOO , "[COLOR %s]%s Complete[/COLOR]" % ( O0O0Oo00 , OO0oO [ len ( OO0oO ) - 1 ] ) )
 if 79 - 79: OOooOOo + o0O00o
def ooOo ( path ) :
 o0oo00000O ( "Deleting File: %s" % path , xbmc . LOGNOTICE )
 try : os . remove ( path )
 except : return False
 if 14 - 14: o0O0Oooo0O / iIII - IIIi11I1 * o0o00Oo0O % o0O00o . o0o00Oo0O
 if 86 - 86: ooOoO0O00 * ii
def IIi ( ) :
 I1I1I1 = os . path . join ( oooOOOOO , 'addon_data' )
 i1iIIIiI = [
 ( os . path . join ( oo0o0O00 , 'plugin.video.phstreams' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.bob' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.specto' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.genesis' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.exodus' , 'cache.db' ) ) ,
 ( os . path . join ( iI111I11I1I1 , 'onechannelcache.db' ) ) ,
 ( os . path . join ( iI111I11I1I1 , 'saltscache.db' ) ) ,
 ( os . path . join ( iI111I11I1I1 , 'saltshd.lite.db' ) ) ]
 I11IiI1iII = [
 ( I1I1I1 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( I1I1I1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1I1I1 , 'plugin.video.itv' , 'Images' ) ) ]
 if 18 - 18: IIIi11I1
 IIiIi1II1IiI = 0
 if 82 - 82: ii - oOOoOooOo * Ii1I * oOOoOooOo * o0o00Oo0O * iI11I1II1I1I
 for IIi1IIIi in I11IiI1iII :
  if os . path . exists ( IIi1IIIi ) and not IIi1IIIi in [ oo0o0O00 , I1I1I1 ] :
   IIiIi1II1IiI = O00O000oOO0oO ( IIi1IIIi , IIiIi1II1IiI )
  else :
   for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( IIi1IIIi ) :
    for oOO0oOooo in Ii1iII1ii1 :
     if 'cache' in oOO0oOooo . lower ( ) and not oOO0oOooo . lower ( ) == 'meta_cache' : IIiIi1II1IiI = O00O000oOO0oO ( os . path . join ( i11O00oO , oOO0oOooo ) , IIiIi1II1IiI )
     if 80 - 80: o0O00o
 return IIiIi1II1IiI
def O00O000oOO0oO ( path , total = 0 ) :
 for iiiI1I1iiiII , IIiIi1I1iI1 , I1oo in os . walk ( path ) :
  for OOo0O0oo0OO0O in I1oo :
   i1I111II11 = os . path . join ( iiiI1I1iiiII , OOo0O0oo0OO0O )
   total += os . path . getsize ( i1I111II11 )
 return total
def OO0OOoOOO ( num , suffix = 'B' ) :
 for o00oO in [ '' , 'K' , 'M' , 'G' ] :
  if abs ( num ) < 1024.0 :
   return "%3.02f %s%s" % ( num , o00oO , suffix )
  num /= 1024.0
 return "%.02f %s%s" % ( num , 'G' , suffix )
 if 32 - 32: IIIIiiII111 . iI11I1II1I1I % I1ii11iIi11i . ii
def i1i1II ( ) :
 OOooOoooOoOo ( )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iiiiiIIii + 'repos.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NEW[/COLOR]' , str ( iI1iIIiiii ) , 22 , iiiiiIIii + 'NEW.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']IPTV[/COLOR]' , str ( iI1iIIiiii ) , 23 , iiiiiIIii + 'IPTV.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']VIDEO[/COLOR]' , str ( iI1iIIiiii ) , 24 , iiiiiIIii + 'VIDEO.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SPORTS[/COLOR]' , str ( iI1iIIiiii ) , 25 , iiiiiIIii + 'SPORTS.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']KIDS[/COLOR]' , str ( iI1iIIiiii ) , 26 , iiiiiIIii + 'KIDS.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MUSIC[/COLOR]' , str ( iI1iIIiiii ) , 27 , iiiiiIIii + 'MUSIC.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']PROGRAMS[/COLOR]' , str ( iI1iIIiiii ) , 28 , iiiiiIIii + 'PROGRAMS.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']XXX[/COLOR]' , 'URL' , 29 , iiiiiIIii + 'XXX.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 81 - 81: Ii * IIIIiiII111 . ooOO0O0ooOooO * ooOO0O0ooOooO . o0O00o
 if 47 - 47: iI11I1II1I1I % iIII . iIII / o0o00Oo0O . Ii * Ii1i1i
def iio0Oo ( ) :
 OOooOoooOoOo ( )
 oOOOoo0O0oO ( 'CHECK ADVANCED XML' , str ( iI1iIIiiii ) , 8 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'MUCKYS XML' , str ( iI1iIIiiii ) + '/wizard/muckys.xml' , 7 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '0CACHE XML' , str ( iI1iIIiiii ) + '/wizard/0cache.xml' , 7 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'MIKEY1234 XML' , str ( iI1iIIiiii ) + '/wizard/mikey.xml' , 7 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'TUXENS XML' , str ( iI1iIIiiii ) + '/wizard/tuxens.xml' , 7 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'P2P RECOMMENDED XML1' , str ( iI1iIIiiii ) + '/wizard/p2p1.xml' , 7 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'P2P RECOMMENDED XML2' , str ( iI1iIIiiii ) + '/wizard/p2p2.xml' , 7 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'DELETE XML' , str ( iI1iIIiiii ) , 11 , iiiiiIIii + 'XML.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 29 - 29: o0o00Oo0O * Ii / ii / I11i . oOOoOooOo
def oOo00 ( ) :
 OOooOoooOoOo ( )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']My Local Zip[/COLOR]' , II , 48 , iiiiiIIii + 'MyLocalZIP.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']My Online Zip[/COLOR]' , iiI1IiI , 43 , iiiiiIIii + 'MyOnlineZip.png' , iIi1ii1I1 , '' )
 if 70 - 70: ii . oOOoOooOo / ooOO0O0ooOooO . ooOO0O0ooOooO - I11i
def i1II1i1iiI1 ( ) :
 OOooOoooOoOo ( )
 oOOOoo0O0oO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( iI1iIIiiii ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiiiiIIii + 'FTV4.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( iI1iIIiiii ) + '/wizard/customftv/settings.xml' , 17 , iiiiiIIii + 'FTV3.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiiiiIIii + 'FTV1.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'RESET FTV DATABASE' , 'url' , 18 , iiiiiIIii + 'FTV2.png' , iIi1ii1I1 , '' )
 if 62 - 62: Ii1i1i . Ii % o0o00Oo0O % o0O0Oooo0O - I1ii11iIi11i
 if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % Ii1i1i + oOo0O0Ooo
 if 100 - 100: Ii - I1ii11iIi11i
def i11I1Ii1Iiii1 ( ) :
 OOooOoooOoOo ( )
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SKINS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  o0oooOoOoOo ( )
 if OoOOo0OOoO == 0 :
  OO0O ( Oo0o00OO0000 )
 if OoOOo0OOoO == 0 :
  oo0ooOoo00Ooo ( Oo0o00OO0000 )
  if 16 - 16: oO0o % iI11I1II1I1I . iIII / IIIIiiII111
  if 87 - 87: o0o00Oo0O * oO0o + ooOoO0O00
  if 33 - 33: oOo0O0Ooo * o0O0Oooo0O
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . oOOoOooOo - ooOoO0O00
def oOOoOo0OoOO ( ) :
 I1I1IiI1 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 Ii1i1iI1iIIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( I1I1IiI1 )
 for iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iII11 , iII11 , '' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 90 - 90: oO0o / Ii1i1i % iI11I1II1I1I / o0o00Oo0O * ooOO0O0ooOooO / oOo0O0Ooo
def oooO0O0Oo00 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( I1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 27 - 27: Ii
def o0oooOoOoOo ( ) :
 OOooOoooOoOo ( )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']GOTHAM SKINS[/COLOR]' , str ( iI1iIIiiii ) , 36 , iiiiiIIii + 'GothamSkins.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']HELIX SKINS[/COLOR]' , str ( iI1iIIiiii ) , 37 , iiiiiIIii + 'HelixSkins.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiiiiIIii + 'IsengaardSkins.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 66 - 66: OOooOOo . iI11I1II1I1I * Ii1I - Ii1i1i - iI11I1II1I1I
def iIii1i1IIi ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + ooo0oo00O00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 73 - 73: ooOO0O0ooOooO - oOo0O0Ooo + Ii * IIiIiII11i
def Oo0ooooO0o00 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + iIIIIIi11Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 92 - 92: ooOO0O0ooOooO / Ii1I
def Iiii ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + Ii11i1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 70 - 70: Ii1I . Ii1I / iIII . Ii1I
def IiIOOOoo ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 61 - 61: IIiIiII11i / IIiIiII11i . Ii
def OO0O ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + OOoo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 40 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 58 - 58: IIIi11I1 % IIIIiiII111 * o0o00Oo0O + Ii1I - o0O00o
def IiiII ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + OO00OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / iIII + oOOoOooOo
def ooO0O00Oo0o ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']GenieTv Apps[/COLOR]' , '[COLOR' + II11iiii1Ii + ']APK Factory[/COLOR]' , '[COLOR' + II11iiii1Ii + ']APK Search[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']APK TOOL[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  i11IiIiii ( )
 if OoOOo0OOoO == 1 :
  i11iI1111ii1I ( )
 if OoOOo0OOoO == 2 :
  OoOo0 ( )
  if 22 - 22: Ii + OOooOOo + ii
  if 2 - 2: oOOoOooOo - iIII * ooOoO0O00 % IIIi11I1 / ii * IIIi11I1
  if 82 - 82: Ii1I . Ii1I * Ii1i1i % iIII % o0o00Oo0O / I1ii11iIi11i
  if 83 - 83: o0O0Oooo0O + I11i % ooOO0O0ooOooO / oO0o
def i11iI1111ii1I ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , o0o000O0ooo0O in Ii1i1iI1iIIi :
  iI ( 'Android Apps' + o0o000O0ooo0O , 'https://www.apkfiles.com' + Oo0o00OO0000 , 30035 , iiiiiIIii + 'apps.png' )
 for Oo0o00OO0000 , o0o000O0ooo0O in I1Ii :
  iI ( 'Android Games' + o0o000O0ooo0O , 'https://www.apkfiles.com' + Oo0o00OO0000 , 30035 , iiiiiIIii + 'GAMES.png' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def I1I11iII11 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '/cat' in url :
   iI ( ( iiIiii1IIIII ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiiiiIIii + 'APK.png' )
def O0O000OOOoO ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '/app' in url :
   iI ( ( iiIiii1IIIII ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiiiiIIii + 'APK.png' )
def O0Oo0O0O0o ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 OOoooO00o0o = url
 if "page=" in str ( url ) :
  OOoooO00o0o = url . split ( '?' ) [ 0 ]
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'apk' in url :
   oOOOoo0O0oO ( ( iiIiii1IIIII ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + iII11 )
 if len ( I1Ii ) > 1 :
  I1Ii = str ( I1Ii [ len ( I1Ii ) - 1 ] )
 oOOOoo0O0oO ( 'Next Page' , OOoooO00o0o + str ( I1Ii ) , 30037 , iiiiiIIii + 'Next.png' )
def iiII11ii1Ii ( name , url ) :
 O0o0O0 = iii1 ( url )
 name = name
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  url = 'https://www.apkfiles.com' + url
  iiI1Ii1iiii1i ( name , url , 'Brackets' )
def OoOo0 ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'https://www.apkfiles.com/search?q=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' ) + '&search_type=1'
 i11ii = IiiI . lower ( )
 O0Oo0O0O0o ( i11ii )
 if 26 - 26: I1ii11iIi11i + IIIi11I1 + I1ii11iIi11i / oO0o / OOooOOo - ooOO0O0ooOooO
def iiIIIi1II1IiiI ( url ) :
 I1iI = xbmc . translatePath ( os . path . join ( oo000O0o , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IIIIiIiIi1 = os . path . join ( I1iI , iiIiii1IIIII + '.apk' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 99 - 99: oOo0O0Ooo
def OOoo ( url ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IIIIiIiIi1 = os . path . join ( I1iI , iiIiii1IIIII + '.mp4' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 87 - 87: oO0o * OOooOOo - I1ii11iIi11i % IIIi11I1 * Ii
 if 59 - 59: o0O0Oooo0O + ii / oOo0O0Ooo / ii . IIIIiiII111
def i1OooO00oO00o ( name , url , description ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IIIIiIiIi1 = os . path . join ( I1iI , name )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 IIII1iI1IiIiI = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIII1iI1IiIiI
 print '======================================='
 extract . all ( IIIIiIiIi1 , IIII1iI1IiIiI , o0oOoO00o )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 43 - 43: IIiIiII11i
 if 95 - 95: o0O0Oooo0O + o0O00o * iI11I1II1I1I
 if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / Ii1i1i
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . iIII
 if 2 - 2: Ii1i1i
def i11IiIiii ( ) :
 I1I1IiI1 = i11oO0oOo0 ( iIii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , Oo0o00OO0000 , iiii1i1II1 , ooo0O0o00O , Ii1i111iI in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , Oo0o00OO0000 , 80003 , iiii1i1II1 , iiiiiIIii + 'APKToolsB.png' , Ii1i111iI )
def iII1ii ( apk , ret = None ) :
 if apk == "kodi" :
  OOO00OiI = "https://kodi.tv/download/"
  I1I1IiI1 = i11oO0oOo0 ( OOO00OiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  Ii1i1iI1iIIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( I1I1IiI1 )
  if len ( Ii1i1iI1iIIi ) == 1 :
   O0o00oO00O0 = Ii1i1iI1iIIi [ 0 ] [ 0 ]
   o00OOoOOO000O0 = Ii1i1iI1iIIi [ 0 ] [ 1 ]
   I1Iii = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( O0o00oO00O0 , o00OOoOOO000O0 )
  if ret == 'version' : return O0o00oO00O0
  else : return I1Iii
 elif apk == "spmc" :
  IIIi1iIii1II11 = 'https://github.com/koying/SPMC/releases/latest/'
  I1I1IiI1 = i11oO0oOo0 ( IIIi1iIii1II11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  Ii1i1iI1iIIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( I1I1IiI1 )
  O0o00oO00O0 = re . sub ( '<[^<]+?>' , '' , Ii1i1iI1iIIi [ 0 ] ) . replace ( ' ' , '' )
  I1Iii = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( O0o00oO00O0 , O0o00oO00O0 )
  if ret == 'version' : return O0o00oO00O0
  else : return I1Iii
def iiI1Ii1iiii1i ( name , url , Brackets ) :
 if iIII1I111III ( ) == 'android' :
  OOOOoOOOO = O0OoO000O0OO . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OOOOoOOOO : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iiIi1 = name
  if OOOOoOOOO :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not oOo00O000Oo0 ( url ) == True : o0Oooo ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iiIi1 , '' , 'Please Wait' )
   IIIIiIiIi1 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( IIIIiIiIi1 )
   except : pass
   downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oO000OoO00OoO = zipfile . ZipFile ( IIIIiIiIi1 )
    for file in oO000OoO00OoO . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as OOo0O0oo0OO0O :
       Oo0OOo = file . split ( '/' ) [ 1 ]
       OOo0O0oo0OO0O . write ( oO000OoO00OoO . read ( file ) )
       xbmc . sleep ( 500 )
       OOo0O0oo0OO0O . close ( )
       try :
        os . remove ( IIIIiIiIi1 )
       except :
        pass
       IIIIiIiIi1 = os . path . join ( i1iIIi1 , Oo0OOo )
   O0OoO000O0OO . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IIIIiIiIi1 + '")' )
  else : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 43 - 43: o0O00o % Ii1i1i . IIIi11I1 / I1ii11iIi11i
 if 55 - 55: Ii1I % ii
 if 73 - 73: ooOoO0O00 - IIIIiiII111 % ooOO0O0ooOooO / ooOoO0O00 + IIiIiII11i + Ii1I
 if 54 - 54: ooOO0O0ooOooO
def I1ii11I1IiI ( ) :
 if not os . path . exists ( OOooO0OOoo ) : os . makedirs ( OOooO0OOoo )
 I1I1IiI1 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( I1I1IiI1 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  Oo0o00OO0000 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + Oo0o00OO0000 )
  i1IIIii ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) , Oo0o00OO0000 )
  if 37 - 37: IIIIiiII111 . I11i / Ii1i1i / IIIi11I1 * ooOoO0O00
def i1IIIii ( name , url ) :
 if iIII1I111III ( ) == 'android' :
  OOOOoOOOO = O0OoO000O0OO . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OOOOoOOOO : o0Oooo ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iiIi1 = name
  if OOOOoOOOO :
   if not os . path . exists ( OOooO0OOoo ) : os . makedirs ( OOooO0OOoo )
   if not oOo00O000Oo0 ( url ) == True : o0Oooo ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iiIi1 , '' , 'Please Wait' )
   IIIIiIiIi1 = os . path . join ( OOooO0OOoo , "%s.apk" % name )
   try : os . remove ( IIIIiIiIi1 )
   except : pass
   downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   O0OoO000O0OO . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IIIIiIiIi1 + '")' )
  else : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + ooOO0O0ooOooO
 if 58 - 58: IIIIiiII111 - ii
def o00oO00 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( iI1iIIiiii + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'INFO' )
 if 27 - 27: IIIIiiII111 . OOooOOo / ii
 if 18 - 18: ooOoO0O00 . oOo0O0Ooo
def iI1 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( iI1iIIiiii + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 30015 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 58 - 58: ooOoO0O00 + o0o00Oo0O . oO0o % iIII
def IIi1I1 ( url , iconimage , fanart ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ooo0 = url
 iII11 = iconimage
 fanart = fanart
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( I1I1IiI1 )
 for i11I1 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '.mp4' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Watch VIDEO' , url + '/' + i11I1 , 222 , iII11 , fanart , '' )
  if 'description' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Read Description' , url + '/' + i11I1 , 30017 , iII11 , fanart , '' )
  if 'images' in iiIiii1IIIII :
   OoOOoOooooOOo ( 'View Images' , url + '/' + i11I1 , 30018 , iII11 , fanart , '' )
  if 'url' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Install Build On Android' , url + '/' + i11I1 , 30016 , iII11 , fanart , '' )
  if 'url' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Install Build On Pc' , url + '/' + i11I1 , 30019 , iII11 , fanart , '' )
 OOoOO0o0o0 ( 'movies' , 'INFO' )
 if 53 - 53: ooOO0O0ooOooO + IIIIiiII111
def oO0O0ooOoo ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'url="([^"]*)"' ) . findall ( I1I1IiI1 )
 for url in Ii1i1iI1iIIi :
  Ii1i1I1 ( url )
  if 39 - 39: OOooOOo + o0O0Oooo0O % o0o00Oo0O
def i1Ii1I ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'url="([^"]*)"' ) . findall ( I1I1IiI1 )
 for url in Ii1i1iI1iIIi :
  O0O0o0o0oo0O ( url )
  if 30 - 30: o0O0Oooo0O / oOo0O0Ooo / ooOoO0O00 - o0o00Oo0O . Ii1i1i - oOOoOooOo
def o00o0o0o ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'desc="([^"]*)"' ) . findall ( I1I1IiI1 )
 for i111I1 in Ii1i1iI1iIIi :
  I1iI1ii1II ( 'Description:' , i111I1 )
  if 11 - 11: iI11I1II1I1I / Ii1i1i + ii % ooOoO0O00 * Ii
def OoOooooo ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 url = url
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1I1IiI1 )
 for i11I1 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'png' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'image' , '' , '' , url + '/' + i11I1 , url + '/' + i11I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . Ii1i1i - I1ii11iIi11i . Ii
def IIIII11II1 ( name , url , description ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IIIIiIiIi1 = os . path . join ( I1iI , name + '.zip' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11iiiiI1i
 print '======================================='
 extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOOoooOO0O ( )
 if 75 - 75: oO0o - OOooOOo - ooOoO0O00 % I1ii11iIi11i - IIiIiII11i
 if 61 - 61: I1ii11iIi11i + ii / Ii
def O0O0o0o0oo0O ( url ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IIIIiIiIi1 = os . path . join ( I1iI , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11iiiiI1i
 print '======================================='
 extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
 iI1i11 ( url )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I11OoooO ( )
 if 49 - 49: o0O00o + oO0o + o0o00Oo0O
def Ii1i1I1 ( url ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IIIIiIiIi1 = os . path . join ( I1iI , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11iiiiI1i
 print '======================================='
 extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
 iI1i11 ( url )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I11OoooO ( )
 if 95 - 95: IIiIiII11i * OOooOOo . IIIi11I1 + Ii1I + I11i + OOooOOo
def OOo0o0o ( name , url , description ) :
 I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IIIIiIiIi1 = os . path . join ( II )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print I11iiiiI1i
 print '======================================='
 extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I11OoooO ( )
 if 72 - 72: ooOoO0O00 . I11i
def iIII1I111III ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def Oo0o0O00 ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : OOo0O0oo0OO0O = open ( oO , 'w' ) ; OOo0O0oo0OO0O . close ( )
 with open ( oO , 'a' ) as OOo0O0oo0OO0O :
  iIIiiIiII1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOo0O0oo0OO0O . write ( iIIiiIiII1i . rstrip ( '\r\n' ) + '\n' )
def o0oo00000O ( msg , level = xbmc . LOGDEBUG ) :
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : OOo0O0oo0OO0O = open ( oO , 'w' ) ; OOo0O0oo0OO0O . close ( )
 if WIZDEBUGGING == 'false' : return False
 if DEBUGLEVEL == '0' : return False
 if DEBUGLEVEL == '1' and not level in [ xbmc . LOGNOTICE , xbmc . LOGERROR , xbmc . LOGSEVERE , xbmc . LOGFATAL ] : return False
 if DEBUGLEVEL == '2' : level = xbmc . LOGNOTICE
 try :
  if isinstance ( msg , unicode ) :
   msg = '%s' % ( msg . encode ( 'utf-8' ) )
  xbmc . log ( '%s: %s' % ( i1iiIIiiI111 , msg ) , level )
 except Exception as I1iI1I1I1i11i :
  try : xbmc . log ( 'Logging Failure: %s' % ( I1iI1I1I1i11i ) , level )
  except : pass
 if ENABLEWIZLOG == 'true' :
  Oo00OOO0 = getS ( 'nextcleandate' ) if not getS ( 'nextcleandate' ) == '' else str ( TODAY )
  if CLEANWIZLOG == 'true' and Oo00OOO0 <= str ( TODAY ) : checkLog ( )
  with open ( oO , 'a' ) as OOo0O0oo0OO0O :
   iIIiiIiII1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , msg )
   OOo0O0oo0OO0O . write ( iIIiiIiII1i . rstrip ( '\r\n' ) + '\n' )
def I11OoooO ( ) :
 OoOOo0OOoO = O0OoO000O0OO . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OoOOo0OOoO == 0 : return
 elif OoOOo0OOoO == 1 : pass
 oOooo0 = iIII1I111III ( )
 Oo0o0O00 ( "Platform: " + str ( oOooo0 ) )
 os . _exit ( 1 )
 Oo0o0O00 ( "Force close failed!  Trying alternate methods." )
 if oOooo0 == 'osx' :
  Oo0o0O00 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oOooo0 == 'linux' :
  Oo0o0O00 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oOooo0 == 'android' :
  Oo0o0O00 ( "############ try android force close #################" )
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
  O0OoO000O0OO . ok ( i1iiIIiiI111 , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif oOooo0 == 'windows' :
  Oo0o0O00 ( "############ try windows force close #################" )
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
  Oo0o0O00 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  Oo0o0O00 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  O0OoO000O0OO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 27 - 27: o0O0Oooo0O
  if 10 - 10: Ii + oOOoOooOo / ii
  if 57 - 57: ii % IIiIiII11i - o0O0Oooo0O
def oo0ooOoo00Ooo ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( url ) :
  for file in ooOo0 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOoO00o = open ( ( os . path . join ( i11O00oO , file ) ) ) . read ( )
    iiIiI11IiI1I = oOoO00o . replace ( oOo0oooo00o , 'special://home/' )
    OOo0O0oo0OO0O = open ( ( os . path . join ( i11O00oO , file ) ) , mode = 'w' )
    OOo0O0oo0OO0O . write ( str ( iiIiI11IiI1I ) )
    OOo0O0oo0OO0O . close ( )
 I11OoooO ( )
 if 98 - 98: IIiIiII11i * o0O00o - oOo0O0Ooo % I11i - IIIIiiII111 % Ii1I
def o0oO00oooo ( ) :
 iI ( ( '[COLOR' + II11iiii1Ii + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiiiiIIii + 'RadioNomy.png' )
 iI ( ( '[COLOR' + II11iiii1Ii + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiiiiIIii + 'RadioNomy.png' )
 iI ( ( '[COLOR' + II11iiii1Ii + ']SEARCH[/COLOR]' ) , '' , 70006 , iiiiiIIii + 'RadioNomy.png' )
 if 69 - 69: ooOoO0O00 % oO0o % o0O0Oooo0O / oOOoOooOo / oOOoOooOo
def Ii1I1i1IiiI ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiiiiIIii + 'RadioNomy.png' )
def IiiiI1i ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiiiiIIii + 'RadioNomy.png' )
def I1iIi1i ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in I1Ii :
  iI ( ( '[COLOR' + II11iiii1Ii + ']Filter - ' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiiiiIIii + 'RadioNomy.png' )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']Stream - ' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iII11 )
def I1II1iI ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
def iIii1Ii11I1i ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii
 iI11IIi1iiI1I = 'https://www.radionomy.com/en/search/index?query=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 oO0000OOo00 = i11oO0oOo0 ( iI11IIi1iiI1I )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']Stream - ' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + Oo0o00OO0000 , 70005 , iII11 )
  if 83 - 83: I1ii11iIi11i / oOOoOooOo
  if 11 - 11: I11i - IIiIiII11i % ooOO0O0ooOooO . IIiIiII11i
def Ooo0OOO0O00 ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.listenlive.eu/' + Oo0o00OO0000 , 10111113 , iiiiiIIii + 'WorldRadio.png' , iiiiiIIii + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def I1iII1 ( url ) :
 O0o0O0 = iii1 ( url )
 if 65 - 65: ooOO0O0ooOooO . Ii % IIIi11I1 * IIIIiiII111 % I1ii11iIi11i
 if 51 - 51: oO0o % IIIIiiII111
 Ii1i1iI1iIIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , IiiiiIiI , url , i1I1IiI1II1 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' [COLORorangered] ' + i1I1IiI1II1 + '[/COLOR]' , url , 222225 , iiiiiIIii + 'WorldRadio.png' , iiiiiIIii + 'WorldRadio.png' , '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[CR]' + IiiiiIiI + '[CR]' + i1I1IiI1II1 + '[/COLOR]' )
  if 21 - 21: ii . o0o00Oo0O / Ii
def oOOOoo0 ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.toonjet.com/' + Oo0o00OO0000 , 8051 , iiiiiIIii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1i11II1i1i ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( O0o0O0 )
 for url , iII11 in Ii1i1iI1iIIi :
  if 'ol.gif' in iII11 :
   pass
  elif 'link_block_' in iII11 :
   pass
  elif '.png' in iII11 :
   pass
  else :
   iI ( ( iII11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiiiiIIii + 'vod.png' )
 for url in I1Ii :
  iI ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiiiiIIii + 'Next.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0O0O00OoO0O ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiiiiIIii + 'classictoons.png' )
  if 22 - 22: iIII - I11i
  if 54 - 54: ooOO0O0ooOooO * oO0o - IIIIiiII111 * iIII + I11i - Ii1i1i
def iI1I11 ( ) :
 iIiiII ( 'Audio Books' , '' , 30011 , iiiiiIIii + 'AudioBooks.png' , iiiiiIIii + 'AudioBooks.png' , '' )
 iIiiII ( 'Kids Audio Books' , '' , 30006 , iiiiiIIii + 'KidsAudioBooks.png' , iiiiiIIii + 'KidsAudioBooks.png' , '' )
 if 92 - 92: oOo0O0Ooo / oO0o - IIIi11I1 / Ii
def IiIi1 ( ) :
 iIiiII ( 'All' , '' , 30001 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 iIiiII ( 'Popular' , '' , 30012 , iiiiiIIii + 'POPULARv.png' , iiiiiIIii + 'POPULARv.png' , '' )
 iIiiII ( 'Search' , '' , 30013 , iiiiiIIii + 'Search.png' , iiiiiIIii + 'Search.png' , '' )
 if 45 - 45: oOOoOooOo + IIiIiII11i % IIIIiiII111
def o00OoOo0 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( I1IIiiIiii + 'books' + I11iii1Ii )
 Ii1i1iI1iIIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , Oo0o00OO0000 , Iii1I in Ii1i1iI1iIIi :
  if 'Parent' in iiIiii1IIIII :
   pass
  elif '2' in Iii1I :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 33 - 33: IIIi11I1 / ooOO0O0ooOooO . Ii * iI11I1II1I1I
def o0O0ooo0o ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( I1IIiiIiii + 'books' + I11iii1Ii )
 Ii1i1iI1iIIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , Oo0o00OO0000 , Iii1I in Ii1i1iI1iIIi :
  if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
   if '1' in Iii1I :
    iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   elif '2' in Iii1I :
    iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   elif '3' in Iii1I :
    iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30009 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
    if 55 - 55: oOOoOooOo . o0O00o * ooOoO0O00 . Ii1i1i
    if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + Ii1i1i % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def oo000O ( ) :
 oO0000OOo00 = i11oO0oOo0 ( I1IIiiIiii + 'books' + I11iii1Ii )
 Ii1i1iI1iIIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , Oo0o00OO0000 , Iii1I in Ii1i1iI1iIIi :
  if '1' in Iii1I :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 3010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif '2' in Iii1I :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif '3' in Iii1I :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30009 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 97 - 97: ii * I11i + ii % Ii1i1i * I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 35 - 35: iI11I1II1I1I % IIIIiiII111 - ooOoO0O00
def I1i1iI1I1II ( url ) :
 i11I1 = url
 oO0000OOo00 = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in I1Ii :
  if 'mp3' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i11I1 + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i11I1 + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i11I1 + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif '/' in iiIiii1IIIII :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i11I1 + url , 30009 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 20 - 20: OOooOOo
   if 1 - 1: o0O0Oooo0O * oO0o - IIIIiiII111
   if 97 - 97: IIIIiiII111 . Ii1I - iI11I1II1I1I . oOOoOooOo + oOo0O0Ooo % ooOO0O0ooOooO
def Ii1i1iiiIiIIiIiiii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 i11I1 = url
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Parent' in iiIiii1IIIII :
   pass
  elif '.db' in iiIiii1IIIII :
   pass
  elif '.jpg' in iiIiii1IIIII :
   pass
  elif '.html' in iiIiii1IIIII :
   pass
  elif '.doc' in iiIiii1IIIII :
   pass
  elif 'mp3' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i11I1 + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i11I1 + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  else :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i11I1 + url , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 99 - 99: o0O00o % o0O0Oooo0O
   if 61 - 61: o0o00Oo0O + oOo0O0Ooo / ii * IIIIiiII111 / IIiIiII11i / IIIIiiII111
def O0OO0oOo00o0 ( ) :
 iIiiII ( 'A-Z' , '' , 30007 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 iIiiII ( 'All' , '' , 30003 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 iIiiII ( 'Search' , '' , 30014 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 if 43 - 43: o0o00Oo0O / o0O0Oooo0O . iI11I1II1I1I - OOooOOo
def iiII1iiI ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 in Ii1i1iI1iIIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + Oo0o00OO0000 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iII11 :
   pass
  else :
   iIiiII ( iII11 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( Oo0o00OO0000 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iII11 + '.gif' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: Ii - iIII / oOOoOooOo / I11i * Ii * I11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: ii % o0o00Oo0O - IIIi11I1 / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * o0O00o / oO0o . ooOO0O0ooOooO
def IiiiiI ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '</a>' in iiIiii1IIIII :
   pass
  elif '(' in iiIiii1IIIII :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  else :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 12 - 12: Ii . iIII * IIIi11I1 % ooOoO0O00 . oOOoOooOo
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: IIIIiiII111 % iI11I1II1I1I . iI11I1II1I1I / iIII
def OOO0O ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
   if '</a>' in iiIiii1IIIII :
    pass
   elif '(' in iiIiii1IIIII :
    iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30005 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   else :
    OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30004 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
    if 21 - 21: I1ii11iIi11i / o0O00o * OOooOOo - o0O0Oooo0O
    if 44 - 44: ii + Ii1i1i
def Oooooo0O ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '</a>' in iiIiii1IIIII :
   pass
  elif '(' in iiIiii1IIIII :
   iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30005 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  else :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30004 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 77 - 77: OOooOOo
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: o0O00o / IIIIiiII111
 if 97 - 97: oO0o + iI11I1II1I1I
def O0OOoo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  i11I1 = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( i11I1 )
  if 38 - 38: o0O00o . I11i
def i1Ii111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '<p align' in iiIiii1IIIII :
   pass
  elif '&nbsp;' in iiIiii1IIIII :
   pass
  else :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 58 - 58: ooOO0O0ooOooO * Ii * oOo0O0Ooo * Ii1I % Ii - ii
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: IIiIiII11i % IIIIiiII111
 if 59 - 59: oOOoOooOo % I1ii11iIi11i - ooOO0O0ooOooO + o0O00o
def I1IIII ( ) :
 oO0000OOo00 = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 Ii1i1iI1iIIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'ongoing' in Oo0o00OO0000 :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 21005 , iiiiiIIii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in Oo0o00OO0000 :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 21005 , iiiiiIIii + 'CartoonShows.png' , '' , '' )
  if 'disney' in Oo0o00OO0000 :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 21005 , iiiiiIIii + 'Disney.png' , '' , '' )
  if 'genre' in Oo0o00OO0000 :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 21005 , iiiiiIIii + 'Genre.png' , '' , '' )
  if 'years' in Oo0o00OO0000 :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 21005 , iiiiiIIii + 'Years.png' , '' , '' )
def oo0oO0o00Oo0 ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1i = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0000OOo00 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iII11 , iII11 , iiIiii1IIIII )
 for url , iiIiii1IIIII in Ii1i :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 21005 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 for url in next :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 21005 , iiiiiIIii + 'Next.png' , '' , '' )
def i1I1IO0O ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1iIII1IiiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 i11iIii11 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0000OOo00 )
 o00oOoOo000Oo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 for url in i11iIii11 :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 for url , iiIiii1IIIII in I1iIII1IiiI :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
def O0o0ooo0 ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
  if 20 - 20: oO0o . ooOO0O0ooOooO
def II111I11iI ( ) :
 oO0000OOo00 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 Ii1i1iI1iIIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '9cart' in Oo0o00OO0000 :
   iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 20001 , iiiiiIIii + 'ORIGINCARTOON.png' )
   if 18 - 18: ii
def oooii111I1I1I ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1i1iii1Ii = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if '9cart' in url :
   iI ( '[COLOR' + II11iiii1Ii + ']ALL[/COLOR]' , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
 for url in I1Ii :
  if '9cart' in url :
   iI ( '[COLOR' + II11iiii1Ii + ']123[/COLOR]' , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
 for url , iiIiii1IIIII in I1i1iii1Ii :
  if '9cart' in url :
   iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
   if 34 - 34: Ii1I % ooOoO0O00 - oO0o
def IiI111i ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 20003 , iII11 )
 for url , iiIiii1IIIII in I1Ii :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
  if 30 - 30: o0o00Oo0O + Ii1i1i - o0o00Oo0O . I11i % o0O00o
def o00oo00oo ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'Watch' in url :
   iI ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiiiiIIii + 'ORIGINCARTOON.png' )
   if 86 - 86: I11i . I11i . IIiIiII11i . I11i
def o0o00oo ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 20005 , iiiiiIIii + 'ORIGINCARTOON.png' )
  if 45 - 45: o0o00Oo0O - OOooOOo % IIIi11I1
def ooI1 ( url ) :
 url = cloudflare . source ( url )
 II1i1i1I1iII ( url )
 if 4 - 4: IIIIiiII111 % Ii1I
def ii1II11I11i11 ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . recompile ( 'src="([^"]*)"' )
 for url in Ii1i1iI1iIIi :
  II1i1i1I1iII ( url )
  if 51 - 51: ii / I11i
  if 15 - 15: IIiIiII11i - Ii1i1i - IIIIiiII111 . ooOO0O0ooOooO / Ii
def iiIiiiI ( url , name ) :
 url = url ; name = name
 iIIIiiii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 iIIIiiii . clear ( )
 I11Ii1 = [ ]
 oO0OOO = [ ]
 Ii1iIi111i1i1 = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Ii1iIi111i1i1 )
 for iII11 in I1Ii :
  OoooooO0oOOoO = iII11
 I1i1iii1Ii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Ii1iIi111i1i1 )
 for I1I1 , oOoooo0OooO in I1i1iii1Ii :
  I11Ii1 . append ( [ I1I1 , oOoooo0OooO ] )
  if len ( I11Ii1 ) == len ( I1i1iii1Ii ) :
   for IIi1IIIi in I11Ii1 :
    OooO0O = random . randint ( 1 , len ( I11Ii1 ) )
    try :
     Oo0o = I11Ii1 [ int ( OooO0O ) ]
     if Oo0o [ 1 ] not in oO0OOO :
      oO0OOO . append ( Oo0o [ 1 ] )
      i1II11II1 = i11oO0oOo0 ( Oo0o [ 0 ] )
      o0oO0OO00ooOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i1II11II1 )
      for O0OO0 , OOI1i11i in o0oO0OO00ooOO :
       if 'easy' in OOI1i11i :
        iiiI1I = i11oO0oOo0 ( OOI1i11i )
        IiIIiii11II1 = re . compile ( 'file: "(.+?)"' ) . findall ( iiiI1I )
        for OOOOo0o0O0 in IiIIiii11II1 :
         if 'http' in OOOOo0o0O0 :
          Oo0oO = xbmcgui . ListItem ( Oo0o [ 1 ] , iconImage = OoooooO0oOOoO , thumbnailImage = OoooooO0oOOoO )
          Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : Oo0o [ 1 ] } )
          Oo0oO . setProperty ( "IsPlayable" , "true" )
          iIIIiiii . add ( OOOOo0o0O0 , Oo0oO )
          xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0oO )
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
   if 7 - 7: IIIi11I1 . o0O00o . o0O0Oooo0O / Ii1i1i / I1ii11iIi11i
def o0Ooo ( url ) :
 iIIIiiii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 iIIIiiii . clear ( )
 iI11IIiII = [ ]
 iii111 = [ ]
 OO0oOOOOO = [ ]
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iii111 . append ( [ url , iiIiii1IIIII ] )
  if len ( iii111 ) == len ( Ii1i1iI1iIIi ) :
   for IIi1IIIi in iii111 :
    OoOooO0 = random . randint ( 1 , len ( iii111 ) )
    try :
     i1ii1i1 = iii111 [ int ( OoOooO0 ) ]
    except :
     pass
    if i1ii1i1 [ 1 ] not in OO0oOOOOO :
     OO0oOOOOO . append ( i1ii1i1 [ 1 ] )
     if int ( len ( iI11IIiII ) ) < 1 :
      iI11IIiII . append ( i1ii1i1 [ 1 ] [ 0 ] )
      iiIiiiI ( i1ii1i1 [ 0 ] , i1ii1i1 [ 1 ] )
     else :
      pass
    else :
     pass
  else :
   pass
   if 42 - 42: ooOO0O0ooOooO
def iiiiiiI1iIi ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = o0
 o0OO0O0OO0oO0 = sys . argv [ 0 ]
 o0OO0O0OO0oO0 += '?mode=' + str ( mode )
 o0OO0O0OO0oO0 += '&title=' + urllib . quote_plus ( name )
 o0OO0O0OO0oO0 += '&image=' + urllib . quote_plus ( image )
 o0OO0O0OO0oO0 += '&page=' + str ( page )
 if url != '' :
  o0OO0O0OO0oO0 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  o0OO0O0OO0oO0 += '&keyword=' + urllib . quote_plus ( keyword )
 Oo0oO = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  Oo0oO . addContextMenuItems ( contextMenu )
 if infoLabels :
  Oo0oO . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  Oo0oO . setProperty ( "IsPlayable" , "true" )
 Oo0oO . setProperty ( 'Fanart_Image' , iIi1ii1I1 )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = isFolder )
 if 40 - 40: Ii1I * oO0o % ii
def OOoOOOo00 ( ) :
 oO00O0OO = i11 ( 'http://www.animetoon.org/cartoon' )
 O0o0O0 = i11oO0oOo0 ( oO00O0OO )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiiiI1iIi ( iiIiii1IIIII , 9110012 , url = Oo0o00OO0000 , image = o0 , isFolder = False )
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 40 - 40: Ii % iI11I1II1I1I % iI11I1II1I1I
def Oo00o0O0O ( ) :
 oO00O0OO = i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Cartoons[/COLOR]' , '' , 10004 , iiiiiIIii + 'ORIGINCARTOON.png' , iIi1ii1I1 , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']24/7 Select Cartoon[/COLOR]' , '' , 9110011 , o0 , iIi1ii1I1 , '' , '' )
 iiiiiiI1iIi ( '[COLOR' + II11iiii1Ii + ']24/7 Random Cartoon[/COLOR]' , 9110010 , url = oO00O0OO , image = o0 , isFolder = False )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search Cartoons[/COLOR]' , '' , 10005 , iiiiiIIii + 'ORIGINCARTOON.png' , iIi1ii1I1 , '' )
 if 79 - 79: Ii
def Oo0oo0OOO0OOoOO ( ) :
 oO00O0OO = i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( oO00O0OO )
 if 20 - 20: ooOoO0O00 - o0O00o + o0O00o . ii . oOo0O0Ooo + iIII
 Ii1i1iI1iIIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0000OOo00 )
 if 10 - 10: o0O00o / I1ii11iIi11i
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
   if 'Dad!' in iiIiii1IIIII :
    pass
   elif 'Family Guy' in iiIiii1IIIII :
    pass
   elif '2 Stupid' in iiIiii1IIIII :
    pass
   elif 'The Zelfs' in iiIiii1IIIII :
    pass
   elif 'A Clone' in iiIiii1IIIII :
    pass
   elif 'A.T.O.M' in iiIiii1IIIII :
    pass
   elif 'Almost Naked' in iiIiii1IIIII :
    pass
   elif 'Angry Kid' in iiIiii1IIIII :
    pass
   elif 'Annoying Orange' in iiIiii1IIIII :
    pass
   elif 'Aqua Teen' in iiIiii1IIIII :
    pass
   elif 'Assy Mcgee' in iiIiii1IIIII :
    pass
   elif 'Astroblast' in iiIiii1IIIII :
    pass
   elif 'Atomic Betty' in iiIiii1IIIII :
    pass
   elif 'Axe Cop' in iiIiii1IIIII :
    pass
   elif 'Baby Playpen' in iiIiii1IIIII :
    pass
   elif 'Beavis and Butt' in iiIiii1IIIII :
    pass
   elif 'Celebrity Deathmatch' in iiIiii1IIIII :
    pass
   elif 'Clerks The' in iiIiii1IIIII :
    pass
   elif 'Crapston Villas' in iiIiii1IIIII :
    pass
   elif 'Duckman:' in iiIiii1IIIII :
    pass
   elif 'Stripperella' in iiIiii1IIIII :
    pass
   elif 'Vixen' in iiIiii1IIIII :
    pass
   else :
    OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 10006 , iiiiiIIii + 'ORIGINCARTOON.png' , iIi1ii1I1 , '' )
    if 82 - 82: Ii1I / IIIIiiII111 + Ii1I + o0O0Oooo0O
    if 63 - 63: IIiIiII11i % iI11I1II1I1I * Ii1I / oOOoOooOo % oOo0O0Ooo % ooOoO0O00
    if 87 - 87: I11i % ooOoO0O00 + ooOO0O0ooOooO - iI11I1II1I1I . IIIi11I1 + Ii
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 83 - 83: Ii1I * IIiIiII11i . o0O0Oooo0O - iIII
def iIII1II11I1 ( url ) :
 oO00O0OO = i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 O0o0O0 = i11oO0oOo0 ( oO00O0OO )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Dad!' in iiIiii1IIIII :
   pass
  elif 'Family Guy' in iiIiii1IIIII :
   pass
  elif '2 Stupid' in iiIiii1IIIII :
   pass
  elif 'The Zelfs' in iiIiii1IIIII :
   pass
  elif 'A Clone' in iiIiii1IIIII :
   pass
  elif 'A.T.O.M' in iiIiii1IIIII :
   pass
  elif 'Almost Naked' in iiIiii1IIIII :
   pass
  elif 'Angry Kid' in iiIiii1IIIII :
   pass
  elif 'Annoying Orange' in iiIiii1IIIII :
   pass
  elif 'Aqua Teen' in iiIiii1IIIII :
   pass
  elif 'Assy Mcgee' in iiIiii1IIIII :
   pass
  elif 'Astroblast' in iiIiii1IIIII :
   pass
  elif 'Atomic Betty' in iiIiii1IIIII :
   pass
  elif 'Axe Cop' in iiIiii1IIIII :
   pass
  elif 'Baby Playpen' in iiIiii1IIIII :
   pass
  elif 'Beavis and Butt' in iiIiii1IIIII :
   pass
  elif 'Celebrity Deathmatch' in iiIiii1IIIII :
   pass
  elif 'Clerks The' in iiIiii1IIIII :
   pass
  elif 'Crapston Villas' in iiIiii1IIIII :
   pass
  elif 'Duckman:' in iiIiii1IIIII :
   pass
  elif 'Stripperella' in iiIiii1IIIII :
   pass
  elif 'Vixen' in iiIiii1IIIII :
   pass
  else :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10006 , iiiiiIIii + 'ORIGINCARTOON.png' , iIi1ii1I1 , '' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: IIIi11I1 % o0O00o % I11i . Ii1i1i . Ii1I
def OOoO0000o00 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O0o0O0 )
 for iII11 in I1Ii :
  OoooooO0oOOoO = iII11
 I1i1iii1Ii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( O0o0O0 )
 for url in I1i1iii1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NEXT PAGE[/COLOR]' , url , 10006 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 Ii1i1iI1iIIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10007 , OoooooO0oOOoO )
  if 23 - 23: oO0o % oOOoOooOo - ooOO0O0ooOooO . Ii1I . ii
  if 65 - 65: o0O00o + ii - ooOoO0O00
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: ooOO0O0ooOooO / IIIi11I1 / IIIi11I1 * I11i * Ii1I - Ii
def oOI1IIi11I1IiIi ( url , IMAGE ) :
 OO0oO0 = [ ]
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , i11I1 in Ii1i1iI1iIIi :
  if 'panda' in i11I1 :
   oO0000OOo00 = i11oO0oOo0 ( i11I1 )
   I1Ii = re . compile ( "url: '(.+?)'" ) . findall ( oO0000OOo00 )
   for IIi11i in I1Ii :
    if 'http' in IIi11i :
     OO0oO0 . append ( { 'source' : 'playpanda' , 'quality' : 'SD' , 'url' : IIi11i } )
  elif 'easy' in i11I1 :
   iiIi1IIiIi = i11oO0oOo0 ( i11I1 )
   I1i1iii1Ii = re . compile ( 'file: "(.+?)"' ) . findall ( iiIi1IIiIi )
   for IIi11i in I1i1iii1Ii :
    if 'http' in IIi11i :
     OO0oO0 . append ( { 'source' : 'easyvideo' , 'quality' : 'SD' , 'url' : IIi11i } )
  elif 'zoo' in i11I1 :
   oOO00Oo = i11oO0oOo0 ( i11I1 )
   o0oO0OO00ooOO = re . compile ( 'src: "(.+?)"' ) . findall ( oOO00Oo )
   for IIi11i in o0oO0OO00ooOO :
    if 'http' in IIi11i :
     OO0oO0 . append ( { 'source' : 'videozoo' , 'quality' : 'SD' , 'url' : IIi11i } )
 if len ( OO0oO0 ) >= 3 :
  OoOOo0OOoO = O0OoO000O0OO . select ( 'Select Playlink' ,
 [ I1I1IiI1 [ "source" ] + " - " + " (" + I1I1IiI1 [ "quality" ] + ")"
 for I1I1IiI1 in OO0oO0 ] )
  if OoOOo0OOoO != - 1 :
   url = OO0oO0 [ OoOOo0OOoO ] [ 'url' ]
   I11iI1i11IiI = False
   xbmc . Player ( ) . play ( url )
   if 78 - 78: o0O00o / IIIIiiII111 * Ii1i1i . IIIi11I1 . ooOO0O0ooOooO - o0O0Oooo0O
   if 39 - 39: oOOoOooOo . ooOoO0O00 + ii . IIIIiiII111 - Ii % o0O0Oooo0O
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 38 - 38: ooOO0O0ooOooO
def I1iIiI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "url: '(.+?)'," ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
  if 45 - 45: iIII . IIiIiII11i / Ii
  if 50 - 50: ii / oO0o % iI11I1II1I1I
  if 41 - 41: Ii1I % Ii1I + o0O00o . IIIIiiII111 % o0O0Oooo0O * oOOoOooOo
def O0Ii1iIii1I1 ( ) :
 if 21 - 21: OOooOOo + OOooOOo * oOOoOooOo / IIIi11I1 * ii . I1ii11iIi11i
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Stand Up[/COLOR]' , '' , 10014 , iiiiiIIii + 'StandUp.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search Comedian[/COLOR]' , '' , 10015 , iiiiiIIii + 'SearchComedian.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Others[/COLOR]' , '' , 10017 , iiiiiIIii + 'Others.png' , iIi1ii1I1 , '' )
 if 22 - 22: oOOoOooOo % OOooOOo / I11i
def oO0OIiIi1ii1Ii ( ) :
 oO0000OOo00 = i11oO0oOo0 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'elete' in iiIiii1IIIII :
   pass
  else :
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 222 , iII11 )
   if 6 - 6: IIIIiiII111 % I11i + o0O0Oooo0O
def OO0o0O0 ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OooO0oO0O0O = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , i1I11i1iii1 , i1iII1IiiIiI1 in OooO0oO0O0O :
  for oOO0ooIiIIi1I1I11Ii in i1I11i1iii1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oO0O00O0O0o = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for Oo0o00OO0000 , iiIiii1IIIII in oO0O00O0O0o :
    if 'tube' in Oo0o00OO0000 :
     pass
    elif 'stage' in Oo0o00OO0000 :
     O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + i1I11i1iii1 + '   -   ' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iII11 , )
    elif 'vee' in Oo0o00OO0000 :
     pass
     if 41 - 41: Ii1i1i . Ii + o0o00Oo0O - ii * ooOO0O0ooOooO
def i1IiI111IiiI1 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OooO0oO0O0O = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , i1I11i1iii1 , i1iII1IiiIiI1 in OooO0oO0O0O :
  oO0O00O0O0o = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for Oo0o00OO0000 , iiIiii1IIIII in oO0O00O0O0o :
   if 'tube' in Oo0o00OO0000 :
    pass
   elif 'stage' in Oo0o00OO0000 :
    O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + i1I11i1iii1 + '   -   ' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iII11 )
   elif 'vee' in Oo0o00OO0000 :
    pass
    if 8 - 8: I1ii11iIi11i / Ii1I + Ii1I . Ii1i1i
    if 27 - 27: IIiIiII11i - Ii - ii
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: oOo0O0Ooo
def i1IiIi1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1iiIiI1iI1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0000OOo00 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1iiIiI1iI1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1iiIiI1iI1I :
  O0o0oo0oOO0oO ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 4 - 4: IIIi11I1 % oOOoOooOo - IIIi11I1 - I11i
  if 30 - 30: o0O00o
  if 34 - 34: ooOO0O0ooOooO - IIiIiII11i - I11i + IIIIiiII111 + o0O0Oooo0O
  if 70 - 70: ii + oO0o * I1ii11iIi11i
  if 20 - 20: Ii - IIiIiII11i - oOOoOooOo % ooOO0O0ooOooO . oOOoOooOo
  if 50 - 50: iI11I1II1I1I + o0O0Oooo0O - iIII - ii
  if 84 - 84: OOooOOo - iIII
def iIIIi1i1I11i ( ) :
 if 80 - 80: Ii % IIIi11I1 - I1ii11iIi11i % IIIi11I1
 O0O0oOo0o0o0 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , iIi1ii1I1 , '' )
 O0O0oOo0o0o0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIi1ii1I1 , '' )
 if 86 - 86: I11i / OOooOOo
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 40 - 40: IIIIiiII111
def o000 ( ) :
 O0O0oOo0o0o0 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIi1ii1I1 , '' )
 O0O0oOo0o0o0 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIi1ii1I1 , '' )
 if 85 - 85: ooOoO0O00 % I11i * Ii1I * oO0o . IIiIiII11i
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def O000 ( ) :
 if 18 - 18: oOOoOooOo + o0O0Oooo0O / IIIi11I1 / ooOO0O0ooOooO + iI11I1II1I1I % o0O00o
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 I1oo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 94 - 94: iIII
 for i1oO00O in I1oo :
  oo0o0ooooo = OOO00O + i1oO00O + I11iii1Ii
  oO0000OOo00 = O0 ( oo0o0ooooo )
  Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , ii1i , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    iI11IiiI1 ( iiIiii1IIIII , Oo0o00OO0000 , 222 , ii1i , ooo0O0o00O , i11II1I11I1 )
    if 83 - 83: ooOO0O0ooOooO / iI11I1II1I1I
    OOoOO0o0o0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 68 - 68: o0O0Oooo0O - OOooOOo . Ii + I11i
    if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
def i1I ( ) :
 if 89 - 89: IIIIiiII111 + ooOoO0O00 - o0O00o + oOOoOooOo . IIiIiII11i
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 I1oo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 85 - 85: iI11I1II1I1I - Ii1i1i * I1ii11iIi11i . ooOO0O0ooOooO + o0O0Oooo0O
 for i1oO00O in I1oo :
  Ii1iIii = OOO00O + i1oO00O + I11iii1Ii
  oO0000OOo00 = O0 ( Ii1iIii )
  Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iiIiii1IIIII , i11II1I11I1 , Oo0o00OO0000 , iII11 , ooo0O0o00O , oOo0 in Ii1i1iI1iIIi :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    O0O0oOo0o0o0 ( iiIiii1IIIII , Oo0o00OO0000 , oOo0 , iII11 , ooo0O0o00O , i11II1I11I1 )
    if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . IIIIiiII111 / IIIIiiII111
    OOoOO0o0o0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 43 - 43: oOo0O0Ooo
    if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
def IIII11i1Ii ( ) :
 if 13 - 13: oOOoOooOo * oO0o % iI11I1II1I1I / o0O00o * IIIIiiII111 . I1ii11iIi11i
 O0o0O0 = i11oO0oOo0 ( OOO00O + 'spongemain.php' )
 Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , i11II1I11I1 , Oo0o00OO0000 , iII11 , ooo0O0o00O , oOo0 in Ii1i1iI1iIIi :
  O0O0oOo0o0o0 ( iiIiii1IIIII , Oo0o00OO0000 , oOo0 , iII11 , ooo0O0o00O , i11II1I11I1 )
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
def I1i1 ( url ) :
 if 89 - 89: o0O00o % Ii . Ii + ooOO0O0ooOooO / Ii1I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1III = ( '%s%s' % ( oO00O0OO , url ) )
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I1IiI1 )
 for url , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0o0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
  for IIi1IIIi in O0o0O :
   if IIi1IIIi == url :
    iiIiii1IIIII = ( '[COLORred]Watched - [/COLOR]' + iiIiii1IIIII ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  iI11IiiI1 ( iiIiii1IIIII , url , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
  if 100 - 100: o0O00o + ooOoO0O00 * oO0o
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
  if 64 - 64: ooOO0O0ooOooO * Ii . I1ii11iIi11i
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: I1ii11iIi11i / oOOoOooOo / IIIIiiII111 - I11i / IIIIiiII111
  if 74 - 74: ooOoO0O00 . iI11I1II1I1I
def ooOoo ( url ) :
 if 25 - 25: iIII . OOooOOo
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , i11II1I11I1 , url , iII11 , ooo0O0o00O , oOo0 in Ii1i1iI1iIIi :
  O0O0oOo0o0o0 ( iiIiii1IIIII , url , oOo0 , iII11 , ooo0O0o00O , i11II1I11I1 )
  if 3 - 3: OOooOOo
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
  if 52 - 52: OOooOOo
  if 79 - 79: oOo0O0Ooo + I1ii11iIi11i % OOooOOo - o0O00o + oOo0O0Ooo * ooOO0O0ooOooO
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: OOooOOo % Ii1I * I1ii11iIi11i % ii - oO0o
def iI11IiiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 13 - 13: IIIi11I1 . Ii1i1i / iIII
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oo0oooo0OoO0o = [ ]
  oo0oooo0OoO0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oo0oooo0OoO0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   oo0oooo0OoO0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0oO . addContextMenuItems ( oo0oooo0OoO0o )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = False )
 return iIiiIi11IIi
 if 93 - 93: oOOoOooOo * oOo0O0Ooo * Ii1I / Ii1I
def O0O0oOo0o0o0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 62 - 62: oOOoOooOo * Ii1i1i % Ii1I - ooOoO0O00 - Ii1I
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oo0oooo0OoO0o = [ ]
  oo0oooo0OoO0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oo0oooo0OoO0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   oo0oooo0OoO0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0oO . addContextMenuItems ( oo0oooo0OoO0o )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = True )
 return iIiiIi11IIi
if 24 - 24: IIIi11I1
if 71 - 71: o0O00o - ooOoO0O00
if 56 - 56: OOooOOo + ooOO0O0ooOooO
if 74 - 74: IIIIiiII111 / o0O0Oooo0O / IIiIiII11i - IIIIiiII111 / ooOO0O0ooOooO % iIII
if 19 - 19: o0O00o % ii + ii
if 7 - 7: ooOoO0O00
if 91 - 91: OOooOOo - OOooOOo . o0O00o
if 33 - 33: o0O0Oooo0O - iI11I1II1I1I / Ii1i1i % o0o00Oo0O
if 80 - 80: o0O00o % ii - o0O00o
if 27 - 27: o0O0Oooo0O - I11i * Ii1I - oOo0O0Ooo
if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIIIiiII111 . Ii1i1i
if 100 - 100: IIiIiII11i / o0O0Oooo0O / IIIIiiII111 - Ii1I * iI11I1II1I1I
if 7 - 7: ooOoO0O00 . o0O00o % Ii * Ii1I . iIII % Ii1I
if 35 - 35: oOo0O0Ooo
if 48 - 48: ii % ii - oO0o . OOooOOo
def I1iiii ( string ) :
 if IIIi1I1IIii1II == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 69 - 69: OOooOOo + o0o00Oo0O - iIII - iI11I1II1I1I . oO0o
def i1IO00oO0oOOOOOO ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 Oo0ooo00OoO = [ ]
 try :
  if 1 - 1: ii * iI11I1II1I1I / Ii1I * iIII
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( oO0Oo ) == False :
  I1iiii ( 'Making Favorites File' )
  Oo0ooo00OoO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOoO00o = open ( oO0Oo , "w" )
  oOoO00o . write ( json . dumps ( Oo0ooo00OoO ) )
  oOoO00o . close ( )
 else :
  I1iiii ( 'Appending Favorites' )
  oOoO00o = open ( oO0Oo ) . read ( )
  I1i1I1i1Ii = json . loads ( oOoO00o )
  I1i1I1i1Ii . append ( ( name , url , iconimage , fanart , mode ) )
  iiIiI11IiI1I = open ( oO0Oo , "w" )
  iiIiI11IiI1I . write ( json . dumps ( I1i1I1i1Ii ) )
  iiIiI11IiI1I . close ( )
  if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
  if 43 - 43: I1ii11iIi11i / o0O0Oooo0O / ooOoO0O00
def I1i11IIiiIiI ( ) :
 if os . path . exists ( oO0Oo ) == False :
  Oo0ooo00OoO = [ ]
  I1iiii ( 'Making Favorites File' )
  Oo0ooo00OoO . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oOoO00o = open ( oO0Oo , "w" )
  oOoO00o . write ( json . dumps ( Oo0ooo00OoO ) )
  oOoO00o . close ( )
 else :
  II1iiiiI1Ii11 = json . loads ( open ( oO0Oo ) . read ( ) )
  oo0oO0oOo0O = len ( II1iiiiI1Ii11 )
  for O0oo in II1iiiiI1Ii11 :
   iiIiii1IIIII = O0oo [ 0 ]
   Oo0o00OO0000 = O0oo [ 1 ]
   ii1i = O0oo [ 2 ]
   try :
    III1II1iiI11 = O0oo [ 3 ]
    if III1II1iiI11 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     III1II1iiI11 = ii1i
    else :
     III1II1iiI11 = ooo0O0o00O
   try : iiIi = O0oo [ 5 ]
   except : iiIi = None
   try : ooO00Oo = O0oo [ 6 ]
   except : ooO00Oo = None
   if 3 - 3: Ii1I % I1ii11iIi11i . o0o00Oo0O % I11i . I11i - IIIIiiII111
   if O0oo [ 4 ] == 0 :
    OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , '' , ii1i , ooo0O0o00O , '' , 'fav' )
   else :
    OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , O0oo [ 4 ] , ii1i , ooo0O0o00O , '' , 'fav' )
    if 68 - 68: Ii . oOOoOooOo % iIII
def iIiii1 ( name ) :
 I1i1I1i1Ii = json . loads ( open ( oO0Oo ) . read ( ) )
 for O0oOoo0OoO0O in range ( len ( I1i1I1i1Ii ) ) :
  if I1i1I1i1Ii [ O0oOoo0OoO0O ] [ 0 ] == name :
   del I1i1I1i1Ii [ O0oOoo0OoO0O ]
   iiIiI11IiI1I = open ( oO0Oo , "w" )
   iiIiI11IiI1I . write ( json . dumps ( I1i1I1i1Ii ) )
   iiIiI11IiI1I . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 37 - 37: oOo0O0Ooo / ii % Ii % Ii1I
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
def iiiiii1ii1 ( ) :
 i1iI11IiII = os . path . join ( ooooooO0oo , 'addons.ini' )
 oO00Oo0OO = open ( i1iI11IiII , "w+" )
 oO0000OOo00 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/get.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO + '&type=m3u_plus&output=mpegts' )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0000OOo00 )
 oO00Oo0OO . write ( r'[' + IiII + ']' + '\n' )
 for iiIiii1IIIII , iII11 , i11iIIiii , Oo0o00OO0000 in Ii1i1iI1iIIi :
  Oo0o00OO0000 = ( Oo0o00OO0000 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  O0o000Oo = ( iiIiii1IIIII + '=plugin://' + IiII + '/?url=' + Oo0o00OO0000 + '&mode=10012&name=' + ( iiIiii1IIIII ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iII11 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iII11 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  oO00Oo0OO . write ( O0o000Oo + '\n' )
  if 1 - 1: o0o00Oo0O * Ii1i1i
  if 5 - 5: IIIIiiII111 - IIIIiiII111 / o0O0Oooo0O % I1ii11iIi11i
def OOoO00OOo ( ) :
 O0o0O0 = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 Ii1i1iI1iIIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 in Ii1i1iI1iIIi :
  iI ( '24/7' , Oo0o00OO0000 , 90021 , iiiiiIIii + '247Streams.png' )
  if 42 - 42: ooOoO0O00 . Ii / OOooOOo
def iii1OO00Oo00o ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + '247Streams.png' , iiiiiIIii + '247Streams.png' , '' )
def ooo0Oo00O ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + 'musicch.png' , iiiiiIIii + 'musicch.png' , '' )
def II1II1iIIi11 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + 'NEWS.png' , iiiiiIIii + 'NEWS.png' , '' )
def Ii1 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + 'adult.png' , iiiiiIIii + 'adult.png' , '' )
def IiII1Iiii ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 Ii1i1iI1iIIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , Oo0o00OO0000 , 1016 , iiiiiIIii + 'TUTS.png' , iiiiiIIii + 'TUTS.png' , '' )
  if 16 - 16: IIIIiiII111 . o0o00Oo0O - o0O0Oooo0O * o0O0Oooo0O
  if 80 - 80: Ii1i1i % Ii1I
def OOoo000OO00 ( ) :
 if 51 - 51: oOOoOooOo * o0O00o * iI11I1II1I1I / OOooOOo % o0O00o
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Recent Episodes[/COLOR]' , '' , 10019 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Genres[/COLOR]' , '' , 10020 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search[/COLOR]' , '' , 10021 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 if 36 - 36: Ii1I * I11i + Ii + ii
def oOi1IiIiIii11I ( ) :
 if 80 - 80: o0O0Oooo0O + iIII . o0O0Oooo0O + IIIi11I1
 O0o0O0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i1iI1iIIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , O0Ooo in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII + '  -  ' + ( O0Ooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Oo0o00OO0000 , 10023 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
  if 85 - 85: Ii . iIII + Ii1i1i / Ii1i1i
  if 43 - 43: o0O00o . ii - IIiIiII11i
  if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * IIIi11I1 * ooOO0O0ooOooO
def I11iIIiiIiIi ( ) :
 if 7 - 7: Ii1I
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Action[/COLOR]' , 'Aksiyon' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Adventure[/COLOR]' , 'Macera' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Animation[/COLOR]' , 'Animasyon' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Anime[/COLOR]' , 'Anime' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Biography[/COLOR]' , 'Biyografi' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Comedy[/COLOR]' , 'Komedi' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Drama[/COLOR]' , 'Dram' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Family[/COLOR]' , 'Aile' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']History[/COLOR]' , 'Tarih' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Horror[/COLOR]' , 'Korku' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Mystery[/COLOR]' , 'Gizem' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Romance[/COLOR]' , 'Romantik' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Sport[/COLOR]' , 'Spor' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Western[/COLOR]' , 'Tarih' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 if 11 - 11: oOOoOooOo
def IIIiII1iIII ( url ) :
 Ooo0 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0000OOo00 = cloudflare . source ( Ooo0 )
 Ii1i1iI1iIIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10022 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
  if 62 - 62: IIiIiII11i . oOOoOooOo + oO0o % oO0o - o0o00Oo0O - IIiIiII11i
  if 22 - 22: Ii1i1i - I1ii11iIi11i % Ii1I % oOOoOooOo % o0O00o
  if 72 - 72: ooOoO0O00
  if 72 - 72: oOOoOooOo + IIiIiII11i . o0o00Oo0O - IIIIiiII111 / ii . o0O0Oooo0O
def iii ( ) :
 if 32 - 32: ii
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 Oo0o00OO0000 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 oO0000OOo00 = cloudflare . source ( Oo0o00OO0000 )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 10022 , iiiiiIIii + 'dtv.png' )
   if 29 - 29: Ii1I
   if 41 - 41: Ii1i1i
   if 49 - 49: Ii1i1i % IIiIiII11i . Ii1i1i - I11i - iIII * o0O00o
def IiiO0O0O0OOO0o ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for i11I1 , ooO0000o00O , IIiI , iiIiii1IIIII in Ii1i1iI1iIIi :
  oO0Oo0oOo = ( IIiI ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  II1oOO0O0Ooo0 = ( ooO0000o00O ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I11iiI1i = 'Season ' + II1oOO0O0Ooo0 + 'Episode ' + oO0Oo0oOo + iiIiii1IIIII
  ooOoOOiIiiII11 ( I11iiI1i , i11I1 )
  if 75 - 75: OOooOOo + Ii1i1i . Ii / Ii1i1i
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 32 - 32: Ii1i1i + o0O00o + Ii1I
  if 79 - 79: ooOoO0O00 / Ii1i1i
def ooOoOOiIiiII11 ( name , url ) :
 i11I1 = url
 o0OO0oO0oOOOoo = name
 iiIi1IIiIi = cloudflare . source ( i11I1 )
 I1Ii = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iiIi1IIiIi )
 for I1iiIiI1iI1I , OooII11II1IIii in I1Ii :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + o0OO0oO0oOOOoo + OooII11II1IIii + '[/COLOR]' , I1iiIiI1iI1I , 222 , iiiiiIIii + 'dtv.png' )
  if 71 - 71: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: I11i * I1ii11iIi11i - Ii1i1i . oOOoOooOo
 if 2 - 2: I1ii11iIi11i - oOOoOooOo % iI11I1II1I1I
def Oo0000O0OOooO ( ) :
 if 88 - 88: o0O0Oooo0O - oO0o
 if 79 - 79: IIIIiiII111
 if 45 - 45: IIiIiII11i + IIIIiiII111 . iIII . o0o00Oo0O * ooOoO0O00 - Ii1i1i
 if 48 - 48: Ii1I + I1ii11iIi11i
 if 76 - 76: Ii1I
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . Ii1i1i
 if 51 - 51: Ii1i1i + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH[/COLOR]' , '' , 10091 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 if 20 - 20: o0O0Oooo0O . iIII . Ii1i1i + iIII - IIIi11I1 * ooOO0O0ooOooO
def o00ooO0 ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0000OOo00 )
 iIIiiI1Ii1II = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + iII11 , '' , '' )
 for url in iIIiiI1Ii1II :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiiiiIIii + 'Next.png' , '' , '' )
  if 25 - 25: oOo0O0Ooo
def o0o0OoOo0 ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0000OOo00 )
 iIIiiI1Ii1II = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iII11 = 'http://watchepisodes.cc/' + iII11
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10093 , iII11 , iII11 , '' )
 for url in iIIiiI1Ii1II :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiiiiIIii + 'Next.png' , '' , '' )
  if 89 - 89: o0O00o
def OO0OOo00Oo ( url , iconimage ) :
 iII11 = iconimage
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0000OOo00 )
 for IIiI , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + IIiI + ' - ' + iiIiii1IIIII + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , iII11 , '' , '' )
  if 26 - 26: IIiIiII11i * IIIIiiII111 + I11i / o0o00Oo0O + ooOoO0O00 - iIII
def o000oOoOOO ( url , iconimage ) :
 iII11 = iconimage
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if 'player' in iiIiii1IIIII :
   pass
  elif 'vod' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , iII11 , '' , '' )
   if 88 - 88: Ii1I % Ii1I + ii - IIIi11I1 * o0o00Oo0O
   if 100 - 100: iI11I1II1I1I - OOooOOo
   if 28 - 28: I1ii11iIi11i . o0o00Oo0O . iIII
   if 60 - 60: IIiIiII11i + o0O0Oooo0O / ooOO0O0ooOooO % ii - ooOoO0O00
   if 57 - 57: oOOoOooOo
   if 99 - 99: I1ii11iIi11i + o0O0Oooo0O % oOOoOooOo - I11i
def O00OO ( ) :
 if 52 - 52: Ii1I
 if 93 - 93: IIIIiiII111 . Ii
 if 24 - 24: IIIi11I1 . oO0o + o0O0Oooo0O . ooOO0O0ooOooO - Ii1I % IIIIiiII111
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / Ii1i1i
 if 29 - 29: Ii1I / ooOO0O0ooOooO * o0o00Oo0O - Ii - oO0o + Ii1i1i
 if 86 - 86: oOo0O0Ooo / Ii1I * Ii1i1i % Ii
 if 20 - 20: IIIIiiII111 . ii + IIIIiiII111 + oOOoOooOo * Ii1I
 if 44 - 44: Ii
 if 69 - 69: IIIi11I1 * o0o00Oo0O + Ii
 if 65 - 65: o0o00Oo0O / IIIIiiII111 . ooOoO0O00 * IIIIiiII111 / iI11I1II1I1I - ooOO0O0ooOooO
 if 93 - 93: OOooOOo % Ii - Ii1i1i % oO0o
 if 55 - 55: I11i . Ii1I
 if 63 - 63: ooOO0O0ooOooO
 if 79 - 79: Ii1I - ooOO0O0ooOooO - I11i . IIIi11I1
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiiiiIIii + 'latest.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiiiiIIii + 'popular.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiiiiIIii + 'Genre.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiiiiIIii + 'series.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search Program[/COLOR]' , '' , 10043 , iiiiiIIii + 'Search.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 if 65 - 65: Ii . oO0o % IIIIiiII111 + o0O00o - Ii
 if 60 - 60: o0O0Oooo0O
def II1II1ii1Ii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
  if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * iIII + IIIi11I1
def i1i11IiII ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
  if 94 - 94: iI11I1II1I1I / oOo0O0Ooo * Ii1I
def I1i1ii1IiI1i ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'episode' in url :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
  else :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 for url in I1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiiiiIIii + 'Next.png' , '' , '' )
  if 78 - 78: IIIIiiII111
  if 15 - 15: IIIIiiII111 + Ii % o0o00Oo0O % o0O0Oooo0O + oO0o * oOOoOooOo
def i1Iii11iiI1 ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0ooOO000O = 'http://www.watchseriesgo.to/search/' + oOO0ooIiIIi1I1I11Ii . replace ( ' ' , '%20' )
 oO0000OOo00 = i11oO0oOo0 ( o0ooOO000O )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'watch online' in iiIiii1IIIII :
   pass
  else :
   print Oo0o00OO0000
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.watchseriesgo.to' + Oo0o00OO0000 , 10044 , iII11 , '' , '' )
   if 49 - 49: I1ii11iIi11i
   xbmcplugin . setContent ( O00oO , 'movies' )
   if 57 - 57: o0o00Oo0O * oOOoOooOo - IIIIiiII111 - iI11I1II1I1I * IIIIiiII111
def i1o0oOoooOoo0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , IIiI , i11II1I11I1 in Ii1i1iI1iIIi :
  o0O00o0OoO = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IIiI ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + o0O00o0OoO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iII11 , '' , i11II1I11I1 )
  if 26 - 26: o0o00Oo0O * Ii1i1i - oOo0O0Ooo - IIIIiiII111 / iI11I1II1I1I
def oO0Ooo00O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  o0O00o0OoO = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + o0O00o0OoO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 for url in I1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiiiiIIii + 'Next.png' , '' , '' )
  if 74 - 74: I11i % OOooOOo . IIIIiiII111 % o0O0Oooo0O . o0o00Oo0O % IIiIiII11i
def iIiiIi11 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iII11 , '' , '' )
 for url in I1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiiiiIIii + 'Next.png' , '' , '' )
  if 73 - 73: o0O00o - o0O00o / ii
def oOoOo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1II1I11i1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for ooO0000o00O , OooO0oO0O0O in Ii1II1I11i1 :
  Ii1i1iI1iIIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OooO0oO0O0O ) )
  for url , iiIiii1IIIII in Ii1i1iI1iIIi :
   o0O00o0OoO = ( ooO0000o00O ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + o0O00o0OoO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 I1Ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 for url in I1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiiiiIIii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 55 - 55: o0O00o * I11i * oOOoOooOo - ooOoO0O00 / Ii1i1i * ooOO0O0ooOooO
class ooOiiIII ( ) :
 if 37 - 37: ii / Ii1I % I11i
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 34 - 34: OOooOOo . iIII % ooOO0O0ooOooO - o0o00Oo0O * o0o00Oo0O
  o0O00o0OoO = name
  self . Get_Sources ( Oo0o00OO0000 , o0O00o0OoO )
  if 11 - 11: o0o00Oo0O * Ii * IIiIiII11i / IIIi11I1 * o0o00Oo0O
  if 71 - 71: iIII . I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0000OOo00 = i11oO0oOo0 ( URL )
  Ii1i1iI1iIIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
   URL = 'http://www.watchseriesgo.to/link/' + Oo0o00OO0000
   self . Get_site_link ( URL , season_name )
   if 24 - 24: IIIi11I1 * ii . o0o00Oo0O . oO0o . oOo0O0Ooo
 def Get_site_link ( self , url , season_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
  I1Ii = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oO0000OOo00 )
  I1i1iii1Ii = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oO0000OOo00 )
  for url in Ii1i1iI1iIIi :
   self . main ( url , season_name )
  for url in I1Ii :
   self . main ( url , season_name )
  for url in I1i1iii1Ii :
   self . main ( url , season_name )
   if 80 - 80: o0o00Oo0O * oO0o . o0O0Oooo0O % o0o00Oo0O
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ii11I1iIIi = 'DACLIPS'
   if ii11I1iIIi in ooOiiIII . source_list :
    pass
   else :
    self . daclips ( url , season_name , ii11I1iIIi )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    ii11I1iIIi = 'THEVIDEO'
    if ii11I1iIIi in ooOiiIII . source_list :
     pass
    else :
     self . thevideo ( url , season_name , ii11I1iIIi )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     ii11I1iIIi = 'ALLMYVIDEOS'
     if ii11I1iIIi in ooOiiIII . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , ii11I1iIIi )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      ii11I1iIIi = 'VIDSPOT'
      if ii11I1iIIi in ooOiiIII . source_list :
       pass
      else :
       self . vidspot ( url , season_name , ii11I1iIIi )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       ii11I1iIIi = 'VODLOCKER'
       if ii11I1iIIi in ooOiiIII . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , ii11I1iIIi )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        ii11I1iIIi = 'VIDTO'
        if ii11I1iIIi in ooOiiIII . source_list :
         pass
        else :
         self . vidto ( url , season_name , ii11I1iIIi )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 29 - 29: Ii1i1i + IIIIiiII111 % Ii1I + iIII * I1ii11iIi11i - Ii
       else :
        if 'youwatch' in url :
         ii11I1iIIi = 'YouWatch'
         if ii11I1iIIi in ooOiiIII . source_list :
          pass
         else :
          self . youwatch ( url , season_name , ii11I1iIIi )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 24 - 24: Ii . oOOoOooOo + oOOoOooOo - Ii % IIIi11I1
          if 58 - 58: oOo0O0Ooo
 def allmyvid ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
  for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 94 - 94: I11i + Ii1i1i % I11i . o0O0Oooo0O - oOOoOooOo * oOo0O0Ooo
 def vidspot ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 62 - 62: I1ii11iIi11i * ooOoO0O00 % Ii1I + I1ii11iIi11i . o0o00Oo0O . oOOoOooOo
 def thevideo ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 57 - 57: I1ii11iIi11i - o0O0Oooo0O + o0o00Oo0O % I11i
 def vodlocker ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 72 - 72: IIIi11I1 . OOooOOo / IIiIiII11i
 def daclips ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 69 - 69: IIIi11I1 * IIiIiII11i - oOOoOooOo - ooOoO0O00 + Ii
 def filehoot ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . youplay ( oOoooooOoO , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 50 - 50: ii * ooOoO0O00 / ooOO0O0ooOooO
 def Printer ( self , Link , season_name , source_name ) :
  if 83 - 83: ooOoO0O00
  if Link in ooOiiIII . List :
   pass
  elif source_name in ooOiiIII . source_list :
   pass
  else :
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + source_name + '[/COLOR]' , Link , 222 , iiiiiIIii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   ooOiiIII . List . append ( Link )
   ooOiiIII . source_list . append ( source_name )
   if 38 - 38: ii * iI11I1II1I1I
   xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 54 - 54: ii . o0O0Oooo0O
   if 71 - 71: Ii1i1i
   if 31 - 31: iIII . Ii . oO0o * I1ii11iIi11i % Ii1i1i . I11i
   if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
   if 93 - 93: oOOoOooOo % o0O0Oooo0O
def OO0oo ( ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Highlights[/COLOR]' , '' , 10008 , iiiiiIIii + 'Highlights.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Fixtures[/COLOR]' , '' , 10009 , iiiiiIIii + 'Fixtures.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiiiiIIii + 'PremiereLeague.png' , iIi1ii1I1 , '' )
 if 46 - 46: Ii1I * OOooOOo * o0O00o * Ii1I . Ii1I
def i1I11iIIiIIiIi ( url ) :
 ii1IiI = '20'
 o0oO00O000O = [ ]
 IiIIiIi1 = '                                                    '
 ooOoo0OoO0 = '        '
 OoOOoOooooOOo ( IiIIiIi1 + 'pl' + ooOoo0OoO0 + 'w' + ooOoo0OoO0 + 'd' + ooOoo0OoO0 + 'l' + ooOoo0OoO0 + 'f' + ooOoo0OoO0 + 'a' + ooOoo0OoO0 + 'pts' , '' , '' , '' , '' , '' )
 O0o0O0 = Oo ( url )
 Ii1i1iI1iIIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( O0o0O0 )
 for oO0OO00o , oooooOOOO0oOo , iiii1Ii , oOO0oOooo , IIiiiI , OOo0O0oo0OO0O , oOoO00o , ii11 , iI1i1i1i1i in Ii1i1iI1iIIi :
  iiII1i1II1iIi = iIIOOOO0o0Oo0 ( oooooOOOO0oOo )
  I1iIiI1iiI = iIIOOOO0o0Oo0 ( iiii1Ii )
  oO000O00 = iIIOOOO0o0Oo0 ( oOO0oOooo )
  IiIIIii1iIII1 = iIIOOOO0o0Oo0 ( IIiiiI )
  OoOooooo0oo = iIIOOOO0o0Oo0 ( OOo0O0oo0OO0O )
  ii1II1 = iIIOOOO0o0Oo0 ( oOoO00o )
  o0oO00O000O . append ( oO0OO00o [ 0 ] )
  i1I1II11I1 = len ( o0oO00O000O )
  oo0o = int ( len ( IiIIiIi1 ) - len ( oO0OO00o ) - 2 )
  if len ( o0oO00O000O ) >= 10 :
   oo0o = oo0o - 1
  if len ( o0oO00O000O ) <= int ( ii1IiI ) :
   oOOOoo0O0oO ( str ( i1I1II11I1 ) + ' ' + oO0OO00o + IiIIiIi1 [ 0 : oo0o ] + oooooOOOO0oOo + iiII1i1II1iIi + iiii1Ii + I1iIiI1iiI + oOO0oOooo + oO000O00 + IIiiiI + IiIIIii1iIII1 + OOo0O0oo0OO0O + OoOooooo0oo + oOoO00o + ii1II1 + ' ' + iI1i1i1i1i , '' , '' , '' , '' , '' )
   if 61 - 61: ooOoO0O00 / ooOoO0O00 + oOOoOooOo . o0O0Oooo0O * oOOoOooOo
   if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
def iIIOOOO0o0Oo0 ( space ) :
 if len ( space ) > 1 :
  OO0III = len ( '        ' ) - len ( space ) + 1
  space = int ( OO0III ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 82 - 82: o0o00Oo0O / IIIIiiII111 * oO0o - iIII + I1ii11iIi11i
def IIiiII11i11I ( ) :
 if 95 - 95: I1ii11iIi11i / o0O00o + I1ii11iIi11i
 if 94 - 94: oOOoOooOo - ooOoO0O00 . o0o00Oo0O / oOo0O0Ooo
 if 37 - 37: Ii1I * o0O0Oooo0O * oOo0O0Ooo * o0o00Oo0O
 if 35 - 35: oOo0O0Ooo - Ii1I * IIIIiiII111 + o0O00o / ooOoO0O00
 if 46 - 46: I1ii11iIi11i . oOOoOooOo % I1ii11iIi11i / IIiIiII11i * oOOoOooOo * IIIi11I1
 if 59 - 59: o0O0Oooo0O * IIIIiiII111
 if 31 - 31: iIII / o0o00Oo0O
 if 57 - 57: ooOoO0O00 % oOOoOooOo
 if 69 - 69: I11i
 if 69 - 69: o0O0Oooo0O
 if 83 - 83: iI11I1II1I1I . I11i + o0O0Oooo0O . ii / oOOoOooOo + IIiIiII11i
 if 90 - 90: Ii1i1i * IIIIiiII111 / IIIi11I1
 if 68 - 68: OOooOOo
 if 65 - 65: ooOO0O0ooOooO
 if 82 - 82: I11i
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + o0O0Oooo0O
 if 65 - 65: Ii1i1i
 if 71 - 71: o0O0Oooo0O % o0O0Oooo0O . ooOO0O0ooOooO + Ii - Ii
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / o0O0Oooo0O - Ii . oOOoOooOo / IIIi11I1
 if 13 - 13: I11i % o0o00Oo0O - o0O0Oooo0O * ii / I1ii11iIi11i - ii
 if 78 - 78: ooOO0O0ooOooO % ii
 if 73 - 73: oOo0O0Ooo % oOOoOooOo % o0O00o + ooOoO0O00 - ii / ooOO0O0ooOooO
 if 78 - 78: ii % ooOO0O0ooOooO - Ii
 if 37 - 37: o0O00o % Ii1i1i % ooOoO0O00
 if 23 - 23: oOOoOooOo - o0o00Oo0O + Ii
 if 98 - 98: ii
 if 61 - 61: I11i . o0O00o . o0o00Oo0O + ii + o0o00Oo0O
 if 65 - 65: ooOoO0O00 * IIIi11I1 * ii - o0O00o . IIIIiiII111 - oO0o
 if 71 - 71: Ii1i1i * OOooOOo
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % o0O0Oooo0O * I11i
 if 64 - 64: oOOoOooOo / oOOoOooOo + Ii1I * IIIi11I1 % IIIi11I1
 if 87 - 87: oO0o * I1ii11iIi11i
 if 83 - 83: ooOoO0O00 * o0O0Oooo0O - o0O00o / Ii1i1i
 if 48 - 48: ooOO0O0ooOooO . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
 if 32 - 32: Ii1i1i * oOo0O0Ooo - IIIi11I1 . I1ii11iIi11i / o0o00Oo0O + Ii1i1i
 if 67 - 67: OOooOOo % I1ii11iIi11i
 if 7 - 7: Ii % Ii1I / o0O0Oooo0O % I1ii11iIi11i - oO0o
 if 73 - 73: Ii1I
 if 92 - 92: Ii + o0o00Oo0O * iIII
 if 60 - 60: I11i / I1ii11iIi11i
 if 19 - 19: iI11I1II1I1I . oO0o / ii
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % o0O0Oooo0O / Ii1I
 if 76 - 76: oO0o * ooOO0O0ooOooO - oO0o
 if 57 - 57: ii / OOooOOo + ooOO0O0ooOooO . Ii1i1i
 if 14 - 14: Ii % IIIi11I1 * I11i * OOooOOo
 if 55 - 55: o0O0Oooo0O * IIIi11I1 * o0O0Oooo0O
 if 70 - 70: o0o00Oo0O . Ii1i1i
 if 33 - 33: IIIi11I1 * Ii1i1i
 if 64 - 64: Ii . iI11I1II1I1I
 if 7 - 7: OOooOOo % oOOoOooOo + OOooOOo - OOooOOo * Ii % oO0o
 if 57 - 57: IIIi11I1 / oO0o + Ii1I
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % IIIi11I1 + o0O00o . oO0o . I1ii11iIi11i
 if 70 - 70: iIII . Ii1I * ooOO0O0ooOooO
 if 97 - 97: ooOO0O0ooOooO . iI11I1II1I1I - IIIi11I1
 if 23 - 23: Ii1I % iIII
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
 if 99 - 99: o0O0Oooo0O - Ii1I - oOo0O0Ooo - o0O0Oooo0O + oO0o + IIiIiII11i
 if 34 - 34: o0O0Oooo0O * iIII
 if 31 - 31: o0O00o . ooOO0O0ooOooO
 if 40 - 40: Ii1i1i - iIII / IIiIiII11i * ooOoO0O00 + o0O00o * IIiIiII11i
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - o0O0Oooo0O
 if 99 - 99: Ii1i1i - o0O00o - ooOoO0O00 / Ii . o0O00o
 if 58 - 58: IIIi11I1
 if 12 - 12: oOo0O0Ooo . I11i * ii
 if 64 - 64: OOooOOo + o0O00o - ooOoO0O00 . IIiIiII11i . oO0o
 if 31 - 31: ooOO0O0ooOooO . IIIIiiII111 - iIII . iI11I1II1I1I + iIII . OOooOOo
 if 86 - 86: Ii1I - Ii1I / IIIIiiII111 - Ii1I * IIIIiiII111 + o0O0Oooo0O
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - o0O00o
 if 30 - 30: ii % IIIi11I1
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - IIIi11I1
 if 81 - 81: IIIIiiII111 % Ii1i1i . oOOoOooOo
 if 66 - 66: Ii1I * Ii1i1i / ii * o0o00Oo0O % IIIi11I1
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * Ii1i1i / o0O0Oooo0O * ii
 if 82 - 82: I1ii11iIi11i / Ii1i1i / Ii1i1i % Ii1i1i
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 Ii1i1iI1iIIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Oo0o00OO0000 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iII11 , iIi1ii1I1 , '' )
  if 20 - 20: oOOoOooOo
def ooOooooOo00OO0o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Ii1II1I11i1 in Ii1II1I11i1 :
  Ooi1IIii11i1I1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( Ii1II1I11i1 ) )
  for oO0o0oo in Ooi1IIii11i1I1 :
   oO0o0oo = oO0o0oo
  Ii1I11ii1i = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
  for O0ooOo0Oooo , iII11 , time , iiiI11iii11iI in Ii1I11ii1i :
   ooooooo00oO0OO = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iiiI11iii11iI )
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + oO0o0oo + ' - ' + O0ooOo0Oooo + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iII11 , iIi1ii1I1 , ( str ( ooooooo00oO0OO ) ) )
   if 46 - 46: IIIIiiII111 % o0O0Oooo0O % OOooOOo . ii . IIiIiII11i % o0O00o
 OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if 6 - 6: o0O0Oooo0O % o0O00o / Ii1i1i + o0O0Oooo0O . ooOO0O0ooOooO
def oo0O0 ( ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iiiiiIIii + 'fanart.jpg' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iiiiiIIii + 'fanart.jpg' , '' )
 if 93 - 93: I1ii11iIi11i
def Oo0OO0ooO0O0O ( url ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'TodaysMacthes.png' , iIi1ii1I1 , '' )
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oO00O = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiIiii1IIIII :
   pass
  else :
   oO00O = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + oO00O + '[/COLOR]' , url , 10013 , iII11 )
 for url , iII11 , iiIiii1IIIII in I1Ii :
  oO00O = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiIiii1IIIII :
   pass
  else :
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + oO00O + '[/COLOR]' , url , 10013 , iII11 )
def ooooooO0o00 ( url ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'TodaysMacthes.png' , iIi1ii1I1 , '' )
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 if 56 - 56: Ii % oOOoOooOo * o0O00o . OOooOOo * IIIi11I1
 if 80 - 80: I1ii11iIi11i - ooOO0O0ooOooO - I1ii11iIi11i / iIII - iI11I1II1I1I * iI11I1II1I1I
 if 18 - 18: iIII * Ii1I / Ii / iI11I1II1I1I * ii . IIIi11I1
 if 69 - 69: I1ii11iIi11i * oOOoOooOo
 if 91 - 91: I11i . oOOoOooOo / oO0o / Ii * I11i
 if 52 - 52: oOo0O0Ooo - Ii / o0O00o . ooOO0O0ooOooO
 if 38 - 38: ooOO0O0ooOooO + ii * OOooOOo % ooOO0O0ooOooO
 for url , iII11 , iiIiii1IIIII in I1Ii :
  oO00O = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiIiii1IIIII :
   pass
  else :
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + oO00O + '[/COLOR]' , url , 10013 , iII11 )
   if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
def iI1iIiI1Ii1iI ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0000OOo00 )
 for I1iiIiI1iI1I in Ii1i1iI1iIIi :
  OooOooo00OOO0o = ( I1iiIiI1iI1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  O0o0oo0oOO0oO ( 'http:' + OooOooo00OOO0o )
  if 41 - 41: IIIi11I1 % Ii * oOo0O0Ooo + I11i / ooOO0O0ooOooO
  if 56 - 56: ooOoO0O00
  if 11 - 11: Ii % I11i / iIII * ii
  if 82 - 82: o0O00o
def IIiI11I1II1 ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  O0O00OOo ( iiIiii1IIIII , url , 8046 , iII11 )
 for url in I1Ii :
  iI ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiiiiIIii + 'Next.png' )
def iiiIiiii1i1 ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0o0oo0oOO0oO ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 18 - 18: OOooOOo * OOooOOo - I11i % oOOoOooOo % IIiIiII11i - o0O00o
def OOoi1Iiiiiii ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  yt . PlayVideo ( url )
  if 62 - 62: iI11I1II1I1I % o0O0Oooo0O % Ii1I * o0O00o
def IIiI11i1111Ii ( ) :
 iI ( '[COLOR' + II11iiii1Ii + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiiiiIIii + 'documentary.png' )
 iI ( '[COLOR' + II11iiii1Ii + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiiiiIIii + 'documentary.png' )
 iI ( '[COLOR' + II11iiii1Ii + ']Search Docs[/COLOR]' , '' , 80012 , iiiiiIIii + 'Search.png' )
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , Oo0o00OO0000 , 8041 , iiiiiIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0OO0o0oo0o ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + iII11 )
 for url in next :
  iI ( 'NEXT PAGE' , url , 8041 , iiiiiIIii + 'Next.png' )
  if 55 - 55: o0O00o
  if 43 - 43: IIIi11I1
def i1OO0o ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']YouTube[/COLOR]' , url , 8043 , iiiiiIIii + 'documentary.png' )
  else :
   iI ( '[COLOR' + II11iiii1Ii + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def ooOoOoO0o00o ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  url = ( url ) . replace ( '\/' , '/' )
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , '' )
  if 46 - 46: IIIIiiII111 + o0O0Oooo0O % ii * Ii1I
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def O000o0O0 ( name , url ) :
 O0000oOoO0o0 = 0
 name = name
 url = url
 I11ii1IIiIi = [ '144' , '240' , '380' , '480' , '720' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Resolution[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  O0i1iI ( url )
  if 19 - 19: ooOoO0O00 % ooOO0O0ooOooO / I11i . I11i
  if 98 - 98: iIII / o0o00Oo0O % OOooOOo
  if 71 - 71: Ii * OOooOOo * IIIi11I1 + ooOO0O0ooOooO + I1ii11iIi11i
  if 59 - 59: o0O00o
  if 54 - 54: IIIi11I1
  if 27 - 27: OOooOOo - oO0o + I11i + oOOoOooOo . oO0o
  if 86 - 86: IIiIiII11i - ii - oOOoOooOo % IIIIiiII111
  if 16 - 16: oOOoOooOo + I1ii11iIi11i + ii
def OooOooO0OoOoo0o ( ) :
 O0o0O0 = iii1 ( 'http://documentarylovers.com/' )
 Ii1i1iI1iIIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  if 'genre' in Oo0o00OO0000 :
   iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , Oo0o00OO0000 , 80010 , iiiiiIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII1iIIIIII ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , iII11 )
 for url in next :
  iI ( 'NEXT PAGE' , url , 80010 , iiiiiIIii + 'Next.png' )
  if 31 - 31: I1ii11iIi11i / Ii1I - o0o00Oo0O + IIIIiiII111 - IIIIiiII111
def ooO0OOO ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']YouTube[/COLOR]' , url , 8043 , iiiiiIIii + 'documentary.png' )
 for url in I1Ii :
  ooOoOoO0o00o ( url )
  if 81 - 81: I1ii11iIi11i
def Oo0oOOo00o ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiI = 'http://documentarylovers.com/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11ii = IiiI . lower ( )
 iII1iIIIIII ( i11ii )
 if 14 - 14: IIiIiII11i + o0o00Oo0O - IIIIiiII111
def II1i1 ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'films' in url :
   iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiiiiIIii + 'documentary.png' )
def ooO0OoOO0 ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'films' in url :
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + iII11 )
 for url in I1Ii :
  iI ( 'NEXT' , url , 8049 , iiiiiIIii + 'Next.png' )
def o0oo00 ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  if 'rtd' in url :
   o000IIIi1IiI1iII ( url )
   if 85 - 85: Ii1I + OOooOOo - Ii % OOooOOo . ooOO0O0ooOooO + Ii
def o000IIIi1IiI1iII ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( O0o0O0 )
 for I1I1IiI1 , file in Ii1i1iI1iIIi :
  url = ( 'https://rtd.rt.com' + I1I1IiI1 + file )
  O0i1iI ( url )
  if 12 - 12: o0O00o + ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii1I
  if 5 - 5: oOOoOooOo - o0O0Oooo0O - IIIIiiII111
def iioOOOoOo0oOoo ( ) :
 oO0000OOo00 = iii1 ( 'http://www.stream2watch.co/live-tv' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , I1ii1Ii1 in Ii1i1iI1iIIi :
  iI ( ( iiIiii1IIIII + '[COLOR' + II11iiii1Ii + ']' + I1ii1Ii1 + '[/COLOR]' ) , Oo0o00OO0000 , 8086 , iII11 )
  if 64 - 64: Ii + OOooOOo + I11i + IIIi11I1
def Iii1iii11 ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 8087 , iII11 )
  if 29 - 29: ii / o0O00o % iIII . IIIi11I1 + o0O0Oooo0O
def oO0OOOo0OO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  i1IiI ( url , iiIiii1IIIII )
  if 31 - 31: iIII + oO0o / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
def i1IiI ( url , name ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  print url
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 34 - 34: o0O00o
def iIiIIiII11i1 ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + Oo0o00OO0000 , 3002 , 'http://www.solie.org/alibrary/' + iII11 )
def i1IiioOOooo ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iII11 )
def IiI11IiIIi ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 oOOo0OoooOo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( O0o0O0 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiiiiIIii + 'classicmovies.png' )
 for url , iiIiii1IIIII in oOOo0OoooOo :
  iI ( '[COLOR' + II11iiii1Ii + ']Season- ' + iiIiii1IIIII + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiiiiIIii + 'classicmovies.png' )
 for url in next :
  iI ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiiiiIIii + 'Next.png' )
 for url , iII11 , iiIiii1IIIII in I1Ii :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iII11 )
def I1I1IiIiIIi1I ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  oo0Ooo ( url )
def oo0Ooo ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
  if 21 - 21: Ii1I - ooOO0O0ooOooO * oO0o
def IIiiii ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Oo0o00OO0000 , 8065 , iiiiiIIii + 'classicmovies.png' )
def oO00oOOOO ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( "v.src = '([^']*)';" ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  II1i1i1I1iII ( url )
  if 54 - 54: iIII * ii
def iIi ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Oo0o00OO0000 , 8065 , iiiiiIIii + 'classictv.png' )
def OO0ooo ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  if 'mp4' in url :
   O0i1iI ( url )
 for url in I1Ii :
  yt . PlayVideo ( url )
  if 94 - 94: Ii1i1i / IIIi11I1 * Ii1I % Ii1I + o0O00o
def O0OO0Oo ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + Oo0o00OO0000 , 8071 , iiiiiIIii + 'streams.png' )
def II1111iII1 ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '(Free Access)' in iiIiii1IIIII :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0o0Oo + '/' + Oo00OOOOO + url ) . strip ( )
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiiiiIIii + 'streams.png' )
def iio0000oO0OOOo0 ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0o0Oo + '/' + Oo00OOOOO + url ) . strip ( )
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iII11 , ooo0O0o00O , '' )
  if 64 - 64: Ii1i1i - IIIIiiII111
def oO0ooOoOO ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']XXX Vids[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Perfect Girls[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Best Videos[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Genres[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Recently Uploaded[/COLOR]' , '[COLOR' + II11iiii1Ii + ']100% Verified[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Tags[/COLOR]' , '[COLOR' + II11iiii1Ii + ']In Your Language[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Search[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  i1II ( 'http://watchxxxfree.com/categories' )
 if OoOOo0OOoO == 1 :
  I1i1I11I ( 'http://www.perfectgirls.net' )
 if OoOOo0OOoO == 2 :
  OOOo00O ( 'http://www.xvideos.com/best' )
 if OoOOo0OOoO == 3 :
  I1iOO000o0o0oo ( 'http://www.xvideos.com/best' )
 if OoOOo0OOoO == 4 :
  OOOo00O ( 'http://www.xvideos.com/best' )
 if OoOOo0OOoO == 5 :
  OOOo00O ( 'http://www.xvideos.com/verified/videos' )
 if OoOOo0OOoO == 6 :
  oO00oOoo0ooO0 ( 'http://www.xvideos.com/tags' )
 if OoOOo0OOoO == 7 :
  Ooo0o0ooO0 ( 'http://www.xvideos.com/porn' )
 if OoOOo0OOoO == 8 :
  oO0o0O ( )
  if 60 - 60: ooOoO0O00 / iIII - I11i - oOOoOooOo
  if 98 - 98: I1ii11iIi11i + OOooOOo * IIIi11I1 / IIIIiiII111 * OOooOOo / ii
  if 35 - 35: IIiIiII11i . IIIi11I1 + iI11I1II1I1I . ooOoO0O00 - OOooOOo + o0O00o
  if 55 - 55: I1ii11iIi11i % o0O0Oooo0O . IIiIiII11i
  if 53 - 53: o0o00Oo0O / oO0o % Ii
  if 11 - 11: o0O0Oooo0O + ooOoO0O00 - IIIIiiII111 - oO0o * oOOoOooOo / oOOoOooOo
  if 4 - 4: iI11I1II1I1I - Ii * oO0o . o0O0Oooo0O + I11i
  if 11 - 11: OOooOOo % Ii1I - Ii1i1i - o0O0Oooo0O
  if 58 - 58: OOooOOo . Ii1i1i / o0O00o * ooOO0O0ooOooO
def oO0ooo0o0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'ch' in url :
   iIiiII ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiiiiIIii + 'Jizbox.png' , iiiiiIIii + 'Jizbox.png' , '' )
def O0oOO0o0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0000OOo00 )
 O000000oooOOo = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiiiiIIii + 'Jizbox.png' , '' , '' )
 for iiIiii1IIIII , url in O000000oooOOo :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiiiiIIii + 'Next.png' , '' , '' )
def I11iiI1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'jetload' in url :
   I1I ( url )
def oo000oooooooO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
def i1II ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , OO0III in Ii1i1iI1iIIi :
  if 'category' in url :
   iIiiII ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORorange]   ' + OO0III + '[/COLOR]' , url , 90006 , iII11 , iiiiiIIii + 'Jizbox.png' , '' )
def II1IIi1ii111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 O000000oooOOo = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , iII11 , '' , '' )
 for url in O000000oooOOo :
  OoOOoOooooOOo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiiiiIIii + 'Next.png' , '' , '' )
def II1OO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'jetload' in url :
   I1I ( url )
def I1I ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
def I1i1I11I ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , OO0III in Ii1i1iI1iIIi :
  if 'category' in url :
   iIiiII ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORorange]' + OO0III + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiiiiIIii + 'Jizbox.png' , '' , '' )
def oo0OOO0O0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 i11I1 = url
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 O000000oooOOo = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , iII11 , '' , '' )
 for url in O000000oooOOo :
  OoOOoOooooOOo ( '[COLORred]NEXT[/COLOR]' , i11I1 + '/' + url , 90003 , iiiiiIIii + 'Next.png' , '' , '' )
def OoooOooo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'get\("(.*)", function' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  IiIi1iiII ( 'http://www.perfectgirls.net' + url )
def IiIi1iiII ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'http://(.+?)\n' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O0o0oo0oOO0oO ( 'http://' + url )
def Ooo0o0ooO0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , OO0III in Ii1i1iI1iIIi :
  iIiiII ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgreen] - No of Videos : [COLORorange]' + OO0III + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Jizbox.png' , '' , '' )
def oO00oOoo0ooO0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O000000oooOOo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0000OOo00 )
 for url in O000000oooOOo :
  iIiiII ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiiiiIIii + 'Jizbox.png' , '' , '' )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , OO0III in Ii1i1iI1iIIi :
  iIiiII ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgreen] - No of Videos : [COLORorange]' + ( OO0III + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Jizbox.png' , '' , '' )
  if 69 - 69: iI11I1II1I1I + I1ii11iIi11i
def oooO0o0OoOo0O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O000000oooOOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for url in O000000oooOOo :
  iIiiII ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiiiiIIii + 'Next.png' , '' , '' )
 Ii1i1iI1iIIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , o0o000O0ooo0O in Ii1i1iI1iIIi :
  iIiiII ( iiIiii1IIIII + '--' + ( o0o000O0ooo0O ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iII11 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 1 - 1: Ii - ooOoO0O00 . oOo0O0Ooo
  if 80 - 80: OOooOOo . o0o00Oo0O - Ii % ii + I11i . I1ii11iIi11i
def OOOo00O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , oOoo , Ii11IIIi1 in Ii1i1iI1iIIi :
  iIiiII ( '[COLORorangered]' + iiIiii1IIIII + '[COLORgreen] - Porn Quality : [COLORorange]' + oOoo + ' - [COLORred]' + Ii11IIIi1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iII11 , iII11 , oOoo + ' - ' + Ii11IIIi1 )
 IIIii1i11111 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , Ii11IIIi1 in I1Ii :
  iIiiII ( '[COLORorangered]' + iiIiii1IIIII + '[COLORgreen] - Porn Quality : [COLORorange]' + Ii11IIIi1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iII11 , iII11 , Ii11IIIi1 )
 IIIii1i11111 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for url in IIIii1i11111 :
  iIiiII ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Next.png' , '' , '' )
  if 12 - 12: oOOoOooOo % OOooOOo
  if 1 - 1: o0o00Oo0O / oOOoOooOo
def I1iOO000o0o0oo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 O000000oooOOo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0000OOo00 )
 for url in O000000oooOOo :
  iIiiII ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiiiiIIii + 'Next.png' , '' , '' )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '/c/' in url :
   iIiiII ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Jizbox.png' , '' , '' )
   if 83 - 83: Ii1i1i / ii * ooOO0O0ooOooO . oOo0O0Ooo . ooOoO0O00
   if 59 - 59: iIII . iIII * oOo0O0Ooo - Ii1i1i % OOooOOo
def oO0o0O ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiIIIiI11i1 = ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 i11ii = IiIIIiI11i1 . lower ( )
 iI11IIi1iiI1I = 'http://www.xvideos.com/?k=' + i11ii
 print iI11IIi1iiI1I + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0000OOo00 = i11oO0oOo0 ( iI11IIi1iiI1I )
 Ii1i1iI1iIIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , Oo0o00OO0000 , iiIiii1IIIII , Ii11IIIi1 , IIIiiiIi1I1 in Ii1i1iI1iIIi :
  iIiiII ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgreen] - Porn Quality : [COLORorange]' + IIIiiiIi1I1 + ' - [COLORred]' + Ii11IIIi1 + '[/COLOR]' , 'http://www.xvideos.com' + Oo0o00OO0000 , 10108 , iII11 , iII11 , IIIiiiIi1I1 + ' - ' + Ii11IIIi1 )
 IIIii1i11111 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 in IIIii1i11111 :
  iIiiII ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + Oo0o00OO0000 , 10105 , iiiiiIIii + 'Next.png' , '' , '' )
if 10 - 10: oO0o - IIiIiII11i % I11i - OOooOOo + oO0o
if 88 - 88: iI11I1II1I1I % oOOoOooOo + I11i * OOooOOo / iIII . oO0o
if 66 - 66: iI11I1II1I1I * IIiIiII11i . iI11I1II1I1I * Ii + iIII + Ii1i1i
if 94 - 94: ooOoO0O00 * iIII - ii . ooOoO0O00 / I11i
if 51 - 51: Ii * ii
if 23 - 23: IIiIiII11i + iIII / o0o00Oo0O . iIII . o0O0Oooo0O + iI11I1II1I1I
if 2 - 2: ooOoO0O00 . o0o00Oo0O / I11i . IIiIiII11i / oO0o % ooOoO0O00
if 12 - 12: I11i
if 58 - 58: iI11I1II1I1I * Ii1i1i . oOOoOooOo . I1ii11iIi11i * Ii1i1i
if 63 - 63: OOooOOo . iIII * I11i - iIII % iIII
if 62 - 62: iIII - oOOoOooOo / oOOoOooOo
if 95 - 95: OOooOOo - ooOoO0O00 / o0O0Oooo0O . oOOoOooOo % IIIi11I1 - ooOoO0O00
if 12 - 12: IIIIiiII111
if 96 - 96: o0o00Oo0O
if 89 - 89: Ii1I - I1ii11iIi11i
if 26 - 26: oOOoOooOo % oOOoOooOo / IIiIiII11i / IIIIiiII111
if 2 - 2: ooOoO0O00 / Ii + oOo0O0Ooo
if 95 - 95: Ii1I / o0O00o % iI11I1II1I1I + o0o00Oo0O
if 6 - 6: o0O00o
if 73 - 73: I11i % I11i . IIIi11I1 * Ii1I - Ii1i1i
if 97 - 97: o0O00o
if 15 - 15: o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . o0O0Oooo0O
if 64 - 64: oOOoOooOo / ooOoO0O00
if 100 - 100: IIiIiII11i
if 16 - 16: Ii1i1i
if 96 - 96: I11i / o0O0Oooo0O % Ii1i1i - oOOoOooOo
if 35 - 35: IIIi11I1
if 90 - 90: Ii
if 47 - 47: oO0o . Ii
if 9 - 9: OOooOOo - iIII . ii % oOOoOooOo
if 13 - 13: oO0o * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - OOooOOo
if 43 - 43: IIIIiiII111 / o0O0Oooo0O * oOo0O0Ooo % oOOoOooOo % oOo0O0Ooo
if 18 - 18: oO0o
if 99 - 99: IIIIiiII111 / ooOO0O0ooOooO . Ii / iIII + ooOoO0O00 - iIII
if 50 - 50: ooOoO0O00
def oOo000o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0000OOo00 )
 I1i1iii1Ii = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'http' in url :
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiiiiIIii + 'Jizbox.png' )
 for url in I1Ii :
  if 'http' in url :
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiiiiIIii + 'Jizbox.png' )
 for url in I1i1iii1Ii :
  if 'http' in url :
   O0O00OOo ( '[COLOR' + II11iiii1Ii + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiiiiIIii + 'Jizbox.png' )
   if 46 - 46: oOOoOooOo + IIIIiiII111 - I1ii11iIi11i % IIIi11I1 + ii + iI11I1II1I1I
def OO00O0oOO ( url ) :
 I1iIII1IiiI = xbmc . Player ( OOoooOoO0Oo ( ) )
 import urlresolver
 try : I1iIII1IiiI . play ( url )
 except : pass
 if 83 - 83: ooOO0O0ooOooO - Ii + iI11I1II1I1I * I11i
 if 51 - 51: iI11I1II1I1I / o0O00o / IIIIiiII111
def i1Iiii1 ( ) :
 if 44 - 44: I1ii11iIi11i % I1ii11iIi11i
 if 58 - 58: IIIi11I1 * IIiIiII11i
 if 29 - 29: iI11I1II1I1I % OOooOOo % Ii1I / OOooOOo - Ii
 if 67 - 67: IIIi11I1 / Ii1i1i
 if 51 - 51: iIII % IIiIiII11i - I11i % oO0o * Ii * IIIIiiII111
 if 82 - 82: ii / oOo0O0Ooo * IIiIiII11i - ii % iI11I1II1I1I * oO0o
 if 32 - 32: Ii - OOooOOo * iIII . I1ii11iIi11i * oOOoOooOo
 if 21 - 21: IIIi11I1
 if 11 - 11: ooOO0O0ooOooO % Ii * o0o00Oo0O
 if 28 - 28: o0O0Oooo0O / iI11I1II1I1I + IIIi11I1 . Ii1I % IIIi11I1 + oO0o
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 8091 , iiiiiIIii + 'gofish.png' )
def oO0000O0o ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 8092 , iII11 )
 for url in next :
  iI ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 8093 , iiiiiIIii + 'Next.png' )
def o0O0oOooo ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0000OOo00 )
 i1i1I11I = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 in i1i1I11I :
  iII11 = iII11
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 8092 , iII11 )
 for url in next :
  iI ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 8093 , iiiiiIIii + 'Next.png' )
  if 1 - 1: OOooOOo
def O0oo0oO ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  yt . PlayVideo ( url )
  if 98 - 98: o0O00o
  if 68 - 68: oOOoOooOo - OOooOOo / ii . ooOoO0O00 + oO0o + o0O00o
  if 90 - 90: Ii1i1i
  if 55 - 55: I1ii11iIi11i % o0O00o + Ii - IIIi11I1 - IIiIiII11i
o0o0Oo0O0O0o = '{PQ},' ; o0OO0o00O00 = '{SC},' ; i111Ii1iI1 = '{XG},' ; O0o000O0Oo0 = '{JP},' ; o0O0oooOoOO0O = '{HW},' ; ii111iIii1 = '{RT},'
def O0Oo00oO0O00 ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oO0o000OooOoo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 Oo0o00OO0000 = 'http://onlinemovies.tube/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 IIi11i = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oo0OoOO0o0o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OO0OOO00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 ooOOo0o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiI1Iii1 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOO0ooIiIIi1I1I11Ii
 Ooooo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIiiiIiIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 89 - 89: IIiIiII11i + oOOoOooOo
 O00oo = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 OoOoooO000OO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 50 - 50: oO0o - oOo0O0Ooo * oOo0O0Ooo / o0O0Oooo0O % iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 iiIi1IIiIi = O0 ( i11I1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 O00OOoOOOO00O = O0 ( i11I1 )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 oOO00Oo = O0 ( IIi11i )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 i1iIIIi1i = O0 ( oo0OoOO0o0o )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 Ooo0OOO = O0 ( iIiiiIiIi )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 55 - 55: oO0o
 if 50 - 50: Ii1I . OOooOOo % I1ii11iIi11i . o0O00o . ooOO0O0ooOooO
 if 77 - 77: ooOoO0O00 + ii + oO0o % oOOoOooOo % Ii1i1i
 if 43 - 43: I1ii11iIi11i . Ii + ooOoO0O00
 if 83 - 83: IIIIiiII111 + OOooOOo % oOOoOooOo
 if 76 - 76: ooOoO0O00 % oOo0O0Ooo + ooOoO0O00
 if 2 - 2: IIIIiiII111 + IIIIiiII111
 if 51 - 51: ii + Ii
 II1 = O0 ( OoOoooO000OO )
 if 57 - 57: I1ii11iIi11i % I11i
 if Ooo0OOO != 'Failed' :
  II1iI1IIi = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Ooo0OOO )
  for Oo0o00OO0000 , iiIiii1IIIII in II1iI1IIi :
   Ii11iiI1 = O0 ( Oo0o00OO0000 )
   oO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii11iiI1 )
   for OOoooO00o0o , I1ii1Ii1 in oO0O :
    I1ii1Ii1 = ( I1ii1Ii1 . replace ( '.' , ' ' ) )
    if i11ii in I1ii1Ii1 . lower ( ) :
     if '.mkv' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + OOoooO00o0o , 222 , '' , '' , '' )
     elif '.mp4' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + OOoooO00o0o , 222 , '' , '' , '' )
     elif '.avi' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + OOoooO00o0o , 222 , '' , '' , '' )
     elif '.wav' in OOoooO00o0o :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + OOoooO00o0o , 222 , '' , '' , '' )
     else :
      OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + OOoooO00o0o , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 99 - 99: I11i / Ii / IIiIiII11i + IIIi11I1 . ooOoO0O00 + OOooOOo
      OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiIi1IIiIi )
  for Oo0o00OO0000 , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in I1Ii :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source Technica[/COLOR]' ) , Oo0o00OO0000 , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 7 - 7: oOo0O0Ooo / oOOoOooOo % oO0o + ooOO0O0ooOooO . I11i / iIII
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 84 - 84: IIIi11I1 + IIiIiII11i . I11i * I1ii11iIi11i
 if oOO00Oo != 'Failed' :
  I1i1iii1Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOO00Oo )
  for o0iIIIIi , iiIiii1IIIII in I1i1iii1Ii :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIi11i + o0iIIIIi ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if i1iIIIi1i != 'Failed' :
  o0oO0OO00ooOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIIi1i )
  for Oo0o00OO0000 , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in o0oO0OO00ooOO :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source RaizTv[/COLOR]' ) , Oo0o00OO0000 , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 68 - 68: Ii1i1i % Ii1i1i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 26 - 26: I11i . Ii1i1i * OOooOOo
    if 58 - 58: oOo0O0Ooo * oO0o * Ii / IIIi11I1 / oOo0O0Ooo
    if 46 - 46: o0O00o - oOo0O0Ooo + oO0o / iIII . Ii
    if 84 - 84: ii . oO0o / OOooOOo * ooOoO0O00
    if 6 - 6: iI11I1II1I1I * iI11I1II1I1I
    if 77 - 77: IIIi11I1 % ooOO0O0ooOooO + iI11I1II1I1I * Ii1i1i . o0O00o . I1ii11iIi11i
    if 29 - 29: Ii1I + ii . oO0o . ooOoO0O00 - ii * Ii
    if 19 - 19: Ii1I * o0o00Oo0O - oOOoOooOo
    if 27 - 27: IIIIiiII111 / I11i . OOooOOo * Ii1i1i * o0O0Oooo0O
    if 81 - 81: o0O0Oooo0O
    if 45 - 45: IIIi11I1 * IIiIiII11i * ii / ii * o0O0Oooo0O
    if 38 - 38: IIIIiiII111 . ii
    if 28 - 28: o0O0Oooo0O * ooOoO0O00 . Ii1I
    if 75 - 75: o0o00Oo0O / ooOO0O0ooOooO * oOOoOooOo - IIIi11I1 / ooOoO0O00
    if 61 - 61: iIII
    if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
    if 35 - 35: oOOoOooOo
    if 57 - 57: oO0o . I1ii11iIi11i + oOo0O0Ooo
    if 18 - 18: oOo0O0Ooo - Ii1I * iIII / Ii - I11i % I11i
    if 31 - 31: iIII
    if 100 - 100: Ii * Ii . iI11I1II1I1I % IIIIiiII111 * Ii1I
    if 17 - 17: Ii1i1i * o0O00o * Ii / Ii1I / Ii
    if 23 - 23: ii + Ii / I1ii11iIi11i / IIIIiiII111 . IIIIiiII111 * oOo0O0Ooo
    if 98 - 98: o0O00o
    if 23 - 23: iIII / ooOoO0O00 * oO0o
    if 51 - 51: IIIi11I1 - ii / ii % ii
    if 85 - 85: oO0o . I11i . oOo0O0Ooo
    if 75 - 75: iI11I1II1I1I - Ii1i1i % o0o00Oo0O % o0O00o
    if 6 - 6: I1ii11iIi11i % ooOO0O0ooOooO * oOOoOooOo - ooOoO0O00 . OOooOOo
    if 20 - 20: I1ii11iIi11i / o0O0Oooo0O . I1ii11iIi11i
    if 60 - 60: Ii1I - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . OOooOOo
    if 24 - 24: o0O00o * oOo0O0Ooo / IIIi11I1
    if 51 - 51: iI11I1II1I1I / iIII * oO0o * Ii1i1i + Ii1I . ii
    if 75 - 75: o0O00o / ii / o0o00Oo0O % IIIi11I1
    if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
    if 11 - 11: I11i * oO0o
    if 92 - 92: OOooOOo . I1ii11iIi11i * iIII
    if 86 - 86: o0o00Oo0O
    if 55 - 55: Ii1i1i / o0O0Oooo0O / Ii1I % oOOoOooOo % oOo0O0Ooo
    if 55 - 55: ooOO0O0ooOooO + ii % ooOoO0O00
 I1oo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 24 - 24: Ii1I - I1ii11iIi11i
 for i1oO00O in I1oo :
  oo0o0ooooo = OOO00O + i1oO00O + I11iii1Ii
  Ooo0OOO = O0 ( oo0o0ooooo )
  if Ooo0OOO != 'Failed' :
   II1iI1IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ooo0OOO )
   for Oo0o00OO0000 , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in II1iI1IIi :
    if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
     oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , Oo0o00OO0000 , 222 , ii1i , Oo00OO0 , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 36 - 36: oOo0O0Ooo . IIIi11I1 % IIiIiII11i * o0O00o
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 34 - 34: iIII % IIIIiiII111 - oOOoOooOo - oOo0O0Ooo
 I1oo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 44 - 44: Ii1i1i . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
 if 22 - 22: iIII * Ii1I . ii / I1ii11iIi11i / Ii1i1i
 for i1oO00O in I1oo :
  oo0o0ooooo = oO0o000OooOoo + i1oO00O
  OoooOo0 = O0 ( oo0o0ooooo )
  if OoooOo0 != 'Failed' :
   IiI1Ii1ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( OoooOo0 )
   for o0iIIIIi , iiIiii1IIIII in IiI1Ii1ii :
    if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
     O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oO0o000OooOoo + i1oO00O + o0iIIIIi ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 54 - 54: o0O0Oooo0O % Ii1i1i + oOOoOooOo
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: Ii1i1i / ooOO0O0ooOooO * o0O0Oooo0O . Ii1i1i
def O0O0o0o0o ( ) :
 if 25 - 25: Ii1I / Ii1I
 if 79 - 79: I1ii11iIi11i - oO0o % I1ii11iIi11i . IIiIiII11i
 if 84 - 84: oOOoOooOo * ii + o0o00Oo0O
 if 84 - 84: ooOoO0O00 . iIII . ooOoO0O00 . I1ii11iIi11i
 if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
 if 5 - 5: iI11I1II1I1I * Ii + oO0o + iIII * o0o00Oo0O % oOOoOooOo
 if 88 - 88: I11i / Ii * Ii1I
 if 23 - 23: o0o00Oo0O / IIIIiiII111
 if 66 - 66: ooOoO0O00 % ii * Ii + ooOO0O0ooOooO * o0o00Oo0O / oO0o
 if 14 - 14: oOo0O0Ooo . o0O00o
 if 29 - 29: ii / o0O00o + OOooOOo - o0O0Oooo0O + o0O00o . ooOoO0O00
 if 26 - 26: Ii - IIiIiII11i
 if 43 - 43: oOo0O0Ooo
 if 35 - 35: oOOoOooOo + OOooOOo * ii - IIiIiII11i
 if 19 - 19: ooOoO0O00 / Ii1i1i / OOooOOo . oOo0O0Ooo / Ii1i1i % I11i
 if 39 - 39: oOOoOooOo - ii
 if 88 - 88: ooOoO0O00 + iI11I1II1I1I * Ii - ii % I11i
 if 74 - 74: oOOoOooOo - Ii
 if 34 - 34: o0O00o + o0O0Oooo0O + I1ii11iIi11i / IIiIiII11i
 if 33 - 33: Ii1i1i . ooOoO0O00 - IIiIiII11i - oO0o
 if 31 - 31: iIII - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
 if 46 - 46: o0O00o * oO0o / IIIi11I1 + I1ii11iIi11i
 if 24 - 24: oOOoOooOo % IIIi11I1 . o0o00Oo0O * I1ii11iIi11i
 if 52 - 52: o0o00Oo0O . o0O0Oooo0O + IIIIiiII111 / Ii
 if 52 - 52: ooOO0O0ooOooO % I1ii11iIi11i * IIiIiII11i
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
 if 27 - 27: ooOoO0O00 - ooOO0O0ooOooO + IIIi11I1
 if 3 - 3: o0O00o % o0O0Oooo0O . ii
 if 19 - 19: o0O0Oooo0O * Ii1i1i - ooOO0O0ooOooO
 if 78 - 78: oO0o - Ii1i1i / IIIi11I1
 if 81 - 81: OOooOOo
 if 21 - 21: IIIIiiII111 / IIIi11I1 % o0O00o
 if 51 - 51: iIII + oOOoOooOo / oOo0O0Ooo
 if 3 - 3: iI11I1II1I1I / IIIi11I1 % ooOO0O0ooOooO . Ii1i1i - Ii1i1i
 if 55 - 55: Ii % ii + o0o00Oo0O
 if 7 - 7: oOOoOooOo - Ii * IIIIiiII111 / Ii1i1i - I11i
 if 62 - 62: I11i - iI11I1II1I1I . iIII . Ii1i1i * Ii1i1i
 if 24 - 24: iIII
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / iIII
 if 60 - 60: oOOoOooOo - Ii1i1i . oOo0O0Ooo * ooOO0O0ooOooO * Ii
 OOoooO00o0o = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 i11I1 = 'http://onlinemovies.tube/?s=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 IIi11i = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 oo0OoOO0o0o = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 ooOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IiI1Iii1 = 'http://www.tvmaze.com/search?q=' + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 Ooooo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iIiiiIiIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 29 - 29: oO0o - I1ii11iIi11i . ooOO0O0ooOooO / oO0o % Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 26 - 26: oOOoOooOo . o0O0Oooo0O / IIiIiII11i % Ii1i1i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 82 - 82: IIIi11I1 % o0o00Oo0O % iI11I1II1I1I % o0O00o + Ii
 if 64 - 64: ooOoO0O00 / o0O00o . o0O00o - o0O0Oooo0O % IIIi11I1 . IIiIiII11i
 iI1iiIi1 = O0 ( OOoooO00o0o )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 iiIi1IIiIi = O0 ( i11I1 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 oOO00Oo = O0 ( IIi11i )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 i1iIIIi1i = O0 ( oo0OoOO0o0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 OoooOo0 = O0 ( ooOOo0o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 i1I1IiI1ii = O0 ( IiI1Iii1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/11 Links" )
 O00OOoOOOO00O = O0 ( Ooooo )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 Ooo0OOO = O0 ( iIiiiIiIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 78 - 78: o0O0Oooo0O - o0o00Oo0O - o0O0Oooo0O . iI11I1II1I1I % Ii1I . ii
 if 64 - 64: o0O00o
 if Ooo0OOO != 'Failed' :
  II1iI1IIi = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Ooo0OOO )
  for Oo0o00OO0000 , iiIiii1IIIII in II1iI1IIi :
   Ii11iiI1 = O0 ( Oo0o00OO0000 )
   oO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii11iiI1 )
   for OOoooO00o0o , I1ii1Ii1 in oO0O :
    if i11ii in I1ii1Ii1 . lower ( ) :
     OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']*' + I1ii1Ii1 + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + OOoooO00o0o , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 21 - 21: I11i - oOOoOooOo * ii . ii
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if O00OOoOOOO00O != 'Failed' :
  iI11II1i1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00OOoOOOO00O )
  for Oo0o00OO0000 , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in iI11II1i1I1 :
   if i11ii in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source HeroVision[/COLOR]' ) , Oo0o00OO0000 , 1016 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 17 - 17: IIIi11I1 - IIIIiiII111 % oOo0O0Ooo * IIIi11I1 * iI11I1II1I1I . I11i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 58 - 58: ooOO0O0ooOooO - IIiIiII11i + o0o00Oo0O
 if i1I1IiI1ii != 'Failed' :
  OoOooO = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( i1I1IiI1ii )
  for Oo0o00OO0000 , iII11 , iiIiii1IIIII in OoOooO :
   i11I1 = 'http://www.tvmaze.com' + Oo0o00OO0000 . replace ( '"' , '' )
   Ii1iIi111i1i1 = requests . get ( i11I1 ) . content
   Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
   for i11II1I11I1 in Ii1i1iI1iIIi :
    if not '<div>' in i11II1I11I1 :
     IIOO0ooOo0OoOo0 = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
    iII11 = 'http:' + iII11
    iiIiii1IIIII = iiIiii1IIIII . replace ( '&#039;' , '' )
    if iiIiii1IIIII == '' :
     oOo = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( Oo0o00OO0000 ) )
     for iiIiii1IIIII in oOo :
      iiIiii1IIIII = iiIiii1IIIII . replace ( '-' , ' ' )
   Iii ( iiIiii1IIIII + '-[COLORgold] source Scraper[/COLOR]' , i11I1 , 9110002 , iII11 , iIi1ii1I1 , IIOO0ooOo0OoOo0 , '' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 20 , "" , "Getting Scraper Links" )
   if 54 - 54: iI11I1II1I1I - o0O00o - o0O00o
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  iI1iI = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  for Oo0o00OO0000 , iII11 , iiIiii1IIIII , O0O0 in I1Ii :
   if i11ii in iiIiii1IIIII . lower ( ) :
    if 'season' in O0O0 :
     iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , Oo0o00OO0000 , 90054 , iII11 , iII11 , '' )
    if 'episodes' in O0O0 :
     iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , Oo0o00OO0000 , 90044 , iII11 , iII11 , '' )
  for Oo0o00OO0000 in iI1iI :
   iI ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , Oo0o00OO0000 , 90053 , iiiiiIIii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 18 - 18: Ii + iI11I1II1I1I . Ii
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iI1iiIi1 != 'Failed' :
  I1iiIIIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iI1iiIi1 )
  for Oo0o00OO0000 , iiIiii1IIIII , iII11 in I1iiIIIi11 :
   if i11ii in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( iiIiii1IIIII ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , Oo0o00OO0000 , 8022 , iII11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 63 - 63: IIIIiiII111 - oO0o * IIIi11I1
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 89 - 89: IIIIiiII111 / I1ii11iIi11i
    if 66 - 66: I11i + OOooOOo % ii . iIII
    if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
    if 93 - 93: ooOoO0O00 + o0O0Oooo0O / oO0o - iIII % I1ii11iIi11i / Ii1i1i
    if 1 - 1: I1ii11iIi11i / Ii1i1i . Ii % IIIi11I1 + I11i + o0o00Oo0O
    if 54 - 54: o0O0Oooo0O + oOOoOooOo % o0O00o
    if 83 - 83: I11i * iI11I1II1I1I
    if 36 - 36: OOooOOo + IIiIiII11i - oO0o % oOOoOooOo * ooOoO0O00
    if 4 - 4: Ii1i1i + oO0o * Ii1I
 if oOO00Oo != 'Failed' :
  I1i1iii1Ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOO00Oo )
  for iiIiii1IIIII in I1i1iii1Ii :
   if i11ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( IIi11i + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 13 - 13: OOooOOo - o0O00o * iI11I1II1I1I * o0o00Oo0O
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if i1iIIIi1i != 'Failed' :
  o0oO0OO00ooOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1iIIIi1i )
  for iiIiii1IIIII in o0oO0OO00ooOO :
   if i11ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( oo0OoOO0o0o + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 26 - 26: ii + ooOO0O0ooOooO + oO0o . o0o00Oo0O
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if OoooOo0 != 'Failed' :
  IiI1Ii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoooOo0 )
  for Oo0o00OO0000 , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in IiI1Ii1ii :
   if i11ii in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] Source Scooby[/COLOR]' ) , Oo0o00OO0000 , 1016 , ii1i , Oo00OO0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 46 - 46: ii - I1ii11iIi11i * o0O0Oooo0O * IIIi11I1 * o0O0Oooo0O . ooOO0O0ooOooO
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 96 - 96: Ii1i1i / o0O00o % I11i + iIII
 II111IIIII = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for i1oO00O in II111IIIII :
  oo0o0ooooo = OOO00O + i1oO00O + I11iii1Ii
  Oo0O0000Oo00o = O0 ( oo0o0ooooo )
  if Oo0O0000Oo00o != 'Failed' :
   oO0o0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oo0O0000Oo00o )
   for iiIiii1IIIII , i11II1I11I1 , Oo0o00OO0000 , iII11 , ooo0O0o00O , oOo0 in oO0o0Oo :
    if i11ii in iiIiii1IIIII . lower ( ) :
     OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , Oo0o00OO0000 , oOo0 , iII11 , ooo0O0o00O , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 46 - 46: oO0o * oOo0O0Ooo
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 25 - 25: o0O0Oooo0O . o0O00o % o0o00Oo0O % ooOoO0O00
     if 53 - 53: o0o00Oo0O % oOOoOooOo
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iii111iI1i11 ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o00OO0000 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( oOO0ooIiIIi1I1I11Ii ) . replace ( ' ' , '+' )
 if 67 - 67: iIII * ooOoO0O00 - ooOoO0O00 . OOooOOo % ooOO0O0ooOooO . I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0000OOo00 = O0 ( Oo0o00OO0000 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 14 - 14: ooOO0O0ooOooO - I1ii11iIi11i % Ii1i1i . o0O0Oooo0O
 if oO0000OOo00 != 'Failed' :
  I1Ii = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , iiIiii1IIIII in I1Ii :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + Oo0o00OO0000 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 14 - 14: oOOoOooOo / o0o00Oo0O - oOo0O0Ooo / Ii1I / oO0o + ooOO0O0ooOooO
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
O0O0O = '{ZH},' ; O0o0OO0oOo0OO = '{IX},' ; I1i11I11 = '{LM},'
if 1 - 1: OOooOOo * iI11I1II1I1I
def iiooOOOo ( url ) :
 ooOO = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( ooOO )
 for url , ooO0000o00O , O0Ooo , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( ooO0000o00O ) . replace ( 'Sezon' , ' Season ' ) + ( O0Ooo ) . replace ( 'Bölüm' , ' Episode ' ) + iiIiii1IIIII , url , 8063 , '' )
  if 97 - 97: oOo0O0Ooo
  if 63 - 63: o0o00Oo0O - OOooOOo / Ii / ii / oOOoOooOo / IIiIiII11i
  if 45 - 45: IIiIiII11i . oO0o + oO0o * iI11I1II1I1I
  if 23 - 23: o0O00o * OOooOOo % Ii1i1i / Ii1i1i - oOOoOooOo - IIIi11I1
def O00 ( url ) :
 ooOO = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( ooOO )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( iiIiii1IIIII , url , 222 , '' )
  if 17 - 17: IIiIiII11i + oOOoOooOo + IIIIiiII111 . Ii1I
  if 36 - 36: oOo0O0Ooo
  if 75 - 75: oOo0O0Ooo % IIiIiII11i * ooOO0O0ooOooO % ooOoO0O00 % IIIi11I1
  if 93 - 93: OOooOOo
def iio0ooo ( ) :
 if 77 - 77: I11i % IIIIiiII111 / ooOoO0O00 . I1ii11iIi11i
 ooOO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i1iI1iIIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( ooOO )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , O0Ooo in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII + '  -  ' + ( O0Ooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Oo0o00OO0000 , 8063 , iII11 )
  if 77 - 77: Ii % o0O0Oooo0O - I1ii11iIi11i - ooOO0O0ooOooO * IIIi11I1
def iiiII1I1 ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 8002 , iII11 )
def oo0oii1IIi1Ii1II1 ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , time , url , iiIiii1IIIII , Ii1i111iI in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '%s %s' % ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , time ) , url , 1015 , iII11 , Ii1i111iI )
  if 60 - 60: IIIi11I1
def I11Ooo0oOoOoOoo ( ) :
 if 40 - 40: Ii1I . oO0o
 iI ( 'Coronation Street' , '' , 8001 , '' )
 iI ( 'Eastenders' , '' , 8002 , '' )
 iI ( 'Emmerdale' , '' , 8003 , '' )
 iI ( 'Hollyoaks' , '' , 8004 , '' )
 iI ( 'Im a Celebrity' , '' , 8005 , '' )
 if 30 - 30: oOOoOooOo % oOo0O0Ooo . ooOO0O0ooOooO
 if 48 - 48: OOooOOo
 if 28 - 28: iIII / o0o00Oo0O * o0O00o - o0O0Oooo0O % o0O00o
 if 8 - 8: iIII / Ii1I % Ii1I % Ii1i1i + IIIIiiII111
def oo0O0O ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Holly' in iiIiii1IIIII :
   iII11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in Oo0o00OO0000 :
    O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 98 - 98: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 74 - 74: OOooOOo . Ii1I
def iIi1Ii ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'East' in iiIiii1IIIII :
   iII11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in Oo0o00OO0000 :
    O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 40 - 40: Ii . o0O00o % o0o00Oo0O
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 64 - 64: I11i . iI11I1II1I1I
def O0o0OooOO ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Emmer' in iiIiii1IIIII :
   iII11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in Oo0o00OO0000 :
    O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 69 - 69: I1ii11iIi11i + Ii1I + iI11I1II1I1I / ii - I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: iI11I1II1I1I + oOo0O0Ooo * OOooOOo % oOo0O0Ooo / IIIIiiII111
def Oo0ooOoo ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Coro' in iiIiii1IIIII :
   iII11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in Oo0o00OO0000 :
    O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 57 - 57: oOo0O0Ooo - ooOoO0O00 + IIIIiiII111 * I1ii11iIi11i % oO0o
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: iI11I1II1I1I % OOooOOo + oO0o / Ii
def o0oOOo0oO0o ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Celeb' in iiIiii1IIIII :
   iII11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in Oo0o00OO0000 :
    O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 20 - 20: I11i . I1ii11iIi11i . Ii / IIIi11I1 + ooOO0O0ooOooO
def iIIiii ( name , url ) :
 ii111Ii = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ii111Ii :
  OOo0o0oOOOO00 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  O0o0O0 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( O0o0O0 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  O0o0O0 = open_url ( url )
  oo0O = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( O0o0O0 ) [ - 1 ]
  OOo0o0oOOOO00 = oo0O . replace ( '\\/' , '/' )
 Oo0oO = xbmcgui . ListItem ( name , '' , '' )
 Oo0oO . setPath ( OOo0o0oOOOO00 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0oO )
 if 20 - 20: IIiIiII11i - IIIi11I1
 if 47 - 47: IIIi11I1 . ii . iIII / OOooOOo
def IiiIIiII ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 Ii1i1iI1iIIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , Oo0o00OO0000 , 7071 , iiiiiIIii + 'popcorn.png' )
 for Oo0o00OO0000 , iiIiii1IIIII in I1Ii :
  iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , Oo0o00OO0000 , 7071 , iiiiiIIii + 'popcorn.png' )
  if 25 - 25: IIIi11I1 % ooOO0O0ooOooO
def II1i1i1111IIIii ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i1iI1iIIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Movies' in iiIiii1IIIII :
   iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( Oo0o00OO0000 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiiiiIIii + 'popcorn.png' )
def ii11IiiiIi1iI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iII11 )
 for url in I1Ii :
  iI ( '[COLOR' + II11iiii1Ii + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiiiiIIii + 'Next.png' )
  if 23 - 23: IIiIiII11i - IIiIiII11i / ooOO0O0ooOooO - o0O00o - Ii
  if 68 - 68: o0o00Oo0O / IIIIiiII111
def oOOO ( url ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i1iI1iIIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  if '{{' in iiIiii1IIIII :
   pass
  else :
   iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iII11 )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
o0OO0O = '{UJ},' ; Ii1Oo0O = '{WE},' ; OOOo0O00oO00 = '{WP},' ; IIiIIIi1I = '{PP},'
def o0II1IIII11Ii1 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  if '{{' in iiIiii1IIIII :
   pass
  else :
   iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iII11 )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII11I1iIiI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  IiIiI1111 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIiI1111 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: o0o00Oo0O - iIII - Ii1I + oOo0O0Ooo - o0O00o / Ii1I
 if 81 - 81: Ii1i1i % oO0o
 if 22 - 22: ooOoO0O00
def Oo0OOO0oo0o ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '(cooltvseries.com)' in iiIiii1IIIII :
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiiiiIIii + 'CoolSeries.png' )
 for url , iiIiii1IIIII in I1Ii :
  if '(cooltvseries.com)' in iiIiii1IIIII :
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiiiiIIii + 'CoolSeries.png' )
def II11 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0o0oo0oOO0oO ( ( url ) . replace ( ' ' , '%20' ) )
oOO0 = '{XX},' ; o0oOOOO00O0 = '{UD},' ; iIiI1iIi1 = '{YT},' ; oOOo0OO0oo = '{JS},' ; OOO0o0ooO0 = '{PF},'
if 16 - 16: IIIIiiII111 . o0O00o . oO0o
def ii1OoO00o ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 Ii1i1iI1iIIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  O0O00OOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( Oo0o00OO0000 ) ) , 222 , iII11 )
  if 76 - 76: o0o00Oo0O + IIiIiII11i * oO0o
def Ii1iiII11ii1 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( O0o0O0 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'youtu' in url :
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iII11 )
 for url in next :
  iI ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 7050 , iiiiiIIii + 'Next.png' )
  if 1 - 1: I11i
def IIi1II ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 36 - 36: o0O00o . o0O00o
def IIii1iI11 ( url ) :
 O0o0O0 = i11oO0oOo0
 Ii1i1iI1iIIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iII11 )
  if 2 - 2: IIIIiiII111 * iIII * oOOoOooOo + Ii + ooOO0O0ooOooO
  if 81 - 81: I11i * oO0o
  if 18 - 18: Ii / I11i - ooOO0O0ooOooO . iIII * ooOoO0O00
  if 67 - 67: Ii1i1i
  if 64 - 64: OOooOOo + IIIIiiII111 * OOooOOo - oOo0O0Ooo * ii
def iiiiii ( ) :
 if 76 - 76: IIiIiII11i % oOOoOooOo - Ii1I
 iI ( 'All Channels' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Entertainment' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Movies' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Music' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'News' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Sports' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Documentary' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Kids' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Food' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Religious' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'USA Channels' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 iI ( 'Other' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 if 50 - 50: IIiIiII11i / oOo0O0Ooo . Ii1i1i % Ii
 if 66 - 66: ooOO0O0ooOooO / IIIi11I1 / IIIIiiII111
def i1Io0ooo ( Cat_Name ) :
 if 5 - 5: iIII
 oOO0ooOO = False
 IiiI11iI = '0'
 if Cat_Name == 'All Channels' : oOO0ooOO = True
 if Cat_Name == 'Entertainment' : IiiI11iI = '1'
 if Cat_Name == 'Movies' : IiiI11iI = '2'
 if Cat_Name == 'Music' : IiiI11iI = '3'
 if Cat_Name == 'News' : IiiI11iI = '4'
 if Cat_Name == 'Sports' : IiiI11iI = '5'
 if Cat_Name == 'Documentary' : IiiI11iI = '6'
 if Cat_Name == 'Kids' : IiiI11iI = '7'
 if Cat_Name == 'Food' : IiiI11iI = '8'
 if Cat_Name == 'Religious' : IiiI11iI = '9'
 if Cat_Name == 'USA Channels' : IiiI11iI = '10'
 if Cat_Name == 'Other' : IiiI11iI = '11'
 if 88 - 88: IIiIiII11i % ii - ooOoO0O00 - oO0o * iIII
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i1iI1iIIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( O0o0O0 )
 print 'Len Match: >>>' + str ( len ( Ii1i1iI1iIIi ) )
 for iiIiii1IIIII , iII11 , I1iII1i1I1 in Ii1i1iI1iIIi :
  iII1I1I11 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iII11 ) . replace ( '\\' , '' )
  if I1iII1i1I1 == IiiI11iI :
   iI ( iiIiii1IIIII , '' , 7022 , iII1I1I11 )
  elif oOO0ooOO == True :
   iI ( iiIiii1IIIII , '' , 7022 , iII1I1I11 )
  else : pass
  if 47 - 47: iI11I1II1I1I / I1ii11iIi11i + oOo0O0Ooo + ooOO0O0ooOooO
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 60 - 60: oO0o
def iiIIII11i1 ( Search_Name ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i1iI1iIIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , Oo0o00OO0000 , i11I1 , IIi11i in Ii1i1iI1iIIi :
  iII1I1I11 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iII11 ) . replace ( '\\' , '' )
  O0O00OOo ( Search_Name + ': Link 1' , ( Oo0o00OO0000 ) . replace ( '\\' , '' ) , 222 , iII1I1I11 )
  O0O00OOo ( Search_Name + ': Link 2' , ( i11I1 ) . replace ( '\\' , '' ) , 222 , iII1I1I11 )
  O0O00OOo ( Search_Name + ': Link 3' , ( IIi11i ) . replace ( '\\' , '' ) , 222 , iII1I1I11 )
  if 58 - 58: IIIIiiII111
def o00OO0O00O0 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  O0O00OOo ( iiIiii1IIIII , ( Oo0o00OO0000 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiiiiIIii + 'english.png' )
def IiiI11I ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  O0O00OOo ( iiIiii1IIIII , ( Oo0o00OO0000 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiiiiIIii + 'xxx.png' )
def ooOOoOo ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  O0O00OOo ( iiIiii1IIIII , ( Oo0o00OO0000 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiiiiIIii + 'vod(1).png' )
  if 59 - 59: Ii1i1i * ii - IIIIiiII111
def iII111IiO00O ( url ) :
 url
 IIi1IIIi = xbmcgui . ListItem ( iiIiii1IIIII , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIi1IIIi )
 return
 if 64 - 64: o0O00o . ii - Ii1I
 if 79 - 79: IIIi11I1 + I11i % IIIIiiII111 . ooOO0O0ooOooO
def I11iiI ( ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']All WorkOuts[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) , 7085 , iiiiiIIii + 'Fitness.png' , iIi1ii1I1 , '' )
 if 14 - 14: Ii1I . ooOO0O0ooOooO + ooOoO0O00
def I1IIIi1iI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '"id":.+?,"title":(.+?),"is_featured":1,"minutes":(.+?),"burnmin":(.+?),"burnmax":(.+?),"burnavg":(.+?),"difficulty":(.+?),"image":"([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '"next_page_url":"([^"]*)"' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , time , I111iII1I111 , OoO , O0OOOO0 , OooOOo0ooO , iII11 , url , IiioO , oO0OooO0O in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( iiIiii1IIIII ) . replace ( '"' , '' ) , 'https://www.fitnessblender.com/videos/' + url , 7086 , 'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-' + iII11 , '' , ( 'Calorie burn:[CR]' + I111iII1I111 + ' - ' + OoO + ' Average = ' + O0OOOO0 + '[CR][CR]Difficulty = ' + OooOOo0ooO + '[CR][CR]Equipment Needed: ' + IiioO + '[CR][CR]Focus: ' + oO0OooO0O ) . replace ( '"' , '' ) )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 for url in I1Ii :
  iI ( 'NEXT' , ( 'https://www.fitnessblender.com/videos' + url ) . replace ( '\/' , '' ) , 7085 , iiiiiIIii + 'Next.png' )
  if 45 - 45: o0O00o
def IIIIi1Ii111 ( url , iconimage , description ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 iII11 = iconimage
 i11II1I11I1 = description
 Ii1i1iI1iIIi = re . compile ( '<div class="responsive-video">.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( 'PLAY' , url , 8043 , iII11 , '' , i11II1I11I1 )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 OooO0oO0O0O = re . compile ( '<div class="article__content">(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for I1iiiiiII1I1I in OooO0oO0O0O :
  IIII1iII = ( I1iiiiiII1I1I ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  OoOOoOooooOOo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iII11 , '' , IIII1iII )
  if 71 - 71: o0O0Oooo0O
def OO00 ( INFO ) :
 I1iI1ii1II ( 'info for workout' , INFO )
 if 21 - 21: Ii1I
 if 9 - 9: IIIi11I1 * oOOoOooOo - ii / o0o00Oo0O
 if 86 - 86: oOo0O0Ooo . I11i % Ii1i1i - OOooOOo . ooOoO0O00
def iiii1II ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( ( iiIiii1IIIII ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiiiiIIii + 'Sport.png' )
def O00OOOO ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , url , 9032 , iiiiiIIii + 'icon.png' )
def OOI11i1iiI1 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '=' in iiIiii1IIIII :
   pass
  else :
   O0O00OOo ( ( iiIiii1IIIII ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiiiiIIii + 'icon.png' )
def IiIIi1I1iII ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '=' in iiIiii1IIIII :
   pass
  else :
   O0O00OOo ( iiIiii1IIIII , url , 222 , iiiiiIIii + 'icon.png' )
   if 100 - 100: Ii % oOOoOooOo . oOOoOooOo - Ii1I % I1ii11iIi11i - IIIIiiII111
   if 12 - 12: OOooOOo + iIII . oO0o * Ii * iIII * o0O0Oooo0O
   if 28 - 28: iI11I1II1I1I * iI11I1II1I1I * oOOoOooOo % Ii1I / Ii
def oOoOO0o ( url ) :
 Iii ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , iII11 , url in Ii1i1iI1iIIi :
  if 'music' in url :
   Iii ( iiIiii1IIIII , url , 90036 , iII11 , iII11 , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   Iii ( iiIiii1IIIII , url , 90039 , iII11 , iII11 , '' , '' )
def OOoOo ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  Ooo00OoOOO ( iiIiii1IIIII , url , 100009 , iII11 , iII11 , '' , '' )
  if 3 - 3: ooOoO0O00
def oOO0o ( url ) :
 Iii ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 Iii ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 O0o0O0 = requests . get ( url ) . text
 i1ii1II1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1II1I11i1 = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  Ii1iIi111i1i1 = requests . get ( url ) . text
  OOOi1I1IIII = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
  for iI11iii111 in OOOi1I1IIII :
   i1II11II1 = requests . get ( iI11iii111 ) . text
   Ii1i1iI1iIIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( i1II11II1 )
   for oOoO00o , iiIiI11IiI1I , i1iII1IiiIiI1 , oOO0oOooo , I1I1IiI1 in Ii1i1iI1iIIi :
    if oOoO00o == 'xyz' :
     IIi1i1111i = 'http://xyz.streamjunkie.tv/hls/' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( iiIiii1IIIII , IIi1i1111i , 1001111 , iII11 , iII11 , '' , '' )
    else :
     IIi1i1111i = 'http://' + oOO0oOooo + '.' + i1iII1IiiIiI1 + '.' + iiIiI11IiI1I + '.' + oOoO00o + '/hls/,' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( iiIiii1IIIII , IIi1i1111i , 1001111 , iII11 , iII11 , '' , '' )
 for o0o0oOoOO0O in i1ii1II1ii :
  Iii ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0o0oOoOO0O , 1000111 , '' , '' , '' , '' )
  if 55 - 55: o0O0Oooo0O / Ii / OOooOOo
  if 25 - 25: I1ii11iIi11i / I1ii11iIi11i
  if 74 - 74: IIIi11I1
def IiioOoo0ooo ( ) :
 Iii ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 25 - 25: o0o00Oo0O + IIIi11I1 / IIIIiiII111
 if 51 - 51: iIII
def OooiIII ( url , name ) :
 Iii ( name , '' , '' , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 O0o0O0 = requests . get ( url ) . text
 i1ii1II1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1II1I11i1 = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iII11 , name in Ii1i1iI1iIIi :
  Ii1iIi111i1i1 = requests . get ( url ) . text
  OOOi1I1IIII = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
  for iI11iii111 in OOOi1I1IIII :
   i1II11II1 = requests . get ( iI11iii111 ) . text
   Ii1i1iI1iIIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( i1II11II1 )
   for oOoO00o , iiIiI11IiI1I , i1iII1IiiIiI1 , oOO0oOooo , I1I1IiI1 in Ii1i1iI1iIIi :
    if oOoO00o == 'xyz' :
     IIi1i1111i = 'http://xyz.streamjunkie.tv/hls/' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , IIi1i1111i , 1001111 , iII11 , iII11 , '' , '' )
    else :
     IIi1i1111i = 'http://' + oOO0oOooo + '.' + i1iII1IiiIiI1 + '.' + iiIiI11IiI1I + '.' + oOoO00o + '/hls/,' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , IIi1i1111i , 1001111 , iII11 , iII11 , '' , '' )
     if 95 - 95: Ii1i1i
 for o0o0oOoOO0O in i1ii1II1ii :
  Iii ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0o0oOoOO0O , 1003111 , '' , '' , '' , '' )
  if 8 - 8: IIIi11I1 . oOo0O0Ooo - oOo0O0Ooo
  if 34 - 34: ooOO0O0ooOooO . Ii - o0O00o
def O0o0 ( ) :
 Iii ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 18 - 18: Ii . o0o00Oo0O / oO0o * ooOO0O0ooOooO + o0O0Oooo0O
 if 91 - 91: oOo0O0Ooo
 if 84 - 84: o0o00Oo0O % Ii1i1i
def iiIi1I1i1i ( url , name ) :
 Iii ( name , '' , '' , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 O0o0O0 = requests . get ( url ) . text
 i1ii1II1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1II1I11i1 = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iII11 , name in Ii1i1iI1iIIi :
  Ii1iIi111i1i1 = requests . get ( url ) . text
  OOOi1I1IIII = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( Ii1iIi111i1i1 )
  for iI11iii111 in OOOi1I1IIII :
   i1II11II1 = requests . get ( iI11iii111 ) . text
   Ii1i1iI1iIIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( i1II11II1 )
   for oOoO00o , iiIiI11IiI1I , i1iII1IiiIiI1 , oOO0oOooo , I1I1IiI1 in Ii1i1iI1iIIi :
    if oOoO00o == 'xyz' :
     IIi1i1111i = 'http://xyz.streamjunkie.tv/hls/' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , IIi1i1111i , 1001111 , iII11 , iII11 , '' , '' )
    else :
     IIi1i1111i = 'http://' + oOO0oOooo + '.' + i1iII1IiiIiI1 + '.' + iiIiI11IiI1I + '.' + oOoO00o + '/hls/,' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , IIi1i1111i , 1001111 , iII11 , iII11 , '' , '' )
     if 14 - 14: Ii
 for o0o0oOoOO0O in i1ii1II1ii :
  Iii ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0o0oOoOO0O , 1005111 , '' , '' , '' , '' )
def I1III111i ( name , url ) :
 import urlresolver
 try :
  iiI1iii = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiI1iii , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 100 - 100: iI11I1II1I1I * IIIi11I1
 if 5 - 5: o0o00Oo0O - ooOO0O0ooOooO - Ii
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / oOOoOooOo
def oo0OoooOo0 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 Ii1i1iI1iIIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Daily' in iiIiii1IIIII :
   iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 9008 , o0 )
def ooo00OO ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , o0 )
def iI1iIIIiIi ( url ) :
 O0O00OOo ( '[COLOR' + II11iiii1Ii + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 O0O00OOo ( '[COLOR' + II11iiii1Ii + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 O0O00OOo ( '[COLOR' + II11iiii1Ii + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  O0O00OOo ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) , url , 222 , o0 )
  if 41 - 41: ii + oOOoOooOo + oOo0O0Ooo + IIiIiII11i * Ii1i1i
def i1IIIii1Ii1 ( ) :
 O0o0O0 = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '.m3u' in Oo0o00OO0000 :
   iI ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + Oo0o00OO0000 ) , 9011 , iiiiiIIii + 'disclose.png' )
def o000O00OO00O ( url ) :
 O0o0O0 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  O0O00OOo ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 77 - 77: o0O00o - ii % o0O0Oooo0O / I1ii11iIi11i % ii * iI11I1II1I1I
def o00O0O ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'category' in Oo0o00OO0000 :
   iI ( iiIiii1IIIII , 'http://www.disclose.tv/' + Oo0o00OO0000 , 7010 , iiiiiIIii + 'disclose.png' )
   if 48 - 48: OOooOOo
   if 65 - 65: iIII * ooOoO0O00 - o0O0Oooo0O / I11i / oO0o - IIIi11I1
def IIiIII ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( O0o0O0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , 'http://www.disclose.tv/' + url , 7011 , iII11 )
 for url in next :
  iI ( 'NEXT' , url , 7010 , iiiiiIIii + 'Next.png' )
  if 76 - 76: o0o00Oo0O % o0O00o . I11i % o0O00o . I11i
  if 20 - 20: Ii . OOooOOo % I1ii11iIi11i
def iiiIIII1Ii1 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( O0o0O0 )
 I1i1iii1Ii = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  if 'http' in url :
   O0O00OOo ( 'video/flv' , url , 222 , iiiiiIIii + 'disclose.png' )
 for url , iiIiii1IIIII in I1Ii :
  O0O00OOo ( iiIiii1IIIII , url , 222 , iiiiiIIii + 'disclose.png' )
 for url in I1i1iii1Ii :
  O0O00OOo ( 'YT Link' , url , 8043 , iiiiiIIii + 'disclose.png' )
  if 58 - 58: oOOoOooOo
  if 98 - 98: Ii1i1i / oO0o % ii
def O0OO0OO0oo ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiiiiIIii + 'icon.png' )
  if 14 - 14: Ii1I * Ii * Ii1I + IIIi11I1 - iI11I1II1I1I * ooOO0O0ooOooO
def oOOO0 ( name , url , img ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 IiIio0oO0O = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0000OOo00 )
 IiiiiII1Ii1 = len ( IiIio0oO0O )
 if 54 - 54: Ii
 if 57 - 57: iIII / o0O00o * ooOoO0O00 + IIiIiII11i . I11i
 if IiiiiII1Ii1 == 1 :
  for iIII1 in IiIio0oO0O :
   iIII1 = iIII1 . replace ( 'player' , 'watch' )
   ii1iI111IIi1 = iIII1 + '&fv=&sou='
   Oo00 = i11oO0oOo0 ( ii1iI111IIi1 )
   IiiiiiiiI1i11 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( Oo00 )
   for oOoooooOoO in IiiiiiiiI1i11 :
    I11iI1i11IiI = False
    Resolve ( oOoooooOoO )
    if 10 - 10: o0o00Oo0O + o0o00Oo0O % o0o00Oo0O % ooOoO0O00 + iIII . Ii1I
 elif IiiiiII1Ii1 > 1 :
  if 31 - 31: iI11I1II1I1I . IIIi11I1 * oOOoOooOo . IIIIiiII111 - o0o00Oo0O . iI11I1II1I1I
  for iIII1 in IiIio0oO0O :
   OoO00 = i11oO0oOo0 ( iIII1 )
   OOOoOOo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OoO00 )
   oOOo0oOoooO0o = OOOoOOo
   oOOo0oOoooO0o = ( str ( oOOo0oOoooO0o ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + oOOo0oOoooO0o
   O0O00OOo ( 'DOUBLE LINK' , oOOo0oOoooO0o , 424 , '' )
   if 24 - 24: o0o00Oo0O / oO0o - I1ii11iIi11i - IIiIiII11i + ii + oOo0O0Ooo
   for url in OOOoOOo :
    iI ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     i11I1 = Google . resolve ( url )
    except :
     pass
    try :
     oooOO = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( i11I1 ) )
     for OO0oO0O , OO0oo00OO00oO in oooOO :
      if 51 - 51: ii * o0o00Oo0O - oO0o . I1ii11iIi11i % IIiIiII11i + o0O00o
      HD_URLS . append ( OO0oO0O )
      SD_URLS . append ( OO0oo00OO00oO )
    except :
     pass
 else :
  pass
  if 48 - 48: o0O00o . IIiIiII11i - Ii * IIIIiiII111
def Ooo0O00 ( ) :
 if 1 - 1: oO0o % IIIi11I1 - IIIIiiII111 * iI11I1II1I1I
 if 14 - 14: OOooOOo
 iI ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiiiiIIii + 'Movies.png' )
 if 17 - 17: I1ii11iIi11i . ii % Ii1I / ii
 iI ( 'Search Movies' , '' , 7017 , iiiiiIIii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 56 - 56: OOooOOo - o0O00o
 if 53 - 53: Ii1I - IIiIiII11i . Ii
def ooO000Oo0 ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://cnfstudio.com/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , 'http://cnfstudio.com/genre/' + Oo0o00OO0000 , 7003 , iiiiiIIii + 'icon.png' )
  if 78 - 78: o0O0Oooo0O * o0O0Oooo0O
O0OoO000O0OO = xbmcgui . Dialog ( )
if 17 - 17: o0O0Oooo0O - o0O0Oooo0O . ooOO0O0ooOooO / o0O0Oooo0O
iIIiiI1iiI11i = '{UN},' ; Ii11iIiI1i1i = '{IG},' ; iIIiiI1I = '{PL},' ; oOOoooO00o0o0 = '{LO},' ; oO000Oo0OoO = '{LP},' ; OOO0OoOOo = '{HA},' ; iIi1I = '{XD},' ; oOooO = '{TA},' ; IiiiiIII = '{DP},' ; Oo0O0 = '{JT},' ; IiIiiiii1i1I1I = '{JJ},' ; Ii11I = '{MM},' ; OooOo0 = '{FQ},' ; i1iiiiI1iIi = '{HH},'
if 3 - 3: I1ii11iIi11i - IIIi11I1 * oO0o - IIiIiII11i . ii
def iII11iIII ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( O0o0O0 )
 ooOoIIi11iiI1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iII11 )
 ooOoIIi11iiI1 = ooOoIIi11iiI1
 for url in ooOoIIi11iiI1 :
  iI ( 'Next Page' , url , 7003 , iiiiiIIii + 'Next.png' )
  if 5 - 5: ooOoO0O00 - OOooOOo - ooOO0O0ooOooO + Ii
def oOoo0O0o ( url ) :
 if 50 - 50: oOOoOooOo + iIII / ooOO0O0ooOooO - o0O00o
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  I1I1IiI1 = url + '&fv=&sou='
  I1I1IiI1 = I1I1IiI1 . replace ( 'player' , 'watch' )
  i11ii1II1Ii = i1I1ii1iI1 ( I1I1IiI1 )
  OOOOooO0Oo0oo = i1I1ii1iI1 ( url )
  if 71 - 71: oO0o - o0o00Oo0O
  if 73 - 73: iI11I1II1I1I
def i1I1ii1iI1 ( url ) :
 if 7 - 7: OOooOOo
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  II1i1i1I1iII ( url )
  if 55 - 55: ooOO0O0ooOooO . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
  if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
def iII1II1ii1 ( ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Local M3u[/COLOR]' , OooO0 , 2001 , iiiiiIIii + 'LocalM3U.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Remote M3u[/COLOR]' , ooOoOoo0O , 7080 , iiiiiIIii + 'RemoteM3U.png' , iIi1ii1I1 , '' )
 if 21 - 21: IIIi11I1 + I11i
def II1oo0OO0OoO ( ) :
 if os . path . exists ( OooO0 ) :
  i111i = open ( OooO0 , 'r' )
  for IIi1IIIi in i111i :
   i111I1I = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IIi1IIIi )
   for iiIiii1IIIII , Oo0o00OO0000 in i111I1I :
    O0O00OOo ( iiIiii1IIIII , Oo0o00OO0000 , 222 , iiiiiIIii + 'streams.png' )
 else :
  O0OoO000O0OO . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 100 - 100: oOOoOooOo + o0O0Oooo0O
def Ii1I1iIiIi ( url ) :
 if os . path . exists ( Remote ) :
  oO0000OOo00 = iii1 ( url )
  Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iiIiii1IIIII , url in Ii1i1iI1iIIi :
   url = ( url ) . strip ( )
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  O0OoO000O0OO . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 82 - 82: IIIIiiII111 % oO0o . Ii . oO0o
  if 13 - 13: I11i / iI11I1II1I1I + o0o00Oo0O % oO0o
def I11iiI1i1 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 Ii1i1iI1iIIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 in Ii1i1iI1iIIi :
  Oo0o00OO0000 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + Oo0o00OO0000
 iiIiii1IIIII = 'plugin.video.GenieTv'
 if 13 - 13: OOooOOo + ooOoO0O00 - oOo0O0Ooo
 ii11iIi1I1i ( Oo0o00OO0000 , iiIiii1IIIII )
 if 79 - 79: Ii1I + o0O00o
def iioOooOOOoOo ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 Ii1i1iI1iIIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 in Ii1i1iI1iIIi :
  Oo0o00OO0000 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + Oo0o00OO0000
 iiIiii1IIIII = 'repository.GenieTv'
 if 94 - 94: Ii % oOOoOooOo * OOooOOo % I1ii11iIi11i * o0O00o
 ii11iIi1I1i ( Oo0o00OO0000 , iiIiii1IIIII )
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . IIIi11I1
 if 95 - 95: ooOoO0O00 . iIII + o0o00Oo0O . iIII - iIII / I1ii11iIi11i
def IiO00Oooo0o000 ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']CATAGORIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SEARCH[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  OoOo0Oo0 ( )
 if OoOOo0OOoO == 1 :
  ii1i1II1 ( )
  if 64 - 64: o0O00o + IIiIiII11i - o0O00o * Ii1I * Ii
  if 99 - 99: iIII / o0O00o . ooOO0O0ooOooO . o0o00Oo0O % ooOoO0O00 - Ii
  if 66 - 66: iI11I1II1I1I . I1ii11iIi11i / Ii1i1i + IIIi11I1 - o0o00Oo0O % o0O00o
  if 22 - 22: ooOO0O0ooOooO - Ii % o0o00Oo0O / IIiIiII11i
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
O0OoO000O0OO = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
i1I11i = 'https://addons.tvaddons.ag/'
if 64 - 64: I11i
def ii1i1II1 ( ) :
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 iI11IIi1iiI1I = 'https://addons.tvaddons.ag/search/?keyword=' + i11ii
 oO0000OOo00 = i11oO0oOo0 ( iI11IIi1iiI1I )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiI , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , 10054 , 'https://addons.tvaddons.ag/' + iiIiI , iIi1ii1I1 , '' )
  if 22 - 22: I11i / ii
  if 63 - 63: o0O0Oooo0O
def OoOo0Oo0 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i1I11i )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Repositories' in iiIiii1IIIII :
   pass
  elif 'Services' in iiIiii1IIIII :
   pass
  elif 'International' in iiIiii1IIIII :
   pass
  else :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 10053 , 'https://addons.tvaddons.ag/' + iII11 , iIi1ii1I1 , '' )
   if 52 - 52: iI11I1II1I1I / IIIIiiII111
   if 46 - 46: o0O0Oooo0O . Ii
def Addon ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 i1ii1II1ii = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0000OOo00 )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Please' in iiIiii1IIIII :
   pass
  else :
   oOOOoo0O0oO ( iiIiii1IIIII , url , 10054 , 'https://addons.tvaddons.ag/' + iII11 , iIi1ii1I1 , '' )
 for url in i1ii1II1ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
  if 89 - 89: oO0o - IIIi11I1 - ooOoO0O00 - oO0o % iI11I1II1I1I
  if 52 - 52: I11i * o0o00Oo0O + Ii1I
def o0OOoo ( url , name ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   IIIIiIiIi1 = os . path . join ( I1iI , name + '.zip' )
   try :
    os . remove ( IIIIiIiIi1 )
   except :
    pass
   downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
   I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print I11iiiiI1i
   print '======================================='
   extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
   OoOOoooOO0O ( )
   if 87 - 87: oOo0O0Ooo * ooOoO0O00 * I1ii11iIi11i / Ii1I - oO0o
def ii11iIi1I1i ( url , name ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IIIIiIiIi1 = os . path . join ( I1iI , name + '.zip' )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 I11iiiiI1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11iiiiI1i
 print '======================================='
 extract . all ( IIIIiIiIi1 , I11iiiiI1i , o0oOoO00o )
 OoOOoooOO0O ( )
 if 44 - 44: I1ii11iIi11i
def OoOOoooOO0O ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 37 - 37: IIIi11I1 / Ii1i1i
 if 51 - 51: IIIi11I1 + o0o00Oo0O
def Oo0OoO ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iiIiI , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , url , 1007 , iiIiI )
def O00oo0o ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iiIiI , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 1006 , iiIiI )
  if 76 - 76: ooOO0O0ooOooO - o0o00Oo0O / I1ii11iIi11i
def o0OooIi1III1 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , ii1i , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiiiI1iIi ( iiIiii1IIIII , 100109 , Oo0o00OO0000 , image = ii1i , isFolder = True )
  if 85 - 85: ooOoO0O00 % IIIIiiII111 * Ii1i1i * OOooOOo
def OoOooO0 ( url ) :
 import random
 iIIIiiii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 iIIIiiii . clear ( )
 O0OiI1i1iIii1 = [ ]
 o0O0 = [ ]
 oO00O = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for i11I1 , ii1i , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0OiI1i1iIii1 . append ( [ i11I1 , iiIiii1IIIII ] )
  if len ( O0OiI1i1iIii1 ) == len ( Ii1i1iI1iIIi ) :
   for IIi1IIIi in O0OiI1i1iIii1 :
    o00OO0000 = random . randint ( 1 , len ( O0OiI1i1iIii1 ) )
    try :
     OOO0O0OO = O0OiI1i1iIii1 [ int ( o00OO0000 ) ]
    except :
     pass
    if len ( o0O0 ) <= 20 :
     if OOO0O0OO [ 1 ] not in oO00O :
      iiIi1IIiIi = i11oO0oOo0 ( OOO0O0OO [ 0 ] )
      I1i1iii1Ii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iiIi1IIiIi )
      for I1I1 , oOoooo0OooO in I1i1iii1Ii :
       i1iIIIi1i = i11oO0oOo0 ( I1I1 )
       o0oO0OO00ooOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i1iIIIi1i )
       for O0OO0 , I1I1IiI1 in o0oO0OO00ooOO :
        if 'panda' in I1I1IiI1 :
         III1iiIIi = i11oO0oOo0 ( I1I1IiI1 )
         IiIIiii11II1 = re . compile ( "url: '(.+?)'" ) . findall ( III1iiIIi )
         for OOOOo0o0O0 in IiIIiii11II1 :
          if 'http' in OOOOo0o0O0 :
           Oo0oO = xbmcgui . ListItem ( OOO0O0OO [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : OOO0O0OO [ 1 ] } )
           Oo0oO . setProperty ( "IsPlayable" , "true" )
           iIIIiiii . add ( OOOOo0o0O0 , Oo0oO )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0oO )
           if 30 - 30: I1ii11iIi11i % ii * Ii % ooOO0O0ooOooO
def iiiiiiI1iIi ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = o0
 o0OO0O0OO0oO0 = sys . argv [ 0 ]
 o0OO0O0OO0oO0 += '?mode=' + str ( mode )
 o0OO0O0OO0oO0 += '&title=' + urllib . quote_plus ( name )
 o0OO0O0OO0oO0 += '&image=' + urllib . quote_plus ( image )
 o0OO0O0OO0oO0 += '&page=' + str ( page )
 if url != '' :
  o0OO0O0OO0oO0 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  o0OO0O0OO0oO0 += '&keyword=' + urllib . quote_plus ( keyword )
 Oo0oO = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  Oo0oO . addContextMenuItems ( contextMenu )
 if infoLabels :
  Oo0oO . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  Oo0oO . setProperty ( "IsPlayable" , "true" )
 Oo0oO . setProperty ( 'Fanart_Image' , iIi1ii1I1 )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = isFolder )
 if 37 - 37: IIIIiiII111
 if 29 - 29: IIIi11I1
def i1ii11 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iconimage , i11II1I11I1 , ooo0O0o00O , name in Ii1i1iI1iIIi :
  if 'http' in url :
   if '.php' in url :
    O0o0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
    for IIi1IIIi in O0o0O :
     if IIi1IIIi == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    O0O0oOo0o0o0 ( name , url , 1016 , iconimage , ooo0O0o00O , i11II1I11I1 )
   else :
    if 'youtube' in url :
     O0o0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
     for IIi1IIIi in O0o0O :
      if IIi1IIIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iI11IiiI1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , ooo0O0o00O , i11II1I11I1 )
    else :
     O0o0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
     for IIi1IIIi in O0o0O :
      if IIi1IIIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iI11IiiI1 ( name , url , 222 , iconimage , ooo0O0o00O , i11II1I11I1 )
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
  else :
   oO0o0O0oOoo ( url , iconimage , name )
   if 70 - 70: o0o00Oo0O / OOooOOo . ooOO0O0ooOooO
 else :
  Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
  for url , iiIiI , name in Ii1i1iI1iIIi :
   if 'http' in url :
    if '.php' in url :
     iI ( name , url , 1016 , iiIiI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      O0O00OOo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiI )
     else :
      O0o0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
      for IIi1IIIi in O0o0O :
       if IIi1IIIi == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      O0O00OOo ( name , url , 222 , iiIiI )
      OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
   else :
    oO0o0O0oOoo ( url , iiIiI , name )
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 12 - 12: iIII / o0o00Oo0O . o0O0Oooo0O % Ii + oO0o . Ii1I
def oO0o0O0oOoo ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 O0O00ooO0O0O = ( url ) . replace ( O0o0OO0oOo0OO , 'http' ) . replace ( o0oOOOO00O0 , '.com' ) ;
 Iiii1II = ( O0O00ooO0O0O ) . replace ( I1i11I11 , 'a' ) . replace ( i111Ii1iI1 , 'b' ) . replace ( O0o000O0Oo0 , 'c' ) . replace ( Ii1Oo0O , 'd' ) . replace ( iIIiiI1I , 'e' ) . replace ( Oo0O0 , 'f' ) ;
 Ooo0o0OoOO = ( Iiii1II ) . replace ( oOO0 , 'g' ) . replace ( OOO0OoOOo , 'h' ) . replace ( iIiI1iIi1 , 'i' ) . replace ( OOO0o0ooO0 , 'j' ) . replace ( o0O0oooOoOO0O , 'k' ) . replace ( ii111iIii1 , 'l' ) ;
 IIi11 = ( Ooo0o0OoOO ) . replace ( oo0OoOoo00oO , 'm' ) . replace ( oo0OO0oo000O00oo , 'n' ) . replace ( ooOOi1IiI1i1iI1Ii , 'o' ) . replace ( O00OiIIII1iiIII , 'p' ) . replace ( OO0oOii11iIIi1i , 'q' ) . replace ( oOOooO00oOo00 , 'r' ) ;
 iIII1II1iI = ( IIi11 ) . replace ( oOOOOoO00o0oo , 's' ) . replace ( OOOo0O00oO00 , 't' ) . replace ( i1i1iIiI , 'u' ) . replace ( oO000ooO , 'v' ) . replace ( OoOiIIiI , 'w' ) . replace ( IIi111i1i1III , 'x' ) ;
 O00oOo = ( iIII1II1iI ) . replace ( Ii1Ii1ii , 'y' ) . replace ( oO0OOoooooo0o , 'z' ) . replace ( iIIiiI1iiI11i , '.' ) . replace ( Ii11iIiI1i1i , '(' ) . replace ( oOOoooO00o0o0 , ')' ) . replace ( oO000Oo0OoO , '/' ) ;
 o0ooO0OO = ( O00oOo ) . replace ( O0O0O , '1' ) . replace ( IIiIIIi1I , '2' ) . replace ( I1IiI1i1Iii , '3' ) . replace ( oOooO , '4' ) . replace ( IiiiiIII , '5' ) . replace ( oOOo0OO0oo , '6' ) ;
 i1i1III11i1111i = ( o0ooO0OO ) . replace ( IiIiiiii1i1I1I , '7' ) . replace ( Ii11I , '8' ) . replace ( OooOo0 , '9' ) . replace ( i1iiiiI1iIi , '0' ) . replace ( o0o0Oo0O0O0o , ':' ) . replace ( o0OO0o00O00 , '%' ) ;
 url = ( i1i1III11i1111i ) . replace ( o0OO0O , '-' ) . replace ( iIi1I , '_' ) ;
 O0O00OOo ( name , url , 222 , iconimage ) ;
 if 95 - 95: oO0o + OOooOOo % I1ii11iIi11i . Ii1i1i * oOo0O0Ooo + o0O0Oooo0O
 if 22 - 22: I1ii11iIi11i . oO0o
def OO0o0ooo0o0 ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiI , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , Oo0o00OO0000 , 1007 , iiIiI )
def IiIIIIii1IIiIIi1I1I ( url ) :
 if 22 - 22: ooOoO0O00 / oO0o * oOo0O0Ooo - I1ii11iIi11i - Ii1i1i
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iiIiI , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 1006 , iiIiI )
  if 80 - 80: oOOoOooOo . Ii
def i1iIi11 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iiIIIiIi1IIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iiIIIiIi1IIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIi1IIi )
 if 76 - 76: oO0o % OOooOOo * oOOoOooOo . oOo0O0Ooo
 if 64 - 64: oOOoOooOo % Ii1I . oO0o . oOOoOooOo + Ii . iI11I1II1I1I
def oO00Oo0O0 ( url ) :
 O0o0O0 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '-dir-' in iiIiii1IIIII :
   iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iII11 )
  else :
   iI ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 1006 , iII11 )
   if 70 - 70: oOOoOooOo
def iiI1iIi1 ( url ) :
 O0o0O0 = iii1 ( url )
 oO00 = ( 'http://afewbitsmore.com/' )
 Ii1i1iI1iIIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '[To Parent Directory]' in iiIiii1IIIII :
   iiIiii1IIIII = 'HOME'
   pass
  elif 'HOME' in iiIiii1IIIII :
   pass
  elif '.m3u' in iiIiii1IIIII :
   iI ( '[COLOR' + II11iiii1Ii + ']PLAY ALL[/COLOR]' , oO00 + url , 2002 , iiiiiIIii + 'music.png' )
  elif '.mp3' in iiIiii1IIIII :
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , oO00 + url , 222 , iiiiiIIii + 'music.png' )
  elif '.m4a' in iiIiii1IIIII :
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , oO00 + url , 222 , iiiiiIIii + 'music.png' )
  else :
   iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) , oO00 + url , 1012 , iiiiiIIii + 'music.png' )
def IiiIIi1IiI ( url ) :
 oO0000OOo00 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiiiiIIii + 'music.png' )
  if 27 - 27: I1ii11iIi11i * IIIi11I1 / o0o00Oo0O . I1ii11iIi11i
def iIi1i1111I ( url ) :
 O0o0O0 = iii1 ( url )
 oO00 = url
 Ii1i1iI1iIIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '.mp3' in iiIiii1IIIII :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiiiiIIii + 'music.png' )
  else :
   iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '/' , '' ) , oO00 + url , 1011 , iiiiiIIii + 'music.png' )
def oOo0oOo0 ( ) :
 O0o0O0 = iii1 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , ( 'http://www.cyn.net/music/' + Oo0o00OO0000 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iII11 ) . replace ( ' ' , '%20' ) )
def iIiII1iiiI11 ( url , img ) :
 O0o0O0 = iii1 ( url )
 i11I1 = url
 img = img
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( i11I1 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 77 - 77: IIiIiII11i % Ii1i1i . IIiIiII11i . oOOoOooOo . IIIi11I1
def iIi11I1II ( url ) :
 O0o0O0 = iii1 ( url )
 i11I1 = url
 Ii1i1iI1iIIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 for type , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '[VID]' in type :
   O0O00OOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , i11I1 + url , 222 , iiiiiIIii + 'music.png' )
  if '[DIR]' in type :
   iIi11I1II ( i11I1 + url )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 40 - 40: ooOO0O0ooOooO
 if 6 - 6: IIIIiiII111 . Ii1i1i / ooOO0O0ooOooO / oOo0O0Ooo
def o0O00O ( ) :
 oO0o000OooOoo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oOO0ooIiIIi1I1I11Ii = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11ii = oOO0ooIiIIi1I1I11Ii . lower ( )
 Oo0o00OO0000 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 OOoooO00o0o = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 i11I1 = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 8 - 8: oOo0O0Ooo * oOo0O0Ooo . Ii1I - IIIIiiII111 . o0O0Oooo0O
 oO0000OOo00 = O0 ( Oo0o00OO0000 )
 iI1iiIi1 = O0 ( OOoooO00o0o )
 iiIi1IIiIi = O0 ( i11I1 )
 if 71 - 71: IIIIiiII111 / oOOoOooOo * ooOoO0O00
 if oO0000OOo00 != 'Failed' :
  Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , ii1i , i11II1I11I1 , Oo00OO0 , iiIiii1IIIII in Ii1i1iI1iIIi :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , Oo0o00OO0000 , 1016 , ii1i , ooo0O0o00O , i11II1I11I1 )
    if 79 - 79: Ii1I - oOo0O0Ooo * o0O0Oooo0O + IIIi11I1 - o0o00Oo0O
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iI1iiIi1 != 'Failed' :
  I1iiIIIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iI1iiIi1 )
  for Oo0o00OO0000 , iiIiii1IIIII in I1iiIIIi11 :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + Oo0o00OO0000 ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'Music.png' )
    if 37 - 37: I1ii11iIi11i + iI11I1II1I1I * iIII / IIiIiII11i . OOooOOo
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( iiIi1IIiIi )
  for Oo0o00OO0000 , iiIiii1IIIII in I1Ii :
   if oOO0ooIiIIi1I1I11Ii in iiIiii1IIIII . lower ( ) :
    iI ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + Oo0o00OO0000 ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'Music.png' )
    if 77 - 77: ooOO0O0ooOooO + iIII . IIiIiII11i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 3 - 3: o0O00o / I11i
    if 71 - 71: o0O00o / o0O0Oooo0O + Ii . IIIi11I1
    if 16 - 16: iI11I1II1I1I + oOo0O0Ooo - IIIi11I1 + IIIi11I1 . iI11I1II1I1I + o0O0Oooo0O
    if 96 - 96: ooOoO0O00 * iI11I1II1I1I . IIIi11I1 + o0o00Oo0O . I11i
    if 23 - 23: Ii1I . Ii1I / oOo0O0Ooo . ooOoO0O00
    if 47 - 47: Ii . I11i . Ii + oOo0O0Ooo - Ii1I
oo0OoOoo00oO = '{SF},' ; oo0OO0oo000O00oo = '{IF},' ; ooOOi1IiI1i1iI1Ii = '{PW},' ; I1IiI1i1Iii = '{AM},' ; O00OiIIII1iiIII = '{GF},' ; OO0oOii11iIIi1i = '{DD},' ; oOOooO00oOo00 = '{UO},' ; oOOOOoO00o0oo = '{LE},' ; i1i1iIiI = '{ZY},' ; oO000ooO = '{UE},' ; OoOiIIiI = '{PE},' ; IIi111i1i1III = '{JE},' ; Ii1Ii1ii = '{TH},' ; oO0OOoooooo0o = '{LK},'
if 62 - 62: ii + oOo0O0Ooo / oOOoOooOo . Ii1i1i . I1ii11iIi11i
if 81 - 81: ooOO0O0ooOooO + o0O00o
def Oo0 ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://www.iwatchseries.me/tv-list/' )
 Ii1i1iI1iIIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , Oo0o00OO0000 , 8021 , iiiiiIIii + 'iwatch.png' )
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
def ooOOOO ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , o00OOoOOO000O0 in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII + o00OOoOOO000O0 , url , 8022 , iiiiiIIii + 'iwatch.png' )
def II1iI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  Oo0o0 ( url )
def Oo0o0 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( O0o0O0 )
 I1i1iii1Ii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( O0o0O0 )
 o0oO0OO00ooOO = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( 'VidSpot - ' + iiIiii1IIIII , url , 222 , iiiiiIIii + 'iwatch.png' )
 for url in I1Ii :
  O0O00OOo ( 'VodLocker' , url , 222 , iiiiiIIii + 'iwatch.png' )
 for url , iiIiii1IIIII in o0oO0OO00ooOO :
  O0O00OOo ( 'VidUp' + iiIiii1IIIII , url , 222 , iiiiiIIii + 'iwatch.png' )
 for iiIiii1IIIII , url in I1i1iii1Ii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   O0O00OOo ( 'TheVideo - ' + iiIiii1IIIII , url , 222 , iiiiiIIii + 'iwatch.png' )
   if 55 - 55: o0o00Oo0O
def IiioOoo ( ) :
 O0o0O0 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 Ii1i1iI1iIIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , Oo0o00OO0000 , 1021 , iiiiiIIii + 'anime.png' )
  if 15 - 15: I11i
  if 55 - 55: Ii / ii - iIII
def O0Oo0oO0 ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://www.animetoon.org/cartoon' )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , Oo0o00OO0000 , 1002 , iiiiiIIii + 'anime.png' )
  if 9 - 9: ooOoO0O00 + Ii + Ii1I % OOooOOo / Ii + Ii
  if 13 - 13: Ii1i1i % oOOoOooOo
  if 92 - 92: IIiIiII11i + Ii1i1i + Ii1i1i
def OoOOoII1iiIIiII1 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O0o0O0 )
 for iII11 in I1Ii :
  OoooooO0oOOoO = iII11
 I1i1iii1Ii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( O0o0O0 )
 for url in I1i1iii1Ii :
  iI ( 'NEXT PAGE' , url , 1002 , iiiiiIIii + 'Next.png' )
 Ii1i1iI1iIIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iI ( iiIiii1IIIII , url , 1003 , OoooooO0oOOoO )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO0o0O ( url , IMAGE ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  print iiIiii1IIIII + '     ' + url
  if 'easy' in url :
   iIIiI11 ( url )
  elif 'playpanda' in url :
   iIIiI11 ( url )
   if 45 - 45: I1ii11iIi11i . ooOoO0O00
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIIiI11 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "url: '(.+?)'," ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0O00OOo ( 'STREAM' , url , 222 , iiiiiIIii + 'anime.png' )
  if 10 - 10: OOooOOo * oOOoOooOo / iI11I1II1I1I . IIIi11I1
  if 93 - 93: I1ii11iIi11i / IIiIiII11i . I1ii11iIi11i + ooOoO0O00 + ooOoO0O00
def IIO0Oo ( url ) :
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 ii1ii1ii . add_header ( 'referer' , url )
 oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
 I1I1IiI1 = oooooOoo0ooo . read ( )
 oooooOoo0ooo . close ( )
 return I1I1IiI1
 if 23 - 23: iIII * o0O0Oooo0O / Ii / IIiIiII11i
def iii1 ( url ) :
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
 I1I1IiI1 = oooooOoo0ooo . read ( )
 oooooOoo0ooo . close ( )
 return I1I1IiI1
 if 32 - 32: Ii1I - o0O0Oooo0O * Ii1I / Ii1i1i
def iIIIIi11 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1III = ( '%s%s' % ( oO00O0OO , url ) )
 I1I1IiI1 = iii1 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1I1IiI1 )
 for url , iiIiI , iiIiii1IIIII in Ii1i1iI1iIIi :
  O0O00OOo ( '%s' % ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiIiI )
  if 58 - 58: Ii1i1i * iIII
def oOoooo0o0 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  OOiIiIII1 ( url , iiIiii1IIIII )
 else :
  O0i1iI ( url )
def O0i1iI ( url ) :
 import urlresolver
 try :
  iiI1iii = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( iiI1iii , xbmcgui . ListItem ( iiIiii1IIIII ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iiIiii1IIIII ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def II1i1i1I1iII ( url ) :
 if 41 - 41: IIIIiiII111
 ii111 = open ( Oo0oOOo , "a" )
 ii111 . write ( 'url="' + url + '"\n' )
 ii111 . close
 if 34 - 34: Ii1i1i - IIIi11I1 % IIIIiiII111
 I1iIII1IiiI = xbmc . Player ( OOoooOoO0Oo ( ) )
 import urlresolver
 try : I1iIII1IiiI . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iiIiii1IIIII ) )
 I1iIII1IiiI = xbmc . Player ( OOoooOoO0Oo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  O0OoO000O0OO = xbmcgui . Dialog ( )
  if O0OoO000O0OO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   O0OoO000O0OO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I1iIII1IiiI . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def OOiIiIII1 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  Iii1I = '.mp4'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.mkv' in url :
  Iii1I = '.mkv'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.mp3' in url :
  Iii1I = '.mp3'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.avi' in url :
  Iii1I = '.avi'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.mov' in url :
  Iii1I = '.mov'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.mpeg' in url :
  Iii1I = '.mpeg'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.mpg' in url :
  Iii1I = '.mpg'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.flv' in url :
  Iii1I = '.flv'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 elif '.wmv' in url :
  Iii1I = '.wmv'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iIii1iii1 ( url , name , Iii1I )
 else :
  O0i1iI ( url )
def iIii1iii1 ( url , name , cat ) :
 O0OOo0 ( )
 I1iI = xbmc . translatePath ( os . path . join ( OO0o ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 IIIIiIiIi1 = os . path . join ( I1iI , file )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def O0OOo0 ( ) :
 I1iI = xbmc . translatePath ( os . path . join ( OO0o ) )
 if not os . path . exists ( OO0o ) :
  O0OoO000O0OO . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def oO000Oo ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iiIiii1IIIII )
 xbmc . sleep ( 1 )
 I1iIII1IiiI = xbmc . Player ( OOoooOoO0Oo ( ) )
 o0oOoO00o . update ( 100 , '%s' % iiIiii1IIIII )
 xbmc . sleep ( 1 )
 I1iIII1IiiI . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 100 - 100: Ii1I . oOOoOooOo
def O0o0oo0oOO0oO ( url ) :
 I1iIII1IiiI = xbmc . Player ( OOoooOoO0Oo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1iIII1IiiI . play ( url ) . strip ( )
 except : pass
 if 37 - 37: iIII % iI11I1II1I1I % Ii1I
def oOo0o00O0oO0 ( url ) :
 I1iIII1IiiI = xbmc . Player ( OOoooOoO0Oo ( ) )
 import urlresolver
 o0OOiiI11Ii1iI = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 I1iIII1IiiI . play ( o0OOiiI11Ii1iI )
 xbmc . sleep ( 1 )
 I1iIII1IiiI . play ( url )
 if 53 - 53: IIIIiiII111 . oOo0O0Ooo
 if 61 - 61: OOooOOo
def OOoooOoO0Oo ( ) :
 try :
  iIii1OOO0 = getSet ( "core-player" )
  if ( iIii1OOO0 == 'DVDPLAYER' ) : i1Ii1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIii1OOO0 == 'MPLAYER' ) : i1Ii1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIii1OOO0 == 'PAPLAYER' ) : i1Ii1 = xbmc . PLAYER_CORE_PAPLAYER
  else : i1Ii1 = xbmc . PLAYER_CORE_AUTO
 except : i1Ii1 = xbmc . PLAYER_CORE_AUTO
 return i1Ii1
 return True
 if 78 - 78: IIIIiiII111 . ooOO0O0ooOooO . oOo0O0Ooo % o0o00Oo0O * oOOoOooOo % o0O0Oooo0O
def iI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oo0oooo0OoO0o = [ ]
  oo0oooo0OoO0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oo0oooo0OoO0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   oo0oooo0OoO0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0oO . addContextMenuItems ( oo0oooo0OoO0o )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = True )
 return iIiiIi11IIi
 if 26 - 26: ii + IIIIiiII111 * oOOoOooOo
def iIiiII ( name , url , mode , iconimage , fanart , description ) :
 if 71 - 71: IIIi11I1 . Ii1I + IIiIiII11i
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = True )
 return iIiiIi11IIi
 if 26 - 26: Ii1I % o0o00Oo0O / Ii1i1i + Ii - Ii1i1i
def O0O00OOo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oo0oooo0OoO0o = [ ]
  oo0oooo0OoO0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oo0oooo0OoO0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   oo0oooo0OoO0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0oO . addContextMenuItems ( oo0oooo0OoO0o )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = False )
 return iIiiIi11IIi
 if 48 - 48: oOo0O0Ooo - Ii * Ii1I
 if 70 - 70: Ii1I * OOooOOo
 if 63 - 63: oOOoOooOo . o0O00o - OOooOOo % o0O00o - o0O0Oooo0O / o0O0Oooo0O
 if 42 - 42: ooOoO0O00 . OOooOOo * OOooOOo * OOooOOo
 if 14 - 14: IIiIiII11i / o0O0Oooo0O . oOo0O0Ooo
 if 66 - 66: o0O0Oooo0O % ooOO0O0ooOooO . IIIIiiII111 * ooOoO0O00
def oooo0oOOooo0 ( url , heading , announce ) :
 class I1iI1ii1II ( ) :
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
   try : OOo0O0oo0OO0O = open ( announce ) ; i111I1 = OOo0O0oo0OO0O . read ( )
   except : i111I1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i111I1 ) )
   return
 I1iI1ii1II ( )
 I1iI1ii1II ( )
def Ii1I1Ii ( heading , announce ) :
 class I1iI1ii1II ( ) :
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
   try : OOo0O0oo0OO0O = open ( announce ) ; i111I1 = OOo0O0oo0OO0O . read ( )
   except : i111I1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i111I1 ) )
   return
 I1iI1ii1II ( )
 I1iI1ii1II ( )
def I1i ( ) :
 oooo0oOOooo0 ( iiiiiIIii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 88 - 88: IIIi11I1 % ii
 if 28 - 28: Ii % oO0o - o0O00o + IIIi11I1 . I11i
 if 66 - 66: IIiIiII11i + Ii1I - OOooOOo . I11i / o0O00o % OOooOOo
 if 32 - 32: IIIIiiII111 . IIIi11I1 * I11i - I1ii11iIi11i % o0o00Oo0O
 if 91 - 91: ii . ooOO0O0ooOooO + Ii1I / Ii * oOOoOooOo
def OoOOoooOO0O ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 25 - 25: Ii1I + oO0o * ii
 if 17 - 17: I1ii11iIi11i / o0o00Oo0O - o0o00Oo0O
 if 83 - 83: IIIi11I1 / Ii1i1i * oOo0O0Ooo % ooOO0O0ooOooO / iI11I1II1I1I
 if 1 - 1: iIII / ii / IIIIiiII111
 if 68 - 68: ooOoO0O00 / I1ii11iIi11i / iIII * I1ii11iIi11i
 if 91 - 91: oO0o . IIIIiiII111
 if 82 - 82: Ii1I / I1ii11iIi11i
 if 63 - 63: oOo0O0Ooo
 if 3 - 3: IIIIiiII111 + Ii1I
 if 35 - 35: ooOO0O0ooOooO * IIIIiiII111 * ooOO0O0ooOooO * o0O0Oooo0O * o0O00o * ooOoO0O00
 if 43 - 43: oO0o * oOo0O0Ooo / o0O00o . Ii + IIIIiiII111 + I11i
 if 1 - 1: oOo0O0Ooo % I11i . o0O0Oooo0O + iIII * ooOO0O0ooOooO
 if 41 - 41: oO0o * ooOO0O0ooOooO - IIiIiII11i
 if 2 - 2: o0O00o + o0O00o - oO0o * IIIIiiII111 . ooOO0O0ooOooO
 if 91 - 91: oOOoOooOo
 if 22 - 22: oOOoOooOo % oO0o * OOooOOo + I1ii11iIi11i
 if 44 - 44: o0o00Oo0O - iIII
 if 43 - 43: o0o00Oo0O
 if 50 - 50: iIII - ii
 if 29 - 29: ooOO0O0ooOooO * ooOO0O0ooOooO
 if 44 - 44: oOOoOooOo . oOo0O0Ooo * ooOO0O0ooOooO * Ii1i1i
 if 41 - 41: ooOoO0O00 % Ii + iIII % ii / Ii1I
 if 8 - 8: ii - oO0o / Ii / o0o00Oo0O . o0O00o
 if 86 - 86: oOOoOooOo * ii + IIIIiiII111 + I11i
def OoOO0OOoOoO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + IioOo0Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 86 - 86: o0O00o
def o0oooo00 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + iIiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 75 - 75: I11i / ii % oO0o / OOooOOo + IIIIiiII111
def ooOoi11I1Ii ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + I1I1iI1Iiiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 51 - 51: IIIIiiII111 - OOooOOo + IIiIiII11i
def ooOOOo0o0OO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + iiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 21 - 21: Ii1I . ooOO0O0ooOooO % o0O00o . Ii1i1i % I1ii11iIi11i
def IiiiOOo000oO0 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + Oo0oo00o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 59 - 59: oO0o + IIIi11I1 . Ii1I - IIIIiiII111 % oOOoOooOo
def iI1I1Ii1IIiI ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + OoOOOO0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 2 - 2: oO0o . Ii1I * Ii
def o00oo0O00o ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + OO0ooo0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 31 - 31: ooOoO0O00 * Ii1I
def iIiiiiiIii ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + O00ii111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 32 - 32: oOo0O0Ooo + oOOoOooOo / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
def o0O00 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + ooOoOOIii11i111iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1i , ooo0O0o00O , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 76 - 76: o0O0Oooo0O - o0o00Oo0O
def OOO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + Ii11111iiIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1i , ooo0O0o00O , iII1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , iiiiiIIii + 'GenieTVRSSFeed.png' , iiiiiIIii + 'GenieTVRSSFeed.png' , iII1 )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 18 - 18: ooOO0O0ooOooO . OOooOOo + oOOoOooOo * IIIIiiII111 * iI11I1II1I1I % o0o00Oo0O
 if 32 - 32: o0o00Oo0O / iIII . o0o00Oo0O
 if 25 - 25: I1ii11iIi11i - IIIIiiII111
 if 96 - 96: o0o00Oo0O . oOo0O0Ooo
 if 2 - 2: iIII . ooOO0O0ooOooO * o0O00o
 if 41 - 41: Ii1i1i / oO0o / oO0o * iIII
 if 31 - 31: Ii1i1i / ii % iI11I1II1I1I - o0O00o * oOo0O0Ooo - o0o00Oo0O
 if 31 - 31: ooOO0O0ooOooO
 if 74 - 74: oO0o
def II1ii1 ( ) :
 try :
  if os . path . exists ( IIiiiiiiIi1I1 ) == True :
   O0OoO000O0OO = xbmcgui . Dialog ( )
   if O0OoO000O0OO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( IIiiiiiiIi1I1 ) :
     OoOo0Oo0o0O = 0
     OoOo0Oo0o0O += len ( ooOo0 )
     if OoOo0Oo0o0O > 0 :
      for OOo0O0oo0OO0O in ooOo0 :
       os . unlink ( os . path . join ( i11O00oO , OOo0O0oo0OO0O ) )
  o0OOoOOO000 = os . path . join ( IIIII , "Textures13.db" )
  os . unlink ( o0OOoOOO000 )
  O0OoO000O0OO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 2 - 2: Ii1i1i . o0O0Oooo0O - OOooOOo - Ii1i1i
 if 56 - 56: ii % oOOoOooOo . IIIi11I1
 if 92 - 92: OOooOOo + iI11I1II1I1I
 if 81 - 81: iI11I1II1I1I * IIiIiII11i + iIII / Ii
 if 68 - 68: ooOO0O0ooOooO * iI11I1II1I1I % I11i - Ii
 if 39 - 39: Ii1i1i . IIIIiiII111
 if 27 - 27: oOo0O0Ooo + OOooOOo + IIIIiiII111
 if 70 - 70: iIII + o0O00o . oOOoOooOo - Ii1I
def o0Oooo ( title , message , times = 2000 , icon = o0 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 34 - 34: ooOoO0O00 % I1ii11iIi11i . ooOO0O0ooOooO
def III1 ( url ) :
 I1I1I1 = os . path . join ( oooOOOOO , 'addon_data' )
 I11IiI1iII = [
 ( I1I1I1 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( I1I1I1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1I1I1 , 'plugin.video.itv' , 'Images' ) ) ]
 if 45 - 45: IIIi11I1 + ooOO0O0ooOooO * o0o00Oo0O % oOOoOooOo + iI11I1II1I1I + o0O0Oooo0O
 oo0iIIII11Iiii11 = 0
 if 86 - 86: Ii1i1i % Ii1I % Ii1I * oOo0O0Ooo
 for IIi1IIIi in I11IiI1iII :
  if os . path . exists ( IIi1IIIi ) and not IIi1IIIi in [ oo0o0O00 , I1I1I1 ] :
   for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( IIi1IIIi ) :
    OoOo0Oo0o0O = 0
    OoOo0Oo0o0O += len ( ooOo0 )
    if OoOo0Oo0o0O > 0 :
     for OOo0O0oo0OO0O in ooOo0 :
      if not OOo0O0oo0OO0O in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( i11O00oO , OOo0O0oo0OO0O ) )
       except :
        pass
      else : Oo0o0O00 ( 'Ignore Log File: %s' % OOo0O0oo0OO0O )
     for oOO0oOooo in Ii1iII1ii1 :
      try :
       shutil . rmtree ( os . path . join ( i11O00oO , oOO0oOooo ) )
       oo0iIIII11Iiii11 += 1
       Oo0o0O00 ( "[Success] cleared %s files from %s" % ( str ( OoOo0Oo0o0O ) , os . path . join ( IIi1IIIi , oOO0oOooo ) ) )
      except :
       Oo0o0O00 ( "[Failed] to wipe cache in: %s" % os . path . join ( IIi1IIIi , oOO0oOooo ) )
  else :
   for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( IIi1IIIi ) :
    for oOO0oOooo in Ii1iII1ii1 :
     if 'cache' in oOO0oOooo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( i11O00oO , oOO0oOooo ) )
       oo0iIIII11Iiii11 += 1
       Oo0o0O00 ( "[Success] wiped %s " % os . path . join ( IIi1IIIi , oOO0oOooo ) )
      except :
       Oo0o0O00 ( "[Failed] to wipe cache in: %s" % os . path . join ( IIi1IIIi , oOO0oOooo ) )
       if 59 - 59: IIIIiiII111 / oOOoOooOo % oO0o / Ii1I - o0O00o
 o0Oooo ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % oo0iIIII11Iiii11 )
 if 96 - 96: o0o00Oo0O / iIII - iI11I1II1I1I
 if 74 - 74: IIiIiII11i % I11i - IIIIiiII111
 if 53 - 53: oOo0O0Ooo * iI11I1II1I1I % I1ii11iIi11i * IIIi11I1 - IIIi11I1
 if 88 - 88: o0O0Oooo0O
 if 72 - 72: iI11I1II1I1I % ooOoO0O00 / oO0o / oOo0O0Ooo - IIiIiII11i - o0O0Oooo0O
 if 43 - 43: I11i - I1ii11iIi11i - Ii1I / IIiIiII11i + oOo0O0Ooo / Ii1I
 if 34 - 34: I1ii11iIi11i
def II1iIOOOo0oO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 o0Ooo0oOOooO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( o0Ooo0oOOooO ) :
   OoOo0Oo0o0O = 0
   OoOo0Oo0o0O += len ( ooOo0 )
   if 36 - 36: Ii1i1i % oO0o
   if 89 - 89: Ii1I + iIII / Ii * oOOoOooOo
   if OoOo0Oo0o0O > 0 :
    if 36 - 36: IIIIiiII111 / ii + Ii1i1i . oOo0O0Ooo
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( OoOo0Oo0o0O ) + " files found" , "Do you want to delete them?" ) :
     if 48 - 48: IIiIiII11i / IIiIiII11i . iIII - oOo0O0Ooo
     for OOo0O0oo0OO0O in ooOo0 :
      os . unlink ( os . path . join ( i11O00oO , OOo0O0oo0OO0O ) )
     for oOO0oOooo in Ii1iII1ii1 :
      shutil . rmtree ( os . path . join ( i11O00oO , oOO0oOooo ) )
     O0OoO000O0OO = xbmcgui . Dialog ( )
     O0OoO000O0OO . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    O0OoO000O0OO = xbmcgui . Dialog ( )
    O0OoO000O0OO . ok ( i1 , "       No Packages to DELETE" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 OOOOoOOOo0oOO ( )
 return
 if 67 - 67: Ii1I + Ii1I
 if 52 - 52: Ii - o0o00Oo0O
 if 64 - 64: Ii . o0O0Oooo0O / o0o00Oo0O - o0O00o
 if 88 - 88: Ii1i1i / oO0o - iIII
 if 11 - 11: oO0o / ooOoO0O00 . ii
 if 40 - 40: o0O00o + IIIIiiII111 * iIII + OOooOOo
 if 5 - 5: o0O0Oooo0O / o0O00o
 if 30 - 30: IIIi11I1 . IIIIiiII111 % oO0o + ooOO0O0ooOooO
 if 69 - 69: Ii + o0O00o * oOOoOooOo * IIIIiiII111 % ooOO0O0ooOooO
def iI1i11 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 o0Ooo0oOOooO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( o0Ooo0oOOooO ) :
   OoOo0Oo0o0O = 0
   OoOo0Oo0o0O += len ( ooOo0 )
   if 66 - 66: IIIi11I1 * o0O00o + o0o00Oo0O - ii
   if 19 - 19: I1ii11iIi11i * OOooOOo
   if OoOo0Oo0o0O > 0 :
    if 52 - 52: oO0o + ooOO0O0ooOooO
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( OoOo0Oo0o0O ) + " files found" , "Do you want to delete them?" ) :
     if 84 - 84: o0o00Oo0O % Ii1I % iI11I1II1I1I - OOooOOo - I1ii11iIi11i
     for OOo0O0oo0OO0O in ooOo0 :
      os . unlink ( os . path . join ( i11O00oO , OOo0O0oo0OO0O ) )
     for oOO0oOooo in Ii1iII1ii1 :
      shutil . rmtree ( os . path . join ( i11O00oO , oOO0oOooo ) )
     O0OoO000O0OO = xbmcgui . Dialog ( )
     O0OoO000O0OO . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    O0OoO000O0OO = xbmcgui . Dialog ( )
    O0OoO000O0OO . ok ( i1 , "       No Packages to DELETE" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 III1 ( url )
 return
 if 7 - 7: IIiIiII11i % ooOO0O0ooOooO % ooOoO0O00 . iI11I1II1I1I
 if 92 - 92: Ii1i1i / I11i % IIIi11I1 - OOooOOo
 if 44 - 44: oOo0O0Ooo + OOooOOo * I1ii11iIi11i
 if 31 - 31: iIII - oOo0O0Ooo - oO0o * OOooOOo
 if 50 - 50: Ii1I + iIII * IIIIiiII111
 if 27 - 27: OOooOOo * IIIi11I1 * iI11I1II1I1I / ooOoO0O00
 if 60 - 60: IIIi11I1 * o0O0Oooo0O . ooOO0O0ooOooO
 if 47 - 47: ooOO0O0ooOooO % IIIi11I1 / IIIi11I1 % OOooOOo % o0O0Oooo0O / OOooOOo
 if 51 - 51: oOo0O0Ooo . iIII - OOooOOo
 if 10 - 10: I1ii11iIi11i * IIIi11I1 / o0O00o . I11i
def o0OOO0OOOOo0O0 ( url , name ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooo0 = os . path . join ( I1iI , 'advancedsettings.xml' )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 OoOo00O = os . path . join ( I1iI , 'advancedsettings.xml.bak' )
 if os . path . exists ( OoOo00O ) == False :
  if O0OoO000O0OO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   ooo0 = os . path . join ( I1iI , 'advancedsettings.xml' )
   try :
    os . remove ( ooo0 )
    print '=== GenieTv - REMOVING    ' + str ( ooo0 ) + '    ==='
   except :
    pass
   I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
   oOoO00o = open ( ooo0 , "w" )
   oOoO00o . write ( I1I1IiI1 )
   oOoO00o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( ooo0 ) + '    ==='
   O0OoO000O0OO = xbmcgui . Dialog ( )
   O0OoO000O0OO . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  ooo0 = os . path . join ( I1iI , 'advancedsettings.xml' )
  try :
   os . remove ( ooo0 )
   print '=== GenieTv - REMOVING    ' + str ( ooo0 ) + '    ==='
  except :
   pass
  I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
  oOoO00o = open ( ooo0 , "w" )
  oOoO00o . write ( I1I1IiI1 )
  oOoO00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooo0 ) + '    ==='
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 72 - 72: IIIi11I1 * OOooOOo
def OoO0 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooo0 = os . path . join ( I1iI , 'advancedsettings.xml' )
 try :
  oOoO00o = open ( ooo0 ) . read ( )
  if 'zero' in oOoO00o :
   name = '0CACHE'
  elif 'tuxen' in oOoO00o :
   name = 'TUXENS'
  elif 'muckys' in oOoO00o :
   name = 'MUCKYS'
  elif 'p2p1' in oOoO00o :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oOoO00o :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oOoO00o :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 58 - 58: ooOoO0O00 - I1ii11iIi11i * Ii % ii + iI11I1II1I1I % o0o00Oo0O
def Iii11I1ii ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooo0 = os . path . join ( I1iI , 'advancedsettings.xml' )
 try :
  os . remove ( ooo0 )
  O0OoO000O0OO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( ooo0 ) + '    ==='
  O0OoO000O0OO . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 55 - 55: I11i / o0o00Oo0O / ii * I1ii11iIi11i % IIIIiiII111
 if 24 - 24: Ii1I % IIIi11I1 + ii + oO0o
 if 100 - 100: I1ii11iIi11i % oO0o - OOooOOo
 if 46 - 46: I11i
 if 28 - 28: ooOoO0O00
 if 81 - 81: ooOO0O0ooOooO % ii . o0O0Oooo0O - OOooOOo / oOo0O0Ooo
 if 62 - 62: o0O0Oooo0O * iIII / iIII
 if 42 - 42: oOOoOooOo * oOOoOooOo / Ii1i1i / IIIi11I1 * IIIi11I1
 if 92 - 92: I1ii11iIi11i / IIIIiiII111 - ii - I11i % oOOoOooOo
 if 35 - 35: ooOoO0O00 % IIIIiiII111 % iIII * iI11I1II1I1I % Ii1i1i - I1ii11iIi11i
def o000ooOooO0 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Ii1i1iI1iIIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( oOOoO0 . http_GET ( url ) . content )
 for I1ii1i11iI1 , O0ooOo00 , iIIiI1i1i , I11Ii1i1 in Ii1i1iI1iIIi :
  if inc < 2 : O0OoO000O0OO = xbmcgui . Dialog ( ) ; O0OoO000O0OO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % I1ii1i11iI1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iIIiI1i1i , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I11Ii1i1 )
  inc = inc + 1
  if 69 - 69: ooOoO0O00
  if 83 - 83: Ii1I . oOOoOooOo + oOo0O0Ooo + o0o00Oo0O
  if 78 - 78: o0o00Oo0O + I1ii11iIi11i
  if 14 - 14: o0o00Oo0O
  if 67 - 67: IIiIiII11i / o0o00Oo0O
  if 10 - 10: ooOoO0O00 / I1ii11iIi11i
  if 20 - 20: I1ii11iIi11i * o0O0Oooo0O / Ii1I . oOOoOooOo
  if 67 - 67: I11i . I1ii11iIi11i % iIII
  if 38 - 38: IIIi11I1 - oO0o . oOOoOooOo
def i1IiiI1i ( url , name ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 if O0OoO000O0OO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  I1iI = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ooo0 = os . path . join ( I1iI , 'addons2.ini' )
  I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
  oOoO00o = open ( ooo0 , "w" )
  oOoO00o . write ( I1I1IiI1 )
  oOoO00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooo0 ) + '    ==='
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 23 - 23: IIIIiiII111 . Ii1i1i - oO0o / Ii1I / o0o00Oo0O
def Ii1I11I111 ( url , name ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 if O0OoO000O0OO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  I1iI = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ooo0 = os . path . join ( I1iI , 'settings.xml' )
  I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
  oOoO00o = open ( ooo0 , "w" )
  oOoO00o . write ( I1I1IiI1 )
  oOoO00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooo0 ) + '    ==='
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 65 - 65: IIIIiiII111 . oOOoOooOo
 if 71 - 71: iI11I1II1I1I % o0O00o . o0o00Oo0O - I1ii11iIi11i
def OoooooO ( ) :
 try :
  o00iI11 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( o00iI11 ) == True :
   O0OoO000O0OO = xbmcgui . Dialog ( )
   if O0OoO000O0OO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Ooo00o = os . path . join ( o00iI11 , "source.db" )
    os . unlink ( Ooo00o )
  O0OoO000O0OO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 78 - 78: I11i / IIIi11I1 / ooOO0O0ooOooO
 if 9 - 9: o0O00o + o0o00Oo0O / oOo0O0Ooo
 if 92 - 92: IIIi11I1 / Ii + ii
 if 9 - 9: IIIIiiII111
 if 9 - 9: o0o00Oo0O / I11i / iIII - Ii - IIIIiiII111 / o0O00o
def i11oO0oOo0 ( url ) :
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
 I1I1IiI1 = oooooOoo0ooo . read ( )
 oooooOoo0ooo . close ( )
 return I1I1IiI1
 if 46 - 46: o0O00o + ii % oOo0O0Ooo
 if 51 - 51: oOo0O0Ooo * o0O0Oooo0O . Ii % I1ii11iIi11i . ooOoO0O00 - ooOO0O0ooOooO
 if 56 - 56: I1ii11iIi11i / IIiIiII11i
 if 76 - 76: OOooOOo % oO0o * o0o00Oo0O
 if 39 - 39: oOOoOooOo / IIIIiiII111
 if 94 - 94: ooOO0O0ooOooO + IIIIiiII111 * OOooOOo - ooOoO0O00 / ii
 if 59 - 59: iIII % Ii1i1i / OOooOOo
def i1iI11i1IIi ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; O0ooOo = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O0ooOo :
  I11I1I1 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; I11I1I1 = xbmc . translatePath ( I11I1I1 ) ;
  oOOO00Oo = os . path . join ( I11I1I1 , ".." , ".." ) ; oOOO00Oo = os . path . abspath ( oOOO00Oo ) ; pluginlog ( "freshstart.main_list xbmcPath=" + oOOO00Oo ) ; iIiIi1III1iII = False
  try :
   for i11O00oO , Ii1iII1ii1 , ooOo0 in os . walk ( oOOO00Oo , topdown = True ) :
    Ii1iII1ii1 [ : ] = [ oOO0oOooo for oOO0oOooo in Ii1iII1ii1 if oOO0oOooo not in o0oO0 ]
    for iiIiii1IIIII in ooOo0 :
     try : os . remove ( os . path . join ( i11O00oO , iiIiii1IIIII ) )
     except :
      if iiIiii1IIIII not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iIiIi1III1iII = True
      pluginlog ( "Error removing " + i11O00oO + " " + iiIiii1IIIII )
    for iiIiii1IIIII in Ii1iII1ii1 :
     try : os . rmdir ( os . path . join ( i11O00oO , iiIiii1IIIII ) )
     except :
      if iiIiii1IIIII not in [ "Database" , "userdata" ] : iIiIi1III1iII = True
      pluginlog ( "Error removing " + i11O00oO + " " + iiIiii1IIIII )
   if not iIiIi1III1iII : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 I11OoooO ( )
 if 30 - 30: IIIi11I1 * Ii1I % ooOO0O0ooOooO
 if 26 - 26: oOo0O0Ooo - IIIIiiII111 + Ii1I + o0O0Oooo0O - oOOoOooOo
 if 72 - 72: iI11I1II1I1I / I11i + Ii
def oOOO0oO ( ) :
 oOo0oo000oOOo0 = [ ]
 Iiii11iiI = sys . argv [ 2 ]
 if len ( Iiii11iiI ) >= 2 :
  ii1IIi111 = sys . argv [ 2 ]
  o00000 = ii1IIi111 . replace ( '?' , '' )
  if ( ii1IIi111 [ len ( ii1IIi111 ) - 1 ] == '/' ) :
   ii1IIi111 = ii1IIi111 [ 0 : len ( ii1IIi111 ) - 2 ]
  Ii1II = o00000 . split ( '&' )
  oOo0oo000oOOo0 = { }
  for O0oo in range ( len ( Ii1II ) ) :
   iI1IiIi1 = { }
   iI1IiIi1 = Ii1II [ O0oo ] . split ( '=' )
   if ( len ( iI1IiIi1 ) ) == 2 :
    oOo0oo000oOOo0 [ iI1IiIi1 [ 0 ] ] = iI1IiIi1 [ 1 ]
    if 5 - 5: IIiIiII11i * IIIIiiII111 - I11i + oOo0O0Ooo % iI11I1II1I1I
 return oOo0oo000oOOo0
 if 97 - 97: I11i % ii . oOo0O0Ooo + iI11I1II1I1I
oO00O0O00OOOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
oo000O0o = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I1o0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
o0oooO0o00 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1I1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
O00OOOOO0Oo0o = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
IioOo0Ooo0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
O0o0OOOo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
iIiII = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
I1I1iI1Iiiii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iiiI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Oo0oo00o00 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
OoOOOO0O00 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OO0ooo0OO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
O00ii111I = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
ooOoOOIii11i111iI = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OO00OO0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iIIIiiiIi1i = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOoo000o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ooo0oo00O00Oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iIIIIIi11Ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
Ii11i1I1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Ii11111iiIi11 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oO00O0OO = base64 . decodestring ( 'Q1VOVA==' )
def IIi1Ii1iiI ( display , mode = None , name = None , url = None , menu = None , description = i1iiIIiiI111 , overwrite = True , fanart = iIi1ii1I1 , icon = o0 , themeit = None ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ]
 if not mode == None : o0OO0O0OO0oO0 += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : o0OO0O0OO0oO0 += "&name=" + urllib . quote_plus ( name )
 if not url == None : o0OO0O0OO0oO0 += "&url=" + urllib . quote_plus ( url )
 iIiiIi11IIi = True
 if themeit : display = themeit % display
 Oo0oO = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : Oo0oO . addContextMenuItems ( menu , replaceItems = overwrite )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = False )
 return iIiiIi11IIi
def ooooOoOooo00Oo ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 Oo0oO . setProperty ( 'fanart_image' , fanart )
 Oo0oO . setProperty ( "IsPlayable" , "true" )
 I1ii11II1Ii1i1 = [ ]
 I1ii11II1Ii1i1 . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 I1ii11II1Ii1i1 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 Oo0oO . addContextMenuItems ( I1ii11II1Ii1i1 , replaceItems = True )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = False )
 return iIiiIi11IIi
def OoOOoOooooOOo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oo0oooo0OoO0o = [ ]
  if showcontext == 'fav' :
   oo0oooo0OoO0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   oo0oooo0OoO0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Oo0oO . addContextMenuItems ( oo0oooo0OoO0o )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = True )
 return iIiiIi11IIi
 if 6 - 6: IIiIiII11i % o0O0Oooo0O - Ii / oOOoOooOo
def oOOOoo0O0oO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0OO0O0OO0oO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiIi11IIi = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oo0oooo0OoO0o = [ ]
  if showcontext == 'fav' :
   oo0oooo0OoO0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   oo0oooo0OoO0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Oo0oO . addContextMenuItems ( oo0oooo0OoO0o )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0O0OO0oO0 , listitem = Oo0oO , isFolder = False )
 return iIiiIi11IIi
 if 51 - 51: IIIi11I1 * I11i / ooOO0O0ooOooO
 if 43 - 43: oOo0O0Ooo * ii * OOooOOo . IIIi11I1 / oOo0O0Ooo
ii1IIi111 = oOOO0oO ( )
Oo0o00OO0000 = None
iiIiii1IIIII = None
oOo0 = None
ii1i = None
ooo0O0o00O = None
iII1 = None
O0ooooo000 = None
OoooOO0 = None
if 49 - 49: ooOO0O0ooOooO
if 36 - 36: IIIIiiII111 . iIII . ooOoO0O00 + iIII
try :
 OoooOO0 = int ( ii1IIi111 [ "fav_mode" ] )
except :
 pass
 if 97 - 97: IIiIiII11i . ii - OOooOOo
try :
 Oo0o00OO0000 = urllib . unquote_plus ( ii1IIi111 [ "url" ] )
except :
 pass
try :
 iiIiii1IIIII = urllib . unquote_plus ( ii1IIi111 [ "name" ] )
except :
 pass
try :
 ii1i = urllib . unquote_plus ( ii1IIi111 [ "iconimage" ] )
except :
 pass
try :
 oOo0 = int ( ii1IIi111 [ "mode" ] )
except :
 pass
try :
 ooo0O0o00O = urllib . unquote_plus ( ii1IIi111 [ "fanart" ] )
except :
 pass
try :
 iII1 = urllib . unquote_plus ( ii1IIi111 [ "description" ] )
except :
 pass
 if 35 - 35: o0O0Oooo0O
 if 35 - 35: I1ii11iIi11i - iI11I1II1I1I / ooOoO0O00 + oO0o - ii / Ii
print str ( I1IIIii ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( oOo0 )
print "URL: " + str ( Oo0o00OO0000 )
print "Name: " + str ( iiIiii1IIIII )
print "IconImage: " + str ( ii1i )
if 79 - 79: oOo0O0Ooo * oOOoOooOo * oOOoOooOo
if 92 - 92: IIIIiiII111 % Ii1I
def OOoOO0o0o0 ( content , viewType ) :
 if 16 - 16: ooOO0O0ooOooO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 52 - 52: ii % oOOoOooOo - o0O0Oooo0O * iIII
if ii1i == None : ii1i = o0
if ooo0O0o00O == None : ooo0O0o00O = iIi1ii1I1
if oOo0 == None :
 O0oO ( )
 if 24 - 24: Ii1i1i + o0O00o + ii / ooOO0O0ooOooO / oOo0O0Ooo + o0O00o
elif oOo0 == 1 :
 o00oO00 ( Oo0o00OO0000 )
 if 52 - 52: oOOoOooOo
elif oOo0 == 44 :
 iI1 ( Oo0o00OO0000 )
 if 38 - 38: oO0o + oOo0O0Ooo % o0O00o
elif oOo0 == 2 :
 i11iI1111ii1I ( )
 if 87 - 87: ooOO0O0ooOooO * Ii1i1i - o0O0Oooo0O / ooOO0O0ooOooO
elif oOo0 == 3 :
 I11iiI11I1II ( )
 if 65 - 65: OOooOOo
elif oOo0 == 21 :
 i1i1II ( )
 if 87 - 87: iIII - Ii - IIIi11I1 . OOooOOo + o0O00o . oO0o
elif oOo0 == 4 :
 iio0Oo ( )
 if 70 - 70: iI11I1II1I1I % ii / oO0o . o0o00Oo0O - iIII % IIiIiII11i
elif oOo0 == 5 :
 O0O0o0o0oo0O ( Oo0o00OO0000 )
 if 84 - 84: IIIi11I1 * ooOoO0O00 . iI11I1II1I1I * IIIIiiII111 + o0O0Oooo0O + IIiIiII11i
elif oOo0 == 6 :
 II1iIOOOo0oO ( Oo0o00OO0000 )
 if 97 - 97: Ii1i1i - o0O00o
elif oOo0 == 7 :
 o0OOO0OOOOo0O0 ( Oo0o00OO0000 , iiIiii1IIIII )
 if 64 - 64: ooOO0O0ooOooO . oOOoOooOo / oOOoOooOo - IIiIiII11i
elif oOo0 == 8 :
 OoO0 ( Oo0o00OO0000 , iiIiii1IIIII )
 if 81 - 81: Ii1I
elif oOo0 == 9 :
 FIXREPOSADDONS ( Oo0o00OO0000 )
 if 64 - 64: ooOO0O0ooOooO * oO0o / IIIi11I1 + Ii1i1i % I1ii11iIi11i . o0O00o
elif oOo0 == 10 :
 OoOOoooOO0O ( )
 if 2 - 2: o0O0Oooo0O + iIII
elif oOo0 == 11 :
 Iii11I1ii ( Oo0o00OO0000 )
 if 47 - 47: Ii + iI11I1II1I1I % Ii1I - ooOO0O0ooOooO % oO0o
elif oOo0 == 12 :
 o000ooOooO0 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 85 - 85: ooOO0O0ooOooO * OOooOOo / OOooOOo
elif oOo0 == 13 :
 II1ii1 ( )
 if 85 - 85: IIIi11I1 / o0O0Oooo0O . ooOoO0O00 / OOooOOo + iI11I1II1I1I
elif oOo0 == 14 :
 III1 ( Oo0o00OO0000 )
 if 71 - 71: oO0o
elif oOo0 == 15 :
 i1II1i1iiI1 ( )
 if 96 - 96: Ii1I / oOo0O0Ooo - Ii1I / IIiIiII11i - o0O00o
elif oOo0 == 16 :
 i1IiiI1i ( Oo0o00OO0000 , iiIiii1IIIII )
 if 74 - 74: Ii1i1i * ii % IIIi11I1 + ii + IIIIiiII111
elif oOo0 == 17 :
 Ii1I11I111 ( Oo0o00OO0000 , iiIiii1IIIII )
 if 83 - 83: ooOoO0O00
elif oOo0 == 18 :
 OoooooO ( )
 if 2 - 2: ooOoO0O00 / IIIi11I1 * o0o00Oo0O
elif oOo0 == 19 :
 iiIIIi1II1IiiI ( Oo0o00OO0000 )
 if 99 - 99: ii . OOooOOo / IIiIiII11i
elif oOo0 == 40 :
 i1OooO00oO00o ( iiIiii1IIIII , Oo0o00OO0000 , iII1 )
 if 64 - 64: IIIIiiII111 / ooOoO0O00 . oOo0O0Ooo + o0o00Oo0O
elif oOo0 == 42 :
 IIIII11II1 ( iiIiii1IIIII , Oo0o00OO0000 , iII1 )
 if 5 - 5: o0o00Oo0O . Ii
elif oOo0 == 43 :
 Ii1i1I1 ( Oo0o00OO0000 )
 if 71 - 71: I11i + IIIIiiII111 + oOOoOooOo
elif oOo0 == 20 :
 oooO0O0Oo00 ( Oo0o00OO0000 )
 if 27 - 27: ii . IIIIiiII111 * o0O0Oooo0O % o0o00Oo0O + ii - IIIIiiII111
elif oOo0 == 22 :
 OoOO0OOoOoO ( Oo0o00OO0000 )
 if 86 - 86: ooOoO0O00
elif oOo0 == 23 :
 o0oooo00 ( Oo0o00OO0000 )
 if 81 - 81: OOooOOo
elif oOo0 == 24 :
 ooOoi11I1Ii ( Oo0o00OO0000 )
 if 52 - 52: IIIIiiII111 * o0O00o % oOo0O0Ooo * iIII
elif oOo0 == 25 :
 ooOOOo0o0OO ( Oo0o00OO0000 )
 if 73 - 73: o0O0Oooo0O * oOOoOooOo
elif oOo0 == 26 :
 IiiiOOo000oO0 ( Oo0o00OO0000 )
 if 62 - 62: IIIi11I1 . oOo0O0Ooo * iI11I1II1I1I + oO0o * oOOoOooOo / ooOO0O0ooOooO
elif oOo0 == 27 :
 iI1I1Ii1IIiI ( Oo0o00OO0000 )
 if 14 - 14: IIIIiiII111 / oO0o
elif oOo0 == 28 :
 o00oo0O00o ( Oo0o00OO0000 )
 if 75 - 75: o0O00o
elif oOo0 == 29 :
 iIiiiiiIii ( Oo0o00OO0000 )
 if 68 - 68: o0O00o - ooOoO0O00 % o0O00o . oO0o . Ii . ii
elif oOo0 == 30 :
 IiiII ( Oo0o00OO0000 )
 if 32 - 32: IIIIiiII111 + oO0o % o0O00o + oOo0O0Ooo
elif oOo0 == 31 :
 o0O00 ( Oo0o00OO0000 )
 if 69 - 69: o0O0Oooo0O + iIII - iI11I1II1I1I - IIiIiII11i . Ii1i1i
elif oOo0 == 32 :
 i11I1Ii1Iiii1 ( )
 if 74 - 74: Ii1I % I11i + o0o00Oo0O - Ii - o0O00o % IIIi11I1
elif oOo0 == 33 :
 o0oooOoOoOo ( )
 if 39 - 39: oO0o - I11i
elif oOo0 == 35 :
 oo0ooOoo00Ooo ( Oo0o00OO0000 )
 if 71 - 71: IIIIiiII111 . oO0o + oOOoOooOo - IIIi11I1 - I1ii11iIi11i
elif oOo0 == 34 :
 OO0O ( Oo0o00OO0000 )
 if 100 - 100: ii - I11i + o0O0Oooo0O . ii % Ii
elif oOo0 == 36 :
 iIii1i1IIi ( Oo0o00OO0000 )
 if 64 - 64: o0O0Oooo0O % ii / ooOoO0O00 / oO0o
elif oOo0 == 37 :
 Oo0ooooO0o00 ( Oo0o00OO0000 )
 if 2 - 2: iIII % I11i . oO0o . oO0o
elif oOo0 == 38 :
 Iiii ( Oo0o00OO0000 )
 if 89 - 89: oOOoOooOo - ooOO0O0ooOooO + IIiIiII11i + oO0o - o0O00o
elif oOo0 == 41 :
 i1iI11i1IIi ( ii1IIi111 )
 if 27 - 27: o0O0Oooo0O - I11i + oO0o
elif oOo0 == 39 :
 OOO ( Oo0o00OO0000 )
 if 38 - 38: OOooOOo + oO0o . Ii + Ii1i1i % ooOoO0O00 % oOo0O0Ooo
elif oOo0 == 45 :
 TEXTS ( )
 if 93 - 93: Ii
elif oOo0 == 46 :
 I1i ( )
 if 63 - 63: iI11I1II1I1I - iI11I1II1I1I % I11i
elif oOo0 == 47 :
 GEVID ( )
 if 97 - 97: ooOoO0O00 % iIII % OOooOOo
elif oOo0 == 48 :
 OOo0o0o ( iiIiii1IIIII , Oo0o00OO0000 , iII1 )
 if 25 - 25: OOooOOo . iI11I1II1I1I - IIIIiiII111 % IIiIiII11i . OOooOOo
elif oOo0 == 49 :
 oOo00 ( )
 if 16 - 16: IIIi11I1 . I1ii11iIi11i . oOo0O0Ooo % o0o00Oo0O . Ii1I + Ii
elif oOo0 == 22222 :
 II1i1i1I1iII ( Oo0o00OO0000 )
 if 100 - 100: Ii1I - ooOoO0O00 - oO0o * I11i + OOooOOo
elif oOo0 == 222225 :
 OO0o0oO0O000o ( Oo0o00OO0000 )
 if 31 - 31: ooOoO0O00
elif oOo0 == 222 :
 oOoooo0o0 ( Oo0o00OO0000 )
 if 21 - 21: I11i / o0o00Oo0O % o0o00Oo0O . ii / oOo0O0Ooo
elif oOo0 == 2222222 :
 O0i1iI ( Oo0o00OO0000 )
 if 94 - 94: oOOoOooOo + oO0o / oOOoOooOo - oOOoOooOo + I1ii11iIi11i + I11i
elif oOo0 == 222222 :
 OOiIiIII1 ( Oo0o00OO0000 , iiIiii1IIIII )
 if 50 - 50: ooOO0O0ooOooO . I1ii11iIi11i
elif oOo0 == 333 :
 iIIIIi11 ( Oo0o00OO0000 )
 if 15 - 15: Ii1i1i
 if 64 - 64: ii
elif oOo0 == 1020 :
 IiioOoo ( )
 if 25 - 25: o0O00o
elif oOo0 == 1021 :
 ANIMEEP ( )
 if 29 - 29: OOooOOo % oOOoOooOo * ii
elif oOo0 == 1022 :
 ANIMEPLAY ( Oo0o00OO0000 )
 if 8 - 8: Ii - o0O0Oooo0O / o0O00o
elif oOo0 == 1001 :
 O0Oo0oO0 ( )
 if 17 - 17: Ii * oO0o . I11i . ii . OOooOOo - Ii1I
elif oOo0 == 1005 :
 OO0o0ooo0o0 ( )
 if 78 - 78: Ii1I - ii + o0o00Oo0O
elif oOo0 == 1007 :
 IiIIIIii1IIiIIi1I1I ( Oo0o00OO0000 )
 if 15 - 15: Ii1I / o0O00o % oOo0O0Ooo
elif oOo0 == 1010 :
 oO00Oo0O0 ( Oo0o00OO0000 )
 if 16 - 16: Ii1i1i
elif oOo0 == 1011 :
 iIi1i1111I ( Oo0o00OO0000 )
 if 26 - 26: I11i / iIII + OOooOOo / OOooOOo
elif oOo0 == 1012 :
 iiI1iIi1 ( Oo0o00OO0000 )
 if 31 - 31: o0O0Oooo0O
elif oOo0 == 1030 :
 oOo0oOo0 ( )
 if 84 - 84: Ii * IIIi11I1 . IIIIiiII111 - Ii1i1i * ooOoO0O00 - Ii1I
elif oOo0 == 1031 :
 iIiII1iiiI11 ( Oo0o00OO0000 , ii1i )
 if 1 - 1: IIiIiII11i
elif oOo0 == 1032 :
 iIi11I1II ( Oo0o00OO0000 )
 if 94 - 94: Ii1I * IIIIiiII111 % IIIIiiII111 % iIII - IIIIiiII111
elif oOo0 == 1006 :
 Parse . ParseURL ( Oo0o00OO0000 )
 if 38 - 38: o0O00o - oO0o % Ii1i1i - IIiIiII11i
elif oOo0 == 2030 :
 Parse . addonParseURL ( Oo0o00OO0000 )
 if 97 - 97: o0o00Oo0O . Ii1i1i
elif oOo0 == 2031 :
 Parse . apkParseURL ( Oo0o00OO0000 )
 if 52 - 52: o0O00o
elif oOo0 == 2032 :
 Parse . ParseBOSS ( Oo0o00OO0000 )
 if 86 - 86: o0O0Oooo0O / o0o00Oo0O + ii % ooOO0O0ooOooO
elif oOo0 == 1002 :
 OoOOoII1iiIIiII1 ( Oo0o00OO0000 )
 if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . iIII . Ii1i1i
elif oOo0 == 1003 :
 ooO0o0O ( Oo0o00OO0000 , ii1i )
 if 81 - 81: IIiIiII11i + OOooOOo % Ii / IIIIiiII111 . o0O0Oooo0O + IIiIiII11i
elif oOo0 == 1004 :
 iIIiI11 ( Oo0o00OO0000 )
 if 48 - 48: oOo0O0Ooo . Ii1I * OOooOOo % ooOoO0O00 / o0O0Oooo0O * IIiIiII11i
elif oOo0 == 1008 :
 ii1OoO00o ( )
 if 62 - 62: I11i * o0O0Oooo0O . iI11I1II1I1I / ooOoO0O00
elif oOo0 == 1009 :
 Ii1I1iIiIi ( Oo0o00OO0000 )
 if 75 - 75: ii / oOOoOooOo - IIIIiiII111 . ii . OOooOOo % ooOoO0O00
elif oOo0 == 2001 :
 II1oo0OO0OoO ( )
 if 7 - 7: OOooOOo . ooOoO0O00 * Ii % Ii
elif oOo0 == 2002 :
 IiiIIi1IiI ( Oo0o00OO0000 )
 if 54 - 54: oO0o / oOo0O0Ooo . I1ii11iIi11i
elif oOo0 == 1013 :
 Ooo0OOO0O00 ( )
elif oOo0 == 10111113 :
 I1iII1 ( Oo0o00OO0000 )
 if 39 - 39: oO0o . oOOoOooOo
elif oOo0 == 1014 :
 iiiII1I1 ( )
 if 41 - 41: I1ii11iIi11i * Ii1I - IIiIiII11i - IIiIiII11i
elif oOo0 == 1015 :
 oo0oii1IIi1Ii1II1 ( Oo0o00OO0000 )
 if 7 - 7: ooOO0O0ooOooO
elif oOo0 == 1016 :
 i1ii11 ( Oo0o00OO0000 , ii1i , iiIiii1IIIII )
 if 41 - 41: oOOoOooOo
elif oOo0 == 1017 :
 oOO0OO0OO ( )
 if 93 - 93: Ii1i1i + o0O0Oooo0O + Ii1i1i
elif oOo0 == 1018 :
 oOOoooO ( Oo0o00OO0000 )
 if 23 - 23: oOo0O0Ooo - ooOoO0O00 / oOOoOooOo
elif oOo0 == 1019 :
 OoOOo ( Oo0o00OO0000 )
elif oOo0 == 10190 :
 oOO0oo ( Oo0o00OO0000 )
 if 4 - 4: o0O00o . Ii1I + IIIIiiII111 % oOOoOooOo
elif oOo0 == 1023 :
 ooIii ( )
 if 28 - 28: o0O0Oooo0O
elif oOo0 == 1024 :
 Oo0OoO ( Oo0o00OO0000 )
 if 27 - 27: IIIIiiII111 * oOo0O0Ooo
elif oOo0 == 1025 :
 O00oo0o ( Oo0o00OO0000 )
 if 60 - 60: ooOoO0O00 / oOo0O0Ooo - Ii1I
elif oOo0 == 4001 :
 i11i1iiI1i ( )
 if 41 - 41: o0O0Oooo0O + oOOoOooOo / IIIi11I1 + iIII % I1ii11iIi11i
elif oOo0 == 4002 :
 Ooo0o0OOO ( )
 if 91 - 91: oOo0O0Ooo % Ii1I % ooOO0O0ooOooO / ooOoO0O00 * iI11I1II1I1I + iIII
elif oOo0 == 4003 :
 O0o0OOo0o0o ( )
 if 48 - 48: oOOoOooOo / Ii1I / oO0o / IIiIiII11i * OOooOOo
elif oOo0 == 4004 :
 oooo00o0o0o ( )
 if 73 - 73: iIII / oOo0O0Ooo - o0O00o - ooOoO0O00 * o0O00o - IIIi11I1
elif oOo0 == 4005 :
 OooOOOo0 ( )
 if 39 - 39: iIII . oOOoOooOo * IIiIiII11i
elif oOo0 == 4006 :
 OOo ( )
 if 21 - 21: Ii1i1i
elif oOo0 == 4007 :
 IiIi1II11i ( )
 if 92 - 92: oO0o * Ii1I + iI11I1II1I1I
elif oOo0 == 4008 :
 IiI1iII1II111 ( )
 if 88 - 88: iI11I1II1I1I + iI11I1II1I1I * Ii . Ii1I % ooOO0O0ooOooO
elif oOo0 == 40099 : Oooo ( )
elif oOo0 == 4009 : Ii11ii1 ( )
elif oOo0 == 4010 : I11iIi1i1I1i1 ( )
elif oOo0 == 3000 :
 iII1II1ii1 ( )
 if 94 - 94: oOo0O0Ooo / Ii1I / IIIi11I1
elif oOo0 == 3001 :
 iIiIIiII11i1 ( )
 if 45 - 45: IIiIiII11i
elif oOo0 == 3002 :
 i1IiioOOooo ( Oo0o00OO0000 )
 if 98 - 98: Ii + Ii1I * IIIi11I1 / OOooOOo
elif oOo0 == 3003 :
 IiI11IiIIi ( Oo0o00OO0000 )
 if 84 - 84: I11i
elif oOo0 == 3004 :
 I1I1IiIiIIi1I ( Oo0o00OO0000 )
 if 40 - 40: ii - ooOO0O0ooOooO / o0o00Oo0O * o0O0Oooo0O . o0o00Oo0O + Ii
elif oOo0 == 404 :
 i1iIi11 ( iiIiii1IIIII , Oo0o00OO0000 , ii1i )
 if 9 - 9: IIIi11I1 % o0o00Oo0O % o0o00Oo0O / Ii1I . IIiIiII11i / IIiIiII11i
elif oOo0 == 405 :
 oO000Oo ( Oo0o00OO0000 )
 if 78 - 78: iI11I1II1I1I - ooOoO0O00 . iIII . I11i
elif oOo0 == 7030 :
 iiiiii ( )
 if 66 - 66: IIIi11I1 * I1ii11iIi11i
elif oOo0 == 7021 :
 i1Io0ooo ( iiIiii1IIIII )
 if 58 - 58: IIIi11I1
elif oOo0 == 7022 :
 iiIIII11i1 ( iiIiii1IIIII )
 if 96 - 96: o0O00o % ii + o0o00Oo0O * IIiIiII11i / IIIi11I1 . o0O0Oooo0O
elif oOo0 == 7000 :
 oOOO0 ( iiIiii1IIIII , Oo0o00OO0000 , img )
 if 47 - 47: oO0o - I1ii11iIi11i * oO0o / ooOO0O0ooOooO
elif oOo0 == 7050 :
 Ii1iiII11ii1 ( Oo0o00OO0000 )
 if 13 - 13: oOOoOooOo
elif oOo0 == 7051 :
 IIi1II ( Oo0o00OO0000 )
 if 55 - 55: ooOoO0O00 . iIII . IIiIiII11i + o0o00Oo0O + oOOoOooOo - ooOoO0O00
elif oOo0 == 7052 :
 Oo0OOO0oo0o ( Oo0o00OO0000 )
 if 3 - 3: iI11I1II1I1I / ooOO0O0ooOooO
elif oOo0 == 7053 :
 II11 ( Oo0o00OO0000 )
 if 61 - 61: o0O0Oooo0O / o0o00Oo0O - IIIIiiII111
elif oOo0 == 7054 :
 CoolPlay ( Oo0o00OO0000 )
 if 44 - 44: ooOoO0O00
elif oOo0 == 7060 :
 II1i1i1111IIIii ( )
 if 23 - 23: Ii1I . ii / Ii1i1i + I11i
elif oOo0 == 7061 :
 oOOO ( Oo0o00OO0000 )
 if 89 - 89: OOooOOo + I1ii11iIi11i . OOooOOo - IIiIiII11i
elif oOo0 == 7063 :
 ii11IiiiIi1iI ( Oo0o00OO0000 )
 if 85 - 85: ii * ii / Ii1i1i - IIiIiII11i
elif oOo0 == 7062 :
 o0II1IIII11Ii1 ( Oo0o00OO0000 )
 if 69 - 69: IIIIiiII111 * iIII
elif oOo0 == 7064 :
 NATatozcat ( )
 if 43 - 43: I11i - o0O00o * Ii1i1i . Ii / IIiIiII11i
elif oOo0 == 7067 :
 iII11I1iIiI ( Oo0o00OO0000 )
 if 61 - 61: OOooOOo / oOo0O0Ooo . Ii1I % IIIi11I1
elif oOo0 == 7066 :
 NATatozA ( Oo0o00OO0000 )
 if 70 - 70: IIIi11I1 * OOooOOo / ooOO0O0ooOooO + I1ii11iIi11i / o0o00Oo0O
elif oOo0 == 7065 :
 IiIiI1111 ( Oo0o00OO0000 )
 if 16 - 16: I1ii11iIi11i / ii / o0O00o + I1ii11iIi11i * Ii
elif oOo0 == 7070 :
 IiiIIiII ( )
 if 15 - 15: I11i / Ii
elif oOo0 == 7071 :
 DIZIlist ( Oo0o00OO0000 )
 if 63 - 63: Ii1I - Ii1i1i + iIII
elif oOo0 == 7072 :
 DIZIpull ( Oo0o00OO0000 )
 if 98 - 98: IIIIiiII111 / o0O00o * oOo0O0Ooo / ooOO0O0ooOooO - iI11I1II1I1I
elif oOo0 == 7073 :
 WATCHDIZI ( Oo0o00OO0000 )
 if 72 - 72: o0o00Oo0O . IIIi11I1
elif oOo0 == 7002 :
 ooO000Oo0 ( )
 if 99 - 99: ooOoO0O00 + iI11I1II1I1I - oOOoOooOo + oO0o + I1ii11iIi11i . Ii1I
elif oOo0 == 7003 :
 iII11iIII ( Oo0o00OO0000 )
 if 74 - 74: ooOoO0O00
elif oOo0 == 7004 :
 oOoo0O0o ( Oo0o00OO0000 )
 if 80 - 80: oOOoOooOo + o0O0Oooo0O . Ii1I % ii
elif oOo0 == 7020 :
 i1I1ii1iI1 ( Oo0o00OO0000 )
 if 26 - 26: OOooOOo . IIIIiiII111 * iI11I1II1I1I / o0O00o
elif oOo0 == 7001 :
 o00O0O ( )
 if 69 - 69: ii / iIII + Ii1i1i * IIiIiII11i
elif oOo0 == 7010 :
 IIiIII ( Oo0o00OO0000 )
 if 35 - 35: Ii + ooOO0O0ooOooO
elif oOo0 == 7011 :
 iiiIIII1Ii1 ( Oo0o00OO0000 )
 if 85 - 85: OOooOOo . o0o00Oo0O % ii % ooOO0O0ooOooO
elif oOo0 == 7012 :
 O0OO0OO0oo ( Oo0o00OO0000 )
 if 43 - 43: oOo0O0Ooo - iIII . oOo0O0Ooo / Ii % o0O00o * Ii
elif oOo0 == 7013 :
 cnfTVPlay2 ( Oo0o00OO0000 )
elif oOo0 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( Oo0o00OO0000 )
elif oOo0 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( Oo0o00OO0000 )
elif oOo0 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiIiii1IIIII , Oo0o00OO0000 , ii1i )
elif oOo0 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oOo0 == 7018 :
 Ooo0O00 ( )
elif oOo0 == 7019 :
 CNF_Studio_Indexer . List_Movies ( Oo0o00OO0000 )
elif oOo0 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( Oo0o00OO0000 )
elif oOo0 == 7024 :
 CNF_Studio_Indexer . Box_Office ( Oo0o00OO0000 )
 if 12 - 12: IIiIiII11i - iI11I1II1I1I
elif oOo0 == 8000 :
 I11Ooo0oOoOoOoo ( )
elif oOo0 == 8001 :
 Oo0ooOoo ( )
elif oOo0 == 8002 :
 iIi1Ii ( )
elif oOo0 == 8003 :
 O0o0OooOO ( )
elif oOo0 == 8004 :
 oo0O0O ( )
elif oOo0 == 8005 :
 o0oOOo0oO0o ( )
elif oOo0 == 8006 :
 iIIiii ( iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 8030 :
 IiIOOOoo ( Oo0o00OO0000 )
elif oOo0 == 8045 :
 IIiI11I1II1 ( Oo0o00OO0000 )
elif oOo0 == 8046 :
 iiiIiiii1i1 ( Oo0o00OO0000 )
elif oOo0 == 8047 :
 OOoi1Iiiiiii ( Oo0o00OO0000 )
elif oOo0 == 8048 :
 II1i1 ( Oo0o00OO0000 )
elif oOo0 == 8049 :
 ooO0OoOO0 ( Oo0o00OO0000 )
elif oOo0 == 804900 :
 o0oo00 ( Oo0o00OO0000 )
elif oOo0 == 8020 :
 Oo0 ( )
elif oOo0 == 8021 :
 ooOOOO ( Oo0o00OO0000 )
elif oOo0 == 8022 :
 II1iI ( Oo0o00OO0000 )
elif oOo0 == 8023 :
 Oo0o0 ( Oo0o00OO0000 )
elif oOo0 == 8040 :
 IIiI11i1111Ii ( )
elif oOo0 == 8041 :
 oO0OO0o0oo0o ( Oo0o00OO0000 )
elif oOo0 == 8042 :
 i1OO0o ( Oo0o00OO0000 )
elif oOo0 == 8043 :
 yt . PlayVideo ( Oo0o00OO0000 )
elif oOo0 == 8044 :
 ooOoOoO0o00o ( Oo0o00OO0000 )
elif oOo0 == 8060 :
 IIiiii ( )
elif oOo0 == 8061 :
 oO00oOOOO ( Oo0o00OO0000 )
elif oOo0 == 8064 :
 iIi ( )
elif oOo0 == 8065 :
 OO0ooo ( Oo0o00OO0000 )
elif oOo0 == 8070 :
 O0OO0Oo ( )
elif oOo0 == 8071 :
 II1111iII1 ( Oo0o00OO0000 )
elif oOo0 == 7080 :
 iio0000oO0OOOo0 ( Oo0o00OO0000 )
elif oOo0 == 8090 :
 i1Iiii1 ( )
elif oOo0 == 8091 :
 oO0000O0o ( Oo0o00OO0000 )
elif oOo0 == 8092 :
 O0oo0oO ( Oo0o00OO0000 )
elif oOo0 == 8093 :
 o0O0oOooo ( Oo0o00OO0000 )
elif oOo0 == 8081 :
 iio0ooo ( )
elif oOo0 == 8062 :
 iiooOOOo ( Oo0o00OO0000 )
elif oOo0 == 8063 :
 O00 ( Oo0o00OO0000 )
elif oOo0 == 8050 :
 oOOOoo0 ( )
elif oOo0 == 8051 :
 iI1i11II1i1i ( Oo0o00OO0000 )
elif oOo0 == 8052 :
 O0O0O00OoO0O ( Oo0o00OO0000 )
elif oOo0 == 8085 :
 iioOOOoOo0oOoo ( )
elif oOo0 == 8086 :
 Iii1iii11 ( Oo0o00OO0000 )
elif oOo0 == 8087 :
 oO0OOOo0OO ( Oo0o00OO0000 )
elif oOo0 == 8088 :
 i1IiI ( Oo0o00OO0000 , iiIiii1IIIII )
elif oOo0 == 9000 :
 i1iIII1IIi ( )
elif oOo0 == 1111 :
 o0O00O ( )
elif oOo0 == 9001 :
 O0Oo00oO0O00 ( )
elif oOo0 == 9002 :
 O0O0o0o0o ( )
elif oOo0 == 9003 :
 iii111iI1i11 ( )
elif oOo0 == 9004 :
 World1 ( )
elif oOo0 == 9005 :
 World2 ( Oo0o00OO0000 )
elif oOo0 == 9006 :
 World3 ( Oo0o00OO0000 )
elif oOo0 == 9007 :
 oo0OoooOo0 ( )
elif oOo0 == 9008 :
 ooo00OO ( Oo0o00OO0000 )
elif oOo0 == 9009 :
 iI1iIIIiIi ( Oo0o00OO0000 )
elif oOo0 == 9010 :
 i1IIIii1Ii1 ( )
elif oOo0 == 9011 :
 o000O00OO00O ( Oo0o00OO0000 )
elif oOo0 == 50 :
 OOoo ( Oo0o00OO0000 )
elif oOo0 == 9020 :
 champlist ( )
elif oOo0 == 9021 :
 o00OO0O00O0 ( )
elif oOo0 == 9022 :
 IiiI11I ( )
elif oOo0 == 9023 :
 ooOOoOo ( )
elif oOo0 == 9024 :
 iII111IiO00O ( Oo0o00OO0000 )
elif oOo0 == 9030 :
 iiii1II ( Oo0o00OO0000 )
elif oOo0 == 9031 :
 O00OOOO ( Oo0o00OO0000 )
elif oOo0 == 9032 :
 OOI11i1iiI1 ( Oo0o00OO0000 )
elif oOo0 == 9033 :
 IiIIi1I1iII ( Oo0o00OO0000 )
elif oOo0 == 9034 :
 O0II11i11II ( )
elif oOo0 == 7084 :
 I11iiI ( )
elif oOo0 == 7085 :
 I1IIIi1iI ( Oo0o00OO0000 )
elif oOo0 == 7086 :
 IIIIi1Ii111 ( Oo0o00OO0000 , ii1i , iII1 )
elif oOo0 == 7087 :
 OO00 ( iII1 )
elif oOo0 == 9666 :
 iI1i11 ( Oo0o00OO0000 )
elif oOo0 == 10100 : oO0ooOoOO ( )
elif oOo0 == 101001 : Ooo0o0ooO0 ( Oo0o00OO0000 )
elif oOo0 == 10105 : OOOo00O ( Oo0o00OO0000 )
elif oOo0 == 10106 : I1iOO000o0o0oo ( Oo0o00OO0000 )
elif oOo0 == 10104 : oooO0o0OoOo0O ( Oo0o00OO0000 )
elif oOo0 == 10107 : oO0o0O ( )
elif oOo0 == 10103 : oO00oOoo0ooO0 ( Oo0o00OO0000 )
elif oOo0 == 10108 : oOo000o ( Oo0o00OO0000 )
elif oOo0 == 10000 : Origin_Menu ( )
elif oOo0 == 10001 : Oo00o0O0O ( )
elif oOo0 == 10002 : OO0oo ( )
elif oOo0 == 10003 : O0Ii1iIii1I1 ( )
elif oOo0 == 10004 : iIII1II11I1 ( Oo0o00OO0000 )
elif oOo0 == 10005 : Oo0oo0OOO0OOoOO ( )
elif oOo0 == 10006 : OOoO0000o00 ( Oo0o00OO0000 )
elif oOo0 == 10007 : oOI1IIi11I1IiIi ( Oo0o00OO0000 , ii1i )
elif oOo0 == 10008 : oo0O0 ( )
elif oOo0 == 10009 : IIiiII11i11I ( )
elif oOo0 == 10010 : ooOooooOo00OO0o ( Oo0o00OO0000 )
elif oOo0 == 10011 : Oo0OO0ooO0O0O ( Oo0o00OO0000 )
elif oOo0 == 10012 : O0i1iI ( Oo0o00OO0000 )
elif oOo0 == 10113 : GRABG ( Oo0o00OO0000 , iiIiii1IIIII )
elif oOo0 == 10109 : oOo0o00O0oO0 ( Oo0o00OO0000 )
elif oOo0 == 10013 : iI1iIiI1Ii1iI ( Oo0o00OO0000 )
elif oOo0 == 10014 : i1IiI111IiiI1 ( )
elif oOo0 == 10015 : OO0o0O0 ( )
elif oOo0 == 10016 : i1IiIi1 ( Oo0o00OO0000 )
elif oOo0 == 10017 : oO0OIiIi1ii1Ii ( )
elif oOo0 == 10018 : OOoo000OO00 ( )
elif oOo0 == 10019 : oOi1IiIiIii11I ( )
elif oOo0 == 10020 : I11iIIiiIiIi ( )
elif oOo0 == 10021 : iii ( )
elif oOo0 == 10022 : IiiO0O0O0OOO0o ( Oo0o00OO0000 )
elif oOo0 == 10023 : ooOoOOiIiiII11 ( iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 10024 : IIIiII1iIII ( Oo0o00OO0000 )
elif oOo0 == 10025 : iIIIi1i1I11i ( )
elif oOo0 == 10026 : o000 ( )
elif oOo0 == 10027 : O000 ( )
elif oOo0 == 10028 : i1I ( )
elif oOo0 == 10029 : IIII11i1Ii ( )
elif oOo0 == 423 : ooOoo ( Oo0o00OO0000 )
elif oOo0 == 426 : I1i1 ( Oo0o00OO0000 )
elif oOo0 == 10030 : Izle_Films ( )
elif oOo0 == 10031 : Latest_Izle_Movies ( )
elif oOo0 == 10032 : Izle_Genres ( )
elif oOo0 == 10033 : Izle_Pop_Movies ( )
elif oOo0 == 10034 : Izle_Boxsets ( )
elif oOo0 == 10035 : Izle_Search ( )
elif oOo0 == 10036 : Izle_Genres_Movie ( Oo0o00OO0000 )
elif oOo0 == 10037 : Izle_Boxset_single ( Oo0o00OO0000 )
elif oOo0 == 10038 : Izle_IFRAME ( )
elif oOo0 == 10039 : Izle_Boxsets_Next ( Oo0o00OO0000 )
elif oOo0 == 10040 : O00OO ( )
elif oOo0 == 10041 : iIiiIi11 ( Oo0o00OO0000 )
elif oOo0 == 10042 : i1o0oOoooOoo0 ( Oo0o00OO0000 )
elif oOo0 == 10043 : i1Iii11iiI1 ( )
elif oOo0 == 10044 : oOoOo ( Oo0o00OO0000 )
elif oOo0 == 10045 : ooOiiIII ( iiIiii1IIIII )
elif oOo0 == 10046 : oO0Ooo00O ( Oo0o00OO0000 )
elif oOo0 == 10047 : II1II1ii1Ii ( Oo0o00OO0000 )
elif oOo0 == 10048 : i1i11IiII ( Oo0o00OO0000 )
elif oOo0 == 10049 : I1i1ii1IiI1i ( Oo0o00OO0000 )
elif oOo0 == 10050 : IiO00Oooo0o000 ( )
elif oOo0 == 10051 : OoOo0Oo0 ( )
elif oOo0 == 10052 : ii1i1II1 ( )
elif oOo0 == 10053 : Addon ( Oo0o00OO0000 )
elif oOo0 == 10054 : o0OOoo ( Oo0o00OO0000 , iiIiii1IIIII )
elif oOo0 == 10055 :
 I1iiii ( "addFavorite" )
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 i1IO00oO0oOOOOOO ( iiIiii1IIIII , Oo0o00OO0000 , ii1i , ooo0O0o00O , OoooOO0 )
elif oOo0 == 10056 :
 I1iiii ( "rmFavorite" )
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 iIiii1 ( iiIiii1IIIII )
elif oOo0 == 10057 :
 I1iiii ( "getFavorites" )
 I1i11IIiiIiI ( )
elif oOo0 == 10058 : iiIIiI1 ( )
elif oOo0 == 10059 : Donators_Guide ( )
elif oOo0 == 10060 : oO0oOOoo00000 ( )
elif oOo0 == 10061 : Iii1i1Ii ( )
elif oOo0 == 10062 : iIi1iI ( iiIiii1IIIII , Oo0o00OO0000 , iII1 )
elif oOo0 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + IIIii1II1II + ")" )
elif oOo0 == 10064 : o00oo ( )
elif oOo0 == 10065 : O00O0 ( Oo0o00OO0000 )
elif oOo0 == 10066 : o0oOO ( Oo0o00OO0000 )
elif oOo0 == 10068 : OOO0ooo ( Oo0o00OO0000 )
elif oOo0 == 10069 : OOOoO ( Oo0o00OO0000 )
elif oOo0 == 10070 : IIiI1iIi1 ( Oo0o00OO0000 )
elif oOo0 == 10071 : Genie_Watch ( )
elif oOo0 == 10072 : o0OoOoo ( )
elif oOo0 == 10073 : Iii1II1ii ( Oo0o00OO0000 )
elif oOo0 == 10074 : oOoO0 ( Oo0o00OO0000 )
elif oOo0 == 10075 : Oo0o0ooOoO ( ii1i , iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 10076 : OOooO ( Oo0o00OO0000 )
elif oOo0 == 10077 : OO0O0OO0O0 ( Oo0o00OO0000 )
elif oOo0 == 10078 : OooO ( )
elif oOo0 == 10079 : Genie_Watch_Tv_Shows ( )
elif oOo0 == 10080 : Genie_Watch_Tv_Genre ( Oo0o00OO0000 )
elif oOo0 == 10081 : Genie_Watch_TV_PlayRun ( Oo0o00OO0000 )
elif oOo0 == 10082 : Genie_Watch_TV_Episodes ( Oo0o00OO0000 , ii1i )
elif oOo0 == 10083 : Genie_Watch_Tv_Recent ( Oo0o00OO0000 )
elif oOo0 == 10084 : i11I1I1iiI ( )
elif oOo0 == 10085 : I11iiI1i1 ( )
elif oOo0 == 10086 : iioOooOOOoOo ( )
elif oOo0 == 20000 : II111I11iI ( )
elif oOo0 == 20001 : oooii111I1I1I ( Oo0o00OO0000 )
elif oOo0 == 20002 : IiI111i ( Oo0o00OO0000 )
elif oOo0 == 20003 : o00oo00oo ( Oo0o00OO0000 )
elif oOo0 == 20004 : o0o00oo ( Oo0o00OO0000 )
elif oOo0 == 20005 : ooI1 ( Oo0o00OO0000 )
elif oOo0 == 21004 : I1IIII ( )
elif oOo0 == 21005 : oo0oO0o00Oo0 ( Oo0o00OO0000 )
elif oOo0 == 21006 : i1I1IO0O ( Oo0o00OO0000 )
elif oOo0 == 21007 : O0o0ooo0 ( Oo0o00OO0000 )
elif oOo0 == 21008 : O0OoooO0 ( Oo0o00OO0000 )
elif oOo0 == 21009 : OOOOoOOo0O0 ( Oo0o00OO0000 )
elif oOo0 == 30000 : iI1I11 ( )
elif oOo0 == 30001 : oo000O ( )
elif oOo0 == 100121 : Resolve ( Oo0o00OO0000 )
elif oOo0 == 30003 : Oooooo0O ( )
elif oOo0 == 30004 : O0OOoo ( Oo0o00OO0000 )
elif oOo0 == 30005 : i1Ii111 ( Oo0o00OO0000 )
elif oOo0 == 30006 : O0OO0oOo00o0 ( )
elif oOo0 == 30007 : iiII1iiI ( )
elif oOo0 == 30008 : IiiiiI ( Oo0o00OO0000 )
elif oOo0 == 30009 : I1i1iI1I1II ( Oo0o00OO0000 )
elif oOo0 == 30010 : Ii1i1iiiIiIIiIiiii ( Oo0o00OO0000 )
elif oOo0 == 30011 : IiIi1 ( )
elif oOo0 == 30012 : o00OoOo0 ( )
elif oOo0 == 30013 : o0O0ooo0o ( )
elif oOo0 == 30014 : OOO0O ( )
elif oOo0 == 30015 : IIi1I1 ( Oo0o00OO0000 , ii1i , ooo0O0o00O )
elif oOo0 == 30016 : oO0O0ooOoo ( Oo0o00OO0000 )
elif oOo0 == 30019 : i1Ii1I ( Oo0o00OO0000 )
elif oOo0 == 30017 : o00o0o0o ( Oo0o00OO0000 )
elif oOo0 == 30018 : OoOooooo ( Oo0o00OO0000 )
elif oOo0 == 30030 : iii1OO00Oo00o ( )
elif oOo0 == 30031 : ooo0Oo00O ( )
elif oOo0 == 30032 : II1II1iIIi11 ( )
elif oOo0 == 30033 : Ii1 ( )
elif oOo0 == 30034 : IiII1Iiii ( )
elif oOo0 == 30035 : I1I11iII11 ( Oo0o00OO0000 )
elif oOo0 == 30036 : O0O000OOOoO ( Oo0o00OO0000 )
elif oOo0 == 30037 : O0Oo0O0O0o ( Oo0o00OO0000 )
elif oOo0 == 30038 : OoOo0 ( )
elif oOo0 == 30039 : ooO0O00Oo0o ( )
elif oOo0 == 50000 : ooo00Ooo ( )
elif oOo0 == 50001 : oOOoOo0OoOO ( )
elif oOo0 == 50002 : i1I11iIIiIIiIi ( Oo0o00OO0000 )
elif oOo0 == 50003 : Table_Menu ( iII1 )
elif oOo0 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif oOo0 == 60001 : Iii1 ( )
elif oOo0 == 60002 : i1i11ii ( iiIiii1IIIII )
elif oOo0 == 60003 : OOoOo0O0 ( Oo0o00OO0000 )
elif oOo0 == 600033 : iiiI1i ( Oo0o00OO0000 )
elif oOo0 == 60004 : i1Iii ( Oo0o00OO0000 )
elif oOo0 == 50004 : iiI11 ( )
elif oOo0 == 50005 : speedtest . runtest ( Oo0o00OO0000 )
elif oOo0 == 70001 : o0oO00oooo ( )
elif oOo0 == 70002 : Ii1I1i1IiiI ( Oo0o00OO0000 )
elif oOo0 == 70003 : IiiiI1i ( Oo0o00OO0000 )
elif oOo0 == 70004 : I1iIi1i ( Oo0o00OO0000 )
elif oOo0 == 70005 : I1II1iI ( Oo0o00OO0000 )
elif oOo0 == 70006 : iIii1Ii11I1i ( )
elif oOo0 == 50006 : Ii1I1Ii ( i1 , i1111 )
elif oOo0 == 80000 : I11OoooO ( )
elif oOo0 == 80001 : resolvefilmon ( Oo0o00OO0000 )
elif oOo0 == 80002 : i11IiIiii ( )
elif oOo0 == 80003 : iiI1Ii1iiii1i ( iiIiii1IIIII , Oo0o00OO0000 , "None" )
elif oOo0 == 80004 : iiII11ii1Ii ( iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 80005 : ooo0oooo0 ( )
elif oOo0 == 80006 : ii1oooO0o0oOoO ( Oo0o00OO0000 )
elif oOo0 == 80007 : I11iii ( Oo0o00OO0000 )
elif oOo0 == 80008 : IIi111 ( )
elif oOo0 == 80009 : OooOooO0OoOoo0o ( )
elif oOo0 == 80010 : iII1iIIIIII ( Oo0o00OO0000 )
elif oOo0 == 80011 : ooO0OOO ( Oo0o00OO0000 )
elif oOo0 == 80012 : Oo0oOOo00o ( )
elif oOo0 == 90000 : O000o0O0 ( iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 90001 : tools ( )
elif oOo0 == 90002 : OO0o0oO ( )
elif oOo0 == 90003 : oo0OOO0O0 ( Oo0o00OO0000 )
elif oOo0 == 90004 : OoooOooo ( Oo0o00OO0000 )
elif oOo0 == 90005 : IiIi1iiII ( Oo0o00OO0000 )
elif oOo0 == 90006 : II1IIi1ii111 ( Oo0o00OO0000 )
elif oOo0 == 90007 : II1OO ( Oo0o00OO0000 )
elif oOo0 == 90008 : O0oOO0o0 ( Oo0o00OO0000 )
elif oOo0 == 90009 : I11iiI1 ( Oo0o00OO0000 )
elif oOo0 == 90010 : OOOOO0O00 ( )
elif oOo0 == 90020 : OOoO00OOo ( )
elif oOo0 == 90021 : hellyeah2 ( Oo0o00OO0000 )
elif oOo0 == 90022 : hellyeah3 ( Oo0o00OO0000 )
elif oOo0 == 90023 : i1I1i ( )
elif oOo0 == 90024 : oOOOoo0o ( Oo0o00OO0000 )
elif oOo0 == 90025 : o0I1IIIi11ii11 ( Oo0o00OO0000 )
if 43 - 43: Ii % oO0o
elif oOo0 == 90026 : OOOo0o0O ( )
elif oOo0 == 90027 : oOO0ooO ( iiIiii1IIIII , Oo0o00OO0000 , iII1 )
elif oOo0 == 90028 : iiiI1IiI ( Oo0o00OO0000 )
if 100 - 100: ooOoO0O00
elif oOo0 == 900300 : i1II1I1Iii1 ( )
elif oOo0 == 900301 : O0o ( Oo0o00OO0000 )
elif oOo0 == 900302 : iII111Ii ( Oo0o00OO0000 )
elif oOo0 == 90030 : Oo0OO0000oooo ( )
elif oOo0 == 90031 : Treplays ( )
elif oOo0 == 90032 : Treplays2 ( Oo0o00OO0000 )
elif oOo0 == 90033 : Treplays3 ( Oo0o00OO0000 )
elif oOo0 == 90034 : Treplays4 ( Oo0o00OO0000 )
elif oOo0 == 90035 : O0OoO0ooOO0o ( Oo0o00OO0000 )
elif oOo0 == 90036 : oOoOO0o ( Oo0o00OO0000 )
elif oOo0 == 90039 : OOoOo ( Oo0o00OO0000 )
elif oOo0 == 90037 : iI11i ( Oo0o00OO0000 )
elif oOo0 == 900377 : i1IiI1I ( Oo0o00OO0000 )
elif oOo0 == 90038 : Oo00oO0oOO ( )
if 4 - 4: Ii - IIIi11I1 * o0O00o % ii - OOooOOo
elif oOo0 == 10090 : Oo0000O0OOooO ( )
elif oOo0 == 10091 : o00ooO0 ( Oo0o00OO0000 )
elif oOo0 == 10092 : o0o0OoOo0 ( Oo0o00OO0000 )
elif oOo0 == 10093 : OO0OOo00Oo ( Oo0o00OO0000 , ii1i )
elif oOo0 == 10094 : o000oOoOOO ( Oo0o00OO0000 , ii1i )
if 81 - 81: Ii1i1i * oOOoOooOo . ooOO0O0ooOooO . o0O00o
elif oOo0 == 10095 : i1111IIiii1 ( )
elif oOo0 == 10096 : IiiIi1 ( Oo0o00OO0000 )
elif oOo0 == 10097 : OOOOoO ( Oo0o00OO0000 )
elif oOo0 == 10098 : oOo0OOOOoO ( Oo0o00OO0000 )
elif oOo0 == 10099 : iI1IIiiIIIII ( Oo0o00OO0000 )
if 71 - 71: o0O00o + oO0o
elif oOo0 == 10200 : IiO000O0OO00oo ( )
elif oOo0 == 10201 : O0OOo ( iiIiii1IIIII , Oo0o00OO0000 , iII1 )
elif oOo0 == 10202 : o00oo0OO0 ( Oo0o00OO0000 )
elif oOo0 == 10203 : RT4 ( Oo0o00OO0000 )
if 39 - 39: oOo0O0Ooo % o0O00o / IIiIiII11i / IIiIiII11i
elif oOo0 == 90040 : iII11II1II ( )
elif oOo0 == 90041 : o0O00OooooO ( Oo0o00OO0000 )
elif oOo0 == 90042 : oO0oo ( Oo0o00OO0000 )
elif oOo0 == 90043 : I111 ( Oo0o00OO0000 )
elif oOo0 == 90044 : iiII1i ( Oo0o00OO0000 )
elif oOo0 == 90045 : o0Oo00oOO ( )
elif oOo0 == 90046 : IiiiI1 ( Oo0o00OO0000 )
elif oOo0 == 90050 : I1IiO00Ooo0ooo0 ( )
elif oOo0 == 90051 : i11Ii ( Oo0o00OO0000 )
elif oOo0 == 90052 : Oo0OoOo ( Oo0o00OO0000 )
elif oOo0 == 90053 : IIi1ii ( Oo0o00OO0000 )
elif oOo0 == 90054 : Oo0OO00OO0Oo ( Oo0o00OO0000 )
elif oOo0 == 90055 : OO0oOoO000o0 ( )
if 95 - 95: IIiIiII11i + Ii + I11i
elif oOo0 == 100001 : Stand_up ( )
if 30 - 30: o0o00Oo0O - o0o00Oo0O % iI11I1II1I1I + IIIIiiII111 * ii
elif oOo0 == 100003 : i1IiIi1 ( Oo0o00OO0000 )
elif oOo0 == 100004 : O0oooo0OoO0oo ( Oo0o00OO0000 )
elif oOo0 == 100005 : Resolve ( Oo0o00OO0000 )
elif oOo0 == 100008 : Search ( )
elif oOo0 == 100007 : IiI1IiI11iII ( Oo0o00OO0000 )
elif oOo0 == 100009 : yt . PlayVideo ( Oo0o00OO0000 )
elif oOo0 == 100010 : o0OO ( Oo0o00OO0000 )
elif oOo0 == 100100 : IIiI1i ( ii1i , Oo0o00OO0000 , O0ooooo000 )
elif oOo0 == 100101 : I11IiIIIi ( Oo0o00OO0000 , iiIiii1IIIII , ooo0O0o00O , O0ooooo000 , ii1i )
elif oOo0 == 100102 : OoIIi1iI ( iiIiii1IIIII , Oo0o00OO0000 , ii1i , ooo0O0o00O )
elif oOo0 == 100106 : ooO ( Oo0o00OO0000 , iiIiii1IIIII )
elif oOo0 == 100107 : I1IIiiI1II1 ( )
elif oOo0 == 100108 : o0OooIi1III1 ( )
elif oOo0 == 100109 : OoOooO0 ( Oo0o00OO0000 )
elif oOo0 == 40000 : iio00O0o00oo ( )
elif oOo0 == 40001 : Oooo0o0oO ( Oo0o00OO0000 )
elif oOo0 == 100110 : O00OOoo000o ( Oo0o00OO0000 )
elif oOo0 == 100111 : i1iiI1i ( Oo0o00OO0000 )
elif oOo0 == 100112 : I1iIiIii ( Oo0o00OO0000 )
elif oOo0 == 100113 : Oo0oOO0O00 ( Oo0o00OO0000 )
elif oOo0 == 100114 : iiIIIIiI111 ( Oo0o00OO0000 )
elif oOo0 == 100115 : i11o00Ooo ( Oo0o00OO0000 )
elif oOo0 == 100117 : OoooOO0Oo0 ( Oo0o00OO0000 )
elif oOo0 == 100118 : I11I1I1i1i ( Oo0o00OO0000 )
elif oOo0 == 100120 : OoO00OOoOOOo0 ( Oo0o00OO0000 )
elif oOo0 == 1001200 : oOoO00O ( Oo0o00OO0000 )
elif oOo0 == 100210 : Oo0O0Oo00O ( Oo0o00OO0000 )
elif oOo0 == 100211 : oooooO00OOO ( )
elif oOo0 == 100212 : I11i1I11iIii ( )
elif oOo0 == 100213 : oO0oO ( )
elif oOo0 == 100214 : OO0OOOOOo ( )
elif oOo0 == 1000111 :
 oOO0o ( Oo0o00OO0000 )
 if 1 - 1: o0o00Oo0O
elif oOo0 == 1001111 :
 I1III111i ( iiIiii1IIIII , Oo0o00OO0000 )
 if 36 - 36: ooOO0O0ooOooO . IIIIiiII111
elif oOo0 == 1002111 :
 IiioOoo0ooo ( )
 if 62 - 62: iIII + iI11I1II1I1I % iIII * IIIi11I1 + iI11I1II1I1I % Ii1i1i
elif oOo0 == 1003111 :
 OooiIII ( Oo0o00OO0000 , iiIiii1IIIII )
 if 56 - 56: I11i
elif oOo0 == 1004111 :
 O0o0 ( )
 if 55 - 55: ooOO0O0ooOooO - o0O0Oooo0O / oOOoOooOo % oOo0O0Ooo * ii * oOo0O0Ooo
elif oOo0 == 1005111 :
 iiIi1I1i1i ( Oo0o00OO0000 , iiIiii1IIIII )
elif oOo0 == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( Oo0o00OO0000 , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( iiIiii1IIIII , Oo0o00OO0000 , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( iiIiii1IIIII , Oo0o00OO0000 , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1105000 :
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( iiIiii1IIIII , Oo0o00OO0000 , ii1i , ooo0O0o00O , OoooOO0 )
elif oOo0 == 1106000 :
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( iiIiii1IIIII )
elif oOo0 == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( Oo0o00OO0000 )
elif oOo0 == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( iiIiii1IIIII )
elif oOo0 == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif oOo0 == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( Oo0o00OO0000 )
elif oOo0 == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in Oo0o00OO0000 :
  import urlresolver
  oooO0 = urlresolver . resolve ( Oo0o00OO0000 )
  IIi1IIIi = xbmcgui . ListItem ( path = oooO0 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIi1IIIi )
 elif not Oo0o00OO0000 . startswith ( "plugin://plugin" ) or not any ( x in Oo0o00OO0000 for x in pyramid . g_ignoreSetResolved ) :
  IIi1IIIi = xbmcgui . ListItem ( path = Oo0o00OO0000 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIi1IIIi )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + Oo0o00OO0000 + ')' )
elif oOo0 == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( iiIiii1IIIII , playlist )
elif oOo0 == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( Oo0o00OO0000 , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1117000 :
 Oo0o00OO0000 , o0o000 = getRegexParsed ( regexs , Oo0o00OO0000 )
 if Oo0o00OO0000 :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( Oo0o00OO0000 , iiIiii1IIIII , ii1i , o0o000 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif oOo0 == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 II1IiiiIIiii = youtubedl . single_YD ( Oo0o00OO0000 )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( II1IiiiIIiii , iiIiii1IIIII , ii1i )
elif oOo0 == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( Oo0o00OO0000 ) , iiIiii1IIIII , ii1i , True )
elif oOo0 == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , iiIiii1IIIII , 'video' )
elif oOo0 == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( Oo0o00OO0000 , iiIiii1IIIII , 'video' )
elif oOo0 == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( Oo0o00OO0000 , iiIiii1IIIII , 'audio' )
elif oOo0 == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1126000 :
 iiIiii1IIIII = iiIiii1IIIII . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( Oo0o00OO0000 , search_term = iiIiii1IIIII [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( Oo0o00OO0000 )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif oOo0 == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif oOo0 == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif oOo0 == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( iiIiii1IIIII , Oo0o00OO0000 , ii1i , ooo0O0o00O )
elif oOo0 == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( Oo0o00OO0000 , ii1i , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( iiIiii1IIIII , Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( Oo0o00OO0000 )
elif oOo0 == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oOo0 == 9050000 : IiIiIi1I1 ( )
elif oOo0 == 9060000 : I1III111i ( iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 9080000 : oOOOiIi1I1 ( )
elif oOo0 == 9070000 : OoOoO0OoOOOOo ( )
elif oOo0 == 9090000 : iI1I1II1 ( )
elif oOo0 == 9100000 : ooOoOO ( )
elif oOo0 == 9110000 : oO0ooOO ( )
elif oOo0 == 9110001 : IIIIIiI ( Oo0o00OO0000 )
elif oOo0 == 9110002 : i1i11I ( Oo0o00OO0000 , iiIiii1IIIII , ii1i )
elif oOo0 == 9110003 : o0O0OO ( iiIiii1IIIII , O0ooooo000 )
elif oOo0 == 9110005 : ooo ( iII1 , Oo0o00OO0000 )
elif oOo0 == 9110004 : Oo00O0ooOO ( )
elif oOo0 == 9110010 : o0Ooo ( Oo0o00OO0000 )
elif oOo0 == 9110011 : OOoOOOo00 ( )
elif oOo0 == 9110012 : iiIiiiI ( Oo0o00OO0000 , iiIiii1IIIII )
elif oOo0 == 9110013 : ii111Ii11iii ( Oo0o00OO0000 )
elif oOo0 == 9110014 : iIIi ( iiIiii1IIIII , Oo0o00OO0000 )
elif oOo0 == 9110015 : i1I11iIII1i1I ( )
elif oOo0 == 9999999 : OO0oI1iii1i ( )
elif oOo0 == 19999999 : OO0i1Ii11ii1I ( )
elif oOo0 == 1999990 : o0oO00 ( )
elif oOo0 == 21999990 : i11I ( )
elif oOo0 == 21999991 : o00Oo0oooooo ( Oo0o00OO0000 )
elif oOo0 == 21999992 : o00o ( Oo0o00OO0000 )
elif oOo0 == 21999993 : IIIIiiIiiI ( Oo0o00OO0000 )
elif oOo0 == 21999994 : IIIIiI11I11 ( Oo0o00OO0000 , ii1i )
elif oOo0 == 21999995 : oo00o0 ( Oo0o00OO0000 )
elif oOo0 == 21999996 : OOoOO0ooo ( Oo0o00OO0000 , ii1i )
elif oOo0 == 21999997 : I11iiii ( Oo0o00OO0000 , ii1i )
elif oOo0 == 21999998 : IiI1iiiIii ( iiIiii1IIIII , Oo0o00OO0000 , ii1i )
elif oOo0 == 219999989 : oOooO0 ( )
elif oOo0 == 219999990 : iiI ( all = True )
elif oOo0 == 219999991 : O000oOOoOOO ( )
elif oOo0 == 219999992 : iIII11Ii1iI1II ( )
if 97 - 97: Ii1i1i - Ii1i1i . IIIIiiII111 + Ii1i1i + IIIIiiII111
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
