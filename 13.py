class data:
    def __init__(self, file_name, file_type, date, size):
        self.file_name = file_name
        self.file_type = file_type
        self.date = date
        self.size = size
        
    def file_open(self):
        f = open(self.file_name , "w")
        f.write("I'm writing something inside the file")
        f.write("  -- I'm again writing something inside the file")
        f.close()
        
    def file_read(self):
        f= open(self.file_name, "r")
        print(f.read())
        f.close()
        
    def file_append(self):
        f= open(self.file_name , "a")
        f.write(" -- I'm appending something INSIDE a file  --")
        f.write(" -- I'm  AGAIN appending something INSIDE a file  --")
        f.close()
        
file1 = data("file1" , "ipynb", "DATA" , "2MB")
file1.file_open()
file1.file_read()
file1.file_append()