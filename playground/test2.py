import psycopg

with psycopg.connect("dbname=testdb user=literate-waffle") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            create table test(
                id int primary key,
                name text    
                )
        """)

    conn.commit()
