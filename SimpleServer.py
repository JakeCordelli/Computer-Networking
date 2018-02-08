#-------------------------------------------------------------------------------
# Name:        Hello World Server
# Purpose:
#
# Author:      vigils
#
# Created:     07/03/2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import WebServer

def main():
    myWebServer = WebServer.WebServer(8080)
    myWebServer.start()
    myWebServer = WebServer.WebServer(8081)
    myWebServer.start()

    pass

if __name__ == '__main__':
    main()