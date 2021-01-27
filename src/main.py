from capture import Capture

video_source = -1
camera = Capture(video_source)

camera.set_frame_config(
    codec = 'YUYV',
    width = 1920,
    height = 1080,
    fps = 30,
)
camera.set_image_config(
    dir = 'images',
    type = 'tiff',
    compression = 0,
    quality = 100,
)

camera.display_frame_config()
camera.display_image_config()

camera.take_and_save()

del camera