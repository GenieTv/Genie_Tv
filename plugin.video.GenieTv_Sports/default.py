# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
import extract
import downloader
from imports import cloudflare
from imports import yt
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from datetime import date , datetime , timedelta
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
IiII1IiiIiI1 = 'plugin.video.GenieTv_Sports'
iIiiiI1IiI1I1 = 'plugin.video.GenieTv_Sports'
o0OoOoOO00 = "0.0.2"
I11i = xbmc . translatePath ( 'special://home/addons/' )
O0O = base64 . decodestring
Oo = datetime . now ( )
I1ii11iIi11i = xbmc . translatePath ( 'special://logpath/' )
I1IiI = xbmc . translatePath ( 'special://home/addonsbroke/' )
o0OOO = xbmcaddon . Addon ( id = iIiiiI1IiI1I1 )
iIiiiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
Iii1ii1II11i = 'plugin.video.GenieTv_Sports'
iI111iI = xbmcgui . DialogProgress ( )
IiII = "GenieTv Sports"
iI1Ii11111iIi = Net ( )
i1i1II = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv_Sports' )
O0oo0OO0 = xbmc . translatePath ( 'special://home/' )
O0O = base64 . decodestring
I1i1iiI1 = xbmc . translatePath ( 'special://profile/' )
iiIIIII1i1iI = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
o0oO0 = os . path . join ( O0oo0OO0 , 'userdata' )
oo00 = os . path . join ( o0oO0 , 'addon_data' , IiII1IiiIiI1 )
o00 = os . path . join ( I11i , 'packages' )
Oo0oO0ooo = O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ2VuaWVzcG9ydHMv' )
o0oOoO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'icon.png' ) )
i1 = Oo0oO0ooo + ( O0O ( 'YXJ0Lw==' ) )
oOOoo00O0O = 'http://genietv.co.uk'
i1111 = os . path . join ( oo00 , 'wizard.log' )
i11 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTv_Sports' )
I11 = xbmc . translatePath ( 'special://thumbnails' ) ;
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'fanart.jpg' ) )
oOo0oooo00o = o0OOO . getLocalizedString
oO0o0o0ooO0oO = CookieJar ( )
oo0o0O00 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( oO0o0o0ooO0oO ) )
oo0o0O00 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
oO = int ( sys . argv [ 1 ] )
i1iiIIiiI111 = xbmc . translatePath ( o0OOO . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
o0oO0 = xbmc . translatePath ( 'special://home/userdata/' )
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
i1iiIII111ii = i11 + '/addons.ini'
i1iIIi1 = xbmcgui . Dialog ( )
ii11iIi1I = xbmcgui . Dialog ( )
if os . path . exists ( oooOOOOO ) == True :
 iI111I11I1I1 = open ( oooOOOOO ) . read ( )
else : iI111I11I1I1 = [ ]
if 55 - 55: iI1I % iiiIi - OO / i1I111I - I1I1IIiiIiI1 . iiIiIIi
if 65 - 65: iii1I1
if 84 - 84: III1I11iiii1I . IiI1i11iii1
def oo0Oo00Oo0 ( ) :
 oOOO00o ( '[COLORorangered]Live Streams[/COLOR]' , O0O ( 'aHR0cDovL2F1dG9pcHR2Lm5ldC9wYWdlcy9wbGF5bGlzdHMv' ) , 300000002 , i1 + 'live.jpg' , Oo0o0000o0o0 , '[COLORorangered]Live Streams[/COLOR]' )
 oOOO00o ( '[COLORorangered]Live Events[/COLOR]' , '' , 31 , i1 + 'live_events.jpg' , Oo0o0000o0o0 , '[COLORorangered]Match Time Only[CR]SportsDevil Required[CR]VPN May Help Certain Links[/COLOR]' )
 oOOO00o ( '[COLORorangered]Replays[/COLOR]' , Oo0oO0ooo , 40 , i1 + 'replays.jpg' , Oo0o0000o0o0 , '[COLORorangered]Replays[/COLOR]' )
 oOOO00o ( '[COLORorangered]Fact Files[/COLOR]' , Oo0oO0ooo , 30 , i1 + 'factfiles.jpg' , Oo0o0000o0o0 , '[COLORorangered]Fact Files[/COLOR]' )
 oOOO00o ( '[COLORorangered]Club Teams[/COLOR]' , Oo0oO0ooo , 1010 , i1 + 'factfiles.jpg' , Oo0o0000o0o0 , '[COLORorangered]Club Teams [CR]YouTube Channels[/COLOR]' )
 if 97 - 97: o0o0OOO0o0 % IIII % o0O0 . o0
def I11II1i ( ) :
 oOOO00o ( '[COLORorangered]Celtic FC[/COLOR]' , Oo0oO0ooo , 1006 , 'https://vignette.wikia.nocookie.net/fifa/images/a/a8/Celtic_FC.png/revision/latest?cb=20180213000259' , Oo0o0000o0o0 , '[COLORorangered]Celtic FC[/COLOR]' )
 oOOO00o ( '[COLORorangered]Rangers[/COLOR]' , Oo0oO0ooo , 1007 , 'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Rangers_FC.svg/1200px-Rangers_FC.svg.png' , Oo0o0000o0o0 , '[COLORorangered]Rangers[/COLOR]' )
def IIIII ( ) :
 oOOO00o ( '[COLORorangered]Rangers[/COLOR]' , Oo0oO0ooo , 1008 , 'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Rangers_FC.svg/1200px-Rangers_FC.svg.png' , Oo0o0000o0o0 , '[COLORorangered]Rangers[/COLOR]' )
 if 75 - 75: iii % I1I1IIiiIiI1
def oO00 ( ) :
 oOOO00o ( '[COLORgreen]Celtic FC Youtube[/COLOR]' , '' , 1000 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Celtic FC Youtube[/COLOR]' )
 oOOO00o ( '[COLORgreen]PLZ Soccer[/COLOR]' , '' , 1001 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]PLZ Soccer[/COLOR]' )
 oOOO00o ( '[COLORgreen]Podcasts[/COLOR]' , '' , 1002 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Podcasts[/COLOR]' )
 oOOO00o ( '[COLORgreen]Rebel Tunes[/COLOR]' , '' , 1003 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Rebel Tunes[/COLOR]' )
 oOOO00o ( '[COLORgreen]Green Brigade[/COLOR]' , '' , 1004 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Green Brigade[/COLOR]' )
 if 53 - 53: OoooooooOO . i1IIi
def ii1I1i1I ( ) :
 oOOO00o ( '[COLORorangered]Extreme Sports[/COLOR]' , 'http://www.ridersmatch.com/' , 20 , i1 + 'extreme.jpg' , Oo0o0000o0o0 , '[COLORorangered]Extreme Sports[/COLOR]' )
 OOoo0O0 = iiiIi1i1I ( Oo0oO0ooo + O0O ( 'VHJvamFuLnBocA==' ) )
 oOO00oOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoo0O0 )
 for OoOo , iI , o00O , OOO0OOO00oo , Iii111II in oOO00oOO :
  iI = ( O0O ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9wbGV4L2Rvd25sb2Fkcy9TUE9SVFMuQ0FUQ0hVUC8=' ) + O0O ( iI ) )
  oOOO00o ( '[COLORorangered]' + Iii111II + '[/COLOR]' , ( Oo0oO0ooo + O0O ( OoOo ) ) , 41 , iI , iI , '[COLORorangered]' + Iii111II + '[/COLOR]' )
def iiii11I ( url ) :
 OOoo0O0 = iiiIi1i1I ( url )
 oOO00oOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoo0O0 )
 for url , iI , o00O , OOO0OOO00oo , Iii111II in oOO00oOO :
  if '.php' in url :
   oOOO00o ( '[COLORorangered]' + Iii111II + '[/COLOR]' , url , 41 , iI , Oo0o0000o0o0 , '[COLORorangered]' + o00O + '[/COLOR]' )
  else :
   Ooo0OO0oOO ( '[COLORorangered]' + Iii111II + '[/COLOR]' , url , 15 , iI , Oo0o0000o0o0 , '[COLORorangered]' + o00O + '[/COLOR]' )
def ii11i1 ( ) :
 oOOO00o ( '[COLORorangered]Highlights[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]Highlights[/COLOR]' )
 oOOO00o ( '[COLORorangered]Latest Results[/COLOR]' , '' , 33 , i1 + 'latest_results.jpg' , Oo0o0000o0o0 , '[COLORorangered]Latest Results[/COLOR]' )
 oOOO00o ( '[COLORorangered]Top Goal Scorers[/COLOR]' , '' , 32 , i1 + 'top_scorers.jpg' , Oo0o0000o0o0 , '[COLORorangered]Top Goal Scorers[/COLOR]' )
 if 29 - 29: iiIiIIi % iI1I + iii / I1I1IIiiIiI1 + III1I11iiii1I * I1I1IIiiIiI1
def i1I1iI ( ) :
 oo0OooOOo0 = iiiIi1i1I ( 'http://www.eplsite.com/fetchdata_toptenscorer.php' )
 o0O = re . compile ( '"Topscorer"(.+?)"AccountInformation"' , re . DOTALL ) . findall ( oo0OooOOo0 )
 O00oO = re . compile ( '{"Rank":"([^"]*)","Name":"([^"]*)","TeamName":"([^"]*)","Team_Id":"([^"]*)","Nationality":"([^"]*)","Goals":"([^"]*)","FirstScorer":"([^"]*)","Penalties":"([^"]*)","MissedPenalties":"([^"]*)"}' , re . DOTALL ) . findall ( str ( o0O ) )
 for I11i1I1I , oO0Oo , oOOoo0Oo , o00OO00OoO , OOOO0OOoO0O0 , O0Oo000ooO00 , oO0 , Ii1iIiII1ii1 , ooOooo000oOO in O00oO :
  Oo0oOOo = 'Rank: ' + I11i1I1I + '[CR]Name: ' + oO0Oo + '[CR]TeamName: ' + oOOoo0Oo + '[CR]Team Id: ' + o00OO00OoO + '[CR]Nationality: ' + OOOO0OOoO0O0 + '[CR]Goals: ' + O0Oo000ooO00 + '[CR]FirstScorer: ' + oO0 + '[CR]Penalties: ' + Ii1iIiII1ii1 + '[CR]MissedPenalties: ' + ooOooo000oOO + '\n'
  Ooo0OO0oOO ( '[COLORorangered]' + oO0Oo + '[/COLOR]' , '' , '' , i1 + 'top_scorers.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + Oo0oOOo + '[/COLOR]' )
  if 58 - 58: II111iiii * III1I11iiii1I * iiIiIIi / III1I11iiii1I
def oO0o0OOOO ( ) :
 oo0OooOOo0 = iiiIi1i1I ( 'http://eplsite.com/fetchdata_liveresult.php' )
 o0O = re . compile ( '"Match"(.+?)"AccountInformation"' , re . DOTALL ) . findall ( oo0OooOOo0 )
 O00oO = re . compile ( '{"Id":(.+?),"FixtureMatch_Id":(.+?),"Date":(.+?),"Round":(.+?),"Spectators":(.+?),"League":(.+?),"HomeTeam":(.+?),"HomeTeam_Id":(.+?),"HomeCorners":(.+?),"HomeGoals":(.+?),"HalfTimeHomeGoals":(.+?),"HomeShots":(.+?),"HomeShotsOnTarget":(.+?),"HomeFouls":(.+?),"HomeGoalDetails":(.+?),"HomeLineupGoalkeeper":(.+?),"HomeLineupDefense":(.+?),"HomeLineupMidfield":(.+?),"HomeLineupForward":(.+?),"HomeLineUpSubstitutes":(.+?),"HomeLineUpCoach":(.+?),"HomeYellowCards":(.+?),"HomeRedCards":(.+?),"HomeTeamFormation":(.+?),"AwayTeam":(.+?),"AwayTeam_Id":(.+?),"AwayCorners":(.+?),"AwayGoals":(.+?),"HalfTimeAwayGoals":(.+?),"AwayShots":(.+?),"AwayShotsOnTarget":(.+?),"AwayFouls":(.+?),"AwayGoalDetails":(.+?),"AwayLineupGoalkeeper":(.+?),"AwayLineupDefense":(.+?),"AwayLineupMidfield":(.+?),"AwayLineupForward":(.+?),"AwayLineUpSubstitutes":(.+?),"AwayLineUpCoach":(.+?),"AwayYellowCards":(.+?),"AwayRedCards":(.+?),"AwayTeamFormation":(.+?),"HomeTeamYellowCardDetails":(.+?),"AwayTeamYellowCardDetails":(.+?),"HomeTeamRedCardDetails":(.+?),"AwayTeamRedCardDetails":(.+?),"HomeSubDetails":(.+?),"AwaySubDetails":(.+?),"Referee":"(.+?)"}' , re . DOTALL ) . findall ( str ( o0O ) )
 for O0O0OoOO0 , iiiI1I11i1 , IIi1i11111 , ooOO00O00oo , I1ii11iI , IIi1i , I1I1iIiII1 , i11i1I1 , ii1I , Oo0ooOo0o , Ii1i1 , iiIii , ooo0O , oOoO0o00OO0 , i1I1ii , oOOo0 , oo00O00oO , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo , oo0OOo , ooOOO00Ooo , IiIIIi1iIi , ooOOoooooo , II1I , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo , o0O0OOO0Ooo , iiIiI , I1 , OOO00O0O , iiioOooOOOoOo , i1Iii1i1I , OOoO00 , IiI111111IIII , i1Ii , ii111iI1iIi1 , OOO , oo0OOo0 , I11IiI , O0ooO0Oo00o , ooO0oOOooOo0 , i1I1ii11i1Iii , I1IiiiiI , o0OIiII , ii1iII1II , Iii1I1I11iiI1 in O00oO :
  Oo0oOOo = 'Date: ' + IIi1i11111 + '[CR]HomeTeam: ' + I1I1iIiII1 + '[CR]HomeGoals: ' + Oo0ooOo0o + '[CR]AwayTeam: ' + ooOOoooooo + '[CR]AwayGoals: ' + IIIIiiIiI + '[CR]Round: ' + ooOO00O00oo + '[CR]Spectators: ' + I1ii11iI + '[CR]League: ' + IIi1i + '[CR]HomeCorners: ' + ii1I + '[CR]HalfTimeHomeGoals: ' + Ii1i1 + '[CR]HomeShots: ' + iiIii + '[CR]HomeShotsOnTarget: ' + ooo0O + '[CR]HomeFouls: ' + oOoO0o00OO0 + '[CR]HomeGoalDetails: ' + i1I1ii + '[CR]HomeLineupGoalkeeper: ' + oOOo0 + '[CR]HomeLineupDefense: ' + oo00O00oO + '[CR]HomeLineupMidfield: ' + iIiIIIi + '[CR]HomeLineupForward: ' + ooo00OOOooO + '[CR]HomeLineUpSubstitutes: ' + O00OOOoOoo0O + '[CR]HomeLineUpCoach: ' + O000OOo00oo + '[CR]HomeYellowCards: ' + oo0OOo + '[CR]HomeRedCards: ' + ooOOO00Ooo + '[CR]HomeTeamFormation: ' + IiIIIi1iIi + '[CR]AwayCorners: ' + O0i1II1Iiii1I11 + '[CR]HalfTimeAwayGoals: ' + o00oooO0Oo + '[CR]AwayShots: ' + o0O0OOO0Ooo + '[CR]AwayShotsOnTarget: ' + iiIiI + '[CR]AwayFouls: ' + I1 + '[CR]AwayGoalDetails: ' + OOO00O0O + '[CR]AwayLineupGoalkeeper: ' + iiioOooOOOoOo + '[CR]AwayLineupDefense: ' + i1Iii1i1I + '[CR]AwayLineupMidfield: ' + OOoO00 + '[CR]AwayLineupForward: ' + IiI111111IIII + '[CR]AwayLineUpSubstitutes: ' + i1Ii + '[CR]AwayLineUpCoach: ' + ii111iI1iIi1 + '[CR]AwayYellowCards: ' + OOO + '[CR]AwayRedCards: ' + oo0OOo0 + '[CR]AwayTeamFormation: ' + I11IiI + '[CR]HomeTeamYellowCardDetails: ' + O0ooO0Oo00o + '[CR]AwayTeamYellowCardDetails: ' + ooO0oOOooOo0 + '[CR]HomeTeamRedCardDetails: ' + i1I1ii11i1Iii + '[CR]AwayTeamRedCardDetails: ' + I1IiiiiI + '[CR]HomeSubDetails: ' + o0OIiII + '[CR]AwaySubDetails: ' + ii1iII1II + '[CR]Referee: ' + Iii1I1I11iiI1 + '\n'
  Ooo0OO0oOO ( ( '[COLORorangered]' + I1I1iIiII1 + '[COLORsteelblue] Vs [COLORorangered]' + ooOOoooooo + '[COLORsteelblue] ' + Oo0ooOo0o + ':' + IIIIiiIiI + '[/COLOR]' ) . replace ( '"' , '' ) , '' , 34 , i1 + 'match_stats.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( Oo0oOOo ) . replace ( '{}' , 'N/A' ) . replace ( '\\' , '' ) . replace ( "'" , '' ) . replace ( '"' , '' ) + '[/COLOR]' )
def I1I1i1I ( name , description ) :
 name = name
 o00O = description
 ii1IO0oO0 ( name , o00O )
 if 87 - 87: iiiIi . o0O0
 if 75 - 75: iii + i1I111I + I1I1IIiiIiI1 * IiI1i11iii1 % iii1I1 . IIII
def oOI1Ii1I1 ( ) :
 IiII111iI1ii1 = [ '[COLORsteelblue]FootBall Source 1[/COLOR]' , '[COLORsteelblue]FootBall Source 2[/COLOR]' , '[COLORsteelblue]FootBall Source 3[/COLOR]' , '[COLORsteelblue]F1[/COLOR]' , '[COLORsteelblue]NFL[/COLOR]' ]
 iI11I1II = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Select Source[/COLOR]' , IiII111iI1ii1 )
 if iI11I1II == 0 :
  Ii1I ( )
 if iI11I1II == 1 :
  IiI1i ( )
 if iI11I1II == 2 :
  o0Oo00 ( )
 if iI11I1II == 3 :
  iIO0O0Oooo0o ( )
 if iI11I1II == 4 :
  oOOoo00O00o ( )
  if 98 - 98: III1I11iiii1I + o0O0 + iii1I1 % OoooooooOO
def Ii1I ( ) :
 Ooo0OO0oOO ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 oo0OooOOo0 = iiiIi1i1I ( 'http://www.eplsite.com/' )
 o0O = re . compile ( '<h4>FOOTBALL LIVE STREAMS</h4>(.+?)</section>' , re . DOTALL ) . findall ( oo0OooOOo0 )
 O00oO = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="vs  "><span>(.+?)</span><div class="accordion-time">(.+?)</div></div>.+?<div class="acoordian-right-section">(.+?)</div>.+?<p>(.+?)</p>.+?<p>(.+?)</p>(.+?)<center>' , re . DOTALL ) . findall ( str ( o0O ) )
 for oooooo0O000o , OoO , time , ooO0O0O0ooOOO , oOOo0O00o , Iii111II , iIiIi11 in O00oO :
  OOOiiiiI = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( iIiIi11 ) )
  Ooo0OO0oOO ( '[COLORorangered]' + ( oOOo0O00o ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOo0O00o ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  Ooo0OO0oOO ( '[COLORorangered]' + '' + oooooo0O000o + ' ' + OoO + ' ' + ooO0O0O0ooOOO + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( Iii111II ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for iI , OoOo , oooOo0OOOoo0 in OOOiiiiI :
   OOoO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OoOo
   Ooo0OO0oOO ( '[COLORsteelblue]' + oooOo0OOOoo0 + '[/COLOR]' , OOoO , 15 , 'http://www.eplsite.com/' + iI , Oo0o0000o0o0 , '[COLORsteelblue]' + oooOo0OOOoo0 + '[/COLOR]' )
   if 89 - 89: I1I1IIiiIiI1 + OO * IiI1i11iii1 * o0o0OOO0o0
def IiI1i ( ) :
 Ooo0OO0oOO ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 oo0OooOOo0 = iiiIi1i1I ( 'http://www.abcast.me/' )
 o0O = re . compile ( '</thead>(.+?)</html>' , re . DOTALL ) . findall ( oo0OooOOo0 )
 O00oO = re . compile ( '<td> (.+?) </td>.+?</strong>.+?<td>(.+?)</td>.+?href="(.+?)">' , re . DOTALL ) . findall ( str ( o0O ) )
 for oOOo0O00o , Iii111II , OoOo in O00oO :
  OOoO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OoOo
  Ooo0OO0oOO ( '[COLORorangered]' + oOOo0O00o + '[COLORsteelblue]' + Iii111II + '[/COLOR]' , OOoO , 15 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + oOOo0O00o + '[COLORsteelblue]' + Iii111II + '[/COLOR]' )
  if 37 - 37: OoooooooOO - O0 - I1I1IIiiIiI1
def o0Oo00 ( ) :
 Ooo0OO0oOO ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 oo0OooOOo0 = iiiIi1i1I ( 'http://www.sports-stream.net/schedule.html' )
 o0o0O0O00oOOo = re . compile ( '<font color="red"><h3>(.+?)<input onclick=(.+?)<br>' , re . DOTALL ) . findall ( oo0OooOOo0 )
 for iIIIiIi , iIiIi11 in o0o0O0O00oOOo :
  O00oO = re . compile ( 'style="color:#FF0000;">(.+?)</span>(.+?) - <a href="(.+?)" ' , re . DOTALL ) . findall ( str ( iIiIi11 ) )
  Ooo0OO0oOO ( '[COLORorangered]' + ( iIIIiIi ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( iIIIiIi ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for time , Iii111II , OoOo in O00oO :
   OOoO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OoOo
   Ooo0OO0oOO ( '[COLORorangered]' + time + '[COLORsteelblue]' + Iii111II + '[/COLOR]' , OOoO , 15 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + time + '[COLORsteelblue]' + Iii111II + '[/COLOR]' )
   if 100 - 100: iI1I / I1I1IIiiIiI1 % II111iiii % iiiIi % III1I11iiii1I
   if 98 - 98: IiI1i11iii1 % i11iIiiIii % iii + o0o0OOO0o0
def iIO0O0Oooo0o ( ) :
 Ooo0OO0oOO ( '[COLORorangered]Race Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 oo0OooOOo0 = iiiIi1i1I ( 'http://www.eplsite.com/f1.html' )
 o0O = re . compile ( '<h4>F1 Live Streams</h4>(.+?)</section>' , re . DOTALL ) . findall ( oo0OooOOo0 )
 O00oO = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="accordion-time">(.+?)</div></div>.+?<p>(.+?)</p>(.+?)</header>' , re . DOTALL ) . findall ( str ( o0O ) )
 for oooooo0O000o , time , Iii111II , iIiIi11 in O00oO :
  OOOiiiiI = re . compile ( '<a href="(.+?)".+?target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( iIiIi11 ) )
  Ooo0OO0oOO ( '[COLORorangered]' + ( oooooo0O000o ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oooooo0O000o ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  Ooo0OO0oOO ( '[COLORorangered]' + '' + Iii111II + '[/COLOR]' , '' , '' , i1 + 'f1.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( Iii111II ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for OoOo , oooOo0OOOoo0 in OOOiiiiI :
   OOoO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OoOo
   if 'bitcoin' in OoOo :
    pass
   else :
    Ooo0OO0oOO ( '[COLORsteelblue]' + oooOo0OOOoo0 + '[/COLOR]' , OOoO , 15 , i1 + 'f1.jpg' , Oo0o0000o0o0 , '[COLORsteelblue]' + oooOo0OOOoo0 + '[/COLOR]' )
    if 78 - 78: iiIiIIi % iii1I1 / IIII - iIii1I11I1II1
def oOOoo00O00o ( ) :
 Ooo0OO0oOO ( '[COLORorangered]Game Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 oo0OooOOo0 = iiiIi1i1I ( 'http://www.eplsite.com/nfl.html' )
 o0O = re . compile ( '<h4>NFL Live Streams</h4>(.+?)</section>' , re . DOTALL ) . findall ( oo0OooOOo0 )
 O00oO = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="vs"><span>(.+?)</span><div class="accordion-time">(.+?)</div></div>.+?<div class="acoordian-right-section">(.+?)</div>.+?<p>(.+?)</p>(.+?)</b></p>' , re . DOTALL ) . findall ( str ( o0O ) )
 for oooooo0O000o , OoO , time , ooO0O0O0ooOOO , Iii111II , iIiIi11 in O00oO :
  OOOiiiiI = re . compile ( '<a href="(.+?)".+?target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( iIiIi11 ) )
  Ooo0OO0oOO ( '[COLORorangered]' + '' + oooooo0O000o + ' ' + OoO + ' ' + ooO0O0O0ooOOO + '[/COLOR]' , '' , '' , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( Iii111II ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  Ooo0OO0oOO ( '[COLORorangered]' + '' + Iii111II + '[/COLOR]' , '' , '' , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( Iii111II ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for OoOo , oooOo0OOOoo0 in OOOiiiiI :
   OOoO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OoOo
   if 'bitcoin' in OoOo :
    pass
   else :
    Ooo0OO0oOO ( '[COLORsteelblue]' + oooOo0OOOoo0 + '[/COLOR]' , OOoO , 15 , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORsteelblue]' + oooOo0OOOoo0 + '[/COLOR]' )
    if 69 - 69: o0
def ii1I1 ( ) :
 OooooOOoo0 = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 oo0OooOOo0 = requests . get ( OoOo ) . content
 O00oO = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( oo0OooOOo0 )
 o0O = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( O00oO ) )
 for i1I1IiiIi1i , Iii111II in o0O :
  if not Iii111II == 'Home' :
   pass
   iiI11ii1I1 = 'http://www.replaymatches.com/' + i1I1IiiIi1i
   if Iii111II in OooooOOoo0 :
    oOOO00o ( '[COLORred]' + Iii111II + '[/COLOR]' , iiI11ii1I1 , 900301 , i1 + 'football.jpg' , '' , '' )
   else :
    oOOO00o ( '[COLORorangered]' + Iii111II + '[/COLOR]' , iiI11ii1I1 , 900301 , i1 + 'football.jpg' , '' , '' )
    if 82 - 82: II111iiii % IiI1i11iii1 / OO + i1I111I / I1I1IIiiIiI1 / o0
def oOo0OOoO0 ( url ) :
 if 11 - 11: iiIiIIi . OO * o0O0 * OoooooooOO + iii
 OOoo0O0 = iiiIi1i1I ( url )
 IiII111i1i11 = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( OOoo0O0 )
 i111iIi1i1II1 = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( OOoo0O0 )
 for url , Iii111II , iI in IiII111i1i11 :
  oOOO00o ( '[COLORorangered]' + Iii111II + '[/COLOR]' , url , 900302 , iI , i1 + 'football.jpg' , '' )
 for oooO in i111iIi1i1II1 :
  oOOO00o ( '[COLORorangered]NEXT PAGE[/COLOR]' , oooO , 900301 , i1 + 'NEXT.png' , '' , '' )
def i1I1i111Ii ( url ) :
 oo0OooOOo0 = requests . get ( url ) . content
 O00oO = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 )
 for i1I1IiiIi1i , iI in O00oO :
  if 'Highlight' in iI :
   Iii111II = 'HighLights'
  elif '1st' in iI :
   Iii111II = '1st Half'
  elif '2nd' in iI :
   Iii111II = '2nd Half'
  else :
   Iii111II = 'Full Match'
  ooo ( '[COLORorangered]' + Iii111II + '[/COLOR]' , i1I1IiiIi1i , 1001111 , iI , i1 + 'football.jpg' , '' , '' )
def i1i1iI1iiiI ( ) :
 oo0OooOOo0 = requests . get ( O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 O00oO = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( oo0OooOOo0 )
 for Ooo0oOooo0 , iIiIi11 in O00oO :
  oOOOoo00 ( '[COLORred]' + Ooo0oOooo0 + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , i1 + 'football.jpg' , '' , '' )
  iiIiIIIiiI = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( iIiIi11 ) )
  for iiI1IIIi , II11IiIi11 in iiIiIIIiiI :
   oOOOoo00 ( '[COLORorangered]' + iiI1IIIi + '[/COLOR]' , '' , '' , II11IiIi11 , i1 + 'football.jpg' , '' , '' )
def II ( name , url ) :
 import urlresolver
 try :
  OOO0O00O0OOOO = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( OOO0O00O0OOOO , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 18 - 18: IiI1i11iii1 - i11iIiiIii / II111iiii . III1I11iiii1I
 if 55 - 55: i1IIi % II111iiii + IiI1i11iii1 * iIii1I11I1II1
def o0ooooO0o0O ( url ) :
 OOoo0O0 = iiiIi1i1I ( url )
 oOO00oOO = re . compile ( '<span class="title">(.+?)</span>.+?<a class="no-style" href="([^"]*)"' , re . DOTALL ) . findall ( OOoo0O0 )
 for Iii111II , url in oOO00oOO :
  if 'Sport' in Iii111II :
   iiIi11iI1iii ( url )
def oo000 ( url ) :
 if url == 'http://' : return False
 try :
  o0000oO = urllib2 . Request ( url )
  o0000oO . add_header ( 'User-Agent' , iIiiiI )
  iI1i111I1Ii = urllib2 . urlopen ( o0000oO )
  iI1i111I1Ii . close ( )
 except Exception , i11i1ii1I :
  return i11i1ii1I
 return True
def o0OO0o0o00o ( name , url ) :
 if 100 - 100: iii1I1 / o0 / iiIiIIi
 if 78 - 78: iiiIi - I1I1IIiiIiI1 / i1I111I
 if 10 - 10: IIII + iiiIi * iiIiIIi + iIii1I11I1II1 / o0 / iiIiIIi
 if 42 - 42: iI1I
 if 38 - 38: III1I11iiii1I + II111iiii % iii % i1I111I - o0o0OOO0o0 / OoooooooOO
 oOOoo0000O0o0 = name
 OOoo0O0 = iiiIi1i1I ( url )
 O00oO = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 OOOiiiiI = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 II1III = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 III1 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 OooooO0oOOOO = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( OOoo0O0 )
 o0O00oOOoo = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 for name , iI , i1I1iIi , oooOo0OOOoo0 , url in O00oO :
  if oOOoo0000O0o0 in i1I1iIi :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( name + oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , iI , iI , ( '[COLORsteelblue]' + ( name + oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iI , i1I1iIi , oooOo0OOOoo0 , url in OOOiiiiI :
  if oOOoo0000O0o0 in i1I1iIi :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , iI , iI , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for i1I1iIi , oooOo0OOOoo0 , url in II1III :
  if oOOoo0000O0o0 in i1I1iIi :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for i1I1iIi , iI , oooOo0OOOoo0 , url in III1 :
  if oOOoo0000O0o0 in i1I1iIi :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , iI , iI , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oooOo0OOOoo0 , url in OooooO0oOOOO :
  Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for i1I1iIi , oooOo0OOOoo0 , url in o0O00oOOoo :
  if oOOoo0000O0o0 in i1I1iIi :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
def IIii11Ii1i1I ( name , url ) :
 OOoo0O0 = iiiIi1i1I ( url )
 Oooo0O = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 for oooOo0OOOoo0 , url in Oooo0O :
  Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 90 - 90: iIii1I11I1II1 % iii
def iiIi11iI1iii ( url ) :
 url = url
 IiII111iI1ii1 = [ '[COLORsteelblue](_) _No Group[/COLOR]' , '[COLORsteelblue](UK) United Kingdom[/COLOR]' , '[COLORsteelblue](US) United States[/COLOR]' , '[COLORsteelblue](AL) Albania[/COLOR]' , '[COLORsteelblue](AS) American Samoa[/COLOR]' , '[COLORsteelblue](AR) Argentina[/COLOR]' , '[COLORsteelblue](AU) Australia[/COLOR]' , '[COLORsteelblue](AZ) Azerbaijan[/COLOR]' , '[COLORsteelblue](BY) Belarus[/COLOR]' , '[COLORsteelblue](BE) Belgium[/COLOR]' , '[COLORsteelblue](BO) Bolivia[/COLOR]' , '[COLORsteelblue](BR) Brazil[/COLOR]' , '[COLORsteelblue](CM) Cameroon[/COLOR]' , '[COLORsteelblue](CA) Canada[/COLOR]' , '[COLORsteelblue](CO) Colombia[/COLOR]' , '[COLORsteelblue](CZ) Czech Republic[/COLOR]' , '[COLORsteelblue](DO) Dominican Republic[/COLOR]' , '[COLORsteelblue](EC) Ecuador[/COLOR]' , '[COLORsteelblue](FO) Faroe Islands[/COLOR]' , '[COLORsteelblue](FR) France[/COLOR]' , '[COLORsteelblue](DE) Germany[/COLOR]' , '[COLORsteelblue](GR) Greece[/COLOR]' , '[COLORsteelblue](IS) Iceland[/COLOR]' , '[COLORsteelblue](IN) India[/COLOR]' , '[COLORsteelblue](ID) Indonesia[/COLOR]' , '[COLORsteelblue](IR) Iran[/COLOR]' , '[COLORsteelblue](IT) Italy[/COLOR]' , '[COLORsteelblue](LA) Laos[/COLOR]' , '[COLORsteelblue](MO) Macau[/COLOR]' , '[COLORsteelblue](MX) Mexico[/COLOR]' , '[COLORsteelblue](NL) Netherlands[/COLOR]' , '[COLORsteelblue](NE) Niger[/COLOR]' , '[COLORsteelblue](PK) Pakistan[/COLOR]' , '[COLORsteelblue](PA) Panama[/COLOR]' , '[COLORsteelblue](PE) Peru[/COLOR]' , '[COLORsteelblue](PL) Poland[/COLOR]' , '[COLORsteelblue](PT) Portugal[/COLOR]' , '[COLORsteelblue](RO) Romania[/COLOR]' , '[COLORsteelblue](RU) Russia[/COLOR]' , '[COLORsteelblue](SL) Sierra Leone[/COLOR]' , '[COLORsteelblue](EX-YU) Slovenia[/COLOR]' , '[COLORsteelblue](SO) Somalia[/COLOR]' , '[COLORsteelblue](SP) Spain[/COLOR]' , '[COLORsteelblue](SE) Sweden[/COLOR]' , '[COLORsteelblue](CH) Switzerland[/COLOR]' , '[COLORsteelblue](TH) Thailand[/COLOR]' , '[COLORsteelblue](TR) Turkey[/COLOR]' , '[COLORsteelblue](UA) Ukraine[/COLOR]' , '[COLORsteelblue](VE) Venezuela[/COLOR]' , '[COLORsteelblue](WW) World Wide[/COLOR]' ]
 iI11I1II = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Select Country[/COLOR]' , IiII111iI1ii1 )
 if iI11I1II == 0 :
  Iii111II = '(_)'
 if iI11I1II == 1 :
  Iii111II = '(UK)'
 if iI11I1II == 2 :
  Iii111II = '(US)'
 if iI11I1II == 3 :
  Iii111II = '(AL)'
 if iI11I1II == 4 :
  Iii111II = '(AS)'
 if iI11I1II == 5 :
  Iii111II = '(AR)'
 if iI11I1II == 6 :
  Iii111II = '(AU)'
 if iI11I1II == 7 :
  Iii111II = '(AZ)'
 if iI11I1II == 8 :
  Iii111II = '(BY)'
 if iI11I1II == 9 :
  Iii111II = '(BE)'
 if iI11I1II == 10 :
  Iii111II = '(BO)'
 if iI11I1II == 11 :
  Iii111II = '(BR)'
 if iI11I1II == 12 :
  Iii111II = '(CM)'
 if iI11I1II == 13 :
  Iii111II = '(CA)'
 if iI11I1II == 14 :
  Iii111II = '(CO)'
 if iI11I1II == 15 :
  Iii111II = '(CZ)'
 if iI11I1II == 16 :
  Iii111II = '(DO)'
 if iI11I1II == 17 :
  Iii111II = '(EC)'
 if iI11I1II == 18 :
  Iii111II = '(FO)'
 if iI11I1II == 19 :
  Iii111II = '(FR)'
 if iI11I1II == 20 :
  Iii111II = '(DE)'
 if iI11I1II == 21 :
  Iii111II = '(GR)'
 if iI11I1II == 22 :
  Iii111II = '(IS)'
 if iI11I1II == 23 :
  Iii111II = '(IN)'
 if iI11I1II == 24 :
  Iii111II = '(ID)'
 if iI11I1II == 25 :
  Iii111II = '(IR)'
 if iI11I1II == 26 :
  Iii111II = '(IT)'
 if iI11I1II == 27 :
  Iii111II = '(LA)'
 if iI11I1II == 28 :
  Iii111II = '(MO)'
 if iI11I1II == 29 :
  Iii111II = '(MX)'
 if iI11I1II == 30 :
  Iii111II = '(NL)'
 if iI11I1II == 31 :
  Iii111II = '(NE)'
 if iI11I1II == 32 :
  Iii111II = '(PK)'
 if iI11I1II == 33 :
  Iii111II = '(PA)'
 if iI11I1II == 34 :
  Iii111II = '(PE)'
 if iI11I1II == 35 :
  Iii111II = '(PL)'
 if iI11I1II == 36 :
  Iii111II = '(PT)'
 if iI11I1II == 37 :
  Iii111II = '(RO)'
 if iI11I1II == 38 :
  Iii111II = '(RU)'
 if iI11I1II == 39 :
  Iii111II = '(SL)'
 if iI11I1II == 40 :
  Iii111II = '(EX-YU)'
 if iI11I1II == 41 :
  Iii111II = '(SO)'
 if iI11I1II == 42 :
  Iii111II = '(SP)'
 if iI11I1II == 43 :
  Iii111II = '(SE)'
 if iI11I1II == 44 :
  Iii111II = '(CH)'
 if iI11I1II == 45 :
  Iii111II = '(TH)'
 if iI11I1II == 46 :
  Iii111II = '(TR)'
 if iI11I1II == 47 :
  Iii111II = '(UA)'
 if iI11I1II == 48 :
  Iii111II = '(VE)'
 if iI11I1II == 49 :
  Iii111II = '(WW)'
 o0OO0o0o00o ( Iii111II , url )
 if 73 - 73: O0 * IIII + o0o0OOO0o0 + iii
def Ii ( url ) :
 OOoo0O0 = iiiIi1i1I ( url )
 O00oO = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 OOOiiiiI = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 II1III = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 III1 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 OooooO0oOOOO = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( OOoo0O0 )
 o0O00oOOoo = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 Oooo0O = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( OOoo0O0 )
 for Iii111II , iI , i1I1iIi , oooOo0OOOoo0 , url in O00oO :
  if 'INFO' in i1I1iIi :
   pass
  else :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( Iii111II + oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , iI , iI , ( '[COLORsteelblue]' + ( Iii111II + oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for iI , i1I1iIi , oooOo0OOOoo0 , url in OOOiiiiI :
  if 'INFO' in i1I1iIi :
   pass
  else :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , iI , iI , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for i1I1iIi , oooOo0OOOoo0 , url in II1III :
  if 'INFO' in i1I1iIi :
   pass
  else :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for i1I1iIi , iI , oooOo0OOOoo0 , url in III1 :
  if 'INFO' in i1I1iIi :
   pass
  else :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , iI , iI , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oooOo0OOOoo0 , url in OooooO0oOOOO :
  Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for i1I1iIi , oooOo0OOOoo0 , url in o0O00oOOoo :
  if 'INFO' in i1I1iIi :
   pass
  else :
   Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + i1I1iIi + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oooOo0OOOoo0 , url in Oooo0O :
  Ooo0OO0oOO ( ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oooOo0OOOoo0 ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 100 - 100: o0 + III1I11iiii1I + III1I11iiii1I
def I1ii1I1iiii ( url ) :
 if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
  RESOLVEtest ( ( url ) . strip ( ) )
 else :
  try :
   iiI ( ( url ) . strip ( ) )
  except :
   pass
  else :
   iiI ( 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + url )
   if 56 - 56: iiiIi . iiIiIIi . iI1I
def ii111I ( url ) :
 OOoo0O0 = cloudflare . source ( url )
 o0O = re . compile ( 'class="footer-univers">.+?<h2 class="tag-sport.+?>(.+?)</h2>(.+?)</span>' , re . DOTALL ) . findall ( OOoo0O0 )
 for Iii111II , iIiIi11 in o0O :
  O00oO = re . compile ( '<a href="([^"]*)">.+?<h3>(.+?)</h3>' , re . DOTALL ) . findall ( str ( iIiIi11 ) )
  Ooo0OO0oOO ( ( '[COLORorangered]' + Iii111II + '[/COLOR]' ) . replace ( '\n' , ' ' ) . replace ( '_' , ' ' ) . replace ( ' ' , '' ) , '' , '' , i1 + 'extreme.jpg' , Oo0o0000o0o0 , ( '[COLORorangered]' + Iii111II + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( ' ' , '' ) )
  for i1I1IiiIi1i , iIIIiIi in O00oO :
   oOOO00o ( ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '-' ) . replace ( '' , '' ) . replace ( '\n' , ' ' ) , 'https://www.ridersmatch.com' + i1I1IiiIi1i , 21 , i1 + 'extreme.jpg' , Oo0o0000o0o0 , ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '-' ) . replace ( '' , '' ) . replace ( '\n' , ' ' ) )
   if 17 - 17: iI1I . O0 + OO
def ii ( url ) :
 OOoo0O0 = cloudflare . source ( url )
 O00oO = re . compile ( 'list-videothumbnail" href="(.+?)".+?title="(.+?)".+?style=".+?url(.+?)"' , re . DOTALL ) . findall ( OOoo0O0 )
 oooO = re . compile ( '<a class="page-link nex" href="([^"]*)">Next</a>' , re . DOTALL ) . findall ( OOoo0O0 )
 for url , Iii111II , iI in O00oO :
  iI = iI . replace ( '(' , '' ) . replace ( ')' , '' )
  Ooo0OO0oOO ( ( '[COLORsteelblue]' + Iii111II + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '' ) . replace ( '_' , ' ' ) . replace ( '\n' , ' ' ) , 'https://www.ridersmatch.com' + url , 23 , iI , Oo0o0000o0o0 , ( '[COLORsteelblue]' + Iii111II + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '' ) . replace ( '_' , ' ' ) . replace ( '\n' , ' ' ) )
 for url in oooO :
  oOOO00o ( ( '[COLORorangered]Next Page[/COLOR]' ) . replace ( '_' , ' ' ) , 'https://www.ridersmatch.com' + url , 21 , iI , Oo0o0000o0o0 , '[COLORorangered]Next Page[/COLOR]' )
  if 25 - 25: OoooooooOO - iI1I . iI1I * iii1I1
def o000oo ( url ) :
 oo0OooOOo0 = cloudflare . source ( url )
 O00oO = re . compile ( 'src="//www.youtube.com/embed/(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 )
 for url in O00oO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 95 - 95: iii / iii
  if 30 - 30: iiIiIIi + iiiIi / iiiIi % iiIiIIi . iiIiIIi
def O0O0Oo00 ( url ) :
 OOoo0O0 = iiiIi1i1I ( url )
 oOO00oOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoo0O0 )
 for url , iI , o00O , OOO0OOO00oo , Iii111II in oOO00oOO :
  if '.php' in url :
   oOOO00o ( Iii111II , url , 211 , iI , OOO0OOO00oo , o00O )
  else :
   oOOO00o ( Iii111II , url , 212 , iI , OOO0OOO00oo , o00O )
def oOoO00o ( url , iconimage ) :
 iI = iconimage
 iI1i111I1Ii = oo0o0O00 . open ( url ) . read ( )
 if 100 - 100: I1I1IIiiIiI1 + III1I11iiii1I * I1I1IIiiIiI1
 try :
  oOOo0OOOo00O = re . findall ( r'<a .*?>(.*?)</a>' , iI1i111I1Ii )
  OooOOOO = re . findall ( r'<a.*?href="(.*?)">' , iI1i111I1Ii )
  if 45 - 45: iiIiIIi % iI1I - i11iIiiIii
  for i1I1IiiIi1i in OooOOOO :
   if '.gif' in i1I1IiiIi1i :
    pass
   if '.srt' in i1I1IiiIi1i :
    pass
   elif '..' in i1I1IiiIi1i :
    pass
   elif '.txt' in i1I1IiiIi1i :
    pass
   elif '.nfo' in i1I1IiiIi1i :
    pass
   elif '.jpg' in i1I1IiiIi1i :
    pass
   elif '1-Irani/' in i1I1IiiIi1i :
    pass
   elif 'index.php' in i1I1IiiIi1i :
    pass
   elif '.png' in i1I1IiiIi1i :
    pass
   elif '?C=M&O=D' in i1I1IiiIi1i :
    pass
   elif '?C=M&O=A' in i1I1IiiIi1i :
    pass
   elif '?C=N&O=D' in i1I1IiiIi1i :
    pass
   elif '?C=N&O=A' in i1I1IiiIi1i :
    pass
   elif '?C=S&O=A' in i1I1IiiIi1i :
    pass
   elif '?C=S&O=D' in i1I1IiiIi1i :
    pass
   elif '?C=N;O=D' in i1I1IiiIi1i :
    pass
   elif '?C=M;O=A' in i1I1IiiIi1i :
    pass
   elif '?C=S;O=A' in i1I1IiiIi1i :
    pass
   elif '?C=D;O=A' in i1I1IiiIi1i :
    pass
   elif 'Torrent' in i1I1IiiIi1i :
    pass
   elif 'exe' in i1I1IiiIi1i :
    pass
   elif 'public' in i1I1IiiIi1i :
    pass
   elif '?C=D;O=A' in i1I1IiiIi1i :
    pass
   elif 'pub' in i1I1IiiIi1i :
    pass
   elif 'install' in i1I1IiiIi1i :
    pass
   elif '?C=D;O=A' in i1I1IiiIi1i :
    pass
   elif '?C=D;O=A' in i1I1IiiIi1i :
    pass
   elif '.m3u' in i1I1IiiIi1i :
    pass
   elif '?C=D;O=A' in i1I1IiiIi1i :
    pass
   elif 'mpeg' in i1I1IiiIi1i :
    pass
   elif '.doc' in i1I1IiiIi1i :
    pass
   elif '.html' in i1I1IiiIi1i :
    pass
   elif 'boss' in i1I1IiiIi1i :
    pass
   elif 'plex' in i1I1IiiIi1i :
    pass
   else :
    Iii111II = i1I1IiiIi1i
    if 'txt' in Iii111II :
     pass
    if '.' in Iii111II :
     Iii111II = Iii111II . replace ( '.' , ' ' )
    if '_' in Iii111II :
     Iii111II = Iii111II . replace ( '_' , ' ' )
    if '%20' in Iii111II :
     Iii111II = Iii111II . replace ( '%20' , ' ' )
    if '/' in Iii111II :
     Iii111II = Iii111II . replace ( '/' , '' )
    if 'mkv' in Iii111II :
     Iii111II = Iii111II . replace ( 'mkv' , '' )
    if 'avi' in Iii111II :
     Iii111II = Iii111II . replace ( 'avi' , '' )
    if 'mp4' in Iii111II :
     Iii111II = Iii111II . replace ( 'mp4' , '' )
    if 'Tehmovies' in Iii111II :
     Iii111II = Iii111II . replace ( 'Tehmovies' , '' )
    if 'h264' in Iii111II :
     Iii111II = Iii111II . replace ( 'h264' , '' )
    if 'WEB' in Iii111II :
     Iii111II = Iii111II . replace ( 'WEB' , '' )
    if 'HEEL' in Iii111II :
     Iii111II = Iii111II . replace ( '-HEEL' , '' )
    if 'MeGusta' in Iii111II :
     Iii111II = Iii111II . replace ( 'MeGusta' , '' )
    if 'x264' in Iii111II :
     Iii111II = Iii111II . replace ( 'x264' , '' )
    if 'x265' in Iii111II :
     Iii111II = Iii111II . replace ( 'x265' , '' )
    if 'HDTV' in Iii111II :
     Iii111II = Iii111II . replace ( 'HDTV' , '' )
    if '-Ebi' in Iii111II :
     Iii111II = Iii111II . replace ( '-Ebi' , '' )
    if '-' in Iii111II :
     Iii111II = Iii111II . replace ( '-' , '' )
    if 'NWCHD' in Iii111II :
     Iii111II = Iii111II . replace ( 'NWCHD' , '' )
    if 'FMN' in Iii111II :
     Iii111II = Iii111II . replace ( 'FMN' , '' )
    if 'PLUTONiUM' in Iii111II :
     Iii111II = Iii111II . replace ( 'PLUTONiUM' , '' )
    if 'H264' in Iii111II :
     Iii111II = Iii111II . replace ( 'H264' , '' )
    if 'H265' in Iii111II :
     Iii111II = Iii111II . replace ( 'H265' , '' )
    if 'WD' in Iii111II :
     Iii111II = Iii111II . replace ( 'WD' , '' )
    if 'hdtv' in Iii111II :
     Iii111II = Iii111II . replace ( 'hdtv' , '' )
     if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * iI1I
     if 46 - 46: i1I111I + OO
    if '.mkv' in i1I1IiiIi1i or '.m4B' in i1I1IiiIi1i or '.m4v' in i1I1IiiIi1i or '.mp3' in i1I1IiiIi1i or '.mp4' in i1I1IiiIi1i or '.avi' in i1I1IiiIi1i or '.flv' in i1I1IiiIi1i or '.mpeg' in i1I1IiiIi1i or '.3gp' in i1I1IiiIi1i or '.divx' in i1I1IiiIi1i or '.strm' in i1I1IiiIi1i :
     o0o0O ( '[COLORsteelblue]' + Iii111II + '[/COLOR]' , url + i1I1IiiIi1i , 222 , iI , OOO0OOO00oo , '[COLORsteelblue]' + Iii111II + '[/COLOR]' )
     if 68 - 68: iii
    else :
     oOOO00o ( '[COLORsteelblue]' + Iii111II + '[/COLOR]' , url + i1I1IiiIi1i , 212 , iI , OOO0OOO00oo , '[COLORsteelblue]' + Iii111II + '[/COLOR]' )
     if 25 - 25: iiIiIIi . iii
     if 24 - 24: iii1I1 / i11iIiiIii + iii1I1
     if 20 - 20: IiI1i11iii1 + o0o0OOO0o0 / O0 % iIii1I11I1II1
     if 88 - 88: i1I111I / II111iiii
 except Exception , i11i1ii1I :
  print str ( i11i1ii1I )
def OOOOO0O00 ( name , url , mode , iconimage , description = "" , isFolder = True , background = None ) :
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 if 31 - 31: I1I1IIiiIiI1 % OO
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 if background :
  iI1IOooOoOo . setProperty ( 'fanart_image' , background )
 if mode == 1 or mode == 2 :
  iI1IOooOoOo . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10008 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=22)' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) ) ) ] )
 elif mode == 404 :
  iI1IOooOoOo . setProperty ( 'IsPlayable' , 'true' )
  iI1IOooOoOo . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10009 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
 elif mode == 556 :
  iI1IOooOoOo . setProperty ( 'IsPlayable' , 'true' )
  iI1IOooOoOo . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10010 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
  if 14 - 14: I1I1IIiiIiI1 * III1I11iiii1I + IIII + O0 + i11iIiiIii
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = isFolder )
 if 77 - 77: I1I1IIiiIiI1 / OoooooooOO
def IIii11I1i1I ( handle , url , listitem , isFolder ) :
 if 99 - 99: IIII
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 76 - 76: OO * iI1I
 if 82 - 82: o0o0OOO0o0 * IIII / iiIiIIi
 if 36 - 36: OoooooooOO - i1IIi . O0 / II111iiii + I1I1IIiiIiI1
def Ii111 ( title , message , times = 2000 , icon = o0oOoO00o ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def I111i1i1111 ( ) :
 IIII1 = I1I1i ( )
 I1IIIiIiIi = IIII1 . replace ( I1ii11iIi11i , "" )
 if os . path . exists ( IIII1 ) or not IIII1 == False :
  IIIII1 = open ( IIII1 , mode = 'r' ) ; iIi1Ii1i1iI = IIIII1 . read ( ) ; IIIII1 . close ( )
  IIiI1 ( "%s - %s" % ( IiII , I1IIIiIiIi ) , iIi1Ii1i1iI )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def I1I1i ( ) :
 i1iI1 = False
 if os . path . exists ( os . path . join ( I1ii11iIi11i , 'xbmc.log' ) ) :
  i1iI1 = os . path . join ( I1ii11iIi11i , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'kodi.log' ) ) :
  i1iI1 = os . path . join ( I1ii11iIi11i , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'spmc.log' ) ) :
  i1iI1 = os . path . join ( I1ii11iIi11i , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'tvmc.log' ) ) :
  i1iI1 = os . path . join ( I1ii11iIi11i , 'tvmc.log' )
 return i1iI1
 if 1 - 1: i1IIi . i11iIiiIii % III1I11iiii1I
 if 82 - 82: iIii1I11I1II1 + iiiIi . iIii1I11I1II1 % o0O0 / o0o0OOO0o0 . o0o0OOO0o0
 if 14 - 14: I1I1IIiiIiI1 . III1I11iiii1I . IiI1i11iii1 + OoooooooOO - III1I11iiii1I + o0O0
 if 9 - 9: o0o0OOO0o0
 if 59 - 59: iI1I * II111iiii . O0
def IIiI1 ( heading , announce ) :
 class ii1IO0oO0 ( ) :
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
   try : IIIII1 = open ( announce ) ; O000OoOO0 = IIIII1 . read ( )
   except : O000OoOO0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O000OoOO0 ) )
   return
 ii1IO0oO0 ( )
 ii1IO0oO0 ( )
 if 30 - 30: o0O0
def oOO ( ) :
 o0o0O ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 o0o0O ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 o0o0O ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 o0o0O ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 o0o0O ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 if 53 - 53: o0 * o0O0 . iiiIi - o0o0OOO0o0 % o0o0OOO0o0 * i11iIiiIii
 if 7 - 7: O0 . o0o0OOO0o0
 if 51 - 51: OO - O0 % iii1I1 - II111iiii
def I1II ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def Oo000ooOOO ( url ) :
 if url == 'http://' : return False
 try :
  o0000oO = urllib2 . Request ( url )
  o0000oO . add_header ( 'User-Agent' , iIiiiI )
  iI1i111I1Ii = urllib2 . urlopen ( o0000oO )
  iI1i111I1Ii . close ( )
 except Exception , i11i1ii1I :
  return i11i1ii1I
 return True
 if 31 - 31: iIii1I11I1II1 % IiI1i11iii1 % iii . o0o0OOO0o0 - IiI1i11iii1
 if 17 - 17: o0o0OOO0o0
 if 27 - 27: i11iIiiIii % II111iiii % IiI1i11iii1 . O0 - iiiIi + i1I111I
def ooO0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv Sports" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By GenieTv Sports[/COLOR]" )
 return
 if 51 - 51: o0O0
def ii11I1 ( url ) :
 print '###' + IiII + ' - DELETING Addons20.db ###'
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 Ii111iIi1iIi = os . path . join ( oO0oo , 'Addons20.db' )
 try :
  os . remove ( Ii111iIi1iIi )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== ' + IiII + ' - DELETING    ' + str ( Ii111iIi1iIi ) + '    ==='
  ii11iIi1I . ok ( IiII , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "       No File To Remove" )
 return
 if 21 - 21: iii1I1 / iiIiIIi + o0o0OOO0o0 + OoooooooOO
 if 91 - 91: i11iIiiIii / i1IIi + IIII + iii * i11iIiiIii
 if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + IiI1i11iii1 * o0 . o0O0
 if 52 - 52: iii + O0 . IIII . iiIiIIi . OO
 if 97 - 97: iI1I / IIII
def iiiIi1i1I ( url ) :
 o0000oO = urllib2 . Request ( url )
 o0000oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iI1i111I1Ii = urllib2 . urlopen ( o0000oO )
 i1I1IiiIi1i = iI1i111I1Ii . read ( )
 iI1i111I1Ii . close ( )
 return i1I1IiiIi1i
def ii1IO0oO0 ( title , msg ) :
 class IIiI1 ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 71 - 71: II111iiii / i1IIi . iiIiIIi % OoooooooOO . i1I111I
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 41 - 41: i1IIi * II111iiii / OoooooooOO . III1I11iiii1I
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 83 - 83: IIII . O0 / iiiIi / III1I11iiii1I - II111iiii
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 100 - 100: OO
 II1i = IIiI1 ( "Textbox.xml" , o0OOO . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 II1i . doModal ( )
 del II1i
def IIiI1 ( heading , announce ) :
 class ii1IO0oO0 ( ) :
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
   try : IIIII1 = open ( announce ) ; O000OoOO0 = IIIII1 . read ( )
   except : O000OoOO0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O000OoOO0 ) )
   return
 ii1IO0oO0 ( )
 ii1IO0oO0 ( )
def Ii1IIIIi1ii1I ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 IiiIiI1Ii1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1iIi , iiiii1II , O0OOO0OOooo00 in os . walk ( IiiIiI1Ii1i ) :
   I111iIi1 = 0
   I111iIi1 += len ( O0OOO0OOooo00 )
   if 92 - 92: iii
   if 22 - 22: iiiIi % IIII * iiIiIIi / III1I11iiii1I % i11iIiiIii * IiI1i11iii1
   if I111iIi1 > 0 :
    if 95 - 95: OoooooooOO - o0O0 * iI1I + i1I111I
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( I111iIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 10 - 10: I1I1IIiiIiI1 / i11iIiiIii
     for IIIII1 in O0OOO0OOooo00 :
      os . unlink ( os . path . join ( i1iIi , IIIII1 ) )
     for o00oO in iiiii1II :
      shutil . rmtree ( os . path . join ( i1iIi , o00oO ) )
     ii11iIi1I = xbmcgui . Dialog ( )
     ii11iIi1I . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    ii11iIi1I = xbmcgui . Dialog ( )
    ii11iIi1I . ok ( IiII , "       No Packages to DELETE" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "Error Deleting Packages please visit The Support Group, GenieTv Sports on facebook" )
 O00O0Ooooo00 ( url )
 return
def O00O0Ooooo00 ( url ) :
 O000 = os . path . join ( I1i1iiI1 , 'addon_data' )
 ooo0o000O = [
 ( O000 ) ,
 ( oo00 ) ,
 ( os . path . join ( O0oo0OO0 , 'cache' ) ) ,
 ( os . path . join ( O0oo0OO0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo00 , 'plugin.video.GenieTv_Sports' , 'Images' ) ) ,
 ( os . path . join ( O000 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( O000 , 'plugin.video.GenieTv_Sports' , 'Images' ) ) ]
 if 100 - 100: iii1I1 . iii * iiIiIIi / iIii1I11I1II1 * i1IIi % iii
 I1I = 0
 if 89 - 89: i1IIi / II111iiii . iIii1I11I1II1
 for i11IIIiI1I in ooo0o000O :
  if os . path . exists ( i11IIIiI1I ) and not i11IIIiI1I in [ oo00 , O000 ] :
   for i1iIi , iiiii1II , O0OOO0OOooo00 in os . walk ( i11IIIiI1I ) :
    I111iIi1 = 0
    I111iIi1 += len ( O0OOO0OOooo00 )
    if I111iIi1 > 0 :
     for IIIII1 in O0OOO0OOooo00 :
      if not IIIII1 in iiIIIII1i1iI :
       try :
        os . unlink ( os . path . join ( i1iIi , IIIII1 ) )
       except :
        pass
      else : IIII1 ( 'Ignore Log File: %s' % IIIII1 )
     for o00oO in iiiii1II :
      try :
       shutil . rmtree ( os . path . join ( i1iIi , o00oO ) )
       I1I += 1
       IIII1 ( "[Success] cleared %s files from %s" % ( str ( I111iIi1 ) , os . path . join ( i11IIIiI1I , o00oO ) ) )
      except :
       IIII1 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11IIIiI1I , o00oO ) )
  else :
   for i1iIi , iiiii1II , O0OOO0OOooo00 in os . walk ( i11IIIiI1I ) :
    for o00oO in iiiii1II :
     if 'cache' in o00oO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( i1iIi , o00oO ) )
       I1I += 1
       IIII1 ( "[Success] wiped %s " % os . path . join ( i11IIIiI1I , o00oO ) )
      except :
       IIII1 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11IIIiI1I , o00oO ) )
       if 69 - 69: O0
 Ii111 ( IiII , 'Clear Cache: Removed %s Files' % I1I )
def o0ooO ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 IiiIiI1Ii1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1iIi , iiiii1II , O0OOO0OOooo00 in os . walk ( IiiIiI1Ii1i ) :
   I111iIi1 = 0
   I111iIi1 += len ( O0OOO0OOooo00 )
   if 74 - 74: O0 * iii1I1 - i11iIiiIii + o0
   if 17 - 17: iIii1I11I1II1 . OoooooooOO / IiI1i11iii1 % II111iiii % i1IIi / i11iIiiIii
   if I111iIi1 > 0 :
    if 58 - 58: iiiIi . II111iiii + iii1I1 - i11iIiiIii / II111iiii / O0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( I111iIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 85 - 85: i1I111I + III1I11iiii1I
     for IIIII1 in O0OOO0OOooo00 :
      os . unlink ( os . path . join ( i1iIi , IIIII1 ) )
     for o00oO in iiiii1II :
      shutil . rmtree ( os . path . join ( i1iIi , o00oO ) )
     ii11iIi1I = xbmcgui . Dialog ( )
     ii11iIi1I . ok ( IiII , "       Deleting Packages all done" )
    else :
     pass
   else :
    ii11iIi1I = xbmcgui . Dialog ( )
    ii11iIi1I . ok ( IiII , "       No Packages to DELETE" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "Error Deleting Packages" )
 return
 if 10 - 10: o0O0 / OO + i1I111I / i1IIi
def i1iII1II11I ( ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 iI11I1II = ii11iIi1I . yesno ( 'Force Close GenieTv Sports' , 'You are about to close GenieTv Sports' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iI11I1II == 0 : return
 elif iI11I1II == 1 : pass
 O0Oo00O = I1II ( )
 IIII1 ( "Platform: " + str ( O0Oo00O ) )
 os . _exit ( 1 )
 IIII1 ( "Force close failed!  Trying alternate methods." )
 if O0Oo00O == 'osx' :
  IIII1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0Oo00O == 'linux' :
  IIII1 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0Oo00O == 'android' :
  IIII1 ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.GenieTv Sports' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.GenieTv Sports' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.GenieTv Sports());' )
  except : pass
  ii11iIi1I . ok ( IiII , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif O0Oo00O == 'windows' :
  IIII1 ( "############ try windows force close #################" )
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
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  IIII1 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  IIII1 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 91 - 91: iii1I1 % o0o0OOO0o0 . iii / IIII * iIii1I11I1II1
def iiI ( url ) :
 import urlresolver
 try :
  OOO0O00O0OOOO = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OOO0O00O0OOOO , xbmcgui . ListItem ( Iii111II ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( Iii111II ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def I1II ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 43 - 43: iii + IIII - o0 / O0 * iiiIi + iI1I
def IIII1 ( log ) :
 xbmc . log ( "[%s]: %s" % ( IiII , log ) )
 if not os . path . exists ( oo00 ) : os . makedirs ( oo00 )
 if not os . path . exists ( i1111 ) : IIIII1 = open ( i1111 , 'w' ) ; IIIII1 . close ( )
 with open ( i1111 , 'a' ) as IIIII1 :
  i1IIIIiI111I = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  IIIII1 . write ( i1IIIIiI111I . rstrip ( '\r\n' ) + '\n' )
  if 11 - 11: iI1I - OO
def iiiiI1i1i ( ) :
 try :
  I1i1iiI1i1i1I = getSet ( "core-player" )
  if ( I1i1iiI1i1i1I == 'DVDPLAYER' ) : oOoo000 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( I1i1iiI1i1i1I == 'MPLAYER' ) : oOoo000 = xbmc . PLAYER_CORE_MPLAYER
  elif ( I1i1iiI1i1i1I == 'PAPLAYER' ) : oOoo000 = xbmc . PLAYER_CORE_PAPLAYER
  else : oOoo000 = xbmc . PLAYER_CORE_AUTO
 except : oOoo000 = xbmc . PLAYER_CORE_AUTO
 return oOoo000
 return True
 if 87 - 87: OoooooooOO - I1I1IIiiIiI1 / o0O0 . i11iIiiIii * OoooooooOO
def oOOOoo00 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO00 = True
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1IOooOoOo . setProperty ( "Fanart_Image" , fanart )
 OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = True )
 return OO00
 if 28 - 28: iii1I1 - i11iIiiIii . iiIiIIi + o0O0 / iiIiIIi
 if 35 - 35: o0O0
def ooo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO00 = True
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1IOooOoOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOoO0 = [ ]
  OOoO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  iI1IOooOoOo . addContextMenuItems ( OOoO0 )
 OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = False )
 return OO00
 if 86 - 86: II111iiii % i11iIiiIii + o0o0OOO0o0 % i11iIiiIii
def oOOO00o ( name , url , mode , iconimage , fanart , description ) :
 if 92 - 92: i11iIiiIii - IIII / iii / iii1I1
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO00 = True
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1IOooOoOo . setProperty ( "Fanart_Image" , fanart )
 OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = True )
 return OO00
 if 43 - 43: II111iiii + III1I11iiii1I + IIII
def o0o0O ( name , url , mode , iconimage , fanart , description ) :
 if 40 - 40: I1I1IIiiIiI1
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO00 = True
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1IOooOoOo . setProperty ( "Fanart_Image" , fanart )
 OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = False )
 return OO00
def Ooo0OO0oOO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO00 = True
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1IOooOoOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOoO0 = [ ]
  if showcontext == 'fav' :
   OOoO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   OOoO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iI1IOooOoOo . addContextMenuItems ( OOoO0 )
 OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = False )
 return OO00
def OOOooo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OO00 = True
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OOoO0 = [ ]
  OOoO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OOoO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   OOoO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iI1IOooOoOo . addContextMenuItems ( OOoO0 )
 OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = True )
 return OO00
def Oo00oo0000OO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Iii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OO00 = True
 iI1IOooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1IOooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OOoO0 = [ ]
  OOoO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OOoO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   OOoO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iI1IOooOoOo . addContextMenuItems ( OOoO0 )
 OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii , listitem = iI1IOooOoOo , isFolder = False )
 return OO00
 if 69 - 69: iii - OO / i11iIiiIii + iiIiIIi % OoooooooOO
def o000O000 ( ) :
 ii1 = [ ]
 oOoO0o0ooo = sys . argv [ 2 ]
 if len ( oOoO0o0ooo ) >= 2 :
  oO0o0O0Ooo0o = sys . argv [ 2 ]
  i1Ii11II = oO0o0O0Ooo0o . replace ( '?' , '' )
  if ( oO0o0O0Ooo0o [ len ( oO0o0O0Ooo0o ) - 1 ] == '/' ) :
   oO0o0O0Ooo0o = oO0o0O0Ooo0o [ 0 : len ( oO0o0O0Ooo0o ) - 2 ]
  IioO0oOOO0Ooo = i1Ii11II . split ( '&' )
  ii1 = { }
  for i1i1I in range ( len ( IioO0oOOO0Ooo ) ) :
   IiIIi1 = { }
   IiIIi1 = IioO0oOOO0Ooo [ i1i1I ] . split ( '=' )
   if ( len ( IiIIi1 ) ) == 2 :
    ii1 [ IiIIi1 [ 0 ] ] = IiIIi1 [ 1 ]
    if 30 - 30: iiIiIIi % iI1I
 return ii1
 if 89 - 89: o0 + OoooooooOO + o0 * i1IIi + iIii1I11I1II1 % IiI1i11iii1
 if 59 - 59: III1I11iiii1I + i11iIiiIii
oO0o0O0Ooo0o = o000O000 ( )
OoOo = None
Iii111II = None
oo0OOo0O = None
Ii1IiII = None
OOO0OOO00oo = None
I1i = None
oooii1iiIi1 = None
if 34 - 34: III1I11iiii1I
if 91 - 91: iIii1I11I1II1 % I1I1IIiiIiI1 . iIii1I11I1II1 % i1IIi / II111iiii * i1I111I
try :
 oooii1iiIi1 = int ( oO0o0O0Ooo0o [ "fav_mode" ] )
except :
 pass
 if 10 - 10: II111iiii . IIII
try :
 OoOo = urllib . unquote_plus ( oO0o0O0Ooo0o [ "url" ] )
except :
 pass
try :
 Iii111II = urllib . unquote_plus ( oO0o0O0Ooo0o [ "name" ] )
except :
 pass
try :
 Ii1IiII = urllib . unquote_plus ( oO0o0O0Ooo0o [ "iconimage" ] )
except :
 pass
try :
 oo0OOo0O = int ( oO0o0O0Ooo0o [ "mode" ] )
except :
 pass
try :
 OOO0OOO00oo = urllib . unquote_plus ( oO0o0O0Ooo0o [ "fanart" ] )
except :
 pass
try :
 I1i = urllib . unquote_plus ( oO0o0O0Ooo0o [ "description" ] )
except :
 pass
 if 32 - 32: o0o0OOO0o0 . o0O0 . OoooooooOO - OO + iii1I1
 if 88 - 88: IIII
print str ( i1i1II ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( oo0OOo0O )
print "URL: " + str ( OoOo )
print "Name: " + str ( Iii111II )
print "IconImage: " + str ( Ii1IiII )
if 19 - 19: II111iiii * o0O0 + o0o0OOO0o0
if 65 - 65: III1I11iiii1I . o0 . OO . IIII - III1I11iiii1I
def ii111i ( content , viewType ) :
 if 93 - 93: OO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OOO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OOO . getSetting ( viewType ) )
  if 5 - 5: IiI1i11iii1 / III1I11iiii1I
  if 77 - 77: iii - iI1I % IiI1i11iii1 - O0
if oo0OOo0O == None : oo0Oo00Oo0 ( )
elif oo0OOo0O == 11111 : ADULT_Menu ( )
elif oo0OOo0O == 1 : Genres ( )
elif oo0OOo0O == 2 : Lists ( OoOo , Ii1IiII )
elif oo0OOo0O == 3 : all_mov ( )
elif oo0OOo0O == 4 : Search ( )
elif oo0OOo0O == 5 : oOO ( )
elif oo0OOo0O == 6 : o0ooO ( OoOo )
elif oo0OOo0O == 7 : O00O0Ooooo00 ( OoOo )
elif oo0OOo0O == 8 : i1iII1II11I ( )
elif oo0OOo0O == 10 : MyAccDetails ( )
elif oo0OOo0O == 15 : iiI ( OoOo )
elif oo0OOo0O == 16 : yt . PlayVideo ( OoOo )
elif oo0OOo0O == 18 : o0OOO . openSettings ( sys . argv [ 0 ] )
elif oo0OOo0O == 20 : ii111I ( OoOo )
elif oo0OOo0O == 21 : ii ( OoOo )
elif oo0OOo0O == 22 : Xtreme2 ( OoOo )
elif oo0OOo0O == 23 : o000oo ( OoOo )
elif oo0OOo0O == 30 : ii11i1 ( )
elif oo0OOo0O == 31 : oOI1Ii1I1 ( )
elif oo0OOo0O == 32 : i1I1iI ( )
elif oo0OOo0O == 33 : oO0o0OOOO ( )
elif oo0OOo0O == 34 : I1I1i1I ( Iii111II , I1i )
elif oo0OOo0O == 40 : ii1I1i1I ( )
elif oo0OOo0O == 41 : iiii11I ( OoOo )
elif oo0OOo0O == 211 : O0O0Oo00 ( OoOo )
elif oo0OOo0O == 212 : oOoO00o ( OoOo , Ii1IiII )
elif oo0OOo0O == 222 : iiI ( OoOo )
elif oo0OOo0O == 1000 : from imports import kodicelticfc
elif oo0OOo0O == 1001 : from imports import plzsoccer
elif oo0OOo0O == 1002 : from imports import podcasts
elif oo0OOo0O == 1003 : from imports import rebeltunes
elif oo0OOo0O == 1004 : from imports import greenbrigade
elif oo0OOo0O == 1010 : from imports import Club_Teams
elif oo0OOo0O == 1005 : I11II1i ( )
elif oo0OOo0O == 1006 : oO00 ( )
elif oo0OOo0O == 1007 : IIIII ( )
elif oo0OOo0O == 1008 : from imports import rangers
elif oo0OOo0O == 50000 : I111i1i1111 ( )
elif oo0OOo0O == 50001 : ooO0o ( )
elif oo0OOo0O == 50002 : ii11I1 ( OoOo )
elif oo0OOo0O == 300000000 : FluxUstv ( )
elif oo0OOo0O == 300000001 : Ii ( OoOo )
elif oo0OOo0O == 300000002 : o0ooooO0o0O ( OoOo )
elif oo0OOo0O == 300000003 : o0OO0o0o00o ( Iii111II , OoOo )
elif oo0OOo0O == 300000004 : iiIi11iI1iii ( OoOo )
elif oo0OOo0O == 300000005 : I1ii1I1iiii ( OoOo )
elif oo0OOo0O == 300000006 : IIii11Ii1i1I ( Iii111II , OoOo )
if 67 - 67: III1I11iiii1I + iiiIi
elif oo0OOo0O == 900300 : ii1I1 ( )
elif oo0OOo0O == 900301 : oOo0OOoO0 ( OoOo )
elif oo0OOo0O == 900302 : i1I1i111Ii ( OoOo )
elif oo0OOo0O == 90030 : i1i1iI1iiiI ( )
elif oo0OOo0O == 1001111 : II ( Iii111II , OoOo )
if 84 - 84: O0 * OoooooooOO - o0O0 * o0O0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
