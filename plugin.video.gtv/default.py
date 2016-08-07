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
O00ooOO = "0.0.1"
I1iII1iiII = xbmc . translatePath ( 'special://home/addons/' )
iI1Ii11111iIi = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
i1i1II = 'plugin.video.gtv'
O0oo0OO0 = xbmcaddon . Addon ( id = i1i1II )
I1i1iiI1 = xbmcgui . DialogProgress ( )
iiIIIII1i1iI = "[COLORgreen]gtv[/COLOR]"
o0oO0 = xbmcgui . Dialog ( )
oo00 = base64 . decodestring
o00 = O0oo0OO0 . getSetting ( 'User' )
Oo0oO0ooo = O0oo0OO0 . getSetting ( 'Pass' )
o0oOoO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + i1i1II , 'fanart.jpg' ) )
i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + i1i1II , 'icon.png' , ) )
oOOoo00O0O = ( oo00 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUv' ) )
i1111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.gtv/imports/tvGuide/ResetDatabase.py' ) )
i11 = "gtv"
I11 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.gtv/' )
Oo0o0000o0o0 = I11 + 'addons.ini'
if os . path . exists ( I11 ) == False :
 os . makedirs ( I11 )
 if 86 - 86: iiiii11iII1 % O0o
def oO0 ( ) :
 IIIi1i1I ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 4 , i1 , o0oOoO00o , '' )
 OOoOoo00oo ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 5 , i1 , o0oOoO00o , '' )
 OOoOoo00oo ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 1 , i1 , o0oOoO00o , '' )
 if 41 - 41: i11IiIiiIIIII / IiiIII111ii / i1iIIi1
def ii11iIi1I ( ) :
 if Oo0oO0ooo == 'insert_password' :
  o0oO0 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  iI111I11I1I1 = open ( Oo0o0000o0o0 )
  OOooO0OOoo = re . compile ( 'plugin.video.gtv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iI111I11I1I1 ) )
  for iIii1 , oOOoO0 in OOooO0OOoo :
   if iIii1 == 'needs replacing' or oOOoO0 == 'needs replacing' :
    O0OoO000O0OO ( )
  IIIi1i1I ( '[COLORgreen]DONATORS LIST[/COLOR]' , oOOoo00O0O + '/thelistnew.m3u' , 2 , i1 , o0oOoO00o , '' )
  if 23 - 23: iIiIiIiIIi + ooOoo0O
def OooO0 ( ) :
 o0oO0 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + i1111 + ")" )
 O0OoO000O0OO ( )
 o0oO0 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 35 - 35: Ooooo0Oo00oO0 % i1iIIi1 . iIii1I11I1II1 * i11iIiiIii
def II1i1Ii11Ii11 ( ) :
 try :
  iII11i = gui . TVGuide ( )
  iII11i . doModal ( )
  del iII11i
  if 97 - 97: i11IiIiiIIIII % i11IiIiiIIIII + OoOoOO00 * i1iIIi1
 except :
  import sys
  import traceback as tb
  ( o0o00o0 , iIi1ii1I1 , traceback ) = sys . exc_info ( )
  tb . print_exception ( o0o00o0 , iIi1ii1I1 , traceback )
  if 71 - 71: ooOoo0O . O0
