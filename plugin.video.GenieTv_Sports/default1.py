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
o0OoOoOO00 = "0.0.4"
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
 oOOO00o ( '[COLORorangered]Club Teams[/COLOR]' , Oo0oO0ooo , 1000 , i1 + 'clubteams.jpg' , Oo0o0000o0o0 , '[COLORorangered]Club Teams [CR]YouTube Channels[/COLOR]' )
 O0O00o0OOO0 ( '[COLORorangered]DISCLAIMER[/COLOR]' , Oo0oO0ooo , 11111 , i1 + 'disclaimer.jpg' , Oo0o0000o0o0 , '[COLORorangered]DISCLAIMER[/COLOR]' )
 if 27 - 27: IIII % o0O0 . ii1I11II1ii1i % I1i1iii - IiiI11Iiiii / OoooooooOO
def I1I1i ( ) :
 oOOOoo0O0OoO = '[COLORorangered]GenieTv Disclaimer[/COLOR]'
 ii1i1I1i = '[COLORorangered]Due to the nature of our content, [COLORsteelblue][B]we are not responsible[/B] [COLORorangered]for the content streamed to your device and neither do we condone piracy [CR]so you must satisfy yourself that either you or the sites accessed for streaming have the copyright agreements in place and are entitled to access this content.[CR][CR]We do not host or upload any video, films, media file, live streams (avi, mov, flv, mpg, mpeg, divx, dvd rip, mp3, mp4, torrent, ipod, psp). [CR][CR][COLORsteelblue][B]GenieTv is not responsible[/B] [COLORorangered]for the accuracy, compliance, copyright, legality, decency, or any other aspect of the content of streamed from your device. [CR]If you have any legal issues please contact the appropriate media file owners or host sites.[CR][CR]We have no control over the links on any site that we provide a link to. [CR]If you see any form of infringements, please contact appropriate media file owners or host sites immediately.[/COLOR]'
 o00oOO0 ( oOOOoo0O0OoO , ii1i1I1i )
 if 95 - 95: III1I11iiii1I / OoooooooOO
 if 18 - 18: i11iIiiIii
def Ii11I ( ) :
 plugintools . log ( "docu.run" )
 if 69 - 69: iii1I1 % I1i1iii - I1I1IIiiIiI1 + I1i1iii - O0 % OoooooooOO
 if 31 - 31: II111iiii - III1I11iiii1I . I1i1iii % i1I111I - O0
 iii11 = plugintools . get_params ( )
 if 58 - 58: III1I11iiii1I * i11iIiiIii / i1I111I % I1i1iii - iiIiIIi / iii1I1
 if iii11 . get ( "action" ) is None :
  ii11i1 ( iii11 )
 else :
  IIIii1II1II = iii11 . get ( "action" )
  exec IIIii1II1II + "(params)"
  if 42 - 42: IIII + iii1I1
 plugintools . close_item_list ( )
def ii11i1 ( params ) :
 o0O0o0Oo = Ii11Ii1I ( Oo0oO0ooo + O0O ( 'Q2x1Yl9UZWFtcy54bWw=' ) )
 O00oO = re . compile ( 'title="([^"]*)",.+?url="([^"]*)",.+?thumbnail="([^"]*)",' , re . DOTALL ) . findall ( o0O0o0Oo )
 for oOOOoo0O0OoO , I11i1I1I , oO0Oo , in O00oO :
  plugintools . add_item (

  title = oOOOoo0O0OoO ,
 url = "plugin://plugin.video.youtube/channel/" + I11i1I1I + "/" ,
 thumbnail = oO0Oo ,
 folder = True )
  if 54 - 54: I1I1IIiiIiI1 - iI1I + OoooooooOO
def O0o0 ( ) :
 oOOO00o ( '[COLORorangered]Extreme Sports[/COLOR]' , 'http://www.ridersmatch.com/' , 20 , i1 + 'extreme.jpg' , Oo0o0000o0o0 , '[COLORorangered]Extreme Sports[/COLOR]' )
 o0O0o0Oo = Ii11Ii1I ( Oo0oO0ooo + O0O ( 'VHJvamFuLnBocA==' ) )
 O00oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0O0o0Oo )
 for I11i1I1I , oO0Oo , ii1i1I1i , OO00Oo , oOOOoo0O0OoO in O00oO :
  oO0Oo = ( O0O ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9wbGV4L2Rvd25sb2Fkcy9TUE9SVFMuQ0FUQ0hVUC8=' ) + O0O ( oO0Oo ) )
  oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , ( Oo0oO0ooo + O0O ( I11i1I1I ) ) , 41 , oO0Oo , oO0Oo , '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' )
def O0OOO0OOoO0O ( url ) :
 o0O0o0Oo = Ii11Ii1I ( url )
 O00oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0O0o0Oo )
 for url , oO0Oo , ii1i1I1i , OO00Oo , oOOOoo0O0OoO in O00oO :
  if '.php' in url :
   oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , url , 41 , oO0Oo , Oo0o0000o0o0 , '[COLORorangered]' + ii1i1I1i + '[/COLOR]' )
  else :
   O0O00o0OOO0 ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , url , 15 , oO0Oo , Oo0o0000o0o0 , '[COLORorangered]' + ii1i1I1i + '[/COLOR]' )
def O00Oo000ooO0 ( ) :
 oOOO00o ( '[COLORorangered]Highlights[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]Highlights[/COLOR]' )
 oOOO00o ( '[COLORorangered]Latest Results[/COLOR]' , '' , 33 , i1 + 'latest_results.jpg' , Oo0o0000o0o0 , '[COLORorangered]Latest Results[/COLOR]' )
 oOOO00o ( '[COLORorangered]Top Goal Scorers[/COLOR]' , '' , 32 , i1 + 'top_scorers.jpg' , Oo0o0000o0o0 , '[COLORorangered]Top Goal Scorers[/COLOR]' )
 if 100 - 100: O0 + ii1I11II1ii1i - III1I11iiii1I + i11iIiiIii * IIII
