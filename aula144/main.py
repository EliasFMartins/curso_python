# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.log_error('qualquer coisa')
# lp.log_sucess('que legal')

# lf = LogFileMixin()
# lf.log_error('qualquer coisa1')
# lf.log_sucess('que legal')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')
galaxy_s.ligar()
iphone.ligar()