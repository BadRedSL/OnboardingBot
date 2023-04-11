import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from typing import Union


def QUERY_GET(connection: any, query: str, param: bool = False) -> Union[tuple, list]:
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            records = cursor.fetchone() if not param else cursor.fetchall()
            return records
    except (Exception, Error) as error:
        print("[ERROR] PostgreSQL", error)


def QUERY(connection: any, query: str):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except (Exception, Error) as error:
        print("[ERROR] PostgreSQL", error)


if __name__ == "__main__":
    try:

        __connection = psycopg2.connect(
            "postgresql://icwsptef:gR5ODsKak2SM-nxdCgY6MpquxjL1u2b2@ziggy.db.elephantsql.com/icwsptef")
        __connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # print(QUERY_GET(__connection, query='SELECT * FROM public."Company"'))
        #
        # print(
        #     QUERY_GET(__connection, query="""SELECT * FROM public."Employee" WHERE full_name = 'werw rwer'""",
        #               param=True))
        #
        # QUERY(__connection, query="""INSERT INTO public."Employee" VALUES (1, 'Galaxy S9', 'Samsung', '4', '63000')""")
        #
        # QUERY(__connection, query="""UPDATE public."Employee" SET id = id + 3000;""")
        #
        # QUERY(__connection, query="""DELETE FROM public."Employee" WHERE full_name='Samsung';""")
        a = QUERY_GET(__connection,
                      query=f"""SELECT full_name, post FROM public."Employee" WHERE true""",
                      param=True)
        print("\n".join([f"{i[0]} \t {i[1]}" for i in a]))

        b = QUERY_GET(__connection,
                      query=f"""SELECT * FROM public."Employee" WHERE full_name != '{"uiu iyu"}'""")
        print("\n".join([f"{i}" for i in b[2:]]))


    except (Exception, Error) as error:
        print("[ERROR] PostgreSQL", error)
