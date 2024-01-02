# Abstração
# Log
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError(
            "Implemente o metodo log"
        )

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} {self.__class__.__name__}'
        print('Salvando... no log', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:  # o a pra n apagar oque ja tiver no documento
            arquivo.write(msg)
            arquivo.write('\n')
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


if __name__ == '__main__':  # pra so executar se quem estiver chamando ele for o main se for de outro modulo n vai executar
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('que legal')

    lf = LogFileMixin()
    lf.log_error('qualquer coisa1')
    lf.log_sucess('que legal')
