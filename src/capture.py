import cv2

class Capture:
    def __init__(self, video_source):
        self.capture = cv2.VideoCapture(video_source)
        self.__define_properties()
        # print(self.decode_fourcc(self.capture.get(cv2.CAP_PROP_FOURCC)))


    def __del__(self):
        self.capture.release()


    def __decode_fourcc(self, value):
        v = int(value)
        charactors = [chr((v >> 8 * i) & 0xFF) for i in range(4)]
        fourcc = ''.join(charactors)
        return fourcc

                
    def __define_properties(self):
        self.__define_property('fourcc', cv2.CAP_PROP_FOURCC)
        self.__define_property('fps', cv2.CAP_PROP_FPS)
        self.__define_property('width', cv2.CAP_PROP_FRAME_WIDTH)
        self.__define_property('height', cv2.CAP_PROP_FRAME_HEIGHT)


    def __define_property(self, name, prop):
        class_name = self.__class__.__name__
        field_name = f"_{class_name}__{name}"
        def getter(_): return self.capture.get(prop)
        def setter(_, value): self.capture.set(prop, value)
        set_prop = property(getter, setter)
        setattr(self.__class__, name, set_prop)