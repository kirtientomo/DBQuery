import streamlit as st
import mysql.connector
from config import DB_CONFIG
from parser import extract_emp_id

def run_query(sql):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        return f"Database error: {str(e)}"

st.set_page_config(page_title="Employee Details Bot", layout="centered")
st.markdown("<h2 style='text-align: center;'>👤 Employee Details Bot</h2>", unsafe_allow_html=True)
st.markdown("---")

# Input field for Employee ID
st.markdown("### 🔍 Enter Employee ID to fetch details:")
emp_id_input = st.text_input("e.g., DO1917356 or 002516")

if emp_id_input:
    emp_id = extract_emp_id(emp_id_input)

    if emp_id:
        st.info(f"🔎 Searching for: `{emp_id}`")

        query_master = f"""
        SELECT *
        FROM DM_EMPLOYEE_DETAILS_MASTER 
        WHERE EMP_ID = '{emp_id}'
        """
        result_master = run_query(query_master)

        if isinstance(result_master, str):
            st.error(result_master)
        elif result_master:
            st.success("✅ Found in main system:")
            st.dataframe(result_master)
        else:
            st.warning("⚠️ Not found in main system. Checking backup...")

            query_backup = f"""
            SELECT * FROM EMPLOYEE_DETAILS_MASTER 
            WHERE EMP_ID = '{emp_id}'
            """
            result_backup = run_query(query_backup)

            if isinstance(result_backup, str):
                st.error(result_backup)
            elif result_backup:
                st.info("ℹ️ Found in backup system:")
                st.dataframe(result_backup)
            else:
                st.error("❌ Employee ID not found in any system.")
    else:
        st.warning("⚠️ Invalid Employee ID format. Please try again.")
