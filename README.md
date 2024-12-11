# Streamlit Dashboard for Customer Analysis

## Overview

This Streamlit dashboard provides an interactive visualization and analysis tool for exploring customer data, particularly focused on customer churn. It includes:

- **Dynamic Filtering:** Filter data by gender, payment method, senior citizen status, and internet service.
- **Key Performance Indicators (KPIs):** Display important metrics like average charges, gender count, and minimum monthly charges.
- **Interactive Visualizations:**
  - Bar charts to display metrics by internet service and payment method.
  - A histogram to visualize monthly charge distributions.
- **Customizable Layout:** Utilize Streamlit’s layout features for optimal user experience.

## Features

- **Dynamic Data Filters:**

  - Filter data based on user-selected criteria from the sidebar.
  - Handle missing or non-numeric values gracefully.

- **KPIs Displayed:**

  - Average Total Charges
  - Gender Count
  - Minimum, Median, and Maximum Monthly Charges

- **Visualizations:**
  - Bar charts for average and monthly charges grouped by internet service and payment method.
  - Histogram for monthly charges distribution.

## Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Pip (Python package manager)

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/0x01-python_dashboard
   cd streamlit-customer-analysis
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your dataset:
   - Place your Excel dataset in the `data/` directory.
   - Ensure the file is named `Telco_customer_churn.xlsx` or update the file path in `first_python_streamlit_dashbord.py`.

## Running the App

1. Start the Streamlit app:

   ```bash
   streamlit run first_python_streamlit_dashbord.py
   ```

2. Open the app in your web browser (default: `http://localhost:8501`).

## Project Structure

```
streamlit-customer-analysis/
├── data/
│   └── Telco_customer_churn.xlsx    # Dataset
├── first_python_streamlit_dashbord.py  # Main Streamlit application
├── requirements.txt                # Required Python libraries
└── README.md                       # Project documentation
```

## Requirements

Add the following to your `requirements.txt` file:

```
pandas
numpy
streamlit
plotly
openpyxl
```

## Usage Instructions

1. Use the sidebar to filter data based on:

   - Gender
   - Payment Method
   - Senior Citizen status
   - Internet Service

2. View the updated KPIs and visualizations dynamically on the main page.

3. Analyze customer trends using interactive bar charts and histograms.

## Troubleshooting

- **Empty Filters:** If the filtered dataset is empty, a warning will appear.
- **Missing Data:** Missing or non-numeric values are handled gracefully with proper conversion or removal.
- **File Path Issues:** Ensure the dataset is located at the correct path or update the script.

## Author

- **Anthony Ndegwa**

Feel free to contribute or reach out for further assistance!
