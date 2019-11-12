package br.com.caelum.empresa;

import java.io.InputStream;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Collection;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

import br.com.caelum.empresa.modelo.Gasto;
import training.Funcionario;

public class ImportadorDeGastos {

  private SimpleDateFormat df = new SimpleDateFormat("ddMMyyyy");

  public Collection<Gasto> importa(InputStream entrada) throws ParseException {
    Scanner leitor = new Scanner(entrada);
    Set<Gasto> gastos = new LinkedHashSet<Gasto>();


    while (leitor.hasNextLine()) {
      String line = leitor.nextLine();
      String tipoDeGasto = line.substring(0, 6);
      String dataGastoTxt = line.substring(6, 14);
      String valorTxt = line.substring(14, 23);
      String matriculaTxt = line.substring(23, 26);
      String nome = line.substring(26, 56);
      String dataNascTxt = line.substring(56);
      double valor = Double.parseDouble(valorTxt);
      int matricula = Integer.parseInt(matriculaTxt);

      Calendar dataNascimento = extractDateCalendar(dataNascTxt);

      Calendar dataDespesa = extractDateCalendar(dataGastoTxt);

      Funcionario funcionario = new Funcionario(nome, matricula, dataNascimento);
      gastos.add(new Gasto(valor, tipoDeGasto, funcionario, dataDespesa, false));
    }
    return gastos;
  }

  private Calendar extractDateCalendar(String dataNascTxt) throws ParseException {
    Calendar dataNascimento = Calendar.getInstance();
    dataNascimento.setTime(df.parse(dataNascTxt));
    return dataNascimento;
  }
}
