import streamlit as st
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="josuan231",
    database="mydatabase"
)

cursor = connection.cursor()

st.title("Simple Message App by Josuan")

name = st.text_input("Name:")
message = st.text_area("Message: ")

if st.button("Send"):
    insert_query = "INSERT INTO msgtable (Name, Messages) VALUES (%s, %s)"
    data = (name, message)
    cursor.execute(insert_query, data)
    connection.commit()
    st.success("Message sent successfully!")

cursor.close()