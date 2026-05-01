# Your folder address
$RepoPath = "C:\Users\Aurnob\Desktop\Barnackle"

# The Ninja's Diary file (it will create this automatically!)
$DiaryFile = "C:\Users\Aurnob\Desktop\Barnackle\NinjaDiary.txt"

# 10 second timer
$CheckInterval = 300 

Set-Location $RepoPath
$StartTime = Get-Date
Add-Content -Path $DiaryFile -Value "[$StartTime] Ninja Robot woke up and is watching!"

while ($true) {
    $changes = git status --porcelain
    
    if ($changes) {
        $Time = Get-Date
        Add-Content -Path $DiaryFile -Value "[$Time] I saw a change! Saving to GitHub..."
        
        git add .
        git commit -m "Auto-sync: Ninja robot saved this"
        git push
        
        Add-Content -Path $DiaryFile -Value "[$Time] All done! Saved safely."
    }
    
    Start-Sleep -Seconds $CheckInterval
}