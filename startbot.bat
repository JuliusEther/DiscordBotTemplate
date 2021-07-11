@echo off

setlocal
pushd "%~dp0"

python src\main.py

popd
endlocal

pause