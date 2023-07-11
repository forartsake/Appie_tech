import sys
import pandas as pd
from datetime import datetime


class CSVFileCombiner:
    def __init__(self, file1, file2, output_file):
        self.file1 = file1
        self.file2 = file2
        self.output_file = output_file

    def validate_file_extension(self, file_path, extension):
        if not file_path.lower().endswith(extension):
            raise ValueError(f"Invalid file permission {file_path}. Expected file format {extension}.")

    def combine_csv_files(self):
        try:
            self.validate_file_extension(self.file1, '.csv')
            self.validate_file_extension(self.file2, '.csv')

            df1 = pd.read_csv(self.file1)
            df2 = pd.read_csv(self.file2)

            df_merged = pd.concat([df1, df2]) \
                .sort_values('updated', ascending=False) \
                .drop_duplicates(
                'ID') \
                .sort_values('ID')
            df_merged['updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            df_merged.to_csv(self.output_file, index=False)

            print("Script has been executed successfully.")

        except Exception as e:
            print("Something went wrong during execution. Message:", str(e))


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Please specify the path to the first file as the first argument, the path"
              " from to the second file as the second argument, and the path for the new"
              " file with its name as the third argument.")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        output_file = sys.argv[3]

        csv_combiner = CSVFileCombiner(file1, file2, output_file)
        csv_combiner.combine_csv_files()
