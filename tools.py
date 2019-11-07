#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math


def rotate(table):
    new_table = []
    for i in range(len(table[0])):
            line = []
            for j in range(len(table)):
                    elem = table[j][i]
                    line.append(elem)
            new_table.append(line)
    return new_table


def print_table(table, names, is_rotated = False, name = "", caption = ""):
    table_text = ""
    enable_h = True

    if enable_h:
            if is_rotated:
                    centering = "|c|"
            else:
                    centering = "|"
    else:
            if is_rotated:
                    centering = "c"
            else:
                    centering = ""                

    if is_rotated:
            table = rotate(table)

    for i in range(len(table)):
            if enable_h:
                    centering += 'c|'
            else:
                    centering += 'c'

    table_text += r'\begin{table}[h!]' + '\n'
    table_text += r'\centering' + '\n'
    table_text += r'\begin{tabular}{'+ centering + '}' + '\n'

    if not is_rotated:
            if enable_h:
                    table_text += r'\hline' + '\n'
            for i in range(len(names)):
                    table_text += names[i]
                    if i != len(names) - 1:
                            table_text += ' & '
            table_text += r'\\'

    for i in range(len(table[0])):
            if is_rotated:
                    line = '\t ' + names[i] + ' & '
            else: 
                    line = '\t '
            for j in range(len(table)):
                    elem = table[j][i]
                    if j != 0:
                            line += ' & ' + str(elem)
                    else:
                            line += str(elem)
            line += r'\\' + '\n'
            if enable_h:
                    table_text += r'\hline'
            table_text += line
    if enable_h:
            table_text += r'\hline' + '\n'
    table_text += r'\end{tabular}' + '\n'
    table_text += r'\caption{' + caption + ' }\n'
    table_text += r'\end{table}' + '\n\n'
    save_table_include(table_text, name)


def save_plot_include(plot, name, caption=''):
    namef = 'plots/' + name + '.png'
    inc = r'\input{' + namef + '}'
    plot.savefig(namef)
    save_figure_include(name, caption)
    return


def save_figure_include(plot_name, caption, width = 0.75):
    inc_text = r'\begin{figure}[h!]' + '\n' + r'\centering' + '\n'
    inc_text += r'\includegraphics[width=' + str(width) + r'\linewidth]{plots/' + plot_name + '.png}\n'
    inc_text += r'\caption{' + caption + '}\n' + r'\end{figure}' + '\n'
    namef = 'include/plot_' + plot_name + '.tex'
    file = open(namef, 'w')
    file.write(inc_text)
    file.close()
    print(r'\input{include/plot_' + plot_name + '}')


def save_table_include(table_text, name):
    name = 'table_' + name
    namef = 'include/' + name + '.tex'
    inc = r'\input{include/' + name + '}'
    file = open(namef, 'w')
    file.write(table_text)
    file.close()
    print(inc)
    return


def build_graph(x_a=[], x_l="", y_a=[], y_l="", save = False):
    plt.plot(x_a, y_a,
             color='red', linestyle='',
             marker='o', markersize=4)

    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel(x_l)
    plt.ylabel(y_l)

    if save:
            plt.savefig('.png')

    plt.show()


class Markers:
    markrs = ['o', 's', '^', 'D', 'v']
    counter = 0
    def get_new(self):
        m = self.markrs[self.counter]
        self.counter += 1
        return m


class Colors:
    colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:pink']
    counter = 0
    def get_new(self):
        m = self.colors[self.counter]
        self.counter += 1
        return m


def plot_family(family, xlab, ylab, name, caption):
    clr = Colors()
    mrs = Markers()

    plt.clf()
    fig, ax1 = plt.subplots(1, 1, figsize = (8, 5), dpi = 160)

    for i in family:
        ax1.plot(i[0], i[1], 
            color = clr.get_new(), marker = mrs.get_new(),  linestyle = '')

    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    ax1.set_xlabel(xlab, fontsize = 12)
    ax1.set_ylabel(ylab, rotation = 0, fontsize = 12)

    ax1.yaxis.set_label_coords(-0.05, 1.04)
    ax1.xaxis.set_label_coords(1, -0.06)

    plt.tight_layout()
    #ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    save_plot_include(plt, name, caption)


def table_family(family, headers, name, caption, reverse = False):
    com_h = []
    table = []
    col  = []
    counters = [0 for i in range(len(family))]
    for i in family:
        com_h.extend(i[0])

    com_h = list(set(com_h))
    com_h.sort(reverse = reverse)

    for i in range(len(com_h)):
        col = [com_h[i]]
        for j in range(len(family)):

            try: 
                if family[j][0][counters[j]] == com_h[i]:
                    col.append(family[j][1][counters[j]])
                    counters[j] += 1
                else:
                    col.append('---')
            except:
                col.append('---')

        table.append(col)

    table = rotate(table)
    print_table(table, headers, True, name, caption)
