from oracle_config import Ora
import pandas as pd
from email_sender import Email_Sender


connection = Ora()

email_data =connection.get_data_for_email()

dr_name = list()
pt_class = list()
pt_id = list()
pt_name = list()
specialty_code = list()
visit_date_time = list()
address = list()
postal_code = list()
area = list()
town = list()
state = list()
contact1_no = list()
contact2_no = list()
email_id = list()

for email in email_data:
    dr_name.append(email[0])
    pt_class.append(email[1])
    pt_id.append(email[2])
    pt_name.append(email[3])
    specialty_code.append(email[4])
    visit_date_time.append(email[5])
    address.append(email[6])
    postal_code.append(email[7])
    area.append(email[8])
    town.append(email[9])
    state.append(email[10])
    contact1_no.append(email[11])
    contact2_no.append(email[12])
    email_id.append(email[13])
    
    
excel_data =pd.DataFrame({  'PRACTITIONER_NAME': dr_name,
                            'PATIENT_CLASS' : pt_class,
                            'PATIENT_ID' : pt_id,
                            'PATIENT_NAME' : pt_name,
                            'SPECIALTY_CODE':specialty_code,
                            'VISIT_ADM_DATE_TIME':visit_date_time,
                            'ADDRESS':address,
                            'POSTALCODE':postal_code,
                            'AREA':area,
                            'TOWN':town,
                            'STATE':state,
                            'CONTACT1_NO':contact1_no,
                            'CONTACT2_NO':contact2_no,
                            'EMAIL_ID':email_id,

})

#Set destination directory to save excel.
generate_excel = pd.ExcelWriter("Query OPD Data.xlsx",engine='xlsxwriter')

#Write excel to file using pandas to_excel
excel_data.to_excel(generate_excel, startrow = 0, sheet_name='OPD Data', index=False)

#Indicate workbook and worksheet for formatting
workbook = generate_excel.book
worksheet = generate_excel.sheets['OPD Data']

#Iterate through each column and set the width == the max length in that column. A padding length of 2 is also added.
for i, col in enumerate(excel_data.columns):
    # find length of column i
    column_len = excel_data[col].astype(str).str.len().max()
    # Setting the length if the column header is larger
    # than the max column value length
    column_len = max(column_len, len(col)) + 2
    # set the column length
    worksheet.set_column(i, i, column_len)

generate_excel.save()

#"ahmed.qureshi@kokilabenhospitals.com",

send_email = Email_Sender(  "Sarika Jadhav <sarika.jadhav@kokilabenhospitals.com>",
                "kdahpfs@gmail.com", 
                "sarika.jadhav@kokilabenhospitals.com",
                "OPD Data via API",
                "",
                '172.20.200.29',
                25,          
                )


