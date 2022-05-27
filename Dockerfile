FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
#cv2 dependencies
RUN apt-get install ffmpeg libsm6 libxext6  -y \
    && apt-get install -y --no-install-recommends \
    build-essential \
    python3.9 \
    python3-pip \
    python3-venv \
    python3-dev \
    && rm -rf /var/cache/apt/archives \
    && rm -rf /var/lib/apt/lists
    #python3.8 python3-pip python3.8-venv python3.8-dev

RUN python3.9 -m pip install --upgrade pip \
    && python3.9 -m pip install build


COPY requirements_prod.txt requirements_prod.txt
RUN pip3 install -r requirements_prod.txt
COPY dist/yolo_demo-0.11.0-py3-none-any.whl .
RUN  python3.9 -m pip install yolo_demo-0.11.0-py3-none-any.whl

#RUN cd data && python3 -m build

WORKDIR /yolo_demo

COPY yolo_demo/web.py /yolo_demo

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["web.py"]



