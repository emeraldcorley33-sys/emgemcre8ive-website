@echo off
cd /d "%~dp0"
git add .
git commit -m "Resolve merge conflicts - keep all corrected image paths"
git push origin main
echo.
echo Merge complete! Pushed to GitHub.
pause
