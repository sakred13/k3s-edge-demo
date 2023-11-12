FROM python:3.8

# Install dependencies
RUN pip install opencv-python-headless numpy

# Add your script that processes video and extracts metrics
COPY process_video.py /process_video.py

CMD ["python", "/process_video.py"]
