# [Python](https://www.python.org/) Basics Exercices
Pratice and learining basics [python](https://www.python.org/)

[![alt text](logo_programme_language_python.png)](https://www.python.org/)

---------------------------------------------------------------
1) [**<ins>Download</ins>**](https://www.python.org/downloads/):

### The base command to <ins>install</ins> [python](https://www.python.org/):
_(just in Ubuntu Linux for me)_

- Check the version of [Python](https://www.python.org/) in the computer:
```
python --version
```

- Update and Refresh Repository Lists:
```
sudo apt update
```

- Install Supporting Software:
```
sudo apt install software-properties-common
```


### <ins>Option 1:</ins> Install Python 3 Using apt (Easier)
- Add Deadsnakes PPA:
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```
- Install Python 3:
```
sudo apt install python3.10
python --version
```


### <ins>Option 2:</ins> Install Python 3.7 From Source Code (Latest Version)
- Update Local Repositories:
```
sudo apt update
```
- Install Supporting Software:
```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```
- Download the Latest Version of Python Source Code:
```
cd /tmp
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
```
- Extract Compressed Files:
```
tar -xf Python-3.8.3.tgz
```
- Test System and Optimize Python:
```
cd python-3.10
./configure --enable-optimizations
```
- Install a Second Instance of Python (recommended):
```
sudo make altinstall
```
- Overwrite Default Python Installation:
(if you want)
```
sudo make install
```
- Verify Python Version:
```
python3 --version
```


---------------------------------------------------------------------------------------
2) **<ins>Tools and pip</ins>**:

### To see if <ins>**pip**</ins> is installed, open a command prompt and run:
```
command -v pip3
```

