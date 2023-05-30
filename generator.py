from datetime import datetime
import pandas as pd
import rules


class ScheduleGenerator():

    def __init__(self, excel_path):
        # INIT df from imported excel schedule
        head = []
        for i in range(1, 32):
            for j in range(2):
                if j == 0:
                    head.append(str(i) + 'NM')
                else:
                    head.append(str(i) + 'EM')

        self.schedule_df = pd.read_excel(
            excel_path, index_col=None, names=head)
        self.schedule_df = self.schedule_df.fillna(' ')

    def generate(self):
        # GENERATE schedule by given rules
        print(self.schedule_df.head())
        return self.schedule_df

    def export(self):
        # EXPORT generated df to an excel file
        file_name = str(datetime.now())[
            :-10].replace(':', '-').replace(' ', '_') + '.xlsx'
        with pd.ExcelWriter(file_name) as writer:
            self.generate().to_excel(writer)