def o0OO0oo0oOO ( url ) :
 oo0oooooO0 = i11Iiii ( url )
 OOooO0OOoo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo0oooooO0 )
 for iI , I1i1I1II , url in OOooO0OOoo :
  url = ( ( oo00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + o00 + '/' + Oo0oO0ooo + url ) . strip ( )
  OOoOoo00oo ( ( '[COLORgreen]' + I1i1I1II + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 3 , iI , '' , '' )
  if 45 - 45: ooOoo0O . I1IiI
def O0OoO000O0OO ( ) :
 oO = os . path . join ( Oo0o0000o0o0 )
 ii1i1I1i = open ( oO , "w+" )
 if 53 - 53: iIiIiIiIIi + OOOo0 * iiiii11iII1
 ii1i1I1i . write ( r'# This file contains the "built-in" channels' + '\n' )
 ii1i1I1i . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 ii1i1I1i . write ( r'[plugin.video.gtv]' + '\n' )
 ii1i1I1i . write ( r'BBC One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F191.m3u8&mode=3&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'BBC Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F190.m3u8&mode=3&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'BBC Four=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F188.m3u8&mode=3&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'ITV=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F208.m3u8&mode=3&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'ITV2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F207.m3u8&mode=3&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'ITV3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F206.m3u8&mode=3&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'ITV4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F205.m3u8&mode=3&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Channel 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F183.m3u8&mode=3&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Channel 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F185.m3u8&mode=3&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'5STAR=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F187.m3u8&mode=3&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'5 USA=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F186.m3u8&mode=3&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'RTE One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F194.m3u8&mode=3&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'RTE Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F193.m3u8&mode=3&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'TG4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F192.m3u8&mode=3&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F32.m3u8&mode=3&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F33.m3u8&mode=3&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Living=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F35.m3u8&mode=3&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Atlantic=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F34.m3u8&mode=3&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Dave=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F325.m3u8&mode=3&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Pick=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F324.m3u8&mode=3&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'GOLD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F326.m3u8&mode=3&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Watch HD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F518.m3u8&mode=3&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'YESTERDAY=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F377.m3u8&mode=3&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Comedy Central=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F181.m3u8&mode=3&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'London Live=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F830.m3u8&mode=3&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Disney Junior=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F230.m3u8&mode=3&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Disney Chnl=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F231.m3u8&mode=3&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Animal Planet=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F198.m3u8&mode=3&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Nat Geo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F197.m3u8&mode=3&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Discovery=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F200.m3u8&mode=3&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Discovery Science=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F199.m3u8&mode=3&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Disc.Turbo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F168.m3u8&mode=3&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Food Network=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F639.m3u8&mode=3&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'MTV MUSIC=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F234.m3u8&mode=3&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Film4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F182.m3u8&mode=3&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'True Movies=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F853.m3u8&mode=3&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'True Movies 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F852.m3u8&mode=3&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Action=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F732.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky ScFiHorror=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F511.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'SkyPremiereHD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F516.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Greats=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F512.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Family=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F509.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky DramaRom=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F510.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Thriller=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F514.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Comedy=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F513.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Showcase=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F46.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Select=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F45.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Disney=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F195.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Sports 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F18.m3u8&mode=3&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Sports 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F19.m3u8&mode=3&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Sports 3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F20.m3u8&mode=3&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Sports 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F21.m3u8&mode=3&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Sports 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F22.m3u8&mode=3&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Sports F1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F24.m3u8&mode=3&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Sky Sports News=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F23.m3u8&mode=3&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'BT Sport 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F309.m3u8&mode=3&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'BT Sport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F26.m3u8&mode=3&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'BT Sport Europe=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F705.m3u8&mode=3&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'BT Sport ESPN=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F28.m3u8&mode=3&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Box Nation=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F173.m3u8&mode=3&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'WWENetwork=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F178.m3u8&mode=3&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Eurosport=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F269.m3u8&mode=3&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Eurosport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F748.m3u8&mode=3&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'At The Races=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F170.m3u8&mode=3&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Racing UK=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F171.m3u8&mode=3&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 ii1i1I1i . write ( r'Poker central US=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F826.m3u8&mode=3&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 61 - 61: i1IIi * O0o / OoooooooOO . i11iIiiIii . I1IiI
def o00O ( url ) :
 OOO0OOO00oo = xbmc . Player ( Iii111II ( ) )
 import urlresolver
 try : OOO0OOO00oo . play ( url )
 except : pass
 if 9 - 9: Ooo00oOo00o
 if 33 - 33: Ooooo0Oo00oO0 . i1iIIi1
def Iii111II ( ) :
 try :
  O0oo0OO0oOOOo = getSet ( "core-player" )
  if ( O0oo0OO0oOOOo == 'DVDPLAYER' ) : i1i1i11IIi = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0oo0OO0oOOOo == 'MPLAYER' ) : i1i1i11IIi = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0oo0OO0oOOOo == 'PAPLAYER' ) : i1i1i11IIi = xbmc . PLAYER_CORE_PAPLAYER
  else : i1i1i11IIi = xbmc . PLAYER_CORE_AUTO
 except : i1i1i11IIi = xbmc . PLAYER_CORE_AUTO
 return i1i1i11IIi
 return True
 if 33 - 33: OOooOOo + O0o * Ooo00oOo00o - Oo / iiiii11iII1 % IiiIII111ii
def i11Iiii ( url ) :
 II1i1IiiIIi11 = urllib2 . Request ( url )
 II1i1IiiIIi11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iI1Ii11iII1 = urllib2 . urlopen ( II1i1IiiIIi11 )
 Oo0O0O0ooO0O = iI1Ii11iII1 . read ( )
 iI1Ii11iII1 . close ( )
 return Oo0O0O0ooO0O
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / O0o
 if 58 - 58: i11iIiiIii % i11IiIiiIIIII
 if 71 - 71: O0o + Ooooo0Oo00oO0 % i11iIiiIii + ii11ii1ii - iIiIiIiIIi
 if 88 - 88: I1IiI - Ooo00oOo00o % O0o
 if 16 - 16: OOOo0 * iiiii11iII1 % iIiIiIiIIi
 if 86 - 86: OOOo0 + IiiIII111ii % i11iIiiIii * iiiii11iII1 . Ooooo0Oo00oO0 * i11IiIiiIIIII
def i1I11i1iI ( heading , announce ) :
 class I1ii1Ii1 ( ) :
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
   try : iii11 = open ( announce ) ; oOOOOo0 = iii11 . read ( )
   except : oOOOOo0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOOOOo0 ) )
   return
 I1ii1Ii1 ( )
 I1ii1Ii1 ( )
 if 20 - 20: i1IIi + ii11ii1ii - Ooooo0Oo00oO0
