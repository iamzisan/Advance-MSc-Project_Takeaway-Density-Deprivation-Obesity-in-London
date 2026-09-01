# Investigating Takeaway Density, Deprivation and Obesity in London

**MSc Project** | University of Hertfordshire | September 2026

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

This repository contains the complete source code, data analysis pipeline, and interactive dashboard for my MSc project investigating the relationship between takeaway food outlet density, area-level deprivation, and adult obesity rates across 28 London boroughs.

### Research Question

> *To what extent does the density of takeaway food outlets in London's neighbourhoods predict obesity prevalence, after controlling for area-level deprivation?*

### Key Findings

- **No significant relationship** was found between takeaway density and obesity rates (Model A: R² = 0.051, p = 0.246)
- **Adding deprivation** as a control variable did not improve the model (Model B: R² = 0.057, p = 0.238 for takeaways, p = 0.715 for deprivation)
- **Both takeaways and obesity** have increased significantly over time (takeaways: +260.89/year, p = 0.003; obesity: +0.34 percentage points/year, p = 0.002)
- **All five regression assumptions** were satisfied, confirming model validity

---

## 📂 Repository Structure

```
Advance-MSc-Project_Takeaway-Density-Deprivation-Obesity-in-London/
│
├── 24162855_ZisanAhmed_FPR.pdf              # Final Project Report
├── 24162855_ZisanAhmed_artefact.txt         # Streamlit Dashboard Source Code
├── MSc Project Source Code.ipynb            # Complete Jupyter Notebook
├── READABLE Source Code.html                # HTML Export of Notebook
├── dashboard.py                             # Streamlit Dashboard Application
│
├── Datasets/                                 # Raw datasets (not tracked in repo)
│   ├── food_hygiene_rating_data.csv         # FHRS Data
│   ├── ONSPD_FEB_2026_UK.csv               # ONS Postcode Directory
│   ├── File_7_All_IoD2019_Scores.csv       # IMD 2019 Data
│   ├── indicator-93088-all-areas.data.csv  # Obesity Data
│   └── mye24tablesew.xlsx                  # Population Data
│
└── Outputs/                                  # Generated files
    ├── london_borough_final_data.csv       # Final dataset (28 boroughs)
    ├── final_data_summary.csv              # Summary statistics
    ├── correlation_matrix.csv              # Correlation matrix
    └── *.png                               # All visualisations
```

---

## 📊 Datasets Used

| Dataset | Source | Rows | Purpose |
|---------|--------|------|---------|
| **FHRS** | Food Standards Agency | 24,352 | Identify takeaways |
| **ONSPD** | Office for National Statistics | 2,723,596 | Map postcodes to areas |
| **IMD 2019** | Ministry of Housing, CLG | 32,844 | Deprivation scores |
| **Obesity Data** | Public Health England | 4,377 | Obesity rates |
| **Population Data** | ONS | 357 | Population estimates |

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/iamzisan/Advance-MSc-Project_Takeaway-Density-Deprivation-Obesity-in-London.git
cd Advance-MSc-Project_Takeaway-Density-Deprivation-Obesity-in-London
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Python Packages

```
pandas==2.2.3
numpy==2.1.3
matplotlib==3.9.2
seaborn==0.13.2
statsmodels==0.14.4
scipy==1.14.0
plotly==5.24.0
streamlit==1.39.0
xlrd==2.0.2
```

---

## 🏃 Running the Analysis

### Jupyter Notebook

Open the notebook to run the full analysis pipeline:

```bash
jupyter notebook "MSc Project Source Code.ipynb"
```

The notebook executes the following steps:
1. Load all five datasets
2. Clean and filter data for London
3. Map postcodes to LSOAs and boroughs
4. Calculate takeaway density per 1,000 residents
5. Exploratory data analysis (visualisations, correlations)
6. Build two linear regression models
7. Test all five regression assumptions
8. Generate all outputs and visualisations

---

## 📊 Interactive Dashboard

This project includes an interactive Streamlit dashboard that visualises the key findings.