def iII ( ) :
 o0 = Ii11Ii1I ( 'http://www.eplsite.com/fetchdata_toptenscorer.php' )
 ooOooo000oOO = re . compile ( '"Topscorer"(.+?)"AccountInformation"' , re . DOTALL ) . findall ( o0 )
 Oo0oOOo = re . compile ( '{"Rank":"([^"]*)","Name":"([^"]*)","TeamName":"([^"]*)","Team_Id":"([^"]*)","Nationality":"([^"]*)","Goals":"([^"]*)","FirstScorer":"([^"]*)","Penalties":"([^"]*)","MissedPenalties":"([^"]*)"}' , re . DOTALL ) . findall ( str ( ooOooo000oOO ) )
 for Oo0OoO00oOO0o , OOO00O , OOoOO0oo0ooO , O0o0O00Oo0o0 , O00O0oOO00O00 , i1Oo00 , i1i , iiI111I1iIiI , II in Oo0oOOo :
  Ii1I1IIii1II = 'Rank: ' + Oo0OoO00oOO0o + '[CR]Name: ' + OOO00O + '[CR]TeamName: ' + OOoOO0oo0ooO + '[CR]Team Id: ' + O0o0O00Oo0o0 + '[CR]Nationality: ' + O00O0oOO00O00 + '[CR]Goals: ' + i1Oo00 + '[CR]FirstScorer: ' + i1i + '[CR]Penalties: ' + iiI111I1iIiI + '[CR]MissedPenalties: ' + II + '\n'
  O0O00o0OOO0 ( '[COLORorangered]' + OOO00O + '[/COLOR]' , '' , '' , i1 + 'top_scorers.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + Ii1I1IIii1II + '[/COLOR]' )
  if 65 - 65: IIII . iIii1I11I1II1 / O0 - IIII
def iii1i1iiiiIi ( ) :
 o0 = Ii11Ii1I ( 'http://eplsite.com/fetchdata_liveresult.php' )
 ooOooo000oOO = re . compile ( '"Match"(.+?)"AccountInformation"' , re . DOTALL ) . findall ( o0 )
 Oo0oOOo = re . compile ( '{"Id":(.+?),"FixtureMatch_Id":(.+?),"Date":(.+?),"Round":(.+?),"Spectators":(.+?),"League":(.+?),"HomeTeam":(.+?),"HomeTeam_Id":(.+?),"HomeCorners":(.+?),"HomeGoals":(.+?),"HalfTimeHomeGoals":(.+?),"HomeShots":(.+?),"HomeShotsOnTarget":(.+?),"HomeFouls":(.+?),"HomeGoalDetails":(.+?),"HomeLineupGoalkeeper":(.+?),"HomeLineupDefense":(.+?),"HomeLineupMidfield":(.+?),"HomeLineupForward":(.+?),"HomeLineUpSubstitutes":(.+?),"HomeLineUpCoach":(.+?),"HomeYellowCards":(.+?),"HomeRedCards":(.+?),"HomeTeamFormation":(.+?),"AwayTeam":(.+?),"AwayTeam_Id":(.+?),"AwayCorners":(.+?),"AwayGoals":(.+?),"HalfTimeAwayGoals":(.+?),"AwayShots":(.+?),"AwayShotsOnTarget":(.+?),"AwayFouls":(.+?),"AwayGoalDetails":(.+?),"AwayLineupGoalkeeper":(.+?),"AwayLineupDefense":(.+?),"AwayLineupMidfield":(.+?),"AwayLineupForward":(.+?),"AwayLineUpSubstitutes":(.+?),"AwayLineUpCoach":(.+?),"AwayYellowCards":(.+?),"AwayRedCards":(.+?),"AwayTeamFormation":(.+?),"HomeTeamYellowCardDetails":(.+?),"AwayTeamYellowCardDetails":(.+?),"HomeTeamRedCardDetails":(.+?),"AwayTeamRedCardDetails":(.+?),"HomeSubDetails":(.+?),"AwaySubDetails":(.+?),"Referee":"(.+?)"}' , re . DOTALL ) . findall ( str ( ooOooo000oOO ) )
 for Iiii , OO0OoO0o00 , ooOO0O0ooOooO , oOOOo00O00oOo , iiIIIi , ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo , oo0OOo , ooOOO00Ooo , IiIIIi1iIi , ooOOoooooo , II1I , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo , o0O0OOO0Ooo , iiIiI , I1 , OOO00O0O , iii , oOooOOOoOo , i1Iii1i1I , OOoO00 , IiI111111IIII , i1Ii , ii111iI1iIi1 , OOO , oo0OOo0 , I11IiI , O0ooO0Oo00o , ooO0oOOooOo0 , i1I1ii11i1Iii , I1IiiiiI , o0O , IiIIii1iII1II , Iii1I1I11iiI1 , I1I1i1I , ii1I , O0oO0 , oO0 , O0OO0O , OOOoOoO , Ii1I1i , OOI1iI1ii1II , O0O0OOOOoo , oOooO0 , Ii1I1Ii , OOoO0 in Oo0oOOo :
  Ii1I1IIii1II = 'Date: ' + ooOO0O0ooOooO + '[CR]HomeTeam: ' + O00OOOoOoo0O + '[CR]HomeGoals: ' + ooOOO00Ooo + '[CR]AwayTeam: ' + IiI111111IIII + '[CR]AwayGoals: ' + OOO + '[CR]Round: ' + oOOOo00O00oOo + '[CR]Spectators: ' + iiIIIi + '[CR]League: ' + ooo00OOOooO + '[CR]HomeCorners: ' + oo0OOo + '[CR]HalfTimeHomeGoals: ' + IiIIIi1iIi + '[CR]HomeShots: ' + ooOOoooooo + '[CR]HomeShotsOnTarget: ' + II1I + '[CR]HomeFouls: ' + O0i1II1Iiii1I11 + '[CR]HomeGoalDetails: ' + IIIIiiIiI + '[CR]HomeLineupGoalkeeper: ' + o00oooO0Oo + '[CR]HomeLineupDefense: ' + o0O0OOO0Ooo + '[CR]HomeLineupMidfield: ' + iiIiI + '[CR]HomeLineupForward: ' + I1 + '[CR]HomeLineUpSubstitutes: ' + OOO00O0O + '[CR]HomeLineUpCoach: ' + iii + '[CR]HomeYellowCards: ' + oOooOOOoOo + '[CR]HomeRedCards: ' + i1Iii1i1I + '[CR]HomeTeamFormation: ' + OOoO00 + '[CR]AwayCorners: ' + ii111iI1iIi1 + '[CR]HalfTimeAwayGoals: ' + oo0OOo0 + '[CR]AwayShots: ' + I11IiI + '[CR]AwayShotsOnTarget: ' + O0ooO0Oo00o + '[CR]AwayFouls: ' + ooO0oOOooOo0 + '[CR]AwayGoalDetails: ' + i1I1ii11i1Iii + '[CR]AwayLineupGoalkeeper: ' + I1IiiiiI + '[CR]AwayLineupDefense: ' + o0O + '[CR]AwayLineupMidfield: ' + IiIIii1iII1II + '[CR]AwayLineupForward: ' + Iii1I1I11iiI1 + '[CR]AwayLineUpSubstitutes: ' + I1I1i1I + '[CR]AwayLineUpCoach: ' + ii1I + '[CR]AwayYellowCards: ' + O0oO0 + '[CR]AwayRedCards: ' + oO0 + '[CR]AwayTeamFormation: ' + O0OO0O + '[CR]HomeTeamYellowCardDetails: ' + OOOoOoO + '[CR]AwayTeamYellowCardDetails: ' + Ii1I1i + '[CR]HomeTeamRedCardDetails: ' + OOI1iI1ii1II + '[CR]AwayTeamRedCardDetails: ' + O0O0OOOOoo + '[CR]HomeSubDetails: ' + oOooO0 + '[CR]AwaySubDetails: ' + Ii1I1Ii + '[CR]Referee: ' + OOoO0 + '\n'
  O0O00o0OOO0 ( ( '[COLORorangered]' + O00OOOoOoo0O + '[COLORsteelblue] Vs [COLORorangered]' + IiI111111IIII + '[COLORsteelblue] ' + ooOOO00Ooo + ':' + OOO + '[/COLOR]' ) . replace ( '"' , '' ) , '' , 34 , i1 + 'match_stats.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( Ii1I1IIii1II ) . replace ( '{}' , 'N/A' ) . replace ( '\\' , '' ) . replace ( "'" , '' ) . replace ( '"' , '' ) + '[/COLOR]' )
def OO0Oooo0oOO0O ( name , description ) :
 name = name
 ii1i1I1i = description
 o00oOO0 ( name , ii1i1I1i )
 if 62 - 62: iI1I
 if 100 - 100: IIII - O0 % iii1I1 * III1I11iiii1I + iI1I
def Oo0O0oooo ( ) :
 I111iI = [ '[COLORsteelblue]FootBall Source 1[/COLOR]' , '[COLORsteelblue]FootBall Source 2[/COLOR]' , '[COLORsteelblue]FootBall Source 3[/COLOR]' , '[COLORsteelblue]F1[/COLOR]' , '[COLORsteelblue]NFL[/COLOR]' ]
 oOOo0 = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Select Source[/COLOR]' , I111iI )
 if oOOo0 == 0 :
  II1I1iiIII ( )
 if oOOo0 == 1 :
  oOOo0O00o ( )
 if oOOo0 == 2 :
  iIiIi11 ( )
 if oOOo0 == 3 :
  OOOiiiiI ( )
 if oOOo0 == 4 :
  oooOo0OOOoo0 ( )
  if 51 - 51: iiiIi / i1I111I . III1I11iiii1I * I1I1IIiiIiI1 + OO * ii1I11II1ii1i
def II1I1iiIII ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 o0 = Ii11Ii1I ( 'http://www.eplsite.com/' )
 ooOooo000oOO = re . compile ( '<h4>FOOTBALL LIVE STREAMS</h4>(.+?)</section>' , re . DOTALL ) . findall ( o0 )
 Oo0oOOo = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="vs  "><span>(.+?)</span><div class="accordion-time">(.+?)</div></div>.+?<div class="acoordian-right-section">(.+?)</div>.+?<p>(.+?)</p>.+?<p>(.+?)</p>(.+?)<center>' , re . DOTALL ) . findall ( str ( ooOooo000oOO ) )
 for OOOoOo , O00o0 , time , I11iII , iIIII , oOOOoo0O0OoO , I11iI1i1I11I11 in Oo0oOOo :
  o000O0O = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + ( iIIII ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( iIIII ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + OOOoOo + ' ' + O00o0 + ' ' + I11iII + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for oO0Oo , I11i1I1I , I1i1i1iii in o000O0O :
   I1111i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + I11i1I1I
   O0O00o0OOO0 ( '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' , I1111i , 15 , 'http://www.eplsite.com/' + oO0Oo , Oo0o0000o0o0 , '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' )
   if 14 - 14: III1I11iiii1I / I1I1IIiiIiI1
def oOOo0O00o ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 o0 = Ii11Ii1I ( 'http://www.abcast.me/' )
 ooOooo000oOO = re . compile ( '</thead>(.+?)</html>' , re . DOTALL ) . findall ( o0 )
 Oo0oOOo = re . compile ( '<td> (.+?) </td>.+?</strong>.+?<td>(.+?)</td>.+?href="(.+?)">' , re . DOTALL ) . findall ( str ( ooOooo000oOO ) )
 for iIIII , oOOOoo0O0OoO , I11i1I1I in Oo0oOOo :
  I1111i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + I11i1I1I
  O0O00o0OOO0 ( '[COLORorangered]' + iIIII + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , I1111i , 15 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + iIIII + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
  if 32 - 32: iI1I * iiiIi
def iIiIi11 ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 o0 = Ii11Ii1I ( 'http://www.sports-stream.net/schedule.html' )
 O0OooOo0o = re . compile ( '<font color="red"><h3>(.+?)<input onclick=(.+?)<br>' , re . DOTALL ) . findall ( o0 )
 for iiI11ii1I1 , I11iI1i1I11I11 in O0OooOo0o :
  Oo0oOOo = re . compile ( 'style="color:#FF0000;">(.+?)</span>(.+?) - <a href="(.+?)" ' , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + ( iiI11ii1I1 ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( iiI11ii1I1 ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for time , oOOOoo0O0OoO , I11i1I1I in Oo0oOOo :
   I1111i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + I11i1I1I
   O0O00o0OOO0 ( '[COLORorangered]' + time + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , I1111i , 15 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + time + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
   if 82 - 82: II111iiii % IiI1i11iii1 / OO + i1I111I / I1I1IIiiIiI1 / I1i1iii
   if 70 - 70: iii1I1
def OOOiiiiI ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Race Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 o0 = Ii11Ii1I ( 'http://www.eplsite.com/f1.html' )
 ooOooo000oOO = re . compile ( '<h4>F1 Live Streams</h4>(.+?)</section>' , re . DOTALL ) . findall ( o0 )
 Oo0oOOo = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="accordion-time">(.+?)</div></div>.+?<p>(.+?)</p>(.+?)</header>' , re . DOTALL ) . findall ( str ( ooOooo000oOO ) )
 for OOOoOo , time , oOOOoo0O0OoO , I11iI1i1I11I11 in Oo0oOOo :
  o000O0O = re . compile ( '<a href="(.+?)".+?target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + ( OOOoOo ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( OOOoOo ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + oOOOoo0O0OoO + '[/COLOR]' , '' , '' , i1 + 'f1.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for I11i1I1I , I1i1i1iii in o000O0O :
   I1111i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + I11i1I1I
   if 'bitcoin' in I11i1I1I :
    pass
   else :
    O0O00o0OOO0 ( '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' , I1111i , 15 , i1 + 'f1.jpg' , Oo0o0000o0o0 , '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' )
    if 59 - 59: I1I1IIiiIiI1 % iii1I1
def oooOo0OOOoo0 ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Game Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 o0 = Ii11Ii1I ( 'http://www.eplsite.com/nfl.html' )
 ooOooo000oOO = re . compile ( '<h4>NFL Live Streams</h4>(.+?)</section>' , re . DOTALL ) . findall ( o0 )
 Oo0oOOo = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="vs"><span>(.+?)</span><div class="accordion-time">(.+?)</div></div>.+?<div class="acoordian-right-section">(.+?)</div>.+?<p>(.+?)</p>(.+?)</b></p>' , re . DOTALL ) . findall ( str ( ooOooo000oOO ) )
 for OOOoOo , O00o0 , time , I11iII , oOOOoo0O0OoO , I11iI1i1I11I11 in Oo0oOOo :
  o000O0O = re . compile ( '<a href="(.+?)".+?target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + OOOoOo + ' ' + O00o0 + ' ' + I11iII + '[/COLOR]' , '' , '' , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + oOOOoo0O0OoO + '[/COLOR]' , '' , '' , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for I11i1I1I , I1i1i1iii in o000O0O :
   I1111i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + I11i1I1I
   if 'bitcoin' in I11i1I1I :
    pass
   else :
    O0O00o0OOO0 ( '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' , I1111i , 15 , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' )
    if 6 - 6: iIii1I11I1II1 % i11iIiiIii % iiIiIIi
def o0Oo0oO0oOO00 ( ) :
 oo00OO0000oO = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 o0 = requests . get ( I11i1I1I ) . content
 Oo0oOOo = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( o0 )
 ooOooo000oOO = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( Oo0oOOo ) )
 for I1II1 , oOOOoo0O0OoO in ooOooo000oOO :
  if not oOOOoo0O0OoO == 'Home' :
   pass
   oooO = 'http://www.replaymatches.com/' + I1II1
   if oOOOoo0O0OoO in oo00OO0000oO :
    oOOO00o ( '[COLORred]' + oOOOoo0O0OoO + '[/COLOR]' , oooO , 900301 , i1 + 'football.jpg' , '' , '' )
   else :
    oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , oooO , 900301 , i1 + 'football.jpg' , '' , '' )
    if 26 - 26: IIII % iiIiIIi
def o00Oo0oooooo ( url ) :
 if 76 - 76: IiI1i11iii1 / III1I11iiii1I . O0 % iI1I . I1I1IIiiIiI1 + ii1I11II1ii1i
 o0O0o0Oo = Ii11Ii1I ( url )
 o0o = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( o0O0o0Oo )
 oo0 = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( o0O0o0Oo )
 for url , oOOOoo0O0OoO , oO0Oo in o0o :
  oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , url , 900302 , oO0Oo , i1 + 'football.jpg' , '' )
 for oOOOoo00 in oo0 :
  oOOO00o ( '[COLORorangered]NEXT PAGE[/COLOR]' , oOOOoo00 , 900301 , i1 + 'NEXT.png' , '' , '' )
def iiIiIIIiiI ( url ) :
 o0 = requests . get ( url ) . content
 Oo0oOOo = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( o0 )
 for I1II1 , oO0Oo in Oo0oOOo :
  if 'Highlight' in oO0Oo :
   oOOOoo0O0OoO = 'HighLights'
  elif '1st' in oO0Oo :
   oOOOoo0O0OoO = '1st Half'
  elif '2nd' in oO0Oo :
   oOOOoo0O0OoO = '2nd Half'
  else :
   oOOOoo0O0OoO = 'Full Match'
  iiI1IIIi ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , I1II1 , 1001111 , oO0Oo , i1 + 'football.jpg' , '' , '' )
def II11IiIi11 ( ) :
 o0 = requests . get ( O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 Oo0oOOo = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( o0 )
 for IIOOO0O00O0OOOO , I11iI1i1I11I11 in Oo0oOOo :
  I1iiii1I ( '[COLORred]' + IIOOO0O00O0OOOO + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , i1 + 'football.jpg' , '' , '' )
  OOo0 = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  for oO00ooooO0o , oo0o in OOo0 :
   I1iiii1I ( '[COLORorangered]' + oO00ooooO0o + '[/COLOR]' , '' , '' , oo0o , i1 + 'football.jpg' , '' , '' )
def o0oO0oooOoo ( name , url ) :
 import urlresolver
 try :
  I1III1111iIi = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( I1III1111iIi , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 38 - 38: o0O0 + IiI1i11iii1 / I1i1iii % IiiI11Iiiii - iiIiIIi
 if 14 - 14: iii1I1 / I1i1iii
def ooo0O0o00O ( url ) :
 o0O0o0Oo = Ii11Ii1I ( url )
 O00oO = re . compile ( '<h1>(.+?)</h1>.+?<a class="nostyle" href="([^"]*)"' , re . DOTALL ) . findall ( o0O0o0Oo )
 for oOOOoo0O0OoO , url in O00oO :
  if 'Sport' in oOOOoo0O0OoO :
   I1i11 ( url )
def IiIi1I1 ( url ) :
 if url == 'http://' : return False
 try :
  IiIIi1 = urllib2 . Request ( url )
  IiIIi1 . add_header ( 'User-Agent' , iIiiiI )
  IIIIiii1IIii = urllib2 . urlopen ( IiIIi1 )
  IIIIiii1IIii . close ( )
 except Exception , II1i11I :
  return II1i11I
 return True
def ii1I1IIii11 ( name , url ) :
 if 67 - 67: o0O0 + IiI1i11iii1 / I1I1IIiiIiI1 . iii1I1 + III1I11iiii1I
 if 62 - 62: i11iIiiIii + i11iIiiIii - I1I1IIiiIiI1
 if 28 - 28: o0O0 . o0O0 % iIii1I11I1II1 * iIii1I11I1II1 . I1I1IIiiIiI1 / o0O0
 if 27 - 27: OO + IiiI11Iiiii - i1IIi
 if 69 - 69: ii1I11II1ii1i - O0 % iiIiIIi + i11iIiiIii . i1I111I / OO
 OoOoo00Ooo00 = name
 o0O0o0Oo = Ii11Ii1I ( url )
 Oo0oOOo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 o000O0O = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 oo0O00Oooo0O0 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 I11OO = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 o0O0oo0OO0O = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( o0O0o0Oo )
 OO0 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 for name , oO0Oo , o0Oooo , I1i1i1iii , url in Oo0oOOo :
  if OoOoo00Ooo00 in o0Oooo :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( name + I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oO0Oo , oO0Oo , ( '[COLORsteelblue]' + ( name + I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO0Oo , o0Oooo , I1i1i1iii , url in o000O0O :
  if OoOoo00Ooo00 in o0Oooo :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oO0Oo , oO0Oo , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0Oooo , I1i1i1iii , url in oo0O00Oooo0O0 :
  if OoOoo00Ooo00 in o0Oooo :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0Oooo , oO0Oo , I1i1i1iii , url in I11OO :
  if OoOoo00Ooo00 in o0Oooo :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oO0Oo , oO0Oo , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for I1i1i1iii , url in o0O0oo0OO0O :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0Oooo , I1i1i1iii , url in OO0 :
  if OoOoo00Ooo00 in o0Oooo :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
def iiI ( name , url ) :
 o0O0o0Oo = Ii11Ii1I ( url )
 oOIIiIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 for I1i1i1iii , url in oOIIiIi :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 91 - 91: iiIiIIi * iiiIi / iI1I . O0 + OO + i1I111I
def I1i11 ( url ) :
 url = url
 I111iI = [ '[COLORsteelblue](_) _No Group[/COLOR]' , '[COLORsteelblue](UK) United Kingdom[/COLOR]' , '[COLORsteelblue](US) United States[/COLOR]' , '[COLORsteelblue](AL) Albania[/COLOR]' , '[COLORsteelblue](AS) American Samoa[/COLOR]' , '[COLORsteelblue](AR) Argentina[/COLOR]' , '[COLORsteelblue](AU) Australia[/COLOR]' , '[COLORsteelblue](AZ) Azerbaijan[/COLOR]' , '[COLORsteelblue](BY) Belarus[/COLOR]' , '[COLORsteelblue](BE) Belgium[/COLOR]' , '[COLORsteelblue](BO) Bolivia[/COLOR]' , '[COLORsteelblue](BR) Brazil[/COLOR]' , '[COLORsteelblue](CM) Cameroon[/COLOR]' , '[COLORsteelblue](CA) Canada[/COLOR]' , '[COLORsteelblue](CO) Colombia[/COLOR]' , '[COLORsteelblue](CZ) Czech Republic[/COLOR]' , '[COLORsteelblue](DO) Dominican Republic[/COLOR]' , '[COLORsteelblue](EC) Ecuador[/COLOR]' , '[COLORsteelblue](FO) Faroe Islands[/COLOR]' , '[COLORsteelblue](FR) France[/COLOR]' , '[COLORsteelblue](DE) Germany[/COLOR]' , '[COLORsteelblue](GR) Greece[/COLOR]' , '[COLORsteelblue](IS) Iceland[/COLOR]' , '[COLORsteelblue](IN) India[/COLOR]' , '[COLORsteelblue](ID) Indonesia[/COLOR]' , '[COLORsteelblue](IR) Iran[/COLOR]' , '[COLORsteelblue](IT) Italy[/COLOR]' , '[COLORsteelblue](LA) Laos[/COLOR]' , '[COLORsteelblue](MO) Macau[/COLOR]' , '[COLORsteelblue](MX) Mexico[/COLOR]' , '[COLORsteelblue](NL) Netherlands[/COLOR]' , '[COLORsteelblue](NE) Niger[/COLOR]' , '[COLORsteelblue](PK) Pakistan[/COLOR]' , '[COLORsteelblue](PA) Panama[/COLOR]' , '[COLORsteelblue](PE) Peru[/COLOR]' , '[COLORsteelblue](PL) Poland[/COLOR]' , '[COLORsteelblue](PT) Portugal[/COLOR]' , '[COLORsteelblue](RO) Romania[/COLOR]' , '[COLORsteelblue](RU) Russia[/COLOR]' , '[COLORsteelblue](SL) Sierra Leone[/COLOR]' , '[COLORsteelblue](EX-YU) Slovenia[/COLOR]' , '[COLORsteelblue](SO) Somalia[/COLOR]' , '[COLORsteelblue](SP) Spain[/COLOR]' , '[COLORsteelblue](SE) Sweden[/COLOR]' , '[COLORsteelblue](CH) Switzerland[/COLOR]' , '[COLORsteelblue](TH) Thailand[/COLOR]' , '[COLORsteelblue](TR) Turkey[/COLOR]' , '[COLORsteelblue](UA) Ukraine[/COLOR]' , '[COLORsteelblue](VE) Venezuela[/COLOR]' , '[COLORsteelblue](WW) World Wide[/COLOR]' ]
 oOOo0 = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Select Country[/COLOR]' , I111iI )
 if oOOo0 == 0 :
  oOOOoo0O0OoO = '(_)'
 if oOOo0 == 1 :
  oOOOoo0O0OoO = '(UK)'
 if oOOo0 == 2 :
  oOOOoo0O0OoO = '(US)'
 if oOOo0 == 3 :
  oOOOoo0O0OoO = '(AL)'
 if oOOo0 == 4 :
  oOOOoo0O0OoO = '(AS)'
 if oOOo0 == 5 :
  oOOOoo0O0OoO = '(AR)'
 if oOOo0 == 6 :
  oOOOoo0O0OoO = '(AU)'
 if oOOo0 == 7 :
  oOOOoo0O0OoO = '(AZ)'
 if oOOo0 == 8 :
  oOOOoo0O0OoO = '(BY)'
 if oOOo0 == 9 :
  oOOOoo0O0OoO = '(BE)'
 if oOOo0 == 10 :
  oOOOoo0O0OoO = '(BO)'
 if oOOo0 == 11 :
  oOOOoo0O0OoO = '(BR)'
 if oOOo0 == 12 :
  oOOOoo0O0OoO = '(CM)'
 if oOOo0 == 13 :
  oOOOoo0O0OoO = '(CA)'
 if oOOo0 == 14 :
  oOOOoo0O0OoO = '(CO)'
 if oOOo0 == 15 :
  oOOOoo0O0OoO = '(CZ)'
 if oOOo0 == 16 :
  oOOOoo0O0OoO = '(DO)'
 if oOOo0 == 17 :
  oOOOoo0O0OoO = '(EC)'
 if oOOo0 == 18 :
  oOOOoo0O0OoO = '(FO)'
 if oOOo0 == 19 :
  oOOOoo0O0OoO = '(FR)'
 if oOOo0 == 20 :
  oOOOoo0O0OoO = '(DE)'
 if oOOo0 == 21 :
  oOOOoo0O0OoO = '(GR)'
 if oOOo0 == 22 :
  oOOOoo0O0OoO = '(IS)'
 if oOOo0 == 23 :
  oOOOoo0O0OoO = '(IN)'
 if oOOo0 == 24 :
  oOOOoo0O0OoO = '(ID)'
 if oOOo0 == 25 :
  oOOOoo0O0OoO = '(IR)'
 if oOOo0 == 26 :
  oOOOoo0O0OoO = '(IT)'
 if oOOo0 == 27 :
  oOOOoo0O0OoO = '(LA)'
 if oOOo0 == 28 :
  oOOOoo0O0OoO = '(MO)'
 if oOOo0 == 29 :
  oOOOoo0O0OoO = '(MX)'
 if oOOo0 == 30 :
  oOOOoo0O0OoO = '(NL)'
 if oOOo0 == 31 :
  oOOOoo0O0OoO = '(NE)'
 if oOOo0 == 32 :
  oOOOoo0O0OoO = '(PK)'
 if oOOo0 == 33 :
  oOOOoo0O0OoO = '(PA)'
 if oOOo0 == 34 :
  oOOOoo0O0OoO = '(PE)'
 if oOOo0 == 35 :
  oOOOoo0O0OoO = '(PL)'
 if oOOo0 == 36 :
  oOOOoo0O0OoO = '(PT)'
 if oOOo0 == 37 :
  oOOOoo0O0OoO = '(RO)'
 if oOOo0 == 38 :
  oOOOoo0O0OoO = '(RU)'
 if oOOo0 == 39 :
  oOOOoo0O0OoO = '(SL)'
 if oOOo0 == 40 :
  oOOOoo0O0OoO = '(EX-YU)'
 if oOOo0 == 41 :
  oOOOoo0O0OoO = '(SO)'
 if oOOo0 == 42 :
  oOOOoo0O0OoO = '(SP)'
 if oOOo0 == 43 :
  oOOOoo0O0OoO = '(SE)'
 if oOOo0 == 44 :
  oOOOoo0O0OoO = '(CH)'
 if oOOo0 == 45 :
  oOOOoo0O0OoO = '(TH)'
 if oOOo0 == 46 :
  oOOOoo0O0OoO = '(TR)'
 if oOOo0 == 47 :
  oOOOoo0O0OoO = '(UA)'
 if oOOo0 == 48 :
  oOOOoo0O0OoO = '(VE)'
 if oOOo0 == 49 :
  oOOOoo0O0OoO = '(WW)'
 ii1I1IIii11 ( oOOOoo0O0OoO , url )
 if 8 - 8: iii1I1 / iiIiIIi
def i1iI1 ( url ) :
 o0O0o0Oo = Ii11Ii1I ( url )
 Oo0oOOo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 o000O0O = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 oo0O00Oooo0O0 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 I11OO = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 o0O0oo0OO0O = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( o0O0o0Oo )
 OO0 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 oOIIiIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( o0O0o0Oo )
 for oOOOoo0O0OoO , oO0Oo , o0Oooo , I1i1i1iii , url in Oo0oOOo :
  if 'INFO' in o0Oooo :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oOOOoo0O0OoO + I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oO0Oo , oO0Oo , ( '[COLORsteelblue]' + ( oOOOoo0O0OoO + I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO0Oo , o0Oooo , I1i1i1iii , url in o000O0O :
  if 'INFO' in o0Oooo :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oO0Oo , oO0Oo , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0Oooo , I1i1i1iii , url in oo0O00Oooo0O0 :
  if 'INFO' in o0Oooo :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0Oooo , oO0Oo , I1i1i1iii , url in I11OO :
  if 'INFO' in o0Oooo :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , oO0Oo , oO0Oo , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for I1i1i1iii , url in o0O0oo0OO0O :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for o0Oooo , I1i1i1iii , url in OO0 :
  if 'INFO' in o0Oooo :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + o0Oooo + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for I1i1i1iii , url in oOIIiIi :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( I1i1i1iii ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 33 - 33: ii1I11II1ii1i % iIii1I11I1II1 * iI1I
def o00o0 ( url ) :
 if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
  RESOLVEtest ( ( url ) . strip ( ) )
 else :
  try :
   II1III1I1I1Ii ( ( url ) . strip ( ) )
  except :
   pass
  else :
   II1III1I1I1Ii ( 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + url )
   if 70 - 70: OO % iii1I1 + III1I11iiii1I / IIII % O0
def oO00O0 ( url ) :
 o0O0o0Oo = cloudflare . source ( url )
 ooOooo000oOO = re . compile ( 'class="footer-univers">.+?<h2 class="tag-sport.+?>(.+?)</h2>(.+?)</span>' , re . DOTALL ) . findall ( o0O0o0Oo )
 for oOOOoo0O0OoO , I11iI1i1I11I11 in ooOooo000oOO :
  Oo0oOOo = re . compile ( '<a href="([^"]*)">.+?<h3>(.+?)</h3>' , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  O0O00o0OOO0 ( ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '\n' , ' ' ) . replace ( '_' , ' ' ) . replace ( ' ' , '' ) , '' , '' , i1 + 'extreme.jpg' , Oo0o0000o0o0 , ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( ' ' , '' ) )
  for I1II1 , iiI11ii1I1 in Oo0oOOo :
   oOOO00o ( ( '[COLORsteelblue]' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '-' ) . replace ( '' , '' ) . replace ( '\n' , ' ' ) , 'https://www.ridersmatch.com' + I1II1 , 21 , i1 + 'extreme.jpg' , Oo0o0000o0o0 , ( '[COLORsteelblue]' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '-' ) . replace ( '' , '' ) . replace ( '\n' , ' ' ) )
   if 36 - 36: iii1I1 - IIII . iiiIi - i11iIiiIii - III1I11iiii1I * iiiIi
def OooOOOO ( url ) :
 o0O0o0Oo = cloudflare . source ( url )
 Oo0oOOo = re . compile ( 'list-videothumbnail" href="(.+?)".+?title="(.+?)".+?style=".+?url(.+?)"' , re . DOTALL ) . findall ( o0O0o0Oo )
 oOOOoo00 = re . compile ( '<a class="page-link nex" href="([^"]*)">Next</a>' , re . DOTALL ) . findall ( o0O0o0Oo )
 for url , oOOOoo0O0OoO , oO0Oo in Oo0oOOo :
  oO0Oo = oO0Oo . replace ( '(' , '' ) . replace ( ')' , '' )
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '' ) . replace ( '_' , ' ' ) . replace ( '\n' , ' ' ) , 'https://www.ridersmatch.com' + url , 23 , oO0Oo , Oo0o0000o0o0 , ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '' ) . replace ( '_' , ' ' ) . replace ( '\n' , ' ' ) )
 for url in oOOOoo00 :
  oOOO00o ( ( '[COLORorangered]Next Page[/COLOR]' ) . replace ( '_' , ' ' ) , 'https://www.ridersmatch.com' + url , 21 , oO0Oo , Oo0o0000o0o0 , '[COLORorangered]Next Page[/COLOR]' )
  if 45 - 45: iiIiIIi % iI1I - i11iIiiIii
def ii1iiIiIII1ii ( url ) :
 o0 = cloudflare . source ( url )
 Oo0oOOo = re . compile ( 'src="//www.youtube.com/embed/(.+?)"' , re . DOTALL ) . findall ( o0 )
 for url in Oo0oOOo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 82 - 82: o0O0
  if 65 - 65: IiiI11Iiiii . OoooooooOO / iiIiIIi . i1IIi * OO
def IiIiII1 ( url ) :
 o0O0o0Oo = Ii11Ii1I ( url )
 O00oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0O0o0Oo )
 for url , oO0Oo , ii1i1I1i , OO00Oo , oOOOoo0O0OoO in O00oO :
  if '.php' in url :
   oOOO00o ( oOOOoo0O0OoO , url , 211 , oO0Oo , OO00Oo , ii1i1I1i )
  else :
   oOOO00o ( oOOOoo0O0OoO , url , 212 , oO0Oo , OO00Oo , ii1i1I1i )
def Iii1iiIi1II ( url , iconimage ) :
 oO0Oo = iconimage
 IIIIiii1IIii = oo0o0O00 . open ( url ) . read ( )
 if 60 - 60: iI1I - iii1I1 * IiI1i11iii1 % II111iiii
 try :
  ooo = re . findall ( r'<a .*?>(.*?)</a>' , IIIIiii1IIii )
  IIiIiI1I = re . findall ( r'<a.*?href="(.*?)">' , IIIIiii1IIii )
  if 100 - 100: iIii1I11I1II1 + i1I111I / iiiIi . i11iIiiIii
  for I1II1 in IIiIiI1I :
   if '.gif' in I1II1 :
    pass
   if '.srt' in I1II1 :
    pass
   elif '..' in I1II1 :
    pass
   elif '.txt' in I1II1 :
    pass
   elif '.nfo' in I1II1 :
    pass
   elif '.jpg' in I1II1 :
    pass
   elif '1-Irani/' in I1II1 :
    pass
   elif 'index.php' in I1II1 :
    pass
   elif '.png' in I1II1 :
    pass
   elif '?C=M&O=D' in I1II1 :
    pass
   elif '?C=M&O=A' in I1II1 :
    pass
   elif '?C=N&O=D' in I1II1 :
    pass
   elif '?C=N&O=A' in I1II1 :
    pass
   elif '?C=S&O=A' in I1II1 :
    pass
   elif '?C=S&O=D' in I1II1 :
    pass
   elif '?C=N;O=D' in I1II1 :
    pass
   elif '?C=M;O=A' in I1II1 :
    pass
   elif '?C=S;O=A' in I1II1 :
    pass
   elif '?C=D;O=A' in I1II1 :
    pass
   elif 'Torrent' in I1II1 :
    pass
   elif 'exe' in I1II1 :
    pass
   elif 'public' in I1II1 :
    pass
   elif '?C=D;O=A' in I1II1 :
    pass
   elif 'pub' in I1II1 :
    pass
   elif 'install' in I1II1 :
    pass
   elif '?C=D;O=A' in I1II1 :
    pass
   elif '?C=D;O=A' in I1II1 :
    pass
   elif '.m3u' in I1II1 :
    pass
   elif '?C=D;O=A' in I1II1 :
    pass
   elif 'mpeg' in I1II1 :
    pass
   elif '.doc' in I1II1 :
    pass
   elif '.html' in I1II1 :
    pass
   elif 'boss' in I1II1 :
    pass
   elif 'plex' in I1II1 :
    pass
   else :
    oOOOoo0O0OoO = I1II1
    if 'txt' in oOOOoo0O0OoO :
     pass
    if '.' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( '.' , ' ' )
    if '_' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( '_' , ' ' )
    if '%20' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( '%20' , ' ' )
    if '/' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( '/' , '' )
    if 'mkv' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'mkv' , '' )
    if 'avi' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'avi' , '' )
    if 'mp4' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'mp4' , '' )
    if 'Tehmovies' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'Tehmovies' , '' )
    if 'h264' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'h264' , '' )
    if 'WEB' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'WEB' , '' )
    if 'HEEL' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( '-HEEL' , '' )
    if 'MeGusta' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'MeGusta' , '' )
    if 'x264' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'x264' , '' )
    if 'x265' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'x265' , '' )
    if 'HDTV' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'HDTV' , '' )
    if '-Ebi' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( '-Ebi' , '' )
    if '-' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( '-' , '' )
    if 'NWCHD' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'NWCHD' , '' )
    if 'FMN' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'FMN' , '' )
    if 'PLUTONiUM' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'PLUTONiUM' , '' )
    if 'H264' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'H264' , '' )
    if 'H265' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'H265' , '' )
    if 'WD' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'WD' , '' )
    if 'hdtv' in oOOOoo0O0OoO :
     oOOOoo0O0OoO = oOOOoo0O0OoO . replace ( 'hdtv' , '' )
     if 14 - 14: I1I1IIiiIiI1 * III1I11iiii1I + o0O0 + O0 + i11iIiiIii
     if 77 - 77: I1I1IIiiIiI1 / OoooooooOO
    if '.mkv' in I1II1 or '.m4B' in I1II1 or '.m4v' in I1II1 or '.mp3' in I1II1 or '.mp4' in I1II1 or '.avi' in I1II1 or '.flv' in I1II1 or '.mpeg' in I1II1 or '.3gp' in I1II1 or '.divx' in I1II1 or '.strm' in I1II1 :
     IIii11I1i1I ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , url + I1II1 , 222 , oO0Oo , OO00Oo , '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
     if 99 - 99: o0O0
    else :
     oOOO00o ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , url + I1II1 , 212 , oO0Oo , OO00Oo , '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
     if 76 - 76: OO * iI1I
     if 82 - 82: IIII * o0O0 / iiIiIIi
     if 36 - 36: OoooooooOO - i1IIi . O0 / II111iiii + I1I1IIiiIiI1
     if 33 - 33: II111iiii / IiiI11Iiiii * O0 % IIII * I1i1iii
 except Exception , II1i11I :
  print str ( II1i11I )
