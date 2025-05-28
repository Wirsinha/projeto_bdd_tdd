from agenda import Agenda

def test_agendar_consulta_valida():
    agenda = Agenda()
    resultado = agenda.agendar("15/06/2023", "14:00", "Dr. Silva")
    assert resultado == True
    assert agenda.consultas[0] == {"data": "15/06/2023", "hora": "14:00", "medico": "Dr. Silva"}

def test_agendar_consulta_conflito():
    agenda = Agenda()
    agenda.agendar("15/06/2023", "14:00", "Dr. Silva")
    resultado = agenda.agendar("15/06/2023", "14:00", "Dr. Silva")
    assert resultado == False