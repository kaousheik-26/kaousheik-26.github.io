#!/usr/bin/env python3
"""Build project_pg_teaser.jpg: two-panel Holmesian scaffolds + Sherlock post-training."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import Patch

OUT_DIR = Path(__file__).resolve().parent
FONT_SCALE = 1.25
OUTPUT_STEM = "project_pg_teaser"


def setup_style() -> None:
    sns.set_theme(style="whitegrid", context="paper")
    plt.rcParams.update(
        {
            "figure.dpi": 180,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "grid.color": "#E6E6E6",
            "grid.linewidth": 0.8,
            "axes.edgecolor": "#CCCCCC",
            "font.size": 10 * FONT_SCALE,
            "axes.titlesize": 11 * FONT_SCALE,
            "axes.labelsize": 10 * FONT_SCALE,
            "xtick.labelsize": 10 * FONT_SCALE,
            "ytick.labelsize": 10 * FONT_SCALE,
            "legend.fontsize": 8 * FONT_SCALE,
        }
    )


def plot_project_pg_teaser() -> None:
    scaffold_order = ["Watson", "Mycroft", "Sherlock"]
    ladder = pd.DataFrame(
        {
            "Scaffold": scaffold_order * 3,
            "Score": [
                13.7,
                14.9,
                17.0,  # Grok-3 Mini
                15.4,
                15.7,
                16.9,  # o3
                13.2,
                12.3,
                16.2,  # Gemini 2.5 Pro
            ],
            "Model": ["Grok-3 Mini"] * 3 + ["o3"] * 3 + ["Gemini 2.5 Pro"] * 3,
        }
    )
    ladder["Scaffold"] = pd.Categorical(
        ladder["Scaffold"], categories=scaffold_order, ordered=True
    )

    bar_labels = ["Base", "SFT", "RL", "o4-mini"]
    bar_means = np.array([4.8, 5.8, 12.3, 15.0], dtype=float)
    bar_colors = ["#6b5b7b", "#a23b72", "#0e7a75", "#c0392b"]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.1, 5.85), sharey=False)

    ax1.axhspan(
        18,
        23,
        facecolor="#C4B5FD",
        alpha=0.32,
        zorder=0,
        edgecolor="none",
    )
    sns.lineplot(
        data=ladder,
        x="Scaffold",
        y="Score",
        hue="Model",
        marker="o",
        linewidth=2.0,
        palette=["#EA580C", "#0F172A", "#2563EB"],
        ax=ax1,
        zorder=2,
    )
    ax1.set_ylim(8, 25)
    ax1.set_title("Holmesian Scaffolds", fontsize=11 * FONT_SCALE, pad=8 * FONT_SCALE)
    ax1.set_xlabel("")
    ax1.set_ylabel("Mean Hanabi Score")
    h1, l1 = ax1.get_legend_handles_labels()
    human_patch = Patch(
        facecolor="#C4B5FD",
        alpha=0.32,
        edgecolor="none",
        label="Strong human player",
    )
    ax1.legend(
        handles=list(h1) + [human_patch],
        labels=list(l1) + ["Strong Human Player"],
        frameon=False,
        title="",
        loc="lower right",
        ncol=2,
        fontsize=8 * FONT_SCALE,
    )

    x = np.arange(len(bar_labels))
    ax2.bar(
        x,
        bar_means,
        color=bar_colors,
        edgecolor="#1F2937",
        linewidth=0.6,
        zorder=2,
    )
    ax2.set_xticks(x)
    ax2.set_xticklabels(bar_labels)
    ax2.set_ylim(0, 17.25)
    ax2.set_yticks([0, 5, 10, 15])
    ax2.set_title(
        "Post-training on our Datasets (Sherlock)",
        fontsize=11 * FONT_SCALE,
        pad=8 * FONT_SCALE,
    )
    ax2.set_xlabel("")
    ax2.set_ylabel("Mean Hanabi Score")
    for i, v in enumerate(bar_means):
        ax2.text(
            i,
            v + 0.35,
            f"{v:.1f}",
            ha="center",
            va="bottom",
            fontsize=8 * FONT_SCALE,
        )

    fig.tight_layout()
    fig.savefig(
        OUT_DIR / f"{OUTPUT_STEM}.jpg",
        format="jpg",
        dpi=250,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    setup_style()
    plot_project_pg_teaser()
    print(f"Saved {OUT_DIR / (OUTPUT_STEM + '.jpg')}")


if __name__ == "__main__":
    main()