def O0o ( name , url , mode , iconimage , description = "" , isFolder = True , background = None ) :
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 if 28 - 28: IiiI11Iiiii + i11iIiiIii / IiI1i11iii1 % i1I111I % iiiIi - O0
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 if background :
  ooo0OOO . setProperty ( 'fanart_image' , background )
 if mode == 1 or mode == 2 :
  ooo0OOO . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10008 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=22)' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) ) ) ] )
 elif mode == 404 :
  ooo0OOO . setProperty ( 'IsPlayable' , 'true' )
  ooo0OOO . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10009 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
 elif mode == 556 :
  ooo0OOO . setProperty ( 'IsPlayable' , 'true' )
  ooo0OOO . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10010 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
  if 49 - 49: i11iIiiIii % IIII . i1I111I
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = isFolder )
 if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - II111iiii * III1I11iiii1I
def iiIi1iI1iIii ( handle , url , listitem , isFolder ) :
 if 68 - 68: III1I11iiii1I
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 82 - 82: iIii1I11I1II1 + iiiIi . iIii1I11I1II1 % ii1I11II1ii1i / IIII . IIII
 if 14 - 14: I1I1IIiiIiI1 . III1I11iiii1I . IiI1i11iii1 + OoooooooOO - III1I11iiii1I + ii1I11II1ii1i
 if 9 - 9: IIII
