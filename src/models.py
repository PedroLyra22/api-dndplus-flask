class Raca:
    def __init__(self, id=None, nome=None, tipo_de_criatura=None, tamanho=None, velocidade=None, tracos_especiais=None, descricao=None):
        self.id = id
        self.nome = nome
        self.tipo_de_criatura = tipo_de_criatura
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.tracos_especiais = tracos_especiais
        self.descricao = descricao

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo_de_criatura': self.tipo_de_criatura,
            'tamanho': self.tamanho,
            'velocidade': self.velocidade,
            'tracos_especiais': self.tracos_especiais,
            'descricao': self.descricao
        }