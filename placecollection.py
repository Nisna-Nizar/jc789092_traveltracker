import csv
class PlaceCollection:
    def __init__(self,file):
        self.file_name=file
    def load_places(self):
        v_count = 0
        p_count = 0
        with open(self.file_name) as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row_data in data:
                if len(row_data) == 0:
                    continue
                display_data = row_data[0].split(',')
                if display_data == '':
                    continue
                if display_data[3] == 'v':
                    print(display_data[0] + ' in ' + display_data[1] + ' priority=' + display_data[2] + '(visited)')
                    v_count = v_count + 1
                else:
                    print(display_data[0] + ' in ' + display_data[1] + ' priority=' + display_data[2])
                    p_count = p_count + 1

        print("Places visted={0}".format(v_count))
        print("Places to visit={0}\n".format(p_count))

    def add_place(self,name,country,priority):
        data1 = [name, country, priority, 'n']
        with open(self.file_name, 'a+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data1)

    def sort_data(self,number):
        v_count = 0
        p_count = 0
        with open(self.file_name) as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            list_data = []
            for row_data in data:
                if len(row_data) == 0:
                    continue
                list_data.append(row_data[0].split(','))
        if number == 2:
            data1 = sorted(list_data, key=lambda list_data: int(list_data[number]))
        else:
            data1 = sorted(list_data, key=lambda list_data: str(list_data[number]).upper())

        for row_data in data1:
            if len(row_data) == 0:
                continue
            display_data = row_data
            if display_data[3] == 'v':
                print(display_data[0] + ' in ' + display_data[1] + ' priority=' + display_data[2] + '(visited)')
                v_count = v_count + 1
            else:
                print(display_data[0] + ' in ' + display_data[1] + ' priority=' + display_data[2])
                p_count = p_count + 1
        print("Places visted={0}".format(v_count))
        print("Places to visit={0}\n".format(p_count))

    def change_visited_status(self, name, visited):
        data1 = []
        with open(self.file_name) as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row_data in data:
                if len(row_data) == 0:
                    continue
                display_data = row_data[0].split(',')
                if str(display_data[0]).lower() == name.lower():
                    display_data[3] = visited
                    data1.append(display_data)
                else:
                    data1.append(display_data)
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for c_dis in data1:
                writer.writerow(c_dis)