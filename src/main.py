from capture import Capture

video_source = 0
camera = Capture(video_source)

print(camera.fps)
camera.fps = 24
print(camera.fps)

print(camera.width)
camera.width = 320
print(camera.width)