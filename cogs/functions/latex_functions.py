import discord
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager


def latex(formula):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.rm'] = 'PazoMath'
    plt.rcParams['mathtext.it'] = 'PazoMath'
    plt.rcParams['mathtext.bf'] = 'PazoMath'
    plt.rcParams['text.usetex'] = True

    fig, ax = plt.subplots()
    ax.axis('off')
    ax.text(0.5, 0.5, formula, ha='center', va='center',fontsize= 25)
    plt.savefig("Formula.png", format='png', bbox_inches='tight', dpi=800)
    plt.close()


