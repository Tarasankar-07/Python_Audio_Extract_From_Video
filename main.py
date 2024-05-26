import os
from moviepy.editor import VideoFileClip

def separate_audio_video():
    video_path = input("Enter the path of the video file: ")
    
    video_dir = os.path.dirname(video_path)
    video_filename = os.path.basename(video_path)
    video_name, video_ext = os.path.splitext(video_filename)
    
    output_audio_path = os.path.join(video_dir, video_name + '_audio.mp3')
    output_video_path = os.path.join(video_dir, video_name + '_video_without_audio.mp4')
    
    video = VideoFileClip(video_path)
    
    audio = video.audio
    audio.write_audiofile(output_audio_path)

    video_without_audio = video.without_audio()
    video_without_audio.write_videofile(output_video_path)

separate_audio_video()
