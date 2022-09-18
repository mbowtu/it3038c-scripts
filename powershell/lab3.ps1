
$IP = getIP
$u = whoami
$a = hostname
$H = $HOST.Version.Major
$g = get-date -UFormat "%A %m/%d/%y"
Write-Host("This machine's IP is $IP. User is $u.Hostname is $a.")
write-host("PowerShell Version $H. Today's Date is $g")