from datetime import datetime
from opencv import OpenCV, save


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


class Capture(OpenCV):
    def __init__(self, video_source):
        super().__init__(video_source)


    def __del__(self):
        super().__del__()


    def set_frame(self, codec, width, height, fps):
        self.codec = codec
        self.width = width
        self.height = height
        self.fps = fps


    def set_frame_size(self, width, height):
        self.width = width
        self.height = height


    def display_settings(self):
        print('-----------------------')
        codec = self.get_setting_of_fourcc()
        print(f"codec: {codec}")
        self.display_settings_without_codec()
        print('-----------------------')


    # def take_and_save_with_timestamp(self, dir='.', image_type='png'):
    #     file_path = get_file_path_from(dir, image_type)
    #     result = self.take_and_save_to(file_path)
    #     return result


    def take_and_save(self, file_path=get_file_path_from(), parames=None):
        frame = self.get_frame()
        result = save(frame, file_path, parames)
        return result