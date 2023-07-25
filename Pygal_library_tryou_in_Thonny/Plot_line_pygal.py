
import pygal


def plot_line_function(title, xvals, yvals):
    """DOCSTRING
    Inputs:
    -Title: Title of the chart
    -xvals: sequence of values that will be the x axis
    -yvals: sequence of values that will be y axis
    
    """
    
    lineplot=pygal.Line()
    lineplot.title=title
    lineplot.x_labels=xvals  #Sequence
    lineplot.add("Data",yvals) # .add in pygal is the way to add new sequences of data that you want to actually plot.
    lineplot.render_in_browser()
