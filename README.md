tastypie-backbone-example
=========================

(For English, see instructions below)

Este é um repositório criado para treinamento de Tastypie do PythonBrasil 2013. 
É necessário seguir alguns procedimentos para configurar o ambiente, descritos abaixo.

Se você tem uma distribuição Ubuntu/Debian, instale os pacotes abaixo (outras distribuições procurar pacotes equivalentes):
```sh
  sudo apt-get install -f python-dev python-pip git libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev
```
Crie e ative um virtualenv (opcional, p/Linux):

```sh
virtualenv virtual
. virtual/bin/activate
```
  
Instale todas as dependências python:
```sh
pip install -r doc/requirements.txt
```
Opcionalmente também você pode instalar as dependências de JavaScript via bower (mas já estão todas inclusas neste projeto):
```sh
bower install bootstrap backbone backbone-tastypie backgrid
```

English instructions
====================

Tastypie and Backbone integration example (to use in PythonBrasil training course)

Please clone this repo and run the following commands:

If you have Ubuntu/Debian distro, install the following packages (for other distros, search for the related packages, should have the same name)
```sh
  sudo apt-get install -f python-dev python-pip git libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev
```
Create and activate a virtualenv (optional, to run on Linux):

```sh
virtualenv virtual
. virtual/bin/activate
```
  
Install all python dependencies:
```sh
pip install -r doc/requirements.txt
```  
Optionally you can run bower dependencies to install JS (but it's already included in this structure):
```sh
bower install bootstrap backbone backbone-tastypie backgrid
```
