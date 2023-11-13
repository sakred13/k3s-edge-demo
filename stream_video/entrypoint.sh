#!/bin/sh

# Start the first video streaming script in the background
./send_to_dashboard.sh &

# Start the second video streaming script in the background
./send_to_processing_edge.sh &

# Wait for both scripts to finish before exiting
wait
