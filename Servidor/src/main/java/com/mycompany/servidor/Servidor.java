package com.mycompany.servidor;
import Cliente.Cliente;
import java.io.IOException;
import java.net.Socket;
import java.net.ServerSocket;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Servidor {
    
    public static void main(String[] args) {
        try {
            ServerSocket servidor = new ServerSocket(4500,50, InetAddress.getByName("0.0.0.0"));
            System.out.println("Servidor iniciado. Esperando conexiones...");
            
            while(true) { // Bucle infinito para mantener el servidor activo
                Socket clienteNuevo = servidor.accept();
                System.out.println("Cliente conectado desde: " + clienteNuevo.getInetAddress());
                
                try {
                    ObjectInputStream entrada = new ObjectInputStream(clienteNuevo.getInputStream());
                    ObjectOutputStream resp = new ObjectOutputStream(clienteNuevo.getOutputStream());
                    
                    while(true) { // Bucle para mantener la conexión con el cliente
                        try {
                            String mensaje = (String)entrada.readObject();
                            if(mensaje.equalsIgnoreCase("salir")) {
                                System.out.println("Cliente desconectado");
                                break; // Sale del bucle interno si el cliente envía "salir"
                            }
                            
                            System.out.println("Mensaje recibido: " + mensaje);
                            
                            // Contar vocales en el mensaje
                            int cantidadVocales = contarVocales(mensaje);
                            System.out.println("El mensaje contiene " + cantidadVocales + " vocales.");

                            // Enviar respuesta al cliente
                            String respuesta = "Tu mensaje tiene " + cantidadVocales + " vocales.";
                            resp.writeObject(respuesta);
                            resp.flush(); // Asegura que el mensaje se envíe inmediatamente
                            
                            System.out.println("Respuesta enviada al cliente");
                            
                        } catch (ClassNotFoundException ex) {
                            Logger.getLogger(Servidor.class.getName()).log(Level.SEVERE, null, ex);
                            break;
                        }
                    }
                    
                    clienteNuevo.close(); // Cierra la conexión con este cliente
                    
                } catch (IOException ex) {
                    System.out.println("Cliente desconectado inesperadamente");
                }
            }
            
        } catch (IOException ex) {
            Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    private static int contarVocales(String mensaje) {
        int contador = 0;
        String vocales = "aeiouAEIOU";
        
        for (char c : mensaje.toCharArray()) {
            if (vocales.indexOf(c) != -1) {
                contador++;
            }
        }
        return contador;
    }
}