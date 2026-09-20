import getpass
import snowflake.connector


password = getpass.getpass("Enter your Snowflake password: ")

conn = snowflake.connector.connect(
    account="DYUJPYV-OG68187",
    user="AMALMS",
    password=password,
    warehouse="COMPUTE_WH",
    database="ATMOSYNC_DB",
    schema="RAW"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT CURRENT_DATABASE(), CURRENT_SCHEMA(), CURRENT_WAREHOUSE()
""")

result = cursor.fetchone()

print("Snowflake connection successful!")
print("Database:", result[0])
print("Schema:", result[1])
print("Warehouse:", result[2])

cursor.close()
conn.close()