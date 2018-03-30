import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon


YOUTUBE_CHANNEL_ID_1 = "UCtS-X1mtrROC6fXMEn0UpYg"
YOUTUBE_CHANNEL_ID_2 = "UCNVnnDQ4qPw8kiQBn5JcE-w"


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
        title="The Celtic Underground",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i.imgur.com/T5XtcA0.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Hail Hail Media",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://i.imgur.com/rfNIPpf.jpg",
        folder=True )	
		
run() 
