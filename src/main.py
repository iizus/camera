import cv2

class Camera:
    def __init__(self, device_num):
        self.camera = cv2.VideoCapture(device_num)
        print(self.decode_fourcc(self.camera.get(cv2.CAP_PROP_FOURCC)))

    def __del__(self):
        self.camera.release()

    def decode_fourcc(self, value):
        v = int(value)
        charactors = [chr((v >> 8 * i) & 0xFF) for i in range(4)]
        fourcc = ''.join(charactors)
        return fourcc

    @property
    def width(self):
        # print(self.width)
        return self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)

    @width.setter
    def width(self, width):
        print(self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 160))
        print(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(self.width)

    @property
    def fps(self):
        # print(self.width)
        return self.camera.get(cv2.CAP_PROP_FPS)

    @fps.setter
    def fps(self, fps):
        self.camera.set(cv2.CAP_PROP_FPS, fps)
        # print(self.camera.get(cv2.CAP_PROP_FPS))
        # print(self.width)

    # def get_camera_setting(self):
    #     self.height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #     self.fps = camera.get(cv2.CAP_PROP_FPS)



camera = Camera(0)
print(camera.fps)
camera.fps = 5
print(camera.fps)

# camera = cv2.VideoCapture(0)
# print(camera.isOpened())


# print(f"width: {width}")

# camera.release()
# print(camera.isOpened())