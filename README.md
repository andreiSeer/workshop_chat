# workshop_chat
## Planning Week
Projeto utilizado para demonstrar uso de websockets, django channels e signals.

* Aplicação simples de Chat;

* Utilizando uma estrutura de Websockets;

* Configuração do Django Channels;

* Routing;

* Consumers;

* Groups;

## Como rodar

É necessário instalar os requirements
```
  pip install -r requirements.txt
```
É necessário instalar o redis
```
  sudo apt-get install redis
```
Criar scripts de migração e executá-los
```
  python manage.py makemigrations
  
  python manage.py migrate
```

A aplicação utiliza o sqlite como BD.


