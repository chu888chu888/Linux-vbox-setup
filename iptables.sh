# flush all rules
iptables --flush

# keep existing connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# allow loop back
iptables -A INPUT -i lo -j ACCEPT

# allowed services
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# allow remote ip to mysql
#iptables -A INPUT -p tcp --dport 3306 -s xxx.xxx.xxx.xxx -j ACCEPT

# reject all input
iptables -A INPUT -j REJECT

# reject all forwarding
iptables -A FORWARD -j REJECT

iptables-save