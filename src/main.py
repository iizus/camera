from capture import Capture

video_source = 0
camera = Capture(video_source)

camera.display_settings()
# camera.take_and_save_to('test1.png')

camera.codec = 'MJPG'
camera.fps = 30
camera.set_frame_size(width=1920, height=1080)

camera.display_settings()
# camera.take_and_save_to('test2.png')

camera.codec = 'YUYV'
camera.display_settings()

del camera