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
        header h1 {
            margin: 0;
            font-size: 2.5em;
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
        ul {
            list-style-type: disc;
            margin-left: 20px;
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
        .btn:hover {
            background-color: #0056b3;
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
        <h3>1. Clone the Repository</h3>
        <pre><code>git clone https://github.com/<your-username>/netscan.git</code></pre>
        <p>Navigate to the project directory:</p>
        <pre><code>cd netscan</code></pre>

        <h3>2. Install Dependencies</h3>
        <p>Install the required Python library <strong>scapy</strong>:</p>
        <pre><code>pip install scapy</code></pre>
    </section>

    <section>
        <h2>Usage</h2>
        <h3>Running the Program</h3>
        <p>To run the program, execute the script with Python 3:</p>
        <pre><code>sudo python3 network_util.py</code></pre>
        <p>Note: Some operations (like ARP scan and traceroute) require elevated privileges, so you may need to run the script with <strong>sudo</strong>.</p>

        <h3>Menu Interface</h3>
        <p>Once the program is running, you will see a menu with the following options:</p>
        <pre><code>
1. Port Scanner
2. Ping a Device
3. Discover Devices (ARP Scan)
4. Trace Route
5. Host Information
6. Exit
        </code></pre>

        <h3>Choose an Option</h3>
        <ul>
            <li>For <strong>Port Scanner</strong>, enter the target IP and a list of comma-separated port numbers (e.g., 22,80,443).</li>
            <li>For <strong>Ping a Device</strong>, enter the target IP to check connectivity.</li>
            <li>For <strong>Discover Devices (ARP Scan)</strong>, the program will scan the local network (default range: 192.168.1.0/24).</li>
            <li>For <strong>Trace Route</strong>, enter the target IP or domain.</li>
            <li>For <strong>Host Information</strong>, enter the domain name to get its IP address.</li>
        </ul>

        <h3>Example of Running the Program:</h3>
        <pre><code>
Network Utility Menu:
1. Port Scanner
2. Ping a Device
3. Discover Devices (ARP Scan)
4. Trace Route
5. Host Information
6. Exit
Enter your choice: 1
Enter the target IP: 192.168.1.1
Enter comma-separated port numbers (e.g., 22,80,443): 22,80,443
Scanning ports on 192.168.1.1...
Port 22 is open
Port 80 is open
Port 443 is open
        </code></pre>
    </section>

    <section>
        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <code><a href="LICENSE" class="btn">LICENSE</a></code> file for details.</p>
    </section>

    <section>
        <h2>Contributing</h2>
        <p>Feel free to fork this repository, create issues, and submit pull requests. Contributions are welcome!</p>
    </section>

    <section>
        <h2>Acknowledgments</h2>
        <ul>
            <li><strong>Scapy:</strong> Used for ARP scanning and packet manipulation.</li>
            <li><strong>Python:</strong> The programming language used for the development of this tool.</li>
        </ul>
    </section>
</main>

<footer>
    <p>&copy; 2024 <a href="https://github.com/<your-username>/netscan" class="btn">Visit Project on GitHub</a></p>
</footer>

</body>
</html>
