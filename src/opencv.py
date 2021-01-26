import cv2
from datetime import datetime


def get_formated_time():
    time_format = '%Y-%m-%d-%X:%f'
    current_time = datetime.now()
    current_time = current_time.strftime(time_format)
    return current_time


def get_file_path_from(dir='.', image_type='png'):
    current_time = get_formated_time()
    file_name = f"{current_time}.{image_type}"
    file_path = f"{dir}/{file_name}"
    return file_path


def save(frame, file_path=get_file_path_from(), params=None):
    result = cv2.imwrite(file_path, frame, params)
    return result


def decode_fourcc(fourcc):
    fourcc = int(fourcc)
    fourcc = fourcc.to_bytes(4, 'little')
    fourcc = fourcc.decode('utf-8')
    return fourcc


def get_fourcc_from(string):
    fourcc = cv2.VideoWriter_fourcc(*string)
    return fourcc


def loop(callback, times):
    for _ in range(times): callback()


class OpenCV:
    __properties = {
        'fps': cv2.CAP_PROP_FPS,
        'width': cv2.CAP_PROP_FRAME_WIDTH,
        'height': cv2.CAP_PROP_FRAME_HEIGHT,
        'rgb': cv2.CAP_PROP_CONVERT_RGB,
    }


    def __init__(self, video_source):
        self.__capture = cv2.VideoCapture(video_source)
        self.__define_properties()
        self.__read_frames()


    def __del__(self):
        self.__capture.release()


    def get_frame(self):
        _, frame = self.__capture.read()
        return frame


    def take_and_save(self, file_path=get_file_path_from(), parames=None):
        frame = self.get_frame()
        result = save(frame, file_path, parames)
        return result


    def __read_frames(self):
        loop(callback=self.get_frame, times=2)


    def display_settings_without_codec(self):
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


    def get_setting_of_fourcc(self):
        encoded_fourcc = self.__get_setting_of(cv2.CAP_PROP_FOURCC)
        decoded_fourcc = decode_fourcc(encoded_fourcc)
        return decoded_fourcc


    def __set_setting_of_fourcc(self, value):
        fourcc = get_fourcc_from(value)
        self.__set_setting_of(cv2.CAP_PROP_FOURCC, fourcc)


    def __get_setting_of(self, prop):
        setting = self.__capture.get(prop)
        return setting

    
    def __set_setting_of(self, prop, value):
        self.__capture.set(prop, value)
        self.__read_frames()


    def __set_property_of(self, name, getter, setter):
        set_prop = property(getter, setter)
        setattr(self.__class__, name, set_prop)