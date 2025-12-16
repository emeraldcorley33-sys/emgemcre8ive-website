@echo off
cd "c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\emgemcre8ive-website"
echo Pulling latest changes from GitHub...
git pull origin main
echo.
echo Staging all changes...
git add .
echo.
echo Committing changes...
git commit -m "Add all asset folders and fix image paths for GitHub Pages"
echo.
echo Pushing to GitHub...
git push origin main
echo.
echo ✓ All done! Your images should now load on the live site.
pause
