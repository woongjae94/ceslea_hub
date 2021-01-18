sudo docker run --device /dev/video0:/dev/video0 --entrypoint mjpg_streamer --rm --name cam_container -p 3009:8090 -it  woongjae94/abr-demo:cam-stream \
-i "/usr/lib64/input_uvc.so -y -d /dev/video0 -r 640x480 -f 20" \
-o "/usr/lib64/output_http.so -p 8090 -w /usr/share/mjpg-streamer/www/"
