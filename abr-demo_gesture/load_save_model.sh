curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=1sEE9s2dbmAn44D5fmHz6-EWYjTrUIwhS" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=1sEE9s2dbmAn44D5fmHz6-EWYjTrUIwhS" -o save_model.tar.gz

curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=1sl7H2zOy4i30qmtCXlaxO4jBOytIw0mj" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=1sl7H2zOy4i30qmtCXlaxO4jBOytIw0mj" -o darknet.tar.gz
tar -xvzf save_model.tar.gz
tar -xvzf darknet.tar.gz
rm -rf *.tar.gz

