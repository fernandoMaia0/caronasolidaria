from models.Carona import Carona  # Ajuste o caminho do modelo se necessário

class CaronaFactory:
    @staticmethod
    def criar_carona(nome, horario, data, descricao, motorista, endereco_saida, endereco_destino, status='A'):
        """
        Cria uma nova instância de Carona com os dados fornecidos.
        """
        return Carona(
            nome=nome,
            horario=horario,
            data=data,
            descricao=descricao,
            motorista=motorista,
            endereco_saida=endereco_saida,
            endereco_destino=endereco_destino,
            status=status
        )