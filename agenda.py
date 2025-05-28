class Agenda:
    def __init__(self):
        self.consultas = []

    def agendar(self, data, hora, medico):
        for consulta in self.consultas:
            if consulta["data"] == data and consulta["hora"] == hora and consulta["medico"] == medico:
                return False
        self.consultas.append({"data": data, "hora": hora, "medico": medico})
        return True