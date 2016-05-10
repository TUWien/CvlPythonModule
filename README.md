# CVL Dummy Python Module 🍸
This repository contains a simple python module.

## Building

### Requirements
- Python 3.4.4 or newer (see https://www.python.org/downloads/)

### Build Steps
- Open this directory (containing the ``setup.py``) in a command line
- Type
```
python setup.py install
```

### Testing
- For the ``cmd`` example dir to this folder (containing the ``setup.py``)
```
python lib/mymodule/script.py C:\valid-path 5
```
- Now you can call functions like this:
```
python
import mymodule
mymodule.helper.hfunction()
mymodule.filefunction("C:/valid-path", 5)
```

### Links
- CVL http://www.caa.tuwien.ac.at/cvl/
