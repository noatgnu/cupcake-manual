Title: Remote access
Order: 07
Summary: Reaching instances and cupcake-master from outside the local network with Cloudflare or Tailscale.
Screens: dashboard:remote_access

Remote access, in the top menu (staff only), connects the cluster to a Cloudflare tunnel or to Tailscale. A domain then
uses it when it is given the "Cloudflare Tunnel" or "Tailscale" route on its [domains]({filename}domains.md) list.

![](shot:screens/04-remote-access)

## Cloudflare Tunnel

1. In Cloudflare Zero Trust, create a tunnel and copy its token.
2. Paste the token here and choose **Connect**.
3. In the tunnel's Public Hostname list, point each Cloudflare domain, or a wildcard such as `*.example.org`, at the
   address shown on this page.
4. Give the domain the "Cloudflare Tunnel" route.

## Tailscale

A Tailscale domain becomes its own device on your tailnet, such as `lab1.tail1234.ts.net`, with a certificate from
Tailscale.

1. In the Tailscale admin console, under Settings, OAuth clients, create a client with the Devices (Core) and Auth
   Keys write scopes and the `tag:k8s-operator` tag. Your tailnet policy must let `tag:k8s-operator` own `tag:k8s`.
2. Enter the client ID and secret here; cupcake-master installs the Tailscale operator.
3. Add the domain, for example `lab1.tail1234.ts.net`, and give it the "Tailscale" route.

On a Pi cluster, the Pi itself can also join your tailnet with an auth key in `cupcake-tailscale.txt`; see
[setting up a Pi cluster]({filename}pi-cluster.md).
