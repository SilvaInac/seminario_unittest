# Hands On - unittest (python).
Repositório para apresentação do Hands On no seminario de testes unitários de C214 (Eng. de Software) do Inatel.

## Como rodar?
### Pré-requisitos:
- Python 3.9.x;
- Python venv.

### Passo à passo:
- Entrar no diretório do repositório;
  ```
  cd seminario_unittest/
  ```

- Criar ambiente virtual Python;
  ```
  python3.9 -m venv ./
  ```

- Ativar ambiente virtual Python;
  ```
  source bin/activate
  ```

- Instalar dependencias;
  ```
  pip install -r requirements.txt
  ```

- Rodar exemplo funcional;
  ```
  python src/main.py
  ```

- Rodar suite de testes;
  ```
  python -m unittest
  ```

- Rodar testes gerando relatório de testes.
  ```
  python -m coverage run -m unittest && python -m coverage report && python -m coverage html
  ```