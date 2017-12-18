
connect('weblogic','admin123','t3://127.0.0.1:7001')

edit()

startEdit()

cd('/')
cmo.createJDBCSystemResource('ds_demo')

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo')
cmo.setName('ds_demo')

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo/JDBCDataSourceParams/ds_demo')
set('JNDINames',jarray.array([String('jdbc/ds_demo')], String))

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo')
cmo.setDatasourceType('GENERIC')

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo/JDBCDriverParams/ds_demo')
cmo.setUrl('jdbc:postgresql://localhost:5432/wlsdemo')
cmo.setDriverName('org.postgresql.Driver')
set('Password', 'wls123')

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo/JDBCConnectionPoolParams/ds_demo')
cmo.setTestTableName('SQL SELECT 1\n')
cmo.setInitialCapacity(0)
cmo.setMinCapacity(0)
cmo.setMaxCapacity(10)

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo/JDBCDriverParams/ds_demo/Properties/ds_demo')
cmo.createProperty('user')

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo/JDBCDriverParams/ds_demo/Properties/ds_demo/Properties/user')
cmo.setValue('wls')

cd('/JDBCSystemResources/ds_demo/JDBCResource/ds_demo/JDBCDataSourceParams/ds_demo')
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')


cd('/JDBCSystemResources/ds_demo')
set('Targets',jarray.array([ObjectName('com.bea:Name=admin_server,Type=Server')], ObjectName))

activate()

exit()

