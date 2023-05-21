"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

#include <stdio.h>

#define MAX_ALUNOS 20 // número máximo de alunos

void leiaVetor(int* v, int n) {
  for (int i = 0; i < n; i++)
    scanf("%d", &v[i]);
}

int main(void) {

  // ENTRADA DE DADOS
  int n, ras[MAX_ALUNOS], notas[MAX_ALUNOS];   // variaveis de referência ras e notas

  printf("Digite o numero de alunos: \n");
  scanf("%d", &n);

  printf("RAs: \n");
  leiaVetor(ras, n);

  printf("Notas: \n");
  leiaVetor(notas, n);

  // PROCESSAMENTO ?
  // SAÍDA
  printf("LISTA DE ALUNOS\nNúmero\t RA\t Nota\n");
  for (int i = 0; i < n; i++)
    printf("%d\t %d\t %d\n", i + 1, ras[i], notas[i]);

  return 0;
}