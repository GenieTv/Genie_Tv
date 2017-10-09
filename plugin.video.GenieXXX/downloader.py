import xbmcgui
import urllib
import time

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Genie XXX","Downloading Content",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0 and not percent == 100: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '[COLORred]%.02f[COLORsteelblue] MB of[COLORred] %.02f [COLORsteelblue]MB[/COLOR]' % (currently_downloaded, total) 
            e = '[COLORsteelblue]Speed:[COLORred] %.02f [COLORsteelblue]Kb/s[/COLOR] ' % kbps_speed 
            e += '[COLORsteelblue]ETA:[COLORred] %02d:%02d[/COLOR]' % divmod(eta, 60) 
            dp.update(percent, mbs, e)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            raise Exception("Canceled")
            dp.close()