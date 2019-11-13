
# author lamyoung

CONST_START_TIME=1;
CONST_END_TIME=3;
CONST_FILE_NAME="jump.mp4";
CONST_FILE_OUTPUT_vedio="jump_cmp_vedio.mp4";
CONST_FILE_OUTPUT_ffmpeg="jump_cmp_ffmpeg.gif";
CONST_FILE_OUTPUT_imageio="jump_cmp_imageio.gif";
CONST_FILE_LOGO="logo.png";
CONST_FPS_PERCENT=0.5;
CONST_COLORS=128;

from moviepy.editor import *

vedioClip = VideoFileClip(CONST_FILE_NAME,audio=False)

duration=CONST_END_TIME-CONST_START_TIME;
 
def logo_pos(t):
	if(t<duration/2):
		return ('center', t*2/duration);
	else:
		return ('center', -t*2/duration+2);

imageClip=ImageClip(CONST_FILE_LOGO).set_duration(duration).set_opacity(0.4).set_position(logo_pos,relative=True);
final_clip=CompositeVideoClip([vedioClip.subclip(t_start=CONST_START_TIME, t_end=CONST_END_TIME),imageClip]).to_RGB();

final_clip.write_gif(CONST_FILE_OUTPUT_ffmpeg,program='ffmpeg',fps=vedioClip.fps*CONST_FPS_PERCENT);
final_clip.write_gif(CONST_FILE_OUTPUT_imageio,colors=CONST_COLORS,fps=vedioClip.fps*CONST_FPS_PERCENT);
final_clip.write_videofile(CONST_FILE_OUTPUT_vedio);
