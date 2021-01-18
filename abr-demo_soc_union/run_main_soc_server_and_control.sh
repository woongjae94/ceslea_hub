export DISPLAY=:0.0
xhost local:root
#sudo docker run --env DISPLAY=unix$DISPLAY --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /dev/shm:/dev/shm -v ~/Desktop/COPY_UPGRADE/abr-demo_soc_union:/home -it --rm --name Socket_container -p 3019:8282 woongjae94/abr-demo:socket python3 main_soc_server_and_control.py
sudo docker run --env DISPLAY=unix$DISPLAY --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /dev/shm:/dev/shm -v ~/Desktop/COPY_UPGRADE/abr-demo_soc_union:/home -it --rm --name Socket_container woongjae94/abr-demo:socket 

#sudo docker run --env DISPLAY=$DISPLAY --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v /dev/shm:/dev/shm -v ~/D_4000/project/ABR_DEMO/abr-demo_soc_union:/home -it --rm --name Socket_container -p 3019:8282 woongjae94/abr-demo:socket
