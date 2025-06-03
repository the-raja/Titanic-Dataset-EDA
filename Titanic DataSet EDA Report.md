# Titanic Dataset EDA Report

---

## 1. Overview

- The dataset contains **891 rows** and **12 columns**.
- Missing values were handled:
  - `'Age'` was filled with the **median**.
  - `'Embarked'` was filled with the **mode**.
- Duplicate entries were removed to ensure data consistency.

---

## 2. Key Insights

- **Survival Rates by Class**:
  - First-class passengers had the highest survival rate (**~62%**).
  - Third-class passengers had the lowest survival rate (**~24%**).

- **Age Distribution**:
  - Most passengers were between **20 and 40 years** old.

- **Fare vs. Age**:
  - A wide range of fares was paid across all ages.
  - Higher fares are loosely associated with younger and middle-aged passengers.

---

## 3. Visual Insights

- **Bar Chart**: Highlights that **survival chances increase with passenger class**.
- **Histogram**: Shows a **right-skewed age distribution**, with a peak between **20–30 years**.
- **Scatter Plot**: Illustrates **fare dispersion across age**, with several high-fare outliers.

---