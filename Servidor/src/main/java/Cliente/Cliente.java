/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Cliente;
import java.io.IOException;
import java.net.Socket;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Cliente {
    
     public static void main(String[] args){
         try {
             Socket cliente = new Socket("192.168.56.1", 4500);
             
             ObjectOutputStream mensaje = new ObjectOutputStream(cliente.getOutputStream());
             mensaje.writeObject("HOLA estoy enviando este mensaje");
             
             ObjectInputStream entrada = new ObjectInputStream(cliente.getInputStream());
             
             try {
                 String mensaje2 = (String)entrada.readObject();
                 
                 System.out.println("mensaje desde el servidor " + mensaje2);
                 cliente.close();
                 
                 System.out.println("conexion cerrada");
                 
             } catch (ClassNotFoundException ex) {
                 Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
             }
             
         } catch (IOException ex) {
             Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
         }
}
}

