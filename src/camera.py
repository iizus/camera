import cv2

class Camera:
    def __init__(self, device_num):
        self.camera = cv2.VideoCapture(device_num)
        print(self.decode_fourcc(self.camera.get(cv2.CAP_PROP_FOURCC)))
        
        self.define_property('fps', cv2.CAP_PROP_FPS)
        self.define_property('width', cv2.CAP_PROP_FRAME_WIDTH)

    def __del__(self):
        self.camera.release()

    def decode_fourcc(self, value):
        v = int(value)
        charactors = [chr((v >> 8 * i) & 0xFF) for i in range(4)]
        fourcc = ''.join(charactors)
        return fourcc

    

    # @property
    # def width(self): return self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    # @width.setter
    # def width(self, width): self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    # @property
    # def fps(self): return self.camera.get(cv2.CAP_PROP_FPS)
    # @fps.setter
    # def fps(self, fps): self.camera.set(cv2.CAP_PROP_FPS, fps)

    # def define_property(self, prop):
    #     def getter(self): return self.camera.get(prop)
    #     def setter(self, value): self.camera.set(prop, value)
    #     fps = property(getter, setter)

    def define_property(self, name, prop):
        class_name = self.__class__.__name__
        field_name = f"_{class_name}__{name}"
        # setattr(self, field_name, value)
        def getter(_): return self.camera.get(prop)
        def setter(_, value): self.camera.set(prop, value)
        set_prop = property(getter, setter)
        setattr(self.__class__, name, set_prop)

    # def get_camera_setting(self):
    #     self.height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #     self.fps = camera.get(cv2.CAP_PROP_FPS)