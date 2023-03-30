from src.record import Record

class Artist:
    def __init__(self, name):
        self.name = name 
        self.records = []

    def get_name(self):
        return self.name
    
    def get_records(self):
        return self.records
    
    def get_first_record(self):
        earliest_record = self.records[0]

        for record in self.records:
            if record.year < earliest_record.year:
                earliest_record = record
        
        return earliest_record