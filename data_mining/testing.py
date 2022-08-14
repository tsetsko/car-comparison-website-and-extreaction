from datetime import datetime
import os
import pandas as pd

testing_data = {'Date_of_extraction': '2022-08-14',
                'Month_of_production': 2,
                'Year_of_production': 1992,
                'Type_of_engine': 'Бензинов',
                'Horsepower': 133.0,
                'Eurostandard': 'Евро 2',
                'Transmission': 'Ръчна',
                'Car_type': 'Седан',
                'Kilometers_traveled': 156000.0,
                'Colour': 'Тъмно син мет.',
                'Price': 7990,
                'Additional_Data': ['Нов внос', 'Сервизна книжка', '4(5) Врати', 'Лети джанти', 'Халогенни фарове', 'Централно заключване', 'Централно заключване', 'Ел. Огледала', 'Ел. Стъкла', 'Климатроник'],
                'link_to_offer': 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11636815858474400&slink=padj4g'}

class OutputExcel:
    def __init__(self, data_row):
        self.TODAYS_DATE = datetime.today().strftime('%Y-%m-%d')
        self.data_row = data_row
        self.data_row_pd = pd.DataFrame.from_dict(self.data_row).reset_index(drop=True)

    def create_new_excel(self):
        if os.path.isfile(f"data_{self.TODAYS_DATE}-test.xlsx"):
            print(os.path.isfile(f"data_{self.TODAYS_DATE}-test.xlsx"))
            with pd.ExcelWriter(f"data_{self.TODAYS_DATE}-test.xlsx", mode='a', engine='openpyxl', if_sheet_exists="overlay") as writer:
                self.data_row_pd.to_excel(writer, sheet_name="Sheet1", startrow=writer.sheets['Sheet1'].max_row, header=False)
                print(self.data_row_pd)
                print("row added")
        else:
            with pd.ExcelWriter(f"data_{self.TODAYS_DATE}-test.xlsx") as writer:
                self.data_row_pd.to_excel(writer, sheet_name="Sheet1")
                print("sheet created")


out = OutputExcel(testing_data).create_new_excel()
