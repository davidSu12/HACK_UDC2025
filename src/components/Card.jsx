export function Card({ titulo, descripcion }) {
  return (
    <article className="flex flex-col justify-around text-center p-4 border-2 border-black rounded-2xl bg-neutral-800">
      <h3 className="text-lg font-bold">{titulo}</h3>
      <p className="text-gray-600">{descripcion}</p>
    </article>
  );
}
