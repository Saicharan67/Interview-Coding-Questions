import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class CaesarCipher {

    public static String Decrypt(String ciphertext, int shift) {
        String decryptMessage = "";
        for (int i = 0; i < ciphertext.length(); i++)

        {
            // Shift one character at a time
            char alphabet = ciphertext.charAt(i);
            // if alphabet lies between a and z
            if (alphabet >= 'a' && alphabet <= 'z') {
                // shift alphabet
                alphabet = (char) (alphabet - shift);

                // shift alphabet lesser than 'a'
                if (alphabet < 'a') {
                    // reshift to starting position
                    alphabet = (char) (alphabet - 'a' + 'z' + 1);
                }
                decryptMessage = decryptMessage + alphabet;
            } else {
                decryptMessage = decryptMessage + alphabet;
            }
        }

        return decryptMessage;
    }

    public static void main(String args[]) {

        int shift = 3;
        Scanner sc2 = null;
        try {
            sc2 = new Scanner(new File("Decrypt.txt"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        while (sc2.hasNextLine()) {
            Scanner s2 = new Scanner(sc2.nextLine());
            while (s2.hasNext()) {
                String s = s2.next();
                System.out.println(Decrypt(s, shift));
            }
        }

    }
}