from comunidadeimpressionadora import app, database

# Criar o banco dentro do contexto do Flask
with app.app_context():
    database.create_all()
    print("Banco de dados criado com sucesso!")