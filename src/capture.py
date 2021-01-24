import cv2


def loop(callback, times):
    for _ in range(times): callback()


def save(frame, file_path):
    return cv2.imwrite(file_path, frame)


class Capture:
    def __init__(self, video_source):
        self.__init_capture(video_source)
        self.__define_properties()
        # print(self.decode_fourcc(self.capture.get(cv2.CAP_PROP_FOURCC)))


    def __del__(self):
        self.capture.release()


    def get_frame(self):
        _, frame = self.capture.read()
        return frame

    
    def take_and_save_to(self, file_path):
        frame = self.get_frame()
        return save(frame, file_path)


    def __init_capture(self, video_source):
        self.capture = cv2.VideoCapture(video_source)
        self.__read_frames()


    def __read_frames(self):
        loop(callback=self.get_frame, times=2)
        

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
        def getter(_):
            return self.capture.get(prop)
        def setter(_, value):
            self.capture.set(prop, value)
            self.__read_frames()
        set_prop = property(getter, setter)
        setattr(self.__class__, name, set_prop)