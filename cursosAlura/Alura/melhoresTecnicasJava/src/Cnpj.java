  public class Cnpj {
        private String valor;

        public Cnpj(String valor) {
            this.valor = valor;
        }

        public String getValor() {
            return valor;
        }
        public boolean ehValido() {
            return primeiroDigitoVerificador() == primeiroDigitoCorreto()
                    && segundoDigitoVerificador() == segundoDigitoCorreto();
        }
        private int primeiroDigitoVerificador() {
            // Extrai o primeiro dígito verificador do CNPJ armazenado
            // no atributo valor
        }
        private int primeiroDigitoCorreto() {
            // Calcula o primeiro dígito verificador correto para
            // o CNPJ armazenado no atributo valor
        }
        private int segundoDigitoVerificador() {
            // Extrai o segundo dígito verificador do CNPJ armazenado
            // no atributo valor
        }
        private int segundoDigitoCorreto() {
            // Calcula o segundo dígito verificador correto para
            // o CNPJ armazenado no atributo valor
        }
    }