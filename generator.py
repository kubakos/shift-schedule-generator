from datetime import datetime
import itertools
import pandas as pd
import rules


class ScheduleGenerator():

    def __init__(self, excel_path):
        self.workers_count_by_shift = 4
        head = [i for i in range(1, 32)]
        self.managers_df = pd.read_excel(
            excel_path, names=head, sheet_name='managers')
        self.managers_df = self.managers_df.fillna(" ")
        self.technicians_df = pd.read_excel(
            excel_path, index_col=None, names=head, sheet_name='technicians')
        self.technicians_df = self.technicians_df.fillna(" ")
        self.groups = self.all_combinations_per_shift()

    def all_combinations_per_shift(self):
        workers = [self.technicians_df.index[i][0]
                   for i in range(len(self.technicians_df.index))]

        args = set()

        for i in range(4):
            args.add(set(workers))

        print(args)
        # for combination in itertools.product(*args):
        #     print(combination)

    def generate(self):
        schedule = []
        for day in range(1, 32):
            NM = rules.primary(day, self.groups)
            EM = rules.primary(day, self.groups)
            schedule.append([NM, EM])

        print(len(schedule))

    def export(self):
        file_name = str(datetime.now())[
            :-10].replace(':', '-').replace(' ', '_') + '.xlsx'
        with pd.ExcelWriter(file_name) as writer:
            self.generate().to_excel(writer)
