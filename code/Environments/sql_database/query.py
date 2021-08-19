# WRITE YOUR QUERY IN THE query VARIABLE #

from database import retrieve_data
def write_query():
    query = "SELECT * FROM student"
    return query

if __name__ == "__main__":
    retrieve_data(write_query())