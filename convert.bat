REM Define the path to the FontForge executable
SET FF_PATH="C:\Program Files\FontForge\bin\fontforge.exe"

REM Run the script with input and output file paths as arguments
%FF_PATH% -script convert.py Rotator.svg Rotator

pause