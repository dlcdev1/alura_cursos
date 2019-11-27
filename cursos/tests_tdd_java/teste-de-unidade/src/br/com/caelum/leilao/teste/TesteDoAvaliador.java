package br.com.caelum.leilao.teste;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Test;

import br.com.caelum.leilao.dominio.Lance;
import br.com.caelum.leilao.dominio.Leilao;
import br.com.caelum.leilao.dominio.Usuario;
import br.com.caelum.leilao.servico.Avaliador;

public class TesteDoAvaliador {
  
  @Test
  public void deveEntenderLancesEmOrdemCrescente() {
    
    // parte 1: cenario
    Usuario joao = new Usuario("João");
    Usuario jose = new Usuario("Jose");
    Usuario maria = new Usuario("Maria");    
    
    Leilao leilao = new Leilao("Playstation 3 novo");
    
    leilao.propoe(new Lance(joao, 250.0));
    leilao.propoe(new Lance(jose, 300.0));
    leilao.propoe(new Lance(maria, 400.0));
    
    // parte 2: acao
    Avaliador leiloeiro = new Avaliador();
    leiloeiro.avaliar(leilao);
    
    // parte 3: validacao
    double maiorEsperado = 400;
    double menorEsperado = 250;
    
    assertEquals(maiorEsperado, leiloeiro.getMaiorLance(), 0.00001);
    assertEquals(menorEsperado, leiloeiro.getMenorLance(), 0.00001);
    
  }
  @Test
  public void deveEntenderLancesEmOrdemCrescenteComOutrosValores() {
    
    // parte 1: cenario
    Usuario joao = new Usuario("João");
    Usuario jose = new Usuario("Jose");
    Usuario maria = new Usuario("Maria");    
    
    Leilao leilao = new Leilao("Playstation 3 novo");
    
    leilao.propoe(new Lance(joao, 1000.0));
    leilao.propoe(new Lance(jose, 2000.0));
    leilao.propoe(new Lance(maria,3000.0));
    
    // parte 2: acao
    Avaliador leiloeiro = new Avaliador();
    leiloeiro.avaliar(leilao);
    
    // parte 3: validacao
    double maiorEsperado = 3000;
    double menorEsperado = 1000;
    
    assertEquals(maiorEsperado, leiloeiro.getMaiorLance(), 0.00001);
    assertEquals(menorEsperado, leiloeiro.getMenorLance(), 0.00001);
    
  }
  
  
}
