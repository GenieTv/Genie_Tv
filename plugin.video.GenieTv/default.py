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
  if 90 - 90: Ii1i1i . o0O00o
  if 81 - 81: IIIi11I1 - iIII % oOOoOooOo - oO0o / I1ii11iIi11i
  if 4 - 4: ii - ooOoO0O00 % Ii1i1i - IIIi11I1 * I11i
  if 85 - 85: ii * iI11I1II1I1I . IIIIiiII111 / ii % oOo0O0Ooo % o0o00Oo0O
  if 36 - 36: Ii1i1i / IIiIiII11i / o0O00o / o0O00o + Ii1I
 else :
  if 95 - 95: o0O00o
  if 51 - 51: IIiIiII11i + o0O00o . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
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
  if 72 - 72: ooOO0O0ooOooO + ooOO0O0ooOooO / IIiIiII11i . ii % Ii1i1i
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']KIDS[/COLOR]' , str ( iI1iIIiiii ) , 4007 , iiiiiIIii + 'Kids.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']COZY CORNER[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 21999990 , iiiiiIIii + 'zone.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiiiiIIii + 'zone.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FREEVIEW[/COLOR]' , str ( iI1iIIiiii ) , 90023 , iiiiiIIii + 'freeview.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']FOOTBALL[/COLOR]' , '' , 10002 , iiiiiIIii + 'Football.png' , iIi1ii1I1 , '' )
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
   if 57 - 57: IIIi11I1 + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
   if 83 - 83: I11i / Ii % iI11I1II1I1I . iIII % ooOO0O0ooOooO . ii
   if 94 - 94: Ii1i1i + iI11I1II1I1I % oO0o
   if 93 - 93: Ii1i1i - IIIi11I1 + iI11I1II1I1I * I11i + o0O0Oooo0O . IIIIiiII111
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def IiI1iII1II111 ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']FOOTBALL[/COLOR]' , '[COLOR' + II11iiii1Ii + ']KIDS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']NEWS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']HOBBIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DISCLOSE TV[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']CATEGORIES[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  IIiI11i1111Ii ( )
 if OoOOo0OOoO == 1 :
  o00O0O ( )
 if OoOOo0OOoO == 2 :
  oOO ( )
 if OoOOo0OOoO == 3 :
  O00o00O ( )
 if OoOOo0OOoO == 4 :
  ii1iii11i1 ( )
 if OoOOo0OOoO == 5 :
  I11Oo00oO0O ( )
  if 96 - 96: Ii1I / IIiIiII11i . Ii1i1i - IIIIiiII111 * iIII * ooOO0O0ooOooO
  if 76 - 76: Ii1i1i - IIiIiII11i * IIIi11I1 / ii
def IIIiIi ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']POPCORN BOX[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DESI FLIX[/COLOR]' , '[COLOR' + II11iiii1Ii + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CLASSIC MOVIES[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']MOVIES[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   IiiIIIII1iii ( )
  if OoOOo0OOoO == 1 :
   IIiiii ( )
  if OoOOo0OOoO == 2 :
   iI111i1I1II ( Oo0o00OO0000 )
  if OoOOo0OOoO == 3 :
   O00OO ( )
  if OoOOo0OOoO == 4 :
   II1Ii1iI1i1 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if OoOOo0OOoO == 5 :
   o0OoO000O ( )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH MOVIES[/COLOR]' , str ( iI1iIIiiii ) , 9001 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TOP RATED MOVIES[/COLOR]' , str ( iI1iIIiiii ) , 10200 , iiiiiIIii + 'rated.png' , iIi1ii1I1 , '' )
  if 94 - 94: OOooOOo . o0o00Oo0O / Ii1i1i . Ii1I - ooOoO0O00
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']POPCORN BOX[/COLOR]' , str ( iI1iIIiiii ) , 7061 , iiiiiIIii + 'PopcornBox.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Desi Flix[/COLOR]' , '' , 80005 , iiiiiIIii + 'Desi.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiiiiIIii + 'FilmTrailers.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiiiiIIii + 'ClassicMovies.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def iIi1III1I ( ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']DAILY LISTS[/COLOR]' , '' , 9007 , o0 , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , o0 , iIi1ii1I1 , '' )
 if 71 - 71: o0O0Oooo0O
 if 11 - 11: o0o00Oo0O / oO0o % IIIi11I1 + I11i + iI11I1II1I1I
 if 40 - 40: oOOoOooOo - IIIi11I1 . Ii1i1i * I1ii11iIi11i % o0O0Oooo0O
 if 56 - 56: Ii . I11i - oOo0O0Ooo * iIII
 if 91 - 91: ooOO0O0ooOooO + ii - ooOoO0O00
def o000 ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Dans Scrapes[/COLOR]' , '[COLOR' + II11iiii1Ii + ']THE SOURCE[/COLOR]' , '[COLOR' + II11iiii1Ii + ']WATCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']RETURN DATES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CLASSIC TV[/COLOR]' , '[COLOR' + II11iiii1Ii + ']TV SHOW TRAILERS[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TV SHOWS[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   OOooo0O ( )
  if OoOOo0OOoO == 1 :
   iiI1iIIiI ( 'http://www.tvmaze.com/shows' )
  if OoOOo0OOoO == 2 :
   oOooo ( )
  if OoOOo0OOoO == 3 :
   oo00OOoOoO00 ( )
  if OoOOo0OOoO == 4 :
   I1iii ( )
  if OoOOo0OOoO == 5 :
   oOO0OO0O ( )
  if OoOOo0OOoO == 6 :
   o00oIII11I ( )
  if OoOOo0OOoO == 7 :
   Ii1I11I ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH SERIES[/COLOR]' , str ( iI1iIIiiii ) , 9002 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
  if 36 - 36: o0o00Oo0O + I1ii11iIi11i
  if 5 - 5: I1ii11iIi11i * OOooOOo
  if 46 - 46: oOOoOooOo
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Dans Scrapes[/COLOR]' , 'http://www.tvmaze.com/shows' , 9110001 , iiiiiIIii + 'ClassicTV.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiiiiIIii + 'iWatchSeries.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']RETURN DATES[/COLOR]' , str ( iI1iIIiiii ) , 10095 , iiiiiIIii + 'RD.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CLASSIC TV[/COLOR]' , str ( iI1iIIiiii ) , 8064 , iiiiiIIii + 'ClassicTV.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiiiiIIii + 'TVShowTrailers.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def I11iIiII ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   OO0OO0OO = '[COLOR' + II11iiii1Ii + ']Murrays Mints[/COLOR]'
   if 61 - 61: ii . ooOO0O0ooOooO . ii / I1ii11iIi11i
   if 72 - 72: ooOoO0O00
   if 82 - 82: OOooOOo + ii / Ii * Ii1I . ii
   if 63 - 63: Ii1I
  I11ii1IIiIi = [ OO0OO0OO , '[COLOR' + II11iiii1Ii + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']BAMF TV[/COLOR]' , '[COLOR' + II11iiii1Ii + ']PIRATE MOVIES[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']StreamTeam[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   i1II ( )
  if OoOOo0OOoO == 1 :
   IiiI11i1I ( )
  if OoOOo0OOoO == 2 :
   OOo0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if OoOOo0OOoO == 3 :
   iiIii1IIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , ii1IiIiI1 , iiIiii1IIIII )
 else :
  if 90 - 90: I11i - Ii + ooOoO0O00 - Ii1i1i % I1ii11iIi11i
  if 59 - 59: IIIi11I1 % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * o0O00o
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Murrays Mints[/COLOR]' , str ( iI1iIIiiii ) , 10025 , iiiiiIIii + 'PandorasBox.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiiiiIIii + 'Technica-Streams.png' , iIi1ii1I1 , '' )
  if 41 - 41: Ii1i1i % Ii1I
  if 12 - 12: IIIi11I1
  if 69 - 69: ii + IIIi11I1
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiiiiIIii + 'bamftv.png' , iIi1ii1I1 , '' )
  if 26 - 26: I1ii11iIi11i + IIIi11I1 / oO0o % OOooOOo % Ii1I + IIiIiII11i
  if 31 - 31: iIII % IIIi11I1 * iIII
  if 45 - 45: ooOoO0O00 . oOo0O0Ooo + IIIi11I1 - ii % oOOoOooOo
  if 1 - 1: iI11I1II1I1I
  if 93 - 93: ooOoO0O00 . Ii . I1ii11iIi11i
  if 99 - 99: iIII - o0O0Oooo0O - ooOO0O0ooOooO % oO0o
  if 21 - 21: IIiIiII11i % Ii1I . ooOoO0O00 - ii
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 4 - 4: ii . oOOoOooOo
def oOO0oo ( ) :
 OOooOoooOoOo ( )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiiiiIIii + 'SilentHunter.png' , iIi1ii1I1 , '' )
def OOo0 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 I1Ii = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 II1iIi1IiIii = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for iiIiii1IIIII , iII11 , url in Ii1i1iI1iIIi :
  if '247ch' in url :
   I111I11I111 ( iiIiii1IIIII , url , 10190 , iII11 )
  elif '.m3u' in url :
   I111I11I111 ( iiIiii1IIIII , url , 1019 , iII11 )
  elif '.xml' in url :
   I111I11I111 ( iiIiii1IIIII , url , 1018 , iII11 )
  else :
   iiiiI11ii ( iiIiii1IIIII , url , 222 , iII11 )
 for iiIiii1IIIII , url , iII11 in I1Ii :
  if '.xml' in url :
   I111I11I111 ( iiIiii1IIIII , url , 1018 , iII11 )
  elif '.m3u' in url :
   I111I11I111 ( iiIiii1IIIII , url , 1019 , iII11 )
  else :
   iiiiI11ii ( iiIiii1IIIII , url , 222 , iII11 )
 for iiIiii1IIIII , url , iII11 in II1iIi1IiIii :
  iiiiI11ii ( iiIiii1IIIII , url , 8043 , iII11 )
def O0i1i1II1i11 ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'BAMFTV.png' )
def iI111I11i ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iII11 )
  if 23 - 23: Ii1i1i . I11i + I1ii11iIi11i - IIIi11I1
def IiiI11i1I ( ) :
 if 18 - 18: OOooOOo % Ii % Ii1I / ooOO0O0ooOooO / I11i / ooOoO0O00
 Iii ( '[COLOR' + II11iiii1Ii + ']All Movies[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' ) ) , 9110013 , iiiiiIIii + 'scraped.png' , iIi1ii1I1 , '' , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']Movies By Genre[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' ) ) , 9110013 , iiiiiIIii + 'scraped.png' , iIi1ii1I1 , '' , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']Movies By A - Z[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ) ) , 9110013 , iiiiiIIii + 'scraped.png' , iIi1ii1I1 , '' , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']Search[/COLOR]' , '' , 9110015 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' , '' )
 if 48 - 48: OOooOOo + iIII / o0O00o + IIiIiII11i
 if 18 - 18: Ii1I
 if 23 - 23: IIiIiII11i
 if 24 - 24: iI11I1II1I1I + iI11I1II1I1I * IIIIiiII111
def i1I11iIII1i1I ( url ) :
 O0o0O0 = requests . get ( url ) . text
 Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for oOO0ooIiIIi1I1I11Ii , o0OO , Oo , O0iIiIIIIIii , iiIiI , o0Ooo0O00 , ooo0O0o00O in Ii1i1iI1iIIi :
  if ooo0O0o00O == ' ' :
   ooo0O0o00O = iIi1ii1I1
  if O0iIiIIIIIii == ' ' :
   O0iIiIIIIIii = o0
  iiIiI = iiIiI . replace ( '\\n' , ' ' )
  if o0OO == 'Movie Search' :
   Ooo00OoOOO ( oOO0ooIiIIi1I1I11Ii , o0Ooo0O00 , 9110014 , O0iIiIIIIIii , ooo0O0o00O , iiIiI , '' )
  elif o0OO == 'Menu' :
   Iii ( oOO0ooIiIIi1I1I11Ii , Oo , 9110013 , O0iIiIIIIIii , ooo0O0o00O , iiIiI , '' )
   if 9 - 9: o0o00Oo0O . o0O00o
def o0oooO ( name , url ) :
 from imports import Scrape_Nan
 name = str ( name )
 o0Ooo0O00 = str ( url )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( name , o0Ooo0O00 , '' )
 if 89 - 89: IIiIiII11i / ooOO0O0ooOooO
def IIo0OoO00 ( ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search your moive' , type = xbmcgui . INPUT_ALPHANUM )
 iiI11Iii = [ 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=' , 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==' ]
 for Oo0o00OO0000 in iiI11Iii :
  O0o0O0 = requests . get ( i11 ( Oo0o00OO0000 ) ) . content
  Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
  for oOO0ooIiIIi1I1I11Ii , o0OO , Oo , O0iIiIIIIIii , iiIiI , o0Ooo0O00 , ooo0O0o00O in Ii1i1iI1iIIi :
   if ooo0O0o00O == ' ' :
    ooo0O0o00O = iIi1ii1I1
   if O0iIiIIIIIii == ' ' :
    O0iIiIIIIIii = o0
   iiIiI = iiIiI . replace ( '\\n' , ' ' )
   if o0OO == 'Movie Search' :
    if IIIIIiII1 . lower ( ) in oOO0ooIiIIi1I1I11Ii . lower ( ) :
     Ooo00OoOOO ( oOO0ooIiIIi1I1I11Ii , o0Ooo0O00 , 9110014 , O0iIiIIIIIii , ooo0O0o00O , iiIiI , '' )
def iii11 ( url ) :
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url , o0OO , iI , ooo0O0o00O , i11II1I11I1 in Ii1i1iI1iIIi :
  if iI == '123' :
   iI = iiiiiIIii + 'appstreams.png'
  if ooo0O0o00O == '123' :
   ooo0O0o00O = iiiiiIIii + 'appstreams.png'
  if 'php' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100010 , iI , ooo0O0o00O , i11II1I11I1 )
  elif 'playlist' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100007 , iI , ooo0O0o00O , i11II1I11I1 )
  elif 'watchseries' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100100 , iI , ooo0O0o00O , i11II1I11I1 )
  elif not 'http' in url :
   Ooo00OoOOO ( iiIiii1IIIII , url , 100009 , iI , ooo0O0o00O , i11II1I11I1 , '' )
  else :
   Ooo00OoOOO ( iiIiii1IIIII , url , 100005 , iI , ooo0O0o00O , i11II1I11I1 , '' )
   if 42 - 42: ii + I1ii11iIi11i % IIiIiII11i + oO0o
def I11i11I1iiII ( url ) :
 oO0000OOo00 = i1oO ( url )
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
   if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
def OoOO ( url ) :
 if 32 - 32: OOooOOo * oOo0O0Ooo % oOOoOooOo * Ii1i1i . o0o00Oo0O
 oO0000OOo00 = i1oO ( url )
 i11i1i1I1iI1 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Ii1II1I11i1 in i11i1i1I1iI1 :
  iI = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iI in iI :
   iI = iI
  iiIiii1IIIII = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iiIiii1IIIII in iiIiii1IIIII :
   if 'elete' in iiIiii1IIIII :
    pass
   elif 'rivate Vid' in iiIiii1IIIII :
    pass
   else :
    iiIiii1IIIII = ( iiIiii1IIIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  O0ooOo0 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( Ii1II1I11i1 ) )
  for O0ooOo0 in O0ooOo0 :
   O0ooOo0 = O0ooOo0
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for url in url :
   url = url
  Ooo00OoOOO ( '[COLORred]' + str ( O0ooOo0 ) + '[/COLOR] : ' + str ( iiIiii1IIIII ) , str ( url ) , 100009 , str ( iI ) , iIi1ii1I1 , '' , '' )
  OOoOO0o0o0 ( 'movies' , '' )
  if 53 - 53: ii - o0O00o
def oOo ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search Dans Scrapes' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'http://www.tvmaze.com/search?q=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 OoO00oo00 = i1iIIIiiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( OoO00oo00 )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  Oo0Oo0O = 'http://www.tvmaze.com' + Oo0o00OO0000 . replace ( '"' , '' )
  iiiI1i11Ii = requests . get ( Oo0Oo0O ) . content
  Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiiI1i11Ii )
  for i11II1I11I1 in Ii1i1iI1iIIi :
   if not '<div>' in i11II1I11I1 :
    iIiII = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   iII11 = 'http:' + iII11
   iiIiii1IIIII = iiIiii1IIIII . replace ( '&#039;' , '' )
   if iiIiii1IIIII == '' :
    i1i1IIIIIIIi = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( Oo0o00OO0000 ) )
    for iiIiii1IIIII in i1i1IIIIIIIi :
     iiIiii1IIIII = iiIiii1IIIII . replace ( '-' , ' ' )
  Iii ( iiIiii1IIIII , Oo0Oo0O , 9110002 , iII11 , iIi1ii1I1 , iIiII , '' )
  if 65 - 65: I11i
def iiI1iIIiI ( url ) :
 I111I11I111 ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 9110004 , iiiiiIIii + 'Search.png' , iIi1ii1I1 , '' )
 O0o0O0 = requests . get ( url ) . content
 Ii1i1iI1iIIi = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( O0o0O0 )
 i1ii1II1ii = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  Oo0Oo0O = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  if 7 - 7: o0O00o . OOooOOo / Ii1I . IIIi11I1 * iIII - IIiIiII11i
  iiiI1i11Ii = requests . get ( Oo0Oo0O ) . content
  Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiiI1i11Ii )
  for i11II1I11I1 in Ii1i1iI1iIIi :
   if not '<div>' in i11II1I11I1 :
    iIiII = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   iII11 = 'http:' + iII11
   iiIiii1IIIII = iiIiii1IIIII . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if iiIiii1IIIII == '' :
    i1i1IIIIIIIi = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for iiIiii1IIIII in i1i1IIIIIIIi :
     iiIiii1IIIII = iiIiii1IIIII . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  Iii ( iiIiii1IIIII , Oo0Oo0O , 9110002 , iII11 , iIi1ii1I1 , iIiII , '' )
  if 37 - 37: o0O0Oooo0O . OOooOOo / o0o00Oo0O * IIIIiiII111
 for o0o0oOoOO0O in i1ii1II1ii :
  url = 'http://www.tvmaze.com' + o0o0oOoOO0O
  Iii ( 'NEXT' , url , 9110001 , iII11 , iIi1ii1I1 , '' , '' )
def III11iiii11i1 ( url ) :
 O0o0O0 = requests . get ( url ) . content
 Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( O0o0O0 )
 for i11II1I11I1 in Ii1i1iI1iIIi :
  iIiII = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
 return iIiII
def ooOo0OoO ( url , name , iconimage ) :
 oOO0ooIiIIi1I1I11Ii = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 iII11 = iconimage
 O0o0O0 = requests . get ( url + '/episodes' ) . content
 iiiI1i11Ii = requests . get ( url ) . content
 Ii1II1I11i1 = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( iiiI1i11Ii )
 for i1iiIIi1I in Ii1i1iI1iIIi :
  i1iiIIi1I = i1iiIIi1I . replace ( ' ' , '' )
 for iiI1I1IIi11i1 , ii1III11 in Ii1II1I11i1 :
  if not 'special' in iiI1I1IIi11i1 . lower ( ) :
   iiI1I1IIi11i1 = iiI1I1IIi11i1 . replace ( 'S' , '' ) . replace ( 's' , '' )
  i1II1iii1i = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( ii1III11 ) )
  for OOO0o , iII , II1 in i1II1iii1i :
   if not 'special' in OOO0o . lower ( ) :
    Iii ( oOO0ooIiIIi1I1I11Ii + ' - SEASON -' + iiI1I1IIi11i1 + '- EPISODE-' + OOO0o + '-' + i1iiIIi1I , '' , 9110003 , iII11 , iIi1ii1I1 , '' , oOO0ooIiIIi1I1I11Ii )
    if 74 - 74: ii % IIIi11I1 % o0O0Oooo0O - oOo0O0Ooo - iIII
    if 58 - 58: o0o00Oo0O
    if 78 - 78: oO0o % o0O00o * ooOoO0O00
def O0iI ( name , extra ) :
 if 15 - 15: o0o00Oo0O / I1ii11iIi11i % Ii1I + I11i
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Checking for stream' )
 from imports import Scrape_Nan
 iiiIiI = name + '<>'
 IiiIIIiI1ii = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( iiiIiI ) )
 for oOO0ooIiIIi1I1I11Ii , oo0OOoOoo0O0O , iiI11ii1111 , i1iiIIi1I in IiiIIIiI1ii :
  oOO0ooIiIIi1I1I11Ii = oOO0ooIiIIi1I1I11Ii
  oo0OOoOoo0O0O = oo0OOoOoo0O0O
  iiI11ii1111 = iiI11ii1111
  IIi = ''
  Scrape_Nan . scrape_episode ( oOO0ooIiIIi1I1I11Ii , i1iiIIi1I , '' , oo0OOoOoo0O0O , iiI11ii1111 , '' )
if 21 - 21: I11i / OOooOOo / iI11I1II1I1I % IIIi11I1
if 2 - 2: Ii - IIiIiII11i / ooOO0O0ooOooO % o0o00Oo0O
if 66 - 66: I1ii11iIi11i
if 28 - 28: o0O00o - o0O00o . ooOoO0O00 - oOOoOooOo + oOo0O0Ooo . o0O00o
if 54 - 54: OOooOOo - o0O0Oooo0O
if 3 - 3: oOo0O0Ooo - I1ii11iIi11i
if 16 - 16: ooOO0O0ooOooO + oOOoOooOo / I11i
if 82 - 82: o0O00o * Ii % IIiIiII11i - ii
if 90 - 90: I1ii11iIi11i . ooOO0O0ooOooO * ooOoO0O00 - ooOoO0O00
if 16 - 16: oOo0O0Ooo * ooOoO0O00 - I11i . o0O00o % iIII / I11i
if 14 - 14: iI11I1II1I1I * o0O0Oooo0O * Ii1I / iI11I1II1I1I * o0O00o / iIII
def OOO000 ( ) :
 Iii ( 'Featured 24/7' , '' , 9070000 , iiiiiIIii + 'arconai/feat.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Tv Thows' , '' , 9080000 , iiiiiIIii + 'arconai/247shows.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Movies' , '' , 9090000 , iiiiiIIii + 'arconai/247movies.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Cable' , '' , 9100000 , iiiiiIIii + 'arconai/247cable.png' , iIi1ii1I1 , '' , '' )
 Iii ( '24/7 Random Stream' , '' , 9110000 , iiiiiIIii + 'arconai/random.png' , iIi1ii1I1 , '' , '' )
 if 28 - 28: ii . ooOO0O0ooOooO % Ii1I / ooOoO0O00 / IIIi11I1
def III1I1I ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 i1i111i1 = 'index.php#shows'
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + i1i111i1 ) . content )
 OoOoOo0 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for i1II11II1 in OoOoOo0 :
  II1IIIii = i1II11II1 . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I1I1IiI1 in II1IIIii :
   iIIIiIi1I1i = I1I1IiI1 . text
  OoOOoO0oOo = i1II11II1 . findAll ( 'a' )
  for I1I1IiI1 in OoOOoO0oOo :
   if I1I1IiI1 . has_key ( 'href' ) :
    O0ooOOOO0O0 = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   i1IIi1i1Ii1 = { 'User-Agent' : random_agent ( ) }
   Iiio0Oo0oO = requests . get ( O0ooOOOO0O0 , headers = i1IIi1i1Ii1 ) . content
   iIII1iiIi11 = packets ( Iiio0Oo0oO )
   if 84 - 84: Ii * oO0o
   Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
   for I1I1iII1i in Ii1i1iI1iIIi :
    I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ooo00OoOOO ( iiIiii1IIIII , iiIIii , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
    if 70 - 70: I11i - IIIi11I1
    if 62 - 62: iIII
def O000oOo ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 i1i111i1 = 'index.php#movies'
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + i1i111i1 ) . content )
 OoOoOo0 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for i1II11II1 in OoOoOo0 :
  II1IIIii = i1II11II1 . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I1I1IiI1 in II1IIIii :
   iIIIiIi1I1i = I1I1IiI1 . text
  OoOOoO0oOo = i1II11II1 . findAll ( 'a' )
  for I1I1IiI1 in OoOOoO0oOo :
   if I1I1IiI1 . has_key ( 'href' ) :
    O0ooOOOO0O0 = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   i1IIi1i1Ii1 = { 'User-Agent' : random_agent ( ) }
   Iiio0Oo0oO = requests . get ( O0ooOOOO0O0 , headers = i1IIi1i1Ii1 ) . content
   iIII1iiIi11 = packets ( Iiio0Oo0oO )
   if 53 - 53: iI11I1II1I1I + I11i - OOooOOo - ooOO0O0ooOooO / oOOoOooOo % Ii
   Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
   for I1I1iII1i in Ii1i1iI1iIIi :
    I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ooo00OoOOO ( iiIiii1IIIII , iiIIii , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
    if 3 - 3: IIIIiiII111 . oOOoOooOo % oOo0O0Ooo + Ii1I
    if 64 - 64: ooOoO0O00
def IIii1 ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 i1i111i1 = 'index.php#cable'
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + i1i111i1 ) . content )
 OoOoOo0 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for i1II11II1 in OoOoOo0 :
  II1IIIii = i1II11II1 . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I1I1IiI1 in II1IIIii :
   iIIIiIi1I1i = I1I1IiI1 . text
  OoOOoO0oOo = i1II11II1 . findAll ( 'a' )
  for I1I1IiI1 in OoOOoO0oOo :
   if I1I1IiI1 . has_key ( 'href' ) :
    O0ooOOOO0O0 = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   i1IIi1i1Ii1 = { 'User-Agent' : random_agent ( ) }
   Iiio0Oo0oO = requests . get ( O0ooOOOO0O0 , headers = i1IIi1i1Ii1 ) . content
   iIII1iiIi11 = packets ( Iiio0Oo0oO )
   if 35 - 35: Ii - oOo0O0Ooo / IIIi11I1 + Ii1i1i * ooOO0O0ooOooO
   Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
   for I1I1iII1i in Ii1i1iI1iIIi :
    I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    Ooo00OoOOO ( iiIiii1IIIII , iiIIii , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
    if 49 - 49: I11i * Ii1i1i + iIII + IIIIiiII111
def IIi11 ( ) :
 iiiI1i11Ii = 'http://arconaitv.me/stream.php?id=random'
 i1IIi1i1Ii1 = { 'User-Agent' : random_agent ( ) }
 Iiio0Oo0oO = requests . get ( iiiI1i11Ii , headers = i1IIi1i1Ii1 ) . content
 iIII1iiIi11 = packets ( Iiio0Oo0oO )
 if 89 - 89: IIiIiII11i * oOOoOooOo . ooOO0O0ooOooO
 Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
 for I1I1iII1i in Ii1i1iI1iIIi :
  I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  Ooo00OoOOO ( 'Random Pick' , iiIIii , 9060000 , iiiiiIIii + '247Streams.png' , iIi1ii1I1 , '' , '' )
  if 85 - 85: Ii1I + Ii1i1i * oOo0O0Ooo % Ii
def iI1i ( ) :
 Oo0o00OO0000 = 'http://arconaitv.me/'
 i1i111i1 = 'index.php#shows'
 if 31 - 31: Ii1i1i
 O0o0O0 = BeautifulSoup ( requests . get ( Oo0o00OO0000 + i1i111i1 ) . content )
 OoOoOo0 = O0o0O0 . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for i1II11II1 in OoOoOo0 :
  II1IIIii = i1II11II1 . findAll ( 'a' )
  for I1I1IiI1 in II1IIIii :
   if I1I1IiI1 . has_key ( 'href' ) :
    O0ooOOOO0O0 = Oo0o00OO0000 + I1I1IiI1 [ 'href' ]
   if I1I1IiI1 . has_key ( 'title' ) :
    iiIiii1IIIII = I1I1IiI1 [ 'title' ]
   OoOOo00 = I1I1IiI1 . findAll ( 'img' )
   for O00 in OoOOo00 :
    iII11 = Oo0o00OO0000 + O00 [ 'src' ]
    i1IIi1i1Ii1 = { 'User-Agent' : random_agent ( ) }
    Iiio0Oo0oO = requests . get ( O0ooOOOO0O0 , headers = i1IIi1i1Ii1 ) . content
    iIII1iiIi11 = packets ( Iiio0Oo0oO )
    if 94 - 94: iIII . iIII + Ii - IIIi11I1 * Ii1I
    Ii1i1iI1iIIi = re . compile ( "'https:(.+?)'" ) . findall ( iIII1iiIi11 )
    for I1I1iII1i in Ii1i1iI1iIIi :
     I1I1iII1i = I1I1iII1i . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     iiIIii = 'https:' + I1I1iII1i + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     Ooo00OoOOO ( iiIiii1IIIII , iiIIii , 9060000 , iII11 , iII11 , '' , '' )
     if 9 - 9: I11i . oOo0O0Ooo - Ii1I
def IiiiI ( name , url ) :
 import urlresolver
 try :
  iiIIi = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiIIi , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 36 - 36: iIII . IIiIiII11i
 if 25 - 25: ooOO0O0ooOooO
def iI1iiII11I ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 O0oO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
 for url , iII11 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in O0oO0 :
  if '.php' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 100210 , iII11 , ooo0O0o00O , i11II1I11I1 )
  else :
   oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , ooo0O0o00O , i11II1I11I1 )
   if 32 - 32: IIIi11I1 % oOOoOooOo - OOooOOo % IIIIiiII111 . o0O0Oooo0O
   if 47 - 47: iIII % ooOoO0O00 + ooOoO0O00
   if 87 - 87: I1ii11iIi11i * IIIi11I1 % o0O00o % OOooOOo
def iIi1Ii ( iconimage , url , extra ) :
 iI = ' '
 IiI1IIIII1I = ' '
 ooo0O0o00O = ' '
 oo0OOoOoo0O0O = ' '
 I1I1IiIi1 = i1oO ( url )
 iI = re . compile ( '<img src="(.+?)">' ) . findall ( I1I1IiIi1 )
 for iI in iI :
  iI = iI
 oOO0o0oo0 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( I1I1IiIi1 )
 for ooo0O0o00O in oOO0o0oo0 :
  ooo0O0o00O = ooo0O0o00O
 Ii1i1iI1iIIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( I1I1IiIi1 )
 for url , oo0OOoOoo0O0O in Ii1i1iI1iIIi :
  oo0OOoOoo0O0O = 'S' + ( oo0OOoOoo0O0O ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = Ii1iIiII1ii1 + url
  Iii ( ( oo0OOoOoo0O0O ) . replace ( '  ' , '' ) , url , 100101 , iI , ooo0O0o00O , IiI1IIIII1I , '' )
  OOoOO0o0o0 ( 'Movies' , 'info' )
  if 78 - 78: IIIi11I1 + IIIIiiII111 . o0O00o
def OoIIi1iI ( url , name , fanart , extra , iconimage ) :
 oO0Ooo0OooOOo = extra
 oo0OOoOoo0O0O = name
 I1I1IiIi1 = i1oO ( url )
 iI = iconimage
 Ii1i1iI1iIIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( I1I1IiIi1 )
 for url , name , O00o0O in Ii1i1iI1iIIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = Ii1iIiII1ii1 + url
  O00o0O = O00o0O
  iIIIiI = name + ' - [COLORred]' + O00o0O + '[/COLOR]'
  Iii ( iIIIiI , url , 100102 , iI , fanart , 'Aired : ' + O00o0O , iIIIiI )
  if 93 - 93: oOOoOooOo . iI11I1II1I1I % Ii . OOooOOo % oOOoOooOo + o0o00Oo0O
def o0OOoOO ( name , URL , iconimage , fanart ) :
 oO0000OOo00 = i1oO ( URL )
 Ii1i1iI1iIIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , name in Ii1i1iI1iIIi :
  for IIi1IIIi in ooOooo000oOO :
   if IIi1IIIi in Oo0o00OO0000 :
    URL = 'http://www.watchseriesgo.to/link/' + Oo0o00OO0000
    Ooo00OoOOO ( name , URL , 100106 , iiiiiIIii + 'appstreams.png' , iIi1ii1I1 , '' , '' )
 if len ( Ii1i1iI1iIIi ) <= 0 :
  Iii ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 46 - 46: ooOO0O0ooOooO / IIIIiiII111 - ooOoO0O00
  if 51 - 51: I1ii11iIi11i - Ii1I * iIII
def ii1111Ii1i ( url , name ) :
 IiI1iiI1III1I = name
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0000OOo00 )
 II1iIi1IiIii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  Oo000 ( url , IiI1iiI1III1I )
 for url in I1Ii :
  Oo000 ( url , IiI1iiI1III1I )
 for url in II1iIi1IiIii :
  Oo000 ( url , IiI1iiI1III1I )
  if 57 - 57: OOooOOo
def Oo000 ( url , season_name ) :
 if 'daclips.in' in url :
  i1IiiI1iii1ii ( url , season_name )
 elif 'filehoot.com' in url :
  II1I11Iii1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  i1iIIi1II1iiI ( url , season_name )
 elif 'vidspot.net' in url :
  III1Ii1i1I1 ( url , season_name )
 elif 'vodlocker' in url :
  O0O00OooO ( url , season_name )
 elif 'vidto' in url :
  I1IiI1iI11 ( url , season_name )
  if 2 - 2: iI11I1II1I1I
  if 45 - 45: ii / Ii
def I1IiI1iI11 ( url , season_name ) :
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
  I11I1i1iI ( oOoooooOoO , season_name )
  if 90 - 90: o0O00o * IIiIiII11i % o0O0Oooo0O + ooOO0O0ooOooO
  if 93 - 93: o0O0Oooo0O + Ii1i1i
def i1iIIi1II1iiI ( url , season_name ) :
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
  I11I1i1iI ( oOoooooOoO , season_name )
  if 33 - 33: o0o00Oo0O
def III1Ii1i1I1 ( url , season_name ) :
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0000OOo00 )
 for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
  I11I1i1iI ( oOoooooOoO , season_name )
  if 78 - 78: o0o00Oo0O / IIiIiII11i * oO0o
def O0O00OooO ( url , season_name ) :
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO in Ii1i1iI1iIIi :
  I11I1i1iI ( oOoooooOoO , season_name )
  if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % o0O0Oooo0O - iI11I1II1I1I % o0o00Oo0O
def i1IiiI1iii1ii ( url , season_name ) :
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0000OOo00 )
 for oOoooooOoO in Ii1i1iI1iIIi :
  I11I1i1iI ( oOoooooOoO , season_name )
  if 58 - 58: o0O00o + iI11I1II1I1I
def II1I11Iii1 ( url , season_name ) :
 oO0000OOo00 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oOoooooOoO in Ii1i1iI1iIIi :
  I11I1i1iI ( oOoooooOoO , season_name )
  if 65 - 65: IIiIiII11i - o0O0Oooo0O % I11i - OOooOOo * IIIIiiII111 + Ii1i1i
def I11I1i1iI ( Link , season_name ) :
 if 'http:/' in Link :
  O0o0O0OO0o ( Link )
  if 54 - 54: OOooOOo . ooOO0O0ooOooO % Ii / ii + o0O00o % ooOO0O0ooOooO
  if 36 - 36: ooOO0O0ooOooO
def o0OOII1I1 ( url ) :
 oO0000OOo00 = OPEN_URL_1 ( url )
 iii11I11iI1 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0000OOo00 )
 for url in iii11I11iI1 :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 4 - 4: IIIi11I1
def Iii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = True )
 return iioO0o
 if 99 - 99: oOOoOooOo / iI11I1II1I1I - Ii1i1i * Ii1I % oOo0O0Ooo
 if 13 - 13: oO0o
def Ooo00OoOOO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0oo0O0 = [ ]
  O0oo0O0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  I1I1 . addContextMenuItems ( O0oo0O0 )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = False )
 return iioO0o
 if 2 - 2: ii . IIIi11I1 . o0O00o
def I1iIII1IiiI ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
def Ii1Iii11 ( url ) :
 o0oO = xbmc . Player ( i11i11 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : o0oO . play ( url ) . strip ( )
 except : pass
 if 18 - 18: iI11I1II1I1I + iIII * oOo0O0Ooo - IIIi11I1 / oOo0O0Ooo
def O0o0O0OO0o ( url ) :
 o0oO = xbmc . Player ( )
 import urlresolver
 try : o0oO . play ( url )
 except : pass
 if 78 - 78: iIII . o0O00o
def i1oO ( url ) :
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
  if 38 - 38: OOooOOo + o0O00o
  if 15 - 15: I1ii11iIi11i + iIII . oOOoOooOo - iI11I1II1I1I / o0o00Oo0O % iI11I1II1I1I
  if 86 - 86: oOo0O0Ooo / ooOO0O0ooOooO * Ii1i1i
def o00O0O ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']CARTOONS[/COLOR]' ]
  if 64 - 64: oOOoOooOo / o0o00Oo0O * OOooOOo * oOOoOooOo
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Kids[/COLOR]' , I11ii1IIiIi )
  if 60 - 60: iIII / ooOoO0O00 % Ii1I / Ii1I * Ii1I . Ii
  if 99 - 99: OOooOOo
  if 77 - 77: I11i
  if 48 - 48: OOooOOo % Ii1I / iIII . iI11I1II1I1I * IIiIiII11i
  if OoOOo0OOoO == 0 :
   oo000oO ( )
   if 78 - 78: Ii1i1i + OOooOOo + o0O00o - o0O00o . Ii / oO0o
   if 27 - 27: Ii1i1i - o0o00Oo0O % iIII * o0O0Oooo0O . o0O00o % iI11I1II1I1I
   if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % oOOoOooOo
   if 24 - 24: OOooOOo
 else :
  if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + IIIi11I1
  if 28 - 28: oOo0O0Ooo
  if 49 - 49: iIII . I11i % ooOO0O0ooOooO / Ii1i1i
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CARTOONS[/COLOR]' , '' , 10001 , iiiiiIIii + 'Cartoons.png' , iIi1ii1I1 , '' )
   if 95 - 95: o0o00Oo0O * OOooOOo * o0O00o . oOOoOooOo / iI11I1II1I1I
   if 28 - 28: o0O00o + ooOO0O0ooOooO - oOOoOooOo / iI11I1II1I1I - oOo0O0Ooo
   if 45 - 45: o0o00Oo0O / ooOoO0O00 * ooOO0O0ooOooO * oO0o
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def O00o00O ( ) :
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
 if 35 - 35: Ii1I / IIIIiiII111 % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / oOOoOooOo
 if 77 - 77: I1ii11iIi11i
def I1i1Iiiii ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 Ii1i1iI1iIIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0000OOo00 )
 for o0OOOO00O0Oo in Ii1i1iI1iIIi :
  o0OOOO00O0Oo = ( str ( o0OOOO00O0Oo ) )
  if os . path . exists ( xbmc . translatePath ( o0OOOO00O0Oo ) ) :
   i1i111Iiiiiii = ( o0OOOO00O0Oo ) . replace ( 'special://home/addons/' , '' )
   I1iI1ii1II ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1i111Iiiiiii + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   OoOOo0OOoO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if OoOOo0OOoO == 0 :
    Iiiii1IIiI ( o0OOOO00O0Oo )
    OoOOoooOO0O ( )
   elif OoOOo0OOoO == 1 :
    i1i1Ii11Ii ( o0OOOO00O0Oo )
  else :
   pass
   if 57 - 57: IIIi11I1 + o0O0Oooo0O % Ii1I . oO0o / oO0o * o0o00Oo0O
def i1i1Ii11Ii ( addon ) :
 i1i111Iiiiiii = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 6 - 6: ooOoO0O00 - IIiIiII11i * I11i . oO0o
def Iiiii1IIiI ( addon ) :
 O0OoO000O0OO . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oooO00Oo = os . path . join ( oOoOooOo0o0 , 'default.py' )
 ooO00o = open ( oooO00Oo , "w+" )
 if 73 - 73: IIIIiiII111 * IIIIiiII111 / oOOoOooOo
 ooO00o . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 ooO00o . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 ooO00o . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 43 - 43: Ii1I . ooOoO0O00 . o0O00o + o0o00Oo0O * Ii1i1i * o0o00Oo0O
 if 41 - 41: Ii1I + Ii1i1i % ii . Ii1I + IIIIiiII111 . IIIIiiII111
 if 31 - 31: Ii + IIiIiII11i . IIIIiiII111 * OOooOOo
 if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
def O0oOO0o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 iiiiI1IiI1I1 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1i1iI1iIIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1iiIIIi11 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 II1iIi1IiIii = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 iI111i11iI1 = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 III1ii = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url , iI1III1iIi11 , ooo0O0o00O , i11II1I11I1 in iiiiI1IiI1I1 :
  if 'php' in url :
   OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iI1III1iIi11 , ooo0O0o00O , i11II1I11I1 )
  elif iiIiii1IIIII == 'Search' :
   OoOOoOooooOOo ( 'Search' , url , 90038 , iI1III1iIi11 , ooo0O0o00O , i11II1I11I1 )
  else :
   oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iI1III1iIi11 , ooo0O0o00O , i11II1I11I1 )
 for iiIiii1IIIII , iII11 , url , i11I1I in I1iiIIIi11 :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iII11 , i11I1I , '' )
 for iiIiii1IIIII , iII11 , url , i11I1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iII11 , i11I1I , '' )
 for iiIiii1IIIII , url , iII11 , i11I1I in I1Ii :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , i11I1I , '' )
 for iiIiii1IIIII , url , iII11 , i11I1I in II1iIi1IiIii :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , i11I1I , '' )
 for iiIiii1IIIII , url , iII11 , i11I1I in iI111i11iI1 :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , i11I1I , '' )
 for iiIiii1IIIII , url , iII11 in III1ii :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , '' , '' )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
def oo0ooooo00o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , iII11 , url , i11I1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 90037 , iII11 , i11I1I , '' )
 for iiIiii1IIIII , url , iII11 , i11I1I in I1Ii :
  oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , iII11 , i11I1I , '' )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
  if 78 - 78: iI11I1II1I1I . I11i % iI11I1II1I1I . o0o00Oo0O / IIIi11I1
def Oo0oOo000OoO0 ( ) :
 IIii1I1i = [ 'serialsearch' , 'moviesearch' ]
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 if OoO00oo00 == '' :
  pass
 else :
  for IIII1iIIii in IIii1I1i :
   IiiOooooOo0 = Oo0o0000o0o0 + IIII1iIIii + '.php'
   I1I1IiIi1 = i11oO0oOo0 ( IiiOooooOo0 )
   if I1I1IiIi1 != 'Opened' :
    O0oO0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( I1I1IiIi1 )
    for iiIiii1IIIII , Oo0o00OO0000 , iI1III1iIi11 , ooo0O0o00O , i11II1I11I1 in O0oO0 :
     if OoO00oo00 in iiIiii1IIIII . lower ( ) :
      I1ii1 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
      for IIi1IIIi in I1ii1 :
       if IIi1IIIi == Oo0o00OO0000 :
        iiIiii1IIIII = '[COLORred]* [/COLOR]' + ( iiIiii1IIIII ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        I1IiIiI = open ( Oo0oOOo , "a" )
        I1IiIiI . write ( 'item="' + iiIiii1IIIII + '"\n' )
        I1IiIiI . close
      if 'php' in Oo0o00OO0000 :
       OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , 90037 , iI1III1iIi11 , ooo0O0o00O , i11II1I11I1 )
      else :
       oOOOoo0O0oO ( iiIiii1IIIII , Oo0o00OO0000 , 222 , iI1III1iIi11 , ooo0O0o00O , i11II1I11I1 )
       if 60 - 60: o0O0Oooo0O
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
   if 98 - 98: oOOoOooOo
def Ii11i1Ii1IIII ( ) :
 if 41 - 41: Ii1i1i / IIiIiII11i . OOooOOo
 if 63 - 63: o0o00Oo0O
 if 6 - 6: IIIi11I1
 if 98 - 98: ii % o0o00Oo0O - o0o00Oo0O
 if 76 - 76: ooOoO0O00 % OOooOOo - oOo0O0Ooo / I11i * oOOoOooOo
 if 4 - 4: I1ii11iIi11i * I1ii11iIi11i / OOooOOo
 if 4 - 4: oOo0O0Ooo * OOooOOo % iIII . OOooOOo
 if 11 - 11: IIIi11I1 - OOooOOo - I11i * OOooOOo + oOOoOooOo
 if 62 - 62: oOo0O0Ooo * Ii . IIIIiiII111
 if 35 - 35: o0O00o . o0o00Oo0O + I1ii11iIi11i + IIIi11I1 + ooOoO0O00
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
 if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
 if 58 - 58: IIIi11I1 . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
 if 50 - 50: IIIIiiII111 % IIiIiII11i - oOOoOooOo . ooOoO0O00 + o0o00Oo0O % IIIIiiII111
 if 10 - 10: IIIIiiII111 . ooOoO0O00 + Ii1i1i
 if 66 - 66: oO0o % I11i
 if 21 - 21: OOooOOo - ii % Ii
 if 71 - 71: ooOoO0O00 - iIII * o0O0Oooo0O + ooOO0O0ooOooO - oO0o % Ii1I
 if 63 - 63: iI11I1II1I1I + IIIi11I1 . oO0o / oOo0O0Ooo
 if 84 - 84: ooOoO0O00
 if 42 - 42: IIiIiII11i - oO0o - ii . IIIIiiII111 / OOooOOo
 O0o0O0 = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 iiiI1i11Ii = requests . get ( 'http://www.djing.com/' ) . content
 I1Ii = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( iiiI1i11Ii )
 OoOoOo0 = O0o0O0 . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for i1II11II1 in OoOoOo0 :
  II1IIIii = i1II11II1 . findAll ( 'a' )
  for I1I1IiI1 in II1IIIii :
   if I1I1IiI1 . has_attr ( 'href' ) :
    O0ooOOOO0O0 = 'https://tvcatchup.com' + I1I1IiI1 [ 'href' ]
   OoOOo00 = I1I1IiI1 . findAll ( 'img' )
   for O00 in OoOOo00 :
    iII11 = O00 [ 'src' ]
    ooooo0Oo0 = O00 [ 'alt' ]
   Ii1i1iI1iIIi = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( I1I1IiI1 ) )
   for o0I1IIIi11ii11 in Ii1i1iI1iIIi :
    iiiiI11ii ( ( '[COLORgold]' + ooooo0Oo0 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + o0I1IIIi11ii11 + '[/COLOR]' ) , O0ooOOOO0O0 , 90024 , iII11 )
    if 53 - 53: o0O0Oooo0O * o0O00o / iI11I1II1I1I / oOo0O0Ooo % Ii1I
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in I1Ii :
  if 'Submit' in iiIiii1IIIII :
   pass
  elif '&lt;' in iiIiii1IIIII :
   pass
  else :
   oOOOoo0O0oO ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 90025 , 'http://www.djing.com' + iII11 , iIi1ii1I1 , '' )
   if 39 - 39: oO0o / ii . oO0o * Ii1I / OOooOOo
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def II111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 if 94 - 94: IIIIiiII111 % oOOoOooOo . ooOO0O0ooOooO
 Ii1i1iI1iIIi = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( html )
 for O00oOo0O0o00O in Ii1i1iI1iIIi :
  if not 'text' in O00oOo0O0o00O :
   ooo0oo00O00Oo = i11 ( i11 ( O00oOo0O0o00O ) )
   O0i1iI ( ooo0oo00O00Oo )
def OOO000000OOO0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  ooOoOOoooO000 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 85 - 85: oOo0O0Ooo % iIII + IIIi11I1 / Ii1i1i % ii
def i11i11II11i1 ( ) :
 oO0000OOo00 = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 iiiI1i1 = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for I1i1i11 , i1I , oOOoooO0O0 in iiiI1i1 :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + I1i1i11 + i1I + oOOoooO0O0 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + Oo0o00OO0000 , 10201 , iiiiiIIii + 'rated.png' )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'yr' in Oo0o00OO0000 :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + Oo0o00OO0000 , 10201 , iiiiiIIii + 'rated.png' )
   if 46 - 46: iI11I1II1I1I
def IIiiii ( ) :
 if 33 - 33: iIII % iIII % o0o00Oo0O / oOo0O0Ooo . ooOoO0O00
 if 91 - 91: oOOoOooOo * iIII - IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + oOOoOooOo
 if 56 - 56: I11i / o0O00o * oOo0O0Ooo . I11i
 if 15 - 15: Ii
 if 13 - 13: iIII * IIiIiII11i * ooOO0O0ooOooO * IIiIiII11i % o0O00o / oOo0O0Ooo
 if 100 - 100: o0O00o . Ii1i1i - iI11I1II1I1I . Ii / IIiIiII11i
 oO0000OOo00 = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'yr' in Oo0o00OO0000 :
   Iii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + Oo0o00OO0000 , 10201 , iiiiiIIii + 'rated.png' , '' , iiIiii1IIIII , '' )
   if 71 - 71: o0O0Oooo0O * I1ii11iIi11i . iIII
def i1ii1iiIi1II ( name , url , description ) :
 iIiII = description
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0000OOo00 )
 for OOo000o0 , url , name in Ii1i1iI1iIIi :
  if 'id' in url :
   o00oo0OO0 = name
   Iii ( ( '[COLORred]RANK [COLORblue]' + OOo000o0 + '[COLORred] - [COLORblue]' + name + '[/COLOR]' ) , name , 9110005 , iiiiiIIii + 'rated.png' , '' , iIiII , o00oo0OO0 )
   if 60 - 60: oOOoOooOo
   if 66 - 66: iIII / oOOoOooOo % ooOoO0O00 - ooOO0O0ooOooO . o0o00Oo0O / o0o00Oo0O
def oo00o0I1IiI ( description , url ) :
 if 44 - 44: IIIi11I1 / IIIi11I1 . I11i % o0O00o + OOooOOo
 o0Ooo0O00 = ( str ( description ) )
 oOO0ooIiIIi1I1I11Ii = ( str ( url ) )
 xbmc . log ( 'title:' + oOO0ooIiIIi1I1I11Ii + '# year:' + o0Ooo0O00 , xbmc . LOGNOTICE )
 from imports import Scrape_Nan
 Scrape_Nan . scrape_movie ( oOO0ooIiIIi1I1I11Ii , o0Ooo0O00 , '' )
 if 57 - 57: IIIIiiII111 % oO0o - oO0o
 if 5 - 5: ooOoO0O00 + ii % OOooOOo
 if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . o0O0Oooo0O
 if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
 if 67 - 67: IIiIiII11i / I11i . IIIi11I1 . ii
 if 19 - 19: o0O00o . Ii1I / OOooOOo
 if 68 - 68: oOOoOooOo / ii * iIII / ooOO0O0ooOooO
def ooooO000 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0O00Oooo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIIIIiII1 = ( url )
 OoO00oo00 = IIIIIiII1 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 i1iIIII1iiIIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1I1IiI1ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 O00OOoOOOO00O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Ooo0OOO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooooOoo0OO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIIIIiII1
 Oo0 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 O0000Oo00o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
 o00iIiiiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ii1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 71 - 71: OOooOOo + iI11I1II1I1I * ooOO0O0ooOooO . o0O0Oooo0O % Ii % iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0000OOo00 = O0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 iiIi1IIiIi = O0 ( Oo0Oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 oOO00Oo = O0 ( i1iIIII1iiIIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 i1iIIIi1i = O0 ( i1I1IiI1ii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OooOO0oOOo0O = O0 ( O00OOoOOOO00O )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 I1II = O0 ( ooooOoo0OO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 iIIi1Ii1III = O0 ( Oo0 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 Oooo00 = O0 ( O0000Oo00o )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 9 - 9: ii * o0o00Oo0O
 if 76 - 76: o0O0Oooo0O - ooOO0O0ooOooO . IIIi11I1 % I11i
 iIi11iiI11 = O0 ( o00iIiiiII )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 i1I111Ii = O0 ( Ii1I1 )
 if 31 - 31: oOo0O0Ooo
 if 73 - 73: oOOoOooOo . o0o00Oo0O / I11i - ii % Ii
 if 80 - 80: Ii1i1i / oOOoOooOo % o0o00Oo0O . I1ii11iIi11i
 if 63 - 63: IIIi11I1 . IIiIiII11i . iIII
 if 46 - 46: oOOoOooOo % o0O00o - I11i - I1ii11iIi11i - Ii1i1i / iIII
 if 68 - 68: ooOoO0O00 - Ii1I / I1ii11iIi11i % iIII . IIIIiiII111
 if 9 - 9: o0O00o
 if 48 - 48: I11i + I11i - I1ii11iIi11i
 if 27 - 27: oO0o + OOooOOo * oOOoOooOo
 if 83 - 83: iI11I1II1I1I
 if 72 - 72: iIII
 if 87 - 87: ooOoO0O00
 if 48 - 48: I1ii11iIi11i * ooOO0O0ooOooO * iI11I1II1I1I + Ii - ii
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for url , iiIiii1IIIII in II1iI :
   Ii1IiI1III11 = O0 ( url )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , O00O00OoO in I1IIII1i1 :
    O00O00OoO = ( O00O00OoO . replace ( '.' , ' ' ) )
    if OoO00oo00 in O00O00OoO . lower ( ) :
     if '.mkv' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     elif '.mp4' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     elif '.avi' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     elif '.wav' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']*' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + oOO0 , 222 , '' , '' , '' )
     else :
      OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']*' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + oOO0 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 20 - 20: o0o00Oo0O - ii - o0O00o + iI11I1II1I1I
      OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiIi1IIiIi )
  for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in I1Ii :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 94 - 94: Ii1i1i . ooOoO0O00
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 71 - 71: IIIIiiII111 + oO0o - o0O00o . oO0o . o0O00o + oOo0O0Ooo
 if oOO00Oo != 'Failed' :
  II1iIi1IiIii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOO00Oo )
  for iii , iiIiii1IIIII in II1iIi1IiIii :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1iIIII1iiIIi + iii ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if i1iIIIi1i != 'Failed' :
  iI111i11iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIIi1i )
  for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in iI111i11iI1 :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 26 - 26: oOo0O0Ooo
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if OooOO0oOOo0O != 'Failed' :
  iiiiIiIiI = [ ]
  III1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OooOO0oOOo0O )
  for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in III1ii :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    if iiIiii1IIIII in iiiiIiIiI :
     pass
    else :
     OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
     iiiiIiIiI . append ( iiIiii1IIIII )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if I1II != 'Failed' :
  o0OOooO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( I1II )
  for url , iII11 , iiIiii1IIIII in o0OOooO :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , iII11 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 41 - 41: ooOoO0O00 + IIiIiII11i * oOOoOooOo
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 68 - 68: Ii1i1i - oOo0O0Ooo
    if 41 - 41: ooOO0O0ooOooO
    if 21 - 21: oOOoOooOo + I11i % o0O0Oooo0O + Ii + IIIIiiII111 + IIiIiII11i
    if 98 - 98: o0O0Oooo0O
    if 49 - 49: I1ii11iIi11i * ooOO0O0ooOooO + I11i - Ii
    if 74 - 74: I1ii11iIi11i / iI11I1II1I1I . IIiIiII11i - oO0o
    if 62 - 62: IIIi11I1 / IIiIiII11i + OOooOOo % oOOoOooOo / OOooOOo + Ii1I
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
    if 9 - 9: iIII . oO0o * ooOoO0O00 . ii
 if iIi11iiI11 != 'Failed' :
  II1OoooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi11iiI11 )
  for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in II1OoooOo :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 34 - 34: Ii1i1i * Ii1i1i - Ii1I - o0o00Oo0O . Ii
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 32 - 32: iI11I1II1I1I . oO0o * ooOO0O0ooOooO / IIIi11I1 . IIiIiII11i - I1ii11iIi11i
    if 10 - 10: Ii1I / Ii - Ii1i1i + ooOO0O0ooOooO * oOo0O0Ooo
    if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
    if 64 - 64: iIII + oO0o
    if 25 - 25: oOo0O0Ooo . oOOoOooOo + oOo0O0Ooo % Ii1i1i * iI11I1II1I1I
    if 31 - 31: Ii + IIIi11I1 - o0o00Oo0O
    if 51 - 51: oO0o * ooOoO0O00 / Ii1i1i * IIIi11I1 + oOOoOooOo % Ii1I
    if 34 - 34: ooOO0O0ooOooO * ii + Ii1i1i + Ii
    if 22 - 22: ooOoO0O00
    if 24 - 24: iIII / oOo0O0Ooo * ooOoO0O00 % ii
 ooiI1i = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 3 - 3: o0O00o / iIII
 for IIII1iIIii in ooiI1i :
  IiiOooooOo0 = OOO00O + IIII1iIIii + I11iii1Ii
  Oooo00 = O0 ( IiiOooooOo0 )
  if Oooo00 != 'Failed' :
   II1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oooo00 )
   for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in II1iI :
    if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
     oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 34 - 34: Ii / o0O0Oooo0O * IIIi11I1 . I1ii11iIi11i
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 79 - 79: o0O0Oooo0O
 ooiI1i = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 31 - 31: IIIi11I1 % o0O0Oooo0O
 if 98 - 98: o0O00o * iI11I1II1I1I . Ii1i1i * I1ii11iIi11i / Ii1I + oOOoOooOo
 for IIII1iIIii in ooiI1i :
  IiiOooooOo0 = o0O00Oooo + IIII1iIIii
  iiI1ii111 = O0 ( IiiOooooOo0 )
  if iiI1ii111 != 'Failed' :
   OoOOIIIIIiI11Ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( iiI1ii111 )
   for iii , iiIiii1IIIII in OoOOIIIIIiI11Ii :
    if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
     iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0O00Oooo + IIII1iIIii + iii ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 41 - 41: Ii - ooOoO0O00 / I1ii11iIi11i * o0O00o / o0O0Oooo0O - I1ii11iIi11i
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: o0o00Oo0O
def oOO0OO0O ( ) :
 I111I11I111 ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiiiiIIii + 'running.png' )
 I111I11I111 ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiiiiIIii + 'countdown.png' )
 I111I11I111 ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiiiiIIii + 'unknown.png' )
 I111I11I111 ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiiiiIIii + 'cancelled.png' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 45 - 45: OOooOOo - oO0o - OOooOOo
def IIiiI ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , oo0OOoOoo0O0O , iII11iiiiiii , O00o0O , O0000 in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLORblue]' + iiIiii1IIIII + '[/COLOR] [COLORred]Season[/COLOR]-' + oo0OOoOoo0O0O + ' [COLORred]Returns [/COLOR]- ' + O0000 + ' ' + O00o0O ) , iiIiii1IIIII , 10099 , iiiiiIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 74 - 74: IIiIiII11i . Ii1i1i % oO0o + IIIi11I1 - I11i + Ii1i1i
def i1IIOO0oo00oOO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , oo0OOoOoo0O0O , iII11iiiiiii in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLORblue]' + iiIiii1IIIII + '[/COLOR] [COLORred]Season[/COLOR]-' + oo0OOoOoo0O0O + ' [COLORred] Status Unknown[/COLOR] ' ) , iiIiii1IIIII , 10099 , iiiiiIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 38 - 38: o0O0Oooo0O . IIIIiiII111 . oOo0O0Ooo * oO0o
def oOoo00o0oOO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , oo0OOoOoo0O0O , iII11iiiiiii , O00o0O in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLORblue]' + iiIiii1IIIII + ' [COLORred] Cancelled On[/COLOR] ' + O00o0O ) , iiIiii1IIIII , 10099 , iiiiiIIii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 61 - 61: ooOoO0O00 * I11i + iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
def oOoo0ooOoo ( url ) :
 IIIIIiII1 = ( url )
 OoO00oo00 = IIIIIiII1 . lower ( )
 if 52 - 52: oO0o * ii
 if 12 - 12: o0o00Oo0O + o0O00o * ooOoO0O00 . oO0o
 oOO0 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 Oo0Oo0O = 'http://onlinemovies.tube/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 i1iIIII1iiIIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1I1IiI1ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 Ooo0OOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 71 - 71: o0O0Oooo0O - I11i - IIIi11I1
 Oo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 O0000Oo00o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 iiIO0OO0o0O00oO = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 81 - 81: o0O00o / iIII
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 46 - 46: Ii1I / o0O0Oooo0O + o0O00o / ooOO0O0ooOooO / o0O0Oooo0O / IIIi11I1
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 73 - 73: oOOoOooOo + Ii1I
 if 100 - 100: iI11I1II1I1I
 ooOOo00 = O0 ( oOO0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 iiIi1IIiIi = O0 ( Oo0Oo0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 oOO00Oo = O0 ( i1iIIII1iiIIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 i1iIIIi1i = O0 ( i1I1IiI1ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 iiI1ii111 = O0 ( Ooo0OOO )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 39 - 39: I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * OOooOOo % o0o00Oo0O
 if 55 - 55: iI11I1II1I1I * IIIIiiII111
 iIIi1Ii1III = O0 ( Oo0 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 Oooo00 = O0 ( O0000Oo00o )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 ooIi11iI = O0 ( iiIO0OO0o0O00oO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 22 - 22: IIIi11I1
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for url , iiIiii1IIIII in II1iI :
   Ii1IiI1III11 = O0 ( url )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , O00O00OoO in I1IIII1i1 :
    if OoO00oo00 in O00O00OoO . lower ( ) :
     OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']*' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , url + oOO0 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 22 - 22: IIIIiiII111 * iIII - I1ii11iIi11i * o0o00Oo0O / Ii
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iIIi1Ii1III != 'Failed' :
  OOooO0Oo0o000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1Ii1III )
  for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in OOooO0Oo0o000 :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 17 - 17: iI11I1II1I1I + oOo0O0Ooo
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 57 - 57: I11i / o0O0Oooo0O
    if 13 - 13: ii + oO0o
    if 32 - 32: o0o00Oo0O + ooOO0O0ooOooO % I1ii11iIi11i
    if 7 - 7: Ii1I / oOOoOooOo
    if 11 - 11: o0O00o * oOOoOooOo / oOOoOooOo - IIIi11I1
    if 68 - 68: oOo0O0Ooo % o0O00o - o0O00o / oOo0O0Ooo + Ii1I - I1ii11iIi11i
    if 65 - 65: oOOoOooOo - ooOoO0O00
    if 62 - 62: iIII / ooOO0O0ooOooO % I1ii11iIi11i . ii / Ii / o0O0Oooo0O
    if 60 - 60: oOo0O0Ooo % ooOO0O0ooOooO / I11i % ooOO0O0ooOooO * Ii / IIIIiiII111
    if 34 - 34: o0O0Oooo0O - IIIi11I1
    if 25 - 25: ooOO0O0ooOooO % oOo0O0Ooo + Ii + o0o00Oo0O * ii
 if ooIi11iI != 'Failed' :
  ooO0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooIi11iI )
  for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in ooO0 :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , ii1IiIiI1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 94 - 94: iIII . oOo0O0Ooo
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  oooO = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  for url , iII11 , iiIiii1IIIII , oo0OoOO0000 in I1Ii :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    if 'season' in oo0OoOO0000 :
     I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , iII11 , iII11 , '' )
    if 'episodes' in oo0OoOO0000 :
     I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , iII11 , iII11 , '' )
  for url in oooO :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiiiiIIii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 2 - 2: Ii1i1i * Ii1I * ii
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if ooOOo00 != 'Failed' :
  I1iiIIIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( ooOOo00 )
  for url , iiIiii1IIIII , iII11 in I1iiIIIi11 :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( iiIiii1IIIII ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , iII11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 73 - 73: OOooOOo + I1ii11iIi11i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 61 - 61: iI11I1II1I1I
    if 47 - 47: ii
    if 2 - 2: OOooOOo % o0O0Oooo0O * I1ii11iIi11i * OOooOOo
    if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
    if 26 - 26: I11i % IIIi11I1 + IIIi11I1 % iIII * Ii / IIIIiiII111
    if 64 - 64: ooOO0O0ooOooO % OOooOOo / IIiIiII11i % oOOoOooOo - IIIIiiII111
    if 2 - 2: o0O0Oooo0O - Ii1I + I11i * oO0o / IIIIiiII111
    if 26 - 26: IIIi11I1 * I1ii11iIi11i
    if 31 - 31: iIII * ooOO0O0ooOooO . Ii1i1i
 if oOO00Oo != 'Failed' :
  II1iIi1IiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOO00Oo )
  for iiIiii1IIIII in II1iIi1IiIii :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( i1iIIII1iiIIi + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 35 - 35: iIII
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if i1iIIIi1i != 'Failed' :
  iI111i11iI1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1iIIIi1i )
  for iiIiii1IIIII in iI111i11iI1 :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1I1IiI1ii + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 94 - 94: oOOoOooOo / Ii % o0o00Oo0O
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiI1ii111 != 'Failed' :
  OoOOIIIIIiI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI1ii111 )
  for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in OoOOIIIIIiI11Ii :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 70 - 70: iIII - I1ii11iIi11i / ii % ii
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 95 - 95: ii % ii . Ii1i1i
 III1iiiII1ii = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IIII1iIIii in III1iiiII1ii :
  IiiOooooOo0 = OOO00O + IIII1iIIii + I11iii1Ii
  iIi11iiI11 = O0 ( IiiOooooOo0 )
  if iIi11iiI11 != 'Failed' :
   II1OoooOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIi11iiI11 )
   for iiIiii1IIIII , i11II1I11I1 , url , iII11 , ooo0O0o00O , o0OO in II1OoooOo :
    if OoO00oo00 in iiIiii1IIIII . lower ( ) :
     OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , url , o0OO , iII11 , ooo0O0o00O , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 76 - 76: Ii1I
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 99 - 99: I11i
     if 1 - 1: Ii1i1i * OOooOOo * oO0o + I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: o0O0Oooo0O % I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / IIIi11I1 + iIII
def o0o00OOOO ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']Adult Gallery[/COLOR]' , '[COLOR' + II11iiii1Ii + ']JizBox[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Adult Channels[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  i11iIi1iIIIIi ( )
 if OoOOo0OOoO == 1 :
  I1111iiiII1Ii ( )
 if OoOOo0OOoO == 2 :
  oO0oOoOoo0 ( )
  if 66 - 66: oO0o
  if 72 - 72: o0O0Oooo0O
  if 91 - 91: IIiIiII11i / o0O00o + iI11I1II1I1I . iIII - o0o00Oo0O
def i11iIi1iIIIIi ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']YOLOselfies[/COLOR]' , '[COLOR' + II11iiii1Ii + ']HotNudeGirls[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MyNudeBabes[/COLOR]' , '[COLOR' + II11iiii1Ii + ']TeenNudeGirls[/COLOR]' , '[COLOR' + II11iiii1Ii + ']ADULTmeme[/COLOR]' , '[COLOR' + II11iiii1Ii + ']GIRLSmeme[/COLOR]' , ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  O0OOO00OOO00o ( 'http://www.yoloselfie.com/' )
 if OoOOo0OOoO == 1 :
  i11o00Ooo ( 'http://www.hotnudegirls.net/#nudegirls' )
 if OoOOo0OOoO == 2 :
  OoO00OOoOOOo0 ( 'http://www.teennudegirls.com/' )
 if OoOOo0OOoO == 3 :
  OoO00OOoOOOo0 ( 'http://www.teennudegirls.com/' )
 if OoOOo0OOoO == 4 :
  oOoO00O ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if OoOOo0OOoO == 5 :
  oOoO00O ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 31 - 31: oOOoOooOo . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * IIIIiiII111
def O0OOO00OOO00o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 100111 , iII11 )
 for url in I1Ii :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 100110 , iII11 )
def I1i1iII1I11 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  o00OOo0o0O = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( o00OOo0o0O )
  sys . exit ( 1 )
def oOoO00O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + iII11 , 100113 , 'http:' + iII11 )
 for url in I1Ii :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , 'http:' + url , 100112 , iII11 )
def i11o00Ooo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , iII11 )
def I111Iii1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']Click To Enlarge[/COLOR]' , iII11 , 100113 , iII11 )
def i11i ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , iII11 )
def O0o0O00o0o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']Click To Enlarge[/COLOR]' , iII11 , 100113 , iII11 )
def OoO00OOoOOOo0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , iII11 )
def II1IIiiI1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']Click To Enlarge[/COLOR]' , iII11 , 100113 , iII11 )
def O00O00 ( url ) :
 o00OOo0o0O = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( o00OOo0o0O )
 sys . exit ( 1 )
 if 66 - 66: I1ii11iIi11i - iI11I1II1I1I
def iIiIIi11iI ( ) :
 if 65 - 65: o0o00Oo0O - o0O0Oooo0O . Ii1i1i
 if 19 - 19: Ii1I . IIIIiiII111 - I11i + iIII - Ii1i1i
 if 13 - 13: o0O00o * Ii1I / Ii1I / iI11I1II1I1I % iI11I1II1I1I
 if 21 - 21: Ii1I
 if 86 - 86: oOOoOooOo
 if 51 - 51: oO0o - Ii * oOo0O0Ooo
 if 95 - 95: IIIi11I1 % Ii1I + I11i % oOOoOooOo
 if 36 - 36: o0o00Oo0O / ooOoO0O00 % IIiIiII11i / IIIIiiII111
 if 96 - 96: I1ii11iIi11i / ooOO0O0ooOooO . IIiIiII11i . I1ii11iIi11i
 if 91 - 91: IIiIiII11i . IIIi11I1 + I11i
 if 8 - 8: IIIi11I1 * I1ii11iIi11i / IIIIiiII111 - oO0o - ii
 I111I11I111 ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiiiiIIii + 'seasons.png' )
 I111I11I111 ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiiiiIIii + 'episodes.png' )
 I111I11I111 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiiiiIIii + 'Search.png' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 100 - 100: ooOO0O0ooOooO . iI11I1II1I1I . iI11I1II1I1I
def oOOo0ooO0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , ii1i1II11II1i in Ii1i1iI1iIIi :
  I111I11I111 ( ( iiIiii1IIIII + ' - ' + ii1i1II11II1i ) . replace ( '&amp;' , '&' ) , url , 90053 , iiiiiIIii + 'seasons.png' )
  if 95 - 95: iIII + I11i * Ii1I
def ooO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , url , 90054 , iiiiiIIii + 'episodes.png' )
  if 16 - 16: I1ii11iIi11i
def o00oO0o00O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , url , 90054 , iII11 )
 for url in next :
  I111I11I111 ( 'NEXT' , url , 90053 , iiiiiIIii + 'Next.png' )
  if 28 - 28: o0O00o * oOo0O0Ooo % o0O00o
def ooo00 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0000OOo00 )
 for iII11 , ii1i1II11II1i , url , iiIiii1IIIII , iII11II1II in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ii1i1II11II1i + ' - ' + iiIiii1IIIII + ' - ' + iII11II1II , url , 90044 , iII11 , iII11 , '' )
 for iII11 , iiIiii1IIIII , url in I1Ii :
  I111I11I111 ( iiIiii1IIIII , url , 90044 , iII11 , iII11 , '' )
 for url in next :
  I111I11I111 ( 'NEXT' , url , 90053 , iiiiiIIii + 'Next.png' )
  if 100 - 100: oO0o % o0O0Oooo0O - iIII % iIII % iIII / oOOoOooOo
def OOO000Oo ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'http://onlinemovies.tube/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 OoO00oo00 = i1iIIIiiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( OoO00oo00 )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , oo0OoOO0000 in Ii1i1iI1iIIi :
  if 'season' in oo0OoOO0000 :
   I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 90054 , iII11 , iII11 , '' )
  if 'episodes' in oo0OoOO0000 :
   I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 90044 , iII11 , iII11 , '' )
 for Oo0o00OO0000 in next :
  I111I11I111 ( 'NEXT' , Oo0o00OO0000 , 90053 , iiiiiIIii + 'Next.png' )
  if 8 - 8: oOOoOooOo - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * Ii1i1i - iI11I1II1I1I
def i1Ii ( ) :
 if 31 - 31: IIIIiiII111 - OOooOOo . OOooOOo - ooOO0O0ooOooO + I1ii11iIi11i / Ii
 if 90 - 90: iI11I1II1I1I + OOooOOo
 if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
 if 30 - 30: IIIIiiII111 / oO0o . IIIIiiII111
 if 17 - 17: I1ii11iIi11i + ii * ii
 if 5 - 5: o0O0Oooo0O % ii . OOooOOo
 if 67 - 67: Ii1I + Ii1i1i
 if 72 - 72: o0O00o % I11i
 if 93 - 93: iI11I1II1I1I + Ii . I11i . ooOoO0O00 % oOo0O0Ooo % oOOoOooOo
 if 74 - 74: OOooOOo / ooOoO0O00 % ii
 I111I11I111 ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiiiiIIii + 'allmov.png' )
 I111I11I111 ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiiiiIIii + 'Genre.png' )
 I111I11I111 ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiiiiIIii + 'Years.png' )
 I111I11I111 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiiiiIIii + 'Search.png' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 52 - 52: o0O00o % oOOoOooOo
def I111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , ii1i1II11II1i in Ii1i1iI1iIIi :
  if 'genre' in url :
   I111I11I111 ( ( iiIiii1IIIII + ' - ' + ii1i1II11II1i ) . replace ( '&amp;' , '&' ) , url , 90043 , iiiiiIIii + 'Genre.png' )
   if 51 - 51: Ii1I * ooOO0O0ooOooO
def i1oooOoOoOO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'release' in url :
   I111I11I111 ( iiIiii1IIIII , url , 90043 , iiiiiIIii + 'Years.png' )
   if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
def iiI1ii1Iii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , Ii1I1IIIiI1i , url , i11II1I11I1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII + ' ' + Ii1I1IIIiI1i , url , 90044 , iII11 , iII11 , i11II1I11I1 )
 for iII11 , iiIiii1IIIII , oo0OoOO0000 , url , o0Oo00oOO , i11II1I11I1 in I1Ii :
  if 'movies' in oo0OoOO0000 :
   OoOOoOooooOOo ( iiIiii1IIIII + ' - ' + o0Oo00oOO , url , 90044 , iII11 , iII11 , i11II1I11I1 )
 for url in next :
  I111I11I111 ( 'NEXT' , url , 90043 , iiiiiIIii + 'Next.png' )
  if 73 - 73: iIII / ii . IIiIiII11i - o0O00o * oOOoOooOo * o0O00o
def IiI1IiI1iiI1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O000o0 ( 'http:' + url )
  if 39 - 39: IIiIiII11i + ii / IIIi11I1 / Ii1i1i * OOooOOo
def O000o0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( iiIiii1IIIII ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiiiiIIii + 'movhub.png' )
def Oo0Oo ( ) :
 if 5 - 5: iI11I1II1I1I . o0O00o
 if 93 - 93: ooOO0O0ooOooO % ooOoO0O00
 if 83 - 83: oOo0O0Ooo . I1ii11iIi11i - iIII . I11i
 if 73 - 73: oOo0O0Ooo - IIIIiiII111 . IIIIiiII111
 if 22 - 22: oOOoOooOo / oOOoOooOo - Ii1i1i % iIII . IIIi11I1 + o0O00o
 if 64 - 64: ooOoO0O00 % Ii1I / Ii1i1i % ii
 if 24 - 24: o0O0Oooo0O + ii . o0O00o / OOooOOo / iIII
 if 65 - 65: ii
 if 18 - 18: o0o00Oo0O - ooOoO0O00 . o0O0Oooo0O
 if 98 - 98: I11i
 if 73 - 73: I1ii11iIi11i - IIIIiiII111 . ooOO0O0ooOooO % ooOoO0O00 . o0o00Oo0O
 if 15 - 15: oOOoOooOo . iI11I1II1I1I * oOo0O0Ooo % iIII
 if 21 - 21: oO0o - oOo0O0Ooo . ii
 if 6 - 6: iI11I1II1I1I - iI11I1II1I1I % I11i / iI11I1II1I1I * o0O0Oooo0O
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'http://onlinemovies.tube/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 OoO00oo00 = i1iIIIiiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( OoO00oo00 )
 Ii1i1iI1iIIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , iIi in Ii1i1iI1iIIi :
  if 'movies' in iIi :
   I111I11I111 ( iIi + '-' + iiIiii1IIIII , Oo0o00OO0000 , 90044 , iII11 )
 for Oo0o00OO0000 in next :
  iiI1ii1Iii ( Oo0o00OO0000 )
  if 88 - 88: IIIIiiII111 * ii . iI11I1II1I1I
def O00OO ( ) :
 I111I11I111 ( 'Search' , '' , 80008 , iiiiiIIii + 'Search.png' )
 oO0000OOo00 = i11oO0oOo0 ( 'http://www.join4films.com/' )
 Ii1i1iI1iIIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 80006 , iiiiiIIii + 'Desi.png' )
def IIi111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0000OOo00 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( iiIiii1IIIII , url , 80007 , iII11 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( 'Next' , url , 80006 , iiiiiIIii + 'Next.png' )
def oO0o0o0O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  url = ( url ) . replace ( ' ' , '%20' )
  O0i1iI ( url )
def I111ii1iI ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'http://www.join4films.com/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 OoO00oo00 = i1iIIIiiiI . lower ( )
 IIi111 ( OoO00oo00 )
 if 33 - 33: Ii1i1i % o0o00Oo0O + Ii1I
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
 if 71 - 71: oOOoOooOo . oOOoOooOo - iI11I1II1I1I
 if 22 - 22: ii / Ii1I % IIIIiiII111 * OOooOOo
 if 32 - 32: ii % ooOO0O0ooOooO % iI11I1II1I1I / o0o00Oo0O
def Ooo0oOOoo0O ( ) :
 OoOOoOooooOOo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( 'Search' , '' , 10078 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
 if 57 - 57: oOo0O0Ooo . Ii * IIiIiII11i + ii + Ii1i1i
def OoO0o0oOOO ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'http://imoviemax.se/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 OoO00oo00 = i1iIIIiiiI . lower ( )
 oO0I1I1i1I1I1I1 ( OoO00oo00 )
def iI11IiIiiII1 ( url ) :
 I11iii1i = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , ii1i1Iii in Ii1i1iI1iIIi :
  if iiIiii1IIIII in I11iii1i :
   pass
  else :
   OoOOoOooooOOo ( iiIiii1IIIII + ' - ' + ii1i1Iii + ' Films' , url , 10074 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
   I11iii1i . append ( iiIiii1IIIII )
   if 57 - 57: o0O00o
def IiI11I1Ii11II ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , oo0ooOoOOoO in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII + ' - Views:' + oo0ooOoOOoO , url , 10075 , iiiiiIIii + 'genievision.png' , iIi1ii1I1 , '' )
  if 65 - 65: o0o00Oo0O + o0O0Oooo0O % Ii1i1i * oOo0O0Ooo / oOOoOooOo / OOooOOo
  if 71 - 71: Ii / OOooOOo . ooOO0O0ooOooO
def oO0I1I1i1I1I1I1 ( url ) :
 iI1IIIi11 = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0000OOo00 )
 for next in next :
  OoOOoOooooOOo ( 'NEXT PAGE' , next , 10074 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 Ii1i1iI1iIIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 10075 , iII11 , iII11 , '' )
  iI1IIIi11 . append ( iiIiii1IIIII )
  if 69 - 69: o0o00Oo0O - o0o00Oo0O
def i1I1i1i1I1 ( img , name , url ) :
 img = img
 name = name
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0000OOo00 )
 for iI1i1I1 , url in Ii1i1iI1iIIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iIi1Ii1111i = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iIi1Ii1111i
  i1iooO0oO0o = ( iI1i1I1 ) . replace ( 'play-' , 'Server ' )
  oOOOoo0O0oO ( i1iooO0oO0o , iIi1Ii1111i , 10076 , img , img , '' )
  if 22 - 22: I11i + I1ii11iIi11i . oOOoOooOo + Ii1I * IIIIiiII111 . Ii
def O0OOOOOO0ooO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0000OOo00 )
 for Oo0Oo0O in Ii1i1iI1iIIi :
  if '=m' in Oo0Oo0O :
   II11IiI1 ( Oo0Oo0O )
  elif 'php' in Oo0Oo0O :
   O0OOOOOO0ooO ( url )
  else :
   oO0000OOo00 = i11oO0oOo0 ( Oo0Oo0O )
   Ii1i1iI1iIIi = re . compile ( 'content="([^"]*)">' ) . findall ( oO0000OOo00 )
   for i1iIIII1iiIIi in Ii1i1iI1iIIi :
    II11IiI1 ( Oo0Oo0O )
    if 86 - 86: iI11I1II1I1I % ooOO0O0ooOooO - OOooOOo + o0O0Oooo0O % oO0o . Ii1I
    if 4 - 4: ooOoO0O00 + OOooOOo
    if 39 - 39: iI11I1II1I1I + oOOoOooOo
def o00oOoo0o00 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 iIiiI11II11i = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for O00o0O , o00OoO0o0 in iIiiI11II11i :
  print 'there ><><><><><><><><><><><><'
  O00o0O = O00o0O
  Ii1i1iI1iIIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o00OoO0o0 ) )
  for iiIiii1IIIII , iiI11ii1111 in Ii1i1iI1iIIi :
   print 'here <><><><><><><><><><><><>'
   OoOOoOooooOOo ( '[COLORred]' + O00o0O + '[/COLOR] - ' + iiIiii1IIIII + ' - [COLOR' + II11iiii1Ii + ']' + iiI11ii1111 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiiiiIIii + 'loader.png' , iIi1ii1I1 , '' )
 Ii1II1I11i1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for O00o0O , o0OOOoO0ooOOOo0 in Ii1II1I11i1 :
  print 'there ><><><><><><><><><><><><'
  O00o0O = O00o0O
  Ii1i1iI1iIIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0OOOoO0ooOOOo0 ) )
  for iiIiii1IIIII , iiI11ii1111 in Ii1i1iI1iIIi :
   print 'here <><><><><><><><><><><><>'
   OoOOoOooooOOo ( '[COLORred]' + O00o0O + '[/COLOR] - ' + iiIiii1IIIII + ' - [COLOR' + II11iiii1Ii + ']' + iiI11ii1111 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiiiiIIii + 'loader.png' , iIi1ii1I1 , '' )
   if 93 - 93: I1ii11iIi11i
   if 75 - 75: OOooOOo
   if 64 - 64: o0O00o / I11i / ooOoO0O00
def Ii1I11I ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Ii1II1I11i1 in Ii1II1I11i1 :
  iiIiii1IIIII = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iiIiii1IIIII in iiIiii1IIIII :
   iiIiii1IIIII = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Ii1II1I11i1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
  for iI in iI :
   iI = 'http:' + iI
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI , '' , '' )
  if 79 - 79: IIIi11I1 % o0O0Oooo0O / ooOO0O0ooOooO - iI11I1II1I1I - OOooOOo
  if 60 - 60: IIiIiII11i
  if 90 - 90: OOooOOo
  if 37 - 37: OOooOOo + o0o00Oo0O . o0o00Oo0O * I1ii11iIi11i % o0O0Oooo0O / IIIIiiII111
def II1Ii1iI1i1 ( url ) :
 if 18 - 18: ii
 O0oOo00oooO = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0Oo0O , iII11 , iiIiii1IIIII , IiiIiI1IIi1IIIii in Ii1i1iI1iIIi :
  iiIiii1IIIII = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iiIi1IIiIi = i11oO0oOo0 ( Oo0Oo0O )
  I1Ii = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iiIi1IIiIi )
  for iii11I11iI1 , IiI1IIIII1I in I1Ii :
   OOO0oO0O00OO = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( IiI1IIIII1I ) )
   for i11II1I11I1 in OOO0oO0O00OO :
    if iiIiii1IIIII in O0oOo00oooO :
     pass
    else :
     oOOOoo0O0oO ( iiIiii1IIIII , iii11I11iI1 , 8043 , iII11 , iII11 , i11II1I11I1 )
     OOoOO0o0o0 ( 'movies' , 'INFO' )
     O0oOo00oooO . append ( iiIiii1IIIII )
     if 43 - 43: ooOO0O0ooOooO + ii . I11i . Ii1I
     if 30 - 30: oOOoOooOo - Ii + oOo0O0Ooo / I1ii11iIi11i % o0o00Oo0O
def oooooO00OOO ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , ii1IiIiI1 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 10065 , ii1IiIiI1 , ooo0O0o00O , i11II1I11I1 )
 OOoOO0o0o0 ( 'movies' , 'INFO' )
 if 53 - 53: IIiIiII11i
def Oo0O0ooo0O0O ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'https://www.youtube.com/results?search_query=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 OoO00oo00 = i1iIIIiiiI . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( OoO00oo00 )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 in next :
  Oo0o00OO0000 = 'https://www.youtube.com' + Oo0o00OO0000
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + '] NEXT [/COLOR]' , Oo0o00OO0000 , 10065 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 for iII11 , Oo0o00OO0000 , iiIiii1IIIII , iIIiI , IiI1IIIII1I in Ii1i1iI1iIIi :
  O000oo0O . append ( iiIiii1IIIII )
  OOoOO0o0o0 ( 'tvshows' , 'INFO' )
  iI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iI
  Oo0o00OO0000 = 'http://www.youtube.com' + Oo0o00OO0000
  oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI , iI , IiI1IIIII1I )
 else :
  Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iII11 , Oo0o00OO0000 , iiIiii1IIIII , iIIiI in Ii1i1iI1iIIi :
   print 'im doing it'
   OOoOO0o0o0 ( 'tvshows' , 'INFO' )
   iI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
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
     iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
     for iI in iI :
      iI = 'http:' + iI
     oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI , iIi1ii1I1 , '' )
   elif iiIiii1IIIII in O000oo0O :
    pass
   elif 'user' in Oo0o00OO0000 or 'elete' in iiIiii1IIIII :
    pass
   elif 'hannel' in Oo0o00OO0000 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Oo0o00OO0000
    oO0000OOo00 = i11oO0oOo0 ( Oo0o00OO0000 )
    Oo0O00oOoo00 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
    for iII11 , Oo0o00OO0000 , iiIiii1IIIII in Oo0O00oOoo00 :
     if 'outube' in Oo0o00OO0000 or 'list' in Oo0o00OO0000 :
      pass
     elif 'atch' in Oo0o00OO0000 :
      Oo0o00OO0000 = ( Oo0o00OO0000 ) . replace ( '/watch?v=' , '' )
      oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iII11 , 'http:' + iII11 , '' )
     else :
      pass
   else :
    oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI , iI , '' )
    if 28 - 28: Ii1I + ooOO0O0ooOooO / IIIi11I1 + IIIIiiII111 + oOOoOooOo
def iiiiii1Ii ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0000OOo00 )
 for url in next :
  url = 'https://www.youtube.com' + url
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + '] NEXT [/COLOR]' , url , 10065 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 for iII11 , url , iiIiii1IIIII , iIIiI , IiI1IIIII1I in Ii1i1iI1iIIi :
  O000oo0O . append ( iiIiii1IIIII )
  OOoOO0o0o0 ( 'tvshows' , 'INFO' )
  iI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iI
  url = 'http://www.youtube.com' + url
  oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI , iI , IiI1IIIII1I )
 else :
  Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iII11 , url , iiIiii1IIIII , iIIiI in Ii1i1iI1iIIi :
   OOoOO0o0o0 ( 'tvshows' , 'INFO' )
   iI = 'http:' + ( iII11 ) . replace ( 'https:' , '' )
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
     iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii1II1I11i1 ) )
     for iI in iI :
      iI = 'http:' + iI
     oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI , iIi1ii1I1 , '' )
   elif iiIiii1IIIII in O000oo0O :
    pass
   elif 'user' in url or 'elete' in iiIiii1IIIII :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0000OOo00 = i11oO0oOo0 ( url )
    Oo0O00oOoo00 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
    for iII11 , url , iiIiii1IIIII in Oo0O00oOoo00 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iII11 , 'http:' + iII11 , '' )
     else :
      pass
   else :
    oOOOoo0O0oO ( '[COLORred]' + iIIiI + '[/COLOR]' + '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI , iI , '' )
    if 20 - 20: o0O0Oooo0O + o0O0Oooo0O * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
    if 62 - 62: ii / OOooOOo . o0O00o . o0O00o % oOOoOooOo
    if 42 - 42: I11i . IIIi11I1 - oOOoOooOo
def Iiii ( ) :
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiiiiIIii + 'linkchannels.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Open Guide[/COLOR]' , '' , 100213 , iiiiiIIii + 'TvGuide.png' , iIi1ii1I1 , '' )
 if 56 - 56: iIII - o0o00Oo0O / o0o00Oo0O * ooOoO0O00 . ii % iI11I1II1I1I
def I11iIiI1 ( ) :
 ivuesetup . iVueInt ( )
 if 22 - 22: o0O00o * Ii1i1i - ii
def i1Ii1 ( ) :
 oooOOo0oOoOO ( )
 return
 if 6 - 6: ooOO0O0ooOooO . iIII
def oooOOo0oOoOO ( ) :
 if 43 - 43: Ii1I + I11i
 o0OOOO00O0Oo = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 iI1iiiiiii = o0OOOO00O0Oo . getSetting ( id = 'User' )
 Oo00oo = o0OOOO00O0Oo . getSetting ( id = 'Pass' )
 oO0oO = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 o0ooo = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 IiI = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 ii11I = "http://piesustv" + O00o0OO + ":8000/get.php?username=" + iI1iiiiiii + "&password=" + Oo00oo + "&type=m3u_plus&output=ts"
 Ooo0O00 = "http://piesustv" + O00o0OO + ":8000/xmltv.php?username=" + iI1iiiiiii + "&password=" + Oo00oo + "&type=m3u_plus&output=ts"
 if 53 - 53: o0o00Oo0O . oOo0O0Ooo
 xbmc . executeJSONRPC ( oO0oO )
 xbmc . executeJSONRPC ( o0ooo )
 xbmc . executeJSONRPC ( IiI )
 if 74 - 74: oOOoOooOo % OOooOOo / I1ii11iIi11i
 i1111Ii11i = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 i1111Ii11i . setSetting ( id = 'm3uUrl' , value = ii11I )
 i1111Ii11i . setSetting ( id = 'epgUrl' , value = Ooo0O00 )
 i1111Ii11i . setSetting ( id = 'm3uCache' , value = "false" )
 i1111Ii11i . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def OoOo00O0o ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 96 - 96: o0O00o * o0O00o % oOOoOooOo + I11i
if 27 - 27: I1ii11iIi11i * oOOoOooOo + Ii / oOo0O0Ooo - ooOO0O0ooOooO
if 44 - 44: Ii1i1i * oOOoOooOo / OOooOOo
def o0Oo0ooo ( ) :
 if 60 - 60: oOo0O0Ooo
 if 44 - 44: IIiIiII11i . IIiIiII11i + IIIi11I1 * Ii1i1i
 if 16 - 16: IIiIiII11i
 if 100 - 100: o0o00Oo0O - ooOoO0O00
 if 48 - 48: ooOO0O0ooOooO % oOOoOooOo + o0o00Oo0O
 if 27 - 27: Ii1I / IIIi11I1
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 if 63 - 63: o0O00o + iI11I1II1I1I + oOo0O0Ooo + o0O0Oooo0O
 if 72 - 72: oO0o + Ii + Ii1I
 if 96 - 96: ooOO0O0ooOooO % ooOoO0O00 / I11i
 if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + IIIIiiII111
 if 88 - 88: o0o00Oo0O . ooOO0O0ooOooO % oOo0O0Ooo
 if O0o0Oo == "insert_username" :
  iii111i = iIi11ii1iI ( )
  oOiI1I = i111I1 ( )
  I11 ( 'User' , iii111i )
  I11 ( 'Pass' , oOiI1I )
  xbmc . executebuiltin ( 'Container.Refresh' )
  OOOo0Oo0O = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( iii111i , oOiI1I )
  OOOo0Oo0O = i11oO0oOo0 ( OOOo0Oo0O )
  if OOOo0Oo0O == "" :
   i1I1I1iIIi = "[COLOR " + II11iiii1Ii + "]Incorrect Login Details[/COLOR]"
   IiOo00O0o0O = "[COLOR " + II11iiii1Ii + "]Please Re-enter[/COLOR]"
   O0OoOO = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , i1I1I1iIIi , IiOo00O0o0O , O0OoOO )
   o0Oo0ooo ( )
  else :
   i1I1I1iIIi = "[COLOR " + II11iiii1Ii + "]Login Successful[/COLOR]"
   IiOo00O0o0O = "[COLOR " + II11iiii1Ii + "]Welcome to GenieTv[/COLOR]"
   O0OoOO = ( '[COLOR ' + II11iiii1Ii + ']%s[/COLOR]' % iii111i )
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
  if 18 - 18: oO0o % ooOO0O0ooOooO . IIIIiiII111 . Ii1i1i . IIIIiiII111 - o0O0Oooo0O
  if 33 - 33: oOOoOooOo + ii - oO0o / ooOoO0O00 / ii
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
 ii11I = "http://piesustv" + O00o0OO + ":8000//get.php?username=" + O0o0Oo + "&password=" + Oo00OOOOO + "&type=m3u_plus&output=ts"
 try :
  IIIIii11II1I = urllib2 . urlopen ( ii11I )
  print IIIIii11II1I . getcode ( )
  IIIIii11II1I . close ( )
  if 48 - 48: Ii1I - o0o00Oo0O . oO0o
  pass
  if 38 - 38: o0o00Oo0O
 except urllib2 . HTTPError , I1iI1I1I1i11i :
  print I1iI1I1I1i11i . getcode ( )
  O0OoO000O0OO . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + II11iiii1Ii + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + II11iiii1Ii + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def o0o0oO0OOO ( ) :
 OOooOoooOoOo ( )
 if 79 - 79: ooOoO0O00 . ooOO0O0ooOooO
 if 34 - 34: o0O0Oooo0O * IIiIiII11i
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']My Account[/COLOR]' , 'http://piesustv' + O00o0OO + ':8000/panel_api.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO , 60004 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Guide Menu[/COLOR]' , '' , 100211 , iiiiiIIii + 'TvGuide.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']VOD Lists[/COLOR]' , '' , 40000 , iiiiiIIii + 'Vod_Lists.png' , iIi1ii1I1 , '' )
 if 71 - 71: o0O00o
 if 97 - 97: Ii1I
 if 86 - 86: I1ii11iIi11i - IIIi11I1 . OOooOOo . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
 if 34 - 34: I11i . o0O0Oooo0O % o0O00o - o0o00Oo0O / o0O0Oooo0O
def Oo00OOoO0oo ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 IIi11ii11 = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + O0o0Oo + '%26password%3D' + Oo00OOOOO + '%26type%3Dm3u_plus%26output%3Dts'
 O0Oo00OOoO = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + O0o0Oo + '%26password%3D' + Oo00OOOOO
 OOOo0Oo0O = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO + '&type=get_vod_categories'
 OOOo0Oo0O = i11oO0oOo0 ( OOOo0Oo0O )
 if not OOOo0Oo0O == "" :
  OoOooO = 'https://tinyurl.com/create.php?source=indexpage&url=' + IIi11ii11 + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( OoOooO ) )
  I1I1i11iiiiI = 'https://tinyurl.com/create.php?source=indexpage&url=' + O0Oo00OOoO + '&submit=Make+TinyURL%21&alias='
  IIi11ii11 = i11oO0oOo0 ( OoOooO )
  O0Oo00OOoO = i11oO0oOo0 ( I1I1i11iiiiI )
  xbmc . log ( str ( O0Oo00OOoO ) )
  oOOoo = I1I1i11 ( IIi11ii11 , '<div class="indent"><b>' , '</b>' )
  oOo0Oo00O = I1I1i11 ( O0Oo00OOoO , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + II11iiii1Ii + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % oOOoo , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % oOo0Oo00O )
 else :
  return
def i1io0o00O ( ) :
 OOO0 ( )
 iiiI1ii ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOoooOooOOoO + '&action=get_vod_streams' , 40001 , iiiiiIIii + 'Vod_Lists.png' , iIi1ii1I1 , '' )
 oO0000OOo00 = i11oO0oOo0 ( O0O0O0OO00oo )
 Ii1i1iI1iIIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLORsteelblue]' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , Oo0o00OO0000 , 40001 , iiiiiIIii + 'Vod_Lists.png' , iIi1ii1I1 , '' )
def I11IIIIiI1 ( url ) :
 open = i11oO0oOo0 ( o0oOOO + url )
 o00OoOooo = i1I1ii1 ( open , '<channel>' , '</channel>' )
 for oOoO00o in o00OoOooo :
  if '<playlist_url>' in open :
   iiIiii1IIIII = I1I1i11 ( oOoO00o , '<title>' , '</title>' )
   oOO0 = I1I1i11 ( oOoO00o , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   OoOOoOooooOOo ( str ( base64 . b64decode ( iiIiii1IIIII ) ) . replace ( '?' , '' ) , oOO0 , 40001 , icon , ooo0O0o00O , '' )
  else :
   if xbmcaddon . Addon ( ) . getSetting ( 'meta' ) == 'true' :
    try :
     iiIiii1IIIII = I1I1i11 ( oOoO00o , '<title>' , '</title>' )
     iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
     Iii1i = I1I1i11 ( oOoO00o , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     url = I1I1i11 ( oOoO00o , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
     i11II1I11I1 = I1I1i11 ( oOoO00o , '<description>' , '</description>' )
     i11II1I11I1 = base64 . b64decode ( i11II1I11I1 )
     iiIiI = I1I1i11 ( i11II1I11I1 , 'PLOT:' , '\n' )
     ooOooo00O = I1I1i11 ( i11II1I11I1 , 'CAST:' , '\n' )
     I1i1I1IIiIIi = I1I1i11 ( i11II1I11I1 , 'RATING:' , '\n' )
     o0Ooo0O00 = I1I1i11 ( i11II1I11I1 , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
     o0Ooo0O00 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( o0Ooo0O00 )
     iII1ii1IIII = I1I1i11 ( i11II1I11I1 , 'DURATION_SECS:' , '\n' )
     Oo0o0O0OOOo0 = I1I1i11 ( i11II1I11I1 , 'GENRE:' , '\n' )
     I1ii1i ( str ( iiIiii1IIIII ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , Iii1i , ooo0O0o00O , iiIiI , str ( o0Ooo0O00 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( ooOooo00O ) . split ( ) , I1i1I1IIiIIi , iII1ii1IIII , Oo0o0O0OOOo0 )
    except : pass
    xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   else :
    iiIiii1IIIII = I1I1i11 ( oOoO00o , '<title>' , '</title>' )
    iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
    Iii1i = I1I1i11 ( oOoO00o , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    url = I1I1i11 ( oOoO00o , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
    i11II1I11I1 = I1I1i11 ( oOoO00o , '<description>' , '</description>' )
    oOOOoo0O0oO ( iiIiii1IIIII , url , 222 , Iii1i , ooo0O0o00O , base64 . b64decode ( i11II1I11I1 ) )
    if 51 - 51: oO0o - IIIIiiII111 % o0o00Oo0O - OOooOOo
o0oooo0oo00O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
IIIIII1iI1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 14 - 14: oOo0O0Ooo / o0o00Oo0O
def II111iii ( ) :
 ii11I = "http://piesustv" + O00o0OO + ":8000/get.php?username=" + O0o0Oo + "&password=" + Oo00OOOOO + "&type=m3u_plus&output=ts"
 try :
  IIIIii11II1I = urllib2 . urlopen ( ii11I )
  print IIIIii11II1I . getcode ( )
  IIIIii11II1I . close ( )
  if 56 - 56: iI11I1II1I1I % oO0o . oOOoOooOo % o0O00o . o0O0Oooo0O * I1ii11iIi11i
  pass
  if 41 - 41: iI11I1II1I1I % o0O00o * ooOO0O0ooOooO - oOOoOooOo
 except urllib2 . HTTPError , I1iI1I1I1i11i :
  print I1iI1I1I1i11i . getcode ( )
  O0OoO000O0OO . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 5 - 5: oO0o + oO0o + IIiIiII11i * iI11I1II1I1I + ii
 Oo0o00OO0000 = "http://piesustv" + O00o0OO + ":8000/xmltv.php?username=%s&password=%s" % ( O0o0Oo , Oo00OOOOO )
 Oo0OOOOOOO0oo ( Oo0o00OO0000 , IIIIII1iI1II + "uide.xml" )
 if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
 OOo0O0oo0OO0O = open ( o0oooo0oo00O , 'r+' )
 input = open ( o0oooo0oo00O ) . read ( ) . decode ( 'UTF-8' )
 I1iIIIiiii = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 OOo0O0oo0OO0O . write ( I1iIIIiiii )
 OOo0O0oo0OO0O . truncate ( )
 OOo0O0oo0OO0O . close ( )
 I1111 ( )
 if 67 - 67: ooOoO0O00
def I1111 ( ) :
 open = i11oO0oOo0 ( O0Oo0oo0O0O0o )
 all = i1I1ii1 ( open , '{"num' , 'direct' )
 for oOoO00o in all :
  if '"tv_archive":1' in oOoO00o :
   iiIiii1IIIII = I1I1i11 ( oOoO00o , '"epg_channel_id":"' , '"' )
   Iii1i = I1I1i11 ( oOoO00o , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = I1I1i11 ( oOoO00o , 'stream_id":"' , '"' )
   iiIiii1IIIII = iiIiii1IIIII . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   OoOOoOooooOOo ( iiIiii1IIIII , id , 90027 , Iii1i , ooo0O0o00O , iiIiii1IIIII )
   if 11 - 11: oO0o * IIiIiII11i + oOOoOooOo * iI11I1II1I1I % I1ii11iIi11i
   if 8 - 8: oOo0O0Ooo % IIiIiII11i - I11i - iIII % oOo0O0Ooo
def o0o0O0oOooO00 ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 O00Ooo = open ( o0oooo0oo00O )
 i1ii1111iiI = ElementTree . parse ( O00Ooo )
 iiIIIII = "apples"
 import datetime as dt
 from datetime import time
 iiI1 = datetime . now ( ) - timedelta ( days = 5 )
 O00o0O = str ( iiI1 )
 O000OO0 = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 iii11i1 = i1ii1111iiI . findall ( "programme" )
 for IIiI1I1IIiiI1 in iii11i1 :
  if name in IIiI1I1IIiiI1 . attrib . get ( 'channel' ) :
   oooOOO0o0O0 = IIiI1I1IIiiI1 . attrib . get ( 'start' )
   iiiI1IiI , Ii111IIIIii , O00o = oooOOO0o0O0 . partition ( ' +' )
   O00o0O = str ( O00o0O ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   o0Ooo0O00 , Iii1iIIiii1ii , O0000 = oooOOO0o0O0 . partition ( '2017' )
   Ii1iii11I = IIiI1I1IIiiI1 . find ( 'title' ) . text + oooOOO0o0O0
   O0000 = O0000 [ : - 6 ]
   if iiiI1IiI > O00o0O :
    if iiiI1IiI < O000OO0 :
     Ii11iIiiI = iiiI1IiI
     Ii11iIiiI = Ii11iIiiI [ : 4 ] + '/' + Ii11iIiiI [ 4 : ]
     iiiI1IiI = iiiI1IiI [ : 4 ] + '-' + iiiI1IiI [ 4 : ]
     Ii11iIiiI = Ii11iIiiI [ : 7 ] + '/' + Ii11iIiiI [ 7 : ]
     iiiI1IiI = iiiI1IiI [ : 7 ] + '-' + iiiI1IiI [ 7 : ]
     Ii11iIiiI = Ii11iIiiI [ : 10 ] + ' - ' + Ii11iIiiI [ 10 : ]
     iiiI1IiI = iiiI1IiI [ : 10 ] + ':' + iiiI1IiI [ 10 : ]
     Ii11iIiiI = Ii11iIiiI [ : 15 ] + ':' + Ii11iIiiI [ 15 : ]
     iiiI1IiI = iiiI1IiI [ : 13 ] + '-' + iiiI1IiI [ 13 : ]
     Ii11iIiiI = Ii11iIiiI [ : - 2 ]
     iiiI1IiI = iiiI1IiI [ : - 2 ]
     iiII = ( "http://piesustv" + O00o0OO + ":8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( iiiI1IiI ) + "&duration=240" + "&stream=%s" ) % ( O0o0Oo , Oo00OOOOO , id )
     iiIIIII = iiII + str ( iiiI1IiI ) + "&duration=240"
     Ii11iIiiI = '[COLOR blue]%s - [/COLOR]' % Ii11iIiiI
     Ii1iii11I = str ( Ii11iIiiI ) + IIiI1I1IIiiI1 . find ( 'title' ) . text
     i11II1I11I1 = IIiI1I1IIiiI1 . find ( 'desc' ) . text
     oOOOoo0O0oO ( Ii1iii11I , iiII , 222 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , i11II1I11I1 )
def iII1IiiIIIIii ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , O0o0Oo ) . replace ( 'PASSWORD' , Oo00OOOOO )
 I1I1 = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = o0 )
 I1I1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 I1I1 . setProperty ( 'IsPlayable' , 'true' )
 I1I1 . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1 )
def Oo0OOOOOOO0oo ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 oOOO = time . time ( )
 urllib . urlretrieve ( url , dest , lambda Iii1IiiII1Ii1 , iiiIIi , OOoOo0O00oo : oo0oO0oOo0O ( Iii1IiiII1Ii1 , iiiIIi , OOoOo0O00oo , o0oOoO00o , oOOO ) )
def oo0oO0oOo0O ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  OoOo00 = min ( numblocks * blocksize * 100 / filesize , 100 )
  OOoOoO = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  OO000 = numblocks * blocksize / ( time . time ( ) - start_time )
  if OO000 > 0 :
   o0oOoo0o = ( filesize - numblocks * blocksize ) / OO000
  else :
   o0oOoo0o = 0
  OO000 = OO000 / 1024
  IiiIiIIi = OO000 / 1024
  O00Oo = float ( filesize ) / ( 1024 * 1024 )
  oOOoooo0O0 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( OOoOoO )
  I1iI1I1I1i11i = '[COLOR white]Speed:  %.02f Mb/s ' % IiiIiIIi + '[/COLOR]'
  dp . update ( OoOo00 , oOOoooo0O0 , I1iI1I1I1i11i )
 except :
  OoOo00 = 100
  dp . update ( OoOo00 )
 if dp . iscanceled ( ) :
  Ii111Ii11 = xbmcgui . Dialog ( )
  Ii111Ii11 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIIi11I1
  sys . exit ( )
  dp . close ( )
  if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
def O00000OO00OO ( ) :
 if Oo00OOOOO == 'insert_password' :
  O0OoO000O0OO . ok ( '[COLOR' + II11iiii1Ii + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II11iiii1Ii + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iI11iI ( )
  if 100 - 100: ii + Ii % I11i + oOo0O0Ooo . I1ii11iIi11i . IIiIiII11i
  if 93 - 93: IIiIiII11i . Ii + IIiIiII11i % ooOO0O0ooOooO
  if 98 - 98: o0O0Oooo0O * ooOO0O0ooOooO * OOooOOo + Ii1i1i * IIIIiiII111
  if 4 - 4: o0O00o
  if 16 - 16: iI11I1II1I1I * IIIIiiII111 + ooOO0O0ooOooO . o0o00Oo0O . I11i
  if 99 - 99: Ii - IIIIiiII111
  if 85 - 85: o0O0Oooo0O % Ii1I
  if 95 - 95: oO0o * IIIi11I1 * IIIIiiII111 . I11i
def iI11iI ( ) :
 I1I1IiI1 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/panel_api.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO )
 Ii1i1iI1iIIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( I1I1IiI1 )
 for Oo0o00OO0000 in Ii1i1iI1iIIi :
  dt = datetime . fromtimestamp ( float ( Ii1i1iI1iIIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if O000OO0 <= dt <= O000OO0 + timedelta ( hours = 24 ) :
   O0OoO000O0OO . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II11iiii1Ii + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II11iiii1Ii + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II11iiii1Ii + '] To Purchase A licence[/COLOR]' )
def oooOo00 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '"username":"(.+?)"' ) . findall ( I1I1IiI1 )
 iII1II = re . compile ( '"password":"(.+?)"' ) . findall ( I1I1IiI1 )
 I1iiIIIi11 = re . compile ( '"status":"(.+?)"' ) . findall ( I1I1IiI1 )
 I1Ii = re . compile ( '"exp_date":"(.+?)"' ) . findall ( I1I1IiI1 )
 II1iIi1IiIii = re . compile ( '"active_cons":"(.+?)"' ) . findall ( I1I1IiI1 )
 iI111i11iI1 = re . compile ( '"created_at":"(.+?)"' ) . findall ( I1I1IiI1 )
 III1ii = re . compile ( '"max_connections":"(.+?)"' ) . findall ( I1I1IiI1 )
 OoOOIIIIIiI11Ii = re . compile ( '"is_trial":"1"' ) . findall ( I1I1IiI1 )
 o0OOooO = re . compile ( '"is_trial":"0"' ) . findall ( I1I1IiI1 )
 iiI111iIi1 = I1i1ii1ii ( )
 i1ii = oOOOOO0 ( )
 for url in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']My GTV Account Information[/COLOR]' , '' , '' , iiiiiIIii + 'MyAcc.png' )
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in iII1II :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in I1iiIIIi11 :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in iI111i11iI1 :
  dt = datetime . fromtimestamp ( float ( iI111i11iI1 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in I1Ii :
  dt = datetime . fromtimestamp ( float ( I1Ii [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if O000OO0 <= dt <= O000OO0 + timedelta ( hours = 24 ) :
   iiiiI11ii ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiiiiIIii + 'MyAcc.png' )
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in II1iIi1IiIii :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in III1ii :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in OoOOIIIIIiI11Ii :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Trial:[/COLOR] Yes' , '' , '' , iiiiiIIii + 'MyAcc.png' )
 for url in o0OOooO :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Trial:[/COLOR] No' , '' , '' , iiiiiIIii + 'MyAcc.png' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Get Short Links[/COLOR]' , '' , 100214 , iiiiiIIii + 'shortlinks.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Local IP Address:[/COLOR] ' + iiI111iIi1 , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']External IP Address:[/COLOR] ' + i1ii , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 if 4 - 4: I11i + iIII / IIIIiiII111 + ooOoO0O00 % I11i % IIIIiiII111
 iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 80 - 80: Ii1i1i
def iioOO ( ) :
 O0OoO000O0OO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOOOi11i1 + ")" )
 I1OO ( )
 O0OoO000O0OO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 34 - 34: o0O0Oooo0O . OOooOOo / Ii / IIIIiiII111
def II1iII1 ( data ) :
 I11II11IiI11 = len ( data ) % 4
 if 97 - 97: oOOoOooOo / iI11I1II1I1I % oOOoOooOo / oOo0O0Ooo * IIIIiiII111 % OOooOOo
 if 17 - 17: iI11I1II1I1I
 if 89 - 89: ooOoO0O00 . ooOoO0O00
 if 10 - 10: IIIIiiII111 % I1ii11iIi11i
 if 48 - 48: IIIi11I1 + o0O0Oooo0O % IIIi11I1
 if 84 - 84: o0o00Oo0O % Ii1i1i . Ii1i1i . IIIIiiII111 * iIII
 if I11II11IiI11 != 0 :
  data += b'=' * ( 4 - I11II11IiI11 )
 return base64 . decodestring ( data )
def I1I1i11 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : iIOO0O = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : iIOO0O = ''
 else :
  try : iIOO0O = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : iIOO0O = ''
 return iIOO0O
 if 34 - 34: Ii1i1i - ooOO0O0ooOooO * ii . oO0o / oOo0O0Ooo
 if 66 - 66: I1ii11iIi11i / Ii % oOOoOooOo
def i1I1ii1 ( text , start_with , end_with ) :
 iIOO0O = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return iIOO0O
def I1i1ii1ii ( ) :
 i1Ii1i11ii = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 i1Ii1i11ii . connect ( ( '8.8.8.8' , 0 ) )
 i1Ii1i11ii = i1Ii1i11ii . getsockname ( ) [ 0 ]
 return i1Ii1i11ii
 if 58 - 58: OOooOOo + oO0o * Ii1i1i
def oOOOOO0 ( ) :
 open = i11oO0oOo0 ( 'http://canyouseeme.org/' )
 iiI111iIi1 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( iiI111iIi1 . group ( ) )
oOoooOooOOoO = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s' % ( O0o0Oo , Oo00OOOOO )
O0Oo0oo0O0O0o = 'http://piesustv' + O00o0OO + ':8000/panel_api.php?username=%s&password=%s' % ( O0o0Oo , Oo00OOOOO )
iI1IIIIII = 'http://piesustv' + O00o0OO + ':8000/movie/%s/%s/' % ( O0o0Oo , Oo00OOOOO )
OO0oO0Oo = 'http://piesustv' + O00o0OO + ':8000/live/%s/%s/' % ( O0o0Oo , Oo00OOOOO )
OoooOO0 = '&action=get_live_categories'
oo0OoO = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( O0o0Oo , Oo00OOOOO )
O0O0O0OO00oo = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( O0o0Oo , Oo00OOOOO )
if 2 - 2: Ii1I - I1ii11iIi11i
o0oOOO = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( O0o0Oo , Oo00OOOOO )
Iii1 = 'http://piesustv' + O00o0OO + ':8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( O0o0Oo , Oo00OOOOO )
o00o0 = 'http://piesustv' + O00o0OO + ':8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( O0o0Oo , Oo00OOOOO )
OOoOo0O0 = "http://piesustv" + O00o0OO + ":8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( O0o0Oo , Oo00OOOOO )
if 39 - 39: o0O0Oooo0O . oO0o % oOOoOooOo . IIIi11I1 / IIIIiiII111 * oO0o
def iiI1i ( ) :
 OOO0 ( )
 open = i11oO0oOo0 ( o00o0 )
 o00OoOooo = i1I1ii1 ( open , '<channel>' , '</channel>' )
 for oOoO00o in o00OoOooo :
  iiIiii1IIIII = I1I1i11 ( oOoO00o , '<title>' , '</title>' )
  iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
  oOO0 = I1I1i11 ( oOoO00o , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OoOOoOooooOOo ( '[COLORsteelblue]' + iiIiii1IIIII + '[/COLOR]' , oOO0 , 60003 , iiiiiIIii + 'GTV.png' , iIi1ii1I1 , '' )
  if 80 - 80: Ii1i1i + iIII + Ii1i1i
def I11iIiIii ( url ) :
 open = i11oO0oOo0 ( OOoOo0O0 + url )
 o00OoOooo = i1I1ii1 ( open , '<channel>' , '</channel>' )
 for oOoO00o in o00OoOooo :
  iiIiii1IIIII = I1I1i11 ( oOoO00o , '<title>' , '</title>' )
  iiIiii1IIIII = base64 . b64decode ( iiIiii1IIIII )
  xbmc . log ( str ( iiIiii1IIIII ) )
  Iii1i = I1I1i11 ( oOoO00o , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  oOO0 = I1I1i11 ( oOoO00o , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  i11II1I11I1 = I1I1i11 ( oOoO00o , '<description>' , '</description>' )
  i11II1I11I1 = base64 . b64decode ( i11II1I11I1 )
  Ooooo = '('
  IIIiI1iIIII = ')'
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , oOO0 , 222 , Iii1i , ooo0O0o00O , ( '[COLOR' + II11iiii1Ii + ']' + i11II1I11I1 + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( IIIiI1iIIII , '[COLORsteelblue]' ) . replace ( Ooooo , '[COLORorangered]' ) )
  if 75 - 75: IIIi11I1 % IIiIiII11i
def IIIIi1Iii1iIi ( url ) :
 url = url
 oO0000OOo00 = i11oO0oOo0 ( oo0OoO + url )
 Ii1i1iI1iIIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , type , Oo0Oo0O , iI1III1iIi11 in Ii1i1iI1iIIi :
  i1iIIII1iiIIi = ( OO0oO0Oo + Oo0Oo0O + '.m3u8' ) . strip ( )
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , i1iIIII1iiIIi , 222 , ( iI1III1iIi11 ) . replace ( '\/' , '/' ) + 'jpg' , iIi1ii1I1 , type )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
def ii1IIi1iI1ii1 ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0000OOo00 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/xmltv.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO )
 Ii1i1iI1iIIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for O00O00OoO , o00iIIiIi111iI in Ii1i1iI1iIIi :
  if name == O00O00OoO :
   oOOOoo0O0oO ( ( '' + name + '' ) . replace ( '_' , ' ' ) + o00iIIiIi111iI , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   oOOOoo0O0oO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def II1I1ii ( name ) :
 oo0OO0O = name
 oO0000OOo00 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/get.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO + '&type=m3u_plus&output=mpegts' )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0000OOo00 )
 for name , iII11 , Oo0o00OO0000 in Ii1i1iI1iIIi :
  Oo0o00OO0000 = ( Oo0o00OO0000 ) . replace ( '.ts' , '.m3u8' )
  oOOOoo0O0oO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Oo0o00OO0000 ) . strip ( ) , 222 , iII11 , iII11 , '' )
 else :
  oOOOoo0O0oO ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 64 - 64: ooOO0O0ooOooO . Ii1I * o0O0Oooo0O % oOo0O0Ooo
  if 25 - 25: o0o00Oo0O + iIII + IIIi11I1 * Ii1I
  if 87 - 87: I1ii11iIi11i . ii * o0O0Oooo0O * IIiIiII11i / ooOoO0O00 * OOooOOo
  if 25 - 25: Ii1i1i * I11i * ooOO0O0ooOooO . oOo0O0Ooo
  if 93 - 93: OOooOOo
  if 97 - 97: Ii
  if 68 - 68: o0O00o * oO0o . iIII / Ii1i1i . I11i - Ii
  if 49 - 49: I1ii11iIi11i / Ii1i1i % iIII + ooOO0O0ooOooO - oO0o
  if 13 - 13: IIiIiII11i
  if 83 - 83: ii . oOo0O0Ooo + Ii1i1i * o0o00Oo0O / ooOO0O0ooOooO
  if 8 - 8: ooOoO0O00 + IIiIiII11i / Ii1i1i + Ii1I % Ii1i1i - iI11I1II1I1I
  if 29 - 29: I1ii11iIi11i + IIiIiII11i
def oO0oOOoo00000 ( ) :
 OoOOoOooooOOo ( 'Full Backup' , '' , 10061 , iiiiiIIii + 'FullBackUp.png' , iIi1ii1I1 , 'Back Up Your Full System' )
 if os . path . exists ( O00O0oOO00O00 ) :
  OoOOoOooooOOo ( 'Backup Genie Favourites' , Oo0o00OO0000 , 10062 , iiiiiIIii + 'BackupGenieFavourites.png' , iIi1ii1I1 , 'Back Up Your favourites' )
 if os . path . exists ( OOoOO0oo0ooO ) :
  OoOOoOooooOOo ( 'Backup Ivue Config' , OOoOO0oo0ooO , 10062 , iiiiiIIii + 'BackUpIvueConfig.png' , iIi1ii1I1 , 'Back Up Your master.db' )
 if os . path . exists ( O0o0O00Oo0o0 ) :
  OoOOoOooooOOo ( 'Backup Kodi Favourites' , O0o0O00Oo0o0 , 10062 , iiiiiIIii + 'BackKodiFavourites.png' , iIi1ii1I1 , 'Back Up Your favourites.xml' )
  if 95 - 95: ooOO0O0ooOooO
  if 48 - 48: iIII / iI11I1II1I1I % IIiIiII11i
  if 39 - 39: ooOoO0O00 . Ii1I / iIII / iIII
zip = oo00 . getSetting ( 'zip' )
ooOo0oO0O = xbmc . translatePath ( os . path . join ( zip ) )
def I1i1 ( ) :
 I1iI = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  O0OoO000O0OO . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 35 - 35: IIiIiII11i / Ii1i1i
  if 79 - 79: OOooOOo + o0O0Oooo0O * IIIIiiII111 * Ii1i1i
  if 53 - 53: IIIi11I1 / I1ii11iIi11i
def iIO0oOoo00Oo0O ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = O00O0oOO00O00
  elif 'Ivue' in name :
   url = OOoOO0oo0ooO
  elif 'Kodi' in name :
   url = O0o0O00Oo0o0
  I1i1 ( )
  Iii1i1Ii = open ( url ) . read ( )
  III1iIii = os . path . join ( ooOo0oO0O , description . split ( 'Your ' ) [ 1 ] )
  OOo0O0oo0OO0O = open ( III1iIii , mode = 'w' )
  OOo0O0oo0OO0O . write ( Iii1i1Ii )
  OOo0O0oo0OO0O . close ( )
 else :
  if 'guisettings.xml' in description :
   oOoO00o = open ( os . path . join ( ooOo0oO0O , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iIOO0O = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   Ii1i1iI1iIIi = re . compile ( iIOO0O ) . findall ( oOoO00o )
   for type , iiIII1i1 , oOOo0OOoOO0 in Ii1i1iI1iIIi :
    oOOo0OOoOO0 = oOOo0OOoOO0 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iiIII1i1 , oOOo0OOoOO0 ) )
  else :
   III1iIii = os . path . join ( url )
   Iii1i1Ii = open ( os . path . join ( ooOo0oO0O , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOo0O0oo0OO0O = open ( III1iIii , mode = 'w' )
   OOo0O0oo0OO0O . write ( Iii1i1Ii )
   OOo0O0oo0OO0O . close ( )
 O0OoO000O0OO . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 30 - 30: IIiIiII11i / oOo0O0Ooo - oOOoOooOo + OOooOOo * oOOoOooOo / OOooOOo
 if 17 - 17: oO0o
 if 31 - 31: ooOO0O0ooOooO + ii - Ii1i1i % I11i / I11i / iI11I1II1I1I
 if 31 - 31: ii - Ii1i1i . o0O00o % ooOO0O0ooOooO
def II11i1I1iiII1 ( ) :
 iI1I1I = 1
 I1i1 ( )
 Oo0o0oOo0oO = xbmc . translatePath ( os . path . join ( ooOo0oO0O , 'Build Backup' , 'Full Backup' , '' ) )
 i1iiiI1I = xbmc . translatePath ( os . path . join ( ooOo0oO0O , 'Build Backup' , 'my_full_backup.zip' ) )
 o00OoOOoO = xbmc . translatePath ( os . path . join ( ooOo0oO0O , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( Oo0o0oOo0oO ) :
  os . makedirs ( Oo0o0oOo0oO )
 iii1i1Iiiiiii = O0OoO000O0OO . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iii1i1Iiiiiii ) : return False , 0
 oOO0ooIiIIi1I1I11Ii = iii1i1Iiiiiii
 OOoo0 = xbmc . translatePath ( os . path . join ( Oo0o0oOo0oO , oOO0ooIiIIi1I1I11Ii + '.zip' ) )
 Ii11I1iIIi = [ 'plugin.video.GenieTv' ]
 O0ooO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iIOO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1III1I11I1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 oO000OoO00OoO = "Creating full backup of existing build"
 I1IiIi1iiI = "Creating Community Build"
 iiII1II11i = "Archiving..."
 ooO0OoooooOo0oOo0 = ""
 II11II = "Please Wait"
 i1ii11 ( oOo0oooo00o , OOoo0 , I1IiIi1iiI , iiII1II11i , ooO0OoooooOo0oOo0 , II11II , iIOO , I1III1I11I1 )
 time . sleep ( 1 )
 III = xbmc . translatePath ( os . path . join ( Oo0o0oOo0oO , oOO0ooIiIIi1I1I11Ii + '_guisettings.zip' ) )
 o00O = zipfile . ZipFile ( III , mode = 'w' )
 try :
  o00O . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 o00O . close ( )
 if iI1I1I == 0 :
  O0OoO000O0OO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  O0OoO000O0OO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  O0OoO000O0OO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i1iiiI1I , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OOoo0 + '[/COLOR]' )
  if 26 - 26: OOooOOo
def i1ii11 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 I1I11I = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 ooOOO0oOoooOo = len ( sourcefile )
 Ii11IIIii11 = [ ]
 O0oo = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for i1ii1i1i1 , oOOoo0 , II1OOO in os . walk ( sourcefile ) :
  for file in II1OOO :
   O0oo . append ( file )
 iiIII1I11iii = len ( O0oo )
 for i1ii1i1i1 , oOOoo0 , II1OOO in os . walk ( sourcefile ) :
  oOOoo0 [ : ] = [ ooIii for ooIii in oOOoo0 if ooIii not in exclude_dirs ]
  II1OOO [ : ] = [ OOo0O0oo0OO0O for OOo0O0oo0OO0O in II1OOO if OOo0O0oo0OO0O not in exclude_files ]
  for file in II1OOO :
   Ii11IIIii11 . append ( file )
   o0OO00oOOO0o0 = len ( Ii11IIIii11 ) / float ( iiIII1I11iii ) * 100
   o0oOoO00o . update ( int ( o0OO00oOOO0o0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iiii = os . path . join ( i1ii1i1i1 , file )
   if not 'temp' in oOOoo0 :
    if not 'plugin.program.originwizard' in oOOoo0 :
     import time
     oOOOO = '01/01/1980'
     OoOOoo0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iiii ) ) )
     if OoOOoo0 > oOOOO :
      I1I11I . write ( iiii , iiii [ ooOOO0oOoooOo : ] )
 I1I11I . close ( )
 o0oOoO00o . close ( )
 if 93 - 93: IIiIiII11i * OOooOOo % I11i
 if 67 - 67: I11i + I1ii11iIi11i . oOOoOooOo - ooOoO0O00 . OOooOOo
def I1iI1 ( ) :
 OOooOoooOoOo ( )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiiiiIIii + 'scoob.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiiiiIIii + 'scoob.png' , iIi1ii1I1 , '' )
 if 9 - 9: I1ii11iIi11i - oOOoOooOo * IIIIiiII111 / Ii / I1ii11iIi11i % ooOO0O0ooOooO
 if 16 - 16: IIIIiiII111 - ooOoO0O00 + I11i * iI11I1II1I1I + ooOO0O0ooOooO . ooOO0O0ooOooO
def O0Oo0o000Oo0ooOo ( ) :
 OOooOoooOoOo ( )
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']SEARCH YOUTUBE[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Search Genie[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  IiiIIIII1iii ( )
 if OoOOo0OOoO == 1 :
  OOooo0O ( )
 if OoOOo0OOoO == 2 :
  OoOo0000o0OOo ( )
 if OoOOo0OOoO == 3 :
  Oo0O0ooo0O0O ( )
  if 84 - 84: oOOoOooOo
  if 28 - 28: iIII . ii * IIIi11I1 + Ii % oOo0O0Ooo . iI11I1II1I1I
  if 63 - 63: IIiIiII11i - iIII . OOooOOo
  if 8 - 8: oOo0O0Ooo * oOOoOooOo / o0O00o + OOooOOo . o0O00o - IIIi11I1
  if 80 - 80: iI11I1II1I1I / ooOO0O0ooOooO * I1ii11iIi11i - IIIi11I1 * IIIIiiII111
  if 97 - 97: o0O00o - iIII / IIiIiII11i
  if 26 - 26: IIIIiiII111 + o0o00Oo0O * IIIIiiII111 . ooOoO0O00
  if 50 - 50: iI11I1II1I1I - iIII % IIIIiiII111 - I1ii11iIi11i
  if 52 - 52: ooOO0O0ooOooO + Ii1i1i - Ii1I * Ii1i1i . IIIi11I1 + o0O0Oooo0O
def iI11II11I1 ( ) :
 OOooOoooOoOo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']RaysRavers Radio[/COLOR]' , '[COLOR' + II11iiii1Ii + ']ThunderStruck[/COLOR]' , '[COLOR' + II11iiii1Ii + ']RadioNomy[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']UK RADIO[/COLOR]' , '[COLOR' + II11iiii1Ii + ']WORLD RADIO[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CONCERTS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC[/COLOR]' , '[COLOR' + II11iiii1Ii + ']MUSIC SEARCH[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Music[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if OoOOo0OOoO == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if OoOOo0OOoO == 2 :
   oo0o0000 ( )
  if OoOOo0OOoO == 3 :
   I1iIiI ( )
  if OoOOo0OOoO == 4 :
   oo0OoOO000O ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if OoOOo0OOoO == 5 :
   Oo0o0OoOoOo0 ( )
  if OoOOo0OOoO == 6 :
   I11iiI11I1II ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if OoOOo0OOoO == 7 :
   oO0iII1i111iI ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if OoOOo0OOoO == 8 :
   IiI1iI1 ( str ( iI1iIIiiii ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if OoOOo0OOoO == 9 :
   oOoo ( )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']RaysRavers Radio[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , iiiiiIIii + 'Rays-Ravers.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']ThunderStruck[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , iiiiiIIii + 'Thunder.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']RadioNomy[/COLOR]' , '' , 70001 , iiiiiIIii + 'RadioNomy.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MUSIC CHANNELS[/COLOR]' , str ( iI1iIIiiii ) , 30031 , iiiiiIIii + 'MusicChannels.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiiiiIIii + 'UKRadio.png' , iIi1ii1I1 , '' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']WORLD RADIO[/COLOR]' , str ( iI1iIIiiii ) , 1013 , iiiiiIIii + 'WorldRadio.png' , iIi1ii1I1 , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiiiiIIii + 'Concerts.png' , iIi1ii1I1 , '' )
   if 25 - 25: ooOO0O0ooOooO
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiiiiIIii + 'MusicVideos.png' , iIi1ii1I1 , '' )
  if 84 - 84: Ii1I - IIIIiiII111 + Ii1I
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']MUSIC SEARCH[/COLOR]' , str ( iI1iIIiiii ) , 1111 , iiiiiIIii + 'MusicSearch.png' , iIi1ii1I1 , '' )
  if 63 - 63: iIII * oOOoOooOo % IIiIiII11i % o0O0Oooo0O + oOo0O0Ooo * I1ii11iIi11i
  if 96 - 96: o0O00o
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
o0OoOO = 'white'
O0O0Oo00 = 'gold'
def oo00OOo0 ( ) :
 OOooOoooOoOo ( )
 if OOoOooOoOOOoo ( True ) == False : OOO0OOoOOO = 0
 else : OOO0OOoOOO = iiI ( OOoOooOoOOOoo ( True ) , True , True )
 if OOoOooOoOOOoo ( True , True ) == False : oOoO0o0o = 0
 else : oOoO0o0o = iiI ( OOoOooOoOOOoo ( True , True ) , True , True )
 O00O000oOO0oO = int ( OOO0OOoOOO ) + int ( oOoO0o0o )
 OO0i1Ii1II11 = str ( O00O000oOO0oO ) + ' Error(s) Found' if O00O000oOO0oO > 0 else 'None Found'
 IiiIIii1I1I = ': [COLORsteelblue]Not Found[/COLOR]' if not os . path . exists ( oO ) else ": [COLORorangered]%s[/COLOR]" % IIiIIiIi1II1IiI ( os . path . getsize ( oO ) )
 oo0OoOI11iIiiI = OO000oo0o ( i1iIIi1 )
 I11iiIiI1II11 = OO000oo0o ( ii11iIi1I )
 OOOoOOOo = oO0000 ( )
 OOOIIIIiiIi = oo0OoOI11iIiiI + I11iiIiI1II11 + OOOoOOOo
 iiI111iIi1 = I1i1ii1ii ( )
 i1ii = oOOOOO0 ( )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']CLEAN UP:[COLORorangered] [B]%s[/B][/COLOR]' % IIiIIiIi1II1IiI ( OOOIIIIiiIi ) , 'url' , 9666 , iiiiiIIii + 'MAIN5.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']KILL KODI[/COLOR]' , '' , 80000 , iiiiiIIii + 'KillKodi.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']SPEEDTEST[/COLOR]' , '' , 50004 , iiiiiIIii + 'Speedtest.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']VIEW LOG Errors:[COLORorangered] %s[/COLOR]' % ( OO0i1Ii1II11 ) , '' , 219999990 , iiiiiIIii + 'View-Log-File.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , iiiiiIIii + 'View-Log-File.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']CLEAR LOG FILES: [COLORorangered]' + IiiIIii1I1I + '[/COLOR]' , '' , 219999991 , iiiiiIIii + 'View-Log-File.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']DELETE CACHE:[COLORorangered] [B]%s[/B][/COLOR]' % IIiIIiIi1II1IiI ( OOOoOOOo ) , 'url' , 14 , iiiiiIIii + 'DeleteCache.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']DELETE PACKAGES:[COLORorangered] [B]%s[/B][/COLOR]' % IIiIIiIi1II1IiI ( oo0OoOI11iIiiI ) , 'url' , 6 , iiiiiIIii + 'DeletePackages.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']FORCE REFRESH[/COLOR]' , 'url' , 10 , iiiiiIIii + 'ForceRefresh.png' , iIi1ii1I1 , 'Force Refresh All Repos' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']LAST RESORT FIX EMPTY REPOS[/COLOR]' , 'url' , 9 , iiiiiIIii + '1.jpg' , iIi1ii1I1 , 'Fix Corrupt Database' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']CLEAR THUBMNAILS:[COLORorangered] [B]%s[/B][/COLOR]' % IIiIIiIi1II1IiI ( I11iiIiI1II11 ) , 'url' , 219999992 , iiiiiIIii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , iIi1ii1I1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']Local IP Address:[COLORorangered] ' + iiI111iIi1 + '[/COLOR] ' , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']External IP Address:[COLORorangered] ' + i1ii + '[/COLOR] ' , '' , '' , iiiiiIIii + 'CheckMyIP.png' , iIi1ii1I1 , '' )
 if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
 if 61 - 61: Ii1i1i * Ii1i1i
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def O0III1Iiii1i11 ( proc ) :
 xbmc . executebuiltin ( proc )
 if 74 - 74: I1ii11iIi11i / o0O0Oooo0O % o0O0Oooo0O . o0O00o
def ooOo ( ) :
 O0III1Iiii1i11 ( 'Container.Refresh()' )
def o0oo00000O ( ) :
 OOo0O0oo0OO0O = open ( oO , 'w' ) ; OOo0O0oo0OO0O . close ( ) ; o0Oooo ( "[COLOR %s]%s[/COLOR]" % ( o0OoOO , i1iiIIiiI111 ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % O0O0Oo00 )
 ooOo ( )
 if 84 - 84: iI11I1II1I1I
def III1Ii11i1II ( type = None ) :
 IIIII1IIiIi = oo0o ( 'Textures' )
 if not type == None : OoOOo0OOoO = 1
 else : OoOOo0OOoO = O0OoO000O0OO . yesno ( i1iiIIiiI111 , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( O0O0Oo00 , IIIII1IIiIi ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if OoOOo0OOoO == 1 :
  try : OOoOooOOOo0Ooo0o00o ( os . join ( iI111I11I1I1 , IIIII1IIiIi ) )
  except : oOoOooO ( 'Failed to delete, Purging DB.' ) ; o0OoOOoooooOO ( IIIII1IIiIi )
  oOOo ( ii11iIi1I )
  if 97 - 97: IIIi11I1
 else : oOoOooO ( 'Clear thumbnames cancelled' )
 Ii1IiiiII ( )
 if 82 - 82: ooOoO0O00 . Ii1I - ooOO0O0ooOooO . o0O0Oooo0O * ooOO0O0ooOooO
 if 29 - 29: iIII + ooOO0O0ooOooO % oOOoOooOo + OOooOOo
def Ii1IiiiII ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 oOoOo000 = '0123456789abcdef'
 iiI1IiI1I1I = os . path . join ( ii11iIi1I , 'Video' , 'Bookmarks' )
 for IIi1IIIi in oOoOo000 :
  IIIiI1i = os . path . join ( ii11iIi1I , IIi1IIIi )
  if not os . path . exists ( IIIiI1i ) : os . makedirs ( IIIiI1i )
 if not os . path . exists ( iiI1IiI1I1I ) : os . makedirs ( iiI1IiI1I1I )
 if 22 - 22: o0O00o / IIIi11I1
def oo0o ( DB ) :
 if DB in [ 'Addons' , 'ADSP' , 'Epg' , 'MyMusic' , 'MyVideos' , 'Textures' , 'TV' , 'ViewModes' ] :
  Ii1i1iI1iIIi = glob . glob ( os . path . join ( iI111I11I1I1 , '%s*.db' % DB ) )
  O0OOoooO = '%s(.+?).db' % DB [ 1 : ]
  IIiiIiIIiI1 = 0
  for file in Ii1i1iI1iIIi :
   try : I1IiI = int ( re . compile ( O0OOoooO ) . findall ( file ) [ 0 ] )
   except : I1IiI = 0
   if IIiiIiIIiI1 < I1IiI :
    IIiiIiIIiI1 = I1IiI
  return '%s%s.db' % ( DB , IIiiIiIIiI1 )
 else : return False
 if 79 - 79: OOooOOo + o0O00o
def oOOo ( path ) :
 oOoOooO ( "Deleting Folder: %s" % path , xbmc . LOGNOTICE )
 try : shutil . rmtree ( path , ignore_errors = True , onerror = None )
 except : return False
 if 14 - 14: o0O0Oooo0O / iIII - IIIi11I1 * o0o00Oo0O % o0O00o . o0o00Oo0O
def o0OoOOoooooOO ( name ) :
 if 86 - 86: ooOoO0O00 * ii
 if 22 - 22: o0O0Oooo0O + IIIIiiII111 - iIII + iI11I1II1I1I / o0O0Oooo0O - ii
 if 42 - 42: ii - OOooOOo - IIIi11I1 * o0O0Oooo0O
 oOoOooO ( 'Purging DB %s.' % name , xbmc . LOGNOTICE )
 if os . path . exists ( name ) :
  try :
   OO0iii111 = database . connect ( name )
   o00O000oooOo = OO0iii111 . cursor ( )
  except Exception , I1iI1I1I1i11i :
   oOoOooO ( "DB Connection Error: %s" % str ( I1iI1I1I1i11i ) , xbmc . LOGERROR )
   return False
 else : oOoOooO ( '%s not found.' % name , xbmc . LOGERROR ) ; return False
 o00O000oooOo . execute ( "SELECT name FROM sqlite_master WHERE type = 'table'" )
 for O0o00oO0o0 in o00O000oooOo . fetchall ( ) :
  if O0o00oO0o0 [ 0 ] == 'version' :
   oOoOooO ( 'Data from table `%s` skipped.' % O0o00oO0o0 [ 0 ] , xbmc . LOGDEBUG )
  else :
   try :
    o00O000oooOo . execute ( "DELETE FROM %s" % O0o00oO0o0 [ 0 ] )
    OO0iii111 . commit ( )
    oOoOooO ( 'Data from table `%s` cleared.' % O0o00oO0o0 [ 0 ] , xbmc . LOGDEBUG )
   except Exception , I1iI1I1I1i11i : oOoOooO ( "DB Remove Table `%s` Error: %s" % ( O0o00oO0o0 [ 0 ] , str ( I1iI1I1I1i11i ) ) , xbmc . LOGERROR )
 o00O000oooOo . close ( )
 oOoOooO ( '%s DB Purging Complete.' % name , xbmc . LOGNOTICE )
 o00iIIiIi111iI = name . replace ( '\\' , '/' ) . split ( '/' )
 o0Oooo ( "[COLOR %s]Purge Database[/COLOR]" % o0OoOO , "[COLOR %s]%s Complete[/COLOR]" % ( O0O0Oo00 , o00iIIiIi111iI [ len ( o00iIIiIi111iI ) - 1 ] ) )
 if 42 - 42: ii * IIiIiII11i
def OOoOooOOOo0Ooo0o00o ( path ) :
 oOoOooO ( "Deleting File: %s" % path , xbmc . LOGNOTICE )
 try : os . remove ( path )
 except : return False
 if 53 - 53: o0O0Oooo0O + ooOoO0O00 . oO0o / Ii + Ii1i1i % OOooOOo
 if 9 - 9: oOOoOooOo . iIII - I1ii11iIi11i . o0O0Oooo0O
def oO0000 ( ) :
 i1I111II11 = os . path . join ( oooOOOOO , 'addon_data' )
 o00oO = [
 ( os . path . join ( oo0o0O00 , 'plugin.video.phstreams' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.bob' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.specto' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.genesis' , 'cache.db' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.exodus' , 'cache.db' ) ) ,
 ( os . path . join ( iI111I11I1I1 , 'onechannelcache.db' ) ) ,
 ( os . path . join ( iI111I11I1I1 , 'saltscache.db' ) ) ,
 ( os . path . join ( iI111I11I1I1 , 'saltshd.lite.db' ) ) ]
 I11ii111i = [
 ( i1I111II11 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( i1I111II11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( i1I111II11 , 'plugin.video.itv' , 'Images' ) ) ]
 if 2 - 2: ooOO0O0ooOooO * ooOO0O0ooOooO . OOooOOo * Ii1i1i * iI11I1II1I1I
 OOOIIIIiiIi = 0
 if 13 - 13: iIII / o0o00Oo0O . Ii * ooOoO0O00 % Ii
 for IIi1IIIi in I11ii111i :
  if os . path . exists ( IIi1IIIi ) and not IIi1IIIi in [ oo0o0O00 , i1I111II11 ] :
   OOOIIIIiiIi = OO000oo0o ( IIi1IIIi , OOOIIIIiiIi )
  else :
   for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( IIi1IIIi ) :
    for ooIii in oOOoo0 :
     if 'cache' in ooIii . lower ( ) and not ooIii . lower ( ) == 'meta_cache' : OOOIIIIiiIi = OO000oo0o ( os . path . join ( iIi1Iii1 , ooIii ) , OOOIIIIiiIi )
     if 87 - 87: ii
 return OOOIIIIiiIi
def OO000oo0o ( path , total = 0 ) :
 for iiI1Oo , IIIOO00O , ooiI1i in os . walk ( path ) :
  for OOo0O0oo0OO0O in ooiI1i :
   O0ooOOo00o0oO0O0 = os . path . join ( iiI1Oo , OOo0O0oo0OO0O )
   total += os . path . getsize ( O0ooOOo00o0oO0O0 )
 return total
def IIiIIiIi1II1IiI ( num , suffix = 'B' ) :
 for o0O0O in [ '' , 'K' , 'M' , 'G' ] :
  if abs ( num ) < 1024.0 :
   return "%3.02f %s%s" % ( num , o0O0O , suffix )
  num /= 1024.0
 return "%.02f %s%s" % ( num , 'G' , suffix )
 if 50 - 50: oOOoOooOo / Ii1I / I1ii11iIi11i . OOooOOo + o0O0Oooo0O
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
 if 85 - 85: o0O00o + iI11I1II1I1I + oO0o % iI11I1II1I1I . oOOoOooOo / ooOO0O0ooOooO
 if 40 - 40: Ii1i1i
def oooOoOoOo ( ) :
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
 if 96 - 96: OOooOOo / oO0o % ii * oOOoOooOo
def oOo00 ( ) :
 OOooOoooOoOo ( )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']My Local Zip[/COLOR]' , II , 48 , iiiiiIIii + 'MyLocalZIP.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']My Online Zip[/COLOR]' , iiI1IiI , 43 , iiiiiIIii + 'MyOnlineZip.png' , iIi1ii1I1 , '' )
 if 6 - 6: oOo0O0Ooo . IIiIiII11i + o0O0Oooo0O / oO0o % oOo0O0Ooo . ii
def Oooo000 ( ) :
 OOooOoooOoOo ( )
 oOOOoo0O0oO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( iI1iIIiiii ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiiiiIIii + 'FTV4.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( iI1iIIiiii ) + '/wizard/customftv/settings.xml' , 17 , iiiiiIIii + 'FTV3.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiiiiIIii + 'FTV1.png' , iIi1ii1I1 , '' )
 oOOOoo0O0oO ( 'RESET FTV DATABASE' , 'url' , 18 , iiiiiIIii + 'FTV2.png' , iIi1ii1I1 , '' )
 if 37 - 37: oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * oOOoOooOo * Ii1i1i
 if 56 - 56: ii / oOo0O0Ooo . oOOoOooOo - ooOoO0O00
 if 60 - 60: OOooOOo % OOooOOo
def I1I ( ) :
 OOooOoooOoOo ( )
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']SKINS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II11iiii1Ii + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  i11iI11ii ( )
 if OoOOo0OOoO == 0 :
  oOo0 ( Oo0o00OO0000 )
 if OoOOo0OOoO == 0 :
  ii1II ( Oo0o00OO0000 )
  if 83 - 83: Ii1I * iIII . ii % Ii1i1i
  if 29 - 29: IIIIiiII111 + IIiIiII11i . Ii . Ii1i1i - o0o00Oo0O
  if 47 - 47: ooOO0O0ooOooO . Ii1I - iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 13 - 13: o0O00o . I1ii11iIi11i - iIII / ooOO0O0ooOooO - I1ii11iIi11i - oOo0O0Ooo
def oOO0o ( ) :
 I1I1IiI1 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 Ii1i1iI1iIIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( I1I1IiI1 )
 for iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iII11 , iII11 , '' )
 OOoOO0o0o0 ( 'tvshows' , 'INFO' )
 if 72 - 72: o0o00Oo0O
def i1i11II1 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( IIIi11Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 92 - 92: ooOO0O0ooOooO / Ii1I
def i11iI11ii ( ) :
 OOooOoooOoOo ( )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']GOTHAM SKINS[/COLOR]' , str ( iI1iIIiiii ) , 36 , iiiiiIIii + 'GothamSkins.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']HELIX SKINS[/COLOR]' , str ( iI1iIIiiii ) , 37 , iiiiiIIii + 'HelixSkins.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiiiiIIii + 'IsengaardSkins.png' , iIi1ii1I1 , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 6 - 6: Ii / ooOoO0O00 / o0O00o . oOo0O0Ooo - IIIi11I1 % Ii
def o0OoOoOo0O ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 37 - 37: ooOoO0O00 . o0O0Oooo0O - IIiIiII11i % I11i - ooOoO0O00 . ooOO0O0ooOooO
def iiiiI ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + Ooo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 21 - 21: IIIIiiII111 % o0O00o % I1ii11iIi11i % o0o00Oo0O
def OoOoooOO00OO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + OO000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 1 - 1: o0o00Oo0O
def iIOOO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 98 - 98: IIiIiII11i + IIiIiII11i - iI11I1II1I1I . OOooOOo . o0O0Oooo0O
def oOo0 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + OO0Ooo0O00ooOo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 40 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 40 - 40: oO0o . ii + Ii
def O000oo00o000o ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + O0000ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 83 - 83: o0O0Oooo0O + I11i % ooOO0O0ooOooO / oO0o
def ooO0O00Oo0o ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']GenieTv Apps[/COLOR]' , '[COLOR' + II11iiii1Ii + ']APK Factory[/COLOR]' , '[COLOR' + II11iiii1Ii + ']APK Search[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']APK TOOL[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  o0o000O0ooo0O ( )
 if OoOOo0OOoO == 1 :
  I1I11iII11 ( )
 if OoOOo0OOoO == 2 :
  O0O000OOOoO ( )
  if 95 - 95: Ii1i1i % oOo0O0Ooo + I1ii11iIi11i * I11i * IIIIiiII111
  if 22 - 22: Ii1i1i + ooOO0O0ooOooO . OOooOOo
  if 84 - 84: Ii / I11i % iI11I1II1I1I . oOOoOooOo . oO0o / IIIIiiII111
  if 55 - 55: IIIIiiII111
def I1I11iII11 ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , ii1iIII1iIiIIIIi in Ii1i1iI1iIIi :
  I111I11I111 ( 'Android Apps' + ii1iIII1iIiIIIIi , 'https://www.apkfiles.com' + Oo0o00OO0000 , 30035 , iiiiiIIii + 'apps.png' )
 for Oo0o00OO0000 , ii1iIII1iIiIIIIi in I1Ii :
  I111I11I111 ( 'Android Games' + ii1iIII1iIiIIIIi , 'https://www.apkfiles.com' + Oo0o00OO0000 , 30035 , iiiiiIIii + 'GAMES.png' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def ii11IoOO0OooO0O ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '/cat' in url :
   I111I11I111 ( ( iiIiii1IIIII ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiiiiIIii + 'APK.png' )
def o00O0o0oo0 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '/app' in url :
   I111I11I111 ( ( iiIiii1IIIII ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiiiiIIii + 'APK.png' )
def ooo000 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 oOO0 = url
 if "page=" in str ( url ) :
  oOO0 = url . split ( '?' ) [ 0 ]
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'apk' in url :
   oOOOoo0O0oO ( ( iiIiii1IIIII ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + iII11 )
 if len ( I1Ii ) > 1 :
  I1Ii = str ( I1Ii [ len ( I1Ii ) - 1 ] )
 oOOOoo0O0oO ( 'Next Page' , oOO0 + str ( I1Ii ) , 30037 , iiiiiIIii + 'Next.png' )
def I1I1IiI ( name , url ) :
 O0o0O0 = o00oiii11II1I ( url )
 name = name
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  url = 'https://www.apkfiles.com' + url
  ooooooo0oOo0 ( name , url , 'Brackets' )
def O0O000OOOoO ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'https://www.apkfiles.com/search?q=' + ( IIIIIiII1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 OoO00oo00 = i1iIIIiiiI . lower ( )
 ooo000 ( OoO00oo00 )
 if 81 - 81: Ii % oOo0O0Ooo / IIIIiiII111 % oO0o / o0O0Oooo0O % iI11I1II1I1I
def IIII1iI1IiIiI ( url ) :
 I1iI = xbmc . translatePath ( os . path . join ( i1II1 , 'Download' ) )
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
 if 91 - 91: ii . IIIi11I1 - oOOoOooOo + IIiIiII11i + Ii1i1i . ii
def Iii1iiIIi1i111i ( url ) :
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
 if 48 - 48: I1ii11iIi11i . I11i - IIIIiiII111
 if 15 - 15: I11i
def o0Oo00Oo ( name , url , description ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IIIIiIiIi1 = os . path . join ( I1iI , name )
 try :
  os . remove ( IIIIiIiIi1 )
 except :
  pass
 downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
 i11i11I = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print i11i11I
 print '======================================='
 extract . all ( IIIIiIiIi1 , i11i11I , o0oOoO00o )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 61 - 61: iI11I1II1I1I % Ii1i1i - ooOO0O0ooOooO * ii % IIiIiII11i - Ii1i1i
 if 44 - 44: o0o00Oo0O
 if 9 - 9: ooOO0O0ooOooO . I1ii11iIi11i + IIIIiiII111 + oOo0O0Ooo * oOo0O0Ooo - oOo0O0Ooo
 if 95 - 95: o0O00o + IIIi11I1 % ooOO0O0ooOooO * IIIi11I1
 if 58 - 58: OOooOOo . I11i + ooOO0O0ooOooO
def o0o000O0ooo0O ( ) :
 I1I1IiI1 = i11oO0oOo0 ( iIii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , Oo0o00OO0000 , iI1III1iIi11 , ooo0O0o00O , iiIi1 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , Oo0o00OO0000 , 80003 , iI1III1iIi11 , iiiiiIIii + 'APKToolsB.png' , iiIi1 )
def Oo0OOo ( apk , ret = None ) :
 if apk == "kodi" :
  I1i1i1IIi1I = "https://kodi.tv/download/"
  I1I1IiI1 = i11oO0oOo0 ( I1i1i1IIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  Ii1i1iI1iIIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( I1I1IiI1 )
  if len ( Ii1i1iI1iIIi ) == 1 :
   IIi11iIIiIiI = Ii1i1iI1iIIi [ 0 ] [ 0 ]
   oOO0ooIiIIi1I1I11Ii = Ii1i1iI1iIIi [ 0 ] [ 1 ]
   oo000oo00 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( IIi11iIIiIiI , oOO0ooIiIIi1I1I11Ii )
  if ret == 'version' : return IIi11iIIiIiI
  else : return oo000oo00
 elif apk == "spmc" :
  IiIiiI1II = 'https://github.com/koying/SPMC/releases/latest/'
  I1I1IiI1 = i11oO0oOo0 ( IiIiiI1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  Ii1i1iI1iIIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( I1I1IiI1 )
  IIi11iIIiIiI = re . sub ( '<[^<]+?>' , '' , Ii1i1iI1iIIi [ 0 ] ) . replace ( ' ' , '' )
  oo000oo00 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( IIi11iIIiIiI , IIi11iIIiIiI )
  if ret == 'version' : return IIi11iIIiIiI
  else : return oo000oo00
def ooooooo0oOo0 ( name , url , Brackets ) :
 if iIII1I111III ( ) == 'android' :
  iI1ioo000o0O = O0OoO000O0OO . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iI1ioo000o0O : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iiIiIIiI1 = name
  if iI1ioo000o0O :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not oOo00O000Oo0 ( url ) == True : o0Oooo ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iiIiIIiI1 , '' , 'Please Wait' )
   IIIIiIiIi1 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( IIIIiIiIi1 )
   except : pass
   downloader . download ( url , IIIIiIiIi1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    o00O = zipfile . ZipFile ( IIIIiIiIi1 )
    for file in o00O . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as OOo0O0oo0OO0O :
       Ii11i = file . split ( '/' ) [ 1 ]
       OOo0O0oo0OO0O . write ( o00O . read ( file ) )
       xbmc . sleep ( 500 )
       OOo0O0oo0OO0O . close ( )
       try :
        os . remove ( IIIIiIiIi1 )
       except :
        pass
       IIIIiIiIi1 = os . path . join ( i1iIIi1 , Ii11i )
   O0OoO000O0OO . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IIIIiIiIi1 + '")' )
  else : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0Oooo ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 62 - 62: iIII . IIiIiII11i * o0o00Oo0O + ooOoO0O00 * ii + ii
 if 23 - 23: ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / iIII . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - o0O00o
def IiII1II1 ( ) :
 if not os . path . exists ( OOooO0OOoo ) : os . makedirs ( OOooO0OOoo )
 I1I1IiI1 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( I1I1IiI1 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  Oo0o00OO0000 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + Oo0o00OO0000 )
  O0ooOo ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) , Oo0o00OO0000 )
  if 30 - 30: OOooOOo - Ii
def O0ooOo ( name , url ) :
 if iIII1I111III ( ) == 'android' :
  iI1ioo000o0O = O0OoO000O0OO . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iI1ioo000o0O : o0Oooo ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iiIiIIiI1 = name
  if iI1ioo000o0O :
   if not os . path . exists ( OOooO0OOoo ) : os . makedirs ( OOooO0OOoo )
   if not oOo00O000Oo0 ( url ) == True : o0Oooo ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iiIiIIiI1 , '' , 'Please Wait' )
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
 if 94 - 94: OOooOOo % IIIIiiII111
 if 39 - 39: OOooOOo + o0O0Oooo0O % o0o00Oo0O
def i1Ii1I ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( iI1iIIiiii + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'INFO' )
 if 60 - 60: oOOoOooOo * Ii1i1i + o0O0Oooo0O . IIIi11I1 . o0o00Oo0O
 if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
def iI1 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( iI1iIIiiii + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 30015 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 66 - 66: o0O0Oooo0O * I11i / o0O00o * IIIIiiII111 / ii
def o0o ( url , iconimage , fanart ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 iIi1Ii1111i = url
 iII11 = iconimage
 fanart = fanart
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( I1I1IiI1 )
 for Oo0Oo0O , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '.mp4' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Watch VIDEO' , url + '/' + Oo0Oo0O , 222 , iII11 , fanart , '' )
  if 'description' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Read Description' , url + '/' + Oo0Oo0O , 30017 , iII11 , fanart , '' )
  if 'images' in iiIiii1IIIII :
   OoOOoOooooOOo ( 'View Images' , url + '/' + Oo0Oo0O , 30018 , iII11 , fanart , '' )
  if 'url' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Install Build On Android' , url + '/' + Oo0Oo0O , 30016 , iII11 , fanart , '' )
  if 'url' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'Install Build On Pc' , url + '/' + Oo0Oo0O , 30019 , iII11 , fanart , '' )
 OOoOO0o0o0 ( 'movies' , 'INFO' )
 if 13 - 13: iIII % o0O0Oooo0O . ooOoO0O00
def IIiIiiiii11 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'url="([^"]*)"' ) . findall ( I1I1IiI1 )
 for url in Ii1i1iI1iIIi :
  oooo ( url )
  if 65 - 65: I1ii11iIi11i . OOooOOo . IIIi11I1 % I11i + oO0o
def OOO000OOOO0oO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'url="([^"]*)"' ) . findall ( I1I1IiI1 )
 for url in Ii1i1iI1iIIi :
  iIIIiiiII ( url )
  if 15 - 15: iIII % oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
def oo000o ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'desc="([^"]*)"' ) . findall ( I1I1IiI1 )
 for I1111i1 in Ii1i1iI1iIIi :
  I1iI1ii1II ( 'Description:' , I1111i1 )
  if 6 - 6: IIIi11I1 + Ii1I + I1ii11iIi11i
def o0OOo0o0o0ooo ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( url )
 url = url
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1I1IiI1 )
 for Oo0Oo0O , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'png' in iiIiii1IIIII :
   oOOOoo0O0oO ( 'image' , '' , '' , url + '/' + Oo0Oo0O , url + '/' + Oo0Oo0O , '' )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 53 - 53: oO0o
def oooOoOO0o ( name , url , description ) :
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
 if 78 - 78: o0o00Oo0O - o0O0Oooo0O * IIIi11I1 + iIII + IIiIiII11i
 if 15 - 15: I1ii11iIi11i . Ii + oOOoOooOo / Ii1I / IIIIiiII111 + ii
def iIIIiiiII ( url ) :
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
 ooo0oOoO00Oo ( )
 if 46 - 46: oOOoOooOo - oOOoOooOo * Ii1I / IIIIiiII111 * IIIi11I1 / I11i
def oooo ( url ) :
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
 ooo0oOoO00Oo ( )
 if 67 - 67: IIIi11I1 - Ii1i1i % IIIIiiII111 / IIiIiII11i + oOo0O0Ooo * oOOoOooOo
def o0o0O0o0O ( name , url , description ) :
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
 ooo0oOoO00Oo ( )
 if 16 - 16: I11i
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
  IiiiI1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOo0O0oo0OO0O . write ( IiiiI1i . rstrip ( '\r\n' ) + '\n' )
def oOoOooO ( msg , level = xbmc . LOGDEBUG ) :
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
  I1iIi1i = getS ( 'nextcleandate' ) if not getS ( 'nextcleandate' ) == '' else str ( TODAY )
  if CLEANWIZLOG == 'true' and I1iIi1i <= str ( TODAY ) : checkLog ( )
  with open ( oO , 'a' ) as OOo0O0oo0OO0O :
   IiiiI1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , msg )
   OOo0O0oo0OO0O . write ( IiiiI1i . rstrip ( '\r\n' ) + '\n' )
def ooo0oOoO00Oo ( ) :
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
  if 24 - 24: oOOoOooOo + oO0o - IIiIiII11i * ii - oOo0O0Ooo . I1ii11iIi11i
  if 9 - 9: Ii1i1i
  if 1 - 1: o0o00Oo0O + IIIIiiII111 * oOOoOooOo - Ii
def ii1II ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( url ) :
  for file in II1OOO :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOoO00o = open ( ( os . path . join ( iIi1Iii1 , file ) ) ) . read ( )
    iI11IIi1iiI1I = oOoO00o . replace ( oOo0oooo00o , 'special://home/' )
    OOo0O0oo0OO0O = open ( ( os . path . join ( iIi1Iii1 , file ) ) , mode = 'w' )
    OOo0O0oo0OO0O . write ( str ( iI11IIi1iiI1I ) )
    OOo0O0oo0OO0O . close ( )
 ooo0oOoO00Oo ( )
 if 83 - 83: I1ii11iIi11i / oOOoOooOo
def oo0o0000 ( ) :
 I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiiiiIIii + 'RadioNomy.png' )
 I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiiiiIIii + 'RadioNomy.png' )
 I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']SEARCH[/COLOR]' ) , '' , 70006 , iiiiiIIii + 'RadioNomy.png' )
 if 11 - 11: I11i - IIiIiII11i % ooOO0O0ooOooO . IIiIiII11i
def OO0I11IIi1I1 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiiiiIIii + 'RadioNomy.png' )
def Iiiii ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiiiiIIii + 'RadioNomy.png' )
def IiIi1I1IiI1II1 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in I1Ii :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']Filter - ' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiiiiIIii + 'RadioNomy.png' )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']Stream - ' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iII11 )
def iii1 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
def iII1iii ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1
 o0O0o = 'https://www.radionomy.com/en/search/index?query=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 oO0000OOo00 = i11oO0oOo0 ( o0O0o )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']Stream - ' + iiIiii1IIIII + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + Oo0o00OO0000 , 70005 , iII11 )
  if 79 - 79: OOooOOo + iI11I1II1I1I * ooOoO0O00 * oOOoOooOo - iIII * oO0o
  if 78 - 78: IIIIiiII111 % Ii + IIIIiiII111 + I11i
def Oo0o0OoOoOo0 ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.listenlive.eu/' + Oo0o00OO0000 , 10111113 , iiiiiIIii + 'WorldRadio.png' , iiiiiIIii + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def oo0OoOO000O ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 if 22 - 22: iIII - I11i
 if 54 - 54: ooOO0O0ooOooO * oO0o - IIIIiiII111 * iIII + I11i - Ii1i1i
 Ii1i1iI1iIIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , iI1I11 , url , OoOOIi in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' [COLORorangered] ' + OoOOIi + '[/COLOR]' , url , 222225 , iiiiiIIii + 'WorldRadio.png' , iiiiiIIii + 'WorldRadio.png' , '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[CR]' + iI1I11 + '[CR]' + OoOOIi + '[/COLOR]' )
  if 91 - 91: I11i / Ii
def oO00o0 ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.toonjet.com/' + Oo0o00OO0000 , 8051 , iiiiiIIii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def o00OoOo0 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
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
   I111I11I111 ( ( iII11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiiiiIIii + 'vod.png' )
 for url in I1Ii :
  I111I11I111 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiiiiIIii + 'Next.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Iii1I ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiiiiIIii + 'classictoons.png' )
  if 33 - 33: IIIi11I1 / ooOO0O0ooOooO . Ii * iI11I1II1I1I
  if 75 - 75: IIIi11I1 - oO0o
def oo0 ( ) :
 iiiI1ii ( 'Audio Books' , '' , 30011 , iiiiiIIii + 'AudioBooks.png' , iiiiiIIii + 'AudioBooks.png' , '' )
 iiiI1ii ( 'Kids Audio Books' , '' , 30006 , iiiiiIIii + 'KidsAudioBooks.png' , iiiiiIIii + 'KidsAudioBooks.png' , '' )
 if 31 - 31: o0o00Oo0O - o0O00o * Ii * ooOoO0O00
def O0oOo00Oo0oo0 ( ) :
 iiiI1ii ( 'All' , '' , 30001 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 iiiI1ii ( 'Popular' , '' , 30012 , iiiiiIIii + 'POPULARv.png' , iiiiiIIii + 'POPULARv.png' , '' )
 iiiI1ii ( 'Search' , '' , 30013 , iiiiiIIii + 'Search.png' , iiiiiIIii + 'Search.png' , '' )
 if 36 - 36: o0O0Oooo0O / o0O0Oooo0O % ooOO0O0ooOooO
def OoOO0o00OOO0o ( ) :
 oO0000OOo00 = i11oO0oOo0 ( I1IIiiIiii + 'books' + I11iii1Ii )
 Ii1i1iI1iIIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , Oo0o00OO0000 , OoO0 in Ii1i1iI1iIIi :
  if 'Parent' in iiIiii1IIIII :
   pass
  elif '2' in OoO0 :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 75 - 75: oOOoOooOo
def II1IIiiIiI11 ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( I1IIiiIiii + 'books' + I11iii1Ii )
 Ii1i1iI1iIIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , Oo0o00OO0000 , OoO0 in Ii1i1iI1iIIi :
  if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
   if '1' in OoO0 :
    iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   elif '2' in OoO0 :
    iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   elif '3' in OoO0 :
    iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30009 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
    if 65 - 65: oOOoOooOo * o0o00Oo0O * IIIIiiII111
    if 60 - 60: iI11I1II1I1I . oOOoOooOo + oOo0O0Ooo % ooOO0O0ooOooO
def Ii1i1 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( I1IIiiIiii + 'books' + I11iii1Ii )
 Ii1i1iI1iIIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , Oo0o00OO0000 , OoO0 in Ii1i1iI1iIIi :
  if '1' in OoO0 :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 3010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif '2' in OoO0 :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif '3' in OoO0 :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Oo0o00OO0000 , 30009 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 6 - 6: iI11I1II1I1I * IIiIiII11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: oOo0O0Ooo
def iiiii1i1 ( url ) :
 Oo0Oo0O = url
 oO0000OOo00 = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in I1Ii :
  if 'mp3' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) , Oo0Oo0O + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) , Oo0Oo0O + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) , Oo0Oo0O + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif '/' in iiIiii1IIIII :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Oo0Oo0O + url , 30009 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: o0O00o - o0o00Oo0O + oOo0O0Ooo / ii * IIIIiiII111 / ooOoO0O00
   if 28 - 28: I11i - IIIIiiII111 * Ii1I - IIiIiII11i % IIiIiII11i - o0O00o
   if 76 - 76: o0O0Oooo0O
def Iii1IiIIiII1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Oo0Oo0O = url
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
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Oo0Oo0O + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Oo0Oo0O + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  else :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Oo0Oo0O + url , 30010 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: Ii1I - o0O00o
   if 64 - 64: ooOoO0O00
def o0O0oOo00oOoo ( ) :
 iiiI1ii ( 'A-Z' , '' , 30007 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 iiiI1ii ( 'All' , '' , 30003 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 iiiI1ii ( 'Search' , '' , 30014 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
 if 67 - 67: oOo0O0Ooo - oO0o
def Oo0oO ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 in Ii1i1iI1iIIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + Oo0o00OO0000 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iII11 :
   pass
  else :
   iiiI1ii ( iII11 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( Oo0o00OO0000 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iII11 + '.gif' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 65 - 65: oO0o * IIiIiII11i / iI11I1II1I1I
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: IIIi11I1 . Ii . iIII * iIII
 if 69 - 69: ooOoO0O00
def O00oooo00 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '</a>' in iiIiii1IIIII :
   pass
  elif '(' in iiIiii1IIIII :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  else :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: IIIi11I1 + IIIi11I1
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
def OO0OoOo00 ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
   if '</a>' in iiIiii1IIIII :
    pass
   elif '(' in iiIiii1IIIII :
    iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30005 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   else :
    OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30004 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
    if 75 - 75: iI11I1II1I1I / IIiIiII11i / Ii1i1i / OOooOOo
    if 77 - 77: OOooOOo
def i111 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '</a>' in iiIiii1IIIII :
   pass
  elif '(' in iiIiii1IIIII :
   iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30005 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
  else :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Oo0o00OO0000 , 30004 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 27 - 27: iI11I1II1I1I + ooOO0O0ooOooO % I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: iI11I1II1I1I - I1ii11iIi11i / o0o00Oo0O / o0O00o
 if 52 - 52: o0o00Oo0O + oOOoOooOo
def Ii111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  Oo0Oo0O = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( Oo0Oo0O )
  if 58 - 58: ooOO0O0ooOooO * Ii * oOo0O0Ooo * Ii1I % Ii - ii
def ii1II11IIII ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '<p align' in iiIiii1IIIII :
   pass
  elif '&nbsp;' in iiIiii1IIIII :
   pass
  else :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiiiiIIii + 'KodibleAudioBooks.png' , iiiiiIIii + 'KodibleAudioBooks.png' , '' )
   if 90 - 90: I1ii11iIi11i * Ii1i1i
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: Ii1I + iI11I1II1I1I % o0O00o
 if 24 - 24: oO0o / o0o00Oo0O * oOOoOooOo % iI11I1II1I1I + ooOoO0O00 % o0o00Oo0O
def I1I11i ( ) :
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
def OoO ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 Oo0o0O0OOOo0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0000OOo00 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iII11 , iII11 , iiIiii1IIIII )
 for url , iiIiii1IIIII in Oo0o0O0OOOo0 :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 21005 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 for url in next :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 21005 , iiiiiIIii + 'Next.png' , '' , '' )
def OOoo ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 o0oO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 OO000oOoOo000 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0000OOo00 )
 o0O0o0ooo0 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 for url in OO000oOoOo000 :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 for url , iiIiii1IIIII in o0oO :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
 else :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
def iIo0O000O00o ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'watchcartoons.png' , '' , '' )
  if 38 - 38: ii . IIIIiiII111
def iiII11 ( ) :
 oO0000OOo00 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 Ii1i1iI1iIIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '9cart' in Oo0o00OO0000 :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 20001 , iiiiiIIii + 'ORIGINCARTOON.png' )
   if 89 - 89: Ii1I * Ii1I * OOooOOo / IIIIiiII111
def OOo0i111ii1Ii ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 II1iIi1IiIii = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if '9cart' in url :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']ALL[/COLOR]' , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
 for url in I1Ii :
  if '9cart' in url :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']123[/COLOR]' , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
 for url , iiIiii1IIIII in II1iIi1IiIii :
  if '9cart' in url :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
   if 59 - 59: o0o00Oo0O . I11i % Ii1I * ooOO0O0ooOooO + iIII
def o00oIiIiIiiI ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 20003 , iII11 )
 for url , iiIiii1IIIII in I1Ii :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiiiiIIii + 'ORIGINCARTOON.png' )
  if 83 - 83: OOooOOo
def o0ooOOOo0O0 ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'Watch' in url :
   I111I11I111 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiiiiIIii + 'ORIGINCARTOON.png' )
   if 100 - 100: Ii . IIIi11I1 . Ii
def o00Oo ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 20005 , iiiiiIIii + 'ORIGINCARTOON.png' )
  if 20 - 20: Ii1i1i . I1ii11iIi11i - iIII % iIII - oOo0O0Ooo * IIIi11I1
def OooOo ( url ) :
 url = cloudflare . source ( url )
 II11IiI1 ( url )
 if 67 - 67: I11i / ii % IIiIiII11i % ooOO0O0ooOooO
def iIIi ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . recompile ( 'src="([^"]*)"' )
 for url in Ii1i1iI1iIIi :
  II11IiI1 ( url )
  if 25 - 25: I1ii11iIi11i + I11i - oO0o
  if 57 - 57: IIiIiII11i . ooOoO0O00
def I11Ii1 ( url , name ) :
 url = url ; name = name
 oO0O = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oO0O . clear ( )
 OOOoooooO0oOOoO = [ ]
 I1I1oOoooo0OooO = [ ]
 iiiI1i11Ii = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iiiI1i11Ii )
 for iII11 in I1Ii :
  OooO0O = iII11
 II1iIi1IiIii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iiiI1i11Ii )
 for Oo0o , O0OO0 in II1iIi1IiIii :
  OOOoooooO0oOOoO . append ( [ Oo0o , O0OO0 ] )
  if len ( OOOoooooO0oOOoO ) == len ( II1iIi1IiIii ) :
   for IIi1IIIi in OOOoooooO0oOOoO :
    OOI1i11i = random . randint ( 1 , len ( OOOoooooO0oOOoO ) )
    try :
     iiiI1I = OOOoooooO0oOOoO [ int ( OOI1i11i ) ]
     if iiiI1I [ 1 ] not in I1I1oOoooo0OooO :
      I1I1oOoooo0OooO . append ( iiiI1I [ 1 ] )
      Iiio0Oo0oO = i11oO0oOo0 ( iiiI1I [ 0 ] )
      iI111i11iI1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Iiio0Oo0oO )
      for OOOOo0o0O0 , I1I1i1 in iI111i11iI1 :
       if 'easy' in I1I1i1 :
        Ii1Ii = i11oO0oOo0 ( I1I1i1 )
        III1ii = re . compile ( 'file: "(.+?)"' ) . findall ( Ii1Ii )
        for iIIOOoOOooO in III1ii :
         if 'http' in iIIOOoOOooO :
          I1I1 = xbmcgui . ListItem ( iiiI1I [ 1 ] , iconImage = OooO0O , thumbnailImage = OooO0O )
          I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : iiiI1I [ 1 ] } )
          I1I1 . setProperty ( "IsPlayable" , "true" )
          oO0O . add ( iIIOOoOOooO , I1I1 )
          xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1 )
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
   if 33 - 33: o0O00o * iIII
def OO0oOOOOO ( url ) :
 oO0O = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oO0O . clear ( )
 OoOo = [ ]
 oO0i1ii1i1 = [ ]
 iiI1iiiii = [ ]
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oO0i1ii1i1 . append ( [ url , iiIiii1IIIII ] )
  if len ( oO0i1ii1i1 ) == len ( Ii1i1iI1iIIi ) :
   for IIi1IIIi in oO0i1ii1i1 :
    OOoOO = random . randint ( 1 , len ( oO0i1ii1i1 ) )
    try :
     OOo00OOoOOO = oO0i1ii1i1 [ int ( OOoOO ) ]
    except :
     pass
    if OOo00OOoOOO [ 1 ] not in iiI1iiiii :
     iiI1iiiii . append ( OOo00OOoOOO [ 1 ] )
     if int ( len ( OoOo ) ) < 1 :
      OoOo . append ( OOo00OOoOOO [ 1 ] [ 0 ] )
      I11Ii1 ( OOo00OOoOOO [ 0 ] , OOo00OOoOOO [ 1 ] )
     else :
      pass
    else :
     pass
  else :
   pass
   if 10 - 10: o0O00o % I11i / iIII + ooOO0O0ooOooO % oOo0O0Ooo % OOooOOo
def ii1ii1iii1I ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = o0
 I1 = sys . argv [ 0 ]
 I1 += '?mode=' + str ( mode )
 I1 += '&title=' + urllib . quote_plus ( name )
 I1 += '&image=' + urllib . quote_plus ( image )
 I1 += '&page=' + str ( page )
 if url != '' :
  I1 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  I1 += '&keyword=' + urllib . quote_plus ( keyword )
 I1I1 = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  I1I1 . addContextMenuItems ( contextMenu )
 if infoLabels :
  I1I1 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  I1I1 . setProperty ( "IsPlayable" , "true" )
 I1I1 . setProperty ( 'Fanart_Image' , iIi1ii1I1 )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = isFolder )
 if 21 - 21: o0o00Oo0O * Ii * ii
def iiii1I1IiI ( ) :
 II1I11i = i11 ( 'http://www.animetoon.org/cartoon' )
 O0o0O0 = i11oO0oOo0 ( II1I11i )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="(.+?)">(.+?)</a></td>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  ii1ii1iii1I ( iiIiii1IIIII , 9110012 , url = Oo0o00OO0000 , image = o0 , isFolder = False )
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 97 - 97: oOo0O0Ooo
def oo000oO ( ) :
 II1I11i = i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Cartoons[/COLOR]' , '' , 10004 , iiiiiIIii + 'ORIGINCARTOON.png' , iIi1ii1I1 , '' )
 Iii ( '[COLOR' + II11iiii1Ii + ']24/7 Select Cartoon[/COLOR]' , '' , 9110011 , o0 , iIi1ii1I1 , '' , '' )
 ii1ii1iii1I ( '[COLOR' + II11iiii1Ii + ']24/7 Random Cartoon[/COLOR]' , 9110010 , url = II1I11i , image = o0 , isFolder = False )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search Cartoons[/COLOR]' , '' , 10005 , iiiiiIIii + 'ORIGINCARTOON.png' , iIi1ii1I1 , '' )
 if 56 - 56: Ii1i1i * ooOoO0O00 + o0O0Oooo0O * I11i % oO0o
def OoOo0000o0OOo ( ) :
 II1I11i = i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( II1I11i )
 if 22 - 22: iI11I1II1I1I - I1ii11iIi11i . Ii % IIIIiiII111
 Ii1i1iI1iIIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0000OOo00 )
 if 51 - 51: o0o00Oo0O - Ii1I / iIII * IIiIiII11i + oO0o % Ii1I
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
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
    if 58 - 58: ooOO0O0ooOooO + o0O00o % IIIIiiII111 - Ii1i1i - IIIi11I1 % Ii1i1i
    if 86 - 86: I11i
    if 15 - 15: ooOO0O0ooOooO - iI11I1II1I1I - IIiIiII11i - o0O00o % Ii1I
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 80 - 80: o0O00o * IIIIiiII111 . ooOoO0O00 % Ii1i1i % Ii1I + oOOoOooOo
def IIII1IiiI ( url ) :
 II1I11i = i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' )
 O0o0O0 = i11oO0oOo0 ( II1I11i )
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
 if 100 - 100: oOo0O0Ooo - IIIi11I1
def OOOOo0ooOOO0 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O0o0O0 )
 for iII11 in I1Ii :
  OooO0O = iII11
 II1iIi1IiIii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( O0o0O0 )
 for url in II1iIi1IiIii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']NEXT PAGE[/COLOR]' , url , 10006 , iiiiiIIii + 'Next.png' , iIi1ii1I1 , '' )
 Ii1i1iI1iIIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10007 , OooO0O )
  if 91 - 91: Ii + Ii1i1i % Ii1i1i + I11i
  if 15 - 15: Ii1I . oOo0O0Ooo - o0O0Oooo0O - ooOoO0O00
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: IIIIiiII111 . Ii1i1i * oOo0O0Ooo % o0O0Oooo0O + iI11I1II1I1I
def OoO00o ( url , IMAGE ) :
 Oo0o0OO0O0o = [ ]
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0Oo0O in Ii1i1iI1iIIi :
  if 'panda' in Oo0Oo0O :
   oO0000OOo00 = i11oO0oOo0 ( Oo0Oo0O )
   I1Ii = re . compile ( "url: '(.+?)'" ) . findall ( oO0000OOo00 )
   for i1iIIII1iiIIi in I1Ii :
    if 'http' in i1iIIII1iiIIi :
     Oo0o0OO0O0o . append ( { 'source' : 'playpanda' , 'quality' : 'SD' , 'url' : i1iIIII1iiIIi } )
  elif 'easy' in Oo0Oo0O :
   iiIi1IIiIi = i11oO0oOo0 ( Oo0Oo0O )
   II1iIi1IiIii = re . compile ( 'file: "(.+?)"' ) . findall ( iiIi1IIiIi )
   for i1iIIII1iiIIi in II1iIi1IiIii :
    if 'http' in i1iIIII1iiIIi :
     Oo0o0OO0O0o . append ( { 'source' : 'easyvideo' , 'quality' : 'SD' , 'url' : i1iIIII1iiIIi } )
  elif 'zoo' in Oo0Oo0O :
   oOO00Oo = i11oO0oOo0 ( Oo0Oo0O )
   iI111i11iI1 = re . compile ( 'src: "(.+?)"' ) . findall ( oOO00Oo )
   for i1iIIII1iiIIi in iI111i11iI1 :
    if 'http' in i1iIIII1iiIIi :
     Oo0o0OO0O0o . append ( { 'source' : 'videozoo' , 'quality' : 'SD' , 'url' : i1iIIII1iiIIi } )
 if len ( Oo0o0OO0O0o ) >= 3 :
  OoOOo0OOoO = O0OoO000O0OO . select ( 'Select Playlink' ,
 [ I1I1IiI1 [ "source" ] + " - " + " (" + I1I1IiI1 [ "quality" ] + ")"
 for I1I1IiI1 in Oo0o0OO0O0o ] )
  if OoOOo0OOoO != - 1 :
   url = Oo0o0OO0O0o [ OoOOo0OOoO ] [ 'url' ]
   oooOO0 = False
   xbmc . Player ( ) . play ( url )
   if 38 - 38: ooOO0O0ooOooO
   if 9 - 9: iIII . oO0o . ooOO0O0ooOooO / ii
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
def iii1IiI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "url: '(.+?)'," ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
  if 87 - 87: oOo0O0Ooo - o0o00Oo0O - iIII * o0O0Oooo0O % o0O0Oooo0O
  if 99 - 99: o0o00Oo0O * Ii % IIIi11I1 * IIiIiII11i
  if 98 - 98: o0o00Oo0O + iI11I1II1I1I
def oo0OO0Oo000oo ( ) :
 if 38 - 38: IIIIiiII111 + oOOoOooOo
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Stand Up[/COLOR]' , '' , 10014 , iiiiiIIii + 'StandUp.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search Comedian[/COLOR]' , '' , 10015 , iiiiiIIii + 'SearchComedian.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Others[/COLOR]' , '' , 10017 , iiiiiIIii + 'Others.png' , iIi1ii1I1 , '' )
 if 32 - 32: oOOoOooOo - ii + oO0o
def OO0oO ( ) :
 oO0000OOo00 = i11oO0oOo0 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'elete' in iiIiii1IIIII :
   pass
  else :
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 222 , iII11 )
   if 5 - 5: Ii / oO0o % o0o00Oo0O / IIIi11I1 + I1ii11iIi11i % I11i
def OOO0o0O00O ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 oO0000OOo00 = i11oO0oOo0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO0oO0OoO00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , Oo0ooo00o0O0 , i1iII1IiiIiI1 in oO0oO0OoO00 :
  for IIIIIiII1 in Oo0ooo00o0O0 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   II1I1iI1i1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for Oo0o00OO0000 , iiIiii1IIIII in II1I1iI1i1IiI :
    if 'tube' in Oo0o00OO0000 :
     pass
    elif 'stage' in Oo0o00OO0000 :
     iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + Oo0ooo00o0O0 + '   -   ' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iII11 , )
    elif 'vee' in Oo0o00OO0000 :
     pass
     if 9 - 9: ooOO0O0ooOooO / ii / IIIi11I1 * Ii - oOOoOooOo + o0O0Oooo0O
def ooOooOOOoO0 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO0oO0OoO00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , Oo0ooo00o0O0 , i1iII1IiiIiI1 in oO0oO0OoO00 :
  II1I1iI1i1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for Oo0o00OO0000 , iiIiii1IIIII in II1I1iI1i1IiI :
   if 'tube' in Oo0o00OO0000 :
    pass
   elif 'stage' in Oo0o00OO0000 :
    iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + Oo0ooo00o0O0 + '   -   ' + iiIiii1IIIII + '[/COLOR]' , ( Oo0o00OO0000 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iII11 )
   elif 'vee' in Oo0o00OO0000 :
    pass
    if 27 - 27: IIiIiII11i - Ii - ii
    if 90 - 90: oOo0O0Ooo
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: IIIi11I1 % oOOoOooOo - IIIi11I1 - I11i
def o0OOII1I1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iii11I11iI1 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0000OOo00 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( iii11I11iI1 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in iii11I11iI1 :
  ooOoOOoooO000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 30 - 30: o0O00o
  if 34 - 34: ooOO0O0ooOooO - IIiIiII11i - I11i + IIIIiiII111 + o0O0Oooo0O
  if 70 - 70: ii + oO0o * I1ii11iIi11i
  if 20 - 20: Ii - IIiIiII11i - oOOoOooOo % ooOO0O0ooOooO . oOOoOooOo
  if 50 - 50: iI11I1II1I1I + o0O0Oooo0O - iIII - ii
  if 84 - 84: OOooOOo - iIII
  if 80 - 80: Ii % IIIi11I1 - I1ii11iIi11i % IIIi11I1
def i1II ( ) :
 if 89 - 89: Ii1i1i * iIII + OOooOOo / Ii
 oo00ooOOOo0O ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , iIi1ii1I1 , '' )
 oo00ooOOOo0O ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIi1ii1I1 , '' )
 if 19 - 19: IIIi11I1 * iIII
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 85 - 85: ooOoO0O00 % I11i * Ii1I * oO0o . IIiIiII11i
def O000 ( ) :
 oo00ooOOOo0O ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIi1ii1I1 , '' )
 oo00ooOOOo0O ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIi1ii1I1 , '' )
 if 18 - 18: oOOoOooOo + o0O0Oooo0O / IIIi11I1 / ooOO0O0ooOooO + iI11I1II1I1I % o0O00o
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
def oOoOO00Ooo ( ) :
 if 49 - 49: ooOoO0O00 % ooOO0O0ooOooO / IIIi11I1 . Ii1I - o0O0Oooo0O
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 ooiI1i = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 12 - 12: Ii + iIII - Ii1I
 for IIII1iIIii in ooiI1i :
  IiiOooooOo0 = OOO00O + IIII1iIIii + I11iii1Ii
  oO0000OOo00 = O0 ( IiiOooooOo0 )
  Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    iiiiIiii1I11 ( iiIiii1IIIII , Oo0o00OO0000 , 222 , ii1IiIiI1 , ooo0O0o00O , i11II1I11I1 )
    if 48 - 48: ooOoO0O00 - o0O00o + oOOoOooOo . IIIIiiII111 / ooOO0O0ooOooO % iI11I1II1I1I
    OOoOO0o0o0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 96 - 96: I1ii11iIi11i . ooOO0O0ooOooO + iI11I1II1I1I * OOooOOo - o0o00Oo0O
    if 74 - 74: OOooOOo
def iI1Iiii11Iii ( ) :
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 ooiI1i = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 34 - 34: I11i % Ii1I + Ii1i1i * iIII / ooOO0O0ooOooO
 for IIII1iIIii in ooiI1i :
  i111Iii11i1Ii = OOO00O + IIII1iIIii + I11iii1Ii
  oO0000OOo00 = O0 ( i111Iii11i1Ii )
  Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iiIiii1IIIII , i11II1I11I1 , Oo0o00OO0000 , iII11 , ooo0O0o00O , o0OO in Ii1i1iI1iIIi :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    oo00ooOOOo0O ( iiIiii1IIIII , Oo0o00OO0000 , o0OO , iII11 , ooo0O0o00O , i11II1I11I1 )
    if 65 - 65: iI11I1II1I1I * o0O00o
    OOoOO0o0o0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 89 - 89: o0O00o % Ii . Ii + ooOO0O0ooOooO / Ii1I
    if 19 - 19: oOo0O0Ooo
def OO0OO0 ( ) :
 if 100 - 100: ooOO0O0ooOooO + oO0o
 O0o0O0 = i11oO0oOo0 ( OOO00O + 'spongemain.php' )
 Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , i11II1I11I1 , Oo0o00OO0000 , iII11 , ooo0O0o00O , o0OO in Ii1i1iI1iIIi :
  oo00ooOOOo0O ( iiIiii1IIIII , Oo0o00OO0000 , o0OO , iII11 , ooo0O0o00O , i11II1I11I1 )
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
def OoOOOo0 ( url ) :
 if 53 - 53: I11i / iIII % o0o00Oo0O / iI11I1II1I1I / IIIIiiII111
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iIiii1Ii = ( '%s%s' % ( II1I11i , url ) )
 I1I1IiI1 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I1IiI1 )
 for url , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I1ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
  for IIi1IIIi in I1ii1 :
   if IIi1IIIi == url :
    iiIiii1IIIII = ( '[COLORred]Watched - [/COLOR]' + iiIiii1IIIII ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  iiiiIiii1I11 ( iiIiii1IIIII , url , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
  if 17 - 17: o0o00Oo0O - Ii1i1i + o0O00o
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
  if 49 - 49: I1ii11iIi11i % ooOO0O0ooOooO
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 49 - 49: o0O0Oooo0O * ooOO0O0ooOooO / I11i
  if 78 - 78: o0O00o + iIII - I11i + oO0o / iI11I1II1I1I
def ii111I111i ( url ) :
 if 18 - 18: ooOO0O0ooOooO - o0O00o % iIII * Ii1i1i
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , i11II1I11I1 , url , iII11 , ooo0O0o00O , o0OO in Ii1i1iI1iIIi :
  oo00ooOOOo0O ( iiIiii1IIIII , url , o0OO , iII11 , ooo0O0o00O , i11II1I11I1 )
  if 66 - 66: ooOoO0O00 - ooOoO0O00 - IIIi11I1 . iIII
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
  if 25 - 25: ooOoO0O00 * oOo0O0Ooo - OOooOOo + ooOO0O0ooOooO
  if 74 - 74: IIIIiiII111 / o0O0Oooo0O / IIiIiII11i - IIIIiiII111 / ooOO0O0ooOooO % iIII
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: o0O00o % ii + ii
def iiiiIiii1I11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 7 - 7: ooOoO0O00
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0oo0O0 = [ ]
  O0oo0O0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0oo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   O0oo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1I1 . addContextMenuItems ( O0oo0O0 )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = False )
 return iioO0o
 if 91 - 91: OOooOOo - OOooOOo . o0O00o
def oo00ooOOOo0O ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 33 - 33: o0O0Oooo0O - iI11I1II1I1I / Ii1i1i % o0o00Oo0O
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0oo0O0 = [ ]
  O0oo0O0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0oo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   O0oo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1I1 . addContextMenuItems ( O0oo0O0 )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = True )
 return iioO0o
if 80 - 80: o0O00o % ii - o0O00o
if 27 - 27: o0O0Oooo0O - I11i * Ii1I - oOo0O0Ooo
if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIIIiiII111 . Ii1i1i
if 100 - 100: IIiIiII11i / o0O0Oooo0O / IIIIiiII111 - Ii1I * iI11I1II1I1I
if 7 - 7: ooOoO0O00 . o0O00o % Ii * Ii1I . iIII % Ii1I
if 35 - 35: oOo0O0Ooo
if 48 - 48: ii % ii - oO0o . OOooOOo
if 22 - 22: oOOoOooOo . Ii . ii . ooOoO0O00
if 12 - 12: OOooOOo % IIIi11I1 + ooOO0O0ooOooO . o0o00Oo0O % iI11I1II1I1I
if 41 - 41: ii
if 13 - 13: iIII + o0O0Oooo0O - o0O0Oooo0O % ooOO0O0ooOooO / iIII
if 4 - 4: oOo0O0Ooo + IIIi11I1 - o0O00o + IIIIiiII111
if 78 - 78: Ii1i1i
if 29 - 29: IIiIiII11i
if 79 - 79: iI11I1II1I1I - Ii + oOOoOooOo - IIiIiII11i . iI11I1II1I1I
def OO000o0O0o ( string ) :
 if IIIi1I1IIii1II == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 67 - 67: IIIi11I1 . Ii + oOOoOooOo . iI11I1II1I1I
def iiIi1i ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I1i11IIiiIiI = [ ]
 try :
  if 7 - 7: oO0o * Ii * iI11I1II1I1I / IIIi11I1 / o0O0Oooo0O
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( oO0Oo ) == False :
  OO000o0O0o ( 'Making Favorites File' )
  I1i11IIiiIiI . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOoO00o = open ( oO0Oo , "w" )
  oOoO00o . write ( json . dumps ( I1i11IIiiIiI ) )
  oOoO00o . close ( )
 else :
  OO000o0O0o ( 'Appending Favorites' )
  oOoO00o = open ( oO0Oo ) . read ( )
  i11Ii1iiiI1I = json . loads ( oOoO00o )
  i11Ii1iiiI1I . append ( ( name , url , iconimage , fanart , mode ) )
  iI11IIi1iiI1I = open ( oO0Oo , "w" )
  iI11IIi1iiI1I . write ( json . dumps ( i11Ii1iiiI1I ) )
  iI11IIi1iiI1I . close ( )
  if 50 - 50: I1ii11iIi11i - oOo0O0Ooo * oO0o . oOOoOooOo % oO0o + ii
  if 25 - 25: IIIIiiII111 . oO0o / iI11I1II1I1I
def OOoo00OoO0o ( ) :
 if os . path . exists ( oO0Oo ) == False :
  I1i11IIiiIiI = [ ]
  OO000o0O0o ( 'Making Favorites File' )
  I1i11IIiiIiI . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oOoO00o = open ( oO0Oo , "w" )
  oOoO00o . write ( json . dumps ( I1i11IIiiIiI ) )
  oOoO00o . close ( )
 else :
  II11Iii1 = json . loads ( open ( oO0Oo ) . read ( ) )
  O00Oo = len ( II11Iii1 )
  for OooOoOo in II11Iii1 :
   iiIiii1IIIII = OooOoOo [ 0 ]
   Oo0o00OO0000 = OooOoOo [ 1 ]
   ii1IiIiI1 = OooOoOo [ 2 ]
   try :
    iIIii1i1iIiI = OooOoOo [ 3 ]
    if iIIii1i1iIiI == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     iIIii1i1iIiI = ii1IiIiI1
    else :
     iIIii1i1iIiI = ooo0O0o00O
   try : oOooooo = OooOoOo [ 5 ]
   except : oOooooo = None
   try : OO00 = OooOoOo [ 6 ]
   except : OO00 = None
   if 44 - 44: I1ii11iIi11i + IIIIiiII111
   if OooOoOo [ 4 ] == 0 :
    OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , '' , ii1IiIiI1 , ooo0O0o00O , '' , 'fav' )
   else :
    OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , OooOoOo [ 4 ] , ii1IiIiI1 , ooo0O0o00O , '' , 'fav' )
    if 8 - 8: IIIIiiII111 - OOooOOo % oOOoOooOo . oO0o
def iI11i ( name ) :
 i11Ii1iiiI1I = json . loads ( open ( oO0Oo ) . read ( ) )
 for i1i111i1 in range ( len ( i11Ii1iiiI1I ) ) :
  if i11Ii1iiiI1I [ i1i111i1 ] [ 0 ] == name :
   del i11Ii1iiiI1I [ i1i111i1 ]
   iI11IIi1iiI1I = open ( oO0Oo , "w" )
   iI11IIi1iiI1I . write ( json . dumps ( i11Ii1iiiI1I ) )
   iI11IIi1iiI1I . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 59 - 59: IIiIiII11i . IIIi11I1 . I11i - o0O0Oooo0O
 if 7 - 7: o0O00o % IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii1i1i
def I1OO ( ) :
 I1i111II = os . path . join ( ooooooO0oo , 'addons.ini' )
 OoO00OOoO = open ( I1i111II , "w+" )
 oO0000OOo00 = i11oO0oOo0 ( 'http://piesustv' + O00o0OO + ':8000/get.php?username=' + O0o0Oo + '&password=' + Oo00OOOOO + '&type=m3u_plus&output=mpegts' )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0000OOo00 )
 OoO00OOoO . write ( r'[' + IiII + ']' + '\n' )
 for iiIiii1IIIII , iII11 , iiiI , Oo0o00OO0000 in Ii1i1iI1iIIi :
  Oo0o00OO0000 = ( Oo0o00OO0000 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iii1OO00Oo00o = ( iiIiii1IIIII + '=plugin://' + IiII + '/?url=' + Oo0o00OO0000 + '&mode=10012&name=' + ( iiIiii1IIIII ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iII11 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iII11 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  OoO00OOoO . write ( iii1OO00Oo00o + '\n' )
  if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . IIIi11I1
  if 3 - 3: o0o00Oo0O - o0O0Oooo0O * Ii1i1i * IIIi11I1 / Ii1i1i
def O0Ooo000OO00 ( ) :
 O0o0O0 = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 Ii1i1iI1iIIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 in Ii1i1iI1iIIi :
  I111I11I111 ( '24/7' , Oo0o00OO0000 , 90021 , iiiiiIIii + '247Streams.png' )
  if 51 - 51: oOOoOooOo * o0O00o * iI11I1II1I1I / OOooOOo % o0O00o
def IIIIIii1iiIIi ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + '247Streams.png' , iiiiiIIii + '247Streams.png' , '' )
def I1iIiI ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + 'musicch.png' , iiiiiIIii + 'musicch.png' , '' )
def oOO ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + 'NEWS.png' , iiiiiIIii + 'NEWS.png' , '' )
def oO0oOoOoo0 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , ( Oo0o00OO0000 ) . strip ( ) , 222 , iiiiiIIii + 'adult.png' , iiiiiIIii + 'adult.png' , '' )
def OoOoOo ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 Ii1i1iI1iIIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( iiIiii1IIIII , Oo0o00OO0000 , 1016 , iiiiiIIii + 'TUTS.png' , iiiiiIIii + 'TUTS.png' , '' )
  if 16 - 16: Ii1I % Ii1I % o0O0Oooo0O + iIII . o0O0Oooo0O + IIIi11I1
  if 85 - 85: Ii . iIII + Ii1i1i / Ii1i1i
def i1o00Oo ( ) :
 if 38 - 38: o0O0Oooo0O
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Recent Episodes[/COLOR]' , '' , 10019 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Genres[/COLOR]' , '' , 10020 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search[/COLOR]' , '' , 10021 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
 if 59 - 59: ooOO0O0ooOooO - ooOO0O0ooOooO / o0O0Oooo0O * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
def IIiI ( ) :
 if 11 - 11: oOOoOooOo
 O0o0O0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i1iI1iIIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , iiI11ii1111 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII + '  -  ' + ( iiI11ii1111 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Oo0o00OO0000 , 10023 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
  if 36 - 36: oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
  if 54 - 54: o0O00o - IIiIiII11i . oOOoOooOo + Ii1i1i
  if 45 - 45: ooOO0O0ooOooO + IIiIiII11i . IIIIiiII111 / Ii1I
def O0O000 ( ) :
 if 72 - 72: ooOoO0O00
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
 if 72 - 72: oOOoOooOo + IIiIiII11i . o0o00Oo0O - IIIIiiII111 / ii . o0O0Oooo0O
def iiiiiiI ( url ) :
 iIi1Ii1111i = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0000OOo00 = cloudflare . source ( iIi1Ii1111i )
 Ii1i1iI1iIIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10022 , iiiiiIIii + 'dtv.png' , iIi1ii1I1 , '' )
  if 41 - 41: Ii1i1i
  if 49 - 49: Ii1i1i % IIiIiII11i . Ii1i1i - I11i - iIII * o0O00o
  if 47 - 47: o0o00Oo0O . I11i / Ii1i1i * IIIIiiII111
  if 63 - 63: o0O0Oooo0O - ooOO0O0ooOooO - IIIIiiII111 - oOOoOooOo / ooOO0O0ooOooO + oO0o
def o0oOo ( ) :
 if 32 - 32: ooOO0O0ooOooO . IIIi11I1 % IIIi11I1 . OOooOOo
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 Oo0o00OO0000 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 oO0000OOo00 = cloudflare . source ( Oo0o00OO0000 )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 10022 , iiiiiIIii + 'dtv.png' )
   if 37 - 37: IIIi11I1 + o0o00Oo0O + IIIi11I1 . IIIIiiII111 . I11i
   if 78 - 78: oOo0O0Ooo / iIII + I11i . I1ii11iIi11i / o0o00Oo0O
   if 49 - 49: Ii1I
def oOOiI111I ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0Oo0O , oo0OOoOoo0O0O , OOO0o , iiIiii1IIIII in Ii1i1iI1iIIi :
  i1iiII1I1I1ii = ( OOO0o ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Iii1I1111iI = ( oo0OOoOoo0O0O ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOOoo0ooo0 = 'Season ' + Iii1I1111iI + 'Episode ' + i1iiII1I1I1ii + iiIiii1IIIII
  o0OO0OOoo0oO ( oOOoo0ooo0 , Oo0Oo0O )
  if 98 - 98: I11i * I1ii11iIi11i - Ii1i1i . oOOoOooOo
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 2 - 2: I1ii11iIi11i - oOOoOooOo % iI11I1II1I1I
  if 88 - 88: o0O0Oooo0O - oO0o
def o0OO0OOoo0oO ( name , url ) :
 Oo0Oo0O = url
 oO0Ooo0o00o = name
 iiIi1IIiIi = cloudflare . source ( Oo0Oo0O )
 I1Ii = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iiIi1IIiIi )
 for iii11I11iI1 , oOoOOO0oO0O in I1Ii :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + oO0Ooo0o00o + oOoOOO0oO0O + '[/COLOR]' , iii11I11iI1 , 222 , iiiiiIIii + 'dtv.png' )
  if 37 - 37: oOo0O0Ooo - iI11I1II1I1I
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: o0O00o - Ii1i1i + Ii * oO0o % oOo0O0Ooo
 if 37 - 37: iI11I1II1I1I + o0O00o / o0O0Oooo0O . ii
def oOooo ( ) :
 if 72 - 72: ooOO0O0ooOooO % oOOoOooOo % IIIi11I1
 if 63 - 63: oO0o . Ii1i1i % IIiIiII11i / iIII - OOooOOo
 if 4 - 4: I1ii11iIi11i - o0o00Oo0O / iIII + o0o00Oo0O - ooOO0O0ooOooO * I1ii11iIi11i
 if 25 - 25: oOo0O0Ooo
 if 64 - 64: ooOO0O0ooOooO
 if 80 - 80: I11i % iI11I1II1I1I
 if 63 - 63: o0O00o * Ii
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']SEARCH[/COLOR]' , '' , 10091 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 if 86 - 86: iIII % iIII - OOooOOo + o0O0Oooo0O / oOo0O0Ooo * ii
def IiI1iIIiIi1Ii ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0000OOo00 )
 O0oOoOOO000 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + iII11 , '' , '' )
 for url in O0oOoOOO000 :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiiiiIIii + 'Next.png' , '' , '' )
  if 57 - 57: I11i - o0O00o . IIIi11I1
def IIiIi ( url ) :
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0000OOo00 )
 O0oOoOOO000 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iII11 = 'http://watchepisodes.cc/' + iII11
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 10093 , iII11 , iII11 , '' )
 for url in O0oOoOOO000 :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiiiiIIii + 'Next.png' , '' , '' )
  if 45 - 45: I1ii11iIi11i
def iI1Iii11II ( url , iconimage ) :
 iII11 = iconimage
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0000OOo00 )
 for OOO0o , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + OOO0o + ' - ' + iiIiii1IIIII + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , iII11 , '' , '' )
  if 17 - 17: iI11I1II1I1I - oOOoOooOo
def OO00O0O ( url , iconimage ) :
 iII11 = iconimage
 oO0000OOo00 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if 'player' in iiIiii1IIIII :
   pass
  elif 'vod' in iiIiii1IIIII :
   OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , iII11 , '' , '' )
   if 52 - 52: Ii1I
   if 93 - 93: IIIIiiII111 . Ii
   if 24 - 24: IIIi11I1 . oO0o + o0O0Oooo0O . ooOO0O0ooOooO - Ii1I % IIIIiiII111
   if 49 - 49: o0o00Oo0O . I1ii11iIi11i / Ii1i1i
   if 29 - 29: Ii1I / ooOO0O0ooOooO * o0o00Oo0O - Ii - oO0o + Ii1i1i
   if 86 - 86: oOo0O0Ooo / Ii1I * Ii1i1i % Ii
def oo00OOoOoO00 ( ) :
 if 20 - 20: IIIIiiII111 . ii + IIIIiiII111 + oOOoOooOo * Ii1I
 if 44 - 44: Ii
 if 69 - 69: IIIi11I1 * o0o00Oo0O + Ii
 if 65 - 65: o0o00Oo0O / IIIIiiII111 . ooOoO0O00 * IIIIiiII111 / iI11I1II1I1I - ooOO0O0ooOooO
 if 93 - 93: OOooOOo % Ii - Ii1i1i % oO0o
 if 55 - 55: I11i . Ii1I
 if 63 - 63: ooOO0O0ooOooO
 if 79 - 79: Ii1I - ooOO0O0ooOooO - I11i . IIIi11I1
 if 65 - 65: Ii . oO0o % IIIIiiII111 + o0O00o - Ii
 if 60 - 60: o0O0Oooo0O
 if 14 - 14: I1ii11iIi11i % ooOO0O0ooOooO * IIIIiiII111 - Ii / Ii1I * Ii
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * iIII + IIIi11I1
 if 14 - 14: Ii1i1i - o0o00Oo0O
 if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiiiiIIii + 'latest.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiiiiIIii + 'popular.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiiiiIIii + 'Genre.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiiiiIIii + 'series.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Search Program[/COLOR]' , '' , 10043 , iiiiiIIii + 'Search.png' , iiiiiIIii + 'WatchSeries.png' , '' )
 if 45 - 45: o0O0Oooo0O * iIII / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
 if 49 - 49: Ii1i1i / IIIIiiII111 . IIIIiiII111 . IIIIiiII111 + Ii % iIII
def i1I1Iii1IiiIi ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
  if 73 - 73: o0o00Oo0O . o0O0Oooo0O - ii % iIII % ooOoO0O00
def i111II ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
  if 6 - 6: IIIi11I1 - o0o00Oo0O * Ii1I
def O0o0ooo00o00 ( url ) :
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
  if 6 - 6: Ii / oO0o . Ii / oOOoOooOo
  if 26 - 26: o0o00Oo0O * Ii1i1i - oOo0O0Ooo - IIIIiiII111 / iI11I1II1I1I
def oO0Ooo00O ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOoO00o00oo = 'http://www.watchseriesgo.to/search/' + IIIIIiII1 . replace ( ' ' , '%20' )
 oO0000OOo00 = i11oO0oOo0 ( OOoO00o00oo )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'watch online' in iiIiii1IIIII :
   pass
  else :
   print Oo0o00OO0000
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.watchseriesgo.to' + Oo0o00OO0000 , 10044 , iII11 , '' , '' )
   if 5 - 5: ooOO0O0ooOooO - ii / OOooOOo
   xbmcplugin . setContent ( O00oO , 'movies' )
   if 30 - 30: iIII % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
def ooO0000 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , OOO0o , i11II1I11I1 in Ii1i1iI1iIIi :
  IiI1iiI1III1I = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( OOO0o ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + IiI1iiI1III1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iII11 , '' , i11II1I11I1 )
  if 51 - 51: oOo0O0Ooo * o0O0Oooo0O / ooOO0O0ooOooO % IIIIiiII111
def iIiiIII ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  IiI1iiI1III1I = ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + IiI1iiI1III1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 for url in I1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiiiiIIii + 'Next.png' , '' , '' )
  if 37 - 37: ii / Ii1I % I11i
def II1O0ooo00o0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iII11 , '' , '' )
 for url in I1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiiiiIIii + 'Next.png' , '' , '' )
  if 2 - 2: o0O0Oooo0O / IIIi11I1
def Ii1II1iiiiiIi1I1i ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0000OOo00 )
 Ii1II1I11i1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for oo0OOoOoo0O0O , oO0oO0OoO00 in Ii1II1I11i1 :
  Ii1i1iI1iIIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oO0oO0OoO00 ) )
  for url , iiIiii1IIIII in Ii1i1iI1iIIi :
   IiI1iiI1III1I = ( oo0OOoOoo0O0O ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + IiI1iiI1III1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 I1Ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiiiiIIii + 'WATCHSERIES.png' , '' , '' )
 for url in I1Ii :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiiiiIIii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16: o0O0Oooo0O % iI11I1II1I1I . ooOoO0O00
class o0O0oOOoo0O0 ( ) :
 if 71 - 71: Ii1I + iIII * I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % Ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 40 - 40: oOOoOooOo - Ii % Ii1I % oOo0O0Ooo . o0O00o * oO0o
  IiI1iiI1III1I = name
  self . Get_Sources ( Oo0o00OO0000 , IiI1iiI1III1I )
  if 51 - 51: o0o00Oo0O % ooOO0O0ooOooO - oOOoOooOo * oOo0O0Ooo * ooOO0O0ooOooO
  if 90 - 90: Ii1i1i + I1ii11iIi11i / iI11I1II1I1I - o0o00Oo0O + oOOoOooOo . Ii1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0000OOo00 = i11oO0oOo0 ( URL )
  Ii1i1iI1iIIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
   URL = 'http://www.watchseriesgo.to/link/' + Oo0o00OO0000
   self . Get_site_link ( URL , season_name )
   if 58 - 58: oO0o + IIIIiiII111 * I11i . iIII
 def Get_site_link ( self , url , season_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
  I1Ii = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oO0000OOo00 )
  II1iIi1IiIii = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oO0000OOo00 )
  for url in Ii1i1iI1iIIi :
   self . main ( url , season_name )
  for url in I1Ii :
   self . main ( url , season_name )
  for url in II1iIi1IiIii :
   self . main ( url , season_name )
   if 48 - 48: IIIi11I1
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   i111I = 'DACLIPS'
   if i111I in o0O0oOOoo0O0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , i111I )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    i111I = 'THEVIDEO'
    if i111I in o0O0oOOoo0O0 . source_list :
     pass
    else :
     self . thevideo ( url , season_name , i111I )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     i111I = 'ALLMYVIDEOS'
     if i111I in o0O0oOOoo0O0 . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , i111I )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      i111I = 'VIDSPOT'
      if i111I in o0O0oOOoo0O0 . source_list :
       pass
      else :
       self . vidspot ( url , season_name , i111I )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       i111I = 'VODLOCKER'
       if i111I in o0O0oOOoo0O0 . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , i111I )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        i111I = 'VIDTO'
        if i111I in o0O0oOOoo0O0 . source_list :
         pass
        else :
         self . vidto ( url , season_name , i111I )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 58 - 58: oOOoOooOo - I1ii11iIi11i
       else :
        if 'youwatch' in url :
         i111I = 'YouWatch'
         if i111I in o0O0oOOoo0O0 . source_list :
          pass
         else :
          self . youwatch ( url , season_name , i111I )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 23 - 23: OOooOOo
          if 38 - 38: oOo0O0Ooo . ooOO0O0ooOooO / o0o00Oo0O % I1ii11iIi11i / o0O00o / ii
 def allmyvid ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
  for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 11 - 11: o0o00Oo0O / o0O0Oooo0O / iI11I1II1I1I % Ii1i1i
 def vidspot ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO , iiIiii1IIIII in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 31 - 31: iIII . Ii . oO0o * I1ii11iIi11i % Ii1i1i . I11i
 def thevideo ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
 def vodlocker ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 93 - 93: oOOoOooOo % o0O0Oooo0O
 def daclips ( self , url , season_name , source_name ) :
  oO0000OOo00 = i11oO0oOo0 ( url )
  Ii1i1iI1iIIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0000OOo00 )
  for oOoooooOoO in Ii1i1iI1iIIi :
   self . Printer ( oOoooooOoO , season_name , source_name )
   if 46 - 46: Ii1I * OOooOOo * o0O00o * Ii1I . Ii1I
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
   if 43 - 43: oOOoOooOo . ooOoO0O00
 def Printer ( self , Link , season_name , source_name ) :
  if 68 - 68: o0O00o % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
  if Link in o0O0oOOoo0O0 . List :
   pass
  elif source_name in o0O0oOOoo0O0 . source_list :
   pass
  else :
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + source_name + '[/COLOR]' , Link , 222 , iiiiiIIii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   o0O0oOOoo0O0 . List . append ( Link )
   o0O0oOOoo0O0 . source_list . append ( source_name )
   if 45 - 45: oOo0O0Ooo
   xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 17 - 17: ii - oOOoOooOo + Ii1i1i . ii % I1ii11iIi11i
   if 92 - 92: o0O0Oooo0O - IIIi11I1 % oO0o - I11i % ooOoO0O00
   if 38 - 38: Ii1I . iIII / OOooOOo % iIII
   if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / IIIIiiII111
   if 61 - 61: I1ii11iIi11i - o0O0Oooo0O
def IIiI11i1111Ii ( ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Highlights[/COLOR]' , '' , 10008 , iiiiiIIii + 'Highlights.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Fixtures[/COLOR]' , '' , 10009 , iiiiiIIii + 'Fixtures.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'Sport.png' , iIi1ii1I1 , '' )
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiiiiIIii + 'PremiereLeague.png' , iIi1ii1I1 , '' )
 if 51 - 51: IIIIiiII111 * oOOoOooOo / o0o00Oo0O / o0o00Oo0O
def oooOOOO0oOo ( url ) :
 iiii1Ii = '20'
 IIiiiI = [ ]
 ii11 = '                                                    '
 iI1i1i1i1i = '        '
 OoOOoOooooOOo ( ii11 + 'pl' + iI1i1i1i1i + 'w' + iI1i1i1i1i + 'd' + iI1i1i1i1i + 'l' + iI1i1i1i1i + 'f' + iI1i1i1i1i + 'a' + iI1i1i1i1i + 'pts' , '' , '' , '' , '' , '' )
 O0o0O0 = i1oO ( url )
 Ii1i1iI1iIIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiII1i1II1iIi , iIIOOOO0o0Oo0 , I1iIiI1iiI , ooIii , oO000O00 , OOo0O0oo0OO0O , oOoO00o , IiIIIii1iIII1 , OoOooooo0oo in Ii1i1iI1iIIi :
  ii1II1 = i1I1II11I1 ( iIIOOOO0o0Oo0 )
  oo0oOoOoo = i1I1II11I1 ( I1iIiI1iiI )
  O0oOoOooo00oo = i1I1II11I1 ( ooIii )
  OOO0OO00 = i1I1II11I1 ( oO000O00 )
  oOO00 = i1I1II11I1 ( OOo0O0oo0OO0O )
  II1IiII1I1II = i1I1II11I1 ( oOoO00o )
  IIiiiI . append ( iiII1i1II1iIi [ 0 ] )
  oooOII111iiI1Ii1 = len ( IIiiiI )
  oo0oO0oO00oO = int ( len ( ii11 ) - len ( iiII1i1II1iIi ) - 2 )
  if len ( IIiiiI ) >= 10 :
   oo0oO0oO00oO = oo0oO0oO00oO - 1
  if len ( IIiiiI ) <= int ( iiii1Ii ) :
   oOOOoo0O0oO ( str ( oooOII111iiI1Ii1 ) + ' ' + iiII1i1II1iIi + ii11 [ 0 : oo0oO0oO00oO ] + iIIOOOO0o0Oo0 + ii1II1 + I1iIiI1iiI + oo0oOoOoo + ooIii + O0oOoOooo00oo + oO000O00 + OOO0OO00 + OOo0O0oo0OO0O + oOO00 + oOoO00o + II1IiII1I1II + ' ' + OoOooooo0oo , '' , '' , '' , '' , '' )
   if 94 - 94: oOOoOooOo * IIIi11I1
   if 59 - 59: o0O0Oooo0O * IIIIiiII111
def i1I1II11I1 ( space ) :
 if len ( space ) > 1 :
  ii1i1Iii = len ( '        ' ) - len ( space ) + 1
  space = int ( ii1i1Iii ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 31 - 31: iIII / o0o00Oo0O
def oo00oO0o000 ( ) :
 if 15 - 15: I1ii11iIi11i
 if 55 - 55: o0O0Oooo0O
 if 29 - 29: I1ii11iIi11i
 if 97 - 97: oO0o * o0O0Oooo0O
 if 80 - 80: IIIi11I1 * IIIi11I1
 if 5 - 5: ii - IIIIiiII111 - Ii
 if 53 - 53: IIIIiiII111 * oO0o / Ii1I + oOo0O0Ooo + ii
 if 47 - 47: o0O0Oooo0O
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
 if 20 - 20: oOOoOooOo
 if 63 - 63: iI11I1II1I1I . oO0o
 if 100 - 100: ooOoO0O00 * ooOoO0O00
 if 26 - 26: IIIi11I1 . oO0o % OOooOOo
 if 94 - 94: o0O00o
 if 15 - 15: Ii1i1i - o0O00o / o0o00Oo0O
 if 28 - 28: o0O0Oooo0O . ooOoO0O00 / Ii1I
 if 77 - 77: Ii / o0O0Oooo0O / Ii % OOooOOo - o0O0Oooo0O
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 Ii1i1iI1iIIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Oo0o00OO0000 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iII11 , iIi1ii1I1 , '' )
  if 80 - 80: o0O0Oooo0O % OOooOOo . ii . IIiIiII11i % o0O00o
def I1i1I1i1I1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Ii1II1I11i1 in Ii1II1I11i1 :
  O0000 = re . compile ( '(.*?)</h2>' ) . findall ( str ( Ii1II1I11i1 ) )
  for i1IOO in O0000 :
   i1IOO = i1IOO
  Ii1I11ii1i = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
  for O0OOoooO , iII11 , time , Oo0OO0ooO0O0O in Ii1I11ii1i :
   Oo0O00oOoo00 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( Oo0OO0ooO0O0O )
   OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + i1IOO + ' - ' + O0OOoooO + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iII11 , iIi1ii1I1 , ( str ( Oo0O00oOoo00 ) ) )
   if 76 - 76: I11i / iIII
 OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
def iIo0O00o00o0 ( ) :
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
 if 87 - 87: Ii1i1i % Ii1I * I1ii11iIi11i
def OOO00i111 ( url ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'TodaysMacthes.png' , iIi1ii1I1 , '' )
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  Ii1i = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiIiii1IIIII :
   pass
  else :
   Ii1i = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + Ii1i + '[/COLOR]' , url , 10013 , iII11 )
 for url , iII11 , iiIiii1IIIII in I1Ii :
  Ii1i = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiIiii1IIIII :
   pass
  else :
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + Ii1i + '[/COLOR]' , url , 10013 , iII11 )
def i1i1I111iI ( url ) :
 OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiiiiIIii + 'TodaysMacthes.png' , iIi1ii1I1 , '' )
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 if 20 - 20: oO0o / Ii * I11i - Ii1I - IIiIiII11i / Ii
 if 17 - 17: I1ii11iIi11i - oOo0O0Ooo - o0O00o - IIIi11I1 / ooOO0O0ooOooO + o0O0Oooo0O
 if 40 - 40: o0O0Oooo0O / oOo0O0Ooo - ii / o0O0Oooo0O
 if 48 - 48: I1ii11iIi11i . oO0o . oOo0O0Ooo * IIIIiiII111 . iI11I1II1I1I
 if 66 - 66: ii * o0o00Oo0O / oOOoOooOo * Ii1i1i
 if 22 - 22: oOo0O0Ooo
 if 76 - 76: oO0o + iIII + oO0o . iIII % IIIi11I1
 for url , iII11 , iiIiii1IIIII in I1Ii :
  Ii1i = iiIiii1IIIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiIiii1IIIII :
   pass
  else :
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + Ii1i + '[/COLOR]' , url , 10013 , iII11 )
   if 96 - 96: I1ii11iIi11i
def iIIiiiI1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0000OOo00 )
 for iii11I11iI1 in Ii1i1iI1iIIi :
  i11i1i1i = ( iii11I11iI1 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  ooOoOOoooO000 ( 'http:' + i11i1i1i )
  if 83 - 83: IIiIiII11i + o0O00o - I11i % I11i * I11i
  if 100 - 100: Ii1i1i . iI11I1II1I1I
  if 33 - 33: oOo0O0Ooo . iI11I1II1I1I / Ii * Ii1i1i
  if 18 - 18: OOooOOo * OOooOOo - I11i % oOOoOooOo % IIiIiII11i - o0O00o
def OOo ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iiiiI11ii ( iiIiii1IIIII , url , 8046 , iII11 )
 for url in I1Ii :
  I111I11I111 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiiiiIIii + 'Next.png' )
def i1Iiiiiii ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  ooOoOOoooO000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 62 - 62: iI11I1II1I1I % o0O0Oooo0O % Ii1I * o0O00o
def oO0OO0o0oo0o ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  yt . PlayVideo ( url )
  if 55 - 55: o0O00o
def ii1iii11i1 ( ) :
 I111I11I111 ( '[COLOR' + II11iiii1Ii + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiiiiIIii + 'documentary.png' )
 I111I11I111 ( '[COLOR' + II11iiii1Ii + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiiiiIIii + 'documentary.png' )
 I111I11I111 ( '[COLOR' + II11iiii1Ii + ']Search Docs[/COLOR]' , '' , 80012 , iiiiiIIii + 'Search.png' )
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 8041 , iiiiiIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiii11IiI1 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + iII11 )
 for url in next :
  I111I11I111 ( 'NEXT PAGE' , url , 8041 , iiiiiIIii + 'Next.png' )
  if 1 - 1: ii / I11i / iIII / o0O0Oooo0O
  if 56 - 56: oO0o
def o0oOOO0000o ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']YouTube[/COLOR]' , url , 8043 , iiiiiIIii + 'documentary.png' )
  else :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def OO000o0O0OO0 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  url = ( url ) . replace ( '\/' , '/' )
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , '' )
  if 97 - 97: Ii1i1i % OOooOOo / Ii1I / iI11I1II1I1I * ii * IIIi11I1
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOoO ( name , url ) :
 Oo00oO = 0
 name = name
 url = url
 I11ii1IIiIi = [ '144' , '240' , '380' , '480' , '720' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Resolution[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  O0i1iI ( url )
  if 71 - 71: Ii * OOooOOo * IIIi11I1 + ooOO0O0ooOooO + I1ii11iIi11i
  if 59 - 59: o0O00o
  if 54 - 54: IIIi11I1
  if 27 - 27: OOooOOo - oO0o + I11i + oOOoOooOo . oO0o
  if 86 - 86: IIiIiII11i - ii - oOOoOooOo % IIIIiiII111
  if 16 - 16: oOOoOooOo + I1ii11iIi11i + ii
  if 87 - 87: oOo0O0Ooo . ooOO0O0ooOooO / o0O00o - ii
  if 33 - 33: ooOO0O0ooOooO % oO0o . iI11I1II1I1I / o0O00o
def i1II1iI ( ) :
 O0o0O0 = o00oiii11II1I ( 'http://documentarylovers.com/' )
 Ii1i1iI1iIIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  if 'genre' in Oo0o00OO0000 :
   I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , Oo0o00OO0000 , 80010 , iiiiiIIii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOo0oOO ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , iII11 )
 for url in next :
  I111I11I111 ( 'NEXT PAGE' , url , 80010 , iiiiiIIii + 'Next.png' )
  if 58 - 58: I11i . IIIIiiII111 % IIIIiiII111
def iI1II ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']YouTube[/COLOR]' , url , 8043 , iiiiiIIii + 'documentary.png' )
 for url in I1Ii :
  OO000o0O0OO0 ( url )
  if 59 - 59: I1ii11iIi11i . I11i % oOo0O0Ooo / ii % ooOO0O0ooOooO
def Oo00o ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIIiiiI = 'http://documentarylovers.com/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 OoO00oo00 = i1iIIIiiiI . lower ( )
 oOOo0oOO ( OoO00oo00 )
 if 14 - 14: IIiIiII11i + o0o00Oo0O - IIIIiiII111
def II1i1 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'films' in url :
   I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiiiiIIii + 'documentary.png' )
def ooO0OoOO0 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'films' in url :
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + iII11 )
 for url in I1Ii :
  I111I11I111 ( 'NEXT' , url , 8049 , iiiiiIIii + 'Next.png' )
def o0oo00 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  if 'rtd' in url :
   o000IIIi1IiI1iII ( url )
   if 85 - 85: Ii1I + OOooOOo - Ii % OOooOOo . ooOO0O0ooOooO + Ii
def o000IIIi1IiI1iII ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( O0o0O0 )
 for I1I1IiI1 , file in Ii1i1iI1iIIi :
  url = ( 'https://rtd.rt.com' + I1I1IiI1 + file )
  O0i1iI ( url )
  if 12 - 12: o0O00o + ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii1I
  if 5 - 5: oOOoOooOo - o0O0Oooo0O - IIIIiiII111
def iioOOOoOo0oOoo ( ) :
 oO0000OOo00 = o00oiii11II1I ( 'http://www.stream2watch.co/live-tv' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , O00O00OoO in Ii1i1iI1iIIi :
  I111I11I111 ( ( iiIiii1IIIII + '[COLOR' + II11iiii1Ii + ']' + O00O00OoO + '[/COLOR]' ) , Oo0o00OO0000 , 8086 , iII11 )
  if 64 - 64: Ii + OOooOOo + I11i + IIIi11I1
def Iii1iii11 ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 8087 , iII11 )
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
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 34 - 34: o0O00o
def iIiIIiII11i1 ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + Oo0o00OO0000 , 3002 , 'http://www.solie.org/alibrary/' + iII11 )
def i1Iii ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iII11 )
def oOOooo ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 IiI11IiIIi = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( O0o0O0 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiiiiIIii + 'classicmovies.png' )
 for url , iiIiii1IIIII in IiI11IiIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']Season- ' + iiIiii1IIIII + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiiiiIIii + 'classicmovies.png' )
 for url in next :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiiiiIIii + 'Next.png' )
 for url , iII11 , iiIiii1IIIII in I1Ii :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iII11 )
def oOOo0OoooOo ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  I1I1IiIiIIi1I ( url )
def I1I1IiIiIIi1I ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
  if 74 - 74: ii + Ii1I % o0o00Oo0O
def o0OoO000O ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Oo0o00OO0000 , 8065 , iiiiiIIii + 'classicmovies.png' )
def iII1IIoO00oOOOO ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( "v.src = '([^']*)';" ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  II11IiI1 ( url )
  if 54 - 54: iIII * ii
def o00oIII11I ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Oo0o00OO0000 , 8065 , iiiiiIIii + 'classictv.png' )
def OO0ooo ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
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
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + Oo0o00OO0000 , 8071 , iiiiiIIii + 'streams.png' )
def II1111iII1 ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '(Free Access)' in iiIiii1IIIII :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0o0Oo + '/' + Oo00OOOOO + url ) . strip ( )
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiiiiIIii + 'streams.png' )
def iio0000oO0OOOo0 ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0o0Oo + '/' + Oo00OOOOO + url ) . strip ( )
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iII11 , ooo0O0o00O , '' )
  if 64 - 64: Ii1i1i - IIIIiiII111
def I1111iiiII1Ii ( ) :
 I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']XXX Vids[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Perfect Girls[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Best Videos[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Genres[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Recently Uploaded[/COLOR]' , '[COLOR' + II11iiii1Ii + ']100% Verified[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Tags[/COLOR]' , '[COLOR' + II11iiii1Ii + ']In Your Language[/COLOR]' , '[COLOR' + II11iiii1Ii + ']Search[/COLOR]' ]
 OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']TOOLS[/COLOR]' , I11ii1IIiIi )
 if OoOOo0OOoO == 0 :
  i1III1i1I11I ( 'http://watchxxxfree.com/categories' )
 if OoOOo0OOoO == 1 :
  OOOo00O ( 'http://www.perfectgirls.net' )
 if OoOOo0OOoO == 2 :
  I1iOO000o0o0oo ( 'http://www.xvideos.com/best' )
 if OoOOo0OOoO == 3 :
  oO00oOoo0ooO0 ( 'http://www.xvideos.com/best' )
 if OoOOo0OOoO == 4 :
  I1iOO000o0o0oo ( 'http://www.xvideos.com/best' )
 if OoOOo0OOoO == 5 :
  I1iOO000o0o0oo ( 'http://www.xvideos.com/verified/videos' )
 if OoOOo0OOoO == 6 :
  Ooo0o0ooO0 ( 'http://www.xvideos.com/tags' )
 if OoOOo0OOoO == 7 :
  oO0o0O ( 'http://www.xvideos.com/porn' )
 if OoOOo0OOoO == 8 :
  OoO0O00OO0OoO00oO ( )
  if 19 - 19: iI11I1II1I1I * I1ii11iIi11i / IIIi11I1
  if 5 - 5: I11i
  if 24 - 24: o0O00o + oO0o - Ii1i1i
  if 38 - 38: o0O0Oooo0O
  if 30 - 30: IIiIiII11i + iIII . Ii + iI11I1II1I1I
  if 100 - 100: ooOO0O0ooOooO * I11i / IIIIiiII111
  if 92 - 92: oOOoOooOo / Ii * IIIi11I1
  if 55 - 55: oOOoOooOo
  if 1 - 1: oO0o
def IiI1IIII ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'ch' in url :
   iiiI1ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiiiiIIii + 'Jizbox.png' , iiiiiIIii + 'Jizbox.png' , '' )
def OOoOo000 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0000OOo00 )
 OoOOOoo = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiiiiIIii + 'Jizbox.png' , '' , '' )
 for iiIiii1IIIII , url in OoOOOoo :
  OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiiiiIIii + 'Next.png' , '' , '' )
def o00O0oOO0o ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'jetload' in url :
   O0000000oooOO ( url )
def iI11iiI1 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
def i1III1i1I11I ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , ii1i1Iii in Ii1i1iI1iIIi :
  if 'category' in url :
   iiiI1ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORorange]   ' + ii1i1Iii + '[/COLOR]' , url , 90006 , iII11 , iiiiiIIii + 'Jizbox.png' , '' )
def I1Ioo000oooooooO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 OoOOOoo = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , iII11 , '' , '' )
 for url in OoOOOoo :
  OoOOoOooooOOo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiiiiIIii + 'Next.png' , '' , '' )
def II1IIi1ii111 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'jetload' in url :
   O0000000oooOO ( url )
def O0000000oooOO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  O0i1iI ( url )
def OOOo00O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , ii1i1Iii in Ii1i1iI1iIIi :
  if 'category' in url :
   iiiI1ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORorange]' + ii1i1Iii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiiiiIIii + 'Jizbox.png' , '' , '' )
def II1OO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Oo0Oo0O = url
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 OoOOOoo = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , iII11 , '' , '' )
 for url in OoOOOoo :
  OoOOoOooooOOo ( '[COLORred]NEXT[/COLOR]' , Oo0Oo0O + '/' + url , 90003 , iiiiiIIii + 'Next.png' , '' , '' )
def oo0OOO0O0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'get\("(.*)", function' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  OoooOooo ( 'http://www.perfectgirls.net' + url )
def OoooOooo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'http://(.+?)\n' ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  ooOoOOoooO000 ( 'http://' + url )
def oO0o0O ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , ii1i1Iii in Ii1i1iI1iIIi :
  iiiI1ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgreen] - No of Videos : [COLORorange]' + ii1i1Iii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Jizbox.png' , '' , '' )
def Ooo0o0ooO0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 OoOOOoo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0000OOo00 )
 for url in OoOOOoo :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiiiiIIii + 'Jizbox.png' , '' , '' )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , ii1i1Iii in Ii1i1iI1iIIi :
  iiiI1ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgreen] - No of Videos : [COLORorange]' + ( ii1i1Iii + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Jizbox.png' , '' , '' )
  if 27 - 27: ooOoO0O00 - iI11I1II1I1I + o0o00Oo0O % I1ii11iIi11i / IIIi11I1 + ooOoO0O00
def i1i1iiO0Oo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 OoOOOoo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for url in OoOOOoo :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiiiiIIii + 'Next.png' , '' , '' )
 Ii1i1iI1iIIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , ii1iIII1iIiIIIIi in Ii1i1iI1iIIi :
  iiiI1ii ( iiIiii1IIIII + '--' + ( ii1iIII1iIiIIIIi ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iII11 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 58 - 58: Ii1I * Ii
  if 47 - 47: o0o00Oo0O . oOo0O0Ooo / oOOoOooOo % Ii
def I1iOO000o0o0oo ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( 'data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , oo0ooOoOOoO , iIIiI in Ii1i1iI1iIIi :
  iiiI1ii ( '[COLORorangered]' + iiIiii1IIIII + '[COLORgreen] - Porn Quality : [COLORorange]' + oo0ooOoOOoO + ' - [COLORred]' + iIIiI + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iII11 , iII11 , oo0ooOoOOoO + ' - ' + iIIiI )
 I1iiII = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for iII11 , url , iiIiii1IIIII , iIIiI in I1Ii :
  iiiI1ii ( '[COLORorangered]' + iiIiii1IIIII + '[COLORgreen] - Porn Quality : [COLORorange]' + iIIiI + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iII11 , iII11 , iIIiI )
 I1iiII = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for url in I1iiII :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Next.png' , '' , '' )
  if 5 - 5: IIIi11I1 * ii + IIIIiiII111 . oOo0O0Ooo
  if 93 - 93: Ii1i1i % iI11I1II1I1I * IIIIiiII111 / OOooOOo * Ii
def oO00oOoo0ooO0 ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1II1I11i1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 OoOOOoo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0000OOo00 )
 for url in OoOOOoo :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiiiiIIii + 'Next.png' , '' , '' )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '/c/' in url :
   iiiI1ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiiiiIIii + 'Jizbox.png' , '' , '' )
   if 26 - 26: oOOoOooOo . IIIIiiII111
   if 76 - 76: o0O0Oooo0O % ii
def OoO0O00OO0OoO00oO ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIi111Ii11Ii = ( IIIIIiII1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OoO00oo00 = IIIi111Ii11Ii . lower ( )
 o0O0o = 'http://www.xvideos.com/?k=' + OoO00oo00
 print o0O0o + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0000OOo00 = i11oO0oOo0 ( o0O0o )
 Ii1i1iI1iIIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , Oo0o00OO0000 , iiIiii1IIIII , iIIiI , oOOooO in Ii1i1iI1iIIi :
  iiiI1ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgreen] - Porn Quality : [COLORorange]' + oOOooO + ' - [COLORred]' + iIIiI + '[/COLOR]' , 'http://www.xvideos.com' + Oo0o00OO0000 , 10108 , iII11 , iII11 , oOOooO + ' - ' + iIIiI )
 I1iiII = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 in I1iiII :
  iiiI1ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + Oo0o00OO0000 , 10105 , iiiiiIIii + 'Next.png' , '' , '' )
if 82 - 82: oOOoOooOo . o0O0Oooo0O . I1ii11iIi11i % iI11I1II1I1I - Ii
if 11 - 11: oOOoOooOo . o0O0Oooo0O - IIIIiiII111 . I11i
if 41 - 41: ooOO0O0ooOooO / oO0o - oO0o + oOOoOooOo * IIIi11I1
if 13 - 13: o0O0Oooo0O * IIiIiII11i - OOooOOo
if 3 - 3: IIIi11I1 + oOOoOooOo * Ii . IIIIiiII111 / iI11I1II1I1I
if 44 - 44: oO0o
if 74 - 74: Ii1i1i * ooOoO0O00 * iIII - ii . oOo0O0Ooo
if 24 - 24: IIiIiII11i - Ii * ooOoO0O00 . oOOoOooOo
if 42 - 42: iIII / Ii
if 7 - 7: iIII
if 50 - 50: Ii . Ii * ooOoO0O00 / Ii . ooOoO0O00 - IIiIiII11i
if 72 - 72: iI11I1II1I1I / I11i . Ii1I
if 78 - 78: iI11I1II1I1I . Ii % o0O00o * Ii1i1i + IIIIiiII111 - iI11I1II1I1I
if 50 - 50: Ii1I % Ii1i1i - iIII % I1ii11iIi11i - iIII - oOo0O0Ooo
if 99 - 99: o0O00o * OOooOOo - ooOoO0O00 / o0O0Oooo0O . oOOoOooOo % I11i
if 69 - 69: o0o00Oo0O . IIIIiiII111
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
def i11i1iI ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0000OOo00 )
 I1Ii = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0000OOo00 )
 II1iIi1IiIii = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  if 'http' in url :
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiiiiIIii + 'Jizbox.png' )
 for url in I1Ii :
  if 'http' in url :
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiiiiIIii + 'Jizbox.png' )
 for url in II1iIi1IiIii :
  if 'http' in url :
   iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiiiiIIii + 'Jizbox.png' )
   if 34 - 34: OOooOOo
def O0Oo ( url ) :
 o0oO = xbmc . Player ( i11i11 ( ) )
 import urlresolver
 try : o0oO . play ( url )
 except : pass
 if 24 - 24: OOooOOo + ii + Ii1i1i * iIII
 if 13 - 13: I1ii11iIi11i * I11i * IIIIiiII111
def o0Ooo0 ( ) :
 if 96 - 96: oOOoOooOo + oO0o * IIiIiII11i * ooOO0O0ooOooO
 if 48 - 48: Ii1I - I1ii11iIi11i - oOOoOooOo . I11i . I11i
 if 49 - 49: ooOoO0O00 . o0O00o
 if 82 - 82: oO0o / iIII
 if 38 - 38: iI11I1II1I1I
 if 9 - 9: IIiIiII11i + I1ii11iIi11i % Ii1I + oOOoOooOo / IIIi11I1
 if 28 - 28: Ii1i1i % iI11I1II1I1I
 if 72 - 72: Ii1I / OOooOOo - Ii
 if 67 - 67: IIIi11I1 / Ii1i1i
 if 51 - 51: iIII % IIiIiII11i - I11i % oO0o * Ii * IIIIiiII111
 oO0000OOo00 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 8091 , iiiiiIIii + 'gofish.png' )
def Oo0ooo0oOo0Oo0O ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 8092 , iII11 )
 for url in next :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 8093 , iiiiiIIii + 'Next.png' )
def II1ii1iI1I1i ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0000OOo00 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0000OOo00 )
 ii1Iii11IIII1 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 in ii1Iii11IIII1 :
  iII11 = iII11
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 8092 , iII11 )
 for url in next :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 8093 , iiiiiIIii + 'Next.png' )
  if 11 - 11: o0O0Oooo0O + o0O0Oooo0O % ooOO0O0ooOooO % Ii1i1i
def II1OOooo ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0000OOo00 )
 for url in Ii1i1iI1iIIi :
  yt . PlayVideo ( url )
  if 44 - 44: iIII - Ii
  if 93 - 93: IIIIiiII111 % Ii - OOooOOo . Ii1i1i
  if 72 - 72: iI11I1II1I1I * IIIi11I1 . iI11I1II1I1I
  if 62 - 62: o0O00o . o0O00o % oOOoOooOo - OOooOOo / ii . oOo0O0Ooo
i11i1I1 = '{PQ},' ; o0OoO0 = '{SC},' ; I11Ii1I1I = '{XG},' ; oo00OO0o0 = '{JP},' ; o0oo0000Oo = '{HW},' ; o00O00 = '{RT},'
def IiiIIIII1iii ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0O00Oooo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 Oo0o00OO0000 = 'http://onlinemovies.tube/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 i1iIIII1iiIIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1I1IiI1ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 O00OOoOOOO00O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Ooo0OOO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooooOoo0OO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIIIIiII1
 Oo0 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 O0000Oo00o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 16 - 16: IIIi11I1 % o0O00o - IIiIiII11i - I11i * Ii / o0O0Oooo0O
 o00iIiiiII = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 Ii1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 74 - 74: IIIIiiII111 % ooOoO0O00 / I1ii11iIi11i . o0o00Oo0O
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 iiIi1IIiIi = O0 ( Oo0Oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 iIIi1Ii1III = O0 ( Oo0Oo0O )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 oOO00Oo = O0 ( i1iIIII1iiIIi )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 i1iIIIi1i = O0 ( i1I1IiI1ii )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 Oooo00 = O0 ( O0000Oo00o )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 48 - 48: Ii1I % IIiIiII11i + iIII
 if 25 - 25: o0O00o * I11i / oOo0O0Ooo . o0O00o % IIiIiII11i
 if 50 - 50: OOooOOo * IIIIiiII111
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / iIII
 if 92 - 92: I11i
 if 8 - 8: IIIIiiII111 + Ii1I . Ii1i1i
 if 50 - 50: I1ii11iIi11i
 if 16 - 16: Ii1i1i - OOooOOo % I1ii11iIi11i / Ii1i1i . iIII + oOOoOooOo
 i1I111Ii = O0 ( Ii1I1 )
 if 78 - 78: iI11I1II1I1I + oO0o + Ii
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for Oo0o00OO0000 , iiIiii1IIIII in II1iI :
   Ii1IiI1III11 = O0 ( Oo0o00OO0000 )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , O00O00OoO in I1IIII1i1 :
    O00O00OoO = ( O00O00OoO . replace ( '.' , ' ' ) )
    if OoO00oo00 in O00O00OoO . lower ( ) :
     if '.mkv' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + oOO0 , 222 , '' , '' , '' )
     elif '.mp4' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + oOO0 , 222 , '' , '' , '' )
     elif '.avi' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + oOO0 , 222 , '' , '' , '' )
     elif '.wav' in oOO0 :
      oOOOoo0O0oO ( ( '[COLOR' + II11iiii1Ii + ']' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + oOO0 , 222 , '' , '' , '' )
     else :
      OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + oOO0 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 21 - 21: I1ii11iIi11i + Ii1i1i % oOOoOooOo + OOooOOo % iIII
      OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiIi1IIiIi )
  for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in I1Ii :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source Technica[/COLOR]' ) , Oo0o00OO0000 , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 22 - 22: ooOoO0O00 / ii . oO0o
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: oOo0O0Ooo - ii + Ii1I . Ii1i1i / I11i + oOOoOooOo
 if oOO00Oo != 'Failed' :
  II1iIi1IiIii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oOO00Oo )
  for iii , iiIiii1IIIII in II1iIi1IiIii :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1iIIII1iiIIi + iii ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if i1iIIIi1i != 'Failed' :
  iI111i11iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIIi1i )
  for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in iI111i11iI1 :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    oOOOoo0O0oO ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORred] source RaizTv[/COLOR]' ) , Oo0o00OO0000 , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 90 - 90: oOo0O0Ooo - Ii
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 42 - 42: IIIi11I1 . I1ii11iIi11i
    if 21 - 21: IIIIiiII111 . oOo0O0Ooo / iIII
    if 97 - 97: iI11I1II1I1I + ooOoO0O00 - I11i
    if 73 - 73: oO0o - Ii % o0O0Oooo0O / I1ii11iIi11i - ii % IIIi11I1
    if 79 - 79: oOo0O0Ooo / I11i . Ii1i1i * Ii1I + iIII
    if 96 - 96: oO0o * IIiIiII11i
    if 1 - 1: oOo0O0Ooo - OOooOOo
    if 74 - 74: OOooOOo * IIiIiII11i + o0o00Oo0O + iIII
    if 3 - 3: iI11I1II1I1I - ooOoO0O00 / IIIIiiII111 + ooOoO0O00 + o0o00Oo0O
    if 18 - 18: iI11I1II1I1I . IIIIiiII111 % IIIi11I1 % ooOO0O0ooOooO + iI11I1II1I1I * ii
    if 78 - 78: o0O00o
    if 38 - 38: oO0o * Ii1I
    if 4 - 4: oO0o . Ii1I
    if 21 - 21: Ii / oO0o / Ii1I * o0o00Oo0O - IIiIiII11i * IIIi11I1
    if 27 - 27: I11i . OOooOOo * Ii1i1i * IIIIiiII111 * o0o00Oo0O
    if 93 - 93: o0O00o % o0O0Oooo0O % IIiIiII11i
    if 20 - 20: ii * o0O0Oooo0O
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
 ooiI1i = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
 for IIII1iIIii in ooiI1i :
  IiiOooooOo0 = OOO00O + IIII1iIIii + I11iii1Ii
  Oooo00 = O0 ( IiiOooooOo0 )
  if Oooo00 != 'Failed' :
   II1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oooo00 )
   for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in II1iI :
    if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
     oOOOoo0O0oO ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , Oo0o00OO0000 , 222 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 11 - 11: I11i * oO0o
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 92 - 92: OOooOOo . I1ii11iIi11i * iIII
 ooiI1i = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 86 - 86: o0o00Oo0O
 if 55 - 55: Ii1i1i / o0O0Oooo0O / Ii1I % oOOoOooOo % oOo0O0Ooo
 for IIII1iIIii in ooiI1i :
  IiiOooooOo0 = o0O00Oooo + IIII1iIIii
  iiI1ii111 = O0 ( IiiOooooOo0 )
  if iiI1ii111 != 'Failed' :
   OoOOIIIIIiI11Ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( iiI1ii111 )
   for iii , iiIiii1IIIII in OoOOIIIIIiI11Ii :
    if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
     iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0O00Oooo + IIII1iIIii + iii ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 55 - 55: ooOO0O0ooOooO + ii % ooOoO0O00
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: Ii1I - I1ii11iIi11i
def OOooo0O ( ) :
 if 36 - 36: oOo0O0Ooo . IIIi11I1 % IIiIiII11i * o0O00o
 if 34 - 34: iIII % IIIIiiII111 - oOOoOooOo - oOo0O0Ooo
 if 44 - 44: Ii1i1i . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
 if 22 - 22: iIII * Ii1I . ii / I1ii11iIi11i / Ii1i1i
 if 54 - 54: o0O0Oooo0O % Ii1i1i + oOOoOooOo
 if 45 - 45: Ii1i1i / ooOO0O0ooOooO * o0O0Oooo0O . Ii1i1i
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
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 if 51 - 51: iIII + oOOoOooOo / oOo0O0Ooo
 if 3 - 3: iI11I1II1I1I / IIIi11I1 % ooOO0O0ooOooO . Ii1i1i - Ii1i1i
 oOO0 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 Oo0Oo0O = 'http://onlinemovies.tube/?s=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 i1iIIII1iiIIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1I1IiI1ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 Ooo0OOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 ooooOoo0OO = 'http://www.tvmaze.com/search?q=' + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 Oo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 O0000Oo00o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 55 - 55: Ii % ii + o0o00Oo0O
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 7 - 7: oOOoOooOo - Ii * IIIIiiII111 / Ii1i1i - I11i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 62 - 62: I11i - iI11I1II1I1I . iIII . Ii1i1i * Ii1i1i
 if 24 - 24: iIII
 ooOOo00 = O0 ( oOO0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 iiIi1IIiIi = O0 ( Oo0Oo0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 oOO00Oo = O0 ( i1iIIII1iiIIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 i1iIIIi1i = O0 ( i1I1IiI1ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 iiI1ii111 = O0 ( Ooo0OOO )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 I1II = O0 ( ooooOoo0OO )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/11 Links" )
 iIIi1Ii1III = O0 ( Oo0 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 Oooo00 = O0 ( O0000Oo00o )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / iIII
 if 60 - 60: oOOoOooOo - Ii1i1i . oOo0O0Ooo * ooOO0O0ooOooO * Ii
 if Oooo00 != 'Failed' :
  II1iI = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oooo00 )
  for Oo0o00OO0000 , iiIiii1IIIII in II1iI :
   Ii1IiI1III11 = O0 ( Oo0o00OO0000 )
   I1IIII1i1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Ii1IiI1III11 )
   for oOO0 , O00O00OoO in I1IIII1i1 :
    if OoO00oo00 in O00O00OoO . lower ( ) :
     OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']*' + O00O00OoO + '-[COLORgold] source ' + iiIiii1IIIII + '[/COLOR]' ) , Oo0o00OO0000 + oOO0 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 29 - 29: oO0o - I1ii11iIi11i . ooOO0O0ooOooO / oO0o % Ii
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iIIi1Ii1III != 'Failed' :
  OOooO0Oo0o000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1Ii1III )
  for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in OOooO0Oo0o000 :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] source HeroVision[/COLOR]' ) , Oo0o00OO0000 , 1016 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 26 - 26: oOOoOooOo . o0O0Oooo0O / IIiIiII11i % Ii1i1i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 82 - 82: IIIi11I1 % o0o00Oo0O % iI11I1II1I1I % o0O00o + Ii
 if I1II != 'Failed' :
  o0OOooO = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( I1II )
  for Oo0o00OO0000 , iII11 , iiIiii1IIIII in o0OOooO :
   Oo0Oo0O = 'http://www.tvmaze.com' + Oo0o00OO0000 . replace ( '"' , '' )
   iiiI1i11Ii = requests . get ( Oo0Oo0O ) . content
   Ii1i1iI1iIIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiiI1i11Ii )
   for i11II1I11I1 in Ii1i1iI1iIIi :
    if not '<div>' in i11II1I11I1 :
     iIiII = i11II1I11I1 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
    iII11 = 'http:' + iII11
    iiIiii1IIIII = iiIiii1IIIII . replace ( '&#039;' , '' )
    if iiIiii1IIIII == '' :
     i1i1IIIIIIIi = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( Oo0o00OO0000 ) )
     for iiIiii1IIIII in i1i1IIIIIIIi :
      iiIiii1IIIII = iiIiii1IIIII . replace ( '-' , ' ' )
   Iii ( iiIiii1IIIII + '-[COLORgold] source Scraper[/COLOR]' , Oo0Oo0O , 9110002 , iII11 , iIi1ii1I1 , iIiII , '' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 20 , "" , "Getting Scraper Links" )
   if 64 - 64: ooOoO0O00 / o0O00o . o0O00o - o0O0Oooo0O % IIIi11I1 . IIiIiII11i
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  oooO = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iiIi1IIiIi )
  for Oo0o00OO0000 , iII11 , iiIiii1IIIII , oo0OoOO0000 in I1Ii :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    if 'season' in oo0OoOO0000 :
     I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , Oo0o00OO0000 , 90054 , iII11 , iII11 , '' )
    if 'episodes' in oo0OoOO0000 :
     I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' - [COLORred]Source - Tv HUB[/COLOR]' , Oo0o00OO0000 , 90044 , iII11 , iII11 , '' )
  for Oo0o00OO0000 in oooO :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , Oo0o00OO0000 , 90053 , iiiiiIIii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 78 - 78: o0O0Oooo0O - o0o00Oo0O - o0O0Oooo0O . iI11I1II1I1I % Ii1I . ii
   OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if ooOOo00 != 'Failed' :
  I1iiIIIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( ooOOo00 )
  for Oo0o00OO0000 , iiIiii1IIIII , iII11 in I1iiIIIi11 :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + ( iiIiii1IIIII ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , Oo0o00OO0000 , 8022 , iII11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 64 - 64: o0O00o
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: I11i - oOOoOooOo * ii . ii
    if 17 - 17: IIIi11I1 - IIIIiiII111 % oOo0O0Ooo * IIIi11I1 * iI11I1II1I1I . I11i
    if 58 - 58: ooOO0O0ooOooO - IIiIiII11i + o0o00Oo0O
    if 54 - 54: iI11I1II1I1I - o0O00o - o0O00o
    if 18 - 18: Ii + iI11I1II1I1I . Ii
    if 63 - 63: IIIIiiII111 - oO0o * IIIi11I1
    if 89 - 89: IIIIiiII111 / I1ii11iIi11i
    if 66 - 66: I11i + OOooOOo % ii . iIII
    if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
 if oOO00Oo != 'Failed' :
  II1iIi1IiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOO00Oo )
  for iiIiii1IIIII in II1iIi1IiIii :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( i1iIIII1iiIIi + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 93 - 93: ooOoO0O00 + o0O0Oooo0O / oO0o - iIII % I1ii11iIi11i / Ii1i1i
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if i1iIIIi1i != 'Failed' :
  iI111i11iI1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1iIIIi1i )
  for iiIiii1IIIII in iI111i11iI1 :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1I1IiI1ii + iiIiii1IIIII ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 1 - 1: I1ii11iIi11i / Ii1i1i . Ii % IIIi11I1 + I11i + o0o00Oo0O
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiI1ii111 != 'Failed' :
  OoOOIIIIIiI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI1ii111 )
  for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in OoOOIIIIIiI11Ii :
   if OoO00oo00 in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLORred]*[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '-[COLORgold] Source Scooby[/COLOR]' ) , Oo0o00OO0000 , 1016 , ii1IiIiI1 , oOO0o0oo0 , i11II1I11I1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 54 - 54: o0O0Oooo0O + oOOoOooOo % o0O00o
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: I11i * iI11I1II1I1I
 III1iiiII1ii = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IIII1iIIii in III1iiiII1ii :
  IiiOooooOo0 = OOO00O + IIII1iIIii + I11iii1Ii
  iIi11iiI11 = O0 ( IiiOooooOo0 )
  if iIi11iiI11 != 'Failed' :
   II1OoooOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIi11iiI11 )
   for iiIiii1IIIII , i11II1I11I1 , Oo0o00OO0000 , iII11 , ooo0O0o00O , o0OO in II1OoooOo :
    if OoO00oo00 in iiIiii1IIIII . lower ( ) :
     OoOOoOooooOOo ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - Source Pandoras[/COLOR]' , Oo0o00OO0000 , o0OO , iII11 , ooo0O0o00O , i11II1I11I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 36 - 36: OOooOOo + IIiIiII11i - oO0o % oOOoOooOo * ooOoO0O00
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
     if 4 - 4: Ii1i1i + oO0o * Ii1I
     if 13 - 13: OOooOOo - o0O00o * iI11I1II1I1I * o0o00Oo0O
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIIiI ( ) :
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o00OO0000 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( IIIIIiII1 ) . replace ( ' ' , '+' )
 if 8 - 8: Ii1I * o0O00o / I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0000OOo00 = O0 ( Oo0o00OO0000 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 99 - 99: IIIi11I1 * o0O0Oooo0O . oOOoOooOo - ooOoO0O00 - iIII % o0O00o
 if oO0000OOo00 != 'Failed' :
  I1Ii = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , iiIiii1IIIII in I1Ii :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + Oo0o00OO0000 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 40 - 40: OOooOOo % o0O0Oooo0O / oOo0O0Ooo + ooOoO0O00
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
o000ooOo0o0Oo = '{ZH},' ; o0OO0 = '{IX},' ; II111Iiii1 = '{LM},'
if 50 - 50: ooOO0O0ooOooO
def oOO0Oo00o ( url ) :
 oOooOoOOOO0Oo = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( oOooOoOOOO0Oo )
 for url , oo0OOoOoo0O0O , iiI11ii1111 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( oo0OOoOoo0O0O ) . replace ( 'Sezon' , ' Season ' ) + ( iiI11ii1111 ) . replace ( 'Bölüm' , ' Episode ' ) + iiIiii1IIIII , url , 8063 , '' )
  if 91 - 91: Ii1I * Ii1i1i * o0O0Oooo0O
  if 98 - 98: oOOoOooOo
  if 38 - 38: o0o00Oo0O * ooOoO0O00 - oO0o * oO0o
  if 11 - 11: oOOoOooOo - Ii1i1i . ooOO0O0ooOooO * Ii1i1i
def o0Oo ( url ) :
 oOooOoOOOO0Oo = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oOooOoOOOO0Oo )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( iiIiii1IIIII , url , 222 , '' )
  if 17 - 17: ii . IIIi11I1
  if 32 - 32: OOooOOo . ooOO0O0ooOooO + o0o00Oo0O
  if 100 - 100: o0o00Oo0O / IIIi11I1 - oOOoOooOo
  if 15 - 15: IIIIiiII111 - o0o00Oo0O - ii
def iiiiIIiiII1Iii1 ( ) :
 if 93 - 93: OOooOOo % Ii1i1i / Ii1i1i - oOOoOooOo - o0O00o % oOOoOooOo
 oOooOoOOOO0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i1iI1iIIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oOooOoOOOO0Oo )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII , iiI11ii1111 in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII + '  -  ' + ( iiI11ii1111 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Oo0o00OO0000 , 8063 , iII11 )
  if 9 - 9: ii * oOo0O0Ooo - I1ii11iIi11i / Ii * IIIIiiII111
def oOOo0o0O0oO0o ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 8002 , iII11 )
def iiIi ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , time , url , iiIiii1IIIII , iiIi1 in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( '%s %s' % ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , time ) , url , 1015 , iII11 , iiIi1 )
  if 90 - 90: IIiIiII11i
def I1Ii1iiI1 ( ) :
 if 77 - 77: I11i . I11i * o0O0Oooo0O + IIIi11I1 - Ii
 I111I11I111 ( 'Coronation Street' , '' , 8001 , '' )
 I111I11I111 ( 'Eastenders' , '' , 8002 , '' )
 I111I11I111 ( 'Emmerdale' , '' , 8003 , '' )
 I111I11I111 ( 'Hollyoaks' , '' , 8004 , '' )
 I111I11I111 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 45 - 45: oOo0O0Ooo . oOo0O0Ooo - I1ii11iIi11i * IIIi11I1
 if 71 - 71: ooOoO0O00 / iIII
 if 14 - 14: ii
 if 99 - 99: I11i * I11i
def Ii1II1I ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Holly' in iiIiii1IIIII :
   iII11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in Oo0o00OO0000 :
    iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 5 - 5: IIIi11I1 . IIIIiiII111 . ooOO0O0ooOooO % o0O00o * o0o00Oo0O
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 20 - 20: I1ii11iIi11i . oOo0O0Ooo . oOo0O0Ooo / ii . ii + iI11I1II1I1I
def oO00o ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'East' in iiIiii1IIIII :
   iII11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in Oo0o00OO0000 :
    iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 32 - 32: Ii + IIiIiII11i + IIiIiII11i % iIII
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: I11i
def O0o0o00O0OO00 ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Emmer' in iiIiii1IIIII :
   iII11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in Oo0o00OO0000 :
    iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 100 - 100: oO0o
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: o0O0Oooo0O - oOOoOooOo + I1ii11iIi11i . oOo0O0Ooo % iI11I1II1I1I
def IiIIi1I ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Coro' in iiIiii1IIIII :
   iII11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in Oo0o00OO0000 :
    iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 5 - 5: Ii + iIII . o0O00o
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: Ii / iI11I1II1I1I - Ii1I * Ii1I
def oOooOO00OO ( ) :
 oO0000OOo00 = i11oO0oOo0 ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Celeb' in iiIiii1IIIII :
   iII11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in Oo0o00OO0000 :
    iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Oo0o00OO0000 . replace ( '\\/' , '/' ) , 8006 , iII11 )
   else :
    pass
    if 47 - 47: iI11I1II1I1I / ii - Ii + iIII
def iI1Iii11Iii11 ( name , url ) :
 iIiiI = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if iIiiI :
  OOo000 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  O0o0O0 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( O0o0O0 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  O0o0O0 = open_url ( url )
  iI1iIIiIi1I1 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( O0o0O0 ) [ - 1 ]
  OOo000 = iI1iIIiIi1I1 . replace ( '\\/' , '/' )
 I1I1 = xbmcgui . ListItem ( name , '' , '' )
 I1I1 . setPath ( OOo000 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1 )
 if 85 - 85: oO0o + IIiIiII11i
 if 87 - 87: oO0o
def o0oOiiI1 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 Ii1i1iI1iIIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , Oo0o00OO0000 , 7071 , iiiiiIIii + 'popcorn.png' )
 for Oo0o00OO0000 , iiIiii1IIIII in I1Ii :
  I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , Oo0o00OO0000 , 7071 , iiiiiIIii + 'popcorn.png' )
  if 64 - 64: OOooOOo
def iIiiii ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i1iI1iIIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Movies' in iiIiii1IIIII :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( Oo0o00OO0000 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiiiiIIii + 'popcorn.png' )
def ii111Ii ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iII11 )
 for url in I1Ii :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiiiiIIii + 'Next.png' )
  if 82 - 82: OOooOOo * iIII . o0O0Oooo0O . ooOO0O0ooOooO . I11i
  if 58 - 58: o0O0Oooo0O * oO0o * ooOoO0O00
def iI111i1I1II ( url ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i1iI1iIIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  if '{{' in iiIiii1IIIII :
   pass
  else :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iII11 )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
IiiIi1II = '{UJ},' ; IiII1IiiI = '{WE},' ; oOoo00OO0 = '{WP},' ; Iii11i1111II = '{PP},'
def oOoo0OoooOo0o ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  if '{{' in iiIiii1IIIII :
   pass
  else :
   I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iII11 )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOoooOOO0o0 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  i11iII1Ii1ii111 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def i11iII1Ii1ii111 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iiiiiIIii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: Ii1i1i
 if 44 - 44: o0O0Oooo0O % OOooOOo + o0O0Oooo0O / oO0o
 if 73 - 73: I1ii11iIi11i . iIII * IIIIiiII111 . Ii1I . o0o00Oo0O
def iiIiIi1I1 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O0o0O0 )
 I1Ii = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '(cooltvseries.com)' in iiIiii1IIIII :
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiiiiIIii + 'CoolSeries.png' )
 for url , iiIiii1IIIII in I1Ii :
  if '(cooltvseries.com)' in iiIiii1IIIII :
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiiiiIIii + 'CoolSeries.png' )
def ii11I1IIII11 ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  ooOoOOoooO000 ( ( url ) . replace ( ' ' , '%20' ) )
iiI1II11I1iI = '{XX},' ; IIIiI = '{UD},' ; I11111IiI1I = '{YT},' ; Oo0O0 = '{JS},' ; IIiiiI1ii1I = '{PF},'
if 94 - 94: IIIi11I1 - oOo0O0Ooo * o0O0Oooo0O / ooOoO0O00
def II11 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 Ii1i1iI1iIIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( Oo0o00OO0000 ) ) , 222 , iII11 )
  if 88 - 88: ii
def I11iiI11I1II ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( O0o0O0 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'youtu' in url :
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iII11 )
 for url in next :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NEXT[/COLOR]' , url , 7050 , iiiiiIIii + 'Next.png' )
  if 60 - 60: o0O0Oooo0O * IIIIiiII111 / ii * I1ii11iIi11i
def I11I1iI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 65 - 65: IIIi11I1 . IIiIiII11i * Ii + IIIi11I1
def oOOo0OO0oo ( url ) :
 O0o0O0 = i11oO0oOo0
 Ii1i1iI1iIIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 222 , iII11 )
  if 68 - 68: ooOO0O0ooOooO % Ii1i1i - IIIi11I1 / ooOoO0O00
  if 1 - 1: ii * iI11I1II1I1I + o0o00Oo0O * o0O00o
  if 42 - 42: o0o00Oo0O . o0O0Oooo0O / iIII
  if 69 - 69: OOooOOo / o0O0Oooo0O * oOo0O0Ooo
  if 76 - 76: o0o00Oo0O + IIiIiII11i * oO0o
def iI1IIi1I ( ) :
 if 42 - 42: ii / o0O00o * IIiIiII11i
 I111I11I111 ( 'All Channels' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Entertainment' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Movies' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Music' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'News' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Sports' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Documentary' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Kids' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Food' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Religious' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'USA Channels' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 I111I11I111 ( 'Other' , '' , 7021 , iiiiiIIii + 'livetv.png' )
 if 77 - 77: IIiIiII11i + IIIIiiII111 . I11i / o0O0Oooo0O
 if 100 - 100: Ii1i1i
def O0O0OoO0o0OO ( Cat_Name ) :
 if 18 - 18: Ii / I11i - ooOO0O0ooOooO . iIII * ooOoO0O00
 oO0OO00OO0O = False
 iIii = '0'
 if Cat_Name == 'All Channels' : oO0OO00OO0O = True
 if Cat_Name == 'Entertainment' : iIii = '1'
 if Cat_Name == 'Movies' : iIii = '2'
 if Cat_Name == 'Music' : iIii = '3'
 if Cat_Name == 'News' : iIii = '4'
 if Cat_Name == 'Sports' : iIii = '5'
 if Cat_Name == 'Documentary' : iIii = '6'
 if Cat_Name == 'Kids' : iIii = '7'
 if Cat_Name == 'Food' : iIii = '8'
 if Cat_Name == 'Religious' : iIii = '9'
 if Cat_Name == 'USA Channels' : iIii = '10'
 if Cat_Name == 'Other' : iIii = '11'
 if 32 - 32: ooOoO0O00
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i1iI1iIIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( O0o0O0 )
 print 'Len Match: >>>' + str ( len ( Ii1i1iI1iIIi ) )
 for iiIiii1IIIII , iII11 , ooO0OOOooo in Ii1i1iI1iIIi :
  IiIIiIiI1ii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iII11 ) . replace ( '\\' , '' )
  if ooO0OOOooo == iIii :
   I111I11I111 ( iiIiii1IIIII , '' , 7022 , IiIIiIiI1ii )
  elif oO0OO00OO0O == True :
   I111I11I111 ( iiIiii1IIIII , '' , 7022 , IiIIiIiI1ii )
  else : pass
  if 10 - 10: Ii1i1i - IIiIiII11i / Ii * oOo0O0Ooo / o0o00Oo0O . iIII
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 67 - 67: OOooOOo - oOOoOooOo - iI11I1II1I1I
def Ii1IiiI ( Search_Name ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i1iI1iIIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( O0o0O0 )
 for iII11 , Oo0o00OO0000 , Oo0Oo0O , i1iIIII1iiIIi in Ii1i1iI1iIIi :
  IiIIiIiI1ii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iII11 ) . replace ( '\\' , '' )
  iiiiI11ii ( Search_Name + ': Link 1' , ( Oo0o00OO0000 ) . replace ( '\\' , '' ) , 222 , IiIIiIiI1ii )
  iiiiI11ii ( Search_Name + ': Link 2' , ( Oo0Oo0O ) . replace ( '\\' , '' ) , 222 , IiIIiIiI1ii )
  iiiiI11ii ( Search_Name + ': Link 3' , ( i1iIIII1iiIIi ) . replace ( '\\' , '' ) , 222 , IiIIiIiI1ii )
  if 73 - 73: ooOO0O0ooOooO / IIIi11I1 * IIiIiII11i % ii - ooOoO0O00 - oOOoOooOo
def II11iI ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  iiiiI11ii ( iiIiii1IIIII , ( Oo0o00OO0000 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiiiiIIii + 'english.png' )
def I1I1iII1I1I11 ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  iiiiI11ii ( iiIiii1IIIII , ( Oo0o00OO0000 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiiiiIIii + 'xxx.png' )
def IiIII ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , Oo0o00OO0000 in Ii1i1iI1iIIi :
  iiiiI11ii ( iiIiii1IIIII , ( Oo0o00OO0000 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiiiiIIii + 'vod(1).png' )
  if 32 - 32: Ii - ii + iIII . ooOoO0O00
def iI11i1Ii ( url ) :
 url
 IIi1IIIi = xbmcgui . ListItem ( iiIiii1IIIII , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIi1IIIi )
 return
 if 82 - 82: IIIIiiII111 + iIII * oO0o - Ii1I % IIIIiiII111
 if 99 - 99: o0o00Oo0O % oO0o % ooOoO0O00 / I11i
def OOoOoOOo ( url ) :
 O0o0O0 = i11oO0oOo0 ( 'http://www.fitnessblender.com/videos/' )
 Ii1i1iI1iIIi = re . compile ( '"id":.+?,"title":"([^"]*)","is_featured":"1","minutes":"([^"]*)","burnmin":"([^"]*)","burnmax":"([^"]*)","burnavg":"([^"]*)","difficulty":"([^"]*)","([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( O0o0O0 )
 for iiIiii1IIIII , time , iI11Ii1i , II111I , Ii11IIIi1I , IIII1Ii1II1 , iII11 , url , IiiIiIiIIIii1 , OOOo0oOOO in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , 'https://www.fitnessblender.com/videos/' + url , 7086 , 'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-' + iII11 , '' , ( 'Calorie burn:[CR]' + iI11Ii1i + ' - ' + II111I + ' Average = ' + Ii11IIIi1I + '[CR][CR]Difficulty = ' + IIII1Ii1II1 + '[CR][CR]Equipment Needed: ' + IiiIiIiIIIii1 + '[CR][CR]Focus: ' + OOOo0oOOO ) )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 for url in I1Ii :
  I111I11I111 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiiiiIIii + 'Next.png' )
  if 87 - 87: oOOoOooOo * I1ii11iIi11i / IIIIiiII111 + iIII + Ii1i1i
def OooO00O0OOOO ( url ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for url , i11II1I11I1 , iII11 in Ii1i1iI1iIIi :
  oOOOoo0O0oO ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iII11 , '' , i11II1I11I1 )
  OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 oO0oO0OoO00 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for O0ooOOo0 in oO0oO0OoO00 :
  IIII1iII = ( O0ooOOo0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  OoOOoOooooOOo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iII11 , '' , IIII1iII )
  if 32 - 32: o0o00Oo0O + o0O0Oooo0O
def iIiiIIIOo ( INFO ) :
 I1iI1ii1II ( 'info for workout' , INFO )
 if 64 - 64: oO0o + o0O00o . oOOoOooOo / ooOO0O0ooOooO % I11i + IIiIiII11i
 if 98 - 98: o0O0Oooo0O / IIIIiiII111 * o0O00o + oOOoOooOo
 if 82 - 82: ooOoO0O00
def iII1 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( ( iiIiii1IIIII ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiiiiIIii + 'Sport.png' )
def I1i11I ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , url , 9032 , iiiiiIIii + 'icon.png' )
def I1iiIiI1II1ii ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '=' in iiIiii1IIIII :
   pass
  else :
   iiiiI11ii ( ( iiIiii1IIIII ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiiiiIIii + 'icon.png' )
def IiI1II1iIi ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  if '=' in iiIiii1IIIII :
   pass
  else :
   iiiiI11ii ( iiIiii1IIIII , url , 222 , iiiiiIIii + 'icon.png' )
   if 30 - 30: IIiIiII11i + iI11I1II1I1I / iIII
   if 58 - 58: o0O0Oooo0O - iIII + ooOO0O0ooOooO * oO0o
   if 45 - 45: o0O00o * IIIi11I1 . oO0o
def O0o0ooO0oO0oO ( url ) :
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
def iI1iII111ii1I ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url , iII11 in Ii1i1iI1iIIi :
  Ooo00OoOOO ( iiIiii1IIIII , url , 100009 , iII11 , iII11 , '' , '' )
  if 97 - 97: ooOO0O0ooOooO - IIIIiiII111 + o0O00o . OOooOOo + iI11I1II1I1I
def O0o000 ( url ) :
 Iii ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 Iii ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 O0o0O0 = requests . get ( url ) . text
 i1ii1II1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1II1I11i1 = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiI1i11Ii = requests . get ( url ) . text
  Ii1i11iIi1iII = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( iiiI1i11Ii )
  for i1i1Ii in Ii1i11iIi1iII :
   Iiio0Oo0oO = requests . get ( i1i1Ii ) . text
   Ii1i1iI1iIIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Iiio0Oo0oO )
   for oOoO00o , iI11IIi1iiI1I , i1iII1IiiIiI1 , ooIii , I1I1IiI1 in Ii1i1iI1iIIi :
    if oOoO00o == 'xyz' :
     ooooo0 = 'http://xyz.streamjunkie.tv/hls/' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( iiIiii1IIIII , ooooo0 , 1001111 , iII11 , iII11 , '' , '' )
    else :
     ooooo0 = 'http://' + ooIii + '.' + i1iII1IiiIiI1 + '.' + iI11IIi1iiI1I + '.' + oOoO00o + '/hls/,' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( iiIiii1IIIII , ooooo0 , 1001111 , iII11 , iII11 , '' , '' )
 for o0o0oOoOO0O in i1ii1II1ii :
  Iii ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0o0oOoOO0O , 1000111 , '' , '' , '' , '' )
  if 7 - 7: I1ii11iIi11i + o0O00o
  if 15 - 15: iI11I1II1I1I % OOooOOo + ooOoO0O00 . Ii1i1i - I1ii11iIi11i
  if 91 - 91: oOo0O0Ooo - ii - ii
def o0ooo000o00O ( ) :
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
 if 7 - 7: o0O0Oooo0O / Ii1i1i * IIiIiII11i * OOooOOo - ii
 if 92 - 92: OOooOOo . ooOoO0O00
def iI1i1i ( url , name ) :
 Iii ( name , '' , '' , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 O0o0O0 = requests . get ( url ) . text
 i1ii1II1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1II1I11i1 = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iII11 , name in Ii1i1iI1iIIi :
  iiiI1i11Ii = requests . get ( url ) . text
  Ii1i11iIi1iII = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( iiiI1i11Ii )
  for i1i1Ii in Ii1i11iIi1iII :
   Iiio0Oo0oO = requests . get ( i1i1Ii ) . text
   Ii1i1iI1iIIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Iiio0Oo0oO )
   for oOoO00o , iI11IIi1iiI1I , i1iII1IiiIiI1 , ooIii , I1I1IiI1 in Ii1i1iI1iIIi :
    if oOoO00o == 'xyz' :
     ooooo0 = 'http://xyz.streamjunkie.tv/hls/' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , ooooo0 , 1001111 , iII11 , iII11 , '' , '' )
    else :
     ooooo0 = 'http://' + ooIii + '.' + i1iII1IiiIiI1 + '.' + iI11IIi1iiI1I + '.' + oOoO00o + '/hls/,' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , ooooo0 , 1001111 , iII11 , iII11 , '' , '' )
     if 83 - 83: o0o00Oo0O
 for o0o0oOoOO0O in i1ii1II1ii :
  Iii ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0o0oOoOO0O , 1003111 , '' , '' , '' , '' )
  if 27 - 27: I11i + oOo0O0Ooo - o0O00o . Ii . oOo0O0Ooo
  if 25 - 25: o0o00Oo0O + IIIi11I1 / IIIIiiII111
def oO0ooooooO ( ) :
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
 if 42 - 42: Ii * o0o00Oo0O % Ii + IIIi11I1
 if 64 - 64: oOo0O0Ooo / OOooOOo
 if 6 - 6: Ii - IIIIiiII111 * ooOoO0O00 - IIIIiiII111
def I1ii ( url , name ) :
 Iii ( name , '' , '' , '' , '' , '' , '' )
 Iii ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 O0o0O0 = requests . get ( url ) . text
 i1ii1II1ii = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1II1I11i1 = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( O0o0O0 )
 Ii1i1iI1iIIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( Ii1II1I11i1 ) )
 for url , iII11 , name in Ii1i1iI1iIIi :
  iiiI1i11Ii = requests . get ( url ) . text
  Ii1i11iIi1iII = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( iiiI1i11Ii )
  for i1i1Ii in Ii1i11iIi1iII :
   Iiio0Oo0oO = requests . get ( i1i1Ii ) . text
   Ii1i1iI1iIIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Iiio0Oo0oO )
   for oOoO00o , iI11IIi1iiI1I , i1iII1IiiIiI1 , ooIii , I1I1IiI1 in Ii1i1iI1iIIi :
    if oOoO00o == 'xyz' :
     ooooo0 = 'http://xyz.streamjunkie.tv/hls/' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , ooooo0 , 1001111 , iII11 , iII11 , '' , '' )
    else :
     ooooo0 = 'http://' + ooIii + '.' + i1iII1IiiIiI1 + '.' + iI11IIi1iiI1I + '.' + oOoO00o + '/hls/,' + I1I1IiI1 + ',.urlset/master.m3u8'
     Ooo00OoOOO ( name , ooooo0 , 1001111 , iII11 , iII11 , '' , '' )
     if 19 - 19: oOOoOooOo
 for o0o0oOoOO0O in i1ii1II1ii :
  Iii ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0o0oOoOO0O , 1005111 , '' , '' , '' , '' )
def IiiiI ( name , url ) :
 import urlresolver
 try :
  iiIIi = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiIIi , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 44 - 44: o0O0Oooo0O - Ii * oOo0O0Ooo
 if 84 - 84: o0o00Oo0O % Ii1i1i
 if 3 - 3: oOo0O0Ooo . iIII / Ii1I
def I1i1ii ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 Ii1i1iI1iIIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'Daily' in iiIiii1IIIII :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , Oo0o00OO0000 , 9008 , o0 )
def ii1iIiIIiIIii ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , o0 )
def ooooo ( url ) :
 iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 iiiiI11ii ( '[COLOR' + II11iiii1Ii + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  iiiiI11ii ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) , url , 222 , o0 )
  if 19 - 19: Ii1i1i * iIII . IIiIiII11i
def oooOo ( ) :
 O0o0O0 = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '.m3u' in Oo0o00OO0000 :
   I111I11I111 ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + Oo0o00OO0000 ) , 9011 , iiiiiIIii + 'disclose.png' )
def OooOOo0 ( url ) :
 O0o0O0 = cloudflare . source ( url )
 Ii1i1iI1iIIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  iiiiI11ii ( ( iiIiii1IIIII ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 73 - 73: oO0o + IIIi11I1 + o0O00o - ooOoO0O00
def I11Oo00oO0O ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if 'category' in Oo0o00OO0000 :
   I111I11I111 ( iiIiii1IIIII , 'http://www.disclose.tv/' + Oo0o00OO0000 , 7010 , iiiiiIIii + 'disclose.png' )
   if 67 - 67: ii - ooOoO0O00 + Ii1i1i + oOo0O0Ooo
   if 18 - 18: I1ii11iIi11i * IIIIiiII111 / IIiIiII11i
def o00Ooo0Oo ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( O0o0O0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , iII11 in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , 'http://www.disclose.tv/' + url , 7011 , iII11 )
 for url in next :
  I111I11I111 ( 'NEXT' , url , 7010 , iiiiiIIii + 'Next.png' )
  if 85 - 85: o0O00o . o0O0Oooo0O % I1ii11iIi11i * IIIi11I1 % oOo0O0Ooo
  if 57 - 57: oO0o % o0O00o % o0O00o - ii % ooOoO0O00
def O0ooOoI11Iii1iIII1i ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( O0o0O0 )
 II1iIi1IiIii = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  if 'http' in url :
   iiiiI11ii ( 'video/flv' , url , 222 , iiiiiIIii + 'disclose.png' )
 for url , iiIiii1IIIII in I1Ii :
  iiiiI11ii ( iiIiii1IIIII , url , 222 , iiiiiIIii + 'disclose.png' )
 for url in II1iIi1IiIii :
  iiiiI11ii ( 'YT Link' , url , 8043 , iiiiiIIii + 'disclose.png' )
  if 79 - 79: IIiIiII11i - ooOO0O0ooOooO + ooOO0O0ooOooO
  if 76 - 76: o0o00Oo0O % o0O00o . I11i % o0O00o . I11i
def iioOo0oo ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiiiiIIii + 'icon.png' )
  if 54 - 54: Ii1I + Ii1I % iI11I1II1I1I
def O00i1IiI111II1 ( name , url , img ) :
 oO0000OOo00 = i11oO0oOo0 ( url )
 iiii11I1iIIII = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0000OOo00 )
 o0OoOOO0O = len ( iiii11I1iIIII )
 if 89 - 89: ooOO0O0ooOooO / Ii
 if 96 - 96: oOo0O0Ooo
 if o0OoOOO0O == 1 :
  for o0OoO0iiII1 in iiii11I1iIIII :
   o0OoO0iiII1 = o0OoO0iiII1 . replace ( 'player' , 'watch' )
   oOooO0o000 = o0OoO0iiII1 + '&fv=&sou='
   iioo = i11oO0oOo0 ( oOooO0o000 )
   O0oo0o0oO = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iioo )
   for oOoooooOoO in O0oo0o0oO :
    oooOO0 = False
    Resolve ( oOoooooOoO )
    if 89 - 89: oO0o * Ii - o0O00o * ooOoO0O00 - oOOoOooOo . Ii1i1i
 elif o0OoOOO0O > 1 :
  if 26 - 26: oOo0O0Ooo * ii / oOo0O0Ooo . o0o00Oo0O . oOOoOooOo + o0o00Oo0O
  for o0OoO0iiII1 in iiii11I1iIIII :
   O0OI1i = i11oO0oOo0 ( o0OoO0iiII1 )
   i1IIi = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( O0OI1i )
   O0Ooo = i1IIi
   O0Ooo = ( str ( O0Ooo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + O0Ooo
   iiiiI11ii ( 'DOUBLE LINK' , O0Ooo , 424 , '' )
   if 54 - 54: iI11I1II1I1I / IIIi11I1 + ooOO0O0ooOooO % OOooOOo * OOooOOo - IIiIiII11i
   for url in i1IIi :
    I111I11I111 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     Oo0Oo0O = Google . resolve ( url )
    except :
     pass
    try :
     I1i1I1i = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( Oo0Oo0O ) )
     for ooO0iiiIIIIIiIii1 , iii1II1iI1III in I1i1I1i :
      if 99 - 99: Ii * oOOoOooOo . oOo0O0Ooo % OOooOOo
      HD_URLS . append ( ooO0iiiIIIIIiIii1 )
      SD_URLS . append ( iii1II1iI1III )
    except :
     pass
 else :
  pass
  if 94 - 94: I1ii11iIi11i / o0O00o - ii * o0o00Oo0O - oO0o . Ii1i1i
def i1IIiO0o0O ( ) :
 if 96 - 96: Ii / oO0o % IIIIiiII111
 if 88 - 88: ooOO0O0ooOooO
 I111I11I111 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiiiiIIii + 'Movies.png' )
 if 82 - 82: IIIi11I1 - IIIIiiII111 * iI11I1II1I1I
 I111I11I111 ( 'Search Movies' , '' , 7017 , iiiiiIIii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 14 - 14: OOooOOo
 if 17 - 17: I1ii11iIi11i . ii % Ii1I / ii
def oO0OOOOo ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://cnfstudio.com/' )
 Ii1i1iI1iIIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , 'http://cnfstudio.com/genre/' + Oo0o00OO0000 , 7003 , iiiiiIIii + 'icon.png' )
  if 28 - 28: Ii1i1i
O0OoO000O0OO = xbmcgui . Dialog ( )
if 27 - 27: I1ii11iIi11i . iIII % oOo0O0Ooo * Ii
O000I1i1iI1II = '{UN},' ; OooO0ooOooO0o00oO = '{IG},' ; Ii1iiiIIIii = '{PL},' ; I1i1IIii = '{LO},' ; I1i1i1Ii1I = '{LP},' ; OOo0OoO00OO = '{HA},' ; OoOOoo = '{XD},' ; ii1I1ii = '{TA},' ; iIiI = '{DP},' ; oooOI1ii1I1i1 = '{JT},' ; i11iii = '{JJ},' ; oO0OoOoo00 = '{MM},' ; IIiiIi1i = '{FQ},' ; IiiiiI1iIi = '{HH},'
if 3 - 3: I1ii11iIi11i - IIIi11I1 * oO0o - IIiIiII11i . ii
def iII11iIII ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( O0o0O0 )
 ooOoIIi11iiI1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( O0o0O0 )
 for iII11 , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iII11 )
 ooOoIIi11iiI1 = ooOoIIi11iiI1
 for url in ooOoIIi11iiI1 :
  I111I11I111 ( 'Next Page' , url , 7003 , iiiiiIIii + 'Next.png' )
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
  II11IiI1 ( url )
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
    iiiiI11ii ( iiIiii1IIIII , Oo0o00OO0000 , 222 , iiiiiIIii + 'streams.png' )
 else :
  O0OoO000O0OO . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 100 - 100: oOOoOooOo + o0O0Oooo0O
def Ii1I1iIiIi ( url ) :
 if os . path . exists ( Remote ) :
  oO0000OOo00 = o00oiii11II1I ( url )
  Ii1i1iI1iIIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
  for iiIiii1IIIII , url in Ii1i1iI1iIIi :
   url = ( url ) . strip ( )
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
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
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 o0O0o = 'https://addons.tvaddons.ag/search/?keyword=' + OoO00oo00
 oO0000OOo00 = i11oO0oOo0 ( o0O0o )
 Ii1i1iI1iIIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0000OOo00 )
 for Oo0o00OO0000 , iI , iiIiii1IIIII in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , Oo0o00OO0000 , 10054 , 'https://addons.tvaddons.ag/' + iI , iIi1ii1I1 , '' )
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
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iI , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , url , 1007 , iI )
def O00oo0o ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iI , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 1006 , iI )
  if 76 - 76: ooOO0O0ooOooO - o0o00Oo0O / I1ii11iIi11i
def o0Ooo ( ) :
 O0o0O0 = i11oO0oOo0 ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
  ii1ii1iii1I ( iiIiii1IIIII , 100109 , Oo0o00OO0000 , image = ii1IiIiI1 , isFolder = True )
  if 24 - 24: ii + I11i * OOooOOo - IIIIiiII111 * ooOO0O0ooOooO
def OOoOO ( url ) :
 import random
 oO0O = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oO0O . clear ( )
 o000O00o0Ooo = [ ]
 Oo0oOoo00oo0O = [ ]
 Ii1i = [ ]
 oO0000OOo00 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0000OOo00 )
 for Oo0Oo0O , ii1IiIiI1 , i11II1I11I1 , ooo0O0o00O , iiIiii1IIIII in Ii1i1iI1iIIi :
  o000O00o0Ooo . append ( [ Oo0Oo0O , iiIiii1IIIII ] )
  if len ( o000O00o0Ooo ) == len ( Ii1i1iI1iIIi ) :
   for IIi1IIIi in o000O00o0Ooo :
    OO00OO = random . randint ( 1 , len ( o000O00o0Ooo ) )
    try :
     O000OOO0O0O = o000O00o0Ooo [ int ( OO00OO ) ]
    except :
     pass
    if len ( Oo0oOoo00oo0O ) <= 20 :
     if O000OOO0O0O [ 1 ] not in Ii1i :
      iiIi1IIiIi = i11oO0oOo0 ( O000OOO0O0O [ 0 ] )
      II1iIi1IiIii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iiIi1IIiIi )
      for Oo0o , O0OO0 in II1iIi1IiIii :
       i1iIIIi1i = i11oO0oOo0 ( Oo0o )
       iI111i11iI1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i1iIIIi1i )
       for OOOOo0o0O0 , I1I1IiI1 in iI111i11iI1 :
        if 'panda' in I1I1IiI1 :
         OooOO0oOOo0O = i11oO0oOo0 ( I1I1IiI1 )
         III1ii = re . compile ( "url: '(.+?)'" ) . findall ( OooOO0oOOo0O )
         for iIIOOoOOooO in III1ii :
          if 'http' in iIIOOoOOooO :
           I1I1 = xbmcgui . ListItem ( O000OOO0O0O [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : O000OOO0O0O [ 1 ] } )
           I1I1 . setProperty ( "IsPlayable" , "true" )
           oO0O . add ( iIIOOoOOooO , I1I1 )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1 )
           if 46 - 46: iIII - I1ii11iIi11i
def ii1ii1iii1I ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = o0
 I1 = sys . argv [ 0 ]
 I1 += '?mode=' + str ( mode )
 I1 += '&title=' + urllib . quote_plus ( name )
 I1 += '&image=' + urllib . quote_plus ( image )
 I1 += '&page=' + str ( page )
 if url != '' :
  I1 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  I1 += '&keyword=' + urllib . quote_plus ( keyword )
 I1I1 = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  I1I1 . addContextMenuItems ( contextMenu )
 if infoLabels :
  I1I1 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  I1I1 . setProperty ( "IsPlayable" , "true" )
 I1I1 . setProperty ( 'Fanart_Image' , iIi1ii1I1 )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = isFolder )
 if 86 - 86: Ii % ooOO0O0ooOooO
 if 37 - 37: IIIIiiII111
def iiIii1IIi ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iconimage , i11II1I11I1 , ooo0O0o00O , name in Ii1i1iI1iIIi :
  if 'http' in url :
   if '.php' in url :
    I1ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
    for IIi1IIIi in I1ii1 :
     if IIi1IIIi == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    oo00ooOOOo0O ( name , url , 1016 , iconimage , ooo0O0o00O , i11II1I11I1 )
   else :
    if 'youtube' in url :
     I1ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
     for IIi1IIIi in I1ii1 :
      if IIi1IIIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iiiiIiii1I11 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , ooo0O0o00O , i11II1I11I1 )
    else :
     I1ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
     for IIi1IIIi in I1ii1 :
      if IIi1IIIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iiiiIiii1I11 ( name , url , 222 , iconimage , ooo0O0o00O , i11II1I11I1 )
     OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
  else :
   i1I1I1i1I1 ( url , iconimage , name )
   if 25 - 25: Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
 else :
  Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
  for url , iI , name in Ii1i1iI1iIIi :
   if 'http' in url :
    if '.php' in url :
     I111I11I111 ( name , url , 1016 , iI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      iiiiI11ii ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI )
     else :
      I1ii1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( Oo0OoO00oOO0o ) )
      for IIi1IIIi in I1ii1 :
       if IIi1IIIi == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      iiiiI11ii ( name , url , 222 , iI )
      OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
   else :
    i1I1I1i1I1 ( url , iI , name )
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 50 - 50: o0O0Oooo0O . iIII / o0o00Oo0O . iIII
def i1I1I1i1I1 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ooI111I11iiI = ( url ) . replace ( o0OO0 , 'http' ) . replace ( IIIiI , '.com' ) ;
 oOoOOooo0OOO = ( ooI111I11iiI ) . replace ( II111Iiii1 , 'a' ) . replace ( I11Ii1I1I , 'b' ) . replace ( oo00OO0o0 , 'c' ) . replace ( IiII1IiiI , 'd' ) . replace ( Ii1iiiIIIii , 'e' ) . replace ( oooOI1ii1I1i1 , 'f' ) ;
 Oo0ooOO = ( oOoOOooo0OOO ) . replace ( iiI1II11I1iI , 'g' ) . replace ( OOo0OoO00OO , 'h' ) . replace ( I11111IiI1I , 'i' ) . replace ( IIiiiI1ii1I , 'j' ) . replace ( o0oo0000Oo , 'k' ) . replace ( o00O00 , 'l' ) ;
 IIi11oo0 = ( Oo0ooOO ) . replace ( OoOoo00oO , 'm' ) . replace ( oo0O , 'n' ) . replace ( O0oo000O00oo , 'o' ) . replace ( ooOO , 'p' ) . replace ( i1IiI1i1iI1Ii , 'q' ) . replace ( O00O , 'r' ) ;
 iIIII1iiIII = ( IIi11oo0 ) . replace ( OO0oOii11iIIi1i , 's' ) . replace ( oOoo00OO0 , 't' ) . replace ( oOOooO00oOo00 , 'u' ) . replace ( iIII1II1iI , 'v' ) . replace ( oOOOOoO00o0oo , 'w' ) . replace ( i1i1iIiI , 'x' ) ;
 oO000ooO = ( iIIII1iiIII ) . replace ( OoOiIIiI , 'y' ) . replace ( IIi111i1i1III , 'z' ) . replace ( O000I1i1iI1II , '.' ) . replace ( OooO0ooOooO0o00oO , '(' ) . replace ( I1i1IIii , ')' ) . replace ( I1i1i1Ii1I , '/' ) ;
 O00oOo = ( oO000ooO ) . replace ( o000ooOo0o0Oo , '1' ) . replace ( Iii11i1111II , '2' ) . replace ( Ii1Ii1ii , '3' ) . replace ( ii1I1ii , '4' ) . replace ( iIiI , '5' ) . replace ( Oo0O0 , '6' ) ;
 oO0OOoooooo0o = ( O00oOo ) . replace ( i11iii , '7' ) . replace ( oO0OoOoo00 , '8' ) . replace ( IIiiIi1i , '9' ) . replace ( IiiiiI1iIi , '0' ) . replace ( i11i1I1 , ':' ) . replace ( o0OoO0 , '%' ) ;
 url = ( oO0OOoooooo0o ) . replace ( IiiIi1II , '-' ) . replace ( OoOOoo , '_' ) ;
 iiiiI11ii ( name , url , 222 , iconimage ) ;
 if 64 - 64: I11i
 if 84 - 84: IIiIiII11i
def OOO0o0 ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iI , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 1007 , iI )
def iIIoOooooO0o0OOO ( url ) :
 if 80 - 80: IIIi11I1 * o0O00o / IIIIiiII111 % Ii1i1i
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iI , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 1006 , iI )
  if 31 - 31: I1ii11iIi11i * Ii1i1i + Ii + o0O0Oooo0O + I1ii11iIi11i % oOo0O0Ooo
def ooOOO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iiIIIiIi1IIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iiIIIiIi1IIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIi1IIi )
 if 54 - 54: o0O00o + iIII / ii / iIII / ooOoO0O00
 if 94 - 94: oO0o - oO0o . OOooOOo
def IiI1iI1 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O0 )
 for url , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '-dir-' in iiIiii1IIIII :
   I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iII11 )
  else :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' , url , 1006 , iII11 )
   if 44 - 44: oOo0O0Ooo / o0O00o . IIIIiiII111
def IIoO0Oo0oo0OO ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 I11ii1 = ( 'http://afewbitsmore.com/' )
 Ii1i1iI1iIIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '[To Parent Directory]' in iiIiii1IIIII :
   iiIiii1IIIII = 'HOME'
   pass
  elif 'HOME' in iiIiii1IIIII :
   pass
  elif '.m3u' in iiIiii1IIIII :
   I111I11I111 ( '[COLOR' + II11iiii1Ii + ']PLAY ALL[/COLOR]' , I11ii1 + url , 2002 , iiiiiIIii + 'music.png' )
  elif '.mp3' in iiIiii1IIIII :
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , I11ii1 + url , 222 , iiiiiIIii + 'music.png' )
  elif '.m4a' in iiIiii1IIIII :
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , I11ii1 + url , 222 , iiiiiIIii + 'music.png' )
  else :
   I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) , I11ii1 + url , 1012 , iiiiiIIii + 'music.png' )
def iI1iI ( url ) :
 oO0000OOo00 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0000OOo00 )
 for iII11 , iiIiii1IIIII , url in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiiiiIIii + 'music.png' )
  if 29 - 29: Ii1i1i % IIIi11I1 - o0O0Oooo0O + iI11I1II1I1I + oOo0O0Ooo * ooOO0O0ooOooO
def OoOoOO0ooo0o0 ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 I11ii1 = url
 Ii1i1iI1iIIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '.mp3' in iiIiii1IIIII :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiiiiIIii + 'music.png' )
  else :
   I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '/' , '' ) , I11ii1 + url , 1011 , iiiiiIIii + 'music.png' )
def iiI1iIi1 ( ) :
 O0o0O0 = o00oiii11II1I ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iII11 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , ( 'http://www.cyn.net/music/' + Oo0o00OO0000 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iII11 ) . replace ( ' ' , '%20' ) )
def oO00 ( url , img ) :
 O0o0O0 = o00oiii11II1I ( url )
 Oo0Oo0O = url
 img = img
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( Oo0Oo0O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 19 - 19: iI11I1II1I1I % IIIi11I1 . IIiIiII11i - oO0o * ii
def oO0iII1i111iI ( url ) :
 O0o0O0 = o00oiii11II1I ( url )
 Oo0Oo0O = url
 Ii1i1iI1iIIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O0o0O0 )
 for type , url , iiIiii1IIIII in Ii1i1iI1iIIi :
  if '[VID]' in type :
   iiiiI11ii ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , Oo0Oo0O + url , 222 , iiiiiIIii + 'music.png' )
  if '[DIR]' in type :
   oO0iII1i111iI ( Oo0Oo0O + url )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: IIIIiiII111 - I1ii11iIi11i
 if 19 - 19: o0o00Oo0O . ooOoO0O00 + iIII / IIiIiII11i + oOOoOooOo
def oOoo ( ) :
 o0O00Oooo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IIIIIiII1 = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO00oo00 = IIIIIiII1 . lower ( )
 Oo0o00OO0000 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 oOO0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 26 - 26: Ii1i1i * ooOO0O0ooOooO % oOo0O0Ooo - IIIi11I1 . o0O0Oooo0O
 oO0000OOo00 = O0 ( Oo0o00OO0000 )
 ooOOo00 = O0 ( oOO0 )
 iiIi1IIiIi = O0 ( Oo0Oo0O )
 if 35 - 35: ooOoO0O00 % Ii + Ii1i1i
 if oO0000OOo00 != 'Failed' :
  Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0000OOo00 )
  for Oo0o00OO0000 , ii1IiIiI1 , i11II1I11I1 , oOO0o0oo0 , iiIiii1IIIII in Ii1i1iI1iIIi :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    OoOOoOooooOOo ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , Oo0o00OO0000 , 1016 , ii1IiIiI1 , ooo0O0o00O , i11II1I11I1 )
    if 14 - 14: oO0o * ii
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if ooOOo00 != 'Failed' :
  I1iiIIIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ooOOo00 )
  for Oo0o00OO0000 , iiIiii1IIIII in I1iiIIIi11 :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + Oo0o00OO0000 ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'Music.png' )
    if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . OOooOOo
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
 if iiIi1IIiIi != 'Failed' :
  I1Ii = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( iiIi1IIiIi )
  for Oo0o00OO0000 , iiIiii1IIIII in I1Ii :
   if IIIIIiII1 in iiIiii1IIIII . lower ( ) :
    I111I11I111 ( ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + Oo0o00OO0000 ) . replace ( ' ' , '%20' ) , 1006 , iiiiiIIii + 'Music.png' )
    if 97 - 97: iIII % IIiIiII11i % Ii1i1i . IIiIiII11i . iI11I1II1I1I
    OOoOO0o0o0 ( 'tvshows' , 'Media Info 3' )
    if 98 - 98: Ii + o0o00Oo0O - o0o00Oo0O - IIIIiiII111
    if 25 - 25: ooOO0O0ooOooO / o0o00Oo0O + o0O0Oooo0O % Ii / oOo0O0Ooo
    if 62 - 62: IIIIiiII111 . iIII * ooOoO0O00 + IIIIiiII111
    if 95 - 95: Ii1i1i / I11i % oOOoOooOo - oOo0O0Ooo / IIIi11I1 * IIIi11I1
    if 6 - 6: oO0o % o0O00o + iI11I1II1I1I
    if 18 - 18: IIiIiII11i . Ii1i1i + OOooOOo + o0o00Oo0O - iIII
OoOoo00oO = '{SF},' ; oo0O = '{IF},' ; O0oo000O00oo = '{PW},' ; Ii1Ii1ii = '{AM},' ; ooOO = '{GF},' ; i1IiI1i1iI1Ii = '{DD},' ; O00O = '{UO},' ; OO0oOii11iIIi1i = '{LE},' ; oOOooO00oOo00 = '{ZY},' ; iIII1II1iI = '{UE},' ; oOOOOoO00o0oo = '{PE},' ; i1i1iIiI = '{JE},' ; OoOiIIiI = '{TH},' ; IIi111i1i1III = '{LK},'
if 30 - 30: IIiIiII11i
if 26 - 26: iIII - ooOoO0O00 - I1ii11iIi11i * o0o00Oo0O * IIIi11I1 . ii
def I1iii ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://www.iwatchseries.me/tv-list/' )
 Ii1i1iI1iIIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 8021 , iiiiiIIii + 'iwatch.png' )
  OOoOO0o0o0 ( 'movies' , 'MAIN' )
def oOoI1I ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII , oOO0ooIiIIi1I1I11Ii in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII + oOO0ooIiIIi1I1I11Ii , url , 8022 , iiiiiIIii + 'iwatch.png' )
def I11iiiI1iiIiI ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IIii ( url )
def IIii ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( O0o0O0 )
 I1Ii = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( O0o0O0 )
 II1iIi1IiIii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( O0o0O0 )
 iI111i11iI1 = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( 'VidSpot - ' + iiIiii1IIIII , url , 222 , iiiiiIIii + 'iwatch.png' )
 for url in I1Ii :
  iiiiI11ii ( 'VodLocker' , url , 222 , iiiiiIIii + 'iwatch.png' )
 for url , iiIiii1IIIII in iI111i11iI1 :
  iiiiI11ii ( 'VidUp' + iiIiii1IIIII , url , 222 , iiiiiIIii + 'iwatch.png' )
 for iiIiii1IIIII , url in II1iIi1IiIii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   iiiiI11ii ( 'TheVideo - ' + iiIiii1IIIII , url , 222 , iiiiiIIii + 'iwatch.png' )
   if 22 - 22: iI11I1II1I1I % iI11I1II1I1I . I11i
def iIII1Iiii ( ) :
 O0o0O0 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 Ii1i1iI1iIIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 1021 , iiiiiIIii + 'anime.png' )
  if 2 - 2: Ii1i1i . IIIIiiII111 + OOooOOo / o0O00o - oOo0O0Ooo % oOo0O0Ooo
  if 6 - 6: OOooOOo - ooOoO0O00 + IIiIiII11i % ooOO0O0ooOooO
def o00oo0 ( ) :
 O0o0O0 = i11oO0oOo0 ( 'http://www.animetoon.org/cartoon' )
 Ii1i1iI1iIIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( O0o0O0 )
 for Oo0o00OO0000 , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , Oo0o00OO0000 , 1002 , iiiiiIIii + 'anime.png' )
  if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / Ii1i1i
  if 11 - 11: iI11I1II1I1I + oOo0O0Ooo
  if 15 - 15: I11i
def ooOoOO0Oo0oO0o ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 I1Ii = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O0o0O0 )
 for iII11 in I1Ii :
  OooO0O = iII11
 II1iIi1IiIii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( O0o0O0 )
 for url in II1iIi1IiIii :
  I111I11I111 ( 'NEXT PAGE' , url , 1002 , iiiiiIIii + 'Next.png' )
 Ii1i1iI1iIIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O0 )
 for url , iiIiii1IIIII in Ii1i1iI1iIIi :
  I111I11I111 ( iiIiii1IIIII , url , 1003 , OooO0O )
 xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOo0oOoooo0 ( url , IMAGE ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( O0o0O0 )
 for iiIiii1IIIII , url in Ii1i1iI1iIIi :
  print iiIiii1IIIII + '     ' + url
  if 'easy' in url :
   OOOoO0000ooO ( url )
  elif 'playpanda' in url :
   OOOoO0000ooO ( url )
   if 53 - 53: iI11I1II1I1I
  xbmcplugin . addSortMethod ( O00oO , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOoO0000ooO ( url ) :
 O0o0O0 = i11oO0oOo0 ( url )
 Ii1i1iI1iIIi = re . compile ( "url: '(.+?)'," ) . findall ( O0o0O0 )
 for url in Ii1i1iI1iIIi :
  iiiiI11ii ( 'STREAM' , url , 222 , iiiiiIIii + 'anime.png' )
  if 79 - 79: Ii1i1i - IIiIiII11i / ooOO0O0ooOooO + I1ii11iIi11i . oOo0O0Ooo
  if 83 - 83: OOooOOo + oO0o / iI11I1II1I1I % Ii1i1i
def oOOi11Iii ( url ) :
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 ii1ii1ii . add_header ( 'referer' , url )
 oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
 I1I1IiI1 = oooooOoo0ooo . read ( )
 oooooOoo0ooo . close ( )
 return I1I1IiI1
 if 37 - 37: I11i . o0O00o
def o00oiii11II1I ( url ) :
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
 I1I1IiI1 = oooooOoo0ooo . read ( )
 oooooOoo0ooo . close ( )
 return I1I1IiI1
 if 48 - 48: ii * iI11I1II1I1I
def OoOooOOOooo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iIiii1Ii = ( '%s%s' % ( II1I11i , url ) )
 I1I1IiI1 = o00oiii11II1I ( url )
 Ii1i1iI1iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1I1IiI1 )
 for url , iI , iiIiii1IIIII in Ii1i1iI1iIIi :
  iiiiI11ii ( '%s' % ( '[COLOR' + II11iiii1Ii + ']' + iiIiii1IIIII + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iI )
  if 68 - 68: OOooOOo
def O0OoI1i1iiiiIII11 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  IiiIIIIIi11 ( url , iiIiii1IIIII )
 else :
  O0i1iI ( url )
def O0i1iI ( url ) :
 import urlresolver
 try :
  iiIIi = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( iiIIi , xbmcgui . ListItem ( iiIiii1IIIII ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iiIiii1IIIII ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def II11IiI1 ( url ) :
 if 58 - 58: Ii1i1i * iIII
 I1IiIiI = open ( Oo0oOOo , "a" )
 I1IiIiI . write ( 'url="' + url + '"\n' )
 I1IiIiI . close
 if 95 - 95: ooOO0O0ooOooO
 o0oO = xbmc . Player ( i11i11 ( ) )
 import urlresolver
 try : o0oO . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iiIiii1IIIII ) )
 o0oO = xbmc . Player ( i11i11 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  O0OoO000O0OO = xbmcgui . Dialog ( )
  if O0OoO000O0OO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   O0OoO000O0OO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : o0oO . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def IiiIIIIIi11 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  OoO0 = '.mp4'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.mkv' in url :
  OoO0 = '.mkv'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.mp3' in url :
  OoO0 = '.mp3'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.avi' in url :
  OoO0 = '.avi'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.mov' in url :
  OoO0 = '.mov'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.mpeg' in url :
  OoO0 = '.mpeg'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.mpg' in url :
  OoO0 = '.mpg'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.flv' in url :
  OoO0 = '.flv'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 elif '.wmv' in url :
  OoO0 = '.wmv'
  I11ii1IIiIi = [ '[COLOR' + II11iiii1Ii + ']PLAY[/COLOR]' , '[COLOR' + II11iiii1Ii + ']DOWNLOAD[/COLOR]' ]
  OoOOo0OOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + II11iiii1Ii + ']Play/Download[/COLOR]' , I11ii1IIiIi )
  if OoOOo0OOoO == 0 :
   O0i1iI ( url )
  if OoOOo0OOoO == 1 :
   iii1i ( url , name , OoO0 )
 else :
  O0i1iI ( url )
def iii1i ( url , name , cat ) :
 OoOooOOo ( )
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
def OoOooOOo ( ) :
 I1iI = xbmc . translatePath ( os . path . join ( OO0o ) )
 if not os . path . exists ( OO0o ) :
  O0OoO000O0OO . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def o0Oo0OOO0 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iiIiii1IIIII )
 xbmc . sleep ( 1 )
 o0oO = xbmc . Player ( i11i11 ( ) )
 o0oOoO00o . update ( 100 , '%s' % iiIiii1IIIII )
 xbmc . sleep ( 1 )
 o0oO . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 73 - 73: OOooOOo % ooOO0O0ooOooO / o0o00Oo0O - ii
def ooOoOOoooO000 ( url ) :
 o0oO = xbmc . Player ( i11i11 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : o0oO . play ( url ) . strip ( )
 except : pass
 if 87 - 87: iI11I1II1I1I
def I1I1IIi11II ( url ) :
 o0oO = xbmc . Player ( i11i11 ( ) )
 import urlresolver
 O0Oo0ooO0OO00 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 o0oO . play ( O0Oo0ooO0OO00 )
 xbmc . sleep ( 1 )
 o0oO . play ( url )
 if 76 - 76: Ii1I
 if 61 - 61: I11i * o0o00Oo0O
def i11i11 ( ) :
 try :
  o0O0oO00oo0O = getSet ( "core-player" )
  if ( o0O0oO00oo0O == 'DVDPLAYER' ) : i1iI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0O0oO00oo0O == 'MPLAYER' ) : i1iI = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0O0oO00oo0O == 'PAPLAYER' ) : i1iI = xbmc . PLAYER_CORE_PAPLAYER
  else : i1iI = xbmc . PLAYER_CORE_AUTO
 except : i1iI = xbmc . PLAYER_CORE_AUTO
 return i1iI
 return True
 if 81 - 81: iI11I1II1I1I + o0o00Oo0O * I11i - Ii / IIIIiiII111
def I111I11I111 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0oo0O0 = [ ]
  O0oo0O0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0oo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   O0oo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1I1 . addContextMenuItems ( O0oo0O0 )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = True )
 return iioO0o
 if 32 - 32: OOooOOo . I1ii11iIi11i . I11i / oOo0O0Ooo
def iiiI1ii ( name , url , mode , iconimage , fanart , description ) :
 if 23 - 23: IIIIiiII111 * Ii1I / Ii1i1i - OOooOOo . IIiIiII11i
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = True )
 return iioO0o
 if 74 - 74: o0O0Oooo0O . o0O00o % IIIIiiII111 . o0o00Oo0O
def iiiiI11ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0oo0O0 = [ ]
  O0oo0O0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0oo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   O0oo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1I1 . addContextMenuItems ( O0oo0O0 )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = False )
 return iioO0o
 if 61 - 61: o0O00o / iIII . o0O0Oooo0O * OOooOOo / oO0o
 if 18 - 18: oOOoOooOo % oO0o % IIIi11I1 . Ii1I + IIiIiII11i / IIIIiiII111
 if 73 - 73: o0o00Oo0O / Ii1i1i + Ii - Ii1i1i
 if 48 - 48: oOo0O0Ooo - Ii * Ii1I
 if 70 - 70: Ii1I * OOooOOo
 if 63 - 63: oOOoOooOo . o0O00o - OOooOOo % o0O00o - o0O0Oooo0O / o0O0Oooo0O
def IioOOoOooo0oOO0 ( url , heading , announce ) :
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
   try : OOo0O0oo0OO0O = open ( announce ) ; I1111i1 = OOo0O0oo0OO0O . read ( )
   except : I1111i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1111i1 ) )
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
   try : OOo0O0oo0OO0O = open ( announce ) ; I1111i1 = OOo0O0oo0OO0O . read ( )
   except : I1111i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1111i1 ) )
   return
 I1iI1ii1II ( )
 I1iI1ii1II ( )
def I1i ( ) :
 IioOOoOooo0oOO0 ( iiiiiIIii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 95 - 95: ooOO0O0ooOooO
 if 88 - 88: IIIIiiII111 / o0O0Oooo0O + ooOoO0O00 / o0O0Oooo0O / I11i . ooOO0O0ooOooO
 if 32 - 32: oOOoOooOo / o0O00o
 if 28 - 28: ii % IIIIiiII111 / Ii % oO0o - I1ii11iIi11i
 if 90 - 90: IIIi11I1
def OoOOoooOO0O ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 O0OoO000O0OO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 52 - 52: oO0o * ooOO0O0ooOooO / iI11I1II1I1I - OOooOOo
 if 20 - 20: o0O00o % oOo0O0Ooo + iI11I1II1I1I % IIIIiiII111
 if 100 - 100: I11i - I1ii11iIi11i % o0O0Oooo0O . Ii % ii
 if 39 - 39: Ii1I / Ii * ooOoO0O00 * I1ii11iIi11i
 if 39 - 39: oO0o * ii / ooOoO0O00 + I1ii11iIi11i
 if 57 - 57: o0o00Oo0O
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
def I1oO0O00oOo00o ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + I1oOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 6 - 6: I11i * oOOoOooOo * ii + IIIIiiII111 + Ii1i1i - ooOO0O0ooOooO
def oO0OOoOoO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + IioOo0Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 86 - 86: o0O00o
def o0oooo00 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + iIiIIOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 23 - 23: OOooOOo + o0O0Oooo0O * oO0o
def iiIII11 ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + IiiI11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 82 - 82: Ii1i1i + I1ii11iIi11i
def iiIIOOo0o0o ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + ii1i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 31 - 31: o0o00Oo0O / OOooOOo / ooOoO0O00
def o0Oo000OO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + ooo00o000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 14 - 14: ooOO0O0ooOooO * IIIi11I1 * Ii
def o0o0O0OOo0OO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + Ooo0O0O0Oo0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 10 - 10: I11i - IIiIiII11i % Ii1I + I1ii11iIi11i
def O00oOoIiIi111ii ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + o0o00OO0ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 54 - 54: oOo0O0Ooo / ooOoO0O00 * Ii1I
def iIiiiiiIii ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + O00ii111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 42 , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 32 - 32: oOo0O0Ooo + oOOoOooOo / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
def OOO ( url ) :
 I1I1IiI1 = i11oO0oOo0 ( str ( iI1iIIiiii ) + o0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i1iI1iIIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1I1IiI1 )
 for iiIiii1IIIII , url , ii1IiIiI1 , ooo0O0o00O , IiI1IIIII1I in Ii1i1iI1iIIi :
  OoOOoOooooOOo ( iiIiii1IIIII , url , 5 , iiiiiIIii + 'GenieTVRSSFeed.png' , iiiiiIIii + 'GenieTVRSSFeed.png' , IiI1IIIII1I )
 OOoOO0o0o0 ( 'movies' , 'MAIN' )
 if 78 - 78: iI11I1II1I1I / oOo0O0Ooo - o0O00o
 if 81 - 81: Ii1I
 if 31 - 31: o0o00Oo0O % oOOoOooOo / oOo0O0Ooo * IIIIiiII111 % iI11I1II1I1I * OOooOOo
 if 76 - 76: o0O0Oooo0O - o0o00Oo0O
 if 23 - 23: o0o00Oo0O * Ii1i1i * oOOoOooOo % oOOoOooOo
 if 7 - 7: IIiIiII11i + iIII
 if 99 - 99: iI11I1II1I1I * ooOO0O0ooOooO
 if 37 - 37: oOOoOooOo * IIIIiiII111 * iIII
 if 11 - 11: oOo0O0Ooo
def ii1iII11 ( ) :
 try :
  if os . path . exists ( IIiiiiiiIi1I1 ) == True :
   O0OoO000O0OO = xbmcgui . Dialog ( )
   if O0OoO000O0OO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( IIiiiiiiIi1I1 ) :
     iii11OOo0oO = 0
     iii11OOo0oO += len ( II1OOO )
     if iii11OOo0oO > 0 :
      for OOo0O0oo0OO0O in II1OOO :
       os . unlink ( os . path . join ( iIi1Iii1 , OOo0O0oo0OO0O ) )
  oo0o00oOo0 = os . path . join ( IIIII , "Textures13.db" )
  os . unlink ( oo0o00oOo0 )
  O0OoO000O0OO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 86 - 86: o0o00Oo0O + o0o00Oo0O / iIII - iI11I1II1I1I
 if 42 - 42: IIIi11I1
 if 39 - 39: o0o00Oo0O % Ii1i1i . iIII * I11i
 if 14 - 14: iIII . iI11I1II1I1I + o0O0Oooo0O % ii
 if 9 - 9: ooOO0O0ooOooO + Ii1i1i / Ii1I * iI11I1II1I1I + I11i
 if 64 - 64: iIII % Ii % Ii1I
 if 14 - 14: o0O0Oooo0O - OOooOOo - Ii1I % iIII + ii
 if 4 - 4: o0O0Oooo0O - oOo0O0Ooo / iI11I1II1I1I + Ii1I % iI11I1II1I1I * oOo0O0Ooo
def o0Oooo ( title , message , times = 2000 , icon = o0 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 30 - 30: Ii % IIIi11I1
def O0oOOoOoo ( url ) :
 i1I111II11 = os . path . join ( oooOOOOO , 'addon_data' )
 I11ii111i = [
 ( i1I111II11 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( i1I111II11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( i1I111II11 , 'plugin.video.itv' , 'Images' ) ) ]
 if 80 - 80: oO0o / oOo0O0Ooo + OOooOOo + IIIi11I1 % ooOO0O0ooOooO
 I1OoO0ooOOO = 0
 if 81 - 81: I11i - o0O0Oooo0O
 for IIi1IIIi in I11ii111i :
  if os . path . exists ( IIi1IIIi ) and not IIi1IIIi in [ oo0o0O00 , i1I111II11 ] :
   for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( IIi1IIIi ) :
    iii11OOo0oO = 0
    iii11OOo0oO += len ( II1OOO )
    if iii11OOo0oO > 0 :
     for OOo0O0oo0OO0O in II1OOO :
      if not OOo0O0oo0OO0O in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( iIi1Iii1 , OOo0O0oo0OO0O ) )
       except :
        pass
      else : Oo0o0O00 ( 'Ignore Log File: %s' % OOo0O0oo0OO0O )
     for ooIii in oOOoo0 :
      try :
       shutil . rmtree ( os . path . join ( iIi1Iii1 , ooIii ) )
       I1OoO0ooOOO += 1
       Oo0o0O00 ( "[Success] cleared %s files from %s" % ( str ( iii11OOo0oO ) , os . path . join ( IIi1IIIi , ooIii ) ) )
      except :
       Oo0o0O00 ( "[Failed] to wipe cache in: %s" % os . path . join ( IIi1IIIi , ooIii ) )
  else :
   for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( IIi1IIIi ) :
    for ooIii in oOOoo0 :
     if 'cache' in ooIii . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iIi1Iii1 , ooIii ) )
       I1OoO0ooOOO += 1
       Oo0o0O00 ( "[Success] wiped %s " % os . path . join ( IIi1IIIi , ooIii ) )
      except :
       Oo0o0O00 ( "[Failed] to wipe cache in: %s" % os . path . join ( IIi1IIIi , ooIii ) )
       if 45 - 45: IIIi11I1 + ooOO0O0ooOooO * o0o00Oo0O % oOOoOooOo + iI11I1II1I1I + o0O0Oooo0O
 o0Oooo ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % I1OoO0ooOOO )
 if 85 - 85: o0o00Oo0O
 if 10 - 10: I1ii11iIi11i / OOooOOo * IIIi11I1 - o0O00o + Ii1i1i
 if 62 - 62: oOo0O0Ooo . Ii1i1i
 if 74 - 74: Ii1i1i - iIII % oOOoOooOo - oOo0O0Ooo - Ii1i1i - IIiIiII11i
 if 81 - 81: ooOoO0O00 * Ii1I + o0O00o - oO0o * ooOoO0O00
 if 6 - 6: iI11I1II1I1I % OOooOOo % IIiIiII11i % I11i
 if 52 - 52: Ii1i1i - oOo0O0Ooo * iI11I1II1I1I % I1ii11iIi11i * IIIi11I1
def Oo0000ooooOO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 I1I1IOoOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( I1I1IOoOOoo ) :
   iii11OOo0oO = 0
   iii11OOo0oO += len ( II1OOO )
   if 33 - 33: o0o00Oo0O + ooOoO0O00 + oOo0O0Ooo * oOo0O0Ooo
   if 79 - 79: o0O0Oooo0O - iIII
   if iii11OOo0oO > 0 :
    if 49 - 49: IIiIiII11i + o0o00Oo0O * oOOoOooOo - I1ii11iIi11i
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( iii11OOo0oO ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: oOo0O0Ooo + iIII . ooOO0O0ooOooO . IIiIiII11i + ooOO0O0ooOooO / I1ii11iIi11i
     for OOo0O0oo0OO0O in II1OOO :
      os . unlink ( os . path . join ( iIi1Iii1 , OOo0O0oo0OO0O ) )
     for ooIii in oOOoo0 :
      shutil . rmtree ( os . path . join ( iIi1Iii1 , ooIii ) )
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
 ooOo ( )
 return
 if 32 - 32: oO0o % ooOO0O0ooOooO * Ii1I + iIII / o0O0Oooo0O
 if 5 - 5: I11i + IIIIiiII111 / ii + Ii1i1i . OOooOOo / ooOO0O0ooOooO
 if 18 - 18: IIiIiII11i . I11i
 if 75 - 75: ii - I1ii11iIi11i
 if 56 - 56: IIiIiII11i - Ii - ooOO0O0ooOooO . I11i
 if 4 - 4: ooOoO0O00
 if 91 - 91: o0O00o . oO0o * Ii1i1i / I11i
 if 41 - 41: oOo0O0Ooo . oO0o / ooOoO0O00 . I1ii11iIi11i . ooOO0O0ooOooO
 if 44 - 44: IIIIiiII111 * iIII + Ii + ooOoO0O00 / o0O00o * IIiIiII11i
def iI1i11 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 I1I1IOoOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( I1I1IOoOOoo ) :
   iii11OOo0oO = 0
   iii11OOo0oO += len ( II1OOO )
   if 58 - 58: IIIi11I1
   if 72 - 72: oO0o + IIIi11I1 - I1ii11iIi11i % oOOoOooOo . o0O00o
   if iii11OOo0oO > 0 :
    if 95 - 95: IIIIiiII111 % IIIi11I1 - o0O00o - OOooOOo % I11i * o0o00Oo0O
    O0OoO000O0OO = xbmcgui . Dialog ( )
    if O0OoO000O0OO . yesno ( "Delete Package Cache Files" , str ( iii11OOo0oO ) + " files found" , "Do you want to delete them?" ) :
     if 16 - 16: o0O0Oooo0O / I1ii11iIi11i
     for OOo0O0oo0OO0O in II1OOO :
      os . unlink ( os . path . join ( iIi1Iii1 , OOo0O0oo0OO0O ) )
     for ooIii in oOOoo0 :
      shutil . rmtree ( os . path . join ( iIi1Iii1 , ooIii ) )
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
 O0oOOoOoo ( url )
 return
 if 48 - 48: I1ii11iIi11i / ooOO0O0ooOooO + IIIIiiII111 % IIIIiiII111
 if 9 - 9: Ii1I - I11i . I1ii11iIi11i + Ii1I . IIIi11I1
 if 30 - 30: ii - iI11I1II1I1I / ooOO0O0ooOooO * Ii1i1i / Ii1i1i
 if 52 - 52: OOooOOo - oO0o + oOo0O0Ooo + o0O00o
 if 49 - 49: ooOO0O0ooOooO / iIII - ooOO0O0ooOooO
 if 31 - 31: OOooOOo + oOo0O0Ooo + Ii1I + iIII * IIiIiII11i % ooOO0O0ooOooO
 if 90 - 90: IIIi11I1 * iI11I1II1I1I / ooOoO0O00
 if 60 - 60: IIIi11I1 * o0O0Oooo0O . ooOO0O0ooOooO
 if 47 - 47: ooOO0O0ooOooO % IIIi11I1 / IIIi11I1 % OOooOOo % o0O0Oooo0O / OOooOOo
 if 51 - 51: oOo0O0Ooo . iIII - OOooOOo
def IIiIi1I1Ii11 ( url , name ) :
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OO0OOOO = os . path . join ( I1iI , 'advancedsettings.xml' )
 O0OoO000O0OO = xbmcgui . Dialog ( )
 I1Iiiii1 = os . path . join ( I1iI , 'advancedsettings.xml.bak' )
 if os . path . exists ( I1Iiiii1 ) == False :
  if O0OoO000O0OO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OO0OOOO = os . path . join ( I1iI , 'advancedsettings.xml' )
   try :
    os . remove ( OO0OOOO )
    print '=== GenieTv - REMOVING    ' + str ( OO0OOOO ) + '    ==='
   except :
    pass
   I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
   oOoO00o = open ( OO0OOOO , "w" )
   oOoO00o . write ( I1I1IiI1 )
   oOoO00o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OO0OOOO ) + '    ==='
   O0OoO000O0OO = xbmcgui . Dialog ( )
   O0OoO000O0OO . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OO0OOOO = os . path . join ( I1iI , 'advancedsettings.xml' )
  try :
   os . remove ( OO0OOOO )
   print '=== GenieTv - REMOVING    ' + str ( OO0OOOO ) + '    ==='
  except :
   pass
  I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
  oOoO00o = open ( OO0OOOO , "w" )
  oOoO00o . write ( I1I1IiI1 )
  oOoO00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OO0OOOO ) + '    ==='
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 79 - 79: oOo0O0Ooo + IIiIiII11i + oOOoOooOo % oO0o
def o0O00ooO0O0Oo ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OO0OOOO = os . path . join ( I1iI , 'advancedsettings.xml' )
 try :
  oOoO00o = open ( OO0OOOO ) . read ( )
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
 if 94 - 94: Ii % ii + IIIIiiII111
def i1Iii1 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OO0OOOO = os . path . join ( I1iI , 'advancedsettings.xml' )
 try :
  os . remove ( OO0OOOO )
  O0OoO000O0OO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OO0OOOO ) + '    ==='
  O0OoO000O0OO . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 95 - 95: IIiIiII11i % I11i . iIII
 if 18 - 18: o0o00Oo0O / ii * I1ii11iIi11i % IIIIiiII111
 if 24 - 24: Ii1I % IIIi11I1 + ii + oO0o
 if 100 - 100: I1ii11iIi11i % oO0o - OOooOOo
 if 46 - 46: I11i
 if 28 - 28: ooOoO0O00
 if 81 - 81: ooOO0O0ooOooO % ii . o0O0Oooo0O - OOooOOo / oOo0O0Ooo
 if 62 - 62: o0O0Oooo0O * iIII / iIII
 if 42 - 42: oOOoOooOo * oOOoOooOo / Ii1i1i / IIIi11I1 * IIIi11I1
 if 92 - 92: I1ii11iIi11i / IIIIiiII111 - ii - I11i % oOOoOooOo
def Ii11111iI1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Ii1i1iI1iIIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( oOOoO0 . http_GET ( url ) . content )
 for iiI111iIi1 , I11OoO , i1I1I1 , ii11IiIII in Ii1i1iI1iIIi :
  if inc < 2 : O0OoO000O0OO = xbmcgui . Dialog ( ) ; O0OoO000O0OO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iiI111iIi1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % i1I1I1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % ii11IiIII )
  inc = inc + 1
  if 22 - 22: IIiIiII11i % iI11I1II1I1I * o0o00Oo0O
  if 78 - 78: o0O0Oooo0O * ooOoO0O00 + ii * oOOoOooOo
  if 69 - 69: ooOoO0O00
  if 83 - 83: Ii1I . oOOoOooOo + oOo0O0Ooo + o0o00Oo0O
  if 78 - 78: o0o00Oo0O + I1ii11iIi11i
  if 14 - 14: o0o00Oo0O
  if 67 - 67: IIiIiII11i / o0o00Oo0O
  if 10 - 10: ooOoO0O00 / I1ii11iIi11i
  if 20 - 20: I1ii11iIi11i * o0O0Oooo0O / Ii1I . oOOoOooOo
def oO0III1iI ( url , name ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 if O0OoO000O0OO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  I1iI = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OO0OOOO = os . path . join ( I1iI , 'addons2.ini' )
  I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
  oOoO00o = open ( OO0OOOO , "w" )
  oOoO00o . write ( I1I1IiI1 )
  oOoO00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OO0OOOO ) + '    ==='
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 96 - 96: I11i . I1ii11iIi11i * Ii
def Iii1i1I1iIi ( url , name ) :
 O0OoO000O0OO = xbmcgui . Dialog ( )
 if O0OoO000O0OO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  I1iI = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OO0OOOO = os . path . join ( I1iI , 'settings.xml' )
  I1I1IiI1 = oOOoO0 . http_GET ( url ) . content
  oOoO00o = open ( OO0OOOO , "w" )
  oOoO00o . write ( I1I1IiI1 )
  oOoO00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OO0OOOO ) + '    ==='
  O0OoO000O0OO = xbmcgui . Dialog ( )
  O0OoO000O0OO . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 59 - 59: Ii
 if 72 - 72: IIIi11I1 / o0O0Oooo0O + Ii1I % iIII * Ii1i1i
def o00Ooo0OoOOOO ( ) :
 try :
  iiiOo00Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iiiOo00Oo ) == True :
   O0OoO000O0OO = xbmcgui . Dialog ( )
   if O0OoO000O0OO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    i1IIIii11i = os . path . join ( iiiOo00Oo , "source.db" )
    os . unlink ( i1IIIii11i )
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
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; O0ooOoI11I1I1 = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O0ooOoI11I1I1 :
  oOOO00Oo = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oOOO00Oo = xbmc . translatePath ( oOOO00Oo ) ;
  iIiIi1III1iII = os . path . join ( oOOO00Oo , ".." , ".." ) ; iIiIi1III1iII = os . path . abspath ( iIiIi1III1iII ) ; pluginlog ( "freshstart.main_list xbmcPath=" + iIiIi1III1iII ) ; i11IIi1III1II = False
  try :
   for iIi1Iii1 , oOOoo0 , II1OOO in os . walk ( iIiIi1III1iII , topdown = True ) :
    oOOoo0 [ : ] = [ ooIii for ooIii in oOOoo0 if ooIii not in o0oO0 ]
    for iiIiii1IIIII in II1OOO :
     try : os . remove ( os . path . join ( iIi1Iii1 , iiIiii1IIIII ) )
     except :
      if iiIiii1IIIII not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : i11IIi1III1II = True
      pluginlog ( "Error removing " + iIi1Iii1 + " " + iiIiii1IIIII )
    for iiIiii1IIIII in oOOoo0 :
     try : os . rmdir ( os . path . join ( iIi1Iii1 , iiIiii1IIIII ) )
     except :
      if iiIiii1IIIII not in [ "Database" , "userdata" ] : i11IIi1III1II = True
      pluginlog ( "Error removing " + iIi1Iii1 + " " + iiIiii1IIIII )
   if not i11IIi1III1II : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 ooo0oOoO00Oo ( )
 if 60 - 60: iIII * ooOoO0O00 + oO0o . Ii - oO0o % oO0o
 if 46 - 46: Ii1i1i + Ii1I / iI11I1II1I1I % ooOoO0O00
 if 47 - 47: Ii1i1i % oO0o
def o00oOOo0O0Ooo ( ) :
 IiiI1iI1111 = [ ]
 ooo0OOoOOO0Oo = sys . argv [ 2 ]
 if len ( ooo0OOoOOO0Oo ) >= 2 :
  ii1IIi111 = sys . argv [ 2 ]
  oo00oO0OO0 = ii1IIi111 . replace ( '?' , '' )
  if ( ii1IIi111 [ len ( ii1IIi111 ) - 1 ] == '/' ) :
   ii1IIi111 = ii1IIi111 [ 0 : len ( ii1IIi111 ) - 2 ]
  iI1IiiIii1i1I = oo00oO0OO0 . split ( '&' )
  IiiI1iI1111 = { }
  for OooOoOo in range ( len ( iI1IiiIii1i1I ) ) :
   O0O00O = { }
   O0O00O = iI1IiiIii1i1I [ OooOoOo ] . split ( '=' )
   if ( len ( O0O00O ) ) == 2 :
    IiiI1iI1111 [ O0O00O [ 0 ] ] = O0O00O [ 1 ]
    if 64 - 64: IIIi11I1 + iIII . oOOoOooOo
 return IiiI1iI1111
 if 17 - 17: OOooOOo . o0O0Oooo0O
II1111IIIII1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
i1II1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
Ooooo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oo00O0o0OOO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
IIIi11Ii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
i1IIii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
I1oOooo = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
ooo00Oo0Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
IioOo0Ooo0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
iIiIIOO0o = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
IiiI11I = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
ii1i1II = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
ooo00o000 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
Ooo0O0O0Oo0OO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o0o00OO0ooo0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
O00ii111I = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
O0000ooO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
oOo0o = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OO0Ooo0O00ooOo0o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
Ooo000 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OO000oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
o0O00 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
II1I11i = base64 . decodestring ( 'Q1VOVA==' )
def o0o00O ( display , mode = None , name = None , url = None , menu = None , description = i1iiIIiiI111 , overwrite = True , fanart = iIi1ii1I1 , icon = o0 , themeit = None ) :
 I1 = sys . argv [ 0 ]
 if not mode == None : I1 += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : I1 += "&name=" + urllib . quote_plus ( name )
 if not url == None : I1 += "&url=" + urllib . quote_plus ( url )
 iioO0o = True
 if themeit : display = themeit % display
 I1I1 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : I1I1 . addContextMenuItems ( menu , replaceItems = overwrite )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = False )
 return iioO0o
def I1ii1i ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 I1I1 . setProperty ( 'fanart_image' , fanart )
 I1I1 . setProperty ( "IsPlayable" , "true" )
 Ii1i1iI = [ ]
 Ii1i1iI . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 Ii1i1iI . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 I1I1 . addContextMenuItems ( Ii1i1iI , replaceItems = True )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = False )
 return iioO0o
def OoOOoOooooOOo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0oo0O0 = [ ]
  if showcontext == 'fav' :
   O0oo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   O0oo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1I1 . addContextMenuItems ( O0oo0O0 )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = True )
 return iioO0o
 if 77 - 77: o0O0Oooo0O - ii
def oOOOoo0O0oO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iioO0o = True
 I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0oo0O0 = [ ]
  if showcontext == 'fav' :
   O0oo0O0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiI111I1iIiI :
   O0oo0O0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1I1 . addContextMenuItems ( O0oo0O0 )
 iioO0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = I1I1 , isFolder = False )
 return iioO0o
 if 2 - 2: OOooOOo - IIIi11I1 * I11i / oO0o - o0O00o % oOo0O0Ooo
 if 98 - 98: iI11I1II1I1I
ii1IIi111 = o00oOOo0O0Ooo ( )
Oo0o00OO0000 = None
iiIiii1IIIII = None
o0OO = None
ii1IiIiI1 = None
ooo0O0o00O = None
IiI1IIIII1I = None
o00oo0OO0 = None
iI1IIiiiI = None
if 61 - 61: iI11I1II1I1I + I1ii11iIi11i - Ii - ii * I1ii11iIi11i % ooOoO0O00
if 71 - 71: Ii + ooOO0O0ooOooO / OOooOOo / ii + oOo0O0Ooo * oOOoOooOo
try :
 iI1IIiiiI = int ( ii1IIi111 [ "fav_mode" ] )
except :
 pass
 if 64 - 64: iI11I1II1I1I / ooOoO0O00 + ooOO0O0ooOooO
try :
 Oo0o00OO0000 = urllib . unquote_plus ( ii1IIi111 [ "url" ] )
except :
 pass
try :
 iiIiii1IIIII = urllib . unquote_plus ( ii1IIi111 [ "name" ] )
except :
 pass
try :
 ii1IiIiI1 = urllib . unquote_plus ( ii1IIi111 [ "iconimage" ] )
except :
 pass
try :
 o0OO = int ( ii1IIi111 [ "mode" ] )
except :
 pass
try :
 ooo0O0o00O = urllib . unquote_plus ( ii1IIi111 [ "fanart" ] )
except :
 pass
try :
 IiI1IIIII1I = urllib . unquote_plus ( ii1IIi111 [ "description" ] )
except :
 pass
 if 45 - 45: Ii . Ii1i1i
 if 34 - 34: o0O00o / oOOoOooOo * IIiIiII11i * IIIIiiII111 % ii - iI11I1II1I1I
print str ( I1IIIii ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( o0OO )
print "URL: " + str ( Oo0o00OO0000 )
print "Name: " + str ( iiIiii1IIIII )
print "IconImage: " + str ( ii1IiIiI1 )
if 61 - 61: IIIi11I1 - IIIi11I1 / oOOoOooOo * o0O0Oooo0O
if 73 - 73: oO0o * Ii1i1i
def OOoOO0o0o0 ( content , viewType ) :
 if 49 - 49: ii / ooOO0O0ooOooO / oOo0O0Ooo + I11i * oOOoOooOo . I1ii11iIi11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 48 - 48: iIII + o0O00o / o0O00o
if ii1IiIiI1 == None : ii1IiIiI1 = o0
if ooo0O0o00O == None : ooo0O0o00O = iIi1ii1I1
if o0OO == None :
 O0oO ( )
 if 65 - 65: Ii1I - ooOoO0O00 % ooOO0O0ooOooO * iI11I1II1I1I - o0O00o + oOOoOooOo
elif o0OO == 1 :
 i1Ii1I ( Oo0o00OO0000 )
 if 63 - 63: Ii - IIIi11I1 . OOooOOo + o0O00o . oO0o
elif o0OO == 44 :
 iI1 ( Oo0o00OO0000 )
 if 70 - 70: iI11I1II1I1I % ii / oO0o . o0o00Oo0O - iIII % IIiIiII11i
elif o0OO == 2 :
 I1I11iII11 ( )
 if 84 - 84: IIIi11I1 * ooOoO0O00 . iI11I1II1I1I * IIIIiiII111 + o0O0Oooo0O + IIiIiII11i
elif o0OO == 3 :
 oo00OOo0 ( )
 if 97 - 97: Ii1i1i - o0O00o
elif o0OO == 21 :
 i1i1II ( )
 if 64 - 64: ooOO0O0ooOooO . oOOoOooOo / oOOoOooOo - IIiIiII11i
elif o0OO == 4 :
 oooOoOoOo ( )
 if 81 - 81: Ii1I
elif o0OO == 5 :
 iIIIiiiII ( Oo0o00OO0000 )
 if 64 - 64: ooOO0O0ooOooO * oO0o / IIIi11I1 + Ii1i1i % I1ii11iIi11i . o0O00o
elif o0OO == 6 :
 Oo0000ooooOO ( Oo0o00OO0000 )
 if 2 - 2: o0O0Oooo0O + iIII
elif o0OO == 7 :
 IIiIi1I1Ii11 ( Oo0o00OO0000 , iiIiii1IIIII )
 if 47 - 47: Ii + iI11I1II1I1I % Ii1I - ooOO0O0ooOooO % oO0o
elif o0OO == 8 :
 o0O00ooO0O0Oo ( Oo0o00OO0000 , iiIiii1IIIII )
 if 85 - 85: ooOO0O0ooOooO * OOooOOo / OOooOOo
elif o0OO == 9 :
 FIXREPOSADDONS ( Oo0o00OO0000 )
 if 85 - 85: IIIi11I1 / o0O0Oooo0O . ooOoO0O00 / OOooOOo + iI11I1II1I1I
elif o0OO == 10 :
 OoOOoooOO0O ( )
 if 71 - 71: oO0o
elif o0OO == 11 :
 i1Iii1 ( Oo0o00OO0000 )
 if 96 - 96: Ii1I / oOo0O0Ooo - Ii1I / IIiIiII11i - o0O00o
elif o0OO == 12 :
 Ii11111iI1 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 74 - 74: Ii1i1i * ii % IIIi11I1 + ii + IIIIiiII111
elif o0OO == 13 :
 ii1iII11 ( )
 if 83 - 83: ooOoO0O00
elif o0OO == 14 :
 O0oOOoOoo ( Oo0o00OO0000 )
 if 2 - 2: ooOoO0O00 / IIIi11I1 * o0o00Oo0O
elif o0OO == 15 :
 Oooo000 ( )
 if 99 - 99: ii . OOooOOo / IIiIiII11i
elif o0OO == 16 :
 oO0III1iI ( Oo0o00OO0000 , iiIiii1IIIII )
 if 64 - 64: IIIIiiII111 / ooOoO0O00 . oOo0O0Ooo + o0o00Oo0O
elif o0OO == 17 :
 Iii1i1I1iIi ( Oo0o00OO0000 , iiIiii1IIIII )
 if 5 - 5: o0o00Oo0O . Ii
elif o0OO == 18 :
 o00Ooo0OoOOOO ( )
 if 71 - 71: I11i + IIIIiiII111 + oOOoOooOo
elif o0OO == 19 :
 IIII1iI1IiIiI ( Oo0o00OO0000 )
 if 27 - 27: ii . IIIIiiII111 * o0O0Oooo0O % o0o00Oo0O + ii - IIIIiiII111
elif o0OO == 40 :
 o0Oo00Oo ( iiIiii1IIIII , Oo0o00OO0000 , IiI1IIIII1I )
 if 86 - 86: ooOoO0O00
elif o0OO == 42 :
 oooOoOO0o ( iiIiii1IIIII , Oo0o00OO0000 , IiI1IIIII1I )
 if 81 - 81: OOooOOo
elif o0OO == 43 :
 oooo ( Oo0o00OO0000 )
 if 52 - 52: IIIIiiII111 * o0O00o % oOo0O0Ooo * iIII
elif o0OO == 20 :
 i1i11II1 ( Oo0o00OO0000 )
 if 73 - 73: o0O0Oooo0O * oOOoOooOo
elif o0OO == 22 :
 I1oO0O00oOo00o ( Oo0o00OO0000 )
 if 62 - 62: IIIi11I1 . oOo0O0Ooo * iI11I1II1I1I + oO0o * oOOoOooOo / ooOO0O0ooOooO
elif o0OO == 23 :
 oO0OOoOoO ( Oo0o00OO0000 )
 if 14 - 14: IIIIiiII111 / oO0o
elif o0OO == 24 :
 o0oooo00 ( Oo0o00OO0000 )
 if 75 - 75: o0O00o
elif o0OO == 25 :
 iiIII11 ( Oo0o00OO0000 )
 if 68 - 68: o0O00o - ooOoO0O00 % o0O00o . oO0o . Ii . ii
elif o0OO == 26 :
 iiIIOOo0o0o ( Oo0o00OO0000 )
 if 32 - 32: IIIIiiII111 + oO0o % o0O00o + oOo0O0Ooo
elif o0OO == 27 :
 o0Oo000OO ( Oo0o00OO0000 )
 if 69 - 69: o0O0Oooo0O + iIII - iI11I1II1I1I - IIiIiII11i . Ii1i1i
elif o0OO == 28 :
 o0o0O0OOo0OO ( Oo0o00OO0000 )
 if 74 - 74: Ii1I % I11i + o0o00Oo0O - Ii - o0O00o % IIIi11I1
elif o0OO == 29 :
 O00oOoIiIi111ii ( Oo0o00OO0000 )
 if 39 - 39: oO0o - I11i
elif o0OO == 30 :
 O000oo00o000o ( Oo0o00OO0000 )
 if 71 - 71: IIIIiiII111 . oO0o + oOOoOooOo - IIIi11I1 - I1ii11iIi11i
elif o0OO == 31 :
 iIiiiiiIii ( Oo0o00OO0000 )
 if 100 - 100: ii - I11i + o0O0Oooo0O . ii % Ii
elif o0OO == 32 :
 I1I ( )
 if 64 - 64: o0O0Oooo0O % ii / ooOoO0O00 / oO0o
elif o0OO == 33 :
 i11iI11ii ( )
 if 2 - 2: iIII % I11i . oO0o . oO0o
elif o0OO == 35 :
 ii1II ( Oo0o00OO0000 )
 if 89 - 89: oOOoOooOo - ooOO0O0ooOooO + IIiIiII11i + oO0o - o0O00o
elif o0OO == 34 :
 oOo0 ( Oo0o00OO0000 )
 if 27 - 27: o0O0Oooo0O - I11i + oO0o
elif o0OO == 36 :
 o0OoOoOo0O ( Oo0o00OO0000 )
 if 38 - 38: OOooOOo + oO0o . Ii + Ii1i1i % ooOoO0O00 % oOo0O0Ooo
elif o0OO == 37 :
 iiiiI ( Oo0o00OO0000 )
 if 93 - 93: Ii
elif o0OO == 38 :
 OoOoooOO00OO ( Oo0o00OO0000 )
 if 63 - 63: iI11I1II1I1I - iI11I1II1I1I % I11i
elif o0OO == 41 :
 i1iI11i1IIi ( ii1IIi111 )
 if 97 - 97: ooOoO0O00 % iIII % OOooOOo
elif o0OO == 39 :
 OOO ( Oo0o00OO0000 )
 if 25 - 25: OOooOOo . iI11I1II1I1I - IIIIiiII111 % IIiIiII11i . OOooOOo
elif o0OO == 45 :
 TEXTS ( )
 if 16 - 16: IIIi11I1 . I1ii11iIi11i . oOo0O0Ooo % o0o00Oo0O . Ii1I + Ii
elif o0OO == 46 :
 I1i ( )
 if 100 - 100: Ii1I - ooOoO0O00 - oO0o * I11i + OOooOOo
elif o0OO == 47 :
 GEVID ( )
 if 31 - 31: ooOoO0O00
elif o0OO == 48 :
 o0o0O0o0O ( iiIiii1IIIII , Oo0o00OO0000 , IiI1IIIII1I )
 if 21 - 21: I11i / o0o00Oo0O % o0o00Oo0O . ii / oOo0O0Ooo
elif o0OO == 49 :
 oOo00 ( )
 if 94 - 94: oOOoOooOo + oO0o / oOOoOooOo - oOOoOooOo + I1ii11iIi11i + I11i
elif o0OO == 22222 :
 II11IiI1 ( Oo0o00OO0000 )
 if 50 - 50: ooOO0O0ooOooO . I1ii11iIi11i
elif o0OO == 222225 :
 O0o0O0OO0o ( Oo0o00OO0000 )
 if 15 - 15: Ii1i1i
elif o0OO == 222 :
 O0OoI1i1iiiiIII11 ( Oo0o00OO0000 )
 if 64 - 64: ii
elif o0OO == 2222222 :
 O0i1iI ( Oo0o00OO0000 )
 if 25 - 25: o0O00o
elif o0OO == 222222 :
 IiiIIIIIi11 ( Oo0o00OO0000 , iiIiii1IIIII )
 if 29 - 29: OOooOOo % oOOoOooOo * ii
elif o0OO == 333 :
 OoOooOOOooo ( Oo0o00OO0000 )
 if 8 - 8: Ii - o0O0Oooo0O / o0O00o
 if 17 - 17: Ii * oO0o . I11i . ii . OOooOOo - Ii1I
elif o0OO == 1020 :
 iIII1Iiii ( )
 if 78 - 78: Ii1I - ii + o0o00Oo0O
elif o0OO == 1021 :
 ANIMEEP ( )
 if 15 - 15: Ii1I / o0O00o % oOo0O0Ooo
elif o0OO == 1022 :
 ANIMEPLAY ( Oo0o00OO0000 )
 if 16 - 16: Ii1i1i
elif o0OO == 1001 :
 o00oo0 ( )
 if 26 - 26: I11i / iIII + OOooOOo / OOooOOo
elif o0OO == 1005 :
 OOO0o0 ( )
 if 31 - 31: o0O0Oooo0O
elif o0OO == 1007 :
 iIIoOooooO0o0OOO ( Oo0o00OO0000 )
 if 84 - 84: Ii * IIIi11I1 . IIIIiiII111 - Ii1i1i * ooOoO0O00 - Ii1I
elif o0OO == 1010 :
 IiI1iI1 ( Oo0o00OO0000 )
 if 1 - 1: IIiIiII11i
elif o0OO == 1011 :
 OoOoOO0ooo0o0 ( Oo0o00OO0000 )
 if 94 - 94: Ii1I * IIIIiiII111 % IIIIiiII111 % iIII - IIIIiiII111
elif o0OO == 1012 :
 IIoO0Oo0oo0OO ( Oo0o00OO0000 )
 if 38 - 38: o0O00o - oO0o % Ii1i1i - IIiIiII11i
elif o0OO == 1030 :
 iiI1iIi1 ( )
 if 97 - 97: o0o00Oo0O . Ii1i1i
elif o0OO == 1031 :
 oO00 ( Oo0o00OO0000 , ii1IiIiI1 )
 if 52 - 52: o0O00o
elif o0OO == 1032 :
 oO0iII1i111iI ( Oo0o00OO0000 )
 if 86 - 86: o0O0Oooo0O / o0o00Oo0O + ii % ooOO0O0ooOooO
elif o0OO == 1006 :
 Parse . ParseURL ( Oo0o00OO0000 )
 if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . iIII . Ii1i1i
elif o0OO == 2030 :
 Parse . addonParseURL ( Oo0o00OO0000 )
 if 81 - 81: IIiIiII11i + OOooOOo % Ii / IIIIiiII111 . o0O0Oooo0O + IIiIiII11i
elif o0OO == 2031 :
 Parse . apkParseURL ( Oo0o00OO0000 )
 if 48 - 48: oOo0O0Ooo . Ii1I * OOooOOo % ooOoO0O00 / o0O0Oooo0O * IIiIiII11i
elif o0OO == 2032 :
 Parse . ParseBOSS ( Oo0o00OO0000 )
 if 62 - 62: I11i * o0O0Oooo0O . iI11I1II1I1I / ooOoO0O00
elif o0OO == 1002 :
 ooOoOO0Oo0oO0o ( Oo0o00OO0000 )
 if 75 - 75: ii / oOOoOooOo - IIIIiiII111 . ii . OOooOOo % ooOoO0O00
elif o0OO == 1003 :
 oOo0oOoooo0 ( Oo0o00OO0000 , ii1IiIiI1 )
 if 7 - 7: OOooOOo . ooOoO0O00 * Ii % Ii
elif o0OO == 1004 :
 OOOoO0000ooO ( Oo0o00OO0000 )
 if 54 - 54: oO0o / oOo0O0Ooo . I1ii11iIi11i
elif o0OO == 1008 :
 II11 ( )
 if 39 - 39: oO0o . oOOoOooOo
elif o0OO == 1009 :
 Ii1I1iIiIi ( Oo0o00OO0000 )
 if 41 - 41: I1ii11iIi11i * Ii1I - IIiIiII11i - IIiIiII11i
elif o0OO == 2001 :
 II1oo0OO0OoO ( )
 if 7 - 7: ooOO0O0ooOooO
elif o0OO == 2002 :
 iI1iI ( Oo0o00OO0000 )
 if 41 - 41: oOOoOooOo
elif o0OO == 1013 :
 Oo0o0OoOoOo0 ( )
elif o0OO == 10111113 :
 oo0OoOO000O ( Oo0o00OO0000 )
 if 93 - 93: Ii1i1i + o0O0Oooo0O + Ii1i1i
elif o0OO == 1014 :
 oOOo0o0O0oO0o ( )
 if 23 - 23: oOo0O0Ooo - ooOoO0O00 / oOOoOooOo
elif o0OO == 1015 :
 iiIi ( Oo0o00OO0000 )
 if 4 - 4: o0O00o . Ii1I + IIIIiiII111 % oOOoOooOo
elif o0OO == 1016 :
 iiIii1IIi ( Oo0o00OO0000 , ii1IiIiI1 , iiIiii1IIIII )
 if 28 - 28: o0O0Oooo0O
elif o0OO == 1017 :
 IiiI11i1I ( )
 if 27 - 27: IIIIiiII111 * oOo0O0Ooo
elif o0OO == 1018 :
 OOo0 ( Oo0o00OO0000 )
 if 60 - 60: ooOoO0O00 / oOo0O0Ooo - Ii1I
elif o0OO == 1019 :
 O0i1i1II1i11 ( Oo0o00OO0000 )
elif o0OO == 10190 :
 iI111I11i ( Oo0o00OO0000 )
 if 41 - 41: o0O0Oooo0O + oOOoOooOo / IIIi11I1 + iIII % I1ii11iIi11i
elif o0OO == 1023 :
 I1iI1 ( )
 if 91 - 91: oOo0O0Ooo % Ii1I % ooOO0O0ooOooO / ooOoO0O00 * iI11I1II1I1I + iIII
elif o0OO == 1024 :
 Oo0OoO ( Oo0o00OO0000 )
 if 48 - 48: oOOoOooOo / Ii1I / oO0o / IIiIiII11i * OOooOOo
elif o0OO == 1025 :
 O00oo0o ( Oo0o00OO0000 )
 if 73 - 73: iIII / oOo0O0Ooo - o0O00o - ooOoO0O00 * o0O00o - IIIi11I1
elif o0OO == 4001 :
 i11i1iiI1i ( )
 if 39 - 39: iIII . oOOoOooOo * IIiIiII11i
elif o0OO == 4002 :
 Ooo0o0OOO ( )
 if 21 - 21: Ii1i1i
elif o0OO == 4003 :
 iI11II11I1 ( )
 if 92 - 92: oO0o * Ii1I + iI11I1II1I1I
elif o0OO == 4004 :
 IIIiIi ( )
 if 88 - 88: iI11I1II1I1I + iI11I1II1I1I * Ii . Ii1I % ooOO0O0ooOooO
elif o0OO == 4005 :
 o000 ( )
 if 94 - 94: oOo0O0Ooo / Ii1I / IIIi11I1
elif o0OO == 4006 :
 I11iIiII ( )
 if 45 - 45: IIiIiII11i
elif o0OO == 4007 :
 o00O0O ( )
 if 98 - 98: Ii + Ii1I * IIIi11I1 / OOooOOo
elif o0OO == 4008 :
 O00o00O ( )
 if 84 - 84: I11i
elif o0OO == 40099 : o0Oo0ooo ( )
elif o0OO == 4009 : o0o0oO0OOO ( )
elif o0OO == 4010 : iioOO ( )
elif o0OO == 3000 :
 iII1II1ii1 ( )
 if 40 - 40: ii - ooOO0O0ooOooO / o0o00Oo0O * o0O0Oooo0O . o0o00Oo0O + Ii
elif o0OO == 3001 :
 iIiIIiII11i1 ( )
 if 9 - 9: IIIi11I1 % o0o00Oo0O % o0o00Oo0O / Ii1I . IIiIiII11i / IIiIiII11i
elif o0OO == 3002 :
 i1Iii ( Oo0o00OO0000 )
 if 78 - 78: iI11I1II1I1I - ooOoO0O00 . iIII . I11i
elif o0OO == 3003 :
 oOOooo ( Oo0o00OO0000 )
 if 66 - 66: IIIi11I1 * I1ii11iIi11i
elif o0OO == 3004 :
 oOOo0OoooOo ( Oo0o00OO0000 )
 if 58 - 58: IIIi11I1
elif o0OO == 404 :
 ooOOO ( iiIiii1IIIII , Oo0o00OO0000 , ii1IiIiI1 )
 if 96 - 96: o0O00o % ii + o0o00Oo0O * IIiIiII11i / IIIi11I1 . o0O0Oooo0O
elif o0OO == 405 :
 o0Oo0OOO0 ( Oo0o00OO0000 )
 if 47 - 47: oO0o - I1ii11iIi11i * oO0o / ooOO0O0ooOooO
elif o0OO == 7030 :
 iI1IIi1I ( )
 if 13 - 13: oOOoOooOo
elif o0OO == 7021 :
 O0O0OoO0o0OO ( iiIiii1IIIII )
 if 55 - 55: ooOoO0O00 . iIII . IIiIiII11i + o0o00Oo0O + oOOoOooOo - ooOoO0O00
elif o0OO == 7022 :
 Ii1IiiI ( iiIiii1IIIII )
 if 3 - 3: iI11I1II1I1I / ooOO0O0ooOooO
elif o0OO == 7000 :
 O00i1IiI111II1 ( iiIiii1IIIII , Oo0o00OO0000 , img )
 if 61 - 61: o0O0Oooo0O / o0o00Oo0O - IIIIiiII111
elif o0OO == 7050 :
 I11iiI11I1II ( Oo0o00OO0000 )
 if 44 - 44: ooOoO0O00
elif o0OO == 7051 :
 I11I1iI ( Oo0o00OO0000 )
 if 23 - 23: Ii1I . ii / Ii1i1i + I11i
elif o0OO == 7052 :
 iiIiIi1I1 ( Oo0o00OO0000 )
 if 89 - 89: OOooOOo + I1ii11iIi11i . OOooOOo - IIiIiII11i
elif o0OO == 7053 :
 ii11I1IIII11 ( Oo0o00OO0000 )
 if 85 - 85: ii * ii / Ii1i1i - IIiIiII11i
elif o0OO == 7054 :
 CoolPlay ( Oo0o00OO0000 )
 if 69 - 69: IIIIiiII111 * iIII
elif o0OO == 7060 :
 iIiiii ( )
 if 43 - 43: I11i - o0O00o * Ii1i1i . Ii / IIiIiII11i
elif o0OO == 7061 :
 iI111i1I1II ( Oo0o00OO0000 )
 if 61 - 61: OOooOOo / oOo0O0Ooo . Ii1I % IIIi11I1
elif o0OO == 7063 :
 ii111Ii ( Oo0o00OO0000 )
 if 70 - 70: IIIi11I1 * OOooOOo / ooOO0O0ooOooO + I1ii11iIi11i / o0o00Oo0O
elif o0OO == 7062 :
 oOoo0OoooOo0o ( Oo0o00OO0000 )
 if 16 - 16: I1ii11iIi11i / ii / o0O00o + I1ii11iIi11i * Ii
elif o0OO == 7064 :
 NATatozcat ( )
 if 15 - 15: I11i / Ii
elif o0OO == 7067 :
 oOoooOOO0o0 ( Oo0o00OO0000 )
 if 63 - 63: Ii1I - Ii1i1i + iIII
elif o0OO == 7066 :
 NATatozA ( Oo0o00OO0000 )
 if 98 - 98: IIIIiiII111 / o0O00o * oOo0O0Ooo / ooOO0O0ooOooO - iI11I1II1I1I
elif o0OO == 7065 :
 i11iII1Ii1ii111 ( Oo0o00OO0000 )
 if 72 - 72: o0o00Oo0O . IIIi11I1
elif o0OO == 7070 :
 o0oOiiI1 ( )
 if 99 - 99: ooOoO0O00 + iI11I1II1I1I - oOOoOooOo + oO0o + I1ii11iIi11i . Ii1I
elif o0OO == 7071 :
 DIZIlist ( Oo0o00OO0000 )
 if 74 - 74: ooOoO0O00
elif o0OO == 7072 :
 DIZIpull ( Oo0o00OO0000 )
 if 80 - 80: oOOoOooOo + o0O0Oooo0O . Ii1I % ii
elif o0OO == 7073 :
 WATCHDIZI ( Oo0o00OO0000 )
 if 26 - 26: OOooOOo . IIIIiiII111 * iI11I1II1I1I / o0O00o
elif o0OO == 7002 :
 oO0OOOOo ( )
 if 69 - 69: ii / iIII + Ii1i1i * IIiIiII11i
elif o0OO == 7003 :
 iII11iIII ( Oo0o00OO0000 )
 if 35 - 35: Ii + ooOO0O0ooOooO
elif o0OO == 7004 :
 oOoo0O0o ( Oo0o00OO0000 )
 if 85 - 85: OOooOOo . o0o00Oo0O % ii % ooOO0O0ooOooO
elif o0OO == 7020 :
 i1I1ii1iI1 ( Oo0o00OO0000 )
 if 43 - 43: oOo0O0Ooo - iIII . oOo0O0Ooo / Ii % o0O00o * Ii
elif o0OO == 7001 :
 I11Oo00oO0O ( )
 if 12 - 12: IIiIiII11i - iI11I1II1I1I
elif o0OO == 7010 :
 o00Ooo0Oo ( Oo0o00OO0000 )
 if 43 - 43: Ii % oO0o
elif o0OO == 7011 :
 O0ooOoI11Iii1iIII1i ( Oo0o00OO0000 )
 if 100 - 100: ooOoO0O00
elif o0OO == 7012 :
 iioOo0oo ( Oo0o00OO0000 )
 if 4 - 4: Ii - IIIi11I1 * o0O00o % ii - OOooOOo
elif o0OO == 7013 :
 cnfTVPlay2 ( Oo0o00OO0000 )
elif o0OO == 7014 :
 CNF_Studio_Indexer . MV_Movies ( Oo0o00OO0000 )
elif o0OO == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( Oo0o00OO0000 )
elif o0OO == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiIiii1IIIII , Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif o0OO == 7018 :
 i1IIiO0o0O ( )
elif o0OO == 7019 :
 CNF_Studio_Indexer . List_Movies ( Oo0o00OO0000 )
elif o0OO == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( Oo0o00OO0000 )
elif o0OO == 7024 :
 CNF_Studio_Indexer . Box_Office ( Oo0o00OO0000 )
 if 81 - 81: Ii1i1i * oOOoOooOo . ooOO0O0ooOooO . o0O00o
elif o0OO == 8000 :
 I1Ii1iiI1 ( )
elif o0OO == 8001 :
 IiIIi1I ( )
elif o0OO == 8002 :
 oO00o ( )
elif o0OO == 8003 :
 O0o0o00O0OO00 ( )
elif o0OO == 8004 :
 Ii1II1I ( )
elif o0OO == 8005 :
 oOooOO00OO ( )
elif o0OO == 8006 :
 iI1Iii11Iii11 ( iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 8030 :
 iIOOO ( Oo0o00OO0000 )
elif o0OO == 8045 :
 OOo ( Oo0o00OO0000 )
elif o0OO == 8046 :
 i1Iiiiiii ( Oo0o00OO0000 )
elif o0OO == 8047 :
 oO0OO0o0oo0o ( Oo0o00OO0000 )
elif o0OO == 8048 :
 II1i1 ( Oo0o00OO0000 )
elif o0OO == 8049 :
 ooO0OoOO0 ( Oo0o00OO0000 )
elif o0OO == 804900 :
 o0oo00 ( Oo0o00OO0000 )
elif o0OO == 8020 :
 I1iii ( )
elif o0OO == 8021 :
 oOoI1I ( Oo0o00OO0000 )
elif o0OO == 8022 :
 I11iiiI1iiIiI ( Oo0o00OO0000 )
elif o0OO == 8023 :
 IIii ( Oo0o00OO0000 )
elif o0OO == 8040 :
 ii1iii11i1 ( )
elif o0OO == 8041 :
 iiii11IiI1 ( Oo0o00OO0000 )
elif o0OO == 8042 :
 o0oOOO0000o ( Oo0o00OO0000 )
elif o0OO == 8043 :
 yt . PlayVideo ( Oo0o00OO0000 )
elif o0OO == 8044 :
 OO000o0O0OO0 ( Oo0o00OO0000 )
elif o0OO == 8060 :
 o0OoO000O ( )
elif o0OO == 8061 :
 iII1IIoO00oOOOO ( Oo0o00OO0000 )
elif o0OO == 8064 :
 o00oIII11I ( )
elif o0OO == 8065 :
 OO0ooo ( Oo0o00OO0000 )
elif o0OO == 8070 :
 O0OO0Oo ( )
elif o0OO == 8071 :
 II1111iII1 ( Oo0o00OO0000 )
elif o0OO == 7080 :
 iio0000oO0OOOo0 ( Oo0o00OO0000 )
elif o0OO == 8090 :
 o0Ooo0 ( )
elif o0OO == 8091 :
 Oo0ooo0oOo0Oo0O ( Oo0o00OO0000 )
elif o0OO == 8092 :
 II1OOooo ( Oo0o00OO0000 )
elif o0OO == 8093 :
 II1ii1iI1I1i ( Oo0o00OO0000 )
elif o0OO == 8081 :
 iiiiIIiiII1Iii1 ( )
elif o0OO == 8062 :
 oOO0Oo00o ( Oo0o00OO0000 )
elif o0OO == 8063 :
 o0Oo ( Oo0o00OO0000 )
elif o0OO == 8050 :
 oO00o0 ( )
elif o0OO == 8051 :
 o00OoOo0 ( Oo0o00OO0000 )
elif o0OO == 8052 :
 Iii1I ( Oo0o00OO0000 )
elif o0OO == 8085 :
 iioOOOoOo0oOoo ( )
elif o0OO == 8086 :
 Iii1iii11 ( Oo0o00OO0000 )
elif o0OO == 8087 :
 oO0OOOo0OO ( Oo0o00OO0000 )
elif o0OO == 8088 :
 i1IiI ( Oo0o00OO0000 , iiIiii1IIIII )
elif o0OO == 9000 :
 O0Oo0o000Oo0ooOo ( )
elif o0OO == 1111 :
 oOoo ( )
elif o0OO == 9001 :
 IiiIIIII1iii ( )
elif o0OO == 9002 :
 OOooo0O ( )
elif o0OO == 9003 :
 IiIIiI ( )
elif o0OO == 9004 :
 World1 ( )
elif o0OO == 9005 :
 World2 ( Oo0o00OO0000 )
elif o0OO == 9006 :
 World3 ( Oo0o00OO0000 )
elif o0OO == 9007 :
 I1i1ii ( )
elif o0OO == 9008 :
 ii1iIiIIiIIii ( Oo0o00OO0000 )
elif o0OO == 9009 :
 ooooo ( Oo0o00OO0000 )
elif o0OO == 9010 :
 oooOo ( )
elif o0OO == 9011 :
 OooOOo0 ( Oo0o00OO0000 )
elif o0OO == 50 :
 Iii1iiIIi1i111i ( Oo0o00OO0000 )
elif o0OO == 9020 :
 champlist ( )
elif o0OO == 9021 :
 II11iI ( )
elif o0OO == 9022 :
 I1I1iII1I1I11 ( )
elif o0OO == 9023 :
 IiIII ( )
elif o0OO == 9024 :
 iI11i1Ii ( Oo0o00OO0000 )
elif o0OO == 9030 :
 iII1 ( Oo0o00OO0000 )
elif o0OO == 9031 :
 I1i11I ( Oo0o00OO0000 )
elif o0OO == 9032 :
 I1iiIiI1II1ii ( Oo0o00OO0000 )
elif o0OO == 9033 :
 IiI1II1iIi ( Oo0o00OO0000 )
elif o0OO == 9034 :
 iIi1III1I ( )
elif o0OO == 7085 :
 OOoOoOOo ( Oo0o00OO0000 )
elif o0OO == 7086 :
 OooO00O0OOOO ( Oo0o00OO0000 )
elif o0OO == 7087 :
 iIiiIIIOo ( IiI1IIIII1I )
elif o0OO == 9666 :
 iI1i11 ( Oo0o00OO0000 )
elif o0OO == 10100 : I1111iiiII1Ii ( )
elif o0OO == 101001 : oO0o0O ( Oo0o00OO0000 )
elif o0OO == 10105 : I1iOO000o0o0oo ( Oo0o00OO0000 )
elif o0OO == 10106 : oO00oOoo0ooO0 ( Oo0o00OO0000 )
elif o0OO == 10104 : i1i1iiO0Oo ( Oo0o00OO0000 )
elif o0OO == 10107 : OoO0O00OO0OoO00oO ( )
elif o0OO == 10103 : Ooo0o0ooO0 ( Oo0o00OO0000 )
elif o0OO == 10108 : i11i1iI ( Oo0o00OO0000 )
elif o0OO == 10000 : Origin_Menu ( )
elif o0OO == 10001 : oo000oO ( )
elif o0OO == 10002 : IIiI11i1111Ii ( )
elif o0OO == 10003 : oo0OO0Oo000oo ( )
elif o0OO == 10004 : IIII1IiiI ( Oo0o00OO0000 )
elif o0OO == 10005 : OoOo0000o0OOo ( )
elif o0OO == 10006 : OOOOo0ooOOO0 ( Oo0o00OO0000 )
elif o0OO == 10007 : OoO00o ( Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 10008 : iIo0O00o00o0 ( )
elif o0OO == 10009 : oo00oO0o000 ( )
elif o0OO == 10010 : I1i1I1i1I1 ( Oo0o00OO0000 )
elif o0OO == 10011 : OOO00i111 ( Oo0o00OO0000 )
elif o0OO == 10012 : O0i1iI ( Oo0o00OO0000 )
elif o0OO == 10113 : GRABG ( Oo0o00OO0000 , iiIiii1IIIII )
elif o0OO == 10109 : I1I1IIi11II ( Oo0o00OO0000 )
elif o0OO == 10013 : iIIiiiI1 ( Oo0o00OO0000 )
elif o0OO == 10014 : ooOooOOOoO0 ( )
elif o0OO == 10015 : OOO0o0O00O ( )
elif o0OO == 10016 : o0OOII1I1 ( Oo0o00OO0000 )
elif o0OO == 10017 : OO0oO ( )
elif o0OO == 10018 : i1o00Oo ( )
elif o0OO == 10019 : IIiI ( )
elif o0OO == 10020 : O0O000 ( )
elif o0OO == 10021 : o0oOo ( )
elif o0OO == 10022 : oOOiI111I ( Oo0o00OO0000 )
elif o0OO == 10023 : o0OO0OOoo0oO ( iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 10024 : iiiiiiI ( Oo0o00OO0000 )
elif o0OO == 10025 : i1II ( )
elif o0OO == 10026 : O000 ( )
elif o0OO == 10027 : oOoOO00Ooo ( )
elif o0OO == 10028 : iI1Iiii11Iii ( )
elif o0OO == 10029 : OO0OO0 ( )
elif o0OO == 423 : ii111I111i ( Oo0o00OO0000 )
elif o0OO == 426 : OoOOOo0 ( Oo0o00OO0000 )
elif o0OO == 10030 : Izle_Films ( )
elif o0OO == 10031 : Latest_Izle_Movies ( )
elif o0OO == 10032 : Izle_Genres ( )
elif o0OO == 10033 : Izle_Pop_Movies ( )
elif o0OO == 10034 : Izle_Boxsets ( )
elif o0OO == 10035 : Izle_Search ( )
elif o0OO == 10036 : Izle_Genres_Movie ( Oo0o00OO0000 )
elif o0OO == 10037 : Izle_Boxset_single ( Oo0o00OO0000 )
elif o0OO == 10038 : Izle_IFRAME ( )
elif o0OO == 10039 : Izle_Boxsets_Next ( Oo0o00OO0000 )
elif o0OO == 10040 : oo00OOoOoO00 ( )
elif o0OO == 10041 : II1O0ooo00o0 ( Oo0o00OO0000 )
elif o0OO == 10042 : ooO0000 ( Oo0o00OO0000 )
elif o0OO == 10043 : oO0Ooo00O ( )
elif o0OO == 10044 : Ii1II1iiiiiIi1I1i ( Oo0o00OO0000 )
elif o0OO == 10045 : o0O0oOOoo0O0 ( iiIiii1IIIII )
elif o0OO == 10046 : iIiiIII ( Oo0o00OO0000 )
elif o0OO == 10047 : i1I1Iii1IiiIi ( Oo0o00OO0000 )
elif o0OO == 10048 : i111II ( Oo0o00OO0000 )
elif o0OO == 10049 : O0o0ooo00o00 ( Oo0o00OO0000 )
elif o0OO == 10050 : IiO00Oooo0o000 ( )
elif o0OO == 10051 : OoOo0Oo0 ( )
elif o0OO == 10052 : ii1i1II1 ( )
elif o0OO == 10053 : Addon ( Oo0o00OO0000 )
elif o0OO == 10054 : o0OOoo ( Oo0o00OO0000 , iiIiii1IIIII )
elif o0OO == 10055 :
 OO000o0O0o ( "addFavorite" )
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiIi1i ( iiIiii1IIIII , Oo0o00OO0000 , ii1IiIiI1 , ooo0O0o00O , iI1IIiiiI )
elif o0OO == 10056 :
 OO000o0O0o ( "rmFavorite" )
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 iI11i ( iiIiii1IIIII )
elif o0OO == 10057 :
 OO000o0O0o ( "getFavorites" )
 OOoo00OoO0o ( )
elif o0OO == 10058 : O00000OO00OO ( )
elif o0OO == 10059 : Donators_Guide ( )
elif o0OO == 10060 : oO0oOOoo00000 ( )
elif o0OO == 10061 : II11i1I1iiII1 ( )
elif o0OO == 10062 : iIO0oOoo00Oo0O ( iiIiii1IIIII , Oo0o00OO0000 , IiI1IIIII1I )
elif o0OO == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + IIIii1II1II + ")" )
elif o0OO == 10064 : Oo0O0ooo0O0O ( )
elif o0OO == 10065 : iiiiii1Ii ( Oo0o00OO0000 )
elif o0OO == 10066 : oooooO00OOO ( Oo0o00OO0000 )
elif o0OO == 10068 : II1Ii1iI1i1 ( Oo0o00OO0000 )
elif o0OO == 10069 : Ii1I11I ( Oo0o00OO0000 )
elif o0OO == 10070 : o00oOoo0o00 ( Oo0o00OO0000 )
elif o0OO == 10071 : Genie_Watch ( )
elif o0OO == 10072 : Ooo0oOOoo0O ( )
elif o0OO == 10073 : iI11IiIiiII1 ( Oo0o00OO0000 )
elif o0OO == 10074 : oO0I1I1i1I1I1I1 ( Oo0o00OO0000 )
elif o0OO == 10075 : i1I1i1i1I1 ( ii1IiIiI1 , iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 10076 : O0OOOOOO0ooO ( Oo0o00OO0000 )
elif o0OO == 10077 : IiI11I1Ii11II ( Oo0o00OO0000 )
elif o0OO == 10078 : OoO0o0oOOO ( )
elif o0OO == 10079 : Genie_Watch_Tv_Shows ( )
elif o0OO == 10080 : Genie_Watch_Tv_Genre ( Oo0o00OO0000 )
elif o0OO == 10081 : Genie_Watch_TV_PlayRun ( Oo0o00OO0000 )
elif o0OO == 10082 : Genie_Watch_TV_Episodes ( Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 10083 : Genie_Watch_Tv_Recent ( Oo0o00OO0000 )
elif o0OO == 10084 : oOO0oo ( )
elif o0OO == 10085 : I11iiI1i1 ( )
elif o0OO == 10086 : iioOooOOOoOo ( )
elif o0OO == 20000 : iiII11 ( )
elif o0OO == 20001 : OOo0i111ii1Ii ( Oo0o00OO0000 )
elif o0OO == 20002 : o00oIiIiIiiI ( Oo0o00OO0000 )
elif o0OO == 20003 : o0ooOOOo0O0 ( Oo0o00OO0000 )
elif o0OO == 20004 : o00Oo ( Oo0o00OO0000 )
elif o0OO == 20005 : OooOo ( Oo0o00OO0000 )
elif o0OO == 21004 : I1I11i ( )
elif o0OO == 21005 : OoO ( Oo0o00OO0000 )
elif o0OO == 21006 : OOoo ( Oo0o00OO0000 )
elif o0OO == 21007 : iIo0O000O00o ( Oo0o00OO0000 )
elif o0OO == 21008 : O0OoooO0 ( Oo0o00OO0000 )
elif o0OO == 21009 : OOOOoOOo0O0 ( Oo0o00OO0000 )
elif o0OO == 30000 : oo0 ( )
elif o0OO == 30001 : Ii1i1 ( )
elif o0OO == 100121 : Resolve ( Oo0o00OO0000 )
elif o0OO == 30003 : i111 ( )
elif o0OO == 30004 : Ii111 ( Oo0o00OO0000 )
elif o0OO == 30005 : ii1II11IIII ( Oo0o00OO0000 )
elif o0OO == 30006 : o0O0oOo00oOoo ( )
elif o0OO == 30007 : Oo0oO ( )
elif o0OO == 30008 : O00oooo00 ( Oo0o00OO0000 )
elif o0OO == 30009 : iiiii1i1 ( Oo0o00OO0000 )
elif o0OO == 30010 : Iii1IiIIiII1 ( Oo0o00OO0000 )
elif o0OO == 30011 : O0oOo00Oo0oo0 ( )
elif o0OO == 30012 : OoOO0o00OOO0o ( )
elif o0OO == 30013 : II1IIiiIiI11 ( )
elif o0OO == 30014 : OO0OoOo00 ( )
elif o0OO == 30015 : o0o ( Oo0o00OO0000 , ii1IiIiI1 , ooo0O0o00O )
elif o0OO == 30016 : IIiIiiiii11 ( Oo0o00OO0000 )
elif o0OO == 30019 : OOO000OOOO0oO ( Oo0o00OO0000 )
elif o0OO == 30017 : oo000o ( Oo0o00OO0000 )
elif o0OO == 30018 : o0OOo0o0o0ooo ( Oo0o00OO0000 )
elif o0OO == 30030 : IIIIIii1iiIIi ( )
elif o0OO == 30031 : I1iIiI ( )
elif o0OO == 30032 : oOO ( )
elif o0OO == 30033 : oO0oOoOoo0 ( )
elif o0OO == 30034 : OoOoOo ( )
elif o0OO == 30035 : ii11IoOO0OooO0O ( Oo0o00OO0000 )
elif o0OO == 30036 : o00O0o0oo0 ( Oo0o00OO0000 )
elif o0OO == 30037 : ooo000 ( Oo0o00OO0000 )
elif o0OO == 30038 : O0O000OOOoO ( )
elif o0OO == 30039 : ooO0O00Oo0o ( )
elif o0OO == 50000 : ooo00Ooo ( )
elif o0OO == 50001 : oOO0o ( )
elif o0OO == 50002 : oooOOOO0oOo ( Oo0o00OO0000 )
elif o0OO == 50003 : Table_Menu ( IiI1IIIII1I )
elif o0OO == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif o0OO == 60001 : iiI1i ( )
elif o0OO == 60002 : II1I1ii ( iiIiii1IIIII )
elif o0OO == 60003 : I11iIiIii ( Oo0o00OO0000 )
elif o0OO == 600033 : IIIIi1Iii1iIi ( Oo0o00OO0000 )
elif o0OO == 60004 : oooOo00 ( Oo0o00OO0000 )
elif o0OO == 50004 : iiI11 ( )
elif o0OO == 50005 : speedtest . runtest ( Oo0o00OO0000 )
elif o0OO == 70001 : oo0o0000 ( )
elif o0OO == 70002 : OO0I11IIi1I1 ( Oo0o00OO0000 )
elif o0OO == 70003 : Iiiii ( Oo0o00OO0000 )
elif o0OO == 70004 : IiIi1I1IiI1II1 ( Oo0o00OO0000 )
elif o0OO == 70005 : iii1 ( Oo0o00OO0000 )
elif o0OO == 70006 : iII1iii ( )
elif o0OO == 50006 : Ii1I1Ii ( i1 , i1111 )
elif o0OO == 80000 : ooo0oOoO00Oo ( )
elif o0OO == 80001 : resolvefilmon ( Oo0o00OO0000 )
elif o0OO == 80002 : o0o000O0ooo0O ( )
elif o0OO == 80003 : ooooooo0oOo0 ( iiIiii1IIIII , Oo0o00OO0000 , "None" )
elif o0OO == 80004 : I1I1IiI ( iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 80005 : O00OO ( )
elif o0OO == 80006 : IIi111 ( Oo0o00OO0000 )
elif o0OO == 80007 : oO0o0o0O ( Oo0o00OO0000 )
elif o0OO == 80008 : I111ii1iI ( )
elif o0OO == 80009 : i1II1iI ( )
elif o0OO == 80010 : oOOo0oOO ( Oo0o00OO0000 )
elif o0OO == 80011 : iI1II ( Oo0o00OO0000 )
elif o0OO == 80012 : Oo00o ( )
elif o0OO == 90000 : oOoO ( iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 90001 : tools ( )
elif o0OO == 90002 : IiI1iII1II111 ( )
elif o0OO == 90003 : II1OO ( Oo0o00OO0000 )
elif o0OO == 90004 : oo0OOO0O0 ( Oo0o00OO0000 )
elif o0OO == 90005 : OoooOooo ( Oo0o00OO0000 )
elif o0OO == 90006 : I1Ioo000oooooooO ( Oo0o00OO0000 )
elif o0OO == 90007 : II1IIi1ii111 ( Oo0o00OO0000 )
elif o0OO == 90008 : OOoOo000 ( Oo0o00OO0000 )
elif o0OO == 90009 : o00O0oOO0o ( Oo0o00OO0000 )
elif o0OO == 90010 : OOOOO0O00 ( )
elif o0OO == 90020 : O0Ooo000OO00 ( )
elif o0OO == 90021 : hellyeah2 ( Oo0o00OO0000 )
elif o0OO == 90022 : hellyeah3 ( Oo0o00OO0000 )
elif o0OO == 90023 : Ii11i1Ii1IIII ( )
elif o0OO == 90024 : II111 ( Oo0o00OO0000 )
elif o0OO == 90025 : OOO000000OOO0 ( Oo0o00OO0000 )
if 71 - 71: o0O00o + oO0o
elif o0OO == 90026 : II111iii ( )
elif o0OO == 90027 : o0o0O0oOooO00 ( iiIiii1IIIII , Oo0o00OO0000 , IiI1IIIII1I )
elif o0OO == 90028 : iII1IiiIIIIii ( Oo0o00OO0000 )
if 39 - 39: oOo0O0Ooo % o0O00o / IIiIiII11i / IIiIiII11i
elif o0OO == 900300 : i1II1I1Iii1 ( )
elif o0OO == 900301 : O0o ( Oo0o00OO0000 )
elif o0OO == 900302 : iII111Ii ( Oo0o00OO0000 )
elif o0OO == 90030 : Oo0OO0000oooo ( )
elif o0OO == 90031 : Treplays ( )
elif o0OO == 90032 : Treplays2 ( Oo0o00OO0000 )
elif o0OO == 90033 : Treplays3 ( Oo0o00OO0000 )
elif o0OO == 90034 : Treplays4 ( Oo0o00OO0000 )
elif o0OO == 90035 : O0OoO0ooOO0o ( Oo0o00OO0000 )
elif o0OO == 90036 : O0o0ooO0oO0oO ( Oo0o00OO0000 )
elif o0OO == 90039 : iI1iII111ii1I ( Oo0o00OO0000 )
elif o0OO == 90037 : O0oOO0o ( Oo0o00OO0000 )
elif o0OO == 900377 : oo0ooooo00o ( Oo0o00OO0000 )
elif o0OO == 90038 : Oo0oOo000OoO0 ( )
if 95 - 95: IIiIiII11i + Ii + I11i
elif o0OO == 10090 : oOooo ( )
elif o0OO == 10091 : IiI1iIIiIi1Ii ( Oo0o00OO0000 )
elif o0OO == 10092 : IIiIi ( Oo0o00OO0000 )
elif o0OO == 10093 : iI1Iii11II ( Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 10094 : OO00O0O ( Oo0o00OO0000 , ii1IiIiI1 )
if 30 - 30: o0o00Oo0O - o0o00Oo0O % iI11I1II1I1I + IIIIiiII111 * ii
elif o0OO == 10095 : oOO0OO0O ( )
elif o0OO == 10096 : IIiiI ( Oo0o00OO0000 )
elif o0OO == 10097 : i1IIOO0oo00oOO ( Oo0o00OO0000 )
elif o0OO == 10098 : oOoo00o0oOO ( Oo0o00OO0000 )
elif o0OO == 10099 : oOoo0ooOoo ( Oo0o00OO0000 )
if 1 - 1: o0o00Oo0O
elif o0OO == 10200 : IIiiii ( )
elif o0OO == 10201 : i1ii1iiIi1II ( iiIiii1IIIII , Oo0o00OO0000 , IiI1IIIII1I )
elif o0OO == 10202 : ooooO000 ( Oo0o00OO0000 )
elif o0OO == 10203 : RT4 ( Oo0o00OO0000 )
if 36 - 36: ooOO0O0ooOooO . IIIIiiII111
elif o0OO == 90040 : i1Ii ( )
elif o0OO == 90041 : I111 ( Oo0o00OO0000 )
elif o0OO == 90042 : i1oooOoOoOO ( Oo0o00OO0000 )
elif o0OO == 90043 : iiI1ii1Iii ( Oo0o00OO0000 )
elif o0OO == 90044 : IiI1IiI1iiI1 ( Oo0o00OO0000 )
elif o0OO == 90045 : Oo0Oo ( )
elif o0OO == 90046 : O000o0 ( Oo0o00OO0000 )
elif o0OO == 90050 : iIiIIi11iI ( )
elif o0OO == 90051 : oOOo0ooO0 ( Oo0o00OO0000 )
elif o0OO == 90052 : ooO ( Oo0o00OO0000 )
elif o0OO == 90053 : o00oO0o00O ( Oo0o00OO0000 )
elif o0OO == 90054 : ooo00 ( Oo0o00OO0000 )
elif o0OO == 90055 : OOO000Oo ( )
if 62 - 62: iIII + iI11I1II1I1I % iIII * IIIi11I1 + iI11I1II1I1I % Ii1i1i
elif o0OO == 100001 : Stand_up ( )
if 56 - 56: I11i
elif o0OO == 100003 : o0OOII1I1 ( Oo0o00OO0000 )
elif o0OO == 100004 : I11i11I1iiII ( Oo0o00OO0000 )
elif o0OO == 100005 : Resolve ( Oo0o00OO0000 )
elif o0OO == 100008 : Search ( )
elif o0OO == 100007 : OoOO ( Oo0o00OO0000 )
elif o0OO == 100009 : yt . PlayVideo ( Oo0o00OO0000 )
elif o0OO == 100010 : iii11 ( Oo0o00OO0000 )
elif o0OO == 100100 : iIi1Ii ( ii1IiIiI1 , Oo0o00OO0000 , o00oo0OO0 )
elif o0OO == 100101 : OoIIi1iI ( Oo0o00OO0000 , iiIiii1IIIII , ooo0O0o00O , o00oo0OO0 , ii1IiIiI1 )
elif o0OO == 100102 : o0OOoOO ( iiIiii1IIIII , Oo0o00OO0000 , ii1IiIiI1 , ooo0O0o00O )
elif o0OO == 100106 : ii1111Ii1i ( Oo0o00OO0000 , iiIiii1IIIII )
elif o0OO == 100107 : I1iIII1IiiI ( )
elif o0OO == 100108 : o0Ooo ( )
elif o0OO == 100109 : OOoOO ( Oo0o00OO0000 )
elif o0OO == 40000 : i1io0o00O ( )
elif o0OO == 40001 : I11IIIIiI1 ( Oo0o00OO0000 )
elif o0OO == 100110 : O0OOO00OOO00o ( Oo0o00OO0000 )
elif o0OO == 100111 : I1i1iII1I11 ( Oo0o00OO0000 )
elif o0OO == 100112 : oOoO00O ( Oo0o00OO0000 )
elif o0OO == 100113 : O00O00 ( Oo0o00OO0000 )
elif o0OO == 100114 : i11o00Ooo ( Oo0o00OO0000 )
elif o0OO == 100115 : I111Iii1 ( Oo0o00OO0000 )
elif o0OO == 100117 : OoO00OOoOOOo0 ( Oo0o00OO0000 )
elif o0OO == 100118 : II1IIiiI1 ( Oo0o00OO0000 )
elif o0OO == 100120 : i11i ( Oo0o00OO0000 )
elif o0OO == 1001200 : O0o0O00o0o ( Oo0o00OO0000 )
elif o0OO == 100210 : iI1iiII11I ( Oo0o00OO0000 )
elif o0OO == 100211 : Iiii ( )
elif o0OO == 100212 : i1Ii1 ( )
elif o0OO == 100213 : OoOo00O0o ( )
elif o0OO == 100214 : Oo00OOoO0oo ( )
elif o0OO == 1000111 :
 O0o000 ( Oo0o00OO0000 )
 if 55 - 55: ooOO0O0ooOooO - o0O0Oooo0O / oOOoOooOo % oOo0O0Ooo * ii * oOo0O0Ooo
elif o0OO == 1001111 :
 IiiiI ( iiIiii1IIIII , Oo0o00OO0000 )
 if 88 - 88: Ii1i1i + o0o00Oo0O
elif o0OO == 1002111 :
 o0ooo000o00O ( )
 if 92 - 92: oOo0O0Ooo % IIIIiiII111 % iIII + ii - Ii
elif o0OO == 1003111 :
 iI1i1i ( Oo0o00OO0000 , iiIiii1IIIII )
 if 9 - 9: Ii - IIiIiII11i / oOOoOooOo
elif o0OO == 1004111 :
 oO0ooooooO ( )
 if 81 - 81: Ii % OOooOOo % oO0o * Ii1i1i
elif o0OO == 1005111 :
 I1ii ( Oo0o00OO0000 , iiIiii1IIIII )
elif o0OO == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( Oo0o00OO0000 , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( iiIiii1IIIII , Oo0o00OO0000 , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( iiIiii1IIIII , Oo0o00OO0000 , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1105000 :
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( iiIiii1IIIII , Oo0o00OO0000 , ii1IiIiI1 , ooo0O0o00O , iI1IIiiiI )
elif o0OO == 1106000 :
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiIiii1IIIII = iiIiii1IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( iiIiii1IIIII )
elif o0OO == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( Oo0o00OO0000 )
elif o0OO == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( iiIiii1IIIII )
elif o0OO == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif o0OO == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( Oo0o00OO0000 )
elif o0OO == 1112000 :
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
elif o0OO == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( iiIiii1IIIII , playlist )
elif o0OO == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( Oo0o00OO0000 , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1117000 :
 Oo0o00OO0000 , oo0o0o0o0Ooo = getRegexParsed ( regexs , Oo0o00OO0000 )
 if Oo0o00OO0000 :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( Oo0o00OO0000 , iiIiii1IIIII , ii1IiIiI1 , oo0o0o0o0Ooo )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif o0OO == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 OOO0o00 = youtubedl . single_YD ( Oo0o00OO0000 )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( OOO0o00 , iiIiii1IIIII , ii1IiIiI1 )
elif o0OO == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( Oo0o00OO0000 ) , iiIiii1IIIII , ii1IiIiI1 , True )
elif o0OO == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , iiIiii1IIIII , 'video' )
elif o0OO == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( Oo0o00OO0000 , iiIiii1IIIII , 'video' )
elif o0OO == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( Oo0o00OO0000 , iiIiii1IIIII , 'audio' )
elif o0OO == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1126000 :
 iiIiii1IIIII = iiIiii1IIIII . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( Oo0o00OO0000 , search_term = iiIiii1IIIII [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( Oo0o00OO0000 )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif o0OO == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif o0OO == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif o0OO == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( iiIiii1IIIII , Oo0o00OO0000 , ii1IiIiI1 , ooo0O0o00O )
elif o0OO == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( Oo0o00OO0000 , ii1IiIiI1 , ooo0O0o00O ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( iiIiii1IIIII , Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( Oo0o00OO0000 )
elif o0OO == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( Oo0o00OO0000 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0OO == 9050000 : OOO000 ( )
elif o0OO == 9060000 : IiiiI ( iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 9080000 : III1I1I ( )
elif o0OO == 9070000 : iI1i ( )
elif o0OO == 9090000 : O000oOo ( )
elif o0OO == 9100000 : IIii1 ( )
elif o0OO == 9110000 : IIi11 ( )
elif o0OO == 9110001 : iiI1iIIiI ( Oo0o00OO0000 )
elif o0OO == 9110002 : ooOo0OoO ( Oo0o00OO0000 , iiIiii1IIIII , ii1IiIiI1 )
elif o0OO == 9110003 : O0iI ( iiIiii1IIIII , o00oo0OO0 )
elif o0OO == 9110005 : oo00o0I1IiI ( IiI1IIIII1I , Oo0o00OO0000 )
elif o0OO == 9110004 : oOo ( )
elif o0OO == 9110010 : OO0oOOOOO ( Oo0o00OO0000 )
elif o0OO == 9110011 : iiii1I1IiI ( )
elif o0OO == 9110012 : I11Ii1 ( Oo0o00OO0000 , iiIiii1IIIII )
elif o0OO == 9110013 : i1I11iIII1i1I ( Oo0o00OO0000 )
elif o0OO == 9110014 : o0oooO ( iiIiii1IIIII , Oo0o00OO0000 )
elif o0OO == 9110015 : IIo0OoO00 ( )
elif o0OO == 9999999 : i11iIi1iIIIIi ( )
elif o0OO == 19999999 : o0o00OOOO ( )
elif o0OO == 1999990 : i11i11II11i1 ( )
elif o0OO == 21999990 : i11I ( )
elif o0OO == 21999991 : o00Oo0oooooo ( Oo0o00OO0000 )
elif o0OO == 21999992 : o00o ( Oo0o00OO0000 )
elif o0OO == 21999993 : IIIIiiIiiI ( Oo0o00OO0000 )
elif o0OO == 21999994 : IIIIiI11I11 ( Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 21999995 : oo00o0 ( Oo0o00OO0000 )
elif o0OO == 21999996 : OOoOO0ooo ( Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 21999997 : I11iiii ( Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 21999998 : IiI1iiiIii ( iiIiii1IIIII , Oo0o00OO0000 , ii1IiIiI1 )
elif o0OO == 219999989 : oOooO0 ( )
elif o0OO == 219999990 : iiI ( all = True )
elif o0OO == 219999991 : o0oo00000O ( )
elif o0OO == 219999992 : III1Ii11i1II ( )
if 99 - 99: iIII / OOooOOo % oO0o * Ii1i1i / IIIi11I1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
