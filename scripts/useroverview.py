from scripts.db_setup import DataLoading

class UserOverview:
    def __init__(self):
        self.main = DataLoading()
    def load_data(self):
        self.data = self.main.data
        return self.data 
    def basic_data(self):
        rows , column = self.data.shape
        columns = self.data.columns
        head = self.data.head()
        print(f"the data have {rows} rows  and {column} columns")
        print(f" the data have this list of columns {columns}")
        print(f"the data looks like this {head}")





