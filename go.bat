set report=%1
cd /d "%~dp0"
python qt_report/main.py %report%
