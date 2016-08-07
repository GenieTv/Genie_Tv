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
O00ooOO = "0.0.2"
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
i11 = "gtv"
I11 = ( oo00 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZUFydC9ORVcv' ) )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.gtv/' )
oOo0oooo00o = Oo0o0000o0o0 + 'addons.ini'
if os . path . exists ( Oo0o0000o0o0 ) == False :
 os . makedirs ( Oo0o0000o0o0 )
 if 65 - 65: O0o * i1iIIII * I1
def O0OoOoo00o ( ) :
 iiiI11 ( '[COLORsteelblue]G-Tv PRIVATE LIST[/COLOR]' , '' , 4 , I11 + 'PrivateList.png' , o0oOoO00o , '' )
 OOooO ( '[COLORsteelblue]TV GUIDE[/COLOR]' , '' , 5 , I11 + 'TvGuide.png' , o0oOoO00o , '' )
 OOooO ( '[COLORsteelblue]Link GTV Username and Password to Guide[/COLOR]' , '' , 1 , I11 + 'linkchannels.png' , o0oOoO00o , '' )
 if 58 - 58: i11iiII + OooooO0oOO + oOo0 / oo0Ooo0
def I1I11I1I1I ( ) :
 if Oo0oO0ooo == 'insert_password' :
  o0oO0 . ok ( '[COLORsteelblue]G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Purchase @ [COLORsteelblue]http://genietv.co.uk[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  OooO0OO = open ( oOo0oooo00o )
  iiiIi = re . compile ( 'plugin.video.gtv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OooO0OO ) )
  for IiIIIiI1I1 , OoO000 in iiiIi :
   if IiIIIiI1I1 == 'needs replacing' or OoO000 == 'needs replacing' :
    IIiiIiI1 ( )
  iiiI11 ( '[COLORsteelblue]PRIVATE LIST[/COLOR]' , oOOoo00O0O + '/thelistnew.m3u' , 2 , i1 , o0oOoO00o , '' )
  if 41 - 41: iiIIiIiIi
def i1I11 ( ) :
 o0oO0 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + i1111 + ")" )
 IIiiIiI1 ( )
 o0oO0 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 26 - 26: i11iIiiIii
def OO0O00 ( ) :
 try :
  ii1 = gui . TVGuide ( )
  ii1 . doModal ( )
  del ii1
  if 57 - 57: i11iiII % OoooooooOO
 except :
  import sys
  import traceback as tb
  ( O00 , i11I1 , traceback ) = sys . exc_info ( )
  tb . print_exception ( O00 , i11I1 , traceback )
  if 8 - 8: iIii1I11I1II1 - oOo0 % iIii1I11I1II1 - i11iiII * OOOo0
def iI11i1I1 ( url ) :
 o0o0OOO0o0 = ooOOOo0oo0O0 ( url )
 iiiIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0o0OOO0o0 )
 for o0 , I11II1i , url in iiiIi :
  url = ( ( oo00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + o00 + '/' + Oo0oO0ooo + url ) . strip ( )
  OOooO ( ( '[COLORsteelblue]' + I11II1i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 3 , o0 , '' , '' )
  if 23 - 23: ii11ii1ii / OOooOOo + I1 + I1 / OoOoOO00
def IIiiIiI1 ( ) :
 iiI1 = os . path . join ( oOo0oooo00o )
 i11Iiii = open ( iiI1 , "w+" )
 if 23 - 23: OOooOOo . OoOoOO00
 i11Iiii . write ( r'# This file contains the "built-in" channels' + '\n' )
 i11Iiii . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 i11Iiii . write ( r'[plugin.video.gtv]' + '\n' )
 i11Iiii . write ( r'BBC One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F191.m3u8&mode=3&name=[COLORsteelblue]BBC+One%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'BBC Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F190.m3u8&mode=3&name=[COLORsteelblue]BBC+Two%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'BBC Four=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F188.m3u8&mode=3&name=[COLORsteelblue]BBC+Four%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'ITV=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F208.m3u8&mode=3&name=[COLORsteelblue]ITV1%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'ITV2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F207.m3u8&mode=3&name=[COLORsteelblue]ITV2%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'ITV3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F206.m3u8&mode=3&name=[COLORsteelblue]ITV3%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'ITV4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F205.m3u8&mode=3&name=[COLORsteelblue]ITV4%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Channel 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F183.m3u8&mode=3&name=[COLORsteelblue]Channel+4%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Channel 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F185.m3u8&mode=3&name=[COLORsteelblue]Channel+5%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'5STAR=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F187.m3u8&mode=3&name=[COLORsteelblue]5%2A%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'5 USA=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F186.m3u8&mode=3&name=[COLORsteelblue]5USA%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'RTE One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F194.m3u8&mode=3&name=[COLORsteelblue]RTE+One%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'RTE Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F193.m3u8&mode=3&name=[COLORsteelblue]RTE+Two%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'TG4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F192.m3u8&mode=3&name=[COLORsteelblue]TG4%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F32.m3u8&mode=3&name=[COLORsteelblue]Sky+1%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F33.m3u8&mode=3&name=[COLORsteelblue]Sky+2%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Living=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F35.m3u8&mode=3&name=[COLORsteelblue]Sky+Living%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Atlantic=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F34.m3u8&mode=3&name=[COLORsteelblue]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Dave=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F325.m3u8&mode=3&name=[COLORsteelblue]Dave%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Pick=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F324.m3u8&mode=3&name=[COLORsteelblue]Pick%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'GOLD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F326.m3u8&mode=3&name=[COLORsteelblue]Gold%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Watch HD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F518.m3u8&mode=3&name=[COLORsteelblue]Watch%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'YESTERDAY=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F377.m3u8&mode=3&name=[COLORsteelblue]Yesterday%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Comedy Central=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F181.m3u8&mode=3&name=[COLORsteelblue]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'London Live=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F830.m3u8&mode=3&name=[COLORsteelblue]London+Live%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Disney Junior=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F230.m3u8&mode=3&name=[COLORsteelblue]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Disney Chnl=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F231.m3u8&mode=3&name=[COLORsteelblue]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Animal Planet=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F198.m3u8&mode=3&name=[COLORsteelblue]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Nat Geo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F197.m3u8&mode=3&name=[COLORsteelblue]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Discovery=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F200.m3u8&mode=3&name=[COLORsteelblue]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Discovery Science=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F199.m3u8&mode=3&name=[COLORsteelblue]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Disc.Turbo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F168.m3u8&mode=3&name=[COLORsteelblue]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Food Network=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F639.m3u8&mode=3&name=[COLORsteelblue]Food+Network%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'MTV MUSIC=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F234.m3u8&mode=3&name=[COLORsteelblue]MTV+Music%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Film4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F182.m3u8&mode=3&name=[COLORsteelblue]Film4%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'True Movies=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F853.m3u8&mode=3&name=[COLORsteelblue]True+Movies%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'True Movies 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F852.m3u8&mode=3&name=[COLORsteelblue]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Action=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F732.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky ScFiHorror=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F511.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'SkyPremiereHD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F516.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Greats=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F512.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Family=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F509.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky DramaRom=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F510.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Thriller=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F514.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Comedy=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F513.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Showcase=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F46.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Select=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F45.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Disney=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F195.m3u8&mode=3&name=[COLORsteelblue]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Sports 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F18.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Sports 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F19.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Sports 3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F20.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Sports 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F21.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Sports 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F22.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Sports F1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F24.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Sky Sports News=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F23.m3u8&mode=3&name=[COLORsteelblue]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'BT Sport 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F309.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'BT Sport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F26.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'BT Sport Europe=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F705.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'BT Sport ESPN=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F28.m3u8&mode=3&name=[COLORsteelblue]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Box Nation=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F173.m3u8&mode=3&name=[COLORsteelblue]Box+Nation%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'WWENetwork=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F178.m3u8&mode=3&name=[COLORsteelblue]WWENetwork%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Eurosport=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F269.m3u8&mode=3&name=[COLORsteelblue]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Eurosport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F748.m3u8&mode=3&name=[COLORsteelblue]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'At The Races=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F170.m3u8&mode=3&name=[COLORsteelblue]At+the+Races%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Racing UK=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F171.m3u8&mode=3&name=[COLORsteelblue]Racing+UK%0D[%2FCOLOR]' + '\n' )
 i11Iiii . write ( r'Poker central US=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + o00 + '%2F' + Oo0oO0ooo + '%2F826.m3u8&mode=3&name=[COLORsteelblue]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 98 - 98: iIii1I11I1II1 % I1IiI * ii11ii1ii * I1IiI
def i1IiIiiI ( url ) :
 I1I = xbmc . Player ( oOO00oOO ( ) )
 import urlresolver
 try : I1I . play ( url )
 except : pass
 if 75 - 75: i1IIi / OoooooooOO - O0 / I1IiI . OoOoOO00 - i1IIi
 if 71 - 71: i1iIIII + i11iiII * i1iIIII - Ooo00oOo00o * OOooOOo
def oOO00oOO ( ) :
 try :
  Oooo0Ooo000 = getSet ( "core-player" )
  if ( Oooo0Ooo000 == 'DVDPLAYER' ) : ooii11I = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( Oooo0Ooo000 == 'MPLAYER' ) : ooii11I = xbmc . PLAYER_CORE_MPLAYER
  elif ( Oooo0Ooo000 == 'PAPLAYER' ) : ooii11I = xbmc . PLAYER_CORE_PAPLAYER
  else : ooii11I = xbmc . PLAYER_CORE_AUTO
 except : ooii11I = xbmc . PLAYER_CORE_AUTO
 return ooii11I
 return True
 if 96 - 96: OoOoOO00 % i11iiII . i1iIIII + OoooooooOO * O0o - I1IiI
def ooOOOo0oo0O0 ( url ) :
 i11i1 = urllib2 . Request ( url )
 i11i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 IIIii1II1II = urllib2 . urlopen ( i11i1 )
 i1I1iI = IIIii1II1II . read ( )
 IIIii1II1II . close ( )
 return i1I1iI
 if 93 - 93: iIii1I11I1II1 % O0o * i1IIi
 if 16 - 16: O0 - oo0Ooo0 * iIii1I11I1II1 + OooooO0oOO
 if 50 - 50: OoOoOO00 - iiIIiIiIi * ii11ii1ii / oo0Ooo0 + OOooOOo
 if 88 - 88: i11iiII / oo0Ooo0 + OooooO0oOO - OoOoOO00 / iiIIiIiIi - I1IiI
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / i1iIIII
 if 58 - 58: i11iIiiIii % I1
def OO00Oo ( heading , announce ) :
 class O0OOO0OOoO0O ( ) :
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
   try : O00Oo000ooO0 = open ( announce ) ; OoO0O00 = O00Oo000ooO0 . read ( )
   except : OoO0O00 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OoO0O00 ) )
   return
 O0OOO0OOoO0O ( )
 O0OOO0OOoO0O ( )
 if 5 - 5: Oo / OOooOOo . i11iiII - O0 / oOo0
def iiiI11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 ooOooo000oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo0oOOo = True
 Oo0OoO00oOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0OoO00oOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0OoO00oOO0o . setProperty ( "Fanart_Image" , fanart )
 Oo0oOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooOooo000oOO , listitem = Oo0OoO00oOO0o , isFolder = True )
 return Oo0oOOo
 if 80 - 80: O0o + i1iIIII - i1iIIII % OooooO0oOO
