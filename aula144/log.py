# Abstração
# Log
class Log:
    def log(self, msg):
        raise NotImplementedError(
            "Implemente o metodo log"
        )


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)


if __name__ == '__main__':  # pra so executar se quem estiver chamando ele for o main se for de outro modulo n vai executar
    l = LogFileMixin()
    l.log('teste')