def oooooOOO000Oo ( title , message , times = 2000 , icon = o0oOoO00o ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def Ooo00OoOOO ( ) :
 Oo0OO0000oooo = IIII1iII ( )
 ii1III11 = Oo0OO0000oooo . replace ( I1ii11iIi11i , "" )
 if os . path . exists ( Oo0OO0000oooo ) or not Oo0OO0000oooo == False :
  I1iiIIIi11 = open ( Oo0OO0000oooo , mode = 'r' ) ; Ii1I11ii1i = I1iiIIIi11 . read ( ) ; I1iiIIIi11 . close ( )
  O0iIiIIIIIii ( "%s - %s" % ( IiII , ii1III11 ) , Ii1I11ii1i )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def IIII1iII ( ) :
 OOo0ii11I1 = False
 if os . path . exists ( os . path . join ( I1ii11iIi11i , 'xbmc.log' ) ) :
  OOo0ii11I1 = os . path . join ( I1ii11iIi11i , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'kodi.log' ) ) :
  OOo0ii11I1 = os . path . join ( I1ii11iIi11i , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'spmc.log' ) ) :
  OOo0ii11I1 = os . path . join ( I1ii11iIi11i , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'tvmc.log' ) ) :
  OOo0ii11I1 = os . path . join ( I1ii11iIi11i , 'tvmc.log' )
 return OOo0ii11I1
 if 75 - 75: OO / II111iiii % O0
 if 38 - 38: OoooooooOO * IiiI11Iiiii % O0 * i1I111I
 if 29 - 29: iiIiIIi / i1IIi . iI1I - i1I111I - i1I111I - IIII
 if 20 - 20: i1IIi % OO . iI1I / ii1I11II1ii1i * i11iIiiIii * III1I11iiii1I
 if 85 - 85: I1I1IIiiIiI1 . i1I111I / IiiI11Iiiii . O0 % I1i1iii
