from pytube import YouTube


colors = ['\033[91m', '\033[93m', '\033[94m', '\033[95m']
path="/home/abhilash/Programming/YouTube-Video-Downloader-Python/.tmp"


def printStreams(av, a, v, mp4):

    print(f'{colors[0]}Audio and Video')
    [print(i) for i in av]

    print(f'{colors[1]}Audio Only')
    [print(i) for i in a]

    print(f'{colors[2]}Video Only')
    [print(i) for i in v]

    print(f'{colors[3]}mp4 Format')
    [print(i) for i in mp4]


def main():
    resolutions = ['144p', '240', '360p', '480p', '720p']
    aStreams = []
    vStreams = []
    avStreams = []
	


    obj = YouTube("https://www.youtube.com/watch?v=cp09TjWJGa0")

    #* (method) filter: (
    #* fps=None, res=None, resolution=None, 
    #* mime_type=None, type=None, subtype=None, 
    #* file_extension=None, abr=None, bitrate=None, 
    #* video_codec=None, audio_codec=None, 
    #* only_audio=None, only_video=None, 
    #* progressive=None, adaptive=None, is_dash=None, 
    #* custom_filter_functions=None) -> Any


    avStreams = obj.streams.filter(progressive=True)
    aStreams = obj.streams.filter(only_audio=True)
    vStreams = obj.streams.filter(only_video=True)
    mp4Streams = obj.streams.filter(file_extension='mp4')
	

    # printStreams(avStreams, aStreams, vStreams, mp4Streams)

    #* Download
    #* (method) download: (
    #* output_path: str, 
    #* filename: str, 
    #* filename_prefix: str,
    #* skip_existing: bool, 
    #* timeout: int, 
    #* max_retries: int) -> str
    #! filter return iterable, get_by_itag return single stream.

    # target=obj.streams.get_by_itag('139')
    # target.download(path)

    print(obj.title)
	


if __name__ == '__main__':
    main()
