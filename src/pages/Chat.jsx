import { Header } from "../components/Header.jsx";
import { Footer } from "../components/Footer.jsx";

export function Chat() {
  return (
    <>
      <Header />
      <div className="max-h-screen">
        <div className="flex flex-row min-h-screen">
          <aside className="w-1/6 bg-blue-300 p-4 border-r-2 border-black"></aside>
          <main className="w-3/3 bg-blue-400 p-4"></main>
        </div>
      </div>
      <Footer />
    </>
  );
}
