import pandas as pd
def combine_csv_files(input_files: list[str], output_file: str):
    data_frames = []
    for file in input_files:
        data = pd.read_csv(file)
        data_frames.append(data)
    combined_data_frame = pd.concat(data_frames, ignore_index=True)
    combined_data_frame.to_csv(output_file, index=False)
csv_file_one = "./one.csv"
csv_file_two = "./two.csv"
combine_csv_files(input_files=[csv_file_one, csv_file_two], output_file="./result.csv")
