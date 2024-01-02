from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_sucess('que legal')

lf = LogFileMixin()
lf.log_error('qualquer coisa1')
lf.log_sucess('que legal')
