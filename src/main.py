from capture import Capture

video_source = -1
camera = Capture(video_source)

# camera.take_and_save_with_timestamp()

camera.display_settings()
# camera.take_and_save_to('test1.png')

# camera.codec = 'MJPG'
# camera.fps = 30
# camera.set_frame_size(width=1920, height=1080)

camera.set_frame(
    codec = 'MJPG',
    width = 1920,
    height = 1080,
    fps = 30,
)
camera.display_settings()
# camera.take_and_save_to('test2.png')

# camera.codec = 'YUYV'
# camera.rgb = 0

camera.set_frame(
    codec = 'YUYV',
    width = 1920,
    height = 1080,
    fps = 30,
)
camera.display_settings()

del camera