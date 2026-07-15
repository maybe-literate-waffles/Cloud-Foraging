import psycopg

curr_id = 0
name = ""


def insert_func(curr_id, name, cur):
    cur.execute(t"INSERT INTO test (id, name) VALUES ({curr_id}, {name})")
    return cur


with psycopg.connect("dbname=testdb user=literate-waffle") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS test(
                id int primary key,
                name text
                );
        """)

        # cur.execute(t"INSERT INTO test (id, name) VALUES ({curr_id}, {name});")
        for i in range(5):
            curr_id = int(input("ID: "))
            name = input("Name: ")

            insert_func(curr_id, name, cur)

    conn.commit()
