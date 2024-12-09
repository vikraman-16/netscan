<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Netscan - Network Utility Tool</h1>
<p>Perform network operations like port scanning, ARP scanning, pinging devices, and more!</p>

<h2>Features</h2>
<ul>
    <li><strong>Port Scanner:</strong> Scan open ports on a specified IP address.</li>
    <li><strong>Ping Device:</strong> Ping a target IP address to check if it is reachable.</li>
    <li><strong>ARP Scan:</strong> Discover devices on the local network.</li>
    <li><strong>Traceroute:</strong> Trace the route to a specified IP or domain.</li>
    <li><strong>Host Information:</strong> Fetch the IP address associated with a domain.</li>
</ul>

<h2>Installation</h2>
<p>Clone the repository and install dependencies:</p>
<pre><code>git clone https://github.com/<your-username>/netscan.git
cd netscan
pip install scapy</code></pre>

<h2>Usage</h2>
<p>Run the program with:</p>
<pre><code>sudo python3 network_util.py</code></pre>
<p>Choose an option from the menu:</p>
<pre><code>1. Port Scanner
2. Ping a Device
3. Discover Devices (ARP Scan)
4. Trace Route
5. Host Information
6. Exit</code></pre>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<p>&copy; 2024 <a href="https://github.com/<your-username>/netscan">Visit on GitHub</a></p>

</body>
</html>
