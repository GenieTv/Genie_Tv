import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon


YOUTUBE_CHANNEL_ID_1 = "UCtHy50ARI1HaAQF6249P2fw"
YOUTUBE_CHANNEL_ID_2 = "UCjciOGFifcBkKofmmLgorFQ"
YOUTUBE_CHANNEL_ID_3 = "UCa-cfv57qlzhl3JW-Vvy6Aw"
YOUTUBE_CHANNEL_ID_4 = "UCekTHbKH8Zjjun5NLCKftUA"
YOUTUBE_CHANNEL_ID_5 = "UCoHnuVKDA26c_GTwF7YSpXQ"
YOUTUBE_CHANNEL_ID_6 = "UCNlVChzUC4v1atSYlKT1R6Q"
YOUTUBE_CHANNEL_ID_7 = "UCvXP5FyT0phf3pQndHLMZ2A"
YOUTUBE_CHANNEL_ID_8 = "UCPgcUObcubzcuO0gjxymTkg"
YOUTUBE_CHANNEL_ID_9 = "UCZ0h_XLpwYfQTtks54Cys8Q"
YOUTUBE_CHANNEL_ID_10 = "UCw2Mtabr0uuy0acDP1MWbvg"
YOUTUBE_CHANNEL_ID_11 = "UC6yTsgvPlVn0ONMFQkvoaBQ"


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))
		
    plugintools.add_item( 
        #action="", 
        title="Wolftones",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i.imgur.com/I5KPzpQ.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Charlie & The Bhoys",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://i.imgur.com/nIoWKsv.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Athenrye",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://i.imgur.com/tcWMF5L.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Eire Og",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://i.imgur.com/OO2SdZF.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Druids",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://i.imgur.com/Tcm2ZSy.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Wakes",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://i.imgur.com/nPJVVtO.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Glasnevin",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://i.imgur.com/OaDeyzR.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Spirit Of Freedom",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://i.imgur.com/2fdDOUA.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Irish Brigade",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://i.imgur.com/NTXrKYD.gif",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Christy Moore",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://i.imgur.com/JJYaXfI.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Billy No Well",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://i.imgur.com/4LVhjKH.jpg",
        folder=True )
		
run() 
