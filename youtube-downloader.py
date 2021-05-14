from pytube import YouTube
#video link ,you will be download 

link="https://www.youtube.com/watch?v=Rv3kVxOhm_Q"

#object  video for link youtube
video=YouTube(link)

#description video
print(f"The video  title is \n {video.title}")
print("\n--------------------------------------")
print(f"The video description is \n {video.description}")
print("\n--------------------------------------")
print(f"The video Rate is \n {video.rating}")
print("\n--------------------------------------")
print(f"The video Views is \n {video.views}")
print("\n--------------------------------------")
print(f"The video length is \n {video.length/60} minutes ")
print("\n--------------------------------------")

#print(video.streams)
#streams is information video in youtube link
#for stream in video.streams:
#   print(stream)

print("\n--------------------------------------")
#for stream in video.streams.filter(progressive=True,res="720p"):
#    print(stream)

def finish():
    print("Download done")

video.streams.get_highest_resolution().download(output_path="/home/ubuntu/Downloads")
video.register_on_complete_callback(finish())