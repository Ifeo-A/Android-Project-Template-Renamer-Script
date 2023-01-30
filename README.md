# Android project file customizer

A python script to customize the android project files. It replaces the default package and application name with what you provide. 
The Android project template can be found [here](https://github.com/Ifeo-A/AndroidProjectTemplate).


## Usage/Examples

These do not need to run in a virtual environment.

If you're on an Intel Mac then run
```
macIntelDist/main/main -p com.your.project [-a YourAppName]
```
or
```
macIntelDist/main/main -packageName com.your.project [-appName YourAppName]
```

If you're on an M1 Mac then run
```
macM1Dist/main/main -p com.your.project [-a YourAppName]
```
or
```
macM1Dist/main/main -packageName com.your.project [-appName YourAppName]
```

If you're on Windows then run
```
windowsDist/main/main -p com.your.project [-a YourAppName]
```
or
```
windowsDist/main/main -packageName com.your.project [-appName YourAppName]
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
pyinstaller command to compile for Mac M1  (Need to run this on a Mac computer)
```angular2html
pyinstaller main.py --target-arch arm64 --distpath ./macM1Dist -y
```

pyinstaller command to compile for Mac Intel (Need to run this on a Mac computer)
```
pyinstaller main.py --target-arch x86_64 --distpath ./macIntelDist -y
```

pyinstaller command to compile for windows (Need to run this on a Windows computer)
```
pyinstaller main.py --distpath ./windowsDist -y
```







