#Malware with python

# Steps to Run
'''plain text
1. create new directory called randomware
2. create multiple files in that directory
3. git clone this repo and python3 not_ransomware.py in that directory 
4. to decrypt run python3 decrypt.py in the same directory
```

# See the Usage Section in each .py file to see what the code does

# 1. Create virtual python env
```bash
python -m venv venv && source venv/bin/activate #Linux
python -m venv venv && \venv\Scripts\activate #Windows
```

### Creates virtual python environment 
```bash
python -m venv venv 
```

### Steps into virtual environment 
```bash
source .venv/bin/activate
```

### See the terminal now has the name of your virtual environment
```bash
(venv) drew@Andrews-MacBook-Pro% 
```

### To Step out of the virtual environment 
```bash
deactivate
```

# 2. Install dependencies (Inside of Virtual environment)
```bash
pip install -r requirements.txt
```

# 3 Run the Code
```bash
python main.py
```

# TROUBLESHOOTING
```bash
pip list
python --version 
pip --version 
```
```plain text
If trying to do this with VS CODE ensure you have your files open on the left side aka the workspace 

Command+shift+p select interpreter and chose .venv/bin python
```
