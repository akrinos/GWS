
import datetime

gwsconf = {
    'debug' : True,
    'def_sims_per_job' : 5,
    'refresh_delay' : datetime.timedelta(seconds = 30),
    'smtp_server' : 'smtp.gmail.com:587',
    'smtp_user' : 'example',
    'smtp_pass' : 'example',
    'base_working_path' : '/home/grapleadmin/grapleService',
    'serv_addr' : 'https://graple.acis.ufl.edu',
    'download_endpoint' : '/DownloadResults/',
    'retention_unit' : datetime.timedelta(days = 1),
    'retention_after_dl' : datetime.timedelta(hours = 1),
    'graple_db_name' : 'grapleDB',
    'graple_coll_name' : 'grapleColl',
    'api_coll_name' : 'grapleAPI',
    'compression_cores' : 2,
}
