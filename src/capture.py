from opencv import OpenCV


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