# Multi-line plot
def plot_multi_line(dat, x, y, factor, x_label = '',
                    y_label = '', title = '', legend = True, xtick =
                    ''):
    factors = dat[factor].unique()
    colourmap = plt.cm.Vega10(range(0, len(factors)))
    colourmap = np.vstack([[0,0,0,1], colourmap]) # Add black to top of
    # colourmap
    fig = plt.figure(figsize = (15, 6))
    ax = fig.gca()
    ax.set_prop_cycle(plt.cycler('color', colourmap))
    for fct in factors:
        d1 = dat[dat[factor] == fct]
        x_dat = d1[x].values
        y_dat = d1[y].values
        ax.plot(x_dat, y_dat, label = fct, marker = 'o')
        if legend:
            ax.legend()
    if len(xtick) > 0:
        ax.set_xticks(xtick)
    ax.set_xlabel(x_label, fontsize = 'x-large')
    ax.set_ylabel(y_label, fontsize = 'x-large')
    ax.set_title(title, loc = 'left', fontsize = 'xx-large')
    ax.tick_params(axis = 'both', labelsize = 14)
    plt.show()
