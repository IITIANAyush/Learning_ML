# 🧠 Swarm-Oriented Agent Clustering (SOAC) Simulation

This project simulates a **swarm-based multi-agent clustering algorithm** inspired by distributed multi-agent reinforcement learning. It models how agents coordinate, elect leaders, and self-organize into clusters through local communication.

## 🚀 Features

- Agent class with decentralized attributes for leadership, tasks, messaging, and clustering
- Randomized agent networks with bidirectional neighbor connections
- Cluster formation through iterative neighbor-based coordination and message propagation
- Console output of final cluster IDs for each agent

## 📦 Requirements

- Python 3.x
- No external libraries required (`random` is built-in)

## 🧪 How It Works

Each agent may begin with a task (5% chance). Agents with tasks initially become **leaders**. Leadership may be revoked if a neighboring agent has a higher ID. Clusters form through neighbor selection with a capacity limit `c`, repeated over multiple iterations. Agents communicate via a `joinMessage` and dynamically update parents and children.

## 🛠️ Run the Simulation

Clone the repo, then run:

```bash
python soac_simulation.py
