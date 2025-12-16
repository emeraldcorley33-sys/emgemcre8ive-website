# Truncate index.html to exactly 606 lines
$filePath = "c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\emgemcre8ive-website\index.html"

# Read first 606 lines
$content = Get-Content $filePath -Head 606

# Write back to file
$content | Set-Content $filePath -Encoding UTF8 -Force

# Verify
$lineCount = (Get-Content $filePath).Count
Write-Host "SUCCESS: File now has $lineCount lines" -ForegroundColor Green
