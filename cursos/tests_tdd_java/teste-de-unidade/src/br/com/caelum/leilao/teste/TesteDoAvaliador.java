package br.com.caelum.leilao.teste;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Test;

import java.util.List;

import br.com.caelum.leilao.dominio.Lance;
import br.com.caelum.leilao.dominio.Leilao;
import br.com.caelum.leilao.dominio.Usuario;
import br.com.caelum.leilao.servico.Avaliador;

public class TesteDoAvaliador {
  
  private List<Lance> maiores;

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
  public void deveEntenderLeilaoComApenasUmLance() {
    Usuario joao = new Usuario("João");
    
    Leilao leilao = new Leilao("Playstation 3 novo");
    
    leilao.propoe(new Lance(joao, 1000.0));
    
    Avaliador leiloeiro = new Avaliador();
    leiloeiro.avaliar(leilao);
    
    assertEquals(1000.0, leiloeiro.getMaiorLance(), 0.00001);
    assertEquals(1000.0, leiloeiro.getMenorLance(), 0.00001);
    
  }
  
  @Test
  public void deveEncontrarOsTresMaioresLances() {
    
    Usuario joao = new Usuario("João");
    Usuario maria = new Usuario("Maria");
    Leilao leilao = new Leilao("Playstation 3 novo");
    
    leilao.propoe(new Lance(joao, 100.00));
    leilao.propoe(new Lance(maria, 200.00));
    leilao.propoe(new Lance(joao, 300.00));
    leilao.propoe(new Lance(joao, 400.00));
    
    Avaliador leiloeiro = new Avaliador();
    leiloeiro.avaliar(leilao);

    List<Lance> maiores = leiloeiro.getMaiores();
    
    assertEquals(3,  maiores.size());
    assertEquals(400, maiores.get(0).getValor(), 0.00001);
    assertEquals(300, maiores.get(1).getValor(), 0.00001);
    assertEquals(200, maiores.get(2).getValor(), 0.00001);
    
  }
  
  @Test
  public void testarLancesDeLeilaoAleatoriamenteEVerificarOmaiorEOmenor() {
    
    Usuario joao = new Usuario("João");
    Usuario maria = new Usuario("maria");
    Usuario pedro = new Usuario("pedro");
    Usuario jose = new Usuario("jose");
    Usuario paulo = new Usuario("paulo");
    Usuario silvia = new Usuario("silvia");
    
    Leilao leilao = new Leilao("Playstation 4 novo");
    
    leilao.propoe(new Lance(joao, 200));
    leilao.propoe(new Lance(maria, 450));
    leilao.propoe(new Lance(pedro, 120));
    leilao.propoe(new Lance(jose, 700));
    leilao.propoe(new Lance(paulo, 630));
    leilao.propoe(new Lance(silvia, 230));

    Avaliador leiloeiro = new Avaliador();
    leiloeiro.avaliar(leilao);
    
    assertEquals(700, leiloeiro.getMaiorLance(), 0.00001);
    assertEquals(120, leiloeiro.getMenorLance(), 0.00001);
    
  }
  
  @Test
  public void testarLancesNaOrdemCrescente() {
    
    Usuario joao = new Usuario("João");
    Usuario maria = new Usuario("maria");
    Usuario pedro = new Usuario("pedro");
    Usuario silvia = new Usuario("silvia");
    
    Leilao leilao = new Leilao("Smarthphone novo");
    
    leilao.propoe(new Lance(joao, 400));
    leilao.propoe(new Lance(maria, 300));
    leilao.propoe(new Lance(pedro, 200));
    leilao.propoe(new Lance(silvia, 100));
    
    Avaliador leiloeiro = new Avaliador();
    leiloeiro.avaliar(leilao);
    
    List<Lance> maiores = leiloeiro.getMaiores();
    
    assertEquals(4, maiores.size());
    assertEquals(400, maiores.get(0).getValor(), 0.00001);
    assertEquals(300, maiores.get(1).getValor(), 0.00001);
    assertEquals(200, maiores.get(2).getValor(), 0.00001);
    assertEquals(100, maiores.get(3).getValor(), 0.00001);
  }
  
}