def O0iIiIIIIIii ( heading , announce ) :
 class o00oOO0 ( ) :
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
   try : I1iiIIIi11 = open ( announce ) ; OO0ooo0oOO = I1iiIIIi11 . read ( )
   except : OO0ooo0oOO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OO0ooo0oOO ) )
   return
 o00oOO0 ( )
 o00oOO0 ( )
 if 97 - 97: iI1I / o0O0
def Oooo0 ( ) :
 IIii11I1i1I ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 IIii11I1i1I ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 IIii11I1i1I ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 IIii11I1i1I ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 IIii11I1i1I ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 if 59 - 59: OoooooooOO
 if 47 - 47: IiiI11Iiiii - iI1I / II111iiii
 if 12 - 12: III1I11iiii1I
def O0iII1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def IIII1i ( url ) :
 if url == 'http://' : return False
 try :
  IiIIi1 = urllib2 . Request ( url )
  IiIIi1 . add_header ( 'User-Agent' , iIiiiI )
  IIIIiii1IIii = urllib2 . urlopen ( IiIIi1 )
  IIIIiii1IIii . close ( )
 except Exception , II1i11I :
  return II1i11I
 return True
 if 2 - 2: iIii1I11I1II1 * iiiIi % iii1I1 - II111iiii - o0O0
 if 3 - 3: I1i1iii
 if 45 - 45: I1i1iii
