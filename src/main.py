from capture import Capture

video_source = -1
camera = Capture(video_source)
camera.set_frame(
    codec = 'MJPG',
    width = 1920,
    height = 1080,
    fps = 30,
)
camera.display_settings()
camera.take_and_save_with_timestamp()

del camera