
## 1. Introdução

Com o objetivo de utilizar o Raspberry Pi, foi desenvolvido um software para medir a velocidade da internet conectada ao Raspberry e projetar os valores obtidos no dashboard gratuito do Ubidots.

## 2. Dependências

Este projeto depende das seguintes bibliotecas:

- Python >= 3.5
- requests
- speedtest-cli

Também é preciso fazer uma conta no https://ubidots.com/ e criar seu Dashboard como este:
![Dashboard](https://i.imgur.com/LhY6l9u.png)

## 3. Como rodar

### 3.1 Instalar dependências

``` 
pip3 install speedtest-cli requests
```

### 3.2 Rodar o script

Rode o script que está na pasta ```/src```  com: ```python3 scr/.py```

## 4. Demostração do projeto

### 4.1 Fotos

![alt text](./content/rasp.jpeg)

### 4.2 Vídeo


## 5. Integrantes

- Ubirantan da Motta Filho R.A 20.00928.3
- João Paulo M Socio R.A 20.00704-3
- Luan Teixeira R.A 20.01681-6
- Bruno Davidovitch Bertanha R.A 20.01521-6