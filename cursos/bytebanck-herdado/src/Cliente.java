
public class Cliente implements Autenticavel {

  private AutentitcacaoUtil autenticador;

  public Cliente() {
   this.autenticador = new AutentitcacaoUtil();
  }
  
  @Override
  public void setSenha(int senha) {
    this.autenticador.setSenha(senha);

  }

  @Override
  public boolean autentica(int senha) {
   return this.autenticador.autentica(senha);
  }
}
