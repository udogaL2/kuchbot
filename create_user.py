import psycopg2


def make_user(id, name):
    con = psycopg2.connect(
        database="d9hggm0jvhd4sl",
        user="ecpbxsubadnayj",
        password="f84e88995d120bd61005899c9ea4a1071e83c6273775157495cb76a699e5b5b9",
        host="ec2-3-248-4-172.eu-west-1.compute.amazonaws.com",
        port="5432"
    )

    try:
        cur = con.cursor()

        cur.execute(
            "INSERT INTO USERS (ID, NAME) VALUES ('{}', '{}')".format(str(id), str(name))
        )

    except Exception:
        pass

    con.commit()
    con.close()
