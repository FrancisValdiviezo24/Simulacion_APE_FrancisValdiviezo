package controlador;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import modelo.Estado;
import modelo.Resultado;
import modelo.ModeloSIR;

// Contiene los métodos de la simulación y coordina la exportación.
public class ControladorSimulacion {
    private Random aleatorio;
    private ModeloSIR parametros;

    public void ejecutar(ModeloSIR parametros, long semilla, Path archivo) throws IOException {
        validarParametros(parametros);
        this.parametros = parametros;
        aleatorio = new Random(semilla);
        List<Resultado> resultados = simular();
        new ExportadorCSV().exportar(resultados, archivo);
    }

    private void validarParametros(ModeloSIR datos) {
        if (datos == null || datos.poblacion <= 0) {
            throw new IllegalArgumentException("La población debe ser mayor que cero.");
        }
        if (datos.infectadosIniciales < 0 || datos.infectadosIniciales > datos.poblacion) {
            throw new IllegalArgumentException("Los infectados iniciales deben estar entre 0 y la población.");
        }
        if (!Double.isFinite(datos.beta) || datos.beta < 0 || datos.beta > 1
                || !Double.isFinite(datos.gamma) || datos.gamma < 0 || datos.gamma > 1) {
            throw new IllegalArgumentException("Beta y gamma deben estar entre 0 y 1.");
        }
        if (datos.tiempoSimulacion < 0 || datos.tiempoSimulacion == Integer.MAX_VALUE) {
            throw new IllegalArgumentException("El tiempo debe estar entre 0 y 2147483646.");
        }
    }

    private List<Resultado> simular() {
        Estado[] poblacion = crearPoblacion();
        List<Resultado> resultados = new ArrayList<>();

        // Incluye el estado inicial y el final: tiempoSimulacion + 1 registros.
        for (int tiempo = 0; tiempo <= parametros.tiempoSimulacion; tiempo++) {
            resultados.add(contarEstados(tiempo, poblacion));
            if (tiempo < parametros.tiempoSimulacion) {
                poblacion = avanzarPaso(poblacion);
            }
        }
        return resultados;
    }

    private Estado[] crearPoblacion() {
        Estado[] poblacion = new Estado[parametros.poblacion];
        for (int i = 0; i < parametros.poblacion; i++) {
            poblacion[i] = Estado.SUSCEPTIBLE;
        }

        int seleccionados = 0;
        while (seleccionados < parametros.infectadosIniciales) {
            int persona = aleatorio.nextInt(parametros.poblacion);
            if (poblacion[persona] == Estado.SUSCEPTIBLE) {
                poblacion[persona] = Estado.INFECTADO;
                seleccionados++;
            }
        }
        return poblacion;
    }

    private Estado[] avanzarPaso(Estado[] poblacion) {
        Estado[] siguiente = poblacion.clone();

        for (int persona = 0; persona < parametros.poblacion; persona++) {
            if (poblacion[persona] == Estado.INFECTADO) {
                // Un contacto por infectado y por paso, excluyendo a sí mismo.
                if (parametros.poblacion > 1) {
                    int contacto = aleatorio.nextInt(parametros.poblacion - 1);
                    if (contacto >= persona) {
                        contacto++;
                    }
                    if (poblacion[contacto] == Estado.SUSCEPTIBLE
                            && aleatorio.nextDouble() < parametros.beta) {
                        siguiente[contacto] = Estado.INFECTADO;
                    }
                }

                if (aleatorio.nextDouble() < parametros.gamma) {
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
