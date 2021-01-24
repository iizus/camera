from capture import Capture

video_source = 0
camera = Capture(video_source)

print(camera.fps)
camera.fps = 5
print(camera.fps)

print(camera.width)
print(camera.height)

camera.width = 800
camera.height = 600

print(camera.width)
print(camera.height)