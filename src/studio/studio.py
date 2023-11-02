class Studio(object):
    def __init__(self, name, num_rows, num_cols):
        self.name = name
        self.num_rows = num_rows
        self.num_cols = num_cols
    def get_name(self):
        return self.name
    def get_num_rows(self):
        return self.num_rows
    def get_num_cols(self):
        return self.num_cols
    def set_name(self, name):
        self.name = name
    def set_num_rows(self, num_rows):
        self.name = num_rows
    def set_num_cols(self, num_cols):
        self.name = num_cols
    def is_Available(self,row, col):
        pass