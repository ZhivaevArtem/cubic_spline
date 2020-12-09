@echo off

python.exe -m pip install -r requirements.txt -qqq

cd src

python.exe -m interpolation

cd ..