### Running the Dashboard Locally

After installing the dependencies, navigate to the project directory and run:

```bash
streamlit run dashboard.py
```

This will launch the dashboard in your default web browser at `http://localhost:8501`.

### Dashboard Features

- **Borough Selector** – Dropdown menu to select any of the 28 London boroughs
- **Key Metrics** – Displays takeaway density, IMD Score, and obesity rate for the selected borough
- **Interactive Map** – London map showing takeaway density by borough with hover details
- **Scatter Plots** – Three scatter plots with trendlines showing relationships between variables
- **Bar Chart** – Takeaway density comparison across all boroughs
- **Correlation Matrix** – Heatmap showing correlations between variables

---

## 📈 Results Summary

### Model A: Takeaway Density → Obesity Rate

| Metric | Value |
|--------|-------|
| R-squared | 0.0514 |
| Adjusted R-squared | 0.0150 |
| p-value | 0.2458 (NOT significant) |
| Coefficient | -2.0792 |

### Model B: Takeaway Density + Deprivation → Obesity Rate

| Metric | Value |
|--------|-------|
| R-squared | 0.0566 |
| Adjusted R-squared | -0.0189 |
| Takeaways p-value | 0.2377 (NOT significant) |
| Deprivation p-value | 0.7147 (NOT significant) |

### Regression Diagnostics ✅ All Passed

| Assumption | Test | Result |
|------------|------|--------|
| Linearity | Visual Check | ✅ Pass |
| Normality | Shapiro-Wilk (p = 0.6518) | ✅ Pass |
| Homoscedasticity | Breusch-Pagan (p = 0.9167) | ✅ Pass |
| No Multicollinearity | VIF = 1.65 | ✅ Pass |
| Independence | Durbin-Watson = 2.4415 | ✅ Pass |

---

## 📁 Output Files

All generated files are saved in the `Outputs/` directory:

| File | Description |
|------|-------------|
| `london_borough_final_data.csv` | Final dataset (28 boroughs × 7 variables) |
| `final_data_summary.csv` | Summary statistics |
| `correlation_matrix.csv` | Correlation matrix |
| `correlation_matrix.png` | Correlation heatmap |
| `scatter_plots.png` | 3 scatter plots |
| `scatter_plots_with_trendline.png` | Scatter plots with trendlines |
| `borough_comparison.png` | Bar chart |
| `takeaway_trend.png` | Takeaways over time |
| `obesity_trend.png` | Obesity over time |
| `linearity_check.png` | Linearity diagnostics |
| `normality_check.png` | Q-Q plot & histogram |
| `homoscedasticity_check.png` | Residuals vs fitted |
| `independence_check.png` | Residuals in order |

---

## 🧪 How to Reproduce

1. **Download the datasets** from the sources listed in the methodology
2. **Place them** in the `Datasets/` directory
3. **Run the Jupyter Notebook** to reproduce all analyses
4. **Run the Streamlit dashboard** to view the interactive visualisations

> **Note:** The raw datasets are not included in this repository due to size constraints. Please download them directly from the sources listed in the report.

---

## 📝 Author

**Zisan Ahmed**
- Student ID: 24162855
- MSc Data Science and Analytics
- University of Hertfordshire

**Supervisor:** Dr. Sarah Beecham

---

## 📚 References

The project report contains a complete list of references. Key citations include:

- Burgoine, T., et al. (2018) *International Journal of Behavioral Nutrition and Physical Activity*
- Pineda, E., et al. (2024) *BMJ Nutrition, Prevention & Health*
- Patterson, R., et al. (2021) *Journal of Epidemiology and Community Health*
- Cummins, S., et al. (2014) *Health Affairs*

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgements

- University of Hertfordshire, School of Physics, Engineering and Computer Science
- Dr. Sarah Beecham for supervision and guidance
- Food Standards Agency, ONS, and Public Health England for open data

---

**Project completed:** September 2026

---

*This repository is part of the MSc Data Science and Analytics programme at the University of Hertfordshire.*
