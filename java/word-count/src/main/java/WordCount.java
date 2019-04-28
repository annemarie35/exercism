import java.util.HashMap;
import java.util.Map;

public class WordCount {
    public Map<String, Integer> phrase(String sentence) {

        Map <String, Integer> compteMots = new HashMap<>();

        String cleansentence =  sentence.toLowerCase().replaceAll("[^A-Za-z0-9]", "");

        compteMots.put("word", 1);
        return compteMots;
    }

}