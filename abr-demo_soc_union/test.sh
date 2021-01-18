export DISPLAY=:0.0
xhost local:root
sudo docker run --env DISPLAY=unix$DISPLAY --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v /dev/shm:/dev/shm -v ~/Desktop/abr-demo_soc_union:/home -it --rm --name Socket_test woongjae94/abr-demo:socket 