def OOooO ( name , url , mode , iconimage , fanart , description ) :
 ooOooo000oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo0oOOo = True
 Oo0OoO00oOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0OoO00oOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0OoO00oOO0o . setProperty ( "Fanart_Image" , fanart )
 Oo0oOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooOooo000oOO , listitem = Oo0OoO00oOO0o , isFolder = False )
 return Oo0oOOo
 if 63 - 63: OOOo0 - ii11ii1ii + O0 % I1 / iIii1I11I1II1 / OOooOOo
def O0o0O00Oo0o0 ( ) :
 O00O0oOO00O00 = [ ]
 i1Oo00 = sys . argv [ 2 ]
 if len ( i1Oo00 ) >= 2 :
  i1i = sys . argv [ 2 ]
  iiI111I1iIiI = i1i . replace ( '?' , '' )
  if ( i1i [ len ( i1i ) - 1 ] == '/' ) :
   i1i = i1i [ 0 : len ( i1i ) - 2 ]
  II = iiI111I1iIiI . split ( '&' )
  O00O0oOO00O00 = { }
  for Ii1I1IIii1II in range ( len ( II ) ) :
   O0ii1ii1ii = { }
   O0ii1ii1ii = II [ Ii1I1IIii1II ] . split ( '=' )
   if ( len ( O0ii1ii1ii ) ) == 2 :
    O00O0oOO00O00 [ O0ii1ii1ii [ 0 ] ] = O0ii1ii1ii [ 1 ]
    if 91 - 91: oOo0
 return O00O0oOO00O00
