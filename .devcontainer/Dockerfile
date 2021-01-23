FROM python


RUN apt update
RUN apt upgrade -y

RUN apt install -y libgl1-mesa-dev

RUN pip install -U pip
RUN pip install opencv-python

RUN python -c 'import cv2'


RUN apt install -y v4l-utils