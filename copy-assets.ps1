# Copies all referenced asset folders/files from parent directory into this repo
$src = "C:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website"
$dst = "C:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\emgemcre8ive-website"

$folders = @(
    "emgemcre8ive-logos-svg",
    "emgemcre8ive-logos-png",
    "website-design-mockups",
    "website-mockups",
    "two-fast-birthday-package-website",
    "printables"
)

$files = @(
    "20180516_131941.jpg",
    "Snapchat-968965457.jpg",
    "Snapchat-1026403631.jpg",
    "emgemcre8ive-hero-banner.png",
    "emgemcre8ive-hero-banner.svg",
    "mobile-emgemcre8ive-hero-banner (1800 x 2400 px).png",
    "facebook-ig-ad.png",
    "custom-cre8ture-cards.jpg",
    "custom-postcards.png",
    "mockup-bela-website.png",
    "fall-in-love-baby-shower-website-mockup.svg"
)

Write-Output "Copying folders..."
foreach ($f in $folders) {
    $s = Join-Path $src $f
    $d = Join-Path $dst $f
    if (Test-Path $s) {
        robocopy $s $d /E /NFL /NDL /NJH /NJS /NC /NS | Out-Null
        Write-Output "Copied folder: $f"
    } else {
        Write-Output "Missing folder: $f"
    }
}

Write-Output "Copying files..."
foreach ($f in $files) {
    $s = Join-Path $src $f
    $d = Join-Path $dst $f
    if (Test-Path $s) {
        Copy-Item $s $d -Force
        Write-Output "Copied file: $f"
    } else {
        Write-Output "Missing file: $f"
    }
}

Write-Output "Done. Verify with:"
Write-Output "  Get-ChildItem $dst | Select-Object Name"
