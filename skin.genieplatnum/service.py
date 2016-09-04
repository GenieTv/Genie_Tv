oo000 = ''
def ii ( i , t1 , t2 = [ ] ) :
 oOOo = oo000
 for O0 in t1 :
  oOOo += chr ( O0 )
  i += 1
  if i > 1 :
   oOOo = oOOo [ : - 1 ]
   i = 0
 for O0 in t2 :
  oOOo += chr ( O0 )
  i += 1
  if i > 1 :
   oOOo = oOOo [ : - 1 ]
   i = 0
 return oOOo
 if 70 - 70: oo0 . O0OO0O0O - oooo
import xbmc , xbmcaddon , xbmcgui , os
if 11 - 11: ii1I - ooO0OO000o
if 4 - 4: IiII1IiiIiI1 / iIiiiI1IiI1I1
def o0OoOoOO00 ( setting , value ) :
 setting = '"%s"' % setting
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
 if isinstance ( value , list ) :
  o0OOO = ''
  for iIiiiI in value :
   o0OOO += '"%s",' % str ( iIiiiI )
   if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
  o0OOO = o0OOO [ : - 1 ]
  o0OOO = '[%s]' % o0OOO
  value = o0OOO
  if 68 - 68: o00ooo0 / Oo00O0
 elif not isinstance ( value , int ) :
  value = '"%s"' % value
  if 66 - 66: o0oooOoO0
 II11i = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":%s,"value":%s}, "id":1}' % ( setting , value )
 xbmc . executeJSONRPC ( II11i )
 if 43 - 43: oO0o0ooO0 . i11iII1iiI
def IIii11I1 ( setting ) :
 if 59 - 59: oooo
 import json
 setting = '"%s"' % setting
 if 31 - 31: o00ooo0 % ooO0OO000o * oooo / o00ooo0 % i11iII1iiI + ii1I
 II11i = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":%s}, "id":1}' % ( setting )
 O00o0o0000o0o = xbmc . executeJSONRPC ( II11i )
 if 88 - 88: iiIIIII1i1iI / iIiiiI1IiI1I1 + ooO0OO000o % ii1I . o00ooo0 / o0oooOoO0
 O00o0o0000o0o = json . loads ( O00o0o0000o0o )
 if 28 - 28: o0oooOoO0 + Oo00O0 - o0oooOoO0 . ii1I
 if O00o0o0000o0o . has_key ( 'result' ) :
  if O00o0o0000o0o [ 'result' ] . has_key ( 'value' ) :
   return O00o0o0000o0o [ 'result' ] [ 'value' ]
   if 97 - 97: Oo . ii1II11I1ii1I
   if 32 - 32: OOOo0 - IiII1IiiIiI1 - oo0 % Oo00O0
O0OoOoo00o = 'lookandfeel.skin'
iiiI11 = IIii11I1 ( O0OoOoo00o )
if 91 - 91: I1IiI / IiII1IiiIiI1 . iii1II11ii + iI1Ii11111iIi
if iiiI11 == 'skin.genieplatnum' :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'userdata' , 'addon_data' , '.flag' ) )
 if ( os . path . isfile ( iI11 ) ) :
  pass
 else :
  import os
  import re
  import time
  import extract
  xbmc . executebuiltin ( 'Notification([COLOR limegreen]GenieTV[/COLOR],[COLOR yellow]Please wait ten seconds...[/COLOR],10000)' )
  time . sleep ( 5 )
  iII111ii = xbmc . translatePath ( os . path . join ( 'special://home' ) )
  i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://xbmc' , 'addons' , 'skin.genieplatnum' , 'resources' , 'GenieTv.zip' ) )
  extract . all ( i1iIIi1 , iII111ii )
  ii11iIi1I = xbmc . translatePath ( os . path . join ( 'special://xbmc' , 'addons' , 'skin.genieplatnum' , 'resources' , 'bools.txt' ) )
  iI111I11I1I1 = open ( ii11iIi1I ) . read ( )
  OOooO0OOoo = re . compile ( 'bool="(.+?)"' ) . findall ( iI111I11I1I1 )
  for iIii1 in OOooO0OOoo : xbmc . executebuiltin ( 'Skin.SetBool(%s)' % iIii1 )
  time . sleep ( 2 )
  oOOoO0 = xbmc . translatePath ( os . path . join ( 'special://xbmc' , 'addons' , 'skin.genieplatnum' , 'resources' , 'strings.txt' ) )
  O0OoO000O0OO = open ( oOOoO0 ) . read ( )
  iiI1IiI = re . compile ( 'string="(.+?)"' ) . findall ( O0OoO000O0OO )
  for II in iiI1IiI : xbmc . executebuiltin ( 'Skin.SetString(%s)' % II )
  time . sleep ( 2 )
  xbmc . executebuiltin ( 'Skin.Setbool(FirstTimeRun)' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateAddonRepos()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateLocalAddons()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( ii ( 0 , [ 82 , 21 , 117 , 108 , 110 , 206 , 65 , 15 , 100 , 180 , 100 , 133 , 111 , 181 , 110 , 97 , 40 , 208 , 112 , 119 , 108 ] , [ 55 , 117 , 56 , 103 , 8 , 105 , 42 , 110 , 105 , 46 , 96 , 118 , 24 , 105 , 136 , 100 , 110 , 101 , 135 , 111 , 0 , 46 , 161 , 65 , 174 , 110 , 206 , 100 , 116 , 114 , 124 , 111 , 195 , 105 , 167 , 100 , 216 , 66 , 213 , 114 , 139 , 111 , 191 , 115 , 61 , 87 , 248 , 105 , 222 , 122 , 205 , 97 , 244 , 114 , 168 , 100 , 57 , 41 ] ) )
  if 57 - 57: i11iII1iiI
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
