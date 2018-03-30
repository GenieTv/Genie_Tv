import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon


YOUTUBE_CHANNEL_ID_NUFC = "UCywGl_BPp9QhD0uAcP2HsJw"
YOUTUBE_CHANNEL_ID_1 = "UCBN-bb-hE7jYlcp4exwXRsQ"
YOUTUBE_CHANNEL_ID_2 = "UCVaGyBPoEAZItDjlFPsRcSA"
YOUTUBE_CHANNEL_ID_3 = "UC6yW44UGJJBvYTlfC7CRg2Q"
YOUTUBE_CHANNEL_ID_4 = "UCkzCjdRMrW2vXLx8mvPVLdQ"
YOUTUBE_CHANNEL_ID_5 = "UC9LQwHZoucFT94I2h6JOcjw"
YOUTUBE_CHANNEL_ID_6 = "UCpryVRk_VDudG8SHXgWcG0w"
YOUTUBE_CHANNEL_ID_7 = "UCtK4QAczAN2mt2ow_jlGinQ"
YOUTUBE_CHANNEL_ID_8 = "UCU2PacFf99vhb3hNiYDmxww"
YOUTUBE_CHANNEL_ID_9 = "UCEg25rdRZXg32iwai6N6l0w"


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
        title="[COLORorangered]Newcastle United[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_NUFC+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/hif/2/25/Newcastle_United_Logo.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]Celtic[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://vignette.wikia.nocookie.net/fifa/images/a/a8/Celtic_FC.png/revision/latest?cb=20180213000259",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]Rangers[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Rangers_FC.svg/1200px-Rangers_FC.svg.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]MUFC[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://pngimg.com/uploads/manchester_united/manchester_united_PNG18.png",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]MCFC[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://vignette.wikia.nocookie.net/clashofclans/images/e/e9/Manchester-city-logo-1-.png/revision/latest?cb=20150222145226",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]Liverpool FC[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://pluspng.com/img-png/logo-liverpool-fc-png-liverpool-fc-logo-500.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]Aresnal[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://www.stickpng.com/assets/images/580b57fcd9996e24bc43c4df.png",
        folder=True )
			
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]Everton[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://webspace.webring.com/people/og/goneil/celts2004.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]Chelsea[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://www.seeklogo.net/wp-content/uploads/2015/07/chelsea-fc-logo-preview.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLORorangered]Tottenham[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://www.stickpng.com/assets/images/580b57fcd9996e24bc43c4ee.png",
        folder=True )
		
run() 
