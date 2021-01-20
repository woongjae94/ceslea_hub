import subprocess

#proc = subprocess.Popen('screen -S cam_test ifconfig', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
statusProc = subprocess.run('sudo sh ~/D_4000/project/ceslea_hub/cam_stream/cam_stream_run_without_TTY.sh', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#statusProc = subprocess.run('screen -X -S cam kill', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#statusString = statusProc.stdout.decode('ascii')
#print(statusString)
# parse screen's output (statusString) for your status list

#subprocess.call(["screen", "-S", "session", "-X", "stuff", "'ifconfig'`echo -ne '\015'`"])

#proc = subprocess.Popen('screen -r cam_test ifconfig', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
