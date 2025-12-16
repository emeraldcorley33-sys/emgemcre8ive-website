# Read first 606 lines and save back to file
$filePath = "c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\emgemcre8ive-website\index.html"
$content = Get-Content $filePath -Head 606
$content | Set-Content $filePath -Encoding UTF8 -Force
Write-Host "File truncated successfully to 606 lines" -ForegroundColor Green
