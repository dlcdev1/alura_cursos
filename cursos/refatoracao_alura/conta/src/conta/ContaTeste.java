package conta;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.CoreMatchers.equalTo;
import static org.junit.Assert.assertThat;

import org.junit.Test;

public class ContaTeste {

  @Test
  public void aoSacarUmValorDeUmaContaOSaldoDeveSofrerUmaSubtracadoDesseValor() {
    Conta conta = new Conta(200);
    conta.sacar(50d);
    
    assertThat(conta.getSaldo(), is(equalTo(150d)));
    
  }

  
}
