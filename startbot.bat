@echo off

setlocal
pushd "%~dp0"

If not exist logs mkdir logs
python src\main.py

popd
endlocal
