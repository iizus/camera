import cv2


def save(frame, file_path):
    return cv2.imwrite(file_path, frame)


def decode_fourcc(value):
    v = int(value)
    charactors = [chr((v >> 8 * i) & 0xFF) for i in range(4)]
    fourcc = ''.join(charactors)
    return fourcc


def get_fourcc_from(string):
    fourcc = cv2.VideoWriter_fourcc(*string)
    return fourcc


def loop(callback, times):
    for _ in range(times): callback()


class Capture:
    # TODO: set width and height together

    __properties = {
        'fps': cv2.CAP_PROP_FPS,
        'width': cv2.CAP_PROP_FRAME_WIDTH,
        'height': cv2.CAP_PROP_FRAME_HEIGHT,
    }


    def __init__(self, video_source):
        self.__capture = cv2.VideoCapture(video_source)
        self.__define_properties()
        self.__read_frames()


    def __del__(self):
        self.__capture.release()


    def display_settings(self):
        print('-----------------------')
        codec = self.__get_setting_of_fourcc()
        print(f"codec: {codec}")
        self.__display_settings_without_codec()
        print('-----------------------')


    def take_and_save_to(self, file_path):
        frame = self.get_frame()
        result = save(frame, file_path)
        return result


    def get_frame(self):
        _, frame = self.__capture.read()
        return frame


    def __read_frames(self):
        loop(callback=self.get_frame, times=2) 


    def __display_settings_without_codec(self):
        for key, prop in self.__properties.items(): self.__display_setting_of(key, prop)
    

    def __display_setting_of(self, key, prop):
        value = self.__get_setting_of(prop)
        print(f"{key}: {value}")

    
    def __define_properties(self):
        self.__define_property_of_fourcc('codec')
        for name, prop in self.__properties.items(): self.__define_property(name, prop)


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
        setting = self.__capture.get(prop)
        setting = int(setting)
        return setting

    
    def __set_setting_of(self, prop, value):
        self.__capture.set(prop, value)
        self.__read_frames()


    def __set_property_of(self, name, getter, setter):
        set_prop = property(getter, setter)
        setattr(self.__class__, name, set_prop)