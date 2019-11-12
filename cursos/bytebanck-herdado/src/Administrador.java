
public class Administrador extends Funcionario implements Autenticavel {

  public AutentitcacaoUtil autenticador;
  
  public Administrador() {
    this.autenticador = new AutentitcacaoUtil();
  }
  
  public double getBonificacao() {
    return super.getSalario();
  }

  @Override
  public void setSenha(int senha) {
    this.autenticador.setSenha(senha);

  }

  @Override
  public boolean autentica(int senha) {
   return this.autenticador.autentica(senha);
  }}
}
