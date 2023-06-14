import csv

def value(lst):
    if not lst[2].isnumeric() or int(lst[2]) < 50:
        return False
    else:
        return True
    
def sumElement(lst):
    if lst[3].isnumeric() and int(lst[3]) > 40 and lst[4].isnumeric() and int(lst[4]) > 40:
        return 0.2 * int(lst[2]) + 0.4 * int(lst[3]) + 0.4 * int(lst[4])
    elif lst[5].isnumeric() and int(lst[5]) > 40:
        return 0.2 * int(lst[2]) + 0.8 * int(lst[5]) 
    else:
        return 1
    
    
def addNumber():
    with open('evidencija.csv') as f:
        with open("output.csv", "a", newline='') as fp:
            wr = csv.writer(fp, dialect='excel')
            reader = csv.reader(f, delimiter = ',')
            for row in reader:
                if value(row):
                    row.append(sumElement(row))
                else:
                    row.append('NOPP')
               
                wr.writerow(row)
               
def main():
    addNumber()
    

if __name__=='__main__':
    main()