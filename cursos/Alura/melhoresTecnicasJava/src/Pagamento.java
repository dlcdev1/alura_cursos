import java.util.Calendar;

public class Pagamento {
    private String pagador;
    private String cnpjPagador;
    private double valor;
    private Calendar data;
    
    public String getPagador() {
        return this.pagador;
    }
    public void setPagador(String pagador) {
        this.pagador = pagador;
    }
    public String getCnpjPagador() {
        return this.cnpjPagador;
    }
    public void setCnpjPagador(String cnpjPagador) {
        this.cnpjPagador = cnpjPagador;
    }
    public double getValor() {
        return this.valor;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }
    public Calendar getData() {
        return this.data;
    }
    public void setData(Calendar data) {
        this.data = data;
    }
}