$BODY = {
$IP = getIP
$u = whoami
$a = hostname
$H = $HOST.Version.Major
$g = get-date -UFormat "%A %m/%d/%y"
Write-Host("This machine's IP is $IP. User is $u.Hostname is $a.")
write-host("PowerShell Version $H. Today's Date is $g")
}
Send-MailMessage -To "mbowtu@ucmail.uc.edu" -From "copambow0@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
