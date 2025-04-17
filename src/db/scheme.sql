    CREATE TABLE raca (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50),
        tipo_de_criatura VARCHAR(50),
        tamanho TEXT,
        velocidade INT,
        tracos_especiais TEXT,
        descricao TEXT
    );

    CREATE TABLE classe (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50),
        dado_vida VARCHAR(10),
        testes_resistencia VARCHAR(50),
        pericias_proficientes VARCHAR(100),
        armas_proficientes VARCHAR(50),
        armaduras_proficientes VARCHAR(50),
        equipamento_inicial TEXT
    );