from datetime import datetime
import pandas as pd
import rules


class ScheduleGenerator():

    def __init__(self, excel_path):
        # INIT df from imported excel schedule
        head = [i for i in range(1, 63)]
        self.managers_df = pd.read_excel(
            excel_path, index_col=None, names=head, sheet_name='managers')
        self.managers_df = self.managers_df.fillna(' ')
        self.technicians_df = pd.read_excel(
            excel_path, index_col=None, names=head, sheet_name='technicians')
        self.technicians_df = self.technicians_df.fillna(' ')
        self.shift_length = {'H': 0, 'NM': 11, 'EM': 11, 'SZ': 8, 'B': 8}

    def generate(self):
        # GENERATE schedule by given rules
        tmp_df = 0
        shifts = ['NM', 'EM']
        counter = []

        for days in self.managers_df.columns:
            counter.append(days)
            for managers in self.managers_df.index[:4]:
                if days % 2 == 0:
                    pass

    def rate(self):
        pass

    def export(self):
        # EXPORT generated df to an excel file
        file_name = str(datetime.now())[
            :-10].replace(':', '-').replace(' ', '_') + '.xlsx'
        with pd.ExcelWriter(file_name) as writer:
            self.generate().to_excel(writer)
