# Android project file customizer

A python script to customize the android project files. It replaces the default package and application name with what you provide. 
The Android project template can be found [here](https://github.com/Ifeo-A/AndroidProjectTemplate).


## Usage/Examples

Prerequisites:
- The script has been tested on python 3. You should have at least Python 3 installed

```python
python customizer.py -p com.your.project [-a YourAppName]
```
or
```
python customizer.py -packageName com.your.project [-appName YourAppName]
```

#
##Notes

First activate venv
```
source venv/bin/activate
```

Then do below


[pyinstaller options](https://pyinstaller.org/en/v5.7.0/usage.html?highlight=target_arch#cmdoption-target-architecture
)
----------
pyinstaller command to compile for Mac M1 
```angular2html
pyinstaller main.py --target-arch arm64 --distpath ./macM1Dist -y
```

pyinstaller command to compile for Mac Intel
```
pyinstaller main.py --target-arch x86_64 --distpath ./macIntelDist -y
```

pyinstaller command to compile for windows
```
pyinstaller main.py --distpath ./windowsDist -y

```






