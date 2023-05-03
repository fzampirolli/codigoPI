/* Copyright (C) 2022 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book
 * Language: C
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>5.
 */
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