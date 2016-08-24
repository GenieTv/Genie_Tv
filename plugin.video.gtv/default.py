# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver , urllib , urllib2 , re
from imports . tvGuide import gui
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = ''
def oo ( i , t1 , t2 = [ ] ) :
 i1iII1IiiIiI1 = o0OO00
 for iIiiiI1IiI1I1 in t1 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 for iIiiiI1IiI1I1 in t2 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 return i1iII1IiiIiI1
 if 87 - 87: OoOoOO00
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
 if 73 - 73: OOooOOo / ii11ii1ii
O00ooOO = "0.0.3"
I1iII1iiII = xbmc . translatePath ( 'special://home/addons/' )
iI1Ii11111iIi = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
i1i1II = 'plugin.video.gtv'
O0oo0OO0 = xbmcaddon . Addon ( id = i1i1II )
I1i1iiI1 = xbmcgui . DialogProgress ( )
iiIIIII1i1iI = "[COLORsteelblue]gtv[/COLOR]"
o0oO0 = xbmcgui . Dialog ( )
oo00 = base64 . decodestring
o00 = O0oo0OO0 . getSetting ( 'User' )
Oo0oO0ooo = O0oo0OO0 . getSetting ( 'Pass' )
o0oOoO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + i1i1II , 'fanart.jpg' ) )
i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + i1i1II , 'icon.png' , ) )
oOOoo00O0O = ( oo00 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUv' ) )
i1111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.gtv/imports/tvGuide/ResetDatabase.py' ) )
i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.gtv/imports/tvGuide/addon.py' ) )
I11 = "gtv"
Oo0o0000o0o0 = ( oo00 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZUFydC9ORVcv' ) )
oOo0oooo00o = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.gtv/' )
oO0o0o0ooO0oO = oOo0oooo00o + 'addons.ini'
if os . path . exists ( oOo0oooo00o ) == False :
 os . makedirs ( oOo0oooo00o )
 if 52 - 52: I1 - OOoOoo00oo - iiI11
def OOooO ( ) :
 OOoO00o ( '[COLORsteelblue]G-Tv PRIVATE LIST[/COLOR]' , '' , 4 , Oo0o0000o0o0 + 'PrivateList.png' , o0oOoO00o , '' )
 II111iiii ( '[COLORsteelblue]TV GUIDE[/COLOR]' , '' , 5 , Oo0o0000o0o0 + 'TvGuide.png' , o0oOoO00o , '' )
 II111iiii ( '[COLORsteelblue]Link GTV Username and Password to Guide[/COLOR]' , '' , 1 , Oo0o0000o0o0 + 'linkchannels.png' , o0oOoO00o , '' )
 if 48 - 48: I1Ii . IiIi1Iii1I1 - O0O0O0O00OooO % Ooooo % i1iIIIiI1I - OOoOoo00oo
def OoO000 ( ) :
 if Oo0oO0ooo == 'insert_password' :
  o0oO0 . ok ( '[COLORsteelblue]G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Purchase @ [COLORsteelblue]http://genietv.co.uk[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  IIiiIiI1 = open ( oO0o0o0ooO0oO )
  iiIiIIi = re . compile ( 'plugin.video.gtv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( IIiiIiI1 ) )
  for ooOoo0O , OooO0 in iiIiIIi :
   if ooOoo0O == 'needs replacing' or OooO0 == 'needs replacing' :
    II11iiii1Ii ( )
  OOoO00o ( '[COLORsteelblue]PRIVATE LIST[/COLOR]' , oOOoo00O0O + '/thelistnew.m3u' , 2 , i1 , o0oOoO00o , '' )
  if 70 - 70: I1 / iIii1I11I1II1 % i1iIIIiI1I % i11iIiiIii . OOOo0
def O0o0Oo ( ) :
 o0oO0 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + i1111 + ")" )
 II11iiii1Ii ( )
 o0oO0 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 78 - 78: iIii1I11I1II1 - I1Ii * Ooo00oOo00o + OOooOOo + IiIi1Iii1I1 + IiIi1Iii1I1
def I11I11i1I ( ) :
 try :
  ii11i1iIII = gui . TVGuide ( )
  ii11i1iIII . doModal ( )
  del ii11i1iIII
  if 3 - 3: i1IIi / OOOo0 % iiI11 * i11iIiiIii / O0 * iiI11
 except :
  import sys
  import traceback as tb
  ( III1ii1iII , oo0oooooO0 , traceback ) = sys . exc_info ( )
  tb . print_exception ( III1ii1iII , oo0oooooO0 , traceback )
  if 19 - 19: iiI11 + i1iIIIiI1I
def ooo ( url ) :
 ii1I1i1I = OOoo0O0 ( url )
 iiIiIIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( ii1I1i1I )
 for iiiIi1i1I , oOO00oOO , url in iiIiIIi :
  url = ( ( oo00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + o00 + '/' + Oo0oO0ooo + url ) . strip ( )
  II111iiii ( ( '[COLORsteelblue]' + oOO00oOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 3 , iiiIi1i1I , '' , '' )
  if 75 - 75: i1IIi / OoooooooOO - O0 / I1IiI . OoOoOO00 - i1IIi
def II11iiii1Ii ( ) :
 O000OO0 = os . path . join ( oO0o0o0ooO0oO )
 I11iii1Ii = open ( O000OO0 , "w+" )
 if 13 - 13: Ooooo % I1IiI - i11iIiiIii . OOOo0 + OoOoOO00
 I11iii1Ii . write ( r'# This file contains the "built-in" channels' + '\n' )
 I11iii1Ii . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 I11iii1Ii . write ( r'[plugin.video.gtv]' + '\n' )
 I11iii1Ii . write ( r'BBC One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F191.m3u8&mode=3&name=[COLORsteelblue]BBC+One%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'BBC Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F190.m3u8&mode=3&name=[COLORsteelblue]BBC+Two%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'BBC Four=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F188.m3u8&mode=3&name=[COLORsteelblue]BBC+Four%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'ITV=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F208.m3u8&mode=3&name=[COLORsteelblue]ITV1%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'ITV2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F207.m3u8&mode=3&name=[COLORsteelblue]ITV2%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'ITV3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F206.m3u8&mode=3&name=[COLORsteelblue]ITV3%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'ITV4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F205.m3u8&mode=3&name=[COLORsteelblue]ITV4%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Channel 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F183.m3u8&mode=3&name=[COLORsteelblue]Channel+4%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Channel 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F185.m3u8&mode=3&name=[COLORsteelblue]Channel+5%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'5STAR=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F187.m3u8&mode=3&name=[COLORsteelblue]5%2A%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'5 USA=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F186.m3u8&mode=3&name=[COLORsteelblue]5USA%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'RTE One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F194.m3u8&mode=3&name=[COLORsteelblue]RTE+One%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'RTE Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F193.m3u8&mode=3&name=[COLORsteelblue]RTE+Two%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'TG4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F192.m3u8&mode=3&name=[COLORsteelblue]TG4%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F32.m3u8&mode=3&name=[COLORsteelblue]Sky+1%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F33.m3u8&mode=3&name=[COLORsteelblue]Sky+2%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Living=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F35.m3u8&mode=3&name=[COLORsteelblue]Sky+Living%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Atlantic=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F34.m3u8&mode=3&name=[COLORsteelblue]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Dave=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F325.m3u8&mode=3&name=[COLORsteelblue]Dave%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Pick=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F324.m3u8&mode=3&name=[COLORsteelblue]Pick%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'GOLD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F326.m3u8&mode=3&name=[COLORsteelblue]Gold%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Watch HD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F518.m3u8&mode=3&name=[COLORsteelblue]Watch%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'YESTERDAY=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F377.m3u8&mode=3&name=[COLORsteelblue]Yesterday%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Comedy Central=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F181.m3u8&mode=3&name=[COLORsteelblue]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'London Live=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F830.m3u8&mode=3&name=[COLORsteelblue]London+Live%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Disney Junior=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F230.m3u8&mode=3&name=[COLORsteelblue]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Disney Chnl=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F231.m3u8&mode=3&name=[COLORsteelblue]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Animal Planet=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F198.m3u8&mode=3&name=[COLORsteelblue]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Nat Geo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F197.m3u8&mode=3&name=[COLORsteelblue]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Discovery=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F200.m3u8&mode=3&name=[COLORsteelblue]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Discovery Science=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F199.m3u8&mode=3&name=[COLORsteelblue]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Disc.Turbo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F168.m3u8&mode=3&name=[COLORsteelblue]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Food Network=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F639.m3u8&mode=3&name=[COLORsteelblue]Food+Network%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'MTV MUSIC=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F234.m3u8&mode=3&name=[COLORsteelblue]MTV+Music%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Film4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F182.m3u8&mode=3&name=[COLORsteelblue]Film4%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'True Movies=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F853.m3u8&mode=3&name=[COLORsteelblue]True+Movies%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'True Movies 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F852.m3u8&mode=3&name=[COLORsteelblue]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Action=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F732.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky ScFiHorror=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F511.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'SkyPremiereHD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F516.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Greats=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F512.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Family=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F509.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky DramaRom=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F510.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Thriller=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F514.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Comedy=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F513.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Showcase=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F46.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Select=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F45.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Disney=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F195.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Sports 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F18.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Sports 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F19.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Sports 3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F20.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Sports 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F21.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Sports 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F22.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Sports F1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F24.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Sky Sports News=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F23.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'BT Sport 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F309.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'BT Sport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F26.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'BT Sport Europe=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F705.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'BT Sport ESPN=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F28.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Box Nation=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F173.m3u8&mode=3&name=[COLORsteelblue]Box+Nation%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'WWENetwork=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F178.m3u8&mode=3&name=[COLORsteelblue]WWENetwork%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Eurosport=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F269.m3u8&mode=3&name=[COLORsteelblue]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Eurosport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F748.m3u8&mode=3&name=[COLORsteelblue]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'At The Races=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F170.m3u8&mode=3&name=[COLORsteelblue]At+the+Races%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Racing UK=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F171.m3u8&mode=3&name=[COLORsteelblue]Racing+UK%0D[%2FCOLOR]' + '\n' )
 I11iii1Ii . write ( r'Poker central US=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F826.m3u8&mode=3&name=[COLORsteelblue]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 10 - 10: ii11ii1ii * i1iIIIiI1I * OoOoOO00 % I1Ii . OOoOoo00oo + Ooooo
def IIiIi11i1 ( url ) :
 IIIii1II1II = xbmc . Player ( i1I1iI ( ) )
 import urlresolver
 try : IIIii1II1II . play ( url )
 except : pass
 if 93 - 93: iIii1I11I1II1 % I1 * i1IIi
 if 16 - 16: O0 - Ooooo * iIii1I11I1II1 + IiIi1Iii1I1
def i1I1iI ( ) :
 try :
  Ii11iII1 = getSet ( "core-player" )
  if ( Ii11iII1 == 'DVDPLAYER' ) : Oo0O0O0ooO0O = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( Ii11iII1 == 'MPLAYER' ) : Oo0O0O0ooO0O = xbmc . PLAYER_CORE_MPLAYER
  elif ( Ii11iII1 == 'PAPLAYER' ) : Oo0O0O0ooO0O = xbmc . PLAYER_CORE_PAPLAYER
  else : Oo0O0O0ooO0O = xbmc . PLAYER_CORE_AUTO
 except : Oo0O0O0ooO0O = xbmc . PLAYER_CORE_AUTO
 return Oo0O0O0ooO0O
 return True
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / OOoOoo00oo
def OOoo0O0 ( url ) :
 oo000OO00Oo = urllib2 . Request ( url )
 oo000OO00Oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0OOO0OOoO0O = urllib2 . urlopen ( oo000OO00Oo )
 O00Oo000ooO0 = O0OOO0OOoO0O . read ( )
 O0OOO0OOoO0O . close ( )
 return O00Oo000ooO0
 if 100 - 100: O0 + O0O0O0O00OooO - OOoOoo00oo + i11iIiiIii * I1Ii
 if 30 - 30: OOooOOo . I1Ii - OoooooooOO
 if 8 - 8: i1IIi - iIii1I11I1II1 * OoOoOO00 + i11iIiiIii / Ooooo % OOoOoo00oo
 if 16 - 16: ii11ii1ii + Ooo00oOo00o - OoOoOO00
 if 85 - 85: I1IiI + i1IIi
 if 58 - 58: OoOoOO00 * OOoOoo00oo * ii11ii1ii / OOoOoo00oo
def oO0o0OOOO ( heading , announce ) :
 class O0O0OoOO0 ( ) :
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
   try : iiiI1I11i1 = open ( announce ) ; IIi1i11111 = iiiI1I11i1 . read ( )
   except : IIi1i11111 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IIi1i11111 ) )
   return
 O0O0OoOO0 ( )
 O0O0OoOO0 ( )
 if 81 - 81: i11iIiiIii % I1IiI - OOoOoo00oo
def OOoO00o ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0ooo0O0oo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oOo = True
 o000O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o000O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o000O0o . setProperty ( "Fanart_Image" , fanart )
 oo0oOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooo0O0oo0 , listitem = o000O0o , isFolder = True )
 return oo0oOo
 if 42 - 42: I1IiI
def II111iiii ( name , url , mode , iconimage , fanart , description ) :
 O0ooo0O0oo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oOo = True
 o000O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o000O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o000O0o . setProperty ( "Fanart_Image" , fanart )
 oo0oOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooo0O0oo0 , listitem = o000O0o , isFolder = False )
 return oo0oOo
 if 41 - 41: Oo . i1iIIIiI1I + O0 * OOooOOo % Oo * Oo
def iIIIIi1iiIi1 ( ) :
 iii1i1iiiiIi = [ ]
 Iiii = sys . argv [ 2 ]
 if len ( Iiii ) >= 2 :
  OO0OoO0o00 = sys . argv [ 2 ]
  ooOO0O0ooOooO = OO0OoO0o00 . replace ( '?' , '' )
  if ( OO0OoO0o00 [ len ( OO0OoO0o00 ) - 1 ] == '/' ) :
   OO0OoO0o00 = OO0OoO0o00 [ 0 : len ( OO0OoO0o00 ) - 2 ]
  oOOOo00O00oOo = ooOO0O0ooOooO . split ( '&' )
  iii1i1iiiiIi = { }
  for iiIIIi in range ( len ( oOOOo00O00oOo ) ) :
   ooo00OOOooO = { }
   ooo00OOOooO = oOOOo00O00oOo [ iiIIIi ] . split ( '=' )
   if ( len ( ooo00OOOooO ) ) == 2 :
    iii1i1iiiiIi [ ooo00OOOooO [ 0 ] ] = ooo00OOOooO [ 1 ]
    if 67 - 67: iiI11 * I1 * ii11ii1ii + OOoOoo00oo / i1IIi
 return iii1i1iiiiIi
OO0OoO0o00 = iIIIIi1iiIi1 ( )
I1I111 = None
oOO00oOO = None
Oo00oo0oO = None
IIiIi1iI = None
i1IiiiI1iI = None
i1iIi = None
ooOOoooooo = None
if 1 - 1: Oo / OOooOOo % IiIi1Iii1I1 * O0O0O0O00OooO . i11iIiiIii
if 2 - 2: ii11ii1ii * iiI11 - iIii1I11I1II1 + OOOo0 . I1 % IiIi1Iii1I1
try :
 ooOOoooooo = int ( OO0OoO0o00 [ "fav_mode" ] )
except :
 pass
 if 92 - 92: IiIi1Iii1I1
try :
 I1I111 = urllib . unquote_plus ( OO0OoO0o00 [ "url" ] )
except :
 pass
try :
 oOO00oOO = urllib . unquote_plus ( OO0OoO0o00 [ "name" ] )
except :
 pass
try :
 IIiIi1iI = urllib . unquote_plus ( OO0OoO0o00 [ "iconimage" ] )
except :
 pass
try :
 Oo00oo0oO = int ( OO0OoO0o00 [ "mode" ] )
except :
 pass
try :
 i1IiiiI1iI = urllib . unquote_plus ( OO0OoO0o00 [ "fanart" ] )
except :
 pass
try :
 i1iIi = urllib . unquote_plus ( OO0OoO0o00 [ "description" ] )
except :
 pass
 if 25 - 25: Oo - OOOo0 / OoooooooOO / OOooOOo
 if 12 - 12: OOOo0 * IiIi1Iii1I1 % i1IIi % iIii1I11I1II1
print str ( I11 ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( Oo00oo0oO )
print "URL: " + str ( I1I111 )
print "Name: " + str ( oOO00oOO )
print "IconImage: " + str ( IIiIi1iI )
if 20 - 20: OOoOoo00oo % I1Ii / I1Ii + I1Ii
if 45 - 45: I1 - O0O0O0O00OooO - OoooooooOO - Ooo00oOo00o . OoOoOO00 / O0
def oo0o00O ( content , viewType ) :
 if 51 - 51: I1Ii - Ooo00oOo00o * IiIi1Iii1I1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 66 - 66: OoooooooOO + O0
  if 11 - 11: iiI11 + OoooooooOO - Ooo00oOo00o / OOooOOo + Oo . OoOoOO00
if Oo00oo0oO == None : OOooO ( )
elif Oo00oo0oO == 1 : O0o0Oo ( )
elif Oo00oo0oO == 2 : ooo ( I1I111 )
elif Oo00oo0oO == 3 : IIiIi11i1 ( I1I111 )
elif Oo00oo0oO == 4 : OoO000 ( )
elif Oo00oo0oO == 5 : xbmc . executebuiltin ( "XBMC.RunScript(" + i11 + ")" )
if 41 - 41: I1Ii - O0 - O0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
