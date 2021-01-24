from camera import Camera

device_num = 0
camera = Camera(device_num)

# print(camera.fps)
# camera.fps = 24
# print(camera.fps)

print(camera.width)
camera.width = 320
print(camera.width)

# camera = cv2.VideoCapture(0)
# print(camera.isOpened())


# print(f"width: {width}")

# camera.release()
# print(camera.isOpened())