/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.javapython;
import java.io.*;
import java.net.*;
public class JavaPython {

static final int PUERTO=5000;
    public JavaPython(){
        try {
            System.out.println("inicializando Servidor");
            ServerSocket socketServidor = new ServerSocket(PUERTO);
            System.out.println("Escucho el puerto" + PUERTO);
            System.out.println("esperando conexiones de clientes ");
            
            for (int numeroCliente = 0; numeroCliente <3; numeroCliente++){
                Socket socketCliente=socketServidor.accept();
                System.out.println("sirvo al cliente" +numeroCliente + "en el puerto de comunicación" +socketCliente.getPort());
                OutputStream mensajeParaCliente= socketCliente.getOutputStream();
                DataOutputStream flujoSecuencial=new DataOutputStream(mensajeParaCliente);
                flujoSecuencial.writeUTF("bienvenido cliente" + numeroCliente+".\nEl puerto de escucha es el numero" +socketCliente.getLocalPort()+"y el puerto de comunicacion bidireccional es "+socketCliente.getPort());
                socketCliente.close();
            }
            
            System.out.println("demasiados clientes ");
            System.out.println("solamente aceptamos 3 clientes");
        } catch (Exception e) {
            
        System.out.println( e.getMessage());
    }
}

public static void main(String[] arg) {
    JavaPython miServidor=new JavaPython();

 
    }

}
