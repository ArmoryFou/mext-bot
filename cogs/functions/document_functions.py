import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager
import logging
import io

def formula1(formula):
    sectionsd = formula.split(':')
    title = sectionsd[0].strip()
    author = sectionsd[1].strip()
    date = sectionsd[2].strip()
    sections = [(section.strip(), description.strip()) for section_and_desc in sectionsd[3:] for section, description in [section_and_desc.split(';')]]
    rcParams['text.usetex'] = True
    rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'
    fig, ax = plt.subplots()
    plt.subplots_adjust(top=0.9)
    y_position = 0.9
    ax.text(0.5, y_position, r'\textbf{' + title + '}', fontsize=20, ha='center')
    if author != "!":
        y_position -= 0.1
        ax.text(0.5, 0.8, author, fontsize=14, ha='center')
    if date != "!":
        y_position -= 0.05
        ax.text(0.5, y_position, date, fontsize=14, ha='center')
    y_position -= 0.1
    for i, section in enumerate(sections):
        section_title = section[0]
        section_content = section[1]
        x_position = 0.1
        if section_title != "!":
            if "/t" in section_title:
                count1 = section_title.count('/t')
                x_position += 0.1 * count1
                section_title = section_title.replace('/t', '')
            ax.text(x_position, y_position, r'\textbf{' + section_title + '}', fontsize=14)
        if section_content != "!":
            if "/t" in section_content:
                count1 = section_content.count('/t')
                x_position += 0.1 * count1
                section_content = section_content.replace('/t', '')
            ax.text(x_position, y_position - 0.1, section_content, fontsize=20)

        y_position -= 0.15

    ax.axis('off')

    data_stream = io.BytesIO()
    plt.savefig("Formula.png", format='png', bbox_inches='tight', dpi=800)
    plt.close()

    
    
