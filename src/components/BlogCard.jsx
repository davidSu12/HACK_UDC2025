const blogPosts = [
  {
    id: 1,
    title: "Ejemplo de la entrada de un blog",
    description:
      "Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog",
    image: "",
    link: "#",
  },
  {
    id: 2,
    title: "Ejemplo de la entrada de un blog",
    description:
      "Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog",
    image: "",
    link: "#",
  },

  {
    id: 3,
    title: "Ejemplo de la entrada de un blog",
    description:
      "Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog",
    image: "",
    link: "#",
  },
  {
    id: 4,
    title: "Ejemplo de la entrada de un blog",
    description:
      "Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog Ejemplo de la entrada de un blog",
    image: "",
    link: "#",
  },
];

const BlogCard = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-center mb-6">Últimos Artículos</h1>
      <div className="grid md:grid-cols-3 gap-6">
        {blogPosts.map((post) => (
          <div
            key={post.id}
            className="bg-white rounded-lg shadow-lg overflow-hidden"
          >
            <img
              src={post.image}
              alt={post.title}
              className="w-full h-48 object-cover"
            />
            <div className="p-4">
              <h2 className="text-xl font-semibold mb-2">{post.title}</h2>
              <p className="text-gray-600 mb-4">{post.description}</p>
              <a
                href={post.link}
                className="text-blue-500 hover:underline font-bold"
              >
                Leer más →
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BlogCard;
