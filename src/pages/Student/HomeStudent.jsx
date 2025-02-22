import { Header } from "../../components/Header.jsx";
import { Footer } from "../../components/Footer.jsx";
import { CardContainer } from "../../components/CardContainer.jsx";

export function HomeStudent() {
  return (
    <>
      <Header />
      <div className="flex flex-row min-h-screen">
        <aside className="w-1/6 bg-blue-200 p-4 border-r-2 border-black"></aside>
        <main className="w-3/3 bg-blue-400 p-4">
          <h2 className="mb-3 text-4xl font-bold text-center">
            Tipos de ejercicios
          </h2>
          <CardContainer />
        </main>
      </div>
      <Footer />
    </>
  );
}
