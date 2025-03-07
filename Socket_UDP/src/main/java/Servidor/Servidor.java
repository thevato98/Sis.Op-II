
package Servidor;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Servidor {
    public static void main(String[] args) throws IOException {
        ServerSocket servidor = null;
        Socket sc = null;
        final int PUERTO = 5000;
        DataInputStream in;
        DataOutputStream out;
        
        try{
            servidor = new ServerSocket(PUERTO);
            System.out.println("Servidor iniciado");
            
            while (true){
                sc = servidor.accept();
                System.out.println("cliente conectado");
                
                in = new DataInputStream (sc.getInputStream());
                out = new DataOutputStream (sc.getOutputStream());
                
                String mensaje = in.readUTF();
                System.out.println(mensaje);
                
                out.writeUTF("HOLA DESDE EL SERVIDOR");
                
                sc.close();
                System.out.println("");
            }
                
        }  catch (IOException ex) {
           
    }
    }
}