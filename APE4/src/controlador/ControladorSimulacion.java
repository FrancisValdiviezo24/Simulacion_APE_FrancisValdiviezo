package controlador;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import modelo.Estado;
import modelo.Resultado;
import static modelo.ModeloSIR.*;

// Contiene los métodos de la simulación y coordina la exportación.
public class ControladorSimulacion {
    private Random aleatorio;

    public void ejecutar(long semilla, Path archivo) throws IOException {
        aleatorio = new Random(semilla);
        List<Resultado> resultados = simular();
        new ExportadorCSV().exportar(resultados, archivo);
    }

    private List<Resultado> simular() {
        Estado[] poblacion = crearPoblacion();
        List<Resultado> resultados = new ArrayList<>();

        // Incluye el estado inicial (0) y el final (100): 101 registros.
        for (int tiempo = 0; tiempo <= TIEMPO_SIMULACION; tiempo++) {
            resultados.add(contarEstados(tiempo, poblacion));
            if (tiempo < TIEMPO_SIMULACION) {
                poblacion = avanzarPaso(poblacion);
            }
        }
        return resultados;
    }

    private Estado[] crearPoblacion() {
        Estado[] poblacion = new Estado[POBLACION];
        for (int i = 0; i < POBLACION; i++) {
            poblacion[i] = Estado.SUSCEPTIBLE;
        }

        int seleccionados = 0;
        while (seleccionados < INFECTADOS_INICIALES) {
            int persona = aleatorio.nextInt(POBLACION);
            if (poblacion[persona] == Estado.SUSCEPTIBLE) {
                poblacion[persona] = Estado.INFECTADO;
                seleccionados++;
            }
        }
        return poblacion;
    }

    private Estado[] avanzarPaso(Estado[] poblacion) {
        Estado[] siguiente = poblacion.clone();

        for (int persona = 0; persona < POBLACION; persona++) {
            if (poblacion[persona] == Estado.INFECTADO) {
                // Un contacto por infectado y por paso, excluyendo a sí mismo.
                int contacto = aleatorio.nextInt(POBLACION - 1);
                if (contacto >= persona) {
                    contacto++;
                }
                if (poblacion[contacto] == Estado.SUSCEPTIBLE
                        && aleatorio.nextDouble() < BETA) {
                    siguiente[contacto] = Estado.INFECTADO;
                }

                if (aleatorio.nextDouble() < GAMMA) {
                    siguiente[persona] = Estado.RECUPERADO;
                }
            }
        }
        return siguiente;
    }

    private Resultado contarEstados(int tiempo, Estado[] poblacion) {
        int susceptibles = 0;
        int infectados = 0;
        int recuperados = 0;

        for (Estado estado : poblacion) {
            switch (estado) {
                case SUSCEPTIBLE: susceptibles++; break;
                case INFECTADO: infectados++; break;
                case RECUPERADO: recuperados++; break;
            }
        }
        return new Resultado(tiempo, susceptibles, infectados, recuperados);
    }
}
