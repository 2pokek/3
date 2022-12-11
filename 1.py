import moviepy.editor

video = moviepy.editor.VideoFileClip('path_mp4')
audio = video.audio
audio.write_audiofile('My_audiopath.mp3')
