# smart_house-Projeto-POO
 Projeto de Casa Inteligente como atividade avaliativa da disciplina de POO do curso de residência em Robótica e IA - Cin UFPE Softex

## Visão Geral do Projeto.
O projeto de Casa Inteligente é um sistema que permite gerenciar e controlar diversos dispositivos eletrônicos em uma residência, como luzes, termostatos e sistemas de segurança, de maneira centralizada. Este sistema utiliza uma combinação de padrões de design de software para garantir um código bem estruturado, modular e de fácil manutenção. A seguir, é apresentada uma visão detalhada dos componentes principais do sistema e os padrões de design empregados.

## Executar o projeto.
Pré condições:
-Python instalado na sua máquina

1. Clone o projeto

2. Para instalar as dependências do projeto, execute o comando:
`py -m pip install -r requirements.txt`

Agora, para iniciar o projeto, rode o arquivo main.py no terminal python.

## Descrições dos principais componentes e padrões de design utilizados.
A classe Home gerencia todos os dispositivos da casa inteligente e garante que apenas uma instância exista durante a execução do programa, implementando o padrão Singleton. Isso evita a criação de múltiplas instâncias que poderiam causar inconsistências no gerenciamento dos dispositivos.

A criação de dispositivos é realizada pela DispositivoFactory, que utiliza o padrão Factory Method para criar instâncias de dispositivos com base no tipo solicitado. Ao receber um tipo de dispositivo (Luz, Termostato, Sistema de Segurança), a fábrica retorna a instância correspondente, encapsulando a lógica de criação e facilitando a adição de novos tipos de dispositivos no futuro.

A classe Device serve como base para todos os dispositivos, definindo a interface comum e o comportamento básico dos dispositivos. Ela herda de Observable, o que a torna capaz de adicionar, remover e notificar observadores sobre mudanças de estado. Isso permite que os dispositivos comuniquem suas mudanças de estado para outras partes do sistema de forma desacoplada. As classes Light, Thermostat e SecuritySystem são implementações concretas de dispositivos específicos, cada uma herdando de Device e implementando comportamentos específicos, como ligar, desligar, aquecer, esfriar, armar e desarmar.

A classe Observable mantém uma lista de observadores e fornece métodos para adicionar, remover e notificar observadores. Ela é herdada pela classe Device para que todos os dispositivos possam notificar seus observadores. A interface Observer define o método update para ser implementado por classes concretas, como ConcreteObserver, que realiza uma ação (como imprimir uma mensagem) quando uma notificação é recebida.

Quando um dispositivo é adicionado à casa, um ConcreteObserver é criado e adicionado ao dispositivo. Isso permite que o ConcreteObserver receba notificações quando o estado do dispositivo mudar. A classe Device, herdando de Observable, gerencia a lista de observadores e notifica-os sobre qualquer mudança de estado.

## Descrição de uso do Projeto.
Ao iniciar o projeto, você deverá inidicar o limite de dispositivos que a casa pode receber.

Após isso, você poderá interagir com o menu de opções abaixo:

```
Menu de Opções:
1. Listar dispositivos
2. Adicionar dispositivo
3. Remover dispositivo
4. Controlar dispositivo
5. Dispositivos On
6. Sair
```

1. Liste-os e visualize os estados de cada um.
2. Adicione os dispositivos que você poderá obter de acordo com o limite que você indicou. 
4. Controle os estados dos dispositivos.
3. Remova dipositivos.
5. Saiba quais são os dispositivos que estão em estado de LIGADO.

Inicie adicionando um dispositivo. Você poderá visualizar os dispostivos disponíveis e escolher um. 
```
Digite o limite de dispositivos que a casa inteligente pode receber: 2

Menu de Opções:
1. Listar dispositivos
2. Adicionar dispositivo
3. Remover dispositivo
4. Controlar dispositivo
5. Dispositivos On
6. Sair
Escolha uma opção: 2

Tipos de dispositivos disponíveis:
1. Luz
2. Termostato
3. Sistema de Segurança

Escolha o tipo de dispositivo (1/2/3): 1

Dispositivo Light adicionado.
Dispositivo adicionado com sucesso!

```

A seguir, você poderá controlar cada dispositivo que adicionou, mudando os seus estados. Ao mudar o estado de cada dispositivo, irá ser enviado uma notificação automática de mudança. 

```
Escolha uma opção: 4

Dispositivos:
0. Luz 1. Estado atual: desligada
Digite o índice do dispositivo a ser controlado: 0
Ações disponíveis para Light:
1. Ligar
2. Desligar
Escolha a ação (1/2): 1
Notificação recebida: Luz 1 foi ligada
Ação realizada com sucesso.

```

Você poderá obter também a quantidade de dispotivos que estão ligados e listar cada um deles na opção 1.

```
Escolha uma opção: 5
Número total de dispositivos ligados: 2

Menu de Opções:
1. Listar dispositivos
2. Adicionar dispositivo
3. Remover dispositivo
4. Controlar dispositivo
5. Dispositivos On
6. Sair
Escolha uma opção: 1

Dispositivos:
0. Luz 1. Estado atual: ligada
1. Termostato 1. Estado atual: aquecendo

```

Como requisito do projeto, você poderá desligar todas as luzes.

```
Menu de Opções:
1. Listar dispositivos
2. Adicionar dispositivo
3. Remover dispositivo
4. Controlar dispositivo
5. Dispositivos On
6. Desligar todas as luzes
7. Sair
Escolha uma opção: 6
Notificação recebida: A luz foi 1 desligada.
Notificação recebida: A luz foi 2 desligada.
```

Por fim, qualquer dispotivo pode ser removido a qualquer momento, utilizando a opção 3.

```
Escolha uma opção: 3

Dispositivos:
0. Luz 1. Estado atual: ligada
1. Termostato 1. Estado atual: aquecendo
Digite o índice do dispositivo a ser removido: 0
Dispositivo removido com sucesso.

Menu de Opções:
1. Listar dispositivos
2. Adicionar dispositivo
3. Remover dispositivo
4. Controlar dispositivo
5. Dispositivos On
6. Sair
Escolha uma opção: 1

Dispositivos:
0. Termostato 1. Estado atual: aquecendo


```

