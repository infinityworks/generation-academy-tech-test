from mycsv import csvparser

def main():
    try:
        with open('./data/people-list.csv') as file:
            while True:
                row = csvparser.read_row(file)

                if row is None:
                    print('End of file reached')
                    break

                print(f'{row[0]} - {row[1]} - {row[2]} - {row[3]}')
    except Exception as e:
        print(f'Error reading CSV file - {str(e)}')
        exit(1)

if __name__ == '__main__':
    main()
