"""
time_series_visualizer.py
Implements:
 - draw_line_plot()
 - draw_bar_plot()
 - draw_box_plot()

Each function returns a Matplotlib Figure and saves the plot to a PNG file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read and clean data once at import (tests expect this pattern)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data: remove top 2.5% and bottom 2.5% of page views
low = df['value'].quantile(0.025)
high = df['value'].quantile(0.975)
df = df[(df['value'] >= low) & (df['value'] <= high)]

sns.set_style('whitegrid')  # nice default for seaborn plots


def draw_line_plot():
    """Draws and saves the line plot. Returns the matplotlib Figure."""
    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.tight_layout()
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    """Draws and saves the bar plot (average daily page views per month grouped by year).
       Returns the matplotlib Figure.
    """
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month  # numeric month (1..12)

    # Group by year and month, then take mean of values
    df_group = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Replace numeric month columns with month names in the correct order
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_group.columns = month_names

    # Draw bar chart (years on x-axis; grouped bars for each month)
    fig, ax = plt.subplots(figsize=(12, 8))
    df_group.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    fig.tight_layout()
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    """Draws and saves the box plots: year-wise and month-wise. Returns the matplotlib Figure."""
    df_box = df.copy()
    df_box = df_box.reset_index()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')   # 'Jan', 'Feb', ...
    df_box['month_num'] = df_box['date'].dt.month        # for correct ordering

    # Sort by month number so month names align in calendar order for the box plot
    df_box = df_box.sort_values('month_num')

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot (trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot (seasonality) — ensure months from Jan to Dec
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, order=order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.tight_layout()
    fig.savefig('box_plot.png')
    return fig
