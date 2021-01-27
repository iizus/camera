from capture import Capture

video_source = -1
camera = Capture(video_source)

camera.set_frame_config(
    codec = 'MJPG',
    width = 800,
    height = 600,
    fps = 30,
)
camera.set_image_config(
    dir = 'images',
    type = 'jpeg',
    compression = 0,
    quality = 100,
)

camera.display_frame_config()
# camera.display_image_config()

# camera.take_and_save()

temp = list()

from time import perf_counter
started_time = perf_counter()

while perf_counter() - started_time <= 1:
    temp.append(camera.get_frame())
else:
    print(len(temp))

del camera