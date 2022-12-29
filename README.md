# tgsim-data-cleaner v.0.1.0

## 1. About

A simple CLI tool that streamlines the process of cleaning TGSIM data. 

The current process of cleaning vehicle recognition data includes:

1. Look through aerial footage frame by frame
2. Record observed vehicle detection errors in an Excel file
3. Use the Excel file to make corresponding changes in the raw data (.csv)

This tool will help researchers speed up the data cleaning process by automating `Step 3` of this process.

## 2. Download

Download links (no installation required):

- For Windows users: Download Link
- For Linux users: (Download link)[https://docs.google.com/uc?export=download&id=1Ihf-7RuiSz6k9EIVr7AMmdJMrEyD9kR2]
- For Mac users: Download link

## 3. Usage

1. Use `Errors_template.xlxs` as the template for recording errors

Excel columns instructions:
| **Column Name** | **Description** |
|----------|----------|
| Initial ID | Car's initial ID |
| Frame Last Seen | Frame number where the car was last observed with the initial ID |
| Time Last Seen | Calculated from `Frame Last Seen` (Do not alter cell content)|
| Changed ID | Car's Changed ID |
| Frame First Seen | Frame number where the car was first observed with the changed ID |
| Time First Seen | Calculated from `Frame First Seen` (Do not alter cell content)|0 Exma

2. To apply changes to raw data run the following command:
```
  ./tgsim_data_cleaner <input_errors_excel_file_name> <input_raw_data_csv_name> <output_cleaned_data_csv_name> 
```

## 4. Example 
- For this example, we are using the following folder where: 
![image](https://user-images.githubusercontent.com/81858354/209454006-4f44cd74-0930-4a84-bb34-57d22a35d5bc.png)

- Errors are recorded in `Example_Errors.xlsx` 

![image](https://user-images.githubusercontent.com/81858354/209454159-30ad2df6-f149-4371-9a28-c8065fd65fc7.png)

- Raw data to be cleaned is stored in`Example_Raw_Data.csv`

![image](https://user-images.githubusercontent.com/81858354/209453958-e6ddfc28-c8b8-4ea5-b320-b9f86143ec29.png)

- Run the following command in terminal: 

```
./tgsim_data_cleaner Example_Errors.xlsx Example_Raw_Data.csv Example_Clenaed_Data.csv
```
- Access the cleaned data `Example_Clenaed_Data.csv`

![image](https://user-images.githubusercontent.com/81858354/209454167-7468860c-f315-42fe-93d3-17705da251e3.png)

![image](https://user-images.githubusercontent.com/81858354/209454155-dfdfb362-53ef-4853-a903-760445673c00.png)

## 5. Contact 
If you have any questions or need assistance, please contact me at jackypark9852@gmail.com or TGSIM Slack!
