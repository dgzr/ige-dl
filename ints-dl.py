#!/data/data/com.termux/files/usr/bin/python
"""
Author : Aditia © 2020
Date : Wed, 25 Nov 2020, 22:10:24 WIB
update dari versi yang lama.
"""
import argparse,re,requests,json
from tqdm import tqdm

def GraphMedia(yurl, path):
    try:
        data = requests.get(yurl,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}).text
        win = re.search(r"window._sharedData\s=\s(.*?);",data)
        if(win):
            do = json.loads(win.group(1))["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]
            if("video_url" in do.keys()):
                url = do["video_url"]
                fm = re.search(r"\/(\d.*?\_\d.+\.mp4)", url).group(1)
                print(f' [video] {fm}')
                Download(path,fm,url)
            elif("edge_sidecar_to_children" in do.keys()):
                dat_ = do["edge_sidecar_to_children"]["edges"]
                for dat in dat_:
                    if(dat["node"]["__typename"] == "GraphImage"):
                        url = dat["node"]["display_resources"][-1]["src"]
                        fm = re.search(r"\/(\d.*?\_\d.+\.jpg)", url).group(1)
                        print(f' [image] {fm}')
                        Download(path,fm,url)
                    elif(dat["node"]["__typename"] == "GraphVideo"):
                        url = dat["node"]["video_url"]
                        fm = re.search(r"\/(\d.*?\_\d.+\.mp4)", url).group(1)
                        print(f' [video] {fm}')
                        Download(path,fm,url)
            else:
                url = do["display_resources"][-1]["src"]
                fm = re.search(r"\/(\d.*?\_\d.+\.jpg)", url).group(1)
                print(f' [image] {fm}')
                Download(path,fm,url)
#            var +=1
        else:
            exit(" Error : Can't find page data please check your url")
    except requests.exceptions.ConnectionError:
        exit(" Error : no internet connection")
    except json.decoder.JSONDecodeError:
        exit(" Error : Your url post is Private!!")

def Download(path ,fname, url):
    try:
        content = requests.get(url, stream=True)
        prog = tqdm(
            total=int(
                content.headers.get(
                    'content-length',
                    0)),
            unit='B',
            unit_scale=True)
        with open(path + fname, 'wb') as f:
            for progs in content.iter_content(1024):
                prog.update(len(progs))
                f.write(progs)
        prog.close()
    except Exception as e:
        raise e

def forFile(file,path):
    try:
        fi = open(file).read().splitlines()
        for get,get_ in enumerate(fi):
            print(f" [intsdl] Downloading {get+1} of {len(fi)} url")
            GraphMedia(get_,path)
    except FileNotFoundError:
        exit(f" Error : File {fi} not found!")

def Main():
    _arg = argparse.ArgumentParser(
    	formatter_class=argparse.RawTextHelpFormatter,
    	description="\t\t insta dl cli version\n\t\t   by aditia_dtz © 2020")
    _arg.add_argument('-f','--file',help='download media using list file url',metavar='')
    _arg.add_argument('-u','--url',help='single url post to download',metavar='')
    _arg.add_argument('-p','--path',help='path to save media',metavar='')
    _arg.add_argument('-i','--info',help='tools information',metavar='')
    pts = _arg.parse_args()
    if(pts.file):
        if(pts.path):
            forFile(pts.file,pts.path)
        else:
            _arg.print_usage()
    elif(pts.url):
        if(pts.path):
            GraphMedia(pts.url,pts.path)
        else:
            _arg.print_usage()
    elif(pts.info):
        print("\n Contact : https://t.me/aditia_dtz\n")
    else:
        _arg.print_usage()

if __name__=="__main__":
    Main()
