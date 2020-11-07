import configparser
def demo_cinfig_parser():
    config = configparser.ConfigParser()
    config.read("demo_config.ini")
    print(config)
    print(config.sections())

    print(list(config))

    psql = config['postgresql']
    print("PSQL:", psql)
    print(list(psql))
    for k in psql:
        print(k, psql[k])

    psql_host = psql['host']
    print('psql_host:', psql_host)
    psql_user = config['postgresql']['user']
    print('psql_user:', psql_user)

    psql_port = psql.get('port',5432)
    print("psql_port:", psql_port)

    config['postgresql']['port'] = str(psql_port)
    with open("demo_config.ini", "w") as f:
        config.write(f)

if __name__ == '__main__':
    demo_cinfig_parser()