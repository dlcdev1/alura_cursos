package training;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class testingRegex {

  public static void main(String[] args) {

    // Scanner sc = new Scanner(System.in);
    //
    // System.out.println("Informe um texto: ");
    String entradaTexto = "&nbsp;Lorem ipsum tempus vel pellentesque vivamus aenean et blandit, bibendum purus nibh magna fames nam pellentesque fermentum, massa leo aliquet bibendum elit cursus habitasse. odio viverra massa at tristique quisque aptent litora quisque elementum sem turpis arcu, ac pulvinar sapien egestas nulla rutrum pretium volutpat pharetra iaculis. varius felis pulvinar quisque arcu sem vehicula per nibh dapibus adipiscing, senectus nullam sit ac vel proin aptent pellentesque sapien ad eleifend, sollicitudin scelerisque accumsan vivamus integer tellus venenatis diam pretium. sed cubilia ipsum integer mollis in augue taciti orci, ornare potenti proin aenean etiam suscipit leo, tellus platea tortor dolor venenatis cras neque.&nbsp; Hendrerit sodales in convallis tellus tempus purus eu, pharetra vivamus curae conubia bibendum laoreet, nisi nam ornare tellus amet elit. nunc dolor hac cubilia orci fusce fringilla, lacinia aliquam vestibulum leo interdum maecenas, aliquet proin hendrerit ullamcorper donec. inceptos diam varius aliquam commodo duis ultricies, sollicitudin tortor aenean vestibulum nisl, lorem venenatis class quam sociosqu. feugiat ultrices molestie nunc ullamcorper ultricies nisi ante quis, a senectus quam cras orci phasellus felis varius, ultrices pulvinar facilisis magna fames lacinia sollicitudin. per tristique metus quisque ac habitasse pretium nullam, vitae magna curabitur lectus neque dictum, senectus pellentesque cubilia etiam velit gravida.pharetra vivamus curae conubia bibendum laoreet, nisi nam ornare tellus amet elit. nunc dolor hac cubilia orci fusce fringilla, lacinia aliquam vestibulum leo interdum maecenas, aliquet proin hendrerit ullamcorper donec. inceptos diam varius aliquam commodo duis ultricies, sollicitudin tortor aenean vestibulum nisl, lorem venenatis class quam sociosqu. feugiat ultrices molestie nunc ullamcorper ultricies nisi ante quis, a senectus quam cras orci phasellus felis varius, ultrices pulvinar facilisis magna fames lacinia sollicitudin....";
        
    System.out.println("total de caracteres entrada: " + entradaTexto.length());
    String validacao = "<(\"[^\"]*\"|'[^']*'|[^'\">])*>";

    String textForValidation = entradaTexto.replaceAll(validacao, "");
    System.out.println(textForValidation);
    System.out.println("total dos caracteres: " + textForValidation.length());

    System.out.println("==================//=================");

    
    Map<String, String> tagsMap = new HashMap<String, String>();

    tagsMap.put("&nbsp;", " ");
    tagsMap.put("&lt;", "<");
    tagsMap.put("&gt;", ">");
    tagsMap.put("&amp;", "&");
    tagsMap.put("&quot;", "\"");
    tagsMap.put("&apos;", "'");
    tagsMap.put("&cent;", "¢");
    tagsMap.put("&pound;", "£");
    tagsMap.put("&yen;", "¥");
    tagsMap.put("&euro;", "€");
    tagsMap.put("&copy;", "©");
    tagsMap.put("&reg;", "®");

    for (Entry<String, String> entry : tagsMap.entrySet()) {
      textForValidation =
          textForValidation.replaceAll(entry.getKey().toString(), entry.getValue().toString());
    }

    System.out.println(textForValidation);
    System.out.println("Total de caracteres: " + textForValidation.length());

  }

  
}
