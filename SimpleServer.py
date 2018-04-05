
import WebServer

def main():
    myWebServer = WebServer.WebServer(8080)
    myWebServer.start()
    myWebServer = WebServer.WebServer(8081)
    myWebServer.start()

    pass

if __name__ == '__main__':
    main()
