package br.com.caelum.leilao.teste;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.List;

import br.com.caelum.leilao.builder.CriadorDeLeilao;
import br.com.caelum.leilao.dominio.Lance;
import br.com.caelum.leilao.dominio.Leilao;
import br.com.caelum.leilao.dominio.Usuario;
import br.com.caelum.leilao.servico.Avaliador;

public class AvaliadorTest {

  private List<Lance> maiores;

  private Avaliador leiloeiro;
  private Usuario joao;
  private Usuario jose;
  private Usuario maria;
  private Usuario pedro;
  private Usuario paulo;
  private Usuario silvia;

  @Before
  public void criaAvalidador() {
    this.leiloeiro = new Avaliador();
    this.joao = new Usuario("João");
    this.jose = new Usuario("Jose");
    this.maria = new Usuario("Maria");
    this.pedro = new Usuario("Pedro");
    this.paulo = new Usuario("Paulo");
    this.silvia = new Usuario("Silvia");
    System.out.println("Inicio do metodo");
  }
  @After
  public void finalizar() {
    System.out.println("Fin");
  }
  
  @BeforeClass
  public static void testandoBeforeClass() {
    System.out.println("before class");
  }
  
  @AfterClass
  public static void testandoAfterClass() {
    System.out.println("afeter class");
  }
  
  @Test(expected=RuntimeException.class)
  public void naoDeveAvaliarLeiloesSemNenhumLanceDado() {
      Leilao leilao = new CriadorDeLeilao().para("Playstation 3 novo").constroi();
      leiloeiro.avaliar(leilao);
      Assert.fail();
  }
  
  @Test
  public void deveEntenderLancesEmOrdemCrescente() {

    // parte 1: cenario

    Leilao leilao = new CriadorDeLeilao().para("Playstation 3 novo")
        .lance(joao, 250.0)
        .lance(jose, 300.0)
        .lance(maria, 400.0)
        .constroi();

    // parte 2: acao
    leiloeiro.avaliar(leilao);

    // parte 3: validacao
    double maiorEsperado = 400;
    double menorEsperado = 250;

    assertEquals(maiorEsperado, leiloeiro.getMaiorLance(), 0.00001);
    assertThat(leiloeiro.getMaiorLance(), equalTo(maiorEsperado));
    assertThat(leiloeiro.getMenorLance(), equalTo(menorEsperado));

  }

  @Test
  public void deveEntenderLeilaoComApenasUmLance() {

    Leilao leilao = new Leilao("Playstation 3 novo");
    leilao.propoe(new Lance(joao, 1000.0));

    leiloeiro.avaliar(leilao);

    assertEquals(1000.0, leiloeiro.getMaiorLance(), 0.00001);
    assertEquals(1000.0, leiloeiro.getMenorLance(), 0.00001);

  }

  @Test
  public void deveEncontrarOsTresMaioresLances() {

    Leilao leilao = new CriadorDeLeilao().para("Playstation 3 novo")
        .lance(joao, 100.0)
        .lance(maria, 200.0)
        .lance(joao, 300.0)
        .lance(maria, 400.0)
        .constroi();
    
    leiloeiro.avaliar(leilao);

    List<Lance> maiores = leiloeiro.getMaiores();

    assertEquals(4, maiores.size());
    assertEquals(400, maiores.get(0).getValor(), 0.00001);
    assertEquals(300, maiores.get(1).getValor(), 0.00001);
    assertEquals(200, maiores.get(2).getValor(), 0.00001);

  }

  @Test
  public void testarLancesDeLeilaoAleatoriamenteEVerificarOmaiorEOmenor() {

    Leilao leilao = new CriadorDeLeilao().para("Playstation 4 novo")
        .lance(joao, 200.0)
        .lance(maria, 450)
        .lance(pedro, 120.0)
        .lance(jose, 700.0)
        .lance(paulo, 630)
        .lance(silvia, 230)
        .constroi();
    
    leiloeiro.avaliar(leilao);

    assertEquals(700, leiloeiro.getMaiorLance(), 0.00001);
    assertEquals(120, leiloeiro.getMenorLance(), 0.00001);

  }

  @Test
  public void testarLancesNaOrdemCrescente() {

    Leilao leilao = new CriadorDeLeilao().para("Smarthphone")
        .lance(joao, 400.)
        .lance(maria, 300.0)
        .lance(pedro, 200.0)
        .lance(silvia, 100.0)
        .constroi();

    leiloeiro.avaliar(leilao);

    List<Lance> maiores = leiloeiro.getMaiores();

    assertEquals(4, maiores.size());
    assertEquals(400, maiores.get(0).getValor(), 0.00001);
    assertEquals(300, maiores.get(1).getValor(), 0.00001);
    assertEquals(200, maiores.get(2).getValor(), 0.00001);
    assertEquals(100, maiores.get(3).getValor(), 0.00001);
  }

}
