function Invoke-CheckAndSync {
    # Step 1: Make a GET request to check the server status
    $checkResponse = Invoke-RestMethod -Uri "http://localhost:8000/check_system" -Method Get -TimeoutSec 30 -ErrorAction SilentlyContinue 

    if ($checkResponse -eq "OK") {
        # Step 2: If OK, make a GET request to sync tables
        $syncResponse = Invoke-RestMethod -Uri "http://localhost:8000/smart-api/sync_tables" -Method Get -TimeoutSec 200 -ErrorAction SilentlyContinue
        if ($null -ne $syncResponse) {
            Write-Host "Tables synced successfully."
            return $true
        } else {
            Write-Host "Failed to sync tables."
            return $false
        }
    } elseif ($null -eq $checkResponse) {
        Write-Host "Check failed. Server might not be running."
        return $false
    }
}

# Try steps 1 and 2 initially
$initialTry = Invoke-CheckAndSync

if (-not $initialTry) {
    # Step 3: If initial check/sync fails, start the FastAPI app
    Write-Host "Attempting to start the FastAPI server..."
    Start-Job -ScriptBlock {
        Set-Location "C:\Users\User\powerbi\fast-ps-app"
        uvicorn main:app --port 8000
    }
    Write-Host "Server started successfully."
    Start-Sleep -Seconds 15 # Give some time for the server to start

    # After starting the server, retry steps 1 and 2
    Write-Host "Retrying check and sync after starting the server..."
    $retryAttempt = Invoke-CheckAndSync

    if (-not $retryAttempt) {
        Write-Host "Failed to check or sync after retrying."
    }
} else {
    Write-Host "Initial check and sync were successful."
}