def oOIIi1iiii1iI ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv Sports" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By GenieTv Sports[/COLOR]" )
 return
 if 25 - 25: iiIiIIi + O0
def i1II ( url ) :
 print '###' + IiII + ' - DELETING Addons20.db ###'
 O0OOO0OOooo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 I111iIi1 = os . path . join ( O0OOO0OOooo00 , 'Addons20.db' )
 try :
  os . remove ( I111iIi1 )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== ' + IiII + ' - DELETING    ' + str ( I111iIi1 ) + '    ==='
  ii11iIi1I . ok ( IiII , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "       No File To Remove" )
 return
 if 92 - 92: IiiI11Iiiii
 if 22 - 22: iiiIi % o0O0 * iiIiIIi / III1I11iiii1I % i11iIiiIii * IiI1i11iii1
 if 95 - 95: OoooooooOO - ii1I11II1ii1i * iI1I + i1I111I
 if 10 - 10: I1I1IIiiIiI1 / i11iIiiIii
 if 92 - 92: IiI1i11iii1 . I1i1iii
def Ii11Ii1I ( url ) :
 IiIIi1 = urllib2 . Request ( url )
 IiIIi1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 IIIIiii1IIii = urllib2 . urlopen ( IiIIi1 )
 I1II1 = IIIIiii1IIii . read ( )
 IIIIiii1IIii . close ( )
 return I1II1
def o00oOO0 ( title , msg ) :
 class O0iIiIIIIIii ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 85 - 85: iiIiIIi . I1i1iii
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 78 - 78: IiiI11Iiiii * I1i1iii + iIii1I11I1II1 + iIii1I11I1II1 / I1i1iii . IIII
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 97 - 97: IiiI11Iiiii / I1i1iii % i1IIi % iiIiIIi
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 18 - 18: iIii1I11I1II1 % IiI1i11iii1
 O00oO0 = O0iIiIIIIIii ( "Textbox.xml" , o0OOO . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 O00oO0 . doModal ( )
 del O00oO0
def O0iIiIIIIIii ( heading , announce ) :
 class o00oOO0 ( ) :
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
   try : I1iiIIIi11 = open ( announce ) ; OO0ooo0oOO = I1iiIIIi11 . read ( )
   except : OO0ooo0oOO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OO0ooo0oOO ) )
   return
 o00oOO0 ( )
 o00oOO0 ( )
