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
o0OoOoOO00 = "0.0.3"
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
 oOOO00o ( '[COLORorangered]Club Teams[/COLOR]' , Oo0oO0ooo , 1010 , i1 + 'clubteams.jpg' , Oo0o0000o0o0 , '[COLORorangered]Club Teams [CR]YouTube Channels[/COLOR]' )
 O0O00o0OOO0 ( '[COLORorangered]DISCLAIMER[/COLOR]' , Oo0oO0ooo , 11111 , i1 + 'disclaimer.jpg' , Oo0o0000o0o0 , '[COLORorangered]DISCLAIMER[/COLOR]' )
 if 27 - 27: IIII % o0O0 . ii1I11II1ii1i % I1i1iii - IiiI11Iiiii / OoooooooOO
def I1I1i ( ) :
 oOOOoo0O0OoO = '[COLORorangered]GenieTv Disclaimer[/COLOR]'
 ii1i1I1i = '[COLORorangered]Due to the nature of our content, [COLORsteelblue][B]we are not responsible[/B] [COLORorangered]for the content streamed to your device and neither do we condone piracy [CR]so you must satisfy yourself that either you or the sites accessed for streaming have the copyright agreements in place and are entitled to access this content.[CR][CR]We do not host or upload any video, films, media file, live streams (avi, mov, flv, mpg, mpeg, divx, dvd rip, mp3, mp4, torrent, ipod, psp). [CR][CR][COLORsteelblue][B]GenieTv is not responsible[/B] [COLORorangered]for the accuracy, compliance, copyright, legality, decency, or any other aspect of the content of streamed from your device. [CR]If you have any legal issues please contact the appropriate media file owners or host sites.[CR][CR]We have no control over the links on any site that we provide a link to. [CR]If you see any form of infringements, please contact appropriate media file owners or host sites immediately.[/COLOR]'
 o00oOO0 ( oOOOoo0O0OoO , ii1i1I1i )
 if 95 - 95: III1I11iiii1I / OoooooooOO
 if 18 - 18: i11iIiiIii
def Ii11I ( ) :
 oOOO00o ( '[COLORorangered]Celtic FC[/COLOR]' , Oo0oO0ooo , 1006 , 'https://vignette.wikia.nocookie.net/fifa/images/a/a8/Celtic_FC.png/revision/latest?cb=20180213000259' , Oo0o0000o0o0 , '[COLORorangered]Celtic FC[/COLOR]' )
 oOOO00o ( '[COLORorangered]Rangers[/COLOR]' , Oo0oO0ooo , 1007 , 'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Rangers_FC.svg/1200px-Rangers_FC.svg.png' , Oo0o0000o0o0 , '[COLORorangered]Rangers[/COLOR]' )
def OOO0OOO00oo ( ) :
 oOOO00o ( '[COLORorangered]Rangers[/COLOR]' , Oo0oO0ooo , 1008 , 'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Rangers_FC.svg/1200px-Rangers_FC.svg.png' , Oo0o0000o0o0 , '[COLORorangered]Rangers[/COLOR]' )
 if 31 - 31: II111iiii - III1I11iiii1I . I1i1iii % i1I111I - O0
def iii11 ( ) :
 oOOO00o ( '[COLORgreen]Celtic FC Youtube[/COLOR]' , '' , 1000 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Celtic FC Youtube[/COLOR]' )
 oOOO00o ( '[COLORgreen]PLZ Soccer[/COLOR]' , '' , 1001 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]PLZ Soccer[/COLOR]' )
 oOOO00o ( '[COLORgreen]Podcasts[/COLOR]' , '' , 1002 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Podcasts[/COLOR]' )
 oOOO00o ( '[COLORgreen]Rebel Tunes[/COLOR]' , '' , 1003 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Rebel Tunes[/COLOR]' )
 oOOO00o ( '[COLORgreen]Green Brigade[/COLOR]' , '' , 1004 , 'http://i.imgur.com/yCI9gJj.jpg' , Oo0o0000o0o0 , '[COLORgreen]Green Brigade[/COLOR]' )
 if 58 - 58: III1I11iiii1I * i11iIiiIii / i1I111I % I1i1iii - iiIiIIi / iii1I1
def ii11i1 ( ) :
 oOOO00o ( '[COLORorangered]Extreme Sports[/COLOR]' , 'http://www.ridersmatch.com/' , 20 , i1 + 'extreme.jpg' , Oo0o0000o0o0 , '[COLORorangered]Extreme Sports[/COLOR]' )
 IIIii1II1II = i1I1iI ( Oo0oO0ooo + O0O ( 'VHJvamFuLnBocA==' ) )
 oo0OooOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIii1II1II )
 for o0O , O00oO , ii1i1I1i , I11i1I1I , oOOOoo0O0OoO in oo0OooOOo0 :
  O00oO = ( O0O ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9wbGV4L2Rvd25sb2Fkcy9TUE9SVFMuQ0FUQ0hVUC8=' ) + O0O ( O00oO ) )
  oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , ( Oo0oO0ooo + O0O ( o0O ) ) , 41 , O00oO , O00oO , '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' )
def oO0Oo ( url ) :
 IIIii1II1II = i1I1iI ( url )
 oo0OooOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIii1II1II )
 for url , O00oO , ii1i1I1i , I11i1I1I , oOOOoo0O0OoO in oo0OooOOo0 :
  if '.php' in url :
   oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , url , 41 , O00oO , Oo0o0000o0o0 , '[COLORorangered]' + ii1i1I1i + '[/COLOR]' )
  else :
   O0O00o0OOO0 ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , url , 15 , O00oO , Oo0o0000o0o0 , '[COLORorangered]' + ii1i1I1i + '[/COLOR]' )
def oOOoo0Oo ( ) :
 oOOO00o ( '[COLORorangered]Highlights[/COLOR]' , 'http://www.replaymatches.com/' , 900300 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]Highlights[/COLOR]' )
 oOOO00o ( '[COLORorangered]Latest Results[/COLOR]' , '' , 33 , i1 + 'latest_results.jpg' , Oo0o0000o0o0 , '[COLORorangered]Latest Results[/COLOR]' )
 oOOO00o ( '[COLORorangered]Top Goal Scorers[/COLOR]' , '' , 32 , i1 + 'top_scorers.jpg' , Oo0o0000o0o0 , '[COLORorangered]Top Goal Scorers[/COLOR]' )
 if 78 - 78: IiI1i11iii1
