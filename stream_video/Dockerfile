FROM alpine:latest

# Install FFmpeg
RUN apk add --no-cache ffmpeg

# Copy the videos into the container
COPY video1.mp4 /video1.mp4
COPY video2.mp4 /video2.mp4

# Entrypoint script to alternate between videos
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
