from urllib import request
from pytube import YouTube



async def fetch():
    obj = YouTube("https://www.youtube.com/watch?v=cp09TjWJGa0")

    url=obj.thumbnail_url

    async with open('Img/thumb.png','wb')as ouput:
        await ouput.write(request.urlopen(f'{url}'))

    return "Img/thumb.png"
    
    
