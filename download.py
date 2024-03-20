import yt_dlp
import aiohttp
import asyncio


async def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                ydl = yt_dlp.YoutubeDL(ydl_opts)
                info_dict = await asyncio.to_thread(ydl.extract_info, url, download=False)
                video_url = info_dict['url']
                description = info_dict.get('description', '')
                channel_url = info_dict.get('uploader_url', '')
                channel_name = info_dict.get('uploader', '')
                views = info_dict.get('view_count', 0)
                likes = info_dict.get('like_count', 0)
                comments = info_dict.get('comment_count', 0)
                repost = info_dict.get('repost_count', 0)
                return video_url, likes, comments, repost, views, description, channel_url, channel_name
            else:
                return None
