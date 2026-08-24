# 🍔 Takeaway Density, Deprivation and Obesity in London

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://advance-msc-projecttakeaway-density-deprivation-obesity-in-lon.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**MSc Project – Data Science and Analytics (7COM1075)**  
**Student:** Zisan Ahmed (24162855)  
**Supervisor:** Dr. Sarah Beecham  
**University of Hertfordshire**

---

## 📌 Live Dashboard

**[Click here to view the live interactive dashboard](https://advance-msc-projecttakeaway-density-deprivation-obesity-in-lon.streamlit.app/)**

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Research Question](#research-question)
- [Datasets](#datasets)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [Dashboard Features](#dashboard-features)
- [How to Run Locally](#how-to-run-locally)
- [Project Structure](#project-structure)
- [Future Work](#future-work)
- [References](#references)

---

## 📖 Project Overview

This project investigates the relationship between the density of takeaway food outlets and adult obesity rates across London boroughs, while examining whether area-level deprivation explains this relationship.

The study combines five UK government datasets to create a comprehensive analysis of the food environment in London. Using statistical modelling and an interactive dashboard, the project explores whether areas with more takeaways have higher obesity rates, and whether deprivation is the real driver behind this relationship.

**Why this matters:** Obesity is a major public health issue in the UK, costing the NHS billions annually and contributing to diseases like diabetes, heart disease, and cancer. Understanding the role of the food environment can inform policy decisions about planning restrictions, health interventions, and public health strategies.

---

## 🔬 Research Question

> *"To what extent does the density of takeaway food outlets in London's neighbourhoods predict obesity prevalence, after controlling for area-level deprivation?"*

### Hypotheses

| Hypothesis | Statement | Status |
|------------|-----------|--------|
| **H1** | Areas with more takeaways have higher obesity rates | ❌ Not supported (p = 0.246) |
| **H2** | When deprivation is added, the effect of takeaways weakens or disappears | ❌ Not supported |

**Note:** While the results did not support the hypotheses, this finding itself is valuable. It suggests that the relationship between food environments and obesity is more complex than a simple density-outcome link, and that other factors – such as data limitations, geographic scale, or the quality and type of takeaways – may play a role.

---

## 📊 Datasets

This project integrates five datasets from UK government sources:

| Dataset | Source | Rows | Key Columns |
|---------|--------|------|-------------|
| **FHRS** | Food Standards Agency | 24,352 | BusinessName, BusinessType, PostCode, RatingDate |
| **ONSPD** | Office for National Statistics | 2,723,596 | pcds (postcode), lsoa11cd, lad25cd |
| **IMD 2019** | Ministry of Housing, CLG | 32,844 | LSOA code, IMD Score |
| **Obesity** | Public Health England | 4,377 | Area Code, Value, Time period |
| **Population** | Office for National Statistics | 357 | Code, Name, All ages |

### Data Pipeline
FHRS (takeaways with postcodes)
↓
ONSPD (postcode → LSOA → borough)
↓
Takeaway count per LSOA
↓
IMD 2019 (deprivation scores per LSOA)
↓
Aggregate to borough level (28 boroughs)
↓
Population data (density calculation)
↓
Obesity data (outcome variable)
↓
FINAL DATASET (28 boroughs × 7 columns)


---

## 🛠️ Methodology

### 1. Data Cleaning & Integration

- Filtered FHRS for takeaway businesses only using keyword-based filtering (`Takeaway`, `Fast Food`, `Sandwich`, `Kebab`, `Burger`, `Pizza`, `Fried Chicken`, `Mobile`)
- Mapped 3,710 takeaways to LSOAs using ONSPD (99.4% match rate)
- Counted takeaways per LSOA (1,260 LSOAs with at least one takeaway)
- Added IMD 2019 deprivation scores
- Aggregated to borough level (28 London boroughs)
- Calculated takeaway density: `(takeaway_count / population) × 1000`

### 2. Exploratory Data Analysis

- Summary statistics for all variables
- Correlation matrix (heatmap)
- Scatter plots: takeaway density vs obesity, deprivation vs obesity
- Bar chart: takeaway density by borough

### 3. Trend Analysis

- Analysed takeaway count trends over time using linear regression
- Analysed obesity rate trends over time using linear regression
- **Takeaway trend:** Slope = 260.9 takeaways/year (p = 0.003) ✅ Significant
- **Obesity trend:** Slope = 0.34 percentage points/year (p = 0.002) ✅ Significant

> *The significant upward trends in both variables highlight the importance of acknowledging the time mismatch between datasets (FHRS up to 2022, IMD 2019, Obesity up to 2025) as a limitation.*

### 4. Regression Modelling

**Model A (Bivariate):** `obesity_rate = β₀ + β₁ × takeaway_density_per_1000`

| Metric | Value |
|--------|-------|
| R² | 0.0514 |
| Adj R² | 0.0150 |
| p-value (β₁) | 0.2458 ❌ Not significant |

**Model B (Multivariate):** `obesity_rate = β₀ + β₁ × takeaway_density_per_1000 + β₂ × IMD_Score`

| Metric | Value |
|--------|-------|
| R² | 0.0566 |
| Adj R² | -0.0189 |
| p-value (β₁) | 0.2377 ❌ Not significant |
| p-value (β₂) | 0.7147 ❌ Not significant |

### 5. Regression Diagnostics

| Assumption | Test | Result | Status |
|------------|------|--------|--------|
| Linearity | Visual Check | No clear pattern | ✅ Pass |
| Normality | Shapiro-Wilk | p = 0.6518 | ✅ Pass |
| Homoscedasticity | Breusch-Pagan | p = 0.9167 | ✅ Pass |
| No Multicollinearity | VIF | 1.65 | ✅ Pass |
| Independence | Durbin-Watson | 2.4415 | ✅ Pass |

✅ **All assumptions satisfied.** The regression models are statistically valid.

---

## 📈 Key Findings

### Summary Statistics

| Variable | Mean | Min | Max |
|----------|------|-----|-----|
| Takeaway Density (per 1,000) | 0.51 | 0.002 (Barnet) | 3.09 (Camden) |
| IMD Score | 23.07 | 8.32 (Barnet) | 32.92 (Barking) |
| Obesity Rate (%) | 57.66 | 45.58 (H&F) | 71.66 (Barking) |

### Top 5 Boroughs by Takeaway Density

| Borough | Density | IMD Score | Obesity Rate |
|---------|---------|-----------|--------------|
| Camden | 3.09 | 19.95 | 48.90% |
| Southwark | 1.54 | 25.44 | 52.12% |
| Islington | 1.10 | 27.75 | 49.84% |
| Hackney | 1.09 | 32.68 | 56.09% |
| Barking & Dagenham | 1.07 | 32.92 | 71.66% |

### Correlations

| Relationship | Correlation |
|--------------|-------------|
| Takeaway Density ↔ Obesity | -0.227 (weak) |
| IMD Score ↔ Obesity | 0.037 (very weak) |
| Takeaway Density ↔ IMD Score | 0.150 (weak) |

---

## 🎨 Dashboard Features

The interactive Streamlit dashboard allows users to:

- **Select a borough** from a dropdown menu
- **View key metrics** for the selected borough (takeaway density, IMD score, obesity rate)
- **Explore an interactive map** of London showing takeaway density by borough
- **See scatter plots** with the selected borough highlighted
- **View a bar chart** comparing all boroughs
- **Explore a correlation matrix** heatmap
- **Understand rankings** – how each borough compares to others

### Dashboard Preview

The dashboard includes:
- 🗺️ Interactive map with circles sized by density
- 📊 Sidebar with borough selector and metrics
- 🔴 Selected borough highlighted in all plots
- 📈 Correlation matrix for quick insights
- 📉 Rankings showing relative performance

---

## 💻 How to Run Locally

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Advance-MSc-Project_Takeaway-Density-Deprivation-Obesity-in-London.git
cd Advance-MSc-Project_Takeaway-Density-Deprivation-Obesity-in-London

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run the Dashboard

streamlit run dashboard.py


Step 4: Run the Jupyter Notebook
To explore the full analysis:

jupyter notebook "MSc_Project_Source_Code.ipynb"


🔮 Future Work
Based on the findings and limitations of this study, future research could:

- Use more recent takeaway data – The FHRS data used in this study goes up to 2022. More recent data would reduce the time mismatch with obesity data.

- Analyse at LSOA level – Borough-level aggregation may mask neighbourhood-level effects. Future work could use LSOA-level obesity data if available.

- Consider takeaway quality – Not all takeaways are the same. Differentiating by cuisine type, portion size, or nutritional content could reveal more nuanced relationships.

- Include other food environment factors – Supermarkets, grocery stores, and access to fresh produce also play a role in the food environment.

- Longitudinal analysis – Tracking changes over time could help establish causal relationships.





