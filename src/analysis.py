import pandas as pd
import matplotlib.pyplot as plt
from db_connection import get_connection

def analyze_data():
    conn = get_connection()
    query = "SELECT * FROM students"
    
    df = pd.read_sql(query, conn)
    conn.close()

    print("\nStudent Data:")
    print(df)

    print("\nAverage Marks by Subject:")
    avg_marks = df.groupby("subject")["marks"].mean()
    print(avg_marks)

    # Plot
    avg_marks.plot(kind="bar")
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.tight_layout()

    plt.savefig("output/graphs.png")
    plt.show()
