"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

#include <stdio.h>

int main(void) {

  // ENTRADA DE DADOS
  int max = 100; // considerar sempre um número grande
  int n, ra[max];     // aloca 100 ra's
  char nome[max][40]; // aloca 100 nomes de até 40 caracteres cada

  printf("Digite o numero de alunos: ");
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    printf("RA: ");
    scanf("%d", &ra[i]);
    printf("Nome: ");
    scanf("%s", nome[i]); // ATENÇÃO: NÃO ACEITA NOME COM ESPAÇOS e NÃO USA &
  }
  // PROCESSAMENTO ?
  // SAÍDA
  printf("LISTA DE ALUNOS\nNúmero\t RA\t Nome\n");
  for (int i = 0; i < n; i++) {
    printf("%d\t %d\t %s\n", i + 1, ra[i], nome[i]);
  }
  return 0;
}