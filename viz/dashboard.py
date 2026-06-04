import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from core.state import QuantumState
from core.gates import H0, CNOT
from core.noise import depolarizing
from physics.bloch import bloch_vector


class QuantumMissionControlV2:
    def __init__(self):

        self.q = QuantumState(2)

        self.circuit = [H0, CNOT]
        self.step = 0

        # history buffers (FIXED)
        self.history_purity = []
        self.history_entropy = []
        self.history_step = []

        self.alert_level = "GREEN"

        self.fig = plt.figure(figsize=(14, 7))

        self.ax1 = self.fig.add_subplot(2, 2, 1)
        self.ax2 = self.fig.add_subplot(2, 2, 2)
        self.ax3 = self.fig.add_subplot(2, 1, 2, projection='3d')

    # --------------------------
    # METRICS
    # --------------------------
    def purity(self, rho):
        return np.real(np.trace(rho @ rho))

    def entropy(self, rho):
        vals = np.linalg.eigvalsh(rho)
        vals = vals[vals > 1e-12]
        return -np.sum(vals * np.log(vals))

    def update_alerts(self, entropy):
        if entropy > 0.8:
            self.alert_level = "RED"
        elif entropy > 0.3:
            self.alert_level = "YELLOW"
        else:
            self.alert_level = "GREEN"

    # --------------------------
    # MAIN LOOP
    # --------------------------
    def update(self, frame):

        # EVOLUTION
        if frame % 25 == 0 and self.step < len(self.circuit):
            self.q.apply(self.circuit[self.step])
            self.step += 1

        self.q.rho = depolarizing(self.q.rho, p=0.015)

        rho = self.q.rho
        probs = np.real(np.diag(rho))

        # METRICS
        purity = self.purity(rho)
        entropy = self.entropy(rho)
        linear_entropy = 1 - purity

        self.update_alerts(entropy)

        # HISTORY
        self.history_purity.append(purity)
        self.history_entropy.append(entropy)
        self.history_step.append(frame)

        N = 200
        self.history_purity = self.history_purity[-N:]
        self.history_entropy = self.history_entropy[-N:]
        self.history_step = self.history_step[-N:]

        # --------------------------
        # TELEMETRY PANEL
        # --------------------------
        self.ax1.clear()
        self.ax1.bar(["00", "01", "10", "11"], probs, color="#00f5ff")

        self.ax1.set_title(f"MISSION TELEMETRY | ALERT: {self.alert_level}")

        self.ax1.text(
            0.02, 0.80,
            f"""STEP: {self.step}
PURITY: {purity:.4f}
ENTROPY: {entropy:.4f}
LINEAR ENT: {linear_entropy:.4f}""",
            transform=self.ax1.transAxes,
            color="#7fdcff"
        )

        # --------------------------
        # HEALTH PANEL
        # --------------------------
        self.ax2.clear()
        self.ax2.plot(self.history_purity, label="Purity", color="#00ffcc")
        self.ax2.plot(self.history_entropy, label="Entropy", color="#ff5555")

        self.ax2.set_ylim(0, 1)
        self.ax2.set_title("SYSTEM HEALTH EVOLUTION")
        self.ax2.legend()

        # --------------------------
        # BLOCH PANEL
        # --------------------------
        rho_red = rho[:2, :2]
        x, y, z = bloch_vector(rho_red)

        self.ax3.clear()

        u = np.linspace(0, 2*np.pi, 25)
        v = np.linspace(0, np.pi, 25)

        xs = np.outer(np.cos(u), np.sin(v))
        ys = np.outer(np.sin(u), np.sin(v))
        zs = np.outer(np.ones_like(u), np.cos(v))

        self.ax3.plot_wireframe(xs, ys, zs, alpha=0.08, color="#00f5ff")

        if len(self.history_purity) > 2:
            traj_x = np.linspace(0, x, len(self.history_purity))
            traj_y = np.linspace(0, y, len(self.history_purity))
            traj_z = np.linspace(0, z, len(self.history_purity))

            self.ax3.plot(traj_x, traj_y, traj_z, color="#00ffcc", alpha=0.6)

        self.ax3.quiver(0, 0, 0, x, y, z, color="#00f5ff")

        self.ax3.set_title("QUANTUM STATE TRAJECTORY")

        return []

    def run(self):
        ani = FuncAnimation(self.fig, self.update, interval=100)
        plt.show()


if __name__ == "__main__":
    app = QuantumMissionControlV2()
    app.run()