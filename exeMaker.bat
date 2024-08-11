title exeMaker
pyinstaller --onefile  --icon=wacom.ico "CTL-472 Cover Maker.py"
copy "dist\CTL-472 Cover Maker.exe" "CTL-472 Cover Maker.exe"
del /f /q "CTL-472 Cover Maker.spec"
rd /s /q __pycache__ && rd /s /q build && rd /s /q dist
pause