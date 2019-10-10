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