def IIIi1i1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 IiI11iII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII11I1I = True
 OOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO0o . setProperty ( "Fanart_Image" , fanart )
 IIII11I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI11iII1 , listitem = OOO0o , isFolder = True )
 return IIII11I1I
 if 30 - 30: iIii1I11I1II1 / Ooooo0Oo00oO0 - ooOoo0O - OoOoOO00 % i1iIIi1
def OOoOoo00oo ( name , url , mode , iconimage , fanart , description ) :
 IiI11iII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII11I1I = True
 OOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO0o . setProperty ( "Fanart_Image" , fanart )
 IIII11I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiI11iII1 , listitem = OOO0o , isFolder = False )
 return IIII11I1I
 if 49 - 49: OOOo0 % Ooooo0Oo00oO0 . Ooooo0Oo00oO0 . i11IiIiiIIIII * Ooooo0Oo00oO0
def O0oOO0 ( ) :
 O0ooo0O0oo0 = [ ]
 oo0oOo = sys . argv [ 2 ]
 if len ( oo0oOo ) >= 2 :
  o000O0o = sys . argv [ 2 ]
  iI1iII1 = o000O0o . replace ( '?' , '' )
  if ( o000O0o [ len ( o000O0o ) - 1 ] == '/' ) :
   o000O0o = o000O0o [ 0 : len ( o000O0o ) - 2 ]
  oO0OOoo0OO = iI1iII1 . split ( '&' )
  O0ooo0O0oo0 = { }
  for O0ii1ii1ii in range ( len ( oO0OOoo0OO ) ) :
   oooooOoo0ooo = { }
   oooooOoo0ooo = oO0OOoo0OO [ O0ii1ii1ii ] . split ( '=' )
   if ( len ( oooooOoo0ooo ) ) == 2 :
    O0ooo0O0oo0 [ oooooOoo0ooo [ 0 ] ] = oooooOoo0ooo [ 1 ]
    if 6 - 6: i11IiIiiIIIII - IiiIII111ii + iIii1I11I1II1 - ooOoo0O - i11iIiiIii
 return O0ooo0O0oo0
o000O0o = O0oOO0 ( )
OO0oOO0O = None
I1i1I1II = None
oOiIi1IIIi1 = None
O0oOoOOOoOO = None
ii1ii11IIIiiI = None
O00OOOoOoo0O = None
O000OOo00oo = None
if 71 - 71: i11iIiiIii + iIiIiIiIIi
if 57 - 57: iiiii11iII1 . i11IiIiiIIIII . i1IIi
try :
 O000OOo00oo = int ( o000O0o [ "fav_mode" ] )
except :
 pass
 if 42 - 42: i11IiIiiIIIII + ii11ii1ii % O0
try :
 OO0oOO0O = urllib . unquote_plus ( o000O0o [ "url" ] )
except :
 pass
try :
 I1i1I1II = urllib . unquote_plus ( o000O0o [ "name" ] )
except :
 pass
try :
 O0oOoOOOoOO = urllib . unquote_plus ( o000O0o [ "iconimage" ] )
except :
 pass
try :
 oOiIi1IIIi1 = int ( o000O0o [ "mode" ] )
except :
 pass
try :
 ii1ii11IIIiiI = urllib . unquote_plus ( o000O0o [ "fanart" ] )
except :
 pass
try :
 O00OOOoOoo0O = urllib . unquote_plus ( o000O0o [ "description" ] )
except :
 pass
 if 6 - 6: iiiii11iII1
 if 68 - 68: I1IiI - Ooo00oOo00o
print str ( i11 ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( oOiIi1IIIi1 )
print "URL: " + str ( OO0oOO0O )
print "Name: " + str ( I1i1I1II )
print "IconImage: " + str ( O0oOoOOOoOO )
if 28 - 28: Ooo00oOo00o . O0o / O0o + Oo . ii11ii1ii
if 1 - 1: iIii1I11I1II1 / OoOoOO00
def iiI1I11i1i ( content , viewType ) :
 if 2 - 2: ii11ii1ii * i11IiIiiIIIII - iIii1I11I1II1 + OOOo0 . iiiii11iII1 % i1iIIi1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 92 - 92: i1iIIi1
  if 25 - 25: Oo - OOOo0 / OoooooooOO / OOooOOo
if oOiIi1IIIi1 == None : oO0 ( )
elif oOiIi1IIIi1 == 1 : OooO0 ( )
elif oOiIi1IIIi1 == 2 : o0OO0oo0oOO ( OO0oOO0O )
elif oOiIi1IIIi1 == 3 : o00O ( OO0oOO0O )
elif oOiIi1IIIi1 == 4 : ii11iIi1I ( )
elif oOiIi1IIIi1 == 5 : II1i1Ii11Ii11 ( )
if 12 - 12: OOOo0 * i1iIIi1 % i1IIi % iIii1I11I1II1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
