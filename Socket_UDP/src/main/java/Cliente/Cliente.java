package Cliente;

import java.io.IOException;
import java.net.Socket;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Cliente {

    public static void main(String[] args) {
        final String HOST = " localhost";
        final int Puerto = 5000;
        DataInputStream in;
        DataOutputStream out;
        try {
            Socket sc = new Socket(HOST, Puerto);
            in = new DataInputStream(sc.getInputStream());
            out = new DataOutputStream(sc.getOutputStream());

            out.writeUTF("Hola desde el cliente ");
            String mensaje = in.readUTF();
            System.out.println(mensaje);
            sc.close();

        } catch (IOException ex) {
            Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
