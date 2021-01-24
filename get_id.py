import psycopg2


def get_id():
    con = psycopg2.connect(
        database="d9hggm0jvhd4sl",
        user="ecpbxsubadnayj",
        password="f84e88995d120bd61005899c9ea4a1071e83c6273775157495cb76a699e5b5b9",
        host="ec2-3-248-4-172.eu-west-1.compute.amazonaws.com",
        port="5432"
    )

    cur = con.cursor()
    cur.execute("SELECT ID, NAME from USERS")

    rows = cur.fetchall()
    con.close()
    return [i[0] for i in rows]
