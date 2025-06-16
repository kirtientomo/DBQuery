# config.py
DB_CONFIG = {
    'host': st.secrets["HOST"] ,
    'port': st.secrets["PORT"] ,
    'user': st.secrets["USER"] ,
    'password': st.secrets["PASSWORD"] ,
    'database': st.secrets["DBNAME"] 
}
