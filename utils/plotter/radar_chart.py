import numpy as np
import matplotlib.pyplot as plt


def draw_chart(categories, values):
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})

    ax.fill(angles, values[0], color='skyblue', alpha=0.5)
    ax.fill(angles, values[1], color='green', alpha=0.5)
    ax.set_xticks(angles)
    ax.set_xticklabels(categories)
    ax.set_yticklabels([])
    ax.set_yticks([])
    ax.set_title('Radar Chart', size=16, color='gray', y=1.1)

    plt.show()


if __name__ == '__main__':
    m = {
        'alpha': (4, 3),
        'betta': (3, 9),
        'gamma': (9, 2),
        'delta': (7, 7),
        'epsilon': (9, 8),
        'zeta': (6, 1),
        'eta': (7, 5),
        'theta': (8, 9)
    }
    draw_chart(m.keys(), list(zip(*m.values())))
