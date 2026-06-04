import matplotlib.pyplot as plt

def apply_nasa_theme():
    plt.style.use("dark_background")

    plt.rcParams.update({
        # background
        "figure.facecolor": "#050814",
        "axes.facecolor": "#070d1a",

        # text + neon cyan
        "axes.edgecolor": "#00f5ff",
        "axes.labelcolor": "#00f5ff",
        "text.color": "#00f5ff",

        # ticks
        "xtick.color": "#7fdcff",
        "ytick.color": "#7fdcff",

        # grid (subtle space grid)
        "grid.color": "#1b2a4a",
        "grid.alpha": 0.35,

        # lines
        "lines.linewidth": 2,
    })
