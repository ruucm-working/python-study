import youtube_dl

ydl_opts = {
    # 'retries': 1000,
    'nocheckcertificate': True,
    'verbose': True,
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    # 'proxy': 'http://91.195.130.237:8080',
    # 'outtmpl': '%(id)s%(ext)s',
    # 'forceGenericExtractor': True,
    'proxy': 'http://50.201.51.216:8080',
}
ydl = youtube_dl.YoutubeDL(ydl_opts)
url = 'https://ddaltime11.com/bbs/board.php?bo_table=kor&wr_id=7968'

with ydl:
    result = ydl.extract_info(
        url,
        # download=False # We just want to extract the info
    )
  #  result = ydl.download(['{0}'.format(url)])

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
video_url = video['url']
print(video_url)