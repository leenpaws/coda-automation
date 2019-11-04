#!/bin/bash

# intentionally only allow coda communications on from a subset of hosts

# Clear
iptables -F INPUT
iptables -F OUTPUT

# Allow list
iplist="127.0.0.1 13.57.10.215 34.220.136.8 34.209.72.71 34.211.231.80 "
for ip in ${iplist}
do
    # Whitelist
    echo "${ip}"
    iptables -A INPUT  -p tcp -s "${ip}" --match multiport --dports 8301:8303 -j ACCEPT
    iptables -A INPUT  -p udp -s "${ip}" --match multiport --dports 8301:8303 -j ACCEPT
    iptables -A OUTPUT -p tcp -d "${ip}" --match multiport --dports 8301:8303 -j ACCEPT
    iptables -A OUTPUT -p udp -d "${ip}" --match multiport --dports 8301:8303 -j ACCEPT
done

# Drop any others
iptables -A INPUT  -p tcp --match multiport --dports 8301:8303 -j DROP
iptables -A INPUT  -p udp --match multiport --dports 8301:8303 -j DROP
iptables -A OUTPUT -p tcp --match multiport --dports 8301:8303 -j DROP
iptables -A OUTPUT -p udp --match multiport --dports 8301:8303 -j DROP
