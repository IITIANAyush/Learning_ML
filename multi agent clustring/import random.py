import random
class Agent:
    def __init__(self,ID):
        self.ID=ID
        self.msgFlag = False
        self.ldrFlag = False
        self.clusterID = None
        self.joinMessage = None
        self.children = []
        self.parent = None
        self.neighbors = []
        self.has_task = False

    def __repr__(self):
        return f"Agent({self.ID}, cluster={self.clusterID}, ldr={self.ldrFlag})"
    
    
def initialize_agents(n):
    agents = [Agent(i) for i in range(n)]

    # Randomly assign neighbors (bidirectional)
    for agent in agents:
        agent.neighbors = random.sample([a for a in agents if a != agent], k=random.randint(1, min(3, n-1)))
        for neighbor in agent.neighbors:
            if agent not in neighbor.neighbors:
                neighbor.neighbors.append(agent)

    # Randomly assign tasks
    for agent in agents:
        agent.has_task = random.random() < 0.05  # 5% chance

    return agents

def soac_phase(agents, c=2, iterations=5):
    # Step 1–2: Initialize
    for a in agents:
        a.msgFlag = a.ldrFlag = False
        a.clusterID = a.joinMessage = None
        a.children = []
        a.parent = None
        if a.has_task:
            a.ldrFlag = True

    # Step 3–5: Leader check
    for a in agents:
        if a.ldrFlag and any(x.ldrFlag and x.ID > a.ID for x in a.neighbors):
            a.ldrFlag = False
    for a in agents:
        if a.ldrFlag:
            a.clusterID = a.ID

    # Step 6–28: Form clusters
    for _ in range(iterations):
        for a in agents:
            if a.clusterID is None:
                eligible_neighbors = [x for x in a.neighbors if x.clusterID is not None and len(x.children) < c]
                if eligible_neighbors:
                    chosen = random.choice(eligible_neighbors)
                    chosen.children.append(a)
                    a.parent = chosen
                    a.clusterID = chosen.clusterID
                else:
                    distinct_clusters = {x.clusterID for x in a.neighbors if x.clusterID is not None}
                    if len(distinct_clusters) <= c and distinct_clusters:
                        a.clusterID = a.ID
                        for x in a.neighbors:
                            x.joinMessage = a.ID  # Simplified join logic
                            
        for a in agents:
            for x in a.neighbors:
                if a.joinMessage == x.ID:
                    a.clusterID = x.clusterID
                    if a not in x.children:
                        x.children.append(a)
                    a.parent = x
                    a.joinMessage = None
                    a.children = []

    print("SOAC Phase Complete.\n")
    for a in agents:
        print(a.clusterID)


# --- Run the Simulation ---
if __name__ == "__main__":
    agents = initialize_agents(n=100)
    soac_phase(agents, c=2, iterations=5)