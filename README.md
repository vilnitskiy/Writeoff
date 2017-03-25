# Writeoff #
## Description ##
App developed for KPI students to make their studying much easier and productive. It helps to save your precious time for more useful things that numerous repetitive tasks. The app gives students ability to share their works (for example home or control works).

You can see diagram in WriteOff/myapp_models.png

To create and run virtual environment:
```
virtualenv venv --no-site-packages
source venv/bin/activate
```
Load initial data:
```
make loaddata
```
To run locally, just execute:
```
cd Writeoff
pip install -r "requirements.txt"
make init
make run
```

## Authors ##
1. Vadym Hevlich
1. Vlad Ilnitskiy
1. Anatoliy Adamovskiy
1. Andriy Herasko

## UML-diagram ##
![UML] (https://github.com/vilnitskiy/Writeoff/blob/master/WriteOff/myapp_models.png)
