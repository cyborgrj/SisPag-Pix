# SisPag-Pix
## Programa para geração de pagamentos Pix para o cartório onde trabalho, como desenvolvedor em Python.

O programa consiste em criar um pagamento utilizando o layout de 750 posições do bradesco, 
repassando esse pagamento para o Bradesco e consumindo da API as informações de status do 
pagamento (aguardando, cancelado, pago etc.)

Inicialmente (enquanto aguardava-se a autorização do cartório para utilização do serviço)
foi desenvolvido para funcionar de modo manual, onde o setor de contabilidade iria efetuar
liberação manual de cada Pix cadastrado, mediante consulta de extrato, saldo na conta bancária

Num segundo passo agora, está sendo desenvolvido um servidor que irá consumir automaticamente
da API de Pix do Bradesco, as informações dos pagamentos cadastrados.