def o0o0o0o0 ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 I1Iiiiiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1IIIiI1I1ii1 , iiiI1I1iIIIi1 , Iii in os . walk ( I1Iiiiiii ) :
   I1iiiiI1iI = 0
   I1iiiiI1iI += len ( Iii )
   if 43 - 43: iii1I1 - OoooooooOO
   if 3 - 3: O0 / o0O0
   if I1iiiiI1iI > 0 :
    if 31 - 31: III1I11iiii1I + I1I1IIiiIiI1 . OoooooooOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( I1iiiiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: II111iiii + i1IIi + II111iiii
     for I1iiIIIi11 in Iii :
      os . unlink ( os . path . join ( I1IIIiI1I1ii1 , I1iiIIIi11 ) )
     for IiII1II11I in iiiI1I1iIIIi1 :
      shutil . rmtree ( os . path . join ( I1IIIiI1I1ii1 , IiII1II11I ) )
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
 O0Oo00O ( url )
 return
def O0Oo00O ( url ) :
 OOo0o000oO = os . path . join ( I1i1iiI1 , 'addon_data' )
 oO0o00oOOooO0 = [
 ( OOo0o000oO ) ,
 ( oo00 ) ,
 ( os . path . join ( O0oo0OO0 , 'cache' ) ) ,
 ( os . path . join ( O0oo0OO0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo00 , 'plugin.video.GenieTv_Sports' , 'Images' ) ) ,
 ( os . path . join ( OOo0o000oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OOo0o000oO , 'plugin.video.GenieTv_Sports' , 'Images' ) ) ]
 if 79 - 79: OO - iIii1I11I1II1 + IIII - I1i1iii
 OoO = 0
 if 35 - 35: i1I111I + i11iIiiIii - II111iiii
 for Ii1ii111i1 in oO0o00oOOooO0 :
  if os . path . exists ( Ii1ii111i1 ) and not Ii1ii111i1 in [ oo00 , OOo0o000oO ] :
   for I1IIIiI1I1ii1 , iiiI1I1iIIIi1 , Iii in os . walk ( Ii1ii111i1 ) :
    I1iiiiI1iI = 0
    I1iiiiI1iI += len ( Iii )
    if I1iiiiI1iI > 0 :
     for I1iiIIIi11 in Iii :
      if not I1iiIIIi11 in iiIIIII1i1iI :
       try :
        os . unlink ( os . path . join ( I1IIIiI1I1ii1 , I1iiIIIi11 ) )
       except :
        pass
      else : Oo0OO0000oooo ( 'Ignore Log File: %s' % I1iiIIIi11 )
     for IiII1II11I in iiiI1I1iIIIi1 :
      try :
       shutil . rmtree ( os . path . join ( I1IIIiI1I1ii1 , IiII1II11I ) )
       OoO += 1
       Oo0OO0000oooo ( "[Success] cleared %s files from %s" % ( str ( I1iiiiI1iI ) , os . path . join ( Ii1ii111i1 , IiII1II11I ) ) )
      except :
       Oo0OO0000oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( Ii1ii111i1 , IiII1II11I ) )
  else :
   for I1IIIiI1I1ii1 , iiiI1I1iIIIi1 , Iii in os . walk ( Ii1ii111i1 ) :
    for IiII1II11I in iiiI1I1iIIIi1 :
     if 'cache' in IiII1II11I . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( I1IIIiI1I1ii1 , IiII1II11I ) )
       OoO += 1
       Oo0OO0000oooo ( "[Success] wiped %s " % os . path . join ( Ii1ii111i1 , IiII1II11I ) )
      except :
       Oo0OO0000oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( Ii1ii111i1 , IiII1II11I ) )
       if 31 - 31: III1I11iiii1I + O0
 oooooOOO000Oo ( IiII , 'Clear Cache: Removed %s Files' % OoO )
def oO0oOOoo00000 ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 I1Iiiiiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1IIIiI1I1ii1 , iiiI1I1iIIIi1 , Iii in os . walk ( I1Iiiiiii ) :
   I1iiiiI1iI = 0
   I1iiiiI1iI += len ( Iii )
   if 52 - 52: iI1I
   if 51 - 51: ii1I11II1ii1i
   if I1iiiiI1iI > 0 :
    if 88 - 88: OoooooooOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( I1iiiiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 84 - 84: i1I111I / IiI1i11iii1 * o0O0 / iii1I1 - i11iIiiIii . iiiIi
     for I1iiIIIi11 in Iii :
      os . unlink ( os . path . join ( I1IIIiI1I1ii1 , I1iiIIIi11 ) )
     for IiII1II11I in iiiI1I1iIIIi1 :
      shutil . rmtree ( os . path . join ( I1IIIiI1I1ii1 , IiII1II11I ) )
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
 if 60 - 60: iiIiIIi * iI1I
def I1iIiI11I1 ( ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 oOOo0 = ii11iIi1I . yesno ( 'Force Close GenieTv Sports' , 'You are about to close GenieTv Sports' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oOOo0 == 0 : return
 elif oOOo0 == 1 : pass
 i1oOOoo0o0OOOO = O0iII1 ( )
 Oo0OO0000oooo ( "Platform: " + str ( i1oOOoo0o0OOOO ) )
 os . _exit ( 1 )
 Oo0OO0000oooo ( "Force close failed!  Trying alternate methods." )
 if i1oOOoo0o0OOOO == 'osx' :
  Oo0OO0000oooo ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1oOOoo0o0OOOO == 'linux' :
  Oo0OO0000oooo ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1oOOoo0o0OOOO == 'android' :
  Oo0OO0000oooo ( "############ try android force close #################" )
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
 elif i1oOOoo0o0OOOO == 'windows' :
  Oo0OO0000oooo ( "############ try windows force close #################" )
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
  Oo0OO0000oooo ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  Oo0OO0000oooo ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 26 - 26: o0O0 % iIii1I11I1II1 + I1I1IIiiIiI1
def II1III1I1I1Ii ( url ) :
 import urlresolver
 try :
  I1III1111iIi = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( I1III1111iIi , xbmcgui . ListItem ( oOOOoo0O0OoO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( oOOOoo0O0OoO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def O0iII1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 67 - 67: iii1I1 + II111iiii - O0 . iii1I1 * II111iiii * IiI1i11iii1
def Oo0OO0000oooo ( log ) :
 xbmc . log ( "[%s]: %s" % ( IiII , log ) )
 if not os . path . exists ( oo00 ) : os . makedirs ( oo00 )
 if not os . path . exists ( i1111 ) : I1iiIIIi11 = open ( i1111 , 'w' ) ; I1iiIIIi11 . close ( )
 with open ( i1111 , 'a' ) as I1iiIIIi11 :
  o00OO00O0oOO = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  I1iiIIIi11 . write ( o00OO00O0oOO . rstrip ( '\r\n' ) + '\n' )
  if 4 - 4: OoooooooOO - i1IIi % IIII - III1I11iiii1I * I1I1IIiiIiI1
def Ooooo00o0OoO ( ) :
 try :
  oooo0O0O0o0 = getSet ( "core-player" )
  if ( oooo0O0O0o0 == 'DVDPLAYER' ) : Ooo0oo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oooo0O0O0o0 == 'MPLAYER' ) : Ooo0oo = xbmc . PLAYER_CORE_MPLAYER
  elif ( oooo0O0O0o0 == 'PAPLAYER' ) : Ooo0oo = xbmc . PLAYER_CORE_PAPLAYER
  else : Ooo0oo = xbmc . PLAYER_CORE_AUTO
 except : Ooo0oo = xbmc . PLAYER_CORE_AUTO
 return Ooo0oo
 return True
 if 41 - 41: i1I111I * IiI1i11iii1 / i1I111I % iii1I1
def I1iiii1I ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii = True
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooo0OOO . setProperty ( "Fanart_Image" , fanart )
 Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = True )
 return Ii
 if 77 - 77: i1I111I % IIII
 if 9 - 9: OO - iiiIi * OoooooooOO . iiiIi
def iiI1IIIi ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii = True
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooo0OOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1Ii1IiIIi = [ ]
  ii1Ii1IiIIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  ooo0OOO . addContextMenuItems ( ii1Ii1IiIIi )
 Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = False )
 return Ii
 if 83 - 83: IiI1i11iii1 / iiIiIIi
def oOOO00o ( name , url , mode , iconimage , fanart , description ) :
 if 34 - 34: iI1I * iiiIi * I1i1iii / OO * IiI1i11iii1 / iIii1I11I1II1
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii = True
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooo0OOO . setProperty ( "Fanart_Image" , fanart )
 Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = True )
 return Ii
 if 74 - 74: iiiIi / i11iIiiIii - II111iiii * I1I1IIiiIiI1
def IIii11I1i1I ( name , url , mode , iconimage , fanart , description ) :
 if 5 - 5: III1I11iiii1I - III1I11iiii1I . iiiIi + i1I111I - III1I11iiii1I . iii1I1
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii = True
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooo0OOO . setProperty ( "Fanart_Image" , fanart )
 Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = False )
 return Ii
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii = True
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooo0OOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1Ii1IiIIi = [ ]
  if showcontext == 'fav' :
   ii1Ii1IiIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   ii1Ii1IiIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooo0OOO . addContextMenuItems ( ii1Ii1IiIIi )
 Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = False )
 return Ii
