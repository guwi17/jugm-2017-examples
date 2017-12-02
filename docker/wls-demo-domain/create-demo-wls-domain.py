#=======================================================================================
# Open a domain template.
#=======================================================================================

selectCustomTemplate("wls/wlserver/common/templates/wls/wls.jar")
loadTemplates()

setOption('NodeManagerType','ManualNodeManagerSetup')
setOption('ServerStartMode','prod')
setOption('OverwriteDomain','true')

domain=cd('/')
domain.setName('demo-wls')

#=======================================================================================
# Configure the Administration Server and SSL port.
#
# To enable access by both local and remote processes, you should not set the 
# listen address for the server instance (that is, it should be left blank or not set). 
# In this case, the server instance will determine the address of the machine and 
# listen on it. 
#=======================================================================================

cd('/Servers/AdminServer')
cmo.setName('admin_server')
cmo.setListenAddress('')
cmo.setListenPort(7001)

create('AdminServer','SSL')
cd('SSL/AdminServer')
cmo.setName('admin_server')
cmo.setListenPort(8001)
cmo.setEnabled(True)

cd('/Security/demo-wls/User/weblogic')
cmo.setPassword('admin123')

domain.setProductionModeEnabled(True)

writeDomain('domains/demo-wls')
closeTemplate()

# enable boot without password
os.makedirs('domains/demo-wls/servers/admin_server/security')
bootprops=open('domains/demo-wls/servers/admin_server/security/boot.properties','w')
bootprops.write('username=%s\npassword=%s\n' % ('weblogic','admin123'))
bootprops.close()


exit()

