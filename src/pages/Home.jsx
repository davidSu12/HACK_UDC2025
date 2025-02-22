import { Header } from "../components/Header.jsx";
import { Footer } from "../components/Footer.jsx";
import { CardContainer } from "../components/CardContainer";
import Calendar from "../components/Calendar";

export function Home() {
  return (
    <>
      <Header />
      <div className="flex items-stretch">
        <aside className="w-1/3 bg-blue-200 p-4">
          <Calendar />
        </aside>
        <main className="w-3/3 bg-blue-400 p-4">
          <h2 className="mb-3 text-4xl font-bold text-center">
            Tipos de ejercicios
          </h2>
          <CardContainer />
        </main>
        <Footer />
      </div>
    </>
  );
}
