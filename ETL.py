df = pd.read_excel('C:\\Users\\asus\\OneDrive\\Desktop\\Internship University\\Internship Project\\HeadCount CTS Folder\\Headcount CTS.xlsx')  
df['First Name'] = df['Employee Name'].str.split().str[0]  
  
engine = sa.create_engine('mssql+pyodbc://DESKTOP-M34O7A7/MyDB2?driver=SQL+Server+Native+Client+11.0&trusted_connection=yes')  
  
df.to_sql(name='EmployeeDATA', con=engine, index=False, if_exists='fail')
