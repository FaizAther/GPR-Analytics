# WRITE YOUR QUERY IN THE query VARIABLE #

from database import query_data
def write_query():
    query = "SELECT * FROM Student"
    return query

if __name__ == "__main__":
    query_data(write_query())