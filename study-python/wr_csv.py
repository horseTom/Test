import csv

class WR_CSV:
    print('读取多个csv文件并写入一个文件')

    def read_csv(self, List):
        rw = []
        for i in range(len(List)):
            with open(List[i], newline='', encoding='UTF-8') as r_csv:
                reader = csv.reader(r_csv)
                for row in reader:
                    rw.append(row)
        return rw

    def write_csv(self, List, wpath):
        rw = self.read_csv(List)
        with open(wpath, 'a', newline='', encoding='UTF-8') as w_csv:
            write = csv.writer(w_csv)
            for i in range(len(rw)):
                if i == 3:
                    pass
                else:
                    write.writerow(rw[i])

test = WR_CSV()
# print(test.read_csv(['test1.csv', 'test2.csv']))
test.write_csv(['test1.csv', 'test2.csv'], 'test.csv')