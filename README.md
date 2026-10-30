# Sales Data Cleaning with Python & Pandas

A small hands-on data cleaning project using Python and Pandas. I started with a messy sales dataset and separated valid records from records that need review instead of guessing missing values.

## What I did
- Standardized product names by removing extra spaces and converting them to lowercase.
- Removed 1 duplicate order.
- Converted the `unit_price` column to numeric values, flagging invalid prices.
- Separated 4 orders with missing prices, missing quantities, or negative quantities for review.
- Kept 6 valid orders.
- Calculated `total = quantity * unit_price` for each valid order.
- Exported the cleaned records and flagged records into separate CSV files.

## Files
- `messy_sales_practice.csv` — original input dataset (11 rows).
- `main.py` — my Python/Pandas cleaning script.
- `clean_sales.csv` — valid cleaned orders (6 rows).
- `needs_review.csv` — orders needing manual review (4 rows).

## Orders needing review

| Order ID | Reason |
| --- | --- |
| 1003 | Missing unit price |
| 1005 | Negative quantity (-1): confirm if this is a return or an entry error |
| 1009 | Invalid price (`abc`) |
| 1010 | Missing quantity |

## Run locally

Install Pandas: `pip install pandas`

Run the script from the project folder: `python main.py`

The script recreates `clean_sales.csv` and `needs_review.csv`.

**Note:** This is a practice dataset for learning data-cleaning workflows. Flagged values were not guessed or filled in.
