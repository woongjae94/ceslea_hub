# sudo docker run --gpus '"device=1"' --network="host" -v ~/Desktop/abr-demo_Action:/home/ -it --rm --name Action_container woongjae94/abr-demo:Action python main_action_recognition.py
sudo docker run --runtime=nvidia --network="host" -v ~/Desktop/abr-demo_Action:/home/ -it --rm --name Action_container woongjae94/abr-demo:Action python main_action_recognition_frontPerson.py
