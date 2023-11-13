#!/bin/sh

# Define the destination IP and port for the metrics processing service
DEST_IP="3.15.154.36"
DEST_PORT="6666"

while true; do
    # Stream the first video for 15 seconds
    ffmpeg -re -i /video1.mp4 -t 46 -f mpegts udp://${DEST_IP}:${DEST_PORT}

    # Stream the second video for 15 seconds
    ffmpeg -re -i /video2.mp4 -t 46 -f mpegts udp://${DEST_IP}:${DEST_PORT}
done
