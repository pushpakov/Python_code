# to read the csv file in chunk 
import csv

def read_csv_in_parts(file_path, chunk_size):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            while True:
                chunk = []
                for i in range(chunk_size):
                    row = next(csv_reader, None)
                    if row is None:
                        break
                    chunk.append(row)
                if not chunk:
                    break
                # print("CHUNK STARTED ",chunk)
                yield chunk
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


for part in read_csv_in_parts(r'C:\Users\LENOVO\Desktop\@albanero\doc\Sample.csv', 2):
    print(part)
    print(len(part))





