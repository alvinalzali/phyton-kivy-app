# This app created to test phyton code on kivy launcher
## This Repo based on 
1. [DENICZ](https://www.youtube.com/watch?v=pzsvN3fuBA0).

### Lib Requirements :
1. kivy 2.1.0
2. kivy_deps.gstreamer 0.3.3 (optional)
3. python 3.9.12 (if higher stable then its better)

### This app can be deployed to apk with some requirement
``` 
On windows 11: (Installation tutorial can be searched at google)
1. Windows Subsystem Linux 
2. Ubuntu 20.04.4 LTS
3. Installed ADB for windows and add it into env path

```

### Lib on Ubuntu Command-line
1. Create kivy's python file on windows
2. After Ubuntu Installed, install required libraries :
```
1. sudo apt update / sudo apt-get update
2. sudo apt-get install openjdk-8-jdk
3. sudo apt-get install zip
4. sudo apt-get install unzip
5. sudo apt-get install python3
6. sudo apt-get install python3-pip
7. sudo apt-get install ipython3
8. sudo apt-get install cython
9. sudo apt-get install autoconf
10. sudo apt-get install build-essential libltdl-dev libffi-dev libssl-dev python-dev
11. sudo pip3 install --upgrade cython
12. sudo pip3 install kivy_garden.graph
13. sudo pip3 install kivy_garden.mapview
```
3. Create apk using buildozer with plugged android device
```
### Install Buildozer on ubuntu
git clone https://github.com/kivy/buildozer.git
1. cd buildozer
2. sudo python3 setup.py install
```
