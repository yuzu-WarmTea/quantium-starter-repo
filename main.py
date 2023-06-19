import csv


path0 = 'data/daily_sales_data_0.csv'
path1 = 'data/daily_sales_data_1.csv'
path2 = 'data/daily_sales_data_2.csv'
f_path = 'new_data.csv'
test_path = 'test.csv'
a = 'pink'

sales0 = []
dates0 = []
regions0 = []


# path0 checking for pink morsels
with open (path0, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        line = [value.replace('$','') for value in line]
        if a in str(line):
            # calculating sales for path0
            sale = float(line[1]) * float(line[2])
            sales0.append(str(sale))
            # adding dates into a list
            date = line[3]
            dates0.append(date)
            # adding region into a list
            region = line[4]
            regions0.append(region)


sales1 = []
dates1 = []
regions1 = []  

# path1 checking for pink morsels
with open (path1, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        line = [value.replace('$','') for value in line]
        if a in str(line):
            # calculating sales for path0
            sale = float(line[1]) * float(line[2])
            sales1.append(str(sale))
            # adding dates into a list
            date = line[3]
            dates1.append(date)
            # adding region into a list
            region = line[4]
            regions1.append(region)

sales2 = []
dates2 = []
regions2 = []  

# path2 checking for pink morsels
with open (path2, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        line = [value.replace('$','') for value in line]
        if a in str(line):
            # calculating sales for path0
            sale = float(line[1]) * float(line[2])
            sales2.append(str(sale))
            # adding dates into a list
            date = line[3]
            dates2.append(date)
            # adding region into a list
            region = line[4]
            regions2.append(region)

# zip data sets
rows = zip(sales0,dates0,regions0)
rows1 = zip(sales1,dates1,regions1)
rows2 = zip(sales2,dates2,regions2)

# writing data into new csv file
with open(test_path,'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Sales","Date","Region"]
    writer.writerow(field)

    for row in rows:
        writer.writerow(row)
    for row in rows1:
        writer.writerow(row)
    for row in rows2:
        writer.writerow(row)



