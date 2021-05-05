class Place:
    def __init__(self,file):
        self.file_name=file
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