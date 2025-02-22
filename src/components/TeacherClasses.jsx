const classes = [
  {
    id: 1,
    subject: "Matemáticas Avanzadas",
    schedule: "Lunes y Miércoles - 10:00 AM",
    students: 25,
  },
  {
    id: 2,
    subject: "Álgebra Lineal",
    schedule: "Martes y Jueves - 2:00 PM",
    students: 30,
  },
  {
    id: 3,
    subject: "Cálculo Diferencial",
    schedule: "Viernes - 8:00 AM",
    students: 20,
  },
];

const TeacherClasses = () => {
  return (
    <div className="container mx-auto px-4 py-6">
      <h1 className="text-2xl font-bold text-center mb-6">Mis Clases</h1>
      <div className="grid md:grid-cols-3 gap-6">
        {classes.map((classItem) => (
          <div
            key={classItem.id}
            className="bg-white rounded-lg shadow-lg p-4 border-l-4 border-blue-500 hover:scale-105 transform transition-transform duration-300"
          >
            <h2 className="text-xl font-semibold text-gray-800 mb-2">
              {classItem.subject}
            </h2>
            <p className="text-gray-600 mb-1">📅 {classItem.schedule}</p>
            <p className="text-gray-600 mb-3">
              👨‍🎓 {classItem.students} estudiantes
            </p>
            <button className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">
              Ver Clase
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TeacherClasses;
