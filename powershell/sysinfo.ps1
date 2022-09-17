$Hello = "Hello, PowerShell"
Write-Host($Hello)
function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}
write-host(getIP)
Send-MailMessage -To "mbowtu@mail.uc.edu" -From "copambow0@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)