# CSV File Combiner

This script allows you to merge two CSV files based on the current date value in the 'update' field and saves the result to a new CSV file. 
Please note that the value of the 'update' column will be replaced with the current date.

## Requirements
- Python 3
 - Pandas Library

You can install dependencies with the command:
```shell
pip install -r requirements.txt
```


## Usage

Run the script as follows:

```shell
python main.py <file1.csv> <file2.csv> <output_file.csv>
```
Where:

- <file1.csv> is the path to the first input CSV file.
- <file2.csv> - path to the second input CSV file.
- <output_file.csv> - the path to the output CSV file where the merge result will be saved.

