Title: Running the appliance
Order: 16
Appliance: yes
Summary: Storage, backups, Wi-Fi, remote access, plugins and power on a Cupcake appliance.
Screens: admin/storage, admin/backup, admin/wifi, admin/remote-access, admin/plugins, admin/power

## Storage

**Storage Management** mounts a USB drive by its label, or an NFS or SMB share, at `/mnt/cupcake-data`.

## Backups

**Backup Management** backs up the database, the uploaded files, or both, to the mounted storage or another folder
under `/mnt/cupcake-data` or `/opt/cupcake/backups`, and lists the backups made.

## Wi-Fi

**WiFi Management** connects to a network with a password (WPA2 Personal) or an institutional account (WPA2
Enterprise, such as eduroam).

## Remote access

**Remote Access** shows whether the appliance is on a Tailscale tailnet or a Cloudflare tunnel, and the commands that
set them up.

## Plugins

**Plugins** lists the installed plugins and their state, starts, stops and restarts them, installs one from a
`.tar.gz` file, and uninstalls them.

## Power

**Power** restarts the backend or the appliance, or shuts it down. After shutting down, wait until its lights stop
before unplugging it.
