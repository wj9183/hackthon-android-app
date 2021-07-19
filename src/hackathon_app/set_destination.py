import mysql.connector
from mysql.connector import Error

def set_destination():
    try :
        connection = mysql.connector.connect(
                host='hackathon-team.crzvgoq5hvu0.ap-northeast-2.rds.amazonaws.com',
                database='hackathon',
                user='hackathon-team',
                password='yh1234')

        if connection.is_connected() :
            db_info = connection.get_server_info()

            #가장 수요가 많은 출발지
            cursor = connection.cursor()
            query = '''select start_x, start_y
                        from users
                        group by start_x, start_y
                        order by count(*) desc limit 2;'''
            cursor.execute(query,)

            start_station_data = cursor.fetchall()
            cursor.close()

            #가장 수요가 많은 종착지
            cursor = connection.cursor()
            query = '''select end_x, end_y
                        from users
                        where start_x = %s and start_y =%s
                        group by end_x, end_y 
                        order by count(*) desc limit 3;'''                  # print("경유지 : ", start_station_data, end='\n\n')

            route = []
            if len(start_station_data) < 2:
                print('set_destination 출발지 수요 부족')
            else:
                for i in range (1+1) :
                    param=(start_station_data[i][0],start_station_data[i][1])
                    cursor.execute(query, param)
                    destination_data = cursor.fetchall()
                    route.append([param, destination_data])                     # print("목적지 : ", destination_data)

            # for i in range (1+1) :
                # print("\n{}수요에 대한 출발지 : {}".format(i+1, route[i][0]))
                # print("{}수요에 대한 목적지 : {}".format(i+1, route[i][1]))

    except Error as e :
        print('\n디비 관련 에러 발생' , e)

    finally :
        cursor.close()
        connection.close()
        print('\nMySQL 커넥션 종료')
    # print(route)
    return route

# hi = set_destination()
# print(hi)