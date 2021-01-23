FROM python

# RUN uname -a
RUN apt update
RUN apt upgrade -y
RUN apt install -y libgl1-mesa-dev

# RUN apt install -y libavutil56 libcairo-gobject2 libgtk-3-0 libqtgui4 libpango-1.0-0 libqtcore4 libavcodec58 libcairo2 libswscale5 libtiff5 libqt4-test libatk1.0-0 libavformat58 libgdk-pixbuf2.0-0 libilmbase23 libjasper1 libopenexr23 libpangocairo-1.0-0 libwebp6

# RUN apt install -y python3-opencv
# RUN lsb_release -a
# RUN ls /usr/bin/

# RUN python3 -m pip install opencv-contrib-python
# RUN python3 -m pip install opencv-python
RUN pip install opencv-python
# RUN python -m cv2