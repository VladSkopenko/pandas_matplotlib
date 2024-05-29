import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style(style=None, rc=None)
sns.set_style("darkgrid")
data = sns.load_dataset("mpg")
sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)
sns.axes_style()
st = {'axes.facecolor': '#EAEAF2',
      'axes.edgecolor': 'white',
      'axes.grid': True,
      'axes.axisbelow': True,
      'axes.labelcolor': '.15',
      'figure.facecolor': 'white',
      'grid.color': 'white',
      'grid.linestyle': '-',
      'text.color': '.15',
      'xtick.color': '.15',
      'ytick.color': '.15',
      'xtick.direction': 'out',
      'ytick.direction': 'out',
      'lines.solid_capstyle': 'round',
      'patch.edgecolor': 'w',
      'patch.force_edgecolor': True,
      'image.cmap': 'rocket',
      'font.family': ['sans-serif'],
      'font.sans-serif': ['Arial',
                          'DejaVu Sans',
                          'Liberation Sans',
                          'Bitstream Vera Sans',
                          'sans-serif'],
      'xtick.bottom': False,
      'xtick.top': False,
      'ytick.left': False,
      'ytick.right': False,
      'axes.spines.left': True,
      'axes.spines.bottom': True,
      'axes.spines.right': True,
      'axes.spines.top': True}
sns.set_style("darkgrid",  {'axes.labelcolor':"(0.5,0.5,0)", 'axes.edgecolor':'#061358',
'xtick.color':'#0A5806'})
sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)
plt.show()
