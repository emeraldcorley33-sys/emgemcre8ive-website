# Compress PNG files using built-in Windows tools
# This script reduces image quality to fit GitHub limits

$folders = @(
    "c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\website-design-mockups",
    "c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\website-mockups",
    "c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\printables"
)

# Check if ImageMagick is installed
try {
    $magick = Get-Command magick -ErrorAction Stop
    Write-Output "ImageMagick found at: $($magick.Source)"
    
    foreach ($folder in $folders) {
        if (Test-Path $folder) {
            Get-ChildItem $folder -Filter "*.png" -Recurse | ForEach-Object {
                $file = $_.FullName
                $newFile = $file -replace "\.png$", "_compressed.png"
                Write-Output "Compressing: $($_.Name)"
                & magick "$file" -quality 85 -strip "$newFile"
                Remove-Item $file
                Rename-Item $newFile $file
            }
        }
    }
    Write-Output "Compression complete!"
}
catch {
    Write-Output "ImageMagick not found. Installing ImageMagick..."
    choco install imagemagick -y
    Write-Output "Please run this script again."
}