def IiIi1i1ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii = True
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1Ii1IiIIi = [ ]
  ii1Ii1IiIIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1Ii1IiIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   ii1Ii1IiIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooo0OOO . addContextMenuItems ( ii1Ii1IiIIi )
 Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = True )
 return Ii
def iiIi ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0OOoOOO0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii = True
 ooo0OOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo0OOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1Ii1IiIIi = [ ]
  ii1Ii1IiIIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1Ii1IiIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   ii1Ii1IiIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooo0OOO . addContextMenuItems ( ii1Ii1IiIIi )
 Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0OOoOOO0oO , listitem = ooo0OOO , isFolder = False )
 return Ii
 if 71 - 71: i1I111I . i1IIi
def o0OooO0ooo0o ( ) :
 iii1 = [ ]
 I1i = sys . argv [ 2 ]
 if len ( I1i ) >= 2 :
  iii11 = sys . argv [ 2 ]
  OOOO = iii11 . replace ( '?' , '' )
  if ( iii11 [ len ( iii11 ) - 1 ] == '/' ) :
   iii11 = iii11 [ 0 : len ( iii11 ) - 2 ]
  ooO0oO00O0o = OOOO . split ( '&' )
  iii1 = { }
  for ooOO00oOOo000 in range ( len ( ooO0oO00O0o ) ) :
   IIi = { }
   IIi = ooO0oO00O0o [ ooOO00oOOo000 ] . split ( '=' )
   if ( len ( IIi ) ) == 2 :
    iii1 [ IIi [ 0 ] ] = IIi [ 1 ]
    if 27 - 27: III1I11iiii1I % IIII
 return iii1
 if 58 - 58: III1I11iiii1I * I1I1IIiiIiI1 + O0 % III1I11iiii1I
 if 25 - 25: iiiIi % iiIiIIi * IiiI11Iiiii
iii11 = o0OooO0ooo0o ( )
I11i1I1I = None
oOOOoo0O0OoO = None
I11oo0ooOO = None
iI1IiIIiIIi = None
OO00Oo = None
IiIi11Iii = None
III1i1iI1 = None
if 97 - 97: IiI1i11iii1 - i11iIiiIii
if 17 - 17: IiI1i11iii1
try :
 III1i1iI1 = int ( iii11 [ "fav_mode" ] )
except :
 pass
 if 73 - 73: iii1I1
try :
 I11i1I1I = urllib . unquote_plus ( iii11 [ "url" ] )
except :
 pass
try :
 oOOOoo0O0OoO = urllib . unquote_plus ( iii11 [ "name" ] )
except :
 pass
try :
 iI1IiIIiIIi = urllib . unquote_plus ( iii11 [ "iconimage" ] )
except :
 pass
try :
 I11oo0ooOO = int ( iii11 [ "mode" ] )
except :
 pass
try :
 OO00Oo = urllib . unquote_plus ( iii11 [ "fanart" ] )
except :
 pass
try :
 IiIi11Iii = urllib . unquote_plus ( iii11 [ "description" ] )
except :
 pass
 if 19 - 19: i1I111I + IiI1i11iii1 % OO . o0O0 * IIII - i1I111I
 if 66 - 66: i1I111I . i11iIiiIii - o0O0 * I1I1IIiiIiI1 + OoooooooOO * iiIiIIi
print str ( i1i1II ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( I11oo0ooOO )
print "URL: " + str ( I11i1I1I )
print "Name: " + str ( oOOOoo0O0OoO )
print "IconImage: " + str ( iI1IiIIiIIi )
if 74 - 74: iiiIi
if 61 - 61: iiiIi - I1i1iii * II111iiii % IiiI11Iiiii * iIii1I11I1II1 + OO
def O0000 ( content , viewType ) :
 if 64 - 64: II111iiii - iI1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OOO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OOO . getSetting ( viewType ) )
  if 68 - 68: IiiI11Iiiii - III1I11iiii1I - iIii1I11I1II1 / i1I111I + III1I11iiii1I - OO
  if 75 - 75: o0O0 / I1I1IIiiIiI1 % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii
if I11oo0ooOO == None : oo0Oo00Oo0 ( )
elif I11oo0ooOO == 11111 : I1I1i ( )
elif I11oo0ooOO == 1 : Genres ( )
elif I11oo0ooOO == 2 : Lists ( I11i1I1I , iI1IiIIiIIi )
elif I11oo0ooOO == 3 : all_mov ( )
elif I11oo0ooOO == 4 : Search ( )
elif I11oo0ooOO == 5 : Oooo0 ( )
elif I11oo0ooOO == 6 : oO0oOOoo00000 ( I11i1I1I )
elif I11oo0ooOO == 7 : O0Oo00O ( I11i1I1I )
elif I11oo0ooOO == 8 : I1iIiI11I1 ( )
elif I11oo0ooOO == 10 : MyAccDetails ( )
elif I11oo0ooOO == 15 : II1III1I1I1Ii ( I11i1I1I )
elif I11oo0ooOO == 16 : yt . PlayVideo ( I11i1I1I )
elif I11oo0ooOO == 18 : o0OOO . openSettings ( sys . argv [ 0 ] )
elif I11oo0ooOO == 20 : oO00O0 ( I11i1I1I )
elif I11oo0ooOO == 21 : OooOOOO ( I11i1I1I )
elif I11oo0ooOO == 22 : Xtreme2 ( I11i1I1I )
elif I11oo0ooOO == 23 : ii1iiIiIII1ii ( I11i1I1I )
elif I11oo0ooOO == 30 : O00Oo000ooO0 ( )
elif I11oo0ooOO == 31 : Oo0O0oooo ( )
elif I11oo0ooOO == 32 : iII ( )
elif I11oo0ooOO == 33 : iii1i1iiiiIi ( )
elif I11oo0ooOO == 34 : OO0Oooo0oOO0O ( oOOOoo0O0OoO , IiIi11Iii )
elif I11oo0ooOO == 40 : O0o0 ( )
elif I11oo0ooOO == 41 : O0OOO0OOoO0O ( I11i1I1I )
elif I11oo0ooOO == 211 : IiIiII1 ( I11i1I1I )
elif I11oo0ooOO == 212 : Iii1iiIi1II ( I11i1I1I , iI1IiIIiIIi )
elif I11oo0ooOO == 222 : II1III1I1I1Ii ( I11i1I1I )
elif I11oo0ooOO == 1000 : Ii11I ( )
elif I11oo0ooOO == 50000 : Ooo00OoOOO ( )
elif I11oo0ooOO == 50001 : oOIIi1iiii1iI ( )
elif I11oo0ooOO == 50002 : i1II ( I11i1I1I )
elif I11oo0ooOO == 300000000 : FluxUstv ( )
elif I11oo0ooOO == 300000001 : i1iI1 ( I11i1I1I )
elif I11oo0ooOO == 300000002 : ooo0O0o00O ( I11i1I1I )
elif I11oo0ooOO == 300000003 : ii1I1IIii11 ( oOOOoo0O0OoO , I11i1I1I )
elif I11oo0ooOO == 300000004 : I1i11 ( I11i1I1I )
elif I11oo0ooOO == 300000005 : o00o0 ( I11i1I1I )
elif I11oo0ooOO == 300000006 : iiI ( oOOOoo0O0OoO , I11i1I1I )
if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % IiI1i11iii1 * IiI1i11iii1 * iiIiIIi
elif I11oo0ooOO == 900300 : o0Oo0oO0oOO00 ( )
elif I11oo0ooOO == 900301 : o00Oo0oooooo ( I11i1I1I )
elif I11oo0ooOO == 900302 : iiIiIIIiiI ( I11i1I1I )
elif I11oo0ooOO == 90030 : II11IiIi11 ( )
elif I11oo0ooOO == 1001111 : o0oO0oooOoo ( oOOOoo0O0OoO , I11i1I1I )
if 24 - 24: II111iiii % I1i1iii - IiiI11Iiiii + iI1I * iiIiIIi
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
