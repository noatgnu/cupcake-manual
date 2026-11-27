Title: Running the appliance
Order: 12
Appliance: yes
Summary: Storage, backups, Wi-Fi and power on a Cupcake appliance.
Screens: admin/storage, admin/backup, admin/wifi, admin/power

## Storage

**Storage Management** mounts a USB drive by its label, or an NFS or SMB share, at `/mnt/cupcake-data`, and shows
what is mounted.

## Backups

**Backup Management** backs up the database, the uploaded files, or both, to the mounted storage or another folder
under `/mnt/cupcake-data` or `/opt/cupcake/backups`, and lists the backups made.

## Wi-Fi

**WiFi Management** connects to a Wi-Fi network with a password (WPA2 Personal) or an institutional account (WPA2
Enterprise, such as eduroam), and shows the connection.

## Power

**Power** restarts the backend or the appliance, or shuts it down. After shutting down, wait until its lights stop
before unplugging it.
