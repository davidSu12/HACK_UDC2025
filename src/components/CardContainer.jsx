import { Card } from "./Card";
export function CardContainer() {
  const tiposEjercicios = [
    { titulo: "Aritmetica", descripcion: "Ejercicios básicos de aritmética" },
    { titulo: "Sumas", descripcion: "Suma de números naturales y enteros" },
    { titulo: "Restas", descripcion: "Restas con y sin llevadas" },
    { titulo: "Algebra", descripcion: "Ecuaciones y expresiones algebraicas" },
    {
      titulo: "Division",
      descripcion: "División de números enteros y decimales",
    },
    { titulo: "Prueba", descripcion: "Ejercicio de prueba 1" },
    { titulo: "Prueba", descripcion: "Ejercicio de prueba 2" },
  ];
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 p-4">
      {tiposEjercicios.map((ejercicio, index) => (
        <Card
          key={index}
          titulo={ejercicio.titulo}
          descripcion={ejercicio.descripcion}
        />
      ))}
    </div>
  );
}
