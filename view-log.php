<?php
// view-log.php
// Simple log viewer for download tracking

echo "<h2>Download Log</h2>";
echo "<pre style='background:#f8f8f8;padding:16px;border-radius:8px;'>";
if (file_exists('downloads.log')) {
    echo htmlspecialchars(file_get_contents('downloads.log'));
} else {
    echo "No log file found.";
}
echo "</pre>";
?>
