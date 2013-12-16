apt-get install pptpd

/etc/pptpd.conf

	option /etc/ppp/pptpd-options
	logwtmp
	debug
	localip 10.0.0.1
	remoteip 10.0.0.2-200

/etc/ppp/chap-secrets

	# Secrets for authentication using CHAP
	# client        server  secret                  IP addresses
	username     	*       password                *

/etc/ppp/pptpd-options

	name domain.com
	refuse-pap
	refuse-chap
	refuse-mschap
	require-mschap-v2
	require-mppe-128
	proxyarp
	nodefaultroute
	debug
	nobsdcomp
	auth
	ms-dns 8.8.8.8
	ms-dns 8.8.4.4

service pptpd restart

/etc/sysctl.conf

	net.ipv4.ip_forward = 1

	sysctl -p

iptables -A POSTROUTING -t nat -o eth0 -j MASQUERADE
iptables -A POSTROUTING -t nat -o ppp+ -j MASQUERADE
iptables -A INPUT -p gre -j ACCEPT
iptables -A OUTPUT -p gre -j ACCEPT

iptables-save > /etc/iptables.up.rules