def OO00Oo ( ) :
 O0OOO0OOoO0O = i1I1iI ( 'http://www.eplsite.com/fetchdata_toptenscorer.php' )
 O00Oo000ooO0 = re . compile ( '"Topscorer"(.+?)"AccountInformation"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 OoO0O00 = re . compile ( '{"Rank":"([^"]*)","Name":"([^"]*)","TeamName":"([^"]*)","Team_Id":"([^"]*)","Nationality":"([^"]*)","Goals":"([^"]*)","FirstScorer":"([^"]*)","Penalties":"([^"]*)","MissedPenalties":"([^"]*)"}' , re . DOTALL ) . findall ( str ( O00Oo000ooO0 ) )
 for IIiII , o0 , ooOooo000oOO , Oo0oOOo , Oo0OoO00oOO0o , OOO00O , OOoOO0oo0ooO , O0o0O00Oo0o0 , O00O0oOO00O00 in OoO0O00 :
  i1Oo00 = 'Rank: ' + IIiII + '[CR]Name: ' + o0 + '[CR]TeamName: ' + ooOooo000oOO + '[CR]Team Id: ' + Oo0oOOo + '[CR]Nationality: ' + Oo0OoO00oOO0o + '[CR]Goals: ' + OOO00O + '[CR]FirstScorer: ' + OOoOO0oo0ooO + '[CR]Penalties: ' + O0o0O00Oo0o0 + '[CR]MissedPenalties: ' + O00O0oOO00O00 + '\n'
  O0O00o0OOO0 ( '[COLORorangered]' + o0 + '[/COLOR]' , '' , '' , i1 + 'top_scorers.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + i1Oo00 + '[/COLOR]' )
  if 31 - 31: I1i1iii . i1I111I / O0
def o000O0o ( ) :
 O0OOO0OOoO0O = i1I1iI ( 'http://eplsite.com/fetchdata_liveresult.php' )
 O00Oo000ooO0 = re . compile ( '"Match"(.+?)"AccountInformation"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 OoO0O00 = re . compile ( '{"Id":(.+?),"FixtureMatch_Id":(.+?),"Date":(.+?),"Round":(.+?),"Spectators":(.+?),"League":(.+?),"HomeTeam":(.+?),"HomeTeam_Id":(.+?),"HomeCorners":(.+?),"HomeGoals":(.+?),"HalfTimeHomeGoals":(.+?),"HomeShots":(.+?),"HomeShotsOnTarget":(.+?),"HomeFouls":(.+?),"HomeGoalDetails":(.+?),"HomeLineupGoalkeeper":(.+?),"HomeLineupDefense":(.+?),"HomeLineupMidfield":(.+?),"HomeLineupForward":(.+?),"HomeLineUpSubstitutes":(.+?),"HomeLineUpCoach":(.+?),"HomeYellowCards":(.+?),"HomeRedCards":(.+?),"HomeTeamFormation":(.+?),"AwayTeam":(.+?),"AwayTeam_Id":(.+?),"AwayCorners":(.+?),"AwayGoals":(.+?),"HalfTimeAwayGoals":(.+?),"AwayShots":(.+?),"AwayShotsOnTarget":(.+?),"AwayFouls":(.+?),"AwayGoalDetails":(.+?),"AwayLineupGoalkeeper":(.+?),"AwayLineupDefense":(.+?),"AwayLineupMidfield":(.+?),"AwayLineupForward":(.+?),"AwayLineUpSubstitutes":(.+?),"AwayLineUpCoach":(.+?),"AwayYellowCards":(.+?),"AwayRedCards":(.+?),"AwayTeamFormation":(.+?),"HomeTeamYellowCardDetails":(.+?),"AwayTeamYellowCardDetails":(.+?),"HomeTeamRedCardDetails":(.+?),"AwayTeamRedCardDetails":(.+?),"HomeSubDetails":(.+?),"AwaySubDetails":(.+?),"Referee":"(.+?)"}' , re . DOTALL ) . findall ( str ( O00Oo000ooO0 ) )
 for iI1iII1 , oO0OOoo0OO , O0ii1ii1ii , oooooOoo0ooo , I1I1IiI1 , III1iII1I1ii , oOOo0 , oo00O00oO , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo , oo0OOo , ooOOO00Ooo , IiIIIi1iIi , ooOOoooooo , II1I , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo , o0O0OOO0Ooo , iiIiI , I1 , OOO00O0O , iii , oOooOOOoOo , i1Iii1i1I , OOoO00 , IiI111111IIII , i1Ii , ii111iI1iIi1 , OOO , oo0OOo0 , I11IiI , O0ooO0Oo00o , ooO0oOOooOo0 , i1I1ii11i1Iii , I1IiiiiI , o0OIiII , ii1iII1II , Iii1I1I11iiI1 , I1I1i1I , ii1I , O0oO0 , oO0 , O0OO0O , OOOoOoO , Ii1I1i , OOI1iI1ii1II in OoO0O00 :
  i1Oo00 = 'Date: ' + O0ii1ii1ii + '[CR]HomeTeam: ' + oOOo0 + '[CR]HomeGoals: ' + ooo00OOOooO + '[CR]AwayTeam: ' + iii + '[CR]AwayGoals: ' + OOoO00 + '[CR]Round: ' + oooooOoo0ooo + '[CR]Spectators: ' + I1I1IiI1 + '[CR]League: ' + III1iII1I1ii + '[CR]HomeCorners: ' + iIiIIIi + '[CR]HalfTimeHomeGoals: ' + O00OOOoOoo0O + '[CR]HomeShots: ' + O000OOo00oo + '[CR]HomeShotsOnTarget: ' + oo0OOo + '[CR]HomeFouls: ' + ooOOO00Ooo + '[CR]HomeGoalDetails: ' + IiIIIi1iIi + '[CR]HomeLineupGoalkeeper: ' + ooOOoooooo + '[CR]HomeLineupDefense: ' + II1I + '[CR]HomeLineupMidfield: ' + O0i1II1Iiii1I11 + '[CR]HomeLineupForward: ' + IIIIiiIiI + '[CR]HomeLineUpSubstitutes: ' + o00oooO0Oo + '[CR]HomeLineUpCoach: ' + o0O0OOO0Ooo + '[CR]HomeYellowCards: ' + iiIiI + '[CR]HomeRedCards: ' + I1 + '[CR]HomeTeamFormation: ' + OOO00O0O + '[CR]AwayCorners: ' + i1Iii1i1I + '[CR]HalfTimeAwayGoals: ' + IiI111111IIII + '[CR]AwayShots: ' + i1Ii + '[CR]AwayShotsOnTarget: ' + ii111iI1iIi1 + '[CR]AwayFouls: ' + OOO + '[CR]AwayGoalDetails: ' + oo0OOo0 + '[CR]AwayLineupGoalkeeper: ' + I11IiI + '[CR]AwayLineupDefense: ' + O0ooO0Oo00o + '[CR]AwayLineupMidfield: ' + ooO0oOOooOo0 + '[CR]AwayLineupForward: ' + i1I1ii11i1Iii + '[CR]AwayLineUpSubstitutes: ' + I1IiiiiI + '[CR]AwayLineUpCoach: ' + o0OIiII + '[CR]AwayYellowCards: ' + ii1iII1II + '[CR]AwayRedCards: ' + Iii1I1I11iiI1 + '[CR]AwayTeamFormation: ' + I1I1i1I + '[CR]HomeTeamYellowCardDetails: ' + ii1I + '[CR]AwayTeamYellowCardDetails: ' + O0oO0 + '[CR]HomeTeamRedCardDetails: ' + oO0 + '[CR]AwayTeamRedCardDetails: ' + O0OO0O + '[CR]HomeSubDetails: ' + OOOoOoO + '[CR]AwaySubDetails: ' + Ii1I1i + '[CR]Referee: ' + OOI1iI1ii1II + '\n'
  O0O00o0OOO0 ( ( '[COLORorangered]' + oOOo0 + '[COLORsteelblue] Vs [COLORorangered]' + iii + '[COLORsteelblue] ' + ooo00OOOooO + ':' + OOoO00 + '[/COLOR]' ) . replace ( '"' , '' ) , '' , 34 , i1 + 'match_stats.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( i1Oo00 ) . replace ( '{}' , 'N/A' ) . replace ( '\\' , '' ) . replace ( "'" , '' ) . replace ( '"' , '' ) + '[/COLOR]' )
def O0O0OOOOoo ( name , description ) :
 name = name
 ii1i1I1i = description
 o00oOO0 ( name , ii1i1I1i )
 if 74 - 74: iiIiIIi + II111iiii / OO
 if 100 - 100: i1I111I * iIii1I11I1II1
def oOo00oOoO000 ( ) :
 OOooo0oOO0O = [ '[COLORsteelblue]FootBall Source 1[/COLOR]' , '[COLORsteelblue]FootBall Source 2[/COLOR]' , '[COLORsteelblue]FootBall Source 3[/COLOR]' , '[COLORsteelblue]F1[/COLOR]' , '[COLORsteelblue]NFL[/COLOR]' ]
 o00O0 = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Select Source[/COLOR]' , OOooo0oOO0O )
 if o00O0 == 0 :
  oOO0O00Oo0O0o ( )
 if o00O0 == 1 :
  ii1 ( )
 if o00O0 == 2 :
  I1iIIiiIIi1i ( )
 if o00O0 == 3 :
  O0O0ooOOO ( )
 if o00O0 == 4 :
  oOOo0O00o ( )
  if 8 - 8: OO
def oOO0O00Oo0O0o ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 O0OOO0OOoO0O = i1I1iI ( 'http://www.eplsite.com/' )
 O00Oo000ooO0 = re . compile ( '<h4>FOOTBALL LIVE STREAMS</h4>(.+?)</section>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 OoO0O00 = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="vs  "><span>(.+?)</span><div class="accordion-time">(.+?)</div></div>.+?<div class="acoordian-right-section">(.+?)</div>.+?<p>(.+?)</p>.+?<p>(.+?)</p>(.+?)<center>' , re . DOTALL ) . findall ( str ( O00Oo000ooO0 ) )
 for ii1111iII , iiiiI , time , oooOo0OOOoo0 , OOoO , oOOOoo0O0OoO , OO0O000 in OoO0O00 :
  iiIiI1i1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( OO0O000 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + ( OOoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( OOoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + ii1111iII + ' ' + iiiiI + ' ' + oooOo0OOOoo0 + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for O00oO , o0O , oO0O00oOOoooO in iiIiI1i1 :
   IiIi11iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O
   O0O00o0OOO0 ( '[COLORsteelblue]' + oO0O00oOOoooO + '[/COLOR]' , IiIi11iI , 15 , 'http://www.eplsite.com/' + O00oO , Oo0o0000o0o0 , '[COLORsteelblue]' + oO0O00oOOoooO + '[/COLOR]' )
   if 83 - 83: II111iiii % iiiIi % IiiI11Iiiii % iiIiIIi
def ii1 ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 O0OOO0OOoO0O = i1I1iI ( 'http://www.abcast.me/' )
 O00Oo000ooO0 = re . compile ( '</thead>(.+?)</html>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 OoO0O00 = re . compile ( '<td> (.+?) </td>.+?</strong>.+?<td>(.+?)</td>.+?href="(.+?)">' , re . DOTALL ) . findall ( str ( O00Oo000ooO0 ) )
 for OOoO , oOOOoo0O0OoO , o0O in OoO0O00 :
  IiIi11iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O
  O0O00o0OOO0 ( '[COLORorangered]' + OOoO + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , IiIi11iI , 15 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + OOoO + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
  if 80 - 80: i11iIiiIii % IiiI11Iiiii + IIII % IiI1i11iii1 - iiIiIIi
def I1iIIiiIIi1i ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Match Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 O0OOO0OOoO0O = i1I1iI ( 'http://www.sports-stream.net/schedule.html' )
 I1i1i1iii = re . compile ( '<font color="red"><h3>(.+?)<input onclick=(.+?)<br>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for I1111i , OO0O000 in I1i1i1iii :
  OoO0O00 = re . compile ( 'style="color:#FF0000;">(.+?)</span>(.+?) - <a href="(.+?)" ' , re . DOTALL ) . findall ( str ( OO0O000 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + ( I1111i ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( I1111i ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for time , oOOOoo0O0OoO , o0O in OoO0O00 :
   IiIi11iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O
   O0O00o0OOO0 ( '[COLORorangered]' + time + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , IiIi11iI , 15 , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + time + '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
   if 14 - 14: III1I11iiii1I / I1I1IIiiIiI1
   if 32 - 32: iI1I * iiiIi
def O0O0ooOOO ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Race Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 O0OOO0OOoO0O = i1I1iI ( 'http://www.eplsite.com/f1.html' )
 O00Oo000ooO0 = re . compile ( '<h4>F1 Live Streams</h4>(.+?)</section>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 OoO0O00 = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="accordion-time">(.+?)</div></div>.+?<p>(.+?)</p>(.+?)</header>' , re . DOTALL ) . findall ( str ( O00Oo000ooO0 ) )
 for ii1111iII , time , oOOOoo0O0OoO , OO0O000 in OoO0O00 :
  iiIiI1i1 = re . compile ( '<a href="(.+?)".+?target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( OO0O000 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + ( ii1111iII ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( ii1111iII ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + oOOOoo0O0OoO + '[/COLOR]' , '' , '' , i1 + 'f1.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for o0O , oO0O00oOOoooO in iiIiI1i1 :
   IiIi11iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O
   if 'bitcoin' in o0O :
    pass
   else :
    O0O00o0OOO0 ( '[COLORsteelblue]' + oO0O00oOOoooO + '[/COLOR]' , IiIi11iI , 15 , i1 + 'f1.jpg' , Oo0o0000o0o0 , '[COLORsteelblue]' + oO0O00oOOoooO + '[/COLOR]' )
    if 78 - 78: III1I11iiii1I - OoooooooOO - iiIiIIi / IiiI11Iiiii / II111iiii
def oOOo0O00o ( ) :
 O0O00o0OOO0 ( '[COLORorangered]Game Time Only[/COLOR]' , '' , '' , i1 + 'football.jpg' , Oo0o0000o0o0 , '' )
 O0OOO0OOoO0O = i1I1iI ( 'http://www.eplsite.com/nfl.html' )
 O00Oo000ooO0 = re . compile ( '<h4>NFL Live Streams</h4>(.+?)</section>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 OoO0O00 = re . compile ( '"acoordian-left-section">(.+?)</div>.+?<div class="vs"><span>(.+?)</span><div class="accordion-time">(.+?)</div></div>.+?<div class="acoordian-right-section">(.+?)</div>.+?<p>(.+?)</p>(.+?)</b></p>' , re . DOTALL ) . findall ( str ( O00Oo000ooO0 ) )
 for ii1111iII , iiiiI , time , oooOo0OOOoo0 , oOOOoo0O0OoO , OO0O000 in OoO0O00 :
  iiIiI1i1 = re . compile ( '<a href="(.+?)".+?target="_blank">(.+?)</a>' , re . DOTALL ) . findall ( str ( OO0O000 ) )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + ii1111iII + ' ' + iiiiI + ' ' + oooOo0OOOoo0 + '[/COLOR]' , '' , '' , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  O0O00o0OOO0 ( '[COLORorangered]' + '' + oOOOoo0O0OoO + '[/COLOR]' , '' , '' , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORorangered]' + ( oOOOoo0O0OoO ) . replace ( '&nbsp;' , '' ) + '[/COLOR]' )
  for o0O , oO0O00oOOoooO in iiIiI1i1 :
   IiIi11iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O
   if 'bitcoin' in o0O :
    pass
   else :
    O0O00o0OOO0 ( '[COLORsteelblue]' + oO0O00oOOoooO + '[/COLOR]' , IiIi11iI , 15 , i1 + 'nfl.jpg' , Oo0o0000o0o0 , '[COLORsteelblue]' + oO0O00oOOoooO + '[/COLOR]' )
    if 29 - 29: iI1I % iI1I
def Oo0O0 ( ) :
 Ooo0OOoOoO0 = [ 'Premier League' , 'La Liga' , 'Serie A' , 'Bundesliga' , 'Liguel' , 'UEFA' , 'FIFA' ]
 O0OOO0OOoO0O = requests . get ( o0O ) . content
 OoO0O00 = re . compile ( "<ul class='shnav simple-mainmenu'>(.+?)</nav>" , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 O00Oo000ooO0 = re . compile ( "<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<" , re . DOTALL ) . findall ( str ( OoO0O00 ) )
 for oOo0OOoO0 , oOOOoo0O0OoO in O00Oo000ooO0 :
  if not oOOOoo0O0OoO == 'Home' :
   pass
   II = 'http://www.replaymatches.com/' + oOo0OOoO0
   if oOOOoo0O0OoO in Ooo0OOoOoO0 :
    oOOO00o ( '[COLORred]' + oOOOoo0O0OoO + '[/COLOR]' , II , 900301 , i1 + 'football.jpg' , '' , '' )
   else :
    oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , II , 900301 , i1 + 'football.jpg' , '' , '' )
    if 93 - 93: ii1I11II1ii1i * OoooooooOO + IiiI11Iiiii
def IiII111i1i11 ( url ) :
 if 40 - 40: IiiI11Iiiii * ii1I11II1ii1i * i11iIiiIii
 IIIii1II1II = i1I1iI ( url )
 oo0OO00OoooOo = re . compile ( "<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>" , re . DOTALL ) . findall ( IIIii1II1II )
 II1i111Ii1i = re . compile ( "<a class='blog-pager-older-link'.+?href='(.+?)'" ) . findall ( IIIii1II1II )
 for url , oOOOoo0O0OoO , O00oO in oo0OO00OoooOo :
  oOOO00o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , url , 900302 , O00oO , i1 + 'football.jpg' , '' )
 for iii1 in II1i111Ii1i :
  oOOO00o ( '[COLORorangered]NEXT PAGE[/COLOR]' , iii1 , 900301 , i1 + 'NEXT.png' , '' , '' )
def ooO0oooOO0 ( url ) :
 O0OOO0OOoO0O = requests . get ( url ) . content
 OoO0O00 = re . compile ( '<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for oOo0OOoO0 , O00oO in OoO0O00 :
  if 'Highlight' in O00oO :
   oOOOoo0O0OoO = 'HighLights'
  elif '1st' in O00oO :
   oOOOoo0O0OoO = '1st Half'
  elif '2nd' in O00oO :
   oOOOoo0O0OoO = '2nd Half'
  else :
   oOOOoo0O0OoO = 'Full Match'
  o0o ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' , oOo0OOoO0 , 1001111 , O00oO , i1 + 'football.jpg' , '' , '' )
def oo0 ( ) :
 O0OOO0OOoO0O = requests . get ( O0O ( 'aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=' ) ) . content
 OoO0O00 = re . compile ( '<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for oOOOoo00 , OO0O000 in OoO0O00 :
  iiIiIIIiiI ( '[COLORred]' + oOOOoo00 + '[/COLOR]' , '' , '' , i1 + 'football.jpg' , i1 + 'football.jpg' , '' , '' )
  iiI1IIIi = re . compile ( "<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"" , re . DOTALL ) . findall ( str ( OO0O000 ) )
  for II11IiIi11 , IIOOO0O00O0OOOO in iiI1IIIi :
   iiIiIIIiiI ( '[COLORorangered]' + II11IiIi11 + '[/COLOR]' , '' , '' , IIOOO0O00O0OOOO , i1 + 'football.jpg' , '' , '' )
def I1iiii1I ( name , url ) :
 import urlresolver
 try :
  OOo0 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( OOo0 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 73 - 73: o0O0
 if 42 - 42: i11iIiiIii * iIii1I11I1II1 / iiIiIIi . i11iIiiIii % IiI1i11iii1
def i1iI ( url ) :
 IIIii1II1II = i1I1iI ( url )
 oo0OooOOo0 = re . compile ( '<span class="title">(.+?)</span>.+?<a class="no-style" href="([^"]*)"' , re . DOTALL ) . findall ( IIIii1II1II )
 for oOOOoo0O0OoO , url in oo0OooOOo0 :
  if 'Sport' in oOOOoo0O0OoO :
   IiI1iiiIii ( url )
def I1III1111iIi ( url ) :
 if url == 'http://' : return False
 try :
  I1i111I = urllib2 . Request ( url )
  I1i111I . add_header ( 'User-Agent' , iIiiiI )
  Ooo = urllib2 . urlopen ( I1i111I )
  Ooo . close ( )
 except Exception , Oo0oo0O0o00O :
  return Oo0oo0O0o00O
 return True
def I1i11 ( name , url ) :
 if 12 - 12: i1IIi + i1IIi - iiIiIIi * iiiIi % iiiIi - II111iiii
 if 52 - 52: IiiI11Iiiii . o0O0 + I1i1iii
 if 38 - 38: i1IIi - II111iiii . I1i1iii
 if 58 - 58: iI1I . o0O0 + i1I111I
 if 66 - 66: o0O0 / iii1I1 * OoooooooOO + OoooooooOO % IiI1i11iii1
 IIii1111 = name
 IIIii1II1II = i1I1iI ( url )
 OoO0O00 = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 iiIiI1i1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 I1iI = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 IIIIiIiIi1 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 I11iiiiI1i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( IIIii1II1II )
 iI1i11 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 for name , O00oO , OoOOoooOO0O , oO0O00oOOoooO , url in OoO0O00 :
  if IIii1111 in OoOOoooOO0O :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( name + oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , O00oO , O00oO , ( '[COLORsteelblue]' + ( name + oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00oO , OoOOoooOO0O , oO0O00oOOoooO , url in iiIiI1i1 :
  if IIii1111 in OoOOoooOO0O :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , O00oO , O00oO , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for OoOOoooOO0O , oO0O00oOOoooO , url in I1iI :
  if IIii1111 in OoOOoooOO0O :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for OoOOoooOO0O , O00oO , oO0O00oOOoooO , url in IIIIiIiIi1 :
  if IIii1111 in OoOOoooOO0O :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , O00oO , O00oO , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO0O00oOOoooO , url in I11iiiiI1i :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for OoOOoooOO0O , oO0O00oOOoooO , url in iI1i11 :
  if IIii1111 in OoOOoooOO0O :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
def ooo00Ooo ( name , url ) :
 IIIii1II1II = i1I1iI ( url )
 Oo0o0O00 = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 for oO0O00oOOoooO , url in Oo0o0O00 :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 40 - 40: OoooooooOO
def IiI1iiiIii ( url ) :
 url = url
 OOooo0oOO0O = [ '[COLORsteelblue](_) _No Group[/COLOR]' , '[COLORsteelblue](UK) United Kingdom[/COLOR]' , '[COLORsteelblue](US) United States[/COLOR]' , '[COLORsteelblue](AL) Albania[/COLOR]' , '[COLORsteelblue](AS) American Samoa[/COLOR]' , '[COLORsteelblue](AR) Argentina[/COLOR]' , '[COLORsteelblue](AU) Australia[/COLOR]' , '[COLORsteelblue](AZ) Azerbaijan[/COLOR]' , '[COLORsteelblue](BY) Belarus[/COLOR]' , '[COLORsteelblue](BE) Belgium[/COLOR]' , '[COLORsteelblue](BO) Bolivia[/COLOR]' , '[COLORsteelblue](BR) Brazil[/COLOR]' , '[COLORsteelblue](CM) Cameroon[/COLOR]' , '[COLORsteelblue](CA) Canada[/COLOR]' , '[COLORsteelblue](CO) Colombia[/COLOR]' , '[COLORsteelblue](CZ) Czech Republic[/COLOR]' , '[COLORsteelblue](DO) Dominican Republic[/COLOR]' , '[COLORsteelblue](EC) Ecuador[/COLOR]' , '[COLORsteelblue](FO) Faroe Islands[/COLOR]' , '[COLORsteelblue](FR) France[/COLOR]' , '[COLORsteelblue](DE) Germany[/COLOR]' , '[COLORsteelblue](GR) Greece[/COLOR]' , '[COLORsteelblue](IS) Iceland[/COLOR]' , '[COLORsteelblue](IN) India[/COLOR]' , '[COLORsteelblue](ID) Indonesia[/COLOR]' , '[COLORsteelblue](IR) Iran[/COLOR]' , '[COLORsteelblue](IT) Italy[/COLOR]' , '[COLORsteelblue](LA) Laos[/COLOR]' , '[COLORsteelblue](MO) Macau[/COLOR]' , '[COLORsteelblue](MX) Mexico[/COLOR]' , '[COLORsteelblue](NL) Netherlands[/COLOR]' , '[COLORsteelblue](NE) Niger[/COLOR]' , '[COLORsteelblue](PK) Pakistan[/COLOR]' , '[COLORsteelblue](PA) Panama[/COLOR]' , '[COLORsteelblue](PE) Peru[/COLOR]' , '[COLORsteelblue](PL) Poland[/COLOR]' , '[COLORsteelblue](PT) Portugal[/COLOR]' , '[COLORsteelblue](RO) Romania[/COLOR]' , '[COLORsteelblue](RU) Russia[/COLOR]' , '[COLORsteelblue](SL) Sierra Leone[/COLOR]' , '[COLORsteelblue](EX-YU) Slovenia[/COLOR]' , '[COLORsteelblue](SO) Somalia[/COLOR]' , '[COLORsteelblue](SP) Spain[/COLOR]' , '[COLORsteelblue](SE) Sweden[/COLOR]' , '[COLORsteelblue](CH) Switzerland[/COLOR]' , '[COLORsteelblue](TH) Thailand[/COLOR]' , '[COLORsteelblue](TR) Turkey[/COLOR]' , '[COLORsteelblue](UA) Ukraine[/COLOR]' , '[COLORsteelblue](VE) Venezuela[/COLOR]' , '[COLORsteelblue](WW) World Wide[/COLOR]' ]
 o00O0 = xbmcgui . Dialog ( ) . select ( '[COLORsteelblue]Select Country[/COLOR]' , OOooo0oOO0O )
 if o00O0 == 0 :
  oOOOoo0O0OoO = '(_)'
 if o00O0 == 1 :
  oOOOoo0O0OoO = '(UK)'
 if o00O0 == 2 :
  oOOOoo0O0OoO = '(US)'
 if o00O0 == 3 :
  oOOOoo0O0OoO = '(AL)'
 if o00O0 == 4 :
  oOOOoo0O0OoO = '(AS)'
 if o00O0 == 5 :
  oOOOoo0O0OoO = '(AR)'
 if o00O0 == 6 :
  oOOOoo0O0OoO = '(AU)'
 if o00O0 == 7 :
  oOOOoo0O0OoO = '(AZ)'
 if o00O0 == 8 :
  oOOOoo0O0OoO = '(BY)'
 if o00O0 == 9 :
  oOOOoo0O0OoO = '(BE)'
 if o00O0 == 10 :
  oOOOoo0O0OoO = '(BO)'
 if o00O0 == 11 :
  oOOOoo0O0OoO = '(BR)'
 if o00O0 == 12 :
  oOOOoo0O0OoO = '(CM)'
 if o00O0 == 13 :
  oOOOoo0O0OoO = '(CA)'
 if o00O0 == 14 :
  oOOOoo0O0OoO = '(CO)'
 if o00O0 == 15 :
  oOOOoo0O0OoO = '(CZ)'
 if o00O0 == 16 :
  oOOOoo0O0OoO = '(DO)'
 if o00O0 == 17 :
  oOOOoo0O0OoO = '(EC)'
 if o00O0 == 18 :
  oOOOoo0O0OoO = '(FO)'
 if o00O0 == 19 :
  oOOOoo0O0OoO = '(FR)'
 if o00O0 == 20 :
  oOOOoo0O0OoO = '(DE)'
 if o00O0 == 21 :
  oOOOoo0O0OoO = '(GR)'
 if o00O0 == 22 :
  oOOOoo0O0OoO = '(IS)'
 if o00O0 == 23 :
  oOOOoo0O0OoO = '(IN)'
 if o00O0 == 24 :
  oOOOoo0O0OoO = '(ID)'
 if o00O0 == 25 :
  oOOOoo0O0OoO = '(IR)'
 if o00O0 == 26 :
  oOOOoo0O0OoO = '(IT)'
 if o00O0 == 27 :
  oOOOoo0O0OoO = '(LA)'
 if o00O0 == 28 :
  oOOOoo0O0OoO = '(MO)'
 if o00O0 == 29 :
  oOOOoo0O0OoO = '(MX)'
 if o00O0 == 30 :
  oOOOoo0O0OoO = '(NL)'
 if o00O0 == 31 :
  oOOOoo0O0OoO = '(NE)'
 if o00O0 == 32 :
  oOOOoo0O0OoO = '(PK)'
 if o00O0 == 33 :
  oOOOoo0O0OoO = '(PA)'
 if o00O0 == 34 :
  oOOOoo0O0OoO = '(PE)'
 if o00O0 == 35 :
  oOOOoo0O0OoO = '(PL)'
 if o00O0 == 36 :
  oOOOoo0O0OoO = '(PT)'
 if o00O0 == 37 :
  oOOOoo0O0OoO = '(RO)'
 if o00O0 == 38 :
  oOOOoo0O0OoO = '(RU)'
 if o00O0 == 39 :
  oOOOoo0O0OoO = '(SL)'
 if o00O0 == 40 :
  oOOOoo0O0OoO = '(EX-YU)'
 if o00O0 == 41 :
  oOOOoo0O0OoO = '(SO)'
 if o00O0 == 42 :
  oOOOoo0O0OoO = '(SP)'
 if o00O0 == 43 :
  oOOOoo0O0OoO = '(SE)'
 if o00O0 == 44 :
  oOOOoo0O0OoO = '(CH)'
 if o00O0 == 45 :
  oOOOoo0O0OoO = '(TH)'
 if o00O0 == 46 :
  oOOOoo0O0OoO = '(TR)'
 if o00O0 == 47 :
  oOOOoo0O0OoO = '(UA)'
 if o00O0 == 48 :
  oOOOoo0O0OoO = '(VE)'
 if o00O0 == 49 :
  oOOOoo0O0OoO = '(WW)'
 I1i11 ( oOOOoo0O0OoO , url )
 if 25 - 25: ii1I11II1ii1i + IIII / IiiI11Iiiii . I1I1IIiiIiI1 % O0 * OO
def o0O0oo0OO0O ( url ) :
 IIIii1II1II = i1I1iI ( url )
 OoO0O00 = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 iiIiI1i1 = re . compile ( '#EXTINF:.+?tvg-logo="([^"]*)" group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 I1iI = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 IIIIiIiIi1 = re . compile ( '#EXTINF:.+?, group-title="([^"]*)" tvg-logo="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 I11iiiiI1i = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>' , re . DOTALL ) . findall ( IIIii1II1II )
 iI1i11 = re . compile ( '#EXTINF:.+? group-title="([^"]*)",(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 Oo0o0O00 = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( IIIii1II1II )
 for oOOOoo0O0OoO , O00oO , OoOOoooOO0O , oO0O00oOOoooO , url in OoO0O00 :
  if 'INFO' in OoOOoooOO0O :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oOOOoo0O0OoO + oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , O00oO , O00oO , ( '[COLORsteelblue]' + ( oOOOoo0O0OoO + oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for O00oO , OoOOoooOO0O , oO0O00oOOoooO , url in iiIiI1i1 :
  if 'INFO' in OoOOoooOO0O :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , O00oO , O00oO , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for OoOOoooOO0O , oO0O00oOOoooO , url in I1iI :
  if 'INFO' in OoOOoooOO0O :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for OoOOoooOO0O , O00oO , oO0O00oOOoooO , url in IIIIiIiIi1 :
  if 'INFO' in OoOOoooOO0O :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , O00oO , O00oO , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO0O00oOOoooO , url in I11iiiiI1i :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for OoOOoooOO0O , oO0O00oOOoooO , url in iI1i11 :
  if 'INFO' in OoOOoooOO0O :
   pass
  else :
   O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[COLORorangered] - ' + OoOOoooOO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) )
 for oO0O00oOOoooO , url in Oo0o0O00 :
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 300000005 , i1 + 'GTV.png' , i1 + 'GTV.png' , ( '[COLORsteelblue]' + ( oO0O00oOOoooO ) . replace ( '(Copyright © 2018 by TeamBlue)' , '' ) + '[/COLOR]' ) . replace ( '_' , ' ' ) )
  if 68 - 68: iii1I1 . IiI1i11iii1 % OoooooooOO . IiI1i11iii1
def OoooO ( url ) :
 if '.mkv' in url or '.MP3' in url or '.wma' in url or '.m4a' in url or '.m4a' in url or '.m4B' in url or '.m4a' in url or '.m4v' in url or '.mp3' in url or '.mp4' in url or '.avi' in url or '.flv' in url or '.mpeg' in url or '.3gp' in url or '.divx' in url or '.flac' in url or '.strm' in url :
  RESOLVEtest ( ( url ) . strip ( ) )
 else :
  try :
   iIII ( ( url ) . strip ( ) )
  except :
   pass
  else :
   iIII ( 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + url )
   if 3 - 3: iiIiIIi . iiiIi / II111iiii
def i11IiIiiIiII ( url ) :
 IIIii1II1II = cloudflare . source ( url )
 O00Oo000ooO0 = re . compile ( 'class="footer-univers">.+?<h2 class="tag-sport.+?>(.+?)</h2>(.+?)</span>' , re . DOTALL ) . findall ( IIIii1II1II )
 for oOOOoo0O0OoO , OO0O000 in O00Oo000ooO0 :
  OoO0O00 = re . compile ( '<a href="([^"]*)">.+?<h3>(.+?)</h3>' , re . DOTALL ) . findall ( str ( OO0O000 ) )
  O0O00o0OOO0 ( ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '\n' , ' ' ) . replace ( '_' , ' ' ) . replace ( ' ' , '' ) , '' , '' , i1 + 'extreme.jpg' , Oo0o0000o0o0 , ( '[COLORorangered]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( ' ' , '' ) )
  for oOo0OOoO0 , I1111i in OoO0O00 :
   oOOO00o ( ( '[COLORsteelblue]' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '-' ) . replace ( '' , '' ) . replace ( '\n' , ' ' ) , 'https://www.ridersmatch.com' + oOo0OOoO0 , 21 , i1 + 'extreme.jpg' , Oo0o0000o0o0 , ( '[COLORsteelblue]' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '-' ) . replace ( '' , '' ) . replace ( '\n' , ' ' ) )
   if 49 - 49: II111iiii
def Iiii1iI1i ( url ) :
 IIIii1II1II = cloudflare . source ( url )
 OoO0O00 = re . compile ( 'list-videothumbnail" href="(.+?)".+?title="(.+?)".+?style=".+?url(.+?)"' , re . DOTALL ) . findall ( IIIii1II1II )
 iii1 = re . compile ( '<a class="page-link nex" href="([^"]*)">Next</a>' , re . DOTALL ) . findall ( IIIii1II1II )
 for url , oOOOoo0O0OoO , O00oO in OoO0O00 :
  O00oO = O00oO . replace ( '(' , '' ) . replace ( ')' , '' )
  O0O00o0OOO0 ( ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '' ) . replace ( '_' , ' ' ) . replace ( '\n' , ' ' ) , 'https://www.ridersmatch.com' + url , 23 , O00oO , Oo0o0000o0o0 , ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '&#x27;' , '' ) . replace ( '_' , ' ' ) . replace ( '\n' , ' ' ) )
 for url in iii1 :
  oOOO00o ( ( '[COLORorangered]Next Page[/COLOR]' ) . replace ( '_' , ' ' ) , 'https://www.ridersmatch.com' + url , 21 , O00oO , Oo0o0000o0o0 , '[COLORorangered]Next Page[/COLOR]' )
  if 34 - 34: IiiI11Iiiii * iI1I . i1IIi * IiiI11Iiiii / IiiI11Iiiii
def IIiI1Ii ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OoO0O00 = re . compile ( 'src="//www.youtube.com/embed/(.+?)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url in OoO0O00 :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 57 - 57: III1I11iiii1I - IiiI11Iiiii - IiI1i11iii1 + OO
  if 30 - 30: IIII % i1I111I + i1IIi - IiI1i11iii1 - IIII
def III11I1 ( url ) :
 IIIii1II1II = i1I1iI ( url )
 oo0OooOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIii1II1II )
 for url , O00oO , ii1i1I1i , I11i1I1I , oOOOoo0O0OoO in oo0OooOOo0 :
  if '.php' in url :
   oOOO00o ( oOOOoo0O0OoO , url , 211 , O00oO , I11i1I1I , ii1i1I1i )
  else :
   oOOO00o ( oOOOoo0O0OoO , url , 212 , O00oO , I11i1I1I , ii1i1I1i )
def IIi1IIIi ( url , iconimage ) :
 O00oO = iconimage
 Ooo = oo0o0O00 . open ( url ) . read ( )
 if 99 - 99: IIII + OO * II111iiii . I1I1IIiiIiI1 - iiIiIIi
 try :
  o0OOOo = re . findall ( r'<a .*?>(.*?)</a>' , Ooo )
  ii1iiIiIII1ii = re . findall ( r'<a.*?href="(.*?)">' , Ooo )
  if 82 - 82: o0O0
  for oOo0OOoO0 in ii1iiIiIII1ii :
   if '.gif' in oOo0OOoO0 :
    pass
   if '.srt' in oOo0OOoO0 :
    pass
   elif '..' in oOo0OOoO0 :
    pass
   elif '.txt' in oOo0OOoO0 :
    pass
   elif '.nfo' in oOo0OOoO0 :
    pass
   elif '.jpg' in oOo0OOoO0 :
    pass
   elif '1-Irani/' in oOo0OOoO0 :
    pass
   elif 'index.php' in oOo0OOoO0 :
    pass
   elif '.png' in oOo0OOoO0 :
    pass
   elif '?C=M&O=D' in oOo0OOoO0 :
    pass
   elif '?C=M&O=A' in oOo0OOoO0 :
    pass
   elif '?C=N&O=D' in oOo0OOoO0 :
    pass
   elif '?C=N&O=A' in oOo0OOoO0 :
    pass
   elif '?C=S&O=A' in oOo0OOoO0 :
    pass
   elif '?C=S&O=D' in oOo0OOoO0 :
    pass
   elif '?C=N;O=D' in oOo0OOoO0 :
    pass
   elif '?C=M;O=A' in oOo0OOoO0 :
    pass
   elif '?C=S;O=A' in oOo0OOoO0 :
    pass
   elif '?C=D;O=A' in oOo0OOoO0 :
    pass
   elif 'Torrent' in oOo0OOoO0 :
    pass
   elif 'exe' in oOo0OOoO0 :
    pass
   elif 'public' in oOo0OOoO0 :
    pass
   elif '?C=D;O=A' in oOo0OOoO0 :
    pass
   elif 'pub' in oOo0OOoO0 :
    pass
   elif 'install' in oOo0OOoO0 :
    pass
   elif '?C=D;O=A' in oOo0OOoO0 :
    pass
   elif '?C=D;O=A' in oOo0OOoO0 :
    pass
   elif '.m3u' in oOo0OOoO0 :
    pass
   elif '?C=D;O=A' in oOo0OOoO0 :
    pass
   elif 'mpeg' in oOo0OOoO0 :
    pass
   elif '.doc' in oOo0OOoO0 :
    pass
   elif '.html' in oOo0OOoO0 :
    pass
   elif 'boss' in oOo0OOoO0 :
    pass
   elif 'plex' in oOo0OOoO0 :
    pass
   else :
    oOOOoo0O0OoO = oOo0OOoO0
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
     if 65 - 65: IiiI11Iiiii . OoooooooOO / iiIiIIi . i1IIi * OO
     if 19 - 19: i11iIiiIii + OoooooooOO - iiiIi - IiI1i11iii1
    if '.mkv' in oOo0OOoO0 or '.m4B' in oOo0OOoO0 or '.m4v' in oOo0OOoO0 or '.mp3' in oOo0OOoO0 or '.mp4' in oOo0OOoO0 or '.avi' in oOo0OOoO0 or '.flv' in oOo0OOoO0 or '.mpeg' in oOo0OOoO0 or '.3gp' in oOo0OOoO0 or '.divx' in oOo0OOoO0 or '.strm' in oOo0OOoO0 :
     Iii1iiIi1II ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , url + oOo0OOoO0 , 222 , O00oO , I11i1I1I , '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
     if 60 - 60: iI1I - iii1I1 * IiI1i11iii1 % II111iiii
    else :
     oOOO00o ( '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' , url + oOo0OOoO0 , 212 , O00oO , I11i1I1I , '[COLORsteelblue]' + oOOOoo0O0OoO + '[/COLOR]' )
     if 62 - 62: iIii1I11I1II1
     if 12 - 12: III1I11iiii1I / I1I1IIiiIiI1
     if 42 - 42: iiiIi
     if 19 - 19: iii1I1 % iiIiIIi * iIii1I11I1II1 + iI1I
 except Exception , Oo0oo0O0o00O :
  print str ( Oo0oo0O0o00O )
def iii11I ( name , url , mode , iconimage , description = "" , isFolder = True , background = None ) :
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 if 30 - 30: OoooooooOO - i1I111I
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 if background :
  Ooo00O0o . setProperty ( 'fanart_image' , background )
 if mode == 1 or mode == 2 :
  Ooo00O0o . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10008 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=22)' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) ) ) ] )
 elif mode == 404 :
  Ooo00O0o . setProperty ( 'IsPlayable' , 'true' )
  Ooo00O0o . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10009 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
 elif mode == 556 :
  Ooo00O0o . setProperty ( 'IsPlayable' , 'true' )
  Ooo00O0o . addContextMenuItems ( items = [ ( '{0}' . format ( oOo0oooo00o ( 10010 ) . encode ( 'utf-8' ) ) , 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})' . format ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , iconimage , name ) ) ] )
  if 72 - 72: iIii1I11I1II1 * IIII % IiiI11Iiiii / OO
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = isFolder )
 if 35 - 35: IiiI11Iiiii + i1IIi % iiIiIIi % IiI1i11iii1 + iii1I1
def iiiI ( handle , url , listitem , isFolder ) :
 if 29 - 29: IiI1i11iii1 / II111iiii / IiiI11Iiiii * III1I11iiii1I
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 10 - 10: I1i1iii % ii1I11II1ii1i * ii1I11II1ii1i . IiI1i11iii1 / IIII % III1I11iiii1I
 if 49 - 49: OO / iii1I1 + O0 * I1I1IIiiIiI1
 if 28 - 28: IiiI11Iiiii + i11iIiiIii / IiI1i11iii1 % i1I111I % iiiIi - O0
def ooo0OOO ( title , message , times = 2000 , icon = o0oOoO00o ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def iii1Ii1Ii1 ( ) :
 IIi = ooO0oOo0o ( )
 OOii111IiiI1 = IIi . replace ( I1ii11iIi11i , "" )
 if os . path . exists ( IIi ) or not IIi == False :
  ii11i1iIiII1 = open ( IIi , mode = 'r' ) ; o00oo0 = ii11i1iIiII1 . read ( ) ; ii11i1iIiII1 . close ( )
  oooooOOO000Oo ( "%s - %s" % ( IiII , OOii111IiiI1 ) , o00oo0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def ooO0oOo0o ( ) :
 Ooo00OoOOO = False
 if os . path . exists ( os . path . join ( I1ii11iIi11i , 'xbmc.log' ) ) :
  Ooo00OoOOO = os . path . join ( I1ii11iIi11i , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'kodi.log' ) ) :
  Ooo00OoOOO = os . path . join ( I1ii11iIi11i , 'kodi.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'spmc.log' ) ) :
  Ooo00OoOOO = os . path . join ( I1ii11iIi11i , 'spmc.log' )
 elif os . path . exists ( os . path . join ( I1ii11iIi11i , 'tvmc.log' ) ) :
  Ooo00OoOOO = os . path . join ( I1ii11iIi11i , 'tvmc.log' )
 return Ooo00OoOOO
 if 98 - 98: iIii1I11I1II1 * iiIiIIi * III1I11iiii1I + IiiI11Iiiii % i11iIiiIii % O0
 if 27 - 27: O0
 if 79 - 79: I1I1IIiiIiI1 - IiI1i11iii1 + I1I1IIiiIiI1 . iii1I1
 if 28 - 28: i1IIi - o0O0
 if 54 - 54: o0O0 - O0 % III1I11iiii1I
def oooooOOO000Oo ( heading , announce ) :
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
   try : ii11i1iIiII1 = open ( announce ) ; Ooii11i11i1 = ii11i1iIiII1 . read ( )
   except : Ooii11i11i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Ooii11i11i1 ) )
   return
 o00oOO0 ( )
 o00oOO0 ( )
 if 53 - 53: OoooooooOO % IIII . ii1I11II1ii1i / i11iIiiIii % o0O0
def iIiIIIIIii ( ) :
 Iii1iiIi1II ( '[COLORorangered]Delete Packages[/COLOR]' , '' , 6 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 Iii1iiIi1II ( '[COLORorangered]Delete Cache[/COLOR]' , '' , 7 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 Iii1iiIi1II ( '[COLORorangered]View Log File[/COLOR]' , '' , 50000 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 Iii1iiIi1II ( '[COLORorangered]Force Refresh[/COLOR]' , '' , 50001 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 Iii1iiIi1II ( '[COLORorangered]Force Close[/COLOR]' , '' , 8 , i1 + '5.png' , Oo0o0000o0o0 , '' )
 if 58 - 58: I1I1IIiiIiI1 / ii1I11II1ii1i . i1I111I / OoooooooOO + I1i1iii
 if 86 - 86: IiI1i11iii1 * iI1I + IiI1i11iii1 + II111iiii
 if 8 - 8: I1i1iii - o0O0 / IiiI11Iiiii
def oo0oOoo ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def oOOO0o00o ( url ) :
 if url == 'http://' : return False
 try :
  I1i111I = urllib2 . Request ( url )
  I1i111I . add_header ( 'User-Agent' , iIiiiI )
  Ooo = urllib2 . urlopen ( I1i111I )
  Ooo . close ( )
 except Exception , Oo0oo0O0o00O :
  return Oo0oo0O0o00O
 return True
 if 1 - 1: iI1I / ii1I11II1ii1i * IiiI11Iiiii
 if 1 - 1: IiI1i11iii1 * I1I1IIiiIiI1 . i1I111I / O0
 if 100 - 100: I1i1iii . I1I1IIiiIiI1 * iiiIi % O0 * O0
def IIIii1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv Sports" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By GenieTv Sports[/COLOR]" )
 return
 if 71 - 71: II111iiii / i1IIi . iiIiIIi % OoooooooOO . i1I111I
def Iiiiii111i1ii ( url ) :
 print '###' + IiII + ' - DELETING Addons20.db ###'
 i1i1iII1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 iii11i1IIII = os . path . join ( i1i1iII1 , 'Addons20.db' )
 try :
  os . remove ( iii11i1IIII )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== ' + IiII + ' - DELETING    ' + str ( iii11i1IIII ) + '    ==='
  ii11iIi1I . ok ( IiII , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( IiII , "       No File To Remove" )
 return
 if 26 - 26: O0 . OO * I1i1iii . iI1I % i11iIiiIii
 if 47 - 47: o0O0 - iiiIi
 if 3 - 3: i1IIi / II111iiii / i11iIiiIii * i1IIi - II111iiii
 if 42 - 42: II111iiii . OoooooooOO . I1I1IIiiIiI1 * iii1I1
 if 81 - 81: IIII * I1I1IIiiIiI1 + I1i1iii + iiiIi - OoooooooOO
def i1I1iI ( url ) :
 I1i111I = urllib2 . Request ( url )
 I1i111I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ooo = urllib2 . urlopen ( I1i111I )
 oOo0OOoO0 = Ooo . read ( )
 Ooo . close ( )
 return oOo0OOoO0
def o00oOO0 ( title , msg ) :
 class oooooOOO000Oo ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . okbutton = 201
   self . showdialog ( )
   if 32 - 32: IIII * O0
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( title )
   self . getControl ( self . msg ) . setText ( msg )
   self . setFocusId ( self . scrollbar )
   if 100 - 100: IiiI11Iiiii % iIii1I11I1II1 * II111iiii - o0O0
  def onClick ( self , controlId ) :
   if ( controlId == self . okbutton ) :
    self . close ( )
    if 92 - 92: IiiI11Iiiii
  def onAction ( self , action ) :
   if action == ACTION_PREVIOUS_MENU : self . close ( )
   elif action == ACTION_NAV_BACK : self . close ( )
   if 22 - 22: iiiIi % o0O0 * iiIiIIi / III1I11iiii1I % i11iIiiIii * IiI1i11iii1
 Oo00OoOo = oooooOOO000Oo ( "Textbox.xml" , o0OOO . getAddonInfo ( 'path' ) , 'DefaultSkin' , title = title , msg = msg )
 Oo00OoOo . doModal ( )
 del Oo00OoOo
def oooooOOO000Oo ( heading , announce ) :
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
   try : ii11i1iIiII1 = open ( announce ) ; Ooii11i11i1 = ii11i1iIiII1 . read ( )
   except : Ooii11i11i1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Ooii11i11i1 ) )
   return
 o00oOO0 ( )
 o00oOO0 ( )
def ii1ii111 ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 i11111I1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1Oo0000oOo , I11o0oO00oO0o0o0 , I1I in os . walk ( i11111I1I ) :
   ooooo = 0
   ooooo += len ( I1I )
   if 1 - 1: IiiI11Iiiii % i1I111I * iiiIi
   if 55 - 55: i1I111I
   if ooooo > 0 :
    if 87 - 87: OoooooooOO % o0O0 . iI1I / IiiI11Iiiii
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( ooooo ) + " files found" , "Do you want to delete them?" ) :
     if 8 - 8: IiI1i11iii1 + I1I1IIiiIiI1
     for ii11i1iIiII1 in I1I :
      os . unlink ( os . path . join ( ii1Oo0000oOo , ii11i1iIiII1 ) )
     for oOOo0o0oo in I11o0oO00oO0o0o0 :
      shutil . rmtree ( os . path . join ( ii1Oo0000oOo , oOOo0o0oo ) )
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
 i11iiiiI1i ( url )
 return
def i11iiiiI1i ( url ) :
 iIIii = os . path . join ( I1i1iiI1 , 'addon_data' )
 i1iIiIi1I = [
 ( iIIii ) ,
 ( oo00 ) ,
 ( os . path . join ( O0oo0OO0 , 'cache' ) ) ,
 ( os . path . join ( O0oo0OO0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo00 , 'plugin.video.GenieTv_Sports' , 'Images' ) ) ,
 ( os . path . join ( iIIii , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( iIIii , 'plugin.video.GenieTv_Sports' , 'Images' ) ) ]
 if 45 - 45: i1IIi + II111iiii
 IiII1II11I = 0
 if 54 - 54: ii1I11II1ii1i + O0 + IiI1i11iii1 * I1i1iii - III1I11iiii1I % iii1I1
 for I111 in i1iIiIi1I :
  if os . path . exists ( I111 ) and not I111 in [ oo00 , iIIii ] :
   for ii1Oo0000oOo , I11o0oO00oO0o0o0 , I1I in os . walk ( I111 ) :
    ooooo = 0
    ooooo += len ( I1I )
    if ooooo > 0 :
     for ii11i1iIiII1 in I1I :
      if not ii11i1iIiII1 in iiIIIII1i1iI :
       try :
        os . unlink ( os . path . join ( ii1Oo0000oOo , ii11i1iIiII1 ) )
       except :
        pass
      else : IIi ( 'Ignore Log File: %s' % ii11i1iIiII1 )
     for oOOo0o0oo in I11o0oO00oO0o0o0 :
      try :
       shutil . rmtree ( os . path . join ( ii1Oo0000oOo , oOOo0o0oo ) )
       IiII1II11I += 1
       IIi ( "[Success] cleared %s files from %s" % ( str ( ooooo ) , os . path . join ( I111 , oOOo0o0oo ) ) )
      except :
       IIi ( "[Failed] to wipe cache in: %s" % os . path . join ( I111 , oOOo0o0oo ) )
  else :
   for ii1Oo0000oOo , I11o0oO00oO0o0o0 , I1I in os . walk ( I111 ) :
    for oOOo0o0oo in I11o0oO00oO0o0o0 :
     if 'cache' in oOOo0o0oo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ii1Oo0000oOo , oOOo0o0oo ) )
       IiII1II11I += 1
       IIi ( "[Success] wiped %s " % os . path . join ( I111 , oOOo0o0oo ) )
      except :
       IIi ( "[Failed] to wipe cache in: %s" % os . path . join ( I111 , oOOo0o0oo ) )
       if 13 - 13: OO * iii1I1 * o0O0
 ooo0OOO ( IiII , 'Clear Cache: Removed %s Files' % IiII1II11I )
def IiIIiiI11III ( url ) :
 print '###' + IiII + ' - DELETING PACKAGES###'
 i11111I1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1Oo0000oOo , I11o0oO00oO0o0o0 , I1I in os . walk ( i11111I1I ) :
   ooooo = 0
   ooooo += len ( I1I )
   if 42 - 42: iiIiIIi
   if 76 - 76: iiIiIIi * II111iiii . iI1I - iiiIi + iii1I1 + i11iIiiIii
   if ooooo > 0 :
    if 28 - 28: iii1I1
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( ooooo ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: ii1I11II1ii1i
     for ii11i1iIiII1 in I1I :
      os . unlink ( os . path . join ( ii1Oo0000oOo , ii11i1iIiII1 ) )
     for oOOo0o0oo in I11o0oO00oO0o0o0 :
      shutil . rmtree ( os . path . join ( ii1Oo0000oOo , oOOo0o0oo ) )
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
 if 34 - 34: I1i1iii % ii1I11II1ii1i
def IiI1i ( ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 o00O0 = ii11iIi1I . yesno ( 'Force Close GenieTv Sports' , 'You are about to close GenieTv Sports' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o00O0 == 0 : return
 elif o00O0 == 1 : pass
 oO0oOOoo00000 = oo0oOoo ( )
 IIi ( "Platform: " + str ( oO0oOOoo00000 ) )
 os . _exit ( 1 )
 IIi ( "Force close failed!  Trying alternate methods." )
 if oO0oOOoo00000 == 'osx' :
  IIi ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oO0oOOoo00000 == 'linux' :
  IIi ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oO0oOOoo00000 == 'android' :
  IIi ( "############ try android force close #################" )
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
 elif oO0oOOoo00000 == 'windows' :
  IIi ( "############ try windows force close #################" )
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
  IIi ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  IIi ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 52 - 52: iI1I
def iIII ( url ) :
 import urlresolver
 try :
  OOo0 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OOo0 , xbmcgui . ListItem ( oOOOoo0O0OoO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( oOOOoo0O0OoO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def oo0oOoo ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 51 - 51: ii1I11II1ii1i
def IIi ( log ) :
 xbmc . log ( "[%s]: %s" % ( IiII , log ) )
 if not os . path . exists ( oo00 ) : os . makedirs ( oo00 )
 if not os . path . exists ( i1111 ) : ii11i1iIiII1 = open ( i1111 , 'w' ) ; ii11i1iIiII1 . close ( )
 with open ( i1111 , 'a' ) as ii11i1iIiII1 :
  o00o = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  ii11i1iIiII1 . write ( o00o . rstrip ( '\r\n' ) + '\n' )
  if 46 - 46: II111iiii % I1I1IIiiIiI1 % iIii1I11I1II1 - iiiIi . OoooooooOO - ii1I11II1ii1i
def o00ooO00O ( ) :
 try :
  oo00o0 = getSet ( "core-player" )
  if ( oo00o0 == 'DVDPLAYER' ) : OooOOOOoO00OoOO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oo00o0 == 'MPLAYER' ) : OooOOOOoO00OoOO = xbmc . PLAYER_CORE_MPLAYER
  elif ( oo00o0 == 'PAPLAYER' ) : OooOOOOoO00OoOO = xbmc . PLAYER_CORE_PAPLAYER
  else : OooOOOOoO00OoOO = xbmc . PLAYER_CORE_AUTO
 except : OooOOOOoO00OoOO = xbmc . PLAYER_CORE_AUTO
 return OooOOOOoO00OoOO
 return True
 if 85 - 85: iii1I1 - iIii1I11I1II1 / O0
def iiIiIIIiiI ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00oo0000OO = True
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo00O0o . setProperty ( "Fanart_Image" , fanart )
 Oo00oo0000OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = True )
 return Oo00oo0000OO
 if 69 - 69: IiiI11Iiiii - OO / i11iIiiIii + iiIiIIi % OoooooooOO
 if 73 - 73: IIII - I1i1iii
def o0o ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00oo0000OO = True
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00oooo00o0O = [ ]
  O00oooo00o0O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  Ooo00O0o . addContextMenuItems ( O00oooo00o0O )
 Oo00oo0000OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = False )
 return Oo00oo0000OO
 if 9 - 9: iI1I % iI1I % II111iiii
def oOOO00o ( name , url , mode , iconimage , fanart , description ) :
 if 30 - 30: ii1I11II1ii1i + I1i1iii - ii1I11II1ii1i . ii1I11II1ii1i - II111iiii + O0
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00oo0000OO = True
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo00O0o . setProperty ( "Fanart_Image" , fanart )
 Oo00oo0000OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = True )
 return Oo00oo0000OO
 if 86 - 86: i1IIi
def Iii1iiIi1II ( name , url , mode , iconimage , fanart , description ) :
 if 41 - 41: i1I111I * IiI1i11iii1 / i1I111I % iii1I1
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00oo0000OO = True
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo00O0o . setProperty ( "Fanart_Image" , fanart )
 Oo00oo0000OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = False )
 return Oo00oo0000OO
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00oo0000OO = True
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00oooo00o0O = [ ]
  if showcontext == 'fav' :
   O00oooo00o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   O00oooo00o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ooo00O0o . addContextMenuItems ( O00oooo00o0O )
 Oo00oo0000OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = False )
 return Oo00oo0000OO
def Ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo00oo0000OO = True
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O00oooo00o0O = [ ]
  O00oooo00o0O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O00oooo00o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   O00oooo00o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooo00O0o . addContextMenuItems ( O00oooo00o0O )
 Oo00oo0000OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = True )
 return Oo00oo0000OO
def oO0oOOO0Ooo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1Iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo00oo0000OO = True
 Ooo00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O00oooo00o0O = [ ]
  O00oooo00o0O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O00oooo00o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iI111I11I1I1 :
   O00oooo00o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooo00O0o . addContextMenuItems ( O00oooo00o0O )
 Oo00oo0000OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Iii1 , listitem = Ooo00O0o , isFolder = False )
 return Oo00oo0000OO
 if 38 - 38: iI1I
def oOo0OoOOo0 ( ) :
 iII11I1Ii1 = [ ]
 o0o0 = sys . argv [ 2 ]
 if len ( o0o0 ) >= 2 :
  oOo0oO = sys . argv [ 2 ]
  IIi1IIIIi = oOo0oO . replace ( '?' , '' )
  if ( oOo0oO [ len ( oOo0oO ) - 1 ] == '/' ) :
   oOo0oO = oOo0oO [ 0 : len ( oOo0oO ) - 2 ]
  OOOoO = IIi1IIIIi . split ( '&' )
  iII11I1Ii1 = { }
  for I1i in range ( len ( OOOoO ) ) :
   iiiIIiIi1 = { }
   iiiIIiIi1 = OOOoO [ I1i ] . split ( '=' )
   if ( len ( iiiIIiIi1 ) ) == 2 :
    iII11I1Ii1 [ iiiIIiIi1 [ 0 ] ] = iiiIIiIi1 [ 1 ]
    if 34 - 34: III1I11iiii1I
 return iII11I1Ii1
 if 91 - 91: iIii1I11I1II1 % I1I1IIiiIiI1 . iIii1I11I1II1 % i1IIi / II111iiii * i1I111I
 if 10 - 10: II111iiii . o0O0
oOo0oO = oOo0OoOOo0 ( )
o0O = None
oOOOoo0O0OoO = None
I1iOOOO = None
ooO0oO00O0o = None
I11i1I1I = None
ooOO00oOOo000 = None
IIii11II11II1 = None
if 10 - 10: iI1I / iiiIi % iiIiIIi * IiiI11Iiiii
if 6 - 6: o0O0 . ii1I11II1ii1i * i1I111I . i1IIi
try :
 IIii11II11II1 = int ( oOo0oO [ "fav_mode" ] )
except :
 pass
 if 98 - 98: i1IIi
try :
 o0O = urllib . unquote_plus ( oOo0oO [ "url" ] )
except :
 pass
try :
 oOOOoo0O0OoO = urllib . unquote_plus ( oOo0oO [ "name" ] )
except :
 pass
try :
 ooO0oO00O0o = urllib . unquote_plus ( oOo0oO [ "iconimage" ] )
except :
 pass
try :
 I1iOOOO = int ( oOo0oO [ "mode" ] )
except :
 pass
try :
 I11i1I1I = urllib . unquote_plus ( oOo0oO [ "fanart" ] )
except :
 pass
try :
 ooOO00oOOo000 = urllib . unquote_plus ( oOo0oO [ "description" ] )
except :
 pass
 if 65 - 65: i1I111I / OO % ii1I11II1ii1i
 if 45 - 45: i1I111I
print str ( i1i1II ) + ': ' + str ( o0OoOoOO00 )
print "Mode: " + str ( I1iOOOO )
print "URL: " + str ( o0O )
print "Name: " + str ( oOOOoo0O0OoO )
print "IconImage: " + str ( ooO0oO00O0o )
if 66 - 66: OO
if 56 - 56: O0
def OOo00 ( content , viewType ) :
 if 37 - 37: i1IIi
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OOO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OOO . getSetting ( viewType ) )
  if 46 - 46: i1I111I - IiI1i11iii1 - IIII . i1IIi
  if 35 - 35: II111iiii * IiI1i11iii1 - OoooooooOO . IiI1i11iii1 . IiI1i11iii1
if I1iOOOO == None : oo0Oo00Oo0 ( )
elif I1iOOOO == 11111 : I1I1i ( )
elif I1iOOOO == 1 : Genres ( )
elif I1iOOOO == 2 : Lists ( o0O , ooO0oO00O0o )
elif I1iOOOO == 3 : all_mov ( )
elif I1iOOOO == 4 : Search ( )
elif I1iOOOO == 5 : iIiIIIIIii ( )
elif I1iOOOO == 6 : IiIIiiI11III ( o0O )
elif I1iOOOO == 7 : i11iiiiI1i ( o0O )
elif I1iOOOO == 8 : IiI1i ( )
elif I1iOOOO == 10 : MyAccDetails ( )
elif I1iOOOO == 15 : iIII ( o0O )
elif I1iOOOO == 16 : yt . PlayVideo ( o0O )
elif I1iOOOO == 18 : o0OOO . openSettings ( sys . argv [ 0 ] )
elif I1iOOOO == 20 : i11IiIiiIiII ( o0O )
elif I1iOOOO == 21 : Iiii1iI1i ( o0O )
elif I1iOOOO == 22 : Xtreme2 ( o0O )
elif I1iOOOO == 23 : IIiI1Ii ( o0O )
elif I1iOOOO == 30 : oOOoo0Oo ( )
elif I1iOOOO == 31 : oOo00oOoO000 ( )
elif I1iOOOO == 32 : OO00Oo ( )
elif I1iOOOO == 33 : o000O0o ( )
elif I1iOOOO == 34 : O0O0OOOOoo ( oOOOoo0O0OoO , ooOO00oOOo000 )
elif I1iOOOO == 40 : ii11i1 ( )
elif I1iOOOO == 41 : oO0Oo ( o0O )
elif I1iOOOO == 211 : III11I1 ( o0O )
elif I1iOOOO == 212 : IIi1IIIi ( o0O , ooO0oO00O0o )
elif I1iOOOO == 222 : iIII ( o0O )
elif I1iOOOO == 1000 : from imports import kodicelticfc
elif I1iOOOO == 1001 : from imports import plzsoccer
elif I1iOOOO == 1002 : from imports import podcasts
elif I1iOOOO == 1003 : from imports import rebeltunes
elif I1iOOOO == 1004 : from imports import greenbrigade
elif I1iOOOO == 1010 : from imports import Club_Teams
elif I1iOOOO == 1005 : Ii11I ( )
elif I1iOOOO == 1006 : iii11 ( )
elif I1iOOOO == 1007 : OOO0OOO00oo ( )
elif I1iOOOO == 1008 : from imports import rangers
elif I1iOOOO == 50000 : iii1Ii1Ii1 ( )
elif I1iOOOO == 50001 : IIIii1 ( )
elif I1iOOOO == 50002 : Iiiiii111i1ii ( o0O )
elif I1iOOOO == 300000000 : FluxUstv ( )
elif I1iOOOO == 300000001 : o0O0oo0OO0O ( o0O )
elif I1iOOOO == 300000002 : i1iI ( o0O )
elif I1iOOOO == 300000003 : I1i11 ( oOOOoo0O0OoO , o0O )
elif I1iOOOO == 300000004 : IiI1iiiIii ( o0O )
elif I1iOOOO == 300000005 : OoooO ( o0O )
elif I1iOOOO == 300000006 : ooo00Ooo ( oOOOoo0O0OoO , o0O )
if 11 - 11: I1i1iii / i1I111I + IiI1i11iii1 % iIii1I11I1II1
elif I1iOOOO == 900300 : Oo0O0 ( )
elif I1iOOOO == 900301 : IiII111i1i11 ( o0O )
elif I1iOOOO == 900302 : ooO0oooOO0 ( o0O )
elif I1iOOOO == 90030 : oo0 ( )
elif I1iOOOO == 1001111 : I1iiii1I ( oOOOoo0O0OoO , o0O )
if 42 - 42: iiIiIIi * i1I111I % IiiI11Iiiii - i1I111I . i11iIiiIii - I1i1iii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
