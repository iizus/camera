import cv2


def loop(callback, times):
    for _ in range(times): callback()


def save(frame, file_path):
    return cv2.imwrite(file_path, frame)


def decode_fourcc(value):
    v = int(value)
    charactors = [chr((v >> 8 * i) & 0xFF) for i in range(4)]
    fourcc = ''.join(charactors)
    return fourcc


def get_fourcc_from(string):
    fourcc = cv2.VideoWriter_fourcc(string[0], string[1], string[2], string[3])
    return fourcc


class Capture:
    properties = {
        'fps': cv2.CAP_PROP_FPS,
        'width': cv2.CAP_PROP_FRAME_WIDTH,
        'height': cv2.CAP_PROP_FRAME_HEIGHT,
    }

    def __init__(self, video_source):
        self.__init_capture(video_source)
        self.__define_properties()


    def __del__(self):
        self.__capture.release()


    def display_settings(self):
        print('-----------------------')
        codec = self.__get_setting_of_fourcc()
        print(f"codec: {codec}")
        for key, prop in self.properties.items():
            value = self.__get_setting_of(prop)
            print(f"{key}: {value}")
        print('-----------------------')


    def take_and_save_to(self, file_path):
        frame = self.get_frame()
        return save(frame, file_path)


    def get_frame(self):
        _, frame = self.__capture.read()
        return frame


    def __init_capture(self, video_source):
        self.__capture = cv2.VideoCapture(video_source)
        self.__read_frames()


    def __read_frames(self):
        loop(callback=self.get_frame, times=2)

    
    def __define_properties(self):
        self.__define_property_of_fourcc('codec')
        for name, prop in self.properties.items(): self.__define_property(name, prop)


    def __define_property(self, name, prop):
        def getter(_): return self.__get_setting_of(prop)
        def setter(_, value): self.__set_setting_of(prop, value)
        self.__set_property_of(name, getter, setter)


    def __define_property_of_fourcc(self, name):
        def getter(_): return self.__get_setting_of_fourcc()
        def setter(_, string): self.__set_setting_of_fourcc(string)
        self.__set_property_of(name, getter, setter)


    def __get_setting_of_fourcc(self):
        encoded_fourcc = self.__get_setting_of(cv2.CAP_PROP_FOURCC)
        decoded_fourcc = decode_fourcc(encoded_fourcc)
        return decoded_fourcc


    def __set_setting_of_fourcc(self, value):
        fourcc = get_fourcc_from(value)
        self.__set_setting_of(cv2.CAP_PROP_FOURCC, fourcc)


    def __get_setting_of(self, prop):
        return self.__capture.get(prop)

    
    def __set_setting_of(self, prop, value):
        self.__capture.set(prop, value)
        self.__read_frames()


    def __set_property_of(self, name, getter, setter):
        set_prop = property(getter, setter)
        setattr(self.__class__, name, set_prop)