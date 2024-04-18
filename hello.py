import argparse 
import xlsxwriter 
 
def txt_to_excel(input_file, output_file): 
    workbook = xlsxwriter.Workbook(output_file) 
    worksheet = workbook.add_worksheet() 
 
    with open(input_file, 'r') as file: 
        row = 0 
        for line in file: 
            data = line.strip().split() 
            for col, item in enumerate(data): 
                worksheet.write(row, col, item) 
            row += 1 
 
    workbook.close() 
    print(f'datas from txt file "{input_file}"recorded to Excel "{output_file}"') 
 
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='from txt to Excel') 
    parser.add_argument('input_file', type=str, help='directory to txt file') 
    parser.add_argument('output_file', type=str, help='directory to excel file') 
    args = parser.parse_args() 
 
    txt_to_excel(args.input_file, args.output_file)