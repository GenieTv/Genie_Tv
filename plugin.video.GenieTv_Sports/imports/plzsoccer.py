import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon


YOUTUBE_CHANNEL_ID_1 = "PLCTeUr0E36UmHweO-wTv85jVkkYJggfn_"


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
        title="PLZ Soccer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i.imgur.com/hyCe245.jpg",
        folder=True )
		
run() 
