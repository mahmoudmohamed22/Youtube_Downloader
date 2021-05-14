from pytube import YouTube
#video link ,you will be download 

link="https://www.youtube.com/watch?v=G6avw6VuA6A"

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

