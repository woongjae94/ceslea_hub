
export DISPLAY=:0.0
xhost local:root
#sudo docker run --runtime=nvidia --network="host" -v ~/Desktop/COPY_UPGRADE/abr-demo_gesture:/home/app -it --rm --name Gesture_container woongjae94/abr-demo:gesture python main_gesture_and_control.py

sudo docker run --runtime=nvidia --network="host"  --env="DISPLAY=$DISPLAY" --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v /dev/shm:/dev/shm -v ~/Desktop/COPY_UPGRADE/abr-demo_gesture:/home/app -it --rm --name Gesture_container woongjae94/abr-demo:gesture python main_gesture_and_control.py
