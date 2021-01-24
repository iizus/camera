import opencv
from opencv import OpenCV


class Capture(OpenCV):
    def __init__(self, video_source):
        super().__init__(video_source)


    def __del__(self):
        super().__del__()


    def display_settings(self):
        print('-----------------------')
        codec = self.get_setting_of_fourcc()
        print(f"codec: {codec}")
        self.display_settings_without_codec()
        print('-----------------------')


    def take_and_save_to(self, file_path):
        frame = self.get_frame()
        result = opencv.save(frame, file_path)
        return result


    def get_frame(self):
        _, frame = self.capture.read()
        return frame