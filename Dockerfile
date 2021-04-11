FROM continuumio/miniconda3
WORKDIR /app
# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml
# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "YOLOv3", "/bin/bash", "-c"]
# Make sure the environment is activated:
RUN echo "Make sure tenserflow is installed:"
RUN python -c "import tensorflow"
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python numba Flask

RUN wget https://pjreddie.com/media/files/yolov3.weights
# The code to run when container is started:
COPY . .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "YOLOv3", "python3", "app.py"]
