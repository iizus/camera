from capture import Capture

video_source = 0
camera = Capture(video_source)

camera.display_setting()
camera.take_and_save_to('test1.png')

camera.codec = 'MJPG'
camera.fps = 30
camera.width = 1920
camera.height = 1080

camera.display_setting()
camera.take_and_save_to('test2.png')

# print(vars(camera))