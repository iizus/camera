# from opencv import OpenCV
import opencv


class Capture(opencv.OpenCV):
    def __init__(self, video_source):
        super().__init__(video_source)
        self.image_type = 'jpeg'
        self.compression = 0
        self.quality = 100
        self.image_dir = 'images'


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


    def save(self, frame):
        file_path = opencv.get_file_path_from(
            dir = self.image_dir,
            image_type = self.image_type,
        )
        if self.image_type == 'png':
            return opencv.save_as_png(frame, file_path, self.compression)
        elif self.image_type == 'tiff':
            return opencv.save_as_tiff(frame, file_path, self.compression)
        elif self.image_type == 'jpeg':
            return opencv.save_as_jpeg(frame, file_path, self.quality)
        else:
            return None


    def take_and_save(self):
        frame = self.get_frame()
        result = self.save(frame)
        return result