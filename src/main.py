from capture import Capture

video_source = 0
camera = Capture(video_source)

print(camera.fourcc)
print(camera.fps)
print(camera.width)
print(camera.height)
camera.take_and_save_to('test1.png')

camera.fourcc = 'MJPG'
camera.fps = 5
camera.width = 800
camera.height = 600

print(camera.fourcc)
print(camera.fps)
print(camera.width)
print(camera.height)
camera.take_and_save_to('test2.png')