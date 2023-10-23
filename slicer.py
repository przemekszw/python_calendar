import re

class Slicer():
    def time(self,text):
        self.text = text
        time = re.search(r'\d{2}:\d{2}\s-\s\d{2}:\d{2}',text).group()
        return time
