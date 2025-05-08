<#
.SYNOPSIS
    Télécharge un fichier .exe, vérifie son hash, l'exécute, loggue et affiche des notifications.
.DESCRIPTION
    - Vérifie que le script tourne en administrateur.
    - Télécharge le .exe depuis une URL.
    - Affiche une barre de progression.
    - Calcule et affiche le SHA256 du fichier téléchargé.
    - Exécute le .exe.
    - Loggue toutes les étapes dans un fichier .log.
    - Affiche des MessageBox WPF pour les statuts.
    - Émet un beep final.
.PARAMETER ExeUrl
    URL directe vers le .exe à télécharger.
.PARAMETER ExeName
    Nom local du fichier .exe.
#>

param(
    [string]$ExeUrl  = "https://raw.githubusercontent.com/TON_USER/TON_REPO/main/test.exe",
    [string]$ExeName = "test.exe"
)

# --- fonctions utilitaires ---

function Assert-Admin {
    if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()
             ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Warning "Ce script doit être lancé en tant qu'administrateur."
        Start-Sleep -Seconds 2
        # ré‑invite l'utilisateur
        Start-Process powershell "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
        exit
    }
}

function Show-Message {
    param($Text, $Title="Info")
    Add-Type -AssemblyName PresentationFramework
    [System.Windows.MessageBox]::Show($Text, $Title) | Out-Null
}

function Download-File {
    param($Url, $OutPath)
    Write-Host "Téléchargement de $Url vers $OutPath"
    Write-Progress -Activity "Téléchargement" -Status "En cours..." -PercentComplete 0
    try {
        Invoke-WebRequest -Uri $Url -OutFile $OutPath -UseBasicParsing -ErrorAction Stop `
            -PercentVariable prog
    }
    catch {
        Write-Error "Échec du téléchargement : $_"
        Show-Message "Échec du téléchargement.`n$_" "Erreur"
        exit 1
    }
    finally {
        Write-Progress -Activity "Téléchargement" -Completed
    }
}

function Calc-Hash {
    param($Path)
    (Get-FileHash -Algorithm SHA256 -Path $Path).Hash
}

function Write-Log {
    param($Msg)
    $logFile = Join-Path $env:TEMP "script.log"
    $timestamp = (Get-Date).ToString("u")
    "$timestamp    $Msg" | Out-File -FilePath $logFile -Append -Encoding UTF8
}

# --- début du script ---

Assert-Admin
Write-Log "Lancement du script en tant qu’administrateur."
Show-Message "Le script va démarrer..." "Démarrage"

# Prépare les chemins
$exePath = Join-Path $env:TEMP $ExeName
Write-Log "Chemin cible : $exePath"

# Téléchargement
Download-File -Url $ExeUrl -OutPath $exePath
Write-Log "Téléchargement terminé."

# Vérification du hash
$hash = Calc-Hash -Path $exePath
Write-Log "SHA256 du fichier : $hash"
Show-Message "Fichier téléchargé.`nSHA256 : $hash" "Téléchargement OK"

# Exécution
Write-Log "Exécution de $exePath"
try {
    Start-Process -FilePath $exePath -Wait
    Write-Log "Processus terminé avec succès."
    Show-Message "L’exécutable s’est terminé correctement." "Terminé"
}
catch {
    Write-Error "Échec de l’exécution : $_"
    Write-Log "Erreur d’exécution : $_"
    Show-Message "Erreur lors de l’exécution.`n$_" "Erreur"
    exit 1
}

# Bip final
[console]::beep(1000,300)
Write-Log "Bip émis."

# Fin
Write-Log "Script terminé."
