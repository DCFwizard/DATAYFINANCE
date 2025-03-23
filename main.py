# main.py

import yfinance as yf 
import pandas as pd


def get_financials(ticker: str):
    stock = yf.Ticker(ticker)

    # Extract financial data
    balance_sheet = stock.balance_sheet
    income_statement = stock.financials
    cash_flow_statement = stock.cashflow

    # Filter specific years
    years = [2024, 2023, 2022, 2021]
    balance_sheet = balance_sheet.loc[:, balance_sheet.columns.year.isin(years)]
    income_statement = income_statement.loc[:, income_statement.columns.year.isin(years)]
    cash_flow_statement = cash_flow_statement.loc[:, cash_flow_statement.columns.year.isin(years)]

    # Sort columns chronologically
    balance_sheet = balance_sheet[sorted(balance_sheet.columns)]
    income_statement = income_statement[sorted(income_statement.columns)]
    cash_flow_statement = cash_flow_statement[sorted(cash_flow_statement.columns)]

    # Reverse row order
    balance_sheet = balance_sheet[::-1]
    income_statement = income_statement[::-1]
    cash_flow_statement = cash_flow_statement[::-1]

    return balance_sheet, income_statement, cash_flow_statement


def save_to_excel(ticker: str, file_path: str):
    balance_sheet, income_statement, cash_flow_statement = get_financials(ticker)

    with pd.ExcelWriter(file_path) as writer:
        balance_sheet.to_excel(writer, sheet_name="Balance Sheet")
        income_statement.to_excel(writer, sheet_name="Income Statement")
        cash_flow_statement.to_excel(writer, sheet_name="Cash Flow Statement")

    print(f"File saved successfully at {file_path}")


if __name__ == "__main__":
    ticker = "TSLA"
    file_name = f"Financials_{ticker}.xlsx"
    file_path = f"./{file_name}"  # Save to current directory
    save_to_excel(ticker, file_path)
