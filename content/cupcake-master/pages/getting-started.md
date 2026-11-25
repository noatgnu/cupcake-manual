Title: Getting started
Order: 01
Summary: Signing in, finding your way around, notifications and appearance.
Screens: account_login, dashboard:index

cupcake-master creates and looks after Cupcake instances on a Kubernetes cluster, such as a set of Raspberry Pis. Each
instance is a separate Cupcake with its own database, files and address.

## Signing in

Open cupcake-master's address in a browser, for example `https://cupcake-k3s.local`, and sign in with your email
address and password. On a Pi cluster, the first admin login is in `cupcake-k3s-credentials.txt` on the control
plane's boot partition.

![](shot:steps-sign-in/1-sign-in-form)

![](shot:steps-sign-in/2-sign-in-filled)

A wrong email address or password is refused:

![](shot:steps-sign-in/0-wrong-password)

After signing in you see your instances:

![](shot:steps-sign-in/3-signed-in)

## Around the screen

The top menu leads to every page. Staff see Models, Users, Domains, Backups, Remote access and Logs as well.

Icon buttons name their action when the pointer rests on them:

![](shot:screens/12-tooltip)

## Notifications

The bell shows what cupcake-master has to tell you, such as a finished or failed task, an instance over its quota or a
certificate about to expire. Unread ones are counted on the bell.

![](shot:screens/10-notification-menu)

All of them are on the Notifications page:

![](shot:screens/09-notifications)

## Appearance

The account menu chooses a light, dark or automatic appearance, and signs you out. Automatic follows your computer.

![](shot:screens/11-account-menu)

![](shot:screens-dark/01-instances)
