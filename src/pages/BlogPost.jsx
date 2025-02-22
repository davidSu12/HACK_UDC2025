import { Header } from "../../components/Header.jsx";
import { Footer } from "../../components/Footer.jsx";

export function BlogPost({ Blog }) {
  return (
    <>
      <Header />
      <div>
        <main className="w-3/3 bg-blue-400 p-4">
          <h1 className="mb-3 text-4xl font-bold text-center">{Blog.tittle}</h1>
          <h3>{Blog.descriptio}</h3>
          {Blog.content}
        </main>
        <Footer />
      </div>
    </>
  );
}
