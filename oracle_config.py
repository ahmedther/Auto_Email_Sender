import cx_Oracle as oracle
#from oracle_config import *

ip = "172.20.100.121"

host = "emdb1-vip.kdahit.com"

port = 1521

service_name =  "EMRAC.kdahit.com"

instance_name = "EMRAC1"



#ora_db = oracle.connect("appluser","appluser",dsn_tns)

#cursor = ora_db.cursor()


# host = 'khdb-scan'

# port = 1521

# service_name = "newdb.kdahit.com"

# instance_name = "NEWDB"

# dsn_tns = oracle.makedsn(ip,port,instance_name)

# ora_db = oracle.connect("ibaehis","ib123",dsn_tns)

# cursor = ora_db.cursor()



    #   'oracle': {
    #     'ENGINE': 'django.db.backends.oracle',
    #     'NAME': 'NEWDB:1521/newdb.kdahit.com',
    #     'NAME': ('(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=khdb-scan)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=newdb.kdahit.com)))'),
    #     'USER': 'ibaehis',
    #     'PASSWORD': 'ib123',


class Ora:

    def __init__(self):
        self.dsn_tns = oracle.makedsn(ip,port,instance_name)
        self.ora_db = oracle.connect("appluser","appluser",self.dsn_tns)
        self.cursor = self.ora_db.cursor()

    def status_update(self):

        if self.ora_db:
            return "You have connected to the Database"

        else:
            return "Unable to connect to the database! Please contact the IT Department" 

     


    #def __del__(self):
        #self.cursor.close()
        #self.ora_db.close()
    
    def get_data_for_email(self):
        
        sql_qurey = ('''
        

select distinct e.practitioner_name,a.PATIENT_CLASS,
a.patient_id,b.patient_name,a.SPECIALTY_CODE,VISIT_ADM_DATE_TIME,
F.addr1_line1 || ' ' || F.addr1_line2 || ' ' || F.addr1_line3 || ' ' || F.addr1_line4 Address, 
g.long_desc postalcode, h.LONG_DESC area, i.LONG_DESC town, j.LONG_DESC state,B.CONTACT1_NO,B.CONTACT2_NO ,b.EMAIL_ID
from pr_encounter a,mp_patient b,am_practitioner e,MP_PAT_ADDRESSES F,  MP_POSTAL_CODE g,  MP_RES_TOWN h , MP_RES_AREA i, mp_region j
where a.patient_id=b.patient_id AND  A.PATIENT_ID=F.PATIENT_ID and a.ATTEND_PRACTITIONER_ID = e.practitioner_id 
--and (e.PRACTITIONER_name like '%PRADNYA%GADGIL%' or e.PRACTITIONER_name like '%JAYANTI%MANI%') 
and f.POSTAL1_CODE = g.POSTAL_CODE (+) and g.RES_TOWN_CODE = h.RES_TOWN_CODE(+) and h.RES_AREA_CODE = i.RES_AREA_CODE(+)
and i.REGION_CODE = j.REGION_CODE(+) 
and VISIT_ADM_DATE_TIME >= (sysdate-3)
and a.PATIENT_CLASS ='OP' and a.facility_id='KH'
and a.SPECIALTY_CODE IN ('ENDO','CARD','ORTH')


        
        ''')

        self.cursor.execute(sql_qurey)
        user_pass = self.cursor.fetchall()

        if self.cursor:
            self.cursor.close()
        if self.ora_db:
            self.ora_db.close()
     

                     
        return user_pass

    





if __name__ == "__main__":
    a = Ora()
    #b = a.get_online_consultation_report('01-Mar-2022','03-Apr-2022')
    b = a.get_package_contract_report('16-Jun-2018','12-Jan-2022','KH')

    print(b)

    for x in b:
        print(x)