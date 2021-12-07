from pytube import YouTube
import sys
import os

url = "not defined"
avStreams, aStreams, vStreams = [], [], []
obj = ''

failed = '\033[91m'
complete = '\033[92m'
bold = '\033[1m'
options = '\033[94m'
cin = '\033[93m'
cout = '\033[95m'
default = '\033[0m'


def checkInternet():
    res = True if os.system('ping www.google.com -w 4 > tmp') == 0 else False
    os.remove('tmp')
    return res


def download():

    if(checkInternet()):
        try:

            itag = int(input(f"{bold}{cin}Enter the itag: {bold}{cin}"))
            target = obj.streams.get_by_itag(itag)
        except:
            print(f"{bold}{failed}Invalid itag{bold}{failed}")
            return
        try:
            path = input(
                f"{bold}{cin}Enter save path leave empty for default: {bold}{cin}")
            path = "CMD Version/"if path == ''else path
            target.download(path)
        except:
            print(f"{bold}{failed}Error while downloading{bold}{failed}")
    else:
        print(f"\n{bold}{failed}Not connected to Internet!{bold}{failed}")


def getDetails():
    if(checkInternet()):
        try:
            print(f"\n\t{cout}Title:{cout}{default} {obj.title}{default}")
            print(f"\t{cout}Views:{cout}{default} {obj.views}{default}")
            print(f"\t{cout}Playtime:{cout}{default} {obj.length} sec{default}")
            print(f"\t{cout}Rating:{cout}{default} {obj.rating} {default}")
            print(
                f"\t{cout}Published Date:{cout}{default}{obj.publish_date} {default}")
        except:
            print(f"{bold}{failed}Url is not defined{bold}{failed}")

    else:
        print(f"\n{bold}{failed}Not connected to Internet!{bold}{failed}")


def fetch():

    global avStreams
    global aStreams
    global vStreams
    global obj

    if(checkInternet()):
        if url == "not defined":
            print(f"\n{bold}{failed}Url is not defined{bold}{failed}")
            return
        try:
            print(f"\n{cout}URL: {cout}{default}{url}{default}")
            obj = YouTube(f"{url}")

            avStreams = [_ for _ in obj.streams.filter(progressive=True)]
            aStreams = [_ for _ in obj.streams.filter(only_audio=True)]
            vStreams = [_ for _ in obj.streams.filter(only_video=True)]

            print(f"{bold}{complete}Complete{bold}{complete}")

        except:
            print(f"\n{bold}{failed}Invalid url try again{bold}{failed}")
    else:
        print(f"\n{bold}{failed}Not connected to Internet!{bold}{failed}")


def enterUrl():
    global url
    url = input(f"\n{bold}{cin}Enter url: {cin}{bold}")


def select():

    while True:
        if(checkInternet()):

            print(
                f"\n\t{bold}{default}1.{default} {options}Audio + Video{options}{bold}")
            print(
                f"\t{bold}{default}2.{default} {options}Audio Only{options}{bold}")
            print(
                f"\t{bold}{default}3.{default} {options}Video Only{options}{bold}")
            print(f"\t{bold}{default}4.{default} {options}Extension{options}{bold}")
            print(f"\t{bold}{default}5.{default} {options}All{options}{bold}")
            print(f"\t{bold}{default}6.{default} {options}Download{options}{bold}")
            print(f"\t{bold}{default}7.{default} {options}Exit{options}{bold}")

            ch = int(input(f"\n\t{bold}{cin}Make Your Choice: {cin}{bold}"))
            if ch == 1:
                print(f"\n\t{options}{bold}Audio + Video{bold}{options}")
                [print(f"{default}\t"+str(x))for x in avStreams]

            elif ch == 2:
                print(f"\n\t{options}{bold}Audio Only{options}{bold}")
                [print(f"{default}\t"+str(x))for x in aStreams]

            elif ch == 3:
                print(f"\n\t{options}{bold}Video Only{options}{bold}")
                [print(f"{default}\t"+str(x))for x in vStreams]

            elif ch == 4:
                pass

            elif ch == 5:
                print(f"\n\t{options}{bold}Audio + Video{options}{bold}")
                [print(f"{default}\t"+str(x))for x in avStreams]
                print(f"\n\t{options}{bold}Audio Only{options}{bold}")
                [print(f"{default}\t"+str(x))for x in aStreams]
                print(f"\n\t{options}{bold}Video Only{options}{bold}")
                [print(f"{default}\t"+str(x))for x in vStreams]
            elif ch == 6:
                download()
            elif ch == 7:
                break
            else:
                print(f"{bold}{failed}Wrong choice try again{failed}{bold}")
        else:
            print(f"\n{bold}{failed}Not connected to Internet!{failed}{bold}")


def main():

    while True:
        print(f"{bold}{default}\n1.{default}{options} Enter URL{options}{bold}")
        print(f"{bold}{default}2.{default}{options} Fetch{options}{bold}")
        print(f"{bold}{default}3.{default}{options} Select{options}{bold}")
        print(f"{bold}{default}4.{default}{options} Download{options}{bold}")
        print(f"{bold}{default}5.{default}{options} Details{options}{bold}")
        print(f"{bold}{default}6.{default}{options} Quit{options}{bold}")
        ch = int(input(f"{bold}{cin}\nMake Your Choice: {bold}{cin}"))
        if ch == 1:
            enterUrl()

        elif ch == 2:
            fetch()

        elif ch == 3:
            select()

        elif ch == 4:
            download()
        elif ch == 5:
            getDetails()
        elif ch == 6:
            quit()
        else:
            print(f"{bold}{failed}Wrong choice try again{bold}{failed}")


if __name__ == "__main__":

    main()
