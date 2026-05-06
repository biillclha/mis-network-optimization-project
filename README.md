Cybersecurity Attack-Path Analysis: Identifying and Mitigating Lateral Movement Risks in Enterprise Networks

1. Real-World Problem Context
In today's cybersecurity landscape, the primary goal of threat actors (such as ransomware groups or Advanced Persistent Threats) after infiltrating a corporate network is to perform "lateral movement" to reach critical systems. Companies have limited IT budgets and cybersecurity team time. Therefore, it is impossible to patch hundreds of vulnerabilities in a network simultaneously. To allocate resources effectively, it is crucial to proactively identify the routes attackers are most likely to choose, which are the "paths of least resistance."

2. Problem Definition
The objective of this project is to find the lowest cost (easiest) path that an attacker, who has compromised an employee's computer (Employee_PC), would take to reach the company's most critical asset, the Domain_Controller. The identification of this path will be used for prioritizing security patches and making network segmentation decisions.

3. Network Model
This problem is modeled as a Shortest Route / Path Problem. The network infrastructure is structured as a "Directed Graph" showing the access directions between systems. Our goal is to find the route from the starting node to the target node that has the minimum total edge weight.

4. Nodes and Edges
Nodes: Represent the IT assets (servers, computers, routers) on the network. Our network has 6 nodes (Employee_PC, Web_Server, Internal_Router, HR_Database, App_Server, Domain_Controller).

Edges: Represent the network connections and transition points between devices. Our network has 8 edges.

Weights: Represents the "difficulty" of exploiting a cybersecurity vulnerability on each connection, or the "effort" the attacker must expend. A low weight means the vulnerability can be easily exploited (e.g., Weak password = 2, Strict firewall = 6).

5. Selected Algorithm
Dijkstra's Algorithm, which is widely used in optimization theory, was selected to find the shortest and lowest-cost path on the graph.

6. Python Implementation
The project solution was developed using Python. The pandas library was used for data manipulation, NetworkX for network modeling and running Dijkstra's algorithm, and matplotlib for visualizing the results. The data in the network_data.csv file was converted into a graph object and analyzed using the nx.shortest_path() function.

7. Results
According to the results obtained when the algorithm is run, the shortest and least resistant path the attacker will use to reach the Domain_Controller is as follows:
Employee_PC -> Internal_Router -> App_Server -> Domain_Controller

The total "attack effort" (cost) of this route was calculated as 7. As can be seen, instead of going through the Web_Server protected by firewall rules (cost: 5) or the strictly isolated HR_Database (cost: 6), the attacker will choose to proceed via the Internal_Router with a default password and the unpatched App_Server.

8. Managerial Interpretation
These findings provide critical decision-making data for company management and the CISO (Chief Information Security Officer):

Budget and Effort Optimization: Instead of trying to patch all servers, the IT department should urgently allocate its limited effort to closing the vulnerabilities (Privilege Escalation) on the App_Server. This point is the attacker's last stop before jumping to the main target.

Architectural Change: The results show that the security of the Internal_Router is very weak (cost: 2). The board of directors should make an investment decision to place a stricter Zero-Trust network or firewall between employee computers (Employee_PC) and internal network routers.

Proactive Defense: Since the most risky path has been identified, the Blue Team (Defense team) should maximize the log monitoring level on these specific devices (Internal_Router and App_Server).

9. How to Run the Code
Follow the steps below to run the project on your own computer:

Clone the repository to your local machine.

Open the terminal in the project directory and install the required libraries:
pip install -r requirements.txt

Run the solution file:
python src/solution.py

The outputs will appear in the terminal, and the visualization graph will be saved to the results/network_visualization.png path.

10. References
Hagberg, A. A., Schult, D. A., & Swart, P. J. (2008). Exploring Network Structure, Dynamics, and Function using NetworkX.

Management Information Systems Network Optimization Lecture Notes.
