# tgsim-data-cleaner v.0.1.0

## 1. About

A simple CLI tool that streamlines the process of cleaning TGSIM data

The current process of cleaning vehicle recognition data includes:

1. Look through aerial footage frame by frame
2. Record observed vehicle detection errors in an Excel file
3. Use the Excel file to make corresponding changes in the raw data (.csv)

This tool will help researchers speed up the data cleaning process by automating `Step 3` of this process.

## 2. Download

Download links (no installation required):

- For Windows users: Download link
- For Linux users: Download link
- For Mac users: Download link

## 3. Usage

1. Use `Errors_template.xlxs` as the template for recording errors

Instructions:
| **Column Name** | **Description** |
|----------|----------|
| Initial ID | Car's initial ID |
| Frame Last Seen | Frame number where the car was last observed with the initial ID |
| Time Last Seen | Calculated from `Frame Last Seen` (Do not alter cell content)|
| Changed ID | Car's Changed ID |
| Frame First Seen | Frame number where the car was first observed with the changed ID |
| Time First Seen | Calculated from `Frame First Seen` (Do not alter cell content)|
