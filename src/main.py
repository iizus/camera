from capture import Capture

video_source = -1
camera = Capture(video_source)

camera.set_frame_config(
    codec = 'MJPG',
    width = 1920,
    height = 1080,
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

frames = list()
interval_time_sec = 1

from time import perf_counter
started_time = perf_counter()

def is_elapsed(started_time, interval_time_sec):
    elapsed_time = perf_counter() - started_time
    is_elapsed = elapsed_time < interval_time_sec
    return is_elapsed

while is_elapsed(started_time, interval_time_sec):
    frame = camera.get_frame()
    frames.append(frame)
else:
    print(len(frames))

del camera