i1i = O0o0O00Oo0o0 ( )
iiIii = None
I11II1i = None
ooo0O = None
oOoO0o00OO0 = None
i1I1ii = None
oOOo0 = None
oo00O00oO = None
if 23 - 23: Ooo00oOo00o + Ooo00oOo00o . i1iIIII
if 38 - 38: oo0Ooo0
try :
 oo00O00oO = int ( i1i [ "fav_mode" ] )
except :
 pass
 if 7 - 7: O0 . OooooO0oOO % ii11ii1ii - OOOo0 - iIii1I11I1II1
try :
 iiIii = urllib . unquote_plus ( i1i [ "url" ] )
except :
 pass
try :
 I11II1i = urllib . unquote_plus ( i1i [ "name" ] )
except :
 pass
try :
 oOoO0o00OO0 = urllib . unquote_plus ( i1i [ "iconimage" ] )
except :
 pass
try :
 ooo0O = int ( i1i [ "mode" ] )
except :
 pass
try :
 i1I1ii = urllib . unquote_plus ( i1i [ "fanart" ] )
except :
 pass
try :
 oOOo0 = urllib . unquote_plus ( i1i [ "description" ] )
except :
 pass
 if 36 - 36: oOo0 % iiIIiIiIi % Oo - ii11ii1ii
 if 22 - 22: iIii1I11I1II1 / Oo * ii11ii1ii % OooooO0oOO
print str ( i11 ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( ooo0O )
print "URL: " + str ( iiIii )
print "Name: " + str ( I11II1i )
print "IconImage: " + str ( oOoO0o00OO0 )
if 85 - 85: O0o % i11iIiiIii - OooooO0oOO * OoooooooOO / OOOo0 % OOOo0
if 1 - 1: Ooo00oOo00o - O0o . I1 . Ooo00oOo00o / Oo + I1
def Ooo ( content , viewType ) :
 if 62 - 62: i1iIIII / Ooo00oOo00o + i11iiII / Ooo00oOo00o . OoOoOO00
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 68 - 68: i11iIiiIii % ii11ii1ii + i11iIiiIii
  if 31 - 31: OoOoOO00 . OOOo0
if ooo0O == None : O0OoOoo00o ( )
elif ooo0O == 1 : i1I11 ( )
elif ooo0O == 2 : iI11i1I1 ( iiIii )
elif ooo0O == 3 : i1IiIiiI ( iiIii )
elif ooo0O == 4 : I1I11I1I1I ( )
elif ooo0O == 5 : OO0O00 ( )
if 1 - 1: Oo / OOooOOo % OooooO0oOO * oOo0 . i11iIiiIii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
