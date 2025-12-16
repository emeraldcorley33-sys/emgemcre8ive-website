@echo off
echo Copying asset folders to repo...
echo.

xcopy /E /I /Y "..\website-mockups" "website-mockups"
echo Copied website-mockups

xcopy /E /I /Y "..\website-design-mockups" "website-design-mockups"
echo Copied website-design-mockups

xcopy /E /I /Y "..\barbie-birthday-package-website" "barbie-birthday-package-website"
echo Copied barbie-birthday-package-website

xcopy /E /I /Y "..\two-fast-birthday-package-website" "two-fast-birthday-package-website"
echo Copied two-fast-birthday-package-website

xcopy /E /I /Y "..\in-full-bloom-birthday-package" "in-full-bloom-birthday-package"
echo Copied in-full-bloom-birthday-package

xcopy /E /I /Y "..\emgemcre8ive-logos-svg" "emgemcre8ive-logos-svg"
echo Copied emgemcre8ive-logos-svg

xcopy /E /I /Y "..\emgemcre8ive-logos-png" "emgemcre8ive-logos-png"
echo Copied emgemcre8ive-logos-png

xcopy /E /I /Y "..\emgemcre8ive-website-icons" "emgemcre8ive-website-icons"
echo Copied emgemcre8ive-website-icons

xcopy /E /I /Y "..\printables" "printables"
echo Copied printables

copy /Y "..\*.jpg" .
copy /Y "..\*.png" .
echo Copied loose image files

echo.
echo ✓ All assets copied successfully!
echo.
echo Now run: git add . && git commit -m "Add all asset folders" && git push
pause
