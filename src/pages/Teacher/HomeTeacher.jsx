import { Header } from "../../components/Header.jsx";
import { Footer } from "../../components/Footer.jsx";
import TeacherClasses from "../../components/TeacherClasses.jsx";

export function HomeTeacher() {
  return (
    <>
      <Header />
      <div className="max-h-screen">
        <div className="flex flex-row min-h-screen">
          <aside className="w-1/6 bg-blue-300 p-4 border-r-2 border-black">
            <h2 className="text-6xl"> Dashboard</h2>
          </aside>
          <main className="w-3/3 bg-blue-400 p-4">
            <h2 className="mb-3 text-4xl font-bold text-center"></h2>
            <TeacherClasses />
          </main>
        </div>
      </div>
      <Footer />
    </>
  );
}
