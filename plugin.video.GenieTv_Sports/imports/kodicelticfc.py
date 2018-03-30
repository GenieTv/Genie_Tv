import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon


YOUTUBE_CHANNEL_ID_1 = "PLQ7SMbALyYiI-2rlAlm62ab6KSXi2f4K2"
YOUTUBE_CHANNEL_ID_2 = "PLBRPzkoqE1iniYZ4fE2qiuJ6ehspplc1z"
YOUTUBE_CHANNEL_ID_3 = "PLZOkXQ8Q1hqshXO_eG2MxvM_IVWTBUUYe"
YOUTUBE_CHANNEL_ID_4 = "PLb0e0LTGZwKmvV72rfTfRJ_cFU0eZoFVv"
YOUTUBE_CHANNEL_ID_5 = "PLZOkXQ8Q1hqtz-PS3ZMv624AxlniijjBE"
YOUTUBE_CHANNEL_ID_6 = "PLRAth6hyT-9EELQCluctR-_b4mD0dtGyG"
YOUTUBE_CHANNEL_ID_7 = "PLEkGkHdMZ4chrpNSrctqPluHMNzAghhXh"
YOUTUBE_CHANNEL_ID_8 = "UCBN-bb-hE7jYlcp4exwXRsQ"
YOUTUBE_CHANNEL_ID_9 = "PLPiMp0i5_dlsZD4Nj_qNtd_OB8YJPLMO_"


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
        title="Celtic v DeedCo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://always-back-winners.com/wp-content/uploads/2015/02/Celtic-V-Rangers-Always-Back-Winners.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="King Of Kings",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://i.dailymail.co.uk/i/pix/2014/11/10/1415653004157_wps_44_SOCCER_Celtic_Celeb_2_Cel.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Euro Goals",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://i.telegraph.co.uk/multimedia/archive/03183/celtic2_3183868b.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Fans",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://ultras-celtic.com/main/site/templates//img/bcg_slide-1.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Classic Goals",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Mcgrory_celtic_1930.jpg/400px-Mcgrory_celtic_1930.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="European Cup Finals",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://www.fawndoo.com/cfcdesign/derek/images/euro-cup1967.jpg",
        folder=True )
			
    plugintools.add_item( 
        #action="", 
        title="2000/2001 Season",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://webspace.webring.com/people/og/goneil/celts2004.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Celtic TV Newsdesk",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://pbs.twimg.com/profile_images/709758963953344512/HCbvQHUi.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Celtic 50s, 60s, 70s, 80s, 90s, 00s",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://image.wikifoundry.com/image/1/fQlTQl6SrzQ0iwfdn2-YZg870959/GW1460H825",
        folder=True )
		
run() 
