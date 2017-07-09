import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
HOME           = xbmc.translatePath('special://home/')
GUSERDATA      = os.path.join(HOME, 'userdata/addon_data/plugin.video.GenieTV')
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'GENIE WIZ'
EXCLUDES       = [ADDON_ID, GUSERDATA, 'repository.GenieTv', 'plugin.video.GenieTv', 'script.module.simplejson', 'script.module.requests', 'script.module.liveresolver', 'script.module.beautifulsoup4', 'script.module.beautifulsoup', 'script.module.addon.common', 'script.common.plugin.cache', 'script.module.urlresolver']
# Text File with build info in it.
BUILDFILE      = 'http://genietvcunts.co.uk/newwiz/builds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')
#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://genietvcunts.co.uk/newwiz/apk/BUILDS.png'
ICONMAINT      = 'http://genietvcunts.co.uk/newwiz/apk/MAINTENANCE.png'
ICONAPK        = 'http://genietvcunts.co.uk/newwiz/apk/APK%20INSTALLER.png'
ICONADDONS     = 'http://genietvcunts.co.uk/newwiz/apk/ADDON%20INSTALLER.png'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'http://genietvcunts.co.uk/newwiz/apk/SAVE%20DATA.png'
ICONTRAKT      = 'http://genietvcunts.co.uk/newwiz/apk/TRAKT.png'
ICONREAL       = 'http://genietvcunts.co.uk/newwiz/apk/REALDIBIRD.png'
ICONLOGIN      = 'http://genietvcunts.co.uk/newwiz/apk/LOGIN.png'
ICONCONTACT    = 'http://genietvcunts.co.uk/newwiz/apk/CONTACT%20US.png'
ICONSETTINGS   = 'http://genietvcunts.co.uk/newwiz/apk/SETTINGS.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'white'
COLOR2         = 'gold'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR'+COLOR1+'][B][I]([COLOR'+COLOR2+']Genie Wiz[/COLOR])[/B][/COLOR] [COLOR'+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR'+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR'+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR'+COLOR1+']Current Build:[/COLOR] [COLOR'+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR'+COLOR1+']Current Theme:[/COLOR] [COLOR'+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = '[COLORwhite]Thank you for choosing  Genie Wiz.\r\n\r\nContact us on facebook at https://www.facebook.com/groups/GenieTv/[/COLOR]'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://genietvcunts.co.uk/newwiz/apk/CONTACT%20US.png'
CONTACTFANART  = 'http://genietvcunts.co.uk/newwiz/apk/NOTIFICATIONS.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://genietvcunts.co.uk/newwiz/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'text'
HEADERMESSAGE  = 'Genie Wiz'
# url to image if using Image 424x180
HEADERIMAGE    = ' '
# Background for Notification Window
BACKGROUND     = 'http://genietvcunts.co.uk/newwiz/nofiyf.jpg'
#########################################################