<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Netscan - Network Utility</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        header {
            background-color: #007BFF;
            color: white;
            padding: 15px 30px;
            text-align: center;
        }
        main {
            padding: 20px;
        }
        section {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            padding: 20px;
        }
        h2 {
            color: #007BFF;
        }
        code {
            background-color: #f8f9fa;
            padding: 5px;
            border-radius: 4px;
        }
        .btn {
            background-color: #007BFF;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
        }
        footer {
            background-color: #343a40;
            color: white;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>

<header>
    <h1>Netscan - Network Utility Tool</h1>
    <p>Perform network operations like port scanning, ARP scanning, pinging devices, and more!</p>
</header>

<main>
    <section>
        <h2>Features</h2>
        <ul>
            <li><strong>Port Scanner:</strong> Scan open ports on a specified IP address.</li>
            <li><strong>Ping Device:</strong> Ping a target IP address to check if it is reachable.</li>
            <li><strong>ARP Scan:</strong> Discover devices on the local network.</li>
            <li><strong>Traceroute:</strong> Trace the route to a specified IP or domain.</li>
            <li><strong>Host Information:</strong> Fetch the IP address associated with a domain.</li>
        </ul>
    </section>

    <section>
        <h2>Installation</h2>
        <p>Clone the repository and install dependencies:</p>
        <pre><code>git clone https://github.com/<your-username>/netscan.git
cd netscan
pip install scapy</code></pre>
    </section>

    <section>
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
    </section>

    <section>
        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE" class="btn">LICENSE</a> file for details.</p>
    </section>
</main>

<footer>
    <p>&copy; 2024 <a href="https://github.com/<your-username>/netscan" class="btn">Visit on GitHub</a></p>
</footer>

</body>
</html>
