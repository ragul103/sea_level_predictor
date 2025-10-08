# Sea Level Predictor

## Overview

The **Sea Level Predictor** analyzes historical global sea level data and predicts future rise up to 2050. It visualizes trends using scatter plots and lines of best fit to compare overall trends versus recent trends since 2000.

---

## Dataset

* File: `epa-sea-level.csv`
* Source: [Download CSV](https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv)
* Contains global average sea level data from 1880 onward.

---

## Installation

Install the required Python libraries:

```bash
pip install pandas matplotlib scipy
```

---

## Usage

1. Place `epa-sea-level.csv` in the project folder.
2. Run the script:

```bash
python sea_level_predictor.py
```

3. The program will:

   * Plot a scatter plot of historical sea level data
   * Draw two lines of best fit (all years vs. since 2000)
   * Predict sea level rise up to 2050
   * Save the plot as `sea_level_plot.png`

---

## Files

* `sea_level_predictor.py` – main code
* `main.py` – optional test file
* `epa-sea-level.csv` – dataset
* `sea_level_plot.png` – generated plot
* `README.md` – project description

---



