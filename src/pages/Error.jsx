import { Header } from "../components/Header.jsx";
import { Footer } from "../components/Footer.jsx";

export function Error({ numberError }) {
  return (
    <>
      <Header />
      <main className=" min-h-screen  bg-blue-400 p-4">
        <h1 className="text-center text-8xl ">Error {numberError}</h1>
      </main>
      <Footer />
    </>
  );
}
