import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load simulation data
# -----------------------------
df = pd.read_csv("../data/simulation.csv")

t = df["t"]
theta = df["theta"]
theta_dot = df["theta_dot"]
u = df["u"]

# -----------------------------
# Plot state response
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(t, theta, label="theta [rad]")
plt.plot(t, theta_dot, label="theta_dot [rad/s]")
plt.axhline(0.0, linestyle="--", linewidth=1)
plt.title("LQR State Response")
plt.xlabel("Time [s]")
plt.ylabel("State value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../data/state_response.png", dpi=200)

# -----------------------------
# Plot control input
# -----------------------------
plt.figure(figsize=(10, 4))
plt.plot(t, u, label="u = torque [Nm]")
plt.axhline(0.0, linestyle="--", linewidth=1)
plt.title("LQR Control Input")
plt.xlabel("Time [s]")
plt.ylabel("Torque [Nm]")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../data/control_input.png", dpi=200)

# -----------------------------
# Phase portrait
# -----------------------------
plt.figure(figsize=(6, 6))
plt.plot(theta, theta_dot)
plt.scatter([0],  [0], marker="x",  s=100, label="equilibrium")
plt.title("Phase Portrait")
plt.xlabel("theta [rad]")
plt.ylabel("theta_dot [rad/s]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("../data/phase_portrait.png", dpi=200)

print("Saved: state_response.png, control_input.png, phase_portrait.png")