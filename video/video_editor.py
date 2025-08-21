import moviepy.editor as mpy
from faster_whisper import WhisperModel

def Modify_Video_Speed(video_path, speed_factor):
    video = mpy.VideoFileClip(video_path)
    modified_video = video.fx(mpy.vfx.speedx, factor=speed_factor)
    return modified_video


def Modify_Video_Resolution(video_path, resolution):
    video = mpy.VideoFileClip(video_path)
    modified_video = video.resize(resolution)
    return modified_video

def Crop_Video(video_path, start_time, end_time):
    video = mpy.VideoFileClip(video_path)
    cropped_video = video.subclip(start_time, end_time)
    return cropped_video

def Add_Text_Overlay(video_path, text, position, fontsize, color , font , relative):
    video = mpy.VideoFileClip(video_path)
    txt_clip = (mpy.TextClip(text, fontsize=fontsize, color=color, font=font)
                .set_position(position , relative=relative)
                .set_duration(video.duration))
    video = mpy.CompositeVideoClip([video, txt_clip])
    return video

def RemoveSound(video_path):
    video = mpy.VideoFileClip(video_path)
    video = video.without_audio()
    return video

def Combine_Videos(video_path1 , video_path2):
    video1 = mpy.VideoFileClip(video_path1)
    video2 = mpy.VideoFileClip(video_path2)
    combined = mpy.concatenate_videoclips([video1, video2])
    return combined

def Split_Video(video_path, split_time):
    video = mpy.VideoFileClip(video_path)
    first_part = video.subclip(0, split_time)
    second_part = video.subclip(split_time)
    return first_part, second_part

def Change_to_mp3(video_path):
    video = mpy.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(video_path.replace(".mp4", ".mp3"))
    return audio

def Add_Audio(videopath , musicpath):
    video = mpy.VideoFileClip(videopath)
    audio = mpy.AudioFileClip(musicpath)
    video = video.set_audio(audio)
    return video
def Adjust_Video_Volume(video_path, volume_scale):
    video = mpy.VideoFileClip(video_path).with_volume(volume_scale)
    return video

def Transcribe_Video(video_path):
    model = WhisperModel("small")
    video = mpy.VideoFileClip(video_path)
    audio = video.audio
    segments , info  = model.transcribe(audio)
    language = info[0]
    return segments, language


# def Add_Subtitles(video_path):
#     video = mpy.VideoFileClip(video_path)
#     subtitles, language = Transcribe_Video(video_path)
#     pass

def Add_Watermark(video_path, watermark_path, position , resizedheight = 50):
    video = mpy.VideoFileClip(video_path)
    watermark = mpy.ImageClip(watermark_path).set_duration(video.duration)
    watermark = watermark.set_position(position).resize(height=resizedheight) 
    video = mpy.CompositeVideoClip([video, watermark])
    return video
