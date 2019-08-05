유투브 동영상을 다운로드 받는 방법을 배운다.
1. 관련 프로그램 설치
    관련자료 참조 : https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme
    
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

mkdir -p ~/bin

음악 다운로드 프로그램 만들기
cat << EOF > ~/bin/dl_mp3.sh
#!/bin/bash
#AnHive 2019
mkdir -p ~/mp3
cd ~/mp3
youtube-dl --extract-audio --audio-format mp3  -o "%(title)s.%(ext)s" \$1

EOF
chmod 775 ~/bin/dl_mp3.sh

음악 다운로드하기
dl_mp3.sh https://www.youtube.com/watch?v=qwAfDM9x-oA

음악 틀기
omxplayer -o local "New Songs of the Week - November 3, 2018.mp3"

음악 일과 재상하기
cat << EOF > ~/bin/play_mp3.sh
#!/bin/bash
#AnHive 2019
export DISPLAY=:0.0  
cd ~/mp3
ls *.mp3 : while read line
do
    omxplayer -o local "$line"
done 
EOF
chmod 755 ~/bin/play_mp3.sh



동영상 다운로드 프로그래 만들기
cat << EOF > ~/bin/dl_mp4.sh
#!/bin/bash
#AnHive 2019

mkdir -p ~/mp4
cd ~/mp4
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' \$1
EOF

chmod 775 ~/bin/dl_mp4.sh

음악다운로드 하기
dl_mp4.sh https://www.youtube.com/watch?v=qwAfDM9x-oA
동영상 플레이
omxplayer -o local "New Songs of the Week - November 3, 2018-qwAfDM9x-oA.mp4"

동영상 일괄 재생 프로그램 만들기
cat << EOF > ~/bin/play_mp4.sh
#!/bin/bash
#AnHive 2019
export DISPLAY=:0.0  
cd ~/mp4
ls *.mp4 : while read line
do
    omxplayer -o local "$line"
done 
EOF
chmod 755 ~/bin/play_mp4.sh

동영상 일괄재생
play_mp4.sh

