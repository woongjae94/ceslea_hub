curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=1518bcFzxXJ_qDrBvRENaKkcYolAu-ZZK" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=1518bcFzxXJ_qDrBvRENaKkcYolAu-ZZK" -o model.tar.gz

tar -xvzf model.tar.gz
rm -rf *.tar.gz
